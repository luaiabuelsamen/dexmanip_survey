# **Holo-Dex: Teaching Dexterity with Immersive Mixed Reality** 

Sridhar Pandian Arunachalam Irmak G¨uzey New York University New York University (a) Demonstration collection in mixed reality 

Soumith Chintala Lerrel Pinto Meta AI New York University 



























<!-- Start of picture text -->
(b) Learned dexterous policies<br><!-- End of picture text -->

Fig. 1: We present HOLO-DEX, a framework that (a) collects high-quality demonstration data by placing human teachers in an immersive mixed reality world, and then (b) learns visual policies from a handful of these demonstrations to solve dexterous manipulation tasks. 

**_Abstract_ — A fundamental challenge in teaching robots is to provide an effective interface for human teachers to demonstrate useful skills to a robot. This challenge is exacerbated in dexterous manipulation, where teaching high-dimensional, contact-rich behaviors often require esoteric teleoperation tools. In this work, we present HOLO-DEX, a framework for dexterous manipulation that places a teacher in an immersive mixed reality through commodity VR headsets. The high-fidelity hand pose estimator onboard the headset is used to teleoperate the robot and collect demonstrations for a variety of generalpurpose dexterous tasks. Given these demonstrations, we use powerful feature learning combined with non-parametric imitation to train dexterous skills. Our experiments on six common dexterous tasks, including in-hand rotation, spinning, and bottle opening, indicate that HOLO-DEX can both collect high-quality demonstration data and train skills in a matter of hours. Finally, we find that our trained skills can exhibit generalization on objects not seen in training. Videos of HOLO-DEX are available on https://holo-dex.github.io/.** 

## I. INTRODUCTION 

Learning-based methods have had a transformational effect in robotics on a wide range of domains from manipulation [1, 2], locomotion [3, 4, 5], and aerial robotics [6, 7, 8]. Such methods often produce policies that input raw sensory observations and output robot actions. This circumvents challenges in developing state-estimation modules, modeling object properties and tuning controller gains, which requires significant domain expertise. Even with the steep progress in robot learning, we are still long way off from dexterous robots that can solve arbitrary robot tasks akin to methods 

in game play [9, 10], text generation [11, 12] or few-shot vision [13, 14]. 

To understand what might be missing in robot learning, we need to ask a central question: How do we collect training data for our robots? One option is to collect data on the robot through self-supervised data collection strategies. While this results in robust behaviors [15, 16, 17, 18], they often require extensive real-world interactions in the order of thousands of hours even for relatively simple manipulation tasks [19]. An alternate option is to train on simulated data and then transfer to the real robot ( _Sim2Real_ ). This allows for learning complex robotic behaviors multiple orders of magnitude faster than on-robot learning [20, 21]. However, setting up simulated robot environments and specifying simulator parameters often requires extensive domain expertise [22, 23]. 

A third, more practical option to collect data is by asking human teachers to provide demonstrations [24, 25]. Robots can then be trained to quickly imitate the demonstrated data. Such imitation methods have recently shown promise in a variety of challenging dexterous manipulation problems [26, 27, 28]. However, there lies a fundamental limitation in most of these works – collecting high-quality demonstration data for dexterous robots is hard! They either require expensive gloves [29], extensive calibration [27], or suffer from monocular occlusions [28]. 

In this work, we present HOLO-DEX, a new framework to collect demonstration data and train dexterous robots. It uses VR headsets (e.g. Quest 2) to put human teachers in an immersive virtual world. In this virtual world, the teacher can view a robotic scene from the eyes of a robot, and control it using their hands through inbuilt pose detectors. HOLO- 

Correspondence to sridhar@nyu.edu. 

DEX allows humans to seamlessly provide robots with highquality demonstration data through a low-latency observational feedback system. HOLO-DEX offers three benefits: (a) Compared to self-supervised data collection methods, it allows for rapid training without reward specification as it is built on powerful imitation learning techniques; (b) Compared to Sim2Real approaches, our learned policies are directly executable on real robots since they are trained on real data; (c) Compared to other imitation approaches, it significantly reduces the need for domain expertise since even untrained humans can operate VR devices. 

We experimentally evaluate HOLO-DEX on six dexterous manipulation tasks that require performing complex, contactrich behavior. These tasks range from in-hand object manipulation to single-handed bottle opening. Across our tasks, we find that a teacher can provide demonstrations at an average of 60 _s_ per demonstration using HOLO-DEX, which is 1 _._ 8 _×_ faster than prior work in single-image teleoperation [28]. On 4 _/_ 6 tasks, HOLO-DEX can learn policies that achieve _>_ 90% success rates. Surprisingly, we find that the dexterous policies learned through HOLO-DEX can generalize on new, previously unseen objects. 

In summary, this work presents HOLO-DEX, a new framework for dexterous imitation learning with the following contributions. First, we demonstrate that high-quality teleoperation can be achieved by immersing human teachers in mixed reality through inexpensive VR headsets. Second, we experimentally show that the demonstrations collected by HOLO-DEX can be used to train effective, and generalpurpose dexterous manipulation behaviors. Third, we analyze and ablate HOLO-DEX over various decisions such as the choice of hand tracker and imitation learning methods. Finally, we will release the mixed reality API, demonstrations collected, and training code associated with HOLO-DEX on https://holo-dex.github.io/. 

## II. RELATED WORK 

Our framework builds upon several important works in robot learning, imitation learning, teleoperation and dexterous manipulation. In this section, we briefly describe prior research that is most relevant to ours. 

## _A. Methodologies for Teaching Robots_ 

