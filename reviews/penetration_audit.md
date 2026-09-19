# Hand audit of the penetration field

Answers objection O2 of `reviews/v5_final_read.md`: *"Your headline finding is a null result over
your own extraction, and your own appendix says that field was never audited."* The objection was
correct as of 2026-09-19 and this file is the work that closes it.

Run `python tools/audit_penetration.py` to redraw the sample and re-run the sweep. The script
asserts the population size and refuses to print a sample if the corpus has moved, because a
changed population means the draw below is stale rather than shifted.

## Why the field was under suspicion

Appendix A measures this extraction's own miss rate on the three fields it was audited against.
Of 34 method rows with a real robot and no recorded trial count, 15 carried the count in plain
text in their own note; the success criterion rose from 79 to 98 and the unseen-object count from
32 to 39. Every one of those audits recovered between a fifth and nearly half of the nulls, and
every recovery converted a silent paper into a reporting one. The same appendix then said the
penetration field had never been audited that way — and the penetration field carries the
survey's second headline finding, which is itself a null.

## The population and the draw

The population is every method row whose `penetration` field is `"not addressed"`: **85 rows** of
the 112, at commit `1746ea9`. The other 27 are 11 that handle penetration in some form (3
penalised, 3 measured, 5 constrained) and 16 nulls, where the note did not settle the question.
The 16 nulls are deliberately outside this audit: they are already counted as unsettled rather
than as silence, so recovering one would not move the finding.

```python
random.Random(20260919).sample(sorted(population), 25)   # 25 of 85, 29 percent
```

Seed **20260919**. Sample size **25**, which is above the 20 the review asked for.

## What was read, and how

For each sampled row: the full parsed source in `papers/md/<key>.md`, the OCR recovery
`papers/md/<key>.ocr.md` where one exists, and the parsed repository in `code/md/<key>.md` where
one exists. The note in `papers/notes/` was **not** consulted, because the note is the artefact
under suspicion — a field is wrong exactly when the source says something the note did not carry.

The sweep matches every word the corpus uses for this quantity — penetration, interpenetration,
intersection, intersection volume, solid intersection, simulation displacement, contact
consistency, physical plausibility, signed distance, contact depth — and also the words that get
mistaken for it: collision, collide, overlap, pierce, volumetric, SDF. Every hit was read in
context. A row is a **recovery** if its own source reports a measurement of interpenetration,
penetration depth, intersection volume, contact consistency or physical plausibility on that
method's own rollouts. A statement that penetration exists, a citation to a paper with
"physically plausible" in its title, a collision-avoidance constraint on a reference trajectory,
and a solver setting are all not that.

`paper N/M` below is thousands of words searched and lines matched; `ocr` is the OCR recovery,
`code` the parsed repository.

## Per-row verdicts

