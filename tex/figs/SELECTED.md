# Selected reproduced figures

**Three** figures, chosen from the 858 catalogued in `corpus/figure_catalogue.json` (166 source
PDFs). An earlier draft of this paper carried eighteen. Fifteen were cut, and the table at the
bottom of this file says what replaced each one.

## Why three

Five well-made surveys were measured against this paper (`reviews/STYLE_GUIDE.md`) and every one
of them reproduces **nothing**: every figure in them is the authors' own diagram, plot or
photograph, held in one to three visual styles. Eighteen borrowed plates from ten source papers
put eleven visual styles on the reader, cost twelve full-width floats, put a credit line under a
third of the figures and created eleven open permissions.

So the rule now is: **a plate is kept only where it carries something a drawing cannot.** A
diagram beats a borrowed photograph on three counts — it is one visual style rather than an
eleventh, it needs no permission, and it can show the mechanism instead of a picture of a device.
Where the cut plate was carrying an argument, the argument was redrawn in the paper's own TikZ
style. Where it was illustrating a point the prose already made well, it was dropped and nothing
was added.

Every survivor is **single column** and none is a `figure*`: a borrowed plate has not earned the
page width. Two of the three are a single panel. The third is a grid because the grid *is* the
comparison. A borrowed multi-panel plate set at one column lands its panels at about 15 mm across
with labels under 8 pt, which is not a figure but the memory of one.

## Provenance

Every file in `tex/figs/selected/` was **re-rendered from the source PDF**, not upscaled from the
200 dpi catalogue preview: `tools/extract_figures.py` locates the figure rectangle, and the
rectangle was rendered again at a dpi close to the embedded raster's own resolution, then cropped.
All three plates are rebuilt by `tools/relayout_plates.py`, which holds their panel boxes as
fractions of the trimmed source region and writes the file; run it to reproduce them.

Colour. All three keep colour, and in two the colour *is* the content: the red and blue hand pair
in `bimanual_grasp_penetration`, and the green robot hand against the tan object in
`teleop_retarget_artifacts`.

Permission. One of the three is cleared under CC BY 4.0; the other two need an email to the
authors. No plate prints its status. See `tex/PERMISSIONS.md`.

---

## The three

### `hand_scale_to_human.png` — 1676x1685, colour, `figure`
- **Source** `leap_hand_2023`, Fig. 3, p. 2.
- **Original caption** "Relative size of popular robot hands to scale. Left to right, adult human
  hand, Allegro Hand [20], LEAP-C Hand, LEAP Hand, Inmoov [18], D'Manus [21]. ... The hands are
  accurate to scale."
- **Crop** re-laid out, 450 dpi. The source is one row of six hands, 3.68:1, which across the
  full text width renders 49 mm tall and wastes a double-column slot on a strip. The row is cut on
  the white gutters between the hands, at 0.2005, 0.3341, 0.4727, 0.6059 and 0.7532 of the width,
  and set as two rows of three: human-with-ruler, Allegro, LEAP-C over LEAP, InMoov, D'Manus. Each
  hand keeps the label under it and none is resampled, so at one column every hand is the same
  30 mm wide it was across two (`tools/relayout_plates.py`).
- **Why a drawing could not do this** How much larger than a human hand the hands the field
  actually trains on are. A ruler and a real palm in frame settle a point no schematic can make
  honestly, because the claim is about physical objects and not about topology. This is the "one
  hand photograph for scale" the style guide allows.

### `teleop_retarget_artifacts.png` — 441x200, colour, `figure`
- **Source** `toporetarget_2026`, Fig. 3, p. 7.
- **Original caption** "Retargeting artifacts of existing methods under hand-object and hand-only
  cases."
- **Crop** one cell of a 4x4 grid, 400 dpi: the hand-object row where DexPilot drives the
  fingertip through the spectacle temple, at x 0.497–0.719 and y 0.280–0.455 of the region. The
  source's own verdict labels are cropped away with it, both because at one column they set at
  about 3 pt and because the caption carries the verdict in the document font instead. The whole
  grid was previously set across both columns at 104 mm tall; one legible cell is worth more than
  sixteen illegible ones, and the other three failure modes are named in the prose.
