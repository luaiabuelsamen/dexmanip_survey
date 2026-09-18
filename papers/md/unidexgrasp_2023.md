# **UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy** 

Yinzhen Xu<sup>*1,2,3</sup> , Weikang Wan<sup>*1,2</sup> , Jialiang Zhang<sup>*1,2</sup> , Haoran Liu<sup>*1,2</sup> , Zikang Shan<sup>1</sup> , Hao Shen<sup>1</sup> , Ruicheng Wang<sup>1</sup> , Haoran Geng<sup>1,2</sup> , Yijia Weng<sup>4</sup> , Jiayi Chen<sup>1</sup> , Tengyu Liu<sup>3</sup> , Li Yi<sup>5</sup> , He Wang<sup>†1,2</sup> 1 Center on Frontiers of Computing Studies, Peking University 2 School of EECS, Peking University 3 Beijing Institute for General AI 4 Stanford University 5 Tsinghua University https://pku-epic.github.io/UniDexGrasp/ 



Figure 1. **UniDexGrasp via grasp proposal generation and goal-conditioned execution.** Left ( _grasp proposals_ ): each figure demonstrates two or three diverse and high-quality grasp proposals that vary greatly in rotation, translation, and joint angles; right ( _grasp execution_ ): given a grasp goal pose, our highly generalizable goal-conditioned grasping policy can grasp the object in the way specified by the goal, as shown in the green and blue trajectories and their corresponding goals. 

## **Abstract** 

_In this work, we tackle the problem of learning universal robotic dexterous grasping from a point cloud observation under a table-top setting. The goal is to grasp and lift up objects in high-quality and diverse ways and generalize across hundreds of categories and even the unseen. Inspired by successful pipelines used in parallel gripper grasping, we split the task into two stages: 1) grasp proposal (pose) generation and 2) goal-conditioned grasp execution. For the first stage, we propose a novel probabilistic model of grasp pose conditioned on the point cloud observation that factorizes rotation from translation and articulation. Trained_ 

> *Equal contribution. 

> †Corresponding author. 

_on our synthesized large-scale dexterous grasp dataset, this model enables us to sample diverse and high-quality dexterous grasp poses for the object point cloud. For the second stage, we propose to replace the motion planning used in parallel gripper grasping with a goal-conditioned grasp policy, due to the complexity involved in dexterous grasping execution. Note that it is very challenging to learn this highly generalizable grasp policy that only takes realistic inputs without oracle states. We thus propose several important innovations, including state canonicalization, object curriculum, and teacher-student distillation. Integrating the two stages, our final pipeline becomes the first to achieve universal generalization for dexterous grasping, demonstrating an average success rate of more than 60% on thousands of object instances, which significantly out-_ 

1 

_performs all baselines, meanwhile showing only a minimal generalization gap._ 

## **1. Introduction** 

Robotic grasping is a fundamental capability for an agent to interact with the environment and serves as a prerequisite to manipulation, which has been extensively studied for decades. Recent years have witnessed great progress in developing grasping algorithms for parallel grippers [8, 17, 18, 21, 54, 56] that carry high success rate on universally grasping unknown objects. However, one fundamental limitation of parallel grasping is its low dexterity which limits its usage to complex and functional object manipulation. 

Dexterous grasping provides a more diverse way to grasp objects and thus is of vital importance to robotics for functional and fine-grained object manipulation [2, 31, 41, 43, 59]. However, the high dimensionality of the actuation space of a dexterous hand is both the advantage that endows it with such versatility and the major cause of the difficulty in executing a successful grasp. As a widely used fivefinger robotic dexterous hand, ShadowHand [1] amounts to 26 degrees of freedom (DoF), in contrast with 7 DoF for a typical parallel gripper. Such high dimensionality magnifies the difficulty in both generating valid grasp poses and planning the execution trajectories, and thus distinguishes the dexterous grasping task from its counterpart for parallel grippers. Several works have tackled the grasping pose synthesis problem [6, 30, 35, 54], however, they all assume oracle inputs (full object geometry and states). Very few works [9,41] tackle dexterous grasping in a realistic robotic setting, but so far no work yet can demonstrate universal and diverse dexterous grasping that can well generalize to unseen objects. 

In this work, we tackle this very challenging task: learning universal dexterous grasping skills that can generalize well across hundreds of seen and unseen object categories in a realistic robotic setting and only allow us to access depth observations and robot proprioception information. Our dataset contains more than one million grasps for 5519 object instances from 133 object categories, which is the largest robotic dexterous grasping benchmark to evaluate universal dexterous grasping. 

Inspired by the successful pipelines from parallel grippers, we propose to decompose this challenging task into two stages: 1) **dexterous grasp proposal generation** , in which we predict diverse grasp poses given the point cloud observations; and 2) **goal-conditioned grasp execution** , in which we take one grasp goal pose predicted by stage 1 as a condition and generates physically correct motion trajectories that comply with the goal pose. Note that both of these two stages are indeed very challenging, for each of which we contribute several innovations, as explained below. 

For dexterous grasp proposal generation, we devise a novel conditional grasp pose generative model that takes point cloud observations and is trained on our synthesized large-scale table-top dataset. Here our approach emphasizes the diversity in grasp pose generation, since the way we humans manipulate objects can vary in many different ways and thus correspond to different grasping poses. Without diversity, it is impossible for the grasping pose generation to comply with the demand of later dexterous manipulation. Previous works [24] leverages CVAE to jointly model hand rotation, translation, and articulations and we observe that such CVAE suffers from severe mode collapse and can’t generate diverse grasp poses, owing to its limited expressivity when compared to conditional normalizing flows [13, 14, 16, 25, 38] and conditional diffusion models [5, 46, 51]. However, no works have developed normalizing flows and diffusion models that work for the grasp pose space, which is a Cartesian product of **SO(3)** of hand rotation and a Euclidean space of the translation and joint angles. We thus propose to decompose this conditional generative model into two conditional generative models: a conditional rotation generative model, _namely_ GraspIPDF, leveraging ImplicitPDF [36] (in short, IPDF) and a conditional normalizing flow, _namely_ GraspGlow, leveraging Glow [25]. Combining these two modules, we can sample diverse grasping poses and even select what we need according to language descriptions. The sampled grasps can be further refined to be more physically plausible via ContactNet, as done in [24]. 

For our grasp execution stage, we learn a goalconditioned policy that can grasp any object in the way specified by the grasp goal pose and only takes realistic inputs: the point cloud observation and robot proprioception information, as required by real robot experiments. Note that reinforcement learning (RL) algorithms usually have difficulties with learning such a highly generalizable policy, especially when the inputs are visual signals without ground truth states. To tackle this challenge, we leverage a teacher-student learning framework that first learns an oracle teacher model that can access the oracle state inputs and then distill it to a student model that only takes realistic inputs. Even though the teacher policy gains access to oracle information, making it successful in grasping thousands of different objects paired with diverse grasp goals is still formidable for RL. We thus introduce two critical innovations: a canonicalization step that ensures **SO(2)** equivariance to ease the policy learning; and an object curriculum that first learns to grasp one object with different goals, then one category, then many categories, and finally all categories. 

Extensive experiments demonstrate the remarkable performance of our pipelines. In the grasp proposal generation stage, our pipeline is the only method that exhibits high di- 

2 

versity while maintaining the highest grasping quality. The whole dexterous grasping pipeline, from the vision to policy, again achieves impressive performance in our simulation environment and, for the first time, demonstrates a universal grasping policy with more than 60% success rate and remarkably outperforms all the baselines. We will make the dataset and the code publicly available to facilitate future research. 

## **2. Related Work** 

**Dexterous Grasp Synthesis** Dexterous grasp synthesis, a task aiming to generate valid grasping poses given the object mesh or point cloud, falls into two categories. First, non-learning methods serve to generate large synthetic datasets. Among which, _GraspIt!_ [35] is a classical tool that synthesizes stable grasps by collision detection, commonly adopted by early works [7, 28, 29]. Recently, an optimization-based method [30] greatly improves grasp diversity with its proposed differentiable force closure estimator, enabling datasets of higher quality [27, 57]. Second, learning-based methods [7,12,22,24,28,48] learn from these datasets to predict grasps with feed-forward pipelines, but struggle to possess quality and diversity at the same time. To tackle this problem, we propose to build a conditional generative model that decouples rotation from translation and articulation. 

**Probabilistic Modeling on SO(3)** _×_ R<sup>_n_</sup> One way to generate diverse grasping poses is to learn the distribution of plausible poses using ground truth poses. GraspTTA [24] uses conditional VAE and suffers from severe model collapse which leads to limited diversity. In contrast, normalizing flow is capable of modeling highly complex distributions as it uses negative log-likelihood (NLL) as loss, suiting our needs for grasping proposal generation. Building normalizing flow (NF) in the Euclidean space has been well studied [13, 14, 25]. But unfortunately, hand pose consists of a **SO(3)** part (the rotation) and a R<sup>_n_</sup> part (the translation and joint angles), and using normalizing flow in **SO(3)** is hard due to its special topological structure. Relie [16] and ProHMR [26] both perform NF in the Euclidean space and then map it into **SO(3)** . As these two spaces are not topologically equivalent, they suffer from discontinuity and infinite-to-one mapping respectively. A more detailed analysis of these phenomena is in Sec. B.1.2 of our supp. In comparison, IPDF [36] uses a neural network to output unnormalized log probability and then normalize it with uniform samples or grids on **SO(3)** and also uses NLL as loss. As IPDF is insensitive to topological structure, it is a better choice to model distributions on **SO(3)** than existing NFs. Therefore, our grasp proposal module decouples rotation from translation and joint angles and models these distributions separately with IPDF [36] and Glow [25]. **Dexterous Grasp Execution** Executing a dexterous grasp 

requires an agent to perform a complete trajectory, rather than a static grasping pose. Previous approaches have used analytical methods [3, 4, 15] to model hand and object kinematics and dynamics, and then optimized trajectories for robot control. However, these methods typically require simplifications such as using simple finger and object geometries to make planning tractable. More recently, reinforcement and imitation learning techniques have shown promise for dexterous grasping [10,34,43,45,53,59]. However, these methods rely on omniscient knowledge of the object mesh and struggle to handle realistic task settings, making them unsuitable for deployment in the real world. To address this issue, recent works have explored using raw RGB images [33, 34] or 3D point clouds [42] as policy inputs. However, none of these methods have been able to generalize to a large number of objects under raw vision input. In contrast, our goal-conditioned grasp execution method achieves universal generalization on thousands of object instances by leveraging a teacher-student distillation trick, object curriculum learning, and state canonicalization. 

