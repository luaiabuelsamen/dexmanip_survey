# Candidate claims for the survey's gap section

Each row is a claim a note-writing agent surfaced. A claim enters the survey only after a
reviewer has checked it against the named note, and the note against papers/md or code/md.
Status: `unverified` until then.

## A. Reported rewards do not match released code
| claim | note | status |
|---|---|---|
| DeXtreme's action-delta penalty weight differs between paper (-0.25) and two shipped configs (-0.2, -0.01); code adds a `timeout_rew` term absent from the paper | dextreme_2022 | unverified |
| DexPBT's paper describes 4 staged reward terms, the code sums 8, and one is multiplied by zero in the shipped config | dexpbt_2023 | unverified |
| DexPBT's paper says no domain randomisation, the config ships a DR schedule gated off | dexpbt_2023 | unverified |
| Visual Dexterity: teacher env count 32k in paper vs 8k/16k in code; a penalty term is missing from code; a friction range differs by 10x | visual_dexterity_2022 | unverified |
| Hora: the repo README itself warns the released commit's numbers differ from the paper's | hora_2022 | unverified |
| PhysHOI's object-rotation reward is hardcoded to zero in released code despite a nonzero weight in the paper's table, making the method position-only in practice | physhoi_2023 | unverified |
| PenSpin: disturbance force described in the appendix is zeroed in the released config | penspin_2024 | unverified |
| GraspXL, DexPoint, PDDM: paper/code reward mismatches flagged | graspxl_2024, dexpoint_2022, pddm_2019 | unverified |
| DexTrack ships several divergent reward-coefficient sets across task configs with no way to tell which produced the headline numbers | dextrack_2025 | unverified |
| RoboPianist's paper lists 3 reward terms, the code's `_set_rewards` has 5 (adds sustain and forearm-collision) | robopianist_2023 | unverified |
| PianoMime's code has energy and fingering reward terms hardcoded to return zero | pianomime_2024 | unverified |
| MuJoCo Playground ships a LEAP Hand in paper and code plus an undocumented Aero Hand in code only | mujoco_playground_2025 | unverified |

## B. Interpenetration is measured on inputs, not on outputs
| claim | note | status |
|---|---|---|
| DexTrack scores interpenetration only on input reference trajectories, never on its own policy's rollouts, and presents tolerance of "severe hand-object penetrations" as robustness | dextrack_2025 | unverified |
| TopoRetarget is the only corpus method that quantifies penetration (max depth, % frames > 2 mm) and constrains it by SDF, but does not re-verify after RL tracking | toporetarget_2026 | unverified |
| Pang et al. impose non-penetration as a hard constraint; MJPC never addresses it | pang_global_planning_2022, mjpc_2022 | unverified |

## C. Reward weights are unpublishable as stated
| claim | note | status |
|---|---|---|
| Robot Synesthesia gives reward weights only symbolically, never numerically, and ships no code | robot_synesthesia_2023 | unverified |
| Several 2025-2026 papers' reward equations exist only as images, so the weights cannot be read at all | poise_2026, simtoolreal_2026, rotating_without_seeing_2023, clutterdexgrasp_2025, force_grasp_sim2real_2026 | unverified |

## D. Evaluation protocol is unspecified even by the papers that prescribe one
| claim | note | status |
|---|---|---|
| Kress-Gazit et al. prescribe no minimum trial count and no confidence-interval width; their own example uses 10 initial conditions x 2 runs | kress_gazit_policy_eval_2024 | unverified |
| RoboArena reports no confidence intervals and no per-policy trial counts | roboarena_2025 | unverified |
| COLOSSEUM's abstract R-squared is never derived in the body; its Table IV mean does not match the text | colosseum_2024 | unverified |
| AutoEval states its throughput two ways in the same paper (500 vs ~850 episodes/day) | autoeval_2025 | unverified |
| RLBench's code lists 106-107 tasks against the paper's 100 | rlbench_2019 | unverified |

## E. Simulator claims are not comparable
| claim | note | status |
|---|---|---|
| Isaac Lab exposes a `--physics newton_mjwarp` switch, so "Isaac Lab means PhysX" is already wrong | isaaclab_2025 | unverified |
| Isaac Lab's paper gives no timestep, decimation or solver iteration counts; its only dexterous throughput figure is prose | isaaclab_2025 | unverified |
| Brax's paper has a four-fingered Grasp environment that is absent from the current repo | brax_2021 | unverified |
| MuJoCo Playground's code ships an undocumented Aero Hand not mentioned in the paper | mujoco_playground_2025 | unverified |
| Erez et al. 2015: MuJoCo holds a grasp at 16 ms timestep where PhysX needs 2 ms, ODE 0.25 ms, Bullet 0.03 ms | physics_engine_comparison_2015 | unverified |
| Throughput figures are quoted at different env counts on different GPUs, so FPS across engines is not a comparison | maniskill3_2024, isaaclab_2025, isaacgym_2021 | unverified |

## F. Hardware claims cannot be checked
| claim | note | status |
|---|---|---|
| Announced hands' pages 404 or carry no hand content, so DoF and force figures circulate without a source (AgiBot, Daxo, Figure, LinkerBot L20, Boston Dynamics) | agibot_omnihand_2025, daxo_muscle_v0_2025, figure_03_hand_2025, linkerbot_l20_2025, boston_dynamics_atlas_hand_2026 | unverified |
| Vendor specs contradict the survey tables that cite them (Tesollo weight and bus, XHAND1 fingertip force, Figure 03 DoF, Xiaomi success rate) | tesollo_dg5f_2024, robotera_xhand1_2024, figure_03_hand_2025, xiaomi_cyberone_hand_2026 | unverified |
| Of the announced hands, only Sharpa appears in any corpus code; most appear nowhere outside their own vendor page | sharpa_wave_2026 and hands batch 3 | unverified |

