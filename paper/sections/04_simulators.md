# 4. Simulators and the physics underneath

## 4.1 Requirements of a dexterous simulation

The clearest demonstration that hands are the hard case came from a benchmark that was not about
hands. Erez et al. built a 35-DOF arm modeled on the Shadow Hand, closed it around a capsule with
fixed spring-dampers, and asked four of the five engines for the largest timestep at which the
object was still in the hand. The answers spanned a factor of 500, from milliseconds down to tens of microseconds, with MuJoCo
at the slow-step end (`physics_engine_comparison_2015`, Sec. IV-D). Three caveats travel with that
spread. The engines ran a deliberately restricted common model, hinge joints with sphere and
capsule geometry and no meshes; the authors call it "an open question whether this model system
can be tuned to work better in the gaming engines"; and they wrote MuJoCo and say so.

A grasp is hard for nameable reasons. It is many contacts at once, all persistent, all near
stiction, on an object much lighter than the mechanism holding it. Persistence and multiplicity
make the problem hyperstatic, and Le Lidec et al. show that per-contact solvers of the projected
Gauss-Seidel family, and RaiSim's, then inject spurious jamming forces at stiction that vanish
only once the object slides. The mass ratio makes it ill-conditioned, and in their stacked-cube
test at a 10^3 to 10^-3 kg ratio those same methods fail to converge. Global methods with proximal
regularisation stay robust in both cases (`contact_models_comparison_2023`, Sec. IV-A). What
degrades a truncated solve is therefore conditioning and redundancy, not stiffness, and a grasp
supplies both by construction. Locomotion is forgiving by comparison. On flat ground the contact
model and solver choice "hardly affects" their quadruped's tracked base velocity, and only on
rough, slippery terrain do RaiSim and CCP deviate. A walking robot makes and breaks a few contacts
against ground far heavier than itself. A hand does neither.

Speed enters by the same door. MuJoCo Playground reports that contact time scales with the number
of possible contacts rather than the active ones, because JAX requires static shapes, which is why
its tasks override the bound on contact points and the bound on geometry pairs by hand
(`mujoco_playground_2025`, Sec. VI). Every override printed in that paper is a locomotion port. A
hand's bound would have to be set the same way, for the worst case, but no hand configuration is
printed.

Figure 3 sets out the stages of one simulation step. Three of them make overlap, and they do not
answer to the same knob. In an engine that enforces non-penetration at the velocity level,
integration turns any residual approach velocity into overlap of order v times Δt; an engine that
enforces the gap at the next configuration carries no such term, which is why Dojo's hard-contact
NCP keeps its feet above the floor at every timestep it was tested at. Constraint assembly fixes
the compliance a loaded contact then rests at. A truncated solver leaves a residual that grows
with conditioning. Which of the three dominates in a grasp is not measured anywhere in this
corpus, and the three are not ordered here. A fourth thing is not on the figure, because it is
not a stage of the step and not a source of overlap: a mismatch between the geometry the solver
uses and the geometry the renderer draws, which runs in both directions.

## 4.2 Contact models and solvers

{{figure:fig3_sim_step}}

Table 4 is the engine-by-engine comparison, one line per simulator, built only from what a note
confirmed. Le Lidec et al. supply the taxonomy that organises it, checking each formulation
against the Signorini condition, Coulomb's law, and the maximum dissipation principle. Linear
complementarity, the family of Bullet, ODE, PhysX and DART, satisfies Signorini alone, because
linearising the friction cone to a pyramid biases friction toward its corners. The cone
complementarity problem satisfies the other two but relaxes Signorini, so contact acts at a
distance of size Δt·µ·‖c_T‖. The full nonlinear problem satisfies all three and is non-convex
(`contact_models_comparison_2023`, Table II). A contact model is not the algorithm that solves it.
PhysX linearises the cone, which places its model in the LCP family, and it does not solve an LCP.
Its Temporal Gauss-Seidel scheme folds substepping into the Gauss-Seidel sweep and exposes
position and velocity iteration counts separately (`isaacgym_2021`, Sec. 3).

MuJoCo is inside that taxonomy. Le Lidec et al. classify it as CCP-MuJoCo, a convex relaxation
solved by a Newton method on the primal QCQP, in the same family as CCP-Drake, the SAP-style
scheme (`contact_models_comparison_2023`, Table III). The relaxation makes two errors of
opposite sign in one engine. A loaded contact carries a violation, and a sliding contact
carries force at a positive gap. Drake's SAP inherits the same pair, and its gliding effect at
distance φ ≈ δt·µ·‖v_t‖ "unfortunately does not go away as δt → 0" (`castro_sap_contact_2021`,
Sec. V-A). Le Lidec et al. call that compliance a "numerical trick designed to circumvent the
issues due to hyper-staticity or ill-conditioning at the cost of impairing the simulation".

