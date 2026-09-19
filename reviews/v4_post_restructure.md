# v4: post-restructure review of the LaTeX edition

Target: `tex/main.pdf`, 43 pages, built 2026-09-18 17:54 from `tex/sections`, `tex/tables`,
`tex/figs`. Reviewed against `corpus/rows/`, `paper/tables/*.md`, `tools/hand_usage.py`,
`tools/make_tables.py`, `tools/check_numbers.py`, `tex/main.aux`, `tex/PERMISSIONS.md`, and every
figure and table page rendered at 100 dpi (300 dpi where a cell was in doubt).

Mechanical checks that came back clean, so they are not itemised below: every `\ref` in
`tex/` resolves (95 labels, 0 undefined); `main.log` carries no undefined reference, no undefined
citation and no error; the build is 43 pages as claimed; the six printed tables are I (task
families), II (protocol), III (matrix), IV (hands available), V (hands announced), VI (simulators),
and all six are reachable.

---

## 1. Section V-H still says ten contradictions, in the sentence that closes the subsection

**Severity: blocker.**

**Location:** `tex/sections/05_training.tex:520-523`, printed p21 left column, final paragraph of
Section V-H ("What the released code says").

> "A reward table is a claim about a training run and the code is a claim about a repository. Here
> the two contradict each other in **ten** cases, in the other **28** the released artefacts do not
> settle the question, and in exactly one, [15], the repository says so itself."

**Problem.** The count was corrected to nine in commit `0c940bd`. Three paragraphs above, the same
subsection says "Nine are contradictions", "Nine is the number to quote" and "Nine of 62 is 15
percent". The closing sentence a reader is most likely to carry away says ten, and its complement
28 is the arithmetic of ten (38 − 10), not of nine (38 − 29). Section VIII-A, the abstract, the
introduction, the conclusion and Figure 1 all say nine.

**Evidence.** `corpus/rows/*.json`: `mismatch_class` counts are contradiction 9, parse-limitation
13, code-absent 8, internal-inconsistency 4, version-skew 4, total 38. `tools/check_numbers.py`
recomputes `contradictions: 9`. The nine contradiction rows are `dexpbt_2023`, `dexpoint_2022`,
`dextreme_2022`, `pddm_2019`, `penspin_2024`, `physhoi_2023`, `pianomime_2024`,
`unidexgrasp_2023`, `visual_dexterity_2022`. Appendix C prints "**contradiction, 9 rows**" and
lists exactly those nine.

**Fix.** `ten` → `nine`, `28` → `29`. The same sentence survives verbatim in the markdown edition
(`paper/sections/05_training.md:430`, `paper/survey.md:1453`); fix both.

---

## 2. "18 of the 33 hand rows" and "7 of those" are 19 and 8; the rule the paper cites mismatches on a substring

**Severity: blocker.**

**Location:** four places, all printing the same pair of numbers.
`tex/sections/abstract.tex:21` ("18 of the 33 hand rows appear in no method row, and 7 of those can
be bought or built today"); `tex/sections/01_introduction.tex:83-85`;
`tex/sections/08_gaps.tex:118-122`; `tex/sections/09_conclusion.tex:35-37`.

**Problem.** `tools/hand_usage.py` — which Section VIII-E names in print as "the rule that decides
used from unused ... so the partition can be recomputed rather than argued about" — matches the
DexHand row with the pattern `dexhand`, and that pattern hits the substring **bi-dexhands** inside
`dp3_2024`'s hand field. Bi-DexHands is a benchmark, not the IoT Design Shop DexHand. DexHand is
therefore counted as used when no method row runs on it. Correcting the false positive moves the
partition from 15 used / 18 unused / 7 unused-but-obtainable to **14 used / 19 unused / 8
unused-but-obtainable**. The 11 unobtainable rows are unaffected, and 19 = 8 + 11 still closes.

**Evidence.** `dp3_2024`'s `hand`: "shadow hand (adroit, **bi-dexhands**, dexdeform, dexmv
domains); allegro hand (...)". `python3 tools/hand_usage.py` returns
`unused_obtainable_keys: ['ruka_2025', 'bidexhand_2025', 'ruka_v2_2026', 'tesollo_dg5f_2024',
'proception_prohand_2026', 'orca_hand_2025', 'unitree_dex5_2025']` — DexHand absent. Table IV as
printed (p36) shows **eight** rows with `uses = 0`: Proception ProHand, BiDexHand, Ruka-v2,
TESOLLO DG-5F, Unitree Dex5-1, ORCA, RUKA, DexHand. The table generator uses a different pattern
(`tools/make_tables.py USES`: `therobotstudio|dexhand v1`) and gets DexHand right.

**Fix.** Tighten `hand_usage.py`'s DexHand pattern to the one `make_tables.py` already uses, rerun
`tools/check_numbers.py`, and change 18 → 19 and 7 → 8 in all four places. See also item 4, which
is the downstream list.

---

## 3. Thirteen of the eighteen reproduced photographs print "permission not yet sought"

**Severity: blocker for posting (not for the argument).**

**Location:** thirteen plates across pp6-31, e.g. p7 under Figure 7 and p25 under Figure 23:

> "*Reproduced from [61]; permission not yet sought, see the register.*"

**Problem.** The paper is to be posted as a preprint. Thirteen third-party photographs and
screenshots are reproduced with the paper's own register saying no permission has been sought; nine
of them sit behind arXiv's non-exclusive licence, which grants a third party nothing, and two need
a publisher request. Posting distributes them.

**Evidence.** `tex/figs/plates.tex` contains 13 `\pending` markers; `tex/PERMISSIONS.md` counts "no
permission needed, attribute under the licence: **7**", "request from the publisher through their
process: **2**", "email the authors: **9**", and states that 9 of the 17 sources "carry only
arXiv's non-exclusive licence to distribute (which grants a third party nothing)".

