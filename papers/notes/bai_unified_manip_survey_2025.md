# bai_unified_manip_survey_2025 — Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey (Bai, Song, Chen, Ji, Zhong, Yang, Zhao, Zhou, Zhao, Li, Ding, Chi, Li, Xu, Zheng, Wang, Zhang, Chen; arXiv 2510.10903, 2025; 212 pages per manifest)

sources: papers/md/bai_unified_manip_survey_2025.md [fe914530] ; code/md/bai_unified_manip_survey_2025.md [b208a663] (Awesome-Robotics-Manipulation README; "Config files (0)", "Python signatures and reward/observation bodies (0 files)")

## One-line contribution
Whole-of-manipulation survey that splits the pipeline into high-level planning (language / code / motion / affordance / 3D / video), low-level learning-based action modelling (learning strategy / input modelling / latent learning / policy learning) and actuation-level control, adds a bottleneck taxonomy (data collection, data utilisation, generalisation), organises benchmarks by task category, and treats dexterous manipulation as one of ten task types (Sec. 4.3, about 30 lines of 5919).

## Setting
- hand(s): Sec. 2.1 "Dexterous Hands" names Robotiq 3-Finger Adaptive Gripper, Allegro Hand, Shadow Dexterous Hand, Unitree Dex3-1, D'Claw and D'Kitty (ROBEL), Inspire Hand, Linker Hand L20, Wuji Hand, "together with other learning-oriented designs [32, 33]". Soft hands: RBO Hand 3, Festo BionicSoftHand, SpiRobs, qb SoftHand. No DoF / DoA figures; Figure 2 is a picture of platforms.
- single/bimanual: both appear as hardware classes (Sec. 2.1 "Bimanual Arms": dual Franka Panda, ALOHA, ABB YuMi) and as a benchmark tag ("Bi = bimanual arms"). "bimanual" occurs 52 times; "dual-hand" once (Dexora, Sec. 4.3).
- simulator / physics: benchmark tables (Sec. 3.2–3.3) list an engine per benchmark: MuJoCo (MetaWorld, Franka Kitchen, Robomimic, LIBERO, VLABench, BiGym, HumanoidBench, RoboSuite, RoboCasa), Isaac Sim (ARNOLD, GENMANIP, RoboDojo, ODYSSEY, ORBIT/Isaac Lab, AgentWorld, SIMPLE), Isaac Gym (TacSL, ManiFeel). The only single-embodiment row tagged "Dex" is "[11] | RSS 2018 | MuJoCo | - | 4 | 100 | RGB, D, T | ADROIT Hand | Dex, Uni" (DAPG). Cross-embodiment rows tagged Dex: RoboSuite, ORBIT/Isaac Lab, RoboCasa, AgentWorld; humanoid rows: HumanoidBench "Unitree H1 + Shadow-Hand", SIMPLE. No engine comparison, no contact-model discussion.
- observation / action: Sec. 6.2 "Input Modeling" (vision-action; VLA with 2D or 3D input; tactile-based; extra modalities). Sec. 2.2.2 gives the MDP five-tuple (equation image dropped by the converter).
- objects / data: Sec. 3.1 grasp datasets, dexterous rows: "Dexgraspnet [89] | ICRA 2023 | dexterous | single-object | 5355 | sim | 1.32M grasps"; "Dex1B [94] | RSS 2025 | dexterous | single object | 6K | sim | 1B grasps | PC".

