# **BiDexGrasp: Coordinated Bimanual Dexterous Grasps across Object Geometries and Sizes** 

**Mu Lin**<sup>1</sup><sup>_,_3</sup><sup>_,∗_</sup> **, Yi-Lin Wei**<sup>1</sup><sup>_,∗_</sup> **, Jiaxuan Chen**<sup>**1**</sup> **, Yuhao Lin**<sup>**1**</sup> **, Shuoyu Chen**<sup>**1**</sup> **, Zhizhao Liang**<sup>**1**</sup> **, Jiangran Lyu**<sup>**2**</sup> **, Jiayi Chen**<sup>2</sup> , **Xiaoyi Fan**<sup>5</sup> , **Chengyi Xing**<sup>4</sup> , **Yansong Tang**<sup>3</sup> , **He Wang**<sup>2</sup> , **Wei-Shi Zheng**<sup>1</sup><sup>_,†_</sup> 1 Sun Yat-sen University 2 Peking University 3 Tsinghua University 

> 4 Stanford University 5 Jiangxing Intelligence (Guizhou) Technology Inc. https://frenkielm.github.io/BiDexGrasp.github.io/ 



<!-- Start of picture text -->
(a) Simulation Dataset<br>(b) IK Configuration<br>(c) Real-World Deployment<br><!-- End of picture text -->

Figure 1: Overview of BiDexGrasp. We construct a large-scale, high-quality dataset of coordinated bimanual dexterous grasps with diverse object geometries and sizes, along with feasible IK configurations in tabletop setting. Based on this dataset, we propose a novel data-driven learning-based framework to generate physically feasible dexterous grasps on unseen objects in the real world. 

**Abstract:** Bimanual dexterous grasping is a fundamental and promising area in robotics, yet its progress is constrained by the lack of comprehensive datasets and powerful generation models. In this work, we propose BiDexGrasp, consisting of a large-scale bimanual dexterous grasp dataset and a novel learning-based framework. For dataset construction, we propose a novel bimanual grasp synthesis pipeline to efficiently annotate physically feasible data. This pipeline addresses the challenges of high-dimensional bimanual grasping through a two-stage synthesis strategy of efficient region-based grasp initialization and decoupled force-closure grasp optimization. Powered by this pipeline, we construct a large-scale bimanual dexterous grasp dataset, comprising 6351 diverse objects with sizes ranging from 30 to 80 cm, along with 9.53 million annotated grasp data. Based on this dataset, we further introduce a novel learning-based dexterous grasping generation framework. The framework lies in two key designs: a bimanual coordination module and a geometry-size-adaptive grasp generation strategy to generate coordinated and high-quality grasps on unseen objects. Extensive experiments conducted in both simulation and real world demonstrate the superior performance of our proposed data synthesis pipeline and learned generative framework. 

## **1 Introduction** 

Robotic dexterous grasping enables human-like object interaction [1, 2, 3, 4, 5, 6, 7, 8]. Data-driven approaches achieve promising results, showing demands for high-quality datasets and advanced generative models [9, 10, 11, 12, 13]. Most prior studies concentrate on single-hand grasping [14, 15, 16, 17, 18]. However, diverse object shapes and sizes restrict single-hand manipulation, making bimanual dexterous grasping indispensable. 

Currently, several recent studies explore data synthesis and data-driven methods for bimanual dexterous grasping [19, 20] but still restricted to objects of limited size and geometry. We attribute this to the dual challenges of varied object sizes and the enlarged bimanual search space, which jointly degrade synthesis efficiency and grasp quality. To address this, we introduce BiDexGrasp in this work, which contributes a large-scale, high-quality bimanual grasp dataset produced by a novel synthesis pipeline, together with a bimanual-coordinated, geometry- and size-adaptive generation framework that learns from this dataset to produce high-quality grasps on diverse unseen objects. 

For dataset construction, we propose an effective bimanual dexterous grasp synthesis pipeline to address the increased complexity and low efficiency caused by the expanded action space. For efficiency, we introduce a bimanual region-constrained grasp initialization strategy to generates coordinated and physically feasible candidates. For quality, we propose a decoupled force-closure grasp optimization strategy that separates the force-closure constraints of each hand, reducing optimization complexity while preserving high-quality per-hand grasps. With this pipeline, we build a large dataset of 9.53M grasps over 6,351 objects spanning diverse geometries and scales (Tab. 1). 

Built on this dataset, we propose the **BiDexGrasp** framework for high-quality grasp generation on diverse unseen objects, tackling two challenges: bimanual coordination and generalization across geometries and scales. To enhance coordination, we introduce a bimanual coordination module to predict coordinated grasp views, to guide the grasp poses generation. To enhance adaptability, we propose a geometry-size-adaptive grasp strategy that compactifies the action space and emphasizes local structural learning, greatly improving robustness to diverse object geometries and scales. 

Extensive simulation and real-world experiments validate both the synthesis pipeline and the generation framework. Our pipeline achieves over 2.8 _×_ higher success rate and 30 _×_ faster synthesis than prior work, and our framework attains 66.8% success in simulation and 74.6% on real experiments, demonstrating consistently strong performance across both settings. 

## **2 Related work** 

### **2.1 Bimanual Dexterous Grasp** 

Bimanual dexterous grasping extends grasping to large and heavy objects but remains underexplored due to the high dimension of the combined degrees of freedom. Reinforcement learning approaches [21, 22] suffer from limited scalability and heavy reliance on hand-crafted rewards, while data-driven methods [19, 20, 23] are constrained by the lack of high-quality datasets and suboptimal model architectures. In this work, we address these challenges with a large-scale dataset with high diversity and quality, and a novel generative framework tailored for bimanual dexterous grasping. 

### **2.2 Dexterous Grasp Dataset** 

The availability of large-scale and high-quality datasets is crucial for the development of robotic [9, 11, 13, 24]. Previous research on single-hand dexterous grasping has explored energy-based optimization methods [25, 10, 14, 15, 26, 27], enabling parallel synthesis of large-scale dexterous grasping data. However, in the bimanual setting, the expanded action space and coordination requirements push existing pipelines [19, 20, 23] into low efficiency and over-reliance on single-hand data, yielding datasets of narrow object diversity. In this work, we introduce a novel bimanual grasp synthesis pipeline and a corresponding large-scale dataset with broad geometric and scale coverage. 

2 

Table 1: Comparison with previous dexterous grasping datasets 

|**Dataset**|**Bim.**|**Obj**|**Grasp**|**Max**|**Range**|**Table**|**IK**|**Pre-Grasp**|**Data Independent**|
|---|---|---|---|---|---|---|---|---|---|
|DexGraspNet[10]<br>BODex[25]|_×_<br>_×_|5355<br>2397|1.32M<br>3.08M|30cm<br>24cm|28cm<br>12cm|_×_<br>✓|_×_<br>✓|_×_<br>✓|✓<br>✓|
|DHAGrasp[20]|✓|802|1.30M|30cm|20cm|_×_|_×_|_×_|_×_|
|BimanGrasp[19]|✓|900|0.15M|40cm|20cm|_×_|_×_|_×_|✓|
|**BiDexGrasp**|✓|**6351**|**9.53M**|**80cm**|**50cm**|✓|✓|✓|✓|



### **2.3 Data-Driven Dexterous Grasp Framework** 

Data-driven dexterous grasping frameworks have shown strong generalization to unseen objects [28, 29, 30]. Most existing methods rely on generative models [16, 31, 32], and extended through richer conditioning [33], dedicated training objectives and strategy [34, 35], physical-guided sampling [36] or bimanual extensions [19, 5]. However, they limit in the adaptation to diverse object geometries and sizes. In this paper, drawing inspiration from prior methods [11], our framework explicitly models bimanual coordination, producing robust bimanual grasps across object geometry and scale. 

## **3 Preliminaries** 

