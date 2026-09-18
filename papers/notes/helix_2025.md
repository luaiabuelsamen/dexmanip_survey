# helix_2025 — Helix: A Vision-Language-Action Model for Generalist Humanoid Control (Figure AI, company blog, Feb 20 2025)

sources: papers/md/helix_2025.md [sha256 37736bd6] ; no code

source: vendor page (company blog post), fetched successfully (193 lines, full text present); specs and results below are manufacturer claims, not independent measurements.

## One-line contribution
Figure claims a "System 2 / System 1" VLA (7B-param VLM + 80M-param cross-attention transformer) that outputs continuous 35-DoF whole-upper-body control (wrists, torso, head, and individual fingers) at 200 Hz on two Figure humanoids simultaneously, trained end-to-end on ~500 hours of teleoperated data, running entirely onboard embedded GPUs.

## Setting (as stated)
- hand(s): not named — the page never gives a model, vendor, or DoF count for the hand itself. It states robot state input is "wrist pose and finger positions" and the action output includes "finger flexion and abduction control," but the hand is only ever "Figure robots equipped with Helix" — Figure's own in-house humanoid hardware (Figure 02/03), not a named/spec'd product.
- arm/embodiment: Figure humanoid, full upper body (wrists, torso, head) plus fingers; bimanual by construction (two arms on one robot) and additionally multi-robot ("simultaneously on two robots").
- simulator / physics: none for evaluation — S1's vision backbone is "initialized from pretraining done entirely in simulation," but no sim engine, timestep, or env count is named.
- observation: monocular robot camera image + robot state (wrist pose, finger positions) + language command, fed to both S2 (7-9 Hz) and S1 (200 Hz).
- action space: continuous, 35-DoF (wrist poses, finger flexion/abduction, torso, head orientation) plus a synthetic "percentage task completion" action; no tokenization.
- data: "~500 hours" of multi-robot, multi-operator teleoperated data, auto-labeled with hindsight language instructions by a VLM; "All items handled during training are excluded from evaluations."

## Method
- paradigm: VLA, dual-system ("System 1, System 2"), trained end-to-end with a "standard regression loss" (loss terms, weights, or equation not given — no formula, no reward/loss quoted beyond "standard regression loss").
- S2: 7B-parameter open-source, open-weight VLM (unnamed), 7-9 Hz, produces a single continuous latent conditioning vector.
- S1: 80M-parameter cross-attention encoder-decoder transformer, 200 Hz, convolutional multi-scale vision backbone, consumes S2's latent plus its own higher-rate image/state inputs.
- key trick: training-time temporal offset between S1 and S2 inputs calibrated to match deployed inference latency ("minimizing the train-inference distribution gap").
- key trick: single set of weights, no per-task fine-tuning or separate action heads.

## Evaluation
- metrics: **none quantified.** No success rate, no trial count, no benchmark table, no comparison numbers anywhere on the page.
- headline claims are qualitative only: "successfully handled thousands of novel items in clutter... without any prior demonstrations" (no count of trials or failures given for "systematic testing"); "achieves strong object generalization"; multi-robot grocery-collaboration and handover demonstrated in video only.
- baselines beaten: none numerically; the page only claims Helix "matches the speed of specialized single-task behavioral cloning policies" and requires "<5%" the data of "previously collected VLA datasets," with no dataset named or size given for the comparison.
- real robot: yes, Figure's own humanoid(s); no trial count or success rate given anywhere.

## Reviewer questions, answered directly

**1. Does the page state a number of actuated DoF for the hand, and is it per hand?**
No. The only DoF number on the page is for the whole upper body, not the hand alone: "Helix coordinates a 35-DoF action space at 200Hz, controlling everything from individual finger movements to end-effector trajectories, head gaze, and torso posture." (Results, "Fine-grained VLA whole upper body control") 35 DoF spans wrists + torso + head + both hands' fingers combined — it is not a per-hand finger-DoF count, and no separate hand DoF number appears anywhere.

**2. Does it report any success rate, trial count, or quantitative evaluation at all?**
No. There is no percentage, fraction, or trial count on the page for any task. The closest the page comes is "In systematic testing, the robots successfully handled thousands of novel items in clutter... without any prior demonstrations or custom programming" — "thousands of items" describes the object pool attempted, not a success count or rate out of that pool.

**3. Does it state the training data quantity and the policy architecture?**
Yes, both. Data: "We collect a high quality, multi-robot, multi-operator dataset of diverse teleoperated behaviors, ~500 hours in total." Architecture: "S2 is built on a 7B-parameter open-source, open-weight VLM... S1, an 80M parameter cross-attention encoder-decoder transformer, handles low-level control."

**4. Is the hand it runs on available to anyone outside the company?**
Not stated as available. The page never names the hand as a product, gives it a model number, or says it is sold, licensed, or open-sourced; it is only ever referred to as part of "Figure robots equipped with Helix" — Figure's own proprietary humanoid platform. Nothing on the page indicates third-party access to this hand.

## Quotable claims (verbatim)
- "Helix coordinates a 35-DoF action space at 200Hz, controlling everything from individual finger movements to end-effector trajectories, head gaze, and torso posture." (Results)
- "We collect a high quality, multi-robot, multi-operator dataset of diverse teleoperated behaviors, ~500 hours in total." (Model and Training Details, Data)
- "S1, an 80M parameter cross-attention encoder-decoder transformer, handles low-level control." (Model and Training Details, Architecture)
- "In systematic testing, the robots successfully handled thousands of novel items in clutter... without any prior demonstrations or custom programming." (Results, "Emergent 'Pick up anything'")

## Notes for the survey
Helix is announcement-grade evidence, not measurement-grade: it names a 35-DoF whole-body action space that includes individual-finger control on Figure's own (unnamed, unspec'd) hand, but gives no per-hand DoF count, no success rate, no trial count, and no comparison table — every "first" claim on the page is qualitative. This does not settle the DoF or numeric-evidence side of a counterexample to "no company-announced hand appears in any corpus method work" — see corpus/rows/helix_2025.json `dexterous_hand_evaluated` and `dexterous_evidence` for the row-level call, and the survey text should distinguish "Figure's hand does individual-finger control per this announcement" (true, per the page) from "with quantified evidence" (false — none given).
