# R2 review: simulation, contact models, and the interpenetration thread

Scope: section 4 in full, Table 4, Figure 3 (`paper/figures/fig3_sim_step.svg`), and the
interpenetration thread wherever it runs (sections 1, 5, 7, 8). Checked against
`papers/notes/` for `mujoco_2012`, `mujoco_convex_contact_2014`, `contact_models_comparison_2023`,
`castro_sap_contact_2021`, `dojo_2022`, `comfree_sim_2026`, `isaacgym_2021`,
`physics_engine_comparison_2015`, plus `mujoco_playground_2025`, `mujoco_warp_2025`,
`newton_2025`, `genesis_2024`, `brax_2021`, `orbit_2023`, `isaaclab_2025`, `maniskill2_2023`,
`maniskill3_2024`, `tactile_genesis_2026`, `dextreme_2022`, `dextrack_2025`, and the code parses
`code/md/isaacgym_2021.md` and `code/md/isaaclab_2025.md`.

Sound and worth saying so before the objections: section 4.4 is the best-conditioned throughput
writing I have read in a survey. Every one of the four headline figures is quoted with what it
measures, the hardware, and what the source failed to state, and the Isaac Lab, ManiSkill3 and
Orbit conditions all check out exactly against their notes. Section 4.5 is accurate line by line.
The Erez grasp-timestep numbers, the Dojo Table II cells, the ComFree-Sim penetration cells, the
Drake SAP bound, the DexTrack config finding, and Table 4's own counts (3 timesteps, 4 iteration
counts, 7 hands, 68 of 165 cells empty) all reproduce from the notes and the rows.

The problems are concentrated in the mechanism claims, and they are serious. Figure 3's
"Where penetration comes from" box is the survey's one-paragraph theory of its own central
theme, and three of its four bullets are wrong about the engines the survey names.

---

## Blocking

### 1. Figure 3, bullet 1: soft contact is not a penalty spring, and depth is not "never zero"

**location** `paper/figures/fig3_sim_step.svg`, "Where penetration comes from": "Soft contact
admits penetration by construction: the contact force is a function of depth, so depth is never
zero." Echoed in 4.2: "penetration is a state variable rather than an error".

**the problem** The bullet describes a penalty / spring-damper contact model. MuJoCo, the engine
the thread is built on, is explicitly not one, and both cited MuJoCo papers say so in their
abstracts. The force is not a function of depth.

**the evidence** `papers/notes/mujoco_convex_contact_2014.md`, Abstract: "We soften all
constraints, in a way that avoids instabilities and unrealistic penetrations associated with
earlier spring-damper methods". `papers/notes/mujoco_2012.md`, Abstract: contact responses use
"the modern velocity-stepping approach which avoids the difficulties with spring-dampers". The
impulse is the solution of a regularised convex program over the whole contact set (Eq. 10-11,
GPGS), not a per-contact function of the gap. The same note records the opposite sign of the
survey's claim: the regulariser R lets contacts act "from a distance", by "increasing R with
distance" (Sec. II-D), so the violation coordinate can be positive, and `mujoco_2012`'s own
Fig. 2 caption for a ball drop reads "there is no penetration".

**the fix** State the actual mechanism, which is more useful than the slogan and is already
half-present in 4.2. In a regularised (compliant) formulation, the steady-state violation at a
contact is the normal load times the compliance: depth ≈ f_N · R. It is zero at zero load, it
grows with load, and it is a chosen number, not an inevitable one. Say why the 2014 closed form
is mass-independent, since that is the one fact that makes the point: MuJoCo scales the
regulariser by the inverse effective inertia at the contact, so the compliance falls as 1/m
exactly as the gravity load rises as m. Rewrite the bullet as: "A regularised contact admits a
violation proportional to the load it carries divided by the chosen stiffness. The depth is a
setting, not an error, and the engine will not tell you what you set it to."

### 2. Figure 3, bullet 2 and section 4.1: the iteration budget is the wrong mechanism

**location** `fig3_sim_step.svg`: "A fixed iteration budget leaves the constraint unconverged, so
a stiff contact under load is resolved as overlap." Section 4.1, final sentence: "the solver,
where a fixed iteration budget leaves a stiff contact unconverged and therefore resolved as
overlap."

**the problem** Three distinct sources of overlap are collapsed into one, and they do not behave
alike under the knob the figure names. In a regularised formulation more iterations converge to a
solution that still carries the prescribed depth, so the iteration budget does not reduce it. And
the dominant mechanism for a hand is missing from the figure entirely.

**the evidence** (a) Compliance: `mujoco_convex_contact_2014` Sec. V derives the steady-state
depth from ε and κ, with no dependence on the GPGS iteration count; the note records that the
same test was run at both 5 and 50 iterations (Fig. 3, Sec. VI-B) and reports only a cost
difference. (b) Truncation: `contact_models_comparison_2023` does show unconverged PGS causing
trouble, but its stated driver is conditioning and redundancy, not stiffness. Per-contact methods
inject jamming forces on hyperstatic problems and "fail to converge" on the 10^3 : 10^-3 kg
stacked-cube test, while ADMM, staggered projections and Newton stay robust (Sec. IV-A). The
survey states this correctly one page earlier and then contradicts it in the figure. (c) The
missing one: every engine in Table 4 enforces non-penetration at the velocity level over a step
of length Δt. Any residual approach velocity is integrated into overlap before the next step's
constraint can act. At Isaac Gym's published Shadow Hand step of 1/120 s
(`papers/notes/isaacgym_2021.md`, Table 4) a fingertip closing at 0.5 m/s accrues about 4 mm of
overlap from discretisation alone, independent of contact model and independent of solver. That
is the scale of every number this survey quotes, and the figure does not mention it.

