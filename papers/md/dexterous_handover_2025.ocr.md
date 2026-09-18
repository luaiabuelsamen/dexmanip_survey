<!-- page 1 (ocr) -->
arXiv:2506.16822v1  [cs.RO]  20 Jun 2025
Learning Dexterous Object Handover
Daniel Frau-Alfaro1, Julio Casta˜no-Amoros1, Santiago Puente1, Pablo Gil1 and Roberto Calandra2
Abstract— Object handover is an important skill that we use
daily when interacting with other humans. To deploy robots
in collaborative setting, like houses, being able to receive and
handing over objects safely and efficiently becomes a crucial
skill. In this work, we demonstrate the use of Reinforcement
Learning (RL) for dexterous object handover between two
multi-finger hands. Key to this task is the use of a novel reward
function based on dual quaternions to minimize the rotation
distance, which outperforms other rotation representations such
as Euler and rotation matrices. The robustness of the trained
policy is experimentally evaluated by testing w.r.t. objects that
are not included in the training distribution, and perturbations
during the handover process. The results demonstrate that
the trained policy successfully perform this task, achieving a
total success rate of 94% in the best-case scenario after 100
experiments, thereby showing the robustness of our policy with
novel objects. In addition, the best-case performance of the
trained policy decreases by only 13.8% when the other robot
moves during the handover, proving that our policy is also
robust to this type of perturbation, which is common in real-
world object handovers. Code and videos can be found here.
I. INTRODUCTION
With the recent focus on humanoid robots, service robots,
and human-robot collaboration, several efforts have been
made to teach robots how to perform dexterous manipulation
tasks, such as collaborative assembly, package manipulation
in logistics, and household chores. However, there are still
many open questions about how to approach this type of
tasks using robots, which require a variety of skills, including
a high degree of dexterity, perception, coordination, collab-
oration, and understanding [1] [2]. In contrast, humans have
an innate talent for performing tasks that require these types
of skills. Therefore, it makes sense to bring humans into the
loop when tackling these complex problems.
In particular, this work addresses the task of object han-
dover which can be very interesting in the context of human-
robot collaboration for both industrial and social applica-
tions. According to [3], the object handover collaboration can
*This work was partially supported by the Interreg-VI Sudoe and Eu-
ropean Regional Development Fund through the REMAIN Project under
Grant S1/1.1/E0111, by the project “Genius Robot” (01IS24083) BMBF,
by the DFG as part of EXC 2050/1 – Project ID 390696704 CeTI of
Technische Universit¨at Dresden by BMBF, and by the DAAD in project
57616814 (SECAI School of Embedded and Composite AI) and by the
Spanish Government through the Grant PID2021-122685OB-I00 and by the
University of Alicante under Grant UAFPU21-26.
*This work was conducted during Julio’s research stay at LASR Lab.
1Daniel
Frau-Alfaro,
1Julio
Casta˜no-Amoros,
1Santiago
Puente
and
1Pablo Gil are with the AUROVA Lab, Department of Physics,
Systems Engineering, and Signal Theory, University of Alicante, 03690
Alicante,
Spain
daniel.frau@ua.es,
julio.ca@ua.es,
santiago.puente@ua.es, pablo.gil@ua.es
2Roberto Calandra is with LASR Lab, Technische Universitat Dresden,
Dresden, Germany rcalandra@lasr.org
st
st+n
rt
rt+n
at
at+n
Maneuver
Approach
Handover
Fig. 1.
Overview of the different phases of the object handover process.
Both robots must collaborate to successfully complete object handover,
which is more complicated when employing multi-finger robotic hands.
be classified into robot-robot collaboration, human-robot col-
laboration, and robot-human collaboration. The differences
between them are whether humans are involved in the task
or not, and which participant acts as the giver and which one
as the receiver. This type of collaboration typically comprises
different subtasks, from the maneuver to set the initial hand
pose to the object handover and its subsequent manipulation,
as illustrated in Fig. 1, that must be resolved in order to
complete the task.
In this work, we explore the object handover task based
on robot-robot collaboration, as an initial step for human-
robot and robot-human collaboration. We assume that the
robotic hand holding the object is already fixed in an arbitrary
handover pose. Consequently, our objective is to train a
single RL policy so that a robotic arm and hand can learn
how to approach, grasp, and transport the object from another
robotic system. The main contributions of this work are
twofold. First, in contrast of using 2-finger small grippers
as in [4], we use 4-finger articulated hands, which increases
the DoF and consequently the difficulty of applying learning-
based strategies. In addition, unlike other works such as
[5] [6], we discard the use of teleoperation systems to
teach robots how to perform the task. Second, [7] proposed
a dual quaternion-based reward function to avoid rotation
constraints in S0(3). The goal of this work is to expand that
reward function to the object handover task using 4-finger
robotic hands, and to compare it with other representations,
such as Euler or matrix rotation, that do require these
restrictions.
II. RELATED WORK
Traditionally, collaboration tasks such as object handover
have been addressed employing control theory algorithms,
sensor fusion techniques, probabilistic methods, etc., as in
[3], [8], and [9]. Although the results of such approaches are
promising, they are limited for several reasons. For instance,
sensor fusion techniques tend to accumulate errors when
calibrating different devices. More specifically, the use of
%


