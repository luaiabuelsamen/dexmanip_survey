# 1. Introduction

A hand is dexterous when it can change an object's pose without putting the object down. That
property, and not the finger count, is what separates a hand from a gripper.
`bicchi_grasping_chapter_2001` draws the same line in Sec. 1.1, between restraining an object and
"manipulating objects with fingers, in contrast to manipulation with the robot arm". Restraint is
a static question about whether the contacts prevent motion. In-hand manipulation is a dynamic
question about whether contacts can be broken and remade while the object stays held.
`an_dexil_survey_2025` puts the same idea in its abstract as the ability "to skillfully control,
reorient, and manipulate objects through precise, coordinated finger movements and adaptive force
modulation". Both definitions place the work in the fingers rather than in the arm.

The analytic theory answered the static question and stalled on the dynamic one. Form closure has
a first-order test on the grasp matrix and known contact counts, four in the plane and seven in
three dimensions for any polyhedron, per `bicchi_grasping_chapter_2001` Sec. 1.3.1. Force closure
adds the wrench balance and the hand Jacobian. Neither delivers what a controller needs. The same
chapter states in Sec. 1.5 that "force closure does not guarantee stability", and its Sec. 1.8
names the reason the theory could not be pushed further, which is that "the nonsmooth nature of
grasp dynamics, because of the unilateral constraints on displacements and forces, has made a
thorough analysis very difficult". That verdict is one architect's, on one chapter, and this
survey did not survey the tradition it judges. Learned control did not solve those modelling
problems. It went around them by sampling a simulator instead of solving a model, and by scoring a
rollout instead of certifying a configuration. Of the 112 method papers in this corpus, 53 train
with reinforcement learning and 36 run in Isaac Gym, against 6 on its successor Isaac Lab.

Three things this survey measured are worth stating before the reader commits to 27,000 words. The
first is that papers disagree with their own released code. Sixty-two of the 112 method rows
released code that could be read against the paper, 38 of those record a discrepancy, and nine are
contradictions where the shipped code states a different objective from the published one. The
sharpest case is `physhoi_2023`. Its `compute_humanoid_reward` hardcodes the object rotation and
rotation-velocity errors to zero, with the real computation commented out beside them, while the
reward table in its own paper lists weights of 0.1 and 0.01 for exactly those terms on GRAB. Its
position-only success criterion could not have caught that, and its headline 95.4 percent is cited
as a baseline. Section 5.8 classifies all 38, and seven further accusations an earlier draft made
were withdrawn under adversarial review and recorded beside the charge.

The second is that the quantity most specific to a hand is the one nobody records. Eleven of the
96 method rows whose notes settle the question address interpenetration at all, seven of the
eleven do it outside a closed-loop policy in a grasp synthesiser, a trajectory optimiser or a
contact model, and none reports a penetration number for its own trained policy's rollouts. The
obstacle is not the engines. NVIDIA's own IsaacGymEnvs repository already computes a
per-environment maximum interpenetration depth in Warp and gates the policy update on a 1 mm
threshold. Section 7.3 has the file and the lines.

The third is that hardware and published work have come apart. 18 of the 33 hand rows in
Tables 2 and 3 appear in no method row, and 7 of those can be bought today or built from
published designs. Thirty-five method rows run on the Allegro, whose weight, joint torque, payload
and price have no reachable source, because its product page returns HTTP 404 and everything Table
2 confirms about it comes from its ROS driver.

Fourteen corpus entries are themselves surveys or engine-comparison studies. Appendix D sets them
on one set of columns in Table 10 and says what each covers. Four of the fourteen could not be
obtained, or were fetched too late to read, and are entered as such. Two of the three things this
survey adds are visible in that table as columns nobody else fills. The first is Table 4, which
takes the engines `nine_physics_engines_review_2024` scored on documentation and usability and
adds contact model, solver, iteration count, default timestep and penetration exposure,
conditioned on what a hand does to a solver. `physics_engine_comparison_2015` and
`contact_models_comparison_2023` do measure engines, on five engines and on four contact
formulations, and neither surveys the field those engines are used in. The second is two hands on
one object as its own problem, which none of the four field surveys gives more than a subsection.

The third is the penetration measurement, on an axis a predecessor had already named.
`zhao_dexhand_survey_2026` states in its Sec. IV-C that the field assesses "at least two layers of
performance: the quality of grasps or poses prior to execution, and the performance of policies or
generators during downstream execution", and names "physical plausibility, including penetration"
as the most common criterion for the first layer. That is the reference-versus-rollout split,
named before this survey measured it, and the idea that contact quality belongs on the evaluation
axis is Zhao's. What Sec. IV-C does not give is a measurement method or a count, and this survey
supplies those two. It does not supply a threshold. The 2 mm figure the field uses is taken from
`toporetarget_2026` with no independent justification, the captured human grasps in `grab_2020`
sit above it at 3.25 mm, and Section 7.7 states plainly that 2 mm is a simulator convention rather
than a physical bound.

The scope is single-hand and bimanual multi-fingered manipulation. Parallel-jaw manipulation
enters only as a comparison, which matters because 12 of the 112 method rows name a parallel-jaw
gripper among their own embodiments. Locomotion is excluded. Prosthetics are excluded except where
a hand crosses over into robot use, as the Psyonic Ability Hand does. The corpus holds 221
bibliography entries, of which 218 carry a structured row read from a note. Those 218 rows are 112
method papers, 33 hands, 15 simulators, 15 datasets, 14 benchmarks, 14 surveys, 8 tactile sensors
and 7 evaluation protocols. "Method row" throughout means one of the 112, and every headline count
in this survey has one of those eight classes as its denominator.

Two limits apply to every number here. This is a corpus of the learned era, which is a selection
effect and not a judgement: 138 of the 221 entries are dated 2024 or later, 16 predate 2018, and
two of the 112 method rows predate 2018, so any statement about a trend over time is a statement
about 2022 onward. The analytic tradition is represented by one readable chapter rather than
surveyed, and the planning line that took up the dynamic question directly, finger gaiting and
rolling-contact manipulation and regrasp planning, is not in the corpus at all. Every coverage
statistic is also a floor rather than a rate, because a value this survey failed to extract is
indistinguishable from a value the paper never reported, and every such miss converts a reporting
paper into a silent one.

Figure 1 puts the field on one page. Section 2 sets out the task families and what makes each
hard. Section 3 covers hands, their makers, and the gap between what is sold and what is run.
Section 4 covers simulators and contact models. Section 5 covers how policies are trained. Section
6 covers bimanual work as its own problem. Section 7 proposes an evaluation frame rather than a
leaderboard, and is the longest section. Section 8 states the gaps as claims with their evidence.
Section 9 says what to do about them, addressed to someone publishing, running experiments or
buying a hand. Appendix A is the method, Appendix B and Appendix C are the full hand and reward
extractions, and Appendix D is the comparison with the existing surveys.

{{figure:fig1_field}}
