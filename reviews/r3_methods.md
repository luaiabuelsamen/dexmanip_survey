# R3 — learning methods. Review of paper/survey.md, sections 5 and 6, tables 5 and 6, figure 4.

Scope: I audited all sixteen rows the survey classes `mismatch_class: contradiction`, against
`papers/notes/<key>.md`, `corpus/rows/<key>.json` and, where the repository was parsed,
`code/md/<key>.md`. I then checked figure 4's branch assignments, six rows of table 5 cell by
cell, table 6's counts, and section 6's denominators. I have been deliberately adversarial in the
accused papers' favour, as section 8.1 makes a serious claim about other people's work.

**Section 5.4 is sound** and is the best-evidenced part of the survey I read: the eight trackers
are described in the paradigm their authors would recognise, the `physhoi_2023` / `dextrack_2025` /
`toporetarget_2026` / `dexplore_2025` characterisations all match their notes, and the closing
claim that penetration is handled at the reference and never at the rollout survives checking.
Section 5.6 and section 6.5 are also sound. Section 5.2.2's counts all reconcile with table 5
(I recomputed each of the nine family counts; nineteen, thirteen, thirteen, twelve, eleven,
eight, five, four are all correct).

The problem is concentrated in three places: the mismatch census that section 8.1 rests on,
figure 4's leaf predicates, and section 6's shifting denominators.

---

## A. Accusations in section 8.1 that should be withdrawn

### 1. blocking — the `maniptrans_2025` accusation is backwards

**location**: §5.8, "`maniptrans_2025`'s stated learning rate and environment count differ from its
own README." `corpus/rows/maniptrans_2025.json`: `mismatch_class: contradiction`,
`mismatch_confidence: high`, "paper's PPO learning rate (5e-4) and env count (4096) differ from the
shipped README/yaml defaults (2e-4, 8192)".

**the problem**: Both halves are wrong in the direction that matters. The repository's own config
default *is* the paper's learning rate, and every README training command *is* the paper's
environment count.

**the evidence**: `code/md/maniptrans_2025.md` line 535 sets `learning_rate: 5e-4`, and lines 683
and 848 resolve to `5e-4` — exactly the paper's stated value. The `2e-4` the row cites appears only
as an explicit command-line override inside README example commands (lines 185-277). Those same
commands all pass `num_envs=4096` — exactly the paper's stated value; `8192` is only the unused
`resolve_default` fallback at lines 886 and 1098. The note itself
(`papers/notes/maniptrans_2025.md`, Setting block) records "yaml default `numEnvs: 8192`, README
commands use `num_envs=4096`", and its closing bullet says "cite the paper values as the paper's
and the README as the reproduction recipe" — i.e. the note does not read this as a contradiction.
Separately, a learning rate is not a reward, and §8.1 is headed "Released code does not implement
the published reward."

**the fix**: Withdraw `maniptrans_2025` from the sixteen. If anything survives, it is a one-line
reproducibility note: "the README's example commands lower the learning rate from the paper's and
the config's 5e-4 to 2e-4." Recount §8.1 and §5.8 accordingly.

### 2. blocking — the `eureka_2023` accusation is refuted by the repository's own README

**location**: §5.2.3, "Eureka's released config ships one iteration and three samples against the
paper's five iterations, sixteen samples and five runs"; §8.1 counts this as a true contradiction.

**the problem**: The repository documents the paper's values as the defaults and tells the user to
pass the knobs on the command line. A hydra fast-test default is not the code contradicting the
paper.

