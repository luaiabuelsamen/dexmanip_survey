# Rotating without Seeing: Towards In-hand Dexterity through Touch 

Zhao-Heng Yin<sup>1</sup><sup>_,∗†_</sup> , Binghao Huang<sup>2</sup><sup>_,∗_</sup> , Yuzhe Qin<sup>2</sup> , Qifeng Chen<sup>1</sup> , Xiaolong Wang<sup>2</sup> 1HKUST 2UC San Diego http://touchdexterity.github.io 



<!-- Start of picture text -->
Simulation<br>Real<br><!-- End of picture text -->



<!-- Start of picture text -->
Training Test in real world<br>Generalize to Unseen Test Objects<br><!-- End of picture text -->

Fig. 1: We propose **Touch Dexterity** , a new dexterous manipulation system to perform in-hand object rotation with only touch sensing. On the left, we show our hardware setup with 16 FSR sensors attached to an Allegro hand. We train our policy in simulation on rotating diverse objects around different axes. Our trained policy can be directly transferred to the real robot hand and can rotate novel/unseen objects successfully. 

**_Abstract_ —Tactile information plays a critical role in human dexterity. It reveals useful contact information that may not be inferred directly from vision. In fact, humans can even perform in-hand dexterous manipulation without using vision. Can we enable the same ability for the multi-finger robot hand? In this paper, we present Touch Dexterity, a new system that can perform in-hand object rotation using only touching without seeing the object. Instead of relying on precise tactile sensing in a small region, we introduce a new system design using dense binary force sensors (touch or no touch) overlaying one side of the whole robot hand (palm, finger links, fingertips). Such a design is low-cost, giving a larger coverage of the object, and minimizing the Sim2Real gap at the same time. We train an inhand rotation policy using Reinforcement Learning on diverse objects in simulation. Relying on touch-only sensing, we can** 

> _∗_ The first two authors contributed equally. 

> _†_ Work done while an intern at UC San Diego. 

**directly deploy the policy in a real robot hand and rotate novel objects that are not presented in training. Extensive ablations are performed on how tactile information help in-hand manipulation.** 

## I. INTRODUCTION 

Imagine we are washing the used pan in the kitchen after dinner. Suddenly, the power is cut off unexpectedly, and all the lights go out. What would we do? Most of us may stop the work, put down the pan in the sink, and then probably find our phone in the pocket to light up the way. Simple as it may seem, this sequence of actions actually requires precise execution of in-hand dexterous manipulation in the dark, where we receive no vision input for guidance. Even in normal situations with lights on, the manipulation of objects in hand often comes with heavy occlusions. Without relying on vision, we humans are still very good at feeling and manipulating 

objects by hand, which is made possible by the tactile (touch) information coming from our skin. Previous studies in biology also confirm the vital importance of touch information for dexterous manipulation [30]. Can we enable robots with such dexterity with touch sensing? 

Indeed, tactile sensing has been a long-standing topic in robotics. With different designs of tactile sensors, robots are able to manipulate objects more precisely using contact information [19, 31, 20] and even complete tasks in a touchonly setup [35, 42]. However, it is still very challenging for touch-only approaches to achieve complex and high degreeof-freedom (DOF) in-hand manipulation. While most current literature focuses on modeling precise and fine-grained contact using increasingly high-quality sensors, it introduces two challenges to in-hand manipulation: (i) Most approaches are only able to attach the expensive sensors to the finger-tips of the gripper or hands instead of covering the whole manipulator, limiting the range of tasks to perform; (ii) It often requires a large number of training samples for complex tasks, but it is hard to leverage a simulator given the Sim2Real gap is usually very large for a delicate sensor. 

In this paper, we present **Touch Dexterity** , a new system design and learning pipeline for in-hand rotation using only touching. Instead of using a few sensors on finger-tips that give high-quality patterns [75, 33, 46], we propose the alternative: Use a lot of low-cost binary force sensors (touch or no touch) attached over one side of the hand (fingertips, links, and palm) as shown in Fig. 1 (left). Specifically, we attach the ForceSensing Resistor (FSR) sensors, which cost around $12 each on Amazon<sup>1</sup> , to the Allegro robot hand. Our insight is that, while one single binary force sensor cannot do much, the combination of 16 of them has a strong representation power (2<sup>16</sup> types of states in maximum), which might allow the robot hand to “feel” the object state without seeing. Importantly, the Sim2Real gap by using such a binary sensor is minimized to the extreme, which allows large-scale sample collection in simulation for training. 

With this system setup, we focus on the task of rotating an “unseen” object around the _x_ , _y_ , and _z_ -axis using the multifinger hand as shown in Fig. 1 (right). Here “unseen” not only indicates there is no vision, but also means the object is not presented during training time. While this task is a simplified version of the in-hand re-orientation task, it is still very challenging as all the fingers are moving with a relatively large motion to rotate the object and prevent it from falling off the palm at the same time. We believe the same pipeline can be directly extended to more complex tasks in the future. We train our policy on multiple objects in parallel in the IsaacGym simulator [38] using Reinforcement Learning (RL), and the learned policy can be directly deployed on the real robot manipulating diverse unseen objects. The key to achieving such generalization across objects and to the real robot is our touch sensors. Our RL policy takes both the binary touch sensing information and the robot’s internal state as input and predicts 

the action in each time step for closed-loop control. With a large coverage over the object using the touch sensors, our hypothesis is that the policy implicitly learns to understand the 3D structure and pose of the object and perform rotation accordingly. 

In our experiments, we test the real-world system with 10 diverse objects. Our method shows surprising robustness in rotating unseen objects using only touch sensing. For example, we can rotate the rubber duck for two cycles without falling, even if it is never presented in training (last row in Fig. 1). We perform extensive ablations on our sensor to validate our design, including disabling all the touch sensors, disabling part of them, and using continuous signals instead of binary signals. 

## II. RELATED WORK 

**Dexterous Manipulation** Dexterous manipulation has been a long-standing problem in robotics [56, 45, 17, 27, 1, 16, 26, 25, 10, 21, 59, 12, 69, 2]. Among these works, dexterous in-hand manipulation receives a lot of attention in recent years [32, 6, 5, 41, 2]. Several early methods propose to tackle the in-hand manipulation problem with analytical model-based approaches [32, 5]. Nevertheless, they pose certain hypotheses about the objects and the controllers, which makes it hard to scale to more complex tasks. To overcome this limitation, deep Reinforcement Learning has been applied recently on dexterous manipulation [2, 28, 15, 52, 14, 51]. Building on these works, incorporating demonstrations in with imitation learning also leads to better sample efficiency and more natural manipulation behaviors [54, 55, 4, 53, 71, 74, 37, 48, 3]. However, most in-hand manipulation methods are still highly relying on visual inputs [2, 28, 14]. For example, Chen et al. [14] propose to perform in-hand object re-orientation using depth image input, and new hardware is designed to avoid heavy occlusion. Instead of relying on vision which faces the occlusion problem with general hardware, recently, several works [51, 61, 50] propose to perform in-hand object rotation without both visual and explicit tactile sensing. The idea of these works is that we can infer the object’s information from the implicit tactile information inside proprioception data. However, these works either only consider object rotation on the fingertip with relatively small finger motion, or the rotation of a limited set of objects. Compared to these works, our system explicitly use touch sensors to percept hand-object interaction, and can solve the object rotation problem on the palm for diverse types of objects, which involves complex object motion and is more challenging. We also find that using explicit tactile sensing enables our touch-based policy to generalize to unseen objects, which is not shown by previous works. 

