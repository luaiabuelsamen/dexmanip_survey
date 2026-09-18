# MuJoCo Playground 

- Kevin Zakka<sup>_∗,_1</sup> , Baruch Tabanpour<sup>_∗,_2</sup> , Qiayuan Liao<sup>_∗,_1</sup> , Mustafa Haiderbhai<sup>_∗,_3</sup> , Samuel Holt<sup>_∗,_4</sup> , Jing Yuan Luo<sup>2</sup> , Arthur Allshire<sup>1</sup> , Erik Frey<sup>2</sup> , Koushil Sreenath<sup>1</sup> , Lueder A. Kahrs<sup>3</sup> , Carmelo Sferrazza<sup>_†,_1</sup> , Yuval Tassa<sup>_†,_2</sup> , and Pieter Abbeel<sup>_†,_1</sup> 

> 1UC Berkeley 2Google DeepMind 3University of Toronto 4University of Cambridge 

> _∗_ Equal contributions _†_ Equal advising 



Fig. 1: A cartoon of MuJoCo Playground’s diverse environments that were successfully transferred to real hardware, including Berkeley Humanoid, Unitree Go1 and G1, LEAP hand and Franka Arm. 

**_Abstract_ —We introduce MuJoCo Playground, a fully opensource framework for robot learning built with MJX, with the express goal of streamlining simulation, training, and simto-real transfer onto robots. With a simple pip install playground, researchers can train policies in minutes on a single GPU. Playground supports diverse robotic platforms, including quadrupeds, humanoids, dexterous hands, and robotic arms, enabling zero-shot sim-to-real transfer from both state and pixel inputs. This is achieved through an integrated stack comprising a physics engine, batch renderer, and training environments. Along with video results, the entire framework is freely available at mujocoplayground.github.io.** 

### I. INTRODUCTION 

Reinforcement learning (RL) [27] with subsequent transfer to hardware (sim-to-real) [69], is emerging as a leading paradigm in modern robotics [26, 30, 40]. The benefits of simulation are obvious – safety and cheap data. The recipe involves four steps: 

- 1) Create a simulated environment that matches the real world. 

- 2) Encode desired robot behavior with a reward function. 

- 3) Train a policy in simulation. 

- 4) Deploy to the robot. 

The key enabler of this approach is a simulator that is realistic, convenient, and fast. 

The realism requirement is self-evident, the “digital twin” of step 1 demands a minimal level of fidelity [69]. Convenience and usability are equally critical, streamlining the creation, modification, composition, and characterization (system identification) of simulated robots. 

The importance of speed is less obvious – why does it matter if training takes ten minutes or ten hours? The answer lies in reward design (step 2), which cannot be easily automated: what the robot _ought_ to do is an expression of human 

preference. Even if reward design is semi-automated [37], the process remains iterative: RL excels at finding policies that obtain reward, but the resulting behavior is often irregular in unexpected ways. Since steps 2 and 3 (and occasionally step 4) must be repeated [7], _time-to-robot_ becomes critical: the time from when you ask the robot to do something until you see what it thinks you meant. 

RL is computationally intensive, requiring an enormous number of agent-environment interactions to train effective policies [24]. GPU-based simulation can significantly accelerate this process for two key reasons. First, the median GPU is far more powerful than the median CPU [65], and while high core-count CPUs exist, they are uncommon. Second, by keeping the entire agent-environment loop on device, we can harness the high-throughput, highly parallel architecture [13, 39]. This is especially true for _on-policy_ RL [3, 51], which employs GPU-friendly, wide-batch operations. Locomotion and manipulation tasks which previously required days of training on multi-host setups [4, 59], can now be solved within minutes or hours on a single GPU [19, 50]. 

With this work, we aim to further advance and make simto-real robot learning even more accessible. We introduce MuJoCo Playground, a fully open-source framework for robot learning designed for rapid iteration and deployment of sim-toreal reinforcement learning policies. We build upon MuJoCo XLA [43] (MJX), a JAX-based branch of the MuJoCo physics engine that runs on GPU, enabling training directly on device. Besides physics and learning, we leverage the open-source nature of our ecosystem to incorporate on-device rendering through the Madrona batch renderer [53], facilitating training of vision-based policies end-to-end, without teacher-student distillation [1]. With a straightforward installation process (pip install playground) and cross-platform support, users can quickly train policies on a single GPU. The entire pipeline—from environment setup to policy optimization— can be executed in a single Colab notebook, with most tasks requiring only minutes of training time. 

MuJoCo Playground’s lightweight implementation greatly simplifies sim-to-real deployment, transforming it into an interactive process where users can quickly tweak parameters to refine robot behavior. In our experiments, we deployed both state- and vision-based policies across six robotic platforms in less than eight weeks. We hope that MuJoCo Playground becomes a valuable resource for the robotics community and expect it to continue building on MuJoCo’s thriving opensource ecosystem. 

Our work makes three main contributions: 

- 1) We develop a comprehensive suite of robotic environments using MJX [43], demonstrating sim-to-real transfer across diverse platforms including quadrupeds, humanoids, dexterous hands, and robot arms. 

- 2) We integrate the open-source Madrona batch GPU renderer [53] to enable end-to-end vision-based policy training on a single GPU device, achieving zero-shot transfer on manipulation tasks. 

- 3) We provide a complete, reproducible training pipeline 

with notebooks, hyperparameters, and training curves, enabling rapid iteration between simulation and realworld deployment. 

### II. ENVIRONMENTS 

MuJoCo Playground contains environments in 3 main categories: DeepMind (DM) Control Suite, Locomotion, and Manipulation, which we briefly describe in this section. Locomotion and manipulation environments are tailored to robotic use-cases and we show zero-shot sim-to-real transfer in many of the available environments. Playground directly utilizes MuJoCo Menagerie [68] which offers a suite of robot assets and configurations tailored to run in MuJoCo. 

### _A. DM Control Suite_ 

The majority of RL environments from [61] are reimplemented in MJX, and serve as entry-level tasks to familiarize users with MuJoCo Playground (Figure 3). 

### _B. Locomotion_ 

Locomotion environments in MuJoCo Playground are implemented for multiple quadrupeds and bipeds (Figure 2 left). The quadrupeds include the Unitree Go1, Boston Dynamics Spot, and Google Barkour [6], while the humanoids include the Berkeley Humanoid [35], Unitree H1 and G1, Booster T1, and the Robotis OP3. For each robot embodiment, we implement a joystick environment that learns to track a velocity command consisting of base linear velocities in both the forward and lateral directions, as well as a desired yaw rate. On the Unitree Go1, we additionally implement fall recovery and handstand environments. A complete list of locomotion environments is provided in Table V in the appendix. 

We demonstrate sim-to-real transfer in two main sets of experiments. First, on the Unitree Go1, we deploy joystick, fall recovery, and handstand policies. Second, we demonstrate joystick-based locomotion on the Berkeley Humanoid, the Unitree G1, and the Booster T1. More details on these simto-real experiments can be found in Section IV-B. 

### _C. Manipulation_ 

Manipulation environments in MuJoCo Playground are implemented for both prehensile and non-prehensile tasks (Figure 2 right). With the Leap Hand [56] robot, we demonstrate contact-rich dexterous re-orientation of a block. Using the Franka Emika Panda and Robotiq gripper, we show reorientation of a yoga block using high frequency torque control. We implement a simple vision-based pick-cube environment on a Franka arm using the Madrona batch renderer. A few additional environments, such as bi-arm peg-insertion with the Aloha robot [2], are also available. We refer to Table VIII in the appendix for a full set of environments. 

We demonstrate sim-to-real transfer on the Leap Hand and Franka arm robots, including an environment trained from vision for the pick-cube task. More details on the sim-to-real experiments are available in Section IV-C. 



Fig. 2: A preview of locomotion and manipulation environments available in MuJoCo Playground. 

### III. BATCH RENDERING WITH MADRONA 

MuJoCo Playground enables vision-based environments through an integration of MJX with Madrona [54]. Madrona is a GPU-based entity-component-system (ECS), which contains GPU implementations of high throughput rendering [49]. Madrona provides two rendering backends: a software-based batch ray tracer written in CUDA (used for the experiments in this work) and a Vulkan-based rasterizer. The raytracing backend supports features including complex lighting scenarios, shadows, textures, and geometry materials. See Figure 4 for examples of rendered images using the batch ray tracer. Some features such as deformable materials, moving lights, and terrain height fields will be added in the future. 

The Madrona Batch Renderer is integrated with MJX through low-level JAX [5] primitives that connect to the initialization and render functions exposed by Madrona. These JAX primitives allow for Madrona to interact seamlessly with JAX transformations such as _jit_ and _vmap_ . Mujoco Playground provides two examples: (cartpole-balance and PandaPickCubeCartesian) to showcase the implementation of vision-based environments and training of visionbased policies. 

The Madrona MJX integration also supports customization of each environment instance, allowing for domain randomization [62] of visual properties such as geometry size, color, lighting conditions, and camera pose. These randomizations play a crucial role in the sim-to-real transfer of vision-based policies, which we discuss more in Section IV-C3. 

### IV. RESULTS 

In this section, we report RL and sim-to-real results for environments in MuJoCo Playground. Sim-to-real experiments (see some examples in Figure 5) are performed for locomotion and manipulation environments from both proprioceptive state 

and from vision. We briefly discuss RL training on different hardware devices and RL libraries. 

### _A. DM Control Suite_ 

We train state-based policies for all available tasks, with most environments training in under 10 minutes on a single GPU device. More details on the training process can be found in Section A.2. All available environments in the MJX port of the DM Control Suite, including any modifications, are detailed in Section A.1. 

Using the batch renderer, we also implement pixel-based observations for the CartpoleBalance environment. These observations are generated on the GPU, allowing us to keep physics, rendering, and training entirely on-device. Although other DM Control Suite environments can also be rendered with Madrona, we demonstrate end-to-end RL training on only one task, leaving a more comprehensive exploration for future work. Section D provides more information on how CartpoleBalance was modified and trained for pixel observations. 



Fig. 3: Several DM Control Suite environments. 

### _B. Locomotion_ 

We present sim-to-real locomotion results on both a quadruped (Unitree Go1) and three humanoid platforms (Berkeley Humanoid,Unitree G1, and Booster T1). Further details on the MDP formulation, including rewards, observation spaces, and action spaces, are provided in Section B. 



Fig. 4: Sample renders from the Madrona batch renderer for the Panda and Aloha environments. Left-most images are the original environments. The remaining images highlight the the support for lighting, shadows, textures, and colors, including the ability to domain randomize these parameters during training. 

### _1) Quadruped Locomotion:_ 

_a) Task definition:_ We implement a joystick locomotion task as in [25, 50], where the command is specified by three values indicating the desired forward velocity, lateral velocity, and turning rate of the robot’s root body. Additionally, we design policies for handstand and footstand tasks, in which the robot balances on the front or hind legs, respectively, while minimizing actuator torque. For fall recovery, we follow [30, 58], enabling the robot to return to a stable “home” posture from arbitrary fallen configurations. 

_b) Hardware:_ We deploy on the _Unitree Go1_ , which is a quadruped robot with four legs, each possessing three degrees of freedom. Trained policies run on real-world outdoor terrain (grass and concrete) and indoor surfaces with different friction properties. 

_c) Training:_ We domain randomize for sensor noise, dynamics properties and task uncertainties. We firstly train the policy in flat ground with restricted command ranges within 5 minutes (2x RTX 4090). and finetune it in rough terrain with wider ranges. See Section B for more detail. 

_d) Results:_ All four policies (joystick, handstand, footstand, and fall recovery) transfer robustly from simulation to reality, coping with uneven terrain and moderate external perturbations without additional fine-tuning. Videos of these deployments are provided on our project website. 

_2) Humanoid Locomotion:_ 

_a) Task definition:_ We implement the same joystick locomotion task as shown for the quadruped environment. 

_b) Hardware:_ We perform sim-to-real experiments on three different humanoid platforms: a) _Berkeley Humanoid_ [35], a low-cost, lightweight bipedal robot with 6 DoF per leg, b) _Unitree G1_ , a humanoid robot featuring 29 DoF in total, and c) _Booster T1_ , a small-scale humanoid robot with 23 Dof. All systems are evaluated in indoor environments, with slight variations in surface friction and ground compliance. 

_c) Training:_ We follow the domain randomization and finetuning strategies of the quadruped robot. Training on flat ground lasts under 15 minutes for the Berkeley Humanoid, and under 30 minutes for the Unitree G1 and the Booster T1 on two RTX 4090. 

_d) Results:_ We successfully deploy joystick-based locomotion on the Berkeley Humanoid, demonstrating robust tracking of velocity commands on surfaces ranging from rigid floors to soft and slippery terrains. On the Unitree G1 and Booster T1, our zero-shot policy similarly achieves stable walking and turning on standard indoor floors. Although minor tuning for each platform’s unique dynamics may further enhance performance, these results confirm that our approach generalizes across a range of legged robot morphologies. 

### _C. Manipulation_ 

In this section, we present sim-to-real results for a broad range of manipulation tasks, including dexterous in-hand manipulation, non-prehensile manipulation, and vision-based grasping. These tasks illustrate Playground’s ability to address a diverse segment of the manipulation spectrum and highlight its robust deployment in real-world settings. 

_1) In-Hand Cube Reorientation:_ 

_a) Task definition:_ We implement an in-hand cube reorientation task using the low-cost, dexterous LEAP hand platform [56], closely following previous works on in-hand manipulation [4, 19]. The task involves reorienting a 7 cm cube repeatedly from random initial poses to new target orientations in SE(3) without dropping it. Further task details are provided in Section C.4. 

