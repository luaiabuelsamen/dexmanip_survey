1 

# An Unconstrained Convex Formulation of Compliant Contact 

Alejandro Castro, Frank Permenter, Xuchen Han 

**_Abstract_ —We present a convex formulation of compliant frictional contact and a robust, performant method to solve it in practice. By analytically eliminating contact constraints, we obtain an unconstrained convex problem. Our solver has proven global convergence and warm-starts effectively, enabling simulation at interactive rates. We develop compact analytical expressions of contact forces allowing us to describe our model in clear physical terms and to rigorously characterize our approximations. Moreover, this enables us not only to model point contact, but also to incorporate sophisticated models of compliant contact patches. Our time stepping scheme includes the midpoint rule, which we demonstrate achieves second order accuracy even with frictional contact. We introduce a number of accuracy metrics and show our method outperforms existing commercial and open source alternatives without sacrificing accuracy. Finally, we demonstrate robust simulation of robotic manipulation tasks at interactive rates, with accurately resolved stiction and contact transitions, as required for meaningful sim-to-real transfer. Our method is implemented in the open source robotics toolkit Drake.** 

**_Index Terms_ —Contact Modeling, Simulation and Animation, Dexterous Manipulation, Dynamics.** 

## I. INTRODUCTION 

**S** IMULATION of multibody systems with frictional contacthas proven indispensable in robotics, aiding at multiple 

has proven indispensable in robotics, aiding at multiple stages during the mechanical and control design, testing, and training of robotic systems. Robotic applications often require robust simulation tools that can perform at interactive rates without sacrificing accuracy, a critical prerequisite for meaningful sim-to-real transfer. However, reliable modeling and simulation for contact-rich robotic applications remains somewhat elusive. 

Rigid body dynamics with frictional contact is complicated by the non-smooth nature of the solutions. It is well known [1] that rigid contact when combined with the Coulomb model of friction can lead to paradoxical configurations for which solutions in terms of accelerations and forces do not exist. These phenomena are known as Painlev´e paradoxes [2]. Theory resolves these paradoxes by allowing discrete velocity jumps and impulsive forces, formally casting the problem as a differential variational inequality [3]. In practice, event based approaches can resolve impulsive transitions [4], though it is not clear how to reliably detect these events even for simple one degree of freedom systems [2]. 

Nevertheless, the problem can be solved in a weaker formulation at the velocity level using a time-stepping scheme where the next step velocities and impulses are the unknowns 

All the authors are with the Toyota Research Institute, USA, firstname.lastname@tri.global. 



Fig. 1: Keyframes of a dual arm manipulation task in simulation (see supplemental video). The robot is commanded to pick up a jar full of marbles, open it, pour its contents into a bowl, close the lid and place the empty jar back in place. This is a computationally intensive simulation with 160 degrees of freedom and hundreds of contact constraints per time step (see Fig. 18). Our SAP solver is robust and warm-starts effectively, enabling this simulation to run at interactive rates. 

at each time step [5], [6]. These formulations lead in general to a non-linear complementarity problem (NCP). A linear complementarity problem (LCP) can be formulated using a polyhedral approximation of the friction cone, though at the expense of non-physical anisotropy [7]. Even though LCP formulations guarantee solution existence [6], [8], solving them accurately and efficiently has remained difficult in practice. This has been explained partly due to the fact that these formulations are equivalent to nonconvex problems in global optimization, which are generally NP-hard [9]. Indeed, popular direct methods based on Lemke’s pivoting algorithm to solve LCPs may exhibit exponential worst-case complexity [10]. Similarly, popular iterative methods based on projected GaussSeidel (PGS) [11], [12] have also shown exponentially slow convergence [13]. These observations are not just of theoretical value—in practice, these methods are numerically brittle and lack robustness when tasked with computing contact forces. 

2 

Software typically attempts to compensate for this inherent lack of stability and robustness through non-physical constraint relaxation and stabilization, requiring a significant amount of application-specific parameter tuning. 

## _A. Previous Work on Convex Approximations of Contact_ 

To improve computational tractability, Anitescu introduced a _convex relaxation_ of the contact problem [14]. This relaxation is a convex approximation with proven convergence to the solution of a measure differential inclusion as the time step goes to zero. For sliding contacts, the convex approximation introduces a _gliding_ artifact at a distance _φ_ that is proportional to the time step _δt_ , friction coefficient _µ_ and sliding velocity _∥_ **_v_** _t∥_ [15], i.e. _φ ∼ δtµ∥_ **_v_** _t∥_ . This artifact can be irrelevant for problems with lubricated contacts (as in many mechanisms) and goes away for sticking contacts (dominant in robotic manipulation). For sliding contact, the approximation can be adequate for applications for which the product _δtµ∥_ **_v_** _t∥_ is usually sufficiently small. For trajectory optimization, Todorov [16] introduces regularization into Anitescu’s formulation in order to write a strictly convex formulation with a unique, smooth and invertible solution. For simulation, Todorov [17] uses regularization to introduce _numerical compliance_ that provides Baumgarte-like stabilization to avoid constraint drift. As a side effect, the regularized formulation can lead to a noticeable non-zero slip velocity even during stiction [18]. 

## _B. Available Software_ 

Even though these formulations introduce a tractable approximation of frictional contact, they have not been widely adopted in practice. We believe this is because of the lack of robust solution methods with a computational cost suitable for interactive simulation. Software such as ODE [19], Dart [20] and Vortex [21] use a polyhedral approximation of the friction cone leading to an LCP formulation. Algoryx [22] uses a _split solver_ , reminiscent of one iteration in the staggered projections method [9]. RaiSim [23] implements an iterative method with exact solution per-contact, a significant improvement over the popular PGS used in computer graphics, though still with no convergence nor accuracy guarantees. Drake [24] solves compliant contact with regularized friction with its transition aware solver TAMSI [25]. 

To our knowledge, Chrono [26], Mujoco [27] and Siconos [28] are the only packages that implement the convex approximation of contact. Chrono implements a variety of solvers for Anitescu’s convex formulation [14] including projected Jacobi and Gauss-Seidel methods [29], Accelerated Projected Gradient Descent (APGD) [30], Spectral Projected Gradients (SPG) [31] and more recently Alternating Direction Method of Multipliers (ADMM) [32]. Though these methods are first order and often exhibit slow convergence, they are amenable to parallelization and have been applied successfully in the simulation of granular flows with millions of bodies. MuJoCo targets robotic applications. Its contact model is parameterized by a daunting number of non-physical parameters aimed at regularizing the problem, though at the expense of drift 

artifacts [18]. Still, it has become very popular in the reinforcement learning community given its performance. Siconos is an open-source software targeting large scale simulation of both rigid and deformable objects. The authors of Siconos perform an exhaustive benchmarking campaign in [33] using the convex approximation of contact. The analysis reveals that there is no universal solver and that every solver technology suffers from accuracy, robustness and/or efficiency problems. 

## _C. Outline and Novel Contributions_ 

It is not clear if these convex approximations present a real advantage when compared to approaches solving the original non-convex NCP problem and whether the artifacts introduced by the approximation are acceptable for robotics applications. In this work, we propose a new unconstrained convex approximation and discuss techniques for its efficient implementation. We carefully quantify the artifacts introduced by the convex approximation and evaluate the robustness and accuracy of our method on a family of examples. 

We introduce a two-stage time stepping approach (Section II-C) that allows us to incorporate both first and second order schemes such as the midpoint rule. In Section VI-B we demonstrate that the midpoint rule can achieve second order accuracy even in problems with frictional contact. Unlike previous work [34], [17] that formulates the problem in its dual form (impulses), we write a primal formulation of compliant contact in velocities (Section III-A). We then analytically eliminate constraints from this formulation to obtain an unconstrained convex problem (Section III-C). 

To solve this formulation, we develop SAP—the SemiAnalytic Primal solver—in Section IV and study its theoretical and practical convergence. Crucially, we show that SAP globally converges from all initial conditions (Appendix E) and warm-starts effectively using the previous time-step velocities, enabling simulation at interactive rates. 

To address accuracy and model validity, Section V-A provides compact analytic formulae for the impulses that correspond to the optimal velocities of the convex approximation. This provides intuition for the approximation, even to those without optimization expertise. Moreover, the artifacts introduced by the approximation become apparent and can be characterized precisely. We provide an exact mapping between the regularization introduced by Todorov [17] to _physical_ parameters of compliance. Therefore regularization is no longer treated as a tuning parameter of the algorithm but as a true physical parameterization of the contact model. This allows us to incorporate not only compliant point contact, but also complex models of compliant surface patches [35], [36], as we demonstrate in Section VI-D. 

We demonstrate the effectiveness of our approach in Section VI in a number of simulation cases, including the simulation of the challenging dual arm manipulation task shown in Fig. 1. We evaluate the accuracy, robustness and performance of SAP against available commercial and open-source optimization solvers. 

Finally, we discuss extensions and variations in Section VII, limitations in Section VIII and conclude with final remarks in Section IX. 

3 

## II. MULTIBODY DYNAMICS WITH CONTACT 

We use generalized coordinates (in particular joint coordinates) to describe our multibody system. Therefore, the state is fully specified by the generalized positions **q** _∈_ R<sup>_nq_</sup> and the generalized velocities **v** _∈_ R<sup>_nv_</sup> , where _nq_ and _nv_ denote the number of generalized positions and velocities, respectively. Time derivatives of the configurations relate to generalized velocities by the kinematic map **N** ( **q** ) _∈_ R<sup>_nq×nv_</sup> as 



## _A. Contact Kinematics_ 

Given a configuration **q** of the system, we assume our geometry engine reports a set _C_ ( **q** ) of _nc_ potential contacts between pairs of bodies. We characterize the _i_ -th _contact pair_ in _C_ ( **q** ) by the location **_p_** _i_ of the contact point, a normal direction **_n_** ˆ _i_ and _signed distance function_ [37], [38] _φi_ ( **q** ) _∈_ R, defined negative for overlapping bodies. The kinematics of each contact is further completed with the relative velocity **_v_** _c,i ∈_ R<sup>3</sup> between these two bodies at point **_p_** _i_ , expressed in a contact frame _Ci_ for which we arbitrarily choose the _z_ -axis to coincide with the contact normal **_n_** ˆ _i_ . In this frame the normal and tangential components of **_v_** _c,i_ are given by _vn,i_ = **_n_** ˆ _i ·_ **_v_** _c,i_ and **_v_** _t,i_ = **_v_** _c,i − vn,i_ ˆ **_n_** _i_ respectively, so that **_v_** _c,i_ = [ **_v_** _t,i vn,i_ ]. 

We form the vector **v** _c ∈_ R<sup>3</sup><sup>_nc_</sup> of contact velocities by stacking velocities **_v_** _c,i_ of all contact pairs together. In general, unless otherwise specified, we use bold italics for vectors in R<sup>3</sup> and non-italics bold for their stacked counterparts. The generalized velocities **v** and contact velocities **v** _c_ satisfy the equation **v** _c_ = **J v** , where **J** ( **q** ) _∈_ R<sup>3</sup><sup>_nc×nv_</sup> denotes the contact Jacobian. 

## _B. Contact Modeling_ 

We model the normal component of the impulse _γn_ during a time interval of size _δt_ with the compliant law 



where _k_ is the stiffness parameter, _τd_ is a _dissipation time scale_ and ( _x_ )+ = max(0 _, x_ ) is the _positive part_ operator. The _δt_ is needed to convert _forces_ into _impulses_ . This model of compliance can be written as the equivalent complementarity condition 



where _c_ = _k_<sup>_−_1</sup> is the compliance parameter and 0 _≤ a ⊥ b ≥_ 0 denotes complementarity, i.e. _a ≥_ 0, _b ≥_ 0 and _a b_ = 0. 

The tangential component **_γ_** _t ∈_ R<sup>2</sup> of the contact impulse is modeled with Coulomb’s law of dry friction as 



where _µ >_ 0 is the coefficient of friction. Equation (4) describes the _maximum dissipation principle_ , which states that friction impulses maximize the rate of energy dissipation. In other words, friction impulses oppose the sliding velocity direction. Moreover, (4) states that contact impulses **_γ_** are constrained to be in the friction cone _F_ = _{_ [ **_x_** _t, xn_ ] _∈_ 

R<sup>3</sup> _| ∥_ **_x_** _t∥≤ µxn}_ . The optimality conditions for Eq. (4) are [39], [29] 



where _λ_ is the multiplier needed to enforce Coulomb’s law condition _∥_ **_γ_** _t∥≤ µγn_ . Notice that in the form we write Eq. (5), multiplier _λ_ is zero during stiction and takes the value _λ_ = _∥_ **_v_** _t∥_ during sliding. Finally, the total contact impulse **_γ_** _∈_ R<sup>3</sup> expressed in the contact frame _C_ is given by **_γ_** = [ **_γ_** _t γn_ ]. 

