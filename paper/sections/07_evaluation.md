# 7. Evaluation: how we would compare these methods

## 7.1 What the field reports, and why the numbers do not compare

Of the 112 method rows in the corpus, 89 report a real-robot experiment, 22 do not and one row is
unsettled: 79 percent of all 112 rows, or 80 percent of the 111 the note settled. Among those 89,
70 state how many real trials produced the headline number, which is 79 percent of them and 62
percent of all 112 method rows. The 89 is the denominator that belongs to this statistic: the 22
rows with no real robot cannot state a real trial count, and counting them as silent turns a
definitional impossibility into a reporting failure. Thirty-nine rows state a count of unseen test
objects, 35 percent. Ninety-eight state how a rollout is scored, 88 percent. Sixty-two released
code and 46 did not, with four rows unsettled: 55 percent of all rows, or 57 percent of the 108
the note settled. Figure 6 draws these six shares, each against the denominator that belongs to
it.

{{figure:fig6_reporting}}

**These are counts of what this survey captured, not of what papers reported, and every one is a
floor.** A row in `corpus/rows` holds a scalar. A paper that reports ten trials on each of nine
tasks, or a scoring rubric instead of a threshold, or a count spread over four tables, has nothing
the extraction can reduce to one integer, so it produces a null — and a null is then
indistinguishable from a paper that said nothing. The bias runs one way: every miss converts a
reporting paper into a silent one, and the survey's argument is that the field reports badly, so
the artefact flatters the argument. Section 5.8 makes the same disclosure about the paper/code
count, subtracting the 13 disagreements that are limitations of this survey's own parsing
before declaring which number to quote, and the coverage statistics above need it more.

So the nulls were audited by hand against the notes they came from, and the numbers above are the
audited ones. Of the 34 method rows with a real robot and no trial count, 15 had the count written
in their own note — `pi0_2024` at ten trials per task, `rdt1b_2024` at 139 across seven tasks,
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
per-cell — ten trials on each task, twenty per condition, five per object — and others are grand
totals over every cell, so the field now carries a `real_trials_kind` beside every value and the
distributions are quoted separately. The 39 per-cell counts run from 5 to 100 with a median of 15
and quartiles at 10 and 20; the modal cell is 10 trials, in 16 rows, then 20, in 12. The 24 grand
totals run from 12 to 750 with a median of 110. Pooling the two gives a median of 20 and a range
of 5 to 1287, and that pooled figure is the one an earlier draft of this section quoted; it
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
stated count is 20 in 2024, 22.5 in 2025 and 20 in 2026; before 2024 the per-year medians rest on
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
no criterion, ten have no success predicate at all — they report radians rotated or time-to-fall
and never define a success, which is a fact about the paper rather than a gap in this survey — and
four are unsettled by the note. What the audit found in the other 19 was mostly not a threshold:
eleven score by rubric or staged partial credit, five judge binary completion against a task
description by eye, two defer to a benchmark's own definition, and exactly one, `pistar06_2025`,
states a verbatim numeric threshold. A rubric is a milder failure than silence and a worse one
than a threshold, because it is reproducible inside a lab and not across two.

## 7.2 The axes that matter

Seven quantities dissociate in the published data, so they have to be reported separately.

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
settled address it, 11 percent, with 16 rows unknown; Section 7.3 takes them apart.

**Sample and wall-clock cost.** Thirty-one of 112 rows state a parallel environment count and 18
a simulated episode count. `robopianist_2023` is the exception, at 5 million samples per song and
roughly 5 hours per run on four Tesla K80 GPUs.

**Real-robot transfer.** Simulated rank order is not real rank order. `autoeval_2025` scores
Open-π0 on put-eggplant-in-sink at 6 of 50 in SIMPLER and 47 of 50 on the real WidowX.
`suresim_2025` states the limit directly: "the simulation-to-real gap precludes rigorous
statistical inferences about real-world outcomes from simulation results alone".