_b) Hardware:_ We employ the same hardware configuration as in [32], mounting the LEAP hand on an 80/20 frame with a 3D-printed bracket that tilts the palm downward by 20°. A single Intel RealSense D415 camera, positioned above the workspace, provides pose estimates of the cube via a pretrained detector [19]. Although occlusions can introduce observation noise, we leave multi-camera extensions to future work. The policy operates at 20 Hz, which remains comfortably below the USB-Dynamixel control bandwidth. 

_c) Training:_ To promote sim-to-real transfer, we apply domain randomization on the robot parameters as well as cube mass and friction. We also include sensor noise, and we finetune with a progressive curriculum to increase both noisy pose estimates and action regularization. The policy trains within 30 min on two RTX 4090 GPUs. Further training details are provided in Section C.4. 

_d) Results:_ As summarized in Table I, our learned policy demonstrates early signs of robust in-hand reorientation with MuJoCo Playground. The most frequent failure occurs when 



Fig. 5: Footage from four of our deployed policies. a) Go1 joystick policy recovering from a kick while travelling at _∼_ 2m/s, b) Berkeley humanoid joystick policy tracking an angular velocity command on a slippery surface. c) In-Hand Cube Reorientation transitioning between two target poses. d) Non-prehensile policy issuing torque commands to rotate a block by 180 degrees. 

TABLE I: In-hand reorientation results on the LEAP hand over 10 trials, reporting the number of consecutive successful rotations before failure. The final two columns show the median and mean of the #Rotations metric. 

||||||**Tri**|**al**||||**Summ**|**ary**|
|---|---|---|---|---|---|---|---|---|---|---|---|
||1|2|3|4|5|6|7<br>8|9|10|Median|Mean|
|# Rotations|3|27|8|2|15|3|4<br>1|3|5|**3.5**|**7.1**|



the cube becomes wedged in the space present between the fingers and the palm of the LEAP hand, causing the policy to stall. Although less common, we also observe accidental interlocking of the index and thumb, attributed to physical flex in the low-cost hardware. Videos of real-world deployments can be found on our project page. We note that improved camera coverage and more accurate collision geometries could mitigate these edge-case failures, which we leave for future work. 

_2) Non-Prehensile Block Reorientation:_ 

_a) Task definition:_ We present a sim-to-real setup for non-prehensile reorientation of a yoga block on a commonly available Franka Emika Panda robot arm with a Robotiq gripper, achieving high zero-shot success. The task involves moving a yoga block from a random initial pose in the robot’s workspace to a fixed goal pose. A trial is deemed successful if the agent reorients the block within 3 cm of the goal position and within 10° of the desired orientation. 

_b) Hardware:_ The policy receives estimates of the block’s position and orientation from an open-source camera 

tracker [44]. We use direct high-frequency torque control at 200 Hz, where the RL policy outputs motor torques for the arm’s seven joints (with the gripper closed). By learning to control torques rather than joint positions, the agent develops smooth, compliant behavior that transfers effectively to hardware, delivering superior performance even when direct torque control at high frequencies poses learning challenges [22]. This recipe, therefore, holds broad value for practitioners. 

_c) Training:_ Robust zero-shot transfer is enabled by stochastic delays and progressive curriculum learning. Each training episode injects randomization into initial poses, joint positions, and velocities, while also imposing action and observation stochastic delays to mirror practical hardware latency. A simple curriculum gradually increases the block’s displacement and orientation range upon each success, preventing overfitting to easier conditions. Training takes 10 minutes on 16x A100 devices. 

_d) Results:_ These techniques, combined with 200 Hz direct torque control, produce a policy resilient to real-world perturbations. The agent reliably reorients the block on hardware with no additional fine-tuning as shown in Table II. Videos of real-world deployments are provided on our project website. Additional implementation details are given in Section C.5. 

_3) Pick-Cube from Pixels:_ 

_a) Task definition:_ We demonstrate sim-to-real transfer with pixel-based policies on a Franka Emika Panda robot. The robot must reliably grasp and lift a small 2 _×_ 2 _×_ 3 cm block from a random location on the table and move it 10 cm above 

TABLE II: Sim-to-real reorientation performance on the Franka Emika Panda robot, evaluated across 35 hardware trials. Each metric is reported as the median and mean (with a 95% confidence interval). The success rate is bolded to highlight final task performance. The training was done on 16x A100 GPUs. 

|Metric|Median|Mean ± 95% Confidence Interval|
|---|---|---|
|**Real Success (%)** _↑_|**100**|**85.7 ± 12.2**|
|Position Error (cm) _↓_|1.95|5.28 ± 3.26|
|Rotation Error (°) _↓_|1.72|3.32 ± 1.59|



the surface. The policy receives a 64 _×_ 64 RGB image as input and outputs a Cartesian command, which is processed by a closed-form inverse kinematics solution to yield joint commands. To simplify the task, we restrict the end-effector to a 2D Y-Z plane (while always pointing downward) and provide a binary jaw open/close action. 

_b) Hardware:_ We use a Franka Emika Panda robot with a single Intel RealSense D435 camera mounted to capture topdown RGB images. The policy operates at 15 Hz, and we run inference on an RTX 3090 GPU. Our setup ensures that the block starts within the field of view over a 20 cm range along the y-axis. 

_c) Training:_ To bridge the sim-to-real gap, we apply domain randomization across visual properties such as lighting, shadows, camera pose, and object colors. We also add random brightness post-processing, and introduce a stochastic gripping delay of up to 250 ms. We choose a reduced action dimension of three (Y-movement, Z-movement, and discrete jaw control) for training sample efficiency, but we have found that the task can also be solved in full Cartesian or joint space given additional camera perspectives and more training samples. Training in simulation takes ten minutes on a single RTX 4090. 

_d) Results:_ Our policy achieves a 100% success rate in 12 real-world trials, robustly grasping the block and lifting it clear of the table. It demonstrates resilience to moderate variations in lighting and minor camera shaking, as shown in the videos on our project website. These findings highlight MuJoCo Playground’s capacity for training pixel-based policies that transfer reliably to real hardware in a zero-shot manner. Additional implementation details are described in Section D. 

### _D. Training Throughput_ 

Across our sim-to-real studies, we used several GPU hardware setups and topologies, including NVIDIA RTX 4090, A100, and H100 GPUs. In Figure 6, we break down the training performance of the LeapCubeReorient environment on different configurations for a fixed set of RL hyper-parameters, demonstrating that MJX is effective on both consumer-grade and datacenter graphics cards. We see that GPUs with higher theoretical performance and larger topologies can reduce training time by a factor of 3x on a contact-rich task like in-hand reorientation. We leave optimization of topology-specific hyperparameters as future work (e.g. the number of environments should ideally increase for larger topologies to maximize throughput, as long as the RL algorithm can utilize the increase in data per epoch). In Table IV, Table VII, and Table IX 



<!-- Start of picture text -->
LeapCubeReorient<br>500<br>400<br>300<br>200 1x 4090<br>2x 4090<br>100 1x H100<br>8x H100<br>0<br>0 500 1000 1500 2000<br>Wallclock Time (s)<br>Episode Reward<br><!-- End of picture text -->

Fig. 6: Training wallclock time for LeapCubeReorient on different GPU device topologies. 1x 4090 takes _∼_ 2080 (s) to train and 8x H100 takes _∼_ 670 (s) to train. All runs use the _same hyperparams_ (e.g. 8192 num envs); we leave tuning hyperparams per topology as a future exercise. 



<!-- Start of picture text -->
CartpoleBalance PandaPickCubeCartesian<br>4e5<br>3e4<br>3e5<br>2e4<br>2e5<br>1e5 1e4<br>4.4e4 1.9e4<br>0 0<br>64 128 256 512 64 128 256 512<br>Image Resolution Image Resolution<br>FPS<br><!-- End of picture text -->

Fig. 7: Environment steps per second on the single-camera CartpoleBalance and PandaPickCubeCartesian environments with pixel-based observations from our on-device renderer. 

in the appendix, we report RL training throughput for all environments in MuJoCo Playground on a single A100 GPU. 

_1) Training Throughput with Batch Rendering:_ Figure 7 highlights the throughput of stepping two of our environments with pixel observations at different resolutions. By pairing MJX physics with Madrona batch rendering, our Cartpole and Franka environments unroll at roughly 403,000 and 37,000 steps per second respectively. Note that our Franka physics are over 20x more costly than Cartpole’s, resulting in the lower sensitivity of FPS to image resolution. 

Computationally, pixel-based policy training generally involves four main components: physics simulation, observation rendering, policy inference and policy updates. Figure 7 only encapsulates the former two and is not fully indicative of overall training throughput. 

We find that in the context of a PPO training loop, physics, rendering, and inference together only comprise 9% and 43% of the Cartpole and Franka total training times, respectively, with most of the time spent updating the expensive CNN-based 



<!-- Start of picture text -->
PPO on Go1JoystickFlatTerrain<br>20<br>10 RSL-RL<br>brax<br>0<br>0 20 40 60 80 100<br>Steps (1e6)<br>Episode Reward<br><!-- End of picture text -->

Fig. 8: Reward curves for PPO trained with RSL-RL and brax on an RTX-4090 GPU for 3 seeds each on the Unitree Go1. 

networks. Hence, compared to traditional on-policy training pipelines, we have shifted our bottleneck from collecting data to processing it. Training bottlenecks are further discussed in Section D.3 under Table X and Table XI. Further performance benchmarking and a rough comparison against prior simulators are in Section D.2. 

_2) RL Libraries:_ While MuJoCo Playground primarily uses a JAX-based physics simulator, practitioners are able to use both JAX and torch-based RL libraries for training RL agents. In Figure 8, we show reward curves for PPO agents trained using both Brax [13] and RSL-RL [31] implementations. Each corresponding RL library is trained with custom hyperparameters tailored to the corresponding PPO implementation. Both libraries are able to achieve successful rewards and gaits within similar wallclock times. All other results in this paper were obtained using the Brax PPO and SAC implementations. 

### V. RELATED WORK 

_a) Physics simulation on GPU:_ The PhysX GPU implementation [34] has been heavily relied on for robotic sim-to-real workloads via IsaacGym [39] and more recently Isaac Lab [41]. The PhysX GPU implementation, however, is closed-source [34] and researchers lack the ability to extend the simulator for their specific tasks or workloads. Several GPU-based physics engines are open-source, such as MJX [43, 63], Brax [13], Warp [38], and Taichi [23]. Only a limited set of robot environments [52, 66] leverage these opensource counterparts, in contrast to the wide range of robotic sim-to-real results that were achieved with IsaacGym and Isaac Lab. Most recently, Genesis [14] provides a rigid-body implementation similar to MJX implemented using Taichi, that allows for dynamic constraints/contacts. However, sim-to-real results are still limited to a few locomotion policies. 

_b) Sim-to-real RL:_ A variety of locomotion and manipulation policies have successfully been deployed in the real world zero-shot [9, 10, 33, 36, 47, 57, 70]. We complement these results by demonstrating zero-shot sim-to-real on the Leap Hand, Unitree Go1, Berkeley Humanoid, Unitree G1, 

Booster T1, and Franka arm using MuJoCo rather than closedsource simulators. Similar to [39, 41], we provide code for environments and training. 

_c) Vision-based RL:_ State-of-the-art algorithms such as DrQ [67], RL from Augmented Data (RAD) [29], Dreamerv3 [17], TD-MPC2 [20], and EfficientZeroV2 [64] have pushed pixel-based RL performance over the years. Transferring these advances to the real world is appealing, as visual control loops offer precise positioning and robust behaviour in uncontrolled in-the-wild scenarios [18]. The limitation of training directly from pixel data is the large visual sim-to-real gap between simulation and reality, which is often overcome using domain randomization [62]. However, such training methods require exponentially more training samples. As as result, policies are typically trained with proprioceptive observations in simulation and subsequently distilled into vision-based policies offline [8, 9, 16], or trained with smaller exteroceptive observations [1, 40]. With Madrona, we are able to train vision-based policies directly in simulation without a distillation step using high-throughput batch rendering, similar to [41] and [60]. 

### VI. LIMITATIONS 

MuJoCo Playground inherits the limitations of MJX due to constraints imposed by JAX. First, just-in-time (JIT) compilation can be slow (1-3 minutes on Playground’s tasks). Second, computation time related to contacts does not scale like the number of _active_ contacts in the scene, but like the number of _possible_ contacts in the scene. This is due to JAX’s requirement of static shapes at compile time. This limitation can be overcome by using more flexible frameworks like Warp [38] and Taichi [14]. This upgrade is an active area of development. Finally we should note that the vision-based training using Madrona is still at an early stage. 

### VII. CONCLUSION 

MuJoCo Playground is a library built upon the opensource MuJoCo simulator and Madrona batch renderer with implementations across several reinforcement learning and robotics environments. We demonstrate policy training on various GPU topologies using JAX and pytorch-based reinforcement learning libraries. We also demonstrate sim-to-real deployment on several robotic tasks and embodiments, from locomotion to both dexterous and non-prehensile manipulation from proprioceptive state and from pixels. We look forward to seeing the community put this resource to use in advancing robotics research and its applications. 

### ACKNOWLEDGMENTS 

