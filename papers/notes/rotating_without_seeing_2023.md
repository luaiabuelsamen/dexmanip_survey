# rotating_without_seeing_2023 — Rotating without Seeing: Towards In-hand Dexterity through Touch (Yin, Huang, Qin, Chen, Wang, RSS 2023, arXiv 2303.10880)

sources: papers/md/rotating_without_seeing_2023.md [sha256 7be48b3f] ; no code

## One-line contribution
Touch-only in-hand rotation: 16 binary (touch/no-touch) FSR contact sensors spread over an Allegro hand (palm, links, fingertips), no vision, trained with PPO in IsaacGym and deployed zero-shot to a real XArm+Allegro hand, generalizing to unseen real objects (Table I: e.g. Ours 4.91±0.52 rounds / 30.00±0.00 s TTF on seen Object C1 vs. best baseline CT-Sensor 2.50±3.25 / 20.00±8.66).

## Setting
- hand(s): Allegro Hand, "16-DOF Allegro Hand" (Sec III.A); vendor not stated. Real setup also has "16 contact sensors" (FSR, ~$12 each) on palm and finger links/tips (Sec III.A, Fig. 1 left).
- arm: real hardware = "XArm robot arm" rigidly carrying the Allegro hand (Sec III.A) — explicit. Simulation: arm not mentioned anywhere in Sec III.B; whether the hand base is fixed or arm-mounted in sim is not stated.
- palm-up or palm-down: not stated. Paper only says the object is "initialized in the palm" and resets trigger when the object "deviates too much from its initial position (i.e., the center of the palm)" (Sec IV.A.4); no statement of palm orientation relative to gravity.
- single/bimanual: single hand.
- simulator / physics: IsaacGym [38]; physics engine (PhysX) not named in the text; no simulator version number given. #envs: 8192 parallel environments (Sec IV.C).
- sim timestep / control rate: dt = 0.01667 s with 2 simulation substeps (Sec IV.C); action executed for 6 sim steps, giving a 10 Hz control frequency, "both in the simulation and the real" (Sec IV.A.2, Sec IV.C).
- GPU / wall-clock training time: not stated.
- observation: state s_t = joint position q_t ∈ R^16, binary sensor observation o_t ∈ {0,1}^16, previous position target q̃_t ∈ R^16, rotation axis k ∈ S^2; stacked with 3 historical states (4 steps total) for the MLP policy (Sec IV.A.1). Value network gets extra privileged input: "contact force over each link, the object's ground-truth pose, and physical parameters" (Sec IV.C, asymmetric actor-critic).
- action space: relative joint position command a_t ∈ R^16; PD-controller target updated as q̃_{t+1} = q̃_t + ã_t with EMA smoothing ã_t = η a_t + (1-η) ã_{t-1}, η = 0.8 (Sec IV.A.2). PD controller runs at 10 Hz in sim and real.
- objects / data: sim training uses "artificial objects of common geometries" — cuboids, cylinders, balls; Object Set A = "Irregular cubes", Object Set B = "Irregular cylinders, Large aspect-ratio objects" (Fig. 5). Real eval: Object Set C, 10 objects total — 5 "seen" (C1–C5, artificial training-like shapes) and 5 "unseen" (Tomato, Apple, Orange, Soupcan, Rubber Duck) (Table I). Shape-understanding ablation (Sec V.H) uses 125 irregular column-shaped objects and 55,000 policy rollouts of 200 control steps (20 s) each, split train/test by object.

## Method
- paradigm: model-free RL, single stage (no teacher-student / privileged-to-vision distillation — the same policy that is trained is deployed directly; only the value network sees privileged information, per the asymmetric actor-critic of [28]).
- algorithm: PPO [58]. Policy and value nets are MLPs with ELU activation; policy hidden layers [512, 256, 256], value hidden layers [512, 512, 256, 256] (Appendix B). Policy LR 1e-4 with adaptive KL threshold 0.02; value LR 5e-4 with adaptive KL threshold 0.016; advantage clip ε = 0.2; horizon length 16; γ = 0.99; GAE τ = 0.95; gradient-norm clip 1.0; minibatch size 16384 (Sec IV.C, Appendix B). Policy outputs a Gaussian with learnable state-independent std.
- teacher-student / distillation: none — see paradigm above; "privileged information is not accessible by the policy network" (Sec IV.C).
- domain randomization (Table VI, verbatim ranges):
  - Object: Mass (kg) [0.2, 0.6]; Friction [0.3, 3.0]; Shape ×U(0.95, 1.05); Initial Position (cm) +U(−0.015, 0.015).
  - Hand: Friction [0.3, 3.0].
  - PD Controller: P Gain ×U(0.66, 1.33); D Gain ×U(0.80, 1.20).
  - Sensor: Lag Probability 0.25; Drop Rate 0.1.
  - Random Force: Scale 0.2; Probability [0.2, 0.25]; Decay Coeff. and Interval 0.99 every 0.1 s.
  - Joint Observation Noise +U(−0.05, 0.05); Action Noise +U(−0.06, 0.06).
  - Prose (Sec IV.B) matches: sensor drop is "for each activated contact sensor that outputs 1, with probability p we flip its output to 0" (= Drop Rate row); signal delay modeled "by an exponential delay used in [28]" (= Lag Probability row); white noise injected into observation and action (= the two noise rows).

