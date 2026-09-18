<!-- page 1 (ocr) -->
PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction
Yinhuai Wang1,2§
Jing Lin3
Ailing Zeng2†
Zhengyi Luo4
Jian Zhang1†
Lei Zhang2
1Peking University
2International Digital Economy Academy
3Tsinghua University
4Carnegie Mellon University
Figure 1. Our method controls physically simulated humanoids to perform various dynamic interaction skills. Our method can imitate
human-object interaction across dynamic scenarios without task-specific rewards. Top-to-bottom: Fingertip spin basketball (left), Grasp
(right); Pick up and dribble; Walk while dribbling. Project page and video demonstrations: https://wyhuai.github.io/physhoi-page/
Abstract
Humans interact with objects all the time. Enabling a
humanoid to learn human-object interaction (HOI) is a key
step for future smart animation and intelligent robotics sys-
tems. However, recent progress in physics-based HOI re-
quires carefully designed task-specific rewards, making the
system unscalable and labor-intensive. This work focuses
on dynamic HOI imitation: teaching humanoid dynamic
interaction skills through imitating kinematic HOI demon-
strations. It is quite challenging because of the complexity
of the interaction between body parts and objects and the
lack of dynamic HOI data. To handle the above issues, we
present PhysHOI, the first physics-based whole-body HOI
imitation approach without task-specific reward designs.
Except for the kinematic HOI representations of humans
and objects, we introduce the contact graph to model the
contact relations between body parts and objects explicitly.
A contact graph reward is also designed, which proved to
be critical for precise HOI imitation. Based on the key de-
signs, PhysHOI can imitate diverse HOI tasks simply yet ef-
fectively without prior knowledge. To make up for the lack
of dynamic HOI scenarios in this area, we introduce the
BallPlay dataset that contains eight whole-body basketball
skills. We validate PhysHOI on diverse HOI tasks, includ-
ing whole-body grasping and basketball skills.
1. Introduction
Creating realistic and agile interactions between objects and
humanoids is a long-standing and challenging problem in
computer animation, robotics, and human-computer inter-
action (HCI) [22, 57, 64, 86]. Recently, due to advances in
deep reinforcement learning and physics simulation, meth-
ods that learn humanoid control from demonstrations (e.g.,
kinematic motions from motion capture data) have been
widely used in animation [53, 69–72, 102, 116] and robotics
[2, 5, 17, 81]. However, most existing physics-based im-
itation learning methods focus on mimicking isolated hu-
man motion without considering human-object interactions,
especially for whole-body (i.e., full-body with hands) mo-
tions, as involving articulated fingers and complex object
dynamics can be exceedingly challenging.
There exist HOI tasks conditioned on goals, in which the
§Work done during an internship at IDEA; † Corresponding authors.
arXiv:2312.04393v1  [cs.CV]  7 Dec 2023
-
PS
-
-
a
a
FY
p
-
—
pro.
-
-—
-
-
-
-
£5
9
»
9
pr
b.
$\
Ae
-
“a
4
a>
4
an
\
v
lo
.
4
)
>
|
FA)
>
IY
IY
J!
EN
J
4
4
y)
4
7
/
\
Lf
2
PN
-
-
\
oc
v
L
3
o'{
3
2
3
- 5
3
5
-
.
$
.
-
®
0
S
a
3
NN
Bi)
!
\
\
¥
X
y
-
-
\
\
®
\
-
\
\
3
3
ol
Lo-
J
3
<y
<y
n
J
=


<!-- page 2 (ocr) -->
humanoid is tasked with manipulating objects to reach cer-
tain kinematic states [1, 6, 31, 116]. Although they perform
well on specific tasks, e.g., playing tennis [116], these meth-
ods may find the learning paradigm difficult to generalize to
new types of interaction and skills, considering each needs
specially designed task rewards. For example, basketball
games consist of multiple basic skills: dribbling, shooting,
passing, fingertip spinning, etc. It is extremely laborious to
design task-specific rewards for all skills.
To solve diverse HOI tasks within a unified solution,
we resort to the HOI imitation, i.e., recreating diverse
HOI skills in simulation from kinematic demonstrations. It
should be noted that the difference between HOI imitation
and previous imitation methods [69, 71] is that they imitate
isolated human motion, while our aim is to recreate motion
for both the human and the object. During simulation, the
object is passive and can only be controlled indirectly by
the humanoid, making this task extremely challenging.
Correspondingly, we introduce the first physics-based
whole-body HOI imitation framework, called PhysHOI,
which makes HOI imitation feasible in diverse scenarios.
Given a kinematic HOI demonstration sequence, PhysHOI
can imitate the HOI skill without task-specific knowledge
and reward designs. Considering the importance of contact
in describing HOI semantics, we introduce a novel general-
purpose Contact Graph (CG), where nodes are whole-body
humanoid body segments and objects, and each edge de-
notes the binary contact information between two nodes,
to enhance the commonly-used kinematic HOI representa-
tion (e.g., the human motion, object motion, and interaction
graph [122]). Based on the contact-aware HOI representa-
tion, we present a task-agnostic HOI imitation reward that
multiplies the kinematic rewards with the proposed contact
graph reward (CGR), which effectively eliminates local op-
tima in kinematic-only rewards. To make up for the lack
of dynamic HOI data, we introduce the BallPlay dataset,
which contains eight diverse human-basketball interaction
demonstrations with high-quality SMPL-X [68] and object
motions, and contact labels.
Our core contributions can be summarized below:
• Aiming at learning dynamic HOI skills with the whole-
body humanoids in simulation, we present PhysHOI. This
first whole-body HOI imitation approach learns interac-
tion skills directly from kinematic HOI demonstrations.
• To make the method task-agnostic towards general HOI
learning, we introduce a general-purpose contact graph
(CG) as a critical complement.
Correspondingly, we
design a novel contact graph reward (CGR), which ef-
fectively guides whole-body humanoids to manipulate
objects or interact with high-dynamic objects precisely
without task-specific reward designs.
• We introduce the BallPlay dataset to fill the gap in miss-
ing dynamic HOI datasets.
High-Dynamic
Contact
Task-Agnostic
Whole-Body
Method
Year
HOI
Guidance
Rewards
Motions
DeepMimic [69]
2018
×
×
×
×
AMP [71]
2021
×
×
×
×
Hassan et al. [31]
2023
×
×
×
×
Vid2tennis [116]
2023
✓
✓
×
×
PMP [1]
2023
×
×
×
✓
Zhang et al. [122]
2023
×
×
✓
×
Braun et al. [6]
2023
×
✓
×
✓
PhysHOI (Ours)
2023
✓
✓
✓
✓
Table 1. Comparisons of the most related physics-based methods.
We validate the effectiveness of our proposed method com-
prehensively on five whole-body grasping cases and eight
basketball skills, as shown in Fig. 1 and Fig. 4.
Com-
pared with previous state-of-the-art methods, PhysHOI sig-
nificantly improves the success rate and object trajectory er-
rors. PhysHOI is simple yet effective and easy to generalize
across diverse types of HOI tasks. We hope this work could
pave the path for humanoids to learn general HOI skills.
2. Related Work
Related works on physically simulated humanoids can be
divided into isolated motion imitation and human-object in-
teraction learning. We compare the most related physics-
based work in Tab. 1 and present the related kinematics-
based methods in the Appendix.
Physics-Based Isolated Motion Imitation. Physics-based
methods generate motions via motor control in physics sim-
ulation [13, 62, 97], which addresses the physically im-
plausible artifacts of kinematic methods [9, 28, 56, 96,
118, 120], e.g., penetration, sliding, and floating.
Early
works rely on hand-crafted [35], model-based [12], and
optimization-based [94] controllers, which suffer from mo-
tion artifacts and complex parameter tuning.
Recently,
DeepMimic [69] proposes tracking motion capture se-
quences via imitation learning and deep reinforcement
learning (RL). To make the generation diverse, AMP [71]
uses generative adversarial imitation learning (GAIL) [33],
which learns the state transition distribution of unstruc-
tured motion dataset. Except for RL-based methods, some
methods use physics simulation with fully differentiable
pipelines [20, 78, 112]. Some works combine kinematic
methods with physics-based imitation policy [60, 80, 114,
116] to obtain physically plausible motions. However, these
methods only imitate isolated human motion.
Physics-based Human-Object Interaction.
Human-
object interaction (HOI) faces more challenges and is less
explored than isolated motion generation due to the com-
plexity of human body parts, various objects, and di-
verse interactions.
Compared to kinematics-based meth-
ods [75, 89, 105], physics-based methods are especially ad-
vantageous for generating human-object interaction since
the physics simulator can explicitly constrain the dynam-
ics of humanoids and objects. Using simulation, one can


