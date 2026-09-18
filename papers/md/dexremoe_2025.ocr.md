<!-- page 1 (ocr) -->
1
DexReMoE:In-hand Reorientation of General
Object via Mixtures of Experts
Jun Wan, Xing Liu, Yunlong Dong†
https://wj-0212.github.io/
Abstract—In hand object reorientation provides capability
for dexterous manipulation, requiring robust control policies to
manage diverse object geometries, maintain stable grasps, and
execute precise complex orientation trajectories. However, prior
works focus on single objects or simple geometries and struggle to
generalize to complex shapes. In this work, we introduce DexRe-
MoE (Dexterous Reorientation Mixture-of-Experts), in which
multiple expert policies are trained for different complex shapes
and integrated within a Mixture-of-Experts (MoE) framework,
making the approach capable of generalizing across a wide
range of objects. Additionally, we incorporate object category
information as privileged inputs to enhance shape representation.
Our framework is trained in simulation using reinforcement
learning (RL) and evaluated on novel out-of-distribution objects
in the most challenging scenario of reorienting objects held in
the air by a downward-facing hand. In terms of the average
consecutive success count, DexReMoE achieves a score of 19.5
across a diverse set of 150 objects. In comparison to the
baselines, it also enhances the worst-case performance, increasing
it from 0.69 to 6.05. These results underscore the scalability and
adaptability of the DexReMoE framework for general-purpose
in-hand reorientation.
I. INTRODUCTION
Dexterous manipulation has advanced for a few objects [1–
3], yet realizing generalizable dexterous manipulation remains
a significant challenge in robotics [4]. In daily life, humans
rely heavily on the remarkable versatility of their hands to
perform tasks such as rearranging objects, loading dishes,
tightening bolts, and slicing vegetables. Replicating this level
of control in robotic systems is still extremely difficult [5]. At
the heart of this problem lies in-hand object reorientation. A
robot must be able to take an object presented in any initial
pose and rotate it precisely to a desired target orientation. The
ability to reliably reorient objects is crucial for flexible tool
use. For example, a screwdriver must be correctly aligned with
a screw before it can function properly. By focusing on this
fundamental skill, we take a step closer to equipping robots
with the adaptability and precision of the human hand.
Recently, the development of RL [6–8] has paved the
way for significant advances in dexterous manipulation re-
search [1, 9]. In 2018, OpenAI [1] demonstrated that a purely
end-to-end deep RL pipeline could endow a multi-fingered
†Corresponding author.
Jun Wan and Xing Liu are with School of Artificial Intelligence and Au-
tomation, Huazhong University of Science and Technology, Wuhan 430074,
China
Yunlong Dong is with Department of Automation, Tsinghua University,
Beijing 100084 (e-mail: yunlongdong@mail.tsinghua.edu.cn)
robotic hand with unprecedented dexterity in contact-rich in-
hand manipulation tasks, sparking a surge of interest despite
the complexity of their sim-to-real transfer approach.. Building
on this, DeXtreme [2] was introduced as a vision-based system
trained in Isaac Gym [10] with extensive domain randomiza-
tion and a learned pose estimator, successfully transferring
agile reorientation policies from simulation to an Allegro
Hand in the real world. Meanwhile, rapid motor adaptation
relying exclusively on proprioceptive history and training on
simple cylindrical objects enabled a fingertip-only controller
to rotate dozens of diverse real objects about the z-axis
without further fine-tuning, with stable finger gaits emerging
naturally [3]. More recently, the Visual Dexterity framework,
driven by a depth camera and capable of reorienting novel,
complex shapes over multiple axes in real time, was presented,
demonstrating generalization to unseen geometries under grav-
ity [11]. Despite these remarkable advances, reliably reorient-
ing complex objects under generalized conditions remains a
formidable challenge [11].
By leveraging transfer learning, robotic systems can gener-
alize policies learned on a limited object set to novel scenarios
with minimal additional supervision [12]. The most common
strategy is fine-tuning, in which pretrained parameters are
adapted using only a few target-task examples. However, fine-
tuning typically tailors policies to individual objects and can
overwrite previously acquired skills, leading to catastrophic
forgetting and limiting robustness across diverse geometries.
Domain adaptation techniques [1, 2] have also been investi-
gated, but these methods focus on closing the sim-to-real gap
rather than on handling substantial variation in object shape.
Another challenge is to extract meaningful object features,
particularly shape information, in a computationally efficient
manner. Training directly on each object’s full point cloud can
capture detailed geometry [11], but the large number of points
slows learning and increases resource demands. To address
these issues, we adopt a low-dimensional extrinsics embedding
that encodes each object’s critical properties (local surface
geometry, mass distribution and pose) into a concise vector.
We then extend this embedding by incorporating a point-
cloud-based shape encoding together with a one-hot category
vector [3]. This representation provides the controller with a
unified and expressive view of each object’s physical attributes
while the category information helps the router assign expert
weights more effectively.
In extensive simulation experiments involving more than
hundreds of complex object models, our DexReMoE surpasses
monolithic baselines in consecutive success count, conver-
arXiv:2508.01695v1  [cs.RO]  3 Aug 2025


