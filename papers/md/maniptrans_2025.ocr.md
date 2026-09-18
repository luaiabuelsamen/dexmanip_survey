<!-- page 1 (ocr) -->
MANIPTRANS: Efficient Dexterous Bimanual Manipulation Transfer
via Residual Learning
Kailin Li1 Puhao Li1,2 Tengyu Liu1 Yuyang Li1,3 Siyuan Huang1
1State Key Laboratory of General Artificial Intelligence, BIGAI
2Department of Automation, Tsinghua University
3Institute for Artificial Intelligence, Peking University
https://maniptrans.github.io
⊕
Figure 1. MANIPTRANS for Bimanual Dexterous Manipulations. Retargeting methods often struggle with transferring MoCap data to
physically plausible motions, while our MANIPTRANS efficiently produces task-compliant, physically accurate motions. It also general-
izes across embodiments like Inspire hands [3], Shadow hands [1], and articulated MANO hands [27, 96].
Abstract
Human hands play a central role in interacting, mo-
tivating increasing research in dexterous robotic manip-
ulation.
Data-driven embodied AI algorithms demand
precise, large-scale, human-like manipulation sequences,
which are challenging to obtain with conventional rein-
forcement learning or real-world teleoperation.
To ad-
dress this, we introduce MANIPTRANS, a novel two-stage
method for efficiently transferring human bimanual skills to
dexterous robotic hands in simulation. MANIPTRANS first
pre-trains a generalist trajectory imitator to mimic hand
motion, then fine-tunes a specific residual module under
interaction constraints, enabling efficient learning and ac-
curate execution of complex bimanual tasks. Experiments
show that MANIPTRANS surpasses state-of-the-art meth-
ods in success rate, fidelity, and efficiency.
Leveraging
MANIPTRANS, we transfer multiple hand-object datasets
to robotic hands, creating DEXMANIPNET, a large-scale
dataset featuring previously unexplored tasks like pen cap-
ping and bottle unscrewing. DEXMANIPNET comprises
3.3K episodes of robotic manipulation and is easily extensi-
ble, facilitating further policy training for dexterous hands
and enabling real-world deployments.
1. Introduction
Embodied AI (EAI) has advanced rapidly in recent years,
with increasing efforts to enable AI-driven embodiments
to interact with physical or virtual environments. Just as
human hands are pivotal for interaction, much research in
EAI focuses on dexterous robotic hand manipulation [4, 16–
22, 41, 46, 52, 58, 59, 63, 65, 66, 68, 70, 72, 75, 77, 81, 82,
104, 113, 115, 118, 130, 131]. Achieving human-like profi-
ciency in complex bimanual tasks holds significant research
value and is crucial for progress toward general AI.
Thus, the rapid acquisition of precise, large-scale, and
human-like dexterous manipulation sequences for data-
driven embodied agents training [11, 12, 25, 83, 133] be-
comes increasingly urgent.
Some studies use reinforce-
ment learning (RL) [54, 99] to explore and generate dex-
terous hand actions [27, 69, 77, 111, 121, 135, 136], while
others collect human-robot paired data through teleopera-
tion [26, 44, 45, 82, 103, 113, 128].
Both methods are
limited: traditional RL requires carefully designed, task-
specific reward functions [78, 135], restricting scalability
1
arXiv:2503.21860v1  [cs.RO]  27 Mar 2025
o~ 2%”
«®, 3
©
Uncap the jar
.
‘ _
.. MANIPTRANS & & 7
®
"a
ew 8,
bor -=
Residual
-
-
-
odule
Put offalcohollamp (two-step extinguishing)
@ieic= 0 2022s 30.3
>,
Les
Imitator
p
;
55.0
Sy
,
MoCap
Retargeting Fails
Roll Out Successfully in Simulation


<!-- page 2 (ocr) -->
and task complexity, while teleoperation is labor-intensive
and costly, yielding only embodiment-specific datasets.
A promising solution is to transfer human manipulation
actions to dexterous robotic hands in simulated environ-
ments via imitation learning [71, 80, 93, 112, 139]. This
approach offers several advantages. First, imitating human
manipulation trajectories creates naturalistic hand-object
interactions, enabling more fluid and human-like motions.
Second, abundant motion-capture (MoCap) datasets [10,
14, 32, 37, 39, 57, 62, 73, 74, 107, 119, 125, 134] and hand
pose estimation techniques [13, 43, 67, 87, 108, 120, 122–
124, 126] makes extracting operational knowledge from hu-
man demonstrations easily accessible [93, 102]. Third, sim-
ulations provide a cost-effective validation, offering a short-
cut to real-world robot deployment [41, 44, 51].
Yet, achieving precise and efficient transfer is non-trivial.
As shown in Fig. 1, morphological differences between hu-
man and robotic hands lead to direct pose retargeting sub-
optimal. Additionally, although MoCap data is relatively
accurate, error accumulation can still lead to critical fail-
ures during high-precision tasks. Moreover, bimanual ma-
nipulation introduces a high-dimensional action space, sig-
nificantly increasing the difficulty of efficient policy learn-
ing. Consequently, most pioneering work generally stops at
single-hand grasping and lifting tasks [27, 111, 121, 135],
leaving complex bimanual activities—such as unscrewing a
bottle or capping a pen—largely unexplored.
In this paper, we propose a simple but efficient method,
MANIPTRANS, which facilitates the transfer of hand ma-
nipulation skills—especially bimanual actions—to dexter-
ous robotic hands in simulation, enabling accurate tracking
of reference motions. Our key insight is to treat the trans-
fer as a two-stage process: a pre-training trajectory imi-
tation stage focusing on hand motion alone, followed by a
specific action fine-tuning stage that meets interaction con-
straints. Specifically, we design a robust generalist model
that learns to accurately mimic human finger motions with
resilience to noise. Based on this initial imitation, we then
introduce a residual learning module [48, 51, 53, 106] that
incrementally refines the robot’s actions, focusing on two
key aspects: 1) ensuring stable contact with object surfaces
under physical constraints, enabling effective object manip-
ulation, and 2) coordinating both hands to ensure precise,
high-fidelity execution of complex bimanual operations.
The advantages of this design are threefold: 1) In the
first stage, focusing on dynamic hand mimicry with large-
scale pretraining effectively mitigates morphological dif-
ferences. 2) Building on this advantage, the second stage
concentrates on tracking bimanual object interactions, en-
abling precise capture of subtle movements and facili-
tating natural, high-fidelity manipulation. 3) It signifi-
cantly reduces action space complexity by decoupling hu-
man hand motion imitation from physics-based object inter-
action constraints, thus improving training efficiency.
Building on this framework, MANIPTRANS corrects
arbitrary, noisy hand MoCap data into physically plausi-
ble motion without predefined stages (e.g., “approaching-
grasping-manipulation”) or task-specific reward engineer-
ing. We, therefore, validate its effectiveness and efficiency
across a range of complex single- and bimanual manipu-
lations, including articulated object handling [32, 34, 62,
107, 134]. Using MANIPTRANS, we transfer several rep-
resentative hand-object manipulation datasets [62, 134] to
dexterous robotic hands in the Isaac Gym simulation [79],
constructing the DEXMANIPNET dataset, which achieves
marked improvements in motion fidelity and compliance.
Currently, DEXMANIPNET comprises 3.3K episodes and
1.34 million frames of robotic hand manipulation, covering
previously unexplored tasks such as pen capping, bottle cap
unscrewing, and chemical experimentation.
We experimentally demonstrate that MANIPTRANS out-
performs baseline methods in both motion precision and
transfer success rate. Notably, it surpasses prior state-of-
the-art (SOTA) approaches in transfer efficiency, even on a
personal computer. To evaluate its extensibility, we con-
ducted cross-embodiment experiments applying MANIP-
TRANS to dexterous hands with varying degrees of free-
dom (DoFs) and morphologies, achieving consistent per-
formance with minimal additional effort. Furthermore, we
replay DEXMANIPNET’s bimanual trajectories on real-
world devices, demonstrating agile and natural dexter-
ous manipulation that, to the best of our knowledge, has
not been achieved by previous RL- or teleoperation-based
methods.
Finally, we benchmark DEXMANIPNET us-
ing several imitation learning frameworks, underscoring its
value to the research community.
In summary, our contributions are as follows:
• We introduce MANIPTRANS, a simple yet effective two-
stage transfer framework that enables precise transfer of
human bimanual manipulation to dexterous robotic hands
in simulation, ensuring accurate tracking of both hand and
object reference motions.
• Using this framework, we construct DEXMANIPNET, a
large-scale, high-quality dataset featuring a wide array
of novel bimanual manipulation tasks with high preci-
sion and compliance. DEXMANIPNET is extensible and
serves as a valuable resource for future policy training.
• Our experiments show that MANIPTRANS outperforms
previous SOTA methods. We further demonstrate its gen-
eralizability across various dexterous hand configurations
and its feasibility for real-world deployment.
2. Related Works
Dexterous Manipulation via Human Demonstration
Learning manipulation skills from human demonstrations
offers an intuitive and effective approach to transferring
2


