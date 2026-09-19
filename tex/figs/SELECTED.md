# Selected reproduced figures

Eighteen figures chosen from the 858 catalogued in `corpus/figure_catalogue.json` (166 source
PDFs). Each was opened and looked at before it was chosen; each was judged on whether it shows
something the survey's own generated charts cannot, and on whether it is still legible when the
page sets it to 8.8 cm (one IEEE column) or 18.2 cm (both).

Provenance. Every file in `tex/figs/selected/` was **re-rendered from the source PDF**, not
upscaled from the 200 dpi catalogue preview: `tools/extract_figures.py` locates the figure
rectangle, and the rectangle was rendered again at a dpi close to the embedded raster's own
resolution, then cropped. The crop column below gives the box in fractions of the trimmed
catalogue preview, so any crop can be reproduced. "none" means the whole catalogued region.
Four plates whose panels were re-cut and re-stacked are rebuilt by
`tools/relayout_plates.py`, which holds their panel boxes as the same fractions and writes the
file; run it to reproduce them.

Colour. Two plates were converted to greyscale because the colour carried no information
(`hand_ilda_linkage`, a near-monochrome metal hand on white; `teleop_bidex_exoskeleton`, a black
rig on a white background). Every other plate keeps colour, and in several the colour *is* the
content: the green tendons in `sim_tendon_model`, the red/green force arrows and viridis
interpenetration field in `sim_tactile_interpenetration`, the red/blue hand pair in
`bimanual_grasp_penetration`, the red and green verdicts in `teleop_retarget_artifacts`.

Permission. None has been sought. Every plate emits `\pending`, not `\credit`; see
`tex/PERMISSIONS.md`.

---

## Sec. III — Hands

### `hand_leap_overview.png` — 2115x864, colour, `figure*`
- **Source** `leap_hand_2023`, Fig. 1, p. 1.
- **Original caption** "(a) LEAP Hand is an anthropomorphic dexterous robot hand designed for
  robot learning research. It can be assembled in under 4 hours for 2000 USD, is composed of
  readily available parts, and is robust. (b) to-scale comparison of LEAP Hand and a human hand
  (c-h) LEAP Hand in different power and precision grasps holding common objects."
- **Crop** none; re-rendered at 300 dpi (the embedded raster is ~139 dpi at print size, so this
  is the practical ceiling for this figure).
- **Shows what the text cannot** That in a direct-drive hand the actuators are the phalanges —
  the labelled motor, spacer and bracket in panel (a) are the finger, so "12 actuated DoF" and
  "the finger is 30 mm thick" are the same design decision.

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
  30 mm wide it was across two, and the plate gives a column slot back
  (`tools/relayout_plates.py`).
- **Shows what the text cannot** How much larger than a human hand the hands the field actually
  trains on are — a ruler in frame settles a point that a DoF table in this survey cannot make.

### `hand_ilda_linkage.png` — 1307x958, **greyscale**, `figure`
- **Source** `ilda_hand_2021`, Fig. 5, p. 8.
- **Original caption** "Manufactured ILDA hand. a Front view. b Rear view. c-i Motion tests of
  the developed ILDA hand. c Fist of the hand. d, e Motions of the five fingers of the hand. f-i
  Maximum 3-DOF motions of the finger."
- **Crop** top 42.5% of the region — panels (a) and (b) only, including the coin left in frame for
  scale; motion-test panels (c-i) dropped. 400 dpi (native ~300 dpi). Greyscale: the source is a
  silver hand on white and colour adds nothing.
- **Shows what the text cannot** A fully actuated hand with its transmission left visible: every
  four-bar, lead screw and routed cable that a 20-DoF, 15-N-fingertip specification costs in
  volume, next to a coin.

### `hand_coupled_linkage.png` — 1564x754, colour, `figure`
- **Source** `bidexhand_2025`, Fig. 2, p. 2.
- **Original caption** "Configuration of the BiDexHand phalanx. a) Configuration of the robotic
  hand phalanx. b) Exploded view of the robotic phalanx."
- **Crop** left 47% — panels (a) and (b); the body-text column that the extractor swept in on the
  right is removed. 500 dpi (native ~255 dpi).