**Grasp Wrench Space (GWS).** Given an object with _m_ contact points, each contact _i_ is characterized by a position **p** _i_ , surface normal **n** _i_ , and a friction-cone-constrained local force **f** _i_ , which together induce a 6D wrench **w** _i_ = **G** _i_ **f** _i_ via the grasp matrix **G** _i_ . The set of feasible wrenches at contact _i_ is denoted _Wi_ , and the overall grasp wrench space is the Minkowski sum _W_ =<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_Wi_, which</sup> characterizes all wrenches the grasp can exert on the object. The minimum distance from the origin to the GWS boundary (GWB) reflects contact stability—a larger distance indicates a more stable grasp. **QP-Energy.** To evaluate the ability of a grasp to resist external disturbances, we adopt a differentiable metric based on quadratic programming. Given six target disturbance wrenches _{_ **t** _j}_<sup>6</sup> _j_ =1<sup>along the</sup> _±x, ±y, ±z_ axes, the energy is defined as _Q_ =<sup>�6</sup> _j_ =1<sup>min</sup><sup>**w**</sup> _j_<sup>_∈W ∥β_</sup><sup>**t**</sup><sup>_j−_</sup><sup>**w**</sup><sup>_j∥_2, where</sup><sup>_β_is a scaling</sup> factor. Intuitively, _Q_ measures how well the grasp wrench space _W_ can approximate disturbance directions. The detailed grasp matrix and QP formulation are provided in Appendix A. 

## **4 BiDexGrasp Dataset** 

### **4.1 Overview** 

**Problem Definition.** Given the object mesh _O_ , the goal of grasp data synthesis is to obtain bimanual dexterous grasp poses _G_<sup>_bi_</sup> = ( _G_<sup>_left_</sup> _, G_<sup>_right_</sup> ) = (( _t_<sup>_r_</sup> _, r_<sup>_r_</sup> _, q_<sup>_r_</sup> ) _,_ ( _t_<sup>_l_</sup> _, r_<sup>_l_</sup> _, q_<sup>_l_</sup> )), where _r_ and _t_ refer to the rotation and translation of hand wrist, and _q_ refers to the joint poses of dexterous hand. 

**Synthesis Overview.** We first collect 6,351 objects from [10] and [37] and scale each to 11 discrete sizes from 30 to 80 cm. The synthesis pipeline is consisted of three stages as shown in Figure 2. 

### **4.2 Bimanual Region-constraint Grasp Initialization** 

**Challenges for Bimanual Grasp Initialization.** Naively extending single-hand initialization causes quadratic sampling complexity, and most random pairs violate bimanual constraints. We address this with a bimanual region-constrained initialization strategy: grasping region candidates are first selected via the grasp wrench space (GWS), and initial poses are then sampled within these regions, yielding both efficient and reliable initialization. 

**GWS-based Bimanual Grasping Region Selection.** This module leverages GWS energy to efficiently filter bimanual grasping regions with the potential for stable, physically feasible grasps. Specifically, the region selection process consists of 3 steps. (1) We first apply farthest point sampling to select _Ka_ = 200 anchors and sample _k_ = 256 points within an 8 cm neighborhood around each anchor to define _Ka_ regions and _Ka_<sup>2region pairs.(2) We exclude the pairs with insufficient inter-</sup> region distance, and evaluate the remain pairs’ stability using the Grasp Wrench Boundary (GWB) 

3 



<!-- Start of picture text -->
1. Bimanual Region-constraint Grasp Initialization 2. Decoupled Grasping Optimization 3. Validation<br>Object Set GWS-based Region Selection Region-based Initialization Decoupled Force-Closure Optimization BiDexGrasp Dataset<br>Objaverse + DexGraspNet  1 Region Sampling Palm and Joint Initialization IK Configuration<br>Scaling(30cm-80cm) Left QP-Enegry Right QP-Enegry<br>…<br>Simulator-based Validation<br>2 GWB Evaluation<br>Collision & IK Filter<br>Contact Distance Energy Region Distance Energy<br>3 Top-K Seclection<br>6351 Objects11 Scale 𝑠= 1≤𝑗≤6min 1≤𝑘≤𝑀 max 𝐭 ⊤ 𝐣 𝐰𝐤<br><!-- End of picture text -->

Figure 2: The data synthesis pipeline for bimanual grasp. (1) Fast constraint-aware bimanual grasp initialization for physically feasible grasp bimanual candidate generation. (2) Decoupled force-closure optimization refines initial candidates into valid bimanual grasps. (3) Arm reachability analysis yields kinematic feasible poses, with MuJoCo [38] simulation filtering invalid grasps. 

estimated by the TDG estimator [39]. Specifically, _N_ = 5 contact points are sampled per region, and the resulting GWB is represented by a set of boundary wrenches _{_ **w** _k}_<sup>_M_</sup> _k_ =1<sup>with</sup><sup>_M_=1000.</sup> To assess robustness against external disturbances, we adopt the six disturbance wrenches _{_ **t** _j}_<sup>6</sup> _j_ =1 defined in the preliminaries. The stability score is computed as the minimum projection of the GWB onto these disturbance directions: _s_ = min1 _≤j≤_ 6 max1 _≤k≤M_ **t**<sup>_⊤_</sup> _j_<sup>**w**</sup><sup>_k._(3) Finally, we rank region</sup> pairs by stability score, and the top _Kr_ = 40 are retained as candidates for grasp initialization. 

**Region-based Grasp Initialization.** Given the selected regions, we initialize bimanual grasps _G_ initial by placing each palm at the closest point on the dilated convex hull to the region center, with orientation aligned to the surface normal. We then enforce collision checking and inverse kinematics (IK) feasibility, discarding invalid configurations before optimization. 

### **4.3 Decoupled Grasping Optimization** 

**Challenges for Bimanual Grasp Optimization.** Bimanual grasp optimization is inherently challenging because the enlarged search space induces a tightly coupled objective that destabilizes optimization and often yields imbalanced solutions, where one hand dominates stability while the other contributes marginally, leading to suboptimal local minima. 

**Decoupled Force Closure.** To obtain high-quality and physically feasible bimanual grasps, we propose a novel optimization strategy which decompose the bimanual force closure energy into singlehand energy terms, allowing each hand to focus on establishing stable local contacts. This decoupling reduces optimization complexity and discourages single-hand-dominated solutions, improving both grasp quality and convergence stability. Specifically, we formulate the overall optimization as follows to optimize _G_<sup>_bi_</sup> by minimizing the QP-Energy decoupled into two single-hand energy terms: 



**c** _i,l_ and **c** _i,w_ denote the positions of the predefined hand contact point _i_ expressed in the local link frame and the world frame. In the QP formulation, the grasp matrix is constructed by associating each **c** _i,w_ with its closest point **p** _i_ on the object surface, while feasibility is ensured through joint-limit and collision-avoidance constraints. We introduce a distance term _Edis_ to encourage proximity between **c** _i,w_ and **p** _i_ , and a region consistency term _Eregion_ to keep the contacts close to the initialized contact regions. The detailed formulations are provided in Appendix B and A. 

### **4.4 Kinematics-Aware Arm-Hand Configuration Synthesis** 

To demonstrate the practical feasibility of the synthesized grasps, our framework supports solving the inverse kinematics (IK) for wrist poses, enabling reachable tabletop configurations. To avoid collisions and facilitate force application, we first synthesize a pre-grasp pose _Gpre_<sup>_bi_, maintaining a</sup> 

4 



<!-- Start of picture text -->
Grasp View Bimanual Coordination Module<br>𝑦𝑥𝑧111 𝑦𝑥𝑧222 𝑦𝑥𝑧333 𝑥𝑦𝑧444 𝑦𝑥𝑧555 𝑦𝑥𝑧666 … 𝑥𝑦𝑧𝑘𝑘𝑘 𝐯 𝟏 𝐯 𝟐 𝐯 𝟑 𝐯 𝟒 … 𝐯 𝐤 0 3.10 1.1 … 1.9 𝑳𝒐𝒔𝒔single−view 0 3 𝑙𝑎𝑏𝑒𝑙 0 1 single … 2<br>𝒗𝒊,𝒋 = 𝒇(𝒗𝒊, 𝒗𝒋) 𝑠𝑒𝑙𝑒𝑐𝑡 best view<br>𝑙𝑎𝑏𝑒𝑙𝑏𝑖<br>𝐯𝟏,𝟏 𝐯𝟏,𝟐 𝐯𝟏,𝟑 𝐯𝟏,𝟒 … 𝐯𝟏,𝐤 0 0.10 0 … 0 0 0 0 0 … 0<br>𝐯𝐯𝟐,𝟏𝟑,𝟏 𝐯𝐯𝟐,𝟐𝟑,𝟐 𝐯𝐯𝟐,𝟑𝟑,𝟑 𝐯𝐯𝟐,𝟒𝟑,𝟒 …… 𝐯𝐯𝟐,𝐤𝟑,𝐤 1.10 00 00 2.10 …… 0.20 𝑳𝒐𝒔𝒔𝒃𝒊−view 01 00 00 02 …… 00<br>𝐯𝟒,𝟏 𝐯𝟒,𝟐 𝐯𝟒,𝟑 𝐯𝟒,𝟒 … 𝐯𝟒,𝐤 0.10 0.8 0 … 0 0 0 1 0 … 0<br>… … … … … … … … … … … … … … … … … …<br>𝐯𝐤,𝟏 𝐯𝐤,𝟐 𝐯𝐤,𝟑 𝐯𝐤,𝟒 … 𝐯𝐤,𝐤 0 0.9 0 0 … 1.1 0 1 0 0 … 1<br>𝑠𝑒𝑙𝑒𝑐𝑡 coordinated bi-views<br>Object Point Cloud Geometry - Adaptive Feature 𝒗𝟒 𝒗𝟒<br>𝒗𝟐 𝒗𝟐<br>Point Filter<br>featuresglobal View features 𝐯 𝟐 𝐯 𝟒 Local features<br>Noise Hand Pose Grasp based on Scale - Adaptive Anchor<br>Relative Dexterous<br>Grasp Diffusion<br>View Feature Extractor<br><!-- End of picture text -->

