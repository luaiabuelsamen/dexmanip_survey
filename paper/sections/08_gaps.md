# 8. Gaps

## 8.1 What opening the repositories showed

This is a result rather than a gap, and a result about publishing practice in robot learning: the
dexterous corpus is its sample, not its subject.

Sixty-two method rows released code that could be parsed against the paper, and 38 carry
a recorded discrepancy. The classification is the finding: ten contradictions, where the paper
states one value and the shipped code demonstrably states another; thirteen limits of this
survey's own parse, which captured signatures or a truncated body rather than the component; eight
cases where the code was never released; three version skew; three inconsistencies inside a paper
with no code involved. Ten is the number to quote, eight at high confidence, with `penspin_2024`
and `omnih2o_2024` held at medium against innocent readings a direct code read would settle.

The first count was sixteen. An adversarial re-reading withdrew seven accusations —
`maniptrans_2025`, `eureka_2023`, `open_television_2024`, `dexmachina_2025`, `artigrasp_2023`,
`graspxl_2024`, and the domain-randomisation half of the charge against `dexpbt_2023` — two
refuted by the accused repository's own README, two resting on reward code never in the parse, one
charging the code with structure the paper prints, one against a paper with no reward function.
Each is recorded in its row in a `mismatch_review` field: a survey that names people should carry
its retractions beside its accusations.

`physhoi_2023` survived every attempt to break it. Table 4 weights object rotation at 0.1 for
GRAB, and the released `compute_humanoid_reward` sets the object rotation and rotation-velocity
errors to `torch.zeros_like`, unconditionally, so the dataset exemption the paper states does not
cover it. The reward behind its 95.4 percent tracked the object in position only, and its own
position-only success criterion could not have caught that. `robot_synesthesia_2023`, at the other
end, prints its six weights as symbols and released nothing, so that objective exists in no
machine-readable form. `hora_2022` alone discloses its own gap, in its README.

Ten is a floor, since fifty method rows released nothing to check. What would close it: publish
the reward table generated from the released config at a named commit, so a reviewer diffs two
artefacts instead of reading two documents.

## 8.2 Nobody records interpenetration for their own policy's rollouts

Eleven method rows handle interpenetration at all, of the ninety-six whose notes settle the
question, and only four of them are closed-loop policies. The engines are not the obstacle:
IsaacGymEnvs ships a task that computes a per-environment maximum interpenetration depth in Warp
and gates its policy update on a 1 mm threshold, and `tactile_genesis_2026` offers two
penetration-depth backends on Genesis geometry as sensors. The depth is computable by anyone from
poses and meshes; nobody reports it for a dexterous rollout. What would close it: maximum and mean
penetration depth over the evaluation rollouts, on a dense surface sample, from a measure the
policy never optimised.

## 8.3 The evaluation-methodology literature contains no dexterous hand

Seven corpus rows are evaluation protocols, a small denominator, and not one uses a dexterous
hand: `suresim_2025` runs a parallel-jaw gripper and the other six state no hand.
`kress_gazit_policy_eval_2024` sets no minimum trial count and no confidence-interval width. What
would close it: run the Table 8 protocol once, on one in-hand reorientation task with one 16-DoF
hand, and release the rollouts as the first row of Table 9.

## 8.4 Generalist policies run on a fraction of the degrees of freedom

The gap is size, not absence. Eighteen rows carry the generalist tag. Fourteen of them settle
whether the reported evaluation ran on a multi-fingered hand, and eight of those fourteen did.
The remaining four do not say, which is itself the smaller half of this gap. Of the eight, five
state the hand's degrees of freedom: four at 6 and one at 12. The median is 6, against 16 over the
44 reinforcement-learning rows that state one. So the generalist policies that do touch a hand run
it at roughly a third of the actuation the reinforcement-learning literature assumes. The stronger
claim, that no generalist reaches the 16-to-24 band, rests on those five stated counts alone, and
`gr_dexter_2025` and `egoscale_2026` are excluded because neither settles the question. What would close it: one
dexterous-hand task in the standard generalist suite, with the hand's DoF and vendor beside the
number.

## 8.5 The hands that can be bought go unused

Seven documented hands that can be bought or built from published designs take zero method rows
between them: Unitree Dex5, Tesollo DG-5F, ORCA, RUKA, Ruka-v2, BiDexHand and DexHand. Only three
of the fifteen simulator rows name a real hand at all, and the five named are the field's
defaults. Nineteen of the 33 hands in Tables 2 and 3 appear in no method row, but 14 are neither
sold nor open and appear in none for that reason, so 33 is not the denominator for a software-lag
claim. `bench2dex_2026` compares 12 hands and `dexverse_2026` six without stating a DoF count for
any. What would close it: a conformance suite for hand models, one URDF or MJCF per hand, with
fixed joint-limit, mass and collision checks and a published pass or fail per engine.

## 8.6 Bimanual work runs on one coordination architecture, and it has been ablated once

Nineteen of the twenty-five rows that Section 6.2 counts as putting a learned controller on two
dexterous hands run one policy over a concatenated two-hand observation. That choice has been
compared twice, with opposite outcomes, and ablated once: `asymdex_2024` scores 0.7701 on Block in
cup over five seeds against 0.0429 for the symmetric monolithic baseline. All three handover
papers share one reward across giver and receiver. What would close it: one handover task, three
architectures, the same hand and the same seeds, with separate giver and receiver returns.

## 8.7 Human data does not port across hands, and the map is usually unstated

Fifty-three method rows use human data and name 45 distinct hand strings between them. Twenty
appear in Table 6 with a stated retargeting objective; the other 33 do not say how the human
motion reached the hand, and the stated objectives do not converge, from a fingertip
keypoint-vector energy in `anyteleop_2023` to a per-joint regression from exoskeleton encoders in
`dexumi_2025` to no retargeting at all in `egozero_2025`. More correspondence is not better:
`objdex_2024` retargets the wrist only and beats both finger-joint and fingertip mapping, and its
added fingertip-matching reward "does not yield benefits and even leads to lower performance".
What would close it: a retargeting benchmark in TopoRetarget's form, reporting contact precision,
contact alignment, maximum penetration and share of frames past 2 mm, per hand and per dataset.
