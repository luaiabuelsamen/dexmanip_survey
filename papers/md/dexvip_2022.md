# **DexVIP: Learning Dexterous Grasping with Human Hand Pose Priors from Video** 

**Priyanka Mandikal**<sup>1</sup><sup>_,_2</sup> **and Kristen Grauman**<sup>1</sup><sup>_,_2</sup> 

1Department of Computer Science, The University of Texas at Austin 

2Facebook AI Research 

```
{mandikal,grauman}@cs.utexas.edu
```

**Abstract:** Dexterous multi-fingered robotic hands have a formidable action space, yet their morphological similarity to the human hand holds immense potential to accelerate robot learning. We propose DexVIP, an approach to learn dexterous robotic grasping from human-object interactions present in in-the-wild YouTube videos. We do this by curating grasp images from human-object interaction videos and imposing a prior over the agent’s hand pose when learning to grasp with deep reinforcement learning. A key advantage of our method is that the learned policy is able to leverage free-form in-the-wild visual data. As a result, it can easily scale to new objects, and it sidesteps the standard practice of collecting human demonstrations in a lab—a much more expensive and indirect way to capture human expertise. Through experiments on 27 objects with a 30-DoF simulated robot hand, we demonstrate that DexVIP compares favorably to existing approaches that lack a hand pose prior or rely on specialized tele-operation equipment to obtain human demonstrations, while also being faster to train. Project page with videos: `https://vision. cs.utexas.edu/projects/dexvip-dexterous-grasp-pose-prior` . 

**Keywords:** dexterous manipulation, learning from observations, learning from demonstrations, computer vision 

## **1 Introduction** 

Many objects in everyday environments are made for human hands. Mugs have handles to grasp; the stove has dials to push and turn; a needle has a small hole through which to weave a tiny thread. In order for robots to assist people in human-centric environments, and in order for them to reach new levels of adept manipulation skill, _multi-fingered dexterous robot hands_ are of great interest as a physical embodiment [1, 2, 3, 4, 5, 6, 7]. Unlike common end effectors like parallel jaw grippers or suction cups, a dexterous hand has the potential to execute complex behaviors beyond pushing, pulling, and picking, and to grasp objects with complex geometries in functionally useful ways [8, 9]. 

The flexibility of a dexterous robotic hand, however, comes with significant learning challenges. With articulated joints offering 24 to 30 degrees of freedom (DoF), the action space is formidable. At the same time, interacting with new objects having unfamiliar shapes demands a high level of generalization. Both factors have prompted exciting research in deep reinforcement learning (RL), where an agent dynamically updates its manipulation strategy using closed-loop feedback control with visual sensing while attempting interactions with different objects [2, 5, 7]. 

To mitigate sample complexity—since many exploratory hand pose trajectories will yield no reward— current methods often incorporate imitation learning [1, 2, 3, 4, 10]. With imitation, expert (human) demonstrations provided by teleoperation in virtual reality [11, 12], mocap [1, 13], or kinesthetic manipulation of the robot’s body [14, 15] are used to steer the RL agent towards desirable state-action sequences. Such demonstrations can noticeably accelerate robot learning. 

However, the existing paradigms for human demonstrations have inherent shortcomings. First, they require some degree of specialized setup: a motion glove for the human demonstrator to wear, a virtual reality platform matched to the target robot, a high precision hand and arm tracker, and/or physical access to the robot equipment itself. This in turn restricts demonstrations to lab environments, 

5th Conference on Robot Learning (CoRL 2021), London, UK. 



<!-- Start of picture text -->
Watch Act<br><!-- End of picture text -->

Figure 1: **Main idea** : We learn dexterous grasping by watching human-object interactions in YouTube how-to videos. Using hand poses extracted from a repository of curated human grasp images (left), we train a dexterous robotic agent to learn to grasp objects in simulation (right). The key benefits include improved grasping performance and the ability to quickly scale the method to new objects. 

assumes certain expertise and resources, and entails repeated overhead to add new manipulations or objects. Second, there is an explicit <u>layer of</u> indirection: in conventional methods, a person does not do a task with their own hands, but instead enacts a proxy under the constraints of the hardware/software used to collect the demonstration. For example, in VR, the person needs to watch a screen to judge their success in manipulating a simulated hand and may receive limited or no force feedback [2, 16]. Similarly, advanced visual teleoperation systems that observe the bare hand [13] still separate the person’s hand from the real-world object being manipulated. In a kinesthetic demonstration, the human expert is furthest removed, manually guiding the robot’s end effector, which has a very different embodiment [15, 17]. 

In light of these challenges, we propose to learn dexterous robot grasping policies by watching people interact with objects in video (see Fig. 1). The main idea is to observe people’s hand poses as they use objects in the real world in order to establish a 3D hand pose prior that a robot might attempt to match during functional grasping. Rather than enlist special purpose demonstrations (e.g., record videos at lab tabletops), we turn to in-the-wild Internet videos as the source of the visual prior. Our method automatically extracts human hand poses from video frames using a state-of-the-art computer vision technique. We then define a deep reinforcement learning model that augments a grasp success reward with a reward favoring human-like hand poses upon object contact, while also preferring to grasp the object around affordance regions predicted from an image-based model. In short, by watching video of people performing everyday activities with a variety of objects, our agents learn how to approach objects effectively using their own multi-fingered hand, while also accelerating training. 

Aside from providing accurate policies and faster learning, our approach has several conceptual advantages. First, it removes the indirection discussed above. There is no awkwardness or artificiality of VR, kinesthetic manipulations, etc,; people in the videos are simply interacting with objects in the context of their real activity. This also promotes learning _functional_ grasps—those that prepare the object for subsequent use—as opposed to grasps that simply lift an object in an arbitrary manner. New demonstrations are also easy to curate whenever new objects become of interest, since it is a matter of downloading additional video. In addition, because our visual model focuses on 3D hand pose, it tolerates viewpoint variation and is agnostic to the complex visual surroundings in training data (e.g., variable kitchens, clutter, etc.). Finally, the proposed method requires only visual input from the human data—no state-action sequences. 

We demonstrate our approach trained with frames from YouTube how-to videos to learn grasps for a 30-DoF robot in simulation for a variety of 27 objects. The resulting policy outperforms state-of-theart methods for learning from demonstration and visual affordances [2, 18], while also being 20% more efficient to train. The learned behavior resembles that of natural human-object interactions and offers an encouraging step in the direction of robot learning from in-the-wild Internet data. 

## **2 Related Work** 

**Learning to grasp objects** Early grasping work explicitly reasons about an object’s 3D shape against the gripper [19, 20], whereas learning methods often estimate an object or hand pose followed by model-based planning [21, 8], optionally using supervised learning on visual inputs to predict successful grasps [21, 22, 23, 24, 25]. Most planning methods cater to simple non-dexterous endeffectors like parallel jaw grippers or suction cups that make a control policy easier to codify but need not yield functional grasps. Rather than plan motions to achieve a grasp, reinforcement learning (RL) methods act in a closed loop with sensing, which has the advantage of dynamically adjusting to object conditions [26, 27, 28]. Only limited work explores RL for dexterous manipulation [5, 7, 18]. 

2 

Our work addresses functional dexterous grasping with RL, but unlike the existing methods it primes agent behavior according to videos of people. 

**Imitation and learning from demonstration** To improve sample complexity, imitation learning from expert demonstrations is often used, whether for non-dexterous [29, 30, 31, 32, 33, 15] or dexterous [1, 2, 3, 4] end effectors. Researchers often use demonstrations to explore dexterous manipulation in simulation [2, 3], and recent work shows the promise of sim2real transfer [11, 7]. Like learning from demonstrations (LfD), our approach aims to learn from human experts, but unlike traditional LfD, our method does so without full state-action trajectories, relying instead only on a visual prior for “good" hand states. Furthermore, our use of in-the-wild video as the source of human behavior is new and has all the advantages discussed above. 

