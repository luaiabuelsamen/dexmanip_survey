# gemini_robotics_2025 — Gemini Robotics: Bringing AI into the Physical World (Gemini Robotics Team, Google DeepMind, arXiv 2025)

sources: papers/md/gemini_robotics_2025.md [sha256 f2c1ab4e] ; no code

## One-line contribution
Two models on Gemini 2.0 — Gemini Robotics-ER (embodied-reasoning VLM: pointing, 3D detection, grasp/trajectory prediction) and Gemini Robotics (a VLA fine-tuned from it to emit robot action chunks) — plus the ERQA benchmark; evaluated on ALOHA 2 bimanual arms with parallel grippers, with preliminary fine-tuned adaptation to a bi-arm Franka (parallel grippers) and to the Apollo humanoid (five-fingered dexterous hands).

## Setting
- hand(s): ALOHA 2 arms use a parallel gripper, two fingers: "Each arm has a parallel gripper with two fingers" (Appendix B.3.2, line 973). Franka platform (§4.4) also "parallel grippers". Apollo/Apptronik (§4.4): "a full-size humanoid robot with five-fingered dexterous hands" — no DoF count or hand model given.
- arm: ALOHA 2 bimanual cell on a 0.8m x 0.4m table (Appendix B.3.1); bi-arm Franka (industrial); Apollo humanoid (full-size). single/bimanual: all three evaluated embodiments are bimanual/bi-arm.
- simulator / physics: not stated for Gemini Robotics training/eval (entirely real-robot, §3-4). A separate zero-/few-shot Gemini 2.0/-ER study (§2.3) uses an "ALOHA 2 Sim Task suite" (Table 5); engine, timestep, contact model not stated.
- observation: "a multimodal prompt consisting of a set of images of the current status of the scene and a text instruction of the task to perform" plus proprioception (Fig. 14: "...and proprioception {proprio}"). No itemized per-task observation vector given.
- action space: "outputs action chunks that are executed by the robot" (Fig. 14 caption); exact low-level representation (joint targets/pose/torque) not stated. The separate zero-shot robot API (Appendix B.3.2) moves "each gripper to a specified pose" and opens/closes grippers — that is the code-generation layer, not necessarily the trained VLA's representation.
- objects / data: "a large-scale teleoperated robot action dataset on a fleet of ALOHA 2 robots ... over 12 months, which consists of thousands of hours of real-world expert robot demonstrations" over "thousands of diverse tasks" (§3.1), plus "web documents, code, multi-modal content (image, audio, video), and embodied reasoning and visual question answering data." No exact hour/episode/object counts stated.

## Method
- paradigm: VLA fine-tune of Gemini for direct action-chunk prediction, on top of Gemini Robotics-ER; also a separate zero-/few-shot "code generation" + in-context-learning (ICL) control mode using Gemini 2.0/-ER directly (§2.3), no action fine-tuning.
- algorithm/implementation: no training-algorithm name given for Gemini Robotics itself (no PPO/diffusion-solver detail); described only architecturally (below). Baselines are explicit: π0 re-implement (diffusion-transformer action expert over PaliGemma) and a CLIP-conditioned multi-task diffusion policy (§C.2).
- distillation: "The Gemini Robotics backbone is formed by a distilled version of Gemini Robotics-ER" (§3.1) — i.e. -ER is distilled into the lower-latency VLA cloud backbone. Nothing is called "privileged information" anywhere.

### A. Embodiment block
- hand+DoF+vendor: ALOHA 2 parallel gripper (2-finger, no DoF/vendor spec beyond "ALOHA 2"); Franka parallel gripper (no spec); Apollo (Apptronik) "five-fingered dexterous hands" (no DoF given).
- arm/base: ALOHA 2 bimanual cell; industrial bi-arm Franka; Apollo full-size humanoid (floating base implied, not elaborated). bimanual: yes, all three.
- simulator+physics engine: not stated (real robot for the VLA; unnamed engine for the separate "ALOHA 2 Sim Task suite").
- timestep/control rate: sim timestep not stated; robot "effective control frequency is 50Hz" (§3.1), end-to-end latency "approximately 250ms", cloud backbone latency "under 160ms".
- parallel envs/GPU/wall-clock: not stated for Gemini Robotics. Underlying stack hardware: "TPU v4, v5p and v6e" with "JAX ... ML Pathways" (Table 7). Baseline compute: π0 re-implement "batch size of 2048 ... 300K steps" then "50K steps" fine-tune; multi-task diffusion "batch size of 512 ... 2M steps" then "1M steps" fine-tune (§C.2).

