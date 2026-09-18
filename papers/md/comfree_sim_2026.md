# **ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and Control** 

Chetan Borse<sup>_∗_1</sup> Zhixian Xie<sup>_∗_1</sup> Wei-Cheng Huang<sup>2</sup> Wanxin Jin<sup>_†_1</sup> 

> 1 Intelligent Robotics and Interactive Systems (IRIS) Lab, Arizona State University 

> 2 Siebel School of Computing and Data Science, University of Illinois at Urbana-Champaign 

> _∗_ Co-first author with equal contribution, _†_ Corresponding author (wjin@asu.edu) Project website: https://irislab.tech/comfree-sim/. 



Fig. 1: Performance overview of the ComFree-Sim. In the second row, it shows 2–3 _×_ higher throughput than MuJoCo Warp (MJWarp) in dense contact simulation; in the first row, it enables low-latency model predictive control for in-hand dexterous manipulation; and in the third row, it is used for dynamics-aware motion retargeting with MuJoCo as rollout environments. 

**_Abstract_ — Physics simulation for contact-rich robotics is often bottlenecked by contact resolution: mainstream engines enforce non-penetration and Coulomb friction via complementarity constraints or constrained optimization, requiring perstep iterative solves whose cost grows superlinearly with contact density. We present ComFree-Sim, a GPU-parallelized analytical contact physics engine built on complementarity-free contact modeling. ComFree-Sim computes contact impulses in closed form via an impedance-style prediction–correction update in the dual cone of Coulomb friction. Contact computation decouples across contact pairs and becomes separable across cone facets, mapping naturally to GPU kernels and yielding near-linear** 

C.B. developed the initial implementation of ComFree-Sim and hardware MPC. Z.X. conducted simulation, MPC, and retargeting experiments, and writing. W.C.H. contributed to MPC, discussions, and writing. W.J. led the project and contributed to coding ComFree-Sim. 

**runtime scaling with the number of contacts. We further extend the formulation to a unified 6D contact model capturing tangential, torsional, and rolling friction, and introduce a practical dual-cone impedance heuristic. ComFree-Sim is implemented in Warp and exposed through a MuJoCo-compatible interface as a drop-in backend alternative to MuJoCo Warp (MJWarp). Experiments benchmark penetration, friction behaviors, stability, and simulation runtime scaling against MJWarp, demonstrating near-linear scaling and 2–3** _×_ **higher throughput in dense contact scenes with comparable physical fidelity. We deploy ComFree-Sim in real-time MPC for in-hand dexterous manipulation on a real-world multi-fingered LEAP hand and in dynamics-aware motion retargeting, demonstrating that lowlatency simulation yields higher closed-loop success rates and enables practical high-frequency control in contact-rich tasks.** 

## I. INTRODUCTION 

Scalable physics simulation has become core infrastructure for modern robotics, enabling large-scale data generation for policy training, parallelized sampling for model predictive control (MPC), and end-to-end differentiable pipelines for system design. Recent GPU-accelerated simulators and system-level platforms have greatly improved parallel simulation throughput, lowering the barrier to training and evaluating increasingly complex tasks. Yet, for _contact-rich_ manipulation and locomotion, simulation remains bottlenecked by the same fundamental difficulty: resolving intermittent, unilateral, frictional contacts accurately and efficiently. 

A rigid-body simulation step typically includes collision detection, contact resolution, and time integration [1], [2]. Among these, _contact resolution_ , which computes contact impulses and post-contact velocities, most strongly impacts physical fidelity, numerical stability, and runtime [3]. Main approaches for contact resolution enforce non-penetration and Coulomb friction via the complementarity constraints or equivalent constrained optimization [4]–[6], resulting in iterative per-step solutions whose cost often grows superlinearly with contact counts. This scaling is prohibitive for batched, differentiable simulation and online planning. Even stateof-the-art GPU-parallelized phsyics engines, e.g., MJWarp [7] can exhibit substantial step-time growth in dense contact scenes, complicating real-time deployment. 

To overcome the iterative-solver contact resolution bottleneck, this paper presents **ComFree-Sim** , a GPU-parallelized analytical contact backend for contact-rich simulation. ComFree-Sim builds on _complementarity-free_ contact modeling [8], which resolves contact impulses in closed form through a prediction-based impedance mechanism in the _dual cone_ of Coulomb friction. A key property of this formulation is _decoupling_ : contact resolution is independent across contact pairs and separable across cone facets. This structure maps directly to GPU parallelism, reducing computation complexity from superlinear to linear with respect to contact count. Our empirical results demonstrate that this lightweight analytical formulation preserves physical realism without noticeable degradation. By eliminating repetitive optimization routines, it avoids solver-induced artifacts while preserving frictional feasibility by construction. Importantly, ComFree-Sim is implemented in Warp and exposed through a MuJoCo-compatible interface, enabling it to serve as an accelerated drop-in replacement backend for MJWarp. This paper makes three main contributions: 

- **Unified analytical 6D frictional contact modeling.** We extend the complementarity-free point contact model to a 6D formulation that captures tangential, torsional, and rolling friction within an analytical dual-cone contact resolution framework. 

- **GPU parallelization with stable impedance heuristics.** We develop GPU implementation for the analytical contact resolution and introduce an effective dual-cone impedance heuristic. This preserves a lightweight user-facing parameterization while also supporting learning-based dynamic 

impedance adaptation [9]. 

- **Evaluation from simulation to hardware.** We benchmark ComFree-Sim against MJWarp on penetration depth, various friction behaviors, numerical stability, and runtime scaling. We demonstrate linear scaling and 2–3 times higher throughput in contact-rich scenes with comparable physical fidelity. We deploy ComFree-Sim for real-time MPPI-based MPC for dexterous in-hand manipulation on multi-fingered LEAP hand hardware, showing that faster rollouts translate directly into higher closed-loop success rates and improved practical deployability. 

Together, these results suggest that analytical, lightweight contact resolution can provide a highly competitive and scalable alternative to iterative complementarity-based backends, particularly for the high-frequency, contact-rich rollouts that underpin modern learning and control. 

## II. BACKGROUND AND RELATED WORK 

## _A. Brief Background of Rigid Body Simulation_ 

Mainstream rigid-body simulators for robotics typically follow a time-stepping pipeline with three stages [1], [2]: **collision detection** , **contact resolution** , and **time integration** . Collision detection identifies potentially interacting body pairs and computes geometric contact quantities (e.g., contact points, normals, signed distances), often using a broad phase (BVH or spatial hashing [10]) followed by a narrow phase e.g., GJK [11], EPA [12], or SDF methods [13], [14]. Contact resolution then computes contact impulses and post-contact velocities that satisfy force–motion constraints (Newton’s laws and frictional contact mechanics); these are commonly posed as complementarity-style constraints [4]–[6] to capture the unilateral, hybrid nature of frictional contact, and are typically solved _iteratively_ in practice. Finally, time integration advances the state using the resolved post-contact velocities; for broader comparisons, see recent surveys [2], [3]. 

