1 

# Contact Models in Robotics: a Comparative Analysis 

Quentin Le Lidec<sup>1,†</sup> , Wilson Jallet<sup>1,2</sup> , Louis Montaut<sup>1,3</sup> , Ivan Laptev<sup>1</sup> , Cordelia Schmid<sup>1</sup> , and Justin Carpentier<sup>1</sup> 

**_Abstract_ —Physics simulation is ubiquitous in robotics. Whether in model-based approaches (** **_e.g._ , trajectory optimization), or model-free algorithms (** **_e.g._ , reinforcement learning), physics simulators are a central component of modern control pipelines in robotics. Over the past decades, several robotic simulators have been developed, each with dedicated contact modeling assumptions and algorithmic solutions. In this article, we survey the main contact models and the associated numerical methods commonly used in robotics for simulating advanced robot motions involving contact interactions. In particular, we recall the physical laws underlying contacts and friction (** **_i.e._ , Signorini condition, Coulomb’s law, and the maximum dissipation principle), and how they are transcribed in current simulators. For each physics engine, we expose their inherent physical relaxations along with their limitations due to the numerical techniques employed. Based on our study, we propose theoretically grounded quantitative criteria on which we build benchmarks assessing both the physical and computational aspects of simulation. We support our work with an open-source and efficient C++ implementation of the existing algorithmic variations. Our results demonstrate that some approximations or algorithms commonly used in robotics can severely widen the reality gap and impact target applications. We hope this work will help motivate the development of new contact models, contact solvers, and robotic simulators in general, at the root of recent progress in motion generation in robotics.** 

**_Index Terms_ —Physical simulation, Numerical optimization.** 

## I. INTRODUCTION 

**S** IMULATIONalgorithms, likeis atrajectoryfundamentaloptimizationtool in robotics.(TO) orControlmodel predictive control (MPC), rely on physics simulators to evaluate the dynamics of the controlled system. Reinforcement Learning (RL) algorithms operate by trial and error and require a simulator to avoid time-consuming and costly failures on real hardware. Robot co-design aims at finding optimal hardware design and morphology, and thus extensively relies on simulation to prevent tedious physical validation. In practice, roboticists also usually perform simulated safety checks before running a new controller on their robots. These applications are evidence for a wide range of research areas in robotics where simulation is critical. 

To be effective and valuable in practice, robot simulators must meet some fidelity or efficiency levels, depending on the use case. For instance, trajectory optimization algorithms, _e.g._ , iLQR[1] or DDP [2], [3], use physics simulation to evaluate the 

> 1Inria - Département d’Informatique de l’École normale supérieure, PSL Research University. Email: firstname.lastname@inria.fr 

> 2LAAS-CNRS, 7 av. du Colonel Roche, 31400 Toulouse 

> 3Czech Institute of Informatics, Robotics and Cybernetics, Czech Technical University, Prague, Czech Republic 

> †Corresponding author 



Fig. 1. **Illustration of the dynamics of frictional contacts** between rigid bodies, which are governed by the Signorini condition, Coulomb’s law, and the maximum dissipation principle. Combining these three principles leads to the Non-linear Complementarity Problem (15). 

system dynamics and leverage finite differences or the recent advent of differentiable simulators [4], [5], [6], [7], [8] to compute derivatives. If the solution lacks precision, the real and planned trajectories may quickly diverge, impacting _de facto_ the capacity of such control solutions to be deployed on real hardware. To absorb such errors, the Model Predictive Control (MPC) [9], [10] paradigm exploits state feedback by repeatedly running Optimal Control (OC) algorithms at high-frequency rates (e.g., 1kHz) [11], [12]. The frequency rate is one factor determining the robustness of this closed-loop algorithm to modeling errors and perturbations; thus, the efficiency of the simulation becomes critical. Although RL [13] is considered a model-free approach, physical models are still at work to generate the samples that are indispensable for learning control policies. In fact, the vast number of required samples is the main bottleneck during training, as days or years of simulation, which corresponds to billions of calls to a simulator, are necessary [14], [15], [16]. Therefore, the efficiency of the simulator directly determines the computational and, thus, the energetic 

2 

cost of learning a control policy. Physical accuracy plays an important role after training as well, as more physically accurate simulations will result in a smaller reality gap to cross for the learned policy to transfer to a real robot [14]. 

Many manipulation tasks can be tackled by assuming quasistaticity and considering only a restricted variety of contact events [17], [18]. The recent robotics efforts, highlighted, for instance, by the athletic motions performed by the humanoid robots of Boston Dynamics [19], focus on very dynamic tasks for which these simplification hypotheses cannot hold. In fact, tasks like agile locomotion or dexterous manipulation require the robot to quickly plan and finely exploit, at best, the contact interactions with its environment to shape the movements [20], [21], [22]. In this respect, the ability to handle impacts and friction, physical phenomena at the core of contact interactions, becomes fundamental for robotic simulators. 

Physics simulation is often considered a solved problem with several well-known simulators that are available off the shelf. However, simulating a physical system raises several complex issues that are usually circumvented at the cost of approximations or costly computation. When simulating a system evolving freely, rigid body dynamics algorithms [23], [24] are now established as the way to go due to their high efficiency. For robotics, one has to consider interactions through contact between the robot and its environment, thus constraining the movement. However, due to the creation of the breaking of contacts along a trajectory, the dynamics switch from one mode to the other, making the problem of simulating a system with contacts and friction highly non-smooth [25], [26], [27]. Numerical integration schemes for non-smooth systems fall into two main categories: event-driven and time-stepping methods [28]. Most modern robotics simulators are part of the latter category because predicting collisions is intractable due to the complexity of the scenes. Therefore, we will restrict our study to this type of method. 

More precisely, contact dynamics between rigid objects are governed by three main principles: the Signorini condition specifies the unilaterality nature of contact interactions, while Coulomb’s law of friction and the maximum dissipation principle (MDP) of Moreau state that friction force should lie inside a second-order cone and oppose the movement. Altogether, these three principles correspond to a so-called nonlinear complementarity problem (NCP). The complementarity constraints define a non-convex set while being non-smooth, this problem is difficult to solve in general [28]. 

Historically, the Open Dynamic Engine (ODE) [29] is one of the first open-source simulators with a large impact on the community, which was then followed by Bullet [30]. Both of them, in their original version, relied on maximal coordinates to depict the state of the objects, and kinematic constraints imposed by the articulations are tackled explicitly. Such a choice leads to large-dimensional problems to solve, impacting _de facto_ the computational performances. To lower the computational burden, alternative simulators rooted in generalized coordinates, like DART [31] and MuJoCo [32], appeared shortly after. Since then, Bullet also made this choice the default one. In practice, these simulators are rarely used to tackle engineering problems but rather as physics engines for 

graphical purposes (Bullet) or research in the RL community (MuJoCo). More recently, RaiSim [33] and Drake [34] were developed as robotic-driven software. RaiSim [33] emerged as one of the first simulators enabling RL policies to transfer to real quadrupedal robots. Its implementation being closed source, we provide what constitutes, to the best of our knowledge, the first in-depth study and open-source re-implementation of this contact solver. Drake also demonstrated some promising results on challenging manipulation [35] as regards the simto-real requirements. Still today, the number of alternative algorithms available is growing fast, in an effort to improve the properties of the existing ones, in terms of accuracy and robustness [36], [37], [38], [6], [39], [35], [8]. In a parallel line of work, Isaac Gym [40] and Brax [41] simulators use elementary contact models and rather focus on exploiting the parallelization abilities from GPUs or TPUs for batch computation. 

In general, these simulators differ at their very core: one should be aware of the contact modeling embedded in the simulator they are using and how it can impact the applications they aim at. Some high-level benchmarks of simulators exist [42], evaluating the whole simulation pipeline and its multiple internal routines, _e.g._ , rigid-body dynamics algorithms, collision detection, and contact problem-solving. Our work closely relates to [43]. It separately assesses the various contact models and their associated algorithms. We achieve this by decoupling the contact models from their implementations and re-implemented the solvers with a unique back-end based on the Pinocchio toolbox [24], [44] for evaluating the dynamic quantities and on HPP-FCL [45], [46], [47] for computing the collisions. We pursue the effort of [43] by studying recent algorithms and adding advanced evaluation criteria. Our experiments are done in both illustrative and realistic robotics setups. 

We make the following contributions: 

- _�→_ we make a detailed survey of contact models and their associated algorithms, including established and more recent robotics simulators; 

- _�→_ we expose the main limitations of existing simulators by inspecting both the physical approximations and the numerical methods that are at work; 

- _�→_ we develop an open source and generic implementation of the main robotic contact solvers in C++; 

- _�→_ based on our implementation and the theoretical study, we propose quantitative criteria that allow performing an in-depth evaluation of both physical and computational aspects of contact models and solvers. 

- _�→_ we explore the impacts of the simulation choices on the practical application of MPC for quadruped locomotion. 

The article is organized as follows: we first recall the background of contact simulation: the physical principles behind contact modeling (Sec. II) and the numerical algorithms allowing us to solve the resulting equations (Sec. III). In the experimental part (Sec. IV), we propose an exhaustive empirical evaluation of the various existing contact models and solvers to assess both their physicality (Sec. IV-A), self-consistency (Sec. IV-B) and computational efficiency (Sec. IV-C). At last, 

3 

Sec. IV-D investigates the consequences of the contact models in the context of quadruped locomotion. It is finally worth mentioning that the authors are linked to the Pinocchio and HPP-FCL open-source projects. 

## II. RIGID CONTACT MODELLING 

We start by stating the physical principles commonly admitted for rigid body simulation with point contact. If these principles remain hypothetical and can still be discussed, they have been, in general, empirically tested and are arguably better than their relaxations. Once the modeling is done, we transcribe these physical laws into a numerical problem, which should be solved via optimization-based techniques to simulate a system with contacts and frictions. We also present the various opensource tools that allow computing all the intermediate quantities necessary to build a physics simulator. 

In this paper, we describe the state of a system with its generalized coordinates _q ∈Q_<sup>_∼_</sup> = R<sup>_nq_</sup> . We denote by _v ∈TqQ_ = R<sup>_nv_</sup> the joint velocity, where _TqQ_ is the tangent space of _Q_ . 

**Free motion.** The principle of least constraint [48], [49], [50] induces the celebrated equations of motion: 



where _M ∈ R_<sup>_nv×nv_</sup> represents the joint space inertia matrix of the system, _b_ ( _q, v_ ) accounts for the centrifugal and Coriolis effects, and for the generalized gravity. This Lagrangian equation of motion naturally accounts for the kinematic constraints induced by the articulations of the rigid-body dynamical system. When applied to a robot, _i.e._ , a system of multiple rigid bodies, the inertia matrix _M_ becomes sparse. Rigid body dynamic algorithms exploit this sparsity at best [23], [24] making it possible to compute the free acceleration in a few microseconds on modern CPUs for robots as complex as a 36-dof humanoid. As done by time-stepping approaches [28], we will express the problem in terms of velocities rather than accelerations, thus discretizing (1) into: 



which corresponds to a semi-implicit Euler integration scheme [51]. More advanced implicit integrators [32], [35], [8] come with stability guarantees even in the presence of stiff forces. However, as time-stepping schemes, their order of integration is inherently degraded due to the non-smoothness of the dynamics [52]. For this reason, we restrict our study to a simple scheme, as integrators are not the main focus of this work. In the following, we often drop the instant at which quantities are evaluated for readability purposes. We denote the free velocity _v_<sup>_f_</sup> , which is defined as the solution of (2). 

**Bilateral contact.** When the system is subject to constraints, _e.g._ kinematic loop closures or anchor points, it is convenient to represent them implicitly: 



where Φ : R<sup>_nq_</sup> _�→_ R<sup>_m_</sup> is a holonomic constraint function of dimension _m_ , which depends on the nature of the constraint. 



Fig. 2. **The separation vector** Φ allows formulating the non-penetration constraint, which leads to the _Signorini condition_ (8). This vector is computed by the GJK or EPA algorithms, which are internal blocks of the simulator. We refer to [56] for a tutorial introduction on the topic. 

For solving, it is more practical to proceed to an index reduction [53] by differentiating (3) w.r.t. time, in order to express it as a constraint on joint velocities: 



