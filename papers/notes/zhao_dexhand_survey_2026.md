# zhao_dexhand_survey_2026 — Towards Robotic Dexterous Hand Intelligence: A Survey (Zhao et al., arXiv 2026)

sources: papers/md/zhao_dexhand_survey_2026.md [82cd2cac] ; no code

## One-line contribution
A 22-page survey (Zhao, Liang, Guo, Zhang, King, Huang; Liverpool / XJTLU / Duke Kunshan / CUHK) that organises dexterous-hand research into four aspects: hardware anatomy (actuation, transmission, perception, Table I of 29 hands), methods grouped by task category x learning paradigm with timelines, datasets/modalities/evaluation (Table II of 15 datasets), and a limitations-to-directions section (Sec. V). No experiments, no numbers of its own.

## Setting
- hand(s): none used; Table I ("ANATOMY OF EXISTING DEXTEROUS HANDS", Sec. II-D) lists 29 hands from SKKU Hand II (2006) to Optimus Gen 3 (2026) and EFORT Dexterous I (2026) with columns Year, Actuation, Transmission, Tactile, Fingers, DoF, Voltage, Current, Capacity, Weight, Communication, Developer. Entries relevant to this corpus, as the table prints them: Shadow Hand 2021, EA, LBT, tactile yes, 5 fingers, 24 DoF, 48V, 2.5A, 5 kg capacity, 4.3 kg, EtherCAT; ShadowHand LITE 2018, 4 fingers, 13 DoF; LEAP Hand II 2023, EA, TDT, no tactile, 5 fingers, 21 DoF, 1.0 kg; RH56DFX (Inspire) 2020, 6 DoF; Unitree Dex3-1 2024, 3 fingers, 7 DoF; Unitree Dex5-1P 2025, 20 DoF; XHAND1 2024, 12 DoF; Skilhand (AgiBot) 2024, 19 DoF; Optimus Gen 3 2026, HA, LRST, 22 DoF; DG-5F (Tesollo) 2024, 20 DoF. Odd cells worth flagging: the Shadow Hand row says transmission "LBT" (linkage) although Sec. II-B text names the Shadow Dexterous Hand as the canonical tendon-driven (TDT) example; "ShadowHand Ertra LITE" is a typo in the source; MPL is listed at 26 DoF. Allegro is absent from Table I (it appears only in Table II datasets).
- arm: not discussed ; single/bimanual: one sub-section (III-F) on bimanual.
- simulator / physics: not covered. The words "simulator", "SAPIEN", "PyBullet", "Genesis" do not occur; "Isaac" occurs once and "MuJoCo" once, both in Sec. IV-A ("validate candidates in physics engines such as MuJoCo or Isaac Gym [198]"). No timestep, contact model or solver appears anywhere.
- observation: Sec. II-C classifies perception into Proprioception (joint pose, motion state/IMU, joint force/torque, tendon tension, FBG), Tactile Sensing ("resistive, capacitive, piezoelectric, triboelectric, optoelectronic, fluidic, and vision-based") and Multimodal Vision Perception (fusion at "data, feature, and decision levels").
- action space: not discussed as such.
- objects / data: Table II ("SUMMARY OF MAJOR DEXTEROUS HAND DATASETS", Sec. IV) lists 15 datasets 2022-2025 with Year/Scene, Modality, Embodiment, Collection, Scale: DexGraspNet (1.32M poses; 5355 objects), GenDexGrasp (436K poses; 58 objects), DexMV (700 demos), DexArt (82 objects; "Adroit; Allegro"), UniDexGrasp++ (1.32M poses; 5355 objects), RealDex (59K poses; 52 objects; 2.6K seqs.), DexCap (3.5h demo), DexFuncGrasp (14K+ Pose; 559 objects), RH20T (110K+ seqs.), DexGraspAnything (3.4M grasps; 15.7K objects), BODex (3.08M grasps; 2397 objects), CEDex (20M grasps; 500K objects), Dex1B (1B demos; 6K+ objects), DexTOG (80K grasps; 80 objects), VTDexManip (182 objects; 2032 seqs.). Table II's citation numbers are inconsistent with the text (e.g. DexGraspNet is [181] in Table II but [181] is DexMimicGen in Sec. III-F), so cross-referencing by number is unreliable.