There are several approaches one can take to teach robots. Reinforcement Learning (RL) [30, 31, 32] can train policies to maximize rewards while collecting data in an automated manner. This process often requires a roboticist to specify the reward function along with ensuring safety during self-supervised data collection [16, 15]. Furthermore, such approaches are often sample-inefficient and might require extensive simulation training for optimizing complex skills. 

Simulation to Real ( _Sim2Real_ ) approaches focus on training RL policies in simulation, followed by transferring to the real robot [22, 33, 34]. Such a methodology of robot training has received significant success owing to the improvements in modern robot simulators. Sim2Real still requires significant human involvement as every task needs to be carefully 

modeled in the simulator. Moreover, even during training special techniques are required to ensure that the resulting policies can transfer to the real robot [21, 35, 36, 37]. 

Imitation learning approaches focus on training policies from demonstrations provided by an expert. Behavior Cloning (BC) is an offline technique that trains a policy to imitate the expert behavior in a supervised manner [24, 38, 39, 40]. Recently, non-parametric imitation approaches have shown promise in learning from fewer demonstrations [41, 42, 28]. Another set of imitation learning is Inverse Reinforcement Learning (IRL) [43, 25, 44]. Here, a reward function is inferred from demonstrations, followed by using RL to optimize the inferred reward. While HOLODEX is geared towards offline imitation, the demonstrations we collect are compatible with IRL approaches as well. 

## _B. Dexterous Teleoperation Frameworks_ 

To effectively use imitation learning for dexterous manipulation we need to obtain accurate hand poses from a human teacher. There are several approaches to gather demonstrations for dexterous tasks. Using a custom glove to measure a user’s hand movements such as CyberGlove [29, 45] or Shadow Dexterous Glove [46] has been a popular solution. However, although such gloves have high accuracy, they can be expensive and require significant calibration effort. Vision-based hand pose detectors have shown promise for dexterous tasks. Some examples include using multiple RGBD [27], single depth [47], RGB [28], and RGBD [37] images. However, such methods either require custom calibration procedures [27] or suffer from occlusion-related issues when using single cameras [28]. Recently, a new generation of VR headsets has enabled advanced multicamera hand pose detection [48] that gave promising results in [49, 50]. This enhancement provides a robust solution that is significantly cheaper compared to CyberGlove and requires little calibration. While VR tools have been used to collect demonstrations [51, 52] for low-dimensional endeffector control, HOLO-DEX shows that the VR headsets can be used for high-dimensional control in augmented reality. Concurrent to our work, Radosavovic et al. [53] also show that hand tracking from VR can be used to teleoperate robot hands albeit without using mixed reality. 

## _C. Dexterous Manipulation_ 

Due to its high-dimensional action space, learning complex skills with dexterous multi-fingered robot hand has been a longstanding challenge [54, 55, 56, 57]. Model-based RL and control approaches have demonstrated significant success on tasks such as spinning objects and in-hand manipulation [58, 59]. Similarly, model-free RL approaches have shown that Sim2Real can enable impressive skills such as in-hand cube rotation and Rubik’s cube face turning [20, 21]. However, both learning approaches requires hand-designing reward functions along with system identification [58] or task-specific training procedures [21]. Coupled with long training times, often requiring weeks [20, 21], they make dexterous manipulation difficult to scale for general tasks. 



<!-- Start of picture text -->
Server<br>Feedback Loop<br>Robot Camera Stream<br>Retargeting<br>Keypoint Extractor<br>Keypoint Transformation<br>Joint Retargeting<br>Robot Controller<br>VR Interface Communication Module Hardware Setting<br><!-- End of picture text -->

Fig. 2: Overview of HOLO-DEX’s teleoperation module. Given a hand pose in the VR interface, the controller streams the keypoint data to the robot’s server which transforms and retargets the human hand key points to the Allegro Hand. Visual feedback of the teleoperated hand is then provided back to the VR Headset for real-time feedback. 

To address the poor sample efficiency of prior learningbased methods, several works have looked at imitation learning [60, 61]. Here, given a handful of demonstrations, simulated policies can be trained in a few hours. More recently, such imitation-based approaches have shown success on real robot hands [28]. HOLO-DEX takes this idea further by improving the teaching process and demonstrating its utility on a variety of in-hand manipulation tasks. 

## III. BACKGROUND ON VISUAL IMITATION LEARNING 

To understand the imitation learning framework used in HOLO-DEX, we first formalize and describe important background work in self-supervised learning and non-parametric imitation. Together, these enable efficient imitation learning from high-dimensional visual observations. 

## _A. Visual Self-Supervised Learning_ 

Self-Supervised Learning (SSL) focuses on obtaining lowdimensional embeddings _z_ from high-dimensional observations _o_ [62]. Operationally, the observations (e.g. RGB images) are fed into an encoder _fθ_ , where _θ_ denotes the weights of a parametric deep network. While there are several methods to train _fθ_ , the central principle in many works is to predict one ‘view’ of the observation given a different ‘view’ of the same observation. One example of such a learning scheme is data-augmented SSL. Here, the observation _o_ is augmented by applying visual augmentations such as color jitter or random grayscale. Given two augmented views of this observation _o_<sup>1</sup> and _o_<sup>2</sup> , the corresponding embeddings would be _z_<sup>1</sup> _≡ fθ_ ( _o_<sup>1</sup> ) and _z_<sup>2</sup> _≡ fθ_ ( _o_<sup>2</sup> ). The training objective for _fθ_ amounts to maximizing the mutual information between the two embeddings _I_ ( _z_<sup>1</sup> _, z_<sup>2</sup> ). 

