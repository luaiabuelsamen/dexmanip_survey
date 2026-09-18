Published as a conference paper at ICLR 2025 

# DEXTRACK: TOWARDS GENERALIZABLE NEURAL TRACKING CONTROL FOR DEXTEROUS MANIPULATION FROM HUMAN REFERENCES 

**Xueyi Liu**<sup>1</sup><sup>_,_2</sup> **, Jianibieke Adalibieke**<sup>2</sup> **, Qianwei Han**<sup>2</sup> **, Yuzhe Qin**<sup>4</sup> **, Li Yi**<sup>1</sup><sup>_,_3</sup><sup>_,_2</sup> 1Tsinghua University 2Shanghai Qi Zhi Institute 3Shanghai AI Laboratory 4UC San Diego Project website: meowuu7.github.io/DexTrack 



<!-- Start of picture text -->
Timestamp<br>ReferencesKinematic … …<br>Goal 0 Goal n Goal n+1 Goal n+2<br>Observation at timestep n<br>Neural Tracking Object State n Goal n+1<br>Controller Update<br>Action Environ-<br>ment Timestamp Timestamp<br>Result n (State n+1) (b) Mimicking intricate manipulations with thin objects (c) Tracking noisy interactions with unreachable<br>(a) Inference flow of the neural tracking controller and intriguing in-hand re-orientations goal states and real-world evaluations<br>Kinematic References<br>Results<br>Kinematic References<br>Results<br><!-- End of picture text -->

Figure 1: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It generates hand action commands from kinematic references, ensuring close tracking of input trajectories ( _Fig. (a)_ ), generalizes to novel and challenging tasks involving thin objects, complex movements and intricate in-hand manipulations ( _Fig. (b)_ ), and demonstrates robustness to large kinematics noise and utility in real-world scenarios ( _Fig. (c)_ ). Kinematic references are illustrated in orange rectangles and background. 

## ABSTRACT 

We address the challenge of developing a generalizable neural tracking controller for dexterous manipulation from human references. This controller aims to manage a dexterous robot hand to manipulate diverse objects for various purposes defined by kinematic human-object interactions. Developing such a controller is complicated by the intricate contact dynamics of dexterous manipulation and the need for adaptivity, generalizability, and robustness. Current reinforcement learning and trajectory optimization methods often fall short due to their dependence on task-specific rewards or precise system models. We introduce an approach that curates large-scale successful robot tracking demonstrations, comprising pairs of human references and robot actions, to train a neural controller. Utilizing a data flywheel, we iteratively enhance the controller’s performance, as well as the number and quality of successful tracking demonstrations. We exploit available tracking demonstrations and carefully integrate reinforcement learning and imitation learning to boost the controller’s performance in dynamic environments. At the same time, to obtain high-quality tracking demonstrations, we individually optimize per-trajectory tracking by leveraging the learned tracking controller in a homotopy optimization method. The homotopy optimization, mimicking chainof-thought, aids in solving challenging trajectory tracking problems to increase demonstration diversity. We showcase our success by training a generalizable neural controller and evaluating it in both simulation and real world. Our method achieves over a 10% improvement in success rates compared to leading baselines. The project website with animated results is available at DexTrack. 

## 1 INTRODUCTION 

Robotic dexterous manipulation refers to the ability of a robot hand skillfully handling and manipulating objects for various target states with precision and adaptability. This capability has attracted 

1 

Published as a conference paper at ICLR 2025 

significant attention because adept object manipulation for goals such as tool use is vital for robots to interact with the world. Many efforts have been devoted previously to push the ability of a dexterous hand toward human-level dexterity and versatility (Rajeswaran et al., 2017; Chen et al., 2023; 2021; Akkaya et al., 2019; Christen et al., 2022; Zhang et al., 2023; Qin et al., 2022; Liu et al., 2022; Wu et al., 2023; Gupta et al., 2016; Wang et al., 2023; Mordatch et al., 2012; Liu et al., 2024a; Li et al., 2024). This also aligns with our vision. 

Achieving human-level robotic dexterous manipulation is challenging due to two main difficulties: the intricate dynamics of contact-rich manipulation, which complicates optimization (Pang & Tedrake, 2021; Pang et al., 2023; Liu et al., 2024a; Jin, 2024), and the need for robots to master a wide range of versatile skills beyond specific tasks. Previous approaches mainly resort to modelfree reinforcement learning (RL) (Chen et al., 2023; 2021; Akkaya et al., 2019; Christen et al., 2022; Zhang et al., 2023; Qin et al., 2022; Liu et al., 2022; Wu et al., 2023; Gupta et al., 2016; Wang et al., 2023) or model-based trajectory optimization (TO) (Pang & Tedrake, 2021; Pang et al., 2023; Jin, 2024; Hwangbo et al., 2018). While RL requires task-specific reward designs, limiting its generalization, TO depends on accurate dynamics models with known contact states, restricting adaptability to new objects and skills. A promising alternative is to leverage human hand-object manipulation references, widely available through videos or motion synthesis, and focus on controlling a dexterous hand to track these references. This approach separates high-level task planning from low-level control, framing diverse skill acquisition as the development of a universal tracking controller. However, challenges remain due to noisy kinematic references, differences in morphology between human and robotic hands, complex dynamics with rich contacts, and diverse object geometry and skills. Existing methods struggle with these issues, often limiting themselves to simple tasks without in-hand manipulation (Christen et al., 2022; Zhang et al., 2023; Wu et al., 2023; Xu et al., 2023; Luo et al., 2024; Singh et al., 2024; Chen et al., 2024) or certain specific skills (Qin et al., 2022; Liu et al., 2024a; Rajeswaran et al., 2017). 

In this work, we aim to develop a general-purpose tracking controller that can follow hand-object manipulation references across various skills and diverse objects. In particular, given a collection of kinematics-only human hand-object manipulation trajectories, the controller is optimized to drive a robotic dexterous hand to manipulate the object so that the resulting hand and object trajectories can closely mimic their corresponding kinematic sequences. We expect the tracking controller to exhibit strong versatility, generalize well to precisely track novel manipulations, and have strong robustness towards large kinematics noises and unexpected reference states. 

To achieve the challenging goal above, we draw three key observations: 1) learning is crucial for handling heterogeneous reference motion noises and transferring data prior to new scenarios, supporting robust and generalizable tracking control; 2) leveraging large-scale, high-quality robot tracking demonstrations that pair kinematic references with tracking action sequences can supervise and significantly empower neural controllers, as demonstrated by data-scaling laws in computer vision and NLP (OpenAI, 2023; Brown et al., 2020); 3) acquiring large and high-quality tracking demonstrations is challenging but we could utilize the data flywheel (Chiang et al., 2024; Bai et al., 2023) to iteratively improve the tracking controller and expand the demonstrations in a bootstrapping manner. 

Based upon the previous observations, we propose DexTrack, a novel neural tracking controller for dexterous manipulation, guided by human references. Specifically, given a collection of human hand-object manipulation trajectories, we first retarget the collection to kinematic robotic dexterous hand sequences to form a set of reference motions as data preparation. Our method then alternates between mining successful robot tracking demonstrations and training the controller with the mined demonstrations. To make sure the data flywheel functions effectively, we introduce two key designs. First, we carefully integrate reinforcement and imitation learning techniques to train a neural controller, ensuring its performance improves with more demonstrations while maintaining robustness against unexpected states and noise. Second, we develop a per-trajectory tracking scheme that uses the trained controller to mine diverse and high-quality tracking demonstrations through a homotopy optimization method. The scheme transfers the tracking prior from the controller to individual trajectories to ease per-trajectory tracking for better demonstration quality. Moreover, the scheme will convert a tracking reference into a series of gradually simplified reference motions so that tracking these references from simple to complex could help better track the original reference motion. This is akin to chain-of-thought and is very suitable for tracking complex reference motions to increase the demonstration diversity. The two designs above together with the iterative training enable DexTrack to successfully track novel and challenging human references. 

2 

Published as a conference paper at ICLR 2025 

We demonstrate the superiority of our method and compare it with previous methods on challenging manipulation tracking tasks in two datasets, describing expressive hand-object interactions in daily and functional tool-using scenarios, involving complex object movements, difficult and subtle inhand re-orientations, interactions with thin objects, and frequent hand-object rich contact variations. We conduct both extensive experiments in the simulator, _i.e.,_ Isaac Gym (Makoviychuk et al., 2021), and evaluations in the real world, to demonstrate the efficacy, generalization ability, and robustness of our tracker to accomplish a wide range of manipulation tracking tasks and even excellently track novel manipulation trajectories (Figure 1). Our approach successfully surpasses the previous methods both quantitatively and qualitatively, achieving more than 10% success rate than the previous best-performed method. Besides, we conduct further analysis and demonstrate the various recovery behaviors of our controller, demonstrating its robustness to unexpected situations. Thorough ablations are conducted to validate the efficacy of our designs. 

Our contributions are threefold: 

- We present a generalizable neural tracking controller that progressively improves its performance through iterative mining and incorporating high-quality tracking demonstrations. 

- We introduce a training method that synergistically combines reinforcement learning and imitation learning. This approach leverages abundant high-quality robot tracking demonstrations to produce a controller that is generalizable, versatile, and robust. 

- We develop a per-trajectory optimization scheme that employs our tracking controller within a homotopy optimization framework. We propose a data-driven way to generate homotopy paths, enabling solving challenging tracking problems. 

## 2 RELATED WORK 

Equipping robots with human-level dexterous manipulation skills is crucial for future advancements. Previous approaches either rely on model-based trajectory optimization or model-free reinforcement learning (RL). Model-based methods face challenges due to the complexity of dynamics, often requiring approximations (Pang et al., 2023; Jin, 2024; Pang & Tedrake, 2021). Model-free approaches, using RL (Rajeswaran et al., 2017; Chen et al., 2023; 2021; Christen et al., 2022; Zhang et al., 2023; Qin et al., 2022; Liu et al., 2022; Wu et al., 2023; Gupta et al., 2016; Wang et al., 2023; Mordatch et al., 2012), focus on goal-driven tasks with task-specific rewards, limiting their generalization across diverse tasks. Our work explores a general controller for dexterous manipulations. Besides, learning via mimicking kinematic trajectories has recently become a popular train to equip the agent with various expressive skills (Jenelten et al., 2023; Luo et al., 2023b;a). DTC (Jenelten et al., 2023) proposes a strategy that can combine the power of model-based motion planning and RL to overcome the sample inefficiency of RL. In the humanoid motion tracking space, PHC (Luo et al., 2023b) proposes an effective RL-based training strategy to develop a general humanoid motion tracker. Recently, OmniGrasp (Luo et al., 2024) proposes to train a universal grasping and trajectory following policy. The policy can generalize to unseen objects as well as track novel motions. However, their considered motions are still restricted in grasping and trajectory following, leaving the problem of tracking more interesting and difficult trajectories such as those with subtle in-hand manipulations largely not explored. In this paper, we focus on these difficult and challenging manipulations. Moreover, we are also related to recent trials on combining RL with imitation learning. To overcome the sample inefficiency problem of RL and to facilitate the convergence, various approaches have been developed aiming to augment RL training with demonstrations (Sun et al., 2018; Hester et al., 2017; Booher et al., 2024; Liu et al., 2023). In our work, we wish to leverage high-quality demonstrations to guide the agent’s explorations. Unlike previous work where demonstrations are readily available, acquiring a sufficient amount of high-quality robot tracking demonstrations remains a significant challenge in our task. 

## 3 METHOD 