While this pipeline is shared by most simulators, the dominant differences in physical realism, numerical stability, and runtime often arise in _contact resolution_ [3], where both the contact formulation [4]–[6], [15] and the solver can vary substantially. In this paper, we focus on an _analytical_ contact resolution method: by avoiding per-step complementarity constraints and heavy iterative solves, our approach computes contact impulses in closed form. 

## _B. Robotics Simulators and Platforms_ 

Early physics engines such as ODE [16], Bullet [17], and PhysX [18] were developed mainly for animation and games, prioritizing visually plausible motion over high-fidelity contact dynamics [19]; their _contact resolution_ often adopts simplified contact models and complementarity-style approximations. In contrast, robotics-oriented simulators such as MuJoCo [6], Pinocchio [20], and Drake [21] emphasize efficiency and physics fidelity for planning, control, and policy learning. In particular, MuJoCo and Drake enforce full friction-cone constraints and cast contact resolution as a cone complementarity problem solvable via convex optimization [5]. Driven by large-scale training and hardware acceleration, 

these simulators have been further ported to GPUs/TPUs, with MJX and MJWarp built on MuJoCo and Isaac Gym/Sim [22], [23] built on PhysX as representative examples. 

In parallel, modular system-level platforms provide out-ofthe-box tasks and benchmarks for robot learning and evaluation. Rather than introducing new contact models/solvers, they typically build on existing physics backends and focus on curated assets, task definitions, and integrated modules (e.g., rendering, data generation). Examples include LIBERO [24], OmniGibson [25], ManiSkill [26], IsaacLab [27], and more recent Mjlab [28]. These systems are popular because they support diverse robots and large-scale GPU parallel backends such as PhysX, MJX, and MJWarp, scaling policy learning [29]–[31]. _In contrast, rather than pursuing system-integration innovations, we focus on a new analytical contact-computation backend with a GPU-parallelized implementation, designed to be readily integrated into these task-centric platforms._ 

## _C. Why A Lightweight Yet Competitive Contact Backend?_ 

A major computational bottleneck for scalable simulation is _contact resolution_ . Many simulators enforce contact force– motion constraints by repeatedly solving complementaritystyle systems or equivalent convex programs, leading to _superlinear_ per-step cost that is often at least quadratic in the number of contacts (e.g., dense factorizations, projections, or repeated iterations). This becomes prohibitive for batched, differentiable simulation, and online planning. Although recent parallel simulators enable online samplingbased predictive control with full-order simulation [32], [33], real-time results are still largely limited to contact-sparse or low-frequency control settings [32]–[35]; extending to _dense contact_ and _high-frequency_ control remains challenging due to heavy contact-resolution solves. 

The above demand motivates a _lightweight_ physics backend that avoids heavy per-step complementarity/optimization and has the computational complexity scales _linearly_ with the number of contacts. Meantime, such a backend must remain _competitive_ with mature and widely used simulators (e.g., MuJoCo and their accelerated variants) in stability and task performance, so it can serve as a practical drop-in engine for large-scale training and real-time control. 

## III. COMFREE-SIM: ANALYTICAL CONTACT PHYSICS COMPUTATION AND GPU IMPLEMENTATION 

Complementarity-free (ComFree) contact modeling was proposed in [8] and subsequently demonstrated in contactrich control and learning [9], [36], [37]. Our ComFree-Sim will extend it with (1) a unified 6D contact model covering tangential, torsional, and rolling friction, (2) effective dualcone impedance heuristics, and (3) GPU parallel implementation [38] as a drop-in backend alternative to MJWarp [7]. 

## _A. Generic Complementarity-Free Contact Modeling_ 

Consider multi-joint robot systems (robots, objects, environments) with dry joint friction, joint limits, and frictional 

or frictionless contacts. Over a timestep _dt_ , the dynamics is 



Here, **_q_** and **_v_** are joint position and velocity; **_M_** ( **_q_** ) is the joint-space inertia; _d_ **_v_** is the velocity increment; **_c_** ( **_q_** _,_ **_v_** ) collects bias forces (Coriolis/centrifugal/gravity); **_τ_** is the applied generalized force; **J** ( **_q_** ) is the contact Jacobian; and **_λ_** is the contact force/torque (wrench). We omit dependence on ( **_q_** _,_ **_v_** ) for **_M_** _,_ **_c_** _,_ **J** when clear. Since hard-contact Coulomb friction is ill-defined in continuous time (Painlev´e’s paradox), we interpret **_λ_** as the _step-averaged_ contact wrench, so **_λ_** _dt_ is the contact impulse. 

Complementarity-free contact modeling [8] computes the contact forces _analytically_ , avoiding per-step complementarity constraints and iterative optimization while automatically satisfying frictional constraints. Intuitively, it follows a _prediction–correction_ principle on the dual cone of the friction cone: it first predicts the momentum/velocity under non-contact (smooth) forces, then applies a correction that resolves constraint violations (non-penetration and frictional feasibility) via a residual-based impedance mechanism. For notation simplicity, we below present the single-contact case; the formulation naturally extends to multiple contacts. 

Specifically, the one-step prediction of the system velocity only under non-contact (smooth) forces **_τ_** and **_c_** is 



To handle various frictional behaviors in a unified manner, we consider (1) tangential (sliding) friction, (2) torsional friction about the contact normal, and (3) rolling friction in the tangential plane. We denote the normal force by _λ_<sup>_n_</sup> _∈_ R, the tangential friction impulse by **_λ_**<sup>t</sup> _∈_ R<sup>2</sup> , the torsional friction moment by _m_<sup>tor</sup> _∈_ R, and rolling friction moment by **_m_**<sup>roll</sup> _∈_ R<sup>2</sup> . The (primal) friction cone constraints are 



Here _µ_<sup>_∗_</sup> s are friction coefficients; _µ_<sup>tor</sup> and _µ_<sup>roll</sup> have units of length (interpreted as effective contact-patch radius). 

The corresponding dual cone constraints are defined in constraint-velocity space. Let ( **_v_** _c,_ **_ω_** _c_ ):= **J** **_v_** denote the _relative_ linear and angular velocities between contact bodies, respectively. We decompose **_v_** _c_ :=( _vc_<sup>_n,_</sup><sup>**_v_**t</sup> _c_<sup>)intonormalve-</sup> locity _vc_<sup>_n∈_Randtangentialslipvelocity</sup><sup>**_v_**t</sup> _c_<sup>_∈_R2.Wealso</sup> decompose **_ω_** _c_ :=( _ωc_<sup>tor</sup><sup>_,_</sup><sup>**_ω_**rol</sup> _c_<sup>)intotorsionalangularvelocity</sup> _ωc_<sup>tor</sup> about the contact normal and the rolling angular velocity **_ω_**<sup>rol</sup> _c ∈_ R<sup>2</sup> in the tangential plane. Accordingly, define Jacobian blocks **J** _n,_ **J** t _,_ **J** tor _,_ **J** rol such that 





