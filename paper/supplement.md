# Learning Dexterous Manipulation: Technical Supplement

Detailed evidence for the paper--code comparisons, predecessor-survey coding, and evaluation-protocol calculations.


---

## Appendix C. Per-paper reward term extraction

Table 5 marks nine recurring term families across the in-hand reorientation methods. This appendix is the extraction underneath it, over every method row that records a reward at all. `terms stated` counts the terms the paper itself names. `where the reward was read` gives the section of the paper or the file in the released code that the note quotes. A row with a `paper/code class` is one where the two disagree, and C.2 prints the disagreement in full. Cells and entries reproduce the text stored in the row, with the source's own punctuation and wording.

### C.1 The extraction

| method | yr | paradigm | terms stated | term names as the paper names them | where the reward was read | in reward matrix | code released | paper/code class | confidence |
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

*77 rows. 253 of 770 cells (32 percent) are values no source stated. A blank `terms stated` with a filled `term names` column is a paper that names its terms without numbering them. `in reward matrix` marks the rows that are also in the reward-term matrix, which covers in-hand reorientation only.*

### C.2 Paper against released code, in full

Each entry below is the disagreement text stored in the row, unedited. The class is what Sec. 5.8 and Sec. 8.1 count. `contradiction` means the paper states one value and the shipped code demonstrably states another. `parse-limitation` means this survey's own parse could not settle it and the accusation is withdrawn. `code-absent` means the described component is not in the released repository. `version-skew` means the repository is a later generation than the paper. `internal-inconsistency` means the paper disagrees with itself and no code is implicated. Every `contradiction` entry carries an `Artefact` line: the repository, the commit `corpus/code_manifest.json` records, the file inside it and where in that file the value sits, so the entry can be checked without asking anyone. None of those authors was written to before this survey was posted; section 5.6 says so beside the finding, the letters that were drafted and not sent are in `outreach/` in the corpus, which is available from the author at the address in the byline, and the route by which a disputed entry is corrected is stated there too.

**contradiction, 9 rows.**

- `pddm_2019` (high). Table 2 states obs-dim 46 for In-hand Reorientation while the released cube_env.py code sums to 39; the Baoding reward code includes an extra -10*wrist_too_high term absent from Table 2's printed formula.
  Artefact: `google-research/pddm` at `06b88cdbaf`, `pddm/envs/cube/cube_env.py` (`_get_obs`).
- `dexpoint_2022` (high). The released code's reward adds several terms absent from the paper's four-term Eq. 5 (a lift-threshold bonus, a target-distance term, a rotation bonus, and an IK controller-tracking penalty) and reshapes the reach/lift terms into inverse-distance and clipped forms rather than the paper's plain distance/height-difference formulas.
  Artefact: `yzqin/dexpoint-release` at `17f1e238bb`, `dexpoint/env/rl_env/relocate_env.py` (`AllegroRelocateRLEnv.get_reward`).
- `dextreme_2022` (high). Action Delta Penalty weight is -0.25 in paper Table 2 but -0.2 in the ADR yaml and -0.01 in the ManualDR yaml; the Joint Velocity Penalty in code normalises velocity by (max_velocity-vel_tolerance) unlike the paper's stated formula; code has a timeout_rew term absent from the paper's reward table; Appendix Table 12 states critic learning rate 5e-4 and KL threshold 0.16, vs body text/code values of 5e-5 and 0.016.
  Artefact: `isaac-sim/IsaacGymEnvs` at `aeed298638`, `isaacgymenvs/cfg/task/AllegroHandDextremeADR.yaml` (`actionDeltaPenaltyScale`).
