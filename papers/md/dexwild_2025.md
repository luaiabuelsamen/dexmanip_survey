# **DexWild** : Dexterous Human Interactions for In-the-Wild Robot Policies 

Tony Tao<sup>_∗_</sup> , Mohan Kumar Srirama<sup>_∗_</sup> , Jason Jingzhou Liu, Kenneth Shaw, Deepak Pathak 

Carnegie Mellon University 

> _∗_ Equal contribution 

### In ~~-t~~ he ~~-W~~ ild ~~H~~ uman Da ~~t~~ a 



<!-- Start of picture text -->
L imi t ed Robo t  Da t a<br><!-- End of picture text -->





<!-- Start of picture text -->
Generalize  t o Unseen  E nvironmen t s<br><!-- End of picture text -->



<!-- Start of picture text -->
     Novel Objec t s<br>     Novel Scenes
️<br>     Cross -T ask<br>     Cross -E mbodimen t<br>De xW ild<br><!-- End of picture text -->

Fig. 1: **DexWild** enables dexterous policies to generalize to new objects, scenes, and embodiments. This is achieved by leveraging large-scale, real-world human embodiment data collected in many scenes and co-trained with a smaller robot embodiment dataset for grounding. 

**_Abstract_ —Large-scale, diverse robot datasets have emerged as a promising path toward enabling dexterous manipulation policies to generalize to novel environments, but acquiring such datasets presents many challenges. While teleoperation provides highfidelity datasets, its high cost limits its scalability. Instead, what if people could use their own hands, just as they do in everyday life, to collect data? In DexWild, a diverse team of data collectors uses their hands to collect hours of interactions across a multitude of environments and objects. To record this data, we create DexWild-System, a low-cost, mobile, and easy-to-use device. The DexWild learning framework co-trains on both human and robot demonstrations, leading to improved performance compared to training on each dataset individually. This combination results in robust robot policies capable of generalizing to novel environments, tasks, and embodiments with minimal additional robot-specific data. Experimental results demonstrate that DexWild significantly improves performance, achieving a 68.5% success rate in unseen environments—nearly four times higher than policies trained with robot data only—and offering 5.8** _×_ **better cross-embodiment generalization. Video results, codebases, and instructions at https: //dexwild.github.io** 

#### I. INTRODUCTION 

Roboticists have long dreamed of creating robots that can perform tasks with the same dexterity and adaptability as humans. We would like robots to deftly generalize to many different objects, environments, and embodiments-yet this vision of truly versatile robot behaviors remains a formidable 

challenge. While there have been many breakthroughs in large language models (LLMs) [53, 51, 3] and vision language models (VLMs) [24, 48], the key to their success lies in harnessing vast datasets. In contrast, robotics faces a critical hurdle: large-scale, diverse robot datasets needed to train foundation models do not yet exist. 

In recent years, a key approach to collecting robot datasets has been through teleoperation, which provides high-precision, high-quality action data that a policy can directly train on. [8, 21, 54]. However, acquiring this data requires highlytrained human operators working with specialized robot setups. Gathering data in diverse environments presents additional challenges such as physically relocating the robot to each new location. This data collection process is both labor-intensive and expensive, making it difficult to scale to the volume of data needed for dexterous generalization in unseen environments. 

Another approach to scaling robot datasets is to leverage internet-scale video data from platforms like YouTube, which provide vast and diverse visual grounding in real-world environments [15, 10]. However, utilizing this data effectively presents significant challenges. First, publicly available videos often lack the fine-grained accuracy needed to capture detailed hand states because vision-based body detection modules are noisy and unreliable. Additionally, these videos are not inherently structured with categorized episodes for task-specific learn- 

ing, further complicating their direct application in robotics. [18, 1, 40]. While some data collection efforts exist with more accurate and structured data, [60, 2], they do not have enough environment diversity. We seek to collect data with **tracking accuracy and environment diversity** to enable generalizable dexterous behavior. 

To overcome these barriers, some have explored collecting accurate in-the-wild human demonstrations by equipping users with a wearable gripper that directly maps their hand movements to robot actions [7]. However, this approach is cumbersome, ill-suited for natural, everyday interactions, and constrains the collected data to a specific embodiment. Other works [55] propose using dexterous hands and gloves, but they do not scale to in-the-wild environments. 

In this paper, we present DexWild, a system that enables effective learning of robust dexterous manipulation policies through co-training on human and robot demonstrations. Our key contributions include: 

- 1) **Scalable Data Collection System** : A novel humanembodiment DexWild-System that enables untrained operators to quickly collect 9,290 demonstrations across 93 diverse environments, achieving 4.6 _×_ speedup over conventional robot-based methods 

- 2) **Efficient Co-training Framework** : An approach that optimally combines human and robot demonstrations, significantly improving policy generalization to achieve 68.5% success rate in novel environments, nearly four times higher than robot-only policies. 

- 3) **Strong Cross Embodiment and Cross Task Performance** : Our data collection system combined with our co-training framework achieves of 5.8 _×_ improvement in cross-embodiment transfer over baselines and effective skill transfer across tasks. 

#### II. RELATED WORKS 

#### _A. Generalization for Imitation Learning_ 

Learning generalizable policies for robot manipulation has seen rapid progress, driven largely by advances in visual representation learning and imitation learning from large-scale datasets. On the visual side, embodied representation learning has benefited from egocentric datasets such as Ego4D [15] and EPIC-KITCHENS [10], with recent methods [27, 11, 47, 39] leveraging these datasets to train scalable visual encoders. However, these approaches still require substantial downstream robot demonstrations to train control policies. 

In parallel, robot-only demonstration datasets have grown significantly in scale and diversity [21, 8, 54], fueling research in behavior cloning and enabling generalist policy architectures [49, 8, 22]. While these policies show impressive performance across many tasks, they often struggle to generalize to unseen object categories, scene layouts, or environmental conditions [25]. This lack of robustness remains a key limitation of current systems. 

#### _B. Data Generation for Robot Manipulation_ 

Overcoming the robot data bottleneck has become a central challenge in robot learning. 

One approach leverages internet videos to extract action information. Several works, such as VideoDex [40] and HOP [42], utilize large scale human videos to learn an action prior through retargeting, which they use to bootstrap policy training. Others, such as LAPA [57], use unlabelled videos to generate latent action representations that can be used for downstream tasks. While these video-based schemes enjoy vast visual diversity, they typically fall short at capturing the precise, lowlevel motor commands needed for real-world manipulation. 

Simulation enables rapid generation of action data at scale. However, creating diverse, realistic environments for many tasks and addressing the sim-to-real gap is challenging. Recent successes in transferring manipulation policies from simulation [43] have been confined to tabletop settings and lack the generalization needed for deployment in diverse environments. 

Direct teleoperation on physical robots yields the highest fidelity, but scales poorly. Recent works have shown impressive dexterity and efficient learning in fixed scenarios [59, 56, 41, 19], yet collecting enough demonstrations to generalize across diverse scenes quickly becomes prohibitively expensive. 

Recently, there has been a growing body of work that utilizes purpose-collected high quality human embodiment data without the tedious teleoperation. We discuss these approaches in the next section. 

#### _C. Human Action Tracking Systems_ 

In order to acquire high-quality data from human motions, accurate hand and wrist tracking is of paramount importance. To bypass the complexities of hand pose estimation, several works equip users with handheld robot grippers [7, 12, 46]. While this approach simplifies retargeting, it constrains users to the specific morphology of the robot gripper, limiting the diversity of captured behavior. Moreover, many of these systems rely on SLAM-based wrist tracking, which can fail in feature-sparse environments or when occlusions occur [7, 23]—such as during drawer opening or tool use. 

Other approaches aim to estimate both hand and wrist poses directly from visual input [29, 35, 5, 45, 28, 20, 32]. These methods are easy to deploy and require no instrumentation, but their performance degrades significantly under occlusion—an unavoidable situation in manipulation. Alternative strategies for wrist tracking, such as IMU-based [9, 50] and outsidein optical systems [30], come with their own limitations: IMUs are lightweight and portable but prone to drift, while optical systems are accurate yet require laborious calibration and controlled environments. DexWild leverages calibrationfree Aruco tracking—significantly improving reliability and minimizing setup time as it requires a single monocular camera. 

While vision-based methods often attempt to track both the wrist and fingers simultaneously, many recent systems decouple the two to improve accuracy. Kinematic exoskeleton gloves can provide high-fidelity joint measurements and even haptic feedback [58], but are bulky and uncomfortable for long-term 

## ~~H~~ uman Demons ~~t~~ ra ~~t~~ ion Se ~~t~~ up 

## Robo ~~t~~ Se ~~t~~ up 



