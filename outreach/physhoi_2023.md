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

Quoted from the paper as it stands today, so that what you are being asked about is the
wording that would actually appear. Only the sentences naming your work are reproduced;
citation markers are replaced with the short name of the work cited.

From Section V, *Training*:

> PhysHOI is the origin of the reward form. It multiplies a body term, an object term, an
> interaction-graph term and a contact-graph term, and reaches 95.4 percent success on GRAB
> against 27.0 percent for a DeepMimic baseline. The contact-graph term exists to stop the
> policy learning not to touch the object.

> PhysHOI is the clearest example. Its paper assigns nonzero weights to object rotation and
> rotation velocity on the GRAB dataset. In the public implementation, both errors are set to
> zero and the calculations are commented out. The paper does specify zero weights for the
> separate BallPlay task, but the implementation does not condition this choice on the
> dataset. Its reported success criterion uses position alone, so that score cannot expose the
> difference. The claim here is limited to this conflict between the paper and the public
> revision listed in Table III; it does not establish which code produced the published
> experiments.

From Appendix C, the per-paper entry:

> PhysHOI (high). The released compute_humanoid_reward sets the body position-velocity error
> and the object rotation and rotation-velocity errors to zeros_like, unconditionally, with
> the computation that would produce them commented out on the same lines, while Table 4 lists
> nonzero lambda^or=0.1/lambda^orv=0.01 weights for GRAB: in that file the object's
> orientation error is the constant zero and those weights cannot change the reward.
>
> Artefact: `wyhuai/PhysHOI` at `6095c605e2`, `physhoi/env/tasks/physhoi.py`
> (`compute_humanoid_reward`).

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
