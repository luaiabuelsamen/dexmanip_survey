<!-- page 1 -->
 
Fig. 1. Increasing system dexterity can be accomplished by 
adding arm kinematic redundancy or hand complexity 
 
Abstract—This paper presents a high-level discussion of 
dexterity in robotic systems, focusing particularly on 
manipulation and hands. While it is generally accepted in the 
robotics community that dexterity is desirable and that end 
effectors with in-hand manipulation capabilities should be 
developed, there has been little, if any, formal description of 
why this is needed, particularly given the increased design and 
control complexity required. This discussion will overview 
various definitions of dexterity used in the literature and 
highlight issues related to specific metrics and quantitative 
analysis. It will also present arguments regarding why hand 
dexterity is desirable or necessary, particularly in contrast to 
the capabilities of a kinematically redundant arm with a simple 
grasper. Finally, we overview and illustrate the various classes 
of in-hand manipulation, and review a number of dexterous 
manipulators that have been previously developed. We believe 
this work will help to revitalize the dialogue on dexterity in the 
manipulation community and lead to further formalization of 
the concepts discussed here. 
I. INTRODUCTION 
HE concept of dexterity is regularly mentioned in the 
context of robotics research, but the term is typically 
applied broadly and qualitatively, most often in the context 
of anthropomorphic manipulation. Additionally, there has 
been little discussion regarding the means of implementing 
dexterity in robotic systems, with many researchers (the 
authors included) operating under the unstated assumption 
that dexterity should be implemented through highly 
functional, dexterous hands.  
The main reference and inspiration for hand dexterity and 
in-hand manipulation is typically and unsurprisingly the 
human hand. The sophistication of the human hand and its 
co-evolution with cognition is one of the most significant 
reasons for the amazing success of Homo sapiens in 
comparison to our most closely related primate relatives [1]. 
The development of the opposable thumb, which imparts the 
ability of the hand to perform precision grasps and in-hand 
manipulation, was particularly important in our rapid 
evolutionary development. 
As our primary means of physically interacting with the 
environment around us, the hand is an integral part of nearly 
all functional human manipulation [2]. These tasks range 
from tactile exploration of surfaces in the dark, simple 
grasping and movement of objects, application of large 
forces and torques through tool use, to complex in-hand 
 
This work was supported in part by the National Science Foundation 
grant IIS-0953856 and DARPA grant W91CRB-10-C-014 
R.R. Ma and A.M. Dollar are with the Yale School of Engineering and 
Applied Science, Department of Mechanical Engineering and Materials 
Science, 
New 
Haven, 
CT 
06511 
USA 
(email:{raymond.ma, 
aaron.dollar}@yale.edu).  
manipulation such as twirling a pen.    
Despite the extensive capabilities of the human hand, its 
level of functionality has proven to be extremely difficult to 
emulate. Mechanically, it is challenging to incorporate a 
large number of articulated degrees of freedom and the 
subsequently required number of actuators and transmission 
components. Limitations in actuation technology typically 
mean that increased controllable degrees of freedom results 
in decreased overall grip strength and grasp stability. 
Additionally, large numbers of small components lead to 
fragile mechanical construction and more frequent failures 
of the mechanism. 
From a controls perspective, the lack of high-quality, 
robust, and readily-available sensing technologies to provide 
precise and high-bandwidth feedback about the nature of the 
contact conditions and the internal states of the mechanism 
result in imprecise position and force outputs. These are 
further aggravated by limitations in computing power and 
bandwidth.  
Given these substantial challenges, why is in-hand 
manipulation truly needed? From an object-centric view of 
the problem, isn’t it sufficient to arbitrarily position and 
orient the object within some reasonable workspace volume, 
while being able to apply useful forces through the object? 
Since this capability can be accomplished with a redundant 
manipulator arm and a simple gripper (Fig. 1), are the 
complications associated with implementing hand dexterity 
for in-hand manipulation worth addressing?  
We begin this paper with a discussion of previous work 
related to classifying and quantifying dexterity in robotic 
manipulation. We then discuss the general problem of 
On Dexterity and Dexterous Manipulation 
Raymond R. Ma and Aaron M. Dollar, Member, IEEE 
T
The 15th International Conference on Advanced Robotics
Tallinn University of Technology
Tallinn, Estonia, June 20-23, 2011
978-1-4577-1159-6/11/$26.00 ©2011 IEEE
1


