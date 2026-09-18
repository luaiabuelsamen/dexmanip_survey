# 6. Bimanual dexterous manipulation

A warning first. Fifty-three corpus method rows record `bimanual: true`, and the flag says only
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
`dexterous_handover_2025` never enters, because its row records `bimanual: no`. Benchmarks and
datasets are outside the 28 by class, `bidexhands_2022`, `bench2dex_2026` and `robopianist_2023`
being benchmarks and `rp1m_2024` and `humanoidgen_2025` datasets; they are quoted here as evidence
and never counted. Every paper below runs two multi-fingered hands unless said otherwise.

## 6.1 Why two hands is not twice one hand

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

{{figure:fig5_bimanual}}

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
Two rows do not say which they are, `bunny_visionpro_2024` and `deximit_2026`, whose notes describe
the rig and the data pipeline but never the policy's own decomposition. The concentration is not
the outcome of a comparison that was won.

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
1.52 cm penetration depth. Neither number transfers, and section 5.4's re-implementation result is the same
lesson on the training side.

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
episode." There is one agent, one reward and no second policy, its row in Table 7 accordingly
records `bimanual: no`, and it is one of the rows the 28 excludes. The 94 percent often attached to this paper needs its conditions. It is
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