where _ϕ_ is the signed gap distance between contact bodies. For notation simplicity, we denote each dual cone constraint in (5) as _µ_<sup>s</sup> _∥_ **J** s **_v_** _∥≤_ **J** _n_ **_v_** + _ϕ/dt_ , with s _∈{_ t _,_ tor _,_ rol _}_ . 

To facilitate computation, we approximate each quadratic dual-cone constraints (5) with linear polyhedral constraints. For each s _∈{_ t _,_ tor _,_ rol _}_ , choose a symmetric set of _n_ s unit directions _{_ **_d_**<sup>(</sup> s<sup>_j_)</sup><sup>_}n_</sup> _j_ =1<sup>sspanningthecorrespondingsubspace,</sup> and define the directional (row) Jacobian **J** s<sup>(</sup><sup>_j_)</sup> := ( **_d_**<sup>(</sup> s<sup>_j_))</sup><sup>_⊤_</sup><sup>**J**s.</sup> This yields the linearized inequalities: 



where 



and **J**<sup>(</sup> s<sup>_j_)</sup> corresponds to the _j_ -th polyhedral face, and _≥_ 0 is applied _elementwise_ . 

The contact force/torque, based on complementarity-free contact modeling, is analytically computed 



where ( _x_ )+ := max( _x,_ 0) is applied element-wise. Here, **˜J** s **_v_**<sup>+</sup> smooth<sup>_dt_+</sup><sup>**˜**</sup><sup>**_ϕ_**measures the violation (“penetration”) of the</sup> dual-cone constraints under the predicted smooth velocity **_v_**<sup>+</sup> smooth<sup>,and</sup><sup>_K_(</sup><sup>**_q_**)and</sup><sup>_D_(</sup><sup>**_q_**)actasstiffnessanddamping</sup> gains in dual-cone space that map this violation to a stabilizing contact impulse. With the above resolved contact forces/forces, the post contact velocity is written as 



Despite its simple form, this analytical update captures sticking, sliding, and separation via different activation patterns of ( _·_ )+ across polyhedral faces, as shown in Fig. 2, while satisfying the primal Coulomb friction constraints (3) by construction; see [8] for theoretical proof. 



Fig. 2: Different contact modes captured by ComFree-Sim. 

## _B. The Heuristics of Dual Cone Impedance_ 

In the above complementarity-free contact model, _K_ ( **_q_** ) and _D_ ( **_q_** ) are impedance parameters defined in the dual-cone space, and they play a central role in shaping the softness of resulting contact interaction. Following [8], a choice is to approximate the dual-cone impedance using a diagonal form, 



However, evaluating the right-hand side exactly for every contact pair and time step can be computationally expensive. 

To reduce this overhead while preserving sufficient flexibility for practical simulation tuning, we introduce a simple heuristic parameterization of _K_ ( **_q_** ) and _D_ ( **_q_** ) that enables users to control the apparent “stiffness” of contact interaction with a small number of global parameters. In most use cases, this provides an effective “one-size-fits-most” setting. Moreover, ComFree-Sim also supports learning-based parameterization for _K_ ( **_q_** ) and _D_ ( **_q_** ) [9]. Specifically, we set 



where _k_ user and _d_ user are user-set global impedance parameters shared across all contact pairs, and _M_ ( _ϕ_ ) is a constraintspace impedance that adapts to the signed distance between the current collision pair, i.e., bodies _i_ and _j_ , Specifically, 



Here, _I_ is identity matrix, _r_ ( _|ϕ|_ ) _∈_ (0 _,_ 1) is a gap-dependent scaling factor, which is used in MuJoCo backend solver [6]: 



where the hyperparameters ( _r_ min _, r_ max _, w, m, p_ ) follow the identical setting API as in MuJoCo. By default, they are set as [0 _._ 9 _,_ 0 _._ 95 _,_ 0 _._ 001 _,_ 0 _._ 5 _,_ 2 _._ 0]. This is to ensure ComFree-Sim share a MuJoCo-compatible interface. 

## _C. GPU Implementation for Contact Resolution_ 

A key advantage of ComFree-Sim is the _decoupling_ nature of the analytical contact resolution: it is independent across contact pairs and, under the polyhedral dual-cone approximation, separable across cone facets. This maps directly to GPU parallelism. Under Warp programming framework [38], ComFree-Sim launch kernels to (i) compute the smooth predicted velocity, (ii) solve dual-cone impulses in parallel over contacts and faces, (iii) accumulate generalized impulses, and (iv) apply velocity correction, as shown in Algorithm 1. 

## IV. GPU SIMULATION BENCHMARKING 

To evaluate ComFree-Sim, we benchmark simulation fidelity, stability, and efficiency against MJWarp [7], a state-ofthe-art GPU simulator. Specifically, we measure penetration depth, torsional/rolling friction behaviors, stability, runtime scaling with contact count, and parallel throughput. To isolate contact-resolution backend, both simulators use the same collision detection and time integration [7]. All tests run on an AMD 32-core CPU with an NVIDIA RTX 4090 GPU. 

## _A. Penetration Depth_ 

Penetration depth indicates rigid-body fidelity: larger interpenetration implies a stronger violation of rigidity. We compare MJWarp and ComFree-Sim in a collision-rich drop test where five 5 _×_ 5 arrays of convex primitives (cubes, cylinders, ellipsoids, capsules, and spheres; average size _≈_ 5 cm) are 

## **Algorithm 1** GPU-Parallelized ComFree-Sim Core 

