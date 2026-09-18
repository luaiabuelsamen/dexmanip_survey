<!-- page 1 (ocr) -->
DyDexHandover: Human-like Dynamic Dexterous Bimanual Handover using
RGB-only Perception
Haoran Zhou, Yangwei You, Shuaijun Wang
Abstract— Dynamic in-air handover is a fundamental chal-
lenge for dual-arm robots, requiring accurate perception, pre-
cise coordination, and natural motion. Prior methods often rely
on dynamics models, strong priors, or depth sensing, limiting
generalization and naturalness. We present DyDexHandover,
a novel framework that employs multi-agent reinforcement
learning to train an end-to-end RGB-based policy for bimanual
object throwing and catching. To achieve more human-like
behavior, the throwing policy is guided by a human-policy
regularization scheme, encouraging fluid and natural motion,
and enhancing the policy’s generalization capability. A dual-
arm simulation environment was built in Isaac Sim for ex-
perimental evaluation. DyDexHandover achieves nearly 99%
success on training objects and 75% on unseen objects, while
generating human-like throwing and catching behaviors. To our
knowledge, it is the first method to realize dual-arm in-air
handover using only raw RGB perception. Our project website
is available at https://sites.google.com/view/dydexhandover
I. INTRODUCTION
For humans, the ability to throw and catch with both
hands is an essential skill in daily life, significantly en-
hancing the efficiency of object transfer. Inspired by this,
bimanual robotic equipped with dexterous hands can emulate
human manipulation behaviors, facilitating the acquisition of
dexterous manipulation skills [1]–[3]. As shown in Fig. 1,
once robots possess the capability to perform bimanual
throwing and catching, they can not only improve the ef-
ficiency of transfer tasks but also extend their operational
workspace beyond their physical motion limits [4], [5]. More
importantly, object transfer via throwing effectively avoids
potential collisions that may occur during direct hand-to-
hand exchange, providing a contact-free and safer solution
for bimanual robotic collaboration.
At present, data-driven methods have been widely applied
to manipulation tasks [6]–[9]. However, most existing works
primarily focus on interactions with static objects, such as
grasping or transporting, while dynamic tasks like object
throwing and catching have received relatively little attention.
The main challenges of the throwing and catching task
include: (1) the high-dimensional action and observation
spaces, which increase the difficulty of learning robust poli-
cies; (2) the stringent requirements on response speed and
motion precision; and (3) the need for real-time hand–arm
and arm–arm coordination.
Due to the aforementioned limitations, it is difficult to
collect effective demonstrations to support training for im-
itation learning (IL). Existing RL-based works [10]–[13]
All authors are with Xiaomi Robotics.
Corresponding author: Shuaijun Wang, email:wukongwoong@gmail.com.
Fig. 1: We present DyDexHandover, a framework for dy-
namic bimanual handover, achieving human-like throwing
and catching using RGB-only perception.
rely on privileged information or observations containing
depth, such as RGBD or point clouds. On the other hand,
these works typically employ collaborative manipulators with
constrained joints, resulting in motions that are less natural
than human throwing and catching strategies. Inspired by
this, we directly employ a pre-trained visual encoder to
extract features from RGB images as observation inputs,
thereby further enhancing the policy’s generalization ability
to unseen objects. Moreover, since the throwing behavior
directly affects the predictability of the object’s trajectory
and the difficulty of catching it, employing a human-like
throwing strategy that propels the object along a higher-
curvature trajectory can enhance the overall task robustness,
which is of significant importance in throwing and catching
tasks. Considering this, we first collect a small number of
human throwing demonstrations to train a human policy,
which is then used to guide the agent’s throwing behavior
during training. By learning a human-like thrower, the policy
can achieve improved generalization and robustness.
In this work, we propose DyDexHandover, a novel frame-
work for learning human-like bimanual throwing and catch-
ing skill using multi-agent reinforcement learning. We con-
structed the training environment in Isaac Sim. The hu-
manoid robot has a dual-arm configuration, with each arm
having 7-DOFs and a 11-DOFs (6 active) dexterous hand
arXiv:2509.17350v2  [cs.RO]  25 Sep 2025
A


