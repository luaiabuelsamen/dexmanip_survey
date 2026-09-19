# 4. Simulators and the physics underneath

## 4.1 Requirements of a dexterous simulation

The clearest demonstration that hands are the hard case came from a benchmark that was not about
hands. Erez et al. built a 35-DOF arm modelled on the Shadow Hand, closed it around a capsule with
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
corpus, and the three are not ordered here. A fourth item on the figure is not a source of overlap
at all. It is a mismatch between the geometry the solver uses and the geometry the renderer draws,
and it runs in both directions.

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

MuJoCo is inside that taxonomy rather than outside it. Le Lidec et al. classify it as CCP-MuJoCo,
a convex relaxation solved by a Newton method on the primal QCQP, in the same family as CCP-Drake,
the SAP-style scheme (Table III). The relaxation makes two errors of opposite sign in one engine.
A loaded contact carries a violation, and a sliding contact carries force at a positive gap.
Drake's SAP inherits the same pair, and its gliding effect at distance φ ≈ δt·µ·‖v_t‖
"unfortunately does not go away as δt → 0" (`castro_sap_contact_2021`, Sec. V-A). Le Lidec et al.
call that compliance a "numerical trick designed to circumvent the issues due to hyper-staticity
or ill-conditioning at the cost of impairing the simulation".

The depth a loaded contact carries is a chosen number. In a regularised formulation the
steady-state violation at a contact is the normal load times the compliance. It is zero at zero
load and it grows with the load carried. MuJoCo drives that violation coordinate with a critically
damped stabiliser parameterised by ε and κ, and for an object resting under gravity the
steady-state depth has a closed form independent of the object's mass
(`mujoco_convex_contact_2014`, Sec. V). The closed form did not survive the parse of that paper,
so the cancellation is quoted and the algebra is not. Neither MuJoCo paper states why mass
cancels, and the explanation this survey offers is its own inference rather than a cited one: the
regulariser is scaled by the inverse effective inertia at the contact, so compliance falls as 1/m
exactly as the gravity load rises as m. The nearest support in a parsed source is for a different
solver of the same engine, MuJoCo's diagonal solver, a "mass-aware spring-damper" that uses the
diagonal of the A matrix to keep contacts critically damped (`mujoco_2012`, Sec. II-E). This is
not a penalty spring, and depth is not always non-zero. The impulse solves a regularised convex
program over the whole contact set rather than a per-contact function of the gap, both MuJoCo
papers reject spring-dampers by name, and the 2012 ball-drop figure is captioned "there is no
penetration" (`mujoco_2012`, Fig. 2).

The first of two concrete measurements comes from the other end. Dojo solves a hard-contact
nonlinear complementarity problem with an exact second-order friction cone, by an interior-point
method converging within 15 iterations on the three robots of its convergence study. Its Table II
drops an Atlas humanoid and reports foot-floor penetration against the timestep. MuJoCo penetrates
−28 mm at Δt = 0.01 s and −46 mm at Δt = 0.001 s, while Dojo stays above the floor at every step
tested (`dojo_2022`, Sec. V-A). The MuJoCo column is not a trend. A ten-times-smaller step
produces more overlap, which no timestep-independent stabiliser does. Either that configuration
ties the compliance to Δt, or the quantity is an impact transient on a drop. Neither reading is a
steady-state grasp depth.

Drake's SAP quotes 2.5×10^-5 m at δt = 10^-2 s and 2.5×10^-7 m at δt = 10^-3 s, three and five
orders of magnitude below Dojo's two MuJoCo cells at the same steps, on an engine that is also
compliant (`castro_sap_contact_2021`, Sec. V-B). Those two figures are analytical bounds for a
single point mass at rest on a plane under that paper's near-rigid stiffness rule, not measured
depths, and they are not a Drake grasp-penetration number: a point-mass bound and a humanoid drop
transient differ in load, effective inertia and regime, so the distance between them is not a
measurement of anything. What the pair of engines does show is that in a compliant formulation the
depth follows from a stiffness that someone chose.

