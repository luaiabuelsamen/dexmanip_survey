# V1 — verification of the revision against R2 (simulation) and R3 (methods)

Scope: not a fresh review. I checked whether the corrections R2 and R3 demanded were made, whether
the corrected text is right against the sources, and whether the repair introduced new errors.

Read: `reviews/r2_simulation.md`, `reviews/r3_methods.md`, `paper/sections/04_simulators.md`,
`paper/sections/05_training.md`, `paper/sections/08_gaps.md`, plus — because the corrected text
leans on them — `paper/figures/fig3_sim_step.svg`, `paper/tables/table4_simulators.md`,
`paper/tables/table5_rewards.md`, `paper/sections/07_evaluation.md` §7.3, `papers/notes/` for
`mujoco_2012`, `mujoco_convex_contact_2014`, `contact_models_comparison_2023`,
`castro_sap_contact_2021`, `dojo_2022`, `comfree_sim_2026`, `physics_engine_comparison_2015`,
`isaacgym_2021`, `physhoi_2023`, `dexpbt_2023`, `dextreme_2022`, `visual_dexterity_2022`,
`penspin_2024`, `omnih2o_2024`, `pianomime_2024`, `dexpoint_2022`, `unidexgrasp_2023`,
`pddm_2019`, `code/md/isaacgym_2021.md`, and all 218 `corpus/rows/*.json` recomputed.

---

## 1. R2's seven blocking mechanism errors

### B1. Soft contact is not a penalty spring — **fixed, and correct**

