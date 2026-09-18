# dexterous_handover_2025 — Learning Dexterous Object Handover (Frau-Alfaro et al., RO-MAN 2025)

sources: papers/md/dexterous_handover_2025.md [sha fa87ed53] ; code/md/dexterous_handover_2025.md — no code (file absent; `ls code/md/dexterous_handover_2025.md` returns "No such file or directory")

## One-line contribution
A single PPO policy trains only the *receiving* arm+hand (Kinova GEN3 + Allegro) to approach, grasp and carry an object away from a fixed, unlearned "giver" arm (UR5e + Allegro), using a phase-switched reward whose orientation term is built from dual-quaternion pose distance instead of Euler angles or rotation matrices (Abstract; Sec. IV).

## Setting
- hand(s): Allegro Hand (4-finger) on both arms, "equipped with Allegro Hands and touch sensors" (Sec. IV-A). DoF of the hand itself not stated numerically.
- arm: receiver = Kinova GEN3 (7 DoF); giver = UR5e (6 DoF) (Sec. IV-A). Bimanual setup, but see "B. Learning" below — only one arm is controlled by the learned policy.
- simulator / physics: IsaacLab [18] simulator; PPO via Stable Baselines3 (SB3) [19]; "1024 environments on a single NVIDIA A40 GPU" (Sec. V-A). Timestep/control rate: not stated.
- observation: per Fig. 2 caption — "Object Pose: Euclidean Translation (size: 3) + Euler (size: 3)"; "Hand Pose: Euclidean Translation (size: 3) + Euler (size: 3)"; "Hand Joint Avg. size: 3" (three global joint values, one per finger group average).
- action space: per Fig. 2 caption — "Incremental Action: Cartesian (size: 6) + Hand Joint Avg. (size: 3)"; i.e. pose increments to the GEN3 end-effector plus three joint-average increments for the hand (Sec. IV-A, Fig. 2).
- objects / data: no dataset — training uses one synthetic object, "an elongated quadrangular prism ... (0.035×0.035×0.45) m" (Sec. V-B). Test objects (out of training distribution): short prism (0.035×0.035×0.35 m), cylinder (r=0.019 m, length 0.45 m), short cylinder (r=0.019 m, length 0.35 m) (Sec. V-C).

## Method
- paradigm: RL (single-agent).
- algorithm: "Proximal Policy Optimization (PPO) [20] with three different seeds" (Sec. V-A), implemented via Stable Baselines3.
- reward: phase-switched, quoted below (block C). Note: the PDF-to-markdown conversion did not extract the actual numbered equations (3)–(12) as text (they render as images in the source PDF); only the surrounding prose describing each term survived in `papers/md/dexterous_handover_2025.md`, so exact algebraic weights beyond the two named constants (α, η₀) below are "not stated" in the parsed text.
- key trick(s): dual-quaternion pose-distance reward term (from prior work [7]) compared head-to-head against Euler-angle and homogeneous-matrix distance formulations within the same phase-reward structure (Sec. IV-C, V-B–D).

## Task decomposition into phases (for the handover comparison)
Fig. 1 shows the pipeline as "Maneuver → Approach → Handover" states with per-phase (s_t, a_t, r_t); the reward section (Sec. IV-B) further splits this into four named stages:
1. **Maneuver phase** — reward restricted so the GEN3 end-effector moves closer to the object than to the UR5e, and a "double frame system" pushes the GEN3 palm toward a correct approach zone (Sec. IV-B.1, condition (4)/modifier `m_MAN_t`).
2. **Approach phase** — extends the maneuver modifier to additionally require the distance at step t to be lower than at t−1 (Sec. IV-B.2, eq. (5)).
3. **Handover phase** — boolean contact-sensor vector `c⃗` (weighted by `w⃗_c`, "the lower phalanges are of greater importance than the tips") modifies the reward weight η_t from base η₀ = 1, and the weighted contact sum `c⃗·w⃗_c` is added to `r_BASE_t`, "when the agent touches the object, the reward encourages it to close the hand rather than to continue advancing towards the target" (Sec. IV-B.3, eq. (6)).
4. **Manipulation phase** — triggered "when the thumb and another finger of the GEN3 hand touch the object"; the UR5e hand opens and the reward switches to minimizing distance `d_TGT` to the GEN3's own starting pose, weighted by "α = 12 ... the weight for the manipulation phase," plus a bonus "when the agent changes to this phase or reaches the target" (Sec. IV-B.4, eq. (7)).

