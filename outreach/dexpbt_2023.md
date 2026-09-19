# Outreach note — dexpbt_2023

**Status note (read first):** the survey's own adversarial review (R3) already withdrew half of
this claim. The row's `paper_code_mismatch` field still contains both halves for the record, but
the running prose in Section V and the conclusion has been
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

Quoted from the paper as it stands today, so that what you are being asked about is the
wording that would actually appear. Only the sentences naming your work are reproduced;
citation markers are replaced with the short name of the work cited.

From Section V, *Training*:

> DexPBT is consistent: its configuration disables randomisation, as the paper says.

> Three marks an earlier draft recorded as code now read code (0), because in each the term is
> in the released code with every shipped configuration setting its weight to zero: DeXtreme's
> timeout reward, DexPBT's fall penalty, and PenSpin's action penalty. Marking them code would
> tell a reader the code optimises something the paper does not state, and leaving them
> unmarked would hide a term that is in the file. The repository carries the config key and
> the zero beside each of the three marks.

> DexPBT tightens a success tolerance from 0.075 to 0.01 by a factor of 0.9 every 3000
> environment steps once three successes are logged, and ManipTrans starts at zero gravity and
> high friction and restores both while narrowing a fingertip threshold from 6 cm to 4 cm.

> DexPBT runs populations of 8, 16 and 32 agents, splits them 30/40/30, mutates the middle and
> replaces the bottom with mutated copies of the top, each float hyperparameter multiplied or
> divided by a factor drawn from U(1.1, 1.5) with probability 0.2. It reports 30 hours on a
> single V100 for a five-billion-transition single-arm run, and 0.32 trillion environment
> steps for its largest population.

From Appendix C, the per-paper entry:

> DexPBT (high). Paper presents the reward as 4 mutually exclusive stage terms (r_reach,
> r_pick, r_targ, -r_vel), but code's compute_kuka_reward sums 8 named components, one of
> which (hand_delta_penalty) is multiplied by 0 and disabled; there is no single r_vel term in
> code, instead separate kuka/allegro action penalties whose exact formula is not shown. Also,
> the paper reports zero experiments with domain randomization, yet the shipped
> AllegroKuka.yaml already carries a fully specified DR schedule (disabled via randomize:
> False).
>
> Artefact: `NVIDIA-Omniverse/IsaacGymEnvs` at `aeed298638`,
> `isaacgymenvs/tasks/allegro_kuka/allegro_kuka_base.py` (`compute_kuka_reward`).
>
> Review: R3 adversarial review: the disabled-randomisation half is withdrawn, since the note
> finds it consistent with the paper; the zeroed reward term stands

## Questions for the authors

1. Is our reading of `compute_kuka_reward` correct — that `hand_delta_penalty` is computed but
   multiplied by zero in the shipped `AllegroKuka.yaml`, and so never affects the trained policy?
2. Is there a reason the released configuration disables this term (e.g., it was an experimental
   addition after the paper's results, or found unhelpful) that we should record alongside the
   observation?
3. Would you like the wording of the claim, as it will appear in the appendix and in Section V,
   changed in any way before we publish?
