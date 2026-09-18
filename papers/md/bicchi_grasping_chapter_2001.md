<!-- page 1 -->
Chapter 1
Robotic Grasping and
Manipulation
In this chapter, we consider problems that arise in designing, building, planning,
and controlling operations of robotic hands and end–eﬀectors. The purpose
of such devices is often manifold, and it typically includes grasping and ﬁne
manipulation of ojects in an accurate, delicate yet ﬁrm way. We survey the
state-of-the-art reached by scientiﬁc research and literature about the problems
engendered by these often conﬂicting requirements, and the work that has been
done in this area over the last two decades. Because of space limitations, the
chapter does not attempt at providing a survey of the technology of robot
hands, but rather it is oriented towards covering the theoretical framework,
analytical results, and open problems in robotic manipulation.
1.1
Introduction
In many roboticists, the admiration for what nature accomplishes in everiday’s
functions of human beings and animals is the original stimulus for their research
in emulating these capabilities in artiﬁcial life.
Among the many awesome
realizations of nature, few of the human abilities distinguish man from animals
as deeply as manipulation and speech.
Indeed, there are animals that can
see, hear, walk, swim, etc.
more eﬀcicently than men - but language and
manipulation skills are peculiar of our race, and constitute a continuing source
of amazement for scientists.
In this chapter, we will consider in detail the
implementation of artiﬁcial systems to replicate in part the manipulating ability
of the human hand.
The three most important functions of the human hand are to explore, to
restrain, and to precisely move objects. The ﬁrst function falls within the realm
of haptics, an active research area in its own merits [46]. We will not attempt
an exhaustive coverage of this area. The work in robot hands has mostly tried
to understand and to emulate the other two functions. We will distinguish
1


<!-- page 2 -->
2
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
Figure 1.1: The University of Bologna dextrous hand [64]
between the task of restraining objects, sometimes called grasping or ﬁxturing,
and the task of manipulating objects with ﬁngers (in contrast to manipulation
with the robot arm), sometimes called dexterous manipulation.
While grippers and ﬁxtures have been used extensively in industry, one
can argue that the ﬁeld of robot grasping started with the work of Asada and
Hanafusa [4] and Salisbury’s ﬁrst three-ﬁngered robotic hand [61]. Since then,
many hand designs have been proposed, ranging from rather simple devices
to very sophisticated multiﬁngered hands such as the Utah-MIT hand [41].
Extensive surveys on robot hand systems are for instance those reported in
[31, 37, 71, 93], and more recently [1, 75, 7].
In robot hand design, it can be observed that there are two prevailing
philosophies, which can be identiﬁed with an anthropomorphic vs. a minimal-
istic approach to design. While the former philosophy basically attempts at
replicating the human hand capabilities by imitating its mechanical structure,
the latter focuses on realization of some desirable grasping or manipulation fea-
tures by purposeful design of mechanisms that have no intentional resemblance
with any biological system. In the latter group, there have been a number
of eﬀorts focussing on reduced-complexity multiﬁngered hands.
Two exam-
ples of robot hands inspired to the two approaches and developed by groups
participating in the RAMSETE project are reported in ﬁgures 1.1 and 1.2,
respectively
Design of robot hands still poses many challenges to the research commu-
nity, and several are common to the two approaches above. However, it seems
fair (though perhaps slightly oversimplifying) to aﬃrm that anthropomorphic
design is mostly confronted with technological problems such as accuracy and
miniaturization of sensors and actuators, power and signal transmission, etc..
In minimalistic design, instead, the emphasis of current research is more on the
theoretical analysis of manipulation systems, and their deep understanding in
order to allow full exploitation of limited hardware capabilities. This chapter


<!-- page 3 -->
1.2. KINEMATICS OF MANIPULATION
3
Figure 1.2: The University of Pisa dexterous gripper
is more focussed on the latter class of problems.
Hardware complexity reduction can be achieved in several ways. For in-
stance, when grasp robustness is considered, it can be observed that enveloping
grasps are superior in terms of restraining objects. Enveloping grasps [101], in
contrast to ﬁngertip grasps, are formed by wrapping the ﬁngers (and the palm)
around the object. Indeed, this is easily seen also in human grasping, where ﬁn-
gertips and distal phalanges are used in ﬁngertip grasps for ﬁne manipulation,
while the inner parts of the hand (palm and proximal phalanges) are used in
enveloping grasps for restraint [20, 40]). One of the ﬁrst attempts at realizing
a reduced-complexity gripper was a three ﬁngered hand powered by four actu-
ators [103] that was designed to grasp by enveloping. Variations of this basic
theme are also seen in grippers designed for the so called whole arm grasps [89]
and power grasps [67]. On the other hand, for achieving dextrous manipula-
tion with a simpliﬁed hardware, the purposeful introduction of nonholonomic
phenomena in manipulation by rolling has been advocated, and experimentally
demonstrated, by several authors (see e.g. [19, 53, 71, 10]). Diﬀerent modalities
of manipulation and grasping share some fundamental theoretical framework,
analytical results, and open problems, that are the subject of this chapter’s
survey.
1.2
Kinematics of Manipulation
The model of the hand we assume is comprised of an arbitrary number of
ﬁngers (i.e. simple chains of links -phalanges -, connected through rotoidal or
prismatic joints), and of an object, which is in contact with some or all of
the phalanges We let q denote a vector of generalized coordinates, completely
describing the conﬁguration of the ﬁngers; and u = (po, Ro) ∈SE(3) denote
the conﬁguration (position and orientation) of the object. With a slight abuse


<!-- page 4 -->
4
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
of notation, we also denote with ˙q and ˙u the elements of the tangent space to
these conﬁguration spaces (hence ˙u ∈se(3) is the object twist).
Contacts represent a particular kind of kinematic constraint on the allowable
conﬁgurations of the system, and cause most of the diﬀerences in the analysis
of dextrous manipulation from other robotic systems. Contact constraints are
typically unilateral, non-holonomic constraints on the generalized coordinates
system, written in general in the form
C(q, ˙q, u, ˙u) ≥0.
(1.1)
The inequality relationship reﬂects the fact that contact can be lost if the con-
tacting bodies are brought away from each other.
This involves an abrupt
change of the structure of the model under consideration. To avoid analytical
diﬃculties, it is usually assumed that manipulation is studied during time in-
tervals when constraints hold with the equal sign (this is not the case in the
study of grasping, where the study of these inequalities is crucial to under-
standing closure properties). The constraint relationship (1.1) is not in general
integrable, i.e., it cannot be expressed in terms of q and u only: integrable
constraints are called “holonomic”. Holonomic constraints between general-
ized coordinates reduce the number of independent coordinates necessary to
describe the system conﬁguration (degrees of freedom), and can be assumed to
be removed from the description of the system by proper coordinate substitu-
tion. Nonholonomic constraints, on the contrary, do not reduce the number of
degrees-of-freedom of the system, but rather reduce the number of independent
coordinate velocities.
Contact kinematics is a study of the relationship between the location of
the point of contact as a function of the relative motion of two contacting
bodies. The ﬁrst fundamental work in this area is due to Cai and Roth [16],
who studied rigid planar bodies in point contact. They derived a relationship
for the rates of change of the location of the point of contact as a function
of the angular and linear velocities and accelerations of the contacting bodies.
Montana [69] provided a more formal description of the conﬁguration space
associated with two contacting bodies, and derived the equations of kinematic
contact that relate the time derivatives of contact coordinates with the relative
angular and linear velocities. These equations include terms that depend on the
curvature of the contacting bodies. Sarkar, Kumar, and Yun [90], extended this
work to include acceleration terms. By using intrinsic geometric properties for
the contacting surfaces, they showed the explicit dependence on the Christoﬀel
symbols and their time derivatives. This set of results is directly relevant to
dexterous manipulation [75], to the analysis of higher order closure properties
[86], to stability analysis [36], and to manipulability by rolling [58].
To describe in more detail contact constraints that are in eﬀect in dextrous
manipulation systems, consider a contact between the i-th phalanx and the
object, occurring at time t at a point described in an inertial base frame B by
the vector xi. A generic point on the surface of the phalanx will be described,
in a frame Ci ﬁxed on the phalanx, by the vector fxi. Note that, fxi ∈IR3 is
actually bounded to lie on the surface Si (which is assumed regular) of the link,