<!-- page 2 (ocr) -->
at the end. Both hands and arms will need to operate
collaboratively at the same time.
In summary, the main contributions of this study include:
1) Human-like throwing and catching skill. We leverage
a pretrained human policy as a regularization term to guide
and constrain the thrower’s learning, mitigate the lack of nat-
uralness in pure RL policies, and improve its generalization
for unseen objects.
2) End-to-end RGB-based policy training. We train
the policy with MAPPO algorithm, observing via a head-
mounted monocular RGB camera and using an attention-
based visual encoder for end-to-end training and deployment.
The policy achieves 99% success on 9 training objects and
75% on 9 unseen objects.
3) Dynamic bimanual cooperation on humanoid. We
enable a humanoid robot to perform human-like, uncon-
strained, and dynamic dual arm-hand cooperation in sim-
ulation.
II. RELATED WORK
A. Multi-Agent Reinforcement Learning
Multi-agent reinforcement learning (MARL) extends re-
inforcement learning (RL) to multi-agent systems, enhanc-
ing inter-agent cooperation, and improving generalization in
unstructured environments [4]. Multi-Agent Proximal Policy
Optimization (MAPPO) [14] further extends the stability and
efficiency of PPO to multi-agent settings, effectively ad-
dressing non-stationarity among agents through a centralized
training with decentralized execution (CTDE) architecture.
In the human brain, each arm is primarily controlled by
the contralateral motor cortex [15], while the corpus cal-
losum facilitates interhemispheric communication to achieve
highly coordinated bimanual movements [16]. Inspired by
this mechanism, a dual-arm robot can be modeled as a
two-agent multi-agent system. Similarly, Guohui Ding et al.
proposed a game-theoretic MARL algorithm that updates Q-
values based on Nash equilibrium in a bimatrix Q-game, ef-
fectively accomplishing dual-arm collaborative manipulation
tasks [17]. Likewise, Luyu Liu et al. combined Hindsight
Experience Replay (HER) with MADDPG and introduced
a “reward cooperation, penalize competition” mechanism
during training, which alleviated self-collision issues in bi-
manual coordination [18].
B. Bimanual Dexterous Manipulation
In recent years, with increasing attention on dexterous
manipulation, data-driven methods have become the main
approach used by researchers in this field, achieving high
success rates in tasks such as pick-place and in-hand manip-
ulation [19]–[22]. Similar to our approach, Rajeswaran et al.
[23] incorporated a small number of human demonstrations
into the RL process to guide policy learning, which not only
made the robot’s motions more natural but also improved the
robustness of the learned policy. However, for object throw-
ing and catching tasks, coordinated dual-arm manipulation is
required, which increases the dimensionality of both the ac-
tion and observation spaces and poses additional challenges
for policy learning. Some prior works have addressed dual-
hand dexterous manipulation tasks by combining RL and IL
[19], [24]. Unlike these approaches that rely on RGB-D or
point cloud observations, our method uses only RGB images
for perception, which simplifies the input representation and
reduces computational complexity, enabling efficient training
in simulation.
C. Dynamic Throwing and Catching
Compared to static manipulation tasks such as pick-and-
place, dynamic manipulation tasks involve more complex
environmental variations, such as throwing an object and
catching it [25]–[27]. These tasks require robots to quickly
perceive the state of objects, and adjust their actions in
real time. When the robot is required to perform throwing
and catching simultaneously, multi-arm coordination, motion
synchronization, and real-time adaptation to environmental
changes become key challenges [10]–[13], [28]. For dynamic
handover tasks, Yuanpei Chen et al. employed MARL al-
gorithms to achieve human-level performance in bimanual
collaboration under varying levels of difficulty [11]. To
enable policy deployment in the real world, Binghao Huang
et al. further integrated a trajectory prediction model to
estimate object landing points, successfully training dual-arm
robots to perform throwing and catching tasks [4]. These
works demonstrate that MARL can significantly enhance the
performance of bimanual cooperative manipulation. How-
ever, although these methods perform well during training,
they exhibit limited generalization to unseen objects. In our
work, we introduce a human policy regularization approach
to learn human-like strategies, thereby improving the policy’s
generalization capability.
III. METHOD
In the throwing and catching task, one hand is responsible
for throwing the object while the other hand is responsible
for catching it. Both hands share aligned objectives, forming
a fully cooperative relationship. Therefore, the humanoid
can be regarded as a multi-agent system composed of two
agents: the thrower and the catcher. As shown in Fig. 2,
we train and deploy policies under the CTDE architecture.
Each agent observes local information from the environment,
executes actions within its own action space, and receives
feedback through a shared reward. This modeling approach
facilitates the design of strategies that fully exploit dual-arm
cooperation, improving the overall efficiency and success rate
of the task.
A. Problem Definition
This work focuses on enabling object throwing and catch-
ing tasks on a humanoid robot equipped with dexterous hands
through MARL. To achieve this, we formulate the problem
as a Decentralized Partially Observable Markov decision
process (Dec-POMDP). And we model the Dec-POMDP for
this task, including the design of the action space, state space,
and reward function.


