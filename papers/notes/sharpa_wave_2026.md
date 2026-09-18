# sharpa_wave_2026 — SharpaWave 22-DoF dexterous hand with Dynamic Tactile Array (Sharpa Robotics, commercial product 2026)

sources: papers/md/sharpa_wave_2026.md [sha256 c36b1d29; no manifest entry, hash computed from file] ; no code
source: vendor page (https://www.sharpa.com/pages/wave); specs are manufacturer claims, not measurements. Page copyright 2026; no page date.

## Hand block
- maker / country: Sharpa ("© Sharpa Pte Ltd") / not stated on page ("Pte Ltd" is a Singapore company form; inference, not page text)
- DoF: 22 active ("22 Active Degrees of Freedom"; "isomorphic design mirrors the human hand"; "1:1 Scale", palm-width to hand-length ratio ≈ 0.618)
- actuated DoF: 22 ("Actuation System | 22 Proprietary Actuation Modules")
- actuation: not specified beyond "22 Proprietary Actuation Modules" (no tendon/linkage/direct-drive statement)
- fingers: 5; four-finger lateral swing ±20°; minimum grasp diameter 10 mm
- thumb design: not described
- weight / size: 1.3 kg; 208 x 90 x 50 mm
- fingertip force: 20 N | 12 N (spec table has two unlabelled columns; "Specifications may vary between products"). Grip force 150 N | 90 N; payload 40 kg | 24 kg; operating speed 4 Hz | 2 Hz; repeatability ±1 mm; rated lifetime >1,000,000 cycles
- tactile sensing: "Dynamic Tactile Array (DTA)", camera-type array at the fingertip ("Raw Image Output | Supported | Not Supported"): resolution 240x240 | 60x60; force resolution 0.02 N | 0.05 N (table labels this row "Spatial Resolution", a labelling error; the mm row is the spatial one); spatial resolution 1 mm | 2 mm; frame rate 180 fps | 30 fps; force range 0-30 N; max load 50 N; latency 20 ms; 6-D F/T (Fx, Fy, Fz, Mx, My, Mz); inference "Host + On-board" | "On-board"; sensor lifetime >100,000 press cycles. Number of sensors per hand NOT stated (bib says per fingertip; page says "at the fingertip", no count).
- control interface / rate: 1000BASE-T Ethernet, 500 Hz; host software Sharpa Pilot, "Sharpa Wave SDK"; ROS 2; MuJoCo and Isaac Sim models. 18-28 V, 0.75 A @ 20 V static, 0-45 °C.
- price: not on page ("Enquire about Wave" form). bib-claim (unverified): "~$50k reported".
- open-hardware: no
- release status / date: sold separately via sales enquiry; no ship date on page. bib-claims (unverified): shipping since ~June 2026; on Apptronik Apollo 2 and Dexmate Vega. Neither robot is named on the page.
- demonstrated vs specified: spec table plus a "Full Video" YouTube link (content not in source). Reliability claims (page): 2,500,000 press cycles; 4,000 m friction travel; hundreds of impact cycles; "Automatic Protective Clench Responds in 0.10 s"; 3,200 shocks at 30 g; 1,000+ h temperature cycling. All vendor-run.
- used by (grep sharpa): bench2dex_2026 (code: `sharpa_tacmap_cfg.py`; paper: tactile-morphology library entry "240 Taxels Sharpa"), tactile_genesis_2026 (code: task `in_hand_repose-sharpa`), dexverse_2026, gr_dexter_2025 (mention in related work), robotera_xhand1_2024 (a humanoid.guide link only).

## Setting / Method / Evaluation
Not applicable (vendor page). The DTA blurb claims "Detects pressure, slip, force changes, and contact location", "Adjusts grip, pose, and force when objects shift, deform, or become occluded" — capability statements without a metric.

## Limitations stated by the vendor
"Products are continuously iterated and improved; minor differences may occur"; "Specifications may vary between products"; shipped appearance may differ.

## Quotable claims (verbatim)
- "Sharpa Wave is a human-scale, five-finger dexterous hand with 22 active DoF, high-resolution tactile sensing for physical AI research and robot integration."
- "Tactile Resolution | 240×240 | 60×60 ... Frame Rate | 180 fps | 30 fps"

## Notes for the survey
- Highest tactile pixel density in the commercial table; but the two spec columns are unlabelled, so any single number must carry both values or say which configuration.
- Communication (500 Hz) is slower than Unitree Dex5 (1000 Hz) and Wuji (1000 Hz); tactile at 180 fps with 20 ms latency.
- Two benchmark codebases (bench2dex, tactile_genesis) already carry Sharpa configs; check those notes for the simulated taxel model.