**the fix** Replace the one bullet with three, in the order they matter for a hand: (i) the step
itself, overlap ≈ v_approach · Δt, removed afterwards by the stabiliser (Baumgarte/ERP in Brax,
ODE and Bullet; solref in MuJoCo; the bias term capped by `max_depenetration_velocity` in PhysX),
which removes only a fraction per step so a transient persists for several steps; (ii) the
prescribed compliance, as in finding 1; (iii) solver truncation, which bites when the Delassus
operator is ill-conditioned or the contact set is redundant, both of which a grasp guarantees.
Drop "stiff contact" as the trigger; stiffness is prescribed, conditioning is what varies.

### 3. "MuJoCo sits outside that taxonomy deliberately" is contradicted by the note it cites

**location** 4.2: "MuJoCo sits outside that taxonomy deliberately. Its contact is soft, convex and
complementarity-free". And two sentences later: "Drake's SAP takes the convex middle".

**the problem** Le Lidec et al. place MuJoCo inside the taxonomy, in the CCP family. The survey
uses their taxonomy to organise Table 4 and then exempts the one engine the whole thread is about.

**the evidence** `papers/notes/contact_models_comparison_2023.md`, Table III as recorded in the
note: "**CCP-MuJoCo** (Newton on the primal QCQP, Alg. 4) — 3/4" and "**CCP-Drake** (Newton,
SAP-style) — 3/4", listed alongside CCP-PGS and CCP-ADMM. MuJoCo and Drake SAP are the same
family, not opposite ends with a middle between them. `papers/notes/castro_sap_contact_2021.md`
confirms it from Drake's side: SAP's stated limitation is "a gliding effect during sliding at
distance φ ∼ δt·µ·‖v_t‖" which "unfortunately does not go away as δt → 0" (Sec. V-A, VIII),
which is exactly the Signorini relaxation the survey attributes to CCP alone two sentences
earlier.

**the fix** Write that MuJoCo is a CCP-family convex relaxation solved by a Newton method on the
primal QCQP, and that the relaxation cuts both ways: the compliance admits overlap under load,
and the Signorini relaxation admits force at positive gap during sliding, of size Δt·µ·‖c_T‖.
Two errors of opposite sign in one engine is a better sentence than the one there now, and it is
what the evidence says. Then say Drake SAP is the same family with a documented penetration bound,
and delete "outside that taxonomy" and "the convex middle".

### 4. The survey puts PhysX in the LCP family in 4.2 and takes it out in 4.3

**location** 4.2: "Linear complementarity, the family used by Bullet, ODE and PhysX, satisfies
Signorini alone". 4.3: "PhysX uses a Temporal Gauss-Seidel solver rather than a classical PGS or
LCP scheme." Table 4's `isaacgym_2021` solver cell repeats the second.

**the problem** A direct contradiction between two subsections of the same section, on the engine
that carries 41 of the 110 method papers. It comes from conflating a contact *model* with the
*algorithm* that solves it, which is precisely the distinction Le Lidec et al. exist to draw.

**the evidence** `papers/notes/contact_models_comparison_2023.md` Table III lists "LCP-PGS (used
by Bullet, ODE, PhysX, DART)", a statement about the model and the solver family.
`papers/notes/isaacgym_2021.md` Sec. 3 quotes PhysX's own description: TGS "uses the observation
that sub-stepping a simulation with a single gauss-seidel solver iteration yields significantly
faster convergence", accumulating per-body velocity deltas into the constraint bias terms. That
is a substepped sequential-impulse Gauss-Seidel scheme, in the LCP family by model, not a
classical LCP solve by algorithm.

**the fix** Keep model and algorithm in separate sentences, once, in 4.2. "PhysX linearises the
friction cone, which places it in the LCP family in Le Lidec's classification. It does not solve
an LCP: its Temporal Gauss-Seidel scheme folds substepping into the Gauss-Seidel sweep, and
exposes position and velocity iteration counts separately." Then delete the "rather than" clause
in 4.3, which currently reads as a correction of 4.2.

### 5. "Engines do not expose penetration depth" is false, and this corpus refutes it

**location** 4.2: "The depth is created by the solver on every step and is not handed to the
user." And "Two of the 15 engines report a penetration depth exposed to the user". And 7.3:
"Simulators would have to expose penetration to code outside the reward, which Table 4 records
that only some do."

**the problem** This is the load-bearing claim of the whole thread, it is the stated reason the
gap in 8.2 cannot close, and it is wrong. The evidence against it is inside this repository, in
the parse of the very repository the survey cites for Isaac Gym.