## **3. Method** 

We propose UniDexGrasp, a two-stage pipeline for generalizable dexterous grasping. We divide the task into two phases: 1) grasp proposal generation (Sec. 3.2), 2) goalconditioned grasp execution (Sec. 3.3). First, the grasp proposal generation module takes the object point cloud and samples a grasp proposal. Then, the goal-conditioned grasping policy takes this proposal as goal pose, and executes the grasp in the Isaac Gym simulator [32], taking only point cloud observations and robot proprioception as input in every time step _t_ . 

### **3.1. Problem Settings and Method Overview** 

The grasp proposal generation module, shown on the left part of Fig. 2, takes the object and table cloud _X_ 0 _∈_ R<sup>_N×_3</sup> as input, and samples a grasp proposal **_g_** = ( _R,_ **_t_** _,_ **_q_** ) out of a distribution, where _R ∈_ **SO(3)** _,_ **_t_** _∈_ R<sup>3</sup> _,_ **_q_** _∈_ R<sup>_K_</sup> represent the root rotation, root translation, and joint angles of the dexterous hand, and _K_ is the total degree-of-freedom of the hand articulations. The proposed grasp **_g_** will be the goal pose of the next module, shown on the right part of Fig. 2. 

The final goal-conditioned grasp execution module is a vision-based policy that runs in the IsaacGym [32] physics simulator. In each time step _t_ , the policy takes the goal pose **_g_** from the previous module, object and the scene point cloud _Xt_ , and robot proprioception **_s_**<sup>_r_</sup> _t_<sup>asobserva-</sup> tion, and outputs an action **_a_** _t_ . The policy should work across different object categories and even unseen categories. To simplify the problem, we initialize the hand with an initial translation **_t_** 0 = (0 _,_ 0 _, h_ 0) and an initial rotation _R_ 0 = (<sup>_<u>π</u>_</sup> 2<sup>_,_0</sup><sup>_, ϕ_0),where</sup><sup>_h_0isafixedheightandthehand</sup> 

3 



<!-- Start of picture text -->
Dexterous Grasp Proposal Generation Goal-Conditioned Dexterous Grasping Policy<br>Input Point Cloud 𝑋! Grasp Orientation Generation 𝒕= 𝑅𝒕 ( Goal-Conditioned RL<br>un-canonicalize Goal Pose 𝒈 + Point Cloud 𝑋" Robot Proprioception<br>𝑝 𝑅𝑋) 𝒈= (𝑅, 𝒕, 𝒒) 𝒔('<br>sample Grasp<br>GraspIPDF or Rotation Optimization<br>select 𝑅<br>Student Policy 𝜋 𝒮<br>canonicalize<br>ℒ$%&<br>&𝑋) = 𝑅 *+ 𝑋)<br>Grasp Translation and<br>Articulation Generation<br>ContactNet 𝒂!<br>Contact map<br>𝑝 (𝒕, 𝒒&𝑋)<br>Canonicalized<br>Point Cloud 𝑋 ( ! Grasp translation ℒ!"#$<br>and joint angles 𝒕, 𝒒 $<br>sample<br>GraspGlow or<br>select Contact-based Optimization<br><!-- End of picture text -->

Figure 2. **Method overview** . The left part is the first stage, which generates a dexterous grasp proposal. The input is the object point cloud at time step 0, _X_ 0, fused from depth images, with ground truth segmentation of the table and the object. A rotation _R_ is sampled from the distribution implied by the GraspIPDF, and the point cloud will be canonicalized by _R_<sup>_−_1</sup> to _X_<sup>˜</sup> 0. The GraspGlow then samples the translation **_t_**<sup>˜</sup> and joint angles **_q_** . Next, the ContactNet takes _X_<sup>˜</sup> 0 and a point cloud _X_<sup>˜</sup> _H_ sampled from the hand to predict the ideal contact map **_c_** on the object. Then, the predicted hand pose is optimized based on the contact information. The final goal pose is transformed by _R_ to align with the original visual observation. The right part is the second stage, the goal-conditioned dexterous grasping policy that takes the goal **_g_** , point cloud _Xt_ and robot proprioception **_s_**<sup>_r_</sup> _t_<sup>to take actions accordingly.</sup> 

rotation is initialized so that the hand palm faces down and its _ϕ_ 0 = _ϕ_ . The joint angles of the hand are set to zero. The task is to grasp the object as specified by the goal grasp label _g_ and lift it to a certain height. The task is successful if the position difference between the object and the target point is smaller than the threshold value **_t_** 0. 

Since directly training such a vision-based policy using reinforcement learning is challenging, we use the idea of _teacher-student learning_ . We first use a popular on-policy RL algorithm, PPO [52], with our proposed object curriculum learning and state canonicalization, to learn an oracle teacher policy that can access the ground-truth states of the environment ( _e.g_ . object poses, velocities and object full point cloud). This information is very useful to the task and available in the simulator but not in the real world. Once the teacher finishes training, we use an imitation learning algorithm, DAgger [49], to distill this policy to a student policy that can only access realistic inputs. 

### **3.2. Dexterous Grasp Proposal Generation** 

In this subsection, we introduce how we model the conditional probability distribution _p_ ( **_g_** _|X_ 0) : **SO(3)** _×_ R<sup>3+</sup><sup>_K_</sup> _→_ R. By factorizing _p_ ( **_g_** _|X_ 0) into two parts _p_ ( _R|X_ 0) _· p_ ( **_t_** _,_ **_q_** _|X_ 0 _, R_ ), we propose a three-stage pipeline: 1) given the point cloud observation, predict the conditional distribution of hand root rotation _p_ ( _R|X_ 0) using 

GraspIPDF (see Sec. 3.2.1) and then sample a single root rotation; 2) given the point cloud observation and the root rotation, predict the conditional distribution of the hand root translation and joint angles _p_ ( **_t_** _,_ **_q_** _|X_ 0 _, R_ ) = _p_ ( **_t_**<sup>˜</sup> _,_ **_q_** _|X_<sup>˜</sup> 0) using GraspGlow (see Sec. 3.2.2) and then sample a single proposal; 3) optimize the sampled grasp pose _g_ with ContactNet to improve physical plausibility (see Sec. 3.2.4). 

#### **3.2.1 GraspIPDF: Grasp Orientation Generation** 

Inspired by IPDF [36], a probabilistic model over **SO(3)** , we propose GraspIPDF _f_ ( _X_ 0 _, R_ ) to predict the conditional probability distribution _p_ ( _R|X_ 0) of the hand root rotation _R_ given the point cloud observation _X_ 0. This model takes _X_ 0 and _R_ as inputs, extracts the geometric features with a PointNet++ [40] backbone, and outputs an unnormalized joint log probability density _f_ ( _X_ 0 _, R_ ) = _α_ log( _p_ ( _X_ 0 _, R_ )), where _α_ is a normalization constant. The normalized probability density is recovered by computing: 



where _M_ is the number of volume partitions and _V_ =<sup>_π_2</sup> _M_ is the volume of partition. 

During train time, GraspIPDF is supervised by an NLL loss _L_ = _−_ log( _p_ ( _R_ 0 _|X_ 0)), where _R_ 0 is a ground-truth 

4 

hand root rotation. During test time, we generate an equivolumetric grid on **SO(3)** as in [20, 36, 60] and sample rotations according to their queried probabilities. 

#### **3.2.2 GraspGlow: Grasp Translation and Articulation Generation given Orientation** 

To condition a probabilistic model on _X_ 0 and _R_ simultaneously, we propose to canonicalize the point cloud to _X_ ˜0 = _R_<sup>_−_1</sup> _X_ 0. This trick simplifies the task from predicting valid grasps for observation _X_ 0 with _R_ as the hand root rotation, to predicting it for _X_<sup>˜</sup> 0 with identity as hand rotation. Then, we use a PointNet [39] to extract the features of _X_<sup>˜</sup> 0, and model the conditional probability distribution _p_ ( **_t_** _,_ **_q_** _|X_ 0 _, R_ ) = _p_ ( **_t_**<sup>˜</sup> _,_ **_q_** _|X_<sup>˜</sup> 0) where **_t_**<sup>˜</sup> = _R_<sup>_−_1</sup> **_t_** with Glow [25], a popular normalizing flow model that handles probabilistic modeling over Euclidean spaces. 

During train time, the model is supervised by an NLL loss _L_ NLL = _−_ log( _p_ ( **_t_**<sup>˜</sup> gt _,_ **_q_** gt _|X_<sup>˜</sup> 0)) using ground truth grasp data tuples ( _X_ 0 _, R_ gt _,_ **_t_** gt _,_ **_q_** gt). During test time, samples are drawn from the base distribution of Glow, and reconstructed into grasp poses using the bijection of the normalizing flow. 

#### **3.2.3 End-to-End Training with ContactNet** 

Inspired by [24], we use ContactNet to model a mapping from flawed raw grasp pose predictions to ideal contact patterns between the hand and the object. The input of the ContactNet is the canonicalized object point cloud _X_<sup>˜</sup> 0 and the sampled hand point cloud _X_<sup>˜</sup> _H_ ; the output is the contact heat _ci ∈_ [0 _,_ 1] predicted at each point **_p_** _i ∈ X_ ˜0. The ground truth of contact heat is given by _ci_ = _f_ ( _Di_ ( _X_<sup>˜</sup> _H_ )) = 2 _−_ 2 _·_ (sigmoid( _β Di_ ( _X_<sup>˜</sup> _H_ ))), where _β_ is a coefficient to help map the distance to [0 _,_ 1], and _Di_ ( _X_<sup>˜</sup> _H_ ) = min _∥_ **_p_** _i −_ **_p_** _j∥_ 2, **_p_** _j ∈ X_<sup>˜</sup> _H_ . _j_ 

Leveraging ContactNet, we construct a self-supervised task to improve the sample quality of GraspGlow by training it end-to-end with RotationNet. To be specific, in this stage, we first sample rotations with GraspIPDF, use them to canonicalize point clouds, then feed the point clouds to GraspGlow to get translations and joint angles samples. Next, ContactNet takes the grasp samples, and outputs ideal contact maps. Here we use four additional loss terms: 1) _L_ cmap: MSE between current and target contact map; 2) _L_ pen: Total penetration from object point cloud to hand mesh calculated using signed squared distance function; 3) _L_ tpen: Total penetration depth from some chosen hand key points to the plane; 4) _L_ spen: Self penetration term inspired by [62]. Then the joint loss becomes _L_ joint = _L_ NLL + _L_ add where _L_ add is defined as: 



