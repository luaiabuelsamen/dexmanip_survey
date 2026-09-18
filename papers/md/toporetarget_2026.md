# **TopoRetarget: Interaction-Preserving Retargeting for Dexterous Manipulation** 

**Jielin Wu**<sup>_∗_</sup> **, Shenzhe Yao**<sup>_∗_</sup> **, Guanqi He**<sup>_∗‡_</sup> **, Xiaohan Liu**<sup>_∗‡_</sup> **, Zhaoqing Zeng, Xiangrui Jiang, Han Yang, Wentao Zhang, Hang Zhao**<sup>_†_</sup> IIIS, Tsinghua University 

- _∗_ Equal contribution _‡_ Project lead _†_ Corresponding author 

- `Project Page: https://toporetarget2026.github.io/TopoRetarget/` 



Figure 1: **TopoRetarget** converts human hand-object trajectories collected with a motion-capture glove (A) into robot references for contact-rich dexterous manipulation. These retargeted references are used to train RL policies that execute dexterous skills in simulation (B) and transfer zero-shot to Wuji Hand (C). 

**Abstract:** Human hand-object demonstrations provide dense reference motions for training dexterous manipulation reinforcement learning (RL) policies through reference tracking. However, to use such demonstrations for RL policy learning, retargeting must preserve hand pose and task-relevant hand-object contact structure. Otherwise, contact and feasibility artifacts can degrade downstream RL policy performance. We introduce **TopoRetarget** , an interaction-preserving retargeting framework that uses a single set of parameters across diverse retargeting conditions while maintaining task-relevant hand-object interaction and adapting human demonstrations to dexterous robot hands. The method constructs a sparse interaction graph over hand and object keypoints and optimizes distance-weighted Laplacian deformation with directional consistency, kinematic constraints, and penetration handling. Evaluations show that the generated references improve both interaction fidelity and policy learning: **TopoRetarget** achieves the best contact precision and alignment over all baselines on the ContactPose Dataset, improves Pen-Spin training success by 40.6 percentage points over the existing baseline methods, and enables zero-shot transfer to Wuji Hand hardware on cube reorientation and pen spinning. Project website: TopoRetarget. 

**Keywords:** motion retargeting, reinforcement learning, dexterous manipulation, trajectory optimization 

## **1 Introduction** 

Learning long-horizon, contact-rich dexterous manipulation with reinforcement learning often relies on carefully designed training pipelines [1, 2, 3]. Human hand-object demonstrations provide dense reference signals that guide reinforcement learning through tracking objectives [4, 5, 6, 7]. Using these demonstrations for robot policy learning requires retargeting human hand-object motion across a substantial embodiment gap, but matching hand pose alone is insufficient since task execution depends on local hand-object interaction. Therefore, preserving hand-object interaction during retargeting is a key bottleneck for learning dexterous manipulation skills from human demonstrations. 

Existing dexterous hand retargeting methods have made human hand motion useful for teleoperation and demonstration collection [8, 9, 10, 11]. Most of these pipelines define hand-centric objectives over hand pose [12], fingertip correspondences [8], and pinch relations [13]. Such objectives align the robot hand with the human hand, but do not directly specify where and how the robot should contact the object. Recent methods address this limitation by incorporating object motion [14, 6, 7], contact consistency [15, 16], or physical feasibility [17] into retargeting or policy learning. However, the resulting motions often still require downstream refinement, policy correction, or task-specific tuning before they can serve as reliable tracking references. 

This motivates **TopoRetarget** , a retargeting framework that focuses on the structure of the local hand-object interaction. It preserves object-relative positional and directional relationships between hand links and object regions, while also maintaining intra-hand relationships among hand links. Our approach reduces interaction artifacts and supports real-time retargeting. 

Our contributions are threefold: 

1. An interaction-preserving retargeting framework that maintains local hand-object interaction while enforcing dexterous hand kinematic and penetration constraints. 

2. A lightweight reference-based RL tracking pipeline that enables zero-shot sim-to-real transfer for contact-rich dexterous skills, including pen spinning and cube reorientation. 

3. A dexterous hand-object interaction dataset of retargeted trajectories, task references, and trained policies for reproducible reference-based dexterous manipulation. 

## **2 Related Work** 

### **2.1 Dexterous Hand Motion Retargeting** 

Dexterous hand motion retargeting maps human hand observations to robot hand motion for teleoperation and demonstration collection. DexPilot formulates vision-based dexterous hand-arm teleoperation around task-space hand objectives [8], and AnyTeleop extends vision-based hand-arm teleoperation across different robotic embodiments [9]. Later studies analyze how hand-pose, fingertip, keyvector, joint-limit, smoothness, and collision objectives affect retargeting quality [12], while GeoRT proposes an ultrafast geometric retargeting model for hand motion transfer [13]. These methods enable practical teleoperation and demonstration collection, but their objectives remain largely hand-centric. For contact-rich policy learning, references must preserve object-relative local interaction, including contacts on fingertips, intermediate phalanges, finger sides, and the palm. DexFlow incorporates hand-object interaction into hand pose retargeting [15], FunGrasp focuses on functional grasping for diverse dexterous hands [16], and GenHand studies generalized human grasp kinematic retargeting [18]. These methods improve grasp or contact transfer, but frequent contact-mode transitions still require references that preserve evolving hand-object relations. **TopoRetarget** treats 

2 

retargeting as interaction-preserving reference generation, maintaining local hand-object interaction while enforcing robot kinematics and penetration constraints. 

### **2.2 Reinforcement Learning for Dexterous Manipulation** 

