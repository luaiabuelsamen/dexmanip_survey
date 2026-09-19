## Appendix E. Where the protocol's counts come from

Every count in Table 8 is derived below, and each axis is derived for the statistic that axis
actually reports rather than by one convention applied to all of them: a single rate takes a Wilson
half-width, a matched comparison takes McNemar, a ratio takes the standard error of the log ratio,
and a correlation takes the Fisher-z interval. Section 7.3 states what these derivations conclude.
This survey re-ran no method, so every count here rests on an interval width, a power calculation
or another paper's measurement, and never on a measurement of our own. The counts an earlier draft
quoted and this one withdrew are kept, so that a reader can see which test was the wrong one and
why.

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
that the perturbation hurt at all. Certifying that same drop takes 101 per arm at 80 percent
power, or about 50 for an interval that merely excludes 1, so Table 8 now asks for absolute rates
with their own intervals at 40, reports the ratio without an interval, and prescribes 101 before any
claim that a named axis hurt.

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
