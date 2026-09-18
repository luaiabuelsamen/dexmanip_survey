# plappert_multigoal_2018 — Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research (Plappert, Andrychowicz, Ray, McGrew, Baker, Powell, Schneider, Tobin, Chociej, Welinder, Kumar, Zaremba; arXiv (OpenAI) 2018, arXiv 1802.09464)

sources: papers/md/plappert_multigoal_2018.md [9a57fe95] ; code/md/plappert_multigoal_2018.md [4d1ebecb]

Code caveat: the code markdown is the Farama `Gymnasium-Robotics` successor repo (README cites version 1.4.0, 2024; `FetchReach-v4`), not the 2018 `openai/gym` release the paper describes. The extract carries class/method signatures plus `_get_obs` and `compute_reward` bodies only; `__init__` bodies, `_is_success`, `_goal_distance` and the registration file are absent, so default threshold values are NOT visible in the extract.

## One-line contribution
A suite of eight sparse-reward, goal-conditioned MuJoCo tasks (four Fetch arm, four Shadow Hand, the hand ones with rotation/full variants) integrated into OpenAI Gym via a `GoalEnv` dict-observation API with an exposed `compute_reward`, plus DDPG and DDPG+HER baselines and a list of open research problems around HER (Abstract; Sec. 1.3; Sec. 2).

## Setting
- hand(s): Shadow Dexterous Hand, "an anthropomorphic robotic hand with 24 degrees of freedom. Of those 24 joints, 20 can be can be controlled independently whereas the remaining ones are coupled joints" (Sec. 1.2). Code README (line 40) describes it as "a 24-DoF anthropomorphic robotic hand". No other hand in the paper. arm: Fetch, "7-DoF Fetch robotics arm, which has a two-fingered parallel gripper" (Sec. 1.1). single/bimanual: single hand or single arm; no bimanual task.
- simulator / physics: MuJoCo (Todorov et al. 2012), released in OpenAI Gym (Sec. 1). Simulator timestep ∆t = 0.002 s; "We apply the same action in 20 subsequent simulator steps ... i.e. the agent's action frequency is f = 25 Hz" (stated identically for Fetch, Sec. 1.1, and Hand, Sec. 1.2). No solver, contact model, or friction settings are stated. Parallelism is on the RL side: 19 CPU cores × 2 rollouts each via MPI (Sec. 1.4), not vectorised envs. Code: `BaseRobotEnv.__init__(self, model_path, initial_qpos, n_actions, n_substeps, ...)` in `gymnasium_robotics/envs/robot_env.py`; Fetch obs velocities are scaled by `dt = self.n_substeps * self.model.opt.timestep` (`fetch_env.py`, `generate_mujoco_observations`). Numeric `n_substeps` defaults are not in the extract.
- observation (paper): Fetch: "Cartesian position of the gripper, its linear velocity as well as the position and linear velocity of the robot's gripper. If an object is present, we also include the object's Cartesian position and rotation using Euler angles, its linear and angular velocities, as well as its position and linear velocities relative to gripper" (Sec. 1.1). Hand: "the 24 positions and velocities of the robot's joints. In case of an object ... its Cartesian position and rotation represented by a quaternion (hence 7-dimensional) as well as its linear and angular velocities. In the reaching task, we include the Cartesian position of all 5 fingertips" (Sec. 1.2). Dimensions: only one is stated, the FetchReach `FlattenDictWrapper(env, ['observation','desired_goal'])` output has shape `(13,)` (Appendix A), i.e. 10-D observation + 3-D goal. No vision, no tactile in this paper.
- observation (code): Fetch `_get_obs` concatenates `[grip_pos, object_pos, object_rel_pos, gripper_state, object_rot, object_velp, object_velr, grip_velp, gripper_vel]`, `achieved_goal = grip_pos` (no object) or `object_pos` (`fetch_env.py`). Hand manipulate `_get_obs` concatenates `[robot_qpos, robot_qvel, object_qvel, achieved_goal]` where `achieved_goal` "contains the object position + rotation" (`shadow_dexterous_hand/manipulate.py`). HandReach: `[robot_qpos, robot_qvel, achieved_goal]` (`shadow_dexterous_hand/reach.py`). The repo also adds `*TouchSensors` variants appending `touch_values` (sensordata / boolean / log; README: 92 touch sensors) from a later paper (`manipulate_touch_sensors.py` docstring cites the Frontiers 2021 tactile paper), not part of this one.
- action space: Fetch: 4-D, "3 dimensions specify the desired gripper movement in Cartesian coordinates and the last dimension controls opening and closing of the gripper" (Sec. 1.1). Hand: 20-D, "absolute position control for all non-coupled joints" (Sec. 1.2). Both at 25 Hz. Code exposes a `relative_control` flag in the manipulate `__init__` signature (`manipulate_touch_sensors.py`); its default is not in the extract.
- objects / data: Fetch: box (Push, PickAndPlace), puck (Slide); Hand: block, egg-shaped object, pen (Secs. 1.1–1.2). Three hand objects, one per task; no dataset, no demonstrations.
- Task list (Secs. 1.1–1.2; `-v0` ids in Figs. 3–4 and App. C):

  | family | task | goal | variants |
  |---|---|---|---|
  | Fetch | FetchReach | 3-D gripper position | – |
  | Fetch | FetchPush | 3-D box position on table; fingers locked | – |
  | Fetch | FetchSlide | 3-D puck position out of reach | – |
  | Fetch | FetchPickAndPlace | 3-D box position, on table or in air | – |
  | Hand | HandReach | 15-D, 5 fingertip positions | – |
  | Hand | HandManipulateBlock | 7-D pos + quaternion | RotateZ, RotateParallel, RotateXYZ, Full |
  | Hand | HandManipulateEgg | 7-D pos + quaternion | Rotate, Full |
  | Hand | HandManipulatePen | 7-D pos + quaternion | Rotate, Full |

  Variant semantics (Sec. 1.2): `RotateZ` random z-rotation only; `RotateParallel` random z plus axis-aligned x/y; `RotateXYZ`/`EggRotate` random rotation on all axes; `PenRotate` random x and y, "no target rotation around the z axis"; `Full` = random rotation plus random target position. Code mirrors this via `__init__(self, target_position, target_rotation, reward_type)` on each `MujocoHand{Block,Egg,Pen}Env` (`manipulate_block.py`, `manipulate_egg.py`, `manipulate_pen.py`).

