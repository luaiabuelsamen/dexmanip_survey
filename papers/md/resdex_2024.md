Preprint. 

# EFFICIENT RESIDUAL LEARNING WITH MIXTURE-OFEXPERTS FOR UNIVERSAL DEXTEROUS GRASPING 

**Ziye Huang**<sup>1</sup> **, Haoqi Yuan**<sup>1</sup> **, Yuhui Fu**<sup>1</sup> **, Zongqing Lu**<sup>1</sup><sup>_,_2</sup><sup>_†_</sup> 

1Peking University 

2Beijing Academy of Artificial Intelligence 

## ABSTRACT 

Universal dexterous grasping across diverse objects presents a fundamental yet formidable challenge in robot learning. Existing approaches using reinforcement learning (RL) to develop policies on extensive object datasets face critical limitations, including complex curriculum design for multi-task learning and limited generalization to unseen objects. To overcome these challenges, we introduce ResDex, a novel approach that integrates residual policy learning with a mixtureof-experts (MoE) framework. ResDex is distinguished by its use of geometryunaware base policies that are efficiently acquired on individual objects and capable of generalizing across a wide range of unseen objects. Our MoE framework incorporates several base policies to facilitate diverse grasping styles suitable for various objects. By learning residual actions alongside weights that combine these base policies, ResDex enables efficient multi-task RL for universal dexterous grasping. ResDex achieves state-of-the-art performance on the DexGraspNet dataset comprising 3,200 objects with an 88.8% success rate. It exhibits no generalization gap with unseen objects and demonstrates superior training efficiency, mastering all tasks within only 12 hours on a single GPU. 

## 1 INTRODUCTION 

Dexterous robotic hands (Pons et al., 1999; Shaw et al., 2023) provide advanced capabilities for complex grasping tasks, similar to those performed by human hands. However, achieving universal dexterous grasping across a wide range of objects remains a significant challenge due to the high degrees of freedom (DoFs) for dexterous hands and the high variability in object geometry in the real world. Previous works (Qin et al., 2022a; Agarwal et al., 2023) develop dexterous grasping policies using reinforcement learning (RL), but these policies are limited to a small range of objects that are similar to the training objects. To improve the scalability of universal dexterous grasping, recent studies (Chao et al., 2021; Wang et al., 2023; Hang et al., 2024) introduce datasets that contain a wide variety of objects, each labeled with grasping poses. Xu et al. (2023); Wan et al. (2023); Wu et al. (2024a) leveraged these datasets to learn universal grasping policies through a teacherstudent framework, which addresses the challenges of multi-task optimization. They first train statebased policies using RL to master all objects within the dataset, and then distill these policies into a universal vision-based policy. 

However, these approaches exhibit certain limitations. UniDexGrasp (Xu et al., 2023) involves a complicated curriculum learning design, requiring iterative training across an expanding set of objects, which significantly increases training time and necessitates careful design for the curriculum. Similarly, UniDexGrasp++ (Wan et al., 2023) requires training various state-based policies on a large number of object clusters. This not only consumes substantial training time but may also lead to overfitting, as training is conducted individually on separate object groups. In this study, we investigate _how to directly learn a multi-task dexterous grasping policy across thousands of objects_ , which enables both efficient learning and enhanced generalization. 

Residual policy learning (Silver et al., 2018; Johannink et al., 2019) offers an efficient approach to learning challenging tasks by training a policy to output residual actions using RL, where a subopti- 

> _†_ Correspondence to Zongqing Lu <zongqing.lu@pku.edu.cn>. 

1 

Preprint. 

mal base policy is provided. This approach has the potential to address the optimization challenges in multi-task RL (Wu et al., 2024b), particularly when the base policy can effectively explore all tasks. Motivated by this, we propose **ResDex** to train a residual multi-task policy for universal dexterous grasping. The key question then becomes, _how to efficiently acquire a base policy that possesses some generalizability to grasp a wide range of objects?_ Directly applying multi-task RL to all objects leads to worse results due to multi-task gradient interference (Yu et al., 2020) and requires extensive training time. Conversely, training a policy to grasp a specific object often results in poor generalization to unseen objects. 

Recent work (Agarwal et al., 2023) suggests that a blind grasping policy, relying solely on robot proprioception, can robustly grasp unseen objects placed close to the palm. This is because the policy does not overfit to specific object information, leveraging feedback from joint positions and fingertip forces to adapt to various object geometries inherently. Given this insight, we propose training geometry-unaware base policies that only observe proprioception and the 3D positions of objects to infer the object location. Experimental results demonstrate that our geometry-unaware policy, even trained on a single object, generalizes better to a broad range of objects compared to policies with full object perception. 

To enhance the diversity of grasping poses across various objects, we introduce a mixture-of-experts (MoE) approach that learns multiple base policies to represent different grasping styles. We use geometric clustering to categorize all objects and train a geometry-unaware policy for each cluster’s center. In our multi-task learning framework, we train a residual policy that not only outputs residual actions but also assigns weight to each base policy. The final control action for the robot is determined by a weighted sum of the base policies’ actions and the residual action. This method effectively diversifies grasping poses by varying the weights for the base policies, thereby adapting to different object geometries. 

ResDex achieves state-of-the-art training performance and generalization capabilities, successfully grasping 3,200 objects in DexGraspNet (Wang et al., 2023). It achieves a success rate of 88.8% across all training objects and exhibits **no generalization gap** when applied to unseen objects and categories. Additionally, ResDex demonstrates remarkable training efficiency, mastering such a wide range of tasks in only 12 hours on a single NVIDIA RTX 4090 GPU. In our ablation study, we highlight the critical roles of residual policy learning and geometry-unaware experts in enhancing multi-task learning efficiency and generalization. We also demonstrate the importance of the MoE approach in achieving proper grasping poses. 

Our main contributions can be summarized as follows: 

- We introduce ResDex, a novel residual policy learning approach that significantly addresses the problem of efficient multi-task learning and generalization for universal dexterous grasping. 

- Our technical contributions, including residual multi-task RL, geometry-unaware base policies, and a mixture of experts, demonstrate marked improvements in developing a universal grasping policy. 

- ResDex achieves state-of-the-art performance on the DexGraspNet dataset, demonstrating its superior training performance and generalization capabilities compared to existing methods. 

