1 

# Adaptive Synergies for the Design and Control of the Pisa/IIT SoftHand 

M. G. Catalano<sup>_∗_+</sup> , G. Grioli<sup>_∗_+</sup> , E. Farnioli<sup>_∗_+</sup> , A. Serio<sup>_∗_+</sup> , C. Piazza<sup>_∗_</sup> , A. Bicchi<sup>_∗_+</sup> 

**_Abstract_ —In this paper we introduce the Pisa/IIT SoftHand, a novel robot hand prototype designed with the purpose of being robust and easy to control as an industrial gripper, while exhibiting high grasping versatility and an aspect similar to that of the human hand. In the paper we briefly review the main theoretical tools used to enable such simplification, i.e. the neuroscience–based notion of** **_soft synergies_ . A discussion of several possible actuation schemes shows that a straightforward implementation of the soft synergy idea in an effective design is not trivial. The approach proposed in this paper, called** **_adaptive synergy_ , rests on ideas coming from underactuated hand design. A synthesis method to realize a desired set of soft synergies through the principled design of adaptive synergy is discussed. This approach leads to the design of hands accommodating in principle an arbitrary number of soft synergies, as demonstrated in grasping and manipulation simulations and experiments with a prototype. As a particular instance of application of the synthesis method of adaptive synergies, the Pisa/IIT SoftHand is described in detail. The hand has 19 joints, but only uses one actuator to activate its adaptive synergy. Of particular relevance in its design is the very soft and safe, yet powerful and extremely robust structure, obtained through the use of innovative articulations and ligaments replacing conventional joint design. The design and implementation of the prototype hand are shown and its effectiveness demonstrated through grasping experiments, reported also in the multimedia extension 1.** 



Fig. 1. Skeleton of the Pisa/IIT SoftHand advanced anthropomorphic hand prototype implementing one adaptive synergy. The prototype dimensions are comparable to those of the hand of an adult human. 

## I. INTRODUCTION 

To get close to the richness and complexity of the sensory and motor functionalities of a human hand with a robust and economically reasonable robotic device remains one of the hardest challenges in robotics. 

In this paper, we propose an integrated approach of mechanics and control co-design, which aims to achieve better results — in terms of performance and design simplicity — by embedding part of the control intelligence in the physical structure of the system itself. Neuroscientific studies, as for example [Santello et al., 1998], [Weiss and Flanders, 2004] and [Latash et al., 2005], suggest that the extremely high complexity of the the human hand sensori-motor system is tamed through a stratified set of motor primitives, or _synergies_ , which render it manageable for the higher level cognitive functions as an organized and ordered ensemble. These are embodied at different levels, from the physical grouping of multiarticular muscles and tendons, to reflex arcs, up to the cerebellar and cortical synaptic circuitry. By virtue of this organization, particular patterns of neuro-muscular 

