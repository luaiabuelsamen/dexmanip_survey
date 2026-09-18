# dexmv_2021 — DexMV: Imitation Learning for Dexterous Manipulation from Human Videos (Qin, Wu, Liu, Jiang, Yang, Fu, Wang; ECCV 2022)

sources: papers/md/dexmv_2021.md [sha256 9b2e0e52] ; code/md/dexmv_2021.md [commit d857c16e]

## One-line contribution
A paired computer-vision/simulation platform and a two-stage "demonstration translation"
pipeline (task-space-vector hand-motion retargeting + inverse-dynamics action estimation) turn
human video of manipulating YCB objects into state-action demonstrations for an Adroit hand,
which then augment TRPO-based RL (DAPG/SOIL/GAIL+) to solve relocate/pour/place-inside tasks
that pure RL cannot (Sec. 6-8, Table 1, Fig. 7).

## Setting
- hand(s): Adroit Robotic Hand, "24 revolute joint and 1 free joint, which leads to 24+1*6 = 30
  DoF" (Sec. 6); open-source MuJoCo model used (Appendix C, footnote to vikashplus/Adroit). No
  arm; single hand only; single-handed tasks throughout.
- simulator / physics: MuJoCo [85]; "timestep set to 0.002 and frame skip set to 5"; "same
  contact friction parameters following the setting in the literature [65]" i.e. DAPG (Appendix
  C). #envs / GPU / wall-clock not stated.
- observation: state-based, task-specific. Relocate: "joint angles of adroit robotic hand;
  global position of adroit hand's root; object position; target position" — "39-dim" (Appendix
  C.1); code (`ycb_relocate_env.py:_get_observations`) confirms
  `concatenate([qp, palm_pos-obj_pos, palm_pos-target_pos, obj_pos-target_pos])`. Pour/Place
  Inside add a quaternion for object orientation (Appendix C.2-C.3); code
  (`mug_pour_water_env.py`, `mug_place_object_env.py`) matches: qpos[:30] plus three
  palm/object/mug relative vectors plus obj_quat. A 48x48 visual-observation path also exists in
  code (`ycb_relocate_env.py:_get_visual_observations`) but is not the main-experiment
  observation.
- action space: "motor command of 30 actuators... The first 6 motors control the global position
  and orientation of the robot while the last 24 motors control the fingers," normalized to
  (-1,1) (Appendix C) — joint position/torque-normalized targets, not raw torque.
- objects / data: YCB objects [15]. Relocate uses 5 objects (mustard bottle, sugar box, tomato
  soup can, large clamp, mug), Pour uses a mug + container, Place Inside uses a banana + mug.
  "We collect 100 demonstrations per object for relocate and 100 demonstrations for pour and
  place inside" (Sec. 4). Generalization tests add 100 ShapeNet instances per category (can,
  bottle, mug, camera, cellphone) (Sec. 8.4, Appendix C.4).

## Method
- paradigm: IL-augmented RL (not pure BC): "we adopt imitation learning algorithms that
  incorporate the demonstrations into RL," specifically state-action DAPG [65] and GAIL+ [33,38],
  and state-only SOIL [64] (Sec. 7). RL baseline is TRPO [73] with identical hyperparameters
  across methods (Sec. 8, "Experiment settings").
- **human data source and size**: real RGB-D video, not a public dataset. "a cubic frame (35
  inch^3)" rig with "two RealSense D435 cameras" (top-front, top-left) recording a human
  performing each task inside the frame (Sec. 4). Collection rate: "around 100 demonstrations
  per hour" (Sec. 3); Appendix B: "each captured demonstration is about 10 seconds... it takes
  about 60 minutes to capture all 100 sequences for a task." Total: 100 demos x 7 task/object
  configurations (5 relocate objects + pour + place-inside) = 700 human video demonstrations.
- **what is extracted from video**: (i) object 6-DoF pose per frame via PVN3D [30] trained on
  YCB, using RGB + point cloud, "instance segmentation... dense voting... 6-DoF object pose
  optimized by minimizing the PnP matching error" (Sec. 5.1); (ii) human hand pose as MANO
  parameters (theta_t: 15-joint axis-angle, r_t: root, beta_t: shape) via skin
  segmentation + hand detection + a pose-estimation network, refined per-frame by minimizing
  2D reprojection + depth-rendering error, optionally multi-camera (Sec. 5.2, Eq. 1). No reward
  signal, affordance map, or latent embedding is extracted — only hand and object pose
  trajectories.
