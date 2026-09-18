# **Towards Human-Level Bimanual Dexterous Manipulation with Reinforcement Learning** 

**Yuanpei Chen**<sup>1</sup> , **Tianhao Wu**<sup>2</sup> , **Shengjie Wang**<sup>1</sup> , **Xidong Feng**<sup>3</sup> , **Jiechuang Jiang**<sup>1</sup> , **Stephen Marcus McAleer**<sup>4</sup> , **Yiran Geng**<sup>1</sup><sup>_,_5</sup> , **Hao Dong**<sup>2</sup> , **Zongqing Lu**<sup>1</sup> , **Song-Chun Zhu**<sup>1</sup><sup>_,_5</sup> , **Yaodong Yang**<sup>1</sup><sup>_,_5</sup><sup>_,†_</sup> 

1Institute for AI, Peking University 

2Center on Frontiers of Computing Studies, Peking University 

3University College London 

4Carnegie Mellon University 

5Beijing Institute for General Artificial Intelligence 

## **Abstract** 

Achieving human-level dexterity is an important open problem in robotics. However, tasks of dexterous hand manipulation, even at the baby level, are challenging to solve through reinforcement learning (RL). The difficulty lies in the high degrees of freedom and the required cooperation among heterogeneous agents (e.g., joints of fingers). In this study, we propose the **Bi** manual **Dex** terous **Hands** Benchmark (Bi-DexHands), a simulator that involves two dexterous hands with tens of bimanual manipulation tasks and thousands of target objects. Specifically, tasks in Bi-DexHands are designed to match different levels of human motor skills according to cognitive science literature. We built Bi-DexHands in the Issac Gym; this enables highly efficient RL training, reaching 30,000+ FPS by only one single NVIDIA RTX 3090. We provide a comprehensive benchmark for popular RL algorithms under different settings; this includes Single-agent/Multi-agent RL, Offline RL, Multi-task RL, and Meta RL. Our results show that the PPO type of on-policy algorithms can master simple manipulation tasks that are equivalent up to 48-month human babies (e.g., catching a flying object, opening a bottle), while multi-agent RL can further help to master manipulations that require skilled bimanual cooperation (e.g., lifting a pot, stacking blocks). Despite the success on each single task, when it comes to acquiring multiple manipulation skills, existing RL algorithms fail to work in most of the multi-task and the few-shot learning settings, which calls for more substantial development from the RL community. Our project is open sourced at https://github.com/PKU-MARL/DexterousHands. 

## **1 Introduction** 

Humans have a skillful ability to manipulate objects of different shapes, sizes, and materials, which rely on the dexterity of our hands and fingers. Building a robot inspired by human hands that can autonomously manipulate various objects has always been an important component of the robotics field [1]. The development of human dexterity begins in infancy and is influenced by what the physical environment provides, including the objects available to the child [2]. As infants and children develop physical and intelligence, they are more likely to attempt complex movements, and often learn dexterity through attempting movements and the consequences of their actions [3, 4, 5]. Similarly, robot dexterity can not be a constant program pre-set in the laboratory. To acquire the capability of object manipulations in the real world, robots must be able to learn dexterous manipulation skills as if we were infants. As a result, we expect robots to learn to master the ability of dexterous manipulation at the human level from daily tasks. 

_†_ : Corresponding to <yaodong.yang@pku.edu.cn> 

36th Conference on Neural Information Processing Systems (NeurIPS 2022) Track on Datasets and Benchmarks. 

Recently, reinforcement learning (RL) algorithms have outperformed human experts in many fields that require decision makings [6, 7]. In contrast to the traditional control methods, RL can complete some challenging tasks in learning dexterous in-hand manipulation [8, 9, 10] or grasping [11, 12]. However, manipulation that generates changes on the object is still difficult [13]. More difficult is generalization across tasks, although previous work can achieve simple level of tasks such as throwing [14], sliding [15], poking [16], pivoting [17], and pushing [18], but is still difficult to perform well in unstructured or contact-rich environments, which require the ability to combine and generalize complex manipulation skills. In a nutshell, reaching human-level sophistication of hand dexterity and bimanual coordination remains an open challenge for modern robotics researchers. 

To help solve the problems mentioned above and let robots have the same dexterous manipulation ability as humans, we developed, in the Isaac Gym [19] simulator, a novel benchmark on bimanual dexterous manipulation for RL algorithms along with a diverse set of tasks and objects named **BiDexHands** . We follow the principle of Fine Motor Subtest (FMS) [20] to design tens of tasks, which provides the opportunities to observe and evaluate specific skills that demonstrate a child’s ability to use their hands to play with toys, manipulate objects, and use tools. Next, we tested the baselines of various model-free RL algorithms to show the ability of the baseline algorithm in these tasks, not only the standard RL algorithms but also multi-agent RL (MARL), offline RL, multi-task RL, and Meta RL algorithms, each of them focuses on the bimanual collaboration, learning from demonstration, and task generalization, respectively. Our major goal is to facilitate researchers to master human-level bimanual dexterous manipulations with RL. Not limited to this, we also hope this study to provide a new platform for the community of RL, robotics, and cognitive science. Bi-DexHands are developed with the following key features: 

- **Isaac Gym Efficiency** : Building on the Isaac Gym simulator, Bi-DexHands supports running thousands of environments simultaneously. On one NVIDIA RTX 3090 GPU, Bi-DexHands can reach 30,000+ mean FPS by running 2,048 environments in parallel. 

- **Comprehensive RL Benchmark** : We provide the first bimanual manipulation task environment for common RL, MARL, offline RL, multi-task RL, and Meta RL practitioners, along with a comprehensive benchmark for SOTA continuous control model-free RL methods. 

- **Heterogeneous-agent Cooperation** : Agents in Bi-DexHands ( _i.e._ , joints, fingers, hands,...) are genuinely heterogeneous; this is different from common multi-agent environments such as SMAC [21] where agents can simply share parameters to solve the task. 

- **Task Generalization** : We introduced a variety of dexterous manipulation tasks (e.g., hand over, lift up, throw, place, put...) as well as enormous target objects from the YCB [22] and SAPIEN [23] dataset, thus allowing meta-RL and multi-task RL algorithms to be tested on the task generalization front. 

- **Cognition** : We provided the underlying relationship between our dexterous tasks and the motor skills of humans at different ages. This facilitates researchers on studying robot skill learning and development, in particular in comparison to humans. 

## **2 Related Work** 

Today, robots are skilled in some repetitive and familiar environments like assembled in the factory. Grasping is a milestone in robotics manipulation. For decades, researchers have been working to establish a stable grasping theory [24]. However, most previous methods have relied on various assumptions, such as known object information or no uncertainty in the process. In recent years, data-driven approaches have been successful in this regard, being able to deal with uncertainty in perception and generate grasping methods for known, familiar, and even unknown objects in real-time [25]. Grasping is only a part of the manipulation. Today’s robots can perform some simple behaviors like grasping, pushing, and throwing. But it is still difficult to manipulate in unstructured scenes and contact-rich situations. Moving objects while in-hand manipulation is also a complex challenge. One step to address this challenge is to use hands with intrinsic dexterity [26, 27], which often mimic human hands [28]. Another undeveloped area is bimanual manipulation, a method of using a second hand to provide additional dexterity [29, 30]. Learning for manipulation is important for robots to continuously learn and achieve intelligent control. It is especially suitable for modeling manipulation on complex non-rigid objects and reducing control dimensions [31], but it still suffers from problems such as lack of accurate models, reality gaps, and difficulty in collecting expert data. There are many other robotic manipulation benchmarks [32, 33, 34], but none of them use dexterous 

2 

hands. Therefore, our work proposes a bimanual dexterous manipulation benchmark, hoping to facilitate researchers to address the challenges of robotic manipulation we mentioned above. 

Dexterous five-finger hands provide an essential tool to perform a multitude of tasks in human-centric environments. However, such dexterous manipulation remains a challenging problem because of the high dimensional actuation space and contact-rich model. Before the emergence of RL-based controllers, a large variety of manipulation tasks highly relied on accurate dynamics models and trajectory optimization methods [35, 36, 37]. For example, Williams et al. [38] used the model predictive path integral control (MPPI) method to perform the task successfully, dexterous manipulation of a cube. Charlesworth et al. [39] improved the MPPI method to make the handing over task between two hands tractable. Since RL simplifies the design process of the controller, model-agnostic approaches have become more and more popular in the field of robotic control [40, 41]. In terms of dexterous manipulation, many works achieve a significant improvement compared with traditional controllers. OpenAI et al. [9] developed an RL-based controller to reorient a block or a Rubik’s cube. Considering the poor generalization of current approaches, Chen et al. [10] presented an efficient system for learning how to reorient a large number of objects without access to shape information. Qin et al. [42, 43] perform learning from demonstrations for dexterous manipulation collected from teleoperation or video. While their studies demonstrate that RL enables efficient and scalable learning on single-hand manipulation, bimanual manipulation remains a hardship for model-free reinforcement learning [39]. In this paper, our benchmark provides a wide range of well-designed and challenging daily life scenarios for comprehensive RL algorithms, hoping to help the researcher toward master human-level bimanual dexterous manipulation. 

## **3 Formulations** & **Algorithms** 

In order to create a platform toward mastering human-level dexterity, we use two Shadow Hands to manipulate in our environment. Shadow Hand [44] is a popular robotic hand usually used in some dexterous manipulation tasks. It is designed to resemble the typical human male hand in shape and size, and capable of performing a variety of flexible and delicate operations. Shadow Hand’s DoF is shown in Fig.1, designed to mimic the human skeleton as much as possible. Concretely, the 24-DoF hand is actuated by 20 pairs of agonist-antagonist tendons, while the other four joints remain underactuated. 



<!-- Start of picture text -->
7 11 15<br>3 12 16<br>8<br>4<br>9 10 13 14 17 18 20<br>5 6 21 22<br>23<br>19 24<br>2<br>1<br><!-- End of picture text -->

Figure 1: Degree-Of-Freedom (DOF) configuration of the Shadow Hand similar to the skeleton of a human hand. 

Furthermore, our low-level controller runs at 1k Hz, as well as the RL-based policy outputs the relative positions of actuated joints at 30 Hz. It is worth noting that compared with previous studies, the base of the hand is not fixed in some tasks. Instead, the policy can control the position and orientation of the base within a restricted space, which takes advantage of the function of the wrist, thus making the Shadow Hand more bio-mimetic. Meanwhile, we can efficiently perform the task in real-world applications by linking the base to a robotic arm. Refer to Appendix A.1 for more details about the physical parameters of the Shadow Hand. 

Our benchmark aims at providing solutions for bimanual dexterous manipulation in a comphensive field of RL. To achieve that, We consider five RL formulations including: Single-agent RL, Multiagent RL (MARL), Offline RL, Multi-task RL, and Meta-RL in Bi-DexHands. In the following part, we will introduce the detailed formulation and the corresponding implemented algorithms in our benchmark of these five RL formulations. 

**RL/MARL.** In order to evaluate the performance of RL/MARL [45, 46], we formulate our scenarios as a decentralized partially observable MDP (Dec-POMDP). The Dec-POMDP consists of 10 components, _Z_ = _< N , M, S,_ **_O_** _,_ **_A_** _,_ **Π** _, P, R, ρ, γ >_ . Initially, the robotic hands are manually separated as _N_ agents, the set of which represents _M_ . When starting the simulation, the state of the environment (i.e., the information of robots and objects) is set at _s_ 0 _∈ S_ according to the initial distribution of states _ρ_ ( _s_ 0). Then at the time step _t_ , _st_ represents the state, and the i-th agent receives an observation _o_<sup>_i_</sup> _t_<sup>_∈_</sup><sup>**_O_**relying on</sup><sup>_st_.Hereafter, the policy of the i-th agent,</sup><sup>_πi∈_</sup><sup>**Π**, takes the</sup><sup>_oi_</sup> _t_<sup>as</sup> input, and outputs an action _a_<sup>_i_</sup> _t_<sup>_∈Ai_.Additionally, we denote the joint action of all agents by</sup><sup>**_a_**</sup><sup>_t∈_</sup><sup>**_A_**,</sup> 

3 



<!-- Start of picture text -->
Tasks<br>Reach Catch Atomic Actions Task Environment distribution Learning Process<br>⋯ Place Combine<br>Throw RL  Algorithms Multi-agent RL  Multi-task RL<br>Pick PPO TRPO MAPPO HAPPO MTPPO MTSAC<br>Dataset DQN A3C ⋯ ⋯<br>Left Hand Right Hand SAC DDPG Meta RL  Offline RL<br>NPG TD3 MAML 𝑹𝑳 𝟐 BCQ TD3-BC<br>⋯ ⋯ ⋯<br><!-- End of picture text -->

Figure 2: Framework of Bi-DexHands, a bechmark for learning bimanual dexterous manipulation. 

and the equation **_A_** = [ _A_ 1 _, ..AN_ ] is naturally satisfied. After that, i-th agent can obtain a reward _rt_<sup>_i_</sup> based on _R_ ( _st,_ **_at_** ), as well as all agents transitions to the next state _st_ +1 with the possibility of the transition function _P_ ( _st_ +1 _|st,_ **_a_** _t_ ). The goal is to find the optimal policy **Π** to maximize the sum of rewards E **Π** [<sup>�</sup><sup>_T_</sup> _t_ =0<sup>_−_1</sup><sup>_γt_�</sup> _i_<sup>_N_</sup> =1<sup>_r_</sup> _t_<sup>_i_] in an episode with</sup><sup>_T_time steps.It should be pointed out that when</sup> _N_ = 1, it is the problem formulation of single-agent RL. 

In this setting, We implemented state-of-the-art continuous single-agent RL algorithms, such as PPO [47], SAC [48], TRPO [49], DDPG [50], and TD3 [51] algorithms. Taking our continuous control and fully cooperative environments into consideration, we introduced HAPPO/HATRPO [52, 53, 54], MAPPO [55], IPPO [56], and MADDPG [57] algorithms. 

**Offline RL.** Offline RL follows the formulation of standard MDP, where the goal is to maximize the expected return E _π_ [<sup>�</sup><sup>_T_</sup> _t_ =0<sup>_−_1</sup><sup>_γtrt_].However, in offline RL, the agent has to learn policy only using</sup> the transitions in previously collected dataset _D_ = _{_ ( _st, at, st_ +1 _, rt_ ) _}_ , without interacting with the environment. The fundamental challenge of offline RL is value errors of out-of-distribution actions [58]. We implemented BCQ [59], TD3+BC [58], and IQL [60] algorithms for offline RL. 

