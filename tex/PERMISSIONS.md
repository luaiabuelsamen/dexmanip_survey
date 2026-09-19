# Reproduced figures: licence, permission and action

Every figure in `tex/figs/selected/` is rendered from a source PDF in `papers/pdf/`. The
catalogue at `corpus/figure_catalogue.json` records, per figure, the source key, the page, the
original caption and the sha256 of the PDF it came from; the crop is in `tex/figs/SELECTED.md`
and is rebuilt by `tools/relayout_plates.py`.

**Nothing in this paper waits on a reply.** The paper is posted without a permission request and
without writing to an author, so a figure whose reuse would need one cannot be in it. That is a
decision, not a finding, and it is recorded in `PUBLISHING.md`. **One plate remains, it is CC BY
4.0, and no request is outstanding.**

**What changed, and why this file is short now.** An earlier draft reproduced eighteen plates from
seventeen sources, and eleven of them had an open permission. Seventeen have since been cut. What
was carrying an argument was redrawn as a diagram in the paper's own TikZ style
(`figs/fig_transmission.tex`, `fig_collision.tex`, `fig_tactiledepth.tex`, `fig_contactlabel.tex`,
`fig_retarget.tex`), and what was illustrating a point the prose already made was dropped.
Redrawing removes the permission question outright, which is why it is the right answer for any
figure that is a diagram rather than a photograph; where the argument was about physical objects
and the corpus does not hold the measurements to draw them, the figure was dropped instead of
invented. The last two to go were:

- **`hand_scale_to_human.png`** (`leap_hand_2023` Fig. 3, arXiv non-exclusive licence) —
  **dropped.** Five research hands photographed to scale beside a human hand and a ruler, arguing
  that a count of actuated degrees of freedom says nothing about physical size. A to-scale outline
  drawing was the obvious redraw and cannot be made honestly: no row in `corpus/rows/` states a
  hand's length or a width, there is no dimension field in the extraction schema and no dimension
  column in either hand table, so every envelope in such a drawing would have been invented. The
  argument survives in prose in Sec.~III, which now says outright that the one specification a
  reader could hold against their own hand is the one nobody publishes.
- **`teleop_retarget_artifacts.png`** (`toporetarget_2026` Fig. 3, arXiv non-exclusive licence) —
  **redrawn** as `tex/figs/fig_retarget.tex`. The photograph showed a retargeted fingertip driven
  through the temple of a pair of spectacles while the joint-angle error reported the pose as
  good. The mechanism behind that is geometric and is the paper's own argument, so the drawing
  puts the metric and the geometry side by side, which the photograph could not: errors small
  enough to pass at every joint compose along the finger into a fingertip displacement larger than
  a thin object is thick.

The files for the seventeen cut plates were deleted from `tex/figs/selected/` and their entries
removed from `tools/relayout_plates.py`, so nothing unlicensed ships in the arXiv source and a run
of that script cannot put one back. Their catalogue entries are untouched and any of them can be
re-rendered from `papers/pdf/` if a decision is reversed.

**What was actually checked, and when.** On **2026-09-18** the arXiv abstract page of every source
with an arXiv identifier was fetched and the licence statement in its `abs-license` block read
directly (the `href` of "view license"). The licence column below quotes what that page states and
gives the URL the statement was read from. Venue and arXiv identifier come from `corpus/bib.json`;
the *licence* comes from the page. The rows for the cut plates were removed with the plates;
nothing below is inferred from a row that is gone.

**This is not legal advice.** It is a record of what a licence page says. The author should confirm
anything that matters — in particular whether a figure contains third-party material that the
paper's own CC licence does not cover.

## Counts

| category | figures |
|---|---|
| no permission needed, attribute under the licence | **1** |
| request from the publisher through their process | **0** |
| email the authors | **0** |
| redraw or drop | **0** (both figures that needed an email have been redrawn or dropped) |

The 1 remaining figure comes from 1 source, and **that arXiv posting is CC BY 4.0**. No email and
no publisher request is left in the paper.

## The decision table

"From" says which artefact the file in `tex/figs/selected/` was rendered from, because the preprint
and the published version are different works with different rights holders.

| figure | source key | from | licence found (URL read) | permission required? | action |
|---|---|---|---|---|---|
| `bimanual_grasp_penetration.png` | `bimangrasp_2024` | **preprint** (arXiv 2411.15903). Published version: IEEE RA-L 9(12):11377–11384, 2024, DOI 10.1109/LRA.2024.3490393, publisher **IEEE** | **CC BY 4.0 on the preprint** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/2411.15903`. The RA-L version is under IEEE copyright and would need RightsLink; the file here is the preprint | no, for the preprint | **no permission needed, attribute under the licence** — credit arXiv:2411.15903 as the source, with the RA-L citation alongside for the reader |

## The attribution string for the cleared figure

CC BY 4.0 requires, in a manner reasonable to the medium: the creator's name, the title of the
work, a link to the material, the licence name **with a link**, and an indication if changes were
made. The crop recorded in `tex/figs/SELECTED.md` is a change, so the string below names it. Use it
verbatim as the second argument of `\licensed` (see `tex/preamble.tex`); the numeric `\cite` stays
in the caption for the reader.

- **`bimanual_grasp_penetration.png`** — Fig. 9 of Y. Shao and C. Xiao, "Bimanual Grasp Synthesis
  for Dexterous Robot Hands", arXiv:2411.15903, licensed under CC BY 4.0
  (`https://creativecommons.org/licenses/by/4.0/`); panels (A) and (C) of Fig. 9 only.

## What these rows rest on, and what they do not

- The licence column is a direct reading of a licence page on 2026-09-18, with the URL given.
  Nothing in it is inferred from the venue or from a sibling paper.
- arXiv licences are chosen per submission **and per version**. The row reflects the licence shown
  on the abstract page for the current version at the date above. If the plate is re-rendered from
  a different version, re-check.
- A CC licence on a paper covers the authors' own content. If a figure embeds third-party material,
  the CC grant does not reach it; CC BY also does not grant trademark or patent rights. The two
  rows that carried an NVIDIA trademark note were both cut, so no such note remains.
- Where a published version exists, its licence was not checked: the row that names a publisher
  names it as a *route*, not as a finding.
- The file in `tex/figs/selected/` was rendered from `papers/pdf/bimangrasp_2024.pdf`, whose sha256
  is recorded in `corpus/figure_catalogue.json`. A crop does not create a new work and does not
  change the permission needed, but it *is* a change that CC attribution must declare.
- The build does not enforce any of this, and the plate does not print a status: its caption
  credits its source and prints the attribution the licence asks for. There is no open action left
  for this file to record.