<!-- page 3 (ocr) -->
st
at
Physics 
Simulator
...
...
Policy
PhysHOI
Reference 
HOI state
Simulated 
HOI state
HOI demonstration
HOI skill
HOI data
MoCap
Task-agnostic HOI imitation reward
ht+2
ht+1
gt+1
gt
Kinematic Rewards
Body
Object
IG
CG Reward
×
...
Contact 
Graph
st+1
Reference 
HOI state
Simulated 
HOI state
×
×
Figure 2. Framework overview: The proposed pipeline of learning HOI skills from HOI demonstrations. We can obtain kinematic HOI
data using mocap devices or estimated from monocular videos. Then, we transfer the HOI data into the reference HOI states, which is
a contact-aware HOI representation {human motion, object motion, interaction graph (IG), contact graph (CG)} for PhysHOI to learn.
PhysHOI: The training process of PhysHOI consists of loops of simulation and optimization. Given the simulated HOI state gt and
reference HOI state ht+1, the policy outputs the action at, then the simulated HOI state will be updated by the physics simulator. For each
time step, we calculate the proposed task-agnostic HOI imitation reward, including kinematic rewards and the key CG reward. We train
the policy until converges, where it can control simulated humanoids to reproduce the reference HOI skills.
create realistic human-object interactions such as carry-
ing boxes [31, 109], striking [72], climbing ropes [1],
grasping [6], and even challenging sports such as skat-
ing [54], playing basketball [51], soccer [38, 108], foot-
ball [55] and tennis [116]. However, these methods rely
on manual task-specific reward designs, making them dif-
ficult to generalize.
Besides, there are active topics on
human-scene interaction [65, 105] and hand-object interac-
tion [11, 15, 21, 66, 111, 115].
A highly related work is [122], where the proposed in-
teraction graph [32] is integrated into kinematic rewards
to learn the simulated multi-character interaction. Though
effective in simple human-object interactions (e.g. pick-
ing up boxes), the kinematic-only rewards are prone to
fall into local optimal when dealing with high-dynamic
scenarios. Another closely related work is [6], a frame-
work for physically plausible whole-body grasping. Sim-
ilar to previous kinematics-based grasping synthesis meth-
ods [24, 104], they design task-specific contact rewards as
guidance for learning grasp tasks. However, their method
contains multiple networks and training rounds with prior
learning dedicated to the grasp tasks. Our work explores
whole-body object interaction with static or high-dynamic
objects (e.g., grasping, playing with balls) without design-
ing task-specific rewards.
3. Method
3.1. Preliminaries on Reinforcement Learning
Our method is based on reinforcement learning, where the
agent interacts with the environment according to a policy
to maximize reward. At each time step t, the agent takes
the system states st as input and outputs an action at by
sampling the policy distribution π(at|st). According to the
physics simulator f(st+1|at, st), the new action at will re-
sult in a new state st+1. Then a reward rt = r(st, at, st+1)
can be calculated, and the goal is to learn a policy that max-
imizes the expected return R(π) = Epπ(τ)
T −1
t=0 γtrt ,
where τ = {s0, a0, r0, ..., sT −1, aT −1, rT −1, sT } repre-
sents the trajectory, pπ(τ) is the probability density func-
tion (PDF) of the trajectory. T denotes the time horizon of
a trajectory, and γ ∈[0, 1) is a discount factor. Following
prior arts [71], We use PPO [79] to optimize the policy.
3.2. Task Definition
Given a reference demonstration of Human-Object Inter-
action (HOI), represented by a kinematic sequence of hu-
man and object states, HOI imitation aims to train a policy
to control the simulated humanoid to reproduce the given
HOI. Unlike kinematics-based methods [24, 44, 89], the
core challenge here is that the object is not directly control-
lable. Instead, we can only indirectly manipulate objects by
controlling the humanoid. The whole-body humanoid fol-
lows the SMPL-X [68] kinematic tree and has a total of 52
body parts and 51×3 DoF actuators where 30×3 DoF is for
the hands and 21×3 DoF for the rest of the body. The ob-
ject is represented as a rigid body with a simplified mesh for
collision detection. Details on the HOI data preprocessing
can be found in the Appendix.
3.3. Overview of PhysHOI
In Fig. 2, we present the overview of the proposed pipeline
for HOI imitation. The core of PhysHOI is the general-
purpose contact graph (Sec. 3.4), introducing it into the
kinematics-based HOI representation as the contact-aware
HOI representation (Sec. 3.5), and the task-agnostic HOI
imitation reward (Sec. 3.6). Similar to prior arts [69], pol-
icy training consists of a loop of simulation and optimiza-
tion: the policy is first used for simulation and then opti-
mized through RL (Sec. 3.1), then the updated policy con-
tinues simulation to collect more experiences and repeat this
simulation-optimization loop until converges. Specifically,
the state st (Sec. 3.7) consists of the simulated HOI state
[=


<!-- page 4 (ocr) -->
gt and the reference HOI state ˆht+1 (Sec. 3.5). The policy
network (Sec. 3.8) takes the state st as input and outputs an
action at ∈R51×3. The PD controller outputs joint torques
(omitted in Fig. 2 for simplicity). Then the physics simula-
tor calculates the updated simulated HOI state gt+1.
3.4. General-purpose Contact Graph
Contact information is essential for HOI. Though contact
forces are hard to acquire, binary contact labels are easy to
extract from kinematic HOI data by calculating the mesh
collision or distances. In addition, estimating the contact
region from images is also a feasible direction [98]. We
propose a general-purpose Contact Graph (CG) to enhance
the HOI representation across diverse interaction imitations.
Complete CG. As illustrated in Fig. 3 (a), the CG is a com-
plete graph in which every pair of distinct nodes connected
by a unique edge, defined as G = {V, E}, where V is the set
of k nodes and E ∈{0, 1}k(k−1)/2 is the set of edges. The
nodes consist of all the objects and humanoid body parts.
Each edge stores a binary label that denotes the contact be-
tween two nodes, where 1 represents contact, and 0 means
no contact. Here, we only use the edge set of CG. The edge
value is calculated frame by frame. For an HOI sequence,
we can calculate a corresponding CG sequence {Et}, which
explicitly describes the mutual contact relationship between
objects and bodies at different moments. Considering the
trend of hinged objects, objects here can also be broken up
into finer parts [18, 23, 115].
Aggregated CG. There are three limitations in the imple-
mentation of the complete CG defined above. First, in the
whole-body grasp scenario, the complete CG has 154 nodes
(152 body parts, 1 table, and 1 object) and 11781 edges,
which is costly in memory and computation. Second, many
contact labels may be noisy due to inevitable errors from
kinematic HOI estimation and annotation. Third, the con-
tact APIs in existing physics simulation environments [62]
are not yet complete. To address these challenges, we pro-
pose the aggregated CG, where the graph node can be com-
posed of multiple aggregated parts, as illustrated in Fig. 3
(b). For example, in basketball scenarios, we can aggregate
two hands as one node, the rest of the bodies as a node,
and the ball as a node. As long as there is any collision be-
tween two aggregated nodes, e.g., the fingertip touches the
ball; the corresponding edge value becomes one. Contact
between parts belonging to the same node is not consid-
ered. The aggregated CG significantly simplifies the use of
CG and proves to be critical for simulated humanoid learn-
ing accurate HOI imitation.
3.5. Contact-Aware HOI Representation
Zhang et al. [122] introduced kinematics-based representa-
tion, including human (subject) motion ˆssbj
t
, object motion
ˆsobj
t
, interaction graph (IG) ˆsig
t . We further introduce the
1
0
0
0
Obj 1
Obj 2
Part 1
Part 2
...
...
Obj 1
Obj 2
Aggregated
parts 1
Aggregated
parts 2
...
...
(a) Contact graph
(b) Aggregated contact graph
0
0
1
0
0
1
0
0
Figure 3. Contact Graph. (a) The nodes of the complete contact
graph consist of all the objects and humanoid body parts. Each
edge stores a binary contact label. (b) A node in the aggregated
contact graph can contain multiple body parts.
proposed CG ˆscg
t to represent the reference HOI state ˆht:
ˆht = {ˆssbj
t
, ˆsobj
t
, ˆsig
t , ˆscg
t }.
(1)
The human motion ˆssbj
t
consists of the position ˆsp
t
∈
R52×3, 6D rotation ˆsr
t ∈R52×6, position velocity ˆspv
t
∈
R52×3, and rotation velocity ˆsrv
t
∈R52×6. The object mo-
tion consists of the object position ˆsop
t
∈R1×3, object 6D
rotation ˆsor
t
∈R1×6, object position velocity ˆsopv
t
∈R1×3,
and object rotation velocity ˆsorv
t
∈R1×6. All velocities
here are calculated via discrete differences, e.g. ˆsopv
t
=
ˆsop
t
−ˆsop
t−1. The IG used in this paper is inspired by pre-
vious works [32, 122], but with a simpler definition: A set
of positional vectors pointed from the objects to the contact
bodies (the body parts that have been in contact with the ob-
ject throughout the sequence). The IG ˆsig
t ∈Rn×m×3 can
be seen as a relative position representation of the object,
where n denotes the contact body numbers and m denotes
the object numbers. The CG ˆscg
t ∈{0, 1}k(k−1)/2, where k
denotes the number of CG nodes.
3.6. Task-agnostic HOI Imitation Reward
Corresponding to the reference HOI state (Sec. 3.5), the
proposed task-agnostic HOI imitation reward consists of
four parts: the body motion reward rb
t, the object motion
reward ro
t , the IG reward rig
t , and the CG reward rcg
t . To
obtain balanced reward values, we multiply these rewards
to request that none of them be small:
rt = rb
t ∗ro
t ∗rig
t ∗rcg
t ,
(2)
Body Motion Reward can be formulated as:
rb
t = rp
t ∗rr
t ∗rpv
t
∗rrv
t ,
(3)
where rp
t , rr
t , rpv
t , rrv
t
are the humanoid position reward,
rotation reward, position velocity reward, and rotation ve-
locity reward, formulated below:
rp
t = exp(−λp ∗ep
t ),
ep
t = MSE(sp
t , ˆsp
t ),
(4)
rr
t = exp(−λr ∗er
t),
er
t = MSE(sr
t, ˆsr
t),
(5)


<!-- page 5 (ocr) -->
Figure 4. Our method controls simulated humanoids to perform various basketball skills. Top-to-bottom: 1) Rebound; 2) Single-hand toss
and catch; 3) Back dribbling; 4) Cross-leg dribble. We mark red when the object has contact with the humanoid.
rpv
t
= exp(−λpv ∗epv
t ),
epv
t
= MSE(spv
t , ˆspv
t ),
(6)
rrv
t
= exp(−λrv ∗erv
t ),
erv
t
= MSE(srv
t , ˆsrv
t ),
(7)
ˆsp
t , ˆsr
t, ˆspv
t , ˆsrv
t
are the components of the reference HOI
state: the humanoid position, rotation, velocity, and rotation
velocity. sp
t , sr
t, spv
t , srv
t are calculated from simulation and
is aligned with the reference HOI state in format. λp, λr,
λpv, λrv are hyperparameters that conditions the sensitivity.
Object Motion Reward. Similar to the human motion re-
ward, the object motion reward is:
ro
t = rop
t
∗ror
t ∗ropv
t
∗rorv
t
,
(8)
where rop
t , ror
t , ropv
t
, rorv
t
are the object position reward, ro-
tation reward, position velocity reward, and rotation veloc-
ity reward, respectively. The calculation of these rewards is
similar to the Eq. 4, with λop, λor, λopv, λorv denotes the
hyperparameters that condition the reward sensitivity.
Interaction Graph Reward. The reward for the IG is:
rig
t = exp(−λig ∗eig
t ),
eig
t = MSE(sig
t , ˆsig
t ),
(9)
where ˆsig
t is the reference and sig
t is calculated from current
simulation. Note that the body motion reward rb
t, object
motion reward ro
t , and IG reward rig
t are all measurements
of kinematic properties. We call them kinematic rewards.
Contact Graph Reward.
Though kinematic rewards can
handle simple interactions, they usually do not handle dy-
namic scenarios and are not robust to noisy data, e.g., dur-
ing the training of grasp tasks, the contact between the hu-
manoid and the object will, in most cases, cause the object
to move away from the desired trajectory and the expected
return becomes smaller. In this case, the policy may learn
not to touch the object and falls into a local optimal, as
demonstrated in Fig. 7 (8). We observe that these issues
are highly related to unwanted contacts. To encourage ac-
curate contact with the object, we design the contact graph
(Sec. 3.4) and a corresponding contact graph reward (CGR)
to guide the humanoid to learn correct contact. The CG er-
ror is defined as
ecg
t = |scg
t −ˆscg
t |,
(10)
where | · | represent element wise absolute value. The CGR
is measured by CG error, with independent weights on dif-
ferent edges:
rcg
t
= exp(−
J
j=1
λcg[j] ∗ecg
t [j]),
(11)
where J = k(k−1)/2 is the CG edge numbers; ecg
t [j] is the
jth element of ecg
t
∈{0, 1}J, a binary label representing a
CG edge error; λcg[j] is the jth element of λcg ∈RJ, a hy-
perparameter controls the sensitivity of a CG edge. We mul-
tiply the CGR with the previous kinematic rewards. With
the guidance of CGR, the humanoid learns the correct con-
tact and avoids the local optimal of kinematic rewards. The
ablation study in Fig. 7 and Tab. 2 justifies our design.
No
Ne
No
ou
\
NP
2
\e
>y
>¥
+3
>¥
>Y
>y
>Y
>Y
n
a
a)
«a
A
a
mM
Y.)
o-&
2
pr
pr
pra
oP
.
.
{
A
\
<
x
N


<!-- page 6 (ocr) -->
3.7. State
The state st is the input of the policy, consisting of two
parts: the simulated HOI state gt and the reference HOI
state ˆht+1 (Sec. 3.5):
st = {gt, ˆht+1},
(12)
where the reference HOI state ˆht+1 is the target that we
expect the humanoid and objects to reach in the next time
step. The simulated HOI state represents the current hu-
manoid and object state under simulation and is necessary
for the policy to sense the current environment. Similar to
previous works [69], we transform all coordinates into the
root local coordinate of the humanoid, simplifying data dis-
tribution and making it more conducive to learning. For
the humanoid, we observe its global root height, local body
position, rotation, position velocity, and rotation velocity.
These representations form the humanoid (subject) obser-
vation osbj
t
. In addition, we detect net contact forces of
t
for the contact bodies (e.g., fingers), which helps to iden-
tify contact and accelerate training. For objects, we observe
their local position, rotation, velocity, and rotation velocity,
which form the object observation oobj
t
. The simulated HOI
state can be formulated as:
gt = {osbj
t
, of
t , oobj
t
}.
(13)
3.8. Policy and Action
We follow the actor-critic framework widely used by prior
arts [71, 72]. The policy output is modeled as a Gaussian
distribution of dimensions 51 × 3 with constant variance,
and the mean is modeled by a two-layer MLP of [1024, 512]
units and ReLU activations. The action at ∈R51×3 sam-
pled from the policy is the target joint rotations for the PD
controller. The PD controller adjusts and outputs the joint
torques to reach the target rotations.
3.9. Simulation Setting
The simulation and the PD controller run at 60 Hz. The
policy is sampled at 30Hz. The humanoid and objects need
initialization when the simulation starts. We use fixed ini-
tialization by default; that is, we extract the rotations and
root positions from the first reference frame to initialize the
humanoids and objects. We do not use random initialization
since the HOI data may have severe collisions that eject the
object. We use early termination depending on the time and
kinematic state errors. See the Appendix for details.
4. The BallPlay Dataset
To compensate for the lack of dynamic HOI scenarios, we
introduce the BallPlay dataset containing eight whole-body
basketball skills, including back dribble, cross leg, hold, fin-
gertip spin, pass, backspin, cross, and rebound, as shown
in Fig. 5. Instead of using MoCap devices that are costly
and hard to scale up, we apply a monocular annotation
solution to estimate the high-quality human SMPL-X pa-
rameters and object translations from RGB videos. How-
ever, annotating these videos with high-speed and dynamic
movements and complex interactions in the 3D camera co-
ordinate is quite challenging. Inspired by the whole-body
annotation pipeline of Motion-X [52], our automatic anno-
tation additionally introduces depth estimation [3], seman-
tic segmentation [26], and CAD model selection to obtain
high-quality whole-body human motions and object mo-
tions.
Besides, we manually annotate three key contact
frames for each video to help the object depth estimation.
The dataset contains videos, estimated HOI sequences, con-
tact labels, and physically rectified HOI sequences using
PhysHOI. Annotation details can be found in the Appendix.
Back dribble
Rebound
Cross leg
Hold
Fingertip spin
Pass
Back spin
Cross
Figure 5. The BallPlay dataset. We show the eight HOI demon-
strations of high-dynamic basketball skills. For each skill, the up-
per rows show the real-life videos, and the lower rows give the
estimated whole-body SMPL-X human model and object mesh.
AARS $8
AAR YY
Ebbott
Aff ei
Tt


<!-- page 7 (ocr) -->
PhysHOI
Zhang et al.*
AMP*
DeepMimic*
Reference
Figure 6. Qualitative results on HOI imitation. *means re-implemented methods. Previous methods that use kinematic-only rewards
fail to reproduce the interaction accurately, e.g., the ball falls or the grasp fails. Guided by the contact graph, our method yields successful
HOI imitation. We mark the object red when it has contact with the humanoid. We outline in red the frame where the failure begins.
5. Experiment
5.1. Evaluation on HOI Imitation
Datasets.
We evaluate PhysHOI on two types of HOI
datasets: GRAB [92] and our proposed BallPlay (Sec. 4).
We chose 5 cases from the GRAB S8 subset, including
grasping cube, cylinder, flashlight, flute, and bottle.
Metrics. We report three types of metrics: 1) the success
rate (Succ) of HOI imitation, where the success is defined
per frame, deeming imitation successful when the object
position and body position errors are both under the thresh-
olds and the contact graph edge value is correct. The Succ
is calculated by averaging the success values of all frames.
The object threshold is defined as 0.2m. The body thresh-
old is defined as 0.1m. The Succ reflects whether the hu-
manoid can accurately imitate the reference body motion to
interact with the object correctly. 2) the mean per-joint po-
sition error (MPJPE) of the humanoid (Eb-mpjpe) and object
(Eo-mpjpe) to evaluate the positional tracking performance
(in mm) following [60]. 3) the contact accuracy Ecg, rang-
ing from 0 to 1, defined as
1
N
N
t=1 MSE(scg
t , ˆscg
t ) where
N is the total frames of the reference HOI data.
Baseline Methods.
To the best of our knowledge, our
proposed PhysHOI is the first whole-body HOI imitation
method.
For fair comparisons, we make proper adapta-
tions for previous human motion imitation methods to ex-
periment on HOI imitation tasks: (1) DeepMimic [69] is
a motion imitation method using additive motion rewards;
we add the object motion reward to it; (2) AMP [71] is an
unaligned motion imitation method, we modify its refer-
ence state as our proposed contact-aware HOI representa-
tion from Sec.3.5; (3) We implement a simplified version of
Zhang’s method [122] via our interaction graph (Sec. 3.5)
since the code is not available yet.
Implementation Details. We use Isaac Gym [62] as the
physics simulation platform. All experiments are trained
on a single Nvidia A100 GPU, with 2048 parallel environ-
ments and fixed simulation initialization. We train 5000
epochs for all experiments on the GRAB dataset, and 15000
epochs for all experiments on the BallPlay dataset. Each
epoch contains 10 frames of sequential simulation. We use
the aggregated contact graph (CG) for experiments. For
GRAB, the CG contains 3 nodes: the table, the object, and
the aggregated whole body. For BallPlay, the CG contains
3 nodes: the object, aggregated hands, and the aggregated
rest body parts. We do not consider the basketball rotation
since it is not provided, i.e., we set λor and λorv as zero for
experiments on BallPlay. The setting of hyperparameters
can be found in the Appendix.
Qualitative Results. From Fig. 6, DeepMimic [69] and
AMP [71] achieve reasonable humanoid motion but fail to
control the object. Zhang et al. [122] is effective on some
interactions but is also prone to local optima due to the lack
of contact guidance.
We highlight the failure beginning
frames in red outlines. In contrast, the proposed PhysHOI
introduces the contact graph that makes it able to handle
-%