**Imitating visual observations** Learning to imitate _observations_ [34] relaxes the requirement of capturing state sequences in demonstrations. This includes ideas for overcoming viewpoint differences between first and third person visual data [33, 30, 31], multi-task datasets to learn correspondences between video of people and kinesthetic trajectories of a robot arm [15], few-shot learning [29, 32], and shaping reward functions with video [33, 35, 15, 31]. However, none of the prior work uses in-the-wild video to learn dexterous grasping as we propose. By connecting real video of humanobject interactions to a dexterous robotic hand, our method capitalizes on both the naturalness of the demonstrations as well as the near-shared embodiment. Furthermore, unlike our approach, the existing (almost exclusively non-dexterous) methods require paired data for the robot and person’s visual state spaces [33, 15, 3], assume the demonstrator and robot share a visual environment (e.g., a lab tabletop) [29, 32, 30, 31, 3], and/or tailor the imitation for a specific object [3]. 

**Visual object affordances** As a dual to hand pose, priors for the object regions that afford an interaction can also influence grasping. Vision methods explore learning affordances from visual data [36, 37, 38], though they stop short of agent action. Visual affordances can successfully influence a pick and place robot [39, 40] and help grasping with simple grippers [9, 21, 23, 24] or a dexterous hand [8, 18]. Object-centric affordances predicted from images also benefit the proposed model, but they are complementary to our novel contribution—the hand-pose prior learned from video. 

**Estimating hand poses** Detecting human hands and their poses is explored using a variety of visual learning methods [41, 42, 43, 44, 45]. Many methods jointly reason about the shape of the object being grasped [43, 9, 46, 47, 46]. Recent work provides large-scale datasets to better understand human hands [48, 49, 50]. We rely on the state-of-the-art FrankMocap method [44] to extract 3D hand poses from video. Our contribution is not a computer vision method to parse pose, but rather a machine learning framework to produce dexterous robot grasping behavior. 

## **3 Approach** 

We consider the task of dexterous grasping with an articulated 30-DoF multi-fingered robotic hand. Our goal is to leverage abundant human interaction videos to provide the robot with a prior over meaningful grasp poses. To this end, we propose DEXVIP, an approach to learn **Dex** terous grasping using **V** ideo **I** nformed **P** ose priors. We first lay out the formulation of the reinforcement learning problem for dexterous grasping (Section 3.1). Then, we describe how we leverage human hand pose priors derived from in-the-wild YouTube videos for this task (Section 3.2). 

### **3.1 Reinforcement Learning Framework for Dexterous Grasping** 

**Background** Our dexterous grasping task is structured as a reinforcement learning (RL) problem, where an agent interacts with the environment according to a policy in order to maximize a specified reward (Fig. 2). At each time step _t_ , the agent observes the current observation _ot_ and samples an action _at_ from its policy _π_ . It then receives a scalar reward _Rt_ +1 and next observation _ot_ +1 from the environment. This feedback loop continues until the episode terminates at _T_ time steps. The goal of the agent is to determine the optimal stochastic policy that maximizes the expected sum of rewards. 

**Observations** Our task setup consists of a robotic hand positioned above a tabletop, with an object of interest resting on the table. At the start of each episode, we sample an object and randomly rotate it from its canonical orientation. The observations _o_<sup>_r_</sup> _t_<sup>(Fig. 2, green block) at each time step</sup><sup>_t_</sup> are a combination of visual and motor inputs to the robot. The visual stream is from an egocentric hand-mounted camera. It consists of an RGB image of the scene _It_<sup>_r_and the corresponding depth map</sup> 

3 



<!-- Start of picture text -->
ot r<br>It r<br> r<br>Dt  r<br>at<br>At r Actor Environment<br>RGB fV Vt<br>Depth<br>Mt<br>Affordance Robot<br>Pose r<br>Pt r Critic pt+1<br>R t+1 Reward<br>fM<br>Proprioception<br>pc*r<br>dt r Ic*h pc*h<br>Hand-Obj  Human  Estimated  Target<br>Distance<br>Grasp Image Human Pose Robot Pose<br>Observations Policy Pose Prior Environment<br><!-- End of picture text -->

Figure 2: **Overview of DEXVIP.** We use grasp poses inferred from Internet video to train a dexterous grasping policy. An actor-critic network (blue) processes sensory observations from visual and motor streams (green) to estimate agent actions. Human hand pose priors derived from how-to videos (red) encourage the <mark>agent to explore worthwhile grasp poses via an auxiliary reward (pur</mark> ple). 

_Dt_<sup>_r_.Additionally, we provide a binary affordance map</sup><sup>_Ar_</sup> _t_<sup>that is inferred from</sup><sup>_I_</sup> 0<sup>_r_using an affordance</sup> prediction network [18] to guide the agent towards functional grasp regions on the object. The motor inputs are a combination of the robot proprioception _Pt_<sup>_r_and the hand-object contact distances</sup><sup>_dr_</sup> _t_<sup>.</sup> _Pt_<sup>_r_comprises of the robot joint angles or pose</sup><sup>_pr_</sup> _t_<sup>and angular velocities</sup><sup>_v_</sup> _t_<sup>_r_of the actuator, while</sup><sup>_dr_</sup> _t_ is the pairwise distance between the object affordance regions and contact points on the hand. The latter assumes the object is tracked in 3D once its affordance region is detected, following [18]. The agent also has 21 touch sensors _T_<sup>_r_</sup> spread uniformly across the palm and fingers. 

**Action space** At each time step _t_ , the policy _π_ processes observations _o_<sup>_r_</sup> _t_<sup>andestimatesactions</sup> _a_<sup>_r_</sup> _t_<sup>—30 continuous joint angle values—which are applied at the joint angles in the actuator.The</sup> robotic manipulator we consider is the Adroit hand [51], a 30-DoF position-controlled dexterous hand. With a five-fingered 24-DoF actuator attached to a 6-DoF arm, the morphology of the robot hand closely resembles that of the human hand. This congruence opens up an exciting avenue to infuse a grasp pose prior learned from human-object interaction videos, as we present later in Sec. 3.2. 

**Feature and policy learning** We adopt an actor-critic model for learning the grasping policy. The visuo-motor observations _o_<sup>_r_</sup> _t_<sup>are processed separately using two neural networks,</sup><sup>_fV_and</sup><sup>_fM_(Fig. 2,</sup> blue block). Specifically, the visual inputs encompassing { _IT_<sup>_r, D_</sup> _T_<sup>_r, A_</sup> _t_<sup>_r_} are concatenated and fed</sup> to a three-layer CNN _fV_ that encodes them to obtain a visual embedding _Vt_ . The motor stream comprised of { _Pt_<sup>_r, dr_</sup> _t_<sup>} is processed by a two-layer fully connected network</sup><sup>_fM_that encodes them to</sup> a motor embedding _Mt_ . Finally _Vt_ and _Mt_ are concatenated and fed to the actor and critic networks to estimate the policy distribution _πθ_ ( _a_<sup>_r_</sup> _t_<sup>_|or_</sup> _t_<sup>) and state values</sup><sup>_Vθ_(</sup><sup>_or_</sup> _t_<sup>), respectively, at each time step.</sup> The resulting policy _π_ outputs a 30-D unit-variance Gaussian whose mean is inferred by the network; we sample from this distribution to obtain the robot’s next action _a_<sup>_r_</sup> _t_<sup>.</sup> 

We train the complete RL network with PPO [52] using a reward that encourages successful grasping, touching object affordance regions, and mimicking human hand poses, as we will detail below. 

**Robot hand simulator** We conduct experiments in MuJoCo [53], a physics simulator commonly used in robotics research. Due to lack of access to a real robotic hand, we perform all experiments in simulation. The successful transfer of dexterous policies trained purely in simulation to the real world [11, 7, 6] supports the value of simulator-based learning in research today. In addition, we conduct numerous experiments with noisy sensing and actuation settings that might occur in the real world to illustrate the robustness of the policy to non-ideal scenarios (see Sec. 4 and Supp.). 

4 



<!-- Start of picture text -->
Human grasp images and poses Robot grasp poses and actions<br>h h h h h h r r<br>Ic* pc* Ici pci Icj pcj pc* aT<br><!-- End of picture text -->