To optimize this objective, we use the BYOL [63] training scheme, which amounts to predicting _z_<sup>2</sup> _← gφ_ ( _z_<sup>1</sup> ) through a small deep model _gφ_ called the ‘projector’. This scheme for learning embeddings has had significant success in a variety of domains ranging from computer vision, audio processing, 

and robotics. Given its simplicity, we use BYOL to obtain concise embeddings from our demonstrated data. 

## _B. Non-Parametric Imitation Learning_ 

In our framework for imitation learning we have access to expert demonstrations in the form of _D_<sup>_E_</sup> _≡{_ ( _o_<sup>_E_</sup> _t_<sup>_′ , sE_</sup> _t_<sup>_′ , aE_</sup> _t_<sup>_′_)</sup><sup>_}_,</sup> where _o_<sup>_E_</sup> _t_<sup>_′_representsthesensoryobservationattime</sup><sup>_t′_,</sup><sup>_sE_</sup> _t_<sup>_′_</sup> represents the robot state, and _a_<sup>_E_</sup> _t_<sup>_′_denotestherobotaction</sup> taken. Note that _s_<sup>_E_</sup> _t_<sup>_′_doesnotcontaininformationaboutthe</sup> object that is being manipulated. Hence, object information needs to be inferred from observations _o_<sup>_E_</sup> _t_<sup>_′_.Giventhese</sup> demonstrations, we would like to learn a policy _π_ ( _at|ot_ ) that follows the expert behavior _D_<sup>_E_</sup> . While there are several strategies for optimizing _π_ , we resort to non-parametric approaches given their superior performance in low-data regimes [42, 28]. 

Our non-parametric control framework follows VINN [42], where given the observations _o_<sup>_E_</sup> from the expert demonstration dataset _D_<sup>_E_</sup> , a BYOL encoder _fθ_ is trained. Next, the observations in the dataset are all converted to embeddings, i.e. _{o_<sup>_E_</sup> _t_<sup>_′ }_</sup> _−→{fθ zt_<sup>_E′ }_.During</sup> run time, when the robot receives an observation _ot_ it is embedded to _zt_ . Then the Nearest-Neighbor (NN) example in _{_ ( _zt_<sup>_E′ , sE_</sup> _t_<sup>_′ , aE_</sup> _t_<sup>_′_)</sup><sup>_}_isselectedtobeimitated.Wedenote</sup> this NN example as _{_ ( _zt_<sup>_E∗, sE_</sup> _t_<sup>_∗, aE_</sup> _t_<sup>_∗_)</sup><sup>_}_.Givenasmalldataset</sup> _D_<sup>_E_</sup> , which is often the case in robotic applications, this NN-based imitation learning provides effective learning compared to parametric approaches such as BC. 

## IV. HOLO-DEX 

As seen in Fig. 1, HOLO-DEX operates in two phases. In the first phase, a human teacher uses a Virtual Reality (VR) headset to provide demonstrations to a robot. This phase consists of creating a virtual world for teaching, estimating hand poses from the teacher, retargeting the teacher’s hand pose to the robot’s hand and finally controlling the robot hand. After a handful of demonstrations are collected in phase one, the second phase of HOLO-DEX learns visual 



<!-- Start of picture text -->
Planar Rotation<br>Object Flipping<br>Can Spinning<br><!-- End of picture text -->

Fig. 3: Demonstration collection process for three of our tasks. For each task, the first row shows the user’s perspective inside the VR Headset and the second row shows the corresponding robot hand configuration. 

policies to solve the demonstrated tasks. In this section, we will describe each sub-component in detail. 

## _A. Placing an Operator in a Virtual World_ 

We use the Meta Quest 2 VR headset to place human teachers in a virtual world. The headset surrounds the human in a virtual environment at a resolution of 1832 _×_ 1920 and a refresh rate of 72 Hz. The base version of this headset is affordable at $399 and is relatively light at 503g. These features allow for comfortable operation by the teacher. Importantly, the API interface of the Quest 2 allows for creating custom mixed reality worlds that visualizes the robotic system along with diagnostic panels in VR. Examples of virtual scenes are depicted in Fig. 2 and Fig. 3. 

## _B. Hand Pose Estimation with VR Headsets_ 

In contrast to prior work on dexterous teleoperation, using VR headsets provides three benefits with regard to hand pose estimation of the human teacher. First, since the Quest 2 uses 4 monochrome cameras, its hand-pose estimator [48] is significantly more robust compared to single camera estimators [64]. Second, since the cameras are internally calibrated, they do not require specialized calibration routines that are needed in prior multi-camera teleoperation frameworks [27]. Third, since the hand pose estimator is integrated into the device, it can stream real-time poses at 72Hz. As noted in prior work [27, 28], a significant challenge in dexterous teleoperation is obtaining hand poses at both high accuracy and a high frequency. HOLO-DEX significantly simplifies this problem by using commercial-grade VR headsets. 

## _C. Human to Robot Hand Pose Retargeting_ 

Once we have extracted the teacher’s hand pose from VR, we will need to retarget it to the robotic hand. This is done by first computing the individual hand joint angles in the teacher’s hand. Given these joint angles, a straightforward method of retargeting is to directly command the robot’s joints to the corresponding angle. In practice, this works well for all fingers except the thumb. The thumb presents a unique challenge to our Allegro robot hand since its morphology does not match a human’s hand. To address this, we map the spatial coordinates of the teacher’s thumb fingertip to the robot’s thumb fingertip. The joint angles of the thumb are then computed through an inverse kinematics solver. Since the Allegro hand does not have a pinky finger, we ignore the teacher’s pinky joints. 

