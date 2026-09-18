1 

# DexReMoE:In-hand Reorientation of General Object via Mixtures of Experts 

Jun Wan, Xing Liu, Yunlong Dong<sup>_†_</sup> https://wj-0212.github.io/ 

**_Abstract_ —In hand object reorientation provides capability for dexterous manipulation, requiring robust control policies to manage diverse object geometries, maintain stable grasps, and execute precise complex orientation trajectories. However, prior works focus on single objects or simple geometries and struggle to generalize to complex shapes. In this work, we introduce DexReMoE (Dexterous Reorientation Mixture-of-Experts), in which multiple expert policies are trained for different complex shapes and integrated within a Mixture-of-Experts (MoE) framework, making the approach capable of generalizing across a wide range of objects. Additionally, we incorporate object category information as privileged inputs to enhance shape representation. Our framework is trained in simulation using reinforcement learning (RL) and evaluated on novel out-of-distribution objects in the most challenging scenario of reorienting objects held in the air by a downward-facing hand. In terms of the average consecutive success count, DexReMoE achieves a score of 19.5 across a diverse set of 150 objects. In comparison to the baselines, it also enhances the worst-case performance, increasing it from 0.69 to 6.05. These results underscore the scalability and adaptability of the DexReMoE framework for general-purpose in-hand reorientation.** 

## I. INTRODUCTION 

Dexterous manipulation has advanced for a few objects [1– 3], yet realizing generalizable dexterous manipulation remains a significant challenge in robotics [4]. In daily life, humans rely heavily on the remarkable versatility of their hands to perform tasks such as rearranging objects, loading dishes, tightening bolts, and slicing vegetables. Replicating this level of control in robotic systems is still extremely difficult [5]. At the heart of this problem lies in-hand object reorientation. A robot must be able to take an object presented in any initial pose and rotate it precisely to a desired target orientation. The ability to reliably reorient objects is crucial for flexible tool use. For example, a screwdriver must be correctly aligned with a screw before it can function properly. By focusing on this fundamental skill, we take a step closer to equipping robots with the adaptability and precision of the human hand. 

Recently, the development of RL [6–8] has paved the way for significant advances in dexterous manipulation research [1, 9]. In 2018, OpenAI [1] demonstrated that a purely end-to-end deep RL pipeline could endow a multi-fingered 

> _†_ Corresponding author. 

> Jun Wan and Xing Liu are with School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China 

Yunlong Dong is with Department of Automation, Tsinghua University, Beijing 100084 (e-mail: yunlongdong@mail.tsinghua.edu.cn) 

robotic hand with unprecedented dexterity in contact-rich inhand manipulation tasks, sparking a surge of interest despite the complexity of their sim-to-real transfer approach.. Building on this, DeXtreme [2] was introduced as a vision-based system trained in Isaac Gym [10] with extensive domain randomization and a learned pose estimator, successfully transferring agile reorientation policies from simulation to an Allegro Hand in the real world. Meanwhile, rapid motor adaptation relying exclusively on proprioceptive history and training on simple cylindrical objects enabled a fingertip-only controller to rotate dozens of diverse real objects about the z-axis without further fine-tuning, with stable finger gaits emerging naturally [3]. More recently, the Visual Dexterity framework, driven by a depth camera and capable of reorienting novel, complex shapes over multiple axes in real time, was presented, demonstrating generalization to unseen geometries under gravity [11]. Despite these remarkable advances, reliably reorienting complex objects under generalized conditions remains a formidable challenge [11]. 

By leveraging transfer learning, robotic systems can generalize policies learned on a limited object set to novel scenarios with minimal additional supervision [12]. The most common strategy is fine-tuning, in which pretrained parameters are adapted using only a few target-task examples. However, finetuning typically tailors policies to individual objects and can overwrite previously acquired skills, leading to catastrophic forgetting and limiting robustness across diverse geometries. Domain adaptation techniques [1, 2] have also been investigated, but these methods focus on closing the sim-to-real gap rather than on handling substantial variation in object shape. 

Another challenge is to extract meaningful object features, particularly shape information, in a computationally efficient manner. Training directly on each object’s full point cloud can capture detailed geometry [11], but the large number of points slows learning and increases resource demands. To address these issues, we adopt a low-dimensional extrinsics embedding that encodes each object’s critical properties (local surface geometry, mass distribution and pose) into a concise vector. We then extend this embedding by incorporating a pointcloud-based shape encoding together with a one-hot category vector [3]. This representation provides the controller with a unified and expressive view of each object’s physical attributes while the category information helps the router assign expert weights more effectively. 

In extensive simulation experiments involving more than hundreds of complex object models, our DexReMoE surpasses monolithic baselines in consecutive success count, conver- 

2 



Fig. 1: Visualization of DexReMoE in action. **Left:** the router adaptively allocates weights to expert policies according to the object’s geometry, enabling a coordinated action generation by multiple experts. **Right:** temporal evolution of in-hand reorientation under the same policy, showing smooth and precise rotation over time. 

gence speed, and resistance to disturbances. Moreover, it maintains these advantages when tested on objects outside the training distribution, demonstrating strong generalization and stability. These results show that a policy formed by combining multiple expert strategies and using an extrinsics embedding to encode object features can effectively tackle the challenging task of in-hand manipulation for objects with complex shapes. 

In light of the above, generalizing in-hand reorientation to objects with complex shapes is still an outstanding challenge in dexterous manipulation, our work proposes a new direction for improving generalization (Figure 1). We will release our codebase and simulation environment to facilitate further research in dexterous manipulation. In the following sections, we first review related work on object reorientation and mixture of experts methods, then describe the proposed architecture and training procedure in detail, and finally present a comprehensive experimental evaluation and analysis. 

The main contributions of this paper are summarized as follows: 

- 1) We propose DexReMoE for in-hand reorientation, enabling assignment of suitable expert policies based on object geometry to accomplish the reorientation task. This framework learns a unified control policy that achieves reliable and precise in-hand repositioning. 

- 2) We propose a novel object shape representation that integrates point-cloud encoding with a one-hot category vector within the existing input decoupling framework. We then fuse this enhanced shape descriptor with physical properties and compress the combined features into a compact vector using a low-dimensional extrinsics embedding. This enriched representation significantly increases the expressiveness of object features. 