We thank Jimmy Wu, Kyle Stachowicz, Kenny Shaw, and Zhongyu Li for help with hardware. We thank Dongho Khang and Yunhao Cao for help with locomotion. We thank Rushrash Hari for help with hardware. We thank Luc Guy Rosenzweig, Brennan Shacklett and Kayvon Fatahalian for their extensive support in integrating the Madrona project into MJX. We thank Ankur Handa for help with manipulation. We thank Laura Smith and Philipp Wu for always being there to help with any 

problem and answer any question. We thank Lambda labs for sponsoring compute for the project. We thank Stone Tao for discussions on manipulation environments in MJX. We thank Erwin Coumans for introducing us to the Madrona team. We thank Kevin Bergamin and Michael Lutter for fruitful technical discussions and paper draft feedback. We thank Brent Yi for fruitful technical discussions and help with the website. We thank Lambda Labs for supporting this project with cloud compute credits. 

This work is supported in part by The AI Institute. K. Sreenath has financial interest in Boston Dynamics AI Institute LLC. He and the company may benefit from the commercialization of the results of this research. 

This work was supported in part by the ONR Science of Autonomy Program N000142212121 and the BAIR Industrial Consortium. Pieter Abbeel holds concurrent appointments as a Professor at UC Berkeley and as an Amazon Scholar. This paper describes work performed at UC Berkeley and is not associated with Amazon. 

### REFERENCES 

- [1] Ananye Agarwal, Ashish Kumar, Jitendra Malik, and Deepak Pathak. Legged locomotion in challenging terrains using egocentric vision. In _Conference on robot learning_ , pages 403–415. PMLR, 2023. 

- [2] Jorge ALOHA 2 Team, Aldaco, Travis Armstrong, Robert Baruch, Jeff Bingham, Sanky Chan, Kenneth Draper, Debidatta Dwibedi, Chelsea Finn, Pete Florence, Spencer Goodrich, et al. Aloha 2: An enhanced lowcost hardware for bimanual teleoperation. _arXiv preprint arXiv:2405.02292_ , 2024. 

- [3] Marcin Andrychowicz, Anton Raichuk, Piotr Sta´nczyk, Manu Orsini, Sertan Girgin, Raphael Marinier, L´eonard Hussenot, Matthieu Geist, Olivier Pietquin, Marcin Michalski, et al. What matters in on-policy reinforcement learning? a large-scale empirical study. _arXiv preprint arXiv:2006.05990_ , 2020. 

- [4] OpenAI: Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 39 (1):3–20, 2020. 

- [5] James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris Leary, Dougal Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-Milne, and Qiao Zhang. JAX: composable transformations of Python+NumPy programs, 2018. URL http://github.com/jax-ml/jax. 

- [6] Ken Caluwaerts, Atil Iscen, J Chase Kew, Wenhao Yu, Tingnan Zhang, Daniel Freeman, Kuang-Huei Lee, Lisa Lee, Stefano Saliceti, Vincent Zhuang, et al. Barkour: Benchmarking animal-level agility with quadruped robots. _arXiv preprint arXiv:2305.14654_ , 2023. 

- [7] Yevgen Chebotar, Ankur Handa, Viktor Makoviychuk, Miles Macklin, Jan Issac, Nathan Ratliff, and Dieter 

Fox. Closing the sim-to-real loop: Adapting simulation randomization with real world experience. In _2019 International Conference on Robotics and Automation (ICRA)_ , pages 8973–8979. IEEE, 2019. 

- [8] Tao Chen, Jie Xu, and Pulkit Agrawal. A system for general in-hand object re-orientation. In _Conference on Robot Learning_ , pages 297–307. PMLR, 2022. 

- [9] Xuxin Cheng, Kexin Shi, Ananye Agarwal, and Deepak Pathak. Extreme parkour with legged robots. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 11443–11450. IEEE, 2024. 

- [10] Yoonyoung Cho, Junhyek Han, Yoontae Cho, and Beomjoon Kim. Corn: Contact-based object representation for nonprehensile manipulation of general unseen objects. _arXiv preprint arXiv:2403.10760_ , 2024. 

- [11] ONNX Runtime developers. Onnx runtime. https: //onnxruntime.ai/, 2021. Version: x.y.z. 

- [12] T. Flayols, A. Del Prete, P. Wensing, A. Mifsud, M. Benallegue, and O. Stasse. Experimental evaluation of simple estimators for humanoid robots. In _2017 IEEE-RAS 17th International Conference on Humanoid Robotics (Humanoids)_ , pages 889–895, 2017. doi: 10.1109/ HUMANOIDS.2017.8246977. 

- [13] C Daniel Freeman, Erik Frey, Anton Raichuk, Sertan Girgin, Igor Mordatch, and Olivier Bachem. Brax-a differentiable physics engine for large scale rigid body simulation, 2021. _URL http://github. com/google/brax_ , 6, 2021. 

- [14] Genesis-Authors. Genesis: A universal and generative physics engine for robotics and beyond, December 2024. URL https://github.com/Genesis-Embodied-AI/Genesis. 

- [15] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In _International conference on machine learning_ , pages 1861–1870. PMLR, 2018. 

- [16] Tuomas Haarnoja, Ben Moran, Guy Lever, Sandy H Huang, Dhruva Tirumala, Jan Humplik, Markus Wulfmeier, Saran Tunyasuvunakool, Noah Y Siegel, Roland Hafner, et al. Learning agile soccer skills for a bipedal robot with deep reinforcement learning. _Science Robotics_ , 9(89):eadi8022, 2024. 

- [17] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. Mastering diverse domains through world models. _arXiv preprint arXiv:2301.04104_ , 2023. 

- [18] Mustafa Haiderbhai, Radian Gondokaryono, Andrew Wu, and Lueder A. Kahrs. Sim2real rope cutting with a surgical robot using vision-based reinforcement learning. _Transactions on Automation Science and Engineering_ , 2024. doi: 10.1109/TASE.2024.3410297. 

- [19] Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zhurkevich, Balakumar Sundaralingam, et al. Dextreme: Transfer of agile in-hand manipulation from simulation to reality. In _2023 IEEE International Conference on Robotics and_ 

_Automation (ICRA)_ , pages 5977–5984. IEEE, 2023. 

- [20] Nicklas Hansen, Hao Su, and Xiaolong Wang. Td-mpc2: Scalable, robust world models for continuous control, 2024. 

- [21] Yanhao He and Steven Liu. Analytical inverse kinematics for franka emika panda – a geometrical solver for 7- dof manipulators with unconventional design. In _2021 9th International Conference on Control, Mechatronics and Automation (ICCMA)_ , pages 194–199, 2021. doi: 10.1109/ICCMA54375.2021.9646185. 

- [22] Samuel Holt, Todor Davchev, Dhruva Tirumala, Ben Moran, Yixin Lin, Antoine Laurens, Atil Iscen, Erik Frey, Markus Wulfmeier, Francesco Romano, and Nicolas Heess. Evolving control: Evolved high frequency control for continuous control tasks. In _CoRL Workshop on Safe and Robust Robot Learning for Operation in the Real World_ , 2024. URL https://openreview.net/forum? id=gzADUWLD9X. 

- [23] Yuanming Hu, Luke Anderson, Tzu-Mao Li, Qi Sun, Nathan Carr, Jonathan Ragan-Kelley, and Fr´edo Durand. Difftaichi: Differentiable programming for physical simulation. _arXiv preprint arXiv:1910.00935_ , 2019. 

- [24] Julian Ibarz, Jie Tan, Chelsea Finn, Mrinal Kalakrishnan, Peter Pastor, and Sergey Levine. How to train your robot with deep reinforcement learning: lessons we have learned. _The International Journal of Robotics Research_ , 40(4-5):698–721, 2021. 

- [25] Gwanghyeon Ji, Juhyeok Mun, Hyeongjun Kim, and Jemin Hwangbo. Concurrent training of a control policy and a state estimator for dynamic and robust legged locomotion. _IEEE Robotics and Automation Letters_ , 7 (2):4630–4637, April 2022. ISSN 2377-3774. doi: 10. 1109/lra.2022.3151396. URL http://dx.doi.org/10.1109/ LRA.2022.3151396. 

- [26] Elia Kaufmann, Leonard Bauersfeld, Antonio Loquercio, Matthias M¨uller, Vladlen Koltun, and Davide Scaramuzza. Champion-level drone racing using deep reinforcement learning. _Nature_ , 620(7976):982–987, 2023. 

- [27] Jens Kober, J Andrew Bagnell, and Jan Peters. Reinforcement learning in robotics: A survey. _The International Journal of Robotics Research_ , 32(11):1238–1274, 2013. 

- [28] Nathan Koenig and Andrew Howard. Design and use paradigms for gazebo, an open-source multi-robot simulator. In _2004 IEEE/RSJ international conference on intelligent robots and systems (IROS)(IEEE Cat. No. 04CH37566)_ , volume 3, pages 2149–2154. Ieee, 2004. 

- [29] Michael Laskin, Kimin Lee, Adam Stooke, Lerrel Pinto, Pieter Abbeel, and Aravind Srinivas. Reinforcement learning with augmented data. arXiv:2004.14990. 

- [30] Joonho Lee, Jemin Hwangbo, and Marco Hutter. Robust recovery controller for a quadrupedal robot using deep reinforcement learning. _arXiv preprint arXiv:1901.07517_ , 2019. 

- [31] leggedrobotics. rsl rl: Fast and simple implementation of rl algorithms, designed to run fully on gpu. https://github. com/leggedrobotics/rsl rl, 2023. Accessed: January 10, 

2025. 

- [32] Albert Hao Li, Preston Culbertson, Vince Kurtz, and Aaron D. Ames. Drop: Dexterous reorientation via online planning. _arXiv preprint arXiv:2409.14562_ , 2024. Available at: https://arxiv.org/abs/2409.14562. 

- [33] Zhongyu Li, Xue Bin Peng, Pieter Abbeel, Sergey Levine, Glen Berseth, and Koushil Sreenath. Reinforcement learning for versatile, dynamic, and robust bipedal locomotion control. _The International Journal of Robotics Research_ , page 02783649241285161, 2024. 

- [34] Jacky Liang, Viktor Makoviychuk, Ankur Handa, Nuttapong Chentanez, Miles Macklin, and Dieter Fox. Gpuaccelerated robotic simulation for distributed reinforcement learning. In _Conference on Robot Learning_ , pages 270–282. PMLR, 2018. 

- [35] Qiayuan Liao, Bike Zhang, Xuanyu Huang, Xiaoyu Huang, Zhongyu Li, and Koushil Sreenath. Berkeley humanoid: A research platform for learning-based control. _arXiv preprint arXiv:2407.21781_ , 2024. 

- [36] Junfeng Long, Junli Ren, Moji Shi, Zirui Wang, Tao Huang, Ping Luo, and Jiangmiao Pang. Learning humanoid locomotion with perceptive internal model. _arXiv preprint arXiv:2411.14386_ , 2024. 

- [37] Yecheng Jason Ma, William Liang, Guanzhi Wang, DeAn Huang, Osbert Bastani, Dinesh Jayaraman, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Eureka: Humanlevel reward design via coding large language models. _arXiv preprint arXiv:2310.12931_ , 2023. 

- [38] Miles Macklin. Warp: A high-performance python framework for gpu simulation and graphics. In _NVIDIA GPU Technology Conference (GTC)_ , 2022. 

- [39] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

- [40] Takahiro Miki, Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen Koltun, and Marco Hutter. Learning robust perceptive locomotion for quadrupedal robots in the wild. _Science robotics_ , 7(62):eabk2822, 2022. 

- [41] Mayank Mittal, Calvin Yu, Qinxi Yu, Jingzhou Liu, Nikita Rudin, David Hoeller, Jia Lin Yuan, Ritvik Singh, Yunrong Guo, Hammad Mazhar, et al. Orbit: A unified simulation framework for interactive robot learning environments. _IEEE Robotics and Automation Letters_ , 8(6): 3740–3747, 2023. 

- [42] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. Human-level control through deep reinforcement learning. _Nature_ , 518(7540):529–533, 2015. doi: 10.1038/ nature14236. URL https://doi.org/10.1038/nature14236. 

- [43] MuJoCo XLA Authors. MuJoCo XLA (MJX). https: //mujoco.readthedocs.io/en/stable/mjx.html. Accessed: December 16, 2024. 

- [44] Scott Niekum and Isaac I.Y. Saito. ar <u>track alvar,</u> 2016. URL https://github.com/ros-perception/ar <u>track alvar.</u> 

- [45] Aleksei Petrenko, Arthur Allshire, Gavriel State, Ankur Handa, and Viktor Makoviychuk. Dexpbt: Scaling up dexterous manipulation for hand-arm systems with population based training. _RSS_ , 2023. 

- [46] Lerrel Pinto, Marcin Andrychowicz, Peter Welinder, Wojciech Zaremba, and Pieter Abbeel. Asymmetric actor critic for image-based robot learning. _RSS_ , 2018. 

- [47] Ilija Radosavovic, Sarthak Kamat, Trevor Darrell, and Jitendra Malik. Learning humanoid locomotion over challenging terrain. _arXiv preprint arXiv:2410.03654_ , 2024. 

- [48] Prajit Ramachandran, Barret Zoph, and Quoc V. Le. Searching for activation functions, 2017. URL https: //arxiv.org/abs/1710.05941. 

- [49] Luc Guy Rosenzweig, Brennan Shacklett, Warren Xia, and Kayvon Fatahalian. High-throughput batch rendering for embodied ai. 2024. 

- [50] Nikita Rudin, David Hoeller, Philipp Reist, and Marco Hutter. Learning to walk in minutes using massively parallel deep reinforcement learning. In _Conference on Robot Learning_ , pages 91–100. PMLR, 2022. 

