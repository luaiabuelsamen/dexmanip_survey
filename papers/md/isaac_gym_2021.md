# **Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning** 

**Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey,** 

**Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, Gavriel State** 

NVIDIA 

```
{vmakoviychuk,lwawrzyniak,kellyg,michellel,kstorey,mmacklin,
```

```
dhoeller,nrudin,aallshire,ahanda,gstate}@nvidia.com
```

## **Abstract** 

Isaac Gym offers a high performance learning platform to train policies for wide variety of robotics tasks directly on GPU. Both physics simulation and the neural network policy training reside on GPU and communicate by directly passing data from physics buffers to PyTorch tensors without ever going through any CPU bottlenecks. This leads to blazing fast training times for complex robotics tasks on a single GPU with 2-3 orders of magnitude improvements compared to conventional RL training that uses a CPU based simulator and GPU for neural networks. We host the results and videos at `https://sites.google.com/view/ isaacgym-nvidia` and isaac gym can be downloaded at `https://developer. nvidia.com/isaac-gym` . 

## **Contents** 

|**1**|**Intr**|**oductio**|**n**|**4**|
|---|---|---|---|---|
|**2**|**Bac**|**kgroun**|**d**|**6**|
||2.1|Paralle|lization Strategy . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>6|
|||2.1.1|CPU Simulations . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>6|
|||2.1.2|GPU Simulations . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>7|
||2.2|Simul|ation Setup . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>8|
||2.3|Tensor|API<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>8|
|||2.3.1|Python Interface<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>9|
|||2.3.2|Physics State Tensors . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>9|
|||2.3.3|Physics Control Tensors . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>10|
|**3**|**Phy**|**sics Sim**|**ulation**|**10**|
|**4**|**Env**|**ironme**|**nts**|**11**|
|**5**|**Cha**|**racteris**|**ing Simulation Performance**|**13**|
||5.1|Ant<br>|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>13|
||5.2|Huma|noid . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>13|
||5.3|Shado|w Hand . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>14|
|**6**|**Cha**|**racteris**|**ing Environment Performance**|**15**|
||6.1|Locom|otion environments<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>15|
|||6.1.1|Ant . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>15|
|||6.1.2|Humanoid . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>15|
|||6.1.3|Ingenuity . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>15|
|||6.1.4|ANYmal Robot Locomotion . . . . . . . . . . . . . .|. . . . . . . . . . .<br>15|
||6.2|Huma|noid Character Animation<br>. . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>16|
||6.3|Franka|Cube Stacking . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>17|
||6.4|Robot|ic Hands<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>17|
|||6.4.1|Shadow Hand . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>18|
|||6.4.2|TriFinger . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>19|
|||6.4.3|Allegro Hand . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>20|
|**7**|**Sum**|**mary**||**20**|
|**8**|**Ack**|**nowled**|**gements**|**21**|
|**A **|**App**|**endix**||**25**|
||A.1|Tendo|ns . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>25|
|||A.1.1|Fixed Tendons<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>25|



2 

||A.1.2|Spatial Tendons . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>25|
|---|---|---|---|
|A.2|Observ|ations & Rewards . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>25|
||A.2.1|Ant and Humanoid environments<br>. . . . . . . . . . .|. . . . . . . . . . .<br>25|
||A.2.2|Locomotion environments . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>26|
||A.2.3|Robotic Hands . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>28|
|A.3|Hyperp|arameters for Training PPO . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>30|
|A.4|Shado|w Hand Details . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>30|
||A.4.1|Randomizations<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>30|
||A.4.2|OpenAI Observations . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>31|



3 

## **1 Introduction** 



Figure 1: Isaac Gym allows high performance training on a variety of robotics environments. We benchmark on 8 different environments that offer a wide range of complexity and show the strengths of the simulator in blazing fast policy training on a single GPU. _Top_ : Ant, Humanoid, Franka-cube-stack, Ingenuity. _Bottom_ : Shadow Hand, ANYmal, Allegro, TriFinger. 

In recent years, reinforcement learning (RL) has become one of the most promising research areas in machine learning and has demonstrated great potential for solving sophisticated decision-making problems. Deep reinforcement learning (Deep RL) has achieved superhuman performance in very challenging tasks, ranging from classic strategy games such as Go and Chess [1], to real-time computer games like StarCraft [2] and DOTA [3]. It has also shown impressive results in robotic settings, including legged locomotion [4] and dexterous manipulation [5]. 

Simulators play a key role in training robots improving both the safety and iteration speed in the learning process. Training a humanoid robot that walks up and down stairs in the real world can lead to damage to its machinery and the environment, including humans that are working on the robot. An alternative is to train inside simulators that offer an efficient and scalable platform via trial-and-error with no safety issues as observed in the real world. To date, most researchers have relied on a combination of CPUs and GPUs to run reinforcement learning system [5]. Different parts of the computer tackle different steps of the physics simulation and rendering process. CPUs are used to simulate environment physics, calculate rewards, and run the environment, while GPUs are used to accelerate neural network models during training and inference as well as rendering if required. 

However, switching back and forth between CPU cores optimized for sequential tasks and GPUs which offer large-scale parallelism is by nature inefficient, requiring data to be transferred between different parts of the system at multiple points during the training process. Therefore, scalability of deep reinforcement learning in robotics is faced with two critical bottlenecks: 1) enormous computational requirements and 2) limited simulation speed. These problems are especially challenging when learning long-horizon behaviours for robots with high degrees of freedom. 

Popular physics engines like MuJoCo[6], PyBullet[7], DART[8], Drake[9], V-Rep[10] _etc._ need large CPU clusters to solve challenging RL tasks naturally face these bottlenecks. For instance, in [11], almost 30,000 CPU cores (920 worker machines with 32 cores each) were used to train a robot to solve the Rubik’s Cube task using RL. In a similar task, [5] used a cluster of 384 systems with 6144 CPU cores, plus 8 NVIDIA V100 GPUs, and required 30 hours of training for RL to converge. 

One way to speed-up simulation and training is to make use of hardware accelerators. GPUs have enjoyed enormous success in computer graphics are also naturally suited for highly parallel simulations. This approach was taken by [12], and showed very promising results running simulation on GPU, proving that it is possible to greatly reduce both training time as well as computational resources required to solve very challenging tasks using RL. However, some bottlenecks were still not addressed in the work – simulation was on GPU but physics state was copied back to CPU. There, observations and rewards were calculated using optimized C++ code and later copied back to GPU 

4 

where policy and value networks ran. Furthermore, only simplified physics-based scenarios were trained, rather than representative robotic environments, and no attempt was made to show sim2real. 

To address these bottlenecks, we present **Isaac Gym** - an end-to-end high performance robotics simulation platform. It runs an end-to-end GPU accelerated training pipeline, which allows researchers to overcome the aforementioned limitations and achieves 2-3 orders of magnitude of training speed-up in continuous control tasks. Isaac Gym leverages NVIDIA PhysX [13] to provide a GPU-accelerated simulation back-end, allowing it to gather experience data required for robotics RL at rates only achievable using a high degree of parallelism. It provides a PyTorch tensor-based API to access the results of physics simulation natively on the GPU. Observation tensors can be used as inputs to a policy network and the resulting action tensors can be directly fed back into the physics system. We note that others [14] have recently begun attempting an approach similar to Isaac Gym with respect to running end-to-end training on hardware accelerators. 

With the end-to-end approach, roll-outs of observation, reward, and action buffers can stay on the GPU for the entire learning process, eliminating the need to read data back from the CPU. This set-up permits tens of thousands of simultaneous environments on a single GPU, allowing researchers to easily run experiments locally on their desktops that previously required an entire data center and to solve previously out of reach tasks using just a small GPU server. 

Isaac Gym provides a straightforward API for creating and populating a scene with robots and objects, supporting loading data from the common URDF and MJCF file formats. Each environment is duplicated as many times as needed, while preserving the ability for variations between copies ( _e.g._ via Domain Randomization [15]). Environments are simulated simultaneously in parallel without interaction with other environments. Using a fully GPU-accelerated simulation and training pipeline can help lower the barrier for research, enabling solving of tasks with a single GPU that were previously only possible on massive CPU clusters. Isaac Gym also includes a basic Proximal Policy Optimization (PPO) implementation and a straightforward RL task system, but users may substitute alternative task systems or RL algorithms as desired. While the included examples use PyTorch, users should also be able to integrate with TensorFlow training libraries with further customization. An overview of the system is provided in Figure 2. 



<!-- Start of picture text -->
Load Existing Robot Models<br>Learning Framework<br>step command, observation<br>action tensors tensors<br>Environment Logic<br>(Observation, reward, non-physics logic)<br>action, config environment Result:<br>tensors states Learn on 1000s of realistic robots in parallel<br>IsaacGym Tensor API<br>PhysX<br>1 GPU<br><!-- End of picture text -->

Figure 2: An illustration of the Isaac Gym pipeline. The Tensor API provides an interface to Python code to step the PhysX backend, as well as get and set simulator states, directly on the GPU, allowing a 100-1000x speedup in the overall RL training pipeline while providing high-fidelity simulation and the ability to interface with existing robot models. 

5 

### **Summary of Results** 

Our major contributions include: 

- Development of high-fidelity GPU-accelerated robotics simulator for robot learning tasks. 

- A Tensor API in Python providing direct access to physics buffers by wrapping them into PyTorch tensors without going through any CPU bottlenecks. 

- Implementation of multiple highly complex robotic manipulation environments which can be simulated at hundreds of thousands of steps per second on a single GPU. 

- High-performance training results using Isaac Gym with Deep Reinforcement Learning on challenging robotic environments. 

Our major empirical results include: 

- We achieve significant speed-ups in training various simulated environments: Ant and Humanoid environments can achieve performant locomotion in 20 seconds and 4 minutes respectively, ANYmal [16] in under 2 minutes, Humanoid character animation using AMP [17] in 6 minutes and cube rotation with Shadow Hand in 35 minutes all on a **single NVIDIA A100 GPU** . 

- Additionally, we reproduce OpenAI Shadow Hand cube training setup [5] with asymmetric actor-critic and domain randomization. We show that we can achieve similar performance to OpenAI results of 20 consecutive successes with feed forward and 37 consecutive successes with LSTM networks with a success tolerance of 0.4 rad in about 1 hour and 6 hours on an average respectively on A100. In contrast, OpenAI effort required 30 hours and 17 hours respectively on a combination of a CPU cluster (384 CPUs with 16 cores each) and 8 NVIDIA V100 GPUs with MuJoCo [6] using a conventional RL training setup. It is worth mentioning that since OpenAI show results with only 1 seed, comparing our best seed we find that we achieve 37 consecutive successes with LSTMs in just 2.5 hours. 

- We also demonstrate sim-to-real transfer results on ANYmal and TriFinger which further showcases the ability of our simulator to perform high-fidelity contact rich manipulation. 

## **2 Background** 

### **2.1 Parallelization Strategy** 

There are many approaches to parallelizing physics simulations. We outline these approaches here and justify our design decisions in the context of GPU-accelerated simulation tailored towards learning algorithms. Isaac Gym was developed to maximize the throughput of physics-based machine learning algorithms with particular emphasis on simulations that require large numbers of environment instances executing in parallel. 