- **human-to-robot mapping**: two-stage "demonstration translation" (Sec. 6), NOT a per-joint
  angle map. (1) Hand motion retargeting: solves for robot joint angles q_t frame-by-frame by
  matching 10 "Task Space Vectors" (TSVs) — palm-to-fingertip AND palm-to-middle-phalanx vectors
  — between the human (MANO forward kinematics) and robot hand, via SLSQP in NLopt, with an L2
  temporal-consistency term (alpha=8e-3), low-pass-filtered human TSVs, and warm-starting q_t
  from q_{t-1} (Eq. 2, Sec. 6.1). A fingertip-only TSV baseline is explicitly rejected because it
  "results in unexpected optimization result... the bending information of hand fingers are lost,
  leading to penetrating the object after retargeting" (Sec. 6.1) — see Block D. t=0 is
  initialized by a hand-designed heuristic phi(theta_0) that projects each MANO joint rotation
  onto the nearest robot joint axis via a manually designed weight vector w in R^15 (Appendix
  D.2), since zero-init "cannot provide reasonable outputs when the goal is far from zeros." (2)
  Robot action estimation: fits a minimum-jerk continuous trajectory q(t) to the retargeted
  joint-angle sequence (justified by human minimum-jerk motion physiology and motor wear), then
  computes torque via inverse dynamics tau(t) = f_inv(q, q', q'') and resamples at the 120 Hz
  sim rate against ~30 Hz video (Sec. 6.2). Kinematic-chain mismatch is quantified: human hand
  51 DoF (15 ball joints x 3 + 6 root) vs. robot 30 DoF (24 revolute + 6 free root) — "projecting
  a pose from a higher dimension to a lower dimension, which will lose information inevitably"
  (Table 4, Appendix D.1).
- **RL or SL**: demonstrations are used to augment on-policy RL (TRPO), not as pure supervised
  behavior cloning: "All these algorithms incorporate demonstrations with TRPO of same
  hyper-parameters" (Sec. 8). DAPG adds a demo-advantage term to the policy gradient; GAIL+ adds
  a learned discriminator reward; SOIL is state-only (learns an inverse dynamics model h_phi
  online to fill in missing actions, then behaves like DAPG) (Sec. 7.1-7.2). Reward functions are
  task-defined RL rewards (quoted from code below), not derived from video; video only supplies
  demonstration state-action(-free) trajectories.
- reward (from code, per task; paper only gives qualitative distance/lift/contact structure,
  Appendix C.1-C.3):
  `ycb_relocate_env.py::reward`: `reward = -0.1*||palm-obj||`; on contact `+0.1 + 50*lift`; once
  `lift > 0.015`: `+2.0 - 0.5*||palm-target|| - 1.5*||obj-target||`, plus
  `1/(obj_target_distance+0.01)` if `obj_target_distance < 0.1`.
  `mug_pour_water_env.py::reward`: `-0.1*||palm-obj||`; on contact `+0.1 + 50*lift`; once
  `lift>0.06`: `+2.0 - 0.5*||palm-target|| - 1.5*obj_target_distance`, plus
  `1/max(obj_target_distance,0.03)` and `arccos(z_axis[2])*100` (upright bonus) if
  `obj_target_distance<0.05`, plus `100 * (fraction of particles in mug)`; final term
  `reward -= 0.1 * dropping_ratio` (particles neither in mug nor above container).
  `mug_place_object_env.py::reward`: `-0.1*||palm-obj||`; on contact `+0.2 + 2*lift`, and if
  lifted off table `+0.2 - 0.5*||palm - mug_top_xy|| - 1*obj_target_distance_xy`, plus vertical
  upright/proximity bonuses (`+0.5`, `+0.3`) when within 5/3 cm of the mug top; a large
  `(max_lift_height - lift) * 12` shaping term plus a hand-joint-flatness bonus once aligned; and
  compensating terms if contact/lift conditions are not met. All three match Appendix C's
  qualitative description (hand-to-object, hand/object-to-target distances, lift, orientation).
- key trick(s): TSV pair (fingertip + mid-phalanx) instead of fingertip-only retargeting (fixes
  penetration, Sec. 6.1, Fig. 4); minimum-jerk action fitting instead of finite-difference torque
  (Sec. 6.2); hindsight goal for Relocate — "we use the position of the object in the last step
  as the hindsight goal" (Appendix D.3); heuristic joint-projection initializer for retargeting
  (Appendix D.2).
- domain randomisation: object/target xy "randomized within a (-0.3,0.3) square" and target
  height in (0.15,0.25) for Relocate; mug xy in (-0.1,0.1) for Pour; object xy in (-0.15,0.15)
  for Place Inside (Appendix C.1-C.3). Robustness ablation (not training-time randomization):
  object size scaled x0.75-x1.125 and friction x0.8-x1.2, holding demonstrations fixed (Fig. 6c-d).
- contact / penetration handling: `check_contact(geoms_1, geoms_2)` (base.py, signature only —
  body not in code/md) gates the contact bonus in every reward. No penetration penalty term
  appears in any reward function. `compute_intersection_rate` exists in
  `mug_place_object_env.py` (signature only, body not extracted) — this is stated in the paper
  as measuring the "Inside Score," i.e. object-in-container volume fraction, not a
  hand-object-interpenetration metric.

## Evaluation
- metrics: Relocate — success rate, "success is defined based on the distance between object and
  target... A trial is counted as success only when the final position of the object (after 200
  steps) is within 0.1 unit length to the target," "evaluated via 100 trials for three seeds"
  (Table 1 caption, Sec. 8.1). Pour — "percentage of particles poured inside the container"
  (Sec. 4, Fig. 7b). Place Inside — "Inside Score," "volume percentage of the banana inside of
  the mug" (Sec. 4, Fig. 7d).
- headline numbers (Table 1, Relocate success %): DAPG best/tied-best on 4/5 objects — mustard
  93+/-5, tomato can 100+/-0, clamp 100+/-0, mug 100+/-0; SOIL best on sugar box 67+/-47 (DAPG
  0+/-0 on sugar box); RL-only fails on mustard (6+/-1) and sugar box (0+/-0). Pour (Fig. 7b):
  DAPG 27.2+/-18.4%, SOIL 3.5+/-3.3%, GAIL+ 3.4+/-2.5%, RL 1.3+/-0.7%. Place Inside Inside Score
  (Fig. 7d): DAPG 31.3+/-30.0, SOIL 27.9+/-26.5, GAIL+ 16.0+/-14.2, RL 3.2+/-5.6. Generalization,
  same-category Relocate (Fig. 8): DAPG e.g. mustard->bottle 68.5+/-7.0% vs RL 0.0+/-0.0%; novel
  category (tomato->camera): DAPG 47.2+/-2.5% vs RL 3.8+/-2.1%. Hand-pose-estimation ablation
  (Table 3): 2-camera + post-processing gives best MPJPE (32.5) and best downstream Relocate
  success (93.3+/-11.5%) vs 1-camera (MPJPE 41.7, success 66.7+/-57.7%).
- baselines beaten: TRPO/RL-from-scratch (author-run, same codebase) on all tasks; GAIL+ and
  SOIL are compared against DAPG as alternative demo-incorporation algorithms, not strictly
  "beaten" — DAPG wins most settings but SOIL wins sugar-box relocate and matches/exceeds DAPG on
  Place Inside's Inside Score mean (though with high variance).
- real robot? No. All numbers are simulation (MuJoCo + Adroit). Human demonstrations are real
  video but the executed/evaluated policy never runs on physical hardware — "success remains" a
  sim-only demonstration; paper makes no real-robot claim.

## Limitations stated by the authors
- Retargeting loses information because the human hand (51 DoF via MANO) has strictly more DoF
  than the Adroit robot hand (30 DoF): "projecting a pose from a higher dimension to a lower
  dimension, which will lose information inevitably" (Appendix D.1, Table 4).
- Fingertip-only retargeting causes finger interpenetration with the object post-retargeting,
  motivating the mid-phalanx TSV term instead (Sec. 6.1, Fig. 4) — noted as "more severe when the
  joint angles are close to the robot singularity."
- No ground-truth hand-pose annotations for their own captured videos: "we have no ground-truth
  pose annotation in our dataset," so hand-pose-estimation quality is validated on the external
  DexYCB dataset instead (Sec. 8.1, "Ablation on hand pose estimation").
- SOIL's online inverse-dynamics model struggles with the Pour task's water particles: "It is
  challenging to learn inverse model with water particles in this task for SOIL" (Sec. 8.2).
- Generalization to a novel object category is harder than within-category: "generalization to
  novel categories brings a larger challenge" (Sec. 8.4).

## Quotable claims (verbatim, with section)
- "the bending information of hand fingers are lost, leading to penetrating the object after
  retargeting. It becomes more severe when the joint angles are closed to the robot singularity"
  (Sec. 6.1).
- "The overall Degree-of-Freedom(DoF) of the human hand is higher than the DoF of the robot
  hand... hand motion retargeting from human to robot is projecting a pose from a higher
  dimension to a lower dimension, which will lose information inevitably" (Appendix D.1).
- "A trial is counted as success only when the final position of the object (after 200 steps) is
  within 0.1 unit length to the target" (Table 1 caption / Sec. 8.1).

## Notes for the survey
Feeds the "video -> demonstration -> RL-augmented-by-demos" branch: state-based
retargeting-plus-RL, not a reward-from-video or affordance-from-video method (contrast
dexvip_2022's hand-pose-prior reward, hudor_2024's point-tracked-object reward). Video is used
only offline to build demonstrations; the deployed policy is a standard state-based TRPO/DAPG
agent. All results are simulation-only. Block D: physical plausibility of the retargeted
hand-object interaction is checked only qualitatively — the authors visually spot finger-object
penetration under a fingertip-only retargeting baseline (Fig. 4) and fix it with a second TSV
term, but no quantitative penetration metric is ever reported for the final retargeting
(`compute_intersection_rate`/`check_contact` bodies are absent from code/md; neither is
described as a penetration-depth check — the former is the Place-Inside volume-overlap metric).
The 51-DoF-to-30-DoF embodiment gap is stated qualitatively ("will lose information inevitably")
but never isolated as a clean number — the closest ablation (Fig. 6a) compares SOIL success
under 3 retargeting variants on one object, which conflates retargeting quality with jerk
smoothness.
