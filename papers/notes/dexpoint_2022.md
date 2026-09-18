# dexpoint_2022 — DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation (Qin et al., CoRL 2022)

sources: papers/md/dexpoint_2022.md [sha256 c77516db] ; code/md/dexpoint_2022.md [commit 17f1e238]

## One-line contribution
An RL policy that takes point-cloud input (real + "imagined" hand points) plus a contact-based reward, trained purely in sim on an Allegro Hand + XArm6, and transfers zero-shot to real-world grasping of novel objects and door opening (Abstract; Sec 3).

## Setting
- hand(s): Allegro Hand, "16-DoF anthropomorphic hand with four fingers" (Sec 3, System Setup, p.3); vendor not stated. arm: XArm6, "6-DoF robot arm" (Sec 3, p.3). single/bimanual: single hand-arm system.
- simulator / physics: SAPIEN [54], "a full-physics simulator"; physics engine name (e.g. PhysX) not stated. Sim timestep 0.005 s; each control step lasts 0.05 s, i.e. 10 physics substeps per control step (Sec 3, System Setup, p.3). Number of parallel envs: not stated.
- observation: point cloud (observed + imagined) + proprioception + goal — see Method/B below.
- action space: 22-dim (6 arm + 16 hand) — see Method/B below.
- objects / data: ShapeNet [55] bottles/cans + YCB [56] bottles/cans (sim); 3 doors (sim + real). See held-out counts below.

## Method
- paradigm: RL (on-policy PPO); the paper separately mentions "distilling experiments" once (App. B, p.13, "We use on-policy RL training for setting except the distilling experiments") with no further description extracted — not detailed enough to call teacher-student here.
- reward or loss: see block C below (quoted verbatim from paper and code).
- key trick(s): (i) imagined hand point cloud — sample points from each finger-link mesh via forward kinematics and concatenate with the observed (camera) point cloud, one-hot-tagged observed/imagined (Sec 3.2, p.4); (ii) contact-based reward using oracle contact-pair information instead of putting contact in the observation (Sec 3.1, p.4).

## A. Embodiment block
- Hand: Allegro Hand, 16 DoF, 4 fingers, vendor not stated. Arm: XArm6, 6 DoF, fixed base (not floating). Bimanual: no.
- Simulator: SAPIEN [54] (version not stated). Physics engine: not stated.
- Sim timestep: 0.005 s. Control step: 0.05 s (→ 20 Hz control, 10 substeps/step) (Sec 3, p.3).
- Parallel envs: not stated. GPU / wall-clock training time: not stated.

## B. Learning block
- Paradigm: RL. Algorithm: PPO [57]; hyperparameters (Table 5, App. B, p.13): mini-batch size 500, learning rate 3e-4, clip range 0.8, horizon 200, epoch 10, steps per iteration 10. Training curves reported to ~600 iterations, "each iteration contains 20K environment steps" (Sec 4.2, p.6).
- Teacher-student / privileged→vision distillation: not stated beyond the single "distilling experiments" mention above; what is privileged, and the distillation procedure, are not given in the extracted text.
- Observation, item by item: paper text (Sec 3, Observation Space, p.4) lists four modalities: (1) observed point cloud from the camera, (2) proprioception (joint positions + end-effector position), (3) imagined hand point cloud (Sec 3.2), (4) object goal position. "The dimension of each observation modality is shown in Figure 3" (a figure, no extracted numeric text — dims not stated). Code: `dexpoint/env/rl_env/base.py: get_visual_observation()` builds `camera_obs` (from `get_camera_obs()`) and adds `state=get_robot_state(), oracle_state=get_oracle_state()`; the bodies of `get_robot_state`/`get_oracle_state` (the exact item list) are not present in the extracted code/md, so the precise per-field vector is not stated at the code level.
- Action space: 22-dim total, "6 + 16" (Sec 3, Action Space, p.4). Arm: 6D translation+rotation of end-effector relative to a reference pose, resolved by damped least-squares IK with damping λ=0.05; hand: per-joint position controller. Both arm and hand run PD controllers. Code: `dexpoint/env/rl_env/base.py` has `compute_inverse_kinematics(delta_pose_world, palm_jacobian, damping)` and `recover_action(action, limit)`, consistent with a position/delta-pose action space, but the mapping from raw action to `limit` is not shown.
- Domain randomization: initial object pose and goal pose randomized every grasping trial; initial pose randomized every door trial (Sec 3, Tasks and Objects, p.3). Point-cloud pipeline adds "distance-dependent Gaussian noise" to the simulated cloud, and simulation uses "ground-truth camera pose with multiplicative noise for frame transformation" (Sec 4.1, Point Cloud Pre-processing, p.5). Code has `generate_random_object_pose(self, randomness_scale)` and `generate_random_target_pose(self, randomness_scale)` (`dexpoint/env/sim_env/relocate_env.py`) but their bodies/ranges are not in the extracted code — exact numeric ranges not stated.