<!-- page 3 (ocr) -->
Fig. 2: Overview of the proposed framework. We employ the upper body of the M92C humanoid, which features 18-DOFs
(7 for the arm and 11 for the hand) on each side. Before RL training, human demonstrations collected via teleoperation are
used to pre-train the visual encoder and human policy (right). Subsequently, policies are trained with the MAPPO algorithm,
where the human policy is incorporated as a regularization term to guide the training process.
1) Action Space: Humans typically perform object throw-
ing and catching by controlling arm velocities in the joint
space. To mimic this behavior, we construct the action space
of both agents using joint quantities, denoted as:
Ai = (˙qi
d,arm, qi
d,hand), i ∈(throw, catch)
(1)
where the 7-DOFs of the arm are controlled via desired joint
velocities, denoted as ˙qi
d,arm ∈R7; while the 6 actuated
DOFs of the hand are controlled via desired joint positions,
denoted as qi
d,hand ∈R6.
2) State Space: In the CTDE framework, the critic re-
ceives the global state, while each policy only observes local
states. In our task, both agents observe the target throwing
position ptarget ∈R3, the joint positions qthrow, qcatch ∈R13
and the visual features f ∈R8 extracted from RGB images
I. The thrower requires the current visual features, while the
catcher requires the past trajectory, define as the temporal
features τf = {ft, ft−1, · · · , ft−5}, to implicitly capture
additional velocity-related features. Thus, the local state
spaces for the two agents are:
Othrow = {qthrow, ptarget, f},
(2)
Ocatch = {qcatch, ptarget, τf}.
(3)
Since the throwing and catching task involves highly
dynamic motions, the joint velocities ˙qthrow, ˙qcatch ∈R13
play a crucial role in policy learning. In addition, the object
position pobj ∈R3 and linear velocity vobj ∈R3 provide
complementary information. We can obtain this additional
privileged information from the simulation. The global state
space is defined as:
S = {Othrow, Ocatch, ˙qthrow, ˙qcatch, pobj, vobj}
(4)
3) Reward Design: Given the distances ltarget (object to
target), lobj (object to left palm), lhand (right palm to left
palm), a boolean fcontact indicating left-hand contact with the
object, the number of robot joints n, and the torque of the
joint τ. We design five types of reward terms:
Distance Reward. Encourage the robot to move the object
toward the target point:
Rdist = exp(−10 · ltarget).
(5)
Catching Reward. Encourages the left hand to get closer
to the object:
Robj = exp(−10 · lobj)
(6)
Contact Reward. Encourage the catcher to make contact
with the object:
Rcontact = I(fcontact) ,
(7)
Action Penalty. To encourage smooth and energy-efficient
control commands, we apply a penalty based on the instan-
taneous joint power:
Paction = −
n
j=1
(τj ˙qj)2,
(8)
T catch
mono-RGB
Joint Position
S
“\
Temporal Emb. Stack
| 4
A
re
Acatch
catch
fiEE
2 1
/
/
|
|
/
|
ne
nk
IRGBEmb A
~~
|
»
Jz throw
throw
|
OO
|
f a8
Encoder
pres Te
raw
{
Athrow
RGB Emb.
77
3
Joint Position
Human
4
| | -
| B oo
Target Goal
Demonstrations
>
a -
Obj Position
al
lo
Human Policy
=
-
a
|
0
jp
DR
.
oe
Human-Regu(®arized MAPPO
uman-regu»arize
Thrower
Catcher
J


<!-- page 4 (ocr) -->
Hand Proximity Penalty. To prevent the policy from
exploiting direct hand-to-hand transfers in the overlapping
workspace, we penalize configurations where the two hands
are too close:
Phand = −exp(−10 · lhand).
(9)
Overall Reward. The final reward is a weighted sum of
the above terms:
R = 4Rdist + 0.5Robj + Rcontact + 0.0001Paction + Phand (10)
Algorithm 1 Human-Regularized MAPPO
1: Initialize parameters θi for policy πi and σi for critic
V i, i ∈(throw, catch)
2: Set hyperparameters as specified in Table I, maximum
steps Lmax, sampling steps Tmax
3: while iteration< Lmax do
4:
// 1. Interact in environments to collect data
5:
for t = 0 to Tmax do
6:
Obtain local observations oi
t.
7:
Each agent selects an action ai
t ∼π(oi
t)
8:
Obtain reward rt and next state st+1
9:
end for
10:
// 2. Calculate necessary information
11:
Read a segment of trajectory τ = {s, ai, r}
12:
Predict values vi = V i(s)
13:
Calculate hybrid advantages ˆAi = Ahybrid(s, snext, ai)
14:
D ∪{si, ai, vi, ˆAi}
15:
// 3. Optimize network parameters θi, σi
16:
for epoch = 1 to K do
17:
Shuffle the data in the experience buffer D
18:
for j = 0 to Tmax
B −1 do
19:
Randomly sample B mini-batches Dj
20:
Calculate and maximize J(θi) with Dj
21:
Update parameters θi and σi
22:
end for
23:
end for
24: end while
TABLE I: The Hyperparameters of Our Training Algorithm
Parameter
Value
Parameter
Value
Discount factor γ
0.995
PPO clip range ε
0.2
GAE parameter λ
0.95
Learning rate
1 × 10−4
FC layer dimension
512
Number of hidden layers
3
Activation function
elu
Max episode time
3(s)
Training epochs K
8
Batchsize B
4096
Decimation
2
Advantage weights β1, β2
0.01, 0.001
4) Failure Mechanism: To ensure stable training and
evaluation, the task episode is terminated once a failure
condition is met. Specifically, the following criteria are used:
• Object falling: The task is defined as failed once the
object’s vertical position falls below the predefined
threshold zobj < 0.1m.
• Deviation from goal: If the distance between the left
palm and the target goal exceeds 0.4 m, the task is
regarded as failed.
• Excessive proximity of the hands: Due to the partially
overlapping workspace of the robot’s two hands, we
reset the episode whenever the distance lhand < 0.1m to
prevent direct hand-to-hand object transfer.
• Unexpected contact: Any unintended arm contact with
the environment or self-collisions triggers a reset.
• Object out of view: If the object is no longer visible in
the camera image, the episode is terminated.
These conditions jointly define the failure mechanism of
the environment, preventing unstable behaviors and ensuring
meaningful policy learning.
B. Pre-traing with Human Demonstration
To collect human demonstrations, we teleoperate the right
arm in simulation to throw objects toward the left arm,
and recording the states (Athrow, qthrow, ptarget, pobj, I) into a
dataset. The collected data is then used to train the human
policy and the visual encoder.
1) Pretrained Vision Encoder: We use a pre-trained
CBAM-based ResNet [29] as the vision backbone, as shown
in Fig. 2, where the Convolutional Block Attention Module
(CBAM) is incorporated to enhance feature representation
of objects in the image, and it is then connected to a two-
layer MLP. The visual encoder takes RGB images I from
the head-mounted camera as input and outputs embeddings
f ∈R8. These embeddings are then concatenated with
processed proprioceptive information, serve as input to the
policy.
To improve the encoder’s performance in this task, we
trained it on the collected dataset using the Adam optimizer
with a learning rate of 1×10−4. The encoder maps the output
embeddings into a 3-dimensional space via a linear layer to
match the supervision labels. To accurately capture object
geometry and spatial features, we use the object’s area ratio
δ and centroid (xc, yc) as labels, and define the loss as the
MSE loss:
L = ∥fo −fi∥2
2,
fi = (δ, xc, yc)
(11)
These labels are computed from segmentation masks: δ
is the ratio of object pixels to total pixels, and (xc, yc) is
obtained via the weighted average of mask coordinates.
2) Pretrained Human Policy: The human policy π∗takes
o∗= (qthrow, ptarget, pobj) as input, and outputs the action
a∗. We used a 3-layer MLP, and trained the network on
the collected dataset with MSE loss. The policy was trained
using the Adam optimizer with a learning rate of 1e-4. The
total number of training epochs was 10k.
C. Policy Training
When training the thrower and catcher using RL, the
thrower requires a significant amount of exploration in the
early stages of training, during which the catcher may
learn many ineffective behaviors, negatively affecting overall


