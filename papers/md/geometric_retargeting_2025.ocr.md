<!-- page 1 (ocr) -->
Geometric Retargeting:
A Principled, Ultrafast Neural Hand Retargeting Algorithm
Zhao-Heng Yin1,2, Changhao Wang2, Luis Pineda2, Krishna Bodduluri2,
Tingfan Wu2, Pieter Abbeel1, Mustafa Mukadam2
Abstract— We introduce Geometric Retargeting (GeoRT), an
ultrafast, and principled neural hand retargeting algorithm for
teleoperation, developed as part of our recent Dexterity Gen
(DexGen) system [1]. GeoRT converts human finger keypoints
to robot hand keypoints at 1KHz, achieving state-of-the-art
speed and accuracy with significantly fewer hyperparameters.
This high-speed capability enables flexible postprocessing, such
as leveraging a foundational controller for action correction
like DexGen. GeoRT is trained in an unsupervised manner,
eliminating the need for manual annotation of hand pairs. The
core of GeoRT lies in novel geometric objective functions that
capture the essence of retargeting: preserving motion fidelity,
ensuring configuration space (C-space) coverage, maintaining
uniform response through high flatness, pinch correspondence
and preventing self-collisions. This approach is free from
intensive test-time optimization, offering a more scalable and
practical solution for real-time hand retargeting.
I. INTRODUCTION
Teleoperation is essential for collecting robotic manipula-
tion data, as it allows humans to remotely control robots in
real-time. In dexterous manipulation, a fundamental com-
ponent of teleoperation is kinematic retargeting [2], [3],
[4], [5], [6]. It involves translating human gestures into
corresponding robot hand poses, enabling intuitive control
of robotic systems. However, defining an effective kinematic
retargeting function remains a longstanding challenge. The
complexity arises from the need to account for variations
in human and robot configurations, and the desired level
of precision. Despite the progress in this area, no universal
methods have been developed that reliably captures human
intent while maintaining natural and efficient robot motion.
One of the main challenges is determining the criteria for
effective kinematic retargeting. Although there are numerous
possible mappings from a human hand to a robot hand, the
simplest and most effective criteria (objective function) for
specifying and training desirable retargeting functions remain
unclear. Existing methods [2], [3], [7], [8] typically rely
on a complex set of task vector constraints that ensures
the retargeted robot hand pose visually looks similar to
the original human hand pose. Most recent teleoperation
works [8] typically take the following linear matching form
in their pipeline:
L =
N
∑
i=1
∥αivi
H −vi
R∥2 +Regularizer.
(1)
*This work was partially done during Z.H. Yin’s intern at Meta.
*Project website: zhaohengyin.github.io/geort
*For application in DexterityGen: zhaohengyin.github.io/dexteritygen
1BAIR, UC Berkeley EECS.
2FAIR at Meta.
Source C-space
Target C-space
f
Fig. 1: Retargeting is an unconstrained problem. There
are many valid retargeting functions (e.g. by dragging the
point anchors in the figure). However, it is unclear how to
define a proper cost functional (objective) to specify desired
retargeting function.
TABLE I: Comparison of technical specifications of existing
approaches. The speed is claimed by the referred paper or
its follow up work.
Method
DexPilot [2] AnyTeleop [3] RTelekinesis [8]
Ours
Hyperparams
≥10
≥10
≥10
≤5
No Task Vector
×
×
×
✓
No Online Opt.
×
×
✓
✓
Retargeting Speed
60-100Hz
60-100Hz
1000Hz
1000Hz
Here vi
H and vi
R = f(vi
H) are the task vectors of (source)
human and (retargeted) robot hands, αi are some scaling
hyperparameter, and N ≈10 is the number of hand keypoints.
The second regularization term is usually used to ensure
smoothness. This formulation has several drawbacks. First, it
requires several hyperparameters (e.g. αi, task vector origin
oi) to recenter and rescale each human keypoint (or task
vectors), which are difficult to specify and vary between
individuals. It requires a tedious process to calibrate these
task-vector-related hyperparameters. Second, we notice that
this linear matching objective may also be suboptimal. To
illustrate this, we use Allegro Hand as an example to
compare the shape of human and robot fingertip keypoint
space, as shown in Figure 2. We observe that the human
fingertip keypoint C-space (moving range) typically has a
more curved and narrower shape, while that of the robot hand
is more regular and wider. Consequently, the linear matching
objective can fail to capture the correspondence and we need
a more principled way to define the retargeting objective.
In this paper, we propose Geometric Retargeting (GeoRT),
a principled retargeting objective and training pipeline. Since
arXiv:2503.07541v1  [cs.RO]  10 Mar 2025
HH