The overall pose retargeting procedure does not require any calibration or user-specific tuning to collect demonstrations. However, we find that thumb retargeting can be improved by finding user-specific maps from their thumb to the robot’s thumb. This entire procedure is computationally inexpensive and can stream desired robot hand poses at 60 Hz. 

## _D. Robot Hand Control_ 

Our Allegro Hand is controlled asynchronously over a ROS [65] communication framework. Given desired robot joint positions that were computed from the retargeting procedure, we use a PD controller to output desired torques at 300Hz. To reduce steady-state error, we use a gravity compensation module to compute offset torques. On latency 



<!-- Start of picture text -->
Planar  Rotation<br>Object  Flipping<br>Can<br>Spinning<br>Bottle  Opening<br>Card  Sliding<br>Postit  Sliding<br><!-- End of picture text -->

Fig. 4: Successful rollouts of visual policies trained through HOLO-DEX on our six dexterous tasks. 

tests, we find that when the VR headset is on the same local network as the robot hand, we achieve latency under 100 milliseconds. Having a low error and latency is crucial for HOLO-DEX since it allows for intuitive teleoperation of the robot hand by the human teacher. 

As the human teacher controls the robot hand, they can see the robot change in real time (60Hz). This allows the teacher to correct execution errors in the robot. During the teaching process, we record observational data from three RGBD cameras and the action information of the robot at 5Hz. We had to reduce the recording frequency due to the large data footprint and associated bandwidth required from recording multiple cameras. 

## _E. Imitation Learning with_ HOLO-DEX _Data_ 

Once data is collected in the first phase of HOLO-DEX, we now proceed to the second phase, where visual policies are trained on top of this data. We employ the Imitation with Nearest Neighbors (INN) algorithm for learning. Background details of INN is present in Section III-B. In prior work, INN was shown to produce state-based dexterous policies on the Allegro hand [28]. HOLO-DEX takes this a few steps further and demonstrates that these visual policies can generalize to novel objects in a variety of dexterous manipulation tasks. 

To select the learning algorithm for obtaining lowdimensional embeddings (see Section III-A), we experiment with several state-of-the-art self-supervised learning algorithms [63, 66, 67, 68] and find that BYOL [63] provides the best nearest neighbour results. Hence we select BYOL as our base self-supervised learning method. Once BYOL is trained on the collected demonstrations, we can run dexterous 

manipulation policies on the robot by performing nearest neighbor action retrieval (see Section III-B) to get the closest example in the trainset ( _zt_<sup>_E∗, aE_</sup> _t_<sup>_∗_).Toaccountfortheslower</sup> rate of demonstration collection, we set the action to the difference between the succeeding state to the closest neighbor and the current state, i.e. _at_ = ( _s_<sup>_E_</sup> _t_<sup>_∗_</sup> + _k_<sup>)</sup><sup>_−_(</sup><sup>_s_</sup> _t_<sup>_E_).Here</sup><sup>_k_</sup> represents the number of states skipped during our recording of demonstrations. Note that directly commanding _a_<sup>_E_</sup> _t_<sup>_∗_would</sup> fail due to our asynchronous data storage framework. 

## V. EXPERIMENTAL EVALUATION 

Our experiments and tasks are designed to answer the following questions: 

- How long does it take HOLO-DEX to collect demonstrations? 

- How successful are policies trained by HOLO-DEX? 

- How general are the skills learned by HOLO-DEX? 

- How many demonstrations from HOLO-DEX are required to successfully solve dexterous tasks? 

## _A. Dexterous Manipulation Tasks_ 

We study six dexterous manipulation tasks that require contact-rich, multi-fingered control for successful completion. Details of these tasks are described below. 

- 1) _Planar Rotation:_ Given an object placed at a random position on the palm of the robot hand, the goal is to rotate the object in the counter-clockwise direction along the palm normal vector. Solving this task requires the robot to make multi-fingered contacts to both rotate and correct for deviations of the object from the center of the hand. The task is considered a success if 

the robot is able to rotate the object by 90<sup>_◦_</sup> under a minute. 

- 2) _Object Flipping:_ Given an object placed at a random position on the palm of the robot, the goal is to flip the object in the hand’s direction. Solving this task requires the robot to make multi-fingered contacts for grasping the top face of the object and to correct the object when it deviates from the center of the hand. The task is considered a success if the robot is able to flip the object by 90<sup>_◦_</sup> within a minute. 

- 3) _Can Spinning:_ Given a large can placed horizontally on the palm of the robot hand, the task is to spin the can in the counter-clockwise direction along the palm normal vector. Solving this task requires the robot to make synchronized multi-fingered contacts to apply controlled torques on the curved sides of the can. The task is considered a success if the robot is able to spin the can by 90<sup>_◦_</sup> under 30 seconds. 

- 4) _Bottle Opening_ : Given a bottle on a desk, the task is to single-handedly grab the bottle and turn its lid open using the index finger. Solving this task requires the robot to use the index finger to grip the bottle cap and turn it while using the non-index fingers to hold the bottle firmly. The task is considered a success when the robot rotates the bottle cap by 360<sup>_◦_</sup> under 180 seconds. 

- 5) _Card Sliding:_ Given a card on a desk in front of the hand, the task is to grab the card by sliding it off the table and picking it up. To solve the task the robot requires to use the thumb finger to slide the card to the edge of the desk and the other non-thumb fingers to grab the card from the edge. The task is considered a success when the robot is able to lift the card off and stably grasp it from the table under 120 seconds. 