Figure 3: BiDexGrasp Framework. Given the input object point cloud and pre-defined grasp view, the framework first predicts a pair of coordinated grasp views for the two hands by Bimanual Coordination Module. Based on this view, we extract geometry-adaptive object feature and determine the scale-adaptive grasp. Then the relative grasp diffusion is employed to predict relative dexterous grasp form the grasp anchor. 

contact distance of 1cm, following [25]. And we compute a squeeze pose as the execution target: _Gsqu_<sup>_bi_= 2</sup><sup>_· Gbi −G_</sup> pre<sup>_bi_.Finally, we generate arm joint trajectories from pre-grasp to squeeze and lift.</sup> 

## **5 BiDexGrasp Framework** 

**Problem Definition.** To learn generable bimanual dexterous grasp, we design a data-driven generation model which take object point cloud _Opc_ as input and generate bimanual dexterous grasp poses _G_<sup>_bi_</sup> . 

**Challenge in Bimanual Grasping.** Bimanual grasp generation introduces two key challenges. (1) _Bimanual coordination_ : Bimanual hands must collaboratively target optimal grasp view to ensure global stability while avoiding inter-hand collisions. (2) _Adaptation across object geometries and sizes_ : The vast diversity in object sizes and geometries greatly hinders efficient model learning, increasing the difficulty of object feature extraction and expanding the action space simultaneously. 

**Model Overview.** To address these challenges, we propose **BiDexGrasp** , which achieves bimanualcoordinated and geometry-size-adaptive grasp generation through two components: (1) a _bimanual coordination module_ that explicitly models inter-hand relationships via coordinated-view prediction; (2) a _geometry-size-adaptive generation strategy_ that improves cross-object generalization through adaptive grasp anchors. The model pipeline is shown in Fig. 3. 

### **5.1 Bimanual Coordination Module.** 

To explicitly model bimanual coordination, we first estimate coordination-aware grasping views to guide subsequent grasp prediction. The module first predicts the most promising view as the primary grasping view, and predicts the second view that is most compatible with the primary view. 

Specifically, we uniformly sample _K_ discrete approach directions on the object bounding sphere to construct a candidate view set _V_ = _{_ **v** _i}_<sup>_K_</sup> _i_ =1<sup>, which formulate view estimation as a view probabilistic</sup> regression. To predict the primary view, we introduce _K_ learnable view embeddings **v** _i_<sup>_emb_</sup> to extract view features **F** view = _{_ **f** _i}_<sup>_K_</sup> _i_ =1<sup>by cross-attention:</sup><sup>**f**</sup><sup>_i_= Attn(</sup><sup>**v**</sup> _i_<sup>_emb_</sup> _,_ **F** _global,_ **F** _global_ ) , where **F** global are point features extracting by PointNet++ [40]. To predict the second view, we model interactions between the primary view and the remaining candidate views to construct bi-view features by a MLPs layer: **f** _i,j_<sup>_bi_=</sup><sup>_MLP_</sup> � _cat_ ( **f** _i,_ **f** _j,_ **f** _i −_ **f** _j,_ **f** _i ⊙_ **f** _j_ )� _._ These features predict the single-view and bi-view probabilities _pi_ and _p_<sup>_bi_</sup> _i,j_<sup>, supervised by SmoothL1 losses against ground-truth probabilities</sup><sup>_yi_and</sup><sup>_y_</sup> _i,j_<sup>_bi_</sup> derived from the successful-grasp distribution of each object. For single-view, we assign each grasp to the nearest predefined candidate view, then count the number of grasps associated with each view and normalize these counts to form a probability. Similarly, the bi-view ground-truth probabilities are 

5 

Table 2: Performance comparison of dual-arm grasping on DexGraspNet and Objaverse datasets. 

|**Method**|**SUC-F**_↑_|**SUC-L**_↑_|**SUC-A**_↑_|**S**_↑_|**PD**_↓_|**SPD**_↓_|**CDC**_↓_|**D**_↓_|
|---|---|---|---|---|---|---|---|---|
|**_DexGraspNet_**|||||||||
|BimanGrasp [19]|26.80|–|–|0.16|1.52|0.26|1.87|**0.150**|
|Ours(Float)|75.84|–|–|6.73|0.17|0.02|0.59|0.190|
|Ours(TableTop)|**77.11**|**80.83**|**71.34**|**6.87**|**0.15**|**0.02**|**0.52**|0.165|
|**_Objaverse_**|||||||||
|BimanGrasp [19]|30.21|–|–|0.16|0.87|0.23|1.38|**0.156**|
|Ours(Float)|**70.82**|–|–|4.55|0.20|**0.04**|0.67|0.180|
|Ours(TableTop)|62.41|**70.41**|**62.40**|**5.10**|**0.20**|0.05|**0.67**|0.158|



obtained by considering pairs of grasps. Each grasp pair is mapped to the nearest candidate view pair, and the counts are normalized over all candidate pairs to produce a probability ground-truth. 

### **5.2 Geometry-Size-Adaptive Grasp Generation Strategy** 

**Scale-Adaptive Grasp Anchor** To improve adaptability to object size, we formulate the grasp wrist prediction as a relative pose (∆ _t,_ ∆ _r_ ) prediction with respect to a grasp anchor _ganchor_ = ( _tanchor, rancho_ ), which is adapted to the size of the object. 





The adaptive grasp anchor is determine dynamically according to the grasp view and object point cloud. Specifically, each predicted view intersects with minimum bounding sphere surface, producing an grasp anchor. This anchor-based formulation converts the original absolute pose prediction problem into a relative regression task, significantly reducing the search space of grasps and improve the adaptation to object scale. 

**Geometry-Adaptive Object Feature** To improve adaptability to object geometry, we extract local geometric features around each predicted grasp anchor, as global features may be dominated by irrelevant structures. Specifically, the global point cloud is first upsampled into _Kp_ representative points using farthest point sampling (FPS). For each predicted grasp anchor, features are then aggregated from its _Kc_ -nearest neighbors (KNN). This local feature **F** local captures fine-grained surface geometry around potential contact regions while filtering out distant or grasp-irrelevant structures, which facilitates geometry-adaptive grasp generation. Finally, the local features, view features, and global features are concatenated along the token dimension to form the final object feature representation. 



**Relative Dexterous Grasp Diffusion** We propose a relative dexterous grasp diffusion to generate bimanual relative wrist poses (∆ _t_<sup>_bi_</sup> _,_ ∆ _r_<sup>_bi_</sup> ) and dexterous joint poses _q_<sup>_bi_</sup> , based on the scale-adaptive grasp anchor _ganchor_ = ( _tanchor, ranchor_ ) and geometry-adaptive object feature **F** _ga−obj_ . We adopt the DDPM sampling process [41], which can be formalized as follows: 



where _G_<sup>_bi,rela_</sup> = (∆ _t_<sup>_bi_</sup> _,_ ∆ _r_<sup>_bi_</sup> _, q_<sup>_bi_</sup> ), and _p_ ( _G_<sup>_bi,rela_</sup> ) is modeled as a Gaussian distribution. During training, we apply L2 losses separately to the translation, rotation, and joint parameter regressions. In addition, we incorporate Chamfer loss [42] to explicitly supervise hand geometry. We further introduce a physics-based loss to penalize hand–object penetration as well as intra- and inter-hand self-penetration. All details could be found in Appendix C. 



6 

