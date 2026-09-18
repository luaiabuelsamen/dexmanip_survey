# an_dexil_survey_2025 — Dexterous Manipulation through Imitation Learning: A Survey (An, Meng, Tang, Zhou, Liu, Ding, Zhang, Mu, Song, Zhang, Hou, Zhang; arXiv 2504.03515, 2025; page header "JOURNAL OF LATEX CLASS FILES ... DEC. 2025")

sources: papers/md/an_dexil_survey_2025.md [c9b206b4] ; no code

## One-line contribution
The closest existing survey to ours: IL for multi-fingered end-effectors organised by IL family (BC / IRL / GAIL / hierarchical / continual), by end-effector class (two-finger / multi-finger / three-finger / tactile), by demonstration source (teleoperation modality / video), plus datasets and an eight-part challenges section with a prioritisation roadmap (Fig. 6, Sec. VI.H).

## Setting
- hand(s): survey. Sec. IV: A two-fingered gripper; B multi-fingered anthropomorphic hand; C three-fingered claw "A Trade-off Solution"; D tactile sensors; E impact of end-effector design on IL. Hands named in Sec. IV.E: Shadow Hand ("20+ DoF", tendon-driven), BarrettHand (rigid linkage, underactuated), LEAP (direct drive: "millimeter-level control precision ... increased inertia due to motor mass"), DoraHand (three-finger), ILDA Hand, RAPID Hand ("< 7 ms response delay"). Table IV compares the three end-effector classes (line 377; not read in full).
- single/bimanual: single by default. Sec. II.E "Multi-agent or Collaborative Dexterous Manipulation" is one page: SRT-H (dual-arm da Vinci suturing), BUDS ("76.9% task success on complex bimanual dexterous tasks without reward signals or RL finetuning"), Bi-DexHands ("over 20 cooperative sub-tasks, providing the first large-scale benchmark for evaluating the scalability of multi-agent RL"), BiDexHD; plus whole-body MPC (Sleiman et al.) and dual-arm deformable MPC (Yu et al.).
- simulator / physics: no simulator section; sim appears in VI.A (data), VI.B (benchmarking), VI.D (sim-to-real).
- observation: Sec. IV.D tactile taxonomy: resistive/capacitive; piezoelectric; optical/vision-based (GelSight, TacTip, GelStereo); magnetic/Hall; bio-inspired (BioTac, NeuTouch, GTac).
- objects / data (Sec. V.C): teleoperated: MIME "8,260 human–robot demonstrations across 20 diverse tasks"; RH20T "over 110,000 multimodal manipulation sequences"; BridgeData "7,200 demonstrations across 71 tasks in 10 environments"; BridgeData V2 "60,096 trajectories in 24 environments". Augmented: RoboAgent 7,500 -> "roughly 98,000"; CyberDemo. Synthetic: MimicGen "over 50,000 demonstrations across 18 tasks from roughly 200 human examples"; IntervenGen; DiffGen. Dexterous/bimanual (V.C.4, Table VIII): ARCTIC "2.1 million videos" in text vs "2.1M frames (3D meshes)" in Table VIII (unit disagrees); DexGraspNet "1.32 million grasps for 5,355 objects using ShadowHand, with each grasp physically validated in simulation to ensure stability"; OAKINK2 "627 sequences and 4.01 million frames".

## Method (taxonomy = section structure)
- II Overview: A dexterous manipulation; B IL; C connections to human motor learning; D long-horizon; E multi-agent/collaborative.
- III IL approaches (Sec. III intro): "(1) Behavioral Cloning, (2) Inverse Reinforcement Learning, (3) Generative Adversarial Imitation Learning, and other extended frameworks, including (4) Hierarchical Imitation Learning and (5) Continual Imitation Learning." Table I pros/cons/applications per family; Table II cost/latency/sample efficiency (BC inference "Very Low (<1 ms)", IRL "1–5 ms", GAIL "2–5 ms", HIL "2–10 ms", CIL "2–8 ms"; no citation for these figures); Table III optimisers / regularisers / convergence.
- IV End-effectors (A–E above).
- V Teleoperation and video. V.A teleoperation: 1) vision-based (TeachNet, DexPilot, Robotic Telekinesis, DIME, Transteleop); 2) mocap gloves (DexCap: "two Franka Emika robotic arms, each with a LEAP dexterous robotic hand"; SenseGlove DK1); 3) VR/AR controllers; 4) exoskeleton and bilateral systems; Table VI compares the four. V.B learning from video: 2) synthetic video-driven IL; 3) representation learning; 4) task-specific architectures (item 1 not read). V.C datasets (above); Table IX dataset-quality rubric: sensor modality richness, annotation quality, task & scene diversity, physical realism.
- VI Challenges: A data collection (heterogeneous fusion; quantity/quality/diversity; high-dimensional sparsity; cost); B benchmarking and reproducibility; C generalization (task/env variability; continual; cross-embodiment); D sim-to-real (domain randomization; feature alignment; adversarial DA; hybrid training/online adaptation); E real-time control; F safety, robustness, social compliance; G high-precision/micro-scale; H roadmap.
- Reward / loss: none of its own. Family definitions in Sec. II.B: "Behavior cloning directly maps observed actions to the agent's actions through SL techniques. Conversely, IRL aims to deduce the underlying reward structure ... GAIL employs adversarial training techniques".