Reinforcement learning for dexterous manipulation trains policies for high-dimensional contactrich skills through task-specific objectives, domain randomization, curriculum learning, and sim-toreal adaptation. OpenAI demonstrates cube reorientation with large-scale simulation and domain randomization [1]; DeXtreme transfers agile in-hand manipulation from simulation to real hardware [2]; RMA-based in-hand rotation adapts to object and dynamics variations through learned adaptation [19]; and recent pen-spinning systems still require carefully designed training pipelines or real-world trial-and-error search for dynamic multi-finger contact [3, 20]. To reduce this burden, reference-based learning turns long-horizon exploration into trajectory tracking. DeepMimic establishes this paradigm for physics-based character skills [21], and OmniH2O applies humanto-humanoid motion tracking to whole-body control [22]. Dexterous-hand systems have begun to adopt reference-guided policy learning: DexTrack trains neural tracking control from human references [4], Dexplore uses reference-scoped exploration [5], DexMachina studies functional retargeting for bimanual dexterous manipulation [6], and ManipTrans uses residual learning for dexterous bimanual transfer [7]. Reference-based learning depends directly on reference quality: policies must be able to follow the provided references. **TopoRetarget** targets this bottleneck by producing references that preserve task-relevant local interaction before RL training. 

### **2.3 Interaction-Preserving Data Generation** 

Interaction-preserving data generation turns human hand-object behavior into policy references that retain task-relevant spatial relationships. DexMV and Robotic Telekinesis recover motion from human videos [23, 10]; From One Hand to Multiple Hands uses single-camera teleoperation for multi-hand imitation [11]; DexCap provides portable MoCap collection [24]; DexMimicGen scales a small set of human demonstrations into large bimanual dexterous datasets [25]; and the ContactPose Dataset provides hand-object contact annotations [26]. These sources collect hand-object motion, but embodiment gaps can still produce contact misalignment, penetration, or infeasible robot poses. ObjDex guides policy learning with object goals and human wrist motion [14], SPIDER uses physics-based sampling and virtual contact guidance for feasible dexterous trajectories [17], and OmniRetarget preserves robot-object relationships through contact-aware mesh deformation [27]. **TopoRetarget** provides real-time retargeting with local contact fidelity using a fixed set of parameters across dexterous in-hand manipulation settings. 

## **3 TopoRetarget: Interaction-Preserving Hand-Object Retargeting** 

We propose **TopoRetarget** , an interaction-preserving retargeting framework for converting human hand-object demonstrations into robot references. The algorithm overview is shown in Fig. 2. We first define the notation and optimization variables in Sec. 3.1, then describe the relative bonedirection initialization in Sec. 3.2, the shared hand-object interaction mesh in Sec. 3.3, and the topology-aware Laplacian optimization in Sec. 3.4. 

### **3.1 Notation Definition** 

We formulate hand-object retargeting as a constrained optimization problem. The inputs are a human-hand trajectory _P_ 1:<sup>_h_</sup> _N_<sup>,anobjectposetrajectory</sup><sup>_q_</sup> 1:<sup>_o_</sup> _N_<sup>,andanobjectmesh</sup><sup>_M_.</sup> Here, _Pt_<sup>_h∈_R21</sup><sup>_×_3denotestheMediaPipe[28]handkeypointsattime</sup><sup>_t_,and</sup><sup>_N_denotesthetrajectory</sup> length. The goal is to compute an optimal robot base-pose trajectory _q_ 1:<sup>base</sup> _N_<sup>and a robot joint trajec-</sup> tory _q_ 1:<sup>_θ_</sup> _N_<sup>_∈_R</sup><sup>_N×nθ_.We write</sup><sup>_q_</sup> _t_<sup>_r_= (</sup><sup>_q_</sup> _t_<sup>base</sup> _, qt_<sup>_θ_) and use</sup><sup>_q_for</sup><sup>_q_</sup> _t_<sup>_r_in single-frame objectives.</sup> 

3 



Figure 2: **TopoRetarget** overview. Given a human demonstration, object mesh, and target hand model, the method aligns bone directions during initialization, constructs source and robot interaction meshes, and computes the robot configuration via topology-aware Laplacian optimization. The output robot motion reference preserves hand-object interaction. **3.2 Relative Bone-Direction Initialization** We first compute an initial guess for the robot-hand configuration by matching local finger articulation between the source and robot hands. For each non-terminal finger keypoint _k_ , define _dk_ as the unit vector from keypoint _k_ to its child keypoint along the same finger. Let _d_<sup>_s_</sup> _k_<sup>and</sup><sup>_dr_</sup> _k_<sup>(</sup><sup>_q_) denote</sup> the source and robot bone directions at frame _t_ , expressed in their respective wrist-centered hand frames, and let _AB_ contain adjacent bone pairs along each finger. The bone-direction mismatch is defined as 



The initial estimate for frame _t_ is 



The first term encourages the robot hand to reproduce the source hand’s relative bone directions, while the second term promotes temporal consistency with the previous initial estimate. The scalar weights _λ_ warm and _λ_ smooth balance these two objectives. We use _λ_ warm for the initialization-stage bone-direction weight. 

### **3.3 Interaction Mesh Construction** 

At each frame _t_ , we build source and robot hand-object vertex sets from the human keypoints _Pt_<sup>_h_,</sup> the corresponding robot keypoints _Pt_<sup>_r_(</sup><sup>_q_), and</sup><sup>_No_object surface samples</sup><sup>_Ot_drawn from the mesh</sup> _M_ posed by _qt_<sup>_o_:</sup> 