|Table 3:|Ablati|on of d|ata s|ynth|esis.|Table|4: Com|paris|on w|ith SO|TAs.|Table 5|: Abla|tion of|fram|ewo|rk.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Method|SUC-L|SUC-A|SGS|PD|SPD|Method|SUC-L|PD|SPD|CDC|D|BCM GAF|SAGA|SUC-L|PD|SPD|CDC|
|Baseline|28.3|12.9|2.1|0.18|0.08|[17]|15.2|3.29|0.11|3.79|**0.174**|_×_<br>_×_|_×_|41.2|2.25|**0.01**|2.87|
|+R|44.4|39.8|2.8|**0.13**|0.03|[43]|41.5|2.24|0.13|3.02|0.201|_×_<br>✓|✓|44.7|2.28|**0.01**|2.96|
|+R+Dc|57.7|49.5|4.0|0.15|0.03|||||||✓<br>✓|_×_|52.7|2.05|0.02|2.82|
|**+R+Dc+Ps**|**80.8**|**71.3**|**5.6**|0.15|**0.03**|**Ours**|**66.8**|**1.53 **|**0.01**|**2.32**|0.197|✓<br>✓|✓|**61.9**|**1.73**|0.02|**2.56**|



## **6 Experiments** 

### **6.1 Experiment Settings** 

**Data Synthesis.** Evaluation is conducted in MuJoCo with Shadow Hand, using tangential/torsional friction coefficients of 0.6/0.02, gravity 9 _._ 8 m _/_ s<sup>2</sup> , object density 2 _._ 5 kg _/_ m<sup>3</sup> . We randomly sample 1,000 objects from DexGraspNet and Objaverse, scale each to 6 sizes (30–80 cm) to form 12,000 instances, synthesizing 5 grasps per instance (60,000 grasps per method). For [19], pre-grasp and squeeze poses are obtained by translating the palm by _±_ 1 cm and perturbing finger joints by _±_ 0 _._ 1 rad. 

**Generation Framework.** The generation framework evaluation is conduct on the DexGraspNet subset of our tabletop dataset. The dataset consists of 2,397 objects, which are randomly split into training and test sets with a 4:1 ratio, resulting in 3,112,117 training grasps. During evaluation, for each test object, we generate 3 grasps for every object pose and scale, yielding a total of 139,956 grasps, which are evaluated under the same evaluation as data generation pipeline. 

### **6.2 Implements Details** 

**Data Synthesis.** We set _wQP_ = 1000, _w_ dis = 100, _w_ region = 50, and generate the dataset on eight NVIDIA 3090 GPUs with 40 parallel worlds per GPU and 20 grasps per world. 

**Generation Framework.** We set _K_ = 16, _Kp_ = 256 and _Kc_ = 16. For the comparison experiments, we train models for 5 epochs. For the ablation studies, models are trained for 20 epochs on a subset that includes all object scales but only one tabletop pose per object. All experiments are implemented in PyTorch and conducted on single RTX 4090 GPU. Additional details are provided in Appendix C. 

### **6.3 Evaluation Metrics** 

Following [25], we evaluate the data synthesis pipeline and generation framework with the following metrics (see Appendix D for full definitions). **Grasp Success Rate (SUC)** (%) measures grasp robustness in simulation under three settings: force-closure against 6 external disturbances ( **SUC-F** ), tabletop lifting with a floating hand ( **SUC-L** ), and with an arm-controlled hand ( **SUC-A** ). **Speed (S)** and **Success Generation Speed (SGS)** (grasps/s) quantify raw and successful synthesis throughput. **Penetration Depth (PD)** (cm) and **Self-Penetration Depth (SPD)** (cm) measure the physical plausibility of hand–object contact and of the hand configuration itself (intra- and inter-hand collisions), respectively. **Contact Distance Consistency (CDC)** (cm) characterizes the uniformity of finger contacts, and **Diversity (D)** (%) the diversity of the generated grasp distribution. 

### **6.4 Data Synthesis Experiments** 

**Comparison Results.** We compare with BimanGrasp, a representative open-source bimanual grasp synthesis pipeline. Since BimanGrasp is restricted to floating-base grasp generation, we evaluate our method in both floating and tabletop settings for a fair comparison. Tab. 2 shows that our pipeline significantly outperforms prior work in both quality (SUC, PD, SPD, CDC) and speed (S). On DexGraspNet, we increase the SUC by roughly 2 _._ 8 _×_ under both floating-hand and tabletop settings, with a 40 _×_ synthesis speedup. On Objaverse, which features more complex geometries, our method maintains strong success rates and high synthesis efficiency. 

**Ablation Study.** Tab. 3 shows the ablation study for each component of our synthesis pipeline. The baseline is a straightforward extension of BODex from the single-hand setting to a bimanual setup. 

7 



<!-- Start of picture text -->
Inspire Hands BrainCo Hands<br>Inspire Hands<br>Object Set<br><!-- End of picture text -->

Figure 5: Real-world experiments. Left: qualitative grasp results. Right: hardware setup and object set. 

The results show that R (Region Initialization), Dc (Decoupled Force-Closure) and Ps (Pre-grasp Strategies) all contribute to improving grasp success rate (SUC-L and -A) and synthesis speed (SGS). 

### **6.5 Generation Framework Experiments** 

**Comparison Results.** Tab. 4 reports our method against recent SOTA approaches. Our method achieves the highest SUC with the lowest PD and SPD, indicating precise and stable grasps. While diversity is slightly lower, this trade-off is acceptable since our task prioritizes grasp success. Overall, our method outperforms prior methods in both feasibility and reliability. 

**Ablation Study.** Tab. 5 evaluates each component over a DDPM-based bimanual baseline. The Bimanual Coordination Module (BCM) substantially raises SUC, confirming its role in coordinating dual-hand grasps. The Geometry-Adaptive Feature (GAF) and Scale-Adaptive Grasp Anchor (SAGA) adapt to local geometry and object scale, jointly boosting SUC and reducing SPD and CDC. 

### **6.6 Real-World Experiments** 

We conduct real-world experiments with two dexterous hands (Inspire and BrainCo) and three robotic arms (Unitree G1, Piper, and Nero), performing 260 trials on 30 objects (setup and qualitative results in Fig. 5). We evaluate two input settings: single-view and full point clouds. For single-view, we extract object point clouds from RGB-D images via a segmentation model [44]. For full point clouds, we reconstruct object meshes [45], estimate 6D poses [46], and sample the point cloud. ShadowHand grasps are retargeted [35] to the Inspire and BrainCo hands. Our method achieves 66.0% success on single-view and 76.7% on full point clouds, averaging 74.6%. 

## **7 Conclusion** 

We present BiDexGrasp, a comprehensive solution that advances bimanual dexterous grasping through both a large-scale dataset and a learning-based framework. Our synthesis pipeline yields a dataset of 6,351 diverse objects with 9.53M annotated grasps, on which our generation framework produces high-quality grasps for unseen objects. Extensive experiments in simulation and the real world show that our pipeline significantly improves synthesis efficiency and quality, and our framework generates coordinated, high-quality grasps across diverse objects. 

## **8 Limitations** 

First, our synthesis pipeline assumes fixed hand contact points, which restricts the contact-space diversity of generated grasps. Second, our method is stability-oriented and may struggle on tasks requiring specific functional contacts; integrating semantic priors into the bimanual grasping region is a promising direction. Finally, our model operates in the floating-hand setting and does not use the dataset’s IK configurations; joint arm-hand prediction is a natural extension for future work. 

8 

## **References** 

- [1] H. Zhang, Z. Wu, L. Huang, S. Christen, and J. Song. Robustdexgrasp: Robust dexterous grasping of general objects. _arXiv preprint arXiv:2504.05287_ , 2025. 

- [2] Y. Zhong, X. Huang, R. Li, C. Zhang, Z. Chen, T. Guan, F. Zeng, K. N. Lui, Y. Ye, Y. Liang, et al. Dexgraspvla: A vision-language-action framework towards general dexterous grasping. _arXiv preprint arXiv:2502.20900_ , 2025. 

- [3] Y. Cui, Y. Zhang, L. Tao, Y. Li, X. Yi, and Z. Li. End-to-end dexterous arm-hand vla policies via shared autonomy: Vr teleoperation augmented by autonomous hand vla policy for efficient data collection. _arXiv preprint arXiv:2511.00139_ , 2025. 

- [4] K. Li, P. Li, T. Liu, Y. Li, and S. Huang. Maniptrans: Efficient dexterous bimanual manipulation transfer via residual learning. In _Proceedings of the Computer Vision and Pattern Recognition Conference_ , pages 6991–7003, 2025. 