**Tactile Robotic Manipulation** Biological evidence suggests that tactile information is crucial for the success of human dexterity [30]. This basic observation naturally motivates the research of tactile robotic manipulation [13, 40, 19, 7, 44, 76, 47, 65, 64, 73, 63, 70, 67, 62, 29, 47, 42, 66, 34, 23, 8]. A fundamental question is what kind of touch information is essential. Existing works propose to extract local geometry, 

1https://www.amazon.com/s?k=fsr+sensor 

force and torque, contact event, and material properties with various sensors to help manipulation [35]. Different from these works, we find that even using the simplest binary contact signal provided by a sparse sensor array can be helpful for a high-dimensional manipulator. This is also found in [49, 22, 36] where binary contact signals are used for manipulation, object tracking and exploration. However, they focus on low-DOF manipulators rather than a multi-finger robot hand. In the dexterous hand research, Buescher et al. [11] develop a skinbased tactile sensing system on the Shadow hand, which has a similar but denser sensor layout over the palm compared with our work. However, it is still unclear how to use it with a control method to solve in-hand rotation as in our work. Another important question in tactile robotic manipulation is how to simulate the tactile event so as to perform Sim2Real transfer. Researchers have proposed many approaches and strategies for tactile simulation [39, 24, 72, 18, 60, 9]. For example, Xu et al. [72] propose a method to simulate normal and shear tactile force field on the contact surface. Compared with these works, our method does not require any extra simulation design but can leverage the built-in contact simulation of an existing physics simulator. 

III. TACTILE DEXTEROUS MANIPULATION SYSTEM 

## _A. Real-word System Setup_ 

Our hardware setup consists of a XArm robot arm and a 16-DOF Allegro Hand with a contact sensor array. The array consists of 16 contact sensors, which are attached to different parts of the allegro hand including the palm and tips as shown in Figure 1(left). The used contact sensors are based on ForceSensing Resistors (FSR), whose resistance will change when an external force is applied to its surface. These sensors are very sensitive to force and widely used in robotics. We use an STM32F microcontroller to collect the analog voltage signals of each sensor and then forward digital signals to the host. 

While these contact sensors are able to output the **continuous** contact force measurement, the signals are usually nonlinear and noisy. As a result, it should undergo necessary preprocessing before being used for control. We **binarize** these measurements with respect to a selected threshold _θth_ and use this binary contact signal for control. The advantage of using binary signals is that it can reduce the gap between the simulation and the real robot, and simplify the Sim2Real transfer procedure. When using the exact force measurement as observation, it is difficult to align the measurement between the simulation and the real robot, especially since there are still errors in aligning the analog voltage signals to the exact force measurement. In contrast, we can easily calibrate the binarized measurement by adjusting the threshold. 

## _B. Simulation Setup_ 

In this paper, we use the IsaacGym simulator [38] for the training of our tactile manipulation system. The simulation setup is shown in Figure 1(left). We simulate each contact sensor as a fixed link on the finger and palm links. We fetch the net contact force _F_ = [ _Fx, Fy, Fz_ ] over each sensor link 





Sensing In-Hand Position Sensing Critical Contact 

Fig. 2: Two major functionalities of our sensors: sensing (i) the objects’ in-hand position, and (ii) the critical contact during the dexterous manipulation process. Note that we use finger cots to increase the friction and we still have force-sensing resistors inside the finger cots. 

provided by the simulator at each simulation step, and use _∥F ∥_ as the simulated contact force measurement. Then, we binarize the measurement with another threshold _θ_<sup>˜</sup> _th_ , Note that the force provided by the sensor’s parent link does not contribute to the net contact force. We adjust the threshold _θ_<sup>˜</sup> _th_ of these sensors to ensure that they have similar behavior to that in the real. We use a _θ_<sup>˜</sup> _th_ = 0 _._ 01 _N_ in simulation. 

## _C. Benchmark Problem: In-hand Rotation_ 

In this paper, we study the dexterity of our system by using it to solve an in-hand rotation task. In this in-hand rotation task, an object is initialized in the palm and the robot hand is then required to rotate this object around a given rotation axis. 

When we are doing in-hand object rotation, the object motion is more complex than that in finger-tip rotation mentioned in section II and brings additional challenges. Specifically, the object can slide or roll in the palm during in-hand manipulation. Due to this complex motion pattern, explicit feedback from tactile or vision becomes necessary for successful manipulation. Otherwise, we are unable to infer the current state of the object and fail to push and rotate it in a secure way. 

## _D. Discussion: What information can sensors provide?_ 

We summarize two kinds of information our system can provide for control as follows, though its sensing is sparser than that of a real human hand. 

**Position information.** The contact sensors can inform the policy where the object is at each time step. One example is shown in Figure 2 (left). In this example, a cuboid is placed on the palm without contacting any fingertip. At this moment, the only way to infer the position of the object is by reading the measurement of the contact sensors on the palm. This measurement can provide an estimation of the object’s position (i.e., at the center), based on which the controller can decide the approximate movement of each finger, for example, driving the thumb toward the center. Without this information, the thumb can move to the right and can not come into contact with the object to initiate a rotation. 

**Interaction information.** During in-hand object rotation, it is essential to ensure that the fingertip in charge of the 



<!-- Start of picture text -->
Stacked States<br>Robot Proprioception EMA<br>Contact Signals Policy<br>Action ��<br>Previous Target<br>Next<br>Target<br>PD Controller<br>Torque<br>MCU<br>�� ∈ 0,1  16<br>�� ∈ℝ 16<br><!-- End of picture text -->

Fig. 3: Overview of the control process. The state contains tactile information, joint position, previous target, and task information like rotation axis (not shown in the figure). The policy then uses the stacked state to get the relative action, and the next target joint position is calculated. The new target is then fed to a PD controller. 

rotation is indeed interacting with the object, see Figure 2 (right). Otherwise, the finger may not be able to push against the object leading to a failure, which may cause the object to move to an unstable position, and even fall out of the hand. 

## IV. LEARNING TOUCH DEXTERITY 

## _A. Problem Formulation_ 

We formulate the in-hand rotation problem as a Markov Decision Process _M_ = ( _S, A, R, P_ ). Here, _S_ is the state space, _A_ is the action space, _R_ is the reward function, and _P_ is the transition dynamics. _R_ and _P_ are unknown to the robot. The robot agent observes state _st_ at each step _t_ and take action _at_ = _π_ ( _st_ ) calculated by the current policy _π_ , then it will receive a reward _rt_ = _R_ ( _st, at, st_ +1). The goal of the agent is to maximize the _γ_ discounted return<sup>�</sup><sup>_T_</sup> _t_ =0<sup>_γtrt_.The</sup> definition of these elements is as follows. 

_1) State:_ The state of the system consists of the joint position of the Allegro hand _qt ∈_ R<sup>16</sup> , the sensor observation _ot ∈ {_ 0 _,_ 1 _}_<sup>16</sup> , the previous position target _q_ ˜ _t ∈_ R<sup>16</sup> , and the rotation axis _k ∈_ S<sup>2</sup> . Since the state at one step may not be sufficient for control, we also stack it with other 3 historical states as the input when we use an MLP as the policy network. 

_2) Action:_ At each step, the action produced by the policy network is a relative control command _at ∈_ R<sup>16</sup> . A PD controller then drives the hand to reach the joint position target _q_ ˜ _t_ +1 = _q_ ˜ _t_ + _at_ at the next step. However, using this target directly may lead to non-smooth finger motion, since the actions of two consecutive steps may conflict with each other. Therefore, in practice, we use an exponential moving average as the target: _q_ ˜ _t_ +1 = _q_ ˜ _t_ +˜ _at_ , where _a_ ˜ _t_ = _ηat_ +(1 _− η_ )˜ _at−_ 1 _, t ≥_ 1 and ˜ _a_ 0 = 0. We find that _η_ = 0 _._ 8 works well in the experiments. This PD controller operates at a control frequency of 10Hz both in the simulation and the real. 



