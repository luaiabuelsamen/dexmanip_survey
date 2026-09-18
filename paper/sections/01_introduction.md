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
states in Sec. 1.5 that "force closure does not guarantee stability", and in Sec. 1.6 that "a
tractable and accurate model of friction, one that accurately predicts slip and one that lends
itself to stability analysis, is currently not available". Its quality measures assume small
perturbations, and Sec. 1.8 names the reason the theory could not be pushed further, which is that
"the nonsmooth nature of grasp dynamics, because of the unilateral constraints on displacements and
forces, has made a thorough analysis very difficult". Learned control did not solve any of those
modelling problems. It went around them by sampling a simulator instead of solving a model, and by
scoring a rollout instead of certifying a configuration. Of the 110 method papers in this corpus,
53 train with reinforcement learning and 35 run in Isaac Gym.

Six recent overviews were obtained and bear directly on this one. Each leaves a different part of
the problem open. `an_dexil_survey_2025` is the closest, covering imitation learning for multi-fingered hands by
learning family, end-effector class and demonstration source. It gives reinforcement learning no
taxonomy, treats bimanual work as a single "multi-agent" subsection, compares no simulator, and
defines no evaluation metric. `welte_iil_survey_2025` argues for interactive imitation learning,
finds only seven dexterous works that use it, and carries a fifteen-hand commercial table. It has no
bimanual section, no benchmark table and no contact modelling. `bai_unified_manip_survey_2025` spans
all of manipulation across 212 pages and gives dexterous manipulation about thirty lines in Sec. 4.3,
deferring the subject to other surveys in its Sec. 1.2. `zhao_dexhand_survey_2026` is the most recent
hand-centred survey, with a 29-hand anatomy table and a task-by-paradigm taxonomy. It has no
simulator section, names Isaac Gym and MuJoCo once each, and uses the word penetration exactly once.
`zhao_sim2real_survey_2020` supplies the standard split of sim-to-real methods into system
identification, domain randomisation and domain adaptation. It predates GPU-parallel simulation,
mentions two hand papers, and never discusses contact models. `firoozi_foundation_models_2023`
surveys foundation models in robotics and contains zero occurrences of bimanual, tactile or
in-hand, which makes it orthogonal rather than competing. What none of them provides is a comparison
of the physics engines these policies are trained in, a treatment of two hands on one object as its
own problem, and an evaluation frame that asks whether the contact a policy produces is physically
plausible. Those three are what this survey adds.

Four foundational overviews could not be obtained. `okamura_overview_2000`, `bicchi_hands_2000`,
`ma_dollar_dexterity_2011` and `piazza_century_2019` are all behind publisher paywalls with no
author-hosted copy found on 2026-09-18. They are cited by metadata only, and nothing here describes
their contents. The open chapter `bicchi_grasping_chapter_2001` was obtained and overlaps the
paywalled Bicchi paper without being identical to it, so it is quoted in its own right.

The scope is single-hand and bimanual multi-fingered manipulation. That covers the hands and who
makes them, the simulators and the contact physics underneath, the training methods, and an
evaluation frame. Parallel-jaw manipulation enters only as a comparison, which matters because
12 of the 110 method rows name a parallel-jaw gripper among their own embodiments. Locomotion is
excluded.
Prosthetics are excluded except where a hand crosses over into robot use, as the Psyonic Ability
Hand does. The corpus behind all of this holds 221 bibliography entries, of which 216 carry a
structured row read from a note.

Figure 1 puts the field on one page. Section 2 sets out the task families and what makes each hard.
Section 3 covers hands, their makers, and the gap between what is sold and what is run. Section 4
covers simulators and contact models. Section 5 covers how policies are trained and is the longest
section. Section 6 covers bimanual work as its own problem. Section 7 proposes an evaluation frame
rather than a leaderboard. Section 8 states the gaps as claims with their evidence.

{{figure:fig1_field}}

<!--
FIGURE 1. The field on one page.

Format: hand-written SVG, paper/figures/fig1_field.svg, light and dark palette via CSS custom
properties, as paper/FIGURES.md requires. Left-to-right flow, five labelled columns.

Column 1, DATA SOURCES. Four nodes: "no demonstrations" (49 of 110 method rows record
human_data = none), "human mocap and hand-object capture", "teleoperated robot demonstrations",
"human video without a robot". The last three together are the 53 of 110 method rows that name a
human data source. Node area proportional to those counts. A fifth small node, "not stated" (8 of
110), drawn in outline only.

Column 2, EMBODIMENT. Two nodes sized by count: "one hand" (56 of 110 method rows with
bimanual = false) and "two hands" (51 of 110 with bimanual = true). Three rows are null and appear
as a hairline stub. Inside each node, list the hands that recur, Allegro, Shadow, LEAP, Inspire,
taken from corpus/stats.json.

Column 3, SIMULATOR. Nodes sized by method count after normalising the free-text sim field:
Isaac Gym 35, MuJoCo 18, Isaac Lab or Isaac Sim 6, SAPIEN 4, RaiSim 2, Drake 2, Genesis 1,
other or unclear 8, no simulator 3, not stated 31. Draw "not stated" in outline only, same
convention as column 1, because it is a reporting gap and not a choice.

Column 4, TRAINING PARADIGM. Nodes sized by method count, labels multi-valued so the column sums
above 110: RL 53, BC 27, distillation 23, VLA 16, teleop-system 14, diffusion 14, data-collection
10, flow 8, RL+demo 6, trajopt 6, MPC 5, grasp-synthesis 4, world-model 2.

Column 5, EVALUATION. Three nodes: "real robot" 87 of 110, "simulation only" 22 of 110, and a
narrow node "penetration addressed at all" 11 of 110, split into penalised 3, measured 3,
constrained 5. Set against it a wide node "penetration not addressed" 83 of 110. This contrast is
the figure's punchline and should be the visually heaviest element in the column.

Edges: draw only routes that exist in the corpus, with stroke width proportional to the number of
method rows taking that route. Label these four routes by name:
(a) no demonstrations -> one hand -> Isaac Gym -> RL -> real robot, the single heaviest path;
(b) human mocap -> one or two hands -> Isaac Gym -> RL tracking -> real robot, the track-human-ref
route; (c) teleoperated demonstrations -> two hands -> no simulator -> BC or diffusion -> real
robot, the route that skips physics entirely; (d) any source -> Isaac Gym -> RL -> distillation ->
real robot, the teacher-student route, drawn as a loop back from column 4 into itself.

The point the figure must make, stated in a one-line caption under it: the routes converge. Almost
everything ends in a policy trained in a GPU simulator and distilled to a vision or proprioception
student, and almost nothing checks whether the contact it produced was physical.

Every number above comes from corpus/rows/*.json and must be regenerated by the drawing script
rather than typed in, so the figure cannot drift from the rows.
-->