## A. Embodiment
- receiver arm+hand: Kinova GEN3 (7 DoF) + Allegro Hand + touch sensors (learned); giver arm+hand: UR5e (6 DoF) + Allegro Hand (fixed, not learned) (Sec. IV-A).
- bimanual: yes in scene, but single-agent control (see B).
- simulator: IsaacLab [18]; RL library: Stable Baselines3 [19]; algorithm PPO [20].
- sim timestep / control rate: not stated.
- parallel envs: 1024 (Sec. V-A). GPU: single NVIDIA A40 (Sec. V-A). Wall-clock training time: not stated. Number of seeds: three (Sec. V-A).

## B. Learning
- paradigm: single-agent, on-policy RL (PPO). No demonstrations, no distillation.
- **Joint vs. separate control of the two hands: the two hands are NOT trained jointly.** Only the GEN3 (receiver) is controlled by the learned policy. The UR5e (giver) is scripted/fixed: "We assume that the robotic hand holding the object is already fixed in an arbitrary handover pose... our objective is to train a single RL policy so that a robotic arm and hand can learn how to approach, grasp, and transport the object from another robotic system" (Sec. I); "The UR5e robot holds the object without moving during the whole episode... This way, it mimics a human giver which should not be trained. Then, the GEN3 has to learn to reach the object and grasp it" (Sec. IV-A). The paper explicitly contrasts this with a multi-agent alternative in related work: "[10] ... proposed a multiagent approach and a three-phase training, while our policy comprises a single agent and trains on a single-phase process" (Sec. II) — meaning even the phase structure is handled by the reward switching inside one policy, not by separate agents/policies per phase or per hand. The Conclusions list as future work: "training not only the receiving robot, but also the handing robot within the RL framework used" (Sec. VI) — confirming the giver is untrained in this paper.
- teacher-student / distillation: none stated.
- observation vector: Cartesian pose (translation+Euler) of GEN3, Cartesian pose (translation+Euler) of object, and three hand-joint-average values (Fig. 2 caption, Sec. IV-A). No vision: "the proposed policy does not incorporate any kind of visual perception; it is only extracting the object pose from the simulator" (Sec. VI, Limitations).
- action space: incremental — "increments in translation and Euler rotation as actions for the GEN3 end effector, and the three corresponding increment joint values for the hand" (Fig. 2 caption; Sec. IV-A: "we add increments to the current pose of the GEN3 end effector and to the joint values of the hand").
- domain randomisation: "we randomly reset the object position inside a cube of ±0.15 m of side, as well as the orientation with a variation of ±0.3 rad in roll and yaw, and ±0.6 rad in pitch" (Sec. V-A). The UR5e start pose is also "chosen randomly" each episode (Sec. IV-A). No randomisation of object mass/friction/visuals is stated.