<!-- page 2 (ocr) -->
Z
Y
Fig. 2: Nonlinear Nature of Retargeting: In this figure, we compare shapes of human and robot (Allegro) fingertip keypoint
C-space (i.e. the moving range of fingertip in the hand frame). The top row shows the ring finger keypoint space comparisons
and the bottom row shows the thumb keypoint space comparisons. We find that the robot and human hands keypoint spaces
are not directly related through a linear mapping as suggested by previous works. In this paper, we propose novel objectives
to overcome this limitation. In this figure, the robot finger keypoints are produced by random sampling in joint space and
then computing forward kinematics. The human finger keypoints are produced by motion capture of a 5-minute play, in
which the human is asked to move their fingers randomly to explore the limit of their hand joints.
Fig. 3: The proposed principled and ultrafast teleoperation
algorithm enables large-scale foundation controllers, unlock-
ing the potential for more dexterous teleoperation systems
like DexterityGen [1].
the ultimate goal of retargeting is to give the human operator
a sense of intuitive control over the robot hand, we define the
ideal retargeting through a set of straightforward geometric
criteria that characterize such requirements. We suggest that
the retargeting model should (1) preserve human motion
locally and preserve pinch grasps, (2) maximize C-space
coverage so that the robot hand is fully utilized, and it should
be (3) flat for uniform control sensitivity , (4) preserve pinch
correspondence, and (5) collision-free. These objectives are
simple to implement while providing a principled specifica-
tion of retargeting quality. We also show that these principles
are independent and they form minimal constraints for defin-
ing retargeting. We compare the technical specifications of
our method to existing approaches in Table I. Our method
has fewer hyperparameters and does not use heuristic task
vectors, while still achieving state-of-the-art inference speed.
In the experiments, we show that our algorithm has much
better hand utilization and achieves better smoothness. It
also outperforms existing methods in the teleoperation-based
grasping task in real world experiments.
In summary, this paper makes the following contributions:
(1) We propose principled retargeting objectives for learning
neural retargeting models. (2) We develop a fast neural
retargeting system based on these objectives, which outper-
forms existing approaches in both retargeting quality and
teleoperation performance and supports further applications
such as DexterityGen [1].
II. GEOMETRIC RETARGETING
A. Preliminaries
We make the following commonly used assumption as
previous works. A1. First, we assume that the robot hand
Human Ring Finger
Allegro Ring Finger
Human Ring Finger
Allegro Ring Finger
01.
03
£
&
J
0121+
02
=
NY
y
Zo
+
202
.
9
00
01
Ba
AA,
a
Va
oor
y
ox
3
ra
Loo
93
V/-
Zoos
'
00
:
-
A
g
ooo
GY
A
AEE
0.
-
86;
a
0.01
RT)
HE
0.00
ry
3
—-0.04
0.02
005
-
Yo
—
x
-0.10
~~
0.05,
Yo.
hard
0.03
0.03
os
x
Zoos
636
002
Vv
Joos
06
£0.00.000010020.030.040.050.06
005
000
005
010
01s
Y
on
%o.04
010
x
x
-oo1
0.06
Yo
-002
0.00
:
© “02 015
Human Thumb
Allegro Thumb
Human Thumb
Allegro Thumb
0475
i
or
oer
28%
Z
.
008
15
012s.
BOIL
a
a
z
Se
}
z
8
5a
To? BBY
7
0
y
\ Ta
|
.
0075
X
>
»
€
>
3
00
Coe
0050
008
XX
Fe;
a
0.05
0.025
A&E
v4
0.06
015
“\
0.08
015
0.04
#
010
0.06
010
v
-
008”
00s
or
002
V
00g,
004
oo
>
008
010
hog
002 ¥
oes
oom
0
od
000
MET
000
®
on
Coos
0.08
x
ood
005x
% gr -002
ass
“ook 590!
ooo
A
ES 2
x’
-
>
Th,
-
Ls <
|
-
‘