- 6) _PostIt Note Sliding_ : This task is similar to card sliding, but instead of a card we use a thicker post-it note pad as the object to pick from the desk. To solve the task, the robot needs to apply a firmer torque on the postit note pad using the thumb finger since the object is heavier. The task is considered a success when the robot is able to lift the card off and stably grasp it from the table under 120 seconds. 

For the _Planar Rotation_ task we collect 120 expert demonstrations, while for all the other tasks we collect 30 demonstrations. Additional demonstrations for _Planar Rotation_ are collected to account for the relative difficulty of this task and experimentation with different dataset sizes. 

## _B. How long does it take to collect demonstrations?_ 

The closest dexterous teleoperation work to ours that uses commodity sensors is single-image teleoperation (e.g. DIME [28]), where hand poses are detected via RGB images to get robot joint angles. Despite its simplicity, such single-image pose estimation [64] suffers from hand occlusions, which results in poor teleoperation performance on challenging manipulation tasks [27]. In Table I we show that HOLO-DEX can collect successful demonstrations 1 _._ 8 _×_ faster compared to DIME. For 3 _/_ 6 tasks that require precise 

TABLE I: Average time taken in seconds to collect a single demonstration on our Allegro hand using HOLO-DEX and DIME [28] 

|Task|D|IME|HOL|O-DEX|
|---|---|---|---|---|
||Expert|New User|Expert|New User|
|Planar Rotation|60|150|30|125|
|Object Flipping|6|21|5|6|
|Can Spinning|15|76|10|68|
|Bottle Opening|N/A|N/A|30|48|
|Card Sliding|N/A|N/A|150|N/A|
|PostIt Note Sliding|N/A|N/A|120|N/A|



3D movements, we find that single-image teleoperation is insufficient to collect even a single demonstration. 

To demonstrate the versatility of HOLO-DEX we ask five untrained users to collect demonstrations for each of our tasks. Unlike prior work [28, 27], no user-specific calibration was done for this evaluation. In Table I, we see that these users are successfully able to solve 4 _/_ 6 tasks on their first try, failing only on more difficult sliding tasks. We also find that training on this system is quite important as it yields a nearly 2 _._ 6 _×_ speedup in demonstration collection. 

## _C. How successful are policies trained by_ HOLO-DEX _?_ 

We examine the performance of various imitation learning policies on all dexterous tasks. The imitation learning algorithms include Behavior Cloning (BC) [24], Behavior Cloning from pretrained representations (BC-Rep) [69] and VINN [42]. Table II shows the success rates of each task with different policies. We find that VINN outperforms both Behavior Cloning algorithms on all tasks. This is in line with prior work [42, 28] and showcases the effectiveness of nonparametric imitation with few demonstrations. However, we find that for the two tasks that involve sliding and picking, the performance of VINN is quite low at 30%. We believe this is due to our robot’s inability to sense touch, which limits our vision-only model from performing precise actions. 

TABLE II: Success rates on our Allegro hand using HOLO-DEX 

|Task|BC|BC - Rep|VINN|VINN<br>(New Objects)|
|---|---|---|---|---|
|Planar Rotation|0/10|0/10|10/10|35/50|
|Object Flipping|0/10|0/10|9/10|50/50|
|Can Spinning|0/10|0/10|10/10|45/50|
|Bottle Opening|0/10|0/10|10/10|N/A|
|Card Sliding|0/10|0/10|3/10|N/A|
|PostIt Note Sliding|0/10|0/10|3/10|N/A|



_D. How general are the policies learned by_ HOLO-DEX _?_ 

To understand the generalization capabilities of our models, we analyse the quality of the embeddings we get for a given visual input. Interestingly, we observed that the Planar Rotation policy’s encoder was able to generalize to the other two in-hand manipulation tasks. We reason that this encoder was able to exhibit this behavior since it was trained on abundant Planar Rotation data, where the object used while collecting demonstrations had different colors on it’s each face and was placed on various locations. 

Since our policies are vision-based and do not require explicitly estimating the states of objects, they are compatible 



<!-- Start of picture text -->
Demo object Rollouts with unseen objects<br>Planar Rotation<br>Object Flipping<br>Can Spinning<br><!-- End of picture text -->

Fig. 5: On the left, we depict the object present in demonstration data. On the right, we depict the rollouts produced by running our policies on objects that were not present in demonstration collection. Green boxes denote a successful rollout, while red boxes denote a failure. We see that policies learned by HOLO-DEX are fairly robust to visually diverse novel objects without object-specific training. 



Fig. 6: Effect of varying demonstration data with HOLO-DEX. 

with objects not seen in training. We evaluate our in-hand manipulation policies which were trained for performing Planar Rotation, Object Flipping, and Can Spinning tasks on 10 visually and geometrically distinct objects each, with 5 rollouts for every object in different initial positions. Results for this experiment are in Table II and are visualized in Fig. 5. Surprisingly, for all three in-hand manipulation tasks, we find high success rates without any additional demonstration collection or training. We observed that the Planar Rotation policy was able to generalize on 7 out of 10 objects, whereas the Object Flipping and Can Spinning policies were able to succeed at performing the task on 10 and 9 unseen objects respectively. We believe that the policy fails to generalize on some objects because of their visual features (object color and shape) being very different from that of the object in the demonstrations. This means that although we collect demonstrations from HOLO-DEX on a single object, the learned policies can generalize in a zero-shot manner. 

## _E. How many demonstrations are needed to solve our tasks?_ 