- [5] K. Shaw, Y. Li, J. Yang, M. K. Srirama, R. Liu, H. Xiong, R. Mendonca, and D. Pathak. Bimanual dexterity for complex tasks. _arXiv preprint arXiv:2411.13677_ , 2024. 

- [6] Y.-L. Wei, Z. Luo, Y. Lin, M. Lin, Z. Liang, S. Chen, and W.-S. Zheng. Omnidexgrasp: Generalizable dexterous grasping via foundation model and force feedback. _arXiv preprint arXiv:2510.23119_ , 2025. 

- [7] H. Yuan, Z. Huang, Y. Wang, C. Mao, C. Xu, and Z. Lu. Demograsp: Universal dexterous grasping from a single demonstration. _arXiv preprint arXiv:2509.22149_ , 2025. 

- [8] Y. Lin, Y.-L. Wei, H. Liao, M. Lin, C. Xing, H. Li, D. Zhang, M. Cutkosky, and W.-S. Zheng. Typetele: Releasing dexterity in teleoperation by dexterous manipulation types. _arXiv preprint arXiv:2507.01857_ , 2025. 

- [9] H.-S. Fang, C. Wang, M. Gou, and C. Lu. Graspnet-1billion: A large-scale benchmark for general object grasping. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 11444–11453, 2020. 

- [10] R. Wang, J. Zhang, J. Chen, Y. Xu, P. Li, T. Liu, and H. Wang. Dexgraspnet: A largescale robotic dexterous grasp dataset for general objects based on simulation. _arXiv preprint arXiv:2210.02697_ , 2022. 

- [11] J. Zhang, H. Liu, D. Li, X. Yu, H. Geng, Y. Ding, J. Chen, and H. Wang. Dexgraspnet 2.0: Learning generative dexterous grasping in large-scale synthetic cluttered scenes. In _8th Annual Conference on Robot Learning_ , 2024. 

- [12] J. He, D. Li, X. Yu, Z. Qi, W. Zhang, J. Chen, Z. Zhang, Z. Zhang, L. Yi, and H. Wang. Dexvlg: Dexterous vision-language-grasp model at scale. _arXiv preprint arXiv:2507.02747_ , 2025. 

- [13] J. Ye, K. Wang, C. Yuan, R. Yang, Y. Li, J. Zhu, Y. Qin, X. Zou, and X. Wang. Dex1b: Learning with 1b demonstrations for dexterous manipulation. _arXiv preprint arXiv:2506.17198_ , 2025. 

- [14] T. Liu, Z. Liu, Z. Jiao, Y. Zhu, and S.-C. Zhu. Synthesizing diverse and physically stable grasps with arbitrary hand structures using differentiable force closure estimator. _IEEE Robotics and Automation Letters_ , 7(1):470–477, 2021. 

- [15] M. Liu, Z. Pan, K. Xu, K. Ganguly, and D. Manocha. Deep differentiable grasp planner for high-dof grippers. _arXiv preprint arXiv:2002.01530_ , 2020. 

- [16] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 4737–4746, 2023. 

9 

- [17] S. Huang, Z. Wang, P. Li, B. Jia, T. Liu, Y. Zhu, W. Liang, and S.-C. Zhu. Diffusion-based generation, optimization, and planning in 3d scenes. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 16750–16761, 2023. 

- [18] L. Shao, F. Ferreira, M. Jorda, V. Nambiar, J. Luo, E. Solowjow, J. A. Ojea, O. Khatib, and J. Bohg. Unigrasp: Learning a unified model to grasp with multifingered robotic hands. _IEEE Robotics and Automation Letters_ , 5(2):2286–2293, 2020. 

- [19] Y. Shao and C. Xiao. Bimanual grasp synthesis for dexterous robot hands. _IEEE Robotics and Automation Letters_ , 2024. 

- [20] Q. Li, Z. Wu, J. Wang, C. C. Loy, and B. Dai. Dhagrasp: Synthesizing affordance-aware dual-hand grasps with text instructions. _arXiv preprint arXiv:2509.22175_ , 2025. 

- [21] H. Zhang, S. Christen, Z. Fan, L. Zheng, J. Hwangbo, J. Song, and O. Hilliges. Artigrasp: Physically plausible synthesis of bi-manual dexterous grasping and articulation. In _2024 International Conference on 3D Vision (3DV)_ , pages 235–246. IEEE, 2024. 

- [22] Y. Chen, Y. Geng, F. Zhong, J. Ji, J. Jiang, Z. Lu, H. Dong, and Y. Yang. Bi-dexhands: Towards human-level bimanual dexterous manipulation. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 46(5):2804–2818, 2023. 

- [23] S. Yang, Y. Xie, Z. Liang, Y. Tian, J. Zeng, D. Lin, and J. Pang. Ultradexgrasp: Learning universal dexterous grasping for bimanual robots with synthetic data. _arXiv preprint arXiv:2603.05312_ , 2026. 

- [24] Y. Mu, T. Chen, S. Peng, Z. Chen, Z. Gao, Y. Zou, L. Lin, Z. Xie, and P. Luo. Robotwin: Dualarm robot benchmark with generative digital twins (early version). In _European Conference on Computer Vision_ , pages 264–273. Springer, 2024. 

- [25] J. Chen, Y. Ke, and H. Wang. Bodex: Scalable and efficient robotic dexterous grasp synthesis using bilevel optimization. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 01–08. IEEE, 2025. 

- [26] R. Zurbrügg, A. Cramariuc, and M. Hutter. Graspqp: Differentiable optimization of force closure for diverse and robust dexterous grasping. _arXiv preprint arXiv:2508.15002_ , 2025. 

- [27] J. Chen, Y. Ke, L. Peng, and H. Wang. Dexonomy: Synthesizing all dexterous grasp types in a grasp taxonomy. _arXiv preprint arXiv:2504.18829_ , 2025. 

- [28] H.-S. Fang, H. Yan, Z. Tang, H. Fang, C. Wang, and C. Lu. Anydexgrasp: General dexterous grasping for different hands with human-level learning efficiency. _arXiv preprint arXiv:2502.16420_ , 2025. 

- [29] Z. Chen, Q. Yan, Y. Chen, T. Wu, J. Zhang, Z. Ding, J. Li, Y. Yang, and H. Dong. Clutterdexgrasp: A sim-to-real system for general dexterous grasping in cluttered scenes. _arXiv preprint arXiv:2506.14317_ , 2025. 

- [30] L. Huang, H. Zhang, Z. Wu, S. Christen, and J. Song. Fungrasp: functional grasping for diverse dexterous hands. _IEEE Robotics and Automation Letters_ , 2025. 

- [31] H. Jiang, S. Liu, J. Wang, and X. Wang. Hand-object contact consistency reasoning for human grasps generation. In _Proceedings of the IEEE/CVF international conference on computer vision_ , pages 11107–11116, 2021. 

- [32] Z. Wei, Z. Xu, J. Guo, Y. Hou, C. Gao, Z. Cai, J. Luo, and L. Shao. D (r, o) grasp: A unified representation of robot and object interaction for cross-embodiment dexterous grasping. _arXiv preprint arXiv:2410.01702_ , 2024. 

10 

- [33] Y.-L. Wei, M. Lin, Y. Lin, J.-J. Jiang, X.-M. Wu, L.-A. Zeng, and W.-S. Zheng. Afforddexgrasp: Open-set language-guided dexterous grasp with generalizable-instructive affordance. _arXiv preprint arXiv:2503.07360_ , 2025. 

- [34] J. Lu, H. Kang, H. Li, B. Liu, Y. Yang, Q. Huang, and G. Hua. Ugg: Unified generative grasping. In _European Conference on Computer Vision_ , pages 414–433. Springer, 2024. 

- [35] Y.-L. Wei, J.-J. Jiang, C. Xing, X.-T. Tan, X.-M. Wu, H. Li, M. Cutkosky, and W.-S. Zheng. Grasp as you say: Language-guided dexterous grasp generation. _Advances in Neural Information Processing Systems_ , 37:46881–46907, 2024. 

- [36] Y. Zhong, Q. Jiang, J. Yu, and Y. Ma. Dexgrasp anything: Towards universal robotic dexterous grasping with physics awareness. In _Proceedings of the Computer Vision and Pattern Recognition Conference_ , pages 22584–22594, 2025. 

