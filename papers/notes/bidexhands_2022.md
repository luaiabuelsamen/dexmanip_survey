# bidexhands_2022 — Towards Human-Level Bimanual Dexterous Manipulation with Reinforcement Learning (Chen, Wu, Wang, Feng, Jiang, McAleer, Geng, Dong, Lu, Zhu, Yang; NeurIPS Datasets and Benchmarks 2022)

sources: papers/md/bidexhands_2022.md [e5691ff2] ; code/md/bidexhands_2022.md [dc41afd1]

## One-line contribution
Bi-DexHands: 20 two-Shadow-Hand manipulation tasks in Isaac Gym (2048 parallel envs, 30k+ FPS on one RTX 3090), ordered by the infant age at which humans acquire the skill (Table 1), with baselines for single-agent RL, MARL, offline RL, multi-task RL and meta-RL; PPO solves most single tasks, MARL narrows the gap on two-hand tasks, multi-task/meta RL largely fail (Abstract, Sec 5).

## Setting
- hand(s): two Shadow Hands; "the 24-DoF hand is actuated by 20 pairs of agonist-antagonist tendons, while the other four joints remain underactuated" (Sec 3). No arm. Bimanual.
  - A.1: thumb 5 DoF/5 joints, each other finger 3 DoF/4 joints with coupled distal joint, LF5 extra little-finger joint, wrist WR1 [-40°,28°], WR2 [-28°,8°] (Table 5).
  - Table 6 DoF properties: stiffness 100 on every joint, friction 0, armature 0; damping WR1 4.78, WR2 2.17, FF2/MF2/RF2/LF2/TH2 "3.4e+38" (as printed; looks like a float-max sentinel), *F3 0.9, *F4 0.725, TH3/TH4 0.99, TH5 0.81.
  - Asset in every yaml: `mjcf/open_ai_assets/hand/shadow_hand.xml` (e.g. code/md line 1818).
  - Base/wrist: "the base of the hand is not fixed in some tasks. Instead, the policy can control the position and orientation of the base within a restricted space" (Sec 3); Hand Over has a fixed base (A.2.1).
  - Code at dc41afd1 also ships `AllegroHandOver.yaml` / `AllegroHandCatchUnderarm.yaml` and `tasks/allegro_hand_*.py` (post-paper; not in the paper).
- simulator / physics: Isaac Gym (Sec 1), PhysX. Hardware i7-9700K + RTX 3090 (Sec 5).
  - Paper: "our low-level controller runs at 1k Hz, as well as the RL-based policy outputs the relative positions of actuated joints at 30 Hz" (Sec 3).
  - Code yaml (all tasks, e.g. `bidexhands/cfg/ShadowHandCatchUnderarm.yaml`): `controlFrequencyInv: 1 # 60 Hz`, `useRelativeControl: False`, `dofSpeedScale: 20.0`, `substeps: 2`; `physx: num_threads 4, solver_type 1 (tgs), num_position_iterations 8, num_velocity_iterations 0, contact_offset 0.002, rest_offset 0.0, bounce_threshold_velocity 0.2, max_depenetration_velocity 1000.0, default_buffer_size_multiplier 5.0`. `randomize: False`.
  - dt is stated nowhere (paper silent; `parse_sim_params` body not in the code extract). MISMATCH: paper 30 Hz relative-position policy vs yaml 60 Hz comment and relative control off.
  - #envs: benchmark at 2048 (Fig 3 caption; README "2048 num_env and 100M total_step"); yaml defaults 256 or 128 per task.
  - Episode length per yaml: Over / Catch Underarm / Over2Underarm / TwoCatch 75; BottleCap / Kettle / Pen / PushBlock / Switch 125; CatchAbreast / Scissors 150; BlockStack, Door x4 250; SwingCup 300; GraspAndPlace / LiftUnderarm 500; ReOrientation 600.
  - Speed (Table 2, FPS mean±std): PPO 35554±613 CatchUnderarm, 35607±344 CatchOver2Underarm, 35164±450 CatchAbreast, 32285±898 TwoCatchUnderarm; HAPPO 23929±98 / 23827±135 / 23456±255 / 23205±168. Abstract "30,000+ FPS"; README "40,000+ mean FPS" (mismatch).