In Fig. 6 we visualize the performance on four of our tasks across different dataset sizes. To decouple the effects of representation learning with action prediction, we use the same encoder (trained on all task data) for different dataset splits. We find that for Can Spinning and Bottle Opening, a single demonstration is sufficient to achieve high performance, while for Planar Rotation and Object Flipping we see steady gains in performance as we increase the amount of demonstration data. 

## VI. LIMITATIONS AND DISCUSSION 

We have presented HOLO-DEX, a framework that takes some of the first steps towards immersive teaching of dexterous robots through VR. There are currently two limitations of this work. First, we find that for the harder manipulation tasks, such as _sliding a card_ our learned policies achieve poor performance. Integrating tactile sensing to HOLO-DEX could remedy this issue. Second, our retargeting procedure only applies to robots that can map to human joints. This limits its applicability to robots with different morphologies (e.g. aerial robots, quadrupeds, etc.). Future research on UX 

design and retargeting mechanisms can enable mapping VR control to more complex end-effectors. 

## VII. ACKNOWLEDGEMENTS 

We thank Ankur Handa, Ilija Radosavovic, Josh Merel, David Brandfonbrener, Ben Evans, Mahi Shaffiulah, Jeff Cui, Jyo Pari and Siddhanth Haldar for feedback and discussions. This work was supported by a Honda award and ONR award N000142112758. 

## REFERENCES 

- [1] C. Chi, B. Burchfiel, E. Cousineau, S. Feng, and S. Song, “Iterative residual policy: for goal-conditioned dynamic manipulation of deformable objects,” _arXiv preprint arXiv:2203.00663_ , 2022. 

- [2] A. E. Tekden, A. Erdem, E. Erdem, M. Imre, M. Y. Seker, and E. Ugur, “Belief regulated dual propagation nets for learning action effects on groups of articulated objects,” in _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , 2020, pp. 10 556–10 562. 

- [3] S. Gangapurwala, M. Geisert, R. Orsolino, M. Fallon, and I. Havoutis, “Rloc: Terrain-aware legged locomotion using reinforcement learning and optimal control,” _IEEE Transactions on Robotics_ , 2022. 

- [4] Y. Ma, F. Farshidian, T. Miki, J. Lee, and M. Hutter, “Combining learning-based locomotion policy with model-based manipulation for legged mobile manipulators,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, pp. 2377–2384, 2022. 

- [5] L. Smith, I. Kostrikov, and S. Levine, “A walk in the park: Learning to walk in 20 minutes with model-free reinforcement learning,” _arXiv preprint arXiv:2208.07860_ , 2022. 

- [6] T. Zhang, G. Kahn, S. Levine, and P. Abbeel, “Learning deep control policies for autonomous aerial vehicles with mpcguided policy search,” in _2016 IEEE international conference on robotics and automation (ICRA)_ . IEEE, 2016, pp. 528– 535. 

- [7] D. Gandhi, L. Pinto, and A. Gupta, “Learning to fly by crashing,” in _2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2017, pp. 3948–3955. 

- [8] J. Hwangbo, I. Sa, R. Siegwart, and M. Hutter, “Control of a quadrotor with reinforcement learning,” _IEEE Robotics and Automation Letters_ , vol. 2, no. 4, pp. 2096–2103, 2017. 

- [9] C. Berner, G. Brockman, B. Chan, V. Cheung, P. Debiak, C. Dennison, D. Farhi, Q. Fischer, S. Hashme, C. Hesse, _et al._ , “Dota 2 with large scale deep reinforcement learning,” _arXiv preprint arXiv:1912.06680_ , 2019. 

- [10] D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. Van Den Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, _et al._ , “Mastering the game of go with deep neural networks and tree search,” _nature_ , vol. 529, no. 7587, pp. 484–489, 2016. 

- [11] J. Guo, S. Lu, H. Cai, W. Zhang, Y. Yu, and J. Wang, “Long text generation via adversarial training with leaked information,” in _Proceedings of the AAAI conference on artificial intelligence_ , vol. 32, no. 1, 2018. 

- [12] M. Huang, F. Li, W. Zou, and W. Zhang, “Sarg: A novel semi autoregressive generator for multi-turn incomplete utterance restoration,” in _Proceedings of the AAAI Conference on Artificial Intelligence_ , vol. 35, no. 14, 2021, pp. 13 055–13 063. 

- [13] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, _et al._ , “An image is worth 16x16 words: Transformers for image recognition at scale,” _arXiv preprint arXiv:2010.11929_ , 2020. 

- [14] S. Gidaris and N. Komodakis, “Dynamic few-shot visual learning without forgetting,” in _Proceedings of the IEEE_ 

_conference on computer vision and pattern recognition_ , 2018, pp. 4367–4375. 

- [15] L. Pinto and A. Gupta, “Supersizing self-supervision: Learning to grasp from 50k tries and 700 robot hours,” _ICRA_ , 2016. 

- [16] S. Levine, P. Pastor, A. Krizhevsky, and D. Quillen, “Learning hand-eye coordination for robotic grasping with deep learning and large-scale data collection,” _ISER_ , 2016. 

- [17] A. Singh, L. Yang, K. Hartikainen, C. Finn, and S. Levine, “End-to-end robotic reinforcement learning without reward engineering,” _arXiv preprint arXiv:1904.07854_ , 2019. 

- [18] M. Vecerik, O. Sushkov, D. Barker, T. Roth¨orl, T. Hester, and J. Scholz, “A practical approach to insertion with variable socket position using deep reinforcement learning,” in _2019 international conference on robotics and automation (ICRA)_ . IEEE, 2019, pp. 754–760. 