|**Require:** State (**_q_**_,_**_v_**), non-contact forces (**_τ_**_,_**_c_**), inertia **_M_**, the detected<br>contact set _C_, where each contact _k ∈C_ contains signed gap _ϕk_, con-<br>tact Jacobians**J**_n,k_,_{_**J**<sup>(</sup><sup>_j_)</sup><br>_k,s_<sup>_}ns_</sup><br>_j_=1<sup>; friction coefficients</sup><sup>_{µs_</sup><br>_k_<sup>_}s∈{_t</sup><sup>_,_tor</sup><sup>_,_rol</sup><sup>_}_;</sup><br>user-set global dual-cone impedance (_k_user_, d_user).<br>**Ensure:** Post-contact velocity **_v_**<sup>+</sup>|
|---|
|**// Kernel I: Smooth prediction**<br>**parallel over DoFs:** **_v_**<sup>+</sup><br>smooth <sup>_←_</sup><sup>**_v_** +</sup><sup>**_M_**</sup><sup>_−_1(</sup><sup>**_τ_**</sup> <sup>_−_</sup><sup>**_c_**)</sup><sup>_h_</sup><br>(Eq. (2))|
|**// Kernel II: Per-contact, per-face dual-cone solve**<br>**parallel over** _k ∈C_**,** _s ∈{_t_,_tor_,_rol_}_**,** _j_ = 1_..ns_**:**<br>˜**J**<sup>(</sup><sup>_j_)</sup><br>_k,s _<sup>_←_</sup><sup>**_J_**</sup><sup>_n_</sup><br>_k _<sup>_−µs_</sup><br>_k_ <sup>**J**(</sup><sup>_j_)</sup><br>_k,s_<br>(Eq. (7))<br>˜_ϕ_<sup>(</sup><sup>_j_)</sup><br>_k,s _<sup>_←ϕk_</sup><br>_s_<sup>(</sup><sup>_j_)</sup><br>_k,s _<sup>_←_˜</sup><sup>**J**(</sup><sup>_j_)</sup><br>_k,s_ <sup>**_v_**+</sup><br>smooth<br>**_K_**<sup>(</sup><sup>_j_)</sup><br>_k,s_<sup>,</sup> <sup>**_D_**(</sup><sup>_j_)</sup><br>_k,s _<sup>_←_(</sup><sup>_k_user</sup><sup>_, d_user),</sup> <sup>_M_(</sup><sup>_ϕk_)</sup><br>(Eq. (11))<br><br><br><br><br><br><br><br>|
|_λ_<sup>(</sup><sup>_j_)</sup><br>_k,s _<sup>_←_</sup><br>�<br>**_K_**<sup>(</sup><sup>_j_)</sup><br>_k,s_<br>�<br>_s_<sup>(</sup><sup>_j_)</sup><br>_k,s_<sup>_dt_ + ˜</sup><sup>_ϕ_(</sup><sup>_j_)</sup><br>_k,s_<br>�<br>+**_D_**<sup>(</sup><sup>_j_)</sup><br>_k,s _<sup>_s_(</sup><sup>_j_)</sup><br>_k,s_<br>�<br>+<br>(Eq. (8))|
|**// Kernel III: Accumulate generalized impulse**<br>**parallel over** (_k, s, j_)**:** **_p_**+=<br>�<br>˜**_J_**<br>(_j_)<br>_k,s_<br>�_⊤_<br>_λ_<sup>(</sup><sup>_j_)</sup><br>_k,s_<br>**// Kernel IV: Velocity correction**<br>**parallel over DoFs:** **_v_**<sup>+</sup> _←_**_v_**<sup>+</sup><br>smooth <sup>+</sup><sup>**_M_**</sup><sup>_−_1</sup><sup>**_p_**</sup><sup>_dt_</sup><br>(Eq. (9))<br>**return** **_v_**<sup>+</sup>|





<!-- Start of picture text -->
(a) Torsional (b) Rolling (c) Stability<br>Fig. 4: Isolated benchmark environments.<br><!-- End of picture text -->







<!-- Start of picture text -->
(a) Torsional: angular velocity. (b) Rolling: linear velocity.<br><!-- End of picture text -->

Fig. 5: Results of torsional and rolling friction test. 

## _C. Simulation Stability_ 

stacked (Fig. 3a) and dropped onto a flat box, inducing dense contacts. At each step, we record the penetration depth of all detected contact pairs; after 1000 steps, we report the mean and standard deviation for MJWarp and multiple ComFreeSim settings (Fig. 3b). Overall, penetration increases with _k_ user and decreases with _d_ user; with appropriate tuning, ComFree-Sim achieves comparable or lower penetration than MJWarp. 

||Engine|_k_use|r_, d_user|Depth (mm)|
|---|---|---|---|---|
||Mujoco-Warp|N/A||1.7 ± 4.9|
||ComFree-Sim|0.1,|0.001|3.9 ± 6.9|
||ComFree-Sim|0.1,|0.005|3.8 ± 5.7|
||ComFree-Sim|0.3,|0.001|1.6 ± 3.3|
||ComFree-Sim|0.3,|0.005|1.4 ± 2.5|
||ComFree-Sim|0.5,|0.001|1.0 ± 2.1|
||ComFree-Sim|0.5,|0.005|0.9 ± 1.5|
|(a) Test Env.|(b) Pe|netra|tion de|pths.|



Fig. 3: Penetration-depth benchmark in a collision-rich drop test: (a) stacked arrays of primitives released to free-fall onto a flat box; (b) mean _±_ std penetration depth over all detected contacts. In all tests, simulation timestep _dt_ = 0 _._ 002. 

## _B. Torsional and Rolling Friction Modelling_ 

We evaluate torsional and rolling friction with two controlled contact tests that isolate each effect. For torsional friction, a sphere in contact with a plane is constrained to rotate only about _z_ -axis (Fig. 4a), and we measure angularvelocity decay under varying torsional friction coefficients (Fig. 5a). For rolling friction, a cylinder rolls freely on a plane (Fig. 4b), and we report the decay of its COM velocity under varying rolling friction coefficients (Fig. 5b). The monotone decay trends and their response to the corresponding coefficients confirm ComFree-Sim captures torsional/rolling dissipation with consistent contact dynamics. 

To assess numerical stability, we run a free-fall-and-sliding test where a cube is dropped onto a flat plane with initial linear velocity (2 _._ 0 _,_ 0 _,_ 0) and angular velocity (0 _._ 1 _,_ 0 _._ 1 _,_ 0 _._ 1) under gravity and friction (Fig. 4c). Since friction should dissipate kinetic energy and drive the cube to rest, we track the horizontal speed and _z_ (vertical) position over time (Fig. 6). We sweep ComFree impedance settings ( _k_ user _, d_ user) and time steps _dt_ . Across a wide range of parameters, ComFreeSim exhibits consistent, monotone horizontal-velocity decay without spurious drift or growth, indicating low sensitivity to moderate impedance variations. ComFree-Sim remains stable at a moderately large time step (e.g., _dt_ =0 _._ 02 s), but typically benefits from smaller _dt_ than MJWarp; unless otherwise noted, we use _dt_ =0 _._ 002s in all benchmarks. 



Fig. 6: Numerical stability test: horizontal speed and vertical position _z_ of free-fall-and-sliding cube over time. Left: ComFree-Sim with varying ( _k_ user _, d_ user) at _dt_ =0 _._ 002s. Right: ComFree-Sim under varying timestep _dt_ . 

## _D. Runtime Performance w.r.t. Contact Numbers_ 

We evaluate runtime scaling by measuring the _wall-clock time per full simulation step_ as a function of the number of contacts in the scene. This metric directly reflects computational efficiency in contact-rich simulation. We instantiate 512 parallel environments. In each environment, three 2 _×_ 2 arrays of convex primitives (cubes, capsules, and spheres) 