**the evidence**: `code/md/eureka_2023.md` lines 65-71 — the README's usage block reads
`python eureka.py env={environment} iteration={num_iterations} sample={num_samples}`, followed by
"`{num_samples}` is the number of reward samples to generate per iteration. Default value is `16`"
and "`{num_iterations}` is the number of Eureka iterations to run. Default value is `5`." The
`iteration: 1 / sample: 3` at lines 237-238 sit beside `max_iterations: 3000 # RL Policy training
iterations (decrease this to make the feedback loop faster)`, i.e. a documented quick-run block.
The note (`papers/notes/eureka_2023.md`, line 17) already calls it "a fast-test default … a
paper/code default mismatch worth flagging if someone reruns the repo as-is" — a usability note,
not a contradiction. The second half of the charge ("the generated rewards are written to a
gitignored directory") is true but is also documented behaviour: README line 81, "Each run will
create a timestamp folder in `eureka/outputs` that saves the Eureka log as well as all intermediate
reward functions and associated policies."

**the fix**: Withdraw `eureka_2023` from the sixteen. Replace the §5.2.3 sentence with: "Eureka's
generated rewards are produced at runtime and not checked into the repository, so the specific
reward behind any reported number cannot be recovered from the repository, though the README
documents the paper's search budget as the default."

### 3. blocking — `open_television_2024` has no reward, and the charge is a README example command

**location**: `corpus/rows/open_television_2024.json`, `mismatch_class: contradiction`,
`confidence: high` — "the paper's prose states 25k training iterations, lr 5e-5, batch size 45,
but the code repo's example training command instead shows 50000 epochs and an explicit
kl_weight=10 not mentioned anywhere in the paper text."

**the problem**: This is a behaviour-cloning teleoperation paper. `papers/notes/open_television_2024.md`
states plainly under the reward bullet: "not an RL paper — no reward function." The comparison is
between paper prose and an example command in a README, and it compares *iterations* to *epochs*,
which are different units. `kl_weight=10` is ACT's own standard CVAE weight, inherited from the
architecture the paper says it uses.

**the evidence**: `papers/notes/open_television_2024.md`, Method block; the note's own phrasing is
"the code repo's training command (`README`, code/md) additionally shows …". No claim is made
anywhere that the shipped code computes a different quantity from the paper's.

**the fix**: Withdraw. A paper with no reward function cannot be evidence for "released code does
not implement the published reward."

### 4. blocking — the `dexmachina_2025` accusation misreads the paper's own equation

**location**: `corpus/rows/dexmachina_2025.json` — "paper describes a plain weighted sum
lambda_task*r_task + … ; code implements a multiplicative task term with per-component beta decay".

**the problem**: The multiplicative task term and the per-component βs are printed in the paper, in
display form. The survey is charging the code with structure the paper states.

**the evidence**: `papers/md/dexmachina_2025.md` line 73:
`r_task = r_pos * r_rot * r_angle = exp(−β_pos d_pos) exp(−β_rot d_rot) exp(−β_ang d_ang)`, with
line 60 saying "The task reward r_task is the product of three terms measuring accuracy in each
state component." The paper also describes the auxiliary-weight decay the row treats as
undisclosed (line 131: "Because the auxiliary rewards use a much smaller weight…"). The note
(`papers/notes/dexmachina_2025.md`, line 20) quotes the multiplicative form as the *paper's*. The
note also records that "The body of `compute_reward` (the weighted sum) is not in the code md; only
its signature is" — so the one thing the row alleges about the top-level combination is not
verifiable from the parse at all.

**the fix**: Withdraw, or reduce to the single defensible item: the code carries a `force_penalty`
of 0.1 the paper does not mention, and the paper's "See Appendix A.4 for precise weights" points at
an appendix that prints no λ. That is a non-disclosure, not a contradiction.

### 5. blocking — `artigrasp_2023`'s reward code was never parsed

**location**: `corpus/rows/artigrasp_2023.json`, `mismatch_class: contradiction`, `confidence: high`.

**the problem**: The comparison is between a paper weight table and YAML key names. The function
that computes the reward is C++ and is absent from the parse, so "the shipped code demonstrably
states another value" cannot be asserted. The phase-1/phase-2 weight difference is also not a
contradiction: the paper documents a two-phase curriculum.

**the evidence**: `papers/notes/artigrasp_2023.md` line 19 — "the reward body is C++ (raisimGymTorch
env, not in the code md, which lists Python signatures only: `get_reward_info` ->
`self.wrapper.rewardInfoLeft()`)". The two "missing" values (fingertip weight 12.0, λ=5.0) are
per-link and cap constants that would live in the unparsed C++, and the five weights that *are*
comparable all match. The curriculum is the paper's own (Sec. 4.4, "fix the objects to the table
surface and train each hand separately", then a shared environment).

**the fix**: Reclassify as `parse-limitation`. If you keep any claim, it is "Table 6 reports one
weight set for a two-phase curriculum whose phases ship different weights", labelled as
under-reporting, not contradiction.

### 6. blocking — `graspxl_2024`'s reward code was never parsed either

**location**: §5.8, "`graspxl_2024` splits one regulariser into four and ships an object-velocity
coefficient of −1.5 against a stated 0.1." Stated as fact, no caveat.

**the problem**: The note says the reward computation cannot be verified and offers a benign
explanation the survey drops.

**the evidence**: `papers/notes/graspxl_2024.md` line 42 — "code/md does not contain
`Environment.hpp` for `ours_fixed`/`ours_floating` (not present in the depth-3 file tree or the
extracted Python signatures), so the actual reward computation cannot be verified beyond these
coefficient tables", and, on the missing wrist-rotation weight, "either it is folded into
`direction_reward` in the (unavailable) C++ reward code, or it is not exposed in this YAML at all."
Once the paper's single `w_o‖u_o‖²` is split into separate object-linear and object-angular
coefficients, its value is not comparable to either of the two code coefficients one-to-one; the
note's own wording is "cannot be reconciled 1:1". This is the one medium-confidence row of the
sixteen and it should not have been promoted.

**the fix**: Reclassify as `parse-limitation` and delete the §5.8 sentence, or rewrite it as
"GraspXL's shipped configs expose four velocity coefficients where the paper prints two; the C++
reward that consumes them is not in the release, so the two cannot be reconciled."

### 7. blocking — half the `dexpbt_2023` charge is a disabled flag the note calls consistent

**location**: §5.2.1, "`dexpbt_2023` reports no domain-randomisation experiments at all, yet its
`AllegroKuka.yaml` carries a complete randomisation schedule behind a `randomize: False` switch",
placed in the paragraph on randomisation "discipline".

**the problem**: `randomize: False` is the shipped state of a shared IsaacGymEnvs config block. The
note reaches the opposite conclusion from the same fact.

**the evidence**: `papers/notes/dexpbt_2023.md`, closing bullet: "DeXtreme's tasks ship
`randomize: True` by default …, while DexPBT's `AllegroKuka.yaml` ships `randomize: False`,
**consistent with the paper's own statement that DR is not used here**." The remaining half of the
charge — "sums eight reward components against the paper's four" — is a grouping difference, not a
disagreement: the same note (line 63) records that "The five weight names/values that ARE named in
both … match exactly between Table II's 'initial value' column and the `AllegroKuka.yaml` defaults",
and the eight code components map onto the paper's four stages (`fingertip_delta_rew` +
`hand_delta_penalty` → r_reach, `lifting_rew` + `lift_bonus_rew` → r_pick, `keypoint_rew` +
`bonus_rew` → r_targ). The zeroed `hand_delta_penalty` is a term the paper never claims, which is
the opposite of the PhysHOI case it is filed beside.

