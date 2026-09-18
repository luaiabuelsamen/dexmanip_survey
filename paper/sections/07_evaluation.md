# 7. Evaluation: how we would compare these methods

## 7.1 What the field reports, and why the numbers do not compare

Of the 110 method rows in the corpus, 87 report a real-robot experiment, which is 79 percent.
Only 55 of those 110 state how many real trials produced the headline number, which is 50
percent. Thirty-two state a count of unseen test objects, 29 percent. Seventy-nine state a
success criterion, 72 percent. Sixty-one released code, 55 percent. Figure 6, generated as
`paper/figures/fig6_reporting.svg`, draws these five shares from `corpus/rows` against the same
denominator. A bar there is evidence that a quantity was stated, not that the work handled it
well.

{{figure:fig6_reporting}}

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

{{table:table8_protocol}}

## 7.6 Table 9, an empty results matrix

The rows are the 12 most-mentioned dexterous-hand policy methods in the corpus, ranked by how
many other corpus papers name them in their parsed text. Parallel-jaw work is excluded, and so
is any row whose only contribution is a teleoperation interface, which drops `dexpilot_2020`.
Mention counts are counts of mentions and not of use, as `METHOD.md` records, and the ranking is
recomputed by `tools/make_eval_tables.py` rather than fixed by hand.

Every cell is empty. This survey re-ran nothing, and no cell can be filled from a published
number, because no number in the corpus carries the interval, the denominator and the criterion
that Table 8 asks for.

{{table:table9_matrix}}

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
