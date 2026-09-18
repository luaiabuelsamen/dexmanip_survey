# rotateit_2023 — General In-Hand Object Rotation with Vision and Touch (Qi, Yi, Suresh, Lambeta, Ma, Calandra, Malik, CoRL 2023)

sources: papers/md/rotateit_2023.md [sha256 6f0d5140] ; no code

## One-line contribution
A two-stage privileged-learning system (oracle policy with ground-truth shape/physics, distilled to a visuotactile transformer) that rotates diverse objects about arbitrary axes using only Allegro-hand fingertips, fusing depth vision, discretized tactile contact location, and proprioception.

## Setting
- hand(s): AllegroHand (Wonik Robotics), 4 fingers x 4 DoF = 16 joints ("Hardware Setup", Sec. 4); arm: not stated; single-handed (no bimanual mention).
- simulator / physics: IsaacGym [79] (Sec. 4, "Simulation Setup"); sim frequency 200 Hz, control frequency 20 Hz (Appendix B); 400 control steps per episode = 20 s; 32768 parallel environments distributed on 4 GPUs (Appendix B, "Simulation Setup"). GPU model and wall-clock training time: not stated.
- observation: oracle policy — proprioception p_t = [q_{t-2:t}, a_{t-3:t-1}] in R^96 plus privileged encoding z_t in R^40 (Sec. 3.1). Visuotactile policy — object depth image (60x60, encoded to 32-dim via 4-layer ConvNet + global average pooling), discretized tactile contact location (N_c x 9 array: 8-dim discretized 2D location + finger index, per contact, MLP-encoded to 32-dim and averaged), joint positions q_t, and previous action a_{t-1} (Sec. 3.2, Appendix B "Network Architecture").
- action space: PD-controller joint position targets a_t in R^16, sent at 20 Hz, converted to torque via PD controller at 300 Hz (Sec. 4, "Hardware Setup"). PD stiffness randomized [2.9, 3.1], damping [0.09, 0.11] (Table 6).
- objects / data: curated set from EGAD [30], Google Scanned Objects [31], YCB [32], ContactDB [33]; "hundreds of objects" (Sec. 3.1); filtered to width/depth/height aspect ratio < 2.0 (Sec. 4, "Object Set"; Fig. 3 caption says "larger than 2.0" is excluded). 15 held-out OOD objects used for generalization eval (Fig. 8). 20 objects (16 train / 4 test) used for the shape-decoding probe (Sec. 5.3).

## Method
- paradigm: RL (teacher/oracle with privileged info) -> supervised distillation to a sensorimotor transformer (rapid-motor-adaptation style, citing [5,6,7]).
- algorithm: PPO [75] for oracle policy (policy and critic share weights plus a linear value head); Adam [78] for visuotactile transformer distillation, minimizing L2 regression loss between z_t and predicted z_hat_t (and between a_t and a_hat_t) (Sec. 3.2).
- teacher-student / privileged->vision distillation: yes. Privileged info z_t = [z_t^phys (8-dim, from object mass, center of mass, coefficient of friction, scale, restitution [7-dim physics vector] concatenated with 10-dim pose [position, quaternion orientation, angular velocity], projected via 3-layer MLP [256,128,8]), z_t^shape (32-dim PointNet [72] encoding of N_p=100 sampled mesh points, 3-layer MLP [32,32,32] with max pooling)] (Sec. 3.1, Table 7).
- domain randomization (Table 6, exact ranges as given): Object Scale [0.46, 0.68]; Mass [0.01, 0.25] kg; Center of Mass [-1.00, 1.00] cm; Coefficient of Friction [0.3, 3.0]; External Disturbance (2, 0.25) [force scale 2*m decayed by 0.9 every 80 ms, resampled each timestep with probability 0.25, "following [1]"]; PD Controller Stiffness [2.9, 3.1]; PD Controller Damping [0.09, 0.11]. Vision randomization (Table 5, "Same Noise as training" row): camera position noise +N(0, 0.01) m, camera RPY noise +N(0, 0.03) rad, camera FOV ~U(52, 58) deg, segmentation noise probability 0.2, segmentation failure probability 0.05.
- key trick(s): explicit object-shape (point-cloud) conditioning of the oracle policy (ablated in Table 1/Fig. 7/Fig. 8b as the biggest single improvement); discretized 2D contact-location touch representation chosen specifically to close the sim-to-real gap (Fig. 4); curriculum on the rotation-penalty weight (see reward block); visuotactile transformer with 2 layers, feature dim 32, 2 attention heads (Appendix B).

