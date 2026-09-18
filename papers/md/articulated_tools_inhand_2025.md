# **In-Hand Manipulation of Articulated Tools with Dexterous Robot Hands with Sim-to-Real Transfer** 

Soofiyan Atar<sup>1</sup> , Daniel Huang<sup>1</sup> , Florian Richter<sup>1</sup> , Michael Yip<sup>1</sup> , _Senior Member, IEEE_ 



**Fig. 1:** An illustration is shown where a privileged oracle is trained in simulation and distilled into a proprioceptive student policy for hardware deployment. Real-world tactile and motor torque signals are then used to train the CATFA module, which refines the transferred policy through cross-attention for contact-aware adaptation. 

**_Abstract_ — Reinforcement learning (RL) and sim-to-real transfer have advanced rigid-object manipulation. However, policies remain brittle for articulated mechanisms due to contact-rich dynamics that require both stable grasping and simultaneous free in-hand articulation. Furthermore, articulated objects and robot hands exhibit under-modeled joint phenomena such as friction, stiction, and backlash in real life that can increase the sim-to-real gap, and robot hands still fall short of idealized tactile sensing, both in terms of coverage, sensitivity, and specificity. In this paper, we present an original approach to learning dexterous in-hand manipulation of articulated tools that has reduced articulation and kinematic redundancy relative to the human hand. Our approach augments a simulationtrained base policy with a sensor-driven refinement learned from hardware demonstrations. This refinement conditions on proprioception and target articulation states while fusing wholehand tactile and force–torque feedback with the policy’s action intent through cross-attention. The resulting controller adapts online to instance-specific articulation properties, stabilizes contact interactions, and regulates internal forces under perturbations. We validate our method across diverse real-world tools, including scissors, pliers, minimally invasive surgical instruments, and staplers, demonstrating robust sim-to-real transfer, improved disturbance resilience, and generalization across structurally related articulated tools without precise physical modeling. Website.** 

## I. INTRODUCTION 

A central goal of robotics is to enable operation in humancentric environments [1], which require interacting with tools designed for human hands. While manipulation of rigid objects has progressed significantly [2], [3], **articulated tools** with internal kinematics, such as scissors or pliers, remain 

> 1Electrical and Computer Engineering Department, University of California, San Diego, La Jolla, CA 92093 USA. _{_ satar, yah032, frichter, yip _}_ @ucsd.edu 

fundamentally challenging. Their joint-dependent dynamics and contact constraints demand precise coordination beyond standard rigid-object control. This challenge is especially critical for humanoid robots [4], [5], which, with their dexterous multi-fingered hands, are expected to use tools and operate in environments built for people [6], [7]. Advancing dexterous in-hand manipulation of articulated tools is therefore a key step toward scalable real-world deployment and practical humanoid capability [8]. 

Beyond sim-to-real transfer, other learning-based strategies have been explored for dexterous manipulation. Imitation learning [9], [10] and foundation models [11] leverage human demonstrations to guide policy training. Demonstration data are often collected via teleoperation with dexterous hands, sometimes enhanced with haptic feedback [12]. While effective, these approaches face limited scalability due to the high cost and time required for demonstration collection. Another direction is hierarchical policy learning and task planning [13], [14], which decomposes complex skills into structured sub-tasks. However, when low-level skills fail to provide accurate or robust feedback, minor execution errors cascade upward, ultimately degrading the performance of higher-level plans. These limitations become particularly pronounced in articulated, contact-rich settings, where precise force regulation and internal joint coordination are critical. 

The prevailing paradigm for training dexterous hands relies on sim-to-real policy transfer [3], [15]. While effective for rigid objects and suction-based grasping [16], [17], this paradigm breaks down in a dynamic, contact-rich manipulation—particularly for articulated tools held in highdegree-of-freedom (DOF) robot hands. Internal joint coupling, friction, stiction, and contact constraints are difficult to 

model, thereby amplifying reality gaps and degrading policy reliability. Articulated tools further introduce joint-dependent dynamics and nonlinear contact interactions, widening this gap. Although tactile and visuo-tactile feedback can partially mitigate state uncertainty [18], [19], current simulators remain fundamentally limited in accurately modeling multibody contact under complex dynamical and kinematic constraints, leading to brittle policies and poor transfer [20]. Taken together, these limitations reveal a fundamental gap; current learning-based approaches remain brittle when confronted with the coupled kinematics and contact dynamics of articulated tools in the real world. 

In this work, we demonstrate that dexterous robotic hands can reliably manipulate articulated tools under real-world contact dynamics, without relying on perfectly modeled simulation or large-scale teleoperated demonstrations. To achieve this, we present the following contributions: 

- A disturbance-driven sim-to-real training pipeline that distills a privileged simulation policy into a student policy trained with structured force–torque randomwalk perturbations to improve contact robustness. 

- Cross-Attention Tactile Force Adaptation (CATFA), an intent-conditioned adaptation module that fuses the frozen base policy embedding with real tactile and force–torque feedback via multi-head cross-attention to produce contact-aware actions. 

- Comprehensive real-world evaluation across five articulated tools, including perturbation analysis and quantitative robustness benchmarking. 

We validate our approach both in simulation and on a physical Franka arm with a dexterous hand, showing substantial improvements in grasp stability and disturbance robustness across all five articulated tools. 

## II. RELATED WORKS 

In-hand manipulation [21], [22], [23] has seen significant progress through reinforcement learning (RL) within a simto-real framework. Seminal works [24] in reorienting a rigid cube and demonstrating dynamic pen spinning have shown that complex skills can be learned entirely in simulation. These methods typically rely on extensive domain randomization to train policies that are robust enough for zero-shot or open-loop transfer to the real world [25], [26]. However, this approach often proves brittle, as the policies still struggle to overcome the reality gap caused by unmodeled, contactrich physics. 