Here, _Nv_ = 21 + _No_ is the total number of graph vertices. We write _Vt_<sup>_s_=</sup><sup>_{v_</sup> _i,t_<sup>_s}_</sup> _i_<sup>_N_</sup> =1<sup>_v_and</sup><sup>_V_</sup> _t_<sup>_r_(</sup><sup>_q_)=</sup> _{vi,t_<sup>_r_(</sup><sup>_q_)</sup><sup>_}_</sup> _i_<sup>_N_</sup> =1<sup>_v_,wherethefirst21verticesarehandkeypointsandtheremainingverticesareobject</sup> samples. We run Delaunay tetrahedralization on the source vertices _Vt_<sup>_s_toobtaintheinteraction</sup> edge set _It_ , then reuse the same connectivity for the robot vertices: 



This shared graph lets the refinement compare the demonstrated and retargeted configurations under the same local hand-object neighborhood structure. It also supports augmentation across object scales and hand embodiments: after scaling or replacing the object, _Ot_ follows the new surface, and the rebuilt graph lets the same Laplacian refinement preserve local interaction without new contact targets. 

4 

### **3.4 Topology-Aware Laplacian Optimization** 

Starting from _q_ ˜ _t_<sup>_r_,werefinetherobotconfigurationbymatchingtopology-awareLaplaciancoor-</sup> dinates on the shared interaction graph. Let _Nt_ ( _i_ ) be the neighbors of vertex _i_ in _It_ . For each interaction edge ( _i, j_ ) _∈It_ , we compute source-frame distance-aware weights 



Here, _κ_ is a spatial decay parameter. The weights are computed on the source configuration and reused for the robot configuration. For a vertex set _V_ = _{vi}_<sup>_N_</sup> _i_ =1<sup>_v_, its weighted Laplacian coordinate</sup> at vertex _i_ is 



We define the interaction-mesh energy as 



The final interaction-preserving optimization is 



Here, the _λ_ terms are scalar weights, _E_ IM maintains the demonstration’s local hand-object interaction, _E_ bone keeps the initialization bone-direction prior, and _E_ reg regularizes smoothness. _λ_ bone denotes the refinement-stage bone-direction prior weight. The implementation of _E_ reg and the fixed parameter values are given in Appendix A.1. We use one fixed parameter setting across our experiments rather than performing extensive per-case tuning; detailed parameter values are provided in Table 3. The query set _Qt_ contains hand-object pairs checked at frame _t_ ; for pair _i_ , _ϕi_ ( _q_ ) is the signed distance, _si_ is the slack variable, _τ_ is the soft tolerance, _b_ is the hard bound, and _ws_ is the slack penalty weight. 

## **4 Minimal RL Tracking Controller** 

We use a minimal reinforcement-learning setup to track the retargeted trajectories. We formulate the hand-object tracking task as a finite-horizon Markov decision process (MDP) and optimize the policy with Proximal Policy Optimization (PPO) [29]. Each reference clip is _ξ_<sup>ref</sup> = _{qk_<sup>_θ,_ref</sup> _, qk_<sup>_o,_ref</sup> _, p_<sup>ref</sup> 1: _L,k_<sup>_}_</sup> _k_<sup>_N_</sup> =0<sup>_−_1,where</sup><sup>_q_</sup> _k_<sup>_θ,_ref</sup> denotes the joint component _qk_<sup>_θ,∗_</sup> of the retargeted configuration _qk_<sup>_r,∗_,</sup><sup>_q_</sup> _k_<sup>_o,_ref</sup> denotes the object pose expressed in the robot base frame, and _p_<sup>ref</sup> 1: _L,k_<sup>denotes</sup> the base-frame positions of the _L_ tracked hand links. Expressing object and link references in the base frame makes the controller focus on relative hand-object interaction rather than global motion. **Action space.** At each control step _t_ , the policy tracks the active reference frame _kt_ using a residual action, _qt_<sup>_θ,_tar</sup> = _qk_<sup>_θ,_</sup> _t_<sup>ref</sup> + _at_ . 

**Observation.** The observation is _ot_ = [ _o_<sup>prop</sup> _t , o_<sup>obj</sup> _t , o_<sup>ref</sup> _t_<sup>],where</sup><sup>_o_</sup> _t_<sup>prop</sup> contains the joint state and previous action, _o_<sup>obj</sup> _t_ contains object-axis points, and _o_<sup>ref</sup> _t_ contains lookahead joint, object, and handlink references in the robot base frame. 

**Reference initialization and sampling.** We use reference-state initialization: at reset, a start frame _k_ 0 is sampled uniformly from the reference trajectory, and each environment is initialized with the corresponding hand and object states. 

**Reward.** The reward is _rt_ = _w_ obj _r_ obj + _w_ link _r_ link + _w_ joint _r_ joint + _w_ smooth _r_ smooth, where the four terms track object pose, hand-link positions, finger joints, and smoothness, respectively; the weights are listed in Appendix A.5. 

5 

**Domain randomization.** During training, we randomize object mass and center of mass, contact parameters, actuator gains, joint damping, and hand-link inertial properties, and apply external object perturbations during rollout. 

## **5 Experiments** 

Our experiments evaluate the proposed retargeting pipeline through three questions: 

1. Does **TopoRetarget** preserve local hand-object interactions across diverse human motions? 

2. How do retargeted references from different methods affect downstream RL tracking policy training and performance? 

3. Does **TopoRetarget** support generalization and augmentation across different objects and robot hands without per-case retuning? 