<!-- page 2 (ocr) -->
2
Fig. 1: Visualization of DexReMoE in action. Left: the router adaptively allocates weights to expert policies according to
the object’s geometry, enabling a coordinated action generation by multiple experts. Right: temporal evolution of in-hand
reorientation under the same policy, showing smooth and precise rotation over time.
gence speed, and resistance to disturbances. Moreover, it
maintains these advantages when tested on objects outside the
training distribution, demonstrating strong generalization and
stability. These results show that a policy formed by combining
multiple expert strategies and using an extrinsics embedding
to encode object features can effectively tackle the challenging
task of in-hand manipulation for objects with complex shapes.
In light of the above, generalizing in-hand reorientation to
objects with complex shapes is still an outstanding challenge
in dexterous manipulation, our work proposes a new direction
for improving generalization (Figure 1). We will release our
codebase and simulation environment to facilitate further re-
search in dexterous manipulation. In the following sections, we
first review related work on object reorientation and mixture
of experts methods, then describe the proposed architecture
and training procedure in detail, and finally present a compre-
hensive experimental evaluation and analysis.
The main contributions of this paper are summarized as
follows:
1) We propose DexReMoE for in-hand reorientation, en-
abling assignment of suitable expert policies based on
object geometry to accomplish the reorientation task.
This framework learns a unified control policy that
achieves reliable and precise in-hand repositioning.
2) We propose a novel object shape representation that
integrates point-cloud encoding with a one-hot category
vector within the existing input decoupling framework.
We then fuse this enhanced shape descriptor with phys-
ical properties and compress the combined features into
a compact vector using a low-dimensional extrinsics
embedding. This enriched representation significantly
increases the expressiveness of object features.
3) We evaluate our method on over hundreds of objects
with significant shape variation, both within and out-
side the training distribution. Performance is measured
by consecutive success counts. Extensive experimental
results for comparison and ablation study demonstrate
the effectiveness of the proposed method.
II. RELATED WORK
In-Hand Dexterous Reorientation. In-hand dexterous reori-
entation has been an active research area for decades [1, 2,
4, 5, 11, 14–17], with its core challenge lying in the precise
coordination of finger motions to reposition, regrasp, and roll
objects within constrained grasps. Early model-based methods
planned stable finger trajectories using analytical representa-
tions of object and hand geometry [14], but their applicability
remained limited by the complexity of real-world physics
and the diversity of objects. More recently, reinforcement
learning has emerged as a promising approach for complex
in-hand tasks. Prior work has focused either on continuous
rotations around a single axis [4, 16], or on multi-axis spins
tailored to specific objects [1, 5, 17]. Studies that incorpo-
rate visual inputs [11] demonstrate that a single policy can
manipulate multiple distinct objects, including those unseen
during training. However, such experiments typically involve
regular shapes and demand substantial training resources,
so reorienting objects with complex geometries remains a
significant challenge. To address this, we introduce a MoE
framework consisting of a gating network and multiple expert
policies, which dynamically select the most suitable expert
according to object geometry to achieve reliable reorientation.
Shape Representation in Reorientation. Accurate encod-
ing of object geometry plays a critical role in any in-hand
reorientation system. The dual demands of computational
efficiency and policy generalization make it an open problem
for dexterous hand manipulation. Prior work often sidesteps
this challenge by choosing a single simple object. For example,
Dextreme [2] focuses exclusively on a cube and therefore
requires no explicit shape encoding, but it cannot extend to
other geometries. Visual Dexterity [11] employs raw point
clouds to represent shape, yet the sheer volume of points drives
up computation and fails on highly symmetric objects, since
point-cloud views remain unchanged under many rotations.
Recently, purely tactile approaches learn a shape agent from
fingertip torques and joint positions [18], but it demand very
high-fidelity sensors. In contrast, our method extracts compact
point-cloud features via PointNet++ [13], combine them with
a one-hot object categories vector, and produces a lightweight
MOE reorientation Policy
Time
Start
Bp) 2%,
Goal
|
i
ow
Router Experts |
7
’
:
a
Zz
:
£ Foy
Zz
A
I
y
:
>
%
[=>
[ll
~G¥
Nim
LAE
C8
Os
fi)
7
\
i
vs
= wi |
:
EN
NS \Tp
pd
vp Ngo
ny
Start
Goal
|
Expensl|
7°
i
~
a
i ¢
Router Exper? 0
Y
;
£, =F
Z
TR
7 ME)
fA
4 4
J
Experss|
2%
4
ll FR. | io
.
Il
Sa
dd]
DES
2B
>
pid 20%,
i
a>
hi
\) -
h
~~
EY
LY