- **Shows what the text cannot** The mechanism by which actuator count is reduced: an
  anti-parallelogram linkage physically ties DIP to PIP, so an underactuated finger's reachable
  set is a curve through joint space, not a region of it.

### `hand_inspire_tactile_pad.png` — 1564x1011, colour, `figure`
- **Source** `articulated_tools_inhand_2025`, Fig. 4, p. 4.
- **Original caption** "Inspire hand with an augmented tactile structure. A 3D-printed pad and
  foam layer redistribute contact loads to enhance tactile sensitivity and repeatability, while
  motor and mimic joints are illustrated for clarity."
- **Crop** right 50% — the figure proper; the body-text column removed. 450 dpi (native ~446 dpi).
- **Shows what the text cannot** That compliance on a commercial hand is retrofitted, not
  designed in: a printed pad over foam, strapped on, is the interface between a rigid shell and
  the contact the policy depends on.

### `hand_digit_fingertips.png` — 1577x1054, colour, `figure`
- **Source** `digit_2020`, Fig. 1, p. 1.
- **Original caption** "DIGITs mounted on an Allegro multi-finger hand. To validate our sensor
  design, we learn to manipulate glass marbles between two fingers."
- **Crop** right 50% — the photograph; the abstract column removed. 450 dpi.
- **Shows what the text cannot** That adding vision-based touch replaces the fingertip rather
  than instrumenting it: the sensor body sets the tip's size, shape and stiffness, which is why
  a tactile retrofit changes the hand's kinematics as well as its observations.

## Sec. IV — Simulators and contact

### `sim_isaacgym_inhand_envs.png` — 2239x1267, colour, `figure*`
- **Source** `isaacgym_2021`, Fig. 13, p. 17.
- **Original caption** "The three in-hand manipulation environments implemented in Isaac Gym:
  Shadow Hand, Trifinger, and Allegro."
- **Crop** re-laid out, 600 dpi. The source is one row of three screenshots, 5.31:1, which across
  the full text width renders 34 mm tall: the parallel copies receding to the horizon, which are
  the whole point, were not visible. Cut on the gutters at 0.3334 and 0.6670 of the width and set
  two-up with the third centred below, 1.77:1, so each screenshot is 90 mm wide instead of 60 and
  51 mm tall instead of 34 (`tools/relayout_plates.py`).
- **Shows what the text cannot** What "1024 parallel environments" looks like from inside the
  renderer: the copies stretching to the horizon behind the foreground scene are the batch, and
  they share one physics step.

### `sim_tendon_model.png` — 1957x1104, colour, `figure`
- **Source** `openai_rubiks_cube_2019`, Fig. 7, p. 8.
- **Original caption** "Transparent view of the hand in the new simulation. One spatial tendon
  (green lines) and two cylindrical geometries acting as pulleys (yellow cylinders) have been
  added for each non-thumb finger in order to achieve coupled joints dynamics similar to the
  physical robot."
- **Crop** none; 300 dpi (native ~295 dpi).
- **Shows what the text cannot** How a tendon-driven hand is actually represented inside a
  physics engine — routed spatial tendons over wrapping cylinders — so that "we model the
  coupling" becomes a specific piece of geometry that can be got wrong.

### `sim_convex_decomposition.png` — 1271x427, colour, `figure`
- **Source** `dexremoe_2025`, Fig. 8, p. 11.
- **Original caption** "We show the difference between object meshes with and without convex
  decomposition."
- **Crop** bottom 40%, left 55% — the three-panel comparison only; the adjacent object-set figure
  and its caption, both swept into the same region by the extractor, are removed. 400 dpi.
- **Shows what the text cannot** That the object a policy contacts is not the object it is shown:
  the single convex hull erases every concavity, and the decomposition that restores them is a
  free parameter no paper in the corpus reports.

### `sim_tactile_interpenetration.png` — 1457x1114, colour, `figure`
- **Source** `isaaclab_2025`, Fig. 10, p. 14.
- **Original caption** "A fast visuo-tactile simulation module that generates tactile images and
  force fields, based on a soft-contact model between rigid bodies and the sensor."