- [51] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 

- [52] Carmelo Sferrazza, Dun-Ming Huang, Xingyu Lin, Youngwoon Lee, and Pieter Abbeel. Humanoidbench: Simulated humanoid benchmark for whole-body locomotion and manipulation. _Robotics: Science and Systems (RSS)_ , 2024. 

- [53] Brennan Shacklett, Luc Guy Rosenzweig, Zhiqiang Xie, Bidipta Sarkar, Andrew Szot, Erik Wijmans, Vladlen Koltun, Dhruv Batra, and Kayvon Fatahalian. An extensible, data-oriented architecture for high-performance, many-world simulation. _ACM Transactions on Graphics (TOG)_ , 42(4):1–13, 2023. 

- [54] Brennan Shacklett, Luc Guy Rosenzweig, Zhiqiang Xie, Bidipta Sarkar, Andrew Szot, Erik Wijmans, Vladlen Koltun, Dhruv Batra, and Kayvon Fatahalian. An extensible, data-oriented architecture for high-performance, many-world simulation. _ACM Trans. Graph._ , 42(4), 2023. 

- [55] Yecheng Shao, Yongbin Jin, Xianwei Liu, Weiyan He, Hongtao Wang, and Wei Yang. Learning free gait transition for quadruped robots via phase-guided controller. _IEEE Robotics and Automation Letters_ , 7(2):1230–1237, 2021. 

- [56] Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _Robotics: Science and Systems (RSS)_ , 2023. 

- [57] Ritvik Singh, Arthur Allshire, Ankur Handa, Nathan 

Ratliff, and Karl Van Wyk. Dextrah-rgb: Visuomotor policies to grasp anything with dexterous hands. _arXiv preprint arXiv:2412.01791_ , 2024. 

- [58] Laura Smith, J Chase Kew, Xue Bin Peng, Sehoon Ha, Jie Tan, and Sergey Levine. Legged robots that keep on learning: Fine-tuning locomotion policies in the real world. In _2022 International Conference on Robotics and Automation (ICRA)_ , pages 1593–1599. IEEE, 2022. 

- [59] Jie Tan, Tingnan Zhang, Erwin Coumans, Atil Iscen, Yunfei Bai, Danijar Hafner, Steven Bohez, and Vincent Vanhoucke. Sim-to-real: Learning agile locomotion for quadruped robots. _arXiv preprint arXiv:1804.10332_ , 2018. 

- [60] Stone Tao, Fanbo Xiang, Arth Shukla, Yuzhe Qin, Xander Hinrichsen, Xiaodi Yuan, Chen Bao, Xinsong Lin, Yulin Liu, Tse-kai Chan, et al. Maniskill3: Gpu parallelized robotics simulation and rendering for generalizable embodied ai. _arXiv preprint arXiv:2410.00425_ , 2024. 

- [61] Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez, Yazhe Li, Diego de Las Casas, David Budden, Abbas Abdolmaleki, Josh Merel, Andrew Lefrancq, et al. Deepmind control suite. _arXiv preprint arXiv:1801.00690_ , 2018. 

- [62] Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. In _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 23–30, 2017. 

- [63] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ international conference on intelligent robots and systems_ , pages 5026–5033. IEEE, 2012. 

- [64] Shengjie Wang, Shaohuai Liu, Weirui Ye, Jiacheng You, and Yang Gao. Efficientzero v2: Mastering discrete and continuous control with limited data. _arXiv preprint arXiv:2403.00564_ , 2024. 

- [65] Yuxin Wang, Qiang Wang, Shaohuai Shi, Xin He, Zhenheng Tang, Kaiyong Zhao, and Xiaowen Chu. Benchmarking the performance and energy efficiency of ai accelerators for ai training. In _2020 20th IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing (CCGRID)_ , pages 744–751. IEEE, 2020. 

- [66] Haoru Xue, Chaoyi Pan, Zeji Yi, Guannan Qu, and Guanya Shi. Full-order sampling-based mpc for torquelevel locomotion control via diffusion-style annealing. _arXiv preprint arXiv:2409.15610_ , 2024. 

- [67] Denis Yarats, Rob Fergus, Alessandro Lazaric, and Lerrel Pinto. Mastering visual continuous control: Improved data-augmented reinforcement learning. _arXiv preprint arXiv:2107.09645_ , 2021. 

- [68] Kevin Zakka, Yuval Tassa, and MuJoCo Menagerie Contributors. MuJoCo Menagerie: A collection of highquality simulation models for MuJoCo, 2022. URL http://github.com/google-deepmind/mujoco <u>menagerie.</u> 

- [69] Wenshuai Zhao, Jorge Pe˜na Queralta, and Tomi Westerlund. Sim-to-real transfer in deep reinforcement learning for robotics: a survey. In _2020 IEEE symposium series on computational intelligence (SSCI)_ , pages 737–744. IEEE, 2020. 

- [70] Ziwen Zhuang, Zipeng Fu, Jianren Wang, Christopher Atkeson, Soeren Schwertfeger, Chelsea Finn, and Hang Zhao. Robot parkour learning. _arXiv preprint arXiv:2309.05665_ , 2023. 

## **Appendix** 

### **Table of Contents** 

|**Appendix A: **|**DM Control Suite**|12|
|---|---|---|
|A.1|Environments<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>12|
|A.2|RL Training Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>12|
|A.3|RL Training Throughput<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>12|
|**Appendix B: **|**Locomotion**|17|
|B.1|Environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>17|
|B.2|RL Training Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>17|
|B.3|RL Training Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>18|
|B.4|RL Training Throughput<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>18|
|B.5|Real-world Setup<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>22|
|**Appendix C: **|**Manipulation**|23|
|C.1|Environments<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>23|
|C.2|RL Training Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>23|
|C.3|RL Training Throughput<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>23|
|C.4|Real-world Cube Reorientation with a Leap Hand<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>26|
|C.5|Real-world Non-prehensile Block Reorientation with a Franka-Robotiq Arm . . . . . . . .|. . . . . . .<br>27|
|C.6|Real-world Franka PickCube from Pixels<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>30|
|**Appendix D: **|**Madrona Rendering Environments**|32|
|D.1|RL Training Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>32|
|D.2|Performance Benchmarking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>32|
|D.3|Bottlenecks in Pixels-based Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>36|
|**Appendix E: **|**Reinforcement Learning Hyper-parameters**|37|
|E.1|DM Control Suite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>37|
|E.2|Locomotion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>38|
|E.3|Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>40|



APPENDIX A 

### DM CONTROL SUITE 

### _A.1. Environments_ 

In Table III, we show the environments from DM Control Suite ([61]) that were re-implemented in MuJoCo Playground. Certain XMLs were modified for performance and are shown in the table. 

### _A.2. RL Training Results_ 

For all DM Control Suite environments ported to MuJoCo Playground, we train both PPO [51] and SAC [15] using the RL implementations in [13] and we report reward curves below. In Figure 9 we report environment steps versus reward and in Figure 10 we report wallclock time versus reward. All environments are run across 5 seeds on a single A100 GPU. 

### _A.3. RL Training Throughput_ 

We report training throughput on all DM Control Suite environments in Table IV by dividing the number of environment steps by wallclock time, as reported in Section A.2, for each RL algorithm. 

|**Env**|**MJX**|**XML Modifications**|
|---|---|---|
|acrobot-swingup|✓|iterations=2, ls<br>iterations=4|
|acrobot-swingup<br>sparse|✓||
|ball<br>in<br>cup-catch|✓|iterations=1, ls<br>iterations=4|
|cartpole-balance|✓|iterations=1, ls<br>iterations=4|
|cartpole-balance<br>sparse|✓<br>||
|cartpole-swingup|✓||
|cartpole-swingup<br>sparse<br>|✓<br>||
|cheetah-run|✓|iterations=4, ls<br>iterations=8, max<br>contact<br>points=6, max<br>geom<br>pairs=4|
|finger-spin|✓|iterations=2,<br>ls<br>iterations=8,<br>max<br>contact<br>points=4,<br>max<br>geom<br>pairs=2,<br>removed<br>cylinder collision|
|finger<br>turn<br>easy|✓<br>||
|finger<br>turn<br>hard|✓||
|fish-upright|✓|iterations=2, ls<br>iterations=6, disabled contacts|
|fish-swim|✓||
|hopper-stand|✓|iterations=4, ls<br>iterations=8, max<br>contact<br>points=6, max<br>geom<br>pairs=2|
|hopper-hop|✓||
|humanoid-stand|✓|timestep=0.005, max<br>contact<br>points=8, max<br>geom<br>pairs=8|
|humanoid-walk|✓||
|humanoid-run|✓||
|pendulum-swingup|✓|timestep=0.01, iterations=4, ls<br>iterations=8|
|point<br>mass-easy|✓|iterations=1, ls<br>iterations=4|
|reacher-easy|✓|timestep=0.005, iterations=1, ls<br>iterations=6|
|reacher-hard|✓||
|swimmer-swimmer6|✓|timestep=0.003, iterations=4, ls<br>iterations=8, contype/conaffinity set to 0|
|swimmer-swimmer15|_×_||
|walker-stand|✓|timestep=0.005,<br>iterations=2,<br>ls<br>iterations=5,<br>max<br>contact<br>points=4,<br>max<br>geom<br>pairs=4|
|walker-walk|✓||
|walker-run|✓||
|manipulator-bring<br>ball|_×_||
|manipulator-bring<br>peg|_×_||
|manipulator-insert<br>ball|_×_||
|manipulator-insert<br>peg|_×_||
|dog-stand|_×_||
|dog-walk|_×_||
|dog-trot|_×_||
|dog-run|_×_||
|dog-fetch|_×_||



TABLE III: DM Control Suite Environments ported to MJX. Where specified, XML modifications were made to the solver iterations, line search iterations, as well as contact custom parameters for MJX. 



<!-- Start of picture text -->
1000 AcrobotSwingup 1000AcrobotSwingupSparse 1000 BallInCup 1000 CartpoleBalance 1000CartpoleBalanceSparse<br>PPO Mean<br>800 SAC Mean 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5 0 2 4 6 0 2 4 6 8 0 2 4 6 8<br>Env Steps 1e8 Env Steps 1e8 Env Steps 1e7 Env Steps 1e7 Env Steps 1e7<br>1000 CartpoleSwingup 1000CartpoleSwingupSparse 1000 CheetahRun 1000 FingerSpin 1000 FingerTurnEasy<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8<br>Env Steps 1e7 Env Steps 1e7 Env Steps 1e7 Env Steps 1e7 Env Steps 1e7<br>1000 FingerTurnHard 1000 FishSwim 1000 HopperHop 1000 HopperStand 1000 HumanoidRun<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8<br>Env Steps 1e7 Env Steps 1e7 Env Steps 1e7 Env Steps 1e7 Env Steps 1e7<br>1000 HumanoidStand 1000 HumanoidWalk 1000 PendulumSwingup 1000 PointMass 1000 ReacherEasy<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8<br>Env Steps 1e7 Env Steps 1e7 Env Steps 1e7 Env Steps 1e7 Env Steps 1e7<br>ReacherHard SwimmerSwimmer6 WalkerRun WalkerStand WalkerWalk<br>1000 1000 1000 1000 1000<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 2 4 6 8 0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5 0 2 4 6 8 0 2 4 6 8<br>Env Steps 1e7 Env Steps 1e8 Env Steps 1e8 Env Steps 1e7 Env Steps 1e7<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br><!-- End of picture text -->

Fig. 9: Reward vs environment steps for PPO and SAC on the full DM Control Suite environments in MuJoCo Playground. We run PPO for 60M steps, with a few selected environments running on 100M steps. SAC runs for 5M steps. All settings are run with 5 seeds on a single A100 GPU device. 



<!-- Start of picture text -->
1000 AcrobotSwingup 1000AcrobotSwingupSparse 1000 BallInCup 1000 CartpoleBalance 1000CartpoleBalanceSparse<br>PPO Mean<br>800 SAC Mean 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 100 200 300 0 100 200 300 0 100 200 300 0 50 100 150 0 50 100 150<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>1000 CartpoleSwingup 1000CartpoleSwingupSparse 1000 CheetahRun 1000 FingerSpin 1000 FingerTurnEasy<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 50 100 150 0 50 100 150 0 100 200 300 400 500 0 200 400 600 0 200 400 600<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>1000 FingerTurnHard 1000 FishSwim 1000 HopperHop 1000 HopperStand 1000 HumanoidRun<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 200 400 600 0 100 200 300 400 500 0 200 400 600 800 0 200 400 600 800 0 200 400 600 800 1000<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>1000 HumanoidStand 1000 HumanoidWalk 1000 PendulumSwingup 1000 PointMass 1000 ReacherEasy<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 200 400 600 800 1000 0 500 1000 1500 0 50 100 150 0 50 100 150 0 50 100 150 200<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>ReacherHard SwimmerSwimmer6 WalkerRun WalkerStand WalkerWalk<br>1000 1000 1000 1000 1000<br>800 800 800 800 800<br>600 600 600 600 600<br>400 400 400 400 400<br>200 200 200 200 200<br>0 0 0 0 0<br>0 50 100 150 200 0 200 400 600 800 1000 0 500 1000 0 200 400 600 0 200 400 600<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward Episode Reward<br><!-- End of picture text -->

Fig. 10: Reward vs wallclock time for PPO and SAC on the full DM Control Suite environments in MuJoCo Playground. All settings are run with 5 seeds on a single A100 GPU device. 