<!-- page 3 (ocr) -->
human abilities to robots [6, 31, 129, 132].
Imitation
learning has shown considerable promise in achieving this
transfer [7, 23, 64, 71, 80, 89, 90, 109, 112, 139, 142].
Recent studies focus on learning RL policies guided by
object trajectories [21, 22, 72, 77, 142].
QuasiSim [72]
advances this approach by directly transferring reference
hand motions to robotic hands via parameterized quasi-
physical simulators. However, these methods are limited
to simpler tasks and are computationally intensive. More
recently,
tailored solutions using task-specific reward
functions have been developed for challenging tasks like
bimanual lip-twisting [68, 70].
In contrast, our method
enables efficient learning of complex manipulation tasks
without task-specific reward engineering.
Dexterous Hand Datasets Object manipulation is funda-
mental for embodied agents. Numerous MANO-based [96]
hand-object interaction datasets exist [9, 10, 14, 28, 32, 36,
37, 39, 40, 42, 55, 57, 60–62, 73, 74, 93, 100, 107, 119, 125,
134, 141, 143].
However, these datasets often prioritize
pose alignment with 2D images while neglecting physical
constraints, limiting their applicability for robotic training.
Teleoperation methods [26, 44, 45, 92, 113, 117, 128, 140]
collect human-to-robot hand matching data online using
AR/VR systems [15, 24, 30, 52, 86] or vision-based Mo-
Cap [94, 113, 114] for real-time data acquisition and cor-
rection with humans in the loop. However, teleoperation
is labor-intensive and time-consuming, and the absence of
tactile feedback often yields stiff, unnatural actions, hin-
dering fine-grained manipulation. In contrast, our method
enables offline transfer of human demonstrations to robots.
Our DEXMANIPNET offers a large, easily expandable col-
lection of human demonstration episodes.
Residual Learning Due to the sample inefficiency and
time-consuming nature of RL training, residual policy
learning [53, 98, 106], which incrementally refines action
control, is widely adopted to enhance efficiency and sta-
bility. In dexterous hand manipulation, various studies ex-
plore residual strategies tailored to specific tasks [5, 21, 29,
38, 98, 118, 138, 139]. For instance, [38] integrates user
input during residual policy training, while [51] learns cor-
rective actions from human demonstrations. GraspGF [118]
employs a pre-trained score-based generative model as a
base, and [21] decomposes the imitation task into wrist
following and finger motion control, integrating a resid-
ual wrist control policy.
Additionally, [48] constructs a
mixture-of-experts system [49] using residual learning, and
DexH2R [139] applies residual learning directly to retar-
geted robotic hand actions. Our method differs from these
approaches by pre-training a finger motion imitation model
that incorporates additional dynamic information, followed
by fine-tuning a residual policy to adapt to task-specific
physical constraints. This approach is more efficient and
generalizable across various manipulation tasks.
3. Method
We provide an overview of our method in Fig. 2. Given
reference human hand–object interaction trajectories, our
goal is to learn a policy that enables dexterous robotic hands
to accurately replicate these trajectories in simulation while
satisfying the task’s semantic manipulation constraints. To
this end, we propose a two-stage framework: the first stage
trains a general hand trajectory imitation model, and the
second stage employs a residual model to refine the initial
coarse motion into task-compliant actions.
3.1. Preliminaries
Without loss of generality, we formulate the manipulation
transfer problem in a complex bimanual setting, where the
left and right dexterous hands, d = {dl, dr}, aim to repli-
cate the behavior of human hands, h = {hl, hr}, which
interact with two objects, o = {ol, or}, in a cooperative
manner (e.g., in a pen-capping task where one hand holds
the cap while the other grips the pen body).
The refer-
ence trajectories from human demonstrations are defined as
T h = {τ t
h}T
t=1 and T o = {τ t
o}T
t=1, where T represents
the total number of frames. The trajectory τ h for each hand
includes the wrist’s 6-DoF pose wh ∈SE(3), the linear and
angular velocities ˙wh = {vh, uh}, and the finger joint po-
sitions jh ∈RF ×3 defined by MANO [96], along with their
respective velocities ˙jh = {vj, uj}; here, F denotes the
number of hand keypoints, including the fingertips. Sim-
ilarly, the object trajectory τ o for each object includes its
6-DoF pose po ∈SE(3) and the corresponding linear and
angular velocities ˙po = {vo, uo}. To reduce spatial com-
plexity, we normalize all translations relative to the dexter-
ous hand’s wrist position while preserving the original rota-
tions to maintain the correct gravity direction.
We model this problem as an implicit Markov Decision
Process (MDP) M = ⟨S, A, T, R, γ⟩, where S represents
the state space, A the action space, T the transition dynam-
ics, R the reward function, and γ the discount factor. The
action for each dexterous hand at time t, denoted as at ∈A,
comprises the target positions of each dexterous hand’s joint
at
q ∈RK for proportional-derivative (PD) control, and the
6-DoF force at
w ∈R6 applied to the robotic wrist, simi-
lar to prior work [48, 111, 121], where K denotes the total
number of robotic hand revolute joints (i.e. the DoF).
Our approach divides the transfer process into two
stages:
1) a pre-trained hand-only trajectory imitation
model I, and 2) a residual module R that fine-tunes the
coarse actions to ensure task compliance. The state at time
t is defined separately for each stage as st
I ∈SI and
st
R ∈SR, with corresponding reward functions rt
I =
R(st
I, at
I) and rt
R = R(st
R, at
R) as described in Sec. 3.2
and Sec. 3.3. For both stages, we employ proximal policy
optimization (PPO) [99] to maximize the discounted reward
E
T
t=1γt−1rt
stage , following previous methods [19, 89].
3
b>


<!-- page 4 (ocr) -->
❄
🔥
⊕
Figure 2. Our MANIPTRANS Pipeline. We first pre-train a hand motion imitation model with large-scale human demonstrations, then
fine-tune a residual policy to adapt to task-specific physical constraints.
3.2. Hand Trajectory Imitating
In this stage, our objective is to learn a general hand trajec-
tory imitation model, I, capable of accurately replicating
detailed human finger motions. The state for each dexter-
ous hand at time t is defined as st
I = {τ t
h, st
prop}, which
includes the target hand trajectory τ t
h and the current pro-
prioception st
prop = {qt
d, ˙qt
d, wt
d, ˙wt
d}. Here, qt
d and wt
d
denote the joint angles and wrist poses, respectively, along
with their corresponding velocities. We aim to train the pol-
icy πI(at|st
I, at−1) using RL to determine the actions at
I.
Reward Functions. The reward function rt
I is designed
to encourage the dexterous hands to track the reference
hand trajectory τ t
h while ensuring stability and smoothness.
It comprises three components: 1) Wrist tracking reward
rt
wrist: This reward minimizes the difference: wt
d ⊖wt
h and
˙wt
d −˙wt
h, ⊖denotes the difference in SE(3) space. 2)
Finger imitation reward rt
finger: This component encourages
the dexterous hand to closely follow the reference finger
joint positions. We manually select F finger keypoints on
the dexterous hand corresponding to the MANO model, de-
noted as jd. The weights wf and decay rates λf are empir-
ically set to emphasize the fingertips, particularly those of
the thumb, index, and middle fingers. The parameters are
in the Appx. This design helps mitigate the impact of mor-
phological differences between human and robotic hands:
  
r^t_{\ t ex
t { fi n ger }} = \t
ex t st
yl e 
\sum _{f=1}^F { w_{f} \cdot \exp {(-\lambda _{f} \|\mbold {j}_{{\dexhand _f}}^t - \mbold {j}_{{\hand _f}}^t\|\smash {_{\scriptscriptstyle 2}^{\scriptscriptstyle 2}})}} \label {eq:finger_reward} 
(1)
3) Smoothness Reward rt
smooth: To alleviate jerky motions,
we introduce a smoothness reward that penalizes the power
exerted on each joint, defined as the element-wise prod-
uct of joint velocities and torques, similar to the approach
in [76]. The total reward is defined as: rt
I = wwrist · rt
wrist +
wfinger · rt
finger + wsmooth · rt
smooth.
Training Strategy. Decoupling hand imitation from object
interaction offers additional benefits; specifically, πI does
not require challenging-to-acquire manipulation data. We
train the policy using hand-only datasets, including exist-
ing hand motion collections [14, 36, 62, 107, 134, 137, 144]
and synthetic data generated via interpolation [105]. To bal-
ance training data between the left and right hands, we mir-
ror these datasets; training time and additional details are
provided in the Appx. For efficiency, we employ reference
state initialization (RSI) and early termination [88, 89]. If
the dexterous hand keypoints jd deviate beyond a threshold
ϵfinger, the episode terminates early and resets to a randomly
sampled MoCap state. We also utilize curriculum learn-
ing [8], gradually reducing ϵfinger to encourage broad explo-
ration initially, then focusing on fine-grained finger control.
3.3. Residual Learning for Interaction
Building on the pre-trained πI, we use a residual module R
to refine coarse actions and satisfy task-specific constraints.
State Space Expansion for Interaction.
To account for
interactions between the dexterous hands and objects, we
expand the state space beyond the hand-related states st
I
by incorporating additional interaction-related information.
First, we compute the convex hull [116] of the object
meshes o from MoCap data to generate the collidable ob-
ject ˆo in the simulation environment. To manipulate the
object along the reference T o, we include the object’s
position pˆo (relative to the wrist position wd) and ve-
locities ˙pˆo, center of mass mˆo, and gravitational force
vector Gˆo. To better encode the object’s shape, we uti-
lize the BPS representation [91].
Additionally, for en-
hancing perception, we encode the spatial relationship be-
tween the hands and the object using the distance met-
ric: D(jt
d, pt
ˆo) = ∥jt
d −pt
ˆo∥2
2, measuring the squared Eu-
clidean distance between the dexterous hand keypoints and
the object’s position. Furthermore, we explicitly include
the contact force C obtained from the simulation, cap-
turing the interaction between the fingertips and the ob-
ject’s surface.
This tactile feedback is critical for stable
grasping and manipulation, ensuring precise control dur-
4
MoCap Data
Rollout in Simulation
Sa
-
€¥ MANIPTRANS
ulin
Simo
u
N
\
||
1
i
(1
o
nll
\
a
>
= \
Prd
u
Reference
hand trajectories 7h—>
—> ™”%
oy
u
It
Hand Imitator
u
|
|
{
u
“dd
=
u
-
n
Reference object trajectories To—p
—>Aar
=
-
=
Shape info
A
Contact info +proprioception


<!-- page 5 (ocr) -->
ing complex tasks.
In summary, the expanded interac-
tion state for the residual module is defined as: st
interact =
{τ t
o, pt
ˆo, ˙pt
ˆo, mt
ˆo, Gt
ˆo, BPS(ˆo), D(jt
d, pt
ˆo), Ct}.
Residual Actions Combining Strategy. Given the com-
bined state st
R
=
st
I ∪st
interact, our goal is to learn
residual actions ∆at
R that refine the initial imitation ac-
tions at
I to ensure task compliance.
During each step
of the manipulation episode, we first sample the imita-
tion action at
I ∼πI(at|st
I, at−1). Conditioned on this
action, we then sample the residual correction ∆at
R ∼
πR(∆at|st
R, at
I, at−1). The final action is computed as:
at = at
I + ∆at
R, where the residual action is added
element-wise. The resulting action at is then clipped to
adhere to the dexterous hand’s joint limits. At the start of
training, since the dexterous hand movements already ap-
proximate the reference hand trajectory, the residual actions
are expected to be close to zero. This initialization helps
prevent model collapse and accelerates convergence. We
achieve this by initializing the residual module with a zero-
mean Gaussian distribution and employing a warm-up strat-
egy to gradually activate its training.
Reward Functions. Our objective is to efficiently transfer
human bimanual manipulation skills to dexterous robotic
hands in a task-agnostic manner. To this end, we avoid task-
specific reward engineering, which, although beneficial for
individual tasks, can limit generalization. Therefore, our
reward design remains simple and general. In addition to
the hand imitation reward rt
I discussed in Sec. 3.2, we in-
troduce two additional components: 1) Object following re-
ward rt
object: Minimizes positional and velocity differences
between the simulated object and its reference trajectory,
specifically pt
ˆo ⊖pt
o and ˙pt
ˆo −˙pt
o. 2) Contact force re-
ward rt
contact: Encourages appropriate contact force when
the hand-object distance in the MoCap dataset is below a
specified threshold ξc. The reward is defined as:
  