- **Why a drawing could not do this** That a retargeting error is invisible in the pose and
  unmistakable in the contact. Drawing it would beg the question: the reader has to see a posture
  that genuinely looks right, and then see the surface pass through the finger.

### `bimanual_grasp_penetration.png` — 753x767, colour, `figure`
- **Source** `bimangrasp_2024`, Fig. 9, p. 7.
- **Original caption** "Visualization of four most common failure patterns: (A) hand-object
  penetration, (B) hand's self-penetration, (C) inter-hand penetration, and (D) failure to
  establish contact."
- **Crop** panels (A) and (C) with their zoomed insets, 450 dpi. Fig. 6, which the extractor
  placed in the same region, is removed by a pre-crop of the right 50 percent; the two panels are
  then taken at x 0.004–0.236 and 0.486–0.722 of what remains. (B) self-penetration and (D)
  no-contact are dropped: four panels at one column put each inset at 20 mm, and (A) and (C) are
  the two the section names (`tools/relayout_plates.py`).
- **Why a drawing could not do this** That the two commonest failures of two-hand grasp synthesis
  are invisible at the scale of the whole grasp and obvious at the scale of the contact. A drawing
  of a finger inside an object would show the defect at both scales, which is exactly the thing
  that is not true.

---

## Cut, and what replaced each

Fifteen plates were removed and their PNG files deleted from `tex/figs/selected/`, so nothing
unlicensed ships in the arXiv source. Their catalogue entries in `corpus/figure_catalogue.json`
are untouched and any of them can be re-rendered from `papers/pdf/` if a decision is reversed.

| cut plate | source | what replaced it |
|---|---|---|
| `hand_leap_overview.png` | `leap_hand_2023` Fig. 1 | `figs/fig_transmission.tex`, row 1: in a direct-drive hand the motor *is* the joint, and the fingertip reaches a region |
| `hand_ilda_linkage.png` | `ilda_hand_2021` Fig. 5 | `figs/fig_transmission.tex`, row 2: motors in the palm driving through four-bars |
| `hand_coupled_linkage.png` | `bidexhand_2025` Fig. 2 | `figs/fig_transmission.tex`, row 2 and the reachable-set column, which draws the thing the photograph could not: a coupling ties two joints, so the fingertip reaches a curve and not a region. This also removes the paper's only CC BY-NC-SA source, whose NC and SA conditions had no clean resolution |
| `sim_tendon_model.png` | `openai_rubiks_cube_2019` Fig. 7 | `figs/fig_transmission.tex`, row 3: the tendon routed over wrapping surfaces, and the state-estimation cost that routing carries |
| `hand_digit_fingertips.png` | `digit_2020` Fig. 1 | nothing. The prose gives the sensor at 20 by 27 by 18 mm, 20 g and about \$15, which says more about what a tactile retrofit does to a fingertip than a photograph of one does |
| `hand_inspire_tactile_pad.png` | `articulated_tools_inhand_2025` Fig. 4 | nothing. "A printed pad over a foam layer, fitted to a commercial hand" is a sentence the prose already carries |
| `sim_convex_decomposition.png` | `dexremoe_2025` Fig. 8 | `figs/fig_collision.tex`, which draws the same fingertip against all three geometries instead of rendering three toys |
| `sim_tactile_interpenetration.png` | `isaaclab_2025` Fig. 10 | `figs/fig_tactiledepth.tex`, which shows that the four outputs are all functions of one overlap depth — the point the four heatmap panels did not make |
| `sim_isaacgym_inhand_envs.png` | `isaacgym_2021` Fig. 13 | nothing. The prose has the number that matters: under an hour on one A100 against 30 hours on 6144 CPU cores and 8 V100s |
| `teleop_dexpilot_studio.png` | `dexpilot_2020` Fig. 3 | nothing. The section's argument is about latency, cost and what the tabulation does not record, not about the size of one table |
| `teleop_bidex_exoskeleton.png` | `bidex_teleop_2024` Fig. 2 | nothing. The fourth retargeting family — remove retargeting from the loop with an exoskeleton — is stated in the prose with its citation |
| `teleop_retarget_embodiments.png` | `anyteleop_2023` Fig. 10 | nothing. Twenty panels at one column is the collage the style guide condemns, and the surviving `teleop_retarget_artifacts` carries the visual argument about retargeting |
| `data_arctic_bimanual.png` | `arctic_2022` Fig. 1 | `figs/fig_contactlabel.tex`, which draws where a capture set's contact label comes from and what bounds it, rather than showing the outputs of that chain |
| `bimanual_handover_allegro.png` | `dynamic_handover_2023` Fig. 2 | nothing. `figs/fig_bimanual.tex` already sets the four coordination architectures side by side, and the handover argument is that all three corpus papers share one reward across giver and receiver |
| `eval_cage_sim_and_real.png` | `openai_dexterity_2018` Fig. 3 | nothing. The paragraph states the cost in rollouts and hours, which is the form a reader can act on; a photograph of a cage is not a cost estimate |

