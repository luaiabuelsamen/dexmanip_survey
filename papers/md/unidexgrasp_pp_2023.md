# **UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning** 

Weikang Wan<sup>1*</sup> Haoran Geng<sup>1,3*</sup> Yun Liu<sup>2</sup> Zikang Shan<sup>1</sup> Yaodong Yang<sup>1,3</sup> Li Yi<sup>2</sup> He Wang<sup>1†</sup> 1Peking University 2Tsinghua University 3Beijing Institute for General Artificial Intelligence 



<!-- Start of picture text -->
UniDex rasp<br><!-- End of picture text -->

Figure 1: In this work, we present a novel dexterous grasping policy learning pipeline, UniDexGrasp++. Same to UniDexGrasp[71], UniDexGrasp++ is trained on 3000+ different object instances with random object poses under a table-top setting. It significantly outperforms the previous SOTA and achieves 85.4% and 78.2% success rates on the train and test set. 

##### **Abstract** 

We propose a novel, object-agnostic method for learning a universal policy for dexterous object grasping from realistic point cloud observations and proprioceptive information under a table-top setting, namely UniDexGrasp++. To address the challenge of learning the vision-based policy across thousands of object instances, we propose Geometry-aware Curriculum Learning ( **_GeoCurriculum_** ) and Geometry-aware iterative Generalist-Specialist Learning ( **_GiGSL_** ) which leverage the geometry feature of the task and significantly improve the generalizability. With our proposed techniques, our final policy shows universal dexterous grasping on thousands of object instances with **85.4%** and **78.2%** success rate on the train set and test set which outperforms the state-of-the-art baseline UniDexGrasp by 11.7% and 11.3%, respectively. 

> *Equal contribution. 

> †Corresponding author. 

## **1. Introduction** 

Robotic grasping is a fundamental and extensively studied problem in robotics, and it has recently gained broader attention from the computer vision community. Recent works [62, 6, 18, 24, 67, 17, 13] have made significant progress in developing grasping algorithms for parallel grippers, using either reinforcement learning or motion planning. However, traditional parallel grippers have limited flexibility, which hinders their ability to assist humans in daily life. 

Consequently, dexterous grasping is becoming more important, as it provides a more diverse range of grasping strategies and enables more advanced manipulation techniques. The high dimensionality of the action space (e.g., 24 to 30 degrees of freedom) of a dexterous hand is a key advantage that provides it with high versatility and, at the same time, the primary cause of the difficulty in executing a successful grasp. What’s more, the complex hand articulation significantly degrades motion planning-based grasping 

methods, making RL the mainstream of dexterous grasping. 

However, it is very challenging to directly train a visionbased universal dexterous grasping policy [37, 38, 40, 59]. First, vision-based policy learning is known to be difficult, since the policy gradients from RL are usually too noisy to update the vision backbone. Second, such policy learning is in nature a multi-task RL problem that carries huge variations (e.g., different geometry and poses) and is known to be hard [40, 29, 59]. Despite recent advancements in reinforcement learning (RL) [4, 2, 37, 8, 9, 49, 41, 27, 38, 58, 69]that have shown promising results in complex dexterous manipulation, the trained policy cannot easily generalize to a large number of objects and the unseen. At the same time, most works [4, 2, 69, 9, 58, 49, 27] assume the robot knows all oracle information such as object position and rotation, making them unrealistic in the real world. 

A recent work, UniDexGrasp [70], shows promising results in vision-based dexterous grasping on their benchmark that covers more than 3000 object instances. Their policy only takes robot proprioceptive information and realistic point cloud observations as input. To ease policy learning, UniDexGrasp proposes object curriculum learning that starts RL with one object and gradually incorporates similar objects from the same categories or similar categories into training to get a state-based teacher policy. After getting this teacher policy, they distill this policy to a vision-based policy using DAgger [51]. It finally achieves 73 _._ 7% and 66 _._ 9% success rates on the train and test splits. One limitation of UniDexGrasp is that its state-based teacher policy can only reach 79 _._ 4% on the training set, which further constrains the performance of the vision-based student policy. Another limitation in the object curriculum is unawareness of object pose and reliance on category labels. 

To overcome these limitations, we propose UniDexGrasp++, a novel pipeline that significantly improves the performance of UniDexGrasp. First, to improve the performance of the state-based teacher policy, we first propose Geometry-aware Task Curriculum Learning **_(GeoCurriculum)_** that measures the task similarity based on the geometry feature of the scene point cloud. To further improve the generalizability of the policy, we adopt the idea of _generalist-specialist learning_ [63, 39, 23, 29] where a group of specialists is trained on the subset of the task space then distill to one generalist. We further propose Geometry-aware iterative Generalist-Specialist Learning **_GiGSL_** where we use the geometry feature to decide which specialist handles which task and iteratively do distillation and fine-tuning. Our method yields the bestperforming state-based policy, which achieves **87.9%** and **83.7%** success rate on the train set and test set. Then we distill the best-performing specialists to a vision-based generalist and do GiGSL again on vision-based policies until it reaches performance saturation. With our full pipeline, our 

final vision-based policy shows universal dexterous grasping on 3000+ object instances with **85.4%** and **78.2%** success rate on the train set and test set that remarkably outperforms the state-of-the-art baseline UniDexGrasp by 11.7% and 11.3%, respectively. The additional experiment on Meta-World [73] further demonstrates the effectiveness of our method which outperforms the previous SOTA multitask RL methods. 

## **2. Related Work** 

### **2.1. Dexterous Grasping** 

Dexterous hand has received extensive attention for its potential for human-like manipulation in robotics [53, 52, 43, 14, 3, 12, 33, 32, 41, 36, 45, 35]. It is of high potential yet very challenging due to its high dexterity. Dexterous grasping is a topic of much interest in this field. Some works [5, 15, 3] have leveraged analytical methods to model the kinematics and dynamics of both hands and objects, but they typically require simplifications, such as using simple finger and object geometries, to ensure the feasibility of the planning process. Recent success has been shown in using reinforcement learning and imitation learning methods [8, 9, 49, 41, 27, 4, 58, 69]. While these works have shown encouraging results, they all suppose that the robot can get all the oracle states (e.g., object position, velocity) during training and testing. However, this state information can not be easily and accurately captured in the real world. To mitigate this issue, some works [38, 37, 46, 70] consider a more realistic setting with the robot proprioception and RGB image or 3D scene point cloud as the input of the policy which can be captured more easily in the real world. Our work is more related to the recently proposed work UniDexGrasp [70] which learns a vision-based policy over 3000+ different objects. In this paper, we propose a novel pipeline that significantly improves the performance and generalization of UniDexGrasp, namely UniDexGrasp++. 

### **2.2. Vision-based Policy Learning** 

Extensive research has been conducted to explore the learning of policies from visual inputs [74, 30, 60, 72, 61, 22, 21, 20]. To ease the optimization and training process, some works have utilized a pre-trained vision model and frozen the backbone, as shown in works such as [57, 48, 56]. Others, such as [69, 68], have employed multi-stage training. Our work is more related to [8, 7, 70], who firstly train a state-based policy and then distill to a vision-based policy. Also, our work makes good use of the pre-training of vision-backbone in the loop of imitation (supervised) learning and reinforcement learning which enables us to train a generalizable policy under the vision-based setting. 

### **2.3. Generalization in Imitation Learning and Policy Distillation** 

To generalize to large environment variations (e.g., object geometry, task semantics) in policy learning, previ- 



<!-- Start of picture text -->
GeoClustering State-based  Vision-based<br>GiGSL Generalist<br>𝑧 Policy Learning Policy Learning Good Enough<br>Specialist Training Cross Model<br>Policy Distillation<br>Pre-trained AutoEncoder  𝓐𝓔 Task  Specialists Generalist  𝐕𝑮𝒇𝒊𝒏𝒂𝒍<br>Assignment Good Enough<br>Point Cloud  𝑷𝒕=𝟎<br>Encoder … Point Cloud  𝑷𝒕<br>𝓔 Generalist  𝐕𝑮𝒊+𝟏<br>Robot Backbone<br>Robot Object Generalist  𝑺𝑮𝟏 State  𝑹𝒕 𝓑<br>State  𝑹𝒕 State  𝑶𝒕 Specialists  {𝑺𝑺𝒊} 𝒇𝒕<br>Specialists  {𝑽𝑺𝒊}<br>Actor Critic Generalist  𝑺𝑮𝒊+𝟏 Actor Critic<br>…<br>action 𝒂𝒕 value  𝒗𝒕 action 𝒂𝒕 value  𝒗𝒕<br>Architecture of  Architecture of  Specialist Training<br>State-based Policy Generalist  𝑺𝑮𝟎 Vision-based Policy<br>𝓔 𝓓<br>Encoder Deoder<br>𝒕=𝟎 Point Cloud  𝑷<br>Task  Policy<br>Assignment Distillation<br>Policy  Task<br>GeoCurriculum Distillation Assignment<br><!-- End of picture text -->

Figure 2: **Method Overview.** We propose to first adopt a state-based policy learning stage followed by a vision-based policy learning stage. The state-based policy takes input robot state _Rt_ , object state _St_ , and the geometric feature _z_ of the scene point cloud of the first frame. We leverage a geometry-aware task curriculum ( **_GeoCurriculum_** ) to learn the first state-based generalist policy. After that, this generalist policy is further improved via iteratively performing specialist fine-tuning and distilling back to the generalist in our proposed geometry-aware iterative generalist-specialist learning ( **_GiGSL_** ), where the task assignment to which specialist is decided by our geometry-aware clustering ( **_GeoClustering_** ). For vision-based policy learning, we first distill the final state-based specialists to an initial vision-based generalist and then do _GiGSL_ for the vision generalist, until we obtain the final vision-based generalist with the highest performance. 