Recent work shows that input representations such as point clouds can significantly improve generalization to novel objects with multi-fingered hands, enabling sim-to-real transfer with minimal real-world tuning [27]. The benefit of rich tactile feedback [28] has been demonstrated, with zero-shot transfer of rotational manipulation tasks for unseen objects under varying contact conditions. 

Separately, a significant body of research has focused on the broader challenge of articulated-object manipulation, with an emphasis on tasks such as opening doors, drawers, and cabinets. Prominent works [29], [30] have successfully 

trained single, general-purpose policies that map visual inputs (typically point clouds) to robot arm actions, enabling zero-shot transfer to a variety of unseen objects. These methods have made great strides in solving the perception and motion planning problems associated with interacting with articulated mechanisms in the environment. However, these approaches treat the articulated object as part of the static world and do not address the distinct and more dynamic challenge of in-hand manipulation, where the object is held and controlled entirely within the grasp of a dexterous hand, thereby requiring the palm and fingers to achieve both objectives of stable grasp, but also articulability of the object. 

The challenge of in-hand manipulation is amplified for articulated tools, whose internal dynamics are complex to simulate. Simple cases, such as power tools with a single trigger finger, allow grasp and articulation to be decoupled. Still, tools like scissors or laparoscopic instruments involve coupled motions that create complex contact interactions. Recent work on tweezer manipulation [31] has shown progress, but remains limited to a single tool and relies on privilegeinformed controllers, reducing generalizability and bypassing the challenge of online skill discovery. In contrast, our approach introduces a post-transfer adaptation mechanism that learns robust, generalizable policies directly from realworld interaction. 

Because of the complexities of in-hand manipulation of articulated tools and the limited observations available from in-hand cameras, the importance of tactile feedback [32] quickly becomes important. However, far fewer recent works explore non-vision-based tactile skin simulation that realistically captures both normal and shear forces. Some simulate simplified skin deformation [33], [34] and sensor response handling, cross-talk, and noise, but remain intractable for training reinforcement learning policies. Others use binary or coarse tactile sensors (e.g., force-sensitive resistors), and other simulators do not represent shear dynamics under contact [35], [36]. In contrast, our work employs wholehand tactile sensing, providing quantized continuous force readings, which are structured into a tactile image and embedded before cross-attention conditioning of the BC policy. 

## III. METHODS 

Our framework, Fig. 2, consists of three stages: (1) training a privileged oracle policy in simulation with disturbance augmentation, (2) distilling the oracle into a deployable proprioceptive base policy for sim-to-real transfer, and (3) enabling online adaptation on hardware via a cross-attention tactile–force refinement module (CATFA). Each stage addresses a specific limitation of articulated in-hand manipulation, progressively bridging the gap between simulation robustness and real-world contact uncertainty. 

## _A. Oracle Policy Definition and Training_ 

We first describe the simulation stage in which a privileged oracle policy is trained to achieve stable articulation behavior under structured perturbations. We define an oracle 





<!-- Start of picture text -->
(a)<br><!-- End of picture text -->





<!-- Start of picture text -->
(b)<br><!-- End of picture text -->

**Fig. 2:** Technical overview of our pipeline for articulated in-hand manipulation. (a) Oracle training with privileged observations in simulation, followed by distillation into a proprioceptive base policy and real-world data collection with additional tactile _ft_<sup>tact</sup> and motor torque _τt_<sup>motor</sup> signals. (b) CATFA fuses these sensory modalities with policy intent via cross-attention to enable online adaptation on hardware. This design establishes a disturbance-aware sim-to-real framework that refines contact interactions and improves robustness under articulation-dependent dynamics. 

policy, _π_ oracle, with privileged observations to learn a base controller for in-hand articulated manipulation. The oracle is trained in simulation using PPO [37] with a curriculum of force–torque perturbations applied to the articulated tool. The disturbance magnitude is gradually increased to emulate arbitrary gravity vectors and external contact dynamics, stabilize articulation under simulated disturbances (see Sec. IIIA). At each timestep _t_ , the oracle outputs absolute joint targets _ut ← π_ oracle( _ot_ ) from privileged observations _ot_ . The privileged signals are later removed via distillation for simto-real transfer, which is more efficient than directly training with non-privileged observations. 

**Initial State.** The articulated tool is initialized using teleoperated demonstrations with a hand tracker (Manus gloves [38]) when a stable grasp cannot be achieved autonomously. This ensures rollouts begin from feasible hand–tool configurations despite articulation variability. 

**Observations.** The privileged observation at time _t_ is 



where _qt ∈_ R<sup>6</sup> and _q_ ˙ _t ∈_ R<sup>6</sup> are joint positions and velocities of the active DoFs (four finger joints and two thumb joints of the Inspire hand), and _ut−_ 1 _∈_ R<sup>6</sup> is the previous joint target. The articulation state is given by _θt_<sup>art</sup> _∈_ R and _θ_ ˙ _t_<sup>art</sup> _∈_ R. The tool pose is represented by _x_<sup>obj</sup> _t ∈_ R<sup>3</sup> and _x_ ˙<sup>obj</sup> _t ∈_ R<sup>3</sup> , corresponding to the position and linear velocity of a reference frame attached to the articulation joint axis (Fig. 5), expressed in the robot base frame. This frame is defined in the URDF and does not correspond to the center of mass or tool tip. Raw simulated joint force signals are _τt_<sup>raw</sup> _∈_ R<sup>6</sup> . The binary one-hot articulation command _st ∈{_ 0 _,_ 1 _}_<sup>2</sup> specifies the desired state (e.g., open or closed). The previous action _ut−_ 1 is included only in the oracle’s privileged observation to compensate for action smoothing and accumulated perturbations, and is removed during distillation. 

