# unidexgrasp_pp_2023 — UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning (Wan et al., ICCV 2023)

sources: papers/md/unidexgrasp_pp_2023.md [12f8ed95] ; code/md/unidexgrasp_pp_2023.md [6c9e710b]

## One-line contribution
GeoCurriculum (geometry-feature task curriculum, replacing category-label object curriculum) plus GiGSL (geometry-aware iterative generalist-specialist learning via a DAgger variant that also distills the critic) raise the UniDexGrasp benchmark's state-based success from 79.4/74.3/70.8% to 87.9/84.3/83.1% and vision-based from 73.7/68.6/65.1% to 85.4/79.6/76.7% (train / unseen-object-seen-category / unseen-category, Table 1).

## Setting
- hand(s): Shadow Hand (`mjcf/open_ai_assets/hand/shadow_hand.xml`, code `cfg/shadow_hand_grasp.yaml`); 24 actuated DoF (App. B.1: "first 6 motors control the global position and orientation ... rest 18 motors control the fingers"); floating base, no arm; single hand.
- simulator / physics: Isaac Gym / PhysX, `ShadowHandGrasp` task, non-goal-conditioned (`goal_cond: False`, code cfg).
  - `sim.physx`: substeps 2, solver_type 1 (TGS), num_position_iterations 8, contact_offset 0.002, rest_offset 0.0, max_depenetration_velocity 1000.0 (code cfg).
  - sim timestep not stated directly; `controlFrequencyInv: 1` with an in-file comment "60 Hz" (code cfg).
  - #envs: 1024 (state-based PPO/GeoCurriculum) vs 32 (vision-based) (Table 5).
  - GPU/wall-clock: "four NVIDIA RTX 3090 Ti"; "20,000 environment steps in the first stage of GeoCurriculum and 15,000 environment steps (for every single policy) in other stages ... two days in total" (App. B.2).
- observation:
  - state-based S_t^S=(R_t,O_t,P_t=0): robot state R_t per Table 4 — joint positions q∈R18, joint velocities q̇∈R18, dof force τ_dof∈R24, fingertip position/orientation/lin-vel/ang-vel/force/torque each ×5 fingertips, hand-root translation t∈R3, hand-root rotation R∈R3×3, action a∈R24 — plus object oracle state O_t (3-DoF position + 9-DoF rotation matrix + linear/angular velocity), plus a frozen point-cloud-autoencoder feature z of the first-frame scene cloud (Sec. 4.1, App. B.1).
  - vision-based S_t^V=(R_t,P_t): robot state R_t + a panoramic cloud fused from 5 fixed RGBD cameras, downsampled to 1024 points from object+hand (Sec. 5.1, App. B.1), encoded with a PointNet+Transformer backbone (Sec. 5.1, App. B.2).