<!-- page 3 (ocr) -->
Motion Preservation
Human Fingertip C-Space
(Cartesian)
Robot Fingertip C-Space
(Cartesian)
Retarget
Maximize Space Coverage (Surjection)
Fig. 4: Basic idea of our geometric objective functions (criterion I and II). (Left) A good retargeting function should preserve
the moving direction of the fingertip. (Right) Besides, the retargeting function should also be a surjection, so that the robot
fingertip C-space is fully utilized. Note that we only show the C-space for one fingertip (e.g. index finger) in the figure.
is anthropomorphic so that a natural and intuitive retargeting
function may exist. A2. We further assume the existence of
finger correspondence: e.g. humans use their index fingertip
to control the robot’s “index” fingertip. We denote the
humans’ and robot’s fingertip position in their own wrist
frame as xi
H and xi
R respectively, where i is the fingertip
index.
In this paper, a kinematic retargeting model f is a function
that maps a set of human fingertip keypoints to robot hand
joint positions, which is different from works that also take
the object model and poses as input for joint hand-object
retargeting.
B. Criterion I: Motion Preservation
We require the retargeting function to preserve the move-
ment direction of each fingertip. This aligns with a funda-
mental expectation in teleoperation: when a human operator
moves their finger in a certain direction, they naturally expect
the robot’s fingertip to follow the same trajectory. Formally,
given any position xi
H for i-th finger and any small moving
direction d, we require d parallel to FKi ◦fi(xi
H +d)−FKi ◦
fi(xi
H), where FKi is the forward kinematics for fingertip
i, and fi is the retargeting component for i-th finger. This
criterion can be described by a simple loss function:
Ldir = −∑
i
Ed,xi
HDir(xi
H,d)
(2)
= −∑
i
Ed,xi
H⟨d
∥d∥, FKi ◦fi(xi
H +d)−FKi ◦fi(xi
H)
∥FKi ◦fi(xi
H +d)−FKi ◦fi(xi
H)∥⟩.
(3)
We implement FKi as a pretrained neural forward kinematics
function. One can also use an analytical forward kinematics
function.
C. Criterion II: C-space Coverage
Besides motion preservation, another important criterion is
C-space coverage. Intuitively, we want the robot’s C-space
to be fully utilized—when a human moves their fingers from
X
Y
X
Y
Low Flatness Mappings
High Flatness Mapping
Fig. 5: The retargeting mapping should have a high flatness
(criterion III). In this 1D retargeting example (mapping an
interval on the x-axis to another interval on the y-axis), this
is equivalent to f ′(x) being constant everywhere, so that any
small ∆x will lead to the same amount of ∆y. Note that the
blue curves on the left can satisfy the criterion I and II.
Therefore, introducing a third flatness objective is necessary.
one limit to the other, the robot hand should replicate this
motion across its full range, rather than being confined to a
limited subset of its C−space.
Formally, we denote the keypoint C−space of i-th robot
and human fingertip as KCi
R and KCi
H respectively. Then, our
coverage criteria states that FKi ◦fi should be a surjection
from KCi
H to KCi
R, and we should minimize the volume
of KCi
R \ (FKi ◦fi(KCi
H)), i.e. the uncovered i-th fingertip
keypoint C-space of robot hand.
However, computing this uncovered space and its volume
is computationally expensive, and this does not yield a
differentiable function either. Therefore, we propose to use
Chamfer loss [9] in 3D vision research as a proxy for this
procedure. In each minibatch, we sample Pi
H ∼KCi
H and
Pi
R ∼KCi
R uniformly, and we minimize
Lcover = ∑
i
EPi
H∼KCi
H,PR∼KCi
RChamfer(Pi
R,FKi ◦fi(Pi
H)). (4)
This loss guarantees that any random point cloud represen-
tation of KCi
R can be closely approximated by projecting the
2alae
Fal