In this stage, we freeze RotationNet as experiments demonstrate that it learns quite well in its own stage. 



Figure 3. **The goal-conditioned dexterous grasping policy pipeline** . _S_<sup>�</sup> _t_<sup>_E_=( �</sup><sup>**_s_**</sup> _t_<sup>_r,_</sup><sup>**_s_**�</sup><sup>_o_</sup> _t_<sup>_, XO,_�</sup><sup>_g_)and</sup> _S_<sup>�</sup> _t_<sup>_S_</sup> = ( **_s_**<sup>�</sup> _t_<sup>_r,_�</sup> _Xt,_ � _g_ ) denote the input state of the teacher policy and student policy after state canonicalization, respectively; _⊕_ denotes concatenation. 

#### **3.2.4 Test-Time Contact-based Optimization** 

Since the randomness of the flow sometimes leads to small artifacts, the raw outputs of GraspGlow may contain slight penetration and inexact contact. So we use ContactNet to construct a self-supervised optimization task for testtime adaptation to adjust the imperfect grasp as in [24]. 

When GraspGlow predicts a grasp, ContactNet takes the scene and hand point cloud, then outputs a target contact map on the scene point cloud. Next, the grasp pose is optimized for 300 steps to match this contact pattern. The total energy _E_ TTA consists of the four additional loss term described in Sec. 3.2.3: 



For network structures, hyperparameters, and other implementation details, please refer to Sec. B.1.1 of our supp. 

### **3.3. Goal-Conditioned Dexterous Grasping Policy** 

In this section, we will introduce our _goal-conditioned_ grasp policy learning. We introduce our proposed state canonicalization, object curriculum learning and other method details for training the teacher policy in Sec. 3.3.1. We then introduce the vision-based student policy training in Sec. 3.3.2. The teacher policy _π_<sup>_E_</sup> has a state space _St_<sup>_E_=(</sup><sup>**_s_**</sup><sup>_r_</sup> _t_<sup>_,_</sup><sup>**_s_**</sup><sup>_o_</sup> _t_<sup>_, XO,_</sup><sup>**_g_**)where</sup><sup>**_s_**</sup><sup>_r_</sup> _t_<sup>isthe robothand proprio-</sup> ception state, **_s_**<sup>_o_</sup> _t_<sup>is the object state,</sup><sup>_XO_is the pre-sampled</sup> object point cloud and **_g_** is the goal grasp label. The state of the student is defined as _S_<sup>_S_</sup> = ( **_s_**<sup>_r_</sup> _t_<sup>_, Xt,_</sup><sup>**_g_**)where</sup><sup>_Xt_is</sup> the raw scene point cloud. Details about the state and action space are provided in Sec. C.1 of our supp. 

#### **3.3.1 Learning Teacher Policy** 

We use a model-free RL framework to learn the oracle teacher policy. The goal of the goal-conditioned RL is 

5 

to maximize the expected reward E _t_ =0<sup>_γtR_(</sup><sup>**_s_**</sup><sup>_t,_</sup><sup>**_a_**</sup><sup>_t, g_)</sup> �� _T −_ 1 � with _π_<sup>_E_</sup> . We use PPO [52] for policy updating in our method. Inspired by ILAD [59], we use a PointNet [39] to extract the geometry feature of the object. ILAD pre-trains the PointNet using behavior cloning from the motion planning demonstrations and jointly trains the PointNet using behavior cloning from the RL demonstrations during policy learning. Although ILAD performs very well in one single category (96% success rate [59]), we find that directly using this method cannot get good results under the setting of _goal-conditioned_ and _cross-category_ . We then propose several techniques on top of it. First, we do state canonicalization according to the initial object pose which improves the sample efficiency of the RL with diverse goal inputs. Second, we design a novel goal-conditioned function. We then do 3-stage curriculum policy learning which significantly improves the performance under _cross-category_ setting. Additionally, we find that doing object category classification when joint training the PointNet using behavior cloning which is proposed in [59] can also improve the performance under _cross-category_ setting. 

**State Canonicalization** Ideally, this goal-conditioned grasping policy should be **SO(2)** equivariant, that is, when we rotate the whole scene and the goal grasp label with the same angle _ϕ_ about the _z_ axis (gravity axis), the grasping trajectory generated by the policy should rotate in the same way. To ensure this **SO(2)** equivariance, we define a static reference frame (denoted by � _·_ ) according to the initial hand pose: the origin of the reference frame is at the initial hand translation (0 _,_ 0 _, h_ 0) and the Euler angle of the reference frame is (0 _,_ 0 _, ϕ_ ) so that the initial Euler angle of _R_ �0the= hand(<sup>_<u>π</u>_</sup> 2<sup>_,_0</sup> in<sup>_,_0)</sup> this<sup>.Before</sup> reference<sup>weinput</sup> frame<sup>the</sup> is always<sup>statesto</sup> a fixed<sup>thepolicy,</sup> value we transfer the states from the world frame to this reference frame: _S_<sup>�</sup> _t_<sup>_E_=(</sup><sup>**_s_**�</sup><sup>_r_</sup> _t_<sup>_,_</sup><sup>**_s_**�</sup><sup>_o_</sup> _t_<sup>_, XO,_�</sup><sup>_g_).Thus,the system is</sup><sup>**SO(2)**</sup> equivariant to _ϕ_ . This improves the sample efficiency of the goal-conditioned RL. 

**Object Curriculum Learning** Since it’s difficult to train the grasping policy _cross-category_ due to the topological and geometric variations in different categories, we propose to build an object curriculum learning method to learn _π_<sup>_E_</sup> . We find that _π_<sup>_E_</sup> can already perform very well when training on one single object but fails when training directly on different category objects simultaneously. We apply curriculum learning techniques. Our curriculum learning technique is constructed as follows: first train the policy on one single object and then on different objects in one category, several representative categories, and finally on all the categories. We find that this 3-stage curriculum learning significantly boosts the success rates. More details about the ablations on the curriculum stages are in Sec. 4.3 and Tab. 4. **Pre-training and Joint Training PointNet with Classification** ILAD [59] proposed an important technique that 

jointly does geometric representation learning using behavior cloning when doing policy learning. We use this technique in our method and add additional object category classification objectives to update the PointNet. 

**Goal-conditioned Reward Function** We are supposed to conquer the dexterous manipulation problem with RL, therefore the reward design is crucial. Here is our novel goal-conditioned reward function which can guide the robot to grasp and lift the object by the standard of the goal grasp label: _r_ = _r_ goal + _r_ reach + _r_ lift + _r_ move. 

The goal reward _r_ goal punished distance between the current hand configuration and the goal hand configuration. The reaching reward _r_ reach encourages the robot fingers to reach the object. The lifting reward _r_ lift encourages the robot hand to lift the object. It’s **non-zero if and only if** the goal grasp label is reached within a threshold. The moving reward _r_ move encourages the object to reach the target. 

#### **3.3.2 Distilling to the Vision-based Student Policy** 

We then distill the teacher policy _π_<sup>_E_</sup> into the student policy _π_<sup>_S_</sup> using DAgger [49] which is an imitation method that overcomes the covariate shift problem of behavior cloning. We optimize _π_<sup>_S_</sup> by: _π_<sup>_S_</sup> = arg min _∥π_<sup>_E_</sup> ( _St_<sup>_E_)</sup><sup>_−πS_(</sup><sup>_S_</sup> _t_<sup>_S_)</sup><sup>_∥_2.</sup> _π_<sup>_S_</sup> We also use state canonicalization but this time _ϕ_ is the initial Euler angle of the robot hand root around the _z_ axis in the world frame because we don’t know the object pose in the student input states. Similarly, we transfer the states from the world frame to this reference frame:� _St_<sup>_S_</sup> = ( **_s_**<sup>�</sup><sup>_r_</sup> _t_<sup>_,_�</sup> _Xt,_ � _g_ ). The pipeline/network architecture is shown in Fig. 3. For implementation details, please refer to Sec. B.2.1 of our supp. 

## **4. Experimentals** 

### **4.1. Data Generation and Statistics** 

We used a similar method from [57] to synthesize grasps. **Data Generation** First, we randomly select an object from the pool of our training instances and let it fall randomly onto the table from a high place. Next, we randomly initialize a dexterous hand and optimize it into a plausible grasp. The optimization is guided by an energy function proposed by [57]. We add an energy term on top of this to punish penetration between the hand and the table. Finally, the grasps are filtered by penetration depth and simulation success in Isaac. Please refers to Sec. A of our supp. **Statistics** We generated 1.12 million valid grasps for 5519 object instances in 133 categories. These objects are split into three sets: training instances (3251), seen category unseen instances (754), unseen category instances (1514). 

### **4.2. Results on Grasp Proposal Generation** 

**Baselines** [24] takes point cloud as input, generates grasps with CVAE, then performs test-time adaptation with 

6 

|Method|se|en cat|uns|een cat|_σR ↑_|_σT |R ↑_|_σθ|R ↑_|_σ_keypoints _↑_|
|---|---|---|---|---|---|---|---|---|
||_Q_1 _↑_|obj. pen._↓_|_Q_1 _↑_|obj. pen._↓_|(degree)|(cm)|(degree)|(cm)|
|GraspTTA [24] (C + T)|0.0269|0.354|0.0239|0.363|4.9|/|/|2.909|
|DDG [28]|0.0357|0.319|0.0223|0.338|0.0|/|/|0.000|
|R + C + T|0.0362|0.251|**0.0336**|0.235|**128.0**|0.095|0.227|5.982|
|ReLie [16] + T|0.0190|0.219|0.0191|0.225|109.9|/|/|**6.698**|
|ProHMR [26] + T|0.0210|**0.202**|0.0221|**0.192**|88.4|/|/|5.837|
|ours (R + GL + T)|**0.0423**|0.205|0.0322|0.220|127.6|**1.143**|**5.806**|6.389|



Table 1. **Results on grasp goal generation.** R: GraspIPDF, C: CVAE, T: test-time adaptation, GL: GraspGlow, and obj. pen. is the penetration between the hand and the object. 

ContactNet. Apart from this baseline, we also designed two ablations to verify the two key designs in our pipeline. First, we substituted GraspGlow for the same CVAE from [24] to demonstrate the severe mode collapse of CVAE. Second, we substituted GraspIPDF with ReLie to demonstrate the problem of discontinuity, as described in Sec. 2. 