## Method (taxonomy = section structure; Contents at lines 24–140)
- 2 Background: 2.1 hardware; 2.2 low-level action modelling (2.2.1 non-learning; 2.2.2 learning-based); 2.3 robotics models; 2.4 evaluation.
- 3 Simulators, Benchmarks, Datasets: 3.1 grasping datasets; 3.2 single-embodiment; 3.3 cross-embodiment; 3.4 trajectory datasets; 3.5 embodied QA / affordance; 3.6 human video and video-world-model benchmarks.
- 4 Tasks: 4.1 grasping; 4.2 basic; 4.3 dexterous; 4.4 soft; 4.5 deformable; 4.6 mobile; 4.7 quadrupedal; 4.8 humanoid; 4.9 aerial; 4.10 underwater.
- 5 High-level planning: 5.1 LLM; 5.2 MLLM; 5.3 programmatic; 5.4 geometric-constraint; 5.5 affordance; 5.6 3D-representation; 5.7 video-based.
- 6 Low-level learning-based action modelling: 6.1 learning strategy (6.1.1 RL model-free / model-based; 6.1.2 IL from action / from observation; 6.1.3 bridging RL and IL; 6.1.4 auxiliary tasks: world model, image/video prediction, vision- and text-grounded goal extraction, contrastive, reconstruction); 6.2 input modelling (VA; VLA 2D/3D; tactile; extra); 6.3 latent learning (pretrained latent; latent action: VQ, continuous, hierarchical); 6.4 policy learning (MLP, transformer, diffusion, flow matching, SSM, SNN, frequency, action tokenisation, drift).
- 7 Bottlenecks: 7.1 data (collection: teleoperation, human-in-the-loop, synthetic, crowdsourcing; utilisation: selection, retrieval, augmentation, expansion, reweighting); 7.2 generalisation (environment: sim2real / real2sim2real, SE(3)/SIM(3) equivariance; task: long-horizon, compositional, few-shot, meta, lifelong; cross-embodiment: human-to-robot, similar, heterogeneous); 7.3 agent; 7.4 HRI.
- 8 Applications; 9 Future directions (9.1 robot brain; 9.2 data; 9.3 multimodal contact-rich; 9.4 safety); 10 Conclusion.
- Dexterous subsection (4.3): definition "in-hand reorientation, fine force modulation, and multi-point contact"; "Human hand models typically include 20–25 DoF, with each finger modeled by 4 DoF, the thumb by 4–5 DoF" [287]. Non-learning: "heuristic search and constrained optimization [291]". Learning: PDDM (model-based); model-free [11]; HIL-SERL; DexScrew (RL finger primitives in sim, then tactile-conditioned BC); DexMV (kinematic retargeting from video); contact-prediction and inverse-dynamics auxiliaries; SAT (joint-wise trajectories, "across heterogeneous hand embodiments"); hybrid IL–RL; ViViDex (privileged RL then IL distillation); VLAs: DexGraspVLA, OFA, LBM, Being-H0, UniDex, Dexora ("high-dimensional dual-arm and dual-hand manipulation"); human guidance (Chen et al., Mandi et al.); affordance; task decomposition; REBOOT reset policies. Challenges: long-horizon, sim-to-real, perception under occlusion (DexPoint).
- Tactile (6.2.3, Fig. 18): representation (T-DEX, Sparsh, CLTP, exUMI, Tactile Beyond Pixels); tactile-action (Seq2Seq Imitation, RoboPack, MimicTouch, Feel the Force, SimShear); tactile-vision-action (RotateIt, Multimodal-SeeThrough, VTTB, VITaL, VT-Refine "precise bimanual assembly", Reactive Diffusion Policy, ViTaS, ViTacGen, ViTacFormer, GelFusion); tactile-language (Octopi, TLA); tactile-VLA (FuSe, VLA-Touch, Tactile-VLA, OmniVTLA, VTLA, T-Rex, FTP-1). The "Tactile-Vision-Action Models" paragraph is printed twice with different wording (lines ~1541 and ~1548).
- Reward / loss: none of its own.

## Evaluation
- Sec. 2.4, verbatim: "The most commonly used metric for evaluating robotic performance is the success rate, which measures whether a given task is completed successfully. For long-horizon tasks [82], this has been extended to metrics such as average success length, which captures the average number of consecutive tasks completed within a sequence of up to n tasks. Beyond success-based measures, efficiency metrics such as task completion time and action frequency are also employed ... In RL settings, return is also widely used as an overall measure of performance."
- Model selection (Sec. 2.4): "evaluate the model every k epochs and select the checkpoint with the highest success rate"; or "average the results of the top-n checkpoints from the final training phase"; multi-task: "reporting performance at the final training epoch or step".
- No numbers of its own; no results tables.
- real robot: n/a.

## Limitations stated by the authors
- Sec. 1: "non-learning methods are primarily introduced as methodological background".
- Sec. 1.1: for dexterous and other non-basic categories "we briefly introduce classical non-learning methods and place greater emphasis on learning-based approaches"; the full planning / action / actuation taxonomy "is developed primarily in the context of basic manipulation".
- Sec. 2.1 on dexterous hands: "the increased number of controllable joints also enlarges the action space and places substantially greater demands on sensing, calibration, demonstration quality, and closed-loop policy learning."