**Multi-task RL.** Multi-task reinforcement learning aims to train a single policy _π_ ( _a|s, z_ ), which can achieve good results on different tasks. _z_ represents an encoding of the task ID. The goal of our policy is to maximize the reward given by E _T ∼p_ ( _T_ )[E _π_ [<sup>�</sup> _t_<sup>_T_</sup> =0<sup>_−_1</sup><sup>_γtrt_], where</sup><sup>_p_(</sup><sup>_T_) is a task distribution in</sup> our benchmark. In practice, multi-task RL adds the context vector corresponding to the type of environment (e.g., one-hot task ID) into states to learn a general skill. We implemented multi-task PPO, multi-task TRPO, and multi-task SAC algorithms for multi-task RL. 

**Meta RL.** Meta RL [61], also known as "learning to learn", aims to gain the ability to train on tasks to extract the common features of these tasks, so as to quickly adapt to new and unseen tasks. In Meta-RL, both training and test environments are assumed to follow the same task distribution _p_ ( _T_ ). In Bi-DexHands, we design some common structures between different tasks for meta-training to ensure that it can adapt efficiently to new tasks. Compared with Multi-task RL, Meta RL is not allowed to get direct task-level information such as task ID. It needs to solve entirely new tasks by task inference and adaptation purely based on interactions. We implemented model-agnostic meta learning (MAML) [62] and proximal meta-policy search (ProMP) [63] algorithms for Meta RL. 

## **4 Bimanual dexterous manipulation benchmark** 

In this section, we will discuss the construction of Bi-DexHands, a benchmark for bimanual dexterous manipulation over diverse scenarios. 

### **4.1 System design** 

As we mentioned before, the core of Bi-DexHands is to build up a learning framework for two Shadow Hands capable of diverse skills as humans, such as reaching, throwing, catching, picking and placing. To be specific, Bi-DexHands consists of three components: datasets, tasks, and learning algorithms, as shown in Fig.2. Varying worlds provide a large number of basic settings for robots, including the configuration of robotic hands and objects. Meanwhile, a variety of tasks corresponding to children’s behaviors at different ages make it possible to learn dexterity like a human. Combining a dataset and task, we can generate a specific environment or scenario for the following learning. Eventually, our experiments demonstrate that reinforcement learning is able to facilitate the robots to achieve some remarkable performance on such challenging tasks, and there is still some room for improvement and more difficult tasks for future work. 

4 

### **4.2 Construction of datasets** 

The construction of the datasets corresponds to the configuration of robots and objects. The core goal of datasets is to generate a large variety of scenes for robot learning. As we mentioned in the last part, the robots in our benchmark are two dexterous Shadow Hands. Other than the robots, the objects also play an essential role in constructing the datasets. For extending the types of tasks, we introduced a variety of objects from the YCB [22] and SAPIEN [23] datasets. Two datasets contain many everyday objects. Notably, the SAPIEN dataset provides many articulated objects with motion annotations and rendering material, which means these objects are close to the real ones significantly. Therefore, it provides a natural way to build a connection between the worlds of our benchmark and scenes of daily life. Concretely, Fig.2 shows the construction of datasets, and we can see that the object includes pots, pens, eggs, scissors, eyeglasses, doors, and other common tools. After defining the configuration of robots and the type of objects, we build the specific world based on the Isaac Gym simulator. Meanwhile, each world defines variable initial poses of robots and objects, providing a diverse set of environments. 

### **4.3 Design of tasks** 

An infant’s behavior experiences a multi-stage development, such as social, communication, and physical parts [64]. Particularly in bimanual dexterous manipulation, there are some relationships between some common behaviors of babies and the ages. To gain insights into the underlying relationships, we conducted an in-depth analysis and built a mapping between the baby’s age and tasks according to the Fine Motor Subtest (FMS) [20]. As the baby’s age increases, the difficulty of completing the designed tasks also increases, because the baby can complete more and more difficult behaviors as the body develops. So it is also of great importance to evaluate the performance of trained agents, because we can roughly point out agents’ intelligence level by analogy with a baby’s movement for bimanual dexterous manipulation. An overview of the correspondence of our tasks to the FMS is shown in Table.1. For more details on the tasks, please refer to Appendix A.2. 

### **4.4 Design of Multi-task/Meta RL** 

The design of our Multi-task/Meta RL categories is generally similar to Meta-World [32], divided into ML1, MT1, ML4, MT4, ML20, and MT20. Each of our tasks has object variation, which as we can interact with different kinds of objects in daily life scenes, providing a foundation for us to learn dexterous manipulation like humans. In the following, we will introduce 6 tasks categories for Multi-task/Meta-RL. More details can refer to Appendix D. 

**MT1&ML1: Learning a multi-task policy & Few-shot adaptation within one task:** Both ML1 and MT1 are categories for generalization ability within the same task, and their generalization ability is reflected in the ability to complete tasks under different goals. ML1 uses meta-reinforcement learning for few-shot adaptation, in which goal information will not be provided. MT1 uses the multi-task method for generalization, and the information on the goal will be provided in a fixed set. 

**MT4&MT20: Learning a multi-task policy belonging to 4&20 training tasks:** MT4 and MT20 conduct policy training in 4&20 tasks and hope to complete all tasks in only one policy. In MT4, we hope to learn policy with similar human skills, so we try to combine similar tasks as much as possible. MT20 uses all of our 20 tasks. In MT4 and MT20, we use a one-hot task ID to represent different tasks, and the information on the goal will be provided in a fixed set. 

**ML4&ML20: Learning a Few-shot adaptation for new 1&5 test tasks from 3&15 training tasks:** ML4 and ML20 are categories for learning meta-policies in 3&15 tasks respectively and hoping to adapt to new 1&5 testing tasks. There is no doubt that this is a difficult challenge. We choose the tasks which using the catch behavior for design in ML4. The ML20 requires adaptation in all 15 tasks with large differences designed according to baby intelligence, which is the most difficult challenge in our benchmark. Similarly, we will variate the goal for each task, and will not provide task information, requiring Meta RL algorithms to identify the tasks. 

## **5 Benchmarking reinforcement learning algorithms** 

In this section, we conduct a full benchmark of the RL algorithms in Bi-DexHands. We firstly quantify our environment speed to demonstrate the running efficiency of Bi-DexHands. Then We offer the benchmark results and corresponding discussion and analysis on those five RL formulations. All of our experiments are run with Intel i7-9700K CPU @ 3.60GHz and NVIDIA RTX 3090 GPU. For the hyperparameters of all algorithms, please refer to Appendix B. 

5 

Table 1: Task name and the description of the human skill in the corresponding age. References under the human age are the cognitive science literature referenced for the behavior designed, and the difficulty level of the tasks is under the task name. Easy level tasks are more basic skills, medium level tasks need more precise control and finger dexterity, and hard level tasks require handing dynamic interaction and tool use. 

|**Human Task Name**|**Human’s Skill Description**|**Age (months)**|**Demo**|
|---|---|---|---|
|Push Block<br>Easy|Child extends one or both arms<br>forward and touches the block with<br>any part of either hand|5-6<br>[20, Chapter 3]||
|Open Scissor &<br>Open Pen Cap<br>Easy|They use one hand to hold<br>a toy and the other hand<br>manipulate it|7<br>[65, Chapter 4]||
|Turn Button<br>ON/OFF<br>Easy|They can push and squish soft<br>stuff or push hard things, like a<br>button on a toy phone or popup toy|11<br>[66, 11 months]||
|Swing Cup<br>Easy|They can turn a ball on their toy<br>mobile, a steering wheel on a toy<br>car, or the faucet in the tub|11<br>[66, 11 months]||
|Lift Pot &<br>Lift Cup<br>Easy|They can put a sippy cup to their<br>mouth to drink|12<br>[66, 12 months]||
|Door Open &<br>Close<br>Easy|Toddlers can open and close<br>cupboards and oven doors|13<br>[66, 13 months]||
|Re-Orientation<br>Medium|Infant further refines this ability<br>to differentiate individual finger<br>movement and manipulate objects|18<br>[65, Chapter 4]||
|Stack Block(2,6,8)<br>Medium|Child stacks at least 2/6/8 blocks<br>in any trial.|2:22-28<br>6,8:33-42<br>[20, Chapter 3]||
|Pull a Ball into<br>Bucket<br>Medium|Child place s 10 pellets in the<br>bottle in 60 seconds or less, one<br>pellet at a time.|22-28<br>[20, Chapter 3]||
|Open Bottle Cap<br>(prismatic joint)<br>Medium|Uses hands to twist things, like<br>turning doorknobs or unscrewing<br>lids|30<br>[67, Table 6]||
|Catch Underarm<br>Hard|Catches a large ball most of the<br>time|48<br>[67, Table 6]||
|Pour Water<br>Hard|Serves himself food or pours<br>water, with adult supervision|48<br>[67, Table 6]||
|Two Catch<br>Underarm<br>Hard|Some adults can throw objects<br>between two hands like magic|adult||



6 

### **5.1 Environmental speed** 

Thanks to Isaac Gym’s high-performance GPU parallel simulating capabilities, we can greatly improve the sampling efficiency of our RL algorithm while using fewer computing resources. We believe that the high sampling efficiency improves the exploration ability of the RL algorithm, allowing us to successfully learn the bimanual dexterous manipulation policy. To demonstrate the Isaac Gym’s efficiency of Bi-DexHands, We provided some results of environmental speed in Table.2 by running on-policy algorithms. Both PPO and HAPPO can achieve more than 20k FPS. 

Table 2: Mean and standard deviation of FPS (frame per second) of the environments in Bi-DexHands. 

|Algorithms|CatchUnderarm|CatchOver2Underarm|CatchAbreast|TwoCatchUnderarm|
|---|---|---|---|---|
|PPO|35554_±_613|35607_±_344|35164_±_450|32285_±_898|
|HAPPO|23929_±_98|23827_±_135|23456_±_255|23205_±_168|



### **5.2 RL/MARL results** 

Currently, we evaluate the performance of PPO, SAC, TRPO, MAPPO, HATRPO and HAPPO algorithms on these 20 tasks, and we implemented the rest of the RL/MARL algorithms in our Github repository. The performance of each algorithm are shown in Figure 3. Note that the experiments of MARL algorithms run based on two agents, which means each hand represents an agent. It can be observed that the PPO algorithm performs well on most tasks. Although there are some tasks that require two-hand cooperation, PPO algorithm is still better than HAPPO, MAPPO algorithms in most cases. This may be because PPO algorithm is able to use all observations for training the policy, while MARL can only use partial observations. However, in most tasks, the more difficult and require the cooperation of both hands, the smaller the performance gap between PPO and HAPPO, MAPPO, indicating that the multi-agent algorithm can improve the performance of bimanual cooperative manipulation. Another finding is that the SAC algorithm does not work on almost all tasks. It may be due to 1) the off-policy algorithm has a lower improvement in high sampling efficiency than on-policy. 2) The policy entropy of SAC brings instability to policy learning under the high-dimension input. We discuss this finding in detail in Appendix C. 

### **5.3 Offline RL results** 

We build offline datasets with four datatypes, _i.e._ , random, replay, medium, and medium-expert. The data collection follows that in D4RL-MuJoCo [68], which is a standard offline benchmark, and the details are given in Appendix A.3. We evaluate behavior cloning (BC), BCQ [59], TD3+BC [58], and IQL [60] on two tasks, Hand Over and Door Open Outward, and report normalized scores in Table 3. BCQ and TD3+BC could obtain significant performance improvement compared with behavior policy (BC). However, the action space and state space in Bi-DexHands are much larger than that in MuJoCo, which means the problem of out-of-distribution action [58] is more severe in Bi-DexHands datasets. That is the reason why IQL could only achieve performance improvement in several datasets. Due to the potential large distribution shift, we believe Bi-DexHands can be a more challenging and meaningful offline benchmark for offline RL research. 

Table 3: Normalized score in offline tasks. 

|Tasks|Datasets|Online PPO|BC|BCQ|TD3+BC|IQL|
|---|---|---|---|---|---|---|
||random|100_._0|0_._7_±_0_._2|1_._0_±_0_._1|0_._9_±_0_._2|0_._7_±_0_._4|
|Hand Over|replay|100_._0|17_._5_±_3_._5|61_._6_±_4_._9|**70****_._1**_±_2_._1|43_._1_±_2_._3|
||medium|100_._0|61_._6_±_1_._0|**66****_._1**_±_1_._9|**65****_._8**_±_2_._2|57_._4_±_1_._5|
||medium-expert|100_._0|63_._3_±_1_._4|**81****_._7**_±_4_._9|**84****_._9**_±_5_._3|67_._2_±_3_._6|
||random|100_._0|2_._1_±_0_._6|23_._8_±_2_._9|**34****_._9**_±_4_._3|3_._8_±_1_._0|
|Door|replay|100_._0|36_._9_±_4_._3|48_._8_±_4_._5|**60****_._5**_±_2_._6|31_._7_±_2_._0|
|Open Outward|medium|100_._0|63_._9_±_0_._7|60_._1_±_2_._3|**66****_._3**_±_0_._7|56_._6_±_1_._2|
||medium-expert|100_._0|69_._0_±_6_._4|**73****_._7**_±_4_._5|**71****_._9**_±_3_._5|53_._8_±_1_._8|



### **5.4 Generalization ability** 

The goals of our generalization evaluation is 1) to find out the ability of current multi-task and meta reinforcement learning algorithms to generalize on the tasks we designed. 2) to find out whether 

7 



Figure 3: Learning curves for all 20 tasks. The shaded region represents the standard deviation of the score over 10 trials. Curves are smoothed uniformly for visual clarity. All algorithms interact with environments in 100M steps and the number of parallel simulations is 2048. 

the tasks that are harder for babies are also harder for RL. The previous RL/MARL results have proved that our individual task is solvable. For goal 1), we evaluate the multi-task PPO [47] and ProMP [63] algorithms on MT1, ML1, MT4, ML4, MT20, and ML20. We also provided the results of random policy and using the PPO algorithm in individual task as the ground truth for comparison. The average reward for each training is shown in Table 4. We can observe that the multi-task PPO does not perform well, and the ProMP have tiny performance improvement compared with random policy. It may because it’s hard to learn policy from individually each task itself in Bi-DexHands. Therefore, we still have a lot of room to improve the generalization ability of bimanual dexterous hands under cross-task setting, which is a meaningful open challenge for the community. 

Table 4: The average reward of all tasks for MT1, ML1, MT4, ML4, MT20, and ML20 on 10 seeds. 

|Method|MT1|MT4|MT20|Method|ML<br>train|1<br>test|M<br>train|L4<br>test|ML<br>train|20<br>test|
|---|---|---|---|---|---|---|---|---|---|---|
|Ground Truth|15.2|24,3|32.5|Ground Truth|15.0|15.8|28.0|13.1|33.7|26.1|
|Multi-task PPO|9.4|5.4|8.9|ProMP|0.95|1.2|2.5|0.5|0.02|0.36|
|Random|0.61|1.1|-2.5|Random|0.59|0.68|1.5|0.24|-2.9|0.27|



For goal 2), we use random and ground truth reward to normalize the results of all tasks in MT20 and arrange them in the order of increasing age. The results is shown in Fig.4. It can be seen that in general, as the age of the person corresponding to the task increases, the difficulty for RL also increases, which proves that our task design is designed with rationality and relevance to people. 

## **6 Conclusion and Future Work** 

We introduced a benchmark, Bi-DexHands, which consists of well-designed tasks and a large variety of objects for learning bimanual dexterous manipulation. We investigated the motor development process of infants’ dexterity from cognitive science, and carefully designed more than twenty tasks for RL based on the results, hoping that robots can learn dexterity like humans. With the help of the Isaac 

8 