<!-- page 5 (ocr) -->
training success. Therefore, optimizing the throwing strategy
is crucial for improving training efficiency and policy per-
formance. To improve convergence and training stability, we
implement two components: (1) human policy regularization;
(2) hybrid advantage estimation. The training procedure is
summarized in Algorithm 1.
1) Human Policy Regularization:
To encourage the
throwing policy to approximate human behavior, we em-
ploy the Kullback–Leibler (KL) divergence to measure the
discrepancy between the human policy distribution and the
thrower’s policy distribution, and incorporate this discrep-
ancy as a regularization term in the training objective of
the thrower. Since we adopt a stochastic policy, each policy
outputs a probability distribution modeled as a Gaussian
distribution π ∼N(µ, σ2). The KL divergence between the
two distributions can be expressed as:
DKL π∗∥πthrow = Eathrow∈Athrow log
π∗(a∗| o∗)
πthrow(athrow | othrow)
= log σthrow
σ∗
+ σ∗2 + (µ∗−µthrow)2
2σthrow2
−1
2
(12)
After incorporating human policy regularization, the ob-
jective function of the throwing policy is given by:
J θthrow
= (1 −λreg )·J θthrow
−λreg ·DKL π∗∥πthrow
(13)
where λreg denotes the regularization weight, which balances
the degree of constraint imposed by the human policy on the
throwing policy. A larger λreg indicates stronger influence
from the human policy, leading the thrower’s behavior to
more closely align with that of the human.
2) Hybrid Advantage Estimation: In the MAPPO algo-
rithm, the advantage function directly influences the opti-
mization direction of the policy. To accelerate policy learn-
ing during the early training stage and to prevent loss of
exploration ability caused by local optima in later stages, we
propose a hybrid advantage estimation method, defined as:
Ahybrid(st, st+1, at) = AGAE(st, at)+β1AI(st, st+1)+β2AN
(14)
where AGAE(st, at) denotes the generalized advantage func-
tion in MAPPO, AI(st, st+1) represents the internal advan-
tage function introduced in [12], AN ∼N(0, 1) denotes the
Gaussian noise, β1 and β2 are the corresponding weighting
hyperparameters.
The introduction of internal advantage AI(st, st+1) =
min(V (st+1) −V (st), 0) enables the advantage function to
place greater emphasis on unfavorable situations, thereby
reducing the failure probability during the early training
stage.
In MAPPO, the partial observability of agents and the non-
stationarity of the environment exacerbate the estimation bias
of the advantage, which can easily lead to policy overfitting.
By applying noise AN into the advantage estimation, the
exploration capability of the policies can be enhanced [30].
IV. EXPERIMENTS
To validate the effectiveness of the proposed approach,
we conduct experiments in simulation related to policy
learning and deployment. The evaluation focuses on: (1) the
effectiveness and generalization of DyDexHandover; (2) the
impact of different components within the framework; and
(3) the effect of varying levels of human policy regularization
on task performance.
TABLE II: Randomization Parameters.
Group
Parameter
Distribution
Operation
Object
Mass
∼µ(0.3, 0.5)
Sampling
Color
∼µ(RGB 0–1)
Sampling
Robot
Joint Stiffness
∼µ(0.75, 1.5)
Scaling
Joint Damping
∼µ(0.75, 1.5)
Scaling
Restitution
∼µ(-0.04, 0.04)
Additive
Friction
∼µ(-0.04, 0.04)
Additive
Observation
Noise
∼N(0.0, 0.02)
Additive
Bias
∼N(0.0, 0.001)
Additive
Action
Noise
∼N(0.0, 0.002)
Additive
Bias
∼N(0.0, 0.0001)
Additive
Environment
Background
p = 0.3, N(0, 1)
Additive
Fig. 3: Object sets used in the experiments. (a) Training
objects, (b) Unseen objects.
A. Experimental Details
In this work, we build a simulated environment for the
throwing and catching task based on the NVIDIA Isaac Lab
framework [31], including the upper body of the M92C-
series humanoid robot and the objects used for throwing
and catching. A monocular RGB camera is mounted on the
robot’s head. During training, each environment randomly
samples objects from the training set, as shown in Fig. 3.
The hardware used in the experiments are as follows: Intel
i9-13900K CPU and NVIDIA GeForce RTX 4090 GPU. The
physics simulator runs at 120 Hz, with both agents controlled
at 60 Hz. To enhance the robustness of the policy, we apply
domain randomization during training, as indicated in Table
II.
To evaluate the performance of the policies, we consider
several metrics as follow:
1) Hit Rate. This metric is defined as the proportion of
objects that successfully hit the hand palm of catcher.
2) Success Rate. This metric is defined as the proportion
of objects that are successfully caught by the catcher and
remain in hand until the end of the episode.
A
(a)
(b)
)
)
)
SEE
Tr


