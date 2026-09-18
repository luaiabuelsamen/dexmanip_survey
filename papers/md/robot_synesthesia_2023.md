**Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing** 

Ying Yuan<sup>*2</sup><sup>_†_</sup> , Haichuan Che<sup>*1</sup> , Yuzhe Qin<sup>*1</sup> , Binghao Huang<sup>3</sup> , Zhao-Heng Yin<sup>4</sup> , Kang-Won Lee<sup>5</sup> , Yi Wu<sup>2</sup> , Soo-Chul Lim<sup>5</sup> , Xiaolong Wang<sup>1</sup> 

# _Training_ 















<!-- Start of picture text -->
Testing in Real World<br><!-- End of picture text -->



















Fig. 1: We propose **Robot Synesthesia** , a novel visuotactile approach to perform in-hand object rotation with visual and tactile modalities. We train our policy in simulation on rotating single or multiple objects around a certain axis and then transfer it to the real robot hand without any real-world data. 

**_Abstract_ — Executing contact-rich manipulation tasks necessitates the fusion of tactile and visual feedback. However, the distinct nature of these modalities poses significant challenges. In this paper, we introduce a system that leverages visual and tactile sensory inputs to enable dexterous in-hand manipulation. Specifically, we propose Robot Synesthesia, a novel point cloudbased tactile representation inspired by human tactile-visual synesthesia. This approach allows for the simultaneous and seamless integration of both sensory inputs, offering richer spatial information and facilitating better reasoning about robot actions. Comprehensive ablations are performed on how the integration of vision and touch can improve reinforcement learning and Sim2Real performance. Our project page is available at https://yingyuan0414.github.io/visuotactile/.** 

## I. INTRODUCTION 

In everyday life, humans effortlessly perform complex manipulation tasks, intuitively using a combination of vision 

- 1 University of California San Diego 

- 2 Tsinghua University 

> 3 University of Illinois Urbana-Champaign 

> 4 University of California Berkeley 

> 5 Dongguk University 

> * Equal contributions. 

- Work done during internship at UC San Diego. 

and touch. Considering the intricate task of threading a needle, we begin by visually locating the needle’s eye and estimating its size. Holding the needle steady in hand, we use touch information to guide the thread. Our visual sensing guides us in aligning the thread with the needle’s eye, while it’s the sense of touch from our fingertips that helps us feel the thread’s position, even when it’s occluded for our eyes to discern accurately. This synergy of vision and touch enables us to interact with our environment with remarkable flexibility and great robustness against occlusion. 

Yet, for robots tasked with similar manipulation tasks, achieving this level of sophistication remains a challenge. There are two primary hurdles that stand in the way of replicating the same level of synergy for robot learning algorithms. (i) _Tactile and visual modality are distinct in nature._ Tactile information is typically sparse and low-dimensional, captured from distinct tactile sensors and provides little contextual details. On the other hand, visual data is dense and high-dimensional, offering a rich tapestry of environmental details. When integrating these two types of data into a single neural network, the model must process and interpret each modality effectively, while also finding a way to synergize this information to facilitate intelligent decision-making. (ii) 

_Vast amounts of training data are required for such tasks_ , which is typically generated within a simulated environment. However, transferring the visuotactile skills learned in a simulator to the real world is a non-trivial problem. Each modality, vision and touch, has its own domain gap. Bridging them concurrently for a combined visual-tactile model even heightens the complexity significantly. 

In this paper, we aim to equip the robot with a policy that effectively leverages multi-modal feedback. In neuroscience studies, certain individuals can perceive color when they touch things, which refers to Tactile-Visual Synesthesia [1], [2]. Inspired by it, instead of processing each modality separately in representation learning and merging the learned features later, we propose a novel point cloud-based tactile representation. We formulate this representation in a way that “paints” the tactile data from Force-Sensing Resistor (FSR) in conjunction with the point cloud from the camera into a unified 3D space. This approach preserves the spatial relationship among the robot links, FSR sensors, and the object being manipulated. Effectively, the robot is equipped to “see” its tactile interactions, a concept we call **Robot Synesthesia** . This method allows for the seamless integration of both sensory inputs from the outset, which offers abundant spatial information, facilitating better reasoning about robot actions. Furthermore, we can easily generate these tactile point clouds in both simulated and real-world using the robot’s kinematics. This strategy can reduce the compounding errors of vision and touch during Sim-to-Real transfer, by treating these two modalities as an integrated entity. 

We focus on in-hand object rotation involving one or two objects, and along the x, y, and z axes. The robot is required to interact with a variety of objects via visuotactile sensing, while learning to prevent the objects from slipping off the hand at the same time. The task becomes more challenging when rotating two balls (the first row of Figure 1), due to the high degree of freedom and complex interaction pattern of this double-ball system. Small finger movements are insufficient to rotate them, while excessive motion risks dropping them. We first train a teacher policy in a physical simulator using Reinforcement Learning (RL) with oracle state information, which is then distilled to a student policy utilizing a PointNet [3] encoder with visual and tactile inputs. The student policy is then deployed in the real world. 

In our experiments, we evaluate the policy with eight real-world objects. Our policy can solve the challenging double-ball rotation task and generalize to novel objects for the three-axis rotation task. Furthermore, we investigate the critical point sets of the point cloud encoder and show that the proposed tactile representation assists the PointNet in locating critical points, such as fingertips, object surfaces, and tactile points that are crucial for action prediction. 

