# R1 review — hardware, section 3, Tables 2 and 3, Figure 2

I build hands. I checked every cell of `paper/tables/table2_hands_available.md` and
`paper/tables/table3_hands_announced.md` against `corpus/rows/<key>.json` and
`papers/notes/<key>.md`, recomputed every count in section 3 from `corpus/rows/*.json`, and
read `paper/figures/fig2_hands.svg`. Sections 3.1 and 3.5 are the best-sourced prose in the
draft. The tables behind them are not yet reviewable, and four of section 3's counts are wrong.

---

## Blocking

**1. Tables 2 and 3 and Figure 2 are not in the draft at all.**
- *location*: section 3 throughout, e.g. "Table 2 therefore prints actuated DoF beside DoF, and the gap is the informative number", "Figure 2 counts, per hand, the method papers whose own experiments use it", "The bottom rows of Figure 2 carry the finding."
- *the problem*: section 3 discusses Table 2, Table 3 and Figure 2 in fifteen places and none of the three appears in `paper/survey.md`. A reviewer cannot check the section's central artefact.
- *the evidence*: `grep '^#\{1,3\} Table' paper/survey.md` returns Tables 1, 5, 6, 7, 8, 9 only. `paper/sections/03_hands.md` contains no `{{table:...}}` or `{{figure:...}}` marker, while `paper/sections/05_training.md` and `07_evaluation.md` do; `tools/assemble.py` only inlines what the markers name. The tables exist on disk, generated, at `paper/tables/table2_hands_available.md` and `table3_hands_announced.md`; Figure 2 exists at `paper/figures/fig2_hands.svg`. Table 4 and Figure 1 are missing by the same mechanism, and Table 10 is specified in `paper/TABLES.md` but was never generated.
- *the fix*: add `{{table:table2_hands_available}}`, `{{table:table3_hands_announced}}` and `{{figure:fig2_hands}}` to `03_hands.md` at the points where the text first uses each, re-run `tools/assemble.py`, and make the script fail loudly when a section names a table it never includes.

**2. The "tip force N" column of Tables 2 and 3 holds six different physical quantities, and one of them is a number no source states.**
- *location*: Table 2 and Table 3, column "tip force N".
- *the problem*: the column reports, as one comparable number: pull-out resistance, pinch force, a single-finger payload converted to newtons, fingertip normal force under an indenter, a whole-fist grip force, and an unlabelled two-column vendor spec. These are not the same measurement and cannot be ranked against each other. This is the column a hand buyer reads first.
- *the evidence*, cell by cell:
  - `leap_hand_2023` 19.5 N is the pull-out test, "the amount of momentary outward force that can be resisted by a flexed finger... before failure", failure = slip or >15 deg deviation (`papers/notes/leap_hand_2023.md`, Sec. IV-B-3, Table III). Not a fingertip force.
  - `orca_hand_2025` 19.6 N appears in no source as a force. The note reads: "it can hold up to 10.5 kg (103 N) using all four fingers, and up to 2 kg (19.6 N) using only the index finger" at a fixed 600 mA motor current (`papers/notes/orca_hand_2025.md`, Sec. III-A). The row took the index-finger payload, at a control-imposed current limit, and printed it as a fingertip force. `paper/TABLES.md` states "a table cannot contain a value that no note confirmed"; this one does.
  - `ruka_2025` 2.74 N is the pinch test, best of 3 trials, averaged over left and right hands (`papers/notes/ruka_2025.md`, Table III, Sec. IV-C-1).
  - `ilda_hand_2021` 34 N is a single fingertip in the bent pose; the same table gives 28 N stretched and 25 N per finger as actually measured while crushing a can (`papers/notes/ilda_hand_2021.md`, Table 1, l. 486-500).
  - `unitree_dex5_2025` 10 N is measured "when it is pressed by a vertical downward cylinder with a diameter of 1cm" (`papers/notes/unitree_dex5_2025.md`, footnote [2]).
  - `brainco_revo2_2025` gives "pinch >=15 N; full fist grip >=50 N" — a whole-hand figure in a fingertip column (`papers/notes/brainco_revo2_2025.md`).
  - `onex_neo_hand_2026` 45 N is "distal flexion forces up to 45N", a peak vendor claim (`papers/notes/onex_neo_hand_2026.md`).
  - `bidexhand_2025` 2.14 N is the only cell that is a measured fingertip force as such (`papers/notes/bidexhand_2025.md`, Abstract).
- *the fix*: split the column into "force figure" and "what was measured" (pull-out / pinch / fingertip normal / single-finger payload / grip), and carry the protocol in the second. Delete ORCA's 19.6 N from the force column and put "10.5 kg four-finger, 2 kg index, at 600 mA" in a payload column. State in the caption that the column is not a ranking.