r^t_{\t e xt {co n
tac
t}
} = w
_{ \ t
e
xt {
c} } \
c d ot \e
xp {(\frac {-\lambda _{\text {c}}}{\textstyle \sum _{f=1}^F\mbold {C}_{\dexhand _f}^t \cdot \mathds {1}\left (\mbold {D}(\mbold {j}_{\hand _f}^t, \mbold {p}_{\obj }^t \cdot \obj ) < \xi _{\text {c}}\right )})} \label {eq:contact_reward} 
(2)
where D(jt
hf , pt
o · o) represents the minimum distance
between the fingertip hf and the transformed object sur-
face, 1(·) is the indicator function, and Ct
df denotes the
contact force at the fingertip. The weight wc and decay
rate λc are empirically set to balance the reward func-
tion. The total reward for the residual stage is defined as
rt
R = rt
I + wobject · rt
object + wcontact · rt
contact.
Training Strategy. Inspired by prior work [72, 84, 85] that
utilizes quasi-physical simulators to relax constraints dur-
ing training and avoid local minima, we introduce a relax-
ation mechanism in the residual learning stage. Unlike [72],
which employs custom simulations, we adjust the physical
constraints directly within the Isaac Gym environment [79]
to enhance training efficiency. Specifically, we initially set
the gravitational constant G to zero and the friction coef-
ficient F to a high value. This setup allows the robotic
hands to, early in training, grip objects firmly and efficiently
align with reference trajectories. As training progresses,
we gradually restore G to its true value and reduce F to
a suitable value to approximate real interactions. Similar
to the imitation stage, we adopt RSI, early termination, and
curriculum learning strategies. Each episode initializes the
robotic hands by randomly selecting a non-colliding near-
object state from the preprocessed trajectory. During train-
ing, if the object’s pose pt
ˆo deviates beyond a predefined
threshold ϵobject, the episode is terminated early. We pro-
gressively reduce ϵobject to encourage more precise object
manipulation. Additionally, we introduce a contact termi-
nation condition: if MoCap data indicates a firm grasp by
the human hands (i.e., D(jt
hf , pt
o · o) < ξt, where ξt is the
termination threshold), the contact force Ct
df must be non-
zero. Failure to meet this condition results in early termi-
nation. This mechanism ensures the agent learns to control
contact forces, promoting stable object manipulation.
3.4. DEXMANIPNET Dataset
Using MANIPTRANS, we generate DEXMANIPNET, de-
rived from two representative large-scale hand-object inter-
action datasets: FAVOR [62] and OakInk-V2 [134]. FA-
VOR employs VR-based teleoperation with human-in-the-
loop corrections, focusing on foundational tasks like ob-
ject rearrangement. In contrast, OakInk-V2 utilizes optical
tracking-based motion capture, targeting more complex in-
teractions such as pen capping and bottle unscrewing.
Due to the lack of standardization in dexterous robotic
hands, we adopt the Inspire Hand [3] as our primary plat-
form for its high dexterity, stability, cost-effectiveness, and
extensive prior use [24, 35, 52]. To address the complexity
of bimanual tasks, we employ a simulated 12-DoF config-
uration of the Inspire Hand, enhancing flexibility compared
to its real-world 6-DoF mechanism. We demonstrate MA-
NIPTRANS’s adaptability to other robotic hands and real-
world deployment in Sec. 4.4 and Sec. 4.5.
Our DEXMANIPNET encompasses 61 diverse and chal-
lenging tasks as defined in [134], comprising 3.3K episodes
of robotic hand manipulation over 1.2K objects, totaling
1.34 million frames, including ∼600 sequences involving
complex bimanual tasks. Each episode executes precisely
in the Isaac Gym simulation [79]. In comparison, a recent
dataset generated via automated augmentation [52] includes
only 60 source human demonstrations across 9 tasks.
4. Experiments
In experiments, we describe the dataset setup and metrics
(Sec. 4.1), followed by implementation details (Sec. 4.2).
We then compare MANIPTRANS with SOTA methods
5


<!-- page 6 (ocr) -->
(Sec. 4.3), demonstrate cross-embodiment generalization
(Sec. 4.4), validate real-world deployment (Sec. 4.5), con-
duct ablation studies (Sec. 4.6), and benchmark DEXMA-
NIPNET for learning manipulation policies (Sec. 4.7).
4.1. Datasets and Metrics
Datasets For quantitative evaluation, we use the official
validation dataset of OakInk-V2 [134], approximately half
of which consists of bimanual tasks. To assess transfer ca-
pabilities, we manually select MoCap sequences that meet
task completeness and semantic relevance, filtering them to
durations of 4–20 seconds and downsampling to 60 fps. We
exclude sequences involving deformable or oversized ob-
jects, resulting in ∼80 episodes. For qualitative evalua-
tion, we also incorporate the GRAB [107], FAOVR [62],
and ARCTIC [32] datasets to demonstrate our advantages.
Metrics To evaluate MANIPTRANS in terms of manipu-
lation precision, task compliance, and transfer efficiency,
we introduce the following metrics.
These are adapted
from [72] but are more stringent due to the complexity of
our bimanual tasks: 1) Per-frame Average Object Rota-
tion and Translation Error:Er = 1
T
T
t=1(prot
t
ˆo · (prot
t
o)−1)
and Et =
1
T
T
t=1 ∥ptsl
t
ˆo −ptsl
t
o∥2
2.
Here, prot and ptsl
are the rotation and translation components of the 6-DoF
pose p, respectively.
Errors Er and Et are reported in
degrees and centimeters. 2) Mean Per-Joint Position Er-
ror (in cm): Ej =
1
T ·F
T
t=1
F
f=1 ∥jt
df −jt
hf ∥2
2. This
metric measures the average error in the positions of the
hand joints. 3) Mean Per-Fingertip Position Error (in cm):
Eft =
1
T ·M
T
t=1
M
ft=1 ∥tt
dft −tt
hft∥2
2. This metric eval-
uates the mimicry quality of fingertip t motions, accounting
for morphological differences between human and robotic
hands. Here, M equals 5 for single-hand tasks and 10 for
bimanual tasks. 4) Success Rate (SR): A tracking attempt
is deemed successful if Er, Et, Ej, and Eft are all below
the specified thresholds: 30◦, 3 cm, 8 cm, and 6 cm, re-
spectively. For bimanual tasks, the trajectory is considered
failed if either hand fails to meet these conditions, making
the success criterion stricter compared to single-hand tasks.
4.2. Implementation Details
In MANIPTRANS, we manually selected F = 21 keypoints
on each dexterous robotic hand, corresponding to the fin-
gertips, palm, and phalangeal positions on the human hand,
to mitigate the morphological differences. Details on key-
point selection and weight coefficients w for reward terms
are provided in Appx. For training, we use a curriculum
learning strategy. The initial threshold ϵfinger is set to 6 cm
and decays to 4 cm. Object alignment thresholds ϵobject start
at 90◦and 6 cm for rotation and translation, gradually de-
creasing to 30◦and 2 cm. We train both the imitation mod-
ule I and residual module R using the Actor-Critic PPO
algorithm [99], with a training horizon of 32 frames, a mini-
batch size of 1024, and a discount factor γ = 0.99. Opti-
mization employs Adam [56] with an initial learning rate
of 5 × 10−4 and a decay scheduler. All experiments are
run in Isaac Gym [79], simulating 4096 environments at a
time step of 1/60 s on a personal computer equipped with
an NVIDIA RTX 4090 GPU and an Intel i9-13900KF CPU.
4.3. Evaluations
As discussed in Sec. 2, dexterous hand manipulation ad-
vances rapidly, with previous approaches differing in prob-
lem formulations and task definitions. To offer a compre-
hensive and fair comparison, we evaluate two categories
of methods—RL-combined and optimization-based—to
demonstrate MANIPTRANS’s accuracy and efficiency.
Comparison with RL-Combined Methods
Due to the
lack of publicly available code for prior RL-combined
methods, we reimplement representative approaches: 1)
RL-Only exploration using only trajectory-following re-
wards, employing the PPO algorithm to train the robotic
hand from scratch based on [27]; 2) Retarget + Residual
learning, applying residual action to retargeted robotic hand
poses obtained via alignment between human and robot
keypoints [94]. As a naive baseline, we also include the
Retarget-Only method—retargeting without any learning.
As shown in Tab. 1, our method outperforms all base-
lines across multiple metrics, demonstrating superior preci-
sion in both single- and bimanual tasks. These results con-
firm that our two-stage transfer framework effectively cap-
tures subtle finger motions and object interactions, leading
to high task success rates and motion fidelity.
We find that the Retarget-Only baseline is nearly infea-
sible due to the complexity of the dexterous hand action
space and error accumulation. The RL-Only baseline per-
forms suboptimally since exploration from scratch is time-
consuming and reduces motion precision. Compared to the
Retarget + Residual baseline, our method—leveraging a
pre-trained hand imitation model—demonstrates improved
control capabilities, enabling more accurate manipulation
aligned with the reference trajectory. Notably, the Retar-
geting method often causes collisions in contact-rich sce-
narios, resulting in instability during residual policy train-
ing.
We further study MANIPTRANS’s robustness and
time cost in Appx.
Fig. 3 shows the qualitative results
Methods
Er ↓
Et ↓
Ej ↓
Eft ↓
SR ↑
Retarget-Only
N/A
N/A
N/A
N/A
4.6 / 0.0
RL-Only
9.72
1.23
2.96
2.38
34.3 / 12.1
Retarget + Residual
11.58
0.79
2.54
1.74
47.8 / 13.9
MANIPTRANS
8.60
0.49
2.15
1.36
58.1 / 39.5
Table 1. Quantitative Comparisons with RL-Combined Base-
lines. The first four metrics are computed only on successfully
rolled-out sequences. The SR includes the separated transfer suc-
cess rates for single/bimanual tasks. The error scores on Retarget-
Only are not available since it hardly works.
6
-x
-X
—X
x
—x
x


