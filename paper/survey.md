# Dexterous Manipulation, Single-Hand and Bimanual

## Machines, simulators, and how policies are trained

A survey of 221 bibliography entries, 218 of which carry a structured row read from a note: 112 method papers, 33 hands, 15 simulators, 15 datasets, 14 benchmarks, 14 surveys, 8 tactile sensors and 7 evaluation protocols.
"Method row" throughout means one of the 112, and every headline count here has one of those eight
classes as its denominator.

*Compiled 2026-09-18. Every claim traces to a note in `papers/notes/`, every note to a parsed source in
`papers/md/` or `code/md/`, and every source to a hash or commit in `corpus/manifest.json`. The
method is in Appendix A.*

---


## Abstract

A hand is dexterous when it can change an object's pose without putting the object down. This
survey divides that problem the way its sections do: the hands, the simulators they are trained
in, how policies are trained, two hands on one object, and how it is evaluated. It rests on 218
sources read into a structured row, and on their released code. Papers disagree with their own
released code: most method rows whose code could be read against the paper record a discrepancy,
and nine are contradictions, where the code states a different objective from the paper. Nobody
measures interpenetration on a rollout: few of the rows that settle the question address it at
all, and not one reports it for its own trained policy's rollouts, though IsaacGymEnvs already
computes that depth and gates a policy update on it. Hardware has come apart from published work:
most tabulated hands appear in no method row, and several can be bought or built today. This
survey re-runs no method and ranks nothing: on penetration it supplies a measurement method and a
count, not a threshold, and every coverage statistic here is a floor over what this extraction
captured.

---

# 1. Introduction

![fig1_field](figures/fig1_field.svg)

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
with reinforcement learning and 35 run in Isaac Gym, against 7 on its successors Isaac Lab and
Isaac Sim.

Three things this survey measured are worth stating before the reader commits to 27,000 words.
Papers disagree with their own released code. Sixty-two of the 112 method rows released code that
could be read against the paper, 38 of those record a discrepancy, and nine are contradictions
where the shipped code states a different objective from the published one. The sharpest case is
`physhoi_2023`. Its `compute_humanoid_reward` hardcodes the object rotation and rotation-velocity
errors to zero, with the real computation commented out beside them, while the reward table in its
own paper lists weights of 0.1 and 0.01 for exactly those terms on GRAB. Its position-only success
criterion could not have caught that, and its headline 95.4 percent is cited as a baseline.
Section 5.6 classifies all 38, and seven further accusations an earlier draft made were withdrawn
under adversarial review and recorded beside the charge.

The quantity most specific to a hand is the one closed-loop policies do not record. Eleven of the
96 method rows whose notes settle the question address interpenetration at all, seven of the
eleven do it outside a closed-loop policy in a grasp synthesiser, a trajectory optimiser or a
contact model, and we found none that reports a penetration number for its own trained policy's
rollouts. The claim is about learned closed-loop control and not about the field. Grasp synthesis
and hand-object reconstruction have reported penetration depth and intersection volume as
comparative columns for years, and four rows of this corpus do it: `oakink_2022` scores a dataset
split on penetration depth, solid intersection volume and simulation displacement,
`bidexgrasp_2026` prints penetration depth beside a prior method's, `bimangrasp_2024` fails any
grasp whose total penetration exceeds 1.5 mm, and `toporetarget_2026` reports a maximum
penetration and a share of frames past 2 mm against a baseline retargeter. Every one of those
numbers scores a pose or a reference trajectory rather than the behaviour a trained policy
produced, and it is the rollout that is missing. The obstacle is not the engines. NVIDIA's own
IsaacGymEnvs repository already computes a per-environment maximum interpenetration depth in Warp
and gates the policy update on a 1 mm threshold. Section 4.2 has the file and the lines.

Hardware and published work have come apart. 19 of the 33 hand rows in Tables 2 and 3 appear in no
method row, and 8 of those can be bought today or built from published designs. Thirty-five method
rows run on the Allegro, whose weight, joint torque, payload and price have no reachable source,
because its product page returns HTTP 404 and everything Table 2 confirms about it comes from its
ROS driver.

None of those three findings is a first, and the audit behind the first of them is not a new idea.
`collberg_repeatability_2016` examined 601 papers in computer systems research for whether the
code behind them could be obtained and built at all. `biocon_2026` aligns 48 bioinformatics
projects with their publications at sentence-to-function granularity under expert annotation, and
`scicoqa_2026` collects 92 real paper-code discrepancies, mined from issue trackers and
reproducibility reports, into a benchmark for detecting such discrepancies automatically. In
reinforcement learning the phenomenon itself is a known result.
`engstrom_implementation_matters_2020` shows that code-level optimisations present only in the
implementation account for most of PPO's reported gain over TRPO, and `metaworld_plus_2025` finds
undocumented changes accumulated across one benchmark's own versions, which make comparisons
between those versions unfair. Both establish it on a single codebase.

The closest relative to the audit here is `knox_reward_misdesign_2023`, which reviews nineteen
reinforcement-learning publications on autonomous driving, characterises the reward functions of
ten of them exhaustively in a standard form, applies eight sanity checks and reports
near-universal flaws in reward design. Its ground truth for what each reward was is the authors,
obtained through correspondence with them rather than by reading a released repository, and what
it establishes is that published reward descriptions are incomplete: one of the ten described its
reward, discount factor, termination conditions and timestep thoroughly. Reading the code instead
needs no correspondence and supports a different charge, which is that where code exists it
sometimes contradicts the description. `raff_reproducibility_2019` took the opposite ground truth
on purpose, reimplementing 255 papers from their text alone and never opening the authors' code,
which is what makes the choice of arbiter a position rather than an accident.

So the claim here is narrow. We are aware of no prior work in robotics, and none in dexterous
manipulation, that reads a field's released reward implementations against the rewards its own
papers describe. Those seven works are cited from outside this corpus and enter none of its
counts. The exposure of the claim belongs beside the count above: the evidence is a repository at
a fetched commit, every hash recorded in the code manifest, and a repository at a commit is
evidence about that repository rather than about the run that produced a paper's numbers, because
the commit may postdate, precede or diverge from it. `hora_2022` states the problem in its own
README, which directs a reader to tag v0.0.1 and not to the commit parsed here to reproduce the
published numbers. Every accusation this survey has withdrawn, eight of them so far, is recorded
in the accused row for the same reason: the withdrawals are the evidence that the charges left
standing were checked rather than counted.

Fourteen corpus entries are themselves surveys or engine-comparison studies. Appendix D sets them
on one set of columns in Table 10 and says what each covers. Four of the fourteen could not be
obtained, or were fetched too late to read, and are entered as such. Two of the three things this
survey adds are visible in that table as columns none of the fourteen fills. One is Table 4, which
takes the engines `nine_physics_engines_review_2024` scored on documentation and usability and
adds contact model, solver, iteration count, default timestep and penetration exposure,
conditioned on what a hand does to a solver. `physics_engine_comparison_2015` and
`contact_models_comparison_2023` do measure engines, on five engines and on four contact
formulations, and neither surveys the field those engines are used in. The other is two hands on
one object as its own problem, which none of the four field surveys gives more than a subsection.

The third addition is the penetration measurement, on an axis a predecessor had already named.
`zhao_dexhand_survey_2026` states in its Sec. IV-C that the field assesses "at least two layers of
performance: the quality of grasps or poses prior to execution, and the performance of policies or
generators during downstream execution", and names "physical plausibility, including penetration"
as the most common criterion for the first layer. That is the reference-versus-rollout split,
named before this survey measured it, and the idea that contact quality belongs on the evaluation
axis is Zhao's. What Sec. IV-C does not give is a measurement method or a count, and this survey
supplies those two. It does not supply a threshold. The 2 mm figure the field uses is taken from
`toporetarget_2026` with no independent justification, the captured human grasps in `grab_2020`
sit above it at 3.25 mm, and Section 7.4 states plainly that 2 mm is a simulator convention rather
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

Figure 1 puts the field on one page. What follows works outward from the task: the six families
and what makes each hard, then the hands and their makers, then the simulators and the contact
models underneath them, then training, then two hands on one object as a problem of its own.
Section 7 is the longest, and it proposes an evaluation frame rather than a leaderboard. Each of
those sections closes on the gap it owns, with the evidence and the experiment that would settle it;
Section 8 is the list of those claims in one place, one sentence each, and Section 9 says what to do
about them, addressed
to someone publishing, running experiments or buying a hand. Appendix A is the method and says
where the tabulation this survey is built on lives; Appendices B and C are the full hand and
reward extractions; Appendix D sets this survey beside the fourteen that precede it.

# 2. A taxonomy of the problem

## 2.1 Task families

The six families below are read off the rows rather than imposed on them, and the last paragraph
here says what they miss. Grasping is the largest. Fifty-seven of the 112 method rows carry the
grasp label, the labels are not exclusive, and one paper can sit in several families. Success is a
lift that survives a hold, and the thresholds differ by more than an order of magnitude.
`dexgraspvla_2025` requires the object "held 10 cm above the table for 20 s", while
`omnigrasp_2024` requires it "held at least 0.5 s in simulation". What makes grasping hard at
scale is the continuum of starting configurations. `unidexgrasp_pp_2023` states it in Sec. 4.3,
that "we are dealing with an infinite number of tasks considering the initial object pose can
change continuously".

Functional and tool use is second with 45 rows. It is the family where a stable grasp can still be
the wrong answer. `dexterous_functional_grasping_2023` gives the case in Sec. 2.1, that "grabbing
a hammer from the head or handle are both equally valid ways of using it", and only one of the two
lets the tool be used. Success is defined against the tool's function, and the field has no shared
way to state it.

In-hand reorientation has 31 rows and the most settled criteria, because the community inherited
one number. `openai_dexterity_2018` declared the goal achieved below 0.4 rad of orientation error,
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

Bimanual coordination has 43 rows and handover has 10. Handover is the smallest family and the one
whose failure has a single moment, because the giver must release only after the receiver has the
object. `dynamic_handover_2023` reports a hit rate above its success rate and blames the gap in
Sec. 5.4 on "occasional challenges encountered during the grasping phase of the catcher". Not
every paper here learns both sides. In `dexterous_handover_2025` only the receiver is learned and
the giver is a scripted arm.

Those six families do not cover the corpus. Twenty-four of the 112 method rows carry a label from
outside them and eight carry no label from the six at all. Twenty fall in a catch-all class,
mostly generalist policies evaluated on a task suite rather than on a dexterous task family, among
them `pi0_2024`, `pi05_2025`, `pistar06_2025`, `openvla_2024` and `gemini_robotics_15_2025`. Three
adjacent families are named here rather than absorbed. Locomanipulation is `humanplus_2024`,
`omnih2o_2024` and `groot_n16_2025`, where the base is not fixed and the gravity argument below
changes character. Piano playing is `robopianist_2023`, `rp1m_2024` and `pianomime_2024`,
discussed in Section 6, where success is a per-timestep F1 against a MIDI score rather than an
object pose. Deformable manipulation is `dexdeform_2023`, whose object carries its own state and
its own physics. `ferrari_canny_1992` carries no task label because it is a grasp-quality measure
rather than a task. Table 1's six rows are the families with enough papers to compare, and not a
partition of the corpus.

## 2.2 Sources of difficulty

Contact is non-smooth, and that is a property of the problem rather than of any solver.
`bicchi_grasping_chapter_2001` states in Sec. 1.2 that contact constraints are unilateral, and
that losing a contact "involves an abrupt change of the structure of the model under
consideration". Its Sec. 1.4 gives the sharper version, that a rod sliding on rough ground has
configurations with no consistent solution and configurations with more than one. Simulators
inherit the difficulty. The re-implementation study `contact_models_comparison_2023` concludes in
Sec. V that "there is no fully satisfactory approach at the moment, as all existing solutions
compromise either accuracy, robustness, or efficiency". `pang_global_planning_2022` treats
non-smoothness as the thing to remove, curating every contact pair in Sec. III-D so that contact
points and normals change smoothly.

The hand has more actuators than the object has degrees of freedom and is still short of authority
over it. The object moves only through contacts, and the contacts are what cannot be commanded.
`bicchi_grasping_chapter_2001` Sec. 1.4 states that in multifingered grasps "the number of
independent contact forces is much larger than the number of actuators. Thus, from a
controllability standpoint, not all the contact forces are controllable".

Vision is occluded by the hand doing the work. `bai_unified_manip_survey_2025` names it in Sec.
4.3, that "occlusion hampers object tracking". `dexpoint_2022` keeps vision and adds imagined hand
points to the point cloud. `rotating_without_seeing_2023` removes vision entirely and rotates
objects from 16 binary touch sensors over the palm, links and fingertips.

Gravity direction changes the task rather than scaling it. `visual_dexterity_2022` states that
reorientation with the hand below the object "is much easier", because "with a downward-facing
hand, the hand must manipulate the object while simultaneously counteracting gravity".
`anyrotate_2024` makes the direction a randomised variable by "randomly initializing hand
orientations between episodes", and its Sec. 5.3 measures the cost, with performance dropping
progressively from palm up and palm down, through base up and base down, to thumb up and thumb
down.

**The second hand, and three counts.** Three counts describe two hands and they measure different things. Fifty-three of the 112 method
rows record two hands on the robot, which is all the corpus's two-hand flag claims. Forty-three
carry the task label for bimanual coordination, the narrower claim that coordinating the hands is
the task. Section 6 narrows again, to the 28 rows whose notes place a learned closed-loop
controller on two multi-fingered hands, and its opening paragraph names every exclusion that takes
the 53 down to the 28. That 28 is the denominator for every architecture count in this survey.
Every bimanual claim here names which of the three it uses.

**What the second hand adds.** Four things genuinely change when the second hand arrives. Contact stays non-smooth, occlusion
stays, and gravity stays the same problem.

Role asymmetry is one. `asymdex_2024` assigns a dominant hand with full finger and wrist control
and a facilitating hand with 6-DoF base pose only, so that "the facilitating hand repositions and
reorients one object, while the dominant hand performs complex manipulations".

Two hands on one object also close a kinematic chain through the object. In
`bicchi_grasping_chapter_2001` Sec. 1.4 the hand and object dynamics are separate and are "linked
through the n rigid-body contact constraints". A second hand adds a second constraint set on the
same object rather than a second independent problem. That is where physical plausibility fails
first. `bimangrasp_2024` is the corpus row that measures it, rejecting a synthesised grasp when
"total penetrations exceeded 1.5 mm" and reporting in Sec. IV-C that "penetration remains the
primary cause of grasp failure".

Two-arm collision does not exist for one hand at all. `dydexhandover_2025` resets an episode when
"any unintended arm contact with the environment or self-collisions" occurs.
`bunny_visionpro_2024` pays for it in the controller, where adding a sphere-approximated
self-collision cost raises motion-control time from 0.74 ms to 7.85 ms. `bidex_teleop_2024` solves
it in hardware, mounting the hands so the human arm and the teacher arm "are perpendicular to each
other and do not collide". `dexmimicgen_2024` states plainly that it does not handle inter-arm
collision at all.

And the action space doubles. `bidexhands_2022` runs 20 tasks on two Shadow Hands and finds
single-agent PPO beating multi-agent RL on most of them, offering in Sec. 5.2 that "PPO algorithm
is able to use all observations for training the policy, while MARL can only use partial
observations". `asymdex_2024` attacks the dimensionality from the other side, halving the
observation and action dimension through its role split and a frame relative to the facilitating
hand's object.

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
involved. A criterion naming a distance, a duration and a trial count can be re-run by someone
else. A rubric cannot, and Section 7 takes up what follows from that.

# 3. Hands and who makes them

## 3.1 Design axes

No degree-of-freedom, force, weight or price figure in Table 2 or Table 3 was measured by anyone
outside the maker. Six rows are the exception, from peer-reviewed papers with stated protocols:
ILDA, Pisa/IIT, ORCA, RUKA, LEAP and BiDexHand. Table 2 dates every other claim.

The degree-of-freedom count is the first number a vendor states and the least comparable one.
Shadow's specification of 4 December 2024 reads "20 actuated DOF and a further 4 under-actuated
movements for a total of 24 joints" `shadow_dexterous_hand_2005`. Table 2 prints joints first and
actuated DoF second, and the gap is the informative number. Where a vendor's own DoF figure
differs from the joint count, the joint count is what the table prints, as with Inspire's "Degrees
of freedom 6, Numbers of joints 12" `inspire_rh56dfx_2023`. An actuator count is neither of those
columns and has its own. DexHand states no joint count at all, only 16 finger micro-servos and two
wrist servos, so 18 servos is the only count quotable for it `dexhand_open_source_2023`. Daxo
states 120 actuators, no DoF figure, and a tendon structure with no rigid joints, which has far
fewer kinematic degrees of freedom than actuators `daxo_muscle_v0_2025`.

The actuation ratio is the real decision. The Pisa/IIT SoftHand drives 19 joints from one motor
and its authors state the cost plainly: "No in-hand dexterous manipulation is required for this
prototype" `pisa_iit_softhand_2014`. Tendon drive moves the motors off the fingers and the mass
follows them. Shadow's hand plus forearm weighs 4.3 kg, against 1.1 kg for the ILDA hand alone
with every motor in its palm `shadow_dexterous_hand_2005` `ilda_hand_2021`. ILDA states an 18 kg
payload against Shadow's 4 kg in a power grasp, and Shadow states no fingertip force at all. What
tendons cost is state estimation. The Faive Hand estimated joint angles from tendon length through
a Kalman filter and its cube reorientation failed on hardware, which its authors blamed on "poor
joint angle measurement from the EKFs, especially when there is contact" `faive_hand_2023`.
Ruka-v2 adds detachable AS5600 encoders to measure that problem rather than close the loop on it,
and those encoders put its open-loop linear joint-to-motor map at 8.26 degrees of error over seven
joints `ruka_v2_2026`.

Direct drive trades torque density for transparency. LEAP's Dynamixel joints resist 19.5 N in a
pull-out test against the Allegro Hand's 8.5 N, at 595 g for the LEAP hand `leap_hand_2023`, and
the Allegro's own weight has no reachable source. Linkage drive is the argument against the
forearm. ILDA puts 15 motors, drivers and ball screws inside the palm and reports 34 N at the
fingertip in the bent pose and 28 N stretched `ilda_hand_2021`. Linkages buy coupling for free, as
in BiDexHand's four-bar that drives each DIP off its PIP, whose paper claims 16 actuated DoF and
21 joints while its README describes 15 servos driving 15 joints `bidexhand_2025`.

Fingertip force is the number a hand buyer reads first, and across these rows it is six different
measurements. Table 2 puts the quantity beside the figure: pull-out resistance for LEAP's 19.5 N,
pinch for RUKA's 2.74 N and BrainCo's 15 N, fingertip normal force under a 1 cm indenter for
Unitree's 10 N, a calibrated five-trial fingertip force for BiDexHand's 2.14 N, a peak vendor
claim for 1X's 45 N, and two unlabelled spec columns for Sharpa's "20 N | 12 N". BrainCo's
whole-fist grip of 50 N is a separate figure and is no longer in the same column as a pinch.
ORCA's 19.6 N was none of these. It is the newton equivalent of a 2 kg index-finger payload at a
fixed 600 mA motor current, so its force cell is empty and its payload cell carries that protocol
`orca_hand_2025`. No two hands in Table 2 report payload under the same test either.

Compliance is repairability seen twice over, and both are mechanical fuses: the Pisa/IIT
SoftHand's rolling-contact joints return to assembly after over-extension and ORCA's "poppable"
pin joints dislocate rather than break `pisa_iit_softhand_2014` `orca_hand_2025`. ORCA also
reports tendon drive as maintenance: "Prolonged use requires manual re-tensioning to maintain
performance". What fails is rarely the motors. Its durability run found silicone skin degrading on
two fingertips after about 2,000 to 4,000 grasp cycles and sensor wires snapping on three after
about 4,500 to 7,000. The sensing wore out an order of magnitude sooner than the hand.

Two columns matter before any of the above and were missing. The first is the rate a loop can be
closed at, which spans 250 Hz on a Tesollo to 1 kHz on a Shadow, a Unitree or a Wuji, with the
Allegro at 333 Hz on its own CAN clock and Inspire stating no rate at all. LEAP's 500 Hz is a
serial query ceiling and its own sim-to-real policy runs at 20 Hz, which answer different
questions `leap_hand_2023`. A reader deploying torque control is bitten by that first. The second
column says whether a URDF or MJCF exists and who ships it, which is the bridge to section 4 and
to this survey's recommendation to pick a hand a simulator already carries. Shadow, Sharpa, Wuji,
the Ability Hand, RUKA, Faive and the Allegro driver ship one. LEAP is the warning: its paper says
the URDF is released and the released API repository contains none `leap_hand_2023`.

### Table 2. Hands that can be obtained

| hand | maker | joints | act. DoF | actuators | actuation | weight g | force N | what the force is | payload | control rate | URDF or MJCF | tactile | price USD | open HW | status | source | claim date | corpus methods using it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `shadow_dexterous_hand_2005` [1] | Shadow Robot Company | 24 | 20 | 20 | tendon-driven, motors in the forearm (20 Smart Motor <br>nodes, Maxon motors, PWM) | 4300 |   |   | 4 kg in a power grasp, vendor claim, protocol not <br>stated | EtherCAT at 1 kHz to the host, with a 5 kHz <br>tendon-force loop inside each motor module | MuJoCo models for Hand E and variants, plus Gazebo, <br>in sr_common | Shadow Tactile Fingertips (STF): 17x3 DoF <br>Hall-effect taxels, 1000 Hz, uncalibrated; up to 5 <br>fingertips; software also supports <br>BioTac/MST/UBI0/PST fingertip options |   | no | sold | datasheet | specification dated 2024-12-04 | 21: `asymdex_2024`, `bidexgrasp_2026`, <br>`bimangrasp_2024`, … |
| `sharpa_wave_2026` [2] | Sharpa Robotics (Sharpa Pte Ltd) | 22 | 22 | 22 |   | 1300 | 20 / 12 | vendor spec table with two unlabelled columns, <br>probably two configurations; grip force is listed <br>separately as 150 N / 90 N | 40 kg / 24 kg (the same two unlabelled columns) | 500 Hz over 1000BASE-T Ethernet | MuJoCo and Isaac Sim models | 'Dynamic Tactile Array' (DTA), camera-type array at <br>the fingertip: resolution 240x240 / 60x60, force <br>resolution 0.02 N / 0.05 N, spatial resolution 1 mm <br>/ 2 mm, frame rate 180 fps / 30 fps, force range <br>0-30 N, latency 20 ms, 6-D F/T; number of sensors <br>per hand not stated |   | no | sold | vendor page | undated page, copyright 2026, fetched 2026-09-17 | 6: `dexteleop0_2026`, `egoscale_2026`, `metis_2025`, <br>… |
| `proception_prohand_2026` [3] | Proception Inc (YC W25) | 22 |   |   | tendon-driven, motors pull cables to move the <br>fingers |   |   |   |   |   |   | integrated skin-like sensors detecting contact, <br>supporting grip control; same 'sensor skin' used on <br>the companion ProGlove; type/count not stated |   | no | sold | press | launch post and press, 2026-06-29 | 0 |
| `bidexhand_2025` [4] | Zhengyang Kris Weng, Center for Robotics and <br>Biosystems, Northwestern University | 21 | 16 | 15 | cable-driven, N-configuration tendon routing <br>(FeeTech servos, endless-loop antagonistic <br>pull-pull); thumb CMC flexion driven via a 4-bar <br>linkage instead of a direct tendon |   | 2.14 | fingertip normal force, calibrated sensor, five <br>trials per finger, average peak | 4.54 kg (10 lb) lifted | serial to an onboard ESP32, ROS 2 position control; <br>rate not stated | URDF, consumed by the ROS 2 and MoveIt stack; no <br>physics simulator | none mentioned |   | yes | open-source | paper | paper, 2025 (ICRA Dexterity workshop abstract) | 0 |
| `wuji_hand_2025` [5] | Wuji Technology (founded 2019) | 20 | 20 | 20 | direct-drive rotary, backdrivable |   |   |   |   | 1000 Hz across 20 axes over 100BASE-TX Ethernet, MIT <br>force-position hybrid mode | MuJoCo and Isaac Sim models | 'Multi-Axis Force/Torque Fingertip Sensing' <br>confirmed present; no type, count or range given |   | no | sold | vendor page | undated page, copyright 2026, fetched 2026-09-17 | 2: `toporetarget_2026`, `unidex_2026` |
| `ruka_v2_2026` [6] | Xinqi (Lucas) Liu, Ruoxi Hu, Alejandro Ojeda <br>Olarte, Zhuoran Chen, Kenny Ma, Charles <br>Cheng Ji, Lerrel Pinto, Raunaq Bhirangi, <br>Irmak Guzey, New York University and NYU <br>Shanghai | 20 | 16 | 16 | tendon-driven, forearm-mounted actuators; decoupled <br>parallel 2-DoF wrist via a passive spherical ball <br>joint; single-tendon-plus-spring abduction/adduction |   |   |   |   | Dynamixel over USB serial; no rate stated | MuJoCo XML in the shared v1 repo; not confirmed to <br>carry the v2 wrist | optional e-flesh fingertips (magnetic touch-sensing <br>form factor); not part of the base design | 1500 | yes | open-source | paper | paper, 2026 | 0 |
| `tesollo_dg5f_2024` | Tesollo Inc. (Incheon HQ, Gwangmyeong <br>R&D/factory) | 20 | 20 | 20 | one integrated actuator per joint ('high-torque <br>actuation', absolute encoder); page does not say <br>direct-drive | 1763 |   |   | pinching 2.5 kg rated and 5 kg maximum; enveloping <br>10 kg rated and 20 kg maximum | 250 Hz over Modbus RTU or TCP and Ethernet TCP/IP |   | none standard; optional fingertip sensors (6-axis <br>F/T, 3-axis force, or tactile) available; count/type <br>not given |   | no | sold | vendor page | undated page, copyright 2026, download links dated <br>2026-08 | 0 |
| `unitree_dex5_2025` | Unitree Robotics (Yushu Technology Co., <br>Ltd.) | 20 | 16 | 16 | in-joint geared motor ('hollow-cup motor' + <br>high-precision encoder + low-damping small-clearance <br>reducer), backdrivable; page does not use the words <br>tendon or linkage | 1100 | 10 | fingertip normal force under a 1 cm diameter <br>cylinder pressed vertically down (vendor footnote) | 3.5 kg palm down and 4.5 kg palm left, on a 5 cm <br>round hard object | 1000 Hz over USB 2.0, with per-joint stiffness and <br>damping commands |   | Dex5-1: none. Dex5-1P: 94 pressure sensors per hand <br>(2x5 palm + 2x3x5 finger pad + 2x3x5 fingertip + <br>2x3x4 finger root), range 10 g-2500 g. |   | no | sold | datasheet | undated page, copyright 2016-2025, fetched <br>2026-09-17 | 0 |
| `orca_hand_2025` [7] | Clemens C. Christoph, Maximilian Eberlein, <br>Filippos Katsimalis, Arturo Roberti, <br>Aristotelis Sympetheros, Michel R. Vogt, <br>Davide Liconti, Chenyu Yang, Barnabas Gavin <br>Cangan, Ronan J. Hinchet, Robert K. <br>Katzschmann, Soft Robotics Lab, ETH Zurich | 17 | 17 | 17 | tendon-driven (antagonistic fishing-line tendon <br>pairs per joint); wrist uses a GT2 timing belt drive | 1200 |   |   | 10.5 kg on all four fingers and 2 kg on the index <br>finger alone, both at a fixed 600 mA motor current | serial to Dynamixel or Feetech motors; rate not <br>stated | URDF-derived kinematic constants only; no URDF or <br>MJCF file in the released tree | yes: FSR-based binary tactile sensing on all 5 <br>fingertips (RP-C7.6-ST), absolute detection <br>threshold as low as 0.05 N |   | yes | open-source | paper | paper, 2025 | 0 |
| `leap_hand_2023` | Kenneth Shaw, Ananye Agarwal, Deepak Pathak, <br>Carnegie Mellon University | 16 | 16 | 16 | direct-drive (Dynamixel servos, e.g. XC330-M288), <br>joint velocity ~8 rad/s | 595 | 19.5 | pull-out resistance: the outward force a flexed <br>finger resists before slipping or deviating more <br>than 15 degrees (Table III) |   | up to 500 Hz querying over USB serial; the paper's <br>own sim-to-real policy runs at 20 Hz | URDF claimed in the paper; the released <br>LEAP_Hand_API repo contains no URDF, xacro or MJCF | none (future work only: 'we plan to develop and <br>integrate LEAP Hand with low-cost touch sensors') | 2000 | yes | open-source | paper | paper, 2023 | 12: `bidex_teleop_2024`, `bidexhd_2024`, <br>`cross_embodiment_world_models_2025`, … |
| `allegro_hand_v4_2016` [8] | Wonik Robotics Co. Ltd. (Seoul, South <br>Korea); earlier versions 1.0/2.0 made by <br>SimLab Co. Ltd. | 16 | 16 | 16 |   |   |   |   |   | 333 Hz, CAN, the hand's own real-time clock (driver <br>README) | URDF and xacro, left and right, in the ROS driver <br>repo | none |   | no | sold | driver repo | driver repo, versions 1.0-4.0 undated, fetched <br>2026-09-17 | 35: `anyrotate_2024`, `anyteleop_2023`, <br>`asymdex_2024`, … |
| `ruka_2025` | Anya Zorin, Irmak Guzey, Billy Yan, <br>Aadhithya Iyer, Lisa Kondrich, Nikhil X. <br>Bhattasali, Lerrel Pinto, New York <br>University | 15 | 11 | 11 | tendon-driven (11 Dynamixel actuators in the <br>forearm: XM430-W210T for the thumb, XL330-M288-T for <br>the other fingers) |   | 2.74 | pinch force, best of three trials, averaged over the <br>left and right hands (Table III) | 6.0 kg: weight added to a curled cloth-bag grip <br>until joint-angle error exceeds 15 degrees, best of <br>three trials | Dynamixel over a USB-to-serial bridge; rate not <br>stated, data collection ran at 15 Hz | MJCF | none (stated limitation: 'lacks tactile sensing') | 1300 | yes | open-source | paper | paper, 2025 | 0 |
| `robotera_xhand1_2024` [9] | ROBOTERA | 12 | 12 |   | gear-driven force-controlled joint modules per <br>finger segment, back-drivable | 1100 |   |   | 25 kg, tracker's 'Strength' figure, over 25 kg <br>gripping palm-up | not stated | URDF exists but is licensed; `maniptrans_2025` <br>withholds it | tactile/force sensors on every fingertip confirmed <br>present (senses contact, force, temperature); count <br>and array size not stated | 14000 | no | sold | third-party tracker | undated tracker page, fetched 2026-09-17; the vendor <br>page was not fetched | 8: `cross_embodiment_world_models_2025`, <br>`deximit_2026`, `dexmachina_2025`, … |
| `shadow_dex_ee_2024` | Shadow Robot Company, in collaboration with <br>Google DeepMind | 12 |   |   |   | 4100 |   |   |   | not stated; the page claims 'high bandwidth torque <br>and position control loops' |   | stereo camera-based fingertip tactile sensors <br>(hundreds of taxels each); multi-taxel 3-DoF arrays <br>on middle and proximal phalanges; counts not stated |   | no | sold | vendor page | undated page, copyright 2026, fetched 2026-09-17 | 1: `demostart_2024` |
| `inspire_rh56dfx_2023` [10] | Beijing Inspire Robots Technology Co., Ltd. | 12 | 6 |   |   | 540 | 10 | fingertip strength, vendor spec, four fingers; thumb <br>15 N; force resolution 0.50 N |   | RS485; rate not stated |   | none (this variant is the 'without tactile sensors' <br>table; a tactile FTP variant exists per bib but is <br>not on this page) |   | no | sold | vendor page | undated page, fetched 2026-09-17 | 19: `ace_teleop_2024`, <br>`articulated_tools_inhand_2025`, `being_h05_2026`, … |
| `brainco_revo2_2025` | BrainCo Inc. | 11 | 6 |   |   | 383 | 15 | pinch force, vendor minimum (>=15 N); the same page <br>states a whole-fist grip of >=50 N | >=20 kg | RS485 and CAN FD; EtherCAT on Pro and Touch; rate <br>not stated |   | Touch variant only: multi-dimensional fingertip <br>tactile module with 'Tactile Adaptive Control'; <br>count/type not stated. Basic and Pro variants: none. |   | no | sold | datasheet | undated page, fetched 2026-09-17 | 1: `bidexgrasp_2026` |
| `agibot_omnihand_2025` |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | unavailable | no source: both store.agibot.com URLs 404, fetched <br>2026-09-17 | 1: `clutterdexgrasp_2025` |
| `linkerbot_l20_2025` | LinkerBot (SDK author 'CHIUS INC') |   |   |   |   |   |   |   |   | USB-to-CAN at 1 Mbit/s, optional Modbus or RS485; <br>rate not stated | URDF, with PyBullet and Isaac Gym examples in the <br>SDK | L10/L20: per finger 4 channels (normal force, <br>tangential force, tangential direction, proximity), <br>5 sites x 4 channels, 0-255 range, sensor type not <br>stated. O6 (reseller): 16 capacitive tactile <br>regions. |   | no | sold | vendor page | undated page, fetched 2026-09-17 | 1: `being_h05_2026` |
| `psyonic_ability_hand_2021` [11] | PSYONIC (San Diego, CA, USA) |   | 6 | 6 | linkage (repo file/function names indicate a <br>four-bar finger linkage; not stated on the vendor <br>page itself) |   |   |   |   | BLE, I2C, UART or RS485; rate not stated | URDF (left, right, large, small, no-FSR) plus MuJoCo <br>and Isaac Sim paths in the vendor repo | 30 touch sensor values streamed (FSR-based per API <br>and URDF 'no_fsr' variant); per-finger split not <br>stated |   | no | sold | vendor page | undated page, fetched 2026-09-17 | 7: `ace_teleop_2024`, `asymdex_2024`, <br>`bunny_visionpro_2024`, … |
| `dexhand_open_source_2023` [12] | Rob Knight, The Robot Studio (design); <br>electronics/firmware/ROS 2 by Trent Shumay, <br>IoT Design Shop |   |   | 18 | tendon (fishing line, Sufix 832 80lb / 0.8mm <br>kiteline); Emax ES3301/ES3302/ES3351/ES3352 <br>micro-servos for fingers, Feetech SCS2332 or PWM <br>servos for the wrist |   |   |   |   | Arduino SCServo or SBUS firmware, BLE; rate not <br>stated | URDF, in the IoT Design Shop ROS 2 packages | none mentioned | 300 | yes | open-source | project page and GitHub <br>README | page posts 2023-08-08 to 2023-10-01; no hardware <br>release date | 0 |

*20 rows. 95 of 240 specification cells (39%) over the 12 specification columns are values no source stated; the key, maker, provenance and usage columns are excluded because they are never blank. Every figure here is the maker's or the authors' own claim. Nobody outside the maker has measured any DoF, force, weight or price cell in this table, except the rows sourced to a peer-reviewed paper with a stated protocol. The force column is not a ranking: read 'what the force is' first, because pull-out resistance, pinch force, a fingertip normal force under an indenter and an unlabelled vendor spec are different measurements. A blank cell means no source stated the value. No cell is truncated: a value wider than its column is wrapped at a word boundary, so a cell that runs to several rendered lines is one value and not several.*

Figures with no reachable source, and other caveats on individual rows:

1. `shadow_dexterous_hand_2005`: the four distal joints are coupled and not independently controllable, so the '24 DoF' quoted in learning papers is the joint count
2. `sharpa_wave_2026`: the page footnotes 'Specifications may vary between products', and no column of the spec table is labelled
3. `proception_prohand_2026`: the evidence is a shipping announcement, not a datasheet: no weight, force, actuated-DoF count or control rate is stated anywhere
4. `bidexhand_2025`: the paper states 16 independently actuated DoF and 21 joints; the README states 15 servos driving 15 joints
5. `wuji_hand_2025`: the page footnotes that these figures 'reflect the current Beta1 product and the SPEC will continue to iterate'
6. `ruka_v2_2026`: the AS5600 encoders are attachable and detachable and are read for calibration and measurement only, not in the control loop
7. `orca_hand_2025`: the 19.6 N previously tabulated as a fingertip force is the newton equivalent of the 2 kg index-finger payload at a control-imposed current limit, and no source states it as a force
8. `allegro_hand_v4_2016`: allegrohand.com/v4 returned HTTP 404 and the Wonik wiki timed out; every cell here comes from the ROS driver repository, and weight, joint torque, payload and price have no reachable source
9. `robotera_xhand1_2024`: the 15 N in circulation comes from a survey table, not from the tracker or the vendor; the tracker states no fingertip force
10. `inspire_rh56dfx_2023`: the vendor's own page reads 'Degrees of freedom 6, Numbers of joints 12'; the joints column here prints the joint count, so the vendor's DoF figure is the actuated-DoF column
11. `psyonic_ability_hand_2021`: the four-bar finger linkage rests on repository file names and the five fingers on URDF meshes; the vendor page states neither
12. `dexhand_open_source_2023`: no joint count is given anywhere, so no DoF figure can be quoted; the servo count is 16 finger and thumb micro-servos plus 2 wrist servos, with a third optional. The $300 is 'additional total cost of components', excluding printing and the wrist servos


