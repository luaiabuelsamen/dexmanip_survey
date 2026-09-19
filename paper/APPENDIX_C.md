## Appendix C. Per-paper reward term extraction

Table 5 marks nine recurring term families across the in-hand reorientation methods. This appendix is the extraction underneath it, over every method row that records a reward at all. `terms stated` counts the terms the paper itself names. `where the reward was read` gives the section of the paper or the file in the released code that the note quotes. A row with a `paper/code class` is one where the two disagree, and C.2 prints the disagreement in full. Cells and entries reproduce the text stored in the row, with the source's own punctuation and wording.

### C.1 The extraction

| method | yr | paradigm | terms stated | term names as the paper names them | where the reward was read | in Table 5 | code released | paper/code class | confidence |
|---|---|---|---|---|---|---|---|---|---|
| `openai_dexterity_2018` | 2018 | RL | 3 |   | Method, reward (Sec 4.2 / App C.1) | yes | no |   |   |
| `openai_rubiks_cube_2019` | 2019 | RL, distillation | 3 |   | Method, reward (Sec. 6.1) | yes | no |   |   |
| `pddm_2019` | 2019 | MPC |   |   |   |   | yes | contradiction | high |
| `dexpoint_2022` | 2022 | RL | 4 | reach, contact, lift, action penalty |   |   | yes | contradiction | high |
| `dextreme_2022` | 2022 | RL | 6 |   | Reward block, paper Table 2 against allegro_hand_dextreme.py and the two DR yamls | yes | yes | contradiction | high |
| `dexvip_2022` | 2022 | RL | 4 |   |   |   | no |   |   |
| `hora_2022` | 2022 | RL, distillation | 5 |   | Block C, paper Sec 3.1/App. C against configs/task/AllegroHandHora.yaml | yes | yes | version-skew | high |
| `mjpc_2022` | 2022 | MPC | 3 |   |   |   | yes |   |   |
| `visual_dexterity_2022` | 2022 | RL, distillation | 7 | c1_sparse_task, c2_dense_task, c3_fingertip_dist, c4_energy, c5_push_away_penalty, c6_table_contact, c7_finger_height | Method, Table S1 against dexenv/envs/rewards.py and dexenv/conf/task/dclaw.yaml | yes | yes | contradiction | high |
| `aloha_act_2023` | 2023 | BC |   |   |   |   | yes | internal-inconsistency | high |
| `artigrasp_2023` | 2023 | RL | 4 | r_p, r_c, r_reg, r_task |   |   | yes | parse-limitation | low |
| `dexpbt_2023` | 2023 | RL | 4 | r_reach, r_pick, r_targ, r_vel | Block C, paper Sec III-C/Table II against allegro_kuka_base.py and AllegroKuka.yaml | yes | yes | contradiction | high |
| `dexterous_functional_grasping_2023` | 2023 | RL | 2 | r_threshold, r_hand-obj |   |   | no |   |   |
| `diffusion_policy_2023` | 2023 | BC, diffusion |   |   |   |   | yes | parse-limitation | high |
| `dynamic_handover_2023` | 2023 | RL | 3 |   |   |   | no |   |   |
| `eureka_2023` | 2023 | RL |   |   | Method, App. G.1/G.2 LLM-authored rewards; generated code not checked into the repo | yes | yes | parse-limitation | low |
| `pgdm_2023` | 2023 | RL | 2 |   |   |   | no |   |   |
| `physhoi_2023` | 2023 | RL | 4 | body motion reward, object motion reward, ig reward, cg reward |   |   | yes | contradiction | high |
| `robot_synesthesia_2023` | 2023 | RL, distillation | 6 |   | Method, reward (Sec IV.A.3 eq. 1); no code released | yes | no |   |   |
| `rotateit_2023` | 2023 | RL, distillation | 6 |   | Block C (paper Sec 3.1, App. B); no code released | yes |   |   |   |
| `rotating_without_seeing_2023` | 2023 | RL | 6 | r_rot, r_vel, r_fall, r_work, r_torque, r_dist | Reward block (Sec IV.A.3, App. D Eq. 9); no code released | yes |   |   |   |
| `unidexgrasp_2023` | 2023 | grasp-synthesis, RL, distillation | 4 | goal, reach, lift, move |   |   | yes | contradiction | high |
| `unidexgrasp_pp_2023` | 2023 | RL, distillation | 4 | r_reach, r_lift, r_move, r_bonus |   |   | yes | parse-limitation | low |
| `anyrotate_2024` | 2024 | RL, distillation | 10 | keypoint distance reward, rotation reward, goal bonus reward, good contact reward, bad contact penalty, angular velocity penalty, pose penalty, work penalty, torque penalty, termination penalty | Block C (App. B.1 weights); no code released | yes | no |   |   |
| `asymdex_2024` | 2024 | RL | 4 |   |   |   | yes | code-absent | medium |
| `bidexhd_2024` | 2024 | RL, distillation | 4 | r_appro, r_lift, r_bonus, r_track |   |   | yes | parse-limitation | high |
| `bimangrasp_2024` | 2024 | grasp-synthesis, diffusion | 7 |   |   |   | no |   |   |
| `demostart_2024` | 2024 | RL, distillation | 1 |   | Method, reward (App. VII-A.1); no code released | yes | no |   |   |
| `dexmimicgen_2024` | 2024 | data-collection, BC | 1 |   |   |   | yes | code-absent | high |
| `dp3_2024` | 2024 | BC, diffusion |   |   |   |   | yes | internal-inconsistency | medium |
| `dreureka_2024` | 2024 | RL | 4 | ang_z_vel_reward, lin_vel_penalty, object_fall_penalty, deviation_penalty | Method, App. B1 Prompt 13; cube-rotation code absent from the released repo | yes | yes | code-absent | high |
| `graspxl_2024` | 2024 | RL | 8 | r_dis, r_v, r_ω, r_m, r_c, r_f, r_reg, r_anatomy |   |   | yes | parse-limitation | low |
| `hudor_2024` | 2024 | RL | 1 |   |   |   | no |   |   |
| `humanplus_2024` | 2024 | RL, BC | 8 |   |   |   | yes | parse-limitation | medium |
| `objdex_2024` | 2024 | BC, RL, distillation | 3 | rotation, translation, joint angle |   |   | no |   |   |
| `omnigrasp_2024` | 2024 | RL, distillation | 3 | r_approach, r_pre-grasp, r_obj |   |   | yes | parse-limitation | medium |
| `omnih2o_2024` | 2024 | RL, distillation | 24 |   |   |   | yes | internal-inconsistency | medium |
| `open_television_2024` | 2024 | teleop-system, BC |   |   |   |   | yes | code-absent | low |
| `penspin_2024` | 2024 | RL, distillation | 7 |   | Method, paper Table 4 against penspin/tasks/allegro_hand_hora.py and configs/task/AllegroHandHora.yaml | yes | yes | contradiction | medium |
| `pi0_2024` | 2024 | VLA, flow |   |   |   |   | yes | version-skew | high |
| `pianomime_2024` | 2024 | RL+demo, distillation | 2 |   |   |   | yes | contradiction | high |
| `resdex_2024` | 2024 | RL, distillation | 7 | task, proposal, pose, reach, lift, move, bonus |   |   | yes | parse-limitation | medium |
| `twisting_lids_2024` | 2024 | RL | 5 |   |   |   | no |   |   |
| `articulated_tools_inhand_2025` | 2025 | RL, BC, distillation | 8 | r_pos, r_quat, r_goal, r_timer, r_inc, r_contact, r_slip, r_act |   |   | no |   |   |
| `being_h0_2025` | 2025 | VLA, BC |   |   |   |   | yes | code-absent | high |
| `clutterdexgrasp_2025` | 2025 | RL, diffusion, distillation | 4 | r_pos, r_neg, r_grasp, r_force |   |   | no |   |   |
| `cross_embodiment_world_models_2025` | 2025 | world-model, MPC | 2 |   |   |   | no |   |   |
| `dexgraspvla_2025` | 2025 | VLA, diffusion | 1 |   |   |   | yes | parse-limitation | high |
| `dexmachina_2025` | 2025 | RL | 4 |   |   |   | yes | internal-inconsistency | low |
| `dexman_2025` | 2025 | RL, trajopt | 3 |   |   |   | no |   |   |
| `dexndm_2025` | 2025 | RL, distillation | 7 |   | Reward block (Sec. 3.1, App. A.1); no code released | yes | no |   |   |
| `dexplore_2025` | 2025 | RL, distillation | 7 | r_j^h, r_r^h, r_p^o, r_r^o, r_d, r_c, r_energy |   |   | yes |   |   |
| `dexremoe_2025` | 2025 | RL | 5 | csuccess, cdist, crot, cω, ca | Method, reward (Sec. III-B, Table II); no code released | yes | no |   |   |
| `dexteritygen_2025` | 2025 | RL, diffusion |   |   | Method, reward/objective: the RL reward behind the pretrained controller is not quoted in the source | yes | no |   |   |
| `dexterous_handover_2025` | 2025 | RL | 3 | r_BASE, contact_term (c·w_c), r_MANIP |   |   |   |   |   |
| `dextrack_2025` | 2025 | RL+demo | 5 | r_o,p, r_o,q, r_wrist, r_finger, r_affinity |   |   | yes | parse-limitation | low |
| `dexvla_2025` | 2025 | VLA, diffusion | 2 |   |   |   | yes | parse-limitation | high |
| `dydexhandover_2025` | 2025 | RL | 5 | R_dist, R_obj, R_contact, P_action, P_hand |   |   | no |   |   |
| `geometric_retargeting_2025` | 2025 | teleop-system | 5 | Ldir, Lcover, Lflat, Lpinch, Lcol |   |   | yes |   |   |
| `groot_n16_2025` | 2025 | VLA |   |   |   |   | yes | version-skew | high |
| `groot_n1_2025` | 2025 | VLA, flow |   |   |   |   | yes | version-skew | high |
| `human2sim2robot_2025` | 2025 | RL | 1 | r_obj |   |   | yes |   |   |
| `humanoid_policy_human_policy_2025` | 2025 | BC | 2 |   |   |   | yes |   |   |
| `humanoid_sim2real_recipe_2025` | 2025 | RL, distillation | 2 |   |   |   | no |   |   |
| `maniptrans_2025` | 2025 | RL, BC, diffusion | 5 | r_wrist, r_finger, r_smooth, r_object, r_contact |   |   | yes | parse-limitation | low |
| `metis_2025` | 2025 | VLA | 2 | Lar, Laction |   |   | no |   |   |
| `pi05_2025` | 2025 | VLA, flow |   |   |   |   | yes | code-absent | high |
| `pistar06_2025` | 2025 | VLA, RL, flow |   |   |   |   | yes | code-absent | high |
| `wm_dex_human_videos_2025` | 2025 | world-model, MPC | 2 |   |   |   | no |   |   |
| `being_h05_2026` | 2026 | VLA, flow |   |   |   |   | yes | code-absent | high |
| `dexteleop0_2026` | 2026 | teleop-system, MPC | 3 |   |   |   | no |   |   |
| `force_grasp_sim2real_2026` | 2026 | RL | 7 | R_torque, R_Force, R_diff, R_outer, terminal-state penalty, R_action, R_vel | Method, reward (Sec 3.5.1, Table 2); no weights survive the parse; no code released | yes | no |   |   |
| `poise_2026` | 2026 | RL | 4 | pose reaching, goal completion, grasp maintenance, drop and actuation regularization | Method, reward (Sec. IV-D); weights lost to the parse; no code released | yes | no |   |   |
| `simtoolreal_2026` | 2026 | RL | 5 | r_smooth, r_approach, r_lift, r_goal, b_succ |   |   | no |   |   |
| `teledexter_2026` | 2026 | RL, teleop-system |   |   | Reward block (Sec. 3.1); term formulas lost to the parse; no code released | yes | no |   |   |
| `toporetarget_2026` | 2026 | trajopt, RL | 4 | object, link-position, joint-position, action-smoothness |   |   | no |   |   |
| `viserdex_2026` | 2026 | RL, distillation | 10 | orientation tracking, success bonus, object dropped, object distance, object velocity, joint velocity, action magnitude, action rate, joint work, joint torques | Method, reward (App. Table IX); no code released | yes | no |   |   |