<!-- page 2 -->
 
dexterity and provide arguments for the justification for in-
hand manipulation, particularly in contrast to a highly 
dexterous, redundant manipulator arm and simple gripper. 
Finally, we overview the various types of manipulation that 
can be accomplished within the hand and provide examples 
from the literature of dexterous manipulators that have been 
previously developed, with a discussion of the tradeoffs of 
these in light of the utility arguments laid out earlier.    
II. BACKGROUND 
A number of interesting reviews have been published on 
the topic of dexterous manipulation and dexterous hands. In 
a review of a workshop on the design of the first dexterous 
hands, Hollerbach [3] defined dexterity as a feature that 
would make assembly lines more adaptive and flexible, 
reducing the need for custom fixtures in each assembly task. 
As a result, the most dexterous hand would be one that could 
serve as a general-purpose manipulator, one capable of 
performing the most diverse set of tasks and operations in a 
manufacturing environment. 
 In discussing the evaluation of manufacturing cells, 
Wright et al. [4] agreed with Hollerbach in that the primary 
benefit of dexterity is the increased ability of a system to 
deal with dynamic environments and a more varied set of 
tasks, though at the expense of power. His study also 
presents a general, subjective dexterity spectrum that 
attempts to compare the dexterous capabilities of various 
manipulators. This was part of an attempt to develop a 
classification system that could best match manipulators 
with dexterous tasks. Such a mapping of manipulators to 
tasks could be used as part of a design framework to more 
intelligently generate and evaluate hand systems.  
 Wright further proposes that all dexterous tasks can be 
decomposed into a set of primitive actions: free motion of 
robotic fingers, acquiring an optimal grasp, turning a 
grasped object about an axis, and redistributing finger-tip 
forces in order to enable finger-gaiting (these various 
manipulation primitives are described in detail in section 
IV). The topic of task decomposition into simpler, 
independent primitive motions is also repeated in various 
discussions of control systems for dexterous hands [5]. 
 Bicchi highlighted [6] a more contemporary state of 
dexterous manipulation research, focusing on the capabilities 
of multi-fingered robotic hands. He discusses the prevalence 
of anthropomorphic hand designs, arguing that while the 
human hand’s level of dexterity remains a lofty goal for 
robotic mechanisms to emulate, it may be necessary in 
applications such as prosthetics where aesthetic is a concern. 
Alternate hand designs, such as the DxGrip-II [7], suggest 
that anthropomorphic solutions may not be optimal for 
certain tasks. Various methods of dexterous manipulation, 
such as finger gaiting, re-grasping, and sliding/rolling, along 
with their mechanical requirements, are also detailed.   
 Okamura et al. [8] laid out the technical requirements and 
basic components for implementing dexterous manipulation, 
including planning strategies, hardware design, and physical 
system parameters. It was noted that the limits of any single 
hand (grasp) configuration are generally insufficient to 
satisfy the majority of dexterous tasks, which require 
changing between grasps in order to extend the kinematic 
limits of the system. She asserts that dexterous manipulation 
problems are object-centered and can be broken down into a 
series of grasps, or grasp gaits, where the set of feasible 
grasps, also known as the grasp map, is constrained by the 
desired trajectory of the object.  
A. Definitions of Dexterity 
These papers and others have put forth or utilized a 
definition of dexterity that varies considerably from one to 
the next. According to each, dexterity is: 
 “(The) capability of changing the position and orientation 
of the manipulated object from a given reference 
configuration to a different one, arbitrarily chosen 
within the hand workspace”, Bicchi 2000, [6]. 
 “(The) process of manipulating an object from one grasp 
configuration to another”, Li 1989, [9]. 
 “(When) multiple manipulators, or fingers, cooperate to 
grasp and manipulate objects”, Okamura 2000 [8]. 
 “(The) kinematic extent over which a manipulator can 
reach all orientations”, Klein/Blaho 1987 [10] 
 “Skill in use of hands” Sturges 1990 [11] 
