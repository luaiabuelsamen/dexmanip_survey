# 7. Evaluation, and a protocol for comparison

## 7.1 Reporting practice

Most of this literature does test on hardware, which is the check that matters and the one a
simulator cannot substitute for: 89 of the 113 papers report a real-robot experiment. What they
report about those experiments is much less even. Figure 6 draws six reporting axes, each against
the denominator that belongs to it, and two of the six are the ones a reader most needs. Without a
count of unseen test objects there is no denominator for a claim about generalisation; without
some statement about contact there is no way to tell whether the hand passed through the object.
Those two are the axes the field states least often. Every share in the figure is a lower bound
rather than a rate, for reasons Appendix A gives.

{{figure:fig6_reporting}}

The plainest gap is the trial count. Nineteen of the papers that ran a real robot never say how
many times they ran it, and a percentage with no denominator cannot be given an interval, so it
cannot be compared with anything.

Where a count is stated it is small, and it is not always the same quantity. Some papers report a
per-cell count, a fixed number of trials on each task or each condition; others report a grand
total over every cell; a few cannot be assigned to either basis. Table 9 keeps the two
distributions apart, because pooling them produces a figure that describes nothing: `hora_2022`'s
240 trials and `visual_dexterity_2022`'s 20 are experiments of comparable size recorded on
different bases.

The per-cell count is the one a confidence interval attaches to, and at the sizes this field uses
the interval is wider than the differences being claimed. At twenty trials per cell, two methods
twenty points apart in success rate are not statistically distinguishable; Appendix E does the
arithmetic, with the intervals and the two-proportion test. The modal cell in this corpus is ten
trials, which is narrower still. This is the single most consequential fact about evaluation in
dexterous manipulation, and it is why section 7.3 proposes a protocol rather than a league table.

Reporting has improved a little and the experiments have not. About two thirds of recent papers
state a trial count, against three fifths of earlier ones, and the counts themselves have not
moved. A field can get better at disclosing a number without the number itself getting any better.

The denominators also sit on different hardware. The papers that name their own hand give 79
distinct descriptions of it, unnormalised, so that figure counts strings and not designs; Figure 2
gives the distribution. A success rate on a 16-degree-of-freedom Allegro and a success rate on a
6-actuator Inspire hand are not measurements of the same thing.

Nor are the criteria the same. `dexverse_2026` counts a pick a success when the cube is "lifted at
least 0.20 m above its resetting height". `bench2dex_2026` requires its terminal predicate to hold
for a continuous dwell time, to reject transient contacts. `colosseum_2024` counts an episode
successful "if the model completes the task fully". `dextrack_2025` reports every success rate as
a pair under two threshold sets, which on one dataset gives 47 and 65 percent for the same
rollouts. Among the papers that state no criterion at all, most have no success predicate to
state: they report radians rotated or time-to-fall and never define a success, which is a fact
about the paper rather than a gap in this survey. Where a criterion is stated it is usually a
rubric, a staged partial credit or a deferral to a benchmark's own definition rather than a
threshold, and a rubric is reproducible inside a lab and not across two.

Seven quantities dissociate in the published data, which is why they have to be reported
separately rather than collapsed into one number.

Task success is the first, and binary success discards the difference between a near-miss and
inaction. `beyond_binary_success_2026` puts it plainly: "a policy that completes 90% of the task
is clearly better than a policy that is frozen the whole time, yet their success rates would be
identically 0%". In `kress_gazit_policy_eval_2024` one policy scores 17 percent overall on a
pancake task while picking up the spatula and flipping the pancake in every attempt.

Robustness to perturbation has been measured, though not yet on a hand. `colosseum_2024` reports
a success drop of a third to a half under single perturbation factors and more than three
quarters under all of them together. In `bench2dex_2026` the leader of the matched condition is
not the leader under combined shift. The ranking at the anchor is not the ranking under shift.

Generalisation to unseen objects is stated by 40 papers, and half of those test on ten objects or
fewer.

Physical plausibility of the contact is the least reported of the six, at 12 percent of the papers
whose notes settle the question. Section 7.2 takes it up.

Sample and wall-clock cost is reported by about a third of the corpus as an environment count and
by fewer as an episode count. `robopianist_2023` is the exception that shows what disclosure looks
like, giving samples per song and hours per run on named hardware.

Real-robot transfer is the one that undoes the rest, because simulated rank order is not real
rank order. `autoeval_2025` scores one policy at 6 of 50 in simulation and 47 of 50 on the real
arm for the same task. `suresim_2025` states the limit directly: "the simulation-to-real gap
precludes rigorous statistical inferences about real-world outcomes from simulation results
alone".

Reproducibility is the last, and releasing code is not the same as releasing something that
settles a question. Eight papers state a training objective in their own repository that differs
from the one in the paper, which section 5.6 sets out and Table 11 names file by file. That is the
figure this section uses.

## 7.2 Physical plausibility