## _C. Discrete Model_ 

We base our time-stepping scheme on the _θ_ -method [40, §II.7]. We discretize time into intervals of fixed size _δt_ and seek to advance the state of the system from time _t_<sup>_n_</sup> to the next step at _t_<sup>_n_+1</sup> = _t_<sup>_n_</sup> + _δt_ . In the _θ_ -method, variables are evaluated at intermediate time steps _t_<sup>_θ_</sup> = _θt_<sup>_n_+1</sup> + (1 _− θ_ ) _t_<sup>_n_</sup> , with _θ ∈_ [0 _,_ 1]. We define _mid-step quantities_ **q**<sup>_θ_</sup> , **v**<sup>_θ_</sup> , and **v**<sup>_θvq_</sup> in accordance with the standard _θ_ -method using scalar parameters _θ_ and _θvq_ 





where, to simplify notation, we use the naught subscript to denote quantities evaluated at the previous time step _t_<sup>_n_</sup> while no additional subscript is used for quantities at the next time step _t_<sup>_n_+1</sup> . Using these definitions we write the following time stepping scheme where the unknowns are the next time step generalized velocities **v** _∈_ R<sup>_nv_</sup> , impulses **_γ_** _∈_ R<sup>3</sup><sup>_nc_</sup> and multipliers **_λ_** _∈_ R<sup>_nc_</sup> 















where **M** ( **q** ) _∈_ R<sup>_nv×nv_</sup> is the mass matrix and **k** ( **q** _,_ **v** ) _∈_ R<sup>_nv_</sup> models external forces such as gravity, gyroscopic terms and other smooth generalized forces such as those arising from springs and dampers. 

This scheme includes some of the most popular schemes for forward dynamics: 

- Explicit Euler with _θ_ = _θvq_ = 0, 

- Symplectic Euler with _θ_ = 0 and _θvq_ = 1, 

- Implicit Euler with _θ_ = _θvq_ = 1, and 

- Symplectic midpoint rule, which is second order, with _θ_ = _θvq_ = 1 _/_ 2. 

Notice that in our version of the _θ_ -method, the additional parameter _θvq_ allows us to also incorporate the popular Symplectic Euler scheme. 

4 

When only conservative forces are considered in **k** ( **q** _,_ **v** ), the symplectic Euler scheme keeps the total mechanical energy bounded while exact energy conservations can be attained with the second order midpoint rule, see results in Section VI-B. In addition, stability analysis in [41], [42] shows that these implicit schemes are appropriate for the integration of stiff forces arising in multibody applications such as springs and dampers. 

## _D. Two-Stage Scheme_ 

Similar to the work in [43] for the simulation of deformable objects and to projection methods used in fluid mechanics [44], we solve Eqs. (7)-(12) in two stages. In the first stage, we solve for the _free motion velocities_ **v**<sup>_∗_</sup> the system would have in the absence of contact constraints, according to 



where we define the momentum residual **m** ( **v** ) from Eq. (7) as 



For integration schemes that are implicit in **v**<sup>_∗_</sup> (e.g. the implicit Euler scheme and the midpoint rule), we solve Eq. (13) with Newton’s method. For schemes explicit in **v**<sup>_∗_</sup> , only the mass matrix **M** needs to be inverted, which can be accomplished efficiently using the _O_ ( _n_ ) _Articulated Body Algorithm_ [45]. 

The second stage solves a linear approximation of the balance of momentum in Eq. (7) about **v**<sup>_∗_</sup> that satisfies the contact constraints, Eqs. (8)-(10). To write a convex formulation of contact in Section III, our linearization uses a symmetric positive definite (SPD) approximation of the Jacobian _∂_ **m** _/∂_ **v** . To achieve this, we split the non-contact forces **k** in Eq. (7) as 

Using this SPD approximation of _∂_ **m** _/∂_ **v** , the linearized balance of momentum (7) reads 



where for convenience we use **J** as a shorthand to denote **J** ( **q** 0). The approximation in Eq. (18) and the original discrete momentum update in Eq. (7) agree to second order as shown by the following result, proved in Appendix A. 

**Proposition 1.** _Matrix_ **A** _is a first order approximation to the Jacobian of_ **m** _, i.e.,_ 



_Therefore, Eq. (18) is a second order approximation of the discrete balance of momentum in Eq. (7). Moreover,_ **A** _≻_ 0 _._ 

Notice that, in the absence of constraint impulses, the velocities at the next time step are equal to the free motion velocities, i.e., **v** = **v**<sup>_∗_</sup> , and they are computed with the order of accuracy of the _θ_ -method. Furthermore, we also expect to recover the properties of the _θ_ -method when contact constraints are in stiction. As an example, for bodies in contact that are under rolling friction, the contact constraints behave as bi-lateral constraints that impose zero slip velocity. In this case, our two-stage method with the midpoint rule exhibits considerably less numerical dissipation than first order methods (see results in Section VI-B.) 

Even after the linearization of the balance of momentum in Eq. (18), the full problem with the contact constraints (8)(10) still consists of a non-convex nonlinear complementarity problem (NCP). This kind of problems are difficult to solve in practice, especially so in engineering applications for which robustness and accuracy are required. In the next section we introduce a number of approximations to this original NCP that allow us to make the problem tractable and solve it efficiently in practice. 



such that the Jacobians _∂_ **k** 1 _/∂_ **q** and _∂_ **k** 1 _/∂_ **v** are negative definite matrices while the same is generally not true for the Jacobians of **k** 2. The term **k** 1( **q** _,_ **v** ) can include forces from modeling elements such as spring and dampers. The term **k** 2( **q** _,_ **v** ) includes all other contributions that cannot guarantee negative definiteness of their Jacobians, such as Coriolis and gyroscopic forces arising in multibody dynamics with generalized coordinates. We can now define the SPD approximation of _∂_ **m** _/∂_ **v** evaluated at **v**<sup>_∗_</sup> as 







where **K** _≻_ 0 and **D** _≻_ 0 are the stiffness and damping matrices of the system, respectively. For joint level springdampers models, **K** and **D** are constant, diagonal, and positive definite matrices. Section VI-B shows the performance of our scheme for a system with a linear spring. 

## III. CONVEX APPROXIMATION OF CONTACT DYNAMICS 

In this section we build from previous work on convex approximations of contact [14], [16], [17] to write a new convex formulation of _compliant_ contact in terms of _velocities_ . 

## _A. Primal Formulation_ 

We introduce a new decision variable **_σ_** _∈_ R<sup>3</sup><sup>_nc_</sup> and set up our convex formulation of compliant contact as the following optimization problem 



where _∥_ **z** _∥_<sup>2</sup> _X_ = **z**<sup>_T_</sup> **Xz** with **X** _≻_ 0 and _F_<sup>_∗_</sup> = _F_ 1<sup>_∗×_</sup> _F_ 2<sup>_∗× · · · × F_</sup> _n_<sup>_∗_</sup> _c_<sup>isthe</sup><sup>_dualcone_ofthefrictioncone</sup><sup>_F_=</sup> _F_ 1 _× F_ 2 _× · · · × Fnc_ , with _×_ the Cartesian product. The positive diagonal matrix **R** _∈_ R<sup>3</sup><sup>_nc×_3</sup><sup>_nc_</sup> and the vector of stabilization velocities **v** ˆ _c_ encode the problem data needed to model compliant contact. We establish a very clear physical 

5 

meaning for these terms in Section V-A. We note that when _R_ and **_σ_** are removed, this reformulation reduces to [15]. We refer to (19) as the _primal formulation_ and next derive its dual. To begin, define the Lagrangian 



where **_γ_** _∈F_ is the dual variable for the constraint **_g_** _∈F_<sup>_∗_</sup> . Taking gradients of the Lagrangian with respect to **v** and **_σ_** leads to the optimality conditions 





Note that (21a) is a restatement of the balance of momentum (18) if the dual variable **_γ_** is interpreted as a vector of contact impulses. Using the optimality condition (21b) to eliminate **_σ_** from the Lagrangian yields the dual formulation 



where **W** = **JA**<sup>_−_1</sup> **J**<sup>_T_</sup> is the Delassus operator and **r** = **v** _c_<sup>_∗−_</sup> **v** ˆ _c_ with **v** _c_<sup>_∗_=</sup><sup>**Jv**</sup><sup>_∗_. In summary, we have proven the following</sup> theorem. 

**Theorem 1.** _The dual of_ (19) _is given by_ (22) _. Moreover, when {_ **v** _,_ **_σ_** _} is primal optimal and_ **_γ_** _is dual optimal,_ **_σ_** = **_γ_** _._ 

Finally, we note that the dual (22) is equivalent to the formulation in [16] when _θ_ = 0 in Eq. (7) and **A** = **M** ( **q** 0). 

## _B. Analytical Inverse Dynamics_ 

The dual optimal impulses of (22) can be constructed from the primal optimal velocities of (19) using a simple projection operation. Following [17], we call this construction _analytical inverse dynamics_ . Moreover, this projection decomposes into a set of individual projections for each contact impulse **_γ_** _i_ given the separable structure of the constraints. Letting **_y_** _i_ ( **_v_** _c,i_ ) = _−_ **_R_** _i_<sup>_−_1(</sup><sup>**_v_**</sup><sup>_c,i −_</sup><sup>**_v_**ˆ</sup><sup>_c,i_),theseprojectionstaketheform</sup> 



where **_R_** _i ∈_ R<sup>3</sup><sup>_×_3</sup> is the _i_ -th diagonal block of the regularization matrix **R** . That is, **_γ_** _i_ is the projection _PFi_ of **_y_** _i_ ( **_v_** _c,i_ ) onto the friction cone _Fi_ using the norm defined by **_R_** _i_ . Remarkably, the projection map _PFi_ can be evaluated _analytically_ . We provide algebraic expressions for it in Section V-A and derivations in Appendix C. The projection _PF_ ( **y** ) onto the full cone _F_ := _F_ 1 _× F_ 2 _× · · · × Fnc_ is obtained by simply stacking together the individual projections _PFi_ ( **_y_** _i_ ) from Eq. (23), where we form **y** by stacking together each **_y_** _i_ from all contact pairs. In this notation, the optimal impulse **_γ_** of (22) and the optimal velocities **v** of (19) satisfy **_γ_** = _PF_ ( **y** ( **v** )). 

## _C. An Unconstrained Convex Formulation_ 

We use the analytical **_γ_** = _PF_ ( **y** ( **v** )) from Section III-B and the optimality condition **_σ_** = **_γ_** from Theorem 1 to eliminate both **_σ_** and the constraints from the primal formulation (19). 

In total, we obtain the following unconstrained problem in velocities only 



Correctness of this reformulation is asserted by the following theorem, which we prove in Appendix B. 

**Theorem 2.** _If_ **v** _solves the unconstrained formulation (24), then_ ( **v** _,_ **_σ_** ) _, with_ **_σ_** = _PF_ ( **y** ( **v** )) _, solves the primal formulation (19)._ 

Lemma 2 in Appendix E shows that the unconstrained cost _ℓp_ ( **v** ) is strongly convex and differentiable with Lipschitz continuous gradients. Therefore, the unconstrained formulation (24) has a unique solution, and can be efficiently solved. Section IV presents our novel SAP solver specifically designed for its solution. 

We outline our time-stepping scheme in Algorithm 1. 

## **Algorithm 1** Overall Time-Stepping Strategy 

1: Solve free motion velocities from **m** ( **v**<sup>_∗_</sup> ) = **0** , Eq. (14) 2: Solve **v** = arg min _ℓp_ ( **v** ), Eq. (24) **v** 

3: Update positions **q** = **q** 0 + _δt_ **N** ( **q**<sup>_θ_</sup> ) **v**<sup>_θvq_</sup> , Eqs. (11)-(12) 

We note that Algorithm 1 is executed once per time step, with no inner iterations updating **A** . That is, our strategy is not solving the original, possibly nonlinear, balance of momentum (7) but its (second-order accurate) linear approximation in (18). This approximation can be exact for many multibody systems encountered in practice. For instance, joint springs and dampers contribute constant stiffness and damping matrices in (15). 

## IV. SEMI-ANALYTIC PRIMAL SOLVER 

Inspired by Newton’s method, our Semi-Analytic Primal Solver (SAP) seeks to solve (24) by monotonically decreasing the primal cost _ℓp_ ( **v** ) at each iteration, as outlined in Algorithm 2. 

## **Algorithm 2** The Semi-Analytic Primal Solver (SAP) 

- 1: Initialize **v** _m ←_ **v** 0 