The 
primary 
difficulty 
in 
defining 
dexterity 
is 
differentiating it from general manipulation. Often, the 
utilized definition of dexterity is anthropocentric, denoting 
precision manipulation tasks primarily between fingertips 
and other small finger-like appendages. In fact, many 
authors have deemed a robotic hand to be dexterous if it has 
multiple, individually-articulated fingers, particularly if it is 
in an anthropomorphic package, despite whether the system 
has actually been successful in performing dexterous tasks.  
For this discussion, we will focus on more generalized 
task and object-centric definitions of dexterity, focusing on 
the systems’ kinematic and dynamic capabilities as opposed 
to the similarity of their mechanical design to the human 
hand. Bicchi [6] suggests that dexterous manipulation is a 
case of general object manipulation within the hand 
workspace. Li [9] provides a similar definition, but also 
stipulates that the object must start and end within some 
stable grasp configuration. Okamura [8] generalizes the 
definition further, describing dexterity as a cooperative 
manipulation between multiple manipulators, implying that 
manipulators with simple end effectors alone are not capable 
of dexterous manipulation. Klein et al. [10] further supports 
this claim, arguing that dexterous manipulation cannot be 
kinematically minimal, and that dexterity measures the 
kinematic extent to which the manipulator can reach all 
orientations. By this definition, dexterous manipulators must 
have kinematic redundancy, a characteristic that is indeed 
found in the majority of mechanisms that would naturally be 
considered dexterous.     
While examples of dexterous manipulation in the 
literature 
predominantly 
involve 
multi-fingered 
and 
anthropomorphic hands, the definitions provided above do 
not constrain the interpretation of the manipulator or hand 
workspace 
such 
that 
non-fingered 
manipulators 
are 
2


<!-- page 3 -->
 
Fig. 2. Fractal, recursively-formed manipulator, where 
differentiation between “hand” and “arm” is dependent on the 
object size. 
excluded. Furthermore, it’s not unreasonable to apply these 
general definitions to locomotion, in which movement tasks 
utilizing cooperative actuation are performed that exceed the 
kinematic joint limits of its limbs. In locomotion, the system 
manipulates its own body position relative to the ground 
surface – essentially the inverse of what is considered 
dexterous manipulation. Indeed, there are many similarities 
between Okamura’s description of grasp gaits [8] and the 
formulation of stable walking patterns.  
III. ARM VS. HAND DEXTERITY 
The above descriptions and definitions of dexterity are 
sufficiently general such that there is not a clear 
differentiation 
between 
dexterity 
provided 
by 
the 
manipulator “arm” and the end-effector or “hand”. Indeed, 
the distinction between the two is not clear cut.  
A. Differentiating Arm and Hand 
In manufacturing and anthropomorphic systems, the arm 
is generally a 6- or 7- degree of freedom  linkage-based 
system (including a 3-dof wrist), to which the end effector, 
or hand, is attached. While this type of system exhibits clear 
differentiation between the arm/wrist and hand, this 
framework does not necessarily apply to all systems. In his 
description of a tentacle manipulator, Pettinato [12] suggests 
that the “hand” can be defined as the set of linkages in 
contact with the object, in which case the task and object 
would define the separation between the two. In the tentacle 
example, the degree of dexterity is also directly related to the 
number of linkages assumed to be part of that system’s 
“hand”.  
Consider another “handless” system where multiple 
manipulator arms without end-effectors work together to 
manipulate an object. Independently, each would only be 
capable 
of 
non-prehensile 
manipulation, 
but 
their 
cooperative behavior together falls under a typical definition 
of dexterity. Imagine also if these multiple manipulators 
were situated together as the end effector of another 
manipulator arm, in which case the distal set of manipulators 
might be naturally viewed as the hand. Accordingly, the 
scale of the object/task related to that of the overall system 
biases the interpretation of whether a mechanism is 
considered an “arm” or a “hand”.  
Taking this illustration to an extreme, consider a “fractal” 
manipulator, consisting of a series of successive smaller 
graspers anchored to the tip of one of the previous stage’s 
fingers (Fig. 2). For any given object or task, there is a 
particular grasper (i.e. matched finger pair) that is most 
appropriate based on the size of the object to be 
manipulated. This pair then determines the division between 
what is considered the “hand” (i.e. grasper) and the “arm” 
that imparts the manipulation capability. 
B. Arguments for Arm- vs. Hand-Based Manipulation 
Many researchers working in the area of robotic and 
prosthetic hands (the present authors included), acknowledge 
that some sort of dexterity within the hand is needed, or at 
least 
desirable. 
However, 
the 
motivation 
for 
such 
functionality has not been concrete. Why does a robotic end-
effector need perform a function other than grasping? As 
Wright [4] and others have stated, an increase in dexterity 
often results in an increase in complexity and a decrease in 
power and strength.  
We lay out a few arguments related to this question 
below, and briefly summarize them in Table I.  
 