Figure 3: **Human hand pose priors informing the agent action.** Each row shows three example images and extracted human hand poses for each object category (left) and the corresponding consensus robot hand pose rewarded by our method and its application by the agent in action (right). 

### **3.2 Object-Specific Human Hand Pose Priors from Video** 

We now describe how we leverage human-object interaction videos to enable robust dexterous grasping. The morphological similarity between the human hand and the dexterous robot holds immense potential to learn meaningful pose priors for grasping. To facilitate this, we first curate a human-object interaction dataset of video frames to infer 3D grasp hand poses for a variety of objects. We then transfer these poses to the robotic hand using inverse kinematics, and finally develop a novel RL reward that favors human-used poses when learning to grasp. The proposed approach allows us to leverage readily available Internet data to learn robotic grasping. 

**Object dataset** We consider household objects often encountered in daily life activity (and hence online instructional videos) and for which 3D models are available. We acquire 3D object models from multiple public repositories: ContactDB [37], 3DNet [54], YCB [55], Free 3D [56], and 3D Warehouse [57]. We specifically include the 16 ContactDB objects with one-hand grasps used in recent grasping work to facilitate concrete comparisons [18]. We obtain a total of 27 objects to be used for training the robotic grasping policy, all 16 from ContactDB plus 11 additional objects. 

**Video frame dataset** We use the HowTo100M dataset [58] to curate images containing humanobject grasps for the objects of interest. HowTo100M is a large-scale dataset consisting of 13.6 M instructional YouTube videos across categories such as cooking, entertainment, hobbies and crafts, etc. We focus on videos consisting of commonly used household objects—tools and kitchen utensils such as mug, hammer, jug, etc. The idea is to capture objects in active use during natural human interactions so that we can obtain functional hand poses. The grasp images contain the object in its canonical upright position (e.g., pan on stove), which is also the initial vertical orientation of the object on the tabletop in the simulator. Using the above criteria, we curate an object interaction repository _Ih_ of 715 video frames from HowTo100M where the human hand is grasping one of the 27 total objects, to yield on average 26 grasp images per object. For instance, to collect expert data for grasping a _pan_ , we curate grasp images from task ids such as “ _care for nonstick pans_ ”, “ _buy cast iron pans_ ”, etc. While we found it effective to use simple filters based on the weakly labeled categories and specific task ids in HowTo100M, the curation step could be streamlined further by deploying vision methods for detecting hands, actions, and objects in video [48, 59, 58]. 

**Target hand pose acquisition** We propose to use the obtained HowTo100M grasp images _Ih_ to provide a learning signal for robotic grasping. To that end, for each image we first infer its 3D human hand pose _p_<sup>_h_</sup> . In particular, we employ FrankMocap [44] to estimate 3D human hand poses (see Fig. 3, left). FrankMocap is a near real-time method for 3D hand and body pose estimation from monocular video; it returns 3D joint angles for detected hands in each frame. While alternative pose estimation methods could be plugged in here, we use FrankMocap in our implementation due to its efficiency and good empirical performance. We keep right hand detections only, since our robot is one-handed; we leave handling bimanual grasps for future work. 

This step yields a collection of different hand poses per object for a variety of objects found in the videos. Let _P_ ( _c_ ) = _{p_<sup>_h_</sup> _c_ 1<sup>_, . . . , ph_</sup> _cn_<sup>_}_be the set of human hand poses associated with object class</sup><sup>_c_.</sup> The poses within an object class are often quite consistent since the videos naturally portray people 

5 

using the object in its standard functional manner, e.g., gripping a pot handle elicits the same pose for most people. However, some objects elicit a multi-modal distribution of poses (e.g., a knife held with or without an index finger outstretched). See Fig. 3. In order to automatically discover the “consensus" pose for an object, we next apply k-medoid clustering on each set _P_ ( _c_ ). We consider the medoid hand pose of the largest cluster to be the consensus target hand pose _p_<sup>_h_</sup> _c_<sup>_∗_and use its associated</sup> target robot pose _p_<sup>_r_</sup> _c_<sup>_∗_(obtainedusingajointre-targetingmechanismdescribedinSupp.Sec.D)</sup> during policy learning for object _c_ . 

**Video-informed reward function** To exert the video prior’s influence in our RL formulation, we incorporate an auxiliary reward function favoring robot poses similar to the human ones in video. In this way, the reward function not only signals _where_ to grasp a particular object, but also guides the agent on _how_ to grasp effectively. To realize this, we combine three rewards: _Rsucc_ (positive reward when the object is lifted off the table), _Raff_ (negative reward denoting the hand-affordance contact distance obtained from [18], see Supp. Sec. F), and—most notably— _Rpose_ , a positive reward when the agent’s pose _p_<sup>_r_</sup> _t_<sup>matches the target grasp pose</sup><sup>_pr_</sup> _c_<sup>_∗_for that object.Our total reward function is:</sup> 



where _α, β, γ, η_ are scalars weighting the rewards that are set by validation, and _Rentropy_ rewards entropy over the target action distribution to encourage the agent to explore the action space. Through _Raff_ , the agent is incentivized to explore areas of the object within the affordance region, while _Rpose_ encourages the agent to reach hand states that are most suitable for grasping those regions. 

For _Rpose_ , we compute the mean per-joint angle error at time _t_ between the robot joints _pt_<sup>_r_and the</sup> target grasp pose _p_<sup>_r_</sup> _c_<sup>_∗_.We ignore the azimuth and elevation values of the arm in the pose error since</sup> they are specific to the object orientation in _I_<sup>_h_</sup> , which may be different from the robot’s viewpoint _I_<sup>_r_</sup> . This provides more flexibility during object reaching to orient the arm while trying to match the hand pose alone. Furthermore, _Rpose_ is applied only when 30% of the robot’s touch sensors are activated. This encourages the robot to assume the target hand pose once it is close to the object and in contact with it. Following [18], _Raff_ is computed as the Chamfer distance between points on the hand and points on the inferred object affordance region. See Supp. Sec. B for reward function details. 

The proposed approach permits imitation by visual observation of the human how-to videos, yet without requiring access to the state-action trajectories of the human activity. Its mode of supervision is therefore much lighter than that of conventional teleoperation or kinesthetic teaching, as we will see in results. Furthermore, because our model can incorporate priors for new objects by obtaining new training images, it scales well to add novel objects. 

## **4 Experiments** 

We present experiments to validate the impact of learning pose priors from video and to gauge DEXVIP’s performance relative to existing methods and baselines. 

**Compared methods** We compare to the following methods: ( **1** ) COM: uses the center of mass of the object as a grasp location prior, since this location can lead to stable grasps [60]. We implement this by penalizing the hand-CoM distance for _Raff_ in Eqn 1, and removing _Rpose_ . ( **2** ) TOUCH: uses only the touch sensors _T_<sup>_r_</sup> on the hand to positively reward the agent +1 for object interaction when 30% of them are activated, but imposes no supervision on the hand pose. ( **3** ) GRAFF [18]: a state-of-the-art RL grasping model that trains a policy to grasp objects at inferred object-centric affordance regions. Unlike our method, GRAFF does not enforce any prior over the agent’s hand pose. All the above three RL methods use the same architecture as our model for the grasping policy, allowing for a fair comparison. ( **4** ) DAPG [2]: is a hybrid imitation+RL model that uses motion-glove demonstrations collected from a human expert in VR. It is trained with object-specific mocap demonstrations collected by [18] for grasping ContactDB object (25 demos per object). For objects beyond ones in ContactDB, we use demos from the object most similar in shape in ContactDB. 

**Metrics** We report four metrics: ( **1)** Grasp Success: when the object is lifted off the table by the hand for at least the last 50 time steps (a quarter of the episode length) to allow time to reach the object and pick it up. ( **2)** Grasp Stability: the firmness with which the object is held by the robot, discounting grasps in which the object can easily be dropped. We apply perturbation forces of 1 Newton in six orthogonal directions on the object after an episode completes. If the object continues to be grasped 

6 