Dojo's Table V times 1000 steps of forward simulation with gradients, at a matched Δt = 0.01 s,
for engines that are not all computing gradients. MuJoCo is fastest on every system, 0.335 ± 0.001
s against Dojo's 1.159 ± 0.077 s on a Franka Panda, and the authors call the comparison difficult
because Dojo is stable at five times the step size (Sec. VI-B). What the regularisation buys, on
Le Lidec's reading quoted above, is conditioning on a hyperstatic problem, and the depth it costs
is tuned separately. Whether that is also what holds Erez's grasp at 16 ms is a question his data
do not answer. His planar chain is contact-free, so its numbers speak to the coordinate
formulation and not to contact: MuJoCo runs at 243.2 kHz there against Bullet's 22.8 and PhysX's
6.4, and Bullet's articulated Featherstone mode at 81.4 kHz beats every Cartesian-coordinate
engine (`physics_engine_comparison_2015`, Sec. IV-B). Those are throughput in evaluations per
second, not a largest-stable-timestep result, and the articulated Bullet mode was never run on the
grasp test at all, being usable only in tests without contact (Appendix). Joint coordinates
explain the contact-free speed advantage. The grasp timestep is a contact result, and the paper
attributes it to nothing: it reports that the other engines go unstable and "effectively simulate
a different physics model which can no longer hold the object" (Sec. IV-D), without an experiment
that separates the coordinate formulation from the soft absorption of penetration.

The GPU era moved the compliance knob rather than removing it. ComFree-Sim resolves contact in
closed form in the dual cone of the friction cone, so penetration becomes an explicit tuning
parameter and the paper reports it. On a drop test of convex primitives about 5 cm across at dt =
0.002 s, MuJoCo Warp penetrates 1.7 ± 4.9 mm and ComFree-Sim runs from 3.9 ± 6.9 mm at k_user =
0.1 down to 0.9 ± 1.5 mm at k_user = 0.5, though its prose describes the opposite direction from
its own table (`comfree_sim_2026`, Sec. IV-A). Its impedance acts on the signed gap through the
"identical" default hyperparameter API as MuJoCo's solver, so the knob it is credited with
exposing is one MuJoCo users already set. Those are 5 cm primitives under their own weight, not a
fingertip loaded by a grasp, and depth scales with the normal load. Nobody has published the
fingertip number. The baseline it measures against is MuJoCo Warp, which Newton builds on and
which MuJoCo Playground names as its intended replacement for JAX (`mujoco_playground_2025`, Sec.
VI).

That brings Table 4's most important column, and the claim it does not support. The column records
whether a parsed source reported a penetration depth, not what an engine can compute. Two of the
15 engines report one, Dojo and ComFree-Sim, and both are engines whose paper is about contact
accuracy. Four are recorded as not reporting it: Brax, Isaac Gym, Isaac Lab and Orbit. Nine rows
are blank. The word "penetration" appears nowhere in the Isaac Gym paper, and Isaac Lab's contact
sensor reports force, duration and an average contact point with no contact-quality metric. The
Isaac family carries 42 of the 112 method papers in this corpus.

**The tooling exists and the number is still not recorded.** NVIDIA's own IsaacGymEnvs repository
computes interpenetration depth in simulation. Its IndustReal tasks load plug and socket meshes
into Warp, sample points on one, query them against the other, and reduce to a per-environment
maximum interpenetration distance (`code/md/isaacgym_2021.md`, lines 8809 to 8862). The policy
update is gated on that number. Environments are split on whether their maximum stays under a
threshold, the reward of those that survive is scaled down as the maximum approaches it, and the
threshold itself is `interpen_thresh: 0.001`, commented as the largest allowed interpenetration
between plug and socket (lines 3630 and 3753). That is a shipped Isaac Gym task measuring
simulated interpenetration per environment at a millimetre threshold, during RL, and acting on it.
Table 4 records Isaac Gym as not exposing penetration, and so does its row in the corpus, which
the code parse in that same corpus contradicts. Tactile Genesis makes the point from the other
side, shipping penetration depth as a sensor on an analytic SDF backend and a BVH backend
(`tactile_genesis_2026`, App. A.1), while Table 4 leaves the Genesis cell blank. The depth is
computable from the poses and the meshes in a few lines of Warp, and the field's own benchmark
repository already does it. Interpenetration in a dexterous rollout is a setting nobody records
and a measurement nobody takes.

