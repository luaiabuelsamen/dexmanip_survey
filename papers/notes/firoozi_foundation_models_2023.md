# firoozi_foundation_models_2023 — Foundation Models in Robotics: Applications, Challenges, and the Future (Firoozi, Tucker, Tian, Majumdar, Sun, Liu, Zhu, Song, Kapoor, Hausman, Ichter, Driess, Wu, Lu, Schwager; arXiv 2312.07843, 2023; bib venue "arXiv / IJRR")

sources: papers/md/firoozi_foundation_models_2023.md [c043fd4e] ; code/md/firoozi_foundation_models_2023.md [58ebfc2a] (Awesome-Robotics-Foundation-Models README; "Config files (0)", "Python signatures and reward/observation bodies (0 files)")

## One-line contribution
33-page (manifest) survey of LLMs / VLMs / generative models in robot decision-making, perception and embodied AI, with a challenges section on data scarcity, real-time inference, multimodal representation, uncertainty quantification, safety evaluation, plug-and-play vs bespoke models, variability, and benchmarking/reproducibility. Self-declared scope (Sec. I): "Background Papers", "Robotics Papers" (plug-and-play, fine-tuned, or new robotic foundation models), "Robotics-Adjacent Papers".

## Setting
- hand(s): none. grep "dexter" hits one sentence (Sec. III.E, on RT-2): "one way to approach this limitation is to collect more diverse and dexterous robotic data". "tactile", "bimanual", "multi-finger", "in-hand": 0 occurrences in 1207 lines.
- arm / platform: RT-1/RT-2 "real-world mobile manipulator robot from Everyday Robots"; RT-2 "action space includes 6-DoF positional and rotational displacement of the robot end-effector, gripper extension, and episode termination command" (Sec. III.E). Parallel-gripper world throughout.
- simulator / physics: Sec. V.B Simulators: Gibson, iGibson, BEHAVIOR-1K, Habitat (-Sim, -Lab, 3.0), RoboTHOR ("75 simulated scenes", "14 scenes each for test-dev and test-standard"), VirtualHome. Sec. VI.H: these "all neglect low-level physics in favor of simulating higher level tasks with high visual fidelity"; PyBullet and MuJoCo named as the physics-based alternatives.
- observation / action: language-conditioned IL formalism (Sec. III.A.1): policy π_θ(a_t | s_t, l); "maximum likelihood goal conditioned imitation objective" over D = {τ_i}, τ_i = {(s_1, l_1, a_1), (s_2, l_2, a_2), ...}; the equation, an image not in the layout-parsed markdown, is recovered as Eq. 9 `LGCIL = E(τ,l)∼D |τ| logπθ(at|st, l),` (9) (recovered by OCR from papers/md/firoozi_foundation_models_2023.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect — the OCR drops the Σ glyph over `|τ|`, leaving the bare bound on its own line).
- objects / data: RT-X "multi-embodiment dataset ... collected through a collaboration between 21 institutions, demonstrating 160266 tasks" (Sec. VI.G); Gato "trained on 604 different tasks", "1.2B parameters" (Sec. V.A).

## Method (taxonomy = section structure)
- II Foundation Models Background: A terminology / preliminaries; B LLMs (heading missing from the markdown); C vision transformers; D VLMs; E embodied multimodal language models; F visual generative models. Table I: CLIP 0.307B, GPT-3 175B, PaLI-X 55B, DALL-E 12B, DALL-E2 3.5B, DINOv2 1.1B, SAM 632M + 63M.
- III Robotics: A policy learning (1 language-conditioned IL: Play-LMP, MCIL, CLIPort, PerAct, Voltron, CACTI, MimicPlay, MUTEX; 2 language-assisted RL: AdA, Palo et al.); B language-image goal-conditioned value learning; C task planning with LLMs; D in-context learning; E robot transformers (RT-1, RT-2, RT-X).
- IV Perception: A open-vocabulary detection / 3D classification; B segmentation; C 3D scene and object representations; D learned affordances; E predictive models.
- V Embodied AI: A generalist AI (Generative Agents, generative simulation, Gato, RRL); B simulators.
- VI Challenges A–H; VII Conclusion.
- Code repo: "The organization of this readme follows Figure 1 in the paper"; a link list with the same tree (Robotics; Perception; Embodied AI); no code, configs or reward functions.