**the fix**: Delete the DR sentence from §5.2.1. Downgrade `dexpbt_2023` from contradiction to a
disclosure note, or, if it stays, say explicitly that the disabled term is one the paper does not
claim, and that the paper's five named weights are all present at their stated values.

### 8. blocking — "all 7 disagree with their paper" contradicts the survey's own classification

**location**: §5.8, "Among the 21 reorientation methods in Table 5, 7 released code and all 7
disagree with their paper."

**the problem**: Two of the seven are not disagreements by §8.1's own taxonomy, and one of them is
the paper the survey elsewhere says could not be checked at all.

**the evidence**: The seven with `code: yes` in `paper/tables/table5_rewards.md` are `dextreme_2022`,
`hora_2022`, `visual_dexterity_2022`, `dexpbt_2023`, `eureka_2023`, `dreureka_2024`, `penspin_2024`.
`corpus/rows/dreureka_2024.json` has `mismatch_class: code-absent` — and §5.2.3 says so in words:
"DrEureka's released repository contains only the locomotion and globe-walking trees, so the quoted
LEAP-hand cube-rotation reward cannot be checked against code at all." `corpus/rows/hora_2022.json`
has `mismatch_class: version-skew`. So "all 7 disagree" counts a paper whose reward code does not
exist in the release and a paper the survey classes as a different repository generation.

**the fix**: "Of the 21 reorientation methods, 7 released a repository. In four of the seven the
released reward code disagrees with the paper; in one the relevant environment is not in the
release; in one the parsed commit is a later generation the authors' own README warns about; in one
the disagreement is a default-value question." Table 5's `code` and `mismatch` columns need a third
state so `dreureka_2024` is not marked `yes / yes`.

### 9. blocking — §5.8's opening number is not the number §8.1 defines

**location**: §5.8, "Thirty-seven of the 110 method rows carry a documented disagreement between
the paper and the released code."

**the problem**: By §8.1's own breakdown, only 16 + 3 = 19 of the 37 are disagreements between a
paper and released code. Nine are limitations of this survey's parse, seven are cases where nothing
could be compared, and two involve no code at all.

**the evidence**: recomputed from `corpus/rows/*.json`: `contradiction` 16, `parse-limitation` 9,
`code-absent` 7, `version-skew` 3, `internal-inconsistency` 2. §8.1 states each of these categories
and then says "Sixteen is therefore the number to quote." §5.8 opens with 37 and derives "the rate
among the 61 methods that released anything is 61 percent" from it — a rate for a thing §8.1 says
the number does not measure.

**the fix**: Open §5.8 with the same 16 §8.1 lands on, and state the 37 as "rows carrying a
recorded paper/repository discrepancy of any kind, including nine that are limits of our parse."
Delete the 61 percent or recompute it on the 19 (31 percent).

---

## B. Accusations that survive, and two that need re-checking

### 10. minor — `physhoi_2023` is correct and should stay the flagship (one wording fix)

I tried to break it and could not. `code/md/physhoi_2023.md` lines 405, 422, 430:
`epv = torch.zeros_like(ep)`, `eor = torch.zeros_like(ep) #torch.mean((ref_obj_rot - obj_rot)**2,dim=-1)`,
`eorv = torch.zeros_like(ep) #…`. The zeroing is unconditional — not switched on the dataset — so
the BallPlay exemption the paper does state (λ^or = 0 for BallPlay, Sec. 5.1) does not explain it
for GRAB, where Table 4 gives λ^or = 0.1. One wording fix: §5.8 says "A method presented as
tracking a 6-DoF reference was, in the code that ran, tracking position only." Body rotation (`rr`,
line 402) and body rotation-velocity (`rrv`, line 409) are live. Say "tracking the *object* in
position only." (minor)

### 11. major — `omnih2o_2024` does not belong in a dexterous-manipulation reward census

**location**: §8.1, "`omnih2o_2024` gives a stumble weight of -0.00125 in Table 15 and ships -1250."

**the problem**: The cited term is a *locomotion* stumble penalty in a whole-body humanoid tracking
controller whose hands are outside the policy and outside the reward. Using it as one of four
exemplars of what is wrong with dexterous reward reporting overstates the case, and the specific
discrepancy is more likely a decimal error in the paper's table than a code that does not implement
the paper.

**the evidence**: `papers/notes/omnih2o_2024.md` line 17 — "The fingers are outside the policy and
outside the reward"; line 21 — "interpenetration / contact: none. No objects in the simulation."
Line 19 shows the code's weights carry a systematic ×1.25 curriculum factor that reproduces the
paper's table exactly for `dof_pos_limits` (−100×1.25 = −125), `termination` (−200×1.25 = −250),
`slippage` (−30×1.25 = −37.5) and `feet_ori` (−50×1.25 = −62.5). The note's own summary is "Weights
otherwise agree." A single term off by 10^6 against four neighbours that agree to the digit is a
typo signature.

**the fix**: Move `omnih2o_2024` out of the §8.1 exemplar list; if it stays in the census at all,
say "a whole-body humanoid controller whose hands are open-loop and outside the reward" and note
that the sign and magnitude pattern is consistent with a typesetting error in the paper's table
rather than a code that departs from it.