Figure 5: **Grasping success and learning speed.** Left: The proposed model outperforms all the baselines, including recent methods for learning from demonstrations (DAPG [2]) or favoring visual affordance regions (GRAFF [18]). Relative results remain stable under noisy sensing and actuation (shaded bars). Right: Our model trains faster than the others, showing that the Internet videos of people help kickstart learning even before the agent begins attempting its own grasps. 

by the agent, the grasp is deemed stable. ( **3)** Functionality: the percentage of successful grasps in which the hand lies close to the GT affordance region. This metric evaluates the utility of the grasp for post-grasp functional use. ( **4)** Posture: the distance between the target human hand pose _p_<sup>_h_</sup> _c∗_<sup>and</sup> the agent hand pose after a successful grasp _p_<sup>_r_</sup> _T_<sup>.It tells us how human-like the learned grasps are.</sup> We normalize all metrics on a [0 _,_ 100%] scale, where higher is better. We evaluate 100 episodes per object with the objects placed at different initial orientations ranging from [0,180<sup>_◦_</sup> ]. We report the mean and standard deviation of the metrics across all models trained with four random seeds. 

**Implementation details** The visual encoder _fV_ has filters of size [8,4,3], and a bottleneck 512-D and uses ReLU activations. The motor encoder _fM_ has dimensions [512,512]. For the hand-object contacts, we use 10 and 20 uniformly sampled points on the hand and affordance region, respectively, following [18]. The entire network is optimized using Adam with a learning rate of 5 _e −_ 5. A single grasping policy is trained on all the curated objects for 150M agent steps with an episode length of 200 time steps. The coefficients in the reward function (Eq. 1) are set as: _α_ = 1 _, β_ = 1 _, γ_ = 1 _, η_ = 0 _._ 001. We train for four random seed initializations. Further details are provided in Supp. Sec. E.1. 

**Grasping policy performance** We take the policy trained on all 27 objects and first evaluate it on the 16 objects from ContactDB [37]. Since these objects have ground truth affordances (used when training GRAFF and our model) and mocap demonstrations (used when training DAPG), they represent the best case scenario for the existing models to train with clean expert data. Note that our method always uses hand poses inferred from YouTube videos, even for the ContactDB objects. 

Fig 5 (left) shows the results. DEXVIP consistently outperforms all the methods on all metrics. The grasp success and stability rates experience a significant boost even compared to GRAFF [18], which utilizes object affordances but does not enforce any constraints on the hand pose. The Functionality values are similar as both the methods encourage the agent to grasp the object at the affordance regions. Our method also scores well on the Posture metric, indicating that the learned policies indeed demonstrate human-like behavior during grasping. See Supp. Sec. G and Sec. E.2 for additional results and Sec. C for TSNE plots illustrating our model’s human-like poses. 

Fig. 4 shows grasp policies from sample episodes. We can see that DEXVIP is able to grasp objects with a human-like natural posture compared to the other methods. Contrast this with COM or GRAFF, which only uses object affordances: those agents often end up in un- 

<mark>pan              mug            teapot          knife              cup           hammer</mark> 



<!-- Start of picture text -->
CoM<br>Touch<br>DAPG<br>GRAFF<br>DexVIP<br><!-- End of picture text -->



















































Figure 4: **Grasping performance.** Example frames for the grasping task. Our DEXVIP policy guided by pose-priors is able to successfully grasp objects in natural human-like poses, while the other methods may either generate unusual poses or fail to grasp effectively. Please see Supp. video. 

7 

usual poses which reduce their applicability to post-grasp functional tasks using the object. Failure cases arise when some objects are in orientations not amenable to the target hand pose. For instance, a knife with the handle on the left would ideally be picked up differently and then re-oriented for use. 

**Training speed** Fig. 5 (right) shows the training curves. Our method learns successful policies 20% faster than the next best method, GRAFF [18]. This underscores how the hand pose priors enable our agent to approach objects in easily graspable configurations, thus improving sample efficiency. 

**Expert data: teleoperation vs. YouTube video** Compared to traditional demonstrations, a key advantage of our video-based approach is the ease of data collection and scalability to new objects. We analyze the time taken to collect demonstrations for DAPG [2] versus the time taken to curate videos for DEXVIP. On average, it takes 5 minutes to collect a single demonstration for DAPG owing to the complex setup, while a video or image for DEXVIP is collected in a few seconds. Fig. 6 quantifies the impact of the efficiency of human demonstrations for our model (trained with video frames) compared to traditional state-action demonstrations (trained with VR demos). Plotting success rates as a function of accumulated demo experience, we see how quickly the proposed imagebased supervision translates to grasping success on an increasing number of new objects, whereas with traditional demonstrations reaching peak performance takes much longer. This highlights the significant gains that can be realized by shifting from tele-op to video supervision for robot learning. 



This efficiency also means new objects are quick to add. To illustrate, we further evaluate DEXVIP and DAPG on all 11 non-ContactDB objects, for which mocap demonstrations are not available. DAPG’s success rate drops from 59% to 50%—a 15% relative drop in performance—while DEXVIP experiences a marginal 4% drop from 68% to 65%, remaining comparable to its performance on ContactDB. Since DAPG is trained on sub-optimal demonstrations, this precludes it from generalizing well to objects for which expert data is absent. DEXVIP, on the other hand, is able to benefit from easily available Internet images to scale up supervision. 

Figure 6: **Demo-time vs success rate.** DexVIP benefits from easily available Internet data to scale up supervision. 

**Ablations** Next we investigate how different compoDexVIP benefits from easily available Innents of the reward influence the dexterous grasping ternet data to scale up supervision. policy. Using only _Raff_ , the success rate is 60% on ContactDB. When we successively add touch and hand pose priors to the reward function (Eq. 1), we obtain success rates of 63% and 68% respectively. Thus our full model is the most effective. 

**Noisy sensing and actuation** Finally, to mimic non-ideal real-world scenarios, we induce multiple sources of noise into our agent’s sensory and actuation modules during training and testing following prior work [11, 7, 6, 18]. These include Gaussian noise on the robot’s proprioception _Pt_<sup>_r_,object</sup> tracking _d_<sup>_r_</sup> _t_<sup>, and actuation</sup><sup>_ar_</sup> _t_<sup>, as well as pixel perturbations on the image observations</sup><sup>_I_</sup> _t_<sup>_r_.Under</sup> heavy noise, DEXVIP still yields a grasp success rate of 64%, even outperforming noise-free models of the other methods (Fig. 5, shaded bars). This encouraging result in a noise-induced simulation environment lends support for potentially transferring the learned policies to the real world [6, 7, 61] were we to gain access to a dexterous robot. Please see Supp. Sec. A for more details. 

## **5 Conclusion** 

We proposed an approach to learn dexterous robotic grasping from human hand pose priors derived from video. By leveraging human-object interactions in YouTube videos, we showed that our dexterous grasping policies outperformed methods that did not have access to these priors, including two state-of-the-art models for RL-based grasping. Key advantages of our approach are 1) humans are observed directly doing real object interactions, without the interference of conventional demonstration tools; and 2) expert information from video sources scales well with new objects. This is an encouraging step towards training robotic manipulation agents from weakly supervised and easily scalable in-the-wild expert data available on the Internet. In the future, we are interested in expanding the repertoire of tasks beyond grasping to learn fine-grained manipulation skills from human interaction videos. 

8 

### **Acknowledgments** 

UT Austin is supported by DARPA L2M, the IFML NSF AI Institute, and NSF IIS -1514118. K.G. is paid as a research scientist at Facebook AI Research. We would like to thank the reviewers for their valuable feedback. 

## **References** 

- [1] A. Gupta, C. Eppner, S. Levine, and P. Abbeel. Learning dexterous manipulation for a soft robotic hand from human demonstrations. In _International Conference on Intelligent Robots and Systems (IROS)_ , 2016. 

- [2] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _Robotics: Science and Systems (RSS)_ , 2018. 

- [3] D. Jain, A. Li, S. Singhal, A. Rajeswaran, V. Kumar, and E. Todorov. Learning deep visuomotor policies for dexterous hand manipulation. In _International Conference on Robotics and Automation (ICRA)_ , 2019. 