## C. Reward / objective (quoted; paper-only — no code available for this key)
- Base term: "_r_ BASE _t_ is a basic reward for approaching the object, _dt_ is the distance between the pose of the hand and the object at step _t_ and _ηt_ is the weight of the reward at step _t_" (Sec. IV-B, describing eq. (3)).
- Maneuver-phase gating: reward restricted "to take the GEN3's end effector closer to the object than to the UR5e," using a "double frame system for the agent to maneuver into a suitable position for manipulation, with the GEN3 palm toward the target" and a modifier "_m_ MAN _t_ ∈ {0, 1}" (Sec. IV-B.1).
- Approach-phase gating: "the action taken at _t_ must bring the agent closer than it was at step _t − 1_," with "(_dt_ < _dt−1_) ∈ {0, 1} and _mt_ ∈ {−1, 1}" (Sec. IV-B.2).
- Handover-phase (contact) term: "We define the contacts as a vector of Boolean values _c⃗_ and we weight them using _w⃗_c_ according to their relevance in the task; the lower phalanges are of greater importance than the tips... In (6) we modify the original weight _η0 = 1_ according to the contacts. Therefore, the more touches, the lower that value will be... we add the weighed sum of contacts _c⃗ · w⃗_c_ to the reward _r_ BASE _t_. Thus, when the agent touches the object, the reward encourages it to close the hand rather than to continue advancing towards the target" (Sec. IV-B.3).
- Manipulation-phase term: "the reward also changes to take into account the distance between the object and the starting pose of the GEN3 _d_ TGT... where _α = 12_ is the weight for the manipulation phase. Moreover, when the agent changes to this phase or reaches the target, it receives a bonus" (Sec. IV-B.4).
- Dual-quaternion orientation-distance term (the reward compared against Euler/matrix): "we calculate the distance between frames using dual quaternions using (9)... In this work, we propose this reward function to perform the object handover task" (Sec. IV-C.1), where the distance is "_||·||2_ of all elements of _q̂_ diff − Î_" (Sec. IV-C.1), i.e. the second norm of the dual-quaternion difference from identity. The Euler-based alternative uses scaling factors "_ψ = 2.1_ and _µ = 0.32_ ... so the magnitude of the distance in translation and rotation is similar due to differences in units" (Sec. IV-C.2); the matrix-based alternative uses "_ψ = 2.1_ and _β = 0.32_" analogously (Sec. IV-C.3).
- There is only one reward function per agent overall — no separate "giving hand" reward, because the UR5e is not trained and receives no reward (consistent with B above). The abstract's framing — "a novel reward function based on dual quaternions to minimize the rotation distance" — is this single receiver-side reward.
- Actual numeric equations (3)–(12) are not present as extracted text in `papers/md/dexterous_handover_2025.md` (image-only in the source PDF); only the prose above, plus the two named constants α = 12 and η₀ = 1, survived conversion.

## D. Contact / penetration handling
Not addressed as a penalty term. Contact is used only positively, as a boolean per-phalange touch signal driving the handover-phase reward (Sec. IV-B.3, quoted above), via "tactile sensors on the phalanges of the fingers and the palm of the GEN3 hand" (Sec. IV-B.3, Fig. 4). Interpenetration/clipping is tracked only as a post-hoc evaluation category, not penalized during training: "**Indetermination** (Ind.): indicates that, although the robot manipulated the object correctly, there are bugs during the episode because of failures of the simulator to resolve collisions" — specifically "the object clip[ping] through the UR5e hand, snatching the object out of its hand instead of grasping and taking it with subtlety" (Sec. V-C). The authors flag this as a limitation: "imperfections in the physics engine limit the training of the policy by enabling undesired grasping behaviors that may not occur in the real-world setup" (Sec. VI).