- [37] M. Deitke, D. Schwenk, J. Salvador, L. Weihs, O. Michel, E. VanderBilt, L. Schmidt, K. Ehsani, A. Kembhavi, and A. Farhadi. Objaverse: A universe of annotated 3d objects. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 13142–13153, 2023. 

- [38] E. Todorov, T. Erez, and Y. Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ international conference on intelligent robots and systems_ , pages 5026–5033. IEEE, 2012. 

- [39] J. Chen, Y. Chen, J. Zhang, and H. Wang. Task-oriented dexterous grasp synthesis via differentiable grasp wrench boundary estimator. _arXiv preprint arXiv:2309.13586_ , 2023. 

- [40] C. R. Qi, L. Yi, H. Su, and L. J. Guibas. Pointnet++: Deep hierarchical feature learning on point sets in a metric space. _Advances in neural information processing systems_ , 30, 2017. 

- [41] J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic models. _Advances in neural information processing systems_ , 33:6840–6851, 2020. 

- [42] H. Fan, H. Su, and L. J. Guibas. A point set generation network for 3d object reconstruction from a single image. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 605–613, 2017. 

- [43] G.-H. Xu, Y.-L. Wei, D. Zheng, X.-M. Wu, and W.-S. Zheng. Dexterous grasp transformer. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 17933–17942, 2024. 

- [44] T. Ren, S. Liu, A. Zeng, J. Lin, K. Li, H. Cao, J. Chen, X. Huang, Y. Chen, F. Yan, et al. Grounded sam: Assembling open-world models for diverse visual tasks. _arXiv preprint arXiv:2401.14159_ , 2024. 

- [45] Hyper3D. Hyper3d: Ai-powered 3d model generator, 2024. URL https://hyper3d.ai/. 

- [46] B. Wen, W. Yang, J. Kautz, and S. Birchfield. Foundationpose: Unified 6d pose estimation and tracking of novel objects. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 17868–17879, 2024. 

- [47] A. L. Bishop, J. Z. Zhang, S. Gurumurthy, K. Tracy, and Z. Manchester. Relu-qp: A gpuaccelerated quadratic programming solver for model-predictive control. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 13285–13292. IEEE, 2024. 

- [48] B. Sundaralingam, S. K. S. Hari, A. Fishman, C. Garrett, K. Van Wyk, V. Blukis, A. Millane, H. Oleynikova, A. Handa, F. Ramos, et al. curobo: Parallelized collision-free minimum-jerk robot motion generation. _arXiv preprint arXiv:2310.17274_ , 2023. 

- [49] K. Shaw, A. Agarwal, and D. Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _arXiv preprint arXiv:2309.06440_ , 2023. 

11 

## **A Preliminaries** 

**Contact Model** characterizes the resultant wrench exerted by a grasp on an object. Considering an object _O_ with _m_ contact points, the local contact mechanics at each point _i ∈{_ 1 _, . . . , m}_ are modeled as follows: 



where **p** _i ∈_ R<sup>3</sup> denotes the contact position and **n** _i ∈_ R<sup>3</sup> represents the inward-pointing unit surface normal. The vectors **d** _i,_ **e** _i ∈_ R<sup>3</sup> are orthogonal unit tangent vectors such that **n** _i_ = **d** _i ×_ **e** _i_ , and _µ_ is the friction coefficient. 

For each contact point, _Fi_ represents the discretized friction cone and _Gi_ is the grasp matrix. The local contact force **f** _i ∈Fi_ is mapped to a 6D wrench **w** _i ∈_ R<sup>6</sup> in the object’s coordinate frame via **w** _i_ = **G** _i_ **f** _i_ and the total wrench **w** generated by the grasp is the sum of the individual wrenches from all _m_ contact points, i.e., **w** =<sup>�</sup><sup>_m_</sup> _i_ =1<sup>**w**</sup><sup>_i_.</sup> 

**Grasp Wrench Space (GWS)** , denoted as _W_ , encompasses the set of all possible resultant wrenches that can be exerted on the object. For each contact point _i_ , we define the individual wrench space as _Wi_ = _{_ **G** _i_ **f** _i |_ **f** _i ∈Fi}_ . The aggregate GWS is then constructed via the Minkowski sum of these per-contact wrench spaces _W_ =<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_Wi_.</sup> 

**QP-Energy** is a differentiable metric designed to evaluate the capability of the current contact state to resist external disturbances _{_ **t** _j}_<sup>6</sup> _j_ =1<sup>along six orthogonal axes, e.g., [</sup><sup>_±_1</sup><sup>_,_0</sup><sup>_,_0</sup><sup>_,_0</sup><sup>_,_0</sup><sup>_,_0]</sup><sup>_⊤_.For a fixed</sup> contact system _{_ **G** _i}_ and disturbances _{tj}_ , the QP-Energy _Q_ is calculated as: 



where _β_ and _γ_ are two positive hyperparameters. 

## **B Data Synthesis Details** 

### **B.1 Details of Bimanual Region-constraint Grasp Initialization** 

**GWS-based Bimanual Grasping Region Selection** As described in the main paper, we first sample candidate regions on the object surface and generate local regions around them. These regions are then filtered to form valid region pairs, which are subsequently evaluated using the GWB metric, from which the top-performing pairs are selected. This section provides additional details on the region filtering process. 

To avoid physically infeasible or redundant grasps, region pairs that are too close are discarded. Given two regions _Ra_ and _Rb_ , we compute the minimum inter-region distance 



and retain the pair only if _d_ ( _Ra, Rb_ ) _≥ τ_ 2, where _τ_ 2 = 5 cm. 

**Region-based Grasp Initialization** This section provides additional details on the initialization of hand poses, including the computation of the initial rotation and the initialization of joint angles. 

As described in the main paper, for each hand we first select the point on the object’s inflated closure that is closest to the chosen region. The palm center is positioned to face this point, and the palm 

12 

normal is aligned with the inward-facing normal of the closure at that location. Subsequently, the hand base is rotated around the palm normal to the orientation that is closest to a predefined preferred direction, which is chosen to be kinematically favorable for the robot arm. Specifically, the preferred direction is set to (1 _, −_ 1 _, −_ 1) for the left hand and (1 _,_ 1 _, −_ 1) for the right hand, corresponding to forward–downward–right and forward–downward–left orientations, respectively. 

For joint angle initialization, we adapt the finger configuration based on whether the associated contact region is locally flat. Flatness is determined by the dispersion of surface normal directions within the region. Given a set of surface normal vectors _{_ **n** _i}_<sup>_N_</sup> _i_ =1<sup>for a region, we first normalize them</sup> and compute the resultant length 



Following directional statistics, we define the angular variance as 



A region is classified as flat if _V < τ_ , where _τ_ = 0 _._ 005 in all experiments. If the region is flat, the fingers are initialized in a more open configuration; otherwise, they are initialized with a slightly inward-curved posture. 

### **B.2 Details of Decoupled Grasping Optimization** 

As stated in the main paper, the overall optimization process can be formulated as 



And we define _Edis_ to encourage the contact points on the hands to be close to the corresponding points on the object surface: 



We further introduce a region consistency term _Eregion_ to keep the contact points close to the contact regions identified during initialization, thereby promoting coordinated bimanual grasping: 



where the effective distance _di_ from the _i_ -th hand contact point to the contact region _R_ is defined as 



and _ϕ_ ( _·_ ) is a piecewise penalty function given by 



with _a_ denoting a distance threshold, _b_ = 2 _a_ defining the transition bandwidth, and _H_ ( _t_ ) = 3 _t_<sup>2</sup> _−_ 2 _t_<sup>3</sup> being a cubic Hermite interpolation function. 

This objective naturally leads to a bi-level optimization procedure. In the low-level optimization, we fix the grasp parameters _G_<sup>_left_</sup> and _G_<sup>_right_</sup> , and solve for the grasp quality terms _Q_ ( _G_<sup>_left_</sup> ) and _Q_ ( _G_<sup>_right_</sup> ). This step is implemented using ReLU-QP[47], a PyTorch-based ADMM solver, which enables efficient and parallel computation of QP-based grasp energies across different objects. 

In the upper-level optimization, the grasp parameters _G_<sup>_left_</sup> and _G_<sup>_right_</sup> are optimized to minimize the weighted sum of all energy terms while satisfying the kinematic and collision constraints. 

13 



