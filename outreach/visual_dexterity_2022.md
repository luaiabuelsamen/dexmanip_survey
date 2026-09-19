# Outreach note — visual_dexterity_2022

## Paper
**Visual Dexterity: In-Hand Reorientation of Novel and Complex Object Shapes**
Chen et al. — Science Robotics 2023 (arXiv 2211.11744)
Code: https://github.com/Improbable-AI/dexenv

## The claim

This row bundles five separate discrepancies, each independently checkable against the released
code:

1. Table S1 states 32,000 teacher-training parallel environments; the released
   `dexenv/conf/dclaw.yaml` sets `alg.num_envs: 8000`, and its parent `hand_default.yaml` sets it
   to 16,384 — neither matches Table S1's figure (though the batch-size number, envs ×
   `train_rollout_steps`, does reproduce from the 8000 figure).
2. `fallDistance` is 0.24 in `dclaw.yaml` but 0.15 in `hand_default.yaml`, two shipped configs that
   both apply to the teacher; only 0.15 matches Table S1's p̄ threshold.
3. The paper's Eq. 8 (in-air reward variant) includes a penultimate-joint penalty with coefficient
   c7 = −2; no such term appears anywhere in `dexenv/envs/rewards.py`.
4. The config carries a key, `distRewardScale: -10.0`, that never appears inside
   `compute_reward`'s body — a dead, unused key.
5. The paper's Table S3 states a table-friction randomization lower bound of 0.05; the code's
   `obj_rand.yaml` scales a base value of 0.5 by a factor whose lower bound (0.01) produces an
   effective lower bound of 0.005 — a factor of ten below the paper's stated value.

## Evidence

- **Code (env count):** `code/md/visual_dexterity_2022.md`, `dexenv/conf/dclaw.yaml`
  (`num_envs: 8000` at code/md line 302) and `hand_default.yaml` (`num_envs: 16384` at code/md line
  505).
- **Code (fall distance):** `dclaw.yaml` (`fallDistance: 0.24` at code/md line 701) vs.
  `hand_default.yaml` (`fallDistance: 0.15` at code/md line 498).
- **Code (reward function):** `dexenv/envs/rewards.py`, function `compute_reward`/
  `compute_dclaw_reward`, quoted in full in `papers/notes/visual_dexterity_2022.md` (no
  penultimate-joint term present; `distRewardScale: -10.0` at code/md line 696 unused in the
  function body).
- **Code (table friction):** `dexenv/conf/task/task/obj_rand.yaml`, scaling
  `tableInitialFriction: 0.5` by a factor range that yields [0.005, 1.0].
- **Paper:** Table S1 (env count, fall distance threshold p̄=0.15), Eq. 8 (penultimate-joint
  penalty c7=−2), Table S3 (table-friction range [0.05, 1.0]).
- **Commit:** `ad9634e9d26cf5555d18728244a58f5b412c1eb2` (`corpus/code_manifest.json`,
  Improbable-AI/dexenv).
- **Note:** `papers/notes/visual_dexterity_2022.md`, "Setting" (env count) and "reward or loss"
  (fall distance, penultimate-joint penalty, dead key, friction range) paragraphs.

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (Privilege/distillation paragraph, cited for the method
generally):

> "Visual Dexterity \cite{visual_dexterity_2022} distils twice, from a state teacher to a synthetic
> point cloud and then to a rendered one, for a fivefold speedup."

From the "Weights drift" paragraph (the mismatch claim itself):

> "Visual Dexterity \cite{visual_dexterity_2022}'s Eq.~8 penultimate-joint penalty is absent from
> \texttt{dexenv/envs/rewards.py}, and its two configs disagree about the fall distance."

From the reward-family/contact-mark paragraph:

> "The fourth, \cite{visual_dexterity_2022}, penalises the \emph{object} touching the table, a
> task-shaping term against using the table as a third finger rather than a hand-object term, and
> its \texttt{pen\_tb\_contact} flag defaults to \texttt{False} with no shipped config setting it
> true."

From `tex/sections/appendix_c_rewards.tex`:

> "Visual Dexterity (high). Table S1 states 32000 teacher training environments, but the released
> config sets alg.num_envs to 8000 (parent config 16384); fallDistance differs across two shipped
> configs (0.24 vs 0.15, only the latter matching Table S1's threshold); the paper's Eq 8
> penultimate-joint penalty (c7=-2) does not appear anywhere in the released reward code; the
> config carries a dead distRewardScale=-10.0 key never used in compute_reward; and the paper's
> table-friction lower bound (0.05) differs by a factor of 10 from the code's randomized lower
> bound (0.005)."

## Questions for the authors

1. Is our reading of the released configs and `dexenv/envs/rewards.py` correct on each of the five
   points above — the environment count, the two disagreeing fall-distance values, the absent
   penultimate-joint penalty, the unused `distRewardScale` key, and the table-friction lower bound?
2. Is there a reason the released training configuration differs from the paper's Table S1/S3 and
   Eq. 8 on these points — for example, values that were tuned after the paper's numbers were
   produced, or a released config that corresponds to a different experiment than the one Table S1
   reports?
3. Would you like the wording of this claim, as it appears in Section V and the appendix, changed
   in any way before we publish?