## 3.2 Hands in use, and what they cost

![fig2_hands](figures/fig2_hands.svg)

The two oldest designs in Table 2 carry 49 of the 103 method rows that name a hand at all, and
seven rows use both. Neither design's date is confirmed by its own sources, so 2005 and 2016 are
the bibliography's. Figure 2 counts, per hand, the method papers whose own experiments use it. Of
112 method rows, 103 name a hand. The Allegro accounts for 35, Shadow for 21, the Inspire RH56
family for 19, a parallel-jaw gripper for 12 and LEAP for 12. Seventy-five of the 103 name an
Allegro, a Shadow or Adroit model, LEAP or an Inspire.

The Allegro's position is the uncomfortable part. Its product page at allegrohand.com/v4 returned
HTTP 404 while the Wonik wiki timed out `allegro_hand_v4_2016`. Everything Table 2 confirms about
the most-used hand in the corpus comes from its ROS driver: 16 joints, four fingers, a torque
interface, a 333 Hz CAN clock, 12 V, no tactile sensing. Its weight, joint torque, payload and
price have no reachable source. The field's most common platform cannot be specified from a page a
reader can open.

Concentration would matter less if the hand did not move the result, and it does. On the same
simulated cube rotation, LEAP reaches 0.2288 rad/s against the Allegro's 0.0828 rad/s
`leap_hand_2023`, and RUKA reports a 2.74 N pinch against the Allegro's 1.60 N under the same
three-trial pinch test `ruka_2025`. A method compared only on Allegro hardware is compared at one
point in a space where a single axis moves the headline number two or three times over. Inspire,
XHand and Sharpa take 29 of the 103 rows between them, four rows use two of the three, and none is
earlier than 2024. Eight take none at all: ORCA, RUKA, Ruka-v2, BiDexHand, DexHand, the Proception
ProHand, the Tesollo DG-5F and the Unitree Dex5.

**Open hardware and the collapse in cost.** Six rows in Table 2 are open hardware, and LEAP Hand V2 in Table 3 is a seventh. Five of the seven
state a dollar cost: $2,000 for LEAP, $3,000 for LEAP Hand V2, $1,500 for Ruka-v2, $1,300 for RUKA
and $300 for DexHand. ORCA states a material cost below 2,000 CHF that the price column leaves
unconverted, and BiDexHand states none `orca_hand_2025` `bidexhand_2025`. The Faive Hand states
neither a cost nor a licence that could be read, so it is not counted as open hardware here
`faive_hand_2023`. Two of the stated bases need saying. DexHand's $300 is "additional total cost
of components", excluding the printing and the wrist servos `dexhand_open_source_2023`, and ORCA's
own figure sits against Ruka-v2's table listing ORCA at about $3.5K `ruka_v2_2026`.

The expensive end of the collapse is secondhand throughout. The only six-figure numbers on disk
are RUKA's comparison table at $100,000 for a Shadow Hand and Faive's "steep price tag of 110k
GBP" `ruka_2025` `faive_hand_2023`. Shadow's own page says to discuss pricing and Table 2's price
cell for it is empty. The collapse is real at the cheap end and secondhand at the expensive one,
and it has barely moved the literature. Twelve of the 103 hand-naming method rows use an
open-hardware hand, and all twelve are LEAP.

What the cheap hands give up is sensing. LEAP has none and names touch sensors as future work
`leap_hand_2023`, RUKA states its design "lacks tactile sensing" `ruka_2025`, and BiDexHand's
sources never mention touch `bidexhand_2025`. ORCA is the exception, with binary FSR fingertips
whose threshold was measured as low as 0.05 N on a fresh fingertip, against the sensor's rated
0.29 N, and 6.38 N on a degraded one `orca_hand_2025`.

## 3.3 Tactile sensing

DIGIT set the cost floor. It is 20 by 27 by 18 mm, weighs about 20 g, streams 640x480 at 60 fps,
and its paper states a "total estimated manufacturing cost is approximately 15 USD per sensor ...
when manufactured in a batch of 1000" `digit_2020`. Durability was as much the contribution as
price: its gel degraded 0.3 percent over 15 abrasion passes, against 805 and 918 percent for the
two gels compared with it.

Digit 360 is the same lineage at a different operating point, claiming about 8.3 million taxels,
spatial features to 7 um, normal and shear force resolution of 1.01 mN and 1.27 mN, and on-device
processing that cuts event-to-action latency from 6 ms to 1.2 ms `digit360_2024`. It is also not
for sale, and no corpus paper's parsed text names it.

XELA's uSkin is the non-camera alternative and the one that bolts onto hands the field already
uses. Its curved fingertip kit for the Allegro V4 and LEAP carries 30 three-axis sensing points, a
full Allegro integration reaches 368, resolution is 0.1 gram-force, and the kit runs at 275 Hz
`xela_uskin_2020`. The 500 Hz figure often quoted belongs to the product family, not the curved
fingertip. One corpus paper names it, `sparsh_2024`, whose self-supervised encoders are
pre-trained on 462.7k tactile images and beat matched end-to-end models by 95.1 percent when both
see 33 to 50 percent of the labels. Its own bead-maze policies never complete the maze on the real
robot.

The usage number is the one to keep, and it needs its inclusion rule stated: a sensor physically
on the hand, read by the deployed policy. Eight of 112 method rows meet it: `anyrotate_2024`,
`articulated_tools_inhand_2025`, `dexteleop0_2026`, `dexumi_2025`, `hato_visuotactile_2024`,
`robot_synesthesia_2023`, `rotateit_2023` and `rotating_without_seeing_2023`. The rule excludes
`penspin_2024`, whose 20 binary contacts are simulated on an Allegro that has no tactile hardware
and whose released config sets `enable_tactile: False`, and it excludes `dexndm_2025` and
`dexplore_2025` for the same reason. Sixty-five of the 112 method papers mention tactile sensing
somewhere, which is the gap worth quoting. Thirty-five is the count over this survey's notes.

Almost none of the eight uses a high-resolution sensor. `rotating_without_seeing_2023` removes
vision entirely and rotates objects from 16 binary touch sensors over the palm, links and
fingertips, deployed zero-shot to a real Allegro, and Robot Synesthesia uses 16 force-sensing
resistors read as binary `robot_synesthesia_2023`. Two papers exclude touch deliberately, HORA
reporting rotation "even without the usage of vision and tactile sensing" `hora_2022`, and ORCA's
authors dropping it from their reinforcement learning "due to the additional complexity involved
in accurately modeling them" `orca_hand_2025`. Taxel counts have risen by three orders of
magnitude while the policies consuming them have stayed at binary contact.

## 3.4 The catalogue against the literature

**Three classes of evidence.** Behind Table 3's rows sit three kinds of evidence, and conflating them is how a DoF figure with no
source ends up in a survey. Vendor prose carrying numbers is the strongest, as on 1X's page of 9
July 2026 `onex_neo_hand_2026`. Video is second and carries none. Press or bibliography assertion
is third, as with Tesla's V3 hand, known here only through a paraphrase of patents because the
USPTO PDF parsed empty `tesla_optimus_hand_2025`. Table 3 blanks the cells resting on the third
class and footnotes who did the arithmetic.

A survey can go one step past recording that a claim is unverified, which is to say which claims
are implausible on their face. Daxo's 120 actuators in 750 g is about 6 g per actuator including
structure, tendons, routing and skin `daxo_muscle_v0_2025`. Clone's 27 degrees of freedom under 2
pounds excludes a 500 W pump the source does not confirm is excluded `clone_robotics_hand_2024`.
Figure 03's "Degrees of freedom, hands | 20" sits on the same tracker page as "Number of fingers |
10", so it is almost certainly the pair `figure_03_hand_2025`. Tesla's repeated 22 is one
article's arithmetic of four DoF on each of five fingers plus two at the wrist, and Gen 2's own
figure was 11 `tesla_optimus_hand_2025`.

Scepticism belongs to the evidence class, not to which table a row lands in. Sharpa's 22 of 22,
Wuji's 20 of 20 and Tesollo's 20 of 20 are vendor claims about unmeasured hardware and they sit in
Table 2, where Sharpa's page footnotes "Specifications may vary between products" and Wuji's says
the spec "will continue to iterate" on a Beta1 product `sharpa_wave_2026` `wuji_hand_2025`. Even
the best-specified vendor page in the corpus leaves its fingertip-force columns unlabelled.

### Table 3. Hands announced but not purchasable

| hand | maker | joints | act. DoF | actuators | actuation | weight g | force N | what the force is | payload | control rate | URDF or MJCF | tactile | price USD | open HW | status | source | claim date | corpus methods using it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `clone_robotics_hand_2024` [1] | Clone Robotics | 27 |   |   | hydraulic artificial muscle ('Myofiber' — small <br>water-filled tubes that contract when pressurized), <br>carbon-fiber bones and ligament-style tethers, <br>driven by a 500 W water pump and 36 <br>electro-hydraulic valves; each Myofiber generates up <br>to 1 kg grip force, survived 650,000 test cycles | <910 |   |   |   |   |   | pressure pads in the palm detect grip firmness <br>(count not given); 70 inertial sensors track <br>angle/speed (proprioception, not tactile) |   | no | internal-only | press | press, 2025-11-24, on a video of 2025-11-15 | 0 |
| `onex_neo_hand_2026` | 1X Technologies | 25 | 25 |   | quasi-direct-drive tendons via the '1X Tendon Drive' <br>at low gear ratios (~5:1-15:1); motors in the <br>forearm, tendons pulled through the wrist |   | 45 | distal flexion force, peak vendor claim |   | not stated |   | high-resolution tactile sensing across fingertips <br>and finger surfaces (normal force, contact location, <br>shear); sensor count/technology not stated |   | no | announced | vendor page | vendor page, 2026-07-09 | 0 |
| `sanctuary_phoenix_hand_2024` | Sanctuary AI (Sanctuary Cognitive Systems <br>Corporation) | 21 |   |   | hydraulic, 'unique miniaturized hydraulic valves' |   |   |   |   |   |   | not in the press release text; sidebar-only <br>headlines mention new touch/tactile sensors as a <br>separate later announcement, not confirmed as part <br>of this hand |   | no | internal-only | press | undated press release; trade reprint 2024-12-17 | 0 |
| `leap_hand_v2_adv_2025` [2] | Kenneth Shaw, Deepak Pathak, Carnegie Mellon <br>University | 21 | 17 | 17 | tendon (PIP/DIP coupled by a single tendon per <br>finger); motor type not stated |   |   |   |   | not stated | URDF, loaded into PyBullet by the released <br>teleoperation node | none mentioned | 3000 | yes | announced | vendor page | undated project page; API repo at commit a0936196, <br>fetched 2026-09-17 | 2: `bidex_teleop_2024`, `dexwild_2025` |
| `ilda_hand_2021` | Ajou University, Korea Institute of <br>Machinery & Materials, Korea University | 20 | 15 | 15 | linkage-driven, direct linear drive (3 Maxon DCX8M <br>motors per finger with GPX8 16:1 gearboxes driving <br>ball screws via parallel+serial four-bar linkages) | 1100 | 34 | fingertip normal force in the bent pose; 28 N <br>stretched, and 25 N per finger measured while <br>crushing an aluminium can | 18 kg | CAN to a desktop; loop rate not stated |   | 6-axis F/T sensor per fingertip (5 total), force <br>resolution 62 mN, range +/-35 N; not a distributed <br>taxel skin |   | no | prototype | paper | paper, accepted 2021-11-05 | 0 |
| `pisa_iit_softhand_2014` | Centro E. Piaggio, University of Pisa and <br>IIT (Catalano, Grioli, Farnioli, Serio, <br>Piazza, Bicchi) | 19 | 1 | 1 | tendon-driven adaptive synergy, single motor via <br>differential gears (6 W Maxon RE-max21, 84:1 <br>reduction) |   |   |   | holding force about 20 N along z and holding torque <br>2 N m, 28 N and 3.5 N m with a stronger motor | not stated | URDF and Gazebo models in the ROS repo (BSD <br>3-Clause) | none (motor encoder only; a padded work glove <br>supplied contact compliance during experiments) |   | no | prototype | paper | paper, IJRR 2014 | 0 |
| `faive_hand_2023` [3] | Yasunori Toshimitsu, Benedek Forrai, <br>Barnabas Gavin Cangan, Ulrich Steger, Manuel <br>Knecht, Stefan Weirich, Robert K. <br>Katzschmann, Soft Robotics Lab, ETH Zurich | 16 | 11 | 16 | tendon-driven, rolling-contact joints (16 Dynamixel <br>XC330-T288-T servos, 6 antagonistic pairs) | 1100 |   |   | 10 kg, whole-hand downward power grasp on a dumbbell | Dynamixel over serial; joint angles estimated from <br>tendon length by EKF; rate not stated | MJCF, used directly by the released Isaac Gym <br>training repo | none on the physical hand; a simulated 'fingertip <br>force' (15-dim, critic-only/privileged) exists only <br>in the RL training observation, not real tactile <br>hardware |   |   | prototype | paper | paper, 2023 | 1: `graspxl_2024` |
| `paxini_dexh13_2024` | PaXini Tech |   |   |   |   |   |   |   |   |   |   | 1,140 ITPU multidimensional tactile processing units <br>(press-release claim; unclear if PX-6AX-GEN3 sensor <br>family) |   |   | announced | press | press, CES 2026-01-07 | 0 |
| `tesla_optimus_hand_2025` [4] | Tesla |   |   |   | V3: tendon-driven from forearm actuators, three <br>tendons per finger through a crosstalk-managing <br>wrist. Gen 2: in-hand actuators/sensors (unlocated <br>in the article). |   |   |   |   |   |   | Gen 2: tactile sensing on all fingers, demonstrated <br>matching contact location and force in an egg-pickup <br>video; type/count not stated. V3: not stated. |   | no | prototype | press | Gen 2 video 2023-12-13; V3 patents filed 2024-10, <br>relayed by press 2026-04 | 0 |
| `boston_dynamics_atlas_hand_2026` | Boston Dynamics |   |   |   | electric (robot is fully electric); specific hand <br>mechanism not stated |   |   |   |   |   |   | tactile sensing in the fingers and palms, confirmed <br>present; type and count not stated |   | no | prototype | press | trade press, 2026-01-05 (CES); the Boston Dynamics <br>blog of the same date has no hand content | 0 |
| `figure_03_hand_2025` [5] | Figure AI |   |   |   |   |   |   |   |   |   |   | not stated on page for the hand itself; palm cameras <br>in each hand are vision, not tactile |   | no | prototype | third-party tracker | undated tracker page, fetched 2026-09-17; figure.ai <br>launch page returned HTTP 404 | 0 |
| `daxo_muscle_v0_2025` [6] | Daxo Robotics |   |   | 120 | ultra-redundant tendon-driven; compliant structure <br>with no rigid joints, flexible materials and tendon <br>routing | 750 |   |   |   |   |   |   |   |   | prototype | third-party tracker | third-party catalogue post, 2026-09-16; <br>daxo-robotics.com returned HTTP 404 | 0 |
| `xiaomi_cyberone_hand_2026` | Xiaomi |   |   |   | motors located in the hand (compact motors generate <br>heat requiring liquid cooling); no tendon/linkage <br>statement, though contrast with tendon-driven hands' <br>cycle life implies a non-tendon design |   |   |   |   |   |   | full-palm tactile sensing, area ~8,200 sq mm, <br>detects pressure and contact across the whole palm <br>not just fingertips; taxel count and type not stated |   | no | prototype | press | press, 2026-03-30 | 0 |

*13 rows. 96 of 156 specification cells (61%) over the 12 specification columns are values no source stated; the key, maker, provenance and usage columns are excluded because they are never blank. Every figure here is the maker's or the authors' own claim. Nobody outside the maker has measured any DoF, force, weight or price cell in this table, except the rows sourced to a peer-reviewed paper with a stated protocol. The force column is not a ranking: read 'what the force is' first, because pull-out resistance, pinch force, a fingertip normal force under an indenter and an unlabelled vendor spec are different measurements. A blank cell means no source stated the value. No cell is truncated: a value wider than its column is wrapped at a word boundary, so a cell that runs to several rendered lines is one value and not several.*

Figures with no reachable source, and other caveats on individual rows:

1. `clone_robotics_hand_2024`: 'under 2 pounds' is an upper bound, and the source does not say whether the 500 W pump and 36 valves are inside it
2. `leap_hand_v2_adv_2025`: the page claims 21 DoF with 17 powered motors and the README calls the same hand 17-DOF
3. `faive_hand_2023`: the row's open-hardware status is unconfirmed: the repo has LICENSE and LICENSE-NVIDIA files whose contents were not captured, and no open-hardware claim appears in the sources
4. `tesla_optimus_hand_2025`: the 22 DoF in circulation is a Teslarati article's arithmetic of four DoF on each of five fingers plus two at the wrist, not a Tesla statement; Gen 2's own figure is 11 DoF. This row's actuation cell describes V3 and its tactile cell describes Gen 2
5. `figure_03_hand_2025`: the tracker's 'Degrees of freedom, hands | 20' sits beside 'Number of fingers | 10', so the 20 is most likely the pair and about 10 per hand; the 16-per-hand figure in circulation has no reachable source
6. `daxo_muscle_v0_2025`: 120 actuators in 750 g is about 6 g per actuator including structure, tendons, routing and skin; no DoF number is stated, and a redundant tendon architecture with no rigid joints has fewer kinematic DoF than actuators


**What is sold against what is published on.** The bottom rows of Figure 2 carry the finding. None of the nine company-announced hands in Table 3
appears in a single method row whose own experiments use it. Tesla, Figure, 1X, Sanctuary, Boston
Dynamics, Xiaomi, Clone, Daxo and PaXini account for zero of the 112 method papers' experiments.
The nearest thing to a counterexample is `helix_2025`, a Figure blog post claiming a 35-DoF
whole-upper-body action space at 200 Hz that includes individual finger control. It never names
the hand, gives no per-hand DoF count, and reports no success rate or trial count for any task. It
is the maker describing its own unreleased hand, which is the evidence class the finding is about.
The four research prototypes in Table 3 are in a different position, since the Faive Hand and LEAP
Hand v2 Advanced account for three method rows between them `graspxl_2024` `bidex_teleop_2024`.

Table 3's emptiness is measurable and part of the same finding. Over the twelve specification
columns, 61 percent of its cells are values no source stated, against 39 percent for the hands
that can be bought. The hands with the highest advertised DoF counts have the least specification
behind them.

The one hand that crosses the gap crosses it because its maker published rather than announced.
ByteDexter reaches a method row through a ByteDance technical report stating 21 DoF per hand, 16
piezoresistive fingertip channels in the action vector and real-robot success rates
`gr_dexter_2025`, not through a product page. That mechanism is available to every vendor in Table
3 and none has used it.

The gap runs the other way too, and the last column of Table 2 shows it. Eight hands that can be
bought or built from published designs take zero method rows each: the Unitree Dex5 with 94
pressure sensors on its P variant `unitree_dex5_2025`, the fully actuated Tesollo DG-5F
`tesollo_dg5f_2024`, the 22-DoF Proception ProHand `proception_prohand_2026`, ORCA, RUKA, Ruka-v2,
BiDexHand and DexHand. Cheapness is established only for RUKA, Ruka-v2 and DexHand, because Table
2's price cell is empty for Unitree, Tesollo, the ProHand, ORCA and BiDexHand, and the only Dex5
price on disk is Ruka-v2's secondhand "~$25K" `ruka_v2_2026`. A reader choosing a hand on this
corpus's evidence has two well-precedented options, an Allegro or an Inspire, and a third in LEAP
if twelve papers is enough. Everything else is a press release or a hand nobody has published on.

**What would close the gap.** Nineteen of the 33 hands in Tables 2 and 3 appear in no method row, and
11 of those are neither sold nor open, so they appear in none for that reason and 33 is not the
denominator for a software-lag claim; the eight hands named just above are. What decides used from
unused is one regular expression per hand run against the method rows' own hand field, in
`tools/hand_usage.py`, so the partition is recomputed rather than argued about. The lag runs through
the tooling too: only three of the fifteen simulator rows name a real hand at all, and the ones they
name are the field's defaults, while `bench2dex_2026` compares 12 hands and `dexverse_2026` six
without stating a DoF count for any. What would close it is a conformance suite for hand models: one
URDF or MJCF per hand, fixed joint-limit, mass and collision checks, and a published pass or fail per
engine.

# 4. Simulators and the physics underneath

## 4.1 Requirements of a dexterous simulation

The clearest demonstration that hands are the hard case came from a benchmark that was not about
hands. Erez et al. built a 35-DOF arm modelled on the Shadow Hand, closed it around a capsule with
fixed spring-dampers, and asked four of the five engines for the largest timestep at which the
object was still in the hand. MuJoCo held the grasp at 16 ms, PhysX at 2 ms, ODE at 0.25 ms and
Bullet at 0.03 ms, a spread of a factor of 500 (`physics_engine_comparison_2015`, Sec. IV-D).
Havok is the fifth and was excluded for want of a working PD controller. Three caveats travel with
that spread. The engines run a deliberately restricted common model, hinge joints with sphere and
capsule geometry, no boxes and no meshes (Sec. II). The authors call it "an open question whether
this model system can be tuned to work better in the gaming engines" (Sec. IV-D). The timesteps
are log-spaced and good only to a factor of two, and the authors wrote MuJoCo and disclose it.

A grasp is hard for nameable reasons. It is many contacts at once, all persistent, all near
stiction, on an object much lighter than the mechanism holding it. Persistence and multiplicity
make the problem hyperstatic, and Le Lidec et al. show that per-contact solvers of the projected
Gauss-Seidel family, and RaiSim's, then inject spurious jamming forces at stiction that vanish
only once the object slides. The mass ratio makes it ill-conditioned, and in their stacked-cube
test at a 10^3 to 10^-3 kg ratio those same methods fail to converge. Global methods with proximal
regularisation stay robust in both cases (`contact_models_comparison_2023`, Sec. IV-A). What
degrades a truncated solve is therefore conditioning and redundancy, not stiffness, and a grasp
supplies both by construction. Locomotion is forgiving by comparison. On flat ground the contact
model and solver choice "hardly affects" their quadruped's tracked base velocity, and only on
rough, slippery terrain do RaiSim and CCP deviate. A walking robot makes and breaks a few contacts
against ground far heavier than itself. A hand does neither.

Speed enters by the same door. MuJoCo Playground reports that contact time scales with the number
of possible contacts rather than the active ones, because JAX requires static shapes, which is why
its tasks override the bound on contact points and the bound on geometry pairs by hand
(`mujoco_playground_2025`, Sec. VI). Every override printed in that paper is a locomotion port. A
hand's bound would have to be set the same way, for the worst case, but no hand configuration is
printed.

Figure 3 sets out the stages of one simulation step. Three of them make overlap, and they do not
answer to the same knob. In an engine that enforces non-penetration at the velocity level,
integration turns any residual approach velocity into overlap of order v times Δt; an engine that
enforces the gap at the next configuration carries no such term, which is why Dojo's hard-contact
NCP keeps its feet above the floor at every timestep it was tested at. Constraint assembly fixes
the compliance a loaded contact then rests at. A truncated solver leaves a residual that grows
with conditioning. Which of the three dominates in a grasp is not measured anywhere in this
corpus, and the three are not ordered here. A fourth item on the figure is not a source of overlap
at all. It is a mismatch between the geometry the solver uses and the geometry the renderer draws,
and it runs in both directions.

## 4.2 Contact models and solvers

![fig3_sim_step](figures/fig3_sim_step.svg)

Table 4 is the engine-by-engine comparison, one row per simulator, built only from what a note
confirmed. Le Lidec et al. supply the taxonomy that organises it, checking each formulation
against the Signorini condition, Coulomb's law, and the maximum dissipation principle. Linear
complementarity, the family of Bullet, ODE, PhysX and DART, satisfies Signorini alone, because
linearising the friction cone to a pyramid biases friction toward its corners. The cone
complementarity problem satisfies the other two but relaxes Signorini, so contact acts at a
distance of size Δt·µ·‖c_T‖. The full nonlinear problem satisfies all three and is non-convex
(`contact_models_comparison_2023`, Table II). A contact model is not the algorithm that solves it.
PhysX linearises the cone, which places its model in the LCP family, and it does not solve an LCP.
Its Temporal Gauss-Seidel scheme folds substepping into the Gauss-Seidel sweep and exposes
position and velocity iteration counts separately (`isaacgym_2021`, Sec. 3).

MuJoCo is inside that taxonomy rather than outside it. Le Lidec et al. classify it as CCP-MuJoCo,
a convex relaxation solved by a Newton method on the primal QCQP, in the same family as CCP-Drake,
the SAP-style scheme (Table III). The relaxation makes two errors of opposite sign in one engine.
A loaded contact carries a violation, and a sliding contact carries force at a positive gap.
Drake's SAP inherits the same pair, and its gliding effect at distance φ ≈ δt·µ·‖v_t‖
"unfortunately does not go away as δt → 0" (`castro_sap_contact_2021`, Sec. V-A). Le Lidec et al.
call that compliance a "numerical trick designed to circumvent the issues due to hyper-staticity
or ill-conditioning at the cost of impairing the simulation".

The depth a loaded contact carries is a chosen number. In a regularised formulation the
steady-state violation at a contact is the normal load times the compliance. It is zero at zero
load and it grows with the load carried. MuJoCo drives that violation coordinate with a critically
damped stabiliser parameterised by ε and κ, and for an object resting under gravity the
steady-state depth has a closed form independent of the object's mass
(`mujoco_convex_contact_2014`, Sec. V). The closed form did not survive the parse of that paper,
so the cancellation is quoted and the algebra is not. Neither MuJoCo paper states why mass
cancels, and the explanation this survey offers is its own inference rather than a cited one: the
regulariser is scaled by the inverse effective inertia at the contact, so compliance falls as 1/m
exactly as the gravity load rises as m. The nearest support in a parsed source is for a different
solver of the same engine, MuJoCo's diagonal solver, a "mass-aware spring-damper" that uses the
diagonal of the A matrix to keep contacts critically damped (`mujoco_2012`, Sec. II-E). This is
not a penalty spring, and depth is not always non-zero. The impulse solves a regularised convex
program over the whole contact set rather than a per-contact function of the gap, both MuJoCo
papers reject spring-dampers by name, and the 2012 ball-drop figure is captioned "there is no
penetration" (`mujoco_2012`, Fig. 2).

The first of two concrete measurements comes from the other end. Dojo solves a hard-contact
nonlinear complementarity problem with an exact second-order friction cone, by an interior-point
method converging within 15 iterations on the three robots of its convergence study. Its Table II
drops an Atlas humanoid and reports foot-floor penetration against the timestep. MuJoCo penetrates
−28 mm at Δt = 0.01 s and −46 mm at Δt = 0.001 s, while Dojo stays above the floor at every step
tested (`dojo_2022`, Sec. V-A). The MuJoCo column is not a trend. A ten-times-smaller step
produces more overlap, which no timestep-independent stabiliser does. Either that configuration
ties the compliance to Δt, or the quantity is an impact transient on a drop. Neither reading is a
steady-state grasp depth.

Drake's SAP quotes 2.5×10^-5 m at δt = 10^-2 s and 2.5×10^-7 m at δt = 10^-3 s, three and five
orders of magnitude below Dojo's two MuJoCo cells at the same steps, on an engine that is also
compliant (`castro_sap_contact_2021`, Sec. V-B). Those two figures are analytical bounds for a
single point mass at rest on a plane under that paper's near-rigid stiffness rule, not measured
depths, and they are not a Drake grasp-penetration number: a point-mass bound and a humanoid drop
transient differ in load, effective inertia and regime, so the distance between them is not a
measurement of anything. What the pair of engines does show is that in a compliant formulation the
depth follows from a stiffness that someone chose.

Dojo's Table V times 1000 steps of forward simulation with gradients, at a matched Δt = 0.01 s,
for engines that are not all computing gradients. MuJoCo is fastest on every system, 0.335 ± 0.001
s against Dojo's 1.159 ± 0.077 s on a Franka Panda, and the authors call the comparison difficult
because Dojo is stable at five times the step size (Sec. VI-B). What the regularisation buys, on
Le Lidec's reading quoted above, is conditioning on a hyperstatic problem, and the depth it costs
is tuned separately. Whether that is also what holds Erez's grasp at 16 ms is a question his data
do not answer. His planar chain is contact-free, so its numbers speak to the coordinate
formulation and not to contact: MuJoCo runs at 243.2 kHz there against Bullet's 22.8 and PhysX's
6.4, and Bullet's articulated Featherstone mode at 81.4 kHz beats every Cartesian-coordinate
engine (`physics_engine_comparison_2015`, Sec. IV-B). Those are throughput in evaluations per
second, not a largest-stable-timestep result, and the articulated Bullet mode was never run on the
grasp test at all, being usable only in tests without contact (Appendix). Joint coordinates
explain the contact-free speed advantage. The grasp timestep is a contact result, and the paper
attributes it to nothing: it reports that the other engines go unstable and "effectively simulate
a different physics model which can no longer hold the object" (Sec. IV-D), without an experiment
that separates the coordinate formulation from the soft absorption of penetration.

The GPU era moved the compliance knob rather than removing it. ComFree-Sim resolves contact in
closed form in the dual cone of the friction cone, so penetration becomes an explicit tuning
parameter and the paper reports it. On a drop test of convex primitives about 5 cm across at dt =
0.002 s, MuJoCo Warp penetrates 1.7 ± 4.9 mm and ComFree-Sim runs from 3.9 ± 6.9 mm at k_user =
0.1 down to 0.9 ± 1.5 mm at k_user = 0.5, though its prose describes the opposite direction from
its own table (`comfree_sim_2026`, Sec. IV-A). Its impedance acts on the signed gap through the
"identical" default hyperparameter API as MuJoCo's solver, so the knob it is credited with
exposing is one MuJoCo users already set. Those are 5 cm primitives under their own weight, not a
fingertip loaded by a grasp, and depth scales with the normal load. Nobody has published the
fingertip number. The baseline it measures against is MuJoCo Warp, which Newton builds on and
which MuJoCo Playground names as its intended replacement for JAX (`mujoco_playground_2025`, Sec.
VI).

That brings Table 4's most important column, and the claim it does not support. The column records
whether a parsed source reported a penetration depth, not what an engine can compute. Two of the
15 engines report one, Dojo and ComFree-Sim, and both are engines whose paper is about contact
accuracy. Four are recorded as not reporting it: Brax, Isaac Gym, Isaac Lab and Orbit. Nine rows
are blank. The word "penetration" appears nowhere in the Isaac Gym paper, and Isaac Lab's contact
sensor reports force, duration and an average contact point with no contact-quality metric. The
Isaac family carries 42 of the 112 method papers in this corpus.

**The tooling exists and the number is still not recorded.** NVIDIA's own IsaacGymEnvs repository
computes interpenetration depth in simulation. Its IndustReal tasks load plug and socket meshes
into Warp, sample points on one, query them against the other, and reduce to a per-environment
maximum interpenetration distance (`code/md/isaacgym_2021.md`, lines 8809 to 8862). The policy
update is gated on that number. Environments are split on whether their maximum stays under a
threshold, the reward of those that survive is scaled down as the maximum approaches it, and the
threshold itself is `interpen_thresh: 0.001`, commented as the largest allowed interpenetration
between plug and socket (lines 3630 and 3753). That is a shipped Isaac Gym task measuring
simulated interpenetration per environment at a millimetre threshold, during RL, and acting on it.
Table 4 records Isaac Gym as not exposing penetration, and so does its row in the corpus, which
the code parse in that same corpus contradicts. Tactile Genesis makes the point from the other
side, shipping penetration depth as a sensor on an analytic SDF backend and a BVH backend
(`tactile_genesis_2026`, App. A.1), while Table 4 leaves the Genesis cell blank. The depth is
computable from the poses and the meshes in a few lines of Warp, and the field's own benchmark
repository already does it. Interpenetration in a dexterous rollout is a setting nobody records
and a measurement nobody takes.

A policy will exploit what nobody looks at. DexTrack's configs carry PhysX's
`max_depenetration_velocity` at 10.0 or 1000.0 depending on the task variant, with no explanation
in the paper or in a config comment (`dextrack_2025`). The same parameter appears across unrelated
stock IsaacGymEnvs tasks at 5.0, 10.0, 100.0 and 1000.0, at five places in the same parsed file,
so DexTrack inherited a template rather than choosing per variant. The parameter caps the rate at
which the solver pushes overlapping bodies apart, so it sets how long an overlap persists and how
violently it is undone, not how deep the overlap gets. The one knob here that governs
interpenetration behaviour is being copied without being read. DexTrack's paper defines a maximum
hand-object penetration depth, applies it only to its input kinematic references, and presents
tolerance of "severe hand-object penetrations" as evidence of robustness (App. B).
`toporetarget_2026` is the one corpus method that reports the number carefully, and it reports it
on retargeted references rather than on a rollout, which section 7 takes up.

The rest of Table 4 is largely empty, and the emptiness is a result. Sixty-nine of its 165 cells
are values no parsed source stated, which is 69 of the 150 cells outside the engine-key column, or
46 percent, and the table's own footer counts the same 69. No engine paper states a default
physics timestep. Three report one for a named experiment, and the timestep column reports those
experiment settings. Isaac Gym's cell is its Shadow Hand step, from the only per-task timestep
table any engine paper here publishes, which runs 1/120 s for Shadow Hand and Allegro, 1/200 s for
ANYmal and TriFinger and 1/60 s for Franka (`isaacgym_2021`, Table 4). MuJoCo's 0.01 s is the
27-DoF humanoid test's step and ComFree-Sim's 0.002 s is its benchmark step, against a stated
stability limit near 0.02 s. Four engines state a solver iteration count and seven ship any
dexterous hand at all. The licence column answers a question a reader choosing an engine actually
has, and thirteen of fifteen rows do not answer it.

### Table 4. Simulators and physics engines