are stacked top-down (similar to Fig. 3a). To introduce stochasticity, we perturb all bodies with small initial linear velocities sampled from _N_ (0 _,_ 10<sup>_−_3</sup> ). We then run 750 simulation steps for MJWarp and ComFree-Sim ( _k_ user = 0 _._ 1, _d_ user = 0 _._ 001, and _dt_ = 0 _._ 002). At each step, we record the total contacts (aggregated over all environments) and the full-step wall-clock time (excluding rendering), including collision detection, contact resolution, and integration; Fig. 7 plots wall-clock time step time versus contact count. 

ComFree-Sim achieves around 3 _×_ faster simulation speed and exhibits an approximately _linear_ step-time scaling with contact count, consistent with its analytical, per-contact decoupled update and GPU parallelism. MJWarp shows _nonlinear_ (often superlinear) step-time growth and higher variance at comparable contact counts. Overall, ComFreeSim provides higher throughput and more predictable scaling in dense contact scenes. 



Fig. 7: Runtime scaling benchmark. Y: wall-clock step time. 

## _E. Throughput for Parallel Simulation_ 

We benchmark simulation throughput versus the number of parallel environments on an Allegro in-hand cube grasping scene (Fig. 8a). Starting from a stable grasp, we run 1500 simulation steps with 256/512/1024/2048/4096 environments and report the mean _±_ std throughput, defined as **singleenvironment** steps per second. To sustain rich robot–object contact, every 50 steps we apply a random joint-position command within ( _−_ 0 _._ 5 _,_ 0 _._ 5) around the initial configuration while preserving the grasp. As shown in Fig. 8b, ComFreeSim achieves nearly 2 _×_ the throughput of MJWarp, highlighting its advantage for large-scale sampling-based control and robot learning. 



<!-- Start of picture text -->
(b) Throughput of parallel simulation.<br><!-- End of picture text -->



(a) Parallel Env. 

Fig. 8: Allegro hand throughput test. 

V. COMFREE-SIM FOR REAL-TIME MPC FOR REAL-WORLD DEXTEROUS MANIPULATION 

We deploy ComFree-Sim as the predictive model in a realtime MPC loop for multi-fingered in-hand object reorientation on a physical LEAP Hand [39]. The goal is to reorient 

objects to target poses, evaluating ComFree-Sim’s closedloop real-time performance and model gap under real-world contact-rich control. The MPC is formulated as 



Here, **_x_** _t_ denotes the system state and **_u_** _t_ the control input at time step _t_ . We set the running and terminal costs as 



where _c_ quat:=1 _−_ ( **q**<sup>_⊤_</sup> target<sup>**q**obj)2 is orientation error; (</sup><sup>_px, py, pz_)</sup> are the absolute position errors; _c_ contact:=<sup>�4</sup> _i_ =1<sup>_∥_</sup><sup>**p**obj</sup><sup>_−_</sup><sup>**p**f/t</sup><sup>_i∥_2</sup> penalizes fingertip-to-object-center distance; _c_ joint:= _∥_ **_q_** robot _−_ **_q_** ref _∥_<sup>2</sup> penalizes deviation from a home pose; and Ifallen = 1 if _pz <_ 0 _._ 05. We tune _ωk_ and ( _ϕ_ 1 _, ϕ_ 2) based on the object mass and geometry. 

Throughout, we set the ComFree-Sim _dt_ =0 _._ 004 s and horizon _H_ =48. We solve (14) using MPPI [40] with _N_ = 256 samples, temperature _λ_ = 2 _×_ 10<sup>_−_3</sup> , and sampling standard deviation 0 _._ 02. We use incremental position control and clip actions to [ _−_ 0 _._ 1 _,_ 0 _._ 1]. For a controlled comparison, we replace ComFree-Sim with MJWarp while keeping all other settings identical. 

## _A. Hardware Setup_ 



Fig. 9: Hardware setup and system diagram. 

The real-world LEAP Hand platform for dexterous manipulation is shown in Fig. 9. The experiment covers objects with diverse (convex or nonconvex) shapes, including Cube, Duck, SpamTin, and Cylinder. Object pose is estimated using an Intel RealSense D435i RGB-D camera mounted above the workspace. We use FoundationPose [41] to perform 6D object pose tracking. The estimated object pose is streamed to the controller at _∼_ 25 Hz via LCM [42]. Robot joint states are read at 100 Hz via the LEAP Hand API and sent to the controller through LCM. ComFree-MPPI Controller receives robot joint states and object pose. We set _k_ user = 0 _._ 1 and _d_ user = 0 _._ 002 for all objects. At each control step, MPPI samples _N_ control sequences and rolls them out over a finite horizon using ComFree simulator. A weighted average control sequence is computed and first control input is applied in a receding-horizon manner as joint position commands. The closed-loop control frequency ranges between 35–72 Hz, 

TABLE I: Control and runtime performance for real-world in-hand dexterous manipulation with LEAP Hand 

||Pos Err|or [m]|Quat|Error|MPPI Ti|me [ms]|Task comple|tion time [s]|Success|Rate (%)|
|---|---|---|---|---|---|---|---|---|---|---|
|Object|ComFree|MJWarp|ComFree|MJWarp|ComFree|MJWarp|ComFree|MJWarp|ComFree|MJWarp|
|Cube<br>(Yaw)|**0.0106**<br>_±_**0.0028**|0.0119<br>_±_0.0041|**0.0231**<br>_±_**0.0081**|0.0236<br>_±_0.0103|**28.2308**<br>_±_**2.0053**|54.5961<br>_±_5.5158|**42.4261**<br>_±_**21.3724**|60.6831<br>_±_40.9661|**80.00**|65.00|
|Cube<br>(Roll/Pitch)|**0.0087**<br>_±_**0.0036**|0.0114<br>_±_0.0032|**0.0250**<br>_±_**0.0084**|0.0291<br>_±_0.0054|**27.7969**<br>_±_**1.0890**|56.4415<br>_±_5.5757|**20.1756**<br>_±_**12.0413**|74.3734<br>_±_44.2553|**55.00**|30.00|
|Duck<br>(Yaw)|0.0150<br>_±_0.0020|**0.0116**<br>_±_**0.0028**|0.0255<br>_±_0.0066|**0.0186**<br>_±_**0.0104**|**18.2271**<br>_±_**0.7618**|41.8674<br>_±_9.3805|**28.7974**<br>_±_**18.4190**|49.4049<br>_±_29.3045|**50.00**|25.00|
|Duck<br>(Roll/Pitch)|0.0183<br>_±_0.0012|**0.0180**<br>_±_**0.0000**|**0.0191**<br>_±_**0.0036**|0.0195<br>_±_0.0000|**13.9000**<br>_±_**5.8266**|49.2301<br>_±_0.0000|24.8061<br>_±_15.4174|**7.6724**<br>_±_**0.0000**|**20.00**|10.00|
|SpamTin<br>(Yaw)|**0.0161**<br>_±_**0.0013**|0.0164<br>_±_0.0011|0.0194<br>_±_0.0085|**0.0172**<br>_±_**0.0036**|**20.0710**<br>_±_**0.8337**|52.4135<br>_±_2.4810|**29.3871**<br>_±_**18.3080**|53.0317<br>_±_21.1797|**65.00**|15.00|
|SpamTin<br>(Roll/Pitch)|0.0178<br>_±_0.0009|**0.0174**<br>_±_**0.0005**|**0.0198**<br>_±_**0.0050**|0.0272<br>_±_0.0029|**19.2457**<br>_±_**0.2715**|68.7749<br>_±_5.8720|36.0421<br>_±_30.5504|**21.7259**<br>_±_**6.0693**|**40.00**|30.00|
|Cylinder<br>(Yaw)|0.0147<br>_±_0.0037|**0.0103**<br>_±_**0.0005**|**0.0221**<br>_±_**0.0094**|0.0241<br>_±_0.0042|**20.7444**<br>_±_**0.9223**|39.2304<br>_±_2.3594|34.1209<br>_±_25.4092|**27.7529**<br>_±_**18.7242**|**50.00**|10.00|
|Cylinder<br>(Roll/Pitch)|**0.0145**<br>_±_**0.0024**|0.0162<br>_±_0.0000|0.0183<br>_±_0.0068|**0.0040**<br>_±_**0.0000**|**21.1287**<br>_±_**1.2188**|34.0165<br>_±_0.0000|**27.1724**<br>_±_**19.8587**|62.2975<br>_±_0.0000|**50.00**|10.00|



