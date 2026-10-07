<!-- page 1 (ocr) -->
D-Grasp: Physically Plausible Dynamic Grasp Synthesis
for Hand-Object Interactions
Sammy Christen1
Muhammed Kocabas1,2
Emre Aksan1
Jemin Hwangbo3
Jie Song1†
Otmar Hilliges1
1Department of Computer Science, ETH Zurich
2Max Planck Institute for Intelligent Systems, T¨ubingen
3 Department of Mechanical Engineering, KAIST
Can - grasp 11- seq 3 / GT 11
Can - grasp 15- seq 2
- sequence 3
1
2
3
4
1
2
3
4
Mustard - grasp 5 - sequence 11
1
2
3
4
Mustard - grasp 5 - sequence 11
Image-based estimates
MoCap input
1
2
3
4
1
2
3
4
1
2
3
4
Figure 1. Dynamic Grasp Synthesis: Our method learns diverse grasps from static grasp labels (shown in insets), originating from existing
datasets, grasp synthesis or image-based estimates. Our approach can then synthesize diverse dynamic sequences with the objects in-hand.
We decompose the task into: stable grasping 1 - 2 , followed by the synthesis of a 3D global motion to move the object into a 6D target
pose 3 - 4 . The hand-pose is continuously adjusted to ensure a stable grasp, leading to physically plausible and human-like sequences.
Abstract
We introduce the dynamic grasp synthesis task: given an
object with a known 6D pose and a grasp reference, our
goal is to generate motions that move the object to a target
6D pose. This is challenging, because it requires reasoning
about the complex articulation of the human hand and the
intricate physical interaction with the object. We propose a
novel method that frames this problem in the reinforcement
learning framework and leverages a physics simulation,
both to learn and to evaluate such dynamic interactions.
A hierarchical approach decomposes the task into low-level
grasping and high-level motion synthesis. It can be used
to generate novel hand sequences that approach, grasp,
and move an object to a desired location, while retaining
human-likeness. We show that our approach leads to stable
grasps and generates a wide range of motions. Further-
more, even imperfect labels can be corrected by our method
to generate dynamic interaction sequences. Video and code
are available at: https://eth-ait.github.io/d-grasp/.
1. Introduction
A key problem in computer vision is to understand how
humans interact with their surroundings. Because hands
are our primary means of manipulation with the physical
world, there has been an intense interest in hand-object pose
estimation [5, 14–16, 20, 41, 42] and the synthesis of static
grasps for a given object [20, 22, 26, 41]. However, human
grasping is not limited to a single time instance, but involves
a continuous interaction with objects in order to move them.
It requires maintaining a stable grasp throughout the inter-
action, introducing intricate dynamics to the task. This in-
volves reasoning about the complex physical interactions
between the dexterous hand and the manipulated object,
including collisions, friction, and dynamics. A generative
model that can synthesize realistic and physically plausi-
ble object manipulation sequences would have many down-
stream applications in AR/VR, robotics and HCI.
†Corresponding author
1
arXiv:2112.03028v2  [cs.CV]  30 Mar 2022
wv
a Vv
«J
¢


<!-- page 2 (ocr) -->
We propose the new task of dynamic grasp synthesis.
Given an object with a known 6D pose and a static grasp
reference, our goal is to generate a grasping motion and
to move the object to a target 6D pose in a natural and
physically-plausible way.
This new setting adds several
challenges. First, the object geometry and the spatial con-
figuration of the object and the hand need to be considered
in continuous interaction.
Second, contacts between the
hand and object are crucial in maintaining stability of the
grasps, where even a small error in hand pose may lead to
an object slipping. Moreover, contact is typically unobserv-
able in images [11] and measuring the stability of a grasp is
very challenging in a static setting. Finally, synthesizing se-
quences of hand motion requires the generation of smooth
and plausible trajectories. While prior work investigates the
control of dexterous hands by learning from full demonstra-
tion trajectories [12,34], we address the generation of hand
motion from only a single-frame grasp reference. This is a
more challenging setting, because the generation of human-
like hand-object interaction trajectories without dense su-
pervision is not straightforward.
Taking a step towards this goal, we propose D-Grasp,
which generates physically plausible grasping motions with
only a single grasp reference as input (Fig. 1). Concretely,
we formulate the dynamic grasp synthesis task as a re-
inforcement learning (RL) problem and propose a policy
learning approach that leverages a physics simulation. Our
RL-based approach considers the underlying physical phe-
nomena and compensates data scarcity via exploration in
the physics simulation. This ensures physical plausibility,
e.g., there is no hand-object interpenetration and the fingers
exert enough force on the object to hold it without slipping.
Specifically, we introduce a hierarchical framework that
consists of a low-level grasping policy and a high-level mo-
tion synthesis module. The grasping policy’s purpose is
to establish and maintain a stable grasp, whereas the mo-
tion synthesis module generates a motion to move the ob-
ject to a user-specified target position. To guide the low-
level grasping policy, we require a single grasp label corre-
sponding to a static hand pose, which can be obtained either
from a hand-grasping dataset [5,14], a state-of-the-art grasp
synthesis method [20] or via an image-based pose estima-
tor [13]. Crucially, we propose a reward function that is
parameterized by the grasp label to incentivize the fingers
to reach contact points on the object, leading to human-like
grasps. Our high-level motion synthesis module generates
motions that move the hand and object to the final target
pose. Importantly, the low-level policy continually controls
the grasp to not drop the object.
In our experiments, we first demonstrate that samples
from motion capture, static grasp synthesis or image-based
pose estimates often do not lead to stable grasps when eval-
uated in a physics simulation (Fig. 4). We then present how
our method can learn to produce physically plausible and
stable grasps when guided by such labels. Next, we set out
to generate motions with the object in-hand to reach a wide
range of target poses. We provide an extensive ablation, re-
vealing the importance of the hierarchical approach and the
reward formulation for dynamic grasp synthesis.
Our contributions can be summarized as follows: i) We
introduce the new task of dynamic grasp synthesis.
ii)
We propose D-Grasp, an RL-based method to synthesize
physically-plausible and natural hand-object interactions.
iii) We show that our method can generate grasp motions
with static grasp references, which can originate from mo-
tion capture, static grasp synthesis or image-based pose es-
timation . We will release our code for research purposes.
2. Related Work
Human Grasp Prediction Recently, hand-object inter-
action has received much research attention. This growth is
accelerated by the introduction of datasets that contain both
hand and object annotations [1,2,5,9,14,25,41]. Leverag-
ing this data, a large number of methods attempt to estimate
grasp parameters, such as the hand and object pose, directly
from RGB images [4, 10, 15, 16, 23, 27, 42, 43]. Some pre-
dict the mesh of the hand and the object directly [16], or
assume a known object and predict its 6DoF in addition to
the hand [4, 15, 27, 43]. Others predict 3D keypoints and
6 DoF pose of the object [10, 42] or produce an implicit
surface representation of the grasping hands [23]. To im-
prove the prediction accuracy of the grasp, many of these
works incorporate additional contact losses [16,23] or pro-
pose a contact-aware refinement step [4,43]. More directly
related are methods that attempt to generate static grasps
given an object and sometimes also information about the
hand [1, 2, 20, 22, 23, 41, 47]. Generally, these approaches
either predict a contact map on the object [1, 2, 20] or syn-
thesize the joint-angle configuration of the grasping hand
[22, 23, 41, 47]. [20] propose a hybrid method, where pre-
dicted contact maps on objects are used to refine an initial
grasp prediction. Some methods have combined these two
directions, for example by leveraging contact information to
post-process noisy hand pose predictions [13]. [46] generate
local grasp motions, given the global motion of the hand and
object. Similarly, [44] synthesize hand grasps given full-
body and object motions. In summary, all of these works
focus on generating static grasps and are purely data-driven.
In our work, however, we take into consideration the dy-
namic nature of human-object interaction and consider the
physical plausibility of dynamic grasp-based hand-object
interactions by leveraging a physics-driven simulation.
Dexterous Hand Control Different approaches have
been used for controlling dexterous hands. Learning-based
methods most often resort to an anchored hand for in-hand
manipulation tasks [6,18,32], which removes the complex-
2


<!-- page 3 (ocr) -->
Physics Simulation
Target 6D pose
Motion Capture
or
Grasp Synthesis
Captured/predicted grasp
Grasp Policy
Motion 
Synthesis
Module
State (   ) 
Grasping Policy
Motion Policy
Feature extraction
PD Controller
MoCap/Generated
Image
Figure 2. Method Overview: Taking a single, static grasp label D and a target object 6D pose Tg as input (leftmost), D-Grasp produces
sequences of dynamic hand-object interactions (rightmost). To do so, we propose a hierarchical framework that consists of a low-level
grasping policy πg(·) and a high-level motion synthesis module. In the grasping phase, only the grasping policy is active and finds a stable
grasp on the object. In the subsequent motion synthesis phase, both the grasping policy and the motion synthesis module act concurrently.
The actions a consist of joint targets. These are combined and passed to a PD-controller that computes the required torques τ to control a
MANO-based hand model in a physics simulation. The physics simulation updates the state s which serves as input to a reward formulation
(Section 3.2.2) that forms our supervision signal and incentivizes the hand to approach and grasp the object and to move it to the target
6D pose. We introduce two feature extraction layers (φ(·) an ψ(·)) that utilize the environment state s and grasp label D to find a suitable
representation for the grasping policy and the motion synthesis module.
ity of generating collision-free trajectories, or rely on ex-
pert demonstrations [8, 12, 17, 33, 34], which can be costly
to obtain. [34] collect expert trajectories via teleoperation,
which they leverage in an RL setup to learn complex manip-
ulation tasks. [12] obtain noisy expert demonstrations from
videos and use residual RL to correct the inputs for hand-
object interaction tasks. In contrast, we only require a sin-
gle frame grasp label per sequence. Similar to our work, [8]
use a parameterized reward function from single data labels
for human-robot interactions, but assume a fixed hand to
interact with. [21] propose a modular human manipulation
framework, but focus on learning power-grasps for picking
up objects. [30] intrinsically motivate a policy to grasp in
the affordance region of objects. However, since the policy
is only incentivized to grasp in a certain region, the fingers
often end up in unnatural configurations. In their follow-up
work [29], the authors address this issue by formulating a
reward based on hand-object interaction videos. However,
the focus is on a single ”consensus” grasp reference per ob-
ject. In our work, we propose a method that learns natural
object interactions and generates a wider variety of grasps
by explicitly conditioning on the desired contact points and
hand pose.
Physics-aware Inference Several recent works have in-
troduced physical awareness to improve purely data-driven
approaches [11,28,31,35,38,39,45]. [31] use a physics sim-
ulation to validate the plausibility of a generative model for
objects via a stability measure. [11] learn to reason about
contacts and forces in hand-object interaction videos by
leveraging a physics simulation for supervision. To improve
the task of human-pose reconstruction from videos, dif-
ferent methods have added physics-based modules to cor-
rect the output of a human-pose estimation model. This
is achieved either in a post-processing optimization frame-
work [35,39], with an approxmation of physics [38], or via a
reinforcement learning policy that directly corrects the pose
estimate [45]. [28] regulate a data-driven policy for ego-
centric pose estimation with a physics-based policy. They
include full-body interactions with larger objects, such as
pushing a box. In contrast to these works, we introduce
the novel task of dynamic hand-object interactions, which
involves more fine-grained control of the dexterous human
hand and has to adhere to the dynamics and displacement
of the object of interest. The task also introduces additional
complexities due to the increased amount of collision detec-
tion queries required for accurately modeling the contacts.
To the best of our knowledge, ours is the first method that
studies this task and constitutes an important first step into
an important direction for human-object interaction.
3. Method
We propose D-Grasp, an RL-based approach that lever-
ages a physics simulation for the dynamic grasp synthe-
sis task (Fig. 2). Our model requires a static grasp label con-
sisting of the hand’s 6D global pose and local pose for the
fingers. We split the task into two distinct phases, namely
a grasping and a motion synthesis phase.
In the grasp-
ing phase, the hand needs to approach an object and find a
physically-plausible and stable grasp. In the motion synthe-
3
°
i
mglalo(s,D))
1
1
1
|
T
aT
1
b
I
—
YsTeD)—
5
| __2
1
I
|
v/a
|
=
2