**Secondary defect in the same place.** Appendix A's "Reproduced figures" subsection
(`appendix_a_method.tex:123-132`) still says "**No** permission to reproduce **any** of them has
been sought yet" and "**Every** reproduced figure is therefore to be read as permission pending".
Seven are now cleared under CC BY and print an attribution line rather than the pending line, so
the appendix contradicts the plates on the facing pages.

**Fix.** Before posting: drop or redraw the 11 uncleared plates, or clear them. Either way rewrite
the Appendix A paragraph to "Seven are reproduced under CC BY 4.0 with attribution; the remaining
eleven are permission pending, and `tex/PERMISSIONS.md` records the licence and the action per
figure."

---

## 4. The list of hands that take zero method rows is wrong in Section III, and differs from the one in Section VIII

**Severity: high.**

**Location:** `tex/sections/03_hands.tex:141-142` and `:266-271` (printed p7 and p8), against
`tex/sections/08_gaps.tex:118-119` (printed p31).

Section III-B: "ORCA, RUKA, Ruka-v2, BiDexHand, **DexHand**, the Tesollo DG-5F and the Unitree Dex5
take none at all."
Section III-F: "**Seven** hands that are sold and documented take zero method rows each: the
Unitree Dex5 ..., the fully actuated Tesollo DG-5F, ORCA, RUKA, Ruka-v2, BiDexHand and
**DexHand**."
Section VIII-E: "**7** documented hands that can be bought or built from published designs take
zero method rows between them: Unitree Dex5, Tesollo DG-5F, **Proception ProHand**, ORCA, RUKA,
RUKA v2, BiDexHand."

**Problem.** Three lists, two memberships. Section III includes DexHand and omits Proception
ProHand; Section VIII does the reverse; Table IV's `uses` column shows both at zero, so the correct
list is eight hands and includes both. The reader who checks the table against either list finds
it wrong.

**Evidence.** Table IV, p36, `uses` column. See item 2 for the generator disagreement behind it.

**Fix.** One list of eight, in both sections, and say "eight" where the text says seven. Generate
the list from the corrected `hand_usage.py` rather than writing it out twice.

---

## 5. Figure 6 and the prose directly beneath it disagree about Shadow, and Figure 6 and Table IV disagree about LEAP

**Severity: high.**

**Location:** page 7. Figure 6's bars read "Shadow or Adroit **24**" and "LEAP **12**". The first
paragraph of Section III-B, five lines under the caption, reads:

> "The Allegro accounts for 35, Shadow for **21**, the Inspire RH56 family for 19, a parallel-jaw
> gripper for 12 and LEAP for 12."

Table IV on p36 gives Shadow **21** and LEAP **11**.

**Problem.** Two generators with two pattern sets, both printed. `tools/hand_usage.py` uses
`shadow|adroit` (24) and `leap` (12); `tools/make_tables.py USES` uses `shadow(?!.*dex-?ee)` (21)
and `\bleap\b` (11). Figure 6 takes the first, Table IV the second, the prose takes Shadow from the
second and LEAP from the first. A reader comparing a figure, a table and a sentence on the same
subject gets three answers.

**Evidence.** Recomputed over `corpus/rows/`: `shadow` → 21, `adroit` → 4, `shadow|adroit` → 24
(dp3_2024 in both); `\bleap\b` → 11, `leap` → 12 (the extra is `teledexter_2026`, whose hand field
reads "also **leaphand** (16-dof)", which is a LEAP hand, so 12 is the right answer and Table IV's
11 is the undercount).

**Fix.** Pick one pattern set, import it in both generators, rebuild. LEAP should read 12
everywhere; decide whether Adroit counts as a Shadow and say so once in the figure caption. Then
fix `03_hands.tex:272-273`, which already reads "a third in LEAP if **eleven** papers is enough"
against its own "LEAP for 12" three subsections earlier.

---

## 6. Section III-A reads four columns out of Table IV that Table IV does not have

**Severity: high.**

**Location:** `tex/sections/03_hands.tex`, printed pp5-7.

- `:25` "Table IV **dates** every other claim." Table IV has no date column; the `claim date`
  column is in Table V.
- `:71-73` "so its force cell is empty and its **payload cell** carries that protocol ... No two
  hands in Table IV report **payload** under the same test either." There is no payload column.
- `:83-91` "Two columns matter before any of the above and were missing. The first is **the rate a
  loop can be closed at** ... The second column **says whether a URDF or MJCF exists** and who ships
  it." Neither column is in Table IV.

**Problem.** All four columns exist in the repository version of the table but not in the printed
one. The prose was written against the wide table and survived the cut to the narrow one.

**Evidence.** Table IV's header, p36: hand, maker, DoF, act. DoF, actuation, mass g, force N, force
kind, tactile, price USD, open HW, status, uses — 13 columns.
`paper/tables/table2_hands_available.md` header: hand, maker, joints, act. DoF, actuators,
actuation, weight g, force N, what the force is, **payload**, **control rate**, **URDF or MJCF**,
tactile, price USD, open HW, status, source, **claim date**, corpus methods using it — 19 columns.

**Fix.** Either restore the four columns to Table IV, or rewrite these four sentences to carry the
values and name the repository: "Shadow closes at 1 kHz over EtherCAT, the Allegro at 333 Hz on its
own CAN clock, and the Tesollo at 250 Hz; Inspire states no rate at all
(`paper/tables/table2_hands_available.md`, the *control rate* column)." Same for payload, URDF and
the claim date, which should say Table V.

---

## 7. Section III-F's emptiness arithmetic is the repository table's, not the printed table's

