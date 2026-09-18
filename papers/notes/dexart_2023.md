# dexart_2023 — DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects (Bao et al., CVPR 2023)

sources: papers/md/dexart_2023.md [44354c04] ; code/md/dexart_2023.md [d6ab75e1]

## One-line contribution
Four SAPIEN tasks (Faucet, Bucket, Laptop, Toilet) in which an XArm6 + Allegro hand must manipulate PartNet-Mobility articulated objects from partial point clouds, with a seen/unseen object split per task; PPO + small PointNet, with part-segmentation pre-training the best of five visual pre-training methods (Table 2).

## Setting
- hand(s): Allegro Hand, "16 DoF" (Sec. 3.2); code finger links `link_15.0` (thumb), `link_3.0` (index), `link_7.0` (middle), `link_11.0` (ring), palm = `base_link` (`dexart/env/rl_env/base.py:configure_robot_contact_reward`). arm: "XArm6 robot arm (6 DoF)" (Sec. 3.2). single hand.
- simulator / physics: "SAPIEN physical simulator [61]" (Sec. 3.2). No timestep, solver, or contact parameters are stated in the paper; the code extract exposes only constructor arguments `frame_skip`, `friction`, `iter` (`dexart/env/sim_env/{faucet,laptop,bucket,toilet}_env.py`) and `check_contact(..., impulse_threshold)` (`sim_env/base.py`) with no values. Number of parallel envs: README training example uses `--workers 10 --n 100` ("number of simulation progress", "number of rollouts to be collected in a single episode"). Control frequency not stated.
- observation (Sec. 3.2): "proprioceptive data S_r includes the current joint position of the whole robot, linear velocity, angular velocity, position and pose of the end-effector palm"; "partial point cloud P_o captured by a depth camera includes the articulated object and the robot ... cropped within the robot workspace and then down-sampled uniformly"; concatenated with an "imagined robot point cloud P_i" sampled from the hand's forward-kinematics geometry (Sec. 4.1). "no oracle information is used". Code: `observation_space` (`rl_env/base.py`) builds a Dict with `state`, `oracle_state`, per-camera `point_cloud` Box of shape `(num_points, 3)`, `seg_gt` of `(num_points, 4)`, and imagination Boxes of shape `(num_points, 7)`; `num_points` value is not in the extract. Point-cloud noise via `pc_processing.add_gaussian_noise` (`noise_level` unspecified).
- action space (Sec. 3.2): "22-dimensional vector ... 6-DoF for arm and 16-DoF for hand. We use an operational space control for robot arm where the first 6-D vector is the target linear and angular velocity of the palm. For Allegro hand, we use a joint position controller to command the position target of 16 joints. Both controllers are implemented by PD control."
- objects / data: PartNet-Mobility [61] models, manually selected, with per-object scale and initial pose annotation and randomised initial pose (Sec. 3.4). Table 1 "Task Statistics" (All / Seen / Unseen): Faucet 18 / 11 / 7; Bucket 19 / 11 / 8; Laptop 17 / 11 / 6; Toilet 28 / 17 / 11 (total 82). Pre-training data (Sec. 4.2): DAM = "6k point clouds for each object" with 4-class labels (functional part, rest of object, hand, arm); PMM = "46 object categories and 1k point clouds for each category" from PartNet-Mobility without the robot.