<!-- page 4 (ocr) -->
sis phase, the hand has to bring the object into the 6D target
pose while the grasping policy retains a stable grasp on the
object. Therefore, the grasping policy and motion synthe-
sis module act concurrently in this phase. To this end, we
follow a hierarchical framework that functionally separates
the grasping from the motion synthesis.
In the next section, we define the task setting and provide
background on RL and the physics simulation. Thereafter,
we present both the grasping and motion synthesis phases
of our method in Sections 3.2 and 3.3, respectively.
3.1. Task Setting
In the dynamic grasp synthesis task, we are given a 6D
global pose Th and 3D local pose qh of a hand, and an
object pose To, where the 6D poses consist of a rotation and
translation component T = [q|t]. Given a label of a static
grasp D = (qh, Th, To), the goal is to grasp the object and
move it into a 6D goal pose Tg. The grasp label consists of
the 6D global pose of the hand Th and object To, as well
as the target hand pose qh at the instance of the static grasp.
Simulation Setup
To approximate a human-like hand in
the physics engine, we create a controllable hand model and
integrate information obtained from a statistical parametric
hand model (i.e., MANO [36]). We extract the skeleton of
the hand to get the relative joint positions and add joint ac-
tuators for the control of the hand. Finally, we restrict the
joints to be within reasonable limits. In our implementation,
we use a unified hand model corresponding to the mean
MANO shape. Objects are modeled via meshes from the
respective datasets [5, 14]. To further speed up the physics
simulation, we approximate simple objects with primitive
shapes via mesh alignment during training (e.g., a soup can
is approximated by a cylinder). For more complex shapes,
we use mesh decimation to reduce the number of vertices.
For further details, please refer to supp. material.
Reinforcement Learning
We follow the standard formu-
lation of a Markov Decision Process (MDP). The MDP
is defined as a tuple M = {S, A, , R, γ, T , ρ0, }, where
S and A are state and action spaces, respectively.
R :
S × A →R is the reward function, γ ∈[0, 1] a dis-
count factor, T
: S × A →S the deterministic transi-
tion function of the environment and ρ0 = p(s0) the ini-
tial state distribution. We aim to find a probabilistic pol-
icy π(at|st) with at ∈A and st ∈S, maximizing the
expected return Eat∼π(·|st),s0∼ρ0
T
i=0 γiR(st, at) with
st+1 = T (st, at) at each timestep t.
State Space
The state s = (qh, ˙qh, f, Th, ˙Th, To, ˙To)
entails proprioceptive information about the hand pose in
the form of joint angles qh and joint angular velocities ˙qh,
the forces between the hand and object f, the 6D pose of
the wrist Th and the global 6D pose of the object To with
their corresponding velocities ˙Th and ˙To. States are ex-
pressed with respect to a fixed global coordinate frame. We
show experimentally that learning from the full state space
can impede learning over several different grasp labels (Sec-
tion 4.5). We therefore propose a representation that enables
learning of the task in Section 3.2.1.
Action Space
We define an action space to control the
hand in the physics simulation. The fingers are controlled
via one actuator per joint for a total of 45 actuators, to which
we add 6 DoF to control the global pose. We employ PD-
controllers that take reference joint angles qref as input and
compute the torques that should be applied to the joints:
τ = kp(qref −q) + kd ˙q
(1)
qref = qb + a.
(2)
The policy π outputs actions a, which are residual actions
that change a bias term qb. For the finger joints, the bias
term is equivalent to the current joint configuration qb =
qh. We found this formulation to lead to smoother finger
motion and therefore more stable grasps compared to the
policy directly predicting qref. Note that for simplicity’s
sake, we use the notation qb for all joints, although the first
three DoF are translational joints.
3.2. Physically Plausible Grasping
Here we discuss the grasping phase.
The goal is to
approach an object and find a physically plausible grasp.
A careful design of the model’s input representation is
key to learning a successful model for hand-object inter-
actions [46], which we show in our ablations (Section 4.5).
Therefore, we introduce a feature extraction layer that con-
verts the information from the physics simulation and grasp
label into a suitable representation for model learning.
3.2.1
Feature Extraction for Grasping
Rather than directly conditioning the policy on the state, we
apply a feature extraction layer φ(s, D) that takes the state
and grasp label as input. For consistency, we can reformu-
late the policy as πg(a|φ(s, D)) (Fig. 2). The function φ(·)
processes information from the grasp label, and applies co-
ordinate frame transformations to achieve invariance w.r.t.
global coordinates by transforming it to object-relative co-
ordinates. To this end, the feature extraction layer receives
the state s = (qh, ˙qh, f, Th, ˙Th, To, ˙To) and grasp label
D = (qh, Th, To) as input. Its output is defined as:
φ(s, D) = (qh, ˙qh, f,
h,
o, ˙
o, ˙
h,
o,
z, G).
(3)
The terms qh and ˙qh are the local joint angles and veloc-
ities, whereas f represents contact force information. The
4
=
For