<!-- Start of picture text -->
1.2<br>0.99<br>1<br>0.81 0.82 Increasing Age<br>0.8 0.7<br>0.6 0.43 0.47 0.42<br>0.4<br>0.2 0.17 0.21 0.18 0.13 0.2 0.08<br>0.00075 0.01 0.0016 0.011 0.0025 0.031 0.0013<br>0<br>push block open pen cap open scissors switch swing cup lift door close inward door open inward close outward door open outward re orientation stack block grasp& place open bottle cap hand over catch underarm catch over2 underarm catch abreast pour water two catch underarm<br>underarm door<br><!-- End of picture text -->

Figure 4: The normalized reward run by the MTPPO algorithm under the MT20 setting. The tasks from left to right according to the increase of corresponding age. The normalized score is computed by score = ground truth reward-random rewardreward-random reward<sup>.</sup> 

ground truth reward-random rewardreward-random reward<sup>.</sup> 

Gym simulator, it can run thousands of environments in parallel, improving the sample efficiency for RL algorithms. Moreover, the implemented RL/MARL/offline RL algorithms achieve superior performance on tasks with simple manipulation skills required. Meanwhile, complex manipulations still remain challenging. In particular, when the agent is trained to master multiple manipulation skills, the results of multi-task/Meta RL are not satisfactory. Interestingly, we found that under the multi-task setting, RL exhibited results associated with the development of human intelligence, that is, the trend of RL performance matches with the development of human ages. So far, in bimanual dexterous robot hand manipulation, the current reinforcement learning can reach the level of 48-months infants. 

However, we think that the limitation of Bi-DexHands is that it does not support the deformable object manipulation tasks. Dexterous hands have unique advantages in manipulating deformable objects, but our tasks currently only cover articulated rigid body object manipulation. We hope to develop in this direction in the future. Another limitation is that our tasks primarily train with policies with a state-based observation space, which is difficult for sim-to-real transfer because such inputs are not available in the real world. Our work will advance the field of robotics, increasing the level of automation in factories or lives to replace human labor. The development of this field will reduce the need to put humans in dangerous situations and improve the quality of human life, but it will also bring about the potential for worker displacement. 

We identify four main future directions toward mastering human-level bimanual dexterous manipulation. **1)** Learning from demonstration: our platform needs some human teaching data to study learning from demonstration. **2)** Soft body and deformable objects simulation: we need a better physics engine to support our research on software and task design, to be more specific daily life scenes. **3)** Current meta/multi-task RL algorithms are unable to perform all tasks in our benchmark successfully, which calls for substantial further development on the algorithmic design end. **4)** We would like address the sim-to-real gap by transferring the simulation result on real dexterous hands. In particular, we hope our benchmark results can serve as a start point to help researchers transfer RL-learned skills to reality and help real-world robots to learn dexterous manipulation. 

## **References** 

- [1] Aude Billard and Danica Kragic. Trends and challenges in robot manipulation. _Science_ , 364(6446):eaat8414, 2019. 

- [2] Leah Nellis and Betty E Gridley. Review of the bayley scales of infant development—second edition. _Journal of School Psychology_ , 32(2):201–209, 1994. 

- [3] Gilbert Gottlieb. _Synthesizing nature-nurture: Prenatal roots of instinctive behavior_ . Psychology press, 2014. 

- [4] Jeffrey J Lockman. A perception–action perspective on tool use development. _Child development_ , 71(1):137–144, 2000. 

- [5] Sarah E Berger and Karen E Adolph. Learning and development in infant locomotion. _Progress in brain research_ , 164:237–255, 2007. 

- [6] David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre, George Van Den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al. Mas- 

9 

tering the game of go with deep neural networks and tree search. _nature_ , 529(7587):484–489, 2016. 

- [7] Oriol Vinyals, Igor Babuschkin, Wojciech M Czarnecki, Michaël Mathieu, Andrew Dudzik, Junyoung Chung, David H Choi, Richard Powell, Timo Ewalds, Petko Georgiev, et al. Grandmaster level in starcraft ii using multi-agent reinforcement learning. _Nature_ , 575(7782):350–354, 2019. 

- [8] Henry Zhu, Abhishek Gupta, Aravind Rajeswaran, Sergey Levine, and Vikash Kumar. Dexterous manipulation with deep reinforcement learning: Efficient, general, and low-cost. In _2019 International Conference on Robotics and Automation (ICRA)_ , pages 3651–3657. IEEE, 2019. 

- [9] OpenAI, Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias Plappert, Glenn Powell, Raphael Ribas, Jonas Schneider, Nikolas Tezak, Jerry Tworek, Peter Welinder, Lilian Weng, Qiming Yuan, Wojciech Zaremba, and Lei Zhang. Solving rubik’s cube with a robot hand. _CoRR_ , abs/1910.07113, 2019. 

- [10] Tao Chen, Jie Xu, and Pulkit Agrawal. A system for general in-hand object re-orientation. In _Conference on Robot Learning_ , pages 297–307. PMLR, 2022. 

- [11] Yiran Geng, Boshi An, Haoran Geng, Yuanpei Chen, Yaodong Yang, and Hao Dong. End-to-end affordance learning for robotic manipulation. _arXiv preprint arXiv:2209.12941_ , 2022. 

- [12] Puhao Li, Tengyu Liu, Yuyang Li, Yiran Geng, Yixin Zhu, Yaodong Yang, and Siyuan Huang. Gendexgrasp: Generalizable dexterous grasping. _arXiv preprint arXiv:2210.00722_ , 2022. 

- [13] Mevlana C Gemici and Ashutosh Saxena. Learning haptic representation for manipulating deformable food objects. In _2014 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 638–645. IEEE, 2014. 

- [14] Ali Ghadirzadeh, Atsuto Maki, Danica Kragic, and Mårten Björkman. Deep predictive policy training using reinforcement learning. In _2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 2351–2358. IEEE, 2017. 

- [15] Jian Shi, J Zachary Woodruff, Paul B Umbanhowar, and Kevin M Lynch. Dynamic in-hand sliding manipulation. _IEEE Transactions on Robotics_ , 33(4):778–795, 2017. 

- [16] Pulkit Agrawal, Ashvin V Nair, Pieter Abbeel, Jitendra Malik, and Sergey Levine. Learning to poke by poking: Experiential learning of intuitive physics. _Advances in neural information processing systems_ , 29, 2016. 

- [17] Rika Antonova, Silvia Cruciani, Christian Smith, and Danica Kragic. Reinforcement learning for pivoting task. _CoRR_ , abs/1703.00472, 2017. 

- [18] J Zachary Woodruff and Kevin M Lynch. Planning and control for dynamic, nonprehensile, and hybrid manipulation tasks. In _2017 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 4066–4073. IEEE, 2017. 

- [19] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel State. Isaac gym: High performance GPU based physics simulation for robot learning. In _NeurIPS Datasets and Benchmarks_ , 2021. 

- [20] Nancy Bayley, Scales Infant, et al. Bayley scales of infant and toddler development–third edition: Technical manual. 2006. 

- [21] Mikayel Samvelyan, Tabish Rashid, Christian Schroeder De Witt, Gregory Farquhar, Nantas Nardelli, Tim GJ Rudner, Chia-Man Hung, Philip HS Torr, Jakob Foerster, and Shimon Whiteson. The starcraft multi-agent challenge. _arXiv preprint arXiv:1902.04043_ , 2019. 

- [22] Berk Calli, Arjun Singh, James Bruce, Aaron Walsman, Kurt Konolige, Siddhartha Srinivasa, Pieter Abbeel, and Aaron M Dollar. Yale-cmu-berkeley dataset for robotic manipulation research. _The International Journal of Robotics Research_ , 36(3):261–268, 2017. 

- [23] Fanbo Xiang, Yuzhe Qin, Kaichun Mo, Yikuan Xia, Hao Zhu, Fangchen Liu, Minghua Liu, Hanxiao Jiang, Yifu Yuan, He Wang, et al. Sapien: A simulated part-based interactive environment. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 11097–11107, 2020. 

- [24] Antonio Bicchi and Vijay Kumar. Robotic grasping and contact: A review. In _Proceedings 2000 ICRA. Millennium conference. IEEE international conference on robotics and automation. Symposia proceedings (Cat. No. 00CH37065)_ , volume 1, pages 348–353. IEEE, 2000. 

10 

- [25] Jeannette Bohg, Antonio Morales, Tamim Asfour, and Danica Kragic. Data-driven grasp synthesis—a survey. _IEEE Transactions on robotics_ , 30(2):289–309, 2013. 

- [26] Walter G Bircher, Aaron M Dollar, and Nicolas Rojas. A two-fingered robot gripper with large object reorientation range. In _2017 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 3453–3460. IEEE, 2017. 

- [27] Nahian Rahman, Luca Carbonari, Mariapaola D’Imperio, Carlo Canali, Darwin G Caldwell, and Ferdinando Cannella. A dexterous gripper for in-hand manipulation. In _2016 IEEE International Conference on Advanced Intelligent Mechatronics (AIM)_ , pages 377–382. IEEE, 2016. 

- [28] Ryuta Ozawa and Kenji Tahara. Grasp and dexterous manipulation of multi-fingered robotic hands: a review from a control view point. _Advanced Robotics_ , 31(19-20):1030–1050, 2017. 

- [29] Nikolaus Vahrenkamp, Markus Przybylski, Tamim Asfour, and Rüdiger Dillmann. Bimanual grasp planning. In _2011 11th IEEE-RAS International Conference on Humanoid Robots_ , pages 493–499. IEEE, 2011. 

- [30] Christian Smith, Yiannis Karayiannidis, Lazaros Nalpantidis, Xavi Gratal, Peng Qi, Dimos V Dimarogonas, and Danica Kragic. Dual arm manipulation—a survey. _Robotics and Autonomous systems_ , 60(10):1340–1353, 2012. 

- [31] Duy Nguyen-Tuong and Jan Peters. Model learning for robot control: a survey. _Cognitive processing_ , 12(4):319–340, 2011. 

- [32] Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Karol Hausman, Chelsea Finn, and Sergey Levine. Meta-world: A benchmark and evaluation for multi-task and meta reinforcement learning. In _Conference on Robot Learning_ , pages 1094–1100. PMLR, 2020. 

- [33] Stephen James, Zicong Ma, David Rovick Arrojo, and Andrew J. Davison. Rlbench: The robot learning benchmark & learning environment. _IEEE Robotics Autom. Lett._ , 5(2):3019–3026, 2020. 

- [34] Yuke Zhu, Josiah Wong, Ajay Mandlekar, and Roberto Martín-Martín. robosuite: A modular simulation framework and benchmark for robot learning. _CoRR_ , abs/2009.12293, 2020. 

- [35] Uikyum Kim, Dawoon Jung, Heeyoen Jeong, Jongwoo Park, Hyun-Mok Jung, Joono Cheong, Hyouk Ryeol Choi, Hyunmin Do, and Chanhun Park. Integrated linkage-driven dexterous anthropomorphic robotic hand. _Nature communications_ , 12(1):1–13, 2021. 

- [36] Allison M Okamura, Niels Smaby, and Mark R Cutkosky. An overview of dexterous manipulation. In _Proceedings 2000 ICRA. Millennium Conference. IEEE International Conference on Robotics and Automation. Symposia Proceedings (Cat. No. 00CH37065)_ , volume 1, pages 255–262. IEEE, 2000. 

- [37] Vikash Kumar, Emanuel Todorov, and Sergey Levine. Optimal control with learned local models: Application to dexterous manipulation. In _2016 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 378–383. IEEE, 2016. 

- [38] Grady Williams, Andrew Aldrich, and Evangelos A. Theodorou. Model predictive path integral control using covariance variable importance sampling. _CoRR_ , abs/1509.01149, 2015. 

- [39] Henry J Charlesworth and Giovanni Montana. Solving challenging dexterous manipulation tasks with trajectory optimisation and reinforcement learning. In _International Conference on Machine Learning_ , pages 1496–1506. PMLR, 2021. 

- [40] Wenlong Huang, Igor Mordatch, Pieter Abbeel, and Deepak Pathak. Generalization in dexterous manipulation via geometry-aware multi-task learning. _CoRR_ , abs/2111.03062, 2021. 

- [41] Tete Xiao, Ilija Radosavovic, Trevor Darrell, and Jitendra Malik. Masked visual pre-training for motor control. _CoRR_ , abs/2203.06173, 2022. 

- [42] Yuzhe Qin, Hao Su, and Xiaolong Wang. From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation. _CoRR_ , abs/2204.12490, 2022. 

- [43] Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. _CoRR_ , abs/2108.05877, 2021. 

- [44] ShadowRobot. Shadowrobot dexterous hand. `https://www.shadowrobot.com/ dexterous-hand-series/` , 2005. 

11 

- [45] Yaodong Yang and Jun Wang. An overview of multi-agent reinforcement learning from game theoretical perspective. _arXiv preprint arXiv:2011.00583_ , 2020. 

- [46] Xiaotie Deng, Yuhao Li, David Henry Mguni, Jun Wang, and Yaodong Yang. On the complexity of computing markov perfect equilibrium in general-sum stochastic games. _arXiv preprint arXiv:2109.01795_ , 2021. 

- [47] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _CoRR_ , abs/1707.06347, 2017. 

- [48] Tuomas Haarnoja, Aurick Zhou, Kristian Hartikainen, George Tucker, Sehoon Ha, Jie Tan, Vikash Kumar, Henry Zhu, Abhishek Gupta, Pieter Abbeel, and Sergey Levine. Soft actor-critic algorithms and applications. _CoRR_ , abs/1812.05905, 2018. 

- [49] John Schulman, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. Trust region policy optimization. In _International conference on machine learning_ , pages 1889–1897. PMLR, 2015. 

- [50] Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra. Continuous control with deep reinforcement learning. In _ICLR (Poster)_ , 2016. 

- [51] Scott Fujimoto, Herke Hoof, and David Meger. Addressing function approximation error in actor-critic methods. In _International conference on machine learning_ , pages 1587–1596. PMLR, 2018. 

- [52] Jakub Grudzien Kuba, Muning Wen, Linghui Meng, Haifeng Zhang, David Mguni, Jun Wang, Yaodong Yang, et al. Settling the variance of multi-agent policy gradients. _Advances in Neural Information Processing Systems_ , 34:13458–13470, 2021. 

- [53] Jakub Grudzien Kuba, Ruiqing Chen, Muning Wen, Ying Wen, Fanglei Sun, Jun Wang, and Yaodong Yang. Trust region policy optimisation in multi-agent reinforcement learning. In _International Conference on Learning Representations_ , 2021. 

- [54] Jakub Grudzien Kuba, Xidong Feng, Shiyao Ding, Hao Dong, Jun Wang, and Yaodong Yang. Heterogeneous-agent mirror learning: A continuum of solutions to cooperative marl. _arXiv preprint arXiv:2208.01682_ , 2022. 

- [55] Chao Yu, Akash Velu, Eugene Vinitsky, Yu Wang, Alexandre Bayen, and Yi Wu. The surprising effectiveness of ppo in cooperative, multi-agent games. _arXiv preprint arXiv:2103.01955_ , 2021. 