## A. Embodiment block
- hand: AllegroHand (Wonik Robotics [42]), 4 fingers x 4 DoF, 16 joints; commands at 20 Hz, PD-converted to torque at 300 Hz.
- arm/floating base: not stated.
- bimanual: no (single hand).
- simulator + version: IsaacGym [79] (version not stated).
- physics engine: IsaacGym's own (not separately named).
- sim timestep / control rate: simulation frequency 200 Hz, control frequency 20 Hz (Appendix B).
- parallel envs: 32768, distributed on 4 GPUs (Appendix B).
- GPU model / wall-clock training time: not stated.

## B. Learning block
- paradigm: RL (PPO) for the oracle policy, then supervised distillation (regression) to a transformer-based sensorimotor policy; the multi-axis policy (Sec. 5.5) additionally uses "the imitation learning objective with the corresponding single-axis oracles" — authors note "the policy does not converge when training with only reinforcement learning" for the multi-axis case.
- algorithm/implementation: PPO [75]; policy/value weights shared with a linear value-projection layer; PPO collects from 32768 envs with 10 agent steps each (0.5 s), 5 epochs, batch size 32768, learning rate 5e-3 (Appendix B, "Optimization Details"). Visuotactile transformer trained with Adam, learning rate 3e-4.
- teacher-student: yes, oracle (privileged, ground-truth shape+physics) -> visuotactile student; privileged info defined exactly in block A above.
- observation vector (as stated, not from code — no code source): oracle p_t = [q_{t-2:t}, a_{t-3:t-1}] in R^96, q_t in R^16 (joint positions); z_t in R^40 = [z_t^phys in R^8, z_t^shape in R^32]. Student: f_t = concat(f_t^depth (32-dim), f_t^touch (32-dim), q_t, a_{t-1}), fed as a sequence f_T = {f_{t-k},...,f_t} to the transformer.
- action space: PD controller joint-position targets a_t in R^16 (position targets, not torque or residual).
- domain randomisation: see Table 6 list under block A/Method above (exact ranges given there).

## C. Reward / objective block (quoted verbatim from the paper)
- "The object rotation task is defined as r_rotr = max(min(ω·k, r_max), r_min) where ω is the object's angular velocity and k is the desired rotation axis in the hand-centric axis."
- "we add a rotation penalty term r_rotp = ‖ω×k‖_1."
- "r_pose = −‖q − q_init‖²₂ is the hand pose deviation penalty"
- "r_torque = −‖τ‖²₂ is the torque penalty"
- "r_work = −τ^T q̇ is the energy consumption penalty"
- "r_linvel = −‖v‖²₂ is the object linear velocity penalty"
- Weights (verbatim, Appendix B "Reward Hyperparameter"): "We use r_max = 0.5, r_min = −0.5, λ_torque = −0.1, λ_linvel = −0.3, λ_work = −2.0, and λ_rotp = −0.1." (λ_pose weight is not given a numeric value in the source text.)
- Curriculum: "if we apply λ_rotp = −0.1 at the start of training, the policy will only learn to stably hold the objects. Therefore we set this coefficient to be 0 at the beginning and then linearly decrease it to −0.1 using curriculum learning [84]."
- No separate code source exists for this key (code/md/rotateit_2023.md absent) — reward terms could not be cross-checked against an implementation.
- Multi-axis stage (Sec. 5.5): "we augment the observation space with k and train it with the reward defined in Section 3.1 and the imitation learning objective with the corresponding single-axis oracles" — the IL loss itself is not spelled out numerically.

## D. Contact / penetration handling
Not addressed as a penalty. The paper measures/uses contact only as a sensing signal: "In simulation, we directly parse the contact position provided by the simulator, project it onto a 2D plane in fingertip frame, and discretize it to 8 locations" (Sec. 3.2). No interpenetration penalty or contact-solver settings are given; no mention of penetration measurement.