<!-- page 5 (ocr) -->
remaining components are expressed in the wrist’s refer-
ence frame (denoted by
): the object’s 6D pose
o and
its linear and angular velocities ˙
o, the hand’s 6D pose
h
(relative to the initial wrist pose and its linear and ang
r
velocity ˙
h, and the displacement of the object from its ini-
tial posit n
o. Furthermore,
z introduces awareness of
the vertical
tance to the sur ce where the object rests.
Lastly, we include the goal components G = [
x|
q|gc],
which incentivize the model to reach contact po ts n the
object. We show that these goal components are crucial for
achieving stable grasps in Section 4.5. More specifically,
the term
x measures the 3D distance between the current
and the t get 3D positions (Fig. 3), x and x, respectively.
Here, all joints and the fingertips are in the wrist’s coordi-
nate frame. Importantly, we compute object-relative target
positions from the label D in order to be invariant to the
object 6D pose during the grasping phase.
The term
q represents the angular distance between the
current rota
ns qh and target rotations qh for the joints
and the wrist. Finally, gc includes the target contact vector
gc, i.e., which finger joints should be in contact with the ob-
ject. A more detailed description about how we extract tar-
get contacts, the applied reference frame conversions, and
the coordinate representation for individual components of
the state or goal space is provided in supp. material.
3.2.2
Reward Function for Grasping
To incentivize the policy to learn the desired behavior, we
need to define a reward function. In our method, we formu-
late it as follows:
r = wxrx + wqrq + wcrc + wregrreg.
(4)
It comprises a combination between position, angle, contact
and regularization terms, respectively. We weigh the reward
components with the factors wx, wq, wc, wreg.
The position reward rx measures the weighted sum of dis-
tances between the target x and the current 3D positions x
for every joint (including the wrist):
rx =
J
j=1
wx,j∥xj −xj∥2.
(5)
Similarly, the pose reward rq measures the distance between
the current pose and the corresponding target pose in Euler
angles and corresponds to the L2-norm of the feature
q:
rq = ∥
q∥,
(6)
The contact reward rc is extracted from the finger parts that
should be in contact with the object. Specifically, it is com-
puted as the sum of two terms. The first one represents the
fraction of target contacts that the agent has achieved. The
Current hand and object pose
Target hand and object pose
Figure 3. Target Distance Component gx. It incentivizes the
policy to reach target points close to the grasp reference label D.
We extract the object-relative target 3D joint positions x from D
and compute the distance between x and the current 3D joint po-
sitions x relative to the object’s origin. We then convert gx into
wrist-relative coordinates
x.
second term rewards the amount of force exerted on desired
contact points, capped by a factor proportional to the ob-
ject’s weight mo through a factor λ:
rc =
⊤
c If>0
⊤
c
c
+ min(
⊤
c f, λmo).
(7)
Finally, the reward r eg involves regularization terms on the
hand’s and object’s linear and angular velocities:
rreg = wreg,h∥˙
h∥2 + wreg,o∥˙
o∥2.
(8)
3.2.3
Wrist-Guidance Technique
To control the global pose during the grasping phase, we
introduce a simple but effective technique which we call
wrist-guidance. Intuitively, we bias the hand to approach
the object. To achieve this, we leverage the object-relative
target pose, of the hand on the object, obtained from the
grasp label D. We then use it as a bias term in the PD-
controller of the global 3DoF position. In other words, we
set the bias term of the first 3DoF (the translational joints)
to qb = xh (Section 3.1), where xh is the target position
which we extract from the label. We find that this technique
leads to better performance and faster convergence than us-
ing the previous joint positions as bias (Section 3.1), which
we show in ablations in Section 4.5.
3.3. Motion Synthesis
We now introduce the motion synthesis module, which
is responsible for moving the object from an initial 6D pose
into a target 6D pose. It controls only the movement of the
wrist, i.e., the first 6DoF of the controllable hand model. In
this phase, both the grasping policy described in Section 3.2
and the motion synthesis module are executed concurrently.
5
be
T
=
xX
xX
T
= SS
ula
=
.
T,
SS
=
4
x
x
Ty
dis
gg
pa
T,
T,
gr=X—X
g
—
g
g
tio
=
g~
—g
gg
g
g


<!-- page 6 (ocr) -->
Models
Training set
Test set
Success↑
SimDist [mm/s]↓
Interp. [cm3]↓
Success↑
SimDist [mm/s]↓
Interp. [cm3]↓
DexYCB
MC
GT+PD
0.31
13.4 ± 9.2
4.59
0.35
13.1 ±9.1
4.41
GT+IK
0.39
11.8 ± 9.4
9.23
0.50
9.1 ± 8.5
9.74
Ours
0.70
5.8 ± 7.4
1.75
0.63
8.0 ± 8.1
1.77
SYN
Jiang et. al [20]+PD
0.25
12.4 ± 6.4
4.92
0.24
12.7 ± 6.5
4.94
Ours
0.75
3.9 ± 7.2
2.84
0.73
4.6 ± 6.7
2.81
HO3D
SYN
Jiang et. al [20]+PD
0.31
10.0 ± 6.6
5.21
0.30
10.6 ± 6.8
5.40
Ours
0.73
4.4 ± 7.4
3.33
0.71
4.9 ± 6.6
3.40
IMG
Grady et. al [13]+PD
0.67
5.1 ± 6.1
14.94
0.60
6.5 ± 5.8
14.00
Ours
0.88
1.4 ± 3.4
2.67
0.81
1.9 ± 3.6
2.08
Table 1. Static grasp evaluation. We compare our model with grasp samples from the DexYCB dataset (MC), generated samples by a
grasp synthesis method on the DexYCB and HO3D object sets (SYN), and samples extracted from an image-based hand pose estimator
(IMG). We evaluate the baseline grasps in the simulation via PD-control (*+PD) directly or after de-noising via inverse kinematics (*+IK)
for the motion capture data. We observe that our method outperforms the baselines in all metrics and conditions. The results indicate that
static grasp references 1) will not lead to stable grasps when evaluated in a physics simulation and 2) suffer from interpenetration. Our
method improves the interpenetration and learn stable grasps in a dynamic setting.
While the grasping policy maintains a stable grasp, the mo-
tion synthesis module takes over the control of the 6D pose
of the hand. Similar to the grasping policy, we propose a
feature extraction layer that incentivizes the model to move
the hand to a target pose with the object in-hand.
To control the global hand motion, we estimate a 6D tar-
get pose for the hand:
h = ψ(s, Tg, D). In particular,
we estimate the global target hand pose
h by computing
the distance between the object’s curren
D pose To and
the target 6D pose To. We then translate and rotate the
hand according to the displacement using closed-loop con-
trol. Hence, the displacement is recomputed after every ac-
tion. For more details, please refer to supp. material.
4. Experiments
We conduct several experiments to analyse the perfor-
mance of our method. We first introduce the data and ex-
perimental details in Sections 4.1 and 4.2. Next, we show
that our method can learn stable grasps and correct imper-
fect labels in Section 4.3. Lastly, we evaluate the motion
synthesis task and provide ablations to highlight the impor-
tance of our method’s components in Sections 4.4 and 4.5.
4.1. Data
DexYCB
We make use of the DexYCB dataset [5]. The
dataset consists of 1000 sequences of object grasping, with
10 different subjects and 20 YCB objects [3]. We filter out
all left handed sequences and create a random 75%/25%
train/test-split over all sequences and subjects. The data se-
quence contains 6D global poses for the hand and objects in
the camera frame and the local joint angles, hence providing
sequences of
(qh, Th, To)
T
t=1. The data also includes
meshes for the hand and objects, and the camera parame-
ters. We determine the grasp label based on the object’s dis-
placement with regards to its initial position. The time-step
with an object displacement greater than a pre-determined
threshold is chosen to be the target grasp D. Furthermore,
we use a recent state-of-the-art grasp synthesis method [20]
to generate grasp labels for all the objects in DexYCB and
create a 400/200 label train/test-split.
HO3D
We use generated grasp labels from static grasp
synthesis [20] or from an image-based pose estimator after
offline optimization [13] for the HO3D objects. We create
a train/test-split that is proportional to the DexYCB split,
which results in a 200/100 label train/test-split.
4.2. Experimental Details
We train policies by using our implementation of the
PPO algorithm [37] and run simulations in RaiSim [19]. For
each sequence, we initialize the environment with an object
and a grasp label. The hand is initialized with a pose from
earlier steps at a pre-determined distance from the object.
First, we train the grasping policy with all training labels
and objects. Then we continue with the motion synthesis
component given the pretrained grasping policy.
We evaluate physical plausibility of a grasp in terms of sta-
bility and interpenetration on a set of unseen grasp labels
and unseen objects. We define a set of complementary met-
rics to quantify performance extensively.
4.2.1
Metrics
Success Rate: We define the success rate as the primary
measure of physical plausibility. It is measured as the per-
centage of sequences which maintain a stable grasp, i.e.,
where the object does not slip for a period of time.
6
|
|
|
|
|
|
T
~
T
_
t6
{(—
1


<!-- page 7 (ocr) -->
(d) GraspTTA
(e) GraspTTA + IK
(f) Ours
Test
Test
(a) DexYCB GT
(b) DexYCB GT + IK
(c) Ours
t0
+0.5s
t0
+0.5s
(g) Input image
(i) ContactOpt
(h) Pose estimation
(j) Ours
Figure 4. Qualitative evaluation. (a)-(c): static grasp labels often
do not lead to stable grasps when evaluated in a physics simulation
(a-b), which can be successfully corrected by our method (c). For
an animated demonstration, please see the video in supp. material.
(d)-(f): showcases artifacts such as interpenetration when using a
state-of-the-art grasp synthesis method [20] (d-e). Our method (f)
can correct such cases and generate physically-plausible grasps.
(g)-(j): using images (g) to estimate an initial grasp (h). Phys-
ically implausible poses occur even with corrections via offline
optimization (i), which can be corrected by our method (j).
Interpenetration: We calculate the amount of hand vol-
ume that penetrates the object. We compute it using the
vertices of the MANO mesh [36] and the high-resolution
object meshes.
Simulated Distance: Similar to the metric proposed in
[20], we compute the mean displacement of the object. In-
stead of measuring the absolute displacement, we report the
mean displacement in mm per second.
Contact Ratio: For the ablation study, we measure the ra-
tio between the target contacts defined via the grasp label D
and the contacts achieved in the physics simulation.
MPE: The mean position error between the object’s posi-
tion and target 3D position (for motion synthesis).
Geodesic: The angular distance between the object’s cur-
rent and target orientation (for motion synthesis).
4.2.2
Baselines
*+PD: Similar to [20], we place the object into the hand via
the grasp label. We then attempt to maintain the grasp using
Models
Success ↑
SimDist [mm/s] ↓
Interpenetration [cm3]↓
GT+PD
0.30
13.7 ± 9.2
4.41
GT+IK
0.38
11.7 ± 9.4
9.08
Ours
0.56
9.0 ± 10.4
1.74
Table 2. Generalization. We evaluate generalization to unseen
objects and compare our model with the baselines. We create six
different test sets of three objects each, which we leave out during
training. We report the average performance over all test sets.
PD-control in the physics simulation.
*+IK: We employ an offline optimization to correct for im-
perfections (i.e., minor distances or penetrations) in the la-
bel. The improved samples are passed to the PD-control.
Flat-RL: We employ an RL baseline that does not separate
the grasping from the motion synthesis phase, but trains the
full dynamic grasp synthesis task end-to-end.
Ours+static grasp: In this variant, we use our grasping
policy for the grasping phase. During motion synthesis, we
use PD-control to maintain the pose while the grasping pol-
icy is frozen and not actively interacting with the object.
4.3. Grasping Objects
In this experiment, we show that our method can learn to
achieve stable grasps and that static grasp reference data is
inherently bound to fail in a dynamic setting. We first train
with labels from DexYCB [5] and further demonstrate that
our approach also works with, and improves upon, labels
obtained from state-of-the-art grasp synthesis method [20],
on both the DexYCB and HO3D object sets. Lastly, we
present results using an image-based hand pose estimator
on HO3D images and labels from ContactOpt [13].
We present quantitative evaluations in Tab. 1 and qual-
itative results in Fig. 4. Compared to the baselines, our
method is able to achieve significantly better performance
on all the metrics. Importantly, the grasping policy can im-
prove the success rate, while minimizing interpenetration
(an important metric in the grasp synthesis literature). We
note that our method achieves 0 interpenetration loss when
evaluated in the physics simulation. In Tab. 1, however, we
report interpenetration on the original MANO hand model
and detailed object meshes. For computational efficiency
during training, the hand model and the object meshes are
simplified in the physics simulation (Section 3.1), limiting
the performance of our model when evaluated in the orig-
inal setting with regards to interpenetration. We found no
improvement with IK for the generated (SYN) or image-
based (IMG) experiments and hence omit it from the results.
The improved performance in the image setup compared
to other settings is due to the high-quality grasp references
from [13], which already optimizes for contact. In general,
there is a performance drop when moving to unseen test la-
bels. We also find that our approach may struggle with thin
7Ch
RY
Y's”


<!-- page 8 (ocr) -->
Models
MPE [mm] ↓
Geodesic [rad.] ↓
Flat-RL
0.55
1.66
Ours+static grasp
0.45
1.46
Ours+learned policy
0.30
0.92
Ours
0.08
0.52
Table 3. Evaluation of motion synthesis. We compare our model
with a standard RL baseline (Flat-RL) and different variants of
our method. We observe that our hierarchical framework outper-
forms Flat-RL. Furthermore, an active grasping policy during mo-
tion synthesis is key to solving the task, as indicated by the perfor-
mance drop for Ours+static grasp.
objects which are difficult to grasp on a surface. For a de-
tailed analysis and failure cases, we refer to supp. material.
Generalization to Unseen Objects
To evaluate the gen-
eralization performance on unseen objects, we train and test
our model on six separate train/test splits with varying com-
plexity.
Each test set consists of three objects from the
DexYCB dataset. The remaining objects are used for train-
ing a policy. We average the results over all test sets and
report the results in Tab. 2. While there is room for im-
provement in overall success rate, our method outperforms
the baseline in all metrics. We provide a more detailed anal-
ysis in supp. material.
4.4. Motion Synthesis
We now demonstrate our method’s ability to synthesize
motions with the grasped object in hand. The goal of this
task is to grasp an object and generate a trajectory that
brings the object to a target 6D pose. We use a subset of
representative YCB objects and create a test set with 100
randomly sampled, out-of-distribution poses Tg. We com-
pare against a standard RL baseline (Flat-RL) and a vari-
ant of our method that only maintains the pose instead of
actively grasping the object (Ours+static grasp). We also
compare against a learning-based motion synthesis policy
(Ours+learned policy). As shown in Tab. 3, the hierarchi-
cal separation in our method is crucial for solving the task.
Moreover, the decrease in performance when the hand pose
is simply maintained (Ours+static grasp) solidifies the con-
tribution of our approach. This implies that active control of
the hand throughout the sequence is mandatory to maintain
a stable grasp. Lastly, our method outperforms the learning-
based variant (Ours+learned policy) of our motion synthesis
module by a large margin on both metrics.
4.5. Ablations
In this experiment, we analyze different components of
our method and show that they are crucial for achieving sta-
ble grasps. To this end, we ablate our method with differ-
ent feature spaces and reward functions. We select a sub-
set of representative objects and evaluate on our train-split
Models
Success ↑
SimDist [mm/s] ↓
Contact Ratio ↑
w/o ContactRew
0.0
24.18 ± 1.58
0.02
w/o GoalSpace
0.28
14.21 ± 10.50
0.18
w/o FeatLayer
0.47
9.69 ± 10.26
0.21
w/o WristGuidance
0.58
7.88 ± 10.57
0.28
Ours
0.89
4.83 ± 1.71
0.43
Table 4. Ablations. We ablate our proposed components. All
components together comprises our method. We observe that each
component increases the performance significantly in all metrics.
of DexYCB (Section 4.1). To validate our feature extrac-
tion layer and in particular the goal space (Section 3.2.1),
we compare to a variant of our approach using the origi-
nal state space (w/o FeatLayer) and a variant without the
goal space (w/o GoalSpace). Furthermore, we evaluate our
method without the contact reward (w/o ContactRew) and
without the proposed wrist-guidance (w/o WristGuidance)
as proposed in Section 3.2.3. Tab. 4 shows that each com-
ponent yields considerable performance improvement. We
emphasize that the contact reward and a suitable feature rep-
resentation are key for achieving stable grasps.
5. Discussion and Conclusion
In this work we have made several contributions. First,
we have introduced the task of dynamic grasp synthesis for
human-object interactions. To take a meaningful step into
this direction, we leverage a physics simulation to gener-
ate sequences of hand-object interactions that are natural
and physically plausible. We propose an RL-based solution
that learns from a single external grasp label. We demon-
strate that our method can learn stable grasps and gener-
ate motions with the object-in hand without slipping. Fur-
thermore, we have provided evidence that our method can
achieve generalization to unseen objects. While this proof
of concept experiment indicates that our method works if a
static hand pose reference for the unseen object is available,
the method could be scaled to even larger train/test sets in
the future. Finally, dynamics components such as friction
of surfaces, inertia, or the center of mass are assumed to be
known a priori, which is often not the case in real world
settings. Adding a perceptual component to estimate these
properties is a promising direction for future work.
Acknowledgements:
This
project has received funding from
the
European
Research
Council
(ERC) under the European Union’s
Horizon 2020 research and innovation programme grant agree-
ment No 717054. Muhammed Kocabas is supported by the Max
Planck ETH Center for Learning Systems.
We thank Marco
Bagatella, Manuel Kaufmann, Thomas Langerak, and Adrian
Spurr for the fruitful discussions and help throughout this project.
Lastly, we thank Alexis E. Block for the voice-over.
8a
———
|
|


<!-- page 9 (ocr) -->
[1] Samarth Brahmbhatt, Cusuh Ham, Charles C Kemp, and
James Hays.
Contactdb: Analyzing and predicting grasp
contact via thermal imaging.
In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 8709–8719, 2019. 2
[2] Samarth Brahmbhatt, Chengcheng Tang, Christopher D
Twigg, Charles C Kemp, and James Hays. Contactpose: A
dataset of grasps with object contact and hand pose. In Pro-
ceedings of the European Conference on Computer Vision
(ECCV), pages 361–378. Springer, 2020. 2
[3] Berk Calli, Arjun Singh, Aaron Walsman, Siddhartha Srini-
vasa, Pieter Abbeel, and Aaron M Dollar. The ycb object and
model set: Towards common benchmarks for manipulation
research. In International Conference on Advanced Robotics
(ICAR), 2015. 6, 14
[4] Zhe Cao, Ilija Radosavovic, Angjoo Kanazawa, and Jitendra
Malik. Reconstructing hand-object interactions in the wild.
In Proceedings of the IEEE/CVF International Conference
on Computer Vision (ICCV), pages 12417–12426, 2021. 2
[5] Yu-Wei Chao, Wei Yang, Yu Xiang, Pavlo Molchanov,
Ankur Handa, Jonathan Tremblay, Yashraj S. Narang, Karl
Van Wyk, Umar Iqbal, Stan Birchfield, Jan Kautz, and Dieter
Fox. DexYCB: A benchmark for capturing hand grasping
of objects. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition (CVPR), 2021. 1,
2, 4, 6, 7, 14, 15
[6] Tao Chen, Jie Xu, and Pulkit Agrawal. A simple method for
complex in-hand manipulation. In 5th Annual Conference on
Robot Learning (CoRL), 2021. 2, 16
[7] Sammy Christen, Lukas Jendele, Emre Aksan, and Otmar
Hilliges. Learning functionally decomposed hierarchies for
continuous control tasks with path planning. IEEE Robotics
and Automation Letters, 6(2):3623–3630, 2021. 11
[8] Sammy Christen, Stefan Stevˇsi´c, and Otmar Hilliges. Guided
deep reinforcement learning of control policies for dexter-
ous human-robot interaction. In 2019 International Confer-
ence on Robotics and Automation (ICRA), pages 2161–2167,
2019. 3
[9] Enric Corona, Albert Pumarola, Guillem Alenya, Francesc
Moreno-Noguer, and Gr´egory Rogez. Ganhand: Predicting
human grasp affordances in multi-object scenes. In Proceed-
ings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), pages 5031–5041, 2020. 2
[10] Bardia Doosti, Shujon Naha, Majid Mirbagheri, and David J
Crandall. Hope-net: A graph-based model for hand-object
pose estimation. In Proceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition (CVPR),
pages 6608–6617, 2020. 2
[11] Kiana Ehsani, Shubham Tulsiani, Saurabh Gupta, Ali
Farhadi, and Abhinav Gupta. Use the force, luke! learning
to predict physical forces by simulating effects. In Proceed-
ings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), 2020. 2, 3
[12] Guillermo Garcia-Hernando, Edward Johns, and Tae-Kyun
Kim. Physics-based dexterous manipulations with estimated
hand poses and residual reinforcement learning. In IEEE/RSJ
International Conference on Intelligent Robots and Systems
(IROS), pages 9561–9568. IEEE, 2020. 2, 3
[13] Patrick Grady, Chengcheng Tang, Christopher D Twigg,
Minh Vo, Samarth Brahmbhatt, and Charles C Kemp. Con-
tactopt: Optimizing contact to improve grasps. In Proceed-
ings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), pages 1471–1481, 2021. 2, 6,
7, 13, 14, 15, 18
[14] Shreyas Hampali, Mahdi Rad, Markus Oberweger, and Vin-
cent Lepetit. Honnotate: A method for 3d annotation of hand
and object poses. In Proceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition (CVPR),
2020. 1, 2, 4
[15] Yana Hasson, Bugra Tekin, Federica Bogo, Ivan Laptev,
Marc Pollefeys, and Cordelia Schmid. Leveraging photomet-
ric consistency over time for sparsely supervised hand-object
reconstruction. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR), pages
571–580, 2020. 1, 2
[16] Yana Hasson, Gul Varol, Dimitrios Tzionas, Igor Kale-
vatykh, Michael J Black, Ivan Laptev, and Cordelia Schmid.
Learning joint reconstruction of hands and manipulated ob-
jects. In Proceedings of the IEEE/CVF Conference on Com-
puter Vision and Pattern Recognition (CVPR), pages 11807–
11816, 2019. 1, 2
[17] Kaijen Hsiao and Tomas Lozano-Perez. Imitation learning of
whole-body grasps. In IEEE/RSJ international conference
on intelligent robots and systems, pages 5657–5662. IEEE,
2006. 3
[18] Wenlong Huang,
Igor Mordatch,
Pieter Abbeel,
and
Deepak Pathak. Generalization in dexterous manipulation
via geometry-aware multi-task learning.
arXiv preprint
arXiv:2111.03062, 2021. 2, 16
[19] Jemin Hwangbo, Joonho Lee, and Marco Hutter.
Per-
contact iteration method for solving contact dynamics. IEEE
Robotics and Automation Letters, 3(2):895–902, 2018. 6, 12
[20] Hanwen Jiang, Shaowei Liu, Jiashun Wang, and Xiaolong
Wang. Hand-object contact consistency reasoning for human
grasps generation. In Proceedings of the IEEE/CVF Interna-
tional Conference on Computer Vision (ICCV), 2021. 1, 2,
6, 7, 13, 14, 15, 17, 18
[21] Yifeng Jiang, Michelle Guo, Jiangshan Li, Ioannis Exarchos,
Jiajun Wu, and C Karen Liu. Dash: Modularized human ma-
nipulation simulation with vision and language for embod-
ied ai. In The ACM SIGGRAPH/Eurographics Symposium
on Computer Animation, pages 1–12, 2021. 3
[22] Korrawe Karunratanakul, Adrian Spurr, Zicong Fan, Otmar
Hilliges, and Siyu Tang. A skeleton-driven neural occupancy
representation for articulated hands. In International Confer-
ence on 3D Vision (3DV), 2021. 1, 2
[23] Korrawe
Karunratanakul,
Jinlong
Yang,
Yan
Zhang,
Michael J Black, Krikamol Muandet, and Siyu Tang. Grasp-
ing field:
Learning implicit representations for human
grasps.
In 2020 International Conference on 3D Vision
(3DV), pages 333–344. IEEE, 2020. 2
[24] Diederik P. Kingma and Jimmy Ba. Adam: A method for
stochastic optimization. In Yoshua Bengio and Yann LeCun,
editors, 3rd International Conference on Learning Represen-
tations (ICLR), 2015. 13
9


