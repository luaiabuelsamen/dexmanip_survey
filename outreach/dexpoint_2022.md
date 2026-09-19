# Outreach note — dexpoint_2022

## Paper
**DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous
Manipulation**
Qin et al. — CoRL 2022 (arXiv 2211.09423)
Code: https://github.com/yzqin/dexpoint-release

## The claim

The paper states the reward is a four-term sum (Eq. 5, Sec. 3.1): `R = w_reach·r_reach +
w_contact·r_contact + w_lift·r_lift + w_penalty·r_penalty`, with a plain distance-based `r_reach`
and `r_lift = h_current − h_init`. The released `AllegroRelocateRLEnv.get_reward` in
`relocate_env.py` computes a materially different function: an inverse-distance shaping term
`1.0 / (0.06 + finger_object_dist)` in place of the plain reach distance, a clipped lift term
`10 * clip(object_lift, 0, 0.2)` rather than the height-difference formula, and three terms with no
counterpart in Eq. 5 at all — a `+1` bonus once lift exceeds 2 cm, a target-distance term `1.0 /
(0.04 + target_obj_dist)`, a rotation bonus `4.0 / (0.4 + theta) * rotation_reward_weight`, and an
IK-tracking penalty `controller_penalty = -1e3 * cartesian_error**2`, with the whole sum finally
divided by 10.

## Evidence

- **Code:** `code/md/dexpoint_2022.md`, `dexpoint/env/rl_env/relocate_env.py`, class
  `AllegroRelocateRLEnv` (header at code/md line 273), method `get_reward` (code/md lines
  288–310). The quoted body:
  ```
  finger_object_dist = np.linalg.norm(self.object_in_tip, axis=1, keepdims=False)
  finger_object_dist = np.clip(finger_object_dist, 0.03, 0.8)
  reward = np.sum(1.0 / (0.06 + finger_object_dist) * self.finger_reward_scale)
  ...
  controller_penalty = (self.cartesian_error ** 2) * -1e3
  return (reward + action_penalty + controller_penalty) / 10
  ```
- **Paper:** Sec. 3.1 and Appendix A ("Reward"), Eq. 5.
- **Commit:** `17f1e238bb120d92baabe8207494d48476fea289` (`corpus/code_manifest.json`,
  yzqin/dexpoint-release).
- **Note:** `papers/notes/dexpoint_2022.md`, section "C. Reward / objective block."

One partial match should be recorded alongside the mismatch: the contact bonus (`+0.5` gated on
`is_contact`) and the lift scale (`10 *`) do match `w_contact=0.5` and `w_lift=10` from the paper's
stated weights, once the gating structure is accepted as an implementation of `r_contact` and
`r_lift`.

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (Section V-H, "What the released code says," the "Weights
drift" paragraph):

> "UniDexGrasp \cite{unidexgrasp_2023} and DexPoint \cite{dexpoint_2022} ship rewards structured
> differently from their equations, and PDDM \cite{pddm_2019}'s Baoding reward carries a $-10$
> wrist-height term Table~2 omits."

From `tex/sections/appendix_c_rewards.tex`:

> "DexPoint (high). The released code's reward adds several terms absent from the paper's
> four-term Eq. 5 (a lift-threshold bonus, a target-distance term, a rotation bonus, and an IK
> controller-tracking penalty) and reshapes the reach/lift terms into inverse-distance and clipped
> forms rather than the paper's plain distance/height-difference formulas."

## Questions for the authors

1. Is our reading of `get_reward` in `relocate_env.py` correct — that it implements a reshaped,
   nine-term function rather than the four-term Eq. 5 in the paper?
2. Is there a reason the released training configuration differs from the paper's stated formula
   (for example, a later tuning pass after submission, or a simplification made for the paper's
   presentation)?
3. Would you like the wording of this claim, as it appears in Section V and the appendix, changed
   in any way before we publish?