**the evidence** `code/md/isaacgym_2021.md` (IsaacGymEnvs, the released code for
`isaacgym_2021`): line 8809 `def get_max_interpen_dists(asset_indices, plug_pos, plug_quat,
socket_pos, socket_quat, wp_plug_meshes_sampled_points, wp_socket_meshes, wp_device, device)`;
line 8823 `def get_interpen_dist(queries, mesh, interpen_dists)`; lines 8840-8862 compute
`max_interpen_dists`, split environments on `low_interpen_envs = torch.nonzero(max_interpen_dists
<= interpen_thresh)` and scale the policy update accordingly; lines 3630 and 3753 set
`interpen_thresh: 0.001  # max allowed interpenetration between gear and shaft` and `# SAPU: max
allowed interpenetration between plug and socket`. That is a released Isaac Gym task measuring
simulated interpenetration depth per environment, at millimetre threshold, during RL, and acting
on it. Table 4 records Isaac Gym as `penetration exposed: no`, and
`corpus/rows/isaacgym_2021.json` carries `penetration_exposed: false` with `penetration: "not
addressed"`, contradicting the code parse in the same corpus. Two more counterexamples:
`papers/notes/tactile_genesis_2026.md` App. A.1 documents two penetration-depth backends on
Genesis collision geometry, an analytic per-geometry SDF query and a BVH sphere/ray-triangle
walk, offered to users as sensors, while Table 4 leaves Genesis's penetration cell blank; and
`papers/notes/comfree_sim_2026.md` Sec. III-B records that ComFree-Sim's impedance acts on the
signed gap through "the identical (r_min, r_max, w, m, p) = [0.9, 0.95, 0.001, 0.5, 2.0] default
hyperparameter API as MuJoCo's own solver", which means MuJoCo's penetration is parameterised by
the same user-facing knob the survey praises ComFree-Sim for exposing. Separately, and not from
disk, so treat it as my testimony rather than as corpus evidence: MuJoCo's C API exposes
`mjContact.dist` per contact in `mjData`, negative when penetrating, and Isaac Gym's Python API
returns per-contact distances from `gym.get_env_rigid_contacts`. I could not verify either from
`code/md/`, which for these engines is a README and file tree only.

**the fix** Three changes. (a) Rename Table 4's column to "penetration depth reported in the
parsed source", and say in the caption that it is a statement about what the papers documented,
not about what the engines can do. (b) Delete "The depth is created by the solver on every step
and is not handed to the user" and replace it with what the code actually shows: the depth is
computable by anyone, from the poses and the meshes, in a few lines of Warp, and one NVIDIA-shipped
Isaac Gym task already does it, so the reason nobody reports it for a dexterous rollout is not that
they cannot. (c) Delete the third of the "four things would have to change" in 7.3 outright, and
in 8.2's "what would close it", point at
`code/md/isaacgym_2021.md`'s SAPU implementation as the worked example. This makes the gap
stronger, not weaker: a field that has the tool in its own benchmark repository and still does not
use it is a more damning finding than a field that is blocked.

### 6. The Erez/Dojo bargain is rhetorically satisfying and mechanically wrong

**location** 4.2: "Read Erez's grasp table backwards and the trade is priced: tens of millimetres
of overlap on a drop test is what buys the 16 ms timestep that holds a grasp where Bullet needs
0.03 ms."

**the problem** It prices a trade between two numbers from different papers, different systems and
different mechanisms, and the source that supplies half of it identifies a different cause.
Penetration depth does not buy timestep. Both are downstream of the regularisation, and the depth
is separately tunable.

**the evidence** Erez et al.'s own results isolate the coordinate representation, not the
compliance, as the driver of MuJoCo's timestep advantage. On the planar chain, which has no
contact at all, MuJoCo runs at 243.2 kHz against Bullet's 22.8 and PhysX's 6.4, and Bullet's
articulated Featherstone mode (BulletMB, 81.4 kHz) "still outperforms all the engines that use
Cartesian coordinates by a significant margin"
(`papers/notes/physics_engine_comparison_2015.md`, Fig. 3 and Sec. IV-B). Contact compliance
cannot explain a contact-free test. Second, the Dojo numbers are non-monotone in the timestep:
MuJoCo at −28 mm at Δt = 0.01 s and −46 mm at Δt = 0.001 s
(`papers/notes/dojo_2022.md`, Table II). A dt-independent stabiliser time constant does not
produce more overlap at a ten-times-smaller step. Either the configuration ties the compliance to
Δt or the reported quantity is an impact transient on a drop, and in both cases it is not the
steady-state grasp depth the survey needs it to be. Third, `castro_sap_contact_2021` reports
2.5×10^-5 m at δt = 10^-2 s for a compliant engine, six orders of magnitude below Dojo's MuJoCo
figure at the same step, which shows directly that the depth is a setting rather than the price
of the step size.

**the fix** Cut the sentence. Replace it with the trade that the evidence does support: the
regularisation buys conditioning, which is what lets a hyperstatic grasp run at a large step, and
Erez's contact-free planar-chain result shows most of the timestep advantage is the joint-coordinate
formulation rather than the contact model at all. Then say the depth it costs is a chosen number,
citing the SAP bound and the ComFree-Sim sweep as two engines that chose it and published it.
Note the non-monotonicity in Dojo's Table II explicitly rather than quoting the two cells as a
trend.

### 7. DeXtreme's calibration failure is inverted