- observation: state only ("We only use the Shadow Hand and object state values as observation at present", A.2). Point-cloud interface exists (Appendix E: PointNet, "only 200+ fps", max 256 envs, below state input on Hand Over, Fig 8).
  - Table 7 per-hand block (199 dims): dof position 24, dof velocity 24, dof force 24, fingertip pose+lin+ang vel 5x13, fingertip force/torque 5x6, base position 3, base rotation 3, actions 26; two hands = indices 0-397.
  - Object/goal block (Table 10): object pose 7, lin vel 3, ang vel 3, goal pose 7, goal rot - object rot 4.
  - Totals stated per task: Hand Over 398 (base fixed, hands "reduced 24 dimensions", Table 8); Catch Underarm / Over2Underarm / Abreast 422; Two Catch Underarm and Re Orientation 446 (two objects); Lift, Door x4, Swing Cup, Scissors, Pen, Switch, Stack Block, Pour Water 428 (+ two handle/part positions); Bottle Cap 414; Push Block 417.
  - A.2 prose says "state space dimension ... up to 400 dimensions in total, and the action space dimension is up to 40", contradicting its own tables (446 / 52).
  - Code docstring `bidexhands/tasks/shadow_hand_over.py::compute_point_cloud_observation` reproduces the 422-dim index table verbatim.
  - MARL obs/state split (README, `MultiVecTaskPython.step`): `hand_obs.append(torch.cat([obs_buf[:, :self.num_hand_obs], obs_buf[:, 2*self.num_hand_obs:]], dim=1))` (right hand; mirrored slice for left), i.e. each agent sees its own hand block plus the object/goal block; `get_state` returns `self.task.states_buf`. Agents are finger/palm groups (`handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"` in every yaml); fully cooperative, "all agents have the same reward" (A.2).
- action space: Hand Over 40 = 20 actuated joints per hand (Table 9). All other tasks 52 = per hand 20 joints + 3 base translation + 3 base rotation (Tables 11, 13, 15, 21, ...).
  - A.2.6 text says Lift Underarm has a "40-dimensional action space" but its Table 19 lists indices 0-51 (52); ambiguous.
  - Base motion scaled per task by yaml `transition_scale` / `orientation_scale`: CatchUnderarm 0.05/0.5, Over2Underarm 0.1/2, Abreast 0.5/1, Door x4 0.5/0.5, Lift 0.25/1, BlockStack 0.2/0.02.
  - Absolute vs relative targets: see the control-rate mismatch above.
- objects / data: YCB and SAPIEN objects (Sec 4.2; README ">2,000 objects"); yaml `objectType` egg / block / pen / pot per task; "each epoch will randomly reset the object's starting pose and target pose" (A.2).
  - Offline datasets (A.3, D4RL-style): random 1e6, replay 1e6, medium 1e6, medium-expert 2e6 samples, for Hand Over and Door Open Outward.
- task list (Fig 3 / Fig 4 order, 20 tasks; A.2 has 17 sub-sections; one `ShadowHand*.yaml` each):
  push block, open pen cap, open scissors, switch, swing cup, lift underarm (pot), door close inward, door open inward, door close outward, door open outward, re orientation, stack block, grasp&place, open bottle cap, hand over, catch underarm, catch over2underarm, catch abreast, pour water (code `ShadowHandKettle`), two catch underarm.
  - Table 1 (age mapping) also names Lift Cup, Stack Block (2,6,8) and "Pull a Ball into Bucket", which have no yaml; Grasp&Place has a yaml but no appendix section.
  - Table 1 ages: Push Block 5-6 mo (easy), Open Scissor / Pen Cap 7, Turn Button 11, Swing Cup 11, Lift Pot 12, Door 13 (easy); Re-Orientation 18, Stack Block 22-42, Open Bottle Cap 30 (medium); Catch Underarm 48, Pour Water 48 (hard); Two Catch Underarm "adult".

## Method
- paradigm: RL benchmark. Implemented: PPO, SAC, TRPO, DDPG, TD3; HAPPO, HATRPO, MAPPO, IPPO, MADDPG; BCQ, TD3+BC, IQL; multi-task PPO/TRPO/SAC; MAML, ProMP (Sec 3). Evaluated in the paper: PPO, SAC, TRPO, MAPPO, HATRPO, HAPPO on all 20 tasks (Sec 5.2); BC / BCQ / TD3+BC / IQL offline (5.3); MT-PPO and ProMP (5.4).
- reward (paper):
  - Catching family, Eq (1)-(3): "r = exp[−0.2(α dt + dr)]", dt = ‖xo − xg‖2, dr = 2 arcsin clamp(‖da‖2, max=1.0), "α is a constant balancing translational and rotational rewards" (A.2.1-A.2.3). Two Catch, Eq (4): sum of two such terms.
  - Lift Underarm, Eq (6): "r = 0.2 − dleft − dright + 3 ∗ (0.985 − dtarget)".
  - Door x4, Bottle Cap, Push Block, Swing Cup, Scissors, Re Orientation, Pen, Switch, Stack Block, Pour Water: dtarget / dleft / dright defined in words, but the displayed equations are blank in the markdown (lost in conversion). Only the structure survives: "the distance from the left hand to the target point on the object ..., the distance from the right hand ..., and the distance from the object to the target" (A.2).
  - MT20 rescales rewards of Grasp&Place, Door x4, Bottle Cap, Block Stack, Lift Underarm, Re Orientation, Scissors, Swing Cup by 0.1 (D.2).