| engine | contact model | solver | iters | diff. | GPU | dt s | penetration exposed | throughput | hands shipped | licence |
|---|---|---|---|---|---|---|---|---|---|---|
| `brax_2021` | rigid bodies in maximal coordinates; <br>naive/quadratic-scaling pairwise collision detection <br>(no broad-phase acceleration structure); no <br>convex-decomposition or mesh-vs-primitive <br>distinction described | not LCP-based; velocity-level collision updates with <br>Baumgarte stabilization (inspired by the Tiny <br>Differentiable Simulator); joints modeled as spring <br>constraints rather than Featherstone-style <br>articulated-body methods |   | yes | yes |   | no | millions of simulation steps/sec on a single <br>accelerator (e.g. MuJoCo Ant equivalent on a <br>single chip); scales to hundreds of millions <br>of steps/sec distributed across a 4x2 TPUv3 <br>and other TPU topologies; Ant on a TPUv3 8x8 <br>estimated at ~hundreds of millions of <br>steps/sec vs ~thousands of steps/sec for <br>single-threaded CPU MuJoCo Gym (all figures <br>qualitative/order-of-magnitude, no exact <br>numeric table) | synthetic 4-fingered claw hand (Grasp <br>environment, non-commercial, <br>from-scratch morphology; not confirmed <br>present in current repo snapshot) |   |
| `comfree_sim_2026` | complementarity-free, analytical (closed-form) <br>contact resolution in the dual cone of the Coulomb <br>friction cone via a <br>prediction-correction/impedance-style update, <br>extended to a unified 6D model (normal, tangential, <br>torsional, rolling friction) | no complementarity solve; a 4-kernel GPU pipeline <br>(Algorithm 1: smooth-velocity prediction, <br>per-contact/per-face dual-cone solve, <br>generalized-impulse accumulation, velocity <br>correction) computes the impulse in closed form per <br>contact facet | none (closed-form, no <br>per-step iterative solve) |   | yes | 0.002 | yes | AMD 32-core CPU + NVIDIA RTX 4090 GPU: ~3x <br>faster (near-linear vs. MJWarp's <br>superlinear) step time vs. contact count at <br>512 parallel envs; ~2x parallel-environment <br>throughput vs. MJWarp at 256-4096 envs <br>(Allegro-hand cube-grasping benchmark); on <br>real LEAP-hand MPC (AMD 32-core CPU + RTX <br>4090), MPPI compute 13.9-28.2 ms vs. <br>MJWarp's 34.0-68.8 ms (~2.4x average <br>speedup) |   |   |
| `dojo_2022` | hard-contact nonlinear complementarity problem (NCP) <br>with an exact nonlinear (second-order-cone) friction <br>cone, avoiding pyramidal/linearized approximation, <br>to avoid interpenetration and creep artifacts | custom primal-dual interior-point solver (Algorithm <br>2), based on Mehrotra's predictor-corrector <br>algorithm, extended for non-Euclidean quaternion <br>variables, with cone-handling borrowed from CVXOPT; <br>gradients via implicit differentiation (implicit <br>function theorem) of the KKT/complementarity system, <br>with central-path parameter kappa trading gradient <br>smoothness for physical accuracy | converges within 15 <br>iterations for all three <br>robots tested in the <br>convergence study (Sec. <br>V-A); default tolerances <br>r_tol = kappa_tol = 1e-5 | yes | no |   | yes | Intel Core i9-10885H, 32GB RAM, CPU only (no <br>GPU support; described as future work). <br>Table V, 1000-step forward+gradient <br>wall-clock time at dt=0.01s: Humanoid - Dojo <br>1.750+/-0.135s vs MuJoCo 1.512+/-0.045s vs <br>Drake 5.463+/-0.078s vs Brax 6.975+/-0.485s; <br>Unitree A1 - Dojo 5.235+/-0.071s vs MuJoCo <br>1.114+/-0.007s vs Drake 3.870+/-0.024s vs <br>Brax 11.064+/-0.521s; Franka Panda - Dojo <br>1.159+/-0.077s vs MuJoCo 0.335+/-0.001s vs <br>Drake 2.352+/-0.055s vs Brax <br>10.954+/-0.395s; Skydio X2 - Dojo <br>0.807+/-0.003s vs MuJoCo 0.047+/-0.002s vs <br>Drake 0.571+/-0.011s vs Brax 7.953+/-0.484s. <br>MuJoCo is fastest on every system. |   |   |
| `genesis_2024` | Constraint-based rigid solver (equality/inequality <br>constraints, plus an explicit noslip() post-pass, <br>architecturally similar to MuJoCo's solver+noslip <br>design) combined with multi-material coupling: FEM, <br>MPM, particle-based PBD and SPH, a libuipc <br>Incremental Potential Contact solver, an explicit <br>inter-solver coupler, and a SAP <br>(semi-analytic-primal-style) compliant-contact path <br>used for grasp-coupling scenes. | ConstraintSolver with Newton-style line-search <br>iterative resolve (linesearch.py) and <br>constraint-island decomposition for parallelism <br>(island.py); multiple pluggable physics solvers <br>(Rigid, FEM, MPM, PBD, SPH, libuipc, SAP) compiled <br>via the Quadrants (Taichi-derived) backend. |   | yes | yes |   |   |   | Shadow Hand |   |
| `isaacgym_2021` | Rigid-body contacts via PhysX; contact geometry can <br>be primitive shapes or meshes loaded from URDF/MJCF <br>(Sec. 2.2); net contact forces exposed <br>per-rigid-body via the Tensor API (Table 1, <br>Get-only). No explicit statement of convex-vs-mesh <br>contact generation or per-pair contact-point count. <br>Shadow Hand tendons simulated via PhysX Fixed Tendon <br>mechanics: spring+damping force proportional to <br>deviation from rest length, propagated through a <br>tendon-joint tree (Sec. 3, Appendix A.1). | Temporal Gauss-Seidel (TGS) solver (Sec. 3, ref. <br>18), not classic PGS/LCP: folds sub-stepping into a <br>per-body accumulated velocity-delta buffer projected <br>onto the constraint Jacobians. Table 3 exposes two <br>user-tunable iteration knobs, Position iterations <br>(biased, velocity+positional-error-correcting) and <br>Velocity iterations (unbiased, <br>velocity-error-only-correcting); no default numeric <br>values for these are given in the main text. |   | no | yes | 0.008333333333333333 | no | Shadow Hand: 150,000 parallel environment <br>steps/sec at 16,384 environments, single <br>NVIDIA A100 GPU (Sec. 5.3); Shadow Hand <br>OpenAI reproduction (feed-forward): >20 <br>consecutive successes in <1 hour on 1x A100 <br>vs. 30 hours on OpenAI's cluster of <br>384x16-core CPUs (6144 cores total) + 8x <br>NVIDIA V100 GPUs (Sec. 6.4.1). | Shadow Dexterous Hand, Allegro Hand, <br>TriFinger (3-finger, 9-DoF manipulator; <br>the paper itself says this is not a <br>hand) |   |
| `isaaclab_2025` | Rigid contacts by default via PhysX 5 (SDF <br>collisions, Featherstone articulation solver, Sec. <br>2.2); `Factory` assembly envs specifically use <br>'SDF-based contact generation, a contact reduction <br>technique, and a Gauss-Seidel solver' (Sec. 6.4). <br>ContactSensor exposes net normal force per body, <br>optional filtered pairs, contact duration, average <br>contact point, and a short history (Sec. 3.3.1); no <br>contact-quality/penetration metric is defined <br>(survey note). | NVIDIA PhysX 5's internal <br>rigid-body/Featherstone-articulation solver, used <br>as-is; Factory assembly envs specifically named as <br>using a Gauss-Seidel solver with SDF-based contact <br>generation and contact reduction (Sec. 6.4). No <br>timestep, decimation, or solver-iteration values are <br>stated anywhere in the paper for the general <br>(dexterous) suite; the only note is qualitative, <br>that the Digit humanoid 'requires a higher solver <br>iteration count for stable simulation' (Fig. 14). |   | no | yes |   | no | DextrAH teacher task (state-based <br>grasp-and-lift): over 900,000 FPS training <br>throughput with 8 GPUs (RTX Pro 6000, the <br>paper's only multi-GPU platform) and 16,384 <br>environments (Sec. 4.1.1); Franka cabinet <br>drawer task: over 1.6 million FPS at the <br>same 8-GPU/16,384-environment setting. <br>Single-GPU dexterous-suite numbers are not <br>stated. | KUKA Allegro hand (first-party dexterous <br>suite, Sec. 7.2.3), ShadowHand <br>(third-party GraspQP grasp evaluation <br>only, Sec. 6.4), AbilityHand <br>(third-party GraspQP grasp evaluation <br>only, Sec. 6.4), Fourier GR1-T2 dex <br>hands, Unitree Inspire hand, Unitree <br>trihand (XR teleop retargeters in code <br>only) |   |
| `maniskill3_2024` | PhysX (via SAPIEN) rigid-body contacts on GPU; no <br>statement of convex-vs-mesh contact generation or <br>contact-point count in the note. <br>AllegroHandRightTouch reads FSR contact impulse <br>(`get_fsr_impulse`) for touch sensing (App. VII-H, <br>code). | PhysX (via SAPIEN), used as-is; no <br>LCP/PGS/TGS/Newton solver-algorithm name given. <br>Benchmark (cartpole) settings state 'Solver Position <br>Iterations: 4 / Solver Velocity Iterations: 0' (App. <br>XI-A), but per-task `_default_sim_config` values are <br>not exported in the parsed source. | 4 position / 0 velocity <br>iterations (benchmarked <br>cartpole configuration only, <br>App. XI-A); per-task <br>defaults not exported in the <br>parsed source |   | yes |   |   | Up to 30,000+ FPS (RGBD+segmentation) on a <br>single RTX 4090 GPU, environment count for <br>that headline figure not stated; at 128 <br>parallel environments with cameras, <br>ManiSkill3 uses 3.5GB GPU memory vs. Isaac <br>Lab's 14.1GB (Sec. III-B); PPO uses up to <br>4096 parallel environments for state-based <br>training and 256-1024 for RGB training (App. <br>IX-A), all on RTX 4090 (App. XI-A benchmark <br>hardware). | Allegro Hand (incl. touch-sensor <br>variant, AllegroHandRightTouch), Ability <br>Hand, Inspire Hand, Delto 3-finger hand, <br>TriFinger | Apache-2.0 |
| `mujoco_2012` | soft, convex velocity-stepping contact; three <br>interchangeable solvers replace the standard <br>LCP-with-friction-pyramid approach: <br>implicit-complementarity, convex (kinetic-energy <br>minimization with a soft non-penetration cost), and <br>diagonal (mass-aware spring-damper) | implicit-complementarity solver (customized <br>non-smooth Newton method, most accurate); convex <br>solver (interior-point method used for reported <br>timings; projected Newton/CG/Gauss-Seidel also <br>mentioned as unverified-faster alternatives); <br>diagonal solver (per-contact critically-damped <br>spring-damper using the diagonal of the A matrix, <br>fastest/least accurate) |   | no | no |   |   | up to ~400,000 dynamics evaluations/sec on a <br>12-physical-core machine (2x 6-core Intel <br>X5860 3.33GHz, 24 threads via <br>hyper-threading), 3D humanoid with 18 DOF <br>and 6 active contacts (Abstract, Table 3) |   |   |
| `mujoco_convex_contact_2014` | soft, convex, complementarity-free; a unified <br>impulse vector covers joint dry friction, <br>joint/tendon/distance limits, and frictional <br>contacts together, with an elliptical friction cone <br>whose dimensionality per contact is 2 (sliding), 3, <br>or 5 (sliding+torsional+rolling) | GPGS (generalized projected Gauss-Seidel, described <br>as the authors' own unpublished-at-the-time method <br>handling cone and pyramid constraints) for the <br>contact/limit impulse; a separate 'soft Gauss <br>principle' derivation for equality/holonomic <br>constraints; an analytically-invertible closed-form <br>solver for a restricted circular-cone special case | 5 and 50 (both tested, Fig. <br>3, Sec. VI-B) | no | no | 0.01 |   | single-core Intel i7-3930K (Windows 7): <br>forward dynamics of a 27-dof humanoid with <br>10 contacts evaluated in 0.1 ms (100x <br>real-time at a 10 ms timestep); inverse <br>dynamics of the same humanoid under 100 <br>impulses in 30 microseconds (10 microseconds <br>with no impulses); no <br>parallel/multi-environment throughput <br>reported |   |   |
| `mujoco_warp_2025` | MuJoCo's native solref/solimp-parameterized <br>soft-constraint contact model ported to Warp — <br>per-contact Jacobian construction (dense and sparse <br>variants, with flex variants) and <br>equality/limit/friction constraint rows; not a <br>re-derived contact model | MuJoCo's default (implicit CCP-style) solver and <br>Newton constraint solver (via a 'newton' flag <br>threaded through equality/limit/friction kernels) <br>are supported; legacy PGS solver and noslip <br>post-processing pass are 'not yet supported' per the <br>README |   | no | yes |   |   |   |   |   |
| `newton_2025` | Solver-dependent: MuJoCo-style soft-constraint <br>(solref/solimp-style) contact via <br>SolverMuJoCo/MJWarp; Proximal-ADMM / <br>Dual-Variational-Inequality contact resolution via <br>SolverKamino; position-based-dynamics-style <br>constraint projection for the XPBD and VBD solvers. | Multi-solver architecture: SolverMuJoCo (wraps <br>MJWarp), SolverKamino (Proximal-ADMM + DVI), XPBD <br>(rigid), VBD (cloth/deformables), Style3D (cloth), <br>plus a separate IKSolver (LM and L-BFGS backends). |   |   | yes |   |   |   | Allegro Hand |   |
| `orbit_2023` | PhysX SDK 5 signed-distance-field (SDF) collision <br>checking for rigid bodies (handles non-convex <br>geometry such as screw threads); FEM-based solver <br>using a constraint-based stable neo-hookean material <br>formulation for deformable bodies; PBD <br>(position-based dynamics) solver for cloth | PhysX SDK 5's internal rigid-body and FEM solvers, <br>used as-is; no LCP/PGS/TGS, Newton, or CG iteration <br>counts given |   | no | yes |   | no | 125,000 FPS physics-only ceiling (no env <br>count stated); ~10x rigid-body throughput <br>vs. CPU-vectorized frameworks (robosuite, <br>ManiSkill2, IsaacGymEnvs) swept 256-4096 <br>envs; ~3x deformable/cloth throughput vs. <br>DEDO; 270 FPS aggregate for 10 cameras at <br>640x480; hardware: 16-core AMD Ryzen 5950X, <br>64GB RAM, NVIDIA RTX 3090 (Sec. V-E-b, VII) | Allegro hand |   |
| `pybullet_2016` |   |   |   |   | yes |   |   |   |   |   |
| `raisim_2018` |   |   |   |   |   |   |   |   |   | requires a valid license <br>and activation key from <br>the RaiSim Tech website; <br>the repo README also <br>states RaiSim itself is <br>no longer supported in <br>favor of a RaiSim2 repo |
| `sapien_2020` | Rigid-body contact with convex-decomposed collision <br>meshes (PhysX 4.1); three joint systems offered <br>(kinematic, dynamic, and PhysX articulation) trading <br>control accuracy against speed. | PhysX 4.1's internal rigid-body solver, used as-is; <br>no LCP/PGS/TGS name or iteration count given in the <br>paper. |   |   | no |   |   | ~5000 Hz engine, ~700 Hz OpenGL render; <br>single-instance CPU-physics figure with no <br>parallel environments, on a laptop with a <br>2.2 GHz Intel i7-8750 CPU and an Nvidia <br>GeForce RTX 2070 GPU. |   |   |

*15 rows; 69 of 165 cells (41%) are values no source stated.*
*No cell is truncated. A value wider than its column is wrapped at a word boundary, so a cell that runs to several rendered lines is one value and not several.*

## 4.3 GPU-parallel engines and their throughput

**The GPU-parallel turn.** Isaac Gym set the pattern. Physics, observations, rewards and actions stay on the GPU, and PhysX
resolves contacts with the Temporal Gauss-Seidel sweep described above. Its per-task timesteps are
published, which is rare: the Shadow Hand runs a 1/120 s physics step under a 1/60 s control step,
or 1/20 s in the OpenAI variant. The result that reorganised the field is that reproducing
OpenAI's Shadow Hand cube reorientation took under an hour on one A100, against 30 hours on 6144
CPU cores and 8 V100s (`isaacgym_2021`, Sec. 6.4.1). Thirty-five of the 112 method papers in this
corpus run on it.

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
solver-dependent, not a property of the engine, which is how Table 4 records it. Isaac Lab's code
already exposes a `--physics newton_mjwarp` backend switch in its hands demo, and its roadmap
announces Newton integration. An experiment reported as Isaac Lab may be running PhysX 5 with TGS,
or MuJoCo's soft constraint rows under Warp, and those two make different contact errors. The name
also fails to fix the physics inside one engine. MuJoCo's convex solver is a family, interior
point or projected Newton, conjugate gradient or Gauss-Seidel (`mujoco_2012`, Sec. II-D), and
MuJoCo Warp supports neither PGS nor the noslip pass. PhysX 4 and PhysX 5 differ in whether
non-convex rigid bodies get SDF collision, which is a contact-geometry difference between Isaac
Gym and Isaac Lab under one vendor name (`orbit_2023`, `isaaclab_2025`). Naming a simulator no
longer names its physics. Papers should report the backend and the solver beside the framework.

**Reported throughput, and why the numbers do not compare.** Four headline figures measure four different quantities. Isaac Gym reports parallel environment
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
487,341 ± 4,346. Same hardware, same measurement, same codebase, a factor of 6.4 between two
environments. It is not a factor from the task in isolation. Playground tunes solver iterations,
line-search iterations, timestep and contact bounds per environment, with values as far apart as
one and four solver iterations (`mujoco_playground_2025`, Table III), and it does not print the
two configurations side by side. That omission is what makes the two figures incomparable. The
same confound sits inside Isaac Gym's paper on one A100: 700,000 environment steps per second for
Ant, 200,000 for Humanoid, 150,000 for the Shadow Hand. A training-loop FPS is also mostly not a
measurement of physics. Playground breaks the fractional cost down on an RTX 4090: for
CartpoleBalance, physics is 0.02, rendering 0.06, inference 0.01 and the policy update 0.91, and
the policy update still dominates on the Franka task.

Cross-framework comparisons add further free parameters. ManiSkill2's PickCube table takes the
best result over 16 to 512 environments for each system (`maniskill2_2023`, Table 1a), giving
ManiSkill2 with a render server 2487 ± 24 FPS at its optimum of 64 environments against Isaac
Gym's 865 ± 35 at its optimum of 512. The env-count tuning is the second problem here. The first
is that the two systems are not the same kind of thing: ManiSkill2 runs rigid-body physics on CPU
worker processes behind a shared GPU render server, Isaac Gym runs physics on the GPU, and its own
paper says so plainly. The measured quantity includes 128×128 rendering at 500 Hz simulation and
20 Hz control for both, so this is a visual sample-collection loop rather than two physics
engines. Its authors add the fidelity caveat themselves, and Playground is equally explicit that
its cross-simulator plot borrows its Isaac Lab and ManiSkill3 numbers from the ManiSkill3 paper.
Several sources give no number at all: MuJoCo Warp's README points to an external nightly
dashboard, and Newton's and Genesis's READMEs contain no FPS or speedup anywhere.

The failure reaches past the engine papers into the methods. Of the 47 corpus method papers that
name a GPU-batched simulator, 19 state no environment count anywhere, and Isaac Lab's own paper
states no physics timestep, no decimation and no solver iteration count for any task. A throughput
figure is interpretable only with the environment count, the GPU, the timesteps, the solver
iteration budget, and a statement of whether rendering and the learning update sit inside the
measurement. Almost nobody reports all five.

## 4.4 Tactile simulation and the sim-to-real gap

The three tactile simulators in this corpus calibrate against three different things, and none of
them is a manipulation outcome. TACTO is a rendering layer over a host engine, by default
PyBullet's rigid contact model. It reads post-solve link poses and the engine's reported normal
force and maps that force to gel-mesh deformation at the rendering level, so it contributes no
contact physics of its own. Its only sim-to-real number is a tactile pose-estimation task, at 1.66
± 0.16 mm with colour-jitter augmentation against 0.76 ± 0.07 mm for a model trained on 128 real
datapoints (`tacto_2020`, Table II).

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
a fidelity measurement. The real XHand1 SDK reports a per-taxel raw pressure field as well as an
aggregate contact pressure, but documents no taxel positions or response characteristics, so the
raw field cannot be registered to the simulated probe layout and only the aggregate is comparable
(App. C). The undocumented calibration is the barrier, not a missing signal.

**The sim-to-real gap for hands.** Most of what is written about this gap is attribution without measurement. PenSpin asserts that
the pure physics gap "cannot be bridged by extensive domain randomization alone" while reporting
no experiment that isolates it (`penspin_2024`). MuJoCo Playground attributes its LEAP hand
failures to physical flex in low-cost hardware and names more accurate collision geometries as the
fix, without measuring either. DeXtreme lists four candidate causes for its shortfall, including a
malfunctioning Allegro thumb used in most trials, and disambiguates none by experiment
(`dextreme_2022`).

What has been measured is narrower, and section 7 collects the transfer numbers. The one result
that links a quantified model error to transfer is a humanoid recipe paper, which ranks its system
identification runs by dynamics-model MSE and pairs each with real success over 10 trials: the
lowest-MSE model grasps 8 out of 10, the median-MSE model 3 out of 10, the highest-MSE model 0 out
of 10 (`humanoid_sim2real_recipe_2025`, Table 1). Where a cause has been pinned down elsewhere it
is usually perception or actuation, not contact. OpenAI's pose estimator has 3.12 mm error on
rendered images and 9.27 ± 4.02 mm on 992 real ones, and PDDM reports a camera tracker with 5 mm
average error and 20 ms latency as the unmodelled source in its real numbers (`pddm_2019`, App.
C).

The contact side stays unmeasured, and the one paper that looks at it is usually read backwards.
DeXtreme's real-to-sim replay interpenetrated because the replayed poses carried the pose
estimator's error, not because the contact model failed. The paper says so: "there is still some
sim-to-real gap in pose estimation. This is manifested when we played back the real states in sim
(real-to-sim) with physics enabled, which sometimes resulted in interpenetrations. Therefore, we
were not able to easily calibrate physics parameters of the cube" (`dextreme_2022`, Sec. 5). A
replayed trajectory is a placement, so the overlap it shows bounds the state estimate rather than
the physics. That is why it could not calibrate the cube, and it is why calibrating contact
against hardware still has no worked example for a hand. The only direct measurement of simulator
fidelity against hardware in this corpus is Dojo's, an average final-position gap of about 0.5 cm
over 5 box-pushing trials. It is a parallel-jaw arm pushing a box, and there is no equivalent
number for a hand.

# 5. Training a dexterous policy

## 5.1 Sources of supervision

A dexterous policy is defined by what supervises it, and four sources are in use across the
corpus's 112 method rows: a reward function supervises reinforcement learning, a human
demonstration supervises imitation, a human reference trajectory supervises a physics-based
tracker, which is imitation with a simulator in the loop, and nothing supervises a model-based
planner, which is handed a cost and a model instead.

The labels do not partition the corpus. Of the 112 method rows, 53 are tagged reinforcement
learning, 27 behaviour cloning, 23 distillation, 18 generalist or vision-language-action, 14
teleoperation systems, 14 diffusion, 10 data collection, 8 flow matching, 6 reinforcement learning
from demonstrations, 6 trajectory optimisation, 5 model-predictive control, 4 grasp synthesis and
2 world models. The tags sum to far more than 112 because most methods published since 2024 sit on
two branches at once. Figure 4 draws the tree and the cross-links. Table 7 is the row-by-row
version of the same thing, and is the table to scan when looking for work comparable to your own.

What the deployed policy looks like once training is done matters more than the name a paper gives
itself, and on that axis the field has converged hard. Section 5.5 shows why.

**What the tabulation does not record.** Table 7's emptiest columns are the ones a reader most needs:
only 31 rows state an environment count, only 70 state how many real trials are behind the headline
number, and only 39 state how many unseen objects were tested. The trial and unseen-object figures
are the audited ones, after section 7.1 recovered 15 trial counts and 7 unseen-object counts that the
notes carried and the extraction had dropped. A mostly empty row is not a weak method, but it is one
that cannot be compared with any other row here.

### Table 7. Methods

| method | yr | task | paradigm | algorithm | hand | DoF | bi | sim | real | trials | unseen obj | penetration | code |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `ferrari_canny_1992` | 1992 |   |   |   |   |   |   |   |   |   |   |   | no |
| `dapg_2017` | 2017 | grasp, reorient, <br>functional/tool, other | RL+demo | NPG (Natural Policy Gradient) + BC pretraining <br>(DAPG) | ADROIT | 24 | no | MuJoCo | no |   |   | not addressed | yes |
| `openai_dexterity_2018` | 2018 | reorient | RL | PPO | ShadowRobot Dexterous Hand <br>(EDC electric-motor version) | 24 | no | MuJoCo | yes | 10 |   | not addressed | no |
| `openai_rubiks_cube_2019` | 2019 | reorient | RL, distillation | PPO with Automatic Domain Randomization (ADR); <br>Policy Cloning (DAGGER/distillation-style) for <br>architecture changes | Shadow Dexterous E Series Hand <br>(E3M5R) | 20 | no | MuJoCo (+ ORRB/Unity3D <br>for rendered vision <br>training images) | yes | 10 |   | not addressed | no |
| `pddm_2019` | 2019 | reorient, other | MPC | PDDM: ensemble of feed-forward dynamics models + <br>MPPI-style filtering/reward-weighted-refinement <br>trajectory optimizer (no policy network, no <br>policy-gradient training) | Shadow Hand (24-DoF, real and <br>sim); D'Claw (9-DoF, sim only, <br>valve turning) |   | no | MuJoCo | yes |   |   | not addressed | yes |
| `dexpilot_2020` | 2020 | reorient, grasp, <br>functional/tool, other | teleop-system | DART model-based hand tracker bootstrapped by <br>two learned neural priors (GloveNet ResNet-50 <br>keypoint regressor; PointNet++-based keypoint <br>network + JointNet FC mapping), online <br>fingertip-vector kinematic retargeting solved <br>via SLSQP (NLopt) warm-started each frame, <br>Riemannian Motion Policies for arm motion <br>generation | Wonik Robotics Allegro hand <br>(16-DoF, 4x4-joint fingers), <br>retrofitted with 4 SynTouch <br>BioTac tactile sensors at the <br>fingertips | 16 | no |   | yes | 150 |   | not addressed | no |
| `castro_sap_contact_2021` | 2021 | bimanual-coord |   | SAP (Semi-Analytic Primal) solver: a custom <br>Newton-type solver on an unconstrained convex <br>primal reformulation of compliant contact, with <br>analytic gradients, line search, and sparsity <br>exploitation | Allegro hand (16 DoF each), <br>two | 16 | yes | Drake | no |   |   | measured | yes |
| `dexmv_2021` | 2021 | grasp, functional/tool | RL+demo, <br>data-collection | DAPG / SOIL / GAIL+ on top of TRPO, using <br>demonstrations translated from human video via <br>TSV retargeting + inverse-dynamics action <br>estimation | Adroit Hand | 30 | no | MuJoCo | no |   | 500 | not addressed | yes |
| `dexpoint_2022` | 2022 | grasp, other | RL | PPO | Allegro Hand | 16 | no | SAPIEN | yes | 260 | 40 | not addressed | yes |
| `dextreme_2022` | 2022 | reorient | RL | PPO (rl-games implementation, LSTM actor/critic, <br>asymmetric/state-privileged critic) | Allegro Hand | 16 | no | Isaac Gym (PhysX) | yes | 10 |   | not addressed | yes |
| `dexvip_2022` | 2022 | grasp | RL | PPO with a video-mined consensus grasp-pose <br>auxiliary reward (R_pose) combined with an <br>affordance reward (R_aff) and a lift-success <br>reward (R_succ) | Adroit Hand | 30 | no | MuJoCo | no |   |   | not addressed | no |
| `dime_2022` | 2022 | reorient, grasp | teleop-system, BC, <br>RL+demo | INN/VINN (nearest-neighbor imitation) vs. BC; <br>DAPG/PPO/BCRL (simulation RL-finetuning) | Allegro Hand |   | no | MuJoCo | yes | 10 |   | not addressed | yes |
| `holo_dex_2022` | 2022 | reorient, grasp, <br>functional/tool | teleop-system, BC | VINN (BYOL nearest-neighbor) vs. Behavior <br>Cloning / BC-Rep | Allegro Hand | 16 | no |   | yes | 10 | 10 | not addressed | yes |
| `hora_2022` | 2022 | reorient | RL, distillation | PPO | Allegro Hand (Wonik Robotics) | 16 | no | IsaacGym | yes | 240 | 30 | not addressed | yes |
| `mjpc_2022` | 2022 | reorient | MPC | Predictive Sampling: zero-order, derivative-free <br>sampling-based shooting MPC over a <br>spline-parameterised control sequence; the <br>framework (MJPC) also implements iLQG and <br>Gradient Descent as alternative planners, but <br>the Hand result is attributed to Predictive <br>Sampling | Shadow Hand (MuJoCo Menagerie <br>model) |   | no | MuJoCo | no |   |   | not addressed | yes |
| `pang_global_planning_2022` | 2022 | reorient, grasp, <br>bimanual-coord, other | trajopt | iMPC (iLQR-style trajectory optimizer over a <br>locally-smoothed convex quasi-dynamic contact <br>model, CQDC) for local case studies; an RRT <br>variant (RRT-through-contact) using a smoothed <br>Mahalanobis distance metric, single-step <br>dynamically-consistent extension, and contact <br>sampling for global planning on harder tasks | Allegro Hand (full 3D model, <br>in-hand rotation / pen <br>placement / plate pickup / <br>door opening); a <br>2-DoF-per-finger planar hand <br>(2 fingers) for 2D <br>reorientation tasks |   | yes | Custom Convex <br>Quasi-Dynamic <br>Differentiable Contact <br>(CQDC) model implemented <br>in Drake <br>(MultibodyPlant/SceneGraph), <br>validated against <br>Drake's own <br>high-fidelity <br>second-order contact <br>solver | yes |   |   | constrained | yes |
| `videodex_2022` | 2022 | grasp, reorient, <br>functional/tool | BC, data-collection | two-stream Neural Dynamic Policy (NDP) <br>trajectory regression (L1 loss): pretrained on <br>human-video-retargeted trajectories, fine-tuned <br>on real teleoperated demonstrations; R3M visual <br>encoder | LEAP Hand | 16 | no |   | yes |   |   | not addressed | no |
| `visual_dexterity_2022` | 2022 | reorient | RL, distillation | PPO (teacher, privileged state) + DAgger <br>imitation distillation to a depth-point-cloud <br>student (two-stage: synthetic-PC pretrain then <br>rendered-occluded-PC fine-tune) | D'Claw (open-source, low-cost; <br>3-finger and modified 4-finger <br>versions) |   | no | Isaac Gym (PhysX) | yes | 20 | 12 | not addressed | yes |
| `aloha_act_2023` | 2023 | bimanual-coord | BC | ACT (Action Chunking with Transformers, CVAE) | parallel-jaw gripper (not <br>dexterous), two |   | yes | MuJoCo | yes | 25 |   | not addressed | yes |
| `anyteleop_2023` | 2023 | grasp, functional/tool, <br>handover | teleop-system, <br>RL+demo | DAPG (downstream IL); keypoint-vector <br>retargeting optimization (dex_retargeting) | Allegro Hand |   | no | SAPIEN | yes | 100 |   | not addressed | yes |
| `artigrasp_2023` | 2023 | grasp, functional/tool, <br>bimanual-coord | RL | PPO (D-Grasp-based implementation) | MANO hand model, two | 51 | yes | RaiSim | no |   | 1 | not addressed | yes |
| `dexdeform_2023` | 2023 | bimanual-coord, other | BC, trajopt | latent skill model (VAE over demonstrations) for <br>skill-planned trajectory initialization, refined <br>by gradient-based trajectory optimization <br>through a differentiable MPM simulator, with <br>refined rollouts fed back as new demonstrations | Shadow Dexterous Hand <br>(simulated) | 28 | yes | PlasticineLab (MLS-MPM, <br>CUDA), built on Hu et <br>al. 2018's Moving Least <br>Squares Material Point <br>Method | no |   |   | not addressed | yes |
| `dexpbt_2023` | 2023 | grasp, reorient, <br>bimanual-coord | RL | PPO (rl_games) with decentralized <br>Population-Based Training (PBT) over RL <br>hyperparameters and reward-shaping coefficients | Allegro Hand | 16 | yes | Isaac Gym (PhysX) | no |   |   | not addressed | yes |
| `dexterous_functional_grasping_2023` | 2023 | functional/tool | RL | PPO | LEAP hand | 16 | no | IsaacGym | yes | 70 | 5 |   | no |
| `diffusion_policy_2023` | 2023 | grasp, functional/tool, <br>bimanual-coord, other | BC, diffusion | conditional DDPM over action sequences (CNN or <br>transformer noise-prediction network), DDIM at <br>inference |   |   | yes | task-specific: Robomimic <br>(MuJoCo-backed), Push-T <br>(custom 2D physics per <br>IBC), BlockPush (per <br>BET), Franka Kitchen <br>(per Relay Policy <br>Learning); no single <br>engine/timestep stated <br>for the combined <br>benchmark | yes | 20 |   | not addressed | yes |
| `dynamic_handover_2023` | 2023 | handover, bimanual-coord | RL | MAPPO | Allegro Hand | 16 | yes | IsaacGym | yes | 15 | 14 | not addressed | no |
| `eureka_2023` | 2023 | reorient, <br>bimanual-coord, other | RL | PPO with LLM-authored (GPT-4) evolutionary <br>reward search | Shadow Hand (also Allegro <br>Hand; bimanual pairs of Shadow <br>Hands for Dexterity tasks) | 20 | yes | IsaacGym | yes |   |   | not addressed | yes |
| `pgdm_2023` | 2023 | grasp, functional/tool | RL | PPO (Stable-Baselines3) with an <br>object-trajectory-tracking reward plus <br>pre-grasp-based exploration initialization <br>(PGDM) | ShadowHand | 24 | no | MuJoCo | yes |   |   | not addressed | no |
| `physhoi_2023` | 2023 | track-human-ref | RL | PPO | SMPL-X humanoid (simulated, <br>not a robot hand) | 90 | no | Isaac Gym | no |   |   | not addressed | yes |
| `robot_synesthesia_2023` | 2023 | reorient | RL, distillation | PPO | Allegro Hand | 16 | no | Isaac Gym | yes | 5 |   | not addressed | no |
| `rotateit_2023` | 2023 | reorient | RL, distillation | PPO | AllegroHand (Wonik Robotics) | 16 | no | IsaacGym | yes |   | 15 | not addressed |   |
| `rotating_without_seeing_2023` | 2023 | reorient | RL | PPO | Allegro Hand | 16 | no | IsaacGym | yes | 30 | 5 | not addressed |   |
| `unidexgrasp_2023` | 2023 | grasp | grasp-synthesis, RL, <br>distillation | PPO (teacher) + DAgger (student distillation) | ShadowHand | 26 | no | Isaac Gym | no |   | 241 | penalised | yes |
| `unidexgrasp_pp_2023` | 2023 | grasp | RL, distillation | PPO + DAgger (with critic distillation) | Shadow Hand | 24 | no | Isaac Gym | no |   |   | not addressed | yes |
| `ace_teleop_2024` | 2024 | grasp, functional/tool | teleop-system, BC | 3D Diffusion Policy (DP3) for xArm platforms; <br>ACT for H1 humanoid (downstream IL); IK-based <br>scale/recenter end-effector mapping + AnyTeleop <br>fingertip-vector hand retargeting | Ability Hand / Inspire Hand / <br>parallel-jaw gripper <br>(embodiment-dependent) |   | yes |   | yes | 10 | 18 | not addressed | no |
| `anyrotate_2024` | 2024 | reorient | RL, distillation | PPO | Allegro Hand | 16 | no | IsaacGym | yes |   | 10 | not addressed | no |
| `asymdex_2024` | 2024 | bimanual-coord, grasp | RL | PPO | Shadow Hand (30-DoF: 24-DoF <br>hand + 6-DoF floating wrist) <br>in simulation; 16-DoF Allegro <br>hand + 6-DoF Ability Hand <br>(mismatched, <br>hardware-availability <br>artifact) in real-world <br>experiments | 30 | yes | NVIDIA Isaac Gym | yes | 20 |   | not addressed | yes |
| `bidex_teleop_2024` | 2024 | bimanual-coord, <br>handover, <br>functional/tool | teleop-system, BC | ACT (Action Chunking Transformer) | LEAP Hand (16 DoF); LEAP Hand <br>V2 (21 DoF) used for 'extreme <br>dexterity' experiments | 16 | yes | none | yes | 20 |   | not addressed | no |
| `bidexhd_2024` | 2024 | functional/tool, <br>bimanual-coord | RL, distillation | IPPO (teacher) + DAgger (student distillation) | LEAP Hand, left and right | 16 | yes | Isaac Gym (PhysX) | no |   |   | not addressed | yes |
| `bimangrasp_2024` | 2024 | grasp, bimanual-coord | grasp-synthesis, <br>diffusion | MALA (Metropolis-adjusted Langevin) energy <br>optimisation + DDPM (BimanGrasp-DDPM) | Shadow Hand, pair | 22 | yes | Isaac Gym | no |   | 225 | penalised | no |
| `bunny_visionpro_2024` | 2024 | grasp, functional/tool, <br>bimanual-coord | teleop-system, BC | ACT, Diffusion Policy, DP3 (downstream IL); SQP <br>fingertip-vector hand retargeting + unified <br>IK/singularity/collision arm-motion optimization | Ability Hand | 24 | yes |   | yes | 10 |   | not addressed | yes |
| `cyberdemo_2024` | 2024 | grasp, reorient, <br>functional/tool | BC, teleop-system, <br>data-collection | ACT (Action Chunking with Transformers) BC <br>policy, trained on sim teleoperation <br>demonstrations augmented via Sensitivity-Aware <br>Kinematics Augmentation, automatic curriculum <br>learning, and action aggregation, fine-tuned on <br>real demonstrations | Allegro Hand | 16 | no | SAPIEN | yes | 20 | 2 | not addressed | no |
| `demostart_2024` | 2024 | grasp, functional/tool, <br>reorient, other | RL, distillation | MPO (teacher, auto-curriculum) + BC distillation <br>(student, Perceiver-Actor-Critic) | DEX-EE Hand | 12 | no | MuJoCo | yes | 100 |   | not addressed | no |
| `dexcap_2024` | 2024 | grasp, bimanual-coord, <br>functional/tool | BC, diffusion, <br>data-collection | Diffusion Policy with Perceiver point-cloud <br>encoder (DP-perc) | LEAP Hand | 16 | yes | none | yes | 60 | 9 |   | yes |
| `dexmimicgen_2024` | 2024 | bimanual-coord, grasp, <br>functional/tool | data-collection, BC | MimicGen-style per-arm subtask transform/replay <br>generation; downstream BC-RNN / BC-RNN-GMM / <br>Diffusion Policy | Inspire dexterous hand (6-DoF, <br>real-world GR1); unnamed <br>'dexterous hands' in the two <br>simulated dexterous-hand <br>embodiments | 6 | yes | RoboSuite (MuJoCo) | yes | 20 |   |   | yes |
| `dp3_2024` | 2024 | reorient, grasp, <br>functional/tool, <br>bimanual-coord, other | BC, diffusion | Diffusion Policy backbone (DDPM training / DDIM <br>inference) conditioned on a compact 3D <br>point-cloud feature (small MLP + max-pool <br>encoder) instead of image features | Shadow Hand (Adroit, <br>Bi-DexHands, DexDeform, DexMV <br>domains); Allegro Hand <br>(DexArt, HORA domains; also <br>real Roll-Up/Dumpling/Drill); <br>parallel gripper (MetaWorld; <br>real Pour) |   | yes | MuJoCo (Adroit, <br>MetaWorld), IsaacGym <br>(Bi-DexHands, HORA), <br>Sapien (DexArt, DexMV), <br>PlasticineLab <br>(DexDeform) | yes | 40 | 5 | not addressed | yes |
| `dreureka_2024` | 2024 | reorient | RL | PPO with LLM-authored (GPT-4) reward search + <br>reward-aware physics prior domain randomization | LEAP hand | 16 | no | Isaac Gym | yes |   |   | not addressed | yes |
| `egomimic_2024` | 2024 | grasp, functional/tool, <br>bimanual-coord | BC | shared-backbone ACT variant co-trained on paired <br>egocentric human video and teleoperated bimanual <br>robot demonstrations, with dual pose-space and <br>joint-space action heads | parallel-jaw gripper (not a <br>dexterous hand; see note scope <br>flag) | 1 | yes |   | yes | 135 |   | not addressed | yes |
| `graspxl_2024` | 2024 | grasp | RL | PPO | MANO (also Shadow Hand, <br>Allegro Hand, Faive Hand) | 45 | no | RaiSim | no |   | 503409 | not addressed | yes |
| `hato_visuotactile_2024` | 2024 | handover, bimanual-coord | diffusion | Diffusion Policy (DDPM, CNN-based) | Psyonic Ability Hand, two | 6 | yes |   | yes | 10 |   | not addressed | yes |
| `hudor_2024` | 2024 | grasp, functional/tool | RL | open-loop IK replay of a single retargeted human <br>fingertip trajectory plus online residual RL <br>(DrQv2) trained with an object-centric <br>point-tracking trajectory-matching reward | Allegro Hand | 16 | no |   | yes | 10 |   | not addressed | no |
| `humanplus_2024` | 2024 | track-human-ref, <br>locomanipulation | RL, BC | PPO (HST shadowing policy) + decoder-only <br>Transformer BC (HIT) | Inspire-Robots RH56DFX, two | 6 | yes | Isaac Gym-based <br>legged_gym/rsl_rl | yes | 10 |   | not addressed | yes |
| `objdex_2024` | 2024 | track-human-ref, <br>bimanual-coord | BC, RL, distillation | BC (Transformer high-level planner) + PPO <br>(low-level controller) | Shadow Hand |   | yes |   | yes | 80 | 1 | not addressed | no |
| `okami_2024` | 2024 | grasp, functional/tool, <br>bimanual-coord | trajopt, BC | single-video imitation: SLAHMR-extended SMPL-H <br>body+hand reconstruction, <br>GPT-4V/Grounded-SAM/Cutie object-centric <br>reference-plan construction, factorized arm IK <br>(Pink) + dex-retargeting hand-joint mapping, <br>SE(3) trajectory warping to new object poses at <br>test time; optional downstream ACT BC policy <br>trained on OKAMI-generated rollouts | Inspire Hand (x2) | 6 | yes | RoboSuite (2 of 6 tasks <br>only) | yes | 12 |   | not addressed | yes |
| `omnigrasp_2024` | 2024 | grasp, track-human-ref | RL, distillation | PPO (hierarchical: PHC-X finger imitator → <br>PULSE-X distilled latent prior → PPO over latent <br>action space) | SMPL-X whole-body humanoid <br>(simulated, not a robot hand) | 90 | yes | Isaac Gym | no |   | 5 | not addressed | yes |
| `omnih2o_2024` | 2024 | track-human-ref, <br>locomanipulation | RL, distillation | PPO (teacher) + DAgger (student) + diffusion <br>policy (autonomy layer) | Inspire hands (open-loop, DoF <br>not stated) |   | yes |   | yes | 20 |   |   | yes |
| `open_television_2024` | 2024 | bimanual-coord, <br>functional/tool | teleop-system, BC | ACT (Action Chunking Transformer) with DinoV2 <br>ViT backbone | Inspire Robots hand (6 <br>actuated DoF, 12 total); <br>Fourier GR-1 embodiment <br>instead uses a 1-DoF <br>parallel-jaw gripper | 6 | yes | none | yes | 20 |   | not addressed | yes |
| `openvla_2024` | 2024 | other | VLA | autoregressive next-token prediction over <br>discretized (256-bin per-dimension, <br>quantile-based) action tokens, single-step (no <br>action chunking) |   |   | no | LIBERO benchmark <br>(simulated Franka) for <br>fine-tuning experiments; <br>engine/version not <br>stated | yes | 230 |   | not addressed | yes |
| `penspin_2024` | 2024 | reorient | RL, distillation | PPO + BC | Allegro Hand | 16 | no | Isaac Gym | yes | 50 | 7 | not addressed | yes |
| `pi0_2024` | 2024 | other | VLA, flow | conditional flow matching <br>(linear-Gaussian/optimal-transport probability <br>path), forward-Euler integration at inference <br>(10 steps), shifted-Beta noisy-timestep sampling |   |   | yes |   | yes | 10 |   | not addressed | yes |
| `pianomime_2024` | 2024 | music | RL+demo, <br>distillation | PPO (per-song specialists); DDPM diffusion <br>(generalist) | Shadow Hand E3M5 | 23 | yes | ROBOPIANIST (MuJoCo) | no |   |   | not addressed | yes |
| `rdt1b_2024` | 2024 | bimanual-coord | diffusion | RDT (DiT + cross-attention, QKNorm/RMSNorm, MLP <br>decoder, Alternating Condition Injection) | parallel-jaw gripper <br>(ALOHA-style, Cobot Mobile <br>ALOHA), two |   | yes |   | yes | 139 | 2 | not addressed | yes |
| `resdex_2024` | 2024 | grasp | RL, distillation | PPO + DAgger | ShadowHand | 18 | no | IsaacGym | no |   | 241 | not addressed | yes |
| `twisting_lids_2024` | 2024 | functional/tool, <br>bimanual-coord | RL | PPO (asymmetric actor-critic) | Allegro Hand, two | 16 | yes | Isaac Gym | yes | 20 | 15 | not addressed | no |
| `umi_2024` | 2024 | functional/tool, <br>bimanual-coord, other | BC, diffusion, <br>data-collection, <br>teleop-system | Diffusion Policy (unmodified loss/decoder); <br>contribution is the hand-held data-collection <br>hardware and the observation/action interface <br>(relative-trajectory representation, <br>inference-time latency matching) |   |   | yes |   | yes | 260 |   |   | yes |
| `articulated_tools_inhand_2025` | 2025 | functional/tool | RL, BC, distillation | PPO (oracle) + BC (student + CATFA online <br>adaptation) | Inspire Hand | 6 | no | IsaacLab | yes | 50 |   | not addressed | no |
| `being_h0_2025` | 2025 | grasp, functional/tool | VLA, BC | autoregressive next-token prediction over <br>discretized MANO motion tokens (Grouped Residual <br>Quantization) for pretraining; L1-loss MLP <br>regression head over learnable query tokens for <br>post-training imitation learning | 6-DoF Inspire hand mounted on <br>a 7-DoF Franka Research 3 arm <br>(real robot); MANO parametric <br>hand model used as the <br>pretraining representation (no <br>physical hardware) | 6 | no |   | yes | 20 |   | not addressed | yes |
| `clutterdexgrasp_2025` | 2025 | grasp | RL, diffusion, <br>distillation | PPO (teacher) + DP3 diffusion policy (student) | AgiBot dexterous hand | 6 | no | Isaac Gym | yes | 167 | 2029 | constrained | no |
| `cross_embodiment_world_models_2025` | 2025 | other | world-model, MPC | DPI-Net (graph neural network particle-dynamics <br>world model) + sampling-based receding-horizon <br>MPC | PSYONIC Ability Hand (6-DoF) <br>and Robot Era XHand (12-DoF) <br>for real-world deployment; <br>trained across 6 simulated <br>hands (Ability, Allegro, <br>XHand, Leap, Shadow, <br>forearm-less Shadow variant) <br>for the embodiment-scaling <br>study |   | no | SAPIEN (rigid-body <br>Object Pushing data) and <br>Rewarped (differentiable <br>multiphysics, deformable <br>Plasticine Reshaping <br>data) | yes | 20 |   | not addressed | no |
| `dexgraspvla_2025` | 2025 | grasp, other | VLA, diffusion | hierarchical VLA: frozen VLM high-level planner <br>(bounding-box affordance) + DiT diffusion-policy <br>controller conditioned on frozen DINOv2 features <br>and a SAM+Cutie object mask, trained end-to-end <br>from scratch by imitation learning (MSE <br>noise-prediction loss); Immiscible Diffusion <br>noise assignment; DDIM sampling (16 of 50 <br>training steps) | PsiBot G0-R, 6-DoF, single <br>(right) hand | 6 | no |   | yes | 1287 | 360 | not addressed | yes |
| `dexmachina_2025` | 2025 | track-human-ref, <br>bimanual-coord | RL | PPO (rl-games) | six URDFs: Inspire, Allegro, <br>XHand, Schunk (main), Ability, <br>DexRobot Dex Hand |   | yes | Genesis | no |   |   | constrained | yes |
| `dexman_2025` | 2025 | track-human-ref, <br>bimanual-coord | RL, trajopt | PPO (RL_GAMES) residual policy on top of <br>IK-retargeted human motion | Shadow Dexterous Hand |   | yes | NVIDIA Isaac Gym | no |   |   |   | no |
| `dexndm_2025` | 2025 | reorient | RL, distillation | PPO (oracle) + BC (generalist) + supervised <br>residual policy | LEAP hand |   | no | Isaac Gym | yes |   |   | not addressed | no |
| `dexplore_2025` | 2025 | track-human-ref | RL, distillation | PPO (teacher) + DAgger-style VAE distillation <br>(student) | Inspire hand (also Allegro <br>hand) | 6 | no | Isaac Gym | yes |   | 2 | not addressed | yes |
| `dexremoe_2025` | 2025 | reorient | RL | PPO | GX11 three-fingered dexterous <br>hand (custom) | 11 | no | IsaacGym | no |   | 50 | not addressed | no |
| `dexteritygen_2025` | 2025 | reorient, <br>functional/tool, grasp | RL, diffusion | RL-generated Anygrasp-to-Anygrasp transitions <br>used to train a UNet DDPM diffusion foundation <br>controller (DexGen) with gradient-guided <br>diffusion sampling that projects an external <br>(teleoperated) command onto a safe, <br>high-likelihood learned action | Allegro Hand | 16 | no |   | yes | 240 |   |   | no |
| `dexterous_handover_2025` | 2025 | handover, grasp | RL | PPO | Allegro Hand |   | no | IsaacLab | no |   | 3 | not addressed |   |
| `dextrack_2025` | 2025 | track-human-ref | RL+demo | PPO + IL action-supervision loss | Allegro hand (sim); LEAP hand <br>(real) | 16 | no | Isaac Gym | yes |   |   | measured | yes |
| `dexumi_2025` | 2025 | grasp, functional/tool | BC, data-collection | diffusion policy (DDPM-style action-chunking) <br>trained on exoskeleton-collected demonstrations <br>converted to robot-hand-looking video via a SAM2 <br>segment/inpaint/composite pipeline | Inspire Hand (12 DoF, 6 <br>active) and XHand (12 active <br>DoF) |   | no |   | yes | 20 |   |   | yes |
| `dexvla_2025` | 2025 | grasp, functional/tool, <br>bimanual-coord | VLA, diffusion | ScaleDP (Scale Diffusion Policy, <br>transformer-based diffusion action head, up to <br>1B parameters, multi-head per embodiment) <br>plugged into a Qwen2-VL-2B VLA backbone, trained <br>with a 3-stage 'Embodied Curriculum Learning' <br>recipe; loss L = Ldiff + αLntp (α=1) | Robotiq parallel-jaw gripper <br>(Franka rig a, Bimanual UR5e <br>rig c); Inspire multi-fingered <br>dexterous hand, 6-DoF hand <br>joint space (Franka rig b); <br>AgileX bimanual arm <br>end-effector unnamed (rig d) |   |   | LIBERO (secondary, App. <br>A.2 only; main results <br>are real-robot) | yes | 10 | 30 | not addressed | yes |
| `dexwild_2025` | 2025 | grasp, functional/tool, <br>bimanual-coord | BC, data-collection | diffusion U-Net policy (also compared against <br>ACT) co-trained on human wearable-rig <br>demonstrations and teleoperated robot <br>demonstrations via fixed-ratio batch sampling | LEAP Hand / LEAP Hand V2 <br>Advanced | 17 | yes |   | yes |   | 11 |   | yes |
| `dydexhandover_2025` | 2025 | handover, bimanual-coord | RL | MAPPO (human-regularized, CTDE, with hybrid <br>advantage estimation) | 11-DoF (6 actuated) dexterous <br>hand, per side (vendor not <br>stated) | 11 | yes | NVIDIA Isaac Sim / Isaac <br>Lab | no |   | 9 | not addressed | no |
| `egozero_2025` | 2025 | grasp, functional/tool | BC | closed-loop Transformer policy (BC, Gaussian NLL <br>loss) over a morphology-agnostic 3D-point <br>state-action space (triangulated object <br>keypoints + thumb/index 3D coordinates + a <br>thresholded grasp scalar) | Franka Panda parallel-jaw <br>gripper (not a dexterous hand; <br>see note scope flag) | 1 | no |   | yes | 15 |   | not addressed | yes |
| `gemini_robotics_15_2025` | 2025 | other | VLA |   | ALOHA parallel gripper (by <br>platform convention, not <br>re-specified); Bi-arm Franka <br>parallel gripper; Apollo <br>humanoid multi-finger <br>dexterous hand (grasp types <br>shown: single-finger push, <br>cylindrical side grasp, medium <br>wrap, five-finger power grasp, <br>bimanual grasp/rotate; no DoF <br>or vendor model given for any <br>embodiment) |   | yes | MuJoCo (used to generate <br>evaluation scenes at <br>scale, not for training; <br>engine timestep/contact <br>model not stated) | yes |   |   | not addressed | no |
| `gemini_robotics_2025` | 2025 | other, handover | VLA, distillation |   | ALOHA 2 parallel gripper, two <br>fingers (primary embodiment); <br>bi-arm Franka parallel <br>gripper; Apollo humanoid <br>five-fingered dexterous hand <br>(no model/DoF given, evaluated <br>only qualitatively) |   | yes |   | yes | 20 |   | not addressed | no |
| `geometric_retargeting_2025` | 2025 | grasp | teleop-system | per-finger MLP retargeting network (GeoRT) <br>trained offline against five geometric losses: <br>motion-direction preservation, C-space coverage <br>(Chamfer), flatness, pinch correspondence, and a <br>learned self-collision classifier | Allegro Hand |   | no |   | yes |   |   | not addressed | yes |
| `gr_dexter_2025` | 2025 | bimanual-coord, grasp | VLA | GR-Dexter (Mixture-of-Transformer VLA, flow <br>matching + next-token prediction, following <br>GR-3) | ByteDexter V2, two | 21 | yes |   | yes | 125 | 23 | not addressed | no |
| `groot_n16_2025` | 2025 | grasp, functional/tool, <br>bimanual-coord, <br>locomanipulation | VLA | flow-matching DiT action head (32 layers, per <br>page and cross-confirmed by code changelog) fed <br>by a Cosmos-2B VLM backbone (per page); predicts <br>state-relative action chunks for most <br>embodiments; no algorithm name beyond "DiT" is <br>given |   |   | yes | Galaxea R1 Pro simulated <br>on the BEHAVIOR suite; <br>physics engine, <br>timestep, and env count <br>not stated | yes |   |   | not addressed | yes |
| `groot_n1_2025` | 2025 | grasp, functional/tool, <br>bimanual-coord, handover | VLA, flow | dual-system architecture: Eagle-2 VLM (System 2, <br>reasoning) feeding a DiT flow-matching action <br>head (System 1, acting) via alternating <br>cross-/self-attention; K=4-step forward-Euler <br>denoising at inference; latent-action VQ-VAE for <br>labeling action-less video | Fourier dexterous hands, on <br>the Fourier GR-1 humanoid; <br>DoF/finger count not stated |   | yes | RoboCasa (Kitchen and <br>GR-1 Tabletop <br>benchmarks); DexMimicGen <br>(cross-embodiment suite <br>and sim pretraining-data <br>generation); underlying <br>physics engine and <br>timestep not stated | yes | 10 | 5 | not addressed | yes |
| `h_rdt_2025` | 2025 | grasp, functional/tool, <br>bimanual-coord | flow | 2B-parameter flow-matching diffusion transformer <br>(H-RDT), pretrained on EgoDex human hand-pose <br>trajectories then fine-tuned per robot <br>embodiment by reinitializing the state/action <br>adaptors and action decoder | parallel-jaw / 2-jaw grippers <br>at deployment (Aloha-Agilex, <br>ARX5, Franka-Panda, UR5+UMI); <br>no dexterous hand deployed, <br>though pretraining action <br>space includes bimanual <br>fingertip positions from <br>EgoDex |   | yes | RoboTwin 2.0 | yes | 25 |   | not addressed | no |
| `helix_2025` | 2025 | grasp, functional/tool, <br>handover | VLA | dual-network "System 1, System 2" VLA: S2 (7B <br>VLM, 7-9Hz) produces a continuous latent <br>conditioning vector consumed by S1 (80M-param <br>cross-attention encoder-decoder transformer, <br>200Hz); trained end-to-end with a "standard <br>regression loss" (no diffusion/flow-matching, no <br>formula given) |   |   | yes |   | yes |   |   | not addressed | no |
| `human2sim2robot_2025` | 2025 | track-human-ref | RL | PPO | Allegro Hand | 16 | no | IsaacGym | yes | 70 |   | not addressed | yes |
| `humanoid_policy_human_policy_2025` | 2025 | grasp, functional/tool | BC | Human Action Transformer (HAT), an ACT-style <br>action-chunking transformer co-trained jointly <br>on unified human (PH2D) and teleoperated-robot <br>demonstrations in a shared 54-D wrist-pose + <br>fingertip state-action space | Inspire Hand (x2, 5-fingered) | 6 | yes |   | yes | 230 |   | not addressed | yes |
| `humanoid_sim2real_recipe_2025` | 2025 | grasp, bimanual-coord, <br>handover | RL, distillation | PPO (asymmetric actor-critic) for per-task <br>specialist policies, distilled into a generalist <br>via Diffusion Policy trained on filtered <br>successful rollouts | Fourier GR1 hand (6 actuated + <br>5 underactuated DoF); <br>cross-embodiment check also <br>uses Inspire hand (6 actuated <br>+ 6 underactuated DoF) | 6 | yes | NVIDIA Isaac Gym | yes | 10 |   |   | no |
| `maniptrans_2025` | 2025 | track-human-ref, <br>bimanual-coord | RL, BC, diffusion | PPO (two-stage: frozen generalist imitator + <br>per-task residual policy) | Inspire Hand (12-DoF sim); <br>also Shadow(22), MANO(22), <br>Allegro(16) | 12 | yes | Isaac Gym | yes |   |   | not addressed | yes |
| `metis_2025` | 2025 | grasp, functional/tool, <br>bimanual-coord | VLA | Autoregressive next-token cross-entropy over <br>discretized 'motion-aware dynamics' tokens <br>(VQ-VAE visual dynamics + RQ-VAE motion <br>dynamics), plus a supervised continuous-action <br>regression head (Action Decoder); combined loss <br>L = Lar + lambda*Laction | Inspire dexterous hand <br>(paired, main real-robot <br>eval); cross-embodiment eval <br>uses 22-DoF SharpaWave <br>Dexterous Hand | 6 | yes |   | yes | 20 |   | not addressed | no |
| `pi05_2025` | 2025 | other | VLA, flow | hierarchical high-level discrete-subtask <br>prediction (FAST tokenizer, autoregressive) + <br>low-level flow-matching action expert; two-stage <br>schedule pretrain (alpha=0, 280k steps) then <br>post-train (alpha=10.0, 80k steps) |   |   | yes |   | yes | 40 |   | not addressed | yes |
| `pistar06_2025` | 2025 | other | VLA, RL, flow | RECAP: advantage-conditioned policy extraction <br>on a flow-matching VLA, using a distributional <br>value function (cross-entropy over 201 <br>discretized return bins) to compute an N-step <br>advantage and a binarized improvement indicator, <br>with classifier-free-guidance-style <br>advantage-conditioning dropout (30%) |   |   | yes |   | yes | 750 |   | not addressed | yes |
| `wm_dex_human_videos_2025` | 2025 | grasp | world-model, MPC | DexWM: a deterministic latent-space (DINOv2) <br>world model with a CDiT-based predictor <br>conditioned on MANO <br>fingertip-keypoint-difference actions, trained <br>with a state-prediction loss plus an auxiliary <br>hand-consistency heatmap loss; controlled via <br>CEM/MPC planning in latent space | Allegro Hand |   | no | RoboCasa | yes | 12 |   |   | no |
| `being_h05_2026` | 2026 | bimanual-coord, other | VLA, flow | Rectified Flow (continuous action velocity-field <br>prediction) + Masked Motion Token Prediction <br>(discrete cross-entropy channel) inside a <br>Mixture-of-Transformers / Mixture-of-Flow (MoF) <br>action expert with shared 'Foundation Expert' <br>layers and routed Top-K specialized experts | Inspire Hand (Franka FR3); <br>LinkerBot O6 (Unitree G1); <br>unnamed 6-DoF dexterous hands <br>on PND Adam-U and BeingBeyond <br>D1; parallel gripper on <br>LeRobot SO-101 (not dexterous) | 6 |   | LIBERO, RoboCasa <br>(engine/timestep not <br>stated) | yes | 20 |   | not addressed | yes |
| `bidexgrasp_2026` | 2026 | grasp, bimanual-coord | grasp-synthesis, <br>diffusion | bi-level QP-ADMM optimisation (region-pair init <br>+ decoupled per-hand force closure) + DDPM <br>generator | Shadow Hand pair (sim); <br>Inspire and BrainCo hands <br>(real) |   | yes | MuJoCo | yes | 260 | 30 | measured | no |
| `deximit_2026` | 2026 | bimanual-coord, grasp, <br>functional/tool | data-collection, BC, <br>grasp-synthesis, <br>trajopt | 4D hand-object reconstruction (ST2+FPose) + <br>LLM-based (Qwen3-VL) subtask decomposition with <br>Action-Centric Scheduling + BODex-style <br>force-closure grasp synthesis and keyframe <br>motion planning, feeding a 3D Diffusion Policy <br>(DP3) | XHands (real-world <br>deployment); exact simulation <br>hand not explicitly named |   | yes |   | yes |   |   | constrained | no |
| `dexora_2026` | 2026 | grasp, functional/tool, <br>bimanual-coord | VLA, diffusion, <br>teleop-system | Decoder-only diffusion transformer (28 layers, <br>hidden size 1024, 16 attention heads) with T5 <br>(language) and SigLIP (vision) encoders feeding <br>conditional tokens; DDPM training, DPMSolver++ <br>sampling for inference; training clips <br>reweighted by a discriminator trained with a <br>positive-unlabeled objective (DWBC-style <br>score-to-weight mapping) that scores <br>demonstration quality | XHAND dexterous hand (paired), <br>12 fully actuated joints per <br>hand, thumb and index <br>additionally support lateral <br>ab/adduction | 12 | yes | MuJoCo (digital twin of <br>the real platform, used <br>to generate the <br>synthetic corpus and <br>mirrored in real-time <br>teleoperation) | yes | 20 |   | not addressed |   |
| `dexteleop0_2026` | 2026 | grasp, functional/tool, <br>bimanual-coord | teleop-system, MPC | box-constrained QP shared-autonomy residual <br>controller (force tracking + multi-contact <br>force-torque balance + nominal stabilization <br>terms) on top of DexPilot-style vector <br>retargeting | Sharpa Wave (x2) | 22 | yes | NVIDIA IsaacSim 4.5 | yes | 35 |   |   | no |
| `egoscale_2026` | 2026 | grasp, functional/tool, <br>bimanual-coord | flow, VLA | flow-based VLA (GR00T N1-style): VLM backbone + <br>DiT action expert trained with a flow-matching <br>objective, in a three-stage recipe (large-scale <br>human-video pretraining, aligned human-robot <br>mid-training, task-specific post-training) | Sharpa Wave (22-DoF); <br>cross-embodiment target <br>Unitree G1 (7-DoF tri-finger <br>hand) | 22 | yes |   | yes | 10 |   |   | no |
| `force_grasp_sim2real_2026` | 2026 | grasp, reorient | RL | PPO (asymmetric actor-critic) | xHand | 12 | no | IsaacLab | yes | 70 | 2 |   | no |
| `poise_2026` | 2026 | reorient | RL | asymmetric PPO | Sharpa Wave hand | 22 | no | Isaac Lab | yes | 10 | 1 | not addressed | no |
| `simtoolreal_2026` | 2026 | functional/tool | RL | SAPG (PPO variant) | Sharpa five-fingered hand | 22 | no | IsaacGym | yes | 120 | 12 | not addressed | no |
| `teledexter_2026` | 2026 | reorient, <br>functional/tool | RL, teleop-system | single-stage RL (SAPG) with consecutive subgoal <br>co-tracking reward | SharpaWave (22-DoF, headline); <br>also LeapHand (16-DoF) | 22 | no | Isaac Gym | yes | 15 |   | penalised | no |
| `toporetarget_2026` | 2026 | track-human-ref | trajopt, RL | constrained Laplacian-optimization retargeting + <br>PPO tracking | Wuji Hand |   | no |   | yes |   |   | constrained | no |
| `unidex_2026` | 2026 | grasp, functional/tool | flow, VLA, <br>data-collection | UniDex-VLA: a pi0-style flow-matching VLA with a <br>Uni3D pointcloud encoder and Gemma-based <br>backbone, predicting actions in a unified <br>Function-Actuator-Aligned Space (FAAS) across 8 <br>dexterous hands | Inspire, Leap, Shadow, <br>Allegro, Ability, Oymotion, <br>XHand, Wuji (8 hands in <br>UniDex-Dataset); real-robot <br>eval uses Inspire, Wuji, and <br>Oymotion hands |   | no |   | yes | 20 | 1 |   | no |
| `viserdex_2026` | 2026 | reorient | RL, distillation | PPO (RSL-RL) | Allegro Hand | 16 | no | Isaac Lab | yes | 50 |   | not addressed | no |

*112 rows; 224 of 1568 cells (14%) are values no source stated.*
*No cell is truncated. A value wider than its column is wrapped at a word boundary, so a cell that runs to several rendered lines is one value and not several.*

![fig4_taxonomy](figures/fig4_taxonomy.svg)

## 5.2 Reinforcement learning

**The standard recipe.** Fifty-nine of the 112 method rows learn from a reward. Forty-eight name PPO as the algorithm, and
the next most frequent, DAPG, appears four times. Forty-three run their own experiments in a
GPU-parallel simulator from the Isaac family or Genesis, and 36 do both. Only 31 rows state an
environment count, with a median of 8192 and a maximum of 64000. Twenty-three rows distil a
privileged teacher into a deployable student, and 16 combine all three of PPO, a GPU simulator and
distillation. That 16-row intersection is the recipe as it is actually practised.

The hand is almost always an Allegro. It appears in 35 of the 112 method rows and in 17 of the 31
reorientation rows, ahead of Shadow at 21 and 6 and LEAP at 12 and 4.

Privilege is handled two ways. `openai_dexterity_2018` gives the value network object and target
orientation, joint angles, joint velocities and object velocities the policy never sees, with a
footnote recording that current object orientation was left out of the policy inputs by accident,
and `dextreme_2022` uses the same asymmetric critic with a 2048-unit LSTM against the actor's
1024. `hora_2022` instead compresses nine privileged object properties into an eight-dimensional
vector regressed from 30 steps of proprioception, and `visual_dexterity_2022` distils twice, from
a state teacher to a synthetic point cloud and then to a rendered one, for a fivefold speedup.

Domain randomisation is the part of the recipe with the least discipline.
`openai_rubiks_cube_2019` made it adaptive, pushing each range boundary out when performance at
that boundary exceeds 20 successes and pulling it in below 10, and `dextreme_2022` reproduced the
mechanism with a 256-sample queue and 40 percent of environments dedicated to boundary evaluation.
Both publish the discovered ranges. Below that standard, two shipped configurations disagree with
their own papers about what was randomised: `hora_2022` states a joint-noise range of U(0, 0.005)
against a shipped `jointNoiseScale` of 0.02, in a commit its own README says is not the one that
reproduces the paper, and `penspin_2024` zeroes the disturbance force its appendix describes.
`dexpbt_2023`'s `randomize: False` is not a third case: it is the IsaacGymEnvs default and agrees
with the paper's statement that randomisation was not used here.

**Reward engineering.** Table 5 puts the 21 in-hand reorientation methods against nine recurring term families and marks
each cell by where the term was found: in the paper, in the code, in both, or in the code with
every shipped configuration setting its weight to zero.

### Table 5. Reward terms across in-hand reorientation methods

| method | yr | goal or rotation tracking | object velocity | finger-object distance | hand-pose deviation | action rate or magnitude | torque, work or joint velocity | drop or failure | contact or force | success bonus | terms | code | paper/code mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `openai_dexterity_2018` | 2018 | paper |   |   |   |   |   | paper |   | paper | 3 | no |   |
| `openai_rubiks_cube_2019` | 2019 | paper |   |   |   |   |   | paper |   | paper | 3 | no |   |
| `dextreme_2022` | 2022 | both |   |   |   | both | both | code (0) |   | both | 6 | yes | yes |
| `hora_2022` | 2022 | both | both |   | both |   | both |   |   |   | 5 | yes | yes |
| `visual_dexterity_2022` | 2022 | both |   | both | paper |   | both | both | paper | both | 7 | yes | yes |
| `dexpbt_2023` | 2023 | both |   | both |   | code | paper | code (0) |   | both | 4 | yes | yes |
| `eureka_2023` | 2023 | paper | paper | paper |   |   |   |   |   |   |   | yes | yes |
| `robot_synesthesia_2023` | 2023 | paper | paper | paper |   | paper | paper | paper |   |   | 6 | no |   |
| `rotateit_2023` | 2023 | paper | paper |   | paper |   | paper |   |   |   | 6 |   |   |
| `rotating_without_seeing_2023` | 2023 | paper | paper | paper |   |   | paper | paper |   |   | 6 |   |   |
| `anyrotate_2024` | 2024 | paper | paper |   | paper |   | paper | paper | paper | paper | 10 | no |   |
| `demostart_2024` | 2024 |   |   |   |   |   |   |   |   | paper | 1 | no |   |
| `dreureka_2024` | 2024 | paper | paper |   | paper |   |   | paper |   |   | 4 | yes | yes |
| `penspin_2024` | 2024 | both | both |   | both | code (0) | both |   |   |   | 7 | yes | yes |
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
sparse success bonus, 11 penalise object velocity and 10 penalise a drop. Eight penalise deviation
of the hand from a canonical grasp pose, a family the plan for this table did not anticipate and
which had to be added. Six penalise action rate or magnitude, five reward closing the distance
from fingertips to the object, and four carry a contact or force mark at all.

Three cells an earlier draft marked *code* print *code (0)* instead, because in each the term is
in the released code with every shipped configuration setting its weight to zero:
`dextreme_2022`'s timeout reward, `dexpbt_2023`'s fall penalty, and `penspin_2024`'s action
penalty. Marking them *code* would tell a reader the code optimises something the paper does not
state, and leaving them blank would hide a term that is in the file. The repository carries the
config key and the zero beside each of the three marks.

Only three of the four contact marks are the finding. `anyrotate_2024` scores good and bad
fingertip contacts, `poise_2026` rewards a friction-cone wrench margin, and
`force_grasp_sim2real_2026` tracks a commanded grasp force. The fourth, `visual_dexterity_2022`,
penalises the *object* touching the table, a task-shaping term against using the table as a third
finger rather than a hand-object term, and its table-contact flag defaults to off, with no shipped
config setting it true. Three of 21 in-hand reorientation methods, then, put a hand-object contact
or force quantity in the reward, and none puts interpenetration in it. `teledexter_2026` penalises
interpenetration with a differentiable signed-distance term, but during offline reference
construction, not in the policy's reward. Across all 112 method rows, 85 do not address
penetration at all, 5 constrain it, 3 measure it, 3 penalise it and 16 say nothing either way. The
physical quality of the contact is not something this literature optimises.

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

**Curricula, populations and machine-written rewards.** Curricula in this literature relax physics or tighten tolerances. `dexpbt_2023` tightens a success
tolerance from 0.075 to 0.01 by a factor of 0.9 every 3000 environment steps once three successes
are logged, and `maniptrans_2025` starts at zero gravity and high friction and restores both while
narrowing a fingertip threshold from 6 cm to 4 cm. `dexmachina_2025` attaches virtual
spring-damper controllers to the object, lets them do the task at first, then decays their gains
to zero. The two that ablate the curriculum report it is load-bearing: `rotateit_2023` sets its
rotation-penalty weight to zero and ramps it to −0.1, because applying it from the start makes the
policy learn only to hold the object still, and `viserdex_2026`, whose performance-based
curriculum runs over regularisation weight, action latency and time between successes, fails
completely without the regularisation component.

Population-based training appears once. `dexpbt_2023` runs populations of 8, 16 and 32 agents,
splits them 30/40/30, mutates the middle and replaces the bottom with mutated copies of the top,
each float hyperparameter multiplied or divided by a factor drawn from U(1.1, 1.5) with
probability 0.2. It reports 30 hours on a single V100 for a five-billion-transition single-arm
run, and 0.32 trillion environment steps for its largest population.

`eureka_2023` has GPT-4 write the reward function directly, constrained to return a total and a
dictionary of named components, and feeds per-component statistics back between iterations. Its
appendix gives an example whose reward correlates at −0.26 with the human-written one and still
scores 1.45 on the human-normalised metric, the strongest argument in the corpus that hand-tuned
weights are not a ceiling. `dreureka_2024` moves the safety requirement into the prompt instead of
a penalty term, asking in words for a cube rotating at about 0.25 radians per second with fingers
penalised for leaving their initial pose. Neither can be checked against a file. Eureka's
generated rewards are written at run time to a gitignored directory and never committed, so the
reward behind any reported number cannot be recovered from the repository, though its README
documents the paper's budget of five iterations and sixteen samples as the default and marks the
shipped one-iteration block a fast-test preset. DrEureka's repository contains only the locomotion
and globe-walking trees, so its LEAP-hand reward has no code at all.

**Where reinforcement learning stalls.** Reinforcement learning stalls on objectives that are not learnable as stated. `anyrotate_2024`
found the angular-velocity objective unlearnable in the multi-axis setting and replaced it with a
moving keypoint target. `rotateit_2023` reports that its multi-axis policy "does not converge when
training with only reinforcement learning" and adds an imitation loss against single-axis oracles.
`eureka_2023` cannot spin a pen from scratch and needs a pretrain-then-finetune split, with the
from-scratch ablation failing to complete one cycle. Section 5.3's contact-graph term exists
because of the general shape of the problem: contact moves the object off the reference, so return
goes down, so the policy learns not to touch the object.

It stalls on geometry too. `hora_2022` fails on objects under 4 cm across because the fingers
collide with each other. What it does not stall on is publication: the real-trial counts behind
these headlines are small enough that section 7.1 treats them as the reporting problem they are.

## 5.3 Learning from human data

**Teleoperation and retargeting.** Table 6 lists the 30 corpus rows that describe a system for getting human motion onto a robot
hand, with the retargeting objective compressed to one clause each.

### Table 6. Teleoperation and human-data systems

| system | operator interface | robot hand | retargeting objective | latency | rig USD | data collected |
|---|---|---|---|---|---|---|
| `dexpilot_2020` | four RealSense D415 RGB-D cameras tracking a <br>bare hand, markerless; a coloured glove is <br>worn only offline to train the neural <br>hand-pose priors | Wonik Robotics Allegro hand <br>(16-DoF, 4x4-joint fingers), <br>retrofitted with 4 SynTouch <br>BioTac tactile sensors at <br>the fingertips | minimise a weighted squared distance between <br>human and Allegro fingertip task-space vectors, <br>with switching weights that close <br>primary-finger-to-thumb gaps and enforce a <br>minimum finger separation, plus a regulariser <br>toward the open hand, solved online with SLSQP | about one second, end <br>to end (Sec. IV) |   |   |
| `dexmv_2021` | human demonstrator recorded on video (cubic <br>capture rig, two RealSense D435 cameras), no <br>live teleoperation; hand pose (MANO) and <br>object pose extracted offline from the <br>recorded video | Adroit Hand | match human (MANO forward-kinematics) and robot <br>task-space vectors (palm-to-fingertip and <br>palm-to-mid-phalanx pairs) per frame via SLSQP <br>with a temporal-consistency term, then fit a <br>minimum-jerk joint trajectory and compute <br>torques via inverse dynamics |   |   | 700 traj, 7 h |
| `dexvip_2022` | no live operator; a consensus hand pose is <br>mined offline from curated HowTo100M video <br>frames via FrankMocap 3D hand-pose estimation <br>and k-medoid clustering | Adroit Hand | deterministic 4-stage geometric mapping (not an <br>optimization) from FrankMocap's 21-joint hand <br>pose to Adroit's 30-DoF joint space, applied <br>once offline to produce a single static <br>consensus target pose per object category, used <br>only as a reward target |   |   |   |
| `dime_2022` | vision-based, single RGB camera, MediaPipe <br>hand detector, no glove/headset/exoskeleton | Allegro Hand | map human fingertip 2D image locations directly <br>to fixed-height robot fingertip 3D targets (no <br>depth estimation), then solve per-finger inverse <br>kinematics for joint angles | not stated; targets at <br>30 Hz, PD loop at 300 <br>Hz |   | 30 traj |
| `holo_dex_2022` | VR headset (Meta Quest 2), built-in 4-camera <br>hand tracker, no glove/exoskeleton | Allegro Hand | direct joint-angle copy for index/middle/ring <br>fingers; thumb fingertip position matched via <br>inverse kinematics; pinky ignored (no cost <br>function or optimization) | under 100 ms on a <br>local network (Sec. <br>IV-D) | 399 |   |
| `videodex_2022` |   | LEAP Hand | hand poses mapped via a distilled MLP <br>replicating a Robotic-Telekinesis-style <br>fingertip/palm keypoint-vector energy function; <br>wrist trajectory computed via a PnP + monocular <br>SLAM + heuristic gravity-alignment + <br>workspace-rescaling pipeline, both applied <br>offline to build pretraining trajectories, not <br>run online at deployment |   |   | 965 traj |
| `anyteleop_2023` | vision-based, camera only (RGB or RGB-D, <br>single or multi-camera), MediaPipe <br>hand-keypoint detection, no <br>glove/headset/exoskeleton | Allegro Hand | minimize the difference between human and robot <br>fingertip keypoint vectors via forward <br>kinematics, with joint-limit constraints and a <br>temporal-smoothness penalty | 26-35 ms hand pose, <br>9-10 ms retargeting <br>(Table II); no <br>end-to-end figure |   |   |
| `pgdm_2023` |   | ShadowHand | for pre-grasps only: inverse kinematics fits the <br>robot hand's fingertip positions to a single <br>human hand pose frame near first contact, used <br>solely to initialize RL exploration; full object <br>trajectories are used directly as the RL goal <br>with no hand-trajectory retargeting |   |   | 40 traj |
| `ace_teleop_2024` | visual exoskeleton: 3D-printed bimanual <br>6-DoF-per-arm exoskeleton with wrist-mounted <br>cameras for MediaPipe finger tracking; not a <br>glove or VR headset | Ability Hand / Inspire Hand <br>/ parallel-jaw gripper <br>(embodiment-dependent) | wrist/end-effector pose mapped via a <br>scale-and-recenter IK transform <br>(Normal/Mirror/Bimanual modes) from exoskeleton <br>forward kinematics; finger joints retargeted via <br>AnyTeleop's fingertip-keypoint-vector <br>optimization with joint limits and temporal <br>smoothing | 27 Hz hand tracking; <br>no end-to-end figure | 600 |   |
| `bidex_teleop_2024` | Manus Meta motion-capture gloves for the <br>fingers plus GELLO-style teacher arms for <br>wrist and arm pose; no headset | LEAP Hand (16 DoF); LEAP <br>Hand V2 (21 DoF) used for <br>'extreme dexterity' <br>experiments | inverse kinematics from glove fingertip <br>positions to LEAP fingertip targets, with the <br>arm commanded directly in joint space from the <br>teacher arm rather than in end-effector space | claimed low-latency, <br>no number given | 6000 | 50 traj |
| `bunny_visionpro_2024` | VR headset (Apple Vision Pro) hand/wrist <br>tracking, plus a custom ERM haptic feedback <br>device driven by fingertip FSR tactile <br>sensors; no glove or exoskeleton | Ability Hand | minimize scaled human-robot fingertip <br>keypoint-vector distance via forward kinematics <br>with joint limits and temporal smoothness <br>(hand), solved online via SQP with a <br>reduced-dimension reformulation for loop joints; <br>separately, a unified IK + singularity-avoidance <br>+ sphere-approximated self-collision objective <br>for arm motion | 3.43 ms retargeting, <br>15.93 ms motion <br>control, >60 Hz <br>overall (Table 1) |   |   |
| `cyberdemo_2024` | vision-based teleoperation (single RealSense <br>camera observing operator hand motion, <br>real-time hand detection and retargeting via a <br>cited third-party system), not a glove or <br>headset | Allegro Hand | delegated entirely to the cited third-party <br>teleoperation system; CyberDemo does not <br>describe or modify the human-to-robot mapping <br>itself |   |   |   |
| `dexcap_2024` | wearable backpack rig: Rokoko EMF gloves, one <br>SLAM camera per wrist and a chest-mounted <br>RGB-D LiDAR; no robot in the loop during <br>collection | LEAP Hand | fingertip-position inverse kinematics into the <br>16-dim LEAP joint space anchored by the mocap <br>wrist pose, with the little finger discarded |   | 4000 | 787 traj, 4.5 h |
| `egomimic_2024` | human data: head-worn Project Aria glasses <br>(egocentric RGB + onboard SLAM/hand-tracking, <br>no glove or exoskeleton); robot <br>demonstrations: standard bimanual ViperX <br>teleoperation | parallel-jaw gripper (not a <br>dexterous hand; see note <br>scope flag) | no per-finger kinematic retargeting (end <br>effector is a 2-finger gripper); domain <br>alignment via a shared per-timestep <br>camera-centered reference frame, per-embodiment <br>Gaussian normalization of <br>proprioception/actions, and SAM2-based visual <br>masking with a directional line overlay applied <br>identically to human and robot streams |   | 1000 | 2,150 traj, 4 h |
| `hudor_2024` | VR headset (Meta Quest 3) built-in hand <br>tracking for fingertip 3D positions, <br>ArUco-marker rigid-body calibration into the <br>robot frame; demonstrator is in the same scene <br>as the robot, not internet video | Allegro Hand | direct Cartesian-space correspondence: human <br>fingertip 3D positions are treated as target <br>Cartesian positions for the corresponding robot <br>fingertips with no kinematic-chain optimization, <br>converted to joint commands via a custom <br>Jacobian-based gradient-descent IK |   |   | 4 traj |
| `okami_2024` | single human demonstrator recorded on a static <br>RGB-D camera (Intel RealSense D435i), no live <br>teleoperation and no glove/headset; single <br>video per task | Inspire Hand (x2) | factorized retargeting run once per <br>demonstration video: arm/shoulder-elbow-wrist IK <br>(via the Pink library, wrist position dominating <br>the objective) plus hand joint angles computed <br>via dex-retargeting from SMPL-H hand keypoints; <br>the resulting trajectory is affinely <br>SE(3)-warped at test time to match newly <br>localized object start/end poses, with fingers <br>retargeted independently of arm warping |   |   |   |
| `open_television_2024` | VR headset (Apple Vision Pro or Meta Quest 3) <br>with active stereo video streamed back from a <br>2-3 DoF camera gimbal on the robot's neck | Inspire Robots hand (6 <br>actuated DoF, 12 total); <br>Fourier GR-1 embodiment <br>instead uses a 1-DoF <br>parallel-jaw gripper | dex-retargeting keypoint-vector optimisation <br>over five wrist-to-fingertip and two <br>thumb-to-finger vectors, solved with SLSQP, with <br>end-effector position taken relative to the head <br>and orientation absolute | 60 Hz stereo round <br>trip and 60 Hz control |   |   |
| `dexteritygen_2025` | human teleoperator tracked via a Manus Glove <br>(retargeted to the Allegro hand at 300Hz via <br>an unreleased, confidential fast retargeting <br>method) plus a Vive tracker for 6-DoF wrist <br>pose driving the arm | Allegro Hand |   |   |   |   |
| `dexumi_2025` | hand-specific 3D-printed wearable exoskeleton <br>(per-robot-hand optimized joint-to-fingertip <br>kinematics), joint encoders reading <br>exoskeleton angles directly (no visual <br>fingertip retargeting), a wrist-mounted camera <br>(ARKit-tracked wrist pose), and matching <br>tactile sensors installed on both exoskeleton <br>and target robot hand | Inspire Hand (12 DoF, 6 <br>active) and XHand (12 active <br>DoF) | no visual/kinematic-chain retargeting at <br>inference; a learned per-joint regression model <br>maps exoskeleton encoder values directly to <br>robot motor values (calibrated by visually <br>overlaying exoskeleton and robot at matched <br>motor values), with the exoskeleton's mechanical <br>linkage itself optimized offline so its <br>fingertip workspace matches the target robot <br>hand's forward-kinematics workspace | per-sensor latency <br>measured and <br>compensated offline, <br>no figure |   | 1,355 traj |
| `dexwild_2025` | wearable, calibration-free rig: motion-capture <br>glove + two palm-mounted stereo cameras <br>(pinky-side and thumb-side) + wrist ArUco <br>marker tracking, worn by untrained operators; <br>no VR headset | LEAP Hand / LEAP Hand V2 <br>Advanced | robot hand kinematics optimized to match <br>observed human fingertip positions (fixed <br>hyperparameters, no per-user tuning); a relative <br>(delta) end-effector state-action representation <br>removes the need for a global coordinate frame, <br>and identical palm-camera mounting on human and <br>robot hands makes RGB observations look the same <br>across embodiments |   |   | 9,290 traj, 46.2 <br>h |
| `doglove_2025` | haptic force-feedback exoskeleton glove <br>(21-DoF encoder-based motion capture, 5-DoF <br>cable-driven force feedback, per-fingertip LRA <br>haptic feedback), plus an HTC Vive Tracker for <br>wrist localization; not vision-based | LEAP Hand | map glove-FK fingertip positions to robot <br>fingertip targets via the third-party Mink <br>differential-IK solver, with a single scalar <br>hand-size scaling factor; no paper-original cost <br>function | 30 Hz minimum system <br>rate (120 Hz mocap, 30 <br>Hz haptics) | 600 |   |
| `egozero_2025` | Project Aria smart glasses (egocentric fisheye <br>RGB + SLAM cameras + onboard hand/camera pose <br>tracking), no glove, no live teleoperation of <br>a robot during data collection; at inference <br>an iPhone provides the egocentric view instead <br>of Aria | Franka Panda parallel-jaw <br>gripper (not a dexterous <br>hand; see note scope flag) | no kinematic hand-to-robot retargeting; both <br>human and robot are represented in a shared <br>morphology-agnostic 3D-point space so the policy <br>transfers zero-shot without any cross-embodiment <br>pose-mapping step |   |   | 700 traj |
| `geometric_retargeting_2025` | Manus glove for fingertip keypoints + HTC Vive <br>tracker for wrist pose (real-world <br>evaluation); the retargeting method itself is <br>tracking-source-agnostic | Allegro Hand | learned per-finger neural network trained <br>offline (3-5 minutes) to jointly satisfy <br>motion-direction preservation, C-space coverage, <br>flatness, pinch correspondence, and <br>self-collision avoidance, replacing per-frame <br>online optimization with a single 1kHz forward <br>pass at inference | 1 kHz retargeting <br>inference, against <br>60-100 Hz for <br>optimisation baselines |   |   |
| `h_rdt_2025` | for pretraining: none (consumes EgoDex's <br>pre-existing released 3D hand-pose <br>annotations, no live capture by this paper); <br>for fine-tuning: standard teleoperation of <br>each robot platform, not described in detail | parallel-jaw / 2-jaw <br>grippers at deployment <br>(Aloha-Agilex, ARX5, <br>Franka-Panda, UR5+UMI); no <br>dexterous hand deployed, <br>though pretraining action <br>space includes bimanual <br>fingertip positions from <br>EgoDex | no explicit kinematic retargeting; the 48-D <br>bimanual wrist+fingertip human action space is <br>treated as a superset of most end-effector <br>action spaces, and the human-to-robot <br>correspondence is instead learned implicitly by <br>reinitializing and fine-tuning the state/action <br>adaptors and action decoder on paired robot data <br>while keeping the pretrained vision/language <br>backbone |   |   | 338,000 traj, <br>829 h |
| `humanoid_policy_human_policy_2025` | consumer VR headsets (Apple Vision Pro <br>built-in camera with ARKit hand/head tracking, <br>or Meta Quest 3/Vision Pro with a 3D-printed <br>ZED Mini stereo mount via an OpenTelevision <br>web app), <$700; robot-side demonstrations <br>collected via standard humanoid teleoperation | Inspire Hand (x2, <br>5-fingered) | no offline kinematic retargeting network; human <br>and robot share an identical 54-D state-action <br>space via a bijective fingertip-to-fingertip <br>correspondence (both are 5-fingered hands), <br>bridged only by action-speed interpolation <br>(human trajectories slowed ~4x) and instructing <br>operators to minimize torso movement |   | 700 |   |
| `wm_dex_human_videos_2025` |   | Allegro Hand | no explicit robot retargeting network; both <br>human hands (MANO 21-keypoint) and robot <br>end-effectors (Allegro fingertips via forward <br>kinematics; parallel-jaw grippers approximated <br>with dummy circular keypoints) are mapped into <br>the same fingertip-keypoint-difference action <br>representation, with the missing pinky filled by <br>reusing the ring-finger-equivalent Allegro <br>keypoints |   |   | 829 h |
| `dexteleop0_2026` | VR headset (Meta Quest 3), egocentric <br>hand/wrist tracking (26 tracked hand-joint <br>transforms per hand), no external motion <br>capture | Sharpa Wave (x2) | DexPilot-style vector matching of critical <br>inter-joint/finger-to-palm target vectors for <br>the hand, plus analytical IK on wrist pose for <br>the arm, producing a raw joint command that a <br>real-time QP then corrects to keep fingertip <br>contact forces in a safe window and balance net <br>object force/torque | 30 Hz QP control cycle |   |   |
| `egoscale_2026` | large-scale pretraining: in-the-wild <br>egocentric video with off-the-shelf SLAM + <br>hand-pose estimation, no dedicated capture <br>rig; aligned mid-training: Vive trackers for <br>3D wrist pose + Manus gloves for 25-joint <br>in-hand pose, same camera rig as the robot | Sharpa Wave (22-DoF); <br>cross-embodiment target <br>Unitree G1 (7-DoF tri-finger <br>hand) | human 21-keypoint (MANO-style) hand pose <br>retargeted via an optimization-based procedure <br>enforcing joint limits and kinematic constraints <br>into the 22-DoF Sharpa Wave hand joint space; <br>wrist motion is represented as a shared relative <br>SE(3) transform identical across human and robot <br>data |   |   | 20854 h |
| `teledexter_2026` | NOKOV motion-capture system tracking operator <br>hand pose and object 6D pose in real time (not <br>vision-based, not a glove) | SharpaWave (22-DoF, <br>headline); also LeapHand <br>(16-DoF) | two-stage geometry-aware retargeting: Stage 1 <br>fingertip-vector alignment to human hand <br>geometry; Stage 2 object-mesh-aware refinement <br>combining a surface-contact term, a <br>differentiable-SDF interpenetration penalty, a <br>self-collision sphere term, and a <br>temporal-smoothness term, producing the <br>fingertip+object-pose subgoals the RL controller <br>tracks |   |   |   |
| `unidex_2026` | human-video side: no live capture rig, <br>converts existing egocentric RGB-D datasets <br>(H2O, HOI4D, HOT3D, TACO) via offline <br>retargeting; fine-tuning demonstrations <br>collected via OpenTeleVision + dex-retargeting <br>on an Apple Vision Pro | Inspire, Leap, Shadow, <br>Allegro, Ability, Oymotion, <br>XHand, Wuji (8 hands in <br>UniDex-Dataset); real-robot <br>eval uses Inspire, Wuji, and <br>Oymotion hands | two-stage human-in-the-loop kinematic <br>retargeting: an automatic PyBullet <br>multi-end-effector IK stage aligns a 6-DoF <br>offset between a virtual human-hand-fixed base <br>and the real robot base to match fingertip <br>positions (respecting joint limits, with <br>iterative mimic-joint correction), followed by <br>an interactive GUI stage where a human manually <br>corrects alignment; a separate visual-alignment <br>step masks the human hand from the pointcloud <br>and re-renders the retargeted robot-hand mesh <br>into the scene |   |   | 52,000 traj |

*30 rows; 60 of 210 cells (28%) are values no source stated.*
*No cell is truncated. A value wider than its column is wrapped at a word boundary, so a cell that runs to several rendered lines is one value and not several.*

Retargeting splits four ways. The dominant family matches task-space vectors between the human and
robot hands. `dexpilot_2020` set the pattern with a weighted squared distance between fingertip
vectors, switching weights of 1, 200 and 400 by whether a pair is within threshold, a
minimum-separation constant of 3 cm between primary fingers, and a regulariser toward the open
hand, solved online with SLSQP; `anyteleop_2023`, `open_television_2024`, `bunny_visionpro_2024`
and `ace_teleop_2024` all use the same formulation. The second copies joint angles where the
kinematics allow it, as `holo_dex_2022` does for index, middle and ring while solving the thumb by
inverse kinematics and discarding the pinky the Allegro does not have. The third learns the map
offline: `geometric_retargeting_2025` trains a per-finger network in three to five minutes against
motion-direction, coverage, flatness, pinch and collision criteria, then runs at 1 kHz against the
60 to 100 Hz of online optimisation, raising configuration-space coverage from 38 to 90 percent
and one-time grasp success from 55 to 87.5 percent. The fourth removes retargeting from the loop:
`dexumi_2025` builds an exoskeleton whose fingertip workspace is optimised to match the target
hand, then regresses encoder values straight to motor values.

The table's empty cells are the point. Only 12 of the 30 rows carry a latency cell at all, three
of those give no number, and only 7 state a rig cost. Where costs are stated they are low and
falling, from `holo_dex_2022`'s $399 headset through the $600 exoskeleton of `ace_teleop_2024` and
the $600 haptic glove of `doglove_2025` to the $4,000 backpack of `dexcap_2024` and the $6,000 rig
of `bidex_teleop_2024`. Latency is not one quantity: `dexpilot_2020`'s "about one second" and
`holo_dex_2022`'s "under 100 milliseconds" are end to end, while `geometric_retargeting_2025`'s 1
kHz and `anyteleop_2023`'s 9 to 10 ms retargeting are single stages and several cells give a
control rate. The column mixes the two, so its spread is not a range. Only 13 rows report how many
trajectories were collected, and only 7 report hours.

Where throughput is measured, human collection beats teleoperation by a wide margin.
`humanoid_policy_human_policy_2025` times a grasp demonstration at 3.79 seconds for a bare human
and 19.72 seconds through a teleoperated humanoid, and a pour at 4.81 against 37.31 seconds. It
attributes the gap to retargeting latency and to the workspace of a 7-DoF arm rather than to
anything about the hand.

**Imitation architectures.** Four architectures cover the corpus. Action chunking came from `aloha_act_2023`, which predicts a
chunk of joint targets with a CVAE and combines overlapping chunks by exponentially weighted
ensembling, reaching 80 to 90 percent on fine bimanual tasks from about 50 demonstrations each.
Diffusion came from `diffusion_policy_2023`, which denoises an action sequence and reports a 46.9
percent average success improvement over LSTM-GMM, IBC and BET across 15 tasks. `dp3_2024` swaps
the image encoder for a small point-cloud encoder and reports 74.4 percent against 59.8 percent
across 72 simulated tasks, and 85.0 against 35.0 percent on four real tasks from 40 demonstrations
each. Flow matching is the 2024-onward default for large models and carries 8 of the 112 rows.
Discrete action tokens are the fourth, used by `openvla_2024` and `metis_2025`, and are the only
one of the four that needs no continuous head at all.

Data generation is a separate lever and is underrated. `dexmimicgen_2024` turns 60 human source
demonstrations into 21,000 simulated ones across 9 tasks and 3 embodiments, and a real Fourier GR1
with two Inspire hands reaches 90 percent from 40 generated demonstrations against 0 percent from
the 4 source ones. `dex1b_2025` iterates optimisation, a CVAE proposal model and a simulator
filter into roughly a billion synthetic grasps, and its CVAE baseline beats the prior best by 22
points.

**Human video without a robot.** Seven rows train a dexterous-hand policy from video with no teleoperation at any stage.
`dexmv_2021` retargets 700 self-recorded demonstrations by matching palm-to-fingertip task-space
vectors and estimating actions by inverse dynamics, `videodex_2022` mines 965 trajectories from
EpicKitchens to pretrain a neural dynamic policy, and `dexvip_2022` goes further into the reward,
clustering 715 curated HowTo100M frames into one consensus grasp pose per object category and
adding it as a reward term. `okami_2024`, `human2sim2robot_2025` and `hudor_2024` work from a
single video each, and `wm_dex_human_videos_2025` pretrains a world model on 829 hours of EgoDex.

**The embodiment gap.** Three papers measure the gap directly rather than asserting it. `okami_2024` runs the same
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

**Tracking a human reference with physics.** Twelve method rows sit in the human-reference tracking family. Eight track a human hand on an
object and are covered here; the other four sit at the edges, `human2sim2robot_2025` tracking only
the object's trajectory, `dexman_2025` retargeting bimanual video onto a full humanoid, and
`humanplus_2024` and `omnih2o_2024` tracking whole-body motion. A reference is retargeted onto the
robot and a policy trained to make the simulated body follow it: the reference supplies the
shaping reward engineering would otherwise have to invent, and the simulator the physical
consistency pure imitation lacks.

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

That is the pattern across all eight, and it is the reference-versus-rollout split in its sharpest
form. Penetration is handled at the reference, if at all, and never at the rollout. `objdex_2024`
completes the set with the only real-robot numbers among them, from 100 percent on a microwave and
a laptop down to 41.2 percent on a ketchup bottle over 20 trials each.

**The retargeting map, and what would close it.** Human data does not port across hands, and the map
is usually left unstated. Fifty-three method rows use human data and name 45 distinct hand strings
between them; twenty of those appear in Table 6 with a stated retargeting objective. The other 33
never say how the human motion reached the hand, and the objectives that are stated do not converge,
running from a fingertip keypoint-vector energy in `anyteleop_2023` through a per-joint regression
from exoskeleton encoders in `dexumi_2025` to no retargeting at all in `egozero_2025`. What would
close it is a retargeting benchmark in TopoRetarget's form `toporetarget_2026`, reporting contact
precision, contact alignment, maximum penetration and the share of frames past 2 mm, per hand and per
dataset.

## 5.4 Generalist and vision-language-action policies

The finding is the size of the hand. Eighteen rows carry the generalist tag. Fourteen of them
settle whether the reported evaluation ran on a multi-fingered hand. Eight of those fourteen did,
six report no hand result at all, and the remaining four never say, `groot_n16_2025` naming no end
effector anywhere on its page.

Five of the eight state a hand size, and that comparison has to be made in actuated degrees of
freedom rather than joints, for the reason section 3 opens with. Four are six, the Inspire RH56DFX
among them actuating six of its twelve joints, and one is twelve, `dexora_2026`'s XHAND. Their
median is 6. Two of the four rows that never settle the hand question do state a size, and both
are large: 21 for `gr_dexter_2025`'s ByteDexter V2 and 22 for `egoscale_2026`'s Sharpa Wave. Of
the 59 reward-learning rows, 48 state a count, 38 of those are 16 or above, and their median is
16: an Allegro and a LEAP actuate 16, and a Shadow actuates 20 of its 24 joints. So no row that
settles the question reaches the band the reinforcement-learning literature of section 5.2 works
in, and the two rows that reach it on paper are the two that never say whether the hand was in the
evaluation. An earlier version of this claim counted eleven rows as evaluating on a hand, which
mixed the settled eight with rows the notes leave open.

The six with no hand result are parallel-jaw throughout (`pi0_2024`, whose released code encodes
each ALOHA gripper as one scalar, `pi05_2025`, `pistar06_2025`, `openvla_2024`, `helix_2025`,
which claims individual-finger control of a 35-DoF upper body with no success rate or trial count
for any task, and `gemini_robotics_2025`, whose Apollo hand appears in a figure caption with no
number attached). Its successor `gemini_robotics_15_2025` closed that gap with Apollo progress
scores, not success rates, of 0.74 down to 0.62 across five generalisation axes. `dexvla_2025` is
the borderline case the other way: a hand in one real-robot task family, grippers in the other
five and in all 91 pretraining tasks.

The released code also drifts. `groot_n1_2025`'s repository is a later N1.7 generation with a
different backbone, a different action horizon and embodiments the paper does not describe, and
`pi05_2025`'s supports only the flow-matching head, not the hybrid recipe the paper describes.

**The size of the gap, and what would close it.** The gap is size rather than absence. A generalist
policy that does touch a hand runs it at roughly a third of the actuation the reinforcement-learning
literature assumes, and the rows that never settle the question are the smaller half of the same gap.
What would close it is one dexterous-hand task inside the standard generalist suite, with the hand's
actuated degrees of freedom and its vendor printed beside the number.

## 5.5 Model-based baselines and hybrids

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
117.16 seconds of planning on a 16-core CPU, against the GPU-days of section 5.2, and it is the
only method here that imposes non-penetration as a hard constraint. Its own limitation is the
honest part: its 3D systems transfer to hardware far worse than its 2D ones, because the
quasi-dynamic assumption breaks and planned grasps miss contacts under a second-order solver.

**Hybrids, and where the field has converged.** The recurring shape is reinforcement learning in simulation distilled into a policy that looks
like an imitation policy, and it appears in four variants. The first distils a privileged teacher
into a vision student inside one paper, which is `hora_2022`, `visual_dexterity_2022`,
`rotateit_2023`, `robot_synesthesia_2023` and `viserdex_2026`. The second uses reinforcement
learning as a demonstration factory: `dextrack_2025` mines demonstrations with per-trajectory RL
and trains a generalist on them, `maniptrans_2025` does the same to build a 3.3K-episode dataset,
and `dexteritygen_2025` trains a diffusion controller on ten billion simulated grasp-to-grasp
transitions and projects a human teleoperator's coarse command onto it, taking four reorientation
tasks from 0 out of 20 under raw teleoperation to 12, 13, 10 and 9 out of 20. The third generates
data without reinforcement learning at all, which is `dexmimicgen_2024`, `dex1b_2025` and
`deximit_2026`; `dex1b_2025`'s row is classed as a dataset, so figure 4's leaf, which counts
method rows, holds the other two. The fourth wraps an RL policy in a residual, which is
`resdex_2024` at 88.8 percent over 3,200 objects in 12 GPU-hours.

In the variants that dominate 2025 and 2026 work, the reward is no longer the objective of the
deployed policy. It is the objective of the process that produced the deployed policy's training
data. Reward engineering has moved upstream into data curation, and every reward-shaping pathology
in section 5.2 now reaches the shipped policy through a dataset rather than a gradient.

## 5.6 Paper against released code

Thirty-eight of the 112 method rows record a discrepancy between a paper and the code it released,
and all 38 released code, so they sit inside the 62 rows that released anything. They are not one
kind of thing. Nine are contradictions, where paper and code state different values or different
terms. Thirteen are limits of this survey's own parse, where the body or config that would settle
the question was never recovered and the row says so. Eight released code without the described
component in it, four are version skew against a later repository, and four are a paper
disagreeing with itself. The fourth version skew is `groot_n16_2025`, which ships a main branch
one generation later than the checkpoint its page describes.

Nine is the number to quote, eight at high confidence and one, `penspin_2024`, held at medium
pending a direct read of the code. Nine of 62 is 15 percent, bounded on both sides: a floor,
because the census covers method rows only and `robopianist_2023`, whose row is a benchmark, sums
five reward terms against the three its Table 2 documents; a ceiling, because eight accusations an
earlier draft of this section made were withdrawn, seven of them under adversarial review and an
eighth, `omnih2o_2024`, once writing to its authors sent someone back to the evidence, each with
its reason recorded in the accused row beside the charge. Among the 21 reorientation methods of
Table 5, seven released a repository: four disagree with their paper, one (`dreureka_2024`) ships
no cube-rotation environment at all, one (`hora_2022`) is a later generation its own README flags,
and one (`eureka_2023`) was a default-value question the same README settles.

The most consequential case is `physhoi_2023`. Its `compute_humanoid_reward` hardcodes the body
position-velocity error and both object rotation errors to zero, with the real computation
commented out beside them, and does so unconditionally rather than per dataset, while its Table 4
lists non-zero weights of 0.1 and 0.01 for those rotation terms on GRAB. The reward that produced
the paper's numbers never tracked object orientation: a method presented as tracking a 6-DoF
reference was, in the code that ran, tracking the object in position only, with body rotation and
body rotation-velocity still live. `omnigrasp_2024`, in the same file family, keeps its object
rotation term live and fails the other way, internally: `compute_pregrasp_reward_time` takes its
weights as arguments and then hardcodes them to 0.9 and 0.1.

Zeroed terms recur, and are not the same failure. A term present and zeroed is worse than a term
missing, because it survives a reader's check of the file, but only when the paper claims it.
`dexpbt_2023` sums eight components against the paper's four and multiplies a hand-delta penalty
by zero with the comment "currently disabled", a term the paper never claims, and its five named
weights are present at their stated values. `pianomime_2024`'s Table 3 states two weighted terms
while its environment sums roughly five unweighted ones, two of them inherited stubs returning
zero and a third, forearm collision, the paper never lists. `penspin_2024` ships `forceScale: 0.0`
against the disturbance force its appendix describes, which is the charge that survives. A second
half of the original charge, that the same 96-dimensional observation disables the paper's tactile
channel, is withdrawn: those dimensions are proprioception-only, consistent with the student
policy the released config runs rather than the tactile-and-point-cloud oracle, and the paper
never claims the student has tactile input. The disturbance-force charge alone is why the row
still reads medium rather than high.

Weights drift. `dextreme_2022` states an action-delta penalty of −0.25 in Table 2 and ships −0.2
and −0.01 in its two DR yamls, neither matching. `visual_dexterity_2022`'s Eq. 8 penultimate-joint
penalty is absent from the released reward file, and its two configs disagree about the fall
distance. `unidexgrasp_2023` and `dexpoint_2022` ship rewards structured differently from their
equations, and `pddm_2019`'s Baoding reward carries a −10 wrist-height term Table 2 omits.

In 13 rows the repository does not settle the question, which is this survey's limit and not an
accusation. The reward code is C++ and outside the parse in `graspxl_2024`, whose configs expose
four velocity coefficients where the paper prints two, and in `artigrasp_2023`, whose two weight
sets are the two phases of a curriculum the paper documents. `dextrack_2025` ships several
unreconciled coefficient sets and which produced its headline table cannot be identified, and
`maniptrans_2025`'s learning rate and environment count match its own config, the differing values
being a README example's override and an unused fallback. `hora_2022` is the one repository that
discloses its own gap, telling the reader to check out tag v0.0.1. Elsewhere a paper disagrees
with itself: `aloha_act_2023`'s Algorithm 1 says MSE and its Section IV.C says L1, `dp3_2024`'s
prose says the network predicts noise while its config sets `prediction_type: sample`, and
`dexmachina_2025`'s multiplicative task reward, charged to its code in an earlier draft, is
printed in the paper.

A reward table is a claim about a training run and the code is a claim about a repository. Here
the two contradict each other in nine cases, in the other 29 the released artefacts do not settle
the question, and in exactly one, `hora_2022`, the repository says so itself. Read the reward
function before the reward table, and treat a printed weight as a hypothesis about the code.

**The withdrawals, and what would close it.** This is a result about publishing practice in robot
learning more than about dexterous manipulation: the dexterous corpus is its sample, not its subject.
Nine is also a floor, since 46 method rows released nothing to check and four more are unsettled. The
first count was sixteen. An adversarial re-reading withdrew six outright, `maniptrans_2025`,
`eureka_2023`, `open_television_2024`, `dexmachina_2025`, `artigrasp_2023` and `graspxl_2024`: two
refuted by the accused repository's own README, two resting on reward code that was never in the
parse, one charging the code with structure the paper prints, one against a paper with no reward
function. A seventh, `dexpbt_2023`, was narrowed rather than dropped, its domain-randomisation half
withdrawn and its zeroed reward term left standing, so that row is still a contradiction and the
narrowing takes nothing off the count. That left ten, and ten held until the letters to the authors
were drafted. Writing to `omnih2o_2024` meant reading its accusation again before it went out, and
reading it again is what broke it: four of its five reward-weight comparisons match the paper's own
table to the digit once a systematic x1.25 curriculum factor is applied, and only the stumble weight
differs, by a factor of about a million, which reads as a typo signature in a table rather than a
policy trained on a different objective. Its hands are driven open-loop from a VR pose as well,
outside the policy and outside the reward, which made the work a poor fit for a reward census in a
dexterous-manipulation survey whatever the weight said. The charge is withdrawn and the row moves to
an internal inconsistency, which is where the count above sits it.

**The survey has now withdrawn eight accusations in total: seven of them under adversarial review,
and the eighth at the point of writing to the authors, because someone sat down to write the letter
and looked at the evidence again.** Each retraction and narrowing is recorded in its row beside the
charge: a survey that names people should carry its corrections beside its accusations, in public and
not just in the corpus. What would close the finding itself is a reward table generated from the
released config at a named commit, so a reviewer diffs two artefacts instead of reading two
documents.

# 6. Bimanual dexterous manipulation

A warning first. Fifty-three corpus method rows carry the two-hand flag, and that flag says only
that the robot has two end effectors. Thirteen of the 53 put no dexterous hand on the robot at
all. `aloha_act_2023`, `rdt1b_2024`, `egomimic_2024`, `h_rdt_2025` and `umi_2024` are parallel-jaw
throughout; `pi0_2024`, `pi05_2025`, `pistar06_2025` and `diffusion_policy_2023` name no hand and
run grippers on every embodiment; `gemini_robotics_2025` and `gemini_robotics_15_2025` report
every bimanual number on grippers and show five-fingered hands only qualitatively; and
`helix_2025` and `groot_n16_2025` name no end effector anywhere on the page. Three more run a
gripper on one embodiment and a hand on another: `ace_teleop_2024`, `dp3_2024` and
`open_television_2024`, whose Unitree H1 carries 6-DoF Inspire hands and whose Fourier GR-1
carries a 1-DoF jaw.

**The denominator for this section is 28**: the method rows whose notes place a learned
closed-loop controller on two multi-fingered hands. It is the 53 less those 16; less two static
grasp-synthesis methods, `bimangrasp_2024` and `bidexgrasp_2026`; less three systems with no
learned policy, `castro_sap_contact_2021`, `dexteleop0_2026` and `pang_global_planning_2022`; and
less four rows where no learned policy holds both hands: `omnih2o_2024`, whose fingers are mapped
open-loop from the Vision Pro and sit outside its 19-DoF policy; `okami_2024`, whose headline
pipeline is open-loop retargeting with a learned policy only in a side experiment;
`dexdeform_2023`, a skill model refined by trajectory optimisation rather than a closed-loop
controller; and `omnigrasp_2024`, a simulated human body with no bimanual task.
`dexterous_handover_2025` never enters, because its row records one hand. Benchmarks and datasets
are outside the 28 by class, `bidexhands_2022`, `bench2dex_2026` and `robopianist_2023` being
benchmarks and `rp1m_2024` and `humanoidgen_2025` datasets; they are quoted here as evidence and
never counted. Every paper below runs two multi-fingered hands unless said otherwise.

## 6.1 Coupling, roles and collision

When both hands hold the same object, the object closes a kinematic loop between them. Neither
hand can move without changing what the other must do. `bidexgrasp_2026` reports that the coupled
objective "often yields imbalanced solutions, where one hand dominates stability while the other
contributes marginally." `artigrasp_2023` reports simulation speed scaling "roughly quadratically
with the number of contacts," and trains each hand alone before pairing them.

Role asymmetry is an assumption almost everyone makes silently. `bidexhd_2024` states it outright:
"we assume the robot to be right-handed by default, i.e., the left hand handles the target object
and the right hand handles the tool," and `twisting_lids_2024` bakes the same split into its
reward, putting reference contact keypoints on the bottle base for the left fingertips and on the
lid for the right. The bias is in the data first: `taco_2024` recruited 14 right-handed subjects
and measures the right hand moving consistently faster.

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

Figure 5 sets the four architectures side by side. Every row of the 28 is assigned to exactly one
of them, read from its note.

Twenty-one of the 28 put one policy over both hands, which is three quarters of the set: the
trackers and tracking-adjacent methods `dexmachina_2025`, `dexman_2025`, `maniptrans_2025`,
`objdex_2024` and `humanplus_2024`; the reinforcement-learning tasks `dexpbt_2023`,
`twisting_lids_2024`, `eureka_2023`, `pianomime_2024` and `humanoid_sim2real_recipe_2025`; the
demonstration pipelines `bidex_teleop_2024`, `dexcap_2024`, `dexwild_2025`, `dexmimicgen_2024`,
`hato_visuotactile_2024` and `humanoid_policy_human_policy_2025`; and the generalist policies
`gr_dexter_2025`, `groot_n1_2025`, `dexora_2026`, `metis_2025` and `egoscale_2026`. In every one
of them a single network takes a concatenated two-hand observation and emits a two-hand action.
Two rows do not say which they are, `bunny_visionpro_2024` and `deximit_2026`, whose notes
describe the rig and the data pipeline but never the policy's own decomposition. The concentration
is not the outcome of a comparison that was won.

Four of the 28 give each hand its own network, and the two papers that compare the choice
disagree. `bidexhands_2022`, a benchmark row and so outside the 28, ships the MARL baselines and
finds PPO over the full observation beats HAPPO and MAPPO "in most cases," with the gap narrowing
on tasks that need both hands, because PPO "can use all observations" where MARL sees only part.
`bidexhd_2024` concludes the opposite. Its independent PPO teachers score 74.59 percent stage-two
tracking rate on trained tasks against 53.88 for a centralised policy over both observations. Both
are simulation only, on different tasks and hands, so neither settles it. `artigrasp_2023` trains
one PPO policy per hand, and `dynamic_handover_2023` and `dydexhandover_2025` use MAPPO with one
agent per arm-hand system.

One of the 28 assigns explicit leader and follower roles, and the same one is the only policy
expressed in a relative frame. `asymdex_2024` is that paper, and the only corpus paper that puts
either mechanism inside a policy. It gives the dominant hand full finger and wrist control,
restricts the facilitating hand to a 6-DoF base pose, and writes the dominant hand and the object
in a frame attached to the object the facilitating hand holds. That cuts the observation from 176
dimensions to 88 and the action from 52 to 26. It ablates the two mechanisms separately, which no
other corpus paper does. On Block in cup the full method scores 0.7701 over five seeds, against
0.1086 for relative frames without asymmetry and 0.0164 for asymmetry without them. Twist Lid
transfers zero-shot at 18 of 20 real trials. The real rig pairs a 16-DoF Allegro with a 6-DoF
Ability Hand because only one Allegro was available, so the roles are confounded with the
hardware. Two other rows use a relative quantity without giving either hand a role: `dexwild_2025`
appends the inter-hand pose to its observation, and `dexmimicgen_2024` applies one shared SE(3)
transform to both arms' source segments when generating data, which is the mechanism offline
rather than in a policy.

**What would close it.** One architecture carries three quarters of the field, and the choice behind
it has been compared twice, with opposite outcomes, and ablated once. What would close it is a single
handover task run on three architectures with the same hand and the same seeds, reporting giver and
receiver returns separately rather than one shared number.

## 6.3 Benchmarks, datasets and the shared axes

Two purpose-built bimanual dexterous suites exist in the corpus, four years apart.

`bidexhands_2022` is 20 tasks on two Shadow Hands in Isaac Gym, ordered by the infant age at which
humans acquire the skill, at 2048 environments and a reported 30,000-plus FPS. Its measurement
discipline is weaker than its coverage. It reports reward and normalised score, never a success
rate. Its only success flag in code tests the object-to-goal distance against 3 cm, which ignores
orientation and exists only in the four catching tasks. Any success rate later work attributes to
Bi-DexHands comes from that flag or its own definition.

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

**Methods on the same axes.** Table 7 carries the bimanual papers on the same columns as every other method here, and three of
those columns are worth reading together.

Real trials. `asymdex_2024` reports 20 per task, `hato_visuotactile_2024` 10 per condition,
`dexmimicgen_2024` 20 on a Fourier GR1 and `bidexgrasp_2026` 260 across 30 objects.
`maniptrans_2025` reaches real Inspire hands by open-loop replay with no trial count and no
success rate. Seven of the 28 have no real robot at all: `artigrasp_2023`, `bidexhd_2024`,
`dexmachina_2025`, `dexman_2025`, `dexpbt_2023`, `dydexhandover_2025` and `pianomime_2024`. The
two piano rows outside the denominator, `robopianist_2023` and `rp1m_2024`, are simulation-only as
well.

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
1.52 cm penetration depth. Neither number transfers, and section 5.3's re-implementation result is
the same lesson on the training side.

## 6.4 Handover, and what transfers from one hand

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
episode." There is one agent, one reward and no second policy, its row in Table 7 accordingly
records one hand, and it is one of the rows the 28 excludes. The 94 percent often attached to this
paper needs its conditions. It is Total Success, which counts "Indetermination" cases where the
simulator failed to resolve collisions and the object clipped through the giver's hand, on the
short prism, in simulation, over 100 episodes, with no real robot in the paper.

Nothing in the handover literature measures contact quality. Contact appears only as a positive
signal, a boolean per-phalange touch in `dexterous_handover_2025` and a boolean contact reward in
`dydexhandover_2025`. The two systems that do handover well sidestep the problem.
`hato_visuotactile_2024` reaches 10 of 10 on a real slippery handover by imitating teleoperation
with fingertip touch sensing and no physics model. `humanoid_sim2real_recipe_2025` stages its
reward with a discrete variable switching which hand's fingertips are scored, and still calls
handover its hardest task at 52.5 percent real success.

**What transfers from single-hand work.** The training recipe transfers intact. PPO with thousands of parallel environments, an asymmetric
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

# 7. Evaluation, and a protocol for comparison

## 7.1 Reporting practice

Of the 112 method rows in the corpus, 89 report a real-robot experiment, 22 do not and one row is
unsettled, which is 80 percent of the 111 the note settled. Among those 89, 70 state how many real
trials produced the headline number, 79 percent of them. The 89 is the denominator that belongs to
this statistic: the 22 rows with no real robot cannot state a real trial count, and counting them
as silent turns a definitional impossibility into a reporting failure. Thirty-nine rows state a
count of unseen test objects, 35 percent. Ninety-eight state how a rollout is scored, 88 percent.
Sixty-two released code and 46 did not, with four rows unsettled, 57 percent of the 108 the note
settled. Figure 6 draws these six shares, each against the denominator that belongs to it.

![fig6_reporting](figures/fig6_reporting.svg)

**These are counts of what this survey captured, not of what papers reported, and every one is a
floor.** A structured row holds a scalar. A paper that reports ten trials on each of nine tasks,
or a scoring rubric instead of a threshold, or a count spread over four tables, has nothing the
extraction can reduce to one integer, so it produces a null, and a null is then indistinguishable
from a paper that said nothing. The bias runs one way: every miss converts a reporting paper into
a silent one, and the survey's argument is that the field reports badly, so the artefact flatters
the argument. Section 5.6 makes the same disclosure about the paper/code count, subtracting the 13
disagreements that are limitations of this survey's own parsing before declaring which number to
quote, and the coverage statistics above need it more.

So the nulls were audited by hand against the notes they came from, and the numbers above are the
audited ones. Of the 34 method rows with a real robot and no trial count, 15 had the count written
in their own note. `pi0_2024` at ten trials per task, `rdt1b_2024` at 139 across seven tasks,
`umi_2024` at 260, `pistar06_2025` at 750, `gemini_robotics_2025` at twenty per task, and ten
more. That is 44 percent of the audited nulls, and it moved the headline from 55 rows to 70, from
62 percent of real-robot papers to 79 percent, and the "never says" figure from 34 of 89 down to
19. The success criterion moved further: of 33 null rows, 19 do state a criterion, so the count
rose from 79 to 98. The unseen-object count moved least, 7 recovered from 80 audited nulls, 32 to
39. The audit only counted cases where the note itself carried the number, so a count that the
note also missed is still uncounted, and 19 trial counts, 8 unseen-object evaluations whose object
count the note never gives, and 4 criteria remain genuinely unsettled. Those nulls are now a
defensible claim rather than an artefact. Every bar in Figure 6 should still be read as a lower
bound.

The remaining gap is the one that matters. Nineteen of the 89 papers with a real robot never say
how many times they ran it. A percentage with no denominator cannot be given an interval, so it
cannot be compared with anything.

Where the denominator is stated it is small, and it is not one quantity. Some stored counts are
per-cell, meaning ten trials on each task, or twenty per condition, or five per object. Others are
grand totals over every cell. The rows now record which of the two each value is, and the two
distributions are quoted separately. The 39 per-cell counts run from 5 to 100 with a median of 15
and quartiles at 10 and 20. The modal cell is 10 trials, in 16 rows, then 20, in 12. The 24 grand
totals run from 12 to 750 with a median of 110. Pooling the two gives a median of 20 and a range
of 5 to 1287, and that pooled figure is the one an earlier draft of this section quoted. It
describes nothing, because `hora_2022`'s 240 and `visual_dexterity_2022`'s 20 are experiments of
comparable size recorded on different bases. Seven further counts could not be assigned a basis at
all.

The per-cell count is the one a Wilson interval attaches to. At 20 trials a reported 60 percent
carries a 95 percent Wilson interval of 39 to 78 percent, and a reported 80 percent an interval of
58 to 92 percent. Overlapping intervals are not a test, so the point is made with one: 12 of 20
against 16 of 20 is z = 1.38, p = 0.17, and the difference is not established. Two methods
separated by 20 points at 20 trials, the larger of the two modal cell sizes, are not separated at
all.

The share of papers stating a count has risen, from 39 of the 65 rows before 2025, 60 percent, to
31 of the 47 rows from 2025 and 2026, 66 percent. The counts themselves have not. The median
stated count is 20 in 2024, 22.5 in 2025 and 20 in 2026. Before 2024 the per-year medians rest on
one to seven observations and should not be read as a trend.

The denominators also sit on different hardware. The 103 method rows that name their own hand give
78 distinct hand strings between them, and this survey applies no normalisation to those strings,
so 78 is a count of strings and not of hand designs. Matching on the string, Allegro appears in
35, Shadow in 21, Inspire in 19 and LEAP in 12. A success rate on a 16-degree-of-freedom Allegro
and a success rate on a 6-actuator Inspire hand are not measurements of the same thing.

Nor are the criteria, and the audit changed what that sentence can claim. `dexverse_2026` counts
PickCube a success when the cube is "lifted at least 0.20 m above its resetting height".
`bench2dex_2026` requires its terminal predicate to hold for a continuous dwell time of 0.5 s, to
reject transient contacts. `colosseum_2024` counts an episode successful "if the model completes
the task fully". `dextrack_2025` reports every success rate as a pair under two threshold sets,
which on GRAB gives 46.70 and 65.48 percent for the same rollouts. Of the 14 rows that still state
no criterion, ten have no success predicate at all. They report radians rotated or time-to-fall
and never define a success, which is a fact about the paper rather than a gap in this survey. And
four are unsettled by the note. What the audit found in the other 19 was mostly not a threshold:
eleven score by rubric or staged partial credit, five judge binary completion against a task
description by eye, two defer to a benchmark's own definition, and exactly one, `pistar06_2025`,
states a verbatim numeric threshold. A rubric is a milder failure than silence and a worse one
than a threshold, because it is reproducible inside a lab and not across two.

**The axes that matter.** Seven quantities dissociate in the published data, so they have to be reported separately.

**Task success.** Binary success discards the difference between near-misses and inaction.
`beyond_binary_success_2026` puts it plainly: "a policy that completes 90% of the task is clearly
better than a policy that is frozen the whole time, yet their success rates would be identically
0%". In `kress_gazit_policy_eval_2024` policy C scores 17 percent overall on the pancake task
while picking up the spatula and flipping the pancake in 23 of 23 attempts.

**Robustness to perturbation.** `colosseum_2024` measures a 30 to 50 percent success drop under
single perturbation factors and at least 75 percent under all 14 together. In `bench2dex_2026`
GR00T N1.5 leads the matched condition at 48.5 percent and falls to 19.8 percent under combined
shift, while π0.5 goes from 27.3 to 19.7 and retains the most at 72.1 percent. The ranking at the
anchor is not the ranking under shift.

**Generalisation to unseen objects.** Only 39 rows state a count and the median is 11 objects.

**Physical plausibility of the contact.** Eleven of the 96 rows whose contact handling the note
settled address it, 11 percent, with 16 rows unknown. Section 7.2 takes them apart.

**Sample and wall-clock cost.** Thirty-one of 112 rows state a parallel environment count and 18 a
simulated episode count. `robopianist_2023` is the exception, at 5 million samples per song and
roughly 5 hours per run on four Tesla K80 GPUs.

**Real-robot transfer.** Simulated rank order is not real rank order. `autoeval_2025` scores
Open-π0 on put-eggplant-in-sink at 6 of 50 in SIMPLER and 47 of 50 on the real WidowX.
`suresim_2025` states the limit directly: "the simulation-to-real gap precludes rigorous
statistical inferences about real-world outcomes from simulation results alone".

**Reproducibility.** 62 rows released code that could be parsed against the paper, and 38 of the
112 rows record a disagreement of some kind between the paper and that code. All 38 released code,
so the raw rate among code-releasing rows is 61 percent. That raw rate is not the finding, because
the 38 are not one thing. Section 5.6 classifies them: 9 contradictions, 13 limitations of this
survey's own parsing, 8 components never released, 4 version skews and 4 inconsistencies internal
to a paper. Only the contradictions are a finding about the work rather than about this survey, so
9 of 62 code-releasing rows, which is 15 percent, is the figure this section and Table 8 use.
`physhoi_2023` is the clearest of the 9. It lists a non-zero object-orientation weight for GRAB in
Table 4, and the reward function it released hard-sets that orientation error to zero, so the
reward that produced the published numbers tracked the object in position only.

## 7.2 Physical plausibility

Eleven method rows handle interpenetration in any form: three penalise it, three measure it, five
constrain it, 11 percent of the settled rows. The denominator is 96, not 112, because the
contact-handling field is null for 16 rows, and a null there means the note did not settle the
question, not that the paper ignored penetration.

That eleven is not a claim that penetration goes unmeasured in general, and reading it that way
would be wrong. Outside closed-loop control the quantity is a standard comparative column, and has
been one for years in grasp synthesis and in hand-object reconstruction. Four rows of this corpus
show the practice. `bidexgrasp_2026` prints a penetration depth beside a prior method's,
`bimangrasp_2024` fails any grasp that exceeds 1.5 mm of total penetration, `toporetarget_2026`
reports a maximum penetration and a share of frames past 2 mm against a baseline retargeter, and
`oakink_2022` scores a dataset split on penetration depth, solid intersection volume and
simulation displacement. The finding is narrower than the field and concerns learned closed-loop
control: all eleven score a pose or a reference trajectory, four of them are closed-loop policies,
and we found none that reports the measurement for rollouts of its own trained policy.

Where in the pipeline those eleven act is the reference-versus-rollout split that section 1 takes
from `zhao_dexhand_survey_2026`. A reference is a pose or a trajectory scored before execution,
and a rollout is what the trained policy actually did. What this section supplies on that axis is
a measurement method and a count, and it does not supply a threshold. The count is the eleven of
96 above, with four closed-loop policies inside it and none we found reporting a number for its
own rollouts. The method is the plausibility row of Table 8: maximum and mean penetration depth
over the evaluation rollouts, on a dense surface sample, computed by code that never entered the
reward or the termination rule. The threshold is borrowed, and section 7.4 says from where and why
it does not bind. Six of the eleven are grasp synthesisers or trajectory optimisers, namely
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

`toporetarget_2026` is the strongest case in the corpus and still stops one step short on the same
reference-versus-rollout line. It constrains penetration during retargeting with a 1 mm soft
tolerance and a 30 mm hard bound, and it reports two numbers on 25 ContactPose grasps: a maximum
penetration of 1.07 mm and 0.00 percent of frames above 2 mm, against 22.22 mm and 96 percent of
frames for its GeoRT baseline. Then a PPO controller tracks those references, and its four reward
terms and its five termination criteria govern object pose, link position, joint error and action
smoothness, never penetration. The constrained quantity is the reference, and the rollout is not
re-measured.

Definitions are not shared either. `grab_2020` estimates contact by proximity, because "contact
cannot be directly observed", with a 4.5 mm tolerance, and reports that "'Use' grasps have 3.25 ±
0.68 mm average penetration", without saying whether 3.25 mm is a maximum, a mean or a median.
`oakink_2022` supplies the fullest published vocabulary: penetration depth, solid intersection
volume and simulation displacement. Its Table 3 scores the GRAB GrabNet split at 2.53 cm
penetration depth, against GRAB's own 3.25 mm. The two differ by a factor of about eight, and
neither source states its distance function precisely enough to reconcile them, and the two are
not scored over the same grasps either, since GRAB's figure is over its own captured "use" grasps
and OakInk's is a model's output on the GrabNet split, so a difference of population and a
difference of definition are confounded in the same ratio.

The analytic tradition scored a grasp without simulating it, and `ferrari_canny_1992` and
`roa_suarez_grasp_quality_2015` are its wrench-space reference points. Neither could be obtained.
The first DOI fetch returned HTTP 202 and the second a Springer JavaScript interstitial, so both
are cited by metadata only and no definition here rests on their contents. The learned literature
has not replaced that tradition with anything it measures on its own rollouts. Penetration is a
quantity between meshes, so it needs a simulator or a mesh reconstruction, and the protocol below
treats it as a simulation-only axis.

**What would close it.** The gap is specific to learned closed-loop control rather than general, and
it is a choice rather than a capability. What would close it is a maximum and a mean penetration
depth over the evaluation rollouts, on a dense surface sample, computed by a measure the policy never
optimised.

## 7.3 Statistical practice, and a proposed protocol

`kress_gazit_policy_eval_2024` is the field's reference protocol and it prescribes process, not
numbers. Write the success criteria before the run and have someone other than their author score
the runs. Match initial conditions with image overlays. Interleave the policies blind within one
session. Report counts rather than percentages, alongside the initial conditions and the failure
modes. Use a posterior over the Bernoulli parameter instead of a point estimate. It prescribes no
minimum trial count anywhere and no frequentist confidence-interval width anywhere. Its own
example report uses 10 initial conditions with two runs each, 20 evaluations per policy, and its
worked case shows what 20 buys. Pancake success of 15 of 18 against 11 of 17, nominally 83 against
65 percent, leaves a 0.11 posterior probability that the worse policy is actually better. At 150
of 180 against 110 of 170 the same rates separate.

`lbm_careful_examination_2025` supplies the missing numbers by fiat rather than derivation: 50
rollouts per task per policy per condition on hardware, 200 in simulation, blind, with randomised
policy order inside per-initial-condition bundles. It replaces confidence intervals with
Beta-posterior violins and corrects its pairwise tests under Bonferroni, "unless otherwise noted".
Its own warning is the strongest sentence in this literature: "there is significant risk that many
robotics papers are measuring statistical noise due to insufficient statistical power".

The rest fall short of their own advice. `roboarena_2025` runs 612 double-blind pairwise
comparisons across seven institutions and 4284 rollouts, and reports no confidence intervals and
no per-policy trial counts. `colosseum_2024` evaluates 235 test sets at 25 episodes each with "one
training seed and one evaluation seed" per baseline and gives no intervals in simulation.
`autoeval_2025` runs 50 trials per policy per task and calls ±10 percent "the natural variance of
robot evaluations", without giving the formula behind the intervals it plots.

Two papers do give usable numbers. `suresim_2025` pairs real and simulated trials and de-biases
the simulation with a rectifier, saving 20 to 25 percent of hardware trials at paired correlations
of roughly 0.6 to 0.7, and nothing at all at a correlation near zero. The 25 percent figure is the
better of its two reported settings, the DP case at ρ = 0.702. Its decision rule is exact:
combining helps only when the rectifier variance is below the variance of the real evaluations.
`beyond_binary_success_2026` gives the largest saving. On the LBM rubrics its sequential test on
graded scores cuts simulated evaluation by about 70 percent and hardware by about 45 percent, 286
trials against a nominal 500, with per-task decisions landing in 12 to 36 paired trials. On
RoboArena's data a 30-point gap on continuous progress scores reaches significance in 18 trials,
while a 20-point gap on binary success needs about 80.

**A proposed protocol.** Every count below is printed by `tools/make_eval_tables.py` in its derivation mode, and each axis
is derived for the statistic that axis actually reports: a single rate takes a Wilson half-width,
a matched comparison takes McNemar, a ratio takes the standard error of the log ratio, a
correlation takes the Fisher-z interval.

Fix the width first, then read off the count. Take a 95 percent Wilson interval on a single
reported rate, at the worst case of p = 0.5. A half-width of 20 points needs 21 trials, 15 points
needs 39, 10 points needs 93 and 5 points needs 381. Ten points is the coarsest width at which a
single rate is worth printing, so the absolute-rate minimum is 93, rounded to 100. At 100 trials a
reported 80 percent has an interval of 71 to 87 percent, and a reported 50 percent has 40 to 60. A
comparison is a different question and a harder one: two rates each carrying ±10 points do not
resolve a 10-point difference between them, because the difference's standard error is larger by a
factor of √2, so the width argument sets a floor on what is worth reporting and not on what can be
compared.

For the A/B comparison the relevant calculation is power, and the design is paired. Table 8
matches initial conditions by image overlay and interleaves the two policies in one session, so
the unit is a matched pair and the count follows McNemar, which depends on the discordance rate.
The share of initial conditions on which the two policies disagree, and not on the two rates
alone. To separate 50 from 70 percent at α = 0.05 with 80 percent power: 37 pairs per arm at a
discordance of 0.2, 57 at 0.3, 77 at 0.4 and 96 at 0.5. The protocol assumes 0.3 and asks for 57,
and states the sensitivity rather than hiding it, because 0.5 is the discordance the same two
rates produce when the pairing buys nothing, and at that value the paired count returns to the 93
per arm an unpaired test would need. The saving from pairing is real but smaller than the pair
counts suggest, since a pair costs two rollouts: 57 pairs is 114 rollouts against 186. An earlier
version of this section quoted 93, 169 and 387 per arm for gaps of 20, 15 and 10 points, which are
correct for independent arms and are the wrong test for this protocol. That 93 was also the same
integer as the half-width calculation in the paragraph above, which is a coincidence of the
worst-case arithmetic and not a second derivation of the same number.

One hundred is a cap and not a bill, because on a graded score a sequential test reached its
decision in 12 to 36 paired hardware trials in `beyond_binary_success_2026`. At 30 rollouts a
continuous score already carries a half-width of ±0.36 standard deviations, which is why a graded
score can stop where a binary one cannot. A cell that stops early does not report a Wilson
interval. Optional stopping breaks the coverage of a fixed-n interval, which is the reason
`beyond_binary_success_2026` and `suresim_2025` use anytime-valid betting intervals rather than
Wilson, so Table 8 asks a cell run to a fixed 100 for a Wilson interval and a cell stopped early
for a confidence sequence, and never for both. Intervals are also marginal rather than
simultaneous. Table 8 has seven axes and Table 9 twelve methods. At 84 independent 95 percent
intervals, four excursions are expected by construction, so a paper comparing k policies on m
tasks corrects its k(k−1)/2 pairwise tests to a global 95 percent level, as
`lbm_careful_examination_2025` does, or says its intervals are not simultaneous.

Simulation is cheap, so simulated cells take 200 episodes, giving a 6.9-point half-width.
Perturbation axes are screened rather than certified, and 40 per axis buys a 15-point half-width
on each axis's own absolute rate, which is enough to rank the axes and pick the two worst for
hardware. It is not enough for the ratio to the anchor that an earlier draft asked each cell to
report. At 40 trials in each arm, a fall from a 0.50 anchor to 0.30 is a ratio of 0.60 with a 95
percent interval of 0.34 to 1.06, which contains 1: at the screening count you cannot establish
that the perturbation hurt at all. Certifying that same drop takes 101 per arm by the log-ratio
standard error, so Table 8 now asks for absolute rates with their own intervals at 40, reports the
ratio without an interval, and prescribes 101 before any claim that a named axis hurt.

For unseen objects the resampling unit is the object and not the trial, so 20 objects at 5 trials
each gives 100 trials and an object-level half-width near 20 points. That 20 points is the Wilson
width at n = 20 and it treats each object's outcome as a single Bernoulli draw, which the five
within-object trials are not. It is the right order of magnitude and the assumption belongs in the
cell. A 10-point claim about an object distribution needs about 93 objects. Seven of the 39 rows
that state an unseen count reach that: 225 in `bimangrasp_2024`, 241 in `resdex_2024` and
`unidexgrasp_2023`, 360 in `dexgraspvla_2025`, 500 in `dexmv_2021`, 2029 in `clutterdexgrasp_2025`
and 503409 in `graspxl_2024`. For a continuous score the half-width is 1.96 standard deviations
over the square root of the count, so 100 rollouts give ±0.20 standard deviations, and the unit is
the rollout because frames within one are correlated.

The transfer axis is the one where 100 is least defensible. On 100 matched pairs a measured
correlation of 0.70 carries a Fisher-z interval of 0.58 to 0.79, a half-width of about 0.10 that
130 pairs would be needed to guarantee. That is enough to establish that a simulator tracks
reality at all, and it is not enough to separate `suresim_2025`'s useful regime from its marginal
one, since those differ by about 0.11 in correlation. Both limits come within 0.05 of the estimate
only at about 457 pairs. Table 8 states which of the two decisions each count supports rather than
leaving a reader to assume the larger one.

### Table 8. The proposed evaluation protocol

| axis | what is measured | how | minimum trial count | reported alongside it | why |
|---|---|---|---|---|---|
| Task success | fraction of episodes meeting a criterion, and a graded rubric score in [0,1] over equally weighted milestones | criterion written before the run by the designer and scored by someone else; terminal predicate held for a 0.5 s dwell; initial conditions matched by image overlay; policies interleaved blind in one session | 100 real and 200 sim per policy per task per condition for an absolute rate at a 10-point interval; a comparison alone needs 57 matched pairs per arm (McNemar, 50 against 70 percent, discordance 0.3) | raw counts, the criterion verbatim, the rubric, the initial-condition protocol, and an interval whose kind is named: Wilson for a cell run to a fixed n, an anytime-valid confidence sequence (WSR, as in `beyond_binary_success_2026`) for a cell stopped early by a sequential test, because a Wilson interval computed at a data-dependent stopping time is not a 95 percent interval. Intervals are marginal, not simultaneous: a paper comparing k policies corrects its k(k&minus;1)/2 pairwise tests to a global 95 percent level, as `lbm_careful_examination_2025` does, or says it has not | a rate without a denominator and an interval cannot be compared; the rubric separates a near-miss from inaction; the design is paired, so the count that governs it is paired |
| Robustness | success under each perturbation axis as an absolute rate; the ratio to the unperturbed anchor is reported descriptively and is not tested at the screening count | axes that must not change the action and axes that must are scored separately; ranges stated; anchor replayed exactly | 40 per axis per policy in sim to rank the axes; 101 per axis and 101 at the anchor before any claim that a named axis hurt | both absolute rates with their Wilson intervals, the ratio without an interval unless the certifying count was run, the axis ranges, and which split each axis is in | the ranking at the anchor is not the ranking under shift; at 40 per arm a fall from 0.50 to 0.30 is a ratio of 0.60 with a 95 percent interval of 0.34 to 1.06, which contains 1 |
| Unseen objects | mean over held-out objects of per-object success | objects drawn from a stated distribution disjoint from training; bootstrap over objects, not trials | 20 objects at 5 trials for a screening claim; 93 objects for a 10-point claim | the object list, per-object rates, the bootstrap interval, the object-count caveat, and the within-object trial count, since the 93 is a Wilson width that treats one object as one Bernoulli draw | the resampling unit is the object, so trial counts overstate the precision |
| Physical plausibility | maximum and mean hand-object penetration depth per rollout, and the fraction of frames above 2 mm | dense surface sample against the object mesh or SDF, computed on the policy's own rollouts by code that never entered the reward or the termination rule | 100 rollouts, simulation only | interval over rollouts, sample density, threshold, solver depenetration settings, and at least one rendered rollout | a measure the policy optimised is not evidence about the policy |
| Sample and wall-clock cost | environment steps and wall-clock to the checkpoint that produced the headline number | counted to that checkpoint, not to the end of training; GPU model and count stated | 3 training seeds | the range over seeds, and the statement that 3 seeds is a range and not an interval | training variance is not rollout variance and the two are routinely conflated |
| Real-robot transfer | paired real and simulated outcomes on matched initial conditions, their correlation, and the rectifier variance against the variance of the real evaluation | the same 100 initial conditions run in both; correlation on the pairs; variance ratio bootstrapped over the same pairs | the 100 real trials paired to 100 sim, which fixes the correlation to about &plusmn;0.10; about 457 pairs for a claim that separates two correlations 0.1 apart | the correlation with its Fisher-z interval, the variance ratio with its bootstrap interval, and which of the two decisions the count supports | a simulator earns a real-world claim only through its measured paired correlation; at 100 pairs &rho;&#770; = 0.70 carries 0.58 to 0.79, enough to say a simulator tracks reality at all and not enough to separate `suresim_2025`'s 0.70 regime from its 0.59 one |
| Reproducibility | code, checkpoints, and the exact config that produced the headline run | diff the paper's stated objective against the released config and name the file and line of every disagreement | not a trial count | the named file and line for each disagreement, or an explicit statement that none was found | 16 of the 62 code-releasing method rows carry a true contradiction between the paper's stated objective and the released code, and 38 carry a recorded disagreement of any kind (&sect;5.8) |


## 7.4 The results matrix, and what filling it would cost

The rows are the 12 most-mentioned dexterous-hand policy methods in the corpus, and the rule is
the one the table's generator implements, stated here in the same words. A candidate is a method
row that names a hand; the hand string must not contain "parallel" or "gripper"; it must carry at
least one paradigm tag that produces a closed-loop policy and must not be a teleoperation system,
because an interface is scored on latency and operator effort rather than on a policy's success
rate. And its name must be at least four characters, so that a short string does not match
everything. Candidates are then scored by the number of other corpus papers whose parsed text
contains the name, and the top 12 by count, ties broken by key, are the rows.

Two corrections changed that ranking. The match is on a whole word. Under the bare substring test
an earlier version used, "UniDex" matched inside "UniDexGrasp" and "UniDexGrasp++", and
`unidex_2026`. A 2026 paper. Sat sixth in a ranking over a corpus written mostly before it, on 34
mentions that belonged to a different work. As a whole word it has 3 and it is not in the table.
And the interface rule is now applied to every row that carries the tag rather than only to rows
that carry nothing else, which drops `anyteleop_2023` at 34 mentions, `dime_2022` at 28 and
`holo_dex_2022` at 23, along with `dexpilot_2020`, which the earlier prose already excluded by
hand. The mention counts are printed under the table so a reader can audit them.

The ranking is not one quantity even so. A method's name is taken from the first line of its note,
which yields an acronym for some works and a full title for others, and a title is matched mostly
inside reference lists while an acronym is matched in running text. Those have different base
rates, so the table marks which kind each row was matched on and the two kinds are not comparable
with each other. Mention counts are counts of mentions and not of use, as the method appendix
records.

Every cell is empty. This survey re-ran nothing, and no cell can be filled at the denominator
Table 8 asks for. `dextreme_2022` comes closest and is the reason the claim is stated that
narrowly: it reports a criterion, a trial count and an interval. Object orientation within 0.4 rad
of target, 27.8 ± 19.0 average consecutive successes with the ± a 90 percent confidence interval.
On 10 trials. Table 7 is not a counter-example either, though it looks like one: it carries
trial-count, unseen-object, penetration and code-release columns for all 112 method rows,
including all 12 of these. Table 7 records what each method reported. Table 9 asks for what Table
8 defines. A value with an interval, a stated denominator and a criterion written before the run.
And none of Table 7's values meets that. The first row of Table 9 is a worked example so that the
format of a cell is unambiguous. Every number in it is fabricated and labelled as such.

### Table 9. The matrix, for someone else to fill

| method | task success (rate &plusmn; Wilson 95, n) | robustness (per-axis rate &plusmn; Wilson 95, n; ratio to anchor) | unseen objects (mean per-object rate, bootstrap 95, k objects) | plausibility (max / mean mm, frac frames > 2 mm) | cost (env steps, GPU-h, 3-seed range) | transfer (&rho; [lo, hi], rectifier var / real var) | reproducibility (file:line of each disagreement, or none) |
|---|---|---|---|---|---|---|---|
| *worked example &mdash; every number fabricated* | 0.72 &plusmn; 0.09 (100) | lighting 0.41 &plusmn; 0.15 (40), ratio 0.57; anchor 0.72 &plusmn; 0.09 (100) | 0.55, [0.41, 0.68], 20 objects | 3.1 / 0.8 mm, 0.12 | 1.2e9 steps, 46 GPU-h, 0.68&ndash;0.74 | 0.61 [0.47, 0.72], 0.43 | `cfg/train.yaml:88` orient weight 0.0 vs paper 0.5 |
| `openai_dexterity_2018`&#10035; | | | | | | | |
| `dexmv_2021` | | | | | | | |
| `dapg_2017`&#10035; | | | | | | | |
| `dextreme_2022` | | | | | | | |
| `dexcap_2024` | | | | | | | |
| `hora_2022`&#10035; | | | | | | | |
| `visual_dexterity_2022`&#10035; | | | | | | | |
| `rotating_without_seeing_2023`&#10035; | | | | | | | |
| `unidexgrasp_2023` | | | | | | | |
| `pddm_2019`&#10035; | | | | | | | |
| `hato_visuotactile_2024`&#10035; | | | | | | | |
| `dexpoint_2022` | | | | | | | |

*12 rows, 84 cells, all 84 empty; the first row is a worked example and every number in it is fabricated. Rows are the 12 most-mentioned dexterous-hand policy methods in the corpus, by the rule in §7.4, scored on whole-word matches over `papers/md`: `openai_dexterity_2018` 64; `dexmv_2021` 50; `dapg_2017` 49; `dextreme_2022` 44; `dexcap_2024` 40; `hora_2022` 34; `visual_dexterity_2022` 32; `rotating_without_seeing_2023` 27; `unidexgrasp_2023` 27; `pddm_2019` 25; `hato_visuotactile_2024` 23; `dexpoint_2022` 22. Mention counts are counts of mentions, not of use. &#10035; marks a work matched on its title rather than a short name; a title is matched mostly inside reference lists and a short name in running text, so the two kinds of count are not comparable with each other.*


**What would have to be true.** The bill comes first. Per policy and per task the protocol asks for 57 matched trials on the
anchor set, which is the paired count from §7.3, and 100 on the unseen-object set, at 20 objects
and 5 trials each, with robustness and plausibility absorbed by simulation. A two-policy
comparison on three tasks is then 342 real rollouts on the matched set and 600 on the
unseen-object set, 942 in all, and at one minute per rollout including the reset that is about 16
hours of robot time, before failed resets, repairs and scoring. The same bill computed from the
independent-arm count, which an earlier draft used, was 1200 rollouts and 20 hours. The pairing
removes about a fifth of it rather than the four fifths the pair counts suggest, because a pair is
two rollouts and only the anchor set is paired. `autoeval_2025` ran about 850 episodes in 24 hours
on a WidowX with three human interventions, and had to pause 20 minutes every 6 hours once the
motors overheated. A tendon-driven multi-finger hand is more fragile, so 16 hours of rollouts is
most of a week of calendar time.

That bill is large but not unprecedented. `autoeval_2025` records that evaluating OpenVLA against
its baselines took more than 2500 rollouts and more than 100 hours of human labour across three
institutions, and `lbm_careful_examination_2025` analysed about 1800 real rollouts across nine
hardware stations. What is unprecedented is paying it for a single dexterous-hand paper, where the
modal per-cell count is 10 trials and the median per-cell count 15, and where the median stated
count has been 20 or 22.5 in each of the last three years.

Four things would have to change. Reviewers would have to reward 57 matched trials on one task
over 20 unmatched trials on five, and nothing in the corpus suggests that is happening. The loop
would have to be automated, and `autoeval_2025` shows it is buildable for a gripper at one to
three hours of setup, while stating that it supports binary success only and no robustness axes.
Somebody would have to run the penetration measure on their own rollouts, which is a choice rather
than a capability: section 4.2 shows the depth is computable from the poses and the meshes in a
few lines of Warp, and IsaacGymEnvs already ships a task that does it every step. An earlier draft
of this section made the engine the barrier, and that claim is withdrawn, because the released
code refutes it. And the comparison would have to be sequential, because the savings in
`beyond_binary_success_2026` are the only reason 100 is a cap rather than a cost.

Four limits apply to the proposal itself. This survey re-ran no method, so every count in Table 8
is derived from an interval width, a power calculation or another paper's measurement, and Table 9
is empty because we filled no cell. The counts are worst-case at p = 0.5, so a method near 90
percent needs fewer trials for the same width and a method near 50 percent needs all 100, and the
paired count additionally rests on an assumed discordance of 0.3, which no paper in this corpus
reports. The perturbation axes are borrowed from `colosseum_2024` and `simpler_2024`, which run
parallel-jaw grippers on rigid objects, where `simpler_2024` found physical parameters moved
success rates by at most 15 percent. That is the sensitivity expected to grow with multi-finger
contact, and nobody has measured it. The 2 mm penetration threshold is taken from
`toporetarget_2026` with no independent justification, and the captured human grasps in
`grab_2020` sit above it at 3.25 mm, which makes 2 mm a simulator convention rather than a
physical bound. So the three things this survey adds to the reference-versus-rollout axis are a
count, a measurement method and a protocol slot for them, and a threshold is not among them. It is
borrowed from one paper and reported as borrowed, and it will stay a convention until somebody
measures penetration on rollouts across hands and engines and finds a value that separates
behaviour a physicist would accept from behaviour they would not.

**The methodology literature has no dexterous hand in it.** Seven corpus rows are evaluation
protocols, a small denominator, and not one of them uses a dexterous hand: `suresim_2025` runs a
parallel-jaw gripper and the other six state no hand. Everything proposed above is therefore
assembled from work on grippers and on whole-arm tasks. What would close that, and close it cheaply,
is to run the Table 8 protocol once, on one in-hand reorientation task with one 16-DoF hand, and
release the rollouts as the first row of Table 9.

# 8. Gaps

Seven claims survive the corpus. Each is one sentence here, with the section that carries its
evidence and the experiment that would close it. Nothing is argued in this list: the denominator, the
evidence and the prescription sit in the section named, at the end of it, so that a finding and its
consequence are read together and stated once.

1. Nine of the 62 method rows that released parseable code contradict it, in the sense that the paper
   states one value or one term and the shipped code demonstrably states another, and eight further
   accusations have been withdrawn since the first draft of that census (section 5.6, Appendix C).

2. No closed-loop policy in the corpus reports interpenetration for the rollouts of its own trained
   policy, and all eleven rows that handle penetration at all sit on the reference side of the
   reference-versus-rollout split (section 7.2, and the contact-handling bar of Figure 6).

3. The evaluation-methodology literature the protocol of section 7.3 is assembled from contains no
   dexterous hand at all: of its seven corpus rows, one runs a parallel-jaw gripper and the other six
   state no hand (section 7.4, Table 8).

4. The generalist and vision-language-action policies that do evaluate on a multi-fingered hand run
   it at a median of 6 actuated degrees of freedom, against 16 across the reinforcement-learning rows
   that state a count, and the two rows that reach the larger band on paper never say whether the
   hand was in the evaluation (section 5.4).

5. Eight hands that can be bought today or built from published designs take zero method rows between
   them, while the corpus's own experiments concentrate on four designs (section 3.4, Figure 2).

6. Twenty-one of the 28 rows that put a learned closed-loop controller on two multi-fingered hands run
   one policy over a concatenated two-hand observation, a choice that has been compared twice with
   opposite outcomes and ablated once (section 6.2, Figure 5).

7. Human data does not port across hands and the map is usually unstated: 33 of the 53 method rows
   that use human data never say how the human motion reached the robot hand (section 5.3, Table 6).

Six of the seven are gaps in the literature. The first is a result about publishing practice, and
this survey's own corrections to it are printed beside it in section 5.6 rather than kept in the
repository.

# 9. Conclusion

The binding constraint on this field is not ideas. It is verification. Sixty-two method papers
released code that could be read against the paper, 38 of those record a discrepancy, and nine are
contradictions where the shipped code states a different objective from the published one. The
first count was sixteen. An adversarial re-reading withdrew six of them outright and narrowed a
seventh, `dexpbt_2023`, to the half that still stands, and an eighth was withdrawn later still,
when writing to `omnih2o_2024`'s authors sent someone back to its evidence and the reward-weight
discrepancy it had rested on turned out to be a typo signature in the paper's own table, not a
different trained objective. Each withdrawal is recorded in the row beside the charge. Nine is a
floor, because forty-six method rows released nothing to check. A reward table in a paper is a
claim about a document, not about a run. `physhoi_2023` is the case to remember, because the term
its table weights at 0.1 is set to zero in the code, and its own success criterion could not have
detected that.

The quantity most specific to dexterous manipulation is the one closed-loop policies do not
record. Contact is what separates a hand from a gripper. Eleven of the 96 method rows whose notes
settle the question address interpenetration at all, only four inside a closed-loop policy, and we
found not one that reports a penetration number for its own policy's rollouts. Grasp synthesis and
hand-object reconstruction have reported penetration comparatively for years, so what is missing
is the measurement of a trained policy's own behaviour. The obstacle is not the engines.
IsaacGymEnvs ships a task that computes a per-environment maximum interpenetration depth against
meshes and gates the policy update on a 1 mm threshold, and `tactile_genesis_2026` offers
penetration depth on Genesis geometry as a sensor. The tooling sits in the field's own benchmark
repository and the number is still not reported. `dextrack_2025` has the formula and points it at
its inputs.

Hardware and software have come apart, on a narrower claim than the hand count first suggests.
Tables 2 and 3 hold 33 hands and 19 appear in no method row. 11 of those 19 are neither sold nor
open and appear in none for that reason, which leaves 8 hands that can be bought today or built
from published designs and that take zero method rows between them. Eight of the fourteen
generalist policies that settle the question do evaluate on a dexterous hand, at a median of 6
degrees of freedom against 16 across the reinforcement-learning rows.

What this survey cannot establish is which method is better than which. It re-runs nothing, and
Section 7 argues that the published numbers do not compare. Six works are cited by metadata only,
and a seventh, Ma and Dollar 2011, is on disk but unread; no claim rests on any of them. Every
coverage statistic here counts what this survey's extraction captured rather than what the
literature reported. Each is a floor and not a rate, because every miss converts a reporting paper
into a silent one.

Three things to do next week, cheapest first.

If you are publishing, generate the reward table from the config that trained the reported run,
print it, and cite the commit. State the trial count, state the success predicate, and release the
per-trial outcomes. None of that needs a GPU.

If you are running experiments, measure penetration depth over your evaluation rollouts on a dense
surface sample, and never let that measure become a reward. `toporetarget_2026` shows what the
number looks like when someone takes it seriously, and what the widely used retargeters look like
when nobody does.

If you are choosing hardware, the corpus names four hands and no more. The Allegro carries 35
method rows, the Shadow 21, the Inspire 19 and LEAP 12, and every other hand in Tables 2 and 3
carries eight rows or fewer. An announced hand has no URDF, no datasheet that can be checked, and
no paper in this corpus that used it.


---

## Appendix A. Method

The survey is written from a corpus that lives on disk. No claim about a paper is made from
memory. Each claim traces to a note, each note to a parsed markdown file, and each markdown file
to a PDF or repository with a recorded hash or commit.

## Selection
Six topic-specific bibliographies were assembled in parallel (simulators and physics, hands and
vendors, reinforcement learning, imitation and human data, bimanual, benchmarks and evaluation),
seeded with the canonical works in each area and extended by search up to 2026-09-17. Every
arXiv identifier was checked by fetching the abstract page and matching the title, and entries
that could not be checked that way are marked. The six lists were merged with deduplication on arXiv
identifier and normalised title, giving 221 entries.

Seven further bibliography entries are not part of that corpus and are not counted anywhere in this
survey. They are the prior audits and case studies section 1 positions this survey against, they
carry the topic `related` in `corpus/bib_related.json`, and none of them carries a structured row.
No source for them was parsed either, so each is quoted only from its abstract and its stated
method.

## Acquisition
PDFs were downloaded from arXiv or, for work without a preprint, from the publisher or vendor
page recorded in the bibliography. Vendor pages for hands without any paper were fetched as HTML
and converted to markdown, so that a specification quoted in this survey is quoted from a stored
copy of the page and dated. Repositories were shallow-cloned and parsed, then deleted. What
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
"not stated", and nothing was inferred from the reviewer's prior knowledge of the work. For method
papers the reward or loss was quoted from the paper and, separately, from the released code, so
that disagreements between the two are visible rather than smoothed over. Those disagreements
turned out to be common enough to become a finding in their own right.

## Sources that could not be obtained
Six works are cited by metadata only and no claim in this survey rests on their contents. Five
are behind publisher paywalls with no author-hosted copy found on 2026-09-18: Okamura et al.
2000, Bicchi 2000 (IEEE T-RO), Piazza et al. 2019, Roa and Suarez 2015, and Butterfass et al.
2001 on DLR-Hand II. The sixth is Hwangbo et al. 2018 on RaiSim, whose hosted PDF returned no
body. The freely circulating PDF often taken for Bicchi 2000 is a different work, a book chapter,
and is listed separately.

Ma and Dollar 2011 is a seventh case with a different cause. The fetch that failed when its note
was written succeeded on 2026-09-18, so a seven-page PDF and its hash are in the manifest, but no
note has been read from it. It is cited by metadata only for that reason and not because the
source is unavailable.

Three of the 221 bibliography entries carry no structured row. Two are the paywalled
Bicchi 2000 and DLR-Hand II entries. The third is `bicchi_grasping_chapter_2001`, which was read
into a note and quoted throughout but is a book chapter rather than a work with an embodiment, a
method or a result to record in a row.

## What this method cannot do
Mention counts over the corpus are counts of mentions, not of use: a related-work sentence
counts the same as an experiment. Vendor specifications are manufacturer claims and are labelled
as such throughout, and where a page has since gone offline the note says so. The corpus is
large but not exhaustive, and selection by search favours work that is indexed, in English, and
posted as a preprint. It also favours recent work. Of the 221 bibliography entries, 138 are dated
2024 or later and 16 predate 2018, so this is a corpus of the learned era and any claim here
about a trend over time is a claim about 2022 onward.

Every coverage statistic in this survey measures what this survey's extraction captured, not what
the literature reported. A structured row holds a scalar. A paper that reports a per-task count,
a rubric, or a total spread across several tables produces a null, and a null is then counted as
silence. The bias runs one way. Every miss converts a reporting paper into a silent one, so the
field is made to look worse at reporting than it is. The size of the effect was measured on the
statistic the survey leads with. Of the 34 method rows that had a real robot and no recorded
trial count, 15 carried a count in plain text in their own note, dropped because the paper
reports it per task and the field takes a single integer. Those 15 have since been re-extracted,
which moved the stated-trial-count row from 55 to 70. The success criterion and the unseen-object
count were audited the same way, rising from 79 to 98 and from 32 to 39. The same mechanism
reaches the penetration, code-release and failure-mode fields, none of which has been audited that
way. Read every coverage statistic in this survey as a floor rather than as a rate, and read the
bars in Figure 6 the same way.


---

## Appendix B. The full hand table with its sources

Table 2 and Table 3 split these rows by whether the hand can be bought, and truncate their cells to stay readable. This appendix prints every hand row once and at full width. Nothing here is a measurement by this survey. Every specification is a manufacturer claim, a figure in a paper, or a figure in a press article, and the `source quality` column in B.2 says which. Cells reproduce the text stored in the row, with the source's own punctuation and wording.

### B.1 Specifications as the source states them

| hand | maker | DoF | act. DoF | actuation | weight g | tip force N | payload | tactile | control rate | price USD | BOM USD | open HW | licence | sim model | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `agibot_omnihand_2025` |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| `onex_neo_hand_2026` | 1X Technologies | 25 | 25 | quasi-direct-drive tendons via the '1X Tendon Drive' at low gear ratios (~5:1-15:1); motors in the forearm, tendons pulled through the wrist |   | 45 |   | high-resolution tactile sensing across fingertips and finger surfaces (normal force, contact location, shear); sensor count/technology not stated | not stated |   |   | no |   |   | announced |
| `leap_hand_v2_adv_2025` | Kenneth Shaw, Deepak Pathak, Carnegie Mellon University | 21 | 17 | tendon (PIP/DIP coupled by a single tendon per finger); motor type not stated |   |   |   | none mentioned | not stated | 3000 | 3000 | yes |   | URDF, loaded into PyBullet by the released teleoperation node | announced |
| `paxini_dexh13_2024` | PaXini Tech |   |   |   |   |   |   | 1,140 ITPU multidimensional tactile processing units (press-release claim; unclear if PX-6AX-GEN3 sensor family) |   |   |   |   |   |   | announced |
| `clone_robotics_hand_2024` | Clone Robotics | 27 |   | hydraulic artificial muscle ('Myofiber' — small water-filled tubes that contract when pressurized), carbon-fiber bones and ligament-style tethers, driven by a 500 W water pump and 36 electro-hydraulic valves; each Myofiber generates up to 1 kg grip force, survived 650,000 test cycles | <910 |   |   | pressure pads in the palm detect grip firmness (count not given); 70 inertial sensors track angle/speed (proprioception, not tactile) |   |   |   | no |   |   | internal-only |
| `sanctuary_phoenix_hand_2024` | Sanctuary AI (Sanctuary Cognitive Systems Corporation) | 21 |   | hydraulic, 'unique miniaturized hydraulic valves' |   |   |   | not in the press release text; sidebar-only headlines mention new touch/tactile sensors as a separate later announcement, not confirmed as part of this hand |   |   |   | no |   |   | internal-only |
| `bidexhand_2025` | Zhengyang Kris Weng, Center for Robotics and Biosystems, Northwestern University | 21 | 16 | cable-driven, N-configuration tendon routing (FeeTech servos, endless-loop antagonistic pull-pull); thumb CMC flexion driven via a 4-bar linkage instead of a direct tendon |   | 2.14 | 4.54 kg (10 lb) lifted | none mentioned | serial to an onboard ESP32, ROS 2 position control; rate not stated |   |   | yes | MIT (code, per README); CAD/hardware licence unconfirmed (bib's claimed CC BY-NC-SA is not verified in the parsed README or file tree) | URDF, consumed by the ROS 2 and MoveIt stack; no physics simulator | open-source |
| `ruka_v2_2026` | Xinqi (Lucas) Liu, Ruoxi Hu, Alejandro Ojeda Olarte, Zhuoran Chen, Kenny Ma, Charles Cheng Ji, Lerrel Pinto, Raunaq Bhirangi, Irmak Guzey, New York University and NYU Shanghai | 20 | 16 | tendon-driven, forearm-mounted actuators; decoupled parallel 2-DoF wrist via a passive spherical ball joint; single-tendon-plus-spring abduction/adduction |   |   |   | optional e-flesh fingertips (magnetic touch-sensing form factor); not part of the base design | Dynamixel over USB serial; no rate stated | 1500 | 1500 | yes |   | MuJoCo XML in the shared v1 repo; not confirmed to carry the v2 wrist | open-source |
| `orca_hand_2025` | Clemens C. Christoph, Maximilian Eberlein, Filippos Katsimalis, Arturo Roberti, Aristotelis Sympetheros, Michel R. Vogt, Davide Liconti, Chenyu Yang, Barnabas Gavin Cangan, Ronan J. Hinchet, Robert K. Katzschmann, Soft Robotics Lab, ETH Zurich | 17 | 17 | tendon-driven (antagonistic fishing-line tendon pairs per joint); wrist uses a GT2 timing belt drive | 1200 |   | 10.5 kg on all four fingers and 2 kg on the index finger alone, both at a fixed 600 mA motor current | yes: FSR-based binary tactile sensing on all 5 fingertips (RP-C7.6-ST), absolute detection threshold as low as 0.05 N | serial to Dynamixel or Feetech motors; rate not stated |   |   | yes |   | URDF-derived kinematic constants only; no URDF or MJCF file in the released tree | open-source |
| `leap_hand_2023` | Kenneth Shaw, Ananye Agarwal, Deepak Pathak, Carnegie Mellon University | 16 | 16 | direct-drive (Dynamixel servos, e.g. XC330-M288), joint velocity ~8 rad/s | 595 | 19.5 |   | none (future work only: 'we plan to develop and integrate LEAP Hand with low-cost touch sensors') | up to 500 Hz querying over USB serial; the paper's own sim-to-real policy runs at 20 Hz | 2000 | 2000 | yes | Code: MIT License; CAD: CC BY-NC-SA (non-commercial use with attribution) | URDF claimed in the paper; the released LEAP_Hand_API repo contains no URDF, xacro or MJCF | open-source |
| `ruka_2025` | Anya Zorin, Irmak Guzey, Billy Yan, Aadhithya Iyer, Lisa Kondrich, Nikhil X. Bhattasali, Lerrel Pinto, New York University | 15 | 11 | tendon-driven (11 Dynamixel actuators in the forearm: XM430-W210T for the thumb, XL330-M288-T for the other fingers) |   | 2.74 | 6.0 kg: weight added to a curled cloth-bag grip until joint-angle error exceeds 15 degrees, best of three trials | none (stated limitation: 'lacks tactile sensing') | Dynamixel over a USB-to-serial bridge; rate not stated, data collection ran at 15 Hz | 1300 | 1300 | yes |   | MJCF | open-source |
| `dexhand_open_source_2023` | Rob Knight, The Robot Studio (design); electronics/firmware/ROS 2 by Trent Shumay, IoT Design Shop |   |   | tendon (fishing line, Sufix 832 80lb / 0.8mm kiteline); Emax ES3301/ES3302/ES3351/ES3352 micro-servos for fingers, Feetech SCS2332 or PWM servos for the wrist |   |   |   | none mentioned | Arduino SCServo or SBUS firmware, BLE; rate not stated | 300 | 300 | yes | CC BY-NC-SA 4.0 (README); Onshape CAD freely available | URDF, in the IoT Design Shop ROS 2 packages | open-source |
| `ilda_hand_2021` | Ajou University, Korea Institute of Machinery & Materials, Korea University | 20 | 15 | linkage-driven, direct linear drive (3 Maxon DCX8M motors per finger with GPX8 16:1 gearboxes driving ball screws via parallel+serial four-bar linkages) | 1100 | 34 | 18 kg | 6-axis F/T sensor per fingertip (5 total), force resolution 62 mN, range +/-35 N; not a distributed taxel skin | CAN to a desktop; loop rate not stated |   |   | no |   |   | prototype |
| `pisa_iit_softhand_2014` | Centro E. Piaggio, University of Pisa and IIT (Catalano, Grioli, Farnioli, Serio, Piazza, Bicchi) | 19 | 1 | tendon-driven adaptive synergy, single motor via differential gears (6 W Maxon RE-max21, 84:1 reduction) |   |   | holding force about 20 N along z and holding torque 2 N m, 28 N and 3.5 N m with a stronger motor | none (motor encoder only; a padded work glove supplied contact compliance during experiments) | not stated |   |   | no |   | URDF and Gazebo models in the ROS repo (BSD 3-Clause) | prototype |
| `faive_hand_2023` | Yasunori Toshimitsu, Benedek Forrai, Barnabas Gavin Cangan, Ulrich Steger, Manuel Knecht, Stefan Weirich, Robert K. Katzschmann, Soft Robotics Lab, ETH Zurich | 16 | 11 | tendon-driven, rolling-contact joints (16 Dynamixel XC330-T288-T servos, 6 antagonistic pairs) | 1100 |   | 10 kg, whole-hand downward power grasp on a dumbbell | none on the physical hand; a simulated 'fingertip force' (15-dim, critic-only/privileged) exists only in the RL training observation, not real tactile hardware | Dynamixel over serial; joint angles estimated from tendon length by EKF; rate not stated |   |   |   |   | MJCF, used directly by the released Isaac Gym training repo | prototype |
| `boston_dynamics_atlas_hand_2026` | Boston Dynamics |   |   | electric (robot is fully electric); specific hand mechanism not stated |   |   |   | tactile sensing in the fingers and palms, confirmed present; type and count not stated |   |   |   | no |   |   | prototype |
| `daxo_muscle_v0_2025` | Daxo Robotics |   |   | ultra-redundant tendon-driven; compliant structure with no rigid joints, flexible materials and tendon routing | 750 |   |   |   |   |   |   |   |   |   | prototype |
| `figure_03_hand_2025` | Figure AI |   |   |   |   |   |   | not stated on page for the hand itself; palm cameras in each hand are vision, not tactile |   |   |   | no |   |   | prototype |
| `tesla_optimus_hand_2025` | Tesla |   |   | V3: tendon-driven from forearm actuators, three tendons per finger through a crosstalk-managing wrist. Gen 2: in-hand actuators/sensors (unlocated in the article). |   |   |   | Gen 2: tactile sensing on all fingers, demonstrated matching contact location and force in an egg-pickup video; type/count not stated. V3: not stated. |   |   |   | no |   |   | prototype |
| `xiaomi_cyberone_hand_2026` | Xiaomi |   |   | motors located in the hand (compact motors generate heat requiring liquid cooling); no tendon/linkage statement, though contrast with tendon-driven hands' cycle life implies a non-tendon design |   |   |   | full-palm tactile sensing, area ~8,200 sq mm, detects pressure and contact across the whole palm not just fingertips; taxel count and type not stated |   |   |   | no |   |   | prototype |
| `shadow_dexterous_hand_2005` | Shadow Robot Company | 24 | 20 | tendon-driven, motors in the forearm (20 Smart Motor nodes, Maxon motors, PWM) | 4300 |   | 4 kg in a power grasp, vendor claim, protocol not stated | Shadow Tactile Fingertips (STF): 17x3 DoF Hall-effect taxels, 1000 Hz, uncalibrated; up to 5 fingertips; software also supports BioTac/MST/UBI0/PST fingertip options | EtherCAT at 1 kHz to the host, with a 5 kHz tendon-force loop inside each motor module |   |   | no |   | MuJoCo models for Hand E and variants, plus Gazebo, in sr_common | sold |
| `proception_prohand_2026` | Proception Inc (YC W25) | 22 |   | tendon-driven, motors pull cables to move the fingers |   |   |   | integrated skin-like sensors detecting contact, supporting grip control; same 'sensor skin' used on the companion ProGlove; type/count not stated |   |   |   | no |   |   | sold |
| `sharpa_wave_2026` | Sharpa Robotics (Sharpa Pte Ltd) | 22 | 22 |   | 1300 | 20 / 12 | 40 kg / 24 kg (the same two unlabelled columns) | 'Dynamic Tactile Array' (DTA), camera-type array at the fingertip: resolution 240x240 / 60x60, force resolution 0.02 N / 0.05 N, spatial resolution 1 mm / 2 mm, frame rate 180 fps / 30 fps, force range 0-30 N, latency 20 ms, 6-D F/T; number of sensors per hand not stated | 500 Hz over 1000BASE-T Ethernet |   |   | no |   | MuJoCo and Isaac Sim models | sold |
| `tesollo_dg5f_2024` | Tesollo Inc. (Incheon HQ, Gwangmyeong R&D/factory) | 20 | 20 | one integrated actuator per joint ('high-torque actuation', absolute encoder); page does not say direct-drive | 1763 |   | pinching 2.5 kg rated and 5 kg maximum; enveloping 10 kg rated and 20 kg maximum | none standard; optional fingertip sensors (6-axis F/T, 3-axis force, or tactile) available; count/type not given | 250 Hz over Modbus RTU or TCP and Ethernet TCP/IP |   |   | no |   |   | sold |
| `unitree_dex5_2025` | Unitree Robotics (Yushu Technology Co., Ltd.) | 20 | 16 | in-joint geared motor ('hollow-cup motor' + high-precision encoder + low-damping small-clearance reducer), backdrivable; page does not use the words tendon or linkage | 1100 | 10 | 3.5 kg palm down and 4.5 kg palm left, on a 5 cm round hard object | Dex5-1: none. Dex5-1P: 94 pressure sensors per hand (2x5 palm + 2x3x5 finger pad + 2x3x5 fingertip + 2x3x4 finger root), range 10 g-2500 g. | 1000 Hz over USB 2.0, with per-joint stiffness and damping commands |   |   | no |   |   | sold |
| `wuji_hand_2025` | Wuji Technology (founded 2019) | 20 | 20 | direct-drive rotary, backdrivable |   |   |   | 'Multi-Axis Force/Torque Fingertip Sensing' confirmed present; no type, count or range given | 1000 Hz across 20 axes over 100BASE-TX Ethernet, MIT force-position hybrid mode |   |   | no |   | MuJoCo and Isaac Sim models | sold |
| `allegro_hand_v4_2016` | Wonik Robotics Co. Ltd. (Seoul, South Korea); earlier versions 1.0/2.0 made by SimLab Co. Ltd. | 16 | 16 |   |   |   |   | none | 333 Hz, CAN, the hand's own real-time clock (driver README) |   |   | no |   | URDF and xacro, left and right, in the ROS driver repo | sold |
| `inspire_rh56dfx_2023` | Beijing Inspire Robots Technology Co., Ltd. | 12 | 6 |   | 540 | 10 |   | none (this variant is the 'without tactile sensors' table; a tactile FTP variant exists per bib but is not on this page) | RS485; rate not stated |   |   | no |   |   | sold |
| `robotera_xhand1_2024` | ROBOTERA | 12 | 12 | gear-driven force-controlled joint modules per finger segment, back-drivable | 1100 |   | 25 kg, tracker's 'Strength' figure, over 25 kg gripping palm-up | tactile/force sensors on every fingertip confirmed present (senses contact, force, temperature); count and array size not stated | not stated | 14000 |   | no |   | URDF exists but is licensed; `maniptrans_2025` withholds it | sold |
| `shadow_dex_ee_2024` | Shadow Robot Company, in collaboration with Google DeepMind | 12 |   |   | 4100 |   |   | stereo camera-based fingertip tactile sensors (hundreds of taxels each); multi-taxel 3-DoF arrays on middle and proximal phalanges; counts not stated | not stated; the page claims 'high bandwidth torque and position control loops' |   |   | no |   |   | sold |
| `brainco_revo2_2025` | BrainCo Inc. | 11 | 6 |   | 383 | 15 | >=20 kg | Touch variant only: multi-dimensional fingertip tactile module with 'Tactile Adaptive Control'; count/type not stated. Basic and Pro variants: none. | RS485 and CAN FD; EtherCAT on Pro and Touch; rate not stated |   |   | no |   |   | sold |
| `linkerbot_l20_2025` | LinkerBot (SDK author 'CHIUS INC') |   |   |   |   |   |   | L10/L20: per finger 4 channels (normal force, tangential force, tangential direction, proximity), 5 sites x 4 channels, 0-255 range, sensor type not stated. O6 (reseller): 16 capacitive tactile regions. | USB-to-CAN at 1 Mbit/s, optional Modbus or RS485; rate not stated |   |   | no |   | URDF, with PyBullet and Isaac Gym examples in the SDK | sold |
| `psyonic_ability_hand_2021` | PSYONIC (San Diego, CA, USA) |   | 6 | linkage (repo file/function names indicate a four-bar finger linkage; not stated on the vendor page itself) |   |   |   | 30 touch sensor values streamed (FSR-based per API and URDF 'no_fsr' variant); per-finger split not stated | BLE, I2C, UART or RS485; rate not stated |   |   | no |   | URDF (left, right, large, small, no-FSR) plus MuJoCo and Isaac Sim paths in the vendor repo | sold |

*33 rows. 216 of 528 cells (40 percent) are values no source stated. A blank price is a hand with no public list price rather than a free hand.*

### B.2 Where each specification came from

| hand | source quality | claim date | caveat recorded in the row | source URL | parsed source in the manifest | note | corpus method rows running it |
|---|---|---|---|---|---|---|---|
| `agibot_omnihand_2025` | unavailable | no source: both store.agibot.com URLs 404, fetched 2026-09-17 |   |   | no manifest entry | papers/notes/agibot_omnihand_2025.md | 1: `clutterdexgrasp_2025` |
| `onex_neo_hand_2026` | vendor page | vendor page, 2026-07-09 |   |   | no manifest entry | papers/notes/onex_neo_hand_2026.md | 0 |
| `leap_hand_v2_adv_2025` | vendor page | undated project page; API repo at commit a0936196, fetched 2026-09-17 | the page claims 21 DoF with 17 powered motors and the README calls the same hand 17-DOF | https://github.com/leap-hand/LEAP_Hand_V2_Adv_API | no manifest entry | papers/notes/leap_hand_v2_adv_2025.md | 2: `bidex_teleop_2024`, `dexwild_2025` |
| `paxini_dexh13_2024` | press | press, CES 2026-01-07 |   |   | no manifest entry | papers/notes/paxini_dexh13_2024.md | 0 |
| `clone_robotics_hand_2024` | press | press, 2025-11-24, on a video of 2025-11-15 | 'under 2 pounds' is an upper bound, and the source does not say whether the 500 W pump and 36 valves are inside it |   | no manifest entry | papers/notes/clone_robotics_hand_2024.md | 0 |
| `sanctuary_phoenix_hand_2024` | press | undated press release; trade reprint 2024-12-17 |   |   | no manifest entry | papers/notes/sanctuary_phoenix_hand_2024.md | 0 |
| `bidexhand_2025` | paper | paper, 2025 (ICRA Dexterity workshop abstract) | the paper states 16 independently actuated DoF and 21 joints; the README states 15 servos driving 15 joints | https://github.com/wengmister/BiDexHand | 5 pp, 89f39715, fetched 2026-09-17 | papers/notes/bidexhand_2025.md | 0 |
| `ruka_v2_2026` | paper | paper, 2026 | the AS5600 encoders are attachable and detachable and are read for calibration and measurement only, not in the control loop | https://github.com/ruka-hand/RUKA | 20 pp, d71d6f90, fetched 2026-09-17 | papers/notes/ruka_v2_2026.md | 0 |
| `orca_hand_2025` | paper | paper, 2025 | the 19.6 N previously tabulated as a fingertip force is the newton equivalent of the 2 kg index-finger payload at a control-imposed current limit, and no source states it as a force | https://github.com/orcahand/orca_core | 8 pp, f3967f2e, fetched 2026-09-17 | papers/notes/orca_hand_2025.md | 0 |
| `leap_hand_2023` | paper | paper, 2023 |   | https://github.com/leap-hand/LEAP_Hand_API | 11 pp, ac08a57e, fetched 2026-09-17 | papers/notes/leap_hand_2023.md | 12: `bidex_teleop_2024`, `bidexhd_2024`, `cross_embodiment_world_models_2025`, `dexcap_2024`, `dexndm_2025`, `dexterous_functional_grasping_2023`, `dextrack_2025`, `dexwild_2025`, `dreureka_2024`, `teledexter_2026`, `unidex_2026`, `videodex_2022` |
| `ruka_2025` | paper | paper, 2025 |   | https://github.com/ruka-hand/RUKA | 13 pp, 3a19161f, fetched 2026-09-17 | papers/notes/ruka_2025.md | 0 |
| `dexhand_open_source_2023` | project page and GitHub README | page posts 2023-08-08 to 2023-10-01; no hardware release date | no joint count is given anywhere, so no DoF figure can be quoted; the servo count is 16 finger and thumb micro-servos plus 2 wrist servos, with a third optional. The $300 is 'additional total cost of components', excluding printing and the wrist servos | https://github.com/TheRobotStudio/V1.0-Dexhand | no manifest entry | papers/notes/dexhand_open_source_2023.md | 0 |
| `ilda_hand_2021` | paper | paper, accepted 2021-11-05 |   | https://www.nature.com/articles/s41467-021-27261-0.pdf | 13 pp, ed0e19c2, fetched 2026-09-17 | papers/notes/ilda_hand_2021.md | 0 |
| `pisa_iit_softhand_2014` | paper | paper, IJRR 2014 |   | https://www.centropiaggio.unipi.it/sites/default/files/PisaIIT_SoftHand_0.pdf | 14 pp, 9c9cd17f, fetched 2026-09-17 | papers/notes/pisa_iit_softhand_2014.md | 0 |
| `faive_hand_2023` | paper | paper, 2023 | the row's open-hardware status is unconfirmed: the repo has LICENSE and LICENSE-NVIDIA files whose contents were not captured, and no open-hardware claim appears in the sources | https://github.com/srl-ethz/faive_gym_oss | 7 pp, 13feb753, fetched 2026-09-17 | papers/notes/faive_hand_2023.md | 1: `graspxl_2024` |
| `boston_dynamics_atlas_hand_2026` | press | trade press, 2026-01-05 (CES); the Boston Dynamics blog of the same date has no hand content |   |   | no manifest entry | papers/notes/boston_dynamics_atlas_hand_2026.md | 0 |
| `daxo_muscle_v0_2025` | third-party tracker | third-party catalogue post, 2026-09-16; daxo-robotics.com returned HTTP 404 | 120 actuators in 750 g is about 6 g per actuator including structure, tendons, routing and skin; no DoF number is stated, and a redundant tendon architecture with no rigid joints has fewer kinematic DoF than actuators |   | no manifest entry | papers/notes/daxo_muscle_v0_2025.md | 0 |
| `figure_03_hand_2025` | third-party tracker | undated tracker page, fetched 2026-09-17; figure.ai launch page returned HTTP 404 | the tracker's 'Degrees of freedom, hands / 20' sits beside 'Number of fingers / 10', so the 20 is most likely the pair and about 10 per hand; the 16-per-hand figure in circulation has no reachable source |   | no manifest entry | papers/notes/figure_03_hand_2025.md | 0 |
| `tesla_optimus_hand_2025` | press | Gen 2 video 2023-12-13; V3 patents filed 2024-10, relayed by press 2026-04 | the 22 DoF in circulation is a Teslarati article's arithmetic of four DoF on each of five fingers plus two at the wrist, not a Tesla statement; Gen 2's own figure is 11 DoF. This row's actuation cell describes V3 and its tactile cell describes Gen 2 | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9505134 | 20 pp, 93664ecb, fetched 2026-09-17 | papers/notes/tesla_optimus_hand_2025.md | 0 |
| `xiaomi_cyberone_hand_2026` | press | press, 2026-03-30 |   |   | no manifest entry | papers/notes/xiaomi_cyberone_hand_2026.md | 0 |
| `shadow_dexterous_hand_2005` | datasheet | specification dated 2024-12-04 | the four distal joints are coupled and not independently controllable, so the '24 DoF' quoted in learning papers is the joint count | https://shadowrobot.com/wp-content/uploads/2024/12/shadow_dexterous_hand_e_technical_specification_20241204.pdf | 11 pp, 66541d02, fetched 2026-09-17 | papers/notes/shadow_dexterous_hand_2005.md | 21: `asymdex_2024`, `bidexgrasp_2026`, `bimangrasp_2024`, `cross_embodiment_world_models_2025`, `dexdeform_2023`, `dexman_2025`, `dp3_2024`, `eureka_2023`, `graspxl_2024`, `maniptrans_2025`, `mjpc_2022`, `objdex_2024`, `openai_dexterity_2018`, `openai_rubiks_cube_2019`, `pddm_2019`, `pgdm_2023`, `pianomime_2024`, `resdex_2024`, `unidex_2026`, `unidexgrasp_2023`, `unidexgrasp_pp_2023` |
| `proception_prohand_2026` | press | launch post and press, 2026-06-29 | the evidence is a shipping announcement, not a datasheet: no weight, force, actuated-DoF count or control rate is stated anywhere |   | no manifest entry | papers/notes/proception_prohand_2026.md | 0 |
| `sharpa_wave_2026` | vendor page | undated page, copyright 2026, fetched 2026-09-17 | the page footnotes 'Specifications may vary between products', and no column of the spec table is labelled |   | no manifest entry | papers/notes/sharpa_wave_2026.md | 6: `dexteleop0_2026`, `egoscale_2026`, `metis_2025`, `poise_2026`, `simtoolreal_2026`, `teledexter_2026` |
| `tesollo_dg5f_2024` | vendor page | undated page, copyright 2026, download links dated 2026-08 |   | https://en.tesollo.com/wp-content/uploads/2025/02/TESOLLO-DG-5F-catalogue-En-2.pdf | no manifest entry | papers/notes/tesollo_dg5f_2024.md | 0 |
| `unitree_dex5_2025` | datasheet | undated page, copyright 2016-2025, fetched 2026-09-17 |   | https://github.com/unitreerobotics/unitree_sdk2 | no manifest entry | papers/notes/unitree_dex5_2025.md | 0 |
| `wuji_hand_2025` | vendor page | undated page, copyright 2026, fetched 2026-09-17 | the page footnotes that these figures 'reflect the current Beta1 product and the SPEC will continue to iterate' |   | no manifest entry | papers/notes/wuji_hand_2025.md | 2: `toporetarget_2026`, `unidex_2026` |
| `allegro_hand_v4_2016` | driver repo | driver repo, versions 1.0-4.0 undated, fetched 2026-09-17 | allegrohand.com/v4 returned HTTP 404 and the Wonik wiki timed out; every cell here comes from the ROS driver repository, and weight, joint torque, payload and price have no reachable source | https://github.com/simlabrobotics/allegro_hand_ros_v4 | no manifest entry | papers/notes/allegro_hand_v4_2016.md | 35: `anyrotate_2024`, `anyteleop_2023`, `asymdex_2024`, `castro_sap_contact_2021`, `cross_embodiment_world_models_2025`, `cyberdemo_2024`, `dexmachina_2025`, `dexpbt_2023`, `dexpilot_2020`, `dexplore_2025`, `dexpoint_2022`, `dexteritygen_2025`, `dexterous_handover_2025`, `dextrack_2025`, `dextreme_2022`, `dime_2022`, `dp3_2024`, `dynamic_handover_2023`, `eureka_2023`, `geometric_retargeting_2025`, `graspxl_2024`, `holo_dex_2022`, `hora_2022`, `hudor_2024`, `human2sim2robot_2025`, `maniptrans_2025`, `pang_global_planning_2022`, `penspin_2024`, `robot_synesthesia_2023`, `rotateit_2023`, `rotating_without_seeing_2023`, `twisting_lids_2024`, `unidex_2026`, `viserdex_2026`, `wm_dex_human_videos_2025` |
| `inspire_rh56dfx_2023` | vendor page | undated page, fetched 2026-09-17 | the vendor's own page reads 'Degrees of freedom 6, Numbers of joints 12'; the joints column here prints the joint count, so the vendor's DoF figure is the actuated-DoF column |   | no manifest entry | papers/notes/inspire_rh56dfx_2023.md | 19: `ace_teleop_2024`, `articulated_tools_inhand_2025`, `being_h05_2026`, `being_h0_2025`, `bidexgrasp_2026`, `dexmachina_2025`, `dexmimicgen_2024`, `dexplore_2025`, `dexumi_2025`, `dexvla_2025`, `humanoid_policy_human_policy_2025`, `humanoid_sim2real_recipe_2025`, `humanplus_2024`, `maniptrans_2025`, `metis_2025`, `okami_2024`, `omnih2o_2024`, `open_television_2024`, `unidex_2026` |
| `robotera_xhand1_2024` | third-party tracker | undated tracker page, fetched 2026-09-17; the vendor page was not fetched | the 15 N in circulation comes from a survey table, not from the tracker or the vendor; the tracker states no fingertip force |   | no manifest entry | papers/notes/robotera_xhand1_2024.md | 8: `cross_embodiment_world_models_2025`, `deximit_2026`, `dexmachina_2025`, `dexora_2026`, `dexumi_2025`, `dp3_2024`, `force_grasp_sim2real_2026`, `unidex_2026` |
| `shadow_dex_ee_2024` | vendor page | undated page, copyright 2026, fetched 2026-09-17 |   |   | no manifest entry | papers/notes/shadow_dex_ee_2024.md | 1: `demostart_2024` |
| `brainco_revo2_2025` | datasheet | undated page, fetched 2026-09-17 |   |   | no manifest entry | papers/notes/brainco_revo2_2025.md | 1: `bidexgrasp_2026` |
| `linkerbot_l20_2025` | vendor page | undated page, fetched 2026-09-17 |   | https://github.com/linkerbotai/linker_hand_sdk | no manifest entry | papers/notes/linkerbot_l20_2025.md | 1: `being_h05_2026` |
| `psyonic_ability_hand_2021` | vendor page | undated page, fetched 2026-09-17 | the four-bar finger linkage rests on repository file names and the five fingers on URDF meshes; the vendor page states neither | https://github.com/psyonicinc/ability-hand-api | no manifest entry | papers/notes/psyonic_ability_hand_2021.md | 7: `ace_teleop_2024`, `asymdex_2024`, `bunny_visionpro_2024`, `cross_embodiment_world_models_2025`, `dexmachina_2025`, `hato_visuotactile_2024`, `unidex_2026` |

*33 rows. 31 of 264 cells (11 percent) are values no source stated. `parsed source in the manifest` gives page count, the first eight characters of the sha256 of the stored copy, and the date it was fetched. A hand with no manifest entry was recorded from a page that could not be stored, and its row should be read as a claim with no retrievable source.*


---

## Appendix C. Per-paper reward term extraction

Table 5 marks nine recurring term families across the in-hand reorientation methods. This appendix is the extraction underneath it, over every method row that records a reward at all. `terms stated` counts the terms the paper itself names. `where the reward was read` gives the section of the paper or the file in the released code that the note quotes. A row with a `paper/code class` is one where the two disagree, and C.2 prints the disagreement in full. Cells and entries reproduce the text stored in the row, with the source's own punctuation and wording.

### C.1 The extraction

| method | yr | paradigm | terms stated | term names as the paper names them | where the reward was read | in reward matrix | code released | paper/code class | confidence |
|---|---|---|---|---|---|---|---|---|---|
| `openai_dexterity_2018` | 2018 | RL | 3 |   | Method, reward (Sec 4.2 / App C.1) | yes | no |   |   |
| `openai_rubiks_cube_2019` | 2019 | RL, distillation | 3 |   | Method, reward (Sec. 6.1) | yes | no |   |   |
| `pddm_2019` | 2019 | MPC |   |   |   |   | yes | contradiction | high |
| `dexpoint_2022` | 2022 | RL | 4 | reach, contact, lift, action penalty |   |   | yes | contradiction | high |
| `dextreme_2022` | 2022 | RL | 6 |   | Reward block, paper Table 2 against allegro_hand_dextreme.py and the two DR yamls | yes | yes | contradiction | high |
| `dexvip_2022` | 2022 | RL | 4 |   |   |   | no |   |   |
| `hora_2022` | 2022 | RL, distillation | 5 |   | Block C, paper Sec 3.1/App. C against configs/task/AllegroHandHora.yaml | yes | yes | version-skew | high |
| `mjpc_2022` | 2022 | MPC | 3 |   |   |   | yes |   |   |
| `visual_dexterity_2022` | 2022 | RL, distillation | 7 | c1_sparse_task, c2_dense_task, c3_fingertip_dist, c4_energy, c5_push_away_penalty, c6_table_contact, c7_finger_height | Method, Table S1 against dexenv/envs/rewards.py and dexenv/conf/task/dclaw.yaml | yes | yes | contradiction | high |
| `aloha_act_2023` | 2023 | BC |   |   |   |   | yes | internal-inconsistency | high |
| `artigrasp_2023` | 2023 | RL | 4 | r_p, r_c, r_reg, r_task |   |   | yes | parse-limitation | low |
| `dexpbt_2023` | 2023 | RL | 4 | r_reach, r_pick, r_targ, r_vel | Block C, paper Sec III-C/Table II against allegro_kuka_base.py and AllegroKuka.yaml | yes | yes | contradiction | high |
| `dexterous_functional_grasping_2023` | 2023 | RL | 2 | r_threshold, r_hand-obj |   |   | no |   |   |
| `diffusion_policy_2023` | 2023 | BC, diffusion |   |   |   |   | yes | parse-limitation | high |
| `dynamic_handover_2023` | 2023 | RL | 3 |   |   |   | no |   |   |
| `eureka_2023` | 2023 | RL |   |   | Method, App. G.1/G.2 LLM-authored rewards; generated code not checked into the repo | yes | yes | parse-limitation | low |
| `pgdm_2023` | 2023 | RL | 2 |   |   |   | no |   |   |
| `physhoi_2023` | 2023 | RL | 4 | body motion reward, object motion reward, ig reward, cg reward |   |   | yes | contradiction | high |
| `robot_synesthesia_2023` | 2023 | RL, distillation | 6 |   | Method, reward (Sec IV.A.3 eq. 1); no code released | yes | no |   |   |
| `rotateit_2023` | 2023 | RL, distillation | 6 |   | Block C (paper Sec 3.1, App. B); no code released | yes |   |   |   |
| `rotating_without_seeing_2023` | 2023 | RL | 6 | r_rot, r_vel, r_fall, r_work, r_torque, r_dist | Reward block (Sec IV.A.3, App. D Eq. 9); no code released | yes |   |   |   |
| `unidexgrasp_2023` | 2023 | grasp-synthesis, RL, distillation | 4 | goal, reach, lift, move |   |   | yes | contradiction | high |
| `unidexgrasp_pp_2023` | 2023 | RL, distillation | 4 | r_reach, r_lift, r_move, r_bonus |   |   | yes | parse-limitation | low |
| `anyrotate_2024` | 2024 | RL, distillation | 10 | keypoint distance reward, rotation reward, goal bonus reward, good contact reward, bad contact penalty, angular velocity penalty, pose penalty, work penalty, torque penalty, termination penalty | Block C (App. B.1 weights); no code released | yes | no |   |   |
| `asymdex_2024` | 2024 | RL | 4 |   |   |   | yes | code-absent | medium |
| `bidexhd_2024` | 2024 | RL, distillation | 4 | r_appro, r_lift, r_bonus, r_track |   |   | yes | parse-limitation | high |
| `bimangrasp_2024` | 2024 | grasp-synthesis, diffusion | 7 |   |   |   | no |   |   |
| `demostart_2024` | 2024 | RL, distillation | 1 |   | Method, reward (App. VII-A.1); no code released | yes | no |   |   |
| `dexmimicgen_2024` | 2024 | data-collection, BC | 1 |   |   |   | yes | code-absent | high |
| `dp3_2024` | 2024 | BC, diffusion |   |   |   |   | yes | internal-inconsistency | medium |
| `dreureka_2024` | 2024 | RL | 4 | ang_z_vel_reward, lin_vel_penalty, object_fall_penalty, deviation_penalty | Method, App. B1 Prompt 13; cube-rotation code absent from the released repo | yes | yes | code-absent | high |
| `graspxl_2024` | 2024 | RL | 8 | r_dis, r_v, r_ω, r_m, r_c, r_f, r_reg, r_anatomy |   |   | yes | parse-limitation | low |
| `hudor_2024` | 2024 | RL | 1 |   |   |   | no |   |   |
| `humanplus_2024` | 2024 | RL, BC | 8 |   |   |   | yes | parse-limitation | medium |
| `objdex_2024` | 2024 | BC, RL, distillation | 3 | rotation, translation, joint angle |   |   | no |   |   |
| `omnigrasp_2024` | 2024 | RL, distillation | 3 | r_approach, r_pre-grasp, r_obj |   |   | yes | parse-limitation | medium |
| `omnih2o_2024` | 2024 | RL, distillation | 24 |   |   |   | yes | internal-inconsistency | medium |
| `open_television_2024` | 2024 | teleop-system, BC |   |   |   |   | yes | code-absent | low |
| `penspin_2024` | 2024 | RL, distillation | 7 |   | Method, paper Table 4 against penspin/tasks/allegro_hand_hora.py and configs/task/AllegroHandHora.yaml | yes | yes | contradiction | medium |
| `pi0_2024` | 2024 | VLA, flow |   |   |   |   | yes | version-skew | high |
| `pianomime_2024` | 2024 | RL+demo, distillation | 2 |   |   |   | yes | contradiction | high |
| `resdex_2024` | 2024 | RL, distillation | 7 | task, proposal, pose, reach, lift, move, bonus |   |   | yes | parse-limitation | medium |
| `twisting_lids_2024` | 2024 | RL | 5 |   |   |   | no |   |   |
| `articulated_tools_inhand_2025` | 2025 | RL, BC, distillation | 8 | r_pos, r_quat, r_goal, r_timer, r_inc, r_contact, r_slip, r_act |   |   | no |   |   |
| `being_h0_2025` | 2025 | VLA, BC |   |   |   |   | yes | code-absent | high |
| `clutterdexgrasp_2025` | 2025 | RL, diffusion, distillation | 4 | r_pos, r_neg, r_grasp, r_force |   |   | no |   |   |
| `cross_embodiment_world_models_2025` | 2025 | world-model, MPC | 2 |   |   |   | no |   |   |
| `dexgraspvla_2025` | 2025 | VLA, diffusion | 1 |   |   |   | yes | parse-limitation | high |
| `dexmachina_2025` | 2025 | RL | 4 |   |   |   | yes | internal-inconsistency | low |
| `dexman_2025` | 2025 | RL, trajopt | 3 |   |   |   | no |   |   |
| `dexndm_2025` | 2025 | RL, distillation | 7 |   | Reward block (Sec. 3.1, App. A.1); no code released | yes | no |   |   |
| `dexplore_2025` | 2025 | RL, distillation | 7 | r_j^h, r_r^h, r_p^o, r_r^o, r_d, r_c, r_energy |   |   | yes |   |   |
| `dexremoe_2025` | 2025 | RL | 5 | csuccess, cdist, crot, cω, ca | Method, reward (Sec. III-B, Table II); no code released | yes | no |   |   |
| `dexteritygen_2025` | 2025 | RL, diffusion |   |   | Method, reward/objective: the RL reward behind the pretrained controller is not quoted in the source | yes | no |   |   |
| `dexterous_handover_2025` | 2025 | RL | 3 | r_BASE, contact_term (c·w_c), r_MANIP |   |   |   |   |   |
| `dextrack_2025` | 2025 | RL+demo | 5 | r_o,p, r_o,q, r_wrist, r_finger, r_affinity |   |   | yes | parse-limitation | low |
| `dexvla_2025` | 2025 | VLA, diffusion | 2 |   |   |   | yes | parse-limitation | high |
| `dydexhandover_2025` | 2025 | RL | 5 | R_dist, R_obj, R_contact, P_action, P_hand |   |   | no |   |   |
| `geometric_retargeting_2025` | 2025 | teleop-system | 5 | Ldir, Lcover, Lflat, Lpinch, Lcol |   |   | yes |   |   |
| `groot_n16_2025` | 2025 | VLA |   |   |   |   | yes | version-skew | high |
| `groot_n1_2025` | 2025 | VLA, flow |   |   |   |   | yes | version-skew | high |
| `human2sim2robot_2025` | 2025 | RL | 1 | r_obj |   |   | yes |   |   |
| `humanoid_policy_human_policy_2025` | 2025 | BC | 2 |   |   |   | yes |   |   |
| `humanoid_sim2real_recipe_2025` | 2025 | RL, distillation | 2 |   |   |   | no |   |   |
| `maniptrans_2025` | 2025 | RL, BC, diffusion | 5 | r_wrist, r_finger, r_smooth, r_object, r_contact |   |   | yes | parse-limitation | low |
| `metis_2025` | 2025 | VLA | 2 | Lar, Laction |   |   | no |   |   |
| `pi05_2025` | 2025 | VLA, flow |   |   |   |   | yes | code-absent | high |
| `pistar06_2025` | 2025 | VLA, RL, flow |   |   |   |   | yes | code-absent | high |
| `wm_dex_human_videos_2025` | 2025 | world-model, MPC | 2 |   |   |   | no |   |   |
| `being_h05_2026` | 2026 | VLA, flow |   |   |   |   | yes | code-absent | high |
| `dexteleop0_2026` | 2026 | teleop-system, MPC | 3 |   |   |   | no |   |   |
| `force_grasp_sim2real_2026` | 2026 | RL | 7 | R_torque, R_Force, R_diff, R_outer, terminal-state penalty, R_action, R_vel | Method, reward (Sec 3.5.1, Table 2); no weights survive the parse; no code released | yes | no |   |   |
| `poise_2026` | 2026 | RL | 4 | pose reaching, goal completion, grasp maintenance, drop and actuation regularization | Method, reward (Sec. IV-D); weights lost to the parse; no code released | yes | no |   |   |
| `simtoolreal_2026` | 2026 | RL | 5 | r_smooth, r_approach, r_lift, r_goal, b_succ |   |   | no |   |   |
| `teledexter_2026` | 2026 | RL, teleop-system |   |   | Reward block (Sec. 3.1); term formulas lost to the parse; no code released | yes | no |   |   |
| `toporetarget_2026` | 2026 | trajopt, RL | 4 | object, link-position, joint-position, action-smoothness |   |   | no |   |   |
| `viserdex_2026` | 2026 | RL, distillation | 10 | orientation tracking, success bonus, object dropped, object distance, object velocity, joint velocity, action magnitude, action rate, joint work, joint torques | Method, reward (App. Table IX); no code released | yes | no |   |   |

*77 rows. 253 of 770 cells (32 percent) are values no source stated. A blank `terms stated` with a filled `term names` column is a paper that names its terms without numbering them. `in reward matrix` marks the rows that are also in the reward-term matrix, which covers in-hand reorientation only.*

### C.2 Paper against released code, in full

Each entry below is the disagreement text stored in the row, unedited. The class is what Sec. 5.8 and Sec. 8.1 count. `contradiction` means the paper states one value and the shipped code demonstrably states another. `parse-limitation` means this survey's own parse could not settle it and the accusation is withdrawn. `code-absent` means the described component is not in the released repository. `version-skew` means the repository is a later generation than the paper. `internal-inconsistency` means the paper disagrees with itself and no code is implicated.

**contradiction, 9 rows.**

- `pddm_2019` (high). Table 2 states obs-dim 46 for In-hand Reorientation while the released cube_env.py code sums to 39; the Baoding reward code includes an extra -10*wrist_too_high term absent from Table 2's printed formula.
- `dexpoint_2022` (high). The released code's reward adds several terms absent from the paper's four-term Eq. 5 (a lift-threshold bonus, a target-distance term, a rotation bonus, and an IK controller-tracking penalty) and reshapes the reach/lift terms into inverse-distance and clipped forms rather than the paper's plain distance/height-difference formulas.
- `dextreme_2022` (high). Action Delta Penalty weight is -0.25 in paper Table 2 but -0.2 in the ADR yaml and -0.01 in the ManualDR yaml; the Joint Velocity Penalty in code normalises velocity by (max_velocity-vel_tolerance) unlike the paper's stated formula; code has a timeout_rew term absent from the paper's reward table; Appendix Table 12 states critic learning rate 5e-4 and KL threshold 0.16, vs body text/code values of 5e-5 and 0.016.
- `visual_dexterity_2022` (high). Table S1 states 32000 teacher training environments, but the released config sets alg.num_envs to 8000 (parent config 16384); fallDistance differs across two shipped configs (0.24 vs 0.15, only the latter matching Table S1's threshold); the paper's Eq 8 penultimate-joint penalty (c7=-2) does not appear anywhere in the released reward code; the config carries a dead distRewardScale=-10.0 key never used in compute_reward; and the paper's table-friction lower bound (0.05) differs by a factor of 10 from the code's randomized lower bound (0.005).
- `dexpbt_2023` (high). Paper presents the reward as 4 mutually exclusive stage terms (r_reach, r_pick, r_targ, -r_vel), but code's compute_kuka_reward sums 8 named components, one of which (hand_delta_penalty) is multiplied by 0 and disabled; there is no single r_vel term in code, instead separate kuka/allegro action penalties whose exact formula is not shown. Also, the paper reports zero experiments with domain randomization, yet the shipped AllegroKuka.yaml already carries a fully specified DR schedule (disabled via randomize: False).
  Review: R3 adversarial review: the disabled-randomisation half is withdrawn, since the note finds it consistent with the paper; the zeroed reward term stands
- `physhoi_2023` (high). The released code hardcodes the body position-velocity error and the object rotation/rotation-velocity errors to zero in compute_humanoid_reward, so despite Table 4 listing nonzero λ^or=0.1/λ^orv=0.01 weights for GRAB, the trained reward never actually tracks object orientation (position-only in practice).
- `unidexgrasp_2023` (high). The paper describes a four-term weighted reward (r_goal + r_reach + r_lift + r_move via Table 7's omega weights) but the released compute_hand_reward implements a different threshold-gated torch.where cascade with distinct hardcoded coefficients that do not map one-to-one onto the paper's weights.
- `penspin_2024` (medium). The appendix states a randomised disturbance force, and the released configs/task/AllegroHandHora.yaml ships forceScale: 0.0, so no shipped configuration applies it.
  Review: Narrowed before author contact. The original charge also said the released code disables the paper's tactile channel, and that half is withdrawn: the config read has numObservations 96 and enable_tactile False, which is consistent with the proprioception-only student rather than the oracle, and the paper never claims the student has tactile input. The disturbance-force half is unaffected.
- `pianomime_2024` (high). Paper's Table 3 states 2 weighted reward terms (Key Press 2/3, Mimic 1/3), but the released code sums roughly 5 unweighted terms (key press doubled, sustain, energy and fingering hardcoded to return 0, forearm-collision) plus a separately-added mimic wrapper term.

**internal-inconsistency, 4 rows.**

- `aloha_act_2023` (high). Algorithm 1 pseudocode states L_reconst = MSE, but Sec.IV.C's prose explicitly states L1 loss is used instead; the algorithm box and the implementation text disagree; code/md captures only function signatures, not bodies, for policy.py's loss implementation
- `dp3_2024` (medium). the paper's prose states the network predicts the noise added to the data, but the shipped default config trains with prediction_type: sample (predicting the denoised action a^0 directly), not epsilon; the paper only qualifies this later in the same section (Fig. 7 ablates both).
- `omnih2o_2024` (medium). stumble weight -0.00125 (paper) vs -1250 (code); max-feet-height sign/magnitude differ (+1000 paper vs -2500 code, a penalty not a bonus); paper's exp(-c*//.//) form vs code's exp(-err^2/sigma); curriculum level-down threshold 40 (paper) vs 50 (code)
  Review: Withdrawn as a contradiction before author contact. Four sibling weights match the paper to the digit under a systematic x1.25 curriculum factor and only the stumble weight differs, by a factor of about a million, which is a typo signature in the paper's own table rather than evidence of a different trained objective. The hands in this work are driven open-loop from VR pose, outside the policy and outside the reward, so it is a weak fit for a dexterous-manipulation reward census in the first place.
- `dexmachina_2025` (low). paper describes a plain weighted sum lambda_task*r_task + lambda_imi*r_imi + lambda_bc*r_bc + lambda_con*r_con with unspecified weights; code implements a multiplicative task term with per-component beta decay, an unmentioned 0.1 force-penalty term, and curriculum-driven decay of auxiliary weights not described as such in the paper
  Review: R3 adversarial review: the multiplicative form credited to the code is printed in the paper itself

**version-skew, 4 rows.**

- `hora_2022` (high). The parsed code commit's joint-noise range, disabled default disturbance force, and default cube object type differ from the paper's stated values; the code README itself says to use tag v0.0.1, not the parsed commit, to reproduce paper numbers.
- `pi0_2024` (high). The released repo (openpi, commit 215abfb2) has evolved past this paper: it also documents pi0-FAST (autoregressive) and pi0.5 checkpoints/configs not described in this paper, which describes only the flow-matching pi0 and the non-VLM pi0-small ablation.
- `groot_n16_2025` (high). code/md is the current Isaac-GR00T main branch (N1.7 generation, commit 51d4c89f), not the N1.6 checkpoint; the repo names a separate n1d6 branch for N1.6 that was not fetched. The page states N1.6's backbone is "an internal NVIDIA Cosmos-2B VLM variant," but the repo's own changelog states the Eagle backbone (nvidia/Eagle-Block2A-2B-v2) was used through N1.6 and only replaced by Cosmos-Reason2-2B in N1.7 -- whether the page's Cosmos-2B variant is a third distinct model or the page is describing N1.7 under an N1.6 headline is not resolvable from what was fetched.
  Review: The page attributes a Cosmos backbone to N1.6 while the repository changelog says N1.6 used Eagle and N1.7 made the switch, so the repository is a later generation than the page describes.
- `groot_n1_2025` (high). The parsed code repo (Isaac-GR00T, commit 51d4c89f) is a later N1.7 generation, not the paper's GR00T-N1-2B: VLM backbone changed from the paper's Eagle-2 to Cosmos-Reason2-2B (via Qwen3-VL); action horizon expanded from the paper's stated H=16 to 40; state/action dimensions expanded from 29 to 132; DiT layers changed from 32 to 16; embodiment scope widened to include Unitree G1, AgiBot G1, and a 'YAM' arm not described in the paper.

**code-absent, 8 rows.**

- `asymdex_2024` (medium). Code contains a GraspAndPlace-task reward variant (AllegroHandDualArmGraspAndPlaceAsymDex.py) with exponential hand-distance and block-alignment terms not one of the four BiDexHands tasks described in the paper body.
- `dexmimicgen_2024` (high). The environment code includes an unused 'reward_shaping' branch (if self.reward_shaping: pass) that is never described or used in the paper text; only the sparse binary completion reward is used, as the paper states.
- `dreureka_2024` (high). The released DrEureka repo (code/md) contains only forward_locomotion/ and globe_walking/ trees; the LEAP-hand cube-rotation training/deployment code and the quoted Prompt-13 reward are the LEAP-hand authors' own code, not included in the released repo, so the cube-rotation reward cannot be cross-checked against a code file.
- `open_television_2024` (low). The paper's prose states 25k training iterations, lr 5e-5, batch size 45, but the code repo's example training command instead shows 50000 epochs and an explicit kl_weight=10 not mentioned anywhere in the paper text.
  Review: R3 adversarial review: a behaviour-cloning paper with no reward; the charge compared paper iterations to a README example's epochs
- `being_h0_2025` (high). The actual downstream action-head module referenced in §4.3 (learnable query tokens, proprioceptive projector f_p, regression head f_r) is not present in the parsed code; the repo's own TODO list marks 'Training code and scripts' as unreleased, so the action-chunk-length=16 value and exact proprioception-vector fields come only from inference/eval CLI examples, not a verifiable implementation.
- `pi05_2025` (high). The paper describes a hybrid discrete-FAST-token-pretrain-then-flow-matching-post-train recipe (Eq. 1, alpha: 0 to 10), but the released repo states plainly it 'currently only support[s] the flow matching head for both pi0.5 training and inference.'
- `pistar06_2025` (high). The general openpi framework (pi0/pi0.5/FAST, flow-matching action head, ALOHA/DROID/LIBERO adapters) is released at commit 215abfb2, but the RECAP-specific pieces described in the paper -- the advantage-conditioning input, the distributional value function, the RECAP training loop (Algorithm 1), and the espresso/laundry/box-assembly checkpoints and datasets -- are not present in the parsed repo.
- `being_h05_2026` (high). Released code (commit e12ac44f) exposes only benchmark/inference/config scaffolding (policy.py, beingh_policy.py, dataset-transform configs). no MoT/MoF model definition, no rectified-flow action-expert source, and no config for any dexterous-hand embodiment; the only post-train configs present (libero_robocasa.yaml, libero_all.yaml, robocasa_human.yaml, so101_example.yaml) are all gripper-only, so the dexterous-hand claims cannot be cross-checked against released code.

**parse-limitation, 13 rows.**

- `artigrasp_2023` (low). paper's two regulariser weights (w_rh=0.5, w_ro=0.2) correspond to five separate velocity penalties in code (-0.5,-0.2,-0.5,-0.5,-0.3); the fingertip weight 12.0 and lambda 5.0 in Table 6 do not appear in the yaml; reward weights differ between curriculum phase-1 and phase-2 configs though Table 6 reports only one set
  Review: R3 adversarial review: the reward body is C++ and absent from the parse; the weight split is the paper's documented curriculum
- `diffusion_policy_2023` (high). the paper's core loss equations (DDPM training loss, EBM/InfoNCE, score-matching) are unrecovered images in the parsed text, and code/md is a signature-only API map, so compute_loss's body could not be verified from code; only the exact shipped noise-scheduler config (DDPMScheduler, 100 train steps) is confirmed.
- `eureka_2023` (low). The released repo's default eureka/cfg/config.yaml ships iteration:1, sample:3 (a fast-test default), not the paper's reported experimental configuration of N=5 iterations × K=16 samples × 5 independent runs, and LLM-generated reward code itself is never checked into the repo (written at runtime to a gitignored outputs/ directory).
  Review: R3 adversarial review: the repo README documents the paper's defaults; the cited config block is a fast-test preset
- `unidexgrasp_pp_2023` (low). The paper's four named reward weights (0.5, 0.1, 2, 10) numerically match literals in the released compute_hand_reward, but the code never labels them with the paper's variable names, and the paper's own display equations were dropped from the PDF, so the correspondence is inferred rather than confirmed by either source.
- `bidexhd_2024` (high). Table 5 weights (w_r, w_t, w1-w4, lambda_w=0.12, lambda_ft=0.48) cannot be matched to code reward lines because the code md truncates the reward function before stage-2/final sum; lambda_w and lambda_ft numerically match the code's grasp-condition thresholds (0.12, 0.12x4 fingers) rather than confirmed reward weights
- `graspxl_2024` (low). The code splits the paper's single r_reg = -w_h//u_h//^2 - w_o//u_o//^2 into four separately-weighted terms (wrist vel, wrist qvel, object vel, object qvel), and the floating-phase object-velocity coefficient (-1.5) does not match the paper's stated w_o=0.1, so the regularization weighting cannot be reconciled 1:1 with Table 9.
  Review: R3 adversarial review: the environment source is not in the parse and the note says the reward cannot be verified
- `humanplus_2024` (medium). code implements a superset of legged_gym reward terms (lin_vel_z, ang_vel_xy, orientation, base_height, torques, dof_vel, dof_acc, action_rate, collision, termination, dof/torque limits, tracking_lin/ang_vel, feet_air_time, stumble, stand_still, feet_contact_forces, target_jt) beyond the 8 terms documented in the paper's Table 1
- `omnigrasp_2024` (medium). The code's compute_pregrasp_reward_time hard-codes w_pos, w_rot = 0.9, 0.1, silently overriding the rwd_specs weight arguments passed into the function; separately, the paper's pre-grasp reward weights (w_hp, w_hr) are not resolvable from either the paper text or Appendix Table 7.
- `resdex_2024` (medium). The base-policy and residual-policy task files implement different variants of compute_hand_reward (whether finger/hand-distance terms are included alongside goal_hand_rew/hand_up/bonus differs), a difference the paper's Sec 4.1/4.4 text does not describe, and the released configs' env count (4096 default) and iteration counts (2500/5000) do not match the paper's stated 11,000 envs and 5,000/20,000 iterations.
- `dexgraspvla_2025` (high). Hardware-interfacing code is explicitly withheld ("Due to intellectual property constraints, we are unable to open-source the hardware-related code"); only function signatures for the controller loss (compute_loss, noise_assignment) are present in code/md, not their bodies, so the MSE/Immiscible-Diffusion loss cannot be verified against code.
- `dextrack_2025` (low). The paper gives one canonical reward-weight table (Table 3), but the released repo's task-config YAMLs contain several divergent, unreconciled reward-coefficient sets across AllegroHandTracking/…TrackingGeneralist/other variants, and it is not identifiable from the parsed source which config produced the paper's headline Table 1 numbers.
- `dexvla_2025` (high). code/md only carries class/function signatures, not bodies, for the diffusion head (modeling_scaledp.py) and no config file with the α weight was captured; the paper's diffusion loss and denoising process cannot be verified against code bodies. only the multi-head ScaleDP signature and a DDIM fp32 patch are available, so none of the paper's tables can be reproduced from what was parsed.
- `maniptrans_2025` (low). paper's PPO learning rate (5e-4) and env count (4096) differ from the shipped README/yaml defaults (2e-4, 8192)
  Review: R3 adversarial review: the cited values are a README override and an unused fallback; the repo's own config matches the paper



---

## Appendix D. The existing surveys, and what each covers

Fourteen corpus entries are themselves surveys or engine-comparison studies. Table 10 sets them on
one set of columns. The columns record what each work covers, not how well. Section 1 states what
this survey adds over them and does not repeat the comparison here.

`an_dexil_survey_2025` is the closest in subject, covering imitation learning for multi-fingered
hands by learning family, end-effector class and demonstration source. It gives reinforcement
learning no taxonomy, treats bimanual work as a single "multi-agent" subsection, compares no
simulator, and defines no evaluation metric. `welte_iil_survey_2025` finds only seven dexterous
works that use interactive imitation learning and carries a fifteen-hand commercial table, with no
bimanual section, no benchmark table and no contact modelling. `zhao_sim2real_survey_2020`
supplies the standard sim-to-real split and predates GPU-parallel simulation.
`firoozi_foundation_models_2023` has zero occurrences of bimanual, tactile or in-hand.

`bai_unified_manip_survey_2025` spans all of manipulation across 212 pages. Its Sec. 4.3 on
dexterous manipulation runs about 720 words, the third longest of its ten task subsections behind
grasping and quadrupedal manipulation, which is a real treatment and not a passing mention. The
difference is elsewhere. Its Sec. 1.2 lists dexterous manipulation among the topics that "existing
surveys" cover from "narrower perspectives" and defers it to two of them.

`zhao_dexhand_survey_2026` is the most recent hand-centred survey, with a 29-hand anatomy table
and a task-by-paradigm taxonomy. Its Sec. IV-C names the reference-versus-rollout split that
Section 1 credits it with, and its Sec. III-F is the one bimanual subsection, 16 cited works with
no coordination analysis.

`nine_physics_engines_review_2024` is the predecessor closest to the engine comparison, and it
reviews Brax, Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Unity and Webots for reinforcement
learning research. It scores each on documentation, model and environment creation, URDF and MJCF
support, and readiness for multi-agent work. It runs no benchmark of its own and says so in its
Sec. V, that implementing the same scenarios across nine engines "goes beyond the scope of this
paper". Its running bodies are ant-and-humanoid RL benchmarks rather than hands, and it discusses
no timestep, no friction model, no contact formulation and no penetration.

### Table 10. Existing surveys and what each covers

| survey | yr | scope | taxonomy used | bimanual covered | hardware covered | evaluation covered | gaps it names |
|---|---|---|---|---|---|---|---|
| `isaac_sim_2026` | 2026 | one simulator's ecosystem and application domains, reviewed rather than measured | qualitative capability matrix, Table 1, over simulators | one cited GR00T task called bimanual, no hand, DoF or number | no hand named anywhere in paper or code parse | none. The paper runs no experiment of its own | computational cost, configuration complexity, learning curve |
| `zhao_dexhand_survey_2026` | 2026 | dexterous hands end to end: hardware anatomy, methods, datasets, directions | five task categories, each split by learning paradigm. Hardware is split by actuation, transmission and perception | one subsection, III-F, 16 cited works, no coordination analysis | Table I, 29 hands, 12 columns, secondary values | names two layers: physical plausibility including penetration before execution, success during it. No threshold, method or count | hardware feasibility, perception fusion, learning beyond benchmark-centric optimisation, industrialisation, absent evaluation standards |
| `an_dexil_survey_2025` | 2025 | imitation learning for multi-fingered end-effectors | IL family by end-effector class by demonstration source. RL gets none | one subsection, II.E, framed as multi-agent | hands named in prose, no hand table | no metric defined and no trial count. Calls for protocols, proposes none | contact dynamics in engines, data-collection standards, cross-hand transfer, failure datasets, end-effector morphology |
| `bai_unified_manip_survey_2025` | 2025 | all of robot manipulation. Dexterous manipulation is one of ten task subsections, about 720 words, and Sec. 1.2 defers it to other surveys | high-level planning, action modelling, actuation control, plus a bottleneck taxonomy of data and generalisation | bimanual means two arms. One dual-hand mention in the paper | hands named, no DoF or actuation table | success rate and checkpoint selection, six lines. Never says how success is judged for a dexterous task | no scaling law, sim-to-real for contact-rich tasks, fragmented datasets, reliability as important as success |
| `welte_iil_survey_2025` | 2025 | interactive imitation learning, seven dexterous works found | IIL feedback type, plus a keyword bibliometric of 326 papers | three mentions in 687 lines, no section | Table 1, 15 commercial hands, manufacturer figures | no metric defined, no benchmark table | tactile feedback, long-horizon tasks, generalisation, human-feedback interface |
| `nine_physics_engines_review_2024` | 2024 | nine physics engines for RL research, scored on documentation and usability | 13-axis feature and usability matrix, Table II, plus citation-count popularity | none. MARL readiness is the multi-agent axis | none. Ant and humanoid RL bodies are the running examples | no benchmark of its own. Throughput claims are second-hand | no cross-engine MARL performance comparison exists in the literature |
| `contact_models_comparison_2023` | 2023 | LCP, CCP, RaiSim and NCP contact models re-implemented in one framework and ranked | contact model by solver, with the physical property each one violates | none | one Allegro hand as a benchmark system, a ball dropped into it | NCP criterion, self-consistency against a 1e-5 s reference, iteration cost | no fully satisfactory contact model, and gradients through simulation artifacts are unexplored |
| `firoozi_foundation_models_2023` | 2023 | foundation models in robot decision-making, perception and embodied AI | background, robotics, and robotics-adjacent papers, then by application | none, zero occurrences | none. Parallel-jaw end effectors throughout | none defined. Benchmarking appears as a reproducibility problem | data scarcity, variability, uncertainty, safety, real-time inference, and simulators that neglect contact physics |
| `zhao_sim2real_survey_2020` | 2020 | sim-to-real transfer in deep RL, eight pages, 21 works tabulated | zero-shot, system identification, domain randomisation, domain adaptation, learning with disturbances, simulator choice | none, zero occurrences | two cited hand works, no hand table | no metric defined, no trial count, no success rate | domain randomisation has no formal account, and domain adaptation assumes matched feature spaces |
| `piazza_century_2019` | 2019 | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* |
| `physics_engine_comparison_2015` | 2015 | five engines on one shared model: speed, self-consistency, conservation, grasp stability | none. Four test systems, one comparison per test | none | one 35-DoF rig modelled on the Shadow Hand | largest timestep that holds a grasp, and a speed-accuracy Pareto curve | restricted feature subset by design, and the authors are MuJoCo's developers |
| `roa_suarez_grasp_quality_2015` | 2015 | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* |
| `ma_dollar_dexterity_2011` | 2011 | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* | *PDF fetched 2026-09-18 after the note was written, no note read from it* |
| `okamura_overview_2000` | 2000 | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* | *source not obtained* |

*14 rows, one per corpus entry of class `survey`, 3 of which could not be obtained and are entered as such, and 1 of which was fetched too late to be read into a note. Every filled cell is read from `papers/notes/<key>.md` and is checked against a quotation from that note by `tools/make_survey_table.py`. A cell whose evidence has gone from the note prints empty rather than printing an unchecked claim. The columns record what each work covers, not how well, and a blank cell in `bimanual covered` or `hardware covered` is a scope decision by its authors rather than a failure.*


Table 10's last rows carry the cost of the corpus. `okamura_overview_2000`, `piazza_century_2019`
and `roa_suarez_grasp_quality_2015` are behind publisher paywalls with no author-hosted copy found
on 2026-09-18, and `bicchi_hands_2000` is in the same position with no row at all.
`ma_dollar_dexterity_2011` is a different case. The fetch that failed when its note was written
succeeded afterwards, so a seven-page PDF is on disk with a recorded hash, and no note has been
read from it. All five are cited by metadata only and nothing in this survey describes their
contents. The open chapter `bicchi_grasping_chapter_2001` overlaps the paywalled Bicchi paper
without being identical to it, so it is quoted in its own right.