### **2.1.1 CPU Simulations** 

When physics simulation runs on CPU, multiple threads can be used to distribute computation among the available cores. The most straightforward strategy is simulating one environment instance per thread. In this approach, scaling is limited by the number of physical cores in the system. On a 64-core hyper-threaded CPU, we could run up to 128 environments in parallel, but CPUs with a large number of cores are typically clocked lower to prevent overheating. Running tens or hundreds of threads comes with other potential pitfalls including synchronization, context-switching overhead, and memory bandwidth limitations. To scale further, we would need to use a multi-CPU setup or build a cluster, which introduces additional communication overhead. 

Running a single environment instance per thread in its own dedicated physics scene can be inefficient. There is some overhead involved in setting up, executing, and gathering the results of each physics 

6 

step. The simpler the environment, the more significant the overhead. To mitigate this, we can pack multiple environments into a single physics scene. For example, we could split 1024 environments into eight physics scenes with 128 environments each. Each scene can run in its own thread. Extra provisions are needed to ensure that environments in the same scene do not interact with each other physically, which can be done using contact filtering and other methods. 

### **2.1.2 GPU Simulations** 

Running the physics simulation on GPU can result in significant speedups, especially for large scenes with thousands of individual actors. On the GPU, the physics engine can parallelize computations at the level of individual shapes, bodies, or joints. High-end GPUs require many thousands of objects to effectively utilize their streaming multiprocessor architecture. This makes them a good match for running simulations with thousands of environment instances. On GPU, we don’t need to worry about splitting the environments into multiple scenes. In fact, the opposite is generally true - we want to pack everything into a single scene to take advantage of the deep fine-grained parallelism and maximize the overall throughput. 

Physics simulations on a GPU is not new. In previous work, we demonstrated good results with running GPU physics simulations for reinforcement learning [12]. In this work, the GPU was used as a co-processor that accelerates the physics simulation, while the API for getting physics state and applying controls was CPU-based. There are, however, performance bottlenecks with this strategy. In a reinforcement learning pipeline, physics simulation is just one part of the system. After a physics step, we need to get the latest physics state to compute observations and rewards. If these computations are done on the CPU, we need to transfer the physics state from the GPU. While modern hardware architectures can achieve impressive data transfer speeds, large simulations can incur nontrivial overhead. Then, the raw physics state needs to be processed on the CPU to compute observations and rewards, which is subject to similar parallelization challenges as discussed above due to the limited number of CPU cores. Next, the observations and rewards need to be copied from system memory back to device memory for the reinforcement learning algorithm. After the learning step, a set of actions is generated by the policy network on the GPU. These actions need to be copied to the CPU so that they can be converted to physics simulation inputs. Those inputs end up being copied to the GPU again to run the next step of physics simulation on the device. 

Isaac Gym eliminates those inefficiencies by keeping all of the computations on the GPU. Stepping physics, computing observations and rewards, and applying actions are performed on the GPU without ever copying large quantities of data between devices. Two new features were added to PhysX to facilitate this. First, PhysX GPU simulations can run without fetching the results to the CPU after every step. Second, a new direct GPU API was added to access the current state, submit state changes, and apply control inputs in GPU buffers. In Figure 3, we contrast the traditional RL experience collection pipeline with our high throughput fully GPU-based pipeline. 





(a) Traditional RL experience collection. 

(b) Isaac Gym experience collection. 

Figure 3: **(a)** Traditional RL experience collection pipelines often use CPU based physics engines which quickly become the bottleneck. **(b)** In contrast, Isaac Gym not only runs physics on the GPU but also directly copies the physics data to the deep neural network framework using CUDA interoperatability without ever using CPU in the process. This massively improves the performance of RL training process leading to significantly faster training times. 

7 

### **2.2 Simulation Setup** 

Isaac Gym provides a simple procedural API to create environments and populate them with actors. It supports loading assets from URDF and MJCF file formats. These assets can be instanced multiple times in simulation environments to create actors. In the underlying PhysX engine, single-body actors are created as rigid dynamics and multi-body actors are created as reduced coordinate articulations. During the setup phase, users can set initial actor poses, configure joint drives, and customize rigid body properties and physics materials. Most joint and rigid body properties can be changed during the simulation as well, which facilitates domain randomization without stopping and restarting the simulation. Below we provide definitions of some useful terms. 

**Actor:** An entity composed of rigid bodies connected via joints. It can be created via direct loading of a URDF model or XML file composed of either meshes or primitive shapes. 

**Rigid Bodies:** A primitive shape or a mesh model that comprises an actor is called a rigid body. The positions, rotations and velocities of a rigid body can be obtained via the API. 

**DOF States:** Rigid bodies are connected by various joints. A joint can have 0 or more degrees of freedom. Fixed joints have no DOFs, revolute and prismatic joints have 1 DOF and spherical joints have 3 DOFs. The DOF states, which include joint position and velocity, can be obtained via the API. 

The setup code runs on the CPU to allow flexibility in per-instance setup, but once the simulation starts Isaac Gym provides a tensor API that can be used to interact with the running simulation on either CPU or GPU. Users can specify the device to be used for the simulation and the tensor interface in the simulation parameters. 



Figure 4: Tensors associated with the scene composed of multiple copies of the same environment simulating different variations all running in parallel. Each actor ( _e.g._ table, box or franka) has various bodies and their corresponding positions, quaternions and velocities are stored directly in PyTorch tensors. 

### **2.3 Tensor API** 

Isaac Gym provides a data abstraction layer over the physics engine. This allows us to support multiple physics engines with a shared front-end API. In this work, the physics engine is PhysX, although some limited tensor API functionality is available with the FleX physics engine as well. 

Instead of calling physics engine functions directly, users can access all of the physics data in flat buffers. This data-oriented approach allows us to eliminate a lot of overhead caused by looping over tens of thousands of individual simulation actors in user code. Physics state is exposed to Python users as global tensors. For example, all rigid body states can be found in a single rigid body state tensor. Figure 4 shows a typical Isaac Gym scene composed of various copies of the same environment simulating different variations all running in parallel and the corresponding tensors associated with it. Control inputs can be applied using global tensors as well. For example, applying forces to all rigid bodies in the simulation can be done using a single function call that takes a tensor containing all of the forces. Users can create custom views or slices of the global tensors to suit their needs. When 

8 

|Tensor|Description|Shape|Usage|
|---|---|---|---|
|Actor root state|State of all actor root bodies (position, orientation,<br>linear and angular velocity).|(_NA,_13)|Get/Set|
|DOF state|State of all degrees of freedom (position and veloc-<br>ity).|(_ND,_2)|Get/Set|
|Rigid body state|State of all rigid bodies (position, orientation, lin-<br>ear and angular velocity).|(_NB,_13)|Get|
|DOF forces|Net forces experienced at each degree of freedom.|_ND_|Get|
|Rigid body forces|Rigid body forces and torques experienced at force<br>sensor locations.|(_NF ,_6)|Get|
|Net contact forces|Net forces experienced byeach rigid body.|(_NB,_3)|Get|
|Jacobian matrix|Jacobian matrices for a homogeneous group of<br>actors.|Variable|Get|
|Mass matrix|Generalized mass matrices for a homogeneous<br>groupof actors.|Variable|Get|



Table 1: Physics state tensors. _NA_ is the total number of actors, _NB_ is the total number of rigid bodies (including articulation links), _ND_ is the total number of degrees of freedom, and _NF_ is the total number of rigid body force sensors. 

multiple environment instances are packed into the simulation, it is possible to create custom views of the data with the environment index as one of the dimensions. This makes it easy to vectorize observation and reward computations by running GPU kernels on multiple environments in parallel. 

### **2.3.1 Python Interface** 

The core of Isaac Gym is implemented using C++ and CUDA. It is completely independent of any Python frameworks commonly used in machine learning. To make the data easily accessible to Python users, Isaac Gym provides utilities that can "wrap" the raw data buffers as tensor objects in common machine learning frameworks like PyTorch. The tensor-wrapping utilities make it possible to share the native CPU or GPU buffers with Python without any copying overhead. 

A powerful feature of Isaac Gym is the ability to run the same code on either CPU or GPU by simply toggling a flag. Python users do not need to write custom CUDA or C++ kernels to compute observations, rewards, or actions. When physics state and control tensors are wrapped as PyTorch tensors, users can take advantage of TorchScript JIT to compile their Python functions to lower level scripts which orchestrate the training pipeline quickly. 

### **2.3.2 Physics State Tensors** 

Physics state tensors are used to obtain state snapshots of a running simulation. Isaac Gym allows for interacting with the simulation using maximal and reduced coordinates. Physics state includes the kinematic state of rigid bodies and degrees of freedom (DOFs). Rigid body state consists of position, orientation (quaternion), linear velocity, and angular velocity. DOF state includes position and velocity. In the code snippet below we show how to access them through the API. 

```
#Acquiretensordescriptors
#-Rawstoragebufferindependentofclientframework.
#-StoragewillbeonGPUifusingGPUpipeline ,CPUotherwise.
#-SamecodeforCPUandGPUjustdifferentdevice.
root_state_desc=gym. acquire_actor_root_state_tensor (sim)
dof_state_desc=gym. acquire_dof_state_tensor (sim)
#PyTorchinterop
#Nodatacopying ,justwrapthegymbuffersastorchtensors.
#Therootstatetensorcapturesthestateoftherootbodiesofallactors.
root_states=gymtorch. wrap_tensor ( root_state_desc )
dof_states=gymtorch. wrap_tensor ( dof_state_desc )
#obtainingphysicsstates
#Physicsstateincludeskinematicstatesofrigidbodiesanddegreesoffreedom(DOFs).
```

9 

```
root_state_vec=root_states.view(num_envs ,actors_per_env ,13)
dof_state_vec=dof_states.view(num_envs ,dofs_per_env ,13)
root_p=root_states [... ,0:3]#positionsofrigidbodies
root_q=root_states [... ,3:7]#rotations ,inquaternions ,ofrigidbodies
root_v=root_states [... ,7:10]#linearvelocitiesofrigidbodies
root_a=root_states [... ,10:13]#angularvelocitiesofrigidbodies
dof_p=dof_state_vec [... ,0]#jointpositions
dof_v=dof_state_vec [... ,1]#jointvelocities
```

Obtaining state information by wrapping physics buffers into PyTorch tensors. CUDA interoperability allows copying the data directly without ever going through the host. 

Revolute DOFs use radians and linear DOFs use meters for units. Additional state data includes contact forces, rigid body force sensors, and DOF force sensors. To support operational space control and inverse kinematics applications, Isaac Gym also provides Jacobian and generalized mass matrices which can be obtained for articulated actors. 

