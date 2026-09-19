# Outreach note — dextreme_2022

**A caution before the claim:** this row bundles two different kinds of finding. The first three
items below (action-delta weight, joint-velocity formula, `timeout_rew`) are genuine paper-vs-code
disagreements. The fourth item (learning rate / KL threshold) is, on closer reading, the paper's
own appendix table disagreeing with its own body text — the code agrees with the body text in both
cases. We are sending all four because all four are true statements worth the authors' eyes, but we
have written the letter so it does not misrepresent the fourth as a code-vs-paper contradiction.

## Paper
**DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality**
Handa et al. — ICRA 2023 (arXiv 2210.13702)
Code: https://github.com/isaac-sim/IsaacGymEnvs

## The claim

Table 2 states the Action Delta Penalty weight is −0.25. The released
`AllegroHandDextremeADR.yaml` sets `actionDeltaPenaltyScale: -0.2`, and
`AllegroHandDextremeManualDR.yaml` sets it to `-0.01`; neither shipped configuration matches the
paper's table. Separately, the paper's Joint Velocity Penalty formula is `||v_joints||²` with
weight −0.003, but the code computes `velocity_penalty_coef * sum((hand_dof_vel / (max_velocity −
vel_tolerance))**2)` with `velocity_penalty_coef = -0.05` and a first normalization by 4.0 rad/s
that is not stated in the paper's table (the two land at a numerically similar effective
coefficient, but by a route the table does not describe). The code also computes a `timeout_rew`
term with no row in the paper's Table 2 (it evaluates to zero given `fallPenalty: 0.0` in both
shipped configs, so it is numerically inert but structurally present and unlisted).

Separately, and not a code discrepancy: Appendix Table 12 states critic learning rate 5e-4 and KL
threshold 0.16; the paper's own Sec. 2.3 body text says 5e-5 and 0.016, and the code
(`central_value_config.learning_rate: 5e-5`, `central_value_config.kl_threshold: 0.016`) matches
the body text, not the appendix table.

## Evidence

- **Code:** `code/md/dextreme_2022.md`, function `compute_hand_reward`,
  `isaacgymenvs/tasks/dextreme/allegro_hand_dextreme.py` (definition at code/md line 7688,
  `timeout_rew` at line 7741, summed into the return at line 7744).
- **Config:** `isaacgymenvs/cfg/task/AllegroHandDextremeADR.yaml` (code/md line 903,
  `actionDeltaPenaltyScale: -0.2` at code/md line 986) and `AllegroHandDextremeManualDR.yaml`
  (code/md line 1146, `actionDeltaPenaltyScale: -0.01` at code/md lines 1233/1464).
- **Paper:** Table 2 (reward terms) and Appendix Table 12 vs. Sec. 2.3 body text (learning rate,
  KL threshold).
- **Commit:** `aeed298638a1f7b5421b38f5f3cc2d1079b6d9c3` (`corpus/code_manifest.json`,
  isaac-sim/IsaacGymEnvs).
- **Note:** `papers/notes/dextreme_2022.md`, section "Reward / objective block," and
  "Reproducibility (F)," internal-inconsistency paragraphs.

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (the "Weights drift" paragraph):

> "Weights drift. DeXtreme \cite{dextreme_2022} states an action-delta penalty of $-0.25$ in
> Table~2 and ships $-0.2$ and $-0.01$ in its two DR yamls, neither matching."

From the same section, the zeroed-terms paragraph:

> "DeXtreme \cite{dextreme_2022}'s \texttt{timeout\_rew} and DexPBT \cite{dexpbt_2023}'s fall
> penalty through \texttt{fallPenalty: 0.0}, and PenSpin \cite{penspin_2024}'s
> \texttt{action\_penalty\_scale: 0.0}."

From `tex/sections/appendix_c_rewards.tex`:

> "DeXtreme (high). Action Delta Penalty weight is -0.25 in paper Table 2 but -0.2 in the ADR yaml
> and -0.01 in the ManualDR yaml; the Joint Velocity Penalty in code normalises velocity by
> (max_velocity-vel_tolerance) unlike the paper's stated formula; code has a timeout_rew term
> absent from the paper's reward table; Appendix Table 12 states critic learning rate 5e-4 and KL
> threshold 0.16, vs body text/code values of 5e-5 and 0.016."

## Questions for the authors

1. Is our reading correct — that neither shipped YAML (`AllegroHandDextremeADR.yaml`,
   `AllegroHandDextremeManualDR.yaml`) reproduces Table 2's −0.25 action-delta weight, and that the
   released joint-velocity formula normalizes by a 4.0 rad/s term the table does not mention?
2. Is there a reason the released configurations differ from Table 2 (for example, values tuned
   after the paper's numbers were produced, or Table 2 describing an earlier run)? And can you
   confirm which of 5e-4/0.16 (appendix) or 5e-5/0.016 (body text) is the value actually used to
   produce the paper's reported results?
3. Would you like the wording of this claim, as it appears in Section V and the appendix, changed
   in any way before we publish?