<!-- Start of picture text -->
Rotation Angle Rotation<br>Axis<br>Normal<br>Plane<br>Rotated vector<br><!-- End of picture text -->

Fig. 4: Illustration of the calculation of rotation angle ∆ _θ_ : The object rotates alone Axis _k_ and here we visualize the rotation angle ∆ _θ_ in the Normal Plane. 

_3) Reward:_ We design a reward function that is able to make the dexterous hand rotate the object in a smooth and transferable way. The reward function used in this paper is a weighted mixture of several components: 

_rt_ = _w_ 1 _rrot_ + _w_ 2 _rvel_ + _w_ 3 _rfall_ + _w_ 4 _rwork_ + _w_ 5 _rtorque_ + _w_ 6 _rdist._ (1) 

The first term _rrot_ is the rotation reward defined as the rotated angle ∆ _θ_ of a sampled unit vector in the normal plane Π of the rotation axis _k_ : 



The detailed calculation of ∆ _θ_ is shown in Figure 4. First, we sample a unit vector _v_ in Π randomly and we may as well imagine it is attached to the object. Then we fetch its corresponding vector _v_<sup>_′_</sup> at the next state and project it to Π: _vp_<sup>_′_=Proj(</sup><sup>_v′,_Π).∆</sup><sup>_θ∈_[</sup><sup>_−π, π_)isdefinedasthesigned</sup> distance between _vp_<sup>_′_and</sup><sup>_v_withrespecttotheaxis</sup><sup>_k_.Notethat</sup> [51] uses _⟨ω, k⟩_ as the rotation reward, where _ω_ is the angular velocity returned by the simulator. Nevertheless, we find that the angular velocity provided by the simulator in our setting is very noisy since the motion of the object is very complex. As a result, using this angular velocity in the reward can usually lead to very undesirable object motion patterns, like vibrating around a specific pose. We find that using this finite difference as the reward can produce consistent rotation behavior across different runs. The second term is a penalty on the object’s velocity _rvel_ = _−∥vt∥_ . This encourages the hand to rotate the object in a stable manner and increases the transferability of the trained policy. The third reward _rfall_ is a negative falling penalty when the object falls out of the palm. The fourth reward _rwork_ penalize the work of controller, which is defined as _rwork_ = _−⟨|τ |, |q_ ˙ _t|⟩_ . Here, _τ_ is the outputted torque of the PD controller at step _t_ . This penalty helps to improve the smoothness of finger motion. The fifth term _rtorque_ = _−∥τ ∥_ penalizes the large torque. Finally, _rdist_ = mean(clip(1 _/_ ( _ϵ_ + _d_ ( _xtip, xobj_ )) _, c_ 2 _, c_ 3)) is a distance reward, which encourages the fingertip to come close to the object and interact with it. 

_4) Reset Strategy:_ We design several reset strategies to reduce unnecessary exploration and speed up the learning process. First, we reset the episode when the object deviates 

too much from its initial position (i.e., the center of the palm). Moreover, we reset the episode when the major axis of the object deviates too much from the rotation axis, this reduces the exploration of an undesired rotation direction. 

## _B. Domain Randomization_ 

We use a wide variety of domain randomization [68] to improve the Sim2real transfer. 

_1) Physics randomization:_ We randomize the object’s initial position, mass, shape, and friction to ensure that the learned policy can deal with different kinds of objects. 

Moreover, we randomize the gain of the PD controller to model the uncertainty of the PD controller in real. Besides, we consider randomizing each tactile sensor. For each activated contact sensor that outputs 1, with probability _p_ we flip its output to 0. We also model the signal delay of the contact sensor by an exponential delay used in [28]. 

_2) Non-physics randomization:_ We use a set of non-physics randomization to further improve the robustness of the trained policy. We inject white noises into the observation of the policy, and its outputted action to ensure that it is robust to small perturbations. 

## _C. Training Procedure_ 

We use the proximal policy optimization (PPO) [58] algorithm to train our control policy and multilayer perceptron (MLP) for both of the policy and value networks. We use the advantage clip threshold _ϵ_ = 0 _._ 2 and the KL threshold of 0.02. We use ELU [43] as the activation function in these networks. The policy network outputs a Gaussian distribution with a learnable state-independent standard deviation. Like [28], in order to reduce the training difficulty, we also use asymmetric observation for the policy and value network. Concretely, for the value network, we add privileged information such as the contact force over each link, the object’s ground-truth pose, and physical parameters to its input. This privileged information is not accessible by the policy network. For the policy network, we only stack the current state with 3 historical states as the input. 

For the IsaacGym simulation, we set _dt_ = 0 _._ 01667 _s_ with 2 simulation substeps. We use 8192 parallel environments. The action (control target) outputted by the policy network is executed by 6 steps, corresponding to a 10Hz control frequency in real. 

## V. EXPERIMENTS 

In this part, we compare our Touch Dexterity system to several baselines in both the simulation and the real. Specifically, we are interested in the following questions: 

- 1) _How much benefit does tactile information offer compared to the baseline in training?_ 

- 2) _Using simulation as an ideal setup, does the usage of tactile information lead to better robustness and generalization?_ 

- 3) _How well does our tactile manipulation system perform and generalize compared with other methods in the real?_ 



<!-- Start of picture text -->
Object Set A<br>Irregular cubes<br>Object Set B<br>Irregular cylinders,<br>Large aspect-ratio<br>objects<br>Simulation<br>Object Dataset<br>Real-world Object Dataset Samples (Object Set C)<br><!-- End of picture text -->

Fig. 5: The object sets used in our experiments. The full object set in the real world can be found in the supplementary material. 

4) _How well does tactile perception in simulation align with that in real? How does it improve performance in real?_ We answer these questions through an extensive case study on the _z_ -axis rotation. Then, we demonstrate that our system can also learn the rotation skill along all the other axes. 

## _A. Experiment Setup_ 

_1) Object Dataset:_ For the simulation experiments, we train and evaluate our policy on a set of artificial objects of common geometries, such as cuboids, cylinders, and balls. Some examples of these objects are shown in Figure 5. Despite their simplicity, their diverse geometry can be used to approximate a large set of common daily objects. For the real experiments, we bring in some unseen real-world objects like a rubber duck, lego box for evaluation as shown in Figure 5. _2) Evaluation Metric:_ To evaluate the performance of a trained policy, we introduce the following metric as suggested by [51]. 

- 1) **Cumulative Rotation Reward (CRR).** We calculated the cumulative rotation reward to evaluate the rotation capability of a policy in the simulation. This metric is only used in the simulation. 

- 2) **Cumulative Rotation Angle (CRA).** We count the cumulative rotation angle (by rounds) to evaluate the rotation capability of a policy in the real. This metric is counted by a human. 

- 3) **Time-to-Fall (TTF/Duration).** We measure the time (by seconds) of an object staying in the palm before falling down the hand. This metric can be used both in the simulation and in real. 



