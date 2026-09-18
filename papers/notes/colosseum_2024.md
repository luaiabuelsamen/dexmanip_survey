# colosseum_2024 — THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation (Pumacay, Singh, Duan, Krishna, Thomason, Fox; RSS 2024)

sources: papers/md/colosseum_2024.md [ae719563] ; code/md/colosseum_2024.md [098a910a]

## One-line contribution
Extends 20 RLBench tasks with 14 test-time "perturbation_factors" (object/receiver colour, texture, size; light, table, background, distractors, camera pose, friction, mass), evaluates 5 BC/zero-shot policies over 235 test sets x 25 episodes, and shows the simulated drops correlate with a 4-task real Franka mirror (abstract: R̄² = 0.614).

## Setting
- hand(s): none. Parallel gripper on a Franka Panda in both sim (RLBench default) and real (Sec. III.D, IV.E). Single arm.
- simulator / physics: CoppeliaSim via PyRep, as inherited from RLBench (Sec. III.C). No timestep, contact model or env count stated. Assets: 213 textures, 20 colours, 78 YCB distractor models converted to .ttm (Sec. III.C). Compute: baselines trained on 1-4 RTX A6000 for 1-6 days; a full evaluation "4 NVIDIA RTX A6000 over 2-3 days for each model" (App. XI.A).
- observation: "a set RGBD images from a given number of cameras, and robot arm's proprioception" (Sec. IV.A); 4 camera views for the baselines (Sec. IV.B). Real: one front Kinect-2 RGB-D, 512x424 at 30 Hz (App. XII.A).
- action space: keypoint actions, "the 6-DoF gripper pose and it's open or close state" (Sec. IV.A); keypoints found where joint velocities are near zero or gripper state changes. Executed by motion planner (real: MoveIt RRT-Connect, App. XII.C).
- objects / data: 20 tasks curated from RLBench's 100; "over 20,371 unique task instances" (Sec. III); 100 scripted demos per task for training, no perturbations (Sec. IV.D). Real: 5 HTC-Vive demos per task for 4 tasks (Sec. IV.E).

## Perturbation axes (verbatim names, Sec. III.B)
- Manipulation object (MO): `MO_Color`, `MO_Texture`, `MO_Size`
- Receiver object (RO): `RO_Color`, `RO_Texture`, `RO_Size`
- Background: `Light_Color`, `Table_Color`, `Table_Texture`, `Distractor` objects, `Background_Texture`, `Camera_Pose`
- Physical: `Object_Friction`, `Object_Mass`
- Object pose variation is always on and not counted (Table I footnote *).
- Ranges (Sec. III.C): colour/texture sampled from 20 colours / 213 textures; size a per-task continuous scale (e.g. basketball_in_hoop MO_Size [0.75, 1.25], hockey [0.95, 1.05]; full list Table III); light RGB from [0,0,0] to [0.5,0.5,0.5] on all 3 directional lights; camera pose (front, left shoulder, right shoulder) position ±0.1 and Euler ±0.05; friction coefficient in [0.75, 1.0]; mass task-dependent (Table III, e.g. slide_block_to_target [1.0, 15.0]).
- Not all factors apply to all tasks: no RO in open_drawer; PyRep cannot texture/scale compound shapes such as the dishwasher (Sec. III.C). Code exposes each axis as `colosseum/variations/{object_color,object_texture,object_size,light_color,table_color,table_texture,distractor_object,background_texture,camera_pose,object_friction,object_mass}.py`, configured per task by YAML (code file tree; paper Fig. 10).