**Actions.** At each timestep, the policy outputs absolute joint 

|Equation|Scale|
|---|---|
|_r_<sup>pos</sup><br>_t_<br>=_−∥x_<sup>obj</sup><br>_t_<br>_−x_<sup>obj</sup><br>0 <sup>_∥_2</sup><br>2<br>_r_<sup>quat</sup><br>_t_<br>=_−∥q_<sup>obj</sup><br>_t_<br>_−q_<sup>obj</sup><br>0 <sup>_∥_2</sup><br>2<br>_r_<sup>goal</sup><br>_t_<br>=_−_<br>��_θ_art<br>_t _<sup>_−θ_target</sup><br>_st_<br>��<br>|500.0<br>5.0<br>10.0|
|<br><br><br>_T_ <sup>open</sup><br>_t−_1 <sup>+1</sup><sup>_,_</sup><br>_st_ = 1_∧θ_<sup>art</sup><br>_t_<br>_≥θ_open_,_||
|_r_<sup>timer</sup><br>_t_<br>=<br><br><br><br>_T_ <sup>close</sup><br>_t−_1 <sup>+1</sup><sup>_,_</sup><br>_st_ = 0_∧θ_<sup>art</sup><br>_t_<br>_≤θ_close_,_<br>_−_1_,_<br>otherwise|0.05|
|_r_<sup>inc</sup><br>_t_<br>= <sup>�</sup><br>_ϑ∈_Θ_st _<sup>_w_(</sup><sup>_ϑ_)</sup><sup>**1**</sup><sup>_{θ_art</sup><br>_t_<br>crosses _ϑ}_|1.0|
|<br>_r_<sup>contact</sup><br>_t_<br>=_n_<sup>_⋆_</sup>_−nt_<br>_r_<sup>slip</sup><br>_t_<br>=**1**_{h_<sup>obj</sup><br>_t_<br>_< h_min_}_<br>_r_<sup>act</sup><br>_t_<br>=_−∥ut∥_<sup>2</sup><br>2|-0.1<br>-1.0<br>-0.001|



**TABLE I:** Reward function for the oracle policy. 

targets _ut ∈_ R<sup>6</sup> for the hand. To improve stability and reduce vibration, the executed command is smoothed using an exponential moving average: 



**Reward.** The reward is designed to to promote articulation progress and grasp stability under perturbations jointly. The reward (Table I) balances articulation progress and grasp stability. Pose regularization terms _rt_<sup>pos</sup> and _rt_<sup>quat</sup> penalize deviation from the initial pose. Task completion is encouraged through _rt_<sup>goal</sup> , minimizing error between _θt_<sup>art</sup> and the target _θs_<sup>target</sup> _t_ , and _rt_<sup>timer</sup> , rewarding sustained achievement of articulation state _st_ . Incremental shaping _rt_<sup>inc</sup> provides bonuses as _θt_<sup>art</sup> crosses thresholds in Θ _st_ where Θ _st_ is a set of predefined articulation angle thresholds corresponding to the commanded state _st_ . Stability is enforced via the contact term _rt_<sup>contact</sup> , penalizing deviation between the number of finger link contacts _nt_ and the desired count _n_<sup>_⋆_</sup> , and the slippage term _rt_<sup>slip,activatedwhenobjectheight</sup><sup>_h_obj</sup> _t_ drops below _h_ min. Finally, the action penalty _rt_<sup>act</sup> regularizes joint motion to prevent excessive excursions and over-tightening that may destabilize articulation. 

**Policy optimization with random walk perturbations.** To further improve robustness beyond reward shaping alone, 

we introduce structured disturbance augmentation during training. External disturbances are simulated as a random walk during training. At each step, external forces _Ft_<sup>ext</sup> _∈_ R<sup>3</sup> and torques _τt_<sup>ext</sup> _∈_ R<sup>3</sup> applied to the hand and tool are updated as 



where ∆ _Ft_<sup>ext</sup> and ∆ _τt_<sup>ext</sup> are sampled from uniform ranges and clipped within predefined bounds. A random walk in force–torque space allows directional accumulation over time, covering disturbances that emulate gravity, acceleration, and external contact within a bounded domain. As shown in Fig. 3, policies trained with random-walk perturbations exhibit improved robustness to external disturbances and the model produces joint configurations that more stably secure the articulated tool in both open and closed states. 

## _B. Base Policy Distillation_ 

While the oracle benefits from privileged state information, such signals are unavailable on hardware. We therefore distill the oracle into a deployable student policy that relies only on observable proprioceptive inputs. Standard distillation methods such as DAgger [39] are ineffective for articulated in-hand manipulation, as partially informed students _π_ student frequently drop objects early and fail to explore. Instead, we distill from stable oracle rollouts _π_ oracle to train a proprioceptive student that operates without privileged inputs. Although visuotactile policies [19] achieve strong performance in simulation, they exhibit a significant sim-toreal gap due to occlusions and sensing discrepancies (see Sec. III-C). In contrast, proprioceptive inputs ( _qt, st_ ) are consistent in simulation and directly observable on hardware, making them more suitable for transfer. Accordingly, we first train an oracle policy _π_ oracle using privileged state information in simulation, then distill its actions into a student policy _π_ student that operates without privileged inputs. Randomwalk force–torque perturbations (Eq. 2) are retained during training, allowing the student to develop robustness to gravity and contact disturbances under quasi-static manipulation. 

## _C. Online Adaptation via Cross-Attention Tactile Force Module (CATFA)_ 