<!-- Start of picture text -->
H uman Demons t ra t ion Se t up Robo t  Se t up<br>DexWild Camera<br>Tracking Camera<br>Mini - PC<br>Mocap Glove<br>E gocen t ric E xocen t ric F ranka Panda x A rm<br><!-- End of picture text -->

Fig. 2: **Left:** DexWild efficiently capture high-fidelity data using an individual’s own hands across various environments. **Right:** Robot hands are equipped with cameras aligned with the human cameras. We test DexWild on two distinct robot hands and robot arms. 

use. Instead, DexWild, along with prior works [41, 55], adopts a lightweight glove-based solution that uses electromagnetic field (EMF) sensing to estimate fingertip positions. This allows for accurate, real-time hand tracking that is robust to occlusions and readily retargetable to a wide range of robot hands. 

#### III. DEXWILD 

Many believe that leveraging large, high-quality datasets is the key for creating dexterous robot policies that generalize [8, 49, 40, 11]. We introduce DexWild-System, a user-friendly, high-fidelity platform for efficiently gathering natural human hand demonstrations across diverse real-world settings. Compared to traditional teleoperation-based approaches, DexWildSystem enables 4.6 _×_ faster data acquisition at scale. 

Building on this system, we propose DexWild, an imitation learning framework that co-trains on large-scale DexWildSystem human demonstrations alongside a small number of robot demonstrations. This approach combines the diversity and richness of human interactions with the grounding of the robot embodiment, enabling policies to robustly generalize across new objects, environments, and embodiments. Figure 1 displays our high level approach. 

#### _A. Data Collection System_ 

A scalable data collection system for dexterous robot learning must enable natural, efficient, and high-fidelity collection across diverse environments. To this end, we design DexWild-System: a portable, user-friendly system that captures human dexterous behavior with minimal setup and training. While previous in-the-wild data collection approaches have typically relied on sensorized grippers, we aimed to create a more intuitive hardware interface that mirrors how humans naturally interact with the world. From delicate fine-motor actions to powerful grasps, humans possess dexterity across a wide range of manipulation tasks. By learning from this intrinsic capability, DexWild-System captures rich, diverse data applicable to a broad range of robot embodiments. 

DexWild-System is designed around three core objectives: 

- **Portability:** Allow rapid, large-scale data collection across diverse environments without requiring complex calibration procedures. 

- **High Fidelity:** Accurately capture fine-grained hand and environment interactions essential for training precise dexterous policies. 

- **Embodiment-Agnostic:** Enable seamless retargeting from human demonstrations to a wide variety of robot hands. 

#### **Portability:** 

To collect data in diverse real-world settings, a system must be portable, robust, and usable by anyone. We design DexWildSystem with these goals in mind: it is lightweight, easy to carry, and can be set up in just a few minutes—enabling scalable data collection across many locations. 

As shown in Figure 2, DexWild-System consists of only three components: a single tracking camera for wrist pose estimation, a battery-powered mini-PC for onboard data capture, and a custom sensor pod comprising a motion-capture glove and synchronized palm-mounted cameras. 

Unlike traditional motion capture systems [60, 13, 4, 52] that often rely on complex outside-in tracking setups that require calibration, DexWild-System is truly calibration free, making it versatile for any scenario and foolproof for untrained operators. 

This is achieved by adopting a relative state-action representation, where each state and action is captured as the relative difference from the previous time step’s pose. This eliminates any need for a global coordinate frame, allowing the tracking camera to be freely placed—either egocentrically or exocentrically. Additionally, the palm cameras are rigidly mounted in fixed positions across both human and robot embodiments. This ensures visual observations are aligned across domains, eliminating the need for further calibration at deployment. The external tracking camera, when carefully positioned, can also capture supplementary environmental context useful for learning robust policies. 

#### **High Fidelity:** 

To learn dexterous behaviors, fine-grained, nuanced motions must be captured in the training dataset. Although DexWildSystem consists of only a few portable components, we make no compromises on data fidelity. Our system is designed to accurately capture both hand and wrist actions, paired with high-quality visual observations. 

For wrist and hand tracking, vision-only methods are easy to setup. However, what they gain in portability, they often lose in accuracy and robustness—yielding noisy pose estimates that degrade policy learning [41, 14, 32, 7]. 

For hand pose estimation, we use motion capture gloves, which offer high accuracy, low latency, and robustness against occlusions [41]. For wrist tracking, we mount ArUco markers on the glove and track them using an external camera. This avoids the fragility of SLAM-based wrist tracking, which often fails in feature-sparse environments or during occlusion-heavy tasks (e.g., drawer opening). 

Unlike many datasets that rely on egocentric or distant external cameras, we place two global-shutter cameras directly on the palm. As illustrated in Figure 2, these stereo cameras capture detailed, localized interaction views with minimal motion blur and a wide field of view. This wide field of view enables policies to operate using only the onboard palm cameras, without any reliance on static viewpoints. 

#### **Embodiment-Agnostic:** 

To ensure the longevity and versatility of DexWild data, we aim for it to remain useful across different robot embodiments—even as hardware platforms evolve. Achieving this goal requires careful alignment of both the observation space and the action space between humans and robots. 

We begin by standardizing the observation space. Although our palm-mounted cameras have a wide field of view, we intentionally position them to focus primarily on the environment, minimizing the visibility of the hand itself. Importantly, the camera placement is mirrored between the human and robot hands. As shown in Figure 3, this design yields visually consistent observations across embodiments, allowing the policy to learn a shared visual representation that generalizes across both human and robot domains. 

For action space alignment, we build on insights from prior work [17, 44], optimizing robot hand kinematics to match the fingertip positions observed in human demonstrations. We note that this method is general and can work for any robot hand embodiment. It operates with fixed hyperparameters across users and is robust to variations in hand size—eliminating the need for user-specific tuning. 

Collecting data using natural human hands offers benefits beyond ease of use. The diversity in hand morphology across human demonstrators introduces useful variation, which we hypothesize helps policies learn more generalizable grasping strategies—particularly important given the inherent mismatch between human and robot hand kinematics. 

In summary, DexWild is a portable, high quality, humancentric system that can be worn by any operator to collect human data in real-world environments. Next, we explain how 



<!-- Start of picture text -->
H uman<br>Robo t<br><!-- End of picture text -->

Fig. 3: DexWild aligns the visual observations between humans and robots to bridge the embodiment gap. This incentivizes the model to learn a task-centric rather than embodiment-centric representation. 

we use the data collected by DexWild to enable dexterous policies to generalize to in-the-wild scenarios. 

#### _B. Training Data Modalities and Preprocessing_ 

Generalization in dexterous manipulation demands both scale and embodiment grounding. With this goal, DexWild collects two complementary datasets: a large-scale human demonstration dataset _DH_ using DexWild-System, and a smaller teleoperated robot dataset _DR_ . Human data offers broad task diversity and ease of collection in real-world settings, but lacks embodiment alignment. Robot data, while limited in scale, provides crucial grounding in the robot’s action and observation spaces. To harness the strengths of both, we co-train policies using a fixed ratio of human and robot data within a batch, ( _wh, wr_ )—balancing diversity with embodiment grounding to enable robust generalization during deployment. 

At each training iteration, we sample a batch consisting of transitions _xh_ and _xr_ from _DH_ and _DR_ , respectively, according to the co-training weights. Each transition _xi_ at timestep _i_ contains: 

- **Observation** _oi_ : An observation at a given timestep consists of two synchronized palm camera images _Ipinky_ and _Ithumb_ captured at the current timestep, as well as a sequence of historical states, sampled at a step size up a given horizon _H_ , comprising of _{_ ∆ _pi,_ ∆ _pi−_ step _, ...,_ ∆ _pi−H }_ . Each ∆ _p_ consists of relative historical end-effector positions. 

- **Action** _ai_ : _i_ + _n−_ 1: An action chunk of size _n_ that includes actions _{ai, ai_ +1 _, . . . , ai_ + _n−_ 1 _}_ , where _ai_ is the action at the current timestep. Specifically, _ai_ is a 26-dimensional vector consisting of: 

   - _aarm_ : A 9-dimensional vector describing relative endeffector position (3D) and orientation (6D). 

   - _ahand_ : A 17-dimensional vector describing the finger joint position targets of the robot hand. 



<!-- Start of picture text -->
Spray Bo tt le Toy Cleanup Pouring<br>F loris t Clo t hes  F olding<br><!-- End of picture text -->

Fig. 4: Using DexWild-System, humans can effortlessly collect accurate data with their own hands across a wide range of environments. This data is directly used to train any robot hand to perform dexterous manipulation in a human-like way in any environment. We validate this approach on five representative tasks. Please see videos of these tasks on our website at https://dexwild.github.io 

