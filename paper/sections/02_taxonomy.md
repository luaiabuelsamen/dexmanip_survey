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