Across the retargeting and downstream tracking experiments, we compare the proposed method with four baselines: OmniRetarget [27] (see details at Appendix A.2), Mink [30], DexPilot [8], and GeoRT [13]. All applicable methods use the same human references and object geometry. 

### **5.1 Interaction-Preserving Retargeting Quality** 

To answer Q1, we compare different retargeting algorithms in terms of their ability to preserve local contact information in hand-object interaction. We treat source in-contact bone segments as the key interaction units and evaluate preservation of object-relative positions and directions after retargeting. We report two metrics on the ContactPose Dataset [26]: _E_ prec, the mean object-relative position displacement of contact links, and _E_ align, the mean object-relative orientation error of contact links. Lower values indicate better interaction preservation. Full definitions are given in Appendix A.3. 

Table 1 shows that **TopoRetarget** achieves the lowest contact precision and contact alignment errors, with 7.71 mm and 15.67<sup>_◦_</sup> , respectively. The residual is attributable to the human-dexterous embodiment gap and source-side ContactPose interpenetration. **TopoRetarget** also keeps penetration small, with a maximum penetration of 1.07 mm, and avoids the severe interpenetration observed in several baselines, indicating that the method better preserves local contact geometry. Moreover, the average solve time is below 5 ms per frame, enabling real-time retargeting. 

Table 1: Quantitative retargeting evaluation on the ContactPose Dataset [26] 

|**Metric**|**TopoRetarget**(Ours)|OmniRetarget|Mink|DexPilot|GeoRT|
|---|---|---|---|---|---|
|Contact precision (mm)_↓_|**7.71**|14.15|14.12|14.13|26.77|
|Contact alignment (<sup>_◦_</sup>)_↓_|**15.67**|30.80|37.36|33.71|25.74|
|Max hand-object penetration (mm)_↓_|**1.07**|1.15|20.12|11.87|22.22|
|% frames with penetration_>_2 mm_↓_|**0.00**|**0.00**|84.00|88.00|96.00|
|Solve time (ms / frame)_↓_|4.70|40.96|4.37|1.74|**1.17**|



Fig. 3 summarizes common retargeting failure modes, including contact-region drift, invalid grasps or penetration, misplaced non-tip contacts, and unnatural joint configurations. In contrast, **TopoRetarget** preserves the hand-object interaction of the source while reducing artifacts. Detailed examples are shown in the figure. 

### **5.2 Downstream Tracking Policy Performance** 

To answer Q2, we use downstream RL tracking policy training as a practical test of trajectory quality. For each retargeting method, we generate references on the Ho-cap [31] and our self-collected MoCap Pen-Spin Dataset (see details in Appendix A.4). We then train RL tracking policies with the setup described in Sec. 4, using identical policy architecture, reward terms, domain randomization, and termination criteria. We evaluate the trained policies in simulation and report success rate and object tracking error. A rollout is counted as successful if it reaches the final reference frame without triggering the object-pose termination criteria in Appendix A.5. 

6 



Figure 3: Retargeting artifacts of existing methods under hand-object and hand-only cases. 

Table 2: Downstream RL tracking performance 

|Metric<br>**TopoRetarget**(Ours)|OmniRetarget|Mink|DexPilot|GeoRT|
|---|---|---|---|---|
|_Ho-cap [31] Dataset (32 clips)_|||||
|Success rate_↑_<br>**84.4% (27/32)**|56.2% (18/32)|75.0% (24/32)|75.0% (24/32)|75.0% (24/32)|
|Obj. pos err (cm)_↓_<br>**0.87**|1.07|0.91|0.92|0.90|
|Obj. rot err (deg)_↓_<br>5.76|7.87|5.55|**4.99**|6.07|
|_MoCap Pen-Spin Dataset (32 clips)_|||||
|Success rate_↑_<br>**87.5% (28/32)**|46.9% (15/32)|21.9% (7/32)|40.6% (13/32)|31.2% (10/32)|
|Obj. pos err (cm)_↓_<br>**0.98**|1.45|1.61|1.29|1.19|
|Obj. rot err (deg)_↓_<br>**9.25**|14.26|15.25|17.66|18.62|





Figure 4: Interaction-mesh visualizations of retargeted reference trajectories (A,C) and corresponding zero-shot real-world executions (B,D) for cube reorientation and pen spinning on the Wuji Hand. 

7 

As shown in Table 2, **TopoRetarget** achieves the highest success rate at 84.4% and the lowest position error at 0.87 cm on the Ho-cap Dataset, while rotation errors remain comparable across methods because the trajectories are primarily grasp-centric. On the MoCap Pen-Spin Dataset, rapid motion and frequent non-tip contact transitions demand high-quality reference motion; **TopoRetarget** reaches 87.5% success, over 40 percentage points above all baselines, with the lowest position and rotation errors. The widened performance gap on pen spinning highlights the applicability of **TopoRetarget** to contact-rich manipulation, where the active hand-object contact changes frequently over time. Fig. 4 further shows zero-shot Wuji Hand sim-to-real transfer on cube reorientation and pen spinning, demonstrating that learned tracking policies can execute contact-rich skills with repeated in-hand contact changes. 

### **5.3 Generalization and Augmentation without Per-Case Retuning** 

To answer Q3 on generalization and augmentation without per-case retuning, we retarget the same human demonstrations to different dexterous hand embodiments and object scales while keeping all retargeting parameters fixed. Fig. 5 shows that the proposed approach transfers both the hand motion and the hand-object interaction under the embodiment and scale changes. The interactionmesh formulation supports this transfer by rebuilding the local hand-object graph with edge weights recomputed from the scaled object mesh, providing a simple way to augment human demonstrations. 



