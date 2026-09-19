# 8. Gaps

## 8.1 What opening the repositories showed

This is a result rather than a gap, and a result about publishing practice in robot learning: the
dexterous corpus is its sample, not its subject.

Sixty-two method rows released code that could be parsed against the paper, and 38 carry
a recorded discrepancy. The classification is the finding: nine contradictions, where the paper
states one value and the shipped code demonstrably states another; thirteen limits of this
survey's own parse, which captured signatures or a truncated body rather than the component; eight
cases where the code was never released; four version skew; four inconsistencies inside a paper
with no code involved. Nine is the number to quote, eight at high confidence, with `penspin_2024`
held at medium against an innocent reading a direct code read would settle.

The first count was sixteen. An adversarial re-reading withdrew six of them outright and narrowed
a seventh to the half that stands. The six were `maniptrans_2025`, `eureka_2023`,
`open_television_2024`, `dexmachina_2025`, `artigrasp_2023` and `graspxl_2024`: two refuted by the
accused repository's own README, two resting on reward code never in the parse, one charging the
code with structure the paper prints, one against a paper with no reward function. The seventh is
`dexpbt_2023`, where the domain-randomisation half of the charge is withdrawn and the zeroed reward
term stands, so that row is still a contradiction and its withdrawal takes nothing off the count.
That left ten, and ten held until the letters to the authors were drafted.

Writing to `omnih2o_2024` meant reading its accusation again before sending it, and reading it
again is what broke it. Four of its five reward-weight comparisons match the paper's own table to
the digit once a systematic ×1.25 curriculum factor is applied, and only the stumble weight
differs, by a factor of about a million, which reads as a typo signature in the paper's own table,
not a policy trained on a different objective. The work's hands are also driven open-loop from a VR pose,
outside the policy and outside the reward, which made it a poor fit for a reward census in a
dexterous-manipulation survey regardless of the weight. The charge is withdrawn and the row moves
to an internal inconsistency, which is where the count above sits it. **The survey has now
withdrawn eight accusations in total: seven of them under adversarial review, and the eighth at
the point of writing to the authors, because someone sat down to write the letter and looked at
the evidence again.** `penspin_2024` is narrowed rather than withdrawn, the same way the charge
against `dexpbt_2023` was narrowed above: the half of it that said the released code disables the
paper's tactile channel is dropped, because the configuration read has proprioception-only
observation dimensions consistent with the student policy rather than the oracle, and the paper
never claims the student has tactile input; the half that stands is that the appendix states a
randomised disturbance force and the shipped configuration sets its scale to zero. Each retraction
and narrowing is recorded in its row's `mismatch_review` field: a survey that names people should
carry its corrections beside its accusations, in public and not just in the corpus.

`physhoi_2023` survived every attempt to break it. Table 4 weights object rotation at 0.1 for
GRAB, and the released `compute_humanoid_reward` sets the object rotation and rotation-velocity
errors to `torch.zeros_like`, unconditionally, so the dataset exemption the paper states does not
cover it. The reward behind its 95.4 percent tracked the object in position only, and its own
position-only success criterion could not have caught that. `robot_synesthesia_2023`, at the other
end, prints its six weights as symbols and released nothing, so that objective exists in no
machine-readable form. `hora_2022` alone discloses its own gap, in its README.

Nine is a floor, since forty-six method rows released nothing to check and four more are
unsettled. What would close it: publish
the reward table generated from the released config at a named commit, so a reviewer diffs two
artefacts instead of reading two documents.

## 8.2 No closed-loop policy records interpenetration for its own rollouts

Eleven method rows handle interpenetration at all, of the ninety-six whose notes settle the
question, and only four of them are closed-loop policies. Every one of the eleven sits on the
reference side of the reference-versus-rollout split, scoring a pose or a trajectory before
execution rather than the behaviour that followed. The gap is therefore specific to learned
closed-loop control rather than general. Grasp synthesis and hand-object reconstruction report
penetration depth and intersection volume comparatively, and `oakink_2022`, `bimangrasp_2024`,
`bidexgrasp_2026` and `toporetarget_2026` do so within this corpus. What none of them scores is the
behaviour a trained policy produced. The engines are not the obstacle:
IsaacGymEnvs ships a task that computes a per-environment maximum interpenetration depth in Warp
and gates its policy update on a 1 mm threshold, and `tactile_genesis_2026` offers two
penetration-depth backends on Genesis geometry as sensors. The depth is computable by anyone from
poses and meshes, and we found no paper that reports it for a dexterous rollout. What would close it: maximum and mean
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
48 reinforcement-learning rows that state one. So the generalist policies that do touch a hand run
it at roughly a third of the actuation the reinforcement-learning literature assumes. The stronger
claim, that no generalist reaches the 16-to-24 band, holds over those five stated counts and no
further, which is what section 5.5 says. `gr_dexter_2025` and `egoscale_2026` name hands at 21 and
22 actuated degrees of freedom, so they do reach the band on paper, and neither settles whether
the reported evaluation ran on that hand. What would close it: one
dexterous-hand task in the standard generalist suite, with the hand's DoF and vendor beside the
number.

## 8.5 The hands that can be bought go unused

Eight documented hands that can be bought or built from published designs take zero method rows
between them: Unitree Dex5, Tesollo DG-5F, Proception ProHand, ORCA, RUKA, Ruka-v2, BiDexHand and
DexHand. Only three of the fifteen simulator rows name a real hand at all, and the ones they do
name are the field's defaults. 19 of the 33 hands in Tables 2 and 3 appear in no method row, but 11 are neither
sold nor open and appear in none for that reason, so 33 is not the denominator for a software-lag
claim. The rule that decides used from unused is one regular expression per hand against the
method rows' own hand field, in `tools/hand_usage.py`, so the partition can be recomputed rather
than argued about. `bench2dex_2026` compares 12 hands and `dexverse_2026` six without stating a DoF count for
any. What would close it: a conformance suite for hand models, one URDF or MJCF per hand, with
fixed joint-limit, mass and collision checks and a published pass or fail per engine.

## 8.6 Bimanual work runs on one coordination architecture, and it has been ablated once

Twenty-one of the 28 rows that Section 6 counts as putting a learned closed-loop controller on two
multi-fingered hands run one policy over a concatenated two-hand observation. That choice has been
compared twice, with opposite outcomes, and ablated once: `asymdex_2024` scores 0.7701 on Block in
cup over five seeds, against 0.1086 with relative frames but no role asymmetry and 0.0164 with
asymmetry but no relative frames. All three handover
papers share one reward across giver and receiver. What would close it: one handover task, three
architectures, the same hand and the same seeds, with separate giver and receiver returns.

## 8.7 Human data does not port across hands, and the map is usually unstated

Fifty-three method rows use human data and name 45 distinct hand strings between them. Twenty
appear in Table 6 with a stated retargeting objective. The other 33 do not say how the human
motion reached the hand, and the stated objectives do not converge, from a fingertip
keypoint-vector energy in `anyteleop_2023` to a per-joint regression from exoskeleton encoders in
`dexumi_2025` to no retargeting at all in `egozero_2025`. More correspondence is not better:
`objdex_2024` retargets the wrist only and beats both finger-joint and fingertip mapping, and its
added fingertip-matching reward "does not yield benefits and even leads to lower performance".
What would close it: a retargeting benchmark in TopoRetarget's form, reporting contact precision,
contact alignment, maximum penetration and share of frames past 2 mm, per hand and per dataset.