## G. Counterintuitive results worth a paragraph
| claim | note | status |
|---|---|---|
| ObjDex finds that retargeting fingers rather than the wrist alone hurts generalisation | objdex_2024 | unverified |

## H. Headline numbers are quoted out of their conditions
| claim | note | status |
|---|---|---|
| The 94% often attributed to Dexterous Handover 2025 is simulation only, N=100, on a single out-of-distribution object, and the paper has no real-robot experiment at all | dexterous_handover_2025 | unverified |
| PianoMime's abstract says up to 56% F1 and its conclusion says 70% | pianomime_2024 | unverified |
| Dynamic Handover's real-robot result is 3 seeds x 5 trials, i.e. 15 attempts, against a sim number from 500 | dynamic_handover_2023 | unverified |
| DexTrack's tracking reward table omits a numeric weight for a term it names | dextrack_2025 | unverified |

## I. Two hands are often one shared reward
| claim | note | status |
|---|---|---|
| All three handover papers use a single shared reward across giver and receiver; none has separate giver and receiver objectives | dynamic_handover_2023, dydexhandover_2025, dexterous_handover_2025 | unverified |
| In Dexterous Handover 2025 only the receiver is learned; the giver is a scripted arm, so it is not a two-agent method at all | dexterous_handover_2025 | unverified |

## J. Sources that cannot be obtained
| claim | note | status |
|---|---|---|
| Four foundational overviews are paywalled with no author-hosted copy (Okamura 2000, Bicchi T-RO 2000, Piazza 2019, DLR Hand II 2001), as is RaiSim's RA-L paper; the survey cites them by metadata and rests no claim on their contents | corpus/bib.json marks each SOURCE UNAVAILABLE | verified 2026-09-18 |
| The open PDF that circulates for Bicchi 2000 is a different work, the RAMSETE book chapter; the survey lists it separately | bicchi_grasping_chapter_2001 | verified 2026-09-18 |

## K. The generalist-policy literature is mostly not about hands
| claim | note | status |
|---|---|---|
| pi0, pi0.5, pi*0.6 and OpenVLA are all evaluated exclusively on parallel-jaw grippers; none reports a dexterous-hand success rate | pi0_2024, pi05_2025, pistar06_2025, openvla_2024 | unverified |
| Gemini Robotics 2025 shows five-fingered Apollo hands only qualitatively, with no success rate or trial count; the quantitative results are all gripper platforms | gemini_robotics_2025 | unverified |
| DexVLA's name notwithstanding, three of four embodiments are parallel-jaw and its 91-task pretraining mixture is entirely gripper-based | dexvla_2025 | unverified |
| The generalist policies that do evaluate on hands use low-DoF commercial hands (Inspire 6-DoF, PsiBot 6-DoF, Fourier), not the 16-24 DoF hands the RL literature uses | groot_n1_2025, being_h0_2025, dexgraspvla_2025, metis_2025 | unverified |
| Released code generations diverge from the paper for GR00T N1 (repo is N1.7) and pi0.5 (flow-matching head) | groot_n1_2025, pi05_2025 | unverified |
| Several VLA papers contain internally inconsistent tables (GR00T N1 Table 2 vs Table 4, Being-H0.5 ablation vs text, Dexora dataset hours) | groot_n1_2025, being_h05_2026, dexora_2026 | unverified |

## L. Benchmark and dataset sources contradict themselves
| claim | note | status |
|---|---|---|
| HOI4D states 4 subjects in one place and 9 in another, and 54 tasks against 76 | hoi4d_2022 | unverified |
| ACT's Algorithm 1 and its prose disagree on whether the reconstruction loss is MSE or L1 | aloha_act_2023 | unverified |
| DexVerse 2026 does not state hand degrees of freedom, vendor, or physics timestep anywhere in the paper | dexverse_2026 | unverified |

## M. Findings raised during drafting, to be checked in revision
| claim | note | status |
|---|---|---|
| No published penetration measurement in the corpus is of a hand grasping an object. Dojo's is a foot-floor humanoid drop, ComFree-Sim's is loose primitives falling, Castro's is an analytic point mass on a plane, TopoRetarget's is a retargeted reference rather than a rollout. The measurement the survey's thread asks for has never been made. | dojo_2022, comfree_sim_2026, castro_sap_contact_2021, toporetarget_2026 | raised by section 4 writer, unverified |
| Only four closed-loop policies in the corpus handle interpenetration at all, not eleven; the other seven are grasp synthesisers, trajectory optimisers or a contact model | clutterdexgrasp_2025, dexmachina_2025, dextrack_2025, teledexter_2026 | raised by section 7 writer, used in draft |
| GRAB reports 3.25 mm penetration and OakInk reports 2.53 cm on the GRAB split, a factor of eight apart, and neither states its distance function precisely enough to reconcile them | grab_2020, oakink_2022 | raised by section 7 writer, used in draft |
| Of 37 recorded paper/code disagreements only 16 are contradictions; 9 are limitations of this survey's own parsing | corpus/rows mismatch_class | verified, draft corrected |
| Figure 2's original annotation wrongly claimed no announced or prototype hand appears in any method row; Faive and LEAP v2 Advanced account for three rows. The defensible claim is about the nine company-announced hands. | fig2, section 3.6 | verified, figure and text corrected |
| Default physics timestep is stated by 3 of 15 engines and solver iteration counts by 4 of 15 | corpus/rows class simulator | raised by section 4 writer, used in draft |
