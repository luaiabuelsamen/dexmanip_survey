# paxini_dexh13_2024 — PaXini DexH13 tactile dexterous hand (PaXini Tech; commercial product)

SOURCE THIN: the product page https://humanoid.guide/product/dexh13/ returned HTTP 503. The only text on disk is a PR Newswire press release (CES 2026, Jan 7 2026), which names the hand once and gives no mechanical specification.

sources: papers/md/paxini_dexh13_2024.md [6b30f177 = sha256 of the md on disk; no corpus/manifest.json entry; pages_manifest fetched 2026-09-17] ; no code
source: vendor press release; specs are manufacturer claims, not measurements.

## One-line contribution
A commercial hand built around PaXini's own multidimensional tactile array ("1,140 ITPU multidimensional tactile processing units"), shown at CES 2026 doing gesture mirroring, grasping and knob turning (press release).

## Hand record (what the press release confirms)
- maker: PaXini Tech. country: China (a related release on the same page is titled "Chinese Robotics Company PaXini Shines at iREX 2025").
- DoF: not stated.
- actuated DoF: not stated.
- actuation: not stated.
- fingers: not stated.
- thumb design: not stated.
- weight: not stated.
- fingertip force: not stated.
- tactile sensing: "Equipped with 1,140 ITPU multidimensional tactile processing units" (press release, "From Perception to Embodied AI Execution"). The underlying sensor family: "PX-6AX-GEN3 multidimensional tactile sensor ... spans three product series and 12 models, achieves <0.5%FS repeatability across the full measurement range, and simultaneously measures 15 sensing dimensions, including six-axis force, material texture, and elastic response" (press release). Whether DexH13 uses GEN3 is not stated.
- control interface and rate: not stated.
- price: not stated.
- open-hardware?: no indication.
- release status and date: demonstrated at CES 2026 (Jan 7 2026, Las Vegas); shipping status not stated.
- used by (grep -l -i "paxini|dexh13", self excluded): linkerbot_l20_2025, welte_iil_survey_2025.

## Unverified bib `specs` (not confirmed by any fetched page)
"4 fingers, 16 DoF (13 active + 3 passive), thumb 4 active, 5 kg load, 8 MP eye-in-hand camera, tactile <0.5% FS repeatability, 3 series / 12 models, shipping 2024-2026." Of these, only "<0.5% FS repeatability" and "3 series / 12 models" appear in the press release, and there they describe the PX-6AX-GEN3 sensor line, not the hand.

## Setting
- Demo tasks (press release): "accurately mirror a wide range of human hand gestures", "stable grasping of irregular objects—from test tubes to cubes", "delicate tasks like knob turning". Shown on the TORA-ONE humanoid making ice cream (lever, ingredients, cup handover).

## Method / Evaluation
None reported. Also announced: PX6D/PXTS Hall-effect 6-D F/T sensor, an "omni-modality" human-centric data acquisition system, and a claim of "nearly 200 million omni-modality data entries annually".

## Quotable claims (verbatim)
- "Equipped with 1,140 ITPU multidimensional tactile processing units, the DexH13 was able to accurately mirror a wide range of human hand gestures" (press release)

## Notes for the survey
- Cannot enter the hand-spec table until the product page or a datasheet is fetched; refetch https://humanoid.guide/product/dexh13/ or PaXini's own site. Quote only the 1,140-unit tactile count, labelled as a press-release claim.