<!-- page 2 (ocr) -->
control theory algorithms require the design of the policy
for each subtask, while our goal is to learn it using RL.
In the literature of RL-based object handover, this task has
been addressed in different ways. For instance, [10] formu-
lated the object handover task by throwing and catching small
objects, while our approach is based on a direct handover
using longer objects due to the size of the hands. The authors
employed two 6-DoF robotic arms and two Allegro hands,
similarly as we do in our work. They proposed a multi-
agent approach and a three-phase training, while our policy
comprises a single agent and trains on a single-phase process,
thereby reducing the number of hyperparameters to tune.
Their trained policies obtained a throw and catch success rate
of 95% and 37% when testing with 11 known objects and
14 novel objects in simulation, respectively. These results
showed a large gap in robustness when evaluating with
objects out of the training distribution. Our policy is more
robust in this type of case, although we use fewer objects to
evaluate in our experiments.
Although throwing and catching can be considered a type
of object handover, it does not involve physical interaction
between the robots and the object at the same time, which
is what we are interested in exploring in this work. In
this context, repositioning objects using two robotic systems
requires transferring the object between them, resulting in a
direct handover [4]. To achieve this, a single-agent policy
was trained via actor-critic learning, which is similar to
our approach. In this case, the authors employed two 7-
DoF robotic arms equipped with two 2-finger grippers to
handover objects similar to ours. However, they simplified
the task by using grippers instead of multi-finger hands,
which require orientation optimization in SO(3), as we
propose in our work. They reported an average success rate
of 94% in the simulated environment, which is similar to the
results obtained in our experiments, taking into account the
complexity of using multi-finger hands with different objects
in our approach.
Humanoid robots equipped with multi-finger hands have
also been employed to approach this task using RL recently
[11]. Specifically, two 7-DoF robotic arms and two 5-finger
grippers were involved in the robotic setup. Initially, they
recorded demonstrations to capture the human pose of the
hands at the beginning of the episode, while we let our policy
learn how to maneuver to approach the object correctly,
which can sometimes produce more optimal results. As
visual input, they performed an ablation study to evaluate the
use of the 3D object position together with the depth image.
The results of this study reported that their policy was not
able to learn with the depth image alone, but with the 3D
object position, as we do in our work. Similar to our work,
they designed a contact-based reward function. However,
they generated several contact markers to guide the policy
to grasp the object, while we only define a single grasping
frame and let the policy learn how to grasp the object and
keep it stable. The main difference of our approach is the
use of dual quaternions to learn the orientation of the hands,
which is not considered in any of the aforementioned works.
TABLE I
BASIC OPERATIONS WITH DUAL QUATERNIONS. WE USED THESE
OPERATIONS TO CALCULATE THE REWARD FUNCTION IN SECTION IV-B.
Operation
Formulation
Primary part
P(ˆq1) = qp1
Dual Part
D(ˆq1) = qd1
Addition
ˆq1 + ˆq2 = qp1 +qp2 +ε(qd1 +qd2)
Multiplication
ˆq1 ⊗ˆq2 = qp1 ·qp2 +ε(qp1 ·qd2 +qd1 ·qp2)
Conjugate
ˆq∗
1 = q∗
p1 +εq∗
d1
Magnitude
||ˆq1|| = ˆq1 ⊗ˆq∗
1
Difference
ˆqdiff = ˆq∗
1 ⊗ˆq2
Identity Element
ˆI = I+ε0, I = (1+0i+0 j +0k) ∈H
III. MATHEMATICAL FOUNDATIONS
RL and Deep Reinforcement Learning (DRL) algorithms
allow to obtain policies for a vast range of tasks with
high dimensionality of actions and observations, like object
handover, which are difficult to deal with classical control
techniques. In this section, a brief introduction to the basics
of the RL paradigm is provided. Next, we explain the dual
quaternion algebra used in this work.
A. RL basics
The RL approach considers every problem as a Markov
Decision Process (MDP) [12] [13]. Following this modeling,
an agent placed in an environment captures information as
a state st. Then, it produces an action at based on a certain
policy at ∼π(·|st). This produces a change (or step) in the
environment, leading to st+1. In addition, the agent receives a
reward rt that indicates how good the action was according
to the task it is performing. With this, the final objective
of the agent is to generate a policy π that maximizes the
expected return over time, estimated using (1).
E[
T
∑
t=0
γtrt]
(1)
where γ ∈[0,1] is the discounting factor over time.
B. Dual quaternion algebra
For the sake of clarity, a brief introduction to dual
quaternion algebra is presented [14] [15]. In the upcoming
explanation, we assume some previous knowledge in the field
of simple quaternions q ∈H to represent rotations in SO(3).
Dual quaternions are an extension of the group of dual
numbers ˆq ∈H with ˆq = (a + εb), (a,b) ∈R and with ε
being the dual operator that fulfils that ε2 = 0, ε̸ = 0. The
elements of a dual quaternion are simple quaternions instead
of real numbers, therefore, considering ˆq as a dual quater-
nion, ˆq ∈H with ˆq = (a+εb), (a,b) ∈H. This formulation
allows performing the mathematical operations in Table I
given ˆq1 = qp1 +εqd1 and ˆq2 = qp2 +εqd2 and with ≪· ≫
being the dot operation of two vectors.