<!-- page 8 (ocr) -->
(10) Ref
(11) w/o CGR on table
(12) w/ CGR
(1) Ref
(2) w/o CGR
(3) w/ CGR
(7) Ref
(8) w/o CGR
(9) w/ CGR
(4) Ref
(5) w/o CGR
(6) w/ CGR
Figure 7. Ablation on Contact Graph Reward (CGR). Without CGR, the humanoid is easy to fall into local optimal, e.g., (2) using the
head to help control the ball, (5) using the wrist to touch the ball, (8) being afraid of catching objects, (11) supporting the table to keep
balance. In comparison, the use of CGR effectively guides the humanoid toward correct interaction, as shown in (3), (6), (9), and (12).
DeepMimic*
Zhang et al. *
PhysHOI (Ours)
Dataset
Succ ↑
Eb-mpjpe ↓
Eo-mpjpe ↓
Ecg ↓
Succ ↑
Eb-mpjpe ↓
Eo-mpjpe ↓
Ecg ↓
Succ ↑
Eb-mpjpe ↓
Eo-mpjpe ↓
Ecg ↓
GRAB
27.0%
44.7
180.2
0.7240
38.6%
91.0
180.1
0.3370
95.4%
71.1
78.0
0.0260
BallPlay
7.5%
40.1
1662.5
0.3063
13.6%
88.5
155.3
0.4124
82.4%
56.8
82.9
0.0877
Table 2. Quantitative results on HOI imitation. Our method yields superior object control and success rate on HOI imitation. *means
re-implemented methods. We repeat all sequences 10 times, report the average values, and bold the best score.
rb
t ∗ro
t
rb
t ∗ro
t ∗rig
t
rb
t ∗ro
t ∗rig
t ∗rcg
t
HOI Data
Succ ↑
Eb-mpjpe ↓
Eo-mpjpe ↓
Ecg ↓
Succ ↑
Eb-mpjpe ↓
Eo-mpjpe ↓
Ecg ↓
Succ ↑
Eb-mpjpe ↓
Eo-mpjpe ↓
Ecg ↓
Toss
20.7%
79.9
31.9
0.3837
7.7%
86.9
154.3
0.4396
84.8%
45.7
77.9
0.0767
Cross leg
6.7%
292.4
246.2
0.5189
8.2%
42.0
51.6
0.5394
88.2%
54.1
92.3
0.0843
Backspin
0.2%
1247.8
7105.6
0.5460
21.7%
50.4
74.9
0.3908
70.3%
60.2
65.2
0.1302
Pass
4.8%
616.5
1047.7
0.5118
16.2%
203.8
418.0
0.2909
71.2%
72.5
110.6
0.1135
Table 3. Ablation on rewards. The interaction graph reward rig
t can refine the interaction and motion imitation quality. The contact graph
reward rcg
t
significantly improves the overall performance, especially the success rate, on HOI imitation.
various complex interactions.
Quantitative Results. Tab. 2 shows the average metrics
on the GRAB subset and the BallPlay dataset. DeepMimic
[69] achieves the best score in body motion metrics, i.e.,
Eb-mpjpe, since it only learns human motions. It fails to con-
trol the object and results in low interaction success rates.
Zhang et al. [122] achieves better interaction than Deep-
Mimic, but still yields low success rates because only learn-
ing kinematic information. Interestingly, their body imita-
tion errors increase severely, and the contact accuracy wors-
ens for dynamic HOI. In contrast, PhysHOI with CG pro-
vides effective contact guidance on HOI learning and yields
superior success rates.
5.2. Ablation on Contact Graph Reward
Tab. 3 and Fig. 7 study the effectiveness of CGR. Overall,
the use of CGR significantly improves success rates. If it
only applies kinematic reward, the humanoid is prone to
fall into local optimal. For instance, the kinematic rewards
result in decent kinematic metrics on the Cross leg data, but
it uses false body parts to control the ball, resulting in infe-
rior HOI imitation in Fig. 7 (5). Similarly, in Fig. 7 (2), on
the Toss data, the humanoid wrongly learns to use its head
to control the ball. On the contrary, by applying the contact
graph reward in Fig. 7 (3) and (6), the humanoid learns cor-
rect contact and avoids incorrect collisions. Another inter-
esting phenomenon is that the HOI generated by our meth-
ods is more accurate than the reference. From Fig. 7 (1),
there is a slight floating between the hand and the ball in the
reference, while our result fits perfectly.
Considering contact with multiple objects is also neces-
sary. In the grasp tasks, the humanoid sometimes learns to
use its hands to support the table to maintain balance if the
table is not considered in the contact graph, as shown in
Fig. 7 (11). By involving the table in the contact graph, this
local optimal can be well addressed (Fig. 7 (12)). In sum-
mary, comprehensive studies have validated the essence and
effectiveness of the proposed CGR.
6. Conclusion
We present a framework for learning Human-Object Inter-
action (HOI) skills from HOI demonstrations. Our method
is able to imitate a diverse set of highly dynamic basketball
skills. We involve the contact graph (CG) to guide the hu-
manoid toward precise object control, which is proven to
be critical for HOI imitation and is effective even when the
reference HOI data is highly biased. The proposed task-
agnostic HOI imitation reward is effective on diverse HOI
types without the need to design task-specific rewards. We
also introduce an HOI dataset called BallPlay is provided
to support research on dynamic HOI. We believe this work
opens up many exciting directions for future exploration to-
ward general HOI learning. See the Appendix for more dis-
cussions about limitations and future work.
FEENEY
TR
EF
rr
EE


