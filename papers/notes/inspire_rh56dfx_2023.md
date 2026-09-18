# inspire_rh56dfx_2023 — Inspire Robots RH56DFX dexterous hand (Beijing Inspire Robots Technology; commercial product)

sources: papers/md/inspire_rh56dfx_2023.md [584a427e = sha256 of the md on disk; no corpus/manifest.json entry; pages_manifest fetched 2026-09-17 https://en.inspire-robots.com/product/rh56dfx/] ; no code
source: vendor page; specs are manufacturer claims, not measurements. The page's parameter table is headed "without tactile sensors"; the tactile (FTP) variant in the bib is not on this page.

## One-line contribution
A six-motor, twelve-joint five-finger hand at 540 g with integrated absolute position and force sensors, RS485, and power-off self-locking, sold in left/right and with an optional 2-DoF wrist (page, Product Parameters).

## Hand record
- maker: Beijing Inspire Robots Technology Co., Ltd. (page footer). country: China.
- DoF: "Degrees of freedom 6", "Numbers of joints 12" (RH56DFX-2L/2R); with wrist (RH56DFXW-2L/2R) "6+2" DoF, 12 joints (page table).
- actuated DoF: 6 (8 with wrist).
- actuation: not stated on this page. Inspire's product menu lists a "Micro Linear Servo Actuator" line (LA/LAS/LAF/LASF/BLA series); the bib's "6 micro linear servos, linkage" is a bib-claim.
- fingers: "humanoid five finger dexterous hand" (page intro).
- thumb design: "Lateral rotation range of thumb >65°" at 107°/s and thumb flexion 70°/s, so the thumb has its own lateral (opposition) motor and flexion motor; the four fingers flex at 260°/s (page table).
- weight: 540 g; 650 g with wrist (page table).
- fingertip force: "Thumb Fingertip Strength 15N", "Fingertip Strength 10N", "Force resolution 0.50N" (page table). Intro text: "thumb active output force of 1.5KG and a four finger fingertip output force of 1KG".
- tactile sensing: none on this model ("without tactile sensors"). "Integrated absolute position sensors and force sensors, it provides real-time force feedback" (intro). Bib "RH56DFTP fingertip+palm arrays" is a bib-claim.
- control interface and rate: RS485 (page table); rate not stated. DC 12-48 V; quiescent 0.09 A @ 24 V; peak 2 A @ 24 V; repeatability ±0.20 mm. Wrist: yaw ±27°, pitch ±22°, load torque 2 N m excluding hand weight. Bib "RS485/CAN" only RS485 is confirmed.
- price: not stated ("Get a Quote"). Bib "~$5.5-5.6k" is a bib-claim.
- open-hardware?: no. A Developer/Download section exists but its contents were not fetched.
- release status and date: shipping product; "Leading cumulative shipments, proven stable performance" (page). No date on the page (bib "since 2023" is a bib-claim).
- used by (grep -l -i "rh56|inspire robot|inspire-robot|inspire hand|inspire dexterous|inspire's", self excluded): 14 keys. Ten: an_dexil_survey_2025, bench2dex_2026, bidexgrasp_2026, dexmachina_2025, dexplore_2025, dexumi_2025, dexverse_2026, humanplus_2024, maniptrans_2025, omnih2o_2024 (also bai_unified_manip_survey_2025, maniskill3_2024, welte_iil_survey_2025, zhao_dexhand_survey_2026). The bare word "inspire" hits many more files as ordinary English and was excluded.

## Setting
- Variants on the page: RH56DFX-2L/2R (no wrist), RH56DFXW-2L/2R (with wrist). Related products RH56BFX, RH56E2, RH56F1, RH5DG2, RH56H1 (nav), not described.

## Method / Evaluation
None (product page). Feature claim: "Power off self-locking, no need to change position when powering on" (intro).

## Limitations stated by the vendor
None stated.

## Quotable claims (verbatim)
- "The DFX series humanoid five finger dexterous hand is a perfect combination of strength and speed,with a thumb active output force of 1.5KG and a four finger fingertip output force of 1KG." (page intro)

## Notes for the survey
- The low-actuator end of the commercial table: 6 motors / 12 joints / 540 g / 10-15 N. Contrast ILDA (15 motors, 34 N, 1.1 kg) and Shadow (20 motors, 4.3 kg).
- Widely used in the corpus (14 keys: humanoid teleop and sim-to-real work), which supports the bib's "shipped on Unitree G1/H1" only indirectly; that claim itself is not on the page.
