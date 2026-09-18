<!-- page 1 (ocr) -->
BiDexGrasp: Coordinated Bimanual Dexterous
Grasps across Object Geometries and Sizes
Mu Lin1,3,∗, Yi-Lin Wei1,∗, Jiaxuan Chen1, Yuhao Lin1, Shuoyu Chen1, Zhizhao Liang1, Jiangran Lyu2,
Jiayi Chen2, Xiaoyi Fan5, Chengyi Xing4, Yansong Tang3, He Wang2, Wei-Shi Zheng1,†
1 Sun Yat-sen University 2 Peking University 3 Tsinghua University
4 Stanford University 5 Jiangxing Intelligence (Guizhou) Technology Inc.
https://frenkielm.github.io/BiDexGrasp.github.io/
(a) Simulation Dataset
(b) IK Configuration
(c) Real-World Deployment
Figure 1: Overview of BiDexGrasp. We construct a large-scale, high-quality dataset of coordinated bimanual
dexterous grasps with diverse object geometries and sizes, along with feasible IK configurations in tabletop
setting. Based on this dataset, we propose a novel data-driven learning-based framework to generate physically
feasible dexterous grasps on unseen objects in the real world.
Abstract: Bimanual dexterous grasping is a fundamental and promising area in
robotics, yet its progress is constrained by the lack of comprehensive datasets and
powerful generation models. In this work, we propose BiDexGrasp, consisting
of a large-scale bimanual dexterous grasp dataset and a novel learning-based
framework. For dataset construction, we propose a novel bimanual grasp synthesis
pipeline to efficiently annotate physically feasible data. This pipeline addresses the
challenges of high-dimensional bimanual grasping through a two-stage synthesis
strategy of efficient region-based grasp initialization and decoupled force-closure
grasp optimization. Powered by this pipeline, we construct a large-scale bimanual
dexterous grasp dataset, comprising 6351 diverse objects with sizes ranging from
30 to 80 cm, along with 9.53 million annotated grasp data. Based on this dataset, we
further introduce a novel learning-based dexterous grasping generation framework.
The framework lies in two key designs: a bimanual coordination module and
a geometry-size-adaptive grasp generation strategy to generate coordinated and
high-quality grasps on unseen objects. Extensive experiments conducted in both
simulation and real world demonstrate the superior performance of our proposed
data synthesis pipeline and learned generative framework.
arXiv:2604.06589v2  [cs.RO]  8 Sep 2026
pit
we
js) Se Je
on
7
|
-
=
=
:
;
og!
AW
wn
fio
wn
pr
IE
Sg
~
Lely
dk
®H
=
A
U
«
L&D
Fo
NES


<!-- page 2 (ocr) -->
1
Introduction
Robotic dexterous grasping enables human-like object interaction [1, 2, 3, 4, 5, 6, 7, 8]. Data-driven
approaches achieve promising results, showing demands for high-quality datasets and advanced
generative models [9, 10, 11, 12, 13]. Most prior studies concentrate on single-hand grasping [14,
15, 16, 17, 18]. However, diverse object shapes and sizes restrict single-hand manipulation, making
bimanual dexterous grasping indispensable.
Currently, several recent studies explore data synthesis and data-driven methods for bimanual dex-
terous grasping [19, 20] but still restricted to objects of limited size and geometry. We attribute this
to the dual challenges of varied object sizes and the enlarged bimanual search space, which jointly
degrade synthesis efficiency and grasp quality. To address this, we introduce BiDexGrasp in this work,
which contributes a large-scale, high-quality bimanual grasp dataset produced by a novel synthesis
pipeline, together with a bimanual-coordinated, geometry- and size-adaptive generation framework
that learns from this dataset to produce high-quality grasps on diverse unseen objects.
For dataset construction, we propose an effective bimanual dexterous grasp synthesis pipeline to
address the increased complexity and low efficiency caused by the expanded action space. For
efficiency, we introduce a bimanual region-constrained grasp initialization strategy to generates
coordinated and physically feasible candidates. For quality, we propose a decoupled force-closure
grasp optimization strategy that separates the force-closure constraints of each hand, reducing
optimization complexity while preserving high-quality per-hand grasps. With this pipeline, we build
a large dataset of 9.53M grasps over 6,351 objects spanning diverse geometries and scales (Tab. 1).
Built on this dataset, we propose the BiDexGrasp framework for high-quality grasp generation on
diverse unseen objects, tackling two challenges: bimanual coordination and generalization across
geometries and scales. To enhance coordination, we introduce a bimanual coordination module to
predict coordinated grasp views, to guide the grasp poses generation. To enhance adaptability, we
propose a geometry-size-adaptive grasp strategy that compactifies the action space and emphasizes
local structural learning, greatly improving robustness to diverse object geometries and scales.
Extensive simulation and real-world experiments validate both the synthesis pipeline and the genera-
tion framework. Our pipeline achieves over 2.8× higher success rate and 30× faster synthesis than
prior work, and our framework attains 66.8% success in simulation and 74.6% on real experiments,
demonstrating consistently strong performance across both settings.
2
Related work
2.1
Bimanual Dexterous Grasp
Bimanual dexterous grasping extends grasping to large and heavy objects but remains underex-
plored due to the high dimension of the combined degrees of freedom. Reinforcement learning
approaches [21, 22] suffer from limited scalability and heavy reliance on hand-crafted rewards, while
data-driven methods [19, 20, 23] are constrained by the lack of high-quality datasets and suboptimal
model architectures. In this work, we address these challenges with a large-scale dataset with high
diversity and quality, and a novel generative framework tailored for bimanual dexterous grasping.
2.2
Dexterous Grasp Dataset
The availability of large-scale and high-quality datasets is crucial for the development of robotic [9, 11,
13, 24]. Previous research on single-hand dexterous grasping has explored energy-based optimization
methods [25, 10, 14, 15, 26, 27], enabling parallel synthesis of large-scale dexterous grasping data.
However, in the bimanual setting, the expanded action space and coordination requirements push
existing pipelines [19, 20, 23] into low efficiency and over-reliance on single-hand data, yielding
datasets of narrow object diversity. In this work, we introduce a novel bimanual grasp synthesis
pipeline and a corresponding large-scale dataset with broad geometric and scale coverage.
2


<!-- page 3 (ocr) -->
Table 1: Comparison with previous dexterous grasping datasets
Dataset
Bim.
Obj
Grasp
Max
Range
Table
IK
Pre-Grasp
Data Independent
DexGraspNet[10]
×
5355
1.32M
30cm
28cm
×
×
×
✓
BODex[25]
×
2397
3.08M
24cm
12cm
✓
✓
✓
✓
DHAGrasp[20]
✓
802
1.30M
30cm
20cm
×
×
×
×
BimanGrasp[19]
✓
900
0.15M
40cm
20cm
×
×
×
✓
BiDexGrasp
✓
6351
9.53M
80cm
50cm
✓
✓
✓
✓
2.3
Data-Driven Dexterous Grasp Framework
Data-driven dexterous grasping frameworks have shown strong generalization to unseen objects [28,
29, 30]. Most existing methods rely on generative models [16, 31, 32], and extended through richer
conditioning [33], dedicated training objectives and strategy [34, 35], physical-guided sampling [36]
or bimanual extensions [19, 5]. However, they limit in the adaptation to diverse object geometries and
sizes. In this paper, drawing inspiration from prior methods [11], our framework explicitly models
bimanual coordination, producing robust bimanual grasps across object geometry and scale.
3
Preliminaries
Grasp Wrench Space (GWS). Given an object with m contact points, each contact i is characterized
by a position pi, surface normal ni, and a friction-cone-constrained local force fi, which together
induce a 6D wrench wi = Gifi via the grasp matrix Gi. The set of feasible wrenches at contact i
is denoted Wi, and the overall grasp wrench space is the Minkowski sum W =
m
i=1 Wi, which
characterizes all wrenches the grasp can exert on the object. The minimum distance from the origin to
the GWS boundary (GWB) reflects contact stability—a larger distance indicates a more stable grasp.
QP-Energy. To evaluate the ability of a grasp to resist external disturbances, we adopt a differentiable
metric based on quadratic programming. Given six target disturbance wrenches {tj}6
j=1 along the
±x, ±y, ±z axes, the energy is defined as Q =
6
j=1 minwj∈W ∥βtj −wj∥2, where β is a scaling
factor. Intuitively, Q measures how well the grasp wrench space W can approximate disturbance
directions. The detailed grasp matrix and QP formulation are provided in Appendix A.
4
BiDexGrasp Dataset
4.1
Overview
Problem Definition. Given the object mesh O, the goal of grasp data synthesis is to obtain bimanual
dexterous grasp poses Gbi = (Gleft, Gright) = ((tr, rr, qr), (tl, rl, ql)), where r and t refer to the
rotation and translation of hand wrist, and q refers to the joint poses of dexterous hand.
Synthesis Overview. We first collect 6,351 objects from [10] and [37] and scale each to 11 discrete
sizes from 30 to 80 cm. The synthesis pipeline is consisted of three stages as shown in Figure 2.
4.2
Bimanual Region-constraint Grasp Initialization
Challenges for Bimanual Grasp Initialization. Naively extending single-hand initialization causes
quadratic sampling complexity, and most random pairs violate bimanual constraints. We address
this with a bimanual region-constrained initialization strategy: grasping region candidates are first
selected via the grasp wrench space (GWS), and initial poses are then sampled within these regions,
yielding both efficient and reliable initialization.
GWS-based Bimanual Grasping Region Selection. This module leverages GWS energy to ef-
ficiently filter bimanual grasping regions with the potential for stable, physically feasible grasps.
Specifically, the region selection process consists of 3 steps. (1) We first apply farthest point sampling
to select Ka = 200 anchors and sample k = 256 points within an 8 cm neighborhood around each
anchor to define Ka regions and K2
a region pairs. (2) We exclude the pairs with insufficient inter-
region distance, and evaluate the remain pairs’ stability using the Grasp Wrench Boundary (GWB)
3
2
x