- [4] H. Zhu, A. Gupta, A. Rajeswaran, S. Levine, and V. Kumar. Dexterous manipulation with deep reinforcement learning: Efficient, general, and low-cost. In _International Conference on Robotics and Automation (ICRA)_ , 2019. 

- [5] A. Nagabandi, K. Konoglie, S. Levine, and V. Kumar. Deep dynamics models for learning dexterous manipulation. _Conference on Robot Learning (CoRL)_ , 2019. 

- [6] I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 

- [7] OpenAI, M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 2020. 

- [8] S. Brahmbhatt, A. Handa, J. Hays, and D. Fox. ContactGrasp: Functional multi-finger grasp synthesis from contact. _IROS_ , 2019. 

- [9] M. Kokic, D. Kragic, and J. Bohg. Learning task-oriented grasping from human activity datasets. _IEEE Robotics and Automation Letters_ , 2020. 

- [10] I. Radosavovic, X. Wang, L. Pinto, and J. Malik. State-only imitation learning for dexterous manipulation. _arXiv:2004.04650v1_ , 2020. 

- [11] Y. Zhu, Z. Wang, J. Merel, A. Rusu, T. Erez, S. Cabi, S. Tunyasuvunakool, J. Kramár, R. Hadsell, N. de Freitas, et al. Reinforcement and imitation learning for diverse visuomotor skills. _arXiv preprint arXiv:1802.09564_ , 2018. 

- [12] A. Nair, B. McGrew, M. Andrychowicz, W. Zaremba, and P. Abbeel. Overcoming exploration in reinforcement learning with demonstrations. _arXiv:1709.10089_ , 2017. 

- [13] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox. Dexpilot: Vision based teleoperation of dexterous robotic hand-arm system. _ICRA_ , 2020. 

- [14] M. Vecerik, T. Hester, J. Scholz, F. Wang, O. Pietquin, B. Piot, N. Heess, T. Rothorl, T. Lampe, and M. Riedmiller. Leveraging demonstrations for deep reinforcement learning on robotics problems with sparse rewards. _arXiv:1707.08817_ , 2018. 

- [15] P. Sharma, L. Mohan, L. Pinto, and A. Gupta. Multiple interactions made easy (mime): Large scale demonstrations data for imitation. In _Conference on Robot Learning (CoRL)_ , 2018. 

- [16] V. Kumar and E. Todorov. Mujoco haptix: A virtual reality system for hand manipulation. In _IEEE-RAS 15th International Conference on Humanoid Robots (Humanoids)_ , 2015. 

- [17] P. Sharma, D. Pathak, and A. Gupta. Third-person visual imitation learning via decoupled hierarchical controller. In _NeurIPS_ , 2019. 

- [18] P. Mandikal and K. Grauman. Dexterous robotic grasping with object-centric visual affordances. In _arXiv preprint arXiv:2009.01439_ , 2020. 

- [19] M. Ciocarlie, C. Goldfeder, and P. Allen. Dimensionality reduction for hand-independent dexterous robotic grasping. In _IROS_ , 2007. 

- [20] A. Bicchi and V. Kumar. Robotic grasping and contact: A review. In _IEEE International Conference on Robotics and Automation_ , 2000. 

- [21] S. Levine, P. Pastor, A. Krizhevsky, J. Ibarz, and D. Quillen. Learning hand-eye coordination for robotic grasping with deep learning and large-scale data collection. _IJRR_ , 2018. 

- [22] C. Wu, J. Chen, Q. Cao, J. Zhang, Y. Tai, L. Sun, and K. Jia. Grasp proposal networks: An end-to-end solution for visual learning of robotic grasps. In _NeurIPS_ , 2020. 

- [23] I. Lenz, H. Lee, and A. Saxena. Deep learning for detecting robotic grasps. _The International Journal of Robotics Research_ , 2015. 

- [24] J. Redmon and A. Angelova. Real-time grasp detection using convolutional neural networks. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2015. 

- [25] J. Mahler, J. Liang, S. Niyaz, M. Laskey, R. Doan, X. Liu, J. A. Ojea, and K. Goldberg. Dex-net 2.0: Deep learning to plan robust grasps with synthetic point clouds and analytic grasp metrics. 2017. 

9 

- [26] D. Kalashnikov, A. Irpan, P. Pastor, J. Ibarz, A. Herzog, E. Jang, D. Quillen, E. Holly, M. Kalakrishnan, V. Vanhoucke, et al. Qt-opt: Scalable deep reinforcement learning for vision-based robotic manipulation. _Conference on Robot Learning (CoRL)_ , 2018. 

- [27] D. Quillen, E. Jang, O. Nachum, C. Finn, J. Ibarz, and S. Levine. Deep reinforcement learning for vision-based robotic grasping: A simulated comparative evaluation of off-policy methods. In _2018 IEEE International Conference on Robotics and Automation (ICRA)_ , 2018. 

- [28] H. Merzi´c, M. Bogdanovi´c, D. Kappler, L. Righetti, and J. Bohg. Leveraging contact forces for learning to grasp. In _International Conference on Robotics and Automation (ICRA)_ , 2019. 

- [29] C. Finn, T. Yu, T. Zhang, P. Abbeel, and S. Levine. One-shot visual imitation learning via meta-learning. In _Conference on Robot Learning (CoRL)_ , 2017. 

- [30] B. Stadie, P. Abbeel, and I. Sutskever. Third-person imitation learning. In _ICLR_ , 2017. 

- [31] Y. Liu, A. Gupta, P. Abbeel, and S. Levine. Imitation from observation: Learning to imitate behaviors from raw video via context translation. In _ICRA_ , 2018. 

- [32] D. Pathak, P. Mahmoudieh, G. Luo, P. Agrawal, D. Chen, Y. Shentu, E. Shelhamer, J. Malik, A. A. Efros, and T. Darrell. Zero-shot visual imitation. In _ICLR_ , 2018. 

- [33] P. Sermanet, C. Lynch, Y. Chebotar, J. Hsu, E. Jang, S. Schaal, and S. Levine. Time-contrastive networks: self-supervised learning from video. In _ICRA_ , 2018. 

- [34] F. Torabi, G. Warnell, and P. Stone. Recent advances in imitation learning from observation. In _IJCAI_ , 2019. 

- [35] W. Goo and S. Niekum. One-shot learning of multi-step tasks from observation via activity localization in auxiliary video. In _ICRA_ , 2019. 

- [36] T.-T. Do, A. Nguyen, D. G. C. Ian Reid, and N. G. Tsagarakis. Affordancenet: An end-to-end deep learning approach for object affordance detection. In _ICRA_ , 2017. 

- [37] S. Brahmbhatt, C. Ham, C. C. Kemp, and J. Hays. Contactdb: Analyzing and predicting grasp contact via thermal imaging. In _IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2019. 

- [38] T. Nagarajan, C. Feichtenhofer, and K. Grauman. Grounded human-object interaction hotspots from video. In _Proceedings of the IEEE International Conference on Computer Vision_ , 2019. 

- [39] H. Wu, Z. Zhang, H. Cheng, K. Yang, J. Liu, and Z. Guo. Learning affordance space in physical world for vision-based robotic object manipulation. In _International Conference on Robotics and Automation (ICRA)_ , 2020. 

- [40] L. Yen-Chen, A. Zeng, S. Song, P. Isola, and T.-Y. Lin. Learning to see before learning to act: Visual pre-training for manipulation. In _IEEE ICRA_ , 2020. 

- [41] M. Cai, K. M. Kitani, and Y. Sato. Understanding hand-object manipulation with grasp types and object attributes. In _Conference on Robotics Science and Systems (RSS)_ , 2016. 

- [42] Y. Zhang, V. N. Boddeti, and K. Kitani. Gesture-based bootstrapping for egocentric hand segmentation. _arXiv:1612.02889_ , 2018. 

- [43] Y. Hasson, G. Varol, D. Tzionas, I. Kalevatykh, M. J. Black, I. Laptev, and C. Schmid. Learning joint reconstruction of hands and manipulated objects. In _CVPR_ , 2019. 

- [44] Y. Rong, T. Shiratori, and H. Joo. Frankmocap: Fast monocular 3d hand and body motion capture by regression and integration. _arXiv preprint arXiv:2008.08324_ , 2020. 

