# zhao_sim2real_survey_2020 — Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey (Zhao, Peña Queralta, Westerlund; IEEE SSCI 2020; arXiv 2009.13303)

sources: papers/md/zhao_sim2real_survey_2020.md [5709cdf4] ; no code

## One-line contribution
Eight-page survey (manifest: pages 8) that sorts sim-to-real methods for deep RL into zero-shot transfer, system identification, domain randomization, domain adaptation, learning with disturbances, and choice of simulator, and tabulates 21 works (Table I) by task, platform, algorithm, simulator and transfer trick. Claims to be "the first survey that describes the different methods being utilized towards closing the simulation-to-reality gap in DRL for robotics" (Sec. I).

## Setting
- hand(s): none of its own. Multi-fingered hands appear only as two cited works: ADROIT 24-DoF hand (Rajeswaran et al. [5], DAPG, MuJoCo, "Imitation learning via demonstrators with VR", Table I last column) and "a physical five-fingered hand" [57] (OpenAI, Sec. III.C). Single hand only.
- simulator / physics: survey-level. Sec. III.F: "The most widely used simulators in the literature are Gazebo [74], Unity3D, and PyBullet [75] or MuJoCo [17]"; "Gazebo suits more complex scenarios while PyBullet and MuJoCo provide faster training." Table I "Simulator / Engine" row: Gazebo, PyBullet, MuJoCo, Unity3D, V-Rep, custom. No GPU-parallel simulator is named.
- observation / action: not treated per method; the survey splits randomization into "visual randomization" and "dynamics randomization" (Sec. III.C).
- objects / data: none.

## Method (taxonomy = section structure)
- II Background: A Deep RL; B Sim-to-Real Transfer; C Transfer Learning and Domain Adaptation; D Knowledge Distillation; E Meta RL; F Robust RL and Imitation Learning.
- III Methodologies: A Zero-shot Transfer; B System Identification; C Domain Randomization (visual vs dynamics); D Domain Adaptation (discrepancy-based, adversarial-based, reconstruction-based); E Learning with Disturbances; F Simulation Environments.
- IV Application Scenarios: A Dexterous Robotic Manipulation; B Robotic Navigation; C Other (plasma jet, tactile sensing, multi-agent manipulation).
- V Main Challenges and Future Directions; VI Conclusion.
- Domain-adaptation formalism (Sec. III.D): source D_S = (S_S, A_S, P_S, R_S), target D_T = (S_T, A_T, P_T, R_T); "the states S of the source and target domain can be quite different (S_S ≠ S_T) due to the perceptual-reality gap [64], while both domains share the action spaces and the transitions P (A_S ≈ A_T, P_S ≈ P_T) and their reward functions R have structural similarity (R_S ≈ R_T)."
- The only hand-specific method content (Sec. III.C, on [57]): "randomizes various physical parameters in the simulator, such as object dimensions, objects and robot link masses, surface friction coefficients, robot joint damping coefficients and actuator force gains."

## Evaluation
- metrics: none defined; no numbers of its own. Table I is qualitative (task / platform / algorithm / simulator / transfer trick). "success rate" occurs 0 times.
- headline numbers: none. One borrowed qualitative finding (Sec. IV.A, on Matas et al. [6]): "excessive domain randomization can be detrimental. Specifically, when the number of different colors that were being used for each texture was too large, the performance of the real robot was significantly worse."
- baselines / real robot: not applicable.

## Limitations stated by the authors
- Scope (Sec. I): "we do not cover specific simulators or techniques for direct learning in real-world settings"; "The focus is mostly in end-to-end approaches".
- Sec. V: "For domain randomization, researchers tend to study empirically examining which randomization to add, but it is hard to explain formally how and why it works, which thereby brings the difficulty of designing efficiently simulations and randomization distributions. For domain adaptation, most existing algorithms focus on homogeneous deep domain adaptation, which assumes that the feature spaces between the source and target domains are the same. However, this assumption may not be true in many applications."
- Sec. VI: "wider theoretical and empirical studies are required to better understand the effect of these techniques in the learning process. Moreover, generalization of existing results with a more comprehensive analysis is also lacking in the literature."

## Gaps / open problems named (verbatim)
- Sec. V: "Two of the most promising research directions are: (i) integration of different existing methods for more efficient transfer (e.g., domain randomization and domain adaptation); and (ii) incremental complexity learning, continual learning, and reward shaping for complex or multi-step tasks."
- Sec. IV.A, force control as the sim-to-real-relevant failure: "applying excessive force to real objects might cause damage, while grasping can fail with a lack of force."
- Sec. IV.B: for navigation, "the lack of standard simulation environments" (contrasted with manipulation, where it says standards exist).

## What it does NOT cover
- Bimanual: 0 occurrences of "bimanual"; the only multi-agent entry is D'Kitty locomotion-manipulation [44].
- Tactile: 3 occurrences, all pointing at Ding et al. [43] "Sim-to-real transfer for optical tactile sensing"; no tactile-in-the-loop policy.
- Multi-fingered hands: two cited works ([5], [57]); no per-hand discussion, no hand table.
- Evaluation protocol: no metric definitions, no trial counts, no success-rate reporting.
- Contact / penetration: no mention of contact modelling fidelity, penetration, or solver choice; the simulator comparison (Sec. III.F) is speed vs ROS integration only.
- Imitation-only pipelines, retargeting, teleoperation: outside scope (RL transfer only; IL is a background subsection II.F).
- Post-2020 methods (automatic DR, real-to-sim, GPU-parallel simulation): absent.

## Quotable claims (verbatim, with section)
- Sec. IV: "Owing to the limited operational space in which most robotic arms operate, simulation environments for dexterous manipulation are relatively easier to generate than those for more complex robotic systems."
- Sec. VI: "Domain randomization has been identified as the most widely adopted method for increasing the realism of simulation and better prepare for the real world."
- Sec. III.C, on [57]: "Their successful sim-to-real transfer experiments show the powerful effect of domain randomization."
- Sec. I: "Deep reinforcement learning (DRL) algorithms have been successfully deployed in various types of simulation environments, yet their success beyond simulated worlds has been limited. An exception to this is, however, robotic tasks involving object manipulation [5], [6]."

## Notes for the survey
- Feeds: sim-to-real section (its DR / DA / sysID split is the standard one to cite); positions our simulator and contact-fidelity discussion as something this survey explicitly leaves out.
- Contradiction to flag: Sec. IV's "relatively easier to generate" claim for dexterous sims sits against an_dexil_survey_2025 Sec. VI.A/B and welte_iil_survey_2025 Sec. 3.2.3, both of which name contact dynamics in dexterous sims as the hard part of the gap.
- Its DA formalism assumes A_S ≈ A_T; that assumption is exactly what retargeting across hands breaks. Cite when motivating cross-embodiment sections.
- Age and size: 2020, 8 pages, SSCI. Background citation, not state of the art.