<!-- page 5 -->
1.2. KINEMATICS OF MANIPULATION
5
and therefore can be regarded as a mapping fxi :
fαi ∈Ui ⊂IR2 7→Si ⊂IR3.
The pair
¡
Ui, fxi(fαi)
¢
is called a chart for (a portion of) the surface Si, and
the 2-vector fαi is referred to as the point coordinates on the i-th link. Orthogal
coordinates can be chosen so that the associated metric tensor is diagonal. A
normalized Gauss frame can be associated with each point on the surface chart
that has the origin in the point and is ﬁxed w.r.t to the body so that its ζ axis
is aligned with the outward pointing normal, while the χ and ξ axes span the
tangent space. The orientation of the Gauss frame centered in xi w.r.t the Ci
frame can be expressed by a rotation matrix fRi. Similar considerations and
deﬁnitions hold for the object surface.
Several types of contact models can be used to describe the interaction
between the links and the object, among which the most common are the
point-contact-with-friction model (or “hard-ﬁnger”), the “soft-ﬁnger” model,
and the complete-constraint model (or “very-soft-ﬁnger”). In each case, the
constraints consist in imposing that some components of the relative velocity
between the Gauss frames that are associated with the contact point on each
surface, are zero:
Hi (o ˙ci −f ˙ci) = 0
(1.2)
where Hi is a constant selection matrix. Being the two frames ﬁxed on the
object and the phalanx, respectively, their velocities can be expressed as a
function of the velocities of the object and of the joints as
o ˙ci
=
GT
i (oαi, u) ˙u;
f ˙ci
=
Ji(fαi, qi) ˙q.
Similar relationships hold for each contact point, and a single equation can
be built to represent all constraints by properly juxtaposing vectors and block
matrices to obtain
HGT ˙u −HJ ˙q =
£
HGT
−HJ
¤ · ˙u
˙q
¸
= 0.
(1.3)
The matrix G is usually termed as the “grasp matrix”, or “grip transform”,
while J is referred to as the hand Jacobian.
One of the goals of the kinematic analysis of manipulation systems is to
explicit the relationships between joint positions and object positions.
Eq.
(1.3) can be used to this purpose (see e.g. [9]). Indeed, from (1.3), it is clear
that the vector [ ˙u, ˙q] must belong to a certain linear space, and hence that
there exist three vectors ν1, ν2, and ν3 (whose dimensions vary with the problem
at hand) such that every possible pair of object velocity ˙u and joint velocity
˙q that comply with the kinematic and contact constraints of the hand system
can be written as
˙u
=
Uoν1
+
Upν2
˙q
=
Qpν2
+
Qoν3 .
(1.4)
The columns of Up and those of Qp form a basis of the subspaces of compatible
object and joint velocities, respectively. Any object motion described by the


<!-- page 6 -->
6
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
coordinate vector ν2 in the image of Up must correspond to a joint motion with
the same coordinates in the basis Qp. The images of Qo and Uo represent the
subspaces of redundant joint velocities and under-actuated object velocities,
respectively.
Note that the matrices appearing on the right hand side of (1.4) are func-
tions of the position of the contact point on the surfaces. If the dependency
between u, q and oα, fα is explicited via the kinematics of rolling (see e.g.
[69, 58]), explicit expressions for the joint motions that are required to perform
a desired object motion can be obtained in principle. Notice also that, besides
the analytical diﬃculties, in practice we often have the case that the geometry
of the object is poorly known, if at all. The availability of contact sensors that
are able to provide information on the position of the contact points on the
phalanges is therefore necessary to attempt closed loop control of ﬁne manipu-
lation. In particular, if joint angles and contact points are sensed, (1.4) can be
used even without information on the geometry of surfaces to control the object
motion about desired trajectories by using generalized resolved-rate control.
1.3
Grasp closure properties
In order to deﬁne what grasping robustness is, the notions of form–closure and
force–closure of a grasp are instrumental. These properties, ﬁrst introduced by
[84], concern the capability of the grasp to completely or partially constrain
the motions of the manipulated object, and to apply arbitrary contact forces
on the object itself, without violating friction constraints at the contacts.
1.3.1
Form closure
Form–closure is the ability of a hand to prevent motions of the object, rely-
ing only on unilateral contact constraints. A mathematical deﬁnition of the
problem can be stated as follows
Deﬁnition 1.1 A conﬁguration u0 of an object is form–closed by a hand in
conﬁguration q if u0 is an isolated solution of the contact inequalities (1.1),
i.e., if for all u close to u0, C(q, ˙q, u, ˙u) ≥0 ⇒u = u0.
This purely geometric, rather general deﬁnition of form–closure can be special-
ized to allow easy–to–check tests. In particular, in many cases it will suﬃce to
look at the ﬁrst-order approximation of the contact inequalities, which under
rather general circumstances can be written as
NT GT ˙u ≥0
(1.5)
where G is the grasp matrix (evaluated at the current conﬁguration) and N is
a matrix stacking contact normal vectors in its diagonal. Hence we have the
following cases
i) if there exists ˙u such that all components of NT GT ˙u are positive, the grasp
is not form–closed;


