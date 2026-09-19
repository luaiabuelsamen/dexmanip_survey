**DOUBT, FLAGGED PROMINENTLY — read before sending.** This claim bundles two sub-claims of very
different strength, and the survey's own adversarial review (`reviews/r3_methods.md`, item 13)
found that one of them is likely reading the wrong stage of the pipeline. The paper's oracle policy
(the RL stage) takes tactile sensing, fingertip positions and a point cloud as input; the paper's
*student* policy — the one actually deployed and fine-tuned on real rollouts — is proprioception
only ("30 steps of joint positions ... and previous targets ... only," per
`papers/notes/penspin_2024.md`). The released `AllegroHandHora.yaml` config we read has
`numObservations: 96` and `enable_tactile: False`, which is consistent with it being the
**student's** config, not the oracle's — in which case "the released code disables the paper's
tactile channel" is not a contradiction at all, since the paper never claims the student has
tactile input. We were not able to confirm from the parsed code alone whether a separate oracle
config with tactile enabled exists elsewhere in the repository. The disturbance-force half of the
claim (`forceScale: 0.0` against the appendix's stated disturbance-force randomization) does not
have this problem and is comparatively solid.

**Recommendation:** lead with the disturbance-force claim, and ask about the tactile-channel
reading directly rather than asserting it — the questions below are written that way.

# Outreach note — penspin_2024

## Paper
**Lessons from Learning to Spin "Pens"**
Wang, Yuan, Che, Qi, Ma, Malik, Wang — CoRL 2024 (arXiv 2407.18902)
Code: https://github.com/HaozhiQi/penspin

## The claim

Appendix A.2 describes an external disturbance force of 0.2× the object's mass, applied with
probability 0.25, as part of domain randomization. The released task config sets both
`forceScale: 0.0` and the corresponding probability scalar to 0.0, so this disturbance force is
disabled in the shipped configuration. Separately (see the doubt above), the released config's
96-dimensional observation has `enable_tactile: False` and no point-cloud channel, which we
initially read as a contradiction of the paper's tactile-sensing oracle but now believe is more
likely the student-stage config, consistent with the paper. A third, weaker observation: the
paper's Table 4 weight names (λ_rot, λ_z, λ_l, λ_diff, λ_ang, λ_torque, λ_work) do not name-match
the code's scale keys one-to-one (`rotate_reward_scale`, `pencil_z_dist_penalty_scale`,
`obj_linvel_penalty_scale`, etc.), though the matched values agree.

## Evidence

- **Code (disturbance force):** `code/md/penspin_2024.md`, `penspin/tasks/allegro_hand_hora.py`
  (file header at code/md line 589); `forceScale: 0.0` at code/md line 320.
- **Code (tactile channel, the disputed half):** `numObservations: 96` at code/md line 293;
  `enable_tactile: False` at code/md line 390; the observation-building code checks
  `self.config['env']['privInfo']['enable_tactile']` at code/md lines 652 and 695.
- **Paper:** Appendix A.2 (disturbance force), Sec. 3.1 (oracle observation, tactile channel c_t),
  Sec. 3.2 (student observation, proprioception only), Table 4 (reward weights).
- **Commit:** `5035c52dc949e81313af71d9a0ca5ead8b463a5a` (`corpus/code_manifest.json`,
  HaozhiQi/penspin).
- **Note:** `papers/notes/penspin_2024.md`, "domain randomization" and observation paragraphs.
- **Internal review:** `reviews/r3_methods.md`, item 13, which raises exactly the tactile-config
  concern described above and recommends checking whether `AllegroHandHora.yaml` is the oracle or
  student config before treating the tactile-channel absence as a discrepancy.

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (domain-randomisation discipline paragraph):

> "PenSpin \cite{penspin_2024} zeroes the disturbance force its appendix describes."

From the same section (zeroed-terms paragraph):

> "PenSpin \cite{penspin_2024}'s \texttt{action\_penalty\_scale: 0.0}."

From the "Weights drift"/reward-naming discussion:

> "PenSpin \cite{penspin_2024} ships \texttt{forceScale: 0.0} against the disturbance force in its
> appendix, and its 96-dimensional observation carries no tactile channel, which is also what its
> proprioception-only student should carry, hence the medium confidence."

From `tex/sections/appendix_c_rewards.tex`:

> "PenSpin (medium). The released code disables the paper's tactile observation channel and zeroes
> the described disturbance-force domain randomization, and the code's reward scale-key names
> (e.g. rotate_reward_scale, pencil_z_dist_penalty_scale) do not 1:1 name-match the paper's Table 4
> weight list, though matched values agree. — Review: R3 adversarial review: plausible alternative
> reading; held at medium confidence pending a direct code read"

## Questions for the authors

1. Is the released `AllegroHandHora.yaml` (`numObservations: 96`, `enable_tactile: False`) the
   configuration for the proprioceptive student, or is it also used for the privileged oracle? If
   it is the student's, we believe our tactile-channel reading was mistaken and would like to
   correct it.
2. Is there a reason the disturbance force is set to zero in the released task configuration
   despite Appendix A.2 describing it as part of training (for example, it was used only in an
   earlier ablation, or disabled after submission)?
3. Would you like the wording of this claim, as it appears in Section V and the appendix, changed
   or narrowed before we publish?