The available state tensors are listed in Table 1. Most of the state tensors are read-only, except the root state tensor and the DOF state tensor. These two tensors play a special role, because they can be used to fully set the poses and velocities of actors. This can be used during environment resets, when new poses are generated or original poses need to be restored. The root state tensor captures the state of the root bodies of all actors. For single-body actors, the root state fully captures their poses and velocities in maximal coordinates. For articulated actors, the root state can be used to "teleport" them without changing the poses of the descendant articulation links. The DOF state tensor can be used to configure the descendant articulation links using reduced coordinates. Setting new DOF states does not affect the root state. For fixed-base articulated actors, such as mounted robotic arms, the DOF state tensor fully captures the articulation poses and velocities. Users can apply new root and DOF states for all actors at once or to a limited subset using an index buffer. This allows resetting a subset of environments without affecting the rest. 

### **2.3.3 Physics Control Tensors** 

Physics simulation inputs include forces, torques, and PD controls such as position and velocity targets. Forces and torques can be applied to rigid bodies and DOFs. PD targets are applied to DOFs that have been configured to use position or velocity drives. Users can configure the drive parameters like stiffness and damping using a separate API. Table 2 lists the available control tensors. The control tensors are typically created in a higher-level framework like PyTorch, but can be efficiently shared with Isaac Gym using the tensor-wrapping utilities. 

|Tensor|Description|Shape|Applied to|
|---|---|---|---|
|DOF actuation forces|Torques or linear forces to be<br>applied to degrees of freedom.|_ND_|All actors or indexed subset|
|DOF position targets|PD position targets for<br>degrees of freedom.|_ND_|All actors or indexed subset|
|DOF velocity targets|PD velocity targets for<br>degrees of freedom.|_ND_|All actors or indexed subset|
|Rigid body forces|Forces to be applied to<br>rigid bodies.|(_NB,_3)|All rigid bodies|
|Rigid body torques|Torques to be applied to<br>rigid bodies.|(_NB,_3)|All rigid bodies|



Table 2: Physics control tensors. _NB_ is the total number of rigid bodies (including articulation links) and _ND_ is the total number of degrees of freedom. 

## **3 Physics Simulation** 

Robots are simulated using PhysX [13] reduced coordinate articulations. Any individual rigid bodies may be simulated using either maximal coordinate rigid bodies or single-link reduced coordinate articulations. Articulations with a single link and rigid bodies are equivalent and interchangeable. 

10 

We also support tendons to actuate degrees of freedom and they are simulated in PhysX using Fixed Tendon mechanics. The physics of tendons are described in detail in Section A.1. We tested the dynamics of tendons using the Shadow Hand simulation environment, described in Section 6.4.1. 

We use the Temporal Gauss Seidel (TGS) [18] solver to compute the future states of objects in our physics simulation. The TGS solver uses the observation that sub-stepping a simulation with a single gauss-seidel solver iteration yields significantly faster convergence than running larger steps with more solver iterations. It folds this process efficiently into the iteration process, calculating the velocity at the end of each iteration and accumulating these velocities (scaled by _dt/N_ , where _N_ is the number of iterations) into a per-body accumulated delta buffer. This delta buffer is projected onto the constraint Jacobians and added to the bias terms in the constraints. This approach adds only a few additional operations to a more traditional Gauss-Seidel solver, producing almost identical performance cost per-iteration. However, it achieves the same effect on convergence as having sub-stepped the simulation without the computational expense. With positional joint constraints, an additional rotational term is calculated for joint anchors to improve handling of non-linear motion to avoid linearization artifacts. This term is not necessary (and in fact undesirable) to add to contacts. Various parameters exposed to the user to tune the simulator are described in Table 3. 

|Parameter|Description|
|---|---|
|Delta time (dt)|Controls time-step size|
|Gravity<br>i|Controls the gravity in the scene|
|Collision filtering|Filters collisions between shapes|
|Position iterations|Biased (velocity + positional error correcting) solver iterations|
|Velocity iterations<br>i|Unbiased (velocity error only correcting) solver iterations|
|Max bias coefficient|Limits the magnitude of position error bias Friction|
|Restitution|Controls bounce<br>i|
|Static/dynamic friction|Static and dynamic friction coefficients|
|<br>Bounce threshold|i<br>Relative normal velocitylimit below which restitution is ignored|
|Rest offset|Distance at which shapes are held separated. Default is 0 but can<br>be increased to hold objects atgap. Useful for thin objects.|
|Friction offset threshold|Distance at which friction anchors are discarded<br>(static friction depends on friction anchor caching)|
|Solver offset slop|An epsilon value used to correct for round-off errors in contact<br>gen. Corrects small skew effects with rollingspheres or capsules.|
|Friction correlation distance|Distance at which contacts are merged into a single<br>friction constraint|
|Max force|Per-body and per-contact force limits<br>i|
|Drive stiffness|Positional error correction coefficient of a PD controller<br>i|
|Drive damping|i<br>Velocity error correction coefficient of a PD controller|
|<br>Joint friction|i<br>Per-joint frictional term. Simulates dry friction in a joint.|
|Joint armature|<br>Per-joint armature term - simulates motor inertia.|
|Body/link Damping|World-space linear/angular damping on each body/link|
|Max velocity|Linear/angular velocitylimitsper-body|



Table 3: Parameters exposed to tune the simulator. 

## **4 Environments** 

We implemented a diverse set of environments covering different application areas. Here we describe a subset of representative examples and key points related to the training. Benchmark results on the simulation performance and training results are presented in the subsequent sections. 

All environments are trained using the Proximal Policy Optimization algorithm [19], using rl_games, a highly-optimized GPU end-to-end implementation from [20]. This implementation vectorizes observations and actions on GPU allowing us to take advantage of the parallelization provided by the simulator. We list the environments used in our experiments below: 

11 

### **Environments used** 

1. **Locomotion Environments** 

   - Ant 

   - Humanoid 

   - Ingenuity 

   - ANYmal 

2. **Franka Cube Stacking** 

3. **Humanoid Character Animation** 

4. **Robotic Hands** 

   - Shadow 

   - Allegro 

   - Trifinger 

While Ant and Humanoid are relatively simple environments popularised by MuJoCo continuous control benchmarks, the strength of our simulator really shines when training on environments that are rich in complexity particularly robotic hands. Various meta-data related to simulation setup for these environments is in Table 4. 

### **Key Experimental Details** 

- Unless stated otherwise, all experiments are done on a system with a **single NVIDIA A100 GPU** and a single 3.7GHz Intel i7-8700K CPU 

- All training runs for each environment are **averaged over 5 seeds** . The reward curves are plotted with _µ ± σ_ regions. 

- All the environments by default follow symmetric actor-critic approach with shared observations as well as shared network for policy and value functions. Sharing the network allows faster forward passes and improves training. 

- Moreover, for Shadow Hand and TriFinger, we also use an asymmetric actor critic approach [21] with policy observations that are closest to real world settings while value function receives privileged state information from simulation as well as the observations received by the policy. This approach is naturally suited for sim-to-real transfers. 

- For all environments trained with feed forward networks we use a discount factor of _γ_ = 0 _._ 99 while LSTM networks use _γ_ = 0 _._ 998. We use a GAE discount factor, _λ_ = 0 _._ 95 and clipping _ϵ_ = 0 _._ 2. Also, we use an adaptive learning rate and varying KL thresholds per environment. 

- Detailed hyper-parameters for each training task are shown in Table 17. Rewards and observations for each environment we used can be found in Appendix A.2. 

|Environment|Control Type|Simulation_dt_|Control_dt_|Action Dims|
|---|---|---|---|---|
|Ant|Joint Torques|1/120 s|1/60 s|8|
|Humanoid|Joint Torques|1/120 s|1/60 s|21|
|Ingenuity|Rigid BodyForces|1/200 s|1/100 s|6|
|ANYmal|Joint Position Targets|1/200 s|1/50 s|12|
|Franka Cube Stacking|Operation Space Control|1/60 s|1/60 s|7|
|Shadow Hand Standard|Joint Position Targets|1/120 s|1/60 s|20|
|Shadow Hand OpenAI|Joint Position Targets|1/120 s|1/20 s|20|
|Allegro Hand|Joint Position Targets|1/120 s|1/20 s|16|
|TriFinger|Joint Torques|1/200 s|1/50 s|9|



Table 4: Simulation setup for the environments. 

12 

## **5 Characterising Simulation Performance** 

We first characterise the simulation performance as a function of number of environments. As we vary this number, we aim to keep the overall experience an RL agent observes constant by decreasing the horizon length proportionally ( _i.e._ number of steps in PPO) for a fair comparison. While we provide detailed training studies for many environments later, we characterise simulation performance only for **Ant** , **Humanoid** and **Shadow Hand** as they are sufficiently complex to test the limits of the simulation and also represent a gradual increase in the complexity. All three environments use feed forward networks for training. 

### **5.1 Ant** 



<!-- Start of picture text -->
8000 (256, 512)<br>600000 (512, 256)<br>6000 (1024, 128)<br>400000 (2048, 64)<br>4000<br>(4096, 32)<br>(8192, 16)<br>2000 200000<br>(16384, 8)<br>0<br>10 0 10 1 10 2 10 3 0 2 4 6<br>Time (sec) Training Steps × 10 7<br>(a) Rewards (b) Total number of environment steps per second<br>Reward<br>FPS on A100<br><!-- End of picture text -->

Figure 5: Rewards and effective FPS with respect to number of parallel environments for the Ant experiment. Best training time is achieved with 8192 environments and a horizon lengths of 16. 

We first experiment with the standard Ant environment where the agent is trained to run on a flat ground. We find that as the number of agents is increased, the training time, as expected, is reduced _i.e._ changing the number of environments from 256 to 8192 — an increase by 5 orders of magnitude — leads to a reduction in training time to reach 7000 reward by an order of magnitude from 1000 seconds (~16.6 minutes) to 100 seconds (~1.6 minutes). **However, note that Ant reaches performant locomotion at 3000 reward in just 20 seconds on a single GPU.** 

Since Ant is one of the simplest environments to simulate, the number of parallel environment steps per second as depicted in the Figure 5(b) can go as high as 700K. We do not observe gains when increasing the number of environments from 8192 to 16384 due to reduced horizon length. 

### **5.2 Humanoid** 

The Humanoid environment has more degrees of freedom and requires the agent to discover the gait that lets itself balance on two feet and walk on the ground. As observed in Figure 6 and Figure 7, the training times are increased by an order of magnitude compared to the Ant in Figure 5. 

We also note in Figure 6 that as the number of agents is increased, in this case, from 256 to 4096, the training time needed to reach the highest reward of 7000 is reduced by an order of magnitude from 10<sup>4</sup> seconds (~2.7 hours) to 10<sup>3</sup> seconds (~17 minutes). **However, performant locomotion starts happening at around a reward of 5000 at a training time of just 4 minutes.** Going beyond 4096 environments for this set up resulted in no further gains and in fact led to both increase in training time and sub-optimal gaits. We attribute this to the complexity of the environment that makes it challenging to learn walking at such small horizon lengths. 

We verified this by training on another set of environment and horizon length combinations where horizon length was increased by a factor of 2 compared to Figure 6. As shown in the Figure 7, the humanoid is able to walk even with 8192 and 16384 environments which have small horizon lengths of 32 and 16 respectively but sufficiently long to enable learning. 

Also worth noting that due to the increased degrees of freedom the number of parallel environment steps per second is reduced from 700K for Ant to 200K for Humanoid as shown in Figures 6 and 7. 