<!-- page 4 (ocr) -->
Retargeting 
Network
Human 
Fingertip
Position
Forward
Kinematics
Robot
Joint
Loss
gradient
Collision
Classifier
Loss
(I-IV)
(V)
Fig. 6: Model training update procedure. The geometrical
loss functions (I-IV) are computed in the keypoint spaces (af-
ter the differentiable forward kinematics). The gradient back-
propagates through the forward kinematics model and the
collision classifier to the retargeting network. Note that the
forward kinematics model and collision classifier are only
used during training.
corresponding representation of KCi
H with retargeting model.
D. Criterion III: High Flatness
While the last two criteria already define a reasonable
retargeting mapping, we find it necessary to introduce a flat-
ness objective to ensure that the model responds uniformly
as the user moves across the C-space, which enhances the
predictability and intuitiveness of the interaction experience.
To understand this, we illustrate an 1D example in Figure 5.
The retargeting functions defined by the blue curves satisfy
the criterion I and II simultaneously, however, the same
∆x in the source X space may lead to different ∆y in the
target Y space. In this case, the user may perceive the
retargeting as too unresponsive (i.e. f ′(x) ≈0) in some areas,
while overly sensitive (i.e. |f ′(x)| too large) in others. The
ideal retargeting should have high flatness, which means
f ′(x) being almost constant, or a low f ′′(x) = d2 f
dx2 (x) ≈0
equivalently. To generalize this idea to high dimensional
space, we propose to minimize ExH,d
d2(FK◦f)
dt2
(xH +td)
2
,
which means the second-order directi
al derivative at
y
point along any direction should be close to 0. We use the
finite difference method to evaluate the derivatives, yielding
the following objective function:
Lflat = Ex,d∥FK◦f(x+d)+FK◦f(x−d)−2FK◦f(x)∥2.
(5)
The global linear matching objective (i.e. Equation 1) used
by previous works naturally encourages flatness. However,
for general non-linear retargeting problems, perhaps the best
way is to use the proposed local flatness constraint.
Note that criteria II and III can not derive criterion I
(motion preservation). In the example, reversing the linear
mapping (change the slope to its opposite and shift) on
the right can still make criteria II and III hold, but the
moving direction in the target space will be reverted and
very unintuitive.
E. Criterion IV: Pinch Correspondence
The previous criterion focused more on per-finger motion
regulation. Another important expectation from users is pinch
Algorithm 1 Geometric Retargeting
1: Generate (joint position q, fingertip position x, collision
c) data in simulation to train each neural forward kine-
matics models FKi and collision classifier C.
2: Generate point cloud approximation
i
R,
i
H of each
keypoint C-space KCi
R,KCi
H.
3: for itr = 0,1,...,Ntrain do
4:
Sample d ∼N (0,σ2) and random human gesture xH
to compute Ldir,Lflat,Lpinch,Lcol;
5:
Sample Pi
H ∼
i
H, Pi
R ∼
i
R to compute Lcover;
6:
Optimize f b
aking gr
ent descent with L =
Ldir +λ1Lcover +λ2Lflat +λ3Lpinch +λ4Lcol.
7: end for
8: return
f
correspondence. For example, when the users do a pinch
grasp using the thumb and index finger, they typically expect
that the robot hand does the same. We find this crucial to
provide users with a sense of agency, however, previous
criteria do not strictly guarantee this and sometimes we
notice that the emerged pinch correspondence is not perfect.
To improve this, we further introduce a pinch correspondence
constraint. Specifically, for a human gesture xH, if xi
H −x j
H
is below a threshold d (such as 1cm), i.e., finger i and j are
pinching, then we require FKi ◦fi(xi
H) close to FKj ◦f j(x j
H).
This can be written as
Lpinch = ExH
(6)
∑
(i,j):i̸=j
1(∥xi
H −x j
H∥< d)∥FKi ◦fi(xi
H)−FKj ◦f j(x j
H)∥2.
(7)
Note that this requires human users to provide some pinch
grasp examples. Fortunately, this can be easily collected
within 5 minutes of random play as we will discuss in the
implementation section.
F. Criterion V: Collision-Free Retargeting
Finally, a collision-free human hand gesture should corre-
spond to a collision-free robot hand gesture. Therefore, we
introduce collision-free as our final criterion. Similar to [8],
we first pretrain a collision classifier C to decide the proba-
bility of a joint configuration q leading to hand self-collision.
The training dataset is generated through simulation, and
the label is obtained by querying a collision checker to get
the binary self-collision label. Then, we use the following
collision loss over retargeting model f:
Lcol = −ExH log(1−C(f(xH)));
(8)
Note that C is fixed as we train f. Interestingly, we find that
even without this term our loss can lead to few collisions
for certain robot hands. Nevertheless, we introduce this for
completeness.
KC
KC
yt
adi
|—
on
an