## 2 RELATED WORK 

**Dexterous Grasping** (Pons et al., 1999; Kappassov et al., 2015) continues to be a formidable challenge, given the high degrees of freedom in multi-fingered robotic hands and the complex geometries and physical properties of real-world objects. A fundamental task in dexterous grasping is to generate grasping poses. Recent studies have employed various methods such as contact points (Shao et al., 2020; Wu et al., 2022), affordance maps (Brahmbhatt et al., 2019; Jiang et al., 2021), natural hand annotations Wei et al. (2023); Hang et al. (2024), and grasping datasets (Chao et al., 2021; Wang et al., 2023) to train models for synthesizing hand grasping poses. While generating target grasping poses is crucial, successfully completing a grasp also requires close-loop policies that can manage the entire trajectory. In learning dexterous grasping policies, both imitation learning (Qin et al., 2022b; Mandikal & Grauman, 2022) and reinforcement learning (RL) (Rajeswaran et al., 

2 

Preprint. 

2017; Wu et al., 2024b) have shown promise. The latter offers scalable advantages across a variety of objects due to its independence from human data collection and the efficiency of simulation environments (Makoviychuk et al., 2021). Recent advancements in research explore universal dexterous grasping using RL for thousands of objects. UniDexGrasp (Xu et al., 2023) and UniDexGrasp++ (Wan et al., 2023) introduce curriculum learning and a teacher-student framework to enable training on numerous objects. UniDexFPM (Wu et al., 2024a) extends these approaches to universal functional grasping tasks. In our study, we propose an improved RL method for universal dexterous grasping that is more efficient and demonstrates superior performance and generalizability. 

**Residual Policy Learning** provides an effective approach to learn challenging RL tasks when a base policy is available. In robotics, residual policy learning is extensively applied in both manipulation (Alakuijala et al., 2021; Davchev et al., 2022; Schoettler et al., 2020) and navigation tasks (Rana et al., 2020). Typically, the residual policy is constructed upon base policies that employ classical model-based control methods (Johannink et al., 2019; Silver et al., 2018). Garcia-Hernando et al. (2020) investigates residual policy learning based on human data. GraspGF (Wu et al., 2024b) explores residual policy learning on a pre-trained score-based generative model (Vincent, 2011). Zhang et al. (2023) and Jiang et al. (2024b) explore using residual policy learning to finetune RL policies. Barekatain et al. (2019) extends residual policy learning to adaptively reweight multiple expert policies. In our work, we adopt residual policy learning to tackle the challenges in universal dexterous grasping. Our method, which integrates residual RL with a mixture of geometry-unaware experts, significantly improves multi-task learning to grasp diverse objects. 

**Mixture-of-Experts (MoE)** is initially introduced by Jacobs et al. (1991); Jordan & Jacobs (1994) and typically comprises a set of expert models alongside a gating network (Shazeer et al., 2017; Fedus et al., 2022) that learns to weight the output of each expert. Recently, the MoE framework has gained substantial interest in fields such as natural language processing (Jiang et al., 2024a) and multi-modal learning (McKinzie et al., 2024). MoE has also been applied in RL policies (Doya et al., 2002; Peng et al., 2019), where each expert policy learns a distinct probability distribution that is subsequently integrated. Recent works (Cheng et al., 2023; Celik et al., 2024) use MoE to enhance multi-task learning in robotics. In our research, we use the MoE framework to improve the diversity of grasping poses in the multi-task learning of dexterous grasping policies. Each expert within our framework is a geometry-unaware policy, trained on an individual object to develop a unique grasping style and achieve broad generalization across a variety of objects. 

## 3 PRELIMINARIES 

### 3.1 PROBLEM FORMULATION 

We consider tabletop grasping tasks using a 5-fingered ShadowHand to grasp and lift objects initially placed on a table. The hand features 18 DoFs that control a total of 22 joints, including 4 coupled joints. Our goal is to enable grasping any object within a large object set, denoted as _ω ∈_ Ω. For each object, the task is formulated as a Partially Observable Markov Decision Process (POMDP) _M_<sup>_ω_</sup> = _⟨O, S, A, T , R, U⟩_ , representing the observation space _O_ , the state space _S_ , the action space _A_ , the transition dynamics _T_ ( _st_ +1 _|st, at_ ), the reward function _R_ ( _st, at_ ), and the observation emission function _U_ ( _ot|st_ ), respectively. At each timestep _t_ , the agent observes _ot ∈O_ and takes an action _at ∈A_ , then receives a reward _rt_ = _R_ ( _st, at_ ). The environment then transitions to the next state _st_ +1 _∼T_ ( _st_ +1 _|st, at_ ). The agent’s objective is to maximize the expected return across all objects<sup>�</sup> _ω∈_ Ω<sup>E</sup> �� _tT_ =0 _−_ 1<sup>_γtrt_</sup> �, where _T_ is the time limit and _γ_ is the discount factor. 

For task learning in simulation, the observation _o ∈O_ includes: (1) Robot proprioception **_J_** _∈_ R<sup>123</sup> , including wrist position and orientation, joint positions of the hand, fingertip states and forces on fingertip sensors; (2) Object pose, including position **_b_**<sup>_p_</sup> _∈_ R<sup>3</sup> and quaternion **_b_**<sup>_q_</sup> _∈_ R<sup>4</sup> ; (3) An object code **_c_**<sup>_ω_</sup> _∈_ R<sup>64</sup> , representing the object geometry via a pre-trained PointNet (Qi et al., 2017). In real-world settings, while precise object pose is unavailable, we opt to use the object point cloud **_p_** _∈_ R<sup>_N×_3</sup> , which contains _N_ points captured by cameras. The action _a ∈A_ consists of target joint positions of the hand and the 6D force applied at the wrist. Our aim is to learn a vision-based policy _πθ_<sup>_V_(</sup><sup>_at|_</sup><sup>**_J_**</sup><sup>_t,_</sup><sup>**_p_**</sup><sup>_t, at−_1), parameterized by</sup><sup>_θ_, to maximize the expected return across all objects.</sup> 

3 

Preprint. 