1) “A Dexterous Arm with a Simple Gripper is Sufficient” 
If dexterous manipulation can be thought of from an 
object-centric perspective, it is desirable to have the ability 
to place the object in an arbitrary set of positions and 
orientations (six degrees of freedom) within some workspace 
while retaining the ability to do “something useful” with the 
object in that configuration – for instance, being able to 
write with a pen, apply force to insert and turn a key, etc.  
According to this (somewhat limited) description of task 
functionality, a simple gripper sufficient to stably grasp a 
wide range of objects combined with a highly dexterous arm 
should be able to accomplish most of the tasks needed. Even 
in cases where limitations in the starting grasp configuration 
of the object in the simple gripper conflicts with the desired 
task goal, the object might be “regrasped” (section IV.A) 
[13] to compensate for the lack of in-hand manipulation 
ability and accomplish the task.  
Given the greater simplicity in this approach, where the 
hand is for simple grasping and the arm is for manipulation 
Table I – Considerations for/against in-hand dexterity 
Advantages 
Disadvantages 
Greater precision 
Increased mechanical 
complexity 
Increased efficiency 
Decreased strength/power 
Increased generality, 
kinematic redundancy 
Increased control 
complexity 
Specialized for tasks of a 
certain scale 
Restricted to tasks of that 
certain scale 
3


<!-- page 4 -->
 
Fig. 3. Dexterity increases manipulability at arm joint limits 
 
Fig. 4. Obstacles can create additional arm limitations 
Fig. 5. Dexterity allows for tools to be more easily reoriented 
and external force application, a dexterous arm and a simple 
gripper is sufficient and appropriate for many manipulation 
tasks.  
 
2) “A Dexterous End-Effector can make up for Limitations 
in Arm Functionality” 
In practice, there are a number of situations in which the 
manipulator arm is not sufficiently functional to enable all 
desired manipulation tasks to be executed.  
For simple grippers, the configuration space of the object 
is limited by the configuration space of the arm, as the hand 
only serves to assemble the object to the arm. At joint limits 
and arm singularities, the possible motions of the object 
become very limited without a dexterous end effector (Fig. 
3). The presence of obstacles also places constraints on the 
set of possible arm configurations, effectively creating 
virtual joint limits. In-hand manipulation can then replace 
some of the lost ability due to these constraints (Fig. 4). 
Hand dexterity can greatly increase the workspace of the 
system distal to the “arm”, which is particularly useful at 
arm singularities or in the presence of obstacles. .  
At the end effector level, a dexterous hand primarily adds 
kinematic redundancy that might otherwise be accomplished 
by adding active joints to the manipulator arm. In scenarios 
where a power grasp is required to secure the manipulated 
object, the dexterity of the hand is greatly reduced, and even 
a dexterous hand’s function becomes comparable to that of a 
parallel-jaw gripper. In these cases, additional arm dexterity 
is more beneficial than hand dexterity.  
 However, for objects and tasks at scales where precision 
grasps are sufficient for force closure, additional hand 
dexterity can sometimes achieve the goal state entirely 
within the hand subsystem without any additional action 
from the arm. By actuating only the smaller finger 
mechanisms, a dexterous hand can enable increased 
precision and speed compared to movements from a larger 
arm. Indeed, in human manipulation, the arm (or wrist) is 
often braced on a surface to decouple the hand and the arm 
in precision tasks, such as writing with a pen. 
 