The depth a loaded contact carries is a chosen number, not a property of the engine. In a
regularised formulation the steady-state violation at a contact is the normal load times the
compliance: zero at zero load, growing with what the contact carries. MuJoCo drives that
violation with a critically damped stabiliser whose steady-state depth, for an object resting
under gravity, has a closed form independent of the object's mass
(`mujoco_convex_contact_2014`, Sec. V). Whoever sets the stiffness sets the depth.

Published penetration figures do not compare with each other, and the reason is worth knowing
before anyone quotes one. Dojo solves a hard-contact problem and stays above the floor on an
Atlas drop test where MuJoCo overlaps by tens of millimetres (`dojo_2022`, Sec. V-A); Drake's
figures for the same quantity are orders of magnitude smaller, and they are analytical bounds for a
point mass at rest rather than measured depths (`castro_sap_contact_2021`, Sec. V-B); ComFree-Sim
reports a depth directly, on small convex primitives dropped under their own weight
(`comfree_sim_2026`, Sec. IV-A). A point-mass bound, a humanoid drop transient and a
dropped primitive differ in load, inertia and regime, so the distances between those figures
measure nothing about each other. What the set does establish is the part that matters for a
hand: in a compliant formulation the depth follows from a stiffness somebody chose, and the GPU
era moved that knob rather than removing it. The oldest engine comparison here puts the
consequence plainly, reporting that engines pushed past their stable step "effectively simulate
a different physics model which can no longer hold the object". No paper in this corpus reports
the depth for a fingertip loaded by a grasp, which is the one configuration a dexterous result
depends on.

Table 4's most interesting column is the one that records whether an engine's own paper reports
a penetration depth, and it is nearly empty. Two engines report one, and both are engines whose
paper is about contact accuracy. The word "penetration" appears nowhere in the Isaac Gym paper,
and Isaac Lab's contact sensor reports force, duration and an average contact point with no
measure of contact quality at all. That is a documentation gap rather than a capability gap:
NVIDIA's own benchmark repository already computes an interpenetration depth per environment for
its assembly tasks and scales the reward down as the depth approaches a millimetre. The quantity
is a few lines of code away in the engine most of this literature trains in.

The rest of Table 4 is largely empty, and the emptiness is a result: two cells in five hold a
value no source stated. No engine paper states a default physics timestep, and the three that
report one report it for a named experiment, so the table's timestep column carries experiment
settings rather than defaults. Fewer than half the engines state a solver iteration count or ship
any dexterous hand. The license column answers a question a reader choosing an engine actually
has, and most engines do not answer it.

{{table:table4_simulators}}

## 4.3 GPU-parallel engines and their throughput

Isaac Gym set the pattern for the GPU-parallel turn. Physics, observations, rewards and actions
stay on the GPU, and PhysX resolves contacts with the Temporal Gauss-Seidel sweep described above.
Its per-task timesteps are published, which is rare. The result that reorganised the field was
that reproducing OpenAI's Shadow Hand cube reorientation took under an hour on a single GPU,
against 30 hours on a CPU cluster (`isaacgym_2021`, Sec. 6.4.1). Thirty-five of the papers
examined run on it.

Orbit and Isaac Lab moved the stack to PhysX 5, and the dexterous offering is thinner than the
predecessor's: the first-party suite is lifting, grasping and reorienting with the KUKA Allegro
hand, while Shadow and Ability hands appear only through third-party grasp evaluation
(`isaaclab_2025`, Sec. 7.2.3). MJX and MuJoCo Playground took the other route, putting MuJoCo's
own solver on the GPU through JAX at the cost described above. MuJoCo Warp ports the same solref
and solimp soft-constraint entries to NVIDIA Warp, and its README states that the legacy PGS solver
and the noslip pass are unsupported and that differentiability "is not yet available"
(`mujoco_warp_2025`). GPU MuJoCo is not a differentiable MuJoCo. Genesis is the broadest, pairing
a rigid constraint solver with FEM, MPM, PBD and SPH solvers and a differentiable backward path,
and it ships a Shadow Hand. Its README quotes no throughput number at all, so the large FPS
figures that circulate for Genesis trace to nothing in `genesis_2024`.

Newton changes how these names should be read. It is explicitly multi-solver: SolverMuJoCo wraps
MuJoCo Warp, SolverKamino is a proximal-ADMM and dual-variational-inequality contact solver, and
XPBD and VBD do position-based constraint projection (`newton_2025`). Its contact model is
solver-dependent, not a property of the engine, which is how Table 4 records it. Isaac Lab's code
already exposes a `--physics newton_mjwarp` backend switch in its hands demo, and its roadmap
announces Newton integration. An experiment reported as Isaac Lab may be running PhysX 5 with TGS,
or MuJoCo's soft-constraint entries under Warp, and those two make different contact errors. The name
also fails to fix the physics inside one engine. MuJoCo's convex solver is a family, interior
point or projected Newton, conjugate gradient or Gauss-Seidel (`mujoco_2012`, Sec. II-D), and
MuJoCo Warp supports neither PGS nor the noslip pass. PhysX 4 and PhysX 5 differ in whether
non-convex rigid bodies get SDF collision, which is a contact-geometry difference between Isaac
Gym and Isaac Lab under one vendor name (`orbit_2023`, `isaaclab_2025`). Naming a simulator no
longer names its physics. Papers should report the backend and the solver beside the framework.