Although the distilled student policy enables sim-to-real transfer, it remains open-loop and lacks real-time sensory feedback. We therefore introduce an online adaptation mechanism to compensate for unmodeled contact dynamics. The distilled base policy _π_ student provides a motion prior but operates open-loop, lacking real-time feedback. This is particularly limiting for articulated tools, where internal joint coupling and contact dynamics increase the likelihood of slip during in-hand execution. Although domain randomization improves simulation robustness, the absence of sensing prevents corrective responses to object slip and disturbances. To address this, we introduce _Cross-Attention Tactile Force Adaptation (CATFA)_ , which incorporates real tactile and joint force inputs to refine the behavior of _π_ student and enable 





**(a) (b)** 

**Fig. 3:** (a) Tool pose variation during open and close phases under dynamic perturbations. The blue curve corresponds to the policy trained with injected perturbations (randomly sampled forces and torques), showing reduced deviation compared to the baseline. (b) Perturbation injection on the scissor, where forces and torques ( _F_ 0 _, F_ 1 _. . ._ ) are sequentially applied during articulation. Both forces and torques are sampled from a predefined ranges and updated as a random walks during execution. 



**Fig. 4:** Inspire hand with an augmented tactile structure. A 3Dprinted pad and foam layer redistribute contact loads to enhance tactile sensitivity and repeatability, while motor and mimic joints are illustrated for clarity. Motor torques _τt_<sup>motor</sup> are computed only from active joints. These tactile and motor signals provide the hardware feedback used by CATFA for cross-attentive tactile–force refinement. 

disturbance rejection. Unlike standard multimodal fusion that concatenates sensor features, CATFA treats the base policy embedding as a query and attends to sensor-derived keys and values. This intent-conditioned design enables targeted correction rather than symmetric feature aggregation, effectively serving as a learned impedance adaptation layer that injects feedback only when contact discrepancies arise. 

## **Reducing Partial Observability via Tactile–Force Feed-** 

**back.** In simulation, the oracle observation _ot_ provides a sufficient description of the articulated hand–tool state and induces a Markov process. After distillation, the hardware policy observes only 



which is a projection of the underlying physical state 



where _ηt_ denotes latent compliance and frictional effects. _Assumption (Load-Bearing Contact)._ During manipulation, the tool is fully supported by the hand; gravity and articulation torques are transmitted through finger contacts, yielding informative tactile and motor-torque signals. Augmenting the observation with 



we model measurements as 



Under this assumption, _yt_ depends on _ηt_ through _h_ ( _χt_ ), implying 



and therefore 



Thus tactile–force feedback reduces uncertainty over latent contact dynamics and moves the representation closer to Markovian. 

_Action-Space Correction._ Let the optimal action under full state information be _u_<sup>_∗_</sup> _t_<sup>=</sup><sup>_π∗_(</sup><sup>_χt_).Underpartialobservabil-</sup> ity, the Bayes-optimal action is 



which generally differs from the distilled base policy 



CATFA therefore learns a residual correction 



where ∆ _ut_ is trained from real rollouts to compensate for systematic discrepancies induced by latent contact dynamics. While no explicit posterior over _ηt_ is computed, the correction implicitly captures the conditional dependence of the optimal action on tactile–force measurements. 

**Hardware Sensing.** On the hardware side, additional tactile and motor force signals are available but are not accurately reproduced in simulation. Each finger is equipped with resistive tactile skins that provide quantized force readings _ft_<sup>tact</sup> _∈_ R<sup>36</sup><sup>_×_44</sup> over the pads. To improve sensitivity and repeatability under noisy sensing, we introduce a foamplate-pad layer (Fig. 4) that redistributes local contact loads across neighboring taxels. We also measure motor torques _τt_<sup>motor</sup> _∈_ R<sup>6</sup> via current sensing. Geared actuators drive flexion, while extension relies on passive spring return. In simulation, the oracle policy _π_ oracle uses actuator estimates _τt_<sup>raw</sup> , which differ from hardware measurements _τt_<sup>motor</sup> due to transmission effects (e.g., gear ratios, friction, backlash, compliance, and sensor scaling). Modeling these effects would require detailed system identification; instead, we directly incorporate _ft_<sup>tact</sup> and _τt_<sup>motor</sup> into CATFA. 

**Model Architecture.** We now describe how these sensory modalities are integrated with the base policy. CATFA augments the frozen base policy _π_ student with a sensor-driven refinement network. At each timestep _t_ , the base policy 

_π_ student produces an internal intent embedding _zt ∈_ R<sup>64</sup> from its final MLP layer. In parallel, the _ft_<sup>tact</sup> _∈_ R<sup>36</sup><sup>_×_44</sup> is processed by a convolutional encoder to yield a compact feature vector _ϕ_<sup>tact</sup> _t ∈_ R<sup>64</sup> . In contrast, _τt_<sup>motor</sup> are mapped through a two-layer MLP to produce _ϕ_<sup>force</sup> _t ∈_ R<sup>64</sup> . These sensor encodings are concatenated into _Ft_ = [ _ϕ_<sup>tact</sup> _t_<sup>_, ϕ_force</sup> _t_ ] _∈_ R<sup>2</sup><sup>_×_64</sup> . A multi-head cross-attention module (MHA, with 8 heads and embed dimension 64) fuses intent and sensor signals by querying with _zt_ against _Ft_ . 



This formulation enables intent-conditioned feedback, where corrective signals are applied selectively based on the policy’s internal action embedding rather than through symmetric feature fusion. As attention applies corrections only when supported by sensory evidence, articulation behavior learned in simulation is preserved while allowing targeted adjustments. The adaptor adds minimal parameters and runs at the same control frequency without increasing inference latency. 