- [45] Y. Zhou, M. Habermann, W. Xu, I. Habibie, C. Theobalt, and F. Xu. Monocular realtime hand shape and motion capture using multi-modal data. In _CVPR_ , 2020. 

- [46] Y.-W. Chao, W. Yang, Y. Xiang, P. Molchanov, A. Handa, J. Tremblay, Y. S. Narang, K. Van Wyk, U. Iqbal, S. Birchfield, J. Kautz, and D. Fox. DexYCB: A benchmark for capturing hand grasping of objects. In _IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2021. 

- [47] Z. Cao, I. Radosavovic, A. Kanazawa, and J. Malik. Reconstructing hand-object interactions in the wild. _arXiv:2012.09856v1_ , 2020. 

- [48] D. Shan, J. Geng, M. Shu, and D. Fouhey. Understanding human hands in contact at internet scale. In _CVPR_ , 2020. 

- [49] S. Brahmbhatt, C. Tang, C. D. Twigg, C. C. Kemp, and J. Hays. ContactPose: A dataset of grasps with object contact and hand pose. In _The European Conference on Computer Vision (ECCV)_ , 2020. 

- [50] O. Taheri, N. Ghorbani, M. Black, and D. Tzionas. Grab: A dataset of whole-body human grasping of objects. In _ECCV_ , 2020. 

- [51] V. Kumar, Z. Xu, and E. Todorov. Fast, strong and compliant pneumatic actuation for dexterous tendondriven hands. In _IEEE international conference on robotics and automation_ , 2013. 

- [52] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 

- [53] E. Todorov, T. Erez, and Y. Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , 2012. 

- [54] W. Wohlkinger, A. Aldoma Buchaca, R. Rusu, and M. Vincze. 3DNet: Large-Scale Object Class Recognition from CAD Models. In _International Conference on Robotics and Automation (ICRA)_ , 2012. 

- [55] B. Calli, A. Singh, J. Bruce, A. Walsman, K. Konolige, S. Srinivasa, P. Abbeel, and A. M. Dollar. Yale-cmu-berkeley dataset for robotic manipulation research. _IJRR_ , 2017. 

- [56] www.free3d.com. 

- [57] www.3dwarehouse.sketchup.com. 

10 

- [58] A. Miech, D. Zhukov, J.-B. Alayrac, M. Tapaswi, I. Laptev, and J. Sivic. HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips. In _ICCV_ , 2019. 

- [59] P. Bojanowski, R. Lajugie, F. Bach, I. Laptev, J. Ponce, C. Schmid, and J. Sivic. Weakly supervised action labeling in videos under ordering constraints. In _ECCV_ , 2014. 

- [60] D. Kanoulas, J. Lee, D. G. Caldwell, and N. G. Tsagarakis. Center-of-mass-based grasp pose adaptation using 3d range and force/torque sensing. _International Journal of Humanoid Robotics_ , 2018. 

- [61] J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. In _IROS_ , 2017. 

11 

# **Supplementary Material** 

_Note: Please see the supplementary video on the project page for example episodes:_ _`https: // vision. cs. utexas. edu/ projects/ dexvip-dexterous-grasp-pose-prior` ._ 

## **A Noisy sensing and actuation** 

We are so far unable to deploy our system on a real robot, since we lack access to a dexterous hand robot. Instead, we provide experiments with a popular realistic simulator and further stress-test our approach with noisy sensing and actuation. Those results appear in the main paper; here we elaborate on the noise models. 

Robots can encounter a number of non-ideal scenarios when executing policies in the real world. The ever changing nature of the real world coupled with faults in hardware systems can pose a daunting challenge to real world deployment. These discrepancies often occur in the form of sensing and actuation failures. Sources for noise include variations in sensory systems such as perception modules as well as fluctuations in actuation control. Before robots can successfully be deployed into the real world, they must be capable of handling such variations. 

In Section 4 of the main paper, we describe the setup for inducing noise into our agent’s sensory and actuation modules during training and testing following prior work [11, 7, 6, 18]. Here, we further describe each of the noise sources in detail. 

1. Proprioceptive noise: We apply additive Gaussian noise of mean 0 and standard deviation 0 _._ 01 on the robot’s joint angles and angular velocities. This simulates the sensing and signal failures that can arise in the system. Thus training with such an induced noise source improves the likelihood of the robot being more robust to hardware failures during actuation. 

2. Actuation noise: Similar to the proprioceptive noise, we apply additive Gaussian noise on the robot actuation values. Such a noise model accounts for fluctuations in actuation control experienced in real-world deployment. 

3. Perception noise: For each RGB image _It_<sup>_r_thatisprocessedbythevisionmodule</sup><sup>_f_</sup> _V_<sup>,weapply</sup> pixel perturbations in the range [ _−_ 5 _,_ 5] and clip all pixel values between [0 _,_ 255]. This more closely resembles noise arising during camera sensing [11]. 

4. Tracking noise: The object tracking points are operated on by a Gaussian noise model of mean 0 and standard deviation 1 cm. Additionally, we also freeze these tracking points for 20 frames at random intervals to further challenge our system. This simulates the effect of tracking failures arising from momentary occlusions of the object during interaction. 

As can be seen in Fig. 5 (left) of the main paper, even under substantial noise, our proposed method DEXVIP still yields a high grasp success rate comparable to its performance under noise-free conditions, and even outperforms noise-free models of the other methods. This demonstrates the robustness of the trained policy to non-ideal realistic conditions. Since our lab does not have access to a real robot, we perform all our experiments in simulation. However, using the noise-induction techniques described above, we are able to test our method for real-world compliance under realistic conditions. 

Some areas that could still vary between simulation and the real world can include friction coefficients, damping factors, and so forth, which could further be accounted for using automatic domain randomization techniques as in [6]. Despite the lack of access to a real robot, the encouraging performance of DEXVIP in a noise-induced simulation environment lends support for potentially transferring the learned policies to the real world [6, 7, 61] were we to gain access to a robot. 

## **B Reward function details** 

We describe the various components of the reward function in Eq.1 of the main paper in more detail. 

1. _Rsucc_ : This is a positive reward determining if the object has been grasped by the agent. At a particular time step _t_ , if there is contact established between the hand and the object and no contact between the object and the table, the agent gets a +1 reward for that time step. This ensures that scenarios where the object is resting on the table as well those in which the object is in the air but out of the agent’s reach do not get counted as grasp successes. 

2. _Raff_ : This is a negative reward denoting the hand-affordance contact distance between points on the hand and object affordance regions. Following [18], we compute _Raff_ as the negative of the Chamfer 

12 

distance between _M_ points on the hand and _N_ points on the object. It is defined as follows: 



We set _M_ = 10 and _N_ = 20 in our experiments, following [18]. In essence, the agent experiences a higher penalty if it is away from the object affordance region, which drops to 0 as it gets closer. This encourages the agent to explore useful object regions during exploration. 

3. _Rpose_ : As discussed in the main paper, _Rpose_ is a mean per-joint angle error applied on the robot joint angles _p_<sup>_r_</sup> _t_<sup>upon making contact with the object,so that it matches the human expert pose</sup><sup>_p_</sup> _c_<sup>_∗_.</sup> We ignore the azimuth and elevation values of the arm in the pose error since they are specific to the object orientation in _I_<sup>_h_</sup> , which may be different from the robot’s viewpoint _I_<sup>_r_</sup> . This joint error is also hierarchically weighted over the joint angles such that errors on the parent joints are more heavily penalized compared to those on the child joints. This encourages the agent to align parent joints first before aligning their children and thus adopts a global to local approach for pose matching. _Rpose_ is therefore defined as follows: 