|Env|PPO Steps per Second|SAC Steps Per Second|
|---|---|---|
|AcrobotSwingup|752092 _±_ 11562|30661 _±_ 244|
|AcrobotSwingupSparse|750597 _±_ 4640|30624 _±_ 210|
|BallInCup<br>|235899 _±_ 565<br>|15492 _±_ 283<br>|
|CartpoleBalance|718626 _±_ 6894|30891 _±_ 168|
|CartpoleBalanceSparse|721061 _±_ 14135|31031 _±_ 183|
|CartpoleSwingup|728088 _±_ 12503|30870 _±_ 207|
|CartpoleSwingupSparse|718355 _±_ 10189|31061 _±_ 226|
|CheetahRun|435162 _±_ 12183|18819 _±_ 202|
|FingerSpin<br>|246791 _±_ 1763<br>|16475 _±_ 153<br>|
|FingerTurnEasy<br>|245255 _±_ 4561<br>|16086 _±_ 112<br>|
|FingerTurnHard|245421 _±_ 4278<br>|16084 _±_ 69<br>|
|FishSwim|183750 _±_ 1773|11591 _±_ 55|
|HopperHop|201313 _±_ 2833|12098 _±_ 166|
|HopperStand|201517 _±_ 3227|12008 _±_ 255|
|HumanoidRun|91617 _±_ 1019|5886 _±_ 62|
|HumanoidStand|91927 _±_ 1004|5893 _±_ 17|
|HumanoidWalk|91563 _±_ 1150|5842 _±_ 51|
|PendulumSwingup|724126 _±_ 21524|32836 _±_ 178|
|PointMass|730775 _±_ 3608|31710 _±_ 148|
|ReacherEasy|520021 _±_ 9637|24888 _±_ 149|
|ReacherHard|523441 _±_ 8012|24874 _±_ 156|
|SwimmerSwimmer6|167259 _±_ 2377|10012 _±_ 79|
|WalkerRun|141581 _±_ 831|6069 _±_ 48|
|WalkerStand|140360 _±_ 1762|6085 _±_ 29|
|WalkerWalk|139818 _±_ 1267|6098 _±_ 30|



TABLE IV: Training throughput is displayed for all the DM Control Suite environments on an A100 GPU device across 5 seeds using brax PPO and the RL hyperparameters in Appendix Section E. We report the 95th percentile confidence interval. 

APPENDIX B LOCOMOTION 

### _B.1. Environment_ 

In Table V we show all the locomotion environments available in MuJoCo Playground, broken down by robot platform and available controller. 

|**Robot**|**Type**|**Environment**|
|---|---|---|
|Google Barkour|Quadruped|JoystickFlatTerrain, JoystickRoughTerrain|
|Berkeley Humanoid|Biped|Joystick|
|Unitree G1|Biped|Joystick|
|Booster T1|Biped|Joystick|
|Unitree Go1|Quadruped|JoystickFlatTerrain, JoystickRoughTerrain, Getup, Handstand, Footstand|
|Unitree H1|Biped|InplaceGaitTracking, JoystickGaitTracking|
|OP3|Biped|Joystick|
|Boston Dynamics Spot|Quadruped|JoystickFlatTerrain, JoystickGaitTracking, Getup|



TABLE V: Locomotion environments implemented in MuJoCo Playground by robot platform. 

### _B.2. RL Training Details_ 

_B.21. Observation and Action:_ We use a unified observation space across all locomotion environments: 

- (a) Gravity projected in the body frame, 

- (b) Base linear and angular velocity, 

- (c) Joint positions and velocities, 

- (d) Previous action, 

- (e) (Optional) User command for joystick-based tasks. 

For humanoid locomotion tasks, a phase variable [55] is introduced to shape the gait. This phase variable cycles between _−π_ and _π_ for each foot, representing the gait phase. To capture this information effectively, the cos and sin of the phase variable for each foot are included in the observation space. This representation provides a continuous and smooth encoding of the phase, enabling the policy to synchronize its actions with the desired gait cycle. 

The action space is defined differently depending on the task. For joystick tasks, we use an _absolute_ joint position with a default offset: 



where _ka_ is the action scale. For all other tasks, we use a _relative_ joint position: 



The desired joint position is mapped to torque via a PD controller: 



where _kp_ and _kd_ are the proportional and derivative gains, respectively. 

_B.22. Domain Randomization:_ To reduce the sim-to-real gap, we randomize several parameters during training: 

- **Sensor noise:** All sensor readings are corrupted with noise. 

- **Dynamic properties:** Physical parameters that are difficult to measure precisely (e.g., link center-of-mass, reflected inertia, joint calibration offsets). 

- **Task uncertainties:** Ground friction and payload mass. 

_B.23. Reward and Termination:_ In Table VI, _cmdv,xy_ and _cmdω,z_ represent the commanded linear velocity in the _xy_ -plane and angular velocity around the _z_ -axis, respectively. _vxy_ and _ωz_ are the actual linear and angular velocities. _Ts_ and _Ta_ represent the time of the last touchdown and takeoff of the feet. _pf,z_ and _p_<sup>des</sup> _f,z_<sup>denotetheactualanddesiredfootheights,while</sup><sup>_vf,xy_is</sup> the horizontal foot velocity. _τ_ is the torque, _q_ is the joint position, and _q_ ˙ is the joint velocity. 

The total reward _r_ total is calculated as the weighted sum of all the reward terms: 



Finally, the total reward is clipped to ensure it remains non-negative. 

**Termination:** For joystick-controlled policies, we use a reduced collision model (only the feet) and terminate the episode if the robot inverts (e.g., ends up upside down). For other tasks, we employ the full collision model approximated using geometric primitives. 

TABLE VI: Reward Functions 

|**Reward**|**Expression**|
|---|---|
|Linear Velocity Tracking|_rv_ =_kv_exp<br>�<br>_−∥cmdv,xy −vxy∥_<sup>2</sup>_/σv_<br>�<br><br><br>|
|Angular Velocity Tracking|_rω_ =_kω_ exp<br>�<br>_−∥cmdω,z −ωz∥_<sup>2</sup>_/σω_<br>�|
|Feet Airtime|_r_air =clip ((_T_air _−T_min)_· C_contact_,_0_, T_max _−T_min)|
|Feet Clearance|_r_clear =_k_clear_· ∥pf,z −p_<sup>des</sup><br>_f,z_<sup>_∥_2</sup> <sup>_· ∥vf,xy∥_0</sup><sup>_._5</sup>|
|Feet Phase|_r_phase =_k_phase _·_exp<br>�<br>_−∥pf,z −rz_(_ϕ_)_∥_<sup>2</sup>_/σ_phase<br>�<br>|
|Feet Slip|_r_slip =_k_slip _·∥Cf,i · vf,xy∥_<sup>2</sup><br>|
|Orientation|_r_ori =_k_ori _·∥ϕ_body,xy_∥_<sup>2</sup>|
|Joint Torque|_rτ_ =_kτ · ∥τ∥_<sup>2</sup>|
|Joint Position|_rq_ =_kq · ∥q −q_nominal_∥_<sup>2</sup>|
|Action Rate|_r_rate =_k_rate _·∥at −at−_1_∥_<sup>2</sup>|
|Energy Consumption|_r_energy =_k_energy _·∥_˙_q · τ∥_<br><br>|
|Pose Deviation|_r_pose =_k_pose_·_exp<br>�<br>_−∥q −q_default_∥_<sup>2�</sup>|
|Termination (Penalty)|_r_termination =_k_termination _·_done|
|Stand Still (Penalty)|_r_standstill =_k_standstill _·∥cmdv,xy∥_|
|Linear Velocity in Z (Penalty)|_r_lin<br>z <sup>=</sup><sup>_k_</sup>lin<br>z <sup>_·∥v_</sup>_z_<sup>_∥_2</sup><br>|
|Angular Velocity in XY (Penalty)|_r_ang<br>xy <sup>=</sup><sup>_k_</sup>ang<br>xy <sup>_·∥ω_</sup>_x,y_<sup>_∥_2</sup>|



_B.24. Network Architecture:_ We employ an asymmetric actor–critic [46] setup, in which the policy network (actor) and the value network (critic) receive different observation inputs. The policy network is fed with the aforementioned observations, while the value network additionally receives uncorrupted versions of these signals and extra sensor readings such as contact forces, perturbation forces, and joint torques. 

Both the policy and value networks use a three-layer multilayer perceptron (MLP) with hidden sizes of 512, 256, and 128. Each hidden layer uses the Swish [48] activation function. A full set of hyper-parameters is available in Section E. 

- _B.25. Finetuning:_ 

- _B.25a. Joystick policy:_ 

- 1) Train for 100 M timesteps with a command range of _{_ 1 _._ 5 _,_ 0 _._ 8 _,_ 1 _._ 2 _}_ . 

- 2) Finetune for 50 M timesteps with a command range of _{_ 1 _._ 5 _,_ 0 _._ 8 _,_ 2 _π}_ . 

- 3) Finetune on rough terrain for 100 M timesteps. 

- _B.25b. Getup policy:_ 

- 1) Train with a power termination cutoff of 400 W. 

- 2) Finetune with a joint velocity cost. 

- _B.25c. Handstand and footstand policies:_ 

- 1) Finetune with a joint acceleration and energy cost. 

- 2) Progressively reduce the power termination budget from 400 W to 200 W. 

Finally, all policies are trained on flat terrain for 200 M timesteps, then finetuned on rough terrain for 100 M timesteps. The rough terrain is modeled as a heightfield generated from Perlin noise. 

### _B.3. RL Training Results_ 

For all locomotion environments implemented in MuJoCo Playground, we train with PPO using the RL implementation from [13] and we report reward curves below. In Figure 11 we report environment steps versus reward and in Figure 12 we report wallclock time versus reward. All environments are run across 5 seeds on a single A100 GPU. 

### _B.4. RL Training Throughput_ 

In Table VII we show training throughput for all locomotion envs. In Figure 13 we show training throughput of the Go1JoystickFlatTerrain environment. Different devices and topologies do not make material difference in training wallclock time, since the environment is quite simple with limited contacts between the feet and the floor. 



<!-- Start of picture text -->
BerkeleyHumanoid BerkeleyHumanoid<br>BarkourJoystick JoystickFlatTerrain JoystickRoughTerrain G1JoystickFlatTerrain<br>30<br>20<br>30 15<br>15<br>20<br>20 10<br>10<br>10<br>10 5 5<br>PPO Mean<br>0 0 0 0<br>0.00 0.25 0.50 0.75 1.00 0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5 2.0<br>Env Steps 1e8 Env Steps 1e8 Env Steps 1e8 Env Steps 1e8<br>G1JoystickRoughTerrain Go1Footstand Go1Getup Go1Handstand<br>6 15<br>15 15<br>4 10<br>10 10<br>2 5 5 5<br>0 0 0 0<br>0.0 0.5 1.0 1.5 0.00 0.25 0.50 0.75 1.00 0 2 4 0.00 0.25 0.50 0.75 1.00<br>Env Steps 1e8 Env Steps 1e8 Env Steps 1e7 Env Steps 1e8<br>Go1JoystickFlatTerrain Go1JoystickRoughTerrain H1InplaceGaitTracking H1JoystickGaitTracking<br>25 10<br>30<br>20 8<br>20<br>15 6 20<br>10 10 4<br>10<br>5 2<br>0 0 0 0<br>0.0 0.5 1.0 1.5 2.0 0.0 0.5 1.0 1.5 2.0 0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00<br>Env Steps 1e8 Env Steps 1e8 Env Steps 1e8 Env Steps 1e8<br>Op3Joystick SpotFlatTerrainJoystick SpotGetup SpotJoystickGaitTracking<br>40<br>20<br>20<br>30 15 30<br>15<br>10 20 10 20<br>5 5 10<br>10<br>0 0 0<br>0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00<br>Env Steps 1e8 Env Steps 1e8 Env Steps 1e8 Env Steps 1e8<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br><!-- End of picture text -->



<!-- Start of picture text -->
Fig. 11: Reward vs environment steps for Brax PPO. All settings are run with 5 seeds on a single A100 GPU device.<br><!-- End of picture text -->



<!-- Start of picture text -->
BerkeleyHumanoid BerkeleyHumanoid<br>BarkourJoystick JoystickFlatTerrain JoystickRoughTerrain G1JoystickFlatTerrain<br>30<br>20<br>30 15<br>15<br>20<br>20 10<br>10<br>10<br>10 5 5<br>PPO Mean<br>0 0 0 0<br>0 100 200 0 500 1000 0 2000 4000 0 2000 4000<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>G1JoystickRoughTerrain Go1Footstand Go1Getup Go1Handstand<br>6 15<br>15 15<br>4 10<br>10 10<br>2 5 5 5<br>0 0 0 0<br>0 2000 4000 6000 8000 0 200 400 0 200 400 0 200 400<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>Go1JoystickFlatTerrain Go1JoystickRoughTerrain H1InplaceGaitTracking H1JoystickGaitTracking<br>25 10<br>30<br>20 8<br>20<br>15 6 20<br>10 10 4<br>10<br>5 2<br>0 0 0 0<br>0 200 400 0 200 400 600 0 100 200 300 0 100 200 300<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>Op3Joystick SpotFlatTerrainJoystick SpotGetup SpotJoystickGaitTracking<br>40<br>20<br>20<br>30<br>15 30<br>15<br>20<br>10 10 20<br>5 10 5 10<br>0 0 0 0<br>0 200 400 0 100 200 0 100 200 300 400 0 100 200<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br><!-- End of picture text -->