- [56] Christian Schröder de Witt, Tarun Gupta, Denys Makoviichuk, Viktor Makoviychuk, Philip H. S. Torr, Mingfei Sun, and Shimon Whiteson. Is independent learning all you need in the starcraft multi-agent challenge? _CoRR_ , abs/2011.09533, 2020. 

- [57] Ryan Lowe, Yi I Wu, Aviv Tamar, Jean Harb, OpenAI Pieter Abbeel, and Igor Mordatch. Multi-agent actor-critic for mixed cooperative-competitive environments. _Advances in neural information processing systems_ , 30, 2017. 

- [58] Scott Fujimoto and Shixiang Shane Gu. A minimalist approach to offline reinforcement learning. _Advances in Neural Information Processing Systems (NeurIPS)_ , 2021. 

- [59] Scott Fujimoto, David Meger, and Doina Precup. Off-policy deep reinforcement learning without exploration. In _International Conference on Machine Learning (ICML)_ , 2019. 

- [60] Ilya Kostrikov, Ashvin Nair, and Sergey Levine. Offline reinforcement learning with implicit q-learning. In _International Conference on Learning Representations (ICLR)_ , 2022. 

- [61] Bo Liu, Xidong Feng, Haifeng Zhang, Jun Wang, and Yaodong Yang. Settling the bias and variance of meta-gradient estimation for meta-reinforcement learning. _arXiv preprint arXiv:2112.15400_ , 2021. 

- [62] Yan Duan, John Schulman, Xi Chen, Peter L Bartlett, Ilya Sutskever, and Pieter Abbeel. Rl<sup>2</sup> : Fast reinforcement learning via slow reinforcement learning. _arXiv preprint arXiv:1611.02779_ , 2016. 

- [63] Jonas Rothfuss, Dennis Lee, Ignasi Clavera, Tamim Asfour, and Pieter Abbeel. Promp: Proximal meta-policy search. In _ICLR (Poster)_ . OpenReview.net, 2019. 

- [64] Marco Del Giudice and Jay Belsky. The development of life history strategies: Toward a multi-stage theory. _The evolution of personality and individual differences_ , pages 154–176, 2011. 

12 

- [65] Lawrence G Weiss, Thomas Oakland, and Glen P Aylward. _Bayley-III clinical use and interpretation_ . Academic Press, 2010. 

- [66] FIRST WORDS Project. 16 actions with objects by 16 months, Feb. 16, 2018 [Online]. 

- [67] Jennifer M Zubler, Lisa D Wiggins, Michelle M Macias, Toni M Whitaker, Judith S Shaw, Jane K Squires, Julie A Pajek, Rebecca B Wolf, Karnesha S Slaughter, Amber S Broughton, et al. Evidence-informed milestones for developmental surveillance tools. _Pediatrics_ , 149(3), 2022. 

- [68] Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, and Sergey Levine. D4RL: datasets for deep data-driven reinforcement learning. _CoRR_ , abs/2004.07219, 2020. 

13 

## **A Task Specifications** 

### **A.1 Physical parameters of Shadow Hand** 

The limits of each joint in Shadow Hand are as Table 5. The thumb has 5 degrees of freedom with 5 joints, the other fingers are all 3 degrees of freedom and 4 joints, and the joints at the ends of each finger are uncontrollable. The distal joints of the fingers are coupled like that of human fingers, making the angle of the middle joint always bigger or equal to the angle of the distal joint. This allows the middle phalange is curved, while the distal phalange is straight. There is an extra joint (LF5) at the end of the little finger to allow the little finger to rotate in the direction of the thumb. There are two joints at the wrist, which guarantees that the entire hand can rotate 360 degrees. 

Table 5: Finger range of motion. 

|Joints<br>Cor|responds to the number of1|Min|Max|
|---|---|---|---|
|Finger Distal(FF1,MF1,RF1,LF1)|15,11,7,3|0°|90°|
|Finger Middle(FF2,MF2,RF2,LF2)|16,12,8,4|0°|90°|
|Finger Base Abduction(FF3,MF3,RF3,LF3)|17,13,9,5|-15°|90°|
|Finger Base Lateral(FF4,MF4,RF4,LF4)|18,14,10,6|-20°|20°|
|Little Finger Rotation(LF5)|19|0°|45°|
|Thumb Distal(TH1)|20|-15°|90°|
|Thumb Middle(TH2)|21|-30°|30°|
|Thumb Base Abduction(TH3)|22|-12°|12°|
|Thumb Base Lateral(TH4)|23|0°|70°|
|Thumb Base Rotation(TH5)|24|-60°|60°|
|Hand Wrist Abduction(WR1)|1|-40°|28°|
|Hand Wrist Lateral (WR2)|2|-28°|8°|



Stiffness, damping, friction, and armature are also important physical parameters in robotics. For each Shadow Hand’s joint, we show our DoF properties in Table 6. This part can be adjusted in the Isaac Gym simulator. 

Table 6: DoF properties of Shadow Hand. 

|Joints|Stifness|Damping|Friction|Armature|
|---|---|---|---|---|
|WR1|100|4.78|0|0|
|WR2|100|2.17|0|0|
|FF2|100|3.4e+38|0|0|
|FF3|100|0.9|0|0|
|FF4|100|0.725|0|0|
|MF2|100|3.4e+38|0|0|
|MF3|100|0.9|0|0|
|MF4|100|0.725|0|0|
|RF2|100|3.4e+38|0|0|
|RF3|100|0.9|0|0|
|RF4|100|0.725|0|0|
|LF2|100|3.4e+38|0|0|
|LF3|100|0.9|0|0|
|LF4|100|0.725|0|0|
|TH2|100|3.4e+38|0|0|
|TH3|100|0.99|0|0|
|TH4|100|0.99|0|0|
|TH5|100|0.81|0|0|



### **A.2 Detailed components of tasks** 

In this section, we detailed the components of tasks in Bi-DexHands. We refer to some designs of existing dexterous hand environments, integrate their advantages, and expand some new environments 

14 

and unique features for single/multi-agent reinforcement learning. Our environments focus on the application of RL algorithms to dexterous hand control, which is challenging in traditional control algorithms. The difficulty of our environment is not only reflected in the challenging task content but also reflected in the high-dimensional continuous space control. The state space dimension of each environment is up to 400 dimensions in total, and the action space dimension is up to 40 dimensions. A multi-agent feature of our environment is that we use five fingers and palms of each hand as a minimum agent unit. It is mean that you can use each finger and palm as an agent, or combine any number of them as an agent by yourself. All environments are goal-based, and each epoch will randomly reset the object’s starting pose and target pose to improve generalization. All objects type can be selected in the config, the basis is egg, block, and pen. We also provide objects type in the YCB dataset as an extension, you can customize the object type they want to use. 

The objects in the YCB dataset are used for our object-catching tasks. Because our object-catching environment is only related to the pose of the object, we can arbitrarily replace objects of suitable size in the YCB dataset. Other tasks use items from the Sapien dataset, and can also use other objects from the same category in Sapien dataset. However, because it is related to the shape of the object, some additional operations are required. We have added examples to Github to show how to use objects from YCB and Sapien datasets, see here. 

An overview of our tasks is shown in Fig.5. Next, we will introduce the basic description, action space, observation space, and reward function of each task. We only use the Shadow Hand and object state values as observation at present, but we also provide an interface for using point cloud as observation in our Github repository for researchers to study in the future. The observation of all tasks is composed of three parts: the state values of the left and right hands, and the information of objects and target. The state values of the left and right hands were the same for each task, including hand joint and finger positions, velocity, and force information. The state values of the object and goal are different for each task, which we will describe in the following. Table.7 gives the specific information of the left-hand and right-hand state values. Note that the observation is slightly different in the HandOver task due to the fixed base. 

Designing a reward function is very important for an RL task. I would like to introduce the method of our reward design in detail. In general, our reward design is goal-based and follows the same set of logic. For object-catching tasks, our reward is simply related to the difference between the pose of the object and the target. The closer the object is to the target, the greater the reward. For other tasks that require the hand to hold the object, our reward generally consists of three parts: the distance from the left hand to the target point on the object that the left-hand needs to operate, the distance from the right hand to the target point on the object that the right-hand needs to operate, and the distance from the object to the target. The principle of our design is to conform to human intuition based on completing the task and to make the reward function structure as unified as possible. This unified reward function structure is also one of the requirements of Meta RL and Multi-task RL environment design. However, because the scenarios of each task are different, the hyperparameters of the reward function will inevitably be different. We have tried our best to avoid manual reward shaping for each task provided that RL can be successfully trained. 

Under the multi-agent setting, the partial observation of each agent depends on the observation of the hand it belongs to. For example, if the left distal finger, left thumb, and right distal finger are one agent respectively, the observation of the left distal finger and left thumb are the observation of the entire left hand in the Table 7 plus the object and target information. The obs of the right distal finger is the observation of the entire right hand in the Table 7 plus object and target information. The action of each agent depends on the multi-agent setting ( _i.e._ , fingers, hands,...), and the output by each agent is the joint degree of itself. Bi-DexHands is a fully-cooperative game where all agents have the same reward. Therefore, the setting of multi-agent can be completely inferred from the setting of single-agent. 

### **A.2.1 Hand Over** 

This environment consists of two Shadow Hands with palms facing up, opposite each other, and an object that needs to be passed. In the beginning, the object will fall randomly in the area of the Shadow Hand on the right side. Then the hand holds the object and passes the object to the other hand. Note that the base of the hand is fixed. More importantly, the hand which holds the object initially can not directly touch the target, nor can it directly roll the object to the other hand, so the 

15 

Table 7: Observation space of dual Shadow Hands. 

|Index|Description|
|---|---|
|0 - 23|right Shadow Hand dofposition|
|24 - 47|right Shadow Hand dof velocity|
|48 - 71|right Shadow Hand dof force|
|72 - 136|right Shadow Hand fingertip pose,linear velocity,angle velocity (5 x 13)|
|137 - 166|right Shadow Hand fingertipforce,torque(5 x 6)|
|167 - 169|right Shadow Hand baseposition|
|170 - 172|right Shadow Hand base rotation|
|173 - 198|right Shadow Hand actions|
|199 - 222|left Shadow Hand dofposition|
|223 - 246|left Shadow Hand dof velocity|
|247 - 270|left Shadow Hand dof force|
|271 - 335|left Shadow Hand fingertip pose,linear velocity,angle velocity (5 x 13)|
|336 - 365|left Shadow Hand fingertipforce,torque(5 x 6)|
|366 - 368|left Shadow Hand baseposition|
|369 - 371|left Shadow Hand base rotation|
|372 - 397|left Shadow Hand actions|





<!-- Start of picture text -->
open pen cap switch grasp&place pour water open scissors<br>re-orientation stack block swing cup two catch underarm open bottle cap<br>lift cup catch abreast catch over2underarm catch underarm door close inward<br>door close outward hand over lift pot door open inward door open outward<br><!-- End of picture text -->

Figure 5: An overview of all tasks. 

object must be thrown up and stays in the air in the process. There are 398-dimensional observations and 40-dimensional actions in the task. Additionally, the reward function is related to the pose error between the object and the target. When the pose error gets smaller, the reward increases dramatically. Specifically, the observation space of each agent is detailed in the following Table 8, and the action space is shown in Table 9. 

**Observations** The 398-dimensional observational space for Hand Over task is shown in Table 8. It should be noted that since the base of the dual hands in this task is fixed, the observation of the dual hands is compared to the Table 7 of reduced 24 dimensions. 

**Actions** The 40-dimensional action space for one hand in Hand Over task is shown in Table 9. 

**Rewards** Denote the object and goal position as _xo_ and _xg_ respectively. Then, the translational position difference between the object and the goal _dt_ is given by _dt_ = _∥xo − xg∥_ 2. Denote the angular position difference between the object and the goal as _da_ , then the rotational difference _dr_ is given by _dr_ = 2 arcsin _clamp_ ( _∥da∥_ 2 _, max_ = 1 _._ 0). Finally, the rewards are given by the following 

16 

Table 8: Observation space of Hand Over. 

|Index|Description|
|---|---|
|0 - 373|dual hands observation shown in Table7|
|374 - 380|objectpose|
|381 - 383|object linear velocity|
|384 - 386|object angle velocity|
|387 - 393|goalpose|
|394 - 397|goal rot - object rot|



Table 9: Action space of Hand Over. 

|Index<br>0 - 19|Description<br>right Shadow Hand actuatedjoint|
|---|---|
|20 - 39|left Shadow Hand actuated joint|



specific formula: 

_r_ = _exp_ [ _−_ 0 _._ 2( _αdt_ + _dr_ )] (1) 

where _α_ is a constant balancing translational and rotational rewards. 

### **A.2.2 Catch Underarm** 

In this problem, two Shadow Hands with palms facing upwards are controlled to pass an object from one palm to the other. What makes it more difficult than the Handover problem is that the hands’ translation and rotation degrees of freedom are no longer frozen but are added into the action space. 

**Observations** The 422-dimensional observational space as shown in Table 10. 

Table 10: Observation space of Catch Underarm. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|objectpose|
|405 - 407|object linear velocity|
|408 - 410|object angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|



**Actions** The 52-dimensional action space as shown in Table 11. 

**Rewards** Denote the object and goal position as _xo_ and _xg_ respectively. Then, the translational position difference between the object and the goal _dt_ is given by _dt_ = _∥xo − xg∥_ 2. Denote the angular position difference between the object and the goal as _da_ , then the rotational difference _dr_ is given by _dr_ = 2 arcsin _clamp_ ( _∥da∥_ 2 _, max_ = 1 _._ 0). Finally, the rewards are given by the following specific formula: 



where _α_ is a constant balancing translational and rotational rewards. 

### **A.2.3 Catch Over2Underarm** 

This environment is like made up of half Hand Over and Catch Underarm, the object needs to be thrown from the vertical hand to the palm-up hand. 

**Observations** The 422-dimensional observational space as shown in Table 12. 

**Actions** The 52-dimensional action space as shown in Table 13. 

17 

Table 11: Action space of Catch Underarm. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



Table 12: Observation space of Catch Over2Underarm. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|objectpose|
|405 - 407|object linear velocity|
|408 - 410|object angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|



**Rewards** Denote the object and goal position as _xo_ and _xg_ respectively. Then, the translational position difference between the object and the goal _dt_ is given by _dt_ = _∥xo − xg∥_ 2. Denote the angular position difference between the object and the goal as _da_ , then the rotational difference _dr_ is given by _dr_ = 2 arcsin _clamp_ ( _∥da∥_ 2 _, max_ = 1 _._ 0). Finally, the rewards are given by the following specific formula: 



where _α_ is a constant balancing translational and rotational rewards. 

### **A.2.4 Two Catch Underarm** 

This environment is similar to Catch Underarm, but with an object in each hand and the corresponding goal on the other hand. Therefore, the environment requires two objects to be thrown into the other hand at the same time, which requires a higher manipulation technique than the environment of a single object. 

**Observations** The 446-dimensional observational space as shown in Table 14. 

**Actions** The 52-dimensional action space as shown in Table 15. 

**Rewards** For the reward part, we use subscripts 1,2 to distinguish the 2 objects. 