## Gaps / open problems named (verbatim)
- Sec. 1.2: "current robot learning has not yet exhibited a reliable scaling law comparable to those observed in language and vision, largely because of the high cost of physical data acquisition and the limitations of simulation."
- Sec. 4.3 Challenges: "sim-to-real transfer remains a bottleneck due to discrepancies in perception, dynamics, and actuation."; "accurate perception is difficult in cluttered or partially observed scenes, where occlusion hampers object tracking."
- Sec. 9.2: "the gap between simulated and real interaction remains particularly severe for contact-rich manipulation, where friction, compliance, collision, deformation, and sensor noise are difficult to reproduce accurately."
- Sec. 9.2: "Real-world robot datasets remain fragmented across hardware platforms, action spaces, sensor configurations, and collection protocols."
- Sec. 9.3: "The main challenge is not simply adding more sensors, but learning representations that align heterogeneous, asynchronous, and multi-rate signals while preserving information relevant to action."
- Sec. 9.3: "Small errors in geometry or force can rapidly turn into task failure. Future research therefore needs policies that jointly reason about geometry, contact, compliance, and dynamics rather than treating motion as purely kinematic trajectory generation."
- Sec. 9.1: world models must "move beyond visually plausible future prediction toward physically grounded models that capture contact, force transmission, object permanence, and causal interactions".
- Sec. 9.4: "reliability becomes as important as task success."
- Sec. 10: "Major open challenges persist, including the development of a unified 'robot brain,' the resolution of data and perception bottlenecks, and the assurance of safety in human–robot collaboration."

## What it does NOT cover
- Dexterous manipulation in depth: one subsection of about 30 lines in a 212-page paper; Sec. 1.2 defers to An et al. [14] and Li et al. [15] ("The developments and challenges toward dexterous and embodied robotic manipulation: A survey", IEEE RAM 2025).
- Hand hardware specs: names only; no DoF / actuation / tactile table (contrast welte_iil_survey_2025 Table 1).
- Dexterous benchmarks: one paragraph (Sec. 3.2): "[11]" DAPG, TriFinger, DexJoCo, DexVerse; one "Dex" row in the single-embodiment table.
- Bimanual dexterous (two hands on one object): "bimanual" means arms; Dexora is the only dual-hand mention; no coordination analysis.
- Contact fidelity / penetration: "penetrat" occurs once (CALAMARI, contact-map prediction; unrelated). Physics engines are table columns, never compared.
- Evaluation protocol: Sec. 2.4 is six lines; no trial counts, seeds, or per-task reporting conventions.
- Sim-to-real methods: bullet lists in 7.2.1 and 9.2 (DR, sysID, adaptive transfer, generative synthesis, hybrid, differentiable sim); no method comparison.

## Quotable claims (verbatim, with section)
- Abstract: "we provide the first dedicated taxonomy of key bottlenecks, focusing on data collection, utilization, and generalization".
- Sec. 1.2: "Existing surveys typically adopt narrower perspectives. Some focus on particular task domains, such as dexterous manipulation [14, 15]".
- Sec. 2.1: "Their articulated structures enable object reorientation, in-hand manipulation, tool use, and coordinated multi-contact interaction."
- Sec. 3.2: "growing attention has been devoted to tactile sensing for policy learning and evaluation in contact-rich manipulation tasks [123, 124, 143]."

## Notes for the survey
- Feeds: the "general manipulation surveys treat hands in passing" positioning sentence (cite Sec. 1.2 and the length of 4.3); Sec. 2.4 as the field's default evaluation statement (success rate + checkpoint selection) that we then argue is insufficient for contact quality; Sec. 6.2.3 as a ready tactile-policy reading list.
- Code README (commit b208a663): version 2 of the paper released 2026/08; a T-RO version ("Embodied Robot Manipulation in the Era of Foundation Models: Planning and Learning Perspectives", arXiv 2512.22983) accepted 2026/08. The markdown on disk was fetched 2026-09-17 from arxiv.org/pdf/2510.10903, so it is likely v2; cite the arXiv version explicitly.
- Contradiction to record: Sec. 2.4 treats success rate as the metric; an_dexil_survey_2025 Sec. VI.B and firoozi_foundation_models_2023 Sec. VI.H say results are not comparable across setups. Bai never says how success is judged for dexterous tasks.
- The converter garbled the Fig. 5 caption into the Sec. 4.3 text (repeated "249, 250, 288–290]" fragments around line 659); do not quote that sentence.