<!-- page 5 (ocr) -->
Baseline (Equation 1)
Ours
Fig. 7: Qualitative comparisons. We find that due to insuffi-
cient C-space coverage, the baseline method fails to provide
important functionalities such as index-ring finger pinch,
which is essential for in-hand manipulation.
G. Implementation
We implement our kinematic retargeting model as a set of
independent retargeting models. For example, for the Allegro
Hand which has four fingers, we define f(x1
H,x2
H,x3
H,x4
H) =
[f1(x1
H), f2(x2
H), f3(x3
H), f4(x4
H)], and each fi is an indepen-
dent retargeting model for the corresponding finger. We
parameterize each fi as a multi-layer perception (MLP). We
also rescale the joint position range to [−1,1] and use Tanh
as output activation of each fi. We use a combination of the
proposed loss functions to train our model:
L = Ldir +λ1Lcover +λ2Lflat +λ3Lpinch +λ4Lcol.
(9)
This optimization objective only has 4 hyperparameters
compared to previous works that have numerous scale hyper-
parameters and heuristic task vectors. We present our training
loop in Algorithm 1 for clarity. The training procedure is very
fast in practice, only taking 3-5 minutes on a single NVIDIA
3060 GPU. The point cloud approximation of the robot hand
fingertip keypoint C-space can be generated by randomly
moving the hand in simulation. For that of human hand, we
find the following method effective: we ask the human user
to stretch their fingers and move back and forth, as well
as perform various pinch grasps under any motion capture
system (or other hand tracking system such as a glove).
We record the moving trajectory of each fingertip keypoint,
giving us several raw point clouds. This data collection
process is fast and typically takes less than 5 minutes and
is a one-time calibration. We find that an empirical loss
weight setup that works well is λ1 ∈[10,100],λ2 = 1,λ3 ∈
[103,106],λ4 = [10−4,10−2]. Varying the weight inside these
intervals can change the retargeting details a bit, but overall
they look similar and provide good results. Note that the
magnitudes of some weights are large due to the distance
unit we use.
TABLE II: Quality metric of different loss objectives. Note
that the online version of Eqn (1) is not time-independent
and its result relies on the previous frame, so we use its
offline version as an approximation.
Method
Equation 1
Ours
Offline [8]
Online [2], [3]
Motion Preservation(↑)
0.73
–
0.94
C-space coverage(↑)
38%
–
90%
TABLE III: Teleoperation performance comparison of dif-
ferent methods in real world. Our method offers a faster and
more effective teleoperation experience.
Method
Equation 1
Ours
Offline [8]
Online [2], [3]
Onetime-Success(↑)
55%
42.5%
87.5%
Completion Time(↓)
9.0s
19.3s
3.2s
III. EXPERIMENTS
In this section, we compare the grasping performance of
this work to other teleoperation methods. We also study
the properties and design choices of our neural retargeting
method. For its application, we refer readers to the Dexteri-
tyGen paper.
A. Simulation Evaluation
We first compare the quality of different methods in
simulation. We quantitatively measure the smoothness score
and the C-space coverage score. The definitions of these two
metrics are as follows:
1) Motion Preservation is related to Criteria I. We com-
pute this by uniformly sample anchor points xi
H and
directions d, and we compute 1
N ∑N
i=1 Ed,xi
HDir(xi
H,d),
i.e. how good the robot hand movement is aligned
with human hand movement. The metric is bounded
by [−1,1].
2) C-space Coverage is related to Criteria II, quantifying
the effective moving range of the fingertip. How-
ever, we do not exactly compute this following the
proposed objective function. We sample sufficiently
many points xi
H in each human fingertip keypoint
C-space and we compute how much they occupy
the robot keypoint C-space, given by Vol(∪iB(FK ◦
f(xi
H),r) ∩KPi
R)/Vol(KPi
R). Here, B(x,r) denotes a
sphere or radius r centered at x. This metric is between
[0%,100%].
Results We list the evaluation results of different methods
on Allegro Hand in Table II. We find that our approach
can achieve much better smoothness and C-space coverage
compared to baseline methods. However, this result is
expected since we directly use these two metrics for
optimization. This suggests that our approach can fully
utilize the moving range of the robot hand while providing
Udy
WegWe