ous works have used imitation learning including behavior cloning [64, 31], augmenting demonstrations to Reinforcement Learning [49, 69, 47, 59, 16] and Inverse Reinforcement Learning [42, 1, 26, 19, 34] to utilize the expert demonstrations or policies. Some works [63, 39, 23, 29] have adopted the _Generalist-Speciliast Learning_ idea in which a group of specialists (teacher) is trained on a subset of the task space, and then distill to a single generalist (student) in the whole task space using the above imitation learning and policy distillation methods. While these works have made great progress on several benchmarks [40, 73, 28, 65, 11], they either do not realize the importance of how to divide the tasks or environment variations for specialists or focus on a different setting to our method. In this work, we leverage the geometry feature of the task in the specialists’ division and curriculum learning which greatly improves the generalizability. 

## **3. Problem Formulation** 

In this work, we focus on learning a universal policy for dexterous object grasping from realistic point cloud observations and proprioceptive information under a table-top setting, similar to [70, 46]. 

We learn such a universal policy from a diverse set of grasping tasks. A grasping task is defined as _τ_ = ( _o, R_ ), where _o ∈_ O is an object instance from the object dataset O, and _R ∈_ **SO(3)** is the initial 3D rotation of the object. To construct the environment, we randomly sample an object _o_ , let it fall from a height, which randomly decides an initial pose, and then move the object center to the center of the table. We always initialize the dexterous hand at a fixed 

pose that is above the table center. The task is successful if the position difference between the object and the target is smaller than a threshold value. This is a multi-task policy learning setting and we require our learned policy to generalize well across diverse grasping tasks, _e.g._ , across random initial poses and thousands of objects including the unseen. 

## **4. Method** 

This section presents a comprehensive description of our proposed method for solving complex tasks. In Sec. 4.1, we provide an overview of our approach along with the training pipeline. Our proposed method leverages DAgger-based distillation and iterative GeneralistSpecialist Learning (iGSL) strategy, which is explained in detail in Sec. 4.2. Moreover, we introduce Geometry-aware Clustering to decide which specialist handles which task, achieving Geometry-aware iterative Generalist-Specialist Learning (GiGSL), which is presented in Sec. 4.3. In Sec. 4.4, we present a Geometry-aware Task Curriculum Learning approach for training the first state-based generalist policy. 

### **4.1. Method Overview** 

Following [70, 8, 7], we can divide our policy learning into two stages: 1) the state-based policy learning stage; 2) the vision-based policy learning stage. It is known that directly learning a vision-based policy is very challenging, we thus first learn a state-based policy that can access oracle information and let this policy help and ease the vision-based policy learning. The full pipeline is shown in Figure 2. **State-based policy learning stage.** The goal of this stage 

is to obtain a universal policy, or we call it a _generalist_ , that takes inputs from robot state _Rt_ , object state _Ot_ , and the scene point cloud _Pt_ =0 at the first frame. Here the object point cloud is fused from multiple depth point clouds captured by multi-view depth cameras. And we include _Pt_ =0 in the input to retain the scene geometry information and we use the encoder of a pre-trained point cloud autoencoder to extract its geometry feature. Note that at this point cloud encoder is frozen to make it as simple as possible, so it doesn’t interfere with policy learning. We leave the visual processing of _Pt_ to the vision-based policy. 

Although learning a state-based policy through reinforcement learning is more manageable than learning a vision-based policy, it is still very challenging to achieve a high success rate under such a diverse multi-task setting. We thus propose a geometry-aware curriculum learning **_(GeoCurriculum)_** to ease the multi-task RL and improve the success rate. 

After this **_GeoCurriculum_** , we obtain the first statebased generalist SG1 that can handle all tasks. We then propose a geometry-aware iterative Generalist-Specialist Learning strategy, dubbed as **_GiGSL_** , to further improve the performance of the generalist. This process involves iterations between learning several state-based specialists _{_ SS _i}_ that specialize in a specific range of tasks and distilling the specialists to a generalist SG _i_ +1, where _i_ denotes the iteration index. The overall performance kept improving through this iterative learning until saturation. 

**Vision-based policy learning.** For vision-based policy, we only allow it to access information available in the real world, including robot state _Rt_ and the scene point clouds _Pt_ . In this stage, we need to jointly learn a vision backbone _B_ that extracts _ft_ from _Pt_ along with our policy (see the blue part of Fig.2). Here we adopt PointNet+Transformer [40] as _B_ , which we find has a larger capacity and thus outperforms PointNet [44]. We randomly initialize the network weight of our first vision generalist VG1. We start with performing a cross-modal distillation that distills the latest state-based specialists _{_ SS _n}_ to VG1. We can then start the _GiGSL_ cycles for vision-based policies that iterate between finetuning _{_ VS _i}_ and distilling to VG _i_ +1 until the performance of the vision-based generalist saturates. The final vision-based generalist VGfinalis our learned universal grasping policy that yields the highest performance. Please refer to supplementary material for the pseudo-code of the whole pipeline. 

### **4.2.** **_iGSL_ : iterative Generalist-Specialist Learning** 

**Recap Generalist-Specialist Learning (** **_GSL)_** . The idea of Generalist-Specialist Learning comes from a series of works [63, 39, 23, 29] that deal with multi-task policy learning. The most recent paper [29] proposes _GSL_ , a method that splits the whole task space into multiple subspaces and lets one specialist take charge of one subspace. Since each 

subspace has fewer task variations and thus is easier to learn, each specialist can be trained well and perform well on their task distributions. Finally, all the specialists will be distilled into one generalist. 

Note that [29] only has one cycle of specialist learning and generalist learning. Straightforwardly, more cycles may be helpful. In _GSL_ , the distillation is implemented using GAIL [26] or DAPG [49] but we find their performance mediocre. In this work, we propose a better policy distillation method based on DAgger, iteratively enabling Generalist-Specialist Learning. 

**Dagger-based policy distillation** . DAgger [51] is an onpolicy imitation learning algorithm. Different from GAIL or DAPG, which only require expert demonstrations, DAgger [51] requires an expert policy, which is called a teacher, and the student that takes charge of interacting with the environment. When the student takes action, the teacher policy will use its action to serve as supervision to improve the student. Given that the student always uses its policy to interact with the environment, such imitation is on-policy and thus doesn’t suffer from the covariate shift problem usually seen in the behavior cloning algorithm. Previous works, such as [70] for dexterous grasping and [8, 7] for in-hand manipulation, have used DAgger for policy distillation from a state-based teacher to a vision-based student and it is shown in UniDexGrasp [70] that DAgger outperforms GAIL and DAPG for policy distillation. 

However, one limitation of DAgger is that it only cares about the policy network and discards the value networks that popular actor-critic RL like PPO [55] and SAC [25] usually have. In this case, when a teacher comes with both an actor and a critic distills to a student, the student will only have an actor without a critic and thus can’t be further finetuned using actor-critic RL. This limits _GSL_ to simply one cycle and hinders it from further improving the generalist. 

To mitigate this issue, we propose a new distillation method that jointly learns a critic function while learning the actor using DAgger. Our DAgger-based distillation learns both a policy and a critic function during the supervised policy distillation process, where the policy loss is the mean squared error (MSE) between the actions from the teacher policy _πteacher_ and the student policy _πθ_ (same in DAgger), and the critic loss is the MSE between the predicted value function _Vφ_ and the estimated returns _R_<sup>ˆ</sup> _t_ using Generalized Advantage Estimation (GAE) [54]. 



This DAgger-based distillation method allows us to retain both the actor and critic while achieving very high performance. Compared to ILAD [69] that only pre-trains the 

actor and directly finetunes the actor-critic RL (the critic network is trained from scratch), our method enables actorcritic RL to fine-tune on both trained actor and critic networks, enhancing the stability and effectiveness of RL training. 

**Iteration between specialist fine-tuning and generalist distillation** . With our proposed DAgger-based distillation method, we can do the following: 1) start with our first generalist learned through _GeoCurriculum_ ; 2) clone the generalist to several specialists, finetune each specialist on their own task distribution; 3) using DAgger-based distillation method to distill all specialists to one generalist; we can iterate between 2) and 3) until the performance saturates. 

### **4.3.** **_GiGSL_ : Geometry-aware iterative Generalist-** 

### **Specialist Learning** 

One important question left for _iGSL_ is how to partition the task space. In [29], they are dealing with a limited amount of tasks and it is possible for them to assign one specialist to one task or randomly. However, in our work, we are dealing with an infinite number of tasks considering the initial object pose can change continuously. We can only afford a finite number of specialists and need to find a way to assign a sampled task to a specialist. We argue that similar tasks need to be assigned to the same specialist since one specialist will improve effectively via reinforcement learning only if its task variation is small. To this end, we propose **_GeoClustering_** , a strategy for geometry-aware clustering in the task space. 