- 3) We evaluate our method on over hundreds of objects with significant shape variation, both within and outside the training distribution. Performance is measured by consecutive success counts. Extensive experimental results for comparison and ablation study demonstrate the effectiveness of the proposed method. 

## II. RELATED WORK 

**In-Hand Dexterous Reorientation.** In-hand dexterous reorientation has been an active research area for decades [1, 2, 4, 5, 11, 14–17], with its core challenge lying in the precise coordination of finger motions to reposition, regrasp, and roll objects within constrained grasps. Early model-based methods planned stable finger trajectories using analytical representations of object and hand geometry [14], but their applicability remained limited by the complexity of real-world physics and the diversity of objects. More recently, reinforcement learning has emerged as a promising approach for complex in-hand tasks. Prior work has focused either on continuous rotations around a single axis [4, 16], or on multi-axis spins tailored to specific objects [1, 5, 17]. Studies that incorporate visual inputs [11] demonstrate that a single policy can manipulate multiple distinct objects, including those unseen during training. However, such experiments typically involve regular shapes and demand substantial training resources, so reorienting objects with complex geometries remains a significant challenge. To address this, we introduce a MoE framework consisting of a gating network and multiple expert policies, which dynamically select the most suitable expert according to object geometry to achieve reliable reorientation. **Shape Representation in Reorientation.** Accurate encoding of object geometry plays a critical role in any in-hand reorientation system. The dual demands of computational efficiency and policy generalization make it an open problem for dexterous hand manipulation. Prior work often sidesteps this challenge by choosing a single simple object. For example, Dextreme [2] focuses exclusively on a cube and therefore requires no explicit shape encoding, but it cannot extend to other geometries. Visual Dexterity [11] employs raw point clouds to represent shape, yet the sheer volume of points drives up computation and fails on highly symmetric objects, since point-cloud views remain unchanged under many rotations. Recently, purely tactile approaches learn a shape agent from fingertip torques and joint positions [18], but it demand very high-fidelity sensors. In contrast, our method extracts compact point-cloud features via PointNet++ [13], combine them with a one-hot object categories vector, and produces a lightweight 

3 



Fig. 2: An overview of our model across training. In **Base Policy Learning** , we jointly train the perception backbone _µ_ pc(based on PointNet++ [13]), _µ_ e and generalist policy _π_ base, using observations _ot_ that include the last three joint positions, commanded actions. Next, in **Experts Policy Training:** We fine-tune _π_<sup>base</sup> to obtain four expert policies _{π_<sup>ei</sup> _}_<sup>_n_</sup> _i_ =1<sup>.Then,in</sup><sup>**MoEPolicy**</sup> **Training:** We freeze the _µ_ pc, _µ_ e, and all _π_<sup>ei</sup> . Only the soft routing network _π_<sup>gate</sup> is trained to infer per-expert weights from the mesh feature embedding and object-category vector, and to compute the final action via a weighted sum of the experts’ outputs. 

expressive embedding suitable for general dexterous reorientation. 

**Mixture of Experts.** MoE was originally introduced in [19, 20], combining multiple specialized expert networks with a trainable gating module that adaptively weights each expert’s output [21, 22]. Recent advances in large language models have leveraged sparse MoE layers to route tokens dynamically into dedicated subnetworks, yielding both modularity and highly scalable inference [23, 24]. In RL, early studies demonstrated that ensembles of expert policies can capture complementary action distributions [25, 26], and more recent work has leveraged MoE to advance multi-task learning in robotics, highlighting its effectiveness in coordinating diverse control objectives [27, 28]. In this research, we adopt the MoE framework to diversify redirection strategies in a multi-task dexterous manipulation setting. Each expert is trained on a single shape category to develop its own redirection behavior, thereby fostering broad generalization across varied object 

geometries. 

III. IN HAND REORIENTATION WITH MOE 

We begin this section by outlining the overall system architecture in Section III-A. Subsequently, we detail the training process for the base policy in Section III-B, and conclude with the description of the MoE training procedure in Section III-C. 

## _A. DexReMoE_ 

We propose DexReMoE, a framework that combines category specific expert fine-tuning with shared encoder representations and MoE to provide versatile and efficient inhand reorientation across diverse object geometries. Figure 2 illustrates an overview of our framework. 

**Multi-Task Reinforcement Learning Framework.** RL formulates sequential decision making as a Markov Decision Process _M_ = ( _S, A, P, r, γ_ ), where _S_ and _A_ denote the 

4 

state and action spaces, _P_ ( _s_<sup>_′_</sup> _| s, a_ ) the transition probability, _r_ ( _s, a, s_<sup>_′_</sup> ) the immediate reward, and _γ ∈_ (0 _,_ 1) the discount factor. A stochastic policy _πθ_ ( _at | st_ ), parameterized by _θ_ , defines a distribution over actions given the current state. The learning objective is to identify parameters _θ_<sup>_∗_</sup> that maximize the expected discounted return as: 

by computing a weighted sum over the expert outputs. This modular design achieves both targeted specialization and broad generalization across diverse object shapes. 

## _B. Base Policy Training_ 