13 



<!-- Start of picture text -->
300000<br>8000 (256, 512)<br>250000<br>(512, 256)<br>6000<br>200000 (1024, 128)<br>(2048, 64)<br>4000 150000<br>(4096, 32)<br>100000 (8192, 16)<br>2000<br>(16384, 8)<br>50000<br>0<br>10 0 10 1 10 2 10 3 10 4 0 1 2 3<br>Time (sec) Training Steps × 10 8<br>(a) Rewards (b) Total number of environment steps per second<br>Reward<br>FPS on A100<br><!-- End of picture text -->

Figure 6: Rewards and effective FPS with respect to number of parallel environments for the Humanoid experiment. Best training time is achieved with 4096 environments and a horizon lengths of 32. 



<!-- Start of picture text -->
8000 300000 (256, 1024)<br>(512, 512)<br>6000 (1024, 256)<br>200000<br>(2048, 128)<br>4000 (4096, 64)<br>100000 (8192, 32)<br>2000<br>(16384, 16)<br>0<br>10 0 10 1 10 2 10 3 10 4 0 2 4 6<br>Time (sec) Training Steps × 10 8<br>(a) Rewards (b) Total number of environment steps per second<br>Reward<br>FPS on A100<br><!-- End of picture text -->

Figure 7: Rewards and effective FPS with respect to number of parallel environments for the Humanoid experiment. Best training time is achieved with both 4096 and 8192 environments and horizon lengths of 64 and 32 respectively. 

### **5.3 Shadow Hand** 



<!-- Start of picture text -->
(256, 512)<br>6000<br>150000 (512, 256)<br>(1024, 128)<br>4000 100000 (2048, 64)<br>(4096, 32)<br>2000 (8192, 16)<br>50000<br>(16384, 8)<br>0<br>10 0 10 1 10 2 10 3 10 4 10 5 0 2 4 6<br>Time (sec) Training Steps × 10 8<br>(a) Rewards. (b) Total number of environment steps per second<br>Reward<br>FPS on A100<br><!-- End of picture text -->

Figure 8: Rewards and effective FPS with respect to number of parallel environments for the Shadow Hand experiment. Best training time is achieved with both 8192 and 16384 environments and horizon lengths of 16 and 8 respectively. 

Lastly, we experiment with Shadow Hand [5] to learn to rotate a cube resting on the palm to a target orientation using the fingers and the wrist. This task is challenging due to the number of DoFs involved and the contacts that are made and broken during the process of rotation. Our results with Shadow Hand environment follow similar trends. As the number of agents is increased, in this case, from 256 to 16384, the training time is reduced by an order of magnitude from 5 _×_ 10<sup>4</sup> seconds (~14 hours) to 3 _×_ 10<sup>3</sup> seconds (~1 hour). **We find that the environment reaches performant dexterity of 10 consecutive successes at reward of 3000 in just 5 minutes.**<sup>1</sup> Further performance 

> 1The experiments used Shadow Hand Standard variant as explained in Section 6.4.1. 

14 











<!-- Start of picture text -->
0 Steps (millions) 65 0 Steps (millions) 327 0 Steps (millions) 32 0 Steps (millions) 65<br>8000 8000<br>5000<br>15<br>6000 6000 4000<br>4000 4000 3000 10<br>2000<br>2000 2000 5<br>1000<br>0 0 25 50 75 100 125 0 0 500 1000 1500 0 0 20 40 60 0 0 50 100 150 200<br>Time (sec) Time (sec) Time (sec) Time (sec)<br>(a) Ant (b) Humanoid (c) Ingenuity (d) ANYmal<br>Reward Reward Reward Reward<br><!-- End of picture text -->

Figure 9: Locomotion environments and the corresponding reward curves. 

improvements continue to happen as more experience is collected. Additionally, we find that the horizon length of 8 for 16384 agents still allows learning re-posing the cube. The maximum effective frame-rate of 150K number of parallel environment steps per second was achieved with 16384 agents. 

## **6 Characterising Environment Performance** 

We now provide details and performance metrics for individual environments mentioned in Section 4 trained using a PPO implementation that operates on vectorised states and actions. 

### **6.1 Locomotion environments** 

### **6.1.1 Ant** 

The Ant model has four legs with two degrees of freedom per leg. On A100 with 4096 agents simulated in parallel we find that ant can learn to run and achieve a reward above 3000 in just 20 seconds, and fully converge in under 2 minutes. The average simulation performance achieved during training is 540K environment steps per second. The results are shown in Figure 9(a). For details of the reward function used, we refer to Appendix A.2.1 and for the observations used, we refer to Appendix A.2.1. 

### **6.1.2 Humanoid** 

The Humanoid environment has 21 DOFs and on a A100 with 4096 agents simulated in parallel we can train it to run — a reward threshold of 5000 — in less than 4 minutes. This is 4x faster than our previous results in [12] obtained using the same threshold. As shown in Figures 6 and 7, we achieve peak performance for this environment at 4096 agents. Figure 9(b) shows the evolution of reward as a function of time. For details of the reward function used, we refer to Appendix A.2.1 and for the observations used, we refer to Appendix A.2.1. 

### **6.1.3 Ingenuity** 

We train a simplified model of NASA’s Ingenuity helicopter to navigate to a target that periodically teleports to different locations. The environment with trained with 4096 agents and achieves a reward of 5000 in just under 30 seconds. Forces are applied directly to the two rotors on the chassis, rather than simulating aerodynamics. We use a gravity value of -3.721 _m/s_<sup>2</sup> to simulate martian gravity. In Figure 9(c) we show how the reward increases as a function of time. 

### **6.1.4 ANYmal Robot Locomotion** 

ANYmal is a robot developed by ANYbotics for industrial maintenance. It is a four-legged dog-like robot, and has been used for experiments on navigation of rough and variable terrain. We train 

15 

the robot to follow target X, Y, and yaw base velocities while minimizing joint torques. The target velocities are randomized at each reset and are provided as observations alongside the positional and angular velocities of the base, the measured gravity vector, most recent actions, and DOF positions and velocities. With 4096 agents simulating in parallel, we find that the robot is able to follow the targets in under 2 minutes as shown in Figure 9(d). The reward function is defined in A.2.2 

**ANYmal Sim-to-real on Uneven Terrain** In addition to the simple flat terrain environment, we have developed a rough terrain locomotion task for ANYmal and validated the approach by transferring trained policies to the real robot. The robot learns to walk on uneven surfaces, slopes, stairs and obstacles. In addition to the observations of the flat terrain environment it receives terrain height measurements around the robot’s base. For sim-to-real transfer we extend the reward function, add noise to the observations, randomize the friction coefficient of the ground, randomly push the robots during the episode and add an actuator network to the simulation. Following the approach used in [22], the actuator network is trained to model the complex dynamics of the series elastic actuators of the real robot. 





Figure 10: Trained policy for ANYmal on rough terrain tested in simulation and on the real robot. 

We implement an automatic curriculum of increasing terrain difficulties. The robots start to learn on simple versions of the terrains, and when they are able to solve a certain level the difficulty is automatically increased. In order to avoid costly terrain generation during training, we create a single mesh with all terrain types and levels and change the robots’ reset location depending on their progress. With 

4096 environments, we can train the full task on NVIDIA RTX A6000 and transfer to the real robot in under 20 minutes. We refer to [23] for more details. 

### **6.2 Humanoid Character Animation** 

We evaluate the performance of Isaac Gym on adversarial imitation learning tasks using an implementation of adversarial motion priors (AMP) [17]. This technique enables physically simulated humanoid character to imitate complex behaviors from reference motion data. Instead of a manually engineered imitation objective, as is commonly used in prior systems [24], AMP learns an imitation objective using an adversarial discriminator trained to differentiate between motion from the dataset and motions produced by the policy. 



Figure 11: Humanoid character trained using AMP to imitate a spin-kick. 

16 

Our character is modelled as a 34-DOF humanoid [17], and all motion clips are recorded from human actors using motion capture. Table 11 in Appendix A.2.2 details the observation features. The adversarial training process enables the character to closely imitate a diverse corpus of motions, ranging from common locomotion behaviors, such as walking and running, to more athletic behaviors, such as spin-kicks and dancing. Effective policies can be learned with approximately 39 million samples, requiring approximately **6 minutes** with 4096 environments. The implementation provided by Peng _et al._ , 2021 [17] requires about **1 day** (30 hours) on 16 CPU cores to simulate a similar number of samples in PyBullet. Therefore, Isaac Gym provides **300x or 2.48 orders of magnitude improvement** in the training time. 

### **6.3 Franka Cube Stacking** 



<!-- Start of picture text -->
0 Steps (millions) 786<br>3000<br>2000<br>1000<br>0<br>0 1000 2000<br>Time (sec)<br>Reward<br><!-- End of picture text -->

We use 16384 agents to train a Franka robot to stack a cube on top of an other. In this environment, we use a slightly different choice of action space, Operation Space Control (OSC), for learning. OSC [25] is a task-space compliant controller that has been shown to enable faster policy learning compared to joint-space controllers [26]26]] and learn 



Figure 12: The Franka Cube Stacking environment and the corresponding reward curves. ing compared to joint-space controllers [26]26]] and learn contact-rich tasks [27]. Our OSC implementation is fully differentiable in Isaac Gym and we obtain convergence with this controller in under 25 minutes. Figure 12 shows the training results. 

### **6.4 Robotic Hands** 







Figure 13: The three in-hand manipulation environments implemented in Isaac Gym: Shadow Hand, Trifinger, and Allegro. 

Large-scale simulation has the ability to solve not just individual instances but whole classes of problems in robotics, by leveraging the generality of the model-free reinforcement learning framework. Dexterous manipulations is one of the most challenging problems in robotics. 

To show the performance of our simulator and the ability to realistically model contact we implemented 3 different hand training environments as shown in Figure13. Shadow Hand and Allegro Hand are trained to learn cube orientation while TriFinger learns to repose the cube in 6 degrees-offreedom involving rotation and translation. We now focus on the specific training details for these environments. 

Firstly, the Shadow Dexterous Hand. We follow the standard formulation where policy and value function both receive the same input as well as OpenAI observations with asymmetric formulation and domain randomisation from [5]. Secondly, the TriFinger robot [28], which shows the ability to do 6-DoF manipulation by reposing the cube to a desired position and orientation, a task which has previously shown to be challenging for model-free reinforcement learning [29]. We use asymmetric actor-critic and domain randomisation for TriFinger and demonstrate sim-to-real transfer on a real robot. Finally, we reuse system from the Shadow Hand to the Allegro hand with minimal changes to show the generality of our approach. These three environments are depicted in Figure 13 and the corresponding reward curves in Figure 14. 

17 