**_GeoClustering_ strategy** . We split the task space T = O _×_ **SO(3)** into _N_ clu clusters, with tasks in each cluster _Cj_ being handled by a designated specialist _Sj_ during specialist fine-tuning. We begin by sampling a large number of tasks _{τ_<sup>(</sup><sup>_k_)</sup> _}_<sup>_N_</sup> _k_ =1<sup>sample</sup> from T ( _N_ sample _≈_ 270 _,_ 000 in our implementation) and clustering their visual features using K-Means. The clustering of the large-scale task samples provides an approximation of the clustering of the whole continuous task space. We first train a point cloud 3D autoencoder using the point cloud _{Pt_<sup>(</sup> =0<sup>_k_)</sup><sup>_}N_</sup> _k_ =1<sup>sample</sup> of the initialized objects in the sample tasks _{τ_<sup>(</sup><sup>_k_)</sup> _}_<sup>_N_</sup> _k_ =1<sup>sample</sup> . The autoencoder follows an encoder-decoder structure. The encoder _E_ encodes _Pt_<sup>(</sup> =0<sup>_k_)</sup> and outputs the encoding latent feature _z_<sup>(</sup><sup>_k_)</sup> = _E_ ( _Pt_<sup>(</sup> =0<sup>_k_)).</sup> The decoder _D_ takes _z_<sup>(</sup><sup>_k_)</sup> as input and generates the point cloud _P_<sup>ˆ</sup> _t_<sup>(</sup> =0<sup>_k_).Themodelistrainedusingthereconstruction</sup> loss _L_ AE, which is the Chamfer Distance between _Pt_<sup>(</sup> =0<sup>_k_)and</sup> _P_ ˆ _t_<sup>(</sup> =0<sup>_k_).See Supplementary Materials for more details.</sup> 

During clustering for the state-based specialists, we use the pre-trained encoder _E_ to encode the object point cloud _Pt_<sup>(</sup> =0<sup>_k_)foratask</sup><sup>_τ_(</sup><sup>_k_)andobtainthelatentcode</sup><sup>_z_(</sup><sup>_k_).We</sup> use this geometry and pose encoded latent code _z_<sup>(</sup><sup>_k_)</sup> as the feature for clustering. We then use K-Means to cluster the features of these sampled tasks _{z_<sup>(</sup><sup>_k_)</sup> _}_<sup>_N_</sup> _k_ =1<sup>sample</sup> and generate 

|**Algorithm 1****_GeoClustering_**|
|---|
|**Require:** Task SpaceT, Encoder_E_ from the pre-trained AutoEn-<br>coder or backbone_B_from the Vision Policy. Number of target<br>clusters_N_clu<br>1: Sample_N_sample tasks_{τ_ <sup>(</sup><sup>_k_)</sup>_}_<br>_N_sample<br>_j_=1<br>fromT<br>|
|2: Get features:<br>state-based: _{z_<sup>(</sup><sup>_k_)</sup>_}_<br>_N_sample<br>_k_=1<br>_←{E_(_P_ <sup>(</sup><sup>_k_)</sup><br>_t_=0<sup>)</sup><sup>_}_</sup><br>_N_sample<br>_k_=1<br>vision-based: _{f_ <sup>(</sup><sup>_k_)</sup>_}_<br>_N_sample<br>_k_=1<br>_←{B_(_P_ <sup>(</sup><sup>_k_)</sup><br>_t_=0<sup>)</sup><sup>_}_</sup><br>_N_sample<br>_k_=1|
|3: Get cluster centers using K-Means:<br>state-based: _{cj}_<sup>_N_clu</sup><br>_j_=1 <sup>_←_K-Means(</sup><sup>_{z_(</sup><sup>_k_)</sup><sup>_}_)</sup><br>vision-based: _{cj}_<sup>_N_clu</sup><br>_j_=1 <sup>_←_K-Means(</sup><sup>_{f_ (</sup><sup>_k_)</sup><sup>_}_)</sup><br>|
|4: **return**Cluster centers_{cj}_<sup>_N_clu</sup><br>_j_=1|



_N_ clu clusters and corresponding cluster centers _{cj}_<sup>_N_</sup> _j_ =1<sup>clu:</sup> And for vision-based specialists, thanks to the trained vision backbone, we directly use it to generate feature _f_<sup>(</sup><sup>_k_)</sup> to replace the corresponding encoding feature _z_<sup>(</sup><sup>_k_)</sup> in the state-based setting. Finally, the clustering for specialists can be formulated as: 

During the specialists fine-tuning, we assign a given task _τ_<sup>(</sup><sup>_k_)</sup> to the specialist in an online fashion to handle the infinite task space. During fine-tuning, we assign _τ_<sup>(</sup><sup>_k_)</sup> to _SSj_ or _V Sj_ if the Specialist have the nearest center _cj_ to the feature _z_<sup>(</sup><sup>_k_)</sup> . or _f_<sup>(</sup><sup>_k_)</sup> . Then each Specialist only needs to train on the assigned task set and distill their learned specific knowledge to the Generalist. 

**Summary and Discussion.** **_GeoClustering_** strategy resolves the problem of task space partition, allows one specialist to focus on concentrated task distribution, and thus facilitates the performance gain for each specialist. Please refer to Algorithm 3 for the pseudo-code of _GeoClustering_ . 

As a way to partition task space, our geometry-aware clustering is much more reasonable and effective than category label-based partition, based on the following reasons: 1) not every object instance has a category label; 2) considering the large intra-category geometry variations, not necessarily objects that belong to the same category would be taken care by the same specialist; 3) object pose can also affect grasping, which is completely ignored in category label based partition but is well captured by our method. 

### **4.4.** **_GeoCurriculum_ : Geometry-aware Task Curriculum Learning** 

**Problems of** **_GiGSL_ from Scratch** For state-based policy learning, we in theory can start _GiGSL_ from scratch. One straightforward way is to directly learn a generalist from scratch on the whole task space and then improve it following G-S-G-S-... steps. However, learning this first generalist directly on the whole task space using reinforcement learning would be very challenging, usually yielding a generalist with an unsatisfactory success rate. 

An alternative would be to first learn _N_ clu specialist, distill to a generalist, and then follow S-G-S-G-... steps. How- 

**Algorithm 2** **_GeoCurriculum_ Require:** Task Space T, _N_ train tasks for training _{τ_<sup>(</sup><sup>_k_)</sup> _}_<sup>_N_</sup> _k_ =1<sup>train</sup> _⊂_ T, _N_ level hierarchical levels of curriculum learning and _N_ sub sub-clusters for each level, Encoder _E_ from the pre-trained AutoEncoder 1: Get features from the encoder: _{z_<sup>(</sup><sup>_k_)</sup> _}_<sup>_N_</sup> _k_ =1<sup>train</sup> 2: **Level** 0: Find the center of the feature space _zc ←_ **_GeoClustering_** ( _N_ clu = 1) and the task _τc_ with features nearest to _zc_ , train _C_ 0 = _{τc}_ (where _∥C_ 0 _∥_ = 1). 3: **for** Level _l_ in 1 _, . . . , N_ level _−_ 1, **do** 4: **Level** _l_ : Split each cluster of the Level _l −_ 1 into _N_ sub sub-clusters. Find the _N_ sub tasks with features nearest to each sub-cluster feature center and add these tasks to _Cl_ , train _Cl_ (where _∥Cl∥_ = _N_ sub<sup>_l_).</sup> 5: **end for** 6: **Level** _N_ **level** : train _CN_ level = _{τ_<sup>(</sup><sup>_k_)</sup> _}_<sup>_N_</sup> _k_ =1<sup>train(where</sup><sup>_∥CN_</sup> level<sup>_∥_=</sup> _N_ train) 7: **return** _<u>{Cl}</u>_<sup>_N_</sup> _<u>l</u>_ =<sup>level</sup> <u>0</u> 

ever, this is still very suboptimal. Given the huge variations in our task space, we need _N_ clu _>>_ 1 so that the task variations in each specialist are small enough to allow them effectively learn. This large number of specialists would be very costly for training. Furthermore, because each specialist is trained separately from scratch, their policy can be substantially different from each other, which may lead to new problems. Considering two tasks that are similar but assigned to different specialists (they are just around the boundary of the task subspace). Then, since the two specialists are trained independently, there is no guarantee that the specialists will do similar things to these two similar tasks, which means the policy is discontinuous around the subspace boundary. During policy distillation, a generalist may get significantly different action supervision from different specialists for those “boundary tasks”. As a result, this discontinuity in policy may lead to difficulty in convergence and hurt the policy generalization toward unseen tasks. 

**Recap Object Curriculum in UniDexGrasp** Following UniDexGrasp [70], we consider leveraging curriculum learning to make the first generalist learning easier. [70] introduced an object curriculum: they start with training a policy using RL to grasp one object instance (this object may be in the different initial poses); once this policy is well trained, they increase the number of objects by incorporating several similar objects from the same category and then finetuning the policy using RL on the new collection of objects; then, they increase the number of objects again by taking all objects from the category and finetune the policy; finally, they expand the object range to all different kinds of categories in the whole training objects and finish the final fine-tuning. [70] shows that object curriculum is crucial to their performance, improving the success rate of their statebased policy from 31% to 74% on training set. 

|Model|Train(%)|Test<br>Uns. Obj.<br>Seen Cat.|(%)<br>Uns. Cat.|
|---|---|---|---|
|PPO[55]|24.3|20.9|17.2|
|DAPG[49]|20.8|15.3|11.1|
|ILAD[69]|31.9|26.4|23.1|
|GSL[29]|57.3|54.1|50.9|
|UniDexGrasp[70]|79.4|74.3|70.8|
|Ours(state-based)|**87.9**|**84.3**|**83.1**|
|PPO[55]+DAgger[51]|20.6|17.2|15.0|
|DAPG[49]+DAgger|17.9|15.2|13.9|
|ILAD[69]+DAgger|27.6|23.2|20.0|
|GSL[29]+DAgger|54.1|50.2|44.8|
|UniDexGrasp[70]|73.7|68.6|65.1|
|Ours (state)+DAgger|77.4|72.6|68.8|
|Ours (vision-based)|**85.4**|**79.6**|**76.7**|
|Table 1: **The Average S**<br>**jects on Both Training**<br>use green for the state-b<br>based policy.|**uccess Rate**<br>**and Test Se**<br>ased policy|**of the Eval**<br>**t**. For better<br>and blue for|**uated Ob-**<br>clarity, we<br>the vision-|