**Terminologies and notations.** Dexterous manipulation “tracking” involves controlling a robotic hand to mimic a kinematic hand-object state sequence, the goal trajectory, denoted as _{_ ˆ **s** _n}_<sup>_N_</sup> _n_ =0<sup>.</sup> These “kinematic references” are retargeted from human manipulation trajectories, with ˆ **s** _n_ representing the robot hand state and object pose at timestep _n_ . A “tracking demonstration” pairs a kinematic reference _{_ ˆ **s** _n}_ with an expert action sequence _{_ **a**<sup>_L_</sup> _n_<sup>_}_, guiding the robot from</sup><sup>**s**0=ˆ</sup><sup>**s**0to</sup> 

3 

Published as a conference paper at ICLR 2025 



<!-- Start of picture text -->
Mining High-Quality Robot Tracking Demonstrations Learning a Neural Tracking Controller from Demonstrations<br>Homotopy Robot Tracking Demonstrations Goal Sate 𝒔'#$% State 𝒔#<br>Optimization Neural<br>Expert Action<br>Trajectory Tracking Action 𝒂! Environment<br>ReferencesKinematicHuman Single TrajectoryTracking ReferencesKinematict {𝒂! " , … , 𝒂# " , … } Demo (Expert)Action 𝒂"! Controller 𝜋 Reward 𝑟!<br>Improving demonstrations via the tracking controller Imitation Loss<br><!-- End of picture text -->

Figure 2: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It alternates between training the tracking controller using abundant and high-quality robot tracking demonstrations and improving the data via the tracking controller through a homotopy optimization scheme. 

achieve a state sequence _{_ **s** _n}_<sup>_N_</sup> _n_ =0<sup>aligned with</sup><sup>_{_ˆ</sup><sup>**s**</sup><sup>_n}N_</sup> _n_ =0<sup>.A “robust” controller can tolerate distur-</sup> bances like kinematics noise and unreachable states. It demonstrates high “generalization ability” if it performs well on unseen scenarios such as new objects and novel motions, and has “adaptivity” if it maintains effectiveness despite shifting contexts, such as changing contacts and dynamics. 

Given a collection of kinematic human-object manipulation trajectories, we wish to learn a generalizable neural tracking controller for a dexterous robotic hand. The problem is challenging due to the difficulty in precise dexterous manipulation, which is challenged by the underlying complex dynamics, and the high demands for the controller’s generalizability and robustness. 

We address these challenges by combining reinforcement learning (RL) and imitation learning (IL) to train a generalizable tracking controller, jointly easing the difficulty in solving the complex problem via supervision from high-quality and diverse robot tracking demonstrations and improving the policy’s robustness via RL explorations. We introduce a single trajectory tracking scheme to mine tracking demonstrations, composed of paired kinematic references and action sequences. For each kinematic reference, we use RL to train a trajectory-specific policy that generates actions to track the reference. To overcome RL’s limitations, we propose to leverage the tracking controller through a homotopy optimization scheme to enhance the demonstration quality and diversity. By iteratively mining better demonstrations and refining the controller in a bootstrapping manner, we develop an effective, generalizable tracking controller. We will explain how we learn the neural tracking controller from demonstrations in Section 3.1, how we mine high-quality demonstrations in Section 3.2, and how we iterate between learning controller and mining demonstrations in Section 3.3. 

### 3.1 LEARNING A NEURAL TRACKING CONTROLLER FROM DEMONSTRATIONS 

Given a collection of human-object manipulation trajectories and a set of high-quality robot tracking demonstrations, our goal is to learn an effective and generalizable neural tracking controller. In the beginning, we retarget human hand-object manipulation to a robotic hand as a data preprocessing step. We combine RL and IL to develop a generalizable and robust neural tracking controller. Taking advantage of imitating diverse and high-quality robot tracking demonstrations, we can effectively let the tracking controller master diverse manipulation skills and also equip it with high generalization ability. Jointly leveraging the power of RL, the controller avoids overfitting to successful tracking results limited to a narrow distribution, thereby maintaining robust performance in the face of dynamic state disturbances. Specifically, we design an RL-based learning scheme for training the tracking controller, including the carefully-designed action space, observations, and the reward tailored for the manipulation tracking task. We also introduce an IL-based strategy that lets the tracking controller benefit from imitating high-quality demonstration data. By integrating these two approaches, we effectively address the complex problem of generalizable tracking control. 

**Neural tracking controller.** In our formulation, the neural tracking controller acts as an agent that interacts with the environment according to a tracking policy _π_ . At each timestep _n_ , the policy observes the observation **o** _n_ and the next goal ˆ **s** _n_ +1 (designated as the target state for the robotic hand and the object). The policy then computes the distribution of the action. Then the agent sample an action **a** _n_ from the policy, _i.e.,_ **a** _n ∼ π_ ( _·|_ **o** _n,_ ˆ **s** _n_ +1). The observation **o** _n_ primarily contains the current state **s** _n_ and the object geometry. Upon executing the action with the robotic dexterous hand, the hand physically interacts with the object, leading both the hand and the object to transition into the next state according to the environment dynamics, represented as **s** _n_ +1 _∼ p_ ( _·|_ **s** _n,_ **a** _n_ ). An effective tracking controller should ensure that the resulting hand and object states closely align with their respective next goal states. 

**Reinforcement learning.** In the RL-based training scheme, the agent receives a reward _rn_ = _r_ ( **s** _n,_ **a** _n,_ ˆ **s** _n_ +1 _,_ **s** _n_ +1) after each transition. The training objective is to maximize the discounted 

4 

Published as a conference paper at ICLR 2025 

cumulative reward: 



where _p_ ( _τ |π_ ) = _p_ ( **s** 0)<sup>�</sup><sup>_N_</sup> _n_ =0<sup>_−_1</sup><sup>_p_(</sup><sup>**s**</sup><sup>_n_+1</sup><sup>_|_</sup><sup>**o**</sup><sup>_n,_</sup><sup>**a**</sup><sup>_n_)</sup><sup>_π_(</sup><sup>**a**</sup><sup>_n|_</sup><sup>**s**</sup><sup>_n,_ˆ</sup><sup>**s**</sup><sup>_n_+1)isthelikelihoodofatransitiontra-</sup> jectory of the agent _τ_ = ( **s** 0 _,_ **a** 0 _, r_ 0 _, ...,_ **s** _N −_ 1 _,_ **a** _N −_ 1 _, rN −_ 1 _,_ **s** _N_ ). The discount factor _γ ∈_ [0 _,_ 1) determines the effective horizon length of the policy. In the tracking control problem, the next goal state ˆ **s** _n_ +1 typically comprises the subsequent hand state and the object state from the kinematic reference sequence. We control the robotic hand using a proportional derivative (PD) controller, following previous literature (Luo et al., 2024; 2023b; Christen et al., 2022; Zhang et al., 2023). The action **a** _n_ contains the target position commands for all hand joints. To enhance the sample efficiency of RL, rather than allowing the tracking policy to learn the absolute positional targets, we introduce a residual action space. Specifically, we introduce a baseline hand trajectory and train the policy to learn the residual relative target ∆ **a** _n_ at each timestep. The baseline trajectory is consistently available for the tracking problem and can be trivially set to the kinematic reference trajectory. In each timestep _n_ , we compute the position target via **a** _n_ = **s**<sup>_b_</sup> _n_<sup>+ �</sup><sup>_n_</sup> _k_ =0<sup>∆</sup><sup>**a**</sup><sup>_k_, where</sup><sup>**s**</sup> _n_<sup>_b_is the</sup><sup>_n_-th</sup> step hand state in the baseline trajectory. The observation at each timestep _n_ encodes the current hand and object state, the baseline trajectory, actions, velocities, and the object geometry: 



where featobj is the object feature generated by a pre-trained object point cloud encoder. We also introduce an auxiliary feature aux _n_ , computed based on available states, to provide the agent with more informative context. Further details will be explained in Appendix A. Our reward for manipulation tracking encourages the transited hand state and the object state to closely match their respective reference states, as well as promoting hand-object affinity: 



where _ro,p, ro,q, r_ wrist _, r_ finger _, r_ affinity represent rewards for object position, object orientation, hand wrist, hand fingers, and hand-object affinity, respectively, while _wo,p, wo,q, w_ wrist _, w_ finger _, w_ affinity are their corresponding weights. Details regarding the reward computation are deferred to Appendix A. 

**Imitation learning.** The RL-based learning scheme, hindered by sample inefficiency and its inability to handle multiple tracking problems, struggles to solve the generalizable tracking control problem, as demonstrated by our early experiments. Therefore, we propose an IL-based strategy to distill successful, abundant, and diverse “tracking knowledge” into the tracking controller. Specifically, we train the tracking agent to imitate a large number of high-quality robot tracking demonstrations. This approach effectively guides the agent to produce “expert actions” that can successfully track the reference state. Additionally, by imitating diverse tracking demonstrations, the agent can avoid repeatedly encountering low rewards in challenging tracking scenarios, while also preventing over-exploitation of easier tasks. Formally, a robot tracking demonstration of length _N_ consists of a kinematic reference sequence (ˆ **s** 0 _, ...,_ ˆ **s** _N_ ) and an expert’s state-action trajectory ( **s**<sup>_L_</sup> 0<sup>_,_</sup><sup>**a**</sup><sup>_L_</sup> 0<sup>_, ...,_</sup><sup>**s**</sup><sup>_L_</sup> _N −_ 1<sup>_,_</sup><sup>**a**</sup><sup>_L_</sup> _N −_ 1<sup>_,_</sup><sup>**s**</sup><sup>_L_</sup> _N_<sup>).Inadditiontotheactorloss,weincorporateanactionsupervision</sup> loss to bias the policy’s predictions at each timestep towards the corresponding expert action in the demonstration: 



This guidance allows the policy’s exploration to be informed by these demonstrations, ultimately speeding up convergence and enhancing performance in complex problems. From the perspective of IL, the RL exploration introduces noise into the states, making the imitation more robust, in a similar flavor to DART (Laskey et al., 2017). Since the agent should not and will not explore states too far from the reference states in the tracking control task, it is feasible to optimize the policy using both the imitation loss and RL reward simultaneously. 

- 3.2 MINING HIGH-QUALITY ROBOT TRACKING DEMONSTRATIONS USING NEURAL CONTROLLER THROUGH A HOMOTOPY OPTIMIZATION SCHEME 

To prepare a demonstration from a kinematic reference trajectory (ˆ **s** 0 _, ...,_ ˆ **s** _N_ ) for training the tracking controller, we need to infer the action sequence ( **a**<sup>_L_</sup> 0<sup>_, ...,_</sup><sup>**a**</sup><sup>_L_</sup> _N −_ 1<sup>) that successfully tracks the ref-</sup> erence sequence. A straightforward approach is to leverage RL to train a single-trajectory tracking 

5 

Published as a conference paper at ICLR 2025 

policy _π_ and use its resulting action sequence directly. However, relying solely on this strategy often fails to provide a diverse and high-quality dataset of tracking demonstrations, as RL struggles with the inherent challenges of dexterous manipulation. To enhance both the diversity and quality of robot tracking demonstrations, we propose utilizing the tracking controller in conjunction with a homotopy optimization scheme to improve the per-trajectory tracking results. 