depending on the number of contacts. The hand is mounted on a rigid steel rail at _∼_ 28<sup>_◦_</sup> inclination to provide a stable base for in-hand manipulation experiments. All algorithms run on an AMD 32-core CPU with NVIDIA 4090 GPUs. 

## _B. Results and Analysis_ 

_1) Metrics and Results:_ We evaluate five metrics: **Success rate** , a trial is successful if position error _<_ 0 _._ 02 m and quaternion error _<_ 0 _._ 04; **MPPI time** , wall-clock compute time per MPC control step; **Position error** , _∥_ **p**<sup>obj</sup> _−_ **p** target _∥_ ; **Quaternion error** , 1 _−_ ( **q**<sup>_⊤_</sup> target<sup>**q**obj)2;and</sup><sup>**Taskcompletion**</sup> **time** , elapsed real time to reach the success condition. For each object/target, we run 20 independent trials; success rate and MPPI time are reported over all trials, while position and quaternion errors are computed over successful trials only. 

_2) Analysis:_ Overall, ComFree-Sim achieves manipulation accuracy comparable to MJWarp: MJWarp yields lower raw error on some tasks (e.g., Duck-Yaw, Cylinder-Yaw), while ComFree-Sim matches or improves others (e.g., CubeRoll/Pitch, Cylinder-Roll/Pitch). Crucially, ComFree-Sim reduces per-step MPPI compute time for _all_ object–task pairs, with _∼_ 2.4 _×_ average speedup (median _∼_ 2.2 _×_ ), which consistently boosts closed-loop success rates (+27 percentage points on average across eight benchmarks). With sub-30 ms MPPI step times (13.9–28.2 ms in Table I), ComFree-Sim enables _∼_ 35–72 Hz control on hardware, making it a strong backend for high-frequency, contact-rich MPC. 

## VI. COMFREE-SIM FOR DYNAMIC-AWARE RETARGETING FOR AGILE LOCOMOTION 

We evaluate ComFree-Sim on model-based, dynamicsaware motion retargeting using SPIDER [43], which optimizes the control sequence **U** in (14) via MPPI with an annealed noise schedule [44]. The optimal control sequence **U**<sup>_∗_</sup> is applied to a simulator in a receding-horizon manner to generate the full trajectory, ensuring physical plausibility. 

The original SPIDER method [43] performs optimization in MJWarp and generates full trajectories in MuJoCo-CPU [7]. 

Since MJWarp can be viewed as a GPU reimplementation of MuJoCo-CPU, it serves as a strong baseline with minimal optimizer–rollout mismatch. To evalaute ComFree-Sim, we replace MJWarp with ComFree-Sim for the optimization, while keeping MuJoCo-CPU unchanged for the full trajectory rollout. This benchmark thus (i) characterizes the _sim-to-sim gap_ between ComFree and the MuJoCo contact backend in control tasks, and (ii) highlights the computational efficiency gains of ComFree-Sim when used inside the MPPI optimization loop. We retarget five Unitree G1 motions from the reference dataset (Fig. 10): **Cartwheels** , a dynamic acrobatic motion with continuous lateral rotation; **Martial Arts** , kicks/punches and stance transitions requiring balance; **Dance** , rhythmic whole-body motion with coordinated footwork and expressive arm gestures; **Getup** , recovery from fallen to standing; and **Pushbox** , sustained box pushing while maintaining locomotion stability. 









<!-- Start of picture text -->
(a) Cartwheels (b) Martial Arts (c) Dance<br>(d) Getup (e) Pushbox<br><!-- End of picture text -->



<!-- Start of picture text -->
Fig. 10: Retargeting Tasks.<br><!-- End of picture text -->

We evaluate performance using multiple metrics that capture both motion accuracy and computational efficiency. In all tasks, we choose _k_ user = 0 _._ 55 _, b_ user = 0 _._ 55 _×_ 10<sup>_−_3</sup> and 

TABLE II: Comparison of Motion Retargeting Performance Across Tasks 

||Pos.|Error|Quat.|Error|Joint|Error|Obj.|Error|Obj. Qua|t. Error|MPPI. T|ime (s)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Task|ComFree|MJWarp|ComFree|MJWarp|ComFree|MJWarp|ComFree|MJWarp|ComFree|MJWarp|ComFree|MJWarp|
|Cartwheels|0.037<br>_±_0.002|**0.033**<br>_±_**0.001**|0.100<br>_±_0.004|**0.074**<br>_±_**0.001**|0.692<br>_±_0.008|**0.682**<br>_±_**0.007**|–|–|–|–|**0.529**<br>_±_**0.422**|0.705<br>_±_0.490|
|Martial Arts|0.047<br>_±_0.003|**0.028**<br>_±_**0.001**|0.118<br>_±_0.005|**0.076**<br>_±_**0.002**|0.830<br>_±_0.007|**0.794**<br>_±_**0.007**|–|–|–|–|**0.589**<br>_±_**0.336**|0.774<br>_±_0.492|
|Dance|0.037<br>_±_0.001|**0.033**<br>_±_**0.000**|0.094<br>_±_0.003|**0.069**<br>_±_**0.000**|0.881<br>_±_0.003|**0.871**<br>_±_**0.001**|–|–|–|–|**0.481**<br>_±_**0.367**|0.646<br>_±_0.428|
|Getup|0.036<br>_±_0.001|**0.032**<br>_±_**0.000**|0.088<br>_±_0.003|**0.068**<br>_±_**0.001**|0.705<br>_±_0.003|**0.682**<br>_±_**0.003**|–|–|–|–|**0.473**<br>_±_**0.388**|0.572<br>_±_0.342|
|PushBox|0.103<br>_±_0.017|**0.080**<br>_±_**0.005**|0.079<br>_±_0.010|**0.057**<br>_±_**0.002**|0.246<br>_±_0.022|**0.196**<br>_±_**0.004**|0.169<br>_±_0.082|**0.098**<br>_±_**0.010**|0.260<br>_±_0.146|**0.161**<br>_±_**0.018**|1.171<br>_±_1.189|**0.719**<br>_±_**0.708**|



