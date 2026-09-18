# **Convex and analytically-invertible dynamics with contacts and constraints: Theory and implementation in MuJoCo** 

Emanuel Todorov 

**_Abstract_ — We describe a full-featured simulation pipeline implemented in the MuJoCo physics engine. It includes multi-joint dynamics in generalized coordinates, holonomic constraints, dry joint friction, joint and tendon limits, frictionless and frictional contacts that can have sliding, torsional and rolling friction. The forward dynamics of a 27-dof humanoid with 10 contacts are evaluated in 0.1 msec. Since the simulation is stable at 10 msec timesteps, it can run 100 times faster than real-time on a single core of a desktop processor. Furthermore the entire simulation pipeline can be inverted analytically, an order-ofmagnitude faster than the corresponding forward dynamics. We soften all constraints, in a way that avoids instabilities and unrealistic penetrations associated with earlier spring-damper methods and yet is sufficient to allow inversion. Constraints are imposed via impulses, using an extended version of the velocitystepping approach. For holomonic constraints the extension involves a soft version of the Gauss principle. For all other constraints we extend our earlier work on complementarity-free contact dynamics – which were already known to be invertible via an iterative solver – and develop a new formulation allowing analytical inversion.** 

## I. INTRODUCTION 

Contacts enable robots to interact with the environment and get a job done. Yet their discontinuous nature complicates simulation, planning and control. One way to sidestep these complications is to focus on the smooth dynamics in between contact events, and handle the transitions via problem-specific and often adhoc methods that tend to limit the capabilities of the robot. Another way is to smooth the contacts using spring-dampers. Here we do not refer to detailed models of material deformations (which are accurate yet slow), but rather to phenomenological spring-damper contact models in the context of rigid-body dynamics. That approach has been superseded by the velocity-stepping complementarity approach [1], [2], where the contact impulse (i.e. the integral of the contact force over the simulation timestep) is computed by solving a linear or nonlinear complementarity problem. Apart from its mathematical elegance, this approach avoids instabilities and unrealistic penetrations and handles interactions among simultaneous contacts – allowing much larger timesteps. However it also has shortcomings: it calls for a computation that is NPhard in its exact form [3], and furthermore it only solves the simulation problem while planning and control remain difficult due to contact discontinuities. 

This work was supported by the NSF and DARPA. E. Todorov is with the departments of Applied Mathematics and Computer Science & Engineering, University of Washington. Thanks to Yuval Tassa for discussions and comments on the manuscript. 

## _A. Complementarity-free contact dynamics_ 

The shortcomings of the now-standard complementarity approach motivated complementarity-free methods, developed independently in [4] and [5]. The idea is to relax the strict complementarity condition and instead enforce it approximately. This relaxation transforms the NP-hard problem into a convex optimization problem: a conic program when the friction cone is treated exactly, and a quadratic program when the cone is approximated with a pyramid. A systematic analysis of the effects of this approximation for complex robots remains to be done. Nevertheless, synthetic tests [6] as well as experience with model-based control [7] indicate that the approximation is accurate. Note also that the complementarity formulation is not necessarily a gold standard [8]. All contact models presently used in rigidbody simulations are phenomenological, and the only way to validate them is to measure the contact interactions between real robots and their environment – which is rarely done. Contact softness in particular may be better modeled by the complementarity-free approach. Such softness arises from regularization terms that are also essential for inversion. 

## _B. Inverse dynamics with contacts and constraints_ 

The goal of inverse dynamics it to compute the control forces _and_ constraint impulses given the positions, velocities and accelerations. This is complicated by the fact that rigidbody contact dynamics are not actually invertible. Consider pushing against a wall. The contact force cannot be recovered from the kinematics, unless of course we measure the material deformations – but such deformations are ignored in the rigid-body approximation and in the complementarity approach. Indeed one of the notable advantages of the complementarity approach is that it considers the control force (as well as all other non-contact forces) before deciding what contact impulse to apply. This avoids penetration, but also makes it impossible to invert the dynamics or smooth the contacts. If on the other hand we were to use springdampers, the contact dynamics would be smooth and trivially invertible – but as mentioned above, spring-dampers have their own limitations that tend to outweigh their advantages. 

Our complementarity-free approach [4] combines the best of both worlds: it allows smoothing and inversion, and at the same time considers both the inertia and the control forces in computing the contact impulses. The related approach [5] is not amenable to inversion because it uses a two-step optimization method, reminiscent of the staggered projection method developed for complementarity problems [3]. 

II. FORWARD DYNAMICS 

## _A. Notation_ 

Throughout the paper we use the following notation: 

|_q_<br>_v_|joint position<br>joint velocity|
|---|---|
|_u_|control force|
|_h_|discrete timestep|
|_D_|armature, implicit damping inertia|
|_M_(_q_)|total joint-space inertia|
|_c_(_q, v_)|gravity, Coriolis, centripetal forces|
|_p_(_q, v_)|spring-dampers, other passive forces|
|_J_E(_q_)|equality constraint Jacobian|
|_f_E(_q, v, u_)|equality constraint impulse|
|_J_(_q_)|contact Jacobian|
|_f_(_q, v, u_)<br>|contact impulse|
|v<sup>+</sup>_,_v<sup>_−_</sup>_,_v<sup>_∗_</sup>|impulse-space velocities defined later|



