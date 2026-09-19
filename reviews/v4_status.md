# v4: what happened to every item

`reviews/v4_post_restructure.md` raised 35 items against a 43-page build of `tex/main.pdf` dated
2026-09-18 17:54. Its three blockers and its twelve high-severity items were addressed in commit
`670c827`. This file records the other twenty, items 16 to 35, and the markdown edition's own
consistency, which the review did not cover.

Every item was checked against the *current* text before anything was changed. The paper moved a
long way after the review was written: 43 pages to 40, eighteen borrowed photographs to three,
fifteen tables to seven, seventy-four headings to thirty-eight, the gaps section merged into the
conclusion, and two sections rebalanced into a new Appendix E. Six of the twenty items had already
been carried off by those changes, and one of the review's prescriptions would have introduced an
error if applied.

**Tally: 14 fixed, 6 already resolved by the restructuring, 0 items declined outright.** Three of
the review's specific prescriptions were declined inside items that were otherwise handled, and one
issue found outside the review was declined. Each is argued below.

Verification after the pass: `tools/check_numbers.py` 0 problems over both editions,
`tools/check_notes.py` 219 notes 0 flagged, `bash tools/build_tex.sh` clean with 0 undefined
references, 0 undefined citations, 0 errors and no overfull box above 20 pt.

---

## 16. "36 run in Isaac Gym" is 35 — already resolved, with one prescribed edit declined

Two of the three places the review named were corrected in `670c827`, together with the binning bug
behind them. `tools/check_numbers.py:28` now tests `isaacsim` as well as `isaac sim`, so
`dexteleop0_2026`'s `NVIDIA IsaacSim 4.5` no longer falls through to Isaac Gym;
`tools/make_tikz_figures.py:231` carries the same test, so Figure 1 prints Isaac Gym 35 and Isaac
Lab or Sim 7. The introduction says 35 and Section IV-C says "Thirty-five of the 112 method papers
in this corpus run on it". Rendered page 2 confirms the figure node.

**The third edit is declined.** The review read `05_training.tex:59` — "Forty-three run their own
experiments in a GPU-parallel simulator from the Isaac family or Genesis, and 36 do both" — as a
third printing of the Isaac Gym count and asked for 36 → 35. It is a different quantity. "Both"
means PPO *and* a GPU-parallel simulator, and recomputing over `corpus/rows/` gives 48 rows whose
`algorithm` names PPO on a word boundary, 43 whose `sim` names the Isaac family or Genesis, and 36
in the intersection. Changing it to 35 would have put a wrong number in a sentence that was right.
The quantity `isaacgym_rows` is now registered in the checker, so the two are told apart
mechanically.

## 17. Appendix C points at a column called "in Table 5" — already resolved

`tools/make_appendices.py:173` renames the column to `in reward matrix` and `paper/APPENDIX_C.md`
prints it under that name. The LaTeX Appendix C no longer reads a column out of the extraction at
all: it says the extraction "is in the repository rather than here". The string `in Table 5` appears
in neither edition.

## 18. Section VII-F's heading fallback prints "Table 9" in the PDF outline — already resolved

The heading-renaming pass replaced `\subsection{\texorpdfstring{Table~\ref{tab:matrix}}{Table 9}, an
empty results matrix}` with the noun phrase "The results matrix, and what filling it would cost".
No `\texorpdfstring` survives anywhere in `tex/sections/`, and `tex/main.out` carries no bookmark
naming a table.

## 19. Section IV-A points at "a fourth item on the figure" — fixed

The LaTeX edition had been rewritten. The markdown edition had not, and `paper/figures/fig3_sim_step.svg`
draws three dashed stages and a three-bullet note block exactly as the LaTeX one does, so the
markdown sentence pointed at an item that is not on its figure either. `paper/sections/04_simulators.md`
now carries the LaTeX wording: "A fourth thing is not on the figure, because it is not a stage of
the step and not a source of overlap".

## 20. Section VII-C contradicts itself about what the eleven rows score — fixed

Both editions still said "all eleven score a pose or a reference trajectory, four of them are
closed-loop policies", which cannot both hold, and the same subsection three paragraphs down gives
the split as six synthesisers or trajectory optimisers, one contact model and four closed-loop
policies. Rewritten in both editions to the claim that is actually true of all eleven:

> all eleven measure at the reference rather than at the rollout, seven of them scoring a pose, a
> trajectory or a contact model before anything executes and the four that are closed-loop policies
> scoring the references they were given

6 + 1 = 7 and 7 + 4 = 11, and the sentence now says the same thing as Section VIII-B and as the
reference-versus-rollout frame it belongs to.

## 21. Arabic section numbers where IEEEtran prints roman — fixed