**Metrics** We use some analytical metrics to evaluate quality and diversity. 1) _Q_ 1 [19]. The smallest wrench needed to make a grasp unstable. 2) Object penetration depth(cm). Maximal penetration from object point cloud to hand mesh. 3) _σR_<sup>2</sup> /keypoints<sup>.Variance of rotation or keypoints.4)</sup><sup>_σ_</sup> _T/θ_<sup>2</sup> _|R_<sup>.</sup> Variance of translation or joint angles with fixed rotation. **Ablation 1: Decoupling.** Tab. 1 shows that the _Q_ 1 of the fourth row and the fifth row is significantly lower than the last row, implying that the normalizing flow on **SO(3)** _×_ R<sup>3+22</sup> failed to learn a good distribution. On the other hand, our model can produce grasps with much higher quality. We argue that this improvement is contributed by rotation factorization, which allows us to use IPDF and GLOW to model the distributions on **SO(3)** and R<sup>22</sup> separately. However, as shown in Tab. 2, further decoupling translation and joint angles will result in worse performance as it is less end-to-end. 

**Ablation 2: GLOW vs CVAE.** The reason we favored GLOW over CVAE can be interpreted from the last two columns of Tab. 1. If the input object point cloud is fixed, then no matter what the latent _z_ vector is, CVAE will always collapse to a single mode. However, GLOW can propose diverse results. Fig. 4 shows a typical case. **Ablation 3: TTA.** As discussed in Sec. 3.2.4 and shown in Tab. 2, poses sampled from flow are usually imperfect and need TTA to make them plausible. 

### **4.3. Grasp Execution** 

**Environment Setup and Data** We use a subset of the train split proposed in Sec. 4.1 as our training data. For the state-based policy evaluation, we use the grasp proposals sampled by our grasp proposal generation module. For the final vision-based policy evaluation, we use both the training data (“GT” in Tab. 4) and grasp proposals sampled by our grasp proposal generation module (“pred” in Tab. 4) as 



Figure 4. **Comparison of diversity in grasp translation and articulation given the rotation.** Left: 8 outputs of CVAE (completely collapsed to one pose); Middle: 8 outputs of GraspGLOW; Right: a ground truth grasp. 

|Met|hod|decoup.T|w/o TTA|ours|
|---|---|---|---|---|
|seen|_Q_1 _↑_|0.0003|0.0013|**0.0423**|
|cat.|pen._↓_|0.862|0.744|**0.205**|
|unseen|_Q_1 _↑_|0.0061|0.0000|**0.0322**|
|cat.|pen._↓_|0.843|0.764|**0.220**|



Table 2. **Ablation study on decoupling translation and joint angles and TTA.** decoup.T: decouple translation, w/o TTA: without TTA and pen. is the penetration between the hand and the object. 

the goal of our policy to do testing on the train object set and test object set. Details are in Sec. C.2 of our supp. **Baselines and Compared Methods** We adopt PPO [52] as our RL baseline and DAPG [45] as our Imitation Learning (IL) baseline. We also compared our method with ILAD [59] which can reach a very high success rate in one category and can generalize to novel object instances within the same category. We further do ablations on our proposed techniques. All methods are compared under the same setting of teacher policy. Once we get the teacher policy with the highest success rate, we distill it to the student policy. **Main Results** The top half of Tab. 3 shows that our method outperforms baselines by a large margin. The PPO (RL) and DAPG (IL) baseline only achieve an average success rate of 14% and 13% on the train set. Our teacher method achieves an average success rate of 74% on the train set, 69% on the test set, which is about **49%** and **47%** improvement over ILAD. Since our method has a teacher pol- 

7 

|Model|Train|Te|st|
|---|---|---|---|
|||unseen obj<br>seen cat|unseen cat|
|MP|0.12_±_0.01|0.02_±_0.00|0.02_±_0.01|
|PPO [52]|0.14_±_0.06|0.11_±_0.04|0.09_±_0.06|
|DAPG [45]|0.13_±_0.05|0.13_±_0.08|0.11_±_0.05|
|ILAD [59]|0.25_±_0.03|0.22_±_0.04|0.20_±_0.05|
|Ours|**0.74**_±_**0.07**|**0.71**_±_**0.05**|**0.66**_±_**0.06**|
|Ours(w/o SC)|0.59_±_0.06|0.54_±_0.07|0.51_±_0.04|
|Ours(w/o cls)|0.65_±_0.05|0.64_±_0.06|0.60_±_0.07|
|Ours(w/o OCL)|0.31_±_0.07|0.23_±_0.06|0.21_±_0.04|
|Ours(1-stage OCL)|0.58_±_0.07|0.55_±_0.03|0.55_±_0.05|
|Ours(2-stage OCL)|0.68_±_0.06|0.67_±_0.07|0.62_±_0.05|



Table 3. **The success rate of state-based policy** . The experiment is evaluated with three different random seeds. “MP”: motion planning;“SC”: state canonicalization; “cls”; joint learning object classification; “OCL”: object curriculum learning. 

icy with the highest success rate, we distill this policy to a vision-based student policy and the success rate decreases by 6% and 7% on the train and test set respectively (the first line of Tab. 4). This indicates that the vision-based, goal-conditional, and cross-category setting is difficult and the student’s performance is limited by the teacher’s performance. 

**Ablation Results** We evaluate our method without state canonicalization (w/o SC), without object classification (w/o classification), and without object curriculum learning (w/o OCL). Tab. 3 shows that each technique yields considerable performance improvement. We do more specific ablations on stages of object curriculum learning (OCL). We stipulate— **a** : train on one object; **b** : train on one category; **c** : train on 3 representative categories; **d** : train on all the categories. We formulate the experiment as follows: w/o OCL: **d** ; 1-stage OCL: **a** _→_ **d** ; 2-stage OCL: **a** _→_ **b** _→_ **d** ; 3-stage OCL: **a** _→_ **b** _→_ **c** _→_ **d** ; As shown in Tab. 3, without OCL, the policy seldom succeeds both during training and testing. However, as the total stages of the curriculum increase, the success rate improves significantly. In Tab. 4, we conduct the robustness test for our vision-based policy by jittering our predicted grasp poses to cause small penetration (a), large penetration (b), and no contact (c) and observe our grasp execution policy is robust to such errors. 

### **4.4. Language-guided Dexterous Grasping** 

A natural downstream task for our method is to introduce specific semantic meaning parsing, _e.g_ . “grasping a hammer by the handle”. Thanks to the great diversity of grasp proposals, this can be easily done by adding a filtering module using CLIP [44], a large text-image pre-train model which shows significant generalizability for computing the similarity between text and images. Combined with the goalconditioned policy network, the robot is endowed with the 

|Penetration (cm)|Train|Te|st|
|---|---|---|---|
|||unseen obj<br>seen cat|unseen cat|
|0.117 (GT)|0.68_±_0.06|0.65_±_0.05|0.63_±_0.04|
|0.208(pred)|0.66_±_0.04|0.59_±_0.04|0.58_±_0.05|
|0.512 (a)|0.63_±_0.05|0.54_±_0.05|0.57_±_0.04|
|1.058 (b)|0.47_±_0.04|0.37_±_0.05|0.39_±_0.04|
|-0.309 (c)|0.50_±_0.03|0.38_±_0.02|0.35_±_0.03|



Table 4. **The success rate of our vision-based policy** . We test our trained vision-based policy with jittered goal grasp on the train and test set. 









<!-- Start of picture text -->
(a) Grasp a bottle by the body/bottleneck, or from below<br><!-- End of picture text -->







<!-- Start of picture text -->
(b) Grasp a hammer by the head/handle<br><!-- End of picture text -->

Figure 5. **Qualitative results of language-guided grasp proposal selection.** CLIP can select proposals complying with the language instruction, allowing the goal-conditioned policy to execute potentially functional grasps. 

ability to grasp an object according to human instructions. One of the most promising applications is for the functional grasping of certain tools, _e.g_ . bottles and hammers. In detail, we select images rendered from grasp proposals with the highest image-text similarity following the user command ( _e.g_ . “A robot hand grasps a hammer by the handle.”). As shown in Fig. 5, with only 10 minutes of fine-tuning, the model can achieve around 90% accuracy in the bottle and hammer categories. This validates the feasibility of generating grasps with specific semantic meanings using our generation pipeline together with the CLIP model. 

## **5. Conclusions and Discussions** 

In our work, we propose a novel two-stage pipeline composed of grasp proposal generation and goal-conditioned grasp execution. The whole pipeline for the first time demonstrates universal dexterous grasping over thousand of objects under a realistic robotic setting and thus has the potential to transfer to real-world settings. The limitation is that we only tackle the grasping of rigid objects, in contrast to articulated objects like scissors. Furthermore, functional dexterous grasping still remains a challenging but promising field to explore. 

8 

## **References** 

- [1] ShadowRobot. URL https://www.shadowrobot. com/dexterous-hand-series/, 2005. 2 

- [2] Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias Plappert, Glenn Powell, Raphael Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 2 

- [3] Sheldon Andrews and Paul G Kry. Goal directed multi-finger manipulation: Control policies and analysis. _Computers & Graphics_ , 37(7):830–839, 2013. 3 

- [4] Yunfei Bai and C. Karen Liu. Dexterous manipulation using both palm and fingers. In _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 1560–1565, 2014. 3 

- [5] Georgios Batzolis, Jan Stanczuk, Carola-Bibiane Sch¨onlieb, and Christian Etmann. Conditional image generation with score-based diffusion models. _arXiv preprint arXiv:2111.13606_ , 2021. 2 

- [6] Samarth Brahmbhatt, Cusuh Ham, Charles C. Kemp, and James Hays. ContactDB: Analyzing and predicting grasp contact via thermal imaging. In _The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 6 2019. 2 

- [7] Samarth Brahmbhatt, Ankur Handa, James Hays, and Dieter Fox. ContactGrasp: Functional Multi-finger Grasp Synthesis from Contact. In _2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2019. 3 

- [8] Michel Breyer, Jen Jen Chung, Lionel Ott, Roland Siegwart, and Juan Nieto. Volumetric grasping network: Realtime 6 dof grasp detection in clutter. _arXiv preprint arXiv:2101.01132_ , 2021. 2 

- [9] Qiuyu Chen, Karl Van Wyk, Yu-Wei Chao, Wei Yang, Arsalan Mousavian, Abhishek Gupta, and Dieter Fox. Learning robust real-world dexterous grasping policies via implicit shape augmentation. In _6th Annual Conference on Robot Learning_ . 2 

