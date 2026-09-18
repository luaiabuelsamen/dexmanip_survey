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