## II. RELATED WORK 

**Dexterous Manipulation** presents a wealth of opportunities for broad applications [4]–[9]. It enables the execution of intricate manipulative tasks, such as sliding [10], [11], 

rolling [12]–[16], pivoting [17], [18], and regrasping [19]– [21]. Earlier methods addressing dexterous manipulation were grounded in classical control [22], [23]. However, these methods rely on expert-engineered dynamics models, which restricts their utility for more complex tasks. To overcome these limitations, recent research has leveraged deep model-free RL for dexterous manipulation [24]–[28]. Further enriching these advancements, imitation learning and combining common RL with demonstrations has led to higher sample efficiency and more natural manipulation behaviors [29]–[37]. Dexterous in-hand manipulation has been a focal point of research interest recently [ **?** ], [38]– [43]. To generalize to new objects, researchers have explored different sensors to capture object geometry and dynamic properties. Qi _et al._ [41] demonstrated that policy could infer object position and physical properties using proprioceptive history. But without explicit object information, it was only effective for z-axis rotation tasks. Yin _et al._ [42] proposed integrating binary tactile signals with proprioception for this task. However, the tactile signal was too sparse to capture detailed geometric attributes and thus could not handle objects with non-convex shapes. To solve this, Chen _et al._ [44] utilized depth information to aid object rotation while Guzey _et al._ [45] learned non-parametric policies on both vision and touch signal. Most similar to us, a recent study [46] utilizes RGB images from optical tactile sensors and depth images for in-hand rotation. However, it necessitated continuous contact between the object and tactile sensors, constraining it to smaller objects that can be rotated on the fingertips. In contrast, our work does not impose any specific requirements on the object’s initial location and can handle objects of diverse shapes and sizes. Furthermore, our tactile point cloud representation provides explicit 3D information about the object and tactile sensors’ location, while their models are based on 2D images. As a result, our policy can solve tasks requiring more complex 3D spatial reasoning, such as rotating two balls simultaneously. 

**Visuotactile Manipulation** , the integration of visual and tactile modalities, is a fundamental mechanism for human interaction with the environment [47], which presents significant potential for enhancing robot manipulation capabilities [45], [48]–[51]. The visual modality offers a comprehensive, non-contact perspective of the environment, while the tactile modality complements this by offering detailed, contact-dependent properties such as texture, temperature, hardness, and weight. The key to integrating these modalities in robotic manipulation lies in two aspects: (i) the representation of each modality, and (ii) the strategy employed to fuse these modalities. In the visual modality, RGB images are a common choice due to their widespread availability [49], [52]. But these images do not inherently capture distance information, which is often critical in manipulation tasks. To address this limitation, researchers [44], [46] proposed using depth to handle more contact-intensive tasks such as in-hand rotation. Different from these methods, our approach utilizes the point cloud captured by a camera, inherently incorporating 3D information into the visual representation. 



<!-- Start of picture text -->
Action<br>Policy<br>Contact & Robot<br>Proprioception<br><!-- End of picture text -->

Fig. 2: **Real-World Setup.** We use an Allegro Hand attached with 16 Force-Sensing Resistors. A Microsoft Azure Kinect camera is placed facing forward the robot. 

For the tactile modality, raw sensor readings are a natural choice [53]–[55]. However, for a smaller Sim-to-Real gap, the binary contact vector has been used [42], [56]–[58]. Notably, vision-based tactile sensors, such as DIGIT [59] and GelSighT [60], can also encode tactile information into RGB images. Another critical consideration is the design of a multi-modal learning paradigm. Most existing approaches favor combining modalities at the feature level, where separate feature extractors are trained for each modality, and the predicted features are concatenated as a multi-modal representation [53], [61]. When utilizing optical tactile sensors with tactile images, the combination can also be performed at the input level, as both vision and touch are represented as RGB images [50], [52]. In contrast, our method represents tactile data as a point cloud and merges with the camera point cloud at the input level. This approach treats the combined visual and tactile data as a single input to the policy network. This innovative design, which we term Robot Synesthesia, enriches the contextual understanding for both modalities and encodes the sensory data into a cohesive 3D space. 

## III. VISUOTACTILE DEXTEROUS MANIPULATION 

## _A. System Setup_ 

As is shown in Figure 2, our hardware setup consists of an XArm6 robot arm and a 16-DOF Allegro Hand with a depth camera. We attach 16 Force-Sensing Resistors (FSR) as tactile sensors to the palm and finger links of the robot hand as suggested by [42]. We gather the contact signal from each sensor, then binarize the measurement according to a predetermined threshold _θth_ to abridge the Sim-to-Real gap. We use Isaac Gym [62] as the rigid body physics simulator. The simulation setup is visualized in Figure 1. 

To obtain visual observations, we place a Microsoft Azure Kinect camera beside the hand in both real and simulated settings. We then generate the point cloud using the depth image. As illustrated in Figure 4, the point clouds in simulation closely mirror those in reality, especially compared with RGB images. We create an augmented point cloud [25] from the robot’s proprioception to model the spatial relationship between the hand and the object, by sampling on the robot’s mesh at the current pose. To differentiate between 

the camera-generated point cloud and the augmented one, we append a one-hot vector to each point. Point cloud visualizations are shown in Figure 3. The control frequency remains consistent at 10Hz in both simulated and real environments. 

## _B. Benchmark Problems_ 

