# Reproduced figures: attribution and permission

Every figure in `tex/figs/extracted/` is rendered from a source PDF in `papers/pdf/`. The
catalogue at `corpus/figure_catalogue.json` records, per figure, the source key, the page, the
original caption and the sha256 of the PDF it came from.

Reproducing a published figure is not automatically permitted. Before this survey is posted or
submitted, each reproduced figure needs one of the following, recorded in the table below:

- the source is on arXiv under a licence that permits redistribution, such as CC BY or
  CC BY-SA. Note that arXiv's own non-exclusive licence does **not** by itself grant reuse;
- the publisher's reuse policy covers it, which for IEEE and ACM generally requires a formal
  permission request when a figure is reproduced in another publication;
- the authors have granted permission in writing;
- or the figure is redrawn rather than reproduced, in which case the artwork is this survey's own
  and only the idea is attributed.

Until a row below says otherwise a figure is `pending`, and the safe options are to redraw it or
to drop it. The build does not enforce this. A person has to.

| figure | source key | licence or policy | status |
|---|---|---|---|
| `hand_leap_overview.png` | `leap_hand_2023` | On arXiv (2309.06440); published at RSS 2023. RSS is neither IEEE nor ACM and its proceedings are author-hosted, so no publisher transfer is known. The per-paper arXiv licence has not been checked, and arXiv's default non-exclusive licence does not grant reuse. Route: the authors' written permission, unless the posting turns out to be CC BY. | pending |
| `hand_scale_to_human.png` | `leap_hand_2023` | Same source and same route as the row above. | pending |
| `hand_ilda_linkage.png` | `ilda_hand_2021` | Not on arXiv. Published in Nature Communications 12 (2021), a fully open-access journal whose research articles carry a Creative Commons licence stated on the article page; Nature Communications offers both CC BY and CC BY-NC-ND, and which one this article uses has not been checked. Route: read the licence on the article page. If CC BY, reuse with attribution; if CC BY-NC-ND, reproduction here needs permission. | pending |
| `hand_coupled_linkage.png` | `bidexhand_2025` | On arXiv (2504.14712); presented at an ICRA 2025 workshop, and workshop papers are generally not in the IEEE Xplore proceedings, so no IEEE copyright transfer is known to apply. Per-paper arXiv licence not checked. Route: the authors' written permission. | pending |
| `hand_inspire_tactile_pad.png` | `articulated_tools_inhand_2025` | arXiv-only preprint (2509.23075); the corpus records no venue. arXiv's default licence does not grant reuse and the per-paper licence has not been checked. Route: the authors' written permission, unless the posting is CC BY. | pending |
| `hand_digit_fingertips.png` | `digit_2020` | On arXiv (2005.14679); published in IEEE Robotics and Automation Letters (2020). IEEE holds copyright in the published version, and IEEE requires a formal permission request (RightsLink) to reproduce a figure in another publication. Route: IEEE permission request, or the authors' permission for the arXiv version if its licence permits. | pending |
| `sim_isaacgym_inhand_envs.png` | `isaacgym_2021` | On arXiv (2108.10470); published in the NeurIPS 2021 Datasets and Benchmarks track, which is neither IEEE nor ACM and where authors retain copyright. Per-paper arXiv licence not checked. Route: the authors' written permission, unless the posting is CC BY. Note the figure also shows NVIDIA product imagery. | pending |
| `sim_tendon_model.png` | `openai_rubiks_cube_2019` | arXiv-only technical report (1910.07113); no peer-reviewed venue recorded. Per-paper arXiv licence not checked. Route: the authors' (OpenAI's) written permission, unless the posting is CC BY. | pending |
| `sim_convex_decomposition.png` | `dexremoe_2025` | arXiv-only preprint (2508.01695); no venue recorded. Per-paper arXiv licence not checked. Route: the authors' written permission, unless the posting is CC BY. | pending |
| `sim_tactile_interpenetration.png` | `isaaclab_2025` | arXiv-only report (2511.04831) from NVIDIA; no peer-reviewed venue recorded. Per-paper arXiv licence not checked, and the copyright holder is likely corporate rather than individual. Route: NVIDIA's written permission, unless the posting is CC BY. | pending |
| `teleop_dexpilot_studio.png` | `dexpilot_2020` | On arXiv (1910.03135); published at ICRA 2020, an IEEE conference. IEEE holds copyright in the proceedings version and requires a formal permission request to reproduce a figure elsewhere. Route: IEEE permission request, or the authors' permission for the arXiv version if its licence permits. | pending |
| `teleop_bidex_exoskeleton.png` | `bidex_teleop_2024` | On arXiv (2411.13677); published at CoRL 2024, whose proceedings appear in PMLR. PMLR carries a per-paper licence chosen by the authors rather than a single blanket licence, and this paper's has not been checked. Route: read the PMLR page; failing a permissive licence there, the authors' written permission. | pending |
| `teleop_retarget_embodiments.png` | `anyteleop_2023` | On arXiv (2307.04577); published at RSS 2023. As with the LEAP rows: not IEEE or ACM, no known publisher transfer, per-paper arXiv licence unchecked. Route: the authors' written permission, unless the posting is CC BY. | pending |
| `teleop_retarget_artifacts.png` | `toporetarget_2026` | arXiv-only preprint (2606.16272); no venue recorded. Per-paper arXiv licence not checked. Route: the authors' written permission, unless the posting is CC BY. | pending |
| `data_arctic_bimanual.png` | `arctic_2022` | On arXiv (2204.13662); published at CVPR 2023, whose proceedings are published by IEEE. An open-access copy on the CVF site is not itself a reuse licence. Route: IEEE permission request, or the authors' permission for the arXiv version if its licence permits. | pending |
| `bimanual_handover_allegro.png` | `dynamic_handover_2023` | On arXiv (2309.05655); published at CoRL 2023 (PMLR). Per-paper PMLR licence not checked. Route: read the PMLR page; failing a permissive licence there, the authors' written permission. | pending |
| `bimanual_grasp_penetration.png` | `bimangrasp_2024` | On arXiv (2411.15903); published in IEEE Robotics and Automation Letters (2024). IEEE holds copyright in the published version and requires a formal permission request. Route: IEEE permission request, or the authors' permission for the arXiv version if its licence permits. | pending |
| `eval_cage_sim_and_real.png` | `openai_dexterity_2018` | On arXiv (1808.00177); the journal version appeared in the International Journal of Robotics Research (2020), a SAGE journal. Two distinct routes with different holders: a SAGE permission request for the journal version, or the arXiv posting if its per-paper licence permits reuse (not checked). The file here was rendered from the arXiv PDF. | pending |

## What these rows rest on, and what they do not

The venue and arXiv identifier in each row come from `corpus/bib.json`. Nothing above was checked
against a publisher's or arXiv's licence page: where a row says "not checked", that is literally
what it means, and no row should be read as an assertion that reuse is permitted.

Every file in `tex/figs/selected/` was rendered from the PDF at `papers/pdf/<source key>.pdf`,
whose sha256 is recorded per source in `corpus/figure_catalogue.json`. For sources that exist both
as a preprint and as a publisher version, that PDF is the preprint, which is why several rows name
two possible rights holders. Crops are recorded in `tex/figs/SELECTED.md`; a crop does not create a
new work and does not change the permission needed.