3)  “Manipulation with a Dexterous End-Effector is 
Sometimes More Appropriate for a Given Task” 
The 
concentration 
of 
kinematic 
redundancy 
and 
complexity in the end effector as opposed to other portions 
of the arm has benefits for certain tasks, particularly related 
to the scale of motion and precision required.  
Most precision tasks require only small degrees of motion, 
making it inefficient or inappropriate to utilize whole-arm 
movements. Manipulations with a dexterous hand can 
reduce the energy required to accomplish the task, due to the 
lower inertial loads that must be moved. Related to this 
point, the use of a dexterous end-effector for fine 
manipulation reduces the magnitude of the feedback gains 
required in the control system for good performance as 
opposed to a full arm, which in turn increases the safety of 
the 
system, 
increases 
mechanical 
adaptability 
and 
compliance (useful for passively accommodating small 
positioning and alignment errors), and decreases electrical 
power usage.  
When handling tools or objects that need to have certain 
features exposed (e.g. the “business end” of a tool or 
implement), a dexterous end-effector allows the object to be 
reoriented within the hand from the initial grasp, such as 
switching from a fingertip grasp to a power grasp. A simple 
gripper and manipulator arm would be forced to release the 
object and re-grasp it in a more appropriate configuration 
(Fig. 5), which may not be desirable in certain scenarios. A 
dexterous manipulator could allow for reorientation to occur 
while the object remains in a stable grasp within the hand, 
which may be necessary or advantageous.  
4


<!-- page 5 -->
 
 
Fig. 8. Finger-pivoting/tracking 
 
Fig. 9. Rolling (left) and Sliding (right) 
IV. WITHIN HAND MANIPULATION 
While there exist many dexterous tasks that require both 
hand and arm actuation, especially for tasks where force and 
torque requirements exceed the limitations of the hand alone 
(e.g. twisting a tight lid off a jar), the contribution of each 
can be decoupled into the arm manipulation (which is 
typically large-scale positioning of the hand in space 
combined with application of large forces) and the within-
hand manipulation component (if any). Previous work has 
described the local manipulation behaviors of the human 
hand (i.e. small time-scale) [2]. Here we describe the larger-
scale movement classifications of in-hand manipulation and 
without the constraint of anthropomorphism [5, 6, 8, 13, 14].   
A. Classes of Within Hand Manipulation 
 Regrasping: As mentioned previously, this type of 
manipulation may be the simplest form of dexterous 
manipulation, where the object is released and re-
grasped in order to change its position and orientation 
within the grasp. The geometry of the object and state 
of the environment must be able to accommodate a 
stable configuration of the object upon release. 
Regrasping can also occur between multiple hand 
workspaces or entirely within the hand workspace, 
independently of the environment, if there are enough 
free fingers to form an entirely new grasp on the object 
such that the original grasping fingers can then release 
the object. This is similar to the tripod gait in hexapod 
locomotion, where three legs provide stability for the 
robot at all times. Some may object to the inclusion of 
regrasping as a dexterous task, as it can be completed 
by a kinematically minimal parallel-jaw gripper 
system, but that may depend on the selected definition 
of the system, which in the case of regrasping requires 
either some environmental component or another 
manipulator. 
 In-Grasp Manipulation: This type of manipulation 
utilizes the kinematic redundancy of fingers to make 
small changes to the object’s orientation and position 
while maintaining fingertip contact with the object 
(Fig. 6). The fingers must maintain a stable grasp on 
the object throughout this task. While it is assumed that 
no sliding or slippage occurs at the fingertips, there 
may be local rolling [14], depending on the finger 
design and number of redundant degrees of freedom.  
 Finger Gaiting: This type of manipulation extends the 
kinematic limits of in-grasp manipulation in the 
absence of rolling and sliding by replacing grasping 
fingers with free fingers (Fig. 7). The grasping fingers 
are generally replaced in the grasp once they have 
reached joints limits. Finger-gaiting can be subdivided 
into finger substitution, where a free finger replaces a 
grasping finger at the edge of its configuration space, 
and finger rewind, where a free finger is used to 
maintain stability of the object while a grasping finger 
is freed to move to another position in its configuration 
space [16]. Its corresponding equivalent in locomotion 
is a wave gait, where leg-ground contacts alternate one 
or several at a time while maintaining stance 
equilibrium. 
Finger 
gaiting 
often 
includes 
a 
“regrasping” component.  
 Finger Pivoting/Tracking: This type of manipulation 
[17] establishes an axis of object rotation through two 
 
Fig. 6. In-grasp manipulation 
 
Fig. 7. Example finger placement during finger gaiting 
 
5


<!-- page 6 -->
 
point contacts while utilizing the remaining free 
fingers to guide the object’s rotation about this axis 
(Fig. 8). In human manipulation, it is commonly 
utilized to re-orient utensils held between the index 
finger and thumb.   
 Rolling: This type of manipulation is only realizable for 