<!-- page 4 (ocr) -->
Object Set
GWS-based Region Selection
Region Sampling
1
GWB Evaluation
2
Top-K Seclection
3
Region-based Initialization
Objaverse + DexGraspNet 
Scaling(30cm-80cm)
6351 Objects
11 Scale
Collision & IK Filter
Decoupled Force-Closure Optimization
BiDexGrasp Dataset
IK Configuration
Simulator-based Validation
…
1. Bimanual Region-constraint Grasp Initialization
2. Decoupled Grasping Optimization
3. Validation
Palm and Joint Initialization
𝑠= min
1≤𝑗≤6 max
1≤𝑘≤𝑀𝐭𝐣
⊤𝐰𝐤
Left QP-Enegry
Right QP-Enegry
Contact Distance Energy
Region Distance Energy
Figure 2: The data synthesis pipeline for bimanual grasp. (1) Fast constraint-aware bimanual grasp initialization
for physically feasible grasp bimanual candidate generation. (2) Decoupled force-closure optimization refines
initial candidates into valid bimanual grasps. (3) Arm reachability analysis yields kinematic feasible poses, with
MuJoCo [38] simulation filtering invalid grasps.
estimated by the TDG estimator [39]. Specifically, N = 5 contact points are sampled per region,
and the resulting GWB is represented by a set of boundary wrenches {wk}M
k=1 with M = 1000.
To assess robustness against external disturbances, we adopt the six disturbance wrenches {tj}6
j=1
defined in the preliminaries. The stability score is computed as the minimum projection of the GWB
onto these disturbance directions: s = min1≤j≤6 max1≤k≤M t⊤
j wk. (3) Finally, we rank region
pairs by stability score, and the top Kr = 40 are retained as candidates for grasp initialization.
Region-based Grasp Initialization. Given the selected regions, we initialize bimanual grasps
Ginitial by placing each palm at the closest point on the dilated convex hull to the region center, with
orientation aligned to the surface normal. We then enforce collision checking and inverse kinematics
(IK) feasibility, discarding invalid configurations before optimization.
4.3
Decoupled Grasping Optimization
Challenges for Bimanual Grasp Optimization. Bimanual grasp optimization is inherently chal-
lenging because the enlarged search space induces a tightly coupled objective that destabilizes
optimization and often yields imbalanced solutions, where one hand dominates stability while the
other contributes marginally, leading to suboptimal local minima.
Decoupled Force Closure. To obtain high-quality and physically feasible bimanual grasps, we
propose a novel optimization strategy which decompose the bimanual force closure energy into single-
hand energy terms, allowing each hand to focus on establishing stable local contacts. This decoupling
reduces optimization complexity and discourages single-hand-dominated solutions, improving both
grasp quality and convergence stability. Specifically, we formulate the overall optimization as follows
to optimize Gbi by minimizing the QP-Energy decoupled into two single-hand energy terms:
min
Gbi (wQP Q(Gleft) + wQP Q(Gright) + wdisEdis + wregionEregion),
s.t.
Gbi
min ≤Gbi ≤Gbi
max,
ci,w = FK(Gbi, ci,l),
No collision.
(1)
ci,l and ci,w denote the positions of the predefined hand contact point i expressed in the local link
frame and the world frame. In the QP formulation, the grasp matrix is constructed by associating each
ci,w with its closest point pi on the object surface, while feasibility is ensured through joint-limit and
collision-avoidance constraints. We introduce a distance term Edis to encourage proximity between
ci,w and pi, and a region consistency term Eregion to keep the contacts close to the initialized contact
regions. The detailed formulations are provided in Appendix B and A.
4.4
Kinematics-Aware Arm-Hand Configuration Synthesis
To demonstrate the practical feasibility of the synthesized grasps, our framework supports solving
the inverse kinematics (IK) for wrist poses, enabling reachable tabletop configurations. To avoid
collisions and facilitate force application, we first synthesize a pre-grasp pose Gbi
pre, maintaining a
4
008
0 esp
<2
vik FY = =p -
WELT
Ee TE


