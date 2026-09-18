# **Geometric Retargeting: A Principled, Ultrafast Neural Hand Retargeting Algorithm** 

Zhao-Heng Yin<sup>1</sup><sup>_,_2</sup> , Changhao Wang<sup>2</sup> , Luis Pineda<sup>2</sup> , Krishna Bodduluri<sup>2</sup> , Tingfan Wu<sup>2</sup> , Pieter Abbeel<sup>1</sup> , Mustafa Mukadam<sup>2</sup> 

**_Abstract_ — We introduce Geometric Retargeting (GeoRT), an ultrafast, and principled neural hand retargeting algorithm for teleoperation, developed as part of our recent Dexterity Gen (DexGen) system [1]. GeoRT converts human finger keypoints to robot hand keypoints at 1KHz, achieving state-of-the-art speed and accuracy with significantly fewer hyperparameters. This high-speed capability enables flexible postprocessing, such as leveraging a foundational controller for action correction like DexGen. GeoRT is trained in an unsupervised manner, eliminating the need for manual annotation of hand pairs. The core of GeoRT lies in novel geometric objective functions that capture the essence of retargeting: preserving motion fidelity, ensuring configuration space (C-space) coverage, maintaining uniform response through high flatness, pinch correspondence and preventing self-collisions. This approach is free from intensive test-time optimization, offering a more scalable and practical solution for real-time hand retargeting.** 

## I. INTRODUCTION 

Teleoperation is essential for collecting robotic manipulation data, as it allows humans to remotely control robots in real-time. In dexterous manipulation, a fundamental component of teleoperation is kinematic retargeting [2], [3], [4], [5], [6]. It involves translating human gestures into corresponding robot hand poses, enabling intuitive control of robotic systems. However, defining an effective kinematic retargeting function remains a longstanding challenge. The complexity arises from the need to account for variations in human and robot configurations, and the desired level of precision. Despite the progress in this area, no universal methods have been developed that reliably captures human intent while maintaining natural and efficient robot motion. 

One of the main challenges is determining the criteria for effective kinematic retargeting. Although there are numerous possible mappings from a human hand to a robot hand, the simplest and most effective criteria (objective function) for specifying and training desirable retargeting functions remain unclear. Existing methods [2], [3], [7], [8] typically rely on a complex set of task vector constraints that ensures the retargeted robot hand pose visually looks similar to the original human hand pose. Most recent teleoperation works [8] typically take the following linear matching form in their pipeline: 



*This work was partially done during Z.H. Yin’s intern at Meta. 

> *Project website: zhaohengyin.github.io/geort 

> *For application in DexterityGen: zhaohengyin.github.io/dexteritygen 

> 1BAIR, UC Berkeley EECS. 

> 2FAIR at Meta. 



<!-- Start of picture text -->
f<br>Source C-space Target C-space<br><!-- End of picture text -->

Fig. 1: Retargeting is an unconstrained problem. There are many valid retargeting functions (e.g. by dragging the point anchors in the figure). However, it is unclear how to define a proper cost functional (objective) to specify desired retargeting function. 

TABLE I: Comparison of technical specifications of existing approaches. The speed is claimed by the referred paper or its follow up work. 

|Method|DexPilot [2]|AnyTeleop [3]|RTelekinesis|[8]<br>Ours|
|---|---|---|---|---|
|Hyperparams|_≥_10|_≥_10|_≥_10|_≤_5|
|No Task Vector|_×_|_×_|_×_|✓|
|No Online Opt.|_×_|_×_|✓|✓|
|Retargeting Speed|60-100Hz|60-100Hz|1000Hz|1000Hz|