| row | searched | what the source says about the quantity | field right |
|---|---|---|---|
| `ace_teleop_2024` | paper 7k/1, ocr 7k/2 | Nothing. The one hit is an unrelated use of "overlap". | yes |
| `anyrotate_2024` | paper 10k/1, ocr 10k/1 | A tactile **contact depth** label, one of six regressed from the sensor on a flat stimulus in a force-torque calibration rig. Sensor indentation, not hand-object penetration, and not on rollouts. | yes |
| `anyteleop_2023` | paper 8k/10, ocr 8k/12, code 4k/7 | CuRobo generates **collision-free** arm trajectories and the system "guarantees no self-collision". Robot self-collision avoided during planning; no hand-object quantity, no number. | yes |
| `articulated_tools_inhand_2025` | paper 6k/1 | Nothing. One collision mention in related work. | yes |
| `being_h05_2026` | paper 21k/7, code 3k/0 | Nothing. All seven hits are "overlap" of action slots and adapter indices. | yes |
| `being_h0_2025` | paper 19k/15, ocr 20k/16, code 1k/0 | "Physically plausible hand motions" as a qualitative aim, shown in figures; metrics are MPJPE, PA-MPJPE and a text-to-motion retrieval accuracy. No plausibility measurement. | yes |
| `bunny_visionpro_2024` | paper 7k/16, code 0k/2 | A **self-collision cost** over spheres per link, in the retargeting objective, plus two unticked to-do boxes for collision-free retargeting. Robot-internal, and a cost rather than a reported number. | yes |
| `cross_embodiment_world_models_2025` | paper 6k/0 | The words do not occur in the source. | yes |
| `dexgraspvla_2025` | paper 11k/0, code 1k/0 | The words do not occur in either source. | yes |
| `dexvla_2025` | paper 10k/1, code 2k/1 | **Intersection over union** of gripper and object bounding boxes, used to auto-label grasp success during data annotation. An image-plane overlap, not a penetration depth. | yes |
| `dynamic_handover_2023` | paper 7k/3 | Collisions between the two arms named as a hazard motivating throw-and-catch. No measurement. | yes |
| `gemini_robotics_2025` | paper 25k/3 | Collision-free motion planning cited as prior art, and one generated code comment about avoiding a collision. No measurement. | yes |
| `graspxl_2024` | paper 8k/7, ocr 9k/7, code 10k/8 | **The closest call in the sample.** A 35-participant study scores realism 1–3 on "human likeness, naturalness, smoothness, and hand-object interpenetration", giving 2.12 for its own motions against 2.05 and 2.45 for HO3D and DexYCB. Its own metric table is midpoint, heading and rotation error, contact ratio and success rate; no penetration quantity anywhere. Recorded as not a recovery, and the rule is below. | yes, flagged |
| `groot_n16_2025` | paper 0k/0, code 9k/0 | The words do not occur. The source is an 844-word blog page, not a paper: the field is right and rests on very little. | yes, thin |
| `holo_dex_2022` | paper 6k/0, code 5k/0 | The words do not occur in either source. | yes |
| `hudor_2024` | paper 7k/0 | The words do not occur. | yes |
| `human2sim2robot_2025` | paper 13k/9, ocr 13k/12, code 8k/18 | **Collision-free arm IK** during retargeting, fabric collision avoidance in the controller, collision spheres in the repository, and `max_depenetration_velocity: 10000.0` in the Isaac Gym task config. The paper states outright: "we enforce collision-free arm IK to avoid contact with the environment. However, we do not enforce object collision." Its IoU is a segmentation-mask score for pose tracking. | yes |
| `humanplus_2024` | paper 9k/0, code 2k/6 | A `_reward_collision` term in the released policy, "penalize collisions on selected bodies" — humanoid self-collision, inherited from the legged-gym reward set, binary and not a depth. Nothing in the paper. | yes |
| `openai_rubiks_cube_2019` | paper 25k/2 | "MuJoCo allows for these shapes to penetrate each other by a small margin when a force is applied" — an acknowledgement in the cube model description, with no number, no metric and no rollout. | yes |
| `physhoi_2023` | paper 12k/18, ocr 12k/20, code 1k/3 | Penetration named as an artefact of kinematic methods in related work, "physically plausible" as an aim, and one limitation: "Due to the low frame rate of HOI data and simulation frequency, some minor penetrations may appear." An admission without a measurement — which is exactly what §VII-B already quotes this paper for. | yes |
| `pi05_2025` | paper 15k/2, code 4k/0 | Nothing. Two unrelated hits. | yes |
| `pianomime_2024` | paper 8k/12, code 4k/23 | The **SDF** is a learned goal representation of the piano state, unrelated to contact. The repository has a boolean forearm-collision penalty and a call that disables collisions between the hands. No hand-object quantity. | yes |
| `rotateit_2023` | paper 8k/1 | Nothing. One hit in related work. | yes |
| `unidexgrasp_pp_2023` | paper 10k/2, ocr 11k/2, code 5k/2 | Two citations with "physically plausible" in the title, and `max_depenetration_velocity: 1000.0` twice in the Isaac Gym configs — the engine default, unchanged. Its metric is success rate. Notably its predecessor UniDexGrasp **is** one of the eleven, so the lineage makes the silence deliberate rather than accidental. | yes |
| `visual_dexterity_2022` | paper 19k/5, ocr 11k/2, code 4k/1 | Object-set shape overlap, one collision-avoidance citation, and `max_depenetration_velocity: 1000.0`. Metrics are orientation error and success rate at 0.4 and 0.8 rad. | yes |

## Recoveries: 0 of 25