Fig. 12: Reward vs wallclock time for Brax PPO. All settings are run with 5 seeds on a single A100 GPU device. Notice that the initial flat region measures the compilation time for the training + environment code. 

|Env|PPO Steps per Second|
|---|---|
|BarkourJoystick|385920 _±_ 2162|
|BerkeleyHumanoidJoystickFlatTerrain|120145 _±_ 484|
|BerkeleyHumanoidJoystickRoughTerrain|30393 _±_ 44|
|G1Joystick|106093 _±_ 131|
|Go1Footstand|204578 _±_ 906|
|Go1Getup|96173 _±_ 230|
|Go1Handstand|204416 _±_ 738|
|Go1JoystickFlatTerrain|417451 _±_ 2955|
|Go1JoystickRoughTerrain|291060 _±_ 727|
|H1InplaceGaitTracking|289372 _±_ 1498|
|H1JoystickGaitTracking|291018 _±_ 1111|
|Op3Joystick|198910 _±_ 406|
|SpotFlatTerrainJoystick|404931 _±_ 2710|
|SpotGetup|266792 _±_ 1038|
|SpotJoystickGaitTracking|407572 _±_ 4091|



TABLE VII: Training throughput is displayed for all the Locomotion environments on an A100 GPU device across 5 seeds using brax PPO and the RL hyperparameters in Section E. We report the 95th percentile confidence interval. 



<!-- Start of picture text -->
Go1JoystickFlatTerrain<br>30<br>25<br>20<br>15<br>1x 4090<br>2x 4090<br>10<br>1x A100<br>16x A100<br>5<br>1x H100<br>8x H100<br>0<br>0 100 200 300 400 500<br>Wallclock Time (s)<br>Episode Reward<br><!-- End of picture text -->

Fig. 13: Training wallclock time for Go1JoystickFlatTerrain on different GPU devices and topologies. 

### _B.5. Real-world Setup_ 

All locomotion deployments are based on ros2-control and are written in C++ with real-time guarantees. The Unitree SDK1, Unitree SDK2, and the Berkeley Humanoid EtherCAT master are each wrapped as abstract sensor and actuator hardware interfaces. These same interfaces are also used in Gazebo [28] to facilitate sim-to-sim verification. 

Different RL policies can be loaded and executed within the same process—whether operating on physical hardware or in simulation—by receiving sensor readings and issuing control commands via the hardware interface. Each policy model is inferenced at 50 Hz using ONNX Runtime [11], alongside a model-based estimator. In addition, a separate model-based estimator [12] runs at the hardware interface’s maximal communication frequency (500–2000 Hz), providing linear velocity observations and other diagnostic information. 

### APPENDIX C MANIPULATION 

### _C.1. Environments_ 

|**Robot**|**Environment**|
|---|---|
|Aloha|SinglePegInsertion|
|Franka Emika Panda|PickCube, PickCubeOrientation, PickCubeCartesian, OpenCabinet|
|Franka Emika Panda, Robotiq Gripper|PushCube|
|Leap Hand|Reorient, RotateZAxis|



TABLE VIII: Manipulation environments implemented in MuJoCo Playground by robot platform. 

### _C.2. RL Training Results_ 

For all manipulation environments implemented in MuJoCo Playground, we train with PPO using the RL implementation from [13] and we report reward curves below. In Figure 14 we report environment steps versus reward and in Figure 15 we report wallclock time versus reward. All environments are run across 5 seeds on a single A100 GPU. 



<!-- Start of picture text -->
AlohaSinglePegInsertion LeapCubeReorient LeapCubeRotateZAxis PandaOpenCabinet<br>25<br>1500<br>600 400 20<br>300 15 1000<br>400<br>200 10<br>200 100 5 500<br>PPO Mean 0 0<br>0 1 2 0 1 2 0.0 0.5 1.0 0 2 4<br>Env Steps 1e8 Env Steps 1e8 Env Steps 1e8 Env Steps 1e7<br>PandaPickCube PandaPickCubeCartesian PandaPickCubeOrientation PandaRobotiqPushCube<br>25<br>1250 10 1250<br>20<br>1000 8 1000<br>15<br>750 6 750<br>10<br>500 4 500<br>5<br>250 2 250<br>0<br>0<br>0 1 2 0 2 4 6 0 1 2 0 1 2<br>Env Steps 1e7 Env Steps 1e6 Env Steps 1e7 Env Steps 1e9<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br><!-- End of picture text -->

Fig. 14: Reward vs environment steps for brax PPO. All settings are run with 5 seeds on a single A100 GPU device. 

### _C.3. RL Training Throughput_ 

We show RL training throughput for all manipulation environments below in Table IX. In Figure 16 we show reward versus wallclock time on different GPU devices and topologies for the LeapCubeReorient environment. 

|Env|PPO Steps per Second|
|---|---|
|AlohaSinglePegInsertion|121119 _±_ 2159|
|LeapCubeReorient|76354 _±_ 143|
|LeapCubeRotateZAxis|76602 _±_ 179|
|PandaOpenCabinet|136007 _±_ 1553|
|PandaPickCube|140386 _±_ 1707|
|PandaPickCubeCartesian|38015 _±_ 5302|
|PandaPickCubeOrientation|140429 _±_ 1604|
|PandaRobotiqPushCube|487341 _±_ 4346|



TABLE IX: Training throughput is displayed for all the Manipulation environments on an A100 GPU device across 5 seeds using brax PPO and the RL hyperparameters in Section E. We report the 95th percentile confidence interval. 



<!-- Start of picture text -->
AlohaSinglePegInsertion LeapCubeReorient LeapCubeRotateZAxis PandaOpenCabinet<br>1500<br>600 400 20<br>300 15 1000<br>400<br>200 10<br>200 500<br>100 5<br>PPO Mean<br>0 0 0 0<br>0 1000 2000 0 1000 2000 3000 0 500 1000 1500 0 100 200 300<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>PandaPickCube PandaPickCubeCartesian PandaPickCubeOrientation PandaRobotiqPushCube<br>1500<br>25<br>10.0<br>1000 7.5 1000 20<br>15<br>5.0<br>500 500 10<br>2.5 5<br>0 0.0 0 0<br>0 100 0 50 100 150 0 100 0 2000 4000<br>Wallclock Time (s) Wallclock Time (s) Wallclock Time (s) Wallclock Time (s)<br>Episode Reward Episode Reward Episode Reward Episode Reward<br>Episode Reward Episode Reward Episode Reward Episode Reward<br><!-- End of picture text -->

Fig. 15: Reward vs wallclock time for brax PPO. All settings are run with 5 seeds on a single A100 GPU device. Notice that the initial flat region measures the compilation time for the training + environment code. 



<!-- Start of picture text -->
LeapCubeReorient<br>500<br>400<br>300<br>200<br>1x 4090<br>2x 4090<br>100 1x A100<br>16x A100<br>1x H100<br>8x H100<br>0<br>0 500 1000 1500 2000 2500<br>Wallclock Time (s)<br>Episode Reward<br><!-- End of picture text -->

Fig. 16: Training wallclock time for LeapHandReorient on different GPU devices and topologies. 

### _C.4. Real-world Cube Reorientation with a Leap Hand_ 

In this section, we present the technical details of our real-world cube reorientation task using the LEAP Hand, covering the simulation environment, training process, hardware interface, and camera-based object pose estimation. 

_C.41. Simulation Environment:_ The in-hand reorientation environment is designed to sequentially re-orient a cube within the palm of a robotic hand, without dropping the cube. The cube is initialized randomly above the palm of the hand. The policy then receives the joint angle measurements, estimated cube pose, and previous action. Upon reaching a target orientation within a 0.4 rad tolerance, a new orientation is sampled and the success counter is incremented. We continue re-sampling new target orientations until the cube is dropped or the hand becomes stuck for over 30 s. To avoid trivial adjustments, new orientations are sampled at least 90° away from the previous goal (as in [19, 32]). The cube must reach a target orientation within 0.1 rad (as opposed to 0.4 rad in the real-world setup). 

_C.41a. Policy Inputs and Actions:_ As in locomotion environments, we use an asymmetric actor–critic setup, in which the policy network (actor) and the value network (critic) receive different observation inputs. The policy network is fed observations as outlined below, while the value network additionally receives uncorrupted robot pose, robot velocity, fingertip positions, cube pose, cube velocity, and perturbation forces. 

- **Observations** (a) noisy estimates of the hand joint positions and velocities, (b) joint position errors (commanded vs achieved), (c) noisy estimates of the cube pose (distance of the cube to the palm center and cube orientation error), and (d) the previous commanded joint positions. 

- **Actions** 16 relative joint positions. 

_C.41b. Training Setup:_ To promote sim-to-real transfer, we apply domain randomization on friction, cube mass, joint offsets, motor friction, reflected inertia, and PD gains, as well as link masses and sensor noise. We also add 2 cm positional and 0.1 rad rotational noise to the cube pose. We conduct two main training phases. During the first 200 M steps, we train without random pose injection and torque limits. We then perform a 100 M-step fine-tuning stage in which we introduce random pose “injections” with a 0.1 probability to mimic “freak-out” moments in real pose estimation (e.g., due to occlusions) and impose torque limits to match the real hardware. 

_C.42. System Identification and Domain Randomization:_ The original simulation environment for sim-to-real transfer provided by the LEAP Hand [56] does not include robust system identification and instead relies heavily on manual parameter tuning. To improve both the performance and transparency of the system, we performed system identification on the DYNAMIXEL servo actuator used in the hand. 

The armature inertia (i.e., rotor inertia reflected through the gearbox) for each joint is: _I_ a = _k_ g<sup>2</sup><sup>_I_r</sup><sup>_,_where</sup><sup>_k_g= 288</sup><sup>_._35isthe</sup> gear ratio from the supplier’s data sheet, and _I_ r =<sup><u>1</u></sup> 2<sup>_m_r</sup><sup>_r_</sup> r<sup>2= 1</sup><sup>_._7</sup><sup>_×_10</sup><sup>_−_8 kg m2istherotorinertia.Toobtain</sup><sup>_I_r,weassumeda</sup> uniform mass distribution of the rotor, based on physical disassembly and measurements of the rotor mass ( _m_ r = 2 _._ 0 _×_ 10<sup>_−_3</sup> kg) and radius ( _r_ r = 4 _._ 12 _×_ 10<sup>_−_3</sup> m). 

Because accurately modeling and measuring friction losses is difficult, we set 10% of the maximum torque as the nominal friction value, and employed heavy domain randomization to account for uncertainties. 

For training, the servo actuator was controlled using a PD mapping similar to the locomotion setup in (1). However, during real-world deployment, the control law running on the servo actuator is: _i_ = _k_ p<sup>m</sup> � _θ_ des<sup>m</sup><sup>_−θ_m�</sup> _− k_ d<sup>m</sup><sup>_θ_˙m, where</sup><sup>_i_is the motor current</sup> command, and _k_ p<sup>m</sup><sup>_, k_</sup> d<sup>m</sup><sup>_, θ_</sup> des<sup>m</sup><sup>_, θ_mareexpressedinunitsdifferentfromthoseusedintraining.Toreconcilethesediscrepancies,</sup> we assume _τ_ = _k_ t _i_ and carefully compute the mappings based on the motor specifications provided in the data sheet. 

Unlike the locomotion setup, the DYNAMIXEL actuator does not perform true current control (i.e., no direct motor current feedback). As a result, the above PD controller may deviate from the ideal behavior. To mitigate this mismatch, we introduce randomization in _k_ p and _k_ d parameters during training. 

_C.43. Real Robot Setup:_ We deploy the learned policy on the hand using its open-source software, with the following modifications: _•_ **Control Frequency.** We reduce the policy control frequency from 150 Hz to 20 Hz in both simulation and real-world deployment, due to jitter issues with the low-level USB driver at higher frequencies. 

- **System Identification.** We use the same torque (current) limit, stiffness, and damping parameters in training, guided by the system identification results described above. 