<!-- page 6 (ocr) -->
Fig. 4: Visualization of the throwing and catching process from two perspectives.
TABLE III: Evaluation results on predefined metrics.
Training objects (9 objects)
Metric
Cone
Cube
Big Cube
Cuboid A
Cuboid B
Cuboid C
Sphere
Big Sphere
Cylinder
Avg.
Hit Rate
100%
100%
100%
100%
100%
100%
100%
100%
100%
100%
Success Rate
100%
99%
99%
99%
99%
99%
100%
98%
99%
99%
Unseen objects (9 objects)
Metric
Dex Cube
Chef Can
Sugar Box
Bottle
Fish Can
Meat Can
Long Cone
Capsule
Long Capsule
Avg.
Hit Rate
100%
93%
95%
98%
83%
100%
99%
98%
99%
92%
Success Rate
97%
69%
74%
40%
73%
48%
98%
92%
92%
75%
Fig. 5: Trajectories of various objects during evaluation.
B. Evaluation Results
After training, we evaluate the proposed method on both
the object set used during training and an unseen object
set. In the test environment, the trained policy is rolled out
for 1,000 episodes, with objects randomly sampled from the
corresponding set in each episode. The mean values of the
evaluation metrics are reported in Table III. For the training
objects, the method achieves an average success rate of 99%,
with 100% success rate on certain objects. Furthermore, for
the unseen objects, our method attains an average success
rate of approximately 75%. These results demonstrate that
the proposed method exhibits strong robustness and general-
ization capability, enabling successful throwing and catching
tasks with diverse objects.
Fig. 4 shows the complete throwing and catching process
of the humanoid from different viewpoints. It can be ob-
served that the robot performs both throwing and catching
in a human-like and natural manner. Fig. 5 provides a more
detailed view of the trajectories for different objects, all
exhibiting natural parabolic shapes. Notably, when the object
hits the catcher, the catcher carries the object along its
original trajectory for a short distance to prevent it from
bouncing away.
C. Ablation Study
We ablate the performance of the components introduced
in our framework. The success rates during training under
different settings are shown in Fig. 6, and the detailed eval-
uation results are summarized in Table V. We observe that
without human policy regularization, the training achieves a
higher success rate upon convergence than all other methods.
However, when tested on unseen objects, its success rate
drops significantly below that of ours. This indicates that,
Third View-
-
-
-
-
v
-
I.
i
|
!
!
\
First View
0.35
—
2D
0.30} 7 TON
z 0.25
j
Pa
N 0.20
i
NZ
0.15
A
y / J
0.10
/
oT
02-01
0.0
0.1
0.2
Y (m)
—— Capsule
—— Sphere
 --—-