<!-- page 10 (ocr) -->
[25] Taein Kwon, Bugra Tekin, Jan St¨uhmer, Federica Bogo,
and Marc Pollefeys. H2o: Two hands manipulating objects
for first person interaction recognition. In Proceedings of
the IEEE/CVF International Conference on Computer Vision
(ICCV), pages 10138–10148, October 2021. 2
[26] Kailin Li, Lixin Yang, Xinyu Zhan, Jun Lv, Wenqiang Xu,
Jiefeng Li, and Cewu Lu. ArtiBoost: Boosting articulated
3d hand-object pose estimation via online exploration and
synthesis. In arXiv preprint arXiv:2109.05488, 2021. 1
[27] Shaowei Liu, Hanwen Jiang, Jiarui Xu, Sifei Liu, and Xi-
aolong Wang.
Semi-supervised 3d hand-object poses es-
timation with interactions in time.
In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 14687–14697, 2021. 2
[28] Zhengyi Luo, Ryo Hachiuma, Ye Yuan, and Kris Kitani.
Dynamics-regulated kinematic policy for egocentric pose es-
timation. In Advances in Neural Information Processing Sys-
tems, 2021. 3
[29] Priyanka Mandikal and Kristen Grauman. Dexvip: Learning
dexterous grasping with human hand pose priors from video.
In Conference on Robot Learning (CoRL), 2021. 3
[30] Priyanka Mandikal and Kristen Grauman.
Learning dex-
terous grasping with object-centric visual affordances.
In
IEEE International Conference on Robotics and Automation
(ICRA), 2021. 3
[31] Mariem Mezghanni, Malika Boulkenafed, Andre Lieutier,
and Maks Ovsjanikov. Physically-aware generative network
for 3d shape modeling.
In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition
(CVPR), pages 9330–9341, June 2021. 3
[32] OpenAI, Marcin Andrychowicz, Bowen Baker, Maciek
Chociej, Rafal J´ozefowicz, Bob McGrew, Jakub W. Pa-
chocki, Jakub Pachocki, Arthur Petron, Matthias Plappert,
Glenn Powell, Alex Ray, Jonas Schneider, Szymon Sidor,
Josh Tobin, Peter Welinder, Lilian Weng, and Wojciech
Zaremba. Learning dexterous in-hand manipulation. CoRR,
abs/1808.00177, 2018. 2
[33] Yuxzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang,
Ruihan Yang, Yang Fu, and Xiaolong Wang. Dexmv: Imita-
tion learning for dexterous manipulation from human videos.
arXiv preprint arXiv:2108.05877, 2021. 3
[34] Aravind Rajeswaran*, Vikash Kumar*, Abhishek Gupta,
Giulia Vezzani, John Schulman, Emanuel Todorov, and
Sergey Levine. Learning Complex Dexterous Manipulation
with Deep Reinforcement Learning and Demonstrations. In
Proceedings of Robotics: Science and Systems (RSS), 2018.
2, 3
[35] Davis Rempe, Leonidas J. Guibas, Aaron Hertzmann, Bryan
Russell, Ruben Villegas, and Jimei Yang. Contact and hu-
man dynamics from monocular video. In Proceedings of the
European Conference on Computer Vision (ECCV), 2020. 3
[36] Javier Romero, Dimitrios Tzionas, and Michael J. Black.
Embodied hands: Modeling and capturing hands and bod-
ies together. ACM Transactions on Graphics (ToG), 36(6),
Nov. 2017. 4, 7, 13
[37] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Rad-
ford, and Oleg Klimov. Proximal policy optimization algo-
rithms. arXiv preprint arXiv:1707.06347, 2017. 6, 12
[38] Soshi Shimada, Vladislav Golyanik, Weipeng Xu, Patrick
P´erez, and Christian Theobalt. Neural monocular 3d human
motion capture with physical awareness. ACM Transactions
on Graphics (ToG), 40(4), July 2021. 3
[39] Soshi Shimada, Vladislav Golyanik, Weipeng Xu, and Chris-
tian Theobalt. Physcap: Physically plausible monocular 3d
motion capture in real time. ACM Transactions on Graphics
(ToG), 39(6), dec 2020. 3
[40] Adrian Spurr, Umar Iqbal, Pavlo Molchanov, Otmar Hilliges,
and Jan Kautz. Weakly supervised 3d hand pose estimation
via biomechanical constraints. In Proceedings of the Euro-
pean Conference on Computer Vision (ECCV), pages 211–
228. Springer, 2020. 12
[41] Omid Taheri, Nima Ghorbani, Michael J. Black, and Dim-
itrios Tzionas.
GRAB: A dataset of whole-body human
grasping of objects. In Proceedings of the European Con-
ference on Computer Vision (ECCV), 2020. 1, 2
[42] Bugra Tekin, Federica Bogo, and Marc Pollefeys.
H+ o:
Unified egocentric recognition of 3d hand-object poses and
interactions. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR), pages
4511–4520, 2019. 1, 2
[43] Lixin Yang, Xinyu Zhan, Kailin Li, Wenqiang Xu, Jiefeng
Li, and Cewu Lu. Cpf: Learning a contact potential field
to model the hand-object interaction.
In Proceedings of
the IEEE/CVF International Conference on Computer Vision
(ICCV), pages 11097–11106, 2021. 2
[44] Yuting Ye and C Karen Liu. Synthesis of detailed hand ma-
nipulations using contact sampling. ACM Transactions on
Graphics (ToG), 31(4):1–10, 2012. 2
[45] Ye Yuan, Shih-En Wei, Tomas Simon, Kris Kitani, and Jason
Saragih. Simpoe: Simulated character control for 3d human
pose estimation. In Proceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition (CVPR),
pages 7159–7169, June 2021. 3, 12
[46] He Zhang, Yuting Ye, Takaaki Shiratori, and Taku Ko-
mura. Manipnet: Neural manipulation synthesis with a hand-
object spatial representation. ACM Transactions on Graphics
(ToG), 40(4), July 2021. 2, 4
[47] Tianqiang Zhu, Rina Wu, Xiangbo Lin, and Yi Sun. Toward
human-like grasp: Dexterous grasping via semantic repre-
sentation of object-hand. In Proceedings of the IEEE/CVF
International Conference on Computer Vision (ICCV), pages
15741–15751, 2021. 2
10


