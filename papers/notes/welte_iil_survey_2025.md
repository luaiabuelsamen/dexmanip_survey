# welte_iil_survey_2025 — Interactive Imitation Learning for Dexterous Robotic Manipulation: Challenges and Perspectives — A Survey (Welte & Rayyes, KIT; Frontiers in Robotics and AI 2025; arXiv 2506.00098; preprint dated August 16, 2025)

sources: papers/md/welte_iil_survey_2025.md [1dea296a] ; no code

## One-line contribution
Argues that interactive imitation learning (IIL: on-policy human corrections or evaluations during execution) is the under-used route to real-world dexterous manipulation; finds only seven IIL-related dexterous works (Sec. 3.3) and therefore reviews IIL in general robotics (Sec. 4) to say how it could transfer. Carries a table of 15 commercial anthropomorphic hands (Table 1) and a keyword bibliometric of 326 "dexterous manipulation" papers from 2023-24 (Fig. 3).

## Setting
- hand(s): survey. Table 1 (Sec. 2) lists 15 commercial hands with DoA / DoF / actuation / fingers / fingertip force / payload / weight / tactile, e.g. Shadow Dexterous Hand 20 DoA / 24 DoF, tendon-driven, 5 fingers, 4.3 kg, tactile yes; TESOLLO DG-5F 20/20 direct-drive; Allegro V4/V5 16/16 direct drive, 4 fingers, 1.0 kg, tactile yes; LEAP 16/16 direct drive, 4 fingers, tactile no; XHAND1 12/12; Schunk SVH 9 DoA / 20 DoF; qb SoftHand2 Research 2 DoA / 19 DoF. Table footnote: "Payload depends on measurement method, tactile sensors include configurable options". Manufacturer figures reproduced by the survey, not measurements.
- Sec. 2: "Among them, 2/3 are nearly fully actuated"; Figure AI, 1X, Tesla hands "are not yet openly available for research or third-party development."
- single/bimanual: single-hand throughout; bimanual appears only inside DexCap ("two 16-DoF robotic hands", Sec. 3.3) and RoboCopilot (Sec. 4).
- simulator: Sec. 3.2.3 names Isaac Sim, GENESIS, MuJoCo and states "Developing more powerful and realistic simulators ... will not completely close the reality gap."
- observation / action: not tabulated per method.

## Method (taxonomy = section structure)
- Sec. 2 Dexterous Manipulation: Hardware, Challenges, and Trends. Actuation split "mechanical links, tendon-driven, and direct drive". Eight bibliometric categories (Table 2): Machine Learning and AI; Sensing and Perception; Control Systems and Planning; Human-Robot Interaction and Collaboration; Mechanics, Dynamics, and Structural Design; Application-Specific Studies; Simulation, Benchmarking, and Evaluation; Haptic and Tactile Interfaces. Fig. 3 shares (2023+2024, n=326, Scopus + IEEEXplore): ML/AI 31 %, Sensing 12 %, Application 9 %, HRI 8 %; the remaining labels in the flattened figure text are "Simulation, Benchmarking, and Evaluation 2% 6% Haptic and Tactile Interfaces" and "Mechanics ... Control Systems and Planning 18% 14%", so the 2/6 and 18/14 assignments are ambiguous in the source; the text of Sec. 2 says haptic/tactile "are not represented in large numbers", consistent with haptic = 2 %.
- Sec. 3 Real-world Learning: 3.1 IL, organised by three challenges: 3.1.1 high-dimensional action space (split policy; latent synergy space via PCA "only five dimensions" (Ben Amor et al. 2012) or VAE; reduce input dimensionality; non-parametric nearest-neighbour, DIME); 3.1.2 multi-modality from contact (latent-variable/ACT, mixture density, energy-based, discretised, diffusion); 3.1.3 long-horizon (DexSkills, VLMs). 3.2 RL: 3.2.1 from scratch; 3.2.2 RL + demonstrations (DAPG, AWAC); 3.2.3 sim-to-real RL. 3.3 IIL for dexterous manipulation (Kaya & Oztop 2018; Ugur 2011; Argall 2011 TPC; Sauser 2012; Ding 2023 preference RL; Tilde 2024; DexCap 2024).
- Sec. 4 IIL in robotics: feedback split into corrective (absolute actions or relative corrections) vs evaluative (human reinforcement or preferences); Table 3 crosses feedback type with policy representation (linear/RBF, FFN, CNN, RNN/LSTM, diffusion, DMP/ProMP).
- No reward or loss terms of its own.

## Evaluation
- metrics: none defined. "success rate" occurs twice, both inside cited-work descriptions.
- numbers carried from cited work (all Sec. 3): DAPG on a real Allegro "cutting training time from 4-7 hours without demonstrations to 2-3 hours with 20 demonstrations" (Zhu et al. 2019, Sec. 3.2.2); Rubik's cube "over 900 parallel workers were used over multiple months to collect data corresponding to 13.000 years of experience in simulation" (Akkaya et al. 2019, Sec. 3.2.3); DexCap "33% improvement by fine-tuning with corrections on six household manipulation tasks with two 16-DoF robotic hands" (Sec. 3.3); 3D Diffusion Policy "as few as 10-40 demonstrations" vs diffusion policies that "often require over 100 expert demonstrations" (Sec. 3.1.2); Tilde: DeltaHand "four fingers, each possessing 3 DoF", "seven distinct manipulation tasks" (Sec. 3.3).
- real robot: n/a.