**_GeoCurriculum._** One fundamental limitation in the object curriculum used in [70] is unawareness of object pose and reliance on category labels. Similar to our argument in the discussion of Sec.4.3, we propose to leverage geometric features to measure the similarity between tasks, rather than object identity and category label. We thus introduce _GeoCurriculum_ , a geometry-aware task curriculum that leverages hierarchical task space partition. 

In detail, we design a _N_ level task curriculum that assigns tasks with increasing level of variations to policy learning and facilitate a step by step learning. As shown in Algorithm 2, we first find a task _τ_<sup>(</sup><sup>_kc_)</sup> with the feature nearest to the feature center of all sampled tasks and train the policy (Level 0). Then iteratively, for level _l_ , we split each cluster in the previous level _l −_ 1 into _N_ sub sub-clusters (30 in our implementation) based on geometry feature _z_<sup>(</sup><sup>_k_)</sup> and find _N_ sub corresponding centers. We then add tasks that have features nearest to these sub-centers to the currently assigned tasks _Ci−_ 1. Finally, we get the hierarchical task groups for the curriculum, that is: 



During training, we iteratively train the policy under each assigned task set. From tackling only one task in _C_ 0 to all the training tasks in _CN_ level , the policy grows up step by step and have better performance than directly training it under all tasks. 

## **5. Experiment** 

### **5.1. Experiment Setting** 

We evaluate the effectiveness of our method in the challenging dexterous grasping benchmark UniDexGrasp [70] which is a recently proposed benchmark suite designated for learning generalizable dexterous grasping. 



<!-- Start of picture text -->
Category<br>Clustering<br>𝒞!: Bottle 𝒞": Camera 𝒞#: Jar<br>State-based<br>Clustering<br>(Ours)<br>𝒞! 𝒞" 𝒞#<br>Vision-based<br>Clustering<br>(Ours)<br>𝒞! 𝒞" 𝒞#<br><!-- End of picture text -->

Figure 3: **Comparison between Category-label-based Clustering and our Geometry-aware Clustering.** Our state-based clustering is based on the features of the firstframe point clouds from the pre-trained encoder, while the vision-based policy utilizes its vision backbone to extract features for clustering. Due to the vision-based clustering being task-aware, we also show the grasping poses of the dexterous hands in the third row. 

UniDexGarsp contains 3165 different object instances spanning 133 categories. Since the ground-truth grasp pose generation for pretraining and point cloud rendering processes are very expensive for UniDexGrasp environments, we only consider the non-goal conditioned setting in UniDexGarsp which does not specify the grasping hand pose. Each environment is randomly initialized with one object and its initial pose, and the environment consists of a panoramic 3D point cloud _Pt_ captured from the fixed cameras for vision-based policy learning. 

For the network architecture, we use MLP with 4 hidden layers (1024,1024,512,512) for the policy network and value network in the state-based setting, and an additional PointNet+Transformer [40] to encode the 3D scene point cloud input in the vision-based setting. We freeze the vision backbone during the vision-based specialist training. We use _K_ = _Nclu_ = 20 in our experiments. Other detailed hyperparameters are shown in supplementary materials. 

### **5.2. Main Results** 

We first train our method in the state-based policy learning setting and compare it with several baselines (green part in Tab.1). We use PPO [55] for the specialist RL in our pipeline. For these baselines: PPO [55] is a popular RL method, DAPG [50], and ILAD [69] are imitation learning methods that further leverage expert demonstrations with RL; GSL [29] adopts the idea of generalist-specialist learning which use PPO for specialist learning and integrates demonstrations for generalist learning using DAPG, but with a random division for each specialist and only performs policy distillation once. UniDexGrasp [70] uses PPO and category-based object curriculum learning. To compare our method to these baselines, we distill our final statebased specialists _{_ SS _n}_ to a state-based generalist SG _n_ +1 



<!-- Start of picture text -->
𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝑹𝒂𝒕𝒆(%)<br>𝟗𝟐 92<br>𝟖𝟗. 𝟗 𝟗𝟎. 𝟑<br>𝟗𝟎 90<br>𝟖𝟖 88 𝟖𝟔. 𝟖 𝟖𝟔. 𝟓 𝟖𝟔. 𝟕<br>𝟖𝟔 86 𝟖𝟕. 𝟗 𝟖𝟓. 𝟒<br>𝟖𝟒 84 𝟖𝟐. 𝟕 𝟖𝟒. 𝟖 𝟖𝟓. 𝟏<br>𝟖𝟐 82<br>𝟖𝟐. 𝟏<br>𝟖𝟎 80<br>𝟎 .0<br>𝟎 78<br>𝑺𝑮 SG0 𝟎 𝑺𝑮 SG1 𝟏 𝑺𝑺 SS1 𝟏 𝑺𝑮 SG2 𝟐 𝑺𝑺 SS2 𝟐 𝑺𝑮 SG3 𝟑 𝑺𝑺 SS3 𝟑 𝑽𝑮 VG1 𝟏 𝑽𝑺 VS1 𝟏 𝑽𝑮 VG2 𝟐 𝑽𝑺 VS2 𝟐 𝑽𝑮 VG3 𝟑<br><!-- End of picture text -->

Figure 4: **Success Rate during our** **_GiGSL_ Training.** We plot the success rate of each training step, where green represents the state-based policy, blue represents the visionbased policy, hollow points represent the specialist policy, and solid points represent the generalist policy. 

(although we won’t use the latter later). With our proposed techniques, our method achieves a success rate of 88% and 84% on the train and test set, which is **9%** and **11%** improvement over the UniDexGrasp in the state-based setting. 

We then compare our method in the vision-based policy learning setting with the baseline methods(blue part in Tab.1). For PPO [55], DAPG [50], ILAD [69] and GSL [29], we distill the state-based policy to the visionbased policy using DAgger [51] since they don’t consider the observation space change (state to vision) and directly training these methods under a vision input leads to completely fail. For our method, we compare our proposed whole pipeline “Ours (vision-based)” with the variant of directly distilling our state-based policy to vision-based policy using DAgger, namely “Ours (state)+DAgger”. Our final results in the vision-based setting reach 85% and 78% on the train set and test set which outperforms the SOTA baseline UniDexGrasp for **12%** and **11%** , respectively. 

### **5.3. Analysis of the Training Process** 

**Geometry-aware Clustering Helps the Policy Learning.** We visualize some qualitative result in Fig.3. The first row shows a simple way of clustering, which is based on the object category. But as we analyzed above, this clustering method has no object geometry information and thus has limited help in grasping learning. The second row shows our stated-based clustering strategy, which is based on the features from the point cloud encoder _E_ and can cluster objects with similar shapes. And furthermore, in the third row, our vision-based clustering strategy utilizes the vision backbone which has more task-relative information, and thus the clustered objects have similar shapes as well as similar grasping poses. 

**Quatitative Performance Improvement of our** **_GiGSL_** . We visualize the success rate of each learning or finetuning step in Fig.4. No matter whether for state-based or vision-based policy, the improvement of GeneralistSpecialist fine-tuning and distillation shows the effective- 

|||||Tech|niques|||Suc|cess Rate|(%)|
|---|---|---|---|---|---|---|---|---|---|---|
|||Geo-Aware<br>Curri.|Iterative<br>Fine-tuningS|Geo-Aware<br>Clustering|Iterative<br>Fine-tuningV|End2End<br>Distillation|Transformer<br>Backbone|Training<br>|Test<br>Uns. Obj.|Test<br>Uns. Cat.|
||1|||||||79.4|74.3|70.8|
|State|2|✓||||||82.7|76.8|74.2|
|-based|3|✓|✓|||||84.0|77.9|74.8|
||4|✓|✓|✓||||**87.9**|**84.3**|**83.1**|
||5|✓|✓|||||77.4|72.6|68.8|
||6|✓|✓|||✓||78.0|72.1|69.1|
||7|✓|✓||✓|✓||78.9|74.7|70.2|
|Vision|8|✓|✓|✓|✓|✓||82.1|77.1|71.9|
|-based|9|✓|✓|✓|✓||✓|82.7|76.2|73.4|
||10|✓|✓|✓||✓|✓|82.5|76.1|72.0|
||11|✓|✓||✓|✓|✓|78.6|73.7|72.3|
||12|✓|✓|✓|✓|✓|✓|**85.4**|**79.6**|**76.7**|



Table 2: **Ablation Study.** For state-based policy (green) and vision-based policy learning (blue), we compare our techniques with various ablations. 

||PPO[55]|GSL[29]|Ours|
|---|---|---|---|
|MT-10(%)|58.4±10.1|77.5±2.9|**80.3±0.5**|



#### Table 3: **Addtional Experiment in Meta-World.** 

ness of our Geometry-aware iterative Generalist-Specialist Learning **_GiGSL_** strategy design and boosts the final performance of Universal Dexterous Grasping. 

### **5.4. Ablation Study** 

The ablation studies are shown in Tab.2. For **state-based policy learning stage** (green part), we analyze the ablation results as follows. 