Right palm
 ¥%
Goal
—— Cuboid
~~ —— Can
~~ Left palm
O
Impact point


<!-- page 7 (ocr) -->
TABLE IV: Different baselines on Bimanual Dexterous Dynamic Handover.
Algorithm
Obs type
Task type
Method
Train objects
Test objects
Success rate(Train/Test)
Bi-DexHands [11]
State
Abreast Catch
PPO/MAPPO/HAPPO
1
1
unknown
Dynamic Handover [4]
RGB-D
Underarm Catch
MAPPO
11
14
95%/37%
DexCatch [12]
Point Cloud
Abreast Catch
PPO
9
11
72.95%/77.89%
Bimanual Catch [28]
State
Bimanual Catch
HAPPO
15
15
unknown
DyDexHandover (Ours)
RGB
Abreast Catch
MAPPO
9
9
99%/75%
Fig. 6: Training curves of average success rate for the
ablation study. Each method was trained for 200k steps.
TABLE V: Ablation study on predefined metrics.
Training objects
Unseen objects
Hit rate
Success rate
Hit rate
Success rate
Open-Loop
40%
0%
X
X
w.o. Multi-Agent
89%
79%
78%
51%
w.o. Human-Reg.
100%
97%
65%
53%
w.o. Hybrid Adv.
100%
99%
86%
74%
Ours
100%
99%
92%
75%
without incorporating human policy regularization, the policy
tends to overfit the training objects and generates unnatural
actions, which in turn degrades its generalization capability.
The introduction of hybrid advantage can slightly improve
the convergence speed during the early stages of training
and enhance policy robustness. Notably, when MARL is
not employed (i.e., training directly with PPO), all metrics
are the lowest, demonstrating the effectiveness of MARL in
learning collaborative tasks. Moreover, compared to single-
agent reinforcement learning (SARL), MARL reduces the
dimensionality of each agent’s observation space, thereby
improving the agent’s robustness.
D. Regularization Coefficient Evaluation
To evaluate the effect of human policy regularization
strength on the agent, we test different regularization weights
λreg, with the results shown in Fig. 7. Without constraining
the thrower with the human policy (λreg = 0), the thrower’s
Fig. 7: Effect of the regularization weight λreg on task
performance. The main plot shows the success rate over
training steps, while the inset visualizes representative throw-
ing trajectories under different λreg values.
policy overfits to the training objects, attempting to maxi-
mize rewards through unnatural behaviors, and consequently
achieves the highest success rate across all λreg values. As
the strength of human policy regularization increases, the
policy’s exploration ability gradually decreases, leading to
lower training success rates. Therefore, we select λreg = 0.2
as the reference value used in the proposed framework. At
this value, the policy achieves a balance between constraint
and exploration, learning an improved strategy without de-
viating from the human policy.
E. Baselines Evaluation
We compare our proposed framework with several works
on bimanual dexterous dynamic handover tasks, as sum-
marized in Table IV. These works cover a wide range
of observation modalities, task settings, and algorithmic
choices. In contrast, our method relies solely on monocular
RGB inputs and trains a MAPPO policy to solve abreast
catch tasks across multiple object categories. It achieves
a success rate of 99% on training objects and 75% on
unseen objects, outperforming most methods in terms of
both accuracy and generalization. These results highlight the
effectiveness of our method in learning human-like throwing
and catching skills using RGB-based observations, while
maintaining robust performance across diverse objects.
1.0
1.0
A A AT
JAD
aA)
Wrarrvaonee de) AAT)
Ee A NRA AY
0.8
Ad
0.8
f
8
/
2
gos
Zo6
P
P
~03
8
4
£
Q
5
=
5
g
Noo
504
& 0.4
l
:
Trajectory
-0.2
0.0
0.2
0.2
— wo. Human-Regular
02
Y (m)
— Aeg=00
—— w.. Hybrid Advantage
—— Meg=02
—— w.0. Multi-Agent
— Aeg=04
— Ours
J
— Aeg=08
00025
50
75
100
125
150
175
200
0025
50
75
100
125
150
175
200
Training Steps (k)
Training Steps (k)