<!-- Start of picture text -->
Single Object Training Single Object Training Multi Object Training Multi Object Training<br>60<br>1000 50 w Sensor (Ours)<br>1250 50 No Sensor<br>1000 40 800 40<br>750 30 600 30<br>500 20 400 20<br>250 10 200 10<br>0 0 0 0<br>0 1K 2K 3K 4K 5K 0 1K 2K 3K 4K 5K 0 1K 2K 3K 4K 5K 0 1K 2K 3K 4K 5K<br>Training Steps Training Steps Training Steps Training Steps<br>Single Object Training Single Object Training Multi Object Training Multi Object Training<br>1250 50 1000 50 High Sensitivity (Ours)<br>1000 40 800 40 Low Sensitivity (LS-Sensor)<br>750 30 600 30<br>500 20 400 20<br>250 10 200 10<br>0<br>0 0 0<br>0 1K 2K 3K 4K 5K 0 1K 2K 3K 4K 5K 0 1K 2K 3K 4K 5K 0 1K 2K 3K 4K 5K<br>Training Steps Training Steps Training Steps Training Steps<br>TTF TTF<br>Cumulative Rotation Reward Cumulative Rotation Reward<br>TTF TTF<br>Cumulative Rotation Reward Cumulative Rotation Reward<br><!-- End of picture text -->

Fig. 6: Top: Policy training curve with and without sensors. Bottom: Policy training curve with sensors of different sensitivities. The results are averaged on 3 seeds. The shaded area shows the standard deviation. 

## _B. Baselines_ 

In the experiments, we mainly compare our methods with the following baselines. 

- 1) **No-Sensor.** We train a PPO policy to control the hand with no tactile information available. The only way to infer the object-hand interaction information is by comparing the current joint position to the desired, target joint position. For example, when a finger (e.g. thumb) is pressing the top surface of a cuboid, we can observe a difference between these two quantities, indicating the existence of pressing behavior. 

- 2) **LS-Sensor.** We set a higher sensor activation threshold _θth_ = 0 _._ 2 _N_ and train another PPO policy. In other words, the sensors now have lower sensitivity to the contact, and we call this policy LS-Sensor. Under this setup, the hand is no longer able to sense some slight contacts. 

- 3) **DS-Sensor.** This policy is used for ablation purposes. Its only difference from our policy is that it will disable all the tactile input during evaluation. This is used to test to which extent the trained tactile policy uses tactile information. 

In the real-world experiments, we also introduce additional two policy baselines: 

- 1) **Openloop Policy.** We collect several successful object rotation trajectories in the simulation and execute these trajectories on the robot. This is to study whether the considered task is complex enough. 

- 2) **CT-Sensor.** We train a policy that uses a continuousvalued sensor input rather than the binarized version. This is to study if using continuous signals will lead to Sim2Real difficulty. 

Note that there also exist some vision-based dexterous manipulation baselines like [14, 28]. However, we do not compare our method to theirs as they require a collection of a very large 

amount of visual simulation data, which takes significantly longer real-world time. 

## _C. Sim: Policy learning with different sensing capabilities._ 

In this section, we study whether our tactile policy and the considered baseline policies are able to succeed in the training environments in the simulation. We study both the single and multi objects setup. We use the cuboid as the object in single-object training, which is common in the previous works [2, 28]. We use object set A for multi-object training. The results are shown in Figure 6. We find that in the single object setup, both the No-Sense and LS-Sensor policies have a lower rotation reward compared with our policy. Interestingly, we find that LS-Sensor can achieve a higher duration (TTF) compared with No-Sensor and can match that of our full system. This result suggests that tactile sensors of low sensitivity may still be useful to make the motion more secure. For the multiobject training, we find that our tactile policy outperforms the baseline policies by a large margin. The baseline policies fail completely in this case, while our policy is still able to succeed. This result indicates that using tactile information is essential to tame touch-only multi-object rotation. The failure of the LS-Sensor in the multi-object training case suggests that having a high-sensitivity sensor to sense the slightest contact is important. 

## _D. Sim: Is a tactile policy robust and generalizable?_ 

Though our tactile policy and the baseline policies can succeed in some cases during training, so far it remains unknown whether they are robust and generalizable. We consider a policy robust if it can perform well on the unseen physics parameter setup on the same set of objects. We consider a policy generalizable if it can perform well on an unseen set of objects. 

TABLE I: Performance of different methods on the multi-object rotation task on the real robot. The results are averaged on 3 policies trained on 3 seeds. Each trial lasts 30 seconds. The CRA metric is measured by the number of turned rounds. The TTF metric is measured in seconds. Our proposed method can rotate both the seen and unseen objects. 

|**Seen**|**Obj**|**ect C1**|**Obj**|**ect C2**|**Obje**|**ct C3**|**Obj**|**ect C4**|**Obj**|**ect C5**|
|---|---|---|---|---|---|---|---|---|---|---|
||CRA|TTF|CRA|TTF|CRA|TTF|CRA|TTF|CRA|TTF|
|OL|0_._58_±_0_._14|13_._30_±_7_._77|0_._08_±_0_._14|4_._67_±_8_._08|0_._75_±_0_._66|18_._67_±_16_._29|0_._50_±_0|24_._00_±_5_._29|0_._83_±_1_._04|13_._67_±_15_._18|
|No-Sensor|0_._25_±_0_._25|7_._67_±_6_._80|0_._33_±_0_._28|14_._7_±_15_._01|0_._08_±_0_._144|3_._67_±_6_._35|0_._42_±_0_._14|16_._00_±_12_._17|0_._25_±_0_._25|12_._67_±_15_._53|
|CT-Sensor|2_._50_±_3_._25|20_._00_±_8_._66|0_._75_±_0_._66|17_._67_±_10_._79|2_._42_±_2_._10|15_._33_±_15_._01|1_._92_±_1_._46|23_._00_±_12_._12|1_._00_±_0_._87|17_._00_±_15_._39|
|Ours|**4.91**_±_**0.52**|**30.00**_±_**0.00**|**2.83**_±_**1.26**|**28.67**_±_**2.31**|**2.92**_±_**1.38**|**30.00**_±_**0 .00**|**4.50**_±_**1.73**|**30.00**_±_**0.00**|**2.00**_±_**0.00**|**26.67**_±_**5.77**|
|**Unseen**|**To**|**mato**|**A**|**pple**|**Or**|**ange**|**Sou**|**pcan**|**Rubb**|**er Duck**|
||CRA|TTF|CRA|TTF|CRA|TTF|CRA|TTF|CRA|TTF|
|OL|0_._25_±_0_._25|20_._00_±_17_._32|0_._67_±_0_._76|20_._00_±_17_._32|0_._5_±_0_._87|10_._00_±_17_._32|1_._5_±_1_._32|20_._00_±_17_._32|0_._33_±_0_._29|20_._00_±_17_._32|
|No-Sensor|0_._00_±_0_._00|0_._00_±_0_._00|0_._33_±_0_._58|10_._00_±_17_._32|0_._75_±_1_._09|12_._33_±_15_._70|0_._08_±_0_._14|2_._00_±_3_._46|0_._33_±_0_._29|20_._00_±_17_._32|
|CT-Sensor|0_._33_±_0_._29|12_._33_±_15_._70|0_._42_±_0_._52|15_._33_±_15_._01|2_._08_±_2_._10|24_._33_±_4_._93|2_._08_±_2_._79|19_._33_±_16_._77|**1.50**_±_**0.75**|**30.00**_±_**0.00**|
|Ours|**1.08**_±_**0.14**|**27.33**_±_**4.62**|**2.67**_±_**1.04**|**30.00**_±_**0.00**|**3.00**_±_**1.32**|**30.00**_±_**0.00**|**4.25**_±_**1.56**|**27.33**_±_**4.62**|1_._42_±_0_._38|29_._00_±_1_._73|



TABLE II: Performance of different methods on the singleobject rotation task with physics distribution shift in simulation. The results are averaged on 3 seeds. 