## E. Evaluation block
- success/metrics (Sec. 4, "Evaluation Metric", using definitions from [7]):
  - "Time-to-Fall (TTF). The average length of the episode before the object falls out of the hand. This value is normalized by the maximum episode length (20 s)."
  - "Rotation Reward (RotR). This is the average rotation reward ω·k of an episode in simulation."
  - "Rotation Penalty (RotP). This is the average rotation penalty per timestep ω×k."
  - "Radians Rotated (Rotations). The rotation (in radians) achieved by the policy with respect to the desired axis. This metric is only used in the real world experiments."
- episode termination: "We reset the episode if the objects fall below 13.5 cm with respect to the hand" (Appendix B).
- eval episode/seed counts: not stated (Table 1/2/3/4 report mean ± std but do not state N).
- sim vs real: Tables 1-4 and Figs 6-9 are simulation; Fig. 10 / Sec. 5.4 are real-world (RotateIt vs Hora [7] on 6 objects: Cocoon, Squishy, Baseball, Puzzle, Box, Stego; rotations over x-axis, RotateIt e.g. 12.71±1.29 vs Hora 0.54±0.39 for Cocoon, per Fig. 10 table). Real-world trial counts: not stated.
- baselines: Hora [7] (re-run/compared directly, Table 1 and Fig. 10); an ablation "w/o shape" (own method without point cloud, Table 1); ablations without vision/touch/transformer (Table 2, Table 4, Fig. 6-8) are the authors' own variants, not external baselines.
- headline numbers: Table 1 — Oracle RotR 125.23±16.24 (x), 118.26±13.20 (y), 140.90±17.26 (z) vs Hora [7] 79.13±11.22 (x), 82.25±14.21 (y), 99.83±11.72 (z). Table 3 — multi-axis policy on par with single-axis oracles (e.g. +x: single 110.19±8.26 vs multi 105.21±9.27). Fig. 8: OOD drop 8% (oracle w/ point cloud) vs 22.6% (w/o) for shape; 15.4% (visuotactile) vs 41.6% (proprioception-only) for sensing.

## F. Reproducibility
Code released: not stated (no GitHub/checkpoint/release statement found in the source text; project page URL given is https://haozhi.io/rotateit/, described only as hosting videos). code/md/rotateit_2023.md does not exist for this key, so no implementation could be checked against the paper's claims.

## Limitations stated by the authors (Sec. 6, verbatim excerpts)
"We assume the objects are not too long (e.g. a pencil or a screwdriver) and are within the mechanical limit of the robot hand." "Our method is not able to utilize real-world experiences during deployment since it is frozen after training." "There are also various ways to improve the touch processing system since we only use the low-dimensional contact location as the input and do not utilize the full information output by the omnidirectional image-based tactile sensor."

## Quotable claims (verbatim, with section)
- "Using proprioception only will lead to a 41% performance drop while using vision and touch can improve it to 15% drop." (Sec. 5.2)
- "Binary contact does not provide additional value compared to NoTouch, since it is already contained in our proprioceptive history. We also find using discretized contact locations can match the performance of using full contact in our task." (Table 2 caption)
- "Hora [7] is not able to finish this task and does not learn finger-gaiting to rotate the object, while RotateIt can." (Fig. 10 caption)
- Object/hand orientation relative to gravity (palm-up vs palm-down): not stated. Whether the hand is fixed or arm-mounted: not stated.
- Multi-axis rotation about arbitrary axes: Sec. 5.5 trains one policy over "six principle axes" (+/-x, +/-y, +/-z, Table 3); the abstract and website are said to show rotation "including but not limited to, the three canonical axes" (Fig. 1 caption / Introduction), but no quantitative arbitrary-axis (non-principal) results are given in the parsed text.

## Notes for the survey
Feeds: embodiment/reward-comparison tables (exact PPO reward weights are rare and fully quoted here); the sensor-fusion architecture section (vision+touch+proprioception transformer design); the domain-randomization comparison table. Table 4 in the source markdown is flattened by the PDF extraction and rows/columns appear misaligned (e.g. the "Conv"/blank-modality rows are hard to attribute unambiguously) — treat any number pulled from Table 4 beyond the ones quoted above as unverified. Contradicts/complements hora_2023 ([7], same hand, same evaluation metrics, no vision/touch) — direct baseline in Table 1 and Fig. 10. No penetration handling here, unlike papers that report interpenetration statistics; note for the survey's contact-handling comparison column that this is a "not addressed" case.