<!-- page 6 (ocr) -->
105s
4s
Fig. 8: The user can use our system to clean up a pile of objects (12) on the table in around 100 seconds easily. Note that
the relatively slow arm motion is the main bottleneck here. The user can grasp most of the objects successfully with 1 trial.
Fig. 9: Qualitative retargeting results of our retargeting method. The top half is the Allegro hand and the bottom half is
the Leap hand. Even if our method does not use any task-vector-based matching terms, it can discover the correspondence
between human and robot hands.
the user with a smooth sense of control.
Qualitative Results Furthermore, we investigate whether
our quantitative results translate to plausible retargeting. We
plot some retargeting results in Figure 7. Surprisingly, even
if we do not use any task vector matching heuristics, a good
correspondence emerges from our simple objective function
on different hands (Allegro and LEAP [10] hand). We also
compare our method to the baseline in Figure 2. We find
that due to insufficient coverage, the baseline method fails
to utilize the lateral movement of fingers effectively and
cannot do effective pinch grasp or finger (thumb) reaching.
B. Real-world Experimental Setup
Then, we evaluate our approach on an arm-hand robotic
system. In this paper, we use the Allegro robot hand with
the Franka Panda robot arm. For the teleoperation of Allegro
VoL owe we
RCI ASE GE GR GY
Ce PY EO
4
OSV OIY@
POVYVEIIYO
YOOYS &WW