**Training Adaptation.** We fine-tune the system by deploying the sim-to-real base policy _π_ student on hardware under random disturbances and collecting fewer than 50 successful rollouts annotated via human feedback. Each rollout spans 2000 timesteps and includes multiple open/close phases, with the articulation command _st_ switching at random intervals (e.g., _t_ = 50 to _t_ = 250). This exposes the policy to diverse articulation states and transitions under gravity and contact effects. CATFA is trained via behavior cloning on a small human-labeled successful real-world rollouts. Given demonstrations _D_ = _{_ ( _qt, st, ut_ ) _}_ , with oracle actions _ut_ , the student minimizes 



enabling efficient sim-to-real adaptation under contact-rich dynamics. During adaptation, the base policy _π_ student remains frozen, allowing CATFA to inherit the motion prior while learning real-time corrective feedback. Together, the disturbance-trained oracle, distilled base policy, and crossattention refinement module form a structured sim-to-real pipeline for articulated in-hand manipulation. 

**Cross-Attention vs Concatenation:** Direct concatenation of sensory embeddings perturbs the articulation prior symmetrically, regardless of whether contact discrepancies are present. In contrast, cross-attention conditions corrections on the policy’s internal intent representation _zt_ , enabling targeted feedback only when tactile or torque signals indicate deviation from expected contact behavior. This intentconditioned design preserves nominal articulation trajectories while selectively compensating for unmodeled contact dynamics. 

## IV. EXPERIMENTS 

**Articulated Tool Set.** We evaluate on five articulated tools, each modeled with a single revolute joint and instantiated in both simulation and hardware (Fig. 5). In simulation, object mass, surface friction, and material properties are randomized to improve transfer robustness. While 



**Fig. 5:** Articulated tools used in experiments: real-world examples (top) and simulated counterparts (bottom). The axis denotes the articulation rotation axis. These tools span a wide range of articulation types and gripping strategies, capturing diverse kinematic structures and manipulation provisions. 

simulated joints capture intended kinematics, they do not fully reproduce real-world mechanics, introducing a domain gap. To account for scale differences, mechanical fixtures are attached so the tools fit the Inspire hand, which is approximately 1.4× the size of an average human hand. This provides a controlled yet challenging benchmark for articulated in-hand manipulation. 

**Hardware.** We use the Inspire Hand with 6 active DoFs (one per finger, two for the thumb) and 6 mimic joints. Joint targets are issued at 30 Hz and tracked by a low-level PD controller at 120 Hz. Tactile sensing operates at 75 Hz using a 36 _×_ 44 resistive array, with additional force measurements at all active joints. The hand is covered with a nitrile glove for consistent contact properties. Initial grasp configurations are collected using Manus MetaGloves Pro [38] (Sec. III-A), and tactile augmentation details are provided in Sec. III-C and Fig. 4. 

**Simulation.** Policies are trained in IsaacLab [40]. Each environment contains a hand and an articulated tool initialized to a feasible state. The simulator runs at 120 Hz with control decimation of 3 (effective 40 Hz). Episodes last 2000 steps ( _≈_ 50s) and terminate upon object drop, workspace exit, or horizon completion. Contact dynamics are approximated using convex decomposition for complex geometries and convex hulls for simpler ones. We run 8192 parallel headless environments on a single Nvidia RTX 4090. Training for each tool requires 4–12 hours, and more complex collision models increase the computational cost. 

## _A. Baselines and Ablation Study_ 

We perform two experiments to evaluate the role of tactile and force feedback. In the first study (Tab. II), we compare 

|**Policy**<br>**Articulated Tool**|**Succ (%)** _↑_|**Opening Disp. (mm)** _↑_|**Closure Residual (mm)** _↓_|
|---|---|---|---|
|_Simulation (Oracle, referenc_|_e only)_|||
|Surgical Clamp|100|17.26 _±_ 0.63|0.0 _±_ 0.0|
|Tong|100|51.55 _±_ 2.93|17.23 _±_ 1.45|
|Plier|100|17.45 _±_ 1.20|9.34 _±_ 2.10|
|Laparoscopic Tool|100|99.31 _±_ 2.24|67.62 _±_ 1.58|
|Stapler|100|22.88 _±_ 1.44|0.000 _±_ 0.000|
|_Sim-to-Real (Student)_||||
|Surgical Clamp|20|6.8 _±_ 2.3|3.4 _±_ 3.8|
|Tong|100|51.23 _±_ 3.97|29.17 _±_ 1.26|
|Plier|30|9.81 _±_ 3.30|9.06 _±_ 9.36|
|Laparoscopic Tool|100|**109.45** _±_ **9.98**|76.98 _±_ 4.52|
|Stapler|100|11.32 _±_ 4.70|1.03 _±_ 0.97|
|_Proprioceptive BC_||||
|Surgical Clamp|90|6.6 _±_ 0.66|1.46 _±_ 0.45|
|Tong|100|51.55 _±_ 0.87|32.64 _±_ 1.7|
|Plier|70|7.73 _±_ 1.87|3.68 _±_ 0.21|
|Laparoscopic Tool|100|107.39 _±_ 1.48|75.07 _±_ 2.06|
|Stapler|100|13.08 _±_ 0.48|0.6 _±_ 0.5|
|**CATFA (Ours)**||||
|Surgical Clamp|100|**8.5** _±_ **0.8**|**0.0** _±_ **0.0**|
|Tong|100|**64.23** _±_ **0.36**|**28.31** _±_ **0.91**|
|Plier|100|**11.28** _±_ **0.76**|**3.12** _±_ **0.16**|
|Laparoscopic Tool|100|109.31 _±_ 1.05|**73.28** _±_ **1.6**|
|Stapler|100|**14.52** _±_ **0.59**|**0.15** _±_ **0.09**|



