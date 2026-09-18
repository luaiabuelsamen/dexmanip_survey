# Dexterous Manipulation, Single-Hand and Bimanual: Machines, Simulators, and How Policies Are Trained
## A survey with an evaluation frame

Audience: a researcher choosing a hand, a simulator and a training recipe. Every claim
traces to papers/notes/<key>.md, which traces to papers/md and code/md on disk.

## 1. Introduction
What makes a hand dexterous; why the field moved from analytic grasp planning to learned
control; what this survey adds over the existing reviews (positioned against the notes for
okamura_overview_2000, bicchi_hands_2000, ma_dollar_dexterity_2011, piazza_century_2019,
an_dexil_survey_2025, welte_iil_survey_2025, bai_unified_manip_survey_2025,
zhao_dexhand_survey_2026). Scope statement and what is excluded.
FIGURE 1: the field on one page. Data sources -> embodiment -> simulator -> training paradigm
-> evaluation, with the paper counts on each path.

## 2. A taxonomy of the problem
2.1 Task families: in-hand reorientation, grasping, functional/tool use, tracking a human
reference, bimanual coordination, handover and in-hand transfer.
2.2 What makes each hard: contact non-smoothness, underactuation, occlusion, gravity direction.
2.3 Single-hand vs bimanual: what genuinely changes (role asymmetry, closed kinematic chain
through the object, two-arm collision, doubled action space).
TABLE 1: task family x the properties that define success.

## 3. Hands and who makes them
3.1 Design axes: DoF and actuated DoF, tendon vs linkage vs direct drive vs hydraulic,
compliance, sensing, cost, repairability.
3.2 Research and commercial hands in use today. TABLE 2, the big hand table, one row per hand:
maker, country, DoF/actuated, actuation, weight, fingertip force, tactile, price, open hardware,
release status, and the corpus papers that use it.
3.3 Open-hardware hands and the cost collapse (LEAP, RUKA, ORCA, Faive, BiDexHand, DexHand).
3.4 Announced and unreleased hands: Tesla, Figure, 1X, Sanctuary, Boston Dynamics, Xiaomi,
Proception, Daxo, Clone, AgiBot, ByteDance. Explicitly separated into datasheet claim,
video demonstration, and independent measurement. TABLE 3.
3.5 Tactile sensing as part of the hand.
3.6 What the research literature actually runs on, versus what is sold. FIGURE 2: hand usage
by paper count over time, from the corpus.

## 4. Simulators and the physics underneath
4.1 What a dexterous simulator must get right: many simultaneous contacts, friction, stiff
contact without instability, speed.
4.2 Contact models and solvers, engine by engine. TABLE 4: engine, contact model, solver,
differentiable, GPU, timestep, exposed penetration, hands shipped.
4.3 The GPU-parallel turn: Isaac Gym, Isaac Lab, MJX, MuJoCo Warp, Newton, Genesis.
4.4 Throughput, and why reported FPS numbers are not comparable.
4.5 Tactile simulation.
4.6 The sim-to-real gap, and what is known about its causes for hands.
FIGURE 3: the contact pipeline of a dexterous simulation step, with where each engine differs.

## 5. How policies are trained
5.1 The design space. FIGURE 4: a taxonomy tree of training paradigms with representative
papers at the leaves.
5.2 Reinforcement learning
  5.2.1 The standard recipe: PPO, massively parallel envs, domain randomisation, teacher-student
        distillation from privileged state to vision.
  5.2.2 Reward engineering. TABLE 5: reward terms across reorientation papers, which terms recur.
  5.2.3 Curricula, population-based training, automated reward design.
  5.2.4 What RL is good at and where it stalls.
5.3 Learning from human data
  5.3.1 Teleoperation systems and retargeting. TABLE 6: teleop rigs, hand, latency, cost.
  5.3.2 Imitation learning architectures: behaviour cloning, action chunking, diffusion, flow.
  5.3.3 Human video without a robot: retargeting, affordances, hand pose priors.
  5.3.4 The embodiment gap and how each method closes it.
5.4 Tracking a human reference with physics: the middle path between RL and IL.
5.5 Vision-language-action models and generalist policies for hands.
5.6 Model-based control, trajectory optimisation and sampling MPC as the non-learning baseline.
5.7 Hybrids, and the recurring pattern of RL in simulation distilled into an IL-shaped policy.
TABLE 7: method x paradigm x embodiment x data x sim, the survey's master table.

## 6. Bimanual dexterous manipulation
6.1 Why two hands is not twice one hand.
6.2 Coordination architectures: monolithic policy, per-hand policies with shared observation,
leader-follower role assignment, relative-frame formulations.
6.3 Bimanual benchmarks and datasets.
6.4 Methods, compared on the same axes as section 5.
6.5 What transfers from single-hand and what does not.
FIGURE 5: coordination architectures side by side.

## 7. Evaluation: how we would compare these methods
Deliberately a frame, not a leaderboard. The survey does not re-run the methods.
7.1 What the field currently reports, and why the numbers do not compare: different hands,
different object sets, different success thresholds, different trial counts.
7.2 The axes that matter: task success, robustness to perturbation, generalisation to unseen
objects, physical plausibility of the contact, sample and wall-clock cost, real-robot transfer,
reproducibility.
7.3 Physical plausibility as a first-class metric: interpenetration, contact consistency, and
why a measure a policy optimises cannot also judge it.
7.4 Statistics: trial counts, confidence intervals, sequential testing, paired comparison
(kress_gazit_policy_eval_2024, lbm_careful_examination_2025, suresim_2025,
beyond_binary_success_2026, roboarena_2025).
7.5 A proposed evaluation protocol, stated concretely enough to be run by someone else.
TABLE 8: the protocol. TABLE 9: an empty results matrix, methods x axes, for the community
to fill.
7.6 What would have to be true for this protocol to be adopted.

## 8. Gaps
Each gap stated as a claim, the evidence for it from the corpus, and what would close it.
Candidates, to be confirmed against the notes: contact-quality reporting is absent; bimanual
evaluation has no shared benchmark; hand hardware is fragmenting faster than the software that
supports it; announced hands are not measurable; tactile is simulated but rarely used in a
policy that ships; human data is not portable across hands; success thresholds are not
standardised; nobody reports failure modes; sim-to-real is reported as a success delta rather
than diagnosed.

## 9. Conclusion

## Appendices
A. Corpus and method: how papers were selected, downloaded, parsed and noted; the manifest.
B. The full hand table with sources.
C. Per-paper reward term extraction.