One quantity is specific to hands and is almost never reported: how far the hand passes into the
object it is holding. Outside closed-loop control it has been a standard comparative column for
years. Grasp synthesisers fail a grasp that penetrates past a stated depth
`bimangrasp_2024`, retargeting methods report a maximum depth against a baseline
`toporetarget_2026`, and hand-object datasets score a split on depth, intersection volume and
simulation displacement `oakink_2022`. Among learned closed-loop policies, almost
nobody reports it, and nobody reports it measured in the physics the policy ran in.

D-Grasp `dgrasp_2022` is the instructive case, because it does report a volume for a pose its own
policy reached, and the way it does so shows where the quantity goes. Inside the simulator the paper
reports zero penetration, since the meshes there are decimated for speed; the figure it prints
instead comes from re-measuring a single frame against the original hand mesh and the
full-resolution object mesh, with, in the paper's words, "no physical simulation involved". So
the number a reader wants, how deep the hand sits in the object in the physics that trained the
policy, is zero by construction, and the number reported is a geometric re-measurement on
geometry the simulator never used.

The same paper supplies the reason to want the measurement. Its appendix observes that a deeply
penetrating reference grasp can raise a success rate rather than lower it, because "the objects
can become entangled within the hand mesh and will therefore not be able to fall down", and
concludes that "the success rate metric should always be interpreted in combination with the
other metrics". A success rate with no plausibility number beside it can be read two ways.

There is a reason the gap persists, and it is not difficulty. A quantity a policy optimises
cannot also judge it, because the policy learns the measure rather than the property the measure
stands for. `physhoi_2023` shows the failure in the clean direction: its imitation reward is
maximised by not touching the object at all, because contact perturbs the reference trajectory.
`dextrack_2025` shows it from the other side, defining a maximum penetration depth, applying it
only to its input references, and then reporting tolerance of "severe hand-object penetrations"
as a result. The remedy is to measure with something the policy never optimised.

Definitions are not shared either, which is the other half of why published figures do not
compare. `grab_2020` reports an average penetration in millimetres without saying whether it is a
maximum, a mean or a median; `oakink_2022` supplies the fullest published vocabulary, separating
penetration depth, solid intersection volume and simulation displacement. A number without its
definition is not a number a second paper can be held to.

What would close the gap is one line in a results table: the maximum and mean penetration depth
over the evaluation rollouts, on a dense surface sample, computed by code that never entered the
reward or the termination rule. That is the plausibility row of the protocol in Table 8. What this
survey supplies there is a measurement and a count; it does not supply a threshold, and section 7.4
says where the one in the table is borrowed from and why it does not bind.

## 7.3 Statistical practice, and a proposed protocol

A protocol already exists for evaluating learned robot policies, and what it does not supply is
the part a reader needs. `kress_gazit_policy_eval_2024` prescribes process rather than numbers:
write the success criteria before the run, have someone other than their author score the runs,
match initial conditions with image overlays, interleave the policies blind within one session,
report counts rather than percentages, and use a posterior over the success probability instead of
a point estimate. All of that is right and none of it fixes the sample size. It prescribes no
minimum trial count and no interval width, and its own worked example shows why one is needed: at
twenty evaluations per policy, an eighteen-point difference in success rate still leaves better
than a one-in-ten chance that the worse policy is actually the better one. Multiply every count in
that example by ten and the same two rates separate.

One study does put numbers on it, without saying where they come from.
`lbm_careful_examination_2025` supplies them by fiat rather than derivation: 50 rollouts per
task per policy per condition on hardware, 200 in simulation, blind, with randomised policy
order inside per-initial-condition bundles. It replaces confidence intervals with
Beta-posterior violins and corrects its pairwise tests under Bonferroni, "unless otherwise
noted". Its own warning is the strongest sentence in this literature: "there is significant
risk that many robotics papers are measuring statistical noise due to insufficient statistical
power".

The rest fall short of their own advice. `roboarena_2025` runs hundreds of double-blind pairwise
comparisons across seven institutions and thousands of rollouts, and reports neither confidence
intervals nor per-policy trial counts. `colosseum_2024` evaluates hundreds of test sets with "one
training seed and one evaluation seed" per baseline and gives no intervals in simulation.
`autoeval_2025` calls ±10 percent "the natural variance of robot evaluations" without giving the
formula behind the intervals it plots.

Two papers do give usable numbers. `suresim_2025` pairs real and simulated trials and de-biases
the simulation with a rectifier, which saves up to a quarter of the hardware trials when the
paired correlation is high and nothing at all when it is near zero; its decision rule is exact,
that combining helps only when the rectifier variance is below the variance of the real
evaluations. `beyond_binary_success_2026` gives the larger saving by scoring progress rather than
success: a sequential test on graded scores cuts hardware trials by about 45 percent, and a gap
that needs 80 binary trials to establish is established in 18 when the score is continuous. That
is the strongest argument in the literature for grading partial progress.