_C.44. Vision-based Pose Estimator:_ We use the vision-based cube pose estimator from [19] in order to solve for the pose of the cube, although any equivalent method of obtaining the SE(3) camera-to-object transformation would work. Given the local-space 3D coordinates of the cube and the 2D keypoints from the pose estimator, we solve for the camera-to-world transformation. Using camera-to-hand intrinsics calibration, we can then find the hand-to-cube transformation which is used as input to the policy. We run the cube pose estimator at 15 Hz. During manipulation, we observe some small jitters or missed detections, but generally it is stable. Despite having access to three cameras on the physical hardware setup ([32], we elect to use only one for simplicity. 



Fig. 17: Example MuJoCo scene of our block reorientation environment. The block is pushed toward the center. 

### _C.5. Real-world Non-prehensile Block Reorientation with a Franka-Robotiq Arm_ 

In this section, we provide technical details for our block reorientation task on a real Franka Emika Panda robot with a Robotiq gripper, including the simulation environment, training process, robot hardware interface, and camera-based object pose estimation. Our approach enables reliably learning and deploying a policy for non-prehensile manipulation of a yoga block, requiring only a brief training time in simulation while allowing zero-shot transfer to the real robot. 

_C.51. Simulation Environment:_ The simulation environment (Figure 17) is designed to reorient a rectangular yoga block within a tabletop workspace region. The block is initialized at a random position and orientation subject to workspace bounds, and is then pushed, slid, or tapped to a desired goal pose at the center of the workspace. The policy uses 7D torque control signals for the robot arm and a fixed, closed Robotiq gripper. We include a simple termination condition when the block leaves the workspace or the end-effector violates safety constraints (e.g., collides with walls or floors). 

_C.51a. Key Features:_ 

- **High-frequency torque control at 200 Hz.** Each simulation step is advanced at a high frequency to match the targeted real-world controller rate. 

- **Curriculum learning.** We randomize initial joint positions, block poses, latencies in actions and observations, and other environment factors. A progressive curriculum increases the difficulty by gradually expanding the block’s displacement and orientation range. 

- **Observation Delay.** Both actions and observations are delayed by random amounts at each episode step to approximate real hardware latencies. 

- **Reward Shaping.** Shaped rewards encourage the robot to (i) stay near a nominal joint configuration, (ii) minimize velocities, (iii) keep the end-effector near the block, (iv) push the block toward the goal, and (v) orient the block to the desired angle. _C.51b. Policy Inputs and Actions:_ As shown in the environment code: 

- **Observations** (a) noisy estimates of the block pose, (b) current and recent robot joint positions and velocities, (c) the estimated end-effector pose, and (d) the target block pose. 

- **Actions** are 7D torque commands applied at the robot’s joints. A constant action for the gripper (fingers closed) is appended for technical reasons in MuJoCo but remains fixed at a configured grasp. 

   - _C.51c. Simulated Environment Details:_ 

- **Gravity Compensation and Torque Bounds.** We configure the MuJoCo model to match the real robot’s gravity compensation mode. Torque bounds are set to 8 Nm per joint in simulation, reflecting the approximate safe torque limit on real hardware. 

- **Collision Geometry.** The environment enforces collisions with floor, walls, and the block. The Robotiq gripper is held fixed but included for contact modeling. 

- **Delayed Observations and Actions.** We adopt random delays (between 1 and 3 steps for actions, and 6 to 12 steps for observations) to emulate real system communication latencies and sensor delay, following best practices in sim-to-real transfer. 

_C.51d. Training Setup:_ We train the policy on a 16x NVIDIA A100 GPU set-up for ten minutes of wall-clock time, with 3000 steps per episode (with action repeat set to 4, effectively running 750 policy decisions per episode). During training, the block’s pose, robot states, and delays are heavily randomized. The final policy was selected from a checkpoint that achieved the highest success rate in the simulator. 

_C.52. Real Robot Setup:_ We deployed the final trained policy on a Franka Emika Panda manipulator equipped with a Robotiq 2F-85 gripper and an integrated force torque sensor (Robotiq FT-300). Figure 18 illustrates the hardware platform used for our experiments. 

_C.52a. Direct Torque Control with Franka FCI:_ We interface with the robot via the Franka Control Interface (FCI) and send torque commands at 200 Hz: 

- **Gravity Compensation.** The Panda is configured to compensate for the arm’s own weight. The policy torques therefore focus on regulating the contact interactions with the block, making the system compliant. 

- **Bypassing Low-level PID Gains.** We avoid additional position or velocity tracking by sending raw joint torques. This significantly reduces the overhead of tuning any gain schedules and allows the learned policy to directly control contact forces. 

- **Safety Considerations.** We define software torque limits and monitor the robot’s built-in safety stops and collision detection thresholds. In practice, the learned policy operates well within these limits to gently push the block. _C.52b. Control and Communication Pipeline:_ We use a lightweight C++/ROS node that relays torque commands to the 

- Franka FCI at 200 Hz: 

- **Policy Node in Python.** Our Python node loads the final trained policy (JIT-compiled for inference speed). At each 5 ms tick, it receives the robot’s current joint positions, velocities, and the estimated block pose from ROS topics. 

- **Torque Message Publication.** The Python node computes a new 7D torque vector and publishes it as a ROS message to the C++ node. This node directly invokes the FCI’s real-time interface to set joint torques. 

- **Timing Synchronization.** We maintain a fixed 200 Hz loop, matching the simulator’s update frequency. This avoids aliasing or missed steps and ensures that delays in the real system resemble the random delays already modeled in simulation. _C.53. Camera-based Block Pose Estimation:_ The policy requires an estimate of the block’s 6D pose (position and 

- orientation). We implement a multi-camera setup with four commodity RGB cameras: 

- **Intrinsics and Extrinsics.** Each camera is calibrated via OpenCV’s standard calibration procedure. We record images of a checkerboard pattern from various viewpoints to obtain precise intrinsic parameters (focal length, principal point) and extrinsic transformations. 

- **AR Tag Tracking.** We attach an Alvar [44] fiducial marker to each face of the yoga block. Each camera runs the Alvar pose estimation pipeline. The final block pose is computed as the uniform average of valid detections. 

- **Placement Recommendations.** To improve coverage and reduce occlusions, we place two cameras at a lower height (approximately 40 cm above the table) and two cameras overhead (around 80 cm), all aimed toward the center of the workspace, inline with the base of the arm. This diversity of vantage points helps maintain robust tracking, even as the block is manipulated. 

- **ROS Integration.** Each camera node publishes pose estimates (with timestamps). A central ROS node fuses these estimates and broadcasts the block pose as a geometry_msgs/PoseStamped message at about 30–60 Hz. 

_C.53a. Summary:_ With this environment and training protocol, policies learned in simulation (under domain randomization and fast torque-control loops) exhibit a robust ability to transfer zero-shot to real hardware. Additionally, we encountered several limitations with the policy and workspace. For example, the policy sometimes pushed the block outside the robot’s workspace, making it impossible for the robot to reach it. We also observed that early versions of the policy moved the block too quickly, exceeding the robot’s force limit and causing it to pause. To address this, we introduced torque penalties, enabling the robot to maintain similar behavior while minimizing force. In summary we found that minimal engineering overhead was needed to align the MuJoCo-based environment with the real robot’s dynamic properties, underscoring the effectiveness of torque-based sim-to-real strategies with MuJoCo Playground. 



Fig. 18: Real Franka Emika Panda robot with a Robotiq gripper, pushing the yoga block to the goal region. 



Fig. 19: Policy inputs across domain randomized environments (64x64 pixels each) used while training the deployed PandaPickCubeCartesian agent. Lighting conditions, colors, brightness and camera pose are all randomized. 

### _C.6. Real-world Franka PickCube from Pixels_ 

To highlight the sim-to-real viability of our pixel-based environment, we highlight a robust real-world transfer using the Franka PickCube task. 

**Task Description.** In our PickCube task, the goal of the robot is to move and grasp a 2x2x3 cm upright cube and return it to a fixed target position. To enable robust deployment with a single RGB camera, we limit both the object randomization and the robot’s action space to a fixed Y-Z plane. We set the target in simulation to be (x, 0.0, 20.0), where x is set such that both the cube and the gripper initialize are in the same plane. Success is defined in simulation as lifting the object to a target height of 17 cm, and in real experiments as a stable grasp followed by lifting the object at least 10 cm above the table. The object’s starting position is randomized along the Y-axis within a 20 cm range centered around 0. Because we train with randomized camera pose and a black background, we lay white tape over the range of possible cube starting positions to allow the memory-less policy to gauge its progress from the grasping site to the target height. 

**Training.** We use a similar reward shaping scheme as [45], using sparse rewards to encourage lifting the cube and bringing it close to the target position and dense rewards to guide the policy search in between. To simplify reward tuning, the dense reward terms only consider progress: _rt_ = clip (<sup>�</sup> _i_<sup>_rt,i −_max(</sup><sup>_r_1</sup><sup>_, r_2</sup><sup>_, ..., rt−_1)</sup><sup>_,_0).Thishelpstoemphasizethesparsetermsduring</sup> training. To improve sample efficiency, we terminate the policy upon completion. We train with randomized lighting conditions, colors, brightness and camera pose for robust real-world transfer as shown in Figure 19. Similar to the non-prehensile task in Section C.51, we adopt a random delay of 0 to 5 steps for the gripper action, as the real system has a small delay before the grippers begin to close. With an environment step of 50 ms, this results in the agent learning to adapt to a action delay of up to 0.25 s. We find the resulting conservative grasp behaviour to be important for sim-to-real transfer. We disable all except the pair-wise collisions between the gripper fingers and cube to increase simulation throughput. 

**Agent.** Both the agent and critic networks comprise of a standard lightweight CNN architecture [42] followed by two hidden dense layers with size 256. Each channel of the input RGB image is individually normalised per sample by subtracting its mean and dividing it by its standard deviation. The policy network outputs a 3 value action from a single RGB camera looking down towards the gripper (Figure 20). The first two actions are Cartesian increments in the Y and Z directions that is subsequently solved by an inverse kinematics controller [21]. X movement is ignored so that the gripper is restricted to the vertical plane of the block. We discretize the third action dimension to command a closed gripper when the policy value is below zero and an open position when greater than or equal to zero. All values are outputted in the range -1 to 1. 

**Hardware.** We train our deployed policies within ten minutes on a single consumer-grade RTX 4090 GPU paired with a i9-14900KF processor. See Section D.1 for training curves for the PandaPickCubeCartesian environment. We deploy on a Franka Research arm with an Intel D435 Realsense camera, using an RTX 3090 GPU for policy inference running at 15Hz. 

**Control and Communication Pipeline.** We use a C++/ROS stack to execute our vision-based policies in real life. Camera images are square-cropped and down-sampled to 64x64 pixels before being passed to a lightweight C++ ONNX ROS Node for inference to produce a Cartesian increment and gripper command. This command is passed to a C++ ROS Node that computes joint commands using the same IK solution as used for training. These commands are output to a final ROS Node that wraps the Franka Control Interface (FCI) to control the robot joints. The control loop runs at 15 Hz, set by the incoming camera stream. We find that sim2real performance drastically improves from roughly calibrating the Cartesian increment scale in our physical setup to the one that the policy was trained on. 



Fig. 20: **Left.** Franka Research robot with a Realsense camera capturing input images. **Right.** Policy inputs from one embodied rollout. 

### APPENDIX D 

### MADRONA RENDERING ENVIRONMENTS 

### _D.1. RL Training Results_ 

MuJoCo Playground showcases two pixel observation environments using batch rendering; CartPoleBalance and PandaPickCubeCartesian. These two environments include complete training examples using brax PPO. We show the PPO training curves for both environments in Figures 21 and 22 across 5 seeds. 

CartPoleBalance is adjusted for pixel-based observations by decreasing the control frequency such that more simulated experience can be factored into training with less policy updates, and by re-adjusting the RL training hyperparameters as necessary. The observations are of dimension 64x64x3 and consist of the current and previous two rendered observations, collapsed into grayscale then transposed for CNN inference. PandaPickCubeCartesian is derived from PandaPickCube. Our changes for faster and more stable pixel-based training are described in Section C.6. 



<!-- Start of picture text -->
CartpoleBalance PandaPickCubeCartesian<br>70<br>8<br>60<br>6<br>50<br>4<br>40<br>PPO Mean 2<br>0.00 0.25 0.50 0.75 1.00 0 2 4<br>Env Steps 1e6 Env Steps 1e6<br>Episode Reward Episode Reward<br><!-- End of picture text -->

Fig. 21: Reward vs environment steps for brax PPO. All settings are run with 5 seeds on a single RTX 4090 GPU. 

### _D.2. Performance Benchmarking_ 

In this section we benchmark the througput of Madrona MJX GPU batch rendering. For reference, we plot our results alongside those from IsaacLab [41] and Maniskill3 [60]; data for IsaacLab and Maniskill3 is obtained from [60]. This is only a rough comparison as we only take steps to ensure similar hardware and timestep size, as a fully controlled performance benchmark is difficult due to the inherent differences between simulators. Our goal in these comparisons is to only highlight that our batch rendering is competitive with other state-of-the-art simulators that also include high-throughput rendering. 

The y-axis of Figure 23 measures the rate of generating environment transitions ( _st, ot, rt, st_ +1) with random actions, comprising the basic data unit of most on and off-policy training algorithms. The first subplot measures Cartpole simulation with computationally trivial state-based observations. The next three plots show the cost of generating transitions where _ot_ involves rendering with increasing resolution. 

Figure 24 evaluates how much of our throughput increase is due to MJX’s faster physics step. For each bar, the dark area shows the cost of the physics step and the non-overlapping light area shows the cost of generating the pixel observation. Note that lower values are better, as we display the inverse of frequency. While MJX’s faster physics simulation indeed benefits throughput at lower image resolutions, Madrona’s rendering speed improvements appear to be the primary driver of the measured speed-ups. 



<!-- Start of picture text -->
CartpoleBalance PandaPickCubeCartesian<br>8<br>60<br>6<br>40<br>4<br>20<br>2<br>PPO Mean<br>0 0<br>0 10 20 30 40 0 100 200 300<br>Wallclock Time (s) Wallclock Time (s)<br>Episode Reward Episode Reward<br><!-- End of picture text -->

Fig. 22: Reward vs wallclock time for brax PPO. All settings are run with 5 seeds on a single RTX 4090 GPU. 



Fig. 23: Comparison of raw environment-stepping throughput with prior simulators for CartpoleBalance with state-based and pixel observations of varying sizes. 



Fig. 24: Time-cost breakdown of unrolling physics simulation and rendering for CartpoleBalance with pixel observations. _Lower is better._ Per-step rendering time is stacked without overlap over physics simulation time. 

### _D.3. Bottlenecks in Pixels-based Training_ 

||**Env Step**|**with Pixels**|**and Inference**|**and Training**|
|---|---|---|---|---|
|**CartpoleBalance**|||||
|FPS|1_._37_×_10<sup>6</sup><br>|4_._03_×_10<sup>5</sup><br>|3_._41_×_10<sup>5</sup><br>|3_._13_×_10<sup>4</sup><br>|
|Time/Env Step (s)|7_._30_×_10<sup>_−_7</sup>|2_._48_×_10<sup>_−_6</sup>|2_._93_×_10<sup>_−_6</sup>|3_._20_×_10<sup>_−_5</sup>|
|**PandaPickCubeCa**|**rtesian**||||
|FPS|6_._40_×_10<sup>4</sup>|3_._69_×_10<sup>4</sup>|3_._60_×_10<sup>4</sup>|1_._56_×_10<sup>4</sup>|
|Time/Env Step (s)|1_._56_×_10<sup>_−_5</sup>|2_._71_×_10<sup>_−_5</sup>|2_._78_×_10<sup>_−_5</sup>|6_._39_×_10<sup>_−_5</sup>|



TABLE X: Raw throughput of our two pixel-based environments in various settings. _Env step_ : stepping the physics with random actions. _with Pixels_ : Same, with the overhead of rendering pixel-based observations. _with Inference_ : random actions are replaced with policy inference. _and Training_ : the speed of PPO training. Results averaged over 5 runs on an RTX4090. 

||**Physics**|**Rendering**|**Inference**|**Policy Update**|
|---|---|---|---|---|
|**CartpoleBalance**|||||
|Time/Env Step (s)|7_._30_×_10<sup>_−_7</sup>|1_._75_×_10<sup>_−_6</sup>|4_._49_×_10<sup>_−_7</sup>|2_._91_×_10<sup>_−_5</sup>|
|Fraction|0.02|0.06|0.01|0.91|
|**PandaPickCubeCa**|**rtesian**||||
|Time/Env Step (s)|1_._56_×_10<sup>_−_5</sup>|1_._15_×_10<sup>_−_5</sup>|6_._45_×_10<sup>_−_7</sup>|3_._62_×_10<sup>_−_5</sup>|
|Fraction|0.24|0.18|0.01|0.57|



TABLE XI: Breakdown of total training time by component for CartpoleBalance and PandaPickCubeCartesian tasks, derived from Table X. Results averaged over 5 runs on an RTX4090. 

Table XI isolates the contributions of policy rollout (physics simulation, rendering, inference) and policy update to the overall cost per step in a training loop. We amortize the cost of policy update per policy rollout step, setting _t_ 4 = _ttraining_ + _tinference_ + _trendering_ + _tenvstep_ , where _t_ 4 corresponds to _Time/Env Step_ in the last column of Table X. Working in reverse order through the table, we isolate each component. For example, _ttraining_ = _t_ 4 _−t_ 3 corresponds to the Policy Update _Time/Env Step_ . 

We see that in both of our provided pixel-based environments, the training speed bottleneck is shifted from rendering to policy updates. This is especially true for the Cartpole, as the policy and value architectures includes convolutions determined by the size of the input image regardless of robot and task complexity. The expensive architecture coupled with the trivial embodiment, shift over 90% of the training burden to network updates. For the Franka Panda environment, we buffer more of the computation into the physics by training with a lower control frequency. At 20 Hz control with a 5ms physics timestep, the policy makes only one decision per 10 simulator sub-steps. Similar to Cartpole, rendering is less of a bottleneck than the cost of processing the resultant images via convolutional-based network architectures. 

### APPENDIX E 

### REINFORCEMENT LEARNING HYPER-PARAMETERS 

In this section, we report the hyper-parameters used to train RL policies for all environments in MuJoCo Playground. 

### _E.1. DM Control Suite_ 



<!-- Start of picture text -->
Hyperparameter Default Value Environment-Specific Modifications<br>num timesteps 60,000,000 AcrobotSwingup, Swimmer, WalkerRun:<br>100,000,000<br>num evals 10<br>reward scaling 10.0<br>normalize observations True<br>action repeat 1 PendulumSwingUp: 4<br>unroll length 30<br>num minibatches 32<br>num updates per batch 16 PendulumSwingUp: 4<br>discounting 0.995 BallInCup: 0.95,<br>FingerSpin: 0.95<br>learning rate 1e-3<br>entropy cost 1e-2<br>num envs 2048<br>batch size 1024<br><!-- End of picture text -->

TABLE XII: Brax PPO hyperparameters. 



<!-- Start of picture text -->
Hyperparameter Default Value<br>madrona backend True<br>wrap env False<br>num timesteps 1,000,000<br>num evals 5<br>reward scaling 0.1<br>normalize observations True<br>action repeat 1<br>unroll length 10<br>num minibatches 8<br>num updates per batch 8<br>discounting 0.97<br>learning rate 5e-4<br>entropy cost 5e-3<br>num envs 1024<br>num eval envs 1024<br>batch size 256<br><!-- End of picture text -->

TABLE XIII: Brax PPO hyperparameters for vision-based environments. 

|**Hyperparameter**|**Default Value**|**Environment-Specific Modifications**|
|---|---|---|
|num<br>timesteps|5,000,000|Acrobot, Swimmer, Finger, Hopper,<br>CheetahRun, HumanoidWalk,<br>PendulumSwingUp,<br>WalkerRun:<br>10,000,000|
|num<br>evals|10||
|reward<br>scaling|1.0||
|normalize<br>observations|True||
|action<br>repeat|1|PendulumSwingUp: 4|
|discounting|0.99||
|learning<br>rate|1e-3||
|num<br>envs|128||
|batch<br>size|512||
|grad<br>updates<br>per<br>step|8||
|max<br>replay<br>size|1048576 * 4||
|min<br>replay<br>size|8192||
|network<br>factory.q<br>network<br>layer<br>norm|True||



TABLE XIV: Brax SAC hyperparameters. 

_E.2. Locomotion_ 

|**Hyperparameter**|**Default Value**|
|---|---|
|num<br>timesteps|100,000,000|
|num<br>evals|10|
|reward<br>scaling|1.0|
|normalize<br>observations|True|
|action<br>repeat|1|
|unroll<br>length|20|
|num<br>minibatches|32|
|num<br>updates<br>per<br>batch|4|
|discounting|0.97|
|learning<br>rate|3e-4|
|entropy<br>cost|1e-2|
|num<br>envs|8192|
|batch<br>size|256|
|max<br>grad<br>norm|1.0|
|policy<br>hidden<br>layer<br>sizes|(128, 128, 128, 128)|
|policy<br>obs<br>key|”state”|
|value<br>obs<br>key|”state”|



TABLE XV: Default Brax PPO hyperparameters. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|200,000,000|
|num<br>evals|10|
|num<br>resets<br>per<br>eval|1|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XVI: Brax PPO hyperparameters specific to Go1JoystickFlatTerrain and Go1JoystickRoughTerrain. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|100,000,000|
|num<br>evals|5|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XVII: Brax PPO hyperparameters specific to Go1Handstand and Go1Footstand. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|200,000,000|
|num<br>evals|10|
|discounting|0.95|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XVIII: Brax PPO hyperparameters specific to Go1Backflip. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|50,000,000|
|num<br>evals|5|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XIX: Brax PPO hyperparameters specific to Go1Getup. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|400,000,000|
|num<br>evals|16|
|num<br>resets<br>per<br>eval|1|
|reward<br>scaling|0.1|
|unroll<br>length|32|
|num<br>updates<br>per<br>batch|5|
|discounting|0.98|
|learning<br>rate|1e-4|
|entropy<br>cost|0|
|num<br>envs|32768|
|batch<br>size|1024|
|clipping<br>epsilon|0.2|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 64)|
|value<br>hidden<br>layer<br>sizes|(256, 256, 256, 256)|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XX: Brax PPO hyperparameters specific to G1Joystick. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|400,000,000|
|num<br>evals|16|
|num<br>resets<br>per<br>eval|1|
|reward<br>scaling|0.1|
|unroll<br>length|32|
|num<br>updates<br>per<br>batch|5|
|discounting|0.98|
|learning<br>rate|1e-4|
|entropy<br>cost|0|
|num<br>envs|32768|
|batch<br>size|1024|
|clipping<br>epsilon|0.2|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 64)|
|value<br>hidden<br>layer<br>sizes|(256, 256, 256, 256)|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XXI: Brax PPO hyperparameters specific to T1Joystick. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|100,000,000|
|num<br>evals|10|
|num<br>resets<br>per<br>eval|1|
|clipping<br>epsilon|0.2|
|discounting|0.99|
|learning<br>rate|1e-4|
|entropy<br>cost|0.005|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XXII: Brax PPO hyperparameters specific to Berkeley Humanoid. 