- [10] Sammy Christen, Muhammed Kocabas, Emre Aksan, Jemin Hwangbo, Jie Song, and Otmar Hilliges. D-grasp: Physically plausible dynamic grasp synthesis for hand-object interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2022. 3 

- [11] Djork-Arn´e Clevert, Thomas Unterthiner, and Sepp Hochreiter. Fast and accurate deep network learning by exponential linear units (elus). _arXiv preprint arXiv:1511.07289_ , 2015. 15 

- [12] Enric Corona, Albert Pumarola, Guillem Alenya, Francesc Moreno-Noguer, and Gr´egory Rogez. Ganhand: Predicting human grasp affordances in multi-object scenes. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 5031–5041, 2020. 3 

- [13] Laurent Dinh, David Krueger, and Yoshua Bengio. Nice: Non-linear independent components estimation. _arXiv preprint arXiv:1410.8516_ , 2014. 2, 3 

- [14] Laurent Dinh, Jascha Sohl-Dickstein, and Samy Bengio. Density estimation using real nvp. _arXiv preprint arXiv:1605.08803_ , 2016. 2, 3 

- [15] Mehmet R. Dogar and Siddhartha S. Srinivasa. Pushgrasping with dexterous hands: Mechanics and a method. In _2010 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 2123–2130, 2010. 3 

- [16] Luca Falorsi, Pim de Haan, Tim R Davidson, and Patrick Forr´e. Reparameterizing distributions on lie groups. In _The 22nd International Conference on Artificial Intelligence and Statistics_ , pages 3244–3253. PMLR, 2019. 2, 3, 7, 14, 18 

- [17] Hongjie Fang, Hao-Shu Fang, Sheng Xu, and Cewu Lu. Transcg: A large-scale real-world dataset for transparent object depth completion and a grasping baseline. _IEEE Robotics and Automation Letters_ , pages 1–8, 2022. 2 

- [18] Hao-Shu Fang, Chenxi Wang, Minghao Gou, and Cewu Lu. Graspnet-1billion: A large-scale benchmark for general object grasping. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 11444– 11453, 2020. 2 

- [19] Carlo Ferrari and John F Canny. Planning optimal grasps. In _ICRA_ , volume 3, page 6, 1992. 7, 17 

- [20] K. M. Gorski, E. Hivon, A. J. Banday, B. D. Wandelt, F. K. Hansen, M. Reinecke, and M. Bartelmann. HEALPix: A framework for high-resolution discretization and fast analysis of data distributed on the sphere. _The Astrophysical Journal_ , 622(2):759–771, apr 2005. 5 

- [21] Minghao Gou, Hao-Shu Fang, Zhanda Zhu, Sheng Xu, Chenxi Wang, and Cewu Lu. Rgb matters: Learning 7-dof grasp poses on monocular rgbd images. In _Proceedings of the International Conference on Robotics and Automation (ICRA)_ , 2021. 2 

- [22] Patrick Grady, Chengcheng Tang, Christopher D. Twigg, Minh Vo, Samarth Brahmbhatt, and Charles C. Kemp. ContactOpt: Optimizing contact to improve grasps. In _Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2021. 3 

- [23] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In _International conference on machine learning_ , pages 1861–1870. PMLR, 2018. 15 

- [24] Hanwen Jiang, Shaowei Liu, Jiashun Wang, and Xiaolong Wang. Hand-object contact consistency reasoning for human grasps generation. In _Proceedings of the International Conference on Computer Vision_ , 2021. 2, 3, 5, 6, 7, 13 

- [25] Durk P Kingma and Prafulla Dhariwal. Glow: Generative flow with invertible 1x1 convolutions. _Advances in neural information processing systems_ , 31, 2018. 2, 3, 5, 13 

- [26] Nikos Kolotouros, Georgios Pavlakos, Dinesh Jayaraman, and Kostas Daniilidis. Probabilistic modeling for human mesh recovery. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 11605–11614, 2021. 3, 7, 13, 14, 18 

- [27] Puhao Li, Tengyu Liu, Yuyang Li, Yiran Geng, Yixin Zhu, Yaodong Yang, and Siyuan Huang. Gendexgrasp: Generalizable dexterous grasping. _arXiv preprint arXiv:2210.00722_ , 2022. 3 

- [28] Min Liu, Zherong Pan, Kai Xu, Kanishka Ganguly, and Dinesh Manocha. Deep differentiable grasp planner for high- 

9 

dof grippers. _arXiv preprint arXiv:2002.01530_ , 2020. 3, 7, 12, 13 

- [29] Min Liu, Zherong Pan, Kai Xu, Kanishka Ganguly, and Dinesh Manocha. Deep differentiable grasp planner for highdof grippers. _CoRR_ , abs/2002.01530, 2020. 3 

- [30] Tengyu Liu, Zeyu Liu, Ziyuan Jiao, Yixin Zhu, and SongChun Zhu. Synthesizing diverse and physically stable grasps with arbitrary hand structures by differentiable force closure estimation. _CoRR_ , abs/2104.09194, 2021. 2, 3, 12 

- [31] Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, and Li Yi. Hoi4d: A 4d egocentric dataset for category-level humanobject interaction. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21013–21022, 2022. 2 

- [32] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel State. Isaac gym: High performance gpu-based physics simulation for robot learning, 2021. 3 

- [33] Priyanka Mandikal and Kristen Grauman. Dexvip: Learning dexterous grasping with human hand pose priors from video. In _Conference on Robot Learning (CoRL)_ , 2021. 3 

- [34] Priyanka Mandikal and Kristen Grauman. Learning dexterous grasping with object-centric visual affordances. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2021. 3 

- [35] A.T. Miller and P.K. Allen. Graspit! a versatile simulator for robotic grasping. _Robotics Automation Magazine, IEEE_ , 11(4):110 – 122, dec. 2004. 2, 3 

- [36] Kieran A Murphy, Carlos Esteves, Varun Jampani, Srikumar Ramalingam, and Ameesh Makadia. Implicit-pdf: Nonparametric representation of probability distributions on the rotation manifold. In _Proceedings of the 38th International Conference on Machine Learning_ , pages 7882–7893, 2021. 2, 3, 4, 5, 13, 18 

- [37] Krishna Murthy Jatavallabhula, Edward Smith, JeanFrancois Lafleche, Clement Fuji Tsang, Artem Rozantsev, Wenzheng Chen, Tommy Xiang, Rev Lebaredian, and Sanja Fidler. Kaolin: A pytorch library for accelerating 3d deep learning research. _arXiv e-prints_ , pages arXiv–1911, 2019. 12 

- [38] George Papamakarios, Eric T Nalisnick, Danilo Jimenez Rezende, Shakir Mohamed, and Balaji Lakshminarayanan. Normalizing flows for probabilistic modeling and inference. _J. Mach. Learn. Res._ , 22(57):1–64, 2021. 2 

- [39] Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas. Pointnet: Deep learning on point sets for 3d classification and segmentation. _arXiv preprint arXiv:1612.00593_ , 2016. 5, 6, 13 

- [40] Charles R Qi, Li Yi, Hao Su, and Leonidas J Guibas. Pointnet++: Deep hierarchical feature learning on point sets in a metric space. _arXiv preprint arXiv:1706.02413_ , 2017. 4, 13 

- [41] Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, and Xiaolong Wang. Generalizable point cloud policy learning for sim-to-real dexterous manipulation. In _6th Annual Conference on Robot Learning_ . 2 

- [42] Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, and Xiaolong Wang. Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. _arXiv preprint arXiv:2211.09423_ , 2022. 3 

- [43] Yuzhe Qin, Yueh-Hua, Shaowei Liu, Hanwen Jiang, Rui Yang, Yang Fu, and Xiaolong Wang. Dexmv: Imitation learn for dexterous manipulation from human videos, 2021. 2, 3 

- [44] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In _International Conference on Machine Learning_ , pages 8748–8763. PMLR, 2021. 8 

- [45] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 3, 7, 8, 15, 18 

- [46] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Bj¨orn Ommer. High-resolution image synthesis with latent diffusion models. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 10684–10695, 2022. 2 

- [47] Javier Romero, Dimitrios Tzionas, and Michael J. Black. Embodied hands: Modeling and capturing hands and bodies together. _ACM TOG_ , 2017. 13 

- [48] Carlos Rosales, Llu´ıs Ros, Josep M. Porta, and Ra´ul Su´arez. Synthesizing grasp configurations with specified contact regions. _The International Journal of Robotics Research_ , 30(4):431–443, 2011. 3 

- [49] St´ephane Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured prediction to noregret online learning. In _Proceedings of the fourteenth international conference on artificial intelligence and statistics_ , pages 627–635. JMLR Workshop and Conference Proceedings, 2011. 4, 6, 16 

- [50] Reuven Rubinstein. The cross-entropy method for combinatorial and continuous optimization. _Methodology and computing in applied probability_ , 1(2):127–190, 1999. 15 

- [51] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S Sara Mahdavi, Rapha Gontijo Lopes, et al. Photorealistic text-to-image diffusion models with deep language understanding. _arXiv preprint arXiv:2205.11487_ , 2022. 2 

- [52] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 4, 6, 7, 8, 15, 16, 18 

- [53] Qijin She, Ruizhen Hu, Juzhan Xu, Min Liu, Kai Xu, and Hui Huang. Learning high-dof reaching-and-grasping via dynamic representation of gripper-object interaction. _arXiv preprint arXiv:2204.13998_ , 2022. 3, 15, 18 

- [54] Martin Sundermeyer, Arsalan Mousavian, Rudolph Triebel, and Dieter Fox. Contact-graspnet: Efficient 6-dof grasp generation in cluttered scenes. 2021. 2 

- [55] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ_ 

10 

_international conference on intelligent robots and systems_ , pages 5026–5033. IEEE, 2012. 12 

- [56] Chenxi Wang, Hao-Shu Fang, Minghao Gou, Hongjie Fang, Jin Gao, and Cewu Lu. Graspness discovery in clutters for fast and accurate grasp detection. In _Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)_ , pages 15964–15973, October 2021. 2 

- [57] Ruicheng Wang, Jialiang Zhang, Jiayi Chen, Yinzhen Xu, Puhao Li, Tengyu Liu, and He Wang. Dexgraspnet: A large-scale robotic dexterous grasp dataset for general objects based on simulation. _arXiv preprint arXiv:2210.02697_ , 2022. 3, 6, 12 