<!-- page 11 (ocr) -->
D-Grasp: Physically Plausible Dynamic Grasp Synthesis
for Hand-Object Interactions
Supplementary Material
The supplementary material of this paper includes a
video and this document. We provide more detailed de-
scriptions of our method in Section A and implementa-
tion details (physics simulation, baselines, metrics, and the
learning algorithm) in Section B. Furthermore, we present
additional qualitative results, as well as more detailed quan-
titative results in Section C. Lastly, we discuss potential so-
cietal impacts in Section D and provide a glossary for the
notations used in this paper in Section E.
A. Method Details
We presented our method in Section 3.
Importantly,
we functionally separate the 6DoF global motion synthe-
sis module from the grasping policy. We achieve this by
explicitly separating the information flow in the feature ex-
traction layers φ(·) and ψ(·), similar to [7]. We show in
Section 4.4 that this enables solving the complex dynamic
grasp synthesis task. We now provide more details on the
feature extraction layers.
A.1. Grasping Feature Extraction Details
We detail our method’s grasping policy in Section 3.2. In
this section, we provide additional details on how we extract
the features of the goal space presented in Section 3.2.1.
Hence, we need to extract object-relative features from the
label D in order to be invariant to the object 6D pose during
the grasping phase. Since collisions with the object occur
when learning a grasp, it is crucial to have a representation
that is flexible with respect to the object’s pose, even when
its position changes. We therefore focus on explaining the
goal components G = [
x|
q|gc].
Relative target positions:
The term
x measures the 3D
distances between the hand’s current a
the target joint 3D
positions xh and xh, respectively. Hence, to get the 3D
target positions xh, we utilize the label’s information about
the (global) 6D poses of the object To and the hand Th, as
well as the target joint configuration qh. Specifically, we
use forward kinematics to compute the global target pose
of the hand, which we then convert into the object-relative
coordinate frame using To. This provides us with the 3D
target positions xh for all the joints. We then apply the same
procedure to the current state of the environment, using the
object’s current 6D pose To, the hand’s current 6D pose Th
and the hand’s current joint configuration qh. This gives us
the 3D joint positions of the current hand configuration xh
in the object-relative frame. Next, we measure the distance
between the current and target joint positions:
gx = xh −xh.
Our final step consists of transforming gx into wrist-relative
coordinates, finally providing us with
x.
Relative target rotations:
The term
q represents the
angular distances between the current
nd target rota-
tions for the joints and the wrist.
For the local joint
rotations, we can directly compute the distance between
the current joint rotations qh and the target joint rota-
tions qh.
For the orientation of the wrist, we follow
the abovementioned procedure to achieve invariance to
the object pose.
Hence, we convert the global 6D hand
target pose Th into an object-relative target pose using
To.
We apply the same conversion to the current 6D
hand pose Th using the object’s current 6D pose To. We
then compute the angular distance between the current
and target object-relative poses. Finally, we transform the
computed distance into wrist-relative frame for consistency.
Target
contacts:
The
contact
goal
vector
gc
=
(gc, If,gc>0) is the concatenation of two vectors, namely
the desired contacts gc and the term Igc>0. To get the de-
sired contacts for each hand joint from the grasp label, we
measure the distance between all of a joint’s vertices of the
created meshes (Section 3.1) and all the vertices of the ob-
ject mesh, which can be computed from the grasp label D.
Hence, for each joint j, the desired contacts are then deter-
mined as follows:
gc,j = I
I
i=1
O
o=1
I[∥vi −vo∥2 < ϵ] > 0 .
(9)
If the distance between any vertex vi of a joint j and an
object vertex vo is below a small threshold ϵ (in our case
0.015m), we determine that the finger part should be in con-
tact and hence the contact label should be equal to 1, other-
wise 0.
The component Igc>0 is a one-hot encoding vector indicat-
ing which of the desired contacts gc are active. Please note
the redundancy in gc, which may be further improved in
future work.
11
g
g
gg
-
-
)
}
Ix oC
|


<!-- page 12 (ocr) -->
A.2. Motion Synthesis
Ours
As described in Section 3.3, we use a closed-loop
control scheme to move the hand from its current 6D pose
Th to the estimated hand pose
h. In particular, we com-
pute the distance between the c
rent and estimated target
6D object pose ∆
h = (
o −To). This term is then added
to the current 6D
se of
e hand and weighted by a factor
β:
Tpd = Th + β∆
h.
(10)
The term Tpd is then sent to the PD-controller of the sim-
ulation. The output of the PD-controller are torques that
generate a motion to guide the hand to the estimated target
pose
h by recomputing ∆
h after each simulation up-
date.
ote that in the motio
ynthesis phase, this module
replaces the control of the first 6DoF of the grasping policy.
Ours+Learned Policy
For the learned variant of the
motion synthesis module, we propose a feature layer
ψ(s, Tg, D) and a motion policy πm(am|ψ(s, Tg, D)). In-
tuitively, it is not necessary for the motion policy to know
about the proprioceptive information of the hand, such as
joint angles and angular velocities. Therefore, we only ex-
tract features which are relevant to the global control of the
6D hand pose Th. The feature extraction layer ψ(s, Tg, D)
receives the state s and the 6D target pose Tg of the object.
The output of this layer is the following:
ψ(s, Tg, D)=(Th, ˙Th, To, ˙To, go,x, go,q),
(11)
where the first four terms include information about the 6D
poses and respective velocities of the hand and object. Cru-
cially, the features go,x and go,q entail information about
the object’s current and target pose. The term go,x is the
Euclidean distance between the object’s current and target
position go,x = To,x −Tg,x in global coordinates. Sim-
ilarly, go,q computes the angular distance between the ob-
ject’s current and target pose go,q = To,q −Tg,q. For mo-
tion synthesis, we use the following reward function:
rm = αxrm,x + αqrm,q.
(12)
The position reward rm,x = empe measures the distance be-
tween the current and target object position (Eq. 13). The
angular reward is the geodesic distance between the object’s
current and target orientation rm,q = egeo (Eq. 14). We
weigh the two components with factors αx and αq.
In general, we propose a learning based variant because we
believe it could come in as a viable solution when the con-
trol of the global hand pose becomes more complex. In the
current work, we directly control the 6D pose of the hand.
In such a setting, an IK-based solution is expected to out-
perform a learning-based variant. In the future, one could
extend our method to include a biomechanical model of a
Figure 5. Physics Simulation. We create a controllable hand
model and deploy it in the RaiSim physics-engine [19] to provide
us with information about contacts and dynamics.
full arm. This would add inherent constraints to the hand
movements and hence increase the complexity of control-
ling the hand successfully. On the upside, this may lead to
more natural movements during the motion synthesis phase.
Hence, in such a setting a learning-based variant may out-
perform an IK-based solution.
B. Implementation Details
B.1. Physics Simulation
To train our method, we use a physics simulation as de-
scribed in Section 3.1.
We chose RaiSim [19], since it
allows modeling non-convex meshes and efficient parallel
training. We first create a controllable hand model (Fig. 5).
Similar to [45], we compute the argmax of the skinning
weights to assign each of the vertices to a body part. We
then group the vertices accordingly and create a mesh for
each body part. We limit the joint range in a data-driven
manner. Specifically, we estimate the joint limits by pars-
ing the DexYCB dataset and acquiring the maximum joint
range, similar to [40]. Since the data may not contain the
full range of possible joint displacements, we increase this
limit by a slack constant. In practice, we found that approx-
imating the collision bodies with primitive shapes (i.e., the
simple objects and the hand meshes) led to an order of mag-
nitude increase in training speed. This is because the sim-
ulation time increases roughly quadratically with the num-
ber of collision points. Therefore, for more complex ob-
ject meshes, we apply a decimation technique to reduce the
number of vertices (Fig. 6). For the simpler meshes, we
use primitive shapes and mesh alignment as an approxima-
tion. For training and evaluation, we therefore use the sim-
plified meshes (except for the interpenetration metric, see
Section B.3).
B.2. Learning Algorithm
We train policies by using our own implementation of
the widely used PPO algorithm [37]. We use the param-
eters summarized in Tab. 5 for training. We create a par-
allelized training scheme with a worker per grasp label for
12
T
a
iN
iN
ur
T
T
po
th
T
TT
N
ns