Denote the object and goal position as _xo_ 1, _xo_ 2 and _xg_ 1, _xg_ 2 respectively. Then, the translational position difference between the object and the goal _dt_ 1, _dt_ 2 is given by _dti_ = _∥xoi − xgi∥_ 2, where _i_ = 1 _,_ 2. Denote the angular position difference between the object and the goal as _da_ 1, _da_ 2, then the rotational difference _dr_ 1 , _dr_ 2 is given by _dri_ = 2 arcsin _clamp_ ( _∥dai∥_ 2 _, max_ = 1 _._ 0). Finally, the 

Table 13: Action space of Catch Over2Underarm. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



18 

Table 14: Observation space of Two Catch Underarm. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|object1pose|
|405 - 407|object1 linear velocity|
|408 - 410|object1 angle velocity|
|411 - 417|goal1pose|
|418 - 421<br>422 - 428|goal1 rot - object rot<br>object2pose|
|429 - 431|object2 linear velocity|
|432 - 434|object2 angle velocity|
|435 - 441|goal2pose|
|442 - 445|goal2 rot - object2 rot|



Table 15: Action space of Two Catch Underarm. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



rewards are given by the following specific formula: 

_r_ = _exp_ [ _−_ 0 _._ 2( _αdt_ 1 + _dr_ 1)] + _exp_ [ _−_ 0 _._ 2( _αdt_ 2 + _dr_ 2)] (4) 

where _α_ is a constant balancing translational and rotational rewards. 

### **A.2.5 Catch Abreast** 

This environment consists of two Shadow Hands placed side by side in the same direction and an object that needs to be passed. Compared with the previous environment which is more like passing objects between the hands of two people, this environment is designed to simulate the two hands of the same person passing objects, so different catch techniques are also required and require more hand translation and rotation techniques. 

**Observations** The 422-dimensional observation space as shown in Table 16. 

Table 16: Observation space of Catch Abreast. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|objectpose|
|405 - 407|object linear velocity|
|408 - 410|object angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|



**Actions** The 52-dimensional action space as shown in Table 17. 

**Rewards** Denote the object and goal position as _xo_ and _xg_ respectively. Then, the translational position difference between the object and the goal _dt_ is given by _dt_ = _∥xo − xg∥_ 2. Denote the angular position difference between the object and the goal as _da_ , then the rotational difference _dr_ is 

19 

Table 17: Action space of Catch Abreast. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



given by _dr_ = 2 arcsin _clamp_ ( _∥da∥_ 2 _, max_ = 1 _._ 0). Finally, the rewards are given by the following specific formula: 



where _α_ is a constant balancing translational and rotational rewards. 

### **A.2.6 Lift Underarm** 

This environment requires grasping the pot handle with two hands and lifting the pot to the designated position. This environment is designed to simulate the scene of lift in daily life and is a practical skill. 

**Observations** The 428-dimensional observation space as shown in Table 18. 

Table 18: Observation space of Lift Underarm. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|objectpose|
|405 - 407|object linear velocity|
|408 - 410|object angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|
|422 - 424|object right handleposition|
|425 - 427|object left handle position|



**Actions** The 40-dimensional action space as shown in Table 19. 

Table 19: Action space of Lift Underarm. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to the left handle, the distance from the right hand to the right handle, and the distance from the object to the target point. The position difference between the object to the target point _dtarget_ is given by _dtarget_ = _∥xobj − xgoal∥_ 2. The position difference between the left hand to the left handle _dleft_ is given by _dleft_ = _∥xlhand − xlhandle∥_ 2.The position difference between the right hand to the right handle _dright_ is given by _dright_ = _∥xrhand − xrhandle∥_ 2. The reward is given by this specific formula: 

_r_ = 0 _._ 2 _− dleft − dright_ + 3 _∗_ (0 _._ 985 _− dtarget_ ) (6) 

20 

### **A.2.7 Door Open Outward/Door Close Inward** 

These two environments require a closed/opened door to be opened/closed and the door can only be pushed outward or initially open inward. Both these two environments only need to do the push behavior, so it is relatively simple. 

**Observations** The 428-dimensional observation space as shown in Table 20. 

Table 20: observation space of Door Open Outward/Door Close Inward. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|objectpose|
|405 - 407|object linear velocity|
|408 - 410|object angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|
|422 - 424|door right handleposition|
|425 - 427|door left handle position|



**Actions** The 52-dimensional action space as shown in Table 21. 

Table 21: Action space of Door Open Outward/Door Close Inward. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to the left handle, the distance from the right hand to the right handle, and the distance between the two handles. The distance between the two handles _dtarget_ is given by _dtarget_ = _∥xlhandle − xrhandle∥_ 2. The position difference between the left hand to the left handle _dleft_ is given by _dleft_ = _∥xlhand − xlhandle∥_ 2.The position difference between the right hand to the right handle _dright_ is given by _dright_ = _∥xrhand − xrhandle∥_ 2. For DoorOpenOutward, the reward is given by this specific formula: 



For DoorCloseInward, the reward is given by this specific formula: 



### **A.2.8 Door Open Inward/Door Close Outward** 

These two environments also require a closed/opened door to be opened/closed and the door can only be pushed inward or initially open outward, but because they can’t complete the task by simply pushing, which need to catch the handle by hand and then open or close it, so it is relatively difficult. 

**Observations** The 428-dimensional observation space as shown in Table 22. 

**Actions** The 52-dimensional action space as shown in Table 23. 

**Rewards** The reward consists of three parts: the distance from the left hand to the left handle, the distance from the right hand to the right handle, and the distance between the two handles. The distance between the two handles _dtarget_ is given by _dtarget_ = _∥xlhandle − xrhandle∥_ 2. The position 

21 

Table 22: Observation space of Door Open Inward/Door Close Outward. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|objectpose|
|405 - 407|object linear velocity|
|408 - 410|object angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|
|422 - 424|door right handleposition|
|425 - 427|door left handle position|



Table 23: Action space of Door Open Inward/Door Close Outward. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



difference between the left hand to the left handle _dleft_ is given by _dleft_ = _∥xlhand − xlhandle∥_ 2.The position difference between the right hand to the right handle _dright_ is given by _dright_ = _∥xrhand − xrhandle∥_ 2. For DoorOpenInward, the reward is given by this specific formula: 



For DoorCloseOutward, the reward is given by this specific formula: 



### **A.2.9 Bottle Cap** 

This environment involves two hands and a bottle, we need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires the cooperation of two hands to ensure that the cap does not fall. 

**Observations** The 414-dimensional observation space as shown in Table 24. 

Table 24: Observation space of Bottle Cap. 

|0 - 397|dual hands observation shown in Table7|
|---|---|
|398 - 404|bottlepose|
|405 - 407|bottle linear velocity|
|408 - 410|bottle angle velocity|
|411 - 413|bottle cap position|



**Actions** The 52-dimensional action space as shown in Table 25. 

**Rewards** The reward also consists of three parts: the distance from the left hand to the bottle cap, the distance from the right hand to the bottle, and the distance between the bottle and bottle cap. The distance between the bottle and bottle cap _dtarget_ is given by _dtarget_ = _∥xbottle − xbottlecap∥_ 2. the distance from the left hand to the bottle cap _dleft_ is given by _dleft_ = _∥xlhand − xbottlecap∥_ 2. the distance from the right hand to the bottle _dright_ is given by _dright_ = _∥xrhand − xbottle∥_ 2. The reward is given by this specific formula: 



22 

Table 25: Action space of Bottle Cap. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



### **A.2.10 Push Block** 

This environment involves two hands and two blocks, we need to use both hands to reach and push the block to the desired goal separately. This is a relatively simple task. 

**Observations** The 417-dimensional observation space as shown in Table 26. 

Table 26: Observation space of Push Block. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|block1pose|
|405 - 407|block1 linear velocity|
|408 - 410|block1 angle velocity|
|411 - 413|block1position|
|414 - 416|block2 position|



**Actions** The 52-dimensional action space as shown in Table 27. 

Table 27: Action space of Push Block. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to block1, the distance from the right hand to block2, and the distance between the block and desired goal. The distance between the block and desired goal _dtarget_ is given by _dtarget_ = _∥xblock_ 1 _−xblock_ 1 _goal∥_ 2+ _∥xblock_ 2 _− xblock_ 2 _goal∥_ 2. the distance from the left hand to the block1 _dleft_ is given by _dleft_ = _∥xlhand − xblock_ 1 _∥_ 2. the distance from the right hand to the block2 _dright_ is given by _dright_ = _∥xrhand − xblock_ 2 _∥_ 2. The reward is given by this specific formula: 



### **A.2.11 Swing Cup** 

This environment involves two hands and a dual handle cup, we need to use two hands to hold and swing the cup together. 

**Observations** The 428-dimensional observation space as shown in Table 28. 

**Actions** The 52-dimensional action space as shown in Table 29. 

23 

Table 28: Observation space of Swing Cup. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|cup pose|
|405 - 407|cuplinear velocity|
|408 - 410|cupangle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|
|422 - 424|cupright handleposition|
|425 - 427|cup left handle position|



Table 29: Action space of Swing Cup. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to the cup’s left handle, the distance from the right hand to the cup’s right handle, and the rotating distance between the cup and desired goal. The rotate distance between the cup and desired goal _dtarget_ is given by _dtarget_ = 2 _∗_ arcsin _qcup ∗ qtarget_ . the distance from the left hand to the cup left handle _dleft_ is given by _dleft_ = _∥xlhand − xlhandle∥_ 2. the distance from the right hand to the cup right handle _dright_ is given by _dright_ = _∥xrhand − xrhandle∥_ 2. The reward is given by this specific formula: 



### **A.2.12 Open Scissors** 

This environment involves two hands and scissors, we need to use two hands to open the scissors. 

**Observations** The 428-dimensional observation space as shown in Table 30. 

Table 30: Observation space of Open Scissors. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|scissorspose|
|405 - 407|scissors linear velocity|
|408 - 410|scissors angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|
|422 - 424|scissors right handleposition|
|425 - 427|scissors left handle position|



**Actions** The 52-dimensional action space as shown in Table 31. 

**Rewards** The reward consists of three parts: the distance from the left hand to the scissors’ left handle, the distance from the right hand to the scissors’ right handle, and the target angle at which the scissors need to be opened. The distance between the scissors dof angle and target dof angle _dtarget_ is given by _dtarget_ = _∥xscissorsdof − xtargetdof ∥_ . the distance from the left hand to the scissors left handle _dleft_ is given by _dleft_ = _∥xlhand − xlhandle∥_ 2. the distance from the right hand to the 

24 

Table 31: Action space of Open Scissors. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



scissors left handle _dright_ is given by _dright_ = _∥xrhand − xrhandle∥_ 2. The reward is given by this specific formula: 



### **A.2.13 Re Orientation** 

This environment involves two hands and two objects. Each hand holds an object and we need to reorient the object to the target orientation. 

**Observations** The 446-dimensional observation space as shown in Table 32. 

Table 32: Observation space of Re Orientation. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|object1pose|
|405 - 407|object1 linear velocity|
|408 - 410|object1 angle velocity|
|411 - 417|goal1pose|
|418 - 421<br>422 - 428|goal1 rot - object rot<br>object2pose|
|429 - 431|object2 linear velocity|
|432 - 434|object2 angle velocity|
|435 - 441|goal2pose|
|442 - 445|goal2 rot - object2 rot|



**Actions** The 52-dimensional action space as shown in Table 33. 

Table 33: Action space of Re Orientation. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left object to the left object goal, the distance from the right object to the right object goal, and the distance between the object and desired goal. The distance between the object and desired goal _dtarget_ is given by _dtarget_ = 2 _∗_ arcsin _qobject_ 1 _∗ qtarget_ + 2 _∗_ arcsin _qobject_ 2 _∗ qtarget_ . the distance from the left hand to the scissors left handle _dleft_ is given by _dleft_ = _∥xlhand − xlhandle∥_ 2. the distance from the right hand to the scissors left handle _dright_ is given by _dright_ = _∥xrhand − xrhandle∥_ 2. The reward is given by this specific formula: 



25 

### **A.2.14 Open Pen Cap** 

This environment involves two hands and a pen, we need to use two hand to open the pen cap. 

**Observations** The 428-dimensional observation space as shown in Table 34. 

Table 34: Observation space of Open Pen Cap. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|penpose|
|405 - 407|pen linear velocity|
|408 - 410|pen angle velocity|
|411 - 417|goalpose|
|418 - 421<br>422 - 424|goal rot - object rot<br>pen body position|
|425 - 427|pen cap position|



**Actions** The 52-dimensional action space as shown in Table 35. 

Table 35: Action space of Open Pen Cap. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to the pen body, the distance from the right hand to the pen cap, and the distance between the pen body and pen cap. The distance between the pen body and pen cap _dtarget_ is given by _dtarget_ = _∥xpenbody − xpencap∥_ . the distance from the left hand to the scissors left handle _dleft_ is given by _dleft_ = _∥xlhand − xpenbody∥_ 2. the distance from the right hand to the scissors left handle _dright_ is given by _dright_ = _∥xrhand − xpencap∥_ 2. The reward is given by this specific formula: 



### **A.2.15 Switch** 

This environment involves dual hands and a bottle, we need to use dual hand fingers to press the desired button. 

**Observations** The 428-dimensional observation space as shown in Table 36. 

Table 36: Observation space of Switch. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|switch1pose|
|405 - 407|switch1 linear velocity|
|408 - 410|switch1 angle velocity|
|411 - 417|goalpose|
|418 - 421<br>422 - 424|goal rot - object rot<br>switch1position|
|425 - 427|switch2 position|



26 

**Actions** The 52-dimensional action space as shown in Table 37. 

Table 37: Action space of Switch. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to the left switch, the distance from the right hand to the right switch, and the distance between the button and button’s desired goal. The distance between the button and the button’s desired goal _dtarget_ is given by _dtarget_ = _∥xbutton_ 1 _− xtarget_ 1 _∥_ 2 + _∥xbutton_ 2 _− xtarget_ 2 _∥_ 2. the distance from the left hand to the scissors left handle _dleft_ is given by _dleft_ = _∥xlhand − xswitch_ 1 _∥_ 2. the distance from the right hand to the scissors left handle _dright_ is given by _dright_ = _∥xrhand − xswitch_ 2 _∥_ 2. The reward is given by this specific formula: 



### **A.2.16 Stack Block** 

This environment involves dual hands and two blocks, and we need to stack the block as a tower. 

**Observations** The 428-dimensional observation space as shown in Table 38. 

Table 38: Observation space of Stack Block. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|block1pose|
|405 - 407|block1 linear velocity|
|408 - 410|block1 angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|
|422 - 424|block1position|
|425 - 427|block2 position|



**Actions** The 52-dimensional action space as shown in Table 39. 

Table 39: Action space of Stack Block. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to block1, the distance from the right hand to block2, and the distance between the block and desired goal. The distance between the block and desired goal _dtarget_ is given by _dtarget_ = _∥xblock_ 1 _− xtarget_ 1 _∥_ 2 + _∥xblock_ 2 _− xtarget_ 2 _∥_ 2. the distance from the left hand to the block1 _dleft_ is given by _dleft_ = _∥xlhand −xblock_ 1 _∥_ 2. 