- `visual_dexterity_2022` (high). Table S1 states 32000 teacher training environments, but the released config sets alg.num_envs to 8000 (parent config 16384); fallDistance differs across two shipped configs (0.24 vs 0.15, only the latter matching Table S1's threshold); the paper's Eq 8 penultimate-joint penalty (c7=-2) does not appear anywhere in the released reward code; the config carries a dead distRewardScale=-10.0 key never used in compute_reward; and the paper's table-friction lower bound (0.05) differs by a factor of 10 from the code's randomized lower bound (0.005).
  Artefact: `Improbable-AI/dexenv` at `ad9634e9d2`, `dexenv/conf/dclaw.yaml` (`alg.num_envs`).
- `dexpbt_2023` (high). Paper presents the reward as 4 mutually exclusive stage terms (r_reach, r_pick, r_targ, -r_vel), but code's compute_kuka_reward sums 8 named components, one of which (hand_delta_penalty) is multiplied by 0 and disabled; there is no single r_vel term in code, instead separate kuka/allegro action penalties whose exact formula is not shown. Also, the paper reports zero experiments with domain randomization, yet the shipped AllegroKuka.yaml already carries a fully specified DR schedule (disabled via randomize: False).
  Artefact: `NVIDIA-Omniverse/IsaacGymEnvs` at `aeed298638`, `isaacgymenvs/tasks/allegro_kuka/allegro_kuka_base.py` (`compute_kuka_reward`).
  Review: R3 adversarial review: the disabled-randomisation half is withdrawn, since the note finds it consistent with the paper; the zeroed reward term stands
- `physhoi_2023` (high). The released compute_humanoid_reward sets the body position-velocity error and the object rotation and rotation-velocity errors to zeros_like, unconditionally, with the computation that would produce them commented out on the same lines, while Table 4 lists nonzero λ^or=0.1/λ^orv=0.01 weights for GRAB: in that file the object's orientation error is the constant zero and those weights cannot change the reward.
  Artefact: `wyhuai/PhysHOI` at `6095c605e2`, `physhoi/env/tasks/physhoi.py` (`compute_humanoid_reward`).
- `unidexgrasp_2023` (high). The paper describes a four-term weighted reward (r_goal + r_reach + r_lift + r_move via Table 7's omega weights) but the released compute_hand_reward implements a different threshold-gated torch.where cascade with distinct hardcoded coefficients that do not map one-to-one onto the paper's weights.
  Artefact: `PKU-EPIC/UniDexGrasp` at `36c9bfcf7c`, `dexgrasp_policy/dexgrasp/tasks/shadow_hand_grasp.py` (`compute_hand_reward, goal_cond branch`).
- `penspin_2024` (medium). The appendix states a randomised disturbance force, and the released configs/task/AllegroHandHora.yaml ships forceScale: 0.0, so no shipped configuration applies it.
  Artefact: `HaozhiQi/penspin` at `5035c52dc9`, `configs/task/AllegroHandHora.yaml` (`forceScale`).
  Review: Narrowed at the point of drafting the letter to its authors, which was never sent. The original comparison also said the released code disables the paper's tactile channel, and that half is withdrawn: the config read has numObservations 96 and enable_tactile False, which is consistent with the proprioception-only student rather than the oracle, and the paper never claims the student has tactile input. The disturbance-force half is unaffected.
- `pianomime_2024` (high). Paper's Table 3 states 2 weighted reward terms (Key Press 2/3, Mimic 1/3), but the released code sums roughly 5 unweighted terms (key press doubled, sustain, energy and fingering hardcoded to return 0, forearm-collision) plus a separately-added mimic wrapper term.
  Artefact: `sNiper-Qian/pianomime` at `c4abefac8d`, `single_task/piano_with_shadow_hands_res.py` (`_set_rewards`).

**internal-inconsistency, 4 rows.**

- `aloha_act_2023` (high). Algorithm 1 pseudocode states L_reconst = MSE, but Sec.IV.C's prose explicitly states L1 loss is used instead; the algorithm box and the implementation text disagree; code/md captures only function signatures, not bodies, for policy.py's loss implementation
- `dp3_2024` (medium). the paper's prose states the network predicts the noise added to the data, but the shipped default config trains with prediction_type: sample (predicting the denoised action a^0 directly), not epsilon; the paper only qualifies this later in the same section (Fig. 7 ablates both).
- `omnih2o_2024` (medium). stumble weight -0.00125 (paper) vs -1250 (code); max-feet-height sign/magnitude differ (+1000 paper vs -2500 code, a penalty not a bonus); paper's exp(-c*//.//) form vs code's exp(-err^2/sigma); curriculum level-down threshold 40 (paper) vs 50 (code)
  Review: Withdrawn as a contradiction at the point of drafting the letter to its authors, which was never sent. Four sibling weights match the paper to the digit under a systematic x1.25 curriculum factor and only the stumble weight differs, by a factor of about a million, which is a typo signature in the paper's own table rather than evidence of a different trained objective. The hands in this work are driven open-loop from VR pose, outside the policy and outside the reward, so it is a weak fit for a dexterous-manipulation reward census in the first place.
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
  Review: R3 adversarial review: a behaviour-cloning paper with no reward; it compared paper iterations to a README example's epochs
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


---

## Appendix D. The existing surveys, and what each covers

Fourteen corpus entries are themselves surveys or engine-comparison studies. Table 10 sets them on
one set of columns. The columns record what each work covers, not how well. Section 1 states what
this survey adds over them and does not repeat the comparison here.

`an_dexil_survey_2025` is the closest in subject, covering imitation learning for multi-fingered
hands by learning family, end-effector class and demonstration source. It gives reinforcement
learning no taxonomy, treats bimanual work as a single "multi-agent" subsection, compares no
simulator, and defines no evaluation metric. `welte_iil_survey_2025` finds only seven dexterous
works that use interactive imitation learning and carries a fifteen-hand commercial table, with no
bimanual section, no benchmark table and no contact modelling. `zhao_sim2real_survey_2020`
supplies the standard sim-to-real split and predates GPU-parallel simulation.
`firoozi_foundation_models_2023` has zero occurrences of bimanual, tactile or in-hand.

`bai_unified_manip_survey_2025` spans all of manipulation across 212 pages. Its Sec. 4.3 on
dexterous manipulation runs about 720 words, the third longest of its ten task subsections behind
grasping and quadrupedal manipulation, which is a real treatment and not a passing mention. The
difference is elsewhere. Its Sec. 1.2 lists dexterous manipulation among the topics that "existing
surveys" cover from "narrower perspectives" and defers it to two of them.

`zhao_dexhand_survey_2026` is the most recent hand-centred survey, with a 29-hand anatomy table
and a task-by-paradigm taxonomy. Its Sec. IV-C names the reference-versus-rollout split that
Section 1 credits it with, and its Sec. III-F is the one bimanual subsection, 16 cited works with
no coordination analysis.

`nine_physics_engines_review_2024` is the predecessor closest to the engine comparison, and it
reviews Brax, Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Unity and Webots for reinforcement
learning research. It scores each on documentation, model and environment creation, URDF and MJCF
support, and readiness for multi-agent work. It runs no benchmark of its own and says so in its
Sec. V, that implementing the same scenarios across nine engines "goes beyond the scope of this
paper". Its running bodies are ant-and-humanoid RL benchmarks rather than hands, and it discusses
no timestep, no friction model, no contact formulation and no penetration.

### Table 10. Existing surveys and what each covers

| survey | yr | scope | taxonomy used | bimanual covered | hardware covered | evaluation covered | gaps it names |
|---|---|---|---|---|---|---|---|
| `isaac_sim_2026` | 2026 | one simulator's ecosystem and application domains, reviewed rather than measured | qualitative capability matrix, Table 1, over simulators | one cited GR00T task called bimanual, no hand, DoF or number | no hand named anywhere in paper or code parse | none. The paper runs no experiment of its own | computational cost, configuration complexity, learning curve |
| `zhao_dexhand_survey_2026` | 2026 | dexterous hands end to end: hardware anatomy, methods, datasets, directions | five task categories, each split by learning paradigm. Hardware is split by actuation, transmission and perception | one subsection, III-F, 16 cited works, no coordination analysis | Table I, 29 hands, 12 columns, secondary values | names two layers: physical plausibility including penetration before execution, success during it. No threshold, method or count | hardware feasibility, perception fusion, learning beyond benchmark-centric optimisation, industrialisation, absent evaluation standards |
| `an_dexil_survey_2025` | 2025 | imitation learning for multi-fingered end-effectors | IL family by end-effector class by demonstration source. RL gets none | one subsection, II.E, framed as multi-agent | hands named in prose, no hand table | no metric defined and no trial count. Calls for protocols, proposes none | contact dynamics in engines, data-collection standards, cross-hand transfer, failure datasets, end-effector morphology |
| `bai_unified_manip_survey_2025` | 2025 | all of robot manipulation. Dexterous manipulation is one of ten task subsections, about 720 words, and Sec. 1.2 defers it to other surveys | high-level planning, action modelling, actuation control, plus a bottleneck taxonomy of data and generalisation | bimanual means two arms. One dual-hand mention in the paper | hands named, no DoF or actuation table | success rate and checkpoint selection, six lines. Never says how success is judged for a dexterous task | no scaling law, sim-to-real for contact-rich tasks, fragmented datasets, reliability as important as success |
| `welte_iil_survey_2025` | 2025 | interactive imitation learning, seven dexterous works found | IIL feedback type, plus a keyword bibliometric of 326 papers | three mentions in 687 lines, no section | Table 1, 15 commercial hands, manufacturer figures | no metric defined, no benchmark table | tactile feedback, long-horizon tasks, generalisation, human-feedback interface |
| `nine_physics_engines_review_2024` | 2024 | nine physics engines for RL research, scored on documentation and usability | 13-axis feature and usability matrix, Table II, plus citation-count popularity | none. MARL readiness is the multi-agent axis | none. Ant and humanoid RL bodies are the running examples | no benchmark of its own. Throughput claims are second-hand | no cross-engine MARL performance comparison exists in the literature |
| `contact_models_comparison_2023` | 2023 | LCP, CCP, RaiSim and NCP contact models re-implemented in one framework and ranked | contact model by solver, with the physical property each one violates | none | one Allegro hand as a benchmark system, a ball dropped into it | NCP criterion, self-consistency against a 1e-5 s reference, iteration cost | no fully satisfactory contact model, and gradients through simulation artifacts are unexplored |
| `firoozi_foundation_models_2023` | 2023 | foundation models in robot decision-making, perception and embodied AI | background, robotics, and robotics-adjacent papers, then by application | none, zero occurrences | none. Parallel-jaw end effectors throughout | none defined. Benchmarking appears as a reproducibility problem | data scarcity, variability, uncertainty, safety, real-time inference, and simulators that neglect contact physics |
| `zhao_sim2real_survey_2020` | 2020 | sim-to-real transfer in deep RL, eight pages, 21 works tabulated | zero-shot, system identification, domain randomisation, domain adaptation, learning with disturbances, simulator choice | none, zero occurrences | two cited hand works, no hand table | no metric defined, no trial count, no success rate | domain randomisation has no formal account, and domain adaptation assumes matched feature spaces |
| `piazza_century_2019` | 2019 | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* |
| `physics_engine_comparison_2015` | 2015 | five engines on one shared model: speed, self-consistency, conservation, grasp stability | none. Four test systems, one comparison per test | none | one 35-DoF rig modelled on the Shadow Hand | largest timestep that holds a grasp, and a speed-accuracy Pareto curve | restricted feature subset by design, and the authors are MuJoCo's developers |
| `roa_suarez_grasp_quality_2015` | 2015 | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* |
| `ma_dollar_dexterity_2011` | 2011 | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* |
| `okamura_overview_2000` | 2000 | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* |

*14 rows, one per corpus entry of class `survey`, 3 of which could not be obtained and are entered as such, and 1 of which was fetched too late to be read into a note. Every filled cell is read from `papers/notes/<key>.md` and is checked against a quotation from that note by `tools/make_survey_table.py`. A cell whose evidence has gone from the note prints empty rather than printing an unchecked claim. The columns record what each work covers, not how well, and a blank cell in `bimanual covered` or `hardware covered` is a scope decision by its authors rather than a failure.*


Table 10's last rows carry the cost of the corpus. `okamura_overview_2000`, `piazza_century_2019`
and `roa_suarez_grasp_quality_2015` are behind publisher paywalls with no author-hosted copy found
on 2026-09-18, and `bicchi_hands_2000` is in the same position with no row at all.
`ma_dollar_dexterity_2011` is a different case. The fetch that failed when its note was written
succeeded afterwards, so a seven-page PDF is on disk with a recorded hash, and no note has been
read from it. All five are cited by metadata only and nothing in this survey describes their
contents. The open chapter `bicchi_grasping_chapter_2001` overlaps the paywalled Bicchi paper
without being identical to it, so it is quoted in its own right.


---

## Appendix E. Where the protocol's counts come from

Every count in Table 8 is derived below, and each axis is derived for the statistic that axis
actually reports rather than by one convention applied to all of them: a single rate takes a Wilson
half-width, a matched comparison takes McNemar, a ratio takes the standard error of the log ratio,
and a correlation takes the Fisher-z interval. Section 7.3 states what these derivations conclude.
This survey re-ran no method, so every count here rests on an interval width, a power calculation
or another paper's measurement, and never on a measurement of our own. The counts an earlier draft
quoted and this one withdrew are kept, so that a reader can see which test was the wrong one and
why.

Fix the width first, then read off the count. Take a 95 percent Wilson interval on a single
reported rate, at the worst case of p = 0.5. A half-width of 20 points needs 21 trials, 15 points
needs 39, 10 points needs 93 and 5 points needs 381. Ten points is the coarsest width at which a
single rate is worth printing, so the absolute-rate minimum is 93, rounded to 100. At 100 trials a
reported 80 percent has an interval of 71 to 87 percent, and a reported 50 percent has 40 to 60. A
comparison is a different question and a harder one: two rates each carrying ±10 points do not
resolve a 10-point difference between them, because the difference's standard error is larger by a
factor of √2, so the width argument sets a floor on what is worth reporting and not on what can be
compared.

For the A/B comparison the relevant calculation is power, and the design is paired. Table 8
matches initial conditions by image overlay and interleaves the two policies in one session, so
the unit is a matched pair and the count follows McNemar, which depends on the discordance rate.
The share of initial conditions on which the two policies disagree, and not on the two rates
alone. To separate 50 from 70 percent at α = 0.05 with 80 percent power: 37 pairs per arm at a
discordance of 0.2, 57 at 0.3, 77 at 0.4 and 96 at 0.5. The protocol assumes 0.3 and asks for 57,
and states the sensitivity rather than hiding it, because 0.5 is the discordance the same two
rates produce when the pairing buys nothing, and at that value the paired count returns to the 93
per arm an unpaired test would need. The saving from pairing is real but smaller than the pair
counts suggest, since a pair costs two rollouts: 57 pairs is 114 rollouts against 186. An earlier
version of this section quoted 93, 169 and 387 per arm for gaps of 20, 15 and 10 points, which are
correct for independent arms and are the wrong test for this protocol. That 93 was also the same
integer as the half-width calculation in the paragraph above, which is a coincidence of the
worst-case arithmetic and not a second derivation of the same number.

One hundred is a cap and not a bill, because on a graded score a sequential test reached its
decision in 12 to 36 paired hardware trials in `beyond_binary_success_2026`. At 30 rollouts a
continuous score already carries a half-width of ±0.36 standard deviations, which is why a graded
score can stop where a binary one cannot. A cell that stops early does not report a Wilson
interval. Optional stopping breaks the coverage of a fixed-n interval, which is the reason
`beyond_binary_success_2026` and `suresim_2025` use anytime-valid betting intervals rather than
Wilson, so Table 8 asks a cell run to a fixed 100 for a Wilson interval and a cell stopped early
for a confidence sequence, and never for both. Intervals are also marginal rather than
simultaneous. For example, evaluating twelve methods on seven axes produces 84 intervals. At 84 independent 95 percent
intervals, four excursions are expected by construction, so a paper comparing k policies on m
tasks corrects its k(k−1)/2 pairwise tests to a global 95 percent level, as
`lbm_careful_examination_2025` does, or says its intervals are not simultaneous.

Simulation is cheap, so simulated cells take 200 episodes, giving a 6.9-point half-width.
Perturbation axes are screened rather than certified, and 40 per axis buys a 15-point half-width
on each axis's own absolute rate, which is enough to rank the axes and pick the two worst for
hardware. It is not enough for the ratio to the anchor that an earlier draft asked each cell to
report. At 40 trials in each arm, a fall from a 0.50 anchor to 0.30 is a ratio of 0.60 with a 95
percent interval of 0.34 to 1.06, which contains 1: at the screening count you cannot establish
that the perturbation hurt at all. Certifying that same drop takes 101 per arm at 80 percent
power, or about 50 for an interval that merely excludes 1, so Table 8 now asks for absolute rates
with their own intervals at 40, reports the ratio without an interval, and prescribes 101 before any
claim that a named axis hurt.

For unseen objects the resampling unit is the object and not the trial, so 20 objects at 5 trials
each gives 100 trials and an object-level half-width near 20 points. That 20 points is the Wilson
width at n = 20 and it treats each object's outcome as a single Bernoulli draw, which the five
within-object trials are not. It is the right order of magnitude and the assumption belongs in the
cell. A 10-point claim about an object distribution needs about 93 objects. Seven of the 39 rows
that state an unseen count reach that: 225 in `bimangrasp_2024`, 241 in `resdex_2024` and
`unidexgrasp_2023`, 360 in `dexgraspvla_2025`, 500 in `dexmv_2021`, 2029 in `clutterdexgrasp_2025`
and 503409 in `graspxl_2024`. For a continuous score the half-width is 1.96 standard deviations
over the square root of the count, so 100 rollouts give ±0.20 standard deviations, and the unit is
the rollout because frames within one are correlated.

The transfer axis is the one where 100 is least defensible. On 100 matched pairs a measured
correlation of 0.70 carries a Fisher-z interval of 0.58 to 0.79, a half-width of about 0.10 that
130 pairs would be needed to guarantee. That is enough to establish that a simulator tracks
reality at all, and it is not enough to separate `suresim_2025`'s useful regime from its marginal
one, since those differ by about 0.11 in correlation. Both limits come within 0.05 of the estimate
only at about 457 pairs. Table 8 states which of the two decisions each count supports rather than
leaving a reader to assume the larger one.