<!-- page 7 -->
1.3. GRASP CLOSURE PROPERTIES
7
ii) if for all ˙u, NT GT ˙u has at least one strictly negative component, the grasp
is form closed;
iii) if case i) does not apply, but there exists ˙u such that NT GT ˙u is nonneg-
ative, the grasp may or may not be form–closed.
In cases i) and ii), second order terms are negligible, and form–closure can
be decided by ﬁrst order arguments, using for instance linear programming.
Speciﬁcally, case ii) is termed “ﬁrst–order form closure”, and it corresponds to
the most widely studied case in the literature. On the other hand, second or
higher order eﬀects must be taken into account in case iii).
First–order form–closure (which also has direct bearing to the design of
mechanical ﬁxtures and jigs for manufacturing parts) has been studied since
the 19th century. Early results showed that at least four frictionless contacts
are necessary for grasping an object in the plane, and seven in the 3D case.
In [68] and [59], it was shown that four and seven contacts are necessary and
suﬃcient for the form–closure grasp of any polyhedron in the 2D and 3D case,
respectively. An active area of research is the synthesis of form–closure grasps,
i.e., given the object geometry, where to place contacts so as to prevent object
motions.
Constructive procedures for placing contacts on given objects to
achieve form–closure have attracted much attention in the literature, due also to
the relevance to the ﬁxturing problem (see e.g. the early work of [60], and more
recently [33, 95, 11, 56, 55, 104]). There is also a form–closure analysis problem,
i.e., given an object and a set of contact locations, to decide whether the object
has any degree-of-freedom left, and which. Both qualitative (true/false) tests
(see e.g. [51, 61, 68, 34]) and quantitative (quality index) tests ([48, 100, 65])
have been proposed for form–closure. The extension of the classical, ﬁrst–order
notion of form–closure to the so–called immobilization problem, where second–
order eﬀects due to the relative curvature of the surfaces in contact are taken
into account, has been introduced rather recently to provide more detailed
results (see e.g. [35, 86, 102]) in case iii) above.
1.3.2
Force closure
The analysis of form–closure is intrinsically geometric, and does not take into
account the kinematics and characteristics of the end–eﬀector. While there is
a wide consensus in the literature on the deﬁnition of form–closure, the con-
cept of force–closure is somewhat less clearcut and universally accepted. The
intuitive meaning of force–closure implies that motions of the grasped object
are completely (or partially) restrained despite whatever external disturbance,
by virtue of suitably large contact forces that the constraining device (the end-
eﬀector) is actually capable to exert on the object.
The force and moment balance equations for an object subject to an external
force f and moment m, while grasped by a robotic mechanism by means of n
contact forces pi applied at contact points ci, is written as
w = Gp,
(1.6)


<!-- page 8 -->
8
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
where w = (f T , mT )T is the external wrench, and p = (pT
1 , . . . , pT
n)T . The
relationship between contact forces and the torques at the m joints of the
robotic hand can be written using the hand jacobian as
τ = JT p,
A general solution of (1.6) can be written in the hypothesis that w is resistible
(i.e., that rank G = rank [G w]) as
p = GRw + Ax,
(1.7)
i.e., the sum of a particular solution of (1.6) (GR is a right-inverse of G),
and a homogeneous solution. A is a matrix whose column form a basis of the
nullspace of G. The coeﬃcient vector x ∈IRh0 parametrizes the homogeneous
solution. Internal contact forces ph = Ax have no direct eﬀect on the external
wrench w, but play an important role in the robustness of the equilibrium with
respect to slippage induced by external disturbances, by allowing to “squeeze”
the object in the grasp.
It should be noted that, in general, for grasping
mechanisms with few degrees of freedom , it may not be possible to apply
arbitrary internal forces (see below section 1.7).
In force–closure analysis one generally has to deal with frictional contacts.
In diﬀerent models of contact, such as the contact-point-with-friction, soft-
ﬁnger, or very-soft-ﬁnger, friction forces and torques will be subject to limita-
tions due to Coulomb’s law of friction or to its generalizations (see e.g. [30, 38]).
We consider here contacts of the ﬁrst type (generalization poses no diﬃculties),
for which Coulomb’s inequality holds,
σi,f(pi) = αi∥pi∥−pT
i ni < 0,
(1.8)
representing a cone in the space of contact forces pi. Substituting (1.7) in (1.8),
an expression of friction constraints in terms of external wrenches and internal
forces σi,f(w, x) < 0 is obtained. In these terms, we can state the following
Deﬁnition 1.2 A grasp is deﬁned Force–Closure if, for any external wrench
w acting on the object, there exists a vector x such that all friction constraints
are fulﬁlled.
The analysis of force–closure has been considered among others by [74,
28, 18, 73], while literature on the synthesis of force–closure grasps include
[74, 79, 80, 81, 6].
According to the previous discussion on force–closure, a crucial problem in
robot manipulation is the choice of grasping forces so as to avoid (or minimize
the risk of) slippage. The problem of choosing joint torques so as to realize the
manipulating forces required by the task, while imposing internal forces that
guarantee slippage avoidance, is often referred to as the force distribution prob-
lem. Further constraints on the choice of contact forces come from limitations
in the object strength, or in the joint actuators torques. Accordingly, an “opti-
mal” set of internal forces can be deﬁned as the one that is further away from


<!-- page 9 -->
1.4. DYNAMICS
9
violating all such constraints. The force distribution problem is common with
other robotic areas, as e.g. legged locomotion, cooperating and/or constrained
manipulation, and has attracted much attention in the past few years (see e.g.
[76, 47, 42, 54, 73, 105, 43, 78, 13]).
An important property of the nonlinear constrained optimization problem
to which grasp force distribution amounts is convexity. This property, used
ﬁrst in [6], enables eﬃcient solutions to an otherwise very complex problem: [6]
proposed numeric integration of an ODE as an iterative solution to the problem;
[15] noticed that nonlinear friction constraints can be rewritten as positive–
deﬁniteness constraints on suitable matrices, and used projected gradient ﬂow
methods to optimize; [52] further exploited the matrix formulation of [15] to
transform the problem in the format of a standard linear matrix inequality
(LMI) problem, for which oﬀ–the–shelf, eﬀective software exists.
1.4
Dynamics
The ability to predict the dynamic behavior of a grasp with a given model
including the control algorithms, is critical to the design of the grasp.
In
multiﬁngered grippers, as in legged locomotion systems, multi-arm systems,
and other constrained robot systems, several limbs are used to constrain and
manipulate an object [50, 54, 67]. The dynamic analysis and the simulation
(the prediction of motion given the external forces and moments on the system)
of such systems is central to the design of such systems and the development
of control algorithms [106, 90].
A hand-object system is a constrained mechanical system, whose dynam-
ical description can be derived using Euler–Lagrange’s equations along with
constraint equations. The disjoint dynamics of the hand and of the object are
written as
Mh(q)¨q + Qh(q, ˙q) = τ;
Mo(u)¨u + Qo(u, ˙u) = w,
where Mh(·) and Mo(·) are symmetric positive deﬁnite composite inertia ma-
trices, and Qh(·, ·) and Qo(·, ·) are terms including velocity-dependent and
gravity forces of the hand and of the object, respectively. Hand and object
dynamics are linked through the n rigid–body contact constraints (1.1).
As we have seen before, when there are contacts between nominally rigid
bodies, contact constraints are unilateral. Featherstone [27], Lotstedt [57] and
Mason and Wang [62] pointed out some of the inconsistencies which arise when
rigid body models are used with Coulomb’s empirical law of friction in unilateral
systems. For example, if we consider the simulation of a rod sliding along a
rough ground in a plane with a single contact, there are conﬁgurations in which
no solutions (that are consistent with the constraints) exist, and others in which
the solution is not unique. Wang, Kumar, and Abel [107, 106] performed a
dynamic analysis of the peg-in-the-hole insertion problem and showed that
there was a range of parameters during two-point-contact for which there were