- reward (code):
  - `bidexhands/tasks/shadow_hand_over.py::compute_hand_reward` (same body in `shadow_hand_catch_underarm.py`, `_catch_abreast.py`, `_catch_over2underarm.py`):
    `goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)`; `rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))`; `reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))`. α = yaml `distRewardScale` = 50 (Over, CatchUnderarm, CatchAbreast, TwoCatch) or 20 (Over2Underarm). `action_penalty` is computed but unused.
  - `shadow_hand_two_catch_underarm.py`: `reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist)) + torch.exp(-0.2*(goal_another_dist * dist_reward_scale + rot_another_dist))` (matches Eq 4).
  - `shadow_hand_lift_underarm.py` (body truncated in the extract): `up_rew = torch.where(right_hand_dist < 0.08, torch.where(left_hand_dist < 0.08, 3*(0.385 - goal`... — lift term gated on both hands within 8 cm of the handles and uses 0.385, not the paper's ungated 0.985 (MISMATCH, partially visible).
  - `shadow_hand_re_orientation.py`: `dist_rew = goal_dist * dist_reward_scale + goal_another_dist * dist_reward_scale`; `rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale + 1.0/(torch.abs(rot_another_dist) + rot_eps) * rot_reward_scale`; `reward = dist_rew + rot_rew + action_penalty * action_penalty_scale` (yaml distRewardScale -10, reachGoalBonus 500, fallDistance 0.24) — an inverse-rotation form, not the "2∗arcsin" description in A.2.13.
  - Door and Stack Block bodies (visible head): per-finger terms `right_hand_finger_dist = Σ_{ff,mf,rf,lf,th} ‖handle − fingertip‖`, never mentioned in the paper.
