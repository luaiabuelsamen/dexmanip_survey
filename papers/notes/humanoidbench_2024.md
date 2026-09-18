# humanoidbench_2024 — HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation (Sferrazza et al., RSS 2024)

sources: papers/md/humanoidbench_2024.md [000dd3c9] ; code/md/humanoidbench_2024.md [cb118903]

## One-line contribution
A MuJoCo benchmark of a Unitree H1 carrying two forearm-less Shadow Hands (61-D action, 151-D proprioceptive state) with 12 locomotion and 15 whole-body manipulation tasks; DreamerV3, TD-MPC2, SAC and PPO fall below the per-task success return on almost all manipulation tasks, and a hierarchical policy on a frozen MJX-pretrained reaching skill solves push.

## Setting
- hand(s): "two dexterous Shadow Hands ... from MuJoCo Menagerie", with "the cumbersome forearms" removed (Sec. III). Table II: two hands = 50 DoF, action 21 per hand ("one Shadow Hand present action spaces (19 and 21, respectively) smaller than their DoFs (25), making them underactuated"). Alternatives (App. A, Table III): H1 w/o hands (obs 51, act 19, body DoF 25), H1 w/ Robotiq 2F-85 gripper ("2-DoF Robotiq 2F-45" in App. A text; obs 55, act 23, end-effector DoF 4), H1 w/ 13-DoF Unitree hand (obs 103, act 45, DoF 26), Digit w/ ShadowHand (obs 221, act 65, body DoF 57), Unitree G1 (obs 87, act 37, body DoF 29, DoF end-effectors 14). Arm: none (humanoid arms). Bimanual: yes, both hands on one humanoid; `h1strong-highbar_hard-v0` uses strengthened hands (README: "Make hands stronger to be able to hang from the high bar").
- simulator / physics: MuJoCo [60]; "simulation timestep of 0.002 s" (App. B-C); control "at 50 Hz" (Sec. III); Table IV FPS on one CPU: Default 1050, Without hands 2450, Simplified body collisions 3600, Collisions only for feet 5100; refined tactile meshes 550 FPS (App. B-D). Whole-body tactile: MuJoCo touch grid, "448 taxels ... each providing three-dimensional contact force readings", meshes subdivided with CoACD for finer contact resolution (Sec. III, App. B-D). Low-level reaching policies trained in MuJoCo MJX on "32,768 parallel environments" with a feet-only-collision H1 without hands, 2B steps (36 h) one-hand and 4B steps (60 h) two-hand (Sec. V-D). Contact solver settings are not stated; code `HumanoidEnv(MujocoEnv)` in `humanoid_bench/env.py` exposes only signatures.
- observation: state-based benchmark: "Proprioceptive robot state (i.e., joint angles and velocities) and task-relevant environment observations (i.e., object poses and velocities)" (Sec. III); 151 = 51 body + 50 per hand (App. B-A); egocentric vision from two head cameras and tactile are available but not benchmarked. Code: `Push.observation_space` shape `(robot.dof*2 - 1 + 12,)`; `Cube.observation_space` shape `(robot.dof*2 - 1 + self.dof*2 - 2 + 4,)` (`humanoid_bench/envs/push.py`, `cube.py`). README: default returns "privileged state"; `obs_wrapper=True, sensors="proprio,image,tactile"` for multimodal.
- action space: "position control (i.e., specifying the target joint positions) ... 61-dimensional including the two hands, and controlled at 50 Hz" (Sec. III); normalised to [-1,1]^61, "19 for the humanoid body and 21 for each hand" (App. B-B); torque control also supported.
- objects / data: no demonstrations; tasks are procedurally initialised with joint noise (App. B-E). Table I comparison row: HumanoidBench action dim 61, DoF 75D, task horizon 500-1000, 27 tasks.

