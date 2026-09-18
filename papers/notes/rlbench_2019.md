# rlbench_2019 — RLBench: The Robot Learning Benchmark & Learning Environment (James, Ma, Rovick Arrojo, Davison; IEEE RA-L 2019/2020)

sources: papers/md/rlbench_2019.md [fbb04509] ; code/md/rlbench_2019.md [02720bba]

## One-line contribution
100 hand-designed, single-arm parallel-gripper manipulation tasks in V-REP/PyRep, each with an unbounded supply of motion-planned demonstrations from authored waypoints, plus a task-building tool and a K-shot challenge (abstract; Sec. I).

## Setting
- hand(s): no dexterous hand. Franka Emika Panda 7-DoF arm with the Franka gripper is the benchmark arm (Sec. IV-A; README "Swapping Arms": "For benchmarking, the arm should remain as the Franka Panda"). Code also ships Mico, Jaco (3-finger Jaco gripper), Sawyer (Baxter gripper) and UR5 (Robotiq 85) as `rlbench/robot_ttms/{jaco,mico,panda,sawyer,ur5}.ttm`, swapped via `Environment(robot_setup=...)`; README warns tasks may then be unsolvable (Mico workspace). Single arm only.
- simulator / physics: V-REP [37] + PyRep [12] (Sec. IV). Code README: "RLBench is built around CoppeliaSim v4.1.0 and PyRep"; CI (`.github/workflows/task_tests.yml`) downloads `CoppeliaSim_Edu_V4_1_0_Ubuntu20_04`. The underlying physics engine (Bullet/ODE/Vortex/Newton) and the simulation timestep are NOT stated in either source. Sec. III-f: "we cannot claim full photorealism in our rendering system, or general realistic physics". No parallel environments; one CoppeliaSim instance per `Environment` (`rlbench/environment.py`); an `examples/rlbench_gym_vector.py` exists but nothing in the sources describes it.
- throughput: no FPS / steps-per-second numbers anywhere in the paper or README. Only the demo lengths: "The tasks lengths vary from 100 to 1000 timesteps" (Fig. 7 caption, mean length of 5 demos over 75 tasks, first variation).
- observation: over-the-shoulder stereo pair + eye-in-hand monocular camera, each giving rgb, depth, segmentation mask (abstract; Fig. 3); proprioception: joint angles, velocities, torques, end-effector pose (Sec. IV-A). Code `rlbench/backend/observation.py::Observation` has five cameras (left_shoulder, right_shoulder, overhead, wrist, front) × {rgb, depth, mask, point_cloud} plus joint_velocities/positions/forces, gripper_open, gripper_pose, gripper_matrix, gripper_joint_positions, gripper_touch_forces, task_low_dim_state, misc. The paper text names only three cameras; overhead and front were added in code. Default image size 128×128 (README "Gotchas"). Gym wrapper exposes 'state' or 'vision' observation modes (`rlbench/gym.py`; README "RLBench Gym"). README warns low-dim state "should be used with extreme caution" because objects leaving the workspace put it out of distribution.
- action space (paper Sec. IV-C): absolute or delta joint velocities, joint positions, joint torques, end-effector velocities, end-effector poses. Code v1.2.0 (`rlbench/action_modes/`): arm modes `JointVelocity`, `JointPosition(absolute_mode)`, `JointTorque`, `EndEffectorPoseViaPlanning(absolute_mode, frame, collision_checking)`, `EndEffectorPoseViaIK`, `ERJointViaIK`; gripper modes `Discrete` ("values > 0.5 will be discretised to 1 (open), and values < 0.5 ... 0 (closed)") and `GripperJointPosition`; composed by `MoveArmThenGripper` ("arm action is first applied, followed by the gripper action") or `JointPositionActionMode`. Control rate not stated. `Environment` takes `arm_max_velocity`, `arm_max_acceleration`.
- objects / data: 100 tasks in the paper (abstract). Code tree at this commit lists 107 `rlbench/task_ttms/*.ttm` and 106 `rlbench/tasks/*.py` signatures (my count of the file tree; the discrepancy with 100 is not explained in the sources). Each task = a `.ttm` V-REP model (scene objects + demo waypoints) + a `.py` file (variations, success criteria) (Sec. IV-E). Task sets in code: few-shot `FS10/25/50/95_V1` (X train tasks + 5 test), multi-task `MT15/30/55/100_V1` (README). Object meshes from turbosquid, cgtrader, free3d, thingiverse, cadnav (README "Acknowledgements").