- action space: 24-D motor command normalised to (−1,1) "based on actuator specification" (App. B.1); first 6 = hand-root position/orientation, remaining 18 = finger joints. Whether these are position, velocity or torque targets is not stated in the paper text beyond "motor command".
- objects / data: UniDexGrasp benchmark, "3165 different object instances spanning 133 categories" (Sec. 5.1), non-goal-conditioned only ("ground-truth grasp pose generation for pretraining and point cloud rendering ... are very expensive ... we only consider the non-goal conditioned setting", Sec. 5.1).
  - three splits by config file: `train_set.yaml`, `test_set_seen_cat.yaml` (unseen objects / seen categories), `test_set_unseen_cat.yaml` (unseen categories) (code file tree; Table 1 column headers).
  - exact per-split object counts are **not stated**: the paper only gives the 3165/133 aggregate, and the two test-set yaml files list individual object codes but the code/md extraction truncates both lists before they finish, so a count cannot be verified from source.
  - N_train (curriculum's final task count, Table 5) = 3200, which does not equal the 3165-instance total in Sec. 5.1 — the paper does not reconcile the discrepancy.

## Method
- paradigm: state-based RL (PPO) → DAgger+critic distillation → iterative specialist-RL/generalist-distillation (GiGSL) → repeated for a vision-based generalist (Sec. 4.1, Fig. 2, Algorithm 3).
  - not a generative-model grasp pipeline: unlike UniDexGrasp's goal-conditioned CVAE-proposal setting, this paper only uses the "non-goal conditioned setting in UniDexGarsp which does not specify the grasping hand pose" (Sec. 5.1) — the hand always starts at one fixed pose above the table (Sec. 3), and the grasp itself is discovered purely by RL/distillation; there is no learned grasp-pose generator anywhere in the pipeline.
- grasp-pose mechanism, precisely — two distinct clustering uses, neither of which is grasp generation:
  1. GeoCurriculum orders *tasks* (object instance + random SO(3) drop pose), not grasp poses, into a 4-level curriculum with task counts 1→300→900→N_train (Algorithm 2, App. A.1), by K-Means-clustering the latent feature z of each task's first-frame scene cloud from a frozen point-cloud autoencoder (trained with Chamfer-distance reconstruction loss on ~270,000 sampled tasks, Sec. 4.3, N_sample=270,000 Table 5), then picking the task nearest each (sub-)cluster centroid at each level.
  2. GiGSL/GeoClustering assigns each of the effectively-infinite tasks online to one of N_clu=20 specialists by nearest K-Means cluster center in that same geometry-feature space (state-based: autoencoder feature z; vision-based: the trained vision backbone's feature f) (Sec. 4.3, Algorithm 1).
  - specialists are PPO-finetuned per cluster, then distilled back into one generalist with the paper's DAgger+critic method; the G→S→G→S… cycle repeats until success-rate gain <0.5% between iterations (App. A.1), for both state and vision stages.
  - net effect: state-only geometric clustering + iterative RL/distillation, no generative grasp-proposal model, no clustering of hand poses themselves — only clustering of object/pose *tasks*.
- algorithm: PPO [55] for all specialist RL; DAgger [51]-based distillation extended to also regress a critic — actor loss = MSE(π_teacher(s), π_θ(s)), critic loss = MSE(V_φ(s), R̂_t) with R̂_t from GAE (Sec. 4.2) — so the distilled generalist keeps a usable value function and can resume actor-critic RL (contrast with plain DAgger/GAIL/DAPG in GSL[29] and ILAD[69]).
  - state-based specialists distill directly to the vision-based generalist VG1 ("end-to-end distillation"), shown to beat state-generalist-then-vision distillation (Table 2 rows 5/6 & 9/12).
- privileged info: exactly the object oracle state O_t (pose, linear/angular velocity), available to the state-based policy and withheld from the vision-based policy (Sec. 4.1); nothing else is privileged.
- domain randomisation: `task.randomize: False` by default in `cfg/shadow_hand_grasp.yaml` — unclear whether ever switched on for reported numbers — but the file defines these ranges, all with 30,000–40,000-step linear schedules:
  - observation noise: additive Gaussian [0,.002] + correlated [0,.001]; action noise: [0,.05] + [0,.015]; gravity: additive [0,0.4].
  - hand tendon/dof damping: loguniform ×[0.3,3.0]; stiffness: loguniform ×[0.75,1.5].
  - hand & object rigid-body mass: uniform ×[0.5,1.5]; hand & object friction: uniform ×[0.7,1.3] (250 buckets); object scale: uniform ×[0.95,1.05].
- reward / objective (verbatim, paper + code):
  - paper (App. B.1) — the display equations are dropped by the PDF-to-markdown conversion, only prose survives: "The lifting reward r_lift encourages the robot hand to lift the object when the fingers are close enough to the object. f is a flag to judge whether the robot reaches the lifting condition ... a_z is the scaled force applied to the hand root along the z-axis (ω_l>0)"; "The moving reward r_move encourages the object to reach the target and it will give a bonus term when the object is lifted very closely to the target"; "Finally, we add each component and formulate our reward function as follows:" (equation itself not recovered). Table 5 gives the weights ω_r=0.5, ω_l=0.1, ω_m=2, ω_b=10, but the paper text never states in prose which symbol multiplies which named term beyond the lift/move descriptions above.
  - code (`dexgrasp/tasks/shadow_hand_grasp.py:compute_hand_reward`, `goal_cond=False` branch, which is what this benchmark uses per cfg):
    ```
    right_hand_dist = clamp(||object_handle_pos − right_hand_pos||, max 0.5)
    right_hand_finger_dist = clamp(Σ||object_handle_pos − {ff,mf,rf,lf,th}_pos||, max 3.0)
    flag = (right_hand_finger_dist<=0.6) + (right_hand_dist<=0.12)
    goal_hand_rew = 0.9 − 2*goal_dist            if flag==2 else 0
    hand_up       = 0.1 + 0.1*actions[:,2]       if lowest>=0.630 and flag==2 else 0
    hand_up       = 0.2                          if lowest>=0.80  and flag==2 (overrides prior)
    reward = −0.5*right_hand_finger_dist − 1.0*right_hand_dist + goal_hand_rew + hand_up + bonus − 0.5*delta_value
    ```
    the `goal_cond=True` branch (unused here) additionally gates on hand-pose/qpos deltas and adds `bonus=1/(1+10*goal_dist)` when `goal_dist<=0.05`. `action_penalty = Σ actions**2` is computed but not visibly folded into `reward` in the captured lines.
  - cfg `shadow_hand_grasp.yaml` separately exposes `distRewardScale:20, rotRewardScale:1.0, rotEps:0.1, actionPenaltyScale:-0.0002, reachGoalBonus:250, fallDistance:0.4, fallPenalty:0.0, successTolerance:0.1`, passed into `compute_hand_reward`'s signature, but none of these names appear in the reward-composition lines actually captured — they are presumably consumed by the success/reset logic that the code/md extraction truncates before reaching (see reproducibility, below).
  - **mismatch**: the paper's named weights (0.5, 0.1, 2, 10) numerically match the code's hardcoded literals (−0.5×finger_dist, 0.1+0.1×action, the 2 in "0.9−2·goal_dist", the 10 in the bonus) but the code never assigns them as named variables — the correspondence is inferred here, not labelled in either source.
- key trick(s): jointly training the critic during DAgger distillation, the paper's central claimed advance over GSL[29]/ILAD[69] (Sec. 4.2); using a frozen geometry-feature space (autoencoder for state, vision backbone for vision) in place of category labels for both curriculum ordering and specialist-task assignment (Sec. 4.3/4.4).
- contact / penetration handling: not addressed as a reward term — no penetration or interpenetration penalty/measurement appears anywhere in the paper text or the extracted reward code. Only generic PhysX contact-solver settings are given: `contact_offset: 0.002`, `rest_offset: 0.0`, `max_depenetration_velocity: 1000.0`, `solver_type: 1` (TGS), `num_position_iterations: 8` (code cfg).

## Evaluation
- metrics (exact definitions): "Average Success Rate of the Evaluated Objects" (Table 1 caption) on train / unseen-object-seen-category / unseen-category splits.
  - success criterion, Sec. 3: "The task is successful if the position difference between the object and the target is smaller than a threshold value" — purely geometric (object-to-target position distance), no hold-duration condition stated in the paper text.
  - closest concrete numeric threshold in the sources: `successTolerance: 0.1` (units not stated, presumed metres since `goal_dist` is a Euclidean position norm), plus `fallDistance: 0.4`/`fallPenalty: 0.0` for episode-ending drops, and the code's height gates `lowest>=0.630`/`lowest>=0.80` that switch on the "hand_up"/lift reward term.
  - no physical grasp-quality check (e.g. re-perturbation, force closure, contact-force measurement) is reported anywhere in the sources — success is checked geometrically only, via object-target distance and these height gates.
  - episode length 200 steps (Table 5). Number of evaluation episodes or seeds per object is not stated.
- headline numbers, Table 1 (success %, Train / Uns.Obj.SeenCat / Uns.Cat):

  | model | train | uns. obj. | uns. cat. |
  |---|---|---|---|
  | PPO[55] | 24.3 | 20.9 | 17.2 |
  | DAPG[49] | 20.8 | 15.3 | 11.1 |
  | ILAD[69] | 31.9 | 26.4 | 23.1 |
  | GSL[29] | 57.3 | 54.1 | 50.9 |
  | UniDexGrasp[70] | 79.4 | 74.3 | 70.8 |
  | **Ours (state-based)** | **87.9** | **84.3** | **83.1** |
  | PPO+DAgger | 20.6 | 17.2 | 15.0 |
  | DAPG+DAgger | 17.9 | 15.2 | 13.9 |
  | ILAD+DAgger | 27.6 | 23.2 | 20.0 |
  | GSL+DAgger | 54.1 | 50.2 | 44.8 |
  | UniDexGrasp[70] (vision) | 73.7 | 68.6 | 65.1 |
  | Ours (state)+DAgger | 77.4 | 72.6 | 68.8 |
  | **Ours (vision-based)** | **85.4** | **79.6** | **76.7** |

  Table 2 ablation (state-based): +GeoCurriculum alone 82.7/76.8/74.2; +iterative fine-tuning 84.0/77.9/74.8; +GeoClustering (full) 87.9/84.3/83.1.
  Table 6 (curriculum ablation): no-curriculum 30.5/23.4/20.6 vs OCL[UniDexGrasp] 79.4/74.3/70.8 vs 4-stage GeoCurriculum 82.7/76.8/74.2 (3-stage 81.3/75.6/73.3, 5-stage 82.9/76.4/74.0).
  Table 7 (distillation-method ablation): BC+Value 12.4/8.6/8.4; GAIL 30.7/26.9/26.0; DAPG 61.4/52.6/47.9; Ours 87.9/84.3/83.1.
  Table 8 (N_clu ablation, vision-based): N_clu=0 77.4/72.6/68.8; N_clu=10 80.3/74.9/75.2; N_clu=20 85.4/79.6/76.7.
  Table 3 (Meta-World MT-10, mean±std): PPO 58.4±10.1; GSL 77.5±2.9; Ours 80.3±0.5.
- baselines beaten: PPO, DAPG, ILAD, GSL — re-implemented/re-run by the authors (Sec. 5.2, App. A.2 describes each baseline's re-implementation); UniDexGrasp's numbers are quoted, not stated as re-run.
- real robot? None reported. Sec. 6: "The limitation is that we only tackle the dexterous grasping task in simulation and we will conduct the real-robot extension in our future work."
- reproducibility: code released (github.com/PKU-EPIC/UniDexGrasp2, commit 6c9e710b).
  - checkpoints: "We provide our trained state-based policy checkpoint at dexgrasp/state_based_model" plus per-split result YAMLs (`results/state_based/{train_set,test_set_seen_cat,test_set_unseen_cat}_results.yaml`) — no vision-based checkpoint is mentioned as released.
  - dataset assets are external (mirror + Google Drive `datasetv4.1_posedata.npy`), not bundled. Scripts exist for all four training stages (`run_train_ppo_state.sh`, `run_train_dagger_state.sh`, `run_train_dagger_state_to_vision.sh`, `run_train_ppo_vision.sh`) with `--test` for evaluation.
  - of the paper's tables, only the state-based row of Table 1 is directly reproducible from the released checkpoint + result YAMLs; the vision-based generalist and all ablations (Tables 2/3/6/7/8) have no released checkpoint in the extracted README.
  - the success/reset logic that would confirm how `successTolerance`/`fallDistance`/`reachGoalBonus` are actually used is cut off by the code/md extraction and could not be verified.

## Limitations stated by the authors
Sec. 6 only: "The limitation is that we only tackle the dexterous grasping task in simulation and we will conduct the real-robot extension in our future work." No other stated limitations; no discussion of penetration, grasp physical plausibility, or failure modes anywhere in the extracted text.

## Quotable claims (verbatim, with section)
- Abstract: "our final policy shows universal dexterous grasping on thousands of object instances with 85.4% and 78.2% success rate on the train set and test set which outperforms the state-of-the-art baseline UniDexGrasp by 11.7% and 11.3%, respectively."
- Sec. 1: "One limitation of UniDexGrasp is that its state-based teacher policy can only reach 79.4% on the training set ... Another limitation in the object curriculum is unawareness of object pose and reliance on category labels."
- Sec. 4.3: "we are dealing with an infinite number of tasks considering the initial object pose can change continuously."
- Sec. 5.1: "we only consider the non-goal conditioned setting in UniDexGarsp which does not specify the grasping hand pose."
- Sec. 6: "We believe such generalizability is also essential for Sim2Real transfer for real robot dexterous grasping."

## Notes for the survey (which sections this feeds; contradictions with other notes)
- Feeds: the generalist-specialist/distillation-with-critic method row of the RL-pipeline comparison table; the geometry-feature-clustering-vs-category-label curriculum discussion; the "no generative grasp-pose model, task curriculum instead" contrast point against goal-conditioned pipelines (e.g. original UniDexGrasp's CVAE proposal stage, explicitly avoided here per Sec. 5.1).
- Explicit deltas over UniDexGrasp, same 3165-object/133-category benchmark, non-goal-conditioned (Table 1, Sec. 1/5.2):
  - state-based: 87.9/84.3/83.1 vs 79.4/74.3/70.8 (raw deltas +8.5/+10.0/+12.3 pts; authors describe this in prose as a "9% and 11% improvement", Sec. 5.2).
  - vision-based: 85.4/79.6/76.7 vs 73.7/68.6/65.1 (raw deltas +11.7/+11.0/+11.6 pts; abstract quotes "11.7%" and "11.3%" — the train-set figure matches exactly but the quoted test figure does not cleanly match either test column, an inconsistency worth flagging before citing it downstream).
- Caution for the survey: the reward equations are unrecoverable from the PDF extraction (converter dropped all LaTeX display equations); only prose plus the four named weights survive, so any restatement of "the reward function" for this paper should cite the code (`compute_hand_reward`) as primary, not the paper's equations.
- Held-out object/category counts per split are not stated anywhere in the sources read here (only the 3165/133 aggregate) — do not quote a per-split count for this paper without returning to the original UniDexGrasp release.
- This is the first note filed for the UniDexGrasp family in this survey (no `unidexgrasp_2023` note exists yet to cross-check), so no contradictions with other notes could be checked.