follow other parameters settings in SPIDER. Specifically, we report the robot base pose difference (position and quaternion), and joint configuration difference between the retargeted motion and the reference trajectory. For the Pushbox task, we additionally measure the object pose differences to assess contact interaction fidelity. Finally, we record the average computation time for one run of MPPI optimization to evaluate computational efficiency. The metrics of all tasks is shown in Table II. ComFree-Sim achieves performance comparable to MJWarp on the humanoid tracking tasks, with minor differences in all metrics. Notably, ComFree-Sim consistently achieves faster optimization time, demonstrating better computational efficiency, except for PushBox task. 

Since MJWarp is a GPU reimplementation of MuJoCoCPU, it is expected to be more closely aligned with the MuJoCo contact backend and thus provide a strong baseline for task-level performance. Nevertheless, the results indicate that ComFree-Sim exhibits a _manageable_ sim-to-sim gap relative to this mature, optimization-based MuJoCo solver while delivering substantially lower rollout latency, suggesting that analytical contact resolution can remain competitive for control tasks without incurring the heavy computational cost of iterative contact solvers. 

## ACKNOWLEDGMENT 

We thank the MuJoCo Warp (MJWarp) team at Google DeepMind and NVIDIA for making the code publicly available. We also thank Vamsi Sai Abhijit Tadepalli from the IRIS Lab for maintaining the vision-tracking module used in our real-world in-hand manipulation experiments. 

## REFERENCES 

- [1] J. Bender, K. Erleben, and J. Trinkle, “Interactive simulation of rigid body dynamics in computer graphics,” _Comput. Graph. Forum_ , vol. 33, no. 1, p. 246–270, Feb. 2014. 

- [2] Q. Le Lidec, W. Jallet, L. Montaut, I. Laptev, C. Schmid, and J. Carpentier, “Contact models in robotics: a comparative analysis,” _IEEE Transactions on Robotics_ , vol. 40, pp. 3716–3733, 2024. 

- [3] P. C. Horak and J. C. Trinkle, “On the similarities and differences among contact models in robot simulation,” _IEEE Robotics and Automation Letters_ , vol. 4, no. 2, pp. 493–499, 2019. 

- [4] D. E. Stewart and J. C. Trinkle, “An implicit time-stepping scheme for rigid body dynamics with inelastic collisions and coulomb friction,” _International Journal for Numerical Methods in Engineering_ , vol. 39, no. 15, pp. 2673–2691, 1996. 

- [5] M. Anitescu, “Optimization-based simulation of nonsmooth rigid multibody dynamics,” _Mathematical Programming_ , vol. 105, no. 1, pp. 113–143, 2006. 

- [6] E. Todorov, T. Erez, and Y. Tassa, “Mujoco: A physics engine for model-based control,” in _2012 IEEE/RSJ International Conference on Intelligent Robots and Systems_ . IEEE, 2012, pp. 5026–5033. 

- [7] Google DeepMind and NVIDIA, “MuJoCo Warp (MJWarp),” https: //mujoco.readthedocs.io/en/stable/mjwarp/. 

## VII. CONCLUSION 

This work introduced **ComFree-Sim** , a GPU-parallelized analytical contact physics engine based on complementarityfree contact modeling. By resolving contact impulses in closed form with a dual-cone impedance update, ComFreeSim achieves _near-linear_ runtime scaling with contact count while maintaining physical fidelity comparable to MJWarp. Extensive benchmarks validate its accuracy, stability, and 2–3 times higher throughput in dense contact scenes. Real-world experiments on MPPI-based dexterous manipulation show that low-latency simulation yields higher control success rates and enables practical high-frequency deployment in contact-rich tasks. Dynamics-aware retargeting experiments further show that ComFree-Sim achieves comparable tasklevel tracking with manageable sim-to-sim gap to MuJoCo backend, while substantially reducing optimization time. 

- [8] W. Jin, “Complementarity-free multi-contact modeling and optimization for dexterous manipulation,” _Robotics: Science and Systems (RSS)_ , 2025. 

- [9] M. Wang, W. Jin, K. Cao, L. Xie, and Y. Hong, “Contactgaussian-wm: Learning physics-grounded world model from videos,” _arXiv preprint arXiv:2602.11021_ , 2026. 

- [10] I. Wald, S. Boulos, and P. Shirley, “Ray tracing deformable scenes using dynamic bounding volume hierarchies,” _ACM Transactions on Graphics_ , vol. 26, no. 1, p. 6, 2007. 

- [11] E. G. Gilbert, D. W. Johnson, and S. S. Keerthi, “A fast procedure for computing the distance between complex objects in three-dimensional space,” _IEEE Journal on Robotics and Automation_ , vol. 4, no. 2, pp. 193–203, 1988. 

- [12] G. Van Den Bergen, “Proximity queries and penetration depth computation on 3d game objects,” in _Game developers conference_ , vol. 170, 2001, p. 209. 

- [13] M. Macklin, K. Erleben, M. M¨uller, N. Chentanez, S. Jeschke, and Z. Corse, “Local optimization for robust signed distance field collision,” _Proceedings of the ACM on Computer Graphics and Interactive Techniques_ , vol. 3, no. 1, pp. 1–17, 2020. 

- [14] W. Yang and W. Jin, “Contactsdf: Signed distance functions as multi-contact models for dexterous manipulation,” _IEEE Robotics and Automation Letters_ , 2025. 

- [15] A. M. Castro, F. N. Permenter, and X. Han, “An unconstrained convex formulation of compliant contact,” _IEEE Transactions on Robotics_ , vol. 39, no. 2, pp. 1301–1320, 2022. 

- [16] R. Smith, “Open dynamics engine,” 2008. [Online]. Available: https://www.ode.org/ 

- [17] E. Coumans and Y. Bai, “Pybullet, a python module for physics simulation for games, robotics and machine learning,” http://pybullet. org. 

