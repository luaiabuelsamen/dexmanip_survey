# Reproduced figures: licence, permission and action

Every figure in `tex/figs/selected/` is rendered from a source PDF in `papers/pdf/`. The
catalogue at `corpus/figure_catalogue.json` records, per figure, the source key, the page, the
original caption and the sha256 of the PDF it came from; the crops are in `tex/figs/SELECTED.md`
and are rebuilt by `tools/relayout_plates.py`.

**What changed, and why this file is short now.** An earlier draft of the paper reproduced
eighteen plates from seventeen sources, and eleven of them had an open permission. Fifteen have
since been cut: what was carrying an argument was redrawn as a diagram in the paper's own TikZ
style (`figs/fig_transmission.tex`, `fig_collision.tex`, `fig_tactiledepth.tex`,
`fig_contactlabel.tex`), and what was illustrating a point the prose already made was dropped.
Redrawing removes the permission question outright, which is why it is the right answer for any
figure that is a diagram rather than a photograph. **Three plates remain, and two of them still
need an email.** The files for the fifteen cut plates were deleted from `tex/figs/selected/`, so
nothing unlicensed ships in the arXiv source; their catalogue entries are untouched and any of
them can be re-rendered from `papers/pdf/` if a decision is reversed.

**What was actually checked, and when.** On **2026-09-18** the arXiv abstract page of every source
with an arXiv identifier was fetched and the licence statement in its `abs-license` block read
directly (the `href` of "view license"). The licence column below quotes what those pages state
and gives the URL the statement was read from. Venue and arXiv identifier come from
`corpus/bib.json`; the *licence* comes from the page. The rows for the fifteen cut plates were
removed with the plates; nothing below is inferred from a row that is gone.

**This is not legal advice.** It is a record of what licence pages say. The author should confirm
anything that matters — in particular whether a figure contains third-party material that the
paper's own CC licence does not cover.

## Counts

| category | figures |
|---|---|
| no permission needed, attribute under the licence | **1** |
| request from the publisher through their process | **0** |
| email the authors | **2** |
| redraw or drop | **0** (the fallback for either of the 2 above that does not come back in time) |

Of the 2 distinct sources behind the 3 figures: **1 arXiv posting is CC BY 4.0** and **1 carries
only arXiv's non-exclusive licence to distribute** (which grants a third party nothing). Both
remaining actions are an email to authors; no publisher request is left in the paper.

## The decision table

Sorted so that the row needing no action comes first. "From" says which artefact the file in
`tex/figs/selected/` was rendered from, because the preprint and the published version are
different works with different rights holders.

| figure | source key | from | licence found (URL read) | permission required? | action |
|---|---|---|---|---|---|
| `bimanual_grasp_penetration.png` | `bimangrasp_2024` | **preprint** (arXiv 2411.15903). Published version: IEEE RA-L 9(12):11377–11384, 2024, DOI 10.1109/LRA.2024.3490393, publisher **IEEE** | **CC BY 4.0 on the preprint** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/2411.15903`. The RA-L version is under IEEE copyright and would need RightsLink; the file here is the preprint | no, for the preprint | **no permission needed, attribute under the licence** — credit arXiv:2411.15903 as the source, with the RA-L citation alongside for the reader |
| `hand_scale_to_human.png` | `leap_hand_2023` | preprint (arXiv 2309.06440); published at RSS 2023 (author-hosted proceedings, no publisher transfer recorded) | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2309.06440` | **yes** | **email the authors** (Shaw, Agarwal, Pathak). Note the *hardware* is open-licensed; that says nothing about the figure. The second LEAP plate that used to share this request has been cut, so this is now a one-figure ask |
| `teleop_retarget_artifacts.png` | `toporetarget_2026` | preprint (arXiv 2606.16272); no venue recorded | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2606.16272` | **yes** | **email the authors** (Wu et al.). The ask is now for one cell of Fig. 3 rather than the whole grid |

## The attribution string for the cleared figure

CC BY 4.0 requires, in a manner reasonable to the medium: the creator's name, the title of the
work, a link to the material, the licence name **with a link**, and an indication if changes were
made. The crop in `tex/figs/SELECTED.md` is a change, so the string below names it. Use it
verbatim as the second argument of `\licensed` (see `tex/preamble.tex`); the numeric `\cite` stays
in the caption for the reader.

- **`bimanual_grasp_penetration.png`** — Fig. 9 of Y. Shao and C. Xiao, "Bimanual Grasp Synthesis
  for Dexterous Robot Hands", arXiv:2411.15903, licensed under CC BY 4.0
  (`https://creativecommons.org/licenses/by/4.0/`); panels (A) and (C) of Fig. 9 only.

The other two plates print `\src` alone and no attribution line, because neither licence grants
one to print. If either request comes back, add the string the reply asks for here and to the
plate in `tex/figs/plates.tex`. If either is refused or goes unanswered, the fallback is the same
one taken fifteen times already: redraw it, or drop it and let the prose carry the point.

## What these rows rest on, and what they do not

- The licence column is a direct reading of a licence page on 2026-09-18, per source, with the URL
  given. Nothing in that column is inferred from the venue or from a sibling paper.
- arXiv licences are chosen per submission **and per version**. Each row reflects the licence shown
  on the abstract page for the current version at the date above. If a plate is re-rendered from a
  different version, re-check.
- A CC licence on a paper covers the authors' own content. If a figure embeds third-party material,
  the CC grant does not reach it; CC BY also does not grant trademark or patent rights. The two
  rows that carried an NVIDIA trademark note were both cut, so no such note remains.
- Where a published version exists, its licence was not checked for either remaining row: the rows
  that name a publisher name it as a *route*, not as a finding.
- Every file in `tex/figs/selected/` was rendered from `papers/pdf/<source key>.pdf`, whose sha256
  is recorded per source in `corpus/figure_catalogue.json`. A crop does not create a new work and
  does not change the permission needed, but it *is* a change that CC attribution must declare.
- The build does not enforce any of this, and no plate prints its status: a caption credits its
  source and, where the licence asks for it, the attribution. The figures with an open action are
  the two rows above, and this file is the only place that records them.