Here **v**<sup>_i_</sup> _H_<sup>and</sup><sup>**v**</sup><sup>_i_</sup> _R_<sup>=</sup><sup>_f_(</sup><sup>**v**</sup><sup>_i_</sup> _H_<sup>)arethetaskvectorsof(source)</sup> human and (retargeted) robot hands, _αi_ are some scaling hyperparameter, and _N ≈_ 10 is the number of hand keypoints. The second regularization term is usually used to ensure smoothness. This formulation has several drawbacks. First, it requires several hyperparameters (e.g. _αi_ , task vector origin _oi_ ) to recenter and rescale each human keypoint (or task vectors), which are difficult to specify and vary between individuals. It requires a tedious process to calibrate these task-vector-related hyperparameters. Second, we notice that this linear matching objective may also be suboptimal. To illustrate this, we use Allegro Hand as an example to compare the shape of human and robot fingertip keypoint space, as shown in Figure 2. We observe that the human fingertip keypoint _C_ -space (moving range) typically has a more curved and narrower shape, while that of the robot hand is more regular and wider. Consequently, the linear matching objective can fail to capture the correspondence and we need a more principled way to define the retargeting objective. 

In this paper, we propose Geometric Retargeting (GeoRT), a principled retargeting objective and training pipeline. Since 



<!-- Start of picture text -->
Z<br>Y<br><!-- End of picture text -->

Fig. 2: Nonlinear Nature of Retargeting: In this figure, we compare shapes of human and robot (Allegro) fingertip keypoint _C_ -space (i.e. the moving range of fingertip in the hand frame). The top row shows the ring finger keypoint space comparisons and the bottom row shows the thumb keypoint space comparisons. We find that the robot and human hands keypoint spaces are not directly related through a linear mapping as suggested by previous works. In this paper, we propose novel objectives to overcome this limitation. In this figure, the robot finger keypoints are produced by random sampling in joint space and then computing forward kinematics. The human finger keypoints are produced by motion capture of a 5-minute play, in which the human is asked to move their fingers randomly to explore the limit of their hand joints. 



Fig. 3: The proposed principled and ultrafast teleoperation algorithm enables large-scale foundation controllers, unlocking the potential for more dexterous teleoperation systems like DexterityGen [1]. 

the ultimate goal of retargeting is to give the human operator a sense of intuitive control over the robot hand, we define the ideal retargeting through a set of straightforward geometric criteria that characterize such requirements. We suggest that the retargeting model should (1) preserve human motion locally and preserve pinch grasps, (2) maximize _C_ -space 

coverage so that the robot hand is fully utilized, and it should be (3) flat for uniform control sensitivity , (4) preserve pinch correspondence, and (5) collision-free. These objectives are simple to implement while providing a principled specification of retargeting quality. We also show that these principles are independent and they form minimal constraints for defining retargeting. We compare the technical specifications of our method to existing approaches in Table I. Our method has fewer hyperparameters and does not use heuristic task vectors, while still achieving state-of-the-art inference speed. In the experiments, we show that our algorithm has much better hand utilization and achieves better smoothness. It also outperforms existing methods in the teleoperation-based grasping task in real world experiments. 

In summary, this paper makes the following contributions: (1) We propose principled retargeting objectives for learning neural retargeting models. (2) We develop a fast neural retargeting system based on these objectives, which outperforms existing approaches in both retargeting quality and teleoperation performance and supports further applications such as DexterityGen [1]. 

II. GEOMETRIC RETARGETING 

## _A. Preliminaries_ 

We make the following commonly used assumption as previous works. **A1** . First, we assume that the robot hand 



<!-- Start of picture text -->
Human Fingertip  C -Space Robot Fingertip  C -Space<br>(Cartesian) (Cartesian)<br>Retarget<br><!-- End of picture text -->

Motion Preservation 



Maximize Space Coverage (Surjection) 

Fig. 4: Basic idea of our geometric objective functions (criterion I and II). (Left) A good retargeting function should preserve the moving direction of the fingertip. (Right) Besides, the retargeting function should also be a surjection, so that the robot fingertip C-space is fully utilized. Note that we only show the _C_ -space for one fingertip (e.g. index finger) in the figure. 

is anthropomorphic so that a natural and intuitive retargeting function may exist. **A2** . We further assume the existence of finger correspondence: e.g. humans use their index fingertip to control the robot’s “index” fingertip. We denote the humans’ and robot’s fingertip position in their own wrist frame as _xH_<sup>_i_and</sup><sup>_x_</sup> _R_<sup>_i_respectively,where</sup><sup>_i_isthefingertip</sup> index. 