**RL-based single trajectory tracking.** A basic approach to acquiring demonstrations is to leverage RL to address the per-trajectory tracking problem, using the resulting action sequence as the demonstration. Given a kinematic reference trajectory, our goal is to optimize a tracking policy _π_ that can accurately track this reference trajectory. At each timestep, _π_ observes the current state **s** _n_ and the next goal state ˆ **s** _n_ +1, and it predicts the distribution of the current action **a** _n_ . The policy _π_ is optimized to minimize the difference between the transited state **s** _n_ +1 _∼ p_ ( _·|_ **s** _n,_ **a** _n_ ) at each timestep _n_ and the goal state ˆ **s** _n_ +1. Similar to our design for the RL-based learning scheme for the tracking controller, we adopt a residual action space. For each tracking task, we introduce a baseline trajectory ( **s**<sup>_b_</sup> 0<sup>_, ...,_</sup><sup>**s**</sup><sup>_b_</sup> _N_<sup>) and only learn a residual policy using RL. The observations and rewards follow the</sup> same design as for the tracking controller (see Eq. 8 and Eq. 10). Once _π_ has been optimized, we can sample the action **a** _n_ from _π_ at each timestep. By iteratively transitioning to the next state using the predicted action and querying the policy _π_ to generate a new action, we can obtain the expert action sequence ( **a**<sup>_L_</sup> 0<sup>_, ...,_</sup><sup>**a**</sup><sup>_L_</sup> _N −_ 1<sup>) for the input kinematic reference trajectory.</sup> 

**Transferring “tracking prior”.** To improve the demonstrations, we devise a strategy that takes advantage of the tracking controller, which has already encoded “knowledge” that can track lots of trajectories (named as “tracking prior”), to improve trajectory-specific tracking policies. Specifically, to track a reference trajectory (ˆ **s** 0 _, ...,_ ˆ **s** _N_ ), we first utilize the tracking controller to track it, with the baseline trajectory set to thew reference sequence. We then adjust the baseline trajectory to the resulting action sequence and re-optimize the residual policy using the RL-based single trajectory tracking method. This approach can help us find a better baseline trajectory, facilitating single-trajectory tracking policy learning and improving the per-trajectory tracking results. 

**A homotopy optimization scheme.** Training the controller with data mined from itself can introduce biases and reduce diversity, hindering its generalization capabilities. To address this issue, we propose a homotopy optimization scheme to improve the per-trajectory tracking performance and to tackle previously unsolvable single-trajectory tracking problems. For the tracking problem _T_ 0, instead of solving it directly, the homotopy optimization iteratively solves each tracking task in an optimization path, _e.g.,_ ( _TK, TK−_ 1 _, ..., T_ 0), and finally solves _T_ 0, in a similar flavor to “chain-ofthought” (Wei et al., 2022). In the beginning, we leverage the RL-based tracking method to solve _TK_ . After that, we solve each task _Tm_ via the RL-based tracking method with the baseline trajectory set to the tracking result of _Tm_ +1. This transfer of tracking results from other tasks helps us establish better baseline trajectories, ultimately yielding higher-quality tracking outcomes. 

**Finding effective homotopy optimization paths.** While leveraging the homotopy optimization scheme to solve previously unsolvable problems has proven effective for many tasks, it depends on identifying effective optimization paths. A straightforward approach is brute-force searching. Specifically, given a set of kinematic references, we first optimize their per-trajectory tracking outcomes. We then identify neighbors for each task based on the similarity between pairs of kinematic reference trajectories. Next, we iteratively transfer optimization results from neighboring tasks and re-optimize the residual policy for each tracking task. For a specific task, we consider a neighbor that provides a better baseline trajectory than its kinematic trajectory as an effective “parent task”. After reaching the maximum number of iterations, _K_ , we can find effective homotopy paths for a task, _i.e., T_ 0, by starting from _T_ 0 and backtracing effective “parent tasks”. We define ( _TK, ..., T_ 0) as an effective homotopy path for _T_ 0 if, for each 0 _≤ m ≤ K_ , _Tm_ +1 is an effective parent task for _Tm_ . 

**Learning a homotopy generator for efficient homotopy path planning.** Finding effective homotopy optimization paths for tracking each trajectory is computationally expensive and impractical during inference. To address this, we propose learning a homotopy path generator _M_ from a small dataset, enabling efficient generation of effective homotopy paths for other tracking tasks. The key problem in identifying homotopy paths lies in finding effective “parent tasks”. We reformulate this problem as a tracking task transformation problem, aiming for a generator _M_ that provides a distribution of effective “parent tasks” for each tracking task _T_ 0: _M_ ( _·|T_ 0), considering the fact that a single tracking task may have multiple effective “parent tasks”. Once _M_ is trained, we can find a homotopy path by iteratively finding parent tasks. We propose training a conditional diffusion model 

6 

Published as a conference paper at ICLR 2025 

as the tracking task transformer, leveraging its strong distribution modeling capability. Given a set of tracking tasks, characterized by the kinematic reference trajectories of the hand and object, as well as object geometry, we first train a diffusion model to capture the distribution of tracking tasks. To fine-tune this diffusion model into a conditional model, we first search for effective homotopy paths within the tracking task dataset. This yields a set of paired data of the tracking task _Tc_ and their corresponding effective “parent task” _Tp_ . We then use this data to tune the diffusion model into a conditional diffusion model, such that _Tp ∼M_ ( _·|Tc_ ). A well-trained _M_ can efficiently propose an effective homotopy path for a tracking task, _i.e., T_ 0, by starting from _T_ 0 and recursively finding the parent task, resulting in ( _TK, ..., T_ 0), where _Tm_ +1 _∼M_ ( _·|Tm_ ) for all 0 _≤ m ≤ K −_ 1. 

### 3.3 IMPROVING THE TRACKING CONTROLLER VIA ITERATIVE OPTIMIZATION 

We adopt an iterative approach that alternates between training the tracking controller with abundant robot tracking demonstrations and curating more diverse, higher-quality demonstrations using the controller. Our method is divided into three stages. In the first stage, we sample a small set of tracking tasks and generate an initial demonstration set by applying RL to obtain single-trajectory tracking results for each task. Using these demonstrations, we train the tracking controller with both RL and IL. At this stage, we do not train the homotopy path generator, as the model’s generalization ability would be limited by the small number of effective homotopy paths available for training. In the second stage, we sample a dataset of trajectories from the remaining tasks, weighted according to the controller’s tracking error. We then use RL, incorporating tracking priors, to optimize pertrajectory tracking, search for homotopy paths, and train a homotopy path generator based on the resulting data. The best tracking results from all successfully tracked trajectories are curated into a new demonstration set, which is used to re-train the tracking controller. In the third stage, we resample tracking tasks from the remaining set and leverage RL, the tracking controller, and the homotopy generator to curate another set of tracking demonstrations. This final set is used to optimize the tracking controller, resulting in our final model. 

## 4 EXPERIMENTS 

We conduct extensive experiments to evaluate the effectiveness, generalizability, and robustness of our tracking controller. Tested on two HOI datasets featuring complex daily manipulation tasks, our method is assessed through both simulation and real-world evaluations (see Sec. 4.1). We compare our approach to strong baselines, showing its superiority. Our controller successfully handles novel manipulations, including intricate movements, thin objects, and dynamic contacts (see Sec. 4.2), while previous methods fail to generalize well. On average, our method improves the tracking success rate by over 10% compared to the best prior methods. Additionally, we analyze its robustness to significant kinematic noise, such as unrealistic states and large penetrations (see Sec. 4.3). 

### 4.1 EXPERIMENTAL SETTINGS 

**Datasets.** We test our method on two public human-object interaction datasets: GRAB (Taheri et al., 2020), featuring daily interactions, and TACO (Liu et al., 2024b), containing functional tool-use interactions. In simulation, we use the Allegro hand, with URDF adapted from IsaacGymEnvs (Makoviychuk et al., 2021), and in real-world experiments, the LEAP hand (Shaw et al., 2023), due to hardware constraints. Human-object interaction trajectories are retargeted to create robot hand-object sequences using PyTorch ~~K~~ inematics (Zhong et al., 2024). We fully retargeted the GRAB and TACO datasets, producing 1,269 and 2,316 robot hand manipulation sequences, respectively. The evaluation on GRAB focus on testing the model’s generalization to unseen interaction sequences. Specifically, we use sequences from subject s1 (197 sequences) as the test data while the remaining trajectories as the training set. For the TACO dataset, we follow the generalization evaluating setting suggested by the authors (Liu et al., 2024b) and split the dataset into a training set with 1,565 trajectories and four distinct test sets at different difficulty levels. The primary quantitative results are reported on the first-level set. More details are provided in Appendix C. **Metrics.** We introduce five metrics to evaluate the tracking accuracy and task success: 1) Per-frame average object rotation error: _R_ err = _N_ <u>1+1</u> � _Nn_ =0<sup>Diff</sup> ~~A~~ ngle( **q** _n,_ ˆ **q** _n_ ), where **q** ˆ _n_ and **q** _n_ are reference and tracked orientation. 2) Per-frame average object translation error: _T_ err = _N_ <u>1+1</u> � _Nn_ =0<sup>_∥_</sup><sup>**t**</sup><sup>_n−_</sup> ˆ **t** _n∥_ , where **t** _n_ and ˆ **t** _n_ are the tracked and reference translations. 3) Per-frame average wrist position and rotation error: _E_ wrist = _N_ <u>1+1</u> � _Nn_ =0 �0 _._ 5 Diff ~~A~~ ngle( **q**<sup>wrist</sup> _n ,_ ˆ **q**<sup>wrist</sup> _n_ ) + 0 _._ 5 _∥_ **t**<sup>wrist</sup> _n −_<sup>ˆ</sup> **t**<sup>wrist</sup> _n ∥_ �, where **q**<sup>wrist</sup> _n_ and **q** ˆ<sup>wrist</sup> _n_ are wrist orientations, and **t**<sup>wrist</sup> _n_ and<sup>ˆ</sup> **t**<sup>wrist</sup> _n_ are translations. 4) Per-frame per-joint 

7 

Published as a conference paper at ICLR 2025 

Table 1: **Quantitative evaluations. Bold red** and _italic blue_ values for best and the second best-performed ones respectively. “Ours (w/o) data” and “Ours (w/o data, w/o homotopy)” are two ablated versions w.r.t. <u>quality of robot tracking demonstrations used in imitation learning (see Section 5 for details).</u> 

|Dataset|Method|_R_err(rad_, ↓_)|_T_err (_cm, ↓_)|_E_wrist(_↓_)|_E_finger (rad_, ↓_)|Success Rate (%_, ↑_)|
|---|---|---|---|---|---|---|
||DGrasp|0.4493|6.75|0.1372|0.6039|34.52/52.79|
||PPO (OmniGrasp rew.)|0.4404|6.69|0.1722|0.6418|35.53/54.82|
|GRAB|PPO (w/o sup., tracking rew.)|0.3945|6.11|**0.1076**|0.5899|38.58/54.82|
||Ours (w/o data, w/o homotopy)|0.3443|7.81|0.1225|_0.5218_|39.59/57.87|
||Ours (w/o data)|_0.3415_|_4.97_|0.1483|0.5264|_43.15_/_62.44_|
||Ours|**0.3303**|**4.53**|_0.1118_|**0.5048**|**46.70**/**65.48**|
||DGrasp|0.5021|5.04|**0.1129**|0.4737|38.42/47.78|
||PPO (OmniGrasp rew.)|0.5174|5.43|0.1279|0.4945|33.5/46.31|
|TACO|PPO (w/o sup., tracking rew.)|_0.4815_|4.82|_0.1195_|_0.4682_|34.98/57.64|
||Ours (w/o data, w/o homotopy)|**0.4444**|2.33|0.1782|0.5438|44.83/67.00|
||Ours (w/o data)|0.4854|_2.21_|0.1698|0.4772|_47.78_/_72.41_|
||Ours|0.4953|**2.10**|0.1510|**0.4661**|**48.77**/**74.38**|



