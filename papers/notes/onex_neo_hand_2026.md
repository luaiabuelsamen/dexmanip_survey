# onex_neo_hand_2026 — NEO's Hands: An API to the Physical World (1X Technologies, company announcement, Jul 9 2026)

sources: papers/md/onex_neo_hand_2026.md [6e97aa36, sha256 of the parsed page; no manifest entry, fetched 2026-09-17 from 1x.tech/discover/neos-hands] ; no code
source: vendor page (dated "JUL 09 '26"); specs are manufacturer claims, not measurements. Bib marks this entry verified.

## One-line contribution
A 25-DoF (22 finger/palm + 3 wrist) hand driven by low-ratio (~5:1-15:1) quasi-direct-drive tendons from forearm motors, claimed fully backdrivable and force-controlled on every joint, with normal/shear/contact-location skin, IP68, and a stated 10,000-hands/yr line; ships only on the NEO humanoid.

## Setting
- hand(s): NEO hand, 1X Technologies; country not stated on page; "These are the hands that will ship on every NEO" — not sold separately (the site's Order link is for NEO)
- simulator / physics: none
- observation: joint force via backdrivable transmission ("The joints are sensors"), proprioception ("every joint is closed-loop"), skin: normal force, contact location, shear
- action space: "natively force-controlled"; rate not stated

## Hand record (page unless marked)
- maker / country: 1X Technologies; country not stated on page
- DoF: 25; actuated DoF: 25 ("All 25 degrees of freedom (22 fully actuated DoF in the fingers and palm, plus 3 at the wrist) are natively force-controlled and fully backdrivable")
- actuation: tendon, "quasi-direct-drive tendons via the 1X Tendon Drive at low gear ratios of approximately 5:1 to 15:1"; "The motors live in the forearm ... pulling proprietary tendons through the wrist"
- fingers: count not stated (demos include "sign language"; DoF "distributed the way anatomy distributes them")
- thumb design: "biased toward a thumb that genuinely opposes"; thumb CMC peak torque 3.5 Nm
- weight: not stated ("lightweight hand")
- fingertip force: "distal flexion forces up to 45N"; finger MCP peak 2.6 Nm; wrist 17.75 Nm; "+/-0.2 mm positioning accuracy"
- tactile sensing: "high-resolution tactile sensing across the fingertips and surfaces, measuring normal force, contact location, and shear"; "Pressure, pressure change, slip — across the whole finger, not just a pad at the tip"; count and technology not stated; skin "co-designed with the sensors inside it"
- control interface and rate: not stated
- price: not stated; not sold separately
- open-hardware?: no ("proprietary tendon systems", in-house motors, electronics, firmware)
- release status and date: announced Jul 9 2026; "hundreds of these hands have already come off a scalable production line"; "capacity to produce 10,000 hands this year"; wrist joints "proven reliable well beyond 2 million cycles under high loads"; IP68, food-safe
- used in corpus: bai_unified_manip_survey_2025 ("1X NEO" listed among humanoids), welte_iil_survey_2025 ("Figure AI, 1X, and Tesla ... actively developing proprietary robotic hands"). No paper or repo in the corpus uses the hand.

## Method
- n/a. Design argument: high-ratio (100:1-200:1) hands are "write-only"; low ratios give "force transparency" so contact forces reach the motor; low distal inertia lets impacts backdrive the fingers (safety).

## Evaluation
- demonstrated in video (page lists as capabilities; "Visualizations show", "Slow-motion footage shows"): LEGO assembly, screws and coins from a wallet, light bulbs, screwdriver, in-hand rotation, zipping a jacket, sorting grapes, pouring tea, catching a ball, USB-C plug, wine glass, wiping, sign language; contact-normal and pressure heatmaps on handshakes and origami; yielding when slapped, hammered, pinched in a drawer. No success rates, trial counts or task definitions.
- specified in a datasheet: DoF, gear ratio range, torques, 45 N, +/-0.2 mm, IP68, >2M wrist cycles, production numbers — all as page prose, no datasheet.

## Limitations stated by the authors
None stated. The page frames the remaining gap as data: "make data the only barrier to capabilities".

## Quotable claims (verbatim, with section)
- "it runs quasi-direct-drive tendons via the 1X Tendon Drive at low gear ratios of approximately 5:1 to 15:1. All 25 degrees of freedom (22 fully actuated DoF in the fingers and palm, plus 3 at the wrist) are natively force-controlled and fully backdrivable." ("The joints are sensors")
- "Peak torques reach 3.5 Nm at the thumb CMC and 2.6 Nm at the finger MCP joints, with distal flexion forces up to 45N. The wrist delivers 17.75 Nm of torque." ("Twenty-five ways to ask a question")
- "This gives us the capacity to produce 10,000 hands this year." ("The hardware behind the instrument")

## Notes for the survey
- Hardware table: highest actuated-DoF count among the commercial/humanoid hands here; the forearm-tendon/low-ratio design pairs with Tesla V3 (tesla_optimus_hand_2025) as the "forearm is the hand" trend, and contrasts with hydraulic Sanctuary (sanctuary_phoenix_hand_2024).
- Every capability is a demo claim; nothing is benchmarked. Weight and tactile count are the two spec gaps.