**location** 4.6: "DeXtreme replayed real cube states back into simulation with physics enabled and
found the replay 'sometimes resulted in interpenetrations', so the cube's physics parameters could
not easily be calibrated. The interpenetration the engine does not expose is also what blocks the
calibration that would let anyone attribute the gap to contact at all."

**the problem** The second sentence reverses the causality of the first and of the source. The
interpenetration was the *symptom* of a pose-estimation error, and DeXtreme saw it. Non-exposure
did not block anything; had the engine reported depth to nine decimals the calibration would have
failed identically, because the states being replayed were wrong.

**the evidence** `papers/notes/dextreme_2022.md` line 70, quoting Sec. 5 verbatim: "there is still
some sim-to-real gap in pose estimation. This is manifested when we played back the real states in
sim (real-to-sim) with physics enabled, which sometimes resulted in interpenetrations. Therefore,
we were not able to easily calibrate physics parameters of the cube". The subject of the sentence
is the pose estimator. The interpenetration is how the error showed itself, which is also an
instance of the general point that a replayed trajectory is placement rather than physics.

**the fix** Keep the quote, drop the inference. Write: "DeXtreme's real-to-sim replay
interpenetrated because the replayed poses carried the pose estimator's error, not because the
contact model failed. A replayed trajectory is a placement, so the overlap it shows bounds the
state estimate rather than the physics. That is why it could not be used to calibrate the cube,
and it is why calibrating contact against hardware still has no worked example for a hand."

---

## Major

### 8. The grasp test used four engines, not five

**location** 4.1: "asked five engines for the largest timestep at which the object was still in
the hand".

**the problem** Havok was excluded from the grasp test. The survey then reports four values, so
the sentence disagrees with its own list.

**the evidence** `papers/notes/physics_engine_comparison_2015.md`, Appendix: "we currently have no
working PD controller for Havok, and it is therefore excluded from the grasping test." The note's
grasp table has exactly four entries plus MuJoCo's two integrators.

**the fix** "asked four of the five engines". While there, add the caveat the authors state and
the survey omits: the comparison runs all engines on a deliberately restricted common feature set,
hinge joints plus sphere and capsule geometry only, no boxes and no meshes (Sec. II), and the
authors close with "It is an open question whether this model system can be tuned to work better
in the gaming engines" (Sec. IV-D). A 500x spread carrying the weight this one carries needs both
sentences, not just the conflict-of-interest disclosure.

### 9. Four of Figure 3's engine labels are wrong or unsourced

**location** `fig3_sim_step.svg`, the per-stage annotations.

**the problem** Four labels contradict the notes or appear in no note.

**the evidence**
- "RK4 (Brax)" under integrate. `papers/notes/brax_2021.md` Sec. 6.2: "Brax achieves competitive
  linear momentum conservation scaling owing to its maximal cartesian coordinate representation of
  positions and symplectic integration scheme." Symplectic, not RK4. RK4 is MuJoCo's, per
  `mujoco_2012` Sec. II-A and Erez's MuJoCo-RK column.
- "Dojo: exact, nonconvex" under narrow phase. `papers/notes/dojo_2022.md` Sec. V: Dojo supports
  "point, sphere, and capsule collisions with flat surfaces", and its limitations list "no
  convex-mesh or triangle-mesh support yet". Its geometry is the most restricted in the figure.
  The non-convexity is in the contact problem, not in the narrow phase, and under a narrow-phase
  heading the label reads as the opposite of the truth.
- "MuJoCo: soft, pyramidal" under constraint assembly. Both MuJoCo notes say the cone is kept
  exact and the pyramid explicitly rejected: `mujoco_2012` Sec. II-B rejects "replace the friction
  cone with a pyramid and convert ... into an LCP"; `mujoco_convex_contact_2014` Eq. 9 uses an
  elliptical cone. 4.2 makes pyramid-linearisation the defining property of the LCP family that
  MuJoCo is being contrasted against, so the figure contradicts the text on the figure's own point.
  (If the intent was the modern implementation's `cone="pyramidal"` default, no parsed source
  states it, and the survey cannot use it.)
- "Genesis: GPU tiles" under broad phase. `papers/notes/genesis_2024.md` records libccd for
  collision detection and constraint-island decomposition for parallelism. "GPU tiles" appears
  nowhere.

**the fix** Brax to "symplectic Euler (Brax)". Dojo's narrow-phase label to "primitives against
half-spaces only", which is a sharper fact and supports the survey's own caveat that Dojo shows no
hand. MuJoCo's constraint-assembly label to "soft, elliptic cone". Cut the Genesis broad-phase
label or replace it with "libccd, constraint islands". Every label in a figure needs the same
citation discipline as a sentence.

### 10. Convex decomposition is the wrong sign for penetration

**location** `fig3_sim_step.svg`: "Convex decomposition replaces the mesh, so the object the solver
sees is not the object the renderer draws." Section 4.1 repeats it as one of the two stages that
matter. Both sit under "Where penetration comes from".

**the problem** The fact is right and the placement is wrong. A convex hull or a convex
decomposition of a concave object is a superset of that object. The solver therefore holds the
finger *further out* than the visual mesh requires, which produces phantom contact, blocks
concave grasps, and makes penetration measured against the visual mesh look smaller, not larger.
Under a "where penetration comes from" heading the bullet points the reader in the opposite
direction.