## Method
- paradigm: RL ; algorithm: PPO [53] with shared PointNet (one hidden layer, GELU, max-pool) + proprioception MLP feeding policy and value heads (Sec. 4.1). Pre-training variants: Segmentation on PMM, Classification on PMM (46-way), Reconstruction on DAM (PointNet encoder + PCN decoder, Chamfer loss), SimSiam on DAM, Segmentation on DAM (Sec. 4.3).
- reward (Sec. 3.3): three stages "reaching the functional part, constructing contact between the hand and manipulated objects, and executing task-specific actions". The equations (reach reward with indicator and lambda regulariser; contact term "IsContact is a boolean function that performs collision detection"; "a good contact relationship is constructed if both the palm and at least two fingers touch the object"; part-manipulation reward using "Progress is a task-specific evaluation function"; penalty "L2 norm of the action and a task-specific term") are dropped by the PDF converter, so only the prose survives; "The overall reward is the weighted sum of four reward terms. More details ... in our supplementary material" (not on disk).
  Code implements a state machine (`self.state` in {1,2,3}) rather than the paper's equations. `dexart/env/rl_env/faucet_env.py:get_reward`:
  ```
  if self.state == 1: reward = -0.1 * min(np.linalg.norm(self.palm_pose.p - self.handle_pose.p), 0.5)
  elif self.state == 2: reward += 0.2 * int(self.is_contact); reward -= 0.1 * int(self.is_arm_contact)
  elif self.state == 3: reward += 0.2 * int(self.is_contact); reward -= 0.1 * int(self.is_arm_contact); reward += 1.0 * self.openness
  if self.early_done: reward += (self.horizon - self.current_step) * 1.2 * self.openness
  action_penalty = np.sum(np.clip(self.robot.get_qvel(), -1, 1) ** 2) * 0.01
  controller_penalty = (self.cartesian_error ** 2) * 1e3
  reward -= 0.01 * (action_penalty + controller_penalty)
  ```
  `laptop_env.py` and `toilet_env.py` are identical in structure with `self.progress` in place of `openness`, an extra `0.5 * self.progress` when `progress < 0` in states 1-2, and penalty weight 0.01 (laptop) vs 0.005 (toilet). `bucket_env.py:get_reward` differs: `0.2 * self.palm_vector[2]`, `-0.2 * self.finger_base_touched_percent` ("under no circumstances should hand touch bucket base"), velocity penalties on the bucket base link, `0.5 * self.progress + 0.2 * progress * finger_touched_percent`, and in state 3 `if self.delta_height < 0.3: reward += 100 * (palm_height - last_palm_height) + delta_height / 0.3 * 10  # lift to 0.6m is enough`, penalty weight 0.1. Finger contact scale `finger_reward_scale = 0.01` per finger, thumb `0.04` (`base.py`).
  Mismatch: the paper describes four weighted terms with an indicator-based reach reward; the code uses stage-gated rewards with a "early_done" bonus of `(horizon - step) * 1.2 * progress` and controller-error penalties not mentioned in the paper.
- key trick(s): imagined hand point cloud from FK (Sec. 4.1); segmentation pre-training on DAM; smallest PointNet generalises best (Sec. 5.2); "we employ a simple version of PointNet ... increasing the volume of the vision extractor actually harms policy learning".