DexGraspNet (Wang et al., 2023) provides a dataset that associates each object with grasping proposals. Each grasping proposal is defined as a triplet **_g_** = ( _R,_ **_t_** _,_ **_q_** ), representing the wrist’s relative rotation _R ∈_ SO(3) and position **_t_** _∈_ R<sup>3</sup> to the object and the hand’s joint positions **_q_** _∈_ R<sup>22</sup> for a successful grasp. Following Xu et al. (2023), these data can be integrated into the reward function to facilitate policy learning: 





where _rt_<sup>_task_</sup> is a predefined reward for the grasping tasks as detailed in Appendix A.1. The reward term _rt_<sup>_proposal_</sup> penalizes the distance to the grasping proposal, where _α_ is a hyperparameter adjusting its weight and **_g_** _t_ = ( _Rt,_ **_t_** _t,_ **_q_** _t_ ) represents the current relative pose of the hand to the object. 

### 3.2 THE TEACHER-STUDENT FRAMEWORK FOR UNIVERSAL DEXTEROUS GRASPING 

Directly optimizing the vision-based policy using RL faces challenges due to gradient interference (Yu et al., 2020) in multi-task RL and the high dimensionality of point cloud observations. Recent works (Xu et al., 2023; Wan et al., 2023; Wu et al., 2024a) have adopted a teacher-student framework in two stages to address these issues. First, a state-based policy _πϕ_<sup>_S_(</sup><sup>_at|_</sup><sup>**_J_**</sup><sup>_t,_</sup><sup>**_b_**</sup> _t_<sup>_p,_</sup><sup>**_b_**</sup><sup>_q_</sup> _t_<sup>_,_</sup><sup>**_c_**</sup><sup>_ω, at−_1) is trained</sup> using privileged object information to master all tasks. Then, this policy is distilled into a visionbased policy using DAgger (Ross et al., 2011), an online imitation learning method. 

To address the multi-task optimization challenge in learning the state-based policy, UniDexGrasp (Xu et al., 2023) proposed a curriculum learning approach. The RL training starts with a single object and, after a certain number of iterations, gradually includes more objects. This process continues until all objects are included and the policy achieves a high success rate. UniDexGrasp++ (Wan et al., 2023) introduced an improved method based on generalist-specialist learning (Jia et al., 2022). The entire object set is divided into groups through geometry-aware clustering. Numerous specialist state-based policies are then trained and subsequently distilled into a generalist state-based policy, with iterative training implemented through a curriculum. These methods require meticulous curriculum design and are time-consuming, as various policies are trained across different sets of objects. Additionally, their learned vision-based policies exhibit a significant decrease of about 7% in success rates when tested on unseen objects, indicating limited generalization capabilities. 

## 4 METHOD 

We propose ResDex, a framework that leverages residual policy learning combined with a mixture of experts to provide an efficient approach for universal dexterous grasping, significantly enhancing generalization capabilities. Figure 1 illustrates an overview of our framework. 

### 4.1 LEARNING GEOMETRY-UNAWARE POLICIES 

To enable efficient multi-task RL using residual policy learning, it is essential to build a base policy that can effectively explore all the involved tasks. Training a base policy directly on a single type of object often results in overfitting, which significantly decreases its generalizability to other objects. Conversely, training a policy on all objects using RL presents unique challenges, as different tasks can lead to gradient interference in the learning processes, making the training highly inefficient. 

We propose to build base policies that, while trained on a limited number of objects, can generalize effectively to a wider range of objects. Empirical insights from Agarwal et al. (2023) suggest that a blind grasping policy, trained solely on robot proprioception without specific object information, can better generalize to unseen objects. We hypothesize that limiting observations helps the policy avoid overfitting to specific object features. When a policy does not have complete information about object poses and geometric features, it tends to learn more generalizable grasping strategies and rely on the proprioceptive feedback to adjust actions. Although we cannot use a fully blind policy in our setting – as the agent must know the object’s location to approach it – we integrate this insight by proposing a **geometry-unaware base policy** , _πψ_<sup>_B_(</sup><sup>_at|_</sup><sup>**_J_**</sup><sup>_t,_</sup><sup>**_b_**</sup> _t_<sup>_p, at−_1), which uses only</sup> robot proprioception **_J_** and the 3D position of the object **_b_**<sup>_p_</sup> . 

4 

Preprint. 



<!-- Start of picture text -->
Robot  Base Policy  𝟏<br>proprioception 𝝀𝒕<br>6D object  Hyper- Base Policy  𝒌<br>pose Policy<br>Robot<br>proprioception3D object  PolicyBase  𝒂𝒕 representationObject visual  𝒂𝑡 𝑹 𝒂𝒕<br>position<br>1. Learning Geometry-unaware Experts 2. Residual Multi-Task RL with MoE<br>…<br><!-- End of picture text -->

**Figure 1:** We propose ResDex, an efficient learning framework for dexterous grasping across thousands of objects. The learning process consists of two stages: (1) For each representative object from the cluster center, we train a geometry-unaware base policy, which provides weak generalization across a broad range of objects. (2) To develop a universal policy applicable to all objects, we use residual multi-task reinforcement learning (RL) to train a hyper-policy, incorporating the base policies within a mixture-of-experts (MoE) framework. ResDex demonstrates efficient training and robust generalization to unseen objects. 

The grasping proposal reward _r_<sup>_proposal_</sup> inherently leaks the object’s geometric information, as the target relative wrist pose specifies “where to grasp on the object”. To mitigate this unwanted information leakage and enhance generalization, we replace this term with a pose reward: 



where **_q_** _t_ represents the current hand joint positions. This reward encourages the hand to reach the target joint positions, focusing on the hand pose rather than the specific region to grasp on the object. 

Experimental results (Section 5.3) show that our geometry-unaware policy, trained on a single object, demonstrates remarkable generalizability to unseen objects and significantly outperforms policies that incorporate full observations or those trained using the full grasping proposal reward. 

### 4.2 RESIDUAL MULTI-TASK REINFORCEMENT LEARNING 

While the base policy trained on a single object offers some degree of generalizability across various objects, it typically achieves a low overall success rate. To address this, we introduce residual policy learning to develop a policy that masters all objects. 