- **Crop** right 38.5% — the four labelled panels; the body-text column removed. 600 dpi.
- **Shows what the text cannot** That under a compliant contact model interpenetration depth is
  the quantity the sensor model integrates, not an error to be driven to zero — the same overlap
  this survey measures elsewhere as a defect is here the signal.

## Sec. V — Teleoperation and human-data sources

### `teleop_dexpilot_studio.png` — 2000x1647, colour, `figure`
- **Source** `dexpilot_2020`, Fig. 3, p. 3.
- **Original caption** "Studio is composed of four cameras pointing towards the table over which
  the user moves their hand with the hand-arm system in close proximity to enable line of sight
  driven teleoperation."
- **Crop** none; rendered at 400 dpi (native ~407 dpi), then resampled to 2000 px on the long
  edge to keep the file proportionate to one column.
- **Shows what the text cannot** The physical envelope a vision-based teleoperation corpus was
  collected in — four cameras, a 55x80 cm marked table, dimensions on every stand — which is the
  scope over which "collected 100 demonstrations" actually holds.

### `teleop_bidex_exoskeleton.png` — 2080x918, **greyscale**, `figure`
- **Source** `bidex_teleop_2024`, Fig. 2, p. 4.
- **Original caption** "Mobile bimanual teleoperation system Left: An operator strapped into
  BiDex. Right: Our bimanual robot setup including two xArm robot arms, two LEAP Hands [1] and
  three cameras on an AgileX base."
- **Crop** none; 380 dpi (native ~387 dpi). Greyscale: a black rig on a white background, colour
  carried nothing.
- **Shows what the text cannot** The contrast with the camera-based cell above: a worn linkage
  measures the operator's joints directly, so the correspondence problem moves from perception
  into mechanism design.

### `teleop_retarget_embodiments.png` — 2070x1900, colour, `figure`
- **Source** `anyteleop_2023`, Fig. 10, p. 15.
- **Original caption** "Visualization of Hand Pose Retargeting. The figure presents the results
  of hand pose retargeting for seven gestures and four different dexterous robot hands. The four
  hands are displayed in order from left to right: (i) Schunk SVH hand; (ii) Shadow Hand; (iii)
  DLR Hand; (iv) Allegro Hand."
- **Crop** composited: the first four gesture rows (top 46.8%) stacked directly above the column
  label strip (bottom 6.2%), so the four hands stay named while the plate fits a column. 400 dpi
  (native ~1516 dpi). Rebuilt at the full width of the region: the earlier crop had trimmed about
  2.5 percent off the right edge and clipped the final letter of the "Allegro" column label
  (`tools/relayout_plates.py`).
- **Shows what the text cannot** How far apart four hands end up from one human pose: the same
  tracked keypoints produce four visibly different postures, which is the embodiment gap that a
  shared demonstration corpus has to cross.

### `teleop_retarget_artifacts.png` — 1982x1142, colour, `figure*`
- **Source** `toporetarget_2026`, Fig. 3, p. 7.
- **Original caption** "Retargeting artifacts of existing methods under hand-object and hand-only
  cases."
- **Crop** none; 400 dpi (native ~1877 dpi). Placed across both columns: the per-panel verdict
  labels stop being legible below about 14 cm.
- **Shows what the text cannot** That retargeting failures are contact failures — misplaced,
  penetrating, non-contacting, hyperextended — each magnified at the fingertip, where a
  joint-angle error metric would report all four as small.

### `data_arctic_bimanual.png` — 3157x1244, colour, `figure*`
- **Source** `arctic_2022`, Fig. 1, p. 1.
- **Original caption** "ARCTIC is a dataset of hands dexterously manipulating articulated
  objects. The dataset contains videos from both eight 3rd-person allocentric views (a) and one
  1st-person egocentric view (b), together with accurate ground-truth 3D hand and object meshes,
  captured with a high-quality motion capture system."