<!-- page 3 (ocr) -->
3
Fig. 2: An overview of our model across training. In Base Policy Learning, we jointly train the perception backbone µpc(based
on PointNet++ [13]), µe and generalist policy πbase, using observations ot that include the last three joint positions, commanded
actions. Next, in Experts Policy Training: We fine-tune πbase to obtain four expert policies {πei}n
i=1. Then, in MoE Policy
Training: We freeze the µpc, µe, and all πei. Only the soft routing network πgate is trained to infer per-expert weights from
the mesh feature embedding and object-category vector, and to compute the final action via a weighted sum of the experts’
outputs.
expressive embedding suitable for general dexterous reorien-
tation.
Mixture of Experts. MoE was originally introduced in
[19, 20], combining multiple specialized expert networks with
a trainable gating module that adaptively weights each expert’s
output [21, 22]. Recent advances in large language models
have leveraged sparse MoE layers to route tokens dynam-
ically into dedicated subnetworks, yielding both modularity
and highly scalable inference [23, 24]. In RL, early studies
demonstrated that ensembles of expert policies can capture
complementary action distributions [25, 26], and more recent
work has leveraged MoE to advance multi-task learning in
robotics, highlighting its effectiveness in coordinating diverse
control objectives [27, 28]. In this research, we adopt the MoE
framework to diversify redirection strategies in a multi-task
dexterous manipulation setting. Each expert is trained on a
single shape category to develop its own redirection behavior,
thereby fostering broad generalization across varied object
geometries.
III. IN HAND REORIENTATION WITH MOE
We begin this section by outlining the overall system archi-
tecture in Section III-A. Subsequently, we detail the training
process for the base policy in Section III-B, and conclude with
the description of the MoE training procedure in Section III-C.
A. DexReMoE
We propose DexReMoE, a framework that combines cat-
egory specific expert fine-tuning with shared encoder rep-
resentations and MoE to provide versatile and efficient in-
hand reorientation across diverse object geometries. Figure 2
illustrates an overview of our framework.
Multi-Task Reinforcement Learning Framework. RL for-
mulates sequential decision making as a Markov Decision
Process M = (S, A, P, r, γ), where S and A denote the
Base Policy Training
Physics Parameters|
Poliey
Object Categories
Object Encoder
Policy
Hpe
]
n
Point cloud
|
|
Object Mesh
Encoder
Mesh feature
!
|
i
i
i
I
i
|
Experts Policy Training
I
EE
—
i
i
i"
-
<7 Experts
:
1
Physics Parameters
v
V
i
He
fad
Y;
v
Object Categories
Object Encod
Contorl
he
od
<r
i
Policy
a |——
-
oint cloug
)
&
IH
In
1
il
)
Lo
1
Mixtures of Experts Policy
i
i
Experts]
i
Training
i
_ou
=
i
i
-
1
!
i
| !
Experts2
>(af’]
i
ih
_—
i
i"
i
-- (a2 ]—
| |
i
Experts3
i
>(af?
fa)
_1
|
1
¥
Experts4
Ly
es
iH
Physics Parameters
:
v
t=
a,’
J—
]
|
He
Te
!
Object Categories
Object Encoder
Contorl | |—r
}
.
Policy
x3
i
L
i
Hye
[poate
i
n
Point cloud
Gati
|
>
Object Mesh
ating [IE(a
—==>
)
Encoder
Network
|~~
.
~>
Fine-tunin
&
jam.
e-1
2
(Object Categories
CZZZZ22> Combine Weights


<!-- page 4 (ocr) -->
4
state and action spaces, P(s′ | s, a) the transition probability,
r(s, a, s′) the immediate reward, and γ ∈(0, 1) the discount
factor. A stochastic policy πθ(at | st), parameterized by θ,
defines a distribution over actions given the current state. The
learning objective is to identify parameters θ∗that maximize
the expected discounted return as:
J(θ) = Eπθ
∞
t=0
γt r(st, at, st+1) .
In the standard single-task RL setting, an agent selects its
action at time t according to:
at = π(st),
where st denotes the current state and π is the learned policy.
To accommodate a diverse set of object geometries, we treat
each substantially different shape category as an individual
task. In conventional multi-task reinforcement learning, differ-
ent tasks may have distinct objectives, reward formulations, or
transition dynamics, even if they share the same state–action
space. In contrast, our formulation employs a unified reward
function and identical state representations across all tasks.
Accordingly, we construct our overall policy by combining
the outputs of n specialized sub-policies:
at = g π1(st), π2(st), . . . , πn(st) ,
where g denotes a generic aggregation function that determines
how the individual policies are integrated into a single action.
In this work, we investigate both the design of the aggregation
mechanism g within a multi-task context and the selection of
state representations st that most effectively capture inter-task
shape variations.
DexReMoE System. An overview of our system architecture
is provided in Figure 2. The learning process is divided into
two stages: base policy training and the subsequent MoE
policy training phase.
In the first stage, we jointly train a base control policy πbase,
a point cloud encoder µpc, and an object encoder µe using data
collected from all object categories. The point cloud encoder
extracts geometric features from raw object meshes, while the
object encoder fuses these features with auxiliary information,
such as object class and physical parameters, to produce a
compact object representation. This representation, together
with the current observation, is fed into the base policy to
generate control actions.
Once training converges, we freeze both encoders and
initialize a set of expert policies {πei}4
i=1 using the parameters
of the base policy. Each expert is then fine-tuned on data
restricted to a specific shape category, allowing it to specialize
in manipulation behaviors tailored to a particular class of
geometries. Notably, the policy inputs remain consistent across
both training stages, enabling the pre-trained encoders to be
reused without modification during expert specialization.
During deployment, a lightweight gating network is used to
adaptively blend the outputs of the specialized experts. The
gating module takes as input the object representation and a
category vector, and produces a set of weights that indicate the
relative importance of each expert. The final action is obtained
by computing a weighted sum over the expert outputs. This
modular design achieves both targeted specialization and broad
generalization across diverse object shapes.
B. Base Policy Training
Privileged Information. Privileged information at time t is
the concatenation of the object’s physical state ephys
t
∈R23
and its shape descriptor eshape
t
∈R38. The physical state
is ephys
t
= [ m,
c,
f,
s,
xt,
qt,
vt,
ωt ], where m
is mass, c center of mass, f friction coefficient, s uniform
scale, xt position, qt orientation quaternion, vt linear velocity,
and ωt angular velocity. To obtain the shape descriptor, we
sample the object’s point cloud and apply PointNet++ [13] to
extract a 100-dimensional feature pt. A learned point-cloud
encoder µpc then maps pt to a 32-dimensional embedding ft.
Appending the six-dimensional one-hot category vector c ∈
{0, 1}6 produces eshape
t
= [ ft, c ]. Concatenating ephys
t
and
eshape
t
yields the full privileged vector et = [ ephys
t
, eshape
t
],
which is passed through an encoder µe to produce the 66-
dimensional embedding zt = µe(et). The resulting embedding
zt = µe(et) serves as the policy’s privileged input. We
refer to zt as the extrinsics embedding and observe that it
significantly enhances generalization across diverse objects
and environments.
Observations and Outputs. In our formulation, we define
the policy input state as the combination of the robot’s
proprioceptive observation ot and a privileged object en-
coding zt. This composite representation captures both the
robot’s recent behavior and essential object-specific infor-
mation. The base policy πbase receives this full state and
produces an action at to be executed by the PD controller.
Specifically, the observation ot encodes a short temporal
window of joint positions and previously applied actions:ot =
qt−2, qt−1, qt, at−3, at−2, at−1 , where each qt denotes
the joint positions at time t, and at−k refers to the executed
action at time t −k. The policy output is then given by:
at = πbase ot, zt . To improve the smoothness of control, we
apply exponential moving average to the action outputs rather
than using them directly: at = α at + (1 −α) at−1 where
α ∈[0, 1] is a smoothing coefficient. Empirically, we observe
that smaller values of α lead to increased training difficulty
due to diminished action responsiveness.
Reward Function. Our reward function (Eq. (1)) is com-
posed of several components. The first term in the reward
function represents the task’s success criterion; within a fixed
time horizon, each successful placement of the object at the
target location yields a reward, and accumulating multiple
successes encourages the dexterous hand to perform consec-
utive repositioning operations. However, this success-based
reward alone is sparse and provides limited learning signals,
making it insufficient for stable policy learning. To address
that, we incorporate additional reward shaping terms to guide
the learning process. Specifically, we penalize the relative
distance |δp| and orientation difference |δθ| between the object
and the target pose to encourage the agent to minimize
both positional and rotational discrepancies . Moreover, we
introduce a penalty on action magnitude and joint velocities
>
|


<!-- page 5 (ocr) -->
5
to further promote smoother control. The reward terms are
mathematically expressed as:













r1 = csuccess
r2 = cdist · |δp| +
crot
|δθ| + ϵ
r3 = cω
n
i=1
[|ωi,t| −ωclip]+ + ca · ∥at∥2
2,
(1)
where csuccess > 0 is the reward for reaching the target;
cdist, crot, cω, ca < 0 are penalty weights; ϵ prevents division
by zero; n is the hand’s degrees of freedom; ωi,t is the angular
velocity of joint i at time t; ωclip is the velocity threshold; and
at is the action vector at time t.
The total reward at each timestep is then defined as:
R = r1 + r2 + r3.
(2)
Our reward function does not include the penalty for the
object falling, as we found during experiments that such a term
suppresses exploratory actions and adversely affects the overall
training performance. The proposed reward function enables
direct training of reorientation policies capable of operating in
air.
Policy Optimization. We employ Proximal Policy Optimiza-
tion [29] to simultaneously train both the policy πbase , the
embedding module µe and µpc . The weights between the
policy and the critic network are shared, with an extra linear
projection layer to estimate the value function. During training,
each environment is initialized with an object in a random
pose. Since our training directly targets in-air object manip-
ulation, we initialize the dexterous hand with a stable grasp
configuration to ensure faster convergence during training.
C. MoE Training
To accommodate the full spectrum of object geometries,
from perfectly flat surfaces and slender elongated forms to
highly intricate topologies, we enhance our base reorientation
policy with a MoE architecture. Rather than relying on a single
network to cover all shape variations, we introduce multiple
specialist sub-networks, each dedicated to capturing specific
geometric features. the gating network assigns each expert a
continuous weight based on the object’s geometry, and the final
control action is obtained by computing the weighted average
of all expert outputs.
Expert Knowledge. Each expert policy is realized as an
independent neural network with its own parameter set, which
enables specialization in distinct regions of the shape-action
manifold. By decoupling representation learning across ex-
perts, we avoid forcing a monolithic policy to cover all geo-
metric variations simultaneously. The total number of experts
n is determined by the intrinsic correlations among object
classes rather than by the count of objects, thereby preventing
model complexity from scaling linearly with dataset size.
In our implementation, four experts share a frozen point-
cloud encoder µpc to preserve a common perceptual backbone
while each expert refines only its private policy head. The
generalist expert is fine-tuned on a broad set of object shapes to
provide baseline reorientation capabilities; the airplane expert
specializes in handling elongated, discontinuous surfaces; the
train expert focuses on slender structures with high aspect
ratios; and the complex animal expert is designed to manage
non-uniform surfaces and intricate topologies. This modular
framework supports efficient extension or pruning as new
shape categories emerge without retraining the entire ensem-
ble.
Task-Specific Feature Extraction and Soft Router Formu-
lation. We designate the object’s geometry as the sole task-
specific feature, encoded by a compact shape descriptor eshape
t
.
This choice ensures that the extracted features capture the most
salient, discriminative aspects of each object while remaining
invariant throughout the reorientation process, thereby simpli-
fying policy optimization and improving convergence. Con-
cretely, eshape
t
is obtained by fusing a point-cloud encoding
with a one-hot category vector and compressing the result via
a low-dimensional extrinsics embedding.
The gating network πgate maps the shape descriptor eshape
t
to a vector of scores, these scores are normalized via softmax
to yield nonnegative weights, which we then use to perform a
weighted aggregation of the experts’ outputs. We demonstrate
in the following chapter through experiments that this dense
soft gating converges much more reliably than hard Top-
K routing, since it avoids abrupt switches between experts
and better accommodates sparse reward signals. To clarify
the underlying mathematical structure of this mechanism, we
introduce the notation and steps of the algorithm. Formally,
let eshape
t
∈Rd denote the shared descriptor vector and
{fi}n
i=1 be our n expert mappings fi : Rd →Rh. The
gating network πgate is implemented as a two-layer MLP with
learnable weight matrices W1 ∈R64×d and W2 ∈Rn×64,
using the ELU [30] activation function between layers. The
Soft Mixture-of-Experts algorithm then proceeds as follows:
1) Gating network. Compute unnormalized expert scores
ℓi = W2 ELU(W1 eshape
t
) i,
i = 1, . . . , n,
and normalize to obtain routing weights
pi =
exp(ℓi)
n
j=1 exp(ℓj).
2) Expert evaluations. Each expert produces
yi = fi(x)
3) Soft aggregation. The final output is
y =
n
i=1
pi yi.
IV. EXPERIMENT
We first describe the experimental setup in Section IV-A. In
Section IV-B, we present our evaluation metrics and baseline
methods for quantitative comparison. Next, in Section IV-C,
we introduce the simulator-state-based base policy and evalu-
ate how object geometry affects its performance. In particular,
we analyze how variations in shape complexity influence the
policy’s convergence and robustness across a wide range of
bh
>
bh