<!-- Start of picture text -->
0 Steps (millions) 925 0 Steps (millions) 655 0 Steps (millions) 655 0 Steps (millions) 655<br>10000 8000 4000<br>6000<br>8000 6000 3000<br>6000 4000<br>4000 2000<br>4000<br>2000 2000 1000<br>2000<br>0 0 5000 10000 15000 20000 0 0 2500 5000 7500 10000 0 0 1000 2000 3000 4000 0 0 1000 2000 3000<br>Time (sec) Time (sec) Time (sec) Time (sec)<br>(a) SH OpenAI LSTM (b) SH OpenAI FF (c) SH Standard (d) Allegro Hand Standard<br>Reward Reward Reward Reward<br><!-- End of picture text -->

Figure 14: Reward curves for the three in-hand manipulation environments implemented in Isaac Gym. These results are obtained with **(a)** Shadow Hand with OpenAI observation and LSTMs, **(b)** Shadow Hand with OpenAI observation and feed forward networks **(c)** Shadow Hand with Standard observations and **(d)** Allegro Hand with Standard observations. Shadow Hand OpenAI is trained with asymmetric actor-critic and domain radomisation while Shadow Hand Standard and Allegro Hand Standard are trained with standard observations and symmetric actor-critic with no domain randomisation. 

### **6.4.1 Shadow Hand** 

As mentioned, the task with Shadow Hand is to manipulate the cube to achieve a specific target orientation and is inspired by OpenAI _et al._ [5]. We train with multiple variants on the Shadow Hand environment and describe them below: 

**Shadow Hand Standard** In this setting, we use a standard formulation for training where the policy and the value function use feed forward networks and receive the same input observations. The default observations we used for the Shadow Hand Standard include joint position, velocities, forces, force-torque sensors reading from each fingertip, manipulated object position and orientation, linear and angular velocities, goal orientation, relative rotation between the current object and target rotations, actions applied on the previous step. For a detailed overview of observation and reward, see Appendix A.4. Also note that this variant does not use any randomisations. 

**Shadow Hand OpenAI** We also reproduce results with OpenAI Shadow Hand experiments in Isaac Gym with observations used in dexterity work from OpenAI _et al._ [5]. A key difference between this and the Shadow Hand Standard variant is that it uses asymmetric observations. The policy receives only the input observations that are possible to obtain in the real world settings while the value function receives the same observations in addition to the other privileged information available from the simulator. This variant should make it possible to transfer the policy to the real world, mimicking the setup in [5]. The observations for the policy and value function are provided in Table 14. We experiment with both feed forward networks (SH OpenAI FF) and LSTMs (SH OpenAI LSTM). The LSTM networks are trained with a sequence length of 4. 

It is worth noting that only networks trained with OpenAI observations use domain randomisation to closely match the results in OpenAI dexterity work [5]. 



<!-- Start of picture text -->
0 Steps (millions) 925 0 Steps (millions) 655 0 Steps (millions) 655 0 Steps (millions) 655<br>40 30 25 12 . 5<br>30 20 10 . 0<br>20<br>15 7 . 5<br>20<br>10 5 . 0<br>10<br>10 5 2 . 5<br>0 0 5000 10000 15000 20000 0 0 2500 5000 7500 10000 0 0 1000 2000 3000 4000 0 . 0 0 1000 2000 3000<br>Time (sec) Time (sec) Time (sec) Time (sec)<br>(a) SH OpenAI LSTM (b) SH OpenAI FF (c) SH Standard (d) Allegro Hand Standard<br>Consecutive Success Consecutive Success Consecutive Success Consecutive Success<br><!-- End of picture text -->

Figure 15: Consecutive successes per episode for **(a)** Shadow Hand with OpenAI observation and LSTMs, **(b)** Shadow Hand with OpenAI observation and feed forward networks **(c)** Shadow Hand with Standard observations and **(d)** Allegro Hand with Standard observations. Shadow Hand Standard and Allegro Hand Standard both use feed forward networks for policy and value functions. 

**Randomizations** For domain randomization we closely followed the approach proposed in [5] and applied correlated and uncorrelated noise to observations, actions, as well as randomized cube size 

18 

and all the key physics properties – masses, inertia tensors, friction, restitution, joint limits, stiffness and damping. Full details of these are available in Appendix A.4.1. 

We outline a few important differences between our setup and the one used in the OpenAI work below: 

- While OpenAI used a success tolerance of 0.4 rad<sup>2</sup> [5], we use both 0.4 rad and a tighter tolerance of 0.1 rad. We focus on results with 0.4 rad in this section and provide results with 0.1 tolerance in Appendix A.4.2 

- We use a continuous as opposed to a discrete control space used in [5]. 

- Our results are averaged with 5 seeds while OpenAI show results with only 1 seed<sup>3</sup> . 

- The randomizations used in our work do not include action delay and motor backlash. 

- We use an LSTM layer of 1024 hidden units after the input followed by an MLP layer of 512 hidden units. On the other hand OpenAI _et al._ [5] used an MLP layer of size 1024 after the input followed by an LSTM layer of size 512 hidden units. We found our setting performs better with Isaac Gym. 

- We use a somewhat different reward function to OpenAI as shown in Appendix A.2.3. 

- Our experiments are only in simulation and unlike [5] we do not attempt any sim-to-real transfer for the Shadow Hand experiment. 

Figure 14(a), (b) and (c) show the reward curves for various settings we used for Shadow Hand. Shadow Hand Standard — trained with no randomization and uses symmetric actor critic setting with a feed forward network — is the fastest to reach a reward of 6000. This setting achieves 20 consecutive successes in under 35 minutes. Important to remember that this setting is not suitable for sim-to-real transfer as it includes some observations that may not be directly available in the real world. 

We now focus on experiments with OpenAI observations and asymmetric feed-forward actor-critic. This setting is suited for sim-to-real transfer and the policy uses only the observations that are possible to obtain in the real world. As shown in Figure 15(b), we achieved more than 20 consecutive successes in less than 1 hour. In contrast, for the same performance it takes 30 hours on the OpenAI setup consisting of CPU based simulation and training setup running MuJoCo [6] simulator on a cluster of 384 16-core CPUs with 6144 CPU cores in total and using 8 NVIDIA V100 GPUs for training. In Figure 15(a) we show that using LSTM networks, the performance increases and we can reach 37 consecutive successes in just under than 6 hours while OpenAI _et al._ [5] achieve same performance in ~17 hours. Since OpenAI _et al._ [5] show results only with 1 seed, comparing their result with our best seed we note that 37 consecutive successes with LSTM experiments can be achieved in just 2.5 hours. We provide the results for Shadow Hand OpenAI experiment with success tolerance of 0.1 in the Appendix A.4. 

### **6.4.2 TriFinger** 



<!-- Start of picture text -->
0 Steps (millions) 4194 0 Steps (millions) 4194<br>15000<br>12500 60<br>10000<br>40<br>7500<br>5000 20<br>2500 0 25000 50000 75000 0 0 20000 40000 60000 80000<br>Time (sec) Time (sec)<br>(a) Reward (b) Success Rate<br>Reward<br>Success Rate (%)<br><!-- End of picture text -->

Figure 16: TriFinger reward and the corresponding success rate. 

The TriFinger manipulation task, originating in [28], involves picking a cube lying on a flat surface and repositioning it to a desired 6-degreesof-freedom pose. The manipulator has 3 fingers each with three degrees of freedom. In [29], it was shown that Isaac Gym training combined with Domain Randomization allows sim-to-real transfer. The environment is shown in Figure 13. 

We use an asymmetric actor-critic formulation for this system as that allows to design a policy that uses input observations that are possible to 

obtain in the real world and therefore enable sim-to-real transfer. We show the reward and success 

> 2page 22, section C.1, paragraph **Goals** in [5] 

> 3page 11, section 6.3, **Ablation of Randomizations** , Figure 8 in [5] 

19 



<!-- Start of picture text -->
Time<br><!-- End of picture text -->



<!-- Start of picture text -->
(a)<br>Initial Grasp Initial Lifting Reorientation Drop & Regrasp Lift Fine correction<br>(b)<br>Initial Grasp Flick to reorient 2 nd reorientation Drop & Regrasp Lift + in-hand Fine correction<br>reorientation<br>(c)<br>Bad grasp Cube Falls Re-grasp Lift Lift + in-hand  Fine correction<br>reorientation<br><!-- End of picture text -->

Figure 17: Trifinger learns a variety of dexterous manipulation behaviours in order to move the cube to the correct position and orientation. These results are obtained on the real TriFinger robot hosted by [28, 30]. 

rate in simulation in Figure 16. We also transfer results from simulation to the real world and note that our mean success rate in the real world is 55%. We refer to [29] for more detailed analysis. 

In particular, this example shows the ability of policies learned using Isaac Gym’s physics to generalize to the real world. Some of the behaviours leaned by the policy are shown in the Figure 17. It is worth noting that the robot is situated in a different location and therefore the sim-to-real transfer was done remotely. 

### **6.4.3 Allegro Hand** 

We learn cube orientation with Allegro Hand and use the same reward as for the Shadow Hand as well similar observation scheme, with the only difference — smaller number of observations because of the different number of fingers in Allegro Hand — that it has 4 fingers instead of 5 and fewer degrees of freedom as a result, shown in Appendix A.2.3. 

Figure 14(d) shows the reward curves for Allegro Hand and Figure 15(d) shows consecutive successes achieved. Interestingly, despite having fewer degrees of freedom this hand does not achieve as high consecutive successes as Shadow hand. This is because the wrist is fixed and fingers are slightly longer. We observed in Shadow hand experiment that having a movable wrist allows for better manipulation when reorienting the cube. 

## **7 Summary** 

We show that Isaac Gym is a high performance and high-fidelity framework that allows blistering fast training on many challenging simulated robotic environments on a single NVIDIA A100 GPU that previously would have required large heterogeneous clusters of CPUs and GPUs using a conventional RL setup with CPU-only simulators. Moreover, the simulation backend [13] is also suited for learning contact-rich manipulations as confirmed by our sim-to-real transfer demonstrations with ANYmal locomotion and TriFinger cube reposing. 

20 

## **8 Acknowledgements** 

We would like to thank the following for additional hard work helping us with this work. 

Jonah Alben, Rika Antonova, Ayon Bakshi, Dennis Da, Shoubhik Debnath, Clemens Eppner, Dieter Fox, Animesh Garg, Renato Gasoto, Isabella Huang, Andrew Kondrich, Rev Lebaredian, Qiyang Li, Jacky Liang, Denys Makoviichuk, Brendon Matusch, Hammad Mazhar, Mayank Mittal, Adam Moravansky, Yashraj Narang, Oyindamola Omotuyi, Fabio Ramos, Andrew Reidmeyer, Philipp Reist, Tony Scudiero, Mike Skolones, Balakumar Sundaralingam, Liila Torabi, Cameron Upright, Zhaoming Xie, Winnie Xu, Yuke Zhu, and the rest of the NVIDIA PhysX, Omniverse, and robotics research teams. We also thank Jason Peng and Josiah Wong for the help in AMP and Franka Cube Stacking experiments. 

Thanks are also due to open-source community projects like Matplotib[31], Python[32], NumPy[33], PyTorch[34], Tensorboard[35], Tensorboard Aggregator[36] and SciencePlots[37] which we used heavily in this work. We are thankful to Overleaf [38] for hosting our latex project. 

21 

## **References** 