We study the dexterity of Robot Synesthesia through an in-hand object rotation task, where the goal is manipulating one or more hand-held objects to rotate along a specific axis. In this paper, we mainly focus on three distinct benchmark problems: **(i) Wheel-Wrench Rotation** : Inspired by scenarios where a user must switch handles on a wrench during use, this task involves rotating an artificial multi-way wheel wrench along the z-axis in hand without dropping it. To successfully complete this task, the robot must visually identify the next ”possible” handle for interaction while concurrently sensing the wrench’s rotation via touch. **(ii) Double-Ball Rotation** : This task requires the simultaneous manipulation of two identical balls to rotate around each other along the z-axis. Given that tactile feedback alone cannot distinguish between the balls, it is crucial for the robot to visually locate both. **(iii) Three-Axis Rotation** : This task extends beyond the z-axis to require the robot to rotate objects around a fixed x or y-axis. Moreover, the policy should demonstrate the ability to manipulate a variety of objects with different shapes, extending its dexterity to objects not included in the training set. 

## IV. LEARNING VISUOTACTILE DEXTERITY 

## _A. Problem Formulation_ 

We formulate the in-hand object rotation task as a Markov Decision Process ( _S, A, P, R, γ_ ). Here, _S_ is the state space, _A_ is the action space, _P_ ( _s_<sup>_′_</sup> _|s, a_ ) is the transition probability, _R_ is the reward function, and _γ_ is the discounted factor. The objective is to find an optimal _θ_<sup>_∗_</sup> that maximizes the expected accumulated reward<sup>�</sup><sup>_T_</sup> _t_ =0<sup>_γtrt_.Anepisodetermi-</sup> nates when reset conditions are achieved or the agent reaches the maximum number of steps _T_ . We prune unnecessary explorations when the object falls off the hand to facilitate efficient training. _1) State:_ The state of the system consists of the joint position _qt ∈_ R<sup>16</sup> of the Allegro hand, the binary tactile signal _ot ∈{_ 0 _,_ 1 _}_<sup>16</sup> , the rotation axis _k ∈_ S<sup>2</sup> , the previous position target _q_ ˆ _t ∈_ R<sup>16</sup> , the camera point cloud _Pt_<sup>_c_</sup> _∈_ R<sup>_Nc×_3</sup> , the augmented point cloud _Pt_<sup>_a∈_R</sup><sup>_Na×_3,andthe</sup> tactile point cloud _Pt_<sup>_touch_</sup> _∈_ R<sup>_Na×_3</sup> . 

_2) Action:_ At each step, the action provided by the policy network is a relative control command _at ∈_ R<sup>16</sup> and a PD controller drives the robot hand to approach _q_ ˆ _t_ +1 = _q_ ˆ _t_ + ˆ _at_ . Note that we employ an exponential moving average in our implementation, i.e., _a_ ˆ _t_ = _ηat_ + (1 _− η_ )ˆ _at−_ 1 _, t ≥_ 1 and let _a_ ˆ0 = 0. We set _η_ = 0 _._ 8 in our experiments. 

_3) Reward:_ We design a reward function for robust and transferable in-hand rotation, which is a weighted composition of several components: 

_rt_ = _c_ 1 _rrot_ + _c_ 2 _rvel_ + _c_ 3 _rdist_ + _c_ 4 _rtorq_ + _c_ 5 _rwork_ + _c_ 6 _rctrl._ (1) 



<!-- Start of picture text -->
X Y Z Teacher<br>X Y Z Tactile  Robot  Critic MLP<br>+ Synesthesia Proprioception  Value<br>X Y Z<br>Binary Contact<br>PPO<br>Object Pose Actor MLP<br>Action<br>Shape Feature<br>Robot  Behavior<br>Proprioception Cloning<br>Binary Contact Actor MLP<br>+ Action<br>PointNet<br>Camera  & X Y Z Student<br>X Y Z +<br>Augmented + + Concatenate (dim=0)<br>Point Cloud X Y Z + Concatenate (dim=-1)<br>.. . .. .<br>.. . . ..<br><!-- End of picture text -->

Fig. 3: **Training Pipeline.** Our teacher policy takes robot proprioception, binary contact, object pose, and object shape embedding as input. After training the teacher policy via RL, we distill it to a visuotactile-based student policy. Besides robot proprioception and touch signal, the student <u>policy</u> takes a <u>point</u> cloud from depth-camera, an augmented point cloud based on robot proprioception, and the proposed tactile point cloud. We use one-hot vectors to distinguish point clouds. Note that we’ve eliminated noise from the point clouds for better clarity here. 



<!-- Start of picture text -->
Sim Image Sim Point Cloud<br><!-- End of picture text -->





Real Image 

Real Point Cloud 

Fig. 4: **Point Cloud Visualization in Sim and Real.** The Sim-to-Real gap is notably larger for RGB images compared to point clouds, leading us to select point clouds as the visual observation for our policy. 

set the number of sampled points _Nc_ = 512 _, Na_ = 8 _nlink_ , and _Nt_ = 8 _ntouch_ , where _nlink_ = 21 is the number of links on hand and _ntouch ∈{_ 0 _, · · · ,_ 16 _}_ is the number of triggered tactile sensors. Our experiments demonstrate that points sampled from active tactile sensors are implicitly chosen by our learned policy for representation learning. Note that we transform all point clouds to the hand palm [63] frame before feeding them into the neural network. 