- 2: **repeat until** _∥∇_<sup>˜</sup> _ℓp∥ < εa_ + _εr_ max( _∥_ **p** ˜ _∥, ∥_ **j**<sup>˜</sup> _c∥_ ), Eq. (26) 3: ∆ **v** _m_ = _−_ **H**<sup>_−_1</sup> ( **v** _m_ ) _∇_ **v** _ℓp_ ( **v** _m_ ) 4: _αm_ = arg min _t∈_ R<sup>++</sup><sup>_ℓp_(</sup><sup>**v**</sup><sup>_m_+</sup><sup>_t_∆</sup><sup>**v**</sup><sup>_m_)</sup> 

5: **v** _m_ +1 = **_v_** _m_ + _αm_ ∆ **v** _m_ 

6: **return** _{_ **v** , **_γ_** = _PF_ ( **_y_** ( **v** )) _}_ 

The SAP iterations require **H** ( **v** ) _≻_ 0 at all iterations. At points where _∇_ **v** _ℓp_ ( **v** ) is differentiable, **H** ( **v** ) is simply set equal to the Hessian of the cost function. In general, **H** ( **v** ) is evaluated using a partition of its domain. For each set in the partition, _∇_ **v** _ℓp_ ( **v** ) is differentiable on the interior, and the Hessian admits a simple formula. We globally define **H** ( **v** ) by adopting one of these Hessian formulas on the boundary. The partition is described in Appendix C. The Hessian formula are 

6 

given in Appendix D. Our convergence analysis in Appendix E also accounts for this definition. 

As shown in Appendix E, SAP globally converges at least at a linear-rate. Further, SAP exhibits quadratic convergence when _∇_<sup>2</sup> _ℓp_ exists in a neighborhood of the optimal **v** . In practice, we initialize SAP with the previous time-step velocity **v** 0. The stopping criteria is discussed below in Section IV-E. 

## _A. Gradients_ 

We provide a detailed derivation of the gradients in Appendix D. Here we summarize the main results required for implementation. The gradient of the primal cost _ℓp_ reduces to the balance of momentum 



where **_γ_** ( **v** ) = _PF_ ( **_y_** ( **v** )) is given by the analytical inverse dynamics (27). We define matrix **G** _⪰_ 0 that evaluates to _−∇_ **v** _c_ **_γ_** where _PF_ ( **y** ( **v** )) is differentiable. Otherwise **G** extends our analytical expressions as outlined in Appendix D. Matrix **G** is a block diagonal matrix where each diagonal block for the _i_ -th contact is a 3 _×_ 3 matrix. 

In total, we evaluate **H** via 

derivatives efficiently in _O_ ( _n_ ) operations. Defining _ℓ_ ( _α_ ) = _ℓp_ ( **v** + _α_ ∆ **v** ), we compute first and second derivatives as 



Using the gradients from Section IV-A, we can write 



These are computed efficiently by first calculating the change in velocity ∆ **v** _c_ := **J** ∆ **v** and change of momentum ∆ **p** := **A** ∆ **v** . The calculation is then completed via 



which only requires dot products that can be computed in _O_ ( _nv_ ) and _O_ ( _nc_ ) respectively. Similarly for the second derivatives 



Notice the first term on the right can be precomputed before the line search starts, while the second term only involves _O_ ( _nc_ ) operations given the block diagonal structure of **G** . 



which is strictly positive definite since **A** _≻_ 0. 

## _B. Line Search_ 

The line search algorithm is critical to the success of SAP given that _∇ℓp_ ( **v** ) can rapidly change during contactmode transitions. We explore two line search algorithms: an approximate backtracking line search with Armijo’s stopping criteria and an exact (to machine epsilon) line search. 

At the _m_ -th Newton iteration, backtracking line search starts with a maximum step length of _α_ Max and progressively decreases it by a factor _ρ ∈_ (0 _,_ 1) as _α ← ρα_ until Armijo’s criteria [46, §3.1] is satisfied. We write Armijo’s criteria as _ℓp_ ( **v**<sup>_m_</sup> + _α_ ∆ **v**<sup>_m_</sup> ) _< ℓp_ ( **v**<sup>_m_</sup> ) + _c α dℓp/dα_ ( **v**<sup>_m_</sup> ). Typical parameters we use are _ρ_ = 0 _._ 8, _c_ = 10<sup>_−_4</sup> and _α_ Max = 1 _._ 25. 

For the exact line search we use the method rtsafe [47, §9.4] to find the unique root of _dℓ/dα_ . This is a onedimensional root finder that uses the Newton-Raphson method and switches to bisection when an iterate falls outside a search bracket or when convergence is slow. The fast computation of derivatives we show next allows us to iterate _α_ to machine precision at a negligible impact on the computational cost. In practice, this is our preferred algorithm since it allows us to use very low regularization parameters without having to tune tolerances in the line search. 

## _C. Efficient Analytical Derivatives For Line Search_ 

The algorithm rtsafe requires the first and second directional derivatives of _ℓp_ . We show how to compute these 

## _D. Problem Sparsity_ 

The block sparsity of **H** is best described with an example. We organize our multibody systems as a collection of articulated _tree structures_ , or a _forest_ . Consider the system in Fig. 2. In this example, a robot arm mounted on a mobile 



Fig. 2: An example of a sparsity pattern commonly encountered in the simulation of robotic mechanical systems. The graph on the right puts _trees_ as nodes and contact _patches_ as edges. 

base constitutes its own tree, here labeled _t_ 1. The number of degrees of freedom of the _t_ -th tree will be denoted with _nt_ . A free body is a common case of a tree with _nt_ = 6. In general, matrix **A** has a block diagonal structure where each diagonal block corresponds to a tree. 

We define as _patches_ a collection of contact pairs between two trees. Each contact pair corresponds to a single cone constraint in our formulation. The set of constraint indexes that belong to patch _p_ is denoted with _Ip_ of size (cardinality) _|Ip|_ = _rp_ . Figure 2 shows the corresponding graph where nodes correspond to trees and edges correspond to patches. 

Generally, the Jacobian is sparse since the relative contact velocity only involves velocities of two trees in contact, Fig. 3. Each non-zero block **J** _pt_ has size 3 _rp ×nt_ . Since **A** is block diagonal, **H** inherits the sparsity structure of **J**<sup>_T_</sup> **GJ** . 

7 

We exploit this structure using a supernodal Cholesky factorization [48, §9] that can take advantage of dense algebra optimizations. Implementing this factorization requires construction of a _junction tree_ . For this we apply the algorithm in [49], using cliques of **H** as input. We use the implementation from the Conex solver [50]. 

The scalability of SAP, like any second-order optimization method, depends on the complexity of solving the Newton system. For dense problems, this has _O_ ( _n_<sup>3</sup> _v_<sup>) complexity, where</sup> _nv_ denotes the number of generalized velocities. For sparse problems the complexity can be dramatically reduced [48]. We study scalability with number of bodies in Section VI-C. Recent work on the modeling of contact rich patches [36] studies the scalability of SAP with the number of constraints. 

## _E. Stopping Criteria_ 

To assess convergence, we monitor the norm of the optimality condition for the unconstrained problem (24) 



Notice that the components of _∇ℓp_ have units of generalized momentum **p** = **Mv** . Depending on the choice of generalized coordinates, the generalized momentum components may have different units. In order to weigh all components equally, we define the diagonal matrix **D** = diag( **M** )<sup>_−_1</sup><sup>_/_2</sup> and perform the following change of variables 



where we define the generalized contact impulse **j** _c_ = **J**<sup>_T_</sup> **_γ_** . With this scaling, all the new _tilde_ variables have the same units, square root of Joules. Using these definitions, we write our stopping criteria as 



where _εr_ is a dimensionless relative tolerance that we usually set in the range from 10<sup>_−_6</sup> to 10<sup>_−_1</sup> . The absolute tolerance _εa_ is used to detect rare cases where the solution leads to no contact and no motion, typically due to external forces. We always set this tolerance to a small number, _εa_ = 10<sup>_−_16</sup> . 

## V. CONTACT MODELING PARAMETERS 

Thus far, **_R_** _i_ and **_v_** ˆ _c,i_ have been treated as known problem data. This section makes an explicit connection of these quantities with physical parameters to model compliant contact with regularized friction. We seek to model compliant contact as in Eq. (2), parameterized by physical parameters: stiffness _k_ (in N/m) and _dissipation time scale τd_ (in seconds). Therefore, users of this model only need to provide these physical parameters and regularization is computed from them. Notice this approach is different from the one in [17], where regularization is not used to model physical compliance but rather to introduce a user tunable Baumgarte-style stabilization to avoid constraint drift. 

_A. Compliant Contact, Principle of Maximum Dissipation and Artifacts_ 

Dropping subscript _i_ for simplicity, we solve the projection problem in Eq. (23) analytically in Appendix C for a regularization matrix of the form **_R_** = diag([ _Rt, Rt, Rn_ ]) 



where **_y_** _t_ and _yn_ are the tangential and normal components of **_y_** , _yr_ = _∥_ **_y_** _t∥_ is the radial component, and **_t_**<sup>ˆ</sup> = **_y_** _t/yr_ is the unit tangent vector. We also define the coefficients _µ_ ˜ = _µ_ ( _Rt/Rn_ )<sup>1</sup><sup>_/_2</sup> and _µ_ ˆ = _µ Rt/Rn_ that result from the _warping_ introduced by the metric **_R_** . 

Our compliant model of contact is defined by 



where _φ_ 0 is the previous step signed distance reported by the geometry engine. The normal direction regularization parameters is taken as _Rn_<sup>_−_1</sup> = _δtk_ ( _δt_ + _τd_ ). To gain physical insight into our model, we substitute **_y_** = _−_ **_R_**<sup>_−_1</sup> ( **_v_** _c −_ **_v_** ˆ _c_ ) into Eq. (27) to obtain 



where _φ_ = _φ_ 0 + _δt vn_ approximates the signed distance function at the next time step. 

Let us now analyze the resulting impulses from this model. **Friction Impulses** . We see that friction impulses behave exactly as a model of regularized friction 



with **_γ_** _t_ linear with the (very small) slip velocity during stiction and with the maximum value given by _µγn_ , effectively modeling Coulomb’s friction. Notice that to better model stiction, we are interested in small values of _Rt_ . We discuss our parameterization of _Rt_ in Section V-B. Moreover, since **_t_** ˆ = **_y_** _t/∥_ **_y_** _t∥_ = _−_ **_v_** _t/∥_ **_v_** _t∥_ , friction impulses oppose sliding and therefore satisfy the principle of maximum dissipation. 

**Normal impulses** . We observe that in stiction, we recover the compliant model given by Eq. (2), as desired. In the sliding region, however, we see that the convex approximation introduces unphysical artifacts. 

Firstly, the factor 1 + _µ_ ˜<sup>2</sup> models an effective stiffness _k_ eff = _k/_ (1+ ˜ _µ_<sup>2</sup> ) different from the physical value. Therefore 

8 



Fig. 3: Block sparsity of the contact Jacobian **J** and the Hessian term **J**<sup>_T_</sup> **GJ** , for the example illustrated in Fig. 2. 

to accurately model compliance during sliding we must satisfy the condition _µ_ ˜ = _µ_ ( _Rt/Rn_ )<sup>1</sup><sup>_/_2</sup> _≈_ 0 or, equivalently, _Rt ≪ Rn_ . Section V-B introduces a parameterization of _Rt_ that satisfies this condition. 

Secondly, we see that the slip velocity **_v_** _t_ unphysically couples into the normal impulses as _γn_ = _−δtk_ ( _φ_ eff + _τd vn_ ) with an _effective_ signed distance _φ_ eff = _φ −_ ( _δt_ + _τd_ ) _µ∥_ **_v_** _t∥_ . That is, we recover the dynamics of compliant contact but with a spurious drift of magnitude ( _δt_ + _τd_ ) _µ∥_ **_v_** _t∥_ . This is consistent with the formulation in [34] for rigid contact when _k →∞_ and _τd_ = 0, leading to an unphysical _gliding effect_ at a positive distance _φ_ = _δtµ∥_ **_v_** _t∥_ . Notice that the _gliding_ goes away as _δt →_ 0 since the formulation converges to the original contact problem [14]. The effect of compliance is to _soften_ this gliding effect. With finite stiffness, the normal impulse when sliding goes to _−k_ ( _φ − τdµ∥_ **_v_** _t∥_ ) _− d vn_ in the limit to _δt →_ 0. This tells us that, unlike the rigid case, the _gliding_ effect unfortunately does not go away as _δt →_ 0. It persists with a finite value that now depends on the dissipation rate, _φ ≈ τdµ∥_ **_v_** _t∥_ . 

We close this discussion by making the following remarks relevant to robotics applications: 

- 1) We are mostly interested in the stiction regime, typically for grasping, locomotion, or rolling contact for mobile bases with wheels. This regime is precisely where the convex approximation does not introduce artifacts. 

- 2) Sliding usually happens with low velocities and therefore the term _δtµ∥_ **_v_** _t∥_ is negligible. 