Since the treatment of equality constraints and contacts is related, we use the same symbols ( _f, J_ ) and the subscript E<sup>todistinguishbetweenthetwo.Inaddition,thefollowing</sup> model parameters will be defined later: 



Multiple friction coefficients are needed to handle tangential, torsional and rolling friction; thus _d_ can be up to 5. 

## _B. Overall computation_ 

We consider multi-joint systems subject to holonomic constraints such as loop joints, and contact impulses arising from dry joint friction, joint and tendon limits, frictionless and frictional contacts. The continuous-time dynamics are 



We have not divided by _dt_ because _f_ E _, f_ are impulses. 

The computation is carried out in two phases. Phase I corresponds to smooth dynamics and preparation for impulse dynamics, and relies on standard methods [9]. Phase II corresponds to impulse dynamics; it is the more the challenging part and is also where the novelty of our approach lies. 

In Phase I we compute _M, D, c, p, J_ E _, J_ . In our implementation in the MuJoCo physics engine, _M_ ( _q_ ) _−D_ is computed with the Composite Rigid Body (CRB) algorithm, then _D_ is added and the resulting _M_ is LDL-factorized taking advantage of branch-induced sparsity. _c_ ( _q, v_ ) is computed with the Recursive Newton-Euler (RNE) algorithm – which is actually an algorithm for inverse dynamics: 



Here we use it to compute RNE ( _q, v,_ 0) = _c_ ( _q, v_ ). Note that CRB and RNE do not take into account the extra inertia _D_ , which is why we have to add it to the output of these algorithms to obtain the total inertia _M_ . The contact Jacobian 

_J_ ( _q_ ) is computed using collision detection. The quantities _p_ ( _q, v_ ) _, J_ E ( _q_ ) are computed from analytical formulas or user callbacks. The extra diagonal inertia _D_ models the armature inertia of motors as well as implicit damping. 

We do not use Featherstone’s _O_ ( _n_ ) forward dynamics. This is because the impulse phase needs the inertia matrix to be computed and factorized, and once this is done, using RNE is faster. Thus our method has _O_ ( _n_<sup>3</sup> ) worstcase performance. However, as Featherstone showed in [10], branch-induced sparsity typical for robotic systems makes the present method very similar to his _O_ ( _n_ ) method. 

In Phase II we compute ( _f_ E _, f_ ) given ( _q, v, u_ ) as explained in the following subsections. This is done in two stages: we first eliminate _f_ E by expressing it as a function _f_ , and then project the dynamics in contact space and solve for _f_ . 

Before proceeding with the impulse computation, we need to transition to discrete time. Let _h >_ 0 be the timestep. Replace _dv_ ( _t_ ) with _v_ ( _t_ + _h_ ) _− v_ ( _t_ ). All relevant quantities except _v_ ( _t_ + _h_ ) are defined at time _t_ , thus we omit _t_ and write _v_ ( _t_ + _h_ ) as _v_<sup>_′_</sup> . The discrete-time dynamics are 





Now that we have transitioned to discrete time, we can clarify how the implicit damping terms in _D_ are computed. Recall that “implicit” refers to evaluating quantities at the next timestep rather than the current timestep, and makes numerical integration more stable. In the case of a damped 2nd-order system _M_ ˙ _v_ = _−Bv_ , implicit damping is implemented in discrete time as 



These dynamics can be written in the familiar (explicit) form 



by modifying the inertia as _M_ = _M_ + _Bh_ . Thus we implement implicit damping by defining _D ≡_ armature+ _Bh_ , and adding _−Bv_ to the passive force _p_ ( _q, v_ ). We require _D_ to be diagonal and non-negative, so as to preserve the sparsity and positive-definiteness of _M_ . 

## _C. Constraint dynamics_ 

The dynamics of equality-constrained systems can be obtained from the Gauss principle [11], which we now recall. Suppose we have unconstrained continuous-time dynamics _Ma_ = _τ_ subject to acceleration constraints _J_ E _a_ = _a_<sup>_∗_</sup> E<sup>.</sup> Then, given _M, τ, J_ E _, a_<sup>_∗_</sup> E<sup>,theconstrainedaccelerationisthe</sup> solution to the convex optimization problem 



Since we aim to invert the dynamics later, and hard constraints are non-invertible, we must soften the constraints somehow. We propose to do this by softening the Gauss principle, i.e. replacing the hard constraint with a soft penalty. 

_Proposition._ The acceleration of the constrained system is defined as the solution to the convex optimization problem 



where the regularizer _R_ E is a diagonal positive matrix. 

In the limit _R_ E _→_ 0 the solution to problem (5) converges to the solution to problem (4), which is non-invertible. However for any _R_ E _≻_ 0 the resulting dynamics are invertible, as shown by construction later. 