The state-based residual policy, denoted as _πϕ_<sup>_R_(</sup><sup>_at|_</sup><sup>**_J_**</sup><sup>_t,_</sup><sup>**_b_**</sup> _t_<sup>_p,_</sup><sup>**_b_**</sup><sup>_q_</sup> _t_<sup>_,_</sup><sup>**_c_**</sup><sup>_ω, at−_1),isparameterizedby</sup><sup>_ϕ_.It</sup> utilizes all available state-based observations to better maximize performance in solving POMDPs. Given the pre-trained base policy _πψ_<sup>_B_, at each timestep, the base policy uses the required observations</sup> from the complete observations to compute a base action _a_<sup>_B_</sup> _t_ = arg max _at πψ_<sup>_B_(</sup><sup>_at|_</sup><sup>**_J_**</sup><sup>_t,_</sup><sup>**_b_**</sup> _t_<sup>_p, at−_1).</sup> Simultaneously, the residual policy samples a residual action _a_<sup>_R_</sup> _t ∼ πϕ_<sup>_R_(</sup><sup>_at|_</sup><sup>**_J_**</sup><sup>_t,_</sup><sup>**_b_**</sup> _t_<sup>_p,_</sup><sup>**_b_**</sup><sup>_q_</sup> _t_<sup>_,_</sup><sup>**_c_**</sup><sup>_ω, at−_1),</sup> and these actions are combined element-wise to form the final action _at_ = _a_<sup>_B_</sup> _t_<sup>+</sup><sup>_aR_</sup> _t_<sup>.</sup> 

The generalizability of the base policy reduces the need for extensive exploration by the residual policy across diverse object geometries, making it practical to train under multi-task settings. For objects already successfully grasped by the base policy, the residual policy refines the grasping process, enhancing the success rate. For objects not successfully grasped by the base policy, the residual policy can efficiently explore in the residual action space, benefiting from the significant exploration bias provided by the base policy. We train this residual policy across the entire object set using RL, aiming to maximize the average return across all objects. Our experiments demonstrate that a single base policy, when aided by the residual policy, can achieve high success rates across thousands of objects. 

### 4.3 INCORPORATING A MIXTURE OF EXPERTS 

Utilizing diverse poses to grasp different objects is not only a crucial feature for dexterous hands but also essential for post-grasping manipulations in real-world tasks. While residual policy learning 

5 

Preprint. 

based on a single base policy can achieve commendable success rates, it often struggles to perform various grasping poses for different objects. This limitation arises because the base policy typically provides only a single grasping pose for its training object, thus posing a significant challenge for the residual policy to explore diverse grasping poses for certain objects. 

To enhance the diversity of grasping poses, we propose a mixture-of-experts (MoE) approach. In this setup, several base policies are trained, each capable of executing distinct grasping styles, and their actions can be combined to generate a variety of novel grasping poses. To acquire base policies that exhibit diverse behaviors and grasping poses, we use geometry-aware clustering (Wan et al., 2023) to divide the object set into _k_ clusters based on object shape representations. Objects at the cluster centers are used to train the base policies _{πψ_<sup>_B_</sup> _i_<sup>_}_</sup> _i_<sup>_k_</sup> =1<sup>,leveragingtheirdistinctandrepresentative</sup> shapes to foster diversified grasping styles. 

In multi-task learning, to integrate the base policies while learning residual actions, we replace the residual policy with a **hyper-policy** , denoted as _πϕ_<sup>_H_</sup> � _a_<sup>_R_</sup> _t_<sup>_,_</sup><sup>**_λ_**</sup><sup>_t|_</sup><sup>**_J_**</sup><sup>_t,_</sup><sup>**_b_**</sup> _t_<sup>_p,_</sup><sup>**_b_**</sup><sup>_q_</sup> _t_<sup>_,_</sup><sup>**_c_**</sup><sup>_ω, at−_1</sup> �. This hyper-policy predicts the residual action _a_<sup>_R_</sup> _t_<sup>_∈A_along with a weight</sup><sup>**_λ_**</sup><sup>_t∈_R</sup><sup>_k_for the MoE. At each timestep, all</sup> base policies predict base actions _{a_<sup>_B_</sup> _t,i_<sup>_}_</sup> _i_<sup>_k_</sup> =1<sup>using partial observations, and the hyper-policy samples</sup> the weights and the residual action. The final action is computed as follows: 



using a normalized weighted sum of base actions in addition to the residual action. This hyperpolicy aims at efficiently learning diverse, natural grasping poses by adjusting the MoE weights and enhancing multi-task performance through residual learning. 

### 4.4 METHOD SUMMARY 

Here, we outline the complete pipeline to train ResDex, which encompasses three training phases: **Training Base Policies:** Using the entire training set of objects, we apply K-Means clustering (Lloyd, 1982) on the PointNet Qi et al. (2017) features of objects to generate _k_ clusters. From each cluster, we select the object closest to the center and train a geometry-unaware base policy for each object using RL, as detailed in Section 4.1. 

**Training the Hyper-Policy:** We train the hyper-policy across parallel environments that span all objects in the training set, as described in Section 4.3. During the training process, the hyperpolicy is continually updated while the base policies remain fixed. To cultivate diverse and effective grasping poses while maximizing success rates, we employ a two-stage reward function: • **First stage:** We use the reward function that includes the grasping proposal reward: _r_ = _r_<sup>_task_</sup> + _r_<sup>_proposal_</sup> . This reward function guides the policy to follow the reference grasping poses provided by the dataset, resulting in more natural and human-like grasps. 

- **Second stage:** We remove the grasping proposal term in the reward function and eliminate terms that encourage approaching the object within _r_<sup>_task_</sup> , focusing solely on terms related to object lifting and task completion. This adjustment further enhances the policy’s performance by removing constraints imposed by these reward terms. Further details on the reward functions are provided in Appendix A.1. 

**Vision-based Distillation:** To learn a vision-based policy _πθ_<sup>_V_thatoperateswithoutprivileged</sup> object information, we adopt the teacher-student framework. The state-based hyper-policy serves as the teacher, and the vision-based policy to learn acts as the student. We use DAgger (Ross et al., 2011) to train, which involves iteratively collecting trajectories with the student policy and supervising it using the teacher policy. 

## 5 EXPERIMENTS 

### 5.1 EXPERIMENT SETTINGS 