<!-- page 6 (ocr) -->
6
objects. In Section IV-D, we report ablation studies on various
design choices. Then, we examine the limitations of the
base policy when dealing with objects of complex geometry
and present our proposed MOE framework, emphasizing its
performance benefits in Section IV-E. Finally, Section IV-F
uses t-SNE to cluster the gating network’s weight vectors,
revealing distinct regions for varied shape complexities and
coherent groupings for similar geometries.
A. Experiment Setup
Simulation Setup. We employ the IsaacGym simulator [10]
to train our skill policy, planner policy and state estimator.
Both simulation and control frequencies are set to 60 Hz.
During training, we run 32768 parallel environments to col-
lect samples for agent training. Related approaches typically
perform object reorientation on a tabletop or with the palm
oriented upward. In contrast, our configuration executes fully
mid-air reorientation with the palm directed downward. This
arrangement is significantly more complex and prone to fail-
ure, making the task more challenging. In our experiments,
we adhere to the standard protocol by reorienting objects
entirely in mid-air with target orientations randomly sampled
from the SO(3) space using our custom GX11 three-fingered
dexterous hand [31], a manipulator with eleven degrees of
freedom.We train on a dataset of 150 object models sourced
from online repositories such as Google Scanned Objects [32].
These models span a broad spectrum of intricate nonconvex
geometries, including vehicles, footwear and various animal
forms, ensuring comprehensive coverage of complex shape
categories.
Reorientation Success Criterion. We quantify manipulation
performance by counting the number of consecutive successful
reorientations achieved within each fixed time window. A
straightforward criterion that declares success whenever the
orientation error falls below a specified tolerance can be
misled by incidental collisions that briefly align the object
with its target pose. To eliminate these false positives, we
require both precise orientation and a sustained halt at the
desired configuration. At each control step, the reach criterion
is considered satisfied only when the rotational distance to
the goal is less than or equal to τθ, each finger joint velocity
remains below τq, the object’s linear velocity stays under τv,
and its angular velocity does not exceed τω.
To guard against transient alignment, we enforce that all
four conditions hold continuously throughout the final control
cycle of the episode. A reorientation is deemed successful only
when this sustained-hold criterion is met, ensuring the policy
learns precise alignment and stable maintenance rather than
relying on incidental collisions. This capability is essential in
real-world tasks where the robot must maintain a tool’s pose
for subsequent actions.
B. Evaluation Metrics and Baseline Methods.
To evaluate the performance of the proposed DexReMoE
algorithm, we employ five summary metrics, denoted as fol-
lows:
Fig. 3: Top: the five worst-performing objects with their con-
secutive success counts ¯S. Bottom: the five best-performing
objects.

