27 

the distance from the right hand to the block2 _dright_ is given by _dright_ = _∥xrhand − xblock_ 2 _∥_ 2. The reward is given by this specific formula: 



### **A.2.17 Pour Water** 

This environment involves two hands and a bottle, we need to Hold the kettle with one hand and the bucket with the other hand, and pour the water from the kettle into the bucket. In the practice task in Isaac Gym, we use many small balls to simulate the water. 

**Observations** The 428-dimensional observation space as shown in Table 40. 

Table 40: Observation space of Pour Water. 

|Index|Description|
|---|---|
|0 - 397|dual hands observation shown in Table7|
|398 - 404|kettlepose|
|405 - 407|kettle linear velocity|
|408 - 410|kettle angle velocity|
|411 - 417|goalpose|
|418 - 421|goal rot - object rot|
|422 - 424|kettle handleposition|
|425 - 427|bucket position|



**Actions** The 52-dimensional action space as shown in Table 41. 

Table 41: Action space of Pour Water. 

|Index|Description|
|---|---|
|0 - 19|right Shadow Hand actuatedjoint|
|20 - 22|right Shadow Hand base translation|
|23 - 25|right Shadow Hand base rotation|
|26 - 45|left Shadow Hand actuatedjoint|
|46 - 48|left Shadow Hand base translation|
|49 - 51|left Shadow Hand base rotation|



**Rewards** The reward consists of three parts: the distance from the left hand to the bucket, the distance from the right hand to the kettle, and the distance between the kettle spout and desired goal. The distance between the kettle spout and desired goal _dtarget_ is given by _dtarget_ = _∥xspout−xgoal∥_ 2. the distance from the left hand to the bucket _dleft_ is given by _dleft_ = _∥xlhand − xbucket∥_ 2. the distance from the right hand to the kettle _dright_ is given by _dright_ = _∥xrhand − xkettle∥_ 2. The reward is given by this specific formula: 



### **A.3 Offline Data Collection** 

We follow the data collection of D4RL[68] mujoco tasks. The medium dataset is generated by first training a policy online using PPO, early-stopping the training, and collecting 10<sup>6</sup> samples ( _st, at, st_ +1 _, rt_ ) using this medium policy. The random dataset is collected by a randomly initialized policy and contains 10<sup>6</sup> samples. The replay dataset consists of 10<sup>6</sup> experienced samples during training of the medium policy. The medium-expert dataset contains 2 _×_ 10<sup>6</sup> samples by mixing equal amounts of samples collected by expert policy and medium policy. To facilitate comparison across tasks, following the setting of D4RL[68], we normalize scores for each task to the range between 0 and 100 , by computing normalized score = 100 _∗_ expert return-random returnreturn-random return<sup>.A normalized score of 0</sup> corresponds to the average return of an agent taking actions uniformly at random across the action space. A score of 100 corresponds to the average return of an expert policy. 

28 

## **B Training details** 

Isaac Gym is different from other simulators in that it can simulate completely on the GPU, so there is no need to exchange data between the GPU and the CPU during the training process. Therefore we reproduced the existing RL algorithm in our Github repository to accommodate this feature. We implemented many different algorithms in the comprehensive RL domain, but only evaluated some of them. We will give a brief introduction to these algorithms below and give the hyperparameters of the algorithms we used in our evaluation. 

### **B.1 Single-agent algorithms** 

### **B.1.1 Trust Region Policy Optimization** 

TRPO is a basic policy optimization algorithm, with theoretically justified monotonic improvement. Based on the theorem1 in the original paper by John Schulman et. al. _η_ ( _πnew_ ) _≥ Lold_ ( _πnew_ ) _−_ (14 _−ϵγγ_ )<sup>2</sup><sup>_α_2,where</sup><sup>_ϵ_=max</sup> _s,a_<sup>_|Aπ_(</sup><sup>_s, a_)</sup><sup>_|_,</sup><sup>_η_istheobjectivefunctionand</sup><sup>_Lold_isasurrogateobjective:</sup> _Lπ_ (ˆ _π_ ) = _η_ ( _π_ ) + _Es∼ρπ,a∼π_ ( _Aπ_ ( _s, a_ )), providing feasible approximation of _η_ according to the theorem. To empirically allow for larger update steps, the optimization problem is adjusted to _πθnew_ = max _Lθold_ ( _θ_ ) subject to _DKL_<sup>_max_(</sup><sup>_θold, θ_)</sup><sup>_≤δ_.To yield a practical algorithm, TRPO makes a</sup> _θ_ bit of approximation like optimizing with conjugate gradient method followed by a line search. 

### **B.1.2 Proximal Policy Optimization** 

PPO is a policy optimization algorithm enjoying simpler implementation, more general application and better sample complexity over TRPO. Based on the surrogate objective in TRPO: _L_<sup>_CP I_</sup> ( _θ_ ) = _E_ ˆ _t_ [ _rt_ ( _θ_ ) ˆ _At_ ], PPO proposed a new approximate surrogate function _L_<sup>_CLIP_</sup> ( _θ_ ) = _E_ ˆ _t_ [ _min_ ( _rt_ ( _θ_ ) ˆ _At, clip_ ( _rt_ ( _θ_ ) _,_ 1 _− ϵ,_ 1 + _ϵ_ ) ˆ _At_ )], which restricts policy optimization step by removing the incentive for _rt_ to move outside of the interval [1 _− ϵ,_ 1 + _ϵ_ ]. Another alternative surrogate objective is given by incorporating a penalty on KL divergence, and adapting the penalty coefficient. During traning, PPO uses a combined objective, consisting of surrogate objective for the policy, value function loss for the critic and a bonus entropy term: _L_<sup>_CLIP_+</sup><sup>_V F_+</sup><sup>_S_</sup> ( _θ_ ) = _E_ ˆ _t_ [ _L_<sup>_CLIP_</sup> _t_ ( _θ_ ) _− c_ 1 _L_<sup>_V F_</sup> _t_ ( _θ_ ) + _c_ 2 _S_ [ _πθ_ ]( _st_ )]. 

Table 42: Hyperparameters of PPO. 

|Hyperparameters|Other Tasks|Lift Underarm|Stack Block|
|---|---|---|---|
|Num mini-batches|4|4|8|
|Num opt-epochs|5|10|2|
|Num episode-length|8|20|8|
|Hidden size|[1024, 1024, 512]|[1024, 1024, 512]|[1024, 1024, 512]|
|Clip range|0.2|0.2|0.2|
|Max grad norm|1|1|1|
|Learning rate|3.e-4|3.e-4|3.e-4|
|Discount (_γ_)|0.96|0.96|0.9|
|GAE lambda (_λ_)|0.95|0.95|0.95|
|Init noise std|0.8|0.8|0.8|
|Desired kl|0.016|0.016|0.016|
|Ent-coef|0|0|0|



### **B.1.3 Deep Deterministic Policy Gradient** 

DDPG, based on the DPG algorithm, is a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. It uses a copy of the actor and critic networks _Q_<sup>_′_</sup> ( _s, a|θ_<sup>_Q′_</sup> ) and _µ_<sup>_′_</sup> ( _s|θ_<sup>_µ′_</sup> ) to calculate the target values, and use "soft" target updates to update the target networks more stably by having them slowly track the learned networks: _θ_<sup>_′_</sup> _← τθ_ + (1 _− τ_ ) _θ_<sup>_′_</sup> with _τ ≪_ 1. It follows an exploration policy _µ_<sup>_′_</sup> by adding noise sampled from a noise process **N** : _µ_<sup>_′_</sup> ( _St_ ) = _µ_ ( _st|θt_<sup>_µ_) +</sup><sup>**N**</sup><sup>_t_.The critic is updated by minimizing the</sup> 

29 

loss: _L_ ( _φ_ ) = _N_<sup><u>1</u></sup> � _i_<sup>(</sup><sup>_yi−Q_(</sup><sup>_si, ai|θQ_))2 where</sup><sup>_yi_=</sup><sup>_ri_+</sup><sup>_γQ′_(</sup><sup>_si_+1</sup><sup>_, µ′_(</sup><sup>_si_+1</sup><sup>_|θµ′_)</sup><sup>_|θQ′_), and the actor</sup> is updated using sampled policy gradient: _∇θJ ≈ N_<sup><u>1</u></sup> � _i_<sup>_∇αQ_(</sup><sup>_s, a|θQ_)</sup><sup>_|s_=</sup><sup>_s_</sup> _i_<sup>_,a_=</sup><sup>_µ_(</sup><sup>_s_</sup> _i_<sup>)</sup><sup>_∇θµµ_(</sup><sup>_s|θµ_)</sup><sup>_|s_</sup> _i_<sup>.</sup> 

### **B.1.4 Twin Delayed Deep Deterministic policy gradient** 

TD3 is an actor-critic algorithm which applies its modifications to the state of the art actor-critic method for continuous control, DDPG. It focused on two outcomes that occur as the result of estimation error, overestimation bias and a high variance build-up. It uses Clipped Double Q-learning method to reduce overestimation bias: _y ← r_ + _γmini_ =1 _,_ 2 _Qθi_<sup>_′_(</sup><sup>_s′,_˜</sup><sup>_a_), where ˜</sup><sup>_a ←πφ′_(</sup><sup>_s_) +</sup><sup>_ϵ, ϵ ∼_</sup> _clip_ ( **N** (0 _,_ ˜ _σ_ ) _, −c, c_ ), which uses target policy smoothing regularization to avoid overfitting and enforce the value similarity between similar actions, It uses delayed policy and target network updates to ensure small value error. 

### **B.1.5 Soft Actor-Critic** 

SAC is an off-policy maximum entropy actor-critic algorithm. It considers a more general maximum entropy objective: _J_ ( _π_ ) =<sup>�</sup><sup>_T_</sup> _t_ =0<sup>**E**(</sup><sup>_s_</sup> _t_<sup>_,a_</sup> _t_<sup>)</sup><sup>_∼_</sup><sup>**D**</sup> _π_<sup>[</sup><sup>_r_(</sup><sup>_st, at_) +</sup><sup>_α_</sup><sup>**H**(</sup><sup>_π_(</sup><sup>_·|st_))],inwhichthetem-</sup> perature parameter _α_ determines the relative importance of the entropy term. The soft value function _Vψ_ ( _st_ ) is trained to minimize the squared residual error: _Lv_ ( _ψ_ ) = **E** _st∼ρ_ [ 2<sup><u>1</u>(</sup><sup>_Vψ_(</sup><sup>_st_)</sup><sup>_−_</sup> **E** _at∼πφ_ [ _Qθ_ ( _st, at_ ) _−_ log _πφ_ ( _at|st_ )])<sup>2</sup> ]. The soft Q-function parameters can be trained to minimize the soft Bellman residual: _LQ_ ( _θ_ ) = **E** ( _st,at_ ) _∼_ **D** [ 2<sup><u>1</u>(</sup><sup>_Qθ_(</sup><sup>_st, at_)</sup><sup>_−Q_ˆ(</sup><sup>_st, at_))2],inwhich</sup> _Q_ ˆ( _st, at_ ) = _r_ ( _st, at_ ) + _γ_ **E** _st_ +1 _∼p_ [ _V_ ¯ _φ_ ( _st_ +1)] and _V_ ¯ _φ_ is the target value network. The policy parameters can be learned by directly minimizing the expected KL-divergence: _KLπ_ ( _φ_ ) = **E** _st∼ρ_ [ _DKL_ ( _πφ_ ( _·|st_ ) _||_<sup>_exp_</sup> _Z_<sup><u>(</u></sup><sup>_<u>Q</u>_</sup> _θ_ (<sup>_<u>θ</u>_</sup> _s_<sup><u>(</u></sup> _t_<sup>_s_</sup> )<sup>_t,·_</sup><sup><u>))</u></sup> )], in which _Zθ_ ( _st_ ) normalizes the distribution. 

Table 43: Hyperparameters of SAC. 

|Hyperparameters|Other Tasks|Lift Underarm|Stack Block|
|---|---|---|---|
|Num opt-epochs|1|1|1|
|Num mini-batches|4|4|4|
|Hidden size|[1024, 1024, 1024]|[1024, 1024, 1024]|[1024, 1024, 1024]|
|Learning rate|3.e-4|3.e-4|3.e-4|
|ReplayBuffer size|5000|5000|5000|
|Discount (_γ_)|0.96|0.96|0.96|
|Polyak (1_−τ_)|0.99|0.99|0.99|
|Entropy coef|0.2|0.2|0.2|
|Reward scale|1|1|1|
|Max grad norm|1|1|1|
|Batch size|32|32|32|



### **B.2 Multi-agent algorithms** 

### **B.2.1 Independent Proximal Policy Optimization** 

IPPO (Independent PPO) is a multi-agent variant of proximal policy optimization(PPO). It uses PPO to learn decentralized policies _π_<sup>_i_</sup> for agents with indicidual policy clippng based on the objective: **L**<sup>_i_</sup> ( _θ_ ) = **E** _sit_<sup>_,ai_</sup> _t_<sup>[</sup><sup>_min_(</sup> _πθoldπθ_ <u>(</u> _a_ (<sup>_i_</sup> _<u>ta</u>_<sup>_<u>|</u>_</sup> _t_<sup>_is|i_</sup> _<u>t</u>_<sup>_s_</sup><sup><u>)</u></sup><sup>_i_</sup> _t_<sup>)</sup><sup>_A_</sup> _t_<sup>_i, clip_(</sup> _πθoldπθ_ <u>(</u> _a_ (<sup>_i_</sup> _<u>ta</u>_<sup>_<u>|</u>_</sup> _t_<sup>_is|i_</sup> _<u>t</u>_<sup>_s_</sup><sup><u>)</u></sup><sup>_i_</sup> _t_<sup>)</sup><sup>_,_1</sup><sup>_−ϵ,_1 +</sup><sup>_ϵ_)</sup><sup>_A_</sup> _t_<sup>_i_)], and the advantage</sup> function is based on independent learning, where each agent a learns a local observation based critic _Vφ_ ( _zt_<sup>_i_)parameterisedby</sup><sup>_φ_usingGAE.Additionally,itusesvalueclippingtorestricttheupdate</sup> of critic function for each agent _i_ : **L**<sup>_i_</sup> ( _φ_ ) = **E** _zti_<sup>[</sup><sup>_min{_(</sup><sup>_Vφ_(</sup><sup>_z_</sup> _t_<sup>_i_)</sup><sup>_−_</sup> _V_<sup>ˆ</sup> _t_<sup>_i_)2</sup><sup>_,_(</sup><sup>_Vφ_</sup> _old_<sup>(</sup><sup>_z_</sup> _t_<sup>_i_) +</sup><sup>_clip_(</sup><sup>_Vφ_(</sup><sup>_z_</sup> _t_<sup>_i_)</sup><sup>_−_</sup> _Vφold_ ( _zt_<sup>_i_)</sup><sup>_, −ϵ,_+</sup><sup>_ϵ_)</sup><sup>_−_</sup> _V_<sup>ˆ</sup> _t_<sup>_i_)2</sup><sup>_}_].The overall learning loss additionally adds an entropy regularization</sup> term of policy _π_<sup>_i_</sup> . 