A policy will exploit what nobody looks at. DexTrack's configs carry PhysX's
`max_depenetration_velocity` at 10.0 or 1000.0 depending on the task variant, with no explanation
in the paper or in a config comment (`dextrack_2025`). The same parameter appears across unrelated
stock IsaacGymEnvs tasks at 5.0, 10.0, 100.0 and 1000.0, at five places in the same parsed file,
so DexTrack inherited a template rather than choosing per variant. The parameter caps the rate at
which the solver pushes overlapping bodies apart, so it sets how long an overlap persists and how
violently it is undone, not how deep the overlap gets. The one knob here that governs
interpenetration behaviour is being copied without being read. DexTrack's paper defines a maximum
hand-object penetration depth, applies it only to its input kinematic references, and presents
tolerance of "severe hand-object penetrations" as evidence of robustness (App. B).
`toporetarget_2026` is the one corpus method that reports the number carefully, and it reports it
on retargeted references rather than on a rollout, which section 7 takes up.

The rest of Table 4 is largely empty, and the emptiness is a result. Sixty-nine of its 165 cells
are values no parsed source stated, which is 69 of the 150 cells outside the engine-key column, or
46 percent, and the table's own footer counts the same 69. No engine paper states a default
physics timestep. Three report one for a named experiment, and the timestep column reports those
experiment settings. Isaac Gym's cell is its Shadow Hand step, from the only per-task timestep
table any engine paper here publishes, which runs 1/120 s for Shadow Hand and Allegro, 1/200 s for
ANYmal and TriFinger and 1/60 s for Franka (`isaacgym_2021`, Table 4). MuJoCo's 0.01 s is the
27-DoF humanoid test's step and ComFree-Sim's 0.002 s is its benchmark step, against a stated
stability limit near 0.02 s. Four engines state a solver iteration count and seven ship any
dexterous hand at all. The licence column answers a question a reader choosing an engine actually
has, and thirteen of fifteen rows do not answer it.

{{table:table4_simulators}}

## 4.3 GPU-parallel engines and their throughput

**The GPU-parallel turn.** Isaac Gym set the pattern. Physics, observations, rewards and actions stay on the GPU, and PhysX
resolves contacts with the Temporal Gauss-Seidel sweep described above. Its per-task timesteps are
published, which is rare: the Shadow Hand runs a 1/120 s physics step under a 1/60 s control step,
or 1/20 s in the OpenAI variant. The result that reorganised the field is that reproducing
OpenAI's Shadow Hand cube reorientation took under an hour on one A100, against 30 hours on 6144
CPU cores and 8 V100s (`isaacgym_2021`, Sec. 6.4.1). Thirty-five of the 112 method papers in this
corpus run on it.

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

**Reported throughput, and why the numbers do not compare.** Four headline figures measure four different quantities. Isaac Gym reports parallel environment
steps per second with physics, observations and rewards on device: 150,000 for the Shadow Hand at
16,384 environments on one A100. Isaac Lab reports frames per second in training, which includes
the learning update: over 900,000 for the DextrAH teacher task at 16,384 environments on eight RTX
Pro 6000 GPUs, with no single-GPU dexterous number anywhere in the paper. ManiSkill3 reports "up
to 30,000+ FPS" with RGBD and segmentation on one RTX 4090, measured over 1000 random actions with
reward and termination removed from the timing, and does not state the environment count behind
the figure (`maniskill3_2024`). Orbit reports a 125,000 FPS physics-only ceiling on an RTX 3090,
also with no environment count (`orbit_2023`, Sec. VII).

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
± 0.16 mm with colour-jitter augmentation against 0.76 ± 0.07 mm for a model trained on 128 real
datapoints (`tacto_2020`, Table II).

