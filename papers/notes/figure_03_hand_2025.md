# figure_03_hand_2025 — Figure 03 hands (Figure AI, company announcement 2025, unreleased)

SOURCE THIN: the launch page (figure.ai/news/introducing-figure-03) returned HTTP 404. The only source on disk is a third-party tracker page (humanoid.guide/product/figure-03/) for the whole robot. None of the bib `specs` for the hand — 16 DoF per hand, ~3 g fingertip sensitivity, soft palm, announced Oct 9 2025 — appear on the tracker page; they are unverified bib-claims. The tracker's own hand figure ("Degrees of freedom, hands | 20") disagrees with the bib's 16.

sources: papers/md/figure_03_hand_2025.md [c62cebad, sha256 of the parsed page; no manifest entry, fetched 2026-09-17] ; no code
source: third-party tracker page; robot-level manufacturer claims relayed by a tracker, not measurements.

## One-line contribution
Figure 03's hands are known here only through a tracker row: palm cameras in each hand, 200 Hz low-level control, and a robot-level "20" hand DoF / "10" fingers entry whose per-hand split is not given.

## Setting
- hand(s): Figure 03 hands, Figure AI, US ("Nationality | US"); "Availability | Prototype"; not sold separately (tracker lists the robot at "130 000 USD", with "Inquire about price")
- simulator / observation / action: nothing hand-specific; robot: "Helix runs entirely on-board on dual low-power embedded GPUs"; "200 Hz low-level control"

## Hand record (tracker unless marked; bib-claim = from `specs`, not on disk)
- maker / country: Figure AI, USA
- DoF: tracker "Degrees of freedom, hands | 20" and "Number of fingers | 10" — both read as totals for two hands (10 per hand? 5 fingers per hand), but the page does not say per-hand. bib-claim: 16 DoF per hand (bib itself labels this third-party reported). actuated DoF: not stated
- actuation: not stated for the hand. Robot rows: "Motor tech | Frameless BLDC-motors", "Gear tech | Strain-wave (harmonic) and/or cycloidal"
- fingers: 10 total (tracker); 5 per hand implied
- thumb design: not stated
- weight / fingertip force: not stated (robot 60 kg, "Strength [kg] | 20")
- tactile sensing: not stated on page. bib-claim: fingertip pads detecting ~3 g. In-hand vision: "palm cameras in each hand" ("Camera resolution" row: "2x frame rate, 1/4 latency, and +60% FoV per camera, plus palm cameras in each hand")
- control interface and rate: "200 Hz low-level control" (robot-level; "Latency glass to action" row says no numeric glass-to-action latency published)
- price: hand none; robot 130,000 USD (tracker figure)
- open-hardware?: no
- release status and date: "Prototype"; no date on page. bib-claim: announced Oct 9 2025, unreleased to third parties
- used in corpus: helix_2025 (site navigation "FIGURE 03" only), humanoidbench_2024 ("Tesla Optimus, Figure 01" as slim-hand trend), bai_unified_manip_survey_2025 (Figure 02 listed), welte_iil_survey_2025 ("Figure AI, 1X, and Tesla ... actively developing proprietary robotic hands"), daxo_muscle_v0_2025 (news sidebar on a Figure deployment), boston_dynamics_atlas_hand_2026 (contrast mention)

## Method
- n/a. Robot-level: Helix VLA, "Ubuntu Linux (LTS) + RT-komponenter" (sic), 10 Gbps mmWave offload, inductive charging; F.03 battery ~5 h, 2 kW charging; BotQ "up to 12,000 humanoid robots per year".

## Evaluation
- demonstrated in video: nothing on this page.
- specified in a datasheet: nothing hand-specific beyond the rows above.

## Limitations stated by the authors
None (tracker: "Verified | Not verified"; "Safe with humans | Not specified").

## Quotable claims (verbatim, with section)
- "03 introduces a new vision system with 2x frame rate, 1/4 latency, and +60% FoV per camera, plus palm cameras in each hand." (Specifications, Camera resolution)
- "Degrees of freedom, hands | 20" ; "Number of fingers | 10" (Specifications)

## Notes for the survey
- Hardware table: keep the hand DoF cell as "16 (bib, third-party) / 20 total (tracker)" until the launch page is fetched; do not quote 3 g or a palm-camera latency as spec.
- The palm camera is the one design fact both bib and page agree on; it belongs in the in-hand sensing section as vision, not tactile.