|Method|Seen Physi|cs Setup|Unseen Phys|ics Setup|
|---|---|---|---|---|
||CRR|TTF|CRR|TTF|
|No-Sensor|689_._3_±_141_._5|33_._3_±_4_._7|369_._0_±_129_._1|23_._5_±_6_._1|
|Sensor|**963.8**_±_**377.8**|**42.2**_±_**4.1**|**919.3**_±_**338.0**|**40.0**_±_**4.3**|
|DS-Sensor|904_._2_±_408_._6|39_._1_±_6_._3|615_._5_±_293_._2|31_._2_±_8_._0|
|LS-Sensor|860_._0_±_348_._7|38_._8_±_6_._9|796_._5_±_366_._7|37_._4_±_8_._4|



We test the robustness of the single-object setting. To do this, we sample from a smaller, unseen range of friction and mass parameters, and perform rollout. In this case, the object is more likely to slide in the hand, requiring the hand to manipulate it in a more careful manner. The results are shown in Table II. We find that there is little performance drop in our full method. However, for No-Sensor and DS-Sensor, we can observe a clear performance drop. We also find that the low-sensitivity policy LS-Sensor also performs well in the unseen physics setup. This suggests that a low-sensitivity tactile sensing ability is sufficient for the robustness of the single object rotation. 

The generalization testing result is shown in Table III. We train the policies on object set A and test them on object set B. Since No-Sensor and LS-Sensor baseline does not work on the multi-object training setup, we only compare our method with DS-Sensor. We find that disabling the sensor input will lead to a significant performance drop both in the seen and unseen object setup. This result suggests that tactile information is indeed important for generalization. 

## _E. Real: Dexterity without Vision_ 

We have seen that our tactile policy can achieve superior performance in the ideal simulation setup. Now, we transfer the trained tactile policy to the real robot and verify if it still offers 

TABLE III: Performance of different methods on the multiobject rotation task in simulation. The results are averaged on 3 seeds. 

|Method|Seen Obje|ct Setup|Unseen Object Setup|
|---|---|---|---|
||CRR|TTF|CRR<br>TTF|
|Sensor|**976.1**_±_**86.5**|**42.1**_±_**0.6**|**594.4**_±_**63.2**<br>**28.2**_±_**2.7**|
|DS-Sensor|351_._5_±_28_._0|18_._6_±_0_._7|186_._5_±_16_._1<br>10_._7_±_1_._4|



the demonstrated benefit. In real-world experiments, we train the baselines on object sets A and B and evaluate these policies on object set C. We evaluate each method using 3 different seeds for each object. The results are shown in Table I. 

Our method can outperform all the baselines. It can not only perform rotation on the seen, artificial training objects but also generalize to unseen real-world objects like apples and tomatoes. The method with continuous tactile sensor signals also performs better than the other two methods without feedback. We observe that both the no-sensor and the open-loop policy can at most rotate the object for 180 degrees on the evaluated objects, after which they will get stuck or push the object off the palm, resulting in a failure. In addition, by studying the behavior of our policy and baselines, we find that our policy can adjust the finger motion immediately when objects get to positions that are easy to get stuck or fall. In contrast, the baselines without sensors do not have such kind of adaptive behavior. This result suggests that it is crucial to have a dose of tactile feedback in the considered in-hand object manipulation setup. By comparing the methods with continuous contact signals and binarized contact signals, we find that the latter has better performance. Even though the policy with continuous signals can perform well in some objects, it has poor generalizability and huge variance between different objects. This may be due to the huge gap in force measurement between simulation and the real world. 





















Fig. 7: Visualization of contact signals in 400 steps in the simulation and real-world experiments on a cuboid. We also show some typical frames during the rotation process. We can see that the contact signals in the simulation and the real world in general align. This accounts for successful Sim2Real transfer. 

## _F. Qualitative Analysis: Sensor Response_ 

To understand why Sim2Real can be successful, we conduct a case study on cuboid rotation to analyze the sensor response. We visualize two 40 seconds test trajectories recorded in the simulation and real in Figure 7 during the test. It is worthwhile mentioning that different runs in real will produce different patterns, and we put more cases in the appendix. We find that the contact signals in the simulation are slightly denser (along the temporal x-axis) and richer (along the sensor y- axis) compared with that of the real. Some sensors are also more likely to be activated (e.g., sensors 1 and 10) in the simulation, but the overall patterns of the simulation and the real are similar. This can explain why our Sim2Real transfer is successful. Moreover, when looking at local windows used by our policy (0.4s) in simulation, we observe that there are various, diverse sensor activation patterns. We hypothesize that learning from such a diverse distribution could also help the policy to transfer to the sensor observation in the real world. 

## _G. Ablation Study I: Importance Analysis of Sensors_ 

Then, we perform ablation studies of the system on the real robot to see which sensors are more important for a successful rotation. We divide the sensors into two groups: Fingertip and Palm. We disable these two groups of sensors and train two policies (No-Fingertip and No-Palm). Then we compare them to our full policy and DS-Sensor, see Table IV. We find that neither of the two considered policies can compare to our full policy. They achieve a similar performance as DS-Sensor, which suggests that both groups of sensors are essential for the success of in-hand object rotation. 

## _H. Ablation Study II: A Shape Understanding Perspective_ 

So far, we have seen that the tactile information is essential for successful object rotation. In this part, our goal is to understand its success from a shape understanding perspective. We study whether our tactile information can reveal the shape information of the object, which may be helpful for learning 











Fig. 8: With the learned rotation primitives around _x_ , _y_ , and _z_ axis, we can perform human-robot shared control to reorient an object. In this example, a human operator uses a keyboard to rotate a cuboid around _x, y, z, y_ axes consecutively. We also visualize the contact signal throughout this 600-step process (60 seconds). 

|GT|TABLE IV: Ablation ana<br>on different sensor setu<br>results are averaged on 3<br>Method<br>Cu|lysis of the <br>ps and test <br> seeds.<br>boid|system. W<br> their perf<br>Rubb|e train policies<br>ormance. The<br>er Duck|
|---|---|---|---|---|
||CRR|TTF|CRR|TTF|
|Prediction<br>w/o touch|Sensor<br>**4.91**_±_**0.52**|**30.00**_±_**0.00**|**1.42**_±_**0.38**|**29.00**_±_**1.73**|
||DS-Sensor<br>0_._25_±_0_._25|7_._67_±_6_._80|0_._33_±_0_._29|20_._00_±_17_._32|
||No-Fingertip 0_._17_±_0_._29|3_._33_±_5_._77|0_._42_±_0_._14|17_._00_±_2_._64|
|Prediction|No-Palm<br>0_._42_±_0_._38|17_._00_±_14_._73|0_._42_±_0_._14|16_._67_±_11_._72|
|w/ touch<br>(Ours)|predict the shape of the|object using|the full ro|llout trajectory|



predict the shape of the object using the full rollout trajectory as input, and then we use the trained model to reconstruct the shape of objects in the test dataset. We compare our model to another ablated model, which discards all the tactile observation in the rollout during prediction (by setting them to 0). The shape reconstruction mean squared error (MSE) of our model is 0.22, while that of the ablated model is 0.45. This suggest that using tactile infomation can indeed help shape understanding. Moreover, we provide visualization of predicted object shapes are in Figure 9. With the tactile sensors, our model can reconstruct object shape much better than the ablated model. The shape understanding results suggest that the binarized tactile information is indeed important for the robot to percept the object and interact with it in a meaningful way. 

Fig. 9: Qualitative mesh reconstruction results in simulation. When the touch information does not present, we can not infer the shape of the rotated object accurately. In contrast, our method is able to reconstruct the groundtruth object by a 20-second rotation. 

