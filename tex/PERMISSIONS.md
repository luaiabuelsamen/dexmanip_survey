# Reproduced figures: licence, permission and action

Every figure in `tex/figs/selected/` is rendered from a source PDF in `papers/pdf/`. The
catalogue at `corpus/figure_catalogue.json` records, per figure, the source key, the page, the
original caption and the sha256 of the PDF it came from; the crops are in `tex/figs/SELECTED.md`.

**What was actually checked, and when.** On **2026-09-18** the arXiv abstract page of every source
with an arXiv identifier was fetched and the licence statement in its `abs-license` block read
directly (the `href` of "view license"), and for the one non-arXiv source the publisher's article
page was read. The licence column below quotes what those pages state and gives the URL the
statement was read from. Where a page states no licence, the row says so rather than guessing.
Venue and arXiv identifier come from `corpus/bib.json`; the *licence* comes from the page.

**This is not legal advice.** It is a record of what licence pages say. The author should confirm
anything that matters — in particular the NC/SA row, the two publisher rows, and whether a figure
contains third-party material that the paper's own CC licence does not cover.

## Counts

| category | figures |
|---|---|
| no permission needed, attribute under the licence | **7** |
| request from the publisher through their process | **2** |
| email the authors | **9** |
| redraw or drop | **0** (the fallback for any of the 11 above that does not come back in time) |

Of the 17 distinct sources behind the 18 figures: **6 arXiv postings are CC BY 4.0**, **1 is
CC BY-NC-SA 4.0**, **9 carry only arXiv's non-exclusive licence to distribute** (which grants a
third party nothing), and **1 is not on arXiv** but is published open access under CC BY 4.0.

## The decision table

Sorted so that the rows needing no action come first. "From" says which artefact the file in
`tex/figs/selected/` was rendered from, because the preprint and the published version are
different works with different rights holders.