Here, _j_ spans all five fingers of the hand and _li_<sup>_j_is the error between joint</sup><sup>_i_of the</sup><sup>_jth_finger of the robot</sup> pose _p_<sup>_r_</sup> _t_<sup>and target robot pose</sup><sup>_p_</sup> _c_<sup>_r∗_.In our experiments, we set</sup><sup>_γ_1= 1</sup><sup>_._0</sup><sup>_, γ_2= 0</sup><sup>_._75</sup><sup>_, γ_3= 0</sup><sup>_._5</sup><sup>_, γ_4=</sup> 0 _._ 25. In this way, we can have the poses align faster starting from the root joint. _Rpose_ is a negative reward that penalizes the agent for having poses that are distant from the human pose _pc_<sup>_∗_.Furthermore,</sup> _Rpose_ is applied only when 30% of the robot’s touch sensors _T_<sup>_r_</sup> are activated. This encourages the robot to assume the target hand pose once it is close to the object and in contact with it. 

4. _Rentropy_ : This reward is used while training the PPO agent so as to encourage exploration of the action space. This is implemented by maximizing the entropy over the target action distribution. 

## **C TSNE on hand poses** 

We perform a TSNE analysis on all the human hand poses _p_<sup>_h_</sup> _∈P_<sup>_h_</sup> in our curated YouTube dataset and the hand poses of our trained grasping agent in Fig. A. We observe a meaningful distribution across object morphologies (e.g. clenched fist – mug, pan, teapot, vs. loose fist – apple, mouse). This behavior is also reflected in the trained DEXVIP agent for which we analyze the robot’s pose at the last time step, _p_<sup>_r_</sup> _T_<sup>of all successful grasps.The</sup> distribution for DEXVIP is also more clustered since it uses the cluster center per object category _pc_<sup>_∗_as the</sup> target pose during training. This shows that the proposed approach of injecting human hand pose priors derived from in-the-wild object interaction videos can successfully guide dexterous robotic agents. 

## **D Hand pose retargeting from FrankMocap to Adroit** 

To use the human pose inferred from FrankMocap in our simulator, we need to re-target the pose from FrankMocap to Adroit. Although both the human hand and the robot hand share a common five-finger morphology, their joint hierarchy trees are different. Fig. B.i shows the two kinematic chains. We briefly describe each morphology below: 

- **FrankMocap** : It uses the hand model from SMPL-X [4] to represent the human hand pose inferred from video frames. It consists of three ball joints in each of the five fingers, each having 3 DoF. This yields 15 ball joints in total with 45 DoF. Additionally, the root joint at the base of the hand _j_ 0<sup>_h_has 6</sup> DoF. The joint space of the human hand in 3D is thus represented as **_J_**<sup>_h_</sup> _∈_ R<sup>21</sup><sup>_×_3</sup> — a wrist, 15 finger joints, and 5 finger tips. Note that the finger tips are not joint locations, but are used for computing joint angles for their parent joints 

- **Adroit** : The Adroit hand in the simulator is actuated by 24 revolute joints having 1 DoF each, resulting in 24 DoF in total. The hand is attached to a 6 DoF robotic arm, yielding 30 DoF in total. The joint space of the robot hand is thus represented by **_J_**<sup>_r_</sup> _∈_ R<sup>30</sup> . 

As we can see, the FrankMocap model has many more degrees of freedom compared to the Adroit hand. Keeping these differences in mind, we design a joint retargeting mechanism to bridge the gap between the FrankMocap and Adroit models and effectively use the human pose to train the robot. 

The hand pose retargeting mechanism is depicted in Fig. B.ii. The different stages of this retargeting pipeline are as follows: 

13 



Figure A: **TSNE over hand poses.** A good distribution of human and robot poses across morphologies is observed (e.g. clenched fist - mug, pan, teapot vs. loose fist - apple, mouse). 

- **a) Hand pose in world coordinates** : We infer the FrankMocap pose from the input video frame _I_<sup>_h_</sup> and obtain the human hand pose _p_<sup>_h_</sup> _∈_ **_J_**<sup>_h_</sup> _w_<sup>as a set of 3D joint key-points in world coordinates.</sup> 

- **b) World to root relative** : We convert raw X, Y, Z positions of the joints in world coordinates to root-relative coordinates by shifting the origin to the wrist joint _j_ 0<sup>_h_to obtain</sup><sup>_ph_</sup> _rr_<sup>in root relative pose</sup> **_J_**<sup>_h_</sup> _rr_<sup>_∈_R21</sup><sup>_×_3.To determine the orientation of the Adroit arm, we first construct a plane through the</sup> wrist _j_ 0<sup>_h_, fore finger knuckle</sup><sup>_j_</sup> 4<sup>_h_and ring finger knuckle</sup><sup>_j_</sup> 10<sup>_h_.The palm is taken to lie in this plane.The</sup> palmar plane along with its normal defines the orientation of the arm. The axis angles obtained during this transformation are used to set the rotational joints of the Adroit arm in **_J_**<sup>_r_</sup> _∈_ R<sup>30</sup> . 

- **c) Root relative to parent relative** : A sequential rotational transform is applied about X, Y and Z axes, with the angular changes _α_ , _β_ and _γ_ respectively, on the joint positions in the Root Relative Coordinate System to get the corresponding skeleton in Parent Relative Coordinate System. These angular changes are computed such that the Z-axis lies along the child joint and the Y-axis points outward at every finger joint. At every level of the joint hierarchy, coordinate transformations of the parent are applied to the child joints so that after successively parsing through the entire tree, the root relative coordinates _p_<sup>_h_</sup> _rr_<sup>are transformed into a parent-relative coordinate frame</sup><sup>_ph_</sup> _pr_<sup>in</sup><sup>**_J_**</sup><sup>_h_</sup> _pr_<sup>_∈_R21</sup><sup>_×_3.</sup> Here every joint _ji_ is expressed relative to a coordinate frame defined at its parent joint _P_ ( _ji_ ). 

- **d) Joint angle transfer** : The polar coordinates (azimuth and elevations) computed in the parent relative system yield local joint angles that are mapped onto the revolute joints in the Adroit space **_J_**<sup>_r_</sup> _∈_ R<sup>30</sup> . Most revolute joints in Adroit can be mapped from the azimuth or elevation values of different joints in _p_<sup>_h_</sup> _pr_<sup>.As an example, consider the middle joint on the fore finger in Adroit i.e.</sup><sup>_j_</sup> 9<sup>_r_in Fig.B.i.This</sup> joint angle can be obtained by computing the elevation of _j_ 6<sup>_h_with respect to the coordinate frame</sup> defined at its parent joint _j_ 5<sup>_h_in FrankMocap, while ignoring the azimuth and tilt angles.Other joints</sup> can similarly be obtained from the joint definitions in _p_<sup>_h_</sup> _pr_<sup>.For the little finger metacarpel</sup><sup>_j_</sup> 19<sup>_r_which is</sup> not modelled in FrankMocap, we set it to be 0.25 of the elevation at _j_ 13<sup>_h_.</sup> 

Using the above re-targeting scheme, we are able to successfully transfer the FrankMocap pose from the human pose space to the Adroit pose space. Samples can be seen in Fig. 3, main paper. While the mapping is approximate—due to the inherent differences in kinematic chains as discussed above—we find that this re-targeting mechanism generates Adroit poses that closely match the human pose and works well for our purpose. 

14 



<!-- Start of picture text -->
f2 Frankmocap hand 10 14 18 Adroit hand<br>f1 f3 23<br>6 9 12 51 DoF 9 13 17 22 30 DoF<br>8 f4<br>5 11 15 15 Joints + Root + 5 Finger tips 7,8 11,115, 20,21 24 Joints + Arm<br>4 7 10 14 TH   - 3xBall - 9 DoF 6 2 16 TH    - 5xRevolute - 5 DoF<br>f0 3 13 FF    - 3xBall - 9 DoFMF   - 3xBall - 9 DoF 4,52,3 19 FF     - 4xRevolute - 4 DoFMF    - 4xRevolute - 4 DoF<br>2 RF    - 3xBall - 9 DoF 1 RF     - 4xRevolute - 4 DoF<br>LF     - 5xRevolute - 5 DoF<br>1 LF    - 3xBall - 9 DoF<br>Wrist - 2xRevolute - 2 DoF<br>0 Root - 1xFree - 6 DoF<br>0 Arm   - 1xFree        - 6 DoF<br>TH=Thumb, FF = Fore finger, MF = Middle finger, RF = Ring finger, LF = Little finger<br>i)  Kinematic chain for FrankMocap (left) and Adroit (right)<br>a) 3D Joints in  b) Root Relative  c) Parent Relative  d) Joint Angles<br>World Frame Frame Frame in Adroit<br>I h , p h w p h rr p h pr p r<br><!-- End of picture text -->