Taxim is example-based rather than simulated, with an optical model calibrated from 50 real
indentations, and it beats TACTO on every optical-similarity metric against real images. Its
marker-motion model is calibrated against an ANSYS FEM, and the errors are 1.00×10^-2 mm real
against FEM, 1.02×10^-2 mm real against Taxim, and 3.96×10^-3 mm FEM against Taxim. Taxim tracks
its own reference more tightly than that reference tracks reality, so its residual is bounded
below by the calibration target. The authors also state that they simulate quasi-static contact
only, with slip left as future work (`taxim_2021`, Sec. V). Slip is what a hand needs.

Tactile Genesis inverts the survey's thread. It implements two penetration-depth backends on the
collision geometry, an analytic SDF query and a BVH raycast, then binarises the result with
Schmitt hysteresis at 5×10^-4 m on and 2×10^-4 m off. Here the penetration depth is the sensor
signal, so the quantity every other engine treats as an error sets this sensor's operating point.
Against a real GelSight it reports relative marker RMSE of 0.329 in dilation and 0.174 in shear,
against HydroShear's 0.403 and 0.217, with each simulator tuned to match the real image first
(`tactile_genesis_2026`, Fig. 2). Its own sim-to-real check is a matched success count rather than
a fidelity measurement. The real XHand1 SDK reports a per-taxel raw pressure field as well as an
aggregate contact pressure, but documents no taxel positions or response characteristics, so the
raw field cannot be registered to the simulated probe layout and only the aggregate is comparable
(App. C). The undocumented calibration is the barrier, not a missing signal.

**The sim-to-real gap for hands.** Most of what is written about this gap is attribution without measurement. PenSpin asserts that
the pure physics gap "cannot be bridged by extensive domain randomization alone" while reporting
no experiment that isolates it (`penspin_2024`). MuJoCo Playground attributes its LEAP hand
failures to physical flex in low-cost hardware and names more accurate collision geometries as the
fix, without measuring either. DeXtreme lists four candidate causes for its shortfall, including a
malfunctioning Allegro thumb used in most trials, and disambiguates none by experiment
(`dextreme_2022`).

What has been measured is narrower, and section 7 collects the transfer numbers. The one result
that links a quantified model error to transfer is a humanoid recipe paper, which ranks its system
identification runs by dynamics-model MSE and pairs each with real success over 10 trials: the
lowest-MSE model grasps 8 out of 10, the median-MSE model 3 out of 10, the highest-MSE model 0 out
of 10 (`humanoid_sim2real_recipe_2025`, Table 1). Where a cause has been pinned down elsewhere it
is usually perception or actuation, not contact. OpenAI's pose estimator has 3.12 mm error on
rendered images and 9.27 ± 4.02 mm on 992 real ones, and PDDM reports a camera tracker with 5 mm
average error and 20 ms latency as the unmodelled source in its real numbers (`pddm_2019`, App.
C).

The contact side stays unmeasured, and the one paper that looks at it is usually read backwards.
DeXtreme's real-to-sim replay interpenetrated because the replayed poses carried the pose
estimator's error, not because the contact model failed. The paper says so: "there is still some
sim-to-real gap in pose estimation. This is manifested when we played back the real states in sim
(real-to-sim) with physics enabled, which sometimes resulted in interpenetrations. Therefore, we
were not able to easily calibrate physics parameters of the cube" (`dextreme_2022`, Sec. 5). A
replayed trajectory is a placement, so the overlap it shows bounds the state estimate rather than
the physics. That is why it could not calibrate the cube, and it is why calibrating contact
against hardware still has no worked example for a hand. The only direct measurement of simulator
fidelity against hardware in this corpus is Dojo's, an average final-position gap of about 0.5 cm
over 5 box-pushing trials. It is a parallel-jaw arm pushing a box, and there is no equivalent
number for a hand.