We evaluate the effectiveness of our method on DexGraspNet (Wang et al., 2023), a large-scale robotic dexterous grasping dataset for thousands of everyday objects. The dataset is split into one 

6 

Preprint. 

**Table 1: Success rates of state-based policies after the first training stage.** We evaluate our method on three different random seeds. _k_ denotes the number of geometry-unaware base policies used to train the hyper-policy. 

|**Method**|**Train(%)**|**Test**<br>**Uns. Obj.**<br>**Seen Cat.**|**(%)**<br>**Uns. Cat.**|
|---|---|---|---|
|UniDexGrasp|79.4|74.3|70.8|
|UniDexGrasp++|87.9|84.3|83.1|
|ResDex (_k_ = 1)|83.2_±_1.5|82.8_±_1.0|85.1_±_0.9|
|ResDex (_k_ = 2)|82.8_±_3.9|82.6_±_3.2|85.0_±_3.3|
|ResDex (_k_ = 3)|88.1_±_1.2|88.2_±_0.4|89.3_±_1.0|
|ResDex (_k_ = 4)|**90.6**_±_**0.6**|**89.7**_±_**0.8**|**90.9**_±_**0.1**|
|ResDex (_k_ = 5)|87.6_±_0.5|87.3_±_0.8|88.1_±_0.2|
|ResDex (_k_ = 6)|88.7_±_0.6|87.8_±_0.5|88.8_±_1.1|



**Table 2: Success rates of state-based policies after the second training stage.** We evaluate our method on three different random seeds. _k_ denotes the number of geometry-unaware base policies used to train the hyper-policy. 

|**Method**|**Train(%)**|**Test**<br>**Uns. Obj.**<br>**Seen Cat.**|**(%)**<br>**Uns. Cat.**|
|---|---|---|---|
|UniDexGrasp|79.4|74.3|70.8|
|UniDexGrasp++|87.9|84.3|83.1|
|ResDex (_k_ = 1)|94.3_±_1.6|93.8_±_1.8|94.5_±_1.3|
|ResDex (_k_ = 2)|94.5_±_0.9|94.3_±_1.1|95.2_±_1.0|
|ResDex (_k_ = 3)|94.1_±_0.9|93.9_±_0.9|94.4_±_1.2|
|ResDex (_k_ = 4)|**94.6**_±_**1.6**|**94.4**_±_**1.7**|**95.4**_±_**1.0**|
|ResDex (_k_ = 5)|94.2_±_0.5|93.7_±_0.9|94.2_±_0.6|
|ResDex (_k_ = 6)|93.9_±_1.3|93.6_±_1.6|94.5_±_1.1|



training set and two test sets, including one that contains unseen objects in the seen categories and the other that contains unseen objects in unseen categories. The training set includes 3,200 object instances, while the test sets contain a total of 241 object instances. 

To train RL policies, we set up parallel simulation environments using IsaacGym (Makoviychuk et al., 2021). For vision-based distillation, we sample 512 points on each object’s mesh to provide point cloud observations. We compare our ResDex with state-of-the-art methods including UniDexGrasp (Xu et al., 2023) and UniDexGrasp++ (Wan et al., 2023). 

### 5.2 MAIN RESULTS 

Table 1 shows that our method outperforms UniDexGrasp++ by 2.7%, 5.4%, and 7.8% respectively on the training set and two test sets when _k_ = 4 after the first training stage. Our method consistently outperforms the baselines using _k_ larger than 2. Additionally, we notice that increasing _k_ leads to a slight performance gain. This indicates that using a mixture of base policies enables the hyper-policy to better align with the guidance provided by the grasping proposal reward. 

Table 2 demonstrates that the second training stage significantly boosts the success rates of all policies, regardless of the value of _k_ . Specifically, our best-performing policy ( _k_ = 4) outperforms UniDexGrasp++ by 6.7%, 10.1%, and 12.3% on the training and test sets respectively. Unlike previous methods, our approach shows no generalization gap, achieving consistent success rates on both 

7 

Preprint. 









<!-- Start of picture text -->
Cell Phone Toy Figure Bottle<br>Video Game Console Toilet Paper Mug<br><!-- End of picture text -->

**Figure 2: Generalization performance to all objects using policies with different observations and reward, each trained on a single object.** Ours: Geometry-unaware policy. Full Obs: Policy trained with the complete state-based observations. Full Pose: Policy trained using the reward function that includes the full grasping proposal reward. 

the training and test sets. This consistency indicates that our method can provide a grasping policy that is more robust and generalizable. 

During distillation, we use the hyper-policy trained with four base policies as the teacher to learn a vision-based policy. Performance of vision-based policies are presented in Table 3. Our visionbased policy outperforms UniDexGrasp++ by 3.4%, 8.9% and 10.5% in success rates on the three object sets respectively, demonstrating strong generalization capabilities to unseen objects. 

**Table 3: Success rates of vision-based policies.** 

|**Methods**|**Train(%)**|**Test**<br>**Uns. Obj.**<br>**Seen Cat.**|**(%)**<br>**Uns. Cat.**|
|---|---|---|---|
|UniDexGrasp|73.7|68.6|65.1|
|UniDexGrasp++|85.4|79.6|76.7|
|ResDex (_k_ = 4)|**88.8**|**88.5**|**87.2**|



### 5.3 ABLATION STUDY 

**Geometry-Unaware Experts.** We compare generalizability between geometry-unaware policies and policies trained with full state-based observations. We train 3 types of policies on 6 objects, including cell phone, toy figure, bottle, video game console, toilet paper and mug, and we evaluate their performance on the training set. The results are shown in Figure 2. Our geometry-unaware policies achieve higher success rates compared to other policies, achieving over 70% success rates when trained on some objects, which demonstrates remarkable generalizability. Policies with the full observations or the full grasping proposal reward demonstrate poor generalization when trained on some specific objects. 

**Residual Reinforcement Learning.** To demonstrate the multi-task learning ability provided by residual reinforcement learning, we implement an ablation method that combines base policies using a hyper-policy which only outputs the weights without residual actions. We evaluate the performance on the training set. The results, as shown in Table 4, demonstrate that for different number of base policies, the method with residual learning can notably boost the performance. 

8 

Preprint. 











<!-- Start of picture text -->
k = 1 k = 2 k = 3 k = 4<br><!-- End of picture text -->

