_E.3. Manipulation_ 

|**Hyperparameter**|**Default Value**|
|---|---|
|normalize<br>observations|True|
|reward<br>scaling|1.0|
|policy<br>hidden<br>layer<br>sizes|(32, 32, 32, 32)|
|policy<br>obs<br>key|”state”|
|value<br>obs<br>key|”state”|



TABLE XXIII: Default Brax PPO hyperparameters. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|150,000,000|
|num<br>evals|10|
|unroll<br>length|40|
|num<br>minibatches|32|
|num<br>updates<br>per<br>batch|8|
|discounting|0.97|
|learning<br>rate|3e-4|
|entropy<br>cost|1e-2|
|num<br>envs|1024|
|batch<br>size|512|
|policy<br>hidden<br>layer<br>sizes|(256, 256, 256, 256)|



TABLE XXIV: Brax PPO hyperparameters for AlohaSinglePegInsertion. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|40,000,000|
|num<br>evals|4|
|unroll<br>length|10|
|num<br>minibatches|32|
|num<br>updates<br>per<br>batch|8|
|discounting|0.97|
|learning<br>rate|1e-3|
|entropy<br>cost|2e-2|
|num<br>envs|2048|
|batch<br>size|512|
|policy<br>hidden<br>layer<br>sizes|(32, 32, 32, 32)|
|num<br>resets<br>per<br>eval|1|



TABLE XXV: Brax PPO hyperparameters for PandaOpenCabinet. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|5,000,000|
|num<br>evals|5|
|unroll<br>length|10|
|num<br>minibatches|8|
|num<br>updates<br>per<br>batch|8|
|discounting|0.97|
|learning<br>rate|5.0e-4|
|entropy<br>cost|7.5e-3|
|num<br>envs|1024|
|batch<br>size|256|
|reward<br>scaling|0.1|
|policy<br>hidden<br>layer<br>sizes|(256, 256)|
|num<br>resets<br>per<br>eval|1|
|max<br>grad<br>norm|1.0|



TABLE XXVI: Brax PPO hyperparameters for PandaPickCubeCartesian. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|20,000,000|
|num<br>evals|4|
|unroll<br>length|10|
|num<br>minibatches|32|
|num<br>updates<br>per<br>batch|8|
|discounting|0.97|
|learning<br>rate|1e-3|
|entropy<br>cost|2e-2|
|num<br>envs|2048|
|batch<br>size|512|
|policy<br>hidden<br>layer<br>sizes|(32, 32, 32, 32)|



TABLE XXVII: Brax PPO hyperparameters for PandaPickCube. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|2,000,000,000|
|num<br>evals|10|
|unroll<br>length|100|
|num<br>minibatches|32|
|num<br>updates<br>per<br>batch|8|
|discounting|0.994|
|learning<br>rate|6e-4|
|entropy<br>cost|1e-2|
|num<br>envs|8192|
|batch<br>size|512|
|num<br>resets<br>per<br>eval|1|
|num<br>eval<br>envs|32|
|policy<br>hidden<br>layer<br>sizes|(64, 64, 64, 64)|



TABLE XXVIII: Brax PPO hyperparameters for PandaRobotiqPushCube. 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|100,000,000|
|num<br>evals|10|
|num<br>minibatches|32|
|unroll<br>length|40|
|num<br>updates<br>per<br>batch|4|
|discounting|0.97|
|learning<br>rate|3e-4|
|entropy<br>cost|1e-2|
|num<br>envs|8192|
|batch<br>size|256|
|num<br>resets<br>per<br>eval|1|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|policy<br>obs<br>key|”state”|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XXIX: Brax PPO hyperparameters for LeapCubeRotateZAxis). 

|**Hyperparameter**|**Value**|
|---|---|
|num<br>timesteps|100,000,000|
|num<br>evals|20|
|num<br>minibatches|32|
|unroll<br>length|40|
|num<br>updates<br>per<br>batch|4|
|discounting|0.99|
|learning<br>rate|3e-4|
|entropy<br>cost|1e-2|
|num<br>envs|8192|
|batch<br>size|256|
|num<br>resets<br>per<br>eval|1|
|policy<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|value<br>hidden<br>layer<br>sizes|(512, 256, 128)|
|policy<br>obs<br>key|”state”|
|value<br>obs<br>key|”privileged<br>state”|



TABLE XXX: Brax PPO hyperparameters for LeapCubeReorient. 

|**Hyperparameter**|**Value**|
|---|---|
|madrona<br>backend|True|
|wrap<br>env|False|
|normalize<br>observations|True|
|reward<br>scaling|1.0|
|policy<br>hidden<br>layer<br>sizes|(32, 32, 32, 32)|
|num<br>timesteps|5,000,000|
|num<br>evals|5|
|unroll<br>length|10|
|num<br>minibatches|8|
|num<br>updates<br>per<br>batch|8|
|discounting|0.97|
|learning<br>rate|5.0e-4|
|entropy<br>cost|7.5e-3|
|num<br>envs|1024|
|batch<br>size|256|
|reward<br>scaling|0.1|
|num<br>resets<br>per<br>eval|1|



TABLE XXXI: Brax PPO hyperparameters for vision-based PandaPickCubeCartesian. 