**Reproducibility.** 62 rows released code that could be parsed against the paper, and 38 of the
112 rows record a disagreement of some kind between the paper and that code. All 38 released
code, so the raw rate among code-releasing rows is 61 percent. That raw rate is not
the finding, because the 38 are not one thing. Section 8.1 classifies them: 10
contradictions, 13 limitations of this survey's own parsing, 8
components never released, 4 version skews and 3
inconsistencies internal to a paper. Only the contradictions are a finding about the work rather
than about this survey, so 10 of 62 code-releasing rows, which is
16 percent, is the figure this section and Table 8 use.
`physhoi_2023` is the clearest of the 10. It lists a non-zero object-orientation
weight for GRAB in Table 4, and its released `compute_humanoid_reward` hard-sets that orientation
error to zero, so the reward that produced the published numbers tracked the object in position
only.

## 7.3 Physical plausibility as a first-class metric

Eleven method rows handle interpenetration in any form: three penalise it, three measure it, five
constrain it. The denominator is 96, not 112, because the `penetration` field is null for 16 rows,
and a null there means the note did not settle the question, not that the paper ignored
penetration. Eleven of 96 is 11 percent. Six of the eleven are grasp synthesisers or trajectory
optimisers, namely `bidexgrasp_2026`, `bimangrasp_2024`, `deximit_2026`,
`pang_global_planning_2022`, `toporetarget_2026` and `unidexgrasp_2023`, and
`castro_sap_contact_2021` is a contact model rather than a controller. That leaves four
closed-loop policies in the whole corpus: `clutterdexgrasp_2025`, `dexmachina_2025`,
`dextrack_2025` and `teledexter_2026`.

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
constrains penetration during retargeting with a 1 mm soft tolerance and a 30 mm hard bound, and
it reports two numbers on 25 ContactPose grasps: a maximum penetration of 1.07 mm and 0.00 percent
of frames above 2 mm, against 22.22 mm and 96 percent of frames for its GeoRT baseline. Then a PPO
controller tracks those references, and its four reward terms and its five termination criteria
govern object pose, link position, joint error and action smoothness, never penetration. The
constrained quantity is the reference, and the rollout is not re-measured.

Definitions are not shared either. `grab_2020` estimates contact by proximity, because "contact
cannot be directly observed", with a 4.5 mm tolerance, and reports that "'Use' grasps have 3.25 ±
0.68 mm average penetration", without saying whether 3.25 mm is a maximum, a mean or a median.
`oakink_2022` supplies the fullest published vocabulary: penetration depth, solid intersection
volume and simulation displacement. Its Table 3 scores the GRAB GrabNet split at 2.53 cm
penetration depth, against GRAB's own 3.25 mm. The two differ by a factor of about eight, and
neither source states its distance function precisely enough to reconcile them — and the two are
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

## 7.4 Statistics

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
of roughly 0.6 to 0.7, and nothing at all at a correlation near zero; the 25 percent figure is the
better of its two reported settings, the DP case at ρ = 0.702. Its decision rule is exact:
combining helps only when the rectifier variance is below the variance of the real evaluations.
`beyond_binary_success_2026` gives the largest saving. On the LBM rubrics its sequential test on
graded scores cuts simulated evaluation by about 70 percent and hardware by about 45 percent, 286
trials against a nominal 500, with per-task decisions landing in 12 to 36 paired trials. On
RoboArena's data a 30-point gap on continuous progress scores reaches significance in 18 trials,
while a 20-point gap on binary success needs about 80.

## 7.5 A proposed protocol

Every count below is printed by `tools/make_eval_tables.py --derive`, and each axis is derived for
the statistic that axis actually reports: a single rate takes a Wilson half-width, a matched
comparison takes McNemar, a ratio takes the standard error of the log ratio, a correlation takes
the Fisher-z interval.

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
the unit is a matched pair and the count follows McNemar, which depends on the discordance rate —
the share of initial conditions on which the two policies disagree — and not on the two rates
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
decision in 12 to 36 paired hardware trials in `beyond_binary_success_2026`; at 30 rollouts a
continuous score already carries a half-width of ±0.36 standard deviations, which is why a graded
score can stop where a binary one cannot. A cell that stops early does not report a Wilson
interval. Optional stopping breaks the coverage of a fixed-n interval, which is the reason
`beyond_binary_success_2026` and `suresim_2025` use anytime-valid betting intervals rather than
Wilson, so Table 8 asks a cell run to a fixed 100 for a Wilson interval and a cell stopped early
for a confidence sequence, and never for both. Intervals are also marginal rather than
simultaneous. Table 8 has seven axes and Table 9 twelve methods; at 84 independent 95 percent
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
within-object trials are not; it is the right order of magnitude and the assumption belongs in the
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
one, since those differ by about 0.11 in correlation; both limits come within 0.05 of the estimate
only at about 457 pairs. Table 8 states which of the two decisions each count supports rather than
leaving a reader to assume the larger one.