**TABLE II:** Quantitative evaluation on articulated tool manipulation. Simulation (Oracle) results are shown for reference only and are not considered for bold comparison. **Opening Disp.** denotes maximum achieved tip separation in the open state (higher is better). **Closure Residual** denotes the remaining tip gap in the closed state (lower is better). Best real-world results per tool are highlighted in bold. 

the sim-to-real student policy _π_ student, a Proprioceptive BC policy (without tactile or force inputs), and CATFA. For each articulated tool, we conduct approximately 10 realworld rollouts and evaluate articulation performance using three metrics: success rate, maximum tip separation in the open state, and residual tip gap in the closed state. Success is defined as maintaining the commanded open or closed configuration (joint angle above or below a predefined threshold) throughout the episode, and tip metrics are computed from endpoint separation after each open/close phase and averaged across trials. 

In the second study (Tab. III), we mount the dexterous hand on a Franka arm and execute predefined end-effector trajectories with randomized accelerations to induce motionplanning disturbances. In addition to the above baselines, we include Proprio–Force BC, Proprio–Tactile BC, and Proprio–Tactile–Force BC, where tactile and/or force embeddings are directly concatenated without cross-attention refinement. We track the articulated tool pose using ArUco markers and quantify robustness via pose deviation, 



where **x**<sup>obj</sup> _t_ and **q**<sup>obj</sup> _t_ denote object position and unit quaternion orientation, and _λ_ balances translational and rotational contributions. Orientation deviation is computed using the _ℓ_ 2 distance between unit quaternions, _∥_ **q** _t−_ **q** 0 _∥_ 2, which approximates the geodesic distance for small angular deviations. All results are reported as mean _±_ standard deviation over _n_ = 10 independent real-world rollouts per tool. 



An overview of the pipeline is shown in Fig. 2. We evaluate the effectiveness of CATFA for sim-to-real adaptation against multiple behavior-cloning baselines. 







<!-- Start of picture text -->
(a) Closed trajectory comparison (b) Open trajectory comparison<br><!-- End of picture text -->

**Fig. 6:** Closed-loop disturbance response during articulated manipulation. We plot the composite pose deviation ∆( _t_ ) = _∥xt_<sup>_obj_</sup> _− x_<sup>_obj_</sup> 0 _∥_ 2 + _λ∥qt_<sup>_obj_</sup> _− q_ 0<sup>_obj_</sup> _∥_ 2. (a) Closed articulation phase. (b) Open articulation phase. CATFA (solid blue) yields a uniformly lower mean error and attenuates high-frequency oscillations induced by disturbances. The proprioceptive BC policy (dashed red) accumulates drift, while the distilled student (dash-dotted green) exhibits large transient error spikes under contact perturbations. These results indicate improved closed-loop robustness and sensor-conditioned stabilization of internal articulation dynamics. 

|Policy|Cl|amp|Pl|ier|Laprosc|opic tool|
|---|---|---|---|---|---|---|
||Open (m)|Close (m)|Open (m)|Close (m)|Open (m)|Close (m)|
|Sim-to-Real (Student)|0.056 _±_ 0.04|0.083 _±_ 0.038|0.265 _±_ 0.078|0.188 _±_ 0.068|0.242 _±_ 0.135|0.09 _±_ 0.044|
|Proprioception BC|0.083 _±_ 0.02|0.053 _±_ 0.017|0.096 _±_ 0.084|0.073 _±_ 0.045|0.159 _±_ 0.096|0.053 _±_ 0.067|
|Proprio–Tactile-Force BC|0.031 _±_ 0.035|0.046 _±_ 0.068|0.046 _±_ 0.090|**0.031** _±_ **0.055**|0.87 _±_ 0.073|0.049_±_ 0.053|
|Proprio–Tactile BC|0.049 _±_ 0.04|0.045 _±_ 0.039|0.051 _±_ 0.043|0.065 _±_ 0.042|0.89 _±_ 0.067|0.052_±_ 0.060|
|Proprio–Force BC|0.046 _±_ 0.038|0.046 _±_ 0.036|0.051 _±_ 0.042|0.056 _±_ 0.053|0.59 _±_ 0.058|0.076_±_ 0.066|
|**CATFA (Ours)**|**0.022** _±_ **0.018**|**0.035** _±_ **0.024**|**0.039** _±_ **0.026**|0.033 _±_ 0.018|**0.05** _±_ **0.066**|**0.044**_±_ **0.086**|



**TABLE III: Perturbation analysis** across three articulated tools in open and closed states. Each entry reports mean _±_ std of pose deviation _e_ pose (m) _↓_ , where _e_ pose( _t_ ) = _∥_ **x** _t −_ **x** 0 _∥_ 2 + _λ∥_ **q** _t −_ **q** 0 _∥_ 2, averaged over _n_ = 10 real-world rollouts while the Franka executes a predefined random trajectory with injected perturbations. Lower is better. m –¿ meters 

**Baselines.** For articulated manipulation (Tab. II), we compare CATFA with (1) a Proprioceptive BC policy (no tactile or force inputs) and (2) the distilled sim-to-real policy _π_ student deployed on hardware with limited fine-tuning. 

**Real-world evaluation.** We evaluate on five articulated tools (Fig. 5). Quantitative results are reported on in-domain objects, with additional qualitative demonstrations on tools varying in weight and geometry. Success is defined by maintaining articulation angle thresholds across repeated open–close cycles (Tab. II). CATFA achieves the most consistent articulation, reducing variance and failure under perturbations compared to all baselines. 