For bimanual tasks, the observation and action spaces are duplicated, and the inter-hand pose is appended to the observation to facilitate coordination. 

While our retargeting procedure brings human and robot trajectories into a shared action space, a few additional steps are necessary to make the human and robot datasets compatible for joint training: 

- **Action Normalization** : The actions of human and robot data are normalized separately to account for inherent distribution mismatches. 

- **Demo Filtering** : Since human demonstrations are collected by untrained operators in uncontrolled environments, we apply a heuristic-based filtering pipeline to automatically detect and remove low-quality or invalid trajectories. This filtering step significantly improves dataset quality without manual labeling. 

#### _C. Policy Training_ 

Through the careful design of our hardware, observation, and action interfaces, we are able to train dexterous robot policies using a simple behavior cloning (BC) objective [31, 37, 36]. To effectively learn from our multimodal, diverse data, our training pipeline leverages large-scale pre-trained visual encoders and shows strong performance across different policy architectures. 

**Visual Encoder** : Training on DexWild data exposes our policy to significant visual diversity—across scenes, objects, and lighting—requiring an encoder that generalizes well to such variability. To address this, we adopt a pre-trained Vision Transformer (ViT) backbone, which has shown superior performance over ResNet-based encoders on in-the-wild manipulation tasks [16, 23]. Pre-trained ViTs, especially those trained on large internet-scale datasets, are particularly effective at extracting rich, transferable features [27, 33, 47, 11], making them well-suited for our setting. 

**Policy Class** : While several imitation learning architectures have been proposed recently [59, 6], we adopt a diffusionbased policy. Diffusion models are particularly well-suited for dexterous manipulation, as they can capture multi-modal 

action distributions more effectively than alternatives such as Gaussian Mixture Models (GMMs) or transformers. This capability becomes increasingly important in DexWild, where demonstrations are collected from multiple humans with diverse strategies, resulting in inherently multi-modal behaviors. As the dataset scales, modeling this variability becomes critical for robust policy learning. Specifically, DexWild uses a diffusion U-Net model [6] to generate action chunks. 

Concretely, the training procedure is outlined in Algorithm 1. 

#### **Algorithm 1** DexWild Imitation Learning Procedure 

**Require:** Human dataset _DH_ , Robot dataset _DR_ , Co-training weights _{ωh, ωr}_ 

- 1: Initialize policy _πθ_ with ViT encoder _ϕ_ vit 

- 2: **while** not converged **do** 

- 3: Sample a batch of transitions _{xh}, {xr}_ from _DH , DR_ using weights _{ωh, ωr}_ 

- 4: **for** each transition _xi_ in the batch **do** 5: Extract observation _oi_ 6: Encode images: _Zi_ = _ϕ_ vit( _oi_ ) 7: Extract ground truth action chunk _ai_ : _i_ + _n−_ 1 = _{ai, . . . , ai_ + _n−_ 1 _}_ 

- 8: Sample noise scale _t ∼U_ (1 _, T_ ) 9: Add noise _ϵt ∼N_ (0 _, σt_ ) to _ai_ : _i_ + _n−_ 1 

- 10: Predict noise _ϵ_ ˆ _θ_ = _πθ_ ( _Zi, ai_ : _i_ + _n−_ 1 + _ϵt, t_ ) 11: Compute diffusion loss _Lθ_ = _∥ϵt − ϵ_ ˆ _θ∥_ 2<sup>2</sup> 12: **end for** 13: Update policy parameters _θ_ 

- 14: **end while** 

An important finding in our training framework is that tuning the human-to-robot data weighting significantly affects realworld performance. We discuss these effects in Section V-A. 

#### IV. EXPERIMENTS 

Our experimental evaluation encompasses extensive realworld deployment across diverse environments and robots, utilizing both human demonstrations and robot teleoperation data. Below, we outline our data collection process, experimental setup, and evaluation tasks. 











<!-- Start of picture text -->
Train<br><!-- End of picture text -->









<u>Tes</u> ~~<u>t</u>~~ 

Fig. 5: We collect data using a diverse set of objects across categories. _Spray Bottle Task_ – 25 Train, 11 Test; _Toy Cleanup Task_ – 64 Train, 9 Test; _Pour Task_ – 35 Train, 5 Test; _Florist Task_ - 6 Train, 2 Test; _Clothes Folding Task_ - 17 Train, 6 Test. 

#### _A. Scaling up Data Collection_ 

Our hardware system was deployed to 10 untrained users to collect data across a wide range of real-world environments. These settings included indoor and outdoor locations, day and night conditions, crowded cafeterias and quiet study areas, with varied tables, objects, and lighting setups. The collectors themselves varied in hand sizes and demonstration styles, enabling us to learn from a wide distribution of environments and interactions. 

We constructed two datasets through our collection efforts: _DH_ (human-collected data) and _DR_ (robot-collected data). The human dataset _DH_ comprises 9,290 demonstrations across five tasks: 3,000 demonstrations from 30 different environments for each of the _Spray Bottle_ and _Toy Cleanup_ tasks, 621 trajectories from 6 environments for the _Pour_ task, 1,545 demonstrations from 15 environments for the _Florist_ task, and 1,124 demonstrations from 12 environments for the _Clothes Folding_ task. 

The robot dataset _DR_ includes 1,395 demonstrations: 388 for _Spray Bottle_ , 370 for _Toy Cleanup_ , 111 for _Pour_ , 236 for _Florist_ , and 290 for _Clothes Folding_ tasks. Robot data was collected using an xArm and LEAP hand V2 Advanced. Our training and test objects are detailed in Figure 5. 

#### _B. Evaluation Tasks_ 

We evaluate our approach on five diverse manipulation tasks, each designed to assess specific aspects of dexterous manipulation: functional grasping, long-horizon planning, crosstask transfer, bimanual coordination, and deformable object manipulation. A task visualization is provided in Figure 4. 

In the Spray Bottle task, the robot grasps a spray bottle by the handle and sprays a target cloth, testing functional grasping and affordance understanding. In Toy Cleanup, the robot picks up scattered toys and places them in a bin, evaluating generalization and long-horizon planning. The Pouring task involves tilting a bottle to pour into a container, demonstrating skill transfer from the spray bottle task. In Bimanual Florist, the robot hands over a flower between its arms and inserts it into a vase, testing precise bimanual coordination. Finally, in Bimanual Clothes Folding, the robot uses both hands to fold a clothing item, assessing manipulation of deformable objects. Full task specifications and scoring criteria for all tasks are provided in Appendix VII-A. 

These tasks systematically evaluate DexWilds _functional grasping_ capabilities, _generalization_ across object types, _transferal_ of skills across tasks, _coordination_ between arms, and _adaptability_ to deformable objects. Success requires the policy to adapt to varying object properties, environmental conditions, and task constraints. 

#### _C. Evaluation Environments_ 

For robot experiments, we employed an xArm robot and Franka system, both equipped with either LEAP hand or LEAP hand V2 Advanced [38, 41]. Unless explicitly mentioned, xArm and LEAP hand V2 Advanced was used. We evaluate our approach across three scenarios: 

- 1) In-Domain: Environments where robot training data was collected, testing with novel objects 

- 2) In-the-Wild: Environments present in DexWild but absent from robot training data 

- 3) In-the-Wild Extreme: Unseen environments absent from both datasets. 

V. ANALYSIS AND RESULTS 

In our evaluations, we seek to investigate the following key questions: 

- 1) How effectively does DexWild leverage human data to achieve strong in-the-wild performance? 

- 2) Does DexWild enable policy transfer across tasks and robot embodiments? 

- 3) Does policy performance scale effectively with increasing amounts of DexWild-System data? 

Please see videos of our results at https://dexwild.github.io. 

#### _A. Zero Shot In the Wild Policies w/ DexWild_ 

**DexWild enables strong policy generalization in novel scenes.** We evaluate policies in environments with increasing novelty to assess their generalization. As shown in Figure 6, policies trained exclusively on robot data perform well in indomain settings (64.7% success rate) but degrade significantly in more challenging scenarios—in-the-wild (28.5%) and inthe-wild extreme (22.0%). This 36-point performance drop suggests that robot-only policies overfit to environment-specific features and fail to develop robust, transferable representations. In contrast, policies trained only on human data learn highlevel object affordances and approach objects reliably, even 



