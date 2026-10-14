# 6. Bimanual dexterous manipulation

Two hands are not two instances of the same problem. They share one object, they can collide with
each other, and the action space doubles, so neither the hardware result nor the policy carries
over from one hand. Counting the work is the first difficulty, because the widest count, the 53
papers whose robot has two end effectors, is not a count of bimanual dexterous manipulation at
all. Thirteen of those put no dexterous hand on the robot: five are parallel-jaw throughout
(`aloha_act_2023`, `rdt1b_2024`, `egomimic_2024`, `h_rdt_2025`, `umi_2024`), four name no hand and
run grippers on every embodiment (`pi0_2024`, `pi05_2025`, `pistar06_2025`,
`diffusion_policy_2023`), two report every bimanual number on grippers and show five-fingered hands
only qualitatively (`gemini_robotics_2025`, `gemini_robotics_15_2025`), and two name no end
effector anywhere (`helix_2025`, `groot_n16_2025`). Three more run a gripper on one embodiment and
a hand on another (`ace_teleop_2024`, `dp3_2024`, `open_television_2024`). The list of exclusions is in Appendix A, so
the denominator can be audited rather than taken on trust.

: the method papers whose notes place a learned
closed-loop controller on two multi-fingered hands. It is the 53 less those 16; less two static
grasp-synthesis methods, `bimangrasp_2024` and `bidexgrasp_2026`; less three systems with no
learned policy, `castro_sap_contact_2021`, `dexteleop0_2026` and `pang_global_planning_2022`; and
less four papers where no learned policy holds both hands: `omnih2o_2024`, whose fingers are mapped
open-loop from the Vision Pro and sit outside its 19-DoF policy; `okami_2024`, whose headline
pipeline is open-loop retargeting with a learned policy only in a side experiment;
`dexdeform_2023`, a skill model refined by trajectory optimization rather than a closed-loop
controller; and `omnigrasp_2024`, a simulated human body with no bimanual task.
`dexterous_handover_2025` never enters, because its entry records one hand. Benchmarks and datasets
are outside the 28 by class, `bidexhands_2022`, `bench2dex_2026` and `robopianist_2023` being
benchmarks and `rp1m_2024` and `humanoidgen_2025` datasets; they are quoted here as evidence and
never counted. Every paper below runs two multi-fingered hands unless said otherwise.

## 6.1 Coupling, roles and collision

When both hands hold the same object, the object closes a kinematic loop between them. Neither
hand can move without changing what the other must do. `bidexgrasp_2026` reports that the coupled
objective "often yields imbalanced solutions, where one hand dominates stability while the other
contributes marginally." `artigrasp_2023` reports simulation speed scaling "roughly quadratically
with the number of contacts," and trains each hand alone before pairing them.

Role asymmetry is an assumption most of these systems make silently. `bidexhd_2024` states it outright:
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

The action space doubles and the observation grows faster: a two-hand benchmark carries action
vectors in the tens and observations in the hundreds of dimensions, and a recent generalist emits
a chunk of arm joints, end-effector poses, hand joints and fingertips together. What the larger
vector does not carry is any statement of who does what. The usual answer is one scalar reward
summed over both sides, and the cost is a compounding failure rate: where success requires both
hands to succeed, `maniptrans_2025`'s rate falls by about a third from single-hand sequences to
bimanual ones.

## 6.2 Coordination architectures

{{figure:fig5_bimanual}}

Figure 5 sets the four mechanisms side by side. Every one of the 28 carries exactly one
architecture, read from its note: one policy over both hands, a network per hand, leader and
follower, or a note that does not say. The fourth panel is not a fourth architecture but the
relative frame, and it is the same single paper as the third.

Twenty-one of the 28 put one policy over both hands, which is three quarters of the set: the
trackers and tracking-adjacent methods `dexmachina_2025`, `dexman_2025`, `maniptrans_2025`,
`objdex_2024` and `humanplus_2024`; the reinforcement-learning tasks `dexpbt_2023`,
`twisting_lids_2024`, `eureka_2023`, `pianomime_2024` and `humanoid_sim2real_recipe_2025`; the
demonstration pipelines `bidex_teleop_2024`, `dexcap_2024`, `dexwild_2025`, `dexmimicgen_2024`,
`hato_visuotactile_2024` and `humanoid_policy_human_policy_2025`; and the generalist policies
`gr_dexter_2025`, `groot_n1_2025`, `dexora_2026`, `metis_2025` and `egoscale_2026`. In every one
of them a single network takes a concatenated two-hand observation and emits a two-hand action.
Two papers do not say which they are, `bunny_visionpro_2024` and `deximit_2026`, whose notes
describe the rig and the data pipeline but never the policy's own decomposition. The concentration
is not the outcome of a comparison that was won.

Four of the 28 give each hand its own network, and the two papers that compare the choice
disagree. `bidexhands_2022`, a benchmark entry and so outside the 28, ships the MARL baselines and
finds PPO over the full observation beats HAPPO and MAPPO "in most cases," with the gap narrowing
on tasks that need both hands, because PPO "can use all observations" where MARL sees only part.
`bidexhd_2024` concludes the opposite. Its independent PPO teachers score 74.59 percent stage-two
tracking rate on trained tasks against 53.88 for a centralised policy over both observations. Both
are simulation only, on different tasks and hands, so neither settles it. `artigrasp_2023` trains
one PPO policy per hand, and `dynamic_handover_2023` and `dydexhandover_2025` use MAPPO with one
agent per arm-hand system.