§4.2 now reads: "This is not a penalty spring, and depth is not always non-zero. The impulse
solves a regularised convex program over the whole contact set rather than a per-contact function
of the gap, both MuJoCo papers reject spring-dampers by name, and the 2012 ball-drop figure is
captioned 'there is no penetration'." All three supports check out:
`mujoco_convex_contact_2014.md:42` ("We soften all constraints, in a way that avoids instabilities
and unrealistic penetrations associated with earlier spring-damper methods"), `mujoco_2012.md:44`
("the modern velocity-stepping approach which avoids the difficulties with spring-dampers"),
`mujoco_2012.md:48` (Fig. 2 caption). The figure bullet was rewritten to match.

**The new claim "depth = normal load × compliance" is right**, and is better supported than R2
realised. `castro_sap_contact_2021.md:15` gives Drake's normal law γ_n = (k(φ − τ_d v_n))_+·δt̄
with "c = k⁻¹ is the compliance", i.e. steady-state φ = γ/(k δt̄): depth is force times compliance.
`contact_models_comparison_2023.md:19` describes MuJoCo's R as "a diagonal regularization matrix
acting like a numerical/physical spring". Zero at zero load follows from the same algebra.

**The mass-independence claim is right; its stated mechanism is an inference beyond the notes.**
`mujoco_convex_contact_2014.md:20` states the result explicitly ("penetration depth is derived in
closed form and shown to be independent of the object's mass") and records that the closed form
did not survive the PDF parse. The survey quotes the result and admits the algebra is missing —
correct discipline. But the sentence that explains it, "Mass cancels because the regulariser is
scaled by the inverse effective inertia at the contact, so compliance falls as 1/m exactly as the
gravity load rises as m" (04_simulators.md:73), appears in no note. It is physically right for
MuJoCo (the diagonal solver's "mass-aware spring-damper ... uses the diagonal of the A matrix",
`mujoco_2012.md:19`, A being the inverse effective inertia), so it is not an error, but it is an
unlabelled inference in a section whose own rule is that every label needs a citation. Half a
sentence of hedging would settle it.

### B2. The iteration budget was the wrong mechanism — **fixed in structure, one new overclaim**

§4.1 now names three sources that "do not answer to the same knob" (step, prescribed compliance,
truncation), drops "stiff contact" as the trigger, and says truncation degrades "with conditioning
and redundancy, not stiffness", which `contact_models_comparison_2023.md:28-29` supports exactly
(jamming on hyperstatic problems, non-convergence on the 10³:10⁻³ kg stack, ADMM/staggered/Newton
robust). Figure 3's bullet was split into the three, in R2's order.

**New error: "the biggest term for a hand" is asserted, unsourced, and is refuted by the survey's
own Dojo row.** The figure now says "The step, and the biggest term for a hand. Non-penetration is
enforced at the velocity level, so any residual approach velocity is integrated into overlap of
order v·Δt." Three problems.

- *Universality.* Dojo is in Table 4 and does not behave this way: `dojo_2022.md:20` records
  +1e-12 mm at Δt = 0.1 s, +1e-7 mm at 0.01 s, +8e-6 mm at 0.001 s — feet above the floor at every
  step tested, because the NCP enforces the gap at the next configuration rather than the
  velocity-level residual. §4.2 quotes that same fact two paragraphs later. The claim holds for
  the velocity-stepping engines it is about; stated of "every engine", it is contradicted inside
  the survey.
- *Dominance.* v·Δt overlap is an impact transient at contact acquisition; a contact that is
  already loaded and held has v_approach ≈ 0 and rests at the compliance. §4.2 uses precisely that
  distinction to refuse Dojo's −28/−46 mm as "an impact transient on a drop ... not a steady-state
  grasp depth". Ranking the same kind of transient first for a hand, with no measurement behind
  it, is the survey arguing both sides. It is defensible for in-hand reorientation, where contacts
  are made and broken continuously — but that argument has to be made, not assumed.
- *Provenance.* The 4 mm illustration is arithmetically right (0.5 m/s ÷ 120 Hz = 4.2 mm) and the
  1/120 s Shadow Hand step is confirmed (`isaacgym_2021.md:21`), but 0.5 m/s is R2's assumed
  fingertip speed and appears in no source. Label it as an illustration.

**Second new error in the same bullet block:** "The depth is a setting, and no engine paper in
Table 4 states the setting it ships" is false for a Table 4 row. `comfree_sim_2026.md:19` records
ComFree-Sim's stated defaults, "the identical (r_min, r_max, w, m, p) = [0.9, 0.95, 0.001, 0.5,
2.0] default hyperparameter API as MuJoCo's own solver", and its k_user/d_user sweep prints the
setting beside the resulting depth. §4.2 praises exactly that. Restrict the clause ("no engine
paper in Table 4 other than ComFree-Sim").

### B3. "MuJoCo sits outside that taxonomy" — **fixed, and correct**

§4.2: "MuJoCo is inside that taxonomy rather than outside it. Le Lidec et al. classify it as
CCP-MuJoCo, a convex relaxation solved by a Newton method on the primal QCQP, in the same family
as CCP-Drake, the SAP-style scheme (Table III)." Matches `contact_models_comparison_2023.md:15`
verbatim in substance. The two-errors-of-opposite-sign sentence and the SAP gliding quote
("unfortunately does not go away as δt → 0") match `castro_sap_contact_2021.md:40`. "Outside that
taxonomy" and "the convex middle" are gone. One looseness: the compliance-induced overlap is not
itself part of the CCP Signorini relaxation — Le Lidec treats MuJoCo's R as an added numerical
trick (`:19`, `:45`) — so "the relaxation makes two errors" bundles two distinct mechanisms under
one noun. Not wrong enough to block.

### B4. PhysX in the LCP family in 4.2, out of it in 4.3 — **fixed, and correct**

§4.2 now separates model from algorithm in the two sentences R2 drafted, cited to `isaacgym_2021`
Sec. 3, and §4.3's "rather than a classical PGS or LCP scheme" is gone ("PhysX resolves contacts
with the Temporal Gauss-Seidel sweep described above"). The TGS description matches
`isaacgym_2021.md:19,51`. Table 4's `isaacgym_2021` solver cell still says "not classic PGS/LCP",
which is now a statement about the algorithm only and no longer contradicts the text.

### B5. "Engines do not expose penetration depth" — **fixed in §4.2, §8.2, §1 and §9; NOT fixed in §7.3**

See item 2 below for the code. §4.2's claim is now the corrected one ("The column records whether a
parsed source reported a penetration depth, not what an engine can compute ... The depth is
computable from the poses and the meshes in a few lines of Warp, and the field's own benchmark
repository already does it"), §8.2 opens "The engines are not the obstacle", §9 says "The obstacle
is not the engines", §1 carries the reporting version. "The depth is created by the solver on
every step and is not handed to the user" is gone.

**But `paper/sections/07_evaluation.md:364` still reads: "Simulators would have to expose
penetration to code outside the reward, which Table 4 records that only some do."** R2's fix (c)
was to delete that sentence outright; `reviews/FINAL_CONSISTENCY.md:4` records the same
requirement. It survives as one of §7.3's "four things would have to change", so the survey now
asserts the barrier in §7.3 and denies it in §4.2, §8.2, §1 and §9. This is the single most
important outstanding item, because §7.3 is where the prescription lives.

Two lesser parts of R2 #5 are also unfixed: Table 4's column is still headed "penetration exposed"
(the prose redefines it instead of the header being renamed), and
`corpus/rows/isaacgym_2021.json` still carries `penetration_exposed: false` with no review field,
while the text says the code parse contradicts it. The row fields carry `mismatch_review` notes
elsewhere; this one deserves the same treatment.

### B6. The Erez/Dojo bargain — **cut, but the replacement carries two new errors**

The priced-trade sentence is gone. The replacement is "What the regularisation buys is
conditioning, which is what lets a hyperstatic grasp run at a large step. It does not buy the step
with overlap, and the depth it costs is tuned separately. Erez's contact-free planar chain settles
that. MuJoCo runs at 243.2 kHz there against Bullet's 22.8 and PhysX's 6.4, and Bullet's
articulated Featherstone mode at 81.4 kHz beats every Cartesian-coordinate engine ... Joint
coordinates explain the timestep advantage and contact compliance cannot."

- **Wrong: "six orders of magnitude".** §4.2 says "Drake's SAP bound of 2.5×10⁻⁵ m at δt = 10⁻² s
  is six orders of magnitude below Dojo's MuJoCo cell at the same step". Dojo's cell at that step
  is −28 mm = 2.8×10⁻² m (`dojo_2022.md:20`). 2.8×10⁻² / 2.5×10⁻⁵ ≈ 1.1×10³ — three orders, not
  six. (At the other step it is 4.6×10⁻² / 2.5×10⁻⁷ ≈ five orders.) R2 made this arithmetic error
  in its own "the fix" text and the revision copied it. The point survives at three orders.
- **Wrong in kind: the SAP number is quoted against its note's explicit prohibition.**
  `castro_sap_contact_2021.md:46`: "The near-rigid penetration estimate (2.5×10⁻⁵ m at δt=10⁻²s
  ...) is an analytical bound for a single point mass on a plane, not a measured penetration depth
  in a hand-object grasp; it should not be quoted as a general Drake grasp-penetration number."
  The draft sets it against an Atlas humanoid drop as evidence that "the depth is a setting". A
  point-mass analytical bound and a 31-body drop transient differ in load, effective inertia and
  regime — the same objection the draft correctly makes against the ComFree-Sim 5 cm primitives
  one paragraph later. Either state the condition ("an analytical bound for a point mass at rest")
  or drop the comparison.
- **Internal contradiction:** "the regularisation buys conditioning, which is what lets a
  hyperstatic grasp run at a large step" and "Joint coordinates explain the timestep advantage and
  contact compliance cannot" are two sentences apart and say opposite things. The planar-chain
  numbers are *throughput* in kHz on a contact-free system (`physics_engine_comparison_2015.md:26`),
  not a largest-stable-timestep result; the grasp-timestep table is a different experiment, and
  BulletMB was never run on it. `physics_engine_comparison_2015.md:73` reads the grasp result the
  opposite way: "large timesteps are tolerable specifically because penetration is absorbed
  softly". So "settles that" overstates what a contact-free speed test can settle. This is the one
  place where a wrong mechanism has been swapped for another wrong mechanism, and it should be
  rewritten as: the coordinate formulation explains the contact-free speed advantage; the grasp
  timestep is a contact result and Erez's data do not attribute it.

### B7. DeXtreme's calibration failure inverted — **fixed, and correct**

§4.6 now matches R2's wording and the source. The verbatim quote is preserved and checks against
`dextreme_2022.md:70`; the inference ("the interpenetration the engine does not expose is also
what blocks the calibration") is gone and replaced by the replay-is-placement reading.

Other R2 items I looked at in passing: #8 ("four of the five engines" — fixed, with both stated
caveats), #9 (all four figure labels fixed: symplectic Euler for Brax, RK4 attributed to MuJoCo,
"primitives vs planes" for Dojo, "soft, elliptic cone" for MuJoCo, "libccd, islands" for Genesis),
#10 (convex decomposition moved out of "where penetration comes from", both signs stated, SDF
exception added), #11, #12, #13 (prose fixed; column still headed `dt s`), #14, #17 (see item 3),
#18, #20, #21, #22, #23 all fixed. **#16 is not done**: Table 4 still marks `newton_2025` as
`diff. = yes` against its note's explicit warning.