### 12. major — `hora_2022` is quoted in §8.1's contradiction list but classed version-skew, and its
authors disclosed the discrepancy

**location**: §8.1, "`hora_2022` says it in its own README: 'The reward number in this repository
are higher than what is reported in the paper.'" And §5.2.1, "`hora_2022` states a joint-noise range
of U(0, 0.005) against a shipped `jointNoiseScale` of 0.02 sampled signed, and its disturbance force
defaults to zero in the parsed config", inside the paragraph on randomisation discipline.

**the problem**: `corpus/rows/hora_2022.json` is `mismatch_class: version-skew`, not one of the
sixteen, so §8.1 illustrates its contradiction claim with a case its own taxonomy excludes. Worse,
the quote is *self-disclosure*, which directly undercuts the paragraph it sits in ("the
disagreement is almost never disclosed").

**the evidence**: `papers/notes/hora_2022.md`, closing bullet: the joint-noise and disturbance-force
differences "both suggest the parsed commit (410d9582) is a later, changed version of the repo — the
code README itself states 'some of the experiment numbers may be inconsistent from what was
reported in the paper. Please check out version 0.0.1 … to reproduce the numbers reported in the
paper.' Any reproduction claim for this survey should target tag v0.0.1, not the commit parsed
here." The same note warns against the cube-vs-cylinder default for the same reason.

**the fix**: In §5.2.1, add "against a later commit than the paper's; the repository's README names
tag v0.0.1 as the reproducing version." In §8.1, use HORA as the *counter*-example — the one
repository that discloses the gap — rather than as evidence for the gap.

### 13. major — the `penspin_2024` tactile charge may be reading the student-stage config

**location**: §5.8, "`penspin_2024` zeroes the disturbance force its appendix describes and disables
the tactile observation channel."

**the problem**: PenSpin's paper puts tactile in the *oracle* observation and trains a
proprioception-only student. The released config's observation is 96-dimensional with
`enable_tactile: False` *and* no point cloud — which is the student's observation, not the oracle's.
That is consistent with the paper, not against it.

**the evidence**: `papers/notes/penspin_2024.md` line 11 — the paper's oracle takes "binary tactile
c_t (20 sensors…), fingertip positions p_t, pen pose+angular velocity w_t, point cloud of the pen
(∈ R^{100×3}, PointNet-encoded)"; the released cfg has `numObservations: 96` built from "a 96-dim
lagged buffer from noisy joint pos + current target (32) with optional tactile (32) + fingertip pos
(12) channels", i.e. 96 without tactile, fingertips or point cloud. Line 11 also says the student
policy is "30 steps of joint positions … and previous targets … only". The disturbance-force half
(`forceScale: 0.0`) does stand.

**the fix**: Check whether `AllegroHandHora.yaml` is the oracle or the student config before
asserting the tactile channel is disabled. If it is the student config, drop that clause and keep
only the disturbance force, and lower the confidence on the row.

The remaining accusations — `dextreme_2022` (action-delta penalty −0.25 in Table 2, −0.2 and −0.01
in the two shipped yamls, neither matching), `visual_dexterity_2022` (Eq. 8's penultimate-joint
penalty absent from `dexenv/envs/rewards.py`), `dexpoint_2022`, `unidexgrasp_2023`, `pddm_2019`,
`pianomime_2024` (2 weighted terms in Table 3 against roughly 5 summed at run time) — are supported
by their notes and should stand, with the caveat in finding 14.

### 14. major — §5.8 misdescribes what `pianomime_2024` zeroed

**location**: §5.8, "`pianomime_2024` hardcodes its energy and fingering reward terms to return
zero", placed under "Zeroed terms recur" next to PhysHOI.

**the problem**: PianoMime's paper does not claim an energy term or a fingering term. Table 3 lists
two terms, Key Press and Mimic. The dead energy and fingering functions are inherited from the
RoboPianist environment the method builds on. Zeroing a term you never claimed is the opposite of
the PhysHOI failure, and the juxtaposition implies otherwise.

**the evidence**: `papers/notes/pianomime_2024.md` line 31 — "paper's Table 3 lists exactly two
weighted terms (Key Press 2/3, Mimic 1/3); the actual environment code sums five terms (key press
×2, sustain, energy [dead, returns 0], fingering [dead, returns 0], forearm-collision) plus a
wrapper-added mimic term."

**the fix**: "PianoMime's Table 3 states two weighted terms; the environment it ships sums roughly
five unweighted ones, two of which are inherited stubs that return zero and a third (forearm
collision) that the paper never lists."

---

## C. Figure 4 — leaf predicates that assert properties they never test

`tools/make_flow_tree.py` lines 93-115 defines every leaf. Three of the largest leaves are selected
by a paradigm tag, then labelled with a claim the tag does not carry.

### 15. blocking — "PPO in a GPU simulator, privileged state, 32" tests none of those three things

**location**: `paper/figures/fig4_taxonomy.svg`, first leaf under "a reward function".

**the problem**: The predicate is `"RL" in paradigm and "distillation" not in paradigm`
(make_flow_tree.py line 95). Nothing checks the algorithm, the simulator, or whether the method uses
privileged state. The result misdescribes at least five of the 32 papers on the face of their own
rows.

**the evidence**, from `corpus/rows/`:
- `pistar06_2025`: `sim: None`, algorithm "RECAP: advantage-conditioned policy extraction on a
  flow-matching VLA", and its `dexterous_evidence` field says "two 6 DoF arms with parallel jaw
  grippers". Not PPO, not a GPU simulator, not a dexterous hand.
- `artigrasp_2023` and `graspxl_2024`: `sim: RaiSim`, a CPU simulator.
- `pgdm_2023` and `dexvip_2022`: `sim: MuJoCo`.
- `physhoi_2023`: Isaac Gym, but no privileged state — `papers/notes/physhoi_2023.md` gives the
  policy state as `s_t = [g_t, ĥ_{t+1}]` with a 2-layer MLP and no asymmetric critic. It is the
  *first* key printed under this leaf.

The survey's own §5.2.1 counts "Forty-three run their own experiments in a GPU-parallel simulator
from the Isaac family or Genesis" — a different quantity from this leaf's 32, computed from a
different field.

**the fix**: Either rename the leaf to what the predicate selects ("reinforcement learning, no
distillation stage, 32") or make the predicate test `sim` and a privileged-observation field and
report the smaller number that results. Do not print `physhoi_2023` and `pistar06_2025` under a
label that asserts privileged state and a GPU simulator.

### 16. major — "plus teacher-student distillation to vision, 23" contradicts §5.7

**location**: same figure, second leaf.

**the problem**: The predicate is `"distillation" in paradigm` (line 96). "To vision" is asserted of
all 23. §5.7 names the papers that actually distil into a vision student and there are five.

**the evidence**: §5.7 — "The first distils a privileged teacher into a vision student inside one
paper, which is `hora_2022`, `visual_dexterity_2022`, `rotateit_2023`, `robot_synesthesia_2023` and
`viserdex_2026`." The 23 in the leaf include `omnih2o_2024`, whose student is proprioception history
plus three VR goal points (`papers/notes/omnih2o_2024.md`, Method: "history instead of linear
velocity"), and `pianomime_2024`, whose generalist consumes an SDF goal representation and
proprioception (`papers/notes/pianomime_2024.md`, key tricks) — neither is a vision student. The
figure prints `pianomime 24` first under the leaf.

**the fix**: Rename to "plus teacher-student distillation, 23" and hang the "to vision" subset, with
its count of five, off it as an annotation.

### 17. major — "synthetic demonstration generation, 10" is the data-collection tag

**location**: same figure, fourth leaf under "a human demonstration".

**the problem**: The predicate is `"data-collection" in paradigm` (line 104). Of the ten rows it
selects, six are *real* human-data collection rigs, not synthetic generators.

**the evidence**: the ten are `cyberdemo_2024`, `dexcap_2024`, `deximit_2026`, `dexmimicgen_2024`,
`dexmv_2021`, `dexumi_2025`, `dexwild_2025`, `umi_2024`, `unidex_2026`, `videodex_2022`. `dexcap_2024`
is a wearable mocap backpack, `dexwild_2025` a wearable glove rig, `dexumi_2025` an exoskeleton,
`umi_2024` a hand-held gripper, `dexmv_2021` and `videodex_2022` human video. The survey's own §5.7
names the synthetic generators correctly and gets three: "The third generates data without
reinforcement learning at all, which is `dexmimicgen_2024`, `dex1b_2025` and `deximit_2026`" — and
`dex1b_2025` is not even in this leaf.

**the fix**: Split into "human data-collection rig, 6" and "synthetic demonstration generation",
with the latter's membership taken from §5.7's list rather than from the tag.

### 18. major — the "a human demonstration, 49" branch count double-counts

**location**: same figure, second branch; `make_flow_tree.py` line 100,
`par.get("BC",0)+par.get("diffusion",0)+par.get("flow",0)`.

**the problem**: These three tags overlap heavily, so the branch prints a sum where it needs a union.

**the evidence**: recomputed from `corpus/rows/*.json` — the union of rows carrying any of `BC`,
`diffusion` or `flow` is **44**, not 49. The sum 27 + 14 + 8 = 49 double-counts every row tagged
both `BC` and `diffusion` (e.g. `dp3_2024`, `dexora_2026`) and both `VLA` and `flow`.

**the fix**: `len({r["key"] for r in M if {"BC","diffusion","flow"} & set(r["paradigm"])})`. The
figure's caption already says counts are recomputed from `corpus/rows`, so this one is a
straightforward bug, and it is the only branch of the four computed as a sum.

### 19. major — the "human reference, tracked with physics" branch and its leaves hold different papers

**location**: same figure, third branch (count 12, from the `track-human-ref` task family).

**the problem**: One paper appears in a leaf without being in the branch; three papers are in the
branch and in no leaf.

**the evidence**: the twelve `track-human-ref` rows are `dexmachina_2025`, `dexman_2025`,
`dexplore_2025`, `dextrack_2025`, `human2sim2robot_2025`, `humanplus_2024`, `maniptrans_2025`,
`objdex_2024`, `omnigrasp_2024`, `omnih2o_2024`, `physhoi_2023`, `toporetarget_2026`. The leaves
(lines 107-110) place `pgdm_2023` under "object trajectory only", but `pgdm_2023`'s task family is
`['grasp', 'functional/tool']` — it is not one of the twelve. `dexman_2025`, `humanplus_2024` and
`omnih2o_2024` appear in no leaf.

**the fix**: Either add the three missing papers to leaves or state the leaf coverage
(10 of 12 shown). Move `pgdm_2023` out, or widen the branch predicate and restate 12.

### 20. major — two more arithmetic gaps in the same figure

- "a reward function, 53" is the `RL` tag, which excludes the six `RL+demo` rows — yet
  "seeded by demonstrations, 6" hangs under it as a leaf. `pianomime_2024` (`['RL+demo',
  'distillation']`) is drawn under this branch twice and counted in it zero times.
- "no learned policy, 11" is `trajopt` 6 + `MPC` 5, but its three leaves hold one paper each. Eight
  papers in that branch are invisible. The figure's own specification comment (§5, item 5) asks for
  scarcity to be legible; as drawn it is the opposite — the branch looks like eleven papers and is
  three.

**the fix**: Make the branch count the union of its leaves, or print "3 of 11 shown".

### 21. minor — the "egocentric video, no robot at all, 7" leaf is a different seven from §5.3.3's

**location**: figure 4 versus §5.3.3.

**the evidence**: the leaf's membership (line 103) is `videodex_2022, dexvip_2022, okami_2024,
egozero_2025, egomimic_2024, hudor_2024, wm_dex_human_videos_2025`. §5.3.3's seven are `dexmv_2021`,
`videodex_2022`, `dexvip_2022`, `okami_2024`, `human2sim2robot_2025`, `hudor_2024`,
`wm_dex_human_videos_2025`. Two papers differ in each direction. Worse, the figure's set includes
`egomimic_2024`, whose `hand` field reads "parallel-jaw gripper (not a dexterous hand; see note
scope flag)" and which §6 itself lists among the four papers with "no dexterous hand at all".

**the fix**: Drive the leaf from the same list §5.3.3 uses and drop `egomimic_2024`.

---

## D. Table 5, cell by cell

I checked all nine families for `dextreme_2022`, `hora_2022`, `visual_dexterity_2022`,
`dexpbt_2023`, `penspin_2024` and `eureka_2023` against the notes and `corpus/reward_matrix.json`.
`hora_2022` is exactly right (pose/objvel/handpose/effort all `both`, five terms, matching
`papers/notes/hora_2022.md` line 44-52). The rest have a common defect.

### 22. blocking — three `code` marks are terms with a shipped weight of zero

**location**: `paper/tables/table5_rewards.md` — `dextreme_2022` drop = `code`; `dexpbt_2023`
drop = `code`; `penspin_2024` action rate = `code`.

**the problem**: In each case the term exists in the code but every shipped config sets its weight
to zero. The table's own key says `code` means "it is in the released code and not in the paper's
stated reward", which a reader takes as "the code optimises this and the paper does not say so."
This also contradicts §5.8's own rule: "A term that is present and zeroed is worse than a term that
is missing."

**the evidence**:
- `papers/notes/dextreme_2022.md` line 66: "Code has a `timeout_rew = timed_out * 0.5 *
  fall_penalty` term not listed anywhere in paper Table 2 (**evaluates to 0 given `fallPenalty: 0.0`
  in both configs**, so numerically inert…)", and line 67 notes the paper's absence of a fall row is
  "consistent with the code's zero setting."
- `papers/notes/dexpbt_2023.md` line 66: "`fallDistance: 0.24` and `fallPenalty: 0.0` (i.e. the
  configured fall penalty is zero)".
- `papers/notes/penspin_2024.md` line 19: released cfg `action_penalty_scale: 0.0`.

**the fix**: Add a fourth mark — `code (zero)` — or blank these three cells. `dextreme_2022`'s term
count of 6 and the derived family counts should be re-derived after the change.

### 23. major — `visual_dexterity_2022`'s contact cell carries the survey's headline finding and is
the wrong kind of contact

**location**: table 5, `visual_dexterity_2022` contact = `both`; §5.2.2, "only four mention contact
or force at all. That last number is the finding."

**the problem**: The term is a penalty on the *object touching the table*, and it is switched off in
every released config. It is not a hand-object contact or force term, which is what the sentence
around it is about.

**the evidence**: `papers/notes/visual_dexterity_2022.md` line 51 — "The only contact-related reward
term penalizes **object-table contact** in the in-air variant (Eq 7 / `pen_tb_contact`+`tb_cf_scale`),
which is a task-shaping term (discourage using the table), not a penetration penalty"; line 48,
mismatch (4) — "`pen_tb_contact` defaults to `False` in the released `dclaw.yaml`; no separate
shipped config with it set `True` … appears in the parsed files." The other three contact cells
survive: `anyrotate_2024`'s good/bad fingertip-contact terms and `poise_2026`'s friction-cone
wrench-margin term are both genuine (notes lines 44-45 and 39-40 respectively).

**the fix**: Mark the cell `paper` with a footnote naming it as an object-table contact term, and
change the headline to "Three of 21 put a hand-object contact or force quantity in the reward; a
fourth penalises the object touching the table, in a variant its released configs disable."

### 24. major — the `eureka_2023` row reads a method's reward off one appendix example

**location**: table 5, `eureka_2023` marked `paper` for goal tracking, object velocity and
finger-object distance, with an empty term count and `code: yes / mismatch: yes`.

**the problem**: Eureka has no published reward. GPT-4 writes a different one every run. The three
cells come from two illustrative listings in Appendix G, which the matrix's own provenance field
admits.

**the evidence**: `corpus/reward_matrix.json`, `eureka_2023` row: `"src": "Method, App. G.1/G.2
LLM-authored rewards; generated code not checked into the repo"`. `papers/notes/eureka_2023.md`
line 48 describes G.2 as an example "offered by the authors specifically to show EUREKA discovering
reward structures that run counter to human intuition" — an illustration chosen for being atypical.

**the fix**: Blank Eureka's family cells and add a row footnote: "reward is generated per run; the
appendix examples are illustrations, not a specification." Same treatment for `dreureka_2024`,
whose reward is a prompt (§5.2.3 says so) and which the table gives four `paper` marks.

### 25. minor — no family covers the "keep the object in the hand" distance term

`dextreme_2022`'s second-largest weight is "Position Close to Fixed Target, `||p_object − p_goal||`,
weight −10.0, Encourage the cube to stay in the hand" (`papers/notes/dextreme_2022.md` line 38), and
it maps to none of the nine families, so it disappears from the matrix while the footer reports
"97 of 189 term cells (51%) are families the method does not use." Several other rows have the same
term. Add an "object position / retention" family, or say in the caption that the nine families are
not exhaustive and name what falls outside.

---

## E. Related-work mentions read as the method's own choice

I looked specifically for this and found the corpus discipline is good — the notes consistently
flag delegation (`cyberdemo_2024`'s retargeting cell literally reads "delegated entirely to the
cited third-party teleoperation system; CyberDemo does not desc…"). Two things leak through.

### 26. minor — table 6's `ace_teleop_2024` cell contradicts §5.3.1's use of it

§5.3.1 says `ace_teleop_2024` is one of four systems using DexPilot's fingertip-vector formulation.
That is right — `papers/notes/ace_teleop_2024.md` line 13 quotes ACE's Appendix B Eq. 2 as
"identical formulation to anyteleop_2023". But table 6's "retargeting objective" cell for
`ace_teleop_2024` describes only the *wrist* mapping ("scale-and-recenter IK transform"), so the
column the text leans on does not contain the objective the text cites. Put the hand retargeting in
the cell, and note that ACE's contribution is the wrist layer — its own note says "ACE's own
contribution is entirely in the wrist/end-effector control-mapping layer".

### 27. minor — three rows in table 6 are not systems for getting human motion onto a hand

`pgdm_2023` (pre-grasps fitted by IK from a dataset, no operator), `dexvip_2022` ("no live operator;
a consensus hand pose is mined offline") and `cyberdemo_2024` (retargeting delegated to a cited
system) are counted among "the 30 corpus rows that describe a system for getting human motion onto a
robot hand" and in the denominators built on it. Either say the table covers human-to-hand
correspondence of any kind, including offline, or drop the three and recount 12/30 latency and
7/30 cost.

---

## F. Section 6 — denominators that move between sections

### 28. major — the 25-paper denominator includes benchmark and dataset rows it says it excludes

**location**: §6.2, "The denominator is the 25 corpus papers whose notes place a learned controller
on two dexterous hands. Datasets, static grasp synthesis and the two-gripper papers are excluded."

**the evidence**: the sentence that follows names `robopianist_2023` (`class: benchmark`),
`rp1m_2024` (`class: dataset`), `humanoidgen_2025` (`class: dataset`) and "all four `bench2dex_2026`
baselines" (`bench2dex_2026` is `class: benchmark`) as members of the 19. Counting a benchmark's four
re-run baselines as four of twenty-five papers is not a defensible denominator for "the field is
concentrated on one architecture", because those four baselines were chosen by the benchmark's
authors, not by four independent research groups.

**the fix**: State the denominator as method rows, recount, and report the benchmark's baselines as
one row with a note.

### 29. major — figure 5 places `dexterous_handover_2025` in the 25 although §6.5 says its row is
`bimanual: no`

`corpus/rows/dexterous_handover_2025.json` has `bimanual: false`. §6.5 says so explicitly: "its row
in Table 7 accordingly records `bimanual: no`." `paper/figures/fig5_bimanual.svg` nonetheless lists
it as one of the two papers in the "leader and follower, 2 of 25" panel. Pick one. If it stays in
the panel, the panel's own caption text ("whose leader is a scripted arm and is never learned")
already concedes it is not a two-policy bimanual system.

### 30. major — §6.2 and §8.8 give incompatible counts for the same fact

§6.2: "Nineteen of 25 use one policy over both hands … Five of 25 give each hand its own network."
§8.8: "Of the 12 that describe a learned controller, 9 are a single policy over a concatenated
two-hand observation" and "`bidexhd_2024` is the one decentralised design." Nineteen of 25 and nine
of 12 are different fractions of different populations, and "five of 25 give each hand its own
network" versus "the one decentralised design" is a flat contradiction — §6.2 names five
(`bidexhands_2022`, `bidexhd_2024`, `artigrasp_2023`, `dynamic_handover_2023`, `dydexhandover_2025`)
and §8.8 names one. Fix by deriving both sections from one list and citing it once.

### 31. minor — §6.2's enumeration does not reach 19

The list names eleven papers plus "all four `bench2dex_2026` baselines" — fifteen. Figure 5 says
"and 13 more" against six named, which is consistent with 19. Either complete the list or write
"among them".

---

## G. Generalist policies and hands (priority 5)

### 32. major — "largely not evaluated on hands" is contradicted by the survey's own rows

**location**: §8.5 heading, "Generalist policies are largely not evaluated on hands."

**the problem**: Of the 16 `VLA` method rows, five report no dexterous-hand result. Eleven do. The
heading asserts the opposite of the corpus.

**the evidence**: `dexterous_hand_evaluated` is present on 13 rows: 8 true, 5 false — which §5.5
states correctly. The three VLA rows not scored on that field are `gr_dexter_2025`, `unidex_2026`
and `egoscale_2026`, and §5.5 itself says all three "evaluate on hands". 8 + 3 = 11 of 16.

**the fix**: Retitle to what the evidence supports — "Generalist policies that do use hands use
small ones, and five report no hand result at all" — and move the DoF comparison to the front, since
it is the claim that holds.

### 33. major — the "eight" denominator excludes the two counterexamples that would break the claim

**location**: §5.5, "None of the eight evaluates on the 16 to 24 actuated degrees of freedom that
the reinforcement learning literature of section 5.2 runs on."

**the problem**: True of the eight *scored* rows, but the next sentence concedes `gr_dexter_2025`
reports a 21-DoF ByteDexter V2, and `corpus/rows/egoscale_2026.json` gives `hand_dof: 22` (Sharpa
Wave). Both are VLA rows. The claim survives only because those two were not scored on the field the
denominator is built from.

**the evidence**: recomputed `hand_dof` over the 16 VLA rows: `gr_dexter_2025` 21, `egoscale_2026`
22, `dexora_2026` 12, `metis_2025` 6, `dexgraspvla_2025` 6, `being_h05_2026` 6, `being_h0_2025` 6.
Median 6 — so §8.5's median is right — but three of seven are 12 or above and two are in the 16-24
band the sentence says none reaches.

**the fix**: "Of the eleven generalist rows that evaluate on a hand, seven state a DoF count: four
are six, one twelve, and two are 21 and 22. The median is 6 against 16 for the RL rows, and 34 of
the 44 RL rows that state a count are 16 or above." Then the contrast is real and no denominator
has to be held still.

### 34. minor — §5.5 and §8.5 report different numbers for the same Gemini Robotics 1.5 claim

§5.5: "reports Apollo progress scores of 0.74, 0.73, 0.66, 0.62 and 0.63 by generalisation axis."
§8.5: "does report Apollo quantitatively, at success rates of 0.64 down to 0.40 across five
generalisation axes." Both are correct — `papers/notes/gemini_robotics_15_2025.md` line 33 gives
progress scores 0.74/0.73/0.66/0.62/0.63 (Fig. 3) and success rates 0.64/0.64/0.56/0.51/0.40
(Fig. 35) — but a reader sees a contradiction. Name the metric in both places.

---

## H. Two smaller items

### 35. minor — `aloha_act_2023` is filed under "What the released code says" but involves no code

§5.8: "`aloha_act_2023`'s Algorithm 1 says the reconstruction loss is MSE and its Section IV.C says
L1." That is a paper disagreeing with itself, and `corpus/rows/aloha_act_2023.json` classes it
`internal-inconsistency`. Move it out of §5.8 or retitle the paragraph. (`dp3_2024`, by contrast, is
classed `internal-inconsistency` but the cited evidence — "its shipped config sets
`prediction_type: sample`" — is a code fact; that row is misclassed the other way.)

### 36. minor — the census is over method rows only, and at least one clean case falls outside it

`robopianist_2023` carries a documented, undisclosed reward-term mismatch — "the code's
`CompositeReward` sums 5 terms by default … vs the paper's Table 2 documenting only 3 … sustain_reward
and forearm_reward exist in code but are undocumented" (`corpus/rows/robopianist_2023.json`) — but
its class is `benchmark`, so it is outside the 110 and outside the 37 and the 16. §6.1 nonetheless
uses exactly this fact ("`robopianist_2023` ships a forearm-forearm collision term that its own
reward table never lists"). Say in §8.1 that the census covers the 110 method rows only, so "sixteen
is a floor" for a second reason besides the unreleased 49.

### 37. minor — §5.3.1's "four orders of magnitude" of latency compares different quantities

"Latency, where reported, spans four orders of magnitude, from `dexpilot_2020`'s 'about one second'
to `holo_dex_2022`'s 'under 100 milliseconds' to `geometric_retargeting_2025`'s 1 kHz retargeting
step." One second is an end-to-end pipeline figure; 1 kHz is the inference rate of one stage.
Table 6's own `anyteleop_2023` cell keeps them apart — "26-35 ms hand pose, 9-10 ms retargeting
(Table II); no end-to-end figure" — and `geometric_retargeting_2025`'s note gives a 3.2 s task
completion time on the same rig. The spread is partly an artefact of mixing the two. Split the
column, or say "end-to-end where stated, per-stage otherwise, and the two are not comparable."

### 38. minor — §5.4's "eight dexterous-hand trackers" excludes a dexterous-hand tracker

"Twelve method rows carry the `track-human-ref` task family, and eight of them are dexterous-hand
trackers rather than whole-body humanoid controllers." `dexman_2025` is one of the twelve and is a
two-hand Isaac Gym tracker — `corpus/rows/dexman_2025.json`, "PPO (RL_GAMES) residual policy on top
of IK-retargeted human motion", `task_family: ['track-human-ref','bimanual-coord']` — and §6 treats
it as a dexterous bimanual method throughout. Either it is a ninth tracker or say why it is
excluded.

---

## Summary

Section 5.4, 5.6 and 6.5 are sound. Section 5.2.2's arithmetic against table 5 is sound. The
central claim of §5.8 — that printed reward tables should be treated as hypotheses about the code —
is worth making and `physhoi_2023`, `dextreme_2022`, `visual_dexterity_2022`, `unidexgrasp_2023`,
`dexpoint_2022`, `pddm_2019` and `pianomime_2024` support it. But seven of the sixteen accusations
do not survive contact with the evidence the survey itself filed, and two of those seven are
refuted by the accused repository's own README. Fix those, fix figure 4's leaf predicates, and the
section is much stronger for being smaller.
