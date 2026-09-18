# R4 — evaluation and statistics review

Scope: section 7 in full, Tables 8 and 9, Figure 6, and every number in the draft that is
derivable from `corpus/rows/*.json`. Everything below was recomputed from the rows, the notes and
`tools/make_eval_tables.py --derive`; the recomputation scripts are reproduced inline in the
evidence lines so the authors can rerun them.

Verdict up front. The arithmetic of section 7 is almost all correct — I checked 68 statistics and
found the Wilson intervals, the power calculation, the corpus tallies and the quoted evidence from
other papers to be right in 55 of them. The problem is not arithmetic. It is that the survey's
headline coverage statistics measure its own extraction pipeline rather than the literature, that
the denominators shift between "110 method rows", "87 real-robot rows" and "61 code-releasing
rows" without saying which is which, and that the trial counts in Table 8 are derived for
quantities Table 8 does not ask anyone to report. Three of those are blocking.

---

## Blocking

### 1. The 50-percent trial-count statistic measures what the extraction captured, not what papers reported

**location** §7.1: "Only 55 of those 110 state how many real trials produced the headline number,
which is 50 percent." And: "Thirty-two of the 87 papers with a real robot never say how many times
they ran it."

**the problem** Both sentences are assertions about what papers *say*. They are computed from
`real_trials != null` in the rows, which is an assertion about what the extraction step could
reduce to a single integer. These are different quantities, and the gap is large enough to move
the headline by twelve points in the direction that flatters the survey's thesis.

**the evidence** I took the 32 method rows with `real_robot: true` and `real_trials: null` and read
their own notes in `papers/notes/`. In at least 13 of the 32 the note records a real-robot trial
count in plain text:

| key | what `papers/notes/<key>.md` says | row |
|---|---|---|
| `pi0_2024` | "averaging over 10 trials per task" (§VI-B, VI-C), line 50 | null |
| `gemini_robotics_2025` | "20 trials/task for §4.1 specialists ... 20 trials/task for the Franka in-distribution eval", line 45 | null |
| `groot_n1_2025` | "Real — 10 trials/task, except Machinery Packing (5 trials) ... (5 objects × 3 trials = 15)", line 37 | null |
| `h_rdt_2025` | "towel folding (25 trials, Table 1) ... Cup-to-coaster (25 trials)", lines 115-116 | null |
| `rdt1b_2024` | "Wash Cup 8 trials × 3 cups = 24 trials; Pour Water ... 24 trials; Handover, Fold Shorts, Robot Dog each 25 trials", line 69 | null |
| `umi_2024` | "20 episodes per narrow-domain task ... 120 object-tosses ... 60 combined trials", line 30 | null |
| `dexpoint_2022` | "26 real objects, 10 trials per object-policy pair (Sec 4.4, p.8, Table 3)", line 73 | null |
| `dexteritygen_2025` | "per-task trial counts of 10 or 20 given directly in Table I/II", line 55 | null |
| `gr_dexter_2025` | "10 eval batches × 5 seen objects = 50 trials", line 30 | null |
| `bidex_teleop_2024` | "Table 2 mobile tasks are 'averaged across 20 trials'", line 32 | null |
| `open_television_2024` | "5 real-world episodes for each task (Table 1 caption)", line 29 | null |
| `twisting_lids_2024` | "20 trials, with each trial lasting for a maximum of 30 seconds", line 32 | null |
| `pistar06_2025` | "300 episodes across 4 robot stations ... 450 evaluation episodes ... 600 autonomous trials", line 40 | null |

Sixteen of the 32 notes explicitly say the count is *not* stated (`anyrotate_2024`,
`maniptrans_2025`, `pang_global_planning_2022`, `dexplore_2025`, `dexwild_2025`, `rotateit_2023`,
`pgdm_2023`, `gemini_robotics_15_2025`, `toporetarget_2026`, `deximit_2026` and others), so those
nulls are correct. The loss is entirely at the note → row step, and the cause is structural: the
schema field is `real_trials: int or null` documented as "total real trials behind the headline
number", and a paper that reports 10 trials per task on nine tasks has no single such integer.

**corrected values**

- state a real trial count: **≥ 68 of 110 = ≥ 62 percent**, not 55 of 110 = 50 percent.
- among the 87 with a real robot: **≥ 68 of 87 = ≥ 78 percent**, not 55 of 87 = 63 percent.
- "never say how many times they ran it": **≤ 19 of 87 = ≤ 22 percent**, not 32 of 87 = 37 percent.

This is a floor, not an estimate: I only counted cases where the note itself carries the number, so
any count that the note also missed is still uncounted.