---

## 2. What `code/md/isaacgym_2021.md` actually contains

I read the parse rather than trusting the citation. The repository is IsaacGymEnvs
(`corpus/code_manifest.json`, commit `aeed2986`), i.e. NVIDIA's own released benchmark code.

What is *in the parse*:

- A module docstring (line 8804): "IndustReal: algorithms module. Contains functions that implement
  Simulation-Aware Policy Update (SAPU), SDF-Based Reward, and Sampling-Based Curriculum (SBC)."
- Signatures only (lines 8806-8823): `load_asset_mesh_in_warp(urdf_path, sample_points,
  num_samples, device)`, `get_max_interpen_dists(asset_indices, plug_pos, plug_quat, socket_pos,
  socket_quat, wp_plug_meshes_sampled_points, wp_socket_meshes, wp_device, device)`,
  `get_interpen_dist(queries, mesh, interpen_dists)`.
- One full function body (lines 8826-8862), `get_sapu_reward_scale`, which calls
  `get_max_interpen_dists` on the live sim poses, then:
  `low_interpen_envs = torch.nonzero(max_interpen_dists <= interpen_thresh)`,
  `high_interpen_envs = torch.nonzero(max_interpen_dists > interpen_thresh)`,
  `reward_scale = 1 - torch.tanh(max_interpen_dists[low_interpen_envs] / interpen_thresh)`,
  returning all three.