In this paper, a kinematic retargeting model _f_ is a function that maps a set of human fingertip keypoints to robot hand joint positions, which is different from works that also take the object model and poses as input for joint hand-object retargeting. 

## _B. Criterion I: Motion Preservation_ 

We require the retargeting function to preserve the movement direction of each fingertip. This aligns with a fundamental expectation in teleoperation: when a human operator moves their finger in a certain direction, they naturally expect the robot’s fingertip to follow the same trajectory. Formally, given any position _xH_<sup>_i_for</sup><sup>_i_-thfingerandanysmallmoving</sup> direction _d_ , we require _d_ parallel to FK _i ◦ fi_ ( _xH_<sup>_i_+</sup><sup>_d_)</sup><sup>_−_FK</sup><sup>_i ◦_</sup> _fi_ ( _xH_<sup>_i_),whereFK</sup><sup>_i_istheforwardkinematicsforfingertip</sup> _i_ , and _fi_ is the retargeting component for _i_ -th finger. This criterion can be described by a simple loss function: 



We implement FK _i_ as a pretrained neural forward kinematics function. One can also use an analytical forward kinematics function. 

## _C. Criterion II: C-space Coverage_ 

Besides motion preservation, another important criterion is _C_ -space coverage. Intuitively, we want the robot’s _C_ -space to be fully utilized—when a human moves their fingers from 



<!-- Start of picture text -->
Y Y<br>X X<br>Low Flatness Mappings High Flatness Mapping<br><!-- End of picture text -->

Fig. 5: The retargeting mapping should have a high flatness (criterion III). In this 1D retargeting example (mapping an interval on the _x_ -axis to another interval on the _y_ -axis), this is equivalent to _f_<sup>_′_</sup> ( _x_ ) being constant everywhere, so that any small ∆ _x_ will lead to the same amount of ∆ _y_ . Note that the blue curves on the left can satisfy the criterion I and II. Therefore, introducing a third flatness objective is necessary. 

one limit to the other, the robot hand should replicate this motion across its full range, rather than being confined to a limited subset of its _C−_ space. 

Formally, we denote the keypoint _C−_ space of _i_ -th robot and human fingertip as _KCR_<sup>_i_and</sup><sup>_KC_</sup> _H_<sup>_i_respectively. Then, our</sup> coverage criteria states that FK _i ◦ fi_ should be a surjection from _KCH_<sup>_i_to</sup><sup>_KC_</sup> _R_<sup>_i_,andweshouldminimizethevolume</sup> of _KCR_<sup>_i\_(FK</sup><sup>_i ◦fi_(</sup><sup>_KC_</sup> _H_<sup>_i_)),i.e.theuncovered</sup><sup>_i_-thfingertip</sup> keypoint _C_ -space of robot hand. However, computing this uncovered space and its volume is computationally expensive, and this does not yield a differentiable function either. Therefore, we propose to use Chamfer loss [9] in 3D vision research as a proxy for this procedure. In each minibatch, we sample _PH_<sup>_i∼KC_</sup> _H_<sup>_i_and</sup> _PR_<sup>_i∼KC_</sup> _R_<sup>_i_uniformly,andweminimize</sup> 



This loss guarantees that any random point cloud representation of _KCR_<sup>_i_can beclosely approximatedby projectingthe</sup> 



<!-- Start of picture text -->
Human  (I-IV)<br>Fingertip Retargeting Network RobotJoint KinematicsForward Loss<br>Position<br>(V)<br>Collision<br>Loss<br>gradient Classifier<br><!-- End of picture text -->

Fig. 6: Model training update procedure. The geometrical loss functions (I-IV) are computed in the keypoint spaces (after the differentiable forward kinematics). The gradient backpropagates through the forward kinematics model and the collision classifier to the retargeting network. Note that the forward kinematics model and collision classifier are only used during training. 

corresponding representation of _KCH_<sup>_i_with retargeting model.</sup> 

## _D. Criterion III: High Flatness_ 