> _∗_ Centro di Ricerca “E. Piaggio”, Universit`a di Pisa, Largo L. Lazzarino, 1, 56126 Pisa, Italy. 

> +Department of Advanced Robotics, Istituto Italiano di Tecnologia, via Morego, 30, 16163 Genova, Italy. 

activities form a base set, analogous to the concept of _basis_ in theory of vector spaces [Easton, 1972]: a minimal number of linearly independent elements that under specific operations generate all members of a given set, in this case, the set of all movements. Such basis are sometimes referred to as the space of _postural synergies_ , or the eigengrasp space [Ciocarlie et al., 2007]. 

Recently, different approaches in robotics tried to take advantage from the idea of synergies, aiming to reproduce a similar “coordinated and ordered ensemble” of human hand motions. To transfer part of the embodied intelligence, typical of the human hand, into a robotic counterpart, a promising possibility is the re-creation of synergy patterns as a feature of the mechatronic hand system. This approach has already been tried in recent literature (see next section for a short review), although a purely kinematic model of synergies leads to inconsistent grasp force distribution models. To solve such problems, the concept of _soft synergies_ was introduced [Gabiccini et al., 2011], [Bicchi et al., 2011], which provides a model of how synergies may generate and control the internal forces needed to hold an object. 

In this paper, partly based on [Catalano et al., 2012], we 

2 



Fig. 2. Full Actuation. Conceptual schematics of a simple bi-dimensional fully actuated hand grasping an object. 

|Notation|Definition|
|---|---|
|_δx_<br>¯_x_<br>_♯x_|variation of variable _x_<br>value of _x_ in the reference configuration<br>dimension of vector _x_|
|_w_<sup>_o_</sup><br>_e _<sup>_∈_R6</sup><br>_u ∈_R<sup>6</sup><br>_f_<sup>_co_</sup><br>_h_<br>_∈_R<sup>_c_</sup><br>_c_<br>_τ ∈_R<sup>_♯q_</sup><br>_q ∈_R<sup>_♯q_</sup><br>_qr ∈_R<sup>_♯q_</sup><br>|external wrench acting on the object<br>pose of the object frame<br>contact forces exerted by the hand on the object<br>number of contact constraints<br>joint torque<br>joint configuration<br>reference joint configuration|
|_σ ∈_R<sup>_♯σ_</sup><br>_ε ∈_R<sup>_♯σ_</sup><br>|soft synergy configuration<br>soft synergy forces|
|_z ∈_R<sup>_♯z_</sup><br>_η ∈_R<sup>_♯z_</sup>|adaptive synergy displacements<br>adaptive synergy forces|
|_oG ∈_R6_×c_<br>|grasp matrix in object frame|
|_c_<sup>_o_</sup>_J ∈_R_c×♯q_<br>_S ∈_R<sup>_♯q×♯σ_</sup><br>_R ∈_R<sup>_♯z×♯q_</sup>|hand Jacobian matrix in object frame<br>soft synergy matrix<br>adaptive synergy matrix|



TABLE I NOTATION FOR GRASP ANALYSIS. 

## II. HAND ACTUATION, SYNERGIES AND ADAPTATION 

exploit the soft synergy idea to build robot hands that can grasp a large variety of objects in a stable way, while remaning very simple and robust. Our approach to the principled simplification of hand design can be summarized as follows. From statistical observations of human grasping, we derive the hand postures most often used in the grasp approach phase (aka synergies) and design the hand mechanism so that similar approach motions are obtained. Indeed, human–like hand movement has great influence in the possibility of successfully achieving a large number of grasps belonging to the sphere of activities of daily living (ADL). The actual realization of the hand mechanics is not however a straightforward implementation of the soft synergy model. Indeed, to achieve a simple and compact design and better robustness, we recur to the technology of underactuated hands [Birglen et al., 2008], complementing it with innovative joint and ligament design. One of the main contributions of this paper is to show how the design parameters of an underactuated hand can be chosen so that its motion replicates a given set of synergies, in a sense allowing the translation of the concept of _soft synergies_ into _adaptive synergies_ . 

The result of our design method is the Pisa/IIT SoftHand (see fig. 1), a 19-joints hand with anthropomorphic features, which grasps objects of rather general shape by using only a single actuator, and employing an innovative design of articulations and ligaments, which provides a high degree of compliance to external solicitations. 

The paper is organized as follows: section II introduces the problem and presents a review of possible hand actuation patterns, before concentrating on the soft and adaptive synergies approaches. Section III presents a proof-of-concept design, after which the Pisa/IIT SoftHand prototype is built, as Section IV describes in detail. Section V presents the grasping results experimentally obtained. Finally, conclusions are drawn in section VI. 

## _A. Fully Actuated Hands_ 

In this section we provide a description of design paradigms of hand motor systems found in robotic literature. Starting from the simplest case of fully actuated hand grasping an object, we also provide an analytical description of the different actuation methods. The nomenclature and notation used for grasping analysis are synthesized in Table I. Finally, we present a map between the human inspired soft synergy model and the adaptive synergy design, used in the Pisa/IIT SoftHand. More details about the mathematical description of grasping can be found in [Murray et al., 1994], [Gabiccini et al., 2012]. 

A quasi-static description of the problem of a hand grasping an object can be formalized by a system of three equations as 







Here, the object equilibrium equation (1) establishes a relationship between external disturbances acting on the object and contact forces that the hand exerts on the object, eq. (2) describes the joint torque variation required to compensate contact force variation and/or kinematic displacement of the system, and the contact constitutive equation (3) relates contact force variation with the mutual displacements of the hand and the object contact points. 

More in detail, in equation (1), the symbol _we_<sup>_o∈_R6indicates</sup> the external wrench acting on the object, described in a local frame _{O}_ , while _fh_<sup>_co∈_R</sup><sup>_c_aretheforcesthatthehandexerts</sup> on the object, described in local contact frames, fixed to the object. The value of _c_ , for the contact force vector, depends on the number and type of contact constraints. For example, an _hard finger_ contact, allows the presence of three components of forces, thus it contributes three. Indeed, the _soft finger_ contact, with respect to the hard one, adds the possibility to exert a moment around the normal vector to the contact 

3 

surface, thus it contributes four. Through the introduction of the _grasp matrix_<sup>_o_</sup> _G ∈_ R<sup>6</sup><sup>_×c_</sup> , the object equilibrium condition is written as 



Because the equation is written in a reference frame attached to the object, the grasp matrix is constant, hence by differentiating (4), (1) follows. 

The hand equilibrium equation relates contact forces with joint torques, _τ ∈_ R<sup>_♯q_</sup> , through the transpose of the hand Jacobian matrix<sup>_co_</sup> _J_<sup>_T_</sup> ( _q, u_ ) _∈_ R<sup>_♯q×c_</sup> , as 



It is worth observing that the Jacobian matrix is here a function both of the hand configuration _q_ and of the object configuration _u ∈_ R<sup>6</sup> . This is a consequence of the choice to describe the contact interaction in a local frame attached to the grasped object. From this fact it follows that, differentiating (5), (2) is obtained, where the terms Ω= _∂_<sup>_co_</sup> _J_<sup>_T_</sup> _<u>fh</u>_<sup>_co_</sup> _∈_ R<sup>_♯q×♯q_</sup> and _∂q_ _<u>h</u> U_ =<sup>_∂coJTf co_</sup> _∈_ R<sup>_♯q×_6</sup> have to be considered. _∂u_ 

As described in [Bicchi, 1994], a rigid model of hand/object interaction does not allow the computation of the contact force distribution. The problem can be simply solved by introducing a _virtual spring_ at the contact points. One extreme of each virtual spring is attached to the hand and the other to the object, both in the nominal contact location. The virtual spring model generates a force variation corresponding to the local interpenetration of the hand and object parts. Correspondingly, a contact force variation is described in (3) through the introduction of the _contact stiffness_ matrix _Kc ∈_ R<sup>_c×c_</sup> . 

The basic grasp equations (1), (2) and (3) can be rearranged in matrix form as 



This is a linear homogeneous system of equations in the form _Aδy_ = 0, where _A ∈_ R<sup>_ra×ca_</sup> is the coefficient matrix, and _δy ∈_ R<sup>_ca_</sup> is the vector containing all system variables. From (6), we easily obtain that _A_ is always full row rank, and its dimensions are 



These facts imply that a basis for the solution space of the system has dimension _ca − ra_ = _♯w_ + _♯q_ . Thus, a perturbed configuration of the system can be completely described knowing the values of the external wrench variation, _δwe_<sup>_o_,andthedisplacementsofthejointconfiguration1,</sup><sup>_δq_.</sup> We will refer to these as the _independent variables_ of the system. The _dependent variables_ will be indicated as _δyd_ = � _δτ_<sup>_T_</sup> _, δfh_<sup>_coT_</sup> _, δu_<sup>_T_�</sup><sup>_T_</sup> . 

> 1From the previous considerations, it follows that other choices are possible. However, a complete discussion about these cases is out of the scope of this work. 

Acting on the coefficient matrix of the system, it is possible to obtain a formal method to get an explicit expression of the dependent variables of the system, as a function of the independent ones. This result is achievable extending the _elementary Gauss operations_ , defined for typical linear systems of equations, in order to act on a block partitioned matrix. A general algorithm to obtain the desired form starting from (6), called GEROME-B, was presented in [Gabiccini et al., 2012]. The final result of the procedure is a set of equations of the type 



In the rest of this paper, we will mostly focus on the study of the controllability of grasping with different hand actuation system, hence considering a null external wrench variation in (8). For the sake of completeness, we report here on the structure of this matrix, which can be partitioned as _Qd_ = � _QτT Q_<sup>_T_</sup> _f Q_<sup>_T_</sup> _u_ � _T_ , with the following explicit formulae 



## _B. Approaches to Simplification_ 

In principle, fully independent actuation offers the widest possibilities, limited only by the hand kinematics. This comes with a cost in terms of design complication to accommodate for the large number of actuators. Even disregarding the hardware aspect, however, the exploitation of the potential of full independent actuation requires sophisticated programming and control of the hand to exploit the potentialities of the kinematic structure. Programming complexity turns often out to represent a major obstacle to usability and efficiency in real-world applications of robot hands. 

One of the main directions recently followed is the under–parametrization of the hand postures, following the idea of _synergies_ , so as to find a trade off between the full utilization of the hand capabilities and the simplicity in control. Neuroscience results, as for example those of [Weiss and Flanders, 2004], [Santello et al., 2013], [Castellini and van der Smagt, 2013], hinted that the brain controls the human hand not as a collection of independent articulations and muscles, but rather as an organized whole of coherent motion patterns or primitives. Particular muscular activation patterns give rise to strongly correlated movements, which form a base set [Easton, 1972], resembling the concept of _basis_ of a vector space in linear algebra. Such basis is referred to as the space of _postural synergies_ , or _eigengrasp space_ [Ciocarlie et al., 2007], [Prattichizzo et al., 2010], [Wimboeck et al., 2012]. 

What makes the bio–aware synergy basis stand out among other possible choices for the basis to describe the hand configuration is the fact that most of the hand grasp posture variance, actually the 80%, is explained just by the first two synergies, and the 87% by the first three 

4 



Fig. 3. Hard Synergy actuation scheme. Turning the shaft of a pulley train generates a joint motion pattern, which can be designed corresponding to a desired synergy vector. 

[Santello et al., 1998]. This renders the synergy space a credible candidate as a basis for simplification. 

The basic idea behind the use of synergies in robotics consists in specifying a suitable base for the joint space movements, called _synergy matrix_ , _S ∈_ R<sup>_♯q×♯σ_</sup> , where _♯σ ≤ ♯q_ is the number of used synergies. A hand configuration can be described in the synergy space by the coordinate vector _σ ∈_ R<sup>_♯σ_</sup> as in 



There already exist some applications in robotics which take advantage of the idea of synergies. For example in [Ciocarlie et al., 2007], the use of _software synergies_ as simulated correlation patterns between joint movements of a fully actuated robotic hand was suggested to simplify control. Software synergies can substantially simplify the design phase of a grasp, by reducing the number of control variables (see also [Ficuciello et al., 2011]). However, software synergies clearly do not impact the simplification of the design of physical hands. 

The possible applications of the synergy concept however are not limited to software. Robotic hand implementing hardware synergies can be build, reducing the number of motors, but preserving the ability to achieve most grasping tasks. The design proposed in [Brown and Asada, 2007], for instance, adopts a train of pulleys of different radii to transmit simultaneously different motions to each joint. Motions corresponding to two synergies can be superimposed via a mechanism with tendons and idle pulleys, as illustrated in the simplified scheme of fig. 3. 

Both the software synergies [Ciocarlie et al., 2007], and the hard synergies [Brown and Asada, 2007] adopt a model of the hand with a number of independent actuators (or Degrees of Actuation, DoA) smaller than the number of joints (or degrees of Freedom, DoF). In both cases, this causes the hand to move 

in a way that do not necessarily comply with the shape of an object to be grasped, hence resulting in few contacts being established between the hand and the object. To this problem, some fixes can be considered, such as e.g. stopping the motion of each finger when it comes in contact with the grasped object, while prosecuting motion of others, or introducing a complementary actuation system for modifying the shape of synergies. While these techniques can be considered to simplify the grasp approaching phase design, they do not benefit from synergies to control grasping forces. 

## _C. Soft Synergies_ 

To take advantage of synergistic approach both in the pre-grasp phase and in contact force control, the idea of _soft synergies_ was introduced and discussed in [Bicchi et al., 2011]. In this model, synergy coordinates define the configuration of a _virtual hand_ , toward which the real one is attracted by an elastic field. To describe this situation, we introduce a _reference configuration_ vector _qr ∈_ R<sup>_♯q_</sup> , describing the configuration of the virtual hand. In this model, the motion of the virtual hand is directly controlled in the synergy space as 



The difference between the real position of the hand and its reference configuration generates the joint torques, which, at equilibrium, balance the interaction forces between the real hand and the grasped object. In formulae, defining a _joint stiffness_ matrix _Kq_<sup>_s∈_R</sup><sup>_♯q×♯q_,thejointtorquesinthesoft</sup> synergy model are given by 



By kineto-static duality, introducing the generalized force in the synergy space _δε ∈_ R<sup>_♯σ_</sup> , one has immediately that 



The soft synergy model can be used to control grasping forces by either commanding the virtual hand posture, as for example in [Gabiccini et al., 2011], or varying the joint stiffness matrix (see below (17)). 

A implementation via software of this approach was demonstrated in [Wimboeck et al., 2006] on the DLR HAND II, a fully actuated hand with programmable gains, which can simulate variable joint stiffness. A hardware implementation of a fully variable stiffness hand, using an antagonist pair of actuators per each joint, as sketched in fig. 4, was presented in [Grebenstein et al., 2011]. Although this hand has the potential for unprecedented versatility and performance, it does not address the simplification goals of this paper. 

One important aspect of the soft synergy model, which can be observed in the comparison between (10) and (11), is that a soft synergy hand can reduce the number of DoA while retaining all its kinematic DOFs, leaving the fine adjustment of the _♯q − ♯σ_ remaining movements to the compliance model. A conceptual hardware implementation of this idea is shown in fig. 5, where springs are used in series with a mechanism similar to that of fig. 3. Such a reduced-DoA soft synergy 

5 



Fig. 4. Full Variable Stiffness Actuation. Schematics of a hand with same kinematics as in fig. 2, where each joint is powered by variable stiffness agonist-antagonist actuators. 



Fig. 5. Soft Synergy Actuation. Schematics of a hand with same kinematics as in fig. 2, where all the joints are moved according to soft synergy actuation system. 

hand can be easily modeled by considering (11), (12) and (13), along with the grasp equation (8). In particular, for zero external wrenches on the object, for the joint torques it holds 



where _Qτ ∈_ R<sup>_♯q×♯q_</sup> was described in (9). Substituting (14) in (12), taking into account (11), we obtain 



Defining the matrix 





Fig. 6. Shape-Adaptive Underactuation. Schematics of a hand with same kinematics as in fig. 2, where all the joints are powered by an Adaptive Under-Actuated distribution system. 

from (8), it immediately follows that 



Equation (17) give us a complete description of the variation of the hand/object configuration as a consequence of the synergistic displacements. 

Applying (17) to (13), we can further evaluate the corresponding generalized force to be applied at the synergy actuator as 



Inverting this result, we arrive to 



Substituting (19) in (15), the hand joint displacement becomes 



Therefore, substituting (20) in (8), the complete system variation, depending on the soft synergy forces, is finally obtained. 

Although the idea of soft synergy actuation sketched in fig. 5 appears to provide an elegant solution to the problem of simple hand design, merging the natural motion inherited from the postural synergy approach with adaptivity due to compliance, its implementation in a mechanical design unfortunately turned out not to be very easy or practical, at least in our attempts. 

## _D. Adaptive Synergies_ 

A distinct thread of research work has addressed the design of simple robot hands via the use of a small number of actuators without decreasing the number of DOF. This approach, authoritatively described in [Birglen et al., 2008], is referred to as _underactuation_ and has produced a number of interesting hands since the earliest times of robotics. For further details the reader can refer 

6 



Fig. 7. Adaptive Synergies. Schematics of a hand with same kinematics as in fig. 2, where all the joints are controlled by two adaptive synergies. 

limits, clutches, and springs [Birglen et al., 2008]. Reasons for adding passive elements are manifold, including avoiding tendon slackness and ensuring the uniqueness of the position of the hand when not in contact with the object. 

Consider the model of an underactuated hand with elastic springs depicted in fig. 7, that we will call, henceforth, _adaptive synergy_ actuation. Notice that springs are arranged in parallel with the actuation and transmission mechanism, as opposed to the soft synergy model in fig. 5 where they are in series. Defining a joint stiffness matrix as _Kq_<sup>_a∈_R</sup><sup>_♯q×♯q_,the</sup> balance equation (22) is rewritten as 



Considering (23) and (14), it immediately follows that 



Thus, substituting this in (8), we obtain a description of the hand/object equilibria caused by the application of given actuator forces. 

If instead actuators are modeled as position sources, defining the matrix 



to [Tomovic and Boni, 1962], [Hirose and Umetani, 1978], [Rovetta, 1981], and also to [Lalibert´e and Gosselin, 1998], [Carrozza et al., 2004], [Gosselin et al., 2008] and [Dollar and Howe, 2010]. 

The basic idea enabling shape adaptation in underactuated hands is that of a differential transmission, the well-known mechanism used to distribute motion of a prime mover to two or more DOFs. Differentials can be realized in various forms, e.g. with gears [Laliberte et al., 2002], closed-chain mechanisms [Laliberte et al., 2002], or tendons and pulleys [Hirose, 1985], and concatenated so as to distribute motion of a small number of motors to all finger joints _q_ . Letting the vector _z ∈_ R<sup>_♯z_</sup> , with _♯z ≤ ♯q_ , denote the position of the prime movers, a general differential mechanism is described by the kinematic equation 



where _R ∈_ R<sup>_♯z×♯q_</sup> is the transmission matrix, whose element _Rij_ is the transmission ratio between the _i_<sup>th</sup> actuator to the _j_<sup>th</sup> joint. Fig. 6 conceptually illustrates a tendon-pulley differential mechanism with a single motor actuating three joints. By kineto-static duality, the relationship between the actuation force vector _η ∈_ R<sup>_♯z_</sup> and the joint torques is 



The kinematic model (21) highlights the non-uniqueness of the position attained by an underactuated hand. Indeed, being the transmission matrix _R_ a rectangular fat matrix, an infinity of possible hand postures _δq_ exist which satisfy (21) for a given actuator position _δz_ , their difference belonging to the kernel of _R_ . 

While it is exactly these kernel motions that provide underactuated hands with the desirable feature of _shape adaptivity_ , in practice these hands associate to differential mechanisms the use of passive elements such as mechanical 

and by substituting equation (24) in (21) and inverting, we find 



Substituing this in (24), we then obtain 



Finally, a complete system description in the case of actuator position control is given by substituting (27) in (8). 

## _E. From Soft to Adaptive Synergies_ 

Summarizing the discussion so far, we have seen that two design techniques for multiarticulated hands with simple mechanics stand out for different reasons. The method of soft synergies provides a sound theoretical basis for the design of anthropomorphic hands with a principled way to compose multiple motion primitives and a well understood neuroscientific rationale, but not an effective technological implementation. On the other hand, underactuated hands have desirable adaptivity to shapes, and can be effectively implemented with simple differential and elastic elements. In this section, we show how an underactuated hand can be indeed designed so as to realize a soft-synergy model. 

Assuming that a desired soft synergy model is assigned trough its synergy and stiffness matrices, _S_ and _Kq_<sup>_s_</sup> respectively, our goal is to find a corresponding adaptive synergy model, identified by a transmission matrix _R_ and a joint stiffness _Kq_<sup>_a_,whichexhibitsthesamebehavior,atleast</sup> locally around an equilibrium configuration. 

As shown in the previous sections, the behavior of the hand/object system is slightly different if the hand is position controlled or force controlled. This holds true for both soft and adaptive synergy model. Nevertheless, in all of the cases, the system is described as a linear map from an independent 

7 

variable _δyi_ , that can be one of _{δσ, δϵ, δz, δη}_ , and the joint displacement as _δq_ = _Aiδyi_ , where _Ai_ is taken from one of (15), (20), (24) or (27), respectively. By means of (8), the joint displacement describes the variation of the dependent variables at the hand/object level. 

The map can be also defined in the opposite direction, starting from a given adaptive synergy, to obtain a corresponding soft synergy. The total amount of possible maps is eight, considering both the case of position and force control. 

We will describe now the procedure to find one of such mappings, from a given position controlled soft synergy model to the corresponding position controlled adaptive synergy hand. All the other maps can be found with similar procedures, and the results will be discuss later. 

The hand/object behavior for a position controlled soft synergy hand is defined by (15), while the behavior of an adaptive underactuated hand is controlled by (27). To match them means to impose 



Looking at the span of the second term of the previous equation, it is possible to see that 



since the term � _RH_<sup>_a_</sup> _R_<sup>_T_�</sup><sup>_−_1</sup> is a square full rank matrix. As a consequence, the span of the two terms in (28) can be matched by imposing 



where matrix _M_ can be any full rank square matrix of suitable dimensions, which can be used as design parameter and accounts also for measurement units harmonization. To complete the map, a relationship has to be defined from _δσ_ to _δz_ . Given the choice on (30), a suitable relationship is 



With similar consideration, it is possible to prove that, even considering all the other possible actuation combinations, the map between soft and adaptive synergies can always be written as in (30). It is worthwhile noting that, by the choice _Kq_<sup>_a_=</sup><sup>_K_</sup> _q_<sup>_s_=</sup><sup>_Kq_,rememberingthedefinitionsin(16)and(25),</sup> the map in (30) can be simplified to 



in accordance with the results shown in [Grioli et al., 2012]. With some computation, a control map, similar to (31), can be found for any actuation combination. Without going into the details, we only report that in the “position controlled soft synergy – force controlled adaptive synergy” case, the control laws can be translated by the simple relation 



It is important nothing that (33) abstracts from the knowledge of _Qτ_ , that is from the knowledge of the object being grasped. In other words this means that this case allows to design a force controlled adaptive synergy hand which behaves, with respect to the grasped object, as a position controlled soft synergy hand. 



<!-- Start of picture text -->
(a) one synergy (b) four synergies<br><!-- End of picture text -->





Fig. 8. A modular hand prototype with adaptive synergies. Left: an assembly with two 4-phalanges fingers, a 2-phalanges thumb, and a single adaptive synergy. Right: a prototype with three equal fingers and four adaptive synergies. 



<!-- Start of picture text -->
(a) palm (b) finger front (c) finger side<br><!-- End of picture text -->





Fig. 9. Arrangement of the differential transmission to implement four adaptive synergies. Notice that the pulleys mounted on the finger (panel b) are idle, to allow a differential effect: the total tendon displacement is proportional to the weighted sum of the joint angles where the weights are the pulley radii. This implies that a given tendon displacement is compatible with different joint configurations, implementing a differential relationship. 

## III. A MODULAR HAND WITH FOUR ADAPTIVE SYNERGIES 

To validate the approach of adaptive synergies and to demonstrate and analyse the effectiveness of the integration of multiple synergies in a single device, a proof-of-concept, rapidly prototyped hand was realized. The hand is conceived as a modular platform, which can accommodate for different numbers of phalanges, fingers, and synergies (see fig. 8). As the hand is not anthropomorphic, the choice of postural synergies from a human grasp database would make no sense. In order to test our design concepts, therefore, we chose the four synergies heuristically. However, we did implement the constraint on these artificial synergies to be orthogonal. 

A schematic of a single stage is shown in fig. 9(a), containing a servomotor and two differential gears used to transmit the torque from the motors to the tendons routed through fingers. From each stage three tendons (one for each finger) go up to the palm. Fig. 9(b) shows how actuation tendons of each synergy are put together and managed inside each finger. Each tendon is routed through each finger in a way similar to the solution shown in fig. 9(c). 

Some experimental tests were performed to demonstrate the main characteristics of the hand prototype. In the experiments reported, some simple grasp tests were performed to show the hand adaptiveness during grasp of objects (a sphere, a cylinder, 

8 



<!-- Start of picture text -->
(a)<br><!-- End of picture text -->





<!-- Start of picture text -->
(b)<br><!-- End of picture text -->





<!-- Start of picture text -->
(c)<br><!-- End of picture text -->





<!-- Start of picture text -->
(d)<br><!-- End of picture text -->



Fig. 10. Hand prototype during the execution of some simple grasps. Only one synergy is used to grasp four test objects. Despite this, depending by the actuation variable, grasped object shape, contact point positions and internal forces, different grasp configurations can be achieved. 

a box and a L-shaped polyhedron). Pictures of the resulting grasp positions are shown in fig. 10, showing the adaptivity allowed by the use of differential transmission. 

## IV. THE PISA/IIT SOFTHAND 

In this section we apply the adaptive synergy design approach of fig. 7 to the design of a humanoid hand. The hand was designed according to few specifications. On the functional side, requirements are to grasp as wide a variety of objects and tools as possible, among those commonly used by humans in everyday tasks. The hand should be primarily able to effect a _whole hand grasp_ of tools, properly and strongly enough to operate them under arm and wrist control, but also be able to achieve _tip grasps_ . No in–hand dexterous manipulation is required for this prototype. The main nonfunctional requirements are resilience against force, overexertion and impacts, and safety in interactions with humans. The hand should be lightweight and self-contained, to avoid encumbering the forearm and wrist with motors, batteries and cabling, along with cost effectiveness. 

To meet the first functional requirement, the hand was designed anthropomorphically, with 19 DOFs arranged in four fingers and an opposable thumb (fig. 11). To maximize simplicity and usability, however, the hand uses only one actuator. According to our design approach, the motor actuates the adaptive synergy as derived from a human postural database [Santello et al., 1998]. The mechanical implementation of the first soft synergy through shape– adaptive underactuation was obtained via the numerical evaluation of the corresponding transmission matrix _R_ and joint stiffness matrix _Kq_<sup>_a_appearingin(21)and(23).The</sup> addition of further degrees of actuation, for example in–hand manipulation capabilities, is possible in principle, following the design approach illustrated in the previous section, but is left for future work. The hand assembly design is shown in fig. 12. Each finger has four phalanges, while the thumb has three. The hand palm is connected to a flange, to be fixed at the forearm, through a compliant wrist allowing for three passively compliant DOFs. 

The wrist of the SoftHand is composed by two curved surfaces, able to roll one on the other. The contact between them is guaranteed by the use of elastic ligaments, arranged along the perimeter of the wrist. When relative motion of the surfaces arises, for example caused by an external load, a set 



Fig. 11. Kinematics of the Pisa/IIT SoftHand. Revolute joints are in dark gray, while rolling–contact joints are in light gray. 



Fig. 12. A three–dimensional view of the Pisa/IIT SoftHand. Main components (the motor, the battery pack and the electronic control board), joints and wrist architecture are highlighted. 

of elastic forces appears. The wrist comes back to the original configuration when the external load is removed. 

In rest position, with fingers stretched out and at a relative angle of about 15<sup>_◦_</sup> in the dorsal plane, the hand spans approximately 230 mm from thumb to little finger tip, is 235 mm long from the wrist basis to the middle finger tip and has 40 mm maximum thickness at the palm. The requirement on power grasp implies that the hand is able to generate a high enough grasping force, and to distribute it evenly through all 

9 

contacts, be them at the fingertips, the inner phalanges, or the palm. These goals are naturally facilitated by the shape adaptivity of the soft synergy approach, yet they also require strong enough actuation and, very importantly, low friction in the joints and transmission mechanisms. 

The requirement on resilience and safety was one of the most exacting demands we set out for our design, as we believe these to be crucial features that robots must possess to be of real use in interaction with, and assistance to, humans. This is only more true for hands, the body part primarily devoted to physical interaction with the environment for exploration and manipulation. To achieve this goal, we adopted a non-conventional “soft robotics” design of the mechanics of the hand, that fully exploits the potential of modern material deposition techniques to build a rather sophisticated design with rolling joints and elastic ligaments at very low cost. A first departure form conventional design is the use of rolling contact articulations to replace standard revolute joints. Our design is inspired to a class of joints known as COmpliant Rolling-contact Elements (CORE) [Cannon and Howell, 2005], [Jeanneau et al., 2004], aka “Rolamite” or “XRjoints” joints [Cadman, 1970] (see fig. 13). Among these, Hillberry’s design of a rolling joint [Hillberry and Hall Jr, 1976] is particularly interesting to our purposes. A Hillberry joint consists of a pair of cylinders 



<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->





Fig. 13. Schematic illustration of two examples of COmpliant Rolling– contacts Elements (CORE): a Rolamite joint (a) and a Hillberry joint (b). 

in rolling contact on each other, held together by metallic bands, which wrap around the cylinders on opposite sides as schematically shown in fig. 13. In Hillberry joints, the band arrangement results in a compliant behavior in flexion but rigid in traction. The joint forms a higher kinematic pair, whose motion is defined by the profile of the cylinders, and exhibits very low friction and abrasive wear. The joint behaves more similarly to the human articulation than simple revolute joint, and for this reason was originally proposed for knee prostheses [Hillberry and Hall Jr, 1976]. Hillberry joints have been used in few robotic applications before, including robot hands [Ruoff, 1985]. Fig. 11 shows how we used CORE joints in the design of the Pisa/IIT SoftHand. In particular, we adopted CORE joints for all the interphalangeal, flexion/extension articulations. Conversely, conventional revolute joints was used for metacarpophalangeal, abduction/adduction articulations. Our design introduces a few important modifications of existing rolling– contact joints, which are illustrated in fig. 14. Firstly, metallic bands were replaced by elastic ligaments, realized 



<!-- Start of picture text -->
(a) Perspective view<br>(b) Side view and movement<br><!-- End of picture text -->

Fig. 14. Design of the compliant rolling–contact joint used in the interphalangeal joints of the Pisa/IIT SofHands: (a) perspective view with rolling cylinders with matching multi-stable profile; (b) lateral view, showing the arrangement of ligaments and tendons. 

a polyurethane rubber able to withstand large deformations and fatigue, and are fixed across the joint with an offset in the dorsal direction. Suitable pretensioning of the ligaments, together with a carefully designed profile of the two cylinders, introduce a desirable passive stability behaviour, with an attractive equilibrium at the rest configuration with fingers stretched. The elastic ligaments are polyurethane rubber segments of 2mm diameter, characterized by 88 Shore A hardness. The rest length of the ligaments is 10mm. Some pre-tensioning is applied with a stretch in the range between 2 to 5 mm. All the long fingers proximal flexion joints have lower values of pre-tensioning, with respect to all the other joints, such to guarantee a hand motion similar to the first human synergy, as explained in section II. 

The coupled rolling cam profiles are designed on a circular primitive with radius 6.5mm. The actuation tendon is wrapped around pulleys with radius 3.5mm. All the radii are the same for all the rolling profiles and the pulleys, in order to obtain a modular design. The rolling cam profile is realized on cylinder portions flanked by lateral walls on both sides, whose slope is about 80<sup>_◦_</sup> (see fig. 14 and fig. 16). When two phalanges are assembled, such walls are housed in a fitting recess of the matching phalanx. These features of our design are particularly important for the system to behave softly and safely in contact, and to recover from force overexertion, due e.g. to impacts or jamming of the hand, making the hand automatically return to its correct assembly configuration. The joint can withstand severe disarticulations (cf. fig. 16) and violent impacts (fig. 17). 

The design of interphalangeal joints does not require the use of screws, shafts, bearings or gears. As can be seen in fig. 14, a few teeth of an involute gear of vanishing height are indeed integrated in the cam shape, to better support tangential loads at the joint. 

Actuation of the hand is effected through a single Dyneema tendon routed through all joints using passive anti-derailment pulleys. The tendon action flexes and adducts fingers and thumb, counteracting the elastic force of ligaments, and implementing adaptive underactuation without the need for 

10 



Fig. 15. Partially exploded line sketch of the Pisa/IIT SoftHand. The tendon routing distributes the motion to all joints. 



<!-- Start of picture text -->
(a) Grasp force test object (b) Holding torque test object<br><!-- End of picture text -->





Fig. 18. Sensorized object for force measurements (a), sensorized object for torque measurements (b). 

differential gears (fig. 15). 

## V. EXPERIMENTAL RESULTS 

The prototype of the Pisa/IIT SoftHand (fig. 1) was built to perform experimentally tests. The actuator powering the hand is a 6 W Maxon motor RE-max21 with a reduction ratio of 84:1 equipped with a 12 bit magnetic encoder (Austrian Microsystems AS5045) with a resolution of 0 _._ 0875<sup>_◦_</sup> . 

The embedded electronic unit hosting sensor processing, motor control and communication is located in the hand back, along with the battery pack. The opening/closing of the hand is controlled via a single set point reference, communicated via one of the available buses (SPI and RS-485). 

During experiments the hand worn an off-the-shelf working glove with padded rubber surfaces, supplying contact compliance and grip. 

## _A. Force and torque measurements_ 

An ATI nano 17 F/T sensor with UDP interface was used to measure holding force and torque of the robotic hand. In the first case, a split cylinders, represented in fig. 18(a), was used to measure the grasp force. The cylinder is 120 mm high and has a diameter of 45 mm. The disk to measure maximum holding torque is represented in fig. 18(b). The disk is 20 mm high and has a diameter of 95 mm. 

In fig. 19(b) we report force acquisitions during sensorized object grasp. It is possible to notice how forces increased when fingers get in contact with the sensorized cylinder (step behavior of the lines in fig. 19(b)). We achieved a maximum holding torque of 2 Nm and maximum holding force of about 



<!-- Start of picture text -->
(a) Torques<br>2<br> Tx<br>1.5  Ty<br> Tz<br>1<br>0.5<br>0<br>−0.5<br>−1<br>0 2 4 6 8 10 12 14 16<br>Time (s)<br>(b) Forces<br>20<br> Fx<br>15  Fy<br> Fz<br>10<br>5<br>0<br>−5<br>−10<br>−15<br>−20<br>0 2 4 6 8 10 12 14 16 18<br>Time (s)<br>Torque (Nm)<br>Force (N)<br><!-- End of picture text -->

Fig. 19. Torques and forces of the robotic hand during grasp task. 

20 N along the _z_ axis. These limits appear to be dictated by the motor size rather than by the hand construction. Although we did not go through an exhaustive analysis, in an occasional experiment with a stronger motor a holding torque of 3 _._ 5 Nm and holding force of 28N were obtained. For more details on the performed experiments, pls. see also the accompanying multimedia extension 1. 

## _B. Grasp Experiments_ 

To test the adaptiveness of the robotic hand, the grasp of several objects of daily use in a domestic or lab environment were performed. Grasp experiments were performed in three different conditions: 1) the hand wrist fixed on a table and the object placed in the grasp; 2) the object placed on a table and the hand mounted on a robot arm, and 3) the hand wrist fixed to the forearm of a human operator. 

Some examples of grasps achieved in the first condition are reported in fig. 20. 

To test usage of the Pisa/IIT SoftHand in a robotic scenario, the hand was mounted at the end-effector flange of a KUKA Light–Weight robot arm. Fig. 21 shows some of the grasps tested. Notice that the robot was manually programmed to reach an area were the object was approximately known to lie, and no grasp planning phase was executed. Rather, the hand was given a closure command by software. The closure time, as well as the robot trajectory, were preprogrammed in the examples shown, and were the same for each object lying roughly in the same area. Video sequences of the performed 

11 



<!-- Start of picture text -->
(a) Finger Side bend (b) Finger Back bend (c) Finger Twist (d) Finger Skew bend<br>(e) Side bend (f) Back bend (g) Twist (h) Skew bend<br><!-- End of picture text -->









Fig. 16. The Pisa/IIT SoftHand joints can withstand severe force overexertion in all directions, automatically returning to the correct assembly configuration. 









Fig. 17. A photo-sequence showing the PISA/IIT SoftHand during a violent impact with a stiff surface. 

experiments can be seen on the multimedia extension 1, including one showing a simple application of grasp force control to first hold, and then operate a spray bottle, and one illustrating on–the–fly grabbing of a water bottle with the arm sweeping a table top at a speed of 1 m/s ca. 

Finally, to test the capability of the Pisa/IIT Hand to acquire complex grasps of objects randomly placed in the environment, we developed a wearable mechanical interface (see fig. 22) allowing an operator to use our hand as a substitution of his/her own. The interface can be strapped on the operator’s forearm and can be controlled by the operator acting on a lever with his/her real hand (see fig. 21(a)). In fig. 23 we report some grasps executed with the human interface (condition 2 above). Again, more results can be seen in the accompanying multimedia extension 1. 

In summary, a total of 107 objects of different shape was successfully grasped, with a whole hand or a tip grasp, in all conditions previous considered, during our tests: bottle, reel, pincer, stapler, pen, phone handset, plier, teddy bear, cup, handle, spray, computer mice, hot–glue gun, human hand, cell phone, glass, screw–driver, hammer, file, book, coin, scotch tape holder, ball, tea bag, ketchup bottle, hamburger, camera, tripod stand, cutter, trash can, keyboard, torch, battery container, battery (AA), small cup, measuring tape, caliper, wrench, lighter, eraser, world map (globe), remote control, hex key, AC adapter, keyring, spoon, fork, knife, hand tissue box, liquid soap dispenser, corkscrew, rag, candy, calculator, slice of cake, rubber-stamp, spring, paper, cellphone case, rubber band, 



<!-- Start of picture text -->
(a)<br>(b)<br><!-- End of picture text -->



Fig. 22. (a) Components of the interface for human use of the Pisa/IIT SoftHand. The angle position of the lever is acquired by the electronics board and adopted as reference position to drive the actuator of the hand. (b) Appearance of the assembled human interface prototype. 

bottle top, watch, umbrella, broom, garbage scoop, scarf, chair, schoolbag, USB cable, glue stick, wallet, credit card, sponge, 

12 



<!-- Start of picture text -->
(a) Cube Grasp (b) Bottle Grasp (c) Reel Grasp (d) Pincer Grasp (e) Stapler Grasp<br>(f) Cube Dimensions (g) Bottle Dimensions (h) Reel Dimensions (i) Pincer Dimensions (j) Stapler Dimensions<br>37 mm<br>50 mm<br>130 mm<br>65 mm 57 mm<br>90 mm<br>74 mm 70 mm 160 mm<br>205 mm 155 mm<br><!-- End of picture text -->

Fig. 20. Some experimental grasps performed with the Pisa/IIT hand, with the object placed in the hand by a human operator. 



<!-- Start of picture text -->
(a) Case Handle Grasp (b) Spray Grasp (c) Cup Grasp (d) Telephone Grasp<br><!-- End of picture text -->









Fig. 21. Grasps executed with the Pisa/IIT SoftHand mounted on a Kuka Light Weight Robot: handbag (a), spray (b), cup(c) and telephone (d). 



<!-- Start of picture text -->
(a) Telephone Grasp (b) Teddy Bear Grasp (c) Book Grasp (d) Strawberry Grasp<br><!-- End of picture text -->









Fig. 23. Some examples of grasps executed with the robotic hand mounted on a wearable Human Interface: telephone (a), Teddy Bear (b), book (c), and strawberry (d) . 

13 

REFERENCES 

pencil sharpener, straight edge, safety lock, mouse pad, hard disk, jacket, drill, chalk, notebook, blackboard eraser, door lock, square ruler, scissors, eyeglasses, deodorant, USB key, hat, headphones, cigarette, helmet, screw (M8), clamp, fridge magnet, drill bit, table calendar, saw, tape cassette, beauty case, bubble gum box, bubble gum, tissue pocket, dish, poster. 

The more difficult situation is in grasping very thin objects. However, since grasp limitations of the prototype are also influenced by the operator training, it is not easy to quantify grasp limitations without resorting to further investigations, which are out of the scope of this paper. 

One of the main lessons learned through these experiments is that, while all grasps could be easily achieved by the hand when operated by a human, programming the robot to achieve the same grasps was in some cases rather complex. One of the main reason for this is, in our understanding, that the human operator quickly learns how to exploit the intrinsic adaptivity of the hand, including the wrist compliance, to shape the hand before and during grasp. This is done with the help of object features and/or environmental constraints, notably the table top and walls. This observation hints that autonomous learning and planning for soft robot grasping might have to be focused on constraint–based motion rather than on free–space, multi-DOF hand shaping. 

## VI. CONCLUSION 

This paper presented the design and implementation of the Pisa/IIT SoftHand, along with the theoretical framework behind that justifies the main design choices. The important aspect of the hand actuation pattern is considered first, reviewing various past and recent approaches, and finally considering adaptive synergies as preferred choice. 

The first prototype of the Pisa/IIT SoftHand, a highly integrated robot hand characterized by a humanoid shape and good robustness and compliance, is presented and discussed. The hand is finally validated experimentally through extensive grasp cases and grasp force measurements. Results are also reported in an the multimedia extension 1. 

## ACKNOWLEDGMENTS 

The authors would like to thank Andrea Di Basco, Fabrizio Vivaldi, Simone Tono and Emanuele Silvestro for their valuable help in the realization of the prototypes, and Manuel Bonilla for programming the robot grasping experiments. 

This work is supported by the European Commission under the CP-IP grant no. 248587 “THE Hand Embodied”, within the FP7-2007-2013 program “Cognitive Systems and Robotics”, and the ERC Advanced Grant no. 291166 “SoftHands”. 

## APPENDIX 

The multimedia extensions to this article are at: http://www.ijrr.org. 

|Extension|Type|Description|
|---|---|---|
|||The video shows the Pisa/IIT SoftHand|
|1|Video|performing many different grasps,|
|||in addition to robustness and grasp force tests.|



- [Bicchi, 1994] Bicchi, A. (1994). On the problem of decomposing grasp and manipulation forces in multiple whole-limb manipulation. _Int. Journal of Robotics and Autonomous Systems_ , 13:127–147. 

- [Bicchi et al., 2011] Bicchi, A., Gabiccini, M., and Santello, M. (2011). Modelling natural and artificial hands with synergies. _Philosophical Transactions of the Royal Society B: Biological Sciences_ , 366(1581):3153– 3161. 

- [Birglen et al., 2008] Birglen, L., Gosselin, C., and Lalibert´e, T. (2008). _Underactuated robotic hands_ , volume 40. Springer Verlag. 

- [Brown and Asada, 2007] Brown, C. and Asada, H. (2007). Inter-finger coordination and postural synergies in robot hands via mechanical implementation of principal components analysis. In _Intelligent Robots and Systems, 2007. IROS 2007. IEEE/RSJ International Conference on_ , pages 2877–2882. IEEE. 

- [Cadman, 1970] Cadman, R. (1970). Rolamite - geometry and force analysis. Technical report, Sandia Laboratories. 

- [Cannon and Howell, 2005] Cannon, J. R. and Howell, L. L. (2005). A compliant contact-aided revolute joint. _Mechanism and Machine Theory_ , 40:1273–1293. 

- [Carrozza et al., 2004] Carrozza, M., Suppo, C., Sebastiani, F., Massa, B., Vecchi, F., Lazzarini, R., Cutkosky, M., and Dario, P. (2004). The spring hand: development of a self-adaptive prosthesis for restoring natural grasping. _Autonomous Robots_ , 16(2):125–141. 

- [Castellini and van der Smagt, 2013] Castellini, C. and van der Smagt, P. (2013). Evidence of muscle synergies during human grasping. _Biological Cybernetics_ , 107(2):233–245. 

- [Catalano et al., 2012] Catalano, M. G., Grioli, G., Serio, A., Farnioli, E., Piazza, C., and Bicchi, A. (2012). Adaptive synergies for a humanoid robot hand. In _IEEE-RAS International Conference on Humanoid Robots_ , Osaka, Japan. 

- [Ciocarlie et al., 2007] Ciocarlie, M., Goldfeder, C., and Allen, P. (2007). Dexterous grasping via eigengrasps: A low-dimensional approach to a high-complexity problem. In _Proceedings of the Robotics: Science & Systems 2007 Workshop-Sensing and Adapting to the Real World, Electronically published_ . Citeseer. 

- [Dollar and Howe, 2010] Dollar, A. and Howe, R. (2010). The highly adaptive sdm hand: Design and performance evaluation. _The International Journal of Robotics Research_ , 29(5):585. 

- [Easton, 1972] Easton, T. (1972). On the normal use of reflexes: The hypothesis that reflexes form the basic language of the motor program permits simple, flexible specifications of voluntary movements and allows fruitful speculation. _American Scientist_ , 60(5):591–599. 

- [Ficuciello et al., 2011] Ficuciello, F., Palli, G., Melchiorri, C., and Siciliano, B. (2011). Experimental evaluation of postural synergies during reach to grasp with the ub hand iv. In _Intelligent Robots and Systems (IROS), 2011 IEEE/RSJ International Conference on_ , pages 1775–1780. IEEE. 

- [Gabiccini et al., 2011] Gabiccini, M., Bicchi, A., Prattichizzo, D., and Malvezzi, M. (2011). On the role of hand synergies in the optimal choice of grasping forces. _Autonomous Robots_ , 31(2 - 3):235 – 252. 

- [Gabiccini et al., 2012] Gabiccini, M., Farnioli, E., and Bicchi, A. (2012). Grasp and manipulation analysis for synergistic underactuated hands under general loading conditions. In _Robotics and Automation (ICRA), 2012 IEEE International Conference on_ , pages 2836–2842. IEEE. 

- [Gosselin et al., 2008] Gosselin, C., Pelletier, F., and Laliberte, T. (2008). An anthropomorphic underactuated robotic hand with 15 dofs and a single actuator. In _Robotics and Automation, 2008. ICRA 2008. IEEE International Conference on_ , pages 749–754. 

- [Grebenstein et al., 2011] Grebenstein, M., Albu-Schaffer, A., Bahls, T., Chalon, M., Eiberger, O., Friedl, W., Gruber, R., Haddadin, S., Hagn, U., Haslinger, R., et al. (2011). The dlr hand arm system. In _Robotics and Automation (ICRA), 2011 IEEE International Conference on_ , pages 3175– 3182. IEEE. 

- [Grioli et al., 2012] Grioli, G., Catalano, M., Silvestro, E., Tono, S., and Bicchi, A. (2012). Adaptive synergies: an approach to the design of underactuated robotic hands. In _Intelligent Robots and Systems, 2012. IROS 2012. IEEE/RSJ International Conference on_ , page submitted. IEEE. 

- [Hillberry and Hall Jr, 1976] Hillberry, B. and Hall Jr, A. (1976). Rolling contact joint. US Patent 3,932,045. 

- [Hirose, 1985] Hirose, S. (1985). Connected differential mechanism and its applications. _Proc. 2nd ICAR_ , pages 319–326. 

- [Hirose and Umetani, 1978] Hirose, S. and Umetani, Y. (1978). The development of soft gripper for the versatile robot hand. _Mechanism and machine theory_ , 13(3):351–359. 

14 

- [Jeanneau et al., 2004] Jeanneau, A., Herder, J., Lalibert´e, T., and Gosselin, C. (2004). A compliant rolling contact joint and its application in a 3- dof planar parallel mechanism with kinematic analysis. _ASME Conference Proceedings_ , 2004(46954):689–698. 

- [Laliberte et al., 2002] Laliberte, T., Birglen, L., and Gosselin, C. (2002). Underactuation in robotic grasping hands. _Machine Intelligence & Robotic Control_ , 4(3):1–11. 

- [Lalibert´e and Gosselin, 1998] Lalibert´e, T. and Gosselin, C. (1998). Simulation and design of underactuated mechanical hands. _Mechanism and Machine Theory_ , 33(1):39–57. 

- [Latash et al., 2005] Latash, M. L., Krishnamoorthy, V., Scholz, J. P., and Zatsiorsky, V. M. (2005). Postural Synergies and their Development. _Neural plasticity_ , 12(2-3):119–30; discussion 263–72. 

- [Murray et al., 1994] Murray, R., Li, Z., and Sastry, S. (1994). _A mathematical introduction to robotic manipulation_ . CRC. 

- [Prattichizzo et al., 2010] Prattichizzo, D., Malvezzi, M., and Bicchi, A. (2010). On motion and force controllability of grasping hands with postural synergies. _Proceedings of Robotics: Science and Systems, Zaragoza, Spain_ . 

- [Rovetta, 1981] Rovetta, A. (1981). On functionality of a new mechanical hand. _Journal of Mechanical Design_ , 103:277. 

- [Ruoff, 1985] Ruoff, C. (1985). Rolling contact robot joint. US Patent 4,558,911. 

- [Santello et al., 2013] Santello, M., Baud-Bovy, G., and Joerntell, E. (2013). Neural bases of hand synergies. note: in review. 

- [Santello et al., 1998] Santello, M., Flanders, M., and Soechting, J. (1998). Postural hand synergies for tool use. _The Journal of Neuroscience_ , 18(23):10105–10115. 

- [Tomovic and Boni, 1962] Tomovic, R. and Boni, G. (1962). An adaptive artificial hand. _Automatic Control, IRE Transactions on_ , 7(3):3–10. 

- [Weiss and Flanders, 2004] Weiss, E. J. and Flanders, M. (2004). Muscular and postural synergies of the human hand. _Journal of neurophysiology_ , 92(1):523–35. 

- [Wimboeck et al., 2006] Wimboeck, T., Ott, C., and Hirzinger, G. (2006). Passivity-based object-level impedance control for a multifingered hand. In _Intelligent Robots and Systems, 2006 IEEE/RSJ International Conference on_ , pages 4621–4627. Ieee. 

- [Wimboeck et al., 2012] Wimboeck, T., Reinecke, J., and Chalon, M. (2012). Derivation and verification of synergy coordinates for the dlr hand arm system. In _CASE_ , pages 454–460. IEEE. 