## Method
- paradigm: benchmark, no learning method. Demonstrations from an expert π* per task/variation using OMPL [38] on authored waypoints (Sec. IV-D). Task/variation/episode hierarchy: "Across variations, usually target objects or colours are changed, whereas across episodes positions are changed" (Fig. 4 caption); formally T = {ν1..νN}, τ ~ ν (Sec. IV-B).
- reward: "Each task has a completely sparse reward of +1 which is given only on task completion" (Sec. IV-C). Code: `rlbench/backend/task.py::Task.reward()` returns `None` by default ("Allows the user to customise the task and add reward shaping"); `Environment(shaped_rewards=...)` (README, 11 May 2022: shaped rewards for reach_target and take_lid_off_saucepan). Shaped bodies in code:
  - `rlbench/tasks/reach_target.py`: `return -np.linalg.norm(self.target.get_position() - self.robot.arm.get_tip().get_position())`
  - `rlbench/tasks/take_lid_off_saucepan.py`: `grasp_lid_reward = -||lid - tip||; lift_lid_reward = -||lid - success_detector||; return grasp_lid_reward + lift_lid_reward`
  - `rlbench/tasks/slide_block_to_target.py`: `grip_to_block + block_to_target` (both negative L2 distances).
  Mismatch to note: paper says sparse only; code at this commit has dense shaping for at least three tasks, off by default.
- success definition (mechanism): a task registers a list of condition sets; the episode terminates as a success when a set is met. Paper Fig. 6 example (`TakeLidOffSaucepan.init_task`):
  ```
  lid = Shape('saucepan_lid'); success_detector = ProximitySensor('success')
  self.register_graspable_objects([lid])
  cond_set = [GraspedCondition(self.robot.gripper, lid), DetectedCondition(lid, success_detector)]
  self.register_success_conditions([cond_set])
  ```
  "the episode should terminate and be considered a success only if the saucepan lid is detected by a proximity sensor and that the lid is being held" (Fig. 6 caption). Code: `rlbench/backend/conditions.py` (in tree; bodies not in the parsed md), `Task.register_success_conditions`, `Task.register_fail_conditions`, `Task.success()` (`rlbench/backend/task.py`). Tasks may define custom conditions, e.g. `class ChairsOrientedCondition(Condition)` with `condition_met()` in `rlbench/tasks/stack_chairs.py`.
- task lifecycle (Sec. IV-E): `init_task()` once; `init_variation(i)` / `init_episode(index)` returns the list of language descriptions; `variation_count()`. Code adds `base_rotation_bounds`, `boundary_root`, `is_static_workspace`, `register_waypoint_ability_start/end`, `register_waypoints_should_repeat`, `register_stop_at_waypoint` (`rlbench/backend/task.py`). Placement randomisation: "The backend handles the randomisation of the position of the task at the beginning of each episode" (Fig. 6 caption; `rlbench/backend/spawn_boundary.py` in tree).
- demo generation / validation: `TaskEnvironment.get_demos(amount, live_demos, ..., max_attempts, random_selection, from_episode_number)` and `_get_live_demos`; `tools/task_validator.py::task_smoke(task, scene, variation, demos, success, max_variations, test_demos)` "attempts to collect a number of demonstrations of the designed task in order to ensure that the path planning aspect of the task only fails a small number of times" (Sec. IV-E). CI runs `pytest tests/demos` on every task (`task_tests.yml`).
- domain randomisation: `rlbench/sim2real/domain_randomization.py` — `VisualRandomizationConfig(image_directory, whitelist, blacklist, randomize_arm)`, `DynamicsRandomizationConfig`, `RandomizeEvery` enum with `frequency` (README "Sim-to-Real" example: `randomize_every=RandomizeEvery.EPISODE, frequency=1`). Paper Sec. III-f mentions "a domain randomisation rendering option".