- 3) For robotics applications, we are mostly interested in inelastic contact. We will see that this can be effectively modeled with _τd ≈ δt_ in Section V-B. Therefore, in this regime, the term _τdµ∥_ **_v_** _t∥_ also goes to zero as _δt →_ 0. 

- 4) We are definitely interested in the onset of sliding. This is captured by the approximation which properly models the Colulomb friction law. 

## _B. Conditioning of the Problem_ 

Regularization parameters not only determine the physical model, but also affect the robustness and performance of the SAP solver. Modeling near-rigid objects and avoiding viscous drift during stiction require very small values of _Rt_ and _Rn_ that can lead to badly ill-conditioned problems. Under these conditions, the Hessian of the system exhibits a large condition number, and round-off errors can render the search direction of Newton iterations useless. We show in this section how a judicious choice of the regularization parameters leads to much better conditioned system of equations, without sacrificing accuracy. This is demonstrated in Section VI with a variety of tests cases. 

**Near-Rigid Contact** . In our formulation rigid objects must be modeled as _near-rigid_ using large stiffnesses. However, as mentioned above, blindly choosing large values of stiffness can lead to ill-conditioned systems of equations. Here, we propose a principled way to choose the stiffness parameter when modeling near-rigid contact. 

Consider the dynamics of a mass particle _m_ laying on the ground, with contact stiffness _k_ and dissipation time scale _τd_ . When in contact, the dynamics of this particle is described by the equations of a harmonic oscillator with natural frequency _ωn_<sup>2=</sup><sup>_k/m_,orperiod</sup><sup>_Tn_=2</sup><sup>_π/ωn_,anddampingratio</sup> _ζ_ = _τdωn/_ 2. We say the contact is _near-rigid_ when _Tn_ ≲ _δt_ and the time step _δt_ cannot temporally resolve the contact dynamics. In this _near-rigid_ regime, we use compliance as a means to add a Baumgarte-like _stabilization_ to avoid constraint drift, as similarly done in [16]. Choosing the time scale of the contact to be _Tn_ = _βδt_ with _β ≤_ 1, we model inelastic contact with a dissipation that leads to a critically damped oscillator, or _ζ_ = 1. This dissipation is _τd_ = 2 _ζ/ωn_ , or in terms of the time step, 



Using the harmonic oscillator equations, we can estimate = the value of stiffness from the frequency _ωn_ as _k_ 4 _π_<sup>2</sup> _m/_ ( _β_<sup>2</sup> _δt_<sup>2</sup> ). Since _τd ≈ δt_ , _Rn_<sup>_−_1</sup> = _δtk_ ( _δt_ + _τd_ ) _≈ δt_<sup>2</sup> _k_ , and we estimate the regularization parameter as 



where we define w = 1 _/m_ . 

It is useful to estimate the amount of penetration for a point mass resting on the ground. In this case we have 



independent of mass. Taking _β_ = 1 _._ 0 and Earth’s gravitational constant, a typical simulation time step of _δt_ = 10<sup>_−_3</sup> s leads to _φ ≈_ 2 _._ 5 _×_ 10<sup>_−_7</sup> m, and a large simulation time step of _δt_ = 10<sup>_−_2</sup> s leads to _φ ≈_ 2 _._ 5 _×_ 10<sup>_−_5</sup> m, well within acceptable bounds to consider a body rigid for typical robotics applications. 

For a general multibody system, we define the per-contact effective mass as w _i_ = _∥_ **W** _ii∥_ rms = _∥_ **W** _ii∥/_ 3 where **W** _ii_ is the 3 _×_ 3 diagonal block of the Delassus operator **W** = **JM**<sup>_−_1</sup> **J**<sup>_T_</sup> for the _i_ -th contact. Explicitly forming the Delassus operator is an expensive operation. Instead we use an _O_ ( _n_ ) approximation. Given contact _i_ involving trees _t_ 1 and _t_ 2, we form the approximation **W** _ii ≈_ **J** _it_ 1 **M**<sup>_−_</sup> _t_ 1<sup>1</sup><sup>**J**</sup><sup>_T_</sup> _it_ 1<sup>+</sup><sup>**J**</sup><sup>_it_</sup> 2<sup>**M**</sup> _t_<sup>_−_</sup> 2<sup>1</sup><sup>**J**</sup><sup>_T_</sup> _it_ 2<sup>.</sup> Finally, we compute the regularization parameter in the normal 

9 

direction as 



With this strategy, our model automatically switches between modeling compliant contact with stiffness _k_ when the time step _δt_ can resolve the temporal dynamics of the contact, and using stabilization to model near-rigid contact with the amount of stabilization controlled by parameter _β_ . In all of our simulations, we use _β_ = 1 _._ 0. 

**Stiction** . Given that our model regularizes friction, we are interested in estimating a bound on the slip velocity at stiction. We propose the following regularization for friction 



where _σ_ is a dimensionless parameter. 

To understand the effect of _σ_ in the approximation of stiction, we consider once again a point of mass _m_ in contact with the ground under gravity, for which w _≈_ 1 _/m_ . We push the particle with a horizontal force of magnitude _F_ = _µγn_ so that friction is right at the boundary of the friction cone and the slip velocity due to regularization, _vs_ , is maximized. Then in stiction, we have 



Using our proposed regularization in Eq. (30), we find the maximum slip velocity 



independent of the mass and linear with the time step size. Even though the friction coefficient _µ_ can take any nonnegative value, most often in practical applications _µ <_ 1. Values on the order of 1 are in fact considered as large friction values. Therefore, for this analysis we consider _µ ≈_ 1. In all of our simulations, we use _σ_ = 10<sup>_−_3</sup> . With Earth’s gravitational constant, a typical simulation with time step of _δt_ = 10<sup>_−_3</sup> s leads to a stiction velocity of _vs ≈_ 10<sup>_−_5</sup> m _/_ s, and with a large step of _δt_ = 10<sup>_−_2</sup> s, _vs ≈_ 10<sup>_−_4</sup> m _/_ s. Smaller friction coefficients lead to even tighter bounds. These values are well within acceptable bounds even for simulation of grasping tasks, which is significantly more demanding than simulation for other robotic applications, see Section VI. 

**Sliding Soft Contact** . As we discussed in Section V-A, we require _Rt/Rn ≪_ 1 so that we model compliance accurately during sliding. Now, in the _near-rigid_ contact regime, the condition _Rt/Rn ≪_ 1 is no longer required since in this regime regularization is used for stabilization. Therefore, we only need to verify this condition in the _soft contact_ regime, when time step _δt_ can properly resolve the contact dynamics, i.e. according to our criteria, when _δt < Tn_ . In this regime, _Rn_<sup>_−_1</sup> _≈ δt_<sup>2</sup> _k_ , and using Eq. (30) we have 



where in the last inequality we used the assumption that we are in the soft regime where _δt < Tn_ . Since _σ ≪_ 1 and in particular we use _σ_ = 10<sup>_−_3</sup> in all of our simulations, we see 

that _Rt/Rn ≪_ 1. Moreover, _Rt/Rn_ goes to zero quadratically with _δt/Tn_ as the time step is reduced and the dynamics of the compliance is better resolved in time. 

Summarizing, we have shown that our choice of regularization parameters enjoys the following properties 

- 1) Users only provide physical parameters; contact stiffness _k_ , dissipation time scale _τd_ , and friction coefficient _µ_ . There is no need for users to tweak solver parameters. 

- 2) In the _near-rigid_ limit, our regularization in Eq. (29) automatically switches the method to model rigid contact with constraint stabilization to avoid excessively large stiffness parameters and the consequent ill-conditioning of the system. 

- 3) Frictional regularization is parameterized by a single dimensionless parameter _σ_ . We estimate a bound for the slip velocity during stiction to be _vs ≈ µσδtg_ . For _σ_ = 10<sup>_−_3</sup> , the slip during stiction is well within acceptable bounds for robotics applications. 

- 4) We show that _Rt/Rn ≪_ 1 when _δt_ can resolve the dynamics of the compliant contact, as required to accurately model compliance during sliding. 

## VI. TEST CASES 

We evaluate the robustness, accuracy, and performance of our method in a number of simulation tests. All simulations are carried out in a system with 24 2.2 GHz Intel Xeon cores (E5-2650 v4) and 128 GB of RAM, running Linux. However, all of our tests are run in a single thread. 

For all of our simulations, unless otherwise specified, our model uses _β_ = 1 _._ 0 and _σ_ = 10<sup>_−_3</sup> for the regularization parameters in Eq. (29) and Eq. (30), respectively. 

## _A. Performance Comparisons Against Other Solvers_ 

We evaluate commercial software Gurobi, considered an industry standard, to solve our primal formulation (19). As an open source option, we evaluate the Geodesic interiorpoint method (IPM) from [50]. Geodesic IPMs, in contrast with primal-dual IPMs, do not apply Newton’s method to the central-path conditions directly. Instead, they use geodesic curves that satisfy the complementarity slackness condition. Since the Geodesic IPM and SAP use the same supernodal linear algebra code described in Section IV-D, it is natural to compare their performance. 

For performance comparisons, we use the steady clock from the STL std::chrono library to measure wall-clock time for SAP and Geodesic IPM. For Gurobi we access the Runtime property reported by Gurobi. Notice this is somewhat unfair to SAP and Geodesic IPM since Gurobi’s reported time does not include the cost of the initial setup. 

## _B. Spring-Cylinder_ 

We model the setup shown in Fig. 4, consisting of a cylinder of radius _R_ = 0 _._ 05 m and mass _m_ = 0 _._ 5 kg connected to a wall to its left by a spring of stiffness _ks_ = 100 N _/_ m. While the cylinder is free to rotate and translate in the plane, the ground constrains the cylinder’s motion in the vertical 

10 

direction. The contact stiffness is _k_ = 10<sup>4</sup> N _/_ m and the dissipation time scale is _τd_ = 0 _._ 02 s. The cylinder is initially placed with zero velocity at _x_ 0 = 0 _._ 1 m to the right of the spring’s resting position, and it is then set free. 



Fig. 4: Spring-Cylinder system. The cylinder can translate horizontally and rotate. Friction with the ground establishes a non-dissipative rolling contact. 

For reference, we first simulate this setup with frictionless contact, i.e. with _µ_ = 0. Without friction, the cylinder does not rotate and we effectively have a spring-mass system with natural frequency _ωn_ = ~~�~~ _ks/m_ . We use a rather coarse time step of _δt_ = 0 _._ 02 s, discretizing each period of oscillation with about 22 steps. Figure 5 shows the total mechanical energy as a function of time computed using three different schemes; symplectic Euler, midpoint rule, and implicit Euler. The amount of numerical dissipation introduced by the implicit Euler scheme dissipates the initial energy in just a few periods of oscillation. For the symplectic Euler scheme, we observe in Fig. 5 that, while the energy is not conserved, it stays bounded, within a band 28% peak-to-peak wide. The figure also confirms that the second order midpoint scheme conserves energy exactly. These are well known theoretical properties of these integration schemes when applied to the spring-mass system. 





Fig. 5: Total mechanical energy for the frictionless springcylinder system in the first few periods of oscillation (left) and long term (right). 

We now focus our attention to a case with frictional contact using _µ_ = 1. As we release the cylinder from its initial position at _x_ 0 = 0 _._ 1 m, friction with the ground establishes a rolling contact, and the system sets into periodic motion. Since now kinetic energy is split into translational and rotational components, the rolling cylinder behaves as a spring-mass system with an effective mass _m_ eff = _m_ + _Io/R_<sup>2</sup> , with _Io_ the rotational inertia of the cylinder about its center. Therefore the frequency of oscillation is slower, and the same time step, _δt_ = 0 _._ 02 s, now discretizes one period of oscillation with about 27 steps. 

Total energy is shown in Fig. 6. Solutions computed with the implicit Euler and the symplectic Euler scheme show similar trends to those in the frictionless case. The midpoint rule does not conserve energy exactly but it does significantly better, with a peak-to-peak variation of only 0.16%. While the ideal rolling contact does not dissipate energy, the regularized model of friction does dissipate energy given the slip velocity is never exactly zero, though small in the order of _∼ σµδtg_ as shown in Section V-A. The symplectic Euler scheme and the midpoint rule take 10 minutes of simulated time and about 1000 oscillations to dissipate 10% of the total energy (Fig. 6, right). This level of numerical dissipation is remarkably low, considering that real mechanical systems often introduce several sources of dissipation. 





Fig. 6: Total mechanical energy for the spring-cylinder system with friction _µ_ = 1 in the first few periods of oscillation (left) and long term (right). 

To study the order of accuracy of our approach, we define the _L_<sup>2</sup> -norm position error as 