While the last two criteria already define a reasonable retargeting mapping, we find it necessary to introduce a flatness objective to ensure that the model responds uniformly as the user moves across the _C_ -space, which enhances the predictability and intuitiveness of the interaction experience. To understand this, we illustrate an 1D example in Figure 5. The retargeting functions defined by the blue curves satisfy the criterion I and II simultaneously, however, the same ∆ _x_ in the source _X_ space may lead to different ∆ _y_ in the target _Y_ space. In this case, the user may perceive the retargeting as too unresponsive (i.e. _f_<sup>_′_</sup> ( _x_ ) _≈_ 0) in some areas, while overly sensitive (i.e. _| f_<sup>_′_</sup> ( _x_ ) _|_ too large) in others. The ideal retargeting should have high flatness, which means _f_<sup>_′_</sup> ( _x_ ) being almost constant, or a low _f_<sup>_′′_</sup> ( _x_ ) =<sup>_d_</sup> _dx_<sup>22</sup><sup>_<u>f</u>_(</sup><sup>_x_)</sup><sup>_≈_0</sup> equivalently. To generalize this idea to high dimensional 2 space, we propose to minimize E _xH ,d_ ��� _d_ 2( _dt_ FK<sup>2</sup> _◦_ _<u>f</u>_ <u>)</u> ( _xH_ + _td_ )��� , which means the second-order directional derivative at any point along any direction should be close to 0. We use the finite difference method to evaluate the derivatives, yielding the following objective function: 





The global linear matching objective (i.e. Equation 1) used by previous works naturally encourages flatness. However, for general non-linear retargeting problems, perhaps the best way is to use the proposed local flatness constraint. 

Note that criteria II and III can not derive criterion I (motion preservation). In the example, reversing the linear mapping (change the slope to its opposite and shift) on the right can still make criteria II and III hold, but the moving direction in the target space will be reverted and very unintuitive. 

## _E. Criterion IV: Pinch Correspondence_ 

The previous criterion focused more on per-finger motion regulation. Another important expectation from users is pinch 

## **Algorithm 1** Geometric Retargeting 

- 1: Generate (joint position _q_ , fingertip position _x_ , collision _c_ ) data in simulation to train each neural forward kinematics models FK _i_ and collision classifier _C_ . 

- _i i_ 

- 2: Generate point cloud approximation _KC_<sup>�</sup> _R_<sup>_,_�</sup> _KCH_<sup>ofeach</sup> keypoint _C_ -space _KCR_<sup>_i,KC_</sup> _H_<sup>_i_.</sup> 

- 3: **for** itr = 0 _,_ 1 _,..., Ntrain_ **do** 

- 4: Sample **d** _∼ N_ (0 _, σ_<sup>2</sup> ) and random human gesture **x** _H_ to compute _Ldir, L flat , Lpinch, Lcol_ ; 

- _i i_ 

- 5: Sample **P**<sup>_i_</sup> _H_<sup>_∼_</sup> _KC_<sup>�</sup> _H_<sup>,</sup><sup>**P**</sup><sup>_i_</sup> _R_<sup>_∼_</sup> _KC_<sup>�</sup> _R_<sup>tocompute</sup><sup>_Lcover_;</sup> 6: Optimize _f_ by taking gradient descent with _L_ = _Ldir_ + _λ_ 1 _Lcover_ + _λ_ 2 _L flat_ + _λ_ 3 _Lpinch_ + _λ_ 4 _Lcol_ . 

- 7: **end for** 

- 8: **return** _f_ 

correspondence. For example, when the users do a pinch grasp using the thumb and index finger, they typically expect that the robot hand does the same. We find this crucial to provide users with a sense of agency, however, previous criteria do not strictly guarantee this and sometimes we notice that the emerged pinch correspondence is not perfect. To improve this, we further introduce a pinch correspondence constraint. Specifically, for a human gesture _xH_ , if _xH_<sup>_i−x_</sup> _H_<sup>_j_</sup> is below a threshold _d_ (such as 1cm), i.e., finger _i_ and _j_ are pinching, then we require FK _i ◦ fi_ ( _xH_<sup>_i_) close to FK</sup><sup>_j ◦f j_(</sup><sup>_x_</sup> _H_<sup>_j_).</sup> This can be written as 