**Robustness to perturbations.** For the dynamic evaluation (Tab. III), we additionally compare Proprio–Force BC, Proprio–Tactile BC, and Proprio–Tactile–Force BC, where tactile and/or force embeddings are directly concatenated without cross-attention refinement. We execute a predefined manipulation trajectory on the Franka hand–tool setup with randomized accelerations and external disturbances, and measure pose error combining position and quaternion deviations. CATFA yields the lowest or near-lowest error across tools, demonstrating improved disturbance rejection over direct-embedding baselines and the sim-to-real student. 

**Simulation validation.** In simulation, we compare policies trained with and without random-walk force–torque perturbations (Eq. 2). Perturbation-trained policies exhibit 

improved stability under disturbances, supporting the robustness gains observed on hardware. 

## VI. DISCUSSION & CONCLUSION 

Our results validate a disturbance-driven sim-to-real framework for in-hand articulation. Structured grasp initialization aligns the hand with tool joints, while simulation enables learning of contact-rich skills that transfer reliably through proprioceptive policies. 

Robustness is introduced at the simulation stage by training the privileged policy under structured force–torque random-walk perturbations. The distilled student inherits this disturbance-aware behavior without directly observing the perturbations. CATFA further refines the frozen student through an intent-conditioned cross-attention adaptor that fuses tactile and motor torque feedback to produce contact-aware corrections without retraining the base policy. Real-world experiments across five articulated tools confirm improved stability and disturbance rejection. This modular design supports extensibility: articulation policies serve as reusable skill primitives, and additional sensing modalities can be integrated via dedicated adaptors. 

During hardware experiments, minor joint microoscillations are occasionally observed in the Inspire hand due to backlash in the geared transmission and spring compliance not modeled in the simulation. These oscillations are reduced under CATFA compared to the 

proprioceptive BC baseline and do not affect articulation success. 

**Limitations and Future Work.** The current formulation assumes binary articulation commands _st ∈{_ 0 _,_ 1 _}_ , limiting applicability to tools with discrete open–close behaviors. Extending CATFA to continuous articulation targets and multiDOF articulated mechanisms remains future work. Hardware fine-tuning is sensitive to motor torque scaling and controlfrequency discrepancies between simulation and the geared, spring-assisted hand. Integrating adaptive torque calibration or online system identification may further reduce sim-to-real discrepancies arising from transmission effects. 

## REFERENCES 

- [1] S. Atar, X. Liang, C. Joyce, F. Richter, W. Ricardo, C. Goldberg, P. Suresh, and M. Yip, “Humanoids in hospitals: A technical study of humanoid robot surrogates for dexterous medical interventions,” 2025. 

- [2] H. Qi, B. Yi, M. Lambeta, Y. Ma, R. Calandra, and J. Malik, “From simple to complex skills: The case of in-hand object reorientation,” 2025. 

- [3] J. Wang, Y. Yuan, H. Che, H. Qi, Y. Ma, J. Malik, and X. Wang, “Lessons from learning to spin ”pens”,” 2024. 

- [4] F. Burget, A. Hornung, and M. Bennewitz, “Whole-body motion planning for manipulation of articulated objects,” in _2013 IEEE International Conference on Robotics and Automation_ , pp. 1656–1662, 2013. 

- [5] Y. Liu, Y. Yang, Y. Wang, X. Wu, J. Wang, Y. Yao, S. Schwertfeger, S. Yang, W. Wang, J. Yu, X. He, and Y. Ma, “Realdex: Towards human-like grasping for robotic dexterous hand,” in _Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial Intelligence_ , IJCAI-2024, p. 6859–6867, International Joint Conferences on Artificial Intelligence Organization, Aug. 2024. 

- [6] A. Werby, M. B¨uchner, A. R¨ofer, C. Huang, W. Burgard, and A. Valada, “Articulated object estimation in the wild,” 2025. 

- [7] R. Chu, Z. Liu, X. Ye, X. Tan, X. Qi, C.-W. Fu, and J. Jia, “Commanddriven articulated object understanding and manipulation,” in _2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 8813–8823, 2023. 

- [8] T. Asfour, P. Azad, N. Vahrenkamp, K. Regenstein, A. Bierbaum, K. Welke, J. Schr¨oder, and R. Dillmann, “Toward humanoid manipulation in human-centred environments,” _Robotics and Autonomous Systems_ , vol. 56, no. 1, pp. 54–65, 2008. Human Technologies: “Know-how”. 

- [9] T. Lin, Y. Zhang, Q. Li, H. Qi, B. Yi, S. Levine, and J. Malik, “Learning visuotactile skills with two multifingered hands,” 2024. 

- [10] J. Li, Y. Zhu, Y. Xie, Z. Jiang, M. Seo, G. Pavlakos, and Y. Zhu, “Okami: Teaching humanoid robots manipulation skills through single video imitation,” 2024. 

- [11] X. Zhang, Y. Wang, R. Wu, K. Xu, Y. Li, L. Xiang, H. Dong, and Z. He, “Adaptive articulated object manipulation on the fly with foundation model reasoning and part grounding,” 2025. 

- [12] Y. Lin, Y.-L. Wei, H. Liao, M. Lin, C. Xing, H. Li, D. Zhang, M. Cutkosky, and W.-S. Zheng, “Typetele: Releasing dexterity in teleoperation by dexterous manipulation types,” 2025. 

- [13] L. P. Kaelbling and T. Lozano-P´erez, “Hierarchical task and motion planning in the now,” in _2011 IEEE International Conference on Robotics and Automation_ , pp. 1470–1477, 2011. 

- [14] A. G. Barto and S. Mahadevan, “Recent advances in hierarchical reinforcement learning,” _Discrete Event Dynamic Systems_ , vol. 13, pp. 41–77, 2003. 

- [15] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik, “In-hand object rotation via rapid motor adaptation,” 2022. 