<!-- Start of picture text -->
In-Domain Performance In the Wild Performance In the Wild Extreme Performance<br>0.8<br>0.8<br>0.6<br>0.6<br>0.6<br>0.4<br>0.4<br>0.4<br>0.2<br>0.2 0.2<br>0.0 0.0 0.0<br>Spray Toy Average Spray Toy Average Spray Toy Florist Clothes Average<br>Cleanup Cleanup Cleanup Folding<br>Robot Only Co-train 1:1 Co-train 1:2 (Ours) Co-train 1:5 Human Only<br>Score<br><!-- End of picture text -->

Fig. 6: **How does co-training help with scaling up in the wild performance?** We evaluate our policy across three scenarios: (a) In-Domain scenes where robot training data was collected but with novel objects, (b) In-the-Wild scenes present in DexWild but not in robot data, and (c) In-the-Wild Extreme scenes absent from both datasets. Displayed ratio is Robot:Human. 

in complex scenes. However, without robot-specific action grounding, they struggle to execute precise manipulation, resulting in poor performance across all scenarios (3.6% indomain, 7.3% in-the-wild). 

To combine the strengths of both modalities, we adopt a co-training strategy—jointly training on both robot and human data—a method validated in prior works [8, 49, 21, 20, 32]. This encourages the policy to learn task-relevant features rather than overfitting to specific embodiments or environments. We experiment with different **robot-to-human** data ratios (1:1 to 1:5) per training batch. Our empirical analysis reveals that a 1:2 ratio yields optimal performance across all scenarios: 

- 1) In Domain: 79.8% vs. 64.7% (robot-only) 

- 2) In-the-wild: 75.1% vs. 28.5% (robot-only) 

- 3) In-the-wild Extreme: 62.7% vs. 22.0% (robot-only) 

Interestingly, increasing the human data ratio further (e.g., 1:5) degrades performance (54.5% in-domain, 50.9% in-thewild), indicating that robot data remains essential for grounding fine-grained control. 

**DexWild extends to complex bimanual coordination tasks.** To evaluate whether DexWild generalizes beyond singlearm tasks, we test it on bimanual tasks that demand precise coordination between two hands. We compare co-trained policies (1:2 ratio) against robot-only policies in in-the-wild extreme settings. DexWild policies achieve a strong 68.1% average success rate, compared to just 13% for the robotonly baseline. Even when failures occur, DexWild policies exhibit meaningful attempts at task execution—while robotonly policies often produce erratic or unstructured behavior. 

These results demonstrate that DexWild not only enables robust generalization across environments but also scales to more complex manipulation behaviors. 

#### _B. Robust Cross-Task and Cross-Embodiment Generalization_ 

**DexWild enables transfer of low-level skills across tasks.** Many manipulation tasks share foundational motor skills—such as lifting, orienting, and rotating objects—which opens the door to skill reuse across related tasks. For example, opening a microwave and opening a cupboard both involve similar coordination and control. We evaluate this form of cross-task 

transfer using the _pouring_ task, which shares many motion primitives with the _spray_ task. Crucially, we use no robot data for pouring and instead combine human (DexWild-System) demonstrations of pouring with robot demonstrations from spraying. This setup enables **zero-shot generalization** to pouring in in-the-wild extreme environments. Using a 1:2 robot-to-human co-training ratio, our policy achieves a **94% success rate** , far exceeding policies trained with only robot (0%) or only human data (11%). 

**DexWild enables transfer across robot embodiments.** Since DexWild data is not tied to any specific embodiment, it naturally supports cross-platform transfer. This prolongs the value of our data, as collecting platform-specific data for every new robot is resource-intensive and impractical. We test two transfer scenarios in in-the-wild extreme scenes: 

- **Cross-arm** : Transferring from an xArm to a Franka Panda arm. We achieve a 37.5% success rate, compared to 4.5% for the robot-only baseline—an **8.3** _×_ **improvement** . 

- **Cross-hand** : Transferring from the LEAP Hand V2 Advanced to the original LEAP Hand. We achieve 65.3% success versus 13.3% for the baseline, showing that DexWild generalizes not only across arms, but across dexterous hands as well. 

These results, shown in Figure 7, demonstrate that DexWild enables zero-shot generalization to new tasks and hardware embodiments **without any additional robot-specific data** , making it an efficient and general framework for dexterous policy learning on many robots. 

#### _C. Scalability of DexWild_ 

**Policy performance scales with dataset size.** To understand how data scale impacts policy performance in the wild, we randomly sample subsets of the full human dataset at varying sizes and evaluate the resulting policies. We fix the size of the robot dataset. As shown in Figure 7, there is a clear positive correlation between dataset size and average task performance—rising from 28.7% at 20% dataset size to 67.8% with the full dataset, marking a 2.36 _×_ improvement. Interestingly, the learning curve is nonlinear, with especially steep gains 



<!-- Start of picture text -->
Cross-Task Performance Cross-Embodiment Performance Scaling Performance<br>1.0 1.0 1.0<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0.0 0.0 0.0<br>Cross-Hand Cross-Arm 0 25 50 100<br>Type DexWild Dataset Scale (%)<br>Robot Only Co-train 1:1 Co-train 1:2 (Ours) Co-train 1:5 Human Only<br>Score<br><!-- End of picture text -->

Fig. 7: Left: **Cross-Task Performance** – Evaluating DexWild on the pour task using robot data exclusively from the spray task. Middle: **Cross-Embodiment Performance** – Testing DexWild policy on the Original LEAP hand and a Franka robot arm. Right: **Scaling Performance** – Demonstrating improved DexWild performance as dataset size increases. Displayed ratio is Robot:Human. 

in the 25–50% range, suggesting a critical threshold where the policy begins to reliably learn generalizable behaviors. 

Importantly, performance continues to improve all the way to 100% data usage, indicating that the system has not yet plateaued. This suggests that even more capable policies could be learned with continued data collection. 

**DexWild-System enables fast and scalable data collection.** Given the observed benefits of scaling, we evaluate the data collection efficiency of DexWild-System via a comparative user study measuring demonstrations per hour. As shown in Figure 8, DexWild-System achieves an average collection rate of **201 demos/hour** across five representative tasks—nearly matching the rate of demonstrations collected using bare hands and **4.6** _×_ **faster** than a traditional robot teleoperation system based on Gello [41, 56], which achieves just 43 demos/hour. 

We identify three key limitations of Gello-based collection that our system overcomes: 

- 1) **Lack of haptic feedback:** Operators cannot feel objects, making fine manipulation difficult for certain tasks. 

- 2) **Scene reset:** Resetting the environment is cumbersome and often requires a second operator or pauses in data collection. 

- 3) **Hardware setup overhead:** Robots are heavy and require time-consuming setup at each new location, whereas DexWild-System is portable and can be set up in minutes. 



<!-- Start of picture text -->
Data Collection Speed by Method<br>250<br>200<br>150<br>100<br>50<br>0<br>Spray Toy Pour Florist Clothes Average<br>Cleanup Folding<br>Robot Ours Human<br>Demos per hour<br><!-- End of picture text -->

Fig. 8: DexWild-System offers **4.6** _×_ improvement over robot data collection speed and nearly matches the human bare hands data collection speed. 

DexWild not only demonstrates strong scaling trends with increasing data volume, but also offers a practical and efficient path to collecting diverse, high-quality data at scale—crucial for real-world generalization. 

#### VI. CONCLUSION AND LIMITATIONS 

We introduce DexWild, a scalable framework for learning dexterous manipulation policies that effectively generalize to new tasks, environments, and robot embodiments. We introduce DexWild-System, a portable, human-centric data collection device that significantly accelerates dataset creation (4.6 _×_ faster than conventional robot teleoperation). We propose DexWild cotraining method, which leverages large scale human demonstrations alongside minimal robot data to achieve robust generalization-reaching a success rate of 68.5% in completely unseen environments, nearly four times higher than methods using robot data only. Furthermore, DexWild’s embodimentagnostic design enables strong cross-embodiment and cross-task transfer capabilities, reducing the need for robot-specific data. 

Despite these strengths, several limitations remain that motivate future research: First, our approach still depends on a limited number of teleoperated robot data to bridge the gap between human and robot actions. Future work could explore improved retargeting or online policy adaptation to remove the need for teleoperated data. Next, because humans typically perform these tasks successfully, their demonstrations seldom include error recovery—causing trained policies to struggle to recover from unexpected failures. Adding recovery examples or adaptive strategies could boost real-world robustness. Finally, our method uses only visual and kinematic data, which limits its performance in contact-rich tasks. Incorporating tactile or haptic sensing could improve the handling of delicate interactions. 

In summary, DexWild represents a significant step toward scalable, generalizable robot manipulation policies. Our results highlight the promise of leveraging human interaction data at scale, offering an exciting avenue toward truly dexterous and versatile robots operating in diverse, real-world environments. 