- [19] G. Dulac-Arnold, N. Levine, D. J. Mankowitz, J. Li, C. Paduraru, S. Gowal, and T. Hester, “An empirical investigation of the challenges of real-world reinforcement learning,” _arXiv preprint arXiv:2003.11881_ , 2020. 

- [20] OpenAI, M. Andrychowicz, B. Baker, M. Chociej, R. J´ozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, J. Schneider, S. Sidor, J. Tobin, P. Welinder, L. Weng, and W. Zaremba, “Learning dexterous in-hand manipulation,” _arXiv_ , 2018. 

- [21] OpenAI, I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, J. Schneider, N. Tezak, J. Tworek, P. Welinder, L. Weng, Q. Yuan, W. Zaremba, and L. Zhang, “Solving rubik’s cube with a robot hand,” _arXiv_ , 2019. 

- [22] J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel, “Domain randomization for transferring deep neural networks from simulation to the real world,” in _IROS_ , 2017. 

- [23] N. Jakobi, P. Husbands, and I. Harvey, “Noise and the reality gap: The use of simulation in evolutionary robotics,” in _Advances in Artificial Life_ , F. Mor´an, A. Moreno, J. J. Merelo, and P. Chac´on, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 1995, pp. 704–720. 

- [24] D. A. Pomerleau, “Alvinn: An autonomous land vehicle in a neural network,” in _NeurIPS_ , 1989, pp. 305–313. 

- [25] P. Abbeel and A. Y. Ng, “Apprenticeship learning via inverse reinforcement learning,” in _ICML_ , 2004, p. 1. 

- [26] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine, “Learning complex dexterous manipulation with deep reinforcement learning and demonstrations,” _RSS_ , 2018. 

- [27] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox, “Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system,” in _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , 2020, pp. 9164–9170. 

- [28] S. P. Arunachalam, S. Silwal, B. Evans, and L. Pinto, “Dexterous imitation made easy: A learning-based framework for efficient dexterous manipulation,” _arXiv preprint arXiv:2203.13251_ , 2022. 

- [29] M. Caeiro-Rodr´ıguez, I. Otero-Gonz´alez, F. A. Mikic-Fonte, and M. Llamas-Nistal, “A systematic review of commercial smart gloves: Current status and applications,” _Sensors_ , 2021. 

- [30] L. P. Kaelbling, M. L. Littman, and A. W. Moore, “Reinforcement learning: A survey,” _JAIR_ , 1996. 

- [31] T. P. Lillicrap, J. J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, and D. Wierstra, “Continuous control with deep reinforcement learning,” _arXiv preprint_ , 2015. 

- [32] D. Yarats, R. Fergus, A. Lazaric, and L. Pinto, “Mastering visual continuous control: Improved data-augmented reinforcement learning,” _arXiv preprint arXiv:2107.09645_ , 2021. 

- [33] F. Sadeghi and S. Levine, “Cad2rl: Real single-image flight without a single real image,” _arXiv preprint arXiv:1611.04201_ , 2016. 

- [34] L. Pinto, M. Andrychowicz, P. Welinder, W. Zaremba, and P. Abbeel, “Asymmetric actor critic for image-based robot learning,” _RSS_ , 2018. 

- [35] Y. Wu, W. Yan, T. Kurutach, L. Pinto, and P. Abbeel, “Learning to manipulate deformable objects without demonstrations,” _arXiv preprint_ , 2019. 

- [36] K. Rao, C. Harris, A. Irpan, S. Levine, J. Ibarz, and M. Khansari, “Rl-cyclegan: Reinforcement learning aware simulation-to-real,” in _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2020, pp. 11 157–11 166. 

- [37] Y. Qin, H. Su, and X. Wang, “From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation,” _arXiv preprint arXiv:2204.12490_ , 2022. 

- [38] P. Florence, C. Lynch, A. Zeng, O. Ramirez, A. Wahid, L. Downs, A. Wong, J. Lee, I. Mordatch, and J. Tompson, “Implicit behavioral cloning,” 2021. 

- [39] M. Bojarski, D. Del Testa, D. Dworakowski, B. Firner, B. Flepp, P. Goyal, L. D. Jackel, M. Monfort, U. Muller, J. Zhang, _et al._ , “End to end learning for self-driving cars,” _arXiv:1604.07316_ , 2016. 

- [40] S. Young, D. Gandhi, S. Tulsiani, A. Gupta, P. Abbeel, and L. Pinto, “Visual imitation made easy,” 2020. 

- [41] S. Schaal and C. Atkeson, “Robot juggling: implementation of memory-based learning,” _IEEE CSM_ , 1994. 

- [42] J. Pari, N. M. Shafiullah, S. P. Arunachalam, and L. Pinto, “The surprising effectiveness of representation learning for visual imitation,” 2021. 

- [43] U. Syed and R. E. Schapire, “A game-theoretic approach to apprenticeship learning,” in _NeruIPS_ , J. Platt, D. Koller, Y. Singer, and S. Roweis, Eds., 2007. 

- [44] S. Haldar, V. Mathur, D. Yarats, and L. Pinto, “Watch and match: Supercharging imitation with regularized optimal transport,” _arXiv preprint arXiv:2206.15469_ , 2022. 

- [45] V. Kumar and E. Todorov, “Mujoco haptix: A virtual reality system for hand manipulation,” in _Humanoids_ , 2015. 