<!-- page 10 -->
10
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
either no solutions or two solutions for the accelerations. Quasi-static analysis
is also known to exhibit such inconsistencies [36].
The inconsistencies and ambiguities in the dynamic analysis of frictional
contacts have been attributed to the approximate nature of Coulomb’s model
and to the incorrect assumption of rigidity.
Recently, there has been some
attention in the robotics community on overcoming these shortcomings by using
rigid body models to predict the gross motion while using compliant contact
models to predict the contact forces and the local deformations [49].
One of the main diﬃculties that is present in multiﬁngered grasps, and a
feature that is particularly true of such grasps as power grasps and enveloping
grasps, is that the number of independent contact forces is much larger than
the number of actuators. Thus, from a controllability standpoint, not all the
contact forces are controllable (see below section 1.7).
The analysis of statically indeterminate grasps or grasps in which there is
no unique solution to the inital value problem is simply not possible unless one
explicitly models the compliance at the contacts [20, 36, 74, 49]. Of course
such contact models tend to be more complex and the parameters are more
diﬃcult to identify (see below section 1.6). Further, it is harder to simulate
systems in which the time scale for the dynamics of contact interactions is
signiﬁcantly diﬀerent from the time scale of rigid body dynamics [63, 97]. Thus,
although eﬃcient, approximate algorithms for “impulsive dynamic simulation”
that incorporate approximate impact models for collisions are available [66], it
is very diﬃcult to write accurate simulators for dexterous and ﬁne manipulation
where the contact forces may be ﬁnite and the results may be sensitive to the
parameters in the contact model.
1.5
Stability
A further important property of grasps is stability. The term is used in the
literature with at least two meanings.
One refers to Lyapunov theory, and
dictates that a grasp is (asymptotically) stable if its dynamics are such that,
when the object is displaced from its reference position, it will stay close (and
ultimately come back), to such position. A second deﬁnition is Lagrange’s,
whereby a grasp in which all forces are conservative, is stable if it corresponds
to a strict local minimum of the potential energy. The second usage is prevalent
in studies on grasp stability.
It is important to note that force closure does not guarantee stability. Any
deﬁnition of stability must regard the grasp as a dynamic system and describe
the properties of the dynamic system when it is perturbed from an equilib-
rium conﬁguration. The role of compliance and dynamics in grasping has been
investigated by many authors, beginning with Hanafusa and Asada [32] and
Salisbury[61]. Cutkosky and Kao [21] discussed how to compute the aggre-
gated compliance matrix of a hand–object system, including ﬁnger ﬂexibility
eﬀects. Relations of compliant and rolling contacts with the stability of the
grasp have been considered, at increasing levels of generality and detail, by


<!-- page 11 -->
1.6. CONTACT COMPLIANCE.
11
[22, 70, 100, 36, 99, 29]. If Lagrange’s stability criterion applies to an equilib-
rium grasp for a conservative system, Lyapunov stability follows. It should be
noted however that Lagrange’s analysis is limited under some regards. In me-
chanics, the seemingly intuitive statement that, if an equilibrium point is not a
minimum for the potential function, then it is unstable, does not have a proof
for systems with more than 2 d.o.f. [3]. Perhaps more importantly, from an
application viewpoint, is the fact that no provision is made in Lagrange anal-
ysis for non–conservative forces (except for Rayleigh–type dissipative terms).
Nonconservative forces may arise in grasping systems because of nonidealities
in the mechanical components, and of the control laws used for actuating the
hand joints. The inclusion of the eﬀects of control on the stability of grasp,
which are apparently of major moment, is as of today a mostly open research
problem. Lyapunov stability, and other structural properties (controllability,
observability, stabilizability) of general grasping systems in their linear approx-
imation have been investigated by [12, 82, 2]. Stable control of manipulation
and grasping systems has been considered among others by [72, 85, 92, 87].
Particularly important is work done towards controlling grasping systems in
the (practically ubiquitous) presence of uncertainties ([17, 24]).
A ﬁgure measuring stability (useful e.g.
to compare diﬀerent possible
grasps) may be considered ([36]) as the real part of the dominant eigenvalue
of the linearized grasp model (large values of this measure indicate that small
perturbations are damped away quickly). An even more useful ﬁgure, in many
applications, would be related to the size of the basin of attraction of the
equilibrium, indicating how large a perturbation can be without causing insta-
bility: however, eﬀective algorithms to evaluate such measure are not available
at present.
1.6
Contact compliance.
The importance of modeling the ﬁnger-object contact and the role of compli-
ance in grasping has been stressed by many researchers [4, 20, 94]. However, it
is particularly diﬃcult to model the relationship between small object/ﬁnger
displacements and changes in contact forces arising from these displacements.
Such contact problems have been studied extensively in the solid mechanics
community in the context of rail-wheel interaction [45] and analysis of ball and
roller bearings [44]. There are diﬃculties even in establishing the uniqueness
and existence of solutions of elastic bodies in static contact [25], and tractable
analytical models are, in general, very diﬃcult to come by.
Hertz’s model
[44]can be used to predict the pressure distribution across each contact patch
when the contacts are frictionless and non-conformal. Hertzian contact theory
is probably the most widely used analytical contact model, and variations of
this are used in [36, 86].
Because friction is central to robotic grasp, the Hertzian contact model
has proved to be inadequate in many cases. Sinha and Abel [94] proposed an
elastic contact stress model for ﬁnger-object contacts in multiﬁngered grasp-