- Two configs: line 3630 `interpen_thresh: 0.001  # max allowed interpenetration between gear and
  shaft`; line 3753 `interpen_thresh: 0.001  # SAPU: max allowed interpenetration between plug and
  socket`. Isaac Gym units are metres, so the threshold is 1 mm.
- Two task docstrings (lines 9016, 9134): "Trains a gear insertion policy / peg insertion policy
  with Simulation-Aware Policy Update (SAPU), SDF-Based Reward, and Sampling-Based Curriculum."

What is *not* in the parse: the bodies of `get_max_interpen_dists` and `get_interpen_dist`, and the
call site that consumes the returned split and scale. So the strongest statement the parse
supports is: **a shipped NVIDIA Isaac Gym task computes, per environment and every step, a maximum
interpenetration distance between two meshed rigid bodies from their simulated poses, splits the
environments on a 1 mm threshold, and scales the reward of the surviving environments by
1 − tanh(depth/threshold).** The depth is recomputed geometrically from poses and meshes; it is not
a quantity the engine hands back. That distinction is the one the survey needs, and §4.2 states it
correctly.

The survey's rendering is right in substance and slightly ahead of the parse in two details:
"sample points on one, query them against the other" is read off argument names
(`wp_plug_meshes_sampled_points`, `queries, mesh, interpen_dists`) and the `load_asset_mesh_in_warp`
signature, not off a body; and "the policy update is gated on that number" is read off the SAPU
name and the returned env split, not off the caller. Both are sound inferences; say "the parse
shows the signatures and the thresholding; the point-sampling is named in the arguments". One
small slip: §4.2 attributes the plug/socket comment to "lines 3630 and 3753" — line 3630's comment
is the gear-and-shaft variant.