## Evaluation
- metrics: success rate on new episodes of a task (binary, from the condition sets). Few-shot challenge v1.0 (Sec. V): 10% of the 100 tasks held out as meta-test; "the system is given K demonstrations of the unseen task (K-shot), and then success should be reported on new episodes of that same task ... Users report 1-shot, 5-shot, and 20-shot results". Multi-task variant: train on all tasks, test on unseen episodes (Sec. VI-d).
- headline numbers: none. The paper reports no baseline results and no learning curves; only task statistics (Fig. 7: word frequencies of descriptions; demo lengths 100-1000 timesteps).
- baselines beaten: none run.
- real robot: none. Sim-to-real is proposed as a use case via arm swapping (Sec. VI-c).

## Limitations stated by the authors
- "we cannot claim full photorealism in our rendering system, or general realistic physics" (Sec. III-f).
- "our system ... sacrifices the real-world aspect, but in exchange we receive the ability generate a diverse range of tasks in a scalable way" (Sec. II-b, vs Simitate).
- "we envision that there may be teething problems as people begin using the platform" (Sec. VII); challenge is versioned v1.0 because the task count is expected to grow (Sec. V).
- README: low-dim observations are unsafe (no workspace safeguard); changing image size requires re-collecting demos; swapped arms may make tasks unsolvable.

## Quotable claims (verbatim, with section)
- "The benchmark features 100 completely unique, hand-designed tasks ranging in difficulty, from simple target reaching and door opening, to longer multi-stage tasks" (abstract).
- "each task comes with an infinite supply of demos through the use of motion planners operating on a series of waypoints given during task creation time" (abstract).
- "Each task has a completely sparse reward of +1 which is given only on task completion." (Sec. IV-C)
- "Every task starts with the same assumption that no objects are held, therefore, unlike many works in the literature, tasks that involve tools will first need to grasp the object appropriately in order to accomplish the task." (Sec. IV-A)
- "these created tasks can often succumb to unintentionally introducing another hyperparameter into the method in the form of the task design itself. For example, a method could fail on a more challenging task, and so results would only be presented for a simpler set of tasks." (Sec. II-a)
- "There must be no prior knowledge of the unseen tasks given to the system that are not included in the training tasks. Users report 1-shot, 5-shot, and 20-shot results for their method." (Sec. V)

## Notes for the survey
- Feeds: benchmarks section (the gripper-benchmark template that COLOSSEUM builds on directly — same CoppeliaSim/PyRep stack, same task/variation/episode and condition-set success mechanism); evaluation section (binary success from proximity-sensor + grasped conditions, no trial-count or CI guidance at all; the K-shot protocol specifies 1/5/20 demos but not the number of evaluation episodes).
- No dexterous hand, no tactile, no bimanual: this is the reference point for what "standardised" looks like in gripper land, not a dexterous benchmark.
- Physics engine and timestep are unrecorded in both sources; do not quote an engine for RLBench from this note. Throughput: none reported; contrast with ManiSkill3 / Isaac Lab notes which report FPS tables.
- Task-count drift: paper says 100, code tree has 107 `.ttm`; cite "100" for the paper and note the repo has grown.
- Paper-vs-code mismatch: sparse-only reward in paper; opt-in dense shaping (negative L2 distances) for a few tasks in code since 2022.