**Privileged Information.** Privileged information at time _t_ is _J_ ( _θ_ ) = E _πθ_ ��<sup>_∞_</sup> _γ_<sup>_t_</sup> _r_ ( _st, at, st_ +1)� _._ the concatenation of the object’s physical state **_e_**<sup>phys</sup> _t ∈_ R<sup>23</sup> _t_ =0 and its shape descriptor **_e_**<sup>shape</sup> _t ∈_ R<sup>38</sup> . The physical state single-task RL setting, an agent selects its is **_e_**<sup>phys</sup> _t_ = [ _m,_ **_c_** _, f, s,_ **_x_** _t,_ **_q_** _t,_ **_v_** _t,_ **_ω_** _t_ ] _,_ where _m_ is mass, **_c_** center of mass, _f_ friction coefficient, _s_ uniform _t_ according to: scale, **_x_** _t_ position, **_q_** _t_ orientation quaternion, **_v_** _t_ linear velocity, _at_ = _π_ ( _st_ ) _,_ and **_ω_** _t_ angular velocity. To obtain the shape descriptor, we sample the object’s point cloud and apply PointNet++ [13] to denotes the current state and _π_ is the learned policy. extract a 100-dimensional feature **_p_** _t_ . A learned point-cloud a diverse set of object geometries, we treat encoder _µ_ pc then maps **_p_** _t_ to a 32-dimensional embedding **_f_** _t_ . different shape category as an individual Appending the six-dimensional one-hot category vector **_c_** _∈_ task. In conventional multi-task reinforcement learning, differ- _{_ 0 _,_ 1 _}_<sup>6</sup> produces **_e_**<sup>shape</sup> _t_ = [ **_f_** _t,_ **_c_** ] _._ Concatenating **_e_**<sup>phys</sup> _t_ and ent tasks may have distinct objectives, reward formulations, or **_e_**<sup>shape</sup> _t_ yields the full privileged vector **_e_** _t_ = [ **_e_**<sup>phys</sup> _t ,_ **_e_**<sup>shape</sup> _t_ ] _,_ dynamics, even if they share the same state–action which is passed through an encoder _µ_ e to produce the 66contrast, our formulation employs a unified reward dimensional embedding **_z_** _t_ = _µ_ e( **_e_** _t_ ) _._ The resulting embedding identical state representations across all tasks. **_z_** _t_ = _µ_ e( **_e_** _t_ ) serves as the policy’s privileged input. We we construct our overall policy by combining refer to **_z_** _t_ as the extrinsics embedding and observe that it _n_ specialized sub-policies: significantly enhances generalization across diverse objects and environments. 

In the standard single-task RL setting, an agent selects its action at time _t_ according to: 

where _st_ denotes the current state and _π_ is the learned policy. To accommodate a diverse set of object geometries, we treat each substantially different shape category as an individual task. In conventional multi-task reinforcement learning, different tasks may have distinct objectives, reward formulations, or transition dynamics, even if they share the same state–action space. In contrast, our formulation employs a unified reward function and identical state representations across all tasks. 

Accordingly, we construct our overall policy by combining the outputs of _n_ specialized sub-policies: 



**Observations and Outputs.** In our formulation, we define the policy input state as the combination of the robot’s proprioceptive observation **_o_** _t_ and a privileged object encoding **_z_** _t_ . This composite representation captures both the robot’s recent behavior and essential object-specific information. The base policy _π_<sup>base</sup> receives this full state and produces an action **_a_** _t_ to be executed by the PD controller. Specifically, the observation **_o_** _t_ encodes a short temporal window of joint positions and previously applied actions: **o** _t_ = � **_q_** _t−_ 2 _,_ **_q_** _t−_ 1 _,_ **_q_** _t,_ **_a_** _t−_ 3 _,_ **_a_** _t−_ 2 _,_ **_a_** _t−_ 1� _,_ where each **_q_** _t_ denotes the joint positions at time _t_ , and **_a_** _t−k_ refers to the executed action at time _t − k_ . The policy output is then given by: **a** _t_ = _π_<sup>_base_�</sup> **o** _t,_ **z** _t_ � _._ To improve the smoothness of control, we apply exponential moving average to the action outputs rather than using them directly: **_<u>a</u>_** _t_ = _α_ **_a_** _t_ + (1 _− α_ ) **_<u>a</u>_** _t−_ 1 where _α ∈_ [0 _,_ 1] is a smoothing coefficient. Empirically, we observe that smaller values of _α_ lead to increased training difficulty due to diminished action responsiveness. 

where _g_ denotes a generic aggregation function that determines how the individual policies are integrated into a single action. In this work, we investigate both the design of the aggregation mechanism _g_ within a multi-task context and the selection of state representations _st_ that most effectively capture inter-task shape variations. 

**DexReMoE System.** An overview of our system architecture is provided in Figure 2. The learning process is divided into two stages: base policy training and the subsequent MoE policy training phase. 

In the first stage, we jointly train a base control policy _π_<sup>base</sup> , a point cloud encoder _µ_ pc, and an object encoder _µ_ e using data collected from all object categories. The point cloud encoder extracts geometric features from raw object meshes, while the object encoder fuses these features with auxiliary information, such as object class and physical parameters, to produce a compact object representation. This representation, together with the current observation, is fed into the base policy to generate control actions. 

**Reward Function.** Our reward function (Eq. (1)) is composed of several components. The first term in the reward function represents the task’s success criterion; within a fixed time horizon, each successful placement of the object at the target location yields a reward, and accumulating multiple successes encourages the dexterous hand to perform consecutive repositioning operations. However, this success-based reward alone is sparse and provides limited learning signals, making it insufficient for stable policy learning. To address that, we incorporate additional reward shaping terms to guide the learning process. Specifically, we penalize the relative distance _|δp|_ and orientation difference _|δθ|_ between the object and the target pose to encourage the agent to minimize both positional and rotational discrepancies . Moreover, we introduce a penalty on action magnitude and joint velocities 

Once training converges, we freeze both encoders and initialize a set of expert policies _{π_<sup>e</sup><sup>_i_</sup> _}_<sup>4</sup> _i_ =1<sup>using the parameters</sup> of the base policy. Each expert is then fine-tuned on data restricted to a specific shape category, allowing it to specialize in manipulation behaviors tailored to a particular class of geometries. Notably, the policy inputs remain consistent across both training stages, enabling the pre-trained encoders to be reused without modification during expert specialization. 

During deployment, a lightweight gating network is used to adaptively blend the outputs of the specialized experts. The gating module takes as input the object representation and a category vector, and produces a set of weights that indicate the relative importance of each expert. The final action is obtained 

5 

to further promote smoother control. The reward terms are mathematically expressed as: 



where _c_ success _>_ 0 is the reward for reaching the target; _c_ dist _, c_ rot _, cω, ca <_ 0 are penalty weights; _ϵ_ prevents division by zero; _n_ is the hand’s degrees of freedom; _ωi,t_ is the angular velocity of joint _i_ at time _t_ ; _ω_ clip is the velocity threshold; and _at_ is the action vector at time _t_ . 

The total reward at each timestep is then defined as: 



Our reward function does not include the penalty for the object falling, as we found during experiments that such a term suppresses exploratory actions and adversely affects the overall training performance. The proposed reward function enables direct training of reorientation policies capable of operating in air. 