The two supporting counterexamples check out: `tactile_genesis_2026.md` App. A.1 records two
penetration-depth backends offered as sensors, and Table 4 does leave the Genesis penetration cell
blank. Table 4's cells are as the text describes them: 2 `yes` (Dojo, ComFree-Sim), 4 `no` (Brax,
Isaac Gym, Isaac Lab, Orbit), 9 blank.

**Verdict: the corrected claim is made and the evidence carries it — except in §7.3, which still
asserts the refuted version (see B5).**

---

## 3. R3's seven withdrawals, the corpus fields, and the ten that remain

### The seven named cases

All seven are gone from the text or requalified, and the six reclassifications are recorded in the
rows. `mismatch_class` now reads (recomputed over the 112 method rows): contradiction 10,
parse-limitation 13, code-absent 8, version-skew 4, internal-inconsistency 3.

| row | old | new class | `mismatch_review` | text |
|---|---|---|---|---|
| `maniptrans_2025` | contradiction/high | parse-limitation/low | yes | §5.8: "matches its own config, the differing values being a README example's override and an unused fallback" — correct |
| `eureka_2023` | contradiction | parse-limitation/low | yes | §5.2.3 rewritten to R3's sentence, incl. "its README documents the paper's budget ... as the default" — correct |
| `open_television_2024` | contradiction | code-absent/low | yes | accusation gone from the text entirely — correct |
| `dexmachina_2025` | contradiction | internal-inconsistency/low | yes | §5.8: "dexmachina_2025's multiplicative task reward, charged to its code in an earlier draft, is printed in the paper" — correct |
| `artigrasp_2023` | contradiction/high | parse-limitation/low | yes | §5.8: "whose two weight sets are the two phases of a curriculum the paper documents" — correct |
| `graspxl_2024` | contradiction/medium | parse-limitation/low | yes | §5.8 sentence replaced with R3's wording — correct |
| `dexpbt_2023` (DR half) | contradiction | contradiction/high, DR half withdrawn | yes | §5.2.1: "`dexpbt_2023`'s `randomize: False` is not a third case: it is the IsaacGymEnvs default and agrees with the paper" — correct, and matches `dexpbt_2023.md`'s closing bullet |

§8.1 names all seven and the reasons, and says the retractions are recorded in the rows. That is
done properly. Two residual problems:

- **Three reclassifications land in classes that do not fit, and inflate the 37/38 census.**
  `maniptrans_2025` and `eureka_2023` are not parse limitations: in both, the repository *does*
  settle the question, in the paper's favour (R3's evidence is the repo's own config and README).
  §5.8 files them under "In 13 rows the repository does not settle the question", which mislabels
  a settled non-discrepancy as an unsettled one. `dexmachina_2025` as `internal-inconsistency` is
  also strained — R3's defensible residue was an undisclosed `force_penalty` of 0.1, which is
  non-disclosure, not a paper contradicting itself. A `withdrawn` class, or removal from the
  census, would be honest; as it stands the withdrawn rows still count toward "thirty-seven ...
  record a discrepancy".
- **The arithmetic reads oddly.** 16 − 7 = 9, but the answer is 10 because the seventh withdrawal
  is half a charge. §8.1 does explain this; a reader will still stop. One clause would fix it.

### The ten remaining, checked against their notes