## Evaluation
- metrics: none defined; "success rate" occurs 5 times, all in cited-work numbers. No results table across policies.
- numbers carried from cited work: BUDS 76.9 % (Sec. II.E); Huang et al. [257] "removing tactile input causes task success rates to plummet to near-random levels" (Sec. IV.E.3); Lin et al. [285] "reducing motion consistency error by 25% in bimanual coordination tasks" and NeuralFeels "cutting trajectory-consistency error by 25%" (Sec. IV.E.3); RH20T "showed that the demonstration data requirement for high-DoF hands grows exponentially" (Sec. IV.E.1, no figure); "vision at 30 Hz vs. tactile sensing at 1 kHz" (Sec. IV.E.3).
- real robot: n/a.

## Limitations stated by the authors
- Note to Practitioners: "key challenges remain—particularly in collecting high-quality demonstrations and enabling generalization from limited data".
- Sec. VI.B: "Hardware dependency is a major obstacle, as reproducing results requires access to the same robotic platform, gripper design, sensor setup, and control software".
- Sec. VI.B: "the lack of standardized simulation settings, computing environments, and evaluation protocols in physics-based simulators limits fair comparisons across studies. Variability in physics engine configurations, actuator models, contact dynamics, and material properties further exacerbates inconsistencies".

## Gaps / open problems named (verbatim)
- Sec. VI.A.4: "physics engines struggle to model contact dynamics, deformable objects, and high-resolution tactile feedback, leading to discrepancies between simulation and reality."
- Sec. VI.A.2: "establishing standardized data collection protocols and defining robust evaluation metrics for data quality and diversity will be essential".
- Sec. VI.B: "Some studies rely on non-physics-based or simplified simulators, which focus on high-level task planning but neglect low-level contact physics modeling."; remedy: "standardization should focus on consistent physics parameterization (e.g., contact dynamics, actuator models, material properties)".
- Sec. VI.C.3: "A policy trained on one robotic hand may struggle to transfer to another due to differences in degrees of freedom, joint limits, contact dynamics, and control strategies."
- Sec. VI.D.1: domain randomization "struggles to address unmodeled dynamics, such as non-linear material deformations or high-frequency contact interactions, which are crucial for dexterous manipulation."
- Sec. VI.F: "large-scale failure datasets and standardized benchmarks are essential for improving data-driven recovery policies."; "there is a lack of publicly available datasets and simulation environments specifically designed for evaluating social compliance in dexterous manipulation".
- Sec. VI.H roadmap: "Data collection and benchmarking are high-impact areas that require relatively low research difficulty." / "Sim-to-real transfer and real-time control are high-impact challenges that involve significant research difficulty." / safety and high-precision "are high-difficulty but relatively lower in impact".
- Sec. III.F: "the integration of model-based control with imitation learning, which is often underexplored."
- Sec. IV.E: "the influence of end-effector morphology, actuation, and sensor configuration on IL performance has received comparatively limited attention."

## What it does NOT cover
- RL as a subject: RL is background (Sec. II.A: "pure RL has several inherent drawbacks"), a DAPG/hybrid mention, and "RL fine-tuning" in VI.A.3; no RL taxonomy, no reward design, no sim-RL pipeline (DexTreme appears only in the Fig. 1 caption).
- Bimanual as a first-class topic: one subsection (II.E) framed as "multi-agent"; ARCTIC/OAKINK2 listed; no treatment of two-hand coordination or two hands on one object.
- Evaluation protocol: no metric definitions, no trial counts, no statement of how success is scored; VI.B calls for protocols but proposes none.
- Contact quality / penetration: "penetrat" occurs 0 times; DexGraspNet's "physically validated in simulation" is repeated without saying what validation means.
- Simulator comparison: none.
- Hand specs: no hand table (contrast welte_iil_survey_2025 Table 1).

## Quotable claims (verbatim, with section)
- Abstract: "Dexterous manipulation, which refers to the ability of a robotic hand or multi-fingered end-effector to skillfully control, reorient, and manipulate objects through precise, coordinated finger movements and adaptive force modulation".
- Sec. I: "In contrast to these existing works, which primarily focus on specific aspects of imitation learning or dexterous manipulation, this survey aims to provide a comprehensive overview of IL-based dexterous manipulation approaches."
- Sec. IV.E: "Future end-effector designs should follow a 'task–morphology–algorithm' co-optimization paradigm."
- Sec. VI.B: "Unlike computer vision or natural language processing, where large-scale datasets enable standardized evaluations, dexterous manipulation involves physical interactions, making consistent replication across research efforts difficult."

## Notes for the survey
- The survey we must differentiate from. Left open for us: RL and sim-RL pipelines; bimanual coordination beyond a "multi-agent" aside; a concrete evaluation protocol; any measurement of contact / penetration quality in sim (it names contact fidelity as a gap repeatedly in Sec. VI but never quantifies it).
- Related-survey list it gives (Sec. I): Zare et al. (IL general), Arora & Doshi (IRL), Han et al. (DRL for manipulation), Li et al. [39] (data collection + skill learning, dexterous), Pitkevich & Makarov (sim-to-real DRL), Welte & Rayyes [41], Tsuji et al. (IL, contact-rich).
- Cites the classics: Okamura et al. 2000 as [47], Ma & Dollar 2011 as [150], Bicchi as [229] with year "2002" (corpus/bib.json says 2000; check DOI 10.1109/70.897777 before quoting a year). Ref [47] gives the second author as "N. Smaby"; corpus/bib.json says "Smith". Bib error to fix.
- Table II latency figures carry no citation; do not quote as measured.
- ARCTIC size: text "2.1 million videos", Table VIII "2.1M frames". Do not quote either without checking the ARCTIC paper.
