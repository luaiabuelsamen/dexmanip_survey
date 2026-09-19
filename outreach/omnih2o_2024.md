**DOUBT, FLAGGED PROMINENTLY — read before sending.** This is one of the two claims the survey
already holds at medium confidence, and reading the underlying adversarial review
(`reviews/r3_methods.md`, item 11) raises a further, specific concern that goes beyond "medium":
four of the five weight comparisons in this row agree with the paper's table to the digit once a
systematic ×1.25 curriculum factor is accounted for (`dof_pos_limits` −100×1.25 = −125,
`termination` −200×1.25 = −250, `slippage` −30×1.25 = −37.5, `feet_ori` −50×1.25 = −62.5, all
exact matches). Only the `stumble` weight is off, by a factor of roughly one million (−0.00125 vs
−1250) — which reads much more like a decimal-point/units typo in the paper's own table than a
policy trained on a different objective than the paper describes. The reviewer's own words: "A
single term off by 10^6 against four neighbours that agree to the digit is a typo signature." The
reviewer also notes this whole paper is a poor fit for a *dexterous-manipulation* reward census in
the first place — the hands are open-loop, driven directly from VR pose, and are "outside the
policy and outside the reward" entirely (`papers/notes/omnih2o_2024.md`); there is no object in
the simulation and no interpenetration or contact term of any kind to speak of.

**Recommendation:** send this letter, but consider it a low-stakes confirmation request rather
than an accusation, and consider downgrading or dropping the `stumble` sub-claim from the
survey's own table if the authors point to a units difference or a printed typo. The
`max_feet_height`, `exp` functional form, and curriculum-threshold sub-claims are comparatively
weaker still (plausible alternate readings per the row's own review note) and should be treated the
same way.

# Outreach note — omnih2o_2024

## Paper
**OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning**
He, Luo, He, Xiao, Zhang, Zhang, Kitani, Liu, Shi — CoRL 2024 (arXiv 2406.08858)
Code: https://github.com/LeCAR-Lab/human2humanoid

## The claim (as currently drafted, held at medium confidence)

Table 15's stumble-penalty weight is −0.00125; the shipped reward config
(`rewards_teleop_omnih2o_teacher.yaml`) sets the corresponding `feet_stumble` scale to a value
consistent with −1250 (a discrepancy of roughly 10^6). Table 15's max-feet-height term is listed as
a +1000 bonus with the form `max(h_max − 0.25, 0)`; the shipped config's `feet_max_height_for_this_air`
scale is −2500, i.e. a penalty rather than a bonus, against a `desired_feet_max_height_for_this_air:
0.25` target. The paper writes several task-tracking terms as `exp(−c‖·‖)`; the code computes them
as `exp(−err²/σ)`. The paper's reward curriculum lowers the difficulty level when mean episode
length falls below 40; the code checks against 50.

## Evidence

- **Code:** `code/md/omnih2o_2024.md`, `legged_gym/legged_gym/cfg/rewards/rewards_teleop_omnih2o_teacher.yaml`
  (file header at code/md line 1525, `scales:` block starting line 1528). The relevant lines:
  `stumble : -1000.0*1.25` (line 1541, i.e. −1250), `feet_max_height_for_this_air : -2500` (line
  1550), alongside four neighboring lines that match Table 15 exactly once the same ×1.25 factor is
  applied — `dof_pos_limits : -100.0*1.25` (line 1537, matches −125), `termination : -200*1.25`
  (line 1539, matches −250), `slippage : -30.0*1.25` (line 1543, matches −37.5), `feet_ori :
  -50.0*1.25` (line 1544, matches −62.5). The separate, unrelated
  `legged_gym/legged_gym/cfg/rewards/rewards_base.yaml` file (code/md line 1476) sets its own
  `feet_stumble : -0.0` default, which is not the file that trains the OmniH2O teacher and should
  not be confused with it — we flag this here because our own first pass at this evidence made
  exactly that mistake, which is itself a small demonstration of how easy this class of error is to
  make when reading configs quickly.
- **Paper:** Appendix E, Table 15 (reward terms and weights).
- **Commit:** `750f1fa052641f0fde43669d50cb4e407dabe6c8` (`corpus/code_manifest.json`,
  LeCAR-Lab/human2humanoid).
- **Note:** `papers/notes/omnih2o_2024.md`, "reward (code, ...)" and "mismatches paper vs code"
  paragraphs.
- **Internal review:** `reviews/r3_methods.md`, item 11 ("`omnih2o_2024` does not belong in a
  dexterous-manipulation reward census"), which argues the stumble discrepancy is very likely a
  typesetting error in the paper's own table rather than evidence the code departs from it, and
  that the paper's hands are outside the learned policy entirely.

## What the survey will say in print if you do not reply

From `tex/sections/05_training.tex` (Section V-H):

> "Ten is the number to quote, eight at high confidence and two, PenSpin \cite{penspin_2024} and
> OmniH2O \cite{omnih2o_2024}, held at medium pending a direct read of the code."

From `tex/sections/08_gaps.tex`:

> "Ten is the number to quote, eight at high confidence, with PenSpin \cite{penspin_2024} and
> OmniH2O \cite{omnih2o_2024} held at medium against innocent readings a direct code read would
> settle."

From `tex/sections/appendix_c_rewards.tex` (the full itemized claim as it stands today):

> "OmniH2O (medium). stumble weight -0.00125 (paper) vs -1250 (code); max-feet-height
> sign/magnitude differ (+1000 paper vs -2500 code, a penalty not a bonus); paper's exp(-c*||.||)
> form vs code's exp(-err²/sigma); curriculum level-down threshold 40 (paper) vs 50 (code). —
> Review: R3 adversarial review: plausible alternative reading; held at medium confidence pending a
> direct code read"

## Questions for the authors

1. Is the stumble-penalty weight in Table 15 (−0.00125) correct as printed, or is it a
   typesetting/units slip relative to the value actually used in the released
   `rewards_teleop_omnih2o_teacher.yaml`? (We suspect the latter, given that four neighboring
   weights in the same table match the code to the digit once a 1.25 curriculum multiplier is
   applied.)
2. Is the max-feet-height term in the released config intended as a penalty against a 0.25 m target
   (as the code reads), or does Table 15's "+1000" describe a different, earlier version of the
   reward?
3. Given that the hands in this paper are open-loop and outside the learned policy, would you
   prefer this paper be described in our survey only in the humanoid-teleoperation/whole-body
   tracking sections, and not cited as an example of a dexterous-hand reward discrepancy?