**the evidence** `papers/notes/mujoco_2012.md` Sec. III-B: "Non-convex meshes can be rendered but
are not used in collision detection; instead the user should decompose them into convex meshes",
which establishes the substitution but says nothing about its sign. The direction is geometry: the
hull contains the mesh. The cases that do create overlap are the reverse substitution, an
inscribed primitive proxy standing in for a larger visual mesh, which is the common fingertip
modelling choice. The bullet also does not apply uniformly to the engines in Table 4: PhysX 5 uses
SDF collision for non-convex rigid bodies (`corpus/rows/orbit_2023.json` and
`corpus/rows/isaaclab_2025.json` both record it), so the two frameworks carrying most of the
corpus are the ones that skip convex decomposition.

**the fix** Move the bullet out of "where penetration comes from" into a separate line about
geometry mismatch, and state the sign both ways: an outer hull blocks contacts that should happen
and hides overlap from any measurement taken against the visual mesh, while an inscribed primitive
admits overlap the solver never sees. Then note that this is why a penetration number must say
which geometry it was measured against, which is the same ambiguity 7.3 already identifies between
`grab_2020`'s 3.25 mm and `oakink_2022`'s 2.53 cm. Add the SDF exception.

### 11. MuJoCo Playground does not build on MuJoCo Warp

**location** 4.2, closing the ComFree-Sim paragraph: "in the GPU backend that both MuJoCo
Playground and Newton build on".

**the problem** Contradicted by the survey's own next subsection and by the note.

**the evidence** `papers/notes/mujoco_playground_2025.md` Sec. VI, quoted in the note: contact cost
scales with possible contacts "due to JAX's requirement of static shapes at compile time. This
limitation can be overcome by using more flexible frameworks like Warp and Taichi. This upgrade is
an active area of development." Warp is future work in the parsed source. Section 4.3 of the
survey says the same: "MJX and MuJoCo Playground took the other route, putting MuJoCo's own solver
on the GPU through JAX".

**the fix** "in the GPU backend Newton builds on, and the one MuJoCo Playground names as its
intended replacement for JAX." That is both accurate and a second instance of the section's best
point, that the backend under a framework name is moving.

### 12. Dojo's Table V is a gradient-inclusive timing and its authors say not to read it this way

**location** 4.2: "The price is in its Table V, where MuJoCo is fastest on every system tested,
0.335 s against Dojo's 1.159 s on a Franka Panda over 1000 steps."

**the problem** This is the section that exists to police incomparable numbers, and it quotes one.
Table V times forward simulation *plus gradients*, for engines that are not all computing
gradients, at a fixed step size that the Dojo authors state is not the step size Dojo needs.

**the evidence** `papers/notes/dojo_2022.md`, Throughput: "Table V compares
forward-simulation-plus-gradient wall-clock time for 1000 steps at Δt=0.01s". Stated limitation,
Sec. VI-B: Dojo "requires more computation per time step compared to existing simulators that use
a soft-contact model (e.g. MuJoCo and Drake), but allows for accurate simulation with a lower
sample rate, making wall-clock comparisons between the two simulators difficult". The note also
records Dojo running stable at h = 0.05 where MuJoCo needs h = 0.01 (Sec. V-C). The survey also
drops the standard deviations (±0.001 and ±0.077) it prints elsewhere.

**the fix** "Its Table V times 1000 steps of forward simulation with gradients at a matched
Δt = 0.01 s, and on that measure MuJoCo is fastest on every system, 0.335 ± 0.001 s against
Dojo's 1.159 ± 0.077 s on a Franka Panda. The authors say the comparison is difficult, because
Dojo is stable at five times the step size, so a per-step ratio overstates the gap and a
per-second-of-simulated-time ratio would understate it."

### 13. Table 4's "dt s" column reports experiment settings as engine defaults

**location** Table 4, column `dt s`; 4.2: "Three of 15 engines state a default physics timestep".

**the problem** None of the three states a default. Each states one experiment's timestep, and in
the Isaac Gym case the paper publishes nine different ones. The finding as phrased is an artefact
of the column name.

**the evidence** Isaac Gym's cell is 0.008333 s. `papers/notes/isaacgym_2021.md` Table 4 lists per
task: Shadow Hand Standard and OpenAI and Allegro at 1/120 s, ANYmal, Ingenuity and TriFinger at
1/200 s, Franka at 1/60 s. `mujoco_convex_contact_2014`'s 0.01 s is the 27-DoF humanoid test's
step (Sec. VI-B), and `mujoco_2012` separately reports 15 ms for a humanoid gait. ComFree-Sim's
0.002 s is the benchmark step; Sec. IV-C states it "remains stable at a moderately large time
step (e.g., dt=0.02 s)".

**the fix** Rename the column "timestep reported, with its condition" and put the condition in
the cell, as the throughput column already does so well. Then the sentence becomes the true and
more interesting one: "No engine paper states a default physics timestep. Three report one for a
named experiment, and Isaac Gym is the only one that publishes a per-task table, which is why its
Shadow Hand step of 1/120 s is quotable at all." Isaac Gym's per-task publication is currently
praised in 4.3 and punished in 4.2's count.