<!-- page 13 (ocr) -->
Figure 6. Mesh Decimation. We use mesh decimation to reduce
the number of vertices of the object mesh. On the left is the orig-
inal object mesh, on the right the decimated mesh. This helps to
speed up the physics simulation during training.
data gathering (amounting to e.g. 376 parallel environments
for DexYCB). We then train a single policy over all ob-
jects, containing all grasps from the training set. For the
GraspTTA [20] and ContactOpt [13] experiments, we dou-
ble the amount of workers, such that they roughly corre-
spond to the batch size of the DexYCB experiment (i.e.,
400 workers with 2 workers for each label). Each training
cycle utilizes a single GPU and 100 CPU cores and takes up
to 24-72 hours of training.
B.3. Metrics Details
This section contains an extended description of the met-
rics depicted in Section 4.2.1.
Success Rate: We define the success rate as the primary
measure of physical plausibility. It is measured as the rate
of sequences which maintain a stable grasp, i.e., where the
object does not slip and fall down for a period of a 5s win-
dow. We lower the surface in the simulation for this pur-
pose. A success rate of 0.0 indicates no success, 1.0 means
all sequences were successful.
Interpenetration: We calculate the amount of hand vol-
ume that penetrates the object. To do so, we use the origi-
nal MANO mesh [36] and the high-resolution object mesh.
Hence, there is no physical simulation involved when mea-
suring interpenetration. To ensure a fair comparison against
the static baseline, we choose the last time step of the grasp-
ing phase for our method and hence omit the approaching
phase from the evaluation.
Simulated Distance: Similar to the metric proposed in
[20], we compute the mean displacement between the ob-
ject and the hand’s wrist. Instead of measuring the abso-
lute displacement, we report the mean displacement in mm
per second. We measure the displacement for a maximum
window of 5s or stop whenever the object falls and hits the
surface.
Contact Ratio: For the ablation study, we measure the ratio
between the target contacts gc defined via the grasp label D
and the contacts achieved in the physics simulation I[f > 0].
Hyperparameters PPO
Value
Epochs
1e4
Steps per epoch
1.2e6
Environment steps for grasping
195
Environment steps for full task
300
Batch size
376
Updates per epoch
16
Simulation timestep
2.22e-3s
Simulation steps per action
13
Discount factor γ
0.996
GAE parameter λ
0.95
Clipping parameter
0.2
Max. gradient norm
0.5
Value loss coefficient
0.5
Entropy coefficient
0.0
Optimizer
Adam [24]
Learning rate
5e-4
Hidden units
128
Hidden layers
2
Weight Parameters
Value
wx
-2.0
wq
-0.1
wc
1.0
wreg,h
0.5
wreg,o
1.0
wx,j
1.0
wx,tip
4.0
λ
5.0
αx
-2.0
αq
-0.25
Table 5. Hyperparameters of our method. The parameter ”steps
per epoch” is reported for the DexYCB training set with a batch
size of 376. This number varies according on the amount of grasp
labels available in the training set.
We average over the whole sequence, therefore both the ap-
proaching and grasping phase are contained in this metric.
MPE: This metric is used for the motion synthesis experi-
ments. It is the mean position error between the object’s 3D
position and the object’s target 3D position, defined as go,x
(Section A.1):
empe = ∥go,x∥2
(13)
Geodesic: This is the angular metric used in the motion
synthesis experiments. In particular, the angular distance
between the object’s current orientation To,q and the ob-
ject’s target orientation Tg,q. It is defined as follows:
egeo = acos(0.5(trace(RoR⊤
g ) −1)),
(14)
where Ro and Rg are the rotation matrices of the corre-
sponding orientations of the object and the target 6D pose,
respectively.
13
rc


<!-- page 14 (ocr) -->
B.4. Baselines
Here we provide an extended description of the base-
lines.
*-PD: Similar to [20], we place the object into the hand
via the grasp label. We then attempt to maintain the grasp
using PD-control in the physics simulation. To do so, the
hand’s 6DoF global pose Th and the joint configuration qh
are initialized with the grasp label reference directly, hence
Th = Th and qh = qh.
*-IK: We employ an offline optimization to correct for
imperfections (i.e., minor distances or penetrations) in
the label by utilizing the information about the target
contacts gc (Section A.1) and the closest points on the
object surface. In particular, for the finger parts that we
deem to be in contact, we replace the original 3D keypoints
from the grasp label xh by the closest vertex points on
the object surface. We then run an optimization to yield a
corrected target pose. The reconstructed samples are then
passed to the PD-control. We found this technique to be
effective for motion capture data, but not for the labels from
GraspTTA [20] or ContactOpt [13], likely because both
methods already inherently optimize for contact. Hence,
we omit it for the latter methods in the main text.
Flat-RL: We employ an RL baseline that does not separate
the grasping from the motion synthesis phase, but trains the
full dynamic grasp synthesis task end-to-end. In particular,
this baseline uses the concatenation of the grasping policy’s
feature layer φ(s, D) (Section 3.2.1) and the feature layer
of the learned motion synthesis module ψ(s, Tg, D) (A.2).
Hence, the policy in this case is π(a|φ(s, D), ψ(s, Tg, D)).
For the reward function we use the combination of the
reward used for the grasping policy (Eq. 4 in main paper)
and the reward for the decoupled motion synthesis policy
(Eq. 12). The weights of the different reward components
are reported in Tab. 5.
B.5. Experimental Details
Here we provide a short overview of the different object
sets and grasp labels used in each experiment.
Grasping Objects
When using grasp predictions from an
external grasp synthesis method [20] (Section 4.3), we train
with the objects used in DexYCB [5]. During evaluation,
we report results on both the HO3D subset as done in [20]
and the objects from DexYCB. For the experiment with
ContactOpt [13], we train and test on the HO3D objects
(except for 019 pitcher base, which is not contained in the
dataset). Note that since the models for grasp synthesis and
the image-based pose estimates have no notion of physics in
terms of where an object is positioned in space (in contrast
to the data from DexYCB), we apply a small modification
to the simulation to ensure a fair comparison. We place the
object on a surface and allow the hand to approach from any
direction, even penetrating the surface. We achieve this by
disabling the collision response between the surface and the
hand. In future work, an optimization could filter out poses
that require approaching from beneath a surface. Also note
that since we only have access to a single grasp reference
and not a sequence for GraspTTA and ContactOpt, we start
each sequence at a predefined distance away from the object
in the mean MANO hand pose.
For the evaluation of our method in this experiment, we re-
move the surface (i.e. table) after the grasping phase. The
metrics are being measured from the moment the table is re-
moved. For the baselines, we directly start the sequence in
the target pose of both the hand and object (without a table
present).
Motion Synthesis
For the experiment presented in Sec-
tion 4.4, we included a representative subset of YCB [3] ob-
jects. Namely, we used 2 cylindric objects (002 master chef
can and 007 tuna can), 2 box-shaped objects (004 sugarbox
and 061 foam), and 2 more complex objects (019 pitcher
base and 052 extra large clamp) for training and evaluation.
We use our train-split of DexYCB in this experiment. Fur-
thermore, we filter out the failed grasps from the experi-
ment in Section 4.3 and train and evaluate only on the sta-
ble grasps. Using unsuccessful grasps in this case would
not produce any viable motions, since the objects cannot
be grasped correctly to initiate the motion synthesis phase.
Each sequence starts with the grasping phase, where only
the grasping policy πg is active. This ensures that a stable
grasp on the object can be reached before moving the object
globally. In the subsequent motion synthesis phase, both the
grasping policy and the motion synthesis module are acting
simultaneously.
Ablations
For the experiment presented in Section 4.5,
we use a subset of YCB [3] objects and train per-object poli-
cies with grasp labels extracted from DexYCB [5]. In par-
ticular, we included one cylindric object (002 master chef
can), one box-shaped object (004 sugarbox) and one com-
plex object (052 extra large clamp) for training and evalua-
tion.
C. Additional Results
All-Object vs. Per-Object Policies We experimented
both with a single policy trained over multiple objects and
single policies trained per object.
A comparison on the
DexYCB train/test-split is shown in Table 6. We observe
that the single object policies (Ours PO) can be trained
faster (i.e. ∼3000 vs. 10’000 epochs) and yield a better
overall performance on the training labels, likely due to
14


<!-- page 15 (ocr) -->
Models
Success ↑
SimDist [mm/s] ↓
Interpenetration ↓
Train
Ours PO
0.81
3.7 ± 5.8
1.94
Ours AO
0.7
5.8 ± 7.4
1.75
Test
Ours PO
0.42
12.4 ± 10.4
1.19
Ours AO
0.63
8.0 ± 8.1
1.77
Table 6. Policy Type Comparison. We compare a single policy
trained over multiple objects (Ours AO) and single policies trained
per object (Ours PO). We find that the all-object policies lead to
better generalization performance on the DexYCB dataset [5].
overfitting. On the other hand, the more general all-object
policies (Ours AO) take longer to train, however, the
generalization performance on unseen grasp labels is better.
The performance on the training data is lower compared
to the per-object policies.
This result indicates that an
all-object policy helps to prevent the policy from overfitting
to single grasp references.
Additional Qualitative Grasping Results We provide
additional qualitative results in Fig. 7.
Specifically, we
include examples on the training sets of DexYCB [5] and
the generated grasps [20]. Moreover, we present additional
examples for both test-sets.
As can be observed, our
method can correct for interpenetration and achieve more
realistic grasps.
Quantitative Grasping Result Details We present the
results of the empirical evaluation per object in Tables
7-12. It allows us to analyze the results in more detail. For
the grasp evaluation experiment (Section 4.3), we find that
the main difficulty for our learned policy are thin objects
which are hard to pick up from the surface, e.g., grasping
a pair of scissors from a table. This is indicated by the
relatively low success rates in Tables 7 and 8 for the ”037
scissors” and ”040 large marker” objects. Grasping these
objects requires very fine-grained finger motion or creating
a distinct motion to pick them up, which involves sliding
the object along the surface to overcome static friction. We
find that this issue is mitigated partially in the experiment
with generated grasp labels (Tables 9 and 10), because the
deactivated collisions of the hand with the surface (see
Section B.5) help to achieve stable grasps.
For the baselines, we occasionally observe a configuration
that leads to high success rates despite noisy pose refer-
ences.
Specifically, if the interpenetration is large (e.g.
GT-IK in Table 8 for ”021 bleach cleanser” or ”024 bowl”),
the objects can become entangled within the hand mesh and
will therefore not be able to fall down. Thus, the success
rate metric should always be interpreted in combination
with the other metrics.
For the experiment with HO3D images, we find that the
performance of our method is equally good across all
DexYCB+PD
DexYCB+IK
Ours
DexYCB GT
DexYCB GT+IK
Ours
GraspTTA
GraspTTA +IK
Ours
GraspTTA
GraspTTA +IK
Ours
Train
Test
Figure 7.
Additional Qualitative Grasps.
We provide addi-
tional qualitative examples of grasps.
Rows 1-2: Comparison
of the grasps on the training-sets of DexYCB [5] and the gener-
ated grasps from [20]. Rows 3-4: Comparison on the test-sets of
DexYCB [5] and the generated grasps from [20]. As shown, our
method produces more physically plausible grasps, i.e., with less
interpenetration and more realistic contacts than the baselines.
objects and conditions (Tables 11 and 12). This is likely
due to the high-quality reference grasps that are produced
by [13]. While our approach can correct interpenetration
and noisy poses to some degree, it is conditioned on the
reference pose, and hence performs best when provided
with grasp targets that roughly approximate a real human
(i.e., physically plausible) grasp on the object. We conclude
that especially for generalization to unseen objects, good
grasp references are important.
Generalization to Unseen Object Details In Table 13,
we report the detailed results of the generalization experi-
ment. We observe a large variance across the different ob-
ject sets. For example, the success rate of our method on
test set 1, which comprises easier geometries, reaches up to
0.83. On the other hand, our method only achieves a 0.33
success rate on the test set 6, which contains the complex
objects ”037 scissors” and ”040 large marker”. Generally,
we find that our method is able to outperform the static base-
lines across the different test sets. As a future extension,
it would be interesting to scale the method to even larger
datasets. Such ambitions are supported by different works
15
EE—
5
5
8
Te


<!-- page 16 (ocr) -->
for dexterous robotic manipulation tasks [6,18], which have
recently demonstrated the ability of large scale training with
regards to object types in order to achieve generalization
across objects.
D. Societal Impact
While the dynamic grasps generated by our method are
not yet indistinguishable from real ones, we can extrapolate
to a more mature version of this work, opening-up many po-
tential applications, e.g., in AR/VR, HCI or robotics. These
applications may lead to negative societal impact, where
so-called deep-fakes are the obvious nefarious use of such
methods. However, it is also possible that due to the compu-
tational complexity and resulting real-world cost of imple-
menting even positive applications, there may be negative
implications for already underprivileged populations. For
example, a service robot that may learn to cooperate with
humans may not be affordable for many that have need for
such advanced care technologies.
In going forward with the development of technologies
related to this paper, one must carefully balance the poten-
tial positive uses and the undesired side-effects. Since we
have no control over whether such technologies will be de-
veloped at all, by whom and for which purposes, we ar-
gue that openly discussing the technical details, properties
and limitations is one way to ensure that a) such technolo-
gies are well understood and therefore counter measures
to nefarious use would be easier to implement and b) that
as many individuals as possible can have access to related
technologies. To this end we will release all source code for
research purposes.
E. Glossary
We include a glossary in Tables 14 and 15 to provide an
overview of the many notations used in this paper.
16