### B. Learning block
- paradigm: as above (VLA fine-tune / behavior-cloning in spirit; separate zero-/few-shot mode needs no action labels).
- backbone VLM: Gemini 2.0. Parameter count: not stated anywhere (Model Card Table 7, §3.1, §6 all silent).
- action head, quoted (§3.1 "Model"): "It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on the robot's onboard computer (Gemini Robotics decoder). The Gemini Robotics backbone is formed by a distilled version of Gemini Robotics-ER and its query-to-response latency has been optimized from seconds to under 160ms. The on-robot Gemini Robotics decoder compensates for the latency of the backbone. When the backbone and local decoder are combined, the end-to-end latency from raw observations to low-level action chunks is approximately 250ms. With multiple actions in the chunk (Zhao et al., 2023), the effective control frequency is 50Hz."
- action chunk length: not given numerically, only "multiple actions" per chunk. Control rate: 50Hz effective (as above).
- domain randomisation: not addressed for the real-robot VLA. The separate sim suite mentions only "random initial conditions" (Table 5 caption), no ranges for any quantity.

### C. Reward / objective block
Not stated. No loss function, reward term, or objective formula appears anywhere in the method text (§3.1, §4) — presented as fine-tuning on demonstrations, not an RL objective. Nothing to quote from paper or code (no code corpus for this entry). The reasoning-enhanced variant (§4.2) is described only architecturally: "The local action decoder from Section 3.1 is extended to convert these reasoning intermediates to continuous low-level actions" — again no loss given.
- key trick(s): (1) split cloud-backbone/on-device-decoder architecture for real-time control from a large VLM; (2) training mixture mixes robot action data with non-action multimodal/web/code/VQA data to preserve Gemini's reasoning; (3) reasoning-enhanced fine-tune (§4.2) re-labels the action dataset to bridge to embodied-reasoning trajectory prediction (§2.2).

## D. Contact / penetration handling
Not addressed. Nearly all evaluation is real hardware (contact is physical, not simulated/penalized); the one simulated study (Table 5) gives no contact-solver settings, penetration metric, or penalty term. The only "contact" mention in the document is forward-looking (§6): "we plan to lean more on simulation to generate visually diverse and contact rich data" — an intention, not a mechanism.

## Evaluation
### E. Evaluation block
- success criterion: binary — "Each evaluation is marked either success or failure (0 for failure, 1 for full completion)" (§C.1) — plus a continuous "progress score, between 0 and 1, reflecting the proportion of the task completed," defined per task by rubric (e.g. "Unzip the lunch bag completely": 1.0 fully unzipped, 0.5 partially unzipped after grasping zipper, 0.25 zipper tag grasped, 0.0 otherwise; §C.1.3.3). No metre/radian/second threshold anywhere — success is rubric-judged, not tolerance-based.
- trial counts: 20 tasks out-of-the-box (Fig. 16); 25 instructions over 5 scenes (§3.3); 85 tasks in the generalization suite (20% in-distribution / 28% visual / 28% instruction / 24% action, §3.4); 20 trials/task for §4.1 specialists (12 for spelling game); 50 trials/task for the separate ALOHA 2 sim suite (Table 5); 20 trials/task for the Franka in-distribution eval (Appendix D.4.2).
- sim vs real: real-robot for essentially all of §3-4 ("All empirical evidence presented in this section is based on rigorous real-world robot experiments", §3.1); Table 5 (sim) / Table 6 (real) belong to the separate Gemini 2.0/-ER zero-/few-shot study (§2.3), not the trained VLA.
- baselines: re-run on the same data mixture, not quoted from their papers — "Both baselines were trained to convergence using the same composition of our diverse data mixture" (§3.1); π0 re-implement is stated to outperform the publicly released π0 (openpi) checkpoint (§C.2, Fig. 41).
- headline numbers: out-of-the-box 20 tasks (Fig. 16, §3.2) — "proficient at half of the tasks out of the box with a success rate exceeding 80%" (per-task numbers only in the figure). Long-horizon specialists (§4.1, Fig. 23) — "2000 and 5000 episodes of high-quality demonstration data for each task", "average success rate of 79%", "100% success rate" on lunch-box packing ("over 2 minutes"), spelling game "4 out of 6 unseen hand-drawn sketches" correct; a from-scratch Gemini Robotics specialist scores "0% success rates across the board". Fast adaptation (§4.3, Fig. 26) — "For 7 out of 8 tasks, fine-tuning was effective at achieving success rate above 70% with at most 100 demonstrations ... for two tasks, Gemini Robotics achieves a 100% success rate." New-embodiment (§4.4): Franka, 4 tasks, 20 trials/task in-distribution — "average success rate of 63%"; Apollo — only a qualitative rollout (Fig. 27, "packs a lunch bag"), no success rate/trial count/table anywhere. Separate ER sim/real study (Tables 5-6, "average success rate over 50 trials with random initial conditions"): 2.0 Flash zero-shot avg. 27%, -ER zero-shot avg. 53%, 2.0 Flash ICL avg. 51%, -ER ICL avg. 65% (sim); real: zero-shot avg. 25%, ICL avg. 65% (Banana Handover/Fold Dress/Wiping).
- baselines beaten: π0 re-implement, multi-task diffusion, and (§4 only) single-task diffusion from scratch (§C.2); Gemini Robotics reported to beat all across §3.2-3.4, §4.1.
- real robot? Yes, trial counts as above; hand/gripper per embodiment as in Setting.