objects/fingers of certain geometries but can also be 
performed by non-fingered end effectors [18,19]. This 
is generally regarded as a form of non-prehensile 
manipulation requiring non-holonomic control in task 
planning (Fig. 9).  
 Sliding: Whereas the other forms of within-hand 
manipulation assume no slippage, sliding manipulates 
objects through controlled slip [20] (Fig. 9). It is 
widely accepted that human manipulation utilizes 
considerable sliding, but the lack of tactile sensor 
arrays with the appropriate sensitivity has made it 
difficult to reproduce the same level of success in 
robotic dexterous manipulators. The more simplified 
task of push-grasping, which leverages slip to reduce 
the uncertainty in grasping problems, has achieved far 
more success in implementation [21]. 
B. Review of Dexterous Within Hand Manipulators 
Dexterous end effectors are typically fingered and 
anthropomorphic in nature, at least partially due to the fact 
that the majority of tasks we consider to be dexterous are 
performed by the human hand.  
The Utah/MIT Dextrous Hand [22] was one of the early 
attempts at reproducing the dexterity of the human hand 
through a tendon-based, fingered design. It had four 
anthropomorphic fingers with four degrees of freedom each, 
but required 32 total actuators to operate. While each joint 
was actuated by a pair of antagonist tendons to reproduce the 
compliant response of human joints, that setup also 
decreased the systems’ overall reliability and consistency in 
positioning. 
Similar work has also been done at the University of 
Bologna on the UB Hand [23], and successive iterations. 
The current version [24] utilizes compliant, elastic hinges in 
place of tendons to better emulate the coupled behavior of 
the human hand. The use of compliant materials in place of 
rigid links and joints has resulted in improvements for both 
adaptability in grasps and ease of fabrication. Other 
anthropomorphic hands include the Gifu hand [25], the DLR 
hand [26], the Robonaut hand [27], and the Karlsruhe 
humanoid hand [28].  
Though also multi-fingered, Salisbury’s Stanford-JPL 
hand [29] was not meant to be anthropomorphic in design. 
The three-fingered system utilizes nine degrees of freedom 
to fully constrain and manipulate an object. Grasp research 
with this device focused on fingertip prehension in grasp 
formulation. The Karlsruhe dexterous hand [14] is another 
non-anthropomorphic hand (with four fingers) that has been 
used to demonstrate in-hand regrasping motions and 
localized rolling at the fingertip.  
There are few non-fingered manipulators that do more 
than just affix the object to the arm. The most well-known 
may be the turntable-based manipulator analyzed by both 
Bicchi [18] and Nagata [30]. This end effector uses 
turntables attached to a parallel-jaw setup that can 
manipulate spherical objects through rolling.  
C. Research Issues in Dexterity 
In continuing dexterity research, researchers must make 
the key decision between pursuing a more complicated hand 
design and attempting to do more with a simpler hand 
mechanism. Most recently, Mason [33] argues that 
generality 
and 
mechanism 
complexity 
are 
directly 
correlated, such that the benefits of a truly general hand 
capable of all examples of in-hand manipulation from 
Section IV.A will not necessarily justify the required level of 
complexity in both mechanical design and control.  
Precise sensory feedback, a prerequisite of many 
approaches 
to 
dexterous 
control 
in 
multi-fingered 
manipulators, continues to be a major challenge in the 
implementation of dexterity. Due to the inconsistency of 
visual feedback, much of the focus for dexterous 
manipulators has been on tactile sensors. These largely use 
layers of piezoresistive films [34], optical arrays [35], and 
fluid-filled sacs [36] to detect slippage and force contact. 
High cost generally limits these sensors to the manipulator 
fingertips, and these sensitive manipulation systems still 
must deal with issues of sensor noise in unstructured 
environments.  
For the purposes of grasp acquisition, the use of compliant 
and adaptive fingers [31] and appropriate control strategies 
such as push-grasping [32] can circumvent strict sensor 
requirements by adapting to uncertainty rather than trying to 
eliminate it. Designing adaptive manipulators with flexible 
material creates “mechanically intelligent” mechanisms 
inherently suited for particular tasks [37].  
V. CONCLUSIONS 
Dexterity in general refers to the variety of tasks that the 
system can complete, and also how well it can perform those 
tasks, though the means by which that can be quantified is 
still open to interpretation. It is perhaps appropriate to 
classify the hand and arm as subsystems responsible for 
tasks of different scales, where the hand performs fixturing 
and fine manipulation while the arm handles gross 
positioning 
motions. 
Though 
a 
standard 
industrial 
manipulator with a 6-7 degree of freedom arm and simple 
grasper has proven to have a great deal of utility, we have 
detailed many scenarios where a dexterous end effector is 
crucial to compensate for functional shortcomings or in the 
presence of obstacles. Additionally, we have identified 
situations in which dexterous in-hand manipulation is more 
appropriate than arm-based manipulation, as it can reduce 
the required power and increase the safety of the system. As 
research in dexterous manipulation continues to advance, we 
look forward to further discussion and formalization of the 
topics presented here.   
6