<!-- page 5 (ocr) -->
𝑠𝑒𝑙𝑒𝑐𝑡 best view
𝑳𝒐𝒔𝒔single−view
0 3.10 1.1… 1.9
𝐯𝟏
…
𝐯𝟐𝐯𝟑𝐯𝟒
𝐯𝐤
0 3 0 1 … 2
𝑙𝑎𝑏𝑒𝑙single
0 0.10 0 … 0
1.10 0 2.1… 0
0 0 0 0 … 0.2
0.10 0.80 … 0
…
0 0.90 0 … 1.1
…
…
…
…
…
0 0 0 0 … 0
1 0 0 2 … 0
0 0 0 0 … 0
0 0 1 0 … 0
…
0 1 0 0 … 1
…
…
…
…
…
𝑳𝒐𝒔𝒔𝒃𝒊−view
𝑙𝑎𝑏𝑒𝑙𝑏𝑖
𝐯𝟏,𝟏𝐯𝟏,𝟐𝐯𝟏,𝟑𝐯𝟏,𝟒
𝐯𝟏,𝐤
𝐯𝟐,𝟏𝐯𝟐,𝟐𝐯𝟐,𝟑𝐯𝟐,𝟒
𝐯𝟐,𝐤
𝐯𝟑,𝟏𝐯𝟑,𝟐𝐯𝟑,𝟑𝐯𝟑,𝟒
𝐯𝟑,𝐤
𝐯𝟒,𝟏𝐯𝟒,𝟐𝐯𝟒,𝟑𝐯𝟒,𝟒
𝐯𝟒,𝐤
𝐯𝐤,𝟏𝐯𝐤,𝟐𝐯𝐤,𝟑𝐯𝐤,𝟒
𝐯𝐤,𝐤
…
…
…
…
…
… …
…
…
…
…
𝒗𝒊,𝒋= 𝒇(𝒗𝒊, 𝒗𝒋)
𝑠𝑒𝑙𝑒𝑐𝑡 coordinated bi-views
𝒗𝟐
𝒗𝟒
Point Filter
Local features
𝒗𝟐
𝒗𝟒
Relative Dexterous 
Grasp Diffusion
𝑥1
𝑦1
𝑧1
𝑥2
𝑦2
𝑧2
𝑥3
𝑦3
𝑧3
𝑥4
𝑦4
𝑧4
𝑥5
𝑦5
𝑧5
𝑥6
𝑦6
𝑧6
𝑥𝑘
𝑦𝑘
𝑧𝑘
…
Grasp View
Object Point Cloud
Noise Hand Pose
View Feature Extractor
View features
𝐯𝟐𝐯𝟒
Bimanual Coordination Module 
Geometry - Adaptive Feature
Grasp based on Scale
- Adaptive Anchor
global
features
Figure 3: BiDexGrasp Framework. Given the input object point cloud and pre-defined grasp view, the framework
first predicts a pair of coordinated grasp views for the two hands by Bimanual Coordination Module. Based on
this view, we extract geometry-adaptive object feature and determine the scale-adaptive grasp. Then the relative
grasp diffusion is employed to predict relative dexterous grasp form the grasp anchor.
contact distance of 1cm, following [25]. And we compute a squeeze pose as the execution target:
Gbi
squ = 2 · Gbi −Gbi
pre. Finally, we generate arm joint trajectories from pre-grasp to squeeze and lift.
5
BiDexGrasp Framework
Problem Definition. To learn generable bimanual dexterous grasp, we design a data-driven generation
model which take object point cloud Opc as input and generate bimanual dexterous grasp poses Gbi.
Challenge in Bimanual Grasping. Bimanual grasp generation introduces two key challenges. (1)
Bimanual coordination: Bimanual hands must collaboratively target optimal grasp view to ensure
global stability while avoiding inter-hand collisions. (2) Adaptation across object geometries and
sizes: The vast diversity in object sizes and geometries greatly hinders efficient model learning,
increasing the difficulty of object feature extraction and expanding the action space simultaneously.
Model Overview. To address these challenges, we propose BiDexGrasp, which achieves bimanual-
coordinated and geometry-size-adaptive grasp generation through two components: (1) a bimanual
coordination module that explicitly models inter-hand relationships via coordinated-view prediction;
(2) a geometry-size-adaptive generation strategy that improves cross-object generalization through
adaptive grasp anchors. The model pipeline is shown in Fig. 3.
5.1
Bimanual Coordination Module.
To explicitly model bimanual coordination, we first estimate coordination-aware grasping views to
guide subsequent grasp prediction. The module first predicts the most promising view as the primary
grasping view, and predicts the second view that is most compatible with the primary view.
Specifically, we uniformly sample K discrete approach directions on the object bounding sphere to
construct a candidate view set V = {vi}K
i=1, which formulate view estimation as a view probabilistic
regression. To predict the primary view, we introduce K learnable view embeddings vemb
i
to extract
view features Fview = {fi}K
i=1 by cross-attention: fi = Attn(vemb
i
, Fglobal, Fglobal) , where Fglobal
are point features extracting by PointNet++ [40]. To predict the second view, we model interactions
between the primary view and the remaining candidate views to construct bi-view features by a MLPs
layer: f bi
i,j = MLP cat(fi, fj, fi −fj, fi ⊙fj) . These features predict the single-view and bi-view
probabilities pi and pbi
i,j, supervised by SmoothL1 losses against ground-truth probabilities yi and ybi
i,j
derived from the successful-grasp distribution of each object. For single-view, we assign each grasp
to the nearest predefined candidate view, then count the number of grasps associated with each view
and normalize these counts to form a probability. Similarly, the bi-view ground-truth probabilities are
5
Grasp View
Bimanual Coordination Module
[IIIT
— [| Ht
for
To
—
-
v
LZ
GT
Canam
EEEEEN
(Of ofo] 17]
1
1
Object Point Cloud
|
Geometry-Adaptive Feature
iTTY
I
TH
Eo
—
wit BEE
i
FEN
H
Beri
dpa —oR eR
wi
arn
a
EA 4
2
Noise
Hand Pose
v
Grasp based on Scale-Adaptive Anchor
-
8
aN
N
-
.


<!-- page 6 (ocr) -->
Table 2: Performance comparison of dual-arm grasping on DexGraspNet and Objaverse datasets.
Method
SUC-F↑
SUC-L↑
SUC-A↑
S↑
PD↓
SPD↓
CDC↓
D↓
DexGraspNet
BimanGrasp [19]
26.80
–
–
0.16
1.52
0.26
1.87
0.150
Ours(Float)
75.84
–
–
6.73
0.17
0.02
0.59
0.190
Ours(TableTop)
77.11
80.83
71.34
6.87
0.15
0.02
0.52
0.165
Objaverse
BimanGrasp [19]
30.21
–
–
0.16
0.87
0.23
1.38
0.156
Ours(Float)
70.82
–
–
4.55
0.20
0.04
0.67
0.180
Ours(TableTop)
62.41
70.41
62.40
5.10
0.20
0.05
0.67
0.158
obtained by considering pairs of grasps. Each grasp pair is mapped to the nearest candidate view pair,
and the counts are normalized over all candidate pairs to produce a probability ground-truth.
5.2
Geometry-Size-Adaptive Grasp Generation Strategy
Figure 4: Visualization of grasp anchors.
Scale-Adaptive Grasp Anchor To improve adaptability to
object size, we formulate the grasp wrist prediction as a
relative pose (∆t, ∆r) prediction with respect to a grasp
anchor ganchor = (tanchor, rancho), which is adapted to the
size of the object.
tpred = tanchor + ∆t,
rpred = ranchor ⊕∆r.
(2)
The adaptive grasp anchor is determine dynamically according to the grasp view and object point
cloud. Specifically, each predicted view intersects with minimum bounding sphere surface, producing
an grasp anchor. This anchor-based formulation converts the original absolute pose prediction
problem into a relative regression task, significantly reducing the search space of grasps and improve
the adaptation to object scale.
Geometry-Adaptive Object Feature To improve adaptability to object geometry, we extract local
geometric features around each predicted grasp anchor, as global features may be dominated by
irrelevant structures. Specifically, the global point cloud is first upsampled into Kp representative
points using farthest point sampling (FPS). For each predicted grasp anchor, features are then
aggregated from its Kc-nearest neighbors (KNN). This local feature Flocal captures fine-grained
surface geometry around potential contact regions while filtering out distant or grasp-irrelevant
structures, which facilitates geometry-adaptive grasp generation. Finally, the local features, view
features, and global features are concatenated along the token dimension to form the final object
feature representation.
Fga−obj = Concat Flocal, Fview, Fglobal .
(3)
Relative Dexterous Grasp Diffusion We propose a relative dexterous grasp diffusion to generate
bimanual relative wrist poses (∆tbi, ∆rbi) and dexterous joint poses qbi, based on the scale-adaptive
grasp anchor ganchor = (tanchor, ranchor) and geometry-adaptive object feature Fga−obj. We adopt
the DDPM sampling process [41], which can be formalized as follows:
pθ(Gbi,rela
0:T
| Fga-obj) = p(Gbi,rela
T
) ×
T
t=1
pθ Gbi,rela
t−1
Gbi,rela
t
, Fga-obj ,
(4)
where Gbi,rela = (∆tbi, ∆rbi, qbi), and p(Gbi,rela) is modeled as a Gaussian distribution. During
training, we apply L2 losses separately to the translation, rotation, and joint parameter regressions.
In addition, we incorporate Chamfer loss [42] to explicitly supervise hand geometry. We further
introduce a physics-based loss to penalize hand–object penetration as well as intra- and inter-hand
self-penetration. All details could be found in Appendix C.
L = λsingle-viewLsingle-view + λbi-viewLbi-view + λparaLpara + λchamferLchamfer + λphysicLphysic.
(5)
6
VOY
II
|


<!-- page 7 (ocr) -->
Table 3: Ablation of data synthesis.
Method
SUC-L SUC-A SGS
PD
SPD
Baseline
28.3
12.9
2.1
0.18 0.08
+R
44.4
39.8
2.8
0.13 0.03
+R+Dc
57.7
49.5
4.0
0.15 0.03
+R+Dc+Ps
80.8
71.3
5.6
0.15 0.03
Table 4: Comparison with SOTAs.
Method SUC-L
PD
SPD CDC
D
[17]
15.2
3.29 0.11
3.79
0.174
[43]
41.5
2.24 0.13
3.02
0.201
Ours
66.8
1.53 0.01
2.32
0.197
Table 5: Ablation of framework.
BCM GAF SAGA SUC-L
PD
SPD CDC
×
×
×
41.2
2.25 0.01 2.87
×
✓
✓
44.7
2.28 0.01 2.96
✓
✓
×
52.7
2.05 0.02 2.82
✓
✓
✓
61.9
1.73 0.02 2.56
6
Experiments
6.1
Experiment Settings
Data Synthesis. Evaluation is conducted in MuJoCo with Shadow Hand, using tangential/torsional
friction coefficients of 0.6/0.02, gravity 9.8 m/s2, object density 2.5 kg/m3. We randomly sample
1,000 objects from DexGraspNet and Objaverse, scale each to 6 sizes (30–80 cm) to form 12,000
instances, synthesizing 5 grasps per instance (60,000 grasps per method). For [19], pre-grasp and
squeeze poses are obtained by translating the palm by ±1 cm and perturbing finger joints by ±0.1 rad.
Generation Framework. The generation framework evaluation is conduct on the DexGraspNet
subset of our tabletop dataset. The dataset consists of 2,397 objects, which are randomly split into
training and test sets with a 4:1 ratio, resulting in 3,112,117 training grasps. During evaluation, for
each test object, we generate 3 grasps for every object pose and scale, yielding a total of 139,956
grasps, which are evaluated under the same evaluation as data generation pipeline.
6.2
Implements Details
Data Synthesis. We set wQP = 1000, wdis = 100, wregion = 50, and generate the dataset on eight
NVIDIA 3090 GPUs with 40 parallel worlds per GPU and 20 grasps per world.
Generation Framework. We set K = 16, Kp = 256 and Kc = 16. For the comparison experiments,
we train models for 5 epochs. For the ablation studies, models are trained for 20 epochs on a subset
that includes all object scales but only one tabletop pose per object. All experiments are implemented
in PyTorch and conducted on single RTX 4090 GPU. Additional details are provided in Appendix C.
6.3
Evaluation Metrics
Following [25], we evaluate the data synthesis pipeline and generation framework with the following
metrics (see Appendix D for full definitions). Grasp Success Rate (SUC) (%) measures grasp
robustness in simulation under three settings: force-closure against 6 external disturbances (SUC-F),
tabletop lifting with a floating hand (SUC-L), and with an arm-controlled hand (SUC-A). Speed (S)
and Success Generation Speed (SGS) (grasps/s) quantify raw and successful synthesis throughput.
Penetration Depth (PD) (cm) and Self-Penetration Depth (SPD) (cm) measure the physical plausi-
bility of hand–object contact and of the hand configuration itself (intra- and inter-hand collisions),
respectively. Contact Distance Consistency (CDC) (cm) characterizes the uniformity of finger
contacts, and Diversity (D) (%) the diversity of the generated grasp distribution.
6.4
Data Synthesis Experiments
Comparison Results. We compare with BimanGrasp, a representative open-source bimanual grasp
synthesis pipeline. Since BimanGrasp is restricted to floating-base grasp generation, we evaluate our
method in both floating and tabletop settings for a fair comparison. Tab. 2 shows that our pipeline
significantly outperforms prior work in both quality (SUC, PD, SPD, CDC) and speed (S). On
DexGraspNet, we increase the SUC by roughly 2.8× under both floating-hand and tabletop settings,
with a 40× synthesis speedup. On Objaverse, which features more complex geometries, our method
maintains strong success rates and high synthesis efficiency.
Ablation Study. Tab. 3 shows the ablation study for each component of our synthesis pipeline. The
baseline is a straightforward extension of BODex from the single-hand setting to a bimanual setup.
7


<!-- page 8 (ocr) -->
Inspire Hands
BrainCo Hands
Inspire Hands
Object Set
Figure 5: Real-world experiments. Left: qualitative grasp results. Right: hardware setup and object set.
The results show that R (Region Initialization), Dc (Decoupled Force-Closure) and Ps (Pre-grasp
Strategies) all contribute to improving grasp success rate (SUC-L and -A) and synthesis speed (SGS).
6.5
Generation Framework Experiments
Comparison Results. Tab. 4 reports our method against recent SOTA approaches. Our method
achieves the highest SUC with the lowest PD and SPD, indicating precise and stable grasps. While
diversity is slightly lower, this trade-off is acceptable since our task prioritizes grasp success. Overall,
our method outperforms prior methods in both feasibility and reliability.
Ablation Study. Tab. 5 evaluates each component over a DDPM-based bimanual baseline. The
Bimanual Coordination Module (BCM) substantially raises SUC, confirming its role in coordinating
dual-hand grasps. The Geometry-Adaptive Feature (GAF) and Scale-Adaptive Grasp Anchor (SAGA)
adapt to local geometry and object scale, jointly boosting SUC and reducing SPD and CDC.
6.6
Real-World Experiments
We conduct real-world experiments with two dexterous hands (Inspire and BrainCo) and three robotic
arms (Unitree G1, Piper, and Nero), performing 260 trials on 30 objects (setup and qualitative results
in Fig. 5). We evaluate two input settings: single-view and full point clouds. For single-view, we
extract object point clouds from RGB-D images via a segmentation model [44]. For full point clouds,
we reconstruct object meshes [45], estimate 6D poses [46], and sample the point cloud. ShadowHand
grasps are retargeted [35] to the Inspire and BrainCo hands. Our method achieves 66.0% success on
single-view and 76.7% on full point clouds, averaging 74.6%.
7
Conclusion
We present BiDexGrasp, a comprehensive solution that advances bimanual dexterous grasping through
both a large-scale dataset and a learning-based framework. Our synthesis pipeline yields a dataset of
6,351 diverse objects with 9.53M annotated grasps, on which our generation framework produces
high-quality grasps for unseen objects. Extensive experiments in simulation and the real world show
that our pipeline significantly improves synthesis efficiency and quality, and our framework generates
coordinated, high-quality grasps across diverse objects.
8
Limitations
First, our synthesis pipeline assumes fixed hand contact points, which restricts the contact-space
diversity of generated grasps. Second, our method is stability-oriented and may struggle on tasks
requiring specific functional contacts; integrating semantic priors into the bimanual grasping region
is a promising direction. Finally, our model operates in the floating-hand setting and does not use the
dataset’s IK configurations; joint arm-hand prediction is a natural extension for future work.
8
4
wv
a
Ir
7
-
(|
3
[CE——
aay
's
Nir Lp
8
8”
I’
I
rr Hr
We
HN
=Q
Yh >
it a
JRE”
=]
4
p
a NE 3)
I]
-
v
d
3
4
va
sa
|
:
[)
4
JOTI
Sgt
TN
came
¢
(mu lg
1. Er
NI
Ey
EE
EE
—
Sg
a—
2)
a
as
(vy Iw
k
’)
No
LDR
2A
Ll
at
CB
i
)
lo
AP
“BI
=
n
=)
So
=
iw
»
ay a
X
y
A
ALY
-
E
&
RR.
>
a Lh >
Tay IRN
TAS Rs Ele
eh
ae alA \'SP
135
\SR vy
l70
nae