Videos, code, and hardware instructions are available on our website at https://dexwild.github.io 

#### ACKNOWLEDGMENTS 

We would like to thank Yulong Li, Hengkai Pan, and Sandeep Routray for thoughtful discussions. We’d also like to thank Andrew Wang for setting up compute and Yulong Li for helping with robot system setup. Lastly, we’d like to express thanks to Hengkai Pan, Andrew Wang, Adam Kan, Ray Liu, Mingxuan Li, Lukas Vargas, Jose German, Laya Satish, Sri Shasanka Madduri for helping collect data. This work was supported in part by AFOSR FA9550-23-1-0747 and Apple Research Award. 

#### REFERENCES 

- [1] Shikhar Bahl, Russell Mendonca, Lili Chen, Unnat Jain, and Deepak Pathak. Affordances from human videos as a versatile representation for robotics. 2023. 2 

- [2] Prithviraj Banerjee, Sindi Shkodrani, Pierre Moulon, Shreyas Hampali, Shangchen Han, Fan Zhang, Linguang Zhang, Jade Fountain, Edward Miller, Selen Basol, et al. Hot3d: Hand and object tracking in 3d from egocentric multi-view videos. _arXiv preprint arXiv:2411.19167_ , 2024. 2 

- [3] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. _Advances in neural information processing systems_ , 33: 1877–1901, 2020. 1 

- [4] Yu-Wei Chao, Wei Yang, Yu Xiang, Pavlo Molchanov, Ankur Handa, Jonathan Tremblay, Yashraj S Narang, Karl Van Wyk, Umar Iqbal, Stan Birchfield, et al. Dexycb: A benchmark for capturing hand grasping of objects. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 9044–9053, 2021. 

   - 3 

- [5] Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, and Xiaolong Wang. Open-television: Teleoperation with immersive active visual feedback. _arXiv preprint arXiv:2407.01512_ , 2024. 2 

- [6] Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, and Shuran Song. Diffusion policy: Visuomotor policy learning via action diffusion. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2023. 5, 14 

- [7] Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Russ Tedrake, and Shuran Song. Universal manipulation interface: Inthe-wild robot teaching without in-the-wild robots. In _Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)_ , 2024. 2, 4 

- [8] Open X-Embodiment Collaboration, Abby O’Neill, Abdul Rehman, Abhinav Gupta, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, Ajinkya Jain, Albert Tung, Alex Bewley, Alex Herzog, Alex Irpan, Alexander Khazatsky, Anant Rai, Anchit Gupta, Andrew Wang, Andrey 

Kolobov, Anikait Singh, Animesh Garg, Aniruddha Kembhavi, Annie Xie, Anthony Brohan, Antonin Raffin, Archit Sharma, Arefeh Yavary, Arhan Jain, Ashwin Balakrishna, Ayzaan Wahid, Ben Burgess-Limerick, Beomjoon Kim, Bernhard Scholkopf,¨ Blake Wulfe, Brian Ichter, Cewu Lu, Charles Xu, Charlotte Le, Chelsea Finn, Chen Wang, Chenfeng Xu, Cheng Chi, Chenguang Huang, Christine Chan, Christopher Agia, Chuer Pan, Chuyuan Fu, Coline Devin, Danfei Xu, Daniel Morton, Danny Driess, Daphne Chen, Deepak Pathak, Dhruv Shah, Dieter Buchler,¨ Dinesh Jayaraman, Dmitry Kalashnikov, Dorsa Sadigh, Edward Johns, Ethan Foster, Fangchen Liu, Federico Ceola, Fei Xia, Feiyu Zhao, Felipe Vieira Frujeri, Freek Stulp, Gaoyue Zhou, Gaurav S. Sukhatme, Gautam Salhotra, Ge Yan, Gilbert Feng, Giulio Schiavi, Glen Berseth, Gregory Kahn, Guangwen Yang, Guanzhi Wang, Hao Su, Hao-Shu Fang, Haochen Shi, Henghui Bao, Heni Ben Amor, Henrik I Christensen, Hiroki Furuta, Homanga Bharadhwaj, Homer Walke, Hongjie Fang, Huy Ha, Igor Mordatch, Ilija Radosavovic, Isabel Leal, Jacky Liang, Jad Abou-Chakra, Jaehyung Kim, Jaimyn Drake, Jan Peters, Jan Schneider, Jasmine Hsu, Jay Vakil, Jeannette Bohg, Jeffrey Bingham, Jeffrey Wu, Jensen Gao, Jiaheng Hu, Jiajun Wu, Jialin Wu, Jiankai Sun, Jianlan Luo, Jiayuan Gu, Jie Tan, Jihoon Oh, Jimmy Wu, Jingpei Lu, Jingyun Yang, Jitendra Malik, Joao˜ Silverio,´ Joey Hejna, Jonathan Booher, Jonathan Tompson, Jonathan Yang, Jordi Salvador, Joseph J. Lim, Junhyek Han, Kaiyuan Wang, Kanishka Rao, Karl Pertsch, Karol Hausman, Keegan Go, Keerthana Gopalakrishnan, Ken Goldberg, Kendra Byrne, Kenneth Oslund, Kento Kawaharazuka, Kevin Black, Kevin Lin, Kevin Zhang, Kiana Ehsani, Kiran Lekkala, Kirsty Ellis, Krishan Rana, Krishnan Srinivasan, Kuan Fang, Kunal Pratap Singh, Kuo-Hao Zeng, Kyle Hatch, Kyle Hsu, Laurent Itti, Lawrence Yunliang Chen, Lerrel Pinto, Li Fei-Fei, Liam Tan, Linxi ”Jim” Fan, Lionel Ott, Lisa Lee, Luca Weihs, Magnum Chen, Marion Lepert, Marius Memmel, Masayoshi Tomizuka, Masha Itkina, Mateo Guaman Castro, Max Spero, Maximilian Du, Michael Ahn, Michael C. Yip, Mingtong Zhang, Mingyu Ding, Minho Heo, Mohan Kumar Srirama, Mohit Sharma, Moo Jin Kim, Naoaki Kanazawa, Nicklas Hansen, Nicolas Heess, Nikhil J Joshi, Niko Suenderhauf, Ning Liu, Norman Di Palo, Nur Muhammad Mahi Shafiullah, Oier Mees, Oliver Kroemer, Osbert Bastani, Pannag R Sanketi, Patrick ”Tree” Miller, Patrick Yin, Paul Wohlhart, Peng Xu, Peter David Fagan, Peter Mitrano, Pierre Sermanet, Pieter Abbeel, Priya Sundaresan, Qiuyu Chen, Quan Vuong, Rafael Rafailov, Ran Tian, Ria Doshi, Roberto Mart’in-Mart’in, Rohan Baijal, Rosario Scalise, Rose Hendrix, Roy Lin, Runjia Qian, Ruohan Zhang, Russell Mendonca, Rutav Shah, Ryan Hoque, Ryan Julian, Samuel Bustamante, Sean Kirmani, Sergey Levine, Shan Lin, Sherry Moore, Shikhar Bahl, Shivin Dass, Shubham Sonawani, Shubham Tulsiani, Shuran Song, Sichun Xu, Siddhant Haldar, Siddharth Karamcheti, Simeon Ade- 

bola, Simon Guist, Soroush Nasiriany, Stefan Schaal, Stefan Welker, Stephen Tian, Subramanian Ramamoorthy, Sudeep Dasari, Suneel Belkhale, Sungjae Park, Suraj Nair, Suvir Mirchandani, Takayuki Osa, Tanmay Gupta, Tatsuya Harada, Tatsuya Matsushima, Ted Xiao, Thomas Kollar, Tianhe Yu, Tianli Ding, Todor Davchev, Tony Z. Zhao, Travis Armstrong, Trevor Darrell, Trinity Chung, Vidhi Jain, Vikash Kumar, Vincent Vanhoucke, Wei Zhan, Wenxuan Zhou, Wolfram Burgard, Xi Chen, Xiangyu Chen, Xiaolong Wang, Xinghao Zhu, Xinyang Geng, Xiyuan Liu, Xu Liangwei, Xuanlin Li, Yansong Pang, Yao Lu, Yecheng Jason Ma, Yejin Kim, Yevgen Chebotar, Yifan Zhou, Yifeng Zhu, Yilin Wu, Ying Xu, Yixuan Wang, Yonatan Bisk, Yongqiang Dou, Yoonyoung Cho, Youngwoon Lee, Yuchen Cui, Yue Cao, Yueh-Hua Wu, Yujin Tang, Yuke Zhu, Yunchu Zhang, Yunfan Jiang, Yunshuang Li, Yunzhu Li, Yusuke Iwasawa, Yutaka Matsuo, Zehan Ma, Zhuo Xu, Zichen Jeff Cui, Zichen Zhang, Zipeng Fu, and Zipeng Lin. Open X-Embodiment: Robotic learning datasets and RT-X models, 2023. 1, 2, 

   - 3, 7 