where _c_ = _J_ ( _q_<sup>_t_</sup> ) _v_<sup>_t_+1</sup> _∈_ R<sup>_m_</sup> is the constraint velocity, _J_ = _∂_ Φ _/∂q_ is the constraint Jacobian explicitly formed at time _t_ , which can be computed efficiently via rigid body dynamics algorithms [23], [54]; and _c_<sup>_∗_</sup> is the reference velocity which stabilizes the constraint. Such a constraint (4) is enforced by the action of the environment on the system via the contact vector impulse _λ ∈_ R<sup>_m_</sup> . These considerations lead to Gauss’s principle of least constraint [55], [48]. By duality, the contact impulses are spanned by the transpose of the constraint Jacobian and should be incorporated in the Lagrangian equations (2) via: 



Regarding bilateral contacts, the contact efforts, corresponding to the Lagrange multipliers associated with the constraint (3), are unconstrained. If a bilateral constraint is well suited to model kinematic closures, it is not to model interactions between the robot and its environment, which are better represented by unilateral contacts. This paper focuses on the latter, for which we provide a more detailed presentation. 

**Unilateral contact.** When a system is in contact with its environment, the non-penetration constraint enforces the signed distance between the two objects to be non-negative [57]. Defining the separation vector as the vector of minimum norm separating two shapes in contact [58], [56](Fig. 2), the signed distance function corresponds to its normal component. By overloading the notation of the bilateral case, the constraint function Φ now maps to the separation vector (Fig. 2) and describes a unilateral constraint: 



where Φ( _q_ ) _∈_ R<sup>3</sup><sup>_nc_</sup> , _nc_ is the number of contacts; the subscripts _N_ and _T_ respectively account for the normal and tangential components. In practice, Φ can be computed efficiently via the Gilbert-Johnson-Keerthi (GJK) [59], [47] and the Expanding Polytope Algorithm (EPA) algorithms[60]. GJK operates on convex shapes, but non-convex shapes can also be handled by proceeding to decomposition into convex sub-shapes [61] during an offline preprocessing step. To ease the solving, one 

4 

can write (6) in terms of velocities, and supposing that shapes are in contact, _i.e._ Φ( _q_<sup>_t_</sup> ) _N ≤_ 0, the Taylor expansion of the condition (6) leads to: 



where _c_ = _J_ ( _q_<sup>_t_</sup> ) _v_<sup>_t_+1</sup> _∈_ R<sup>3</sup><sup>_nc_</sup> is the velocity of contact points. It should be noted that J is evaluated at _q_<sup>_t_</sup> as it avoids computing Φ and its Jacobian several times when solving for _q_<sup>_t_+1</sup> and _v_<sup>_t_+1</sup> which significantly decreases the computational burden. We explain later how _c_<sup>_∗_</sup> _N_<sup>is set to model physical effects or improve</sup> the numerical accuracy of the solutions. As in the bilateral case, the transpose of the contact Jacobian _J_ spans the contact forces, which leads again to (5) the constrained equations of motion. Unlike the bilateral case, unilateral contacts constrain the possible contact impulses _λ_ . In a frictionless situation, the tangential forces are null, which implies that _λT_ = 0. In addition, the contact forces _λ_ can only be repulsive _i.e._ , they should not act in a glue-like fashion (the environment can only push and not pull on the feet of a legged robot) and, thus, are forced to be non-negative. An impulse cannot occur when an object takes off, _i.e._ , the normal velocity and impulse cannot be non-null simultaneously. Combining these conditions, we obtain the so called _Signorini condition_ [62] at the velocity level [25]: 



where _a ⊥ b_ for vectors _a_ and _b_ means _a_<sup>_⊤_</sup> _b_ = 0. However, such a condition does not define a mapping between _λN_ and _cN_ , _i.e._ , the contact forces are not a function of the penetration error. Indeed, their representation is an infinitely steep graph that may be relaxed into a mapping via a spring damper accounting for local deformation of the materials (see Fig. 3). Substituting, _v_<sup>_t_+1</sup> by its expression from the Lagrangian equations (5), we obtain a Linear Complementarity Problem (LCP) [63]: 



where _G_ = _JM_<sup>_−_1</sup> _J_<sup>_⊤_</sup> is the so-called Delassus matrix, and _g_ = _Jv_<sup>_f_</sup> is the free velocity of contact points (the velocity of the contact points in the unconstrained cases). It is worth mentioning at this stage that several approaches [23], [64], [54] have been developed in the computational dynamics and robotics literature to efficiently evaluate the Delassus matrix. 

In the case of rigid bodies, the reference velocity _c_<sup>_∗_</sup> _N_<sup>can</sup> Φ( _<u>q</u>_<sup>_t_</sup> <u>)</u> be set to ∆ _t_ to complete the Taylor expansion of (6). However, adding bias terms to this velocity may be useful to improve modeling on both physical and numerical aspects. A first benefit is the possibility of accounting for impacts that may occur when two objects collide with non-null relative normal velocity. The most common impact law stipulates to introduce a bias term _−ec_<sup>_t_</sup> where _e_ is the restitution coefficient, which adjusts the quantity of energy dissipated during the collision. When time-stepping methods are employed, one cannot avoid penetration errors, _i.e._ Φ( _q_ ) _N <_ 0, without using stabilization by reprojection techniques [65] which are computationally expensive to use in robotics due to the cost of detecting a collision. However, it is still possible to prevent these errors from dramatically growing over time via a Baumgarte correction [66] which adds _kB_ max(0 _, −_ Φ( _q_<sup>_t_</sup> ) _N_ ) to 



<!-- Start of picture text -->
Normal contact  Friction force (N)<br>force (N) Coulomb law<br>Signorini condition relaxed Coulomb<br>law<br>relaxed Signorini<br>condition<br>Tangent<br>velocity (m/s)<br>Distance (m)<br><!-- End of picture text -->

Fig. 3. Both the _Signorini condition_ ( **Left** ) and Coulomb’s law ( **Right** ) induce infinitely steep graphs, which make the contact problem hard to solve. 

the reference velocity _c_<sup>_∗_</sup> and where the Baumgarte coefficient _kB_ is set to be proportional to ∆1 _t_<sup>.</sup> 

In addition, in many cases in robotics, Delassus’ matrix _G_ is rank deficient. Such physical systems are said to be hyperstatic, and because rank( _J_ ) _> nv_ , several _λ_ values may lead to the same trajectory. This under-determination can be circumvented by relaxing the rigid-body hypothesis, _e.g._ the _Signorini condition_ , and considering compliant contacts via a reference velocity linearly depending on _λ_ as represented in Fig. 3. Indeed, by adding _−Rλ_ to _c_<sup>_∗_</sup> where _R_ is a diagonal matrix with non-null and positive elements only on the normal components, called compliance and whose value is a property of the material, the original Delassus matrix _G_ is replaced by the damped matrix _G_<sup>˜</sup> = _G_ + _R_ which is full rank. At this stage, one should note that the physical compliance acts on the conditioning in an equivalent way to a numerical regularization. 

**Friction phenomena** are at the core of contact modeling, as they precisely enable manipulation or locomotion tasks. Coulomb’s law for dry friction represents the most common way to model friction forces. This phenomenological law states that the maximum friction forces _∥λT ∥_ should be proportional to the normal contact forces _λN_ and the friction coefficient _µ_ . Mathematically, this suggests that contact forces should lie inside an ice cream cone whose aperture is set by the coefficient of friction _µ_ : 



where the product is Cartesian, the superscript ( _i_ ) refers to the i<sup>_th_</sup> contact point and _Kµ_ ( _i_ ) = � _λ|λ ∈_ R<sup>3</sup> _, λN ≥_ 0 _, ∥λT ∥_ 2 _≤ µ_<sup>(</sup><sup>_i_)</sup> _λN_ �. Additionally, when sliding occurs, the maximum dissipation principle formulated by Jean-Jacques Moreau [25] implies that the frictional forces should maximize the dissipated power: 



whose optimality conditions yield the following equation in the sliding case: 



As for the _Signorini condition_ , Coulomb’s law does not describe a mapping but an infinitely steep graph (Fig. 3). Relaxing this law via viscous frictions, _i.e._ , assuming the 

5 

tangent contact forces to be proportional to the tangent velocities, allows defining a mapping between _λT_ and _cT_ . 

**The Non-linear Complementarity Problem.** Combining the Coulomb’s law for friction with the _Signorini condition_ evoked earlier, we finally get three distinct cases corresponding to a sticking contact point (13a), a sliding contact point (13c) or a take-off (13b): 



where _∂K_ indicates the boundary of the cone. The equations (13) are referred to as the disjunctive formulation of the contact problem. However, such a formulation is unsuitable in practice for solving, as the switching condition depends on the contact point velocity _c_ . As this quantity is an unknown of the problem, one cannot know in which case of (13) one is standing. For this reason, the problem is often reformulated as a nonlinear complementarity problem (NCP). Indeed, using de Saxcé’s bipotential function [67] defined as: 



one can show that (13) is equivalent to the following [27], [68] (Fig. 1): 



In (15), _Kµ_<sup>_∗_refers to the dual cone of</sup><sup>_Kµ_, such that if</sup><sup>_λ ∈Kµ_</sup> and _c ∈ Kµ_<sup>_∗_,then</sup><sup>_⟨λ, c⟩≥_0,where</sup><sup>_⟨·, ·⟩_isthecanonical</sup> scalar product. It is worth noting that the relation _Kµ_<sup>_∗_=</sup><sup>_K_</sup> 1 _/µ_ stands for second-order cones. Eq. (15) allows defining, for each contact _i ∈_ �1 _, nc_ �, the primal and dual residuals as _ϵ_<sup>(</sup> p<sup>_i_)</sup> = dist _Kµ_ ( _i_ ) � _λ_<sup>(</sup><sup>_i_)�</sup> and _ϵ_<sup>(</sup> d<sup>_i_)</sup> = dist _K_<sup>_∗_</sup> � _c_<sup>(</sup><sup>_i_)</sup> + Γ � _c_<sup>(</sup><sup>_i_)</sup> _, µ_<sup>(</sup><sup>_i_)��</sup> respectively, where _µ_<sup>(</sup><sup>_i_)</sup> dist _C_ is the distance function w.r.t. a convex set _C_ . It also induces a contact complementarity criterion _ϵ_<sup>(</sup> c<sup>_i_)</sup> = �� _⟨λ_ ( _i_ ) _, c_ ( _i_ ) + Γ � _c_<sup>(</sup><sup>_i_)</sup> _, µ_<sup>(</sup><sup>_i_)�</sup> _⟩_ ��. From these per-contact criteria, it is then possible to introduce a well-posed absolute convergence criterion _ϵ_ abs for (15), as the maximum of _ϵ_<sup>(</sup> p<sup>_i_),</sup><sup>_ϵ_(</sup> d<sup>_i_)</sup> and _ϵ_<sup>(</sup> c<sup>_i_)</sup> for all _i_ . We use this criterion as a stopping criterion in our implementation of NCP solvers, but also as a measure of physical accuracy in our experiments of Section IV. All the previous derivations were made with _λ_ being an impulse which causes it, and thus the criteria _ϵ_ p _,_ c, to be proportional to the time step ∆ _t_ . However, it is preferable from the user-side to have _ϵ_ c and _ϵ_ p not correlated to ∆ _t_ so the precision threshold of the simulation _ϵ_ abs can be set independently of the time-step. In practice, before solving we operate a change of variable to directly work on the equivalent contact forces ∆ _<u>λt</u>_<sup>.Thisisdone</sup> by replacing _g_ and _c_<sup>_∗_</sup> by their scaled counterpart ∆ _<u>gt</u>_<sup>and</sup> ∆ _<u>c</u>_<sup>_∗_</sup> _t_ in the formulation of (15). For readability purposes, equations are still written in impulse in what follows. 

At this point, it is worth mentioning that the problem (15), which we refer to as NCP, does not derive from a convex optimization problem, thus making its solving complex. 



<!-- Start of picture text -->
-mg -mg<br>𝝺 (1) 𝝺 (2) 𝝺 (1) 𝝺 (2)<br><!-- End of picture text -->

Fig. 4. **Underdetermined contact problem.** The left and right contact forces are solutions of the NCP (15) and lead to the same system velocity. Such an undetermined problem can also occur on normal forces. 

Alternatively, one can see the frictional contact problem as two interleaved convex optimization problems [69], [70], [36], [71], [6] whose unknowns, _λ_ and _v_ , appear in both. Other formulations exist and we refer to [68] for a more complete review on the NCP. Practically, the non-convexity can induce the existence of multiple, or even an infinite number of contact forces satisfying (15). As mentioned earlier, this can be due to normal forces, but tangential components can also cause underdetermination (Fig. 4). In this situation, it would be preferable for a simulator to provide the minimum norm solution in forces. This property can prevent a simulator from exhibiting internal friction forces compressing or stretching the objects (Fig. 4, right). Indeed, such forces may not coincide with the forces observed by force sensors and would rather correspond to some internal deformations of the objects, which should thus be considered soft and no more rigid. In the following, we will use the term “internal forces” to denote the force component deviating from the minimum norm solution. Additionally, these internal forces might also be problematic as it is difficult to characterize them. This may induce inconsistent derivatives, which become critical in the context of differentiable simulation. 

