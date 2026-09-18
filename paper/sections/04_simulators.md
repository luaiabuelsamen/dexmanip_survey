# 4. Simulators and the physics underneath

## 4.1 What a dexterous simulation must get right

The clearest demonstration that hands are the hard case came from a benchmark that was not about
hands. Erez et al. built a 35-DOF arm modelled on the Shadow Hand, closed it around a capsule with
fixed spring-dampers, and asked five engines for the largest timestep at which the object was
still in the hand at the end of the run. MuJoCo held the grasp at 16 ms, PhysX at 2 ms, ODE at
0.25 ms and Bullet at 0.03 ms, a spread of a factor of 500
(`physics_engine_comparison_2015`, Sec. IV-D). On a falling 25-DOF humanoid the same engines
differ by about a factor of four in speed, and on a pile of 27 capsules the ranking inverts. The
grasp is the test that separates them. The authors wrote MuJoCo and disclose it, and their
timesteps are log-spaced, so each is good only to a factor of two.

A grasp is hard for nameable reasons. It is many contacts at once, all persistent, all near
stiction, on an object much lighter than the mechanism holding it. Persistence and multiplicity
make the problem hyperstatic, and Le Lidec et al. show that per-contact solvers of the projected
Gauss-Seidel family, and RaiSim's, then inject spurious internal jamming forces at stiction that
vanish only once the object slides. The mass ratio makes it ill-conditioned, and in their
stacked-cube test at a 10^3 to 10^-3 kg ratio those same per-contact methods fail to converge.
Global methods with proximal regularisation stay robust in both cases
(`contact_models_comparison_2023`, Sec. IV-A). Locomotion is forgiving by comparison. In their MPC
task on a Solo-12 quadruped on flat ground the contact model and solver choice "hardly affects"
the tracked base velocity, and only on rough, slippery terrain do RaiSim and CCP deviate. A
walking robot makes and breaks a few contacts against ground far heavier than itself. A hand does
neither.

Speed enters by the same door, because contact resolution is where the cost is, and on MJX it does
not even scale with the contacts that exist. MuJoCo Playground reports that contact time scales
with the number of possible contacts rather than the active ones, because JAX requires static
shapes, which is why its tasks carry hand-tuned `max_contact_points` and `max_geom_pairs`
overrides (`mujoco_playground_2025`, Sec. VI). For a hand the bound is set for the worst case.

Figure 3 sets out the stages of one simulation step and marks where the engines used for hands
diverge. Two stages matter below: contact generation, where convex decomposition replaces the mesh
the renderer draws, and the solver, where a fixed iteration budget leaves a stiff contact
unconverged and therefore resolved as overlap.

## 4.2 Contact models and solvers, engine by engine

Table 4 is the engine-by-engine comparison, one row per simulator, built only from what a note
confirmed. Le Lidec et al. supply the taxonomy that organises it, checking each formulation
against the Signorini condition, Coulomb's law, and the maximum dissipation principle. Linear
complementarity, the family used by Bullet, ODE and PhysX, satisfies Signorini alone, because
linearising the friction cone to a pyramid biases friction toward its corners. The cone
complementarity problem satisfies the other two but relaxes Signorini, so contact acts at a
distance of size Δt·µ·‖c_T‖ and their dragged cube slides above the floor. The full nonlinear
problem satisfies all three and is non-convex (`contact_models_comparison_2023`, Table II).

MuJoCo sits outside that taxonomy deliberately. Its contact is soft, convex and
complementarity-free, and penetration is a state variable rather than an error: the violation
distance is driven by a critically damped stabiliser, and for an object resting under gravity the
steady-state depth has a closed form independent of the object's mass
(`mujoco_convex_contact_2014`, Sec. V). The original paper says why non-penetration is a cost and
not a constraint, "otherwise the inverse dynamics could not be defined for trajectories that
happen to have penetration" (`mujoco_2012`, Sec. II-D). The model is built to stay well-defined
while the bodies overlap. Le Lidec et al., who compete with it, call that compliance a "numerical
trick designed to circumvent the issues due to hyper-staticity or ill-conditioning at the cost of
impairing the simulation". Drake's SAP takes the convex middle, bounding penetration at about
2.5×10^-5 m for a point mass at δt = 10^-2 s (`castro_sap_contact_2021`).

The first of two concrete measurements comes from the other end. Dojo solves a hard-contact
nonlinear complementarity problem with an exact second-order friction cone, by an interior-point
method converging within 15 iterations. Its Table II drops an Atlas humanoid and reports
foot-floor penetration against the timestep. MuJoCo penetrates −28 mm at Δt = 0.01 s and −46 mm at
Δt = 0.001 s, and fails outright at Δt = 0.1 s. Dojo records +1×10^-12 mm at Δt = 0.1 s and
+8×10^-6 mm at Δt = 0.001 s, so its feet stay above the floor at every step size tested
(`dojo_2022`, Sec. V-A). That is one scenario, on the authors' own configuration of the competing
engine, and Dojo demonstrates no dexterous hand anywhere in the paper. The price is in its
Table V, where MuJoCo is fastest on every system tested, 0.335 s against Dojo's 1.159 s on a
Franka Panda over 1000 steps. Read Erez's grasp table backwards and the trade is priced: tens of
millimetres of overlap on a drop test is what buys the 16 ms timestep that holds a grasp where
Bullet needs 0.03 ms.