1) (Row 1,2) Effective of _GeoCurriculum_ . Using our proposed _GeoCurriculum_ (Row 2) performs better than using object-curriculum-learning in [70] (Row 1). 

2) (Row 2,3) Effective of iterative fine-tuningS. The policy can benefit from the iterative fine-tuning process and reach a higher success rate on both training and test set (Row 3) than a single cycle (Row 2). Also see Figure 4. 

3) (Row 3,4) Effective of _GeoClustering_ in the statebased setting. With the pre-trained visual feature, the tasks assigned to one specialist are around the same feature clusters and thus are similar to each other. This significantly reduces the difficulty of policy learning and, in return, improves performance (Row 4), compared to randomly assigning tasks to the specialists (Row 3). 

For the ablation studies of **vision-based policy learning stage** (blue part), we use _GeoClustering_ in the state-based policy training by default, and the checkmark of _GeoClustering_ in this part indicates whether we use it in the visionbased policy learning. We use PointNet [44] if there’s no checkmark in “Transformer Backbone”. 

4) (Row 5,6 & 9,12) Effective of end-to-end distillation. We find directly distilling the final state-based specialists _{_ SS _n}_ to the vision-based generalist VG1 (Row 6, 12) performs better than first distilling the state-based specialists 

_{_ SS _n}_ to the state-based generalist SG _n_ +1, then distilling this generalist to vision-based generalist VG1 (Row 5, 9). 

5) (Row 6,7 & 10,12) Effective of iterative fine-tuningV. The policy can benefit from the iterative fine-tuning process and reach a higher success rate on both training and test set than the single stage. Also see Figure 4. 

6) (Row 7,8 & 11,12) Effective of _GeoClustering_ in the vision-based setting. By dividing the specialists using the learned visual feature from the vision backbone of the generalist, the final performance can be significantly improved than randomly dividing the specialists ( **7%** and **5%** on training and test set, comparing Row 11 and 12). 

7) (Row 8,12) Effective of the Transformer backbone. The results show that the PointNet+Transformer backbone [40] (Row 13) has a better expressive capacity which can improve the performance of DAgger-based distillation than using the PointNet [44] backbone (Row 8). 

### **5.5. Addtional Experiment in Meta-World** 

To further demonstrate the effectiveness of our proposed training strategy, we conduct more experiments in metaworld benchmark [73], which focus more on state-based multi-task learning. We use our **_iGSL_** method to handle the MT10 tasks and the results in Tab.3 show that our method outperforms the previous SOTA methods and demonstrates the advantages of our training strategy design, which enables iterative distillation and fine-tuning. More details and results can be found in the Supplementary Materials. 

## **6. Conclusions and Discussions** 

In this paper, we propose a novel pipeline, UniDexGrasp++, that significantly improves the performance and generalization of UniDexGrasp. We believe such generalizability is also essential for Sim2Real transfer for real robot dexterous grasping. The limitation is that we only tackle the dexterous grasping task in simulation and we will conduct the real-robot extension in our future work. 

## **References** 

- [1] Pieter Abbeel and Andrew Y Ng. Apprenticeship learning via inverse reinforcement learning. In _Proceedings of the twenty-first international conference on Machine learning_ , page 1, 2004. 3 

- [2] Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias Plappert, Glenn Powell, Raphael Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 2 

- [3] Sheldon Andrews and Paul G Kry. Goal directed multi-finger manipulation: Control policies and analysis. _Computers & Graphics_ , 37(7):830–839, 2013. 2 

- [4] OpenAI: Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 39(1):3–20, 2020. 2 

- [5] Yunfei Bai and C. Karen Liu. Dexterous manipulation using both palm and fingers. In _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 1560–1565, 2014. 2 

- [6] Michel Breyer, Jen Jen Chung, Lionel Ott, Roland Siegwart, and Juan Nieto. Volumetric grasping network: Realtime 6 dof grasp detection in clutter. _arXiv preprint arXiv:2101.01132_ , 2021. 1 

- [7] Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Edward Adelson, and Pulkit Agrawal. Visual dexterity: Inhand dexterous manipulation from depth. _arXiv preprint arXiv:2211.11744_ , 2022. 2, 3, 4 

- [8] Tao Chen, Jie Xu, and Pulkit Agrawal. A system for general in-hand object re-orientation. _Conference on Robot Learning_ , 2021. 2, 3, 4 

- [9] Sammy Christen, Muhammed Kocabas, Emre Aksan, Jemin Hwangbo, Jie Song, and Otmar Hilliges. D-grasp: Physically plausible dynamic grasp synthesis for hand-object interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2022. 2 

- [10] Djork-Arn´e Clevert, Thomas Unterthiner, and Sepp Hochreiter. Fast and accurate deep network learning by exponential linear units (elus). _arXiv preprint arXiv:1511.07289_ , 2015. 13 

- [11] Karl Cobbe, Chris Hesse, Jacob Hilton, and John Schulman. Leveraging procedural generation to benchmark reinforcement learning. In _International conference on machine learning_ , pages 2048–2056. PMLR, 2020. 3 

- [12] Nikhil Chavan Dafle, Alberto Rodriguez, Robert Paolini, Bowei Tang, Siddhartha S Srinivasa, Michael Erdmann, Matthew T Mason, Ivan Lundberg, Harald Staab, and Thomas Fuhlbrigge. Extrinsic dexterity: In-hand manipulation with external forces. In _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 1578– 1585. IEEE, 2014. 2 

- [13] Qiyu Dai, Yan Zhu, Yiran Geng, Ciyu Ruan, Jiazhao Zhang, and He Wang. Graspnerf: Multiview-based 6-dof grasp detection for transparent and specular objects using generalizable nerf. _arXiv preprint arXiv:2210.06575_ , 2022. 1 

- [14] Mehmet R Dogar and Siddhartha S Srinivasa. Push-grasping with dexterous hands: Mechanics and a method. In _2010 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 2123–2130. IEEE, 2010. 2 

- [15] Mehmet R. Dogar and Siddhartha S. Srinivasa. Pushgrasping with dexterous hands: Mechanics and a method. In _2010 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 2123–2130, 2010. 2 

- [16] Yan Duan, Xi Chen, Rein Houthooft, John Schulman, and Pieter Abbeel. Benchmarking deep reinforcement learning for continuous control. In _International conference on machine learning_ , pages 1329–1338. PMLR, 2016. 3 

- [17] Hongjie Fang, Hao-Shu Fang, Sheng Xu, and Cewu Lu. Transcg: A large-scale real-world dataset for transparent object depth completion and a grasping baseline. _IEEE Robotics and Automation Letters_ , pages 1–8, 2022. 1 

- [18] Hao-Shu Fang, Chenxi Wang, Minghao Gou, and Cewu Lu. Graspnet-1billion: A large-scale benchmark for general object grasping. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 11444– 11453, 2020. 1 

- [19] Justin Fu, Katie Luo, and Sergey Levine. Learning robust rewards with adversarial inverse reinforcement learning. _arXiv preprint arXiv:1710.11248_ , 2017. 3 

- [20] Haoran Geng, Ziming Li, Yiran Geng, Jiayi Chen, Hao Dong, and He Wang. Partmanip: Learning cross-category generalizable part manipulation policy from point cloud observations, 2023. 2 

- [21] Haoran Geng, Helin Xu, Chengyang Zhao, Chao Xu, Li Yi, Siyuan Huang, and He Wang. Gapartnet: Crosscategory domain-generalizable object perception and manipulation via generalizable and actionable parts. _arXiv preprint arXiv:2211.05272_ , 2022. 2 

- [22] Yiran Geng, Boshi An, Haoran Geng, Yuanpei Chen, Yaodong Yang, and Hao Dong. End-to-end affordance learning for robotic manipulation. _arXiv preprint arXiv:2209.12941_ , 2022. 2 

- [23] Dibya Ghosh, Avi Singh, Aravind Rajeswaran, Vikash Kumar, and Sergey Levine. Divide-and-conquer reinforcement learning. _arXiv preprint arXiv:1711.09874_ , 2017. 2, 3, 4 

- [24] Minghao Gou, Hao-Shu Fang, Zhanda Zhu, Sheng Xu, Chenxi Wang, and Cewu Lu. Rgb matters: Learning 7-dof grasp poses on monocular rgbd images. In _2021 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 13459–13466. IEEE, 2021. 1 

- [25] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In _International conference on machine learning_ , pages 1861–1870. PMLR, 2018. 4 

- [26] Jonathan Ho and Stefano Ermon. Generative adversarial imitation learning. _Advances in neural information processing systems_ , 29, 2016. 3, 4, 14, 15 

- [27] Wenlong Huang, Igor Mordatch, Pieter Abbeel, and Deepak Pathak. Generalization in dexterous manipulation via geometry-aware multi-task learning. _arXiv preprint arXiv:2111.03062_ , 2021. 2 

- [28] Stephen James, Zicong Ma, David Rovick Arrojo, and Andrew J Davison. Rlbench: The robot learning benchmark & learning environment. _IEEE Robotics and Automation Letters_ , 5(2):3019–3026, 2020. 3 

- [29] Zhiwei Jia, Xuanlin Li, Zhan Ling, Shuang Liu, Yiran Wu, and Hao Su. Improving policy optimization with generalistspecialist learning. In _International Conference on Machine Learning_ , pages 10104–10119. PMLR, 2022. 2, 3, 4, 5, 6, 7, 8, 12, 15 