<!-- page 7 -->
 
ACKNOWLEDGMENT 
 The authors would like to thank Lael Odhner and Robert 
D. Howe for their helpful discussions related to these topics. 
REFERENCES 
[1] J. Napier, “The prehensile movements of the human hand,” J. Bone 
Joint Surg., vol. 38B, no. 4, pp. 902-913, Nov. 1956. 
[2] I. Bullock, A.M. Dollar, “Classifying Human Manipulation Behavior,” 
in Proc. 2011 IEEE International Conf. on Rehabilitation Robotics, 
2011. 
[3] J. Hollerbach, Workshop on the Design and Control of Dexterous 
Hands, A.I. Memo 661, A.I. Laboratory, MIT, Cambridge, MA, 
1982. 
[4] P.K. Wright, J.W. Demmel, M.L. Nagurka,“The Dexterity of 
Manufacturing Hands,” in ASME Winter Annual Meeting, San 
Francisco, CA, December 10-15, 1989, pp. 157-163. 
[5] T.H. Speeter, “Primitive Based Control of the Utah/MIT Dextrous 
Hand,” in Proc. 1991 International Conf. Robotics and Automation, 
1991, pp. 866-877. 
[6] A. Bicchi, “Hands for dexterous manipulation and robust grasping: a 
difficult road toward simplicity,” IEEE Trans. Robotics and 
Automation, vol. 16, no. 6, 652-662, 2000. 
[7] A. Bicchi, A. Marigo, “Dexterous Grippers: Putting Nonholonomy to 
Work for Fine Manipulation,” The International Journal of Robotics 
Research, vol. 21, no. 5-6, 427-442, May 2002. 
[8] A. Okamura, N. Smaby, M.R. Cutkosky, “An overview of dexterous 
manipulation,” in Proc. 2000 International Conf. Robotics and 
Automation, 2000, pp. 255-262. 
[9] Z. Li, J.F. Canny, S.S. Sastry, “On motion planning for dexterous 
manipulation. I. The problem formulation," in Proc.  1989 
International Robotics and Automation. 1989, pp.775-780. 
[10] C.A. Klein, B.E. Blaho, “Dexterity Measures for the Design and 
Control 
of 
Kinematically 
Redundant 
Manipulators,” 
The 
International Journal of Robotics Research, vol. 6, no. 2, 72-83, 
June 1987.  
[11] R.H. Sturges, “A Quantification of Machine Dexterity Applied to an 
Assembly Task.” The International Journal of Robotics Research 
vol. 9, no. 3, 49-62, June 1990.  
[12] J.S. Pettinato & H.E. Stephanou, “Manipulability and stability of a 
tentacle based robot manipulator,” in Proc. 1989 International Conf. 
Robotics and Automation, 1989, pp. 458-463. 
[13] P. Tournassoud, T. Lozano-Perez, E. Mazer, “Regrasping,” in Proc. 
1987 International Conf. Robotics and Automation, 1987, pp. 1924-
1928.  
[14] D. Osswald, W. Heinz, “Mechanical System and Control System of a 
Dexterous Robot Hand” in Proc. IEEE-RAS International Conf. on 
Humanoid Robots, 2001. 
[15] M.T. Mason, J.K. Salisbury, Robot hands and the mechanics of 
manipulation, Cambridge: MIT Press, 1985. 
[16] L. Han, J.C. Trinkle, “Dextrous Manipulation by Rolling and Finger 
Gaiting,”in 
Proc. 
1998 
International 
Conf. 
Robotics 
and 
Automation, 1998, pp. 730-735. 
[17] D. Rus, “Dexterous rotations of polyhedral,” in Proc. 1992 IEEE 
International Conf. on Robotics and Automation, 1992, pp. 2758-
2763.  
[18] A. Bicchi, R. Sorrentino, “Dexterous manipulation through rolling,” in 
Proc. 1995 International Conf. Robotics and Automation, 1995, pp. 
452-457.  
[19] L. Han et al., "Dextrous manipulation with rolling contacts," in Proc. 
1997 International Conf. Robotics and Automation,  1997, pp.992-
997. 
[20] D.L. Brock, “Enhancing the dexterity of a robot hand using controlled 
slip,” in Proc. 1988 International Conf. Robotics and Automation, 
1988, pp. 249-251.  
[21] M.R. Dogar, S.S. Srinivasa, “Push-Grasping with Dexterous Hands : 
Mechanics and a Method,” in Proc. 2010 International Conf. 
Intelligent Robots and Systems, 2010, pp. 2123-2130. 
[22] S.C. Jacobsen et al., “The UTAH/M.I.T. Dextrous Hand: Work in 
Progress.” The International Journ. of Robotics Research, vol. 3, no. 
4, 21-50, 1987.  
[23] L. Bologni, S. Caselli, C. Melchiorri, “Design Issues for the U.B. 
Robotic hand,” in Proc. NATO Advanced Research Workshop on 
Robots with Redundancy, Salo, Italy June 27-July 1, 1988. 
[24] F. Lotti et al. “UBH 3: an Anthropomorphic Hand with Simplified 
Endo-Skeletal Structure and Soft Continuous Fingerpads,” in Proc. 
2004 International Conf. Robotics and Automation, 2004, pp. 4736-
4741. 
[25] T. Mouri et al., “Anthropomorphic Robot Hand : Gifu Hand III,” in 
Proc. International Conf. Control, Automation and Systems, 2002, 
pp. 1288-1293. 
[26] J. Butterfab et al., “DLR-Hand II : Next Generation of a Dextrous 
Robot Hand,” in Proc. 2001 International Conf. Robotics and 
Automation, 2001, pp. 109-114. 
[27] C.S. Lovchik, M.A. Diftler, “The Robonaut hand: a dexterous robot 
hand for space.” in Proc. 1999 International Conference on 
Robotics and Automation ,1999, pp. 907-912.  
[28] S. Schulz, C. Pylatiuk, G. Bretthauer, “A New Ultralight 
Anthropomorphic Hand,” in Proc. 2001 International Conf. 
Robotics and Automation, 2001, pp. 2437-2441. 
[29] J.K. Salisbury, J.J. Craig, “Articulated Hands: Force Control and 
Kinematic Issues.” The International Journal of Robotics Research 
vol. 1, no. 1, 4-17, 1982. 
[30] K. Nagata, “Manipulation by a parallel-jaw gripper having a turntable 
at each fingertip,” in Proc. 1994 International Conf. Robotics and 
Automation, 1994, pp. 1663-1670.  
[31] A. M. Dollar and R. D. Howe, “Towards Grasping in Unstructured 
Environments: 
Grasper 
Compliance 
and 
Configuration,” 
Optimization,Advanced Robotics, vol. 19, no. 5, pp 523-543, 2005. 
[32] M.T. Mason, “Mechanics and Planning of Manipulator Pushing 
Operations,” IJRR, vol. 5, no. 3, 53-71, 1986. 
[33] M.T. Mason et al., “Generality and Simple Hands,” Springer 
Transactions in Advanced Robotics, vol. 70, pp 345-361, 2011. 
[34] J. Jockush et al., “A Tactile Sensor System for a Three-fingered Robot 
Manipulator,” in Proc. 1997 International Conf. Robotics and 
Automation, 1997, pp. 3080-3086. 
[35] M. Ohka et al., “Sensing Characteristics of an Optical Three-axis 
Tactile Sensor Mounted on a Multi-fingered Robotic Hand,” in 
Proc. 2005 Intelligent Robots and Systems, 2005, pp. 493-498. 
[36] E. Torres-Jara, I. Vasilescu, R. Coral, “A Soft Touch: Compliant 
Tactile Sensors for Sensitive Manipulation,” in 2006 CSAIL 
Technical Reports.  
 [37] A. M. Dollar and R. D. Howe, “The Highly Adaptive SDM Hand: 
Design and Performance Evaluation,” International Journal of 
Robotics Research, Vol. 29, No. 5, pp 585-97, 2010. 
 
7