| row | conf | holds? |
|---|---|---|
| `physhoi_2023` | high | yes — see item 4 |
| `dextreme_2022` | high | yes. `dextreme_2022.md:63`: paper Table 2 −0.25, ADR yaml −0.2, ManualDR yaml −0.01, "Neither config file matches". The survey says exactly this |
| `visual_dexterity_2022` | high | yes. `:48` mismatch (1), penultimate-joint penalty (Eq. 8, c7=−2) absent from `rewards.py`; fallDistance 0.24 vs 0.15 across two shipped configs |
| `dexpoint_2022` | high | yes. `:64` — the code reward is not Eq. 5's four-term sum; three terms absent from the paper plus an IK-error penalty |
| `unidexgrasp_2023` | high | yes. `:37` — four additive terms with seven ω weights in Table 7 against nested `torch.where` gates with literal coefficients that "do not correspond one-to-one" |
| `pddm_2019` | high | yes. `:76-77` — the Baoding `-10*wrist_too_high` term is absent from Table 2. (The survey calls it a "wrist-height term"; the code gates on wrist *angle* past 0.15) |
| `pianomime_2024` | high | yes, and the R3 wording fix landed: two inherited stubs and a forearm term "the paper never lists" (`pianomime_2024.md:31`) |
| `penspin_2024` | medium | yes, narrowly. `forceScale: 0.0` against an appendix that describes a disturbance force at 0.2×mass with p = 0.25 (`penspin_2024.md:21`) is a genuine value contradiction. The tactile clause is now correctly hedged as the student's observation |
| `dexpbt_2023` | high | **no — should fall or be reclassified** |
| `omnih2o_2024` | medium | **doubtful — should be dropped from this census or explicitly scoped** |

**`dexpbt_2023`.** What survives the DR withdrawal is "sums eight components against the paper's
four" plus a zeroed `hand_delta_penalty`. §8.1 defines a contradiction as "the paper states one
value and the shipped code demonstrably states another". No value differs: §5.8 itself says "its
five named weights are present at their stated values", and `dexpbt_2023.md:63` confirms it. The
eight-vs-four is a grouping difference. So the row fails the survey's own class definition. Worse,
the survey's exculpatory clause is contradicted by its own note: §5.8 and
`corpus/reward_matrix.json` call `hand_delta_penalty` "a term the paper never claims", while
`papers/notes/dexpbt_2023.md` calls it "the paper's implicit 'moving away' penalty inside r_reach".
Either the paper claims it — and then the zeroing is a real PhysHOI-shaped contradiction and the
"never claims" clause is wrong — or it does not, and the row is not a contradiction. It cannot be
both. Pick one; on the note's own reading I would keep the row and delete the clause, but as
written the row is unsupported.

**`omnih2o_2024`.** The discrepancies are real (`omnih2o_2024.md`: stumble −0.00125 vs −1250;
max-feet-height +1000 bonus vs −2500 penalty; exp(−c‖·‖) vs exp(−err²/σ); curriculum threshold 40
vs 50), and the sign flip on feet height is not a typo signature even if the stumble weight is
(the ×1.25 curriculum factor reproduces four neighbours exactly). But the paper has no objects in
simulation and its "fingers are outside the policy and outside the reward" (`:17`, `:21`), so it is
evidence about humanoid locomotion reward reporting, not dexterous. R3 asked for that scoping
sentence; it is nowhere in §5.8 or §8.1. Keep it and say what it is, or drop it — as printed it is
one of ten numbers carrying a claim about dexterous manipulation.

**My count: 8 of the accusations survive** (physhoi, dextreme, visual_dexterity, dexpoint,
unidexgrasp, pddm, pianomime, penspin), 9 if `omnih2o_2024` stays with an explicit scope caveat.
The survey's "ten" is one or two too many.

### Collateral errors found in the three sections

These are not R2 or R3 findings; they are new or surviving defects in the revised text.

1. **The census total is 38, not 37, and `groot_n16_2025` is classified.** §5.8: "Thirty-seven of
   the 112 method rows record a discrepancy ... three are version skew ... An unclassified
   thirty-eighth, `groot_n16_2025`". The row now carries `mismatch_class: version-skew`,
   `mismatch_confidence: high` and a `mismatch_review`. Recomputed: 38 rows carry a class, of which
   4 are version-skew. `FINAL_CONSISTENCY.md:2` flagged this as untriaged; the corpus was triaged
   and the text was not updated. §8.1 repeats "three version skew".
