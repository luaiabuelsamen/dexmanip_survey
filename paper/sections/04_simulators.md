# 4. Simulators and the physics underneath

## 4.1 Requirements of a dexterous simulation

The clearest demonstration that hands are the hard case came from a benchmark that was not about
hands. Erez et al. built a 35-DOF arm modeled on the Shadow Hand, closed it around a capsule with
fixed spring-dampers, and asked four of the five engines for the largest timestep at which the
object was still in the hand. MuJoCo held the grasp at 16 ms, PhysX at 2 ms, ODE at 0.25 ms and
Bullet at 0.03 ms, a spread of a factor of 500 (`physics_engine_comparison_2015`, Sec. IV-D).
Havok is the fifth and was excluded for want of a working PD controller. Three caveats travel with
that spread. The engines run a deliberately restricted common model, hinge joints with sphere and
capsule geometry, no boxes and no meshes (Sec. II). The authors call it "an open question whether
this model system can be tuned to work better in the gaming engines" (Sec. IV-D). The timesteps
are log-spaced and good only to a factor of two, and the authors wrote MuJoCo and disclose it.

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

Table 4 is the engine-by-engine comparison, one row per simulator, built only from what a note
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

Published penetration figures do not compare with each other, and the reasons are instructive.
Dojo solves a hard-contact complementarity problem and stays above the floor at every timestep
it was tested at, where MuJoCo penetrates tens of millimetres on the same Atlas drop
(`dojo_2022`, Sec. V-A). But the MuJoCo column is not a trend: a ten-times-smaller step
produces more overlap, which no timestep-independent stabiliser does, so either that
configuration ties compliance to the timestep or the quantity is an impact transient rather
than a steady-state depth. Drake's SAP reports figures orders of magnitude smaller again, and
they are analytical bounds for a point mass at rest on a plane under a near-rigid stiffness
rule, not measured depths (`castro_sap_contact_2021`, Sec. V-B). ComFree-Sim does report
penetration directly, as an explicit tuning parameter, on 5 cm convex primitives dropped under
their own weight (`comfree_sim_2026`, Sec. IV-A). A point-mass bound, a humanoid drop transient
and a dropped primitive differ in load, inertia and regime, so the distances between them
measure nothing. What the set does establish is the part that matters for a hand: in a
compliant formulation the depth follows from a stiffness somebody chose, and the GPU era moved
that knob rather than removing it. `physics_engine_comparison_2015` puts the consequence
plainly, reporting that engines pushed past their stable step "effectively simulate a different
physics model which can no longer hold the object" (Sec. IV-D). No paper in this corpus reports
the depth for a fingertip loaded by a grasp, which is the one configuration a dexterous result
depends on.

That brings Table 4's most important column, and the claim it does not support. The column records
whether a parsed source reported a penetration depth, not what an engine can compute. Two of the
15 engines report one, Dojo and ComFree-Sim, and both are engines whose paper is about contact
accuracy. Four are recorded as not reporting it: Brax, Isaac Gym, Isaac Lab and Orbit. Nine rows
are blank. The word "penetration" appears nowhere in the Isaac Gym paper, and Isaac Lab's contact
sensor reports force, duration and an average contact point with no contact-quality metric. The
Isaac family carries 42 of the 112 method papers in this corpus.

**The tooling exists and the number is not recorded.** NVIDIA's own IsaacGymEnvs computes
interpenetration depth in simulation: its IndustReal tasks sample points on one mesh, query
them against the other, and reduce to a per-environment maximum, then gate the policy update on
it, scaling reward down as the maximum approaches a one-millimetre threshold
(`code/md/isaacgym_2021.md`). That is a shipped task measuring penetration per environment
during training and acting on it, in the engine Table 4 records as not exposing the quantity.
The depth is computable from the poses and the meshes in a few lines of Warp, and the field's
own benchmark repository already does it.

One knob in that stack bears on penetration and nothing in the corpus explains its setting.
PhysX's `max_depenetration_velocity` caps how fast the solver pushes overlapping bodies apart,
so it governs how long an overlap persists rather than how deep it gets, and it appears across
unrelated stock IsaacGymEnvs tasks at five different values (`dextrack_2025`). What the corpus
shows is the pattern of values; why any of them was chosen is not in the record.