**Policy Optimization.** We employ Proximal Policy Optimization [29] to simultaneously train both the policy _π_<sup>base</sup> , the embedding module _µ_ e and _µ_ pc . The weights between the policy and the critic network are shared, with an extra linear projection layer to estimate the value function. During training, each environment is initialized with an object in a random pose. Since our training directly targets in-air object manipulation, we initialize the dexterous hand with a stable grasp configuration to ensure faster convergence during training. 

## _C. MoE Training_ 

To accommodate the full spectrum of object geometries, from perfectly flat surfaces and slender elongated forms to highly intricate topologies, we enhance our base reorientation policy with a MoE architecture. Rather than relying on a single network to cover all shape variations, we introduce multiple specialist sub-networks, each dedicated to capturing specific geometric features. the gating network assigns each expert a continuous weight based on the object’s geometry, and the final control action is obtained by computing the weighted average of all expert outputs. 

**Expert Knowledge.** Each expert policy is realized as an independent neural network with its own parameter set, which enables specialization in distinct regions of the shape-action manifold. By decoupling representation learning across experts, we avoid forcing a monolithic policy to cover all geometric variations simultaneously. The total number of experts _n_ is determined by the intrinsic correlations among object classes rather than by the count of objects, thereby preventing model complexity from scaling linearly with dataset size. In our implementation, four experts share a frozen pointcloud encoder _µ_ pc to preserve a common perceptual backbone while each expert refines only its private policy head. The generalist expert is fine-tuned on a broad set of object shapes to 

provide baseline reorientation capabilities; the airplane expert specializes in handling elongated, discontinuous surfaces; the train expert focuses on slender structures with high aspect ratios; and the complex animal expert is designed to manage non-uniform surfaces and intricate topologies. This modular framework supports efficient extension or pruning as new shape categories emerge without retraining the entire ensemble. 

**Task-Specific Feature Extraction and Soft Router Formulation.** We designate the object’s geometry as the sole taskspecific feature, encoded by a compact shape descriptor **_e_**<sup>shape</sup> _t_ . This choice ensures that the extracted features capture the most salient, discriminative aspects of each object while remaining invariant throughout the reorientation process, thereby simplifying policy optimization and improving convergence. Concretely, **_e_**<sup>shape</sup> _t_ is obtained by fusing a point-cloud encoding with a one-hot category vector and compressing the result via a low-dimensional extrinsics embedding. 

The gating network _π_<sup>gate</sup> maps the shape descriptor **_e_**<sup>shape</sup> _t_ to a vector of scores, these scores are normalized via softmax to yield nonnegative weights, which we then use to perform a weighted aggregation of the experts’ outputs. We demonstrate in the following chapter through experiments that this dense soft gating converges much more reliably than hard TopK routing, since it avoids abrupt switches between experts and better accommodates sparse reward signals. To clarify the underlying mathematical structure of this mechanism, we introduce the notation and steps of the algorithm. Formally, let **_e_**<sup>shape</sup> _t ∈_ R<sup>_d_</sup> denote the shared descriptor vector and _{fi}_<sup>_n_</sup> _i_ =1<sup>beour</sup><sup>_n_expertmappings</sup><sup>_fi_:R</sup><sup>_d→_R</sup><sup>_h_.The</sup> gating network _π_<sup>gate</sup> is implemented as a two-layer MLP with learnable weight matrices _W_ 1 _∈_ R<sup>64</sup><sup>_×d_</sup> and _W_ 2 _∈_ R<sup>_n×_64</sup> , using the ELU [30] activation function between layers. The Soft Mixture-of-Experts algorithm then proceeds as follows: 

1) **Gating network.** Compute unnormalized expert scores 



and normalize to obtain routing weights 



2) **Expert evaluations.** Each expert produces 



3) **Soft aggregation.** The final output is 





We first describe the experimental setup in Section IV-A. In Section IV-B, we present our evaluation metrics and baseline methods for quantitative comparison. Next, in Section IV-C, we introduce the simulator-state-based base policy and evaluate how object geometry affects its performance. In particular, we analyze how variations in shape complexity influence the policy’s convergence and robustness across a wide range of 

6 

objects. In Section IV-D, we report ablation studies on various design choices. Then, we examine the limitations of the base policy when dealing with objects of complex geometry and present our proposed MOE framework, emphasizing its performance benefits in Section IV-E. Finally, Section IV-F uses t-SNE to cluster the gating network’s weight vectors, revealing distinct regions for varied shape complexities and coherent groupings for similar geometries. 

## _A. Experiment Setup_ 

**Simulation Setup.** We employ the IsaacGym simulator [10] to train our skill policy, planner policy and state estimator. Both simulation and control frequencies are set to 60 Hz. During training, we run 32768 parallel environments to collect samples for agent training. Related approaches typically perform object reorientation on a tabletop or with the palm oriented upward. In contrast, our configuration executes fully mid-air reorientation with the palm directed downward. This arrangement is significantly more complex and prone to failure, making the task more challenging. In our experiments, we adhere to the standard protocol by reorienting objects entirely in mid-air with target orientations randomly sampled from the SO(3) space using our custom GX11 three-fingered dexterous hand [31], a manipulator with eleven degrees of freedom.We train on a dataset of 150 object models sourced from online repositories such as Google Scanned Objects [32]. These models span a broad spectrum of intricate nonconvex geometries, including vehicles, footwear and various animal forms, ensuring comprehensive coverage of complex shape categories. 

**Reorientation Success Criterion.** We quantify manipulation performance by counting the number of consecutive successful reorientations achieved within each fixed time window. A straightforward criterion that declares success whenever the orientation error falls below a specified tolerance can be misled by incidental collisions that briefly align the object with its target pose. To eliminate these false positives, we require both precise orientation and a sustained halt at the desired configuration. At each control step, the reach criterion is considered satisfied only when the rotational distance to the goal is less than or equal to _τθ_ , each finger joint velocity remains below _τq_ , the object’s linear velocity stays under _τv_ , and its angular velocity does not exceed _τω_ . 