| figure | source key | from | licence found (URL read) | permission required? | action |
|---|---|---|---|---|---|
| `hand_inspire_tactile_pad.png` | `articulated_tools_inhand_2025` | preprint (arXiv 2509.23075; no venue recorded, so the preprint is the only version) | **CC BY 4.0** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/2509.23075` | no | **no permission needed, attribute under the licence** |
| `sim_isaacgym_inhand_envs.png` | `isaacgym_2021` | preprint (arXiv 2108.10470); also published in the NeurIPS 2021 Datasets and Benchmarks track, where authors retain copyright | **CC BY 4.0** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/2108.10470` | no | **no permission needed, attribute under the licence.** Note: the plate shows NVIDIA product/UI imagery; CC BY covers copyright, not trademark |
| `sim_tactile_interpenetration.png` | `isaaclab_2025` | preprint (arXiv 2511.04831, NVIDIA; no peer-reviewed venue recorded) | **CC BY 4.0** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/2511.04831` | no | **no permission needed, attribute under the licence.** Same trademark note as above |
| `teleop_dexpilot_studio.png` | `dexpilot_2020` | **preprint** (arXiv 1910.03135). Published version: ICRA 2020, publisher **IEEE** | **CC BY 4.0 on the preprint** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/1910.03135`. The IEEE proceedings version is a separate work under IEEE copyright and is *not* covered | no, for the preprint | **no permission needed, attribute under the licence** — and the credit must name arXiv:1910.03135, not the ICRA proceedings, since that is the version reproduced |
| `teleop_retarget_embodiments.png` | `anyteleop_2023` | **preprint** (arXiv 2307.04577). Published version: RSS 2023 (author-hosted proceedings, no publisher transfer recorded) | **CC BY 4.0** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/2307.04577` | no | **no permission needed, attribute under the licence** |
| `bimanual_grasp_penetration.png` | `bimangrasp_2024` | **preprint** (arXiv 2411.15903). Published version: IEEE RA-L 9(12):11377–11384, 2024, DOI 10.1109/LRA.2024.3490393, publisher **IEEE** | **CC BY 4.0 on the preprint** — `http://creativecommons.org/licenses/by/4.0/`, stated on `https://arxiv.org/abs/2411.15903`. The RA-L version is under IEEE copyright and would need RightsLink; the file here is the preprint | no, for the preprint | **no permission needed, attribute under the licence** — credit arXiv:2411.15903 as the source, with the RA-L citation alongside for the reader |
| `hand_ilda_linkage.png` | `ilda_hand_2021` | **published version** (the Nature Communications open-access PDF; not on arXiv), *Nat. Commun.* 12:7177, DOI 10.1038/s41467-021-27261-0, publisher **Springer Nature** | **CC BY 4.0** — "This article is licensed under a Creative Commons Attribution 4.0 International License … To view a copy of this license, visit `http://creativecommons.org/licenses/by/4.0/`", stated on `https://www.nature.com/articles/s41467-021-27261-0` | no | **no permission needed, attribute under the licence.** Confirm the figure is not flagged as third-party material in a credit line (the article's CC grant excludes such material) |
| `hand_digit_fingertips.png` | `digit_2020` | **preprint** (arXiv 2005.14679). Published version: IEEE RA-L 2020, DOI 10.1109/LRA.2020.2977257, publisher **IEEE** | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2005.14679`. That licence permits arXiv to distribute; it grants this survey nothing. The published version is under IEEE copyright | **yes** | **request from the publisher through their process** (IEEE RightsLink on the Xplore page for the DOI). Emailing the authors would cover the preprint version instead; pick one and record which version the caption credits |
| `data_arctic_bimanual.png` | `arctic_2022` | **preprint** (arXiv 2204.13662). Published version: CVPR 2023, proceedings published by **IEEE** (a CVF open-access copy is a free copy, not a reuse licence) | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2204.13662` | **yes** | **request from the publisher through their process** (IEEE RightsLink for the CVPR 2023 paper), or email the authors for the preprint version |
| `hand_coupled_linkage.png` | `bidexhand_2025` | preprint (arXiv 2504.14712); presented at the ICRA 2025 Dexterity Workshop, which is not in the IEEE Xplore proceedings | **CC BY-NC-SA 4.0** — `http://creativecommons.org/licenses/by-nc-sa/4.0/`, stated on `https://arxiv.org/abs/2504.14712` | **yes**, unless the survey's publication is non-commercial *and* it can meet ShareAlike | **email the authors** (single author, Zhengyang Kris Weng). Two independent problems: **NC** — a survey published by IEEE/ACM or any commercial press is not a non-commercial use; **SA** — the plate is a crop, i.e. an adaptation, which BY-NC-SA requires be released under BY-NC-SA, which a copyright-transferred paper cannot do. Fallback: redraw the linkage diagram |
| `hand_leap_overview.png` | `leap_hand_2023` | preprint (arXiv 2309.06440); published at RSS 2023 (author-hosted proceedings, no publisher transfer recorded) | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2309.06440` | **yes** | **email the authors** (Shaw, Agarwal, Pathak). Note the *hardware* is open-licensed; that says nothing about the figure |
| `hand_scale_to_human.png` | `leap_hand_2023` | same source and same version as the row above | same: **arXiv non-exclusive licence to distribute**, `https://arxiv.org/abs/2309.06440` | **yes** | **email the authors** — same request, both figures in one message |
| `sim_tendon_model.png` | `openai_rubiks_cube_2019` | preprint (arXiv 1910.07113); no peer-reviewed venue, so the preprint is the only version | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/1910.07113` | **yes** | **email the authors** — the holder is corporate (OpenAI), so this goes to OpenAI rather than an individual |
| `sim_convex_decomposition.png` | `dexremoe_2025` | preprint (arXiv 2508.01695); no venue recorded | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2508.01695` | **yes** | **email the authors** (Wan, Liu, Dong) |
| `teleop_bidex_exoskeleton.png` | `bidex_teleop_2024` | **preprint** (arXiv 2411.13677). Published version: CoRL 2024, proceedings in **PMLR** vol. 270 | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2411.13677`. The PMLR page `https://proceedings.mlr.press/v270/shaw25a.html` **states no licence** for this paper — only a site-wide "Copyright © The authors and PMLR 2025" — so it provides no reuse grant either | **yes** | **email the authors** (Shaw et al.); neither version carries a reuse licence |
| `teleop_retarget_artifacts.png` | `toporetarget_2026` | preprint (arXiv 2606.16272); no venue recorded | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2606.16272` | **yes** | **email the authors** (Wu et al.) |
| `bimanual_handover_allegro.png` | `dynamic_handover_2023` | **preprint** (arXiv 2309.05655). Published version: CoRL 2023, proceedings in **PMLR** vol. 229 | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/2309.05655`. The PMLR page `https://proceedings.mlr.press/v229/huang23d.html` **states no licence** for this paper, only the site-wide author/PMLR copyright line | **yes** | **email the authors** (Huang et al.) |
| `eval_cage_sim_and_real.png` | `openai_dexterity_2018` | **preprint** (arXiv 1808.00177) — that is the PDF this plate was rendered from. Journal version: IJRR 2020, publisher **SAGE** | **arXiv non-exclusive licence to distribute** — `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, stated on `https://arxiv.org/abs/1808.00177`. The SAGE version's licence was **not** checked and is a separate route | **yes** | **email the authors** (OpenAI) for the preprint version reproduced here; alternatively a SAGE permission request (RightsLink) for the IJRR version, which would mean re-rendering the plate from that PDF |

## The attribution strings for the cleared figures

CC BY 4.0 and CC BY-SA 4.0 require, in a manner reasonable to the medium: the creator's name, the
title of the work, a link to the material, the licence name **with a link**, and an indication if
changes were made. The crops and greyscale conversions in `tex/figs/SELECTED.md` are changes, so
each string below names them. Use these verbatim as the second argument of `\licensed` (see
`tex/preamble.tex`); the numeric `\cite` stays in the caption for the reader.

- **`hand_inspire_tactile_pad.png`** — Fig. 4 of S. Atar, D. Huang, F. Richter and M. Yip,
  "In-Hand Manipulation of Articulated Tools with Dexterous Robot Hands with Sim-to-Real
  Transfer", arXiv:2509.23075, licensed under CC BY 4.0
  (`https://creativecommons.org/licenses/by/4.0/`); cropped to the right half of the page region.

- **`sim_isaacgym_inhand_envs.png`** — Fig. 13 of V. Makoviychuk et al., "Isaac Gym: High
  Performance GPU-Based Physics Simulation For Robot Learning", arXiv:2108.10470, licensed under
  CC BY 4.0 (`https://creativecommons.org/licenses/by/4.0/`); re-rendered, not otherwise changed.

- **`sim_tactile_interpenetration.png`** — Fig. 10 of M. Mittal et al. (NVIDIA), "Isaac Lab: A
  GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning", arXiv:2511.04831, licensed
  under CC BY 4.0 (`https://creativecommons.org/licenses/by/4.0/`); cropped to the four labelled
  panels.

- **`teleop_dexpilot_studio.png`** — Fig. 3 of A. Handa et al., "DexPilot: Vision Based
  Teleoperation of Dexterous Robotic Hand-Arm System", arXiv:1910.03135, licensed under CC BY 4.0
  (`https://creativecommons.org/licenses/by/4.0/`); re-rendered and resampled.

- **`teleop_retarget_embodiments.png`** — Fig. 10 of Y. Qin et al., "AnyTeleop: A General
  Vision-Based Dexterous Robot Arm-Hand Teleoperation System", arXiv:2307.04577, licensed under
  CC BY 4.0 (`https://creativecommons.org/licenses/by/4.0/`); four gesture rows and the column
  labels composited from the original figure.

- **`bimanual_grasp_penetration.png`** — Fig. 9 of Y. Shao and C. Xiao, "Bimanual Grasp Synthesis
  for Dexterous Robot Hands", arXiv:2411.15903, licensed under CC BY 4.0
  (`https://creativecommons.org/licenses/by/4.0/`); cropped to Fig. 9 alone.

- **`hand_ilda_linkage.png`** — Fig. 5 of U. Kim et al., "Integrated linkage-driven dexterous
  anthropomorphic robotic hand", *Nature Communications* 12:7177 (2021), DOI 10.1038/s41467-021-27261-0, licensed under CC BY 4.0
  (`https://creativecommons.org/licenses/by/4.0/`); panels (a) and (b) only, converted to
  greyscale.

Not cleared, for completeness: `hand_coupled_linkage.png` would be Fig. 2 of Z. K. Weng,
"BiDexHand: Design and Evaluation of an Open-Source 16-DoF Biomimetic Dexterous Hand",
arXiv:2504.14712, under CC BY-NC-SA 4.0 — the string is easy, the NC and SA conditions are the
obstacle, so this figure stays `\pending` until the author replies.

## What these rows rest on, and what they do not

- The licence column is a direct reading of a licence page on 2026-09-18, per source, with the URL
  given. Nothing in that column is inferred from the venue or from a sibling paper.
- arXiv licences are chosen per submission **and per version**. Each row reflects the licence shown
  on the abstract page for the current version at the date above. If a plate is re-rendered from a
  different version, re-check.
- A CC licence on a paper covers the authors' own content. If a figure embeds third-party material,
  the CC grant does not reach it; CC BY also does not grant trademark or patent rights, which is
  why the two NVIDIA rows carry a note.
- The venue, publisher and DOI fields are from `corpus/bib.json` plus the DOI/journal-ref shown on
  the arXiv page where one is present (`digit_2020`, `bimangrasp_2024`). Where a published version
  exists, its licence was checked only for `ilda_hand_2021` (Nature Communications),
  `dynamic_handover_2023` and `bidex_teleop_2024` (PMLR). IEEE, SAGE, NeurIPS and RSS pages were
  not opened; the rows that name them name them as a *route*, not as a finding.
- Every file in `tex/figs/selected/` was rendered from `papers/pdf/<source key>.pdf`, whose sha256
  is recorded per source in `corpus/figure_catalogue.json`. `tools/fetch_papers.py` takes that PDF
  from `arxiv.org/pdf/<id>` unless `bib.json` gives a `pdf_url`, which is why every row but
  `ilda_hand_2021` reads "preprint". A crop does not create a new work and does not change the
  permission needed, but it *is* a change that CC attribution must declare.
- The build does not enforce any of this. A person has to: figures still on `\pending` are the ones
  with an open action above.