Figure 5: Augmentation across object scales and dexterous hand embodiments without per-case retuning. 

## **6 Conclusion** 

We presented **TopoRetarget** , a fixed-parameter retargeting framework that converts human handobject demonstrations into dexterous robot references. **TopoRetarget** maintains hand-object interaction in the object frame through distance-weighted Laplacian optimization, directional consistency, kinematic constraints, and penetration handling. This design improves reference-level retargeting quality, achieving better contact precision, contact alignment, and penetration metrics than representative baselines on the ContactPose Dataset. The improved references also lead to stronger downstream RL tracking, with higher success rates and lower object tracking errors, especially on agile pen-spinning demonstrations with frequent non-tip contact transitions. The same formulation supports augmentation across object scales and hand embodiments without task-specific tuning. 

## **7 Limitations and Future Work** 

**TopoRetarget** depends on the quality of the upstream human reference motion. Our method can handle contact distortion caused by penetration in the source motion, but it is less effective for virtual contacts, where the source finger is intended to interact with the object but does not actually touch the object surface. Future work can incorporate source-motion preprocessing to correct such missing-contact cases before retargeting. 

8 

### **Acknowledgments** 

We would like to thank Fan Yang, Chaoyi Pan, Cunxi Dai, and Xiaofeng Guo for valuable discussions and helpful feedback on the paper. We are also grateful to Tongbin Liu and Wenkai Nie for their support in preparing the experimental setup. 

9 

## **References** 

- [1] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 39(1):3–20, 2020. 

- [2] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko, R. Singh, J. Liu, D. Makoviichuk, K. Van Wyk, A. Zhurkevich, B. Sundaralingam, et al. Dextreme: Transfer of agile in-hand manipulation from simulation to reality. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 5977–5984. IEEE, 2023. 

- [3] J. Wang, Y. Yuan, H. Che, H. Qi, Y. Ma, J. Malik, and X. Wang. Lessons from learning to spin” pens”. _arXiv preprint arXiv:2407.18902_ , 2024. 

- [4] X. Liu, J. Adalibieke, Q. Han, Y. Qin, and L. Yi. Dextrack: Towards generalizable neural tracking control for dexterous manipulation from human references. _arXiv preprint arXiv:2502.09614_ , 2025. 

- [5] S. Xu, Y.-W. Chao, L. Bian, A. Mousavian, Y.-X. Wang, L. Gui, and W. Yang. Dexplore: Scalable neural control for dexterous manipulation from reference scoped exploration. In _Conference on Robot Learning_ , pages 2184–2199. PMLR, 2025. 

- [6] Z. Mandi, Y. Hou, D. Fox, Y. Narang, A. Mandlekar, and S. Song. Dexmachina: Functional retargeting for bimanual dexterous manipulation. _arXiv preprint arXiv:2505.24853_ , 2025. 

- [7] K. Li, P. Li, T. Liu, Y. Li, and S. Huang. Maniptrans: Efficient dexterous bimanual manipulation transfer via residual learning. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 6991–7003, 2025. 

- [8] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox. Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 9164–9170. IEEE, 2020. 

- [9] Y. Qin, W. Yang, B. Huang, K. Van Wyk, H. Su, X. Wang, Y.-W. Chao, and D. Fox. Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system. _arXiv preprint arXiv:2307.04577_ , 2023. 

- [10] A. Sivakumar, K. Shaw, and D. Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube. _arXiv preprint arXiv:2202.10448_ , 2022. 

- [11] Y. Qin, H. Su, and X. Wang. From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation. _IEEE Robotics and Automation Letters_ , 7(4): 10873–10881, 2022. 

- [12] C. Xin, M. Yu, Y. Jiang, Z. Zhang, and X. Li. Analyzing key objectives in human-to-robot retargeting for dexterous manipulation. _IEEE Robotics and Automation Practice_ , 2026. 

- [13] Z.-H. Yin, C. Wang, L. Pineda, K. Bodduluri, T. Wu, P. Abbeel, and M. Mukadam. Geometric retargeting: A principled, ultrafast neural hand retargeting algorithm. In _2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 17376–17382. IEEE, 2025. 

- [14] Y. Chen, C. Wang, Y. Yang, and C. K. Liu. Object-centric dexterous manipulation from human motion data. _arXiv preprint arXiv:2411.04005_ , 2024. 

- [15] X. Lin, K. Yao, L. Xu, X. Wang, X. Li, Y. Wang, and M. Li. Dexflow: A unified approach for dexterous hand pose retargeting and interaction. _arXiv preprint arXiv:2505.01083_ , 2025. 

10 

- [16] L. Huang, H. Zhang, Z. Wu, S. Christen, and J. Song. Fungrasp: Functional grasping for diverse dexterous hands. _IEEE Robotics and Automation Letters_ , 2025. 

- [17] C. Pan, C. Wang, H. Qi, Z. Liu, H. Bharadhwaj, A. Sharma, T. Wu, G. Shi, J. Malik, and F. Hogan. Spider: Scalable physics-informed dexterous retargeting. _arXiv preprint arXiv:2511.09484_ , 2025. 

- [18] L. Qi, O. Popoola, M. A. Imran, and W. Ahmad. Genhand: generalised human grasp kinematic retargeting. _npj Robotics_ , 4(1):19, 2026. 

- [19] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik. In-hand object rotation via rapid motor adaptation. In _Conference on Robot Learning_ , pages 1722–1732. PMLR, 2023. 

- [20] Y. Yao, U. Yoo, J. Oh, C. G. Atkeson, and J. Ichnowski. Soft robotic dynamic in-hand pen spinning. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , 2025. 