_rrot_ rewards the object’s rotation angle. _rvel_ penalizes the object’s linear velocity to discourage motions that translate the object. _rdist_ is a decreasing function regarding the distance between the object and the fingertips, encouraging the fingers to approach the object in hand and interact with it. _rtorq_ penalizes large torques, _rwork_ penalizes the work of the controller, and _rctrl_ penalizes the control error between command targets and real robot motion. We additionally implement a large penalty when the object falls off the hand. _c_ 1 _, c_ 2 _, · · · , c_ 6 are tuned hyper-parameters. 

## _B. Tactile-Visual Synesthesia_ 

Instead of processing tactile and visual modalities separately for feature extraction, we unify tactile and visual modalities by projecting them onto a single 3D space, similar to how humans might simultaneously perceive touch and visual stimuli in their minds. Concretely, for each tactile sensor on the hand that detects a signal (i.e., _ot,i_ = 1), we sample points on the sensor’s meshes to create a tactile-based point cloud _Pt_<sup>_touch_</sup> . When combining _Pt_<sup>_touch_</sup> with _Pt_<sup>_c_and</sup> _Pt_<sup>_a_, we provide the policy network with a spatial relationship</sup> of all the observation entities. In our implementation, we 

## _C. Teacher-Student Training Pipeline_ 

Learning the controller _π_ using RL is data inefficient when the observation is high-dimensional, e.g., point clouds. To mitigate this issue, we employ a teacher-student learning approach to obviate training vision policies with RL, as shown in Figure 3. 

_1) Teacher policy training:_ We first use the proximal policy optimization (PPO) [64] to train teacher policies with low-dimensional states. Its input consists of the joint position of the Allegro hand _qt_ , the binary tactile signal _ot_ , the rotation axis _k_ , the previous position target _q_ ˆ _t_ , the object’s position _xt ∈_ R<sup>3</sup> , its velocity _vt ∈_ R<sup>3</sup> , its angular velocity _wt ∈_ R<sup>3</sup> , and the object’s shape feature embedding _f ∈_ R<sup>32</sup> . For tasks that require generalizability over multiple objects, we encode the shape information via a pre-trained PointNet [3] encoder in [33]. Note that for each object, the shape feature embedding remains the same throughout the training. Given the state information, we use a Multi Layer Perceptron (MLP) for both policy and value networks. We stack the current state with 3 historical states as input for better perception. 



Fig. 5: **Object Sets in Sim and Real.** We use artificial objects for training and daily objects for testing. 

_2) Student policy training:_ After using RL to train the teacher policy, we distill it to a student policy with visuotactile input. Concretely, its input includes the joint position _qt_ , the binary tactile signal _ot_ , the rotation axis _k_ , and the previous position target _q_ ˆ _t_ . We stack it with 3 historical states. For the visual observation, the input includes camera point cloud _Pt_<sup>_c_, augmented point cloud</sup><sup>_P a_</sup> _t_<sup>, and the proposed</sup> tactile point cloud _Pt_<sup>_touch_</sup> . We attach a one-hot vector to each point and concatenate them together as _Pt_ . 

We use PointNet [3] as the point cloud encoder and feed the latent vector and other inputs into an MLP. We adopt a two-stage distillation pipeline: We first collect a teacher dataset _D_ of 5120 _k_ transitions and use Behavior Cloning (BC) to pre-train our student policy network; in the second stage, we use Dataset Aggregation (DAgger) [65] to fine-tune the network for more robust behavior. 

## V. EXPERIMENTS 

In this part, we compare our robot synesthesia approach to several baselines in both the simulation and the real. Specifically, we are interested in the following questions: 

1) _How much benefit do visual and tactile modalities offer?_ 

- 2) _Is teacher-student pipeline necessary for efficient training given both tactile and visual modalities?_ 

- 3) _How does our policy network process the two modalities through synesthesia?_ 

## _A. Setup_ 

_1) Object Dataset:_ The objects used for the benchmark problems are shown in Figure 5. For task (i), we use an artificially designed four-way wheel wrench in both simulation and real. For task (ii), we use two balls of the same size. For task (iii), we train and evaluate our policy on a set of artificial objects of common geometries _S_ , such as cuboids, cylinders, polygons, etc. in the simulation. For real deployment, we use cubes and other daily objects of distinct sizes and shapes to test our policy’s generalization ability. 

_2) Evaluation Metric:_ To evaluate the policy performance, we use the following metrics as suggested by [41]. 

- 1) **Cumulative Rotation Reward (CRR)** is the reward our agent obtains in an episode. We use it to evaluate the rotation capability of a policy in the simulation. 

- 2) **Cumulative Rotation Angle (CRA)** is the angle (by rounds) the object rotates along the axis in an episode. We use it to evaluate a policy in the real. 

- 3) **Time-to-Fall (TTF/Duration)** is the length of an episode (by seconds). TTF varies when the object falls off before the maximal episode length. 



Fig. 6: Learning curve of teacher policy on double-ball rotation. The results are averaged on 3 seeds. 



Fig. 7: Visualization of selected point clouds (foreground) among observed point clouds (background) during evaluation. Red points belong to the proposed tactile point cloud. 

_B. Stage I: RL training with different sensing capabilities_ 