<!-- page 9 (ocr) -->
References
[1] Jinseok Bae, Jungdam Won, Donggeun Lim, Cheol-Hui
Min, and Young Min Kim. Pmp: Learning to physically
interact with environments using part-wise motion priors.
arXiv preprint arXiv:2305.03249, 2023. 2, 3
[2] Shikhar Bahl, Abhinav Gupta, and Deepak Pathak. Human-
to-robot imitation in the wild. In RSS, 2022. 1
[3] Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter
Wonka, and Matthias M¨uller. Zoedepth: Zero-shot trans-
fer by combining relative and metric depth. arXiv preprint
arXiv:2302.12288, 2023. 6, 2
[4] Bharat Lal Bhatnagar, Xianghui Xie, Ilya Petrov, Cristian
Sminchisescu, Christian Theobalt, and Gerard Pons-Moll.
BEHAVE: Dataset and method for tracking human object
interactions. In CVPR, 2022. 3
[5] Steven Bohez, Saran Tunyasuvunakool, Philemon Brakel,
Fereshteh Sadeghi, Leonard Hasenclever, Yuval Tassa,
Emilio Parisotto, Jan Humplik, Tuomas Haarnoja, Roland
Hafner, et al.
Imitate and repurpose: Learning reusable
robot movement skills from human and animal behaviors.
arXiv preprint arXiv:2203.17138, 2022. 1
[6] Jona Braun, Sammy Christen, Muhammed Kocabas, Emre
Aksan, and Otmar Hilliges. Physically plausible full-body
hand-object interaction synthesis. In International Confer-
ence on 3D Vision (3DV), 2024. 2, 3
[7] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Nee-
lakantan, Pranav Shyam, Girish Sastry, Amanda Askell,
Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger,
Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M.
Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse,
Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Ben-
jamin Chess, Jack Clark, Christopher Berner, Sam McCan-
dlish, Alec Radford, Ilya Sutskever, and Dario Amodei.
Language models are few-shot learners. 2020. 3
[8] Angel X Chang, Thomas Funkhouser, Leonidas Guibas,
Pat Hanrahan, Qixing Huang, Zimo Li, Silvio Savarese,
Manolis Savva, Shuran Song, Hao Su, et al.
Shapenet:
An information-rich 3d model repository. arXiv preprint
arXiv:1512.03012, 2015. 2
[9] Xin Chen, Biao Jiang, Wen Liu, Zilong Huang, Bin Fu, Tao
Chen, and Gang Yu. Executing your commands via motion
diffusion in latent space. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition,
pages 18000–18010, 2023. 2, 3
[10] Yixin Chen, Sai Kumar Dwivedi, Michael J Black, and
Dimitrios Tzionas. Detecting human-object contact in im-
ages. In CVPR, 2023. 3
[11] Sammy Christen, Muhammed Kocabas, Emre Aksan,
Jemin Hwangbo, Jie Song, and Otmar Hilliges. D-grasp:
Physically plausible dynamic grasp synthesis for hand-
object interactions. In Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition, pages
20577–20586, 2022. 3
[12] Stelian Coros, Philippe Beaudoin, and Michiel van de
Panne. Generalized biped walking control. ACM Trans-
actions on Graphics, 29(4):1–9, 2010. 2
[13] Erwin Coumans and Yunfei Bai. Pybullet, a python mod-
ule for physics simulation for games, robotics and machine
learning. 2016. 2
[14] Rishabh Dabral, Muhammad Hamza Mughal, Vladislav
Golyanik, and Christian Theobalt.
Mofusion: A frame-
work for denoising-diffusion-based motion synthesis.
In
Proceedings of the IEEE/CVF Conference on Computer Vi-
sion and Pattern Recognition, pages 9760–9770, 2023. 3
[15] Sudeep Dasari, Abhinav Gupta, and Vikash Kumar. Learn-
ing dexterous manipulation from exemplar object trajec-
tories and pre-grasps.
In 2023 IEEE International Con-
ference on Robotics and Automation (ICRA), pages 3889–
3896. IEEE, 2023. 3
[16] Dawson-Haggerty et al. trimesh. 2
[17] Alejandro Escontrela, Xue Bin Peng, Wenhao Yu, Tingnan
Zhang, Atil Iscen, Ken Goldberg, and Pieter Abbeel. Ad-
versarial motion priors make good substitutes for complex
reward functions. In 2022 IEEE/RSJ International Confer-
ence on Intelligent Robots and Systems (IROS), pages 25–
32. IEEE, 2022. 1
[18] Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed
Kocabas, Manuel Kaufmann, Michael J Black, and Otmar
Hilliges. Arctic: A dataset for dexterous bimanual hand-
object manipulation. In Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition, pages
12943–12954, 2023. 4, 3
[19] Katerina Fragkiadaki, Sergey Levine, Panna Felsen, and Ji-
tendra Malik. Recurrent network models for human dynam-
ics. In 2015 IEEE International Conference on Computer
Vision (ICCV), 2015. 3
[20] Levi Fussell, Kevin Bergamin, and Daniel Holden. Super-
track: Motion tracking for physically simulated characters
using supervised learning. ACM Transactions on Graphics
(TOG), 40(6):1–13, 2021. 2
[21] Guillermo Garcia-Hernando, Edward Johns, and Tae-Kyun
Kim.
Physics-based dexterous manipulations with esti-
mated hand poses and residual reinforcement learning. In
2020 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 9561–9568. IEEE, 2020.
3
[22] Thomas Geijtenbeek and Nicolas Pronost. Interactive char-
acter animation using simulated physics: A state-of-the-art
review.
In Computer graphics forum, pages 2492–2515.
Wiley Online Library, 2012. 1
[23] Haoran Geng, Helin Xu, Chengyang Zhao, Chao Xu, Li Yi,
Siyuan Huang, and He Wang. Gapartnet: Cross-category
domain-generalizable object perception and manipulation
via generalizable and actionable parts. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 7081–7091, 2023. 4
[24] Anindita Ghosh, Rishabh Dabral, Vladislav Golyanik,
Christian Theobalt, and Philipp Slusallek. Imos: Intent-
driven full-body motion synthesis for human-object inter-
actions. In Eurographics, 2023. 3
[25] Georgia Gkioxari, Ross Girshick, Piotr Doll´ar, and Kaim-
ing He. Detecting and recognizing human-object interac-
tions. In CVPR, 2018. 3


