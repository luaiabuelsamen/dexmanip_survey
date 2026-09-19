# 7. Evaluation, and a protocol for comparison

## 7.1 Reporting practice

Of the 112 method rows in the corpus, 89 report a real-robot experiment, 22 do not and one row is
unsettled, which is 80 percent of the 111 the note settled. Among those 89, 70 state how many real
trials produced the headline number, 79 percent of them. The 89 is the denominator that belongs to
this statistic: the 22 rows with no real robot cannot state a real trial count, and counting them
as silent turns a definitional impossibility into a reporting failure. Thirty-nine rows state a
count of unseen test objects, 35 percent. Ninety-eight state how a rollout is scored, 88 percent.
Sixty-two released code and 46 did not, with four rows unsettled, 57 percent of the 108 the note
settled. Figure 6 draws these six shares, each against the denominator that belongs to it. Every
bar is a lower bound, for the reason the next section gives. The two items flagged red there,
unseen-object count and contact or penetration handling, are the pair a reader actually needs to
compare two methods: no unseen-object count means no generalisation denominator for a success
rate, and no contact handling means no way to tell whether the hand passed through the object. They
are also the two the field states least often.

{{figure:fig6_reporting}}

**These are counts of what this survey captured, not of what papers reported, and every one is a
floor.** A structured row holds a scalar. A paper that reports ten trials on each of nine tasks,
or a scoring rubric instead of a threshold, or a count spread over four tables, has nothing the
extraction can reduce to one integer, so it produces a null, and a null is then indistinguishable
from a paper that said nothing. The bias runs one way: every miss converts a reporting paper into
a silent one, and the survey's argument is that the field reports badly, so the artefact flatters
the argument. Section 5.6 makes the same disclosure about the paper/code count, subtracting the 13
disagreements that are limitations of this survey's own parsing before declaring which number to
quote, and the coverage statistics above need it more.

The nulls behind those six shares were therefore audited by hand against the notes they came from,
and every number above is post-audit. Appendix A gives what that audit recovered and what it could
not: the counts moved by tens of rows, 19 trial counts and 4 criteria remain genuinely unsettled,
and every bar in Figure 6 is still a lower bound.

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

Nor are the criteria. `dexverse_2026` counts
PickCube a success when the cube is "lifted at least 0.20 m above its resetting height".
`bench2dex_2026` requires its terminal predicate to hold for a continuous dwell time of 0.5 s, to
reject transient contacts. `colosseum_2024` counts an episode successful "if the model completes
the task fully". `dextrack_2025` reports every success rate as a pair under two threshold sets,
which on GRAB gives 46.70 and 65.48 percent for the same rollouts. Of the 14 rows that still state
no criterion, ten have no success predicate at all. They report radians rotated or time-to-fall
and never define a success, which is a fact about the paper rather than a gap in this survey. And
four are unsettled by the note. Of the 19 criteria the audit recovered, all but one are a rubric, a
staged partial credit, a judgement by eye or a deferral to a benchmark's own definition rather than
a threshold, and exactly one, `pistar06_2025`, states a verbatim numeric one; Appendix A counts the
four kinds. A rubric is a milder failure than silence and a worse one
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
Table 4, and the reward function in the repository at the commit this survey fetched sets that
orientation error to zero, so in that file the object is tracked in position only.

## 7.2 Physical plausibility

The quantity most specific to a hand is the one closed-loop policies do not record; this section
is the funnel that narrows to zero. Eleven method rows handle interpenetration in any form: three
penalise it, three measure it, five
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
control: all eleven measure at the reference rather than at the rollout, seven of them scoring a
pose, a trajectory or a contact model before anything executes and the four that are closed-loop
policies scoring the references they were given, and we found none that reports the measurement for
rollouts of its own trained policy.

**The field behind that null was audited.** A null is worth what the search behind it is worth, and
this survey's extraction under-counted every other field it was audited against, by twenty to
forty-five percent. The 85 method rows whose contact-handling field records that the work does not
address penetration were therefore sampled: 25 of the 85, drawn at random with a fixed seed, each
read again in its own parsed source and its released repository rather than in the note the field
was written from, since the note is the artefact under suspicion. Not one of the 25 reports a
measurement of penetration depth, intersection volume or physical plausibility on its own rollouts.
Zero recoveries in 25 bounds the rows that could be hiding one at 8 of the 85 at 95 percent
confidence, so the eleven is a floor and nineteen a ceiling; had this field under-counted at even
the mildest rate the other audits found, a sample of 25 would have missed every recoverable row with
probability 0.001. The nearest miss is worth naming, because it is the one a reader might count
differently: `graspxl_2024` puts hand-object interpenetration to 35 human raters as one of four
dimensions of a single realism score, which is a judgement of its own rollouts rather than a
measurement of one, and counting it would give one recovery in 25 and a bound of 13 rows. Three near
misses recurred across the sample and none of them is a measurement of a rollout: self-collision
avoidance in a retargeter, a binary self-collision penalty in a released reward, and an engine's
de-penetration velocity left at its default. The draw, the seed and the per-row verdicts are in `reviews/penetration_audit.md`, and
Appendix A states the method and the two fields that remain unaudited.

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

The technical supplement gives the full derivation; what it concludes is the following, and every count in Table 8 is
one of these. A single reported rate takes 100 real rollouts per cell, because 93 is where the
worst-case Wilson half-width falls to 10 points and 10 points is the coarsest width at which a rate
is worth printing. A comparison is a different question and a harder one. The design is paired, so
the count follows McNemar and depends on the discordance rate rather than on the two rates alone,
and separating 50 from 70 percent at 80 percent power takes 57 matched pairs per arm at the assumed
discordance of 0.3, which is 114 rollouts against the 186 two independent arms would need.
Simulated cells take 200 episodes for a 6.9-point half-width. Perturbation axes are screened at 40
per axis, which ranks the axes and cannot establish that any one of them hurt, and certified at 101
per arm. Unseen objects resample the object rather than the trial, at 20 objects and 5 trials each,
and a 10-point claim about an object distribution needs about 93 objects. The transfer axis takes
the 100 real trials paired to 100 simulated, and about 457 pairs to separate two correlations 0.1
apart. One hundred is a cap and not a bill, because a sequential test on a graded score reached its
decision in 12 to 36 paired trials in `beyond_binary_success_2026`, and a cell that stops early
reports a confidence sequence rather than a Wilson interval, never both. The appendix also keeps
the counts an earlier draft of this section quoted and this one withdrew, since the test they were
computed for was the wrong one.

{{table:table8_protocol}}

## 7.4 Feasibility and limitations

The proposed protocol has not been run. In the twelve-method comparison assembled for this
survey, no method supplied all the measurements needed for a complete protocol row. DeXtreme
`dextreme_2022`, for example, reports a success criterion and a confidence interval, but uses ten
trials. This limits retrospective comparison; it does not imply that the reported experiments
failed their own stated objectives.

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
is derived from an interval width, a power calculation or another paper's measurement. The counts are worst-case at p = 0.5, so a method near 90
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
release the rollouts and per-trial outcomes for independent analysis.