In this section, we experiment with training RL teacher policies in the simulation. We compare our implementation with two baselines: **Partially-observable-State(PS/Nonvisual RL)** policy [42] is a non-visual policy that observes only robot proprioception and contact signals; **Visual RL** policy is a visuotactile policy trained via RL from scratch. Figure 6 shows learning curves of double-ball rotation and multi-object rotation around the x-axis. We find that our method achieves a higher reward compared with PS, and that visual RL hardly learns high-rewarding actions within the same number of training epochs. We evaluate policies trained on the benchmark problems for 500 episodes as is shown in Table I. Our approach outperforms PS and Visual RL in all the tasks. This indicates that the ground-truth object pose is essential for robust and meticulous manipulation, especially when the object, e.g. multi-way wrenches, requires different actions as its direction varies. Also, learning vision-based RL policies is data-inefficient, probably because the policy needs to extract features from high-dimensional inputs and learn high-rewarding actions simultaneously. 

_C. Stage II: Imitation learning with different sensing capabilities_ 

In this stage, we distill teacher policies to visuotactile policies and perform ablation study for different sensing capabilities. As shown in Table II, **Touch** refers to binary contact, **Cam** refers to camera-based point clouds, **Aug** refers to augmented point clouds, and **Syn** refers to proposed tactile point clouds. For rotating objects of regular shapes, visual policies achieve similar dexterity to each other. However, 

TABLE I: Evaluation of RL policies of different sensing capabilities on three benchmark problems in the simulation. Each policy is tested for 500 episodes. The results are averaged over 3 policies trained on 3 seeds. Each trial lasts 50 seconds. 

|ObsTe|4-way|Wrench|Double|Balls|Multi-Objec|t (x-axis)|Multi-Obje|ct (y-axis)|Multi-Objec|t (z-axis)|
|---|---|---|---|---|---|---|---|---|---|---|
|yp|CRR|TTF|CRR|TTF|CRR|TTF|CRR|TTF|CRR|TTF|
|Visual RL|10.9_±_2_._2|8.1_±_3_._2|127.8_±_78_._6|10.5_±_3_._7|15.3_±_8_._2|16.8_±_11_._8|22.4_±_8_._8|21.4_±_17_._8|29.5_±_7_._1|2.9_±_0_._4|
|PS|440.7_±_590_._3|22.6_±_18_._5|620.9_±_39_._9|28.8_±_0_._7|446.1_±_137_._7|33.1_±_7_._1|552.1_±_318_._7|33.5_±_8_._3|878.7_±_528_._3|36.9_±_15_._4|
|Ours|**1011.1**_±_329_._9|**47.5**_±_0_._4|**1045.3**_±_64_._9|**36.2**_±_2_._3|**985.9**_±_174_._1|**45.1**_±_2_._6|**987.3**_±_141_._9|**46.8**_±_1_._0|**1353.7**_±_123_._8|**48.2**_±_0_._4|



TABLE II: Evaluation of student policies of different sensing capabilities on three benchmark problems in the simulation. Each policy is tested for 500 episodes. Each trial lasts 50 seconds. 

|Obs Type|4-way <br>CRR|Wrench<br>TTF|Double <br>CRR|Balls<br>TTF|Multi-Ob<br>CRR|ject (x-axis)<br>TTF|Multi-Ob<br>CRR|ject (y-axis)<br>TTF|Multi-Obje<br>CRR|c|t (z-axis)<br>TTF|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Touch|363.2|23.6|317.1|13.6|390.9|24.2|710.9|42.6|702.4||35.6|
|Cam+Aug|94.6|15.2|162.7|9.6|630.9|40.3|**743.5**|**42.9**|624.2||29.2|
|Touch+Cam+Aug|344.1|21.1|148.6|9.6|**881.1**|**47.4**|619.0|41.3|909.8||37.7|
|Touch+Cam+Aug+Syn|**504.0**|**29.2**|**407.7**|**17.1**|846.9|39.9|686.8|41.2|**1035.0**||**41.3**|



TABLE III: Evaluation of policies (CRA/TTF) in the real-world deployment. The above two lines refer to non-visual methods and the rest are visual policies. Each policy is tested for 5 episodes. Each trial lasts 60 seconds. 

|Obs Type<br>(CRA/TTF)|4-way Wrench|Double Balls|Multi-Object (x-axis)|Multi-Object (y-axis)|Multi-Object (z-axis)|
|---|---|---|---|---|---|
|Non-visual RL<br>Touch|0.25/60.0<br>0.25/60.0|0.2/28.6<br>15.6/26.7|0.35/60.0<br>0.7/60.0|1.0/60.0<br>0.2/60.0|8.6/60.0<br>7.4/60.0|
|Cam+Aug|0.25/60.0|10.1/20.8|0.25/60.0|1.0/33.3|5.1/60.0|
|Touch+Cam+Aug|0.25/60.0|18.8/32.7|0.5/60.0|**1.4/28.3**|5.1/57.1|
|Touch+Cam+Aug+Syn|**1.5/43.0**|**22.9/36.6**|**2.1/26.6**|0.9/29.3|**10.2/60.0**|



when it comes to more challenging objects like multi-way wrenches and two balls, our method outperforms all the baselines. 

## _D. Real-world Deployment_ 