**Open-source frameworks for contact simulation.** To conclude this section, we propose to review the open-source software that is popular in the robotics community and that can be used for simulating contact. Simulating contact interactions, as illustrated in Fig. 5, involves two main stages, corresponding to the collision detection step (which objects are in contact) and the collision resolution (which contact forces are applied through the contact interaction). These frameworks are enumerated in Tab. I. 

More precisely, at each time step, a simulator must first detect which geometries are colliding and compute their separation vector Φ. The GJK and EPA algorithms are widely adopted for their low computational cost. HPP-FCL [45], [46], [47], an extension of the Flexible Collision Library (FCL) [72] and libccd [73] implement them efficiently. Some simulators such as Bullet [30], ODE [29] or PhysX [74] also re-implement the same algorithm as an internal routine. 

Once collisions are evaluated, one still requires the contact points free velocity _vf_ and Jacobians _J_ to formulate (15). These two quantities are efficiently computed via rigid body algorithms [23]. The RBDL [75] or the Pinocchio library [24] provide efficient implementations to evaluate them. In addition, 

6 



Fig. 5. **Simulation routines.** When simulating rigid bodies with frictional contacts, a physics engine goes through a sequence of potentially challenging sub-problems: collision detection, contact forces computation, and integration time step. 

TABLE I 

OPEN SOURCE TOOLS FOR PHYSICS SIMULATION IN ROBOTICS. 

||License|API|Used by|
|---|---|---|---|
|FCL [72]|**Collisi**<br>BSD|**on detection**<br>C++|DART, Drake<br>|
|libccd [73]|BSD|C++, Python|MuJoCo, Drake,<br>FCL, Bullet, ODE|
|HPP-FCL [45]|BSD|C++, Python|Pinocchio|
|Bullet [30]|BSD|C++, Python|DART|
|ODE [29]|BSD/GPL|C++, Python|DART|
|PhysX [74]|BSD 3|C++, Python||
|**Rig**|**id body d**|**ynamics algor**|**ithms**|
|Pinocchio [24]|BSD|C++, Python||
|RBDL [75]|zlib|C++, Python||
|Drake [34]|BSD3|C++, Python||
||**Forces **|**computation**||
|MuJoCo [32]|Apache 2.0|C++, Python||
|DART [31]|BSD 2|C++, Python||
|Bullet [30]|BSD|C++, Python||
|Drake [34]|BSD 3|C++, Python||
|ODE [34]|BSD/GPL|C++, Python||
|PhysX [74]|BSD 3|C++, Python||



Pinocchio proposes a direct and robust way to compute the Cholesky decomposition of the Delassus matrix G [54]. These algorithms are also embedded as internal routines in various simulators such as MuJoCo [32], DART [31], Drake [34], Bullet [30] or ODE [29], but they often are only partially exposed to the user. 

Eventually, when all quantities necessary to formulate the NCP (15) are computed, the simulator has to call a solver. Every simulator, _i.e._ MuJoCo [32], DART [31], Bullet [30], Drake [34] and ODE [29], proposes its own implementation. This procedure varies greatly depending on the physics engine, as each has its own physical and numerical choices. In the next section, we detail the existing algorithms. 

## III. ALGORITHMIC VARIATIONS OF THE CONTACT PROBLEM 

As explained in the previous section, the nonlinear complementarity problem (15) does not derive from a variational principle but can be formulated as variational inequalities [68]. Thus, classical numerical optimization solvers cannot be used straightforwardly to solve it. This section studies 

TABLE II 

CHARACTERISTICS OF VARIOUS CONTACT MODELS. 

||Signorini|Coulomb|MDP|
|---|---|---|---|
|**LCP**|✓|||
|**CCP**||✓|✓|
|**RaiSim** [33]|✓|✓||
|**NCP**|✓|✓|✓|



the various approximations and algorithmic techniques in the literature to tackle this problem. As summarized in Tab. III, this section is organized into subsections describing the four contact models most commonly used in robotics, namely the linear complementarity problem (LCP), the cone complementary problem (CCP), RaiSim, and the nonlinear complementarity problem (NCP). For each contact model, we also report the related algorithmic variants. If each tick in Tab. III represents a positive point for the concerned algorithm, Sec. IV shows that even one missing tick may be prohibitive and can cause a solver to be unusable in practice. Finally, we also mention a set of useful implementation tricks that can be used to build an efficient simulator. 

## _A. Linear Complementarity Problem_ 

A first way to simplify the solving of problem (15) is to linearize the NCP problem by approximating the second-order cone constraint from Coulomb’s law with a pyramid, typically composed of four facets. This is done by replacing _Kµ_ ( _i_ ) by _K_<sup>˜</sup> _µ_ ( _i_ ) = � _λ|λN ≥_ 0 _, ∥λT ∥∞ ≤ µ_<sup>(</sup><sup>_i_)</sup> _λN_ �. Doing so allows retrieving a linear complementarity problem (LCP), often easier to solve [63]. Such a problem is more standard and betterstudied than its nonlinear counterpart as it already has a long history of applications to frictional contacts [77], [78], [79], [80]. 

**Direct methods** for LCP date back to the 1960s and are available options in well-known simulators such as ODE [29] and Bullet [30] which implement respectively the Lemke’s [81] and Dantzig’s [82] algorithms. Under specific circumstances [83], the algorithm is guaranteed to find a solution. 

**Projected Gauss-Seidel.** Due to its easy implementation and the possibility to early-stop it, the projected Gauss-Seidel (PGS) algorithm (Alg. 1) algorithm represents an attractive alternative and was widely adopted as the default solver by many physics engines, such as in Bullet [30], PhysX [74], ODE [29], and DART [31], [7] simulators. This iterative algorithm loops on contact points and successively updates the normal and tangent contact forces. Because PGS works separately on each contact point, the update compensates for the current errors due to the estimated forces from other contact points. Yet, as illustrated in the experimental section IV, this process induces the emergence of internal forces during the solving. Moreover, Gauss-Seidelbased approaches are similar to what is also known as block coordinate descent in the optimization literature. As first-order algorithms, they do not benefit from improved convergence 

7 

TABLE III 

CHARACTERISTICS OF NUMERICAL ALGORITHMS. 



<!-- Start of picture text -->
Hard contacts No internal forces Robust Convergence guarantees<br>LCP<br>PGS [30], [29], [74], [31] ✓<br>Staggered projections [36] ✓ ✓ ✓<br>CCP<br>PGS [76] ✓ ✓<br>MuJoCo [32] ✓ ✓ ✓<br>ADMM (Alg. 3) ✓ ✓ ✓ ✓<br>Drake [35] ✓ ✓ ✓<br>RaiSim [33] ✓<br>NCP<br>PGS ✓<br>Staggered projections [6] ✓ ✓ ✓<br><!-- End of picture text -->

**Algorithm 1:** Pseudocode of the projected Gauss-Seidel (PGS) algorithm for solving LCPs. 



<!-- Start of picture text -->
Input: Delassus matrix: G , free velocity: g , friction<br>cones: Kµ<br>Output: Contact forces: λ<br>1 for k = 1 to niter do<br>2 for i  = 1 to nc do<br>1<br>3 λ ( N i ) ← λ ( N i ) − GNN ( ii ) ( Gλ  +  g ) N ( i );<br>4 λ ( N i ) ← max(0 , λ ( N i ));<br>1<br>5 λ ( T i ) ← λ ( T i ) − min( GTxTx ( ii ) ,G TyTy ( ii ) ) ( Gλ  +  g ) T ( i );<br>6 λ ( T i ) ← clamp( λ T ( i ) , µiλN );<br>7 end<br>8 end<br><!-- End of picture text -->



Fig. 6. **Cone linear approximation.** Linearizing the friction cone induces a bias in the direction of friction forces. The MDP tends to push tangential forces toward the corners of the pyramid. 

rates or robustness with respect to their conditioning, unlike second-order algorithms. 

In parallel, the linearization of the second-order cone causes the loss of the isotropy for friction, as stated by Coulomb’s law. By choosing the axes for the facets of the pyramid and due to the maximum dissipation principle, it is established that one incidentally biases the friction forces towards the corners [84], [85], as illustrated in Fig. 6. This error is sometimes mitigated by increasing the number of facets, which also comes at the cost of more computations. 

## _B. Cone Complementarity Problem._ 

An alternative approach consists of approximating the NCP problem in order to transform it into a more classical convex optimization problem. By relaxing the complementarity constraint from (15), one can obtain a Cone Complementarity Problem (CCP) [86]: 



If this relaxation preserves the Maximum Dissipation Principle (MDP) and the second-order friction cone, it loses the _Signorini_ 

_condition_ (8). Indeed, re-writing the complementarity of (16) yields: 



and if the i<sup>th</sup> contact point is sliding, the MDP (12) leads to: 



which is equivalent to the following complementarity condition: 



(19) indicates that the CCP approximation allows for simultaneous normal velocity and forces, contrary to (8). In practice, this results in objects interacting at distance when contact points are sliding. In its seminal work [86], Anitescu shows the interaction distance to be ∆ _tµ∥c_<sup>(</sup> _T_<sup>_i_)</sup><sup>_∥_.Itisworthinsisting</sup> on the fact that such an artifact only emerges in the case of a sliding contact and can be mitigated, and even controlled, with smaller time steps and sliding velocities. Moreover, it is still under debate to determine if this behavior is prohibitive for robotics applications. 

Because CCP (16) approximates the NCP (15), the convergence is checked via a different criterion. In fact, in the same way, the De Saxcé correction was ignored in (16), a convergence criterion is obtained by removing this term 

8 

**Algorithm 2:** Projected Gauss-Seidel (PGS) algorithm for the dual Cone Complementarity Problem (CCP) 

**Input:** Delassus matrix: _G_ , free velocity: _g_ , friction cones: _Kµ_ 



from the dual convergence criterion _ϵ_ d of the NCP introduced previously. 

**PGS.** The PGS algorithm can be directly adapted to handle the CCP problem [76] (Alg. 2) but inherits from the first-order convergence rates ([76] exhibits in the order of hundreds of iterations to converge in general). In the light of what follows, the algorithm even becomes equivalent to a projected gradient descent which is a classical constrained optimization technique. 

**Optimization on the dual.** The problem (16) can, in fact, be viewed as the Karush-Kuhn-Tucker conditions of an equivalent Quadratically Constrained Quadratic Programming (QCQP) problem: 



Once the contact problem is formulated as an optimization problem, any optimization algorithms can be employed to solve it and classical optimization theory provides convergence guarantees. Here, we propose to study an ADMM algorithm [87], an advanced first-order algorithm known to be efficient to reach mild accuracy and which can stall when further improving the solution. As pointed out in [32], Interior Point algorithms [88] could also be used to reach higher precision solutions even though we do not find them in any of the robotics simulators here mentioned. A benefit of using the family of proximal algorithms like ADMM is their natural ability to handle the numerical issues coming from ill-conditioned and hyper-static cases [89], [90]. This property makes it possible to accurately simulate hard contacts, _i.e._ , without any shift due to compliance _R_ = 0, and is reported in Tab. III by the "hard contacts" column. Another by-product of such methods is the implicit regularization they induce on the found solution, which removes the potential internal forces. This last property is an empirical observation resulting from the experimental section IV and, to our knowledge, has not yet been proven by the literature of proximal optimization. Therefore, it remains to be confirmed by subsequent work. 

One may argue that such algorithms require to compute _G_<sup>_−_1</sup> (Alg. 3, line 3) while per contact approaches repeatedly solve for each contact point individually, and thus only require the cheap inverse of diagonal blocks from _G_ (Alg. 1, lines 3,5, Alg. 2, line 3, Alg. 5, line 4, Alg. 6, lines 3,5). However, the 

**Algorithm 3:** ADMM algorithm for the dual Cone Complementarity Problem (CCP) 

**Input:** Delassus matrix: _G_ , free velocity: _g_ , friction 

cones: _Kµ_ 

**Output:** Contact forces: _λ_ 





recent progress [54] demonstrated the Cholesky decomposition of _G_ can be computed efficiently and robustly. We detail this point later when discussing implementation tricks, at the end of this section. Exploiting the knowledge of _G_<sup>_−_1</sup> and not the block components as in the "per-contact" approaches mentioned earlier allows us to capture the coupling between all contact points. 

