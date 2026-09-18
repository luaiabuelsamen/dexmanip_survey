# openai_dexterity_2018 — Learning Dexterous In-Hand Manipulation (OpenAI et al., IJRR 2020 / arXiv 2018)

sources: papers/md/openai_dexterity_2018.md [sha256 da6ec44d] ; no code

## One-line contribution
A recurrent PPO policy with an asymmetric actor-critic, trained on a heavily domain-randomized MuJoCo simulation, transfers zero-shot to a physical 24-DoF Shadow Dexterous Hand for in-hand block/octagonal-prism reorientation, using either PhaseSpace tracking or a CNN pose estimator trained purely on synthetic images.

## Setting
- hand: ShadowRobot Dexterous Hand, EDC (EtherCAT-Dual-CAN) electric-motor version, 24 DoF, 40 Spectra tendons via 20 DC motors (20 agonist-antagonist pairs); 16 DoF independently controlled, 8 joints coupled into 4 pairs (App B.1).
- arm: hand only; wrist pitch is one of the hand's own joints (locked in one ablation, §6.1); no separate robot arm is described. The hand sits fixed inside a "cage" with 16 PhaseSpace cameras and 3 RGB cameras around it (Fig. 3, App B.2–B.3).
- palm orientation: not stated as "palm-up"/"palm-down" verbatim. The object is "place[d] ... onto the palm" (§2) and the policy exhibits "the controlled use of gravity" (§1) with dropping as a failure mode (§2, §6.1) — consistent with holding the object against gravity, but the source never uses the up/down terms, so treat as not explicitly stated.
- single/bimanual: single hand.
- simulator/physics: MuJoCo [64] for physics; Unity for rendering training images for the vision model (§2.2, §5.1). Hand model based on the OpenAI Gym robotics environments [49], "improved to match the physical system more closely through calibration" (App C.3, 264 calibrated parameters).
- sim timestep / control rate: 1 MuJoCo step = 8ms; 1 env step = 10 MuJoCo steps = 80ms (App C.1 "Timing"); high-level policy runs "roughly 12 Hz" / queries sensors "every 80ms" (§2.1, App B.4); low-level PD controller "roughly 1kHz" / "every 5ms" (App B.4).
- parallel workers/GPUs: default = "8 NVIDIA V100 GPUs + 6144 CPU cores" (Table 10), from "384 worker machines, each with 16 CPU cores" (§4.3). Scale ablation uses 1/8/16/32 GPUs with 768/6144/12288/24576 CPU cores (Fig. 10). No explicit "number of parallel environments" is given, only CPU core counts.
- wall-clock training time: fully randomized policy needs "about 100 years" of simulated experience, "corresponds to a wall-clock time of ... around ... 50 hours" on the default setup, vs "3 years"/"1.5 hours" with no randomization (§6.3).
- observation: PhaseSpace fingertip + object pose (state policy) or the vision CNN's pose estimate; explicitly excludes the hand's built-in tactile/Hall-effect sensors because they are "subject to state-dependent noise that would have been difficult to model" (§3.1).
- action space: 20-dim desired joint angles relative to the current position, discretized into "11 bins of equal size" per coordinate (§4.2, App C.1); categorical, not continuous ("we noticed that discrete action spaces work much better," §4.2).
- objects/data: block and octagonal prism (§2); no demonstration dataset — "does not rely on any human demonstrations" (Abstract).