- [21] X. B. Peng, P. Abbeel, S. Levine, and M. Van de Panne. Deepmimic: Example-guided deep reinforcement learning of physics-based character skills. _ACM Transactions On Graphics (TOG)_ , 37(4):1–14, 2018. 

- [22] T. He, Z. Luo, X. He, W. Xiao, C. Zhang, W. Zhang, K. Kitani, C. Liu, and G. Shi. Omnih2o: Universal and dexterous human-to-humanoid whole-body teleoperation and learning. _arXiv preprint arXiv:2406.08858_ , 2024. 

- [23] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision_ , pages 570–587. Springer, 2022. 

- [24] C. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and C. K. Liu. Dexcap: Scalable and portable mocap data collection system for dexterous manipulation. _arXiv preprint arXiv:2403.07788_ , 2024. 

- [25] Z. Jiang, Y. Xie, K. Lin, Z. Xu, W. Wan, A. Mandlekar, L. Fan, and Y. Zhu. Dexmimicgen: Automated data generation for bimanual dexterous manipulation via imitation learning. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , 2025. 

- [26] S. Brahmbhatt, C. Tang, C. D. Twigg, C. C. Kemp, and J. Hays. Contactpose: A dataset of grasps with object contact and hand pose. In _European Conference on Computer Vision_ , pages 361–378. Springer, 2020. 

- [27] L. Yang, X. Huang, Z. Wu, A. Kanazawa, P. Abbeel, C. Sferrazza, C. K. Liu, R. Duan, and G. Shi. Omniretarget: Interaction-preserving data generation for humanoid whole-body locomanipulation and scene interaction. _arXiv preprint arXiv:2509.26633_ , 2025. 

- [28] C. Lugaresi, J. Tang, H. Nash, C. McClanahan, E. Uboweja, M. Hays, F. Zhang, C.-L. Chang, M. G. Yong, J. Lee, et al. Mediapipe: A framework for building perception pipelines. _arXiv preprint arXiv:1906.08172_ , 2019. 

- [29] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 

- [30] K. Zakka. Mink: Python inverse kinematics based on MuJoCo, Feb. 2026. URL `https: //github.com/kevinzakka/mink` . 

- [31] J. Wang, Q. Zhang, Y.-W. Chao, B. Wen, X. Guo, and Y. Xiang. Ho-cap: A capture system and dataset for 3d reconstruction and pose tracking of hand-object interaction. _Advances in Neural Information Processing Systems_ , 38, 2026. 

11 

## **A Appendix** 

### **A.1 Retargeting Details** 

**Implementation detail for** _E_ reg. In the implementation, the regularization term in the final refinement is expanded as 



The first term enforces temporal smoothness in the optimizer coordinates, while the last two terms are a lightweight base-pose prior for floating-base retargeting. Here, _q_ pos<sup>baseand</sup><sup>_q_</sup> rot<sup>base</sup> denote the translational and rotational components of the robot base pose _q_<sup>base</sup> , respectively. 

Table 3: Selected retargeting parameter settings. 

|**Parameter**|**Value**|**Description**|
|---|---|---|
|_No_|50|Number of object surface samples in the interaction mesh.|
|_λ_IM|500|Weight of the interaction-mesh Laplacian objective.|
|_κ_|30|Distance-decay factor for the exponential Laplacian edge weights.|
|_λ_warm|1|Bone-direction weight in the initialization stage.|
|_λ_bone|0_._1|Bone-direction prior weight in the final refinement stage.|
|_λ_smooth|2_._5|Temporal smoothness weight in the initialization stage.|
|_λ_reg|2_._5|Temporal smoothness weight inside_E_reg.|
|_λ_base_,_pos|100|Floating-base translation prior weight used in_E_reg.|
|_λ_base_,_rot|1|Floating-base rotation prior weight used in_E_reg.|
|_τ_|0_._001 m|Soft penetration tolerance.|
|_b_|0_._030 m<br>|Hard penetration backstop.|
|_ws_|1_._0_×_10<sup>5</sup>|Slack penalty weight for the penetration constraint.|



### **A.2 OmniRetarget Baseline** 

OmniRetarget [27] is originally designed for humanoid whole-body loco-manipulation and scene interaction. For our dexterous hand-object baseline, we keep its interaction-mesh objective and object surface sampling, but replace the humanoid source keypoints with MediaPipe hand keypoints: 



where _Pt_<sup>mp</sup> _∈_ R<sup>21</sup><sup>_×_3</sup> denotes the source MediaPipe hand keypoints and _Ot_<sup>_s, O_</sup> _t_<sup>_r_arethesampled</sup> object points under the source and retargeted object poses. 

We make two hand-specific changes. First, the wrist is not fixed as a root anchor; it is included in _Pt_<sup>_r_(</sup><sup>_q_) and optimized jointly with the other hand joints.Second, collision handling is applied to the</sup> full hand geometry rather than to a sparse humanoid contact set, since dexterous manipulation may contact the object with fingertips, intermediate phalanges, finger sides, or the palm. 

### **A.3 Retargeting Metrics** 

