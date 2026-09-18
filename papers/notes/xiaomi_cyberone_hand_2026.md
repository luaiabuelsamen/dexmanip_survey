# xiaomi_cyberone_hand_2026 — Xiaomi next-gen CyberOne bionic hand (Xiaomi, company announcement, unreleased)

sources: papers/md/xiaomi_cyberone_hand_2026.md [sha256 2130b324; no manifest entry, hash computed from file] ; no code
source: press. The 36kr page (eu.36kr.com/en/p/3947315943472512) fetched EMPTY (navigation and footer only, no article body). The usable source is Interesting Engineering, "CyberOne humanoid robot's hand mimics human sweat glands for thermal management", Atharva Gosavi, Mar 30, 2026, which relays a post on "Xiaomi Technology's official WeChat account". Specs are second-hand vendor claims, not measurements. bib entry marked verified: false.

## Hand block (from the IE article)
- maker / country: Xiaomi / China
- DoF: NOT given as a number. The article says the redesign "increases active degrees of freedom by 83 percent, bringing the robot's bionic hand closer to the human hand standard of roughly 22 to 27 degrees of freedom". The "22-27" in the bib title is the article's figure for the human hand, not the robot's spec.
- actuated DoF: not stated (only "+83 percent" active DoF vs the previous version)
- actuation: motors in the hand ("the hand's compact motors can generate significant heat"; "3D-printed metal liquid cooling channels inside the hand"). No tendon/linkage statement; the article contrasts the 150,000-cycle result with "the roughly 10,000-cycle failure threshold commonly seen in tendon-driven robotic hands", which implies but does not state a non-tendon design. bib "forearm actuation" is not in the article.
- fingers: not stated (a "full-palm tactile bionic hand")
- thumb design: not described
- weight: not stated. Size: "reducing the hand's volume by 60 percent to achieve a 1:1 human scale", "based on a 1.73-meter (5.6 feet) human hand model"
- fingertip force: not stated
- tactile sensing: "full-palm tactile sensing", area "around 8,200 square millimeters", detects "pressure and contact across the entire palm rather than just the fingertips"; taxel count and type not stated
- control interface / rate: not stated
- price: none; not a product
- open-hardware: no. Software/data: "open-sourced the TacRefineNet framework along with 61 hours of raw tactile data", collected with "tactile gloves for direct data collection"
- release status / date: unreleased; part of the CyberOne humanoid; not buyable separately. Article date Mar 30, 2026.
- demonstrated vs specified: no datasheet. Reported test results (vendor-run, relayed): ">150,000 grasping cycles"; automotive assembly "90.2 percent success rate for nut-fastening tasks within a strict 76-second factory cycle over three hours of operation".
- used by (grep cyberone over code/md, papers/md): none besides this entry (the "xiaomi" hit in arctic_2022 is unrelated).

## bib `specs` claims NOT confirmed by the fetched source (unverified)
"Unveiled at WRC Aug 19 2026 after four months on Xiaomi's car line"; "64% more DoF" (article: 83 %); "33 DoF across both hands (66 whole body)"; "22-27 DoF per hand"; "forearm actuation ... evaporative heat dissipation"; "98% success on self-tapping nut installation" (article: 90.2 %). These may come from the empty 36kr article; they cannot be checked here.

## Setting / Method / Evaluation
Only the relayed factory test above: task nut fastening, cycle 76 s, duration 3 h, success 90.2 %. No trial count, no definition of success.

## Quotable claims (verbatim, IE)
- "the company integrated 3D-printed metal liquid cooling channels inside the hand that function similarly to sweat glands"
- "the hand surviving more than 150,000 grasping cycles"

## Notes for the survey
- Thermal management as a hand-design axis (liquid-cooled in-hand motors) is unique in this corpus; cite with the second-hand caveat.
- Two headline numbers in the bib (DoF gain, nut success) disagree with the only readable source; the note carries the article's values. Re-fetch 36kr before quoting either.