- [9] Juan Antonio Corrales, Francisco A Candelas, and Fernando Torres. Hybrid tracking of human operators using imu/uwb data fusion by a kalman filter. In _Proceedings of the 3rd ACM/IEEE international conference on Human robot interaction_ , pages 193–200, 2008. 2 

- [10] Dima Damen, Hazel Doughty, Giovanni Maria Farinella, Sanja Fidler, Antonino Furnari, Evangelos Kazakos, Davide Moltisanti, Jonathan Munro, Toby Perrett, Will Price, and Michael Wray. Epic-kitchens: A large-scale dataset for recognizing, anticipating, and retrieving handobject interactions. In _Proceedings of the European Conference on Computer Vision (ECCV)_ , pages 802–819, 2018. 1, 2 

- [11] Sudeep Dasari, Mohan Kumar Srirama, Unnat Jain, and Abhinav Gupta. An unbiased look at datasets for visuomotor pre-training. In _Conference on Robot Learning_ . PMLR, 2023. 2, 3, 5, 14 

- [12] Haritheja Etukuru, Norihito Naka, Zijin Hu, Seungjae Lee, Julian Mehu, Aaron Edsinger, Chris Paxton, Soumith Chintala, Lerrel Pinto, and Nur Muhammad Mahi Shafiullah. Robot utility models: General policies for zero-shot deployment in new environments, 2024. 2 

- [13] Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed Kocabas, Manuel Kaufmann, Michael J Black, and Otmar Hilliges. Arctic: A dataset for dexterous bimanual handobject manipulation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 12943–12954, 2023. 3 

- [14] Authors from UC San Diego and MIT. Open-television: An open-source immersive teleoperation system with stereo visual feedback. _The Robot Report_ , 2024. 4 

- [15] Kristen Grauman, Michael Ryoo, Aljosaˇ Smolic,´ Minh Vo, and et al. Ego4d: Around the world in 3,000 hours of egocentric video. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ 

_(CVPR)_ , pages 11743–11753, 2022. 1, 2 

- [16] Huy Ha, Yihuai Gao, Zipeng Fu, Jie Tan, and Shuran Song. UMI on legs: Making manipulation policies mobile with manipulation-centric whole-body controllers. In _Proceedings of the 2024 Conference on Robot Learning_ , 2024. 5 

- [17] Ankur Handa, Karl Van Wyk, Wei Yang, Jacky Liang, Yu-Wei Chao, Qian Wan, Stan Birchfield, Nathan Ratliff, and Dieter Fox. Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 9164–9170. IEEE, 2020. 4 

- [18] Yafei Hu, Quanting Xie, Vidhi Jain, Jonathan Francis, Jay Patrikar, Nikhil Keetha, Seungchan Kim, Yaqi Xie, Tianyi Zhang, Zhibo Zhao, et al. Toward general-purpose robots via foundation models: A survey and meta-analysis. _arXiv preprint arXiv:2312.08782_ , 2023. 2 

- [19] Aadhithya Iyer, Zhuoran Peng, Yinlong Dai, Irmak Guzey, Siddhant Haldar, Soumith Chintala, and Lerrel Pinto. OPEN TEACH: A versatile teleoperation system for robotic manipulation. _arXiv preprint arXiv:2403.07870_ , 2024. 2 

- [20] Simar Kareer, Dhruv Patel, Ryan Punamiya, Pranay Mathur, Shuo Cheng, Chen Wang, Judy Hoffman, and Danfei Xu. Egomimic: Scaling imitation learning via egocentric video, 2024. 2, 7 

- [21] Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth Karamcheti, Soroush Nasiriany, Mohan Kumar Srirama, Lawrence Yunliang Chen, Kirsty Ellis, et al. Droid: A large-scale in-the-wild robot manipulation dataset. _arXiv preprint arXiv:2403.12945_ , 2024. 1, 2, 7 

- [22] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, et al. Openvla: An open-source vision-language-action model. _arXiv preprint arXiv:2406.09246_ , 2024. 2 

- [23] Fanqi Lin, Yingdong Hu, Pingyue Sheng, Chuan Wen, Jiacheng You, and Yang Gao. Data scaling laws in imitation learning for robotic manipulation. In _Conference on Robot Learning (CoRL)_ , 2024. 2, 5 

- [24] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. In _NeurIPS_ , 2023. 1 

- [25] Ajay Mandlekar, Danfei Xu, Josiah Wong, Soroush Nasiriany, Chen Wang, Rohun Kulkarni, Li Fei-Fei, Silvio Savarese, Yuke Zhu, and Roberto Mart´ın-Mart´ın. What matters in learning from offline human demonstrations for robot manipulation. _arXiv preprint arXiv:2108.03298_ , 2021. 2 

- [26] Mayank Mittal, Calvin Yu, Qinxi Yu, Jingzhou Liu, Nikita Rudin, David Hoeller, Jia Lin Yuan, Ritvik Singh, Yunrong Guo, Hammad Mazhar, Ajay Mandlekar, Buck Babich, Gavriel State, Marco Hutter, and Animesh Garg. Orbit: A unified simulation framework for interactive robot learning environments. _IEEE Robotics and Automation Letters_ , 8(6):3740–3747, June 2023. ISSN 

2377-3774. doi: 10.1109/lra.2023.3270034. URL http: //dx.doi.org/10.1109/LRA.2023.3270034. 14 

- [27] Suraj Nair, Aravind Rajeswaran, Vikash Kumar, and Chelsea Finn. R3M: A universal visual representation for robot manipulation. _arXiv preprint arXiv:2203.12601_ , 2022. 2, 5 

- [28] Georgios Pavlakos, Dandan Shan, Ilija Radosavovic, Angjoo Kanazawa, David Fouhey, and Jitendra Malik. Hamer: Hand mesh recovery for the egoexo4d hand pose challenge. 2 

- [29] Georgios Pavlakos, Dandan Shan, Ilija Radosavovic, Angjoo Kanazawa, David Fouhey, and Jitendra Malik. Reconstructing hands in 3d with transformers. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2024. 2 

- [30] Alexandra Pfister, Alexandre M West, Shaw Bronner, and Jack Adam Noah. Comparative abilities of microsoft kinect and vicon 3d motion capture for gait analysis. _Journal of medical engineering & technology_ , 38(5):274– 280, 2014. 2 

- [31] Dean A Pomerleau. Alvinn: An autonomous land vehicle in a neural network. _Advances in neural information processing systems_ , 1, 1988. 5 

- [32] Ri-Zhao Qiu, Shiqi Yang, Xuxin Cheng, Chaitanya Chawla, Jialong Li, Tairan He, Ge Yan, David J. Yoon, Ryan Hoque, Lars Paulsen, Ge Yang, Jian Zhang, Sha Yi, Guanya Shi, and Xiaolong Wang. Humanoid policy ˜ human policy. _arXiv preprint arXiv:2503.13441_ , 2025. 2, 4, 7 

- [33] Ilija Radosavovic, Tete Xiao, Stephen James, Pieter Abbeel, Jitendra Malik, and Trevor Darrell. Real-world robot learning with masked visual pre-training. _CoRL_ , 2022. 5 

- [34] Nathan D. Ratliff, Jan Issac, Daniel Kappler, Stan Birchfield, and Dieter Fox. Riemannian motion policies, 2018. URL https://arxiv.org/abs/1801.02854. 14 

- [35] Yu Rong, Takaaki Shiratori, and Hanbyul Joo. Frankmocap: A monocular 3d whole-body pose estimation system via regression and integration. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 1749–1759, 2021. 2 

- [36] Stephane´ Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. In _Proceedings of the fourteenth international conference on artificial intelligence and statistics_ , pages 627–635. JMLR Workshop and Conference Proceedings, 2011. 5 

- [37] Stefan Schaal. Is imitation learning the route to humanoid robots? _Trends in cognitive sciences_ , 3(6):233–242, 1999. 5 

- [38] Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _Robotics: Science and Systems (RSS)_ , 2023. 6 

- [39] Kenneth Shaw, Shikhar Bahl, and Deepak Pathak. Videodex: Learning dexterity from internet videos. In 

   - Karen Liu, Dana Kulic, and Jeff Ichnowski, editors, _Proceedings of The 6th Conference on Robot Learning_ , volume 205 of _Proceedings of Machine Learning Research_ , pages 654–665. PMLR, 14–18 Dec 2023. 2 