- [46] S. Li, J. Jiang, P. Ruppel, H. Liang, X. Ma, N. Hendrich, F. Sun, and J. Zhang, “A mobile robot hand-arm teleoperation system by vision and imu,” in _2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2020, pp. 10 900–10 906. 

- [47] S. Li, X. Ma, H. Liang, M. G¨orner, P. Ruppel, B. Fang, F. Sun, and J. Zhang, “Vision-based teleoperation of shadow dexterous hand using end-to-end deep neural network,” in _2019 International Conference on Robotics and Automation (ICRA)_ . IEEE, 2019, pp. 416–422. 

- [48] S. Han, B. Liu, R. Cabezas, C. D. Twigg, P. Zhang, J. Petkau, T.-H. Yu, C.-J. Tai, M. Akbay, Z. Wang, A. Nitzan, G. Dong, Y. Ye, L. Tao, C. Wan, and R. Wang, “Megatrack: Monochrome egocentric articulated hand-tracking for virtual reality,” 2020. 

- [49] T. Hentschel and J. A. Neuh¨ofer, “Steady hands - an evaluation on the use of hand tracking in virtual reality training in nursing,” in _Proceedings of the 21st Congress of the International Ergonomics Association (IEA 2021)_ , N. L. Black, W. P. Neumann, and I. Noy, Eds. Cham: Springer International Publishing, 2022, pp. 643–649. 

- [50] M. Salvato, N. Heravi, A. M. Okamura, and J. Bohg, “Predicting hand-object interaction for improved haptic feedback in mixed reality,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, pp. 3851–3857, 2022. 

- [51] Z. Gharaybeh, H. Chizeck, and A. Stewart, “Telerobotic control in virtual reality,” in _OCEANS 2019 MTS/IEEE SEATTLE_ , 2019, pp. 1–8. 

- [52] T. Zhang, Z. McCarthy, O. Jow, D. Lee, X. Chen, K. Goldberg, and P. Abbeel, “Deep imitation learning for complex manipulation tasks from virtual reality teleoperation,” in _ICRA_ , 2018. 

- [53] I. Radosavovic, T. Xiao, S. James, P. Abbeel, J. Malik, and T. Darrell, “Real-world robot learning with masked visual pre-training,” 2022. [Online]. Available: https://arxiv.org/abs/ 2210.03109 

- [54] V. Kumar, Y. Tassa, T. Erez, and E. Todorov, “Real-time behaviour synthesis for dynamic hand-manipulation,” in _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , 2014, pp. 6808–6815. 

- [55] I. Mordatch, Z. Popovi´c, and E. Todorov, “Contact-invariant optimization for hand manipulation,” in _Proceedings of the ACM SIGGRAPH/Eurographics Symposium on Computer Animation_ , ser. SCA ’12. Goslar, DEU: Eurographics Association, 2012, p. 137–144. 

- [56] R. Deimel and O. Brock, “A novel type of compliant and underactuated robotic hand for dexterous grasping,” _The International Journal of Robotics Research_ , vol. 35, no. 1-3, pp. 161–185, 2016. 

- [57] J. Mahler, M. Matl, V. Satish, M. Danielczuk, B. DeRose, S. McKinley, and K. Goldberg, “Learning ambidextrous robot grasping policies,” _Science Robotics_ , vol. 4, no. 26, p. eaau4984, 2019. 

- [58] V. Kumar, A. Gupta, E. Todorov, and S. Levine, “Learning dexterous manipulation policies from experience and imitation,” _arXiv_ , 2016. 

- [59] A. Nagabandi, K. Konoglie, S. Levine, and V. Kumar, “Deep dynamics models for learning dexterous manipulation,” _arXiv_ , 2019. 

- [60] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine, “Learning complex dexterous manipulation with deep reinforcement learning and demonstrations,” in _RSS_ , 2018. 

- [61] I. Radosavovic, X. Wang, L. Pinto, and J. Malik, “Stateonly imitation learning for dexterous manipulation,” in _2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2021, pp. 7865–7871. 

- [62] L. Ericsson, H. Gouk, C. C. Loy, and T. M. Hospedales, “Selfsupervised representation learning: Introduction, advances, and challenges,” _IEEE Signal Processing Magazine_ , vol. 39, no. 3, pp. 42–62, 2022. 

- [63] J.-B. Grill, F. Strub, F. Altch´e, C. Tallec, P. Richemond, E. Buchatskaya, C. Doersch, B. Avila Pires, Z. Guo, M. Gheshlaghi Azar, _et al._ , “Bootstrap your own latent-a new approach to self-supervised learning,” _NeurIPS_ , 2020. 

- [64] F. Zhang, V. Bazarevsky, A. Vakunov, A. Tkachenka, G. Sung, C.-L. Chang, and M. Grundmann, “Mediapipe hands: Ondevice real-time hand tracking,” 2020. 

- [65] Stanford Artificial Intelligence Laboratory et al., “Robotic operating system.” [Online]. Available: https://www.ros.org 

- [66] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton, “A simple framework for contrastive learning of visual representations,” _arXiv preprint_ , 2020. 

- [67] X. Chen, S. Xie, and K. He, “An empirical study of training self-supervised vision transformers,” in _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , 2021, pp. 9640–9649. 

- [68] A. Bardes, J. Ponce, and Y. LeCun, “Vicreg: Varianceinvariance-covariance regularization for self-supervised learning,” _arXiv preprint arXiv:2105.04906_ , 2021. 

- [69] S. Young, J. Pari, P. Abbeel, and L. Pinto, “Playful interactions for representation learning,” _arXiv preprint arXiv:2107.09046_ , 2021. 