<!-- page 12 -->
12
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
ing and a variational approach for quasi-static analysis. Wang, Kumar, and
Abel [107] proposed a similar approach for dynamic analysis. They developed
a mathematical programming approach for frictional, elastic contacts as well
as viscoelastic contacts in which the inertial forces due to the deformations at
the contacts are neglected. While such distributed parameter models yield ac-
curate results, the solutions require computation-intensive numerical methods.
A possible simpliﬁcation is provided by the Winkler elastic foundation model
[44], and the lumped parameter visco-elastic models used in [30, 49, 97] provide
the simplest model for simulation and analysis.
One of the very hard problems is getting an accurate and tractable model of
contact compliance, particularly in the tangential direction. This is recognized
to be a diﬃcult problem in the mechanics literature as well [44]. In addition to
this, a tractable and accurate model of friction, one that accurately predicts slip
and one that lends itself to stability analysis, is currently not available. Both
these fundamental problem areas are crucial to robotic grasping and contact
analysis.
For the purposes of analysis of grasp, it is generally assumed in the literature
that all contacts are point contacts and idealizations such as a line or surface
contact can be approximated by two or more point contacts. Each point contact
can be modeled as either a frictionless point contact, a frictional point contact,
or a soft contact [88]. A frictionless contact is deﬁned as a contact in which
the ﬁnger (or eﬀector/ﬁxture) can only exert a force along the common normal
at the point of contact. A frictional contact (sometimes referred to as a point
contact with friction) is deﬁned as a contact that can transmit both a normal
force and a tangential force, while a soft contact also allows the ﬁnger to exert
a pure torsional moment about the common normal at the point of contact.
1.7
Grasping and the kinematics of the hand
It is interesting that much of the literature in grasping actually ignores the
kinematics of the ﬁngers or the articulations that are involved in contacting
the object. While Reuleaux’s problem of form closure justiﬁably focused on
the geometry of the object and the arrangement of contacts, it is diﬃcult to
analyze a grasp without modeling the dynamics, or at least the kinematics, of
the ﬁngers and the interaction of the ﬁngers with the object.
Trinkle et. al. explore the kinematics of enveloping grasps [101] using the
restrictive but conservative assumption of frictionless contacts. The kinematics
of ﬁngers with two or three point contacts with ﬁngertips and palms have been
studied by [77, 26]. While the analysis of form–closure is intrinsically geometric,
force–closure is tightly linked to the kinematics and characteristics of the end–
eﬀector. In fact, it is possible that a geometric analysis of a grasp may predict
force–closure, but a careful analysis of the kinematics may reveal that this is not
the case [35]. Deﬁnitions of force–closure that take into account the kinematics
of the gripping device were proposed in [6], along with an exact algorithm for
testing such property. Yoshikawa proposes a new set of deﬁnitions for closure


<!-- page 13 -->
1.8. MEASURES OF GRASP PERFORMANCE
13
properties, including what he calls active and passive closures, to explicitly
model the properties of the grasping mechanism [109]. Unfortunately, much of
this, and other related work [39] is based on instantaneous kinematics.
Modeling of the ﬁngers is particularly important when end–eﬀectors that
have fewer degrees–of–freedom than necessary to impart arbitrary motions/forces
at all contacts. Such kinematically defective grasps are common in simple in-
dustrial grippers. If the hand Jacobian matrix is not full rank, it is not possible
to command an arbitrary set of grasp forces [5]. This is usually the case in all
power grasps. The modeling of the kinematics and manipulability of whole–
hand manipulation in such systems is discussed in [83]. Intuitively, the more
a grasp is defective, the more robust it is in restraining an object with respect
to external disturbances and the lower is sensitivity to positioning errors, but
also the lower is manipulability. However, a case-by-case analysis is necessary
for optimal power grasps [6].
Many open problems remain to be solved in order to be able to design
robot hands to eﬀectively exploit defectivity to increase grasp robustness and
reduce hardware complexity.
Among these, perhaps the most important is
the need for a reliable estimate of contact compliance, arising with statically
indeterminate grasps. This will then allow the calculation of contact forces,
and the development of models that relate joint displacements and torques to
contact forces.
1.8
Measures of grasp performance
Recent work in the literature has tried to develop quality measures for grasps.
One such measure can be derived from the conditioning of the grasp matrix
and is directly connected with the closure properties of the grasp [54]. In a sim-
ilar fashion, other structural properties can be derived from the characteristic
matrices, for example, controllability and observability [83].
When an object is restrained or grasped with multiple eﬀectors, there are
two, often conﬂicting, measures of grasp performance. First, if the ﬁxtures can
be accurately positioned, the system’s ability to reject wrench disturbances is
a measure of grasp stability. The grasp stiﬀness matrix, or a frame invariant
measure of the minimum grasp stiﬀness [14], provides one choice for a per-
formance metric.
This assumption of being able to accurately position the
end-eﬀector is extensively used in the ﬁxturing and grasping literature. How-
ever, when there are errors in positioning and orienting the end-eﬀectors, it is
important to choose a grasp so that the system performance is insensitive to
these positioning errors. Thus, it also makes sense to minimize the dependence
of grasp forces on such positioning errors.
Howard and Kumar [36] develop the theory needed to combine the stiﬀness
matrices at each contact to calculate a grasp stiﬀness matrix. While the signs
of the eigenvalues allow a test of grasp stability, the eigenvalues themselves
are not invariant with respect to changes in reference frames [35]. Bruyninckx
et al.
[14] develops a frame invariant measure of stability that is based on


<!-- page 14 -->
14
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
the grasp stiﬀness matrix and a metric on the Euclidean group. Lin develops
a frame-invariant quality measure that essentially minimizes the “object de-
ﬂection” when the grasped object is subject to force disturbances [55]. The
basic idea here is to scale the eigenvalues measuring the rotational stiﬀness by
a characteristic distance to an edge of the object. Thus it is possible to de-
velop a scaled stiﬀness matrix and the smallest eigenvalue of the scaled matrix
characterizes the system.
The focus in the above work is to quantify the ability of a ﬁxture to reject
disturbances due to external forces on the workpiece [23]. This is clearly a
measure of performance that is relevant. However, the robustness of a grasp
to errors in positioning the eﬀectors has not been addressed in this literature.
Sugar and Kumar develop a second measure of performance that characterizes
this robustness and discuss an approach to optimizing ﬁxtures based on both
measures [98]. In this connection, the control of grasping and the eﬀects of of
uncertainties are particularly important.
Unfortunately most of these measures are based on the assumptions of small
perturbations: displacements, forces and errors. There is no question that more
global measures would be more useful. For example, in stability analysis, a
ﬁgure relating to the size of the basin of attraction of the equilibrium, indicating
how large a perturbation can be without causing instability would be desirable.
However, the nonsmooth nature of grasp dynamics (because of the unilateral
constraints on displacements and forces) has made a thorough analysis very
diﬃcult.
1.9
Concluding Remarks
This chapter presented a survey of work in robotic grasping and manipulation
over the last twenty years. It is impossible to do justice to all the work in this
area, particularly because of the breadth of the ﬁeld and its close connection
to dexterous manipulation, ﬁxturing, and haptics. We chose to focus on issues
that are central to the mechanics of grasping and the ﬁnger–object contact
interactions. In addition, the review mainly addressed research that has estab-
lished the theoretical framework for grasp analysis, simulation and synthesis.
Because of the limitations on space, we have not given the algorithmic aspects,
and the applications the attention that they deserve.
Acknowledgements
This paper builds upon previous works by the authors ([7],[8]), and reports
on work done by A. Bicchi at the University of Pisa with the support of the
MURST project “RAMSETE”, and Prof. Vijay Kumar at the University of
Pennsylvania, who acknowledges support from NSF grants CISE RI 9703220,
GRT 9355018, DARPA grants ITO/MARS 130-1303-4-534328-2000-0000 and
ATO/TMR DAAH04-96-1-0007, and ARO grant MURI DAAH04-96-1-0007.