<!-- Start of picture text -->
ii)  Hand pose retargeting mechanism between FrankMocap and Adroit<br><!-- End of picture text -->

Figure B: **Pose retargeting from FrankMocap to Adroit** . **i)** Joint hierarchies for Frankmocap (left) ad Adroit (right). Frankmocap has 15 ball joints with 3 DoF, root with 6 DoF and 5 finger tips. Adroit has 24 revolute joints with 1 DoF and an arm (not shown) with 6 DoF. **ii) Pose retargeting mechanism for transforming Frankmocap joints to the Adroit joint space.** a) We first obtain the Frankmocap pose i.e. 3D joint locations in the world coordinate frame b) This is converted to a root relative coordinate frame through a simple coordinate translation. c) We then compute the palmar plane in Frankmocap to obtain the arm orientation for Adroit. Subsequently, the structure of the kinematic tree is used to successively transform the root relative coordinate frame to a parent relative frame centered at each joint. d) The polar coordinates (azimuth and elevations) computed in the parent relative system yield local joint angles that are mapped onto the revolute joints in Adroit. 

|Parameter|Value|
|---|---|
|Sliding friction|1_N_|
|Tortional friction|0_._5_N_|
|Rolling friction|0_._01_N_|
|Hand wrist damping|0_._5_N_|
|Hand fingers damping|0_._05_N_|
|Object rotational damping|0_._1_N_|
|Object mass|1_kg_|



Table A: **Physical parameter settings used in the simulator** 

## **E Physical parameters in the simulator** 

### **E.1 Parameter settings** 

We report the physical parameters setting for the simulated environment in Table A. All environment physical parameters are taken from [2]. The sliding friction acts along both axes of the tangent plane. The torsional friction acts around the contact normal. The rolling friction acts around both axes of the tangent plane. Regular friction is present between the hand, object and table. The joints within the hand are assumed to be friction-less with respect to each other. 

15 



<!-- Start of picture text -->
= 0.1 Training settings<br>(kg) (kg)<br>Succes Stability<br><!-- End of picture text -->

Figure C: **Robustness to changes in physical parameters** . We evaluate DexVIP on a range of object mass and scale values. DEXVIP remains fairly robust to large variations in such physical object properties. 

### **E.2 Robustness to parameters** 

To further demonstrate the robustness of the trained policy to different masses and scales of the objects, we evaluate the trained policy on objects with varying masses and scales. Specifically, we vary the mass between 0 _._ 5 _kg_ and 1 _._ 5 _kg_ and the scale between 0 _._ 8 _x_ and 1 _._ 2 _x_ of the training size. Results can be seen in Figure C. We observe that DexVIP remains fairly robust to large variations in these physical properties. It is easier to grasp lighter object than heavier ones as expected. 

## **F Hand-Affordance distance** 

The distance input _d_<sup>_r_</sup> _t_<sup>is the pairwise distance between the agent’s hand and the object affordance region as</sup> defined in GRAFF [18]. Here the object affordance region is a 2D binary affordance map that is inferred from a model from [18] that is trained for affordance anticipation on ContactDB objects. Like in [18], we find that this model works reasonably well for objects outside ContactDB as well. We obtain affordance points by back-projecting the affordance map to 3D points in the camera coordinate system using the depth map at _t_ 0. We sample _M_ = 20 points from these back-projected points. We then track these points throughout the rest of the episode. In the noise experiments, in addition to the stated noise models, we also induce tracking failure on the affordance points to relax the tracking assumption as in [18]. For points on the hand, we sample _N_ = 10 regular points on the surface of the palm and fingers. The number of points at every time step remains the same across all objects. 

## **G Additional results** 

### **G.1 Effect of pose prediction on performance** 

DEXVIP uses hand poses inferred from video frames for obtaining target pose priors. Since these poses are inferred, there can be errors in these predictions. To examine the effects of those errors on our policies, we train a model on ground truth (GT) hand poses from ContactPose [49] captured using mocap for all ContactDB objects. Using these GT poses to train the DEXVIP policy provides an upper bound for grasp performance with perfect pose. Results are reported in Table B. We find that the policy trained using inferred poses performs comparably to the one trained on GT poses, showing that DEXVIP is fairly robust to errors in pose predictions. We further note that the hand pose clustering process that we perform is able to effectively filter out bad/outlier poses so that we obtain a representative hand pose for each object (Fig. D). 

### **G.2 Effect of object shape variation on performance** 

We use keywords containing the object class label for obtaining grasp images for each object. We use the same object category in simulation as well. Note that we do not require an exact matching object instance for the one in the video. A generic object mesh from the same category works quite well. To illustrate this, we show samples of a few objects in the video frame and within the simulator along with their grasp success rate in Fig. E. We find that DEXVIP remains fairly robust to variations in the object shape between the video and simulator. For instance, even though objects like teapot, flashlight and saucepan do not have an exact match in the simulator, the grasp policy works quite well on these objects. 

16 

|Pose Supervision|Success|Stability|Functionality|Posture|
|---|---|---|---|---|
|Inferred pose|68|51|64|62|
|GT pose|70|53|65|65|



Table B: **Effect of hand pose supervision on grasping performance** . DEXVIP uses hand poses inferred from video frames for supervision. Using ground truth poses captured using mocap to train the DEXVIP policy provides an upper bound for grasp performance. The policy trained using inferred poses performs comparably to the one trained on GT poses indicating robustness to pose errors. 



<!-- Start of picture text -->
Cluster center Outliers<br><!-- End of picture text -->

Figure D: **Outlier poses.** The clustering mechanism effectively filters out outlier poses which are produced due to errors in pose prediction. 



<!-- Start of picture text -->
Teapot: 59% Mug: 51% Flashlight: 81% Saucepan: 86% Bottle: 61%<br><!-- End of picture text -->

Figure E: **Effect of object shape variation on performance.** DEXVIP remains fairly robust to variations in the object shape between the video and simulator. For instance, even though objects like teapot, flashlight and saucepan don’t have an exact match in the simulator, the grasp policy works quite well on these objects. 

17 

|Model|Success|Stability|Functionality|Posture|
|---|---|---|---|---|
|Affordance only|60|41|63|48|
|Affordance + Touch|63|45|64|49|
|Affordance + Touch + Pose prior<br>(full DEXVIP model)|**68**|**51**|**64**|**62**|



Table C: **Metrics for DEXVIP ablations.** The full DEXVIP policy is able to leverage the touchinformed pose prior to perform well across all metrics. 



Figure F: **Grasping results on additional non-ContactDB objects.** Compared to the performance on ContactDB, DEXVIP is able to maintain its performance and experiences only a marginal drop whereas the other methods take substantial hits to performance. While the success rate of DAPG and GRAFF drop by 15% and 12% respectively, the drop for DexVIP is only 4%. These results indicate that DEXVIP can effectively leverage hand poses for a variety of different objects. 

### **G.3 Ablation evaluation** 

We report all metrics for the ablations of the main paper in Table C. We observe that the full DEXVIP model gains substantially in success, stability and posture metrics, while maintaining the functionality score of the policy that is trained using only affordance. 

### **G.4 Performance on additional objects** 

In addition to comparing performance on non-ContactDB objects with DAPG, we provide a comparison against all methods in Figure F. Note that all 11 non-ContactDB objects belong to object classes not found in ContactDB. When compared to performance on ContactDB, we observe that DEXVIP is able to maintain its performance and experiences only a marginal drop whereas the other methods undergo substantial drops in performance. As reported in L318-320, DAPG’s success rate drops from 59%-50%, a 15% drop in performance, while DEXVIP sees a marginal 4% drop from 68% to 65%. Furthermore GRAFF also sees a large 12% drop from 60% to 53%. The results indicate that DEXVIP can effectively leverage hand poses for a variety of objects. 

18 