## Evaluation
- metrics: none defined; "success rate" occurs 0 times. Sec. III explains why: papers "either rely on hardware experiments, using custom elements in the low-level control and planning stack that are not easily transferred to other hardware or other experimental setups, or they utilize non-physics-based simulators".
- headline numbers: Table II inference times (Sec. VI.B; not extracted here); [125] "as little as 1%" language-annotated data suffices for a visuo-lingual affordance model (Sec. VI.A.1).
- real robot: n/a.

## Limitations stated by the authors
- Sec. I footnote: "Preliminary release. We are committed to further enhancing and updating this work".
- Sec. I, the five challenges: "1) Data Scarcity ... 2) High Variability ... 3) Uncertainty Quantification ... 4) Safety Evaluation ... 5) Real-Time Performance".
- Sec. VI.H: "Even when physics-based simulators are used (e.g., PyBullet or MuJoCo), the absence of standardized simulation settings, computing environments, and a persistent sim-to-real gap impede efforts to benchmark and compare performance across various research endeavors."

## Gaps / open problems named (verbatim)
- Sec. VI.A.6: "robot physical skills are limited to the distribution of skills observed within the robot data. Using these transformers, the robot lacks the capability to generate new movements."
- Sec. VI.A.2: inpainting augmentation "may result in an image with a physically unrealistic grasp, leading to poor downstream training performance."
- Sec. VI.B: "the inference time for some of the models still needs to be improved for reliable real-time deployment of the robotic systems."
- Sec. VI.C: "the question of whether a single multimodal model can accommodate all modalities remains an open challenge."
- Sec. VI.D: "Bayesian techniques (e.g., Gaussian processes or Bayesian ensembles) do not necessarily produce estimates of uncertainty that are calibrated in this Frequentist sense".
- Sec. VI.E.1: "Developing ways to perform red-teaming (both by humans and in a partially automated way) for foundation models in robotics is an exciting direction for future research."
- Sec. VI.E.2: "Developing techniques that perform runtime monitoring and OOD detection with statistical guarantees on false positive/negative error rates in a data-efficient manner remains an important research direction."
- Sec. VI.H: "A combination of open hardware, benchmarking in physics-based simulators, and promoting transparency in experimental and simulation setups can significantly alleviate the challenges associated with reproducibility".

## What it does NOT cover
- Dexterous hands, multi-fingered control, in-hand manipulation: absent (one adjective, Sec. III.E).
- Tactile sensing: absent (0 occurrences).
- Bimanual: absent (0 occurrences).
- Sim-to-real for control: "sim-to-real" appears twice (an aside in Sec. III.A.2; Sec. VI.H); no DR/DA treatment (defer to zhao_sim2real_survey_2020).
- Contact physics: named only as what the listed simulators neglect (Sec. VI.H); no engine comparison, no penetration or contact-fidelity discussion.
- Evaluation protocol for policies: none; benchmarking appears only as a reproducibility problem.
- Low-level RL, reward design, teleoperation, retargeting: outside scope.

## Quotable claims (verbatim, with section)
- Sec. I: "Another survey on foundation models in robotics appeared simultaneously with ours on arXiv [20]. In comparison with that paper, ours emphasizes future challenges and opportunities, including safety and risk".
- Sec. VI.H: "many recent works have relied on non-physics-based simulators (e.g., ignoring or greatly simplifying contact physics in gasping)" [sic].
- Sec. VI.G: "robotic solutions are usually tailored to specific robot platforms with specific layouts, environments, and objects for specific tasks. These solutions are not generalizable across various embodiments, environments, or tasks."

## Notes for the survey
- Feeds: the "what we do not re-cover" paragraph (VLAs, LLM planners, open-vocabulary perception); Sec. VI.H as an independent voice saying FM-era benchmarks skip contact physics.
- Positioning: orthogonal to a hand-focused survey: zero overlap on hands, touch, bimanual, or contact.
- Converter dropped the Sec. II.B and Sec. III.A markdown headings (content is present around lines 280–347) and the "A.", "B.", "F.", "G." headings in Sec. VI. Cite by section letter from the text, not from a "^#" grep.