where _xe_ ( _t_ ) is the known exact solution. We simulate for _T_ = 5s, about 10 periods of oscillation. Figure 7 shows the position error as a function of the time step. We see that even with frictional contact, the two-stage approach with the midpoint rule achieves second order accuracy. Both the implicit Euler and the symplectic Euler scheme are first order, though the error is significantly smaller when using the symplectic Euler scheme. 



Fig. 7: Position error as a function of time step for the springcylinder system with friction. First and second order references are shown with dashed lines. 

11 









Fig. 8: Initial conditions (top) and an intermediate configuration after 2 seconds of simulated time (bottom) for the clutter setup with (left) and without (right) walls. Many of the spheres in the configuration with no walls roll outside the frame in the intermediate configuration. 

## _C. Clutter_ 

Objects are dropped into an 80 cm _×_ 80 cm _×_ 80 cm container in four different columns with the same number of objects in each (see Fig. 8). Each column consists of an arbitrary assortment of spheres of radius 5 cm and boxes with sides of 10 cm in length. With a density of 1000kg _/_ m<sup>3</sup> , spheres have a mass of 0 _._ 524 kg and boxes have a mass of 1 _._ 0 kg. We set a very high contact stiffness of _k_ = 10<sup>12</sup> N _/_ m so that the model is in the _near-rigid_ regime. The dissipation time scale is set to equal the time step and the friction coefficient of all surfaces is _µ_ = 1 _._ 0. 

We first run our simulations with 10 bodies per column for a total of 40 bodies. We simulate 10 seconds using time steps of size _δt_ = 10 ms. Number of solver iterations and wall-clock time per time step are reported in Fig. 9. We observe that SAP needs to perform a larger number of iterations during the very energetic initial transient. As the system reaches a steady state, however, SAP warm starts very effectively, performing only about 3 iterations per time step. Even though SAP necessities a larger number of iterations to converge than Geodesic IPM during this initial transient, the wall-clock time per time step is very similar. Unlike SAP and Geodesic IPM that benefit from warm start, Gurobi performs about 9 iterations per time step in both the initial transient and the steady state. 

Figure 10 shows two examples of convergence history. We denote with _ℓ_<sup>0</sup> the cost evaluated at the initial guess, the previous time step velocity. With _ℓ∗_ we denote the optimal cost, which we approximate with its value from the last iteration. At step 60 during the initial transient for which SAP requires 21 iterations to converge, we observe that 





Fig. 9: Iterations and wall-clock time per time step for the clutter case with 40 bodies and with walls. 

the algorithm reaches quadratic convergence after an initial linear convergence transient, matching theoretical predictions (Appendix E). At step 520, past the initial energetic transient, SAP exhibits linear convergence and satisfies the convergence criteria within 5 iterations. 





Fig. 10: Cost as a function of Newton iterations for step 60 (left) and for step 520 (right) using SAP. The cost decreases monotonically. Reference lines are shown for linear convergence (dotted) and quadratic convergence (dashed). 

_1) Scalability:_ We evaluate the scalability of SAP by varying the number of objects in the clutter. We study the case with and without walls (see Fig. 8) as this variation leads to very different contact configurations and sparsity patterns. The size of the problems can be appreciated in Fig. 11 showing the number of contact constraints at the end of the simulation when objects are in steady state. We observe a larger number of contacts for the configuration without walls since in this configuration many of the boxes spread over the ground and lay flat on one of their faces, leading to multicontact configurations (see Fig. 8). 



Fig. 11: Total number of contacts with objects in steady state at the end of the simulation for setups with and without walls. 

12 

We define the _speedup_ against Gurobi as the ratio of the wall-clock time spent by a solver to the wall-clock time reported by Gurobi. Figure 12 shows the speedup for both SAP and Geodesic IPM in the configuration with and without walls. The setup with walls is particularly difficult given that objects are constrained to pile up, leading to a configuration in which almost all objects are coupled with every other object by frictional contact (see Fig. 8). For example, the motion of an object at the bottom of the pile can lead to motion of another object far on top of the pile. In contrast, the simulation with no walls leads to _islands_ of objects that do not interact with each other. 

In general, we observe two regimes. For problems with less than about 40 bodies, SAP outperforms Gurobi significantly by up to a factor of 25 in the case with walls and up to a factor of 50 with no walls. Beyond 80 bodies, Gurobi outperforms both SAP and Geodesic IPM in the case with walls, but SAP is about 10 times faster for the case with no walls. Though SAP shows to be about twice as fast as Geodesic IPM for most problem sizes, it can be five times faster for small problems with 8 bodies or less. 





Fig. 12: Speedup against Gurobi for the configuration with walls (left) and without walls (right). 

It could be argued that these speedup results depend on the accuracy settings of each solver. For a fair comparison, we define the dimensionless momentum error as 



using the scaled generalized momentum quantities in Eq. (25). We also define the dimensionless complementarity slackness error as 



Figure 13 shows average values of _em_ and _eµ_ over all time steps. Since SAP satisfies the complementarity slackness exactly, _eµ_ is not shown. We have verified this to be true within machine precision for all simulated cases. 

SAP’s momentum error is below 10<sup>_−_5</sup> as expected since this is the value used for the termination condition. Similarly, the complementarity slackness is below 10<sup>_−_5</sup> for Geodesic IPM, since this is the value used for its own termination condition. Gurobi does a good job at satisfying the complementarity slackness. However, it is the solver with the largest error in the momentum equations, even though both SAP and Geodesic IPM outperform Gurobi in most of the test cases. 

These metrics demonstrate that when SAP and Geodesic IPM outperform Gurobi, it is not at the expense of accuracy. 









Fig. 13: Momentum balance error _em_ (top) and complementarity condition error _eµ_ (bottom) for the clutter case with walls (left) and without walls (right). 

_2) Slip Parameter:_ We study the effect of the slip parameter _σ_ in Eq. (30). We use _δt_ = 10 ms and simulate with SAP 40 objects for 10 seconds to a steady state configuration. At this steady state, we compute the mean slip velocity among all contacts, shown in Fig. 14 along with the estimated slip in Eq. (31), _vs ≈ σµδtg_ . We see that the mean slip velocity remains below the estimated slip as expected in a static configuration with objects in stiction. In the case with walls where stiction helps to hold the steady state static configuration, we see that the mean slip velocity closely follows the slope of the slip estimate. Without the walls, objects do not pile up in a complex static structure but simply lie on the ground, and therefore, the resulting slip velocities are significantly smaller. The sudden drop in the slip velocity for _σ >_ 10<sup>_−_3</sup> is caused by the sensitivity of the final state on the value of _σ_ . As _σ_ increases, so does the slip velocity bound _vs_ and objects in the configuration without walls can slowly drift into a configuration leading to more contacts. In particular, boxes are more likely to slowly drift until one of their faces lies flat on the ground, a configuration with zero slip once steady state is reached. 

We conclude by examining the effect of _σ_ on the conditioning of the system. Figure 15 shows the condition number of the Hessian in the final configuration and the mean number of Newton iterations throughout the simulation. We see that the condition number scales as _σ_<sup>_−_1</sup> while the mean number of Newton iterations is roughly proportional to ln( _σ_ ). Our default choice _σ_ = 10<sup>_−_3</sup> is a good compromise between accurate stiction, performance and conditioning. 

## _D. Slip Control_ 

While previous work on convex approximations model rigid contact [14], [15] or use regularization as a means of constraint 

13 



Fig. 14: Mean slip velocity at the end of the simulation with objects at rest as a function of the slip parameter. The estimated bound _vs_ = _σµδtg_ is shown in dashed lines. 





Fig. 15: Effect of the slip parameter on the mean Newton iterations per step (left) and mean condition number (right). 



Fig. 16: Highly compliant _Soft-bubble_ gripper [51] holding a spatula. Unlike traditional point contact approaches, the hydroelastic contact model provides rich contact information and captures area-dependent phenomena such as the net-torque to hold the spatula. Contact patches are colored by contact pressure. 





Fig. 17: Grip force command (left) and spatula pitch angle (right) as a function of time. 

stabilization [17], our work is novel in that we incorporate physical compliance. This allows us not only to model compliant point contact, but also to incorporate sophisticated models of surfaces patches. We incorporate the pressure field model [35] implemented as part of Drake’s [24] _hydroelastic contact_ model. We use the discrete approximation introduced in [36] to approximate each face of the contact surface as a compliant contact point at its centroid. 

To demonstrate this capability, we reproduce the test in [36] that models a _Soft-bubble_ gripper [51]; a parallel jaw WSG 50 Schunk gripper outfitted with air filled compliant surfaces (Fig. 16). The aforementioned gripper is simulated anchored to the world holding a spatula by the handle horizontally. We use _δt_ = 5 _×_ 10<sup>_−_3</sup> s. The grasp force is commanded to vary between 1 N and 16 N with square wave having a 6 second period and a 75% duty cycle (see Fig. 17, left). This results in a periodic transition from a secure grip to a loose grip allowing the spatula to pitch in a controlled manner within grasp (see Fig. 17 and the accompanying video). These contact mode transitions are resolved by our model. We observe that stiction during the secure grip is properly resolved with the tight bounds for the slip due to regularization discussed in Section V-B. While this case only has 8 degrees of freedom, it generates about 60 contact constraints during the slip phase and about 160 contact constraints during the stiction phase. 

We compare the performance of SAP against both Gurobi and Geodesic IPM, see Section VI-A. For SAP we use a relative tolerance _εr_ = 10<sup>_−_3</sup> , see Section IV-E. For Gurobi we set its tolerance parameter BarQCPConvTol to 10<sup>_−_8</sup> . For 

Geodesic IPM, we set its complementary slackness tolerance to 10<sup>_−_6</sup> ; larger values lead to failure for this task. SAP bounds the momentum error, exhibiting a maximum value of of 9 _._ 99 _×_ 10<sup>_−_2</sup> %. Even with such a tight tolerance, Gurobi exhibits 2 _._ 6 % maximum error. Geodesic IPM’s errors are significantly smaller, below 2 _×_ 10<sup>_−_4</sup> %. However its robustness is very sensitive to the specified tolerance. 

Even though SAP’s solutions are significantly more accurate than those from Gurobi, it performs 92 times faster than Gurobi. SAP is 20 times faster than Geodesic IPM and significantly more robust to solver tolerances. In terms of solver iterations, SAP only performs 0.62 iterations on average, showcasing how effectively it warm-starts. Geodesic IPM performs 5.6 iterations per step on average and Gurobi performs 10.1 iterations on average. 

## _E. Dual Arm Manipulation_ 

We demonstrate the effectiveness of our approach with the simulation of a complex manipulation task. In this scenario, two Kuka IIWA arms (7 DOFs each) are outfitted with anthropomorphic Allegro hands (16 DOFs each) (Fig. 1). In front of the robot, a table has a jar (with a lid, 12 DOFs) full of 16 marbles of 50 gr each (96 DOFs) and a bowl (6 DOFs), completing the model with a total of 160 DOFs. Contact between the jar and the lid is modeled using Drake’s hydroelastic model [35], [36] (see Section VI-D), while point 

14 

contact is used for all other interactions. The time step is set to _δt_ = 5 _×_ 10<sup>_−_3</sup> s. 

The arms’ controllers track a prescribed sequence of Cartesian end-effector keyframe poses, while the hands’ controllers track prescribed _open/close_ configurations. We use force feedback to gauge successful grasps and to know when the jar makes contact with the table. The robot is commanded to open the jar, pour its contents into the bowl, close the lid and put the empty jar back in place (keyframes in Fig. 1 and the accompanying video). 

This particular task generates hundreds of contact constraints, as shown in Fig. 18 which also labels important events during the task. We remark that our framework predicts contact mode switching as a result of the computation. For instance, the lid initially covering the jar is held by stiction and it transitions to sliding as the robot pulls it out. 



Fig. 18: Number of contact constraints as a function time. Important events during the task are highlighted. 

To assess accuracy, we evaluate the dimensionless momentum and complementarity slackness errors defined in Eqs. (32) and (33) respectively. We perform the simulation of the same task several times using different solver tolerances. The results of these runs are shown in Figures 19 and 20. Even though each solver uses a different tolerance parameter, it is still useful to place these tolerances in the same horizontal axis. The maximum tolerance we use for each solver corresponds to the largest value that can be used to complete the task successfully. For Gurobi and Geodesic IPM, smaller values of the tolerance parameter make the simulation impractically slow. SAP on the other hand cannot achieve errors below 10<sup>_−_6</sup> for this case due to round-off errors. Figures 19 and 20 show both mean and median of the errors over the entire simulation to show errors do not follow a symmetric distribution. More interesting however are the minimum and maximum errors, shown as shaded areas. SAP guarantees that momentum errors are below the specified tolerance, given this is precisely its stopping criteria in Eq. (26). We see however that it is difficult to correlate the expected error to solver tolerance when using Gurobi or Geodesic IPM. In practice, we consistently observe that the robot does not complete the task successfully when momentum errors are larger than about 10%, regardless of the solver. Therefore, we find that being able to specify a tolerance for the momentum error directly is immensely useful. Given that SAP satisfies the complementarity slackness condition exactly, complementarity slackness error for SAP is not included in Fig. 20. 



