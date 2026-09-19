# Outreach note — unidexgrasp_2023

## Paper
**UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and
Goal-Conditioned Policy**
Xu et al. — CVPR 2023 (arXiv 2303.00938)
Code: https://github.com/PKU-EPIC/UniDexGrasp

## The claim

Sec. 3.3.1 (Eq. 10, recovered by OCR where the layout parse dropped the typeset equations) states
the execution-stage reward is a four-term additive sum, `r = r_goal + r_reach + r_lift + r_move`,
weighted by seven named ω-coefficients listed in Table 7 (ω_g,q=0.1, ω_g,t=0.6, ω_g,R=0.1,
ω_r=0.5, ω_l=0.1, ω_m=2, ω_b=10). The released `compute_hand_reward` (goal-conditioned branch,
`shadow_hand_grasp.py`) instead computes the reward as a set of nested `torch.where` gates on
distance and flag thresholds, with hardcoded literal coefficients (−0.5, −1.0, 0.9, 2, 0.1, 0.2,
0.05, 10, 0.6/0.04/0.1) that do not map one-to-one onto Table 7's named ω-weights. The config keys
that are passed into the function (`dist_reward_scale: 20`, `rot_reward_scale: 1.0`,
`action_penalty_scale: -0.0002`) do not appear to be used inside the goal-conditioned branch we
were able to read.

## Evidence

- **Code:** `code/md/unidexgrasp_2023.md`, `dexgrasp_policy/dexgrasp/tasks/shadow_hand_grasp.py`
  (file header at code/md line 2712), function `compute_hand_reward`, goal-conditioned branch
  (`if goal_cond:` at code/md line 2780; the second `compute_hand_reward` definition at code/md
  line 2953 with the same `goal_cond` parameter at line 2961).
- **Paper:** Sec. 3.3.1 (Eqs. 5–10, reward formulas) and Table 7 (ω-weight values).
- **Commit:** `36c9bfcf7cedc987dd15e2384c548e51d5aadc21` (`corpus/code_manifest.json`,
  PKU-EPIC/UniDexGrasp).
- **Note:** `papers/notes/unidexgrasp_2023.md`, "Reward / objective block."

We note for completeness that the paper's four-term structure and the code's threshold-gated
structure are not necessarily inconsistent in spirit — both give a large reward once several
sub-goals (finger contact, lift, target position) are jointly satisfied — but the specific
coefficients in Table 7 do not appear as literals anywhere in the reward function we read, so a
reader trying to reproduce Table 7's reward from the paper alone would not arrive at the code's
actual formula.

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (the "Weights drift" paragraph):

> "UniDexGrasp \cite{unidexgrasp_2023} and DexPoint \cite{dexpoint_2022} ship rewards structured
> differently from their equations."

From `tex/sections/appendix_c_rewards.tex`:

> "UniDexGrasp (high). The paper describes a four-term weighted reward (r_goal + r_reach + r_lift +
> r_move via Table 7's omega weights) but the released compute_hand_reward implements a different
> threshold-gated torch.where cascade with distinct hardcoded coefficients that do not map
> one-to-one onto the paper's weights."

## Questions for the authors

1. Is our reading of the goal-conditioned branch of `compute_hand_reward` correct — that its
   literal coefficients do not correspond one-to-one to Table 7's ω_g,q/ω_g,t/ω_g,R/ω_r/ω_l/ω_m/ω_b
   weights?
2. Is there a reason the released reward function is structured differently from Sec. 3.3.1's
   equations — for example, does Table 7 describe an earlier, non-goal-conditioned reward, or was
   the released function refactored for efficiency in a way that changed its literal form without
   changing its intended shaping?
3. Would you like the wording of this claim, as it appears in Section V and the appendix, changed
   in any way before we publish?