**Figure 3: Grasping poses achieved by hyper-policies trained with various numbers of base policies.** Each row displays grasping poses for a kettle, tape measure, mug, and headphone, respectively. Columns show hyper-policies trained with 1, 2, 3, and 4 base policies, arranged from left to right. 

**Table 4: Ablation study on residual reinforcement learning.** We assess success rates of policies on the training set. **Method** indicates the number of base policies used. **MoE** shows the results for hyper-policies without residual actions, while **MoE+Res** shows the results for policies that output both normalized weights for MoE and residual actions. 

|**Method**|_k_ = 1|_k_ = 2|_k_ = 3|_k_ = 4|_k_ = 5|_k_ = 6|
|---|---|---|---|---|---|---|
|**MoE**|61.4|71.1|79.4|80.3|72.1|81.6|
|**MoE+Res**|83.2|82.8|88.1|90.6|87.6|88.7|



**Mixture-of-Experts.** We further demonstrate that a mixture of base policies can generate better grasping poses. We assess the quality of the grasping poses executed by our policies by computing _D_ = _−_<sup>�</sup><sup>_T_</sup> _t_ =1<sup>_r_</sup> _t_<sup>_proposal_</sup> . The term _rt_<sup>_proposal_</sup> is a negative reward that punishes the difference between the current grasping pose and the grasping proposal ( _R,_ **_t_** _,_ **_q_** ). Therefore, the higher the value of _D_ , the less natural the grasping poses executed by the policy. The results, as shown in Table 5, reveal that for the hyper-policies trained over two stages, although their success rates are very close, those with more base policies generally display better grasping poses. 

Moreover, Figure 3 illustrates the various grasping poses executed by our policies with different numbers of base policies on randomly selected objects (kettle, tape measure, mug, and headphones). We observe that ResDex trained with more base policies tend to learn grasping strategies that are more appropriate and natural. 

9 

Preprint. 

**Table 5: Quality of grasping poses achieved by different policies.** We evaluate the _D_ values of ResDex policies with various _k_ on the test set of unseen objects in unseen categories. The lower _D_ means the better grasping poses achieved. 

|**Methods**|_k_ = 1|_k_ = 2|_k_ = 3|_k_ = 4|_k_ = 5|_k_ = 6|
|---|---|---|---|---|---|---|
|**_D_** _↓_|223.6|174.5|194.3|176.3|204.6|176.1|



## 6 CONCLUSION AND LIMITATIONS 

We propose ResDex for universal dexterous grasping, a framework that effectively addresses the challenges of training efficiency and generalization that are prevalent in existing methods. Our technical contributions include a residual policy learning framework designed for efficient multi-task reinforcement learning in dexterous grasping, a method to train geometry-unaware base policies that enhances generalization and facilitates exploration across multiple tasks, and an MoE framework that enriches the diversity of the learned grasping poses. We demonstrate the superior performance of ResDex compared to existing methods on the large-scale object dataset DexGraspNet, notably achieving a zero generalization gap to unseen objects. The framework also showcases promising simplicity and training efficiency, marking a significant step towards scaling up dexterous learning. 

The limitations of our work include: (1) Although we incorporate a grasping proposal reward to refine grasping poses, we have not yet considered the task as functional grasping. Future work could extend our approach to functional grasping tasks to further enhance general robotic manipulation in real-world settings. (2) We have not deployed the vision-based policy on hardware. Future efforts should focus on this aspect and overcome the sim-to-real gap. 

## REFERENCES 

Ananye Agarwal, Shagun Uppal, Kenneth Shaw, and Deepak Pathak. Dexterous functional grasping. In _7th Annual Conference on Robot Learning_ , 2023. 

- Minttu Alakuijala, Gabriel Dulac-Arnold, Julien Mairal, Jean Ponce, and Cordelia Schmid. Residual reinforcement learning from demonstrations. _arXiv preprint arXiv:2106.08050_ , 2021. 

- Mohammadamin Barekatain, Ryo Yonetani, and Masashi Hamaya. Multipolar: Multi-source policy aggregation for transfer reinforcement learning between diverse environmental dynamics. _arXiv preprint arXiv:1909.13111_ , 2019. 

- Samarth Brahmbhatt, Ankur Handa, James Hays, and Dieter Fox. Contactgrasp: Functional multifinger grasp synthesis from contact. In _2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 2386–2393. IEEE, 2019. 

- Onur Celik, Aleksandar Taranovic, and Gerhard Neumann. Acquiring diverse skills using curriculum reinforcement learning with mixture of experts. _arXiv preprint arXiv:2403.06966_ , 2024. 

- Yu-Wei Chao, Wei Yang, Yu Xiang, Pavlo Molchanov, Ankur Handa, Jonathan Tremblay, Yashraj S Narang, Karl Van Wyk, Umar Iqbal, Stan Birchfield, et al. Dexycb: A benchmark for capturing hand grasping of objects. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2021. 

- Guangran Cheng, Lu Dong, Wenzhe Cai, and Changyin Sun. Multi-task reinforcement learning with attention-based mixture of experts. _IEEE Robotics and Automation Letters_ , 8(6):3812–3819, 2023. 

- Djork-Arné Clevert. Fast and accurate deep network learning by exponential linear units (elus). _arXiv preprint arXiv:1511.07289_ , 2015. 

- Todor Davchev, Kevin Sebastian Luck, Michael Burke, Franziska Meier, Stefan Schaal, and Subramanian Ramamoorthy. Residual learning from demonstration: Adapting dmps for contact-rich manipulation. _IEEE Robotics and Automation Letters_ , 7(2):4488–4495, 2022. 

10 

Preprint. 

- Kenji Doya, Kazuyuki Samejima, Ken-ichi Katagiri, and Mitsuo Kawato. Multiple model-based reinforcement learning. _Neural computation_ , 14(6):1347–1369, 2002. 

- William Fedus, Barret Zoph, and Noam Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. _Journal of Machine Learning Research_ , 23(120):1–39, 2022. 

- Guillermo Garcia-Hernando, Edward Johns, and Tae-Kyun Kim. Physics-based dexterous manipulations with estimated hand poses and residual reinforcement learning. In _2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 9561–9568. IEEE, 2020. 