<!-- page 15 -->
REFERENCES
15
References
[1] 2000 Symposium on Part Feeding and Fixturing, Goldberg K (Org). In:
Proceedings of 2000 IEEE International Conference on Robotics and Au-
tomation San Francisco, CA
[2] Al-Fahed Nuseirat A M, Hamdan A M A, Hamdan H M A 1999 Stability
and modal control of an object grasped by a multiﬁngered Robot Hand
Zeitschrift f¨ur Angewandte Mathematik und Mechanik 79:473–479
[3] Arnold V I 1980 Mathematical Methods of Classical Mechanics Springer
Heidelberg
[4] Asada H 1979 Studies on Prehension and Handling by Robot Hands with
Elastic Fingers PhD Thesis, Kyoto University
[5] Bicchi A 1994 On the problem of decomposing grasp and manipulation
forces in multiple whole–limb manipulation. Journal of Robotics and Au-
tonomous Systems 13:127–147
[6] Bicchi A 1995 On the closure properties of robotic grasping. International
Journal of Robotics Research 14:319–334
[7] Bicchi A 2000 Hands for dextrous manipulation and robust grasping: a
diﬃcult road towards simplicity. IEEE Transactions on Robotics and Au-
tomation 16:652–662
[8] Bicchi A, Kumar V 2000 Robotic grasping and contact: A review, In:
Proceedings of 2000 IEEE International Conference on Robotics and Au-
tomation San Francisco, CA, pp 348-353
[9] Bicchi A, Melchiorri C, Balluchi D 1995 On the mobility and manipulability
of general multiple limb robotic systems. IEEE Transactions on Robotics
and Automation 11:215–228
[10] Bicchi A, Sorrentino R 1995 Dexterous manipulation through rolling. In:
Proceedings of 1995 IEEE International Conference on Robotics and Au-
tomation Nagoya, J pp 452–457
[11] Borst Ch, Fischer M, Hirzinger G 1999 A fast and robust grasp plan-
ner for arbitrary 3D objects. In: Proceedings of 1999 IEEE International
Conference on Robotics and Automation Detroit, MI, pp 1890–1896
[12] Brook N, Shoham M, Dayan J 1998 Controllability of grasps and ma-
nipulations in multi–ﬁngered hands. IEEE Transactions on Robotics and
Automation 14:185–192
[13] Bruyninckx H, Demey S, Dutr´e S, DeSchutter J 1995 Kinematic models for
model based compliant motion in the presence of uncertainty. International
Journal of Robotics Research 14:465–482


<!-- page 16 -->
16
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
[14] Bruyninckx H, Demey S, Kumar V 1998 Generalized stability of compliant
grasps. In: Proceedings of 1998 IEEE International Conference on Robotics
and Automation Leuven, B, pp 2396-1401
[15] Buss M, Hashimoto H, Moore J 1996 Dextrous hand grasping force opti-
mization. IEEE Transactions on Robotics and Automation 12:406–418
[16] Cai C, Roth B 1987 On the spatial motion of rigid bodies with point
contact. In: Proceedings of 1987 International Conference on Robotics and
Automation Rayleigh, NC, pp 686–695
[17] Cheah C C, Han H-Y, Kawamura S, Arimoto S 1998 Grasping and position
control for multi-ﬁngered robot hands with uncertain Jacobian matrices.
In: Proceedings of 1998 IEEE International Conference on Robotics and
Automation Leuven, B, pp 2403-2408
[18] Chen I-M, Burdick J W 1993 A qualitative test for n-ﬁnger force–closure
grasps on planar objects with applications to manipulation and ﬁnger gaits.
In: Proceedings 1993 IEEE International Conference on Robotics and Au-
tomation Atlanta, GA, pp 814–820
[19] Cole A A, Hsu P, Sastry S S 1992 Dynamic control of sliding by robot hands
for regrasping. IEEE Transactions on Robotics and Automation 8:42–52
[20] Cutkosky M R 1985 Robotic Grasping and Fine Manipulation Kluwer,
Boston, MA
[21] Cutkosky M R, Kao I 1989 Computing and controlling the compliance of a
robotic hand. IEEE Transactions on Robotics and Automation 5:151–165
[22] Cutkosky M, Wright P 1986 Friction, stability and the design of robotic
ﬁngers. International Journal of Robotics Research 5:20–37
[23] Donoghue J, Howard W S, Kumar V 1994 Stable workpiece ﬁxturing.
In: Proceedings 3rd Biennial ASME Mechanisms Conference Minneapolis,
MN, pp 475–482
[24] Doulgeri Z, Arimoto S 1999 A force control for a robot ﬁnger under kine-
matic uncertainties. In: Proceedings of 1999 IEEE International Confer-
ence on Robotics and Automation Detroit, MI, pp 1475–1480
[25] Duvaut G, Lions J L 1976 Inequality in Mechanics and Physics Springer,
London
[26] Erdmann M 1997 An exploration of nonprehensile two-palm manipulation.
International Journal of Robotics Research 16:1–23
[27] Featherstone R 1986 The dynamics of rigid body systems with multiple
concurrent contacts. In: Faugeras O D, Giralt G (Eds) Robotics Research:
The Third International Symposium MIT Press, Cambridge, MA, pp. 189–
196


<!-- page 17 -->
REFERENCES
17
[28] Ferrari C, Canny J 1992 Planning optimal grasps. In:
Proceedings of
1992 IEEE International Conference on Robotics and Automation Nice,
F, pp 2290-2295
[29] Funahashi Y, Yamada T, Tate M, Suzuki Y 1996 Grasp stability analysis
considering the curvatures at contact points. In: Proceedings of 1996 IEEE
International Conference on Robotics and Automation Minneapolis, MN,
pp 3040–3046
[30] Goyal S, Pinson E M, Sinden F W 1994 Simulation of dynamics of in-
teracting rigid bodies including friction - I: General problem and contact
model. Engineering with Computers 10:162–174
[31] Grupen R A, Henderson T C, McCammon I D 1989 A survey of general–
purpose manipulation. International Journal of Robotics Research 8:38-62
[32] Hanafusa H, Asada H 1982 Stable prehension by a robot hand with elastic
ﬁngers. In: Brady M, Hollerbach J M, Johnson T L, Lozano-Perez T, Mason
M T (Ed) Robot Motion Planning and Control MIT Press, Cambridge, MA,
pp 323–336
[33] Hester R D, Cetin M, Kapoor C, Tesar D 1999 A criteria-based approach
to grasp synthesis In: Proceedings of 1999 IEEE International Conference
on Robotics and Automation Detroit, MI, pp 1255–1260
[34] Hirai S, Asada H 1993 Kinematics and statics of manipulation using the
theory of polyhedral convex cones. International Journal of Robotics Re-
search 12:434–447
[35] Howard W S 1995 On the Stability of Grasped Objects PhD Thesis, Uni-
versity of Pennsylvania
[36] Howard W S, Kumar V 1996 On the stability of grasped objects. IEEE
Transactions on Robotics and Automation 12:904–917
[37] Howe R D, Cutkosky M R 1992 Touch sensing for robotic manipulation
and recognition. In: Khatib O, Craig J J, Lozano-P´erez (Eds) The Robotics
Review 2 MIT Press, pp 55–112
[38] Howe R D, Cutkosky M R 1996 Practical force–motion models for sliding
manipulation. International Journal of Robotics Research 15:557–572
[39] Hunt K H, Samuel A E, McAree P R 1991 Special conﬁgurations of multi–
ﬁnger multi–freedom grippers — A kinematic study. International Journal
of Robotics Research 10:123–134
[40] Iberall T 1997 Human Prehension and Dexterous Robot Hands. Interna-
tional Journal of Robotics Research 16:285–299
[41] Jacobsen S C, Knutti D F, Johnson R T, Sears H H 1982 Development
of the Utah Artiﬁcial Arm. IEEE Transactions on Biomedical Engineering
29:249-269