- [18] M. Macklin, K. Storey, M. Lu, P. Terdiman, N. Chentanez, S. Jeschke, and M. M¨uller, “Small steps in physics simulation,” in _Proceedings of the 18th annual ACM siggraph/eurographics symposium on computer animation_ , 2019, pp. 1–7. 

- [19] T. Erez, Y. Tassa, and E. Todorov, “Simulation tools for modelbased robotics: Comparison of bullet, havok, mujoco, ode and physx,” in _2015 IEEE international conference on robotics and automation (ICRA)_ . IEEE, 2015, pp. 4397–4404. 

- [20] J. Carpentier, G. Saurel, G. Buondonno, J. Mirabel, F. Lamiraux, O. Stasse, and N. Mansard, “The pinocchio c++ library – a fast and flexible implementation of rigid body dynamics algorithms and their analytical derivatives,” in _IEEE International Symposium on System Integrations (SII)_ , 2019. 

- [21] R. Tedrake and the Drake Development Team, “Drake: Model-based design and verification for robotics,” 2019. [Online]. Available: https://drake.mit.edu 

- [22] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, and G. State, “Isaac gym: High performance GPU-based physics simulation for robot learning,” in _Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)_ , 2021. 

horizon dexterous manipulation,” _arXiv preprint arXiv:2601.10930_ , 2026. 

   - [37] Z. Xie, W. Yang, and W. Jin, “On-palm dexterity: Dynamic reorientation of objects via emergent flipping and sliding,” in _ICRA 2025 Workshop on Learning Meets Model-Based Methods for Contact-Rich Manipulation_ , 2025. 

   - [38] M. Macklin, “Warp: A high-performance python framework for gpu simulation and graphics,” https://github.com/nvidia/warp, 2022, nVIDIA GTC. 

   - [39] K. Shaw, A. Agarwal, and D. Pathak, “Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning,” _Robotics: Science and Systems (RSS)_ , 2023. 

   - [40] G. Williams, A. Aldrich, and E. A. Theodorou, “Model predictive path integral control: From theory to parallel computation,” _Journal of Guidance, Control, and Dynamics_ , vol. 40, no. 2, pp. 344–357, 2017. 

   - [41] B. Wen, W. Yang, J. Kautz, and S. Birchfield, “Foundationpose: Unified 6d pose estimation and tracking of novel objects,” 2024. [Online]. Available: https://arxiv.org/abs/2312.08344 

   - [42] A. S. Huang, E. Olson, and D. C. Moore, “Lcm: Lightweight communications and marshalling,” in _2010 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , 2010, pp. 4057–4062. 

   - [43] C. Pan, C. Wang, H. Qi, Z. Liu, H. Bharadhwaj, A. Sharma, T. Wu, G. Shi, J. Malik, and F. Hogan, “Spider: Scalable physics-informed dexterous retargeting,” _arXiv preprint arXiv:2511.09484_ , 2025. 

   - [44] H. Xue, C. Pan, Z. Yi, G. Qu, and G. Shi, “Full-order sampling-based mpc for torque-level locomotion control via diffusion-style annealing,” in _2025 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2025, pp. 4974–4981. 

- [23] NVIDIA, “Isaac Sim.” [Online]. Available: https://github.com/ isaac-sim/IsaacSim 

- [24] B. Liu, Y. Zhu, C. Gao, Y. Feng, Q. Liu, Y. Zhu, and P. Stone, “Libero: Benchmarking knowledge transfer for lifelong robot learning,” _Advances in Neural Information Processing Systems_ , vol. 36, pp. 44 776–44 791, 2023. 

- [25] C. Li, R. Zhang, J. Wong, C. Gokmen, S. Srivastava, R. Mart´ın-Mart´ın, C. Wang, G. Levine, M. Lingelbach, J. Sun _et al._ , “Behavior-1k: A benchmark for embodied ai with 1,000 everyday activities and realistic simulation,” in _Conference on Robot Learning_ , 2023, pp. 80–93. 

- [26] S. Tao, F. Xiang, A. Shukla, Y. Qin, X. Hinrichsen, X. Yuan, C. Bao, X. Lin, Y. Liu, T.-K. Chan, Y. Gao, X. Li, T. Mu, N. Xiao, A. Gurha, V. N. Rajesh, Y. W. Choi, Y.-R. Chen, Z. Huang, R. Calandra, R. Chen, S. Luo, and H. Su, “Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3,” in _Proceedings of Robotics: Science and Systems_ , 2025. 

- [27] NVIDIA, “Isaac lab: A gpu-accelerated simulation framework for multi-modal robot learning,” _arXiv preprint arXiv:2511.04831_ , 2025. 

- [28] K. Zakka, Q. Liao, B. Yi, L. L. Lay, K. Sreenath, and P. Abbeel, “mjlab: A lightweight framework for gpu-accelerated robot learning,” 2026. [Online]. Available: https://arxiv.org/abs/2601.22074 

- [29] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray _et al._ , “Learning dexterous in-hand manipulation,” _The International Journal of Robotics Research_ , vol. 39, no. 1, pp. 3–20, 2020. 

- [30] E. Kaufmann, L. Bauersfeld, A. Loquercio, M. M¨uller, V. Koltun, and D. Scaramuzza, “Champion-level drone racing using deep reinforcement learning,” _Nature_ , vol. 620, no. 7976, pp. 982–987, 2023. 

- [31] J. Lee, J. Hwangbo, L. Wellhausen, V. Koltun, and M. Hutter, “Learning quadrupedal locomotion over challenging terrain,” _Science robotics_ , vol. 5, no. 47, p. eabc5986, 2020. 

- [32] T. Howell, N. Gileadi, S. Tunyasuvunakool, K. Zakka, T. Erez, and Y. Tassa, “Predictive sampling: Real-time behaviour synthesis with mujoco,” _arXiv preprint arXiv:2212.00541_ , 2022. 

- [33] A. H. Li, B. Hung, A. D. Ames, J. Wang, S. L. Cleac’h, and P. Culbertson, “Judo: A user-friendly open-source package for sampling-based model predictive control,” _arXiv preprint arXiv:2506.17184_ , 2025. 

- [34] A. H. Li, P. Culbertson, V. Kurtz, and A. D. Ames, “Drop: Dexterous reorientation via online planning,” in _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , 2025, pp. 14 299–14 306. 

- [35] J. Alvarez-Padilla, J. Z. Zhang, S. Kwok, J. M. Dolan, and Z. Manchester, “Real-time whole-body control of legged robots with modelpredictive path integral control,” in _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , 2025, pp. 14 721–14 727. 

- [36] Z. Xie, Y. Xiang, M. Posa, and W. Jin, “Where to touch, how to contact: Hierarchical rl-mpc framework for geometry-aware long- 