Reported throughput does not compare across engines, because four headline figures measure four
different quantities. One engine reports parallel environment steps per second with physics,
observations and rewards on device. Its successor reports frames per second in training, which
includes the learning update, and on eight GPUs rather than one. A third reports a rendering-heavy
figure with reward and termination removed from the timing and no environment count
(`maniskill3_2024`). A fourth reports a physics-only ceiling, also without an environment count
(`orbit_2023`). Table 4 records each figure
with the quantity it measures, which is the only form in which any of them is usable.

The one number reported cleanly enough to reuse is MuJoCo Playground's, in training steps per
second on one GPU over five seeds. A hand reorientation task runs about six times slower there
than a parallel-jaw pushing task on the same hardware in the same codebase. That factor is not a
property of the task alone: Playground tunes solver iterations, line-search iterations, timestep
and contact bounds per environment, and does not print the two configurations side by side, which
is what makes even those two figures incomparable. A training-loop rate is also mostly not a
measurement of physics. On Playground's own breakdown the policy update dominates the frame, with
physics a few percent of it.

Cross-framework comparisons add further free parameters. One widely cited table takes the best
result over a range of environment counts for each system (`maniskill2_2023`, Table 1a), which
tunes a free parameter per competitor; and the two systems being compared are not the same kind of thing, one running
rigid-body physics on CPU workers behind a shared render server and the other on the GPU. Because
the measured loop includes rendering at a fixed control rate, what is compared is a visual
sample-collection loop rather than two physics engines. Its authors say so themselves, and
Playground is equally explicit that its own cross-simulator plot borrows two of its numbers from
another paper. Several sources give no figure at all, pointing instead at an external dashboard or
omitting throughput from their documentation entirely.

The failure reaches past the engine papers into the methods. Of the 47 corpus method papers that
name a GPU-batched simulator, 19 state no environment count anywhere, and Isaac Lab's own paper
states no physics timestep, no decimation and no solver iteration count for any task. A throughput
figure is interpretable only with the environment count, the GPU, the timesteps, the solver
iteration budget, and a statement of whether rendering and the learning update sit inside the
measurement. Almost nobody reports all five.

## 4.4 Tactile simulation and the sim-to-real gap

The three tactile simulators in this corpus calibrate against three different things, and none of
them is a manipulation outcome. TACTO is a rendering layer over a host engine, by default
PyBullet's rigid contact model. It reads post-solve link poses and the engine's reported normal
force and maps that force to gel-mesh deformation at the rendering level, so it contributes no
contact physics of its own. Its only sim-to-real number is a tactile pose-estimation task, where the simulated-data model is
about twice the error of one trained on a small set of real datapoints (`tacto_2020`, Table II).

Taxim is example-based rather than simulated, calibrated from real indentations, and it beats
TACTO on every optical-similarity metric against real images. Its marker-motion model is
calibrated against a finite-element reference, and it tracks that reference about three times more
tightly than the reference tracks reality, so its residual is bounded below by its own calibration
target. The authors also state that they simulate quasi-static contact only, with slip left as
future work (`taxim_2021`, Sec. V). Slip is what a hand needs.

Tactile Genesis inverts the thread. It implements two penetration-depth backends on the
collision geometry, an analytic SDF query and a BVH raycast, and uses the depth as the sensor
signal rather than as an error, so the quantity every other engine treats as a defect sets this
one's operating point.

Most of what is written about this gap is attribution
without measurement. PenSpin asserts that the pure physics gap "cannot be bridged by extensive
domain randomization alone" while reporting no experiment that isolates it (`penspin_2024`).
MuJoCo Playground attributes its LEAP hand failures to physical flex in low-cost hardware and
names more accurate collision geometries as the fix, without measuring either. DeXtreme lists
four candidate causes for its shortfall, including a malfunctioning Allegro thumb used in most
trials, and disambiguates none by experiment (`dextreme_2022`).

What has been measured is narrower, and section 7 collects the transfer numbers. The one result
that links a quantified model error to transfer ranks system-identification runs by dynamics-model
error and pairs each with real success: the best-identified model grasps 8 of 10 attempts, the
worst 0 of 10 (`humanoid_sim2real_recipe_2025`, Table 1). Where a cause has been pinned down
elsewhere it is usually perception or actuation rather than contact, with pose estimators and
camera trackers named as the unmodelled source in the real numbers (`pddm_2019`, App. C).

The one paper that looks at the contact side is usually read backwards. DeXtreme's real-to-sim
replay interpenetrated because the replayed poses carried the pose estimator's error, not
because the contact model failed, and the paper says so: it could not calibrate physics against
the real system because the state it replayed was already wrong. The commonly cited reading,
that the contact model was at fault, is not what the sentence says.