To guard against transient alignment, we enforce that all four conditions hold continuously throughout the final control cycle of the episode. A reorientation is deemed successful only when this sustained-hold criterion is met, ensuring the policy learns precise alignment and stable maintenance rather than relying on incidental collisions. This capability is essential in real-world tasks where the robot must maintain a tool’s pose for subsequent actions. 

## _B. Evaluation Metrics and Baseline Methods._ 

To evaluate the performance of the proposed DexReMoE algorithm, we employ five summary metrics, denoted as follows: 



Fig. 3: Top: the five worst-performing objects with their consecutive success counts _S_<sup>¯</sup> . Bottom: the five best-performing objects. 



where, _Si_ denotes the consecutive success count for object _i_ , _W_ 5 and _B_ 5 are the index sets of the five lowest- and highestperforming objects respectively, and _N_ is the total number of test objects. Table I reports these five metrics for all evaluated methods. 

To verify the superiority of our method, we use the following RL algorithms as baselines: 1) the ideal policy trained with Domain Randomization (DR) by OpenAI [1]; 2) the Privileged Feature (PrivFeat) policy [3], which uses privileged physical state information in place of raw observations; 3) the Privileged Shape (PrivShape) policy [4], which incorporates additional object shape information (e.g., point clouds) as privileged input; 4) the Adaptive Domain Randomization (ADR) policy [2], which adjusts domain parameters based on task performance; 5) the Residual Actions (Res) policy [33], which learns a residual correction on top of a pre-trained base policy for high-dimensional dexterous hand control ;6) the Sparse Mixture-of-Experts (SparseMoE) policy [21], which activates a sparse subset of experts via a noisy gating network; 7) the Switch Transformer (Switch) policy [22], which routes each input to a single expert using a learned switching mechanism; 8) the Low-Rank Expert Mixture (MLoRE) policy [34], which augments the MoE architecture with a shared convolutional path for task-invariant feature extraction, and adopts low-rank convolutional experts to reduce parameter and computational overhead; and 9) the Multi-gate Mixture-of-Experts (MMoE) policy [35], which shares expert sub-networks across tasks and employs task-specific gates to combine experts and model inter-task relationships. Both the baseline are trained with the same reward and penalty settings as our method. 

7 



Fig. 4: Comparison of Consecutive Success Count Across Baselines. (a) compares the consecutive success count of our policy against the baseline across all 100 objects, with objects ordered from lowest to highest success under our method. It is clear that our approach consistently outperforms the baseline on the majority of items. (b) focuses on the five objects that the baseline struggled with the most. While the baseline’s performance remains poor on these challenging shapes, our policy achieves substantially higher and more reliable success rates. (c) presents results for ten objects randomly selected from outside the training domain. For simpler shapes, both methods achieve similar levels of consecutive successes; however, as object complexity increases, our policy continues to maintain a clear advantage over both baseline strategies. 

## _C. Impact of Object Geometry on Base Policy Performance._ 

We tested the base policy on 100 objects from the training set in 6000 episodes. Empirically, we observe that the majority of objects can be successfully reoriented more than 15 consecutive times, with some achieving up to 23. However, a small subset of objects consistently fails to succeed even once. To better understand how object geometry affects reorientation performance, we first identify the five best-performing and five worst-performing objects under the base policy. Their shapes, along with their corresponding mean consecutive success counts _S_<sup>¯</sup> , are visualized in Figure 3. We then analyze the reorientation trajectories of the low-performing group and observe that failures frequently arise when protruding components become lodged between the fingers, preventing further rotation until the episode times out. For instance, repeated jamming occurs with airplane models, where wing tips obstruct motion, and with train model, whose elongated chassis often becomes trapped during manipulation. These outcomes suggest that objects with pronounced protrusions or extreme aspect ratios present substantial learning difficulties due to their increased shape complexity. 

## _D. Ablation Experiments_ 

In addition to the design of Soft MoE policy, we also make several critical design choices within our architecture. In this section, we examined two key design choices: the number of Experts and the inputs provided to the gating network. All experiments were conducted on the same set of 100 objects used during training to ensure a fair comparison across conditions. 

**Number of Expert Policies.** We investigated how the number of expert policies affects performance in our Soft MoE framework by comparing configurations with 1, 4, 6, and 8 expert policies. The single-expert case corresponds to a conventional base policy without any specialization. In the four-expert 



Fig. 5: Ablation Experiments. **Left** : Performance of MoE policies with varying numbers of expert policies. **Right** : Impact of different inputs to the gating network. Error bars indicate the standard deviation of the performance metric computed over 6,000 episodes. 

setup, three specialists were trained on the poorest-performing object classes while a single generalist policy addressed all others. The six-expert configuration allocates one expert per object category. Finally, the eight-expert configuration adopts a finer-grained taxonomy to further partition object types, yielding eight distinct experts. As illustrated in Figure 5(Left), the four-expert configuration unexpectedly achieves superior _S_ min and _S_<sup>¯</sup> 5 _−_ compared with both outperforming both the single-expert and the larger expert variants. We hypothesize that exceeding an optimal expert count degrades performance because routing inefficiencies and diminished per-expert data lead to imbalanced training and overfitting, which together undermine both specialization and generalization on the most challenging geometries. These findings highlight that, beyond a certain point, more experts do not necessarily translate to better performance; rather, a suitable expert count offers the best trade-off between expressivity and robustness. **Gating Network Inputs.** To assess the impact of gating 

8 