Smin = min
i
Si
Smax = max
i
Si
¯S5−= 1
5 i∈W5
Si
¯S5+ = 1
5 i∈B5
Si
¯S = 1
N
N
i=1
Si,
(3)
where, Si denotes the consecutive success count for object i,
W5 and B5 are the index sets of the five lowest- and highest-
performing objects respectively, and N is the total number of
test objects. Table I reports these five metrics for all evaluated
methods.
To verify the superiority of our method, we use the follow-
ing RL algorithms as baselines: 1) the ideal policy trained
with Domain Randomization (DR) by OpenAI [1]; 2) the
Privileged Feature (PrivFeat) policy [3], which uses privileged
physical state information in place of raw observations; 3) the
Privileged Shape (PrivShape) policy [4], which incorporates
additional object shape information (e.g., point clouds) as priv-
ileged input; 4) the Adaptive Domain Randomization (ADR)
policy [2], which adjusts domain parameters based on task
performance; 5) the Residual Actions (Res) policy [33], which
learns a residual correction on top of a pre-trained base policy
for high-dimensional dexterous hand control ;6) the Sparse
Mixture-of-Experts (SparseMoE) policy [21], which activates
a sparse subset of experts via a noisy gating network; 7) the
Switch Transformer (Switch) policy [22], which routes each
input to a single expert using a learned switching mechanism;
8) the Low-Rank Expert Mixture (MLoRE) policy [34], which
augments the MoE architecture with a shared convolutional
path for task-invariant feature extraction, and adopts low-rank
convolutional experts to reduce parameter and computational
overhead; and 9) the Multi-gate Mixture-of-Experts (MMoE)
policy [35], which shares expert sub-networks across tasks
and employs task-specific gates to combine experts and model
inter-task relationships. Both the baseline are trained with the
same reward and penalty settings as our method.
$:031
$:1.45
$:2.03
5:3.03
5:354
$:22.73
$:22.84
$:2298
$:2345
$:23.57