**Optimization on the primal.** By reverse engineering, it is possible to form an optimization problem on joint velocities _v_ whose dual would be (20). This approach is adopted in both MuJoCo[32] and Drake[35] and results in the following optimization problem: 



where _∥x∥X_ = _√x_<sup>_⊤_</sup> _Xx_ with _X ≻_ 0. Working on the equations, this problem can be formulated as an unconstrained optimization problem: 



where _PK_<sup>_R_</sup> _µ_<sup>(</sup><sup>_y_)=arg min</sup> _γ∈Kµ_<sup>_∥γ −y∥_</sup> _R_<sup>2;</sup><sup>_y_(</sup><sup>_c_)=</sup><sup>_−R−_1(</sup><sup>_c −_</sup> _c_<sup>_∗_</sup> ); and which is viable only when _R_ is non-null. The latter condition makes it impossible to model hard contacts. As evoked earlier, this is equivalent to replacing _G_ by _G_<sup>˜</sup> = _G_ + _R_ in the quadratic part of (20), which is justified by a compliant contact hypothesis. Indeed, _R_ corresponds to a compliance, which should be a material property of the objects involved in the collision. However, MuJoCo arbitrarily sets this to the diagonal of _αG_ , where _α ∈_ [0 _,_ 1] is close to 0. This choice has no physical justification (at least, without making strong assumptions that are not met in practice), and its only intent is to improve the conditioning of the problem to ease the solving and artificially make the solution unique. Moreover, _R_ has nonnull tangential components and thus may also introduce some tangential "compliance" which corresponds to the relaxation of Coulomb’s law (Fig. 3). In fact, this should instead be interpreted as a Tikhonov regularization term enforcing the strict convexity of the problem to facilitate the numerics and the existence of both the forward and inverse dynamics computation at the cost of shifting, even more, the solution. Drake’s algorithm [35] improves this point by providing a more physical way of setting _R_ . 

9 

**Algorithm 4:** Newton algorithm for the primal Cone Complementarity Problem (CCP) 

**Input:** Inertia matrix: _M_ , Jacobian of contacts: _J_ , compliance: _R_ , free velocity: _v_<sup>_f_</sup> , friction cones: _Kµ_ 

**Output:** Joint velocity: _v_ 

**1 for** _k_ = 1 **to** _niter_ **do** 

**2** _∇vlp ← M_ ( _v − v_<sup>_f_</sup> ) _− J_<sup>_⊤_</sup> _PK_<sup>_R_</sup> _µ_<sup>(</sup><sup>_y_(</sup><sup>_Jv_));</sup> **3** _H ← M_ + _J_<sup>_⊤_</sup> _∇vPK_<sup>_R_</sup> _µ_<sup>(</sup><sup>_y_(</sup><sup>_Jv_))</sup><sup>_J_;</sup> **4** ∆ _v ←−H_<sup>_−_1</sup> _∇vlp_ ; **5** _α ←_ arg min _β lp_ ( _v_ + _β_ ∆ _v_ ) ; **6** _v ← v_ + _α_ ∆ _v_ ; 

**7 end** 

Both Drake and MuJoCo use a Newton solver to tackle (22) (Alg. 4). Due to the non-linearity of the second term of (22), this approach requires updating the inverse of the Hessian at every iteration (Alg. 4,line 3). As proposed in [35], the use of advanced algebra routines allows to reduce the computational burden of each step. In this work, we provide an implementation of the Newton algorithm with an Armijo backtracking line search (using parameters from [35]). MuJoCo and Drake additionally implement an exact line search which improves performance and this difference should be kept in mind when interpreting the results obtained with our implementation. 

## _C. Raisim contact model_ 

A contact model introduced in [91] and implemented in the RaiSim simulator [33] aims at partially correcting the drawbacks from the CCP contact model exploited in MuJoCo [32] and Drake [34]. As explained earlier, the CCP formulation relaxes the Signorini condition for sliding contacts, leading to positive power from normal contact forces. The contact model proposed in [91] fixes this by explicitly enforcing the Signorini condition by constraining _λ_<sup>(</sup><sup>_i_)</sup> to remain in the null normal velocity hyper-plane _VN_<sup>(</sup><sup>_i_)</sup> = _{λ|GN_<sup>(</sup><sup>_ii_)</sup><sup>_λ_+ ˜</sup><sup>_g_</sup> _N_<sup>(</sup><sup>_i_)= 0</sup><sup>_}_</sup> where _g_ ˜<sup>(</sup><sup>_i_)</sup> = _g_<sup>(</sup><sup>_i_)</sup> +<sup>�</sup> _j̸_ = _i_<sup>_G_(</sup><sup>_ij_)</sup><sup>_λ_(</sup><sup>_j_)istheithcontactpoint</sup> velocity as if it were free. Here, we generalize the use of the subscript and the superscript introduced previously to matrices, where a second superscript (or subscript) corresponds to a slicing operation on the columns _e.g. G_<sup>(</sup><sup>_ij_)</sup> _∈_ R<sup>3</sup><sup>_×_3</sup> denotes the sub-block of _G_ whose rows are associated to the i<sup>th</sup> contact and columns to the j<sup>th</sup> contact. For a sliding contact point, the problem (20) becomes: 



The new problem (23) remains a QCQP and [33] leverages the analytical formula of the ellipse _Kµ_ ( _i_ ) _∩ VN_<sup>(</sup><sup>_i_)</sup> in polar coordinates to tackle it as a 1D problem via the bisection algorithm [92] (Alg. 5, line 10). We refer to the original publication for a more detailed description of the bisection routine [33]. 

This approach implies several drawbacks. Indeed, it requires knowing whether a contact point is sliding, which cannot be 



Fig. 7. **Bisection algorithm.** When the contact point is sliding, _λ_<sup>(</sup> _v_<sup>_i_</sup> 0<sup>)(Alg.5,</sup> line 4) lies outside the friction cone _Kµ_ ( _i_ ) , leading to a non-null tangential contact velocity _c_<sup>(</sup><sup>_i_)</sup> . In this case, RaiSim solves (23). This is equivalent to finding the _λ ∈ Kµ_ ( _i_ ) _∩ VN_<sup>(</sup><sup>_i_)</sup> which is the closest to _λ_<sup>(</sup> _v_<sup>_i_</sup> 0<sup>)underthemetric</sup> defined by _G_<sup>(</sup><sup>_ii_)</sup> . The constraint set being an ellipse, the problem boils down to a 1D problem on _θ_ using polar coordinates. This figure is inspired from Fig. 2 of [33]. 

known in advance as the contact point velocity depends on the contact forces. Thus, some heuristics, based on the disjunctive formulation of the contact problem (13), are introduced to try to guess the type of contact which will occur, _i.e._ take-off (Alg. 5, line 5), sticking (Alg. 5, line 7) or sliding (Alg. 5, line 9). Such heuristics may be wrong, which may cause the algorithms to get stuck and lose convergence guarantees. This effect is strengthened by the caveats of the per-contact loop, which additionally make RaiSim not robust to conditioning and prone to internal forces. Eventually, if adding the constraint _λ_<sup>(</sup><sup>_i_)</sup> _∈ VN_<sup>(</sup><sup>_i_)</sup> allows retrieving the Signorini condition from the CCP model, it also induces the loss of the maximum dissipation principle. Writing the Karush Kuhn Tucker (KKT) conditions of the problem (23) and some algebra manipulations yields: 



which contradicts (12). 

The problem solved by RaiSim depends on the contact mode, _e.g._ (23) is solved only for a sliding contact and would require the computation of the unknown dual variable. Therefore, it is more complex to define a proper convergence criterion than in previous cases (15) and (16). In this respect, either a fixpoint criterion _i.e_ the distance between two consecutive iterates, or the previously defined NCP criterion (15) can be used to coarsely monitor convergence. We chose the latest in order to have a criterion homogeneous to the ones used for (15) and (16). 

## _D. Tackling the NCP_ 

Despite the non-smooth and non-convex issues described previously, some simulation algorithms aim to directly solve the original NCP problem [79], [68], [37], [8]. **PGS.** The PGS algorithm exploited for LCP and CCP problems 

10 

## **Algorithm 5:** Per-contact bisection algorithm 

**Algorithm 7:** Staggered <u>projections</u> algorithm 

**Input:** Delassus matrix: _G_ , free velocity: _g_ , friction **Input:** Delassus matrix: _G_ , free velocity: _g_ , friction cones: _Kµ_ cones: _Kµ_ **Output:** Contact forces: _λ_ , velocity: _v_ **Output:** Contact forces: _λ_ , velocity: _v_ **1 for** _k_ = 1 **to** _niter_ **do 1 for** _k_ = 1 **to** _niter_ **do 2 for** _i_ = 1 **to** _nc_ **do 2** _g_ ˜ _N ← gT_ + _GNT λT_ ; <u>1</u> **34** _gλ_ ˜<sup>((</sup> _v_<sup>_ii_</sup> 0<sup>))</sup> _←_<sup>_←−_</sup> _g_<sup>(</sup><sup>_iG_)(</sup> +<sup>_ii_)�</sup><sup>_−_1</sup> _j_<sup>_g_˜</sup> _̸_ =<sup>(</sup> _i_<sup>_i_)</sup><sup>_G_;(</sup><sup>_ij_)</sup><sup>_λ_(</sup><sup>_j_);</sup> **34** _λg_ ˜ _TN ←←g_ arg min _T_ + _GT Nλ≥λ_ 0 _N_ 2;<sup>_λ⊤GNλ_+</sup> _g_<sup>˜</sup> _N ⊤λ_ ; <u>1</u> **5 if** _g_ ˜ _N_<sup>(</sup><sup>_i_)</sup><sup>_>_0</sup><sup>**then**</sup> **5** _λT ←_ arg min _∥λ_ ( _i_ ) _∥≤µiλ_ ( _Ni_ ) 2<sup>_λ⊤GT λ_+</sup> _g_<sup>˜</sup> _T ⊤λ_ ; // takeoff **6 end 6** _λ_<sup>_∗_</sup> _←_ 0; **7 else if** _λ_<sup>(</sup><sup>_i_)</sup> _v_ 0<sup>_∈K_</sup> _µ_<sup>(</sup><sup>_i_)</sup><sup>**then**</sup> // stiction of the time in a few iterations (typically five iterations **8** _λ_<sup>_∗_</sup> _← λ_<sup>(</sup> _v_<sup>_i_</sup> 0<sup>);</sup> Solving a cascade of optimization problems allows **9 else** of robust optimization algorithms ( _e.g._ , ADMM), but // sliding more costly than other approaches. **10** _λ_<sup>_∗_</sup> _←_ bisection( _G_<sup>(</sup><sup>_ii_)</sup> _,_ ˜ _g_<sup>(</sup><sup>_i_)</sup> _, Kµ_ ( _i_ ) _, λv_<sup>(</sup><sup>_i_</sup> 0<sup>));</sup> **11 end 12** _λ_<sup>(</sup><sup>_i_)</sup> _←_ (1 _− α_ ) _λ_<sup>(</sup><sup>_i_)</sup> + _αλ_<sup>_∗_</sup> ; _E. Implementation details_ **13** _α ← γα_ + (1 _− γ_ ) _αmin_ ; In practice, the performances of contact solvers **14 end** improved by a few simple tricks. **15 end** 

of the time in a few iterations (typically five iterations [6]). Solving a cascade of optimization problems allows the use of robust optimization algorithms ( _e.g._ , ADMM), but remains more costly than other approaches. 

In practice, the performances of contact solvers can be improved by a few simple tricks. 

**Warm-starting** the solver by providing the contact forces from the previous time step allows to greatly reduce the required computation. Indeed, in the case of a persisting contact between two objects, the contact forces are being cached and reused as an initial guess when solving for the contact forces of the next time step. This relies on the ability of the contact solver algorithm to be warm-started. This excludes Interior Point [88] algorithms, as they would only benefit from an initial guess close to the so-called central path [89]. By contrast, the feasible set of contact forces may change from one time step to the other, even in the case of a persisting contact point. On the opposite, ADMM and, more generally, Augmented Lagrangian (AL) methods can naturally be warm started: not only the primal ( _i.e._ , contact velocities) and dual ( _i.e._ , contact forces) variables, but also the proximal parameter is initialized with the previous values. 



**Cholesky computation.** In addition, second-order algorithms can further exploit the recent progress in rigid body algorithms [54]. This work takes advantage of the sparse structure of the kinematic chains in order to efficiently compute the Cholesky decomposition of the Delassus matrix _G_ . This approach is robust enough to handle the case of hyperstatic systems and reduces the cost of the computation of matrix-vector products involving _G_<sup>_−_1</sup> (Alg. 3, line 3). This also indicates that evaluating _G_ from its Cholesky decomposition, as required by per-contact approaches, actually constitutes an additional cost. 