Nine of the thirteen had gone with the headings they lived in. Four printed references remained:
`02_taxonomy.tex:53` and `:98` ("Section 6") and `:192` ("Section 7"), and
`appendix_d_surveys.tex:36` ("Section 1"). All four are now `Section~\ref{...}` against labels that
already existed, so they print VI, VI, VII and I and cannot go stale again. The remaining
`Section N` strings in `tex/sections/` are file-header comments, and every `Sec.~N.N` is a cited
paper's own section, which the review said was correct as it stands.

## 22. The number checker reports zero problems about a document that is not this one — fixed

The first half was done in `670c827`: the checker reads `tex/sections/*.tex` as well as
`paper/survey.md`, stripping commands and comments, and reports per edition. This pass did the rest.

*The unregistered quantities.* The checker had been printing "no prose in either edition matched
`hands_unused_obtainable`, `hands_unused_unobtainable`, `isaacgym_rows`, `isaaclab_rows`,
`method_rows`" — five quantities it computed and never checked, one of which (`isaacgym_rows`) was
the wrong one. All five now carry patterns against the sentences that print them, and the
"no prose matched" line is gone. Two more were added, `open_hw_hands` and `open_hw_available`, for
the "six rows are open hardware, and LEAP Hand V2 is a seventh" sentence the review asked for; both
reproduce.

*The table captions.* A new check, `caption_problems()`, reads the empty-cell count out of each
printed table's own generated caption, works out the share it implies, and requires the section that
argues from that table to state it. Six tables are registered, three per edition, because the two
editions print different column sets and so different shares. It fired once on a live defect: the
markdown Section 4.2 quoted 46 percent, its share over the 150 cells outside the key column, and
never stated the 41 percent its own Table 4 footer counts. Fixed by stating both. Injecting the
exact defect of item 8 into a caption makes the check fail, as it should.

*The two pattern sets.* Item 2's blocker was `tools/hand_usage.py` and `tools/make_tables.py`
keeping one regular expression per hand each and drifting apart. Both were corrected but both still
exist. A new check, `pattern_problems()`, runs the two sets over the method rows and requires them
to place all 33 hands on the same side of used and unused. Restoring the `dexhand` substring pattern
makes it fail, naming the hand and both files.

**The review's third sub-request is declined as written.** It asked for "the per-hand `uses` counts
against the figure". The figure cannot disagree with the table any more: `tools/make_tikz_figures.py:90`
imports `USES` from `make_tables` rather than keeping a second set, which is what `670c827` did for
item 5. A check comparing the figure's numbers with the table's would compare a value with itself.
The remaining second set is `hand_usage.py`'s, and that is what the new check guards.

## 23. Section III-E's tactile pair gives two numbers and says the larger is the one to quote — fixed

The larger was wrong. Recomputed: the parsed markdown of 63 of the 112 method rows contains
"tactile", and the structured note of 35 does. Both editions now read:

> Sixty-three of the 112 method papers use the word tactile somewhere in their parsed text and 35
> carry it in their structured note. Against the eight that meet the rule above, either number is
> the gap worth quoting.

Each number now says what it measures, and the sentence no longer picks the wrong one.

## 24. Tables IV, V and VI referenced on page 5 and printed on pages 36 and 37 — already resolved

`670c827` added the parenthetical the review asked for, at the first reference in each section.
`03_hands.tex:19` reads "No degree-of-freedom, force, weight or price figure in
Table~\ref{tab:hands-available} or Table~\ref{tab:hands-announced}, both set in
Appendix~\ref{app:tables}, was measured by anyone outside the maker", and `04_simulators.tex:82`
reads "Table~\ref{tab:simulators}, set in Appendix~\ref{app:tables}, is the engine-by-engine
comparison".

## 25. Figure 15's corpus keys are 5 pt and not legible at printed size — fixed

`key` was `\tiny\ttfamily`, which is 5 pt against IEEEtran's 10 pt base, in a `figure*` with no
`\resizebox`, so it printed at 5 pt. Raised to `\scriptsize`, 7 pt, which is IEEE's stated minimum.
The width that bought is paid for by printing two keys a leaf and counting the remainder instead of
five: the widest key line now ends at 15.2 cm against the cross-link gutter at 16.2 cm, measured
from the character widths and confirmed by rendering page 14 at 400 dpi. One line, the
teacher-student leaf, was given its two shortest keys to clear a crossing curve. The caption now
says what the leaves carry: "each leaf names two of its corpus keys and counts the rest". The full
per-leaf lists are in `corpus/rows/` and in the markdown edition's own Figure 4, which is read on a
screen and keeps five. `\resizebox` was not used, as the review asked.