- [40] Kenneth Shaw, Shikhar Bahl, and Deepak Pathak. Videodex: Learning dexterity from internet videos. In _Conference on Robot Learning_ , pages 654–665. PMLR, 2023. 2, 3 

- [41] Kenneth Shaw, Yulong Li, Jiahui Yang, Mohan Kumar Srirama, Ray Liu, Haoyu Xiong, Russell Mendonca, and Deepak Pathak. Bimanual dexterity for complex tasks. In _8th Annual Conference on Robot Learning_ , 2024. 2, 3, 4, 6, 8, 14 

- [42] Himanshu Gaurav Singh, Antonio Loquercio, Carmelo Sferrazza, Jane Wu, Haozhi Qi, Pieter Abbeel, and Jitendra Malik. Hand-object interaction pretraining from videos, 2024. URL https://arxiv.org/abs/2409.08273. 2 

- [43] Ritvik Singh, Arthur Allshire, Ankur Handa, Nathan Ratliff, and Karl Van Wyk. Dextrah-rgb: Visuomotor policies to grasp anything with dexterous hands. _arXiv preprint arXiv:2412.01791_ , 2024. 2 

- [44] Aravind Sivakumar, Kenneth Shaw, and Deepak Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube, 2022. 4 

- [45] Aravind Sivakumar, Kenneth Shaw, and Deepak Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube. _RSS_ , 2022. 2 

- [46] Shuran Song, Andy Zeng, Johnny Lee, and Thomas Funkhouser. Grasping in the wild: Learning 6dof closedloop grasping from low-cost demonstrations. _Robotics and Automation Letters_ , 2020. 2 

- [47] Mohan Kumar Srirama, Sudeep Dasari, Shikhar Bahl, and Abhinav Gupta. HRP: Human affordances for robotic pre-training. In _Proceedings of Robotics: Science and Systems_ , Delft, Netherlands, 2024. 2, 5 

- [48] Andreas Steiner, Andre´ Susano Pinto, Michael Tschannen, Daniel Keysers, Xiao Wang, Yonatan Bitton, Alexey Gritsenko, Matthias Minderer, Anthony Sherbondy, Shangbang Long, Siyang Qin, Reeve Ingle, Emanuele Bugliarello, Sahar Kazemzadeh, Thomas Mesnard, Ibrahim Alabdulmohsin, Lucas Beyer, and Xiaohua Zhai. PaliGemma 2: A Family of Versatile VLMs for Transfer. _arXiv preprint arXiv:2412.03555_ , 2024. 1 

- [49] OM Team, D Ghosh, H Walke, K Pertsch, K Black, O Mees, S Dasari, J Hejna, C Xu, J Luo, et al. Octo: An open-source generalist robot policy. _Proceedings of Robotics: Science and Systems, Delft, Netherlands_ , 2023. 2, 3, 7 

- [50] Yushuang Tian, Xiaoli Meng, Dapeng Tao, Dongquan Liu, and Chen Feng. Upper limb motion tracking with the integration of imu and kinect. _Neurocomputing_ , 159: 207–218, 2015. 2 