<!-- page 9 (ocr) -->
References
[1] H. Zhang, Z. Wu, L. Huang, S. Christen, and J. Song. Robustdexgrasp: Robust dexterous
grasping of general objects. arXiv preprint arXiv:2504.05287, 2025.
[2] Y. Zhong, X. Huang, R. Li, C. Zhang, Z. Chen, T. Guan, F. Zeng, K. N. Lui, Y. Ye, Y. Liang,
et al. Dexgraspvla: A vision-language-action framework towards general dexterous grasping.
arXiv preprint arXiv:2502.20900, 2025.
[3] Y. Cui, Y. Zhang, L. Tao, Y. Li, X. Yi, and Z. Li. End-to-end dexterous arm-hand vla policies
via shared autonomy: Vr teleoperation augmented by autonomous hand vla policy for efficient
data collection. arXiv preprint arXiv:2511.00139, 2025.
[4] K. Li, P. Li, T. Liu, Y. Li, and S. Huang. Maniptrans: Efficient dexterous bimanual manipulation
transfer via residual learning. In Proceedings of the Computer Vision and Pattern Recognition
Conference, pages 6991–7003, 2025.
[5] K. Shaw, Y. Li, J. Yang, M. K. Srirama, R. Liu, H. Xiong, R. Mendonca, and D. Pathak.
Bimanual dexterity for complex tasks. arXiv preprint arXiv:2411.13677, 2024.
[6] Y.-L. Wei, Z. Luo, Y. Lin, M. Lin, Z. Liang, S. Chen, and W.-S. Zheng. Omnidexgrasp:
Generalizable dexterous grasping via foundation model and force feedback. arXiv preprint
arXiv:2510.23119, 2025.
[7] H. Yuan, Z. Huang, Y. Wang, C. Mao, C. Xu, and Z. Lu. Demograsp: Universal dexterous
grasping from a single demonstration. arXiv preprint arXiv:2509.22149, 2025.
[8] Y. Lin, Y.-L. Wei, H. Liao, M. Lin, C. Xing, H. Li, D. Zhang, M. Cutkosky, and W.-S. Zheng.
Typetele: Releasing dexterity in teleoperation by dexterous manipulation types. arXiv preprint
arXiv:2507.01857, 2025.
[9] H.-S. Fang, C. Wang, M. Gou, and C. Lu. Graspnet-1billion: A large-scale benchmark for
general object grasping. In Proceedings of the IEEE/CVF conference on computer vision and
pattern recognition, pages 11444–11453, 2020.
[10] R. Wang, J. Zhang, J. Chen, Y. Xu, P. Li, T. Liu, and H. Wang. Dexgraspnet: A large-
scale robotic dexterous grasp dataset for general objects based on simulation. arXiv preprint
arXiv:2210.02697, 2022.
[11] J. Zhang, H. Liu, D. Li, X. Yu, H. Geng, Y. Ding, J. Chen, and H. Wang. Dexgraspnet 2.0:
Learning generative dexterous grasping in large-scale synthetic cluttered scenes. In 8th Annual
Conference on Robot Learning, 2024.
[12] J. He, D. Li, X. Yu, Z. Qi, W. Zhang, J. Chen, Z. Zhang, Z. Zhang, L. Yi, and H. Wang. Dexvlg:
Dexterous vision-language-grasp model at scale. arXiv preprint arXiv:2507.02747, 2025.
[13] J. Ye, K. Wang, C. Yuan, R. Yang, Y. Li, J. Zhu, Y. Qin, X. Zou, and X. Wang. Dex1b: Learning
with 1b demonstrations for dexterous manipulation. arXiv preprint arXiv:2506.17198, 2025.
[14] T. Liu, Z. Liu, Z. Jiao, Y. Zhu, and S.-C. Zhu. Synthesizing diverse and physically stable grasps
with arbitrary hand structures using differentiable force closure estimator. IEEE Robotics and
Automation Letters, 7(1):470–477, 2021.
[15] M. Liu, Z. Pan, K. Xu, K. Ganguly, and D. Manocha. Deep differentiable grasp planner for
high-dof grippers. arXiv preprint arXiv:2002.01530, 2020.
[16] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, et al.
Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and
goal-conditioned policy. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 4737–4746, 2023.
9


