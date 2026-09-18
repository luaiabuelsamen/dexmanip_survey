# wuji_hand_2025 — Wuji Hand / Wuji Hand 2: 20-DoF direct-drive dexterous hand (Wuji Technology, commercial product 2025)

sources: papers/md/wuji_hand_2025.md [sha256 658793c3; no manifest entry, hash computed from file] ; no code
source: vendor page (https://www.wuji.tech/en/hand2, the Hand 2 page); the docs URL (docs.wuji.tech .../overview/) returned HTTP 404. Specs are manufacturer claims, not measurements. Page copyright 2026; spec footnote: "These specifications reflect the current Beta1 product and the SPEC will continue to iterate."

## Hand block
- maker / country: Wuji Technology, founded 2019 / China (footer: "Shanghai ICP No. 2021026345-5")
- DoF: 20 ("Active DOFs | 20 DOF"); "Finger Configuration | Full opposition, lateral movement"
- actuated DoF: 20 (all active; "1000 Hz × 20 axes")
- actuation: direct-drive ("Kinematics | Direct-drive rotary, back-drivable"; highlight "Direct Actuation, Force Penetration"; "High Torque Transparency")
- fingers: 5 (inferred from "Full opposition" and 4 DoF/finger arithmetic; page shows no finger count). Minimum grasping diameter 0 mm.
- thumb design: not described ("Full opposition")
- weight / size: weight not on page; frame ≈ 180 x 80 x 40 mm
- fingertip force: not on page
- tactile sensing: page highlight "Multi-Axis Force/ Torque Fingertip Sensing" and "Touch Aligned, Fingers Refined"; no type, count, or range given. This contradicts bib "no built-in tactile" (bib-claim, unverified; the bib likely described Hand 1).
- control interface / rate: 1000 Hz x 20 axes; "Mode | MIT force-position hybrid"; Ethernet (100BASE-TX); 12 V DC. Ecosystem: Wuji SDK + Wuji Studio, ROS 2, MuJoCo / Isaac Sim models, teleop via Wuji Glove, Apple Vision Pro, Intel RealSense.
- price: not on page ("Contact Sales")
- open-hardware: no; "Open Source" links to github.com/wuji-technology (software; contents not in source)
- release status / date: Hand 2 is "the current Beta1 product"; sold separately via Contact Sales. bib-claims (unverified): Hand 1 shipping 2025, Hand 2 beta 2026, Hand 1 <600 g / ~15 N fingertip / 10 kg static / ±1 mm, Hand 2 ~800 g, USB/RS485/EtherCAT, 300k+ cycles.
- demonstrated vs specified: specified: DoF, control mode, rate, comm, voltage, size. Demonstrated (capability tiles, no data): "Precision Pinch", "Compliant Motion", "Nail Action".
- used by (grep wuji): bench2dex_2026 (code: `multi_ur5_wuji_with_flange.py`, a UR5 + Wuji hand embodiment; paper: bimanual box-loading task text), dexverse_2026, bai_unified_manip_survey_2025 (hand taxonomy list), linkerbot_l20_2025 (incidental "Try: ... Wuji Hand" site link).

## Setting / Method / Evaluation
Not applicable (vendor page). Robustness section: "Robust and Impact-Resistant", "Modular Quick Assembly" — no cycle counts on this page.

## Limitations stated by the vendor
Beta1 spec, will iterate; latest numbers deferred to the (404) documentation.

## Quotable claims (verbatim)
- "Kinematics | Direct-drive rotary, back-drivable"
- "Frequency | 1000 Hz × 20 axes"; "Mode | MIT force-position hybrid"
- "Biomimetic Skeleton & Soft Body"

## Notes for the survey
- The direct-drive column of the commercial table: only 20-DoF fully-actuated backdrivable hand with per-axis 1 kHz hybrid control stated on a vendor page in this corpus. Weight, force, and tactile count remain unknown from the page; do not quote the bib's Hand 1 numbers as Hand 2.
- bench2dex_2026 uses it on a real UR5 rig: that note, not this page, is the source for any measured behaviour.