## Method
- paradigm: model-free RL (PPO) with asymmetric actor-critic; separate supervised vision pose estimator.
- algorithm: "Proximal Policy Optimization (PPO) [57]" (§4.1); "the same distributed implementation of PPO that was used to train OpenAI Five [43] without any modifications" (§4.3), run on the "Rapid" infrastructure (worker pool → Redis → 8-GPU optimizer, Fig. 5).
- policy architecture: "recurrent neural network with memory, namely an LSTM ... with an additional hidden layer with ReLU activations inserted between inputs and the LSTM" (§4.1); dense hidden layer 1024, LSTM size 512 (Table 10, App D.1).
- asymmetric actor-critic (privileged value net, Table 2): value net additionally sees object orientation (4D quat), target orientation (4D quat), hand joint angles (24D), hand joint velocities (24D), object velocity (3D), object angular velocity (4D quat) — none given to the policy net. Policy net sees fingertip positions (15D), object position (3D), relative target orientation (4D quat). Footnote 4: current object orientation was "accidentally" left out of the policy inputs.
- reward (quoted verbatim, §4.2 / App C.1 "Rewards"): "The reward given at timestep t is r_t = d_t − d_t+1, where d_t and d_t+1 are the rotation angles between the desired and current object orientations before and after the transition, respectively. We give an additional reward of 5 whenever a goal is achieved with the tolerance of 0.4 rad (i.e. d_t+1 < 0.4) and a reward of −20 (penalty) whenever the object is dropped." No other terms are given anywhere in the source; no penetration/contact term.
- key tricks: domain randomization of physics, observation noise, unmodeled effects (backlash, action delay/noise, marker occlusion, random forces) and visual appearance (§3.2, App C.2); MuJoCo calibration to real trajectories via coordinate descent over "264 parameter values" (App C.3); action smoothing by exponential moving average, coefficient "0.3 per 80ms" (App C.1 fn.15); discretized action space (§4.2).

## Domain randomization (verbatim ranges — Tables 1, 7, 8, 9; App C.2)
- object dimensions: scaling factor uniform([0.95, 1.05]) (Table 1)
- object and robot link masses: scaling factor uniform([0.5, 1.5]) (Table 1)
- surface friction coefficients: scaling factor uniform([0.7, 1.3]) (Table 1)
- robot joint damping coefficients: scaling factor loguniform([0.3, 3.0]) (Table 1)
- actuator forcegains (P term): scaling factor loguniform([0.75, 1.5]) (Table 1)
- joint limits: additive N(0, 0.15) rad (Table 1)
- gravity vector (each coordinate): additive N(0, 0.4) m/s² (Table 1)
- observation noise (Table 7): fingertip positions 1mm correlated / 2mm uncorrelated; object position 5mm correlated / 1mm uncorrelated; object orientation 0.1 rad correlated / 0.1 rad uncorrelated; fingertip marker positions 3mm correlated; hand base marker position 1mm correlated.
- action noise (Table 8, % of action range): uncorrelated additive 5%, correlated additive 1.5%, uncorrelated multiplicative 1.5%.
- action delay: per actuator, delayed w.p. 0.5 by one env step ("approximately 80ms") (App C.2).
- PhaseSpace marker dropout: masked w.p. 0.2/second for 1 second (App C.2).
- timing randomization: Δt = 8ms + Exp(λ), λ sampled once per episode ~ Uniform([1250, 10000]) (App C.2).
- backlash: per-episode δ−1, δ+1 ~ Gaussian centered on calibrated values, std 0.1 (App C.2, full recurrence given).
- random forces on object: probability p ~ loguniform(0.1%, 10%) per episode; when applied, force ~ N(0, (1 m/s² × object mass)²) per coordinate per timestep, decaying at 0.99 per 80ms (App C.2).
- vision randomizations (Table 9): #cameras 3; camera position ±1.5mm; camera rotation 0–3° about a random axis; camera FOV ±1°; robot material metallic 5–25%; robot material glossiness 0–100%; object hue = calibrated ±1%; object saturation = calibrated ±15%; object value = calibrated ±15%; object metallic 5–15%; object glossiness 5–15%; #lights 4–6; light position uniform over upper half-sphere; light relative intensity 1–5; total light intensity 0–15 (Unity units); image contrast 50–150%; additive per-pixel Gaussian noise ±10%.

## Contact / penetration handling
Not addressed as a reward or reported metric. The reward (above) contains only the goal-distance shaping term, the +5 bonus, and the −20 drop penalty. MuJoCo is noted to use "rigid body contact models instead of deformable body contact models" (§2.2), flagged as a source of reality gap, but no interpenetration statistic is measured or penalized anywhere in the source.