- [30] Dmitry Kalashnikov, Alex Irpan, Peter Pastor, Julian Ibarz, Alexander Herzog, Eric Jang, Deirdre Quillen, Ethan Holly, Mrinal Kalakrishnan, Vincent Vanhoucke, et al. Scalable deep reinforcement learning for vision-based robotic manipulation. In _Conference on Robot Learning_ , pages 651–673. PMLR, 2018. 2 

- [31] Michael Kelly, Chelsea Sidrane, Katherine DriggsCampbell, and Mykel J Kochenderfer. Hg-dagger: Interactive imitation learning with human experts. In _2019 International Conference on Robotics and Automation (ICRA)_ , pages 8077–8083. IEEE, 2019. 3 

- [32] Vikash Kumar, Abhishek Gupta, Emanuel Todorov, and Sergey Levine. Learning dexterous manipulation policies from experience and imitation. _arXiv preprint arXiv:1611.05095_ , 2016. 2 

- [33] Vikash Kumar, Emanuel Todorov, and Sergey Levine. Optimal control with learned local models: Application to dexterous manipulation. In _2016 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 378–383. IEEE, 2016. 2 

- [34] Fangchen Liu, Zhan Ling, Tongzhou Mu, and Hao Su. State alignment-based imitation learning. _arXiv preprint arXiv:1911.10947_ , 2019. 3 

- [35] Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, and Li Yi. Hoi4d: A 4d egocentric dataset for category-level humanobject interaction. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21013–21022, 2022. 2 

- [36] Qingkai Lu, Kautilya Chenna, Balakumar Sundaralingam, and Tucker Hermans. Planning multi-fingered grasps as probabilistic inference in a learned deep network. In _Robotics Research: The 18th International Symposium ISRR_ , pages 455–472. Springer, 2020. 2 

- [37] Priyanka Mandikal and Kristen Grauman. Dexvip: Learning dexterous grasping with human hand pose priors from video. In _Conference on Robot Learning (CoRL)_ , 2021. 2 

- [38] Priyanka Mandikal and Kristen Grauman. Learning dexterous grasping with object-centric visual affordances. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2021. 2 

- [39] Tongzhou Mu, Jiayuan Gu, Zhiwei Jia, Hao Tang, and Hao Su. Refactoring policy for compositional generalizability using self-supervised object proposals. _Advances in Neural Information Processing Systems_ , 33:8883–8894, 2020. 2, 3, 4 

- [40] Tongzhou Mu, Zhan Ling, Fanbo Xiang, Derek Yang, Xuanlin Li, Stone Tao, Zhiao Huang, Zhiwei Jia, and Hao 

   - Su. Maniskill: Generalizable manipulation skill benchmark with large-scale demonstrations. _arXiv preprint arXiv:2107.14483_ , 2021. 2, 3, 4, 7, 8, 14 

- [41] Anusha Nagabandi, Kurt Konolige, Sergey Levine, and Vikash Kumar. Deep dynamics models for learning dexterous manipulation. In _Conference on Robot Learning_ , pages 1101–1112. PMLR, 2020. 2 

- [42] Andrew Y Ng, Stuart Russell, et al. Algorithms for inverse reinforcement learning. In _Icml_ , volume 1, page 2, 2000. 3 

- [43] Allison M Okamura, Niels Smaby, and Mark R Cutkosky. An overview of dexterous manipulation. In _Proceedings 2000 ICRA. Millennium Conference. IEEE International Conference on Robotics and Automation. Symposia Proceedings (Cat. No. 00CH37065)_ , volume 1, pages 255–262. IEEE, 2000. 2 

- [44] Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas. Pointnet: Deep learning on point sets for 3d classification and segmentation. _arXiv preprint arXiv:1612.00593_ , 2016. 4, 8, 14 

- [45] Haozhi Qi, Ashish Kumar, Roberto Calandra, Yi Ma, and Jitendra Malik. In-hand object rotation via rapid motor adaptation. _arXiv preprint arXiv:2210.04887_ , 2022. 2 

- [46] Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, and Xiaolong Wang. Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. _arXiv preprint arXiv:2211.09423_ , 2022. 2, 3 

- [47] Ilija Radosavovic, Xiaolong Wang, Lerrel Pinto, and Jitendra Malik. State-only imitation learning for dexterous manipulation. In _2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 7865–7871. IEEE, 2021. 3 

- [48] Ilija Radosavovic, Tete Xiao, Stephen James, Pieter Abbeel, Jitendra Malik, and Trevor Darrell. Real-world robot learning with masked visual pre-training. _arXiv preprint arXiv:2210.03109_ , 2022. 2 

- [49] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 2, 3, 4, 6, 12 

- [50] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 7 

- [51] St´ephane Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured prediction to noregret online learning. In _Proceedings of the fourteenth international conference on artificial intelligence and statistics_ , pages 627–635. JMLR Workshop and Conference Proceedings, 2011. 2, 4, 6, 7, 12 

- [52] Daniela Rus. In-hand dexterous manipulation of piecewisesmooth 3-d objects. _The International Journal of Robotics Research_ , 18(4):355–381, 1999. 2 

- [53] J Kenneth Salisbury and John J Craig. Articulated hands: Force control and kinematic issues. _The International journal of Robotics research_ , 1(1):4–17, 1982. 2 

- [54] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. _arXiv preprint arXiv:1506.02438_ , 2015. 4 

- [55] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 4, 6, 7, 8, 12, 15 

- [56] Younggyo Seo, Danijar Hafner, Hao Liu, Fangchen Liu, Stephen James, Kimin Lee, and Pieter Abbeel. Masked world models for visual control. _arXiv preprint arXiv:2206.14244_ , 2022. 2 

- [57] Younggyo Seo, Kimin Lee, Stephen L James, and Pieter Abbeel. Reinforcement learning with action-free pretraining from videos. In _International Conference on Machine Learning_ , pages 19561–19579. PMLR, 2022. 2 

- [58] Qijin She, Ruizhen Hu, Juzhan Xu, Min Liu, Kai Xu, and Hui Huang. Learning high-dof reaching-and-grasping via dynamic representation of gripper-object interaction. _arXiv preprint arXiv:2204.13998_ , 2022. 2 

- [59] Hao Shen, Weikang Wan, and He Wang. Learning categorylevel generalizable object manipulation policy via generative adversarial self-imitation learning from demonstrations. _arXiv preprint arXiv:2203.02107_ , 2022. 2, 3 

- [60] Aravind Srinivas, Michael Laskin, and Pieter Abbeel. Curl: Contrastive unsupervised representations for reinforcement learning. _arXiv preprint arXiv:2004.04136_ , 2020. 2 

- [61] Adam Stooke, Kimin Lee, Pieter Abbeel, and Michael Laskin. Decoupling representation learning from reinforcement learning. In _International Conference on Machine Learning_ , pages 9870–9879. PMLR, 2021. 2 

- [62] Martin Sundermeyer, Arsalan Mousavian, Rudolph Triebel, and Dieter Fox. Contact-graspnet: Efficient 6-dof grasp generation in cluttered scenes. In _2021 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 13438– 13444. IEEE, 2021. 1 

   - [68] Ruihai Wu, Yan Zhao, Kaichun Mo, Zizheng Guo, Yian Wang, Tianhao Wu, Qingnan Fan, Xuelin Chen, Leonidas Guibas, and Hao Dong. VAT-mart: Learning visual action trajectory proposals for manipulating 3d ARTiculated objects. In _International Conference on Learning Representations_ , 2022. 2 

   - [69] Yueh-Hua Wu, Jiashun Wang, and Xiaolong Wang. Learning generalizable dexterous manipulation from human grasp affordance. _arXiv preprint arXiv:2204.02320_ , 2022. 2, 3, 4, 6, 7, 12 

   - [70] Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng, Yijia Weng, Jiayi Chen, Tengyu Liu, Li Yi, and He Wang. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy, 2023. 2, 3, 4, 6, 7, 8, 12, 13, 14, 15 

   - [71] Zhenjia Xu, Zhanpeng He, and Shuran Song. Universal manipulation policy network for articulated objects. _IEEE Robotics and Automation Letters_ , 7(2):2447–2454, 2022. 1 

   - [72] Denis Yarats, Amy Zhang, Ilya Kostrikov, Brandon Amos, Joelle Pineau, and Rob Fergus. Improving sample efficiency in model-free reinforcement learning from images. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 35, pages 10674–10681, 2021. 2 

   - [73] Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Karol Hausman, Chelsea Finn, and Sergey Levine. Metaworld: A benchmark and evaluation for multi-task and meta reinforcement learning. In _Conference on robot learning_ , pages 1094–1100. PMLR, 2020. 2, 3, 8, 15 

   - [74] Fangyi Zhang, J¨urgen Leitner, Michael Milford, Ben Upcroft, and Peter Corke. Towards vision-based deep reinforcement learning for robotic motion control. _arXiv preprint arXiv:1511.03791_ , 2015. 2 

- [63] Yee Teh, Victor Bapst, Wojciech M Czarnecki, John Quan, James Kirkpatrick, Raia Hadsell, Nicolas Heess, and Razvan Pascanu. Distral: Robust multitask reinforcement learning. _Advances in neural information processing systems_ , 30, 2017. 2, 3, 4 

- [64] Faraz Torabi, Garrett Warnell, and Peter Stone. Behavioral cloning from observation. _arXiv preprint arXiv:1805.01954_ , 2018. 3 

- [65] Yusuke Urakami, Alec Hodgkinson, Casey Carlin, Randall Leu, Luca Rigazio, and Pieter Abbeel. Doorgym: A scalable door opening environment and baseline agent. _arXiv preprint arXiv:1908.01887_ , 2019. 3 