Let _C_ denote the in-contact hand links, where each link _c_ associates a source hand point _h_<sup>_s_</sup> _c_<sup>,a</sup> retargeted robot point _h_<sup>_r_</sup> _c_<sup>,thecorrespondingsourceandretargetedobjectpoints</sup><sup>_os_</sup> _c_<sup>and</sup><sup>_or_</sup> _c_<sup>,anda</sup> parent joint with source and retarget positions _h_<sup>_s_</sup> pa( _c_ )<sup>and</sup><sup>_hr_</sup> pa( _c_ )<sup>(thewristfortheproximallink).</sup> The set _C_ is obtained directly from the ContactPose contact annotations using ContactPose’s own attribution: per-vertex contact intensity is sigmoid-normalized and thresholded, each contact vertex is assigned to its nearest of the 20 hand bones by point-to-segment distance, and a link is marked in contact when at least 10 vertices fall on it. Contact precision measures the object-relative position error: 



12 

Contact alignment measures the angular deviation between the source and retargeted bone-segment orientations of the in-contact links: 



For penetration, let _Xt_<sup>_r_besampledrobot-handsurfacepointsandlet</sup><sup>_Mt_denotetheposedobject</sup> mesh with signed distance _dMt_ ( _x_ ), positive outside the object. We report the maximum penetration depth and the fraction of frames whose maximum penetration exceeds _δ_ = 2 mm: 



### **A.4 Experimental Setup** 

**Datasets and Tasks.** For reference motion retargeting evaluation, we use the ContactPose Dataset [26] to measure hand-object contact precision, contact alignment, and penetration. We evaluate on 25 of the 28 ContactPose grasps, excluding three with deeply concave object geometry (mug, scissors, Utah teapot) that no method reliably handles. For downstream tracking evaluation, we use two trajectory sets. Ho-cap [31] provides 32 grasp-centric hand-object references that test whether retargeted motions remain trackable under relatively stable contact conditions. The 32 trajectories are randomly drawn from Ho-cap’s single-hand interactions to fit our training budget. Our self-collected MoCap Pen-Spin Dataset contains 32 pen-spinning demonstrations recorded with motion capture and the Wuji Glove, with trajectories averaging 12.4 s and containing frequent non-tip contacts and contact-mode transitions. For both datasets, all retargeting methods are evaluated on the same human references and object geometry, and each generated reference set is used to train a separate policy under the identical RL setup. We further deploy the trained policies on the Wuji Hand for cube reorientation and pen spinning. 

**Baselines and Metrics.** We compare **TopoRetarget** with OmniRetarget [27], Mink [30], DexPilot [8], and GeoRT [13] under the same human references and object geometry when applicable. Reference-level metrics include contact precision, contact alignment, maximum penetration, penetration rate, and solve time; full definitions are provided in Appendix A.3. Policy metrics include success rate and object pose tracking error. 

### **A.5 RL Training** 

We formulate single-hand object manipulation as a finite-horizon MDP. The goal is to track a reference manipulation clip with a right dexterous hand while keeping the manipulated object aligned with the demonstrated motion. A reference clip is a sequence 



where _qk_<sup>_θ,_ref</sup> denotes the reference finger joint positions, _qk_<sup>_o,_ref</sup> _∈_ SE(3) denotes the object pose expressed in the base frame, and _p_<sup>ref</sup> 1: _L,k_<sup>denotesthereferencepositionsofthetrackedhandlinks.</sup> We use the base frame for reference quantities so that the policy learns the relative hand-object interaction instead of a global trajectory. 

### **A.5.1 State and action** 

The simulator state contains the hand joint state, actuator state, contact state, and object pose and velocity. The policy does not observe the full state. At each control step _t_ , the active reference index 

13 

is _kt_ . The action _at_ is a residual joint-position command for the _nθ_ right-hand finger joints. The low-level target is centered at the current reference pose, 



This residual parameterization lets the policy correct tracking errors while using the demonstration as a strong prior. 

### **A.5.2 Observation** 

The policy observation has three parts. First, proprioception includes the current finger joint positions, joint velocities, and the previous action. Second, the object observation represents the current object pose in the base frame with a small set of axis points attached to the object. This avoids direct dependence on a particular quaternion parameterization while still encoding position and orientation. Third, the reference observation contains the current reference joint pose, object axis points, and tracked hand-link positions, plus short lookahead reference features from future frames. In our implementation we use lookahead offsets of 1, 3, and 5 control steps. During training we add small noise to proprioception and the observed object pose to improve robustness. 

### **A.5.3 Reference initialization and sampling** 

We use reference initialization at every reset. A start frame _k_ 0 is sampled uniformly from the reference trajectory, and the simulator is reset to the corresponding reference hand pose and object pose. The reference index then advances with the simulator control steps, _kt_ +1 = _kt_ + 1. Uniform sampling over the trajectory exposes the policy to all phases of the manipulation and avoids overfitting to the beginning of the clip. We optionally apply small reset noise to the object pose around the sampled reference state. 

### **A.5.4 Reward** 

The reward is dominated by tracking terms for the object, hand links, and joints. For an error _e_ and scale _σ_ , we use a Gaussian tracking kernel 



The object term tracks a set of axis points attached to the object, which jointly encode its base-frame position and orientation, 



where _um,t_ and _u_<sup>ref</sup> _m,kt_<sup>are current and reference object axis points in the base frame.The hand-link</sup> term tracks the positions of the palm and finger links, 



and the joint term tracks the normalized finger joint error, 



The total reward is a weighted sum: 

_rt_ = _w_ obj _r_ obj + _w_ link _r_ link + _w_ joint _r_ joint + _w_ smooth _r_ smooth _,_ 

where _r_ smooth = _∥at − at−_ 1 _∥_<sup>2</sup> 2<sup>+</sup><sup>_∥at−_2</sup><sup>_at−_1+</sup><sup>_at−_2</sup><sup>_∥_</sup> 2<sup>2.In practice, the largest weight is assigned</sup> to object tracking, followed by link, joint, and smoothness terms. 