average position error: _E_ finger = _N_ <u>1+1</u> � _Nn_ =0 � _d_ <u>1</u><sup>_∥θ_</sup> _n_<sup>finger</sup> _− θ_<sup>ˆ</sup> _n_<sup>finger</sup> _∥_ 1�, where _θ_ denotes finger joint positions, _d_ is the degrees of freedom. 5) Success rate: A tracking attempt is successful if _T_ err, _R_ err, and 0 _._ 5 _E_ wrist + 0 _._ 5 _E_ finger are all below the thresholds. Success is calculated with two thresholds: 10cm-20<sup>_◦_</sup> -0 _._ 8 and 10cm-40<sup>_◦_</sup> -1 _._ 2. 

**Baselines.** To our knowledge, no prior model-based methods have directly tackled tracking control for dexterous manipulation. Most existing approaches focus on single goal-driven trajectory optimization with simplified dynamics models (Jin, 2024; Pang et al., 2023; Pang & Tedrake, 2021), limiting their adaptability for our framework’s generalizable tracking controller. Thus, we primarily compare our method with model-free approaches: 1) DGrasp (Christen et al., 2022): Adapted to track by dividing sequences into subsequences of 10 frames, with each subsequence solved incrementally. 2) PPO (OmniGrasp rew.): We re-implemented OmniGrasp’s reward (Luo et al., 2024) to train a policy for tracking object trajectories. 3) PPO (w/o sup., tracking rew.): We trained a policy using PPO with our proposed tracking reward and observation design. 

**Training and evaluation settings.** We use PPO (Schulman et al., 2017), implemented in rl games (Makoviichuk & Makoviychuk, 2021), with Isaac Gym (Makoviychuk et al., 2021) for simulation. Training is performed with 8192 parallel environments for both the per-trajectory tracker and the tracking controller. For the dexterous hand, the position gain and damping coefficient are set to 20 and 1 per finger joint. Evaluation results are averaged across 1000 parallel environments, and for real-world evaluations, we use LEAP (Shaw et al., 2023) with a Franka arm and FoundationPose (Wen et al., 2023) for object state estimation. Additional details are provided in Appendix C. 

### 4.2 GENERALIZABLE TRACKING CONTROL FOR DEXTEROOUS MANIPULATION 



<!-- Start of picture text -->
Timestamp<br>Kinematic<br>Reference<br>Ours<br><!-- End of picture text -->

Figure 3: **Robustness w.r.t. unreasonable states.** Please check **our website and video** for animated results. 

We demonstrate the generalization ability and robustness of our tracking controller on unseen trajectories involving challenging manipulations and novel, thin objects. Our controller has no difficulty in handling intricate motions, subtle in-hand re-orientations, and expressive functional manipulations, even when dealing with thin objects. As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across both datasets. Figure 4 provides qualitative examples and comparisons. We show the real-world effectiveness of our method and the superiority over best-performing baselines (Figure 4,Table 2). For animated results, please visit our project website and the accompanying video. 

**Intriguing in-hand manipulations.** Our method effectively generalizes to novel, complex, and challenging functional manipulations, featured by subtle in-hand re-orientations, essential for precise tool-use tasks. For instance, in Figure 4a, the shovel is lifted, tilted, and reoriented with intricate finger movements to complete a stirring motion. Similarly, in Figure 4c, the small shovel is reori- 

8 

Published as a conference paper at ICLR 2025 

Table 2: **Real-world quantitative comparisons. Bold red** numbers for best values. 

|Method|apple<br>banana|duck|elephant|flashlight|flute|hammer|hand<br>phone<br>waterbottle|
|---|---|---|---|---|---|---|---|
|PPO (w/o sup., tracking rew)|0/0/0<br>25.0/25.0/0.0|50.0/25.0/0|50.0/0.0/0.0|50.0/0/0|0/0/0|25.0/0/0|66.7/33.3/0<br>25.0/0/0<br>33.3/33.3/0|
|Ours|**25.0**/0/0<br>**50.0**/**50.0**/**25.0**|**75.0**/**50.0**/**25.0**|**75.0**/**50.0**/**50.0**|**50.0**/**25.0**/**25.0**|**25.0**/**25.0**/**25.0**|**50.0**/**50.0**/**50.0**|**66.7**/**33.3**/**33.3**<br>**50.0**/**50.0**/**25.0**<br>**50.0**/**33.3**/**33.3**|



ented using minimal wrist adjustments. These results demonstrate the robustness and generalization of our controller, outperforming the PPO baseline, which struggles with basic lifting. 

**Intricate manipulations with thin objects.** Our method also generalizes well to challenging manipulations involving thin objects. In Figure 4b, despite the thin shovel’s complexity and missing CAD model parts, our method successfully lifts and controls it using a firm grasp with the second and third fingers. Similarly, in Figure 4e, our controller adeptly lifts and manipulates a thin flute, while the best-performing baseline struggles with the initial grasp. These results highlight the advantages of our approach in handling complex and delicate manipulations. 

**Real-world evaluations and comparisons.** We directly transfer tracking results to the real world to assess tracking quality and evaluate the robustness of the state-based controller against noise in the state estimator. Success rates are measured under three thresholds and compared with the best baseline. Table 2 summarizes the per-object success rates averaged over their manipulation trajectories in the transferred controller setting. As demonstrated in Figures 4f and 4g, we enable the robot to track complex object movements and successfully lift a hard-to-grasp round apple in real-world scenarios. While the baseline fails. Further details can be found in Appendix B.2. 

### 4.3 FURTHER ANALYSIS AND DISCUSSIONS 

**Robustness to noise in the kinematic reference motions.** Despite severe hand-object penetrations in Figure 4c (frames 2 and 3) and Figure 4a (frame 2), the hand still interacts effectively with the object, highlighting the resilience of our tracking controller in challenging scenarios. 

**Robustness to unreasonable references.** As shown in Figure 3, our method remains unaffected by significant noise in the kinematic references with unreasonable states. We effectively track the entire motion trajectory, demonstrating the controller’s robustness in handling unexpected noise. 

## 5 ABLATION STUDIES 

**Diversity and quality of robot tracking demonstrations.** We propose enhancing the diversity and quality of tracking demonstrations using the tracking controller and homotopy generator. We ablate these strategies by creating two variants: “Ours (w/o data, w/o homotopy)”, where the dataset is built by optimizing each trajectory without prior knowledge, and “Ours (w/o data)”, which uses only the homotopy optimization scheme to improve demonstrations. Despite using the same number of demonstrations, both variants produce lower-quality data. As shown in Table 1, they underperform compared to our full method, underscoring the importance of data quality in training the controller. 

**Scaling the number of demonstrations.** To investigate the relationship between the tracking controller’s performance and the number of demonstrations, we vary the size of the demonstration dataset during training and tested performance on the TACO dataset. Specifically, in the final training iteration, we down-sampled the dataset to 0.1, 0.3, 0.5, and 0.9 of its original size and re-trained the model. As shown in Figure 5, there is a clear correlation between the amount of demonstrations and model performance. Since the curve has not plateaued, we hypothesize that increasing the amount of high-quality data could further improve performance. 



<!-- Start of picture text -->
75 Scaling the number of demonstrations 74.38<br>72.91<br>70<br>67.0<br>65<br>62.07<br>59.61<br>60<br>57.64<br>0.0 0.2 0.4 0.6 0.8 1.0<br>Proportion of Total Demonstrations Used<br>Figure 5: Scaling the amount of demonstrations.<br>Success Rate (%)<br><!-- End of picture text -->

## 6 CONCLUSIONS AND LIMITATIONS 

We propose DexTrack to develop a generalizable tracking controller for dexterous manipulation. Leveraging high-quality tracking demonstrations and a pre-trajectory tracking scheme, we refine the controller through bootstrapping. Extensive experiments confirm its effectiveness, establishing a strong foundation for future advancements. **Limitations.** A key limitation is the time-consuming process of acquiring high-quality demonstrations. Future work could explore faster, approximate methods for homotopy optimization to speed up training. 

9 

Published as a conference paper at ICLR 2025 



<!-- Start of picture text -->
Timestamp<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>(a) Manipulating a shovel. ( Challenges:  difficult to grasp, in-hand re-orientations using fingers, complex object movements)<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>(b) Manipulating an extremely thin shovel. ( Challenges:  difficult to hold from the end, in-hand re-orientations using fingers, complex object movements)<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>(c) Waving a small shovel. ( Challenges:  difficult to grasp, in-hand re-orientations using fingers, complex object movements, noisy kinematic reference)<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>(d) Using a hammer. ( Challenges:  difficult to grasp, complex object movements)<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>(e) Playing a flute. ( Challenges:  difficult to grasp, in-hand re-orientations using fingers)<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>Timestamp  (f)  Complex object movements  with  in-hand subtle re-orientations Timestamp  (g) Lifting an apple that is  hard to grasp  and lift up<br><!-- End of picture text -->

Figure 4: **Qualitative comparisons.** Please check **our website and the accompanying video** for animated results. 

10 

Published as a conference paper at ICLR 2025 

## REFERENCES 

- Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias Plappert, Glenn Powell, Raphael Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 2 

- Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenhang Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, K. Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Yu Bowen, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xing Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. _ArXiv_ , abs/2309.16609, 2023. URL https://api.semanticscholar.org/ CorpusID:263134555. 2 

- Jonathan Booher, Khashayar Rohanimanesh, Junhong Xu, Vladislav Isenbaev, Ashwin Balakrishna, Ishan Gupta, Wei Liu, and Aleksandr Petiushko. Cimrl: Combining imitation and reinforcement learning for safe autonomous driving. _ArXiv_ , abs/2406.08878, 2024. URL https://api. semanticscholar.org/CorpusID:270440413. 3 

- Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeff Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Ma teusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. _ArXiv_ , abs/2005.14165, 2020. URL https://api.semanticscholar.org/ CorpusID:218971783. 2 

- Tao Chen, Jie Xu, and Pulkit Agrawal. A system for general in-hand object re-orientation. _Conference on Robot Learning_ , 2021. 2, 3 

- Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Edward Adelson, and Pulkit Agrawal. Visual dexterity: In-hand reorientation of novel and complex object shapes. _Science Robotics_ , 8(84): eadc9244, 2023. doi: 10.1126/scirobotics.adc9244. URL https://www.science.org/ doi/abs/10.1126/scirobotics.adc9244. 2, 3 

- Zerui Chen, Shizhe Chen, Cordelia Schmid, and Ivan Laptev. Vividex: Learning vision-based dexterous manipulation from human videos. _ArXiv_ , abs/2404.15709, 2024. URL https: //api.semanticscholar.org/CorpusID:269330215. 2 

- Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li, Hao Zhang, Banghua Zhu, Michael Jordan, Joseph E. Gonzalez, and Ion Stoica. Chatbot arena: An open platform for evaluating llms by human preference. _ArXiv_ , abs/2403.04132, 2024. URL https://api.semanticscholar.org/CorpusID: 268264163. 2 

- Sammy Christen, Muhammed Kocabas, Emre Aksan, Jemin Hwangbo, Jie Song, and Otmar Hilliges. D-grasp: Physically plausible dynamic grasp synthesis for hand-object interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 20577–20586, 2022. 2, 3, 5, 8 

- Abhishek Gupta, Clemens Eppner, Sergey Levine, and Pieter Abbeel. Learning dexterous manipulation for a soft robotic hand from human demonstrations. In _2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 3786–3793. IEEE, 2016. 2, 3 

- Todd Hester, Matej Vecer´ık, Olivier Pietquin, Marc Lanctot, Tom Schaul, Bilal Piot, Dan Horgan, John Quan, Andrew Sendonaris, Ian Osband, Gabriel Dulac-Arnold, John P. Agapiou, Joel Z. Leibo, and Audrunas Gruslys. Deep q-learning from demonstrations. In _AAAI Conference on Artificial Intelligence_ , 2017. URL https://api.semanticscholar.org/CorpusID: 10208474. 3 

