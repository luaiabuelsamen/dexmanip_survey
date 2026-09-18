# tesollo_dg5f_2024 — TESOLLO DG-5F / DG-5F-M / DG-5F-S humanoid robot hand (TESOLLO, commercial product 2024)

sources: papers/md/tesollo_dg5f_2024.md [sha256 7afa92b4; no manifest entry, hash computed from file] ; no code
source: vendor page (https://www.tesollo.com/products/grippers/dg-5f-m, the DG-5F-M page); the catalogue PDF (bib pdf_url) returned HTTP 404. Specs are manufacturer claims, not measurements. Page copyright 2026, download links dated 2026/08; no product date. DG-5F-S is a separate page, not fetched. bib entry marked verified: false.

## Hand block (DG-5F-M)
- maker / country: Tesollo Inc., CEO Young-Jin Kim, Incheon (HQ) and Gwangmyeong (R&D, factory) / South Korea
- DoF: 20 ("20 DoF (4 DoF per finger)")
- actuated DoF: 20 ("fully actuated"; "Each of the 20 joints is driven by its own integrated actuator, enabling fully independent joint control without inter-joint mechanical coupling")
- actuation: one integrated actuator per joint, "high-torque actuation", absolute encoder. The page does not say "direct-drive"; bib "direct-drive (low backlash)" is a bib-claim.
- fingers: 5, "anthropomorphic", "Modeled after the size and proportions of an adult male hand"
- thumb design: not described
- weight: 1,763 g (page). bib says "1.4 kg (DG-5F-S < 1 kg)": contradicts the page for the M; the S value is unverified.
- fingertip force: not stated. Gripping capacity: "Pinching Payload (Rated / Max) : 2.5 / 5 kg, Envelop Payload (Rated / Max) : 10 / 20 kg *Performance may vary depending on object friction." bib "7 kg grip force" is not on the page.
- tactile sensing: none standard. Options: "Fingertip Sensor (6-axis F/T Sensor)", "Fingertip Sensor (3-axis Force Sensor)", "Fingertip Sensor (Tactile Sensor)"; count and type not given.
- control interface / rate: "Modbus (RTU, TCP), Ethernet (TCP/IP)"; control frequency 250 Hz; 24 V, max 10 A; ROS 2 integration; URCaps 1.0.2 and TMflow2 1.0.2 plugins; GitHub github.com/tesollodelto; Delto Gripper Manager and SDK. bib "EtherCAT" is not on the page.
- price: not on page ("Contact sales"). bib-claim (unverified): "~$8.8k list".
- open-hardware: no (manuals and SDK downloadable: Control Manual v2.0.0, Hardware Manual v2.0.0, Short Wrist Hardware Manual)
- release status / date: shipping product sold separately, with distributors ("Find a Distributor"). bib-claim: "shipping since 2024". Other options: suction-type fingertip, short-wrist version, mounting stand.
- demonstrated vs specified: specified in the spec list above; grip modes (pinch, power, precision) are described, not measured. No videos in the source.
- used by (grep tesollo|dg-5f over code/md, papers/md): zhao_dexhand_survey_2026 (table row: DG-5F, 2024, 5 fingers, 20 DoF, 24 V, 10 A, 20 kg, 1.8 kg, "EtherNet, Modbus"), welte_iil_survey_2025 (table row: 20/20, "direct-drive", 2.5-10 kg, 1.7 kg). No repo drives it.

## Setting / Method / Evaluation
Not applicable (product page). Applications named: humanoid research, in-hand manipulation ("object assembly and connector fastening"), tool use and dual-arm tasks.

## Limitations stated by the vendor
Payload "may vary depending on object friction". DG-3F-B is discontinued (menu).

## Quotable claims (verbatim)
- "Each of the 20 joints is driven by its own integrated actuator, enabling fully independent joint control without inter-joint mechanical coupling."
- "Control Frequency | 250 Hz"; "Weight | 1,763 g"

## Notes for the survey
- Fully-actuated 20-DoF row; the slowest stated control rate among the commercial hands here (250 Hz vs 1000 Hz Unitree/Wuji, 500 Hz Sharpa) and the heaviest (1.76 kg).
- Two survey tables round the weight differently (1.7 / 1.8 kg); the page says 1,763 g. Both surveys and the bib call it direct-drive; the page says only "integrated actuator" per joint.