2. **61 vs 62 inside §8.1.** "Sixty-one method rows released code that could be parsed" against
   "fifty method rows released nothing" (112 − 50 = 62) and §5.8's "the 62 rows that released
   anything". `code_released: true` on 62 method rows. `FINAL_CONSISTENCY.md:1` predicted exactly
   this; only §8.1 is stale.
3. **§5.2.2 says three Table 5 cells "are blank in it"; Table 5 prints `code (0)` in all three.**
   `paper/tables/table5_rewards.md` rows 7, 10 and 18 read `code (0)` for `dextreme_2022` drop,
   `dexpbt_2023` drop and `penspin_2024` action rate — which is R3's requested fourth mark, and
   which the same paragraph's opening sentence describes. The "blank" sentence contradicts both.
4. **§8.4 versus §5.5 on generalist DoF.** §5.5 adopts R3 #33 ("two are 21 and 22 ... Two
   generalist rows reach the band"). §8.4 still runs the old denominator: "The stronger claim, that
   no generalist reaches the 16-to-24 band, rests on those five stated counts alone, and
   `gr_dexter_2025` and `egoscale_2026` are excluded because neither settles the question." The two
   sections now assert opposite things about the same two papers. §8.4 also says "16 over the 44
   reinforcement-learning rows that state one"; recomputed, 48 of the 59 reward rows state a count
   (median 16, 38 at 16 or above), which is what §5.5 says.
5. **§5.5's own arithmetic does not close.** 18 VLA rows = "eleven evaluate on a multi-fingered
   hand" + "six report no hand result at all" = 17, with `groot_n16_2025` attached to the six in
   one sentence and excluded from the list of six two paragraphs later. Corpus:
   `dexterous_hand_evaluated` true 8, false 6, absent 4.
6. **Two engine counts are off by one.** §4.3 "Thirty-six of the 112 method papers ... run on it";
   I count 35 method rows whose `sim` names Isaac Gym. §4.2 "Those two simulators carry 42 of the
   112"; Isaac Gym plus Isaac Lab/Orbit is 41, reaching 42 only if `dexteleop0_2026` (Isaac Sim
   4.5) is counted as one of "those two".
7. Numbers I recomputed and found **correct**: the penetration split (85 not addressed / 16 null /
   5 constrained / 3 penalised / 3 measured over 112 method rows, so 11 of 96 — R2 #17 fully
   fixed, and §7.3/§8.2/§1 all use the same split); Table 4's 68 of 165 and 68 of 150; the 2/4/9
   penetration-column tally; Dojo's Table V cells with both standard deviations; ComFree-Sim's
   3.9 ± 6.9 → 0.9 ± 1.5 mm and MuJoCo Warp's 1.7 ± 4.9 mm; Erez's 16/2/0.25/0.03 ms and
   243.2/22.8/6.4/81.4 kHz; Isaac Gym's 1/120 s and 1/20 s OpenAI control step.

---

## 4. `physhoi_2023` as the flagship

**Stands, and the wording is now precise.** Checked line by line against
`papers/notes/physhoi_2023.md`:

- "hardcodes the body position-velocity error and both object rotation errors to zero, with the
  real computation commented out beside them" — `:134` confirms `epv` hard-set to
  `torch.zeros_like(ep)`, and the object rotation and rotation-velocity errors likewise, with the
  live computation commented out (R3 quotes lines 405, 422, 430 of the code parse).
- "unconditionally rather than per dataset" — correct, and it is what defeats the paper's own
  BallPlay exemption. `:135` gives Table 4's GRAB weights λ^or = 0.1, λ^orv = 0.01 against
  BallPlay's 0 and 0, so the zeroing is not covered by the dataset the paper exempts. §8.1 says
  this exactly.
- "non-zero weights of 0.1 and 0.01 for those rotation terms on GRAB" — correct.
- **R3's requested wording fix landed.** §5.8 now reads "tracking the *object* in position only,
  with body rotation and body rotation-velocity still live". `:134` confirms `rr` and `rrv` are
  computed normally; only the body *position-velocity* error is zeroed on the body side. The
  earlier "tracking position only" is gone.