<!-- page 10 (ocr) -->
[26] Grounded-SAM
Contributors.
Grounded-Segment-
Anything:
https://github.com/IDEA-Research/Grounded-
Segment-Anything, 2023. 6, 2
[27] Chuan Guo, Xinxin Zuo, Sen Wang, Shihao Zou, Qingyao
Sun, Annan Deng, Minglun Gong, and Li Cheng.
Ac-
tion2motion: Conditioned generation of 3d human motions.
In Proceedings of the 28th ACM International Conference
on Multimedia, 2020. 3
[28] Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji,
Xingyu Li, and Li Cheng. Generating diverse and natural 3d
human motions from text. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition
(CVPR), pages 5152–5161, 2022. 2, 3
[29] F´elix G. Harvey, Mike Yurick, Derek Nowrouzezahrai, and
Christopher Pal.
Robust motion in-betweening.
ACM
Transactions on Graphics, 2020. 3
[30] Mohamed Hassan, Duygu Ceylan, Ruben Villegas, Jun
Saito, Jimei Yang, Yi Zhou, and Michael Black. Stochastic
scene-aware motion prediction. In ICCV, 2021. 3
[31] Mohamed Hassan, Yunrong Guo, Tingwu Wang, Michael
Black, Sanja Fidler, and Xue Bin Peng. Synthesizing phys-
ical character-scene interactions. In ACM SIGGRAPH 2022
Conference Proceedings, 2023. 2, 3
[32] Edmond SL Ho, Taku Komura, and Chiew-Lan Tai. Spa-
tial relationship preserving character motion adaptation. In
ACM SIGGRAPH 2010 papers, pages 1–8, 2010. 3, 4
[33] Jonathan Ho and Stefano Ermon. Generative adversarial
imitation learning. Advances in neural information process-
ing systems, 29, 2016. 2
[34] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising dif-
fusion probabilistic models. Advances in Neural Informa-
tion Processing Systems (NeurIPS), 33, 2020. 3
[35] Jessica K. Hodgins, Wayne L. Wooten, David C. Bro-
gan, and James F. O’Brien.
Animating human athletics.
In Proceedings of the 22nd annual conference on Com-
puter graphics and interactive techniques - SIGGRAPH
’95, 1995. 2
[36] Daniel Holden, Jun Saito, and Taku Komura. A deep learn-
ing framework for character motion synthesis and editing.
ACM Transactions on Graphics, page 1–11, 2016. 3
[37] Daniel Holden, Taku Komura, and Jun Saito.
Phase-
functioned neural networks for character control.
ACM
Transactions on Graphics, page 1–13, 2017. 3
[38] Seokpyo Hong, Daseong Han, Kyungmin Cho, Joseph S
Shin, and Junyong Noh.
Physics-based full-body soccer
motion control for dribbling and shooting. ACM Transac-
tions on Graphics (TOG), 38(4):1–12, 2019. 3
[39] Zhi Hou, Baosheng Yu, and Dacheng Tao.
Composi-
tional 3d human-object neural animation. arXiv preprint
arXiv:2304.14070, 2023. 3
[40] Yinghao Huang, Omid Taheri, Michael J. Black, and Dim-
itrios Tzionas. InterCap: Joint markerless 3D tracking of
humans and objects in interaction. In GCPR, 2022. 3
[41] Jingwei Ji, Rishi Desai, and Juan Carlos Niebles. Detecting
human-object relationships in videos. In ICCV, 2021. 3
[42] Nan Jiang, Tengyu Liu, Zhexuan Cao, Jieming Cui, Yixin
Chen, He Wang, Yixin Zhu, and Siyuan Huang. CHAIRS:
Towards full-body articulated human-object interaction.
arXiv preprint arXiv:2212.10621, 2022. 3
[43] Peng Jin, Yang Wu, Yanbo Fan, Zhongqian Sun, Yang Wei,
and Li Yuan. Act as you wish: Fine-grained control of mo-
tion diffusion model with hierarchical semantic graphs. In
NeurIPS, 2023. 3
[44] Roy Kapon, Guy Tevet, Daniel Cohen-Or, and Amit H
Bermano.
Mas: Multi-view ancestral sampling for 3d
motion generation using 2d diffusion.
arXiv preprint
arXiv:2310.14729, 2023. 3
[45] Bahjat Kawar, Michael Elad, Stefano Ermon, and Jiaming
Song.
Denoising diffusion restoration models.
In ICLR
Workshop on Deep Generative Models for Highly Struc-
tured Data (ICLRW), 2022. 3
[46] Taeksoo Kim, Shunsuke Saito, and Hanbyul Joo. NCHO:
Unsupervised learning for neural 3d composition of hu-
mans and objects. In ICCV, 2023. 3
[47] Jiye
Lee
and
Hanbyul
Joo.
Locomotion-action-
manipulation:
Synthesizing
human-scene
interac-
tions in complex 3d environments.
arXiv preprint
arXiv:2301.02667, 2023. 3
[48] Jiaman Li, Jiajun Wu, and C Karen Liu.
Object mo-
tion guided human motion synthesis.
arXiv preprint
arXiv:2309.16237, 2023. 3
[49] Ruilong Li, Shan Yang, David A. Ross, and Angjoo
Kanazawa. Learn to dance with aist++: Music conditioned
3d dance generation, 2021. 3
[50] Yuanzhi Liang, Qianyu Feng, Linchao Zhu, Li Hu, Pan Pan,
and Yi Yang. Seeg: Semantic energized co-speech gesture
generation. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 10473–
10482, 2022. 3
[51] Jessica Hodgins Libin Liu. Learning basketball dribbling
skills using trajectory optimization and deep reinforcement
learning. ACM Transactions on Graphics, 37(4), August
2018. 3
[52] Jing Lin, Ailing Zeng, Shunlin Lu, Yuanhao Cai, Ruimao
Zhang, Haoqian Wang, and Lei Zhang. Motion-x: A large-
scale 3d expressive whole-body human motion dataset. Ad-
vances in Neural Information Processing Systems, 2023. 6,
2, 3
[53] Hung Yu Ling, Fabio Zinno, George Cheng, and Michiel
Van De Panne. Character controllers using motion vaes.
ACM Transactions on Graphics, 2020. 1, 3, 4
[54] Libin Liu and Jessica Hodgins. Learning to schedule con-
trol fragments for physics-based characters using deep q-
learning. ACM Transactions on Graphics, 36(3), 2017. 3
[55] Siqi Liu, Guy Lever, Zhe Wang, Josh Merel, SM Ali Es-
lami, Daniel Hennes, Wojciech M Czarnecki, Yuval Tassa,
Shayegan Omidshafiei, Abbas Abdolmaleki, et al. From
motor control to team play in simulated humanoid football.
Science Robotics, 7(69):eabo0235, 2022. 3
[56] Shunlin Lu, Ling-Hao Chen, Ailing Zeng, Jing Lin,
Ruimao Zhang, Lei Zhang, and Heung-Yeung Shum. Hu-
mantomato: Text-aligned whole-body motion generation.
arxiv:2310.12978, 2023. 2, 3


<!-- page 11 (ocr) -->
[57] Michael Luck and Ruth Aylett. Applying artificial intel-
ligence to virtual reality: Intelligent virtual environments.
Applied artificial intelligence, 14(1):3–32, 2000. 1
[58] Zhengyi Luo, Ryo Hachiuma, Ye Yuan, and Kris Kitani.
Dynamics-regulated kinematic policy for egocentric pose
estimation. In Advances in Neural Information Processing
Systems, 2021. 1
[59] Zhengyi Luo, Shun Iwase, Ye Yuan, and Kris Kitani. Em-
bodied scene-aware human pose estimation. In Advances in
Neural Information Processing Systems, 2022. 1
[60] Zhengyi Luo, Jinkun Cao, Alexander Winkler, Kris Kitani,
and Weipeng Xu. Perpetual humanoid control for real-time
simulated avatars, 2023. 2, 7
[61] Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje,
Gerard Pons-Moll, and Michael J. Black. AMASS: Archive
of motion capture as surface shapes. In International Con-
ference on Computer Vision, pages 5442–5451, 2019. 3
[62] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo,
Michelle Lu, Kier Storey, Miles Macklin, David Hoeller,
Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel
State. Isaac gym: High performance GPU based physics
simulation for robot learning.
In Thirty-fifth Conference
on Neural Information Processing Systems Datasets and
Benchmarks Track (Round 2), 2021. 2, 4, 7
[63] Julieta Martinez, Michael J. Black, and Javier Romero. On
human motion prediction using recurrent neural networks.
In 2017 IEEE Conference on Computer Vision and Pattern
Recognition (CVPR), 2017. 3
[64] Lucas Mourot, Ludovic Hoyet, Franc¸ois Le Clerc, Franc¸ois
Schnitzler, and Pierre Hellier. A survey on deep learning for
skeleton-based human animation. In Computer Graphics
Forum, pages 122–157. Wiley Online Library, 2022. 1
[65] Liang Pan, Jingbo Wang, Buzhen Huang, Junyu Zhang,
Haofan Wang, Xu Tang, and Yangang Wang. Synthesiz-
ing physically plausible human motions in 3d scenes. arXiv
preprint arXiv:2308.09036, 2023. 3
[66] Austin Patel, Andrew Wang, Ilija Radosavovic, and Jitendra
Malik. Learning to imitate object interactions from internet
videos. arXiv preprint arXiv:2211.13225, 2022. 3
[67] Georgios Pavlakos, Vasileios Choutas, Nima Ghorbani,
Timo Bolkart, Ahmed A. A. Osman, Dimitrios Tzionas,
and Michael J. Black. Expressive body capture: 3D hands,
face, and body from a single image.
In Proceedings
IEEE Conf. on Computer Vision and Pattern Recognition
(CVPR), pages 10975–10985, 2019. 1
[68] Georgios Pavlakos, Vasileios Choutas, Nima Ghorbani,
Timo Bolkart, Ahmed A. A. Osman, Dimitrios Tzionas,
and Michael J. Black. Expressive body capture: 3d hands,
face, and body from a single image.
In Proceedings
IEEE Conf. on Computer Vision and Pattern Recognition
(CVPR), 2019. 2, 3
[69] Xue Bin Peng, Pieter Abbeel, Sergey Levine, and Michiel
van de Panne. Deepmimic. ACM Transactions on Graphics,
page 1–14, 2018. 1, 2, 3, 6, 7, 8
[70] Xue Bin Peng, Erwin Coumans, Tingnan Zhang, Tsang-
Wei Edward Lee, Jie Tan, and Sergey Levine. Learning
agile robotic locomotion skills by imitating animals.
In
Robotics: Science and Systems, 2020.
[71] Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, and
Angjoo Kanazawa.
Amp: Adversarial motion priors for
stylized physics-based character control.
ACM Transac-
tions on Graphics, page 1–20, 2021. 2, 3, 6, 7
[72] Xue Bin Peng, Yunrong Guo, Lina Halper, Sergexuey
Levine, and Sanja Fidler. Ase: Large-scale reusable adver-
sarial skill embeddings for physically simulated characters.
ACM Trans. Graph., 41(4), 2022. 1, 3, 6, 2
[73] Ilya A Petrov, Riccardo Marin, Julian Chibane, and Gerard
Pons-Moll. Object pop-up: Can we infer 3d objects and
their poses from human interactions alone? In CVPR, 2023.
3
[74] Mathis Petrovich, Michael J. Black, and Gul Varol. Action-
conditioned 3d human motion synthesis with transformer
vae. In 2021 IEEE/CVF International Conference on Com-
puter Vision (ICCV), 2021. 3
[75] Huaijin Pi, Sida Peng, Minghui Yang, Xiaowei Zhou, and
Hujun Bao. Hierarchical generation of human-object inter-
actions with diffusion probabilistic models. In Proceedings
of the IEEE/CVF International Conference on Computer
Vision, pages 15061–15073, 2023. 2, 3
[76] Matthias Plappert, Christian Mandery, and Tamim Asfour.
The KIT motion-language dataset. Big Data, 4(4):236–252,
2016. 3
[77] Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario
Amodei, and Ilya Sutskever. Language models are unsu-
pervised multitask learners. 2019. 3
[78] Jiawei Ren, Cunjun Yu, Siwei Chen, Xiao Ma, Liang Pan,
and Ziwei Liu.
Diffmimic: Efficient motion mimicking
with differentiable physics. In The Eleventh International
Conference on Learning Representations, 2023. 2
[79] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Rad-
ford, and Oleg Klimov. Proximal policy optimization algo-
rithms. arXiv preprint arXiv:1707.06347, 2017. 3
[80] Yi Shi,
Jingbo Wang,
Xuekun Jiang,
and Bo Dai.
Controllable motion diffusion model.
arXiv preprint
arXiv:2306.00416, 2023. 2
[81] Laura M. Smith, J. Chase Kew, Tianyu Li, Linda Luu,
Xue Bin Peng, Sehoon Ha, Jie Tan, and Sergey Levine.
Learning and adapting agile locomotion skills by transfer-
ring experience. In Robotics: Science and Systems XIX,
Daegu, Republic of Korea, July 10-14, 2023, 2023. 1
[82] Jiaming Song,
Chenlin Meng,
and Stefano Ermon.
Denoising diffusion implicit models.
arXiv preprint
arXiv:2010.02502, 2020. 3
[83] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denois-
ing diffusion implicit models. In International Conference
on Learning Representations (ICLR), 2021.
[84] Yang Song and Stefano Ermon. Generative modeling by
estimating gradients of the data distribution.
Advances
in Neural Information Processing Systems (NeurIPS), 32,
2019.
[85] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma,
Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-
based generative modeling through stochastic differential
equations. In International Conference on Learning Repre-
sentations (ICLR), 2020. 3