## Method
- paradigm: RL benchmark ; algorithms DreamerV3 ("medium" config, UTD 64), TD-MPC2 (5M config), SAC (JaxRL Minimal), PPO (Stable-Baselines3, 4 envs; run only on walk, kitchen, door, package) (Sec. V-A, App. C-A); hierarchical RL: frozen PPO/PureJaxRL reaching policy (one-hand for push, two-hand for package) as low level, DreamerV3 or TD-MPC2 high level outputting reaching targets restricted to the workspace (Sec. V-D).
- reward: App. B-E defines `tol`, `height` (head z > 1.65, margin 0.4125), `upright` (z_proj > 0.9, margin 1.9), `stand = height x upright`, `e` (small control effort), `stable = stand x e`. walk: `R = stable x tol(vx, (1, inf), 1)`, terminate after 1000 steps or z_pelvis < 0.2. run: `stable x tol(vx, (5, inf), 5)`. stand: `stable x mean(still_x, still_y)`. push: `d_goal = d(box, destination)`, `success = 1[d_goal < 0.05]`, `d_hand = d(box, hand_left)`, "by default alpha_s = 1000, alpha_t = 1, alpha_h = 0.1" (the equation itself is lost by the converter); terminate after 500 steps or d_goal < 0.05. package: `success = 1[d(package, destination) < 0.1]`, reward `... + stable + height_package + 1000 * success`, terminate after 1000 steps or success. cube: orientation term from quaternion differences and `proximity_cube` (equations lost), terminate after 500 steps or z_pelvis < 0.5 or either cube z < 0.5. kitchen: "sparse reward is the number of subtasks completed", max 4. basketball: 1000 sparse reward when d(ball, basket) <= 0.05. cabinet: three subtasks with `R_3 = 0.2 * stable + 0.8 * r_3`.
  Code, `humanoid_bench/envs/push.py:get_reward`: `penalty_dist = reward_dict["target_dist"] * goal_dist; reward_success = reward_dict["success"] if goal_dist < 0.05 else 0; hand_penalty = reward_dict["hand_dist"] * hand_dist; reward = -hand_penalty - penalty_dist + reward_success; info["success"] = reward_success > 0`. Code, `cube.py:get_reward`: `reward = 0.2 * (small_control * stand_reward * dont_move) + 0.5 * orientation_alignment_reward + 0.3 * cube_closeness_reward` with `rewards.tolerance(||quat_cube - quat_target||, margin=0.3)` per hand and hand-cube proximity `bounds=(0, 0.1), margin=0.5`; no `success` key is returned for cube. Code, `package.py`: `reward_success = dist_package_destination < 0.1`, `+ reward_success * 1000`.
  Mismatch: DreamerV3 config `dreamerv3/embodied/agents/dreamerv3/configs.yaml` sets `humanoid: {... actuation: position, reward_dict: {hand_dist: 0.1, target_dist: 0.1, success: 10, terminate: False}}`, i.e. push success bonus 10 and target-distance weight 0.1, versus the paper's defaults alpha_s = 1000, alpha_t = 1 (App. B-E). The Table V push returns are negative (-1251.9 DreamerV3), consistent with a small success bonus.
- key trick(s): hands removed from the body for reaching pretraining; force perturbations on links during pretraining; observation kept identical across tasks "to minimize domain knowledge" (Sec. III).