## Reward / objective block (C) — quoted verbatim, Sec IV.A.3 + Appendix D
Overall (Eq. 1 body / Eq. 9 appendix, identical):
r_t = w1 r_rot + w2 r_vel + w3 r_fall + w4 r_work + w5 r_torque + w6 r_dist
Weights (Appendix, Eq. 9): w1 = 20.0, w2 = 0.1, w3 = 1.0, w4 = 0.0003, w5 = 0.0003, w6 = 0.1.
- r_rot: "the rotated angle Δθ of a sampled unit vector in the normal plane Π of the rotation axis k" — sample unit vector v in Π, project its next-state vector v′ onto Π to get v′_p, "Δθ ∈ [−π, π) is defined as the signed distance between v′_p and v with respect to the axis k" (Fig. 4). Paper notes prior work [51] instead uses ⟨ω, k⟩ (simulator angular velocity dotted with axis) but found simulator angular velocity "very noisy" and liable to produce "vibrating around a specific pose"; the finite-difference angle was found more consistent across runs.
- r_vel = "−∥v_t∥", a penalty on the object's velocity, to "encourage[s] the hand to rotate the object in a stable manner and increase[s] the transferability of the trained policy."
- r_fall: "a negative falling penalty when the object falls out of the palm" — exact functional form recovered by OCR: "rfall = −50.0" (Eq. 5, Appendix D, "Falling Reward (Penalty)") (recovered by OCR from papers/md/rotating_without_seeing_2023.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect) — a flat constant penalty (not a function of any state variable), previously rendered as an unparsed figure/image in the source markdown.
- r_work = "−⟨|τ|, |q̇_t|⟩", where τ is the PD controller's output torque at step t; "helps to improve the smoothness of finger motion."
- r_torque = "−∥τ∥", penalizing large torque. Its "Torque Reward (Penalty)" appendix box, previously an unextracted image, is recovered by OCR: "rtorque = −∥τ∥" (Eq. 7) (recovered by OCR from papers/md/rotating_without_seeing_2023.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect) — matches the prose form exactly.
- r_dist: body text gives the general form "mean(clip(1/(ϵ + d(x_tip, x_obj)), c2, c3))"; Appendix Eq. 8 gives the concrete instantiation: r_dist = mean_{i=0,1,2,3}(clip(0.1/(0.02 + 4 d(x^i_tip, x_obj)), 0, 1)) — "encourages the fingertip to come close to the object and interact with it."
- The appendix "Rotation Reward" and "Velocity Reward" sub-headings (Appendix D), previously present with no extractable formula text (image only), are now recovered by OCR: "rrot = clip(∆θ, −0.157, 0.157)" (Eq. 3) and "rvel = −∥vt∥" (Eq. 4) (recovered by OCR from papers/md/rotating_without_seeing_2023.ocr.md; OCR text is noisier than the layout parse, symbols may be imperfect) — both match the prose definitions from Sec IV.A.3 exactly (the numeric clip bound ±0.157 rad is new information not previously quoted verbatim from the appendix). The appendix "Distance Reward" (Eq. 8) also matches the Sec IV.A.3-derived instantiation already quoted below.
- Reset strategy (not a reward term): episode resets if the object "deviates too much from its initial position" or if "the major axis of the object deviates too much from the rotation axis" — no numeric thresholds given (Sec IV.A.4).

## Contact / penetration handling (D)
Not addressed as interpenetration. Contact is only used to build the binary touch signal: the simulator's net contact force F = [Fx, Fy, Fz] on each fixed sensor link is fetched each step, its norm ∥F∥ is thresholded at θ̃_th = 0.01 N in simulation (Sec III.B) to produce the binary o_t; the real hardware binarizes analog FSR voltage at a threshold θ_th whose default numeric value is not given (only the LS-Sensor ablation's raised threshold, θ_th = 0.2 N, is stated, Sec V.B). No penetration penalty, no contact-solver iteration counts, no contact-offset values are given anywhere in the source.