We now return to discrete time and impose a soft constraint on velocity rather than acceleration: _J_ E _v_<sup>_′_</sup> = v<sup>_∗_</sup> E<sup>(</sup><sup>_q, v_).</sup> Here v<sup>_∗_</sup> E<sup>isthedesirednext-stepvelocityinconstraintspace,</sup> computed by any suitable constraint stabilization mechanism. Our specific choice will be described later. 

**Theorem 1.** The dynamics under the proposed soft Gauss principle are 



where _M_<sup>�</sup> and _v_ � are defined as 



_Proof._ Apply the soft Gauss principle with 



Solving (5) analytically yields (6, 7). ■ 

We can interpret _M_<sup>�</sup> as the apparent inertia that takes into account the constraints, and _v_ � as the next-step velocity that takes into account all forces except for the contact impulse. 

For hard constraints the dynamics remain in the general form (6), but the definitions (7) are replaced with 



where _A_ E _≡ J_ E _M_<sup>_−_1</sup> _J_ E<sup>_T_istheinverseinertiainconstraint</sup> space. This can be shown by solving (4), or by taking the limit _R_ E _→_ 0 and using the matrix inversion lemma. 

Equations (6, 7) represent modified dynamics which implicitly take the constraints into account. We did not compute the impulse _f_ E explicitly because it can only be computed after _v_<sup>_′_</sup> is known, i.e. in the context of inverse dynamics. 

_D. Contact dynamics_ 

We now have everything in place for the contact computation stage. First we project (6) in contact space via multiplication by the contact Jacobian _J_ : 



Then we write the contact-space dynamics as 



where _A ≡ JM_<sup>�</sup><sup>_−_1</sup> _J_<sup>_T_</sup> is the inverse of the apparent inertia, v<sup>_−_</sup> _≡ Jv_ � is the next-step velocity before the contact impulse, 

and v<sup>+</sup> _≡ Jv_<sup>_′_</sup> is the next-step velocity after the contact impulse, all expressed in contact space. 

To complete the forward dynamics computation we have to solve (8) for ( _f,_ v<sup>+</sup> ) given ( _A,_ v<sup>_−_</sup> ). This involves twice as many unknowns as the number of equations in (8), thus we need additional information – which comes in the from of inequality constraints reflecting the laws of contact and friction. We now introduce these inequalities, and at the same time explain what exactly is included in the contact space. 

In our current implementation in MuJoCo the contact solver can handle three types of objects: friction loss in the joints, limits on joint angles and distances, and frictional contacts. The elements _fi_ of the vector _f_ satisfy different inequality constraints depending on the type of object they represent, as follows: 





Assembling the left hand sides of the above inequalities in the vector _φ_ ( _f_ ), we can write (9) as _φ_ ( _f_ ) _≥_ 0. 

In (9) subscripts denote vector elements as usual, while _i_ in brackets denotes parameters of the object whose data starts at position _i_ in the vector _f_ . In the case of friction loss, _η_ ( _i_ ) is the (load-independent) joint torque that is lost to friction before the joint starts accelerating. Limits can be defined for revolute, prismatic and ball joints (the latter limits are cylinders in the angle-axis representation of the joint quaternion), as well as for tendon lengths (tendons are strings whose spatial path is defined by via points and wrapping objects), and distances between geometric shapes (i.e. frictionless contacts). 

In the case of frictional contacts, _d_ ( _i_ ) _∈{_ 2 _,_ 3 _,_ 5 _}_ is the dimensionality of the friction space and _µj_ ( _i_ ) are the friction coefficients in the _d_ ( _i_ ) dimensions. The contact contributes 1 + _d_ ( _i_ ) elements to the vector _f_ with the following semantics. Consider a 3D frame whose first axis is aligned with the contact normal. Impulses ( _fi, fi_ +1 _, fi_ +2) cause relative translation along the contact frame axes, while ( _fi_ +3 _, fi_ +4 _, fi_ +5) cause relative rotation around the axes. Thus _fi_ is the normal impulse, ( _fi_ +1 _, fi_ +2) is the tangential friction impulse, _fi_ +3 is the torsional friction impulse, and ( _fi_ +4 _, fi_ +5) is the rolling friction impulse. The contact inequalities in (9) specify that the normal impulse must be non-negative, and that the impulse vector must lie within the elliptical friction cone. In the special case when _d_ ( _i_ ) = 2 and _µ_ 1 ( _i_ ) = _µ_ 2 ( _i_ ) = _µ_ ( _i_ ), this reduces to the more familiar definition of a friction cone: 



We now return to the computation of the contact impulse _f_ and next-step velocity v<sup>+</sup> . Conditions (8, 9) are still 

insufficient to determine a unique solution. There are two paths forward: complementarity-based and complementarityfree. The former approach introduces additional constraints (complementarity conditions) to obtain a unique solution. For example, the contact normal inequality _fi ≥_ 0 is augmented with v _i_<sup>+</sup> _≥_ 0 and _fi_ v _i_<sup>+</sup> = 0. In the presence of frictional contacts, this approach yields an NP-hard problem in the forward dynamics. Furthermore its inverse cannot be defined. Thus we will not pursue it further in this paper. Instead we will rely on the complementarity-free approach. 