Fig. 19: Dimensionless momentum error, defined in Eq. (32). Mean (solid) and median (dashed) errors along with minimum and maximum errors (shaded areas) over the entire simulation. 



Fig. 20: Dimensionless complementarity slackness error, defined in Eq. (33). Mean (solid) and median (dashed) errors along with minimum and maximum errors (shaded areas) over the entire simulation. Figure 21 shows the mean number of iterations per time-step for each solver. We see that the number of iterations needed by the SAP solver is consistently below the other two solvers given how effectively SAP warm-starts from the previous timestep solution. 

To make a fair comparison among solvers, from Fig. 19 we choose tolerances for each solver that result in similar values of the mean momentum error. For Gurobi, we set its tolerance parameter BarQCPConvTol to 10<sup>_−_8</sup> . For Geodesic IPM, we set its complementary slackness tolerance to 10<sup>_−_6</sup> . For SAP, we set its relative tolerance to 10<sup>_−_3</sup> . Notice this is not entirely fair to SAP, given that SAP does guarantee the maximum momentum error to be below 10<sup>_−_3</sup> , while this is not true for the other two solvers. Still, SAP is 7.4 faster than Gurobi and 2.2 faster than Geodesic IPM. In terms of iterations, SAP performs 4 iterations on average while Geodesic IPM performs 8.3 iterations on average. This shows that since both solvers use exactly the same sparse algebra, the performance gains with SAP are entirely due to its ability to warm-start effectively rather than to differences in the implementation. The general purpose solver Gurobi on the other hand performs 10.1 iterations on average. 

In summary, the simulation of this complex robotic task demonstrates how accuracy translates directly to robustness. We observe how the maximum momentum error defined in Eq. 

15 



Fig. 21: Mean number of iterations per time-step for the dual arm simulation. 

(32) is a good proxy for robustness in simulation; simulations with errors larger than about 10% could not complete the task successfully. In this regard, SAP provides a certificate of accuracy that proves useful in practice. 

## VII. VARIATIONS AND EXTENSIONS 

The method presented in this paper can be extended in several ways: 

**Expand the family of constraints:** No doubt contact constraints are the most challenging. However, our method can be extended to include bilateral constraints, PD controllers with force limits and even joint dry friction [17]. 

**Branch induced sparsity:** In this work we exploit sparsity only at the tree level. However, branch sparsity can lead to additional performance. Consider for instance a standing humanoid robot with a floating hip. Since arms and the upper torso are not in contact with the ground, they can be eliminated from the computation. Additional performance gains could be attained using specialized algebra for multibody dynamics [52]. 

**Parallelization:** This work focuses on accuracy, robustness, and convergence properties of the algorithm executed in a single thread. The sparse algebra can be parallelized and, in particular, disjoint _islands_ of bodies can be solved separately in different threads. 

**Deformable FEM models:** Using the SAP solver for the modeling of deformable objects with contact and friction is the topic of current research efforts by the authors. FEM models lead to state dependent stiffness (16) and damping (17) matrices with a complex structure that requires specialized handling of sparsity. Moreover, modeling assumptions must be carefully analyzed in order to ensure the positive definiteness of these matrices used in our convex approximation of contact. 

**Differentiation:** Since forces are a continuous function of state, the model is well suited for applications requiring gradients such as trajectory optimization, machine learning, parameter estimation, and control. Factorizations computed during forward dynamics can be reused when computing gradients for a performant implementation. 

## VIII. LIMITATIONS 

All models are approximations of reality, while numerical methods can only approximate our models. We list here the limitations we identify for our method. 

**Convex Approximation:** The convex approximation amounts to a _gliding effect_ during sliding at a distance _φ ∼ δtµ∥_ **_v_** _t∥_ . Regularization leads to a model of regularized friction, Eq. (28). Details are provided in Section V. 

**Stiffness and Dissipation:** Our method requires stiffness **K** and damping **D** matrices to be SPD or SPD approximations (see Section II-D). For joint level spring-dampers, the exact **K** and **D** can be used, but for other forces such as those arising from a spatial arrangement of springs, an SPD approximation must be made as **K** might not be SPD in certain configurations. 

**Linear Approximations:** Algorithm 1 evaluates the SPD gradient **A** once at **v**<sup>_∗_</sup> at each time step. In other words, our method replaces the original balance of momentum (7) with its linear approximation (18). This is exact for many important cases and accurate to second-order in the general case. See Section III-C for details. 

**Delassus Operator Estimation:** In Section V-B we use a diagonal approximation of the Delassus operator to estimate stiffness in the _near-rigid_ regime. Corner cases exist. Consider a pile of books. While the inertia of a contact at the bottom of the pile is estimated solely on the mass of one book, this contact is supporting the weight of the entire stack. Stiffness is underestimated and user intervention is needed to set proper parameters. 

**Scalability:** We see no reason SAP with the direct supernodal algebra (Section IV-D) could not scale to thousands of bodies if there is structured sparsity. However, scalability needs to be studied further, along with the usage of iterative solvers such as Conjugate Gradient (CG), widely used in optimization. 

## IX. CONCLUSION 

We presented a novel unconstrained convex formulation of compliant contact. In this formulation constraints are eliminated using analytic formulae that we developed. Our scheme incorporates the midpoint rule into a two-stage scheme, with demonstrated second order accuracy. We rigorously characterized our numerical approximations and the artifacts introduced by the convex approximation of contact. We reported limitations of our method and discussed extensions and areas of further research. 

We showed that regularization maps to physical compliance, allowing us to eliminate algorithmic parameters and to incorporate complex models of continuous contact patches. Moreover, we studied the trade off between regularization and numerical conditioning for the simulation of _near-rigid_ bodies and the accurate resolution of stiction. 

We presented SAP, a robust and performant solver that warm-starts very effectively in practice. SAP globally converges at least at a linear-rate and exhibits quadratic convergence when additional smoothness conditions are satisfied. SAP can be up to 50 times faster than Gurobi in small problems with up to a dozen objects and up to 10 times 

16 

faster in medium sized problems with about 100 objects. Even though SAP uses the supernodal algebra implemented for Geodesic IPM, it performs at least two times faster due to its effective warm-starts from the previous time-step solution. Moreover, SAP is significantly more robust in practice given that it guarantees a hard bound on the error in momentum, effectively providing a certificate of accuracy. 

We have incorporated SAP into the open source robotics toolkit Drake [24], and hope that the simulation and robotics communities can benefit from our contribution. 



The Taylor expansion of **m** ( **v** ) at **v** = **v**<sup>_∗_</sup> reads 



where we use the fact that by definition **m**<sup>_∗_</sup> = **m** ( **v**<sup>_∗_</sup> ) = **0** . All derivatives are evaluated at **v** = **v**<sup>_∗_</sup> unless otherwise noted. We first evaluate the Jacobian of the mass matrix term in Eq. (14) 



where we defined 



Note that by combining Eqs. (6) and (12), the mid-step configuration **q**<sup>_θ_</sup> can be written as 



Hence by the chain rule, **E** can be further calculated as 



Notice that 



since _∥_ **v**<sup>_∗_</sup> _−_ **v** 0 _∥_ = _O_ ( _δt_ ). 

We proceed similarly to expand the Jacobian of **F** 1( **v** ) = **F** 1( **q**<sup>_θ_</sup> ( **v** ) _,_ **v**<sup>_θ_</sup> ( **v** )) as 



with **K** and **D** the stiffness and damping matrices defined by Eqs. (16)-(17). 

We can now write the Jacobian of **m** ( **v** ) in Eq. (34) as 



where we defined 

**A** = **M** + _δt_<sup>2</sup> _θθqv_ **K** + _δtθ_ **D** _._ 

With these definitions the Taylor expansion in Eq. (34) becomes 



Since contact is compliant, forces are finite within the finite interval _δt_ and therefore _∥_ **v** _−_ **v**<sup>_∗_</sup> _∥_ = _O_ ( _δt_ ). Thus 



Therefore, the positive definite linearization 

**A** ( **v** _−_ **v**<sup>_∗_</sup> ) + _OE_ ( _δt_<sup>3</sup> ) + _OF_ 2( _δt_<sup>2</sup> ) + _Om_ ( _δt_<sup>2</sup> ) = **J**<sup>_T_</sup> **_γ_** _,_ 

agrees with the original momentum balance in Eq. (7) to second order. 

Finally, notice that **A** is a linear combination of positive definite matrices with non-negative scalars in the linear combination, and therefore **A** _≻_ 0. 



Before proving this theorem, we need the following result. **Lemma 1.** _The conic constraint_ **g** ( **v** _,_ **_σ_** ) _∈F_<sup>_∗_</sup> _is satisfied if_ **_σ_** _is given by PF_ ( **y** ( **v** )) _._ 

_Proof:_ Since **_σ_** is the projection of **y** ( **v** ) to the cone _F_ with the **R** norm, by Moreau’s decomposition theorem, we know that **y** ( **v** ) _−_ **_σ_** is in the polar cone of _F_ with the **R** norm. That is, _⟨_ **y** ( **v** ) _−_ **_σ_** _,_ **x** _⟩_ **R** _≤_ 0 for all **x** _∈F_ , with the inner product _⟨_ **v** _,_ **w** _⟩_ **R** = **v**<sup>_T_</sup> **Rw** . Reorganizing terms, we get 



for all **x** _∈F_ . Therefore, it follows that _−_ **g** = _−_ ( **v** _c −_ **v** ˆ _c_ + **R** **_σ_** ) is in the polar cone of _F_ and thus **g** is in the dual cone of _F_ . 

The optimality condition for the unconstrained formulation in (24) is _∇ℓp_ ( **v** ) = **0** . It is shown in Appendix D that 



with impulses given by **_γ_** ( **v** ) = _PF_ ( **y** ( **v** )), the dual optimal. Therefore, _∇ℓp_ ( **v** ) = **0** implies (21a), the first optimality condition for (19). 

The analytical inverse dynamics solution shows that **_γ_** = _PF_ ( **y** ( **v** )) with the primal optimal **v** . Hence, choosing **_σ_** = _PF_ ( **y** ( **v** )) with the primal optimal **v** satisfies (21b), the second optimality condition for (19). 

Finally, by Lemma 1, the cone constraint **g** ( **v** _,_ **_σ_** ) _∈F_<sup>_∗_</sup> is satisfied. 

17 

## APPENDIX C 

## ANALYTICAL INVERSE DYNAMICS 

We perform the projection in Eq. (23) for a regularization of the form **_R_** = diag([ _Rt, Rt, Rn_ ]). For simplicity, we drop contact subindex _i_ . We make the change of variables **_γ_** ˜ = **_R_**<sup>1</sup><sup>_/_2</sup> **_γ_** and **_y_** ˜ = **_R_**<sup>1</sup><sup>_/_2</sup> **_y_** [17], and observe that **_γ_** ˜ is the Euclidian projection of **_y_** ˜ onto cone _F_<sup>˜</sup> with coefficient _µ_ ˜ = _µ_ ( _Rt/Rn_ )<sup>1</sup><sup>_/_2</sup> . We conclude that 



We partition R<sup>3</sup> into three regions, see Fig. 22: closed cone _F_ ˜, denoted with _RI_ , the interior of the polar _F_ ˜<sup>_◦_</sup> , denoted with _RIII_ , and the remaining area, which we denote with _RII_ . For **_y_** ˜ _∈RI_ we simply have that _P_ ˜ _F_<sup>(˜</sup><sup>**_y_**)=</sup><sup>**_y_**˜.When</sup><sup>**_y_**˜</sup><sup>_∈RIII_,</sup> _P_ ˜ _F_<sup>(˜</sup><sup>**_y_**)=</sup><sup>**0**.Finally,when</sup><sup>**_y_**˜</sup><sup>_∈RII_,weevaluate</sup><sup>_P_˜</sup> _F_<sup>(˜</sup><sup>**_y_**)via</sup> Euclidean projection onto the boundary of _F_<sup>˜</sup> <u>,</u> which admits a simple formula. We define **_f_**<sup>ˆ</sup> = [˜ _µ_ **_t_**<sup>ˆ</sup> _,_ 1] _/_ ~~�~~ 1 + _µ_ ˜<sup>2</sup> , the unit vector along the wall of the cone shown in Fig. 22, with **_t_** ˆ = **_y_** ˜ _t/∥_ **_y_** ˜ _t∥_ = **_y_** _t/∥_ **_y_** _t∥_ . Then the projection is computed as **_γ_** ˜ = (˜ **_y_** _·_ **_f_**<sup>ˆ</sup> ) **_f_**<sup>ˆ</sup> . After some algebraic manipulation we have that _P_ ˜ _F_<sup>(˜</sup><sup>**_y_**) = [˜</sup><sup>**_γ_**</sup><sup>_t,_˜</sup><sup>_γn_]with</sup> 