Every count below is printed by `tools/make_eval_tables.py` in its
derivation mode, and each axis is derived for the statistic that axis actually reports: a
single rate takes a Wilson half-width, a matched comparison takes McNemar, a ratio takes the
standard error of the log ratio, a correlation takes the Fisher-z interval.

Appendix E derives the counts in Table 8, and they come to this. Reporting a single rate honestly
takes about 100 real rollouts per cell, which is where the worst-case interval half-width falls to
ten points. Comparing two policies is a harder question: because the design is paired, the count
depends on how often the two disagree rather than on the two rates alone, and separating a
twenty-point difference at conventional power takes 57 matched pairs per arm, which is fewer
rollouts than two independent arms would need. Simulated cells are cheap enough to run in the
hundreds.

The other axes follow the same logic and Appendix E gives their counts. Perturbation axes are
screened cheaply, which ranks them but cannot establish that any one of them hurt, and certified at
the same cost as a single rate. Unseen-object claims resample the object rather than the trial, so
the count that matters is the number of objects and not the number of rollouts. The transfer axis
needs real and simulated trials paired, and separating two correlations takes several hundred
pairs, which is why it belongs in a benchmark rather than in a paper. Every count there is a cap
rather than a bill: a sequential test on a graded score can decide in a fraction of the trials,
and a cell that stops early reports a confidence sequence rather than a fixed-sample interval,
never both.

{{table:table8_protocol}}

## 7.4 Feasibility and limitations

The proposed protocol has not been run. In the twelve-method comparison assembled for this
survey, no method supplied all the measurements needed for a complete protocol row. DeXtreme
`dextreme_2022`, for example, reports a success criterion and a confidence interval, but uses ten
trials. This limits retrospective comparison; it does not imply that the reported experiments
failed their own stated objectives.

The bill comes first, because it decides whether any of this is adoptable. Comparing two policies
on three tasks under the protocol in Table 8 comes to 942 real rollouts, which at a minute each
including the reset is about 16 hours of robot time before failed resets, repairs and scoring.
Appendix E itemises it. Pairing the anchor set removes about a fifth of the bill rather than the
four fifths the pair counts suggest, because a pair is still two rollouts. For scale,
`autoeval_2025` ran roughly 850 episodes in a day on a parallel-jaw arm with three human
interventions, pausing regularly once the motors overheated; a tendon-driven multi-finger hand is
more fragile, so those 16 hours are most of a week of calendar time.

That bill is large but not unprecedented. Evaluating one generalist policy against its baselines
has taken more than 2500 rollouts and more than 100 hours of human labour across three
institutions (`autoeval_2025`), and a recent careful examination analysed close to two thousand
real rollouts across nine hardware stations. What is unprecedented is paying that cost for a single
dexterous-hand paper, where the modal cell is ten trials.

Four things would have to change. Reviewers would have to reward 57 matched trials on one task
over 20 unmatched trials on five, and nothing in the corpus suggests that is happening. The loop
would have to be automated, and `autoeval_2025` shows it is buildable for a gripper at one to
three hours of setup, while stating that it supports binary success only and no robustness axes.
Somebody would have to run the penetration measure on their own rollouts, which is a choice rather
than a capability: section 4.2 shows the depth is computable from the poses and the meshes in a
few lines of code, and the field's own benchmark repository already ships a task that does it
every step. The comparison would also have to be sequential, because the savings in
`beyond_binary_success_2026` are the only reason the protocol's counts are caps rather than
costs.

Four limits apply to the proposal itself. This survey re-ran no method, so every count in Table 8
is derived from an interval width, a power calculation or another paper's measurement rather than
from an experiment here. The counts are worst case, so a method with a high success rate needs
fewer trials for the same interval, and the paired count rests on an assumed discordance rate that
no paper in this corpus reports. The perturbation axes are borrowed from benchmarks that run
parallel-jaw grippers on rigid objects (`colosseum_2024`, `simpler_2024`), where the measured
sensitivity to physical parameters is smaller than a multi-finger hand should be expected to
show.

That sensitivity should grow with multi-finger contact, and no work in this corpus
measures it. The 2 mm penetration threshold is taken from `toporetarget_2026` with no
independent justification, and the captured human grasps in `grab_2020` sit above it at 3.25
mm, which makes 2 mm a simulator convention rather than a physical bound. So the three things
this survey adds to the reference-versus-rollout axis are a count, a measurement method and a
protocol slot for them, and a threshold is not among them. It is borrowed from one paper and
reported as borrowed, and it will stay a convention until somebody measures penetration on
rollouts across hands and engines and finds a value that separates behavior a physicist would
accept from behavior they would not.

Seven papers in this corpus are evaluation
protocols, a small denominator, and not one of them uses a dexterous hand: `suresim_2025` runs
a parallel-jaw gripper and the other six state no hand. Everything proposed above is therefore
assembled from work on grippers and on whole-arm tasks. What would close that, and close it
cheaply, is to run the Table 8 protocol once, on one in-hand reorientation task with one 16-DoF
hand, and release the rollouts and per-trial outcomes for independent analysis.