Note that this requires human users to provide some pinch grasp examples. Fortunately, this can be easily collected within 5 minutes of random play as we will discuss in the implementation section. 

## _F. Criterion V: Collision-Free Retargeting_ 

Finally, a collision-free human hand gesture should correspond to a collision-free robot hand gesture. Therefore, we introduce collision-free as our final criterion. Similar to [8], we first pretrain a collision classifier _C_ to decide the probability of a joint configuration _q_ leading to hand self-collision. The training dataset is generated through simulation, and the label is obtained by querying a collision checker to get the binary self-collision label. Then, we use the following collision loss over retargeting model _f_ : 



Note that _C_ is fixed as we train _f_ . Interestingly, we find that even without this term our loss can lead to few collisions for certain robot hands. Nevertheless, we introduce this for completeness. 











<!-- Start of picture text -->
Baseline (Equation 1) Ours<br><!-- End of picture text -->

Fig. 7: Qualitative comparisons. We find that due to insufficient _C_ -space coverage, the baseline method fails to provide important functionalities such as index-ring finger pinch, which is essential for in-hand manipulation. 

## _G. Implementation_ 

We implement our kinematic retargeting model as a set of independent retargeting models. For example, for the Allegro Hand which has four fingers, we define _f_ ( _xH_<sup>1</sup><sup>_,x_</sup> _H_<sup>2</sup><sup>_,x_</sup> _H_<sup>3</sup><sup>_,x_</sup> _H_<sup>4) =</sup> [ _f_ 1( _xH_<sup>1)</sup><sup>_, f_2(</sup><sup>_x_</sup> _H_<sup>2)</sup><sup>_, f_3(</sup><sup>_x_</sup> _H_<sup>3)</sup><sup>_, f_4(</sup><sup>_x_</sup> _H_<sup>4)],andeach</sup><sup>_fi_isanindepen-</sup> dent retargeting model for the corresponding finger. We parameterize each _fi_ as a multi-layer perception (MLP). We also rescale the joint position range to [ _−_ 1 _,_ 1] and use Tanh as output activation of each _fi_ . We use a combination of the proposed loss functions to train our model: 



This optimization objective only has 4 hyperparameters compared to previous works that have numerous scale hyperparameters and heuristic task vectors. We present our training loop in Algorithm 1 for clarity. The training procedure is very fast in practice, only taking 3-5 minutes on a single NVIDIA 3060 GPU. The point cloud approximation of the robot hand fingertip keypoint _C_ -space can be generated by randomly moving the hand in simulation. For that of human hand, we find the following method effective: we ask the human user to stretch their fingers and move back and forth, as well as perform various pinch grasps under any motion capture system (or other hand tracking system such as a glove). We record the moving trajectory of each fingertip keypoint, giving us several raw point clouds. This data collection process is fast and typically takes less than 5 minutes and is a one-time calibration. We find that an empirical loss weight setup that works well is _λ_ 1 _∈_ [10 _,_ 100] _, λ_ 2 = 1 _, λ_ 3 _∈_ [10<sup>3</sup> _,_ 10<sup>6</sup> ] _, λ_ 4 = [10<sup>_−_4</sup> _,_ 10<sup>_−_2</sup> ]. Varying the weight inside these intervals can change the retargeting details a bit, but overall they look similar and provide good results. Note that the magnitudes of some weights are large due to the distance unit we use. 

TABLE II: Quality metric of different loss objectives. Note that the online version of Eqn (1) is not time-independent and its result relies on the previous frame, so we use its offline version as an approximation. 

|**Method**||**Equation 1**|**Ours**|
|---|---|---|---|
||Offline|[8]<br>Online [2], [3]||
|Motion Preservation(_↑_)|0.73|–|**0.94**|
|_C_-space coverage(_↑_)|38%|–|**90%**|