can easily be adapted to the NCP case by changing the clamping step (Alg. 1,line 6) or the normal projection (Alg. 2, line 4) for a horizontal projection on the cone (Alg. 6, line 6). However, it is worth noting that such approaches have fewer convergence guarantees than their relaxed counterpart [27]. As with every Gauss-Seidel approach, the methods inherited from the sensitivity to ill-conditioning and jamming internal forces. 

**Staggered-projections.** The staggered projections (Alg. 7) approach, appearing in [69], [70] and implemented in a simulator in [36], [6], proceeds by rewriting the NCP as two interleaved optimization problems. This interconnection is solved via a fix-point algorithm that repeatedly injects one problem’s solution into the formulation of the other. The staggered projection algorithm has no convergence guarantees but was heavily tested and seems, in practice, to converge most 

**Proximal parameter adaptation.** In the context of ADMM (Alg. 3), the algorithm from [54] can also be favorably combined with the adaptation of the proximal parameter. Indeed, updating the regularized Cholesky can be done at almost no cost by using [54]. In our implementation, we follow the work from [93] to detect when and how _ρ_ should be adapted. More 

11 







Fig. 8. **Robotics systems used for the experiments** . The Solo-12 quadruped ( **Left** ), the Talos humanoid ( **Center** ), and the Allegro hand ( **Right** ) allow to respectively exhibit locomotion, high-dimensional, and manipulation contact scenario. 

precisely, whenever the primal residual is significantly greater than the dual one (a threshold for the ratio has to be set, a typical value being 10), _ρ_ should be increased in order to better enforce the constraint of the problem and thus, reduce the primal residual. The proximal parameter _ρ_ is then updated via a spectral rule which multiplies it by _κ_<sup>0</sup><sup>_._05</sup> , _κ_ being the condition number of the Delassus matrix, defined as the ratio between the largest and the smallest eigenvalues. Conversely, whenever the dual residual dominates the primal one, _ρ_ should be decreased by dividing it with the same factor. The condition number _κ_ can be efficiently evaluated beforehand via a power-iteration algorithm whose iterates have a computational cost equivalent to the ones from the ADMM algorithm. This procedure is detailed and evaluated in [93]. Alternatively, we could use a linear update rule for _ρ_ as it is done in OSQP [94] which would be less efficient in the case of ill-conditioned problems. 

**Over-relaxation.** Additionally, over-relaxation is often employed to accelerate the convergence of both Gauss-Seidel and ADMM algorithms. This technique applies the following update: 



where _α ∈_ ]0 _,_ 2[ and _λ_<sup>_−_</sup> denotes the previous iteration. For _α >_ 1, over-relaxing consists of an extrapolation step and should be carefully used, as it may also hinder convergence. Typically, setting _α_ to 0 _._ 8 improved convergence of the PGS algorithm. 

Several factors may hinder the correctness and accuracy of simulators based on time-stepping methods: 

- i) the low accuracy of the solver of the contact problem; 

- ii) the limitation from the contact model itself; 

- iii) or the numerical integration due to the time discretization scheme. 

In this section, we first evaluate the error from sources i) and ii) (Sec. IV-A). The source of error i) is evaluated by measuring the time taken to reach a given accuracy. The errors from ii) are analyzed by measuring the residual for an (approximately) infinite time budget. We further assess i) and iii) by examining the sensitivity of the contact solvers with respect to respectively the stopping criterion value _ϵ_ abs and the time-step ∆ _t_ (Sec. IV-B). Sec. IV-C evaluates their computational efficiency. Finally, Sec. IV-D explores how the contact models and their implementations can impact the final robotics applications, in the case of the MPC for quadruped locomotion. 

Except where expressly indicated, we use the following values for the solvers’ parameters: an absolute convergence criterion _ϵabs_ = 10<sup>_−_6</sup> , a maximum number of iteration _niter_ = 10<sup>4</sup> and a time-step ∆ _t_ = 1 _ms_ . For the ADMM algorithm, the proximal parameter _ρ_ is adapted dynamically as previously detailed (Sec. III-E). 

## _A. Evaluation of physical correctness_ 

## IV. EXPERIMENTS 