<!-- page 10 (ocr) -->
[17] S. Huang, Z. Wang, P. Li, B. Jia, T. Liu, Y. Zhu, W. Liang, and S.-C. Zhu. Diffusion-based gen-
eration, optimization, and planning in 3d scenes. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 16750–16761, 2023.
[18] L. Shao, F. Ferreira, M. Jorda, V. Nambiar, J. Luo, E. Solowjow, J. A. Ojea, O. Khatib, and
J. Bohg. Unigrasp: Learning a unified model to grasp with multifingered robotic hands. IEEE
Robotics and Automation Letters, 5(2):2286–2293, 2020.
[19] Y. Shao and C. Xiao. Bimanual grasp synthesis for dexterous robot hands. IEEE Robotics and
Automation Letters, 2024.
[20] Q. Li, Z. Wu, J. Wang, C. C. Loy, and B. Dai. Dhagrasp: Synthesizing affordance-aware
dual-hand grasps with text instructions. arXiv preprint arXiv:2509.22175, 2025.
[21] H. Zhang, S. Christen, Z. Fan, L. Zheng, J. Hwangbo, J. Song, and O. Hilliges. Artigrasp:
Physically plausible synthesis of bi-manual dexterous grasping and articulation. In 2024
International Conference on 3D Vision (3DV), pages 235–246. IEEE, 2024.
[22] Y. Chen, Y. Geng, F. Zhong, J. Ji, J. Jiang, Z. Lu, H. Dong, and Y. Yang. Bi-dexhands: Towards
human-level bimanual dexterous manipulation. IEEE Transactions on Pattern Analysis and
Machine Intelligence, 46(5):2804–2818, 2023.
[23] S. Yang, Y. Xie, Z. Liang, Y. Tian, J. Zeng, D. Lin, and J. Pang. Ultradexgrasp: Learning univer-
sal dexterous grasping for bimanual robots with synthetic data. arXiv preprint arXiv:2603.05312,
2026.
[24] Y. Mu, T. Chen, S. Peng, Z. Chen, Z. Gao, Y. Zou, L. Lin, Z. Xie, and P. Luo. Robotwin: Dual-
arm robot benchmark with generative digital twins (early version). In European Conference on
Computer Vision, pages 264–273. Springer, 2024.
[25] J. Chen, Y. Ke, and H. Wang. Bodex: Scalable and efficient robotic dexterous grasp synthesis
using bilevel optimization. In 2025 IEEE International Conference on Robotics and Automation
(ICRA), pages 01–08. IEEE, 2025.
[26] R. Zurbrügg, A. Cramariuc, and M. Hutter. Graspqp: Differentiable optimization of force
closure for diverse and robust dexterous grasping. arXiv preprint arXiv:2508.15002, 2025.
[27] J. Chen, Y. Ke, L. Peng, and H. Wang. Dexonomy: Synthesizing all dexterous grasp types in a
grasp taxonomy. arXiv preprint arXiv:2504.18829, 2025.
[28] H.-S. Fang, H. Yan, Z. Tang, H. Fang, C. Wang, and C. Lu. Anydexgrasp: General dex-
terous grasping for different hands with human-level learning efficiency.
arXiv preprint
arXiv:2502.16420, 2025.
[29] Z. Chen, Q. Yan, Y. Chen, T. Wu, J. Zhang, Z. Ding, J. Li, Y. Yang, and H. Dong. Clutterdex-
grasp: A sim-to-real system for general dexterous grasping in cluttered scenes. arXiv preprint
arXiv:2506.14317, 2025.
[30] L. Huang, H. Zhang, Z. Wu, S. Christen, and J. Song. Fungrasp: functional grasping for diverse
dexterous hands. IEEE Robotics and Automation Letters, 2025.
[31] H. Jiang, S. Liu, J. Wang, and X. Wang. Hand-object contact consistency reasoning for human
grasps generation. In Proceedings of the IEEE/CVF international conference on computer
vision, pages 11107–11116, 2021.
[32] Z. Wei, Z. Xu, J. Guo, Y. Hou, C. Gao, Z. Cai, J. Luo, and L. Shao. D (r, o) grasp: A unified
representation of robot and object interaction for cross-embodiment dexterous grasping. arXiv
preprint arXiv:2410.01702, 2024.
10