<!-- page 3 (ocr) -->
Hand Pose
Euclidean Translation (size: 3) + Euler (size: 3)
Hand Joint Avg.
size: 3
Object Pose
Euclidean Translation (size: 3) + Euler (size: 3)
Kinova GEN3
UR5e
PPO
Policy
Incremental Action
Cartesian (size: 6) + Hand Joint Avg. (size: 3)
Object Pose
Hand Pose
Hand Joint Avg.
Fig. 2.
Overview of the RL environment used in this work, comprising a single PPO agent. The observations consist of the Euclidean translations and
Euler rotations of the GEN3 robot and the object, as well as the average of each joint value for the different fingers, resulting in three global joint values
for the whole hand. The policy outputs increments in translation and Euler rotation as actions for the GEN3 end effector, and the three corresponding
increment joint values for the hand.
Dual quaternions are often used to represent poses in
SE(3) space, combining translations and rotations in a com-
pact and short formulation. Hence, given a rotation quater-
nion qr and a translation qt expressed as a pure quaternion,
that is, a quaternion with null real part, the dual quaternion
expressing that transformation is written following (2).
ˆq = qr +ε
1
2qr ·qt
,
(2)
where the resulting dual quaternion meets the unitary
condition as ||ˆq|| = 1. The primary part of a dual quaternion
represents the rotation of a pose, while the dual part contains
information about the translation along that orientation.
There are other formulations so as to represent poses in
3D space. Most of them utilize the Euclidean translation
to encode translations and vary the way in which we can
express orientations. An example of this issue are homoge-
neous transformation matrices SO(3) ⋊R3. This approach
employs 16 values to encode a pose in space, which is
less computationally efficient to operate with, compared
to the dual quaternion representation. In addition, we can
compute the difference or distance between poses separately
in rotation and translation, which requires normalization to
combine them. Other representations use translation vectors
along with Euler angles to represent positions and rotations
R3 ⋊R3, respectively. However, this alternative also suffers
from the separation of distances and other problems, e.g.
gimbal lock or singularities when interpolating.
Summarizing, the dual quaternion allows for a unified
representation of poses; both translations and rotations are
expressed under the same formulation, and they do not need
further processing or constraints to compute distances.
IV. HANDOVER SYSTEM AND REWARD FUNCTION
DESIGN
We now introduce the task modeling and the design of our
reward function. We define the states and actions in the RL
framework, as well as the division of the handover task into
movement primitives that enable the formulation of a reward
function by parts.
A. Object Handover Setup
In terms of modeling of the environment, we use an UR5e
(6 DoF) and GEN3 (7 DoF), both equipped with Allegro
Hands and touch sensors to perform the manipulation. At the
start of each episode, we initialize the UR5e to an arbitrary
pose chosen randomly. The UR5e robot holds the object
without moving during the whole episode as shown in Fig. 2.
This way, it mimics a human giver which should not be
trained. Then, the GEN3 has to learn to reach the object
and grasp it from the same starting pose in each episode.
The policy takes as observations the Cartesian poses of the
GEN3 and the object along with its hand joint values. In
terms of actions, we add increments to the current pose of
the GEN3 end effector and to the joint values of the hand.
B. Task Modeling
As for the task modeling and the reward function, it is
worth mentioning that we divide the object handover task
into different movement primitives or phases, as shown in
Fig. 1. In each stage, we change a simple initial reward
function defined in (3) using different modifiers. These
provide the reward function
rBASEt = ηt e−dt,
(3)
—r
4
4
Prag
\ &
/
/
-
-
’
-
i
’
Pid
/
.
1
co
O0= OO
1
\
JS
QFOIOEORD
\
So
OO OF OO
$e
Le
QROKOE O70
i
=r
lee te te}
-