<!-- page 7 (ocr) -->
Figure 3. Qualitative Results of MANIPTRANS. We showcase the transfer results using the Inspire left and right hands on both single-
hand tasks (top two rows) and bimanual tasks (bottom row) from the OakInk-V2 [134] dataset. Notably, the dexterous hands successfully
manipulate delicate and slim objects, such as a pen and a flower stem.
Figure 4. Qualitative Comparison with QuasiSim [72]. MA-
NIPTRANS produces more natural motion of the Shadow hand
(purple region) and is applicable to other dexterous hands.
on seldom-explored tasks, highlighting the natural and pre-
cision of MANIPTRANS transferring human manipulation
skills. Additional details and more qualitative results apply-
ing our method to articulated objects are provided in Appx.
Comparison with Optimization-Based Method
Qua-
siSim [72] optimizes over customized simulations to track
human motions. Currently, their full pipeline has not yet
been released, and their “randomly” selected validation set
is not available. Thus, a direct quantitative comparison is
not feasible. Therefore, we provide a qualitative compar-
ison in Fig. 4, demonstrating MANIPTRANS’s ability to
transfer human motions to the Shadow Hand in a setting
similar to QuasiSim’s, but with more stable contacts and
smoother motions. Notably, due to our two-stage design,
for an unseen single-hand manipulation trajectory of 60
frames (“rotating a mouse”), our method requires ∼15
minutes of training to achieve robust results, compared
to QuasiSim’s ∼40 hours of optimization1, highlighting
MANIPTRANS’s significant efficiency.
4.4. Cross-Embodiments Validation
We demonstrate MANIPTRANS’s extensibility across vari-
ous dexterous hand embodiments. As described in Sec. 3,
the imitation module I addresses hand keypoint tracking,
while the residual module R captures physical interac-
tions between fingertips and objects.
Our framework is
1Results shown in QuasiSim’s Appx and its official repository:
https://github.com/Meowuu7/QuasiSim
Figure 5. Cross Embodiments Results: Putting off Alcohol lamp.
embodiment-agnostic since it relies solely on the correspon-
dence between human fingers and robotic joints, allowing
adaptation to different dexterous hands with minimal effort.
We evaluate MANIPTRANS on the Shadow Hand [1], ar-
ticulated MANO hand [27, 96], Inspire Hand [3], and Al-
legro Hand [2], which have varying DoFs: K = 22, 22,
12, and 16, respectively. Without altering network hyperpa-
rameters or reward weights, MANIPTRANS achieves con-
sistent, fluid, and precise performance across all embodi-
ments in both single-hand tasks (Fig. 4) and bimanual tasks
(Fig. 5). Additional details on the Allegro Hand—a robotic
hand with only four fingers—are provided in Appx.
4.5. Real-World Deployment
As illustrated in Fig. 6, we conduct experiments using
two 7-DoF Realman arms [95] and a pair of upgraded In-
spire Hands (same configuration yet adding tactile sensors).
To bridge the gap between the simulated 12-DoF robotic
hands and the 6-DoF real hardware, we employ a fitting-
based method that optimizes the joint angles q˜d ∈R6 of
the real robots (denoted as ˜·) for fingertip alignment, for-
mulated as: argminq˜d
1
T ·M
T
t=1
M
ft=1 ∥tt
dft −tt
˜dft∥2
2
with an additional temporal smoothness loss: Lsmooth =
1
T −1
T −1
t=1 ∥qt+1
˜d
−qt
˜d∥2
2. We control the arms by solving
inverse kinematics to align the arms’ flanges with the dex-
terous hands’ wrists wd. During replay, we do not enforce
strict temporal alignment, as the real robots cannot always
operate as quickly as human hands.
Fig. 6 showcases dexterous manipulation that, to the best
7
Shake the erlenmeyer flask
Flower atrangement
EE © Lhne \) ®
&
Pour water
IEEELL ddd
a
Pour from the mug into the teacup
Scrape out with the spoon
QuasiSimy,
-
;
)
f
TF FN
SE
Wo So A fei Ba ll on WO Sg
i, Be Te a fa de dw
i
stro Sr SR
<<,<< <5
Allegroif amy 58:ns,£4J {Pry :Zo =:2
—X
x
—Xx


<!-- page 8 (ocr) -->
Figure 6. Real-world bimanual manipulation deployment. Pur-
ple box: human hand motion; orange box: close-up of dexterous
hands. More results are on the website. (Zoom in for details.
)
0
100
200
300
400
500
Iteration
0.0
0.2
0.4
0.6
0.8
1.0
Success Rate (%)
w/o C reward
w/o C obs
w/o C term
Ours
(a) Tactile ablations training curve.
0
200
400
600
800
Iteration
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
Success Rate (%)
w/o relax-gravity
w/o increased friction
w/o relax-thresholds
Ours
(b) Curve on training strategies.
Figure 7. Training Curve of Ablation Studies. We assess tactile
feedback in contact-rich tasks (e.g., turning off a lamp) and cur-
riculum learning in complex ones (e.g., capping a pen).
Methods
IBC [33]
BET [101]
DP-UNet [25]
DP-Trans [25]
SR
4.69%
9.69%
18.44%
14.69%
Table 2. Imitating Learning on Bottle Rearrangement Task.
of our knowledge, has not previously been achieved. For
example, in “opening the toothpaste”, the left hand stably
holds the tube while the right hand’s thumb and index fin-
ger flexibly pop open the tiny cap—motions challenging to
capture via teleoperation. This underscores the potential of
our method for future real-world policy learning.
4.6. Abalation Studies
Tactile Information as Auxiliary Input In Sec. 3.3, we
integrate tactile information, specifically the contact force
C, into the pipeline in three ways: (1) as an observation in-
put, (2) as a reward component to encourage contact, and
(3) as a condition for early termination. Ablation studies
(Fig. 7a) labeled w/o C obs, w/o C reward, and w/o C term
demonstrate that including C in the reward function im-
proves task success rates, and treating C as an observation
accelerates convergence. We also find that omitting C as a
termination condition seems to enhance initial training per-
formance but lowers overall convergence speed, highlight-
ing the importance of stable contact in task completion.
Training Strategy We begin training with a curriculum
learning strategy that includes (1) relaxing gravity effects,
(2) increasing friction influence, and (3) relaxing thresh-
olds ϵfinger and ϵobject. Ablation studies (Fig. 7b), labeled
w/o relax-gravity, w/o increased friction, and w/o relax-
thresholds, show that for precise, complex bimanual mo-
tions, ignoring gravity and using high friction coefficients in
the early stages accelerate convergence and achieve higher
overall SR. Without initial relaxation of the threshold con-
straints, the network may fail to converge entirely.
4.7. DEXMANIPNET for Policy Learning
To benchmark DEXMANIPNET’s potential, we evaluate
representative imitation learning methods on a fundamental
policy learning task: rearrangement. Specifically, we focus
on moving a bottle to a goal position. Given the bottle’s
current and goal 6D poses, the environment state (includ-
ing obstacles on the table), and the dexterous hand’s propri-
oception, the policy generates a sequence of robotic hand
actions to pick up the bottle and place it at the target.
We evaluate four representative imitation learning
methods:
two regression-based behavior cloning ap-
proaches—IBC [33] and BET [101]—and two diffusion
policy methods [25] with UNet [97] and Transformer [110]
backbones. Each policy is trained on 85% of the 140 se-
quences involving the bottle rearrangement task in DEX-
MANIPNET and evaluated on the remaining 15%. We per-
form 20 rollouts per sequence. A rollout is considered suc-
cessful if the object’s final position is within 10 cm of the
goal. Further details are provided in Appx.
As shown in Tab. 2, all methods perform suboptimally
due to the task’s difficulty and the complexity of the dexter-
ous hand action space. Regression-based behavior cloning
approaches, in particular, suffer from error accumulation.
These results highlight the inherent challenges of dexterous
manipulation tasks, which require precise finger control and
effective object manipulation. We hope that DEXMANIP-
NET will facilitate advancements in this domain.
5. Conclusion and Discussion
MANIPTRANS is a two-stage framework that efficiently
transfers human manipulation skills to dexterous robotic
hands. By decoupling hand motion imitation from object
interaction via residual learning, MANIPTRANS overcomes
morphological differences and complex task challenges, en-
suring high-fidelity motions and efficient training. Exper-
iments demonstrate that MANIPTRANS surpasses SOTA
methods in motion precision and computational efficiency,
while also exhibiting cross-embodiment adaptability and
feasibility for real-world deployment. Furthermore, the ex-
tensible DEXMANIPNET establishes a new benchmark to
advance progress in embodied AI.
Discussion and Limitations
Although
MANIPTRANS
successfully handles most MoCap data, some sequences
cannot be transferred effectively. We attribute this to two
main reasons: 1) excessive noise in interaction poses and
2) insufficiently accurate object models for simulation,
particularly for articulated objects.
Enhancing MANIP-
TRANS’s robustness and generating physically plausible
object models are valuable directions for future research.
8
5%
a NE \e Cl \ SE
Q
A EE
J
EE


<!-- page 9 (ocr) -->
References
[1] ShadowRobot. https://www.shadowrobot.com/
dexterous-hand-series, 2005. 1, 7, 2
[2] Allegro Hands. https://www.allegrohand.com,
2013. 7, 1, 2
[3] Inspire
Hands.
https : / / en . inspire -
robots . com / product - category / the -
dexterous-hands, 2019. 1, 5, 7, 2
[4] Ananye Agarwal, Shagun Uppal, Kenneth Shaw, and
Deepak Pathak. Dexterous functional grasping. In CoRL,
2023. 1
[5] Minttu Alakuijala, Gabriel Dulac-Arnold, Julien Mairal,
Jean Ponce, and Cordelia Schmid.
Residual reinforce-
ment learning from demonstrations.
arXiv preprint
arXiv:2106.08050, 2021. 3
[6] Brenna D Argall, Sonia Chernova, Manuela Veloso, and
Brett Browning. A survey of robot learning from demon-
stration. Robotics and autonomous systems, 2009. 3
[7] Sridhar Pandian Arunachalam, Sneha Silwal, Ben Evans,
and Lerrel Pinto.
Dexterous imitation made easy:
A
learning-based framework for efficient dexterous manipu-
lation. In ICRA, 2023. 3
[8] Yoshua Bengio, J´erˆome Louradour, Ronan Collobert, and
Jason Weston. Curriculum learning. In Proceedings of the
26th annual international conference on machine learning,
2009. 4
[9] Samarth Brahmbhatt, Cusuh Ham, Charles C. Kemp, and
James Hays. ContactDB: Analyzing and predicting grasp
contact via thermal imaging. In CVPR, 2019. 3
[10] Samarth Brahmbhatt, Chengcheng Tang, Christopher D.
Twigg, Charles C. Kemp, and James Hays. ContactPose:
A dataset of grasps with object contact and hand pose. In
ECCV, 2020. 2, 3
[11] Anthony Brohan, Noah Brown, Justice Carbajal, Yev-
gen Chebotar, Joseph Dabis, Chelsea Finn, Keerthana
Gopalakrishnan, Karol Hausman, Alex Herzog, Jasmine
Hsu, et al. Rt-1: Robotics transformer for real-world con-
trol at scale. arXiv preprint arXiv:2212.06817, 2022. 1
[12] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen
Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding,
Danny Driess, Avinava Dubey, Chelsea Finn, et al. Rt-2:
Vision-language-action models transfer web knowledge to
robotic control. arXiv preprint arXiv:2307.15818, 2023. 1
[13] Zhe Cao, Ilija Radosavovic, Angjoo Kanazawa, and Jiten-
dra Malik. Reconstructing hand-object interactions in the
wild. In ICCV, 2021. 2
[14] Yu-Wei Chao, Wei Yang, Yu Xiang, Pavlo Molchanov,
Ankur Handa, Jonathan Tremblay, Yashraj S Narang, Karl
Van Wyk, Umar Iqbal, Stan Birchfield, et al.
Dexycb:
A benchmark for capturing hand grasping of objects. In
CVPR, 2021. 2, 3, 4
[15] Sirui Chen, Chen Wang, Kaden Nguyen, Li Fei-Fei, and
C Karen Liu.
Arcap:
Collecting high-quality human
demonstrations for robot learning with augmented reality
feedback. arXiv preprint arXiv:2410.08464, 2024. 3
[16] Tao Chen, Jie Xu, and Pulkit Agrawal. A system for general
in-hand object re-orientation. In CoRL, 2022. 1
[17] Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Ed-
ward Adelson, and Pulkit Agrawal. Visual dexterity: In-
hand reorientation of novel and complex object shapes. Sci-
ence Robotics, 2023.
[18] Tao Chen, Eric Cousineau, Naveen Kuppuswamy, and
Pulkit Agrawal.
Vegetable peeling:
A case study
in constrained dexterous manipulation.
arXiv preprint
arXiv:2407.07884, 2024.
[19] Yuanpei Chen, Tianhao Wu, Shengjie Wang, Xidong Feng,
Jiechuan Jiang, Zongqing Lu, Stephen McAleer, Hao Dong,
Song-Chun Zhu, and Yaodong Yang. Towards human-level
bimanual dexterous manipulation with reinforcement learn-
ing. NeurIPS, 2022. 3
[20] Yuanpei Chen, Chen Wang, Li Fei-Fei, and C Karen Liu.
Sequential dexterity: Chaining dexterous policies for long-
horizon manipulation.
arXiv preprint arXiv:2309.00987,
2023.
[21] Yuanpei Chen, Chen Wang, Yaodong Yang, and Karen Liu.
Object-centric dexterous manipulation from human motion
data. In CoRL, 2024. 3
[22] Zerui Chen, Shizhe Chen, Cordelia Schmid, and Ivan
Laptev.
Vividex:
Learning vision-based dexterous
manipulation
from
human
videos.
arXiv
preprint
arXiv:2404.15709, 2024. 1, 3
[23] Zoey Qiuyu Chen, Karl Van Wyk, Yu-Wei Chao, Wei Yang,
Arsalan Mousavian, Abhishek Gupta, and Dieter Fox.
Dextransfer: Real world multi-fingered dexterous grasp-
ing with minimal human demonstrations. arXiv preprint
arXiv:2209.14284, 2022. 3
[24] Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, and Xiao-
long Wang. Open-television: Teleoperation with immersive
active visual feedback. arXiv preprint arXiv:2407.01512,
2024. 3, 5, 2
[25] Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau,
Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran
Song. Diffusion policy: Visuomotor policy learning via ac-
tion diffusion. IJRR, 2023. 1, 8, 4
[26] Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, Ben-
jamin Burchfiel, Siyuan Feng, Russ Tedrake, and Shu-
ran Song.
Universal manipulation interface: In-the-wild
robot teaching without in-the-wild robots. arXiv preprint
arXiv:2402.10329, 2024. 1, 3
[27] Sammy Christen, Muhammed Kocabas, Emre Aksan,
Jemin Hwangbo, Jie Song, and Otmar Hilliges. D-grasp:
Physically plausible dynamic grasp synthesis for hand-
object interactions. In CVPR, 2022. 1, 2, 6, 7
[28] Enric Corona, Albert Pumarola, Guillem Alenya, Francesc
Moreno-Noguer, and Gr´egory Rogez. Ganhand: Predicting
human grasp affordances in multi-object scenes. In CVPR,
2020. 3
[29] Todor Davchev, Kevin Sebastian Luck, Michael Burke,
Franziska Meier, Stefan Schaal, and Subramanian Ra-
mamoorthy. Residual learning from demonstration: Adapt-
ing dmps for contact-rich manipulation. RA-L, 2022. 3
[30] Runyu Ding, Yuzhe Qin, Jiyue Zhu, Chengzhe Jia,
Shiqi Yang, Ruihan Yang, Xiaojuan Qi, and Xiaolong
Wang.
Bunny-visionpro:
Real-time bimanual dexter-
9