The reward weights and scales, together with the termination conditions, are summarized in Table 4. 

14 

Table 4: Reference-tracking MDP. We define _ψ_ ( _e_ ; _σ_ ) = exp( _−∥e/σ∥_<sup>2</sup> ). 

|**Term**|**Expression / specification**|**Weight**|
|---|---|---|
|Object|_ψ_( <sup>1</sup><br>6<br>�6<br>_m_=1 <sup>_∥um −u_ref</sup><br>_m _<sup>_∥_</sup>2<sup>; 0</sup><sup>_._04)</sup><br><br><br>|8.0|
|Link position|1<br>_L_<br>�_L_<br>_ℓ_=1 <sup>_ψ_(</sup><sup>_∥pℓ−p_ref</sup><br>_ℓ_<sup>_∥_2; 0</sup><sup>_._025)</sup><br><br><br><br>|1.0|
|Joint position|1<br>_nθ_<br>�_nθ_<br>_j_=1 <sup>_ψ_(</sup><sup>_|qθ_</sup><br>_j _<sup>_−qθ,_ref</sup><br>_j_<br>_|/_(_q_<sup>max</sup><br>_j_<br>_−q_<sup>min</sup><br>_j_<br>); 0_._1)<br><br>|1.0|
|Action smoothness|_∥at −at−_1_∥_<sup>2</sup><br>2 <sup>+</sup><sup>_∥a_</sup>_t _<sup>_−_2</sup><sup>_a_</sup>_t−_1 <sup>+</sup><sup>_a_</sup>_t−_2<sup>_∥_2</sup><br>2|-0.01|
|Timeout|Episode reaches 20 s|–|
|Object unstable|Height_<_0_._06m, linear velocity_>_10m/s, or angular velocity_>_500rad/s<br>|–|
|Object position error|_∥po −p_<sup>ref</sup><br>_o _<sup>_∥_</sup>2 <sup>_>_ 0</sup><sup>_._05 m</sup>|–|
|Object orientation error|Orientation error_>_45<sup>_◦_</sup>|–|
|Object axis-point error|Any of the 6 object axis-point errors_>_0_._05m|–|



### **A.5.5 Domain randomization** 

To reduce overfitting to a single simulator instance, training randomizes object mass and center of mass, contact friction, actuator gains, joint damping and armature, encoder bias, and hand link inertial properties. We also apply intermittent external force and torque disturbances to the object. These perturbations are sampled at reset or during rollout and are not included in the policy observation. 

The full randomization ranges are listed in Table 5. 

Table 5: Domain randomization ranges used during tracking-policy training. 

|**Randomized quantity**|**Range / setting**|**Mode**|
|---|---|---|
|Joint-position observation noise|_N_(0_,_0_._02)rad<br>|Step obs.|
|Joint-velocity observation noise|_N_(0_,_0_._05)rad/s|Step obs.|
|Object axis-point position noise|_N_(0_,_0_._002)m|Step obs.|
|Object axis-point orientation noise|_N_(0_,_0_._01)rad|Step obs.|
|Observation delay|0–2 control steps|Step obs.|
|Reference reset: finger joints|_U_[_−_0_._02_,_0_._02]rad|Reset|
|Reference reset: object position|_U_[_−_0_._005_,_0_._005]m|Reset|
|Reference reset: object orientation|Axis-angle perturbation, angle_U_[_−_0_._03_,_0_._03]rad|Reset|
|Object COM offset|[_−_0_._003_,_0_._003]m|Startup|
|Robot friction scale|[0_._7_,_1_._3]|Startup|
|Robot collision-geometry scale|[0_._9_,_1_._1]|Startup|
|Object mass / inertia scale|[0_._4_,_1_._6]|Startup|
|PD stiffness scale|[0_._75_,_1_._5], log-uniform|Startup|
|PD damping scale|[0_._5_,_2_._0], log-uniform|Startup|
|Joint damping scale|[0_._3_,_3_._0], log-uniform|Startup|
|Joint armature scale|[0_._75_,_1_._3]|Startup|
|Joint friction-loss scale|[0_._5_,_2_._0]|Startup|
|Encoder bias|[_−_0_._01_,_0_._01]rad|Startup|
|Robot link inertia scale|[0_._4_,_1_._5]|Startup|
|Robot link mass scale|[0_._4_,_1_._5]|Startup|
|External object force disturbance|_U_[_−_0_._25_,_0_._25]N, single-step impulse every0_._6–1_._8s|Rollout|
|External object torque disturbance|_U_[_−_0_._00375_,_0_._00375]N m|Rollout|



### **A.5.6 Policy network and optimization** 

The policy and value networks and the PPO optimizer use the settings in Table 6. 

15 

Table 6: PPO training and network hyperparameters. 

|**Parameter**|**Value**|
|---|---|
|Parallel environments|4096|
|Simulation step|0.01 s|
|Decimation|5|
|RL control frequency|20 Hz|
|Reference trajectory frequency|20 Hz|
|Episode length|20 s (400 control steps)|
|Rollout length|40 control steps / environment|
|Samples per PPO iteration|163,840|
|Actor network|MLP [512, 256, 128], ELU|
|Critic network|MLP [512, 512, 256, 128], ELU|
|Observation normalization|Enabled|
|Action distribution|Softplus Gaussian|
|Optimizer|Adam<br>|
|Learning rate|1_×_10<sup>_−_4</sup>|
|PPO epochs / minibatches|4 / 32|
|Entropy coefficient|0.001|
|Discount_γ_|0.99|
|GAE_λ_|0.95|



16 