**No sampled row reports a measurement of interpenetration on its own rollouts.** The field held on
every one of the 25.

Three classes of near miss recurred, and all three are ruled out on the same grounds — none is a
geometric quantity reported over the method's own rollouts:

1. **Robot self-collision**, as an avoidance constraint (`anyteleop_2023`, `bunny_visionpro_2024`,
   `human2sim2robot_2025`) or as a binary reward penalty (`humanplus_2024`, `pianomime_2024`).
   Link against link, not hand against object, and no depth is reported.
2. **Engine settings**, specifically `max_depenetration_velocity` in four Isaac Gym task configs
   (`human2sim2robot_2025`, `unidexgrasp_pp_2023`, `visual_dexterity_2022`). A solver's recovery
   velocity, at its default in three of the four, is not a measurement and is not the paper's.
3. **Words that collide with the vocabulary**: an SDF that encodes a piano keyboard, an IoU over
   bounding boxes or segmentation masks, a tactile sensor's contact depth, and "physically
   plausible" in the title of a cited paper.

**The borderline case, stated so a reader can overrule it.** `graspxl_2024` puts hand-object
interpenetration to 35 human raters as one of four named dimensions of a single 1-to-3 realism
score, on motions its own trained policy produced. It is the only thing in the sample that is
both about interpenetration and about the method's own rollouts. It is recorded as not a recovery
because it reports no penetration quantity — no depth, no volume, no threshold, no distance
function — and because counting a subjective composite would make the survey's own vocabulary
unusable: every "physically plausible" in a results section would then have to count too. A
reader who disagrees gets 1 of 25 rather than 0, and the paragraph in Appendix A states that
alternative rather than hiding it. Either way GraspXL's `penetration` field stays `not addressed`,
because the enum has no value for *assessed subjectively* and promoting it to `measured` would
claim a number that does not exist.

## What 0 of 25 implies for the 85

Sampling 25 of 85 without replacement. If *k* of the 85 carried a recoverable measurement, the
probability that a sample of 25 contains none of them is `C(85-k,25)/C(85,25)`.

| k recoverable among the 85 | P(all 25 miss them) |
|---|---|
| 8 | 0.053 |
| 9 | 0.036 |
| 17 (20 percent, the mildest rate seen on an audited field) | 0.0012 |
| 37 (44 percent, the trial-count rate) | 3e-8 |

So at 95 percent confidence **at most 8 of the 85 rows, 9.4 percent, could be hiding a
penetration measurement**, and the count of eleven becomes a floor of eleven and a ceiling of
nineteen. The equivalent binomial bound, ignoring the finite population, is 11.3 percent. If the
borderline case is counted as a recovery the bound loosens to at most 13 of 85, 15 percent.

The load-bearing comparison is the last two rows of that table. The three fields that were
audited earlier under-counted by 20 to 45 percent. Had the penetration field under-counted at even
the mildest of those rates, a sample of 25 would have missed every recoverable row with
probability 0.0012. It did not under-count at anything like that rate, and the reason is
visible in the verdicts: the recovered trial counts and success criteria were numbers **present in
the source and dropped by a scalar-shaped field**, whereas a penetration number is absent from the
source altogether. The earlier audits measured a schema problem. This one looks for a
literature-level absence, and finds it.

## What changed

**No row was corrected**, because none was wrong. `corpus/rows/` is unchanged by this audit, so
every count in the paper that depends on the penetration field is unchanged: 11 handled, 96
settled, 85 not addressed, 4 closed-loop, 0 reporting on rollouts.

The headline finding survives, and is stated more strongly than before: the paper now says the
field was audited, gives the sample size and the recovery rate, and prints the bound.

Written into the paper in two places, both editions:

- **§VII-B / section 7.2**, beside the claim: sample size, seed, zero recoveries, the 9.4 percent
  bound, and the borderline case named. This also carries out the review's other request under
  O2, that the unaudited-field admission move out of Appendix A to sit beside the claim.
- **Appendix A**, the method: population, seed, what was read, the rule for a recovery, the
  arithmetic, and a pointer to this file. The sentence that said the penetration field had never
  been audited now says it has, and names the two fields — code release and failure mode — that
  still have not.