<!-- page 10 (ocr) -->
ous teleoperation for imitation learning.
arXiv preprint
arXiv:2407.03162, 2024. 3
[31] Peter Englert and Marc Toussaint. Learning manipulation
skills from a single demonstration. IJRR, 2018. 3
[32] Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed
Kocabas, Manuel Kaufmann, Michael J Black, and Otmar
Hilliges. Arctic: A dataset for dexterous bimanual hand-
object manipulation. In CVPR, 2023. 2, 3, 6, 1
[33] Pete Florence, Corey Lynch, Andy Zeng, Oscar A Ramirez,
Ayzaan Wahid, Laura Downs, Adrian Wong, Johnny Lee,
Igor Mordatch, and Jonathan Tompson. Implicit behavioral
cloning. In CoRL, 2022. 8, 4
[34] Rao Fu, Dingxi Zhang, Alex Jiang, Wanjia Fu, Austin
Funk, Daniel Ritchie, and Srinath Sridhar.
Gigahands:
A massive annotated dataset of bimanual hand activities.
arXiv preprint arXiv:2412.04244, 2024. 2
[35] Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, and
Chelsea Finn. Humanplus: Humanoid shadowing and im-
itation from humans.
arXiv preprint arXiv:2406.10454,
2024. 5, 2
[36] Daiheng Gao, Yuliang Xiu, Kailin Li, Lixin Yang, Feng
Wang, Peng Zhang, Bang Zhang, Cewu Lu, and Ping Tan.
Dart: Articulated hand model with diverse accessories and
rich textures. NeurIPS, 2022. 3, 4
[37] Guillermo Garcia-Hernando, Shanxin Yuan, Seungryul
Baek, and Tae-Kyun Kim. First-person hand action bench-
mark with rgb-d videos and 3d hand pose annotations. In
CVPR, 2018. 2, 3
[38] Guillermo Garcia-Hernando, Edward Johns, and Tae-Kyun
Kim.
Physics-based dexterous manipulations with esti-
mated hand poses and residual reinforcement learning. In
IROS, 2020. 3
[39] Shreyas Hampali, Mahdi Rad, Markus Oberweger, and Vin-
cent Lepetit. Honnotate: A method for 3d annotation of
hand and object poses. In CVPR, 2020. 2, 3
[40] Shreyas Hampali, Sayan Deb Sarkar, Mahdi Rad, and Vin-
cent Lepetit. Keypoint transformer: Solving joint identifi-
cation in challenging hands and object interactions for ac-
curate 3d pose estimation. In CVPR, 2022. 3
[41] Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Alek-
sei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makovi-
ichuk, Karl Van Wyk, Alexander Zhurkevich, Balakumar
Sundaralingam, et al. Dextreme: Transfer of agile in-hand
manipulation from simulation to reality. In ICRA. IEEE,
2023. 1, 2
[42] Yana Hasson, Gul Varol, Dimitrios Tzionas, Igor Kale-
vatykh, Michael J Black, Ivan Laptev, and Cordelia
Schmid. Learning joint reconstruction of hands and ma-
nipulated objects. In CVPR, 2019. 3
[43] Yana Hasson, Bugra Tekin, Federica Bogo, Ivan Laptev,
Marc Pollefeys, and Cordelia Schmid. Leveraging photo-
metric consistency over time for sparsely supervised hand-
object reconstruction. In CVPR, 2020. 2
[44] Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong
Zhang, Weinan Zhang, Kris Kitani, Changliu Liu, and
Guanya Shi. Omnih2o: Universal and dexterous human-
to-humanoid whole-body teleoperation and learning. arXiv
preprint arXiv:2406.08858, 2024. 1, 2, 3
[45] Tairan He, Zhengyi Luo, Wenli Xiao, Chong Zhang, Kris
Kitani, Changliu Liu, and Guanya Shi. Learning human-
to-humanoid real-time whole-body teleoperation.
arXiv
preprint arXiv:2403.04436, 2024. 1, 3
[46] Binghao Huang, Yuanpei Chen, Tianyu Wang, Yuzhe Qin,
Yaodong Yang, Nikolay Atanasov, and Xiaolong Wang.
Dynamic handover: Throw and catch with bimanual hands.
CoRL, 2023. 1
[47] Jingwei Huang, Yichao Zhou, and Leonidas Guibas. Man-
ifoldplus: A robust and scalable watertight manifold sur-
face generation method for triangle soups. arXiv preprint
arXiv:2005.11621, 2020. 4
[48] Ziye Huang, Haoqi Yuan, Yuhui Fu, and Zongqing Lu. Ef-
ficient residual learning with mixture-of-experts for univer-
sal dexterous grasping. arXiv preprint arXiv:2410.02475,
2024. 2, 3
[49] Robert A Jacobs, Michael I Jordan, Steven J Nowlan, and
Geoffrey E Hinton.
Adaptive mixtures of local experts.
Neural computation, 1991. 3
[50] Hanwen Jiang, Shaowei Liu, Jiashun Wang, and Xiaolong
Wang. Hand-object contact consistency reasoning for hu-
man grasps generation. In ICCV, 2021. 3
[51] Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, and
Li Fei-Fei. Transic: Sim-to-real policy transfer by learning
from online correction. In CoRL, 2024. 2, 3
[52] Zhenyu Jiang, Yuqi Xie, Kevin Lin, Zhenjia Xu, Weikang
Wan, Ajay Mandlekar, Linxi Fan, and Yuke Zhu. Dexmim-
icgen: Automated data generation for bimanual dexter-
ous manipulation via imitation learning.
arXiv preprint
arXiv:2410.24185, 2024. 1, 3, 5, 2
[53] Tobias Johannink, Shikhar Bahl, Ashvin Nair, Jianlan Luo,
Avinash Kumar, Matthias Loskyll, Juan Aparicio Ojea, Eu-
gen Solowjow, and Sergey Levine. Residual reinforcement
learning for robot control. In ICRA, 2019. 2, 3
[54] Leslie Pack Kaelbling, Michael L Littman, and Andrew W
Moore. Reinforcement learning: A survey. Journal of arti-
ficial intelligence research, 1996. 1
[55] Jeonghwan Kim, Jisoo Kim, Jeonghyeon Na, and Hanbyul
Joo. Parahome: Parameterizing everyday home activities
towards 3d generative modeling of human-object interac-
tions. arXiv preprint arXiv:2401.10232, 2024. 3
[56] Diederik Kingma and Jimmy Ba.
Adam: A method for
stochastic optimization. In ICLR, 2015. 6
[57] Taein Kwon, Bugra Tekin, Jan St¨uhmer, Federica Bogo,
and Marc Pollefeys. H2o: Two hands manipulating objects
for first person interaction recognition. In ICCV, 2021. 2, 3
[58] Haoming Li, Qi Ye, Yuchi Huo, Qingtao Liu, Shijian Jiang,
Tao Zhou, Xiang Li, Yang Zhou, and Jiming Chen. Tpgp:
Temporal-parametric optimization with deep grasp prior for
dexterous motion planning. In ICRA, 2024. 1
[59] Jinhan Li, Yifeng Zhu, Yuqi Xie, Zhenyu Jiang, Mingyo
Seo, Georgios Pavlakos, and Yuke Zhu. Okami: Teaching
humanoid robots manipulation skills through single video
imitation. arXiv preprint arXiv:2410.11792, 2024. 1
[60] Kailin Li, Lixin Yang, Haoyu Zhen, Zenan Lin, Xinyu
Zhan, Licheng Zhong, Jian Xu, Kejian Wu, and Cewu Lu.
Chord: Category-level hand-held object reconstruction via
shape deformation. In ICCV, 2023. 3
10