The rest of Table 4 is largely empty, and the emptiness is a result. Sixty-nine of its 165 cells
are values no parsed source stated, 41 percent, which is the share its own footer counts; over the
150 cells outside the engine-key column the share is 46 percent. No engine paper states a default
physics timestep. Three report one for a named experiment, and the timestep column reports those
experiment settings. Isaac Gym's cell is its Shadow Hand step, from the only per-task timestep
table any engine paper here publishes, which runs 1/120 s for Shadow Hand and Allegro, 1/200 s for
ANYmal and TriFinger and 1/60 s for Franka (`isaacgym_2021`, Table 4). MuJoCo's 0.01 s is the
27-DoF humanoid test's step and ComFree-Sim's 0.002 s is its benchmark step, against a stated
stability limit near 0.02 s. Four engines state a solver iteration count and seven ship any
dexterous hand at all. The license column answers a question a reader choosing an engine actually
has, and thirteen of fifteen rows do not answer it.

{{table:table4_simulators}}

## 4.3 GPU-parallel engines and their throughput

**The GPU-parallel turn.** Isaac Gym set the pattern. Physics, observations, rewards and
actions stay on the GPU, and PhysX resolves contacts with the Temporal Gauss-Seidel sweep
described above. Its per-task timesteps are published, which is rare: the Shadow Hand runs a
1/120 s physics step under a 1/60 s control step, or 1/20 s in the OpenAI variant. The result
that reorganised the field is that reproducing OpenAI's Shadow Hand cube reorientation took
under an hour on one A100, against 30 hours on 6144 CPU cores and 8 V100s (`isaacgym_2021`,
Sec. 6.4.1). Thirty-five of the 112 method papers in this corpus run on it.

Orbit and Isaac Lab moved the stack to PhysX 5, and the dexterous offering is thinner than the
predecessor's: the first-party suite is lifting, grasping and reorienting with the KUKA Allegro
hand, while Shadow and Ability hands appear only through third-party grasp evaluation
(`isaaclab_2025`, Sec. 7.2.3). MJX and MuJoCo Playground took the other route, putting MuJoCo's
own solver on the GPU through JAX at the cost described above. MuJoCo Warp ports the same solref
and solimp soft-constraint rows to NVIDIA Warp, and its README states that the legacy PGS solver
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
or MuJoCo's soft constraint rows under Warp, and those two make different contact errors. The name
also fails to fix the physics inside one engine. MuJoCo's convex solver is a family, interior
point or projected Newton, conjugate gradient or Gauss-Seidel (`mujoco_2012`, Sec. II-D), and
MuJoCo Warp supports neither PGS nor the noslip pass. PhysX 4 and PhysX 5 differ in whether
non-convex rigid bodies get SDF collision, which is a contact-geometry difference between Isaac
Gym and Isaac Lab under one vendor name (`orbit_2023`, `isaaclab_2025`). Naming a simulator no
longer names its physics. Papers should report the backend and the solver beside the framework.

**Reported throughput, and why the numbers do not compare.** Four headline figures measure four
different quantities. Isaac Gym reports parallel environment steps per second with physics,
observations and rewards on device: 150,000 for the Shadow Hand at 16,384 environments on one
A100. Isaac Lab reports frames per second in training, which includes the learning update: over
900,000 for the DextrAH teacher task at 16,384 environments on eight RTX Pro 6000 GPUs, with no
single-GPU dexterous number anywhere in the paper. ManiSkill3 reports "up to 30,000+ FPS" with
RGBD and segmentation on one RTX 4090, measured over 1000 random actions with reward and
termination removed from the timing, and does not state the environment count behind the figure
(`maniskill3_2024`). Orbit reports a 125,000 FPS physics-only ceiling on an RTX 3090, also with
no environment count (`orbit_2023`, Sec. VII).

The one number reported cleanly enough to reuse is MuJoCo Playground's, in PPO steps per second on
a single A100 over five seeds. LeapCubeReorient runs at 76,354 ± 143 and PandaRobotiqPushCube at
487,341 ± 4,346. Same hardware, same measurement, same codebase, a factor of 6.4 between two
environments. It is not a factor from the task in isolation. Playground tunes solver iterations,
line-search iterations, timestep and contact bounds per environment, with values as far apart as
one and four solver iterations (`mujoco_playground_2025`, Table III), and it does not print the
two configurations side by side. That omission is what makes the two figures incomparable. The
same confound sits inside Isaac Gym's paper on one A100: 700,000 environment steps per second for
Ant, 200,000 for Humanoid, 150,000 for the Shadow Hand. A training-loop FPS is also mostly not a
measurement of physics. Playground breaks the fractional cost down on an RTX 4090: for
CartpoleBalance, physics is 0.02, rendering 0.06, inference 0.01 and the policy update 0.91, and
the policy update still dominates on the Franka task.