In this section, we evaluate the performances and behaviors of the formulations explained in Sec. III. To fairly compare and benchmark the various algorithmic formulations, we have implemented them in a unified C++ framework called ContactBench. In the following, we denote by RaiSim and Drake our re-implementation of the contact solvers described in the corresponding papers [33], [35]. For Drake, it is worth noting that our implementation uses a backtracking line-search with an Armijo condition instead of the line-search proposed in the original paper [35]. Our framework extensively relies on the Pinocchio library [24] for rigid body algorithms and HPP-FCL [45], [56] implementation of GJK and EPA for collision detection. Our code is made open-source in the Contactbench C++ library (https://github.com/Simple-Robotics/contactbench). 

**LCP relaxation.** The linearization of the friction cone loses the isotropy and biases the friction forces towards some specific directions, as shown in Fig. 6. This observation has already been raised in the literature [84], [95], [85], [6], [8]. As expected, the bias on the contact forces significantly impairs the simulation by deviating the trajectory of the simulated system (Fig. 9). 

**CCP relaxation.** As detailed previously, the CCP contact model relaxes the _Signorini condition_ . As shown in Fig. 10, this results in non-null normal contact forces and velocities when a contact point is sliding. As a consequence, the contact points start to bounce, which modifies the trajectory of the system (Fig. 10, left), which also impacts the overall dissipated energy (Fig. 10, right). The model adopted by Raisim aims at correcting this undesired phenomenon by enforcing the 

12 



<!-- Start of picture text -->
0.14 LCP/PGS<br>NCP/PGS<br>0.12 Analytical<br>0.10<br>v0 g 0.080.06<br>0.04<br>0.02<br>z y 0.00<br>1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6<br>x x coordinate (m)<br>Fig. 9. Trajectory of a cube sliding on a plane. The cube is initialized<br>with an initial tangential velocity along the x-axis. Right: The bias of friction<br>forces (Fig.6) introduces a tangential velocity along the y-axis, which deviates<br>the cube from the expected straight-line trajectory.<br>0.012 CCP/PGS 0.5 CCP/PGS<br>NCP/PGS NCP/PGS<br>0.010 0.4 RaiSim<br>0.008 0.3 Analytical<br>0.006<br>0.2<br>0.004<br>0.002 0.1<br>0.000 0.0<br>0.0 0.1 0.2 0.3 0.4 0.5 0.0 0.1 0.2 0.3 0.4 0.5<br>Time (s) Time (s)<br>y coordinate (m)<br>z coordinate (m)<br>Mechanical energy (J)<br><!-- End of picture text -->

Fig. 9. **Trajectory of a cube sliding on a plane.** The cube is initialized with an initial tangential velocity along the x-axis. **Right:** The bias of friction forces (Fig.6) introduces a tangential velocity along the y-axis, which deviates the cube from the expected straight-line trajectory. 

Fig. 10. **A cube is initialized on a plane with a tangential velocity along the x-axis,** similarly to the case studied in Fig. 9. **Left:** The CCP contact model relaxes the Signorini condition, which induces unphysical forces leading to the vertical bouncing of the cube. **Right:** From the MDP, it is possible to determine the evolution of the energy of the system analytically and compare it to what is computed by the various simulation algorithms. The CCP relaxation induces a significant gap with the analytical solution. The RaiSim contact model narrows this gap but dissipates less power than expected, as it does not always enforce the MDP. The NCP formulation, solved using the PGS solver, is the only formulation that closely matches the expected analytical behavior of the system. 

Signorini condition but still does not match the analytical solution due to its relaxation of the MDP (24) (Fig. 10, right). 

In Figure 11, we simulate a cube dragged on a plane and measure the integral error between the trajectory obtained with the CCP/ADMM solver with various ∆ _t_ and a reference one computed via the NCP/PGS solver with small time step ∆ _t_ = 10<sup>_−_5</sup> _s_ . The deviation from the reference trajectory is quantified via the integral consistency error defined as<sup>�</sup><sup>_T_</sup> _τ_ =0<sup>_∥qτ −_</sup> _<u>q</u>_<sup>_~~τ~~_</sup> _∥_ ∆ _t_ . As detailed in Sec. III-B, the error between the trajectories obtained with the CCP and NCP models is proportional to the time step ∆ _t_ . 

## **Underdetermined contact problems.** Underdetermination 



<!-- Start of picture text -->
10 1 CCP/ADMM<br>10 2<br>10 3<br>10 4<br>10 5 10 4 10 3 10 2 10 1<br>t<br>Error (m)<br><!-- End of picture text -->

Fig. 11. **Applying a linearly growing force along the x-axis to a cube on a plane.** The cube has a mass of 1kg, a side length of 0.2m, a friction coefficient of 0.4 and the external force grows linearly from 0 to 20N over 1s. This induces relatively high velocities in a robotic context that are useful for illustrative purposes here. 



<!-- Start of picture text -->
1.41.2 NCP/PGSCCP/ADMM 2 CCP/ADMMCCP/PGS<br>CCP/PGS RaiSim<br>1.0 RaiSim 1<br>0.8 0<br>0.6<br>0.4 1<br>0.2 2<br>0.0<br>0.0 0.1 0.2 0.3 0.4 0.5 0.0 0.1 0.2 0.3 0.4 0.5<br>Time (s) Time (s)<br>Velocity (m/s)<br>Internal forces (N)<br><!-- End of picture text -->

Fig. 12. **A cube is dragged on a plane along the x-axis** similarly to the case studied in Fig. 11. **Left:** The cube is at stiction before it starts sliding after approximately 0.25s. The tangential velocity differs depending on the contact model e.g. RaiSim violates the MDP leading to contact points sliding faster than in the case of NCP. **Right:** At stiction, multiple combinations of tangential forces may lead to the same trajectory. There are four curves for each contact model, each curve accounting for the y-component from one of the four contact forces on the cube. Gauss-Seidel-like solvers, _e.g._ RaiSim and PGS, exhibit internal forces "stretching" the cube at stiction before the MDP enforces these forces to disappear when the cube starts to slide. RaiSim relaxes the maximum dissipation principle so the friction forces are not opposed to the movements, and internal forces persist when the cube is sliding. Eventually, ADMM avoids injecting jamming internal forces even at stiction. 

occurs when infinite combinations of contact forces lead to the same trajectory. These artifacts happen on the normal and tangential components of contact forces, as depicted in Fig. 12. As shown in Fig. 12, the solution found depends on the numerical scheme. We observe that the per-contact approaches (Alg. 2,5 and 6) exhibit jamming internal forces at stiction, values which are not controlled by the algorithms. On the opposite, the algorithms working directly on the global contact problem with a proximal regularization (Alg. 3 and 7) seem to avoid injecting such artifacts in the contact forces (Fig. ,12). As future work, it would be interesting to investigate the theory behind the latter conjecture. 

This phenomenon may seem innocuous as forward dynamics are not affected. However, it makes the inverse dynamics illposed, as there is no way to predict such numerical artifacts. Additionally, in the context of differentiable physics, we believe these spurious contact forces may catastrophically impact the computation of derivatives, but we also leave this study as future work. Finally, it is worth mentioning that such underdetermined cases are ubiquitous in robotics (e.g., legged robots making redundant contact with their environments). 

**Robustness to ill-conditioned contact problems.** More generally, the contact problem becomes challenging when the ratio between the biggest and the smallest eigenvalue of the Delassus matrix grows. The experiment of Fig. 13 exhibits the convergence issues of per-contact approaches when simulating systems with a strong coupling between the different contact points, which causes large off-diagonal terms on the matrix _G_ . In this situation, the latter approaches hit the maximum number of iterations before convergence, leading to unrealistic trajectories. Such a behavior can be expected as supposing the matrix to be diagonally dominant is a classical hypothesis ensuring the convergence of Gauss-Seidel methods. On the contrary, the proximal algorithms account for off-diagonal terms of _G_ , and only rely on a regularized inverse of _G_ (Alg. 3, line 1), and thus robustly converge towards an optimal solution. 

13 



<!-- Start of picture text -->
10 4<br>10 2 CCP/ADMM 10 2 CCP/ADMM<br>10102 0 CCP/PGSNCP/PGS 10 1 CCP/PGSDrake<br>1010 46 NCP/StagProjRaiSim 10 4<br>10 8 CCP/Newton 10 7<br>1010 1012 10 10<br>10 14 10 13<br>10 16<br>0.00 0.02 0.04 0.06 0.08 0.10 10 0 10 1 10 2 10 3 10 4 10 5 10 6<br>Time (s) Mass ratio<br>NCP criterion<br>Contact complementarity ()c<br><!-- End of picture text -->

Fig. 13. **Simulation of ill-conditioned systems. Left:** Stacking a heavy cube (10<sup>3</sup> kg) on a light one (10<sup>_−_3</sup> kg) makes the problem ill-conditioned and, therefore, not solvable via per-contact algorithms (CCP/PGS, NCP/PGS and RaiSim) which results in the violation of the contact complementarity criterion (15). By contrast, the ADMM, staggered projections, and Newton approaches appear to be robust in this case. **Right:** The accuracy of the simulators improves when the ratio between the masses of the two cubes gets close to one. The ADMM and Newton algorithms are less affected by this ratio than PGS. 

**Effects of compliance.** As demonstrated by Fig. 14, the normal forces vary linearly with the compliance parameter _R_ . Moreover, adding compliance to the tangential components induces the vanishing of dry friction, resulting in tangential oscillations instead of a null velocity. These compliant effects regularize the infinitely steep graphs due to the Signorini condition and Coulomb’s law and replace them with locally linear mapping, which also eases the numerics. Therefore, the compliance added in MuJoCo has no physical purpose and should be considered a numerical trick designed to circumvent the issues due to hyper-staticity or ill-conditioning at the cost of impairing the simulation. 

## _B. Self-consistency of the solvers_ 

The accuracy of simulators can be affected by the numerical resolution induced by two "hyper-parameters": the value of the stopping criterion for the contact solver desired accuracy ( _ϵabs_ ) and the time-step value (∆ _t_ ). We measure their effect on the simulation quality when varying them independently. A simulator is said to be self-consistent when this deviation remains limited. 

Time-stepping simulators are sensitive to the choice of the time-step ∆ _t_ . Here, we intend to assess the self-consistency of the various contact solvers by examining their deviation when ∆ _t_ grows. Because time discretization also affects the collision detection process, our study is done on the trajectory of a cube dragged on a plane by a growing tangential force and whose contact points should remain constant (as done in Fig. 11). This scenario also allows to asses both sticking and sliding modes. For each simulator, a trajectory _<u>q</u>_ obtained by simulating the system with a small time-step (∆ _t_ = 10<sup>_−_2</sup> _ms_ ) serves as a reference to compute the state consistency error along the trajectories simulated with larger time-steps (Fig. 15). 

Looking at Fig. 15, we observe that the CCP contact model is more sensitive with respect to the time step in the considered scenario. Indeed, because CCP relaxes the _Signorini condition_ , the cube slides at a height proportional to ∆ _t_ . Similarly, as shown by Fig. 15, the energy evolution of the system simulated via NCP and RaiSim models is only a little modified 

when increasing ∆ _t_ while CCP leads to a nonphysical and inconsistent behavior. 

## _C. Performance benchmarks_ 

As evoked earlier, in addition to being physically accurate, it is also essential for a simulator to be fast, which, in general, constitutes two adversarial requirements. To evaluate the computational footprint of the various solvers, we measure both the number of iterations and the time taken to reach a fixed accuracy on dynamic trajectories involving robotics systems (Fig. 8). This is done on three different robotics scenarios: the quadruped Solo (12-dof) and the humanoid Talos (32-dof) are in a standing position and perturbed by applying an external force (of respectively 10N and 80N) at their center of mass, while a ball is dropped in the Allegro hand (16-dof), so the trajectories are not static. 

Looking at the number of iterations required to converge (Fig. 16), PGS approaches appear to be reasonably fast to reach mild accuracy ( _ϵ_ abs = 10<sup>_−_5</sup> ) while they eventually saturate before reaching high precision in complex scenarii (Fig. 16, bottom). We show later this can be insufficient for challenging tasks (Fig. 19). On the other hand, ADMM, Newton and Staggered Projections algorithms can find high-accuracy solutions using only a few, but more costly, iterations. As mentioned earlier, our implementation of Drake’s solver uses a backtracking line search with an Armijo condition while the original algorithm [35] uses a more advanced routine. This difference could lead to degraded performances here which should be kept in mind when interpreting the results. 

The latter analysis does not account for the per-iteration computational cost, so we report a study on final timings in Fig. 17. As they work with various contact model hypotheses and thus have different convergence criteria, it is challenging to make a fair comparison between the solvers. Therefore, we choose to run the solvers in the setup they are usually used in practice: the solver is stopped whenever it reaches an absolute convergence threshold ( _ϵ_ abs = 10<sup>_−_6</sup> ) or otherwise, it is early-stopped if a maximum number of iteration ( _n_ iter = 10<sup>4</sup> ) is reached or stalling is detected via relative convergence criterion ( _ϵ_ abs = 10<sup>_−_8</sup> ). For this reason, Fig. 17 is only informative about the computational cost but not about the accuracy of solvers. When the contact solvers are cold started, we observe that the second-order optimization techniques [32], [35] are less efficient than the PGS solvers and their cheap per-contact iterations (Fig. 17, left). The advanced first-order algorithms like ADMM (Alg. 3) working on the dual CCP problem (20) stands in-between as they leverage the very efficient Featherstone algebra [54] for the computation of the Cholesky factorization of _G_ (Sec. III-E). However, leveraging the solution from the previous time step to warm-start the solvers — a common strategy in practice — allows for significantly reducing this gap (Fig. 17, right). Therefore, regarding the study of Sec. IV-A, a trade-off appears for algorithms like ADMM, which treat all the contact points globally. In practice, they might be slower than their PGS counterpart while they benefit from better behaviors on ill-conditioned problems. 

14 



<!-- Start of picture text -->
0 CCP/ADMM 10 4 CCP/ADMM<br>8<br>CCP/PGS CCP/PGS<br>10 6 Analytical 10 5 6 Analytical<br>10 5<br>10 4 10 6 CCP/ADMM 4<br>CCP/PGS 2<br>10 3 Analytical<br>0 0<br>0 10 3 10 2 10 1 10 0 0 10 3 10 2 10 1 10 0 0 10 3 10 2 10 1 10 0<br>Compliance (m/N) Compliance (m/N) Compliance (m/N)<br>of Solo-12 with varying compliance for the contacts with the floor. The robot is in a standing position and perturbed with an external<br>Left: Adding a compliance to the contact model relaxes the Signorini condition. Center: This compliance also relaxes the Coulomb’s law<br>Compliance also regularizes the problem, removing the jamming internal forces in the under-determined cases.<br>40 0.1ms 10 0 CCP/ADMM 10 2 CCP/ADMM<br>35 1ms 10 3 CCP/PGSNCP/PGS 10 5 CCP/PGSNCP/PGS<br>30 10ms 10 6 CCP/Newton 10 8 CCP/Newton<br>25 100msNCP/PGS 10 9 10 11<br>20 CCP/ADMM 10 12 10 14<br>15 RaiSim 10 15 10 17<br>10 0 20 40 60 80 0 20 40 60 80<br>5 Iterations Iterations<br>0 0.0 0.2 0.4Time (s)0.6 0.8 1.0 1010 24 1010 35<br>10 6 10 7<br>10 2 10 8 CCP/ADMMCCP/PGS 10 9 CCP/ADMMCCP/PGS<br>10 10 NCP/PGS 10 11 NCP/PGS<br>10 3 CCP/Newton CCP/Newton<br>0 20 40 60 80 100 0 20 40 60 80 100<br>Iterations Iterations<br>10 4<br>10 5 NCP/PGSCCP/ADMMRaiSim (Bottom) Fig. 16. Convergencerobots. The considered for contact contact problems problems on Solo are extracted (Top) and from<br>time step of the full trajectory. PGS is fast to reach a mild accuracy before<br>10 4 10 3 10 2 10 1 saturating, while ADMM and second-order algorithms can get to higher<br>t precision.<br>Internal forces (N)<br>Normal velocity (m/s) Tangent velocity (m/s)<br>Dual feasibility ()d<br>Contact complementarity ()c<br>Mechanical energy (J)<br>Dual feasibility ()d<br>Contact complementarity ()c<br>Consistency error (m)<br><!-- End of picture text -->

Fig. 14. **Simulation of Solo-12 with varying compliance for the contacts with the floor.** The robot is in a standing position and perturbed with an external horizontal force. **Left:** Adding a compliance to the contact model relaxes the Signorini condition. **Center:** This compliance also relaxes the Coulomb’s law of friction. **Right:** Compliance also regularizes the problem, removing the jamming internal forces in the under-determined cases. 

Fig. 16. **Convergencerobots. for contact problems on Solo (Top) and Talos (Bottom) robots.** The considered contact problems are extracted from one time step of the full trajectory. PGS is fast to reach a mild accuracy before saturating, while ADMM and second-order algorithms can get to higher precision. 

Fig. 15. **Self-consistency w.r.t. time-stepping when simulating a cube dragged on a plane by a growing tangential force.** The CCP contact model appears to be more sensitive to the time step ∆ _t_ . This sensitivity can also be observed through the evolution of mechanical energy. 



<!-- Start of picture text -->
CCP/ADMM RaiSim CCP/ADMM RaiSim<br>10 3 CCP/PGS NCP/StagProj 10 3 CCP/PGS NCP/StagProj<br>NCP/PGS Drake NCP/PGS Drake<br>10 2 10 2<br>10 1 10 1<br>10 0 10 0<br>solo allegro hand talos solo allegro hand talos<br>Runtime (s) Runtime (s)<br><!-- End of picture text -->

## _D. MPC for quadruped locomotion_ 

The previous examples already illustrate the differences among the various simulators in terms of both physical accuracy and computational efficiency. However, such scenarios may not represent the richness of contacts in practical robotics situations. For this purpose, we use the implementation of MPC on the Solo-12 system introduced in [96] to generate locomotion trajectories on flat and bumpy terrains. These experiments are designed to involve a wide variety of contacts ( _i.e._ , sticking, sliding, and taking-off) and see how the simulation choices impact the final task ( _i.e._ , horizontal translation of the robot). 

Fig. 17. **Computational timings measured along a trajectory for three robotic systems** ( _c.f._ Fig. 8). The represented timings are obtained by averaging on the entire trajectory. The contact solvers are tested in both cold-start ( **Left** ) and warm-start ( **Right** ) modes. We simulate the same trajectories to evaluate the benefit of warm-starting, but we use the solution of the previous time step as an initial guess. This leads to significant improvements in the computational timings. 

For a flat and barely slippery ( _µ_ = 0 _._ 9) ground, we observe that the choice of simulator hardly affects the base velocity tracked by the MPC controller (Fig. 18, top right). In this case, the contacts are mainly sticking, leading to low violation of the NCP criterion (15) (Fig. 18, bottom left). 

of our previous study, as both the RaiSim and CCP contact models make physical approximations when contact points are sliding (Fig. 19, bottom left). However, we occasionally observe that NCP/PGS also violates the NCP criterion (15) (Fig. 19, bottom left) but for a different reason: PGS was not able to converge before the maximum number of iterations was reached. Therefore, Gauss-Seidel-like approaches appear to be sufficient for mild conditions (Fig. 18) but are not robust enough to ensure convergence of the simulation when the 

When the terrain is bumpy (roughness of 10<sup>_−_1</sup> _m_ ) and slippery ( _µ_ = 0 _._ 3), the locomotion velocity generated from the RaiSim and CCP models significantly deviates from the NCP one (Fig. 19, top right). This can be expected, in light 

15 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2 CCP/ADMM<br>0.0 NCP/PGS<br>RaiSim<br>0.2 target velocity<br>0 1 2 3 4 5<br>Time (s)<br>10 2<br>CCP/ADMM CCP/ADMM<br>10 1 RaiSim 10 NCP/PGS<br>10 0 NCP/PGS RaiSim<br>8<br>10 1<br>10 2 6<br>10 3 4<br>10 4<br>2<br>0<br>0 1 2 3 4 5 0<br>Time (s) solo<br>Base velocity (m/s)<br>Runtime (s)<br>Contact complementarity ()c<br><!-- End of picture text -->

Fig. 18. **MPC for locomotion on a flat terrain** ( **Top left** ). The target horizontal translation velocity of the base is similarly reached by the controller with the different simulators ( **Top right** ). However, they do not equally respect the contact complementarity criterion (15) ( **Bottom left** ). Per-contact approaches, _e.g._ PGS and RaiSim, are more efficient ( **Bottom right** ). 



<!-- Start of picture text -->
CCP/ADMM<br>1.5 NCP/PGS<br>1.0 RaiSimtarget velocity<br>0.5<br>0.0<br>0.5<br>1.0<br>0 1 2 3 4 5<br>Time (s)<br>10 2 CCP/ADMM CCP/ADMM<br>RaiSim 25 NCP/PGS<br>10 1 NCP/PGS RaiSim<br>10 0 20<br>10 1 15<br>10 2<br>10 3 10<br>10 4 5<br>0<br>0 1 2 3 4 5 0<br>Time (s) solo<br>Base velocity (m/s)<br>Runtime (s)<br>Contact complementarity ()c<br><!-- End of picture text -->

Fig. 19. **MPC for locomotion on a bumpy terrain** ( **Top left** ). The tracked velocity of the base quickly differs depending on the used simulator ( **Top right** ). Slippery contact points violate the contact complementarity criterion (15) for the RaiSim and CCP contact modelings ( **Bottom left** ). The complexity of contacts also hampers the solvers and reduces the gap between per-contact and ADMM approaches ( **Bottom right** ). 

locomotion tasks become more challenging (Fig. 19). This also causes increased computations from the solvers, particularly for RaiSim (Fig. 19, bottom right). These observations indicate that the combination of low-level choices on both the contact model and solver may induce significant differences in the high-level behaviors of locomotion controllers on complex terrains. 

## V. DISCUSSION AND CONCLUSION 

NCP is known to be complex to solve and thus is often relaxed to find approximate solutions. In this article, we report a deeper study on how the various rigid contact models commonly employed in robotics and their associated solvers can impact the resulting simulation. We have notably established and experimentally highlighted that these choices may induce unphysical artifacts, thus widening the reality gap, leading 

to unrealistic behaviors when the simulator is later used for practical robotics applications. Our experiments show that there is no fully satisfactory approach at the moment, as all existing solutions compromise either accuracy, robustness, or efficiency. This indicates that there may still be room for improvements in contact simulation. It is also worth mentionning that, for robotics, simulation samples of lesser but controlled accuracy are already valuable for many applications, _e.g._ RL and MPC, while a failed simulation represent a waste of ressources. This paper showcases that situations prone to failure of simulation are not only corner cases but can become quite common when adressing challenging tasks such as locomotion. This justifies the emphasis put by modern simulators [32], [37], [35] on robustness when modeling contacts and implementing the associated solvers. 

Beyond contact simulation, differentiable physics constitutes an emergent and closely related topic. However, the impact of forward simulation artifacts on gradient computation remains unexplored. In particular, some of the relaxations at work, _e.g._ the artificial compliance added in MuJoCo, result in crucial differences in gradients, which then affect downstream applications like trajectory optimization [97], [98]. We leave the study of the various existing differentiable simulators [5], [6], [7], [99], [8] through this lens as future work. 

For all these reasons, we believe it would be highly beneficial for the robotics community to take up such low-level topics around simulation, as they could lead to substantial progress in the field. The work of [43] is an inspiring first step in this direction. With this article, we intend to go further by also providing open-source implementations and benchmarks to the community. 

## ACKNOWLEDGMENTS 

We warmly thank Jemin Hwangbo for providing useful details on the algorithm of the RaiSim simulator, Stéphane Caron and Nicolas Mansard for helpful discussions. This work was supported in part by L’Agence d’Innovation Défense, the French government under the management of Agence Nationale de la Recherche through the project INEXACT (ANR-22-CE33-0007-01) and as part of the "Investissements d’avenir" program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute), by the European Union through the AGIMUS project (GA no.101070165) and the Louis Vuitton ENS Chair on Artificial Intelligence. Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the European Commission can be held responsible for them. 