<!-- page 11 (ocr) -->
[61] Kailin Li, Jingbo Wang, Lixin Yang, Cewu Lu, and Bo Dai.
Semgrasp: Semantic grasp generation via language aligned
discretization. In ECCV, 2024. 3
[62] Kailin Li, Lixin Yang, Zenan Lin, Jian Xu, Xinyu Zhan,
Yifei Zhao, Pengxiang Zhu, Wenxiong Kang, Kejian Wu,
and Cewu Lu.
Favor: Full-body ar-driven virtual object
rearrangement guided by instruction text. AAAI, 2024. 2,
3, 4, 5, 6
[63] Puhao Li, Tengyu Liu, Yuyang Li, Yiran Geng, Yixin Zhu,
Yaodong Yang, and Siyuan Huang. Gendexgrasp: General-
izable dexterous grasping. In ICRA, 2023. 1
[64] Sizhe Li, Zhiao Huang, Tao Chen, Tao Du, Hao Su,
Joshua B Tenenbaum, and Chuang Gan. Dexdeform: Dex-
terous deformable object manipulation with human demon-
strations and differentiable physics. ICLR, 2023. 3
[65] Yuyang Li, Bo Liu, Yiran Geng, Puhao Li, Yaodong Yang,
Yixin Zhu, Tengyu Liu, and Siyuan Huang. Grasp multiple
objects with one hand. RA-L, 2024. 1
[66] Davide
Liconti,
Yasunori
Toshimitsu,
and
Robert
Katzschmann.
Leveraging pretrained latent represen-
tations for few-shot imitation learning on a dexterous
robotic hand. arXiv preprint arXiv:2404.16483, 2024. 1
[67] Kevin Lin, Lijuan Wang, and Zicheng Liu. End-to-end hu-
man pose and mesh reconstruction with transformers. In
CVPR, 2021. 2
[68] Toru Lin, Zhao-Heng Yin, Haozhi Qi, Pieter Abbeel, and
Jitendra Malik. Twisting lids off with two hands. arXiv
preprint arXiv:2403.02338, 2024. 1, 3, 2
[69] Qingtao Liu, Yu Cui, Qi Ye, Zhengnan Sun, Haoming Li,
Gaofeng Li, Lin Shao, and Jiming Chen. Dexrepnet: Learn-
ing dexterous robotic grasping network with geometric and
spatial hand-object representations. In IROS, 2023. 1
[70] Qingtao Liu, Qi Ye, Zhengnan Sun, Yu Cui, Gaofeng Li,
and Jiming Chen.
Masked visual-tactile pre-training for
robot manipulation. In ICRA, 2024. 1, 3
[71] Wenhai Liu, Junbo Wang, Yiming Wang, Weiming Wang,
and Cewu Lu. Force-centric imitation learning with force-
motion capture system for contact-rich manipulation. arXiv
preprint arXiv:2410.07554, 2024. 2, 3
[72] Xueyi Liu, Kangbo Lyu, Jieqiong Zhang, Tao Du, and Li
Yi. Parameterized quasi-physical simulators for dexterous
manipulations transfer. In ECCV, 2024. 1, 3, 5, 6, 7
[73] Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang
Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, and
Li Yi. Hoi4d: A 4d egocentric dataset for category-level
human-object interaction. In CVPR, 2022. 2, 3
[74] Yun Liu, Haolin Yang, Xu Si, Ling Liu, Zipeng Li, Yuxiang
Zhang, Yebin Liu, and Li Yi. Taco: Benchmarking gener-
alizable bimanual tool-action-object understanding. arXiv
preprint arXiv:2401.08399, 2024. 2, 3
[75] Haoran Lu, Ruihai Wu, Yitong Li, Sijie Li, Ziyu Zhu,
Chuanruo Ning, Yan Shen, Longzan Luo, Yuanpei Chen,
and Hao Dong.
Garmentlab: A unified simulation and
benchmark for garment manipulation. In NeurIPS, 2024.
1
[76] Zhengyi Luo, Jinkun Cao, Kris Kitani, Weipeng Xu, et al.
Perpetual humanoid control for real-time simulated avatars.
In ICCV, 2023. 4
[77] Zhengyi Luo, Jinkun Cao, Sammy Christen, Alexander
Winkler, Kris Kitani, and Weipeng Xu.
Grasping di-
verse objects with simulated humanoids.
arXiv preprint
arXiv:2407.11385, 2024. 1, 3
[78] Zhengyi Luo, Jiashun Wang, Kangni Liu, Haotian Zhang,
Chen Tessler, Jingbo Wang, Ye Yuan, Jinkun Cao, Zihui
Lin, Fengyi Wang, et al. Smplolympics: Sports environ-
ments for physically simulated humanoids. arXiv preprint
arXiv:2407.00187, 2024. 1
[79] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo,
Michelle Lu, Kier Storey, Miles Macklin, David Hoeller,
Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac
gym: High performance gpu-based physics simulation for
robot learning. arXiv preprint arXiv:2108.10470, 2021. 2,
5, 6, 1, 4
[80] Ajay Mandlekar, Yuke Zhu, Animesh Garg, Jonathan
Booher, Max Spero, Albert Tung, Julian Gao, John Em-
mons, Anchit Gupta, Emre Orbay, et al.
Roboturk: A
crowdsourcing platform for robotic skill learning through
imitation. In Conference on Robot Learning, 2018. 2, 3
[81] Xiaofeng Mao, Gabriele Giudici, Claudio Coppola, Kas-
par Althoefer, Ildar Farkhatdinov, Zhibin Li, and Lorenzo
Jamone. Dexskills: Skill segmentation using haptic data
for learning autonomous long-horizon robotic manipulation
tasks. arXiv preprint arXiv:2405.03476, 2024. 1
[82] Ji-Heon Oh, Ismael Espinoza, Danbi Jung, and Tae-Seong
Kim. Bimanual long-horizon manipulation via temporal-
context transformer rl. RA-L, 2024. 1
[83] Abby O’Neill, Abdul Rehman, Abhinav Gupta, Abhiram
Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham
Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, et al.
Open x-embodiment: Robotic learning datasets and rt-x
models. arXiv preprint arXiv:2310.08864, 2023. 1
[84] Tao Pang and Russ Tedrake. A convex quasistatic time-
stepping scheme for rigid multibody systems with contact
and friction. In ICRA, 2021. 5
[85] Tao Pang, HJ Terry Suh, Lujie Yang, and Russ Tedrake.
Global planning for contact-rich manipulation via local
smoothing of quasi-dynamic contact models. IEEE Trans-
actions on Robotics, 2023. 5
[86] Younghyo Park, Jagdeep Singh Bhatia, Lars Ankile, and
Pulkit Agrawal. Dexhub and dart: Towards internet scale
robot data collection.
arXiv preprint arXiv:2411.02214,
2024. 3
[87] Georgios Pavlakos,
Dandan Shan,
Ilija Radosavovic,
Angjoo Kanazawa, David Fouhey, and Jitendra Malik. Re-
constructing hands in 3d with transformers. In CVPR, 2024.
2
[88] Xue Bin Peng, Pieter Abbeel, Sergey Levine, and Michiel
Van de Panne.
Deepmimic: Example-guided deep rein-
forcement learning of physics-based character skills. ACM
TOG, 2018. 4
[89] Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, and
Angjoo Kanazawa.
Amp: Adversarial motion priors for
stylized physics-based character control. ACM TOG, 2021.
3, 4
[90] Xue Bin Peng, Yunrong Guo, Lina Halper, Sergey Levine,
and Sanja Fidler.
Ase: Large-scale reusable adversarial
11


<!-- page 12 (ocr) -->
skill embeddings for physically simulated characters. ACM
TOG, 2022. 3
[91] Sergey Prokudin, Christoph Lassner, and Javier Romero.
Efficient learning on point clouds with basis point sets. In
ICCV, 2019. 4
[92] Yuzhe Qin, Hao Su, and Xiaolong Wang. From one hand to
multiple hands: Imitation learning for dexterous manipula-
tion from single-camera teleoperation. RA-L, 2022. 3
[93] Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang,
Ruihan Yang, Yang Fu, and Xiaolong Wang. Dexmv: Im-
itation learning for dexterous manipulation from human
videos. In ECCV, 2022. 2, 3
[94] Yuzhe Qin, Wei Yang, Binghao Huang, Karl Van Wyk,
Hao Su, Xiaolong Wang, Yu-Wei Chao, and Dieter Fox.
Anyteleop: A general vision-based dexterous robot arm-
hand teleoperation system. In RSS, 2023. 3, 6, 2
[95] Realman Robotics.
RM Series.
https://www.
realman-robotics.com/rm-series123, 2010. 7
[96] Javier Romero, Dimitrios Tzionas, and Michael J. Black.
Embodied hands: Modeling and capturing hands and bod-
ies together. ACM TOG, 2017. 1, 3, 7, 2
[97] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-
net: Convolutional networks for biomedical image segmen-
tation. In MICCAI, 2015. 8
[98] Gerrit Schoettler, Ashvin Nair, Jianlan Luo, Shikhar Bahl,
Juan Aparicio Ojea, Eugen Solowjow, and Sergey Levine.
Deep reinforcement learning for industrial insertion tasks
with visual inputs and natural rewards. In IROS, 2020. 3
[99] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Rad-
ford, and Oleg Klimov. Proximal policy optimization algo-
rithms. arXiv preprint arXiv:1707.06347, 2017. 1, 3, 6
[100] Fadime Sener, Dibyadip Chatterjee, Daniel Shelepov, Kun
He, Dipika Singhania, Robert Wang, and Angela Yao. As-
sembly101: A large-scale multi-view video dataset for un-
derstanding procedural activities. In CVPR, 2022. 3
[101] Nur Muhammad Shafiullah, Zichen Cui, Ariuntuya Arty
Altanzaya, and Lerrel Pinto.
Behavior transformers:
Cloning k modes with one stone. NeurIPS, 2022. 8, 4
[102] Kenneth
Shaw,
Shikhar
Bahl,
and
Deepak
Pathak.
Videodex: Learning dexterity from internet videos.
In
CoRL, 2023. 2
[103] Kenneth Shaw, Yulong Li, Jiahui Yang, Mohan Kumar
Srirama, Ray Liu, Haoyu Xiong, Russell Mendonca, and
Deepak Pathak.
Bimanual dexterity for complex tasks.
arXiv preprint arXiv:2411.13677, 2024. 1
[104] Qijin She, Shishun Zhang, Yunfan Ye, Min Liu, Ruizhen
Hu, and Kai Xu. Learning cross-hand policies for high-dof
reaching and grasping. ECCV, 2024. 1
[105] Ken Shoemake. Animating rotation with quaternion curves.
In Proceedings of the 12th annual conference on Computer
graphics and interactive techniques, 1985. 4
[106] Tom Silver, Kelsey Allen, Josh Tenenbaum, and Leslie
Kaelbling.
Residual policy learning.
arXiv preprint
arXiv:1812.06298, 2018. 2, 3
[107] Omid Taheri, Nima Ghorbani, Michael J Black, and Dim-
itrios Tzionas.
Grab: A dataset of whole-body human
grasping of objects. In ECCV, 2020. 2, 3, 4, 6
[108] Bugra Tekin, Federica Bogo, and Marc Pollefeys. H+ o:
Unified egocentric recognition of 3d hand-object poses and
interactions. In CVPR, 2019. 2
[109] Chen Tessler, Yunrong Guo, Ofir Nabati, Gal Chechik,
and Xue Bin Peng. Maskedmimic: Unified physics-based
character control through masked motion inpainting. SIG-
GRAPH ASIA, 2024. 3
[110] A Vaswani. Attention is all you need. NeurIPS, 2017. 8
[111] Weikang Wan, Haoran Geng, Yun Liu, Zikang Shan,
Yaodong Yang, Li Yi, and He Wang. Unidexgrasp++: Im-
proving dexterous grasping policy learning via geometry-
aware curriculum and iterative generalist-specialist learn-
ing. In ICCV, 2023. 1, 2, 3
[112] Chen Wang, Linxi Fan, Jiankai Sun, Ruohan Zhang, Li Fei-
Fei, Danfei Xu, Yuke Zhu, and Anima Anandkumar. Mim-
icplay: Long-horizon imitation learning by watching hu-
man play. arXiv preprint arXiv:2302.12422, 2023. 2, 3
[113] Chen Wang, Haochen Shi, Weizhuo Wang, Ruohan Zhang,
Li Fei-Fei, and C Karen Liu. Dexcap: Scalable and portable
mocap data collection system for dexterous manipulation.
arXiv preprint arXiv:2403.07788, 2024. 1, 3
[114] Jun Wang, Yuzhe Qin, Kaiming Kuang, Yigit Korkmaz,
Akhilan Gurumoorthy, Hao Su, and Xiaolong Wang. Cy-
berdemo: Augmenting simulated human demonstration for
real-world dexterous manipulation. In CVPR, 2024. 3
[115] Ruicheng Wang, Jialiang Zhang, Jiayi Chen, Yinzhen Xu,
Puhao Li, Tengyu Liu, and He Wang.
Dexgraspnet: A
large-scale robotic dexterous grasp dataset for general ob-
jects based on simulation. In ICRA, 2023. 1
[116] Xinyue Wei, Minghua Liu, Zhan Ling, and Hao Su.
Approximate convex decomposition for 3d meshes with
collision-aware concavity and tree search.
ACM TOG,
2022. 4
[117] Philipp Wu, Yide Shentu, Zhongke Yi, Xingyu Lin, and
Pieter Abbeel. Gello: A general, low-cost, and intuitive
teleoperation framework for robot manipulators.
arXiv
preprint arXiv:2309.13037, 2023. 3
[118] Tianhao Wu, Mingdong Wu, Jiyao Zhang, Yunchong Gan,
and Hao Dong. Learning score-based grasping primitive for
human-assisting dexterous grasping. NeurIPS, 2024. 1, 3
[119] Wei Xie, Zhipeng Yu, Zimeng Zhao, Binghui Zuo, and Yan-
gang Wang. Hmdo: Markerless multi-view hand manipu-
lation capture with deformable objects. Graphical Models,
2023. 2, 3
[120] Yufei Xu, Jing Zhang, Qiming Zhang, and Dacheng Tao.
Vitpose: Simple vision transformer baselines for human
pose estimation. NeurIPS, 2022. 2
[121] Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu,
Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng, Yi-
jia Weng, Jiayi Chen, et al. Unidexgrasp: Universal robotic
dexterous grasping via learning diverse proposal generation
and goal-conditioned policy. In CVPR, 2023. 1, 2, 3
[122] Yufei Xu, Jing Zhang, Qiming Zhang, and Dacheng Tao.
Vitpose++: Vision transformer for generic body pose esti-
mation. IEEE TPAMI, 2023. 2
[123] Lixin Yang, Xinyu Zhan, Kailin Li, Wenqiang Xu, Jiefeng
Li, and Cewu Lu. Cpf: Learning a contact potential field to
model the hand-object interaction. In ICCV, 2021.
12