- [58] Xinyue Wei, Minghua Liu, Zhan Ling, and Hao Su. Approximate convex decomposition for 3d meshes with collision-aware concavity and tree search. _arXiv preprint arXiv:2205.02961_ , 2022. 12 

- [59] Yueh-Hua Wu, Jiashun Wang, and Xiaolong Wang. Learning generalizable dexterous manipulation from human grasp affordance. _arXiv preprint arXiv:2204.02320_ , 2022. 2, 3, 6, 7, 8, 14, 15, 18 

- [60] Anna Yershova, Swati Jain, Steven M. Lavalle, and Julie C. Mitchell. Generating uniform incremental grids on so(3) using the hopf fibration. _International Journal of Robotics Research_ , 29(7):801–812, June 2010. 5 

- [61] Anna Yershova, Swati Jain, Steven M. LaValle, and Julie C. Mitchell. Generating uniform incremental grids on so(3) using the hopf fibration. _The International Journal of Robotics Research_ , 29(7):801–812, 2010. PMID: 20607113. 18 

- [62] Tianqiang Zhu, Rina Wu, Xiangbo Lin, and Yi Sun. Toward human-like grasp: Dexterous grasping via semantic representation of object-hand. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 15741– 15751, 2021. 5, 12 

11 

## **Supplementary Material** 

**Abstract** In this supplementary material, we provide our dataset generation method in Section A, details about our method, baselines, and implementation in Section B, details about the experiments in Section C, and more quantitative and qualitative experiment results, in Section D. For more visualization of our generated dataset and grasping demonstrations, please refer to the supplementary video. 

## **A. Dataset Generation** 

In order to train our vision model and RL policy to be universal and diverse in the table-top setting, we need a dexterous grasping dataset that provides numerous object instances and holds diverse grasping labels. Moreover, each grasp should correspond to a physically plausible tabletop scene that is free of any penetration. We synthesized this dataset using a similar method from [57]. 

**Object Preperation** Our object dataset is composed of 5519 object instances in 133 categories selected from ShapeNet, [28], and [55]. Each object instance is canonicalized into a unit sphere, then re-scaled by each factor in _{_ 0 _._ 06 _,_ 0 _._ 08 _,_ 0 _._ 1 _,_ 0 _._ 12 _,_ 0 _._ 15 _}_ . We decompose our meshes into convex pieces using [58]. 



Figure 6. Our object dataset contains more than five thousand objects from various categories. These are the visualization of some decomposed meshes. 

**Grasp Generation** Our table-top scene starts with a flat plane which overlaps with the _z_ = 0 plane of the world reference frame. For each generation environment, we randomly select an object from the pool of our training in- 

stances, randomly rotate it, then let it fall onto the plane from a high place. Next, we randomly initialize a dexterous gripper in an area above the object, and let it face the object. Then, the initial gripper pose is optimized into a plausible grasp in a 6000-step optimization process, guided by an energy function. Finally, the object’s pose and the gripper’s translation, rotation, and joint angles are saved for further validation. 

**Energy Function** We base our energy function on [30], and modified it to suit the table-top setting. It is composed of the following terms. 1) _E_ fc: A differentiable force closure estimator that encourages physical stability; 2) _E_ dis: Attraction energy to ensure contact; 3) _E_ pen: Repulsion energy to elliminate penetration; 4) _E_ tpen: L1 energy that keeps the gripper above the table; 5) _E_ joints: Regularization term to enforce joint limits; 6) _E_ spen: Self penetration energy inspired by [62]. The total energy is a linear combination of the six terms. 



**Grasp Validation** We filter our generated dataset by physical stability and penetration depth. A grasp is considered physically stable if it can resist gravity in all 6 axisaligned directions in the IsaacGym simulator. Moreover, we discard grasps that penetrate the object for more than 1mm. We ran 1000 generations for each object instance, and harvested 1.12 million valid grasps in total. This tabletop dataset features stability and diversity, which empowers our models to learn object-agnostic dexterous grasping in a table-top scene. 

**Hand SDF Calculation** The signed distance function from the object point cloud to the hand mesh is needed when calculating the penetration energy. However, this forms a batched points-to-mesh distance calculation problem with different meshes, which is hard to compute. So we add some tricks to speed up this calculation. First, we use the collision mesh of the Shadowhand, which is composed of articulation of simple primitives namely boxes and capsules. Second, for a batch of object point clouds, we consider each link of the hand respectively. Third, we use forward kinematics to transform the object point clouds into the link’s local reference frame. This operation turns the problem into a points-to-mesh distance calculation with a single mesh. The meshes for boxes are simple, so we use Kaolin [37] to compute points-to-mesh distances. As for capsules, the signed distance functions can be defined analytically. Finally, for each point, we take the minimal signed distance across all links to get the signed distance from that point to the complete hand collision mesh. 

12 

## **B. Method and Implementation Details** 

### **B.1. Goal Proposal Generation** 

#### **B.1.1 Details about Our Method** 

**GraspIPDF:** The original IPDF [36] is a probabilistic model over **SO(3)** that maps a pair of input and rotation, _i.e_ ., ( _X , R_ ), where the input _X_ in IPDF is an image, to an unnormalized joint log probability that indicates the likelihood of this pair. Following this work, we implement our GraspIPDF as a function _f_ ( _X_ 0 _, R_ ) : R<sup>_N×_3</sup> _×_ **SO(3)** _→_ R. We choose PointNet++ [40] to extract a global feature from the input point cloud _X_ 0, and concatenate it with rotation representation using the same positional encoding in [36]. The concatenated feature is processed by an MLP with layer sizes (256 _,_ 256 _,_ 256) to output _f_ ( _X_ 0 _, R_ ) as formulated in the paper. 

**GraspGlow:** We use Glow [25] to implement normalizing flow in this part. Glow implements its bijective transformation _f_ : R<sup>3+</sup><sup>_K_</sup> _→_ R<sup>3+</sup><sup>_K_</sup> as the composition of several blocks, where each block consists of three parts: actnorm, 1 _×_ 1 convolution, and affine coupling layer. 

Our implementation of actnorm and 1 _×_ 1 convolution is similar to the implementation in Glow, and the only difference is that our flow is used to transform a single vector of R<sup>3+</sup><sup>_K_</sup> instead of an image. Actnorm is a linear function _f_ actnorm( _x_ ) = _x/σθ_ + _µθ_ where _µθ, σθ ∈_ R<sup>3+</sup><sup>_K_</sup> are initialized using the first batch’s mean and standard deviation and then optimized with gradient descent like other parameters. 1 _×_ 1 convolution, which can be written as _f_ conv( _x_ ) = _Wx_ where _W_ is a (3+ _K_ ) _×_ (3+ _K_ ) invertible matrix, is a linear transformation used as a generalization of a permutation operation. To constraint _W_ to be invertible, _W_ is parametrized with LU decomposition _W_ = _PL_ ( _U_ + _S_ ) where _P_ is a random orthogonal matrix fixed in the training process, _L_ is a lower triangular matrix with ones on the diagonal, _U_ is an upper triangular matrix with zeros on the diagonal, and _S_ is a diagonal matrix whose diagonal elements are ensured to be positive using exp. We modify the affine coupling layer in a similar way to ProHMR [26], which can be described as follows: 



where _x_ is the input of the transformation, _c ∈_ **R**<sup>_c_</sup> is the feature extracted by PointNet, _x_ 1 is the first half dimensions of _x_ and _x_ 2 is the last half dimensions. 

In GraspGlow, we compose 21 blocks described above, and the NNs in each block’s coupling layer has 2 residual blocks containing MLPs with two layers, and the number of hidden dimensions is 64. The activation function is ReLU and we use batch normalization in MLPs and the probability of dropout is 0.5. For more details, we refer the reader to ProHMR [26]’s code as we use their implementation of conditional Glow. 

**ContactNet:** The ContactNet has 2 independent PointNet [39] modules respectively for the canonicalized object point cloud _X_<sup>˜</sup> and the hand point cloud _XH_ sampled from the hand mesh constructed by the forward kinematics. The global feature from the hand is broadcast and concatenated to the per-point feature of the object point cloud. Afterward, the feature goes through an MLP with layer sizes (1024 _,_ 512 _,_ 512 _,_ 256 _,_ 256 _,_ 128 _,_ 128 _,_ 10) to output the 10-bin-discretized contact map per-point prediction. The discretization is found to greatly boost the robustness of our ContactNet. 

#### **B.1.2 Details about Baselines** 

**GraspTTA:** GraspTTA [24] proposed a two-stage framework to synthesize grasps for MANO [47]. They designed a CVAE and a ContactNet to perform the tasks. During training, the CVAE learns to reconstruct the grasp dataset, and the ContactNet learns a mapping from the object and hand point cloud to the object’s contact map. During testing, in the first stage, the CVAE takes the object point cloud’s feature as a condition, samples a latent vector from the Gaussian distribution, and outputs the hand rotation, translation, and parameters. They use these to reconstruct the hand mesh. In the second stage, the ContactNet takes the object and hand point cloud, and predicts a target contact map on the objects. The consistency energy is defined as the MSE between the actual contact map and the target contact map predicted by the contact net. Using this energy, the hand is optimized toward the target in a test-time adaptation process. Note that in their work, the target contact map is recalculated in every optimization step. We also use test-time adaptation in our pipeline, but only calculate the target contact map in the first iteration to save time. 

**DDG:** Deep Differentiable Grasp (DDG) [28] takes 5 depth images of the object and regresses the translation, rotation, and joint angles of the ShadowHand. The learning process is divided into two stages. In the first stage, only a min-of-N loss is used for grasp pose regression. In the second stage, other loss functions are added to encourage contact, avoid penetration, and improve grasp quality. It is important to note that, the original method doesn’t take the 

13 

table as input. They assume that all depth images are taken in the object reference frame, and for each set of depth images, 100 ground-truth grasps are required to define the min-of-N regression loss. However, if we change this setting and take the depth images in the table reference frame, then only 15 ground-truth grasps are available for each set of images on average. This is because when we synthesized data for each object, the table planes are randomly chosen in each generation process. So in this experiment, we preserved their original settings without the table. In evaluation, we don’t filter grasps that have large table penetration depth for this method, which makes the problem easier, and prove that our method still out-perform theirs. 