## Evaluation
- metrics: success rate and episodic return "on both seen objects and unseen objects. We train RL policy with 3 different random seeds for each experiment" (Sec. 5). Success criteria stated per task (Sec. 3.1): Faucet "rotate it by around 90 degrees ... evaluation criteria are based on the rotated angle of the handle"; Bucket "considered a success if the bucket is lifted to a given height" (code comment: "lift to 0.6m is enough", `delta_height < 0.3` gate); Laptop "evaluated based on the changed angle of laptop lid"; Toilet "successfully solved if the toilet lid is opened at a threshold degree". Numeric thresholds are not given in the paper text; the code extract contains only signatures for `is_done`, `update_cached_state`, `horizon`, so thresholds could not be verified from code. README evaluation: `evaluate_policy.py ... --eval_per_instance 100`, `--use_test_set` for unseen.
- headline numbers, Table 2 "Success Rate of Different Pre-training Methods" (mean +/- std, Seen / Unseen):

  | method | Faucet | Bucket | Laptop | Toilet |
  |---|---|---|---|---|
  | No Pre-train | 0.30+-0.22 / 0.28+-0.21 | 0.51+-0.12 / 0.56+-0.08 | 0.81+-0.01 / 0.41+-0.09 | 0.71+-0.05 / 0.46+-0.02 |
  | Segmentation on PMM | 0.27+-0.12 / 0.17+-0.09 | 0.35+-0.25 / 0.34+-0.24 | 0.85+-0.09 / 0.55+-0.09 | 0.66+-0.08 / 0.44+-0.02 |
  | Classification on PMM | 0.20+-0.12 / 0.18+-0.14 | 0.56+-0.06 / 0.58+-0.12 | 0.80+-0.20 / 0.41+-0.14 | 0.69+-0.08 / 0.38+-0.03 |
  | Reconstruction on DAM | 0.35+-0.02 / 0.21+-0.03 | 0.51+-0.08 / 0.50+-0.05 | 0.85+-0.04 / 0.54+-0.08 | 0.76+-0.03 / 0.52+-0.03 |
  | SimSiam on DAM | 0.60+-0.15 / 0.45+-0.12 | 0.41+-0.30 / 0.38+-0.31 | 0.84+-0.04 / 0.49+-0.13 | 0.82+-0.02 / 0.50+-0.06 |
  | Segmentation on DAM (bold) | 0.79+-0.02 / 0.58+-0.07 | 0.75+-0.04 / 0.76+-0.07 | 0.92+-0.02 / 0.60+-0.07 | 0.85+-0.01 / 0.55+-0.01 |

  The README "Main Results" re-reports per-seed train/test numbers (3 seeds, `eval_per_instance 100`) that differ slightly from Table 2 (e.g. Faucet No Pre-train 0.32/0.26 vs 0.30/0.28; Laptop Segmentation on DAM 0.91/0.60 vs 0.92/0.60; Bucket Segmentation on DAM 0.73/0.75 vs 0.75/0.76) and show seed collapse (Faucet No Pre-train seed 1 = 0.00/0.00; Bucket SimSiam seed 0 = 0.00/0.00; Bucket Segmentation on PMM seed 1 = 0.00/0.00).
  Table 3 "Non-3D Representations" (Laptop, Seen / Unseen): PointNet 0.78+-0.04 / 0.41+-0.08; ResNet-18 (R3M) 0.64+-0.07 / 0.28+-0.05. (Flattened in the source; the row assignment above follows the text order "PointNet 0.78 ... ResNet-18 0.64".)
  Fig. 6: 100 % vs 50 % of seen objects, unseen success higher with 100 % on all tasks; x-axes to 10M (Faucet), 40M (Bucket), 15M (Laptop), 8M (Toilet) environment steps. Fig. 7: small > medium > large PointNet. Fig. 9: 35 camera poses (azimuth -60..60 deg, polar -20..20 deg, 20 deg steps); PointNet policy robust, ResNet-18 "suffers dramatically drop".
- baselines beaten: no external methods; internal comparison of pre-training methods and R3M/ResNet-18.
- real robot? None reported.

## Limitations stated by the authors
No limitations section. Implicit: "the RL training can only handle low-resolution point cloud due to the memory limitation" (Sec. 4.1); reward relies on "human knowledge" (Sec. 3.2) and a supplementary that is not on disk.

## Quotable claims (verbatim, with section)
- Abstract: "Our main focus is to evaluate the generalizability of the learned policy on unseen articulated objects."
- Sec. 1: "the simplest one with the least parameters achieves the best sample efficiency and success rate, whether the network is pre-trained or not."
- Sec. 3.3: "We believe a good contact relationship is constructed if both the palm and at least two fingers touch the object."
- Sec. 5.1: "Part segmentation boosts the policy learning on all tasks. It performs the best on all tasks."
- Sec. 6: "Large encoders may not be necessary for RL training to perform dexterous manipulation tasks."

## Notes for the survey (which sections this feeds; contradictions with other notes)
- Feeds: benchmark table (single Allegro + XArm6, SAPIEN, 4 task families, 82 objects, seen/unseen split, point-cloud obs, 22-D action, PPO baselines); the generalisation-across-instances paragraph; the "reward is a hand-tuned state machine" observation (paper prose vs code).
- Seen success on Faucet is only 0.79 even for the best method, so "solved" is not claimed for any task.
- Contradiction: zhao_dexhand_survey_2026 Table II lists DexArt's embodiment as "Adroit; Allegro"; the paper and code use only Allegro on XArm6.
- Measurement caution: success thresholds live in un-extracted code (`is_done`), std over 3 seeds hides seed-collapse runs visible in the README per-seed table; physics settings (timestep, substeps, friction) are not reported anywhere in the sources.