`fig_bimanual.tex` keeps `\tiny` for its four key nodes. The review called those borderline and they
are: four short stacked lines in a `figure*` with no competition for width. Raising them would have
forced the panels apart for no legibility the reader lacks.

## 26. Figure 2's edges are an unreadable tangle and the caption asks the reader to trace them — already resolved

Commit `de81e40` redrew it. `tools/make_tikz_figures.py` now draws each route at a stroke
proportional to its share of the heaviest route, with a floor of 0.4 pt and 40 per cent black,
"which is the weight that survives print", and spreads the routes along the edge of each box so a
single one can be followed. The caption no longer claims "the routes converge" and no longer asks
the reader to trace anything: it says nodes are sized by corpus papers, edges are drawn only for
routes the corpus contains, and each column head names the section that covers it. Rendered page 2
confirms the dominant route is followable across all four gutters.

## 27. Figure 24's annotation sits at the opposite end of the chart from its bracket — fixed, by a different remedy

The defect was real: the bracket was at x = 6.62 and its sentence at x = −2.4, under the row labels,
with nothing joining them.

**The review's prescribed placement is declined.** Moving the node to `(6.86,-1.98)` beside the
bracket would push the bounding box from 10.3 cm to about 12.3 cm wide, and the figure is set with
`\resizebox{\columnwidth}`, so every label in it would shrink from about 6 pt to about 5 pt. The
generator's own comment says this chart's text "is the smallest in the paper and must not be shrunk
further". Trading the whole chart's legibility for the annotation's position is a bad trade.

Instead the annotation now sits directly under the bar track, at x = 0.12, wrapped to the track's
own 5.2 cm width, and names the colour rather than the bracket: "the two rows in this colour are the
pair a reader needs in order to compare any two methods". Both rows are already drawn in the accent
colour, labels, bars and numbers alike, so the reference resolves by looking. The bounding box is
unchanged and the chart did not shrink. Rendered page 24 confirms it.

## 28. Three sentence fragments in Section VII-F — fixed

"and [186]. A 2026 paper. Sat sixth in a ranking" is one sentence with its joints cut. The clause
also read as though "UniDex" had matched inside the 2026 paper's own name, when the point is that
the substring test put that paper sixth on 34 mentions belonging to other work. Both editions now
read "so \cite{unidex_2026}, a 2026 paper, sat sixth in a ranking over a corpus written mostly
before it, on 34 mentions that belonged to a different work."

## 29. Table V prints a literal backslash in the Pisa/IIT maker cell — fixed

The corpus string was innocent. `tools/make_tex_tables.py`'s `MAKER_ABBREV` rewrote "University of
Pisa" to `Univ.\ Pisa` with a LaTeX control space, and `tex()` escapes the cell *after* the
abbreviations run, so the backslash became `\textbackslash{}`. The replacements are now plain text,
`Univ. \1` and `Inst. Tech.`, with a comment saying why they must be. Regenerated: the cell prints
"Centro E. Piaggio, Univ. Pisa and IIT", confirmed in the rendered table. No other maker cell
carried the escape.

## 30. Table III's caption says all 84 cells are empty above a filled row — fixed

The generator's own comment already said "the caption says which 84"; the caption-capping pass had
cut it back to "All 84 empty." The caption is now "The matrix, for someone else to fill: 12 methods
against Table~\ref{tab:protocol}. All 84 method cells empty; row one fabricated." That is 20 words,
which is the cap `write_table` asserts, so the longer wording the review suggested would not build.
Confirmed in the rendered table: the caption no longer reads as false above the worked example.

## 31. "(Table III)" in Section IV-B collides with the survey's own Table III — already resolved

`04_simulators.tex:97` now reads `\cite[Table~III]{contact_models_comparison_2023}`, which prints
the reference number with the table and cannot be mistaken for the survey's own. No bare
"(Table III)" remains in either edition.

## 32. Section VIII-E says three simulator rows name a real hand; Table VI names six — fixed

Both editions said three, the printed table's own note lists seven engines shipping a first-party
hand model, and Section IV-B says seven. Recounted from the generated note: Brax ships a synthetic
four-fingered claw and the other six ship real hands, and every one of those six ships an Allegro or
a Shadow. Of the 33 tabulated hands, four appear in any engine at all: Shadow, Allegro, Inspire and
Ability. Both editions now read:

> Seven of the fifteen simulator rows ship a first-party hand model at all, six of those hands are
> real, Brax's being a synthetic claw, and every one of the six is an Allegro or a Shadow; only four
> of the 33 tabulated hands appear in any engine.

`README.md`'s "the simulators name five between them" was the same claim at a third value and is now
four, which is the one the corpus supports.

## 33. "101 per arm by the log-ratio standard error" is a power calculation — fixed