- [1] David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, et al. A general reinforcement learning algorithm that masters chess, shogi, and go through self-play. _Science_ , 2018. 

- [2] Santiago Ontanón, Gabriel Synnaeve, Alberto Uriarte, Florian Richoux, David Churchill, and Mike Preuss. A survey of real-time strategy game ai research and competition in starcraft. _IEEE Transactions on Computational Intelligence and AI in games_ , 5(4):293–311, 2013. 

- [3] Christopher Berner, Greg Brockman, Brooke Chan, Vicki Cheung, Przemysław D˛ebiak, Christy Dennison, David Farhi, Quirin Fischer, Shariq Hashme, Chris Hesse, et al. Dota 2 with large scale deep reinforcement learning. _arXiv preprint arXiv:1912.06680_ , 2019. 

- [4] Xue Bin Peng, Erwin Coumans, Tingnan Zhang, Tsang-Wei Edward Lee, Jie Tan, and Sergey Levine. Learning Agile Robotic Locomotion Skills by Imitating Animals. In _Robotics: Science and Systems_ , 07 2020. doi: 10.15607/RSS.2020.XVI.064. 

- [5] OpenAI, Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Józefowicz, Bob McGrew, Jakub W. Pachocki, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, Jonas Schneider, Szymon Sidor, Josh Tobin, Peter Welinder, Lilian Weng, and Wojciech Zaremba. Learning dexterous in-hand manipulation. _CoRR_ , abs/1808.00177, 2018. URL `http://arxiv.org/abs/1808.00177` . 

- [6] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 5026–5033. IEEE, 2012. 

- [7] Erwin Coumans and Yunfei Bai. Pybullet, a python module for physics simulation for games, robotics and machine learning, 2016. _URL http://pybullet. org_ , 2016. 

- [8] Jeongseok Lee, Michael X Grey, Sehoon Ha, Tobias Kunz, Sumit Jain, Yuting Ye, Siddhartha S Srinivasa, Mike Stilman, and C Karen Liu. Dart: Dynamic animation and robotics toolkit. _Journal of Open Source Software_ , 2018. 

- [9] Russ Tedrake and the Drake Development Team. Drake: Model-based design and verification for robotics, 2019. URL `https://drake.mit.edu` . 

- [10] Eric Rohmer, Surya PN Singh, and Marc Freese. V-rep: A versatile and scalable robot simulation framework. In _2013 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 1321–1326. IEEE, 2013. 

- [11] Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias Plappert, Glenn Powell, Raphael Ribas, et al. Solving Rubik’s Cube with a Robot Hand. _arXiv preprint arXiv:1910.07113_ , 2019. 

- [12] Jacky Liang, Viktor Makoviychuk, Ankur Handa, Nuttapong Chentanez, Miles Macklin, and Dieter Fox. Gpu-accelerated robotic simulation for distributed reinforcement learning. In _Conference on Robot Learning_ . PMLR, 2018. 

- [13] NVIDIA. Nvidia PhysX, 2020. URL `https://developer.nvidia.com/physx-sdk` . 

- [14] C. Daniel Freeman, Erik Frey, Anton Raichuk, Sertan Girgin, Igor Mordatch, and Olivier Bachem. Brax - A Differentiable Physics Engine for Large Scale Rigid Body Simulation, 2021. URL `http://github.com/google/brax` . 

- [15] Joshua Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. _CoRR_ , abs/1703.06907, 2017. URL `http://arxiv.org/abs/1703.06907` . 

- [16] M. Hutter, Christian Gehring, Dominic Jud, Andreas Lauber, Dario Bellicoso, Vassilios Tsounis, Jemin Hwangbo, K. Bodie, P. Fankhauser, Michael Bloesch, Remo Diethelm, Samuel Bachmann, A. Melzer, and M. Höpflinger. Anymal - a highly mobile and dynamic quadrupedal robot. _(IROS)_ , 2016. 

22 

- [17] Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, and Angjoo Kanazawa. AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control. _ACM Trans. Graph._ , 2021. 

- [18] Miles Macklin, Kier Storey, Michelle Lu, Pierre Terdiman, Nuttapong Chentanez, Stefan Jeschke, and Matthias Müller. Small steps in physics simulation. In _Proceedings of the 18th Annual ACM SIGGRAPH/Eurographics Symposium on Computer Animation_ , SCA ’19, New York, NY, USA, 2019. Association for Computing Machinery. doi: 10.1145/3309486.3340247. URL `https://doi.org/10.1145/3309486.3340247` . 

- [19] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal Policy Optimization Algorithms, 2017. 

- [20] Denys Makoviichuk and Viktor Makoviychuk. RL Games, 2021. URL `https://github. com/Denys88/rl_games/` . 

- [21] Lerrel Pinto, Marcin Andrychowicz, Peter Welinder, Wojciech Zaremba, and Pieter Abbeel. Asymmetric actor critic for image-based robot learning. _CoRR_ , 2017. URL `http://arxiv. org/abs/1710.06542` . 

- [22] Jemin Hwangbo, Joonho Lee, Alexey Dosovitskiy, Dario Bellicoso, Vassilios Tsounis, Vladlen Koltun, and Marco Hutter. Learning Agile and Dynamic Motor Skills for Legged Robots. _Science Robotics_ , Jan 2019. 

- [23] Anonymous. Learning to walk in minutes using massively parallel deep reinforcement learning. In _Submitted to 5th Annual Conference on Robot Learning_ , 2021. URL `https://openreview. net/forum?id=wK2fDDJ5VcF` . under review. 

- [24] Xue Bin Peng, Pieter Abbeel, Sergey Levine, and Michiel van de Panne. Deepmimic: Exampleguided deep reinforcement learning of physics-based character skills. _ACM Trans. Graph._ , 37 (4), July 2018. doi: 10.1145/3197517.3201311. 

- [25] O. Khatib. A unified approach for motion and force control of robot manipulators: The operational space formulation. _IEEE Journal on Robotics and Automation_ , 3(1):43–53, 1987. doi: 10.1109/JRA.1987.1087068. 

- [26] Yuke Zhu, Josiah Wong, Ajay Mandlekar, and Roberto Martín-Martín. robosuite: A modular simulation framework and benchmark for robot learning, 2020. 

- [27] Roberto Martín-Martín, Michelle A. Lee, Rachel Gardner, Silvio Savarese, Jeannette Bohg, and Animesh Garg. Variable impedance control in end-effector space: An action space for reinforcement learning in contact-rich tasks, 2019. 

- [28] Manuel Wüthrich, Felix Widmaier, Felix Grimminger, Joel Akpo, Shruti Joshi, Vaibhav Agrawal, Bilal Hammoud, Majid Khadiv, Miroslav Bogdanovic, Vincent Berenz, Julian Viereck, Maximilien Naveau, Ludovic Righetti, Bernhard Schölkopf, and Stefan Bauer. TriFinger: An Open-Source Robot for Learning Dexterity. _CoRR_ , abs/2008.03596, 2020. URL `https://arxiv.org/abs/2008.03596` . 

- [29] Arthur Allshire, Mayank Mittal, Varun Lodaya, Viktor Makoviychuk, Denys Makoviichuk, Felix Widmaier, Manuel Wuthrich, Stefan Bauer, Ankur Handa, and Animesh Garg. Transferring Dexterous Manipulation from GPU Simulation to a Remote Real-World TriFinger. _CoRR_ , 2021. 

- [30] Niklas Funk, Charles B. Schaff, Rishabh Madan, Takuma Yoneda, Julen Urain De Jesus, Joe Watson, Ethan K. Gordon, Felix Widmaier, Stefan Bauer, Siddhartha S. Srinivasa, Tapomayukh Bhattacharjee, Matthew R. Walter, and Jan Peters. Benchmarking structured policies and policy optimization for real-world dexterous object manipulation. _CoRR_ , abs/2105.02087, 2021. URL `https://arxiv.org/abs/2105.02087` . 

- [31] J. D. Hunter. Matplotlib: A 2d graphics environment. _Computing in Science & Engineering_ , pages 90–95, 2007. 

- [32] Guido Van Rossum and Fred L. Drake. _Python 3 Reference Manual_ . CreateSpace, Scotts Valley, CA, 2009. 

23 

- [33] Charles R. Harris, K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett, Allan Haldane, Jaime Fernández del Río, Mark Wiebe, Pearu Peterson, Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer Abbasi, Christoph Gohlke, and Travis E. Oliphant. Array programming with NumPy. _Nature_ , 2020. doi: 10.1038/s41586-020-2649-2. URL `https://doi.org/10.1038/s41586-020-2649-2` . 

- [34] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala. Pytorch: An imperative style, highperformance deep learning library. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'AlchéBuc, E. Fox, and R. Garnett, editors, _Advances in Neural Information Processing Systems 32_ , pages 8024–8035. Curran Associates, Inc., 2019. URL `http://papers.neurips.cc/paper/ 9015-pytorch-an-imperative-style-high-performance-deep-learning-library. pdf` . 

- [35] Martín Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo, Zhifeng Chen, Craig Citro, Greg S. Corrado, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Ian Goodfellow, Andrew Harp, Geoffrey Irving, Michael Isard, Yangqing Jia, Rafal Jozefowicz, Lukasz Kaiser, Manjunath Kudlur, Josh Levenberg, Dandelion Mané, Rajat Monga, Sherry Moore, Derek Murray, Chris Olah, Mike Schuster, Jonathon Shlens, Benoit Steiner, Ilya Sutskever, Kunal Talwar, Paul Tucker, Vincent Vanhoucke, Vijay Vasudevan, Fernanda Viégas, Oriol Vinyals, Pete Warden, Martin Wattenberg, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng. TensorFlow: Largescale machine learning on heterogeneous systems, 2015. URL `https://www.tensorflow. org/` . Software available from tensorflow.org. 

- [36] Sebastian Penhouet. TensorBoard Aggregator, February 2021. URL `https://github.com/ Spenhouet/tensorboard-aggregator` . 

- [37] John D. Garrett and Hsin-Hsiang Peng. garrettj403/SciencePlots, February 2021. URL `http: //doi.org/10.5281/zenodo.4106649` . 

- [38] Overleaf, 2012. URL `https://www.overleaf.com/` . 

- [39] Ossama Ahmed, Frederik Träuble, Anirudh Goyal, Alexander Neitz, Manuel Wüthrich, Yoshua Bengio, Bernhard Schölkopf, and Stefan Bauer. CausalWorld: A Robotic Manipulation Benchmark for Causal Structure and Transfer Learning. _CoRR_ , abs/2010.04296, 2020. URL `https://arxiv.org/abs/2010.04296` . 

24 

## **A Appendix** 

### **A.1 Tendons** 

We simulate tendons as part of the Shadow Hand environment and describe the details of this simulation here. 

### **A.1.1 Fixed Tendons** 

Fixed tendons are an abstract mechanism that couple degrees of freedom (DOF) of an articulation. A fixed tendon is composed of a tree of tendon joints, where each joint is associated with exactly one axis of a link’s incoming articulation joint. In the following, when we refer to a tendon joint’s position, we mean the position of the axis of this associated articulation joint. 