11 

Published as a conference paper at ICLR 2025 

- Jemin Hwangbo, Joonho Lee, and Marco Hutter. Per-contact iteration method for solving contact dynamics. _IEEE Robotics and Automation Letters_ , 3(2):895–902, 2018. 2 

- Fabian Jenelten, Junzhe He, Farbod Farshidian, and Marco Hutter. Dtc: Deep tracking control. _Science Robotics_ , 9, 2023. URL https://api.semanticscholar.org/CorpusID: 263152143. 3 

- Wanxin Jin. Complementarity-free multi-contact modeling and optimization for dexterous manipulation. 2024. URL https://api.semanticscholar.org/CorpusID:271874325. 2, 3, 8 

- Michael Laskey, Jonathan Lee, Roy Fox, Anca Dragan, and Ken Goldberg. Dart: Noise injection for robust imitation learning. In _Conference on robot learning_ , pp. 143–156. PMLR, 2017. 5 

- Zhongyu Li, Xue Bin Peng, Pieter Abbeel, Sergey Levine, Glen Berseth, and Koushil Sreenath. Reinforcement learning for versatile, dynamic, and robust bipedal locomotion control. _ArXiv_ , abs/2401.16889, 2024. URL https://api.semanticscholar.org/ CorpusID:267320454. 2 

- Xingyu Liu, Deepak Pathak, and Kris M Kitani. Herd: Continuous human-to-robot evolution for learning from human demonstration. _arXiv preprint arXiv:2212.04359_ , 2022. 2, 3 

- Xuefeng Liu, Takuma Yoneda, Rick L. Stevens, Matthew R. Walter, and Yuxin Chen. Blending imitation and reinforcement learning for robust policy improvement. _ArXiv_ , abs/2310.01737, 2023. URL https://api.semanticscholar.org/CorpusID:263609068. 3 

- Xueyi Liu, Kangbo Lyu, Jieqiong Zhang, Tao Du, and Li Yi. Quasisim: Parameterized quasiphysical simulators for dexterous manipulations transfer. _arXiv preprint arXiv:2404.07988_ , 2024a. 2 

- Yun Liu, Haolin Yang, Xu Si, Ling Liu, Zipeng Li, Yuxiang Zhang, Yebin Liu, and Li Yi. Taco: Benchmarking generalizable bimanual tool-action-object understanding. _arXiv preprint arXiv:2401.08399_ , 2024b. 7, 21 

- Zhengyi Luo, Jinkun Cao, Josh Merel, Alexander Winkler, Jing Huang, Kris Kitani, and Weipeng Xu. Universal humanoid motion representations for physics-based control. _ArXiv_ , abs/2310.04582, 2023a. URL https://api.semanticscholar.org/CorpusID: 263829555. 3 

- Zhengyi Luo, Jinkun Cao, Alexander W. Winkler, Kris Kitani, and Weipeng Xu. Perpetual humanoid control for real-time simulated avatars. In _International Conference on Computer Vision (ICCV)_ , 2023b. 3, 5 

- Zhengyi Luo, Jinkun Cao, Sammy Joe Christen, Alexander Winkler, Kris Kitani, and Weipeng Xu. Grasping diverse objects with simulated humanoids. _ArXiv_ , abs/2407.11385, 2024. URL https://api.semanticscholar.org/CorpusID:271217823. 2, 3, 5, 8 

- Denys Makoviichuk and Viktor Makoviychuk. rl-games: A high-performance framework for reinforcement learning. https://github.com/Denys88/rl_games, May 2021. 8 

- Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 3, 7, 8 

- Igor Mordatch, Zoran Popovi´c, and Emanuel Todorov. Contact-invariant optimization for hand manipulation. In _Proceedings of the ACM SIGGRAPH/Eurographics symposium on computer animation_ , pp. 137–144, 2012. 2, 3 

- OpenAI. Gpt-4 technical report. 2023. URL https://api.semanticscholar.org/ CorpusID:257532815. 2 

- Tao Pang and Russ Tedrake. A convex quasistatic time-stepping scheme for rigid multibody systems with contact and friction. In _2021 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 6614–6620. IEEE, 2021. 2, 3, 8 

12 

Published as a conference paper at ICLR 2025 

- Tao Pang, HJ Terry Suh, Lujie Yang, and Russ Tedrake. Global planning for contact-rich manipulation via local smoothing of quasi-dynamic contact models. _IEEE Transactions on Robotics_ , 2023. 2, 3, 8 

- Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision_ , pp. 570–587. Springer, 2022. 2, 3 

- Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 2, 3 

- John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _ArXiv_ , abs/1707.06347, 2017. URL https://api. semanticscholar.org/CorpusID:28695052. 8 

- Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _ArXiv_ , abs/2309.06440, 2023. URL https://api. semanticscholar.org/CorpusID:259327055. 7, 8 

- Himanshu Gaurav Singh, Antonio Loquercio, Carmelo Sferrazza, Jane Wu, Haozhi Qi, Pieter Abbeel, and Jitendra Malik. Hand-object interaction pretraining from videos. 2024. URL https://api.semanticscholar.org/CorpusID:272600324. 2 

- Wen Sun, J. Andrew Bagnell, and Byron Boots. Truncated horizon policy search: Combining reinforcement learning & imitation learning. _ArXiv_ , abs/1805.11240, 2018. URL https:// api.semanticscholar.org/CorpusID:3533333. 3 

- Omid Taheri, Nima Ghorbani, Michael J Black, and Dimitrios Tzionas. Grab: A dataset of wholebody human grasping of objects. In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IV 16_ , pp. 581–600. Springer, 2020. 7, 21 

- Yinhuai Wang, Jing Lin, Ailing Zeng, Zhengyi Luo, Jian Zhang, and Lei Zhang. Physhoi: Physicsbased imitation of dynamic human-object interaction. _arXiv preprint arXiv:2312.04393_ , 2023. 2, 3 

- Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Huai hsin Chi, F. Xia, Quoc Le, and Denny Zhou. Chain of thought prompting elicits reasoning in large language models. _ArXiv_ , abs/2201.11903, 2022. URL https://api.semanticscholar.org/ CorpusID:246411621. 6 

- Bowen Wen, Wei Yang, Jan Kautz, and Stanley T. Birchfield. Foundationpose: Unified 6d pose estimation and tracking of novel objects. _2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 17868–17879, 2023. URL https://api. semanticscholar.org/CorpusID:266191252. 8, 22 

- Yueh-Hua Wu, Jiashun Wang, and Xiaolong Wang. Learning generalizable dexterous manipulation from human grasp affordance. In _Conference on Robot Learning_ , pp. 618–629. PMLR, 2023. 2, 3 

- Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng, Yijia Weng, Jiayi Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. _arXiv preprint arXiv:2303.00938_ , 2023. 2 

- Hui Zhang, Sammy Christen, Zicong Fan, Luocheng Zheng, Jemin Hwangbo, Jie Song, and Otmar Hilliges. Artigrasp: Physically plausible synthesis of bi-manual dexterous grasping and articulation. _arXiv preprint arXiv:2309.03891_ , 2023. 2, 3, 5 

- Sheng Zhong, Thomas Power, Ashwin Gupta, and Peter Mitrano. PyTorch Kinematics, February 2024. 7, 15 

13 

Published as a conference paper at ICLR 2025 

**Overview.** The **Appendix** provides a list of materials to support the main paper. 

- **Additional Technical Explanations (Sec. A).** We give additional explanations to complement the main paper. 

   - _Detailed Method Overview Figure_ . We include an overview figure for the method (Figure 6) that illustrates the method more detailed than the figure in the method section. 

   - _Data Preprocessing (Sec. A.1)_ . We present details of the kinematics retargeting strategy we leverage to create a dexterous kinematic robot hand manipulation dataset from human references. 

   - _Tracking Controller Training (Sec. A.2)_ . We explain additional details in the RLbased training scheme design, including the observation space and the reward. We also explain the control strategy for a floating base dexterous hand. 

   - _Homotopy Generator Learning (Sec. A.3)_ . We explain details in the homotopy generator learning. 

   - _Additional Details (Sec. A.4)_ . We present additional details w.r.t. the techniques. 

- **Additional Experimental Results (Sec. B).** We include more experimental results in this section to support the effectiveness of the method, including 

   - _Dexterous Manipulation Tracking Control (Sec. B.1)._ We present additional experiments of our methods as well as additional comparisons, including results achieved by using different training settings and additional qualitative results. We will also discuss more generalization ability evaluation experiments. 

   - _Real-World Evaluations (Sec. B.2)_ . We include more results of the real-world evaluations. We will discuss failure cases in the real-world evaluation as well. 

   - _Analysis on the Homotopy Optimization Scheme (Sec. B.3)._ We present qualitative results achieved by the proposed homotopy optimization method and comparisons to demonstrate the capability of the homotopy optimization as well as the effectiveness of the homotopy optimization path generator. Additionally, we discuss the generalization ability of the homotopy path generator. 

   - _Failure Cases (Sec. B.4)._ We discuss the failure cases for a comprehensive evaluation and understanding w.r.t. the ability of our method. 

- **Experimental Details (Sec. C)** . We illustrate details of datasets, models, training and evaluation settings, simulation settings, real-world evaluation settings, and the running time as well as the complexity analysis. Additionally, we attempt to ground some key properties of the tracking controller computationally and present quantified evaluations regarding these properties. 

We include a **video** and an **website** to introduce our work. The website and the video contain animated results. We highly recommend exploring these resources for an intuitive understanding of the challenges, the effectiveness of our model, and its superiority over prior approaches. 

## A ADDITIONAL TECHNICAL EXPLANATIONS 

**Overview figure of the method with details.** In figure 6, to present a comprehensive overview of our method, we draw a detailed overview figure that includes more important details than the figure of the original method in Section 3. 

### A.1 DATA PREPROCESSING 

**Kinematic retargeting.** We curate kinematic robot-object interaction data from human references by retargeting robot hand manipulation sequences from human hand trajectories. For instance, given a human hand-object interaction trajectory describing the human hand pose sequences represented in MANO and the object pose sequences ( **H**<sup>human</sup> ) _,_ **O** as well as the description of the articulated robot hand, we retarget **H**<sup>human</sup> to acquire the robot hand trajectory **H** . We manually define correspondences between the robot hand mesh and the MNAO hand mesh. After that, the sequence of the robot hand DoF positions is optimized so that the resulting robot hand mesh sequence is close to the 

14 

Published as a conference paper at ICLR 2025 



<!-- Start of picture text -->
Learning a Neural Tracking Controller from Demonstrations Mining High-Quality Robot Tracking Demonstrations<br>Object State 𝒔! Goal 𝒔"!"# ControllerTracking 𝜋 Action𝒂! Environment ResultTracking 𝒔!"# ReferencesKinematict Single TrajectoryTracking Policy {𝒂Expert ActionTrajectory%$, … , 𝒂!%, … } Expert TrackingResults t<br>Imitation Lossℒ! = 𝔼𝒂!∼$(⋅|𝒐!,𝒔+!"#)‖𝒂- −𝒂- . ‖ Reinforcement Learning ObjectivesLossActor ℒ& LossCritic ℒ' LossBound ℒ( … ControllerTracking 𝜋 the Tracking ControllerTracking Results from Single TrajectoryTracking Policy<br>Robot Tracking Demonstrations Task A Task B Task C<br>Homotopy Optimization …<br>𝒔"$Kinematic References… 𝒔"! 𝒔"!"# … Expert Action Trajectory𝒂%$ … 𝒂! % 𝒂%!"# … 𝒔%$Expert Tracking Results… 𝒔! % 𝒔%!"# … Tracking Path GeneratorKinematic References, TrackingResult TrackingResult TrackingResult<br>Task Object Shape An Effective Homotopy Optimization Path<br><!-- End of picture text -->