## _E. Complementarity-free contact dynamics_ 

In our approach to contact dynamics [4], the impulse _f_ is defined via minimization of the (regularized and offset) next-step kinetic energy subject to (9): 



The regularizer _R_ is a diagonal positive matrix, which is needed because _A_ can be singular and also because it introduces smoothing that is necessary to define the inverse later. Kinetic energy is measured relative to a desired contact velocity v<sup>_∗_</sup> which can be computed by any suitable contact stabilization mechanism (details below). 

Substituting (8) in (10), the impulse _f_ is found as 



This is a convex optimization problem and has a unique global minimum. We solve it using our (yet unpublished) generalization of the projected Gauss-Seidel method (GPGS) that can handle cone and pyramid constraints. 

III. INVERSE DYNAMICS 

## _A. Overall inverse computation_ 

Given ( _q, v, v_<sup>_′_</sup> ), we compute _J, J_ E _, D, p,_ v<sup>_∗_</sup> _,_ v<sup>_∗_</sup> E<sup>asinthe</sup> forward dynamics, and define _v_ ˙ _≡_ ( _v_<sup>_′_</sup> _− v_ ) _h_<sup>_−_1</sup> . Then we apply the RNE algorithm to compute the sum of all forces acting on the system except for the Coriolis, centripetal and gravity force _c_ ( _q, v_ ) and the extra inertial force _D_ ˙ _v_ . More precisely, from (1) and (2) we have 



Once the impulses _f, f_ E are computed as explained below, the control force _u_ is recovered from (12) and we are done. 

Note that we did not need to compute or factorize the inertia matrix _M_ . It will turn out that _M_ is not needed to recover the impulses either. 

## _B. Inverse constraint dynamics_ 

Recall that in the forward dynamics we did not compute the constraint impulse _f_ E, but only modified the dynamics so as to take it into account implicitly. Here _f_ E can be computed explicitly because _v_<sup>_′_</sup> is known. 

**Theorem 2.** The constraint impulse _f_ E which caused the observed state transition ( _q, v_ ) _→ v_<sup>_′_</sup> satisfies 



_Proof._ Combining (6) and (7) yields 



Subtracting this from (3) yields the result (13). ■ 

We can further recover the actual _f_ E if we assume that the equality constraints are non-redundant (i.e. that _J_ E has full rank). However this assumption is not needed to complete the inverse dynamics computation, because (12) only depends on _J_ E<sup>_Tf_Ewhichwealreadyhavefrom(13).</sup> 

## _C. Inverse contact dynamics: General case_ 

In our previous work [4] we showed how the convex contact model described above can be inverted in an unconstrained setting, by converting the inequality constraints into log-barrier penalty functions. Here we present a more general version of this result, allowing hard inequality constraints – which in turn make it possible to use projected and active-set methods in the forward dynamics. We first state the abstract result and then specialize it to dynamic simulation. 

**Theorem 3.** Let _A ∈_ R<sup>_n,n_</sup> be symmetric positive semidefinite, _r, s_ : R<sup>_n_</sup> _→_ R be convex, _φ_ : R<sup>_n_</sup> _→_ R<sup>_n_</sup> be convex, and _b, c ∈_ R<sup>_n_</sup> . Define _x_<sup>_∗_</sup> _b_<sup>_, x_</sup> _c_<sup>_∗∈_R</sup><sup>_n_asthe(uniqueglobal)</sup> solutions to the following convex optimization problems: 







Then _Ax_<sup>_∗_</sup> _b_<sup>+</sup><sup>_b_=</sup><sup>_c_implies</sup><sup>_x∗_</sup> _b_<sup>=</sup><sup>_x_</sup> _c_<sup>_∗_.</sup> _Proof_ **.** Since _x_<sup>_∗_</sup> _b_<sup>_, x_</sup> _c_<sup>_∗_are defined as solutions to convex opti-</sup> mization problems, they can be equivalently characterized by the corresponding Karush-Kuhn-Tucker (KKT) conditions. The KKT conditions for problem (14a) are: 





The KKT conditions for problem (14b) are: 





These two sets of conditions are identical when _Ax_ + _b_ = _c_ . Therefore, if the solution _x_<sup>_∗_</sup> _b_<sup>tothefirstproblemsatisfies</sup> _Ax_<sup>_∗_</sup> _b_<sup>+</sup><sup>_b_=</sup><sup>_c_,then</sup><sup>_x_</sup> _b_<sup>_∗_willalsobethesolutiontothesecond</sup> problem, and so _x_<sup>_∗_</sup> _b_<sup>=</sup><sup>_x_</sup> _c_<sup>_∗_.■</sup> 

This theorem can be applied to complementarity-free contact dynamics by identifying _x_ with _f_ , _b_ with v<sup>_−_</sup> , _c_ with v<sup>+</sup> , and absorbing the linear term _−f_<sup>_T_</sup> v<sup>_∗_</sup> in _r_ ( _f_ ). Thus we have the following corollary. 