In addition, each tendon joint has a coefficient that determines the contribution of the (rotational or translational) joint position to the length of the tendon, which is evaluated recursively by traversing the tree: The length at a given tendon joint is the length at its parent tendon joint plus its joint position scaled by the coefficient. 

Given the tendon length at each joint, the tendon applies a spring force (or torque) to the joint’s child link that is proportional to the deviation of the tendon length from a desired (tendon-wide) rest length. An equal and opposing force is applied to the parent link of the root tendon joint; conceptually, each tendon joint is a virtual joint drive between the root parent link and the tendon joint’s child link. In addition to the spring force, the tendon-joint applies a damping force that is proportional to and acting against the velocity of the virtual root-to-child link joint. 

Analogous to the length dynamics, the tendon supports length limits that apply an additional force or torque that is proportional to the deviation from set limits. 

### **A.1.2 Spatial Tendons** 

Spatial tendons create line-of-sight distance constraints between links of a single articulation. In particular, spatial tendons run through attachments that are positioned relative to an articulation link, and their length is defined as a weighted sum of the distance between the attachments in the tendon. It is possible to create multiple attachments per link, for example for tendon-routing purposes. In contrast to fixed tendons, spatial tendons are not constrained to follow the articulation topology. 

Same as fixed tendons, spatial tendons may branch, in which case the tendon splits up into multiple conceptual sub-tendons, one for each root-to-leaf path in the tendon tree. Length and limit constraints are evaluated per sub-tendon, and have spring-damper dynamics that may both contract and extend the tendon (one may use appropriately set limits to achieve a one-sided, string-like constraint). 

The sub-tendon constraint force acts on the leaf and root attachments, in the direction of its parent for the leaf, and in the direction of the child on the path to the sub-tendon leaf for the root. However, the force does not propagate further and act on any intermediate attachments between root and leaf. 

### **A.2 Observations & Rewards** 

In this section we describe the reward and observations for each environment in detail. 

### **A.2.1 Ant and Humanoid environments** 

Both the Ant and Humanoid environments use the same reward formulation, namely: 

- R = Rprogress + Ralive _×_ 1 (torso_height _≥_ termination_height) + Rupright + Rheading + Reffort + Ract + Rdof + Rdeath _×_ 1 (torso_height _≤_ termination_height) 

where 

25 



**Ant** Reward described in Section A.2.1. Observations detailed in Table 5. 

|Observation s|pace|Degrees of freedom|
|---|---|---|
|Torso verticalpositio|n|1|
|Velocity|positional<br>angular|3<br>3|
|Yaw,roll,angle to tar|get|3|
|Upand headingvecto|rproj.|2|
|DOF measurements|position<br>velocity|8<br>8|
|Sensor forces,torque|s|24|
|Actions||8|
|Total number of ob|servations|60|



Table 5: Observations used for Ant training. 

|Observation s|pace|Degrees of freedom|
|---|---|---|
|Torso verticalpositio|n|1|
|Velocity|positional<br>angular|3<br>3|
|Yaw,roll,angle to tar|get|3|
|Upand headingvecto|rproj.|2|
|DOF measurements|position<br>velocity<br>force|21<br>21<br>21|
|Sensor forces/torques||12|
|Actions||21|
|Total number of ob|servations|108|



Table 6: Observations used for Humanoid training. 

**Humanoid** Reward described in Section A.2.1. Observations detailed in Table 6. 

### **A.2.2 Locomotion environments** 

**Ingenuity** Observations detailed in Table 7. The reward function is as follows: 



### **reaching cost** 

### **spinning cost** 

### **upright cost** 



**ANYmal Locomotion** For the included flat-terrain environment, observations are detailed in Table 8 and the reward function is as follows: 



Reward terms are defined in Table 10 and symbols in Table 9. 

26 

|Observation space<br>Degrees of freedom<br>Offset from target<br>3<br>Rotation<br>4<br>Velocity<br>positional<br>3<br>angular<br>3<br>Total number of observations<br>13<br>Table 7: Observations used for ingenuity training.|Observati<br>Base velocity<br>Body-relativeg<br>Target X,Y, ya<br>DOF states<br>Actions<br>Total number o|on space<br>positional<br>angular<br>ravity<br>w velocities<br>position<br>velocity<br>f observations|Degrees of freedom<br>3<br>3<br>3<br>3<br>12<br>12<br>12<br>48|
|---|---|---|---|



Table 8: Observations used for ANYmal training. 

For rough terrain locomotion with sim-to-real, we extend the observations with 140 terrain heights around the robot’s base and use the more complex reward function: 



|Quantity<br>|Symbol|Reward|Symbol|Definition<br><br>|Weight|
|---|---|---|---|---|---|
|Jointpositions<br>|**q**_j_<br>˙|Linear velocitytracking|Rvel_,_xy|_φ_(**v**<sup>_∗_</sup><br>_b,xy _<sup>_−_</sup><sup>**v**</sup><sup>_b,xy_)</sup>|1_dt_|
|Joint velocities<br>i li|**q**_j_<br>¨|Angular velocitytracking|Rvel_,_yaw|_φ_(**_ω_**<sup>_∗_</sup><br>_b,z _<sup>_−_</sup><sup>**_ω_**</sup><sup>_b,z_)</sup><br>|0_._5_dt_|
|Jont acceeratons<br>Taretjointositions|**q**_j_<br>¨<sup>_∗_</sup><br>|Linear velocity penalty|Rvel_,_z|_−_**v**<sup>2</sup><br>_b,z_<br>|4_dt_|
|g  p<br>Joint torques|**q**<br>_j_<br>**_τ_**|Angular velocity penalty<br>|Rvel_,_pitch_/_roll<br>|_−||_**_ω_**_b,xy||_<sup>2</sup><br>|0_._05_dt_<br>|
|<br>Base linear velocity|_j_<br>**v**_b_|Joint motion<br>|Rjoint vel_/_acc<br>|_−||_¨**q**_j||_<sup>2</sup> _−||_ ˙**q**_j||_<sup>2</sup><br>|0_._001_dt_<br>|
|Base angular velocity|**_ω_**_b_|Joint torques|Rtorque|_−||_**_τ_** _j||_<sup>2</sup><br><sup>˙</sup><br>|0_._00002_dt_|
|Commanded base linear velocity|**v**<sup>_∗_</sup><br>_b_|Action rate<br>|Rrate<br>|_−||_ **q**<sup>_∗_</sup><br>_j_<sup>_||_2</sup>|0_._25_dt_<br>|
|Commanded base angular velocity|**_ω_**<sup>_∗_</sup><br>_b_|Collisions|Rcoll_._|_−ncollision_<br>|0_._001_dt_|
|Number of collisions<br>|_nc_<br>|Feet air time<br>|Rairtime<br>|�4<br>_f_=0<sup>(</sup><sup>**t**</sup><sup>_air,f −_0</sup><sup>_._5)</sup><br>|2_dt_<br>|
|Feet air time<br>Environment time step<br>i|**t**_air_<br>_dt_<br>i|Table 10: Definition of|i  reward term|i   s, with_φ_(_x_) := e|xp(_−_<sup>_||x||_2</sup><br>0_._25 <sup>).</sup>|
|Table 9: Definition of sym|i  bols.|The z axis is aligned wi|th gravity.|||



Table 9: Definition of symbols. 

**Adversarial Imitation Learning** AMP learns an imitation objective using an adversarial discriminator _D_ , trained to differentiate between motion from the dataset _M_ and motions produced by the policy _π_ , 



where _pM_ ( _s, s_<sup>_′_</sup> ) denotes the likelihood of observing a state transition from _s_ to _s_<sup>_′_</sup> in the motion data, and _pπ_ ( _s, s_<sup>_′_</sup> ) is likelihood of a state transition under the policy. The discriminator can then be used to specify rewards _rt_ for training a policy to imitate behaviors shown in the motion data 



This objective, in effect encourages the policy to produce behaviors that fool the discriminator into classifying them as behaviors from the reference motion data. 

|Observation sp<br>Pelvis vertical height<br>Pelvis rotation|ace|Degrees of freedom<br>1<br>6|Observation space<br>Joint DOFs<br>arm position<br>eefposition<br>|Degrees of freedom<br>7 (Joint Torque only)<br>2<br>|
|---|---|---|---|---|
||positional|3|EEFpose|7|
|Pelvis Velocity|angular|3|Cube Apose<br>|7|
|DOF|position|52|Cube A to Cube Bposition|3|
|measurements|velocity|28|Total number of observations|19 / 26|
|Key pointposition||15|Table 12: Franka Cube Stac|k observations. No|
|Total number of obs|ervations|108|thtbtiil|dthlbl3di|



Table 12: Franka Cube Stack observations. Note that pose observations include the global 3-dim cartesian position and 4-dim quaternion orientation, and the arm joint position observations are only provided if using joint torque control. 

Table 11: Observations used for AMP training with a humanoid character. 3D rotations are represented using a 6D tangent-normal encoding. 

**Franka Cube Stack** Observations are detailed in Table 12. The reward function used is as follows: 

27 

R = max (Rstack _,_ Ralign + Rlift + Rreach) 

where: 

Rstack = wstack _×_ 1 ((heightcubeA _>_ heightcubeB)&(cubeA_aligned_cubeB)&(gripper_away_from_cubeA)) _,_ Ralign = walign _×_ (1 _−_ tanh(10 _×_ cubeA_to_B_xy_dist)) _×_ 1 (cubeA_is_lifted) _,_ Rlift = wlift _×_ 1 (cubeA_is_lifted) _,_ Rreach = wreach _×_ 1 _−_ tanh � 10 � 3<sup>_×_(dist(cubeA</sup><sup>_,_gripper) + dist(cubeA</sup><sup>_,_lfinger) + dist(cubeA</sup><sup>_,_rfinger))</sup> �<sup>�</sup> 

We set wstack = 16 _._ 0, walign = 2 _._ 0, wlift = 1 _._ 5, and wreach = 0 _._ 1 

### **A.2.3 Robotic Hands** 

**Shadow Hand** The reward function for Shadow Hand is as follows: 



### **distance cost** 



### **orientation cost** 





### **action smoothness cost** 



where wdist = _−_ 10 and wact = _−_ 2 _e −_ 4. 

|Observation spa|ce|Degrees of freedom|
|---|---|---|
|Finger joints|position<br>velocity<br>force|24<br>24<br>24|
|Cube pose|translation<br>quaternion<br>linear velocity<br>angular velocity|3<br>4<br>3<br>3|
|Cube rotation relative togoal|quaternion|4|
|Goal pose|translation<br>quaternion|3<br>4|
||position|3|
||quaternion|4|
|5_×_Finger tips|linear velocity<br>angular velocity<br>force<br>torque|3<br>3<br>3<br>3|
|Previous action output f|rompolicy|20|
|Total number of obse|rvations|211|



|Observation space|Degrees of freedom|
|---|---|
|5_×_Fingerjoints<br>position|3|
|Cubepose<br>translation|3|
|Cube rotation relative togoal<br>quaternion|4|
|Previous action output frompolicy|20|
|Total number of observations|42|
|Table 14: Observations for the Sh|adow Hand**Ope-**|
|**nAI**environment. The observat<br>are the same as for Shadow Ha|ions of the critic<br>nd Standard (see|
|Table13).||