Figure 6: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It alternates between training the tracking controller using abundant and high-quality robot tracking demonstrations, and improving the data via the tracking controller through a homotopy optimization scheme. 

Table 3: Weights of different reward components. 

||_wo,p_|_wo,q_|_w_wrist_· w_trans|_w_wrist_· w_ornt|_w_finger|
|---|---|---|---|---|---|
|Weight|1.0|0.33|0.3|0.05|0.05|



human hand sequence. Formally, let **K**<sup>human</sup> and **K** denote the human hand keypoint sequence and the robot hand keypoint sequence respectively, the optimization objective is: 



We use PyTorch ~~K~~ inematics (Zhong et al., 2024) to calculate the forward kinematics. Specifically, given the robot hand per-joint DoF position _θn_ at the timestep _n_ , we calculate **h** _n_ and **k** _n_ as follows: 





where Forward ~~K~~ inematics( _·_ ) computes the forward kinematics using the function provided in PyTorch ~~K~~ inematics, KeyPoints( _·_ ) reads out keypoints from the converted articulated mesh. We use a second-order optimizer, _i.e.,_ L-BFGS implemented in PyTorch, to solve the optimization problem 5. 

### A.2 TRACKING CONTROLLER TRAINING 

**Controlling a floating-base articulated hand.** The articulated hand is represented in the reduced coordinate _θ_<sup>finger</sup> . We additionally add three translation joints and three revolute joints to control the global position and orientation of the hand, resulting in _θ_ = ( _θ_ )<sup>trans</sup> _, θ_<sup>rot</sup> _, θ_<sup>rot</sup> ). For the Allegro hand and the LEAP hand that we use in our experiments, _θ_<sup>finger</sup> is a 16-dimensional vector. Therefore, _θ_ is a 22-dimensional vector. 

**Observations.** The observation at each timestep _n_ encodes the current hand and object state, the next goal state, baseline trajectory, actions, and the object geometry: 



where aux _n_ is the auxiliary features, computed as follows: 



where ˆ **s** _n_ +1 _⊖_ **s** _n_ calculates the difference between two states, including the hand state difference and the object state difference, **f** _n_ indicates the hand finger positions in the world space. 

**Reward.** Our reward for manipulating tracking encourages the transited hand state and the object state to be close to their corresponding reference states and the hand-object affinity: 



15 

Published as a conference paper at ICLR 2025 

Table 4: **Quantitative evaluations and comparisons. Bold red** numbers for best values. Models are trained on training tracking tasks from both the GRAB and the TACO datasets. 

|Dataset|Method|_R_err (rad_, ↓_)|_T_err (_cm, ↓_)|_E_wrist(_↓_)|_E_finger (rad_, ↓_)|Success Rate (%_, ↑_)|
|---|---|---|---|---|---|---|
|GRAB|PPO (w/o sup., tracking rew.)|0.5813|6.03|0.1730|0.5439|36.04/55.84|
||Ours|**0.4515**|**4.82**|**0.14574**|**0.4574**|**42.64**/**61.42**|
|TACO|PPO (w/o sup., tracking rew.)|0.6751|6.37|**0.1264**|0.5443|21.67/50.25|
||Ours|**0.4782**|**3.94**|0.1329|**0.4228**|**32.02**/**62.07**|



where _ro,p, ro,q, r_ wrist _, r_ finger are rewards for tracking object position, object orientation, hand wrist, hand fingers, _wo,p, wo,q, w_ wrist _, w_ finger _, w_ affinity are their weights. _ro,p, ro,q, r_ wrist _, r_ finger are computed as follows: 



where **p**<sup>_o_</sup> _n_<sup>and</sup><sup>**q**</sup><sup>_o_</sup> _n_<sup>denote the position and the orientation, represented in quaternion, of the current</sup> object, **s**<sup>_h_</sup> _n_<sup>denotes the current hand state.In addition to these rewards, we would add an additional</sup> bonus reward 1 if the object is accurately tracked, _i.e.,_ with the rotation error kept in 5-degree and the translation error kept in 5-cm. Table 3 summarizes weights of different reward components we use in our experiments. 

**Pre-processing object features.** We train PonintNet-based auto-encoder on all objects from the two datasets we considered, namely GRAB and TACO. After that, we use the latent embedding of each object as its latent feature feeding into the observation of the tracking controller. The object feature dimension is 256 in our experiments. 

### A.3 HOMOTOPY GENERATOR LEARNING 

**Mining effective homotopy optimization paths.** The maximum number of iterations _K_ is set to 3 in our method to balance between the time cost and the effectiveness. 

We need to identify neighbors for each tracking task so that we can avoid iterating over all tasks and reduce the time cost. We use the cross-kinematic trajectory similarity to filter neighboring tasks. We pre-select _K_ nei =10 neighbouring tasks for each tracking task. 

### A.4 ADDITIONAL EXPLANATIONS 

In the reward design, we do not include the velocity-related terms since it is impossible for us to get accurate velocities from kinematic references. One can imagine calculating the finite differences between adjacent two frames as the velocities. However, it may not be accurate. Therefore, we do not use them to avoid unnecessary noise. 

## B ADDITIONAL EXPERIMENTS 

### B.1 DEXTEROUS MANIPULATION TRACKING CONTROL 

**Training the tracking controller on two datasets.** In the main experiments, the training data and the test data come from the same dataset. We adopt such a setting considering the large crossdataset trajectory differences. Specifically, GRAB mainly contains manipulation trajectories with daily objects, while TACO mainly covers functional tool-using trajectories. However, jointly using the trajectories from such two datasets to train the model can potentially offer us a stronger controller considering the increased labeled data coverage. Therefore, we additionally conduct this experiment where we train a single model using trajectories provided by the two datasets and test the performance on their test sets respectively. Results are summarized in Table 4, which can still demonstrate the effectiveness of our approach. 

16 

Published as a conference paper at ICLR 2025 

Table 5: Generalizability evaluations on the TACO dataset. 

|Test set|_R_err(rad_, ↓_)|_T_err (_cm, ↓_)|_E_wrist(_↓_)|_E_finger (rad_, ↓_)|Success Rate (%_, ↑_)|
|---|---|---|---|---|---|
|S1|0.5787|2.43|0.1481|0.4703|35.97/67.63|
|S2|0.6026|2.46|0.1455|0.4709|30.83/65.00|
|S3|0.6508|8.06|0.1513|0.4683|10.18/46.32|



Table 6: Performance comparisons across models trained with different amount of demonstration data. 