We transfer the visuotactile policies to the real robot without any fine-tuning and test whether visual policies continue to provide benefits. The results are shown in Table III. Although visual policy might show comparable performance for simple geometry in simulation, the advantage of integrating vision and touch becomes more significant when deployed to the real world. **These results highlight the low domain gap of our proposed tactile point cloud representation.** A rudimentary concatenation of tactile signals and the extracted features of point clouds could increase the challenge for the policy to comprehend their underlying relationship. In contrast, our proposed visual-tactile synesthesia approach generally offers benefits. We also observe that visual policies tend to operate more cautiously, making occasional adjustments to nudge the object back to the palm center, while policies lacking visual perception tend to execute an almost fixed sequence of motion, irrespective of the object’s deviation or instances of it becoming stuck. 

_E. Qualitative Analysis: Visualization of PointNet intermediates_ 

In PointNet, the input point cloud is fed into a local MLP extracting features of each point before a Max Pooling layer over points in each dimension of the features. Thus, PointNet is trained to implicitly select no more than _cout_ points for 

representation learning, where _cout_ is the output dimension of PointNet. We visualize in Figure 7 the points selected by our policy during evaluation. Interestingly, we find that our policy uses 42.7% of tactile-based points on average and the rest points are mainly from the tips or edges of fingers and the palm. This indicates that the point cloud encoder can extract meaningful features based on our visual-tactile synesthesia design. 

## VI. CONCLUSION 

This paper introduces a system for in-hand dexterous manipulation utilizing visuotactile sensing. We propose a novel tactile representation based on point clouds, and a paired network architecture to leverage it. Our results show that the policy, which has been trained in a simulator using vision and touch input, effectively transfers to the real world. It can solve complex tasks such as double-ball rotation and generalize to novel objects. Future work may encompass goal-conditioned object rotation tasks and the integration of optical tactile sensors. We are committed to releasing the code for our simulation environment and training pipeline. 

## VII. ACKNOWLEDGEMENT 

Acknowledgment: This work was supported, in part, by the Qualcomm Innovation Fellowship, and the Technology Innovation Program (20018112, Development of autonomous manipulation and gripping technology using imitation learning based on visual and tactile sensing) funded by the Ministry of Trade, Industry & Energy (MOTIE), Korea. 

REFERENCES 

- [1] J. Simner and V. U. Ludwig, “The color of touch: A case of tactile– visual synaesthesia,” _Neurocase_ , vol. 18, no. 2, pp. 167–180, 2012. 

- [2] A. M. A. Davies and R. C. White, “A sensational illusion: vision-touch synaesthesia and the rubber hand paradigm,” _Cortex_ , vol. 49, no. 3, pp. 806–818, 2013. 

- [3] C. R. Qi, H. Su, K. Mo, and L. J. Guibas, “Pointnet: Deep learning on point sets for 3d classification and segmentation,” _CoRR_ , vol. abs/1612.00593, 2016. 

- [4] A. M. Okamura, N. Smaby, and M. R. Cutkosky, “An overview of dexterous manipulation,” in _IEEE International Conference on Robotics and Automation. Symposia Proceedings_ , 2000. 

- [5] N. Chavan-Dafle and A. Rodriguez, “Sampling-based planning of inhand manipulation with external pushes,” in _Robotics Research: The 18th International Symposium ISRR_ . Springer, 2020, pp. 523–539. 

- [6] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray _et al._ , “Learning dexterous in-hand manipulation,” _The International Journal of Robotics Research (IJRR)_ , vol. 39, no. 1, pp. 3–20, 2020. 

- [7] Y. Qin, W. Yang, B. Huang, K. Van Wyk, H. Su, X. Wang, Y.-W. Chao, and D. Fox, “Anyteleop: A general vision-based dexterous robot armhand teleoperation system,” _arXiv preprint arXiv:2307.04577_ , 2023. 

- [8] K. Shaw and D. Pathak, “Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning,” _Submission, ICRA_ , 2023. 

- [9] J. Ye, J. Wang, B. Huang, Y. Qin, and X. Wang, “Learning continuous grasping function with a dexterous hand from human demonstrations,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2023. 

- [10] M. Cherif and K. K. Gupta, “Planning quasi-static fingertip manipulations for reconfiguring objects,” _IEEE Transactions on Robotics and Automation_ , vol. 15, no. 5, pp. 837–848, 1999. 

- [11] J. Shi, J. Z. Woodruff, P. B. Umbanhowar, and K. M. Lynch, “Dynamic in-hand sliding manipulation,” _IEEE Transactions on Robotics_ , vol. 33, no. 4, pp. 778–795, 2017. 

- [12] L. Han, Y.-S. Guan, Z. Li, Q. Shi, and J. C. Trinkle, “Dextrous manipulation with rolling contacts,” in _International Conference on Robotics and Automation (ICRA)_ , 1997. 

- [13] L. Han and J. Trinkle, “Dextrous manipulation by rolling and finger gaiting,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , 1998. 

- [14] A. Bicchi and R. Sorrentino, “Dexterous manipulation through rolling,” in _Proceedings of 1995 IEEE International Conference on Robotics and Automation_ , vol. 1, 1995, pp. 452–457 vol.1. 

- [15] Z. Doulgeri and L. Droukas, “On rolling contact motion by robotic fingers via prescribed performance control,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , 2013. 

- [16] M. Lepert, C. Pan, S. Yuan, R. Antonova, and J. Bohg, “In-hand manipulation of unknown objects with tactile sensing for insertion,” in _Embracing Contacts-Workshop at ICRA 2023_ , 2023. 

- [17] Y. Aiyama, M. Inaba, and H. Inoue, “Pivoting: A new method of graspless manipulation of object by robot fingers,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 1993. 