### 14. "Primitives the size of a fingertip" overstates the ComFree-Sim drop test

**location** 4.2: "Millimetres, on primitives the size of a fingertip, in the GPU backend that both
MuJoCo Playground and Newton build on."

**the problem** The primitives are about 5 cm across, roughly four times a fingertip, and they are
dropped rather than loaded by a hand. Penetration under a regularised contact scales with the
normal load and the effective inertia at the contact, so a dropped 5 cm block and a fingertip
pressing a held object are different regimes, and the sentence transfers a number between them.

**the evidence** `papers/notes/comfree_sim_2026.md`: "collision-rich drop test (five 5×5 arrays of
convex primitives, ~5 cm average size, dt=0.002s, 1000 steps, mean±std over all detected
contacts)". The survey states the 5 cm correctly one sentence earlier and then calls it a
fingertip.

**the fix** Delete "the size of a fingertip". The honest version: "Millimetres, on 5 cm primitives
under their own weight. Nobody has published the equivalent number for a fingertip loaded by a
grasp, which is the measurement this survey asks for in section 7."

### 15. "A factor of 6.4 from the task alone" is not established

**location** 4.4: "LeapCubeReorient runs at 76,354 ± 143 and PandaRobotiqPushCube at 487,341 ±
4,346. Same hardware, same measurement, same codebase, a factor of 6.4 from the task alone."

**the problem** The two environments differ in robot, degrees of freedom, contact count *and*
solver configuration, because Playground tunes solver settings per environment. "The task alone"
claims all else equal, which the source does not support.

**the evidence** `papers/notes/mujoco_playground_2025.md` Table III records per-environment
overrides of `iterations`, `ls_iterations`, `timestep`, `max_contact_points` and `max_geom_pairs`,
with values as far apart as `iterations=1, ls_iterations=4` and `iterations=4, ls_iterations=8`.
The note does not record the settings used for LeapCubeReorient or PandaRobotiqPushCube, so
whether they match cannot be checked from disk.

**the fix** "a factor of 6.4 between two environments in one codebase on one A100. Playground
tunes solver iterations and contact bounds per environment, so the ratio is the environment and
not the task in isolation, and the paper does not print the two configurations side by side.
That is itself the reporting failure this subsection is about."

### 16. Table 4 marks Newton differentiable against its note's explicit warning

**location** Table 4, `newton_2025`, `diff. = yes`.

**the problem** The note says the only evidence is a test file name and tells the survey not to
claim it.

**the evidence** `papers/notes/newton_2025.md`: "The presence of `test_differentiable_contacts.py`
is the only positive evidence in this corpus that a *Newton* solver (likely Kamino ...) supports
differentiable contacts ... this distinction (Newton-via-Kamino may be differentiable even where
Newton-via-MJWarp is not) is worth flagging explicitly if the survey claims 'Newton is
differentiable.'" And `mujoco_warp_2025`'s README states differentiability "is not yet available".

**the fix** Change the cell to "solver-dependent; not confirmed", consistent with how the contact
model cell already handles the same problem for the same row. This also strengthens 4.3: Newton's
differentiability, like its contact model, is a property of the backend rather than the name,
which is the subsection's thesis.

### 17. Sixteen null rows disappear from the thread's denominator in section 5

**location** 5.4: "Across all 110 method rows, 83 do not address penetration, 5 constrain it, 3
measure it and 3 penalise it."

**the problem** 83 + 5 + 3 + 3 = 94. Sixteen rows are null and are not mentioned here, so a reader
infers that 99 of 110 papers ignored penetration. Section 8.2 does say "16 do not settle it",
which makes section 5 the inconsistent one.

**the evidence** Recomputed from `corpus/rows/*.json` over the 110 rows with `class == "method"`:
`not addressed` 83, `null` 16, `constrained` 5, `penalised` 3, `measured` 3. A null is a note that
did not settle the question, which is a fact about the note-writing process, not about the paper.

**the fix** Use the same four-way split everywhere it appears, and say what null means: "Of the 94
method rows where the note settles it, 83 do not address penetration. Sixteen rows are unsettled,
which is a limit of our reading and not a finding about those papers." The claim survives at
83 of 94 and is no longer open to the objection that it counts our own silence as theirs.

### 18. The ManiSkill2 cross-framework comparison is incomparable for a deeper reason than env count

**location** 4.4: "ManiSkill2's PickCube table takes the best result over 16 to 512 environments
for each system ... giving ManiSkill2 with a render server 2487 ± 24 FPS at its optimum of 64
environments against Isaac Gym's 865 ± 35 at its optimum of 512."

**the problem** Every number checks out, and the env-count objection is correct, but the larger
incomparability is left out: these are two different architectures being timed on a visual
sample-collection loop, not two physics engines.