<!-- Start of picture text -->
𝒗 𝟓<br>𝒗 𝟒<br>𝒗 𝟏𝟑 𝒗 𝟗<br>𝒗 𝟏𝟎<br>𝒗 𝟏𝟐<br>𝑣 1 𝑣 2 𝑣 3 𝒗 𝟒 𝒗 𝟓 𝑣 6 𝑣 7 𝑣 8 𝒗 𝟗 𝒗 𝟏𝟎 𝑣 11 𝒗 𝟏𝟐 𝒗 𝟏𝟑 𝑣 14 𝑣 15 𝑣 16<br>0.12 0.16 0.15 0.12 0.25 0.11 0.20 0.21 0.10 0.46 0.10 0.13 0.54 0.07 0.25 0.14<br>0.01 0.00 0.00 0.06 0.00 0.04 0.00 0.00 0.19 0.01 0.02 0.46 0.00 0.02 0.02 0.00<br>(a) Distribution of grasp translation parameter (b) Grasp anchors and their scores during inference<br><!-- End of picture text -->

Figure 6: Visualization of scale-adaptive grasp anchors. (a) Distribution of grasp translation parameters represented in the world coordinate system (blue) and in the anchor coordinate system (orange), respectively. Results show the proposed anchor-based formulation effectively reduces the action space for a more compact grasp representation. (b) Grasp anchors and corresponding view scores during inference, illustrating the conditional view selection process. The model first samples the primary grasp view from the top candidate views, then samples the secondary grasp view via the conditional bi-view distribution. 

Specifically, we optimize the grasp parameters under joint limits, object contact constraints, and collision-free conditions. To enforce these constraints, we directly adopt the energy functions provided by cuRobo[48], including joint limitation energy, self-penetration energy, and inter-hand penetration energy. 

## **C Framework Details** 

### **C.1 Model Details** 

### **C.1.1 Grasp View** 

We uniformly sample _K_ grasp views on the upper hemisphere of a unit sphere and use these fixed directions as candidate grasp views. Specifically, each grasp view is represented as a unit vector **v** _i ∈_ R<sup>3</sup> pointing from the hemisphere surface to the object center. 

### **C.1.2 Scale-Adaptive Grasp Anchor** 

= Given a selected grasp view **v** , we construct a scale-adaptive grasp anchor _ganchor_ ( _tanchor, ranchor_ ). The translation component _tanchor_ is determined as the intersection point between the grasp view direction and the object’s minimum bounding sphere, ensuring that the anchor location adapts to the object scale. 

The rotation component _ranchor_ is defined by aligning the _x_ -axis of the grasp frame with the direction pointing toward the object center. The _z_ -axis is computed as the projection of the world _z_ -axis onto the plane orthogonal to the _x_ -axis, and the _y_ -axis is obtained accordingly to form a right-handed coordinate frame. This construction yields a unique and consistent grasp anchor frame for each grasp view. 

With the grasp anchor defined, a grasp pose ( _t, r_ ) expressed in the world coordinate system can be transformed into a relative representation (∆ _t,_ ∆ _r_ ) with respect to the anchor frame. Fig. 6(a) visualizes the distribution of grasp translation parameters represented in the world coordinate system and the anchor coordinate system, respectively. The results show that the proposed anchor-based formulation effectively reduces the action space, leading to a more compact and structured grasp representation. 

14 

### **C.1.3 Selection of Grasp View in Training and Inference Time** 

During training, we adopt a teacher-forcing strategy, where the ground-truth grasp views are directly used to construct the scale-adaptive grasp anchors. This stabilizes training and allows the model to focus on learning grasp generation conditioned on correct view information. 

During inference, the model first predicts the single-view probabilistic _{pi} ∈_ R<sup>_K_</sup> and the bi-view probabilistic _{p_<sup>_bi_</sup> _i,j_<sup>_} ∈_R</sup><sup>_K×K_.We select the top-</sup><sup>_k_views with the highest single-view probabilities</sup> (with _k_ = 5), apply temperature scaling with _τ_ = 0 _._ 1, and perform softmax sampling to obtain the primary grasp view index _i_ . Conditioned on the selected primary view, we extract the corresponding row _{p_<sup>_bi_</sup> _i,j_<sup>_}_from the bi-view probabilistic and apply the same top-</sup><sup>_k_sampling strategy to obtain the</sup> second grasp view index _j_ . The overall sampling process is illustrated in Fig. 6(b). In the example, the model first samples the primary grasp view from the top-scoring candidate views _{_ 5 _,_ 8 _,_ 10 _,_ 13 _,_ 15 _}_ and selects view 13. Subsequently, the conditional bi-view distribution _{p_<sup>_bi_</sup> 13 _,j_<sup>_}_is used to sample the second grasp view</sup> from _{_ 4 _,_ 6 _,_ 9 _,_ 12 _,_ 15 _}_ , resulting in the selection of view 12. 

### **C.2 Loss Function Details** 

We provide a detailed description of the loss functions used to train our framework. The overall training objective is defined as: 



where the details are as following: 

**Single-view Loss.** We supervise the predicted primary grasping view scores using a masked regression loss. Let _pi_ denote the predicted score for view **v** _i ∈V_ and _yi_ the ground-truth signal. The loss is defined as 



where _mi ∈{_ 0 _,_ 1 _}_ is a validity mask indicating whether view _i_ has supervision. 

**Bi-view Loss.** We supervise the predicted bi-view compatibility using a masked pairwise regression loss. Let _p_<sup>_bi_</sup> _i,j_<sup>denote the predicted compatibility score for view pair (</sup><sup>**v**</sup><sup>_i,_</sup><sup>**v**</sup><sup>_j_) and</sup><sup>_y_</sup> _i,j_<sup>_bi_the corresponding</sup> ground-truth signal. The loss is defined as 



where _mi ∈{_ 0 _,_ 1 _}_ is the validity mask applied to each row. 

**Parameter Loss.** We supervise the predicted bimanual dexterous grasp poses by minimizing the L2 distance between the predicted grasp parameters _Gpred_<sup>_bi_and the ground-truth grasp parameters</sup><sup>_G_</sup> _gt_<sup>_bi_:</sup> 



**Chamfer Loss.** We further impose a geometric consistency loss in 3D space. The predicted grasp parameters _Gpred_<sup>_bi_are converted into hand meshes via the dexterous hand model, from which surface</sup> point clouds _Ppred_ are sampled. Ground-truth point clouds _Pgt_ are obtained in the same way from _Ggt_<sup>_bi_.The Chamfer loss is defined as</sup> 



15 

**Physics-base Losses.** To ensure physical plausibility of the predicted grasps, we further introduce Physics-base losses to improve physical feasibility. The physics-based losses are: 



**Self-bi-penetration Loss.** We penalize self-collisions of inter-hands and intra-hands. Let _K_ = _{_ **k** _i}_<sup>_N_</sup> _i_ =1<sup>denote a set of predefined hand keypoints used for penetration avoidance (including both</sup> hands). We compute all pairwise distances and apply a soft penalty when the distance is smaller than a safety threshold _δ_ : 



This term discourages physically infeasible interpenetration between fingers and hands. 

**Hand–Object Penetration Loss.** To prevent the hand from penetrating into the object, we compute the signed distance _si_ from each hand surface keypoint **p** _i_ to the object surface, where _si >_ 0 indicates the point lies inside the object. The loss is defined as 



**Contact Loss.** To encourage hand–object contact, we pull predefined hand contact candidate points _C_ = _{_ **c** _i}_ toward the object surface point cloud _O_ . For each point, we compute the nearest-neighbor distance 



Only points within a threshold _τ_ are considered, and the loss is 



The weighting coefficients of the loss terms are set as follows: _λ_ single-view = 10 _._ 0, _λ_ bi-view = 1 _._ 0, _λ_ para = 15 _._ 0, _λ_ chamfer = 0 _._ 25, _λ_ physic = 1 _._ 0, _λ_ obj-pen = 100 _._ 0, _λ_ self-pen = 50 _._ 0, and _λ_ spf = 50 _._ 0. 

## **D Evaluation Metric Details** 

**Grasp Success Rate (SUC).** The hand executes a grasp from the pre-grasp pose _Gpre_<sup>_bi_to the squeeze</sup> pose _Gsqu_<sup>_bi_.A grasp is considered successful if the object’s translation and rotation remain within 5 cm</sup> and 15° for at least 3 seconds after execution. **SUC-F** evaluates force-closure success under external disturbances along six orthogonal directions. **SUC-L** evaluates lift success in a tabletop scenario with a floating hand. **SUC-A** evaluates lift success in a tabletop scenario with an arm-controlled hand. 