where _y_ ˜ _r_ = _∥_ **_y_** ˜ _t∥_ . Note that this formula is well-defined on _RII_ , since **_y_** _t_ = **0** only if **_y_** is in regions _RI_ or _RIII_ . 



Fig. 22: Geometry of the projection and regions in the **_y_** ˜ space. 

Finally, we apply the inverse transformation **_γ_** = **R**<sup>_−_1</sup><sup>_/_2</sup> _P_ ˜ _F_<sup>(˜</sup><sup>**_y_**)andaftersomealgebraicmanipulationwere-</sup> cover the projection **_γ_** = _PF_ ( **_y_** ) in Eq. (27). 





We will start by taking derivatives of the regularizer term _ℓR_ . First we notice that we can write this term as 



with _ℓRi_ = 1 _/_ 2 _∥_ **_γ_** _i∥_<sup>2</sup> _Ri_<sup>.Since</sup><sup>_∇_</sup><sup>**_y_**</sup> _j_<sup>_ℓR_</sup> _i_<sup>=</sup><sup>**0**for</sup><sup>_i̸_=</sup><sup>_j_,weonly</sup> need to compute the gradients of _ℓRi_ ( **y** ) with respect to the contact point variable **_y_** _i ∈_ R<sup>3</sup> . Dropping contact subindex _i_ for simplicity, we write the regularization as 



We use Eq. (27) to write the cost in terms of **_y_** as 



## _A. Gradients per Contact Point_ 

We use the following identities to simplify expressions 



where the 2 _×_ 2 projection matrix is 

**_P_**<sup>_⊥_</sup> ( **_t_**<sup>ˆ</sup> ) = **_I_** 2 _−_ **_P_** ( **_t_**<sup>ˆ</sup> ) _,_ with **_P_** ( **_t_**<sup>ˆ</sup> ) = **_t_**<sup>ˆ</sup> _⊗_ **_t_**<sup>ˆ</sup> _._ 

Taking the gradient of Eq. (35) results in 



with _s_ ˆ<sup>_◦_</sup> ( **_y_** ) = _µy_ ˆ _r_ + _yn_ positive in the sliding region. We note that _∇_ **_y_** _ℓR_ ( **_y_** ) is not differentiable at the boundaries of _F_ and _F_<sup>_◦_</sup> . At points of differentiability, the Hessian _∇_<sup>2</sup> **_y_**<sup>_ℓR_(</sup><sup>**_y_**)</sup> is computed by taking derivatives of Eq. (36) 



Clearly in the stiction region we have _∇_<sup>2</sup> **_y_**<sup>_ℓR_(</sup><sup>**_y_**)</sup><sup>_≻_0.</sup> Since in the stiction region we have _s_ ˆ<sup>_◦_</sup> ( **_y_** ) _>_ 0, the linear combination of **_P_** ( **_t_**<sup>ˆ</sup> ) and **_P_** ( **_t_**<sup>ˆ</sup> )<sup>_⊥_</sup> in Eq. (37) is PSD (since both projection matrices are PSD). Therefore _∇_<sup>2</sup> **_y_**<sup>_ℓR_(</sup><sup>**_y_**)</sup><sup>_⪰_0.</sup> 

## _B. Gradients with Respect to Velocities_ 

Recall we use bold italics for vectors in R<sup>3</sup> and non-italics bold for their stacked counterpart. With **y** = _−_ **R**<sup>_−_1</sup> ( **Jv** _−_ **v** ˆ _c_ ) we use the chain rule to compute the gradient in terms of velocities 



which, using Eq. (36), can be shown to equal 



At points of differentiability, we obtain the Hessian of the regularizer _ℓR_ ( **v** ) from the gradient of **_γ_** ( **v** ) in Eq. (39) 



18 

where _∇_ **v** _c_ **_γ_** is a block diagonal matrix where each diagonal block is the 3 _×_ 3 matrix _∇_ **v** _c,i_ **_γ_** _i_ for the _i_ -th contact. Alternatively, taking the gradient of Eq. (38) leads to the equivalent result 



where we can verify indeed that _−∇_ **v** _c_ **_γ_** = **R**<sup>_−_1</sup> _∇_<sup>2</sup> **y**<sup>_ℓR_</sup><sup>**R**</sup><sup>_−_1.</sup> Since _∇_<sup>2</sup> **y**<sup>_ℓR⪰_0,itfollowsthat</sup><sup>_−∇_</sup><sup>**v**</sup> _c_<sup>**_γ_**</sup><sup>_⪰_0.</sup> 

We define **_G_** _i ∈_ R<sup>3</sup><sup>_×_3</sup> the matrix that evaluates to _−∇_ **v** _c,i_ **_γ_** _i_ within regions _RI_ , _RII_ and _RIII_ where the projection is differentiable. At the boundary of _F_ we use the analytical expression from _RI_ . At the boundary of _F_<sup>_◦_</sup> we use the analytical expression from _RII_ . This extension fully specifies **_G_** _i_ for all **_y_** _i ∈_ R<sup>3</sup> . Finally, we define the 3 _nc ×_ 3 _nc_ matrix **G** = diag( **_G_** _i_ ) _⪰_ 0. 

## _C. Gradients of the Primal Cost_ 

With these results, we can now write the gradient _∇_ **_v_** _ℓp_ and weighting matrix **H** in Algorithm 2. For the gradient we have 



which using Eq. (39) can be written as 



and since the unconstrained minimization seeks to satisfy the optimality condition _∇_ **v** _ℓp_ = **0** , we recover the balance of momentum. 

- _The function ℓp_ ( **v** ) _is differentiable and has Lipschitz continuous gradients, i.e., ∇ℓp_ ( **v** ) _exists for all_ **v** _and there exists L ≥_ 0 _satisfying_ 



_Proof._ The objective _ℓp_ ( **v** ) is a function _f_ : R<sup>_n_</sup> _→_ R of the following form 



where **Z** _∈_ R<sup>_m×n_</sup> , **W** _∈_ R<sup>_n×n_</sup> is symmetric and positive definite, and _dK_ : R<sup>_m_</sup> _→_ R denotes the distance function of a closed, convex set _K ⊆_ R<sup>_m_</sup> as measured by some quadratic norm _∥_ **x** _∥Q_ , i.e., 



The sum of a strongly convex function with a convex function is strongly convex. Since the squared distance function is convex, and the quadratic term **v**<sup>_T_</sup> **Wv** is strongly convex (given that **W** _≻_ 0), the first statement holds. The second statement follows trivially if we can show it holds for the squared distance function. Differentiability follows from Chapter 4 (Theorems 5.3-i 6.1-i) of [53], which shows that 



That the gradient of _d_<sup>2</sup> _K_<sup>(</sup><sup>**v**) is Lipschitz follows from Lipschitz</sup> continuity of projection maps onto closed, convex sets. 

Finally, we define the weighting matrix **H** as 



which, given the definition of **G** , returns the Hessian of _ℓp_ ( **_v_** ) when the gradient is differentiable and extends the analytical expressions at points of non-differentiability. Since **A** _≻_ 0 and **G** _⪰_ 0, we have **H** _≻_ 0. 

## APPENDIX E CONVERGENCE ANALYSIS OF SAP 

Convergence of SAP is established by first showing that the objective function _ℓp_ ( **v** ) =<sup><u>1</u></sup> 2<sup>_∥_</sup><sup>**v**</sup><sup>_−_</sup><sup>**v**</sup><sup>_∗∥_</sup> _A_<sup>2+</sup><sup>_PF_(</sup><sup>**y**(</sup><sup>**v**))</sup><sup>_∥_2</sup> _R_ is _strongly convex_ and differentiable with _Lipschitz continuous_ gradients. The former property is inherited from the positivedefinite quadratic term provided by the positive definite matrix **A** in Eq. (24). The latter is shown using differentiability of the squared-distance function and the Lipschitz continuity of its gradient map (Theorems 5.3-i 6.1-i of [53]) combined with the identity 



for any closed, convex cone _K_ . Here the distance and projection functions are with respect to the norm _∥· ∥_ **R** , while _K_<sup>_◦_</sup> denotes the polar cone with respect to the corresponding inner-product **x**<sup>_T_</sup> **Ry** . 

**Lemma 2.** _The following statements hold._ 

- _The function ℓp_ ( **v** ) _is strongly convex, i.e., there exists µ >_ 0 _such that_ 



We remark that strong convexity implies the reverse Lipschitz inequality _∥∇f_ ( **v** ) _−∇f_ ( **u** ) _∥≥ µ∥_ **v** _−_ **u** _∥_ , which in turn means that the parameter _µ_ and the Lipschitz constant _L_ satisfy _µ ≤ L_ . Recall that SAP (Algorithm 2) is a special case of the following iterative method for minimizing a function _f_ : R<sup>_n_</sup> _→_ R given some initial point **v** 0 _∈_ R<sup>_n_</sup> : 



where **H** : R<sup>_n_</sup> _→_ R<sup>_n×n_</sup> is a function into the set of symmetric positive definite matrices, i.e., **H** ( **v** ) = **H** ( **v** )<sup>_T_</sup> and **H** ( **v** ) _≻_ 0 for all **v** _∈_ R<sup>_n_</sup> . It is well known that gradient descent exhibits linear convergence to the global minimum when applied to a strongly convex function with Lipschitz continuous gradient. Incorporating a condition number bound _σ_ for **H** ( **v** ) into standard gradient-descent analysis will prove that the iterations (40) also have linear convergence. To show this, we let cond( **H** ( **v** )) denote the condition number of **H** ( **v** ) and _S_ ( **v** 0) denote the sub-level set _{_ **v** _∈_ R<sup>_n_</sup> : _f_ ( **v** ) _≤ f_ ( **v** 0) _}_ . 

**Lemma 3.** _Let f_ : R<sup>_n_</sup> _→_ R _be strongly convex and differentiable with Lipschitz-continuous gradients. Fix_ **v** 0 _∈_ R<sup>_n_</sup> _. If there exists σ >_ 0 _such that cond_ ( **H** ( **v** )) _≤ σ for all_ **v** _∈ S_ ( **v** 0) _, then the iterations_ (40) _converge to the global minimum_ **v** _∗ of f_ ( **v** ) _when initialized at_ **v** 0 _. Moreover,_ 



19 

_for all iterations m, where µ is the strong-convexity parameter of f_ ( **v** ) _and L is the Lipschitz constant of ∇f_ ( **v** ) _._ 

_Proof._ Dropping the subscript _m_ from ( **v** _m, tm,_ **d** _m_ ), we first observe that 



by Lipschitz continuity. Substituting **d** = _−_ **H**<sup>_−_1</sup> _∇f_ ( **v** ) gives 



Letting _λmax_ and _λmin_ denote the maximum and minimum eigenvalues of **H** evaluated at **v** , it also follows that 



Letting _t_<sup>¯</sup> denote the minimizer of the right-hand-side, we conclude that 



where the first inequality follows from the exact line search used to select _t_ . Since _σ_<sup>2</sup> _≥ λ_<sup>2</sup> max<sup>_/λ_2</sup> min<sup>,weconcludethat</sup> 



On the other hand, letting _f∗_ = _f_ ( **v** _∗_ ) we have from strong convexity that the Polyak-Lojasiewicz inequality holds: 



Hence, 



Subtracting _f∗_ from both sides and factoring shows 



It follows that each iteration _m_ satisfies 



Since _σ ≥_ 1 and _L ≥ µ_ , the iterations converge, and the proof is completed. 

Combining these lemmas shows that SAP globally convergences at (at least) a linear rate. By observing that SAP reduces to Newton’s method when the gradient is differentiable, we can also prove local quadratic convergence assuming differentiability on a neighborhood of the optimum **v** _∗_ . 

**Theorem 3.** _The following statements hold._ 

- _SAP globally converges from all initial conditions._ 

- _If ∇f_ ( **v** ) _is differentiable on the ball B_ ( **v** _∗, r_ ) := _{_ **v** : _∥_ **v** _−_ **v** _∗∥≤ r} for some r >_ 0 _, then SAP exhibits quadratic convergence, i.e., for some finite M and ζ >_ 0 



_Proof._ The first statement follows from Lemmas 2 and 3. 

To prove the second, we show that _B_ ( **v** _∗, r_ ) contains a sublevel set Ω _β_ = _{_ **v** : _f_ ( **v** ) _≤ β}_ for some _β >_ 0, implying that SAP reduces to Newton’s method with exact line search for some _m > M_ , given that sublevel sets are invariant. 