- [18] E. Yoshida, P. Blazevic, and V. Hugel, “Pivoting manipulation of a large object: A study of application using humanoid platform,” in _Proceedings of the 2005 IEEE International Conference on Robotics and Automation_ . IEEE, 2005, pp. 1040–1045. 

- [19] P. Tournassoud, T. Lozano-P´erez, and E. Mazer, “Regrasping,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , 1987. 

- [20] P. Vinayavekhin, S. Kudoh, and K. Ikeuchi, “Towards an automatic robot regrasping movement based on human demonstration using tangle topology,” in _2011 IEEE International Conference on Robotics and Automation_ . IEEE, 2011, pp. 3332–3339. 

- [21] A. A. Cole, P. Hsu, and S. S. Sastry, “Dynamic control of sliding by robot hands for regrasping,” _IEEE Transactions on robotics and automation_ , vol. 8, no. 1, pp. 42–52, 1992. 

- [22] V. Kumar, Y. Tassa, T. Erez, and E. Todorov, “Real-time behaviour synthesis for dynamic hand-manipulation,” in _2014 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2014, pp. 6808–6815. 

- [23] Y. Bai and C. K. Liu, “Dexterous manipulation using both palm and fingers,” in _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , 2014, pp. 1560–1565. 

- [24] T. Chen, J. Xu, and P. Agrawal, “A system for general in-hand object re-orientation,” in _Conference on Robot Learning (CoRL)_ , 2022, pp. 297–307. 

- [25] Y. Qin, B. Huang, Z.-H. Yin, H. Su, and X. Wang, “Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation,” in _Conference on Robot Learning (CoRL)_ , 2022. 

- [26] G. Khandate, M. Haas-Heger, and M. Ciocarlie, “On the feasibility of learning finger-gaiting in-hand manipulation with intrinsic sensing,” in _International Conference on Robotics and Automation (ICRA)_ , 2022. 

- [27] C. Bao, H. Xu, Y. Qin, and X. Wang, “Dexart: Benchmarking generalizable dexterous manipulation with articulated objects,” in _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2023, pp. 21 190–21 200. 

- [28] B. Huang, Y. Chen, T. Wang, Y. Qin, Y. Yang, N. Atanasov, and X. Wang, “Dynamic handover: Throw and catch with bimanual hands,” in _7th Annual Conference on Robot Learning_ , 2023. 

- [29] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang, “Dexmv: Imitation learning for dexterous manipulation from human videos,” in _European Conference on Computer Vision (ECCV)_ , 2022. 

- [30] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine, “Learning complex dexterous manipulation with deep reinforcement learning and demonstrations,” in _Robotics: Science and Systems (RSS)_ , 2018. 

- [31] S. P. Arunachalam, S. Silwal, B. Evans, and L. Pinto, “Dexterous imitation made easy: A learning-based framework for efficient dexterous manipulation,” _arXiv preprint arXiv:2203.13251_ , 2022. 

- [32] Y. Qin, H. Su, and X. Wang, “From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 4, pp. 10 873–10 881, 2022. 

- [33] Y.-H. Wu, J. Wang, and X. Wang, “Learning generalizable dexterous manipulation from human grasp affordance,” in _Conference on Robot Learning (CoRL)_ , 2022. 

- [34] X. Liu, D. Pathak, and K. M. Kitani, “Herd: Continuous humanto-robot evolution for learning from human demonstration,” _arXiv preprint arXiv:2212.04359_ , 2022. 

- [35] A. Patel, A. Wang, I. Radosavovic, and J. Malik, “Learning to imitate object interactions from internet videos,” _arXiv preprint arXiv:2211.13225_ , 2022. 

- [36] S. P. Arunachalam, I. G¨uzey, S. Chintala, and L. Pinto, “Holo-dex: Teaching dexterity with immersive mixed reality,” _arXiv preprint arXiv:2210.06463_ , 2022. 

- [37] A. Sivakumar, K. Shaw, and D. Pathak, “Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube,” _arXiv preprint arXiv:2202.10448_ , 2022. 

- [38] A. Bhatt, A. Sieler, S. Puhlmann, and O. Brock, “Surprisingly robust in-hand manipulation: An empirical study,” in _Robotics: Science and Systems (RSS)_ , 2021. 

- [39] A. Nagabandi, K. Konolige, S. Levine, and V. Kumar, “Deep dynamics models for learning dexterous manipulation,” in _Conference on Robot Learning_ . PMLR, 2020, pp. 1101–1112. 

- [40] A. S. Morgan, K. Hang, B. Wen, K. Bekris, and A. M. Dollar, “Complex in-hand manipulation via compliance-enabled finger gaiting and multi-modal planning,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, pp. 4821–4828, 2022. 

- [41] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik, “In-hand object rotation via rapid motor adaptation,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 1722–1732. 

- [42] Z.-H. Yin, B. Huang, Y. Qin, Q. Chen, and X. Wang, “Rotating without seeing: Towards in-hand dexterity through touch,” _Robotics: Science and Systems_ , 2023. 

- [43] L. R¨ostel, J. Pitz, L. Sievers, and B. B¨auml, “Estimator-coupled reinforcement learning for robust purely tactile in-hand manipulation,” in _2023 IEEE-RAS 22nd International Conference on Humanoid Robots (Humanoids)_ . IEEE, 2023, pp. 1–8. 