robust and adaptive rotation behavior across different objects. Specifically, we would like to see if it is possible to predict the shape of the object using the rollout of a rotation policy. For simplicity, we focus on the _z_ -axis rotation of column-shaped objects. We first train a _z_ -axis rotation policy on 125 different irregular, column-shaped objects. Then, we use this policy to collect 55000 policy rollouts of rotating these objects, and each of these rollouts lasts 200 control steps (20 seconds). Next, we split these collected rollouts into a training dataset and a test dataset. The objects in the test dataset do not present in the training dataset. We train a temporal-CNN model to 

## _I. Rotation Around Other Axes_ 

Besides the rotation around the _z_ axis, we also test whether our system is able to perform rotation around other axes. Here, we study the rotation around the _x_ and _y_ axes. To do so, we train our policy on the object set A and B as in the previous 

TABLE V: Summary of rotation performance around different axes. We provide the averaged results over the object set on the _x_ , _y_ , and _z_ axis rotations. The results are averaged on 3 seeds. 

|Rotation|See|n|Obj|Unse|en Obj|
|---|---|---|---|---|---|
||CRR||TTF|CRR|TTF|
|_x_-axis|1_._68_±_0_._78||24_._13_±_6_._04|2_._71_±_1_._37|18_._2_±_9_._19|
|_y_-axis|1_._88_±_0_._38||22_._46_±_4_._81|1_._05_±_0_._56|23_._13_±_3_._01|
|_z_-axis|3_._43_±_1_._22||29_._06_±_1_._45|2_._48_±_1_._27|28_._73_±_1_._34|



experiments. The results are shown in Table V. We find that our system is still able to rotate most of the objects successfully, though it may have difficulty rotation some particular objects which results in lower CRAs. We observe that rotation around _x_ and _y_ axes involves many critical contacts between the object and the side of finger links. This may explain why failures can occur since the layout of our current sensor array does not support this feature. We hypothesis that a denser contact sensor array over each finger link can remedy this problem. 

The rotation around _x_ , _y_ , and _z_ axis provides a useful set of primitives. This enables human to use high-level commands to control the rotation behavior, as shown in Figure 8. In this example, A human operator presses the keyboard to send different rotation commands (i.e. around _x_ , _y_ , or _z_ ). The robot hand is then able to execute the desired rotation, reorienting the object to different poses. 

## VI. CONCLUSION 

In this paper, we have presented Touch Dexterity, a new dexterous manipulation system that is able to rotate different objects through touch without vision. We showed an endto-end reinforcement learning framework to learn dexterous manipulation skills on the proposed system. We carried out experiments both in simulation and real to demonstrate its effectiveness. Our work demonstrated that we are able to achieve touch-only dexterity as humans in real for the first time. In the future, there are many promising future directions to investigate, such as exploring the use of a more dense contact sensor array and scaling up the system to solve more diverse tasks. We hope that our work can pave the way for more intelligent robot hands. 

## REFERENCES 

- [1] Y. Aiyama, M. Inaba, and H. Inoue. Pivoting: A new method of graspless manipulation of object by robot fingers. In _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 1993. 

- [2] OpenAI: Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research (IJRR)_ , 39(1): 3–20, 2020. 

- [3] Sridhar Pandian Arunachalam, Irmak Guzey,¨ Soumith Chintala, and Lerrel Pinto. Holo-dex: Teaching dexterity with immersive mixed reality. _arXiv preprint arXiv:2210.06463_ , 2022. 

- [4] Sridhar Pandian Arunachalam, Sneha Silwal, Ben Evans, and Lerrel Pinto. Dexterous imitation made easy: A learning-based framework for efficient dexterous manipulation. _arXiv preprint arXiv:2203.13251_ , 2022. 

- [5] Yunfei Bai and C. Karen Liu. Dexterous manipulation using both palm and fingers. In _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 1560–1565, 2014. doi: 10.1109/ICRA.2014.6907059. 

- [6] Aditya Bhatt, Adrian Sieler, Steffen Puhlmann, and Oliver Brock. Surprisingly robust in-hand manipulation: An empirical study. In _Robotics: Science and Systems (RSS)_ , 2021. 

- [7] Tapomayukh Bhattacharjee, Joshua Wade, and Charles C Kemp. Material recognition from heat transfer given varying initial conditions and short-duration contact. In _Robotics: Science and Systems (RSS)_ , 2015. 

- [8] Raunaq Bhirangi, Tess Hellebrekers, Carmel Majidi, and Abhinav Gupta. Reskin:versatile, replaceable, lasting tactile skins. In _Conference on Robot Learning (CoRL)_ , 2021. 

- [9] Thomas Bi, Carmelo Sferrazza, and Raffaello D’Andrea. Zero-shot sim-to-real transfer of tactile control policies for aggressive swing-up manipulation. _IEEE Robotics and Automation Letters_ , 6(3):5761–5768, 2021. 

- [10] A. Bicchi and R. Sorrentino. Dexterous manipulation through rolling. In _Proceedings of 1995 IEEE International Conference on Robotics and Automation_ , volume 1, pages 452–457 vol.1, 1995. doi: 10.1109/ROBOT.1995. 525325. 

- [11] Gereon Buescher, Martin Meier, Guillaume Walck, Robert Haschke, and Helge J Ritter. Augmenting curved robot surfaces with soft tactile skin. In _2015 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2015. 

- [12] Nikhil Chavan-Dafle and Alberto Rodriguez. Samplingbased planning of in-hand manipulation with external pushes. In _Robotics Research: The 18th International Symposium ISRR_ , pages 523–539. Springer, 2020. 

- [13] Yevgen Chebotar, Oliver Kroemer, and Jan Peters. Learning robot tactile sensing for object manipulation. In _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2014. 

- [14] Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Edward Adelson, and Pulkit Agrawal. Visual dexterity: Inhand dexterous manipulation from depth. _arXiv preprint arXiv:2211.11744_ , 2022. 

- [15] Tao Chen, Jie Xu, and Pulkit Agrawal. A system for general in-hand object re-orientation. In _Conference on Robot Learning (CoRL)_ , pages 297–307, 2022. 

- [16] Mo¨ez Cherif and Kamal K Gupta. Planning quasi-static fingertip manipulations for reconfiguring objects. _IEEE Transactions on Robotics and Automation_ , 15(5):837–848, 

1999. 

- [17] Mo¨ez Cherif and Kamal K Gupta. Planning quasi-static fingertip manipulations for reconfiguring objects. _IEEE Transactions on Robotics and Automation_ , 15(5):837–848, 1999. 

- [18] Alex Church, John Lloyd, Nathan F Lepora, et al. Tactile sim-to-real policy transfer via real-to-sim image translation. In _Conference on Robot Learning (CoRL)_ , 2022. 

- [19] Siyuan Dong, Devesh K Jha, Diego Romeres, Sangwoon Kim, Daniel Nikovski, and Alberto Rodriguez. Tactilerl for insertion: Generalization to objects of unknown geometry. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2021. 

- [20] Neel Doshi, Orion Taylor, and Alberto Rodriguez. Manipulation of unknown objects via contact configuration regulation. In _International Conference on Robotics and Automation (ICRA)_ , 2022. 

- [21] Zoe Doulgeri and Leonidas Droukas. On rolling contact motion by robotic fingers via prescribed performance control. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2013. 

- [22] Danny Driess, Peter Englert, and Marc Toussaint. Active learning with query paths for tactile object shape exploration. In _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2017. 

- [23] Ruohan Gao, Zilin Si, Yen-Yu Chang, Samuel Clarke, Jeannette Bohg, Li Fei-Fei, Wenzhen Yuan, and Jiajun Wu. Objectfolder 2.0: A multisensory object dataset for sim2real transfer. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 10598–10608, 2022. 

- [24] Ahsan Habib, Isura Ranatunga, Kyle Shook, and Dan O Popa. Skinsim: A simulation environment for multimodal robot skin. In _IEEE International Conference on Automation Science and Engineering (CASE)_ , 2014. 