<!-- page 7 (ocr) -->
7
Fig. 4: Comparison of Consecutive Success Count Across Baselines. (a) compares the consecutive success count of our policy
against the baseline across all 100 objects, with objects ordered from lowest to highest success under our method. It is clear
that our approach consistently outperforms the baseline on the majority of items. (b) focuses on the five objects that the
baseline struggled with the most. While the baseline’s performance remains poor on these challenging shapes, our policy
achieves substantially higher and more reliable success rates. (c) presents results for ten objects randomly selected from
outside the training domain. For simpler shapes, both methods achieve similar levels of consecutive successes; however, as
object complexity increases, our policy continues to maintain a clear advantage over both baseline strategies.
C. Impact of Object Geometry on Base Policy Performance.
We tested the base policy on 100 objects from the training
set in 6000 episodes. Empirically, we observe that the majority
of objects can be successfully reoriented more than 15 consec-
utive times, with some achieving up to 23. However, a small
subset of objects consistently fails to succeed even once. To
better understand how object geometry affects reorientation
performance, we first identify the five best-performing and
five worst-performing objects under the base policy. Their
shapes, along with their corresponding mean consecutive suc-
cess counts ¯S, are visualized in Figure 3. We then analyze
the reorientation trajectories of the low-performing group
and observe that failures frequently arise when protruding
components become lodged between the fingers, preventing
further rotation until the episode times out. For instance,
repeated jamming occurs with airplane models, where wing
tips obstruct motion, and with train model, whose elongated
chassis often becomes trapped during manipulation. These
outcomes suggest that objects with pronounced protrusions or
extreme aspect ratios present substantial learning difficulties
due to their increased shape complexity.
D. Ablation Experiments
In addition to the design of Soft MoE policy, we also make
several critical design choices within our architecture. In this
section, we examined two key design choices: the number
of Experts and the inputs provided to the gating network.
All experiments were conducted on the same set of 100
objects used during training to ensure a fair comparison across
conditions.
Number of Expert Policies. We investigated how the number
of expert policies affects performance in our Soft MoE frame-
work by comparing configurations with 1, 4, 6, and 8 expert
policies. The single-expert case corresponds to a conventional
base policy without any specialization. In the four-expert
Fig. 5: Ablation Experiments. Left: Performance of MoE poli-
cies with varying numbers of expert policies. Right: Impact of
different inputs to the gating network. Error bars indicate the
standard deviation of the performance metric computed over
6,000 episodes.
setup, three specialists were trained on the poorest-performing
object classes while a single generalist policy addressed all
others. The six-expert configuration allocates one expert per
object category. Finally, the eight-expert configuration adopts
a finer-grained taxonomy to further partition object types,
yielding eight distinct experts. As illustrated in Figure 5(Left),
the four-expert configuration unexpectedly achieves superior
Smin and ¯S5−compared with both outperforming both the
single-expert and the larger expert variants. We hypothesize
that exceeding an optimal expert count degrades performance
because routing inefficiencies and diminished per-expert data
lead to imbalanced training and overfitting, which together
undermine both specialization and generalization on the most
challenging geometries. These findings highlight that, beyond
a certain point, more experts do not necessarily translate to
better performance; rather, a suitable expert count offers the
best trade-off between expressivity and robustness.
Gating Network Inputs. To assess the impact of gating
(A) The 100 objects for training
(B) The 5 worst objects
(C) 10 out-of-distribution objects
“
=
O
alia Ww
:
|
~
—
[S—
V
\
ols
o
o
—
The object ID
+ [FY =
Mm TF FA)
"> X at
@
A
v
ADR
PrivShape
SparseMOE
Ours
Smin
Ss
Smin
Ss-
.5
a
.
Ji
il
mn a
m—
| expert policies
sm With point-cloud embeddings,No categories
m4 expert policies
smn No point-cloud embeddings , With categories
6 expert policies.
With both point-cloud embeddings and categories
sm
§ expert policies


<!-- page 8 (ocr) -->
8
Method
Within Training Distribution
Out-of-Distribution
S↑
min
S↑
max
¯S↑
5−
¯S↑
5+
¯S↑
S↑
min
S↑
max
¯S↑
5−
¯S↑
5+
¯S↑
DR [1]
0.11
23.52
0.84
22.15
11.38
0.09
21.42
1.20
20.79
11.59
PrivFeat [3]
0.31
23.48
2.06
22.74
15.13
1.71
23.51
3.60
23.29
16.59
PrivShape [4]
0.41
23.5
1.59
23.12
16.93
2.59
23.42
3.97
23.21
16.25
ADR [2]
0.14
23.53
0.64
23.1
12.32
0.85
23.52
1.79
23.13
12.44
Res [33]
0.70
23.52
2.09
23.29
15.62
0.53
23.33
2.48
21.01
13.00
SparseMoE [21]
0.52
23.50
4.68
23.43
19.02
3.03
23.47
7.50
23.26
17.45
Switch [22]
0.66
23.52
2.67
23.33
18.33
2.27
23.59
5.39
23.31
16.85
MLoRE [34]
1.49
23.24
4.88
22.91
17.35
2.71
23.24
5.99
23.07
16.64
MMoE [35]
3.36
23.35
7.42
23.17
18.97
3.80
23.49
8.67
23.35
18.18
Ours
6.05
23.56
7.90
23.43
19.62
4.11
23.69
9.14
23.53
19.12
TABLE I: We compare our method to several baselines in simulation under two evaluation settings: (1) Within Training
Distribution; (2) Out-of-Distribution. Each method is evaluated across five metrics: the minimum consecutive success count
Smin, the maximum Smax, the average of the five worst-performing objects ¯S5−, the average of the five best-performing objects
¯S5+, and the overall average ¯S. Our approach performs exceptionally well on objects with complex surface geometries in both
the training-distribution and out-of-distribution scenarios, significantly outperforming the baseline methods.
network inputs on reorientation performance, we compared
the full router (which ingests both point-cloud embeddings
and category embeddings) against two ablated variants: one
driven solely by the point-cloud embedding and another re-
lying exclusively on the category embedding. As show in
Figure 5 (Right), although the two configurations achieved
similar average success counts, the model with the additional
categories embedding produced noticeably better results on the
worst single object and on the worst five objects. The observed
improvement implies that category embeddings provide global
directional cues to counteract performance drops on complex
shapes, with point cloud data simultaneously refining expert
probability distributions.
E. Evaluation of the Soft MoE Policy
Soft MoE Policy Performance. We first assess all methods on
objects drawn from the same distribution used during policy
training. To provide quantitative comparisons, Table I summa-
rizes five key metrics: minimum and maximum single-object
consecutive successes (Smin, Smax), mean performance on the
five hardest and easiest objects ( ¯S5−, ¯S5+), and the overall
average ( ¯S). Among the baselines, MoE-based schemes (e.g.,
MMoE and SparseMoE) deliver respectable overall means near
19 but still suffer from low worst-case performance (Smin
below 1 for SparseMoE). Traditional methods such as ADR
and PrivShape lag further behind, with overall averages under
17 and minimal robustness on the most challenging shapes.
In contrast, our Soft MoE policy dramatically elevates the
performance floor by raising Smin from under 1 to 6.05,
and it matches or exceeds ceiling performance, achieving
¯S5+ = 23.43 and Smax = 23.56. Overall, it achieves ¯S =
19.62 consecutive successes, outperforming all nine baselines
while demonstrating both stronger worst-case guarantees and
consistently high success across the entire object set.
Figure 4(A) plots the consecutive-success counts for each
of the 100 objects, sorted by performance under our model.
For clarity, we compare only three representative baselines
(ADR, PrivShape and SparseMoE) to highlight the relative
gains. Our policy surpasses each of these methods on the
vast majority of shapes, demonstrating its ability to generalize
across varied surface geometries. Figure 4(B) then focuses on
the five most challenging objects for these three baselines,
which were previously unsolvable under their policies. With
our approach, those objects become reliably reorientable with
multiple consecutive successes in every trial.
When initially reproducing the baseline DR and ADR [1, 2]
under our strict success criterion, which requires maintaining a
stable hold at the goal orientation, training failed to converge.
Specifically, the monolithic policy never achieved reliable in-
hand rotations across the full spectrum of complex geometries.
To restore performance, we implemented curriculum learning.
This process began with a relaxed success test using a single
cube, then progressively tightened the criterion while incre-
mentally introducing all 100 objects. Only after this staged
progression did the baseline achieve comparable results in
our evaluation. Conversely, our approach utilizes a modular
reinforcement learning framework that explicitly segregates
object-centric inputs from hand-centric state-action informa-
tion. This decoupled architecture not only facilitates more
effective feature learning but also eliminates the necessity for
curriculum training. From the initial epoch onward, the policy
acquires robust reorientation behaviors within a single training
phase.
Out-of-Distribution Robustness. We then study the out-of-
distribution robustness of object shapes for a trained model.
We begin by assessing each policy’s ability to handle object
shapes that lie beyond the training distribution. Figure 4(C)
shows consecutive-success counts on ten randomly selected
out-of-distribution objects. For the simple objects, both our
method and the baseline achieve comparable success count.
However, as surface complexity increases, the baseline’s per-
formance degrades sharply, ultimately failing entirely on some
items, whereas our policy continues to deliver consistent, high-
success count.
As shown in Table I, the strongest baseline, MMoE, already
exhibits zero-shot capability. It achieves an out-of-distribution
mean of 18.18 consecutive successes. However, it still col-
_[


<!-- page 9 (ocr) -->
9
lapses on the most challenging shapes, registering a minimum
success count of only 3.80 and an average of 8.67 on the five
hardest objects. By contrast, our method raises the minimum
consecutive-success count on these difficult items to 4.11 and
boosts the mean across the five most challenging objects to
9.14.
These findings confirm that our method not only excels
on familiar objects but also preserves its advantage when
confronted with novel, complex geometries, achieving strong
zero-shot performance without any further training or adapta-
tion.
F. Clustering Analysis of Gating Network Outputs
To understand how the gating network πgate differentiates
object geometries when assigning experts, we employed t-SNE
(Figure 6) to visualize the expert assignment weight vectors
produced by the gating network πgate after it was trained
on 100 object models with rotational augmentation for 6000
times. We found that objects of different geometric complexity,
as reflected by their consecutive success rates under the base
policy, occupy separate regions in the embedding space. For
example, objects that achieve high consecutive success rates
tend to cluster in the upper-right quadrant, such as object IDs
91 and 93, while those with lower rates group in the lower-left
quadrant. Moreover, objects with similar shapes form tighter
clusters, for instance IDs 41 and 50 (both shoes) and IDs
19 and 57 (both sculpted human heads). These observations
indicate that the gating network effectively captures geometric
distinctions and assigns experts in a shape-dependent manner.
Fig. 6: t-SNE projection of gating-network weight vectors for
100 objects. Points are colored by cluster assignment, showing
that objects with different geometries occupy distinct regions
while similar shapes form the same clusters.
V. CONCLUSION AND LIMITATIONS
In this work, we introduced the Soft MoE policy for
in-hand object reorientation and demonstrated its successful
deployment across a variety of complex shapes. By leveraging
multiple specialized experts, our approach efficiently adapts
to differing object geometries during training. Experiments
show that the Soft MoE architecture not only achieves reliable
performance on known objects but also generalizes effectively
to new, unseen shapes without additional retraining. Our re-
sults underscore the potential of Mixture-of-Experts networks
in robotic policy learning. Specifically, incorporating diverse
expert models enhances training efficiency, bolsters robustness
against challenging object geometries, and improves overall
generalization. These findings suggest that Soft MoE frame-
works can serve as a powerful tool for developing adaptable,
high-performing robotic manipulation strategies.
Limitations and Future Work: Our reliance on manually
labeled object categories limits scalability. To overcome this,
we will explore multimodal large-language models to automate
labeling. Moreover, we have yet to validate Soft MoE on
physical hardware; conducting real-world trials is a primary
goal for our next research phase.
REFERENCES
[1] O. M. Andrychowicz, B. Baker, M. Chociej, R. Joze-
fowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert,
G. Powell, A. Ray et al., “Learning dexterous in-hand
manipulation,” The International Journal of Robotics
Research, vol. 39, no. 1, pp. 3–20, 2020.
[2] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko,
R. Singh, J. Liu, D. Makoviichuk, K. Van Wyk,
A. Zhurkevich, B. Sundaralingam et al., “Dextreme:
Transfer of agile in-hand manipulation from simulation
to reality,” in 2023 IEEE International Conference on
Robotics and Automation (ICRA).
IEEE, 2023, pp.
5977–5984.
[3] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik,
“In-hand object rotation via rapid motor adaptation,” in
Conference on Robot Learning. PMLR, 2023, pp. 1722–
1732.
[4] H. Qi, B. Yi, S. Suresh, M. Lambeta, Y. Ma, R. Calandra,
and J. Malik, “General in-hand object rotation with vision
and touch,” in Conference on Robot Learning.
PMLR,
2023, pp. 2549–2564.
[5] H. Qi, B. Yi, M. Lambeta, Y. Ma, R. Calandra, and J. Ma-
lik, “From simple to complex skills: The case of in-hand
object reorientation,” arXiv preprint arXiv:2501.05439,
2025.
[6] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Ve-
ness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K.
Fidjeland, G. Ostrovski et al., “Human-level control
through deep reinforcement learning,” nature, vol. 518,
no. 7540, pp. 529–533, 2015.
[7] D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou,
A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai,
A. Bolton et al., “Mastering the game of go without
human knowledge,” nature, vol. 550, no. 7676, pp. 354–
359, 2017.
[8] J. Schrittwieser, I. Antonoglou, T. Hubert, K. Simonyan,
L. Sifre, S. Schmitt, A. Guez, E. Lockhart, D. Hassabis,
T. Graepel et al., “Mastering atari, go, chess and shogi
by planning with a learned model,” Nature, vol. 588, no.
7839, pp. 604–609, 2020.
[9] A. Nagabandi, K. Konolige, S. Levine, and V. Kumar,
“Deep dynamics models for learning dexterous manipu-
ra gerd Tee
&
wan
Te
ad
=
]
~~
po
-
00?®
__
1476
h-3
Co]
\i3
:
FL
=
3
Sse
aad
RENN
—
Fa
NZ go
“Ey