<!-- page 18 -->
18
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
[42] Jameson J W 1985 Analythic Techniques for Automated Grasp PhD The-
sis, Stanford University
[43] Joh J, Lipkin H 1991 Lagrangian wrench distribution for cooperating
robotic mechanisms. In: Proceedings of 1991 IEEE International Confer-
ence on Robotics and Automation Sacramento, CA, pp 224–229
[44] Johnson K 1985 Contact Mechanics Cambridge University Press, Cam-
bridge, UK
[45] Kalker J J 1990 Three-Dimensional Elastic Bodies in Rolling Contact
Kluwer, Boston, MA
[46] Klatzky R, Lederman S 1990 Intelligent exploration by the human hand.
In:
Venkataraman S T, Iberall T (Eds) Dextrous Robot Manipulation
Springer, London, UK
[47] Kerr J, Roth B 1986 Analysis of multiﬁngered hands International Journal
of Robotics Research 4:3–17
[48] Kirkpatrick D, Kosaraju S R, Mishra B, Yap C–K 1989 Quantitative
Steinitz’s Theorem with Applications to Multiﬁngered Grasping TR460,
Courant Institute of Mathematical Sciences, New York University
[49] Kraus P R, Fredriksson A, Kumar V 1997 Modeling of frictional contacts
for dynamic simulation. In: Proceedings of Workshop on Dynamic Simu-
lation: Methods and Applications at IEEE/RSJ International Symposium
on Robotic and Intelligent Systems, Nice, F, pp 33–38
[50] Kumar V, Waldron K J 1988 Force distribution in closed kinematic chains.
IEEE Journal of Robotics and Automation 4:313–321
[51] Lakshminarayana K 1978 Mechanics of Form Closure ASME Technical
report 78-DET32
[52] Li H, Trinkle J C, Li Z 1999 Grasp analysis as linear matrix inequal-
ity problems. In: Proceedings of 1999 IEEE International Conference on
Robotics and Automation Detroit, MI, pp 1261–1266
[53] Li Z, Canny J 1990 Motion of two rigid bodies with rolling constraint.
IEEE Transactions on Robotics and Automation 6:62–72
[54] Li Z, Hsu P, Sastry S S 1989 Grasping and coordinated manipulation
by a multiﬁngered robot hand. International Journal of Robotics Research
8:42–52
[55] Lin Q, Burdick J W 1999 A task-dependent approach to minimum-
deﬂection ﬁxtures. In: Proceedings of 1999 IEEE International Conference
on Robotics and Automation Detroit, MI, pp 1562–1567


<!-- page 19 -->
REFERENCES
19
[56] Liu Y H, Ding D, Wang S 1999 Constructing 3D frictional form-closure
grasps of polyhedral oObjects. In: Proceedings of 1999 IEEE International
Conference on Robotics and Automation Detroit, MI, pp 1904–1909
[57] Lostedt P 1982 Mechanical systems of rigid bodies subject to unilateral
constraints. SIAM Journal of Applied Mathematics 42:281-296
[58] Marigo A, Bicchi A 2000 Rolling bodies with regular surfaces: Controlla-
bility theory and applications. IEEE Transactions on Automatic Control
45:1586–1599
[59] MarkenscoﬀX, Ni L, Papadimitriou C H 1990 The geometry of grasping.
International Journal of Robotics Research 9:61–74
[60] MarkenscoﬀX, Papadimitriou C H 1989 Optimum grip of a polygon. In-
ternational Journal of Robotics Research 8:17–29
[61] Mason M T, Salisbury J K 1985 Robot Hands and the Mechanics of Ma-
nipulation MIT Press Cambridge, MA
[62] Mason M T, Wang Y 1988 On the inconsistency of rigid-body frictional
planar mechanics. In: Proceedings of 1988 IEEE International Conference
on Robotics and Automation Philadelphia, PA, pp 524–528
[63] McClamroch N H 1989 A singular perturbation approach to modeling and
control of manipulators constrained by a stiﬀenvironment. In: Proceedings
of 28th IEEE Conference on Decision and Control, pp.2407–2411
[64] Melchiorri C, Vassura G 1992 Mechanical and control features of the Uni-
versity of Bologna Hand Version 2. In: Proceedings of 1992 IEEE/RSJ In-
ternational Conference on Intelligent Robots and Systems, Rayleigh, NC,
pp 187–193
[65] Miller A T, Allen P K 1999 Examples of 3D grasp quality computations.
In: Proceedings of 1999 IEEE International Conference on Robotics and
Automation Detroit, MI, pp 1240–1245
[66] Mirtich B, Canny J 1996 Estimating pose statistics for robotic part feeders.
In: Proceedings of 1996 IEEE International Conference on Robotics and
Automation Minneapolis, MN, pp 1140-1146
[67] Mirza K, Orin D E 1994 General formulation for force distribution in power
grasp. In: Proceedings of 1996 IEEE International Conference on Robotics
and Automation San Diego, CA, pp 880–887
[68] Mishra B, Schwartz J T, Sharir M 1987 On the existence and synthesis of
multiﬁnger positive grips. Algorithmica 2:541–558
[69] Montana D J 1988 The kinematics of contact and grasp. International
Journal of Robotics Research 7:17–32