- **Crop** left 76.4%, 600 dpi. The whole figure is 3.33:1 and renders 54 mm tall across the text
  width. Panels (a)-(d) already sit two-up, so the leftmost 76.4 percent is the capture-to-contact
  chain this plate is placed for, at 2.54:1 and 71 mm tall, with every one of those four panels and
  its label intact. Column (e), object articulation, is dropped: it is full height, so keeping it
  is what makes the plate a strip, and the caption does not discuss it. Precedent is
  `hand_ilda_linkage`, whose motion-test panels are dropped the same way
  (`tools/relayout_plates.py`).
- **Shows what the text cannot** The chain of a hand-object dataset in one plate — captured
  video, fitted hand and object meshes, and the dense contact field between them — making plain
  that the contact label is inferred from a mesh fit and never measured at the surface.

## Sec. VI — Two hands

### `bimanual_handover_allegro.png` — 2000x1005, colour, `figure*`
- **Source** `dynamic_handover_2023`, Fig. 2, p. 4.
- **Original caption** "Real Robot System: We employ two Allegro Hands, each individually mounted
  on separate XArm-6 robots, arranged in a face-to-face configuration. We incorporate a RealSense
  D435 camera for real-time object position tracking..."
- **Crop** none; 440 dpi (native ~448 dpi), resampled to 2000 px on the long edge.
- **Shows what the text cannot** A two-hand system in which the hands never touch: the figure's
  own overlay gives each policy's 22-dimensional action and its observation, and the only
  coupling drawn between them is the object's flight.

### `bimanual_grasp_penetration.png` — 1551x712, colour, `figure*`
- **Source** `bimangrasp_2024`, Fig. 9, p. 7.
- **Original caption** "Visualization of four most common failure patterns: (A) hand-object
  penetration, (B) hand's self-penetration, (C) inter-hand penetration, and (D) failure to
  establish contact."
- **Crop** right 50% — Fig. 9 alone; Fig. 6, which the extractor placed in the same region, is
  removed. 450 dpi (native ~852 dpi). Two columns: the zoomed insets are the point and they need
  the width.
- **Shows what the text cannot** That the four commonest failures of two-hand grasp synthesis are
  invisible at the scale of the whole grasp and obvious at the scale of the contact — the direct
  visual case for reporting a penetration measure alongside a success rate.

## Sec. VII — Evaluation

### `eval_cage_sim_and_real.png` — 2000x1161, colour, `figure`
- **Source** `openai_dexterity_2018`, Fig. 3, p. 3.
- **Original caption** "(left) The \"cage\" which houses the robot hand, 16 PhaseSpace tracking
  cameras, and 3 Basler RGB cameras. (right) A rendering of the simulated environment."
- **Crop** none; 480 dpi (native ~482 dpi), resampled to 2000 px on the long edge.
- **Shows what the text cannot** The apparatus a headline in-hand reorientation number rests on,
  beside the simulation it was trained in: reproducing the result means reproducing the cage, and
  the photograph is the cost estimate.

---

## Rejected, and why

Of roughly sixty figures opened and looked at, the ones that came closest and were still turned
down:

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
- **Redundant with a better plate.** `dextreme_2022` Fig. 2 and `gr_dexter_2025` Fig. 4 (hardware
  setups, covered by `eval_cage_sim_and_real` and `bimanual_handover_allegro`); `isaacgym_2021`
  Fig. 4 and `maniskill3_2024` Fig. 5 (parallel environments, covered by
  `sim_isaacgym_inhand_envs`); `grab_2020` Fig. 4 (contact areas from MoCap, covered by
  `data_arctic_bimanual`); `pisa_iit_softhand_2014` Fig. 12 and `ruka_v2_2026` Figs. 2 and 5
  (underactuated transmissions, covered by `hand_coupled_linkage` and `hand_ilda_linkage`);
  `dexterous_functional_grasping_2023` Fig. 12 (glove to robot hand, covered by the two
  teleoperation plates).
- **Not dexterous manipulation.** `physhoi_2023` Fig. 11 (parallel humanoids with basketballs),
  `brax_2021` Fig. 1 (locomotion suite), `ycb_2015` Figs. 1-4 (the object set is a fine
  photograph but belongs to a benchmark section this survey does not illustrate).