_Corollary._ Given _A,_ v<sup>_∗_</sup> _,_ v<sup>_−_</sup> , the impulse is computed by solving the (forward dynamics) convex optimization problem 



Given _A,_ v<sup>_∗_</sup> _,_ v<sup>+</sup> , the impulse is computed by solving the (inverse dynamics) convex optimization problem 

This general problem cannot be solved analytically because both the cone and the distance metric are elliptical, making the problem equivalent to finding the roots of a polynomial of order 2 ( _d_ + 1). Our goal then is to identify conditions that simplify the problem, in particular make the cone circular and the metric Cartesian. The metric is made Cartesian by the change of variables 



Both computations yield the same impulse _f_ . 

## _D. Inverse contact dynamics: Analytical special case_ 



We now focus on the specific formulation (11) used in the forward dynamics, where instead of a general impulse regularizer _r_ ( _f_ ) we had 

The minimization problem now becomes 





where the transformed friction cone _C_<sup>�</sup> is 

In this case the inverse can be computed analytically. In particular, problem (14b) can be written in least-squares form 



This cone is circular when _µ_<sup>2</sup> _j_<sup>_rj_=</sup><sup>_const_,whichcanbe</sup> enforced by requiring that there exists a scalar _µ_ � such that 

where the vector _y_ is defined as 







Including a general velocity regularizer _s_ (v<sup>+</sup> ) would merely add a constant to _y_ and still allow the inverse to be computed analytically, but we omit it here so as to match the forward dynamics formulation (11) used by our GPGS solver. 

The resulting optimization problem can now be solved analytically. If _y_ � _∈ C_<sup>�</sup> then _x_ � = _y_ � and we are done. Otherwise _x_ � lies on the surface of the cone _C_<sup>�</sup> and can be found via Lagrange multipliers: there exists a scalar _λ_ such that 

We now make a key observation: the terms corresponding to the different objects used to construct the contact space are decoupled, both in the objective function and in the constraints. Thus problem (15) decomposes into a collection of smaller problems – one for each friction loss, limit, and frictional contact object. These smaller problems can be solved analytically as follows. 



We can find _λ_ by expressing _x_ � as a function of _y_ � and _λ_ : 



**Theorem 4** _._ The solution to the inverse dynamics optimization problem (15) is 

Substituting this _x_ � in the surface equality constraint and solving for _λ_ yields two general solutions: 

friction: _fi_ = max ( _−η_ ( _i_ ) _,_ min ( _η_ ( _i_ ) _, yi_ )) limit: _fi_ = max (0 _, yi_ ) contact: _fi, · · · , fi_ + _d_ ( _i_ ) = ConeProject ( _y, i_ ) 



ConeProject extracts the contact-specific data _yi, · · · , yi_ + _d_ ( _i_ ) from _y_ , and then calls Algorithm 5 below to compute the nearest vector within the friction cone. 

with corresponding vectors _x_ �<sup>_±_</sup> given by (18). If both vectors have non-negative first components � _x_ �<sup>_±_</sup> 0<sup>_≥_0</sup> �, the optimal solution is the one closer to _y_ �. If only one vector has nonnegative first component, it is the optimal solution. If both have negative first components, the optimal solution is � _x_ = 0. 

_E. Projection on a friction cone_ 

Here we develop the analytical procedure for projecting a vector on a friction cone with certain properties. Let _C_ be an elliptical cone defined as 

We must also handle two special cases where the above general method involves division by 0. If _y_ �0 = 0 we have 1 + _µ_ �<sup>2</sup> _λ_ = 0. In that case the solution can be shown to be 





We seek the vector _x ∈C_ which minimizes the weighted distance to a given vector _y ∈_ R<sup>_d_+1</sup> : 



We now clarify how the contact model can be constructed so as to obey the restriction (17). The regularizing weights _r_ 0 _, · · · , rd_ together with the friction coefficients _µ_ 1 _, · · · , µd_ and the transformed coefficient _µ_ � appear to have 2 _d_ + 2 

Here _r ∈_ R<sup>_d_+1</sup> is a vector of positive weights, i.e. the diagonal of the matrix _R_ above. Throughout this section _k_ is an index starting at 0 while _j_ is an index starting at 1. 

degrees of freedom, however _d_ of them are removed due to (17), leaving us with _d_ + 2 degrees of freedom. The friction coefficients clearly need to be under the control of the user, thus only two of the regularizers can be specified independently. It is then natural to construct the contact model by specifying the following independent parameters: 



Defining 



where _⟨.⟩_ denotes the mean value, we can verify that (17) is satisfied and furthermore _r_ F = _⟨rj⟩_ as intended. We now summarize the algorithm. 

**Algorithm 5.** Given the contact model parameters (21) and the vector _y_ , compute the vector _x_ as follows: 

- 1) if _y_ is inside the friction cone, set _x_ = _y_ and return; 

- 2) if _yj_ = 0 for all _j ≥_ 1, set _x_ = 0 and return; 

- 3) compute _rj_ and _µ_ �<sup>2</sup> from (22); 

