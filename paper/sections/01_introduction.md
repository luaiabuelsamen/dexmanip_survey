# 1. Introduction

A hand is dexterous when it can change an object's pose without putting the object down. That
property, and not the finger count, is what separates a hand from a gripper. `bicchi_grasping_chapter_2001`
draws the same line in Sec. 1.1, between restraining an object and "manipulating objects with
fingers, in contrast to manipulation with the robot arm". Restraint is a static question about
whether the contacts prevent motion. In-hand manipulation is a dynamic question about whether
contacts can be broken and remade while the object stays held. `an_dexil_survey_2025` puts the same
idea in its abstract as the ability "to skillfully control, reorient, and manipulate objects through
precise, coordinated finger movements and adaptive force modulation". Both definitions place the
work in the fingers rather than in the arm.

The analytic theory answered the static question and stalled on the dynamic one. Form closure has a
first-order test on the grasp matrix and known contact counts, four in the plane and seven in three
dimensions for any polyhedron, per `bicchi_grasping_chapter_2001` Sec. 1.3.1. Force closure adds the
wrench balance and the hand Jacobian. Neither delivers what a controller needs. The same chapter
states in Sec. 1.5 that "force closure does not guarantee stability", and its Sec. 1.8 names the
reason the theory could not be pushed further, which is that "the nonsmooth nature of grasp
dynamics, because of the unilateral constraints on displacements and forces, has made a thorough
analysis very difficult". That verdict is one architect's, on one chapter, and this survey did not
survey the tradition it judges. Learned control did not solve those modelling problems. It went
around them by sampling a simulator instead of solving a model, and by scoring a rollout instead of
certifying a configuration. Of the 112 method papers in this corpus, 53 train with reinforcement
learning and 35 run in Isaac Gym.

Fourteen corpus entries are themselves surveys or engine-comparison studies, and Table 10 sets them
on one set of columns. The columns are what each work covers, not how well.
`an_dexil_survey_2025` is the closest in subject, covering imitation learning for multi-fingered
hands by learning family, end-effector class and demonstration source. It gives reinforcement
learning no taxonomy, treats bimanual work as a single "multi-agent" subsection, compares no
simulator, and defines no evaluation metric. `welte_iil_survey_2025` finds only seven dexterous
works that use interactive imitation learning and carries a fifteen-hand commercial table, with no
bimanual section, no benchmark table and no contact modelling. `zhao_sim2real_survey_2020` supplies
the standard sim-to-real split and predates GPU-parallel simulation.
`firoozi_foundation_models_2023` has zero occurrences of bimanual, tactile or in-hand.

`bai_unified_manip_survey_2025` spans all of manipulation across 212 pages. Its Sec. 4.3 on
dexterous manipulation runs about 720 words, the third longest of its ten task subsections behind
grasping and quadrupedal manipulation, which is a real treatment and not a passing mention. The
difference is elsewhere. Its Sec. 1.2 lists dexterous manipulation among the topics that "existing
surveys" cover from "narrower perspectives" and defers it to two of them.

`zhao_dexhand_survey_2026` is the most recent hand-centred survey, with a 29-hand anatomy table and
a task-by-paradigm taxonomy, and it already draws the distinction this survey builds on. Its
Sec. IV-C states that the field assesses "at least two layers of performance: the quality of grasps
or poses prior to execution, and the performance of policies or generators during downstream
execution", and names "physical plausibility, including penetration" as the most common criterion
for the first layer. That is the reference-versus-rollout split, named by a predecessor before this
survey measured it. What Sec. IV-C does not give is a threshold, a measurement method or a count.
This survey supplies those three. Eleven of the 96 method rows whose notes settle the question
address interpenetration at all, seven of the eleven do it outside a closed-loop policy in a grasp
synthesiser, a trajectory optimiser or a contact model, and none reports a penetration number for
its own trained policy's rollouts. The contribution here is that measurement
and the argument that a measure a policy optimises cannot also judge it. The idea that contact
quality belongs on the evaluation axis is Zhao's.

`nine_physics_engines_review_2024` is the predecessor closest to the engine comparison, and it
reviews Brax, Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Unity and Webots for reinforcement
learning research. It scores each on documentation, model and environment creation, URDF and MJCF
support, and readiness for multi-agent work. It runs no benchmark of its own and says so in its
Sec. V, that implementing the same scenarios across nine engines "goes beyond the scope of this
paper". Its running bodies are ant-and-humanoid RL benchmarks rather than hands, and it discusses
no timestep, no friction model, no contact formulation and no penetration.

The three things this survey adds are narrower than a claim of breadth. The first is Table 4, which
takes the same engines and adds contact model, solver, iteration count, default timestep and
penetration exposure, conditioned on what a hand does to a solver. `physics_engine_comparison_2015`
and `contact_models_comparison_2023` do measure engines, on five engines and on four contact
formulations, and neither surveys the field those engines are used in. The second is two hands on
one object as its own problem, which none of the four field surveys gives more than a subsection.
The third is the penetration measurement above, on an axis `zhao_dexhand_survey_2026` had already
named.

{{table:table10_surveys}}

Table 10's last rows carry the cost of the corpus. `okamura_overview_2000`, `piazza_century_2019`
and `roa_suarez_grasp_quality_2015` are behind publisher paywalls with no author-hosted copy found
on 2026-09-18, and `bicchi_hands_2000` is in the same position with no row at all.
`ma_dollar_dexterity_2011` is a different case. The fetch that failed when its note was written
succeeded afterwards, so a seven-page PDF is on disk with a recorded hash, and no note has been
read from it. All five are cited by metadata only and nothing here describes their contents. The
open chapter `bicchi_grasping_chapter_2001` overlaps the paywalled Bicchi paper without being
identical to it, so it is quoted in its own right.

This is a corpus of the learned era, which is a selection effect and not a judgement. Of the 221
bibliography entries, 138 are dated 2024 or later and 16 predate 2018, and two of the 112 method
rows predate 2018. Any statement here about a trend over time is a statement about 2022 onward. The
analytic tradition is represented by one readable chapter rather than surveyed, and the planning
line that took up the dynamic question directly, finger gaiting and rolling-contact manipulation
and regrasp planning, is not in the corpus at all.

The scope is single-hand and bimanual multi-fingered manipulation. That covers the hands and who
makes them, the simulators and the contact physics underneath, the training methods, and an
evaluation frame. Parallel-jaw manipulation enters only as a comparison, which matters because
12 of the 112 method rows name a parallel-jaw gripper among their own embodiments. Locomotion is
excluded. Prosthetics are excluded except where a hand crosses over into robot use, as the Psyonic
Ability Hand does. The corpus behind all of this holds 221 bibliography entries, of which 218 carry
a structured row read from a note.

Figure 1 puts the field on one page. Section 2 sets out the task families and what makes each hard.
Section 3 covers hands, their makers, and the gap between what is sold and what is run. Section 4
covers simulators and contact models. Section 5 covers how policies are trained and is the longest
section. Section 6 covers bimanual work as its own problem. Section 7 proposes an evaluation frame
rather than a leaderboard. Section 8 states the gaps as claims with their evidence.

{{figure:fig1_field}}