<!-- page 10 (ocr) -->
10
lation,” in Conference on robot learning.
PMLR, 2020,
pp. 1101–1112.
[10] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu,
K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. All-
shire, A. Handa et al., “Isaac gym: High performance
gpu-based physics simulation for robot learning,” arXiv
preprint arXiv:2108.10470, 2021.
[11] T. Chen, M. Tippur, S. Wu, V. Kumar, E. Adelson, and
P. Agrawal, “Visual dexterity: In-hand reorientation of
novel and complex object shapes,” Science Robotics,
vol. 8, no. 84, p. eadc9244, 2023.
[12] A. Karni, G. Meyer, C. Rey-Hipolito, P. Jezzard, M. M.
Adams, R. Turner, and L. G. Ungerleider, “The ac-
quisition of skilled motor performance: fast and slow
experience-driven changes in primary motor cortex,” Pro-
ceedings of the National Academy of Sciences, vol. 95,
no. 3, pp. 861–868, 1998.
[13] C. R. Qi, L. Yi, H. Su, and L. J. Guibas, “Pointnet++:
Deep hierarchical feature learning on point sets in a
metric space,” Advances in neural information processing
systems, vol. 30, 2017.
[14] J.-P. Saut, A. Sahbani, S. El-Khoury, and V. Perdereau,
“Dexterous manipulation planning using probabilistic
roadmaps in continuous grasp subspaces,” in 2007
IEEE/RSJ International Conference on Intelligent Robots
and Systems.
IEEE, 2007, pp. 2907–2912.
[15] Y. Bai and C. K. Liu, “Dexterous manipulation using
both palm and fingers,” in 2014 IEEE International
Conference on Robotics and Automation (ICRA).
IEEE,
2014, pp. 1560–1565.
[16] L. Sievers, J. Pitz, and B. Bäuml, “Learning purely
tactile in-hand manipulation with a torque-controlled
hand,” in 2022 International conference on robotics and
automation (ICRA).
IEEE, 2022, pp. 2745–2751.
[17] I. OpenAI Akkaya, M. Andrychowicz, M. Chociej,
M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert,
G. Powell, R. Ribas et al., “Solving rubik’s cube with a
robot hand,” arXiv preprint arXiv:1910.07113, 2019.
[18] J. Pitz, L. Röstel, L. Sievers, D. Burschka, and B. Bäuml,
“Learning a shape-conditioned agent for purely tactile in-
hand manipulation of various objects,” in 2024 IEEE/RSJ
International Conference on Intelligent Robots and Sys-
tems (IROS).
IEEE, 2024, pp. 13 112–13 119.
[19] R. A. Jacobs, M. I. Jordan, S. J. Nowlan, and G. E.
Hinton, “Adaptive mixtures of local experts,” Neural
computation, vol. 3, no. 1, pp. 79–87, 1991.
[20] M. I. Jordan and R. A. Jacobs, “Hierarchical mixtures
of experts and the em algorithm,” Neural computation,
vol. 6, no. 2, pp. 181–214, 1994.
[21] N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. Le,
G. Hinton, and J. Dean, “Outrageously large neural
networks: The sparsely-gated mixture-of-experts layer,”
arXiv preprint arXiv:1701.06538, 2017.
[22] W. Fedus, B. Zoph, and N. Shazeer, “Switch transform-
ers: Scaling to trillion parameter models with simple
and efficient sparsity,” Journal of Machine Learning
Research, vol. 23, no. 120, pp. 1–39, 2022.
[23] F. Xue, Z. Zheng, Y. Fu, J. Ni, Z. Zheng, W. Zhou,
and Y. You, “Openmoe: An early effort on open
mixture-of-experts language models,” arXiv preprint
arXiv:2402.01739, 2024.
[24] B. Lin, Z. Tang, Y. Ye, J. Cui, B. Zhu, P. Jin, J. Huang,
J. Zhang, Y. Pang, M. Ning et al., “Moe-llava: Mixture of
experts for large vision-language models,” arXiv preprint
arXiv:2401.15947, 2024.
[25] K. Doya, K. Samejima, K.-i. Katagiri, and M. Kawato,
“Multiple model-based reinforcement learning,” Neural
computation, vol. 14, no. 6, pp. 1347–1369, 2002.
[26] X. B. Peng, M. Chang, G. Zhang, P. Abbeel, and
S. Levine, “Mcp: Learning composable hierarchical
control with multiplicative compositional policies,” Ad-
vances in neural information processing systems, vol. 32,
2019.
[27] G. Cheng, L. Dong, W. Cai, and C. Sun, “Multi-task
reinforcement learning with attention-based mixture of
experts,” IEEE Robotics and Automation Letters, vol. 8,
no. 6, pp. 3812–3819, 2023.
[28] Z. Huang, H. Yuan, Y. Fu, and Z. Lu, “Efficient residual
learning with mixture-of-experts for universal dexterous
grasping,” arXiv preprint arXiv:2410.02475, 2024.
[29] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and
O. Klimov, “Proximal policy optimization algorithms,”
arXiv preprint arXiv:1707.06347, 2017.
[30] D.-A. Clevert, T. Unterthiner, and S. Hochreiter, “Fast
and accurate deep network learning by exponential linear
units (elus),” arXiv preprint arXiv:1511.07289, 2015.
[31] Y. Dong, X. Liu, J. Wan, and Z. Deng, “Gex: Democra-
tizing dexterity with fully-actuated dexterous hand and
exoskeleton glove,” arXiv preprint arXiv:2506.04982,
2025.
[32] L. Downs, A. Francis, N. Koenig, B. Kinman, R. Hick-
man, K. Reymann, T. B. McHugh, and V. Vanhoucke,
“Google scanned objects: A high-quality dataset of 3d
scanned household items,” in 2022 International Confer-
ence on Robotics and Automation (ICRA).
IEEE, 2022,
pp. 2553–2560.
[33] F. Ceola, L. Rosasco, and L. Natale, “Resprect: Speeding-
up multi-fingered grasping with residual reinforcement
learning,” IEEE Robotics and Automation Letters, vol. 9,
no. 4, pp. 3045–3052, 2024.
[34] Y. Yang, P.-T. Jiang, Q. Hou, H. Zhang, J. Chen, and
B. Li, “Multi-task dense prediction via mixture of low-
rank experts,” in Proceedings of the IEEE/CVF confer-
ence on computer vision and pattern recognition, 2024,
pp. 27 927–27 937.
[35] J. Ma, Z. Zhao, X. Yi, J. Chen, L. Hong, and E. H.
Chi, “Modeling task relationships in multi-task learning
with multi-gate mixture-of-experts,” in Proceedings of
the 24th ACM SIGKDD international conference on
knowledge discovery & data mining, 2018, pp. 1930–
1939.
[36] K. Mamou, E. Lengyel, and A. Peters, “Volumetric
hierarchical approximate convex decomposition,” Game
engine gems, vol. 3, pp. 141–158, 2016.
[37] D. P. Kingma, “Adam: A method for stochastic optimiza-
tion,” arXiv preprint arXiv:1412.6980, 2014.