- 4) compute _y_ � from (16); 

- 5) if _y_ �0 = 0, compute _x_ � from (20) and go to step 8; 

- 6) compute _x_ �<sup>_±_</sup> from (18, 19); 

- 7) choose the optimal _x_ � among _{x_ �<sup>_±_</sup> _,_ 0 _}_ ; 

- 8) compute _x_ by inverting (16). 

As a sanity check, we generated random optimization problems in this family and compared our analytical solution to the solution found by the MATLAB fmincon iterative solver. The two solutions agreed within the tolerance level specified for the iterative solver. 

## IV. COMPUTATIONAL COMPLEXITY 

Let _n_ = dim( _v_ ) be the number of degrees of freedom and _m_ = dim( _f_ ) the number of impulses. We will ignore holonomic constraints in this analysis because the computational cost is dominated by the contact impulses. 

The forward dynamics involve computing and factorizing the inertia _M_ which is _O_ � _n_<sup>3�</sup> . Computing _A_ = _JM_<sup>_−_1</sup> _J_<sup>_T_</sup> is _O_ � _m_<sup>2</sup> _n_ + _n_<sup>2</sup> _m_ �. Applying the GPGS iterative solver is _O_ � _m_<sup>2</sup> maxiter�. Note however that the branch-induced sparsity of _M_ as well as the sparsity of _J_ make the actual performance better than these worst-case estimates. Our implementation exploits sparsity. The inverse dynamics involve RNE which is _O_ ( _n_ ), as well as our new analytical impulse solver which is _O_ ( _m_ ). We use a precomputed approximation to the diagonal of _A_ to set the regularizer _R_ , avoiding any higher-order operations. Thus the worst-case performance is dominated by the computation of the contact Jacobian _J_ which is _O_ ( _mn_ ). Again, sparsity makes the actual performance better. 

The above computational complexity analysis does not include collision detection – which is identical in both the forward and inverse dynamics. In simulations relevant to robotics, we have found collision detection to be a small fraction of the computational cost. 

V. ANALYSIS AND TUNING OF THE IMPULSE DYNAMICS 

Here we analyze the behavior of the dynamics defined above. We also show how to set the solver parameters _R, R_ E _,_ v<sup>_∗_</sup> _,_ v<sup>_∗_</sup> E<sup>soastoobtainastabilizationmechanism.</sup> 

For contacts we focus on the case when all inequality constraints are inactive, i.e. _φ_ ( _f_ ) _>_ 0 at the solution _f_ found by the impulse solver. Physically this corresponds to nonsliding contacts (modulo contact softness). In that case, from (15) we have 



Note how similar this contact impulse is to the constraint impulse (13), despite the fact that the two were defined and computed differently. This observation motivates analysis in the combined space of constraints and contacts, with coordinates _x_ defined as follows. For constraints, limits and contact normals _xi_ is the violation/penetration distance. For frictional dimensions _xi_ is defined relative to an arbitrary offset (we only care about the velocity in that case). 

Define the Jacobian _J_ , regularization matrix _R_ and desired next-step velocity _x_ ˙<sup>_∗_</sup> in _x_ -space by stacking the corresponding quantities for constraints and contacts: 



Then the velocity and inverse inertia in _x_ -space are 



As before, _x_ ˙<sup>_′_</sup> = _x_ ˙ + _hx_ ¨ will denote the actual next-step velocity. We will also need the _x_ -space acceleration that the non-impulsive forces cause: 



Finally we must decide how the desired next-step velocity _x_ ˙<sup>_∗_</sup> is computed; different choices give rise to different dynamics. Motivated by the idea of Baumgarte stabilization [12], we consider a virtual PD controller that causes acceleration _−B_ ˙ _x −Kx_ . Thus _x_ ˙<sup>_∗_</sup> is defined as 



We now have everything in place to obtain the dynamics. **Theorem 6.** The _x_ -space dynamics are 



_Proof._ Substituting (23) and (13) in (3) yields 



Multiplying by _J M_<sup>_−_1</sup> and using the above definitions, 



Using the definitions of _x_ ˙<sup>_′_</sup> and _x_ ˙<sup>_∗_</sup> yields the result (25). ■ We can now gain a better understanding of what the impulse solver is doing. Suppose we set _R_ = _Aϵ_ for some positive _ϵ_ . Since _A_ and _R_ have the same units (they were added together in (11)), _ϵ_ is a dimensionless constant. Also 





Fig. 1. The two MuJoCo models used in the simulations. Left: single-joint mechanism with dry friction. The arrow shows the contact impulse. Right: 27-dof humanoid. The red cylinders show the active contacts. Joint limits prevent more contacts. 

set _B_ = _B_ (1 + _ϵ_ ) _, K_ = _K_ (1 + _ϵ_ ) for some _B, K_ . Assuming for the moment that _A_ is invertible, (25) becomes 