- [16] S. Atar, Y. Li, M. Grotz, M. Wolf, D. Fox, and J. Smith, “Optigrasp: Optimized grasp pose detection using rgb images for warehouse picking robots,” 2024. 

- [17] B. Yang, S. Atar, M. Grotz, B. Boots, and J. Smith, “DYNAMOGRASP: DYNAMics-aware optimization for GRASP point detection in suction grippers,” in _7th Annual Conference on Robot Learning_ , 2023. 

- [18] S. Wang, M. Lambeta, P.-W. Chou, and R. Calandra, “Tacto: A fast, flexible, and open-source simulator for high-resolution visionbased tactile sensors,” _IEEE Robotics and Automation Letters_ , vol. 7, p. 3930–3937, Apr. 2022. 

- [19] H. Qi, B. Yi, S. Suresh, M. Lambeta, Y. Ma, R. Calandra, and J. Malik, “General in-hand object rotation with vision and touch,” 2023. 

- [20] B. Acosta, W. Yang, and M. Posa, “Validating robotics simulators on real-world impacts,” 2022. 

- [21] J.-P. Saut, A. Sahbani, S. El-Khoury, and V. Perdereau, “Dexterous manipulation planning using probabilistic roadmaps in continuous grasp subspaces,” pp. 2907 – 2912, 10 2007. 

- [22] L. Han, Y. Guan, Z. Li, Q. Shi, and J. J. Trinkle, “Dextrous manipulation with rolling contacts,” pp. 992 – 997 vol.2, 05 1997. 

- [23] O. M. Andrychowicz, B. Baker, M. Chociej, R. J´ozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, J. Schneider, S. Sidor, J. Tobin, P. Welinder, L. Weng, and W. Zaremba, “Learning dexterous in-hand manipulation,” _The International Journal of Robotics Research_ , vol. 39, no. 1, pp. 3–20, 2020. 

- [24] OpenAI, I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, J. Schneider, N. Tezak, J. Tworek, P. Welinder, L. Weng, Q. Yuan, W. Zaremba, and L. Zhang, “Solving rubik’s cube with a robot hand,” 2019. 

- [25] A. Bhatt*, A. Sieler*, S. Puhlmann, and O. Brock, “Surprisingly robust in-hand manipulation: An empirical study,” in _Robotics: Science and Systems XVII_ , RSS2021, Robotics: Science and Systems Foundation, July 2021. 

- [26] S. Patidar, A. Sieler, and O. Brock, “In-hand cube reconfiguration: Simplified,” 2023. 

- [27] Y. Qin, B. Huang, Z.-H. Yin, H. Su, and X. Wang, “Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation,” 2022. 

- [28] M. Yang, C. Lu, A. Church, Y. Lin, C. Ford, H. Li, E. Psomopoulou, D. A. W. Barton, and N. F. Lepora, “Anyrotate: Gravity-invariant inhand object rotation with sim-to-real touch,” 2024. 

- [29] Y. Wang, Z. Wang, M. Nakura, P. Bhowal, C.-L. Kuo, Y.-T. Chen, Z. Erickson, and D. Held, “Articubot: Learning universal articulated object manipulation policy via large scale simulation,” 2025. 

- [30] Z. Xu, Z. He, and S. Song, “Universal manipulation policy network for articulated objects,” _IEEE Robotics and Automation Letters_ , vol. 7, p. 2447–2454, Apr. 2022. 

- [31] W. Xu, Y. Zhao, W. Guo, and X. Sheng, “Hierarchical reinforcement learning for articulated tool manipulation with multifingered hand,” 2025. 

- [32] N. Jawale, N. Kaur, A. Santoso, X. Hu, and X. Chen, _Learned Slip-Detection-Severity Framework using Tactile Deformation Field Feedback for Robotic Manipulation_ . 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), IEEE, 202410-14. 

- [33] S. Cremer, M. N. Saadatzi, I. B. Wijayasinghe, S. K. Das, M. H. Saadatzi, and D. O. Popa, “Skinsim: A design and simulation tool for robot skin with closed-loop phri controllers,” _IEEE Transactions on Automation Science and Engineering_ , vol. 18, no. 3, pp. 1302–1314, 2021. 

- [34] Z. Kappassov, J.-A. Corrales-Ramon, and V. Perdereau, “Simulation of tactile sensing arrays for physical interaction tasks,” in _2020 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM)_ , pp. 196–201, 2020. 

- [35] Y. Yuan, H. Che, Y. Qin, B. Huang, Z.-H. Yin, K.-W. Lee, Y. Wu, S.-C. Lim, and X. Wang, “Robot synesthesia: In-hand manipulation with visuotactile sensing,” 2024. 

- [36] Z.-H. Yin, B. Huang, Y. Qin, Q. Chen, and X. Wang, “Rotating without seeing: Towards in-hand dexterity through touch,” 2023. 

- [37] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” 2017. 

- [38] MANUS Technology Group, “High-precision hand tracking & mocap gloves — manus.” https://www.manus-meta.com/, 2025. Accessed: 2025-09-13. 

- [39] S. Ross, G. J. Gordon, and J. A. Bagnell, “A reduction of imitation learning and structured prediction to no-regret online learning,” 2011. 

- [40] M. Mittal, C. Yu, Q. Yu, J. Liu, N. Rudin, D. Hoeller, J. L. Yuan, R. Singh, Y. Guo, H. Mazhar, A. Mandlekar, B. Babich, G. State, M. Hutter, and A. Garg, “Orbit: A unified simulation framework for interactive robot learning environments,” _IEEE Robotics and Automation Letters_ , vol. 8, no. 6, pp. 3740–3747, 2023. 