|Method||Within Tra<br>|ining D<br>|istribution<br>|||Out-o<br>|f-Distrib<br>|ution<br>||
|---|---|---|---|---|---|---|---|---|---|---|
||_S_<sup>_↑_</sup><br>min|_S_<sup>_↑_</sup><br>max|¯_S_<sup>_↑_</sup><br>5_−_|¯_S_<sup>_↑_</sup><br>5+|¯_S_<sup>_↑_</sup>|_S_<sup>_↑_</sup><br>min|_S_<sup>_↑_</sup><br>max|¯_S_<sup>_↑_</sup><br>5_−_|¯_S_<sup>_↑_</sup><br>5+|¯_S_<sup>_↑_</sup>|
|DR [1]|0.11|23.52|0.84|22.15|11.38|0.09|21.42|1.20|20.79|11.59|
|PrivFeat [3]|0.31|23.48|2.06|22.74|15.13|1.71|23.51|3.60|23.29|16.59|
|PrivShape [4]|0.41|23.5|1.59|23.12|16.93|2.59|23.42|3.97|23.21|16.25|
|ADR [2]|0.14|23.53|0.64|23.1|12.32|0.85|23.52|1.79|23.13|12.44|
|Res [33]|0.70|23.52|2.09|23.29|15.62|0.53|23.33|2.48|21.01|13.00|
|SparseMoE [21]|0.52|23.50|4.68|23.43|19.02|3.03|23.47|7.50|23.26|17.45|
|Switch [22]|0.66|23.52|2.67|23.33|18.33|2.27|23.59|5.39|23.31|16.85|
|MLoRE [34]|1.49|23.24|4.88|22.91|17.35|2.71|23.24|5.99|23.07|16.64|
|MMoE [35]|3.36|23.35|7.42|23.17|18.97|3.80|23.49|8.67|23.35|18.18|
|Ours|**6.05**|**23.56**|**7.90**|**23.43**|**19.62**|**4.11**|**23.69**|**9.14**|**23.53**|**19.12**|



TABLE I: We compare our method to several baselines in simulation under two evaluation settings: (1) _Within Training Distribution_ ; (2) _Out-of-Distribution_ . Each method is evaluated across five metrics: the minimum consecutive success count _S_ min, the maximum _S_ max, the average of the five worst-performing objects _S_<sup>¯</sup> 5 _−_ , the average of the five best-performing objects _S_ ¯5+, and the overall average _S_ ¯. Our approach performs exceptionally well on objects with complex surface geometries in both the training-distribution and out-of-distribution scenarios, significantly outperforming the baseline methods. 

network inputs on reorientation performance, we compared the full router (which ingests both point-cloud embeddings and category embeddings) against two ablated variants: one driven solely by the point-cloud embedding and another relying exclusively on the category embedding. As show in Figure 5 (Right), although the two configurations achieved similar average success counts, the model with the additional categories embedding produced noticeably better results on the worst single object and on the worst five objects. The observed improvement implies that category embeddings provide global directional cues to counteract performance drops on complex shapes, with point cloud data simultaneously refining expert probability distributions. 

## _E. Evaluation of the Soft MoE Policy_ 

**Soft MoE Policy Performance.** We first assess all methods on objects drawn from the same distribution used during policy training. To provide quantitative comparisons, Table I summarizes five key metrics: minimum and maximum single-object consecutive successes ( _S_ min, _S_ max), mean performance on the five hardest and easiest objects ( _S_<sup>¯</sup> 5 _−_ , _S_<sup>¯</sup> 5+), and the overall average ( _S_<sup>¯</sup> ). Among the baselines, MoE-based schemes (e.g., MMoE and SparseMoE) deliver respectable overall means near 19 but still suffer from low worst-case performance ( _S_ min below 1 for SparseMoE). Traditional methods such as ADR and PrivShape lag further behind, with overall averages under 17 and minimal robustness on the most challenging shapes. 

In contrast, our Soft MoE policy dramatically elevates the performance floor by raising _S_ min from under 1 to 6.05, and it matches or exceeds ceiling performance, achieving _S_ ¯5+ = 23 _._ 43 and _S_ max = 23 _._ 56. Overall, it achieves _S_ ¯ = 19 _._ 62 consecutive successes, outperforming all nine baselines while demonstrating both stronger worst-case guarantees and consistently high success across the entire object set. 

Figure 4(A) plots the consecutive-success counts for each of the 100 objects, sorted by performance under our model. For clarity, we compare only three representative baselines (ADR, PrivShape and SparseMoE) to highlight the relative 

gains. Our policy surpasses each of these methods on the vast majority of shapes, demonstrating its ability to generalize across varied surface geometries. Figure 4(B) then focuses on the five most challenging objects for these three baselines, which were previously unsolvable under their policies. With our approach, those objects become reliably reorientable with multiple consecutive successes in every trial. 

When initially reproducing the baseline DR and ADR [1, 2] under our strict success criterion, which requires maintaining a stable hold at the goal orientation, training failed to converge. Specifically, the monolithic policy never achieved reliable inhand rotations across the full spectrum of complex geometries. To restore performance, we implemented curriculum learning. This process began with a relaxed success test using a single cube, then progressively tightened the criterion while incrementally introducing all 100 objects. Only after this staged progression did the baseline achieve comparable results in our evaluation. Conversely, our approach utilizes a modular reinforcement learning framework that explicitly segregates object-centric inputs from hand-centric state-action information. This decoupled architecture not only facilitates more effective feature learning but also eliminates the necessity for curriculum training. From the initial epoch onward, the policy acquires robust reorientation behaviors within a single training phase. 

**Out-of-Distribution Robustness.** We then study the out-ofdistribution robustness of object shapes for a trained model. We begin by assessing each policy’s ability to handle object shapes that lie beyond the training distribution. Figure 4(C) shows consecutive-success counts on ten randomly selected out-of-distribution objects. For the simple objects, both our method and the baseline achieve comparable success count. However, as surface complexity increases, the baseline’s performance degrades sharply, ultimately failing entirely on some items, whereas our policy continues to deliver consistent, highsuccess count. 

As shown in Table I, the strongest baseline, MMoE, already exhibits zero-shot capability. It achieves an out-of-distribution mean of 18.18 consecutive successes. However, it still col- 

9 

lapses on the most challenging shapes, registering a minimum success count of only 3.80 and an average of 8.67 on the five hardest objects. By contrast, our method raises the minimum consecutive-success count on these difficult items to 4.11 and boosts the mean across the five most challenging objects to 9.14. 

These findings confirm that our method not only excels on familiar objects but also preserves its advantage when confronted with novel, complex geometries, achieving strong zero-shot performance without any further training or adaptation. 

## _F. Clustering Analysis of Gating Network Outputs_ 