- [25] L. Han and J.C. Trinkle. Dextrous manipulation by rolling and finger gaiting. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 1998. 

- [26] Li Han, Yi-Sheng Guan, ZX Li, Q Shi, and Jeffrey C Trinkle. Dextrous manipulation with rolling contacts. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 1997. 

- [27] Li Han, Yi-Sheng Guan, ZX Li, Q Shi, and Jeffrey C Trinkle. Dextrous manipulation with rolling contacts. In _International Conference on Robotics and Automation (ICRA)_ , 1997. 

- [28] Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zhurkevich, Balakumar Sundaralingam, et al. Dextreme: Transfer of agile in-hand manipulation from simulation to reality. In _International Conference on Robotics and Automation (ICRA)_ , 2023. 

- [29] Francois R Hogan, Jose Ballester, Siyuan Dong, and Alberto Rodriguez. Tactile dexterity: Manipulation 

   - primitives with tactile feedback. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2020. 

- [30] Roland S Johansson and Goran Westling. Roles of glabrous skin receptors and sensorimotor memory in automatic control of precision grip when lifting rougher or more slippery objects. _Experimental brain research_ , 56:550–564, 1984. 

- [31] Raj Kolamuri, Zilin Si, Yufan Zhang, Arpit Agarwal, and Wenzhen Yuan. Improving grasp stability with rotation measurement from tactile sensing. In _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2021. 

- [32] Vikash Kumar, Yuval Tassa, Tom Erez, and Emanuel Todorov. Real-time behaviour synthesis for dynamic handmanipulation. In _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 6808–6815. IEEE, 2014. 

- [33] Mike Lambeta, Po-Wei Chou, Stephen Tian, Brian Yang, Benjamin Maloon, Victoria Rose Most, Dave Stroud, Raymond Santos, Ahmad Byagowi, Gregg Kammerer, et al. Digit: A novel design for a low-cost compact high-resolution tactile sensor with application to in-hand manipulation. _IEEE Robotics and Automation Letters_ , 5 (3):3838–3845, 2020. 

- [34] Michelle A. Lee, Yuke Zhu, Peter Zachares, Matthew Tan, Krishnan Srinivasan, Silvio Savarese, Li Fei-Fei, Animesh Garg, and Jeannette Bohg. Making sense of vision and touch: Learning multimodal representations for contactrich tasks, 2019. URL https://arxiv.org/abs/1907.13098. 

- [35] Qiang Li, Oliver Kroemer, Zhe Su, Filipe Fernandes Veiga, Mohsen Kaboli, and Helge Joachim Ritter. A review of tactile information: Perception and action through touch. _IEEE Transactions on Robotics_ , 36(6):1619–1634, 2020. 

- [36] Jacky Liang, Ankur Handa, Karl Van Wyk, Viktor Makoviychuk, Oliver Kroemer, and Dieter Fox. Inhand object pose tracking via contact feedback and gpuaccelerated robotic simulation. In _IEEE International Conference on Robotics and Automation (ICRA)_ , pages 6203–6209. IEEE, 2020. 

- [37] Xingyu Liu, Deepak Pathak, and Kris M Kitani. Herd: Continuous human-to-robot evolution for learning from human demonstration. _arXiv preprint arXiv:2212.04359_ , 2022. 

- [38] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

- [39] Sami Moisio, Beatriz Leon,´ Pasi Korkealaakso, and Antonio Morales. Model of tactile sensors using soft contacts and its application in robot grasping simulation. _Robotics and Autonomous Systems_ , 61(1):1–12, 2013. 

- [40] Artem Molchanov, Oliver Kroemer, Zhe Su, and Gaurav S Sukhatme. Contact localization on grasped objects using tactile sensing. In _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2016. 

- [41] Andrew S. Morgan, Kaiyu Hang, Bowen Wen, Kostas Bekris, and Aaron M. Dollar. Complex in-hand manipulation via compliance-enabled finger gaiting and multimodal planning. _IEEE Robotics and Automation Letters_ , 7(2):4821–4828, 2022. doi: 10.1109/LRA.2022.3145961. 

- [42] Adithyavairavan Murali, Yin Li, Dhiraj Gandhi, and Abhinav Gupta. Learning to grasp without seeing. In _Proceedings of the 2018 International Symposium on Experimental Robotics_ , pages 375–386. Springer, 2020. 

- [43] Vinod Nair and Geoffrey E Hinton. Rectified linear units improve restricted boltzmann machines. In _International Conference on Machine Learning (ICML)_ , 2010. 

- [44] Benjamin Navarro, Prajval Kumar, Aicha Fonte, Philippe Fraisse, Gerard´ Poisson, and Andrea Cherubini. Active calibration of tactile sensors mounted on a robotic hand. In _Intelligent RObots and Systems Workshop on Multimodal sensor-based robot control for HRI and soft manipulation_ , 2015. 

- [45] Allison M Okamura, Niels Smaby, and Mark R Cutkosky. An overview of dexterous manipulation. In _IEEE International Conference on Robotics and Automation. Symposia Proceedings_ , 2000. 

- [46] Akhil Padmanabha, Frederik Ebert, Stephen Tian, Roberto Calandra, Chelsea Finn, and Sergey Levine. Omnitact: A multi-directional high-resolution touch sensor. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 618–624. IEEE, 2020. 

- [47] Chaoyi Pan, Marion Lepert, Shenli Yuan, Rika Antonova, and Jeannette Bohg. Task-driven in-hand manipulation of unknown objects with tactile sensing. _arXiv preprint arXiv:2210.13403_ , 2022. 

- [48] Austin Patel, Andrew Wang, Ilija Radosavovic, and Jitendra Malik. Learning to imitate object interactions from internet videos. _arXiv preprint arXiv:2211.13225_ , 2022. 

- [49] Anna Petrovskaya and Oussama Khatib. Global localization of objects via touch. _IEEE Transactions on Robotics_ , 27(3):569–585, 2011. 

- [50] Johannes Pitz, Lennart Rostel, Leon Sievers, and Berthold¨ Bauml.¨ Dextrous tactile in-hand manipulation using a modular reinforcement learning architecture. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2023. 

- [51] Haozhi Qi, Ashish Kumar, Roberto Calandra, Yi Ma, and Jitendra Malik. In-hand object rotation via rapid motor adaptation. In _Conference on Robot Learning (CoRL)_ , 2022. 

- [52] Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, and Xiaolong Wang. Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. In _Conference on Robot Learning (CoRL)_ , 2022. 

- [53] Yuzhe Qin, Hao Su, and Xiaolong Wang. From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation. _IEEE Robotics and Automation Letters_ , 7(4):10873–10881, 

2022. 

- [54] Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision (ECCV)_ , 2022. 

- [55] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. In _Robotics: Science and Systems (RSS)_ , 2018. 

- [56] Daniela Rus. In-hand dexterous manipulation of piecewise-smooth 3-d objects. _The International Journal of Robotics Research (IJRR)_ , 18(4):355–381, 1999. 

- [57] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. _arXiv preprint arXiv:1506.02438_ , 2015. 

- [58] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 

- [59] Jian Shi, J. Zachary Woodruff, Paul B. Umbanhowar, and Kevin M. Lynch. Dynamic in-hand sliding manipulation. _IEEE Transactions on Robotics_ , 33(4):778–795, 2017. 

- [60] Zilin Si and Wenzhen Yuan. Taxim: An example-based simulation model for gelsight tactile sensors. _IEEE Robotics and Automation Letters_ , 7(2):2361–2368, 2022. 

- [61] Leon Sievers, Johannes Pitz, and Berthold Bauml.¨ Learning purely tactile in-hand manipulation with a torquecontrolled hand. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2022. 