<!-- page 13 (ocr) -->
[124] Lixin Yang, Kailin Li, Xinyu Zhan, Jun Lv, Wenqiang Xu,
Jiefeng Li, and Cewu Lu. Artiboost: Boosting articulated
3d hand-object pose estimation via online exploration and
synthesis. In CVPR, 2022. 2
[125] Lixin Yang, Kailin Li, Xinyu Zhan, Fei Wu, Anran Xu, Liu
Liu, and Cewu Lu. Oakink: A large-scale knowledge repos-
itory for understanding hand-object interaction. In CVPR,
2022. 2, 3
[126] Lixin Yang, Jian Xu, Licheng Zhong, Xinyu Zhan,
Zhicheng Wang, Kejian Wu, and Cewu Lu. Poem: recon-
structing hand in a point embedded multi-view stereo. In
CVPR, 2023. 2
[127] Lixin Yang, Xinyu Zhan, Kailin Li, Wenqiang Xu, Junming
Zhang, Jiefeng Li, and Cewu Lu. Learning a contact poten-
tial field for modeling the hand-object interaction. IEEE
TPAMI, 2024. 2, 3
[128] Shiqi Yang, Minghuan Liu, Yuzhe Qin, Runyu Ding, Jia-
long Li, Xuxin Cheng, Ruihan Yang, Sha Yi, and Xiao-
long Wang. Ace: A cross-platform visual-exoskeletons sys-
tem for low-cost dexterous teleoperation. arXiv preprint
arXiv:2408.11805, 2024. 1, 3
[129] Jianglong Ye, Jiashun Wang, Binghao Huang, Yuzhe Qin,
and Xiaolong Wang. Learning continuous grasping func-
tion with a dexterous hand from human demonstrations.
RA-L, 2023. 3
[130] Zhao-Heng Yin, Binghao Huang, Yuzhe Qin, Qifeng Chen,
and Xiaolong Wang. Rotating without seeing: Towards in-
hand dexterity through touch. RSS, 2023. 1
[131] Haoqi Yuan, Bohan Zhou, Yuhui Fu, and Zongqing Lu.
Cross-embodiment dexterous grasping with reinforcement
learning. arXiv preprint arXiv:2410.02479, 2024. 1
[132] Kevin Zakka, Philipp Wu, Laura Smith, Nimrod Gileadi,
Taylor Howell, Xue Bin Peng, Sumeet Singh, Yuval Tassa,
Pete Florence, Andy Zeng, et al. Robopianist: Dexterous
piano playing with deep reinforcement learning.
CoRL,
2023. 3
[133] Yanjie Ze, Gu Zhang, Kangning Zhang, Chenyuan Hu,
Muhan Wang, and Huazhe Xu. 3d diffusion policy: Gener-
alizable visuomotor policy learning via simple 3d represen-
tations. In RSS, 2024. 1
[134] Xinyu Zhan, Lixin Yang, Yifei Zhao, Kangrui Mao, Han-
lin Xu, Zenan Lin, Kailin Li, and Cewu Lu. Oakink2: A
dataset of bimanual hands-object manipulation in complex
task completion. In CVPR, 2024. 2, 3, 4, 5, 6, 7
[135] Hui Zhang, Sammy Christen, Zicong Fan, Otmar Hilliges,
and Jie Song. Graspxl: Generating grasping motions for
diverse objects at scale. ECCV, 2024. 1, 2
[136] Hui Zhang, Sammy Christen, Zicong Fan, Luocheng
Zheng, Jemin Hwangbo, Jie Song, and Otmar Hilliges. Ar-
tigrasp: Physically plausible synthesis of bi-manual dexter-
ous grasping and articulation. In 3DV, 2024. 1
[137] Jiawei Zhang, Jianbo Jiao, Mingliang Chen, Liangqiong
Qu, Xiaobin Xu, and Qingxiong Yang. A hand pose track-
ing benchmark from stereo matching. In ICIP, 2017. 4
[138] Xiang Zhang, Changhao Wang, Lingfeng Sun, Zheng Wu,
Xinghao Zhu, and Masayoshi Tomizuka. Efficient sim-to-
real transfer of contact-rich manipulation skills with online
admittance residual learning. In CoRL, 2023. 3
[139] Shuqi Zhao, Xinghao Zhu, Yuxin Chen, Chenran Li,
Xiang Zhang, Mingyu Ding, and Masayoshi Tomizuka.
Dexh2r: Task-oriented dexterous manipulation from human
to robots. arXiv preprint arXiv:2411.04428, 2024. 2, 3
[140] Tony Z Zhao, Vikash Kumar, Sergey Levine, and Chelsea
Finn. Learning fine-grained bimanual manipulation with
low-cost hardware.
arXiv preprint arXiv:2304.13705,
2023. 3
[141] Licheng Zhong, Lixin Yang, Kailin Li, Haoyu Zhen, Mei
Han, and Cewu Lu. Color-neus: Reconstructing neural im-
plicit surfaces with color. In 3DV, 2024. 3
[142] Bohan Zhou, Haoqi Yuan, Yuhui Fu, and Zongqing
Lu.
Learning diverse bimanual dexterous manipula-
tion skills from human demonstrations.
arXiv preprint
arXiv:2410.02477, 2024. 3
[143] Zehao Zhu, Jiashun Wang, Yuzhe Qin, Deqing Sun, Varun
Jampani, and Xiaolong Wang.
Contactart: Learning 3d
interaction priors for category-level articulated object and
hand poses estimation. arXiv preprint arXiv:2305.01618,
2023. 3
[144] Christian Zimmermann, Duygu Ceylan, Jimei Yang, Bryan
Russell, Max Argus, and Thomas Brox. Freihand: A dataset
for markerless capture of hand pose and shape from single
rgb images. In ICCV, 2019. 4
13


<!-- page 14 (ocr) -->
MANIPTRANS: Efficient Dexterous Bimanual Manipulation Transfer
via Residual Learning
Supplementary Material
This appendix provides additional details and results that
complement the main paper. We first validate the extensibil-
ity of MANIPTRANS in Appendix A. We then evaluate the
robustness of MANIPTRANS under noisy conditions in Ap-
pendix B and analyze its time cost in Appendix C. Detailed
information on the settings of MANIPTRANS is provided
in Appendix D, along with statistics for the DEXMANIP-
NET dataset in Appendix E. Finally, we present the training
details for the rearrangement policies in Appendix F.
A. Further Extension of MANIPTRANS
A.1. Articulated Object Manipulation
We demonstrate the extensibility of MANIPTRANS by ap-
plying it to the ARCTIC dataset [32], which includes ap-
proximately 10 articulated objects, each with precise hand
manipulation trajectories for bimanual single-object manip-
ulation tasks.
To accommodate the articulated object manipulation
task, we extend our method pipeline. For a single articu-
lated object oA, we define its trajectory as T oA = {τ t
oA}T
t=1,
where τ oA = {poA, ˙poA, θoA, ˙θoA} represents the object’s
transformation, velocity, and the angle and angular velocity
of its articulated part. The reward function for articulated
objects, rt
objectA, includes two additional terms compared to
the reward for rigid objects: the angle difference |θoA −θ ˆ
oA|
and the angular velocity difference | ˙θoA −˙θ ˆ
oA|, where ˆoA
represents the collidable articulated object in the simulation
environment [79]. Apart from this modification, the rest of
the pipeline remains unchanged.
Qualitative results of MANIPTRANS applied to the
ARCTIC dataset are presented in Fig. 8, demonstrating
that our method successfully imitates human demonstra-
tions and rotates the articulated object to the desired target
angle. This highlights the extensibility of our pipeline when
the physical properties of the articulated object can be ac-
curately modeled in simulation.
A.2. Challenging Hand Embodiments
We investigate the generalization capabilities of MANIP-
TRANS across different hand embodiments in the main pa-
per. Here, we provide further details on adapting MANIP-
TRANS to a challenging hand model: the Allegro Hand [2],
which possesses K = 16 degrees of freedom. The chal-
lenges encountered stem from two primary factors: 1) the
Allegro Hand has only four fingers, a significant devia-
tion from the structure of the human hand, and 2) the Al-
Figure 8. Applying MANIPTRANS to Articulated Object Ma-
nipulation. In the first row, the two hands collaborate to not only
close the book but also place it stably on the table.
Figure 9. Extending MANIPTRANS to the Allegro Hand. De-
spite the Allegro Hand having only four fingers and a significantly
larger size, the transferred motion remains stable and natural.
legro Hand is approximately twice the size of a human
hand. These morphological discrepancies present substan-
tial challenges in transferring human demonstrations to the
Allegro Hand.
To address these challenges, we adaptively modify the
fingertip mapping relationships, mapping both the pinky
and ring fingers to the same fingertip on the Allegro Hand.
Additionally, we relax the fingertip keypoint threshold ϵfinger
to 8 cm to accommodate the larger dimensions of the Alle-
gro Hand. Successful application of MANIPTRANS to the
Allegro Hand is demonstrated in Fig. 9.
A.3. Discussion on the Extension
To summarize, we present all settings for the extension
experiments in Tab. 3.
The green checkmark (✓) indi-
cates the successful transfer of the dataset to the specified
hand embodiment, with results included in DEXMANIP-
NET. The blue checkmark (✓) denotes dataset verifica-
tion, where MANIPTRANS is tested on only a subset of the
dataset to assess generalizability. The results demonstrate
that our pipeline effectively accommodates various morpho-
logical differences across hand embodiments and supports a
1
fzzrtss
Hep Ose