To understand how the gating network _π_<sup>gate</sup> differentiates object geometries when assigning experts, we employed t-SNE (Figure 6) to visualize the expert assignment weight vectors produced by the gating network _π_<sup>gate</sup> after it was trained on 100 object models with rotational augmentation for 6000 times. We found that objects of different geometric complexity, as reflected by their consecutive success rates under the base policy, occupy separate regions in the embedding space. For example, objects that achieve high consecutive success rates tend to cluster in the upper-right quadrant, such as object IDs 91 and 93, while those with lower rates group in the lower-left quadrant. Moreover, objects with similar shapes form tighter clusters, for instance IDs 41 and 50 (both shoes) and IDs 19 and 57 (both sculpted human heads). These observations indicate that the gating network effectively captures geometric distinctions and assigns experts in a shape-dependent manner. 



Fig. 6: t-SNE projection of gating-network weight vectors for 100 objects. Points are colored by cluster assignment, showing that objects with different geometries occupy distinct regions while similar shapes form the same clusters. 

## V. CONCLUSION AND LIMITATIONS 

In this work, we introduced the Soft MoE policy for in-hand object reorientation and demonstrated its successful deployment across a variety of complex shapes. By leveraging multiple specialized experts, our approach efficiently adapts to differing object geometries during training. Experiments show that the Soft MoE architecture not only achieves reliable performance on known objects but also generalizes effectively 

to new, unseen shapes without additional retraining. Our results underscore the potential of Mixture-of-Experts networks in robotic policy learning. Specifically, incorporating diverse expert models enhances training efficiency, bolsters robustness against challenging object geometries, and improves overall generalization. These findings suggest that Soft MoE frameworks can serve as a powerful tool for developing adaptable, high-performing robotic manipulation strategies. 

**Limitations and Future Work:** Our reliance on manually labeled object categories limits scalability. To overcome this, we will explore multimodal large-language models to automate labeling. Moreover, we have yet to validate Soft MoE on physical hardware; conducting real-world trials is a primary goal for our next research phase. 

## REFERENCES 

- [1] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray _et al._ , “Learning dexterous in-hand manipulation,” _The International Journal of Robotics Research_ , vol. 39, no. 1, pp. 3–20, 2020. 

- [2] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko, R. Singh, J. Liu, D. Makoviichuk, K. Van Wyk, A. Zhurkevich, B. Sundaralingam _et al._ , “Dextreme: Transfer of agile in-hand manipulation from simulation to reality,” in _2023 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2023, pp. 5977–5984. 

- [3] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik, “In-hand object rotation via rapid motor adaptation,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 1722– 1732. 

- [4] H. Qi, B. Yi, S. Suresh, M. Lambeta, Y. Ma, R. Calandra, and J. Malik, “General in-hand object rotation with vision and touch,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 2549–2564. 

- [5] H. Qi, B. Yi, M. Lambeta, Y. Ma, R. Calandra, and J. Malik, “From simple to complex skills: The case of in-hand object reorientation,” _arXiv preprint arXiv:2501.05439_ , 2025. 

- [6] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski _et al._ , “Human-level control through deep reinforcement learning,” _nature_ , vol. 518, no. 7540, pp. 529–533, 2015. 

- [7] D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou, A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai, A. Bolton _et al._ , “Mastering the game of go without human knowledge,” _nature_ , vol. 550, no. 7676, pp. 354– 359, 2017. 

- [8] J. Schrittwieser, I. Antonoglou, T. Hubert, K. Simonyan, L. Sifre, S. Schmitt, A. Guez, E. Lockhart, D. Hassabis, T. Graepel _et al._ , “Mastering atari, go, chess and shogi by planning with a learned model,” _Nature_ , vol. 588, no. 7839, pp. 604–609, 2020. 

- [9] A. Nagabandi, K. Konolige, S. Levine, and V. Kumar, “Deep dynamics models for learning dexterous manipu- 

10 

lation,” in _Conference on robot learning_ . PMLR, 2020, pp. 1101–1112. 

- [10] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa _et al._ , “Isaac gym: High performance gpu-based physics simulation for robot learning,” _arXiv preprint arXiv:2108.10470_ , 2021. 

- [11] T. Chen, M. Tippur, S. Wu, V. Kumar, E. Adelson, and P. Agrawal, “Visual dexterity: In-hand reorientation of novel and complex object shapes,” _Science Robotics_ , vol. 8, no. 84, p. eadc9244, 2023. 

- [12] A. Karni, G. Meyer, C. Rey-Hipolito, P. Jezzard, M. M. Adams, R. Turner, and L. G. Ungerleider, “The acquisition of skilled motor performance: fast and slow experience-driven changes in primary motor cortex,” _Proceedings of the National Academy of Sciences_ , vol. 95, no. 3, pp. 861–868, 1998. 

- [13] C. R. Qi, L. Yi, H. Su, and L. J. Guibas, “Pointnet++: Deep hierarchical feature learning on point sets in a metric space,” _Advances in neural information processing systems_ , vol. 30, 2017. 

- [14] J.-P. Saut, A. Sahbani, S. El-Khoury, and V. Perdereau, “Dexterous manipulation planning using probabilistic roadmaps in continuous grasp subspaces,” in _2007 IEEE/RSJ International Conference on Intelligent Robots and Systems_ . IEEE, 2007, pp. 2907–2912. 

- [15] Y. Bai and C. K. Liu, “Dexterous manipulation using both palm and fingers,” in _2014 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2014, pp. 1560–1565. 

- [16] L. Sievers, J. Pitz, and B. Bäuml, “Learning purely tactile in-hand manipulation with a torque-controlled hand,” in _2022 International conference on robotics and_ 

   - _automation (ICRA)_ . IEEE, 2022, pp. 2745–2751. 

- [17] I. OpenAI Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas _et al._ , “Solving rubik’s cube with a robot hand,” _arXiv preprint arXiv:1910.07113_ , 2019. 

- [18] J. Pitz, L. Röstel, L. Sievers, D. Burschka, and B. Bäuml, “Learning a shape-conditioned agent for purely tactile inhand manipulation of various objects,” in _2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2024, pp. 13 112–13 119. 

- [19] R. A. Jacobs, M. I. Jordan, S. J. Nowlan, and G. E. Hinton, “Adaptive mixtures of local experts,” _Neural computation_ , vol. 3, no. 1, pp. 79–87, 1991. 

- [20] M. I. Jordan and R. A. Jacobs, “Hierarchical mixtures of experts and the em algorithm,” _Neural computation_ , vol. 6, no. 2, pp. 181–214, 1994. 