**ReLie:** ReLie [16] proposes a general way to perform normalizing flow on Lie groups using Lie algebra, and in **SO(3)** this equals to using the axis-angle representation **v** = _θ_ **n** where _θ_ is the angle of the rotation and that **n** is a unit vector representing the axis of rotation. In their implementation, the normalizing flow is performed on R<sup>3</sup> and then the samples are transformed using tanh( _·_ ) and multiplied by _r_ , so that the length of the sampled vector is less than _r_ , and at last, the transformed samples are converted to rotation using the exponential map. Note that for surjectivity, they sacrifice invertibility and set _r_ to 1 _._ 6 _π_ . In our experiment, we add those three dimensions to GraspGlow so that the hand root rotation, translation, and joint angles can be sampled jointly. The problem with this method is that it suffers from discontinuity of the axis angle representation and that the lack of bijectivity is also harmful to the learning process. 

**ProHMR:** ProHMR [26] proposes to use a 6D representation of **SO(3)** , which is the first two columns of the rotation matrix, to avoid discontinuity. In their method, normalizing flow is performed on R<sup>6</sup> and the samples are projected to the manifold of **SO(3)** afterward. In our experiment, we add those six dimensions to GraspGlow similar to the baseline of ReLie, and to make the samples close to the **SO(3)** manifold, we also add the orthogonal loss following ProHMR. The problem with this method is that the projection is an infinite-to-one mapping so that the probability of a specific rotation is intractable, so theoretically the normalizing flow can place infinite probability to the **SO(3)** manifold without learning distribution on **SO(3)** to get infinitely low NLL. 

### **B.2. Goal-conditioned Dexterous Grasping Policy** 

#### **B.2.1 Details about Our Method** 

As we introduced in Sec. 3.3.2, we use PPO to update the teacher policy. We also adopt the technique in ILAD [59] 

which jointly learns object geometric representation by updating the PointNet using behavior cloning objective during RL policy training. We further propose three important techniques including state canonicalization, object curriculum learning, and joint training object classification to update the PointNet in our network. 

**Reward Function:** To ensure proper interaction between the robot hand and the object and encourage the robot to grasp the object according to the input grasping goal pose, we define a novel goal-conditioned reward function. Since we aim to solve the dexterous manipulation problem with pure RL, the reward design is crucial. Note that all the _ω∗∗_ here are hyper-parameters. 

The goal pose reward _r_ goal encourages the robot hand to reach the input grasping goal pose. It measures the weighted sum of distances between current robot joint angles _qj_ and goal joint angles _qj_<sup>_g_,andthedistancebetween</sup> hand root pose ( _t_<sup>_obj_</sup> _h_<sup>_, R_</sup> _h_<sup>_obj_)intheobjectreferenceframe</sup> and the goal hand root pose ( _t_<sup>_g_</sup> _h_<sup>_, R_</sup> _h_<sup>_g_) :</sup> 



_MRhobj_ and _MRh_<sup>_g_are matrices of the object relative hand</sup> rotation and goal hand rotation. The _Lrot_ here stands for the axis angle from goal hand rotation to object relative hand rotation, and is formulated as follows: 



The reaching reward _r_ reach encourages the robot fingers to reach the object. Here, **x** finger and **x** obj denote the position of each finger and object: 



The lifting reward _r_ lift encourages the robot hand to lift the object when the fingers are close enough to the object and the robot hand is considered to reach the target goal grasp pose. _f_ is a flag to judge whether the robot reaches the lifting condition: _f_ = **Is** (<sup>�</sup><sup>_J_</sup> _j_ =1<sup>_ωg,j∥_</sup><sup>**x**</sup> _j_<sup>_obj_</sup> _−_ **x**<sup>_obj_</sup> _g,j_<sup>_∥_2</sup><sup>_<_</sup> _λf_ 1)+ **Is** (<sup>�</sup> _∥_ **x** finger _−_ **x** obj _∥_ 2 _< λf_ 2)+ **Is** ( _d_ obj _> λ_ 0). Here, _d_ obj = _∥_ **x** obj _−_ **x** target _∥_ 2, where **x** obj and **x** target are object position and target position. _az_ is the scaled force applied to the hand root along the z-axis ( _ωl >_ 0). 



The moving reward _r_ move encourages the object to reach the target and it will give a bonus term when the object is 

14 

lifted very close to the target: 



Finally, we add each component and formulate our reward function as follows: 



**Details of Object Curriculum Learning:** For OCL (Object Curriculum Learning) experiments in Sec. 4.3 in the main paper, here is the detail of the curriculum. 

For 1-stage OCL we randomly choose three different categories’ objects and do three experiments. Each time first we train on one object and then train on all the categories. 

For 2-stage OCL we randomly choose three categories and do three experiments. Each time first we train on one object from each category, then train on the category where the object is from, and last train on all the categories. 

For 3-stage OCL, we do two experiments. The 3 representative categories we use in the first experiment are (toy car, bottle, and camera). The 3 representative categories we use in the second experiment are the (light bulb, cereal box, and toy airplane). We first train on one object, then train on the category of the object, then train on 3 representative categories, and last train on all the categories. 

**Network Architecture:** The MLP in teacher policy _πE_ and student policy _πS_ consists of 4 hidden layers (1024, 1024, 512, 512). The network structure of the PointNet in both the _πE_ and _πS_ is (1024, 512, 64). We use the exponential linear unit (ELU) [11] as the activation function. 

**PPO** PPO [52] is a popular model-free on-policy RL method. We use PPO together with our designed goalconditioned reward function as our RL baseline. 

**DAPG** Demo Augmented Policy Gradient (DAPG) [45] is a popular imitation learning (IL) method that leverages expert demonstrations to reduce sample complexity. Followed by ILAD [59], we use motion planning to generate demonstrations from our goal grasp label dataset. We use our designed goal-conditioned reward function in this method. 

**ILAD** ILAD [59] is an imitation learning method that improves the generalizability of DAPG. ILAD proposes a novel imitation learning objective on top of DAPG and it jointly learns the geometric representation of the object using behavior cloning from the generated demonstrations during policy learning. For this method, we use the same generated demonstrations as in DAPG and use our designed goal-conditioned reward function. 

**IBS-Grasp** IBS-Grasp [53] propose an effective representation of the grasping state called Interaction Bisector Surface (IBS) characterizing the spatial interaction between the robot hand and the object. The IBS representation, together with a novel vector-based reward and an effective training strategy, facilitates learning a strong control model of dexterous grasping with good sample efficiency and cross-category generalizability. It uses SAC [23]to train the policy. Note that we evaluate the baseline using the official code which uses the Pybullet simulator because it’s hard to do the proposed fast IBS approximation in Isaac gym. Additionally, it cannot train under the goal-conditioned setting using the proposed reward function. 

#### **B.2.2 Details about Baselines** 

**MP (Motion Planning)** We use cross-entropy method (CEM) [50] for motion planning given target hand joint positions _j_<sup>_g_</sup> computed from the target goal hand grasp label **_g_** using forward kinematics. The goal is to find a robot hand action sequence _a_ 1 _, ..., aK_ which generates a robot hand joint position sequence **_j_** 0<sup>_r, ...,_</sup><sup>**_j_**</sup> _K_<sup>_r_</sup> and the last robot hand joint positions **_j_** _K_<sup>_r_reaches</sup><sup>**_j_**</sup><sup>_g_.</sup> Followed by [59], the objective of the motion planning is min _a_ 1 _,...aK ∥_ **_j_** _K_<sup>_r−_</sup><sup>**_j_**</sup><sup>_g∥_2+</sup><sup>_λ∥_</sup><sup>**x**1</sup> obj<sup>_−_</sup><sup>**x**</sup><sup>_K_</sup> obj<sup>_∥_2, where</sup><sup>**x**1</sup> obj<sup>and</sup><sup>**x**</sup><sup>_K_</sup> obj are object poses at time step 1 and _K_ . This objective function encourages the robot hand to reach the goal hand grasp label as well as prevents the object from moving during the process. We use model predictive control (MPC) to execute the planned trajectories sampled from CEM process until the objective is below a threshold _δ_ . Once the process ends, we lift the robot’s hand to see whether the object falls down. 

## **C. Experiment Details** 

### **C.1. Environment Setup** 

**State Definition** The full state of the teacher policy _S_<sup>_E_</sup> = ( **_s_**<sup>_r_</sup> _t_<sup>_,_</sup><sup>**_s_**</sup><sup>_o_</sup> _t_<sup>_, XO,_</sup><sup>**_g_**).Thefullstateofthestudentpolicy</sup> _S_<sup>_S_</sup> = ( **_s_**<sup>_r_</sup> _t_<sup>_, Xt,_</sup><sup>**_g_**).Therobotstate</sup><sup>**_s_**</sup><sup>_r_isdetailedinTab.5</sup> and the object oracle state **_s_** _o_ includes the object pose, linear velocity, and angular velocity. For the pre-sampled object point cloud _X_<sup>_O_</sup> , we sample 2048 points from the object mesh. For the scene point cloud _XS_ , we only sample 1024 points from the object and the hand to speed up the training. 

**Action Space** The action space is the motor command of 24 actuators on the robotic hand. The first 6 motors control the global position and orientation of the robotic hand and the rest 18 motors control the fingers of the hand. We normalize the action range to (-1,1) based on actuator specification. 

15 

|Parameters|Description|Hyperparameter|Value|
|---|---|---|---|
|**_q_** _∈_R<sup>18</sup>|joint positions|_λ_cmap|0.02|
|**˙****_q_** _∈_R<sup>18</sup>|joint velocities|_λ_pen|500|
|**_τ_**dof _∈_R<sup>24</sup>|dof force|_λ_tpen|50|
|_x_finger _∈_R<sup>3</sup><sup>_×_5</sup>|fingertip position|_λ_spen|10|
|_α_finger _∈_R<sup>4</sup><sup>_×_5</sup>|fingertip orientation|_λ_<sup>TTA</sup><br>cmap|0.07|
|˙_x_finger _∈_R<sup>3</sup><sup>_×_5</sup><br>|fingertip linear velocities|_λ_<sup>TTA</sup><br>pen|10000|
|_ω_finger _∈_R<sup>3</sup><sup>_×_5</sup>|fingertip angular velocities|_λ_<sup>TTA</sup><br>tpen|1000|
|_F_finger _∈_R<sup>3</sup><sup>_×_5</sup><br>|fingertip force|_λ_<sup>TTA</sup><br>spen|10|
|_τ_finger _∈_R<sup>3</sup><sup>_×_5</sup>|fingertip torque|step size|0.001|
|**_t_**_∈_R<sup>3</sup>|hand root global transition|||
|_R ∈_R<sup>3</sup><sup>_×_3</sup><br>**_a_**_∈_R<sup>24</sup>|hand root global orientation<br>action|Table 6.**Hyperparameters for end-to**<br>**and test-time adaptation (lower half)**|**-end tra**<br>**.**|