- Jinglue Hang, Xiangbo Lin, Tianqiang Zhu, Xuanheng Li, Rina Wu, Xiaohong Ma, and Yi Sun. Dexfuncgrasp: A robotic dexterous functional grasp dataset constructed from a cost-effective realsimulation annotation system. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 38, pp. 10306–10313, 2024. 

- Robert A Jacobs, Michael I Jordan, Steven J Nowlan, and Geoffrey E Hinton. Adaptive mixtures of local experts. _Neural computation_ , 3(1):79–87, 1991. 

- Zhiwei Jia, Xuanlin Li, Zhan Ling, Shuang Liu, Yiran Wu, and Hao Su. Improving policy optimization with generalist-specialist learning. In _International Conference on Machine Learning_ , 2022. 

- Albert Q Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, et al. Mixtral of experts. _arXiv preprint arXiv:2401.04088_ , 2024a. 

- Hanwen Jiang, Shaowei Liu, Jiashun Wang, and Xiaolong Wang. Hand-object contact consistency reasoning for human grasps generation. In _Proceedings of the IEEE/CVF international conference on computer vision_ , pp. 11107–11116, 2021. 

- Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, and Li Fei-Fei. Transic: Sim-to-real policy transfer by learning from online correction. _arXiv preprint arXiv:2405.10315_ , 2024b. 

- Tobias Johannink, Shikhar Bahl, Ashvin Nair, Jianlan Luo, Avinash Kumar, Matthias Loskyll, Juan Aparicio Ojea, Eugen Solowjow, and Sergey Levine. Residual reinforcement learning for robot control. In _2019 international conference on robotics and automation (ICRA)_ , pp. 6023– 6029. IEEE, 2019. 

- Michael I Jordan and Robert A Jacobs. Hierarchical mixtures of experts and the em algorithm. _Neural computation_ , 6(2):181–214, 1994. 

- Zhanat Kappassov, Juan-Antonio Corrales, and Véronique Perdereau. Tactile sensing in dexterous robot hands. _Robotics and Autonomous Systems_ , 2015. 

- Stuart Lloyd. Least squares quantization in pcm. _IEEE transactions on information theory_ , 1982. 

- Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

- Priyanka Mandikal and Kristen Grauman. Dexvip: Learning dexterous grasping with human hand pose priors from video. In _Conference on Robot Learning_ , pp. 651–661. PMLR, 2022. 

- Brandon McKinzie, Zhe Gan, Jean-Philippe Fauconnier, Sam Dodge, Bowen Zhang, Philipp Dufter, Dhruti Shah, Xianzhi Du, Futang Peng, Floris Weers, et al. Mm1: Methods, analysis & insights from multimodal llm pre-training. _arXiv preprint arXiv:2403.09611_ , 2024. 

- Xue Bin Peng, Michael Chang, Grace Zhang, Pieter Abbeel, and Sergey Levine. Mcp: Learning composable hierarchical control with multiplicative compositional policies. _Advances in neural information processing systems_ , 32, 2019. 

- Jose L Pons, R Ceres, and Friedrich Pfeiffer. Multifingered dextrous robotics hand design and control: a review. _Robotica_ , 1999. 

11 

Preprint. 

- Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas. Pointnet: Deep learning on point sets for 3d classification and segmentation. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , 2017. 

- Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, and Xiaolong Wang. Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. _Conference on Robot Learning (CoRL)_ , 2022a. 

- Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision_ , pp. 570–587. Springer, 2022b. 

- Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 

- Krishan Rana, Ben Talbot, Vibhavari Dasagi, Michael Milford, and Niko Sünderhauf. Residual reactive navigation: Combining classical and learned navigation strategies for deployment in unknown environments. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 11493–11499. IEEE, 2020. 

- Stéphane Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. In _Proceedings of the fourteenth international conference on artificial intelligence and statistics_ , 2011. 

- Gerrit Schoettler, Ashvin Nair, Jianlan Luo, Shikhar Bahl, Juan Aparicio Ojea, Eugen Solowjow, and Sergey Levine. Deep reinforcement learning for industrial insertion tasks with visual inputs and natural rewards. In _2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 5548–5555. IEEE, 2020. 

- John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 

- Lin Shao, Fabio Ferreira, Mikael Jorda, Varun Nambiar, Jianlan Luo, Eugen Solowjow, Juan Aparicio Ojea, Oussama Khatib, and Jeannette Bohg. Unigrasp: Learning a unified model to grasp with multifingered robotic hands. _IEEE Robotics and Automation Letters_ , 5(2):2286–2293, 2020. 

- Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _arXiv preprint arXiv:2309.06440_ , 2023. 

- Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. _arXiv preprint arXiv:1701.06538_ , 2017. 

- Tom Silver, Kelsey Allen, Josh Tenenbaum, and Leslie Kaelbling. Residual policy learning. _arXiv preprint arXiv:1812.06298_ , 2018. 

- Pascal Vincent. A connection between score matching and denoising autoencoders. _Neural computation_ , 2011. 

- Weikang Wan, Haoran Geng, Yun Liu, Zikang Shan, Yaodong Yang, Li Yi, and He Wang. Unidexgrasp++: Improving dexterous grasping policy learning via geometry-aware curriculum and iterative generalist-specialist learning. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pp. 3891–3902, 2023. 

- Ruicheng Wang, Jialiang Zhang, Jiayi Chen, Yinzhen Xu, Puhao Li, Tengyu Liu, and He Wang. Dexgraspnet: A large-scale robotic dexterous grasp dataset for general objects based on simulation. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 11359–11366. IEEE, 2023. 

- Wei Wei, Peng Wang, and Sizhe Wang. Generalized anthropomorphic functional grasping with minimal demonstrations. _arXiv preprint arXiv:2303.17808_ , 2023. 

12 

Preprint. 

- Albert Wu, Michelle Guo, and C Karen Liu. Learning diverse and physically feasible dexterous grasps with generative model and bilevel optimization. _arXiv preprint arXiv:2207.00195_ , 2022. 

- Tianhao Wu, Yunchong Gan, Mingdong Wu, Jingbo Cheng, Yaodong Yang, Yixin Zhu, and Hao Dong. Unidexfpm: Universal dexterous functional pre-grasp manipulation via diffusion policy. _arXiv preprint arXiv:2403.12421_ , 2024a. 