<!-- page 11 (ocr) -->
[33] Y.-L. Wei, M. Lin, Y. Lin, J.-J. Jiang, X.-M. Wu, L.-A. Zeng, and W.-S. Zheng. Afforddexgrasp:
Open-set language-guided dexterous grasp with generalizable-instructive affordance. arXiv
preprint arXiv:2503.07360, 2025.
[34] J. Lu, H. Kang, H. Li, B. Liu, Y. Yang, Q. Huang, and G. Hua. Ugg: Unified generative grasping.
In European Conference on Computer Vision, pages 414–433. Springer, 2024.
[35] Y.-L. Wei, J.-J. Jiang, C. Xing, X.-T. Tan, X.-M. Wu, H. Li, M. Cutkosky, and W.-S. Zheng.
Grasp as you say: Language-guided dexterous grasp generation. Advances in Neural Information
Processing Systems, 37:46881–46907, 2024.
[36] Y. Zhong, Q. Jiang, J. Yu, and Y. Ma. Dexgrasp anything: Towards universal robotic dex-
terous grasping with physics awareness. In Proceedings of the Computer Vision and Pattern
Recognition Conference, pages 22584–22594, 2025.
[37] M. Deitke, D. Schwenk, J. Salvador, L. Weihs, O. Michel, E. VanderBilt, L. Schmidt, K. Ehsani,
A. Kembhavi, and A. Farhadi. Objaverse: A universe of annotated 3d objects. In Proceedings
of the IEEE/CVF conference on computer vision and pattern recognition, pages 13142–13153,
2023.
[38] E. Todorov, T. Erez, and Y. Tassa. Mujoco: A physics engine for model-based control. In 2012
IEEE/RSJ international conference on intelligent robots and systems, pages 5026–5033. IEEE,
2012.
[39] J. Chen, Y. Chen, J. Zhang, and H. Wang. Task-oriented dexterous grasp synthesis via differen-
tiable grasp wrench boundary estimator. arXiv preprint arXiv:2309.13586, 2023.
[40] C. R. Qi, L. Yi, H. Su, and L. J. Guibas. Pointnet++: Deep hierarchical feature learning on
point sets in a metric space. Advances in neural information processing systems, 30, 2017.
[41] J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic models. Advances in neural
information processing systems, 33:6840–6851, 2020.
[42] H. Fan, H. Su, and L. J. Guibas. A point set generation network for 3d object reconstruction
from a single image. In Proceedings of the IEEE conference on computer vision and pattern
recognition, pages 605–613, 2017.
[43] G.-H. Xu, Y.-L. Wei, D. Zheng, X.-M. Wu, and W.-S. Zheng. Dexterous grasp transformer. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
17933–17942, 2024.
[44] T. Ren, S. Liu, A. Zeng, J. Lin, K. Li, H. Cao, J. Chen, X. Huang, Y. Chen, F. Yan, et al. Grounded
sam: Assembling open-world models for diverse visual tasks. arXiv preprint arXiv:2401.14159,
2024.
[45] Hyper3D. Hyper3d: Ai-powered 3d model generator, 2024. URL https://hyper3d.ai/.
[46] B. Wen, W. Yang, J. Kautz, and S. Birchfield. Foundationpose: Unified 6d pose estimation and
tracking of novel objects. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 17868–17879, 2024.
[47] A. L. Bishop, J. Z. Zhang, S. Gurumurthy, K. Tracy, and Z. Manchester. Relu-qp: A gpu-
accelerated quadratic programming solver for model-predictive control. In 2024 IEEE Interna-
tional Conference on Robotics and Automation (ICRA), pages 13285–13292. IEEE, 2024.
[48] B. Sundaralingam, S. K. S. Hari, A. Fishman, C. Garrett, K. Van Wyk, V. Blukis, A. Millane,
H. Oleynikova, A. Handa, F. Ramos, et al. curobo: Parallelized collision-free minimum-jerk
robot motion generation. arXiv preprint arXiv:2310.17274, 2023.
[49] K. Shaw, A. Agarwal, and D. Pathak. Leap hand: Low-cost, efficient, and anthropomorphic
hand for robot learning. arXiv preprint arXiv:2309.06440, 2023.
11


<!-- page 12 (ocr) -->
A
Preliminaries
Contact Model characterizes the resultant wrench exerted by a grasp on an object. Considering
an object O with m contact points, the local contact mechanics at each point i ∈{1, . . . , m} are
modeled as follows:
Fi = {fi ∈R3 | 0 ≤fi,1 ≤1,
f 2
i,2 + f 2
i,3 ≤µfi,1},
Gi =
ni
di
ei
pi × ni
pi × di
pi × ei
∈R6×3,
(6)
where pi ∈R3 denotes the contact position and ni ∈R3 represents the inward-pointing unit surface
normal. The vectors di, ei ∈R3 are orthogonal unit tangent vectors such that ni = di × ei, and µ is
the friction coefficient.
For each contact point, Fi represents the discretized friction cone and Gi is the grasp matrix. The
local contact force fi ∈Fi is mapped to a 6D wrench wi ∈R6 in the object’s coordinate frame via
wi = Gifi and the total wrench w generated by the grasp is the sum of the individual wrenches from
all m contact points, i.e., w =
m
i=1 wi.
Grasp Wrench Space (GWS), denoted as W, encompasses the set of all possible resultant wrenches
that can be exerted on the object. For each contact point i, we define the individual wrench space as
Wi = {Gifi | fi ∈Fi}. The aggregate GWS is then constructed via the Minkowski sum of these
per-contact wrench spaces W =
m
i=1 Wi.
QP-Energy is a differentiable metric designed to evaluate the capability of the current contact state
to resist external disturbances {tj}6
j=1 along six orthogonal axes, e.g., [±1, 0, 0, 0, 0, 0]⊤. For a fixed
contact system {Gi} and disturbances {tj}, the QP-Energy Q is calculated as:
Q ≜
6
j=1
min
fj,1,...,fj,m βtj −
m
i=1
Gifj,i
2
,
s.t.fj,i ∈Fi,
m
i=1
fi,1 ≥γ,
(7)
where β and γ are two positive hyperparameters.
B
Data Synthesis Details
B.1
Details of Bimanual Region-constraint Grasp Initialization
GWS-based Bimanual Grasping Region Selection As described in the main paper, we first sample
candidate regions on the object surface and generate local regions around them. These regions are
then filtered to form valid region pairs, which are subsequently evaluated using the GWB metric,
from which the top-performing pairs are selected. This section provides additional details on the
region filtering process.
To avoid physically infeasible or redundant grasps, region pairs that are too close are discarded. Given
two regions Ra and Rb, we compute the minimum inter-region distance
d(Ra, Rb) =
min
p∈Ra, q∈Rb∥p −q∥,
(8)
and retain the pair only if d(Ra, Rb) ≥τ2, where τ2 = 5 cm.
Region-based Grasp Initialization This section provides additional details on the initialization of
hand poses, including the computation of the initial rotation and the initialization of joint angles.
As described in the main paper, for each hand we first select the point on the object’s inflated closure
that is closest to the chosen region. The palm center is positioned to face this point, and the palm
12
Va
5
I
5
|
by


<!-- page 13 (ocr) -->
normal is aligned with the inward-facing normal of the closure at that location. Subsequently, the
hand base is rotated around the palm normal to the orientation that is closest to a predefined preferred
direction, which is chosen to be kinematically favorable for the robot arm. Specifically, the preferred
direction is set to (1, −1, −1) for the left hand and (1, 1, −1) for the right hand, corresponding to
forward–downward–right and forward–downward–left orientations, respectively.
For joint angle initialization, we adapt the finger configuration based on whether the associated
contact region is locally flat. Flatness is determined by the dispersion of surface normal directions
within the region. Given a set of surface normal vectors {ni}N
i=1 for a region, we first normalize them
and compute the resultant length
R =
1
N
N
i=1
ni
∥ni∥
.
(9)
Following directional statistics, we define the angular variance as
V = 2(1 −R).
(10)
A region is classified as flat if V < τ, where τ = 0.005 in all experiments. If the region is flat, the
fingers are initialized in a more open configuration; otherwise, they are initialized with a slightly
inward-curved posture.
B.2
Details of Decoupled Grasping Optimization
As stated in the main paper, the overall optimization process can be formulated as
min
Gbi (wQP Q(Gleft) + wQP Q(Gright) + wdisEdis + wregionEregion),
s.t.
Gbi
min ≤Gbi ≤Gbi
max,
ci,w = FK(Gbi, ci,l),
No collision.
(11)
And we define Edis to encourage the contact points on the hands to be close to the corresponding
points on the object surface:
Edis =
m
i=1
(||ci,w −pi||)2.
(12)
We further introduce a region consistency term Eregion to keep the contact points close to the contact
regions identified during initialization, thereby promoting coordinated bimanual grasping:
Eregion =
m
i=1
ϕ(di),
(13)
where the effective distance di from the i-th hand contact point to the contact region R is defined as
di =min
r∈R∥ci,w −r∥,
(14)
and ϕ(·) is a piecewise penalty function given by
ϕ(d) =









0,
d ≤a,
H
d −a
b −a
(d −a),
a < d ≤b,
d −a,
d > b,
(15)
with a denoting a distance threshold, b = 2a defining the transition bandwidth, and H(t) = 3t2 −2t3
being a cubic Hermite interpolation function.
This objective naturally leads to a bi-level optimization procedure. In the low-level optimization,
we fix the grasp parameters Gleft and Gright, and solve for the grasp quality terms Q(Gleft) and
Q(Gright). This step is implemented using ReLU-QP[47], a PyTorch-based ADMM solver, which
enables efficient and parallel computation of QP-based grasp energies across different objects.
In the upper-level optimization, the grasp parameters Gleft and Gright are optimized to minimize
the weighted sum of all energy terms while satisfying the kinematic and collision constraints.
13
Fe
(+)