**Speed (S) and Success Generation Speed (SGS).** These measure the number of raw grasps and successful grasps synthesized per second, respectively. All numbers are obtained on a single NVIDIA GeForce RTX 3090 GPU, while baseline speeds are cited from their original reports. 

**Penetration Depth (PD).** The maximum intersection distance between the object mesh and the hand mesh. 

**Self-Penetration Depth (SPD).** The maximum penetration distance among all hand collision meshes, including both intra-hand and inter-hand self-penetrations. 

**Contact Distance Consistency (CDC).** The range between the maximum and minimum signed contact distances across all fingers, reflecting the uniformity of finger-object contacts. 

**Diversity (D).** The explained variance ratio of the first principal component from PCA applied to the generated grasp distribution, quantifying the concentration (and inversely, diversity) of bimanual grasps. 

16 

## **E Experiments of Data Synthesis** 

### **E.1 Qualitative Experiments of Region Selection** 

To validate the effectiveness of our region filtering strategy, we compare our method with random initialization. We randomly select 2,000 objects from DexGraspNet[10] and Objaverse[37], respectively. For each object, five region pairs are generated using our region generation method and random sampling, and five contact points are sampled within each region to compute the Q1 metric, which measures the distance between the Grasp Wrench Space (GWS) formed by the contact points and the origin, where a larger value indicates a more stable grasp. As shown in Table 7, our method consistently achieves higher Q1 values than random sampling on both datasets, demonstrating that the proposed region filtering strategy is more likely to produce stable grasp configurations and generalizes well across both structured and diverse object geometries. 

|Method|ours(DGN)|random(DGN)|ours(Objaverse)|random(Objaverse)|
|---|---|---|---|---|
|Q1(_×_10<sup>_−_2</sup>)|**1.25**|0.47|**1.41**|0.79|



Table 6: The region quality comparison between our method and random sample. The results demonstrate that our initialization strategy can initialize grasp region candidates with significantly higher quality. 



Figure 7: Visualization of extending our pipeline to cluttered scenes. 

### **E.2 Extension to Cluttered Scenes** 

Our pipeline can be readily extended to cluttered environments (Fig. 7). By incorporating additional collision constraints, the method is able to optimize collision-free grasps in complex, cluttered scenarios. 

### **E.3 More Visualization of Diverse Grasping on Data Generation** 

### **E.3.1 Visualization of other Dexterous Hands** 

Our data synthesis pipeline is not limited to a specific hand model and can be naturally extended to other dexterous hands. Fig. 8 visualizes grasp samples generated by applying our pipeline to the Leap Hand [49], demonstrating the generality of the proposed method across different dexterous hand embodiments. 



Figure 8: The visualization of the reslut of our data synthesis on LeapHand. Our data synthesis pipeline can be used for different dexterous hands. 

17 

### **E.3.2 Visualization of Grasps in our Dataset** 

We present a visualization of the grasps contained in our dataset in 9. These examples demonstrate that our dataset covers a wide range of object sizes and exhibits significant grasp diversity when objects are placed in identical poses on the tabletop. 



Figure 9: Visualization of the dataset diversity. The samples span multiple object scales and demonstrate diverse grasping poses even under identical object placements. 

## **F Experiments of Framework** 

### **F.1 Reproduction of SOTA method** 

**DGTR** [43] We utilize the original three independent MLP heads—responsible for predicting translation, rotation, and joint angles—by expanding their output dimensions to generate bimanual poses. The total loss is defined as the summation of the individual losses for both hands, with calculation metrics consistent with the original paper. Furthermore, we strictly adhere to the official three-stage training strategy. 

**SceneDiffuser** [17] We doubled the input and output dimensions of the SceneDiffuser model to represent both left- and right-hand grasping, while continuing to use the previous loss function. 

### **F.2 Efficiency Analysis of Framework** 

To further evaluate our model, we conduct ablation studies on inference time. We measure the inference time of a single batch with batch size 64 and compare our method against the DDPMBaseline (removes the BCM, GAF and SAGA component). To reduce measurement variance, we run each experiment for five epochs and report the mean and standard deviation. As shown in Table 7, and the results indicate that our method significantly improves the success rate at the cost of only a modest increase in inference time. 

### **F.3 Further Ablation of the Bimanual Coordination Module** 

We further conduct an ablation study on the bimanual coordination module to analyze the view sampling strategy. In our full model, the coordinated grasp views are sampled in a conditional manner. Specifically, we first sample the primary grasping view from the predicted single-view probabilistic 

18 

|Method|Average Inference Time (s)|Success Rate-Lift(%)|
|---|---|---|
|Baseline|1_._21_±_0_._03|41.17|
|Ours|1_._67_±_0_._05|61.93|



Table 7: Inference time comparison per batch. Our method achieves a good balance between model performance and efficiency. 

_pi_ . Given the sampled primary view, we then select the corresponding row from the predicted bi-view probabilistic _p_<sup>_bi_</sup> _i,j_<sup>and sample the second view conditioned on the primary one.</sup> 

For ablation, we remove this conditional sampling procedure and instead directly sample a single entry from the bi-view probabilistic _p_<sup>_bi_</sup> _i,j_<sup>.Inthiscase,thesampledindexjointlydeterminesthe</sup> primary and second grasping views without conditioning. Although this strategy treats the two hands in a fully symmetric manner, the results in Table 8 show a clear performance degradation across most metrics. This is because the conditional sampling in our design decomposes view selection into two sequential decisions, which is significantly easier than directly selecting a view pair from the full bi-view distribution, leading to more reliable bimanual coordination. 

|**Method**||**Met**|**rics**||
|---|---|---|---|---|
||SUC-L_↑_|PD_↓_|SPD_↓_|CDC_↓_|
|Direct Bi-view Sampling|45.49|2.23|**0.01**|2.96|
|Ours|**61.93**|**1.73**|0.02|**2.56**|



Table 8: Further Ablation of the Bimanual Coordination Module. This module can significantly improve the framework performance. 

### **F.4 Failure Case Analysis** 

As illustrated in Fig. 10 , failure cases primarily manifest as physical instability. Minor object penetration or floating grasps may occur when the generative model fails to perfectly balance the penetration penalty and contact supervision. Furthermore, as demonstrated in the rightmost case, a small number of objects undergo lateral sliding due to insufficient force closure, resulting in grasp failure. 



Figure 10: The visualization of failure cases. We find that the common failure cases are caused by object-hand penetration and non-contact. 

### **F.5 More Visulization of Generated Poses** 

In Fig. 11, we provide additional visualizations of the generated bimanual grasps on various objects. As observed, our framework consistently produces physically plausible and stable grasps, effectively adapting to objects with diverse geometric shapes and sizes. Furthermore, the model is capable of generating a rich variety of grasping postures for the same object, and the visualized results demonstrate distinct bimanual coordination. 

19 



Figure 11: The visualization of dexterous grasping generated by our model. 

## **G Real world Experiments** 

### **G.1 Real world Experiments Details** 

In this subsection, we describe the real-world experimental pipeline.For the single-view point cloud setting, we apply Grounded-SAM [44] to segment the object, and use the resulting mask to crop the object point cloud from the RGB-D frame as input to the model. For full points cloud setting, we first reconstruct the target object using a single-view 3D reconstruction method [45] and align the observed point cloud with the reconstructed mesh by matching their 3D bounding boxes to obtain the object scale. Next, we estimate the object 6D pose using 6D pose estimation [46] and we obtain the object point cloud input to our model by uniformly sampling points from the surface of the scaled mesh after world-frame pose transformation. 

We then convert the predicted Shadow Hand joint poses into the specific dexterous hand joint configuration via a hand-object consistent retargeting [6]. We define the pre-grasp pose by offsetting the final grasp pose along the hand’s negative approach direction (moving backward from the grasp along the hand-back/approach axis) by a fixed distance. 

During execution, as shown in Figure 12, the robot arm and hand first move from a predefined safe configuration to the pre-grasp pose. The system then commands the arm–hand to move from pre-grasp to the final grasp pose, and then to lift pose to complete the grasp. 

20 



<!-- Start of picture text -->
Initial State<br>Safe State<br>Pre-Grasp Pose<br>Grasp Pose<br>Lift Pose<br><!-- End of picture text -->

Figure 12: The visualization of real world execution. During execution, the robot arm and hand first move from a predefined safe configuration to the pre-grasp pose. The system then commands the arm–hand to move from pre-grasp to the final grasp pose, and then to lift pose to complete the grasp. 

21 

