# Dexterous Manipulation, Single-Hand and Bimanual

## Machines, simulators, and how policies are trained

A survey of 216 works, with an evaluation frame and the gaps it exposes.

*Compiled 2026-09-18. Every claim traces to a note in `papers/notes/`, every note to a parsed source in
`papers/md/` or `code/md/`, and every source to a hash or commit in `corpus/manifest.json`. The
method is in Appendix A.*

---


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

![fig1_field](figures/fig1_field.svg)

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

# 2. A taxonomy of the problem

## 2.1 Task families

Grasping is the largest family. Fifty-five of the 110 method rows carry the grasp label, and the
labels are not exclusive, so one paper can sit in several families. Success is a lift that survives a
hold, and the thresholds differ by more than an order of magnitude. `dexgraspvla_2025` requires the
object "held 10 cm above the table for 20 s", while `omnigrasp_2024` requires it "held at least 0.5 s
in simulation". What makes grasping hard at scale is the continuum of starting configurations.
`unidexgrasp_pp_2023` states it in Sec. 4.3, that "we are dealing with an infinite number of tasks
considering the initial object pose can change continuously".

Functional and tool use is second with 43 rows. It is the family where a stable grasp can still be
the wrong answer. `dexterous_functional_grasping_2023` gives the case in Sec. 2.1, that "grabbing a
hammer from the head or handle are both equally valid ways of using it", and only one of the two
lets the tool be used. Success is defined against the tool's function, and the field has no shared
way to state it.

In-hand reorientation has 31 rows and the most settled criteria, because the community inherited one
number. `openai_dexterity_2018` declared the goal achieved below 0.4 rad of orientation error,
`dextreme_2022` keeps 0.4 rad at test time against a 0.1 rad training tolerance, and `eureka_2023`
counts consecutive successes at 0.1 rad. A shared tolerance is not a shared protocol, because the
stopping rule differs. `visual_dexterity_2022` measures error "when the controller predicts it has
reached the goal and stops", which makes the policy a judge of its own trial.

Tracking a human reference has 12 rows and inverts the problem. The target is a trajectory rather
than an endpoint, so success is a per-frame error band. `maniptrans_2025` requires all four of 30
degrees of rotation, 3 cm of translation, 8 cm of joint error and 6 cm of fingertip error. The
difficulty is that the reference came from a human hand and was never dynamically feasible for the
robot. `dexmachina_2025` warns in App. B.4 that scoring by timesteps inside the thresholds makes
"the results highly sensitive to the threshold values".

Bimanual coordination has 42 rows and handover has 9. Handover is the smallest family and the one
whose failure has a single moment, because the giver must release only after the receiver has the
object. `dynamic_handover_2023` reports a hit rate above its success rate and blames the gap in
Sec. 5.4 on "occasional challenges encountered during the grasping phase of the catcher". Not every
paper here learns both sides. In `dexterous_handover_2025` only the receiver is learned and the giver
is a scripted arm.

## 2.2 What makes dexterous control hard

Contact is non-smooth, and that is a property of the problem rather than of any solver.
`bicchi_grasping_chapter_2001` states in Sec. 1.2 that contact constraints are unilateral, and that
losing a contact "involves an abrupt change of the structure of the model under consideration". Its
Sec. 1.4 gives the sharper version, that a rod sliding on rough ground has configurations with no
consistent solution and configurations with more than one. Simulators inherit the difficulty. The
re-implementation study `contact_models_comparison_2023` concludes in Sec. V that "there is no fully
satisfactory approach at the moment, as all existing solutions compromise either accuracy,
robustness, or efficiency". `pang_global_planning_2022` treats non-smoothness as the thing to remove,
curating every contact pair in Sec. III-D so that contact points and normals change smoothly.

The hand has more actuators than the object has degrees of freedom and is still short of authority
over it. The object moves only through contacts, and the contacts are what cannot be commanded.
`bicchi_grasping_chapter_2001` Sec. 1.4 states that in multifingered grasps "the number of
independent contact forces is much larger than the number of actuators. Thus, from a controllability
standpoint, not all the contact forces are controllable".

Vision is occluded by the hand doing the work. `bai_unified_manip_survey_2025` names it in Sec. 4.3,
that "occlusion hampers object tracking". `dexpoint_2022` keeps vision and adds imagined hand points
to the point cloud. `rotating_without_seeing_2023` removes vision entirely and rotates objects from
16 binary touch sensors over the palm, links and fingertips.

Gravity direction changes the task rather than scaling it. `visual_dexterity_2022` states that
reorientation with the hand below the object "is much easier", because "with a downward-facing hand,
the hand must manipulate the object while simultaneously counteracting gravity". `anyrotate_2024`
makes the direction a randomised variable by "randomly initializing hand orientations between
episodes", and its Sec. 5.3 measures the cost, with performance dropping progressively from palm up
and palm down, through base up and base down, to thumb up and thumb down.

## 2.3 Single hand versus two

Fifty-one of the 110 method rows run two hands. Four things genuinely change. Contact stays
non-smooth, occlusion stays, and gravity stays the same problem.

Role asymmetry is the first. `asymdex_2024` assigns a dominant hand with full finger and wrist
control and a facilitating hand with 6-DoF base pose only, so that "the facilitating hand repositions
and reorients one object, while the dominant hand performs complex manipulations".

The second is that two hands on one object close a kinematic chain through the object. In
`bicchi_grasping_chapter_2001` Sec. 1.4 the hand and object dynamics are separate and are "linked
through the n rigid-body contact constraints". A second hand adds a second constraint set on the
same object rather than a second independent problem. That is where physical plausibility fails
first. `bimangrasp_2024` is the corpus row that measures it, rejecting a synthesised grasp when
"total penetrations exceeded 1.5 mm" and reporting in Sec. IV-C that "penetration remains the primary
cause of grasp failure".

The third is two-arm collision, which does not exist for one hand. `dydexhandover_2025` resets an
episode when "any unintended arm contact with the environment or self-collisions" occurs.
`bunny_visionpro_2024` pays for it in the controller, where adding a sphere-approximated
self-collision cost raises motion-control time from 0.74 ms to 7.85 ms. `bidex_teleop_2024` solves it
in hardware, mounting the hands so the human arm and the teacher arm "are perpendicular to each other
and do not collide". `dexmimicgen_2024` states plainly that it does not handle inter-arm collision at
all.

The fourth is the doubled action space. `bidexhands_2022` runs 20 tasks on two Shadow Hands and finds
single-agent PPO beating multi-agent RL on most of them, offering in Sec. 5.2 that "PPO algorithm is
able to use all observations for training the policy, while MARL can only use partial observations".
`asymdex_2024` attacks the dimensionality from the other side, halving the observation and action
dimension through its role split and a frame relative to the facilitating hand's object.

## Table 1. Task families against the properties that define success

| task family | what is held | what moves | what gravity does | what counts as failure | shortest honest success criterion |
|---|---|---|---|---|---|
| In-hand reorientation | one rigid object, held by the fingers for the whole episode | the object's orientation in the palm frame, while contacts break and remake | a disturbance whose direction is set by hand orientation, and a load to counteract with the palm down, `visual_dexterity_2022` | the object leaves the hand, e.g. the fall reset at goal distance 0.24 m in `dextreme_2022` | orientation error below a stated tolerance under a stated stopping rule, 0.4 rad in `openai_dexterity_2018` and `dextreme_2022`, 0.1 rad in `eureka_2023` |
| Grasping | nothing at the start, the object rests on a support | the hand closes, then the object is lifted clear | the test itself, since the grasp exists to resist it | no lift, or a drop inside the hold window | a stated lift height held for a stated duration, 10 cm for 20 s in `dexgraspvla_2025`, 10 cm to episode end in `graspxl_2024`, 0.5 s in `omnigrasp_2024` |
| Functional and tool use | a tool, held in the pose its function requires rather than the most stable one | the tool's own joint, or the tool acting on a second object | secondary, the function dominates | a stable grasp in the wrong place, `dexterous_functional_grasping_2023` | no agreed criterion. Criteria range from never dropping the object, `dexterous_functional_grasping_2023`, to a four-point rubric, `dexvla_2025`. The one mechanical threshold is holding the tool joint past a commanded angle for the episode, `articulated_tools_inhand_2025` |
| Tracking a human reference | whatever the human held in the captured clip | hand and object follow a recorded trajectory under physics | full, and the reference never obeyed it, so the reference is not dynamically feasible | per-frame error leaves the band, or the object drops | all stated per-frame errors below threshold for the whole clip, 30 deg and 3 cm and 8 cm joint and 6 cm fingertip in `maniptrans_2025`. Thresholds are not comparable across papers, and `dexmachina_2025` calls the results "highly sensitive to the threshold values" |
| Bimanual coordination | one object by two hands, or one object per hand | both hands, the object, and the relative pose of the hands | can be carried by one hand while the other acts, `asymdex_2024` | the object drops, the arms collide, or the hands work against each other | no agreed criterion. Task-specific thresholds dominate, e.g. 0.035 m block-to-cup distance in `asymdex_2024`. The one criterion with a physical-plausibility gate is 2.0 s of hold with total penetration under 1.5 mm, `bimangrasp_2024` |
| Handover and in-hand transfer | by the giver at the start, by the receiver at the end | the object crosses between hands, released only after it is regained | unopposed during the exchange, and total in a thrown transfer, `dynamic_handover_2023` | a drop at the moment of release, and the catcher's grasp phase, `dynamic_handover_2023` Sec. 5.4 | the receiver holds the object and moves it clear, more than 10 cm from the first hand in `hato_visuotactile_2024`, or holds it to episode end in `dydexhandover_2025` |

Two cells say the field has no agreed criterion, and both are in families where a second body is
involved. A criterion naming a distance, a duration and a trial count can be re-run by someone else.
A rubric cannot, and Section 7 takes up what follows from that.

# 3. Hands and who makes them

## 3.1 The design axes

The degree-of-freedom count is the first number a vendor states and the least comparable one.
Shadow's specification of December 2024 reads "20 actuated DOF and a further 4 under-actuated
movements for a total of 24 joints" `shadow_dexterous_hand_2005`. LEAP Hand v2 Advanced claims
"21 DOF with 17 powered motors" on its page while its own README calls the hand "17-DOF"
`leap_hand_v2_adv_2025`. Unitree's Dex5-1 page reads "20 Degrees of freedom (16 active+4)"
`unitree_dex5_2025`. Table 2 therefore prints actuated DoF beside DoF, and the gap is the
informative number.

The actuation ratio is the real decision. The Pisa/IIT SoftHand drives 19 joints from one motor
through an adaptive-synergy differential and holds about 20 N with a 6 W Maxon RE-max21
`pisa_iit_softhand_2014`. Its authors state the cost plainly: "No in-hand dexterous manipulation
is required for this prototype." At the other end sit 1X's claimed 25 fully actuated degrees of
freedom `onex_neo_hand_2026` and Daxo's reported 120 actuators in 0.75 kg
`daxo_muscle_v0_2025`, neither of them measured by anyone outside the company.

Tendon drive moves the motors off the fingers and the mass follows them. Shadow's hand plus
forearm weighs 4.3 kg and holds 4 kg in a power grasp `shadow_dexterous_hand_2005`, while RUKA's
11 forearm Dynamixels give a 2.74 N pinch and a 6.0 kg payload `ruka_2025`. What tendons cost is
state estimation. The Faive Hand shipped without joint encoders and estimated angles from tendon
length through a Kalman filter, and its cube reorientation still failed on hardware, which its
authors blamed on "poor joint angle measurement from the EKFs, especially when there is contact"
`faive_hand_2023`. ORCA reports the same problem as maintenance: "Prolonged use requires manual
re-tensioning to maintain performance" `orca_hand_2025`. Ruka-v2 bolts AS5600 encoders onto the
joints instead, leaving an 8.26-degree average error under a linear joint-to-motor map
`ruka_v2_2026`.

Direct drive trades torque density for transparency. LEAP's Dynamixel joints give a 19.5 N
pull-out force against the Allegro Hand's 8.5 N at 595 g `leap_hand_2023`. Wuji states
"Direct-drive rotary, back-drivable" with 1000 Hz across 20 axes, and states no weight and no
fingertip force at all `wuji_hand_2025`. 1X makes the same argument by gear ratio, calling the
100:1 to 200:1 ratios of stiff hands "write-only" `onex_neo_hand_2026`.

Linkage drive is the argument against the forearm. ILDA puts 15 motors, drivers and ball screws
inside the palm and reports 34 N of fingertip force at 1.1 kg `ilda_hand_2021`, a quarter of
Shadow's mass for a larger force. Linkages also buy coupling for free, as in BiDexHand's
anti-parallelogram four-bar that drives each DIP off its PIP and saves an actuator per finger
`bidexhand_2025`, or the Ability Hand's five fingers on six motors `psyonic_ability_hand_2021`.
Hydraulics appear only in hands nobody outside the company has held. Sanctuary claims
miniaturised valves with "an order of magnitude higher power density than cable and
electromechanical-based systems" and puts no number behind it `sanctuary_phoenix_hand_2024`.
Clone's 27-DoF hand weighs under 2 pounds only because its 500 W pump sits outside it
`clone_robotics_hand_2024`.

Compliance and repairability are the same axis seen twice. The Pisa/IIT SoftHand's
rolling-contact joints are held by polyurethane ligaments and return to assembly after
over-extension `pisa_iit_softhand_2014`, and ORCA's "poppable" pin joints dislocate rather than
break `orca_hand_2025`. Both are mechanical fuses, and both are cheaper than the force
transparency 1X buys with low gear ratios `onex_neo_hand_2026`. RUKA states that "most repairs
take under 20 minutes" `ruka_2025` and ORCA that one person with no prior experience assembles
it "in less than eight hours" `orca_hand_2025`, while Shadow releases controller source and
schematics only under a non-disclosure agreement `shadow_dexterous_hand_2005`. What fails is
rarely the motors. ORCA's durability run found silicone skin degrading on two fingertips after
about 2,000 to 4,000 grasp cycles and sensor wires snapping on three after about 4,500 to 7,000
`orca_hand_2025`. The sensing wore out an order of magnitude sooner than the hand.

### Table 2. Hands that can be obtained