## Method
- paradigm: survey ; literature collected "primarily ... through the EI and Web of Science databases" (Sec. I).
- Taxonomy (Fig. 3 "Research on Dexterous Hand", Sec. III): five task categories, each split by method paradigm.
  1. In-Hand Manipulation (III-B): Reinforcement Learning, Diffusion Policy, Imitation Learning, Model-based Control, VLA, Other. Timeline Fig. 4 (2015-2025; names include Popov, Andrychowicz, Bi-DexHands, MyoDex, DexPoint, KODex, DextrAH-G, DexVLA, OmniVLA, DexHandDiff, ManiDext).
  2. Grasping & Pick-and-Place (III-C): RL, Diffusion Policy, Imitation Learning, Representation Learning, VLA, Other. Timeline Fig. 5 (D-Grasp, DexMV, UniDexGrasp/++, CrossDex, SpringGrasp, DextrAH-RGB, DexGraspVLA, GraspVLA, UniGraspTransformer, D3Grasp).
  3. Tool & Device Operation (III-D): RL, Imitation Learning, VLA, Other. Timeline Fig. 8 (PDDM, TOG-Net, RT-2, pi0, DexGen, MimicFunc, Hierarchical RL).
  4. Human Interaction (III-E): RL, Imitation Learning only.
  5. Bimanual Manipulation (III-F): RL, Diffusion Policy, Imitation Learning, VLA, Representation Learning, Other. Timeline Fig. 9 (2022-2025: Bi-DexHands, ARCTIC, SIMPLe, TACO, UMI, HATO, BiDexHD, DexMimicGen, PAD, HDP, RDT-1B, Bi-VLA, Shake-VLA, 3D-ViTac, RoboMIND, ManipTrans, "Unified Bimanual").
- Hardware taxonomy (Sec. II): actuation = Electromagnetic (EA), Fluidic (FA), Smart-Material (SMA), Hybrid (HA); transmission = Tendon-Driven (TDT), Linkage-Based (LBT), Gear-Based (GT), Lead/Roller-Screw (LRST), Belt-Cable-Pulley (BCPT), Direct/Integrated (DIT); perception = proprioception, tactile, multimodal vision.
- Workflow (Fig. 2, Sec. III-A): "three-stage closed loop" of task planning, policy training ("simulation and collected data ... domain randomization, calibration, and sim-to-real adaptation"), deployment.
- Data taxonomy (Sec. IV-A): "optimization-based acquisition in simulation, learning-based acquisition in simulation, and human capture".
- reward or loss: none (survey).
- key trick(s): none.

## Evaluation
- metrics (as the survey describes the field, Sec. IV-C "Evaluation Metric"): "existing works usually assess at least two layers of performance: the quality of grasps or poses prior to execution, and the performance of policies or generators during downstream execution. For grasp- and pose-centric datasets, the most common criteria concern physical plausibility, including penetration, analytic or quasi-static stability, and diversity". "task success rate remains the dominant endpoint, but its interpretation depends strongly on the evaluation protocol." The only occurrence of "penetration" in the paper is this sentence; no penetration threshold or measurement method is given.
- headline numbers: none of its own. The only success rates quoted are other papers' claims in Sec. III-C: DexGraspVLA "overall success rate of 89.6%" and GraspVLA "91.2% success on unseen objects".
- baselines beaten: n/a.
- real robot? n/a.

## Limitations stated by the authors
Sec. V pairs each bottleneck with a direction; the four named gaps, verbatim from the bold headings:
1. "From the trade-off between bionic complexity and hardware feasibility to scalable dexterous hand design."
2. "From the dilemma of multimodal perception fusion to robust and interpretable perception."
3. "From limitations in learning, control, and data to robust and generalizable learning frameworks beyond benchmark-centric optimization."
4. "From system integration and industrialization barriers to deployable dexterous platforms."
Supporting statements (Sec. V): "Existing datasets also lack sufficient diversity in long-horizon interactions, failure cases, and recovery behaviors, and tactile information is often underutilized." "the absence of unified performance evaluation standards and benchmark protocols hampers objective comparison across systems, slowing standardization and industrialization. Establishing authoritative evaluation frameworks is therefore essential". "the sim-to-real gap continues to degrade real-world performance despite domain randomization and adaptation efforts". Sec. IV-C "Reliability and Trustworthiness" proposes future criteria: "uncertainty calibration, robustness to occlusion and clutter, out-of-distribution detection, failure prediction, recovery rate, safety violation rate, and multimodal consistency across vision, tactile sensing, and proprioception."
The survey states no limitations of itself.

