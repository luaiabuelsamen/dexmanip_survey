# xela_uskin_2020 — XELA uSkin 3-axis tactile skin, curved fingertip kit for Allegro/LEAP (XELA Robotics; vendor material)

sources: papers/md/xela_uskin_2020.md [a1a64fcb = sha256 of the md on disk; no corpus/manifest.json entry; pages_manifest fetched 2026-09-17: Hannover Messe 2022 A4 leaflet "uSkin Curved" (published 05/2021) and https://xelarobotics.com/products/uscu-alha/] ; no code
source: vendor page; specs are manufacturer claims, not measurements.

## One-line contribution
A soft, 3-axis (shear + normal) tactile skin sold as a curved 30-taxel fingertip (uSCu ALHA) for the Allegro Hand V4 and LEAP Hand, plus flat modules for phalanges and palm (product page; leaflet).

## Hand record (sensor kit; the host hand is the Allegro Hand by Wonik Robotics)
- maker: XELA Robotics Co., Ltd., Shinjuku-ku, Tokyo, Japan (leaflet address; page footer "stemming from Waseda University").
- host hand as described by XELA: "16 independent torque-controlled joints, 4 joints on each finger", "Capable of holding up to 5 kg" (leaflet, "FEATURES OF ALLEGRO HAND by WONIK Robotics"). These are XELA restating Wonik's claims.
- tactile sensing (type): magnetic-based 3-axis taxels; each "mimic[s] a joystick, measuring X, Y and Z force" (leaflet); the page describes "Temperature & Magnetic Compensation" and interference "from nearby magnetic fields"; the words "Hall effect" do not appear in either source (bib says Hall-effect: bib-claim).
- tactile sensing (count): fingertip uSCu ALHA "30 3-axis sensing points, covering all surface except the dorsal side" (page); full Allegro integration "368 3-axis measurements" (leaflet). Up to 64 points per module; each point ~4 x 4 mm; modules from 4 mm thick, uSPr 6.6 mm (page).
- resolution / range: "0.1 gram-force (gf)" resolution; "up to 1500 gram of normal force and can be further overloaded to 3000 gf" per point (page). High/low sensitivity switchable in software.
- rate: uSCu ALHA "Maximum sensing frequency 275 Hz" (page, Specifications). The generic feature text says "Fast Sampling: 500 Hz"; the bib's 500 Hz applies to the family, not the curved fingertip.
- control interface: digital taxels, daisy-chained microcontrollers on CAN, one CAN2USB to the PC; only changes are broadcast; XELA server resamples to constant frequency; websocket API, Python/C++ samples, Windows/Linux, ROS and ROS2 (page). Leaflet: "only 4 wires are required to collect all the tactile information".
- calibration: standard (free) or individual per-taxel (paid) calibration in newtons; per-taxel temperature sensor (page).
- price: not stated (request a quotation).
- open-hardware?: no.
- release status and date: leaflet "Published on 05/2021"; product page current (spec sheet Oct 2024). Bib "commercial since ~2020" is a bib-claim.
- used by (grep -l -i "xela|uskin", self excluded): sparsh_2024.

## Setting
- hand(s): Allegro Hand V4 (Wonik) and LEAP Hand integrations (page, "Integrations"); replaceable outer layer; microcontrollers "encapsulated and can be mounted to the back of the fingers".

## Method
- Not applicable (sensor product). Torque inference: "When the grasped object is in contact with three or more sensing points, also the torques ... are reflected in the measurements (6-axis force / torque sensing)" (page).

## Evaluation
None; no measurements, hysteresis or drift figures given beyond "extremely low hysteresis for a soft skin sensor" (page).

## Limitations stated by the vendor
- Magnetic interference must be compensated by reference measurements (page).
- Higher sensitivity narrows range ("the sensor will saturate at lower forces", page).

## Quotable claims (verbatim)
- "Integrating uSkin regular sensors and uSkin Curved onto the Allegro Hand provides you with 368 3-axis measurements." (leaflet)
- "Each sensing point has a resolution of 0.1 gram-force (gf)" (page)

## Notes for the survey
- Tactile-modality table: taxel count (30/fingertip, 368/hand), 3-axis, 275 Hz at the fingertip. Cross-check any paper quoting 500 Hz for the fingertip kit.
- Only sparsh_2024 in the corpus names uSkin; the bib's "main non-camera skin in tactile RL/IL papers" is not supported by this corpus grep.