Therefore in the limit _ϵ →∞_ we have a spring-damper driven by _a_ . In the limit _ϵ →_ 0 the spring-damper becomes autonomous and removes constraint violations regardless of _a_ . The latter limit corresponds to hard constraints and contacts. In practice we use small _ϵ_ . Since our solver implements the above dynamics implicitly, we can get very close to the _ϵ →_ 0 limit without instabilities, numerical errors, or need for small timesteps. 

While (26) is illuminating, it does not apply in general because _A_ can be singular; for example, two frictional contacts on the same body make _A_ singular. Furthermore we cannot set _R_ = _Aϵ_ because we want _R_ to be diagonal, so that the dynamics can be inverted analytically. 

In our implementation we set _R_ to a diagonal matrix: 



Similarly the stiffness and damping are diagonal: 



We can now carry the analysis of (25) further by approximating _A_ with its diagonal, resulting in 



Note that the choice of stiffness and damping coefficients in (28) made the autonomous part of the dynamics criticallydamped, where _κ_<sup>_−_1</sup> is the natural frequency and so _κ_ is the time constant of the _x_ -space dynamics. It is also informative to look at penetrations. If we consider a free-floating object resting on the ground in the presence of gravity _g_ , we have _a_ = _g_ , and so the penetration is 



independent of the mass of the object. 

There are two final caveats. First, the _Rii_ corresponding to the friction dimensions of each contact must be further adjusted so as to satisfy (22). Second, in friction dimensions we only care about velocity, thus we set the corresponding _Kii_ = 0. In that case the velocity decays to 0 at rate 2 _κ_<sup>_−_1</sup> , and _κ_ again has the meaning of a time constant. 



<!-- Start of picture text -->
Time (2 sec) Time (2 sec)<br>Friction impulse Contact impulse<br><!-- End of picture text -->

Fig. 2. Comparison of the friction impulse and contact impulse computed by the forward (black) and inverse (orange) dynamics, while the singlejoint system was being perturbed randomly. The two curves in each plot are within 1E-5 of each other, thus the difference is not visible. 

To summarize, the user specifies the impulse regularization scaling _ϵ_ and the error reduction time constant _κ_ , and then the solver parameters _R, R_ E _,_ v<sup>_∗_</sup> _,_ v<sup>_∗_</sup> E<sup>arecomputedautomatically</sup> using (27, 28, 24) with the above modifications. 

Instead of using a diagonal approximation, we can obtain a stabilization mechanism that is closer to critical damping as follows. Define a diagonal _R_ as above. Now solve the following equations for _B_ and _K_ : 



If _A_ is invertible these equations can be solved exactly, resulting in exact critical damping. If not, then a pseudoinverse can be used. The resulting _B_ and _K_ are no longer diagonal, but that does not complicate the computation. 



## _A. Correctness_ 

We demonstrate numerically the correctness of the inversion using a single-joint mechanism (Figure 1 left) with two impulses: dry friction in the joint and contact with the ground. Figure 2 compares these impulses as computed by the forward and inverse dynamics, while the mechanism is perturbed with random control forces. 

Recall that the impulses in the forward dynamics are computed with our GPGS iterative solver which may not discover the optimal solution within the number of iterations we allow in runtime. Indeed for more complex simulations the forward and inverse do not agree so closely, making the inverse dynamics approach more appealing for optimal control and estimation applications. 

## _B. Speed of computation_ 

Figure 3 illustrates the computational efficiency of our algorithms and their implementation in MuJoCo. The tests were done on an Intel i7-3930K processor, Windows 7, single-threaded computation taking advantage of AVX instructions (with custom BLAS-like routines). We dragged the humanoid model around in the virtual environment using a 3D mouse. This generated many different contact configurations with different Jacobian size. We run both the forward and inverse dynamics and timed them using highresolution timers. The timing data and size of the Jacobian at each simulation step were saved in a file. Afterwards, we found all simulation steps in which the Jacobian had a given 



<!-- Start of picture text -->
500 20<br>400 Forward(50) / Inverse<br>15<br>300 Forward(50)<br>10<br>200<br>5<br>100 Forward(5) Forward(5) / Inverse<br>Inverse<br>0 0<br>0 20 40 60 80 100 0 20 40 60 80 100<br>Size of contact Jacobian Size of contact Jacobian<br>Speedup factor<br>CPU time per step (microsec)<br><!-- End of picture text -->

Fig. 3. Comparison of the speed of the forward and inverse dynamics computations for the humanoid. Left: CPU time per simulation step is shown for different sizes of the contact Jacobian. The PGS iterative solver in the forward dynamics was run for 5 or 50 iterations. Right: the speedup factor is the ratio of forward dynamics CPU time to inverse dynamics CPU time. 

size (plotted on the x-axis in Figure 3), and computed the median of the corresponding CPU times. We performed the test twice, with 5 and 50 iterations of the GPGS solver in the forward dynamics. To generate larger Jacobians we enabled all contact friction directions. For 10 contacts with sliding friction only, the Jacobian size would be 30. 