To begin, we have, by strong convexity, that 



for all **v** _∈_ Ω _β_ . Rearranging shows that 



Hence, _B_ ( **v** _∗, r_ ) contains Ω _β_ for any _β_ satisfying 2<sup>_<u>β−f</u>_</sup> _µ_<sup><u>(</u></sup><sup>**v**</sup><sup>_∗_</sup><sup><u>)</u></sup> _< r_ . For some finite _M_ , we also have that _vm ∈_ Ω _β_ for all _m > M_ by Lemma 3. 

_µ_<sup><u>(</u></sup><sup>**v**</sup><sup>_∗_</sup><sup><u>)</u></sup> _<_ 

Next, we prove that Newton iterations are quadratically convergent with exact line search. Indeed, using once more the strong convexity result in Eq. (41) 



where the first line uses strong convexity, the third exact line search, and the last Lipschitz continuity. But for some _κ >_ 0, we have that _∥_ **v** _m_ + **d** _m −_ **v** _∗∥_<sup>2</sup> _≤ κ∥_ **v** _m −_ **v** _∗∥_<sup>4</sup> by quadratic convergence of Newton’s method with unit step-size ([46, Theorem 3.5]). Hence, 



and the claim is proven. 

## ACKNOWLEDGMENT 

The authors would like to thank especially to Michael Sherman for his trust on this research from day one and to the Dynamics & Simulation and Dexterous Manipulation teams at TRI for their continuous patience and support. 

## REFERENCES 

- [1] D. Baraff, “Issues in computing contact forces for non-penetrating rigid bodies,” _Algorithmica_ , vol. 10, no. 2, pp. 292–352, 1993. 

- [2] S. Hogan and K. U. Kristiansen, “On the regularization of impact without collision: the painlev´e paradox and compliance,” _Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences_ , vol. 473, no. 2202, p. 20160773, 2017. 

- [3] J.-S. Pang and D. E. Stewart, “Differential variational inequalities,” _Mathematical programming_ , vol. 113, no. 2, pp. 345–424, 2008. 

- [4] E. J. Haug, S. C. Wu, and S. M. Yang, “Dynamics of mechanical systems with coulomb friction, stiction, impact and constraint additiondeletion—i theory,” _Mechanism and Machine Theory_ , vol. 21, no. 5, pp. 401–406, 1986. 

- [5] D. E. Stewart and J. C. Trinkle, “An implicit time-stepping scheme for rigid body dynamics with inelastic collisions and coulomb friction,” _International Journal for Numerical Methods in Engineering_ , vol. 39, no. 15, pp. 2673–2691, 1996. 

- [6] M. Anitescu and F. A. Potra, “Formulating dynamic multi-rigid-body contact problems with friction as solvable linear complementarity problems,” _Nonlinear Dynamics_ , vol. 14, no. 3, pp. 231–247, 1997. 

20 

- [7] J. Li, G. Daviet, R. Narain, F. Bertails-Descoubes, M. Overby, G. E. Brown, and L. Boissieux, “An implicit frictional contact solver for adaptive cloth simulation,” _ACM Transactions on Graphics (TOG)_ , vol. 37, no. 4, pp. 1–15, 2018. 

- [8] D. E. Stewart, “Convergence of a time-stepping scheme for rigid-body dynamics and resolution of painlev´e’s problem,” _Archive for Rational Mechanics and Analysis_ , vol. 145, no. 3, pp. 215–260, 1998. 

- [9] D. M. Kaufman, S. Sueda, D. L. James, and D. K. Pai, “Staggered projections for frictional contact in multibody systems,” _ACM Trans. Graph._ , vol. 27, no. 5, Dec. 2008. 

- [10] D. Baraff, “Fast contact force computation for nonpenetrating rigid bodies,” in _Proceedings of the 21st annual conference on Computer graphics and interactive techniques_ , 1994, pp. 23–34. 

- [11] C. Duriez, F. Dubois, A. Kheddar, and C. Andriot, “Realistic haptic rendering of interacting deformable objects in virtual environments,” _IEEE transactions on visualization and computer graphics_ , vol. 12, no. 1, pp. 36–47, 2006. 

- [12] E. Coumans and Y. Bai, “Pybullet, a python module for physics simulation for games, robotics and machine learning,” http://pybullet.org, 2016–2020. 

- [13] K. Erleben, “Velocity-based shock propagation for multibody dynamics animation,” _ACM Transactions on Graphics (TOG)_ , vol. 26, no. 2, pp. 12–es, 2007. 

- [14] M. Anitescu, “Optimization-based simulation of nonsmooth rigid multibody dynamics,” _Mathematical Programming_ , vol. 105, no. 1, pp. 113– 143, 2006. 

- [15] H. Mazhar, D. Melanz, M. Ferris, and D. Negrut, “An analysis of several methods for handling hard-sphere frictional contact in rigid multibody dynamics,” Citeseer, Tech. Rep., 2014. 

- [16] E. Todorov, “A convex, smooth and invertible contact model for trajectory optimization,” in _2011 IEEE International Conference on Robotics and Automation_ . IEEE, 2011, pp. 1071–1076. 

- [17] ——, “Convex and analytically-invertible dynamics with contacts and constraints: Theory and implementation in mujoco,” in _2014 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2014, pp. 6054–6061. 

- [18] D. Kang and J. Hwangho, “SimBenchmark. Physics engine benchmark for robotics applications: RaiSim vs. Bullet vs. ODE vs. MuJoCo vs. DartSim.” https://leggedrobotics.github.io/SimBenchmark. 

- [19] R. Smith, “Open dynamics engine,” http://www.ode.org/. 

- [20] J. Lee, M. X. Grey, S. Ha, T. Kunz, S. Jain, Y. Ye, S. S. Srinivasa, M. Stilman, and C. K. Liu, “Dart: Dynamic animation and robotics toolkit,” _Journal of Open Source Software_ , vol. 3, no. 22, p. 500, 2018. 

- [21] CM Labs Simulations, “Theory guide: Vortex software’s multibody dynamics engine,” https://www.cm-labs.com/vortexstudiodocumentation. 

- [22] “AGX Dynamics,” https://www.algoryx.se/products/agx-dynamics. [23] J. Hwangbo, J. Lee, and M. Hutter, “Per-contact iteration method for solving contact dynamics,” _IEEE Robotics and Automation Letters_ , vol. 3, no. 2, pp. 895–902, 2018. [Online]. Available: www.raisim.com 

- [24] R. Tedrake and the Drake Development Team, “Drake: Model-based design and verification for robotics,” https://drake.mit.edu, 2019. 

- [25] A. M. Castro, A. Qu, N. Kuppuswamy, A. Alspach, and M. Sherman, “A transition-aware method for the simulation of compliant contact with regularized friction,” _IEEE Robotics and Automation Letters_ , vol. 5, no. 2, pp. 1859–1866, 2020. 

- [26] A. Tasora, R. Serban, H. Mazhar, A. Pazouki, D. Melanz, J. Fleischmann, M. Taylor, H. Sugiyama, and D. Negrut, “Chrono: An open source multi-physics dynamics engine,” T. Kozubek, Ed. Springer, 2016, pp. 19–49. 

- [27] E. Todorov, “MuJoCo,” http://www.mujoco.org. 

- [28] V. Acary, O. Bonnefon, M. Br´emond, O. Huber, F. P´erignon, and S. Sinclair, “An introduction to siconos,” INRIA, Tech. Rep., 2019. 

_Journal for Numerical Methods in Engineering_ , vol. 122, no. 16, pp. 4093–4113, 2021. 

   - [33] V. Acary, M. Br´emond, and O. Huber, “On solving contact problems with coulomb friction: formulations and numerical comparisons,” in _Advanced Topics in Nonsmooth Dynamics_ . Springer, 2018, pp. 375– 457. 

   - [34] M. Anitescu and A. Tasora, “An iterative approach for cone complementarity problems for nonsmooth dynamics,” _Computational Optimization and Applications_ , vol. 47, no. 2, pp. 207–235, 2010. 

   - [35] R. Elandt, E. Drumwright, M. Sherman, and A. Ruina, “A pressure field model for fast, robust approximation of net contact force and moment between nominally rigid objects,” in _2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2019, pp. 8238–8245. 

   - [36] J. Masterjohn, D. Guoy, J. Shepherd, and A. Castro, “Discrete approximation of pressure field contact patches,” 2021, preprint available at https://arxiv.org/abs/2110.04157. 

   - [37] P. Flores, “Contact mechanics for dynamical systems: a comprehensive review,” _Multibody System Dynamics_ , pp. 1–51, 2021. 

   - [38] F. Pfeiffer and C. Glocker, _Multibody Dynamics with Unilateral Contacts_ , ser. Wiley Series in Nonlinear Science. Wiley, 1996. 

   - [39] D. E. Stewart, “Rigid-body dynamics with friction and impact,” _SIAM review_ , vol. 42, no. 1, pp. 3–39, 2000. 

   - [40] E. Hairer, S. Nørsett, and G. Wanner, _Solving Ordinary Differential Equations I: Nonstiff Problems_ , ser. Springer Series in Computational Mathematics. Springer Berlin Heidelberg, 2008. 

   - [41] M. Anitescu and F. A. Potra, “A time-stepping method for stiff multibody dynamics with contact and friction,” _International journal for numerical methods in engineering_ , vol. 55, no. 7, pp. 753–784, 2002. 

   - [42] F. A. Potra, M. Anitescu, B. Gavrea, and J. Trinkle, “A linearly implicit trapezoidal method for integrating stiff multibody dynamics with contact, joints, and friction,” _International Journal for Numerical Methods in Engineering_ , vol. 66, no. 7, pp. 1079–1124, 2006. 

   - [43] C. Duriez, F. Dubois, A. Kheddar, and C. Andriot, “Realistic haptic rendering of interacting deformable objects in virtual environments,” _IEEE transactions on visualization and computer graphics_ , vol. 12, no. 1, pp. 36–47, 2005. 

   - [44] J. BELL, L. HOWELL, and P. Colella, “An efficient second-order projection method for viscous incompressible flow,” in _10th Computational Fluid Dynamics Conference_ , 1991, p. 1560. 

   - [45] R. Featherstone, _Rigid body dynamics algorithms_ . Springer, 2008. [46] J. Nocedal and S. Wright, _Numerical optimization_ . Springer Science & Business Media, 2006. 

   - [47] W. H. Press, H. William, S. A. Teukolsky, A. Saul, W. T. Vetterling, and B. P. Flannery, _Numerical recipes 3rd edition: The art of scientific computing_ . Cambridge university press, 2007. 

   - [48] T. A. Davis, S. Rajamanickam, and W. M. Sid-Lakhdar, “A survey of direct methods for sparse linear systems,” _Acta Numerica_ , vol. 25, pp. 383–566, 2016. 

   - [49] L. Smail, “Junction trees constructions in bayesian networks,” in _Journal of Physics: Conference Series_ , vol. 893, no. 1. IOP Publishing, 2017, p. 012056. 

   - [50] F. Permenter, “A geodesic interior-point method for linear optimization over symmetric cones,” _arXiv preprint arXiv:2008.08047_ , 2020. 

   - [51] N. Kuppuswamy, A. Alspach, A. Uttamchandani, S. Creasey, T. Ikeda, and R. Tedrake, “Soft-bubble grippers for robust and perceptive manipulation,” in _2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2020, pp. 9917–9924. 

   - [52] J. Carpentier, R. Budhiraja, and N. Mansard, “Proximal and sparse resolution of constrained dynamic equations,” in _Robotics: Science and Systems 2021_ , 2021. 

   - [53] M. C. Delfour and J.-P. Zol´esio, _Shapes and geometries: metrics, analysis, differential calculus, and optimization_ . SIAM, 2011. 

- [29] A. Tasora and M. Anitescu, “A matrix-free cone complementarity approach for solving large-scale, nonsmooth, rigid body dynamics,” _Computer Methods in Applied Mechanics and Engineering_ , vol. 200, no. 5-8, pp. 439–453, 2011. 

- [30] H. Mazhar, T. Heyn, D. Negrut, and A. Tasora, “Using nesterov’s method to accelerate multibody dynamics with friction and contact,” _ACM Transactions on Graphics (TOG)_ , vol. 34, no. 3, pp. 1–14, 2015. 

- [31] T. Heyn, M. Anitescu, A. Tasora, and D. Negrut, “Using krylov subspace and spectral methods for solving complementarity problems in manybody contact dynamics simulation,” _International Journal for Numerical Methods in Engineering_ , vol. 95, no. 7, pp. 541–561, 2013. 

- [32] A. Tasora, D. Mangoni, S. Benatti, and R. Garziera, “Solving variational inequalities and cone complementarity problems in nonsmooth dynamics using the alternating direction method of multipliers,” _International_ 