<!-- page 12 (ocr) -->
[86] Jackie Stacey and Lucy Suchman.
Animation and
automation–the liveliness and labours of bodies and ma-
chines. Body & Society, 18(1):1–46, 2012. 1
[87] Sebastian Starke, He Zhang, Taku Komura, and Jun Saito.
Neural state machine for character-scene interactions. ACM
Trans. Graph., 38(6):209–1, 2019. 3
[88] Sebastian Starke, Yiwei Zhao, Taku Komura, and Kazi Za-
man. Local motion phases for learning multi-contact char-
acter movements. ACM Transactions on Graphics, 2020.
3
[89] Sebastian Starke, Yiwei Zhao, Taku Komura, and Kazi Za-
man. Local motion phases for learning multi-contact char-
acter movements. ACM Transactions on Graphics (TOG),
39(4):54–1, 2020. 2, 3
[90] Sebastian Starke, Yiwei Zhao, Fabio Zinno, and Taku Ko-
mura. Neural animation layering for synthesizing martial
arts movements.
ACM Transactions on Graphics, page
1–16, 2021.
[91] Sebastian Starke, Ian Mason, and Taku Komura.
Deep-
phase. ACM Transactions on Graphics, 41(4):1–13, 2022.
3
[92] Omid Taheri, Nima Ghorbani, Michael J. Black, and Dim-
itrios Tzionas.
GRAB: A dataset of whole-body human
grasping of objects. In European Conference on Computer
Vision (ECCV), 2020. 7, 3
[93] Omid Taheri, Vasileios Choutas, Michael J. Black, and
Dimitrios Tzionas. Goal: Generating 4d whole-body mo-
tion for hand-object grasping. In 2022 IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition (CVPR),
2022. 3
[94] Jie Tan, Yuting Gu, C. Karen Liu, and Greg Turk. Learning
bicycle stunts. ACM Transactions on Graphics, 33(4):1–12,
2014. 2
[95] Purva Tendulkar, D´ıdac Sur´ıs, and Carl Vondrick.
Flex:
Full-body grasping without full-body grasps. In Proceed-
ings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 21179–21189, 2023. 3
[96] Guy Tevet, Sigal Raab, Brian Gordon, Yoni Shafir, Daniel
Cohen-or, and Amit Haim Bermano. Human motion diffu-
sion model. In The Eleventh International Conference on
Learning Representations, 2023. 2, 3
[97] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A
physics engine for model-based control. In 2012 IEEE/RSJ
international conference on intelligent robots and systems,
pages 5026–5033. IEEE, 2012. 2
[98] Shashank Tripathi, Agniv Chatterjee, Jean-Claude Passy,
Hongwei Yi, Dimitrios Tzionas, and Michael J. Black.
DECO: Dense estimation of 3D human-scene contact in
the wild. In Proceedings of the IEEE/CVF International
Conference on Computer Vision (ICCV), pages 8001–8013,
2023. 4
[99] Jonathan Tseng, Rodrigo Castellon, and Karen Liu. Edge:
Editable dance generation from music. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 448–458, 2023. 3
[100] Xi Wang, Gen Li, Yen-Ling Kuo, Muhammed Kocabas,
Emre Aksan, and Otmar Hilliges. Reconstructing action-
conditioned human-object interactions using commonsense
knowledge priors. In 3DV, 2022. 3
[101] Yinhuai Wang, Jiwen Yu, and Jian Zhang. Zero-shot image
restoration using denoising diffusion null-space model. In
The Eleventh International Conference on Learning Repre-
sentations, 2023. 3
[102] Jungdam Won, Deepak Gopinath, and Jessica Hodgins.
Physics-based character controllers using conditional vaes.
ACM Transactions on Graphics (TOG), 41(4):1–12, 2022.
1
[103] Xiaoqian Wu, Yong-Lu Li, Xinpeng Liu, Junyi Zhang,
Yuzhe Wu, and Cewu Lu. Mining cross-person cues for
body-part interactiveness learning in hoi detection.
In
ECCV, 2022. 3
[104] Yan Wu, Jiahao Wang, Yan Zhang, Siwei Zhang, Otmar
Hilliges, Fisher Yu, and Siyu Tang. Saga: Stochastic whole-
body grasping with contact. In Proceedings of the European
Conference on Computer Vision (ECCV), 2022. 3
[105] Zeqi Xiao, Tai Wang, Jingbo Wang, Jinkun Cao, Wenwei
Zhang, Bo Dai, Dahua Lin, and Jiangmiao Pang. Unified
human-scene interaction via prompted chain-of-contacts.
arXiv preprint arXiv:2309.07918, 2023. 2, 3
[106] Xianghui Xie, Bharat Lal Bhatnagar, and Gerard Pons-
Moll.
Chore: Contact, human and object reconstruction
from a single rgb image. In ECCV, 2022. 3
[107] Xianghui Xie, Bharat Lal Bhatnagar, and Gerard Pons-
Moll. Visibility aware human-object interaction tracking
from single rgb camera. In CVPR, 2023. 3
[108] Zhaoming Xie, Sebastian Starke, Hung Yu Ling, and
Michiel van de Panne. Learning soccer juggling skills with
layer-wise mixture-of-experts. In ACM SIGGRAPH 2022
Conference Proceedings, pages 1–9, 2022. 3
[109] Zhaoming Xie, Jonathan Tseng, Sebastian Starke, Michiel
van de Panne, and C. Karen Liu. Hierarchical planning and
control for box loco-manipulation, 2023. 3
[110] Sirui Xu, Zhengyuan Li, Yu-Xiong Wang, and Liang-Yan
Gui.
Interdiff: Generating 3d human-object interactions
with physics-informed diffusion.
In Proceedings of the
IEEE/CVF International Conference on Computer Vision,
pages 14928–14940, 2023. 3
[111] Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu,
Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng,
Yijia Weng, Jiayi Chen, et al.
Unidexgrasp: Universal
robotic dexterous grasping via learning diverse proposal
generation and goal-conditioned policy. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 4737–4746, 2023. 3
[112] Heyuan Yao, Zhenhua Song, Baoquan Chen, and Libin Liu.
Controlvae: Model-based learning of generative controllers
for physics-based characters. ACM Transactions on Graph-
ics (TOG), 41(6):1–16, 2022. 2
[113] Youngwoo Yoon, Woo-Ri Ko, Minsu Jang, Jaeyeon Lee,
Jaehong Kim, and Geehyuk Lee. Robots learn social skills:
End-to-end learning of co-speech gesture generation for
humanoid robots.
In 2019 International Conference on
Robotics and Automation (ICRA), pages 4303–4309. IEEE,
2019. 3