dexterous-hand-evaluated: yes and no — depends on embodiment. ALOHA 2 (all of §3, §4.1-4.3) and the Franka (§4.4, quantified 63%) both use parallel grippers, not dexterous hands: "Each arm has a parallel gripper with two fingers" (Appendix B.3.2, line 973) and "We consider a bi-arm Franka robot with parallel grippers and Apollo from Apptronik, a full-size humanoid robot with five-fingered dexterous hands" (§4.4, line 575). Apollo does carry a dexterous hand and is shown "packs a lunch bag" (Fig. 27 caption), but only qualitatively — no success rate, trial count, or table is reported for Apollo anywhere in the text.

## F. Reproducibility
- Code released? No — no repo for Gemini Robotics or -ER; confirmed no code/md/gemini_robotics_2025.md exists in this corpus.
- Checkpoints/assets released? No — not applicable, no code repo. The model card (Table 7) lists only architecture/inputs/outputs/training-data description, no access path.
- What the paper says was released: the ERQA benchmark ("An open-source benchmark ...", §1 item 1; details at github.com/embodiedreasoning/ERQA, §2.1); the ASIMOV safety datasets, "concurrent with this tech report, we develop and release the ASIMOV-datasets" (§5). No action dataset, policy weights, or eval suite for Gemini Robotics/-ER stated as released.
- Tables reproducible from code: not applicable — no code corpus for this entry.

## Limitations stated by the authors
§6: "Gemini 2.0 may struggle with grounding spatial relationships across long videos, and its numerical predictions (e.g., points and boxes) may not be precise enough for more fine-grained robot control tasks." Future work: "enhance Gemini Robotics's ability to handle complex scenarios requiring both multi-step reasoning and precise dexterous movements, particularly in novel situations"; "lean more on simulation to generate visually diverse and contact rich data"; "expand our multi-embodiment experiments, aiming to reduce the data needed to adapt to new robot types and ultimately achieve zero-shot cross-embodiment transfer." For -ER's zero-/few-shot mode (§2.3): "Gemini Robotics-ER is currently unable to perform dress folding, mostly due to its inability to generate precise enough grasps." New-embodiment work (§4.4) is explicitly framed as "preliminary experiments."

## Quotable claims (verbatim, with section)
- "Gemini Robotics is a derivative of Gemini fine-tuned to predict robot actions." (Fig. 14 caption, §3.1)
- "We consider a bi-arm Franka robot with parallel grippers and Apollo from Apptronik, a full-size humanoid robot with five-fingered dexterous hands." (§4.4)
- "when we directly train the Gemini Robotics specialist model from scratch using the specialization datasets, we find that it is unable to solve any of these tasks (0% success rates across the board, ...)" (§4.1)
- "ERQA ... An open-source benchmark specifically designed to evaluate embodied reasoning capabilities of multimodal models." (§1, item 1)

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the VLA/generalist-policy section as a frontier-VLM-backbone example, and the cross-embodiment-transfer section (ALOHA 2 -> Franka -> Apollo humanoid). Caveat for the dexterous-hand comparison table: unlike papers that train and quantitatively evaluate on a multi-fingered hand, Gemini Robotics' only dexterous-hand embodiment (Apollo) is shown qualitatively (one figure, one task) with zero reported trials or success rate — flag as "dexterous hand shown, not benchmarked," versus the ALOHA 2/Franka numbers, which are all parallel-gripper results. No reward function, loss, observation vector, domain-randomization list, or contact/penetration handling is specified anywhere, consistent with a systems-and-scale technical report rather than a methods paper — a real gap versus the academic RL/IL dexterous-manipulation papers in this corpus. No code/checkpoints/weights released; the only concrete released artifacts are the ERQA benchmark and the concurrently-released ASIMOV safety datasets (§5).