<!-- page 8 (ocr) -->
V. CONCLUSION AND FUTURE WORK
This work introduced DyDexHandover, the first end-to-
end RGB-based framework for dual-arm in-air handover. By
combining multi-agent reinforcement learning with human-
policy regularization, our approach enables robots to perform
fluid, human-like throwing and catching without relying on
explicit dynamics models or depth sensing. Experiments in
Isaac Sim show a 99% success rate on training objects
and 75% on unseen objects, underscoring the advantages of
human-inspired guidance for natural and adaptive dual-arm
coordination. These results highlight the promise of leverag-
ing human priors to achieve more robust, generalizable, and
human-like collaboration in high-dynamic robotic scenarios.
Considering the dynamic of the environment and the
discrepancies between simulation and the real world, these
instabilities may pose safety risks during actual deployment.
Future work will explore incorporating safety mechanisms
into the policy learning process and further enhancing policy
generalization to enable transfer to real robots.
REFERENCES
[1] Y. Shao and C. Xiao, “Bimanual grasp synthesis for dexterous robot
hands,” IEEE Robotics and Automation Letters, 2024.
[2] S. Wang, L. Sun, M. Li, P. Wang, F. Zha, W. Guo, and Q. Li, “Learning
an image-based visual servoing controller for object grasping,” Inter-
national Journal of Humanoid Robotics, vol. 21, no. 05, p. 2350033,
2024.
[3] B. Zhou, H. Yuan, Y. Fu, and Z. Lu, “Learning diverse bimanual
dexterous manipulation skills from human demonstrations,” arXiv
preprint arXiv:2410.02477, 2024.
[4] B. Huang, Y. Chen, T. Wang, Y. Qin, Y. Yang, N. Atanasov, and
X. Wang, “Dynamic handover: Throw and catch with bimanual hands,”
arXiv preprint arXiv:2309.05655, 2023.
[5] S. Wang, X. Wang, B. Zhan, S. Wang, and F. Zha, “A generic
control method of manipulator based on optimization,” in 2017 2nd
International Conference on Advanced Robotics and Mechatronics
(ICARM).
IEEE, 2017, pp. 486–491.
[6] S. Wang, L. Sun, F. Zha, W. Guo, and P. Wang, “Learning adaptive
reaching and pushing skills using contact information,” Frontiers in
Neurorobotics, vol. 17, p. 1271607, 2023.
[7] Y. Chen, C. Wang, Y. Yang, and C. K. Liu, “Object-centric
dexterous manipulation from human motion data,” arXiv preprint
arXiv:2411.04005, 2024.
[8] S. Wang, W. Hu, L. Sun, X. Wang, and Z. Li, “Learning adaptive
grasping from human demonstrations,” IEEE/ASME Transactions on
Mechatronics, vol. 27, no. 5, pp. 3865–3873, 2022.
[9] H. Zhou and X. Lin, “Intelligent redundant manipulation for long-
horizon operations with multiple goal-conditioned hierarchical learn-
ing,” Advanced Robotics, vol. 39, no. 6, pp. 291–304, 2025.
[10] J. Kober, K. Muelling, and J. Peters, “Learning throwing and catching
skills,” in 2012 IEEE/RSJ International Conference on Intelligent
Robots and Systems.
IEEE, 2012, pp. 5167–5168.
[11] Y. Chen, T. Wu, S. Wang, X. Feng, J. Jiang, Z. Lu, S. McAleer,
H. Dong, S.-C. Zhu, and Y. Yang, “Towards human-level bimanual
dexterous manipulation with reinforcement learning,” Advances in
Neural Information Processing Systems, vol. 35, pp. 5150–5163, 2022.
[12] F. Lan, S. Wang, Y. Zhang, H. Xu, O. Oseni, Z. Zhang, Y. Gao,
and T. Zhang, “Dexcatch: Learning to catch arbitrary objects with
dexterous hands,” arXiv preprint arXiv:2310.08809, 2023.
[13] W. Zhan and P. Chin, “Safe multi-agent reinforcement learning for
bimanual dexterous manipulation,” in 2024 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS).
IEEE, 2024,
pp. 12 420–12 427.
[14] C. Yu, A. Velu, E. Vinitsky, J. Gao, Y. Wang, A. Bayen, and
Y. Wu, “The surprising effectiveness of ppo in cooperative multi-agent
games,” Advances in neural information processing systems, vol. 35,
pp. 24 611–24 624, 2022.
[15] E. M. Gordon, R. J. Chauvin, A. N. Van, A. Rajesh, A. Nielsen,
D. J. Newbold, C. J. Lynch, N. A. Seider, S. R. Krimmel, K. M.
Scheidter et al., “A somato-cognitive action network alternates with
effector regions in motor cortex,” Nature, vol. 617, no. 7960, pp. 351–
359, 2023.
[16] P. Fitzpatrick, “The primary motor cortex: upper motor neurons that
initiate complex voluntary movements,” Neuroscience, vol. 2, 2001.
[17] G. Ding, J. J. Koh, K. Merckaert, B. Vanderborght, M. M. Nicotra,
C. Heckman, A. Roncone, and L. Chen, “Distributed reinforce-
ment learning for cooperative multi-robot object manipulation,” arXiv
preprint arXiv:2003.09540, 2020.
[18] L. Liu, Q. Liu, Y. Song, B. Pang, X. Yuan, and Q. Xu, “A collaborative
control method of dual-arm robots based on deep reinforcement
learning,” Applied Sciences, vol. 11, no. 4, p. 1816, 2021.
[19] T. Lin, K. Sachdev, L. Fan, J. Malik, and Y. Zhu, “Sim-to-real
reinforcement learning for vision-based dexterous manipulation on
humanoids,” arXiv preprint arXiv:2502.20396, 2025.
[20] Y. Qin, B. Huang, Z.-H. Yin, H. Su, and X. Wang, “Dexpoint: Gener-
alizable point cloud reinforcement learning for sim-to-real dexterous
manipulation,” in Conference on Robot Learning.
PMLR, 2023, pp.
594–605.
[21] Y.-H. Wu, J. Wang, and X. Wang, “Learning generalizable dexterous
manipulation from human grasp affordance,” in Conference on Robot
Learning.
PMLR, 2023, pp. 618–629.
[22] K. Van Wyk, A. Handa, V. Makoviychuk, Y. Guo, A. Allshire, and
N. D. Ratliff, “Geometric fabrics: a safe guiding medium for policy
learning,” in 2024 IEEE International Conference on Robotics and
Automation (ICRA).
IEEE, 2024, pp. 6537–6543.
[23] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman,
E. Todorov, and S. Levine, “Learning complex dexterous manipulation
with deep reinforcement learning and demonstrations,” arXiv preprint
arXiv:1709.10087, 2017.
[24] C. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and C. K. Liu,
“Dexcap: Scalable and portable mocap data collection system for
dexterous manipulation,” arXiv preprint arXiv:2403.07788, 2024.
[25] Y. Zhang, T. Liang, Z. Chen, Y. Ze, and H. Xu, “Catch it! learning
to catch in flight with mobile dexterous hands,” in 2025 IEEE
International Conference on Robotics and Automation (ICRA). IEEE,
2025, pp. 14 385–14 391.
[26] A. Zeng, S. Song, J. Lee, A. Rodriguez, and T. Funkhouser, “Tossing-
bot: Learning to throw arbitrary objects with residual physics,” IEEE
Transactions on Robotics, vol. 36, no. 4, pp. 1307–1319, 2020.
[27] L. Werner, F. Nan, P. Eyschen, F. A. Spinelli, H. Yang, and M. Hutter,
“Dynamic throwing with robotic material handling machines,” in 2024
IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS).
IEEE, 2024, pp. 98–104.
[28] T. Kim, Y. Yoon, and J. Kim, “Learning dexterous bimanual catch
skills through adversarial-cooperative heterogeneous-agent reinforce-
ment learning,” arXiv preprint arXiv:2502.11437, 2025.
[29] Y. Xiao, H. Yin, S.-H. Wang, and Y.-D. Zhang, “Trec: Transferred
resnet and cbam for detecting brain diseases,” Frontiers in Neuroin-
formatics, vol. 15, p. 781551, 2021.
[30] H. Zhang, Y. Du, S. Zhao, Y. Yuan, and Q. Gao, “Vn-maddpg:
A variable-noise-based multi-agent reinforcement learning algorithm
for autonomous vehicles at unsignalized intersections,” Electronics,
vol. 13, no. 16, p. 3180, 2024.
[31] M. Mittal, C. Yu, Q. Yu, J. Liu, N. Rudin, D. Hoeller, J. L. Yuan,
R. Singh, Y. Guo, H. Mazhar et al., “Orbit: A unified simulation
framework for interactive robot learning environments,” IEEE Robotics
and Automation Letters, vol. 8, no. 6, pp. 3740–3747, 2023.