## C. Reward / objective block
Paper (Sec 3.1 + App. A, "Reward", p.4 and p.13), verbatim/near-verbatim:
- "The overall reward for our task is composed of four parts: reach, contact, lift, and action penalty."
- Eq. 5: `R = w_reach·r_reach + w_contact·r_contact + w_lift·r_lift + w_penalty·r_penalty`
- "we set the lift reward as the difference between object current height and object initial height `r_lift = h_current − h_init`. The action penalty reward `r_penalty = −||a||²`. For reaching reward, it consists of the distance between object and target, the distance between finger tip and the target."
- Weights: `w_reach = 1, w_contact = 0.5, w_lift = 10, w_penalty = 0.01`.
- `r_contact ∈ {0,1}`: "It outputs 1 only if the thumb is in contact with the object and there are more than one finger in contact with the object" (Sec 3.1, p.4).
- "the lift reward `r_lift` is set to 0 if the contact reward `r_contact` is 0" (App. A, p.13).

Code (`dexpoint/env/rl_env/relocate_env.py`, `AllegroRelocateRLEnv.get_reward`, code/md lines ~296–311), verbatim:
```
finger_object_dist = np.linalg.norm(self.object_in_tip, axis=1, keepdims=False)
finger_object_dist = np.clip(finger_object_dist, 0.03, 0.8)
reward = np.sum(1.0 / (0.06 + finger_object_dist) * self.finger_reward_scale)
# at least one tip and palm or two tips are contacting obj. Thumb contact is required.
is_contact = np.sum(self.robot_object_contact) >= 2
if is_contact:
    reward += 0.5
    lift = np.clip(self.object_lift, 0, 0.2)
    reward += 10 * lift
    if lift > 0.02:
        reward += 1
        target_obj_dist = np.linalg.norm(self.target_in_object)
        reward += 1.0 / (0.04 + target_obj_dist)
        if target_obj_dist < 0.1:
            theta = self.target_in_object_angle[0]
            reward += 4.0 / (0.4 + theta) * self.rotation_reward_weight
action_penalty = np.sum(np.clip(self.robot.get_qvel(), -1, 1) ** 2) * -0.01
controller_penalty = (self.cartesian_error ** 2) * -1e3
return (reward + action_penalty + controller_penalty) / 10
```
**Mismatch, noted explicitly:** the code reward is not the 4-term sum described in the paper/Eq. 5. The reach term in code is an inverse-distance shaping `1/(0.06+dist)` (not the paper's plain distance-based `r_reach`); the contact bonus is a flat `+0.5` gated by `is_contact` (matches `w_contact·r_contact` if `r_contact∈{0,1}` and `w_contact=0.5`, consistent), and lift uses `10 * lift` (matches `w_lift=10`) but `lift = clip(object_lift, 0, 0.2)` rather than the paper's `h_current − h_init` difference. The code additionally has three terms **absent from the paper's Eq. 5**: a `+1` bonus once `lift > 0.02`, a target-distance term `1/(0.04+target_obj_dist)`, a rotation bonus `4/(0.4+theta)*rotation_reward_weight`, a `controller_penalty = -1e3 * cartesian_error²` (IK tracking-error penalty), and a final `/10` normalization. Also, `is_contact` in the shown code is only `count(robot_object_contact) >= 2`; the comment claims "Thumb contact is required" and the paper's text requires the thumb specifically, but that condition is not visible in this excerpt — it may be enforced by how `robot_object_contact` is constructed elsewhere (not shown). Net: paper's reward description is a simplified/partial account of the actual reward implementation.

## D. Contact / penetration handling
Not addressed as a penalty or explicit interpenetration metric in either source. Contact is used only for the reward's `is_contact` gate. `dexpoint/env/sim_env/base.py` provides `check_contact(self, actors1, actors2, impulse_threshold)` / `check_actor_pair_contact(...)` / `check_actor_pair_contacts(...)` — contact detection via an impulse threshold, not a penetration-depth measure. No contact-solver settings (stiffness/damping/friction solver iterations) are given beyond "friction" appearing as an env constructor argument (`AllegroRelocateRLEnv.__init__(..., friction, ...)`), value not stated.

## Evaluation
- metrics (exact definitions): Sim grasping success: `d_obj < 0.05 m`, distance between object position and goal position (Sec 4.1, Evaluation Criterion, p.6). Real-world grasping success: "the XY position of the object is within 5cm from the target position and the height of the object is at least 15cm from table top" (Sec 4.1, p.6). Door success: "the door is opened to at least around 45 degrees" (Sec 4.1, p.6). No hold-duration criterion is stated for any task.
- headline numbers: Table 1 (sim, multi- vs single-object training, 5 seeds per caption but Sec 4.2 text says "we run 100 trials to compute the average success rate" — both figures given in the source, not reconciled there): multi-obj bottle novel 0.81±0.15 vs single-obj 0.60±0.06; multi-obj can novel 0.68±0.09 vs single-obj 0.63±0.18 (Table 1, p.6). Table 2 (sim ablation): "Ours" (full method) 0.83/0.81 (bottle known/novel), 0.93/0.68 (can), 0.92/0.79 (door known/novel); "w/o Contact Rew." collapses to ≈0.00–0.21 across all settings; "w/o Both" is 0.00 everywhere (Table 2, p.7). Table 3 (real, 10 trials/pair, Sec 4.4 p.8): Multi Obj. Train 0.87±0.03 (bottle), 0.83±0.13 (can), 0.73±0.12 (mixed, 26 objects: 10 bottles, 6 cans, 10 other); EigenGrasp baseline 0.50 (bottle)/0.41 (can), EigenGrasp Oracle 0.66/0.45 (Table 3, p.8). Table 4 (real door): Single Door Train 0.72±0.07 (original), 0.60±0.03 / 0.67±0.01 on the two novel doors (Table 4, p.8).
- baselines beaten: EigenGrasp (GraspIt-searched grasp + RRTConnect/OMPL motion plan to a pre-grasp then screw motion to grasp) and an "EigenGrasp Oracle" variant; both re-run by the authors (they built the ShapeNet grasp database themselves), not quoted from another paper (Sec 4.1, EigenGrasp Baseline, p.6).
- real robot? Allegro Hand on XArm6 with a RealSense D435 camera (Fig. 2). Grasping: 26 real objects, 10 trials per object-policy pair (Sec 4.4, p.8, Table 3). Door: 3 real doors (1 train, 2 novel), Table 4.

## Limitations stated by the authors
"In our experiments, we only train and test our method on two tasks, which limits the scope of the proposed method." Future direction: use "Recurrent Neural Network and temporal information for policy networks" to "enable us to do long-horizon tasks" (Sec 5, Conclusion and Limitation, p.8).

## Quotable claims (verbatim, with section)
- "we design a novel reward using contact pair information without adding contact to the observation" (Sec 1, p.2).
- "our approach is the first work to train a dexterous manipulation reinforcement learning policy with point cloud inputs that can transfer to the real world" (Sec 5, p.8).
- "Without using contact reward, the agent can hardly learn anything ... and get nearly zero success rate during evaluation for both bottle and can categories" (Sec 4.3, p.7).

## Grasp-pose generation, object set, success criterion, and quality check (required beyond template)
- Grasp pose generation: end-to-end RL for the main method — no separate grasp-pose generator or predictor; the policy directly outputs arm/hand motion. The only analytic grasp-pose pipeline is the EigenGrasp *baseline*: EigenGrasp representation + GraspIt search on the object mesh, then RRTConnect (OMPL) motion planning to pre-grasp/grasp poses (Sec 4.1, EigenGrasp Baseline, p.6) — this is not the method being evaluated as DexPoint.
- Object set / held-out count: sim multi-object training uses "10 objects from the can or bottle categories of ShapeNet" for training and "another 40 objects for testing in simulation" (App. A, Object Set, p.13) — 40 held-out sim test objects. Real world: 26 objects total, "10 bottles, 6 cans, and 10 other objects in multiple mixed categories" (Table 3 caption, p.8), used only for testing (novel relative to sim training set). Door: 3 doors, 1 used for training and 2 held out as novel, tested in both sim and real (Sec 3, Tasks and Objects, p.3; Table 4, p.8).
- Success criterion: grasping-sim, object-to-goal distance < 0.05 m; grasping-real, object XY within 5 cm of target AND lift height ≥ 15 cm off the table; door, opening angle ≥ ~45°. No dwell/hold-duration requirement is stated for any of these (Sec 4.1, p.6).
- Grasp quality check: both. Geometric/sim metric (distance-to-goal threshold, Table 1/2) and physical real-robot trials (Table 3/4, Sec 4.4).

## F. Reproducibility
- Code released: yes, `dexpoint-release` GitHub repo (commit 17f1e238), MIT-style repo with env + reward code (`dexpoint/env/rl_env/relocate_env.py`, `dexpoint/env/sim_env/relocate_env.py`, etc.).
- Checkpoints: not stated (no checkpoint release mentioned in the parsed README).
- Assets: ShapeNet object models linked via Google Drive; a scene lighting file (`day.ktx`) fetched separately; YCB/ShapeNet preprocessing utilities exist in `dexpoint/utils/` (`shapenet_utils.py`, `ycb_object_utils.py`) per the file tree.
- Training code: the README states DexPoint "is using the same training code as DexArt ... Please check the training code here to train DexPoint with PPO" — i.e. the PPO training loop itself lives in a separate repo, not in dexpoint-release.
- Reproducible from the repo as parsed: the grasping (`relocate_env.py`) reward/observation wiring for Tables 1–2 is present in the parsed code. No door-opening environment/reward file appears in the parsed file tree (only `real_world/lab_door.py`, no `rl_env` door reward shown), so Table 2's door rows and Table 4 are not reproducible from what was parsed here.

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the point-cloud-RL and contact-reward-design sections of the survey (imagined point cloud vs. tactile/contact observation; ablation Table 2 is the clearest "contact reward is necessary, not just helpful" data point in the corpus so far — collapses to ~0 success without it). Flag for cross-checking against other reward-design notes: DexPoint's actual reward code (quoted above) is considerably more shaped/hand-tuned (inverse-distance terms, IK-error penalty, staged bonuses) than the paper's four-term Eq. 5 suggests — any survey table that lists DexPoint's reward by the paper's equation alone should footnote this mismatch.