## Method
- paradigm: RL benchmark; baselines are DDPG and DDPG+HER (Andrychowicz et al. 2017) from OpenAI Baselines, each with sparse and with dense rewards (Sec. 1.4).
- reward (paper): Fetch: "The agent obtains a reward of 0 if the object is at the target location (within a tolerance of 5 cm) and −1 otherwise" (Sec. 1.1). Hand: "a reward of 0 if the goal has been achieved (within some task-specific tolerance) and −1 otherwise" (Sec. 1.2). Dense reward is not defined in the text beyond "the Euclidean distance between positions and the difference between two quaternions for rotations" (Sec. 1.4 discussion).
- reward (code), `gymnasium_robotics/envs/fetch/fetch_env.py` and `shadow_dexterous_hand/reach.py`, identical bodies:
  ```python
  d = goal_distance(achieved_goal, desired_goal)
  if self.reward_type == "sparse":
      return -(d > self.distance_threshold).astype(np.float32)
  else:
      return -d
  ```
  `shadow_dexterous_hand/manipulate.py`:
  ```python
  if self.reward_type == "sparse":
      success = self._is_success(achieved_goal, desired_goal).astype(np.float32)
      return success - 1.0
  else:
      d_pos, d_rot = self._goal_distance(achieved_goal, desired_goal)
      # We weigh the difference in position to avoid that `d_pos` (in meters) is completely
      # dominated by `d_rot` (in radians).
      return -(10.0 * d_pos + d_rot)
  ```
  So the code's dense manipulation reward is −(10·d_pos + d_rot); the paper never states this weighting.
- key trick(s): `gym.GoalEnv` with a `Dict` observation of `observation`, `desired_goal`, `achieved_goal`, and an exposed `compute_reward(achieved_goal, desired_goal, info)` such that `reward == env.compute_reward(obs['achieved_goal'], obs['desired_goal'], info)` always holds and goals can be substituted for HER (Sec. 1.3, App. A). Code extends this with `compute_terminated`/`compute_truncated` (README "Multi-goal API"). Hyperparameters (App. B): 3×256 ReLU actor/critic, Adam 1e-3, buffer 1e6, Polyak 0.95, action-L2 1.0, batch 256, 19 MPI workers × 2 rollouts, 50 cycles/epoch, 40 batches/cycle, random-action prob 0.3, Gaussian noise 0.2, HER replay prob 0.8; chosen by 40 random combinations on `HandManipulateBlockRotateZ-v0`, 3 seeds, area under the test-success curve.

## Evaluation
- success criteria (paper, verbatim):
  - Fetch (all four): reward 0 "if the object is at the target location (within a tolerance of 5 cm)" (Sec. 1.1); code: `-(d > self.distance_threshold)` with `d = goal_distance` (`fetch_env.py`).
  - HandReach: "A goal is considered achieved if the mean distance between fingertips and their desired position is less than 1 cm" (Sec. 1.2); code: same `distance_threshold` form (`reach.py`).
  - HandManipulateBlock and Egg: "achieved if the distance between the block's position and its desired position is less than 1 cm (applicable only in the `Full` variant) and the difference in rotation is less than 0.1 rad" (Sec. 1.2).
  - HandManipulatePen: "less than 5 cm (applicable only in the `Full` variant) and the difference in rotation, ignoring the z axis, is less than 0.1 rad" (Sec. 1.2; footnote 6: pen z axis runs along its body). Code carries `distance_threshold`, `rotation_threshold`, `ignore_z_target_rotation` as `__init__` arguments (`manipulate_touch_sensors.py` signature) but their values are not in the extract, so paper-vs-code agreement on 1 cm / 5 cm / 0.1 rad could not be checked.