**the evidence** `papers/notes/maniskill2_2023.md`: ManiSkill2's rigid-body physics runs on CPU
across worker processes with a shared GPU render server, and the paper is explicit that "this
CPU-rigid-body and GPU-soft-body ... not a fully GPU-parallel rigid-body pipeline (like Isaac
Gym's) ... is the architecture". The benchmark renders 128×128 images at 500 Hz sim and 20 Hz
control, so rendering is inside the number for both.

**the fix** Add one sentence: "The two systems are not the same kind of thing. ManiSkill2 runs
rigid-body physics on CPU worker processes behind a GPU render server, Isaac Gym runs physics on
the GPU, and the measured quantity includes 128×128 rendering for both. The env-count tuning is
the second problem, not the first."

---

## Minor

### 19. "For a hand the bound is set for the worst case" is an unlabelled inference

**location** 4.1, closing the MJX paragraph.

**the evidence** `papers/notes/mujoco_playground_2025.md` Table III records `max_contact_points`
and `max_geom_pairs` overrides for DM Control Suite ports (cheetah-run, finger-spin, hopper-stand,
humanoid-stand, walker-stand). No hand environment in the note carries one, and LeapCubeReorient's
settings are not recorded.

**the fix** Either cite a hand environment's override or label the sentence as inference: "The
overrides recorded in the paper are for locomotion ports. A hand's bound would have to be set the
same way, for the worst case, though the paper does not print the hand configurations."

### 20. ComFree-Sim's prose contradicts its own table, and the survey quietly picks the table

**location** 4.2: "ComFree-Sim ranges from 3.9 ± 6.9 mm to 0.9 ± 1.5 mm as its stiffness and
damping are raised."

**the evidence** The direction in the survey matches the table and is the physically correct one.
The paper's own sentence, recorded in `papers/notes/comfree_sim_2026.md` Sec. IV-A, says the
opposite: "penetration increases with k_user and decreases with d_user", while its cells go
(0.1 → 3.9 mm), (0.3 → 1.6 mm), (0.5 → 1.0 mm).

**the fix** Say so in half a sentence. "Its stiffness sweep runs 3.9 ± 6.9 mm down to
0.9 ± 1.5 mm as k_user rises, though the paper's prose describes the opposite direction from its
own table." This is a paper-versus-itself disagreement, which is a category the survey already
treats as a finding elsewhere.

### 21. Dojo's 15 iterations are scoped to three robots

**location** 4.2: "by an interior-point method converging within 15 iterations".

**the evidence** `papers/notes/dojo_2022.md`: "Converges 'within 15 iterations for all three
robots' tested in the convergence study (Sec. V-A)". None of the three is a hand, which the survey
notes two sentences later for a different purpose.

**the fix** "converging within 15 iterations on the three robots of its convergence study".

### 22. `max_depenetration_velocity` is boilerplate, and it caps a rate rather than a depth

**location** 4.2: "DexTrack's released configs set PhysX's `max_depenetration_velocity`, which
bounds how fast overlapping bodies are pushed apart, to either 10.0 or 1000.0 depending on the
task variant, with no explanation".

**the evidence** The claim is exactly right and well sourced (`papers/notes/dextrack_2025.md`
line 41, and `code/md/dextrack_2025.md` lines 1182, 4464, 5609 and others). Two things sharpen it.
The same parameter appears across unrelated stock IsaacGymEnvs tasks at 5.0, 10.0, 100.0 and
1000.0 (`code/md/isaacgym_2021.md` lines 897, 1924, 2083, 2448, 3113), so DexTrack inherited a
template rather than choosing per variant. And the parameter caps the velocity of the positional
bias term, so its effect is how many steps an overlap persists and how much energy the recovery
injects, not how deep the overlap gets.

**the fix** "DexTrack's configs carry PhysX's `max_depenetration_velocity` at 10.0 or 1000.0
depending on the variant, inherited from the IsaacGymEnvs templates, which ship values from 5.0 to
1000.0 across unrelated tasks. The parameter caps the rate at which the solver pushes overlapping
bodies apart, so it sets how long an overlap persists and how violently it is undone, and no
config in the corpus comments on it." That makes the point stronger: the one knob in the stack that
governs interpenetration behaviour is being copied without being read.

### 23. Tactile Genesis's XHand1 SDK reports more than an aggregate

**location** 4.5: "because the real XHand1 SDK exposes only an aggregate contact pressure".

**the evidence** `papers/notes/tactile_genesis_2026.md` App. C: "The real XHand1 SDK reports both
a per-taxel raw pressure field and an aggregate contact pressure... but the exact position and
response characteristics of each taxel are not documented, so we cannot register the raw field to
our simulated probe layout."

**the fix** "because the real XHand1's per-taxel field cannot be registered to the simulated probe
layout, leaving only the aggregate pressure comparable." The undocumented calibration, not the
missing signal, is the barrier, and it is the more interesting one.

### 24. Table 4 carries a column the text never discusses, and the 41 percent has a loose denominator

**location** Table 4, `licence` column; and 4.2: "Sixty-eight of its 165 cells, 41 percent, are
values no parsed source stated."

**the evidence** Recounted from `paper/tables/table4_simulators.md`: 68 of 165 empty, 41.2 percent,
which reproduces exactly. Per column: licence 13 empty of 15, dt 12, iters 11, penetration 9,
hands 8. The 165 includes the engine-key column, which is never empty, so over the ten data
columns the figure is 68 of 150, 45 percent. The licence column has one populated cell
(`maniskill3_2024`, Apache-2.0) and one that is really a licensing sentence about RaiSim, and the
survey's own brief says a table the text never discusses should be cut.

**the fix** Either cut the licence column or give it a sentence, since "which of these engines can
be used without a key" is a real question for a reader choosing one and RaiSim's row answers it.
And quote the emptiness over the ten data columns, 68 of 150.

### 25. Section 4 is 39 percent over its target

**location** `paper/sections/04_simulators.md`, 3058 words against the 2200 in
`paper/SECTION_BRIEF.md`, which allows 20 percent.

**the fix** The cuts this review implies (the Erez/Dojo bargain, the "outside that taxonomy"
framing, the duplicated PhysX-solver sentence in 4.3) recover roughly 150 words. If more is
needed, 4.6 duplicates material that section 7 covers better, particularly the OpenAI and
DemoStart transfer numbers.

---

## The two judgements

### Is the survey right that naming a simulator no longer names its physics?

Yes, and this is the best claim in section 4. It is the one place where the survey draws a
conclusion the primary sources do not draw for it and the evidence carries it. The
`--physics newton_mjwarp` switch is in Isaac Lab's own hands demo
(`code/md/isaaclab_2025.md:8172`, and a test at :8544 enumerating physics variants), Newton is
multi-solver by construction with MuJoCo-style soft constraints under SolverMuJoCo and ADMM/DVI
under SolverKamino (`papers/notes/newton_2025.md`), and those two make genuinely different contact
errors. "Papers should report the backend and the solver beside the framework" is the right
recommendation and should be promoted into section 7's protocol table, where it currently is not.

The survey in fact understates it. The name fails to determine the physics *within* a single
engine, not only across backends. MuJoCo's friction cone can be pyramidal or elliptic and its
solver PGS, CG or Newton, and MuJoCo Warp does not support PGS or the noslip pass at all
(`papers/notes/mujoco_warp_2025.md`), so "MuJoCo" names at least three different contact solves
before anyone chooses a backend. PhysX 4 and PhysX 5 differ in whether non-convex rigid bodies get
SDF collision, which is a contact-geometry difference between Isaac Gym and Isaac Lab hiding under
one vendor name. Add those two sentences and the claim goes from true to unarguable.

### Is the interpenetration thread a real technical concern, or is it being inflated into a theme?

Split verdict, and the authors need to hear both halves.

**The reporting finding is real and is the best thing in the survey.** Eighty-three of the 94
method rows where the note settles it do not address penetration; of the eleven that do, seven do
it offline in a synthesiser or a retargeter, and not one reports a penetration number for its own
trained policy's rollouts. `dextrack_2025` is the clean case and the survey nails it: a penetration
formula in Appendix B, applied only to input references, with the policy's own overlap given prose
instead of a number and reported as robustness. `toporetarget_2026` constrains the reference and
does not re-measure the rollout. `grab_2020` at 3.25 mm and `oakink_2022` at 2.53 cm on
overlapping data, a factor of eight apart with neither stating its distance function, is a real
and damaging finding about the field's vocabulary. None of that is inflated. It is the correct
diagnosis of a field that optimises a tracking reward and never checks whether the contact
underneath it was physical, and section 7's prescription, a dense surface sample scored by code
that never entered the reward, is the right fix and is well argued.

**The mechanism story underneath it is wrong, in three places, and it is load-bearing.** Findings
1, 2 and 6 are not quibbles. The survey's account of why penetration exists (a penalty force
proportional to depth, an unconverged iteration budget, a price paid for a large timestep) is not
how any of the engines in Table 4 works, and a reader who writes simulators will stop trusting the
section at Figure 3 and will carry that distrust into sections 7 and 8. The correct account is
shorter and more damning: overlap is set by the step size, by a compliance the user chose without
knowing they chose it, and by solver truncation on a problem a grasp makes ill-conditioned by
construction. All three are properties of the configuration, which means interpenetration in a
dexterous rollout is a *reporting* failure about *settings*, not an inherent property of soft
contact.