- [51] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee´ Lacroix, Baptiste Roziere,` Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language 

models. _arXiv preprint arXiv:2302.13971_ , 2023. 1 

- [52] Valve Corporation. https://store.steampowered.com/ steamvr. [Virtual reality platform]. 3 

- [53] A Vaswani. Attention is all you need. _Advances in Neural Information Processing Systems_ , 2017. 1 

- [54] Homer Walke, Kevin Black, Abraham Lee, Moo Jin Kim, Max Du, Chongyi Zheng, Tony Zhao, Philippe HansenEstruch, Quan Vuong, Andre He, Vivek Myers, Kuan Fang, Chelsea Finn, and Sergey Levine. Bridgedata v2: A dataset for robot learning at scale. In _Conference on Robot Learning (CoRL)_ , 2023. 1, 2 

- [55] Chen Wang, Haochen Shi, Weizhuo Wang, Ruohan Zhang, Li Fei-Fei, and Karen Liu. Dexcap: Scalable and portable mocap data collection system for dexterous manipulation. In _Robotics: Science and Systems (RSS)_ , 2024. 2, 3 

- [56] Philipp Wu, Yide Shentu, Zhongke Yi, Xingyu Lin, and Pieter Abbeel. Gello: A general, low-cost, and intuitive teleoperation framework for robot manipulators, 2023. 2, 8 

- [57] Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Sejune Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, et al. Latent action pretraining from videos. _arXiv preprint arXiv:2410.11758_ , 2024. 2 

- [58] Han Zhang, Songbo Hu, Zhecheng Yuan, and Huazhe Xu. Doglove: Dexterous manipulation with a low-cost open-source haptic force feedback glove. _arXiv preprint arXiv:2502.07730_ , 2025. 2 

- [59] Tony Z. Zhao, Vikash Kumar, Sergey Levine, and Chelsea Finn. Learning fine-grained bimanual manipulation with low-cost hardware. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2023. 2, 5, 14 

- [60] Christian Zimmermann, Duygu Ceylan, Jimei Yang, Bryan Russell, Max Argus, and Thomas Brox. Freihand: A dataset for markerless capture of hand pose and shape from single rgb images. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 813– 822, 2019. 2, 3 

#### VII. APPENDIX 

Videos of our results, code to recreate our system, and hardware instructions are available on our website at https: //dexwild.github.io 

#### _A. Detailed Task Description and Scoring Criteria:_ 

We evaluate five dexterous manipulation tasks, each designed to assess different capabilities such as functional grasping, long-horizon planning, precision, bimanual coordination, and deformable object manipulation. Each task is scored according to a structured rubric based on discrete completion milestones. 

The task scoring criteria are designed to quantify the performance of different robot tasks based on specific completion milestones. Each task has a set of defined actions with corresponding point values. Higher scores are assigned to more complex or functionally successful actions, while partial completions and failed attempts receive lower scores. This structured scoring system allows for consistent evaluation and comparison of task performance. 

#### **Spray Bottle** 

This task evaluates functional grasping and affordance understanding. The robot must grasp a spray bottle and orient it to spray over a target cloth. 

- 0.00: Nothing 

- 0.15: Tries functional grasp but fails 

- 0.25: Grasp bottle 

- 0.75: Grasp bottle, orient over cloth 

- 0.75: Grasp bottle, use functional grasp 

- 1.00: Grasp bottle, use functional grasp, orient over cloth 

#### **Toy Cleanup** 

This task tests long-horizon planning and generalization. The robot must collect scattered toys and deposit them in a designated bin. 

- 0.00: Nothing 

- 0.25: Tries for grasp but fails 

- 0.50: Grasp object 

- 1.00: Grasp object, drop into bin 

#### **Pouring** 

This task assesses precise motion control and transfer learning from the spray bottle task. The robot must pour liquid from a bottle into a container. 

- 0.00: Nothing 

- 0.15: Tries functional grasp but fails 

- 0.25: Grasp bottle 

- 0.75: Grasp bottle, pour into container 

- 0.75: Grasp bottle, use functional grasp 

- 1.00: Grasp bottle, use functional grasp, pour into container 

#### **Bimanual Florist** 

This task evaluates coordinated control of both hands. The robot must pick up a flower, hand it to the other arm, and insert it into a vase. 

- 0.00: Nothing 

- 0.15: Tries grasp but fails 

- 0.25: Grasp the bouquet 



Fig. 9: DexWild-System features a simple and easy-to-use interface for deployment by untrained data collectors. 

- 0.75: Grasp the bouquet, handover 

- 1.00: Grasp the bouquet, handover, insert into vase 

#### **Clothes Folding** 

This task tests manipulation of deformable objects using both hands. The robot must fold a clothing item placed on a surface. 

- 0.00: Nothing 

- 0.25: Tries grasp but fails 

- 0.50: Grasp with one hand 

- 0.75: Grasp with both hands 

- 1.00: Grasp and fold 

#### _B. Data Collection Procedure_ 

To deploy DexWild-System with untrained data collectors, we provide a one-page instruction sheet outlining the task, object setup, and system startup/shutdown. DexWild-System includes three core components: a wrist-tracking camera, a battery-powered mini-PC for onboard data capture, and a custom sensor pod with a motion-capture glove and palmmounted cameras. At a new site, users simply wear the mocap glove and power on the mini-PC with a provided power bank. For egocentric tracking, a headstrap holds the tracking camera; for exocentric tracking, we provide a collapsible tripod. Once booted, users launch our custom desktop app and control recording via a Bluetooth clicker or foot pedal. The UI (Fig. 9) shows sensor status, SLAM recording, and data capture indicators, along with buttons to view the tracking camera feed and delete the last episode. Collectors gather 100 episodes per location. After the day is finished, we upload the data to our remote machine for processing. 

#### _C. Downstream Data Processing_ 

Each episode is stored in its own folder, with subfolders organizing individual actions and observations. SVO recordings from the Zed Mini camera—used for SLAM and wrist pose tracking—are saved separately, with each file covering five episodes. To begin data processing, we use the Zed SDK to decode these SVO files, reconstruct the camera’s motion, 

and perform ArUco cube tracking and wrist pose estimation using both the left image and stereo depth data. We then apply a filtering pipeline to assess tracking quality; episodes are discarded if the wrist pose cannot be reliably tracked for more than 75% of the duration. Next, we compute the action distribution and clip outliers outside the 2nd and 97th percentiles. We smooth the trajectories using interpolation and Gaussian filtering to ensure fluid motion. Hand motions are then retargeted using inverse kinematics in PyBullet, following the method in [41]. The entire pipeline is parallelized using Ray for efficiency. 

#### _D. Behavior Cloning Policy Architecture and Training HyperParameters_ 

Our behavior cloning policy takes as input RGB images and relative state history. We obtain tokens for the image observation via a ViT and tokens for relative states via linear layers. The weights of ViT is initialized from the Soup 1M model from [11]. We decide to include relative states as we found it greatly increases the robustness of the policy, and enables smoother motions. In particular, for bimanual tasks, we find that including the interhand pose (pose of left hand relative to right hand) greatly increases success rate in tasks like Florist We implement both Action Chunking Transformer [59] and Diffusion U-Net [6] as policy classes, which output a sequence of actions. The network outputs actions which consists of relative end effector actions and absolute hand joint angles. 

We list the hyper-paramaters that we used for policy training using behavior-cloning in this Table V 

#### _E. Low Level Motion Control_ 

For optimal smoothness of our policies and safety, we employ a Riemannian Motion Policy (RMP) [34] implemented in Isaac Lab [26], where the RMP dynamically generates jointspace targets given end effector targets. RMP also has the added benefit of incorporating real-time collision avoidance, preventing self-collision between the arms and a set table height. Although our policies does not rely on RMP to prevent collisions, the peace of mind is appreciated. 

#### _F. Comparing Policy Classes_ 

**Does DexWild work with different behavior cloning policy classes?** Table I compares the performance of ACT and Diffusion—across both the In-the-Wild and In-the-Wild Extreme settings. Each policy is evaluated in a robot-only setting and a co-trained (1:2) setting using the DexWild dataset. Notably, Diffusion policies benefit more from DexWild cotraining, achieving the highest scores in all tasks, including substantial improvements on the Pour task where the policy must generalize across tasks. These results suggest that DexWild co-training enables stronger generalization, especially when paired with expressive policy architectures like Diffusion. 

#### _G. Cross Hand Extended Results_ 

**Does DexWild generalize across different robot hands?** Table II reports LEAP Hand performance under both _In the Wild_ and _In the Wild Extreme_ conditions. In every case, DexWild co-training substantially outperforms the robot-only baseline. These results highlight the effectiveness of DexWild in cross embodiment generalization even when using a completely different robot hand. 

#### _H. Scaling Extended Results_ 

**Does DexWild improve as more DexWild data is added?** Table III shows steady gains as we scale from 0% to 100% of the DexWild dataset. Performance increases steadily with more human demonstrations, with a notable jump between 25% and 50% of the dataset. These results demonstrate that DexWild enables scalable learning, where even comparably smaller data scales yields substantial gains, and additional data continues to enhance generalization 

#### _I. Cotraining Extended Results_ 

**How does DexWild react to different cotraining ratios?** Table IV groups all three raw metrics: (a) In-Domain, (b) Inthe-Wild, and (c) In-the-Wild Extreme. All evaluations were run on xArm + LEAP Hand V2 Advanced. 

|**Task**|**Policy Class**|**In the **|**Wild**|**In the Wild **|**Extreme**|
|---|---|---|---|---|---|
|||**Robot Onl**|**y**<br>**1:2**|**Robot Only**|**1:2**|
|S|ACT|0.000|**0.680**|0.115|**0.395**|
|pray|Diffusion|0.050|**0.628**|0.120|**0.520**|
|TCl|ACT|0.458|**0.583**|0.125|**0.458**|
|oy eanup|Diffusion|0.521|**0.875**|0.500|**0.625**|
|PCTk|ACT|0.025|**0.508**|0.000|**0.350**|
|our (ross as)|Diffusion|0.000|**0.958**|0.000|**0.917**|



TABLE I: DexWild Performance on Different Policy Classes 

||**In the Wild**|**In the Wild **|**Extreme**|
|---|---|---|---|
|**Task**|**Robot Only**<br>**1:2**|**Robot Only**|**1:2**|
|Spray|0.305<br>**0.805**|0.150|**0.600**|
|Toy Cleanup|0.500<br>**0.656**|0.250|**0.542**|
|Pour (Cross Task)|0.050<br>**0.917**|0.000|**0.817**|



TABLE II: LEAP Hand Performance on In-the-Wild and Inthe-Wild Extreme Tasks. Ratio is Robot:Human 

|**Scale**|**0%**|**25%**|**50%**|**100%**|
|---|---|---|---|---|
|Spray|0.060|0.260|0.605|0.565|
|Toy Cleanup|0.514|0.442|0.440|0.792|
|**Average**|**0.287**|**0.351**|**0.523**|**0.678**|
|**Std**|**0.321**|**0.129**|**0.116**|**0.160**|



TABLE III: Performance Scaling with DexWild Dataset Size 

|**Task**|**Robot**|**1:1**|**1:2**|**1:5**|**Human**|
|---|---|---|---|---|---|
|Spray|0.690|0.630|0.763|0.381|0.030|
|Toy Cleanup|0.604|0.792|0.833|0.708|0.042|
|**Average**|**0.647**|**0.711**|**0.798**|**0.545**|**0.036**|
|**Std**|**0.061**|**0.114**|**0.050**|**0.232**|**0.008**|



|(a) In Distribution Task Performance|
|---|



|**Task**|**Robot**|**1:1**|**1:2**|**1:5**|**Human**|
|---|---|---|---|---|---|
|Spray|0.050|0.625|0.628|0.393|0.063|
|Toy Cleanup|0.521|0.646|0.875|0.625|0.083|
|**Average**|**0.285**|**0.635**|**0.751**|**0.509**|**0.073**|
|**Std**|**0.333**|**0.015**|**0.175**|**0.164**|**0.015**|



(b) In-the-Wild Task Performance 

|**Task**|**Robot**|**1:2**|
|---|---|---|
|Spray|0.120|0.520|
|Toy Cleanup|0.500|0.625|
|Bimanual Florist|0.063|0.623|
|Bimanual Clothes Folding|0.198|0.740|
|**Average**|**0.220**|**0.627**|
|**Std**|**0.195**|**0.090**|



(c) In-the-Wild Extreme Task Performance 

TABLE IV: Performance Across Cotrain Ratios for Varying Deployment Conditions. Ratio is Robot:Human 

|**Hyperparameter**<br>**Training Coni**|**Value**<br>**figuration**|
|---|---|
|Optimizer|AdamW|
|Base Learning Rate|3e-4|
|Optimizer Momentum|_β_1_, β_2 = 0_._95_,_0_._999|
|Learning Rate Schedule|Cosine (diffusers)|
|Warmup Steps|2000|
|Total Steps|70000|
|Batch Size|256|
|Environment Frequency|30 Hz|
|**Observation **|**Settings**|
|Proprioception Horizon|1 (Spray, Toy, Pour)<br>3 (Florist, Clothes)|
|Image Horizon|1 (all tasks)|
|Observation Resolution|224×224|
|Observation Dim|9 (Spray, Toy, Pour)<br>27 (Florist, Clothes)|
|Action Dimension|26 (Spray, Toy, Pour)<br>52 (Florist, Clothes)|
|Action Chunk Size|48|
|**Action Chunking **|**Transformer**|
|# Encoder Layers|4|
|# Decoder Layers|6|
|# MHSA Heads|8|
|Feed-Forward Dim|3200|
|Hidden Dim (Token Dim)|768|
|Dropout|0.1|
|Feature Norm|LayerNorm|
|**Diffusion U-N**|**et Policy**|
|Train Diffusion Steps|100|
|Eval Diffusion Steps|16|
|Down Channels|[256, 512, 1024]|
|Kernel Size|3|
|Groups (GN)|8|
|Dropout|0.1|
|Feature Norm|None|



TABLE V: Full training and architecture settings used across our experiments. 