<!-- page 20 -->
20
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
[70] Montana D J 1992 Contact stability for two-ﬁngered grasps. IEEE Trans-
actions on Robotics and Automation 8:421-430
[71] Murray R M, Li Z, Sastry S S 1994 A Mathematical Introduction to Robotic
Manipulation CRC Press, Boca Raton, FL
[72] Nagai K, Yoshikawa T 1993 Dynamic manipulation/grasping control of
multiﬁngered robot hands. In: Proceedings of 1993 IEEE International
Conference on Robotics and Automation Atlanta, GA, vol 3, pp 1027–1032
[73] Nakamura Y, Nagai K, Yoshikawa T 1989 Dynamics and stability in co-
ordination of multiple robotic systems. International Journal of Robotics
Research 8:44–61
[74] Nguyen V D 1988 Constructing force-closure grasps. International Journal
of Robotics Research 7:3–16
[75] Okamura A M, Smaby N, Cutkosky M R 2000 An overview of dextrous
manipulation. In: Proceedings of 2000 IEEE International Conference on
Robotics and Automation San Francisco, CA, pp 255-262
[76] Orin D E, Oh S Y 1981 Control of force distribution in robotic mechanisms
containing closed kinematic chains. ASME Journal of Dynamic Systems,
Measurement and Control 102: 134–141
[77] Paljug E, Yun X, Kumar V 1994 Control of rolling contacts in two-arm
manipulation. IEEE Transactions on Robotics and Automation 10:441–452
[78] Panagiotopoulos P D, Al-Fahed A M 1994 Robot hand grasping and re-
lated problems: optimal control and identiﬁcation. International Journal
of Robotics Research 13:127–136
[79] Park Y C, Starr G P 1992 Grasp synthesis of polygonal objects using
a three-ﬁngered robot hand. International Journal of Robotics Research
11:163–184
[80] Ponce J, Faverjon B 1995 On computing three ﬁnger force–closure grasp of
polygonal objects. IEEE Transactions on Robotics and Automation 11:868–
881
[81] Ponce J, Sullivan S, Sudsang A, Boissonnat J D, Merlet J P 1997 On
computing four–ﬁnger equilibrium and force-closure grasps of polyhedral
objects. International Journal of Robotics Research 16:11–35
[82] Prattichizzo D, Bicchi A 1997 Consistent speciﬁcation of manipulation
tasks for defective mechanical systems ASME Journal of Dynamical Sys-
tems, Measurement and Control 119:767–775
[83] Prattichizzo D, Bicchi A 1998 Dynamic analysis of mobility and graspabil-
ity of general manipulation systems. IEEE Transactions on Robotics and
Automation 14:241–258


<!-- page 21 -->
REFERENCES
21
[84] Reuleaux F 1875 Theoretische Kinematic. Translated 1963 as Kinematics
of Machinery Dover, New York, NY
[85] Reznik D, Lumelsky V 1994 Multi–ﬁnger “hugging”: A robust approach to
sensor based grasp planning. In: Proceedings of 1994 IEEE International
Conference on Robotics and Automation San Diego, CA, pp 754–759
[86] Rimon E, Burdick J W 1998 Mobility of bodies in contact. IEEE Trans-
actions on Robotics and Automation 14:696–717
[87] Rodriguez-Angeles
A,
Parra-Vega
V
1998
Adaptive
control
with
impedance of cooperative multi-robot system. In:
Proceedings of 1988
IEEE International Conference on Robotics and Automation Philadelphia,
PA, pp 1522–1527
[88] Salisbury J K 1982 Kinematics and Force Analysis of Articulated Hands
PhD Thesis, Stanford University
[89] Salisbury J K 1987 Whole-arm manipulation. In: Bolles R, Roth B (Eds)
Robotics Research: The 4th International Symposium MIT Press, Cam-
bridge, MA, pp 183–189
[90] Sarkar N, Yun Y, Kumar V 1997 Dynamic control of 3-D rolling contacts
in two-arm manipulation. IEEE Transactions on Robotics and Automation
13:364–376
[91] Selig A J, Rooney P K 1989 Reuleaux pairs and surfaces that cannot be
gripped. International Journal of Robotics Research 8:79–87
[92] Sheridan M J, Ahalt S C, Orin DE 1995 Fuzzy control for robotic power
grasp. Advanced Robotics 9:535–546
[93] Shimoga K B 1996 Robot grasp synthesis algorithms: A survey. Interna-
tional Journal of Robotics Research 15:230–266
[94] Sinha P R, Abel J M 1992 A contact stress model for multiﬁngered grasps
of rough objects. IEEE Transactions on Robotics and Automation 8:7–22
[95] Smith G, Lee E, Goldberg K Y, Bohringer K, Craig J 1999 Computing
parallel-jaw grips. In: Proceedings of 1999 IEEE International Conference
on Robotics and Automation Detroit, MI, pp 1897–1902
[96] SomoﬀR 1897 Uber schraubengeschwindigkeiten eines festen korpers bei
verschiedener zahl von stutzﬂachen, Zietschrift f¨ur Mathematik und Physik
42:133–153
[97] Song
P,
Kraus
P,
Kumar
V,
Dupont
P
1999
A
singular
per-
turbation analysis of the dynamics of systems with frictional con-
tacts. ASME Journal of Applied Mechanics under review. Available at
http://www.cis.upenn.edu/ pengs/publications/j am99.ps


<!-- page 22 -->
22
CHAPTER 1. ROBOTIC GRASPING AND MANIPULATION
[98] Sugar T, Kumar V 1998 Decentralized control of cooperating mobile ma-
nipulators. In:
Proceedings of 1998 IEEE International Conference on
Robotics and Automation Leuven, B, pp 2916–2921
[99] Svinin M M, Ueda K, Kaneko M 1999 Analytical conditions for the ro-
tational stability of an object in multi-ﬁnger grasping. In: Proceedings of
1999 IEEE International Conference on Robotics and Automation Detroit,
MI, pp 1347–1352
[100] Trinkle J C 1992 On the stability and instantaneous velocity of grasped
frictionless objects. IEEE Transactions on Robotics and Automation 8:560–
572
[101] Trinkle J C, Abel J M, Paul R P 1987 An investigation of frictionless en-
veloping grasping in the plane. International Journal of Robotics Research
7:33–51
[102] Trinkle J C, Farahat A O, Stiller P F 1995 First order stability cells
of active multi-rigid body systems. IEEE Transactions on Robotics and
Automation, 11:545-557
[103] Ulrich N, Kumar V, Paul R, Bajcsy R 1990 Grasping with mechanical
intelligence. In: Preprints CISM-IFToMM Symposium on Robots, Manip-
ulators, and Systems, pp. 333–339
[104] van der Stappen A F, Wentink C, Overmars M H 1999 Computing form-
closure conﬁgurations In: Proceedings of 1999 IEEE International Confer-
ence on Robotics and Automation Detroit, MI, pp 1837–1842
[105] Walker I D, Freeman R A, Marcus S I 1991 Analysis of motion and
internal loading of objects grasped by multiple cooperating manipulators.
International Journal of Robotics Research 10:396–409
[106] Wang Y, Kumar V 1994 Simulation of mechanical systems with unilateral
constraints. ASME Journal of Mechanical Design 116:571-580
[107] Wang Y-T, Kumar V, Abel J 1992 Dynamics of rigid bodies with multiple
frictional contacts. In: Proceedings of 1992 IEEE International Conference
on Robotics and Automation Nice, F, pp 2764–2769
[108] Wen J T, Wilﬁnger L S 1998 Kinematic manipulability of general con-
strained rigid multibody systems. In: Proceedings of 1998 IEEE Interna-
tional Conference on Robotics and Automation Leuven, B, pp 1020–1025
[109] Yoshikawa T 1996 Passive and active closures by constraining mecha-
nisms. In: Proceedings of 1996 IEEE International Conference on Robotics
and Automation Minneapolis, MN, pp 1477–1484