- Tianhao Wu, Mingdong Wu, Jiyao Zhang, Yunchong Gan, and Hao Dong. Learning score-based grasping primitive for human-assisting dexterous grasping. _Advances in Neural Information Processing Systems_ , 36, 2024b. 

- Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng, Yijia Weng, Jiayi Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 4737–4746, 2023. 

- Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn. Gradient surgery for multi-task learning. _Advances in Neural Information Processing Systems_ , 2020. 

- Xiang Zhang, Changhao Wang, Lingfeng Sun, Zheng Wu, Xinghao Zhu, and Masayoshi Tomizuka. Efficient sim-to-real transfer of contact-rich manipulation skills with online admittance residual learning. In _Conference on Robot Learning_ , pp. 1621–1639. PMLR, 2023. 

13 

Preprint. 

## A APPENDIX 

### A.1 SIMULATION SETUP 

We conduct all our experiments in IsaacGym (Makoviychuk et al., 2021), a GPU-accelerated platform for physics simulation and reinforcement learning. Each environment features a table that is 60 cm tall, with an object initialized 10 cm above the tabletop, which then falls onto it. The shadow hand is initialized 20 cm above the desktop. The task is to grasp the object and lift its center to 20 cm above the center of the tabletop. 

The dataset is split into one training set and two test sets. The training set contains 3,200 object instances. The test sets include 141 instances of unseen objects within seen categories from the training set and 100 instances of unseen objects in unseen categories. For state-based policies, we use PPO (Schulman et al., 2017) for training. For vision-based policies, we distill the state-based expert policy into a vision-based policy using DAgger (Ross et al., 2011). Each geometry-unaware policy is trained with 4,096 environments in parallel for 5,000 iterations. The hyper policy is trained with 11,000 environments in parallel for 20,000 iterations for every training stage. The vision-based policy is trained with 11,000 environments in parallel for 8000 iterations. 

**Reward Function for Base Policy** We use a modified goal-conditioned reward function to train geometry-unaware base policies. The reward function is defined as: 



_Xjoint_ denotes the joint positions. The _r_<sup>_pose_</sup> is defined as follows: 



_r_<sup>_task_</sup> is defined as follows: 



The _r_<sup>_reach_</sup> encourages the hand to reach the object, as it penalizes the distance between the object and different parts of the hand. Here, _Xobj_ and _Xhand_ denote the position of the object and the hand, and _Xfinger_ denotes positions of all the fingers. The _r_<sup>_reach_</sup> is defined as follows: 



The _r_<sup>_lift_</sup> encourages the hand to lift the object. It gives a positive reward when this condition can be satisfied: _f_ 1 = **1** (<sup>�</sup> _∥Xobj − Xfinger∥_ 2 _≤_ 0 _._ 6) + **1** ( _∥Xobj − Xhand∥_ 2 _≤_ 0 _._ 12). _az_ is the scaled force applied to the hand root along the z-axis. The _r_<sup>_lift_</sup> is defined as follows: 



The _r_<sup>_move_</sup> encourages the hand to move the object to the target position. _Xtarget_ denotes the target position. It gives a positive reward when this condition is satisfied: _f_ 2 = **1** (<sup>�</sup> _∥Xobj − Xfinger∥_ 2 _≤_ 0 _._ 6) + **1** ( _∥Xobj − Xhand∥_ 2 _≤_ 0 _._ 12) + **1** ( _∥_ **_q_** _− Xjoint∥_ 1 _≤_ 6). The _r_<sup>_move_</sup> is defined as follows: 



The _r_<sup>_bonus_</sup> gives an extra reward when the object is close to the target position. We denote _∥Xobj − Xtarget∥_ 2 as _dobj_ . The _r_<sup>_bonus_</sup> is defined as follows: 



**Reward Function for Hyper Policy** At the first training stage for a hyper policy, we use the goalconditioned reward function exactly the same as the one proposed in UniDexGrasp(Xu et al., 2023). 

14 

Preprint. 

At the second training stage for a hyper policy, we use a loosened reward function defined as follows: 



The definitions of _r_<sup>_lift_</sup> and _r_<sup>_bonus_</sup> are the same as those mentioned above. The _r_<sup>_move_</sup> has loosened its condition. It is defined as follows: 



### A.2 TRAINING DETAILS 

**Network Architecture** We use a MLP architecture which consists of 4 layers (1024, 1024, 512, 512) for base policies and the hyper policy. For the vision-based policy, we use a simplified PointNet (Qi et al., 2017) encoder to represent the object point cloud and apply MLPs with the same hidden layer sizes for the actor and the critic. We use ELU (Clevert, 2015) as the activation function. 

**Training Device and Training Time** All the state-based policies are trained on on a single NVIDIA RTX 4090 GPU. Training a base policy takes about 20 minutes, while training a hyper-policy takes about 11 hours. For the vision-based policy, we train on a single A800 GPU, taking about 16 hours. 

The hyperparameters of PPO and DAgger are described in Table 6 and Table 7. 

**Table 6:** Hyperparameters of PPO. 

|Name|Symbol|Value|
|---|---|---|
|Episode length|--|200|
|Num. envs (base policy)|--|4096|
|Num. envs (hyper-policy)|--|11000|
|Parallel rollout steps per iteration|--|8|
|Training epochs per iteration|--|5|
|Num. minibatches per epoch|--|4|
|Optimizer|--|Adam|
|Clip gradient norm|--|1.0|
|Initial noise std.|--|0.8|
|Clip observations|--|5.0|
|Clip actions|--|1.0|
|Learning rate|_η_|3e-4|
|Discount factor|_γ_|0.96|
|GAE lambda|_λ_|0.95|
|Clip range|_ϵ_|0.2|



**Table 7:** Hyperparameters of DAgger. 

|Name|Symbol|Value|
|---|---|---|
|Episode length|--|200|
|Num. envs|--|11000|
|Parallel rollout steps per iteration|--|1|
|Training epochs per iteration|--|5|
|Num. minibatches per epoch|--|4|
|Optimizer|--|Adam|
|Clip observations|--|5.0|
|Clip actions|--|1.0|
|Learning rate|_η_|3e-4|
|Clip range|_ϵ_|0.2|



15 