- [44] T. Chen, M. Tippur, S. Wu, V. Kumar, E. Adelson, and P. Agrawal, “Visual dexterity: In-hand dexterous manipulation from depth,” in _Icml workshop on new frontiers in learning, control, and dynamical systems_ , 2023. 

- [45] I. Guzey, B. Evans, S. Chintala, and L. Pinto, “Dexterity from touch: Self-supervised pre-training of tactile representations with robotic play,” _arXiv preprint arXiv:2303.12076_ , 2023. 

- [46] H. Qi, B. Yi, S. Suresh, M. Lambeta, Y. Ma, R. Calandra, and J. Malik, “General in-hand object rotation with vision and touch,” in _7th Annual Conference on Robot Learning_ , 2023. 

- [47] P. Jenmalm and R. S. Johansson, “Visual and somatosensory information about object shape control manipulative fingertip forces,” _Journal of Neuroscience_ , vol. 17, no. 11, pp. 4486–4499, 1997. 

- [48] Y. Chen, A. Sipos, M. Van der Merwe, and N. Fazeli, “Visuo-tactile transformers for manipulation,” _arXiv preprint arXiv:2210.00121_ , 2022. 

- [49] P. Falco, S. Lu, A. Cirillo, C. Natale, S. Pirozzi, and D. Lee, “Cross-modal visuo-tactile object recognition using robotic active exploration,” in _2017 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2017, pp. 5273–5280. 

- [50] S. Wang, J. Wu, X. Sun, W. Yuan, W. T. Freeman, J. B. Tenenbaum, and E. H. Adelson, “3d shape perception from monocular vision, touch, and shape priors,” in _2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2018, pp. 1606– 1613. 

- [51] A. Billard and D. Kragic, “Trends and challenges in robot manipulation,” _Science_ , vol. 364, no. 6446, p. eaat8414, 2019. 

- [52] R. Calandra, A. Owens, D. Jayaraman, J. Lin, W. Yuan, J. Malik, E. H. Adelson, and S. Levine, “More than a feeling: Learning to grasp and regrasp using vision and touch,” _IEEE Robotics and Automation Letters_ , vol. 3, no. 4, pp. 3300–3307, 2018. 

- [53] M. A. Lee, Y. Zhu, K. Srinivasan, P. Shah, S. Savarese, L. Fei-Fei, A. Garg, and J. Bohg, “Making sense of vision and touch: Selfsupervised learning of multimodal representations for contact-rich tasks,” in _2019 International Conference on Robotics and Automation (ICRA)_ . IEEE, 2019, pp. 8943–8950. 

- [54] R. Bischoff and V. Graefe, “Integrating vision, touch and natural language in the control of a situation-oriented behavior-based humanoid robot,” in _IEEE SMC’99 Conference Proceedings. 1999 IEEE International Conference on Systems, Man, and Cybernetics (Cat. No. 99CH37028)_ , vol. 2. IEEE, 1999, pp. 999–1004. 

- [55] I. Guzey, Y. Dai, B. Evans, S. Chintala, and L. Pinto, “See to touch: Learning tactile dexterity through visual incentives,” _arXiv preprint arXiv:2309.12300_ , 2023. 

- [56] A. Petrovskaya and O. Khatib, “Global localization of objects via touch,” _IEEE Transactions on Robotics_ , vol. 27, no. 3, pp. 569–585, 2011. 

- [57] D. Driess, P. Englert, and M. Toussaint, “Active learning with query paths for tactile object shape exploration,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2017. 

- [58] J. Liang, A. Handa, K. Van Wyk, V. Makoviychuk, O. Kroemer, and D. Fox, “In-hand object pose tracking via contact feedback and gpuaccelerated robotic simulation,” in _IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2020, pp. 6203–6209. 

- [59] M. Lambeta, P.-W. Chou, S. Tian, B. Yang, B. Maloon, V. R. Most, D. Stroud, R. Santos, A. Byagowi, G. Kammerer _et al._ , “Digit: A novel design for a low-cost compact high-resolution tactile sensor with application to in-hand manipulation,” _IEEE Robotics and Automation Letters_ , vol. 5, no. 3, pp. 3838–3845, 2020. 

- [60] W. Yuan, S. Dong, and E. H. Adelson, “Gelsight: High-resolution robot tactile sensors for estimating geometry and force,” _Sensors_ , vol. 17, no. 12, p. 2762, 2017. 

- [61] J. Hansen, F. Hogan, D. Rivkin, D. Meger, M. Jenkin, and G. Dudek, “Visuotactile-rl: learning multimodal manipulation policies with deep reinforcement learning,” in _2022 International Conference on Robotics and Automation (ICRA)_ . IEEE, 2022, pp. 8298–8304. 

- [62] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa _et al._ , “Isaac gym: High performance gpu-based physics simulation for robot learning,” _arXiv preprint arXiv:2108.10470_ , 2021. 

- [63] M. Liu, X. Li, Z. Ling, Y. Li, and H. Su, “Frame mining: a free lunch for learning robotic manipulation from 3d point clouds,” _arXiv preprint arXiv:2210.07442_ , 2022. 

- [64] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” _arXiv preprint arXiv:1707.06347_ , 2017. 

- [65] S. Ross, G. J. Gordon, and J. A. Bagnell, “No-regret reductions for imitation learning and structured prediction,” _CoRR_ , vol. abs/1011.0686, 2010. 