Table 13: Observations for the Shadow Hand **Standard** environment. 

There are two different variants of observations used. In the Shadow Hand **Standard** environment, the observations are as shown in Table 13. In The ShadowHand **OpenAI** environment, in order to compare to compare to [5], we use observations as shown in Table 14. Further details of the Shadow Hand environments are available in Appendix A.4. Below we provide the code snippet to compute the reward as used in our implementation. 

28 

```
@torch.jit.script
defcompute_hand_reward (
object_pos ,object_rot ,target_pos ,target_rot ,actions ,
dist_reward_scale :float ,rot_reward_scale :float ,rot_eps:float ,
action_penalty_scale :float ,success_tolerance :float ,reach_goal_bonus :float ,
fall_dist:float , fall_penalty :float):
# dist_reward_scale :-10.0
# rot_reward_scale :1.0
#rot_eps:0.1
# action_penalty_scale :-0.0002
# reach_goal_bonus :250
# fall_distance :0.24
# fall_penalty :0.0
#Distancefromthehandtotheobject
goal_dist=torch.norm(object_pos-target_pos ,p=2,dim =-1)
#Orientationalignmentforthecubeinhandandgoalcube
quat_diff=quat_mul(object_rot ,quat_conjugate (target_rot))
rot_dist=2.0*torch.asin(torch.clamp(torch.norm(quat_diff [:,0:3] ,p=2,dim =-1),
max =1.0))
#Orientationreward
rot_rew=1.0/( torch.abs(rot_dist)+rot_eps)
#actionsmoothnessreward
action_penalty=torch.sum(actions**2,dim =-1)
#Totalrewardis:positiondistance+orientationalignment+actionregularization
+successbonus+fallpenalty
reward=goal_dist*dist_reward_scale+rot_rew*rot_reward_scale
+action_penalty*action_penalty_scale
#Findoutwhichenvshitthegoalandupdatesuccessescount
goal_resets=torch.where(torch.abs(rot_dist)<=success_tolerance ,
torch.ones_like( reset_goal_buf ),reset_goal_buf )
#Successbonus:orientationisinsidethe‘success_tolerance ‘ofgoalorientation
reward=torch.where( goal_resets==1,reward+reach_goal_bonus ,reward)
#Fallpenalty:distancetothegoalislargerthanathreashold
reward=torch.where(goal_dist>=fall_dist ,reward+fall_penalty ,reward)
```

```
returnreward
```

Reward function for cube orientation for Shadow Hand experiments. 

|Obse<br>Finger joints|rvation space<br>position<br>velocity|Degrees of freedom<br>9<br>9|Observat<br>Actor Observatio<br>Cube pose|ion space<br>De<br>ns(see Table15)<br>linear velocity<br>angular velocity<br>|grees of freedom<br>41<br>3<br>3<br>|
|---|---|---|---|---|---|
|||||osition|3|
|Cube pose|translation<br>quaternion|3<br>4||p<br>quaternion<br>linear velocit|4<br>3|
|Goal pose|translation<br>quaternion|3<br>4|3_×_Finger tips|y<br>angular velocity<br>force|3<br>3|
|Previous actio|n output frompolicy|9||torue|3|
|Total numb<br>|er of observations<br>i|41<br>i|Finerjoints|q<br>terue|9|
|Table 1|5: Trifinger Actor|i  Observations.|g <br>Total number|q<br>of observations|113|



Table 16: Trifinger Critic Observations 

**Trifinger** Our total reward is defined as: 



### **reposing cost** 



### **fingertips interaction cost** 



29 

### **fingertips smoothness cost** 



∆<sup>_t_</sup> _i_<sup>denotes the change across the timestep of the fingertip distance to the centroid of the object and</sup> was found to be helpful in [39]. Formally, ∆<sup>_t_</sup> _i_<sup>=</sup><sup>_||_fti</sup><sup>_,_t</sup><sup>_−_tcurr</sup><sup>_,_t</sup><sup>_||_2</sup><sup>_−||_fti</sup><sup>_,_t</sup><sup>_−_1</sup><sup>_−_tcurr</sup><sup>_,_t</sup><sup>_−_1</sup><sup>_||_2, where tcurr</sup><sup>_,_t</sup> is position of the cube centroid and fti denotes the position of the _i_ -th fingertip at time _t_ . 

rot_dist is the angluar difference between the current and target cube pose, rot_dist = 2 _×_ arcsin(min(1 _._ 0 _, ||_ qdiff _||_ 2)) _,_ qdiff = qcurrq<sup>_∗_</sup> target<sup>.Following [22], a logistic kernel is used to convert</sup> tracking error in euclidean space into a bounded reward function, with _K_ ( _x_ ) = ( _e_<sup>_ax_</sup> + _b_ + _e_<sup>_−ax_</sup> )<sup>_−_1</sup> , where _a_ is a scaling factor; we use _a_ = 50. See [29] for a more thorough motivation and description of these reward terms. 

**Allegro** The reward formulation is identical to that used in Shadow Hand - see Appendix A.2.3. The observations are also identical, save for the change in number of fingers. 

### **A.3 Hyperparameters for Training PPO** 

|Environment|# Environments|KL Threshold|Mini-batch Size|Horizon Length|# PPO Epochs|Hidden Units|TrainingSteps|
|---|---|---|---|---|---|---|---|
|Ant|4096|8e-3|32768|16|4|256,128,64|32M|
|Humanoid|4096|8e-3|32768|32|5|400,200,100|327M|
|Ingenuity|4096|1.6 e-2|32768|16|8|256,256,128|32M|
|ANYmal|8192|1e-2|32768|16|5|256,128,64|65M|
|ANYmal Terrain|4096|1e-2|24576|24|10|512,256,128|150M|
|AMP|4096|2e-1|16384|32|8|1024,512|39M|
|Franka|16384|1.6 e-2|131072|32|4|256,128,64|786M|
|SH Standard|16384|1.6 e-2|32768|8|5|512,512,256,128|655M|
|SH OpenAI FF|16384|1.6 e-2|32768|8|5|400,400,200,100|655M|
|SH OpenAI LSTM|8192|1.6 e-2|32768|16|4|lstm: 1024,mlp: 512|925M|



Table 17: Hyperparameters used for training in each environment. Allegro shares the parameters for Shadow Hand. The hidden units are ELU for every environment except AMP, where ReLU units are used. Additionally, every environment uses an adaptive learning rate with a KL divergence target specified in the _KL Threshold_ column, except for AMP which uses a fixed learning rate of 2e-5 and fixed KL theshold of 2e-1. The SH OpenAI LSTM experiment uses an LSTM layer of 1024 hidden dims followed by MLP of 512 dims, and a fixed learning rate of 1e-4 for the value function. 

### **A.4 Shadow Hand Details** 

As mentioned previously, we implemented two variants of the Shadow Hand environment. The **Standard** variant uses privileged policy observations and no Domain Randomization, in order to provide a quick training example to test Reinforcement Learning algorithms on. The **OpenAI** variant uses asymmetric observations, such that it would be possible to transfer the policy to the real world, mimicing the setup in [5]. 

### **A.4.1 Randomizations** 

Isaac Gym implements a high-level API that simplifies setting up physics domain randomization parameters and schedule in yaml configuration files and is very extensible. Here we detail the randomization parameters that we used. 

**Random forces on the object.** Following [5] unmodeled dynamics is represented by applying random forces on the object. The probability _p_ that a random force is applied is sampled at the beginning of the randomization episode from the loguniform distribution between 0 _._ 1% and 10%. Then, at every timestep, with probability _p_ we apply a random force from the 3-dimensional Gaussian distribution with the standard deviation equal to 1 _m/s_<sup>2</sup> times the mass of the object on each coordinate and decay the force with the coefficient of 0 _._ 99 per 50ms. 

**Physics randomizations.** Physical parameters like friction, link and object masses, cube size, joint and tendon properties, as well as correlated noise parameters are randomized every time an 

30 

|**Parameter**|**Scaling factor range**|**Additive term range**|
|---|---|---|
|object dimensions|uniform([0_._95_,_1_._05])||
|object and robot link masses|uniform([0_._5_,_1_._5])||
|surface friction coefficients|uniform([0_._7_,_1_._3])||
|robot joint damping coefficients|loguniform([0_._3_,_3_._0])||
|actuator forcegains (P term)|loguniform([0_._75_,_1_._5])||
|joint limits||_N_(0_,_0_._15) rad|
|gravity vector (each coordinate)||_N_(0_,_0_._4) m_/_s<sup>2</sup>|



Table 18: Ranges of physics parameter randomizations. 

environment is reset, with a minimum interval of 720 steps. Table 18 lists all physics parameters that are randomized. 

### **A.4.2 OpenAI Observations** 

We conduct experiments with Shadow Hand OpenAI observations with a tighter success tolerance of 0.1 radians and show the reward curves as well as the consecutive successes achieved with this training in Figure 18 and 19. 



<!-- Start of picture text -->
0 Steps (millions) 1310 0 Steps (millions) 1310<br>30<br>8000<br>6000<br>20<br>4000<br>10<br>2000<br>0 0<br>0 5000 10000 15000 20000 0 5000 10000 15000 20000<br>Time (sec) Time (sec)<br>(a) Reward (b) Consecutive Successes<br>Reward<br>Consecutive Success<br><!-- End of picture text -->

Figure 18: Training curves for ShadowHand environments with **OpenAI observations** and Feed Forward policy and value functions with a tighter success tolerance of 0.1 rad. 

**Feed Forward Networks** We achieve 20 consecutive successful cube rotations after training in just under 1 hour. This is similar to the performance<sup>4</sup> achieved by OpenAI _et al._ [5] but with a cluster of 384 16-core CPUs and 8 V100 GPUs with training for 30 hours while we only need a single A100. 

**LSTMs** Using sequence networks like LSTMs improve the performance and we find that we are able to achieve 37 consecutive successful cube rotations after training in just under 6 hours. OpenAI _et al._ [5] achieve similar performance in about 17 hours again on a cluster of 384 16-core CPUs and 8 V100 GPUs. We use a sequence length of 4 to train the LSTM. Various other parameters for this set up are in Table 17. 

We also note that training with a tolerance of 0.1 rad and testing with a tolerance of 0.4 rad, we are able to even go up to 44 consecutive cube rotations. 

> 4pp 13, Section 6.5 titled **Sample Complexity & Scale** 

31 



<!-- Start of picture text -->
0 Steps (millions) 897 0 Steps (millions) 897<br>40<br>10000 35<br>30<br>8000<br>25<br>6000<br>20<br>4000 15<br>10<br>2000<br>5<br>0 0<br>0 5000 10000 15000 20000 0 5000 10000 15000 20000<br>Time (sec) Time (sec)<br>(a) Reward (b) Consecutive Successes<br>Reward<br>Consecutive Success<br><!-- End of picture text -->

Figure 19: Training curves for ShadowHand environments with **OpenAI observations** and an LSTM based policy and value function with a tighter success tolerance of 0.1 rad. 

32 