## E. Evaluation
- **Handover-moment detection**: contact-based, via the boolean touch-sensor vector; the manipulation phase (object "susceptible to be grasped," UR5e hand opens) begins "when the thumb and another finger of the GEN3 hand touch the object" (Sec. IV-B.4) — a fingers-in-contact rule, not a force or distance threshold and not a learned classifier.
- **Success criterion** (quoted, Sec. V-C, illustrated in Fig. 6): "**Success** (Succ.): the robot grasped and manipulated the object correctly." "**Indetermination** (Ind.): indicates that, although the robot manipulated the object correctly, there are bugs during the episode because of failures of the simulator to resolve collisions. Therefore, in a real environment, we would not consider the grasp an absolute success." "**Total Success** (Total Succ.): the combination of indetermination and success cases." "**Fail**: indicates object falling during the episode."
- Eval episodes: 100 per condition ("The results in Table II show the performance for a total of 100 episodes in each case," Sec. V-C); Table III (novel objects) and Table IV (perturbation) are described as using the same evaluation protocol (counts not restated per-object beyond "100 episodes in each case").
- Sim vs. real: **sim only**. No real-robot trials appear anywhere in the source markdown; the Conclusions list "transfer the policy to real-world scenarios" as future work (Sec. VI). So "real-robot success rate: not stated / not run in this paper."
- Headline sim numbers:
  - Training object (elongated prism), N=100 (Table II): DQ agent — Succ. 59%, Ind. 32%, **Total Succ. 91%**, Fail 9%. EULER agent — Succ. 17%, Ind. 66%, Total Succ. 83%, Fail 17%.
  - Novel/out-of-distribution objects, N=100 each (Table III): short prism — DQ Total Succ. **94%** (Succ. 69, Ind. 25, Fail 6), EULER 92% (Succ. 32, Ind. 60, Fail 8). Cylinder — DQ 87% (Fail 13), EULER 84% (Fail 16). Short cylinder — DQ 90% (Fail 10), EULER 86% (Fail 14).
  - **On the bib's "94% success on novel objects" claim**: verified against Table III / Sec. V-C text — the 94% is the DQ agent's **Total Success** (success + indetermination), **in simulation only**, on the **short prism**, which the paper classifies as an object "out of the training distribution" (the training object was the longer prism); it is not a plain "success" rate and not real-robot. The abstract's "total success rate of 94% in the best-case scenario after 100 experiments" (Abstract) matches this same DQ/short-prism/Table III figure.
  - Under motion perturbation of the giver, N=100 per object (Table IV): DQ prism/short-prism 81% each; cylinder 71% (EULER 77% there, the one object where EULER beats DQ); short cylinder 65% (DQ) vs. 72% (EULER, best there). "All the total success rates decreased around 13.68% on average" (Sec. V-E), matching the abstract's "13.8%."
- baselines beaten: an internal ablation — DQ agent vs. EULER-angle agent vs. homogeneous-matrix agent (MATRIX "collapsed with a constant reward near zero" and was dropped from further evaluation, Sec. V-B). No external baseline method is re-run; related work numbers from other papers (e.g., "[4] ... 94% ... in the simulated environment" with grippers, Sec. II) are quoted, not reproduced.
- real robot: none (see above).

## F. Reproducibility
Abstract states "Code and videos can be found here," but no URL is present in the parsed text (`papers/md/dexterous_handover_2025.md` — link target not captured by the PDF→markdown conversion), and there is no `code/md/dexterous_handover_2025.md` for this key (confirmed via `ls`, file absent), and the bib entry's `github` field is null. So: code/checkpoints/assets availability — not verifiable from available sources; nothing in this corpus can be used to reproduce any of the paper's tables.

## Limitations stated by the authors (Sec. VI)
- "a single object is employed for the training process, thereby diminishing the generalization capabilities of the policy."
- "the proposed policy does not incorporate any kind of visual perception; it is only extracting the object pose from the simulator... important to transfer the trained policy from simulation to the real-world setup."
- "imperfections in the physics engine limit the training of the policy by enabling undesired grasping behaviors that may not occur in the real-world setup."
- Future work: train the handing (giving) robot too, generalize to more objects, and transfer to real hardware with noisy sensing and human givers.

## Quotable claims (verbatim, with section)
- "we discard the use of teleoperation systems to teach robots how to perform the task" (Sec. I).
- "our policy comprises a single agent and trains on a single-phase process, thereby reducing the number of hyperparameters to tune" — contrasted with a cited multi-agent, three-phase approach (Sec. II).
- "This stage is changed when the thumb and another finger of the GEN3 hand touch the object. At this point, we consider the object susceptible to be grasped, so the UR5e hand opens" (Sec. IV-B.4).
- "The DQ agent minimized the rotational poses from the starting pose around 43% on average. Far from reducing it, the EULER one increased it" (Sec. V-D).

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the hand-to-hand transfer / in-hand handover comparison table, but with a key caveat to flag against any two-hand co-trained baseline: this paper is **not** a two-hand joint-policy handover method — it is a single-hand receiving policy against a scripted, unmoving giver, explicitly deferring joint giver+receiver training to future work (Sec. VI). The "94% novel-object success" headline number must be reported as DQ/short-prism/Total-Success/sim-only/N=100 (Table III), not as a generic novel-object success rate, and not as a real-robot number — there are no real-robot results in this paper. No interpenetration penalty or explicit contact-force/distance handover trigger exists here (contrast with any survey entries that use force thresholds or learned handover classifiers).
