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

Quoted from the paper as it stands today, so that what you are being asked about is the
wording that would actually appear. Only the sentences naming your work are reproduced;
citation markers are replaced with the short name of the work cited.

From Section V, *Training*:

> PenSpin describes random disturbance forces, while the only public configuration that names
> them disables them.

> Three marks an earlier draft recorded as code now read code (0), because in each the term is
> in the released code with every shipped configuration setting its weight to zero: DeXtreme's
> timeout reward, DexPBT's fall penalty, and PenSpin's action penalty. Marking them code would
> tell a reader the code optimises something the paper does not state, and leaving them
> unmarked would hide a term that is in the file. The repository carries the config key and
> the zero beside each of the three marks.

> Nine is the number to quote, eight at high confidence and one, PenSpin, held at medium.

> PenSpin, the sole medium-confidence case retained, concerns a disabled disturbance rather
> than the tactile input claimed in an earlier draft. Each change and its reason is preserved
> with the underlying record. Future papers can avoid most of this ambiguity by generating the
> reward table directly from the configuration used for training and citing the corresponding
> revision.

From Appendix C, the per-paper entry:

> PenSpin (medium). The appendix states a randomised disturbance force and the released task
> config sets its scale to zero. A second half of the original comparison, that the released
> code disables the paper's tactile observation channel, is withdrawn: the config read has 96
> observation dimensions and `enable_tactile: False`, consistent with the proprioception-only
> student policy rather than the tactile-and-point-cloud oracle, and the paper never claims
> the student has tactile input. The code's reward scale-key names (e.g. rotate_reward_scale,
> pencil_z_dist_penalty_scale) also do not 1:1 name-match the paper's Table 4 weight list,
> though matched values agree.
>
> Artefact: `HaozhiQi/penspin` at `5035c52dc9`, `configs/task/AllegroHandHora.yaml`
> (`forceScale`).
>
> Review: Narrowed at the point of drafting the letter to its authors, which was never sent.
> The tactile-channel half is withdrawn as a plausible reading of which pipeline stage the
> config belongs to; the disturbance-force half stands. Held at medium confidence pending a
> direct code read.

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