**3. Tables 2 and 3 print as plain values the DoF and actuator figures that section 3.4 says have no reachable source, and two of them convert actuator counts into actuated DoF.**
- *location*: Table 3 rows `tesla_optimus_hand_2025` (DoF 22), `figure_03_hand_2025` (DoF 20), `daxo_muscle_v0_2025` (act. DoF 120); Table 2 row `dexhand_open_source_2023` (act. DoF 16).
- *the problem*: the prose is careful and the tables are not. Both tables sort by DoF, so an unsourced number also sets a row's rank.
  - Tesla: the text says "The repeated 22-DoF figure is that article's arithmetic of four DoF on each of five fingers plus two at the wrist... As manufacturer statements, both have no reachable source." The note agrees: "'The 22-DoF architecture' (Teslarati's own phrase, not attributed to the patent)... is the article's arithmetic, not stated as such" (`papers/notes/tesla_optimus_hand_2025.md`). The table prints 22. The same row also mixes generations: its actuation cell describes V3, its tactile cell describes Gen 2, and Gen 2's own figure is 11 DoF.
  - Figure 03: the text says the 20 comes from a tracker that "does speak... without saying whether either is per hand or for the pair". The note says the same and adds "Number of fingers | 10", i.e. the row is almost certainly for two hands (`papers/notes/figure_03_hand_2025.md`). The table prints 20 in a per-hand column, ranking Figure 03 above ILDA and Pisa/IIT.
  - Daxo: the source says "120 individual actuators"; DoF is "not stated as a number" (`papers/notes/daxo_muscle_v0_2025.md`). A redundant tendon architecture with no rigid joints has far fewer kinematic DoF than actuators. Printing 120 in the actuated-DoF column asserts the opposite.
  - DexHand: the note says "no joint count is given" and "16 slim micro-servos... plus 2 standard micro servos... for wrist flexion and extension" (`papers/notes/dexhand_open_source_2023.md`), and its "Notes for the survey" says explicitly "No DoF number can be quoted; quote servo counts." The table prints act. DoF 16, which is neither the servo total (18) nor a DoF count.
- *the fix*: add an "actuators" column distinct from "act. DoF" and move Daxo's 120 and DexHand's 16 into it. Blank Tesla's and Figure 03's DoF cells and carry the figure as a footnote naming who did the arithmetic. If an unsourced figure must be shown, mark it (e.g. parenthesised and greyed) and sort those rows last rather than by the unsourced value.

---

## Major

**4. "Two hand designs, one from 2005 and one from 2016, carry 52 of the 103 method rows that name a hand at all."**
- *the problem*: 52 is neither the sum nor the union.
- *the evidence*: recomputed over `corpus/rows/*.json` with the patterns in `tools/make_tables.py`. Allegro 35, Shadow 21, sum 56, intersection 7, union **49**. The table's own per-hand counts (35 and 21) and Figure 2 agree with mine; only the prose does not.
- *the fix*: "carry 49 of the 103", and add "seven rows use both."