One paper assigns explicit leader and follower roles, and it is the same one that expresses its
policy in a relative frame. `asymdex_2024` gives the dominant hand full finger and wrist control,
restricts the facilitating hand to a base pose, and writes both the dominant hand and the object
in a frame attached to the object the other hand holds, which halves the observation and the
action. It is also the only paper here that ablates the two mechanisms separately, and neither
works without the other: relative frames without asymmetry and asymmetry without relative frames
both collapse to near zero where the full method succeeds most of the time. Its real rig pairs an
Allegro with a cheaper hand because only one Allegro was available, so the roles are confounded
with the hardware. Two other papers use a relative quantity without giving either hand a role, one
appending the inter-hand pose to its observation and one applying a shared transform to both arms
while generating data, which is the mechanism offline rather than in a policy.

One architecture carries three quarters of the field, and the choice behind
it has been compared twice, with opposite outcomes, and ablated once. What would close it is a single
handover task run on three architectures with the same hand and the same seeds, reporting giver and
receiver returns separately rather than one shared number.

## 6.3 Benchmarks, datasets and the shared axes

Two purpose-built bimanual dexterous suites exist in the corpus, four years apart.

The two bimanual benchmarks in the corpus trade coverage against measurement, in opposite
directions. `bidexhands_2022` is 20 tasks on two Shadow Hands in Isaac Gym, ordered by the
infant age at which humans acquire the skill, at 2048 environments and a reported 30,000-plus
FPS. Its measurement discipline is weaker than its coverage. It reports reward and normalized
score, never a success rate. Its only success flag in code tests the object-to-goal distance
against 3 cm, which ignores orientation and exists only in the four catching tasks. Any success
rate later work attributes to Bi-DexHands comes from that flag or its own definition.

`bench2dex_2026` is the more instrumented of the two, running 26 long-horizon tasks across 12
arm-and-hand embodiments with thousands of teleoperated demonstrations in eight modalities,
including a ray-cast tactile image that maps every hand geometry into one representation. Its
headline result is the gap between conditions rather than the leaderboard: the matched leader takes
about half the rollouts and falls to a fifth under combined perturbation, which compresses the
field until the ranking no longer holds. Tasks are not crossed with embodiments, so no contrast
isolates the hand, and the authors state that their hand and tactile models are not calibrated
against matching physical hardware.

Ten papers in this corpus are bimanual datasets, five of them two-hand interaction capture, and
their annotations are where the contact problem first appears. `arctic_2022` deliberately labels
over-shooting vertices as in contact, so its ground truth records interpenetration as contact.
`taco_2024` fits its sequences under an attraction loss and a penetration loss that the paper says
trade against each other. `oakink2_2024` is the only one publishing a penetration figure for its
own annotations, at a mean depth of a few millimetres. The two largest egocentric sets publish none
at all (`hot3d_2024`, `gigahands_2024`). Those five feed most of the physics-based tracking work in this section, so an
interpenetrating reference is where several of these pipelines start.

Table 7 carries the bimanual papers on the same columns as every other method here, and three of
those columns are worth reading together.

Real trials. `asymdex_2024` reports 20 per task, `hato_visuotactile_2024` 10 per condition,
`dexmimicgen_2024` 20 on a Fourier GR1 and `bidexgrasp_2026` 260 across 30 objects.
`maniptrans_2025` reaches real Inspire hands by open-loop replay with no trial count and no
success rate. Seven of the 28 have no real robot at all: `artigrasp_2023`, `bidexhd_2024`,
`dexmachina_2025`, `dexman_2025`, `dexpbt_2023`, `dydexhandover_2025` and `pianomime_2024`. The
two piano papers outside the denominator, `robopianist_2023` and `rp1m_2024`, are simulation-only as
well.

Penetration. Most bimanual papers read "not addressed." `bimangrasp_2024` gates on it, failing any
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

Whether the two hands optimize the same objective is usually left implicit.
`dynamic_handover_2023` states one formula, r = r_dis + r_linvel + r_torque, and never says
whether thrower and catcher receive different decompositions of it. `dydexhandover_2025` is
explicit that they do not: "Both hands share aligned objectives, forming a fully cooperative
relationship," with one weighted sum feeding both agents. Only the thrower gets an extra KL
regulariser toward a policy pretrained on human throws, which constrains style and not role.

The third case is weaker still. In `dexterous_handover_2025` only the receiver is learned. The
giver is a UR5e with an Allegro hand that "holds the object without moving during the whole
episode." There is one agent, one reward and no second policy, its entry in Table 7 accordingly
records one hand, and it is one of the papers the 28 excludes. The 94 percent often attached to this
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
bimanual controller in the corpus measures or penalizes hand-hand penetration during a rollout.
`pianomime_2024` ships a flag that turns inter-hand collision off in the physics.