<!-- page 7 (ocr) -->
hand, we first use a Manus glove to capture the human hand
keypoints. These keypoints are then fed into the retargeting
model to produce the allegro hand joint target. These joint
target are then sent to a PD controller to drive the hand.
For the arm teleoperation, we use a Vive tracker system to
capture the human wrist pose and use it to control the motion
of robot arm’s end-effector pose.
C. Real-world Evaluation
Since performing dexterous in-hand manipulation is hard
as suggested by previous works, in this paper we mainly
consider the grasping performance, which is also a crucial
step in robotic manipulation. We record the one-trial success
rate and the average time a user takes to grasp an object
successfully.
Results We show the result in Table III. We find that our
method can allow for faster and more effective grasping in
real world. We account for this by better utilization of fin-
gertip C-space and smoother and more intuitive retargeting.
Specifically, we find that it is hard to grasp tiny objects with
the baseline method due to the unintuitive finegrained control
of fingertip.
IV. RELATED WORKS
Retargeting Retargeting is an important step in teleopera-
tion. Some works propose to use joint-space retargeting [11],
[12], which maps the joint of the human hand to that of
the robot hand through some predefined mapping. Although
this approach is intuitive in some cases, it fails to provide
precise control in general due to differences in kinematic
structure between the robot hand and the human hand. Some
works also propose direct cartesian mapping [2] from human
hand keypoint to robot hand keypoint and use an inverse
kinematics model to decide the hand joints. Most of the
recent works in robot hand teleoperation apply this cartesian
keypoint mapping approach. However, specifying keypoint
mapping is nontrivial as we discussed and they can lead
to unnatural hand poses. Instead of using some heuristic
cartesian mapping rule (e.g. linear rule), in this paper we
propose novel objectives based on local motion and global C-
space matching, avoiding the challenge of designing complex
heuristics. In the retargeting literature, some works also
consider task-oriented retargeting which takes object state
as input [13], and this setup is different from ours. However,
we believe that our proposed regularization can also be used
to improve these methods. We refer readers to [14] for a
comprehensive review of existing retargeting approaches.
Shape Correspondence Our idea is also related to shape
correspondence research in vision and 3D data processing
research. The goal of shape correspondence is to find some
homeomorphic mapping between two manifolds [15], and the
idea can also be applied to direct cartesian mapping (retarget-
ing). Existing work typically defines some form of energy or
cost functional for the whole mapping, such as elastic energy
to minimize distortion. There is a rich literature on learning
from functional maps, and the proposed methods have been
applied to define a correspondence between different object
shapes (e.g. human to human correspondence) [16], [17],
[18]. However, so far this line of research has not been
applied to retargeting systematically yet. A recent retargeting
work [19], harmonic autoencoder, also leveraged ideas in this
field (e.g. using chamfer loss) to improve mapping quality.
However, it also uses pairwise human-to-robot data in train-
ing. In contrast, we propose using motion and flatness losses
as supervision, which makes our method fully unsupervised.
V. CONCLUSION
In this paper, we have presented Geometric Retargeting
(GeoRT) a fast, efficient, and principled approach to neu-
ral hand retargeting for teleoperation, integrated into the
Dexterity Gen (DexGen) system. GeoRT achieves state-of-
the-art speed with minimal hyperparameters compared to
existing methods. Its unsupervised training eliminates the
need for manual hand pair annotations, while its novel
geometric objective functions ensure both motion fidelity
and C-space coverage. GeoRT’s high-speed performance and
scalability make it a practical and flexible solution for real-
time hand retargeting without the need for intensive test-time
optimization.
ACKNOWLEDGMENTS
This work was partially carried out during Zhao-Heng
Yin’s intern at the Meta FAIR Labs. This work is supported
by the Meta FAIR Labs. Zhao-Heng Yin’s research is sup-
ported by ONR MURI N00014-22-1-2773. Pieter Abbeel
holds concurrent appointments as a Professor at UC Berkeley
and as an Amazon Scholar. This paper describes work per-
formed at UC Berkeley and is not associated with Amazon.
REFERENCES
[1] Zhao-Heng Yin, Changhao Wang, Luis Pineda, Francois Hogan, Kr-
ishna Bodduluri, Akash Sharma, Patrick Lancaster, Ishita Prasad, Mri-
nal Kalakrishnan, Jitendra Malik, et al. Dexteritygen: Foundation con-
troller for unprecedented dexterity. arXiv preprint arXiv:2502.04307,
2025.
[2] Ankur Handa, Karl Van Wyk, Wei Yang, Jacky Liang, Yu-Wei Chao,
Qian Wan, Stan Birchfield, Nathan Ratliff, and Dieter Fox. Dexpilot:
Vision-based teleoperation of dexterous robotic hand-arm system. In
International Conference on Robotics and Automation (ICRA), 2020.
[3] Yuzhe Qin, Wei Yang, Binghao Huang, Karl Van Wyk, Hao Su,
Xiaolong Wang, Yu-Wei Chao, and Dieter Fox. Anyteleop: A general
vision-based dexterous robot arm-hand teleoperation system.
In
Robotics: Science and Systems (RSS), 2023.
[4] Runyu Ding, Yuzhe Qin, Jiyue Zhu, Chengzhe Jia, Shiqi Yang, Ruihan
Yang, Xiaojuan Qi, and Xiaolong Wang. Bunny-visionpro: Real-time
bimanual dexterous teleoperation for imitation learning. arXiv preprint
arXiv:2407.03162, 2024.
[5] Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, and Xiaolong Wang.
Open-television: Teleoperation with immersive active visual feedback.
In Conference on Robot Learning (CoRL), 2024.
[6] Chen Wang, Haochen Shi, Weizhuo Wang, Ruohan Zhang, Li Fei-
Fei, and C Karen Liu.
Dexcap: Scalable and portable mocap data
collection system for dexterous manipulation. In Robotics: Science
and Systems (RSS), 2024.
[7] Patrick Naughton, Jinda Cui, Karankumar Patel, and Soshi Iba. Respi-
lot: Teleoperated finger gaiting via gaussian process residual learning.
In Conference on Robot Learning (CoRL), 2024.
[8] Aravind Sivakumar, Kenneth Shaw, and Deepak Pathak.
Robotic
telekinesis: Learning a robotic hand imitator by watching humans on
youtube. In Robotics: Science and Systems (RSS), 2022.