- [21] N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. Le, G. Hinton, and J. Dean, “Outrageously large neural networks: The sparsely-gated mixture-of-experts layer,” _arXiv preprint arXiv:1701.06538_ , 2017. 

- [22] W. Fedus, B. Zoph, and N. Shazeer, “Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity,” _Journal of Machine Learning Research_ , vol. 23, no. 120, pp. 1–39, 2022. 

- [23] F. Xue, Z. Zheng, Y. Fu, J. Ni, Z. Zheng, W. Zhou, 

and Y. You, “Openmoe: An early effort on open mixture-of-experts language models,” _arXiv preprint arXiv:2402.01739_ , 2024. 

- [24] B. Lin, Z. Tang, Y. Ye, J. Cui, B. Zhu, P. Jin, J. Huang, J. Zhang, Y. Pang, M. Ning _et al._ , “Moe-llava: Mixture of experts for large vision-language models,” _arXiv preprint arXiv:2401.15947_ , 2024. 

- [25] K. Doya, K. Samejima, K.-i. Katagiri, and M. Kawato, “Multiple model-based reinforcement learning,” _Neural computation_ , vol. 14, no. 6, pp. 1347–1369, 2002. 

- [26] X. B. Peng, M. Chang, G. Zhang, P. Abbeel, and S. Levine, “Mcp: Learning composable hierarchical control with multiplicative compositional policies,” _Advances in neural information processing systems_ , vol. 32, 2019. 

- [27] G. Cheng, L. Dong, W. Cai, and C. Sun, “Multi-task reinforcement learning with attention-based mixture of experts,” _IEEE Robotics and Automation Letters_ , vol. 8, no. 6, pp. 3812–3819, 2023. 

- [28] Z. Huang, H. Yuan, Y. Fu, and Z. Lu, “Efficient residual learning with mixture-of-experts for universal dexterous grasping,” _arXiv preprint arXiv:2410.02475_ , 2024. 

- [29] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” _arXiv preprint arXiv:1707.06347_ , 2017. 

- [30] D.-A. Clevert, T. Unterthiner, and S. Hochreiter, “Fast and accurate deep network learning by exponential linear units (elus),” _arXiv preprint arXiv:1511.07289_ , 2015. 

- [31] Y. Dong, X. Liu, J. Wan, and Z. Deng, “Gex: Democratizing dexterity with fully-actuated dexterous hand and exoskeleton glove,” _arXiv preprint arXiv:2506.04982_ , 2025. 

- [32] L. Downs, A. Francis, N. Koenig, B. Kinman, R. Hickman, K. Reymann, T. B. McHugh, and V. Vanhoucke, “Google scanned objects: A high-quality dataset of 3d scanned household items,” in _2022 International Conference on Robotics and Automation (ICRA)_ . IEEE, 2022, pp. 2553–2560. 

- [33] F. Ceola, L. Rosasco, and L. Natale, “Resprect: Speedingup multi-fingered grasping with residual reinforcement learning,” _IEEE Robotics and Automation Letters_ , vol. 9, no. 4, pp. 3045–3052, 2024. 

- [34] Y. Yang, P.-T. Jiang, Q. Hou, H. Zhang, J. Chen, and B. Li, “Multi-task dense prediction via mixture of lowrank experts,” in _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , 2024, pp. 27 927–27 937. 

- [35] J. Ma, Z. Zhao, X. Yi, J. Chen, L. Hong, and E. H. Chi, “Modeling task relationships in multi-task learning with multi-gate mixture-of-experts,” in _Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining_ , 2018, pp. 1930– 1939. 

- [36] K. Mamou, E. Lengyel, and A. Peters, “Volumetric hierarchical approximate convex decomposition,” _Game engine gems_ , vol. 3, pp. 141–158, 2016. 

- [37] D. P. Kingma, “Adam: A method for stochastic optimization,” _arXiv preprint arXiv:1412.6980_ , 2014. 

11 

## APPENDIX 

## EXPERIMENTAL DETAILS 

**Object Dataset:** We employ the full set of 150 objects from our dataset (see Figure 7), selecting 100 at random for training and reserving the remaining 50 for out-of-distribution evaluation. To ensure that each mesh can be manipulated by the robotic hand, we first center it and then scale it by a factor of 0.8 so that its dimensions align with the hand’s workspace in simulation. We observed that scaling meshes below a certain threshold, such as reducing them to 60% of their original size, shifts manipulation from precise fingertip control to collisions with the inner surfaces of the fingers. Moreover, when an object becomes very small, its complex geometric features no longer convey meaningful distinctions, and the dexterous hand effectively treats it as a simple, diminutive cube. 

**Convex Decomposition:** We use approximate convex decomposition (V-HACD [36]) to perform an approximate convex decomposition on the object and the robot hand meshes for fast collision detection in the simulator (Figure 8). **Policy architecture:** All networks are implemented as MLPs and trained with Adams [37]: the base policy _π_<sup>base</sup> uses two hidden layers of 512 units each; the point-cloud encoder _µ_ pc has three layers of 32 units; the object encoder _µ_ e comprises two layers of 256 and 128 units; and the gating network _π_<sup>gate</sup> consists of two 64-unit layers with ELU activations [30]. **Hyper-parameters:** Table II lists the hyper-parameters used in the experiments. 



TABLE II: Hyper-parameter Setup 

|Hyper-parameter|Value|Hyper-parameter|Value|
|---|---|---|---|
|num of envs|32768|episode length|600|
|horizon length|8|minibatch size|16384|
|learning rate|5e-3|PPO clip range|0.2|
|kl threshold|0.02|PPO gamma|0.99|
|PPO tau|0.95|success tolerance|0.4|
|_c_success|800|_c_dist|-10.0|
|_c_rot|-1.0|_ca_|-0.0002|
|_τθ_|0.1|_τq_|10.0|
|_τv_|0.04|_τω_|0.5|



Fig. 7: Overview of the complete object dataset, on the left of the red line, we show the training dataset. And on the right of the red line, we show the out-of-distribution (testing) dataset. 



Fig. 8: We show the difference between object meshes with and without convex decomposition. 