We find the results in Figure 3 quite remarkable. On a single core of a desktop processor, we can evaluate the inverse dynamics of a 27-dof humanoid subject to 100 impulses in 30 microseconds. In the absence of impulses the time goes down to 10 microseconds. Since the simulation timestep is 10 milliseconds, the inverse dynamics are being computed between 300 and 1000 times faster than real time depending on the number of impulses. The forward dynamics are slower – by an order of magnitude – but still much faster than real time. Note that increasing the number of GPGS iterations from 5 to 50 is expensive with large number of impulses, but the inverse dynamics are faster regardless of the number of GPGS iterations. This is because computing the full _A_ matrix is avoided. 

## VII. CONCLUSIONS AND FUTURE WORK 

We described a full-featured simulation pipeline for multijoint dynamics subject to constraints and contacts. Forward simulation requires an iterative solver, while inverse dynamics are computed analytically and faster. 

The inversion is possible because our formulation allows a certain amount of softness. One can think of the impulses as being generated by smart spring-dampers, which are aware of each other and furthermore scale their stiffness and damping automatically with inertia. The forward formulation considers the interactions among all impulses, involving the dense matrix _A_ and the diagonal regularizer _R_ . The mathematical relation between the forward and inverse is such that the _A_ matrix is no longer needed in the inverse, and we are left only with the _R_ matrix allowing us to decompose the problem. 

Softness is controlled by the two parameters _ϵ, κ_ whose effects we analyzed. Small values of these parameters make the forward dynamics harder to simulate (requiring smaller timesteps or larger number of solver iterations). They also make the output of the inverse dynamics more sensitive to 

the input, but the actual computation is not affected since it always relies on the same analytical procedure. 

Our softness parameters _ϵ, κ_ are generally related to the constraint-force mixing (CFM) and error reduction parameter (ERP) introduced in the Open Dynamics Engine (ODE), although the specifics are different. CFM regularization in ODE is applied to the full system while we only apply regularization in the impulse space, and furthermore the problem solved by ODE does not become convex even after regularization. ERP implements a first-order constraint stabilization mechanism while we use a second-order mechanism. 

Our results have many potential applications in data analysis, simulation, estimation and control. We have already leveraged the new analytical inverse dynamics in the context of state estimation, using it to enforce a physics consistency prior [13]. Future applications to optimal control are particularly exciting. We were recently able to synthesize complex full-body movements with direct trajectory optimization automatically, without relying on motion capture or manual scripting [14]. While this was done offline, we estimate that in model-predictive control (MPC) mode our existing optimizer will be an order of magnitude slower than real time. The analytical inverse dynamics developed here may provide the missing order of magnitude speedup. If we could replicate [14] in MPC mode, it is likely to transform robotic control as well as interactive games. 

## REFERENCES 

- [1] D. Stewart and J. Trinkle, “An implicit time-stepping scheme for rigid-body dynamics with inelastic collisions and coulomb friction,” _International Journal Numerical Methods Engineering_ , vol. 39, pp. 2673–2691, 1996. 

- [2] M. Anitescu, F. Potra, and D. Stewart, “Time-stepping for threedimensional rigid body dynamics,” _Computer Methods in Applied Mechanics and Engineering_ , vol. 177, pp. 183–197, 1999. 

- [3] D. Kaufman, S. Sueda, D. James, and D. Pai, “Staggered projections for frictional contact in multibody systems,” _ACM Transactions on Graphics_ , vol. 164, pp. 1–11, 2008. 

- [4] E. Todorov, “A convex, smooth and invertible contact model for trajectory optimization,” _ICRA_ , 2011. 

- [5] E. Drumwright and Shell, “Modeling contact friction and joint friction in dynamic robotic simulation using the principle of maximum dissipation,” _International Workshop on the Algorithmic Foundations of Robotics_ , 2010. 

- [6] E. Drumwright and E. Shell, “An evaluation of methods for modeling contact in multibody simulation,” _ICRA_ , 2011. 

- [7] Y. Tassa, T. Erez, and E. Todorov, “Synthesis and stabilization of complex behaviors through online trajectory optimization,” _IROS_ , 2012. 

- [8] A. Chatterjee and A. Ruina, “A new algebraic rigid body collision law based on impulse space considerations,” _Journal of Applied Mechanics_ , 1998. 

- [9] R. Featherstone, _Rigid Body Dynamics Algorithms_ . Springer, 2008. 

- [10] ——, “Efficient factorization of the joint-space inertia matrix for branched kinematic trees,” _International Journal of Robotics Research_ , 2005. 

- [11] F. Udwadia and R. Kalaba, “A new perspective on constrained motion,” _Proceedings of the Royal Society_ , 1992. 

- [12] J. Baumgarte, “Stabilization of constraints and integrals of motion in dynamical systems,” _Computer Methods In Applied Mechanics And Engineering_ , 1972. 

- [13] K. Lowrey, Y. Tassa, T. Erez, S. Kolev, and E. Todorov, “Physicallyconsistent sensor fusion for contact-rich behaviors,” _manuscript under review_ , 2014. 

- [14] I. Mordatch, E. Todorov, and Z. Popovic, “Discovery of complex behaviors through contact-invariant optimization,” _SIGGRAPH_ , 2012. 