**Severity: high.**

**Location:** `tex/sections/03_hands.tex:255-258`, printed p8.

> "Table V's emptiness is measurable and part of the same finding. Over the **twelve** specification
> columns, **61** percent of its cells are values no source stated, against **39** percent for the
> hands that can be bought."

**Problem.** Table V's own caption on p37 says "**60 of the 104 cells in the 8 specification columns
(DoF through price) (58%)**", and Table IV's says "**68 of the 160 cells in the 8 specification
columns (42%)**". So the reader is told twelve columns and 61/39 by the prose and eight columns and
58/42 by the two captions a page apart. The prose's figures are the repository table's (12 spec
columns), which is no longer what is printed.

**Evidence.** Captions of Tables IV and V, p36-37. `paper/tables/table2_hands_available.md` has 12
specification columns between `joints` and `price USD`.

**Fix.** "Over the eight specification columns Table V prints, 58 percent of its cells are values
no source stated, against 42 percent for the hands that can be bought. Over the twelve columns the
repository table carries the split is 61 to 39." Keep whichever pair you quote consistent with the
caption on the same page.

---

## 8. Section IV-B reads three things out of Table VI that Table VI no longer carries

**Severity: high.**

**Location:** `tex/sections/04_simulators.tex:208-215`, printed p11.

> "The rest of Table VI is largely empty, and the emptiness is a result. **Sixty-eight of its 165
> cells** are values no parsed source stated, which is 68 of the **150 cells outside the engine-key
> column, or 45 percent**. ... **Four engines state a solver iteration count** and seven ship any
> dexterous hand at all. **The licence column** answers a question a reader choosing an engine
> actually has, and **thirteen of fifteen rows do not answer it**."

**Problem.** Table VI's caption says "**40 of the 105 cells in the 7 property columns (38%)**", and
the table has eight columns: engine, contact model, solver, diff., GPU, dt (s), penetration
exposed, hands. There is no iteration-count column and no licence column. Three of the four claims
in this paragraph cannot be checked against the table the sentence names.

**Evidence.** Table VI, p37, header and caption. `paper/tables/table4_simulators.md` has 11 columns
including `iters` (filled in 4 of 15 rows) and `licence` (filled in 2 of 15) — 15 × 11 = 165 cells,
15 × 10 = 150 outside the key column, which is exactly the prose's arithmetic. The repository table
is the one being described.

**Fix.** Rewrite to "Forty of Table VI's 105 property cells, 38 percent, are values no parsed
source stated. The repository table carries four further columns and is emptier still: 68 of 150,
45 percent. Four of the fifteen engines state a solver iteration count there and only two state a
licence." Cite `paper/tables/table4_simulators.md` once.

---

## 9. Two paragraphs of Section V-B2 describe a reward-term matrix that is not in the paper

**Severity: high.**

**Location:** `tex/sections/05_training.tex:97-135`, printed p15. `tables/table5_rewards.tex` is an
alias for `tables/table4_rewards.tex`, which emits nothing, so nothing appears between the
paragraphs.

> ":104 ... Eight penalise deviation of the hand from a canonical grasp pose, a family the plan for
> **this table** did not anticipate and which had to be added."
> ":113-118 Three **cells** an earlier draft marked `code` **print** `code (0)` instead, because in
> each the term is in the released code with every shipped configuration setting its weight to
> zero ... Marking them `code` would tell a reader the code optimises something the paper does not
> state, and leaving them **blank** would hide a term that is in the file."
> ":133 ViserDex is the cleanest specification **in the table**, with every term, weight and
> equation in one appendix table."

