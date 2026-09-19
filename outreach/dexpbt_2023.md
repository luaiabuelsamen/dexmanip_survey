# Outreach note — dexpbt_2023

**Status note (read first):** the survey's own adversarial review (R3) already withdrew half of
this claim. The row's `paper_code_mismatch` field still contains both halves for the record, but
the running prose in `tex/sections/05_training.tex` and `tex/sections/08_gaps.tex` has been
corrected to print only the surviving half. This letter follows the corrected, printed claim, not
the stale full text — the withdrawn half is disclosed below for transparency but is not part of
what we are asking the authors to confirm.

## Paper
**DexPBT: Scaling up Dexterous Manipulation for Hand-Arm Systems with Population Based Training**
Petrenko et al. — RSS 2023 (arXiv 2305.12127)
Code: https://github.com/NVIDIA-Omniverse/IsaacGymEnvs

## The claim as it will actually appear in print

The paper presents the reward as four mutually exclusive staged terms — r_reach, r_pick, r_targ,
and −r_vel — and states "we apply virtually the same reward function in all scenarios." The
released `compute_kuka_reward` sums eight named components instead of four, and one of them,
`hand_delta_penalty`, is multiplied by zero with the code comment "currently disabled," so it
contributes nothing to training despite existing in the file. The five weights that can be matched
by name between Table II and `AllegroKuka.yaml` (α_reach, α_pick, r_picked, α_targ, r_success) are
present at their stated values — this part of the reward is not in question.

**Withdrawn, for disclosure only:** an earlier draft also charged that the paper reports zero
experiments with domain randomization while the shipped `AllegroKuka.yaml` carries a full DR
schedule behind `randomize: False`. On review, this was found to be the shared IsaacGymEnvs
default, not an undisclosed use of DR, and is consistent with the paper's own statement that
randomization was not used here. That half of the claim will not be sent to you and will not
appear in the survey as an accusation; we mention it only so you can see exactly what changed.

## Evidence

- **Code:** `code/md/dexpbt_2023.md`, function `compute_kuka_reward`, `isaacgymenvs/tasks/allegro_kuka/allegro_kuka_base.py` (module header at code/md line 5881; the reward function itself at lines 6004–6032, with the disabling line `hand_delta_penalty *= self.distance_delta_rew_scale * 0  # currently disabled` at code/md line 6027).
- **Config:** `AllegroKuka.yaml` (`distanceDeltaRewScale: 50.0`, `liftingRewScale: 20.0`, `liftingBonus: 300.0`, `keypointRewScale: 200.0`, `reachGoalBonus: 1000.0` — the five matching weights).
- **Paper:** Sec. III-C, Eq. 1–4, and Table II.
- **Commit:** `aeed298638a1f7b5421b38f5f3cc2d1079b6d9c3` (`corpus/code_manifest.json`, NVIDIA-Omniverse/IsaacGymEnvs).
- **Note:** `papers/notes/dexpbt_2023.md`, section "C. Reward / objective block."

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (Reward engineering, the paragraph on zeroed terms):

> "Zeroed terms recur, and are not the same failure. A term present and zeroed is worse than a term
> missing, because it survives a reader's check of the file, but only when the paper claims it.
> DexPBT \cite{dexpbt_2023} sums eight components against the paper's four and multiplies
> \texttt{hand\_delta\_penalty} by zero with the comment ``currently disabled'', a term the paper
> never claims, and its five named weights are present at their stated values."

From `tex/sections/05_training.tex` (the three-zeroed-terms paragraph, listing this alongside
DeXtreme and PenSpin):

> "Three cells an earlier draft marked \texttt{code} print \texttt{code (0)} instead, because in
> each the term is in the released code with every shipped configuration setting its weight to
> zero: DeXtreme \cite{dextreme_2022}'s \texttt{timeout\_rew} and DexPBT \cite{dexpbt_2023}'s fall
> penalty through \texttt{fallPenalty: 0.0}, and PenSpin \cite{penspin_2024}'s
> \texttt{action\_penalty\_scale: 0.0}."

From `tex/sections/08_gaps.tex`:

> "An adversarial re-reading withdrew seven accusations. ManipTrans, Eureka, Open-TeleVision,
> DexMachina, ArtiGrasp and GraspXL ..., and the domain-randomisation half of the charge against
> DexPBT \cite{dexpbt_2023}."

The appendix (`tex/sections/appendix_c_rewards.tex`) currently lists both the surviving and
withdrawn halves together, with the review note attached:

> "DexPBT (high). Paper presents the reward as 4 mutually exclusive stage terms ... but code's
> compute_kuka_reward sums 8 named components, one of which (hand_delta_penalty) is multiplied by
> 0 and disabled ... Also, the paper reports zero experiments with domain randomization, yet the
> shipped AllegroKuka.yaml already carries a fully specified DR schedule (disabled via randomize:
> False). — Review: R3 adversarial review: the disabled-randomisation half is withdrawn, since the
> note finds it consistent with the paper; the zeroed reward term stands"

## Questions for the authors

1. Is our reading of `compute_kuka_reward` correct — that `hand_delta_penalty` is computed but
   multiplied by zero in the shipped `AllegroKuka.yaml`, and so never affects the trained policy?
2. Is there a reason the released configuration disables this term (e.g., it was an experimental
   addition after the paper's results, or found unhelpful) that we should record alongside the
   observation?
3. Would you like the wording of the claim, as it will appear in the appendix and in Section V,
   changed in any way before we publish?