TABLE III: Teleoperation performance comparison of different methods in real world. Our method offers a faster and more effective teleoperation experience. 

|**Method**|**Eq**|**uation 1**|**Ours**|
|---|---|---|---|
||Offline [8]|Online [2], [3]||
|Onetime-Success(_↑_)|55%|42.5%|**87.5%**|
|Completion Time(_↓_|)<br>9.0s|19.3s|**3.2s**|



## III. EXPERIMENTS 

In this section, we compare the grasping performance of this work to other teleoperation methods. We also study the properties and design choices of our neural retargeting method. For its application, we refer readers to the DexterityGen paper. 

## _A. Simulation Evaluation_ 

We first compare the quality of different methods in simulation. We quantitatively measure the smoothness score and the _C_ -space coverage score. The definitions of these two metrics are as follows: 

- 1) **Motion Preservation** is related to Criteria I. We compute this by uniformly sample anchor points _xH_<sup>_i_and</sup> directions _d_ , and we compute _N_<sup><u>1</u>∑</sup><sup>_N_</sup> _i_ =1<sup>E</sup> _d,xH_<sup>_i_Dir(</sup><sup>_x_</sup> _H_<sup>_i,d_),</sup> i.e. how good the robot hand movement is aligned with human hand movement. The metric is bounded by [ _−_ 1 _,_ 1]. 

- 2) _C_ **-space Coverage** is related to Criteria II, quantifying the effective moving range of the fingertip. However, we do not exactly compute this following the proposed objective function. We sample sufficiently many points _xH_<sup>_i_ineachhumanfingertipkeypoint</sup> _C_ -space and we compute how much they occupy the robot keypoint _C_ -space, given by Vol( _∪iB_ (FK _◦ f_ ( _xH_<sup>_i_)</sup><sup>_,r_)</sup><sup>_∩KP_</sup> _R_<sup>_i_)</sup><sup>_/_Vol(</sup><sup>_KP_</sup> _R_<sup>_i_).Here,</sup><sup>_B_(</sup><sup>_x,r_)denotesa</sup> sphere or radius _r_ centered at _x_ . This metric is between [0% _,_ 100%]. 

**Results** We list the evaluation results of different methods on Allegro Hand in Table II. We find that our approach can achieve much better smoothness and _C_ -space coverage compared to baseline methods. However, this result is expected since we directly use these two metrics for optimization. This suggests that our approach can fully utilize the moving range of the robot hand while providing 



<!-- Start of picture text -->
4s<br><!-- End of picture text -->





<!-- Start of picture text -->
105s<br><!-- End of picture text -->



Fig. 8: The user can use our system to clean up a pile of objects (12) on the table in around 100 seconds easily. Note that the relatively slow arm motion is the main bottleneck here. The user can grasp most of the objects successfully with 1 trial. 





Fig. 9: Qualitative retargeting results of our retargeting method. The top half is the Allegro hand and the bottom half is the Leap hand. Even if our method does not use any task-vector-based matching terms, it can discover the correspondence between human and robot hands. 

the user with a smooth sense of control. 

**Qualitative Results** Furthermore, we investigate whether our quantitative results translate to plausible retargeting. We plot some retargeting results in Figure 7. Surprisingly, even if we do not use any task vector matching heuristics, a good correspondence emerges from our simple objective function on different hands (Allegro and LEAP [10] hand). We also 

compare our method to the baseline in Figure 2. We find that due to insufficient coverage, the baseline method fails to utilize the lateral movement of fingers effectively and cannot do effective pinch grasp or finger (thumb) reaching. 

_B. Real-world Experimental Setup_ 

Then, we evaluate our approach on an arm-hand robotic system. In this paper, we use the Allegro robot hand with the Franka Panda robot arm. For the teleoperation of Allegro 

hand, we first use a Manus glove to capture the human hand keypoints. These keypoints are then fed into the retargeting model to produce the allegro hand joint target. These joint target are then sent to a PD controller to drive the hand. For the arm teleoperation, we use a Vive tracker system to capture the human wrist pose and use it to control the motion of robot arm’s end-effector pose. 