<!-- page 14 (ocr) -->
0.12
0.16
0.01
0.00
0.15
0.12
0.25
0.11
0.20
0.21
0.10
0.46
0.10
0.13
0.54
0.07
0.25
0.14
0.00
0.06
0.00
0.04
0.00
0.00
0.19
0.01
0.02
0.46
0.00
0.02
0.02
0.00
𝑣1
𝑣2
𝑣3
𝒗𝟒
𝒗𝟓
𝑣6
𝑣7
𝑣8
𝒗𝟗𝒗𝟏𝟎𝑣11 𝒗𝟏𝟐𝒗𝟏𝟑𝑣14 𝑣15 𝑣16
𝒗𝟏𝟐
𝒗𝟏𝟑
𝒗𝟗
𝒗𝟒
𝒗𝟏𝟎
𝒗𝟓
(a) Distribution of grasp translation parameter
(b) Grasp anchors and their scores during inference 
Figure 6: Visualization of scale-adaptive grasp anchors. (a) Distribution of grasp translation parame-
ters represented in the world coordinate system (blue) and in the anchor coordinate system (orange),
respectively. Results show the proposed anchor-based formulation effectively reduces the action
space for a more compact grasp representation. (b) Grasp anchors and corresponding view scores
during inference, illustrating the conditional view selection process. The model first samples the
primary grasp view from the top candidate views, then samples the secondary grasp view via the
conditional bi-view distribution.
Specifically, we optimize the grasp parameters under joint limits, object contact constraints, and
collision-free conditions. To enforce these constraints, we directly adopt the energy functions
provided by cuRobo[48], including joint limitation energy, self-penetration energy, and inter-hand
penetration energy.
C
Framework Details
C.1
Model Details
C.1.1
Grasp View
We uniformly sample K grasp views on the upper hemisphere of a unit sphere and use these fixed
directions as candidate grasp views. Specifically, each grasp view is represented as a unit vector
vi ∈R3 pointing from the hemisphere surface to the object center.
C.1.2
Scale-Adaptive Grasp Anchor
Given a selected grasp view v, we construct a scale-adaptive grasp anchor ganchor
=
(tanchor, ranchor). The translation component tanchor is determined as the intersection point between
the grasp view direction and the object’s minimum bounding sphere, ensuring that the anchor location
adapts to the object scale.
The rotation component ranchor is defined by aligning the x-axis of the grasp frame with the direction
pointing toward the object center. The z-axis is computed as the projection of the world z-axis onto
the plane orthogonal to the x-axis, and the y-axis is obtained accordingly to form a right-handed
coordinate frame. This construction yields a unique and consistent grasp anchor frame for each grasp
view.
With the grasp anchor defined, a grasp pose (t, r) expressed in the world coordinate system can
be transformed into a relative representation (∆t, ∆r) with respect to the anchor frame. Fig. 6(a)
visualizes the distribution of grasp translation parameters represented in the world coordinate system
and the anchor coordinate system, respectively. The results show that the proposed anchor-based
formulation effectively reduces the action space, leading to a more compact and structured grasp
representation.
14
H
f
i"
H
[=
SE
{
NEG Og
it
i
i
fr 508
Sea i
i
i
Pe
=)
i
|
i
a
RT Gl des
foe
i
i
Po
eames
|
|
dE
|


<!-- page 15 (ocr) -->
C.1.3
Selection of Grasp View in Training and Inference Time
During training, we adopt a teacher-forcing strategy, where the ground-truth grasp views are directly
used to construct the scale-adaptive grasp anchors. This stabilizes training and allows the model to
focus on learning grasp generation conditioned on correct view information.
During inference, the model first predicts the single-view probabilistic {pi} ∈RK and the bi-view
probabilistic {pbi
i,j} ∈RK×K. We select the top-k views with the highest single-view probabilities
(with k = 5), apply temperature scaling with τ = 0.1, and perform softmax sampling to obtain the
primary grasp view index i. Conditioned on the selected primary view, we extract the corresponding
row {pbi
i,j} from the bi-view probabilistic and apply the same top-k sampling strategy to obtain the
second grasp view index j.
The overall sampling process is illustrated in Fig. 6(b). In the example, the model first samples
the primary grasp view from the top-scoring candidate views {5, 8, 10, 13, 15} and selects view 13.
Subsequently, the conditional bi-view distribution {pbi
13,j} is used to sample the second grasp view
from {4, 6, 9, 12, 15}, resulting in the selection of view 12.
C.2
Loss Function Details
We provide a detailed description of the loss functions used to train our framework. The overall
training objective is defined as:
L = λsingle-viewLsingle-view + λbi-viewLbi-view + λparaLpara
+ λchamferLchamfer + λphysicLphysic.
(16)
where the details are as following:
Single-view Loss.
We supervise the predicted primary grasping view scores using a masked
regression loss. Let pi denote the predicted score for view vi ∈V and yi the ground-truth signal. The
loss is defined as
Lsingle-view =
K
i=1 mi · SmoothL1(pi, yi)
K
i=1 mi + ϵ
,
(17)
where mi ∈{0, 1} is a validity mask indicating whether view i has supervision.
Bi-view Loss.
We supervise the predicted bi-view compatibility using a masked pairwise regression
loss. Let pbi
i,j denote the predicted compatibility score for view pair (vi, vj) and ybi
i,j the corresponding
ground-truth signal. The loss is defined as
Lbi-view =
K
i=1
K
j=1 mi · SmoothL1(pbi
i,j, ybi
i,j)
K
i=1 mi · K + ϵ
,
(18)
where mi ∈{0, 1} is the validity mask applied to each row.
Parameter Loss.
We supervise the predicted bimanual dexterous grasp poses by minimizing the
L2 distance between the predicted grasp parameters Gbi
pred and the ground-truth grasp parameters Gbi
gt:
Lpara =
Gbi
pred −Gbi
gt
2
2 .
(19)
Chamfer Loss.
We further impose a geometric consistency loss in 3D space. The predicted grasp
parameters Gbi
pred are converted into hand meshes via the dexterous hand model, from which surface
point clouds Ppred are sampled. Ground-truth point clouds Pgt are obtained in the same way from
Gbi
gt. The Chamfer loss is defined as
Lchamfer =
1
|Ppred| x∈Ppred
min
y∈Pgt ∥x −y∥2
2 +
1
|Pgt| y∈Pgt
min
x∈Ppred ∥y −x∥2
2.
(20)
15
=
>
Tz
z
I
I
—
—2


<!-- page 16 (ocr) -->
Physics-base Losses.
To ensure physical plausibility of the predicted grasps, we further introduce
Physics-base losses to improve physical feasibility. The physics-based losses are:
Lphysic = λself-penLself-pen + λobj-penLobj-pen + λspfLspf
(21)
Self-bi-penetration Loss.
We penalize self-collisions of inter-hands and intra-hands. Let K =
{ki}N
i=1 denote a set of predefined hand keypoints used for penetration avoidance (including both
hands). We compute all pairwise distances and apply a soft penalty when the distance is smaller than
a safety threshold δ:
Lself−pen =
i̸=j
max 0, δ −∥ki −kj∥2 .
(22)
This term discourages physically infeasible interpenetration between fingers and hands.
Hand–Object Penetration Loss.
To prevent the hand from penetrating into the object, we compute
the signed distance si from each hand surface keypoint pi to the object surface, where si > 0
indicates the point lies inside the object. The loss is defined as
Lobj−pen =
i
max(0, si).
(23)
Contact Loss.
To encourage hand–object contact, we pull predefined hand contact candidate points
C = {ci} toward the object surface point cloud O. For each point, we compute the nearest-neighbor
distance
di = min
o∈O ∥ci −o∥2.
(24)
Only points within a threshold τ are considered, and the loss is
Lspf = 1
|I| i∈I
di,
I = {i | di < τ}.
(25)
The weighting coefficients of the loss terms are set as follows: λsingle-view = 10.0, λbi-view = 1.0,
λpara = 15.0, λchamfer = 0.25, λphysic = 1.0, λobj-pen = 100.0, λself-pen = 50.0, and λspf = 50.0.
D
Evaluation Metric Details
Grasp Success Rate (SUC). The hand executes a grasp from the pre-grasp pose Gbi
pre to the squeeze
pose Gbi
squ. A grasp is considered successful if the object’s translation and rotation remain within 5 cm
and 15° for at least 3 seconds after execution. SUC-F evaluates force-closure success under external
disturbances along six orthogonal directions. SUC-L evaluates lift success in a tabletop scenario with
a floating hand. SUC-A evaluates lift success in a tabletop scenario with an arm-controlled hand.
Speed (S) and Success Generation Speed (SGS). These measure the number of raw grasps and
successful grasps synthesized per second, respectively. All numbers are obtained on a single NVIDIA
GeForce RTX 3090 GPU, while baseline speeds are cited from their original reports.
Penetration Depth (PD). The maximum intersection distance between the object mesh and the hand
mesh.
Self-Penetration Depth (SPD). The maximum penetration distance among all hand collision meshes,
including both intra-hand and inter-hand self-penetrations.
Contact Distance Consistency (CDC). The range between the maximum and minimum signed
contact distances across all fingers, reflecting the uniformity of finger-object contacts.
Diversity (D). The explained variance ratio of the first principal component from PCA applied to
the generated grasp distribution, quantifying the concentration (and inversely, diversity) of bimanual
grasps.
16
bh
>
—2


<!-- page 17 (ocr) -->
E
Experiments of Data Synthesis
E.1
Qualitative Experiments of Region Selection
To validate the effectiveness of our region filtering strategy, we compare our method with random ini-
tialization. We randomly select 2,000 objects from DexGraspNet[10] and Objaverse[37], respectively.
For each object, five region pairs are generated using our region generation method and random
sampling, and five contact points are sampled within each region to compute the Q1 metric, which
measures the distance between the Grasp Wrench Space (GWS) formed by the contact points and
the origin, where a larger value indicates a more stable grasp. As shown in Table 7, our method
consistently achieves higher Q1 values than random sampling on both datasets, demonstrating that the
proposed region filtering strategy is more likely to produce stable grasp configurations and generalizes
well across both structured and diverse object geometries.
Method
ours(DGN)
random(DGN)
ours(Objaverse)
random(Objaverse)
Q1(×10−2)
1.25
0.47
1.41
0.79
Table 6: The region quality comparison between our method and random sample. The results
demonstrate that our initialization strategy can initialize grasp region candidates with significantly
higher quality.
Figure 7: Visualization of extending our pipeline to cluttered scenes.
E.2
Extension to Cluttered Scenes
Our pipeline can be readily extended to cluttered environments (Fig. 7). By incorporating additional
collision constraints, the method is able to optimize collision-free grasps in complex, cluttered
scenarios.
E.3
More Visualization of Diverse Grasping on Data Generation
E.3.1
Visualization of other Dexterous Hands
Our data synthesis pipeline is not limited to a specific hand model and can be naturally extended
to other dexterous hands. Fig. 8 visualizes grasp samples generated by applying our pipeline to the
Leap Hand [49], demonstrating the generality of the proposed method across different dexterous
hand embodiments.
Figure 8: The visualization of the reslut of our data synthesis on LeapHand. Our data synthesis
pipeline can be used for different dexterous hands.
17


<!-- page 18 (ocr) -->
E.3.2
Visualization of Grasps in our Dataset
We present a visualization of the grasps contained in our dataset in 9. These examples demonstrate
that our dataset covers a wide range of object sizes and exhibits significant grasp diversity when
objects are placed in identical poses on the tabletop.
Figure 9: Visualization of the dataset diversity. The samples span multiple object scales and
demonstrate diverse grasping poses even under identical object placements.
F
Experiments of Framework
F.1
Reproduction of SOTA method
DGTR[43] We utilize the original three independent MLP heads—responsible for predicting transla-
tion, rotation, and joint angles—by expanding their output dimensions to generate bimanual poses.
The total loss is defined as the summation of the individual losses for both hands, with calculation
metrics consistent with the original paper. Furthermore, we strictly adhere to the official three-stage
training strategy.
SceneDiffuser[17] We doubled the input and output dimensions of the SceneDiffuser model to
represent both left- and right-hand grasping, while continuing to use the previous loss function.
F.2
Efficiency Analysis of Framework
To further evaluate our model, we conduct ablation studies on inference time. We measure the
inference time of a single batch with batch size 64 and compare our method against the DDPM-
Baseline (removes the BCM, GAF and SAGA component). To reduce measurement variance, we run
each experiment for five epochs and report the mean and standard deviation. As shown in Table 7,
and the results indicate that our method significantly improves the success rate at the cost of only a
modest increase in inference time.
F.3
Further Ablation of the Bimanual Coordination Module
We further conduct an ablation study on the bimanual coordination module to analyze the view
sampling strategy. In our full model, the coordinated grasp views are sampled in a conditional manner.
Specifically, we first sample the primary grasping view from the predicted single-view probabilistic
18
AREAS
2
42h
NAYS 444-4
IE ATRCALE.
VOePEe TWOP
PPVEDP NNN §


<!-- page 19 (ocr) -->
Method
Average Inference Time (s)
Success Rate-Lift(%)
Baseline
1.21 ± 0.03
41.17
Ours
1.67 ± 0.05
61.93
Table 7: Inference time comparison per batch. Our method achieves a good balance between model
performance and efficiency.
pi. Given the sampled primary view, we then select the corresponding row from the predicted bi-view
probabilistic pbi
i,j and sample the second view conditioned on the primary one.
For ablation, we remove this conditional sampling procedure and instead directly sample a single
entry from the bi-view probabilistic pbi
i,j. In this case, the sampled index jointly determines the
primary and second grasping views without conditioning. Although this strategy treats the two hands
in a fully symmetric manner, the results in Table 8 show a clear performance degradation across most
metrics. This is because the conditional sampling in our design decomposes view selection into two
sequential decisions, which is significantly easier than directly selecting a view pair from the full
bi-view distribution, leading to more reliable bimanual coordination.
Method
Metrics
SUC-L↑
PD↓
SPD↓
CDC↓
Direct Bi-view Sampling
45.49
2.23
0.01
2.96
Ours
61.93
1.73
0.02
2.56
Table 8: Further Ablation of the Bimanual Coordination Module. This module can significantly
improve the framework performance.
F.4
Failure Case Analysis
As illustrated in Fig. 10 , failure cases primarily manifest as physical instability. Minor object
penetration or floating grasps may occur when the generative model fails to perfectly balance the
penetration penalty and contact supervision. Furthermore, as demonstrated in the rightmost case, a
small number of objects undergo lateral sliding due to insufficient force closure, resulting in grasp
failure.
Figure 10: The visualization of failure cases. We find that the common failure cases are caused by
object-hand penetration and non-contact.
F.5
More Visulization of Generated Poses
In Fig. 11, we provide additional visualizations of the generated bimanual grasps on various objects.
As observed, our framework consistently produces physically plausible and stable grasps, effectively
adapting to objects with diverse geometric shapes and sizes. Furthermore, the model is capable
of generating a rich variety of grasping postures for the same object, and the visualized results
demonstrate distinct bimanual coordination.
19


<!-- page 20 (ocr) -->
Figure 11: The visualization of dexterous grasping generated by our model.
G
Real world Experiments
G.1
Real world Experiments Details
In this subsection, we describe the real-world experimental pipeline.For the single-view point cloud
setting, we apply Grounded-SAM [44] to segment the object, and use the resulting mask to crop the
object point cloud from the RGB-D frame as input to the model. For full points cloud setting, we
first reconstruct the target object using a single-view 3D reconstruction method [45] and align the
observed point cloud with the reconstructed mesh by matching their 3D bounding boxes to obtain the
object scale. Next, we estimate the object 6D pose using 6D pose estimation [46] and we obtain the
object point cloud input to our model by uniformly sampling points from the surface of the scaled
mesh after world-frame pose transformation.
We then convert the predicted Shadow Hand joint poses into the specific dexterous hand joint
configuration via a hand-object consistent retargeting [6]. We define the pre-grasp pose by offsetting
the final grasp pose along the hand’s negative approach direction (moving backward from the grasp
along the hand-back/approach axis) by a fixed distance.
During execution, as shown in Figure 12, the robot arm and hand first move from a predefined
safe configuration to the pre-grasp pose. The system then commands the arm–hand to move from
pre-grasp to the final grasp pose, and then to lift pose to complete the grasp.
20
Cedpev oY
Peete tid éd
4880000000


<!-- page 21 (ocr) -->
Initial State
Safe State
Pre-Grasp Pose
Grasp Pose
Lift Pose
Figure 12: The visualization of real world execution. During execution, the robot arm and hand first
move from a predefined safe configuration to the pre-grasp pose. The system then commands the
arm–hand to move from pre-grasp to the final grasp pose, and then to lift pose to complete the grasp.
21
00]
7
>
ta
fos
Ia
1]
RE 5
-
=
Ee)
Is
._]
oe
[ee
5
\
-
- RB
\ /
a
Re)
Es
\
¢
R, 4
KF—¥
%
~
|
Ts
Toa
\
i
2
oe