---

## Rejected, and why

Of roughly sixty figures opened and looked at before the cut, the ones that came closest and were
still turned down. Every reason below now applies a fortiori.

- **Plots we generate ourselves.** `dexmachina_2025` Fig. 3 (per-hand success bars),
  `geometric_retargeting_2025` Fig. 2 (retargeting workspace scatters), `brax_2021` Figs. 2-9
  (throughput and reward curves), `isaaclab_2025` Figs. 13-17 (throughput comparisons),
  `suresim_2025` Figs. 4-11 (interval widths). The survey's own charts, built from the corpus,
  say the same thing with provenance we control.
- **Too dense at column width.** `bidexhand_2025` Fig. 5 (all 33 GRASP taxonomy poses in one
  grid), `colosseum_2024` Figs. 11-20 (per-task perturbation grids), `libero_2023` Figs. 8-11,
  `penspin_2024` Fig. 1 (twelve tiny rollout tiles), `oakink_2022` Fig. 17.
- **Mostly text or logos.** `dexverse_2026` Fig. 1 and `bench2dex_2026` Fig. 1, both teaser
  posters dominated by branding; `maniskill3_2024` Figs. 9-10, which are code listings.
- **Composites of other people's figures.** `an_dexil_survey_2025` Figs. 4-5 — good photographs
  of three-fingered claws and teleoperation devices, but assembled from third-party sources, so
  reproducing them would need permission from each original owner rather than from the authors.
- **Murky, cropped or too small at source.** `dapg_2017` Fig. 6 (ADROIT render, ~390 px after
  crop), `faive_hand_2023` Fig. 3 (dark, small), `hot3d_2024` Fig. 5 (small snapshot of a lab),
  `dexumi_2025` Fig. 5, `dexcap_2024` Fig. 11 (CAD parts), `visual_dexterity_2022` Fig. 1 (the
  extractor cut off panel A).
- **Redundant, and now redundant with a drawing.** `dextreme_2022` Fig. 2 and `gr_dexter_2025`
  Fig. 4 (hardware setups: the plates that covered them are themselves cut, and the prose carries
  the cost); `isaacgym_2021` Fig. 4 and `maniskill3_2024` Fig. 5 (parallel environments, now
  prose only); `grab_2020` Fig. 4 (contact areas from MoCap, covered by
  `figs/fig_contactlabel.tex`); `pisa_iit_softhand_2014` Fig. 12 and `ruka_v2_2026` Figs. 2 and 5
  (underactuated transmissions, covered by `figs/fig_transmission.tex`);
  `dexterous_functional_grasping_2023` Fig. 12 (glove to robot hand, now prose only).
- **Not dexterous manipulation.** `physhoi_2023` Fig. 11 (parallel humanoids with basketballs),
  `brax_2021` Fig. 1 (locomotion suite), `ycb_2015` Figs. 1-4 (the object set is a fine
  photograph but belongs to a benchmark section this survey does not illustrate).
