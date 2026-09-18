# unitree_dex5_2025 — Unitree Dex5-1 / Dex5-1P dexterous hand (Unitree Robotics, commercial product 2025)

sources: papers/md/unitree_dex5_2025.md [sha256 d7a4ea18; no corpus/manifest.json entry for this key, hash computed from the file] ; code/md/unitree_dex5_2025.md [unitree_sdk2 @ c7538298]
source: vendor page (https://www.unitree.com/Dex5-1); specs are manufacturer claims, not measurements. Page footer copyright 2016-2025; no page date.

## Hand block
- maker / country: Unitree Robotics (footer: Yushu Technology Co., Ltd., Zhejiang ICP filing) / China
- DoF: 20 ("20 Degrees of freedom (16 active+4)"; per-finger table: thumb x4, index/middle/ring/little x3 each = 16 listed; four-finger "Knuckles 3: 0°~81° (Coupling with finger joint 2)" is the coupled 4th joint per finger)
- actuated DoF: 16 ("12 self-developed micro force-controlled composite transmission joints" + "4 micro force-controlled joint gear transmission"); 4 coupled/passive
- actuation: in-joint geared motor ("hollow-cup motor", "high-precision encoder", "Low damping small clearance reducer"), backdrivable ("support smooth backdrivability"). Page does not use the words tendon or linkage; the transmission type behind "composite transmission" is not specified.
- fingers: 5, "All five fingers can be replaced independently"; four-finger lateral swing ±22°; minimum grip diameter 10 mm
- thumb design: 4 joints; ranges Thumb Joint 0: -33.5°~39°, 1: 0°~100°, 2: 0°~110°, 3: 0°~92° (spec table). Four-finger joints: 0: -22°~22°, 1: 0°~90°, 2: 0°~95°, 3: 0°~81°.
- weight / size: 1100 g; 217.3 x 127.5 x 72.1 mm flat ("The final shipped version may vary")
- fingertip force: 10 N ("Fingertip strength"); footnote [2]: measured "when it is pressed by a vertical downward cylinder with a diameter of 1cm". Repeatability ±1 mm. Load: 3.5 kg palm down, 4.5 kg palm facing left, "Grasping A 5cm Round Hard Object".
- tactile sensing: Dex5-1: none ("/"). Dex5-1P: "12 (94 pressure sensors in total)"; array resolution 2x5 palm, 2x3 per finger pad x5, 2x3 per fingertip x5, 2x3 per finger root x4 (= 10+30+30+24 = 94); range 10 g-2500 g; "Maximum Acceptance (Unamaged)" 20 kg
- control interface / rate: USB 2.0; communication rate 1000 Hz; packet 1234 B send / 1270 B receive; feedback: joint mode, position, velocity, torque, temperature, voltage/current, IMU (+ sensor pressure and temperature on P); command: mode, position, velocity, torque, stiffness coefficient, damping coefficient (i.e. PD-with-feedforward-torque per joint). 24-60 V, 58 V @ 0.2 A static, 58 V @ 4 A max, -20 to 60 °C.
- price: not on page. bib-claim (unverified): "price on request (~$4-5k class)".
- open-hardware: no. SDK: unitree_sdk2 (Apache-style prebuilt static lib; README gives build only). At commit c7538298 the example tree has `example/g1/dex3/` and no Dex5 example, and the md lists "Config files (0)", "Python signatures ... (0 files)". Nothing in the repo confirms Dex5 support.
- release status / date: listed for sale on the vendor site under "Components" and "Dexterous Hand" with a "Store / Cooperate" link, i.e. sold as a separate component. No ship date on page; bib-claim: "shipping 2025". Compatibility with G1/H1-2/H2 (bib "why") is not stated on the page beyond both appearing in the site menu.
- demonstrated vs specified: everything above is from the spec table; the page has no task videos or demonstrations.
- used by (grep dex5|dex-5 over code/md, papers/md): gr_dexter_2025 (reference [58] to the Dex5-1 URL), zhao_dexhand_survey_2026 (comparison-table row for Dex5-1P), welte_iil_survey_2025 (table row: 16/20 DoF, "mechanical", 10 N, 1.0 kg). No repo in code/md drives the hand.

## Setting / Method / Evaluation
Not applicable: vendor page, no task, reward, or evaluation. The page's RL framing is one sentence: backdrivability "Eliminates 'stiff hands', making operations smoother and more convenient for reinforcement learning(RL) training."

## Limitations stated by the vendor
Footnotes [1]-[4]: size is flat-state; fingertip force depends on scenario; "The above parameters may vary in different scenarios and configurations"; appearance subject to change.

## Quotable claims (verbatim)
- "20 Degrees of freedom (16 active+4)" (hero)
- "94 tactile sensors per hand; supports secondary development of tactile algorithms for dexterous hands" (hero; P variant only per spec table)
- "The rotation axis of joint is closer to the surface, with ultra-small joint gaps." (design section)

## Notes for the survey
- Feeds the commercial-hand table (tendonless in-joint geared design, 1 kHz USB, per-joint stiffness/damping command). Tactile count 94 is only on the P variant; Dex5-1 has zero.
- The 16-vs-20 split matters when other notes quote "20 DoF": four are coupled distal joints.
- Weight 1100 g vs welte table 1.0 kg: welte rounds; page says 1100 g.
- The two survey rows disagree on actuation label ("mechanical" vs "DIT"); the page supports neither word.