## REFERENCES 

- [1] W. Li and E. Todorov, “Iterative linear quadratic regulator design for nonlinear biological movement systems.,” vol. 1, pp. 222–229, 01 2004. 

> [2] D. Mayne, “A second-order gradient method for determining optimal trajectories of non-linear discrete-time systems,” _International Journal of Control_ , vol. 3, no. 1, pp. 85–95, 1966. 

> [3] Y. Tassa, T. Erez, and E. Todorov, “Synthesis and stabilization of complex behaviors through online trajectory optimization,” in _2012 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pp. 4906– 4913, IEEE, 2012. 

16 

- [4] J. Carpentier and N. Mansard, “Analytical derivatives of rigid body dynamics algorithms,” in _Robotics: Science and systems (RSS 2018)_ , 2018. 

- [5] F. de Avila Belbute-Peres, K. Smith, K. Allen, J. Tenenbaum, and J. Z. Kolter, “End-to-end differentiable physics for learning and control,” _Advances in neural information processing systems_ , vol. 31, 2018. 

- [6] Q. Le Lidec, I. Kalevatykh, I. Laptev, C. Schmid, and J. Carpentier, “Differentiable simulation for physical system identification,” _IEEE Robotics and Automation Letters_ , vol. 6, no. 2, pp. 3413–3420, 2021. 

- [7] K. Werling, D. Omens, J. Lee, I. Exarchos, and C. K. Liu, “Fast and feature-complete differentiable physics engine for articulated rigid bodies with contact constraints,” in _Robotics: Science and Systems_ , 2021. 

- [8] T. Howell, S. Le Cleac’h, J. Brüdigam, Z. Kolter, M. Schwager, and Z. Manchester, “Dojo: A differentiable simulator for robotics,” _arXiv preprint arXiv:2203.00806_ , 2022. 

- [9] M. Diehl, H. G. Bock, H. Diedam, and P.-B. Wieber, “Fast direct multiple shooting algorithms for optimal robot control,” in _Fast motions in biomechanics and robotics_ , pp. 65–93, Springer, 2006. 

- [10] D. Q. Mayne, “Model predictive control: Recent developments and future promise,” _Automatica_ , vol. 50, no. 12, pp. 2967–2986, 2014. 

- [11] S. Kleff, A. Meduri, R. Budhiraja, N. Mansard, and L. Righetti, “Highfrequency nonlinear model predictive control of a manipulator,” in _2021 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 7330–7336, IEEE, 2021. 

- [12] E. Dantec, M. Taix, and N. Mansard, “First order approximation of model predictive control solutions for high frequency feedback,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, pp. 4448–4455, 2022. 

- [13] R. S. Sutton and A. G. Barto, _Reinforcement learning: An introduction_ . MIT press, 2018. 

- [14] J. Tan, T. Zhang, E. Coumans, A. Iscen, Y. Bai, D. Hafner, S. Bohez, and V. Vanhoucke, “Sim-to-real: Learning agile locomotion for quadruped robots.,” in _Robotics: Science and Systems_ , 2018. 

- [15] I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, _et al._ , “Solving rubik’s cube with a robot hand,” _arXiv preprint arXiv:1910.07113_ , 2019. 

- [16] J. Hwangbo, J. Lee, A. Dosovitskiy, D. Bellicoso, V. Tsounis, V. Koltun, and M. Hutter, “Learning agile and dynamic motor skills for legged robots,” _Science Robotics_ , vol. 4, no. 26, p. eaau5872, 2019. 

- [17] M. T. Mason and J. K. Salisbury Jr, _Robot hands and the mechanics of manipulation_ . The MIT Press, Cambridge, MA, 1985. 

- [18] J. Ponce, S. Sullivan, A. Sudsang, J.-D. Boissonnat, and J.-P. Merlet, “On computing four-finger equilibrium and force-closure grasps of polyhedral objects,” _The International Journal of Robotics Research_ , vol. 16, no. 1, pp. 11–35, 1997. 

- [19] B. Dynamics, “Atlas gets a grip | boston dynamics.” https://youtu.be/ -e1_QhJ1EhQ. 

- [20] I. Mordatch, E. Todorov, and Z. Popovi´c, “Discovery of complex behaviors through contact-invariant optimization,” _ACM Transactions on Graphics (ToG)_ , vol. 31, no. 4, pp. 1–8, 2012. 

- [21] M. Posa, C. Cantu, and R. Tedrake, “A direct method for trajectory optimization of rigid bodies through contact,” _The International Journal of Robotics Research_ , vol. 33, no. 1, pp. 69–81, 2014. 

- [22] M. A. Toussaint, K. R. Allen, K. A. Smith, and J. B. Tenenbaum, “Differentiable physics and stable modes for tool-use and manipulation planning,” 2018. 

- [23] R. Featherstone, _Rigid body dynamics algorithms_ . Springer, 2014. 

- [24] J. Carpentier, G. Saurel, G. Buondonno, J. Mirabel, F. Lamiraux, O. Stasse, and N. Mansard, “The pinocchio c++ library: A fast and flexible implementation of rigid body dynamics algorithms and their analytical derivatives,” in _2019 IEEE/SICE International Symposium on System Integration (SII)_ , pp. 614–619, IEEE, 2019. 

- [25] J. J. Moreau, “Unilateral Contact and Dry Friction in Finite Freedom Dynamics,” in _Nonsmooth Mechanics and Applications_ (M. J.J. and P. P.D., eds.), vol. 302 of _International Centre for Mechanical Sciences (Courses and Lectures)_ , pp. 1–82, Springer, 1988. 

- [26] M. Jean, “The non-smooth contact dynamics method,” _Computer methods in applied mechanics and engineering_ , vol. 177, no. 3-4, pp. 235–257, 1999. 

- [27] V. Acary, F. Cadoux, C. Lemaréchal, and J. Malick, “A formulation of the linear discrete Coulomb friction problem via convex optimization,” _Journal of Applied Mathematics and Mechanics / Zeitschrift für Angewandte Mathematik und Mechanik_ , vol. 91, pp. 155–175, Feb. 2011. 

- [28] B. Brogliato, A. Ten Dam, L. Paoli, F. Génot, and M. Abadie, “Numerical simulation of finite dimensional multibody nonsmooth mechanical systems,” _Appl. Mech. Rev._ , vol. 55, no. 2, pp. 107–150, 2002. 

- [29] R. Smith, “Open dynamics engine,” 2008. http://www.ode.org/. 

- [30] E. Coumans and Y. Bai, “Pybullet, a python module for physics simulation for games, robotics and machine learning.” http://pybullet.org, 2016–2021. 

- [31] J. Lee, M. X. Grey, S. Ha, T. Kunz, S. Jain, Y. Ye, S. S. Srinivasa, M. Stilman, and C. K. Liu, “DART: Dynamic animation and robotics toolkit,” _The Journal of Open Source Software_ , vol. 3, p. 500, Feb 2018. 

- [32] E. Todorov, T. Erez, and Y. Tassa, “Mujoco: A physics engine for modelbased control,” in _2012 IEEE/RSJ international conference on intelligent robots and systems_ , pp. 5026–5033, IEEE, 2012. 

- [33] J. Hwangbo, J. Lee, and M. Hutter, “Per-contact iteration method for solving contact dynamics,” _IEEE Robotics and Automation Letters_ , vol. 3, no. 2, pp. 895–902, 2018. 

- [34] R. Tedrake and the Drake Development Team, “Drake: Model-based design and verification for robotics,” 2019. 

- [35] A. M. Castro, F. N. Permenter, and X. Han, “An unconstrained convex formulation of compliant contact,” _IEEE Transactions on Robotics_ , vol. 39, no. 2, pp. 1301–1320, 2022. 

- [36] D. M. Kaufman, S. Sueda, D. L. James, and D. K. Pai, “Staggered projections for frictional contact in multibody systems,” pp. 1–11, 2008. 

- [37] M. Macklin, K. Erleben, M. Müller, N. Chentanez, S. Jeschke, and V. Makoviychuk, “Non-smooth newton methods for deformable multibody dynamics,” _ACM Transactions on Graphics (TOG)_ , vol. 38, no. 5, pp. 1–20, 2019. 

- [38] A. Enzenhöfer, N. Lefebvre, and S. Andrews, “Efficient block pivoting for multibody simulations with contact,” in _Proceedings of the ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games_ , pp. 1–9, 2019. 

- [39] Z. Ferguson, M. Li, T. Schneider, F. Gil-Ureta, T. Langlois, C. Jiang, D. Zorin, D. M. Kaufman, and D. Panozzo, “Intersection-free rigid body dynamics,” _ACM Trans. Graph._ , vol. 40, jul 2021. 

- [40] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, _et al._ , “Isaac gym: High performance gpu based physics simulation for robot learning,” in _Thirtyfifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)_ , 2021. 

- [41] C. D. Freeman, E. Frey, A. Raichuk, S. Girgin, I. Mordatch, and O. Bachem, “Brax-a differentiable physics engine for large scale rigid body simulation,” in _Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 1)_ , 2021. 