## Evaluation
- goal/success criterion: "a new goal is generated after the current one has been achieved within a tolerance of 0.4 rad" (App C.1 "Goals"), i.e. d_t+1 < 0.4 rad.
- episode/trial termination: App C.1 "Timing" states training episodes end at 50 consecutive goals, current goal unmet within "8 seconds of simulated time," or a drop. §6.2 instead defines the quantitative-evaluation trials as ending at a drop, "a goal has not been achieved within 80 seconds," or 50 rotations. These two per-goal timeout numbers (8s vs 80s) differ in the source and are not reconciled there — reported here as given, not merged.
- trial counts: "100 trials in simulation and 10 trials per policy on the physical robot" (Table 3 caption).
- headline numbers (Table 3, mean±std / median consecutive successful rotations): Block (state) sim 43.4±13.8/50, physical 18.8±17.1/13; Block (state, locked wrist) sim 44.2±13.4/50, physical 26.4±13.4/28.5; Block (vision) sim 30.0±10.3/33, physical 15.2±14.3/11.5; Octagonal prism (state) sim 29.0±19.7/30, physical 7.8±7.8/5.
- randomization ablation (Table 4, physical robot, median): all randomizations 13; no randomizations 0; no observation noise 8.5; no physics randomizations 2; no unmodeled effects 2; vision + all randomizations 11.5; vision + no observation noise 3.5.
- memory ablation (Table 5, physical robot, median): LSTM policy/LSTM value 13; FF policy/LSTM value 3.5; FF policy/FF value 3. LSTM hidden state after 5s of interaction predicts block size (bigger/smaller than average) "in 80% of cases" (§6.4).
- vision pose-estimator error (Table 6): Unity-rendered 2.71°±1.62 rotation / 3.12mm±1.52 position; MuJoCo-rendered 3.23°±2.91 / 3.71mm±4.07; real images (992 samples) 5.01°±2.47 / 9.27mm±4.02.
- baselines beaten: none re-run quantitatively; §7 situates the work narratively against planning-based, tactile closed-loop, and on-robot RL approaches only.
- real robot: ShadowRobot Dexterous Hand; 10 trials per policy per condition (Tables 3–5); scored as consecutive-rotation counts, not a binary success rate.

## Limitations stated by the authors
- "the simulation is still a rough approximation of the physical setup": direct joint torque instead of tendon actuation, rigid-body instead of deformable contact (§2.2).
- sim-to-real gap persists across every condition: e.g. block median 50 (sim) vs 13 (physical, state) (§6.2).
- octagonal prism transfers worse than the block; "further tuning is necessary" (§6.2).
- sphere: "failed to achieve more than a few rotations in a row" (§6.2), attributed to lacking rolling-related randomization or sensitivity to unmodeled screw holes.
- top failure modes: dropping while rotating the wrist pitch joint down; getting "stuck because the edge of an object got caught in a screw hole (which we do not model)" (§6.1).
- hardware breakage was "one of the key challenges," forcing Table 3's rows to be collected "at different times" (§6.2).
- ablation curves use "only ... one seed per experiment" (Fig. 8 caption).

## Quotable claims (verbatim, with section)
- "The reward given at timestep t is r_t = d_t − d_t+1 ... We give an additional reward of 5 whenever a goal is achieved and a reward of −20 (a penalty) whenever the object is dropped." (§4.2)
- "we noticed that discrete action spaces work much better." (§4.2)
- "This setup allows us to generate about 2 years of simulated experience per hour." (§4.3)
- "training with all randomizations leads to a median of 13 consecutive goals achieved, while policies trained with no randomizations, no physics randomizations, and no unmodeled effects achieve only median of 0, 2, and 2 consecutive goals, respectively." (§6.3)
- "we discovered that the LSTM hidden state after 5 seconds of simulated interaction with the block allows to predict whether the block is bigger or smaller than average in 80% of cases." (§6.4)

## Reproducibility
code/md/openai_dexterity_2018.md does not exist in this corpus — no code source for this note. Nothing in the read sections points to a released repository, checkpoints, or asset files. Table reproducibility from code cannot be assessed here; every number above is paper-only.

## Notes for the survey
Feeds: the domain-randomization comparison table (Tables 1/7/8/9 are the canonical DR-range reference for this era); the reward-shaping comparison (dense rotation-angle delta + sparse goal/drop bonuses, no penetration term, contrast with methods in D that do penalize penetration); the embodiment comparison (single Shadow Hand, 24 DoF, no arm, object resting on the palm). Flag for the survey: two different per-goal timeout values appear in the source itself (8s, App C.1, vs 80s, §6.2) — do not silently collapse them when citing "episode length" elsewhere. Flag: the combined vision+policy system is only evaluated end-to-end via Table 3 trial counts; the vision model alone is only scored on pose error (Table 6), not as an isolated RL ablation.