**The barrier claim is false and should be deleted rather than softened.** "Simulators would have
to expose penetration to code outside the reward" (7.3) is refuted inside this corpus by NVIDIA's
own Isaac Gym repository, which computes per-environment max interpenetration depth against meshes
and gates the policy update on a 1 mm threshold (`code/md/isaacgym_2021.md:8809-8862`), and by
Tactile Genesis, which ships penetration depth as a *sensor* on two backends. Table 4's
"penetration exposed" column is measuring which papers happened to write the word, and the survey
reads it as which engines can report the number. Those are different claims and the survey
conflates them in the one sentence that everything else depends on.

So: keep the thread, and keep it as the spine. Retitle what it is a thread *about*. It is not
"engines hide penetration and the field cannot see it". It is "penetration is a setting nobody
records and a measurement nobody takes, in a field that already has the tooling in its own
benchmark repository". That version is true, it is supported by every piece of evidence the
survey has assembled, it survives contact with a physics-engine reviewer, and it is a harder
finding for the field to shrug off.

---

## Counts

- blocking: 7
- major: 11
- minor: 7
- total: 25

**Verdict on the interpenetration thread: justified as an evaluation and reporting finding, not as
a physics finding.** The 83-of-94 silence, the reference-versus-rollout pattern, and the 3.25 mm
against 2.53 cm definitional gap all hold. The mechanistic account in Figure 3 and section 4.2, and
the claim that engines do not expose the depth, do not hold and must be rewritten before the thread
can carry the weight sections 7 and 8 put on it.