## _C. Real-world Evaluation_ 

Since performing dexterous in-hand manipulation is hard as suggested by previous works, in this paper we mainly consider the grasping performance, which is also a crucial step in robotic manipulation. We record the one-trial success rate and the average time a user takes to grasp an object successfully. 

**Results** We show the result in Table III. We find that our method can allow for faster and more effective grasping in real world. We account for this by better utilization of fingertip _C_ -space and smoother and more intuitive retargeting. Specifically, we find that it is hard to grasp tiny objects with the baseline method due to the unintuitive finegrained control of fingertip. 

shapes (e.g. human to human correspondence) [16], [17], [18]. However, so far this line of research has not been applied to retargeting systematically yet. A recent retargeting work [19], harmonic autoencoder, also leveraged ideas in this field (e.g. using chamfer loss) to improve mapping quality. However, it also uses pairwise human-to-robot data in training. In contrast, we propose using motion and flatness losses as supervision, which makes our method fully unsupervised. 

## V. CONCLUSION 

In this paper, we have presented Geometric Retargeting (GeoRT) a fast, efficient, and principled approach to neural hand retargeting for teleoperation, integrated into the Dexterity Gen (DexGen) system. GeoRT achieves state-ofthe-art speed with minimal hyperparameters compared to existing methods. Its unsupervised training eliminates the need for manual hand pair annotations, while its novel geometric objective functions ensure both motion fidelity and C-space coverage. GeoRT’s high-speed performance and scalability make it a practical and flexible solution for realtime hand retargeting without the need for intensive test-time optimization. 

## IV. RELATED WORKS 

## ACKNOWLEDGMENTS 

**Retargeting** Retargeting is an important step in teleoperation. Some works propose to use joint-space retargeting [11], [12], which maps the joint of the human hand to that of the robot hand through some predefined mapping. Although this approach is intuitive in some cases, it fails to provide precise control in general due to differences in kinematic structure between the robot hand and the human hand. Some works also propose direct cartesian mapping [2] from human hand keypoint to robot hand keypoint and use an inverse kinematics model to decide the hand joints. Most of the recent works in robot hand teleoperation apply this cartesian keypoint mapping approach. However, specifying keypoint mapping is nontrivial as we discussed and they can lead to unnatural hand poses. Instead of using some heuristic cartesian mapping rule (e.g. linear rule), in this paper we propose novel objectives based on local motion and global _C_ - space matching, avoiding the challenge of designing complex heuristics. In the retargeting literature, some works also consider task-oriented retargeting which takes object state as input [13], and this setup is different from ours. However, we believe that our proposed regularization can also be used to improve these methods. We refer readers to [14] for a comprehensive review of existing retargeting approaches. 

**Shape Correspondence** Our idea is also related to shape correspondence research in vision and 3D data processing research. The goal of shape correspondence is to find some homeomorphic mapping between two manifolds [15], and the idea can also be applied to direct cartesian mapping (retargeting). Existing work typically defines some form of energy or cost functional for the whole mapping, such as elastic energy to minimize distortion. There is a rich literature on learning from functional maps, and the proposed methods have been applied to define a correspondence between different object 

This work was partially carried out during Zhao-Heng Yin’s intern at the Meta FAIR Labs. This work is supported by the Meta FAIR Labs. Zhao-Heng Yin’s research is supported by ONR MURI N00014-22-1-2773. Pieter Abbeel holds concurrent appointments as a Professor at UC Berkeley and as an Amazon Scholar. This paper describes work performed at UC Berkeley and is not associated with Amazon. 

## REFERENCES 

- [1] Zhao-Heng Yin, Changhao Wang, Luis Pineda, Francois Hogan, Krishna Bodduluri, Akash Sharma, Patrick Lancaster, Ishita Prasad, Mrinal Kalakrishnan, Jitendra Malik, et al. Dexteritygen: Foundation controller for unprecedented dexterity. _arXiv preprint arXiv:2502.04307_ , 2025. 