Cross-framework comparisons add further free parameters. ManiSkill2's PickCube table takes the
best result over 16 to 512 environments for each system (`maniskill2_2023`, Table 1a), giving
ManiSkill2 with a render server 2487 ± 24 FPS at its optimum of 64 environments against Isaac
Gym's 865 ± 35 at its optimum of 512. The env-count tuning is the second problem here. The first
is that the two systems are not the same kind of thing: ManiSkill2 runs rigid-body physics on CPU
worker processes behind a shared GPU render server, Isaac Gym runs physics on the GPU, and its own
paper says so plainly. The measured quantity includes 128×128 rendering at 500 Hz simulation and
20 Hz control for both, so this is a visual sample-collection loop rather than two physics
engines. Its authors add the fidelity caveat themselves, and Playground is equally explicit that
its cross-simulator plot borrows its Isaac Lab and ManiSkill3 numbers from the ManiSkill3 paper.
Several sources give no number at all: MuJoCo Warp's README points to an external nightly
dashboard, and Newton's and Genesis's READMEs contain no FPS or speedup anywhere.

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
contact physics of its own. Its only sim-to-real number is a tactile pose-estimation task, at 1.66
± 0.16 mm with color-jitter augmentation against 0.76 ± 0.07 mm for a model trained on 128 real
datapoints (`tacto_2020`, Table II).

Taxim is example-based rather than simulated, with an optical model calibrated from 50 real
indentations, and it beats TACTO on every optical-similarity metric against real images. Its
marker-motion model is calibrated against an ANSYS FEM, and the errors are 1.00×10^-2 mm real
against FEM, 1.02×10^-2 mm real against Taxim, and 3.96×10^-3 mm FEM against Taxim. Taxim tracks
its own reference more tightly than that reference tracks reality, so its residual is bounded
below by the calibration target. The authors also state that they simulate quasi-static contact
only, with slip left as future work (`taxim_2021`, Sec. V). Slip is what a hand needs.

Tactile Genesis inverts the thread. It implements two penetration-depth backends on the
collision geometry, an analytic SDF query and a BVH raycast, and uses the depth as the sensor
signal rather than as an error, so the quantity every other engine treats as a defect sets this
one's operating point.

**The sim-to-real gap for hands.** Most of what is written about this gap is attribution
without measurement. PenSpin asserts that the pure physics gap "cannot be bridged by extensive
domain randomization alone" while reporting no experiment that isolates it (`penspin_2024`).
MuJoCo Playground attributes its LEAP hand failures to physical flex in low-cost hardware and
names more accurate collision geometries as the fix, without measuring either. DeXtreme lists
four candidate causes for its shortfall, including a malfunctioning Allegro thumb used in most
trials, and disambiguates none by experiment (`dextreme_2022`).

What has been measured is narrower, and section 7 collects the transfer numbers. The one result
that links a quantified model error to transfer is a humanoid recipe paper, which ranks its system
identification runs by dynamics-model MSE and pairs each with real success over 10 trials: the
lowest-MSE model grasps 8 out of 10, the median-MSE model 3 out of 10, the highest-MSE model 0 out
of 10 (`humanoid_sim2real_recipe_2025`, Table 1). Where a cause has been pinned down elsewhere it
is usually perception or actuation, not contact. OpenAI's pose estimator has 3.12 mm error on
rendered images and 9.27 ± 4.02 mm on 992 real ones, and PDDM reports a camera tracker with 5 mm
average error and 20 ms latency as the unmodelled source in its real numbers (`pddm_2019`, App.
C).

The one paper that looks at the contact side is usually read backwards. DeXtreme's real-to-sim
replay interpenetrated because the replayed poses carried the pose estimator's error, not
because the contact model failed, and the paper says so: it could not calibrate physics against
the real system because the state it replayed was already wrong. The commonly cited reading,
that the contact model was at fault, is not what the sentence says.