The review is right and the arithmetic reproduces both ways. At a 0.50 anchor falling to 0.30,
`Var(ln RR) = 3.3333/n`, so 80 percent power at α = 0.05 needs
`(1.96 + 0.8416)² × 3.3333 / (ln 0.6)² = 100.3`, and an interval that merely excludes 1 needs
`n > (1.96 × √3.3333 / |ln 0.6|)² = 49.1`. The sentence moved into Appendix E with the rest of the
derivation and still named the wrong mechanism. Both editions now read "Certifying that same drop
takes 101 per arm at 80 percent power, or about 50 for an interval that merely excludes 1". The
prescription of 101 in the protocol table is unchanged, and the 40-trial interval quoted just above
it, 0.34 to 1.06, reproduces exactly.

## 34. Section VIII-G's "45 distinct hand strings" recomputes as 44 — fixed

The gaps section carrying it was merged into the conclusion and the sentence moved to Section V-C in
both editions, where it still said 45. Recomputed over the 53 rows that use human data: 3 have a
null `hand` and the other 50 give 44 distinct strings, case-sensitive and unnormalised, which is the
same rule that reproduces the neighbouring 103 → 78. The null was being counted. Both editions now
say 44. The "twenty of those appear in Table 6" and "the other 33" in the same sentence are over 53
and are unaffected.

## 35. "as the first row of Table III" is the fabricated worked example — fixed

Both editions now say "release the rollouts as the first measured row", which is what the sentence
means and is not the worked example. "First filled row", which the review suggested, would still
have named the worked example, whose cells are filled.

---

## Beyond the review: the markdown edition after the restructure

The markdown edition at `paper/` is the one the reviewers read, and the LaTeX edition diverged from
it when the gaps section merged into the conclusion and Appendix E appeared. It was audited in full.

**What is sound.** `tools/assemble.py` produces a document whose numbering matches its own text:
sections 1 to 8 with their subsections, appendices A to E, and every one of the 36 numbered headings
resolvable. Every `section N.N` and `§N.N` reference in the assembled `paper/survey.md` resolves to a
heading that exists; so does every `Table N` for N in 1 to 11 and every `Figure N` for N in 1 to 6.
The only apparent misses are a cited paper's own "Appendix Table 12" and "Appendix A.1", quoted
inside table cells. The six figure SVGs carry internal titles numbered 1 to 6 in the order they are
inlined. No reference to the removed gaps section or to a section 9 survives anywhere, and the two
sentences that point at Appendix E point at the right place.

**What was broken and is fixed.**

- Figure 5's subtitle said its counts were "the 25 corpus papers" while all four of its panels
  printed "of 28", and its first panel listed `deximit_2026`, which both editions' prose classes as
  a row whose note never says which architecture it uses. `tools/make_diagrams.py` now states the 28
  denominator, names `asymdex_2024` as the row drawn twice, and lists `groot_n1_2025` in the first
  panel. The subtitle was split over two lines because one line of it ran past the 940 px frame, and
  the panels moved down 16 px to make room.
- Both editions introduced that figure with "Every row of the 28 is assigned to exactly one of
  them", which the figure does not show: `asymdex_2024` is in two panels, the two unstated rows are
  in none, and 21 + 4 + 1 + 1 is 27. The architecture split *is* a partition, into 21 / 4 / 1 / 2,
  and `check_numbers.py` shape-checks it; the figure's fourth panel is the relative frame, which is a
  second mechanism of the third panel's single row. Both editions now say so, and both captions say
  the panels are not a partition.
- `README.md` still stated the headline as "Ten of the sixty-two method papers ... contradict" and
  "the seven accusations this survey withdrew", against nine and eight everywhere in the paper. Both
  corrected. `PUBLISHING.md` carried the same two numbers in its advice about what to say publicly
  and is corrected to match.
- The markdown Section 4.2 never stated the 41 percent its own Table 4 footer counts, which the new
  caption check caught.

**Declined: the markdown edition's tables print out of numerical order.** They appear as 1, 2, 3, 4,
7, 5, 6, 11, 8, 9, 10: Table 7 is in section 5.1 ahead of Tables 5 and 6, and Table 11 is in 5.6
ahead of 8, 9 and 10. This is legacy of the fifteen-table plan the numbers were assigned under, not
damage from the restructure, and every reference to every one of them resolves. Renumbering would
touch seven generated table files, about sixty prose references across both the sections and the
appendices, two generators, and the path `paper/tables/table5_rewards.md` that
`check_numbers.py`'s `REQUIRED_IN` pins. That is a large mechanical change with real chances of
introducing exactly the kind of dangling reference this pass exists to remove, on a document being
published now, in a checkout another lane is editing. It is a clean one-commit change for anyone who
wants it later; it is not worth the risk today.
