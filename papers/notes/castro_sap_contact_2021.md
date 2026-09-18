# castro_sap_contact_2021 — An Unconstrained Convex Formulation of Compliant Contact (Castro, Permenter, Han; IEEE T-RO 2022, arXiv 2021)

sources: papers/md/castro_sap_contact_2021.md [b67485bc] ; code/md/castro_sap_contact_2021.md [5a73436c]

## One-line contribution
Analytically eliminates contact constraints from a primal, velocity-level compliant-contact formulation to get an unconstrained convex problem, then solves it with a custom "Semi-Analytic Primal" (SAP) solver that has proven global convergence and warm-starts effectively; implemented in Drake (Abstract).

## Setting
- hand(s): Allegro hand (16 DoF each), two of them, mounted on two 7-DoF Kuka IIWA arms, for the dual-arm demo (Sec. VI-E, Fig. 1). Other test cases (spring-cylinder, clutter, slip control) are objects/robots, not hands.
- simulator / physics: Drake, SAP solver (this paper's contribution). Compliant contact with a discrete θ-method time integrator (θ-method covers explicit Euler, symplectic Euler, implicit Euler, and the second-order symplectic midpoint rule as special cases, Sec. II-C).
- observation / action space: not applicable — this is a physics-engine/solver paper, not a policy paper.
- objects / data: dual-arm task has a jar with lid (12 DoF), 16 marbles at 50 g each (96 DoF), and a bowl (6 DoF); total 160 DOF, "hundreds of contact constraints per time step" (Sec. VI-E, Fig. 1 caption).

## Physics block
- contact model: compliant point contact by default; the normal impulse law is γ_n = (k(φ − τ_d v_n))_+ · δt̄ with stiffness k and dissipation time-scale τ_d (Sec. II-B, Eq. following "we model the normal component of the impulse"), equivalent to a complementarity condition 0 ≤ c⁻¹γ_n ⊥ ... ≥ 0 where c = k⁻¹ is the compliance. Tangential impulse follows Coulomb's law with the maximum-dissipation principle (Sec. II-B). Also supports compliant surface-patch ("hydroelastic") contact for the jar/lid pair in the dual-arm demo (Sec. VI-E, Sec. VI-D refs [35],[36]).
- solver and iterations: SAP (Semi-Analytic Primal), a custom Newton-type solver on the unconstrained convex primal problem, with analytic gradients, a line search, and exploitation of sparsity (Sec. IV). SAP "globally converges from all initial conditions" (Appendix E) and warm-starts from the previous time step's velocities. In the dual-arm comparison (Sec. VI-E), SAP averages 4 iterations/timestep vs. 8.3 for Geodesic IPM and 10.1 for Gurobi, at the same mean momentum-error tolerance, and is reported "7.4× faster than Gurobi and 2.2× faster than Geodesic IPM" (Sec. VI-E, Fig. 21).
- differentiability: "Since forces are a continuous function of state, the model is well suited for applications requiring gradients such as trajectory optimization, machine learning, parameter estimation, and control. Factorizations computed during forward dynamics can be reused when computing gradients" (Sec. VII, "Differentiation"). No explicit autodiff/adjoint implementation is described in this paper; it is stated as a property of the formulation.
- timestep: task-dependent; dual-arm demo uses δt = 5×10⁻³ s (Sec. VI-E). No single global default is stated.
- friction model: Coulomb's law with the maximum dissipation principle (MDP), regularized via the compliance/regularization matrix R = diag([R_t, R_t, R_n]); stiction slip velocity is bounded as v_s ≈ µσδt·g with σ = 10⁻³ used in all experiments (Sec. V-B), e.g. v_s ≈ 10⁻⁵ m/s at δt = 10⁻³ s and v_s ≈ 10⁻⁴ m/s at δt = 10⁻² s.
- how penetration is resolved / is depth exposed: penetration is not eliminated but bounded and quoted analytically. For a point mass at rest with the paper's near-rigid stiffness rule (T_n = βδt, β=1, critically damped, Sec. V-B): φ ≈ 2.5×10⁻⁷ m at δt = 10⁻³ s, and φ ≈ 2.5×10⁻⁵ m at δt = 10⁻² s ("well within acceptable bounds to consider a body rigid for typical robotics applications," Sec. V-B). Signed distance φ is a first-class quantity in the formulation (φ_i(q) ∈ R, negative for overlapping bodies, Sec. II-A) and is exposed to the solver at every contact.
- GPU or CPU: CPU only. "All simulations are carried out in a system with 24 2.2 GHz Intel Xeon cores (E5-2650 v4) and 128 GB of RAM, running Linux. However, all of our tests are run in a single thread" (Sec. VI).
- throughput: no absolute steps/sec or FPS number is given. Only relative solver speedups are reported (SAP 7.4× faster than Gurobi, 2.2× faster than Geodesic IPM, dual-arm task, Sec. VI-E, Fig. 17/21); warm-starting "allows for significantly reducing" the cold-start timing gap for ADMM-type solvers vs. PGS (Sec. IV-D discussion, Fig. 17 caption region — note this specific comparison is elaborated in `contact_models_comparison_2023`, which builds on this paper's solver).

## Evaluation
- metrics (exact definitions): dimensionless momentum error (Eq. 32) and dimensionless complementarity-slackness error (Eq. 33), both reported as mean/median with min–max shaded bands over a trajectory (Sec. VI-E, Figs. 19–20); number of solver iterations per timestep (Fig. 21).
- headline numbers: at matched mean momentum error (Gurobi BarQCPConvTol=10⁻⁸, Geodesic IPM complementarity tol=10⁻⁶, SAP relative tol=10⁻³), SAP is "7.4 faster than Gurobi and 2.2 faster than Geodesic IPM" with 4 mean iterations vs. 8.3 (Geodesic IPM) and 10.1 (Gurobi) (Sec. VI-E). SAP "cannot achieve errors below 10⁻⁶ for this case due to round-off errors" (Sec. VI-E).
- baselines beaten: Gurobi (commercial QP/QCP solver) and a Geodesic interior-point method sharing the same sparse linear algebra (Sec. VI-A).
- real robot? none — all results are simulation-only (dual Kuka+Allegro task is simulated, Fig. 1 caption: "Keyframes of a dual arm manipulation task in simulation").

## Limitations stated by the authors
- "Convex Approximation": introduces a gliding effect during sliding at distance φ ∼ δt·µ·‖v_t‖ (Sec. VIII).
- "Stiffness and Dissipation": requires K and D to be SPD or SPD approximations; not exact for non-joint-level spring arrangements (Sec. VIII).
- "Linear Approximations": the SPD gradient A is evaluated once per timestep at v*, i.e. the balance of momentum is replaced by its linear approximation — exact for many cases, second-order accurate in general (Sec. VIII).
- "Delassus Operator Estimation": the diagonal approximation used for near-rigid stiffness estimation underestimates stiffness in corner cases such as a stack of books, requiring user intervention (Sec. VIII).
- "Scalability": no fundamental barrier is claimed to scaling SAP to thousands of bodies with structured sparsity, "but scalability needs to be studied further" (Sec. VIII).

## Quotable claims (verbatim, with section)
- "Our solver has proven global convergence and warm-starts effectively, enabling simulation at interactive rates." (Abstract)
- "MuJoCo targets robotic applications. Its contact model is parameterized by a daunting number of non-physical parameters aimed at regularizing the problem, though at the expense of drift artifacts." (Sec. I-B)
- "Therefore, the effect of compliance is to soften this gliding effect ... the gliding effect unfortunately does not go away as δt → 0." (Sec. V-A)
- "SAP is 7.4 faster than Gurobi and 2.2 faster than Geodesic IPM." (Sec. VI-E)
- "We consistently observe that the robot does not complete the task successfully when momentum errors are larger than about 10%, regardless of the solver." (Sec. VI-E)

## Notes for the survey
- This is the theory paper behind Drake's SAP solver; `contact_models_comparison_2023` (Le Lidec et al.) re-implements SAP (with a different line search — backtracking Armijo instead of the original's, an explicitly noted mismatch, Sec. IV of that paper) and benchmarks it against RaiSim, PGS/LCP, PGS/CCP, and ADMM on the same hardware — that is the source for cross-engine wall-clock and convergence comparisons; this paper alone provides only relative (SAP vs. Gurobi vs. Geodesic IPM) numbers on Drake's own C++ implementation.
- The near-rigid penetration estimate (2.5×10⁻⁵ m at δt=10⁻²s, 2.5×10⁻⁷ m at δt=10⁻³s) is an analytical bound for a single point mass on a plane, not a measured penetration depth in a hand-object grasp; it should not be quoted as a general Drake grasp-penetration number.
- Code md provenance: `code/md/castro_sap_contact_2021.md` is a README + pruned file tree + Python (pydrake) signatures only; no C++ SAP solver source was captured, so the solver internals here come entirely from the paper text, not from inspecting the implementation.