The GPU era moved that knob rather than removing it. ComFree-Sim resolves contact in closed form
in the dual cone of the friction cone, with no complementarity solve, so penetration becomes an
explicit tuning parameter and the paper reports it. On a drop test of convex primitives about 5 cm
across at dt = 0.002 s, averaged over all detected contacts, MuJoCo Warp penetrates 1.7 ± 4.9 mm
and ComFree-Sim ranges from 3.9 ± 6.9 mm to 0.9 ± 1.5 mm as its stiffness and damping are raised.
Millimetres, on primitives the size of a fingertip, in the GPU backend that both MuJoCo Playground
and Newton build on.

That brings Table 4's most important column. Two of the 15 engines report a penetration depth
exposed to the user, Dojo and ComFree-Sim, and both are engines whose paper is about contact
accuracy. Four are recorded as not exposing it: Brax, Isaac Gym, Isaac Lab and Orbit. Nine rows
are blank, meaning no parsed source stated it either way. The word "penetration" appears nowhere
in the Isaac Gym paper, whose tensor API exposes net contact force per rigid body and no depth,
and Isaac Lab's contact sensor reports force, duration and an average contact point but defines no
contact-quality metric. Those two simulators carry 41 of the 110 method papers in this corpus. The
depth is created by the solver on every step and is not handed to the user.

A policy will use what the user cannot see. DexTrack's released configs set PhysX's
`max_depenetration_velocity`, which bounds how fast overlapping bodies are pushed apart, to either
10.0 or 1000.0 depending on the task variant, with no explanation in the paper or in a config
comment. The paper defines a maximum hand-object penetration depth, applies it only to its input
kinematic references, and presents tolerance of "severe hand-object penetrations" as evidence of
robustness (`dextrack_2025`, App. B). TopoRetarget is the counterexample, reporting max penetration
depth and the share of frames above 2 mm over 25 ContactPose grasps: 1.07 mm and 0.00% for its own
retargeting, against 20.12 mm and 84% of frames for Mink and 22.22 mm and 96% for GeoRT
(`toporetarget_2026`, Table 1). Those are retargeted reference trajectories, which are placement
rather than simulated physics, and they are not re-measured after RL tracking. The one method in
the corpus that measures penetration carefully measures it on the input.

The rest of Table 4 is largely empty, and the emptiness is a result. Sixty-eight of its 165 cells,
41 percent, are values no parsed source stated. Three of 15 engines state a default physics
timestep, four state a solver iteration count, and seven ship any dexterous hand at all.

## 4.3 The GPU-parallel turn

Isaac Gym set the pattern. Physics, observations, rewards and actions stay on the GPU, and PhysX
uses a Temporal Gauss-Seidel solver rather than a classical PGS or LCP scheme. Its per-task
timesteps are published, which is rare: the Shadow Hand runs a 1/120 s physics step under a 1/60 s
control step, or 1/20 s in the OpenAI variant. The result that reorganised the field is that
reproducing OpenAI's Shadow Hand cube reorientation took under an hour on one A100, against 30
hours on 6144 CPU cores and 8 V100s (`isaacgym_2021`, Sec. 6.4.1). Thirty-five of the 110 method
papers in this corpus run on it.

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
solver-dependent, not a property of the engine, which is how Table 4 records it. The consequence
reaches upward. Isaac Lab's code already exposes a `--physics newton_mjwarp` backend switch in its
hands demo, and its roadmap announces Newton integration. An experiment reported as Isaac Lab may
be running PhysX 5 with TGS, or MuJoCo's soft constraint rows under Warp, and those two make
different contact errors. Naming a simulator no longer names its physics. Papers should report the
backend and the solver beside the framework.

## 4.4 Throughput, and why the reported numbers do not compare

Four headline figures measure four different quantities. Isaac Gym reports parallel environment
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
487,341 ± 4,346. Same hardware, same measurement, same codebase, a factor of 6.4 from the task
alone. The same confound sits inside Isaac Gym's paper on one A100: 700,000 environment steps per
second for Ant, 200,000 for Humanoid, 150,000 for the Shadow Hand. A training-loop FPS is also
mostly not a measurement of physics. Playground breaks the fractional cost down on an RTX 4090:
for CartpoleBalance, physics is 0.02, rendering 0.06, inference 0.01 and the policy update 0.91,
and the policy update still dominates on the Franka task.