<!-- page 15 (ocr) -->
Hands
Datasets
FAVOR [62]
OakInk-V2 [134]
GRAB [107]
ARCTIC [32]
Inspire [3]
✓
✓
✓
✓
Shadow [1]
✓
✓
✓
✓
Arti-MANO [96]
✓
✓
✓
✓
Allegro [2]
✓
✓
✓
✓
Table 3. Extensibility of MANIPTRANS. Arti-MANO refers to
the articulated MANO hand used in [27].
wide range of tasks, including single-hand manipulation, bi-
manual articulated object manipulation, and bimanual two-
object manipulation.
As discussed in Sec. 3.4 of the main paper, FAVOR [62]
and OakInk-V2 [134] represent the largest datasets with the
most diverse task types, while the Inspire Hand is distin-
guished by its high dexterity, stability, cost-effectiveness,
and extensive prior use [24, 35, 52]. Consequently, this
setup was chosen for collecting DEXMANIPNET. How-
ever, MANIPTRANS is fully adaptable, and we demonstrate
that all of the aforementioned MoCap datasets can be trans-
ferred to other robotic hands. We welcome further collabo-
ration from the research community.
B. Robustness Evaluation
MoCap data and model-based pose estimation results often
contain noise. To assess whether MANIPTRANS can reli-
ably transfer noisy real-world data into stable robotic mo-
tions within a simulation environment, we conduct robust-
ness tests. Since MANIPTRANS is designed for general-
purpose transfer and does not depend on task-specific re-
ward functions (e.g., the twisting reward proposed in [68]
for the lip-twisting task), noisy object trajectories may in-
troduce instability during the rollout process. Thus, to eval-
uate MANIPTRANS’s performance under such conditions,
we introduce random Gaussian noise into the hand trajec-
tory input and focus on single-hand manipulation tasks.
This choice is motivated by the fact that most hand pose
estimation methods [67, 124, 127] are optimized for single-
hand scenarios.
The results, presented in Tab. 4, demonstrate that MA-
NIPTRANS maintains acceptable performance even when
the noise level reaches up to 1.5 cm. These findings high-
light the potential of MANIPTRANS for real-world scaling,
particularly in applications involving hand pose estimation
Noise
Er ↓
Et ↓
Ej ↓
Eft ↓
SR ↑
+ σ = 0.5 cm
9.15
0.51
2.40
1.66
55.1 / 30.1
+ σ = 1.0 cm
9.56
0.57
2.87
2.13
55.3 / 19.5
+ σ = 1.5 cm
9.65
0.69
3.29
2.69
46.7 / 39.2
Table 4. Quantitative Results Under Different Noise Levels. We
add the Gaussian noise N(0, σ2) to the target hand joints poses.
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0
Time (minute)
0.2
0.4
0.6
0.8
1.0
Success Rate (%)
Ours
Retarget+Residual
RL-Only
Figure 10. Detailed Efficiency Comparison. The success rate
curves for the “rotating a mouse” task.
from web video data, which may implicitly contain a vast
array of dexterous manipulation skills.
C. Time Cost Analysis
In Sec. 4.3 of the main paper, we compare the efficiency
of our method with the previous SOTA method, QuasiSim.
QuasiSim employs a set of quasi-physical simulations, di-
viding the transfer process into three primary stages, with
each stage requiring approximately 10-20 hours for a 60-
frame trajectory 1.
Since MANIPTRANS also follows a
multi-stage framework, incorporating both a pre-trained
hand imitation module and a residual refinement module
tailored to physical dynamics, we provide a more compre-
hensive comparison of efficiency.
For a fair evaluation, we use the official QuasiSim demo
data for the “rotating a mouse” task as a representative ex-
ample. The success rate curves for three different settings,
as discussed in Sec. 4.3 of the main paper, are shown in
Fig. 10: 1) RL-Only: This approach trains the policy net-
work from scratch using RL with our reward design. The
curve illustrates the entire training process. 2) Retarget +
Residual Learning: Inspired by [139], this method retar-
gets human hand poses to initial dexterous hand poses via
keypoint alignment [94], followed by residual learning for
refinement. The retargeting process is performed via par-
allel optimization and only requires approximately several
minutes on a single GPU to optimize full sequence. The
training curve for the residual learning stage is represented
by the orange line. 3) MANIPTRANS: We pre-train the
hand imitation model on a large-scale training dataset, as
described in Sec. 3.2, which takes approximately 1.5 days
on a single GPU to obtain the reusable imitator. The resid-
ual learning stage training curve is shown by the blue line.
From the results in Fig. 10, we observe that for the rel-
atively simple task of “rotating a mouse”, the Retarget +
Residual method achieves performance comparable to MA-
NIPTRANS but requires slightly more time to converge.
The RL-Only approach, while yielding suboptimal perfor-
mance compared to the other methods, still produces ac-
1As reported in the official repository: https://github.com/
Meowuu7/QuasiSim
2
=—— mia


<!-- page 16 (ocr) -->
ceptable motions within 20 minutes. This indicates that our
reward design effectively accelerates the training process,
facilitating faster convergence.
D. Details of MANIPTRANS Settings
D.1. Correspondence Between Human Hand and
Dexterous Hand
Due to the significant morphological differences between
human hands and dexterous robotic hands, we manually
establish correspondences between them. For the human
hand’s fingertip keypoints, we select the midpoint of the
three tip anchors as defined in [127].
For the dexterous
hands, given their varying shapes, we define the fingertip
keypoints as the points of maximum curvature along the
central axis of the finger pads, as these points are most likely
to contact objects. For other keypoints, such as the wrist
and phalanges, we intuitively align the rotation axes of the
human joints with those of the robotic joints. For further
details, please refer to our code implementation.
In addition, regarding the articulated MANO model, the
original human hand model MANO [96] has 45-DoF, which
presents extreme challenges for RL-based policies due to
the vast exploration space. To mitigate this, we follow the
approach in [127] by constraining certain DoFs and fix-
ing the hand collision meshes, thereby reducing the original
MANO model to a 22-DoF articulated MANO.
D.2. Details of Training Parameters
In this section, we present the core parameters of our re-
ward functions in MANIPTRANS. The reward parameters
for rt
finger in Eq. (1) of the main paper are summarized in
Tab. 5. These parameters are determined based on the ob-
servation that the thumb, index, and middle fingers play a
pivotal role in grasping and manipulation tasks, as they sta-
tistically interact with objects more frequently than other
fingers [9, 10, 134]. Consequently, the weights are assigned
according to the contact frequency. In our implementation,
if a dexterous hand lacks a specific finger or joint (e.g., the
Inspire Hand does not have distal joints), the corresponding
Figners
weight wf
decay rate λf
Thumb
0.5, 0.3, 0.3, 0.9
50, 40, 40, 100
Index
0.5, 0.3,0.3, 0.8
50, 40, 40, 90
Middle
0.5, 0.3,0.3, 0.75
50, 40, 40, 80
Ring
0.5, 0.3,0.3, 0.6
50, 40, 40, 60
Pinky
0.5, 0.3,0.3, 0.6
50,40, 40, 60
Table 5. Hyperparameters for the Finger Reward. The weight
wf and decay rate λf are used to balance the importance of each
finger. Each cell in the table contains four values, representing the
parameters for the proximal, intermediate, distal, and tip joints,
respectively. For anatomical definitions, please refer to [127].
parameters are set to zero. For the contact reward rt
contact in
Eq. (2) of the main paper, we set both parameters, wc and
λc, to 1.
D.3. Details of Simulation Parameters
In the Isaac Gym environment, configuring physical prop-
erties significantly influences the success rate of transfer.
Alongside domain randomization (DR) during training, we
set physical constants as follows.
For certain objects in
OakInk-V2 [134], we obtained actual masses by directly
measuring them in collaboration with the dataset authors.
For the remaining objects, we assigned a constant density of
200 kg/m3, approximating the average density of low-fill-
rate 3D-printed models. Using this density, we recalculated
the objects’ masses and moments of inertia.
It is worth noting that human skin is elastic. When grasp-
ing objects, fingertip skin undergoes slight deformations,
enhancing contact with object surfaces and generating suit-
able friction, whereas dexterous robotic hands lack this be-
havior. Previous kinematics-based grasp generation meth-
ods [50, 61] often permit slight penetration between finger-
tips and object surfaces to improve interaction stability (for
detailed discussion, please refer to [50]). Therefore, to com-
pensate for the absence of skin deformation in simulation,
we set the friction coefficient F slightly higher than the real-
world value. Accurately simulating contact-rich scenarios
remains an area for future exploration.
E. DEXMANIPNET Statistics
To the best of our knowledge, no prior work has collected a
large-scale bimanual manipulation dataset in which all tra-
assemble, brush whiteboard, cap, cap the pen,
close book, close gate, close laptop lid,
cut, flip close tooth paste cap,
flip open tooth paste cap, heat beaker, heat test
tube, hold, hold test tube, ignite alcohol lamp,
insert lightbulb, insert pencil, insert usb,
open gate, open laptop lid, place asbestos mesh,
place inside, place on test tube rack, place
onto, place test tube on rack with holder,
plug in power plug, pour, pour in lab,
press button, put flower into vase,
put off alcohol lamp, put on lid, rearrange,
remove from test tube rack, remove lid,
remove pencil, remove power plug,
remove test tube, remove test tube from
rack with holder, remove the pen cap,
remove usb, scoop, scrape, screw, shake
lab container, sharpen pencil, shear paper,
spread, squeeze tooth paste, stir,
stir experiment substances, swap, take outside,
trigger lever, uncap, uncap alcohol lamp,
unscrew, use mouse, wipe, write on paper,
write on whiteboard
Table 6. List of tasks in the DEXMANIPNET dataset. Tasks with
underlined names usually require bimanual manipulation.
3


<!-- page 17 (ocr) -->
Figure 11. Qualitative Results of Rearrangement Policy Learn-
ing. The policy successfully moves the bottle to the goal position.
Results are directly visualized in the IsaacGym environment, high-
lighting distinctions between these policies and MANIPTRANS’s
rollouts.
jectories are directly transferred from real human demon-
strations without the use of teleportation. Leveraging the ef-
ficiency and precision of MANIPTRANS, our dataset, DEX-
MANIPNET, comprises 3.3K diverse manipulation trajec-
tories across 61 distinct tasks, as detailed in Tab. 6. To en-
sure stability during simulation, we fix the object meshes to
a watertight state using ManifoldPlus [47] and may slightly
adjust the object size to enhance object-object interactions
(e.g., the cap and body of the bottle).
Additionally, we provide sample data on our website,
showcasing trajectories generated from our policy in sim-
ulation. A simple first-order low-pass filter (α = 0.4) is
applied to the rollouts, effectively reducing jitter with mini-
mal impact on tracking accuracy.
F. Details of Rearrangement Policy Learning
As discussed in Sec. 4.7 of the main paper, we benchmark
DEXMANIPNET using four data-driven imitation learning
methods on the moving a bottle to a goal position task.
The primary challenge in this task is to enable the dex-
terous hand to maintain a stable grasp on the object while
smoothly placing it at the specified goal position. We eval-
uate the dataset using four methods: IBC [33], BET [101],
and Diffusion Policy [25], which include both UNet- and
Transformer-based architectures. These policies are trained
for 500 epochs using the Adam optimizer with a learning
rate of 1 × 10−4, while all other hyperparameters remain at
their default settings.
The dimensions of the observation and action spaces for
these policies are provided in Tab. 7. The observation space
includes the current object state {pˆo, ˙pˆo}, the hand wrist
state {wd, ˙wd}, hand joint angles qd, and the goal poses
for both the object gˆo and the hand wrist gw. The action
a = {aq, aw} ∈A specifies the target hand joint angles
and wrist poses using a PD controller. Note that PD control
is used for wrist poses rather than a 6-DoF force, as is done
in MANIPTRANS.
We evaluate the policies’ performance on previously un-
seen goal positions within the IsaacGym environment [79].
A rollout is considered successful if the object’s distance
from the goal position is within 10 cm; otherwise, it is
classified as a failure. Qualitative results are presented in
Fig. 11, while quantitative results are summarized in Tab. 2
of the main paper.
Observation
Dimensions
Hand joint angles q
12
Hand wrist state {wd, ˙wd}
13
Object state {pˆo, ˙pˆo}
13
Object pose goal gˆo
7
Hand wrist pose goal gw
7
(a) Observation space.
Action
Dimensions
Hand joint angles aq
12
Hand wrist pose aw
7
(b) Action space.
Table 7. Observation and Action Definitions for the Imitation
Policy. The policy’s 7-dimensional pose includes both position
and orientation, represented as XYZW quaternions. The policy’s
13-dimensional state extends this pose by incorporating both linear
and angular velocities.
4
p——
TO — —
- =
((®
>
—
—_—
o ra—
- —
ES
y
ry
A
—
4
&
-