<!-- page 4 (ocr) -->
Fig. 3.
Example of different poses of the GEN3 hand evaluated with
respect to the relative pose of the object. The different colors of the GEN3
hand indicate how adequate is the approach to grasp the object correctly.
Red: oriented with the back of the hand toward the object, Orange: closer
to the UR5e hand than to the object frame, Green: palm facing the object
correctly and closer to the object frame.
for each phase of the task, where rBASEt is a basic reward for
approaching the object, dt is the distance between the pose
of the hand and the object at step t and ηt is the weight of
the reward at step t which will be defined in (6).
1) Maneuver phase: The reward in (3) incentivizes the
agent to approach the object along a straight trajectory,
although it can be troublesome because the robots may
collide or the GEN3 hand might be oriented with its back
facing the object, as shown in Fig. 3. For this reason, we
restrict the reward to take the GEN3’s end effector closer
to the object than to the UR5e. Moreover, we propose a
double frame system for the agent to maneuver into a suitable
position for manipulation, with the GEN3 palm toward the
target. If both conditions are satisfied, the agent is in a
correct zone for approaching. First, we calculate the distance
between the palm of each robot dROBOTSt. Then, we define a
frame for the back of the GEN3 hand, computing the distance
between it and the object dBACKt. In this way, we define a
condition for the approach phase in (4), which we will use
in (5).
mMANt = (dROBOTSt > dt)∧(dBACKt > dt),
(4)
where mMANt ∈{0,1} is a modifier for (3) which we will
use in the following equations.
2) Approach phase: Once the GEN3 palm is located in a
suitable zone for approaching the object, the action taken at
t must bring the agent closer than it was at step t −1. Hence,
in (5) we extend the maneuver modifier mMANt to restrict the
distance at t and so to be lower than the one in the previous
step.
mt = 2[(dt < dt−1)∧mMANt]−1,
(5)
where (dt < dt−1) ∈{0,1} and mt ∈{−1,1}.
3) Handover phase: For the handover phase, we place
tactile sensors on the phalanges of the fingers and the palm
of the GEN3 hand, as shown in Fig. 4. In this way, we can
detect the contacts between each finger and other elements of
Contact Sensors
Fig. 4.
Placement of the contact sensors on the Allegro hand. Each green
area represents a boolean contact sensor. It is important to note that contact
sensing beyond the fingertips is necessary to successfully complete the
object handover task as the object is mainly grasped with the palm and
the proximal phalanges.
the simulation. We define the contacts as a vector of Boolean
values⃗c and we weight them using⃗wc according to their
relevance in the task; the lower phalanges are of greater
importance than the tips. In this work, it is worth mentioning
that we only consider the contacts between the GEN3 hand
and the object. In (6) we modify the original weight η0 = 1
according to the contacts. Therefore, the more touches, the
lower that value will be.
ηt =
η0
∑i
0⃗ci +1 .
(6)
In addition, we add the weighed sum of contacts⃗c·⃗wc to
the reward rBASEt. Thus, when the agent touches the object,
the reward encourages it to close the hand rather than to
continue advancing towards the target.
4) Manipulation phase: In the previous phases, the object
is not grasped yet and the UR5e hand remains closed. This
stage is changed when the thumb and another finger of the
GEN3 hand touch the object. At this point, we consider the
object susceptible to be grasped, so the UR5e hand opens.
The reward also changes to take into account the distance
between the object and the starting pose of the GEN3 dTGT
following (7). Hence, the objective of this phase is to take
the object to the starting pose of the GEN3.
rMANIPt = α e−dTGTt ,
(7)
where α = 12 is the weight for the manipulation phase.
Moreover, when the agent changes to this phase or reaches
the target, it receives a bonus.
The final reward function remain as (8), involving all
phases and modifiers.
rt =
mt rBASEt +⃗c·⃗wc
, if not (1G)
rMANIPt +⃗c·⃗wc
, otherwise
(8)
where 1G ∈{0,1} indicates whether the agent has already
grasped the object or not.
C. Distance calculation methods
We need to calculate the distances between poses in the
environment to compute the rewards. When dealing with
hx
W
= 4
:


<!-- page 5 (ocr) -->
poses, it is important to define precise metrics that reflect
not only translational distances but also orientation ones.
For this reason, we use and compare several representations
according to their formulation: dual quaternion, translation
along with Euler angles, and homogeneous transformation
matrices.
1) Dual Quaternions: Given two dual quaternions ˆq1
and ˆq2, we compute the difference transformation between
them, noted as ˆqdiff, using the corresponding formula in
Table I. This difference ˆqdiff is the identity element ˆI when
they represent the same pose. Then, ˆqdiff −ˆI ≈01×8 if both
transformations are the same. In this regard, we calculate
the distance between frames using dual quaternions using (9)
as presented in [16]. In this work, we propose this reward
function to perform the object handover task.
dDQ = ||ˆqdiff −ˆI||2,
(9)
where ||·||2 is the second norm of all elements of ˆqdiff −ˆI.
2) Euler Angles: Considering two sets of Euler angles⃗
e1 and⃗e2 in the XYZ convention with their corresponding
Euclidean translations⃗t1 and⃗t2, we calculate the distance
using this representation applying (10), extended from [17].
dEULER = ψ||⃗t1 −⃗t2||2 + µ||⃗e1 −⃗e2||,
(10)
where ψ = 2.1 and µ = 0.32 are scaling factors, so the
magnitude of the distance in translation and rotation is
similar due to differences in units.
3) Homogeneous Transformation Matrices: The poses are
represented in homogeneous transformation matrices as T 1
and T 2 being T = [R3×3⃗
t;
01×3
1], with R3×3 ∈SO(3)
as the rotation matrix and⃗t ∈R3 as the Euclidean translation
vector. Consequently, we obtain the distance by separating
the translation and rotation parts from the elements as shown
in (10). Therefore, we compute the orientation component
using (11), which corresponds to the relative angle between
the two rotation matrices.
θdiff = acos(
trace(RT
13×3 ·R23×3)−1
2
),
(11)
As a result, the final distance consists of the addition of
the rotation and translation components, as shown in (12).
dMAT = ψ||⃗t1 −⃗t2||2 +β θdiff,
(12)
where ψ = 2.1 and β = 0.32 are scaling factors to nor-
malize the distances so the magnitudes are similar.
V. EXPERIMENTS
We now present several experiments to evaluate the per-
formance of the agents produced by all the proposed reward
functions, as well as to test the robustness of the system
to novel objects. Specifically, we investigate the following
questions:
• Can we use RL to train an object handover policy using
two robotic arms equipped with multi-finger hands?
Fig. 5.
Average reward for all the agents trained for the object handover
task using different reward functions: DQ (blue), EULER (red), MATRIX
(green). The DQ agent shows the higher reward values, followed by the
EULER and MATRIX agents.
• How accurate and robust is the trained policy to seen
and novel objects in simulation?
• Are dual quaternions more adequate to compute reward
distances in SE(3) than Euler or rotation matrices?
• Is the trained policy robust enough to handle motion
perturbations during the object handover?
A. Simulation
We performed the entire training process along with exper-
iments on the IsaacLab simulator [18] using the Stable Base-
lines 3 (SB3) framework [19]. In addition, we used Proximal
Policy Optimization (PPO) [20] with three different seeds,
using 1024 environments on a single NVIDIA A40 GPU. For
each episode, we randomly reset the object position inside a
cube of ±0.15 m of side, as well as the orientation with a
variation of ±0.3 rad in roll and yaw, and ±0.6 rad in pitch.
B. Learning to handover an object
We chose an elongated quadrangular prism as the original
training object of (0.035 × 0.035 × 0.45) m, as shown in
Fig. 2. The single object training aims to reduce computa-
tional resources and to assess how the policy performs under
unseen objects in this setup. The training results in terms of
the average reward are shown in Fig. 5.
The MATRIX agent was unable to learn the task correctly,
collapsing with a constant reward near zero. A possible
reason for this issue may be the angle representation of the
angle-vector to compute rotational distances. During training,
there might be cases in which the observations were similar
but the θdiff for each observation was not. In these cases,
the rotation vector was different as the angle remained the
same. This can generate ambiguity when the policy obtained
the actions. Thus, we did not consider this agent for the next
experiments.
In contrast, the EULER agent learned faster to perform
the task successfully compared to the DQ agent, but the
reward became constant while the DQ agent continued to
learn. Specifically, the EULER agent exploited the reward
bonuses for grasping the object, thereby trying to reach those
stages of the task quickly to increase the reward. However,
— oo
—
EULER
2500{ —
MATRIX
T2000
sH
3
< 1500
o
3
c
g
1000
<
500
o
0
1
2
3
a
5
6
Time Step
1le8


<!-- page 6 (ocr) -->
(a) Success.
(b) Indetermination.
(c) Failure.
Fig. 6. Graphical description of the different cases contemplated during the
experiments to evaluate the object handover. The success case is a correct
handover without collision or falling. During the indetermination case, the
object is clipped through the UR5e hand. The failure case happens when
the object falls during handover.
this behavior led to an incorrect learning of the task during
simulation, as explained in the following Section V-C.
The DQ agent achieved the highest reward during the
training process without stabilizing, indicating that the agent
would collect an even higher reward if the training continued.
The best results obtained by the DQ agent may be due to
the ability of the proposed reward function to calculate the
rotation differences or distances more accurately.
Finally, we can answer the first question by saying that
RL can be used to learn the dexterous object handover
task. However, we observed that the results are highly
dependent on the representation used to compute the rotation
distances in the reward function, with Euler angles and dual
quaternions being able to solve the task.
C. Success rate with seen and novel objects
We used the following metrics to measure the success rate
during the experimentation (see Fig. 6).
• Success (Succ.): the robot grasped and manipulated the
object correctly.
• Indetermination (Ind.): indicates that, although the
robot manipulated the object correctly, there are bugs
during the episode because of failures of the simulator
to resolve collisions. Therefore, in a real environment,
we would not consider the grasp an absolute success.
• Total Success (Total Succ.): the combination of inde-
termination and success cases.
• Fail: indicates object falling during the episode.
We selected the best agents for each case to evaluate the
trained policies using the same object as during training.
The results in Table II show the performance for a total of
100 episodes in each case. The DQ agent achieved a total
success rate of 91%, while the EULER agent obtained 83%.
These results are an improvement of nearly 10% from the DQ
agent with respect to the EULER agent, although both have
a considerable number of indeterminate cases. During tests,
inconsistencies in the simulation may be causing movements
that made the object clip through the UR5e hand, snatching
the object out of its hand instead of grasping and taking it
with subtlety. Furthermore, the EULER agent collided with
the UR5e robot frequently, causing imprecisions during the
episode that led to cases of indetermination.
The objective of the following experiments is to test
the robustness of the agents to different types of unseen
TABLE II
SUCCESS RATE OF THE AGENTS EXPRESSED AS A PERCENTAGE (%)
WHEN EVALUATING WITH THE PRISM USED DURING TRAINING. THE DQ
AGENT ACHIEVED THE HIGHEST TOTAL SUCCESS VALUE COMPARED TO
THE EULER AGENT. THE BEST RESULTS ARE IN BOLD.
Agent
Suc. (%)
Ind. (%)
Total
Succ. (%)
Fail (%)
DQ
59
32
91
9
EULER
17
66
83
17
object morphologies. The new objects are a short prism of
dimension (0.035 × 0.035 × 0.35) m, a cylinder of radius
0.019 m and length of 0.45 m, and a short cylinder with
the same radius and a length of 0.35 m. In Table III the
success rates for each agent with each object are shown.
When testing with the short prism, the DQ and EULER
agents obtained a total success rate of 94% and 92%,
respectively, which are higher rates with respect to the
previous experiment. The smaller size of the object may be
causing a more precise and stable grasp because the robot
is approaching better the grasp frame. Although they have
similar total success rates, the EULER agent obtained many
more cases of indetermination owing to the same reasons as
when testing with the original prism. Regarding the results
with respect to the cylinder objects in Table III, the circular
shape of its surface can cause the orientation of the object
to slightly vary inside the UR5e hand. This rotates the target
frame to unseen poses, leading to a lower success rate for all
agents with 87% and 84% for the DQ and EULER. When
testing with the shorter version of the cylinder, a success
rate of 90% and 86% is obtained for the DQ and EULER
agent, respectively. It is relevant to consider that both agents
obtained around 20% less indetermination cases with the
shorter version of the cylinder.
Therefore, to respond to the second question, we can
confirm that the trained policy is accurate when evaluating
with objects from the training distribution and is also robust
to objects from another distribution. Specifically, the best
results are achieved when manipulating short rectangular
objects.
D. Distance minimization with dual quaternions
The objective of these experiments is to test how precise
the trajectory followed by the agent is from the starting
point to the target frame of the object. We conducted a
total of 10 successful experiments for each agent with the
different objects proposed. During those, we collected how
the distance to the object frame is minimized. In Fig. 7,
all three minimization cases are shown for both agents,
confirming the results in Tables II and III.
For the DQ agent, we calculated the mean distances fol-
lowing (9) in each step until the target pose is reached. Given
two frames in space, we obtained the translation distance by
applying ||⃗t1 −⃗t2||2, which represents the Euclidean distance
between two poses. On the other hand, we calculated the
rotational distance using ||P(ˆqdiff −ˆI)||2, which represents
the rotation term of the dual quaternion difference of bothAL


<!-- page 7 (ocr) -->
TABLE III
SUCCESS RATE OF THE AGENTS EXPRESSED AS A PERCENTAGE (%) WHEN EVALUATING WITH THE OBJECTS OUT OF THE TRAINING DISTRIBUTION.
NOTE THAT THE DQ AGENT ACHIEVED THE HIGHER TOTAL SUCESS VALUE COMPARED TO THE EULER AGENT. THE BEST RESULTS ARE IN BOLD.
Short
Prism
Cylinder
Short
Cylinder
Agent
Succ. (%)
Ind. (%)
Total
Succ. (%)
Fail (%)
Succ. (%)
Ind. (%)
Total
Succ. (%)
Fail (%)
Succ. (%)
Ind. (%)
Total
Succ. (%)
Fail (%)
DQ
69
25
94
6
41
46
87
13
55
35
90
10
EULER
32
60
92
8
8
76
84
16
25
61
86
14
(a) Global distance in Dual Quaternions for the
DQ agent.
(b) Euclidean Translation for the DQ agent.
(c) Rotation Distance in Dual Quaternions for the
DQ agent.
(d) Global distance in Translation + Euler for the
EULER agent.
(e) Euclidean Translation for the EULER agent.
(f) Rotation Distance for the EULER agent.
Fig. 7.
Distance minimization of the agents for all selected objects. The DQ agent showed a greater minimization of the rotation distance than the EULER
agent, which maximized it in most cases.
poses. Alternatively, we computed the global distance for the
EULER agent using (10), while we extracted the translational
and rotational distances from the respective terms of the
addition in that equation.
Both policies minimized the global distance from the
target (Fig. 7a and 7d). However, the DQ one made it
smoother than the EULER. Even though both agents were
able to minimize the translational distance (Fig. 7b and 7e),
the EULER one failed to orient the end effector to the
target rotation as shown in Fig. 7f. The DQ agent minimized
the rotational poses from the starting pose around 43% on
average. Far from reducing it, the EULER one increased it.
This fact may be one of the reasons why the latter obtains
more indetermination cases during the tests.
Answering the third question, we state that dual quater-
nions are more adequate to calculate the rewards on SE(3)
for approach trajectories. The distance minimized by the
agents trained with this representation is lower and smoother
than the obtained using the EULER representation.
E. Success rate under perturbations
When dealing with object handover in the real world, it is
common to have perturbations on the object pose from the
giver agent. For this reason, we conducted some experiments
where the handing robot (UR5e) is moving during the object
handover. The objective of these is to test the robustness
of the policy to unseen states where there is movement of
the target. In these experiments, the UR5e is moving in
a random direction within the limits where the agent was
trained. The velocity is set to be 40% lower than GEN3
so it can reach it. Specifically, at 0.03 m/s for the linear
velocity and 0.16 rad/s for the angular velocity. The results
are shown in Table IV. All the total success rates decreased
around 13.68% on average due to movement during the task
in our setup. The best results are still achieved by the DQ
agent when manipulating the original or short prism with
81% success compared to a 78% from the EULER. The DQ
agent performed better with all objects except the cylinder,
where the EULER obtained 77% compared to a 71% of
total success from the DQ. The movement of the UR5e
caused the agent to lose precision in the task, although it
still tried to perform the handover even taking advantage of
the simulation problems.
As a result and answering the fourth question, our policies
are robust to movement of the object during the handover. In
particular, the DQ agent obtained a higher success rate with
almost all proposed objects.
0.6
—— DQw. Cylinder
—— DQw. Original Prism
£1.00
=
~—— DQ w. Short Prism
=
=03
20.4
= DQ w. Short Cylinder
F075
L
©
i
3
140.50
=02
0.2
0.25
0
50
100
150
200
250
0
50
100
150
200
250
0
50
100
150
200
250
Time Step
Time Step
Time Step
—— EULERw. Cylinder
1.25
=038
—— EULERw. Original Prism
€
°
~— EULER
w. Short Prism
=
=
e! 5
—— EULER
w. Short Cylinder
«1.00
208
3
ie
&
©
1 0.75
10.4
0
=
&
—0.50
=0.2
0
50
100
150
200
250
0
50
100
150
200
250
0
50
100
150
200
250
Time Step
Time Step
Time Step


<!-- page 8 (ocr) -->
TABLE IV
SUCCESS RATE OF THE AGENTS EXPRESSED AS A PERCENTAGE (%) WHEN EVALUATING THE TRAINED POLICIES UNDER PERTURBATIONS. THE DQ
AGENT SHOWED HIGHER TOTAL SUCCESS VALUES FOR 3 OUT OF THE 4 OBJECTS COMPARED TO THE EULER ONE. THE BEST RESULTS ARE IN BOLD.
Prism
Short
Prism
Cylinder
Short
Cylinder
Agent
Succ. (%) Ind. (%)
Total
Succ. (%) Fail (%) Succ. (%) Ind. (%)
Total
Succ. (%) Fail (%) Succ. (%) Ind. (%)
Total
Succ. (%) Fail (%) Succ. (%) Ind. (%)
Total
Succ. (%) Fail (%)
DQ
46
35
81
19
55
26
81
19
37
34
71
29
12
65
77
23
EULER
11
67
78
22
21
51
72
28
12
65
77
23
13
59
72
28
VI. CONCLUSIONS
In this work, we evaluate in simulation an RL policy
to perform dexterous object handover with a multi-finger
hand. We trained the policy by using the PPO algorithm,
a single quadrangular prism as the handover object, and a
variety of random poses to reset the object differently at the
beginning of each episode. Experimental results demonstrate
that the policy trained with the quadrangular prism object is
robust to other objects with similar geometric shapes and
also with different sizes. Furthermore, it is shown that the
dual quaternion representation can minimize the orientation
of the hand with respect to the target orientation of the
object, while other representations failed. Finally, the trained
policy was evaluated under perturbations during the object
handover, showing only minimal decrease in performance
after the same number of experiments.
While this work is a promising first step towards dexterous
object handover, it is limited by several factors: First, a
single object is employed for the training process, thereby
diminishing the generalization capabilities of the policy.
Second, the proposed policy does not incorporate any kind of
visual perception; it is only extracting the object pose from
the simulator. This is very important to transfer the trained
policy from simulation to the real-world setup. Finally,
imperfections in the physics engine limit the training of the
policy by enabling undesired grasping behaviors that may
not occur in the real-world setup. Future work will look into
training not only the receiving robot, but also the handing
robot within the RL framework used, as well as looking into
the generalization of the policy to a wider set of objects.
Moreover, it is planned to transfer the policy to real-
world scenarios. In this way, it could be assessed how
the policy behaves under noisy observations provided by
sensors in real environments. By doing so, it will remove
the indetermination cases present during the simulation and
test the trained policies with humans as givers.
REFERENCES
[1] V. Ortenzi, A. Cosgun, T. Pardi, W. P. Chan, E. Croft, and
D. Kuli´c, “Object handovers: A review for robotics,” IEEE Trans-
actions on Robotics, vol. 37, no. 6, pp. 1855–1873, 2021. doi:
10.1109/TRO.2021.3075365
[2] D. Haonan, Y. Yifan, L. Daheng, and W. Peng, “Human–robot
object handover: Recent progress and future direction,” Biomimetic
Intelligence and Robotics, vol. 4, no. 1, p. 100145, 2024. doi:
10.1016/j.birob.2024.100145
[3] M. Costanzo, G. D. Maria, and C. Natale, “Handover control for
human-robot and robot-robot collaboration,” Frontiers in Robotics and
AI, vol. 8, 2021. doi: 10.3389/frobt.2021.672995
[4] Y. Li, C. Pan, H. Xu, X. Wang, and Y. Wu, “Efficient bimanual han-
dover and rearrangement via symmetry-aware actor-critic learning,” in
IEEE International Conference on Robotics and Automation (ICRA),
2023. doi: 10.1109/ICRA48891.2023.10160739
[5] B. Huang, Y. Wang, X. Yang, Y. Luo, and Y. Li, “3d-vitac: Learning
fine-grained manipulation with visuo-tactile sensing,” in 8th Annual
Conference on Robot Learning, 2024. doi: 10.48550/arXiv.2410.24091
[6] Z. Wang, J. Chen, Z. Chen, P. Xie, R. Chen, and L. Yi, “Genh2r: Learn-
ing generalizable human-to-robot handover via scalable simulation,
demonstration, and imitation,” in IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), 2024, pp. 16 362–16 372. doi:
10.1109/CVPR52733.2024.01548
[7] D. Frau-Alfaro, S. T. Puente, I. De Loyola P´aez-Ubieta, and
E. Velasco-S´anchez, “Robotic approach trajectory using reinforcement
learning with dual quaternions,” in 7th Iberian Robotics Conference
(ROBOT), 2024. doi: 10.1109/ROBOT61475.2024.10796878
[8] W. He, J. Li, Z. Yan, and F. Chen, “Bidirectional human–robot
bimanual handover of big planar object with vertical posture,” IEEE
Transactions on Automation Science and Engineering, pp. 1180–1191,
2022. doi: 10.1109/TASE.2020.3043480
[9] S. E. Ovur and Y. Demiris, “Naturalistic robot-to-human bimanual
handover in complex environments through multi-sensor fusion,” IEEE
Transactions on Automation Science and Engineering, pp. 3730–3741,
2024. doi: 10.1109/TASE.2023.3284668
[10] B. Huang, Y. Chen, T. Wang, Y. Qin, Y. Yang, N. Atanasov, and
X. Wang, “Dynamic handover: Throw and catch with bimanual
hands,” in 7th Annual Conference on Robot Learning, 2023. doi:
10.48550/arXiv.2309.05655
[11] T. Lin, K. Sachdev, L. Fan, J. Malik, and Y. Zhu, “Sim-to-
real reinforcement learning for vision-based dexterous manipula-
tion on humanoids,” arXiv preprint arXiv:2502.20396, 2025. doi:
10.48550/arXiv.2502.20396
[12] Y. Li, “Deep reinforcement learning: An overview,” arXiv preprint
arXiv:1701.07274, 2017. doi: 10.48550/arXiv.2412.05265
[13] M. A. Wiering and M. Van Otterlo, “Reinforcement learning,” Adap-
tation, learning, and optimization, vol. 12, no. 3, p. 729, 2012.
[14] Y.-B. Jia, “Dual quaternions,” Iowa State University: Ames, IA,
USA, 2013. [Online]. Available: https://faculty.sites.iastate.edu/jia/
files/inline-files/dual-quaternion.pdf
[15] F. Thomas, “Approaching dual quaternions from matrix algebra,” IEEE
Transactions on Robotics, 2014. doi: 10.1109/TRO.2014.2341312
[16] E. P. Velasco-S´anchez, L. F. Recalde, G. Li, F. A. Candelas-Herias,
S. T. Puente-Mendez, and F. Torres-Medina, “Dualquat-loam: Lidar
odometry and mapping parameterized on dual quaternions,” Robotics
and Autonomous Systems, 2025. doi: 10.1016/j.robot.2025.105009
[17] A. Iriondo, E. Lazkano, A. Ansuategi, A. Rivera, I. Lluvia, and
C. Tub´ıo, “Learning positioning policies for mobile manipulation
operations with deep reinforcement learning,” International journal
of machine learning and cybernetics, 2023. doi: 10.1007/s13042-023-
01815-8
[18] M. Mittal, C. Yu, Q. Yu, J. Liu, N. Rudin, D. Hoeller, J. L. Yuan,
R. Singh, Y. Guo, H. Mazhar, A. Mandlekar, B. Babich, G. State,
M. Hutter, and A. Garg, “Orbit: A unified simulation framework for
interactive robot learning environments,” IEEE Robotics and Automa-
tion Letters, 2023. doi: 10.1109/LRA.2023.3270034
[19] A. Raffin, A. Hill, A. Gleave, A. Kanervisto, M. Ernestus, and
N. Dormann, “Stable-baselines3: Reliable reinforcement learning
implementations,” Journal of Machine Learning Research. [Online].
Available: http://jmlr.org/papers/v22/20-1364.html
[20] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov,
“Proximal
policy
optimization
algorithms,”
arXiv
preprint
arXiv:1707.06347, 2017. doi: 10.48550/arXiv.1707.06347
=== ==