## Evaluation block (E)
- metrics (Sec V.A.2, exact definitions quoted): "Cumulative Rotation Reward (CRR)" — cumulative rotation reward, sim only; "Cumulative Rotation Angle (CRA)" — cumulative rotation angle "by rounds," real only, "counted by a human"; "Time-to-Fall (TTF/Duration)" — "the time (by seconds) of an object staying in the palm before falling down the hand," used in both sim and real.
- success criterion: not stated as a discrete threshold — all three metrics above are continuous/count measures, no pass/fail cutoff (e.g. in radians or metres) is given.
- eval episodes/seeds: sim tables (II, III, V) are "averaged on 3 seeds" with no per-seed episode count given. Real Table I: "results are averaged on 3 policies trained on 3 seeds. Each trial lasts 30 seconds," over 10 objects (5 seen + 5 unseen).
- headline numbers: Table I (real, multi-object rotation, 30 s/trial) — Ours vs. best baseline on seen Object C1: CRA 4.91±0.52 vs. CT-Sensor 2.50±3.25; TTF 30.00±0.00 vs. CT-Sensor 20.00±8.66. On unseen Apple: Ours CRA 2.67±1.04 / TTF 30.00±0.00 vs. CT-Sensor 0.42±0.52 / 15.33±15.01. Table II (sim, single-object, physics-shift robustness): Sensor 963.8±377.8 CRR / 42.2±4.1 TTF (seen physics) vs. 919.3±338.0 / 40.0±4.3 (unseen physics), vs. No-Sensor 689.3±141.5→369.0±129.1 CRR (large drop). Table III (sim, multi-object generalization): Sensor 976.1±86.5 CRR (seen objects) vs. DS-Sensor 351.5±28.0; unseen objects Sensor 594.4±63.2 vs. DS-Sensor 186.5±16.1. Table V (rotation about other axes, sim): z-axis best, seen CRR 3.43±1.22/TTF 29.06±1.45; x- and y-axis weaker, attributed to the sensor layout not covering side-of-finger-link contacts needed for those axes (Sec V.I). Shape-reconstruction ablation (Sec V.H): MSE 0.22 (with touch) vs. 0.45 (touch zeroed out).
- baselines: No-Sensor (no tactile obs), LS-Sensor (higher threshold θ_th = 0.2 N), DS-Sensor (tactile disabled only at eval time), Openloop (replays sim trajectories on the real robot), CT-Sensor (continuous, non-binarized sensor values). All are the authors' own trained ablation baselines, not numbers quoted from other papers.
- real robot: XArm + 16-DOF Allegro hand, 10 objects (Object Set C), 3 seeds per method per object, 30 s per trial (Table I caption).

## Reproducibility (F)
Code released: not stated — no code/model/checkpoint repository is mentioned anywhere in the source; the only released artifact referenced is a project-page video demo (http://touchdexterity.github.io) and "the raw video demo ... in the submitted files" (Appendix A). No code/md source exists for this paper in this survey's corpus, so no table here can be cross-checked against an implementation.

## Limitations stated by the authors
- Rotation around x and y axes is weaker than z (Table V) because it "involves many critical contacts between the object and the side of finger links," which "the layout of our current sensor array does not support"; the authors hypothesize "a denser contact sensor array over each finger link can remedy this problem" (Sec V.I).
- The system's sensing is explicitly framed as "sparser than that of a real human hand" (Sec III.D).
- CT-Sensor (continuous, non-binarized signal) "has poor generalizability and huge variance between different objects," attributed to "the huge gap in force measurement between simulation and the real world" (Sec V.E) — a limitation of the non-binary alternative, not of the main method, but bears on the touch-only design choice.
- Conclusion lists future work rather than resolved gaps: "exploring the use of a more dense contact sensor array and scaling up the system to solve more diverse tasks" (Sec VI).

## Quotable claims (verbatim, with section)
- "we introduce a new system design using dense binary force sensors (touch or no touch) overlaying one side of the whole robot hand (palm, finger links, fingertips). Such a design is low-cost, giving a larger coverage of the object, and minimizing the Sim2Real gap at the same time." (Abstract)
- "while one single binary force sensor cannot do much, the combination of 16 of them has a strong representation power (2^16 types of states in maximum), which might allow the robot hand to "feel" the object state without seeing." (Sec I)
- "We binarize these measurements with respect to a selected threshold θth ... The advantage of using binary signals is that it can reduce the gap between the simulation and the real robot, and simplify the Sim2Real transfer procedure." (Sec III.A)
- "We observe that both the no-sensor and the open-loop policy can at most rotate the object for 180 degrees on the evaluated objects, after which they will get stuck or push the object off the palm, resulting in a failure." (Sec V.E)
- "by comparing the methods with continuous contact signals and binarized contact signals, we find that the latter has better performance." (Sec V.E)

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the survey's sensing-modality comparison (touch-only vs. vision-based in-hand reorientation, e.g. against DeXtreme/dextreme_2022, which uses vision pose estimation and a locked wrist with no tactile sensing) and the reward-shaping comparison table, since this reward (finite-difference rotation angle rather than angular-velocity dot product) is explicitly presented as a deliberate departure from a cited prior reward ("[51] uses ⟨ω, k⟩"). No penetration handling here to compare against penetration-penalty methods — flag as a method with contact used purely for sensing, never for a physical/interpenetration penalty. Embodiment fields (palm-up/down, sim arm-mounting, real threshold θ_th default value, r_fall exact formula) are genuinely silent in the source (not authoring gaps) — do not backfill these from other Allegro-hand papers when tabulating across notes.