Table 6. **Hyperparameters for end-to-end training (upper half) and test-time adaptation (lower half).** 

Table 5. Robot state definition. 



Figure 7. **Camera positions** 

**Camera Setup** We placed five RGBD cameras, four around the table and one above the table, as shown in Fig.7. The origin of the system is the center of the table. The positions of the five cameras are: ([0.5, 0, 0.05], [-0.5, 0, 0.05], [0, 0.5, 0.05], [0, -0.05, 0.05], [0, 0, 0.55]) and all their focus point is [0, 0, 0.05]. 

### **C.2. Training Details** 

(1) For the goal proposal generation part, we use Adam optimizer to train GraspIPDF, with a learning rate of 10<sup>_−_3</sup> and a batch size of 16. The loss Curve converges in 24 hours. In the training process of GraspGlow, we use Adam as our optimizer and the learning rate is 10<sup>_−_3</sup> . The experiment is done on an NVIDIA RTX A5000, and the batch size is set to 64 in the first stage and 32 in the second stage with 8 samples for each object. The training process consists of 160k iterations in the first stage and 8k iterations in the second stage, and it needs one day in total. ContactNet also uses Adam, with a learning rate of 10<sup>_−_3</sup> and a batch size of 128, and the normalization factor _β_ is set to 60. This module needs 8 hours of training. The hyperparameters for 

|Hyperparameter|Value|
|---|---|
|Num. envs (Isaac Gym)|1024|
|Env spacing (Isaac Gym)|1.5|
|Num. rollout steps per policy update|8|
|Num. batches per agent|4|
|Num. learning epochs|5|
|Episode length|200|
|Discount factor|0.96|
|GAE parameter|0.95|
|Entropy coeff.|0.0|
|PPO clip range|0.2|
|Learning rate|0.0003|
|Value loss coeff.|1.0|
|Max gradient norm|1.0|
|Initial noise std.|0.8|
|Desired KL|0.16|
|Clip observations|5.0|
|Clip actions|1.0|
|_ωg,q_|0.1|
|_ωg,t_|0.6|
|_ωg,R_|0.1|
|_ωr_|0.5|
|_ωl_|0.1|
|_ωm_|2|
|_ωb_|10|



Table 7. **Hyperparameters for grasping policy.** 

end-to-end training and test-time adaptation are in Tab. 6. 

(2) For the goal-conditioned dexterous grasping policy part, we use PPO [52] to learn _πE_ and then distill to _πS_ using DAgger [49]. Since some of the object meshes in the dataset are too large for dexterous grasping, we filter out some large-scale object instances. In the end, we obtain a train set of 3200 object instances and a test set of 241 object instances for the grasping execution experiments. The hyperparameters for the experiments are in Tab. 7. 

16 

### **C.3. Metric Details** 

#### **C.3.1 Metrics for Goal Proposal Generation** 

For the goal proposal generation part, we introduce seven metrics to evaluate grasp quality and two metrics to measure the diversity of our generated results. 

**Mean** _Q_ 1 _Q_ 1 [19] is defined as the minimal wrench needed to make a grasp unstable. This metric is only well defined when the grasp has exact contact and doesn’t penetrate the object, which is impossible for vision-based methods. So we relaxed the contact distance to 1cm. Moreover, if a grasp penetrates the table for more than 1cm, or has an object penetration depth larger than 5mm, then this grasp will be considered invalid, so its _Q_ 1 will be manually set to zero. 

**Object Penetration Depth** We define object penetration depth as the maximal penetration from the object’s point cloud to the hand mesh. This is calculated using the tricks we introduced in Sec. A. 

**Rotation Standard Deviation** This metric evaluates the standard deviation of rotation by first calculating the chordal L2 mean of rotation samples (argmin � _ni_ =1<sup>(</sup><sup>_||R−Ri||_</sup> _F_<sup>2),</sup> and then calculate the _R_ standard deviation between the rotation samples and the mean. This metric is used to show the diversity of rotation samples from GraspIPDF. 

**Translation and Joint Angles Standard Deviation (conditional)** These two metrics evaluate the standard deviations of translation and joint angles, given a sampled rotation from GraspIPDF, and are used to show the diversity of translation and joint angles in the grasp samples from GraspGlow. 

**Keypoint Standard Deviation** This metric evaluates the average standard deviation of 15 joint (keypoint) positions of the robotic hand. This metric is used to show the diversity of our grasp proposals generated by the whole grasp proposal generation pipeline. 

**Log-likelihood** We evaluate the log-likelihood of the ground truth grasping rotation, translation, and joint angles predicted by the model, and this metric is used to show how well the model fits the ground truth distribution. Note that for our model, we calculate _p_ ( _R, t, θ|X_ ) as _p_ ( _R|X_ ) _· p_ ( _t, θ|R_<sup>_−_1</sup> _X_ ). 

#### **C.3.2 Metrics for Goal-conditioned Grasp Execution** 

For the goal-conditioned dexterous grasping policy part, we introduce metrics to measure the success rate of grasping, as well as how strictly our policy follows the specified grasping goal. 

**Simulation Success Rate** We define the success rate as the primary measure of the grasping policy. The target position of the object is 0.3m above its initial position. The task is considered successful if the position difference between the object and the target is smaller than 0.05m at the final step of one sequence. 

**MPE (cm)** This metric is used to measure the mean joint position error between the joint position **_j_**<sup>_r_</sup> of the exact grasping pose and the joint angels **_j_**<sup>_g_</sup> computed from the input goal hand grasp label **_g_** using forward kinematics. _J_ is the number of joints. Note we only calculate the MPE for the success grasp. 



## **D. Additional Results and Analysis** 

This section contains extended results of the experiment depicted in Sec. 4. 

### **D.1. Goal-conditioned Dexterous Grasping Policy Results** 

**Goal-conditioned vs. Non-Goal-conditioned** We also conducted experiments in a non-goal-conditioned setting, which is the task of grasping objects alone. We compare our results with baselines described in Sec. B.2.2. We add MP and IBS-Grasp only in supplementary because MP cannot perform non-goal-conditioned tasks and IBS-Grasp does not have a goal-conditioned setting. To perform non-goal-conditioned tasks using our method, we simply remove the goal input and goal reward in RL training. The results are shown in Tab. 8. In non-goal-conditioned settings, our teacher policy has the highest success rate across training and all testing data sets. 

**Analysis of Quantitative Grasping Results** The metric MPE in Tab. 8 measures the deviation between each method’s interaction ending grasp and input goal grasp, as defined in Sec. C.3. The results show that except for the motion planning, our method has the lowest MPE among all the RL-based methods. Though the MPE of motion planning is the lowest, it has the lowest success rate, so it is unreliable. Especially, since our generated grasping proposal on unseen object categories is noisy, simply motion planning to the goal position cannot grasp 

17 

|Method|||goal-|conditioned|||n|on-goal-cond|itioned|
|---|---|---|---|---|---|---|---|---|---|
|||Train|||Test||Train|T|est|
||||un<br>s|seen obj<br>een cat|un|seen cat||unseen obj<br>seen cat|unseen cat|
||succ_↑_|MPE(cm)_↓_|succ_↑_|MPE(cm)|_↓_<br>succ_↑_|MPE(cm)_↓_|succ_↑_|succ_↑_|succ_↑_|
|MP|0.12|**1.2**|0.02|**1.8**|0.02|**1.8**|/|/|/|
|PPO [52]|0.14|4.4|0.11|4.9|0.09|5.8|0.24|0.21|0.17|
|DAPG [45]|0.13|8.0|0.13|7.4|0.11|9.1|0.21|0.15|0.10|
|ILAD [59]|0.25|5.1|0.22|5.3|0.20|5.6|0.32|0.26|0.23|
|IBS-Grasp [53]|/|/|/|/|/|/|0.57|0.54|0.54|
|Ours(teacher)|**0.74**|3.5|**0.71**|3.9|**0.67**|4.5|**0.79**|**0.74**|**0.71**|
|Ours (student)|0.68|3.8|0.64|4.3|0.60|4.7|0.74|0.69|0.65|



Table 8. **Results on dexterous grasping policy.** We use bold to indicate the best metric and underline to indicate the second-best metric. Note that for MP (Motion planning), “train” means optimizing on our synthetic ground truth grasp dataset and “test” means optimizing on the predicted grasp from our vision pipeline. 



Figure 8. **Diverse grasp proposals** . Here we show the diversity of our grasping pose samples. On the same row, the objects are the same, and in the same picture, the hand root rotation is also the same. It can be shown that both the rotation samples from GraspIPDF and the translation and joint angles samples from GraspGlow have high diversity. 

|Method|Log-likelihood|
|---|---|
|ReLie [16]|-1.540|
|ProHMR [26]|-1.710|
|ours (R + GL)|**10.908**|



Table 9. **Comparison on Log-likelihood of ground truth grasps.** R: GraspIPDF, GL: GraspGlow. Note that the outputted probability of flow in baselines on **SO(3)** is unnormalized and that we generate uniform grids using the method described in [61] and approximate the normalizing constant similar to IPDF [36]. 

MP but this kind of low MPE is helpless since it cannot seam the gap. On the contrary, our method can modify the generated noisy grasp goal and make the grasp possible. 

**Additional Qualitative Grasping Results** We provide a qualitative demonstration of the diverse grasp proposals in Fig. 8. Comparing the two images of each row, one can see the diverse rotation predictions of GraspIPDF. The different hands in each image demonstrate the diverse translation and articulation predictions of GraspGlow. We also provide additional qualitative grasping results in Fig. 9. The left part of the figure is the visualization of the goal hand-grasping pose. For each row, the right part is the generated grasping sequence using the left part as the grasping goal, and we select four representative stages as pictures. From top to bottom, the four featured objects are a bottle, a camera, a toy dog, and a headphone. All the objects here are in the test data set, and the grasping goals are selected from our generated grasping proposals. 

the object firmly. The gaps between hand and object in generated data lead to the minimization of the MPE of 

18 



Figure 9. **Qualitative Grasping Results** . The left side includes objects and corresponding grasping poses generated using our method, and the right side is the policy-generated grasping sequence using the left corresponding part as the grasping goal. Object categories from top to bottom: bottle, camera, toy dog, and a headphone. 

19 

