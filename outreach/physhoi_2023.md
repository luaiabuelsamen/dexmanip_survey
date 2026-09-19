# Outreach note — physhoi_2023

## Paper
**PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction**
Wang et al. — arXiv 2023 (arXiv 2312.04393)
Code: https://github.com/wyhuai/PhysHOI

## The claim

Table 4 lists nonzero weights for the GRAB dataset's object-rotation reward terms — λ^or = 0.1 and
λ^orv = 0.01 — implying the reward tracks the object's orientation and orientation-velocity, in
addition to its position. The released `compute_humanoid_reward` hardcodes the corresponding
per-step errors, `eor` and `eorv`, to `torch.zeros_like(ep)` unconditionally (the real computation
is present but commented out immediately beside the zeroing line), so `ror` and `rorv` are always
1 regardless of the weight. The body position-velocity error `epv` is hardcoded to zero the same
way. This is not dataset-conditional — the paper does say, explicitly, that λ^or and λ^orv are
zero *for BallPlay* because that dataset provides no ball-rotation ground truth; that stated
exemption does not cover GRAB, where Table 4's weights are nonzero. In the reward that actually
trained the policy, GRAB's object is tracked in position only, while Table 4 states an
orientation-tracking objective.

## Evidence

- **Code:** `code/md/physhoi_2023.md`, `physhoi/env/tasks/physhoi.py`, function
  `compute_humanoid_reward` (definition at code/md line 358; `epv = torch.zeros_like(ep)` at line
  405; `eor = torch.zeros_like(ep) #torch.mean((ref_obj_rot - obj_rot)**2,dim=-1)` at line 422;
  `eorv = torch.zeros_like(ep) #torch.mean((ref_obj_rot_vel - obj_rot_vel)**2,dim=-1)` at line 430
  — the commented-out real computation sits on the same line as the zeroing).
- **Paper:** Sec. 3.6 (reward form, Eq. 2–11, recovered by OCR where the layout parse dropped the
  typeset equations) and Table 4 (App. A.3), GRAB row: `[λ^p, λ^r, λ^pv, λ^rv | λ^op, λ^or, λ^opv,
  λ^orv | λ^ig | λ^cg...] = [50, 20, 0.01, 0.01 | 1, 0.1, 0.01, 0.01 | 20 | 50, 5, 5]`.
- **Commit:** `6095c605e22bd01f78ed356e8b08250edf3c5da6` (`corpus/code_manifest.json`,
  wyhuai/PhysHOI).
- **Note:** `papers/notes/physhoi_2023.md`, reward block, "**Mismatch (important for 'position only
  vs. position+orientation' question)**" paragraph.

This is the row the survey treats as its strongest single case: the discrepancy is a hardcoded,
unconditional zero next to a live commented-out formula, checked against a paper table with
explicit nonzero weights, and it is not one we were able to break under adversarial review.

## What the survey will say in print if you do not reply

From `tex/sections/08_gaps.tex`:

> "PhysHOI \cite{physhoi_2023} survived every attempt to break it. Table 4 weights object rotation
> at 0.1 for GRAB, and the released \texttt{compute\_\allowbreak{}humanoid\_\allowbreak{}reward}
> sets the object rotation and rotation-velocity errors to \texttt{torch.zeros\_\allowbreak{}like},
> unconditionally, so the dataset exemption the paper states does not cover it. The reward behind
> its 95.4 percent tracked the object in position only, and its own position-only success criterion
> could not have caught that."

From `tex/sections/05_training.tex` (Section V-H, called out as "the most consequential case"):

> "The most consequential case is \cite{physhoi_2023}. Its
> \texttt{compute\_\allowbreak{}humanoid\_\allowbreak{}reward} hardcodes the body position-velocity
> error and both object rotation errors to zero, with the real computation commented out beside
> them, and does so unconditionally rather than per dataset, while its Table~4 lists non-zero
> weights of 0.1 and 0.01 for those rotation terms on GRAB. The reward that produced the paper's
> numbers never tracked object orientation: a method presented as tracking a 6-DoF reference was,
> in the code that ran, tracking the object in position only, with body rotation and body
> rotation-velocity still live."

From `tex/sections/05_training.tex`, the Tracking-a-human-reference subsection:

> "PhysHOI \cite{physhoi_2023} is the origin of the reward form. It multiplies a body term, an
> object term, an interaction-graph term and a contact-graph term, and reaches 95.4 percent success
> on GRAB against 27.0 percent for a DeepMimic baseline. The contact-graph term exists to stop the
> policy learning not to touch the object."

From `tex/sections/appendix_c_rewards.tex`:

> "PhysHOI (high). The released code hardcodes the body position-velocity error and the object
> rotation/rotation-velocity errors to zero in compute_humanoid_reward, so despite Table 4 listing
> nonzero λ^or=0.1/λ^orv=0.01 weights for GRAB, the trained reward never actually tracks object
> orientation (position-only in practice)."

## Questions for the authors

1. Is our reading of `compute_humanoid_reward` correct — that `eor` and `eorv` (and `epv`) are
   hardcoded to zero unconditionally, including for the GRAB dataset where Table 4 lists nonzero
   λ^or and λ^orv?
2. Is there a reason the released training code differs from Table 4 for GRAB specifically — for
   example, was orientation tracking found unnecessary or harmful for GRAB after the paper's
   numbers were produced, or is there a different code path (a flag or branch we did not locate)
   that re-enables the real computation for GRAB runs?
3. Would you like the wording of this claim, as it appears in Sections V and VIII and the appendix,
   changed in any way before we publish?