- [42] T. Erez, Y. Tassa, and E. Todorov, “Simulation tools for model-based robotics: Comparison of bullet, havok, mujoco, ode and physx,” in _2015 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 4397–4404, 2015. 

- [43] P. Horak and J. C. Trinkle, “On the similarities and differences among contact models in robot simulation,” _IEEE Robotics and Automation Letters_ , vol. 4, pp. 493–499, 2019. 

- [44] J. Carpentier, F. Valenza, N. Mansard, _et al._ , “Pinocchio: fast forward and inverse dynamics for poly-articulated systems.” https://stack-oftasks.github.io/pinocchio, 2015–2021. 

- [45] J. Pan, S. Chitta, D. Manocha, F. Lamiraux, J. Mirabel, J. Carpentier, _et al._ , “HPP-FCL: an extension of the Flexible Collision Library.” https://github.com/humanoid-path-planner/hpp-fcl, 2015–2022. 

- [46] J. Mirabel, S. Tonneau, P. Fernbach, A.-K. Seppälä, M. Campana, N. Mansard, and F. Lamiraux, “HPP: A new software for constrained motion planning,” in _International Conference on Intelligent Robots and Systems_ , 2016. 

- [47] L. Montaut, Q. Le Lidec, V. Petrík, J. Sivic, and J. Carpentier, “Collision Detection Accelerated: An Optimization Perspective,” in _Proceedings of Robotics: Science and Systems_ , (New York City, NY, USA), June 2022. 

- [48] F. E. Udwadia and R. E. Kalaba, “A new perspective on constrained motion,” _Proceedings of the Royal Society of London. Series A: Mathematical and Physical Sciences_ , vol. 439, no. 1906, pp. 407–410, 1992. 

- [49] H. Bruyninckx and O. Khatib, “Gauss’ principle and the dynamics of redundant and constrained manipulators,” in _Proceedings 2000 ICRA. Millennium Conference. IEEE International Conference on Robotics and Automation. Symposia Proceedings (Cat. No. 00CH37065)_ , vol. 3, pp. 2563–2568, IEEE, 2000. 

- [50] S. Redon, A. Kheddar, and S. Coquillart, “Gauss’ least constraints principle and rigid body simulations,” in _Robotics and Automation, 2002. Proceedings. ICRA’02. IEEE International Conference on_ , vol. 1, (Washington, DC, United States), pp. 517–522, 2002. 

- [51] E. Todorov, “A convex, smooth and invertible contact model for trajectory optimization,” in _2011 IEEE International Conference on Robotics and Automation_ , pp. 1071–1076, IEEE, 2011. 

- [52] C. Studer, R. Leine, and C. Glocker, “Step size adjustment and extrapolation for time-stepping schemes in non-smooth dynamics,” _International journal for numerical methods in engineering_ , vol. 76, no. 11, pp. 1747– 1781, 2008. 

17 

- [53] S. L. Campbell and C. W. Gear, “The index of general nonlinear DAEs,” _Numerische Mathematik_ , vol. 72, pp. 173–196, 1995. 

- [54] J. Carpentier, R. Budhiraja, and N. Mansard, “Proximal and sparse resolution of constrained dynamic equations,” in _Robotics: Science and Systems_ , 2021. 

- [55] C. F. Gauß, “Über ein neues allgemeines grundgesetz der mechanik.,” 1829. 

- [56] L. Montaut, Q. Le Lidec, V. Petrik, J. Sivic, and J. Carpentier, “Collision detection accelerated: An optimization perspective,” in _RSS 2022Robotics: Science and Systems_ , 2022. 

- [57] F. Pfeiffer and C. Glocker, _Multibody Dynamics with Unilateral Contacts_ . CISM International Centre for Mechanical Sciences, Springer, 2000. 

- [58] C. Ericson, _Real-time collision detection_ . Crc Press, 2004. [59] E. G. Gilbert, D. W. Johnson, and S. S. Keerthi, “A fast procedure for computing the distance between complex objects in three-dimensional space,” _IEEE Journal on Robotics and Automation_ , vol. 4, no. 2, pp. 193– 203, 1988. 

- [60] C. Ericson, _Real-Time Collision Detection_ . The Morgan Kaufmann Series, 2004. 

- [61] K. Mamou and F. Ghorbel, “A simple and efficient approach for 3d mesh approximate convex decomposition,” in _2009 16th IEEE International Conference on Image Processing (ICIP)_ , pp. 3501–3504, 2009. 

- [62] A. Signorini, “Questioni di elasticità non linearizzata e semilinearizzata,” _Rendiconti di Matematica e delle sue applicazioni_ , vol. 18, no. 5, pp. 95– 139, 1959. 

- [63] R. W. Cottle, J.-S. Pang, and R. E. Stone, _The Linear Complementarity Problem_ . Society for Industrial and Applied Mathematics, 2009. 

- [64] P. Wensing, R. Featherstone, and D. E. Orin, “A reduced-order recursive algorithm for the computation of the operational-space inertia matrix,” in _2012 IEEE International Conference on Robotics and Automation_ , pp. 4911–4917, IEEE, 2012. 

- [65] O. A. Bauchau and A. Laulusa, “Review of contemporary approaches for constraint enforcement in multibody systems,” 2008. 

- [66] J. Baumgarte, “Stabilization of constraints and integrals of motion in dynamical systems,” _Computer methods in applied mechanics and engineering_ , vol. 1, no. 1, pp. 1–16, 1972. 

- [67] G. de Saxcé and Z.-Q. Feng, “The bipotential method: A constructive approach to design the complete contact law with friction and improved numerical algorithms,” _Mathematical and Computer Modelling_ , vol. 28, pp. 225–245, Aug. 1998. 

- [68] V. Acary, M. Brémond, and O. Huber, “On solving contact problems with Coulomb friction: formulations and numerical comparisons,” Research Report RR-9118, INRIA, Nov. 2017. 

- [69] H. Barbosa and R. Feijóo, “A numerical algorithm for signorini’s problem with coulomb friction,” in _Unilateral Problems in Structural Analysis—2: Proceedings of the Second Meeting on Unilateral Problems in Structural Analysis, Prescudin, June 17–20, 1985_ , pp. 33–45, Springer, 1987. 

- [70] M. A. Tzaferopoulos, “On an efficient new numerical method for the frictional contact problem of structures with convex energy density,” _Computers & structures_ , vol. 48, no. 1, pp. 87–106, 1993. 

- [71] K. Erleben, “Rigid body contact problems using proximal operators,” in _Proceedings of the ACM SIGGRAPH / Eurographics Symposium on Computer Animation_ , SCA ’17, (New York, NY, USA), Association for Computing Machinery, 2017. 

- [72] J. Pan, S. Chitta, and D. Manocha, “FCL: A General Purpose Library for Collision and Proximity Queries,” in _2012 IEEE International Conference on Robotics and Automation_ , IEEE, 2012. 

- [73] D. Fiser, “libccd.” https://github.com/danfis/libccd. [74] M. Macklin, K. Storey, M. Lu, P. Terdiman, N. Chentanez, S. Jeschke, and M. Müller, “Small steps in physics simulation,” in _Proceedings of the 18th Annual ACM SIGGRAPH/Eurographics Symposium on Computer Animation_ , SCA ’19, (New York, NY, USA), Association for Computing Machinery, 2019. 

- [75] M. L. Felis, “Rbdl: an efficient rigid-body dynamics library using recursive algorithms,” _Autonomous Robots_ , vol. 41, no. 2, pp. 495–511, 2017. 

- [76] M. Anitescu and A. Tasora, “An iterative approach for cone complementarity problems for nonsmooth dynamics,” _Computational Optimization and Applications_ , vol. 47, no. 2, pp. 207–235, 2010. 

- [77] E. Mitsopoulou and I. Doudoumis, “A contribution to the analysis of unilateral contact problems with friction,” _Solid Mechanics Archives_ , vol. 12, no. 3, pp. 165–186, 1987. 

- [78] I. Doudoumis and E. Mitsopoulou, “On the solution of the unilateral contact frictional problem for general static loading conditions,” _Computers & structures_ , vol. 30, no. 5, pp. 1111–1126, 1988. 

- [79] F. Jourdan, P. Alart, and M. Jean, “A gauss-seidel like algorithm to solve frictional contact problems,” _Computer methods in applied mechanics and engineering_ , vol. 155, no. 1-2, pp. 31–47, 1998. 

- [80] K. Erleben, “Numerical methods for linear complementarity problems in physics-based animation,” in _ACM SIGGRAPH 2013 Courses_ , SIGGRAPH ’13, (New York, NY, USA), Association for Computing Machinery, 2013. 

- [81] C. E. Lemke, “Bimatrix equilibrium points and mathematical programming,” _Management science_ , vol. 11, no. 7, pp. 681–689, 1965. 

- [82] G. B. Dantzig and R. W. Cottle, “Positive (semi-) definite matrices and mathematical programming,” _Report ORC_ , vol. 13, pp. 63–18, 1963. 

- [83] M. Anitescu and F. Potra, “Formulating dynamic multi-rigid-body contact problems with friction as solvable linear complementarity problems,” _Nonlinear Dynamics_ , vol. 14, 03 1997. 

- [84] J. Trinkle, J.-S. Pang, S. Sudarsky, and G. Lo, “On dynamic multi-rigidbody contact problems with coulomb friction,” _Zeitschrift Angewandte Mathematik und Mechanik_ , vol. 77, no. 4, pp. 267–279, 1997. 

- [85] V. Acary and B. Brogliato, _Numerical methods for nonsmooth dynamical systems: applications in mechanics and electronics_ . Springer Science & Business Media, 2008. 

- [86] M. Anitescu, “Optimization-based simulation of nonsmooth rigid multibody dynamics,” _Mathematical Programming_ , vol. 105, pp. 113–143, 2006. 

- [87] S. Boyd, N. Parikh, E. Chu, B. Peleato, J. Eckstein, _et al._ , “Distributed optimization and statistical learning via the alternating direction method of multipliers,” _Foundations and Trends® in Machine learning_ , vol. 3, no. 1, pp. 1–122, 2011. 

- [88] S. Mehrotra, “On the implementation of a primal-dual interior point method,” _SIAM Journal on optimization_ , vol. 2, no. 4, pp. 575–601, 1992. 

- [89] J. Nocedal and S. J. Wright, _Numerical optimization_ . Springer, 1999. 

- [90] N. Parikh, S. Boyd, _et al._ , “Proximal algorithms,” _Foundations and trends® in Optimization_ , vol. 1, no. 3, pp. 127–239, 2014. 

- [91] T. Preclik, _Models and algorithms for ultrascale simulations of nonsmooth granular dynamics_ . Friedrich-Alexander-Universitaet ErlangenNuernberg (Germany), 2014. 

- [92] S. Boyd and L. Vandenberghe, “Localization and cutting-plane methods,” _From Stanford EE 364b lecture notes_ , 2007. 

- [93] J. Carpentier, Q. Le Lidec, and L. Montaut, “From compliant to rigid contact simulation: a unified and efficient approach,” in _20th edition of the “Robotics: Science and Systems”(RSS) Conference_ , 2024. 

- [94] B. Stellato, G. Banjac, P. Goulart, A. Bemporad, and S. Boyd, “OSQP: an operator splitting solver for quadratic programs,” _Mathematical Programming Computation_ , vol. 12, no. 4, pp. 637–672, 2020. 

- [95] M. Renouf, V. Acary, and G. Dumont, “3d frictional contact and impact multibody dynamics. a comparison of algorithms suitable for realtime applications,” in _Mutlibody Dynamics 2005, ECCOMAS Thematic Conference_ , 2005. 

- [96] P.-A. Léziart, T. Flayols, F. Grimminger, N. Mansard, and P. Souères, “Implementation of a Reactive Walking Controller for the New OpenHardware Quadruped Solo-12,” in _2021 IEEE International Conference on Robotics and Automation - ICRA_ , (Xi’an, China), May 2021. 

- [97] H. J. T. Suh, T. Pang, and R. Tedrake, “Bundled gradients through contact via randomized smoothing,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, pp. 4000–4007, 2022. 

- [98] Q. Le Lidec, F. Schramm, L. Montaut, C. Schmid, I. Laptev, and J. Carpentier, “Leveraging randomized smoothing for optimal control of nonsmooth dynamical systems,” _Nonlinear Analysis: Hybrid Systems_ , vol. 52, p. 101468, 2024. 

- [99] E. Heiden, D. Millard, E. Coumans, Y. Sheng, and G. S. Sukhatme, “NeuralSim: Augmenting differentiable simulators with neural networks,” in _Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)_ , 2021. 