- "its own position-only success criterion could not have caught that" — `:145`, Succ is defined on
  object and body position errors with no orientation threshold. Correct.
- 95.4 percent on GRAB — `:146`. Correct.

One asymmetry worth a word: §8.1's summary mentions only the two object-rotation zeroings, while
§5.8 also names the body position-velocity zeroing. Not an error; §5.8 is the complete one.

---

## Verdicts

| # | item checked | verdict |
|---|---|---|
| B1 | soft contact is not a penalty spring; depth = load × compliance; mass-independence | fixed (mechanism sentence is an unlabelled inference) |
| B2 | three sources of overlap, not the iteration budget | fixed |
| B2a | "the step ... the biggest term for a hand", stated of every engine | wrong (Dojo refutes universality; dominance unmeasured; 0.5 m/s unsourced) |
| B2b | "no engine paper in Table 4 states the setting it ships" | wrong (ComFree-Sim states it) |
| B3 | MuJoCo is CCP-family, same family as Drake SAP | fixed |
| B4 | PhysX: LCP model, TGS algorithm, stated once | fixed |
| B5 | engines do not hide penetration — §4.2, §8.2, §1, §9 | fixed |
| B5a | §7.3 "Simulators would have to expose penetration to code outside the reward" | not done |
| B5b | Table 4 column renamed; `isaacgym_2021.json` `penetration_exposed` flagged | not done |
| B6 | Erez/Dojo bargain cut | fixed |
| B6a | "six orders of magnitude" below Dojo's MuJoCo cell | wrong (three orders) |
| B6b | SAP point-mass bound quoted against its note's explicit warning | wrong |
| B6c | "regularisation buys the large step" vs "joint coordinates explain the timestep advantage" | wrong (self-contradictory; a speed test cannot settle a timestep claim) |
| B7 | DeXtreme replay: symptom, not cause | fixed |
| — | R2 #16, Newton `diff. = yes` | not done |
| 2 | Isaac Gym interpenetration evidence stated accurately | fixed (two details run slightly ahead of the parse; line 3630 mis-attributed) |
| 3a | `maniptrans_2025` withdrawn | fixed (class is wrong in kind) |
| 3b | `eureka_2023` withdrawn | fixed (class is wrong in kind) |
| 3c | `open_television_2024` withdrawn | fixed |
| 3d | `dexmachina_2025` withdrawn | fixed (class is strained) |
| 3e | `artigrasp_2023` withdrawn | fixed |
| 3f | `graspxl_2024` withdrawn | fixed |
| 3g | `dexpbt_2023` DR half withdrawn | fixed |
| 3h | `dexpbt_2023` retained as a contradiction | wrong (fails §8.1's own definition; "a term the paper never claims" contradicts its note) |
| 3i | `omnih2o_2024` retained without R3's scoping sentence | not done |
| 3j | census total 37 and "unclassified thirty-eighth" | wrong (38 classified; version-skew is 4) |
| 3k | §8.1 "sixty-one method rows released code" | wrong (62) |
| 3l | §5.2.2 "three cells ... are blank in it" | wrong (Table 5 prints `code (0)`) |
| 3m | §8.4 generalist DoF claim and its 44-row denominator | not done (contradicts the fixed §5.5; 48 rows state a count) |
| 3n | §5.5 eleven + six ≠ eighteen | wrong |
| 3o | §4.3 "thirty-six" Isaac Gym rows; §4.2 "42" | wrong (35; 41) |
| 4 | `physhoi_2023` flagship, and what was zeroed | fixed |

**Contradiction accusations that survive, by my count: 8** — `physhoi_2023`, `dextreme_2022`,
`visual_dexterity_2022`, `dexpoint_2022`, `unidexgrasp_2023`, `pddm_2019`, `pianomime_2024`,
`penspin_2024`. `dexpbt_2023` fails the survey's own definition of the class and `omnih2o_2024` is
a hands-outside-the-reward humanoid controller; with `omnih2o_2024` retained under an explicit
scope caveat the number is 9. The survey's "ten" is not supportable as printed.