|Proportion|_R_err (rad_, ↓_)|_T_err (_cm, ↓_)|_E_wrist (_↓_)|_E_finger(rad_, ↓_)|Success Rate (%_, ↑_)|
|---|---|---|---|---|---|
|0.0|0.4985|4.42|0.1435|0.4767|31.03/57.64|
|0.1|**0.4730**|3.86|0.1502|0.4921|36.45/59.61|
|0.3|0.4903|2.94|**0.1256**|0.4804|40.89/62.07|
|0.5|0.4749|2.51|0.1680|0.4682|41.38/67.00|
|0.9|0.4776|2.29|0.1437|0.4839|44.83/72.91|
|1.0|0.4953|**2.10**|0.1510|**0.4661**|**48.77**/**74.38**|



**Comparisons with labeling the whole dataset for training the controller.** In our method we only try to label a small fraction of data in a progressive way leveraging the power of the tracking prior provided by the tracking controller and the homotopy paths proposed by the homotopy generator so that we can get high-quality demonstrations within an affordable time budget. One may wonder whether it is possible to label all the training dataset trajectories and train the tracking controller using those demonstrations. And if possible, what’s the performance of the model trained via this approach? We therefore manage to label each trajectory in the training dataset of the GRAB dataset by running the per-trajectory tracking experiments in parallel in 16 GPUs using two machines. We complete the optimization within one week. After that, we use the resulting demonstrations to train the trajectory controller. The final model trained in this way achieves 42.13% and 60.41% success rates under two thresholds. The performance can still not reach our original method where we only try to optimize high-quality demonstrations for part of the data (see Table 1 for details). We suppose it is the quality difference between the two labeled datasets that causes the discrepancy. This further validates our assumption that both the quantity and the quality of the labeled dataset matter to train a good tracking controller. 



<!-- Start of picture text -->
Timestamp<br>Kinematic<br>Reference<br>Ours<br><!-- End of picture text -->

Figure 7: **Robustness towards out-of-distribution objects and manipulations.** Please refer to **our website and the accompanying video** for animated results. 

**Further generalization ability evaluations on TACO dataset.** We further evaluate the model’s generalization ability across various test sets within the TACO dataset. As shown in Table 5, the controller performs well in the category-level generalization setting (S1), where object categories are known but manipulation trajectories and object geometries are novel. Performance on S2, involving novel interaction triplets, is satisfactory, demonstrating the controller’s capacity to handle new manipulation sequences. However, results from S3 reveal challenges when dealing with new object categories and unseen interaction triplets. For instance, generalizing from interactions with shovels and spoons to using bowls for holding objects is particularly difficult. As shown in Figure 7, despite unfamiliar objects and interactions, we successfully lift the knife and mimic the motion, though execution is imperfect, highlighting areas for improvement and adaptability in challenging scenarios. 

**Additional results.** We present additional qualitatively results in Figure 8 to further demonstrate the capability of our method. 

**Scaling the number of demonstration data.** In Table 6, we present the full evaluation results on all five types of metrics of each model traiend in the ablation study regarding the influence of the amount of demonstration data on model’s performance (see section 5 for details). 

17 

Published as a conference paper at ICLR 2025 



<!-- Start of picture text -->
Timestamp<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>(a) Waving a water scoop. ( Challenges:  in-hand re-orientations using fingers, complex object movements)<br>Retargeted<br>Kinematic<br>Trajectory<br>PPO<br>(tracking<br>rew.)<br>Ours<br>(b) Lifting a hand model. ( Challenges:  complex object movements)<br><!-- End of picture text -->

Figure 8: **Additional qualitative comparisons.** Please refer to **our website and the accompanying video** for animated results. 



<!-- Start of picture text -->
Table 7: Real-world quantitative comparisons (GRAB dataset). Bold red  numbers for best values.<br>Method apple banana duck elephant flashlight flute hammer hand phone waterbottle<br>PPO (w/o sup., tracking rew) 0/0/0 25.0/25.0/0.0 50.0/50.0/0 25.0/0.0/0.0 50.0/25.0/0 0/0/0 25.0/25.0/0 33.3/33.3/0 25.0/25.0/0 33.3/0/0<br>Ours 50.0 / 50.0 / 25.0 50.0 / 50.0 / 25.0 75.0 /50.0/ 50.0 50.0 / 50.0 / 50.0 75.0 / 50.0 / 25.0 25.0 / 25.0 /0.0 50.0 / 25.0 / 25.0 66.7 / 66.7 / 66.7 25.0 / 25.0 / 25.0 50.0 / 50.0 / 50.0<br><!-- End of picture text -->

B.2 REAL-WORLD EVALUATIONS 



<!-- Start of picture text -->
Timestamp  Timestamp<br><!-- End of picture text -->

Figure 9: **Additional real-world qualitative results.** Please refer to **our website and the accompanying video** for animated results. 

**Success thresholds.** We define three levels of success rates. The first level of success is defined as reaching the object, finding a good grasp pose, and exhibiting the potential movements to lift the object up, _i.e.,_ one side of the object is successfully lifted up from the table. The second level of success is defined as finding a way to manage to lift the whole object up from the table. The third level of success is lifting the object up, followed by keeping tracking the object’s trajectory for more than 100 timesteps. 

**More results.** For direct tracking results transferring setting, we present the quantitative success rates evaluated on our method and the best-performed baseline in Table 7 (for the dataset GRAB) and Table 8 (for the dataset TACO). As observed in the table, the tracking results achieved by our method can be well transferred to the real-world robot, helping us achieve obviously better results than the baseline methods. It validates the real-world applicability of our tracking results. 

Please refer to the main text (Sec. 4) for the quantitative comparisons between the transferred controllers. We include more qualitative results in Figure 9 to demonstrate the real-world application value of our method. 

18 

Published as a conference paper at ICLR 2025 

Table 8: **Real-world quantitative comparisons (TACO dataset). Bold red** numbers for best values. 



<!-- Start of picture text -->
Method soap shovel brush roller knife spoon<br>PPO (w/o sup., tracking rew) 33.3/0/0 25.0/0.0/0.0 25.0/0/0 25.0/25.0/0.0 0/0/0 25.0/0/0<br>Ours 100.0 / 66.7 / 66.7 50.0 / 25.0 / 25.0 25.0 / 25.0 /0.0 50.0 / 25.0 / 25.0 25.0 / 25.0 /0.0 50.0 / 50.0 / 25.0<br>Object about<br>to drop<br>Object about<br>to drop<br>Timestamp<br><!-- End of picture text -->

Figure 10: **Failure cases in real-world experiments.** Please refer to **our website** for animated results. 

**Failure cases.** A typical fail mode is that the object tends to drop from the hand as contact varies when attempting the in-hand manipulations, as shown in Figure 10. 

B.3 ANALYSIS ON THE HOMOTOPY OPTIMIZATION SCHEME 



<!-- Start of picture text -->
Timestamp<br>Retargeted<br>Kinematic<br>Trajectory<br>w/o<br>Tracking<br>Curriculum<br>w/<br>Tracking<br>Curriculum<br>(a) Lifting a thin flute.<br>Retargeted<br>Kinematic<br>Trajectory<br>w/o<br>Tracking<br>Curriculum<br>w/<br>Tracking<br>Curriculum<br>(b) Passing a small sphere.<br>Retargeted<br>Kinematic<br>Trajectory<br>w/o<br>Tracking<br>Curriculum<br>w/<br>Tracking<br>Curriculum<br>(c) Grasping an apple.<br><!-- End of picture text -->

Figure 11: **Effectiveness of the homotopy optimization scheme.** Please refer to **our website and the accompanying video** for animated results. 

We conduct further analysis of the proposed homotopy optimization scheme and the homotopy path generator to demonstrate their effectiveness. As shown in Figure 11, by optimizing through the homotopy optimization path, we can get better results in per-trajectory tracking. 

**Lifting thin objects.** As demonstrated in Figure 11a, for the originally unsolvable tracking problem where we should manage to lift a very thin flute up from the table, we can finally ease the tracking 

19 

Published as a conference paper at ICLR 2025 

Table 9: Generalization experiments on the homotopy <u>path generator.</u> 

|Homotopy test (a)|Homotopy test (b)<br>Homotopy test (c)|Homotopy test (d)|
|---|---|---|
|Effectiveness Ratio (%)<br>64.0|56.0<br>28.0|52.0|



difficulty by gradually solving each tracking problem in the homotopy optimization path proposed by the generator. 

**Grasping small objects.** As shown in Figure 11b, the original per-trajectory tracker fails to find a proper way to grasp the small sphere and lift it up from the table. However, empowered by the homotopy optimization, we can finally find a way to lift it up from the table. 

**Lifting a round apple.** Figure 11c demonstrates an effective homotopy optimization path that can let us lift an apple up from the table which would previously challenge the policy due to the round surface. 

**Generalization experiments on the homotopy path generator.** To further understand the generalization ability of the homotopy generator, we conduct the following tests: 

- (a) Train the path generator via homotopy paths mined from GRAB’s training set and evaluate it on the first test set that contains 50 tracking tasks uniformly randomly selected from remaining tracking tasks in GRAB’s training set that are not observed by the homotopy generator. 

- (b) Evaluate the path generator trained in (a) on the second test set that contains 50 tracking tasks uniformly randomly selected from the test tracking tasks of GRAB’s test set. 

- (c) Evaluate the path generator trained in (a) on 50 tracking tasks uniformly randomly selected from the test tracking tasks of TACO’s first-level test set. 

- (d) Train the path generator via homotopy paths mined from both GRAB’s and TACO’s training set and evaluate it on the test set used in (c). 

For each tracking task, if the tracking results obtained by optimizing through the optimization path are better than the original tracking results produced by RL-based per-trajectory tracking, we regard the generated homotopy optimization path as an effective one. Otherwise, we regard it as ineffective. We summarize the ratio of the effective homotopy optimization paths in Table 9. 

In summary: 

- (a) the homotopy path generator can perform relatively well in the in-distribution test setting; 

- (b) the performance would decrease slightly as the manipulation patterns shift a bit (please refer to section 4.1 for the difference between GRAB’s training split and the test split); 

- (c) the path generator would struggle to generalize to relatively out-of-distribution tracking tasks involving brand new objects with quite novel manipulation patterns; 

- (d) Increasing the training data coverage for the homotopy path generator would let it get obviously better. 



<!-- Start of picture text -->
Timestamp<br><!-- End of picture text -->











<!-- Start of picture text -->
Timestamp<br><!-- End of picture text -->









Figure 12: **Failure Cases.** Please refer to **our website and the accompanying video** for animated results. 

### B.4 FAILURE CASES 

Our method may fail to perform well in some cases where the object is from a brand new category with challenging thin geometry, as demonstrated in Figure 12. 

20 

Published as a conference paper at ICLR 2025 

## C ADDITIONAL EXPERIMENTAL DETAILS 



Figure 13: Examples of novel objects from the seen object category (TACO). 



Figure 14: Examples of objects from new object categories (TACO). 

**Datasets.** Our dexterous robot hand-object manipulation dataset is created by retargeting two public human-object datasets, namely GRAB Taheri et al. (2020), containing single-hand interactions with daily objects, and TACO Liu et al. (2024b), featured by functional tool using interactions. We retarget the full GRAB dataset and the fully released TACO dataset, obtaining 1269 and 2316 robot hand manipulation sequences respectively. For GRAB, we use sequences of the subject s1, with 197 sequences in total, as the test dataset. The training dataset is constructed by remaining sequences from other subjects. For the TACO dataset, we create one training set with four distinct test sets with different generalization levels for a detailed evaluation of the model’s generalization performance. Specifically, the whole dataset is split into 1) a training dataset, containing 1565 trajectories, 2) test set S0 where both the tool object geometries and the interaction triplets are seen during training containing 207 trajectories in total, 3) test set S1 where the tool geometry is novel but the interaction triplets are seen during training with 139 trajectories, 3) test set S2 with novel interaction triplets but seen object categories and geometries, containing 120 trajectories in total, and 4) test set S3 with 285 trajectories where both the object category and interaction triplets are new to the training dataset. Figure 13 and Figure 14 draw the examples of unseen objects from seen categories and the objects from new categories respectively. The original data presented in TACO often contains noisy initial frames where the hand penetrates through the table or the object. Such noise, though seems subtle, would affect the initial dynamics, however. For instance, if the hand initially penetrates through the table, a large force would be applied to the hand at the beginning, which would severely affect the simulation in subsequent steps. Moreover, if the hand initially penetrates through the object, the object would be bounced away at the start of the simulation. To get rid of such phenomena, we make small modifications to the original sequences. Specifically, we interpolate the phone pass sequence of the subject s2 from the GRAB dataset with such TACO sequences as the final modified sequence. Specifically, we take hand poses from the initial 60 frames of the GRAB sequence. We then linearly interpolate the hand pose in the 60th frame of the GRAB sequence with the hand pose in the 60th frame of the TACO sequence. For details, please refer to code in the supplementary material (refer “README.md” for instructions). 

**Training and evaluation settings.** For both GRAB and TACO, in the first stage, we first sample 100 trajectories from the training dataset. We train their per-trajectory trackers to obtain their action-labeled data to construct our first version of the labeled dataset. After that, 

Table 10: Total training time consumption <u>(TACO dataset).</u> 

||PPO<br>(w/o sup)|Ours<br>(w/o prior.,<br>w/o curri.)|Ours<br>(w/o prior)|Ours|
|---|---|---|---|---|
|Time|_∼_1 day|_∼_2 days|_∼_4 days|_∼_4 days|



the first tracking controller is trained and evaluated on all trajectories. We then additionally sample 100 trajectories from the remaining trajectories using the weights positively proportional to the tracking object position error. These sampled trajectories and those sampled in the first stage then form our second version of the dataset to label. We leverage both per-trajectory tracker optimization and the tracking prior from the first version of the trained tracking controller to label the data aiming to get high-quality labeled trajectories. After that, we search tracking curricula from such 200 trajectories and train a tracking curriculum scheduler using the mined curricula. We then construct 

21 

Published as a conference paper at ICLR 2025 

the second version of the action-labeled dataset using the final best-optimized trajectories. We then re-train the tracking controller and evaluate its performance on each trajectory. In the third stage, we sample additionally 200 trajectories from the remaining not selected trajectories. We then label them using the joint power of per-trajectory tracking optimization, tracking prior from the tracking controller, and the curriculum scheduled by the curriculum scheduler. After that, our third version is constructed using best-optimized labeled trajectories. We then re-train the tracking controller using this version of the labeled dataset. When training the tracking controller, we set a threshold in the reward, _i.e.,_ 50. Only trajectories with a reward above the threshold is used to provide supervision. Both the simulation and the policy run at 60Hz. The hand’s gravity is ignored in the simulation. Please refer to the code in the supplementary materials for detailed settings. We train all models in a Ubuntu 20.04.6 LTS with eight NVIDIA A10 cards and CUDA version 12.5. All the models are trained in a single card without multi-gpu parallelization. 



<!-- Start of picture text -->
RealSenseCamera from the Real World (bottle and cube)3D Printed Objects & Daily Objects<br>Leap Hand<br>Franka Arm<br><!-- End of picture text -->

Figure 15: Real-world experiment setup. 

**Real world experiment setup.** We use the Franka arm and LEAP hand to conduct real-world evaluations (Figure 15). When transferring the state-based policy, we use FoundationPose Wen et al. (2023) to estimate object poses. We use finite difference to estimate both the hand joint velocities as well as the object linear and angular velocities. Considering the gap between the control strategy we use in the simulator and the control of the Franka arm and the LEAP hand, we devise a strategy to mitigate the discrepancy between these two control methods. Specifically, instead of directly applying the control signal to the LEAP hand and the Franka arm, we set up a simulator with physical and control-related parameters same as our simulation settings during training. Then, in each timestep, we first apply the control commands to the simulated LEAP hand. We then simulate the hand. After that, we read the simulated state out from the simulator. We then calculate the positional target signal that should be applied to the real LEAP hand using the current obtained state from the simulator and the current state of the real LEAP hand. The calculated positional target signal is then directly fed to the real LEAP hand controller. In our observation, once the real hand has been commanded, it can almost reach exactly the same position in the command. Thereby, in practice, we directly use the state obtained from the simulator as the positional target command fed to the real LEAP controller. Experiments demonstrate the effectiveness of this control strategy. 

**Time consumption and time complexity.** Table 10 summarizes the total time consumption of different methods on the TACO dataset. Directly training PPO without any supervision is the most efficient approach while the performance lagged behind due to no proper guidance. Solving the per-trajectory tracking problem for providing high-quality data for training the general tracking controller would additionally increase the time consumption due to the requirement in optimizing per-trajectory trackers. Since we only select a subset from the whole training dataset, the time consumption is still affordable. Improving the per-trajectory trackers via mining tracing curricula would introduce additional time costs. Since the number of trajectories we consider for learning the curriculum scheduler is still controlled to a relatively small value. The final time cost is still relatively affordable. Experiments are conducted on a Ubuntu 20.04 machine with eight A10 GPU cards. For per-trajectory tracker optimization, we train eight trackers in parallel at one time. 

The overall time complexity of the training process is _O_ ( _|S|_ + _KK_ nei _|S|_ ). _S_ denotes the training dataset. 

**“Robustness”, “Generalization Ability”, and “Adaptivity”.** We try to give computational definitions of some crucial characteristics of the neural tracking controller. Please note that there is no standard formal computational definitions of such concepts, to our best knowledge. The definition and the quantification we present here is only from our perspective. 

22 

Published as a conference paper at ICLR 2025 

Table 11: **Generlaization score (GRAB dataset). Bold red** numbers for best values. 

|Method|DGrasp|PPO<br>(OmniGrasp rew.)|PPO<br>(w/o sup., tracking rew.)|Ours<br>(w/o data, w/o homotopy)|Ours<br>(w/o data)|Ours|
|---|---|---|---|---|---|---|
|_sg_|2.424|2.389|2.688|2.725|3.050|**3.251**|



Table 12: **Robustness score (GRAB dataset). Bold red** numbers for best values. 

|Method|PPO<br>(w/o sup., tracking rew.)<br>Ours|
|---|---|
|_sr_|2.665<br>**3.276**|



- To quantify the “generalization ability”, we need to first quantify 1) the distribution gap between two trajectory distributions, so that we can define the levels of generalization, 2) the generalization ability from the training distribution to the test distribution via the gap between the model performance: 

Denote _E_ as the distribution of the tracking task of the training set, and _D_ as the test distribution, we define their gap as follows: 



where Tracking ~~T~~ ask ~~D~~ iff( _·, ·_ ) measures the differnece between two manipulation trajectory tracking problem. For a trajectory tracking task described by the kinematic hand state sequence _{_ **s**<sup>_h_</sup> _n_<sup>_}N_</sup> _n_ =0<sup>,thekinematicobjectposesequence</sup><sup>_{_</sup><sup>**p**</sup> _n_<sup>_o,_</sup><sup>**q**</sup><sup>_o_</sup> _n_<sup>_}N_</sup> _n_ =0<sup>,andtheob-</sup> ject geometry PC, _e.g.,_ represented as the point cloud, we calculate the trajectory tracking task difference between two tracking tasks, _i.e.,_ **T** _A_ = _{{_ **s**<sup>_h,A_</sup> _n }, {_ **p**<sup>_o,A_</sup> _n_<sup>_,_</sup><sup>**q**</sup><sup>_o,A_</sup> _n_<sup>_},_PC</sup><sup>_A}_and</sup> **T** _B_ = _{{_ **s**<sup>_h,B_</sup> _n }, {_ **p**<sup>_o,G_</sup> _n ,_ **q**<sup>_o,G_</sup> _n },_ PC<sup>_B_</sup> _}_ , as a weighted sum of the hand trajectory difference, object pose sequence difference and the object geometry difference: 









where _wdiff_<sup>_h_= 0</sup><sup>_._1</sup><sup>_, w_</sup> _diff_<sup>_o,p_= 1</sup><sup>_, w_</sup> _diff_<sup>_o,q_= 0</sup><sup>_._3</sup><sup>_, w_</sup> _diff_<sup>_pc_= 0</sup><sup>_._5.For a tracking policy</sup><sup>_π_, define</sup> its performance on tracking tasks from the distribution _E_ via the expectation of tracking errors: 



where Tracking ~~E~~ rror _π_ ( _·_ ) evaluates the tracking error of the tracking policy _π_ on a trajectory tracking problem. It is a weighted sum of the difference between the tracking result and the reference trajectory of the robot hand and that of the object: 

Tracking ~~E~~ rror _π_ ( **T** ) = _werr_<sup>_o,pTerr_+</sup><sup>_w_</sup> _err_<sup>_o,qRerr_+</sup><sup>_w_</sup> _err_<sup>_h,wrist_</sup> _Ewrist_ + _werr_<sup>_h,finger_</sup> _Efinger,_ (20) where _werr_<sup>_h,wrist_</sup> = 0 _._ 1 _, werr_<sup>_h,finger_</sup> = 0 _._ 1 _, werr_<sup>_o,p_= 1</sup><sup>_._0</sup><sup>_, w_</sup> _err_<sup>_o,q_= 0</sup><sup>_._3.</sup> Therefore, the genralization ability of the policy _π_ trained to solve the trajectories from trianing distribution _E_ to the test distribution _D_ is measured as: 



where _ϵ_ is a small value to avoid numerical issue. The score _sg_ increases as the train-test distribution gap increases or the tracking error on the test distribution decreases. Using the above quantification w.r.t. the tracking task distribution gap and the generalization ability score, we summarize the generalization ability score of different kinds of models achieved on the GRAB dataset in Table 11. 

23 

Published as a conference paper at ICLR 2025 

Table 13: **Adaptativity score (GRAB dataset). Bold red** numbers for best values. 

|Method|PPO<br>(w/o sup., tracking rew.)|Ours|
|---|---|---|
|_sa_|0.317/0.098/0.0|**0.537**/**0.415**/**0.293**|



- To quantify the “robustness”, since it is quite difficult to analyze the dynamic function with a neural controller, we measure the robustness by the performance discrepancy between the tracking policy’s performance on the tracking tasks with relatively high-quality kinematic trajectories to those with disturbed kinematic references. 

To measure the “quality” of kinematic manipulation trajectories, we introduce three trends of quantities: 

- Smoothness: it calculates the difference between state finite differentiations : 



where **w** _s_ is the weight vector of each state DoF, ∆ _t_ is the time between two neighbouring frames. 

**–** Consistency: it calculates the hand object motion consistency: 



where **p**<sup>_o_</sup> _i_<sup>istheobjectpositionatframe</sup><sup>_i_while</sup><sup>**p**</sup><sup>_h_</sup> _i_<sup>isthehandwristpositionatthe</sup> frame _i_ . 

**–** Penetrations: it calculates the penetration between hand and object across all frames: 



where **P**<sup>_o_</sup> represents the object point cloud, Pene ~~D~~ epth calculates the maximum penetration depth between hand and the object. 

“Quality” of kinematic manipulation references can be grounded using such three measurements. Combining the above quantities, define the overall “quality” of the test distribution _L_ as: 



The “robustness” can be measured by the performance gap of the model on tracking tasks with “high-quality” references and those with “perturbed” thus “low-quality” tracking tasks. Denote the “high-qualtiy” tracking task distribution as _H_ while those with low quality as _L_ . Thus we can quantify the “robustness” as: 



As the quality of the trajectory distribution gets worse and the tracking error decreases, the “robustness score” would increase. 

To evaluate this, we construct a disturbed test set by adding random noise to the hand trajectory and the object position trajectory to test the trajectories of the GRAB dataset. After that, we test the performance of our method and the best-performed baseline, PPO (w/o sup., tracking rew.). We summarize the results in Table 12. 

- We mainly focus on the real-world adaptivity to evaluate the “adaptivity” of the tracking controller. Since it is hard to quantitatively measure the discrepancy between the real-world dynamics and that in the simulator, we use the model’s performance gap as the metric to directly evaluate the adaptivity. We use real-world per-trajectory average success rate to measure the “adaptivity”. For our real-world test on trajectories from the GRAB dataset, we summarize the result in Table 14. 

24 

Published as a conference paper at ICLR 2025 

Table 14: **Generlaization score (GRAB dataset). Bold red** numbers for best values. 

|Mthd|PPO|O|
|---|---|---|
|eo|(w/o sup., tracking rew.)|urs|
|_sa_|0.317/0.098/0.0|**0.537**/**0.415**/**0.293**|



Table 15: **Trajectory difficulty statistics.** 

||_s_<sup>_o_</sup><br>_smooth_<sup>(</sup><sup>_m · s−_2)</sup>|_vcontact_|_sshape_(_cm_<sup>_−_1</sup>)|
|---|---|---|---|
|GRAB|3.426|1.641|0.275|
|TACO|1.978|2.285|0.497|



**Computational interpretation of “hard-to-track”.** The most direct quantification is defining a score related to the tracking method’s performance. For the tracking method _M_ and the trajectory **T** , define _π_ is the best tracking policy that we can optimize for the trajectory **T** ( _i.e., π_ = _M_ ( **T** ). Given the tracking error Tracking ~~E~~ rror _π_ ( **T** ), the “hard-to-track” score could be defined as: _sht_ = <u>1</u> min(Tracking Error _π_ ( **T** ) _,ϵ_ )<sup>, where</sup><sup>_ϵ_is a small value to avoid numerical issue.</sup> 

Besides, we can use some statistics of the hand and object kinematic trajectories to quantify the “hard-to-track” characteristic. Here we introduce three types of statistics: 1) object movement smoohtness _s_<sup>_o_</sup> _smooth_<sup>:it quantifies the motion smoothness by calculating the per-frame average ob-</sup> <u>1</u> **p**<sup>_o_</sup> _i_ <u>+1</u><sup>_−_</sup><sup>**p**</sup> _i_<sup>_o_</sup> _−_ **p**<sup>_o_</sup> _i_<sup>_−_</sup><sup>**p**</sup><sup>_o_</sup> _i−_ 1 ject accelerations, _i.e., s_<sup>_o_</sup> _smooth_<sup>=</sup> _N −_ 1 � _Ni_ =1 _−_ 1<sup>_∥_</sup> ∆<sup><u>1</u></sup> _t_<sup>(</sup> ∆ _t_ ∆ _t_ ) _∥_ , 2) hand-object contact shifting velocity _vcontact_ : it quantifies the per-frame velocity of the contact map change, _i.e.,_ <u>1</u> _vcontact_ = _N_ � _Ni_ =1<sup>_∥_</sup><sup>**c**</sup><sup>_i_</sup> _N_<sup>_−_</sup> _p_<sup>**c**</sup> ∆<sup>_i−_</sup> _t_<sup>1</sup><sup>_∥_, where</sup><sup>**c**</sup><sup>_i∈{_0</sup><sup>_,_1</sup><sup>_}Np_is the binary contact map which encodes the</sup> contact flag between sampled points from the hand surface and the object, _Np_ is the number of points sampled from the hand, 3) object shape score _sshape_ : it is the z-axis extent of the object’s bounding box to quantify the shape of the object: _sshape_ = min(extent1 _z,ϵ_ )<sup>, where extent</sup><sup>_∈_R3is the</sup> extent of the bounding box of the object. We can jointly use these three trends of scores to quantify the “hard-to-track” characteristic. As _s_<sup>_o_</sup> _smooth_<sup>increases,</sup><sup>_vcontact_increases,and</sup><sup>_sshape_increases,</sup> the trajectory would get more “difficult”, thus “hard” to train a policy to track it. As shown in Table 15, the test trajectories in GRAB are more “difficult” than those in TACO w.r.t. the trajectory smoothness, while test trajectories in TACO are more difficult than those in GRAB regarding the contact velocity and the shape difficulty. 

**Additional details.** For tracking error metrics, we report the medium value of per-trajectory result in the test set, under the consideration that the average value may be affected by outliers. 

25 