<!-- page 17 (ocr) -->
GT+PD
GT+IK
Ours
Object
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
002 master chef can
18.0 ± 9.8
0.19
5.68
17.2 ± 10.0
0.20
12.96
1.5 ± 5.7
0.90
1.54
003 cracker box
18.2 ± 10.1
0.16
3.62
9.2 ± 10.7
0.47
9.16
8.4 ± 12.3
0.68
2.48
004 sugar box
15.6 ± 11.2
0.32
5.52
8.7 ± 9.7
0.50
11.64
0.1 ± 0.0
1.00
3.28
005 tomato soup can
12.1 ± 10.8
0.28
4.34
12.2 ± 10.1
0.33
10.72
1.4 ± 5.5
0.90
2.51
006 mustard bottle
4.4 ± 7.8
0.64
9.51
1.1 ± 1.5
0.76
16.50
3.2 ± 8.5
0.88
2.20
007 tuna fish can
17.4 ± 9.4
0.14
2.52
16.6 ± 9.6
0.19
5.26
1.8 ± 4.6
0.71
1.13
008 pudding box
15.1 ± 9.7
0.21
3.91
13.2 ± 11.2
0.39
7.19
2.4 ± 5.9
0.78
0.98
009 gelatin box
18.9 ± 9.4
0.15
2.23
18.3 ± 9.3
0.20
4.61
3.7 ± 8.6
0.85
0.98
010 potted meat can
13.6 ± 10.3
0.30
4.14
11.4 ± 10.0
0.39
8.81
1.8 ± 6.0
0.89
0.64
011 banana
16.7 ± 8.6
0.09
3.27
15.9 ± 10.0
0.20
4.97
5.9 ± 9.6
0.47
0.73
019 pitcher base
11.0 ± 11.1
0.40
7.47
11.2 ± 11.2
0.37
17.01
6.9 ± 10.8
0.68
3.16
021 bleach cleanser
5.1 ± 8.5
0.61
8.25
3.8 ± 7.0
0.61
15.64
0.2 ± 0.4
0.94
3.08
024 bowl
10.2 ± 10.7
0.41
3.15
7.3 ± 9.3
0.62
9.83
7.5 ± 10.7
0.62
2.08
025 mug
12.3 ± 10.3
0.35
3.24
9.7 ± 10.6
0.53
6.56
10.2 ± 12.2
0.59
1.61
035 power drill
0.8 ± 1.8
0.83
10.68
5.3 ± 9.0
0.65
15.76
6.4 ± 10.7
0.59
1.64
036 wood block
13.4 ± 11.6
0.42
7.31
11.3 ± 11.5
0.50
13.36
0.1 ± 0.0
1.00
3.56
037 scissors
10.6 ± 9.9
0.35
1.72
13.5 ± 9.4
0.22
3.03
19.3 ± 10.0
0.11
0.35
040 large marker
19.8 ± 5.8
0.04
1.38
21.5 ± 5.9
0.05
2.81
20.9 ± 7.3
0.05
0.09
052 extra large clamp
15.0 ± 9.9
0.28
1.97
12.3 ± 11.0
0.44
3.50
10.4 ± 11.7
0.44
1.70
061 foam brick
18.9 ± 7.3
0.12
1.93
17.2 ± 10.5
0.26
5.23
3.5 ± 8.1
0.84
1.30
Average
13.4 ± 9.2
0.31
4.59
11.8 ± 9.4
0.39
9.23
5.8 ± 7.4
0.70
1.75
Table 7. Detailed results for the DexYCB train set.
GT+PD
GT+IK
Ours
Object
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
002 master chef can
20.4 ± 9.3
0.17
4.17
19.2 ± 8.6
0.17
10.73
0.6 ± 1.2
0.83
1.67
003 cracker box
14.7 ± 11.1
0.33
5.21
9.0 ± 11.5
0.67
13.10
8.9 ± 12.4
0.67
4.06
004 sugar box
14.1 ± 12.1
0.43
6.75
3.9 ± 8.5
0.86
16.04
3.9 ± 9.3
0.86
3.02
005 tomato soup can
7.6 ± 9.0
0.50
3.25
8.2 ± 8.4
0.25
7.56
14.4 ± 11.4
0.25
1.03
006 mustard bottle
9.5 ± 9.9
0.50
6.77
6.7 ± 9.9
0.63
13.19
7.0 ± 12.0
0.75
2.13
007 tuna fish can
16.4 ± 9.4
0.14
1.55
16.3 ± 8.5
0.14
3.55
0.1 ± 0.0
1.00
1.50
008 pudding box
18.5 ± 8.2
0.17
2.08
12.7 ± 10.5
0.33
4.19
4.2 ± 9.2
0.83
0.92
009 gelatin box
21.6 ± 9.7
0.14
2.00
15.3 ± 13.3
0.29
4.59
3.8 ± 8.5
0.71
0.86
010 potted meat can
9.9 ± 10.2
0.40
2.60
10.8 ± 10.8
0.40
7.00
0.1 ± 0.1
1.00
1.00
011 banana
13.8 ± 9.9
0.14
2.79
13.0 ± 10.8
0.29
4.36
10.8 ± 12.0
0.43
0.50
019 pitcher base
12.6 ± 12.5
0.50
7.83
13.1 ± 12.7
0.50
25.54
6.2 ± 9.1
0.50
3.08
021 bleach cleanser
5.8 ± 8.3
0.40
10.43
5.1 ± 9.3
0.80
15.40
10.2 ± 12.3
0.60
2.10
024 bowl
9.3 ± 11.1
0.50
5.83
0.3 ± 0.3
1.00
13.44
12.0 ± 11.9
0.50
1.56
025 mug
7.4 ± 9.2
0.50
3.00
0.5 ± 0.5
1.00
9.13
4.1 ± 9.0
0.83
1.33
035 power drill
0.2 ± 0.1
1.00
8.25
0.5 ± 0.4
0.83
15.02
5.6 ± 10.4
0.67
2.71
036 wood block
20.6 ± 9.1
0.17
4.88
12.9 ± 12.4
0.50
11.73
0.2 ± 0.1
1.00
4.17
037 scissors
8.1 ± 9.9
0.50
4.44
6.4 ± 8.6
0.50
6.55
19.0 ± 8.1
0.13
0.58
040 large marker
18.7 ± 3.2
0.00
1.43
13.5 ± 8.7
0.20
3.58
24.2 ± 0.1
0.00
0.00
052 extra large clamp
16.2 ± 8.9
0.14
2.48
5.1 ± 7.7
0.43
5.21
14.0 ± 12.1
0.43
1.88
061 foam brick
16.0 ± 10.8
0.29
2.43
10.0 ± 8.3
0.13
4.86
10.5 ± 12.0
0.57
1.30
Average
13.1 ± 9.1
0.35
4.41
9.1 ± 8.5
0.50
9.74
8.0 ± 8.1
0.63
1.77
Table 8. Detailed results for the DexYCB test set.
Jiang et. al [20]+PD
Jiang et. al [20]+IK
Ours
Object
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
002 master chef can
24.0 ± 1.5
0.00
6.39
24.0 ± 1.6
0.00
16.19
2.6 ± 7.5
0.90
2.70
003 cracker box*
22.8 ± 2.4
0.00
6.97
22.8 ± 2.5
0.00
8.18
6.0 ± 10.3
0.70
5.80
004 sugar box*
14.7 ± 8.5
0.10
5.60
15.2 ± 8.7
0.10
10.45
1.4 ± 5.3
0.95
4.03
005 tomato soup can
14.8 ± 9.1
0.10
5.62
14.6 ± 9.0
0.10
11.51
3.8 ± 8.7
0.85
5.76
006 mustard bottle*
5.6 ± 7.2
0.30
5.66
5.2 ± 7.3
0.50
10.61
0.8 ± 2.8
0.95
5.14
007 tuna fish can
20.9 ± 1.7
0.00
2.88
21.4 ± 1.7
0.00
4.84
0.3 ± 0.5
0.90
2.03
008 pudding box
11.0 ± 10.3
0.10
4.92
10.9 ± 10.2
0.10
7.88
6.2 ± 10.1
0.70
0.91
009 gelatin box
14.1 ± 8.7
0.10
3.89
14.3 ± 9.2
0.10
8.38
1.7 ± 5.9
0.90
1.44
010 potted meat can*
20.4 ± 2.9
0.00
3.96
20.7 ± 2.8
0.00
6.89
7.1 ± 11.0
0.65
0.46
011 banana*
4.4 ± 6.1
0.30
3.52
6.1 ± 8.0
0.40
2.33
7.0 ± 9.4
0.45
3.18
019 pitcher base*
6.4 ± 8.4
0.50
8.11
7.1 ± 8.0
0.30
13.64
6.4 ± 10.1
0.65
1.56
021 bleach cleanser*
0.8 ± 1.9
0.90
5.76
0.5 ± 0.6
0.80
6.82
2.1 ± 6.4
0.90
4.89
024 bowl
5.5 ± 8.0
0.70
4.93
5.7 ± 8.3
0.70
3.24
5.2 ± 7.7
0.40
1.78
025 mug*
7.9 ± 9.4
0.50
4.32
8.2 ± 9.5
0.40
2.19
1.3 ± 5.2
0.95
4.78
035 power drill*
12.3 ± 12.0
0.20
5.84
12.1 ± 12.1
0.20
8.40
11.4 ± 11.5
0.20
1.27
036 wood block
22.0 ± 4.6
0.00
7.28
22.2 ± 4.2
0.00
5.06
2.6 ± 7.5
0.90
2.99
037 scissors*
5.0 ± 7.5
0.30
2.37
8.2 ± 8.5
0.30
1.50
0.7 ± 1.4
0.85
2.18
040 large marker
10.3 ± 9.6
0.40
1.86
10.1 ± 9.7
0.40
3.41
7.2 ± 9.6
0.55
0.92
052 extra large clamp
3.6 ± 5.9
0.40
4.97
3.6 ± 6.0
0.40
8.21
3.4 ± 7.2
0.65
3.37
061 foam brick
20.9 ± 1.8
0.00
3.46
21.3 ± 2.0
0.00
6.56
1.3 ± 5.1
0.95
1.66
Average
12.4 ± 6.4
0.25
4.92
12.7 ± 6.5
0.24
7.31
3.9 ± 7.2
0.75
2.84
Table 9. Detailed results for the DexYCB and HO3D train set with grasp references from a static grasp synthesis method [20]. HO3D
objects are marked by *.
17