**Problem.** The opening sentence was correctly rescoped ("**The repository** puts the 21 in-hand
reorientation methods against nine recurring term families"), but the three sentences that read
cells out of it were not. A reader is told what three cells print and which row is cleanest in a
table they cannot see, and the `code`/`code (0)`/blank distinction is meaningless without the
marks.

**Evidence.** `tex/tables/table4_rewards.tex`: "Withdrawn from the paper: the reward-term matrix
... This file emits nothing". Rendered p15 shows prose running straight on.

**Fix.** Name the artefact and carry the values: "Three marks that an earlier draft recorded as
`code` are recorded as `code (0)` in `corpus/reward_matrix.json`, because the term ships with every
configuration setting its weight to zero: DeXtreme's `timeout_rew`, DexPBT's `fallPenalty: 0.0` and
PenSpin's `action_penalty_scale: 0.0`." Change "in the table" to "of the 21" for ViserDex, and
"the plan for this table" to "the plan for that matrix".

---

## 10. Section V-C1 says "the table's empty cells are the point" with no table

**Severity: high.**

**Location:** `tex/sections/05_training.tex:198-227`, printed pp16-17.
`tables/table6_teleop.tex` → `tables/table5_teleop.tex`, which emits nothing.

> "**The table's empty cells are the point.** Only 12 of the 30 rows carry a latency cell at all,
> three of those give no number, and only 7 state a rig cost. ... **The column** mixes the two, so
> its spread is not a range."

**Problem.** Both deictics point at a table that is now only in the repository. The paragraph's own
numbers survive, so the argument is recoverable, but "the table's empty cells" and "the column" are
not.

**Evidence.** `tex/tables/table5_teleop.tex`: "Withdrawn from the paper: the teleoperation systems
... This file emits nothing."

**Fix.** "**What the tabulation does not carry is the point.** Only 12 of the 30 rows record a
latency at all ... The *latency* column of `paper/tables/table6_teleop.md` mixes end-to-end figures
with single-stage ones, so its spread is not a range."

---

## 11. Section V-I is a subsection called "The master table" with no table in it

**Severity: high.**

**Location:** `tex/sections/05_training.tex:534-549`, printed p21 left column. The heading, one
paragraph, then Section VI.

**Problem.** The heading promises a table; `tables/table7_methods.tex` emits nothing, so the
subsection ends after four sentences. The paragraph itself is fine and already rescoped ("The
emptiest columns of **the method tabulation**"), but the heading is now false and the subsection
reads as truncated — the clearest place in the paper where the restructure shows.

**Evidence.** Rendered p21; `tex/tables/table6_methods_top.tex` emits nothing.

**Fix.** Retitle to "What the method tabulation does not record" and add one sentence saying where
it is: "All 112 rows, on the columns this paragraph reads, are in `corpus/rows/` and in
`paper/tables/table7_methods.md`; Appendix A-G says how to read them."

---

## 12. The introduction sends the reader to Section 7.3 for the IsaacGymEnvs file and lines, which are in Section IV-B

**Severity: high.**

**Location:** `tex/sections/01_introduction.tex:79-81`, printed p2 left column.

> "NVIDIA's own IsaacGymEnvs repository already computes a per-environment maximum interpenetration
> depth in Warp and gates the policy update on a 1 mm threshold. **Section 7.3 has the file and the
> lines.**"

**Problem.** Section 7.3 is VII-C, "Physical plausibility as a first-class metric" (p26-28). It
names neither a file nor a line. The file and the lines —
`code/md/isaacgym_2021.md`, lines 8809-8862 and 3630, 3753 — are in Section IV-B (p11). The paper
gets this right elsewhere: Section VII-G says "**Section IV-B** shows the depth is computable from
the poses and the meshes in a few lines of Warp".

**Fix.** "Section IV-B has the file and the lines."

---

## 13. Figure 1 and its caption call 29 of the 38 disagreements "withdrawn"

**Severity: high.**

**Location:** `tex/figs/fig_codegap.tex` (the bracket label "**29 withdrawn**" and the legend line
"withdrawn: 13 a limit of this survey's own parse, 8 the component was never released, 4 version
skew, 4 a paper disagreeing with itself") and its caption at
`tex/sections/01_introduction.tex:54-62`, printed p2.

> "9 are contradictions, where the shipped code states a different objective from the published
> one, and 29 are **withdrawn**, most of them about this survey's own parse or about what a
> repository shipped rather than about the work. **Further accusations an earlier draft made were
> withdrawn** under adversarial review ..."

**Problem.** The 29 are not withdrawn accusations. They are the four other classes of disagreement,
and most were never charged as contradictions at all. The accusations actually withdrawn number
eight, and the caption uses "withdrawn" for both in consecutive sentences. In a paper whose case
rests on counting accusations carefully, the headline figure mislabels the survey's own ledger.

**Evidence.** `corpus/rows/*.json` `mismatch_class`: parse-limitation 13, code-absent 8,
version-skew 4, internal-inconsistency 4 — the 29. `mismatch_review` is set on 10 rows, and Section
VIII-A states "The survey has now withdrawn eight accusations in total". Appendix C's per-class
lists confirm the 29 are classified, not retracted.

**Fix.** Relabel the bracket "29 **not a contradiction**" and change `\fnWithdrawn` to
`\fnOtherClass` in `tools/make_finding_figures.py`. Caption: "... and 29 fall in four other
classes, most of them a limit of this survey's own parse or a component a repository never shipped.
Separately, eight accusations an earlier draft made were withdrawn under adversarial review, each
recorded in the accused row's `mismatch_review` field." Note also the stale LaTeX comment at
`01_introduction.tex:41-43`, which still says "the ten whose code contradicts the paper" and "the
28 charges the survey withdrew ... the 10 it kept".

---

## 14. "The first count was sixteen. An adversarial re-reading withdrew seven accusations ... That left ten"

**Severity: high.**

**Location:** `tex/sections/08_gaps.tex:24-30`, printed p31; and the same claim, without the
"ten", at `tex/sections/09_conclusion.tex:9-13`, printed p33.

> "The first count was **sixteen**. An adversarial re-reading withdrew **seven** accusations. [six
> names], and the domain-randomisation half of the charge against DexPBT. ... That left **ten**, and
> ten held until the letters to the authors were drafted."

**Problem.** 16 − 7 = 9, and the text says ten. The reconciliation is that only six of the seven
were whole rows — the DexPBT withdrawal was half a charge and left its row a contradiction — but
nothing on the page says so, and the reader hits a visible arithmetic error in the paragraph whose
job is to prove the accusations were counted carefully. The conclusion has the same premise with
one more withdrawal ("an eighth fell later still"), giving 16 − 8 = 8 against its own "nine are
contradictions" two sentences earlier.

**Evidence.** Section VIII-A's own list is six named rows plus a half-charge; Appendix C shows
DexPBT still classed `contradiction` with a `Review` line reading "the disabled-randomisation half
is withdrawn ... the zeroed reward term stands".

**Fix.** "The first count was sixteen. An adversarial re-reading withdrew six of them outright and
narrowed a seventh, DexPBT, to the half that stands. That left ten, and ten held until the letters
to the authors were drafted." Then make the conclusion say the same thing rather than compressing
it to "withdrew seven accusations".

---

## 15. The conclusion says five works are cited by metadata only; Appendix A says six

**Severity: high.**

**Location:** `tex/sections/09_conclusion.tex:42-43`, printed p33.

> "**Five** works are cited by metadata only and no claim rests on them."

**Problem.** Appendix A (`appendix_a_method.tex:52-63`) says "**Six** works are cited by metadata
only and no claim in this survey rests on their contents", lists five paywalled works plus Hwangbo
2018 on RaiSim, and then adds Ma and Dollar 2011 as "a seventh case with a different cause". The
`README.md` says six. Appendix D says "All **five** are cited by metadata only" but is scoped to
the survey rows only, so it is consistent within itself and the conclusion is the outlier.

**Fix.** "Six works are cited by metadata only, and a seventh, Ma and Dollar 2011, is on disk but
unread; no claim rests on any of them."

---

## 16. "36 run in Isaac Gym" is 35; one Isaac Sim row is misbinned by the checker

**Severity: medium.**

**Location:** three places. `tex/sections/01_introduction.tex:26` ("36 run in Isaac Gym, against 6
on its successor Isaac Lab"); `tex/sections/04_simulators.tex:235-236` ("Thirty-six of the 112
method papers in this corpus run on it"); `tex/sections/05_training.tex:59` ("43 run their own
experiments in a GPU-parallel simulator from the Isaac family or Genesis, and **36** do both").
Figure 2 on p4 prints "Isaac Gym 36".

**Problem.** `tools/check_numbers.py:28-29` tests `"isaac lab" in s or "isaaclab" in s or "isaac
sim" in s or "orbit" in s` and otherwise bins any string containing "isaac" as Isaac Gym.
`dexteleop0_2026`'s `sim` field is "NVIDIA **IsaacSim** 4.5", which has no space, so it falls
through to Isaac Gym. The true Isaac Gym count is 35.

**Evidence.** Enumerating `sim` over the 112 method rows: "Isaac Gym" 15, "IsaacGym" 11, "Isaac Gym
(PhysX)" 4, "NVIDIA Isaac Gym" 3, "Isaac Gym-based legged_gym/rsl_rl" 1, and one mixed string
naming IsaacGym among three engines = 35. `NVIDIA IsaacSim 4.5` is the 36th.

**Fix.** Add `"isaacsim"` to the Isaac Lab / Isaac Sim test in `check_numbers.py:28`, rerun, and
change 36 → 35 in the three sentences and in `tools/make_tikz_figures.py`'s Figure 2 node. The
downstream "Those two simulators carry 42 of the 112 method papers"
(`04_simulators.tex:189-190`) should become "The Isaac family carries 42".

---

## 17. Appendix C points at a column called "in Table 5"

**Severity: medium.**

**Location:** `tex/sections/appendix_c_rewards.tex:18-19`, printed p36.

> "And its `in Table 5` column marks the rows that are also in the reward-term matrix, which covers
> in-hand reorientation only."

**Problem.** There is no Table 5 in the paper. Table V is the announced-hands table, which has
nothing to do with reward terms. The column name is a leftover from the fifteen-table numbering.

**Evidence.** The paper's tables are I to VI (`main.aux`). The reward matrix was withdrawn
(`tex/tables/table4_rewards.tex`).

**Fix.** Rename the column in the generator to `in reward matrix` and change the sentence to "its
`in reward matrix` column marks the rows that are also in the reward-term matrix in
`corpus/reward_matrix.json`, which covers in-hand reorientation only."

---

## 18. Section VII-F's heading fallback prints "Table 9" in the PDF outline

**Severity: medium.**

**Location:** `tex/sections/07_evaluation.tex:453`.

```
\subsection{\texorpdfstring{Table~\ref{tab:matrix}}{Table 9}, an empty results matrix}
```

**Problem.** The `\texorpdfstring` fallback is what hyperref writes to the bookmark and to the PDF
outline. It still says Table 9; the table is Table III. A reader navigating by outline sees a
heading naming a table that does not exist.

**Fix.** `{Table 3}`, or better `{The matrix}` so it does not go stale again.

---

## 19. Section IV-A points at "a fourth item on the figure" that the re-laid-out Figure 11 does not show

**Severity: medium.**

**Location:** `tex/sections/04_simulators.tex:52-62`, printed p9-10.

> "**A fourth item on the figure** is not a source of overlap at all. It is a mismatch between the
> geometry the solver uses and the geometry the renderer draws, and it runs in both directions."

**Problem.** Figure 11 on p10 has exactly three dashed-arrow boxes — prescribed compliance, solver
truncation, velocity-level enforcement — plus a note block headed "Where penetration comes from".
There is no fourth item. Commit `4b1cc1e` cut the diagram "from a prose panel to three labelled
boxes" and the paragraph was not updated. The caption is consistent with the figure ("The dashed
arrows mark the three stages that make overlap"); only the body text is not.

**Fix.** Either restore the fourth box, or rewrite: "One further source of apparent overlap is not
on the figure, because it is not a stage of the step at all: a mismatch between the geometry the
solver uses and the geometry the renderer draws, which runs in both directions."

---

## 20. Section VII-C contradicts itself in one sentence about what the eleven rows score

**Severity: medium.**

**Location:** `tex/sections/07_evaluation.tex:224-228`, printed p27 left column.

> "The finding is narrower than the field and concerns learned closed-loop control: **all eleven
> score a pose or a reference trajectory, four of them are closed-loop policies**, and we found none
> that reports the measurement for rollouts of its own trained policy."

**Problem.** If four are closed-loop policies then not all eleven score a pose or a reference
trajectory; and one of the eleven, Castro et al., is a contact model, which scores neither. The
intended claim — that all eleven measure at the reference rather than at the rollout — is elsewhere
in the same subsection and in Section VIII-B, correctly. This sentence garbles it.

**Evidence.** The paragraph three below names the split itself: "Six of the eleven are grasp
synthesisers or trajectory optimisers ... Castro et al. give a contact model rather than a
controller. That leaves four closed-loop policies."

**Fix.** "all eleven measure at the reference rather than at the rollout — seven of them score a
pose, a reference trajectory or a contact model, and the four that are closed-loop policies score
their inputs — and we found none that reports the measurement for rollouts of its own trained
policy."

---

## 21. The paper numbers its own sections in arabic and prints them in roman

**Severity: medium.**

**Location:** thirteen sentences. The subsection references are the ones that actually break:
`01_introduction.tex:36` "Section 5.8"; `:81` "Section 7.3"; `:146` "Section 7.7";
`08_gaps.tex:107` "section 5.5"; `appendix_c_rewards.tex:25` "Sec. 5.8 and Sec. 8.1". Plus the
section-level "Section 1" through "Section 9" in the introduction roadmap, Section II, Section
VIII-F, Appendix D and the conclusion.

**Problem.** IEEEtran prints I, II, ... IX and V-H, VII-C, VIII-A. A reader looking for "Section
5.8" finds no such heading. The paper already uses the printed form in eleven other places
(Section V-G, V-H, VII-A, VIII-A, VIII-D, IV, III, V-B, V-D), so it is inconsistent with itself.

**Fix.** Convert the survey's own references to the printed form — 5.8 → V-H, 7.3 → IV-B (see item
12), 7.7 → VII-G, 5.5 → V-E, 8.1 → VIII-A, "Section 1" → "Section I" — or, better, replace them
with `\ref` to the existing labels, all of which are defined. References to a *cited paper's* own
sections (Sec.~1.1 of Bicchi, Sec.~IV-C of Zhao) are correct as they stand.

---

## 22. `tools/check_numbers.py` reports zero problems about a document that is not this one

**Severity: medium.**

**Location:** `tools/check_numbers.py:298`, `:238-254`.

**Problem.** The checker reads `paper/survey.md` and five files under `paper/sections/`. It never
opens `tex/`. Its "0 problems" is a statement about the markdown edition only, which is why the
stale "ten cases" of item 1 survives in both editions unflagged, and why nothing caught items 6, 7
or 8. Its own output admits it does not check four of the quantities it computes: "no prose matched
for `hands_unused_unobtainable`, `isaacgym_rows`, `isaaclab_rows`, `method_rows`" — and
`isaacgym_rows` is the one that is wrong (item 16).

**Fix.** Add the `tex/sections/*.tex` files to the corpus the checker scans, stripping `\cite{}`,
`\ref{}` and comments first. Register the quantities that are currently computed but unmatched, and
add the ones this review had to compute by hand: Table IV/V/VI cell counts against their captions,
the per-hand `uses` counts against the figure, and the open-hardware row count.

---

## 23. Section III-E's tactile sentence pair gives two numbers and says which to quote is the larger one

**Severity: medium.**

**Location:** `tex/sections/03_hands.tex:229-230`, printed p8.

> "**Sixty-five** of the 112 method papers mention tactile sensing somewhere, which is the gap worth
> quoting. **Thirty-five** is the count over this survey's notes."

**Problem.** Two figures, no statement of which measures what, and the larger one is 63 rather than
65. As written a reader cannot tell whether 65 counts occurrences in the parsed source and 35 in
the notes, or something else, and "which is the gap worth quoting" attaches to the number that is
wrong.

**Evidence.** Recomputed: the parsed markdown of 63 of the 112 method rows contains "tactile"; the
structured note of 35 of them does. The 35 is right.

**Fix.** "Sixty-three of the 112 method papers use the word tactile somewhere in their parsed text,
and 35 carry it in their structured note. Against the eight that meet the inclusion rule, either
number is the gap worth quoting."

---

## 24. Tables IV, V and VI are first referenced on page 5 and printed on pages 36 and 37, with no signpost at the point of use

**Severity: medium.**

**Location:** `tex/sections/03_hands.tex:23` is the first reference, printed p5; Table IV is p36.
Section III makes thirteen references to Table IV and eight to Table V; Section IV makes six to
Table VI. The only pointer to Appendix B is in the introduction's roadmap on p3.

**Problem.** Sections III and IV are cell-level arguments about tables 31 pages away. The `.tex`
files carry comments saying so ("Table 2, the hands that can be bought or built, is set in Appendix
B rather than here"), but a comment is invisible in print. A reader on p5 has no way to know the
table exists later rather than being missing.

**Fix.** One parenthetical at the first reference in each section: "No degree-of-freedom, force,
weight or price figure in Table IV or Table V (both in Appendix B) was measured by anyone outside
the maker", and the same for Table VI at `04_simulators.tex:74`.

---

## 25. Figure 15's corpus keys are set at 5 pt and are not legible at printed size

**Severity: medium.**

**Location:** `tex/figs/fig_taxonomy.tex:21`,
`key/.style={font=\tiny\ttfamily\color{black!58},anchor=west}`. The figure is `\input` into a
`figure*` without a `\resizebox`, so `\tiny` at IEEEtran's 10 pt base is 5 pt as printed. Printed
p15.

**Problem.** Every leaf's corpus keys — "physhoi_2023, force_grasp_sim2real_2026, dexman_2025, and
17 more" and twenty more such lines — are 5 pt grey typewriter. The caption says "with the corpus
keys at each leaf", so they are meant to be read, and IEEE's own figure guidance asks for 8 pt
minimum. The same `\tiny\ttfamily` style is used for the keys in Figure 20 (`fig_bimanual.tex`),
where there are fewer of them and the result is borderline.

**Fix.** Raise `key` to `\scriptsize` (7 pt) and drop a key or two per leaf to make room, or keep
`\tiny` and move the key lists to the caption. Do not solve it with `\resizebox`, which would
shrink the rest of the figure.

---

## 26. Figure 2's edges are an unreadable tangle and the caption asks the reader to trace them

**Severity: medium.**

**Location:** `tex/figs/fig_field.tex`, printed p4.

> "... and **edges drawn only for routes the corpus actually contains**. **The routes converge**:
> almost everything ends in a policy trained in a GPU simulator and distilled to vision."

**Problem.** At printed size the edges are hairlines confined to four narrow gutters between the
five columns, crossing so densely that no individual route can be followed. The caption's main
claim — that the routes converge — cannot be read off the figure; the reader has to take it on
trust. The node sizing the caption also promises is visible only in the evaluation column.

**Fix.** Either widen the gutters and draw the edges with weight proportional to the count so the
dominant route is visible, or drop the edges, keep the five columns as a counted inventory, and
change the caption to say so ("Five stages of the pipeline with the corpus counts at each; the
routes between them are in `corpus/matrix.json`").

---

## 27. Figure 24's annotation sits at the opposite end of the chart from the bracket it explains

**Severity: medium.**

**Location:** `tex/figs/fig_reporting.tex`, last node,
`\node[anchor=north west,...] at (-2.4,-2.60) {the two a reader needs in order to compare any two
methods};`. Printed p25.

**Problem.** The accent bracket marking the two bottom bars is drawn at x = 6.62-6.72, at the right
edge; its label is placed at x = -2.4, under the left-hand row labels. As rendered the sentence
floats below the chart with nothing connecting it to the bracket, and its left edge also pushes the
figure's bounding box left, so the `\resizebox` shrinks the whole chart to fit it.

**Fix.** Place the annotation at the bracket: `\node[anchor=west,align=left] at (6.86,-1.98)`, wrapped
to two or three short lines, or drop the bracket and set the sentence directly under the two accent
bars.

---

## 28. Section VII-F has three sentence fragments where an em-dash was removed

**Severity: low.**

**Location:** `tex/sections/07_evaluation.tex:466-469`, printed p29.

> "Under the bare substring test an earlier version used, ``UniDex'' matched inside ``UniDexGrasp''
> and ``UniDexGrasp++'', and [186]. **A 2026 paper. Sat sixth in a ranking** over a corpus written
> mostly before it, on 34 mentions that belonged to a different work."

**Problem.** "A 2026 paper." and "Sat sixth in a ranking ..." are not sentences. The clause was
almost certainly a parenthetical joined by dashes, cut by the em-dash removal pass of `e52adba`.

**Fix.** "... and [186], a 2026 paper, which sat sixth in a ranking over a corpus written mostly
before it, on 34 mentions that belonged to a different work."

---

## 29. Table V prints a literal backslash in the Pisa/IIT maker cell

**Severity: low.**

**Location:** `tex/tables/table2_hands_announced.tex`, Pisa/IIT SoftHand row, printed p37:
"Centro E. Piaggio, **Univ.\ Pisa** and IIT". The source is
`Centro E. Piaggio, Univ.\textbackslash{} Pisa and IIT`.

**Problem.** The escaper in `tools/make_tex_tables.py` turned a "/" or a stray "\" in the corpus
maker string into `\textbackslash{}`, which prints as a visible backslash. Confirmed by rendering
the cell at 300 dpi.

**Fix.** Fix the maker string in `corpus/rows/pisa_iit_softhand_2014.json` to "Centro E. Piaggio,
University of Pisa, and IIT" and regenerate. Check the other maker cells for the same escape.

---

## 30. Table III's caption says all 84 cells are empty directly above a filled row

**Severity: low.**

**Location:** `tex/tables/table8_matrix.tex` caption, printed p30.

> "... the 12 most-mentioned dexterous-hand policy methods against the axes of Table II. **All 84
> cells are empty.**"

**Problem.** The row immediately under the header is the worked example, with seven filled cells.
The footnote explains it and Section VII-F explains it, but the caption alone reads as false to
anyone who looks at the table before the text.

**Fix.** "All 84 method cells are empty; the first row is a worked example and every number in it
is fabricated."

---

## 31. "(Table III)" in Section IV-B now collides with the survey's own Table III

**Severity: low.**

**Location:** `tex/sections/04_simulators.tex:93`, printed p10.

> "Le Lidec et al. classify it as CCP-MuJoCo ... in the same family as CCP-Drake, the SAP-style
> scheme **(Table III)**."

**Problem.** It means Le Lidec et al.'s Table III, but the survey's own tables are now numbered in
roman and Table III is the empty results matrix. The nearby "\cite[Table~II]" forms are
unambiguous; this bare one is not. Same risk at `:319` and `:85`, which are protected by their
`\cite`.

**Fix.** "(their Table III)" or `\cite[Table~III]{contact_models_comparison_2023}`.

---

## 32. Section VIII-E says three simulator rows name a real hand; Table VI names six

**Severity: low.**

**Location:** `tex/sections/08_gaps.tex:119-121`, printed p32.

> "Only **three** of the fifteen simulator rows name a real hand at all, and the ones they do name
> are the field's defaults."

**Problem.** Table VI's footnote lists seven engines that ship a hand, six of them real: Genesis
(Shadow), Isaac Gym (Shadow, Allegro, TriFinger), Isaac Lab (KUKA Allegro, ShadowHand, AbilityHand,
Fourier GR1-T2, Unitree Inspire, Unitree trihand), ManiSkill3 (Allegro, Ability, Inspire, Delto,
TriFinger), Newton (Allegro), Orbit (Allegro). Only Brax's is synthetic. Section IV-B says "seven
ship any dexterous hand at all", so the paper disagrees with itself across sections.

**Fix.** "Six of the fifteen simulator rows ship a model of a real hand, and every one of them is
an Allegro, a Shadow, an Ability, an Inspire or a TriFinger." Check whether the intended claim was
about *distinct* hands (the `README.md` says "the simulators name five between them") and say which.

---

## 33. "Certifying that same drop takes 101 per arm by the log-ratio standard error" is a power calculation, not a standard-error one

**Severity: low.**

**Location:** `tex/sections/07_evaluation.tex:420-424`, printed p29.

**Problem.** 101 is right for 80 percent power at α = 0.05 on a log ratio of 0.6 —
`(1.96 + 0.84)² × 3.333 / (ln 0.6)² = 100.1`. The count that makes the confidence interval exclude
1 is about 50. The clause "by the log-ratio standard error" reads as the second calculation and
gives the first, and the surrounding paragraph derives the 40-trial figure from an interval width.
Everything else in Sections VII-A and VII-E checked out exactly (n_min 21/39/93/381, the Wilson
intervals at 20 and 100 trials, the McNemar table 37/57/77/96, the Fisher-z intervals at 100, 130
and 457 pairs, the 342 + 600 = 942 bill and the 1200 comparison).

**Fix.** "Certifying that same drop takes 101 per arm at 80 percent power, or about 50 for an
interval that excludes 1."

---

## 34. Section VIII-G's "45 distinct hand strings" recomputes as 44

**Severity: low.**

**Location:** `tex/sections/08_gaps.tex:147`, printed p32.

> "Fifty-three method rows use human data and name **45** distinct hand strings between them."

**Problem.** 53 is right. Counting distinct non-null `hand` strings over those 53 rows,
case-sensitively and with no normalisation, gives 44. The neighbouring figure in Section VII-A
("The 103 method rows that name their own hand give 78 distinct hand strings") reproduces exactly,
so the rule is the same and the 45 is one out — most likely a null counted as a string.

**Fix.** Recompute and change to 44, or state the rule that makes it 45.

---

## 35. Section VIII-C tells the reader to release rollouts "as the first row of Table III", which is the fabricated worked example

**Severity: low.**

**Location:** `tex/sections/08_gaps.tex:94-96`, printed p32.

**Fix.** "as the first filled row of Table III".

---

## Sections that survived the restructure cleanly

- **Section II (taxonomy, pp3-5).** Table I is present, referenced once, and its six rows match the
  six families in the prose; every count reproduces from `corpus/rows/` (57 grasp, 45
  functional/tool, 31 reorient, 12 track-human-ref, 43 bimanual-coord, 10 handover, 20 other).
  Only the arabic self-references of item 21 touch it.
- **Section VI (bimanual, pp21-23).** The one section that was rescoped correctly throughout: it
  says "the method tabulation carries the bimanual papers on the same columns" and then carries
  every value in prose. The 53 → 28 derivation, the 21/4/1/2 architecture split, the ten bimanual
  datasets and the exclusion list all reproduce, and `check_numbers.py` shape-checks them.
- **Section VII-D and VII-E (statistics and protocol, pp28-30).** Every derived count I recomputed
  is exact apart from item 33. Table II is present, complete and consistent with the prose.
- **Appendix B (pp35-37).** Correctly introduced, and its "Each caption states how many of its own
  cells no source filled" is true of the three captions as printed — it is Sections III and IV that
  quote the other version's figures.
- **Appendix D (p40).** Reads the survey columns out in prose, points at the repository for the
  table, and the "four of the fourteen could not be obtained" reconciles with the four named rows.

---

## Count by severity

| severity | items |
|---|---|
| blocker | 3 (items 1, 2, 3) |
| high | 12 (items 4-15) |
| medium | 12 (items 16-27) |
| low | 8 (items 28-35) |
| **total** | **35** |

## The three most serious

1. **Item 1** — Section V-H's closing sentence still says the paper and the code "contradict each
   other in ten cases". It is the last sentence of the subsection that carries the survey's first
   finding, it contradicts three sentences above it in the same subsection, and it is the exact
   number the paper spent a commit correcting. It also survives in the markdown edition.
2. **Item 2** — the third headline finding, "18 of the 33 hand rows appear in no method row and 7 of
   those can be bought", is 19 and 8. The rule the paper names in print as the reason the partition
   can be recomputed rather than argued about matches `dexhand` against the substring
   `bi-dexhands`. Four places print the wrong pair, and item 4 is the list that inherits it.
3. **Item 3** — thirteen of the eighteen reproduced photographs print "permission not yet sought",
   nine of them from sources that grant a third party nothing, and Appendix A says none of the
   eighteen has been cleared when seven now have. This is the only item that is a reason not to post
   rather than a reason to revise.

## Verdict

Not ready to post, but close, and the remaining work is a day rather than a week. The argument
survived the restructure intact: the three findings are sound, the statistics in Sections VII-D and
VII-E are exact to the digit on every one of the fourteen derivations I recomputed, and Section VI
shows what a correctly rescoped section looks like. What did not survive is the paper's grip on its
own tables. Nine tables left the paper and three moved to the appendix, and the prose that read
cells out of them was not rewritten: Section III reads a date column, a payload column, a control
rate and a URDF column out of a Table IV that has none of them, Section IV-B quotes the repository
table's 165 cells and its licence column against a printed Table VI with 105 cells and no licence
column, and Sections V-B2, V-C1 and V-I discuss a reward matrix, a teleoperation table and a master
table that emit nothing at all — V-I is a subsection heading with no table under it. Two number
errors are worse than cosmetic: the contradiction count reverts to ten in the sentence that closes
the finding, and the hand partition is off by one in both directions because two generators
disagree and one of them matches on a substring. Underneath all of it, `tools/check_numbers.py`
reads `paper/survey.md` and never opens `tex/`, so its zero-problems report was never evidence
about this document; extending it to the LaTeX sources and registering the table-caption cell counts
would have caught roughly half of this list and will stop it recurring. Fix items 1, 2 and 3, sweep
items 4-15, and the paper is postable; the medium and low items can follow in a v2 on arXiv.