30 

### **B.2.2 Heterogenous-Agent Trust Region Policy Optimization** 

HATRPO is a multi-agent algorithm developed from TRPO. With the advantage decomposition lemma, the algorithm is proposed to implement a multi-agent policy iteration procedure with monotonic improvement guarantee. It requires no homogeneity of agents, nor any restrictive assumptions on the decomposibility of joint Q-functions. At each iteration k+1, given a random permutation of agents _i_ 1: _n_ , agent _im_ sequentially optimizes its own policy parameter _θk_<sup>_im_</sup> +1<sup>by maximizing the ob-</sup> jective: _θk_<sup>_im_</sup> +1<sup>=</sup><sup>_argmaxθim_</sup><sup>**E**</sup> _s∼ρθk ,a_<sup>_i_</sup> 1: _m−_ 1 _∼πθi_ 1: _ki_ 1:+1 _mm−−_ 11 _,a_<sup>_im_</sup> _∼πθ_<sup>_imim_</sup> [ _A_<sup>_i_</sup> _π_<sup>_m_</sup> _θk_<sup>(</sup><sup>_s, ai_1:</sup><sup>_m−_1</sup><sup>_, aim_)],subject to</sup> 

**E** _s∼ρθk_ [ _DKL_ ( _πθ_<sup>_im_</sup> _k_<sup>_im_(</sup><sup>_·|s_)</sup><sup>_, π_</sup> _θ_<sup>_imim_(</sup><sup>_·|s_))]</sup><sup>_≤δ_.Apply a linear approximation to the objective function and</sup> a quadratic approximation to the KL constraint: _θk_<sup>_im_</sup> +1<sup>=</sup><sup>_θ_</sup> _k_<sup>_im_</sup> + _α_<sup>_j_�</sup> _gk_<sup>_im_</sup> ( _Hk_<sup>_im_</sup> <u>2</u> _<u>δ</u>_ )<sup>_−_1</sup> _gk_<sup>_im_(</sup><sup>_H_</sup> _k_<sup>_im_)</sup><sup>_−_1</sup><sup>_g_</sup> _k_<sup>_im_,</sup> in which _Hk_<sup>_im_</sup> is the Hessian of the expected KL-divergence, _gk_<sup>_im_</sup> is the gradient of the objective function, and _α_<sup>_j_</sup> _<_ 1 is a positive coefficient. Estimate the advantage function **E** [ _A_<sup>_i_</sup> _π_<sup>_m_</sup> _θk_<sup>(</sup><sup>_s, ai_1:</sup><sup>_m−_1</sup><sup>_, ai_</sup> _m_<sup>)]</sup> _<u>θ</u>_ <u>(</u> _aim_ _<u>|s</u>_ <u>)</u> with (<sup>_π_</sup> _πθk_<sup>_imim_(</sup><sup>_ai_</sup> _m_<sup>_|s_)</sup><sup>_−_1)</sup><sup>_M i_1:</sup><sup>_m_(</sup><sup>_s, a_), where</sup><sup>_M i_1:</sup><sup>_m_=</sup><sup>_<u>π</u>_</sup> _π_<sup>¯</sup> _i_<sup>_i_</sup> 1:<sup>1:</sup> _m_<sup>_m_</sup> _−_<sup>_−_</sup> 1<sup>1</sup> _A_ ˆ( _s, a_ ) and _π_ ¯<sup>_i_</sup> 1: _m−_ 1 =<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_−_1</sup><sup>_π_¯</sup><sup>_ij_is the</sup> policies of agents _i_ 1: _m−_ 1 just updated in the same iteration k+1. 

### **B.2.3 Heterogeneous-Agent Proximal Policy Optimisation** 

HAPPO is a multi-agent policy optimization algorithm that follows the centralized training decentralized execution (CTDE) paradigm. HAPPO doesn’t assume homogeneous agents and doesn’t require decomposibility of the joint value function. The theoretical core of extending PPO to multiagent settings is the advantage decomposition lemma(Lemma 1 in the original paper). As a result of it, similar to single agent PPO, we have a theoretical monotonic improvement guarantee for the multi-agent setting: _J_ <u>(</u> _<u>π</u>_ ) _≥ J_ ( _π_ ) + _σm_<sup>_n_</sup> =1<sup>[</sup><sup>_L_</sup> _π_<sup>_i_1:</sup><sup>_m_</sup> <u>(</u> _<u>π</u>_<sup>_i_1:</sup><sup>_m−_1</sup> _,_ _<u>π</u>_<sup>_~~i~~m_</sup> ) _− CDKL_<sup>_max_(</sup><sup>_πim,_</sup> _<u>π</u>_<sup>_~~i~~m_</sup> )](Lemma 2 in the original paper). This lemma yields a similar policy optimization iteration: _πk_<sup>_im_</sup> +1<sup>=</sup> _arg_ max _π_<sup>_im_[</sup><sup>_L_</sup> _π_<sup>_i_1:</sup><sup>_m_</sup> ( _π_<sup>_i_1:</sup><sup>_m−_1</sup> _, π_<sup>_im_</sup> ) _− CDKL_<sup>_max_(</sup><sup>_πim, πim_)].Toavoidmaintainingvaluefunctionsfor</sup> 