- [66] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. _Advances in neural information processing systems_ , 30, 2017. 14 

- [67] Chenxi Wang, Hao-Shu Fang, Minghao Gou, Hongjie Fang, Jin Gao, and Cewu Lu. Graspness discovery in clutters for fast and accurate grasp detection. In _Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)_ , pages 15964–15973, October 2021. 1 

## **A. Method and Implementation Details** 

We formalize our whole pipeline method in Algorithm 3. 

### **A.1. Details about Our Method** 

**Algorithm 3** UniDexGrasp++ 

- **Require:** Task Space T, _K_ State-based Specialists _{SS_<sup>_j_</sup> _}_ , a State-based Generalist _SG_ , _K_ Vision-based Specialists _{V S_<sup>_j_</sup> _}_ , a Vision-based Generalist _V G_ 

- 1: _{Cl} ←_ **_GeoCurriculum_** (T) for object curriculum. 2: Geometry-aware task curriculum learning to train _SG_ 0. 3: **for** _i_ = 1 _,_ 2 _, . . ._ **do** : 4: Initialize specialist _SSi_<sup>_j_=</sup><sup>_SGi_</sup> 5: _{cj} ←_ **_GeoClustering_** (T) 6: Online assign tasks that are nearest to _cj_ to specialist _SSi_<sup>_j_</sup> and train _SSi_<sup>_j_</sup> _▷_ RL 

- 7: **if** _{SSi_<sup>_j}_are optimal</sup><sup>**then break**</sup> 8: **else** 9: Distill _{SSi_<sup>_j}_to</sup><sup>_SGi_+1</sup><sup>_▷_DAgger-based Distillation</sup> 

- 10: **end if** 11: **end for** 12: Distill _{SSi_<sup>_j}_to</sup><sup>_V G_0</sup> _▷_ DAgger-based Distillation 13: **for** _i_ = 1 _,_ 2 _, . . ._ **do** : 14: Initialize specialist _V Si_<sup>_j_=</sup><sup>_V Gi_</sup> 15: _{cj} ←_ **_GeoClustering_** (T) 16: Online assign tasks that are nearest to _cj_ to specialist _V Si_<sup>_j_</sup> and train _V Si_<sup>_j_</sup> _▷_ RL 

- 17: Distill _{V Si_<sup>_j}_</sup> _i_<sup>_K_</sup> =1<sup>to</sup><sup>_V Gi_+1</sup><sup>_▷_DAgger-based Distillation</sup> 18: **if** _V Gi_ +1 is optimal **then break** 19: **end if** <u>20:</u> **<u>end for</u>** 

**Details of** **_GiGSL_ :** During the state-based policy learning stage, we terminate training when the success rate of the current policy _SSn_ is only marginally better than the previous policy _SSn−_ 1 (by less than 0.5%). At this point, we distill _SSn_ to the vision-based policy. In the vision-based policy learning stage, we stop training when the success rate of the current policy _V Gn_ is only marginally better than the previous policy _V Gn−_ 1 (by less than 0.5%). We then use _V Gn_ as our final policy. 

**Details of** **_AutoEncoder_ :** We train the point cloud 3D autoencoder using the point cloud _{Pt_<sup>(</sup> =0<sup>_k_)</sup><sup>_}N_</sup> _k_ =1<sup>sample</sup> of the initialized objects in the sample tasks _{τ_<sup>(</sup><sup>_k_)</sup> _}_<sup>_N_</sup> _k_ =1<sup>sample</sup> . The autoencoder follows an encoder-decoder structure. The encoder _E_ encodes _Pt_<sup>(</sup> =0<sup>_k_)and outputs the encoding latent fea-</sup> ture _z_<sup>(</sup><sup>_k_)</sup> = _E_ ( _Pt_<sup>(</sup> =0<sup>_k_)). The decoder</sup><sup>_D_takes</sup><sup>_z_(</sup><sup>_k_) as input and</sup> generates the point cloud _P_<sup>ˆ</sup> _t_<sup>(</sup> =0<sup>_k_).</sup> 





The model is trained using the reconstruction loss _L_ AE, which is the Chamfer Distance between _Pt_<sup>(</sup> =0<sup>_k_)and</sup><sup>_P_ˆ (</sup> _t_ =0<sup>_k_).</sup> 



**Details of** **_GeoCurriculum_ :** In our implementation, we choose _N_ level = 4 and use a 4-stage _GeoCurriculum_ to train, where the task number is 1-300-900- _N_ train. We also compare different _N_ level and the result can be found in Sec. C 

### **A.2. Details about Baselines** 

**PPO** Proximal Policy Optimization (PPO) [55] is a popular model-free on-policy RL method. We adopt PPO as our RL baseline. 

**DAPG** Demo Augmented Policy Gradient (DAPG) [49] is a popular imitation learning (IL) method that leverages expert demonstrations to reduce sample complexity. Following the approach of ILAD [69], we generate demonstrations using motion planning. 

**ILAD** ILAD [69] is an imitation learning method that enhances the generalizability of DAPG. It introduces a novel imitation learning objective on top of DAPG, which jointly learns the geometric representation of the object using behavior cloning from the generated demonstrations during policy learning. We use the same generated demonstrations as in DAPG in this method. 

**GSL** Generalist-Specialist Learning (GSL) [29] is a three-stage learning method that first trains a generalist using RL on all environment variations, then fine-tunes a large population of specialists with weights cloned from the generalist, each trained using RL to master a selected small subset of variations. Finally, GSL uses these specialists to collect demonstrations and employs DAPG for the IL part to train a generalist. For a fair comparison, we adopt PPO [55] for the RL part and DAPG [49] for the IL part in our implementation. **UniDexGrasp** UniDexGrasp [70] is a two-stage learning method. In the first state-based stage, they propose Object Curriculum Learning (OCL), which starts RL with one object and gradually incorporates similar objects from the same or similar categories into the training to obtain a state-based teacher policy. Once they obtain this teacher policy, they use DAgger [51] to distill it to a vision-based policy. 

## **B. Experiment Details** 

As described in Sec.4, we use PPO [55] in _GeoCurriculum_ learning stage to get the first generalist _SG_ 1, and 

|Parameters|Description|
|---|---|
|**_q_** _∈_R<sup>18</sup><br>**˙****_q_** _∈_R<sup>18</sup><br>**_τ_**dof _∈_R<sup>24</sup><br>_x_finger _∈_R<sup>3</sup><sup>_×_5</sup><br>_α_finger _∈_R<sup>4</sup><sup>_×_5</sup><br>˙_x_finger _∈_R<sup>3</sup><sup>_×_5</sup><br>_ω_finger _∈_R<sup>3</sup><sup>_×_5</sup><br>_F_finger _∈_R<sup>3</sup><sup>_×_5</sup><br>_τ_finger _∈_R<sup>3</sup><sup>_×_5</sup>|joint positions<br>joint velocities<br>dof force<br>fingertip position<br>fingertip orientation<br>fingertip linear velocities<br>fingertip angular velocities<br>fingertip force<br>fingertip torque|
|**_t_**_∈_R<sup>3</sup>|hand root global transition|
|_R ∈_R<sup>3</sup><sup>_×_3</sup><br>**_a_**_∈_R<sup>24</sup>|hand root global orientation<br>action|





Figure 5: **Camera positions** 

Table 4: Robot state definition. 

follows (All the _ω∗_ here are hyper-parameters same with UniDexGrasp.): 

in specialist learning stage _{_ SS _i}_ , _{_ VS _i}_ to train these specialist. In the generalist learning stages _SGi_ ( _i >_ 1) and _V Gi_ , we employ our proposed DAgger-based policy distillation. Note that we freeze the vision-backbone in the _{_ VS _i}_ learning stage. 

### **B.1. Environment Setup** 

**State Definition** The full state of the state-based policy is denoted as _St_<sup>_S_=(</sup><sup>_Rt, Ot, Pt_=0), while the full state of the</sup> vision-based policy is represented as _St_<sup>_V_=(</sup><sup>_Rt, Pt_).The</sup> robot state _Rr_ is detailed in Table 4, and the object oracle state _Ot_ includes the object pose (3 degrees of freedom for position and 9 degrees of freedom for rotation matrix), linear velocity, and angular velocity. To accelerate the training process, we sample only 1024 points from the object and the hand in the scene point cloud _Pt_ . 

**Action Space** The action space is the motor command of 24 actuators on the dexterous hand. The first 6 motors control the global position and orientation of the dexterous hand and the rest 18 motors control the fingers of the hand. We normalize the action range to ( _−_ 1 _,_ 1) based on actuator specification. 

**Camera Setup** Similar to UniDexGrasp [70], we employ a setup consisting of five RGBD cameras positioned around and above the table, as shown in Fig. 5. The system’s origin is located at the center of the table, and the cameras are positioned at ([0.5, 0, 0.05], [-0.5, 0, 0.05], [0, 0.5, 0.05], [0, -0.05, 0.05], [0, 0, 0.55]), with their focal points set to [0, 0, 0.05]. We fuse the partial point clouds generated by the five cameras to one scene point cloud _Pt_ . 

**Reward Function:** We use the non-goal-conditioned reward version in UniDexGrasp [70], and we formalize it as 



The lifting reward _r_ lift encourages the robot hand to lift the object when the fingers are close enough to the object. _f_ is a flag to judge whether the robot reaches the lifting condition: _f_ = **Is** (<sup>�</sup> _∥_ **x** finger _−_ **x** obj _∥_ 2 _< λf_ 1) + **Is** ( _d_ obj _> λ_ 0). Here, _d_ obj = _∥_ **x** obj _−_ **x** target _∥_ 2, where **x** obj and **x** target are object position and target position. _az_ is the scaled force applied to the hand root along the z-axis ( _ωl >_ 0). 