Cross-framework comparisons add a further free parameter, because the environment count is itself
tuned per framework. ManiSkill2's PickCube table takes the best result over 16 to 512 environments
for each system (`maniskill2_2023`, Table 1a), giving ManiSkill2 with a render server 2487 ± 24 FPS at its optimum of 64
environments against Isaac Gym's 865 ± 35 at its optimum of 512. Its authors add the caveat
themselves, that a fair comparison remains hard because fidelity differs, and Playground is
equally explicit that its cross-simulator plot borrows its Isaac Lab and ManiSkill3 numbers from
the ManiSkill3 paper. Several sources give no number at all: MuJoCo Warp's README points to an
external nightly dashboard, and Newton's and Genesis's READMEs contain no FPS or speedup
anywhere.

The failure reaches past the engine papers into the methods. Of the 47 corpus method papers that
name a GPU-batched simulator, 19 state no environment count anywhere, and Isaac Lab's own paper
states no physics timestep, no decimation and no solver iteration count for any task. A throughput
figure is interpretable only with the environment count, the GPU, the timesteps, the solver
iteration budget, and a statement of whether rendering and the learning update sit inside the
measurement. Almost nobody reports all five.

## 4.5 Tactile simulation and what it is calibrated against

The three tactile simulators in this corpus calibrate against three different things, and none of
them is a manipulation outcome. TACTO is a rendering layer over a host engine, by default
PyBullet's rigid contact model. It reads post-solve link poses and the engine's reported normal
force and maps that force to gel-mesh deformation at the rendering level, so it contributes no
contact physics of its own. Its only sim-to-real number is a tactile pose-estimation task, at
1.66 ± 0.16 mm with colour-jitter augmentation against 0.76 ± 0.07 mm for a model trained on 128
real datapoints (`tacto_2020`, Table II).

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
a fidelity measurement, because the real XHand1 SDK exposes only an aggregate contact pressure.

## 4.6 The sim-to-real gap for hands

Most of what is written about this gap is attribution without measurement. PenSpin asserts that
the pure physics gap "cannot be bridged by extensive domain randomization alone" while reporting
no experiment that isolates it (`penspin_2024`). MuJoCo Playground attributes its LEAP hand
failures to physical flex in low-cost hardware and names more accurate collision geometries as the
fix, without measuring either. DeXtreme lists four candidate causes for its shortfall, including a
malfunctioning Allegro thumb used in most trials, and disambiguates none by experiment
(`dextreme_2022`).

What has been measured is narrower. The size of the gap is known wherever a paper runs the same
policy in both places. OpenAI's Shadow Hand block reorientation reaches 43.4 ± 13.8 mean
consecutive successes in simulation and 18.8 ± 17.1 on the physical hand over 10 trials per
policy (`openai_dexterity_2018`, Table 3). Visual Dexterity reports 96 percent in simulation against 81 percent on the real D'Claw
for training objects, and 85 against 45 percent for held-out ones, over 20 real trials on each of
12 objects (`visual_dexterity_2022`, Table 1). Roughly half, and worse as the task hardens.

Three results identify causes with evidence. A humanoid recipe paper ranks its system
identification runs by dynamics-model MSE and pairs each with real success over 10 trials: the
lowest-MSE model grasps 8 out of 10, the median-MSE model 3 out of 10, the highest-MSE model 0 out
of 10 (`humanoid_sim2real_recipe_2025`, Table 1). That is the corpus's clearest measured link
between a quantified model error and transfer. OpenAI's per-category randomisation ablation on the
physical Shadow Hand gives median consecutive successes of 13 with all randomisations, 8.5 without
observation noise, 2 without physics randomisations, and 0 with none. DemoStart shows that gap
size is a function of design choice rather than a fixed property of the simulator: its full method
scores 99.0 percent in simulation and 64 percent over 100 real episodes, dropping photorealistic
data moves those to 97.0 and 29, and using one camera moves them to 97.0 and 17
(`demostart_2024`, Table IV). The simulation number barely moves while the real number collapses.

Where a cause has been pinned down it is usually perception or actuation, not contact. OpenAI's
pose estimator has 3.12 mm error on rendered images and 9.27 ± 4.02 mm on 992 real ones, and PDDM
reports a camera tracker with 5 mm average error and 20 ms latency as the unmodelled source in its
real numbers (`pddm_2019`, App. C). The contact side stays unmeasured, and one paper records why.
DeXtreme replayed real cube states back into simulation with physics enabled and found the replay
"sometimes resulted in interpenetrations", so the cube's physics parameters could not easily be
calibrated. The interpenetration the engine does not expose is also what blocks the
calibration that would let anyone attribute the gap to contact at all. The only direct measurement
of simulator fidelity against hardware in this corpus is Dojo's, an average final-position gap of
about 0.5 cm over 5 box-pushing trials. It is a parallel-jaw arm pushing a box, and there is no
equivalent number for a hand.