## Evaluation
- metrics: episode return; per-task "Target" return (Tables V, VI) and "dashed lines qualitatively indicate task success" (Figs. 5, 6). "We report the mean and standard deviation of maximum episode returns over three seeds. DreamerV3 and SAC are trained for 10M, while TD-MPC2 is trained for 2M environment steps, which roughly corresponds to 48 h" (App. C-C). Success flags exist in code (`info["success"]`) but no success rate is tabulated in the paper.
- task list (Sec. IV; README env ids `h1hand-<task>-v0`): locomotion walk, stand, run, reach, hurdle, crawl, maze, sit (sit_simple, sit_hard), balance (balance_simple, balance_hard), stair, slide, pole; manipulation push, cabinet, highbar, door, truck, cube, bookshelf (bookshelf_simple, bookshelf_hard), basketball, window, spoon, kitchen, package, powerlift, room, insert (insert_small, insert_normal). 31 env ids for the 27 named tasks.
- headline numbers, Table V (average return@10M, TD-MPC2 @2M; mean +- std over 3 seeds; Target):

  | task | DreamerV3 | TD-MPC2 | SAC | Target |
  |---|---|---|---|---|
  | walk | 800.2+-158.7 | 782.0+-109.2 | 31.7+-24.0 | 700 |
  | stand | 622.7+-404.8 | 809.0+-137.1 | 208.3+-105.6 | 800 |
  | run | 633.8+-222.4 | 93.3+-14.3 | 5.0+-2.1 | 700 |
  | reach | 7580.9+-1951.0 | 7316.1+-2112.1 | 4565.1+-212.8 | 12000 |
  | hurdle | 126.2+-59.4 | 46.4+-10.8 | 13.2+-8.8 | 700 |
  | crawl | 878.8+-122.7 | 957.4+-17.5 | 330.0+-111.9 | 700 |
  | maze | 272.3+-116.6 | 244.3+-97.7 | 144.8+-17.8 | 1200 |
  | sit_simple | 891.4+-38.4 | 411.1+-368.0 | 148.3+-103.8 | 750 |
  | sit_hard | 433.4+-355.9 | 343.0+-381.7 | 55.0+-18.2 | 750 |
  | balance_simple | 19.8+-7.0 | 40.5+-23.9 | 61.5+-1.1 | 800 |
  | balance_hard | 45.9+-27.4 | 48.2+-28.5 | 42.5+-22.6 | 800 |
  | stair | 131.1+-43.6 | 70.4+-7.1 | 14.1+-6.8 | 700 |
  | slide | 436.5+-200.1 | 119.0+-35.9 | 6.3+-2.8 | 700 |
  | pole | 658.3+-343.3 | 226.3+-116.1 | 46.3+-26.4 | 700 |
  | push | -1251.9+-659.8 | -258.7+-66.5 | -97.9+-147.0 | 700 |
  | cabinet | 57.3+-66.3 | 112.8+-142.9 | 211.8+-33.8 | 2500 |
  | highbar | 8.9+-5.8 | 0.3+-0.0 | 9.4+-3.7 | 750 |
  | door | 213.0+-149.3 | 274.7+-12.5 | 39.4+-25.2 | 600 |
  | truck | 1103.8+-232.9 | 1132.6+-72.1 | 1077.5+-95.0 | 3000 |
  | cube | 111.2+-59.9 | 54.7+-33.1 | 130.7+-30.5 | 370 |
  | bookshelf_simple | 840.4+-5.6 | 136.2+-71.6 | 346.9+-231.5 | 2000 |
  | bookshelf_hard | 530.2+-302.5 | 37.0+-1.3 | 293.9+-121.6 | 2000 |
  | basketball | 19.3+-2.5 | 42.0+-14.8 | 22.1+-3.2 | 1200 |
  | window | 461.0+-252.8 | 87.1+-37.5 | 62.9+-83.8 | 650 |
  | spoon | 349.7+-46.2 | 77.9+-80.6 | 87.7+-80.5 | 650 |
  | kitchen | 0.0+-0.0 | 0.0+-0.0 | 0.0+-0.0 | 4 |
  | package | -18015.2+-9477.7 | -3655.6+-1055.0 | -6718.3+-607.0 | 1500 |
  | powerlift | 315.9+-16.9 | 99.1+-47.3 | 81.8+-46.7 | 800 |
  | room | 120.5+-71.4 | 131.4+-56.7 | 12.0+-4.9 | 400 |
  | insert_small | 184.8+-26.3 | 129.8+-51.9 | 10.8+-13.4 | 350 |
  | insert_normal | 171.5+-33.2 | 237.6+-9.1 | 46.3+-63.1 | 350 |

  Average return exceeds Target only for walk (DreamerV3, TD-MPC2), stand (TD-MPC2), crawl (DreamerV3, TD-MPC2), sit_simple (DreamerV3); no manipulation task reaches Target on average. Table VI (maximum return) adds push 1000.0+-0.0 (DreamerV3, TD-MPC2), package 1009.2+-4.1 / 1003.3+-3.4, room 420.8 (DreamerV3), pole 952.2, slide 928.4, run 895.9, sit_hard 914.6 (DreamerV3) above Target; cube max 237.9-241.1 vs Target 370; kitchen 0 for all. Fig. 7: with hands vs without vs "Reduced Action Space" (hand actuation fixed to zero, 61D -> 19D, obs kept 151D): "most of the performance drop is indeed due to the increased action dimensionality" (Sec. V-C). Fig. 9: hierarchical DreamerV3 on push "achieving very high success rates"; on package "the policy struggles in lifting it" (Sec. V-D). No numbers for Figs. 7 and 9 in the text.