- metric: "Median test success rate" (Figs. 3–4 y-axis). Protocol: after each epoch, "10 deterministic test rollouts per MPI worker", success averaged across rollouts and the 19 workers; 5 seeds; median with interquartile range (Sec. 1.4). Epoch = 19·2·50 = 1900 episodes. 50 epochs (4.75e6 timesteps) for the four Fetch tasks and HandReach; 200 epochs (38e6 timesteps) for the manipulation tasks (Sec. 1.4).
- headline numbers: none are given numerically. All results are curves: Fig. 3 (Fetch, four panels, epochs 0–50) and Fig. 4 (HandReach, HandManipulateBlockRotateXYZ, HandManipulateEggFull, HandManipulatePenRotate; hand panels to epoch 200); App. C repeats every task/variant one panel each (FetchPickAndPlace, FetchPush, FetchReach, FetchSlide, BlockFull, BlockRotateParallel, BlockRotateXYZ, BlockRotateZ, EggFull, EggRotate, PenFull, PenRotate). The PDF extract contains only axis labels and legends, no values, so no success-rate number can be quoted. Note Fig. 4's caption in the extract reads "for all four Fetch environments" although it plots the hand tasks (caption error in the paper).
- qualitative results (Sec. 1.4): FetchReach "can easily be solved by all four configurations"; on the other Fetch tasks "DDPG+HER clearly outperforms all other configurations"; DDPG+HER "performs best if the reward structure is sparse"; vanilla DDPG finds dense easier. Hand: DDPG+HER "significantly outperforms the DDPG baseline. In fact, the baseline often is not able to learn the problem at all"; "HER is able to learn partly successful policies on all environments but especially `HandManipulatePen` is especially challenging and we are not able to fully solve it."
- baselines beaten: DDPG+HER (sparse) > DDPG+HER (dense) > DDPG (dense/sparse) on every non-trivial task, by curves only.
- real robot? No. Simulation only; hardware is the reference for the models.

## Limitations stated by the authors
- FetchReach "is so easy that even partially broken implementations sometimes learn successful policies, so no conclusions should be drawn from this task alone" (footnote 4).
- HandManipulatePen not fully solved by DDPG+HER (Sec. 1.4).
- HER "changes the joint distribution of replayed (state, action, next_state, goal) tuples in an unprincipled way", could fail in very stochastic environments (Sec. 2, "Unbiased HER").
- Learning speed is limited by target-network update frequency / one-step bootstrapping (Sec. 2, "Faster information propagation").
- Request for Research list (Sec. 2, in order): Automatic hindsight goals generation; Unbiased HER; HER+HRL; Richer value functions; Faster information propagation; HER + multi-step returns; On-policy HER; Combine HER with recent improvements in RL; RL with very frequent actions.

## Quotable claims (verbatim, with section)
- "All tasks have sparse binary rewards and follow a Multi-Goal Reinforcement Learning (RL) framework in which an agent is told what to do using an additional input." (Abstract)
- "We find that the object geometry makes a significant differences in how hard the problem is and the egg is probably the easiest object." (Sec. 1.2)
- "Grasping the pen is quite hard since it easily falls off the hand and can easily collide and get stuck between other fingers." (Sec. 1.2)
- "Learning the critic is much simpler for sparse rewards. In the dense case, the critic has to approximate a highly non-linear function that includes the Euclidean distance between positions and the difference between two quaternions for rotations." (Sec. 1.4)
- "A dense reward biases the policy towards a specific strategy. For instance, it may be beneficial to first grasp an object properly and then start rotating it towards the desired goal." (Sec. 1.4)

## Notes for the survey (which sections this feeds; contradictions with other notes)
- Feeds: benchmarks/simulators (the canonical Gym Shadow Hand tasks; 24-DoF/20-actuated model, 25 Hz, ∆t 0.002), reward design (sparse-binary vs dense, and the argument that sparse+HER beats dense), and the in-hand reorientation lineage (HandManipulateBlock* is the seed of later cube-reorientation work).
- Success thresholds to reuse when comparing across notes: 5 cm (Fetch), 1 cm mean fingertip (HandReach), 1 cm + 0.1 rad (Block/Egg Full), 5 cm + 0.1 rad ignoring z (Pen Full); rotation-only variants ignore position (Sec. 1.2).
- Code mismatch/gap: the maintained repo is Farama Gymnasium-Robotics, not the paper's Gym; env ids are `-v4` there vs `-v0` in the paper; threshold defaults could not be read from the extract (signatures only), so any code-side check of 1 cm / 0.1 rad remains open. The code dense reward −(10·d_pos + d_rot) is undocumented in the paper.
- The task set has no object variety within a task (one block, one egg, one pen) and no penetration or contact-quality measure; success is purely pose distance. The repo also contains Adroit, Franka Kitchen, Maze, MaMuJoCo environments that are unrelated to this paper.
- No numeric success rates exist in the text; any cited "DDPG+HER reaches X% on HandManipulateBlock" would have to be read off the figures, which this extract does not permit.