- key trick(s): GPU-resident training; all tasks of an MT/ML set loaded in one Isaac Gym instance and sampled synchronously (D.1); multi-task adds a one-hot task ID, meta masks goal info (D.2).
  - PPO Table 42: hidden [1024,1024,512], lr 3e-4, γ 0.96 (0.9 Stack Block), λ 0.95, clip 0.2, nsteps 8 (20 Lift), desired KL 0.016, ent 0; code `cfg/ppo/config.yaml` matches (max_iterations 6500).
  - HAPPO Table 44: lr 1e-4, max grad norm 1; code `cfg/happo/config.yaml`: lr 5e-4, max_grad_norm 10, num_env_steps 50M, n_rollout_threads 80 (MISMATCH with paper's 100M / 2048). SAC Table 43: buffer 5000, batch 32, ent 0.2.

## Evaluation
- metrics (exact definitions): episode reward only; no success rate anywhere in the paper.
  - Fig 3: reward curves. Table 3: "normalized score = 100 ∗ (return − random return)/(expert return − random return)" (A.3). Table 4: "average reward". Fig 4: "score = (reward − random reward)/(ground truth reward − random reward)".
  - Code success is a distance threshold, not a reward threshold: `successes = torch.where(successes == 0, torch.where(goal_dist < 0.03, torch.ones_like(successes), successes), successes)` (3 cm on object-goal position, orientation ignored) in hand_over / catch_underarm / catch_over2underarm / catch_abreast; exported as `self.extras['successes']`, unused in the paper.
  - `goal_resets = torch.where(torch.abs(goal_dist) <= 0, ...)` can never trigger, so `reachGoalBonus: 250` is dead; `successTolerance: 0.1` only enters the `max_consecutive_successes > 0` branch (yaml `maxConsecutiveSuccesses: 0`).
  - Episode ends on drop: `object_pos[:, 2] <= 0.2` (Over) / `<= 0.1` (CatchUnderarm), `fallPenalty: 0.0`. Lift / Door / Stack bodies are truncated in the extract; their success rule is not visible.
- headline numbers:
  - Sec 5.2 / Fig 3 (10 trials, 100M steps, 2048 envs): curves only, no table. "PPO algorithm performs well on most tasks ... better than HAPPO, MAPPO algorithms in most cases"; "the more difficult and require the cooperation of both hands, the smaller the performance gap between PPO and HAPPO, MAPPO"; "SAC algorithm does not work on almost all tasks". DDPG, TD3, IPPO, MADDPG: implemented, not evaluated.
  - Table 3 (normalized score, mean±std; BC / BCQ / TD3+BC / IQL; Online PPO = 100): Hand Over random 0.7±0.2 / 1.0±0.1 / 0.9±0.2 / 0.7±0.4; replay 17.5±3.5 / 61.6±4.9 / 70.1±2.1 / 43.1±2.3; medium 61.6±1.0 / 66.1±1.9 / 65.8±2.2 / 57.4±1.5; medium-expert 63.3±1.4 / 81.7±4.9 / 84.9±5.3 / 67.2±3.6.
  - Table 3, Door Open Outward: random 2.1±0.6 / 23.8±2.9 / 34.9±4.3 / 3.8±1.0; replay 36.9±4.3 / 48.8±4.5 / 60.5±2.6 / 31.7±2.0; medium 63.9±0.7 / 60.1±2.3 / 66.3±0.7 / 56.6±1.2; medium-expert 69.0±6.4 / 73.7±4.5 / 71.9±3.5 / 53.8±1.8.
  - Table 4 (average reward, 10 seeds): MT1 / MT4 / MT20 ground truth 15.2 / "24,3" (typo, presumably 24.3) / 32.5; MT-PPO 9.4 / 5.4 / 8.9; random 0.61 / 1.1 / -2.5.
  - Table 4, meta (train/test): ML1 ground truth 15.0/15.8, ProMP 0.95/1.2, random 0.59/0.68; ML4 28.0/13.1, 2.5/0.5, 1.5/0.24; ML20 33.7/26.1, 0.02/0.36, -2.9/0.27. Column headers are garbled ("ML<br>train|1<br>test|M<br>train|L4<br>test"); assignment inferred from order.
  - Fig 4 (MT20 normalized reward, age order): picture text gives 0.99, 0.81, 0.82, 0.7, 0.43, 0.47, 0.42, 0.17, 0.21, 0.18, 0.13, 0.2, 0.08, then 0.00075-0.031 for the oldest-age tasks; per-task mapping not recoverable from the flattened figure.
- baselines beaten: none claimed; benchmark paper. Offline: TD3+BC / BCQ > BC on replay and medium-expert, IQL only "in several datasets" (5.3). ProMP has "tiny performance improvement compared with random policy" (5.4).
- real robot? No. Sec 6: state-based observations are "difficult for sim-to-real transfer"; sim-to-real is future direction 4.

## Limitations stated by the authors
- No deformable objects: "our tasks currently only cover articulated rigid body object manipulation" (Sec 6).
- State-based observation only; visual/point-cloud RL runs at ~200 FPS and is capped at 256 envs because Isaac Gym renders cameras serially (Appendix E).
- SAC fails on almost all tasks; attributed to off-policy gaining less from 2048 envs and to entropy instability with 50+-dim actions (Appendix C, Fig 6 on Humanoid).
- Multi-task PPO and ProMP fail on MT4 / MT20 / ML4 / ML20 (Table 4, Sec 5.4, Sec 6).
- Reward hyper-parameters differ per task despite the "unified reward function structure" (A.2).

## Quotable claims (verbatim, with section)
- "Bi-DexHands can reach 30,000+ mean FPS by running 2,048 environments in parallel" (Sec 1).
- "the PPO type of on-policy algorithms can master simple manipulation tasks that are equivalent up to 48-month human babies (e.g., catching a flying object, opening a bottle), while multi-agent RL can further help to master manipulations that require skilled bimanual cooperation (e.g., lifting a pot, stacking blocks)" (Abstract).
- "existing RL algorithms fail to work in most of the multi-task and the few-shot learning settings" (Abstract).
- "This may be because PPO algorithm is able to use all observations for training the policy, while MARL can only use partial observations" (Sec 5.2).
- "in bimanual dexterous robot hand manipulation, the current reinforcement learning can reach the level of 48-months infants" (Sec 6).

## Notes for the survey
- Feeds: benchmarks/simulators table (Isaac Gym, two Shadow Hands, 20 tasks, 2048 envs); bimanual section; MARL-for-hands; offline-RL datasets for hands; multi-task/meta negative results.
- Everything reported is reward, not success. Any "success rate" quoted for Bi-DexHands by later papers comes from the 3 cm `goal_dist < 0.03` code flag (catching family only) or from their own definition, not from this paper.
- Paper-vs-code mismatches to carry: 30 Hz relative control (paper) vs `controlFrequencyInv: 1 # 60 Hz`, `useRelativeControl: False` (yaml); Lift reward 0.985 ungated (paper) vs gated 0.385 (code); Re Orientation reward form; HAPPO lr / grad-norm / steps; FPS 30k (paper) vs 40k (README); dt never stated.
- Physics detail relevant to interpenetration work: TGS solver, 8 position / 0 velocity iterations, contact_offset 2 mm, rest_offset 0, substeps 2; no contact or penetration term in any reward; per-joint stiffness 100 with damping printed as 3.4e+38 on the *F2/TH2 joints (Table 6), to be treated as a table artifact until checked against the MJCF.
- Contrast with single-hand in-hand reorientation benchmarks (OpenAI-style `rot_rew = 1/(|rot_dist|+eps)`): only Re Orientation keeps that form here; the catching tasks use exp(−0.2(α d_t + d_r)) with α = 20-50.