> <sup>_i_</sup> _π_<sup>_m_(</sup><sup>_s, aii_1:</sup><sup>_m−−_1</sup><sup>_, aimimm_)] =</sup><sup>_E_[(</sup><sup>_π_ˆ</sup><sup>_imm_</sup><sup><u>(</u></sup><sup>_aim|sim|sm|s|ss_</sup><sup><u>)</u></sup> _π_<sup>_imm_</sup> ( _a_<sup>_imm_</sup> _|ss_ )<sup>_−_</sup> 

each single agent, the following proposition is used: _E_ [ _A_<sup>_i_</sup> _π_<sup>_m_(</sup><sup>_s, aii_1:</sup><sup>_m−−_1</sup><sup>_, aimimm_)] =</sup><sup>_E_[(</sup><sup>_π_ˆ</sup><sup>_imm_</sup><sup><u>(</u></sup><sup>_aim|sim|sm|s|ss_</sup><sup><u>)</u></sup> _π_<sup>_imm_</sup> ( _a_<sup>_imm_</sup> _|ss_ )<sup>_−_</sup> _<u>π</u>_<sup>_~~i~~_1:</sup><sup>_m−_1</sup> <u>(</u> _a_<sup>_i_1:</sup><sup>_m−_1</sup> _<u>|s</u>_ <u>)</u> 1) _π_<sup>_i_1:</sup><sup>_m−_1</sup> ( _a_<sup>_i_1:</sup><sup>_m−_1</sup> _|s_ )<sup>_Aπ_(</sup><sup>_s, a_)]),sothatitonlyneedtokeeponevaluefunction</sup><sup>_Aπ_(</sup><sup>_s, a_)forall</sup> agents.Finally, it uses the clipping trick similar to single agent PPO, obtaining the final practical algorithm, for details, please refer to (11) in the original paper. 

### **B.2.4 Multi-Agent Proximal Policy Optimization** 

MAPPO (Multi-Agent PPO) is an application of the actor-critic single-agent PPO algorithm to multi-agent tasks. It follows the CTDE structure. Each agent i follows a shared policy _πθ_ ( _ai|oi_ ) based on local observation _oi_ = _O_ ( _s_ ; _i_ ) at global state _s_ , takes its action _ai_ and optimizes its reward _J_ ( _θ_ ) = _Eat,st_ [<sup>�</sup> _t_<sup>_γtR_(</sup><sup>_st, at_)].Theactornetworkmaximizes:</sup><sup>_L_(</sup><sup>_θ_)=</sup> [ _Bn_<sup><u>1</u></sup> � _Bi_ =1 � _nk_ =1<sup>_min_(</sup><sup>_r_</sup> _θ,i_<sup>(</sup><sup>_k_)</sup><sup>_A_(</sup> _i_<sup>_k_)</sup> _, clip_ ( _rθ,i_<sup>(</sup><sup>_k_)</sup><sup>_,_1</sup><sup>_−ϵ,_1+</sup><sup>_ϵ_)</sup><sup>_A_</sup> _i_<sup>(</sup><sup>_k_)</sup> )] + _σ Bn_<sup><u>1</u></sup> � _Bi_ =1 � _nk_ =1<sup>_S_[</sup><sup>_πθ_(</sup><sup>_o_</sup> _i_<sup>(</sup><sup>_k_)</sup> )], where _n_ refers to the agent number, _A_<sup>(</sup> _I_<sup>_k_)</sup> is computed using GAE method, _S_ is policy entropy and _σ_ is entropy coefficient hyper-parameter. The critic network minimizes: _L_ ( _φ_ ) = _Bn_ <u>1</u> � _Bi_ =1 � _nk_ =1<sup>(</sup><sup>_max_[(</sup><sup>_Vφ_(</sup><sup>_s_</sup> _i_<sup>(</sup><sup>_k_)</sup> ) _− R_<sup>ˆ</sup> _i_ )<sup>2</sup> _,_ ( _clip_ ( _Vφ_ ( _si_<sup>(</sup><sup>_k_)</sup> ) _, Vφold_ ( _si_<sup>(</sup><sup>_k_)</sup> ) _− ϵ, Vφold_ ( _si_<sup>(</sup><sup>_k_)</sup> ) + _ϵ_ ) _− R_<sup>ˆ</sup> _i_ )<sup>2</sup> ]), where _R_<sup>ˆ</sup> _i_ is reward-to-go. 

### **B.2.5 Multi-Agent Deep Deterministic Policy Gradient** 

MADDPG (Multi-Agent DDPG) is an actor-critic deep policy gradient algorithm solving multi-agent tasks. Based on DDPG, it uses CTDE structure, in which the critic uses global information to optimize Q-function while training and the actor uses local observation to take actions while testing. For each agent i, update the critic by minimizing the loss function: _L_<sup>_i_</sup> ( _φ_ ) = _S_<sup><u>1</u></sup> � _j_<sup>(</sup><sup>_yj−Q_</sup> _i_<sup>_µ_(</sup><sup>**x**</sup><sup>_j, a_</sup> 1<sup>_j, . . . , aj_</sup> _N_<sup>))2,</sup> where _y_<sup>_j_</sup> = _ri_<sup>_j_+</sup><sup>_γQµ_</sup> _i_<sup>_′_(</sup><sup>**x**</sup><sup>_′j, a_</sup> 1<sup>_′, . . . , a′_</sup> _N_<sup>)</sup><sup>_|_</sup> _a_<sup>_′_</sup> _k_<sup>=</sup><sup>_µ′_</sup> _k_<sup>(</sup><sup>_σ_</sup> _k_<sup>_j_),andupdateactorusingthesampledpolicy</sup> 

31 

Table 44: Hyperparameters of HAPPO. 

|Hyperparameters|Other Tasks|Lift Underarm|Stack Block|
|---|---|---|---|
|Num mini-batches<br>|1<br>|1<br>|1<br>|
|Num opt-epochs<br>|5<br>|10<br>|5<br>|
|Num episode-length|8|20|8|
|Hidden size|[1024, 1024, 512]|[1024, 1024, 512]|[1024, 1024, 512]|
|Use popart<br>|True|True|True|
|Use value norm<br>|True<br>|True<br>|True<br>|
|Use proper time limits<br>|False<br>|False<br>|False<br>|
|Use huber loss<br>|True<br>|True<br>|True<br>|
|Huber delta<br>|10<br>|10<br>|10<br>|
|Replay Size|10000|10000|10000|
|Polyak|0.995|0.995|0.995|
|Reward scale|1|1|1|
|Clip range|0.2|0.2|0.2|
|Max grad norm|1|1|1|
|Learning rate|1.e-4|1.e-4|1.e-4|
|Discount (_γ_)|0.96|0.96|0.96|
|GAE lambda (_λ_)|0.95|0.95|0.95|
|Init noise std<br>|1|1|1|
|Ent-coef|0|0|0|



Table 45: Hyperparameters of MAPPO. 

|Hyperparameters|HandCatch|HandLift|Stack Block|
|---|---|---|---|
|Num mini-batches|1|1|1|
|Num opt-epochs|5|10|5|
|Num episode-length|8|20|8|
|Hidden size|[1024, 1024, 512]|[1024, 1024, 512]|[1024, 1024, 512]|
|Use popart|True|True|True|
|Use value norm|True|True|True|
|Use proper time limits|False|False|False|
|Use huber loss|True|True|True|
|Huber delta|10|10|10|
|Clip range|0.2|0.2|0.2|
|Max grad norm|10|10|10|
|Learning rate|5.e-4|5.e-4|5.e-4|
|Opt-eps|5.e-4|5.e-4|5.e-4|
|Discount (_γ_)|0.96|0.96|0.96|
|GAE lambda (_λ_)|0.95|0.95|0.95|
|Std x coef|1|1|1|
|Stdycoef|0.5|0.5|0.5|
|Ent-coef|0|0|0|



32 

Table 46: Hyperparameters of offline algorithms. 

|Hyperparameters|BCQ|TD3+BC|IQL|
|---|---|---|---|
|Hidden size|[400,300]|[256,256]|[256,256]|
|Learning rate|1.e-3|3.e-4|3.e-4|
|Discount (_γ_)|0.99|0.99|0.99|
|Polyak (1_−τ_)|0.995|0.995|0.995|
|Batch size|100|256|256|
|Φ|0.05|-|-|
|generated actions|10|-|-|
|_α_|-|0.2|-|
|_β_|-|-|3.0|
|_τ_ (IQL)|-|-|0.7|



gradient: _∇θiJ ≈ S_<sup><u>1</u></sup> � _j_<sup>_∇θ_</sup> _i_<sup>_µi_(</sup><sup>_σ_</sup> _i_<sup>_j_)</sup><sup>_∇a_</sup> _i_<sup>_Qµ_</sup> _i_<sup>(</sup><sup>**x**</sup><sup>_j, aj_</sup> _i_<sup>_, . . . , ai, . . . , aj_</sup> _N_<sup>)</sup><sup>_|_</sup> _ai_ = _µi_ ( _σi_<sup>_j_), where</sup><sup>_S_is the size</sup> of the mini-batch. 

### **B.3 Offline algorithms** 

### **B.3.1 BCQ** 

BCQ constrains the selected actions to be in the action distribution of the dataset. It trains a Q-network _Q_ , a perturbation network _ξ_ , and a conditional VAE _G_ = _{E_ ( _µ, σ|s, a_ ) _, D_ ( _a|s, z ∼_ ( _µ, σ_ )) _}_ . The agent generates _n_ actions by _G_ , adds small perturbations _∈_ [ _−_ Φ _,_ Φ] on the actions using _ξ_ , and then selects the action with the highest value in _Q_ . The policy can be written as 



_Q_ is updated by minimizing E( _s,a,s′_ ) _∼D|Q_ ( _s, a_ ) _−y|_<sup>2</sup> _,_ where _y_ = _r_ + _γQ_<sup>ˆ</sup> ( _s_<sup>_′_</sup> _,_ ˆ _π_ ( _s_<sup>_′_</sup> )) _. y_ is calculated by the target networks _Q_<sup>ˆ</sup> and _ξ_<sup>ˆ</sup> , where _π_ ˆ is correspondingly the policy induced by _Q_<sup>ˆ</sup> and _ξ_<sup>ˆ</sup> . _ξi_ is updated by maximizing E( _s,a_ ) _∼DQ_ ( _s, a_ + _ξ_ ( _s, a_ )). 

### **B.3.2 TD3+BC** 

TD3+BC simply adds the behavior clone term into the objective of policy optimization in TD3 to constrain the learned policy to be close to the behavior policy. Specifically, 



### **B.3.3 IQL** 

IQL avoids to query the values of any out-of-distribution actions without explicit constraints. It approximates an upper expectile of the value distribution by simply modifying the loss function in a SARSA-style TD backup, without ever using out-of-distribution actions in the target value. The V values are updated by minimizing 

E( _s,a_ ) _∼D_ [ _L_ 2<sup>_τ_(</sup><sup>_Q_(</sup><sup>_s, a_)</sup><sup>_−V_(</sup><sup>_s_))]</sup><sup>_,_</sup> 

where _L_<sup>_τ_</sup> 2<sup>(</sup><sup>_u_) =</sup><sup>_|τ−_⊮(</sup><sup>_u <_0)</sup><sup>_|u_2.And Q values are updated by minimizing</sup> 



After the Q values have converged, the policy are updated by advantage-weighted behavioral cloning: 



Most of parameters of offline algorithms follow the official settings. We find that a small _α_ for TD3+BC would achieve better performance and we choose 0 _._ 2 rather than 2 _._ 5 (official setting). BC is TD3+BC with _α_ = 0. 

33 

### **B.4 Multi-task RL algorithms** 

### **B.4.1 Multi-task PPO/SAC/TRPO** 

Multi-task PPO, Multi-task SAC, and Multi-task TRPO are basically the same as the original PPO, SAC, and TRPO, except for a small change called "disentangled alphas" in the Multi-task SAC algorithm. Alpha is the entropy coefficient used to control policy exploration. Disentangled alpha means that the learning of each task has a separate alpha coefficient for better exploration between different tasks. 

Table 47: Hyperparameters of Multi-task PPO. 

|Hyperparameters|MT1,MT4,and MT20|
|---|---|
|Num mini-batches|4|
|Num opt-epochs|5|
|Num episode-length|8|
|Hidden size|[2048, 1024, 512]|
|Clip range|0.2|
|Max grad norm|1|
|Learning rate|3.e-4|
|Discount (_γ_)|0.96|
|GAE lambda (_λ_)|0.95|
|Init noise std|0.8|
|Desired kl|0.016|
|Ent-coef|0|



### **B.5 Meta RL algorithms** 

### **B.5.1 MAML** 

MAML is a model-agnostic algorithm for meta learning, it can be used for both supervised learning and reinforcement learning. In reinforcement learning, the goal of meta-learning is to allow the agent to quickly acquire policy for new tasks through only a small amount of experience samples in the testing phase. A task is an MDP, and any aspect of the MDP may change across tasks in the task distribution _p_ ( _T_ ). At this time, the _fθ_ represents the agent’s policy (a mapping from state **x** _t_ to action **a** _t_ ), and the loss function of each task _Ti_ is: 



where H is the horizon of MDP. In a _K_ shot reinforcement learning, _K_ rollouts ( **x** 1 _,_ **a** 1 _, ...,_ **x** _H_ ) generated from _fθ_ , task _Ti_ , and their corresponding rewards _R_ ( **x** _t,_ **a** _t_ ) will be used to adapt to the new task _Ti_ . 

### **B.5.2 ProMP** 

ProMP (Proximal Meta-Policy search) proposes a novel meta-learning algorithm based on the MAML. It combines the PPO algorithm with the idea of MAML and improves the efficiency and stability of the meta-learning training process by controlling the statistical distance of both pre-adaptation and adapted policies. In general, ProMP optimizes 



where _L_<sup>_CLIP_</sup> _T_ ( _θ_<sup>_′_</sup> ) is the same as PPO which allows it to safely use a single trajectory for multiple gradient update steps, and _L_<sup>_LR_</sup> _T_<sup>(</sup><sup>_θ_) results in the following objective:</sup> 



34 

Table 48: Hyperparameters of ProMP. 

|Hyperparameters|ML1,ML4,and ML20|
|---|---|
|Num mini-batches<br>Inner loop opt-epochs|1<br>1|
|Outer loop opt-epochs|3|
|Num episode-length|8|
|Hidden size<br>Clip range|[2048, 1024, 512]<br>0.2|
|Max grad norm|1|
|Outer loop learning rate|3.e-4|
|Inner loop learning rate|3.e-4|
|Discount (_γ_)|0.9|
|GAE lambda (_λ_)<br>Init noise std|0.95<br>1|
|Desired kl<br>Ent-coef|0.016<br>0|



## **C Performance discussion of PPO and SAC** 

In our RL/MARL experiments, we found that SAC does not work on almost all tasks, which is an anomalous phenomenon. Firstly, bimanual dexterous manipulation is a challenging task, and previous studies have shown that simple model-free RL is basically unable to complete the task. So why do we get such good performance with PPO, and SAC almost all fail? We speculate that it is because the success of PPO relies on the huge improvement in sampling efficiency brought by 2048 parallel environments. Empirically, the gain of on-policy RL due to the improvement of sampling efficiency is larger than that of off-policy RL, so SAC can not be improved to the extent that it can complete the task of bimanual dexterous manipulation. In other words, it is normal that SAC can not complete our task, and PPO can complete it because of the high sampling efficiency brought by Isaac Gym. To verify our conjecture, we tested the SAC and PPO algorithm in different environments number (8, 16, 32, 64, 128, 256, 512, 1024, 2048) in the humanoid environment officially implemented by NVIDIA [19]. The results are shown in the Figure.6. It can be seen that the performance of the SAC algorithm is better than that of the PPO below 128 environments, indicating that the implementation of our SAC algorithm is good and meets our expectations. After more than 128 environments, the performance improvement of PPO by the increase of the number of environments is apparent, while the training of the SAC algorithm is unstable, and the performance is obviously inferior to the PPO. This proves our previous conjecture and explains why SAC performs so poorly on Bi-DexHands. In addition, because the action dimension of the Bi-DexHands has 50+ dimensions, the policy entropy method used by the SAC algorithm is easy causes instability during training. This instability appears to be exacerbated in the case of high sampling efficiency, and may also be a reason for the poor performance of SAC. In general, RL algorithms with high sampling efficiency will show some different characteristics. We also hope that Bi-DexHands can help researchers to study how to design RL algorithms with high sampling efficiency. 

35 







<!-- Start of picture text -->
(a) SAC (b) PPO<br><!-- End of picture text -->

Figure 6: Performance of SAC and PPO algorithms on humanoid with different numbers of environments 

|Table 49: Hyperpar|ameters of SAC.|Table 50: Hyperpar|ameters of PPO.|
|---|---|---|---|
|Hyperparameters|Humanoid|Hyperparameters|Humanoid|
|Num opt-epochs|2|Num opt-epochs|5|
|Num mini-batches|1|Num mini-batches|4|
|Num episode-length|32|Num episode-length|32|
|Hidden size|[1024, 1024, 1024]|Hidden size|[1024, 1024, 1024]|
|ReplayBuffer size|40000|Clip range|0.1|
|Learning rate|3.e-4|Learning rate|3.e-4|
|Discount (_γ_)|0.99|Discount (_γ_)|0.99|
|Polyak (1_−τ_)|0.995|GAE lambda (_λ_)|0.95|
|Ent-coef|0.2|Init noise std|1.0|
|Reward scale|1|Desired kl|0.01|
|Max grad norm|1|Max grad norm|1|
|Batch size|64|Ent-coef|0|



## **D Details of multi-task/Meta RL training** 

In order to better take advantage of Isaac Gym’s large-scale parallel simulation, the design of our multi-task/Meta RL pipeline is different from all existing benchmarks. The largest difference is that we do not need to only sample part of all tasks for training, all tasks are trained at the same time. I will introduce our pipeline and the detail of the multi-task/Meta RL categories respectively below. 

### **D.1 High performance multi-task/meta RL pipeline using Isaac Gym** 

Isaac Gym is a recent promising simulator for reinforcement learning. Different from previous simulators that can only use CPU to simulate, it can put all simulation calculations in GPU. Benefiting from the powerful parallel computing capability of GPU and avoiding switching data between CPU and GPU, Isaac Gym is able to create a large number of simulation environments in parallel without consuming many resources. This improvement in sampling efficiency is helpful for reinforcement learning, especially in on-policy RL and multi-task/meta RL. It also has a problem that Isaac Gym only allows one single environment instance to be created on a single GPU, so we can not create multiple gym-like environments at the same time as other simulators. So we designed a pipeline that runs through the entire training pipeline of one single environment instance, to make the multitask/meta RL algorithm better leverage Isaac Gym’s advantages. We directly load all tasks into an environment instance when initializing the environment, and use all tasks for data sampling and policy update at the same time, which is equivalent to that we sample all the environments every time in other simulators. In this way, each task can be trained synchronously, and the FPS is not significantly lower than one single task in parallel environments. To the best of our knowledge, our benchmark is the first to use Isaac Gym as a simulator for multi-task/meta RL. The sampling efficiency is greatly 

36 



<!-- Start of picture text -->
Train Tasks Test Tasks<br>ML1&MT1 ⋯<br>catch underarm catch underarm catch underarm catch underarm<br>desired goal 𝑔𝑤1 desired goal 𝑔𝑤2 desired goal 𝑔𝑤𝑛 desired goal 𝑔∉𝑔1⋯𝑛<br>ML4<br>catch abreast catch over2underarm catch underarm two catch underarm<br>MT4<br>catch abreast catch over2underarm catch underarm two catch underarm catch abreast catch over2underarm catch underarm two catch underarm<br>open pen cap switch grasp&place pour water open scissors<br>ML20<br>re-orientation stack block swing cup two catch underarm open bottle cap door close outward hand over lift pot door open inward door open outward<br>lift cup catch abreast catch over2underarm catch underarm door close inward<br>open pen cap switch grasp&place pour water open scissors open pen cap switch grasp&place pour water open scissors<br>MT20 re-orientation stack block swing cup two catch underarm open bottle cap re-orientation stack block swing cup two catch underarm open bottle cap<br>lift cup catch abreast catch over2underarm catch underarm door close inward lift cup catch abreast catch over2underarm catch underarm door close inward<br>door close outward hand over lift pot door open inward door open outward door close outward hand over lift pot door open inward door open outward<br><!-- End of picture text -->

Figure 7: Detail implementations of multi-task/meta settings. 

improved compared to previous simulators that rely on python parallel programs, which is helpful for multi-task/meta RL training. We hope that this will facilitate the research of multi-task/meta RL. 

### **D.2 Detail implementation of MT1, ML1, MT4, ML4, MT20, and ML20** 

Our multi-task/meta RL categories are formed by our carefully designed combinations of individual tasks detailed above. According to what we said above, the ML category is that all tasks are trained and tested at the same time. Therefore, MT1 and ML1, MT4 and ML4, MT20 and ML20 are all the same in terms of category settings. The difference is 1) ML categories only use a part of tasks as meta-train sets, and the other part is used for meta-test sets, while the MT categories are all trained together. 2) From the perspective of observation, multi-task adds a one-hot vector to represent task ID, while meta masks the observation related to the goal, which requires the Meta RL algorithm to learn by itself. Figure.2 visualizes the detailed design of our multi-task and meta categories. Let’s introduce their settings in detail separately: 

**MT1&ML1:** These two categories are only trained and tested in one type of task, only the pose of the goal is different between different tasks. We use Catch Underarm as the basic category, and translate the goal pose to the left, right, and back by 0.03cm, plus the goal of the original pose to form the task of MT1&ML1. ML1 train on left, right translation, and in-position tasks, and have to quickly adapt to backward translation tasks. 

**MT4&ML4:** These two categories consist of 4 tasks, namely Catch Underarm, Hand Over, Catch Abreast, and Two Catch Underarm. The main reason for choosing these four tasks is that they are all object throwing and catching tasks, and the skills required are relatively similar, which is conducive to multi-task and Meta RL. It should be noted that to maintain the consistency of the environment, we no longer fix the base of the handover task. ML4 train on Catch Underarm, handover, catch abreast tasks and have to adapt to two Catch Underarm tasks. 

37 



<!-- Start of picture text -->
Environment Episodes<br><!-- End of picture text -->

Figure 8: Simple point cloud RL experiment. **Left image** is an RGB image taken with the RGBD camera that comes with isaacgym and is used to convert it into a point cloud. **Middle image** is a point cloud image converted from an RGB image. **Right image** is the experimental result of using PPO to run 6000 episodes in 256 parallel ShadowHandOver environments. The purple line is the result of RL training using point cloud input, and the blue line is the result of RL training using state input. Other parameters and settings are the same as baseline. 

**MT20&ML20:** These two categories are composed of all of the 20 designed tasks. Due to the large span between different tasks, they are undoubtedly the most challenging tasks in Bi-DexHands. But it is also the most meaningful task because it covers the development of human dexterity and provides a good environment for us to master human-level dexterity. Note that there are some orders of magnitude differences in rewards between tasks. To make their rewards as close as possible, we scale the rewards in Grasp&Place, Door Open Outward, Door Open Inward, Bottle Cap, Block Stack, Door Close Inward, Door close Outward, Lift Underarm, Re Orientation, Scissors, and Swing Cup tasks by 0.1 factor to ensure the order of magnitude consistency between their rewards. ML20 needs to adapt quickly in Door Close Outward, Hand Over, Lift Pot, Open Scissors, and Two Catch Underarm tasks. All the remaining environments are given for training. 

## **E Visual observation about the Bi-DexHands** 

Currently, the observations of Bi-DexHands are state-based. This is good for a beginning research, but not a realistic setting. In the real world, the agent always needs to estimate the states of other objects by visual observations, so using visual input RL is very important for sim2real transfer. Isaac Gym can use RGBD cameras to provide us with visual information, which can be directly used as image input or processed into a point cloud. We have tried point cloud RL in Bi-DexHands, but it still has some problems. Below I will detail why we are not using visual input in Bi-DexHands. 

The problem is that the parallelism of Isaac Gym’s cameras is not very good. It can only obtain images one by one env serially, which will greatly slow down the running speed. At the same time, the training of the dexterous hand is very difficult and greatly depends on the high sampling efficiency. we do a simple experiment and result in Figure.8. We replace the object information with point clouds in the case of a small number of environments, and use PointNet to extract point cloud features. It can be seen that under the same episode and same number of environments, the performance of point cloud input is not as good as full state input, but it can also achieve some performance. But also using an RTX 3090 GPU, the point cloud RL has only 200+ fps, and the full state can reach 30000+. In fact, we can only open up to 256 environments when using point clouds. This was a problem with Isaac Gym’s poor parallel support for cameras, so we didn’t use point clouds or other visual inputs as our baselines, but they certainly could. 

38 