<!-- page 13 (ocr) -->
[114] Ye Yuan, Jiaming Song, Umar Iqbal, Arash Vahdat, and Jan
Kautz. Physdiff: Physics-guided human motion diffusion
model, 2022. 2
[115] Hui Zhang, Sammy Christen, Zicong Fan, Luocheng
Zheng, Jemin Hwangbo, Jie Song, and Otmar Hilliges.
Artigrasp:
Physically plausible synthesis of bi-manual
dexterous grasping and articulation.
arXiv preprint
arXiv:2309.03891, 2023. 3, 4
[116] Haotian Zhang, Ye Yuan, Viktor Makoviychuk, Yunrong
Guo, Sanja Fidler, Xue Bin Peng, and Kayvon Fatahalian.
Learning physically simulated tennis skills from broadcast
videos. ACM Trans. Graph., 2023. 1, 2, 3
[117] Juze Zhang, Haimin Luo, Hongdi Yang, Xinru Xu,
Qianyang Wu, Ye Shi, Jingyi Yu, Lan Xu, and Jingya Wang.
NeuralDome: A neural modeling pipeline on multi-view
human-object interactions. In CVPR, 2023. 3
[118] Jianrong Zhang, Yangsong Zhang, Xiaodong Cun, Shaoli
Huang, Yong Zhang, Hongwei Zhao, Hongtao Lu, and Xi
Shen.
T2m-gpt: Generating human motion from textual
descriptions with discrete representations. Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, 2023. 2, 3
[119] Jason Y Zhang, Sam Pepose, Hanbyul Joo, Deva Ramanan,
Jitendra Malik, and Angjoo Kanazawa.
Perceiving 3d
human-object spatial arrangements from a single image in
the wild. In ECCV, 2020. 3
[120] Mingyuan Zhang, Zhongang Cai, Liang Pan, Fangzhou
Hong, Xinying Guo, Lei Yang, and Ziwei Liu. Motiondif-
fuse: Text-driven human motion generation with diffusion
model. arXiv preprint arXiv:2208.15001, 2022. 2, 3
[121] Xiaohan Zhang, Bharat Lal Bhatnagar, Sebastian Starke,
Vladimir Guzov, and Gerard Pons-Moll. COUCH: Towards
controllable human-chair interactions. In ECCV, 2022. 3
[122] Yunbo Zhang, Deepak Gopinath, Yuting Ye, Jessica Hod-
gins, Greg Turk, and Jungdam Won. Simulation and re-
targeting of complex multi-character interactions. In ACM
SIGGRAPH 2023 Conference Proceedings, 2023. 2, 3, 4,
7, 8
[123] Desen Zhou, Zhichao Liu, Jian Wang, Leshan Wang, Tao
Hu, Errui Ding, and Jingdong Wang. Human-object inter-
action detection via disentangled transformer.
In CVPR,
2022. 3
[124] Fangrui Zhu, Yiming Xie, Weidi Xie, and Huaizu Jiang.
Diagnosing human-object interaction detectors.
arXiv
preprint arXiv:2308.08529, 2023. 3
[125] Lingting Zhu, Xian Liu, Xuanyu Liu, Rui Qian, Ziwei
Liu, and Lequan Yu. Taming diffusion models for audio-
driven co-speech gesture generation.
In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 10544–10553, 2023. 3


<!-- page 14 (ocr) -->
PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction
Supplementary Material
In the following document, we provide additional infor-
mation to supplement the main paper. Video demonstra-
tions can be found on our project page. We will release the
BallPlay dataset and open source the code.
Contents
A. Technical Details
1
A.1. HOI Data Preprocessing . . . . . . . . . . .
1
A.2. Details on Simulation Setting
. . . . . . . .
1
A.3. Experiment Details . . . . . . . . . . . . . .
2
B. The BallPlay Dataset
2
B.1. HOI Data Annotation . . . . . . . . . . . . .
2
B.2. Refine The HOI Data Using PhysHOI . . . .
2
C. Additional Experiments
3
C.1. Varying Ball Sizes . . . . . . . . . . . . . .
3
C.2. Ablation on Contact Graph Reward . . . . .
3
D. Related Work on Kinematic-Based Methods
3
D.1. Human Motion Generation . . . . . . . . . .
3
D.2. Human-Object Interaction Generation . . . .
3
E. Discussions
4
E.1. Failure Cases . . . . . . . . . . . . . . . . .
4
E.2. Limitations . . . . . . . . . . . . . . . . . .
4
E.3. Future Work
. . . . . . . . . . . . . . . . .
4
A. Technical Details
A.1. HOI Data Preprocessing
Since the shapes of humans and objects in HOI data are rep-
resented by mesh and cannot be directly used for the simula-
tion environment, we build the simulation models of robots
and objects to match their meshes and make necessary cali-
brations for the HOI data.
Raw HOI Data Format. The raw HOI data consists of
frames at 30 fps. Each frame contains the human joint rota-
tion, human root rotation, human root position, object posi-
tion, and object rotation. We use the SMPL-X model [67] to
parameterize the whole-body shape as β ∈R10 and whole-
body pose as θ ∈R51×3. The object is represented as mesh.
Simulation Models for Human and Object.
Given an
SMPL-X shape parameter β, we generate a corresponding
whole-body humanoid robot following UHC [58, 59]. To
drive the poses, we use SMPL-X pose parameter θ. Accord-
ingly, the robot has a total of 51×3 DoF actuators where
21×3 DoF for the body and 30×3 DoF for the hands. To
Figure 8. The original human and object shape (bottom) and their
approximated simulation model (up).
simplify collision calculation, bodies are simplified as sim-
ple geometries like capsules or boxes. For general objects,
we use convex decomposition to approximate the object
mesh as convex hulls, which is necessary for collision de-
tection. For the basketball, we simply use a sphere as an
approximation. Fig. 8 shows the original human and object
shape and the approximated simulation model.
HOI Data Calibration. We transfer the original HOI data
to the simulation environment and perform coordinate cal-
ibration to obtain preliminary data samples. To accurately
model interaction information, we extract and save the body
positions and the binary contact labels per frame, which can
be easily acquired by reading the simulator’s API after load-
ing the calibrated HOI data into the simulation. This data
calibration process is effective in resolving hand-object pen-
etration in the data, because the simulator will automatically
adjust the body position to avoid collision.
A.2. Details on Simulation Setting
Simulation Initialization. We use first-frame initialization
by default; that is, we extract the rotations and root posi-
tions from the first reference state to initialize the robot and
objects.
Early Termination. Since our imitation learning is strictly
aligned with the reference frame, the maximum duration of
the simulation is the length of the reference HOI sequence.
In general, during training, the simulation is reset only when
the maximum time is reached. However, during the training
process, the robot often fails before reaching the maximum
time, such as falling down or the object significantly devi-
ating from the reference trajectory. In these cases, we reset
the simulation to improve the simulation sample efficiency.
Specifically, in three cases we reset the simulation: (1) the
maximum time is reached; (2) the object deviates far from
the reference trajectory; (3) the robot positions deviate from
the reference. The threshold of position error is set to 0.5m.


<!-- page 15 (ocr) -->
body
object
IG
CG
Dataset
λp
λr
λpv
λrv
λop
λor
λopv
λorv
λig
λcg[0]
λcg[1]
λcg[2]
BallPlay
50
20
0.01
0.01
1
0
0.01
0
20
5
5
5
GRAB
50
20
0.01
0.01
1
0.1
0.01
0.01
20
50
5
5
Table 4. Reward weights for PhysHOI. Note that for the finger-
tip spin case, we set λcg[0]=0.01 to weak restrictions on contact
between hands and the ball, as explained in Fig. 14.
body
object
IG
CG
Methods
+ or ×
rp
rr
rpv
rrv
rop
ror
ropv
rorv
rig
rcg
DeepMimic
+
✓
✓
✓
✓
✓
✓
✓
✓
×
×
Zhang et al.
×
✓
✓
✓
✓
✓
✓
✓
✓
✓
×
Table 5. Reward design for re-implemented methods.
A.3. Experiment Details
Hyperparameters. We use the aggregated contact graph
(CG) for experiments. For GRAB, the CG contains 3 nodes:
the table, the object, and the aggregated whole body. For
BallPlay, the CG contains 3 nodes: the object, the aggre-
gated hands, and the aggregated rest body parts. We pro-
vide the setting of reward weights in Tab. 4. For BallPlay,
λcg[0] corresponding to the CG edge connecting the hands
and the ball, λcg[1] corresponding to the CG edge connect-
ing the hands and the rest body, λcg[2] corresponding to the
CG edge connecting the rest body and the ball. For GRAB,
λcg[0] corresponding to the CG edge connecting the body
and the object, λcg[1] corresponding to the CG edge con-
necting the body and the table, λcg[2] corresponding to the
CG edge connecting the table and the object.
Details on Re-Implemented Methods. For fair compar-
isons, we re-implement related state-of-the-art methods:
DeepMimic [69], AMP [71], and Zhang’s method [122].
The main difference is the reward design, which is pre-
sented in Tab. 5. Note that our code is based on the ASE
project [72], which contains the implementation of AMP.
We change the original AMP observation as our HOI repre-
sentation for HOI imitation.
Contact Detection. Since Isaac Gym does not yet provide
contact detection APIs for the GPU pipeline, we use force
detections as approximations for contact detections. For ex-
ample, if the net contact force of the ball on either of the x
and y axes is above a threshold and the net contact force
of the hands-excluded body parts is under a threshold, we
deem that the ball has contact with the hands.
B. The BallPlay Dataset
B.1. HOI Data Annotation
To construct the BallPlay dataset, we propose a semi-
automatic annotation pipeline to estimate 3D human-object
interaction motion from monocular RGB videos. As de-
picted in Fig. 9, our annotation pipeline mainly involved
three stages: whole-body human motion annotation, object
annotation, and contact-based manual correction.
Whole-Body Human Motion Annotation. Initially, we
adopt an optimization-based approach, as introduced in
Motion-X [52], to annotate high-quality 3D whole-body hu-
man motion from RGB videos. This optimization process
also includes the estimation of camera parameters.
Object Annotation. Subsequently, we employ Grounded-
SAM [26] to annotate the object category and the segmen-
tation mask, along with utilizing ZoeDepth [3] for depth es-
timation. We then project the object mask into a point cloud
in the world coordinate system based on the depth map and
camera parameters. The central point of the resulting point
cloud serves as the initialized object center. Meanwhile,
based on the object category, we retrieve the object mesh
from a CAD model library. The meshes of the CAD model
library are collected from ShapeNet [8] and some geome-
tries built by ourselves with Trimesh [16] tool.
Contact-based Manual Correction. Due to the inherent
depth ambiguity of monocular video, the object center ob-
tained from the previous steps can be noisy. To address this
issue, we propose a contact-based manual correction proce-
dure. Specifically, we manually annotate the human-object
contact labels of three keyframes within each video, and
then compute the average depth of the contact body parts to
update the object center position. This manual correction
can greatly mitigate depth ambiguity and enhance overall
data quality. Ultimately, our refined object mesh and human
mesh constitute the final human-object interaction dataset.
Human 
Detection
Grounded -
SAM
Camera
Projection
Pose
Optimization
Human 
Mesh
Object 
Center
CAD Models
Object 
Mesh
Category
RGB Image
Output Meshes
Depth 
Estimation
Mask
Camera
Contact Label
Depth
BBox
Figure 9. Annotation pipeline of BallPlay.
Contact Graph Annotation. We focus on basketball skills
that involve only hands to interact with the ball. In this sce-
nario, we aggregate all elements as 3 Contact Graph (CG)
nodes: the ball, the hands, and the rest of body parts. For
all sequences, the rest body parts do not come into contact
with the ball and the hands, so we only need to manually
label the CG edge between the hands and the ball, which is
easy to obtain through observation.
B.2. Refine The HOI Data Using PhysHOI
Though some HOI data in BallPlay may be biased, we may
resort to PhysHOI to eliminate errors and yield physically
plausible HOI data. As shown in Fig. 10, we can see that
the reference HOI data suffer inaccuracies, while the results
Ee