## Limitations stated by the authors
- Sec. 3.3: "only a limited number of works have explored interactive human involvement in real-world dexterous manipulation tasks"; "Not all of these works aim to learn generalized policies."
- Sec. 3.3, causes: "the need for physical hardware ... an especially costly requirement"; "the availability of suitable robotic hands remains limited"; "sim-to-real transfer remains a significant challenge, often requiring substantial engineering effort".
- Sec. 3.2.3, opinion: "We believe that using such a vast amount of computational resources to train a single task is not an effective approach."

## Gaps / open problems named (verbatim)
- Sec. 3.3: "Current works demonstrate the viability of IIL, but also reveal gaps—such as the limited use of tactile feedback and generalization in unstructured environments—that point to valuable directions for future research."
- Sec. 2: "haptic and tactile interfaces are not represented in large numbers, although they offer, in our opinion, great potential for interactive learning between humans and robots".
- Sec. 3.1: "Publications that deal with long-horizon tasks specifically for dexterous manipulation are very rare."; "all those applications do not fully utilize the dexterity of an anthropomorphic hand."
- Sec. 3.1.3: "The highlighted publications reveal two most prominent challenges: generalization across tasks and the ability to handle long-horizon behaviors."
- Sec. 4: "the question of how an interface between a robot and a human should be designed so that the human can comfortably provide valuable feedback to the robot."
- Sec. 5: "Bridging the gap between current capabilities and real-world demands will require continued exploration of interactive learning paradigms, integration of tactile and multimodal feedback, and adaptation of successful strategies from broader robotic domains."

## What it does NOT cover
- Bimanual / two hands on one object: three "bimanual" mentions in 687 lines, all descriptive (DexCap, RoboCopilot, Bi-KVIL); no bimanual section, no coordination discussion.
- Evaluation protocol: no metric definitions, no benchmark table; "Simulation, Benchmarking, and Evaluation" is counted in Fig. 3 but not reviewed.
- Contact modelling / penetration: none ("penetrat" 0 occurrences); the sim-to-real paragraph (3.2.3) treats the gap via domain randomization only.
- RL depth: Sec. 3.2 is three short subsections; no reward design; the only algorithm comparison is DAPG vs AWAC ("AWAC can achieve faster learning and better data efficiency than DAPG", Nair et al. 2020).
- Retargeting, teleoperation systems, datasets: mentioned only inside DexCap / Tilde descriptions; no taxonomy (contrast an_dexil_survey_2025 Sec. V).
- Hands: Table 1 is commercial hands only; research hands beyond LEAP and mimic are absent; Figure AI / 1X / Tesla excluded by its own statement.
- Simulators: named, not compared.

## Quotable claims (verbatim, with section)
- Abstract: "While interactive imitation learning has shown success in various robotic tasks, its application to dexterous manipulation remains limited."
- Sec. 2: "Dexterous Manipulation is a specialized field in robotics focused on controlling multi-fingered end effectors to grasp and manipulate objects effectively (Okamura et al., 2000)."
- Sec. 3.1: "the applications of dexterous manipulation using imitation learning are currently confined to relatively simple tasks."
- Sec. 3.1.3: "demonstrations represent an upper bound that the policy cannot exceed."
- Sec. 3.2.2: "Only a few studies use reinforcement learning with demonstrations on physical robots (Gupta et al., 2016; Zhu et al., 2019; Nair et al., 2020). Their ability to conduct real-world experiments hinges on the constraint of basing their policy on low-dimensional state spaces".
- Sec. 3.2.3: "sim-to-real zero-shot achieves only limited performance due to the reality gap (Gilles et al., 2024, 2025)."; "Especially for dexterous manipulation with its complex dynamics, it is challenging to create a simulation model that corresponds to reality."

## Notes for the survey
- Feeds: hardware table (cross-check DoF/DoA against the vendor-page notes before reuse; Welte's figures are secondary); the three-challenge framing of IL for hands (3.1.1-3.1.3); IIL as a paradigm to cite and set aside.
- The PDF's running header reads "(PREPRINT) DIFFUSION MODELS FOR ROBOTIC MANIPULATION: A SURVEY" on every page (e.g. lines 8, 37): a template artefact from another paper. Do not cite that title.
- an_dexil_survey_2025 Sec. I summarises this paper as having "examined the potential of interactive imitation learning for humanoid robots"; the paper's own framing is dexterous hands, with humanoids as motivation.
- Positioning: Fig. 3's shares for evaluation and tactile are the numbers to quote when arguing evaluation protocol is under-studied; they are keyword counts ("checked on 05.08.2025", Fig. 2 caption), not a reviewed sample, and the 2 %/6 % split is ambiguous in the flattened figure.
