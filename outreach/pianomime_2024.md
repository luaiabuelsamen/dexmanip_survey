# Outreach note — pianomime_2024

## Paper
**PianoMime: Learning a Generalist, Dexterous Piano Player from Internet Demonstrations**
Qian et al. — CoRL 2024 (arXiv 2407.18178)
Code: https://github.com/sNiper-Qian/pianomime

## The claim

Table 3 states the per-song reward is a two-term weighted sum: Key Press (weight 2/3) and Mimic
(weight 1/3). The released environment's `_set_rewards` sums roughly five terms with no explicit
weight arguments: `_compute_key_press_reward` (which itself doubles its own [0,1]-range formula,
returning `2*rew` rather than applying the paper's stated 2/3 weight), `_compute_sustain_reward`,
`_compute_energy_reward` (computed but hardcoded to `return 0`), `_compute_fingering_reward`
(computed but hardcoded to `return 0.0`, with the real computation commented out), and
`_compute_forearm_reward` (a term — reward for not colliding the forearms — with no counterpart in
Table 3 at all). The paper's "Mimic" term is implemented separately, added by a wrapper
(`DeepMimicWrapper`) rather than inside the environment's own reward function.

## Evidence

- **Code:** `code/md/pianomime_2024.md`, `single_task/piano_with_shadow_hands_res.py` (file header
  at code/md line 1261), class `PianoWithShadowHandsResidual`: `_set_rewards` (code/md line 1301)
  builds the composite reward from `_compute_key_press_reward`, `_compute_sustain_reward`,
  `_compute_energy_reward`, and conditionally `_compute_fingering_reward` and
  `_compute_forearm_reward`. `_compute_key_press_reward` (code/md line 1358) computes `rew` as the
  paper's stated [0,1] formula, then `return 2*rew` (the doubling). `_compute_energy_reward` (code/md
  line 1348) computes `rew` from actuator power but its final line is `return 0` (the computed value
  discarded). `_compute_fingering_reward` (code/md line 1381) computes `rews` from fingertip-to-key
  distance but its final line is `return 0.0`, with `# return float(np.mean(rews))` commented out
  immediately above it. `_compute_forearm_reward` (code/md line 1324) returns 0.5 for no
  forearm-forearm collision, 0.0 otherwise — a term with no row in Table 3. The mimic term lives in
  a separate wrapper file referenced at code/md lines 216 and 244 (`deep_mimic.py`,
  `DeepMimicWrapper._compute_end_effector_pos_mimic_reward`), added to the reward function from
  outside this class.
- **Paper:** Table 3 and Appendix C (reward weights and descriptions).
- **Commit:** `c4abefac8d2941f5a08ca656b12f5e047cab7155` (`corpus/code_manifest.json`,
  sNiper-Qian/pianomime).
- **Note:** `papers/notes/pianomime_2024.md`, section "C. Reward / objective — quoted verbatim,
  paper vs. code."

The note also flags, separately from this reward mismatch and worth mentioning to the authors in
the same letter since it touches the same headline numbers: the abstract states "up to 56% F1 on
unseen songs" and Table 1/9 report a mean test F1 of 0.57 for the best variant, but Sec. 5's
Conclusion states "an average F1-score of 70% on unseen songs," with no reconciling number found in
either source we parsed.

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (the zeroed-terms paragraph):

> "PianoMime \cite{pianomime_2024}'s Table~3 states two weighted terms while its environment sums
> roughly five unweighted ones, two of them inherited stubs returning zero and a third, forearm
> collision, the paper never lists."

From `tex/sections/appendix_c_rewards.tex`:

> "PianoMime (high). Paper's Table 3 states 2 weighted reward terms (Key Press 2/3, Mimic 1/3), but
> the released code sums roughly 5 unweighted terms (key press doubled, sustain, energy and
> fingering hardcoded to return 0, forearm-collision) plus a separately-added mimic wrapper term."

## Questions for the authors

1. Is our reading of `_set_rewards`/`_compute_key_press_reward` etc. correct — that the released
   environment sums roughly five terms (with energy and fingering computed but discarded) rather
   than the two weighted terms in Table 3?
2. Is there a reason the released reward differs from Table 3's description — for example, did
   Table 3 describe an earlier or simplified version of the reward, or were the energy/fingering
   terms disabled after an ablation showed they did not help?
3. Would you like the wording of this claim, as it appears in Section V and the appendix, changed
   in any way before we publish?

(A separate, smaller point worth raising in the same email since it touches the same headline
numbers: the abstract's "56% F1 on unseen songs" and Sec. 5's "an average F1-score of 70% on
unseen songs" do not obviously reconcile against Table 1/9's reported 0.57 mean test F1. If you can
point us to the reconciling number, we would be glad to fix our citation of it as well.)