The moving reward _r_ move encourages the object to reach the target and it will give a bonus term when the object is lifted very closely to the target: 



Finally, we add each component and formulate our reward function as follows: 



### **B.2. Training Details** 

**Network Architecture:** The MLP used in the statebased policy _πE_ and the vision-based policy _πS_ consists of 4 hidden layers (1024, 1024, 512, 512). We use the exponential linear unit (ELU) [10] as the activation function. 

|Hyperparameter|Value|
|---|---|
|Num. envs (Isaac Gym, state-based)|1024|
|Num. envs (Isaac Gym, vision-based)|32|
|Env spacing (Isaac Gym)|1.5|
|Num. rollout steps per policy update (PPO)|8|
|Num. rollout steps per policy update (DAgger)|1|
|Num. batches per agent|4|
|Num. learning epochs|5|
|Buffer size (DAgger)|2000|
|<br>Episode length|200|
|Saturation threshold of policy iteration|0.005|
|<br>Discount factor|0.96|
|GAE parameter|0.95|
|<br>Entropy coeff.|0.0|
|PPO clip range|0.2|
|Learning rate|0.0003|
|Value loss coeff.|1.0|
|Max gradient norm|1.0|
|Initial noise std.|0.8|
|Desired KL|0.16|
|Clip observations|5.0|
|Clip actions|1.0|
|_N_sample|270,000|
|_N_train|3200|
|_N_clu|20|
|_ωr_|0.5|
|_ωl_|0.1|
|_ωm_|2|
|_ωb_|10|



#### Table 5: **Hyperparameter for grasping policy.** 

The network structure of the PointNet in the autoencoder is (1024, 512, 64). We use the PointNet + Transformer backbone in [40] as our vision backbone, where we use different PointNets [44] to process points having different segmentation masks (robot, object, entire point cloud). There’s also an additional MLP to output a 256-d hidden vector for the robot state alone. All the features from the MLP and PointNets are fed into a Transformer [66]. The output vectors are passed through global attention pooling to extract a representation of dimension 256, which is then provided into a final MLP with layer sizes [256, 128, feature ~~d~~ im] to output a visual feature, that is then concatenated with the robot state. 

**Hyperparameters of Training:** The hyperparameters in our experiments are listed in Tab.5. 

**Training time:** The experiment is done on four NVIDIA RTX 3090 Ti. The training process consists of 20,000 environment steps in the first stage of _GeoCurriculum_ and 15,000 environment steps (for every single policy) in other stages. It needs two days in total. 

## **C. Additional Results and Analysis** 

This section contains extended results of the experiment depicted in Sec. 5. 

**More ablation on** **_GeoCurriculum_ .** We do additional ablation experiments on the effectiveness of _GeoCurriculum_ , and the results are presented in Table 6. Specifically, we compare our proposed _GeoCurriculum_ approach with not using any curriculum learning and with the objectcurriculum-learning (OCL) method proposed in [70]. Our findings indicate that curriculum learning is essential for achieving success in the challenging dexterous grasping task with large variations in object instances and their initial poses. Moreover, we observed that our _GeoCurriculum_ approach, which considers the geometric similarity of different objects and poses, outperforms the OCL method, which only considers the category label of objects. In addition, we do an ablation study on the number of curriculum learning stages. For the 3-stage _GeoCurriculum_ , the task number is 1-100- _N_ train; for the 4-stage _GeoCurriculum_ , the task number is 1-300-900- _N_ train; and for the 5-stage _GeoCurriculum_ , the task number is 1-20-100-1000- _N_ train. We compared the performance of _SG_ 1 for all the experiments. Since the performance of the 5-stage _GeoCurriculum_ is similar to that of the 4-stage _GeoCurriculum_ , we choose the 4-stage in our main experiment for simplicity. 

|Model|Train(%)<br>Test(%)|
|---|---|
||Uns. Obj.<br>Seen Cat.<br>Uns. Cat.|
|No Curriculum|30.5<br>23.4<br>20.6|
|OCL[70]|79.4<br>74.3<br>70.8|
|_GeoCurriculum_(3)|81.3<br>75.6<br>73.3|
|_GeoCurriculum_(4)|82.7<br>**76.8**<br>**74.2**|
|_GeoCurriculum_(5)|**82.9**<br>76.4<br>74.0|
|Table 6: **Ablation st**|**udy on** **_GeoCurriculum_.** OCL refers|
|to the Object Curric<br>numbers in brackets<br>riculum learning.|ulum Learning proposed in [70]. The<br>represent the number of stages for cur-|
|**More ablation stud**<br>method used in it|**y on** **_iGSL_** For the policy distillation<br>erative Generlist-Specilist Learning|
|(_iGSL_), we compare <br>with several popular|our DAgger-based policy distillation<br>imitation learning methods, including|
|Behavior Cloning (w|e also add a value function learning|
|to make the process|iterative), GAIL [26] and DAPG [70].|
|We use _GeoCurricul_|_um_ for all the methods and compare|
|the performance of <br>which demonstrate <br>lation method signii|_SGn_+1.<br>Tab.7 shows the results,<br>that our DAgger-based policy distil-<br>ficantly outperforms other methods.|



Notably, our method uses the teacher checkpoint, while other methods only use the demonstrations from the teacher. 

|Model|Train(%)|Test|(%)|
|---|---|---|---|
|||Uns. Obj.<br>Seen Cat.|Uns. Cat.|
|BC + Value|12.4|8.6|8.4|
|GAIL[26]|30.7|26.9|26.0|
|DAPG[70]|61.4|52.6|47.9|
|Ours|**87.9**|**84.3**|**83.1**|



Table 7: **Ablation study on the policy distillation method.** 

**More ablation study on** **_GiGSL_** We provide more ablation results of _GiGSL_ . First, we do ablation experiments on the cluster number _N_ clu in _GeoClustering_ . We compare the performance of the final vision-based policy _V Gn_ for different _N_ clu. The results are in Tab.8 which show that increasing _N_ clu beyond a certain point does not improve performance and may even decrease it. 

|Model|Train(%)|Test|(%)|
|---|---|---|---|
|||Uns. Obj.<br>Seen Cat.|Uns. Cat.|
|0 (No specialist)|77.4|72.6|68.8|
|10|80.3|74.9|75.2|
|20|**85.4**|**79.6**|**76.7**|
|50|77.2|71.2|69.9|



Table 8: **Ablation study on the cluster number.** 

|Model|Train(%)|Test|(%)|
|---|---|---|---|
|||Uns. Obj.<br>Seen Cat.|Uns. Cat.|
|Random|77.0|71.9|68.2|
|Category Label.|79.7|73.9|74.1|
|Ours|**85.4**|**79.6**|**76.7**|



Table 9: **Ablation study on the pre-trained autoencoder.** The features from the encoder are used in _GeoClustering_ in the state-based setting. 

proposed technique, **_iGSL_** , performs well on the multi-task MT-10 & MT-50 and outperforms the baseline methods. 

||PPO[55]|GSL[29]|Ours|
|---|---|---|---|
|MT-10(%)|58.4±10.1|77.5±2.9|**80.3±0.5**|
|MT-50(%)|31.1±4.5|43.5±2.2|**45.9±1.7**|



Table 10: **Addtional Experiment in Meta-World.** 

**Additional Qualitative Grasping Results** We show more qualitative results in Fig.6 and Fig.7. In Fig.6, we provide more results about our _GeoClustering_ in the vision-based policy learning stage. The vision-based policy _V G_ 1 utilizes its vision backbone to extract visual features of the tasks for clustering. Due to the vision-based clustering being task-aware, we also show the grasping poses of these tasks. The results in Fig.6 demonstrate that our approach can cluster tasks based on the object geometry, pose features, and corresponding grasping strategy of the generalist policy. In Fig.7, we provide several grasping trajectories for different objects with different initial poses. 

Then, we compare our _GeoClustering_ with random clustering and category label-based clustering (we evenly divide all the categories into _N_ clu parts for a fair comparison). In category class-based clustering, we pre-train a classification task on all the objects and their initial poses. We then use the feature of the second-to-last layer for clustering and concatenate this feature to the robot state and object state in the state-based policy learning. We compare the performance of the final vision-based policy _V Gn_ for different methods. The results are shown in Tab.9. 

**More Results on Meta-World** Here we show additional results on Meta-World [73], a popular multi-task policy learning benchmark. The MT-10 task consists of 10 diverse and challenging tasks, such as opening a door or picking up objects, that require a wide range of skills and abilities. The MT-50 task set is an extension of the MT-10 task set and includes 50 additional tasks that are even more complex and diverse. We The results in Tab.10 demonstrate that our 



<!-- Start of picture text -->
𝒞!<br>𝒞"<br>𝒞#<br>𝒞$<br><!-- End of picture text -->

Figure 6: **Qualitative Grasping Results** . For each of the 4 clusters, we visualize 10 tasks and their corresponding grasping poses of the policy. The clusters are generated by our _GeoClustering_ in the vision-based policy learning stage. 



<!-- Start of picture text -->
Object Initial Pose Init Reach Grasp Lift Final<br>Airplane<br>Bottle<br>Camera<br>Elephant<br><!-- End of picture text -->

Figure 7: **Qualitative Grasping Trajecoties** . We provide several grasping trajectories for different objects with different initial poses. 