*77 rows. 253 of 770 cells (32 percent) are values no source stated. A blank `terms stated` with a filled `term names` column is a paper that names its terms without numbering them. `in Table 5` marks the rows that are also in the body matrix, which covers in-hand reorientation only.*

### C.2 Paper against released code, in full

Each entry below is the disagreement text stored in the row, unedited. The class is what Sec. 5.8 and Sec. 8.1 count. `contradiction` means the paper states one value and the shipped code demonstrably states another. `parse-limitation` means this survey's own parse could not settle it and the accusation is withdrawn. `code-absent` means the described component is not in the released repository. `version-skew` means the repository is a later generation than the paper. `internal-inconsistency` means the paper disagrees with itself and no code is implicated.

**contradiction, 9 rows.**

- `pddm_2019` (high). Table 2 states obs-dim 46 for In-hand Reorientation while the released cube_env.py code sums to 39; the Baoding reward code includes an extra -10*wrist_too_high term absent from Table 2's printed formula.
- `dexpoint_2022` (high). The released code's reward adds several terms absent from the paper's four-term Eq. 5 (a lift-threshold bonus, a target-distance term, a rotation bonus, and an IK controller-tracking penalty) and reshapes the reach/lift terms into inverse-distance and clipped forms rather than the paper's plain distance/height-difference formulas.
- `dextreme_2022` (high). Action Delta Penalty weight is -0.25 in paper Table 2 but -0.2 in the ADR yaml and -0.01 in the ManualDR yaml; the Joint Velocity Penalty in code normalises velocity by (max_velocity-vel_tolerance) unlike the paper's stated formula; code has a timeout_rew term absent from the paper's reward table; Appendix Table 12 states critic learning rate 5e-4 and KL threshold 0.16, vs body text/code values of 5e-5 and 0.016.
- `visual_dexterity_2022` (high). Table S1 states 32000 teacher training environments, but the released config sets alg.num_envs to 8000 (parent config 16384); fallDistance differs across two shipped configs (0.24 vs 0.15, only the latter matching Table S1's threshold); the paper's Eq 8 penultimate-joint penalty (c7=-2) does not appear anywhere in the released reward code; the config carries a dead distRewardScale=-10.0 key never used in compute_reward; and the paper's table-friction lower bound (0.05) differs by a factor of 10 from the code's randomized lower bound (0.005).
- `dexpbt_2023` (high). Paper presents the reward as 4 mutually exclusive stage terms (r_reach, r_pick, r_targ, -r_vel), but code's compute_kuka_reward sums 8 named components, one of which (hand_delta_penalty) is multiplied by 0 and disabled; there is no single r_vel term in code, instead separate kuka/allegro action penalties whose exact formula is not shown. Also, the paper reports zero experiments with domain randomization, yet the shipped AllegroKuka.yaml already carries a fully specified DR schedule (disabled via randomize: False).
  Review: R3 adversarial review: the disabled-randomisation half is withdrawn, since the note finds it consistent with the paper; the zeroed reward term stands
- `physhoi_2023` (high). The released code hardcodes the body position-velocity error and the object rotation/rotation-velocity errors to zero in compute_humanoid_reward, so despite Table 4 listing nonzero λ^or=0.1/λ^orv=0.01 weights for GRAB, the trained reward never actually tracks object orientation (position-only in practice).
- `unidexgrasp_2023` (high). The paper describes a four-term weighted reward (r_goal + r_reach + r_lift + r_move via Table 7's omega weights) but the released compute_hand_reward implements a different threshold-gated torch.where cascade with distinct hardcoded coefficients that do not map one-to-one onto the paper's weights.
- `penspin_2024` (medium). The appendix states a randomised disturbance force and the released task config sets its scale to zero. A second half of the original charge, that the released code disables the paper's tactile observation channel, is withdrawn: the config read has 96 observation dimensions and `enable_tactile: False`, consistent with the proprioception-only student policy rather than the tactile-and-point-cloud oracle, and the paper never claims the student has tactile input. The code's reward scale-key names (e.g. rotate_reward_scale, pencil_z_dist_penalty_scale) also do not 1:1 name-match the paper's Table 4 weight list, though matched values agree.
  Review: Narrowed before author contact. The tactile-channel half is withdrawn as a plausible reading of which pipeline stage the config belongs to; the disturbance-force half stands. Held at medium confidence pending a direct code read.
- `pianomime_2024` (high). Paper's Table 3 states 2 weighted reward terms (Key Press 2/3, Mimic 1/3), but the released code sums roughly 5 unweighted terms (key press doubled, sustain, energy and fingering hardcoded to return 0, forearm-collision) plus a separately-added mimic wrapper term.

**internal-inconsistency, 4 rows.**

- `aloha_act_2023` (high). Algorithm 1 pseudocode states L_reconst = MSE, but Sec.IV.C's prose explicitly states L1 loss is used instead; the algorithm box and the implementation text disagree; code/md captures only function signatures, not bodies, for policy.py's loss implementation
- `dp3_2024` (medium). the paper's prose states the network predicts the noise added to the data, but the shipped default config trains with prediction_type: sample (predicting the denoised action a^0 directly), not epsilon; the paper only qualifies this later in the same section (Fig. 7 ablates both).
- `omnih2o_2024` (medium). stumble weight -0.00125 (paper) vs -1250 (code); max-feet-height sign/magnitude differ (+1000 paper vs -2500 code, a penalty not a bonus); paper's exp(-c*//.//) form vs code's exp(-err^2/sigma); curriculum level-down threshold 40 (paper) vs 50 (code).
  Review: Withdrawn as a contradiction before author contact. Four of the five weight comparisons match the paper's table to the digit once a systematic x1.25 curriculum factor is accounted for, and only the stumble weight differs, by a factor of about a million, which is a typo signature in the paper's own table rather than evidence of a different trained objective. The hands in this work are also driven open-loop from VR pose, outside the policy and outside the reward, making it a poor fit for a dexterous-manipulation reward census regardless.
- `dexmachina_2025` (low). paper describes a plain weighted sum lambda_task*r_task + lambda_imi*r_imi + lambda_bc*r_bc + lambda_con*r_con with unspecified weights; code implements a multiplicative task term with per-component beta decay, an unmentioned 0.1 force-penalty term, and curriculum-driven decay of auxiliary weights not described as such in the paper
  Review: R3 adversarial review: the multiplicative form credited to the code is printed in the paper itself

**version-skew, 4 rows.**

- `hora_2022` (high). The parsed code commit's joint-noise range, disabled default disturbance force, and default cube object type differ from the paper's stated values; the code README itself says to use tag v0.0.1, not the parsed commit, to reproduce paper numbers.
- `pi0_2024` (high). The released repo (openpi, commit 215abfb2) has evolved past this paper: it also documents pi0-FAST (autoregressive) and pi0.5 checkpoints/configs not described in this paper, which describes only the flow-matching pi0 and the non-VLM pi0-small ablation.
- `groot_n16_2025` (high). code/md is the current Isaac-GR00T main branch (N1.7 generation, commit 51d4c89f), not the N1.6 checkpoint; the repo names a separate n1d6 branch for N1.6 that was not fetched. The page states N1.6's backbone is "an internal NVIDIA Cosmos-2B VLM variant," but the repo's own changelog states the Eagle backbone (nvidia/Eagle-Block2A-2B-v2) was used through N1.6 and only replaced by Cosmos-Reason2-2B in N1.7 -- whether the page's Cosmos-2B variant is a third distinct model or the page is describing N1.7 under an N1.6 headline is not resolvable from what was fetched.
  Review: The page attributes a Cosmos backbone to N1.6 while the repository changelog says N1.6 used Eagle and N1.7 made the switch, so the repository is a later generation than the page describes.
- `groot_n1_2025` (high). The parsed code repo (Isaac-GR00T, commit 51d4c89f) is a later N1.7 generation, not the paper's GR00T-N1-2B: VLM backbone changed from the paper's Eagle-2 to Cosmos-Reason2-2B (via Qwen3-VL); action horizon expanded from the paper's stated H=16 to 40; state/action dimensions expanded from 29 to 132; DiT layers changed from 32 to 16; embodiment scope widened to include Unitree G1, AgiBot G1, and a 'YAM' arm not described in the paper.

**code-absent, 8 rows.**

- `asymdex_2024` (medium). Code contains a GraspAndPlace-task reward variant (AllegroHandDualArmGraspAndPlaceAsymDex.py) with exponential hand-distance and block-alignment terms not one of the four BiDexHands tasks described in the paper body.
- `dexmimicgen_2024` (high). The environment code includes an unused 'reward_shaping' branch (if self.reward_shaping: pass) that is never described or used in the paper text; only the sparse binary completion reward is used, as the paper states.
- `dreureka_2024` (high). The released DrEureka repo (code/md) contains only forward_locomotion/ and globe_walking/ trees; the LEAP-hand cube-rotation training/deployment code and the quoted Prompt-13 reward are the LEAP-hand authors' own code, not included in the released repo, so the cube-rotation reward cannot be cross-checked against a code file.
- `open_television_2024` (low). The paper's prose states 25k training iterations, lr 5e-5, batch size 45, but the code repo's example training command instead shows 50000 epochs and an explicit kl_weight=10 not mentioned anywhere in the paper text.
  Review: R3 adversarial review: a behaviour-cloning paper with no reward; the charge compared paper iterations to a README example's epochs
- `being_h0_2025` (high). The actual downstream action-head module referenced in §4.3 (learnable query tokens, proprioceptive projector f_p, regression head f_r) is not present in the parsed code; the repo's own TODO list marks 'Training code and scripts' as unreleased, so the action-chunk-length=16 value and exact proprioception-vector fields come only from inference/eval CLI examples, not a verifiable implementation.
- `pi05_2025` (high). The paper describes a hybrid discrete-FAST-token-pretrain-then-flow-matching-post-train recipe (Eq. 1, alpha: 0 to 10), but the released repo states plainly it 'currently only support[s] the flow matching head for both pi0.5 training and inference.'
- `pistar06_2025` (high). The general openpi framework (pi0/pi0.5/FAST, flow-matching action head, ALOHA/DROID/LIBERO adapters) is released at commit 215abfb2, but the RECAP-specific pieces described in the paper -- the advantage-conditioning input, the distributional value function, the RECAP training loop (Algorithm 1), and the espresso/laundry/box-assembly checkpoints and datasets -- are not present in the parsed repo.
- `being_h05_2026` (high). Released code (commit e12ac44f) exposes only benchmark/inference/config scaffolding (policy.py, beingh_policy.py, dataset-transform configs). no MoT/MoF model definition, no rectified-flow action-expert source, and no config for any dexterous-hand embodiment; the only post-train configs present (libero_robocasa.yaml, libero_all.yaml, robocasa_human.yaml, so101_example.yaml) are all gripper-only, so the dexterous-hand claims cannot be cross-checked against released code.

**parse-limitation, 13 rows.**

- `artigrasp_2023` (low). paper's two regulariser weights (w_rh=0.5, w_ro=0.2) correspond to five separate velocity penalties in code (-0.5,-0.2,-0.5,-0.5,-0.3); the fingertip weight 12.0 and lambda 5.0 in Table 6 do not appear in the yaml; reward weights differ between curriculum phase-1 and phase-2 configs though Table 6 reports only one set
  Review: R3 adversarial review: the reward body is C++ and absent from the parse; the weight split is the paper's documented curriculum
- `diffusion_policy_2023` (high). the paper's core loss equations (DDPM training loss, EBM/InfoNCE, score-matching) are unrecovered images in the parsed text, and code/md is a signature-only API map, so compute_loss's body could not be verified from code; only the exact shipped noise-scheduler config (DDPMScheduler, 100 train steps) is confirmed.
- `eureka_2023` (low). The released repo's default eureka/cfg/config.yaml ships iteration:1, sample:3 (a fast-test default), not the paper's reported experimental configuration of N=5 iterations × K=16 samples × 5 independent runs, and LLM-generated reward code itself is never checked into the repo (written at runtime to a gitignored outputs/ directory).
  Review: R3 adversarial review: the repo README documents the paper's defaults; the cited config block is a fast-test preset
- `unidexgrasp_pp_2023` (low). The paper's four named reward weights (0.5, 0.1, 2, 10) numerically match literals in the released compute_hand_reward, but the code never labels them with the paper's variable names, and the paper's own display equations were dropped from the PDF, so the correspondence is inferred rather than confirmed by either source.
- `bidexhd_2024` (high). Table 5 weights (w_r, w_t, w1-w4, lambda_w=0.12, lambda_ft=0.48) cannot be matched to code reward lines because the code md truncates the reward function before stage-2/final sum; lambda_w and lambda_ft numerically match the code's grasp-condition thresholds (0.12, 0.12x4 fingers) rather than confirmed reward weights
- `graspxl_2024` (low). The code splits the paper's single r_reg = -w_h//u_h//^2 - w_o//u_o//^2 into four separately-weighted terms (wrist vel, wrist qvel, object vel, object qvel), and the floating-phase object-velocity coefficient (-1.5) does not match the paper's stated w_o=0.1, so the regularization weighting cannot be reconciled 1:1 with Table 9.
  Review: R3 adversarial review: the environment source is not in the parse and the note says the reward cannot be verified
- `humanplus_2024` (medium). code implements a superset of legged_gym reward terms (lin_vel_z, ang_vel_xy, orientation, base_height, torques, dof_vel, dof_acc, action_rate, collision, termination, dof/torque limits, tracking_lin/ang_vel, feet_air_time, stumble, stand_still, feet_contact_forces, target_jt) beyond the 8 terms documented in the paper's Table 1
- `omnigrasp_2024` (medium). The code's compute_pregrasp_reward_time hard-codes w_pos, w_rot = 0.9, 0.1, silently overriding the rwd_specs weight arguments passed into the function; separately, the paper's pre-grasp reward weights (w_hp, w_hr) are not resolvable from either the paper text or Appendix Table 7.
- `resdex_2024` (medium). The base-policy and residual-policy task files implement different variants of compute_hand_reward (whether finger/hand-distance terms are included alongside goal_hand_rew/hand_up/bonus differs), a difference the paper's Sec 4.1/4.4 text does not describe, and the released configs' env count (4096 default) and iteration counts (2500/5000) do not match the paper's stated 11,000 envs and 5,000/20,000 iterations.
- `dexgraspvla_2025` (high). Hardware-interfacing code is explicitly withheld ("Due to intellectual property constraints, we are unable to open-source the hardware-related code"); only function signatures for the controller loss (compute_loss, noise_assignment) are present in code/md, not their bodies, so the MSE/Immiscible-Diffusion loss cannot be verified against code.
- `dextrack_2025` (low). The paper gives one canonical reward-weight table (Table 3), but the released repo's task-config YAMLs contain several divergent, unreconciled reward-coefficient sets across AllegroHandTracking/…TrackingGeneralist/other variants, and it is not identifiable from the parsed source which config produced the paper's headline Table 1 numbers.
- `dexvla_2025` (high). code/md only carries class/function signatures, not bodies, for the diffusion head (modeling_scaledp.py) and no config file with the α weight was captured; the paper's diffusion loss and denoising process cannot be verified against code bodies. only the multi-head ScaleDP signature and a DDIM fp32 patch are available, so none of the paper's tables can be reproduced from what was parsed.
- `maniptrans_2025` (low). paper's PPO learning rate (5e-4) and env count (4096) differ from the shipped README/yaml defaults (2e-4, 8192)
  Review: R3 adversarial review: the cited values are a README override and an unused fallback; the repo's own config matches the paper