## What it does not cover
- Simulators and physics: no section on simulation engines, contact models, timesteps, solver settings or GPU-parallel simulation; Isaac Gym and MuJoCo are each named once, in passing, as grasp validators (Sec. IV-A).
- Benchmarks as objects of study: no benchmark table. Of the corpus benchmarks, Bi-DexHands is cited ("first systematic learning platform for bimanual dexterous manipulation", III-F) and DexArt appears in Table II as a dataset; HumanoidBench, RoboHive, DexVerse, Bench2Dex, Isaac Gym / IsaacGymEnvs and the Gym Shadow Hand tasks are not mentioned (grep: 0 hits each).
- Measurement rigour: no discussion of seeds, variance, confidence intervals or reproducibility protocols (grep: "seed" 0, "variance" 0, "confidence" 0, "reproducib" 1 - used only for "reproducible labels" of optimisation-based grasp data). Interpenetration is never treated as a measured quantity.
- Bimanual: one 1.5-page sub-section (III-F) of 16 cited works, mostly single-paragraph summaries; no bimanual benchmark comparison, no bimanual success criteria, no two-hands-one-object contact analysis.
- Humanoid whole-body manipulation with hands: "humanoid" appears 6 times, only for the Tesla Optimus hand hardware and "large-scale humanoid platforms" in Sec. II.
- Observation/action-space conventions, control rates, and reward design are not compared across works.
- Teleoperation and data-collection hardware are covered only as a "human capture" family (IV-A).

## Quotable claims (verbatim, with section)
- Sec. I: "existing studies are often developed under different assumptions regarding hand embodiments, sensory configurations, task settings, training data, and evaluation protocols, making systematic comparison difficult and obscuring the developmental trajectory of the field." (Abstract)
- Sec. II-D: "Table I highlights that dexterous hands span a wide range of design envelopes rather than converging on a single best architecture."
- Sec. III-F: "Bimanual manipulation requires synchronized control of two high-DoF hands under complex contact dynamics, making coordination, force allocation, and stability notably more challenging than single-hand tasks."
- Sec. III-F: "Bi-DexHands[90] establishes the first systematic learning platform for bimanual dexterous manipulation ... serving as a key benchmark for advancing human-level bimanual manipulation research."
- Sec. IV-C: "the success rate is meaningful only when paired with a clear specification of whether it reflects nominal execution, cross-instance generalization, or robustness to sensing perturbations"
- Sec. IV-C: "A system may perform well under nominal benchmark settings, yet still fail under occlusion, sensor noise, ambiguous object boundaries, unseen objects, changing contact conditions, or human intervention"
- Sec. V: "In addition, the absence of unified performance evaluation standards and benchmark protocols hampers objective comparison across systems, slowing standardization and industrialization."
- Sec. V: "High-performance systems such as the Shadow Hand are expensive to manufacture and maintain, while low-cost or open-source alternatives often sacrifice sensing quality, material durability, or long-term reliability"
- Sec. VI: "the lack of unified evaluation standards continues to hinder fair comparison across different systems and methods."

## Notes for the survey (which sections this feeds; contradictions with other notes)
- Feeds: related-surveys paragraph (this is the most recent holistic survey; its own positioning vs. hardware [2-4], sensing [5-8], learning [9-12] and holistic [13-16] surveys is in Sec. I); the hand table (Table I gives DoF/weight/interface for 29 hands, to be cross-checked against vendor notes since these are secondary values); the evaluation-practices section (its Sec. IV-C two-layer view: grasp validity vs. execution success).
- Differentiation for our survey: it has no simulator/physics coverage, no benchmark comparison, no bimanual benchmark, and treats penetration as one word in a list. Our bimanual coverage (Bi-DexHands, Bench2Dex, DexVerse, HumanoidBench) and the measurement-rigour thread (interpenetration as a measured quantity, replay vs. live physics, seed variance) are absent here, which supports the "why" in the bib entry.
- Its own call for "authoritative evaluation frameworks" (Sec. V) and for reporting success with its protocol (Sec. IV-C) is a quotable motivation for a measurement-centred benchmark section.
- Contradictions/cautions: Table I's Shadow Hand transmission "LBT" contradicts its own Sec. II-B text (tendon-driven); Table II lists DexArt's embodiment as "Adroit; Allegro" - check against the dexart_2023 note before quoting. Table II citation numbers do not match the reference list numbering used in the body text.