| hand | maker | DoF | act. DoF | actuation | weight g | tip force N | tactile | price USD | open HW | status | source | corpus methods using it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `shadow_dexterous_hand_2005` | Shadow Robot Company | 24 | 20 | tendon-driven, motors in the forearm (20 Smart Motor nodes, Maxon motors, PWM) | 4300 |   | Shadow Tactile Fingertips (STF): 17x3 DoF Hall-effect taxels, 1000 Hz, uncalibrated; up t… |   | no | sold | datasheet | 21: `asymdex_2024`, `bidexgrasp_2026`, `bimangrasp_2024`, … |
| `sharpa_wave_2026` | Sharpa Robotics (Sharpa Pte Ltd) | 22 | 22 |   | 1300 | 20 N / 12 N (two unlabelled spec-table columns, likely two product configurations) | 'Dynamic Tactile Array' (DTA), camera-type array at the fingertip: resolution 240x240 / 6… |   | no | sold | vendor page | 6: `dexteleop0_2026`, `egoscale_2026`, `metis_2025`, … |
| `proception_prohand_2026` | Proception Inc (YC W25) | 22 |   | tendon-driven, motors pull cables to move the fingers |   |   | integrated skin-like sensors detecting contact, supporting grip control; same 'sensor ski… |   | no | sold | press | 0 |
| `bidexhand_2025` | Zhengyang Kris Weng, Center for Robotics and Biosystems, Northwestern University | 21 | 16 | cable-driven, N-configuration tendon routing (FeeTech servos, endless-loop antagonistic p… |   | 2.14 | none mentioned |   | yes | open-source | paper | 0 |
| `wuji_hand_2025` | Wuji Technology (founded 2019) | 20 | 20 | direct-drive rotary, backdrivable |   |   | 'Multi-Axis Force/Torque Fingertip Sensing' confirmed present; no type, count or range gi… |   | no | sold | vendor page | 2: `toporetarget_2026`, `unidex_2026` |
| `ruka_v2_2026` | Xinqi (Lucas) Liu, Ruoxi Hu, Alejandro Ojeda Olarte, Zhuoran Chen, Kenny Ma, Charles Chen… | 20 | 16 | tendon-driven, forearm-mounted actuators; decoupled parallel 2-DoF wrist via a passive sp… |   |   | optional e-flesh fingertips (magnetic touch-sensing form factor); not part of the base de… | 1500 | yes | open-source | paper | 0 |
| `tesollo_dg5f_2024` | Tesollo Inc. (Incheon HQ, Gwangmyeong R&D/factory) | 20 | 20 | one integrated actuator per joint ('high-torque actuation', absolute encoder); page does… | 1763 |   | none standard; optional fingertip sensors (6-axis F/T, 3-axis force, or tactile) availabl… |   | no | sold | vendor page | 0 |
| `unitree_dex5_2025` | Unitree Robotics (Yushu Technology Co., Ltd.) | 20 | 16 | in-joint geared motor ('hollow-cup motor' + high-precision encoder + low-damping small-cl… | 1100 | 10 | Dex5-1: none. Dex5-1P: 94 pressure sensors per hand (2x5 palm + 2x3x5 finger pad + 2x3x5… |   | no | sold | datasheet | 0 |
| `orca_hand_2025` | Clemens C. Christoph, Maximilian Eberlein, Filippos Katsimalis, Arturo Roberti, Aristotel… | 17 | 17 | tendon-driven (antagonistic fishing-line tendon pairs per joint); wrist uses a GT2 timing… | 1200 | 19.6 | yes: FSR-based binary tactile sensing on all 5 fingertips (RP-C7.6-ST), absolute detectio… |   | yes | open-source | paper | 0 |
| `leap_hand_2023` | Kenneth Shaw, Ananye Agarwal, Deepak Pathak, Carnegie Mellon University | 16 | 16 | direct-drive (Dynamixel servos, e.g. XC330-M288), joint velocity ~8 rad/s | 595 | 19.5 | none (future work only: 'we plan to develop and integrate LEAP Hand with low-cost touch s… | 2000 | yes | open-source | paper | 11: `bidex_teleop_2024`, `bidexhd_2024`, `cross_embodiment_world_models_2025`, … |
| `allegro_hand_v4_2016` | Wonik Robotics Co. Ltd. (Seoul, South Korea); earlier versions 1.0/2.0 made by SimLab Co.… | 16 | 16 |   |   |   | none |   | no | sold | vendor page | 35: `anyrotate_2024`, `anyteleop_2023`, `asymdex_2024`, … |
| `ruka_2025` | Anya Zorin, Irmak Guzey, Billy Yan, Aadhithya Iyer, Lisa Kondrich, Nikhil X. Bhattasali,… | 15 | 11 | tendon-driven (11 Dynamixel actuators in the forearm: XM430-W210T for the thumb, XL330-M2… |   | 2.74 | none (stated limitation: 'lacks tactile sensing') | 1300 | yes | open-source | paper | 0 |
| `robotera_xhand1_2024` | ROBOTERA | 12 | 12 | gear-driven force-controlled joint modules per finger segment, back-drivable | 1100 |   | tactile/force sensors on every fingertip confirmed present (senses contact, force, temper… | 14000 | no | sold | vendor page | 8: `cross_embodiment_world_models_2025`, `deximit_2026`, `dexmachina_2025`, … |
| `shadow_dex_ee_2024` | Shadow Robot Company, in collaboration with Google DeepMind | 12 |   |   | 4100 |   | stereo camera-based fingertip tactile sensors (hundreds of taxels each); multi-taxel 3-Do… |   | no | sold | vendor page | 1: `demostart_2024` |
| `inspire_rh56dfx_2023` | Beijing Inspire Robots Technology Co., Ltd. | 12 | 6 |   | 540 | 10 N (fingers), 15 N (thumb); force resolution 0.50 N | none (this variant is the 'without tactile sensors' table; a tactile FTP variant exists p… |   | no | sold | vendor page | 19: `ace_teleop_2024`, `articulated_tools_inhand_2025`, `being_h05_2026`, … |
| `brainco_revo2_2025` | BrainCo Inc. | 11 | 6 |   | 383 | pinch >=15 N; full fist grip >=50 N | Touch variant only: multi-dimensional fingertip tactile module with 'Tactile Adaptive Con… |   | no | sold | datasheet | 1: `bidexgrasp_2026` |
| `agibot_omnihand_2025` |   |   |   |   |   |   |   |   |   |   | unavailable | 1: `clutterdexgrasp_2025` |
| `linkerbot_l20_2025` | LinkerBot (SDK author 'CHIUS INC') |   |   |   |   |   | L10/L20: per finger 4 channels (normal force, tangential force, tangential direction, pro… |   | no | sold | vendor page | 1: `being_h05_2026` |
| `psyonic_ability_hand_2021` | PSYONIC (San Diego, CA, USA) |   | 6 | linkage (repo file/function names indicate a four-bar finger linkage; not stated on the v… |   |   | 30 touch sensor values streamed (FSR-based per API and URDF 'no_fsr' variant); per-finger… |   | no | sold | vendor page | 7: `ace_teleop_2024`, `asymdex_2024`, `bunny_visionpro_2024`, … |
| `dexhand_open_source_2023` | Rob Knight, The Robot Studio (design); electronics/firmware/ROS 2 by Trent Shumay, IoT De… |   | 16 | tendon (fishing line, Sufix 832 80lb / 0.8mm kiteline); Emax ES3301/ES3302/ES3351/ES3352… |   |   | none mentioned | 300 | yes | open-source | vendor page | 0 |

*20 rows; 56 of 260 cells (21%) are values no source stated.*

## 3.2 The hands the research literature actually runs on

![fig2_hands](figures/fig2_hands.svg)

Two hand designs, one from 2005 and one from 2016, carry 52 of the 103 method rows that name a
hand at all. Figure 2 counts, per hand, the method papers whose own experiments use it. Of 110
method rows, 103 name a hand. The Allegro accounts for 35, Shadow for 21, the Inspire RH56 family
for 19, a parallel-jaw gripper for 12 and LEAP for 11. Seventy-four of the 103 name an Allegro, a
Shadow or Adroit model, LEAP or an Inspire.

The Allegro's position is the uncomfortable part. It is a 16-joint hand with no tactile sensing,
and its product page at allegrohand.com/v4 returned HTTP 404 while the Wonik wiki timed out
`allegro_hand_v4_2016`. Everything Table 2 confirms about the most-used hand in the corpus comes
from its ROS driver: 16 joints, four fingers, a torque interface, a 333 Hz CAN clock, 12 V. Its
weight, joint torque, payload and price have no reachable source. The field's most common
platform cannot be specified from a page a reader can open.

Concentration would matter less if the hand did not move the result, and it does. On the same
simulated cube rotation, LEAP reaches 0.2288 rad/s against the Allegro's 0.0828 rad/s, which the
LEAP authors attribute to supporting the cube from the sides without releasing it
`leap_hand_2023`. RUKA reports a 2.74 N pinch against the Allegro's 1.60 N over three trials per
test `ruka_2025`. A method compared only on Allegro hardware is compared at one point in a space
where a single axis moves the headline number by two or three times. Two further patterns follow
in the figure: Inspire, XHand and Sharpa take 33 method rows between them and none predates 2023
here, while ORCA, RUKA, Ruka-v2, BiDexHand, DexHand, the Tesollo DG-5F and the Unitree Dex5 take
none at all.

## 3.3 Open hardware and the collapse in cost

The costs are quoted verbatim because they are quoted on inconsistent bases at the source. LEAP
Hand: "LEAP Hand is low-cost and can be assembled in 4 hours at a cost of 2000 USD from readily
available parts", alongside a separate "commodity 3D printer that costs around 200 USD" and a
two-day print `leap_hand_2023`. RUKA: "The total cost of the raw materials needed, excluding
tools (a 3D-printer and soldering iron), is under $1,300 USD. There is also a $500 and $900
version of RUKA with varying Dynamixel motors" `ruka_2025`. Ruka-v2: "The total material cost of
Ruka-v2 is under $1,500" `ruka_v2_2026`. LEAP Hand v2 Advanced: "a dexterous, $3000, simple
anthropomorphic hybrid rigid-soft hand" `leap_hand_v2_adv_2025`. DexHand: "The hand is made
entirely by 3dprinting with additional total cost of components required for the hand around
$300 USD" `dexhand_open_source_2023`. ORCA is "built for a material cost below 2,000 CHF"
`orca_hand_2025`, stated only in Swiss francs, which is why Table 2's price column is empty for
ORCA rather than silently converted.

Two of the six have no cost figure at all. The Faive Hand paper states no bill of materials for
itself and only names a comparison, "a steep price tag of 110k GBP as quoted from their website",
for the Shadow Hand `faive_hand_2023`. BiDexHand's README points at a `BOM.md` that the parsed
repository does not contain, and no figure appears in its paper either `bidexhand_2025`. Neither
hand should carry an inferred price.

For scale, RUKA's comparison table lists the Allegro at $15,000 and the Shadow Hand at $100,000
`ruka_2025`, and Ruka-v2's lists the Sharpa Wave at about $50K under a footnote saying it is
"reported by third-party sources only" `ruka_v2_2026`. Those are secondhand figures in a hardware
paper and belong to those tables, not to the vendors. The only vendor-adjacent price in Table 2
is the 14,000 USD a tracker lists for the XHAND1 `robotera_xhand1_2024`.

The collapse is real, from a six-figure hand to a $300 one inside a decade, and it has barely
moved the literature. Fourteen of the 103 hand-naming method rows use an open-hardware hand, and
11 of those are LEAP. What the cheap hands give up is sensing. LEAP has none and names touch
sensors as future work `leap_hand_2023`, RUKA states its design "lacks tactile sensing"
`ruka_2025`, Ruka-v2 offers e-flesh fingertips outside the base design `ruka_v2_2026`, and
BiDexHand's sources never mention touch `bidexhand_2025`. ORCA is the exception, with binary FSR
fingertips whose detection threshold was measured "as low as 0.05 N" `orca_hand_2025`.

## 3.4 Announced and unreleased hands

Behind Table 3's rows sit three kinds of evidence, and conflating them is how a DoF figure with
no source ends up in a survey.

One row rests on vendor prose carrying numbers. 1X's page dated 9 July 2026 claims 25 degrees of
freedom, 22 in the fingers and palm plus three at the wrist, quasi-direct-drive tendons at
roughly 5:1 to 15:1, peak torques of 3.5 Nm at the thumb CMC and 2.6 Nm at the finger MCP,
distal flexion forces to 45 N, IP68, and capacity "to produce 10,000 hands this year"
`onex_neo_hand_2026`. No datasheet sits behind that prose, and every capability the page names is
a video with no success rate, trial count or task definition.

Video is the second kind of evidence, and it carries no numbers. Tesla's Optimus Gen 2 was shown
on 13 December 2023 with a feature list reading "Faster, 11-DoF brand-new hands" and "Tactile
sensing on all fingers", over an egg pick-up with a fingertip force overlay
`tesla_optimus_hand_2025`. Sanctuary's release links an in-hand manipulation video with no task
list and no trial counts `sanctuary_phoenix_hand_2024`. Clone Robotics' whole evidence is a
teleoperated desk video of 15 November 2025, and the press item notes Clone "hasn't released a
full demo of the robot with the hand" `clone_robotics_hand_2024`.

Everything else is press or bibliography assertion. Tesla's V3 hand is known here only through a
Teslarati paraphrase of three patents filed in October 2024, because the USPTO PDF parsed empty
and the Wikipedia page returned HTTP 404 `tesla_optimus_hand_2025`. The repeated 22-DoF figure is
that article's arithmetic of four DoF on each of five fingers plus two at the wrist, and the
50-actuator figure is a bibliography claim. As manufacturer statements, both have no reachable
source.

Figure 03 is the clearest case of a number outrunning its source. The launch page
figure.ai/news/introducing-figure-03 returned HTTP 404, leaving a third-party tracker as the only
stored source `figure_03_hand_2025`. The repeated 16 DoF per hand and roughly 3 g of fingertip
sensitivity have no reachable source. Where the tracker does speak it contradicts them, listing
"Degrees of freedom, hands | 20" and "Number of fingers | 10" without saying whether either is
per hand or for the pair. The one fact both sources share is palm cameras, which are vision, not
tactile.

Boston Dynamics is the counterexample to five fingers, and its own CES blog of 5 January 2026
contains no hand content at all. The description comes from trade press: "a four-digit
gripper—three fingers and an opposable thumb—equipped with tactile sensing in the fingers and
palms" `boston_dynamics_atlas_hand_2026`. No DoF figure is stated, and the 7-DoF, 7-actuator
figure circulating for the 2025 three-finger hand has no reachable source.

Xiaomi shows a vendor-relayed number contradicting the circulating one. The 36kr page fetched
empty, leaving an Interesting Engineering article of 30 March 2026 relaying a WeChat post
`xiaomi_cyberone_hand_2026`. It says the redesign "increases active degrees of freedom by 83
percent" without giving an absolute count, and reports a 90.2 percent nut-fastening success rate
in a 76-second factory cycle. The figures in circulation are 64 percent and 98 percent, and both
contradict the only readable source. The hand's own DoF count has no reachable source.

Proception's ProHand belongs in Table 2, since a Y Combinator post and a TechCrunch article of
29 June 2026 state 22 degrees of freedom, tendon actuation and "integrated skin-like sensors",
with the first batch shipping that week `proception_prohand_2026`. Beyond the 22, nothing is
specified. Daxo's Muscle V0 is known only through the catalogue post, since
daxo-robotics.com returned HTTP 404, and the circulating "108 artificial muscles" and roughly
$1,200 prototype cost have no reachable source against that post's 120 actuators
`daxo_muscle_v0_2025`. AgiBot's OmniHand is worse: both store.agibot.com URLs returned HTTP 404
and the stored page holds no product text, so the circulating 16 DoF, 500 g, "400+ touch points"
and RMB 9,800 price all have no reachable source `agibot_omnihand_2025`. One method paper
nonetheless runs on an "AgiBot dexterous hand" `clutterdexgrasp_2025`, so the hand exists, is
used, and cannot be specified.

ByteDance's ByteDexter breaks the pattern. It has no vendor page here and no Table 3 row, because
its evidence is a technical report: 21 DoF per hand, linkage-driven, with piezoresistive tactile
fingertips, 16 of them present in the policy's action vector `gr_dexter_2025`. The Sharpa Wave is
the best-specified vendor page in the corpus and still ambiguous, because its spec table has two
unlabelled columns, so fingertip force reads "20 N | 12 N" and the fingertip array reads 240x240
at 180 fps or 60x60 at 30 fps `sharpa_wave_2026`.

The same divergence reaches the hands that are sold. Tesollo's page gives 1,763 g, Modbus and
Ethernet, while two published survey tables round the weight to 1.7 and 1.8 kg and one names
EtherCAT, which the page does not `tesollo_dg5f_2024`. The XHAND1 tracker page states no
fingertip force, a survey table gives 15 N and the bibliography gives an 80 N grip
`robotera_xhand1_2024`.

### Table 3. Hands announced but not purchasable

| hand | maker | DoF | act. DoF | actuation | weight g | tip force N | tactile | price USD | open HW | status | source | corpus methods using it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `clone_robotics_hand_2024` | Clone Robotics | 27 |   | hydraulic artificial muscle ('Myofiber' — small water-filled tubes that contract when pre… | 907 |   | pressure pads in the palm detect grip firmness (count not given); 70 inertial sensors tra… |   | no | internal-only | press | 0 |
| `onex_neo_hand_2026` | 1X Technologies | 25 | 25 | quasi-direct-drive tendons via the '1X Tendon Drive' at low gear ratios (~5:1-15:1); moto… |   | 45 | high-resolution tactile sensing across fingertips and finger surfaces (normal force, cont… |   | no | announced | vendor page | 0 |
| `tesla_optimus_hand_2025` | Tesla | 22 |   | V3: tendon-driven from forearm actuators, three tendons per finger through a crosstalk-ma… |   |   | Gen 2: tactile sensing on all fingers, demonstrated matching contact location and force i… |   | no | prototype | press | 0 |
| `sanctuary_phoenix_hand_2024` | Sanctuary AI (Sanctuary Cognitive Systems Corporation) | 21 |   | hydraulic, 'unique miniaturized hydraulic valves' |   |   | not in the press release text; sidebar-only headlines mention new touch/tactile sensors a… |   | no | internal-only | press | 0 |
| `leap_hand_v2_adv_2025` | Kenneth Shaw, Deepak Pathak, Carnegie Mellon University | 21 | 17 | tendon (PIP/DIP coupled by a single tendon per finger); motor type not stated |   |   | none mentioned | 3000 | yes | announced | vendor page | 2: `bidex_teleop_2024`, `dexwild_2025` |
| `figure_03_hand_2025` | Figure AI | 20 |   |   |   |   | not stated on page for the hand itself; palm cameras in each hand are vision, not tactile |   | no | prototype | vendor page | 0 |
| `ilda_hand_2021` | Ajou University, Korea Institute of Machinery & Materials, Korea University | 20 | 15 | linkage-driven, direct linear drive (3 Maxon DCX8M motors per finger with GPX8 16:1 gearb… | 1100 | 34 | 6-axis F/T sensor per fingertip (5 total), force resolution 62 mN, range +/-35 N; not a d… |   | no | prototype | paper | 0 |
| `pisa_iit_softhand_2014` | Centro E. Piaggio, University of Pisa and IIT (Catalano, Grioli, Farnioli, Serio, Piazza,… | 19 | 1 | tendon-driven adaptive synergy, single motor via differential gears (6 W Maxon RE-max21,… |   |   | none (motor encoder only; a padded work glove supplied contact compliance during experime… |   | no | prototype | paper | 0 |
| `faive_hand_2023` | Yasunori Toshimitsu, Benedek Forrai, Barnabas Gavin Cangan, Ulrich Steger, Manuel Knecht,… | 16 | 11 | tendon-driven, rolling-contact joints (16 Dynamixel XC330-T288-T servos, 6 antagonistic p… | 1100 |   | none on the physical hand; a simulated 'fingertip force' (15-dim, critic-only/privileged)… |   |   | prototype | paper | 1: `graspxl_2024` |
| `paxini_dexh13_2024` | PaXini Tech |   |   |   |   |   | 1,140 ITPU multidimensional tactile processing units (press-release claim; unclear if PX-… |   |   | announced | press | 0 |
| `boston_dynamics_atlas_hand_2026` | Boston Dynamics |   |   | electric (robot is fully electric); specific hand mechanism not stated |   |   | tactile sensing in the fingers and palms, confirmed present; type and count not stated |   | no | prototype | press | 0 |
| `daxo_muscle_v0_2025` | Daxo Robotics |   | 120 | ultra-redundant tendon-driven; compliant structure with no rigid joints, flexible materia… | 750 |   |   |   |   | prototype | unavailable | 0 |
| `xiaomi_cyberone_hand_2026` | Xiaomi |   |   | motors located in the hand (compact motors generate heat requiring liquid cooling); no te… |   |   | full-palm tactile sensing, area ~8,200 sq mm, detects pressure and contact across the who… |   | no | prototype | press | 0 |

*13 rows; 49 of 169 cells (28%) are values no source stated.*

## 3.5 Tactile sensing as part of the hand

DIGIT set the cost floor. It is 20 by 27 by 18 mm, weighs about 20 g, streams 640x480 at 60 fps,
and its paper states a "total estimated manufacturing cost is approximately 15 USD per sensor ...
when manufactured in a batch of 1000" `digit_2020`. Durability was as much the contribution as
price: its gel degraded 0.3 percent over 15 abrasion passes, against 805 and 918 percent for the
two gels compared with it.

Digit 360 is the same lineage at a different operating point, claiming about 8.3 million taxels,
spatial features to 7 um, normal and shear force resolution of 1.01 mN and 1.27 mN, and
on-device processing that cuts event-to-action latency from 6 ms to 1.2 ms `digit360_2024`. It is
also not for sale. Units go at no charge to selected researchers, and no corpus paper's parsed
text names the sensor.

XELA's uSkin is the non-camera alternative and the one that bolts onto hands the field already
uses. Its curved fingertip kit for the Allegro V4 and LEAP carries 30 three-axis sensing points,
a full Allegro integration reaches 368, resolution is 0.1 gram-force, and the fingertip kit runs
at 275 Hz `xela_uskin_2020`. The 500 Hz figure often quoted belongs to the product family, not
the curved fingertip. One corpus paper names it, `sparsh_2024`.

Sparsh is the layer above. Its self-supervised encoders are pre-trained on 462.7k tactile images
spanning DIGIT, GelSight 2017 and GelSight Mini, and frozen Sparsh features beat matched
end-to-end models by 95.1 percent on average when both see 33 to 50 percent of the labels
`sparsh_2024`. Its own bead-maze policies never complete the maze on the real robot. It also
reports DIGIT at 320x240 where DIGIT's table says 640x480, which neither source resolves.

The usage number is the one to keep. Eight of 110 method rows feed a physical tactile signal into
a policy: `anyrotate_2024`, `articulated_tools_inhand_2025`, `dexteleop0_2026`, `dexumi_2025`,
`hato_visuotactile_2024`, `penspin_2024`, `robot_synesthesia_2023` and `rotateit_2023`.
Thirty-five of the 110 mention tactile somewhere. Almost none of the eight uses a
high-resolution sensor. PenSpin uses 20 binary contacts, five per fingertip `penspin_2024`, and
Robot Synesthesia uses 16 force-sensing resistors read as binary `robot_synesthesia_2023`. Two
papers exclude touch deliberately, HORA reporting rotation "even without the usage of vision and
tactile sensing" `hora_2022`, and ORCA's authors dropped it from their reinforcement learning
"due to the additional complexity involved in accurately modeling them" `orca_hand_2025`. Taxel
counts have risen by three orders of magnitude while the policies consuming them have stayed at
binary contact.

## 3.6 What is sold against what is published on

The bottom rows of Figure 2 carry the finding. None of the nine company-announced hands in
Table 3 appears in a single method row. Tesla, Figure, 1X, Sanctuary, Boston Dynamics, Xiaomi,
Clone, Daxo and PaXini together account for zero of the 110 method papers' experiments. The four
research prototypes in Table 3 are not in that position, since the Faive Hand and LEAP Hand v2
Advanced account for three method rows between them `graspxl_2024`, `bidex_teleop_2024`,
`dexwild_2025`. The clean claim is about company hands, not about Table 3 as a whole.

Table 3's emptiness is measurable and part of the same finding. Twenty-eight percent of its cells
are values no source stated, against 21 percent for the hands that can be bought. The hands with
the highest advertised DoF counts have the least specification behind them.

The one hand that crosses the gap crosses it because its maker published rather than announced.
ByteDexter reaches a method row through a ByteDance technical report with real-robot success
rates `gr_dexter_2025`, not through a product page. That mechanism is available to every vendor
in Table 3 and none of them has used it.

The gap runs the other way too, and the last column of Table 2 shows it. Hands that are sold,
documented and cheap go unused: the Unitree Dex5 with 94 pressure sensors on its P variant
`unitree_dex5_2025`, the fully actuated Tesollo DG-5F `tesollo_dg5f_2024`, ORCA `orca_hand_2025`,
RUKA `ruka_2025`, Ruka-v2 `ruka_v2_2026`, BiDexHand `bidexhand_2025` and DexHand
`dexhand_open_source_2023` take zero method rows each. A reader choosing a hand on this corpus's
evidence has two well-precedented options, an Allegro or an Inspire, and a third in LEAP if
eleven papers is enough. Everything else is a press release or a hand nobody has published a
result on.

# 4. Simulators and the physics underneath

## 4.1 What a dexterous simulation must get right

The clearest demonstration that hands are the hard case came from a benchmark that was not about
hands. Erez et al. built a 35-DOF arm modelled on the Shadow Hand, closed it around a capsule with
fixed spring-dampers, and asked five engines for the largest timestep at which the object was
still in the hand at the end of the run. MuJoCo held the grasp at 16 ms, PhysX at 2 ms, ODE at
0.25 ms and Bullet at 0.03 ms, a spread of a factor of 500
(`physics_engine_comparison_2015`, Sec. IV-D). On a falling 25-DOF humanoid the same engines
differ by about a factor of four in speed, and on a pile of 27 capsules the ranking inverts. The
grasp is the test that separates them. The authors wrote MuJoCo and disclose it, and their
timesteps are log-spaced, so each is good only to a factor of two.

A grasp is hard for nameable reasons. It is many contacts at once, all persistent, all near
stiction, on an object much lighter than the mechanism holding it. Persistence and multiplicity
make the problem hyperstatic, and Le Lidec et al. show that per-contact solvers of the projected
Gauss-Seidel family, and RaiSim's, then inject spurious internal jamming forces at stiction that
vanish only once the object slides. The mass ratio makes it ill-conditioned, and in their
stacked-cube test at a 10^3 to 10^-3 kg ratio those same per-contact methods fail to converge.
Global methods with proximal regularisation stay robust in both cases
(`contact_models_comparison_2023`, Sec. IV-A). Locomotion is forgiving by comparison. In their MPC
task on a Solo-12 quadruped on flat ground the contact model and solver choice "hardly affects"
the tracked base velocity, and only on rough, slippery terrain do RaiSim and CCP deviate. A
walking robot makes and breaks a few contacts against ground far heavier than itself. A hand does
neither.

Speed enters by the same door, because contact resolution is where the cost is, and on MJX it does
not even scale with the contacts that exist. MuJoCo Playground reports that contact time scales
with the number of possible contacts rather than the active ones, because JAX requires static
shapes, which is why its tasks carry hand-tuned `max_contact_points` and `max_geom_pairs`
overrides (`mujoco_playground_2025`, Sec. VI). For a hand the bound is set for the worst case.

Figure 3 sets out the stages of one simulation step and marks where the engines used for hands
diverge. Two stages matter below: contact generation, where convex decomposition replaces the mesh
the renderer draws, and the solver, where a fixed iteration budget leaves a stiff contact
unconverged and therefore resolved as overlap.

## 4.2 Contact models and solvers, engine by engine

![fig3_sim_step](figures/fig3_sim_step.svg)

Table 4 is the engine-by-engine comparison, one row per simulator, built only from what a note
confirmed. Le Lidec et al. supply the taxonomy that organises it, checking each formulation
against the Signorini condition, Coulomb's law, and the maximum dissipation principle. Linear
complementarity, the family used by Bullet, ODE and PhysX, satisfies Signorini alone, because
linearising the friction cone to a pyramid biases friction toward its corners. The cone
complementarity problem satisfies the other two but relaxes Signorini, so contact acts at a
distance of size Δt·µ·‖c_T‖ and their dragged cube slides above the floor. The full nonlinear
problem satisfies all three and is non-convex (`contact_models_comparison_2023`, Table II).

MuJoCo sits outside that taxonomy deliberately. Its contact is soft, convex and
complementarity-free, and penetration is a state variable rather than an error: the violation
distance is driven by a critically damped stabiliser, and for an object resting under gravity the
steady-state depth has a closed form independent of the object's mass
(`mujoco_convex_contact_2014`, Sec. V). The original paper says why non-penetration is a cost and
not a constraint, "otherwise the inverse dynamics could not be defined for trajectories that
happen to have penetration" (`mujoco_2012`, Sec. II-D). The model is built to stay well-defined
while the bodies overlap. Le Lidec et al., who compete with it, call that compliance a "numerical
trick designed to circumvent the issues due to hyper-staticity or ill-conditioning at the cost of
impairing the simulation". Drake's SAP takes the convex middle, bounding penetration at about
2.5×10^-5 m for a point mass at δt = 10^-2 s (`castro_sap_contact_2021`).

The first of two concrete measurements comes from the other end. Dojo solves a hard-contact
nonlinear complementarity problem with an exact second-order friction cone, by an interior-point
method converging within 15 iterations. Its Table II drops an Atlas humanoid and reports
foot-floor penetration against the timestep. MuJoCo penetrates −28 mm at Δt = 0.01 s and −46 mm at
Δt = 0.001 s, and fails outright at Δt = 0.1 s. Dojo records +1×10^-12 mm at Δt = 0.1 s and
+8×10^-6 mm at Δt = 0.001 s, so its feet stay above the floor at every step size tested
(`dojo_2022`, Sec. V-A). That is one scenario, on the authors' own configuration of the competing
engine, and Dojo demonstrates no dexterous hand anywhere in the paper. The price is in its
Table V, where MuJoCo is fastest on every system tested, 0.335 s against Dojo's 1.159 s on a
Franka Panda over 1000 steps. Read Erez's grasp table backwards and the trade is priced: tens of
millimetres of overlap on a drop test is what buys the 16 ms timestep that holds a grasp where
Bullet needs 0.03 ms.

The GPU era moved that knob rather than removing it. ComFree-Sim resolves contact in closed form
in the dual cone of the friction cone, with no complementarity solve, so penetration becomes an
explicit tuning parameter and the paper reports it. On a drop test of convex primitives about 5 cm
across at dt = 0.002 s, averaged over all detected contacts, MuJoCo Warp penetrates 1.7 ± 4.9 mm
and ComFree-Sim ranges from 3.9 ± 6.9 mm to 0.9 ± 1.5 mm as its stiffness and damping are raised.
Millimetres, on primitives the size of a fingertip, in the GPU backend that both MuJoCo Playground
and Newton build on.

That brings Table 4's most important column. Two of the 15 engines report a penetration depth
exposed to the user, Dojo and ComFree-Sim, and both are engines whose paper is about contact
accuracy. Four are recorded as not exposing it: Brax, Isaac Gym, Isaac Lab and Orbit. Nine rows
are blank, meaning no parsed source stated it either way. The word "penetration" appears nowhere
in the Isaac Gym paper, whose tensor API exposes net contact force per rigid body and no depth,
and Isaac Lab's contact sensor reports force, duration and an average contact point but defines no
contact-quality metric. Those two simulators carry 41 of the 110 method papers in this corpus. The
depth is created by the solver on every step and is not handed to the user.

A policy will use what the user cannot see. DexTrack's released configs set PhysX's
`max_depenetration_velocity`, which bounds how fast overlapping bodies are pushed apart, to either
10.0 or 1000.0 depending on the task variant, with no explanation in the paper or in a config
comment. The paper defines a maximum hand-object penetration depth, applies it only to its input
kinematic references, and presents tolerance of "severe hand-object penetrations" as evidence of
robustness (`dextrack_2025`, App. B). TopoRetarget is the counterexample, reporting max penetration
depth and the share of frames above 2 mm over 25 ContactPose grasps: 1.07 mm and 0.00% for its own
retargeting, against 20.12 mm and 84% of frames for Mink and 22.22 mm and 96% for GeoRT
(`toporetarget_2026`, Table 1). Those are retargeted reference trajectories, which are placement
rather than simulated physics, and they are not re-measured after RL tracking. The one method in
the corpus that measures penetration carefully measures it on the input.

The rest of Table 4 is largely empty, and the emptiness is a result. Sixty-eight of its 165 cells,
41 percent, are values no parsed source stated. Three of 15 engines state a default physics
timestep, four state a solver iteration count, and seven ship any dexterous hand at all.

### Table 4. Simulators and physics engines

| engine | contact model | solver | iters | diff. | GPU | dt s | penetration exposed | throughput | hands shipped | licence |
|---|---|---|---|---|---|---|---|---|---|---|
| `brax_2021` | rigid bodies in maximal coordinates; naive/quadratic-scaling pairwise collision detection… | not LCP-based; velocity-level collision updates with Baumgarte stabilization (inspired by… |   | yes | yes |   | no | millions of simulation steps/sec on a single accelerator (e.g. MuJoCo Ant equivalent on a… | synthetic 4-fingered claw hand (Grasp environment, non-commercial, from-scratch morpholog… |   |
| `comfree_sim_2026` | complementarity-free, analytical (closed-form) contact resolution in the dual cone of the… | no complementarity solve; a 4-kernel GPU pipeline (Algorithm 1: smooth-velocity predictio… | none (closed-form, no per-step iterative solve) |   | yes | 0.002 | yes | AMD 32-core CPU + NVIDIA RTX 4090 GPU: ~3x faster (near-linear vs. MJWarp's superlinear)… |   |   |
| `dojo_2022` | hard-contact nonlinear complementarity problem (NCP) with an exact nonlinear (second-orde… | custom primal-dual interior-point solver (Algorithm 2), based on Mehrotra's predictor-cor… | converges within 15 iterations for all three robots tested in the convergence study (Sec.… | yes | no |   | yes | Intel Core i9-10885H, 32GB RAM, CPU only (no GPU support; described as future work). Tabl… |   |   |
| `genesis_2024` | Constraint-based rigid solver (equality/inequality constraints, plus an explicit noslip()… | ConstraintSolver with Newton-style line-search iterative resolve (linesearch.py) and cons… |   | yes | yes |   |   |   | Shadow Hand |   |
| `isaacgym_2021` | Rigid-body contacts via PhysX; contact geometry can be primitive shapes or meshes loaded… | Temporal Gauss-Seidel (TGS) solver (Sec. 3, ref. 18), not classic PGS/LCP: folds sub-step… |   | no | yes | 0.008333333333333333 | no | Shadow Hand: 150,000 parallel environment steps/sec at 16,384 environments, single NVIDIA… | Shadow Dexterous Hand, Allegro Hand, TriFinger (3-finger, 9-DoF manipulator; the paper it… |   |
| `isaaclab_2025` | Rigid contacts by default via PhysX 5 (SDF collisions, Featherstone articulation solver,… | NVIDIA PhysX 5's internal rigid-body/Featherstone-articulation solver, used as-is; Factor… |   | no | yes |   | no | DextrAH teacher task (state-based grasp-and-lift): over 900,000 FPS training throughput w… | KUKA Allegro hand (first-party dexterous suite, Sec. 7.2.3), ShadowHand (third-party Gras… |   |
| `maniskill3_2024` | PhysX (via SAPIEN) rigid-body contacts on GPU; no statement of convex-vs-mesh contact gen… | PhysX (via SAPIEN), used as-is; no LCP/PGS/TGS/Newton solver-algorithm name given. Benchm… | 4 position / 0 velocity iterations (benchmarked cartpole configuration only, App. XI-A);… |   | yes |   |   | Up to 30,000+ FPS (RGBD+segmentation) on a single RTX 4090 GPU, environment count for tha… | Allegro Hand (incl. touch-sensor variant, AllegroHandRightTouch), Ability Hand, Inspire H… | Apache-2.0 |
| `mujoco_2012` | soft, convex velocity-stepping contact; three interchangeable solvers replace the standar… | implicit-complementarity solver (customized non-smooth Newton method, most accurate); con… |   | no | no |   |   | up to ~400,000 dynamics evaluations/sec on a 12-physical-core machine (2x 6-core Intel X5… |   |   |
| `mujoco_convex_contact_2014` | soft, convex, complementarity-free; a unified impulse vector covers joint dry friction, j… | GPGS (generalized projected Gauss-Seidel, described as the authors' own unpublished-at-th… | 5 and 50 (both tested, Fig. 3, Sec. VI-B) | no | no | 0.01 |   | single-core Intel i7-3930K (Windows 7): forward dynamics of a 27-dof humanoid with 10 con… |   |   |
| `mujoco_warp_2025` | MuJoCo's native solref/solimp-parameterized soft-constraint contact model ported to Warp… | MuJoCo's default (implicit CCP-style) solver and Newton constraint solver (via a 'newton'… |   | no | yes |   |   |   |   |   |
| `newton_2025` | Solver-dependent: MuJoCo-style soft-constraint (solref/solimp-style) contact via SolverMu… | Multi-solver architecture: SolverMuJoCo (wraps MJWarp), SolverKamino (Proximal-ADMM + DVI… |   | yes | yes |   |   |   | Allegro Hand |   |
| `orbit_2023` | PhysX SDK 5 signed-distance-field (SDF) collision checking for rigid bodies (handles non-… | PhysX SDK 5's internal rigid-body and FEM solvers, used as-is; no LCP/PGS/TGS, Newton, or… |   | no | yes |   | no | 125,000 FPS physics-only ceiling (no env count stated); ~10x rigid-body throughput vs. CP… | Allegro hand |   |
| `pybullet_2016` |   |   |   |   | yes |   |   |   |   |   |
| `raisim_2018` |   |   |   |   |   |   |   |   |   | requires a valid license and activation key from the RaiSim Tech website; the repo README… |
| `sapien_2020` | Rigid-body contact with convex-decomposed collision meshes (PhysX 4.1); three joint syste… | PhysX 4.1's internal rigid-body solver, used as-is; no LCP/PGS/TGS name or iteration coun… |   |   | no |   |   | ~5000 Hz engine, ~700 Hz OpenGL render; single-instance CPU-physics figure with no parall… |   |   |

*15 rows; 68 of 165 cells (41%) are values no source stated.*

## 4.3 The GPU-parallel turn

Isaac Gym set the pattern. Physics, observations, rewards and actions stay on the GPU, and PhysX
uses a Temporal Gauss-Seidel solver rather than a classical PGS or LCP scheme. Its per-task
timesteps are published, which is rare: the Shadow Hand runs a 1/120 s physics step under a 1/60 s
control step, or 1/20 s in the OpenAI variant. The result that reorganised the field is that
reproducing OpenAI's Shadow Hand cube reorientation took under an hour on one A100, against 30
hours on 6144 CPU cores and 8 V100s (`isaacgym_2021`, Sec. 6.4.1). Thirty-five of the 110 method
papers in this corpus run on it.

Orbit and Isaac Lab moved the stack to PhysX 5, and the dexterous offering is thinner than the
predecessor's: the first-party suite is lifting, grasping and reorienting with the KUKA Allegro
hand, while Shadow and Ability hands appear only through third-party grasp evaluation
(`isaaclab_2025`, Sec. 7.2.3). MJX and MuJoCo Playground took the other route, putting MuJoCo's
own solver on the GPU through JAX at the cost described above. MuJoCo Warp ports the same solref
and solimp soft-constraint rows to NVIDIA Warp, and its README states that the legacy PGS solver
and the noslip pass are unsupported and that differentiability "is not yet available"
(`mujoco_warp_2025`). GPU MuJoCo is not a differentiable MuJoCo. Genesis is the broadest, pairing
a rigid constraint solver with FEM, MPM, PBD and SPH solvers and a differentiable backward path,
and it ships a Shadow Hand. Its README quotes no throughput number at all, so the large FPS
figures that circulate for Genesis trace to nothing in `genesis_2024`.

Newton changes how these names should be read. It is explicitly multi-solver: SolverMuJoCo wraps
MuJoCo Warp, SolverKamino is a proximal-ADMM and dual-variational-inequality contact solver, and
XPBD and VBD do position-based constraint projection (`newton_2025`). Its contact model is
solver-dependent, not a property of the engine, which is how Table 4 records it. The consequence
reaches upward. Isaac Lab's code already exposes a `--physics newton_mjwarp` backend switch in its
hands demo, and its roadmap announces Newton integration. An experiment reported as Isaac Lab may
be running PhysX 5 with TGS, or MuJoCo's soft constraint rows under Warp, and those two make
different contact errors. Naming a simulator no longer names its physics. Papers should report the
backend and the solver beside the framework.

## 4.4 Throughput, and why the reported numbers do not compare

Four headline figures measure four different quantities. Isaac Gym reports parallel environment
steps per second with physics, observations and rewards on device: 150,000 for the Shadow Hand at
16,384 environments on one A100. Isaac Lab reports frames per second in training, which includes
the learning update: over 900,000 for the DextrAH teacher task at 16,384 environments on eight RTX
Pro 6000 GPUs, with no single-GPU dexterous number anywhere in the paper. ManiSkill3 reports "up
to 30,000+ FPS" with RGBD and segmentation on one RTX 4090, measured over 1000 random actions with
reward and termination removed from the timing, and does not state the environment count behind
the figure (`maniskill3_2024`). Orbit reports a 125,000 FPS physics-only ceiling on an RTX 3090,
also with no environment count (`orbit_2023`, Sec. VII).

The one number reported cleanly enough to reuse is MuJoCo Playground's, in PPO steps per second on
a single A100 over five seeds. LeapCubeReorient runs at 76,354 ± 143 and PandaRobotiqPushCube at
487,341 ± 4,346. Same hardware, same measurement, same codebase, a factor of 6.4 from the task
alone. The same confound sits inside Isaac Gym's paper on one A100: 700,000 environment steps per
second for Ant, 200,000 for Humanoid, 150,000 for the Shadow Hand. A training-loop FPS is also
mostly not a measurement of physics. Playground breaks the fractional cost down on an RTX 4090:
for CartpoleBalance, physics is 0.02, rendering 0.06, inference 0.01 and the policy update 0.91,
and the policy update still dominates on the Franka task.

Cross-framework comparisons add a further free parameter, because the environment count is itself
tuned per framework. ManiSkill2's PickCube table takes the best result over 16 to 512 environments
for each system (`maniskill2_2023`, Table 1a), giving ManiSkill2 with a render server 2487 ± 24 FPS at its optimum of 64
environments against Isaac Gym's 865 ± 35 at its optimum of 512. Its authors add the caveat
themselves, that a fair comparison remains hard because fidelity differs, and Playground is
equally explicit that its cross-simulator plot borrows its Isaac Lab and ManiSkill3 numbers from
the ManiSkill3 paper. Several sources give no number at all: MuJoCo Warp's README points to an
external nightly dashboard, and Newton's and Genesis's READMEs contain no FPS or speedup
anywhere.

The failure reaches past the engine papers into the methods. Of the 47 corpus method papers that
name a GPU-batched simulator, 19 state no environment count anywhere, and Isaac Lab's own paper
states no physics timestep, no decimation and no solver iteration count for any task. A throughput
figure is interpretable only with the environment count, the GPU, the timesteps, the solver
iteration budget, and a statement of whether rendering and the learning update sit inside the
measurement. Almost nobody reports all five.

## 4.5 Tactile simulation and what it is calibrated against

The three tactile simulators in this corpus calibrate against three different things, and none of
them is a manipulation outcome. TACTO is a rendering layer over a host engine, by default
PyBullet's rigid contact model. It reads post-solve link poses and the engine's reported normal
force and maps that force to gel-mesh deformation at the rendering level, so it contributes no
contact physics of its own. Its only sim-to-real number is a tactile pose-estimation task, at
1.66 ± 0.16 mm with colour-jitter augmentation against 0.76 ± 0.07 mm for a model trained on 128
real datapoints (`tacto_2020`, Table II).

Taxim is example-based rather than simulated, with an optical model calibrated from 50 real
indentations, and it beats TACTO on every optical-similarity metric against real images. Its
marker-motion model is calibrated against an ANSYS FEM, and the errors are 1.00×10^-2 mm real
against FEM, 1.02×10^-2 mm real against Taxim, and 3.96×10^-3 mm FEM against Taxim. Taxim tracks
its own reference more tightly than that reference tracks reality, so its residual is bounded
below by the calibration target. The authors also state that they simulate quasi-static contact
only, with slip left as future work (`taxim_2021`, Sec. V). Slip is what a hand needs.

Tactile Genesis inverts the survey's thread. It implements two penetration-depth backends on the
collision geometry, an analytic SDF query and a BVH raycast, then binarises the result with
Schmitt hysteresis at 5×10^-4 m on and 2×10^-4 m off. Here the penetration depth is the sensor
signal, so the quantity every other engine treats as an error sets this sensor's operating point.
Against a real GelSight it reports relative marker RMSE of 0.329 in dilation and 0.174 in shear,
against HydroShear's 0.403 and 0.217, with each simulator tuned to match the real image first
(`tactile_genesis_2026`, Fig. 2). Its own sim-to-real check is a matched success count rather than
a fidelity measurement, because the real XHand1 SDK exposes only an aggregate contact pressure.

## 4.6 The sim-to-real gap for hands

Most of what is written about this gap is attribution without measurement. PenSpin asserts that
the pure physics gap "cannot be bridged by extensive domain randomization alone" while reporting
no experiment that isolates it (`penspin_2024`). MuJoCo Playground attributes its LEAP hand
failures to physical flex in low-cost hardware and names more accurate collision geometries as the
fix, without measuring either. DeXtreme lists four candidate causes for its shortfall, including a
malfunctioning Allegro thumb used in most trials, and disambiguates none by experiment
(`dextreme_2022`).

What has been measured is narrower. The size of the gap is known wherever a paper runs the same
policy in both places. OpenAI's Shadow Hand block reorientation reaches 43.4 ± 13.8 mean
consecutive successes in simulation and 18.8 ± 17.1 on the physical hand over 10 trials per
policy (`openai_dexterity_2018`, Table 3). Visual Dexterity reports 96 percent in simulation against 81 percent on the real D'Claw
for training objects, and 85 against 45 percent for held-out ones, over 20 real trials on each of
12 objects (`visual_dexterity_2022`, Table 1). Roughly half, and worse as the task hardens.

Three results identify causes with evidence. A humanoid recipe paper ranks its system
identification runs by dynamics-model MSE and pairs each with real success over 10 trials: the
lowest-MSE model grasps 8 out of 10, the median-MSE model 3 out of 10, the highest-MSE model 0 out
of 10 (`humanoid_sim2real_recipe_2025`, Table 1). That is the corpus's clearest measured link
between a quantified model error and transfer. OpenAI's per-category randomisation ablation on the
physical Shadow Hand gives median consecutive successes of 13 with all randomisations, 8.5 without
observation noise, 2 without physics randomisations, and 0 with none. DemoStart shows that gap
size is a function of design choice rather than a fixed property of the simulator: its full method
scores 99.0 percent in simulation and 64 percent over 100 real episodes, dropping photorealistic
data moves those to 97.0 and 29, and using one camera moves them to 97.0 and 17
(`demostart_2024`, Table IV). The simulation number barely moves while the real number collapses.

Where a cause has been pinned down it is usually perception or actuation, not contact. OpenAI's
pose estimator has 3.12 mm error on rendered images and 9.27 ± 4.02 mm on 992 real ones, and PDDM
reports a camera tracker with 5 mm average error and 20 ms latency as the unmodelled source in its
real numbers (`pddm_2019`, App. C). The contact side stays unmeasured, and one paper records why.
DeXtreme replayed real cube states back into simulation with physics enabled and found the replay
"sometimes resulted in interpenetrations", so the cube's physics parameters could not easily be
calibrated. The interpenetration the engine does not expose is also what blocks the
calibration that would let anyone attribute the gap to contact at all. The only direct measurement
of simulator fidelity against hardware in this corpus is Dojo's, an average final-position gap of
about 0.5 cm over 5 box-pushing trials. It is a parallel-jaw arm pushing a box, and there is no
equivalent number for a hand.

## 5. How policies are trained

### 5.1 The design space

A dexterous policy is defined by what supervises it. Four sources are in use across the corpus's
110 method rows. A reward function supervises reinforcement learning. A human demonstration
supervises imitation. A human reference trajectory supervises a physics-based tracker, which is
imitation with a simulator in the loop. And nothing supervises a model-based planner, which is
handed a cost and a model instead.

The labels do not partition the corpus. Of the 110 method rows, 53 carry the tag `RL`, 27 `BC`, 23
`distillation`, 16 `VLA`, 14 `teleop-system`, 14 `diffusion`, 10 `data-collection`, 8 `flow`, 6
`RL+demo`, 6 `trajopt`, 5 `MPC`, 4 `grasp-synthesis` and 2 `world-model`. The tags sum to far more
than 110 because most methods published since 2024 sit on two branches at once. Figure 4 draws the
tree and the cross-links. Table 7 is the row-by-row version of the same thing, and is the table to
scan when looking for work comparable to your own.

Three axes matter more than the name a paper gives itself: where the supervision comes from,
whether it is optimised in a simulator or on hardware, and what the deployed policy looks like
once training is done. On the last axis the field has converged hard, and section 5.7 shows why.

![fig4_taxonomy](figures/fig4_taxonomy.svg)

### 5.2 Reinforcement learning

#### 5.2.1 The standard recipe

Fifty-nine of the 110 method rows learn from a reward. Forty-eight name PPO as the algorithm, and
the next most frequent, DAPG, appears four times. Forty-three run their own experiments in a
GPU-parallel simulator from the Isaac family or Genesis, and 36 do both. Only 31 rows state an
environment count, with a median of 8192 and a maximum of 64000. Twenty-three rows distil a
privileged teacher into a deployable student, and 16 combine all three of PPO, a GPU simulator and
distillation. That 16-row intersection is the recipe as it is actually practised.

The hand is almost always an Allegro. It appears in 35 of the 110 method rows and in 17 of the 31
reorientation rows, ahead of Shadow at 21 and 6 and LEAP at 12 and 4.

Privilege is handled two ways. `openai_dexterity_2018` gives the value network object and target
orientation, joint angles, joint velocities and object velocities that the policy never sees, and
its footnote records that current object orientation was left out of the policy inputs by
accident. `dextreme_2022` uses the same asymmetric critic with a 2048-unit LSTM against the
actor's 1024. `hora_2022` instead compresses nine privileged object properties into an
eight-dimensional vector and regresses that vector from 30 steps of proprioception.
`visual_dexterity_2022` distils twice, from a state teacher to a synthetic point cloud and then to
a rendered one, for a stated fivefold training speedup.

Domain randomisation is the part of the recipe with the least discipline.
`openai_rubiks_cube_2019` made it adaptive, pushing each range boundary out when performance at
that boundary exceeds 20 successes and pulling it in below 10, and `dextreme_2022` reproduced the
mechanism with a 256-sample queue and 40 percent of environments dedicated to boundary evaluation.
Both publish the discovered ranges. Below that standard, three shipped configurations disagree
with their own papers about what was randomised. `hora_2022` states a joint-noise range of U(0,
0.005) against a shipped `jointNoiseScale` of 0.02, `penspin_2024` zeroes the disturbance force
its appendix describes, and `dexpbt_2023` reports no randomisation experiments while shipping a
full schedule behind a `randomize: False` switch.

#### 5.2.2 Reward engineering

Table 5 puts the 21 in-hand reorientation methods against nine recurring term families and marks
each cell by where the term was found, in the paper, in the code, or in both.

### Table 5. Reward terms across in-hand reorientation methods

| method | yr | goal or rotation tracking | object velocity | finger-object distance | hand-pose deviation | action rate or magnitude | torque, work or joint velocity | drop or failure | contact or force | success bonus | terms | code | paper/code mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `openai_dexterity_2018` | 2018 | paper |   |   |   |   |   | paper |   | paper | 3 | no |   |
| `openai_rubiks_cube_2019` | 2019 | paper |   |   |   |   |   | paper |   | paper | 3 | no |   |
| `dextreme_2022` | 2022 | both |   |   |   | both | both | code |   | both | 6 | yes | yes |
| `hora_2022` | 2022 | both | both |   | both |   | both |   |   |   | 5 | yes | yes |
| `visual_dexterity_2022` | 2022 | both |   | both | paper |   | both | both | both | both | 7 | yes | yes |
| `dexpbt_2023` | 2023 | both |   | both |   | code | paper | code |   | both | 4 | yes | yes |
| `eureka_2023` | 2023 | paper | paper | paper |   |   |   |   |   |   |   | yes | yes |
| `robot_synesthesia_2023` | 2023 | paper | paper | paper |   | paper | paper | paper |   |   | 6 | no |   |
| `rotateit_2023` | 2023 | paper | paper |   | paper |   | paper |   |   |   | 6 |   |   |
| `rotating_without_seeing_2023` | 2023 | paper | paper | paper |   |   | paper | paper |   |   | 6 |   |   |
| `anyrotate_2024` | 2024 | paper | paper |   | paper |   | paper | paper | paper | paper | 10 | no |   |
| `demostart_2024` | 2024 |   |   |   |   |   |   |   |   | paper | 1 | no |   |
| `dreureka_2024` | 2024 | paper | paper |   | paper |   |   | paper |   |   | 4 | yes | yes |
| `penspin_2024` | 2024 | both | both |   | both | code | both |   |   |   | 7 | yes | yes |
| `dexndm_2025` | 2025 | paper | paper |   | paper |   | paper |   |   | paper | 7 | no |   |
| `dexremoe_2025` | 2025 | paper | paper |   |   | paper |   |   |   | paper | 5 | no |   |
| `dexteritygen_2025` | 2025 |   |   |   |   |   |   |   |   |   |   | no |   |
| `force_grasp_sim2real_2026` | 2026 | paper |   |   | paper | paper | paper | paper | paper | paper | 7 | no |   |
| `poise_2026` | 2026 | paper |   |   |   |   | paper | paper | paper | paper | 4 | no |   |
| `teledexter_2026` | 2026 | paper |   |   |   |   |   |   |   | paper |   | no |   |
| `viserdex_2026` | 2026 | paper | paper |   |   | paper | paper | paper |   | paper | 10 | no |   |

*21 rows; 97 of 189 term cells (51%) are families the method does not use. `paper` means the term is in the paper and either no code was released or it is absent from the released reward code; `code` means it is in the released code and not in the paper's stated reward; `both` means it is in both. Marks are read from papers/notes/, term by term; the per-method source section is in corpus/reward_matrix.json.*

The families are not equally popular. Nineteen of 21 methods have a goal or rotation tracking
term, which is the task. Thirteen penalise effort as torque, work or joint velocity, 13 pay a
sparse success bonus, 12 penalise a drop and 11 penalise object velocity. Eight penalise deviation
of the hand from a canonical grasp pose, a family the plan for this table did not anticipate and
which had to be added. Only five reward closing the distance from fingertips to the object, and
only four mention contact or force at all.

That last number is the finding. Four of 21 in-hand reorientation methods put any contact or force
quantity in the reward. None puts interpenetration in it. `teledexter_2026` penalises
interpenetration with a differentiable signed-distance term, but during offline reference
construction, not in the policy's reward. Across all 110 method rows, 83 do not address
penetration at all, 5 constrain it, 3 measure it and 3 penalise it. The physical quality of the
contact is not something this literature optimises.

Term counts range from one to ten. `demostart_2024` gives a single binary terminal reward of 1 and
lets a curriculum over demonstration states do the shaping. `anyrotate_2024` and `viserdex_2026`
each publish ten weighted terms. `viserdex_2026` is the cleanest specification in the table, with
every term, weight and equation in one appendix table, and a statement that the same weights are
used for every object.

Weights are frequently unrecoverable. Three of the 21 rows give no numeric weight that survives
PDF conversion, because the equation blocks are images, which is a limit of this survey and is
recorded as such. `robot_synesthesia_2023` is a worse case. Its six coefficients are described
only as "tuned hyper-parameters" and no number is printed anywhere in the paper, so the reward it
reports cannot be reconstructed by anyone. `dexremoe_2025` names an angular-velocity penalty
weight in prose with no entry in its hyperparameter table, and `dextrack_2025` names an affinity
reward that is missing from its weight table.

#### 5.2.3 Curricula, populations and machine-written rewards

Curricula in this literature relax physics or tighten tolerances. `dexpbt_2023` tightens a success
tolerance from 0.075 to 0.01 by a factor of 0.9 every 3000 environment steps once three successes
are logged. `maniptrans_2025` starts at zero gravity and high friction and restores both, while
narrowing a fingertip threshold from 6 cm to 4 cm. `dexmachina_2025` attaches virtual
spring-damper controllers to the object, lets them do the task at first, then decays their gains
to zero. `rotateit_2023` sets its rotation-penalty weight to zero and ramps it to −0.1, reporting
that applying it from the start makes the policy learn only to hold the object still.
`viserdex_2026` replaces adaptive domain randomisation with a performance-based curriculum over
regularisation weight, action latency and time between successes, and reports that removing the
regularisation component causes complete failure.

Population-based training appears once. `dexpbt_2023` runs populations of 8, 16 and 32 agents,
splits them 30/40/30, mutates the middle and replaces the bottom with mutated copies of the top,
with each float hyperparameter multiplied or divided by a factor drawn from U(1.1, 1.5) with
probability 0.2. It reports 30 hours on a single V100 for a five-billion-transition single-arm
run, and 0.32 trillion environment steps for its largest population.

`eureka_2023` has GPT-4 write the reward function directly, constrained to return a total and a
dictionary of named components, and feeds per-component statistics back to the model between
iterations. Its own appendix gives an example whose reward correlates at −0.26 with the
human-written one and still scores 1.45 on the human-normalised metric, which is the strongest
argument in the corpus that hand-tuned weights are not a ceiling. `dreureka_2024` moves the safety
requirement into the prompt instead of a penalty term, asking in words for a cube rotating at
about 0.25 radians per second with fingers penalised for leaving their initial pose. Neither can
be checked. Eureka's config ships one iteration and three samples against the paper's five
iterations and sixteen samples, and writes generated rewards to a gitignored directory. DrEureka's
repository contains only the locomotion and globe-walking trees, so its LEAP-hand reward has no
code at all.

#### 5.2.4 Where reinforcement learning stalls

Reinforcement learning stalls on objectives that are not learnable as stated. `anyrotate_2024`
found the angular-velocity objective unlearnable in the multi-axis setting and replaced it with a
moving keypoint target. `rotateit_2023` reports that its multi-axis policy "does not converge when
training with only reinforcement learning" and adds an imitation loss against single-axis oracles.
`eureka_2023` cannot spin a pen from scratch and needs a pretrain-then-finetune split, with the
from-scratch ablation failing to complete one cycle. `physhoi_2023` documents the general shape of
the problem: contact moves the object off the reference, so return goes down, so the policy learns
not to touch the object.

It stalls on geometry too, and on evidence. `hora_2022` fails on objects under 4 cm across because
the fingers collide with each other. Real-robot trial counts stay small: `openai_dexterity_2018`,
`openai_rubiks_cube_2019`, `dextreme_2022` and `poise_2026` each report 10 trials for their
headline, and `robot_synesthesia_2023` reports 5. `hora_2022` at 240 is the outlier, not the norm.

### 5.3 Learning from human data

#### 5.3.1 Teleoperation and retargeting

Table 6 lists the 30 corpus rows that describe a system for getting human motion onto a robot
hand, with the retargeting objective compressed to one clause each.

### Table 6. Teleoperation and human-data systems

| system | operator interface | robot hand | retargeting objective | latency | rig USD | data collected |
|---|---|---|---|---|---|---|
| `dexpilot_2020` | four RealSense D415 RGB-D cameras tracking a bare hand, markerless; a coloured glove is w… | Wonik Robotics Allegro hand (16-DoF, 4x4-joint fingers), retrofitted with 4 SynTouch BioT… | minimise a weighted squared distance between human and Allegro fingertip task-space vecto… | about one second, end to end (Sec. IV) |   |   |
| `dexmv_2021` | human demonstrator recorded on video (cubic capture rig, two RealSense D435 cameras), no… | Adroit Hand | match human (MANO forward-kinematics) and robot task-space vectors (palm-to-fingertip and… |   |   | 700 traj, 7 h |
| `dexvip_2022` | no live operator; a consensus hand pose is mined offline from curated HowTo100M video fra… | Adroit Hand | deterministic 4-stage geometric mapping (not an optimization) from FrankMocap's 21-joint… |   |   |   |
| `dime_2022` | vision-based, single RGB camera, MediaPipe hand detector, no glove/headset/exoskeleton | Allegro Hand | map human fingertip 2D image locations directly to fixed-height robot fingertip 3D target… | not stated; targets at 30 Hz, PD loop at 300 Hz |   | 30 traj |
| `holo_dex_2022` | VR headset (Meta Quest 2), built-in 4-camera hand tracker, no glove/exoskeleton | Allegro Hand | direct joint-angle copy for index/middle/ring fingers; thumb fingertip position matched v… | under 100 ms on a local network (Sec. IV-D) | 399 |   |
| `videodex_2022` |   | LEAP Hand | hand poses mapped via a distilled MLP replicating a Robotic-Telekinesis-style fingertip/p… |   |   | 965 traj |
| `anyteleop_2023` | vision-based, camera only (RGB or RGB-D, single or multi-camera), MediaPipe hand-keypoint… | Allegro Hand | minimize the difference between human and robot fingertip keypoint vectors via forward ki… | 26-35 ms hand pose, 9-10 ms retargeting (Table II); no end-to-end figure |   |   |
| `pgdm_2023` |   | ShadowHand | for pre-grasps only: inverse kinematics fits the robot hand's fingertip positions to a si… |   |   | 40 traj |
| `ace_teleop_2024` | visual exoskeleton: 3D-printed bimanual 6-DoF-per-arm exoskeleton with wrist-mounted came… | Ability Hand / Inspire Hand / parallel-jaw gripper (embodiment-dependent) | wrist/end-effector pose mapped via a scale-and-recenter IK transform (Normal/Mirror/Biman… | 27 Hz hand tracking; no end-to-end figure | 600 |   |
| `bidex_teleop_2024` | Manus Meta motion-capture gloves for the fingers plus GELLO-style teacher arms for wrist… | LEAP Hand (16 DoF); LEAP Hand V2 (21 DoF) used for 'extreme dexterity' experiments | inverse kinematics from glove fingertip positions to LEAP fingertip targets, with the arm… | claimed low-latency, no number given | 6000 | 50 traj |
| `bunny_visionpro_2024` | VR headset (Apple Vision Pro) hand/wrist tracking, plus a custom ERM haptic feedback devi… | Ability Hand | minimize scaled human-robot fingertip keypoint-vector distance via forward kinematics wit… | 3.43 ms retargeting, 15.93 ms motion control, >60 Hz overall (Table 1) |   |   |
| `cyberdemo_2024` | vision-based teleoperation (single RealSense camera observing operator hand motion, real-… | Allegro Hand | delegated entirely to the cited third-party teleoperation system; CyberDemo does not desc… |   |   |   |
| `dexcap_2024` | wearable backpack rig: Rokoko EMF gloves, one SLAM camera per wrist and a chest-mounted R… | LEAP Hand | fingertip-position inverse kinematics into the 16-dim LEAP joint space anchored by the mo… |   | 4000 | 787 traj, 4.5 h |
| `egomimic_2024` | human data: head-worn Project Aria glasses (egocentric RGB + onboard SLAM/hand-tracking,… | parallel-jaw gripper (not a dexterous hand; see note scope flag) | no per-finger kinematic retargeting (end effector is a 2-finger gripper); domain alignmen… |   | 1000 | 2,150 traj, 4 h |
| `hudor_2024` | VR headset (Meta Quest 3) built-in hand tracking for fingertip 3D positions, ArUco-marker… | Allegro Hand | direct Cartesian-space correspondence: human fingertip 3D positions are treated as target… |   |   | 4 traj |
| `okami_2024` | single human demonstrator recorded on a static RGB-D camera (Intel RealSense D435i), no l… | Inspire Hand (x2) | factorized retargeting run once per demonstration video: arm/shoulder-elbow-wrist IK (via… |   |   |   |
| `open_television_2024` | VR headset (Apple Vision Pro or Meta Quest 3) with active stereo video streamed back from… | Inspire Robots hand (6 actuated DoF, 12 total); Fourier GR-1 embodiment instead uses a 1-… | dex-retargeting keypoint-vector optimisation over five wrist-to-fingertip and two thumb-t… | 60 Hz stereo round trip and 60 Hz control |   |   |
| `dexteritygen_2025` | human teleoperator tracked via a Manus Glove (retargeted to the Allegro hand at 300Hz via… | Allegro Hand |   |   |   |   |
| `dexumi_2025` | hand-specific 3D-printed wearable exoskeleton (per-robot-hand optimized joint-to-fingerti… | Inspire Hand (12 DoF, 6 active) and XHand (12 active DoF) | no visual/kinematic-chain retargeting at inference; a learned per-joint regression model… | per-sensor latency measured and compensated offline, no figure |   | 1,355 traj |
| `dexwild_2025` | wearable, calibration-free rig: motion-capture glove + two palm-mounted stereo cameras (p… | LEAP Hand / LEAP Hand V2 Advanced | robot hand kinematics optimized to match observed human fingertip positions (fixed hyperp… |   |   | 9,290 traj, 46.2 h |
| `doglove_2025` | haptic force-feedback exoskeleton glove (21-DoF encoder-based motion capture, 5-DoF cable… | LEAP Hand | map glove-FK fingertip positions to robot fingertip targets via the third-party Mink diff… | 30 Hz minimum system rate (120 Hz mocap, 30 Hz haptics) | 600 |   |
| `egozero_2025` | Project Aria smart glasses (egocentric fisheye RGB + SLAM cameras + onboard hand/camera p… | Franka Panda parallel-jaw gripper (not a dexterous hand; see note scope flag) | no kinematic hand-to-robot retargeting; both human and robot are represented in a shared… |   |   | 700 traj |
| `geometric_retargeting_2025` | Manus glove for fingertip keypoints + HTC Vive tracker for wrist pose (real-world evaluat… | Allegro Hand | learned per-finger neural network trained offline (3-5 minutes) to jointly satisfy motion… | 1 kHz retargeting inference, against 60-100 Hz for optimisation baselines |   |   |
| `h_rdt_2025` | for pretraining: none (consumes EgoDex's pre-existing released 3D hand-pose annotations,… | parallel-jaw / 2-jaw grippers at deployment (Aloha-Agilex, ARX5, Franka-Panda, UR5+UMI);… | no explicit kinematic retargeting; the 48-D bimanual wrist+fingertip human action space i… |   |   | 338,000 traj, 829 h |
| `humanoid_policy_human_policy_2025` | consumer VR headsets (Apple Vision Pro built-in camera with ARKit hand/head tracking, or… | Inspire Hand (x2, 5-fingered) | no offline kinematic retargeting network; human and robot share an identical 54-D state-a… |   | 700 |   |
| `wm_dex_human_videos_2025` |   | Allegro Hand | no explicit robot retargeting network; both human hands (MANO 21-keypoint) and robot end-… |   |   | 829 h |
| `dexteleop0_2026` | VR headset (Meta Quest 3), egocentric hand/wrist tracking (26 tracked hand-joint transfor… | Sharpa Wave (x2) | DexPilot-style vector matching of critical inter-joint/finger-to-palm target vectors for… | 30 Hz QP control cycle |   |   |
| `egoscale_2026` | large-scale pretraining: in-the-wild egocentric video with off-the-shelf SLAM + hand-pose… | Sharpa Wave (22-DoF); cross-embodiment target Unitree G1 (7-DoF tri-finger hand) | human 21-keypoint (MANO-style) hand pose retargeted via an optimization-based procedure e… |   |   | 20854 h |
| `teledexter_2026` | NOKOV motion-capture system tracking operator hand pose and object 6D pose in real time (… | SharpaWave (22-DoF, headline); also LeapHand (16-DoF) | two-stage geometry-aware retargeting: Stage 1 fingertip-vector alignment to human hand ge… |   |   |   |
| `unidex_2026` | human-video side: no live capture rig, converts existing egocentric RGB-D datasets (H2O,… | Inspire, Leap, Shadow, Allegro, Ability, Oymotion, XHand, Wuji (8 hands in UniDex-Dataset… | two-stage human-in-the-loop kinematic retargeting: an automatic PyBullet multi-end-effect… |   |   | 52,000 traj |

*30 rows; 60 of 210 cells (28%) are values no source stated.*

Retargeting splits four ways. The dominant family matches task-space vectors between the human and
robot hands. `dexpilot_2020` set the pattern with a weighted squared distance between fingertip
vectors, switching weights of 1, 200 and 400 by whether a pair is within threshold, a
minimum-separation constant of 3 cm between primary fingers, and a regulariser toward the open
hand, solved online with SLSQP. `anyteleop_2023`, `open_television_2024`, `bunny_visionpro_2024`
and `ace_teleop_2024` all use the same formulation. The second family copies joint angles where
the kinematics allow it, as `holo_dex_2022` does for index, middle and ring while solving the
thumb by inverse kinematics and discarding the pinky the Allegro does not have. The third family
learns the map offline. `geometric_retargeting_2025` trains a per-finger network in three to five
minutes against motion-direction, coverage, flatness, pinch and collision criteria, then runs at 1
kHz against the 60 to 100 Hz of online optimisation, raising configuration-space coverage from 38
to 90 percent and one-time grasp success from 55 to 87.5 percent. The fourth family removes
retargeting from the loop. `dexumi_2025` builds an exoskeleton whose fingertip workspace is
optimised to match the target hand, then regresses encoder values straight to motor values.

The table's empty cells are the point. Only 12 of the 30 rows state a latency of any kind, and
only 7 state a rig cost. Where costs are stated they are low and falling, from the $399 headset of
`holo_dex_2022` through the $600 exoskeleton of `ace_teleop_2024` and the $600 haptic glove of
`doglove_2025` to the $4,000 backpack of `dexcap_2024` and the roughly $6,000
glove-and-teacher-arm rig of `bidex_teleop_2024`. Latency, where reported, spans four orders of
magnitude, from `dexpilot_2020`'s "about one second" to `holo_dex_2022`'s "under 100 milliseconds"
to `geometric_retargeting_2025`'s 1 kHz retargeting step. Only 13 rows report how many
trajectories were collected, and only 7 report hours.

Where throughput is measured, human collection beats teleoperation by a wide margin.
`humanoid_policy_human_policy_2025` times a grasp demonstration at 3.79 seconds for a bare human
and 19.72 seconds through a teleoperated humanoid, and a pour at 4.81 against 37.31 seconds. It
attributes the gap to retargeting latency and to the workspace of a 7-DoF arm rather than to
anything about the hand.

#### 5.3.2 Imitation architectures

Four architectures cover the corpus. Action chunking came from `aloha_act_2023`, which predicts a
chunk of joint targets with a CVAE and combines overlapping chunks by exponentially weighted
ensembling, reaching 80 to 90 percent on fine bimanual tasks from about 50 demonstrations each.
Diffusion came from `diffusion_policy_2023`, which denoises an action sequence and reports a 46.9
percent average success improvement over LSTM-GMM, IBC and BET across 15 tasks. `dp3_2024` swaps
the image encoder for a small point-cloud encoder and reports 74.4 percent against 59.8 percent
across 72 simulated tasks, and 85.0 against 35.0 percent on four real tasks from 40 demonstrations
each. Flow matching is the 2024-onward default for large models and carries 8 of the 110 rows.
Discrete action tokens are the fourth, used by `openvla_2024` and `metis_2025`, and are the only
one of the four that needs no continuous head at all.

Data generation is a separate lever and is underrated. `dexmimicgen_2024` turns 60 human source
demonstrations into 21,000 simulated ones across 9 tasks and 3 embodiments, and a real Fourier GR1
with two Inspire hands reaches 90 percent from 40 generated demonstrations against 0 percent from
the 4 source demonstrations. `dex1b_2025` iterates optimisation, a CVAE proposal model and a
simulator filter to produce roughly a billion synthetic grasps, and its CVAE baseline beats the
prior best by 22 points.

#### 5.3.3 Human video without a robot

Seven rows train a dexterous-hand policy from video with no teleoperation at any stage.
`dexmv_2021` retargets 700 self-recorded demonstrations by matching palm-to-fingertip task-space
vectors and estimating actions by inverse dynamics. `videodex_2022` mines 965 trajectories from
EpicKitchens to pretrain a neural dynamic policy. `dexvip_2022` goes further into the reward,
clustering 715 curated HowTo100M frames into one consensus grasp pose per object category and
adding it as a reward term. `okami_2024`, `human2sim2robot_2025` and `hudor_2024` work from a
single video each. `wm_dex_human_videos_2025` pretrains a world model on 829 hours of EgoDex.

#### 5.3.4 The embodiment gap, and what closing it is worth

Three papers measure the gap directly rather than asserting it. `okami_2024` runs the same
reference-plan and warping pipeline with and without human body and hand retargeting, and the
version without it loses 75.0, 42.1, 82.0 and 74.0 points across four task and setting pairs. That
is the largest clean embodiment-gap number in the corpus.

`humanoid_policy_human_policy_2025` ablates two mitigations separately on the same vertical-grasp
task over 10 trials. The full method scores 4 out of 10. Removing the interpolation that slows
human trajectories by a factor of four drops it to 1 out of 10. Removing the unified
54-dimensional state space while keeping the slowdown drops it to 0 out of 10, because the policy
is handed a shortcut for telling the two embodiments apart. `egozero_2025` reports the sharpest
version of the same effect. Removing 3D augmentation drops every one of its seven tasks to 0 out
of 15, and substituting monocular depth for triangulated depth does the same, because the best
metric depth models it tested carry more than 5 cm of error. It also quantifies what its hand-pose
pipeline costs, at 1 to 2 cm of action-label error.

`objdex_2024` supplies the counterexample. It retargets only the wrist and lets reinforcement
learning discover finger motion, and its ablation that adds a fingertip-matching reward "does not
yield benefits and even leads to lower performance". Richer human correspondence is not uniformly
better, and this is the one result in the corpus that says so with an ablation.

### 5.4 Tracking a human reference with physics

Twelve method rows carry the `track-human-ref` task family. Eight of them track a human hand on an
object and are covered here. The other four sit at the edges of the family: `human2sim2robot_2025`
tracks only the object's trajectory, `dexman_2025` retargets bimanual video onto a full humanoid,
and `humanplus_2024` and `omnih2o_2024` track whole-body human motion. In all of them a reference
is retargeted onto the robot and a policy is trained to make the simulated body follow it. The
reference supplies the shaping that reward engineering would otherwise have to invent, and the
simulator supplies the physical consistency that pure imitation lacks.

`physhoi_2023` is the origin of the reward form. It multiplies a body term, an object term, an
interaction-graph term and a contact-graph term, and reaches 95.4 percent success on GRAB against
27.0 percent for a DeepMimic baseline. The contact-graph term exists to stop the policy learning
not to touch the object. `omnigrasp_2024` replaces the action space with a pretrained latent
motion prior and reports 94.6 percent grasp success and 84.8 percent trajectory success on GRAB,
while stating outright that it omits penetration metrics.

`dextrack_2025` adds an imitation loss to PPO and mines its own demonstrations through a homotopy
search over easier neighbouring trajectories, reaching 46.70 and 65.48 percent on GRAB at loose
and strict thresholds against 38.58 and 54.82 for the best baseline. It has a penetration-depth
formula and applies it only to input references, never to its own rollouts, and presents tolerance
of "severe hand-object penetrations" as robustness. `maniptrans_2025` freezes a generalist hand
imitator and trains a per-task residual on top, reaching 58.1 percent single-hand and 39.5 percent
bimanual success on OakInk-V2. Its stance on contact is to raise the friction coefficient above
the real value rather than model skin deformation, and its real deployment is open-loop replay.

`dexmachina_2025` moves to Genesis with 12,000 environments and six hand URDFs, and drives the
object with virtual controllers that decay to zero. Its re-implementation of `maniptrans_2025`'s
curriculum does not beat no curriculum on its own setup, which is a direct disagreement between
two papers worth quoting in both directions. `dexplore_2025` drops the explicit retargeting stage
and treats the reference as soft guidance, with termination thresholds derived from the failure
rate, reaching 87.7 percent on GRAB with an Inspire hand.

`toporetarget_2026` is the only corpus method that quantifies penetration as an evaluation
quantity, reporting maximum depth and the fraction of frames past 2 mm, and constraining it during
retargeting with a 1 mm soft tolerance and a 30 mm hard bound. It reaches 87.5 percent on its own
pen-spinning set against 46.9 for the best baseline. It does not re-measure penetration after the
tracking policy runs, so the property it constrains is a property of the reference and not of the
behaviour.

That is the pattern across all eight. Penetration is handled at the reference, if at all, and
never at the rollout. `objdex_2024` completes the set with the only real-robot numbers among them,
from 100 percent on a microwave and a laptop down to 41.2 percent on a ketchup bottle over 20
trials each.

### 5.5 Generalist and vision-language-action policies

The corpus scores 13 generalist policies on whether their own experiments report a result on a
multi-fingered hand. Eight do and five do not. The evidence is one sentence in each case.

Five are gripper-only. `pi0_2024` writes "UR5e. An arm with a parallel jaw gripper", and its
released code encodes each ALOHA gripper as a single scalar. `pi05_2025` writes "Both platforms
are equipped with two 6 DoF arms with parallel jaw grippers". `pistar06_2025` writes "we use a
static bimanual system with two 6 DoF arms with parallel jaw grippers". `openvla_2024` evaluates
on a WidowX, a Google robot, a Franka tabletop and DROID, all parallel-jaw, with the gripper as
one action dimension. `gemini_robotics_2025` puts a five-fingered Apollo hand in a figure caption
and reports no success rate, trial count or table for it anywhere.

Eight do evaluate on a hand. `gemini_robotics_15_2025` is the successor that fixed the gap, and
reports Apollo progress scores of 0.74, 0.73, 0.66, 0.62 and 0.63 by generalisation axis.
`groot_n1_2025` writes "This benchmark focuses on dexterous hand control using the GR-1 humanoid
robot equipped with Fourier dexterous hands", without stating the hand's degrees of freedom.
`being_h0_2025` uses "a 7-DoF Franka Research 3 arm, a 6-DoF Inspire hand" over 20 trials per
task, and `being_h05_2026` adds a LinkerBot O6 and two further hands, all tagged as six degrees of
freedom. `dexgraspvla_2025` uses "a 7-DoF RealMan RM75-6F arm and a 6-DoF PsiBot G0-R hand" over
1,287 trials, `metis_2025` uses "a pair of Inspire 6-DoF dexterous hands" on a Unitree G1, and
`dexora_2026` uses two XHAND hands with 12 actuated joints each. `dexvla_2025` is the borderline
case: the hand appears in one real-robot task family, while shirt folding, bussing, sorting, bin
picking and laundry all run on parallel-jaw grippers, and its 91-task pretraining mixture is
entirely gripper-based.

The hands that do appear are small. Four of the eight report six actuated degrees of freedom, one
reports twelve, and three do not state the number. None of the eight evaluates on the 16 to 24
actuated degrees of freedom that the reinforcement learning literature of section 5.2 runs on.
Three further rows, `gr_dexter_2025`, `unidex_2026` and `egoscale_2026`, evaluate on hands but
were not scored on this field, and the first of them reports a 21-DoF ByteDexter V2.

The released code also drifts. `groot_n1_2025`'s repository is a later N1.7 generation with a
different backbone, a different action horizon and embodiments the paper does not describe.
`pi05_2025`'s repository states that it supports only the flow-matching head, not the hybrid
recipe the paper describes.

### 5.6 Model-based control as the non-learning baseline

Three corpus methods solve dexterous tasks without learning a policy, and they are the control
group the rest of this section lacks.

`pddm_2019` learns an ensemble of dynamics models and plans through it with an MPPI-style
optimiser, replanning every step. It needs 1 to 2 hours of data in simulation and 2 to 4 hours on
a real 24-DoF Shadow Hand. `mjpc_2022` removes the learned model too and samples ten rollouts per
step through MuJoCo itself, planning in 1 to 20 milliseconds. It reorients a cube with a Shadow
Hand in real time from scratch, and reports no success criterion, no trial count and no real-robot
result.

`pang_global_planning_2022` is the most substantial of the three. It proves that the randomised
smoothing implicit in reinforcement learning and an analytic log-barrier relaxation compute the
same local linear model of contact, then uses the analytic version inside a trajectory optimiser
and an RRT. Allegro in-hand rotation takes 19.59 seconds to optimise and its plate-pickup task
takes 117.16 seconds of planning on a 16-core CPU, against the GPU-days of section 5.2. It is also
the only method here that imposes non-penetration as a hard constraint. Its own limitation is the
honest part: its 3D systems transfer to hardware far worse than its 2D ones, because the
quasi-dynamic assumption breaks and planned grasps miss contacts under a second-order solver.

### 5.7 Hybrids, and where the field has converged

The recurring shape is reinforcement learning in simulation distilled into a policy that looks
like an imitation policy. Twenty-three rows label the distillation step, and 16 combine PPO, a GPU
simulator and distillation in one pipeline.

The shape appears in four variants. The first distils a privileged teacher into a vision student
inside one paper, which is `hora_2022`, `visual_dexterity_2022`, `rotateit_2023`,
`robot_synesthesia_2023` and `viserdex_2026`. The second uses reinforcement learning as a
demonstration factory. `dextrack_2025` mines demonstrations with per-trajectory RL and trains a
generalist on them, and `maniptrans_2025` does the same to build a 3.3K-episode dataset.
`dexteritygen_2025` trains a diffusion controller on ten billion simulated grasp-to-grasp
transitions and then projects a human teleoperator's coarse command onto it, taking four
reorientation tasks from 0 out of 20 under raw teleoperation to 12, 13, 10 and 9 out of 20. The
third generates data without reinforcement learning at all, which is `dexmimicgen_2024`,
`dex1b_2025` and `deximit_2026`. The fourth wraps an RL policy in a residual, which is
`resdex_2024` at 88.8 percent over 3,200 objects in 12 GPU-hours.

The consequence is worth stating plainly. In the variants that dominate 2025 and 2026 work, the
reward is no longer the objective of the deployed policy. It is the objective of the process that
produced the deployed policy's training data. Reward engineering has moved upstream into data
curation, and every reward-shaping pathology in section 5.2 now reaches the shipped policy through
a dataset rather than a gradient.

### 5.8 What the released code says

Thirty-seven of the 110 method rows record a disagreement between the paper and the released code,
and all 37 released code, so the rate among the 61 methods that released anything is 61 percent.
Not all 37 are the same kind of thing. Sixteen are contradictions, where paper and code state
different values or different terms. Nine are limitations of this survey's own parsing, where the
relevant function body or config was not recovered and the survey says so. Seven released code
that does not contain the described component at all, three are version skew between the paper and
a later repository, and two are inconsistencies inside the paper. The 16 contradictions are the
number to quote. Among the 21 reorientation methods in Table 5, seven released code, five of those
seven contradict their paper outright, one is version skew and one released a repository without
the reward in it.

The most consequential case is `physhoi_2023`. Its `compute_humanoid_reward` hardcodes the body
position-velocity error and both object rotation errors to zero, with the real computation
commented out beside them. Its Table 4 lists non-zero weights of 0.1 and 0.01 for those object
rotation terms on GRAB. The reward that produced the paper's numbers therefore never tracked
object orientation. A method presented as tracking a 6-DoF reference was, in the code that ran,
tracking position only. The same file family shows the opposite outcome in `omnigrasp_2024`, whose
object rotation term is live. Its `compute_pregrasp_reward_time` has a problem of its own, and it
is internal to the code rather than a paper disagreement. The function accepts weights as
arguments and then hardcodes `w_pos, w_rot = 0.9, 0.1` inside its body.

Zeroed terms recur. `dexpbt_2023`'s `allegro_kuka_base.py` sums eight reward components against
the paper's four, and multiplies one of them, `hand_delta_penalty`, by zero with the comment
"currently disabled". `pianomime_2024` hardcodes its energy and fingering reward terms to return
zero. `penspin_2024` zeroes the disturbance force its appendix describes and disables the tactile
observation channel. A term that is present and zeroed is worse than a term that is missing,
because it survives a reader's check of the file.

Weights drift. `dextreme_2022` states an action-delta penalty of −0.25 in Table 2, ships −0.2 in
`AllegroHandDextremeADR.yaml` and −0.01 in `AllegroHandDextremeManualDR.yaml`, and adds a
`timeout_rew` term that appears in no table. `visual_dexterity_2022`'s Eq. 8 penultimate-joint
penalty does not exist in `dexenv/envs/rewards.py`. `graspxl_2024` ships an object-velocity
coefficient of −1.5 against a stated 0.1, and `unidexgrasp_2023` and `dexpoint_2022` both ship
reward functions structured differently from the paper's equation. `hora_2022`'s own README says
to check out tag v0.0.1 rather than the current commit to reproduce the paper's numbers, which is
version skew rather than contradiction. `dextrack_2025` ships several unreconciled
reward-coefficient sets, and which one produced its headline table could not be determined from
what this survey parsed.

The pattern is not confined to reinforcement learning, and some of it is internal to the papers.
`aloha_act_2023`'s Algorithm 1 says the reconstruction loss is MSE and its Section IV.C says L1.
`dp3_2024`'s prose says the network predicts noise while its shipped config sets `prediction_type:
sample`. `eureka_2023` ships a one-iteration, three-sample default against a reported five
iterations and sixteen samples. `maniptrans_2025`'s stated learning rate and environment count
differ from its own README.

A reward table in a paper is a claim about a training run, and the code is a claim about a
repository. In this corpus the two contradict each other in 16 cases, and in the other 21 the
released artefacts do not settle the question. In none of the 37 does the paper say so. Read the
reward function before the reward table, and treat a printed weight as a hypothesis about the
code.


### 5.9 The master table

Table 7 is every method row on one set of axes, and its footer is worth reading before its rows.
Two hundred and thirty-seven of its 1540 cells are values no source stated. The emptiest columns
are the ones a reader most needs: only 31 rows state an environment count, only 55 state how many
real trials are behind the headline number, and only 32 state how many unseen objects were tested.
A mostly empty row is not a weak method, but it is one that cannot be compared with any other row
here.

### Table 7. Methods

| method | yr | task | paradigm | algorithm | hand | DoF | bi | sim | real | trials | unseen obj | penetration | code |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `ferrari_canny_1992` | 1992 |   |   |   |   |   |   |   |   |   |   |   | no |
| `dapg_2017` | 2017 | grasp, reorient, functional/tool, other | RL+demo | NPG (Natural Policy Gradient) + BC pretraining (DAPG) | ADROIT | 24 | no | MuJoCo | no |   |   | not addressed | yes |
| `openai_dexterity_2018` | 2018 | reorient | RL | PPO | ShadowRobot Dexterous Hand (EDC electric-motor version) | 24 | no | MuJoCo | yes | 10 |   | not addressed | no |
| `openai_rubiks_cube_2019` | 2019 | reorient | RL, distillation | PPO with Automatic Domain Randomization (ADR); Policy Cloning (DAGGER/distillation-style)… | Shadow Dexterous E Series Hand (E3M5R) | 20 | no | MuJoCo (+ ORRB/Unity3D for rendered vision training images) | yes | 10 |   | not addressed | no |
| `pddm_2019` | 2019 | reorient, other | MPC | PDDM: ensemble of feed-forward dynamics models + MPPI-style filtering/reward-weighted-ref… | Shadow Hand (24-DoF, real and sim); D'Claw (9-DoF, sim only, valve turning) |   | no | MuJoCo | yes |   |   | not addressed | yes |
| `dexpilot_2020` | 2020 | reorient, grasp, functional/tool, other | teleop-system | DART model-based hand tracker bootstrapped by two learned neural priors (GloveNet ResNet-… | Wonik Robotics Allegro hand (16-DoF, 4x4-joint fingers), retrofitted with 4 SynTouch BioT… | 16 | no |   | yes | 150 |   | not addressed | no |
| `castro_sap_contact_2021` | 2021 | bimanual-coord |   | SAP (Semi-Analytic Primal) solver: a custom Newton-type solver on an unconstrained convex… | Allegro hand (16 DoF each), two | 16 | yes | Drake | no |   |   | measured | yes |
| `dexmv_2021` | 2021 | grasp, functional/tool | RL+demo, data-collection | DAPG / SOIL / GAIL+ on top of TRPO, using demonstrations translated from human video via… | Adroit Hand | 30 | no | MuJoCo | no |   | 500 | not addressed | yes |
| `dexpoint_2022` | 2022 | grasp, other | RL | PPO | Allegro Hand | 16 | no | SAPIEN | yes |   | 40 | not addressed | yes |
| `dextreme_2022` | 2022 | reorient | RL | PPO (rl-games implementation, LSTM actor/critic, asymmetric/state-privileged critic) | Allegro Hand | 16 | no | Isaac Gym (PhysX) | yes | 10 |   | not addressed | yes |
| `dexvip_2022` | 2022 | grasp | RL | PPO with a video-mined consensus grasp-pose auxiliary reward (R_pose) combined with an af… | Adroit Hand | 30 | no | MuJoCo | no |   |   | not addressed | no |
| `dime_2022` | 2022 | reorient, grasp | teleop-system, BC, RL+demo | INN/VINN (nearest-neighbor imitation) vs. BC; DAPG/PPO/BCRL (simulation RL-finetuning) | Allegro Hand |   | no | MuJoCo | yes | 10 |   | not addressed | yes |
| `holo_dex_2022` | 2022 | reorient, grasp, functional/tool | teleop-system, BC | VINN (BYOL nearest-neighbor) vs. Behavior Cloning / BC-Rep | Allegro Hand | 16 | no |   | yes | 10 | 10 | not addressed | yes |
| `hora_2022` | 2022 | reorient | RL, distillation | PPO | Allegro Hand (Wonik Robotics) | 16 | no | IsaacGym | yes | 240 | 30 | not addressed | yes |
| `mjpc_2022` | 2022 | reorient | MPC | Predictive Sampling: zero-order, derivative-free sampling-based shooting MPC over a splin… | Shadow Hand (MuJoCo Menagerie model) |   | no | MuJoCo | no |   |   | not addressed | yes |
| `pang_global_planning_2022` | 2022 | reorient, grasp, bimanual-coord, other | trajopt | iMPC (iLQR-style trajectory optimizer over a locally-smoothed convex quasi-dynamic contac… | Allegro Hand (full 3D model, in-hand rotation / pen placement / plate pickup / door openi… |   | yes | Custom Convex Quasi-Dynamic Differentiable Contact (CQDC) model implemented in Drake (Mul… | yes |   |   | constrained | yes |
| `videodex_2022` | 2022 | grasp, reorient, functional/tool | BC, data-collection | two-stream Neural Dynamic Policy (NDP) trajectory regression (L1 loss): pretrained on hum… | LEAP Hand | 16 | no |   | yes |   |   | not addressed | no |
| `visual_dexterity_2022` | 2022 | reorient | RL, distillation | PPO (teacher, privileged state) + DAgger imitation distillation to a depth-point-cloud st… | D'Claw (open-source, low-cost; 3-finger and modified 4-finger versions) |   | no | Isaac Gym (PhysX) | yes | 20 | 12 | not addressed | yes |
| `aloha_act_2023` | 2023 | bimanual-coord | BC | ACT (Action Chunking with Transformers, CVAE) | parallel-jaw gripper (not dexterous), two |   | yes | MuJoCo | yes | 25 |   | not addressed | yes |
| `anyteleop_2023` | 2023 | grasp, functional/tool, handover | teleop-system, RL+demo | DAPG (downstream IL); keypoint-vector retargeting optimization (dex_retargeting) | Allegro Hand |   | no | SAPIEN | yes | 100 |   | not addressed | yes |
| `artigrasp_2023` | 2023 | grasp, functional/tool, bimanual-coord | RL | PPO (D-Grasp-based implementation) | MANO hand model, two | 51 | yes | RaiSim | no |   | 1 | not addressed | yes |
| `dexdeform_2023` | 2023 | bimanual-coord, other | BC, trajopt | latent skill model (VAE over demonstrations) for skill-planned trajectory initialization,… | Shadow Dexterous Hand (simulated) | 28 | yes | PlasticineLab (MLS-MPM, CUDA), built on Hu et al. 2018's Moving Least Squares Material Po… | no |   |   | not addressed | yes |
| `dexpbt_2023` | 2023 | grasp, reorient, bimanual-coord | RL | PPO (rl_games) with decentralized Population-Based Training (PBT) over RL hyperparameters… | Allegro Hand | 16 | yes | Isaac Gym (PhysX) | no |   |   | not addressed | yes |
| `dexterous_functional_grasping_2023` | 2023 | functional/tool | RL | PPO | LEAP hand | 16 | no | IsaacGym | yes | 70 | 5 |   | no |
| `diffusion_policy_2023` | 2023 | grasp, functional/tool, bimanual-coord, other | BC, diffusion | conditional DDPM over action sequences (CNN or transformer noise-prediction network), DDI… |   |   | yes | task-specific: Robomimic (MuJoCo-backed), Push-T (custom 2D physics per IBC), BlockPush (… | yes |   |   | not addressed | yes |
| `dynamic_handover_2023` | 2023 | handover, bimanual-coord | RL | MAPPO | Allegro Hand | 16 | yes | IsaacGym | yes | 15 | 14 | not addressed | no |
| `eureka_2023` | 2023 | reorient, bimanual-coord, other | RL | PPO with LLM-authored (GPT-4) evolutionary reward search | Shadow Hand (also Allegro Hand; bimanual pairs of Shadow Hands for Dexterity tasks) | 20 | yes | IsaacGym | yes |   |   | not addressed | yes |
| `pgdm_2023` | 2023 | grasp, functional/tool | RL | PPO (Stable-Baselines3) with an object-trajectory-tracking reward plus pre-grasp-based ex… | ShadowHand | 24 | no | MuJoCo | yes |   |   | not addressed | no |
| `physhoi_2023` | 2023 | track-human-ref | RL | PPO | SMPL-X humanoid (simulated, not a robot hand) | 90 | no | Isaac Gym | no |   |   | not addressed | yes |
| `robot_synesthesia_2023` | 2023 | reorient | RL, distillation | PPO | Allegro Hand | 16 | no | Isaac Gym | yes | 5 |   | not addressed | no |
| `rotateit_2023` | 2023 | reorient | RL, distillation | PPO | AllegroHand (Wonik Robotics) | 16 | no | IsaacGym | yes |   | 15 | not addressed |   |
| `rotating_without_seeing_2023` | 2023 | reorient | RL | PPO | Allegro Hand | 16 | no | IsaacGym | yes | 30 | 5 | not addressed |   |
| `unidexgrasp_2023` | 2023 | grasp | grasp-synthesis, RL, distillation | PPO (teacher) + DAgger (student distillation) | ShadowHand | 26 | no | Isaac Gym | no |   | 241 | penalised | yes |
| `unidexgrasp_pp_2023` | 2023 | grasp | RL, distillation | PPO + DAgger (with critic distillation) | Shadow Hand | 24 | no | Isaac Gym | no |   |   | not addressed | yes |
| `ace_teleop_2024` | 2024 | grasp, functional/tool | teleop-system, BC | 3D Diffusion Policy (DP3) for xArm platforms; ACT for H1 humanoid (downstream IL); IK-bas… | Ability Hand / Inspire Hand / parallel-jaw gripper (embodiment-dependent) |   | yes |   | yes | 10 | 18 | not addressed | no |
| `anyrotate_2024` | 2024 | reorient | RL, distillation | PPO | Allegro Hand | 16 | no | IsaacGym | yes |   |   | not addressed | no |
| `asymdex_2024` | 2024 | bimanual-coord, grasp | RL | PPO | Shadow Hand (30-DoF: 24-DoF hand + 6-DoF floating wrist) in simulation; 16-DoF Allegro ha… | 30 | yes | NVIDIA Isaac Gym | yes | 20 |   | not addressed | yes |
| `bidex_teleop_2024` | 2024 | bimanual-coord, handover, functional/tool | teleop-system, BC | ACT (Action Chunking Transformer) | LEAP Hand (16 DoF); LEAP Hand V2 (21 DoF) used for 'extreme dexterity' experiments | 16 | yes | none | yes |   |   | not addressed | no |
| `bidexhd_2024` | 2024 | functional/tool, bimanual-coord | RL, distillation | IPPO (teacher) + DAgger (student distillation) | LEAP Hand, left and right | 16 | yes | Isaac Gym (PhysX) | no |   |   | not addressed | yes |
| `bimangrasp_2024` | 2024 | grasp, bimanual-coord | grasp-synthesis, diffusion | MALA (Metropolis-adjusted Langevin) energy optimisation + DDPM (BimanGrasp-DDPM) | Shadow Hand, pair | 22 | yes | Isaac Gym | no |   | 225 | penalised | no |
| `bunny_visionpro_2024` | 2024 | grasp, functional/tool, bimanual-coord | teleop-system, BC | ACT, Diffusion Policy, DP3 (downstream IL); SQP fingertip-vector hand retargeting + unifi… | Ability Hand | 24 | yes |   | yes | 10 |   | not addressed | yes |
| `cyberdemo_2024` | 2024 | grasp, reorient, functional/tool | BC, teleop-system, data-collection | ACT (Action Chunking with Transformers) BC policy, trained on sim teleoperation demonstra… | Allegro Hand | 16 | no | SAPIEN | yes | 20 | 2 | not addressed | no |
| `demostart_2024` | 2024 | grasp, functional/tool, reorient, other | RL, distillation | MPO (teacher, auto-curriculum) + BC distillation (student, Perceiver-Actor-Critic) | DEX-EE Hand | 12 | no | MuJoCo | yes | 100 |   | not addressed | no |
| `dexcap_2024` | 2024 | grasp, bimanual-coord, functional/tool | BC, diffusion, data-collection | Diffusion Policy with Perceiver point-cloud encoder (DP-perc) | LEAP Hand | 16 | yes | none | yes | 60 | 9 |   | yes |
| `dexmimicgen_2024` | 2024 | bimanual-coord, grasp, functional/tool | data-collection, BC | MimicGen-style per-arm subtask transform/replay generation; downstream BC-RNN / BC-RNN-GM… | Inspire dexterous hand (6-DoF, real-world GR1); unnamed 'dexterous hands' in the two simu… | 6 | yes | RoboSuite (MuJoCo) | yes | 20 |   |   | yes |
| `dp3_2024` | 2024 | reorient, grasp, functional/tool, bimanual-coord, other | BC, diffusion | Diffusion Policy backbone (DDPM training / DDIM inference) conditioned on a compact 3D po… | Shadow Hand (Adroit, Bi-DexHands, DexDeform, DexMV domains); Allegro Hand (DexArt, HORA d… |   | yes | MuJoCo (Adroit, MetaWorld), IsaacGym (Bi-DexHands, HORA), Sapien (DexArt, DexMV), Plastic… | yes | 40 |   | not addressed | yes |
| `dreureka_2024` | 2024 | reorient | RL | PPO with LLM-authored (GPT-4) reward search + reward-aware physics prior domain randomiza… | LEAP hand | 16 | no | Isaac Gym | yes |   |   | not addressed | yes |
| `egomimic_2024` | 2024 | grasp, functional/tool, bimanual-coord | BC | shared-backbone ACT variant co-trained on paired egocentric human video and teleoperated… | parallel-jaw gripper (not a dexterous hand; see note scope flag) | 1 | yes |   | yes | 135 |   | not addressed | yes |
| `graspxl_2024` | 2024 | grasp | RL | PPO | MANO (also Shadow Hand, Allegro Hand, Faive Hand) | 45 | no | RaiSim | no |   | 503409 | not addressed | yes |
| `hato_visuotactile_2024` | 2024 | handover, bimanual-coord | diffusion | Diffusion Policy (DDPM, CNN-based) | Psyonic Ability Hand, two | 6 | yes |   | yes | 10 |   | not addressed | yes |
| `hudor_2024` | 2024 | grasp, functional/tool | RL | open-loop IK replay of a single retargeted human fingertip trajectory plus online residua… | Allegro Hand | 16 | no |   | yes | 10 |   | not addressed | no |
| `humanplus_2024` | 2024 | track-human-ref, locomanipulation | RL, BC | PPO (HST shadowing policy) + decoder-only Transformer BC (HIT) | Inspire-Robots RH56DFX, two | 6 | yes | Isaac Gym-based legged_gym/rsl_rl | yes | 10 |   | not addressed | yes |
| `objdex_2024` | 2024 | track-human-ref, bimanual-coord | BC, RL, distillation | BC (Transformer high-level planner) + PPO (low-level controller) | Shadow Hand |   | yes |   | yes | 80 | 1 | not addressed | no |
| `okami_2024` | 2024 | grasp, functional/tool, bimanual-coord | trajopt, BC | single-video imitation: SLAHMR-extended SMPL-H body+hand reconstruction, GPT-4V/Grounded-… | Inspire Hand (x2) | 6 | yes | RoboSuite (2 of 6 tasks only) | yes | 12 |   | not addressed | yes |
| `omnigrasp_2024` | 2024 | grasp, track-human-ref | RL, distillation | PPO (hierarchical: PHC-X finger imitator → PULSE-X distilled latent prior → PPO over late… | SMPL-X whole-body humanoid (simulated, not a robot hand) | 90 | yes | Isaac Gym | no |   | 5 | not addressed | yes |
| `omnih2o_2024` | 2024 | track-human-ref, locomanipulation | RL, distillation | PPO (teacher) + DAgger (student) + diffusion policy (autonomy layer) | Inspire hands (open-loop, DoF not stated) |   | yes |   | yes | 20 |   |   | yes |
| `open_television_2024` | 2024 | bimanual-coord, functional/tool | teleop-system, BC | ACT (Action Chunking Transformer) with DinoV2 ViT backbone | Inspire Robots hand (6 actuated DoF, 12 total); Fourier GR-1 embodiment instead uses a 1-… | 6 | yes | none | yes |   |   | not addressed | yes |
| `openvla_2024` | 2024 | other | VLA | autoregressive next-token prediction over discretized (256-bin per-dimension, quantile-ba… |   |   | no | LIBERO benchmark (simulated Franka) for fine-tuning experiments; engine/version not stated | yes | 230 |   | not addressed | yes |
| `penspin_2024` | 2024 | reorient | RL, distillation | PPO + BC | Allegro Hand | 16 | no | Isaac Gym | yes |   | 7 | not addressed | yes |
| `pi0_2024` | 2024 | other | VLA, flow | conditional flow matching (linear-Gaussian/optimal-transport probability path), forward-E… |   |   | yes |   | yes |   |   | not addressed | yes |
| `pianomime_2024` | 2024 | music | RL+demo, distillation | PPO (per-song specialists); DDPM diffusion (generalist) | Shadow Hand E3M5 | 23 | yes | ROBOPIANIST (MuJoCo) | no |   |   | not addressed | yes |
| `rdt1b_2024` | 2024 | bimanual-coord | diffusion | RDT (DiT + cross-attention, QKNorm/RMSNorm, MLP decoder, Alternating Condition Injection) | parallel-jaw gripper (ALOHA-style, Cobot Mobile ALOHA), two |   | yes |   | yes |   |   | not addressed | yes |
| `resdex_2024` | 2024 | grasp | RL, distillation | PPO + DAgger | ShadowHand | 18 | no | IsaacGym | no |   | 241 | not addressed | yes |
| `twisting_lids_2024` | 2024 | functional/tool, bimanual-coord | RL | PPO (asymmetric actor-critic) | Allegro Hand, two | 16 | yes | Isaac Gym | yes |   | 15 | not addressed | no |
| `umi_2024` | 2024 | functional/tool, bimanual-coord, other | BC, diffusion, data-collection, teleop-system | Diffusion Policy (unmodified loss/decoder); contribution is the hand-held data-collection… |   |   | yes |   | yes |   |   |   | yes |
| `articulated_tools_inhand_2025` | 2025 | functional/tool | RL, BC, distillation | PPO (oracle) + BC (student + CATFA online adaptation) | Inspire Hand | 6 | no | IsaacLab | yes | 50 |   | not addressed | no |
| `being_h0_2025` | 2025 | grasp, functional/tool | VLA, BC | autoregressive next-token prediction over discretized MANO motion tokens (Grouped Residua… | 6-DoF Inspire hand mounted on a 7-DoF Franka Research 3 arm (real robot); MANO parametric… | 6 | no |   | yes | 20 |   | not addressed | yes |
| `clutterdexgrasp_2025` | 2025 | grasp | RL, diffusion, distillation | PPO (teacher) + DP3 diffusion policy (student) | AgiBot dexterous hand | 6 | no | Isaac Gym | yes | 167 | 2029 | constrained | no |
| `cross_embodiment_world_models_2025` | 2025 | other | world-model, MPC | DPI-Net (graph neural network particle-dynamics world model) + sampling-based receding-ho… | PSYONIC Ability Hand (6-DoF) and Robot Era XHand (12-DoF) for real-world deployment; trai… |   | no | SAPIEN (rigid-body Object Pushing data) and Rewarped (differentiable multiphysics, deform… | yes | 20 |   | not addressed | no |
| `dexgraspvla_2025` | 2025 | grasp, other | VLA, diffusion | hierarchical VLA: frozen VLM high-level planner (bounding-box affordance) + DiT diffusion… | PsiBot G0-R, 6-DoF, single (right) hand | 6 | no |   | yes | 1287 | 360 | not addressed | yes |
| `dexmachina_2025` | 2025 | track-human-ref, bimanual-coord | RL | PPO (rl-games) | six URDFs: Inspire, Allegro, XHand, Schunk (main), Ability, DexRobot Dex Hand |   | yes | Genesis | no |   |   | constrained | yes |
| `dexman_2025` | 2025 | track-human-ref, bimanual-coord | RL, trajopt | PPO (RL_GAMES) residual policy on top of IK-retargeted human motion | Shadow Dexterous Hand |   | yes | NVIDIA Isaac Gym | no |   |   |   | no |
| `dexndm_2025` | 2025 | reorient | RL, distillation | PPO (oracle) + BC (generalist) + supervised residual policy | LEAP hand |   | no | Isaac Gym | yes |   |   | not addressed | no |
| `dexplore_2025` | 2025 | track-human-ref | RL, distillation | PPO (teacher) + DAgger-style VAE distillation (student) | Inspire hand (also Allegro hand) | 6 | no | Isaac Gym | yes |   |   | not addressed | yes |
| `dexremoe_2025` | 2025 | reorient | RL | PPO | GX11 three-fingered dexterous hand (custom) | 11 | no | IsaacGym | no |   | 50 | not addressed | no |
| `dexteritygen_2025` | 2025 | reorient, functional/tool, grasp | RL, diffusion | RL-generated Anygrasp-to-Anygrasp transitions used to train a UNet DDPM diffusion foundat… | Allegro Hand | 16 | no |   | yes |   |   |   | no |
| `dexterous_handover_2025` | 2025 | handover, grasp | RL | PPO | Allegro Hand |   | no | IsaacLab | no |   | 3 | not addressed |   |
| `dextrack_2025` | 2025 | track-human-ref | RL+demo | PPO + IL action-supervision loss | Allegro hand (sim); LEAP hand (real) | 16 | no | Isaac Gym | yes |   |   | measured | yes |
| `dexumi_2025` | 2025 | grasp, functional/tool | BC, data-collection | diffusion policy (DDPM-style action-chunking) trained on exoskeleton-collected demonstrat… | Inspire Hand (12 DoF, 6 active) and XHand (12 active DoF) |   | no |   | yes | 20 |   |   | yes |
| `dexvla_2025` | 2025 | grasp, functional/tool, bimanual-coord | VLA, diffusion | ScaleDP (Scale Diffusion Policy, transformer-based diffusion action head, up to 1B parame… | Robotiq parallel-jaw gripper (Franka rig a, Bimanual UR5e rig c); Inspire multi-fingered… |   |   | LIBERO (secondary, App. A.2 only; main results are real-robot) | yes | 10 | 30 | not addressed | yes |
| `dexwild_2025` | 2025 | grasp, functional/tool, bimanual-coord | BC, data-collection | diffusion U-Net policy (also compared against ACT) co-trained on human wearable-rig demon… | LEAP Hand / LEAP Hand V2 Advanced | 17 | yes |   | yes |   |   |   | yes |
| `dydexhandover_2025` | 2025 | handover, bimanual-coord | RL | MAPPO (human-regularized, CTDE, with hybrid advantage estimation) | 11-DoF (6 actuated) dexterous hand, per side (vendor not stated) | 11 | yes | NVIDIA Isaac Sim / Isaac Lab | no |   | 9 | not addressed | no |
| `egozero_2025` | 2025 | grasp, functional/tool | BC | closed-loop Transformer policy (BC, Gaussian NLL loss) over a morphology-agnostic 3D-poin… | Franka Panda parallel-jaw gripper (not a dexterous hand; see note scope flag) | 1 | no |   | yes | 15 |   | not addressed | yes |
| `gemini_robotics_15_2025` | 2025 | other | VLA |   | ALOHA parallel gripper (by platform convention, not re-specified); Bi-arm Franka parallel… |   | yes | MuJoCo (used to generate evaluation scenes at scale, not for training; engine timestep/co… | yes |   |   | not addressed | no |
| `gemini_robotics_2025` | 2025 | other, handover | VLA, distillation |   | ALOHA 2 parallel gripper, two fingers (primary embodiment); bi-arm Franka parallel grippe… |   | yes |   | yes |   |   | not addressed | no |
| `geometric_retargeting_2025` | 2025 | grasp | teleop-system | per-finger MLP retargeting network (GeoRT) trained offline against five geometric losses:… | Allegro Hand |   | no |   | yes |   |   | not addressed | yes |
| `gr_dexter_2025` | 2025 | bimanual-coord, grasp | VLA | GR-Dexter (Mixture-of-Transformer VLA, flow matching + next-token prediction, following G… | ByteDexter V2, two | 21 | yes |   | yes |   | 23 | not addressed | no |
| `groot_n1_2025` | 2025 | grasp, functional/tool, bimanual-coord, handover | VLA, flow | dual-system architecture: Eagle-2 VLM (System 2, reasoning) feeding a DiT flow-matching a… | Fourier dexterous hands, on the Fourier GR-1 humanoid; DoF/finger count not stated |   | yes | RoboCasa (Kitchen and GR-1 Tabletop benchmarks); DexMimicGen (cross-embodiment suite and… | yes |   |   | not addressed | yes |
| `h_rdt_2025` | 2025 | grasp, functional/tool, bimanual-coord | flow | 2B-parameter flow-matching diffusion transformer (H-RDT), pretrained on EgoDex human hand… | parallel-jaw / 2-jaw grippers at deployment (Aloha-Agilex, ARX5, Franka-Panda, UR5+UMI);… |   | yes | RoboTwin 2.0 | yes |   |   | not addressed | no |
| `human2sim2robot_2025` | 2025 | track-human-ref | RL | PPO | Allegro Hand | 16 | no | IsaacGym | yes | 70 |   | not addressed | yes |
| `humanoid_policy_human_policy_2025` | 2025 | grasp, functional/tool | BC | Human Action Transformer (HAT), an ACT-style action-chunking transformer co-trained joint… | Inspire Hand (x2, 5-fingered) | 6 | yes |   | yes | 230 |   | not addressed | yes |
| `humanoid_sim2real_recipe_2025` | 2025 | grasp, bimanual-coord, handover | RL, distillation | PPO (asymmetric actor-critic) for per-task specialist policies, distilled into a generali… | Fourier GR1 hand (6 actuated + 5 underactuated DoF); cross-embodiment check also uses Ins… | 6 | yes | NVIDIA Isaac Gym | yes | 10 |   |   | no |
| `maniptrans_2025` | 2025 | track-human-ref, bimanual-coord | RL, BC, diffusion | PPO (two-stage: frozen generalist imitator + per-task residual policy) | Inspire Hand (12-DoF sim); also Shadow(22), MANO(22), Allegro(16) | 12 | yes | Isaac Gym | yes |   |   | not addressed | yes |
| `metis_2025` | 2025 | grasp, functional/tool, bimanual-coord | VLA | Autoregressive next-token cross-entropy over discretized 'motion-aware dynamics' tokens (… | Inspire dexterous hand (paired, main real-robot eval); cross-embodiment eval uses 22-DoF… | 6 | yes |   | yes | 20 |   | not addressed | no |
| `pi05_2025` | 2025 | other | VLA, flow | hierarchical high-level discrete-subtask prediction (FAST tokenizer, autoregressive) + lo… |   |   | yes |   | yes | 40 |   | not addressed | yes |
| `pistar06_2025` | 2025 | other | VLA, RL, flow | RECAP: advantage-conditioned policy extraction on a flow-matching VLA, using a distributi… |   |   | yes |   | yes |   |   | not addressed | yes |
| `wm_dex_human_videos_2025` | 2025 | grasp | world-model, MPC | DexWM: a deterministic latent-space (DINOv2) world model with a CDiT-based predictor cond… | Allegro Hand |   | no | RoboCasa | yes | 12 |   |   | no |
| `being_h05_2026` | 2026 | bimanual-coord, other | VLA, flow | Rectified Flow (continuous action velocity-field prediction) + Masked Motion Token Predic… | Inspire Hand (Franka FR3); LinkerBot O6 (Unitree G1); unnamed 6-DoF dexterous hands on PN… | 6 |   | LIBERO, RoboCasa (engine/timestep not stated) | yes | 20 |   | not addressed | yes |
| `bidexgrasp_2026` | 2026 | grasp, bimanual-coord | grasp-synthesis, diffusion | bi-level QP-ADMM optimisation (region-pair init + decoupled per-hand force closure) + DDP… | Shadow Hand pair (sim); Inspire and BrainCo hands (real) |   | yes | MuJoCo | yes | 260 | 30 | measured | no |
| `deximit_2026` | 2026 | bimanual-coord, grasp, functional/tool | data-collection, BC, grasp-synthesis, trajopt | 4D hand-object reconstruction (ST2+FPose) + LLM-based (Qwen3-VL) subtask decomposition wi… | XHands (real-world deployment); exact simulation hand not explicitly named |   | yes |   | yes |   |   | constrained | no |
| `dexora_2026` | 2026 | grasp, functional/tool, bimanual-coord | VLA, diffusion, teleop-system | Decoder-only diffusion transformer (28 layers, hidden size 1024, 16 attention heads) with… | XHAND dexterous hand (paired), 12 fully actuated joints per hand, thumb and index additio… | 12 | yes | MuJoCo (digital twin of the real platform, used to generate the synthetic corpus and mirr… | yes | 20 |   | not addressed |   |
| `dexteleop0_2026` | 2026 | grasp, functional/tool, bimanual-coord | teleop-system, MPC | box-constrained QP shared-autonomy residual controller (force tracking + multi-contact fo… | Sharpa Wave (x2) | 22 | yes | NVIDIA IsaacSim 4.5 | yes | 35 |   |   | no |
| `egoscale_2026` | 2026 | grasp, functional/tool, bimanual-coord | flow, VLA | flow-based VLA (GR00T N1-style): VLM backbone + DiT action expert trained with a flow-mat… | Sharpa Wave (22-DoF); cross-embodiment target Unitree G1 (7-DoF tri-finger hand) | 22 | yes |   | yes | 10 |   |   | no |
| `force_grasp_sim2real_2026` | 2026 | grasp, reorient | RL | PPO (asymmetric actor-critic) | xHand | 12 | no | IsaacLab | yes | 70 | 2 |   | no |
| `poise_2026` | 2026 | reorient | RL | asymmetric PPO | Sharpa Wave hand | 22 | no | Isaac Lab | yes | 10 | 1 | not addressed | no |
| `simtoolreal_2026` | 2026 | functional/tool | RL | SAPG (PPO variant) | Sharpa five-fingered hand | 22 | no | IsaacGym | yes | 120 | 12 | not addressed | no |
| `teledexter_2026` | 2026 | reorient, functional/tool | RL, teleop-system | single-stage RL (SAPG) with consecutive subgoal co-tracking reward | SharpaWave (22-DoF, headline); also LeapHand (16-DoF) | 22 | no | Isaac Gym | yes | 15 |   | penalised | no |
| `toporetarget_2026` | 2026 | track-human-ref | trajopt, RL | constrained Laplacian-optimization retargeting + PPO tracking | Wuji Hand |   | no |   | yes |   |   | constrained | no |
| `unidex_2026` | 2026 | grasp, functional/tool | flow, VLA, data-collection | UniDex-VLA: a pi0-style flow-matching VLA with a Uni3D pointcloud encoder and Gemma-based… | Inspire, Leap, Shadow, Allegro, Ability, Oymotion, XHand, Wuji (8 hands in UniDex-Dataset… |   | no |   | yes | 20 |   |   | no |
| `viserdex_2026` | 2026 | reorient | RL, distillation | PPO (RSL-RL) | Allegro Hand | 16 | no | Isaac Lab | yes | 50 |   | not addressed | no |

*110 rows; 237 of 1540 cells (15%) are values no source stated.*

<!--
FIGURE 4. Taxonomy of training paradigms. A draft exists at paper/figures/fig4_taxonomy.svg,
generated by tools/make_figures.py with counts recomputed from corpus/rows. This comment is the
specification the drawn figure should satisfy. The draft already gets the frame right: four
first-level branches off "supervision for a dexterous policy", 110 method papers at the root,
branch counts of 53 for a reward function, 49 for a human demonstration, 12 for a human reference
tracked with physics and 11 for no learned policy, and a footer saying the branches are not
exclusive. Five things still need to be true of it.

1. LEAF KEYS MUST BE EXHAUSTIVE OR MARKED. The draft prints five example keys per leaf with no
   indication that the list is truncated. A reader cannot tell whether "egocentric video, no robot
   at all, 7" lists all seven. Either print every key at a leaf or append "and N more" so the
   truncation is visible. This matters most at the two largest leaves, "PPO in a GPU simulator,
   privileged state" at 32 and "synthetic demonstration generation" at 10.

2. THE CROSS-LINKS ARE MISSING AND THEY ARE THE POINT. The draft states in its footer that the
   branches are not exclusive, then draws a strict tree. Draw the overlaps as dashed curves behind
   the nodes, in the muted accent colour, each labelled with one word:
     reward-branch distillation leaf  ->  demonstration-branch architecture tags   "distil"
     reward-branch PPO leaf           ->  synthetic demonstration generation        "generate"
     egocentric video leaf            ->  human-reference branch                    "retarget"
     human-reference branch           ->  demonstration-branch architecture tags    "distil"
     no-learned-policy branch         ->  reward-branch PPO leaf                    "smooth"
     teleoperated-on-robot leaf       ->  seeded by demonstrations                  "seed"
   The fifth link carries `pang_global_planning_2022`'s proof that randomised smoothing, which is
   what a policy gradient does implicitly, and analytic log-barrier smoothing compute the same
   local model of contact. It is the only edge in the figure that is a theorem rather than a
   pipeline, and it should be drawn differently, for instance with a double dash.

3. THE ARCHITECTURE AXIS IS ABSENT. Under the human-demonstration branch, what supervises the
   policy and what shape the policy has are independent choices. Add four small tags, not full
   nodes, hanging under the branch: action chunking `aloha_act_2023`; diffusion
   `diffusion_policy_2023`, `dp3_2024`; flow matching `pi0_2024`, `groot_n1_2025`, `h_rdt_2025`,
   `unidex_2026`, `egoscale_2026`; autoregressive action tokens `openvla_2024`, `metis_2025`.
   Tag counts are 1, 14 and 8 for the first three from the `diffusion` and `flow` paradigm labels.

4. TWO LEAF ASSIGNMENTS IN THE DRAFT ARE WRONG AGAINST THE NOTES. `physhoi_2023` is placed under
   "reference as soft guidance". It is not soft guidance. It tracks a fixed reference with a
   multiplicative kinematic and contact-graph reward, and it does not randomise initialisation
   because "the HOI data may have severe collisions that eject the object". Move it to "whole
   reference including fingers", which then holds five. `omnigrasp_2024` is likewise not soft
   guidance. It tracks a generated object trajectory from a single pre-grasp pose, so it belongs
   under "object trajectory only", which then holds three. "Reference as soft guidance" should
   hold `dexplore_2025` alone, and its count of one is itself informative.

5. SCARCITY MUST BE LEGIBLE. The three leaves under "no learned policy" hold one paper each, and
   population-based training over hyperparameters holds one, `dexpbt_2023`, which the draft does
   not show at all. Add it as an annotation hanging off the PPO leaf with the count 1. Size or
   shade every leaf by its count so that a reader sees, without reading a number, that the
   demonstration branch is wide, the non-learning branch is three single papers, and automated
   reward design is two.

Palette, dark-mode handling and font stack follow the other figures in paper/figures/. All counts
are recomputed from corpus/rows/*.json at generation time and never hardcoded, so the figure
cannot drift from the corpus.
-->

# 6. Bimanual dexterous manipulation

A warning first. Of the 51 corpus method papers whose row records `bimanual: true`, four put two
parallel-jaw grippers on the robot and no dexterous hand at all: `aloha_act_2023`, `rdt1b_2024`,
`egomimic_2024` and `h_rdt_2025`. Two more report every bimanual number on grippers and show
five-fingered hands only qualitatively, `gemini_robotics_2025` and `gemini_robotics_15_2025`.
Three run a gripper on one embodiment and a hand on another, `ace_teleop_2024`, `dp3_2024` and
`open_television_2024`, whose Unitree H1 carries 6-DoF Inspire hands and whose Fourier GR-1
carries a 1-DoF jaw. Every paper below runs two multi-fingered hands unless said otherwise.

## 6.1 Why two hands is not twice one hand

When both hands hold the same object, the object closes a kinematic loop between them. Neither
hand can move without changing what the other must do. `bidexgrasp_2026` reports that the coupled
objective "often yields imbalanced solutions, where one hand dominates stability while the other
contributes marginally." `artigrasp_2023` reports simulation speed scaling "roughly quadratically
with the number of contacts," and trains each hand alone before pairing them.

Role asymmetry is an assumption almost everyone makes silently. `bidexhd_2024` states it outright:
"we assume the robot to be right-handed by default, i.e., the left hand handles the target object
and the right hand handles the tool." `twisting_lids_2024` bakes the same split into its reward,
putting reference contact keypoints on the bottle base for the left fingertips and on the lid for
the right. The bias is in the data first, since `taco_2024` recruited 14 right-handed subjects and
measures the right hand moving consistently faster.

The arms collide, and the corpus handles this by construction rather than by control.
`robopianist_2023` ships a forearm-forearm collision term that its own reward table never lists.
Two papers name arm collision as unsolved. `dexmimicgen_2024` "does not explicitly handle
collisions," and `dexman_2025` says its control parameterisation "overlooks full arm posture,"
which it needs to avoid them.

The action space doubles and the observation grows faster. `bidexhands_2022` uses a 52-dimensional
action for 18 of its 20 tasks against observations of 398 to 446 dimensions. `gr_dexter_2025`
emits an 88-dimensional chunk of arm joints, end-effector poses, hand joints and fingertips. What
the larger vector does not carry is any statement of who does what. The usual answer is one scalar
reward summed over both sides, and the cost is a compounding failure rate. `maniptrans_2025`
scores success only if both hands succeed, and its OakInk-V2 success rate falls from 58.1 percent
on single-hand sequences to 39.5 percent on bimanual ones.

## 6.2 Coordination architectures

![fig5_bimanual](figures/fig5_bimanual.svg)

Figure 5 sets the four architectures side by side with the counts on the panel borders. The
denominator is the 25 corpus papers whose notes place a learned controller on two dexterous hands.
Datasets, static grasp synthesis and the two-gripper papers are excluded.

Nineteen of 25 use one policy over both hands: the video and teleoperation pipelines
`dexman_2025`, `deximit_2026`, `bidex_teleop_2024` and `hato_visuotactile_2024`, the piano papers
`robopianist_2023`, `rp1m_2024` and `pianomime_2024`, the trackers `dexmachina_2025` and
`maniptrans_2025`, the generator `humanoidgen_2025`, and `gr_dexter_2025` with all four
`bench2dex_2026` baselines. The concentration is not the outcome of a comparison that was won.

Five of 25 give each hand its own network, and the two papers that compare the choice disagree.
`bidexhands_2022` ships the MARL baselines and finds PPO over the full observation beats HAPPO and
MAPPO "in most cases," with the gap narrowing on tasks that need both hands, because PPO "can use
all observations" where MARL sees only part. `bidexhd_2024` concludes the opposite. Its
independent PPO teachers score 74.59 percent stage-two tracking rate on trained tasks against
53.88 for a centralised policy over both observations. Both are simulation only, on different
tasks and hands, so neither settles it. `artigrasp_2023` trains one PPO policy per hand, and
`dynamic_handover_2023` and `dydexhandover_2025` use MAPPO with one agent per arm-hand system.

Two of 25 assign explicit leader and follower roles, and one of 25 expresses the policy in a
relative frame. `asymdex_2024` is the clearest case of both, and the only corpus paper that puts
either mechanism inside a policy. It gives the dominant hand full finger and wrist control,
restricts the facilitating hand to a 6-DoF base pose, and writes the dominant hand and the object
in a frame attached to the object the facilitating hand holds. That cuts the observation from 176
dimensions to 88 and the action from 52 to 26. It ablates the two mechanisms separately, which no
other corpus paper does. On Block in cup the full method scores 0.7701 over five seeds, against
0.1086 for relative frames without asymmetry and 0.0164 for asymmetry without them. Twist Lid
transfers zero-shot at 18 of 20 real trials. The real rig pairs a 16-DoF Allegro with a 6-DoF
Ability Hand because only one Allegro was available, so the roles are confounded with the
hardware. `dexmimicgen_2024` preserves relative pose too, but offline, by applying one shared
SE(3) transform to both arms' source segments when generating data.

## 6.3 Benchmarks and datasets for two hands

Two purpose-built bimanual dexterous suites exist in the corpus, four years apart.

`bidexhands_2022` is 20 tasks on two Shadow Hands in Isaac Gym, ordered by the infant age at which
humans acquire the skill, at 2048 environments and a reported 30,000-plus FPS. Its measurement
discipline is weaker than its coverage. It reports reward and normalised score, never a success
rate. The only success flag in the code is `goal_dist < 0.03`, a 3 cm object-to-goal test that
ignores orientation and exists only in the four catching tasks. Any success rate later work
attributes to Bi-DexHands comes from that flag or its own definition.

`bench2dex_2026` is the more instrumented of the two. It runs 26 long-horizon tasks in Isaac Lab
across 12 arm-and-hand embodiments, with roughly 1.3K teleoperated demonstrations in eight
modalities, including a ray-cast tactile image that maps all 12 hand geometries into one
representation. Success needs the terminal predicate held for 0.5 s. Matched, GR00T N1.5 leads at
631 of 1300 rollouts, 48.5 percent, against ACT at 29.5, π0.5 at 27.3 and Diffusion Policy at
12.9. Under combined perturbation those first two compress to 19.8 and 19.7. Tasks are not crossed
with embodiments, so no contrast isolates the hand, and the authors state the hand and tactile
models are not calibrated against matching physical hardware.

Ten corpus rows are bimanual datasets, and five are two-hand interaction capture. `arctic_2022`
gives 339 mocap sequences of 11 one-DoF articulated objects held in both hands, and deliberately
labels over-shooting vertices as in contact, so its ground truth records interpenetration as
contact. `taco_2024` gives 2.5K bimanual tool-use sequences fitted markerlessly under an
attraction loss and a penetration loss the paper says trade against each other. `oakink2_2024` is
the only corpus dataset publishing a penetration number for its own annotations, a mean depth of
0.25 cm over its 627 long-horizon sequences. `hot3d_2024` gives 833 egocentric minutes with
mocap-grade poses for both hands and up to six objects, and `gigahands_2024` gives 2,034
markerless minutes from 56 subjects, neither with a penetration metric. These five feed the
tracking work here: `dexmachina_2025` and `artigrasp_2023` from ARCTIC, `bidexhd_2024` from TACO,
`maniptrans_2025` from OakInk-V2 and `dexman_2025` from both.

## 6.4 Methods on the same axes

Table 7 carries the bimanual papers on the same columns as every other method here, and three of
those columns are worth reading together.

Real trials. `asymdex_2024` reports 20 per task, `hato_visuotactile_2024` 10 per condition,
`dexmimicgen_2024` 20 on a Fourier GR1 and `bidexgrasp_2026` 260 across 30 objects.
`maniptrans_2025` reaches real Inspire hands by open-loop replay with no trial count and no
success rate. Ten bimanual method rows have no real robot at all, including `dexmachina_2025`,
`dexman_2025`, `bidexhd_2024` and all three piano papers.

Penetration. Most bimanual rows read "not addressed." `bimangrasp_2024` gates on it, failing any
grasp whose total penetration across hand-object, self and inter-hand exceeds 1.5 mm, and reports
that "penetration remains the primary cause of grasp failure." `bidexgrasp_2026` reports it as a
number, 0.15 to 0.20 cm maximum depth for its own grasps. `deximit_2026` carries a named hand-hand
penetration term in its grasp-synthesis objective. `dexmachina_2025` resolves it once, replaying
retargeted joints against a fixed object "to eliminate object penetrations" and measuring nothing
during rollout. `artigrasp_2023` declines the metric outright, because its baselines "include a
physics simulation which exhibits no interpenetration."

Comparability. `bimangrasp_2024` reports 54.03 percent success in Isaac Gym at friction 3.
`bidexgrasp_2026` re-runs the same grasps in MuJoCo at friction 0.6 and gets 26.80 percent, at
1.52 cm penetration depth. Neither number transfers. `dexmachina_2025` likewise re-implements the
`maniptrans_2025` curriculum in Genesis and finds "no clear improvements over the no-curriculum
setting."

## 6.5 Handover and in-hand transfer

Handover is the one bimanual task where the hands are unambiguously asymmetric, because one gives
and one receives. All three corpus handover papers use a single shared reward across giver and
receiver. None defines separate objectives for the two roles.

`dynamic_handover_2023` states one formula, r = r_dis + r_linvel + r_torque, and never says
whether thrower and catcher receive different decompositions of it. `dydexhandover_2025` is
explicit that they do not: "Both hands share aligned objectives, forming a fully cooperative
relationship," with one weighted sum feeding both agents. Only the thrower gets an extra KL
regulariser toward a policy pretrained on human throws, which constrains style and not role.

The third case is weaker still. In `dexterous_handover_2025` only the receiver is learned. The
giver is a UR5e with an Allegro hand that "holds the object without moving during the whole
episode." There is one agent, one reward and no second policy, and its row in Table 7 accordingly
records `bimanual: no`. The 94 percent often attached to this paper needs its conditions. It is
Total Success, which counts "Indetermination" cases where the simulator failed to resolve
collisions and the object clipped through the giver's hand, on the short prism, in simulation,
over 100 episodes, with no real robot in the paper.

Nothing in the handover literature measures contact quality. Contact appears only as a positive
signal, a boolean per-phalange touch in `dexterous_handover_2025` and a boolean contact reward in
`dydexhandover_2025`. The two systems that do handover well sidestep the problem.
`hato_visuotactile_2024` reaches 10 of 10 on a real slippery handover by imitating teleoperation
with fingertip touch sensing and no physics model. `humanoid_sim2real_recipe_2025` stages its
reward with a discrete variable switching which hand's fingertips are scored, and still calls
handover its hardest task at 52.5 percent real success.

## 6.6 What transfers from single-hand work

The training recipe transfers intact. PPO with thousands of parallel environments, an asymmetric
critic on privileged state, domain randomisation and distillation into a vision policy is the same
in `twisting_lids_2024` and `humanoid_sim2real_recipe_2025` as in section 5.2. Reward forms
transfer literally, and the contact-goal reward r_contact = Σ 1/(1+α d) appears in both.

Multi-task learning does not transfer, and the bimanual benchmarks show it clearest.
`bidexhands_2022` finds multi-task PPO and ProMP fail on MT4, MT20, ML4 and ML20.
`robopianist_2023` finds F1 on the shared training song drops "from roughly 0.7 F1 for 1 song to
almost 0 F1 for 16 songs," with no positive transfer "regardless of the size of the pre-training
tasks."

Single-hand evaluation does not transfer either. Success criteria compound, because
`maniptrans_2025` fails a trajectory "if either hand fails to meet these conditions." And
object-centric metrics cannot say which hand caused the failure. `bidexhd_2024` scores the steps
where both objects track their references, and `dexmachina_2025` averages ADD across object parts
before an AUC. Both say whether the task worked and nothing about which hand lost it.

One failure mode has no single-hand counterpart. Two hands can penetrate each other, and the
corpus almost never looks. Three papers carry an inter-hand penetration term, and all three are
static grasp synthesis: `bimangrasp_2024`, `bidexgrasp_2026` and `deximit_2026`. Not one learned
bimanual controller in the corpus measures or penalises hand-hand penetration during a rollout.
`pianomime_2024` ships a flag that turns inter-hand collision off in the physics.

# 7. Evaluation: how we would compare these methods

## 7.1 What the field reports, and why the numbers do not compare

Of the 110 method rows in the corpus, 87 report a real-robot experiment, which is 79 percent.
Only 55 of those 110 state how many real trials produced the headline number, which is 50
percent. Thirty-two state a count of unseen test objects, 29 percent. Seventy-nine state a
success criterion, 72 percent. Sixty-one released code, 55 percent. Figure 6, generated as
`paper/figures/fig6_reporting.svg`, draws these five shares from `corpus/rows` against the same
denominator. A bar there is evidence that a quantity was stated, not that the work handled it
well.

![fig6_reporting](figures/fig6_reporting.svg)

The gap between the first two bars is the one that matters. Thirty-two of the 87 papers with a
real robot never say how many times they ran it. A percentage with no denominator cannot be
given an interval, so it cannot be compared with anything.

Where the denominator is stated it is small. The 55 counts run from 5 to 1287, with a median of
20 and quartiles at 10 and 70. At 20 trials a reported 60 percent carries a 95 percent Wilson
interval of 39 to 78 percent, and a reported 80 percent an interval of 58 to 92 percent. Two
methods separated by 20 points at the median trial count are not separated at all. This has not
improved: 25 of the 45 rows from 2025 and 2026 state a trial count, and their median is also
20.

The denominators also sit on different hardware. The 103 method rows that name their own hand
name 52 distinct hands between them, with Allegro in 35, Shadow in 21, Inspire in 19 and LEAP in
12. A success rate on a 16-degree-of-freedom Allegro and a success rate on a 6-actuator Inspire
hand are not measurements of the same thing.

Nor are the criteria. `dexverse_2026` counts PickCube a success when the cube is "lifted at
least 0.20 m above its resetting height". `bench2dex_2026` requires its terminal predicate to
hold for a continuous dwell time of 0.5 s, to reject transient contacts. `colosseum_2024`
counts an episode successful "if the model completes the task fully". `dextrack_2025` reports
every success rate as a pair under two threshold sets, which on GRAB gives 46.70 and 65.48
percent for the same rollouts. Thirty-one method rows state no criterion at all.

## 7.2 The axes that matter

Seven quantities dissociate in the published data, so they have to be reported separately.

**Task success.** Binary success discards the difference between near-misses and inaction.
`beyond_binary_success_2026` puts it plainly: "a policy that completes 90% of the task is
clearly better than a policy that is frozen the whole time, yet their success rates would be
identically 0%". In `kress_gazit_policy_eval_2024` policy C scores 17 percent overall on the
pancake task while picking up the spatula and flipping the pancake in 23 of 23 attempts.

**Robustness to perturbation.** `colosseum_2024` measures a 30 to 50 percent success drop under
single perturbation factors and at least 75 percent under all 14 together. In `bench2dex_2026`
GR00T N1.5 leads the matched condition at 48.5 percent and falls to 19.8 percent under combined
shift, while π0.5 goes from 27.3 to 19.7 and retains the most at 72.1 percent. The ranking at
the anchor is not the ranking under shift.

**Generalisation to unseen objects.** Only 32 rows state a count and the median is 14.5 objects.

**Physical plausibility of the contact.** Eleven of the 110 rows address it, and Section 7.3
takes it apart.

**Sample and wall-clock cost.** Thirty-one of 110 rows state a parallel environment count and 18
a simulated episode count. `robopianist_2023` is the exception, at 5 million samples per song and
roughly 5 hours per run on four Tesla K80 GPUs.

**Real-robot transfer.** Simulated rank order is not real rank order. `autoeval_2025` scores
Open-π0 on put-eggplant-in-sink at 6 of 50 in SIMPLER and 47 of 50 on the real WidowX.
`suresim_2025` states the limit directly: "the simulation-to-real gap precludes rigorous
statistical inferences about real-world outcomes from simulation results alone".

**Reproducibility.** Fifty-five percent released code, and 37 of the 110 rows record a
disagreement between the paper and that code. `physhoi_2023` lists a non-zero
object-orientation weight for GRAB in Table 4, and its released `compute_humanoid_reward`
hard-sets the orientation error to zero, so the reward that produced the published numbers
tracked object position only.

## 7.3 Physical plausibility as a first-class metric

Eleven of the 110 method rows handle interpenetration in any form: three penalise it, three
measure it, five constrain it. Six are grasp synthesisers or trajectory optimisers, namely
`bidexgrasp_2026`, `bimangrasp_2024`, `deximit_2026`, `pang_global_planning_2022`,
`toporetarget_2026` and `unidexgrasp_2023`, and `castro_sap_contact_2021` is a contact model
rather than a controller. That leaves four closed-loop policies in the whole corpus:
`clutterdexgrasp_2025`, `dexmachina_2025`, `dextrack_2025` and `teledexter_2026`.

The reason the number is four is a measurement trap. A quantity a policy optimises cannot also
judge it, because the policy learns the measure rather than the property the measure stands for.
`physhoi_2023` documents the failure in the clean direction. Its kinematic imitation reward was
maximised by not touching the object at all, because contact perturbed the reference trajectory:
"the policy may learn not to touch the object and falls into a local optimal". A contact-graph
reward closed the hole, and that reward reads a force threshold rather than geometry, so it
constrains contact presence and says nothing about penetration depth.

`dextrack_2025` shows the trap in the other direction. It defines a maximum hand-object
penetration depth over all frames in its Appendix B, and applies it only to the input kinematic
references, as one component of a reference-quality score. No penetration number appears for any
of its own rollouts, in simulation or on the LEAP hand. Tolerance of the failure is then reported
as a result: "Despite severe hand-object penetrations in Figure 4c and Figure 4a, the hand still
interacts effectively with the object, highlighting the resilience of our tracking controller".

`toporetarget_2026` is the strongest case in the corpus and still stops one step short. It
constrains penetration during retargeting with a 1 mm soft tolerance and a 30 mm hard bound,
and it reports two numbers on 25 ContactPose grasps: a maximum penetration of 1.07 mm and 0.00
percent of frames above 2 mm, against 22.22 mm and 96 percent of frames for its GeoRT baseline.
Then a PPO controller tracks those references, and its reward and its five termination criteria
govern object pose, link position and joint error, never penetration. The constrained quantity
is the reference, and the rollout is not re-measured.

Definitions are not shared either. `grab_2020` estimates contact by proximity, because "contact
cannot be directly observed", with a 4.5 mm tolerance, and reports that "'Use' grasps have
3.25 ± 0.68 mm average penetration", without saying whether 3.25 mm is a maximum, a mean or a
median. `oakink_2022` supplies the fullest published vocabulary:
penetration depth, solid intersection volume and simulation displacement. Its Table 3 scores the
GRAB GrabNet split at 2.53 cm penetration depth, against GRAB's own 3.25 mm. The two differ by a
factor of about eight, and neither source states its distance function precisely enough to
reconcile them.

The analytic tradition scored a grasp without simulating it, and `ferrari_canny_1992` and
`roa_suarez_grasp_quality_2015` are its wrench-space reference points. Neither could be
obtained. The first DOI fetch returned HTTP 202 and the second a Springer JavaScript
interstitial, so both are cited by metadata only and no definition here rests on their contents.
The learned literature has not replaced that tradition with anything it measures on its own
rollouts. Penetration is a quantity between meshes, so it needs a simulator or a mesh
reconstruction, and the protocol below treats it as a simulation-only axis.

## 7.4 Statistics

`kress_gazit_policy_eval_2024` is the field's reference protocol and it prescribes process, not
numbers. Write the success criteria before the run and have someone other than their author
score the runs. Match initial conditions with image overlays. Interleave the policies blind
within one session. Report counts rather than percentages, alongside the initial conditions and
the failure modes. Use a posterior over the Bernoulli parameter instead of a point estimate. It
prescribes no minimum trial count anywhere and no frequentist confidence-interval width
anywhere. Its own example report uses 10 initial conditions with two runs each, 20 evaluations
per policy, and its worked case shows what 20 buys. Pancake success of 15 of 18 against 11 of
17, nominally 83 against 65 percent, leaves a 0.11 posterior probability that the worse policy
is actually better. At 150 of 180 against 110 of 170 the same rates separate.

`lbm_careful_examination_2025` supplies the missing numbers by fiat rather than derivation: 50
rollouts per task per policy per condition on hardware, 200 in simulation, blind, with
randomised policy order inside per-initial-condition bundles. It replaces confidence intervals
with Beta-posterior violins and corrects all pairwise tests under Bonferroni. Its own warning is
the strongest sentence in this literature: "there is significant risk that many robotics papers
are measuring statistical noise due to insufficient statistical power".

The rest fall short of their own advice. `roboarena_2025` runs 612 double-blind pairwise
comparisons across seven institutions and 4284 rollouts, and reports no confidence intervals and
no per-policy trial counts. `colosseum_2024` evaluates 235 test sets at 25 episodes each with
"one training seed and one evaluation seed" per baseline and gives no intervals in simulation.
`autoeval_2025` runs 50 trials per policy per task and calls ±10 percent "the natural variance
of robot evaluations", without giving the formula behind the intervals it plots.

Two papers do give usable numbers. `suresim_2025` pairs real and simulated trials and de-biases
the simulation with a rectifier, saving more than 25 percent of hardware trials at a paired
correlation of 0.70 and nothing at all at a correlation near zero. Its decision rule is exact:
combining helps only when the rectifier variance is below the variance of the real evaluations.
`beyond_binary_success_2026` gives the largest saving. On the LBM rubrics its sequential test on
graded scores cuts simulated evaluation by about 70 percent and hardware by about 45 percent,
286 trials against a nominal 500, with per-task decisions landing in 12 to 36 paired trials. On
RoboArena's data a 30-point gap on continuous progress scores reaches significance in 18 trials,
while a 20-point gap on binary success needs about 80.

## 7.5 A proposed protocol

Fix the width first, then read off the count. Take a 95 percent Wilson interval on a single
reported rate, at the worst case of p = 0.5. A half-width of 20 points needs 21 trials, 15
points needs 39, 10 points needs 93 and 5 points needs 381. Ten points is the coarsest width at
which a claim that one method beats another survives a sceptical reader, so the absolute-rate
minimum is 93, rounded to 100. At 100 trials a reported 80 percent has an interval of 71 to 87
percent, and a reported 50 percent has 40 to 60.

For the A/B comparison the relevant calculation is power, not width. A two-sided two-proportion
test at α = 0.05 with 80 percent power needs 93 trials per arm to separate 50 from 70 percent,
169 to separate 50 from 65, and 387 to separate 50 from 60. So 100 trials buys a 20-point effect
and nothing finer, and the protocol says so rather than implying more. One hundred is a cap and
not a bill, because on a graded score a sequential test reached its decision in 12 to 36 paired
hardware trials in `beyond_binary_success_2026`.

Simulation is cheap, so simulated cells take 200 episodes, giving a 6.9-point half-width.
Perturbation axes are screened rather than certified, so 40 per axis at a 15-point half-width is
enough to rank them and pick the two worst for hardware. For unseen objects the resampling unit
is the object and not the trial, so 20 objects at 5 trials each gives 100 trials and an
object-level interval near 20 points. A 10-point claim about an object distribution needs about
93 objects. Seven of the 32 rows that state an unseen count reach that: 225 in `bimangrasp_2024`,
241 in `resdex_2024` and `unidexgrasp_2023`, 360 in `dexgraspvla_2025`, 500 in `dexmv_2021`,
2029 in `clutterdexgrasp_2025` and 503409 in `graspxl_2024`. For a continuous score the
half-width is 1.96 standard deviations over the square root of the count, so 100 rollouts give
±0.20 standard deviations, and the unit is the rollout because frames within one are correlated.

### Table 8. The proposed evaluation protocol

| axis | what is measured | how | minimum trial count | reported alongside it | why |
|---|---|---|---|---|---|
| Task success | fraction of episodes meeting a criterion, and a graded rubric score in [0,1] over equally weighted milestones | criterion written before the run by the designer and scored by someone else; terminal predicate held for a 0.5 s dwell; initial conditions matched by image overlay; policies interleaved blind in one session | 100 real and 200 sim, per task per policy per condition | Wilson 95 percent interval, raw counts, the criterion verbatim, the rubric, the initial-condition protocol | a rate without a denominator and an interval cannot be compared; the rubric separates a near-miss from inaction |
| Robustness | success under each perturbation axis, reported as the ratio to the unperturbed anchor | axes that must not change the action and axes that must are scored separately; ranges stated; anchor replayed exactly | 40 per axis per policy in sim; the two worst axes repeated at 100 real | both absolute rates, the ratio, the axis ranges, and which split each axis is in | the ranking at the anchor is not the ranking under shift |
| Unseen objects | mean over held-out objects of per-object success | objects drawn from a stated distribution disjoint from training; bootstrap over objects, not trials | 20 objects at 5 trials for a screening claim; 93 objects for a 10-point claim | the object list, per-object rates, the bootstrap interval, the object-count caveat | the resampling unit is the object, so trial counts overstate the precision |
| Physical plausibility | maximum and mean hand-object penetration depth per rollout, and the fraction of frames above 2 mm | dense surface sample against the object mesh or SDF, computed on the policy's own rollouts by code that never entered the reward or the termination rule | 100 rollouts, simulation only | interval over rollouts, sample density, threshold, solver depenetration settings, and at least one rendered rollout | a measure the policy optimised is not evidence about the policy |
| Sample and wall-clock cost | environment steps and wall-clock to the checkpoint that produced the headline number | counted to that checkpoint, not to the end of training; GPU model and count stated | 3 training seeds | the range over seeds, and the statement that 3 seeds is a range and not an interval | training variance is not rollout variance and the two are routinely conflated |
| Real-robot transfer | paired real and simulated outcomes on matched initial conditions, and their correlation | the same 100 initial conditions run in both; report the paired correlation and the rectifier variance | the 100 real trials, paired to 100 sim | correlation, rectifier variance against real variance, and whether simulation narrowed the interval | a simulator earns a real-world claim only through its measured paired correlation |
| Reproducibility | code, checkpoints, and the exact config that produced the headline run | diff the paper's stated objective against the released config and name the file and line of every disagreement | not a trial count | the named file and line for each disagreement, or an explicit statement that none was found | 37 of the 110 method rows already carry such a disagreement |


## 7.6 Table 9, an empty results matrix

The rows are the 12 most-mentioned dexterous-hand policy methods in the corpus, ranked by how
many other corpus papers name them in their parsed text. Parallel-jaw work is excluded, and so
is any row whose only contribution is a teleoperation interface, which drops `dexpilot_2020`.
Mention counts are counts of mentions and not of use, as `METHOD.md` records, and the ranking is
recomputed by `tools/make_eval_tables.py` rather than fixed by hand.

Every cell is empty. This survey re-ran nothing, and no cell can be filled from a published
number, because no number in the corpus carries the interval, the denominator and the criterion
that Table 8 asks for.

### Table 9. The matrix, for someone else to fill

| method | task success | robustness | unseen objects | physical plausibility | cost | transfer | reproducibility |
|---|---|---|---|---|---|---|---|
| `openai_dexterity_2018` | | | | | | | |
| `dexmv_2021` | | | | | | | |
| `dapg_2017` | | | | | | | |
| `dextreme_2022` | | | | | | | |
| `dexcap_2024` | | | | | | | |
| `anyteleop_2023` | | | | | | | |
| `hora_2022` | | | | | | | |
| `unidex_2026` | | | | | | | |
| `unidexgrasp_2023` | | | | | | | |
| `visual_dexterity_2022` | | | | | | | |
| `dime_2022` | | | | | | | |
| `rotating_without_seeing_2023` | | | | | | | |

*12 rows, 84 cells, all 84 empty. Rows are the 12 most-mentioned dexterous-hand policy methods in the corpus; mention counts are counts of mentions, not of use.*


## 7.7 What would have to be true

The bill comes first. Per method and per task the protocol asks for 100 real rollouts on the
matched set and 100 on the unseen-object set, with robustness and plausibility absorbed by
simulation. A two-policy comparison on three tasks is 1200 real rollouts, and at one minute per
rollout including the reset that is 20 hours of robot time, before failed resets, repairs and
scoring. `autoeval_2025` ran about 850 episodes in 24 hours on a WidowX with three human
interventions, and had to pause 20 minutes every 6 hours once the motors overheated. A
tendon-driven multi-finger hand is more fragile, so 20 hours of rollouts is a week of calendar
time.

That bill is large but not unprecedented. `autoeval_2025` records that evaluating OpenVLA
against its baselines took more than 2500 rollouts and more than 100 hours of human labour
across three institutions, and `lbm_careful_examination_2025` analysed about 1800 real rollouts
across nine hardware stations. What is unprecedented is paying it for a single dexterous-hand
paper, where the corpus median is 20 trials and has not moved since 2022.

Four things would have to change. Reviewers would have to reward 100 trials on one task over 20
trials on five, and nothing in the corpus suggests that is happening. The loop would have to be
automated, and `autoeval_2025` shows it is buildable for a gripper at one to three hours of
setup, while stating that it supports binary success only and no robustness axes. Simulators
would have to expose penetration to code outside the reward, which Table 4 records that only
some do. And the comparison would have to be sequential, because the savings in
`beyond_binary_success_2026` are the only reason 100 is a cap rather than a cost.

Four limits apply to the proposal itself. This survey re-ran no method, so every count in
Table 8 is derived from an interval width and from other people's measurements, and Table 9 is
empty because we filled no cell. The counts are worst-case at p = 0.5, so a method near 90
percent needs fewer trials for the same width and a method near 50 percent needs all 100. The
perturbation axes are borrowed from `colosseum_2024` and `simpler_2024`, which run parallel-jaw
grippers on rigid objects, where `simpler_2024` found physical parameters moved success rates by
at most 15 percent. That is the sensitivity expected to grow with multi-finger contact, and
nobody has measured it. The 2 mm penetration threshold is taken from `toporetarget_2026` with
no independent justification, and the captured human grasps in
`grab_2020` sit above it at 3.25 mm, which makes 2 mm a simulator convention rather than a
physical bound.

# 8. Gaps

## 8.1 Released code does not implement the published reward

Sixty-one of the 110 method rows released code. Thirty-seven of those carry a recorded
disagreement between paper and repository, but only some of those are the paper's fault. Each was
classified against its note. Sixteen are true contradictions, where the paper states one value and
the shipped code demonstrably states another, and fifteen of the sixteen are high confidence. Seven
are cases where the relevant code was never released, so nothing could be compared. Three are
version skew, where the repository is a different generation from the one the paper describes.
Two are inconsistencies inside a paper with no code involved. The remaining nine are limitations of
this survey rather than findings about the work: the repository holds the component, but the parse
captured only signatures or a truncated body, so the comparison could not be made. Sixteen is
therefore the number to quote, and it is a floor, because the forty-nine rows that released nothing
cannot be checked at all.

The sharpest case is `physhoi_2023`. Its Table 4 gives a nonzero object-rotation weight of 0.1 for
GRAB, and the released `compute_humanoid_reward` sets that error to `torch.zeros_like` with the
real computation commented out. The term is inert, so the reward behind the 95.4 percent success in
Table 2 tracked object position only. Its success criterion is position-only too, so the evaluation
could not have caught it. The shape recurs. `dexpbt_2023` ships
`hand_delta_penalty *= self.distance_delta_rew_scale * 0  # currently disabled`.
`omnih2o_2024` gives a stumble weight of -0.00125 in Table 15 and ships -1250. `hora_2022` says it
in its own README: "The reward number in this repository are higher than what is reported in the
paper."

What would close it: print the reward table generated from the released config at a named commit
and cite that commit, so a reviewer diffs two artefacts instead of reading two documents. Table 5
marks each cell as paper, code, or both, and that mismatch column is the one to read.

## 8.2 No method reports interpenetration for its own policy's rollouts

Eleven of the 110 method rows handle interpenetration at all. Eighty-three notes record it as not
addressed and 16 do not settle it. Seven of the 11 do the work offline, in a grasp synthesiser or a
trajectory optimiser.

The best cases stop before the policy runs. `toporetarget_2026` measures penetration depth and
constrains it by signed distance during retargeting, then does not re-measure after its RL tracker
executes. `teledexter_2026` and `dexmachina_2025` do the same. `unidexgrasp_2023` reports
penetration depth for synthesised grasp proposals, which its note states is not a reward term for
the execution policy. `dextrack_2025` applies its Appendix B formula only to input references, and
gives its own rollouts prose: "Despite severe hand-object penetrations in Figure 4c, the hand still
interacts effectively with the object." Those references are not clean. TopoRetarget's Table 1,
over 25 ContactPose grasps, gives DexPilot 11.87 mm maximum penetration with 88 percent of frames
past 2 mm, and GeoRT 22.22 mm with 96 percent.

What would close it: report maximum and mean penetration depth over the evaluation rollouts, on a
dense surface sample, using a measure the policy never optimised.

## 8.3 Reward weights are not recoverable from what was published

`robot_synesthesia_2023` states its six reward weights only as the symbols c1 through c6, called
"tuned hyper-parameters". No numeric value appears anywhere and no code was released.

Five further papers render their reward equations as images: `poise_2026`, `simtoolreal_2026`,
`rotating_without_seeing_2023`, `clutterdexgrasp_2025` and `force_grasp_sim2real_2026`. None
released code. A human reading the PDF can read those equations and our converter cannot, so this
part of the gap is partly an artefact of our own pipeline, as `paper/METHOD.md` records. What is
not an artefact is that with no code, no machine-readable copy of the weights exists anywhere.
Across the corpus, 54 of 110 method rows state no reward-term count at all.

What would close it: ship the weights as a supplementary YAML or JSON file generated from the
config that trained the reported run.

## 8.4 The evaluation-methodology literature contains no dexterous hand

Seven corpus rows are evaluation protocols and not one uses a dexterous hand. `suresim_2025` uses a
Franka parallel-jaw gripper and the other six state no hand. The most careful,
`lbm_careful_examination_2025`, runs 50 rollouts per task per policy per condition on a bimanual
Franka with parallel-jaw grippers.

The prescriptive papers do not prescribe enough. `kress_gazit_policy_eval_2024` gives no minimum
trial count and no confidence-interval width, and its own report uses 10 initial conditions run
twice each. `roboarena_2025` reports no confidence intervals and no per-policy trial counts. Thirty-one of 110
method rows state no success criterion. Of the 87 with a real robot, 32 state no trial count, and
the median across the 55 that do is 20.
`dynamic_handover_2023` backs its real-robot claim with 15 attempts, 3 seeds of 5 trials, against a
simulation number computed from 500.

What would close it: run the Table 8 protocol once, on one in-hand reorientation task with one
16-DoF hand, and release the rollouts as the first row of Table 9.

## 8.5 Generalist policies are largely not evaluated on hands

Sixteen method rows are vision-language-action models, and five report no dexterous-hand result at
all: `openvla_2024`, `pi0_2024`, `pi05_2025`, `pistar06_2025` and `gemini_robotics_2025`. Gemini
Robotics fine-tunes to the Apollo humanoid and shows it in Figure 27 with no success rate or trial
count anywhere.

The ones that use hands use small ones. Seven VLA rows state a hand DoF count and the median is 6.
Among RL method rows 44 state a DoF count, the median is 16, and 34 of the 44 are 16 or above.
`gemini_robotics_15_2025` does report Apollo quantitatively, at success rates of 0.64 down to 0.40
across five generalisation axes, and never states that hand's DoF or vendor. That number cannot be
placed against any row of Table 2.

What would close it: one dexterous-hand task inside the standard generalist evaluation suite, with
the hand's DoF and vendor named in the same table as the number.

## 8.6 Hardware is multiplying faster than the software that carries it

Tables 2 and 3 hold 33 hands. The 14 simulator rows ship six distinct real hands between them:
Shadow, Allegro, Ability, Inspire, Delto and TriFinger. The 110 method rows name 79 distinct hand
strings. Fourteen of the 33 table hands appear in at least one method row and 19 appear in none.
That match is our own string matching over the `hand` field, so an unnamed hand would be missed.

The cost collapse has not reached the method literature. `ruka_2025`, `ruka_v2_2026`,
`orca_hand_2025`, `bidexhand_2025` and `dexhand_open_source_2023` appear in no method row here, and
`leap_hand_2023` is the counterexample at 12. The benchmarks built to compare across hands do not
describe them. `bench2dex_2026` covers 12 hands and `dexverse_2026` covers 6, and neither states a
DoF count for any hand or a physics timestep. `mujoco_playground_2025` ships a tendon-driven Aero
Hand its paper never mentions, so its code and its paper disagree about what exists.

What would close it: a conformance suite for hand models, with one URDF or MJCF per hand, fixed
joint-limit, mass and collision checks, and a published pass or fail per engine.

## 8.7 Announced hands cannot be checked

Fourteen of the 33 hands are neither sold nor open. Of those 14, only 2 state a fingertip force,
only 4 a weight, and only 9 a DoF count. Twenty-five of the 33 rows rest on something other than a
paper.

Four vendor pages are gone while their numbers circulate. The `agibot_omnihand_2025` store pages
returned HTTP 404 and the stored markdown holds no product text. `daxo_muscle_v0_2025` returned 404
at its vendor domain, so every fact on that row comes from a third-party catalogue. The
`figure_03_hand_2025` launch page 404s, and the tracker page that remains gives 20 DoF as a
robot-level total against the bibliography's 16 per hand. `linkerbot_l20_2025` 404s too, and the
22-DoF figure for `tesla_optimus_hand_2025` is a journalist's arithmetic over a patent paraphrase.
No announced humanoid hand appears in any method row. `clutterdexgrasp_2025` names an "AgiBot
dexterous hand", and the AgiBot pages 404, so it cannot be matched to Table 3.

What would close it: a dated PDF datasheet with a measured fingertip force and the fixture used to
measure it.

## 8.8 Bimanual work runs on one coordination architecture, and one paper has ablated it

Fifty-one method rows are bimanual, and 15 of their notes state a coordination architecture at all.
Of the 12 that describe a learned controller, 9 are a single policy over a concatenated two-hand
observation, among them `dexmachina_2025`, `dexman_2025` and `gr_dexter_2025`. `bidexhd_2024` is
the one decentralised design, a two-agent Dec-POMDP trained with IPPO, and it reports its own
centralised variant scoring lower. `asymdex_2024` is the only paper that ablates the architecture,
and its symmetric monolithic baseline scores 0.0429 against 0.7701 for the asymmetric
relative-frame design on Block in cup over five seeds. The dominant architecture has been tested
once and lost.

Handover is narrower still. All three handover papers share one reward across giver and receiver,
with no per-agent split in `dynamic_handover_2023` and none in `dydexhandover_2025`, which states
that "each policy receives feedback through a shared reward". `dexterous_handover_2025` trains only
the receiver against a scripted UR5e giver that never moves. Its 94 percent is total success
including indeterminate outcomes, in simulation, N=100, on one object outside the training
distribution, with no real-robot experiment.

What would close it: one handover task, three architectures, the same hand and the same seeds, with
separate giver and receiver returns reported.

## 8.9 Human data does not port across hands, and the map is usually unstated

Fifty-three of the 110 method rows use human data, and they name 45 distinct hand strings between
them. Only 17 of those 53 state a retargeting objective. Across all 25 rows that state one, the
objectives do not agree. `anyteleop_2023` and `dexmv_2021` minimise a fingertip keypoint-vector
energy under joint limits. `hudor_2024` treats human fingertip positions as Cartesian targets with
no kinematic correspondence. `dexumi_2025` learns a per-joint regression from exoskeleton encoders.
`egozero_2025` and `humanoid_policy_human_policy_2025` retarget nothing and define a shared
representation instead. Table 6 gives each objective in one clause, and the column does not
cluster.

More correspondence is not better. `objdex_2024` retargets the wrist only and beats both finger
joint mapping and fingertip mapping, and its ablation adding a fingertip-matching reward "does not
yield benefits and even leads to lower performance".

What would close it: a retargeting benchmark in TopoRetarget's form, reporting contact precision,
contact alignment, maximum penetration and share of frames past 2 mm, per hand and per dataset.

## 8.10 Failure modes are reported as prose or not at all

`kress_gazit_policy_eval_2024` recommends reporting failure categories, their frequency and a
narrative description. Two method rows do something like it. `okami_2024` splits its 12 trials per
task into missed grasping and failed completion. `penspin_2024` names one recurring failure in a
table caption, a 90-degree rotation followed by a drop. No other method row's note records a
failure taxonomy.

This gap is the weakest evidenced of the ten, and the weakness is ours. The note template has a
field for author-stated limitations and none for a per-trial failure breakdown, so such a table
could have been read without being recorded. Treat the count as a prompt to re-check, not a rate.

What would close it: publish the per-trial outcome file, one row per rollout with a labelled
failure category, beside the success rate it explains.

# 9. Conclusion

The binding constraint on this field is not ideas. It is verification. Sixteen of the 61 method
papers that released code contradict their own paper about the objective that was trained, and the
49 that released nothing cannot be checked at all. Sixteen is a floor twice over, because a further
nine disagreements could not be resolved by our own parse and are withdrawn rather than counted. A reward table in a paper is a
claim about a document, not about a run. `physhoi_2023` is the case to remember, because the term
its table weights at 0.1 is set to zero in the code, and its own success criterion could not have
detected that.

The second finding is that the quantity most specific to dexterous manipulation is the one nobody
measures. Contact is what separates a hand from a gripper. Eleven of 110 method rows address
interpenetration, only four of them inside a closed-loop policy, and not one reports a penetration
number for its own trained policy's rollouts. No published penetration measurement in this corpus
is even of a hand grasping an object. `dextrack_2025` has
the formula and points it at its inputs.

The third is that hardware and software have come apart. Tables 2 and 3 hold 33 hands, the
simulators ship six between them, and 19 of the 33 appear in no method row. The generalist policies
that were meant to absorb all of this mostly do not use hands, with five of 16 VLA rows reporting
no dexterous-hand result at all.

What this survey cannot establish is which method is better than which. It re-runs nothing, and
Section 7 argues the published numbers do not compare. Five works are paywalled and no claim here
rests on them. Six papers' reward weights defeated our converter while remaining legible to a human
with the PDF, so that count measures our pipeline as much as it measures them. The failure-mode
count in Section 8.10 is a floor set by a note template, not a rate.

Three things to do next week, cheapest first.

If you are publishing, generate the reward table from the config that trained the reported run,
print it, and cite the commit. State the trial count, state the success predicate, and release the
per-trial outcomes. None of that needs a GPU.

If you are running experiments, measure penetration depth over your evaluation rollouts on a dense
surface sample, and never let that measure become a reward. `toporetarget_2026` shows what the
number looks like when someone takes it seriously, and what the widely used retargeters look like
when nobody does.

If you are choosing hardware, pick from the six hands a simulator already ships. An announced hand
has no URDF, no datasheet that can be checked, and no paper in this corpus that used it.


---

## Appendix A. Method

The survey is written from a corpus that lives on disk. No claim about a paper is made from
memory; each traces to a note, each note to a parsed markdown file, and each markdown file to a
PDF or repository with a recorded hash or commit.

## Selection
Six topic-specific bibliographies were assembled in parallel (simulators and physics, hands and
vendors, reinforcement learning, imitation and human data, bimanual, benchmarks and evaluation),
seeded with the canonical works in each area and extended by search up to 2026-09-17. Every
arXiv identifier was checked by fetching the abstract page and matching the title; entries that
could not be checked that way are marked. The six lists were merged with deduplication on arXiv
identifier and normalised title, giving 221 entries.

## Acquisition
PDFs were downloaded from arXiv or, for work without a preprint, from the publisher or vendor
page recorded in the bibliography. Vendor pages for hands without any paper were fetched as HTML
and converted to markdown, so that a specification quoted in this survey is quoted from a stored
copy of the page and dated. Repositories were shallow-cloned and parsed, then deleted; what
remains is one markdown per repository holding the README, a pruned file tree, the task and
reward configuration files, and the bodies of reward and observation functions.

## Parsing
PDFs were converted with pymupdf4llm, falling back to raw text extraction when the layout parse
returned too little. The corpus manifest records, per entry, the source URL, page count, sha256
of the PDF and the converter used. Two consequences matter for reading this survey. Equations
rendered as images do not survive conversion, so where a reward weight exists only inside a
figure it is recorded as unreadable rather than guessed. Tables are flattened, so a number taken
from a table is quoted with the table it came from and, where the flattening is ambiguous, the
ambiguity is stated.

## Notes
Each entry was read into a structured note under a fixed template: embodiment, learning method,
objective, contact handling, evaluation, reproducibility, stated limitations, and quotable
claims. Notes were written only from the parsed files. Where the source is silent the note says
"not stated"; nothing was inferred from the reviewer's prior knowledge of the work. For method
papers the reward or loss was quoted from the paper and, separately, from the released code, so
that disagreements between the two are visible rather than smoothed over. Those disagreements
turned out to be common enough to become a finding in their own right.

## Sources that could not be obtained
Five works are behind publisher paywalls with no author-hosted copy found: Okamura et al. 2000,
Bicchi 2000 (IEEE T-RO), Piazza et al. 2019, Butterfass et al. 2001 (DLR-Hand II), and Hwangbo
et al. 2018 (RaiSim). They are cited by metadata and no claim in this survey rests on their
contents. The freely circulating PDF often taken for Bicchi 2000 is a different work, a book
chapter, and is listed separately.

## What this method cannot do
Mention counts over the corpus are counts of mentions, not of use: a related-work sentence
counts the same as an experiment. Vendor specifications are manufacturer claims and are labelled
as such throughout; where a page has since gone offline the note says so. The corpus is large
but not exhaustive, and selection by search favours work that is indexed, in English, and
posted as a preprint.
