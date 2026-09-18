# tesla_optimus_hand_2025 — Tesla Optimus hands: Gen 2 (2023) and V3 (patents 2025-2026) (Tesla, company announcement and USPTO patents, unreleased)

SOURCE THIN (partial): the USPTO patent PDF section is empty (header only, no text extracted) and the Wikipedia page returned HTTP 404. On disk: a Not a Tesla App article on the Gen 2 video (Dec 13 2023) and a Teslarati article on the V3 patents (tweets dated Apr 16 2026). Everything below about the patents is Teslarati's paraphrase, not patent text.

sources: papers/md/tesla_optimus_hand_2025.md [0797707b, sha256 of the parsed page; no manifest entry, fetched 2026-09-17] ; no code
source: press articles about a video and about patents; all figures are claims, none measured.

## One-line contribution
Two announced, unreleased generations: Gen 2 (Dec 2023) with "11-DoF brand-new hands" and fingertip tactile shown in a 1:43 video, and V3 with forearm actuators driving each finger by three tendons through a crosstalk-managing wrist, described in patents filed Oct 2024.

## Setting
- hand(s): Optimus Gen 2 hand; Optimus V3 hand (Teslarati; bib calls it Gen 3 / V3). Tesla, USA. Never sold separately; no availability stated.
- simulator / observation / action: nothing in either article

## Hand record (article unless marked; bib-claim = from `specs`, not on disk)
- maker / country: Tesla, USA
- DoF: Gen 2 "11-DoF" (video caption list, Dec 13 2023). V3 "Each finger features four degrees of freedom (DoF), while the wrist adds two more"; "The 22-DoF architecture" (Teslarati's own phrase, not attributed to the patent). Per-hand total with 5 fingers x 4 = 20 + 2 wrist = 22 is the article's arithmetic, not stated as such. actuated DoF: not stated. bib-claim: ~50 actuators per arm-hand
- actuation: Gen 2 "Tesla-designed actuators & sensors", in-hand (bib-claim; article does not locate them). V3 tendon: "Actuators are positioned in the forearm rather than the hand"; "Three thin, flexible control cables (tendons) per finger extend from the forearm actuators, pass through the wrist, and connect to the finger segments"
- fingers: 5 implied ("all fingers"); count not stated
- thumb design: not stated
- weight / fingertip force: not stated
- tactile sensing: Gen 2 "Tactile sensing on all fingers"; egg demo "sensors in the fingertips matching where the egg is situated and the force the fingers are using". Type/count not stated. V3: not stated
- control interface and rate: not stated
- price: none; not sold
- open-hardware?: no (patented; three patents named: "Mechanically Actuated Robotic Hand", "Robotic Appendage", "Joint Assembly for Robotic Appendage")
- release status and date: Gen 2 shown Dec 13 2023 (video); V3 patents filed Oct 2024 ("same day as the 'We, Robot' event"), published Apr 2026 (tweets); "Tesla is planning to soon reveal" V3; mid-2025 Musk "struggling" with the hand, early 2026 "overcome the 'hardest' problems". Unreleased. bib-claim: V3 production targeted 2026
- used in corpus: humanoidbench_2024 ("slimmer, human-like hands (e.g., Tesla Optimus, Figure 01)"), zhao_dexhand_survey_2026 ("the 'planetary gearbox + lead screw + tendon' architecture adopted in the Tesla Optimus hand"), an_dexil_survey_2025 (Fig. 3 (k) Tesla Optimus Hand), bai_unified_manip_survey_2025 (Optimus Gen 2 listed), welte_iil_survey_2025 (Tesla "actively developing proprietary robotic hands"), proception_prohand_2026 (lawsuit against an ex-Optimus engineer), boston_dynamics_atlas_hand_2026. egomimic_2024 matches "Optimus codebase" (a software library), not the hand.

## Method
- n/a. V3 mechanism (Teslarati): tendons routed "behind some joints and forward of others" in phalanx channels for independent bending; wrist transition from "a lateral stack on the forearm side to a vertical stack on the hand side" to cut "cable stretch, torque, friction, and crosstalk during combined yaw and pitch"; joint assembly with "curved contact surfaces ... paired with a composite flexible member".

## Evaluation
- demonstrated in video: Gen 2 egg pick-up with fingertip force visualisation (Dec 2023). No task numbers.
- specified in a datasheet: nothing; V3 exists only as patent drawings and an announced reveal.

## Limitations stated by the authors
Musk (via Teslarati): the hand is "the majority of the engineering difficulty of the entire robot", "about 60 percent of the overall Optimus challenge", with no existing supply chain for the precision parts.

## Quotable claims (verbatim, with section)
- "Faster, 11-DoF brand-new hands" / "Tactile sensing on all fingers" (Not a Tesla App, video feature list)
- "Actuators are positioned in the forearm rather than the hand. Each finger features four degrees of freedom (DoF), while the wrist adds two more." (Teslarati, "Core Tendon-Driven Hand Architecture")

## Notes for the survey
- Feeds the "forearm is the hand" / remote tendon actuation trend alongside 1X (onex_neo_hand_2026); contrast with in-hand actuation (XHAND1, Revo 2). zhao_dexhand_survey_2026 attributes a gearbox+lead-screw+tendon architecture to "the Optimus hand" without generation; do not merge with the V3 patent description.
- The 22-DoF and 50-actuator numbers are press/bib figures; cite as "reported", never as spec.