- [62] Edward Smith, David Meger, Luis Pineda, Roberto Calandra, Jitendra Malik, Adriana Romero Soriano, and Michal Drozdzal. Active 3d shape reconstruction from vision and touch. _Advances in Neural Information Processing Systems_ , 34:16064–16078, 2021. 

- [63] Paloma Sodhi, Michael Kaess, Mustafa Mukadanr, and Stuart Anderson. Patchgraph: In-hand tactile tracking with learned surface normals. In _International Conference on Robotics and Automation (ICRA)_ , 2022. 

- [64] Sudharshan Suresh, Maria Bauza, Kuan-Ting Yu, Joshua G Mangelson, Alberto Rodriguez, and Michael Kaess. Tactile slam: Real-time inference of shape and pose from planar pushing. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 2021. 

- [65] Sudharshan Suresh, Zilin Si, Stuart Anderson, Michael Kaess, and Mustafa Mukadam. Midastouch: Monte-carlo inference over distributions across sliding touch. In _Conference on Robot Learning (CoRL)_ , 2022. 

- [66] Ian H Taylor, Siyuan Dong, and Alberto Rodriguez. Gelslim 3.0: High-resolution measurement of shape, force and slip in a compact tactile-sensing finger. In _International Conference on Robotics and Automation (ICRA)_ , 2022. 

- [67] Stephen Tian, Frederik Ebert, Dinesh Jayaraman, Mayur Mudigonda, Chelsea Finn, Roberto Calandra, and Sergey 

Levine. Manipulation by feel: Touch-based control with deep predictive models. In _International Conference on Robotics and Automation (ICRA)_ , 2019. 

- [68] Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. In _IEEE/RSJ international conference on intelligent robots and systems (IROS)_ , 2017. 

- [69] Pierre Tournassoud, Tomas´ Lozano-Perez,´ and Emmanuel Mazer. Regrasping. In _IEEE International Conference on Robotics and Automation (ICRA)_ , 1987. 

- [70] Herke Van Hoof, Nutan Chen, Maximilian Karl, Patrick van der Smagt, and Jan Peters. Stable reinforcement learning with autoencoders for tactile and visual data. In _IEEE/RSJ international conference on intelligent robots and systems (IROS)_ , 2016. 

- [71] Yueh-Hua Wu, Jiashun Wang, and Xiaolong Wang. Learning generalizable dexterous manipulation from human grasp affordance. In _Conference on Robot Learning (CoRL)_ , 2022. 

- [72] Jie Xu, Sangwoon Kim, Tao Chen, Alberto Rodriguez Garcia, Pulkit Agrawal, Wojciech Matusik, and Shinjiro Sueda. Efficient tactile simulation with differentiability for robotic manipulation. In _Conference on Robot Learning (CoRL)_ . 

- [73] Jingxi Xu, Shuran Song, and Matei Ciocarlie. Tandem: Learning joint exploration and decision making with tactile sensors. _IEEE Robotics and Automation Letters_ , 7 (4):10391–10398, 2022. 

- [74] Jianglong Ye, Jiashun Wang, Binghao Huang, Yuzhe Qin, and Xiaolong Wang. Learning continuous grasping function with a dexterous hand from human demonstrations. _arXiv preprint arXiv:2207.05053_ , 2022. 

- [75] Wenzhen Yuan, Siyuan Dong, and Edward H Adelson. Gelsight: High-resolution robot tactile sensors for estimating geometry and force. _Sensors_ , 17(12):2762, 2017. 

- [76] Xinghao Zhu, Siddarth Jain, Masayoshi Tomizuka, and Jeroen Van Baar. Learning to synthesize volumetric meshes from vision-based tactile imprints. In _International Conference on Robotics and Automation (ICRA)_ , 2022. 

APPENDIX 

## _A. System Video Demo_ 

We provide a video demo of our system at http:// touchdexterity.github.io. The raw video demo can also be founded in the submitted files. 

## _B. PPO Training Hyperparameters_ 

We use the proximal policy optimization (PPO) algorithm to train our control policy. The setup of the PPO algorithm is as follows. We use an advantage clipping coefficient _ϵ_ = 0 _._ 2. We use a horizon length of 16, with _γ_ = 0 _._ 99 and generalized advantage estimator (GAE) [57] coefficient _τ_ = 0 _._ 95. The policy network is a three-layer MLP with ELU activation. Its hidden layer is [512, 256, 256]. The policy network’s learning rate is set to 1e-4, with an adaptive KL threshold of 0.02. The value network is a four-layer MLP with ELU activation. Its hidden layer is [512, 512, 256, 256]. The value network’s learning rate is set to 5e-4, with an adaptive KL threshold of 0.016. We normalize the state input, value, and advantage during training. We use a gradient norm of 1.0. The minibatch size is set to 16384. 



Fig. 10: Contact sensor map. 

## **Falling Reward (Penalty)** 



## _C. Improving Sim2Real Transfer_ 

**Domain Randomization** We use several domain randomization techniques to improve the Sim2Real transfer. The details are shown in Table VI. 

TABLE VI: Domain Randomization Setup 

|Object: Mass (kg)|[0.2, 0.6]|
|---|---|
|Object: Friction|[0.3, 3.0]|
|Object: Shape|_×U_(0_._95_,_1_._05)|
|Object: Initial Position (cm)<br>|+_U_(_−_0_._015_,_0_._015)|
|Hand: Friction|[0.3, 3.0]|
|PD Controller: P Gain|_×U_(0_._66_,_1_._33)|
|PD Controller: D Gain|_×U_(0_._80_,_1_._20)|
|Sensor: Lag Probability|0.25|
|Sensor: Drop Rate|0.1|
|Random Force: Scale|0.2|
|Random Force: Probability|[0.2, 0.25]|
|Random Force: Decay Coeff. and Interval|0.99 every 0.1s|
|Joint Observation Noise.|+_U_(_−_0_._05_,_0_._05)|
|Action Noise.|+_U_(_−_0_._06_,_0_._06)|



**System Identification** We apply system identification to align the behavior of the PD controller in simulation to that in the real. We tune the PD coefficients to ensure that the responses of the controllers to the impulse and sinusoidal inputs are aligned. We find this step crucial for successful Sim2Real transfer. 





## **Torque Reward (Penalty)** 



## **Distance Reward** 

_rdist_ = mean _i_ =0 _,_ 1 _,_ 2 _,_ 3(clip(0 _._ 1 _/_ (0 _._ 02 + 4 _d_ ( _x_<sup>_i_</sup> _tip_<sup>_, xobj_))</sup><sup>_,_0</sup><sup>_,_1))</sup><sup>_._</sup> (8) 

The overall reward function is 

_rt_ = _w_ 1 _rrot_ + _w_ 2 _rvel_ + _w_ 3 _rfall_ + _w_ 4 _rwork_ + _w_ 5 _rtorque_ + _w_ 6 _rdist._ (9) 

The setup of each weight: _w_ 1 = 20 _._ 0 _, w_ 2 = 0 _._ 1 _, w_ 3 = 1 _._ 0 _, w_ 4 = 0 _._ 0003 _, w_ 5 = 0 _._ 0003 _, w_ 6 = 0 _._ 1. 

## _E. More Sensor Response Examples_ 

We show more examples of sensor activation trajectories collected in real-world experiments in Figure 11. These trajectories are collected on different objects. We can observe different activation patterns in the trajectories. 

## _D. Reward Design_ 

## **Rotation Reward** 



## **Velocity Reward** 

































Fig. 11: More sensor activation trajectories in the real world experiments. The curves are collected on different objects and display different patterns. 