<!-- page 11 (ocr) -->
11
APPENDIX
EXPERIMENTAL DETAILS
Object Dataset: We employ the full set of 150 objects
from our dataset (see Figure 7), selecting 100 at random for
training and reserving the remaining 50 for out-of-distribution
evaluation. To ensure that each mesh can be manipulated by
the robotic hand, we first center it and then scale it by a factor
of 0.8 so that its dimensions align with the hand’s workspace
in simulation. We observed that scaling meshes below a certain
threshold, such as reducing them to 60% of their original size,
shifts manipulation from precise fingertip control to collisions
with the inner surfaces of the fingers. Moreover, when an
object becomes very small, its complex geometric features no
longer convey meaningful distinctions, and the dexterous hand
effectively treats it as a simple, diminutive cube.
Convex Decomposition: We use approximate convex decom-
position (V-HACD [36]) to perform an approximate convex
decomposition on the object and the robot hand meshes for
fast collision detection in the simulator (Figure 8).
Policy architecture: All networks are implemented as MLPs
and trained with Adams [37]: the base policy πbase uses two
hidden layers of 512 units each; the point-cloud encoder µpc
has three layers of 32 units; the object encoder µe comprises
two layers of 256 and 128 units; and the gating network πgate
consists of two 64-unit layers with ELU activations [30].
Hyper-parameters: Table II lists the hyper-parameters used
in the experiments.
Fig. 7: Overview of the complete object dataset, on the left of
the red line, we show the training dataset. And on the right of
the red line, we show the out-of-distribution (testing) dataset.
Fig. 8: We show the difference between object meshes with
and without convex decomposition.
TABLE II: Hyper-parameter Setup
Hyper-parameter
Value
Hyper-parameter
Value
num of envs
32768
episode length
600
horizon length
8
minibatch size
16384
learning rate
5e-3
PPO clip range
0.2
kl threshold
0.02
PPO gamma
0.99
PPO tau
0.95
success tolerance
0.4
csuccess
800
cdist
-10.0
crot
-1.0
ca
-0.0002
τθ
0.1
τq
10.0
τv
0.04
τω
0.5
Within Training Distribution
|
Out-of-Distribution
"RE ET CY
Treats
seh I@eoHB
vr 3 amid
dihPitnimaw
i
dwsrae
Fellosonsigd
jg Fmusg a
QA
iME Ne gw deied
ascend
lB YE a
gwmPEOE
me Enon ¥ r=
wADParp
tT RAT SE mR L
Fars rj3iinvadadX 3
ASH 4TOLAASS
§ rd
~~ J
Mesh
No V-HACD
V-HACD
