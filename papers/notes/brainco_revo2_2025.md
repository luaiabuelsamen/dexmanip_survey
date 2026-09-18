# brainco_revo2_2025 — BrainCo Revo 2 dexterous hand (BrainCo, commercial product 2025)

sources: papers/md/brainco_revo2_2025.md [34e99937, sha256 of the parsed page; no manifest entry, fetched 2026-09-17 from brainco-hz.com/docs/revolimb-hand/en/revo2/parameters.html] ; no code
source: vendor documentation page (parameters table); specs are manufacturer claims, not measurements.

## One-line contribution
A 383 g, 6-motor / 11-DoF bionic hand in three variants (Basic / Pro / Touch) with RS485, CAN FD and (Pro/Touch) EtherCAT, five control modes and, on Touch, a fingertip tactile module with "Tactile Adaptive Control".

## Setting
- hand(s): Revo 2 (models BASIC XRL/XRR, PRO XEL/XER, TOUCH XTL/XTR; L/R = left/right); BrainCo Inc. Country not stated on the page (docs domain brainco-hz.com, Chinese-language alternate)
- simulator / physics: none on page; "SDK supports Python/C and is compatible with Linux/Windows/ROS systems"
- observation: "Position, velocity, current feedback control"; Touch adds tactile
- action space: control modes 1-5 (table "Control Mode Description"): Position+Time, Position+Speed, Speed, Current, PWM; rate not stated

## Hand record (all from the page's "Product parameters" and "Parameter description" unless marked)
- maker / country: BrainCo; country not stated on page
- DoF: 11; actuated DoF: 6 ("6 active joints and 11 degrees of freedom")
- actuation: not stated on the page (motors named FINGERID_*; "Turbo mode is based on stall detection"). bib-claim: tendon/linkage from micro motors
- fingers: 5 (thumb + four fingers; "Maximum opening and closing distance | 100mm (from thumb to index finger)")
- thumb design: "two active degrees of freedom for abduction and adduction, as well as one passive degree of freedom for flexion and extension"; ranges Thumb Flex 0-59 deg, Thumb Aux (add/abd) 0-90 deg. Each other finger: 1 active flex (0-81 deg) + 1 passive
- weight: 383 g; height 160 mm (palm base to middle fingertip)
- fingertip force: pinch >= 15 N; full fist grip >= 50 N; max payload >= 20 kg; flexion/extension <= 0.65 s; noise <= 50 dB at 50 cm; repeat precision 0.1 deg
- tactile sensing: Basic and Pro "/" (none); Touch "Multi-dimensional fingertip tactile module" plus "Tactile Adaptive Control"; count and type not stated. bib-claim: multimodal tactile at 0.1 N
- control interface and rate: Basic 485 / CAN FD; Pro and Touch 485 / CAN FD / EtherCAT; supply 12-28 V (Basic), 12-64 V (Pro/Touch); max current 4.6-4.65 A at 24 V; rate not stated. Default IDs 126 (left) / 127 (right)
- price: not stated. bib-claim: ~$8.9k MSRP
- open-hardware?: no (SDK only)
- release status and date: shipping (docs cover Revo 1, 2 and 3; OTA upgrades); no date on page. bib-claim: 2025
- used in corpus: bench2dex_2026 (task row "Faucet Cup Water Fill | RM65+Revo2"), bidexgrasp_2026 ("ShadowHand grasps are retargeted [35] to the Inspire and BrainCo hands"), linkerbot_l20_2025 (reseller cross-link "BrainCo Revo II -- Bionic hand with BLE + USB dual interface", only)

## Method
- n/a (hardware). "Smart Control": position/velocity/current feedback, cascaded control, compliance control; Touch adds tactile adaptive control. Protections: current, stall, high temperature, anti-collision.
- key trick(s): Turbo mode "pauses for the configured stall duration and then continues gripping at 500 ms intervals" for soft or shifting objects.

## Evaluation
- specified in a datasheet: everything above.
- demonstrated in video: none on this page.
- real robot: none named on this page (bib "why" names Unitree).

## Limitations stated by the authors
- "During the position calibration process, if the dexterous hand is currently gripping an object, it will drop the object." and "position calibration must be completed successfully before normal control is permitted." (Power-on auto-calibration)

## Quotable claims (verbatim, with section)
- "It provides 6 active joints and 11 degrees of freedom, supports RS485, CAN FD, and EtherCAT communication interfaces" (Overview)
- "Full fist grip force | >=50N ; Pinch force | >=15N ; Max Payload | >=20kg ; Flexion/Extension Speed | <=0.65s" (Product parameters table, flattened)

## Notes for the survey
- Hardware table: the lowest-DoF entry among the commercial five-finger hands here (6 actuated), coupled flex on every finger; contrast with XHAND1's 12 fully actuated joints at 3x the weight.
- Tactile column: only the Touch variant; count unknown. The bench2dex row is the one closed-loop use in the corpus.