## Method (baselines, Sec. IV.B-C)
- paradigm: benchmark of behaviour cloning + one zero-shot LLM method. Baselines: R3M-MLP and MVP-MLP (frozen 2D encoders, ~3M-param MLP head, RGB only, batch 32, 300k iters), PerAct (100³ voxel grid, ~33M params, batch 16, 300k iters), RVT (~36M params, batch 24, 100k iters), VoxPoser (zero-shot, manual object-name annotation). Language via frozen CLIP.
- reward or loss: none of the benchmark's own; test-time covariate shift is the object of study: "p(x_test) ≠ p(x_train), but ... p(y_test|x_test) = p(y_train|x_train)" (Sec. III).
- key trick(s): waypoints rescaled or repositioned with object size so RLBench's scripted demo generation still works (Sec. III.C); 3D-printed real objects in 2 extra sizes and 2 alternate colours/textures (Sec. III.D, App. XII.B: scale ±0.2, red and blue filament).

## Evaluation
- protocol (Sec. IV.D, verbatim): "we generate training and test data once and use the last checkpoint for each of the above trained baselines, and evaluate on each of the perturbation_factors. We fix each task to the default RLBench task variations ... However, we do not fix the object pose variations across our test episodes." Test sets: No Perturbation, each single factor, and All Perturbations: "THE COLOSSEUM test sets 235-strong, with 25 episodes per test set."
- success (Sec. IV.D): "A test episode is successful if the model completes the task fully. We report the average success rate for each test set, further averaged across tasks, referred to as task-averaged success rate hereon." Per-task success conditions are RLBench's (App. X), e.g. slide_block_to_target "Some part of the block is inside the specified target area"; open_drawer "The prismatic joint of the specified drawer is fully extended"; close_box "revolute joint ... at least 60° off from the starting position".
- seeds (Sec. IV.D, verbatim): "We report results with one training seed and one evaluation seed over the benchmark per baseline model."
- challenge protocol (Sec. III.E): 100 demos x 20 tasks without perturbations; "evaluate over a fixed 25 episodes set of each of the 14 perturbation_factors"; ranking by "the percentage change in their performance across these perturbation_factors."
- headline numbers: success "degrades between 30-50% across these perturbation factors"; with all factors together "≥ 75%" (abstract, Sec. V.A, Fig. 5). Most damaging: "changing the number of distractor objects, target object color, or lighting conditions" (abstract). 2D models most hurt by object/light colour, texture, camera pose; 3D models (RVT, PerAct) by colour factors and distractors but "robust to changes in Camera_Pose" (Sec. V.A). Per-task absolute rates in Tables IV-VIII; PerAct No-variation column (Table IV) averages to 34.5% over 20 tasks (my sum of the column; 7 of 20 tasks at 0%, including empty_dishwasher, hockey, move_hanger, wipe_desk).
- All-Perturbations ablation (Sec. V.B, Fig. 7): PerAct trained unperturbed scores 6.4% task-averaged under All Perturbations, "28.1% lower than No Perturbations"; training PerAct with All Perturbations enabled "increases by 21.1% only". (Table IV's All-variations column averages to 7.2%, not 6.4%; the Fig. 7 number may be a separate run. Ambiguous.)
- sim-to-real alignment (Sec. IV.E, V.C, Fig. 6): PerAct trained in real (200k iters, batch 1) vs PerAct trained in sim on the same 4 tasks (50k iters, batch 4), "each with 10 episodes, for 3 separate runs" on every factor plus No Perturbation. No-Perturbation gap 6.67%. R² computed per factor with "the success rate performance of each individual run for each task as a data point": 0.46 ≤ R² ≤ 0.52 for MO_Color, Table_Texture, Camera_Pose; 0.74-0.94 for Background_Texture, Distractor, Table_Color, Light_Color, RO_Color, RO_Texture, RO_Size (Table_Color highest). Abstract's R̄² = 0.614 is not derived in the text; presumably the mean over factors. Real MO_Color: 82.6% drop; real MO_Size: +4.34% (Sec. V.C).
- compounding vs natural scenes (Sec. V.D, App. XII.E, Table II): slide_block_to_target, 5 trials x 10 episodes; [Distractor + MO_Size] R² = 0.75, [Light_Color + Table_Texture + Distractor + MO_Size] R² = 0.83, [Distractor + Light_Color] R² = 0.01 (Table II; the text reports only the two high values).
- baselines beaten: not applicable (benchmark paper); ordering 3D (PerAct, RVT) > 2D (R3M, MVP) on both absolute and robustness (Sec. V.A, Fig. 1, Fig. 5).
- real robot? Franka Panda + parallel gripper, 4 tasks (insert onto square peg, slide block to target, scoop with spatula, setup chess), 10 episodes x 3 runs per factor (Sec. IV.E).

## Limitations stated by the authors (Sec. VI)
- Only 4 trained baselines, all BC; RL, diffusion, feature-field and large-pretrained methods not yet on the leaderboard.
- Real world: "a key limitation lies in precisely replicating the pose, orientation, and execution of tasks both in the collected training data and during evaluation"; "each perturbed factor in the real-world setup was limited to only two alternate variations", so real results are "a comparative performance distribution".
- App. IX: factors "do not cover the exhaustive list of factors that vary in the real-world"; chosen because they appear in Open-X, DROID, Ego4D.

## Quotable claims (verbatim, with section)
- "a majority of studies evaluate robot performance in environments closely resembling or even identical to the training setup" (abstract).
- "their success rate degrades between 30-50% across these perturbation factors. When multiple perturbations are applied in unison, the success rate degrades ≥ 75%" (abstract).
- "our results in simulation are correlated (R̄² = 0.614) to similar perturbations in real-world experiments" (abstract).
- "for at least 7 out of 14 perturbation_factors there is a strong correlation between the performances of the two models, thereby indicating a clear alignment between evaluation done on THE COLOSSEUM in simulation and in the real-world" (Sec. V.C).
- "THE COLOSSEUM's perturbation_factors not only study systematic perturbations added to the environment, but also increase the difficulty of the tasks itself, even with ground truth perturbed scenes available for training" (Sec. V.B).
- "We report results with one training seed and one evaluation seed over the benchmark per baseline model" (Sec. IV.D).

## Code notes
- Repo "implements 20 out of the original 100 tasks from RLBench, and extends it by supporting 14 variation factors" (README). `colosseum/rlbench/extensions/environment.py: EnvironmentExt(Environment).__init__(..., vis_random_config, dyn_random_config, ...)` splits visual and dynamic randomisation; `task_environment.py: TaskEnvironmentExt.reset_to_demo(demo)`. Task files (`colosseum/rlbench/tasks/*.py`) define only `init_task/init_episode/variation_count`; success conditions are inherited from RLBench and not shown in the parsed code, so the App. X success metrics cannot be checked against code here. Data generation via `colosseum/tools/dataset_generator.py`, `collect_dataset.sh`. No mismatch with the paper found in what was parsed.

## Notes for the survey
- Evaluation section: the cleanest published template for a perturbation-axis protocol: 14 named axes, single-factor and all-factor test sets, 25 episodes per set, fixed test data, last checkpoint, score = % change vs No Perturbation. Cite the one-seed caveat alongside kress_gazit_policy_eval_2024's trial-count and CI recommendations; COLOSSEUM reports no confidence intervals in sim.
- Sim-to-real: pairs with simpler_2024 (ranking correlation) as evidence that simulated robustness evaluation predicts real drops; note the real side here is 3 runs x 10 episodes on 4 tasks, and 3 of 14 factors correlate only moderately.
- Dexterous gap: gripper only, keypoint actions, no hand; physical perturbations (friction, mass) are the axes most relevant to in-hand manipulation and are the least populated here (only tasks with sliding/lifting, Table III; most baselines score 0 on them, Sec. V.A).
- Related: rlbench_2019 (base tasks, CoppeliaSim), libero_2023 (GROOT row in Table I uses LIBERO), Table I contrasts FactorWorld (11 factors, 19 tasks, MuJoCo) and KitchenShift (7 factors, 3 tasks, Isaac Sim).