**the fix** Three things, in order of importance. (a) Re-derive the five coverage statistics from
the notes rather than the rows, or add a second row field (`real_trials_per_cell` and
`real_trials_basis`) and recompute. (b) Rename every such statistic in the text and in Figure 6's
caption from "state X" to "state X in a form this survey's extraction could record", and give both
numbers where they differ. (c) Add to Appendix A, under "What this method cannot do", a paragraph
in the style the survey already uses in §5.8: *"Every coverage statistic in §7.1 is a lower bound.
A structured row records a scalar; a paper that reports a per-task count, a rubric, or a count
spread over several tables produces a null. Hand-checking the 32 real-robot rows with a null trial
count against their own notes recovered 13 stated counts, so the 50 percent figure should be read
as ≥62 percent and every other bar in Figure 6 as a floor."* §5.8 already does exactly this for the
paper/code statistic ("Nine are limitations of this survey's own parsing"; "Sixteen is therefore
the number to quote, and it is a floor"). Section 7 must do it too, or §5.8's honesty makes §7 look
like a choice.

### 2. `real_trials` is not one quantity, so its range, median and quartiles describe nothing

**location** §7.1: "The 55 counts run from 5 to 1287, with a median of 20 and quartiles at 10 and
70."

**the problem** Some stored values are per-cell counts (per task, per policy, per condition) and
others are grand totals across all cells. Pooling them makes the distribution uninterpretable, and
the Wilson argument that follows it applies only to the per-cell reading.

**the evidence** Checked each stored value against its note:

- `visual_dexterity_2022` row = 20. Note line 61: "12 evaluation objects (7 train / 5 OOD), each
  tested 20 times per real-world condition". The total is ≥240; the row holds the per-cell count.
- `hora_2022` row = 240. Note line 57: "20 trials/object × 6 objects per set ... heavy-object set
  and irregular-object set" = 240. The row holds a **total**.
- `dime_2022` row = 10. Note line 28: "For each algorithm and each task, we run the robot for ten
  trials", over 4 algorithms × 4 tasks. Per-cell.
- `openai_dexterity_2018` row = 10. Note line 52: "10 trials per policy on the physical robot",
  across Tables 3–5. Per-cell.
- `dexcap_2024` row = 60. Note lines 34-36: 20 trials/task on 3 tasks, **plus** a separate 75-trial
  Packaging evaluation the row drops. Partial total.

So `hora_2022` at 240 and `visual_dexterity_2022` at 20 are the same experiment size recorded two
different ways, and the survey then calls 240 "the outlier, not the norm" (§5.2.2, line 908).

**the fix** Split the field into `real_trials_per_cell` and `real_trials_total`, re-extract, and
quote the distribution of the per-cell count only, since that is the denominator a Wilson interval
attaches to. Re-run the quartiles afterwards. Until then, drop the range and the quartiles and
quote only that the modal per-cell count is 10 or 20.

### 3. §7.5 derives the A/B trial count from the wrong test, and the wrong test is the one the bill rests on

**location** §7.5: "For the A/B comparison the relevant calculation is power, not width. A
two-sided two-proportion test at α = 0.05 with 80 percent power needs 93 trials per arm to separate
50 from 70 percent, 169 to separate 50 from 65, and 387 to separate 50 from 60."

**the problem** The arithmetic is right for an *unpaired* two-proportion test — I reproduced
93 / 169 / 387 exactly from `n_per_arm` — but the protocol these numbers justify is explicitly
paired. Table 8 requires "initial conditions matched by image overlay" and "policies interleaved
blind in one session"; §7.6's transfer row requires "the same 100 initial conditions run in both".
`tools/make_eval_tables.py` even labels its own output "Paired A/B, alpha 0.05 two-sided, 80 percent
power, trials per arm" (line 76) while calling `n_per_arm`, which is the independent-samples
formula. For a matched-pair binary comparison the sample size follows McNemar and depends on the
discordance rate, not on p1 and p2 alone:

```
50 vs 70 percent, alpha .05, power .80, McNemar:
  discordance 0.2 ->  37 pairs      0.3 ->  56 pairs
  discordance 0.4 ->  76 pairs      0.5 ->  96 pairs
```

At any plausible discordance the paired design needs 37 to 96 *pairs*, against the 93 per arm (186
rollouts) the draft asks for. The recommendation is therefore up to five times too expensive, and
§7.7's whole rhetorical arc — "A two-policy comparison on three tasks is 1200 real rollouts ... 20
hours of robot time ... a week of calendar time" — is built on the number that is wrong.

**the fix** Either (a) keep the pairing and redo the derivation with McNemar, stating the assumed
discordance and showing the sensitivity, which will roughly halve the bill and strengthen the
proposal, or (b) drop the pairing from Table 8 and say the 93 is for independent arms. Do not leave
the tool printing "Paired" over an unpaired formula. If (a), also fix §7.7's 1200 and the 20 hours.

### 4. Table 8's per-axis trial counts are derived for quantities Table 8 does not ask anyone to report

**location** Table 8, rows "Robustness" and "Real-robot transfer"; §7.5: "Perturbation axes are
screened rather than certified, so 40 per axis at a 15-point half-width is enough to rank them".

**the problem** Two of the seven axes report something other than a single rate, and the derivation
covers only a single rate.

**the evidence**

- *Robustness*. Table 8 says the measured quantity is "success under each perturbation axis,
  reported as **the ratio to the unperturbed anchor**". The 40 comes from `n_for_halfwidth(0.15)`
  = 39, which is the Wilson half-width of one proportion. The interval on a ratio of two
  proportions is much wider. Worked: anchor 0.5, perturbed 0.3, n = 40 in each →
  RR = 0.60, 95 percent CI 0.34 to 1.06. The interval contains 1. At the count Table 8 prescribes
  you cannot establish that the perturbation hurt at all, let alone "rank them and pick the two
  worst for hardware".
- *Real-robot transfer*. Table 8 asks for "the paired correlation and the rectifier variance" and
  prescribes "the 100 real trials, paired to 100 sim". No derivation anywhere gives the precision of
  a correlation. At n = 100 and ρ̂ = 0.70 the Fisher-z 95 percent interval is 0.58 to 0.79. That
  cannot separate `suresim_2025`'s useful regime (ρ ≈ 0.70, ">25 percent hardware trials saved")
  from its marginal one (ρ ≈ 0.59, ">20 percent"), which is precisely the decision the axis exists
  to support.

**the fix** Add a derivation per axis for the statistic that axis actually reports. For robustness
either report absolute rates with their own intervals and drop the ratio, or derive n from the
log-ratio standard error. For transfer, state the n needed for the correlation interval width you
want (ρ ± 0.10 at ρ = 0.7 needs about 100; ρ ± 0.05 needs about 370) and say which decision it
supports.

### 5. The protocol asks for a fixed-n Wilson interval and a sequential stop at the same time

**location** Table 8 "Task success": "100 real and 200 sim ... reported alongside it: Wilson 95
percent interval". §7.5: "One hundred is a cap and not a bill, because on a graded score a
sequential test reached its decision in 12 to 36 paired hardware trials in
`beyond_binary_success_2026`."

**the problem** These are incompatible. If you stop when a sequential test declares a winner, the
Wilson interval computed at the stopping time is not a 95 percent interval — optional stopping
biases it, and that is the whole reason `beyond_binary_success_2026` and `suresim_2025` use
anytime-valid betting intervals (WSR confidence sequences) rather than Wilson. The draft quotes
both papers approvingly in §7.4 and then prescribes the statistic they replaced.

**the fix** Say which regime the cell is in. Concretely: "a cell stopped early by a sequential test
reports an anytime-valid confidence sequence (WSR, as in `beyond_binary_success_2026`), not a
Wilson interval; a cell run to a fixed 100 reports Wilson." One clause in Table 8's "reported
alongside it" column and one sentence in §7.5.

### 6. Table 9's row selection is corrupted by substring matching, and one row does not belong

**location** §7.6: "The rows are the 12 most-mentioned dexterous-hand policy methods in the corpus,
ranked by how many other corpus papers name them in their parsed text ... the ranking is recomputed
by `tools/make_eval_tables.py` rather than fixed by hand." Table 9 row `unidex_2026`.

**the problem** `table9_rows()` scores a method by `name.lower() in t`, a bare substring test.
"UniDex" is a prefix of "UniDexGrasp" and "UniDexGrasp++", so `unidex_2026` inherits the mention
count of a different, earlier, much better-known paper.

**the evidence** Recomputed both ways over `papers/md/*.md`:

```
unidex_2026        loose substring = 34    word-boundary = 3
unidexgrasp_2023   loose substring = 32    word-boundary = 27
```

Twenty-nine of the 35 documents containing "unidex" never contain it as a standalone token. Under a
word-boundary match `unidex_2026` falls out of the top 12 entirely and `pddm_2019` (25) enters at
rank 12. A 2026 paper sitting sixth in a "most-mentioned" ranking over a corpus written mostly
before it should have been a red flag.

A second, separate defect in the same function: `method_name()` returns whatever follows the em-dash
on the note's first line, which is an acronym for some works and a full title for others. The
ranking therefore counts "DexMV" (an acronym, 50) against "Learning Dexterous In-Hand Manipulation"
(a 39-character title, 64) and "Learning Complex Dexterous Manipulation with Deep Reinforcement
Learning and Demonstrations" (49). A title is matched mostly inside reference lists; an acronym is
matched in running text. These have different base rates, so the ranking is not a single quantity,
and it is closer to a citation-age proxy than to importance.

**the fix** Match on a word boundary (`re.escape(name) + r'(?![A-Za-z0-9+-])'`), regenerate, and
report the ranked counts in the caption so a reader can audit them. Decide whether the unit is the
acronym or the title and use one consistently; if a work has no acronym, say in §7.6 that its title
was used and that the counts are not comparable across the two kinds. Then restate §7.6's rule to
match the code exactly, including the `len(name) < 4` filter and the "hand string contains
'parallel' or 'gripper'" filter, neither of which the prose mentions.

---

## Major

### 7. The headline denominator excludes nobody and should exclude 23 papers

**location** §7.1: "Of the 110 method rows, 87 report a real-robot experiment, which is 79 percent.
Only 55 of those 110 state how many real trials produced the headline number, which is 50 percent."

**the problem** "Only 55 of those 110" reads as though 110 were the set just described, which was
87. Twenty-three rows have no real robot and so cannot state a real trial count; including them in
the denominator makes a reporting failure out of a definitional impossibility. The 50 percent is
the number the abstract-level reader will carry away.

**the evidence** `real_robot: true` = 87; every one of the 55 rows with a `real_trials` value also
has `real_robot: true` (checked: the set of rows with a trial count and `real_robot != true` is
empty). So the conditional rate is 55/87 = 63 percent, or ≥ 68/87 = ≥ 78 percent once finding 1 is
applied.

**the fix** "Of the 87 with a real-robot experiment, 55 state how many real trials produced the
headline number, 63 percent" — and then the corrected floor. Figure 6 should either use the 87
denominator for that bar or label the mixed denominator on the bar itself.

### 8. §7.2 and Table 8 quote 37 paper/code disagreements; §5.8 and §8 say the number to quote is 16

**location** §7.2: "Fifty-five percent released code, and 37 of the 110 rows record a disagreement
between the paper and that code." Table 8, Reproducibility row, "why" column: "37 of the 110 method
rows already carry such a disagreement."

**the problem** §5.8 decomposes the 37 into 16 contradictions, 9 limitations of this survey's own
parsing, 7 cases where the component was never released, 3 version skew and 2 intra-paper
inconsistencies, and states outright: "Sixteen is the number to quote." §8 repeats it. Section 7
quotes 37 twice without the decomposition, which is the survey contradicting itself on its own
finding, in the section where a sceptical reader is least forgiving.

**the evidence** Recomputed: `paper_code_mismatch != null` = 37; all 37 have `code_released: true`.
Decomposition is the draft's own, lines 1166-1172 and 1855-1865.

**the fix** In §7.2 and in Table 8 write "16 of the 61 code-releasing rows (26 percent) carry a true
contradiction between the paper's stated objective and the released code, and 37 carry a recorded
disagreement of any kind including 9 that are limits of this survey's parse (§5.8)."

### 9. Penetration coverage treats 16 unknowns as negatives

**location** §7.3: "Eleven of the 110 method rows handle interpenetration in any form". Figure 6
bar: "contact or penetration handled — 11 (10%)". Figure 1 spec: "'penetration not addressed' 83 of
110".

**the problem** The `penetration` field is null for 16 of the 110 rows. Null means the note did not
settle it, not that the paper ignored penetration. The draft's own figure-1 spec shows the
arithmetic: 11 + 83 = 94, and the missing 16 are silently folded into the denominator of the
percentage while being excluded from the "not addressed" node.

**the evidence** `Counter(penetration)` over the 110 method rows =
`{'not addressed': 83, None: 16, 'constrained': 5, 'measured': 3, 'penalised': 3}`. Among rows with
a known status the rate is 11/94 = 12 percent, not 10 percent.

**the fix** Quote "11 of the 94 rows whose contact handling the note settled, 12 percent; 16 rows
are unknown". Add the 16 as a dashed node in Figure 1 the way the spec already does for
`human_data` "not stated" and for the simulator column, and as a separate grey segment in Figure 6.
The classification of the 11 into 3 penalised / 3 measured / 5 constrained and the named keys in
§7.3 are all correct — I verified every key.

### 10. The code-release denominator has four unknowns

**location** §7.1 "Sixty-one released code, 55 percent"; §7.2 "Fifty-five percent released code";
§8 "the forty-nine rows that released nothing cannot be checked at all".

**the evidence** `code_released`: true 61, false 45, null 4. So 61/110 = 55 percent mixes 4
unknowns into the denominator; among known rows it is 61/106 = 58 percent. And "the forty-nine rows
that released nothing" is 45 known-no plus 4 unknown.

**the fix** "61 of the 110 released code and 45 did not; 4 rows are unknown" — then quote 55 percent
of all rows or 58 percent of settled rows and say which.

### 11. "Thirty-one method rows state no criterion at all" is the same capture artefact as finding 1

**location** §7.1, last sentence of the paragraph on criteria.

**the evidence** Of the 31 method rows with `success_criterion: null`, the notes of at least these
state one: `pistar06_2025` ("fold[ed] and stacked in the top right corner of the table within 200
seconds", note line 40, per-task criteria with numeric limits); `bunny_visionpro_2024` ("binary
per-trial task completion ... judged against the task description in Tab. 1", line 27);
`pi0_2024` ("each task has a hand-designed scoring rubric (Appendix E)", line 50);
`groot_n1_2025` ("task-defined binary or staged success per the cited benchmark's own protocol",
line 37). The field is documented as "verbatim if short", so a rubric or a deferred criterion
produces a null.

**the fix** "Thirty-one rows state no criterion this survey could record as a verbatim threshold;
several of those state a rubric or defer to a benchmark's own definition, which is a different
failure and a milder one." Then the sentence still supports the argument — a rubric is not
comparable across papers either — without overstating it.

### 12. "The corpus median is 20 trials and has not moved since 2022" is false

**location** §7.7: "the corpus median is 20 trials and has not moved since 2022". Supported by
§7.1: "This has not improved: 25 of the 45 rows from 2025 and 2026 state a trial count, and their
median is also 20."

**the evidence** Median per-year of the stated counts:

```
2018 n=1  median 10      2023 n=6  median 27.5
2019 n=1  median 10      2024 n=16 median 20
2020 n=1  median 150     2025 n=14 median 20
2022 n=5  median 10      2026 n=11 median 20
```

The median was 10 in 2022 and 27.5 in 2023, so it has moved, twice. What is true is that it has been
20 in each of the last three years. Separately, the *rate* of stating a count did improve: 25/45 =
56 percent for 2025-26 against 30/65 = 46 percent for everything earlier. "This has not improved"
is asserted immediately before a statistic showing a ten-point improvement in the neighbouring
quantity.

**the fix** "The median stated count has been 20 in each of 2024, 2025 and 2026. It is 20 across the
corpus as a whole. Per-year medians before 2024 rest on one to six observations and should not be
read as a trend." And in §7.1, "the share stating a count has risen from 46 to 56 percent, but the
median count has not moved."

### 13. §7.6's absolute claim is refuted by a row in the corpus

**location** §7.6: "no cell can be filled from a published number, because no number in the corpus
carries the interval, the denominator and the criterion that Table 8 asks for."

**the evidence** `dextreme_2022` carries all three. `corpus/rows/dextreme_2022.json`:
`real_trials: 10`; `success_criterion: "object orientation within 0.4 rad of target triggers a new
goal at test time (training success tolerance 0.1 rad); episode resets as a 'fall' when goal_dist
>= 0.24 m fallDistance"`; `headline_value: "27.8±19.0 average consecutive successes (median 14.0,
best rollout 112) (Table 7/9)"`, and `papers/notes/dextreme_2022.md` line 74: "± is a '90%
confidence interval'". Denominator, interval and criterion, all three.

**the fix** Narrow the claim to the denominator, which is the defensible version: "no cell can be
filled at the denominator Table 8 asks for. `dextreme_2022` comes closest, reporting a criterion,
a count and a 90 percent interval — on 10 trials."

### 14. Table 9 says no cell can be filled; Table 7 has already filled several of them

**location** §7.6: "Every cell is empty ... no cell can be filled from a published number."

**the problem** Table 7 carries `trials`, `unseen obj`, `penetration` and `code` columns for all 110
method rows, including all 12 of Table 9's rows. The reproducibility axis in particular is fully
populated for these methods in the survey's own data: the survey knows which released code and
which carry a paper/code disagreement. A reader who has just read Table 7 will notice.

**the fix** Say what is different. Table 9's cells demand a number with an interval, a denominator
and a pre-registered criterion; Table 7's cells are bare values. Write that distinction into §7.6
explicitly — "Table 7 records what each method reported; Table 9 asks for what Table 8 defines, and
none of Table 7's values meet it" — and consider pre-filling Table 9's reproducibility column from
Table 7, which would make the emptiness of the other six columns land harder.

### 15. Table 9 is not usable as an empty matrix without a cell contract

**location** Table 9, all 84 cells; §7.6.

**the problem** Task 4 of my brief. Axes: five of the seven are measurable as written (task success,
unseen objects, physical plausibility, cost, reproducibility). Two are not, for the reasons in
finding 4 — "robustness" does not say whether the cell holds the absolute rate or the ratio, and
"transfer" does not say whether it holds the correlation, the rectifier variance, or both. Row
selection: the rule is stated in prose but does not match the code (finding 6), and one row is
wrong. Cell format: nowhere does the survey say what goes in a cell. A reader filling it has to
reverse-engineer "value ± Wilson half-width (n), criterion cited" from Table 8's fifth column.

**the fix** Three additions and the table becomes usable. (a) Give each column its unit in the
header: "task success (rate ± Wilson 95, n)", "robustness (ratio to anchor, [lo, hi])", "unseen
objects (mean per-object rate, bootstrap 95, k objects)", "plausibility (max/mean mm, frac >2 mm)",
"cost (env steps, GPU-h, 3-seed range)", "transfer (ρ [lo, hi], rectifier var / real var)",
"reproducibility (file:line of each disagreement, or none)". (b) One worked example row, filled
with fabricated-but-labelled values, so the format is unambiguous. (c) State the row rule as the
code implements it and publish the mention counts.

### 16. Section 3.2's hand counts contradict sections 5 and 7

**location** §3.2: "The Allegro accounts for 35, Shadow for 21, the Inspire RH56 family for 19, a
parallel-jaw gripper for 12 and **LEAP for 11**. **Seventy-four** of the 103 name an Allegro, a
Shadow or Adroit model, LEAP or an Inspire."

**the evidence** Over the 103 method rows with a non-null `hand`, substring-matching the hand string
(the same rule that reproduces 35 / 21 / 19 / 12 exactly): LEAP = **12**, not 11. §5.2.1 says "LEAP
at 12 and 4" and §7.1 says "LEAP in 12". The union of Allegro, Shadow, Adroit, LEAP and Inspire is
**75**, not 74. Separately §3.4 says "Fourteen of the 103 hand-naming method rows use an
open-hardware hand, and 11 of those are LEAP", which needs the twelfth LEAP row named and excluded
or it inherits the same error.

The "52 of the 103" in the same paragraph *is* reproducible, but only under a rule the paragraph
does not state: Allegro ∪ Shadow = 49, Allegro ∪ Shadow ∪ Adroit = 52. Since the next sentence gives
Allegro 35 and Shadow 21 (which sum to 56 and overlap on 7), a reader cannot get from 35 and 21 to
52 without being told that Adroit counts as a Shadow design and that the union is not the sum.

**the fix** LEAP 11 → 12; 74 → 75; add "counting Adroit as a Shadow derivative, and as a union
rather than a sum" to the 52.

### 17. The Isaac Gym count is 35 in two places, 36 in the generator, and 36 by implication in a third place

**location** §1: "53 train with reinforcement learning and 35 run in Isaac Gym." §4.3: "Thirty-five
of the 110 method papers in this corpus run on it." §4.2: "Those two simulators carry 41 of the 110
method papers." §5.2.1: "Forty-three run their own experiments in a GPU-parallel simulator from the
Isaac family or Genesis."

**the evidence** `tools/make_flow_tree.py:norm_sim`, which the draft says the figures must use,
returns over the 110 method rows: Isaac Gym **36**, not stated 35, MuJoCo **16**, Isaac Lab/Sim 6,
other **5**, SAPIEN 4, no simulator 3, Drake 2, RaiSim 2, Genesis 1. So Isaac Gym + Isaac Lab = 42,
not 41, and Isaac family + Genesis = 43, which is the number §5.2.1 already uses. 35 + 6 + 1 = 42 ≠
43: the draft's own two numbers cannot both be right.

The Figure 1 spec (§1.4) also disagrees with its own generator on four of ten nodes — it lists
"Isaac Gym 35, MuJoCo 18, ... other or unclear 8, ... not stated 31" against the generator's 36 /
16 / 5 / 35 — while the caption insists "Every number above comes from corpus/rows/*.json and must
be regenerated by the drawing script". The 31 is the count of `sim: null`; the generator's 35 also
folds in four rows whose `sim` string contains "not stated".

**the fix** Regenerate the figure-1 spec from `norm_sim` and propagate: 35 → 36 in §1 and §4.3,
41 → 42 in §4.2. Then state in the caption whether "not stated" means a null field or a field whose
text says not stated, and use one rule.

### 18. The "not separated at all" argument uses overlapping intervals, which is not a test

**location** §7.1: "At 20 trials a reported 60 percent carries a 95 percent Wilson interval of 39 to
78 percent, and a reported 80 percent an interval of 58 to 92 percent. Two methods separated by 20
points at the median trial count are not separated at all."

**the problem** The intervals are correct — I reproduce 38.7–78.1 and 58.4–91.9 exactly. But
overlapping confidence intervals do not imply a non-significant difference; that inference is a
known fallacy and R4-shaped reviewers will say so. Here the conclusion happens to hold (two-sided
two-proportion test, 12/20 vs 16/20: z = 1.38, p = 0.17), so the fix is cheap.

**the fix** Add the test: "and a two-proportion test on 12 of 20 against 16 of 20 gives p = 0.17, so
the difference is not established." Keep the intervals for the width argument, which is what they
are for.

### 19. The 93 coincidence is never flagged, and reads as confirmation

**location** §7.5, consecutive paragraphs: "10 points needs 93 ... so the absolute-rate minimum is
93, rounded to 100" then "needs 93 trials per arm to separate 50 from 70 percent".

**the problem** These are two unrelated derivations — a one-sample Wilson half-width and a
two-sample power calculation — that happen to land on the same integer. Printed back to back with
no comment, the second reads as independent confirmation of the first. It is not. The draft is
otherwise scrupulous about this kind of thing (§7.6's "mention counts are counts of mentions, not of
use"), so the silence stands out.

**the fix** One sentence: "That 93 is the same integer as the half-width calculation above is a
coincidence of the worst-case arithmetic, not a second derivation of the same number."

Related, and worth one more sentence: the justification "Ten points is the coarsest width at which a
claim that one method beats another survives a sceptical reader" uses a *single-rate* half-width to
justify a *comparison* claim. Two rates each carrying ±10 points do not resolve a 10-point
difference; the difference's standard error is √2 larger. The draft reaches the right conclusion two
sentences later ("100 trials buys a 20-point effect and nothing finer"), so the fix is to lead with
the comparison framing rather than the width framing.

### 20. No multiplicity anywhere in the protocol

**location** Table 8, all rows; §7.5.

**the problem** §7.4 correctly praises `lbm_careful_examination_2025` for correcting pairwise tests
under Bonferroni, and quotes its warning about measuring statistical noise. Table 8 then prescribes
seven axes, and Table 9 twelve methods, with no statement of what a 95 percent interval means when
84 of them are reported together. At 84 independent 95 percent intervals, four excursions are
expected by construction.

**the fix** One line in Table 8's "reported alongside it" column for task success, and one sentence
in §7.5: "Intervals are marginal. A paper comparing k policies on m tasks corrects for the k(k−1)/2
pairwise tests at a global 95 percent level, as `lbm_careful_examination_2025` does, or states that
its intervals are marginal and not simultaneous."

### 21. Appendix A does not carry the capture caveat

**location** Appendix A, "What this method cannot do".

**the problem** It names three limitations — mention counts are not usage counts, vendor specs are
manufacturer claims, selection favours indexed English preprints. It does not name the one that
governs every number in §7.1 and every bar in Figure 6: that a structured row holds a scalar and a
paper that reports a per-task count, a rubric or a distributed total produces a null.

**the fix** Add the paragraph drafted in finding 1(c). This is the single highest-value edit in the
review: it costs five sentences and it converts §7.1 from a claim the survey cannot support into a
floor it can.

---

## Minor

22. **Figure 6 has six bars; §7.1 calls them five.** "Figure 6 ... draws these five shares from
    `corpus/rows` against the same denominator" follows a list of five items (real robot, trial
    count, unseen objects, criterion, code). The SVG also draws "contact or penetration handled —
    11 (10%)". Fix the count or drop the sixth bar. Bar geometry itself is correct: all six widths
    are `round(n/110 × 380)` to the pixel.

23. **Figure 6's caption is more honest than the body text.** The caption says "Share of the 110
    surveyed method papers **whose note confirms** each item", which is nearly the right framing;
    §7.1 says papers "state" the item. Make the body text match the caption, and make the caption
    exact — the count is from the row, not the note, which is a further step removed.

24. **Figure 1's "simulation only 22" will draw as 23.** The spec says "'real robot' 87 of 110,
    'simulation only' 22 of 110". `fig1()` computes `simonly = N - real` = 23, folding the one row
    with `real_robot: null` into the simulation-only node. 87 + 22 + 1 = 110. Either add the null as
    a dashed node, as the same figure does for `human_data`, or change the generator.

25. **Figure 1 mixes a mention count into a figure of row counts.** Column 2: "Inside each node,
    list the hands that recur, Allegro, Shadow, LEAP, Inspire, taken from `corpus/stats.json`."
    `stats.json` is built by `corpus_stats.py`, which regex-matches every parsed source including
    surveys, simulators and hand papers — Allegro appears in 83 sources there against 35 method
    rows. Take the hand labels from the rows like every other node, or label them as mentions.

26. **§7.4 overstates lbm's Bonferroni.** "corrects all pairwise tests under Bonferroni"; the note
    (line 28) quotes "the confidence level is adjusted for multiplicity via Bonferroni correction
    **unless otherwise noted**". Drop "all".

27. **§7.4's suresim saving is the best case, not the summary.** "saving more than 25 percent of
    hardware trials at a paired correlation of 0.70" is the DP case (ρ = 0.702, Fig. 4-5). The
    paper's own abstract summary is "20–25 % of hardware trials when paired correlation is
    ~0.6–0.7". Quote the range, or say the 25 is the best of the two reported settings.

28. **§7.3's eight-fold penetration discrepancy is also a difference of population.** GRAB's
    3.25 mm is over its captured "use" grasps; OakInk's 2.53 cm is its Table 3 score for the GRAB
    GrabNet split. The draft's caveat is about the distance function only. Add: "and the two are not
    scored over the same grasps."

29. **§5.3.1's latency count includes cells that say there is no latency.** "Only 12 of the 30 rows
    state a latency of any kind" counts 12 non-empty cells in Table 6, but two of them are
    `bidex_teleop_2024` ("claimed low-latency, no number given") and `dexumi_2025` ("no figure").
    Ten rows state a number. The rest of the paragraph's counts are right: 7 rig costs, 13
    trajectory counts, 7 hour counts, and the $399 / $600 / $600 / $4,000 / $6,000 figures all match
    Table 6.

30. **`--derive` prints a line the text never uses.** "n = 30 rollouts -> +/- 0.36 sd". Either use it
    (it would support the sequential-stopping argument) or drop it, so the tool's output and the
    prose stay in one-to-one correspondence, which is the point of having the tool.

31. **The object-level interval is asserted, not derived.** §7.5: "20 objects at 5 trials each gives
    100 trials and an object-level interval near 20 points" uses the Wilson binomial at n = 20
    (19.7 points, so "near 20" is right) but the estimand Table 8 defines is "mean over held-out
    objects of per-object success" with "bootstrap over objects, not trials". Those coincide only if
    each object's outcome is treated as Bernoulli. State the assumption, or give the design effect
    for 5 trials per object.

32. **§7.3 lists three of `toporetarget_2026`'s four reward terms.** "its reward and its five
    termination criteria govern object pose, link position and joint error" — there is also an
    action-smoothness term at weight −0.01 (note line 20). The claim that carries ("never
    penetration") is correct, and the five termination criteria are correct.

---

## What I checked and found sound

I am listing these so the authors do not spend review-response time on them.

- Every Wilson interval in §7.1 and §7.5, to the digit: 39–78 and 58–92 at n = 20; 71–87 and 40–60
  at n = 100; 6.9 points at n = 200; n = 21 / 39 / 93 / 381 for half-widths of 20 / 15 / 10 / 5.
- The unpaired power arithmetic: 93 / 169 / 387. Right for the test that was run (see finding 3 for
  whether it is the right test).
- The continuous-score half-width: 1.96/√100 = 0.196 sd.
- §7.7's cost arithmetic: 2 policies × 3 tasks × 200 rollouts = 1200; 1200 minutes = 20 hours.
- Every corpus tally in §7.1, §7.2 and §7.3 against `corpus/rows/*.json` — 87, 55, 32, 79, 61, 31,
  18, 11, 3/3/5, 37, 25/45, the 5-to-1287 range, the 10/20/70 quartiles and the 14.5-object median
  all reproduce exactly. The complaints above are about what those counts mean, not about the
  counting.
- The named keys in §7.3's penetration taxonomy: all 11, and the 6 + 1 + 4 split, are exactly what
  the rows say.
- Every quoted number from another paper in §7.2, §7.3, §7.4 and §7.7, checked against
  `papers/notes/`: `bench2dex_2026` 48.5 / 19.8 / 27.3 / 19.7 / 72.1 and the 0.5 s dwell;
  `colosseum_2024` 235 × 25, 30–50 percent, ≥75 percent, "one training seed and one evaluation
  seed", "if the model completes the task fully"; `autoeval_2025` 6/50 vs 47/50, 50 trials, ±10
  percent, ~850 episodes / 3 interventions / 24 h, 20 minutes every 6 hours, >2500 rollouts and
  >100 hours; `kress_gazit_policy_eval_2024` 17 percent, 23 of 23, 15/18 vs 11/17, the 0.11
  posterior, and 150/180 vs 110/170; `roboarena_2025` 612 and 4284 with no intervals;
  `lbm_careful_examination_2025` 50 real / 200 sim, ~1800 real rollouts, 9 hardware stations, and
  the "measuring statistical noise" quote; `beyond_binary_success_2026` ~70 percent sim, ~45 percent
  hardware, 286 against 500, the 12–36 per-task range, 18 trials and ~80 trials;
  `suresim_2025`'s rectifier decision rule and the "precludes rigorous statistical inferences"
  quote; `toporetarget_2026` 25 grasps, 1.07 mm, 0.00 percent, 22.22 mm, 96 percent, 1 mm / 30 mm;
  `grab_2020` 4.5 mm and 3.25 ± 0.68 mm and "contact cannot be directly observed"; `oakink_2022`
  2.53 cm and the three metric names; `physhoi_2023`'s zeroed orientation error and the "local
  optimal" quote; `dextrack_2025` 46.70 / 65.48 and the "Despite severe hand-object penetrations"
  quote; `dexverse_2026`'s 0.20 m; `robopianist_2023`'s 5 million samples, ~5 hours and 4 Tesla
  K80s; `simpler_2024`'s ≤15 percent.
- §7.5's seven unseen-object counts ≥ 93 and their values: 225, 241, 241, 360, 500, 2029, 503409.
- `python3 tools/make_eval_tables.py` regenerates Tables 8 and 9 byte-identically to the committed
  files, so the section and the tables have not drifted.
- Table 6's derived counts (12 / 7 / 13 / 7) and Table 5's "7 released code and all 7 disagree".
- §5.2.1 in full: 59 reward-learners, 48 PPO, 4 DAPG, 43 GPU-sim, 36 both, 23 distillation, 16 all
  three, 31 env counts with median 8192 and max 64000, Allegro 35 and 17/31, Shadow 21 and 6, LEAP
  12 and 4. All exact.
- §5.1's thirteen paradigm counts, §2.1's six task-family counts, the 51/56/3 bimanual split, the
  49/53/8 human-data split, 12 parallel-jaw rows, 47 GPU-batched rows of which 19 state no
  environment count, and 221 bibliography entries against 216 rows. All exact.

---

---

## Provenance and a warning about a moving corpus

All counts above were computed on 2026-09-18 against `corpus/rows/*.json` as it stood at commit
`53f6e7c`, with 216 rows of which 110 are method rows. **While this review was being written two
further method rows were added to the corpus**: `groot_n16_2025` and `helix_2025`, both
`class: method`, both `real_robot: true`, both `real_trials: null`. If they stay, every denominator
in section 7 becomes 112 and every percentage in Figure 6 changes: real robot 89/112 = 79 percent,
trial count 55/112 = 49 percent, unseen objects 32/112 = 29 percent, criterion 79/112 = 71 percent,
code 62/112 = 55 percent, penetration 11/112 = 10 percent. Both new rows also fall into exactly the
category finding 1 is about — a real robot with no extractable trial count — so they should be
hand-checked against their notes before the bar is redrawn, not counted as silent.

Regenerate every figure and every count in one pass before submission, and record the corpus commit
in the survey's header line beside the compile date. A survey whose denominators move between
sections and a corpus that grows during drafting are the same problem seen twice.

## Findings by severity

- blocking: 6
- major: 15
- minor: 11
- total: 32

## Every statistic checked

`=` means the draft's value reproduces exactly from the evidence on disk.

| # | location | statistic | draft | recomputed | |
|---|---|---|---|---|---|
| 1 | §7.1 | method rows with a real robot | 87 / 110 = 79% | 87 / 110 = 79.1% | = |
| 2 | §7.1 | rows stating a real trial count | 55 / 110 = 50% | 55 rows, but ≥68 papers state one | **≥62%** |
| 3 | §7.1 | real-robot papers not stating a count | 32 of 87 | ≤19 of 87 | **≤22%** |
| 4 | §7.1 | denominator for the 50% | 110 | should be 87 → 63% (≥78%) | **wrong denom** |
| 5 | §7.1 | rows stating an unseen-object count | 32 / 110 = 29% | 32 / 110 = 29.1% | = |
| 6 | §7.1 | rows stating a success criterion | 79 / 110 = 72% | 79 / 110 = 71.8% | = |
| 7 | §7.1 | rows with no criterion | 31 | 31 nulls, ≥4 do state one | **overstated** |
| 8 | §7.1 | rows releasing code | 61 / 110 = 55% | 61 true, 45 false, 4 null; 58% of settled | **4 unknowns** |
| 9 | §7.1 | trial-count range | 5 to 1287 | 5 to 1287, but units mixed | **not one quantity** |
| 10 | §7.1 | trial-count median / quartiles | 20; 10 and 70 | 20; 10 and 70 | = (units mixed) |
| 11 | §7.1 | Wilson 60% on n=20 | 39 to 78 | 38.7 to 78.1 | = |
| 12 | §7.1 | Wilson 80% on n=20 | 58 to 92 | 58.4 to 91.9 | = |
| 13 | §7.1 | 20-point gap at n=20 is not a separation | asserted | z=1.38, p=0.17 | = (fallacious route) |
| 14 | §7.1 | 2025-26 rows stating a count | 25 of 45 | 25 of 45 | = |
| 15 | §7.1 | 2025-26 median | 20 | 20 | = |
| 16 | §7.1 | "has not improved" | asserted | rate rose 46% → 56% | **contradicted** |
| 17 | §7.1 | rows naming a hand | 103 | 103 | = |
| 18 | §7.1 | distinct hands | 52 | 78 raw strings; no rule on disk | **unreproducible** |
| 19 | §7.1 | Allegro / Shadow / Inspire / LEAP | 35 / 21 / 19 / 12 | 35 / 21 / 19 / 12 | = |
| 20 | §7.2 | unseen-object median | 14.5 | 14.5 | = |
| 21 | §7.2 | rows addressing penetration | 11 of 110 = 10% | 11 of 94 settled = 12%; 16 unknown | **denom** |
| 22 | §7.2 | rows stating an env count | 31 of 110 | 31 | = |
| 23 | §7.2 | rows stating a sim-episode count | 18 of 110 | 18 | = |
| 24 | §7.2 | paper/code disagreements | 37 of 110 | 37 of 61 = 61%; §5.8 says quote 16 | **inflated** |
| 25 | §7.2 | bench2dex matched / shift | 48.5, 19.8, 27.3, 19.7, 72.1 | same | = |
| 26 | §7.2 | autoeval SIMPLER vs real | 6/50, 47/50 | same | = |
| 27 | §7.2 | kress-gazit policy C | 17%, 23 of 23 | same | = |
| 28 | §7.2 | robopianist cost | 5M samples, ~5 h, 4 K80 | same | = |
| 29 | §7.3 | penetration split | 3 / 3 / 5 | 3 / 3 / 5 | = |
| 30 | §7.3 | closed-loop policies remaining | 4 | 4, keys match | = |
| 31 | §7.3 | toporetarget penetration | 1.07 mm, 0.00% | same | = |
| 32 | §7.3 | GeoRT baseline | 22.22 mm, 96% | same | = |
| 33 | §7.3 | toporetarget grasps / bounds | 25; 1 mm, 30 mm | same | = |
| 34 | §7.3 | GRAB penetration / tolerance | 3.25 ± 0.68 mm; 4.5 mm | same | = |
| 35 | §7.3 | OakInk on GRAB split | 2.53 cm | same | = |
| 36 | §7.3 | ratio of the two | about eight | 7.78 | = |
| 37 | §7.3 | dextrack success pair | 46.70 / 65.48 | same | = |
| 38 | §7.4 | kress-gazit pancake | 15/18 vs 11/17, 83 vs 65, 0.11 | same | = |
| 39 | §7.4 | kress-gazit at scale | 150/180 vs 110/170 | same | = |
| 40 | §7.4 | roboarena | 612 comparisons, 4284 rollouts | same | = |
| 41 | §7.4 | colosseum | 235 sets × 25 episodes | same | = |
| 42 | §7.4 | colosseum drops | 30-50%, ≥75% over 14 | same | = |
| 43 | §7.4 | lbm counts | 50 real / 200 sim | same | = |
| 44 | §7.4 | lbm Bonferroni | "all pairwise" | "unless otherwise noted" | **overstated** |
| 45 | §7.4 | autoeval | 50 trials, ±10%, no formula | same | = |
| 46 | §7.4 | suresim saving | >25% at ρ=0.70 | best case; abstract says 20-25% at 0.6-0.7 | **best case** |
| 47 | §7.4 | beyond-binary savings | ~70% sim, ~45% hw, 286 vs 500 | same | = |
| 48 | §7.4 | beyond-binary per-task range | 12 to 36 | 12, 16, 29, 36 | = |
| 49 | §7.4 | beyond-binary roboarena | 18 trials, ~80 trials | same | = |
| 50 | §7.5 | n for half-widths 20/15/10/5 | 21 / 39 / 93 / 381 | 21 / 39 / 93 / 381 | = |
| 51 | §7.5 | Wilson at n=100 | 71-87 and 40-60 | 71.1-86.7, 40.4-59.6 | = |
| 52 | §7.5 | power, 50 vs 70 / 65 / 60 | 93 / 169 / 387 per arm | 93 / 169 / 387 unpaired | = |
| 53 | §7.5 | that calculation's design | "paired" per the tool | McNemar: 37-96 pairs | **wrong test** |
| 54 | §7.5 | sim cell | 200 → 6.9 points | 6.86 | = |
| 55 | §7.5 | perturbation screen | 40 per axis → 15 points | 14.8 for one rate; ratio CI 0.34-1.06 | **wrong statistic** |
| 56 | §7.5 | object-level interval | 20 objects → ~20 points | 19.7 under a Bernoulli assumption | = (unstated) |
| 57 | §7.5 | objects for a 10-point claim | ~93 | 93 | = |
| 58 | §7.5 | rows reaching 93 unseen objects | 7, values listed | 7, values match | = |
| 59 | §7.5 | continuous score at n=100 | ±0.20 sd | 0.196 | = |
| 60 | §7.6 | Table 9 shape | 12 rows, 84 cells | 12 × 7 = 84 | = |
| 61 | §7.6 | Table 9 row 6 (`unidex_2026`) | 34 mentions | 3 under word-boundary | **artefact** |
| 62 | §7.6 | "no number carries all three" | absolute | `dextreme_2022` carries all three | **refuted** |
| 63 | §7.7 | bill for 2 policies × 3 tasks | 1200 rollouts, 20 h | 1200, 20 h | = |
| 64 | §7.7 | corpus median since 2022 | "has not moved" | 10, 27.5, 20, 20, 20 by year | **false** |
| 65 | §7.7 | autoeval throughput | ~850 in 24 h, 3 interventions | same | = |
| 66 | §7.7 | OpenVLA evaluation cost | >2500 rollouts, >100 h | same | = |
| 67 | §7.7 | lbm scale | ~1800 rollouts, 9 stations | same | = |
| 68 | §7.7 | simpler physical-parameter effect | ≤15% | ≤15% | = |
| 69 | Fig 6 | number of bars | "these five shares" | six bars drawn | **mismatch** |
| 70 | Fig 6 | bar widths | — | all six = round(n/110 × 380) | = |
| 71 | Tab 8 | reproducibility rationale | 37 of 110 | 16 of 61 per §5.8 | **inflated** |
| 72 | §1 | RL rows / Isaac Gym rows | 53 / 35 | 53 / **36** | **off by one** |
| 73 | §1 | corpus size | 221 bib, 216 rows | 221 / 216 | = |
| 74 | §1.3 | parallel-jaw rows | 12 of 110 | 12 | = |
| 75 | Fig 1 | human data | 49 / 53 / 8 | 49 / 53 / 8 | = |
| 76 | Fig 1 | embodiment | 56 / 51 / 3 | 56 / 51 / 3 | = |
| 77 | Fig 1 | simulator nodes | 35 / 18 / 6 / 4 / 2 / 2 / 1 / 8 / 3 / 31 | 36 / 16 / 6 / 4 / 2 / 2 / 1 / 5 / 3 / 35 | **4 wrong** |
| 78 | Fig 1 | paradigm nodes | 53 / 27 / 23 / 16 / 14 / 14 / 10 / 8 / 6 / 6 / 5 / 4 / 2 | identical | = |
| 79 | Fig 1 | evaluation nodes | 87 / 22 / 11 / 83 | 87 / 22 (generator draws 23) / 11 / 83 | **null folded** |
| 80 | §2.1 | task families | 55 / 43 / 31 / 12 / 42 / 9 | identical | = |
| 81 | §3.2 | two designs' share | 52 of 103 | 52 with Adroit as Shadow; 49 without | = (rule unstated) |
| 82 | §3.2 | LEAP rows | 11 | 12 | **wrong** |
| 83 | §3.2 | five families' union | 74 of 103 | 75 | **off by one** |
| 84 | §4.2 | Isaac Gym + Isaac Lab | 41 of 110 | 42 | **off by one** |
| 85 | §4.4 | GPU-batched rows, no env count | 47, 19 | 47, 19 | = |
| 86 | §5.1 | paradigm tags | 53 / 27 / 23 / 16 / 14 / 14 / 10 / 8 / 6 / 6 / 5 / 4 / 2 | identical | = |
| 87 | §5.2.1 | reward learners / PPO / DAPG | 59 / 48 / 4 | 59 / 48 / 4 | = |
| 88 | §5.2.1 | GPU sim / both / distil / all three | 43 / 36 / 23 / 16 | 43 / 36 / 23 / 16 | = |
| 89 | §5.2.1 | env counts | 31, median 8192, max 64000 | identical | = |
| 90 | §5.2.1 | Allegro, Shadow, LEAP in reorient | 35&17 / 21&6 / 12&4 | identical | = |
| 91 | §5.3.1 | Table 6 derived counts | 12 latency / 7 cost / 13 traj / 7 hours | 12 cells but 10 numbers; 7 / 13 / 7 | **2 cells empty of a number** |
| 92 | §5.8 | mismatch decomposition | 37 → 16 + 9 + 7 + 3 + 2 | 37 total; decomposition is the draft's | = |
| 93 | §5.8 | reorient code and mismatch | 7 released, all 7 disagree | 7 and 7 in Table 5 | = |
| 94 | §6 | bimanual rows | 51 | 51 | = |
| 95 | §8 | rows that released nothing | 49 | 45 false + 4 null | **unknowns folded** |

## Verdict on capture versus reporting

The survey's coverage statistics are counts of what the extraction captured, and the draft presents
them as counts of what papers reported. The bias is one-directional — every miss turns a reporting
paper into a silent one — and it is large enough to matter, not a rounding concern.

I quantified it on the statistic the draft leads with. Of the 32 method rows that have a real robot
and no trial count, **at least 13 have the count written in their own note**, dropped at the
note → row step because `real_trials` is a single integer and those papers report per-task counts.
The corrected floor is **≥68 of 110 (≥62 percent)** rather than 50 percent, and **≥78 percent of
real-robot papers** rather than 63 percent. The same mechanism reaches at least four of the 31
"no criterion" rows, and the `penetration` and `code_released` fields each carry unknowns (16 and
4) that the percentages quietly convert into negatives.

The direction is what makes this blocking rather than major. Every one of these errors makes the
field look worse at reporting than it is, and the survey's central argument is that the field
reports badly. A reviewer who spot-checks three papers — `pi0_2024`, `gemini_robotics_2025`,
`rdt1b_2024` all state their trial counts plainly — will conclude that the survey's diagnosis was
manufactured by its own pipeline. It was not; it is a schema artefact. But the draft gives a reader
no way to tell those apart, and it must.

The remedy is not a re-extraction, though a re-extraction would be better. It is three sentences of
disclosure plus one hand-audit, and the survey has already written the template for it. §5.8 takes
37 paper/code disagreements, subtracts the 9 that are "limitations of this survey's own parsing",
declares "Sixteen is therefore the number to quote", and adds "it is a floor, because the forty-nine
rows that released nothing cannot be checked at all". That paragraph is the best methodological
writing in the draft. Section 7 needs the identical treatment of its own five bars: audit the nulls
against the notes, publish both numbers, label every coverage figure a floor, and put the reason in
Appendix A's "What this method cannot do". Do that and the weakened claim — at least 38 percent of
method papers with a real robot do not state a trial count, and the median stated count is 20 — is
still damning, still supports every recommendation in Table 8, and is defensible against the first
reviewer who opens a PDF.