- [2] Ankur Handa, Karl Van Wyk, Wei Yang, Jacky Liang, Yu-Wei Chao, Qian Wan, Stan Birchfield, Nathan Ratliff, and Dieter Fox. Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _International Conference on Robotics and Automation (ICRA)_ , 2020. 

- [3] Yuzhe Qin, Wei Yang, Binghao Huang, Karl Van Wyk, Hao Su, Xiaolong Wang, Yu-Wei Chao, and Dieter Fox. Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system. In _Robotics: Science and Systems (RSS)_ , 2023. 

- [4] Runyu Ding, Yuzhe Qin, Jiyue Zhu, Chengzhe Jia, Shiqi Yang, Ruihan Yang, Xiaojuan Qi, and Xiaolong Wang. Bunny-visionpro: Real-time bimanual dexterous teleoperation for imitation learning. _arXiv preprint arXiv:2407.03162_ , 2024. 

- [5] Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, and Xiaolong Wang. Open-television: Teleoperation with immersive active visual feedback. In _Conference on Robot Learning (CoRL)_ , 2024. 

- [6] Chen Wang, Haochen Shi, Weizhuo Wang, Ruohan Zhang, Li FeiFei, and C Karen Liu. Dexcap: Scalable and portable mocap data collection system for dexterous manipulation. In _Robotics: Science and Systems (RSS)_ , 2024. 

- [7] Patrick Naughton, Jinda Cui, Karankumar Patel, and Soshi Iba. Respilot: Teleoperated finger gaiting via gaussian process residual learning. In _Conference on Robot Learning (CoRL)_ , 2024. 

- [8] Aravind Sivakumar, Kenneth Shaw, and Deepak Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube. In _Robotics: Science and Systems (RSS)_ , 2022. 

- [9] Harry G Barrow, Jay M Tenenbaum, Robert C Bolles, and Helen C Wolf. Parametric correspondence and chamfer matching: Two new techniques for image matching. In _Proceedings: Image Understanding Workshop_ , pages 21–27. Science Applications, Inc, 1977. 

- [10] Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. In _Robotics: Science and Systems (RSS)_ , 2023. 

- [11] Hangxin Liu, Xu Xie, Matt Millar, Mark Edmonds, Feng Gao, Yixin Zhu, Veronica J Santos, Brandon Rothrock, and Song-Chun Zhu. A glove-based system for studying hand-object manipulation via joint pose and force sensing. In _International Conference on Intelligent Robots and Systems (IROS)_ , 2017. 

- [12] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. In _Robotics: Science and Systems (RSS)_ , 2017. 

- [13] Arjun S Lakshmipathy, Jessica K Hodgins, and Nancy S Pollard. Kinematic motion retargeting for contact-rich anthropomorphic manipulations. _arXiv preprint arXiv:2402.04820_ , 2024. 

- [14] Roberto Meattini, Raul Suarez, Gianluca Palli, and Claudio Melchiorri. Human to robot hand motion mapping methods: Review and classification. _IEEE Transactions on Robotics_ , 39(2):842–861, 2022. 

- [15] Teuvo Kohonen. The self-organizing map. _Proceedings of the IEEE_ , 78(9):1464–1480, 1990. 

- [16] Souhaib Attaiki, Gautam Pai, and Maks Ovsjanikov. Dpfm: Deep partial functional maps. In _International Conference on 3D Vision (3DV)_ , 2021. 

- [17] Gautam Pai, Jing Ren, Simone Melzi, Peter Wonka, and Maks Ovsjanikov. Fast sinkhorn filters: Using matrix scaling for non-rigid shape correspondence with functional maps. In _IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2021. 

- [18] Nicholas Sharp, Souhaib Attaiki, Keenan Crane, and Maks Ovsjanikov. Diffusionnet: Discretization agnostic learning on surfaces. _ACM Transactions on Graphics (TOG)_ , 41(3):1–16, 2022. 

- [19] Eunsuk Chong, Lionel Zhang, and Veronica J Santos. A learning-based harmonic mapping: Framework, assessment, and case study of humanto-robot hand pose mapping. _The International Journal of Robotics Research_ , 40(2-3):534–557, 2021. 