**5. "Fourteen of the 103 hand-naming method rows use an open-hardware hand, and 11 of those are LEAP."**
- *the problem*: the correct figure is 11, and all 11 are LEAP, which changes the sentence's point from "mostly LEAP" to "only LEAP".
- *the evidence*: the seven rows with `open_hardware: true` are `leap_hand_2023`, `leap_hand_v2_adv_2025`, `ruka_2025`, `ruka_v2_2026`, `orca_hand_2025`, `bidexhand_2025`, `dexhand_open_source_2023`. The union of method rows naming any of them is 11: `bidex_teleop_2024`, `bidexhd_2024`, `cross_embodiment_world_models_2025`, `dexcap_2024`, `dexndm_2025`, `dexterous_functional_grasping_2023`, `dextrack_2025`, `dexwild_2025`, `dreureka_2024`, `unidex_2026`, `videodex_2022` — every one of them a LEAP row. 14 is reachable only by adding the per-hand counts 11 (LEAP) + 2 (LEAP v2 Adv, both already counted) + 1 (Faive, whose row's `open_hardware` is null, see finding 12).
- *the fix*: "Eleven of the 103 hand-naming method rows use an open-hardware hand, and all eleven are LEAP."

**6. Section 8.5 contradicts section 3 and Figure 2 about LEAP.**
- *location*: "`leap_hand_2023` is the counterexample at 12."
- *the problem*: section 3.2, Table 2 and Figure 2 all say 11.
- *the evidence*: recomputed union is 11 (finding 5); `paper/figures/fig2_hands.svg` prints "LEAP 11"; `table2_hands_available.md` prints "11: `bidex_teleop_2024`, ...".
- *the fix*: 12 → 11.

**7. Section 5.5 conflates joints with actuated DoF, the exact error section 3.1 is written to prevent.**
- *location*: "None of the eight evaluates on the 16 to 24 actuated degrees of freedom that the reinforcement learning literature of section 5.2 runs on"; and "2 to 4 hours on a real 24-DoF Shadow Hand".
- *the problem*: no hand in this corpus has 24 actuated DoF. The Shadow Dexterous Hand has 20 actuated DoF and 24 joints, 4 of them coupled and not independently controllable.
- *the evidence*: `papers/notes/shadow_dexterous_hand_2005.md`: "20 actuated DOF and a further 4 under-actuated movements for a total of 24 joints"; "Distal finger joints are coupled and not independently controllable (Sec. 2.3)"; and its Notes for the survey: "Its '24 DoF' in learning papers usually means joints, with 20 actuated." Section 3.1 opens on this exact quote.
- *the fix*: "the 16 to 20 actuated degrees of freedom"; and "a real Shadow Hand, 24 joints and 20 actuated".

**8. The eight tactile method rows are the wrong eight.**
- *location*: "Eight of 110 method rows feed a physical tactile signal into a policy: `anyrotate_2024`, `articulated_tools_inhand_2025`, `dexteleop0_2026`, `dexumi_2025`, `hato_visuotactile_2024`, `penspin_2024`, `robot_synesthesia_2023` and `rotateit_2023`."
- *the problem*: one work with sixteen physical contact sensors on a real hand is missing, and one work whose tactile channel is simulated and shipped disabled is included.
  - `rotating_without_seeing_2023` is omitted, yet the survey's own section 2 says it "removes vision entirely and rotates objects from 16 binary touch sensors over the palm, links and fingertips". Its note: "16 binary (touch/no-touch) FSR contact sensors spread over an Allegro hand (palm, links, fingertips)... deployed zero-shot to a real XArm+Allegro hand"; observation `o_t ∈ {0,1}^16` is in the deployed policy, not the critic (`papers/notes/rotating_without_seeing_2023.md`).
  - `penspin_2024` is included, but its tactile is simulated binary contact on an Allegro, which has no tactile hardware, its deployed student policy takes joint positions and targets only, and the released config sets `enable_tactile: False`. Section 5 of this same draft says so: "`penspin_2024` zeroes the disturbance force its appendix describes and disables the tactile observation channel." Evidence: `papers/notes/penspin_2024.md`, observation line and code note; Table 2 gives Allegro tactile "none".
- *the fix*: add `rotating_without_seeing_2023`; either drop `penspin_2024` or keep it with the sentence "whose tactile channel is simulated and is disabled in the released config". State the inclusion rule explicitly ("a sensor physically on the hand, read by the deployed policy"), because that rule is what correctly excludes `dexndm_2025` and `dexplore_2025`, whose notes also carry binary-contact observations but in simulation only.

**9. "Thirty-five of the 110 mention tactile somewhere" counts the notes, not the papers.**
- *the problem*: as written the sentence is a claim about what the papers say. It is a claim about what the note template captured, and it understates the real figure by a factor of nearly two, which weakens the survey's own argument.
- *the evidence*: 35 of the 110 method keys have "tactile" or "taxel" anywhere in `papers/notes/<key>.md`; 65 of them have it in `papers/md/<key>.md` or the note. Recomputed directly.
- *the fix*: "Sixty-five of the 110 method papers mention tactile sensing; eight feed a physical tactile signal into a policy." That is a better gap than the one currently claimed. If the 35 is kept for some other reason, label it as a count over the notes.

**10. The "source" column, which `paper/TABLES.md` calls "the column reviewers should read first", is wrong in four rows, and the prose knows it.**
- *the evidence*:
  - `allegro_hand_v4_2016`: source cell "vendor page". Its note is headed "SOURCE THIN: https://www.allegrohand.com/v4 returned HTTP 404 and the Wonik wiki timed out... Everything confirmed below comes from the ROS driver repository." Section 3.2 says the same thing. The source is a driver repo.
  - `robotera_xhand1_2024`: source cell "vendor page". Note: "third-party tracker page (humanoid.guide), not the vendor... The vendor page (robotera.com/en/goods1/4.html) is linked but was not fetched." Section 3.4 correctly calls it "the XHAND1 tracker page".
  - `figure_03_hand_2025`: source cell "vendor page". Note: "SOURCE THIN: the launch page... returned HTTP 404. The only source on disk is a third-party tracker page." Section 3.4 says exactly this.
  - `dexhand_open_source_2023`: source cell "vendor page"; the note's every citation is the GitHub README.
  - Related: `daxo_muscle_v0_2025` carries source "unavailable" and still prints 120 and 750 g.
- *the fix*: make the vocabulary exhaustive and enforced — datasheet / vendor page / third-party tracker / press / driver repo / paper / unavailable — and forbid any non-empty spec cell in a row whose source is "unavailable". Fix the four rows above.

**11. No vendor claim in either table carries a date, which `paper/SECTION_BRIEF.md` rule 5 requires and which `paper/TABLES.md` promises for Table 3.**
- *the problem*: a hand spec without a date is not checkable. `paper/TABLES.md` specifies Table 3 as "Same columns plus the date of the claim and whether it is datasheet, video or press"; the generated table has neither extra column (`tools/make_tables.py` uses the identical `hc`/`hh` lists for both tables). The prose dates some claims well (Shadow December 2024, 1X 9 July 2026, Tesla 13 December 2023, Boston Dynamics 5 January 2026, Xiaomi 30 March 2026) and the tables date none.
- *the evidence*: the notes hold the dates or say there is none — e.g. `unitree_dex5_2025` "Page footer copyright 2016-2025; no page date"; `wuji_hand_2025` "Page copyright 2026"; `sharpa_wave_2026` "Page copyright 2026; no page date"; `tesollo_dg5f_2024` "download links dated 2026/08; no product date"; `xela_uskin_2020` "leaflet Published on 05/2021... spec sheet Oct 2024".
- *the fix*: add a `claim_date` field to the hand rows and a date column to both tables, with "undated page, fetched 2026-09-17" where the page carries no date. That is one field and it converts both tables from assertions into dated claims.

**12. "Two of the six have no cost figure at all" — the six is never defined, and one of the two is not an open-hardware hand.**
- *location*: section 3.3, following the paragraph that quotes LEAP, RUKA, Ruka-v2, LEAP v2 Advanced, DexHand and ORCA verbatim.
- *the problem*: the reader counts six hands in the preceding paragraph, all of which do have a cost figure, then is told two of six have none and is given two different hands. The actual population is seven rows with `open_hardware: true`; five carry a USD figure, ORCA carries a CHF figure the survey deliberately does not convert, and BiDexHand carries none. Faive is a separate case: `corpus/rows/faive_hand_2023.json` has `open_hardware: null`, and `papers/notes/faive_hand_2023.md` records only that a `LICENSE` and `LICENSE-NVIDIA` file exist whose contents were not captured — no open-hardware claim is confirmed anywhere.
- *the evidence*: the seven `open_hardware: true` rows and their prices are LEAP $2000, RUKA $1300, Ruka-v2 $1500, LEAP v2 Adv $3000, DexHand $300, ORCA null, BiDexHand null. Faive's note: "No verifiable BOM cost exists for this hand in the parsed sources — do not populate a dollar figure."
- *the fix*: "Of the seven open-hardware hands, five state a dollar cost, ORCA states 2,000 CHF and BiDexHand states none. The Faive Hand states neither a cost nor a licence we could read, so it is not counted as open hardware here." Then keep the existing Faive and BiDexHand sentences as the evidence for that.

**13. The cost-collapse claim rests on the secondhand prices the survey has just said not to trust.**
- *location*: "Those are secondhand figures in a hardware paper and belong to those tables, not to the vendors." Two paragraphs later: "The collapse is real, from a six-figure hand to a $300 one inside a decade."
- *the problem*: the only six-figure figures on disk are RUKA's comparison table ($100,000 for Shadow) and Faive's citation of "a steep price tag of 110k GBP as quoted from their website". Shadow's own note says price "not stated ('discuss pricing', page)" and marks "~$100k class" a bib-claim. Table 2's price cell for Shadow is empty, correctly.
- *the evidence*: `papers/notes/shadow_dexterous_hand_2005.md` price line; `papers/notes/ruka_2025.md` Table I; `papers/notes/faive_hand_2023.md` Sec. I-B-b.
- *the fix*: "The collapse is real at the cheap end and secondhand at the expensive one. No vendor price for a Shadow Hand is reachable here; the six-figure anchor is two research papers' comparison tables, and the $300 end is a README."

**14. Clone's weight is given a mechanical explanation its source does not give, and an upper bound is tabulated as a point value.**
- *location*: "Clone's 27-DoF hand weighs under 2 pounds only because its 500 W pump sits outside it."
- *the problem*: the "only because" is the survey's inference. The note is explicit: "weight: 'under 2 pounds' (≈0.9 kg; conversion mine). **Whether the pump is included is not stated.**" Table 3 then prints 907 g, a three-significant-figure conversion of a one-significant-figure upper bound.
- *the evidence*: `papers/notes/clone_robotics_hand_2024.md`, weight line.
- *the fix*: "Clone states the hand is under 2 pounds and does not say whether its 500 W pump is inside that figure." Table cell: "<910" or "<2 lb".

**15. Ruka-v2's encoders are described as closing the loop they do not close.**
- *location*: "Ruka-v2 bolts AS5600 encoders onto the joints instead, leaving an 8.26-degree average error under a linear joint-to-motor map."
- *the problem*: the paragraph's subject is what tendon drive costs in state estimation, and this sentence reads as Ruka-v2 solving it with joint encoders. It does not. The encoders are attachable, detachable, and used for calibration and measurement only.
- *the evidence*: `papers/notes/ruka_v2_2026.md`: "Attachable magnetic encoders (AS5600, 12-bit resolution) are read via 'an ESP32 QTPy microcontroller... over an I2C multiplexer board' for calibration/data collection only (Sec. 2.5), **not part of the control loop**." The 8.26 deg is the error of the open-loop linear map as measured by those encoders over 4 index and 3 thumb joints at 20 random angles each (Table 5).
- *the fix*: "Ruka-v2 adds detachable AS5600 encoders to measure the problem rather than close the loop on it: control is still an open-loop linear joint-to-motor map, whose error those encoders put at 8.26 degrees over seven joints at 20 angles each."

**16. The DoF column silently overrides what the vendor calls DoF, and the survey never says so.**
- *location*: "Table 2 therefore prints actuated DoF beside DoF, and the gap is the informative number."
- *the problem*: the column is joints, not DoF, and for at least one hand the vendor's own "DoF" number is the other column. Inspire's page says "Degrees of freedom 6, Numbers of joints 12"; Table 2 prints DoF 12, act. DoF 6. A reader comparing Table 2's Inspire row against the Inspire datasheet finds two different numbers under the same word. Unitree (20 = 16 active + 4 coupled) and Shadow (24 joints, 20 actuated) are the same pattern with the vendor's arithmetic shown; Inspire's is not.
- *the evidence*: `papers/notes/inspire_rh56dfx_2023.md` DoF line; `papers/notes/unitree_dex5_2025.md`; `papers/notes/shadow_dexterous_hand_2005.md`.
- *the fix*: rename the column "joints" and the next one "actuated DoF", and add one sentence to 3.1: "Where a vendor's own DoF figure differs from the joint count, the joint count is what Table 2 prints; Inspire's page says 6 DoF and 12 joints."

**17. "Inspire, XHand and Sharpa take 33 method rows between them."**
- *the problem*: 33 is the sum of three overlapping sets. The union is 29; four rows use two of the three.
- *the evidence*: recomputed from `corpus/rows/*.json` with the `USES` patterns: Inspire 19, XHand 8, Sharpa 6, union 29. Their years are 2024-2026, so the follow-on clause "none predates 2023 here" is true but weaker than the evidence supports.
- *the fix*: "take 29 of the 103 rows between them, none of them earlier than 2024."

**18. Shadow's 4 kg and RUKA's 6.0 kg are put side by side as if they were the same measurement.**
- *location*: "Shadow's hand plus forearm weighs 4.3 kg and holds 4 kg in a power grasp, while RUKA's 11 forearm Dynamixels give a 2.74 N pinch and a 6.0 kg payload."
- *the problem*: the sentence invites the conclusion that a $1,300 hand out-lifts a Shadow. Shadow's 4 kg is an undated-protocol vendor claim ("while in a power grasp, can hold up to 4 kg"). RUKA's 6.0 kg is "weight added to a curled cloth-bag grip until >15 deg joint-angle error", best of three trials, averaged over left and right hands. Different grasp, different failure criterion, one measured and one claimed.
- *the evidence*: `papers/notes/shadow_dexterous_hand_2005.md` Sec. 2.4; `papers/notes/ruka_2025.md` Table III and Sec. IV-C.
- *the fix*: give each figure its protocol in the same sentence, or drop the juxtaposition and make the point you actually have, which is that no two hands in Table 2 report payload under the same test.

**19. "a quarter of Shadow's mass for a larger force" compares a hand against a hand plus forearm, and against a force Shadow never states.**
- *location*: section 3.1, ILDA.
- *the problem*: ILDA's 1.1 kg is the hand, with all 15 motors inside the palm and no forearm. Shadow's 4.3 kg is "Hand and forearm". And Shadow's fingertip force is "not stated" in its note and empty in Table 2, so there is no Shadow force for ILDA's 34 N to be larger than. The only Shadow force figure on disk is the 4 kg power-grasp payload, against ILDA's stated 18 kg payload — which is the comparison the sentence should be making.
- *the evidence*: `papers/notes/ilda_hand_2021.md` Table 1; `papers/notes/shadow_dexterous_hand_2005.md` Sec. 2.4 and fingertip-force line.
- *the fix*: "ILDA's 1.1 kg is the hand alone, against 4.3 kg for a Shadow hand and forearm, and it states an 18 kg payload against Shadow's 4 kg. Shadow states no fingertip force, so the fingertip figures cannot be compared."

**20. AgiBot sits in "Hands that can be obtained" with no specification at all, and section 8 says it is in the other table.**
- *location*: Table 2, row `agibot_omnihand_2025`; section 8, "the AgiBot pages 404, so it cannot be matched to Table 3."
- *the problem*: the row has 10 of its 11 spec cells empty, a blank status and source "unavailable", and it lands in Table 2 only because `release_status` is null and `tools/make_tables.py` puts null in the sold bucket. Section 3.4 is right that the hand "exists, is used, and cannot be specified"; section 8 then says it cannot be matched to Table 3, when in fact it is the one row in Table 2 with nothing in it.
- *the evidence*: `papers/notes/agibot_omnihand_2025.md` ("SOURCE THIN: both vendor URLs returned HTTP 404... No spec below is verified"); the `sold` filter in `tools/make_tables.py`.
- *the fix*: give the row an explicit status ("sold, unspecifiable") rather than null, decide which table it belongs in, and make the script raise on a null `release_status` instead of defaulting. Fix the section 8 sentence to name the table it actually lands in.

---

## Minor

**21. "LEAP's Dynamixel joints give a 19.5 N pull-out force against the Allegro Hand's 8.5 N at 595 g."** The 595 g is LEAP's weight ("The 4-finger LEAP Hand weighs 595g", Sec. V), not the Allegro's; the Allegro's weight has no reachable source at all and its Table 2 cell is empty (`papers/notes/allegro_hand_v4_2016.md`: "weight: not stated in sources (bib ~1.1-1.2 kg: bib-claim)"). Fix: "...against the Allegro Hand's 8.5 N, at 595 g for the LEAP hand; the Allegro's weight has no reachable source."

**22. ILDA's 34 N is quoted without the pose it was measured in.** The note gives 28 N stretched, 34 N bent, and 25 N per finger measured while crushing an aluminium can (`papers/notes/ilda_hand_2021.md`, Table 1, Fig. 6b). `paper/SECTION_BRIEF.md` rule 2 asks for the condition beside the number. Fix: "34 N at the fingertip in the bent pose, 28 N stretched".

**23. Table 3's title misdescribes four of its thirteen rows.** "Hands announced but not purchasable" contains three published research prototypes (`ilda_hand_2021`, `pisa_iit_softhand_2014`, `faive_hand_2023`) and one open-hardware hand with a published price and released CAD (`leap_hand_v2_adv_2025`, $3000), which section 3.3 uses as a cost-collapse data point. Pisa/IIT's note further records that the hand "is sold with" qbTools electronics. Section 3.6 already has to write around this ("The four research prototypes in Table 3 are not in that position"). Fix: split by evidence class rather than purchasability — "company announcements" and "research prototypes" — which is the distinction 3.4 opens with anyway.

**24. "Two hand designs, one from 2005 and one from 2016" dates both hands from bib-claims their own notes flag as unverified.** Shadow's parsed spec is dated December 2024 and "commercial since 2005" is marked a bib-claim; the Allegro driver's zero files "span versions 1.0, 2.0, 3.0 and 4.0; no dates" and "V4 2016-2024" is marked a bib-claim (`papers/notes/shadow_dexterous_hand_2005.md`, `papers/notes/allegro_hand_v4_2016.md`). Fix: say the designs are of 2005 and 2016 "by the bibliography's dating, which neither source confirms", or drop the years and say "the two oldest designs in Table 2".

**25. Proception is filed as "sold" on the strength of a launch post.** The note records no datasheet, no weight, no force, no actuated-DoF count, and "the first batch of units is shipping this week" from a Y Combinator post (`papers/notes/proception_prohand_2026.md`). A shipping announcement is not the same evidence class as Tesollo's or Unitree's spec tables. Section 3.4's own sentence ("Beyond the 22, nothing is specified") is the argument against its Table 2 placement. Fix: status "announced shipping, 2026-06-29".

**26. Two attributions in 3.1 rest on file names rather than on any statement.** The Ability Hand's linkage drive rests on repo filenames (`get_abh_4bar_driven_angle.m`) and its five fingers on URDF meshes; the page states neither ("actuation: linkage. Page does not say... so 'linkage' rests on code file names"; "fingers: 5 implied by URDF meshes; page does not count them", `papers/notes/psyonic_ability_hand_2021.md`). Table 2's actuation cell flags this and the prose does not. Fix: "the Ability Hand, whose six motors are stated and whose four-bar fingers are inferred from its own repository".

**27. BiDexHand carries a paper/code actuator mismatch the survey does not flag, in a survey whose thesis is paper/code mismatches.** Paper: "16 independently actuated degrees of freedom and 5 mechanically coupled joints... 21 joints in total". README: "15 servos arranged in N configuration to drive its 15 joints" (`papers/notes/bidexhand_2025.md`). Table 2 prints 21/16 with no mismatch note. Fix: one clause in 3.1 or a footnote to the row.

**28. The XHAND1 "15 N" is real but untraceable through the notes.** The figure is in `papers/md/welte_iil_survey_2025.md` line 75 ("XHAND1 (ROBOTERA, 2025) | 12 | 12 | direct drive | 5 | 15 N | 16-25 kg | 1.1 kg | yes"), but `papers/notes/welte_iil_survey_2025.md` records the Table 1 column list without that cell, so a reader following the survey's own evidence rule ("from a note that names the table the number is in") cannot confirm it. Fix: add the XHAND1 row to the welte note.

**29. Both emptiness percentages are diluted by columns that can never be empty.** "Twenty-eight percent of its cells are values no source stated, against 21 percent for the hands that can be bought" counts the key column and the "corpus methods using it" column, neither of which is ever blank (`used_by` prints "0"). Over the eleven specification columns only, the figures are 34 percent for Table 3 and 25 percent for Table 2. Moving AgiBot to Table 3, per finding 20, gives 38 and 22. The finding survives in every version, which is worth saying. Fix: quote the spec-column percentages and state the denominator.

**30. ORCA's 0.05 N threshold is a best case against a 0.29 N rated part.** The note: "Absolute detection threshold measured down to 'as low as 0.05 N with perfect accuracy over 10 cycles' (Sec. III-E) despite the FSR's rated minimum trigger force of 0.29 N", and a degraded fingertip's threshold rose to 6.38 N (`papers/notes/orca_hand_2025.md`). The survey quotes the 0.05 and, two paragraphs earlier, the degradation, without connecting them. Fix: "measured as low as 0.05 N on a fresh fingertip, against the sensor's rated 0.29 N, and 6.38 N on a degraded one."

---

## What is sound, and what section 3 is missing

**Sound.** Section 3.5 is the strongest prose in the draft on my side of the paper. I checked every number in it and every one holds with its condition: DIGIT's 20x27x18 mm, 20 g, 640x480 at 60 fps and $15-in-1000 (`papers/notes/digit_2020.md`, Table I); the 0.3 percent against 805 and 918 percent at 15 abrasion passes (Table II); Digit 360's 8.3 M taxels, 7 um, 1.01 and 1.27 mN and 6 ms to 1.2 ms, and that it is not for sale (`papers/notes/digit360_2024.md`); XELA's 30 points on the curved fingertip, 368 on a full Allegro, 0.1 gram-force, 275 Hz, and the correction that the 500 Hz belongs to the family rather than the fingertip (`papers/notes/xela_uskin_2020.md`); Sparsh's 462.7k images, 95.1 percent at 33-50 percent of labels, the bead maze never completed on the real robot, and the unresolved 320x240 against 640x480 (`papers/notes/sparsh_2024.md`). The closing observation — taxel counts up three orders of magnitude while the policies consuming them stayed binary — is the best sentence in section 3. The Tesollo paragraph in 3.4 is exactly right (1,763 g, Modbus and Ethernet, against two survey tables rounding to 1.7 and 1.8 kg and one inventing EtherCAT), and so is the treatment of Sharpa's two unlabelled columns, Wuji's missing weight and force, Boston Dynamics' empty blog, and Xiaomi's 83 percent with no absolute count. The Faive, ORCA and Pisa/IIT quotes all check out verbatim.

**Does 3.1 help a reader choose a hand?** Mostly yes, and it is the right organising axis: transmission, then what the transmission costs you (state estimation for tendons, mass for forearm drives, repairability, the mechanical fuse). That is how hands are actually chosen. Two things are missing that this survey's own notes already contain and that its audience needs first:

- **Control interface and bandwidth.** Nothing in Table 2 or section 3 tells a reader what rate they can close a loop at, and it varies by a factor of four across hands people actually buy: Allegro CAN at the hand's own 333 Hz clock, Shadow EtherCAT at 1 kHz with a 5 kHz in-module torque loop, Sharpa Ethernet at 500 Hz, Tesollo 250 Hz, Wuji and Unitree 1 kHz, Inspire RS485 with no stated rate, LEAP up to 500 Hz over USB serial. Every one of those is in the note. A reader deploying a 20 Hz policy does not care; a reader deploying torque control does, and it is the first thing that bites. LEAP's note even warns to keep the 500 Hz query ceiling and the 20 Hz policy rate distinct. Add the column.
- **Whether a simulation model exists, and whose.** For a survey whose spine is simulators and sim-to-real, Table 2 does not say which hands ship a URDF or MJCF. The notes do: Shadow's `sr_common` ships MuJoCo models for Hand E and variants; Sharpa and Wuji ship MuJoCo and Isaac Sim models; ORCA and RUKA ship MJCF assets; the Ability Hand's repo ships a MuJoCo simulator and an Isaac Sim path; and LEAP's released API repo contains **no** URDF despite the paper claiming one, which `corpus/rows/leap_hand_2023.json` already records as a paper/code mismatch. Section 8.5 asks for "a conformance suite for hand models, with one URDF or MJCF per hand" without first telling the reader which hands have one. That column is the bridge between section 3 and section 4, and it is free.

**Is the open-hardware cost story told accurately?** The quoting discipline is right and unusual — verbatim, on inconsistent bases, with ORCA's CHF left unconverted. The arithmetic around it is not (findings 5, 12, 13). Two further things it gets wrong by omission. DexHand's $300 is "additional total cost of components", i.e. excluding the printing, and it excludes the wrist servos; the survey quotes it verbatim but then calls DexHand "sold, documented and cheap" in 3.6, where it is not sold at all. And ORCA's own "below 2,000 CHF" sits against Ruka-v2's comparison table listing ORCA at "~$3.5K" (`papers/notes/ruka_v2_2026.md`, Table 1) — a nearly twofold disagreement between a hand's own paper and another hand's table, which is precisely the kind of secondhand-figure problem 3.3 raises and then does not apply here.

Relatedly, section 3.6's closing list — "Hands that are sold, documented and cheap go unused: the Unitree Dex5... the fully actuated Tesollo DG-5F, ORCA, RUKA, Ruka-v2, BiDexHand and DexHand" — asserts cheapness for four hands with no price on record. Table 2's price cell is empty for Unitree, Tesollo, BiDexHand and ORCA, and the only Dex5 price anywhere on disk is Ruka-v2's secondhand "~$25K" (`papers/notes/ruka_v2_2026.md`, Table 1), which is not cheap. Fix: "sold and documented", and move "cheap" to the three hands that state a figure.

**Is the treatment of unreleased hands sceptical enough?** The prose is, and 3.4 is the most careful part of the section. The scepticism is applied by table membership rather than by evidence class, which is the flaw. Every vendor-page hand in Table 2 carries the same warning in its own note — "specs are manufacturer claims, not measurements" — and gets none of 3.4's framing: Sharpa's 22/22, Wuji's 20/20, Unitree's 20/16 and Tesollo's 20/20 are all stated in the text and tables as facts about hardware nobody outside the company has measured. Sharpa's page even footnotes "Specifications may vary between products" and Wuji's says the spec "will continue to iterate" on a Beta1 product. One sentence at the head of 3.1 would fix it: no DoF, force, weight or price figure in Table 2 or Table 3 has been measured by anyone outside the maker, and four of them (ILDA, Pisa/IIT, ORCA, RUKA, and the LEAP/BiDexHand fingertip forces) come from peer-reviewed papers with stated protocols, which is a different thing.

It is not too sceptical. If anything it stops one step short of what a survey can add over a tracker page, which is an engineering sanity check. Daxo's claim is 120 actuators in 750 g — about 6 g per actuator including structure, tendons, routing and skin — and the survey records that it has no reachable source without noting that it is also extraordinary. Clone's 27 DoF under 2 lb excludes a 500 W pump that the source does not even confirm is excluded. Figure 03's "20" is almost certainly ten per hand. Saying which unverifiable claims are merely unverified and which are implausible on their face is the judgement `paper/SECTION_BRIEF.md` asks for under "Voice", and it costs three sentences.

**Length.** Section 3 is 2,919 words against a 2,200 target, 33 percent over the brief's 20 percent allowance. 3.4 is where it goes: nine paragraphs to establish one finding that 3.6 then restates. Findings 5, 12, 13 and the two missing columns above would all fit inside the words 3.4 could give back.

---

## Findings by severity

- blocking: 3
- major: 17
- minor: 10
- total: 30