{{table:table8_protocol}}

## 7.6 Table 9, an empty results matrix

The rows are the 12 most-mentioned dexterous-hand policy methods in the corpus, and the rule is
the one `tools/make_eval_tables.py` implements, stated here in the same words. A candidate is a
method row with a non-null `hand`; its hand string must not contain "parallel" or "gripper"; it
must carry at least one paradigm tag that produces a closed-loop policy and must not carry
`teleop-system`, because an interface is scored on latency and operator effort rather than on a
policy's success rate; and its name must be at least four characters, so that a short string does
not match everything. Candidates are then scored by the number of other corpus papers whose parsed
text in `papers/md` contains the name, and the top 12 by count, ties broken by key, are the rows.

Two corrections to that ranking are worth stating, because both changed it. The match is on a
whole word. Under the bare substring test an earlier version used, "UniDex" matched inside
"UniDexGrasp" and "UniDexGrasp++", and `unidex_2026` — a 2026 paper — sat sixth in a ranking over
a corpus written mostly before it, on 34 mentions that belonged to a different work; as a whole
word it has 3 and it is not in the table. And the interface rule is now applied to every row that
carries the tag rather than only to rows that carry nothing else, which drops `anyteleop_2023` at
34 mentions, `dime_2022` at 28 and `holo_dex_2022` at 23, along with `dexpilot_2020`, which the
earlier prose already excluded by hand. The mention counts are printed under the table so a reader
can audit them.

The ranking is not one quantity even so. A method's name is taken from the first line of its note,
which yields an acronym for some works and a full title for others, and a title is matched mostly
inside reference lists while an acronym is matched in running text. Those have different base
rates, so the table marks which kind each row was matched on and the two kinds are not comparable
with each other. Mention counts are counts of mentions and not of use, as `METHOD.md` records.

Every cell is empty. This survey re-ran nothing, and no cell can be filled at the denominator
Table 8 asks for. `dextreme_2022` comes closest and is the reason the claim is stated that
narrowly: it reports a criterion, a trial count and an interval — object orientation within 0.4
rad of target, 27.8 ± 19.0 average consecutive successes with the ± a 90 percent confidence
interval — on 10 trials. Table 7 is not a counter-example either, though it looks like one: it
carries `trials`, `unseen obj`, `penetration` and `code` columns for all 112 method rows,
including all 12 of these. Table 7 records what each method reported. Table 9 asks for what Table
8 defines — a value with an interval, a stated denominator and a criterion written before the run
— and none of Table 7's values meets that. The first row of Table 9 is a worked example so that
the format of a cell is unambiguous; every number in it is fabricated and labelled as such.

{{table:table9_matrix}}

## 7.7 What would have to be true

The bill comes first. Per policy and per task the protocol asks for 57 matched trials on the
anchor set, which is the paired count from §7.5, and 100 on the unseen-object set, at 20 objects
and 5 trials each, with robustness and plausibility absorbed by simulation. A two-policy
comparison on three tasks is then 342 real rollouts on the matched set and 600 on the
unseen-object set, 942 in all, and at one minute per rollout including the reset that is about 16
hours of robot time, before failed resets, repairs and scoring. The same bill computed from the
independent-arm count, which an earlier draft used, was 1200 rollouts and 20 hours; the pairing
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
Simulators would have to expose penetration to code outside the reward, which Table 4 records that
only some do. And the comparison would have to be sequential, because the savings in
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
physical bound.