- baselines beaten: none claimed; the hierarchical variant beats flat RL on push only.
- real robot? None.

## Limitations stated by the authors
Sec. VI "Future work": experiments "only benchmarked the performance of state-based environments"; environments to be extended "to include more realistic objects and environments with real-world diversity and higher-quality rendering"; envisioned "screwing and furniture assembly tasks ... particularly tailored for bimanual manipulation"; focus on RL "because collecting physical demonstrations with humanoid robots is particularly challenging". Sec. III: the forearm-less Shadow Hand "is not currently a realistic model". Sec. V-E common failures: highbar (short-horizon planning), door (pulling needs whole-body retreat), hurdle (never explores jumping).

## Quotable claims (verbatim, with section)
- Abstract: "state-of-the-art reinforcement learning algorithms struggle with most tasks, whereas a hierarchical learning approach achieves superior performance when supported by robust low-level policies, such as walking or reaching."
- Sec. V-B: "All the baseline algorithms perform below the success threshold on most tasks, particularly struggling on tasks that require long-horizon planning and intricate whole-body coordination in a high-dimensional action space."
- Sec. V-B: "Although the hands of the humanoid robot are barely used for most locomotion tasks, the RL algorithms fail to ignore this information, which makes policy learning challenging."
- Sec. V-B: "All the policies barely learn to stabilize using the dense reward, but struggle to learn any complex manipulation skills."
- Sec. V-C: "the presence of hands, with their additional joints and actuators, leads to a large decrease in performance compared to training the same task without the dexterous hands"
- App. B-C: "HumanoidBench can run 1000+ FPS on a single CPU with a simulation timestep of 0.002 s."

## Notes for the survey (which sections this feeds; contradictions with other notes)
- Feeds: bimanual/humanoid benchmark row (two Shadow Hands on H1, MuJoCo 2 ms / 50 Hz, 61-D position control, 27 tasks, 3 seeds, return-based evaluation); the "hands make RL harder" evidence (Fig. 7) for the dimensionality discussion; the hierarchical-vs-flat paragraph.
- Only cube is an in-hand dexterous task; it is unsolved (max return 241 of 370) and its code reward returns no success flag, so no in-hand success rate exists here.
- Evaluation reports returns, not success rates, and the "Target" thresholds are set by the authors per task; contrast with RoboHive's explicit `solved` flags and Bi-DexHands' reward-only reporting.
- Contradictions: paper push reward defaults (alpha_s = 1000) vs shipped DreamerV3 config (success: 10); Robotiq gripper named "2F-85" in Sec. III and "2F-45" in App. A.
- Shadow Hand DoF here is 25 per hand (Table II, includes the wrist as attached), vs 24 in plappert_multigoal_2018 / the vendor spec; the forearm removal changes the kinematic chain.