<!-- page 18 (ocr) -->
Jiang et. al [20]+PD
Jiang et. al [20]+IK
Ours
Object
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
002 master chef can
24.0 ± 1.6
0.00
7.54
23.3 ± 1.3
0.00
7.03
5.3 ± 10.5
0.80
1.88
003 cracker box*
22.8 ± 2.5
0.00
6.73
20.3 ± 5.4
0.00
7.74
5.4 ± 10.6
0.80
7.06
004 sugar box*
15.2 ± 8.7
0.10
5.18
15.0 ± 8.4
0.00
13.85
0.2 ± 0.2
1.00
3.48
005 tomato soup can
14.6 ± 9.0
0.10
5.29
15.0 ± 9.0
0.00
10.75
0.1 ± 0.1
1.00
5.86
006 mustard bottle*
5.2 ± 7.3
0.50
5.19
7.6 ± 7.6
0.10
14.29
0.4 ± 0.9
0.90
6.23
007 tuna fish can
21.4 ± 1.7
0.00
2.61
19.8 ± 6.7
0.10
5.25
2.5 ± 7.0
0.90
1.51
008 pudding box
10.9 ± 10.2
0.10
5.51
7.0 ± 9.1
0.30
9.38
7.3 ± 10.7
0.60
0.46
009 gelatin box
14.3 ± 9.2
0.10
3.49
13.0 ± 10.6
0.40
6.91
0.8 ± 1.6
0.80
1.83
010 potted meat can*
20.7 ± 2.8
0.00
4.74
21.0 ± 2.6
0.00
8.70
7.6 ± 10.4
0.40
0.60
011 banana*
6.1 ± 8.0
0.40
3.38
8.1 ± 8.9
0.50
3.16
4.8 ± 9.1
0.80
2.09
019 pitcher base*
7.1 ± 8.0
0.30
8.50
6.3 ± 8.1
0.40
0.00
12.3 ± 11.9
0.40
0.98
021 bleach cleanser*
0.5 ± 0.6
0.80
6.50
9.9 ± 9.1
0.30
7.75
0.2 ± 0.2
1.00
5.69
024 bowl
5.7 ± 8.3
0.70
4.51
2.5 ± 5.1
0.80
2.83
3.4 ± 7.0
0.80
2.18
025 mug*
8.2 ± 9.5
0.40
5.94
3.7 ± 6.3
0.60
2.41
0.1 ± 0.0
1.00
4.64
035 power drill*
12.1 ± 12.1
0.20
4.91
14.7 ± 12.0
0.30
5.91
10.2 ± 11.4
0.20
1.49
036 wood block
22.2 ± 4.2
0.00
6.65
24.0 ± 2.0
0.00
1.94
10.7 ± 12.4
0.50
1.84
037 scissors*
8.2 ± 8.5
0.30
2.94
5.1 ± 7.1
0.50
1.26
7.8 ± 11.3
0.60
1.74
040 large marker
10.1 ± 9.7
0.40
1.65
6.8 ± 9.9
0.60
4.01
7.3 ± 10.4
0.50
1.94
052 extra large clamp
3.6 ± 6.0
0.40
4.09
3.1 ± 6.1
0.60
7.46
5.1 ± 8.4
0.60
3.22
061 foam brick
21.3 ± 2.0
0.00
3.51
20.9 ± 1.3
0.00
7.81
0.1 ± 0.0
1.00
1.46
Average
12.7 ± 6.5
0.24
4.94
12.4 ± 6.8
0.28
6.42
4.6 ± 6.7
0.73
2.81
Table 10. Detailed results for the DexYCB and HO3D test set with grasp references from a static grasp synthesis method [20]. HO3D
objects are marked by *.
Grady et. al [13]+PD
Ours
Object
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
003 cracker box
2.5 ± 6.7
0.85
14.33
0.3 ± 0.1
1.00
3.18
004 sugar box
16.3 ± 9.3
0.05
17.04
2.9 ± 6.6
0.70
2.40
006 mustard bottle
9.1 ± 9.7
0.40
26.46
0.3 ± 0.4
0.95
2.89
010 potted meat can
3.9 ± 8.5
0.70
15.42
2.2 ± 5.9
0.90
0.78
011 banana
10.0 ± 9.9
0.35
13.80
1.7 ± 4.9
0.80
1.98
021 bleach cleanser
0.9 ± 3.3
0.95
18.84
0.3 ± 0.1
1.00
2.86
025 mug
2.7 ± 6.7
0.80
5.49
2.0 ± 5.4
0.85
4.74
035 power drill
0.2 ± 0.4
0.95
16.09
0.3 ± 0.2
1.00
2.56
037 scissors
0.1 ± 0.1
1.00
6.96
3.0 ± 7.3
0.75
2.60
Average
5.1 ± 6.1
0.67
14.94
1.4 ± 3.4
0.88
2.67
Table 11. Detailed results for the train set with ContactOpt [13] on HO3D images.
Grady et. al [13]+PD
Ours
Object
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
003 cracker box
6.7 ± 9.7
0.60
13.41
0.26 ± 0.1
1.00
2.14
004 sugar box
23.6 ± 1.5
0.00
17.71
0.95 ± 2.2
0.90
2.53
006 mustard bottle
4.6 ± 7.6
0.60
25.16
0.64 ± 0.8
0.80
2.46
010 potted meat can
1.9 ± 5.5
0.90
14.08
0.63 ± 1.3
0.90
0.38
011 banana
12.0 ± 10.4
0.20
13.38
0.61 ± 0.5
0.80
1.91
021 bleach cleanser
0.9 ± 2.4
0.90
18.23
2.86 ± 7.6
0.90
2.25
025 mug
6.4 ± 8.4
0.50
4.80
5.05 ± 9.7
0.80
4.16
035 power drill
0.1 ± 0.1
1.00
14.84
0.71 ± 0.6
0.60
1.68
037 scissors
2.7 ± 6.9
0.70
4.34
5.30 ± 9.3
0.60
1.21
Average
6.5 ± 5.8
0.60
13.99
1.9 ± 3.57
0.81
2.08
Table 12. Detailed results for the test set with ContactOpt [13] on HO3D images.
18


<!-- page 19 (ocr) -->
GT+PD
GT+IK
Ours
Object
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
SimDist [mm/s] ↓
Success ↑
Interp. [cm3]
Test set 1
004 sugar box
15.2 ± 11.4
0.35
5.86
7.4 ± 9.4
0.60
12.87
2.3 ± 7.2
0.92
3.35
005 tomato soup can
11.4 ± 10.5
0.32
4.17
11.5 ± 9.8
0.32
10.21
5.7 ± 10.3
0.76
1.56
006 mustard bottle
6.0 ± 8.5
0.60
8.64
2.9 ± 4.2
0.72
15.44
2.1 ± 5.7
0.80
1.87
Average
10.9 ± 10.1
0.42
6.22
7.3 ± 7.8
0.55
12.84
3.3 ± 7.7
0.83
2.26
Test set 2
061 foam brick
18.1 ± 8.3
0.16
2.06
15.3 ± 9.9
0.23
5.13
9.6 ± 12.0
0.62
0.55
010 potted meat can
12.8 ± 10.2
0.33
3.80
11.3 ± 10.2
0.39
8.42
5.1 ± 9.3
0.61
1.36
052 extra large clamp
15.4 ± 9.6
0.24
2.11
10.3 ± 10.1
0.44
3.98
14.8 ± 11.5
0.16
1.53
Average
15.4 ± 9.4
0.24
2.66
12.3 ± 10.1
0.35
5.84
9.8 ± 10.9
0.46
1.15
Test set 3
003 cracker box
17.4 ± 10.3
0.20
4.00
9.1 ± 10.9
0.52
10.11
12.9 ± 13.3
0.52
2.86
007 tuna fish can
17.1 ± 9.4
0.14
2.28
16.5 ± 9.3
0.18
4.83
5.4 ± 10.2
0.79
0.88
011 banana
15.8 ± 9.0
0.11
3.11
14.9 ± 10.2
0.23
4.78
7.2 ± 10.3
0.50
1.24
Average
16.8 ± 9.6
0.15
3.13
13.5 ± 10.2
0.31
6.57
8.5 ± 11.3
0.60
1.66
Test set 4
002 master chef can
18.5 ± 9.7
0.19
5.33
17.6 ± 9.7
0.19
12.45
6.6 ± 11.1
0.65
1.21
036 wood block
15.1 ± 11.1
0.36
6.75
11.7 ± 11.7
0.50
12.98
3.4 ± 8.8
0.85
3.31
052 extra large clamp
15.4 ± 9.6
0.24
2.11
10.3 ± 10.1
0.44
3.98
15.1 ± 11.3
0.28
2.26
Average
16.3 ± 10.1
0.26
4.73
13.2 ± 10.5
0.38
9.80
8.4 ± 10.4
0.59
2.26
Test set 5
008 pudding box
16.0 ± 9.4
0.20
3.45
13.0 ± 11.0
0.38
6.44
3.5 ± 8.4
0.83
0.90
019 pitcher base
11.4 ± 11.4
0.42
7.56
11.6 ± 11.5
0.40
19.06
11.3 ± 11.5
0.40
3.52
035 power drill
0.6 ± 1.3
0.87
10.04
4.0 ± 6.8
0.70
15.57
11.0 ± 12.8
0.43
1.63
Average
9.3 ± 7.4
0.50
7.02
9.6 ± 9.8
0.49
13.69
8.6 ± 10.9
0.56
2.02
Test set 6
005 tomato soup can
11.4 ± 10.5
0.32
4.17
11.5 ± 9.8
0.32
10.21
9.1 ± 12.0
0.60
2.10
037 scissors
9.9 ± 9.9
0.39
2.55
11.3 ± 9.2
0.31
4.11
18.3 ± 10.4
0.19
0.71
040 large marker
19.6 ± 5.3
0.03
1.38
20.0 ± 6.4
0.07
2.95
18.2 ± 10.2
0.19
0.51
Average
13.6 ± 8.6
0.25
2.70
14.3 ± 8.4
0.23
5.76
15.2 ± 10.9
0.33
1.11
Table 13. Generalization to Unseen Objects. We evaluate generalization to unseen objects and compare our model with the baselines.
We create six different test sets of three objects, which we leave out during training. We report the detailed results per test set in this table.
19


<!-- page 20 (ocr) -->
Notation
Meaning
s
state
a
action
πg
grasping policy
πm
motion synthesis policy
D
static grasp label
x
3D joint position
q
joint angles
T
6D pose
Th
6D global hand pose
˙Th
6D global hand velocities
To
6D object pose
˙To
6D object velocities
Tg
6D goal object pose
qh
hand joint angles
˙qh
hand joint angular velocities
Th
6D global hand pose in grasp label
To
6D global object pose in grasp label
qh
3D hand pose in grasp label
gc
target contacts
x
3D target joint position
f
contact forces
τ
joint torques
kp
PD-controller parameter
kd
PD-controller parameter
qref
reference joint angles
qb
bias joint angle term
φ(·)
feature extractor
transformation to wrist reference frame
o
6D object pose in wrist reference frame
o
6D object velocities in wrist reference frame
h
6D global hand velocities in wrist reference frame
z
vertical distance to surface where object rests
Table 14. Glossary (part 1) for the notation used in this paper.
Notation
Meaning
G
goals
x
3D distance between current and target joint positions
q
angular distance between current and target joint/wrist rotations
c
contact vector
go,x
3D distance between current and target object position
go,q
angular distance between current and target object rotation
r
total reward for grasping
rx
position reward
wx
position reward weight
rq
pose reward
wq
pose reward weight
rc
contact reward
wc
contact reward weight
λ
contact reward coefficient
mo
object’s mass
rreg
regularizing reward term
wreg,h
regularizing reward term hand weight
wreg,o
regularizing reward term object weight
rm
total reward motion synthesis
rm,x
position reward motion synthesis
rm,q
pose reward motion synthesis
αx
position reward weight motion synthesis
αq
pose reward weight motion synthesis
ψ(·)
feature extractor motion synthesis
h
estimated 6D target hand pose
pd
6D pose input to the PD-controller for motion synthesis
vh
hand mesh
vo
object mesh
Table 15. Glossary (part 2) for the notation used in this paper.
20
g
g
g
.
T
I.
T
T
%
i.
i_
x