<!-- page 8 (ocr) -->
[9] Harry G Barrow, Jay M Tenenbaum, Robert C Bolles, and Helen C
Wolf. Parametric correspondence and chamfer matching: Two new
techniques for image matching. In Proceedings: Image Understanding
Workshop, pages 21–27. Science Applications, Inc, 1977.
[10] Kenneth Shaw, Ananye Agarwal, and Deepak Pathak.
Leap hand:
Low-cost, efficient, and anthropomorphic hand for robot learning. In
Robotics: Science and Systems (RSS), 2023.
[11] Hangxin Liu, Xu Xie, Matt Millar, Mark Edmonds, Feng Gao, Yixin
Zhu, Veronica J Santos, Brandon Rothrock, and Song-Chun Zhu. A
glove-based system for studying hand-object manipulation via joint
pose and force sensing.
In International Conference on Intelligent
Robots and Systems (IROS), 2017.
[12] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani,
John Schulman, Emanuel Todorov, and Sergey Levine.
Learning
complex dexterous manipulation with deep reinforcement learning and
demonstrations. In Robotics: Science and Systems (RSS), 2017.
[13] Arjun S Lakshmipathy, Jessica K Hodgins, and Nancy S Pollard.
Kinematic motion retargeting for contact-rich anthropomorphic ma-
nipulations. arXiv preprint arXiv:2402.04820, 2024.
[14] Roberto Meattini, Raul Suarez, Gianluca Palli, and Claudio Melchiorri.
Human to robot hand motion mapping methods: Review and classifi-
cation. IEEE Transactions on Robotics, 39(2):842–861, 2022.
[15] Teuvo Kohonen. The self-organizing map. Proceedings of the IEEE,
78(9):1464–1480, 1990.
[16] Souhaib Attaiki, Gautam Pai, and Maks Ovsjanikov.
Dpfm: Deep
partial functional maps.
In International Conference on 3D Vision
(3DV), 2021.
[17] Gautam Pai, Jing Ren, Simone Melzi, Peter Wonka, and Maks Ovs-
janikov. Fast sinkhorn filters: Using matrix scaling for non-rigid shape
correspondence with functional maps. In IEEE/CVF Conference on
Computer Vision and Pattern Recognition (CVPR), 2021.
[18] Nicholas Sharp, Souhaib Attaiki, Keenan Crane, and Maks Ovsjanikov.
Diffusionnet: Discretization agnostic learning on surfaces.
ACM
Transactions on Graphics (TOG), 41(3):1–16, 2022.
[19] Eunsuk Chong, Lionel Zhang, and Veronica J Santos. A learning-based
harmonic mapping: Framework, assessment, and case study of human-
to-robot hand pose mapping. The International Journal of Robotics
Research, 40(2-3):534–557, 2021.