<!-- page 16 (ocr) -->
Figure 10. PhysHOI can rectify the error of reference HOI data. We can see that the reference HOI data suffers inaccuracies more or
less, while the result generated by PhysHOI can be much better than the reference.
generated by PhysHOI are much better than the reference,
in terms of physical plausibility and smoothness. Specifi-
cally, we first train PhysHOI to imitate an HOI sequence.
After convergence, we do the inference under physics sim-
ulation and record the HOI data as well as the CG through
the API of the environment. Physically rectified HOI data
is also provided in the BallPlay dataset.
C. Additional Experiments
C.1. Varying Ball Sizes
During the inference time, we change the radius of the ball
to different values and surprisingly find that the humanoids
can still perform plausible interaction, even if they are not
trained on these ball sizes. Fig. 13 shows the result in three
cases. Interestingly, we still get reasonable results without
additional training for different ball sizes, which shows the
robustness of PhysHOI. Note that the humanoid may fail if
the ball size changes too drastically.
C.2. Ablation on Contact Graph Reward
In addition to the ablation in the main paper, we provide
more visual comparisons in Fig. 12 for an intuitive under-
standing. In the cross leg case, the humanoid trained w/o
CGR tends to hold the ball between its left hand and leg
(we provide another view in red boxes for better observa-
tion), which causes unnatural interaction. In the pass case,
the ball drops without the CGR. In the fingertip spin case,
the humanoid trained w/o CGR tends to hold the ball with
its hands and head. In comparison, applying CGR addresses
these problems well. In Fig. 11 we visualize multiple en-
vironments to intuitively demonstrate the success rate w/
or w/o CGR. Each environment applies different random
seeds. We can see that the ball falling w/o CGR is not acci-
dental, but common. Instead, our method applies CGR and
achieves steady success in ball holding.
D. Related Work on Kinematic-Based Methods
D.1. Human Motion Generation
Kinematic motion generation methods are usually learned
from motion capture datasets [28, 52, 61, 76].
Early
attempts generate motions from the prefix [19, 63] and
keyframes [29]. [36] generate motions using an autoen-
coder, and further apply motion phases to generate consis-
tent motions [37, 89–91]. Beyond action-conditioned mo-
tion generation [27, 53, 74], recent advances make it possi-
ble to control motions with text description [9, 28, 43, 56,
96, 118, 120], music [14, 49, 99], and speech [50, 113, 125],
based on recent progress in autoregressive models [7, 77]
and diffusion models [34, 45, 82–85, 101].
D.2. Human-Object Interaction Generation
There are many research topics surrounding HOI, espe-
cially detection [10, 25, 41, 103, 107, 123, 124] and re-
construction [39, 46, 73, 100, 106, 119].
Based on re-
cent development of 3D HOI datasets [4, 18, 30, 40, 42,
87, 92, 117, 121], there emerges a branch of research fo-
cuses on generating human motion that interacts with ob-
jects [24, 44, 47, 48, 75, 88, 93, 95, 104, 110]. However,
all the methods mentioned learn directly from kinematic
datasets without strict modeling of dynamics and contacts,
causing artifacts that harm the motion quality, e.g., penetra-
tion, shaking, sliding, and floating. Besides, kinematic HOI
generation can not be used for robot control yet.
Fingertip spin
Jump shot
-~
-~
A
=
3
py
Aa
-
-
1 I
VY
=
Mey
— =
-
ay
4
Ew
Bl
\
~~
-
-
\
EX
Noy
»
[3
¢
|
Is)
SY
-
-
|
\


<!-- page 17 (ocr) -->
Figure 11. Ablation on Contact Graph Reward (CGR). We visualize multiple environments to intuitively demonstrate the success rate
w/ or w/o CGR. We can see that if w/o CGR, the ball falling is not accidental, but common. Instead, our method applies CGR and achieves
steady success in ball holding.
E. Discussions
E.1. Failure Cases
The failure cases of our method are mainly due to inaccu-
rate data or incomplete contact graphs. For example, in the
rebound case in Fig. 14, the ball in the reference data is al-
ways under the hand, which, combined with the fact that the
ball bounces back to the hand very quickly, results in a local
optimum: the ball is not firmly grasped during the learning
process. This problem can be solved with precise HOI data.
High CGR weight may lead to unpleasant interactions if
the CG node is not detailed enough. As shown in the finger-
tip spin case in Fig. 14, when we set a high CGR weight
on the CG edge between hands and the ball, the trained
humanoid tends to use multiple fingers to maintain steady
contact. The reasons can be twofold: (1) The CG is not
detailed enough, e.g., we simply take two hands as one CG
node, but it is necessary to take fingers as separate CG nodes
in this case. (2) The frame rate of simulation and reference
data is low, which yields frequent bouncing, i.e., less con-
tact. While reducing the corresponding CG edge weights
can improve this problem, as shown in the fingertip spin
case in Fig. 13 and Fig. 12, a more general solution requires
richer CGs and higher frame rates, which is also the solution
we expect.
E.2. Limitations
Though our method is able to mimic diverse dynamic HOI
skills, it still faces several limitations, which we list here:
• Our method may fail when the reference HOI data suffers
severe biases, e.g., the false reference data can result in a
ball drop, as shown in the rebound case in Fig. 14.
• When CG nodes are not detailed enough, some subtle
operations can still easily fall into local optimality. For
example, fingers should be independent CG nodes when
learning complex in-hand manipulations.
• Due to the low frame rate of HOI data and simulation
frequency, some minor penetrations may appear.
• Informing the policy with a single reference object state
may not be sufficient for long-term hands-off object con-
trol. For example, when learning diverse jump shot se-
quences, it is difficult for the policy to determine how to
control the ball through a single frame of HOI reference
state because the ball is out of control after being shot
out. One potential solution is to provide the policy with
multi-frame reference states of the ball.
• Our method can not generalize to HOIs that are not
trained on, e.g., the policy trained on back dribble can
not handle fingertip spin.
E.3. Future Work
We believe this work opens up many exciting directions for
future exploration, which we list here:
• Our work demonstrates the potential to learn generic hu-
man skills from diverse HOI data. The way of acquiring
HOI data accurately and conveniently is worth studying.
• When large HOI data is available, studying generalization
and generation based on HOI imitation will be an attrac-
tive direction toward future humanoid autonomy, consid-
ering no need for designing task-specific rewards. For
example, train an MVAE [53] using HOI imitation based
on a large HOI dataset.
• Although building a real humanoid with 153 DOF seems
far away, it is promising to explore retargeting-based HOI
Imitation, e.g., teaching a robot arm with a dextrous hand
to play basketball via HOI Imitation.
• Multi-human dynamic interactions are also worth study-
ing, such as multi-player basketball games.
4
10}
5}
2
EH
2
5
[<}


<!-- page 18 (ocr) -->
Ref
w/o CGR
Ours
Cross leg
Pass
Ref
w/o CGR
Ours
Fingertip spin
Ref
w/o CGR
Ours
Figure 12. Ablation on Contact Graph Reward (CGR). The humanoid trained w/o CGR tends to fall into the local optimal of kinematic
rewards, e.g., using its left leg and left hand to hold the ball. We provide the cross leg case another view in boxes for better observation.


<!-- page 19 (ocr) -->
Fingertip spin
R = 12-2 cm
R = 12+4 cm
Jump shoot
R = 12-2 cm
R = 12+1 cm
Crossover dribble
R = 12+8 cm
R = 12-6 cm
Figure 13. Varying Ball Sizes. During inference, we change the ball radius to different values. Interestingly, we still get reasonable results,
which show the robustness of PhysHOI. The default ball radius is 12cm. R denotes the changed ball radius.
2
De
=
V
r
2
CA
WwW
<7
“%
|-
-
3
.
.
.
-
S
-=


<!-- page 20 (ocr) -->
Ref
Ours
Rebound
Fingertip spin
Ref
Ours
Figure 14. Failure cases. The failure cases of our method are mainly due to inaccurate data or incomplete contact graphs. In the rebound
case, the biased ball position results in a local optimum: the ball not being firmly grasped during the learning process. High CGR weight
may lead to unpleasant interactions if the CG node is not detailed enough. In the fingertip spin case, when we set a high CGR weight on
the CG edge between hands and the ball, the trained humanoid tends to use multiple fingers to maintain steady contact. The reasons can be
twofold: (1) The CG is not detailed enough, e.g., we simply take two hands as one CG node, but it is necessary to take fingers as separate
CG nodes in this case. (2) The frame rate of simulation and reference data is low, which yields frequent bouncing, i.e., less contact. While
reducing the corresponding CG edge weights can improve this problem, as shown in the fingertip spin case in Fig. 13 and Fig. 12, a more
general solution requires richer CGs and higher frame rates, which is also the solution we expect.
EAS
4
2
et
&
7 od
Bos
v. >
>. pg
3 >
4 —
a
3
of,
¥
»
-
-
Z
ek
3
eS
Tet
-
EN
a
PN
EN
EN
\—
\r
\=
NF
No
7
iin
Ee Ce—eT e— Re
Ce — Ee
Ce —eT — ———T—
Th
~
=)
5%
=
ON
=
PA
=i
2)
