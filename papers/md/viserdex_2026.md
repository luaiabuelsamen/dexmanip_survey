# ViserDex: **Vi** sual **S** im-to- **R** eal for Robust **Dex** terous In-hand Reorientation 

Arjun Bhardwaj<sup>1</sup> , Maximum Wilder-Smith<sup>1</sup> , Mayank Mittal<sup>1</sup><sup>_,_2</sup> , Vaishakh Patil<sup>1</sup> and Marco Hutter<sup>1</sup> 1ETH Zurich, 2NVIDIA 

Email: _{_ abhardwaj, mwilder, mittalma, patilv, mahutter _}_ @ethz.ch 



<!-- Start of picture text -->
Sim-Integrated 3D Gaussians Training Phases<br>Privileged Teacher Training<br>+<br>Teacher-Student Distillation<br>3D Gaussian Scene Parallelized  Pose Estimator Training<br>Object with Augmentations Physics Simulation Rasterization<br>Deployment Different Lighting Conditions Multiple Objects<br><!-- End of picture text -->

Fig. 1: We introduce a pipeline for training vision-based policies in simulation using 3D Gaussian Splatting. We successfully deploy these policies to the real world using a single monocular RGB camera, demonstrating robust in-hand reorientation of complex object geometries even under adversarial lighting conditions. 

**_Abstract_ —In-hand object reorientation requires precise estimation of the object pose to handle complex task dynamics. While RGB sensing offers rich semantic cues for pose tracking, existing solutions rely on multi-camera setups or costly ray tracing. We present a sim-to-real framework for monocular RGB in-hand reorientation that integrates 3D Gaussian Splatting (3DGS) to bridge the visual sim-to-real gap. Our key insight is performing domain randomization in the Gaussian representation space: by applying physically consistent, pre-rendering augmentations to 3D Gaussians, we generate photorealistic, randomized visual data for object pose estimation. The manipulation policy is trained using curriculum-based reinforcement learning with teacher–student distillation, enabling efficient learning of complex behaviors. Importantly, both perception and control models can be trained independently on consumer-grade hardware, eliminating the need for large compute clusters. Experiments show that the pose estimator trained with 3DGS data outperforms those trained using conventional rendering data in challenging visual environments. We validate the system on a physical multi-fingered hand equipped with an RGB camera, demonstrating robust reorientation of five diverse objects even under challenging lighting conditions. Our results highlight Gaussian splatting as a practical path for RGB-only dexterous manipulation. For videos of the hardware deployments and additional supplementary materials, please refer to the project website: https://rffr.leggedrobotics.com/works/viserdex/.** 

## I. INTRODUCTION 

Robotic dexterity requires not only grasping objects but also reorienting them within the hand into precise, functional poses. Deep Reinforcement Learning (DRL) has shown promise in acquiring such skills [2, 7]. However, existing methods often succeed only with visually simple objects, such as colored cubes, and struggle with realistic textures, complex shapes, and varied appearances. A major challenge is the perception–control gap: rapid in-hand motions create severe self-occlusions, making accurate object pose estimation from real sensors extremely difficult. Alternative sensing modalities, such as tactile arrays [18, 35], depth cameras [5], or multiview rigs [7], offer partial solutions but introduce instrumentation overhead, calibration complexity, or limited scalability. Consequently, sim-to-real dexterous control has often avoided relying primarily on monocular RGB camera observations, resulting in a perception–robustness bottleneck that constrains current approaches. 

A fundamental challenge in RGB-based manipulation lies in the simulation pipeline. Achieving the photorealism required for robust sim-to-real transfer via standard mesh-based ren- 

dering is computationally intractable for high-throughput RL training. Existing methods [27, 28] attempt to address this gap using high-fidelity visual simulation; however, generating sufficient visual diversity over days of training demands massive compute clusters, even for simple objects [7]. Explicit scene representations, particularly 3D Gaussian Splatting (3DGS) [10], enable real-time, photorealistic rendering that outperforms traditional mesh rasterization. Its compact and flexible scene representation allows efficient manipulation of scenes, making it ideal for RL tasks that require large-scale visual diversity. Despite these advantages, standard 3DGS is limited to static scenes and entangles illumination with geometry [10]. This prevents independent manipulation of lighting and material properties, which is a prerequisite for Domain Randomization (DR) that facilitates robust sim-to-real transfer. In this work, we investigate strategies to overcome these limitations to generate diverse, dynamic visual data for robust object pose estimation during dexterous manipulation. 

This paper proposes a monocular RGB-based training and deployment pipeline for robust in-hand reorientation of complex objects. The system is decomposed into two components: object pose estimation from RGB images as geometric keypoints, and an RL control policy that reorients the object to a desired goal pose. We integrate 3DGS directly into the simulation loop, overcoming the limitations of standard mesh-based rendering for high-throughput simulation-based training. Our key contribution is a suite of _pre-rasterization augmentations_ for Gaussian scenes. These augmentations generate consistent, diverse visual data and relax the static scene assumption of vanilla 3DGS. Furthermore, we simplify the RL process by replacing the extensive DR schemes used in previous works [1, 7] with a performance-based curriculum and a student-teacher distillation framework, substantially improving training efficiency. Notably, our pipeline enables learning complex manipulation behaviors using only a single consumergrade GPU. We validate this approach through zero-shot simto-real transfer on a 16-DoF Allegro Hand with a monocular RGB camera. Our approach demonstrates robust performance across five objects under both nominal and adversarial lighting conditions (shown in Fig. 1), achieving over 25 consecutive successful reorientations on average. 

## II. RELATED WORKS 

## _A. Sim-to-Real RL for In-Hand Manipulation_ 

In-hand manipulation tasks in sim-to-real RL can be categorized into two primitives: continuous in-hand rotation and goal-conditioned reorientation. Continuous rotation, where the objective is to spin an object around a canonical axis, has been demonstrated using proprioceptive and tactile feedback [20, 34, 35], as well as through repetitive open-loop finger gaits [3]. 

Goal-conditioned reorientation, in contrast, requires precise object state tracking and geometric reasoning to repose the object to the target configuration. Pitz et al. [18] propose a tactile-based object state estimator. While tactile sensing captures local geometry, it lacks a global reference frame, making their method susceptible to drift over long horizons 

and unable to resolve fine-grained features. Depth-based approaches [5] provide geometric structure but miss the semantic texture information needed to disambiguate the orientation of symmetric or visually complex objects. 

RGB vision provides dense semantic feedback useful for robust in-hand reorientation. Prior works [2, 7] have applied this modality to simple objects, such as colored cubes, but typically rely on multi-camera setups to handle occlusions. These methods also use computationally expensive Automatic Domain Randomization (ADR) [1] to bridge the sim-toreal gap, requiring large-scale compute clusters. While recent efforts improve training efficiency through student-teacher distillation [27], generating photorealistic visual data remains a bottleneck. Developing a monocular RGB-based framework that is both computationally efficient and generalizes to complex, real-world objects remains an open challenge. 

## _B. 3D Gaussian Splatting for Robotic Manipulation_ 

3D Gaussian Splatting (3DGS) [10] was developed for fast novel-view synthesis, generating photorealistic images from unseen viewpoints. Its rapid, high-fidelity reconstruction has been adopted in robotics for SLAM [13, 9], teleoperation [32, 11], and planning [6, 14]. The ability to easily capture and reconstruct arbitrary objects makes 3DGS a promising tool for reducing sim-to-real gaps in deploying visual policies. 

Methods such as SplatSim [21] leverage 3DGS to produce higher-fidelity observations than mesh-based renders, improving realism and reducing sim-to-real discrepancies in manipulation tasks. However, traditional 3DGS scenes are optimized for single objects or static scenes, which limits domain randomization on them. GSRL [30] addresses this by training a network to accelerate Gaussian generation across multiple scenes, and RL-GSBridge [33] and RoboGSim [12] combine physics-compatible meshes with high-quality Gaussian rendering for visual RL. RoboGSim further expands the training domain with a Scene Composer that randomizes objects, backgrounds, and viewpoints. Our work extends 3DGS by integrating it directly into a high-throughput simulation loop, combined with pre-rasterization augmentations. This approach addresses both visual realism and domain diversity challenges, paving the way for efficient sim-to-real transfer of dexterous manipulation policies. 

## III. METHOD 

We consider the problem of continuous, goal-conditioned in-hand object reorientation using a multi-fingered robotic hand observed only through a monocular RGB camera. From a control perspective, this task constitutes a Partially Observable Markov Decision Process (POMDP) with severe perceptual challenges. During manipulation, the object undergoes rapid motion, frequent self-occlusions by the fingers, and significant motion blur, making direct state estimation from RGB images highly unreliable. At the same time, learning the underlying dexterous manipulation skills requires accurate reasoning about object geometry and contact dynamics, which is difficult to acquire from raw visual input alone. 



<!-- Start of picture text -->
  Phase II:  Teacher-Student Distillation<br>Proprioceptive Exteroceptive Privileged Behaviour<br>Information Information Information Loss<br>Teacher<br>ãt at<br>  Phase I: Privileged Teacher Training Policy<br>Perception Student<br>PPOLoss GeneratorNoise Policy õexte<br>õpriv<br>Teacher at Rewards<br>Policy Reconstruction<br>Loss<br>Hidden State<br>  Phase IV: Deployment RGB    Phase III: Visual Pose Estimator Training<br>3D Gaussians Perturbed 3DG 3DGS Render Input RGB<br>Object<br>Segmentor Robot<br>Masked Augmentations Rasterization Masking<br>RGB<br>Pose<br>Estimator<br>(Object Pose) (Object Pose) (Robot Joint State)<br>Student Predicted  Pose<br>PD Controller ãt Policy Camera  Keypoints Estimator<br>Projection Prediction<br>Loss<br>Object Keypoints Projected Keypoints<br><!-- End of picture text -->

Fig. 2: Overview of our sim-to-real in-hand reorientation pipeline. We first train a teacher policy in simulation with full state access, then distill it into a recurrent student policy that operates from noisy observations. A monocular RGB pose estimator trained with 3D Gaussian Splatting data provides object poses to the student policy, enabling goal-conditioned dexterous manipulation on a real multi-fingered hand. 

A naive end-to-end approach that learns control directly from images must simultaneously solve three difficult problems: learn dexterous motor skills, infer hidden object state from partial observations, and overcome the visual sim-to-real gap. Jointly optimizing these objectives with reinforcement learning is challenging and sample inefficient. Instead, we follow a principled decomposition that addresses each challenge in a separate phase: 

- 1) **Teacher Training using RL:** We first train a teacher policy in simulation with full state access using reinforcement learning. This stage focuses solely on acquiring the geometric and contact-rich manipulation skills required for reorientation. 

- 2) **Student Distillation:** We distill the teacher into a recurrent student policy that learns to infer the underlying system state from noisy, real-world observations. 

- 3) **Visual Pose Estimator Training:** We train a monocular RGB pose estimator using synthetic images rendered from a 3D Gaussian Splatting representation of the object. By performing domain randomization directly in the Gaussian space prior to rendering, we generate photorealistic and diverse training data that significantly reduces the visual sim-to-real gap. 

At deployment, we predict object pose estimates from RGB images, which are fed to the recurrent student policy to produce goal-conditioned actions on the real robot. This modular design enables efficient training on consumer-grade hardware. An overview of the pipeline is shown in Fig. 2. 

_A. Teacher Training using Reinforcement Learning_ 

- _1) MDP Formulation:_ We formulate the reorientation task 

- as a goal-conditioned MDP, and train a policy _πθ_ ( _at|ot, gt_ ) 

to rotate the object to a target orientation _gt ∈_ SO(3) using PPO [25]. The policy commands the robot’s joint position targets _at ∈_ R<sup>16</sup> . The agent receives a dense reward for aligning the object with the goal, a sparse success bonus, and penalties that encourage smooth actions. Upon reaching a goal, a new target is sampled. Episodes terminate if the object is dropped or if no goals are achieved within a specified time window. Additional details are provided in the Appendix. 

_2) Observations:_ We divide the observation space _O_ into three groups: _proprioceptive_ , _exteroceptive_ , and _privileged_ . Proprioceptive observations _O_ prop consist of robot’s joint positions, action history from the last four steps, the current object goal, and the remaining episode time. Exteroceptivederived observations _O_ exte provide the object’s current pose in the hand frame and its orientation relative to the goal. Privileged observations _O_ priv is available only to the teacher policy and contain ground-truth state information, including the object’s velocity, robot’s fingertip contact forces, and randomized physical properties ( _e_ . _g_ ., object mass and scale). 

_3) Performance-based Curriculum:_ Prior work on in-hand reorientation [1, 7] uses ADR over many environment parameters, which is computationally expensive. Instead, we propose a lightweight, performance-driven curriculum [17] that increases the task complexity according to the agent’s average consecutive success count. The curriculum has three complementary components. First, we gradually increase the regularization penalties, allowing the policy to prioritize task completion before refining smoothness and efficiency. Second, we incrementally increase the random action latency to prepare the agent for asynchronous delays on real hardware. Finally, we also progressively narrow the allowed time window between consecutive successes, encouraging more efficient 

object reorientation. Each curriculum component scales with the moving average of consecutive successes over all the environments. Together, these mechanisms improve sample efficiency and stabilize training, shown later in Section IV-C. 

## _B. Student Training using Distillation_ 

The RL policy from the previous phase has access to privileged signals, which are unavailable during deployment. We therefore distill it into a student policy which receives noisy proprioception _o_<sup>noisy</sup> prop and noisy exteroceptive _o_<sup>noisy</sup> exte observations. To handle partial observability, we parameterize the student as a recurrent network with a belief encoder [15], allowing it to implicitly infer the system state. 

_1) Perception Noise Generator:_ Inspired by [7], we corrupt simulated object pose observations with four perturbations. We apply temporal downsampling to simulate low frame rates, stochastic jitter to model variable latency, systematic bias for calibration errors, and inject random poses for occasional tracking failures. This realistic noise improves student policy robustness and facilitates effective sim-to-real transfer. 

_2) Student Policy Architecture:_ The student policy uses a _belief encoder-decoder_ network architecture, previously applied in perceptive locomotion [15]. At each timestep, = the recurrent encoder updates a latent belief state _z fϕ_ ( _o_ prop<sup>noisy</sup><sup>_, o_</sup> exte<sup>noisy).Duringtraining,thebeliefdecodernet-</sup> work reconstructs the teacher’s observations (˜ _o_ exte _,_ ˜ _o_ priv) = _hψ_ ( _z, o_ exte<sup>noisy). The encoder-decoder is trained with a reconstruc-</sup> tion loss _L_ recon( _ϕ, ψ_ ), which penalizes errors in reconstructing the privileged and exteroceptive information. This encourages the latent _z_ to capture the structure necessary to combine noisy inputs and compensate for partial observability. 

The control head outputs the actions ˜ _a_ = _gρ_ ( _z, o_ prop<sup>noisy</sup><sup>_, o_</sup> exte<sup>noisy),</sup> supervised with a behavior cloning loss _L_ BC( _ϕ, ρ_ ), that minimizes the L2 distance between the student and teacher actions. We train the student policy end-to-end using a composite loss function _L_ = _L_ BC + _λL_ recon and employ an online variant of DAgger [23] detailed in the Appendix. 

## _C. Visual Object Representation and Augmentations_ 

The student policy’s exteroceptive input requires object pose estimates from RGB images. A key challenge in training a robust perception model for this task is generating diverse visual data that handles lighting variations and heavy occlusions. To avoid the computational overhead of ray-tracing in simulators, we integrate Gaussian Splatting rasterization into the simulation loop. 

_1) 3D Gaussian Object Representation:_ We represent object geometry and appearance using 3DGS [10]. The object is represented by a set of 3D Gaussians, each characterized by a position, covariance, opacity, and spherical harmonic (SH) coefficients [24]. To capture view-dependent effects, the color _c_ ( **d** ) along the viewing direction **d** is computed by spherical harmonics up to degree _L_ = 3: 







<!-- Start of picture text -->
Base Random Spatial Color Global<br><!-- End of picture text -->

Fig. 3: Pre-rasterization augmentation examples. Visualizations of the proposed SH-based perturbations applied to clustered Gaussians, producing structured variations in color, reflectance, and spatial appearance without ray-tracing. 

where _kℓ_<sup>_m_</sup> are the learned coefficients. The 0<sup>_th_</sup> -order coefficients (SH0) capture view-independent Lambertian base colors, while the higher-order coefficients (SHN) encode highfrequency specular effects. 

_2) Simulation-Integrated GS Rendering:_ During in-hand manipulation, the camera is fixed while the object moves due to robot interactions. To render the moving object with 3DGS, we apply the inverse of the object’s transform to the camera and produce RGB and depth _D_ splat. This transformation keeps the scene as static, satisfying the assumptions of vanilla 3DGS, while producing images that reflect changing object poses. However, the object-centric rendering ignores occlusions from the robot’s fingers. To restore physical consistency, we generate a depth map of the hand _D_ phys from the same viewpoint using a low-fidelity depth raycaster within the physics simulator. We mask out pixels in the RGB image where the hand is in the front ( _D_ phys _< D_ splat). This aligns visual observations with the simulation state without full-scene ray-tracing. 

_3) Pre-Rasterization Augmentations:_ Strategies for generating diverse visual data typically fall into two categories. First, _post-process image augmentations_ ( _e_ . _g_ ., color jitter, brightness), which are computationally cheap but apply global 2D transformations that disregard 3D geometry. Second, _scene parameter randomizations_ (domain randomization) [28] alter lighting and materials during rendering but require computationally expensive ray-tracing. 

We propose a hybrid approach termed _pre-rasterization augmentation_ , which leverages the explicit nature of the 3D Gaussian representation. We operate directly on the Gaussian attributes, specifically the Spherical Harmonic (SH) coefficients, before rasterization. This provides fine-grained control over scene appearance without the cost of full scene raytracing. Na¨ıvely randomizing individual Gaussians, however, breaks photometric consistency, producing high-frequency noise rather than realistic lighting variations. To generate diverse yet plausible data, we exploit the fact that lighting and material changes are inherently structured, typically affecting spatially proximal regions or specific materials uniformly. We therefore cluster Gaussians based on geometric or photometric correlations and perturb each cluster as a group. These perturbations include additive and scaling noise on the base color (SH0) and specular components in higher-order SH 

TABLE I: Pre-Rasterization Augmentation Parameters 

|**Augmentation**|**Targets**|**Probability**|**Fraction**|**Range**|Cube|
|---|---|---|---|---|---|
|**RANDOM NOISE**|||||3D Printed Toy|
|Additive|SH0, SHN|0.2|1.0|[_−_0_._1_,_0_._1]|Camera|
|Scaling|SH0, SHN|0.2|1.0|[0_._8_,_1_._2]|Light<br>|
|**SPATIAL CLUSTER**|||||Rubber Duck<br>|
|Additive|SH0, SHN|0.8|0.10|[_−_0_._1_,_0_._1]||
|Scaling|SH0, SHN|0.8|0.20|[0_._9_,_1_._1]|Tablet Bottle|
|**COLOR CLUSTER**|||||Hand|
|Additive|SH0|0.8|0.10|[_−_0_._2_,_0_._2]||
|Additive|SHN|0.8|0.10|[_−_0_._1_,_0_._1]|Globe|
|Scaling|SH0, SHN|0.8|0.10|[0_._6_,_1_._4]||
|**GLOBAL SHIFT**<br>Additive|SHN|0.2|1.0|[_−_0_._1_,_0_._1]|Fig. 4: Left: The experimental setup with an RGB camera, an Allegr<br>Hand, and a multi-colored light source for adversarial lighting. Right<br>i|
|Scaling|SH0, SHN|0.2|1.0|[0_._6_,_1_._4]|The object set displayed under normal lighting (first column) an|
|Uniform Additive|SH0, SHN|0.8|1.0|[_−_0_._2_,_0_._2]|adversarial lighting (second column).|
|Uniform Scaling|SH0|0.8|1.0|[0_._9_,_1_._4]||



Fig. 4: Left: The experimental setup with an RGB camera, an Allegro Hand, and a multi-colored light source for adversarial lighting. Right: The object set displayed under normal lighting (first column) and adversarial lighting (second column). 

## _D. Visual Object Pose Estimator Training_ 

coefficients (SHN). They are summarized as follows: 

- **Random Noise Group:** We apply random perturbations to each Gaussian independently. This unstructured randomization effectively simulates high-frequency sensor noise, pixel-level artifacts, and minor mesh imperfections. 

- **Spatial Cluster Group:** Real-world variations such as shadows, damage, and marks are often localized in a small region on the object. To mimic this effect, we cluster Gaussians by spatial location into 64 clusters using k-means. Perturbing these spatially contiguous clusters simulates local inconsistencies and patch-level noise. 

- **Color Cluster Group:** Objects are often composed of distinct materials that interact differently with light. Assuming that these material properties correlate with diffuse color, we cluster Gaussians based on their 0<sup>_th_</sup> order spherical harmonic (SH0) into 32 clusters. Perturbing these clusters simulates material-specific shifts, such as albedo modifications or reflectance changes, across photometrically similar regions. 

- **Global Shift Group:** To simulate macro-level environmental changes, we treat the entire scene of Gaussians as a single cluster. We apply global shifts and scaling to the color attributes, where noise is sampled either independently per dimension or as a single value (Uniform) for the entire vector. These perturbations effectively replicate environmental variations such as ambient brightness, color temperature, camera exposure, and saturation. 

Each Gaussian scene is preprocessed to identify the cluster indices for these strategies. During visual data generation, we sequentially apply stochastic variations to the SH coefficients, allowing different visual perturbations to compound. This produces a diverse set of scene appearances from a single static representation, as shown in Fig. 3. Table I summarizes the augmentation types and parameters. Each augmentation is applied with a specified probability, and only a fraction of the clusters are perturbed at a time. Despite their distinct semantic targets ( _e_ . _g_ ., spatial vs. color), the procedural logic for applying any augmentation layer is consistent. 

We train a keypoint-based pose estimator to recover the object pose from RGB images, thereby providing the exteroceptive input required by the student policy during real-world deployment. The training dataset is generated by rolling out the expert teacher policy within the simulation and rendering the RGB images through our 3DGS pipeline with pre-rasterization augmentation strategies. This process results in a large-scale, annotated dataset with ground-truth object poses. To improve robustness to real-world sensor imperfections, we apply random ISO noise and motion blur to the images during training. 

The pose estimator uses a ResNet-34 [8] backbone, initialized with ImageNet-pretrained weights. The network is trained to regress a set of nine keypoints, corresponding to the eight object-specific points plus the geometric centroid. For each keypoint, the network predicts the normalized 2.5D coordinates ( _u, v, d_ ), where ( _u, v_ ) represent the normalized pixel coordinates in the image plane and _d_ represents the metric depth. The predicted 2.5D keypoints can be resolved to a 6D object pose via the Rigid Procrustes algorithm [29]. 

## _E. Experimental Setup_ 

We consider a 16-DOF Allegro Hand with a wrist-mounted Intel RealSense D435i camera for visual feedback, as shown in Fig. 4. We deploy all models on a single workstation with an Intel Core i9 CPU and NVIDIA RTX 6000 Ada GPU. The policy infers at 30 Hz and outputs the joint position targets that are tracked by a low-level joint PD controller at 300 Hz. Since the learned pose estimator relies on segmented object inputs, we fine-tune SAM2 [22] per object to generate precise object masks in real-time. 

We evaluate our system on five objects (see Fig. 4) exhibiting diverse geometric and physical properties, spanning primitives shapes ( _Cube_ , _Globe_ ) to complex, non-convex items ( _Tablet Bottle_ , _3D Printed Toy_ , _Rubber Duck_ ). For these objects, high-fidelity meshes are obtained using Polycam [19]. These are then rendered in NVIDIA Isaac Lab [16] to generate pose-annotated images for Gaussian Splatting. For each object, we train a pose estimator and control policy in NVIDIA Isaac Lab. Additional training details are provided in the Appendix. 

We consider two lighting regimes: nominal (white distant light) and adversarial (low-illumination point sources with dynamic hue shifts). As shown in Fig. 4, adversarial conditions present significant visual challenges, including low contrast, specular highlights, and strong color casts, providing a rigorous test of system robustness. 

## IV. RESULTS 

## _A. Pose Estimation using Different Rendering Pipelines_ 

To evaluate our pose estimation pipeline, we create a realworld test set for each object using FoundationPose [31] as a ground-truth pose labeler. To ensure high-quality labels, we provide FoundationPose with privileged inputs, including object masks, CAD meshes, and high-resolution RGB-D images, and perform multiple refinement iterations. We discard frames where the rendered pose does not visually align with the input image. Additional details on test dataset is in the Appendix. 

We evaluate our proposed pose estimator training pipeline against three baselines, keeping network architecture, training hyperparameters, and dataset sizes constant. The baselines differ solely in their image generation approach: 

- 1) _Standard Tiled Rendering:_ Isaac Lab’s default RTX renderer combined with standard post-process image augmentations. 

- 2) _Domain Randomized (DR) Tiled Rendering_ : Extends the above with randomized scene attributes (background HDRI lighting, material properties such as albedo tint, roughness, and metallic). We use the randomization parameters for material and background from [27]. 

- 3) _Na¨ıve Gaussian Splatting:_ Our GS-based pipeline without pre-rasterization augmentations, and using only standard post-process image augmentations. 

All methods use the same source meshes for geometrybased rendering and Gaussian Splat scene optimization to ensure a fair comparison. We report the Average Distance of Model Points (ADD) and a prediction accuracy metric (error _<_ 10mm and _<_ 10<sup>_◦_</sup> ), averaged over five training seeds. 

_a) Nominal Conditions:_ Table II details the pose estimation results under nominal lighting. Our method achieves the highest overall performance with a mean accuracy of 65 _._ 4% and a mean ADD of 10 _._ 2 mm, surpassing standard tiled rendering (53 _._ 3%) and the randomized tiled baseline (55 _._ 6%). While geometrically simple objects ( _e_ . _g_ ., _Cube_ ) show similar performance across methods, our approach yields the largest gains on geometrically and texturally complex objects, such as the _3D Printed Toy_ (+24% improvement over randomized tiled rendering) and the _Rubber Duck_ . 

_b) Adversarial Conditions:_ Under adversarial lighting, the performance differences between methods become even more pronounced (see Table II). Our method demonstrates superior robustness, with a mean accuracy of **56** _._ **3** %, significantly outperforming the strongest baseline, Randomized Tiled Rendering (47 _._ 2%). A critical observation is that the weak performance of the Na¨ıve GS baseline achieves only 36 _._ 5% accuracy. Since this baseline uses the same underlying 

rendering engine but lacks our specific randomization strategy, this failure highlights that high-fidelity rendering alone is insufficient for generalizing to out-of-distribution visual domains. In contrast, our approach leverages explicit control over scene attributes to generate diverse, challenging training samples. By tailoring these pre-rasterization augmentations to simulate physical lighting variations, which standard 2D image augmentations fail to capture, we maintain performance even in difficult visual scenarios. 

_c) Computational Efficiency:_ Beyond data quality, our integrated 3DGS pipeline provides significant computational advantages over standard rendering solutions. Compared to Isaac Lab’s tiled renderer, it achieves a 1.6 _×_ faster rendering throughput on an RTX 6000 Ada. Furthermore, it is substantially more memory-efficient: rendering a batch of 1,024 environments consumes only 12 GB of VRAM, compared to the prohibitive 34 GB required by the tiled renderer. Critically, our proposed pre-rasterization augmentations introduce negligible overhead, executing in less than 2 ms per batch, and representing only _≈_ 4% of the total frame rendering time. 

## _B. Effect of Pre-Rasterization Augmentations_ 

To isolate the contributions of the pre-rasterization augmentations introduced in Section III-C3, we perform a “leave-oneout” ablation study. For each experiment, a pose estimator is trained with data generated with one augmentation group (defined in Table I) removed and evaluated against the full pipeline. Results on the nominal and adversarial test set are reported in Table III. 

_a) Nominal Conditions:_ We observe that the complete augmentation pipeline yields the highest overall robustness. The removal of localized augmentations, specifically _Random Noise_ and _Structured Clustering_ (Means/SH0), results in moderate performance dips (the accuracy dropping to 57-59%). This suggests that while fine-grained perturbations refine the decision boundary, they are not the sole drivers of performance under nominal conditions, where lighting is relatively standard. 

However, a critical insight emerges from the exclusion of _Global Shift_ augmentations. Removing these environmental perturbations causes a significant performance collapse, with mean accuracy dropping to 51 _._ 2% and ADD error nearly doubling to 16 _._ 9 mm. This degradation is particularly acute for the _Tablet Bottle_ , which has reflective surfaces. This indicates that even under ”nominal” real-world conditions, simulating global variations in exposure, color temperature, and ambient intensity is essential for bridging the sim-to-real gap. 

_b) Adversarial Conditions:_ First, removing _Random Noise_ results in a comparatively moderate performance drop (Mean Accuracy: 48 _._ 6%), suggesting that while unstructured noise aids general robustness, it is not the primary driver of feature learning. In contrast, omitting the structured augmentations leads to significant degradation. The removal of _Spatial Clustering_ (3D means) and _Color Clustering_ (SH0) drops accuracy to 42 _._ 5% and 44 _._ 7%, respectively, validating that correlated perturbations are essential for modeling localized effects. Most critically, the exclusion of _Global Shift_ 

TABLE II: Evaluation of learned pose estimator on real-world data under nominal and adversarial lighting. Our method is compared against three baselines: _Standard Tiled_ , _Randomized Tiled_ , and _Naive GS_ rendering. We report Average Distance of Model Points (ADD) in mm and a strict accuracy metric ( _<_ 10mm and _<_ 10<sup>_◦_</sup> ), averaged over 5 random seeds. 

|**Objects**|**Cu**|**be**|**3D Prin**|**ted Toy**|**Rubbe**|**r Duck**|**Tablet **|**Bottle**|**Glo**|**be**|**M**|**ean**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Method**|ADD|Accuracy|ADD|Accuracy|ADD|Accuracy|ADD|Accuracy|ADD|Accuracy|ADD|Accuracy|
||||||**NOMI**|**NAL CONDITIO**|**NS**||||||
|Standard Tiled<br>DR Tiled<br>Na¨ıve GS<br>Ours|11_._9_±_0_._86<br>10_._5_±_0_._75<br>10_._4_±_1_._35<br>**9**_._**1**_±_**0**_._**51**|57_._2_±_8_._13<br>69_._7_±_9_._05<br>59_._0_±_4_._66<br>**73**_._**1**_±_**4**_._**73**|14_._1_±_0_._92<br>15_._9_±_0_._64<br>18_._7_±_0_._95<br>**11**_._**3**_±_**0**_._**82**|37_._7_±_2_._84<br>32_._5_±_2_._78<br>23_._3_±_3_._18<br>**56**_._**5**_±_**5**_._**77**|9_._5_±_0_._23<br>9_._1_±_0_._23<br>11_._4_±_0_._26<br>**7**_._**9**_±_**0**_._**24**|67_._0_±_1_._47<br>73_._7_±_2_._22<br>44_._3_±_4_._88<br>**78**_._**0**_±_**3**_._**97**|10_._0_±_0_._65<br>**9**_._**0**_±_**0**_._**52**<br>11_._2_±_0_._63<br>10_._2_±_0_._84|45_._7_±_4_._78<br>50_._7_±_3_._56<br>48_._3_±_4_._59<br>**51**_._**7**_±_**5**_._**06**|15_._0_±_2_._41<br>16_._7_±_1_._20<br>20_._2_±_1_._45<br>**12**_._**3**_±_**0**_._**89**|59_._1_±_3_._68<br>51_._3_±_4_._21<br>17_._2_±_4_._61<br>**67**_._**7**_±_**3**_._**06**|12_._1_±_1_._01<br>12_._2_±_0_._67<br>14_._4_±_0_._93<br>**10**_._**2**_±_**0**_._**66**|53_._3_±_4_._18<br>55_._6_±_4_._36<br>38_._4_±_4_._38<br>**65**_._**4**_±_**4**_._**52**|
||||||**ADVERS**|**ARIAL CONDI**|**TIONS**||||||
|Standard Tiled<br>DR Tiled<br>Na¨ıve GS<br>Ours|12_._6_±_0_._74<br>11_._5_±_0_._89<br>14_._3_±_0_._85<br>**10**_._**6**_±_**0**_._**38**|56_._8_±_4_._83<br>57_._6_±_4_._69<br>44_._3_±_2_._30<br>**60**_._**6**_±_**5**_._**47**|20_._3_±_2_._10<br>**13**_._**8**_±_**0**_._**54**<br>21_._9_±_0_._85<br>14_._4_±_0_._77|29_._1_±_7_._05<br>39_._0_±_2_._54<br>27_._9_±_4_._85<br>**45**_._**9**_±_**4**_._**58**|15_._6_±_0_._86<br>**11**_._**5**_±_**0**_._**61**<br>13_._9_±_1_._25<br>12_._2_±_0_._53|51_._3_±_4_._52<br>57_._7_±_3_._89<br>57_._3_±_4_._29<br>**62**_._**7**_±_**3**_._**09**|24_._1_±_1_._58<br>14_._4_±_1_._68<br>22_._1_±_1_._39<br>**13**_._**5**_±_**0**_._**99**|25_._0_±_3_._95<br>39_._1_±_5_._14<br>25_._0_±_3_._35<br>**46**_._**5**_±_**3**_._**43**|18_._7_±_2_._04<br>18_._6_±_1_._07<br>21_._0_±_1_._52<br>**13**_._**8**_±_**0**_._**78**|41_._9_±_2_._68<br>42_._7_±_4_._44<br>28_._1_±_5_._95<br>**65**_._**6**_±_**2**_._**52**|18_._3_±_1_._46<br>14_._0_±_0_._96<br>18_._6_±_1_._17<br>**12**_._**9**_±_**0**_._**69**|40_._8_±_4_._61<br>47_._2_±_4_._14<br>36_._5_±_4_._15<br>**56**_._**3**_±_**3**_._**82**|



TABLE III: Ablation study of pre-rasterization augmentations under nominal and adversarial conditions for pose estimation. We compare our method with models trained with specific augmentation groups removed. We report Average Distance of Model Points (ADD) in mm and a strict accuracy metric ( _<_ 10mm and _<_ 10<sup>_◦_</sup> ), averaged over 5 random seeds. 

|**Objects**|**Cub**|**e**|**3D Prin**|**ted Toy**|**Rubbe**|**r Duck**|**Tablet **|**Bottle**|**Glo**|**be**|**M**|**ean**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Method**|ADD|Accuracy|ADD|Accuracy|ADD<br>**NOMINA**|Accuracy<br>**L CONDITIONS**|ADD|Accuracy|ADD|Accuracy|ADD|Accuracy|
|w/o Random Noise<br>w/o Spatial Clustering<br>w/o Color Clustering<br>w/o Global Shift<br>Ours|11_._9_±_3_._24<br>9_._2_±_0_._91<br>9_._2_±_0_._41<br>11_._2_±_1_._26<br>**9**_._**1**_±_**0**_._**51**|61_._5_±_11_._21<br>**74**_._**9**_±_**8**_._**49**<br>71_._0_±_5_._94<br>67_._2_±_3_._85<br>73_._1_±_4_._73|13_._5_±_1_._14<br>12_._9_±_0_._86<br>13_._6_±_1_._60<br>**10**_._**9**_±_**1**_._**13**<br>11_._3_±_0_._82|37_._2_±_9_._13<br>44_._7_±_7_._06<br>49_._4_±_2_._42<br>55_._7_±_6_._58<br>**56**_._**5**_±_**5**_._**77**|8_._2_±_0_._39<br>8_._0_±_0_._22<br>8_._2_±_0_._59<br>9_._1_±_0_._41<br>**7**_._**9**_±_**0**_._**24**|**80**_._**9**_±_**2**_._**88**<br>73_._5_±_3_._27<br>77_._4_±_5_._64<br>70_._9_±_3_._85<br>78_._0_±_3_._97|10_._7_±_0_._84<br>16_._3_±_1_._38<br>20_._4_±_0_._56<br>39_._5_±_2_._84<br>**10**_._**2**_±_**0**_._**84**|46_._7_±_3_._33<br>39_._3_±_5_._64<br>34_._3_±_4_._03<br>10_._3_±_2_._45<br>**51**_._**7**_±_**5**_._**06**|14_._5_±_1_._17<br>13_._8_±_2_._15<br>14_._5_±_1_._69<br>13_._9_±_0_._25<br>**12**_._**3**_±_**0**_._**89**|66_._5_±_5_._32<br>51_._3_±_5_._73<br>64_._8_±_3_._09<br>52_._1_±_5_._17<br>**67**_._**7**_±_**3**_._**06**|11_._8_±_1_._36<br>12_._0_±_1_._10<br>13_._2_±_0_._97<br>16_._9_±_1_._18<br>**10**_._**2**_±_**0**_._**66**|58_._6_±_6_._37<br>56_._7_±_6_._04<br>59_._4_±_4_._22<br>51_._2_±_4_._38<br>**65**_._**4**_±_**4**_._**52**|
||||||**ADVERSAR**|**IAL CONDITIO**|**NS**||||||
|w/o Random Noise<br>w/o Spatial Clustering<br>w/o Color Clustering<br>w/o Global Shift<br>Ours|13_._2_±_0_._77<br>13_._5_±_1_._40<br>14_._4_±_0_._68<br>24_._9_±_1_._29<br>**10**_._**6**_±_**0**_._**38**|49_._7_±_5_._46<br>46_._2_±_7_._00<br>47_._3_±_6_._63<br>17_._8_±_3_._16<br>**60**_._**6**_±_**5**_._**47**|15_._8_±_1_._34<br>16_._4_±_1_._20<br>16_._7_±_1_._60<br>22_._0_±_1_._54<br>**14**_._**4**_±_**0**_._**77**|40_._7_±_4_._62<br>39_._3_±_7_._13<br>41_._2_±_4_._03<br>25_._4_±_2_._54<br>**45**_._**9**_±_**4**_._**58**|12_._9_±_0_._39<br>14_._0_±_0_._69<br>14_._8_±_0_._80<br>20_._0_±_1_._89<br>**12**_._**2**_±_**0**_._**53**|52_._7_±_4_._29<br>51_._7_±_4_._22<br>46_._7_±_3_._16<br>27_._7_±_1_._70<br>**62**_._**7**_±_**3**_._**09**|13_._9_±_0_._78<br>17_._6_±_0_._84<br>19_._9_±_1_._15<br>30_._2_±_1_._63<br>**13**_._**5**_±_**0**_._**99**|41_._5_±_1_._10<br>35_._6_±_3_._00<br>29_._4_±_4_._46<br>12_._6_±_2_._39<br>**46**_._**5**_±_**3**_._**43**|16_._3_±_0_._86<br>16_._2_±_1_._59<br>16_._2_±_1_._46<br>17_._5_±_0_._52<br>**13**_._**8**_±_**0**_._**78**|58_._4_±_3_._83<br>39_._6_±_5_._92<br>58_._9_±_3_._93<br>34_._4_±_2_._42<br>**65**_._**6**_±_**2**_._**52**|14_._4_±_0_._83<br>15_._5_±_1_._14<br>16_._4_±_1_._14<br>22_._9_±_1_._37<br>**12**_._**9**_±_**0**_._**69**|48_._6_±_3_._86<br>42_._5_±_5_._45<br>44_._7_±_4_._44<br>23_._6_±_2_._44<br>**56**_._**3**_±_**3**_._**82**|
|<br>No Cu|rriculum|w/o A|ction Latenc|y Curriculu|m<br>w|/o Penalty C|urriculum|w/o|Time Window|Curriculum|O|urs|
|25<br>esses<br>Cu|be|25|3D Printed|Toy<br>|20<br>Ru|bber Duck|30|Tablet|Bottle|50|Globe||
|0<br>5<br>10<br>15<br>20<br>Consecutive Succ||0<br>5<br>10<br>15<br>20|||0<br>5<br>10<br>15||0<br>5<br>10<br>15<br>20<br>25|||0<br>10<br>20<br>30<br>40|||
|0<br>1000<br>200<br>Training I<br>Avg.|0<br>3000<br>40<br>terations|00<br>0<br>|1000<br>2000<br>Training Iterat|3000<br>4000<br>ions|0<br>1000<br>Train|2000<br>3000<br>ing Iterations|4000<br>0|1000<br>200<br>Training I|0<br>3000<br>40<br>terations|00<br>0<br>100<br>Tra|0<br>2000<br>ining Iterat|3000<br>4000<br>ions|



Fig. 5: Impact of performance-based curricula on training efficiency. Curves show learning progress for full curriculum compared with ablations with individual components removed. Note that _No Curriculum_ and _w/o Penalty Curriculum_ coincide at zero. 

augmentations causes a catastrophic collapse in performance, with mean accuracy plummeting to just 23 _._ 6%. This underscores that simulating macro-level environmental changes is the single most important factor for generalizing to diverse real-world lighting conditions. 

## _C. In-hand Reorientation Policy Learning_ 

_1) Resource-Efficient Policy Training:_ The teacher RL training phase learns in-hand manipulation skills efficiently, scaling across diverse object geometries while using minimal GPU resources. Policies are trained using 24,576 parallel environments. For primitive geometries ( _e_ . _g_ ., the Cube), the training converges in 26 hours on a single consumer-grade NVIDIA RTX 4090 (24GB VRAM). More complex objects are trained on a dual-GPU setup, requiring 30 GB VRAM and converging in roughly 90 hours due to the increased simulation fidelity of complex contact geometry. The subsequent student-teacher distillation phase completes in 16 hours for 4 _,_ 096 environments on a single NVIDIA RTX 4090 GPU. 

Compared to prior work [7], which requires eight A40 GPUs over 60 hours, our pipeline achieves an order-of-magnitude improvement in VRAM efficiency and substantially reduced training time, making high-fidelity RL more accessible for real-world robotics. 

_2) Impact of Performance-based Curriculum:_ We evaluate the sample efficiency of our performance-based curriculum by selectively enabling different curriculum components (Section III-A3). Fig. 5 reports the consecutive successes averaged across all environments during training. Applying all the curriculum components leads to the fastest convergence and highest CS. Removing either the _Action Latency_ or _Time Window_ components significantly slows learning, particularly for complex geometries such as the _3D Printed Toy_ and _Rubber Duck_ . Removing the _Regularization Penalty_ curriculum causes complete failure, since the policy becomes more conservative and deprioritizes task completion. Similarly, having no curriculum also yields near-zero success. Beyond accelerating convergence, the curriculum also acts as a self-regulating 



<!-- Start of picture text -->
Target Time<br><!-- End of picture text -->

Fig. 6: Rollout sequence of the hand reorienting an object to the target pose. The images are from the robot camera feed. 

mechanism for reward balancing, eliminating the need for perobject tuning. All teacher RL training and student distillation experiments use the same reward weights and hyperparameters across objects, demonstrating the approach’s generality. 

## _D. Hardware Deployment_ 

Similar to the pose estimation experiments, we validate the sim-to-real deployment of the in-hand reorientation system under nominal and adversarial lighting, as shown in Fig. 6. Consistent with prior work [2, 7], we define successful inhand reorientation when the object orientation error is within 0 _._ 4 radians. We measure _consecutive successes_ (CS), _i_ . _e_ ., , the number of goals reached before a failure occurs (object falls out of the hand). Table IV reports the consecutive successes (CS) averaged over five runs per object and lighting condition. 

_a) Comparison to Baselines:_ Under nominal lighting, our system achieves a mean of 37 _._ 6 consecutive reorientations across objects. It substantially outperforms the only prior vision-based baseline reported on hardware, DeXtreme [7], on the shared _Cube_ object (35 _._ 4 vs. 27 _._ 8). 

To further validate the necessity of our tailored perception pipeline, we replaced our estimator with FoundationPose [31] during deployment. This configuration resulted in near-total failure, achieving only 0.4 consecutive successes (CS) on average. We attribute this collapse to two factors: (i) FoundationPose operates at approximately 4 Hz, which is too slow for the rapid control loop compared to the _∼_ 18 Hz throughput of our estimator, and (ii) frequent tracking loss caused by rapid object motion and severe finger occlusions inherent to in-hand manipulation. This experiment underscores that robust manipulation performance depends not only on policy quality but critically on high-frequency, occlusiontolerant pose estimation. 

_b) Object-Specific Performance:_ The learned policy demonstrates exceptional robustness on primitive geometries, with the _Globe_ exceeding 200 CS in one of the trials. The performance extends to highly non-convex objects, such as the _3D Printed Toy_ and _Rubber Duck_ , obtaining more than 20 CS on average. We qualitatively observe smoother manipulation 

TABLE IV: Real-world deployment on different objects. 

||**Consecutive **|**Successes (Over **|**Five Runs)**|
|---|---|---|---|
|**Objects**|DeXtreme [7]|Ours<br>(Nominal)|Ours<br>(Adversarial)|
|**Cube**|27_._8_±_19_._0|35_._4_±_13_._8|25_._6_±_8_._9|
|**3D Printed Toy**|-|28_._2_±_12_._6|12_._0_±_6_._9|
|**Rubber Duck**|-|24_._2_±_15_._3|9_._0_±_5_._0|
|**Tablet Bottle**|-|12_._6_±_8_._8|4_._2_±_0_._7|
|**Globe**|-|87_._6_±_41_._4|76_._2_±_66_._2|
|**Mean**|-|37_._6_±_21_._8|25_._4_±_30_._1|



behaviors with compliant objects (e.g., _Globe_ , _Duck_ ), suggesting that inherent material damping aids stability despite not being explicitly modeled in simulation. However, we observe a notable sim-to-real gap for the _Tablet Bottle_ . We attribute this degradation to unmodeled friction effects, particularly the extremely low surface friction introduced by its label. 

_c) Robustness to Adversarial Lighting:_ Under severe adversarial lighting conditions, the policy maintained an average of consecutive successes of _∼_ 25. To our knowledge, this is the first demonstration of sustained dexterous inhand manipulation under such extreme visual perturbations. Although performance decreases relative to nominal lighting, the decline highlights the tight coupling between perception and control. The reduction in overall task success disproportionately exceeds the degradation in pose estimation accuracy (Section IV-A). This indicates that even small perceptual errors can compound into significant control failures. 

## V. CONCLUSION 

In this work, we presented a framework for robust inhand reorientation using monocular RGB vision. By integrating 3D Gaussian Splatting directly into the simulation loop, we substantially reduced the computational cost of highfidelity rendering. Our novel _pre-rasterization augmentations_ introduce structured diversity into static Gaussian scenes, effectively bridging the visual sim-to-real gap. This approach enabled the training of a perception module for object pose estimation that is robust to both nominal and severe adversarial lighting conditions. Deploying the resulting system on a multifingered hand, we achieved an average of over 25 consecutive successful reorientations across diverse object geometries, even under adversarial lighting. 

Our findings underscore a critical insight for the field: the primary bottleneck in real-world dexterity often lies less in control complexity and more in perceptual fidelity. We show that when vision is modeled with sufficient physical grounding, it can support complex and precise manipulation tasks, previously dominated by proprioceptive or tactile-based approaches. Nevertheless, vision is fundamentally constrained by finger occlusions and its inability to directly sense contact forces. A promising direction for future work is the integration of dense visual feedback with high-frequency tactile sensing to better handle unmodeled surface properties. Moreover, while our method excels at instance-specific manipulation, extending this pipeline to support broader generalization is a key step toward truly general-purpose dexterous manipulation. 

## ACKNOWLEDGMENTS 

This work was funded by ETH Zurich (research grant no. 22-2 ETH-47), Swiss National Science Foundation (NCCR Automation grant no. 51NF40 225155), Swiss Federal Railways (SBB) via ETH Mobility Initiative, ETHAR and by grants from NVIDIA. The authors also acknowledge the use of NVIDIA RTX 6000 Ada Generation GPUs, which facilitated this research. 

The authors would like to thank Ren´e Zurbr¨ugg for insightful discussions regarding pose estimator training and system identification, Pascal Roth for the initial integration of Gaussian splatting rendering with IsaacLab, and Elena Krasnova for assistance with the robotic hardware. 

## REFERENCES 

- [1] Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias Plappert, Glenn Powell, Raphael Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 

- [2] OpenAI: Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 39 (1):3–20, 2020. 

- [3] Aditya Bhatt, Adrian Sieler, Steffen Puhlmann, and Oliver Brock. Surprisingly robust in-hand manipulation: An empirical study. _Robotics: Science and Systems_ , 2021. 

- [4] Filip Bjelonic, Fabian Tischhauser, and Marco Hutter. Towards bridging the gap: Systematic sim-toreal transfer for diverse legged robots. _arXiv preprint arXiv:2509.06342_ , 2025. 

- [5] Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Edward Adelson, and Pulkit Agrawal. Visual dexterity: Inhand reorientation of novel and complex object shapes. _Science Robotics_ , 8(84):eadc9244, 2023. 

- [6] Timothy Chen, Ola Shorinwa, Joseph Bruno, Aiden Swann, Javier Yu, Weijia Zeng, Keiko Nagami, Philip Dames, and Mac Schwager. Splat-nav: Safe real-time robot navigation in gaussian splatting maps, 2024. URL https://arxiv.org/abs/2403.02751. 

- [7] Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zhurkevich, Balakumar Sundaralingam, et al. Dextreme: Transfer of agile in-hand manipulation from simulation to reality. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 5977–5984. IEEE, 2023. 

- [8] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In _2016 IEEE Conference on Computer Vision and Pattern Recognition, (CVPR)_ , pages 770–778, 2016. 

- [9] Huajian Huang, Longwei Li, Cheng Hui, and Sai-Kit Yeung. Photo-slam: Real-time simultaneous localization 

and photorealistic mapping for monocular, stereo, and rgb-d cameras. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2024. 

- [10] Bernhard Kerbl, Georgios Kopanas, Thomas Leimk¨uhler, and George Drettakis. 3d gaussian splatting for real-time radiance field rendering. _ACM Transactions on Graphics_ , 42(4), July 2023. URL https://repo-sam.inria.fr/fungraph/ 3d-gaussian-splatting/. 

- [11] Yongseok Lee, Hyunsu Kim, Harim Ji, Jinuk Heo, Youngseon Lee, Jiseock Kang, Jeongseob Lee, and Dongjun Lee. Human-in-the-loop gaussian splatting for robotic teleoperation. _IEEE Robotics and Automation Letters_ , 11(1):105–112, 2026. doi: 10.1109/LRA.2025. 3632755. 

- [12] Xinhai Li, Jialin Li, Ziheng Zhang, Rui Zhang, Fan Jia, Tiancai Wang, Haoqiang Fan, Kuo-Kun Tseng, and Ruiping Wang. Robogsim: A real2sim2real robotic gaussian splatting simulator, 2024. URL https://arxiv. org/abs/2411.11839. 

- [13] Hidenobu Matsuki, Riku Murai, Paul H. J. Kelly, and Andrew J. Davison. Gaussian Splatting SLAM. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2024. 

- [14] Jonathan Michaux, Seth Isaacson, Challen Enninful Adu, Adam Li, Rahul Kashyap Swayampakula, Parker Ewen, Sean Rice, Katherine A. Skinner, and Ram Vasudevan. Let’s make a splan: Risk-aware trajectory optimization in a normalized gaussian splat. _IEEE Transactions on Robotics_ , pages 1–19, 2025. doi: 10.1109/TRO.2025. 3584559. 

- [15] Takahiro Miki, Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen Koltun, and Marco Hutter. Learning robust perceptive locomotion for quadrupedal robots in the wild. _Science Robotics_ , 7(62):eabk2822, 2022. doi: 10.1126/scirobotics.abk2822. URL https://www.science. org/doi/abs/10.1126/scirobotics.abk2822. 

- [16] Mayank Mittal, Pascal Roth, James Tigue, Antoine Richard, Octi Zhang, Peter Du, Antonio Serrano-Mu˜noz, Xinjie Yao, Ren´e Zurbr¨ugg, Nikita Rudin, Lukasz Wawrzyniak, Milad Rakhsha, Alain Denzler, Eric Heiden, Ales Borovicka, Ossama Ahmed, Iretiayo Akinola, Abrar Anwar, Mark T. Carlson, Ji Yuan Feng, Animesh Garg, Renato Gasoto, Lionel Gulich, Yijie Guo, M. Gussert, Alex Hansen, Mihir Kulkarni, Chenran Li, Wei Liu, Viktor Makoviychuk, Grzegorz Malczyk, Hammad Mazhar, Masoud Moghani, Adithyavairavan Murali, Michael Noseworthy, Alexander Poddubny, Nathan Ratliff, Welf Rehberg, Clemens Schwarke, Ritvik Singh, James Latham Smith, Bingjie Tang, Ruchik Thaker, Matthew Trepte, Karl Van Wyk, Fangzhou Yu, Alex Millane, Vikram Ramasamy, Remo Steiner, Sangeeta Subramanian, Clemens Volk, CY Chen, Neel Jawale, Ashwin Varghese Kuruttukulam, Michael A. Lin, Ajay Mandlekar, Karsten Patzwaldt, John Welsh, Huihua Zhao, Fatima Anes, Jean-Francois Lafleche, Nicolas Mo¨enneLoccoz, Soowan Park, Rob Stepinski, Dirk Van Gelder, 

Chris Amevor, Jan Carius, Jumyung Chang, Anka He Chen, Pablo de Heras Ciechomski, Gilles Daviet, Mohammad Mohajerani, Julia von Muralt, Viktor Reutskyy, Michael Sauter, Simon Schirm, Eric L. Shi, Pierre Terdiman, Kenny Vilella, Tobias Widmer, Gordon Yeoman, Tiffany Chen, Sergey Grizan, Cathy Li, Lotus Li, Connor Smith, Rafael Wiltz, Kostas Alexis, Yan Chang, David Chu, Linxi ”Jim” Fan, Farbod Farshidian, Ankur Handa, Spencer Huang, Marco Hutter, Yashraj Narang, Soha Pouya, Shiwei Sheng, Yuke Zhu, Miles Macklin, Adam Moravanszky, Philipp Reist, Yunrong Guo, David Hoeller, and Gavriel State. Isaac lab: A gpuaccelerated simulation framework for multi-modal robot learning. _arXiv preprint arXiv:2511.04831_ , 2025. URL https://arxiv.org/abs/2511.04831. 

- [17] Sanmit Narvekar, Bei Peng, Matteo Leonetti, Jivko Sinapov, Matthew E. Taylor, and Peter Stone. Curriculum learning for reinforcement learning domains: a framework and survey. _J. Mach. Learn. Res._ , 21(1), January 2020. ISSN 1532-4435. 

- [18] Johannes Pitz, Lennart R¨ostel, Leon Sievers, Darius Burschka, and Berthold B¨auml. Learning a shapeconditioned agent for purely tactile in-hand manipulation of various objects. In _2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 13112–13119. IEEE, 2024. 

- [19] Polycam Inc. Polycam - lidar & 3d scanner for iphone and android, 2024. URL https://poly.cam/. Accessed: 2024-05-20. 

- [20] Haozhi Qi, Brent Yi, Sudharshan Suresh, Mike Lambeta, Yi Ma, Roberto Calandra, and Jitendra Malik. General In-Hand Object Rotation with Vision and Touch. In _Conference on Robot Learning (CoRL)_ , 2023. 

- [21] Mohammad Nomaan Qureshi, Sparsh Garg, Francisco Yandun, David Held, George Kantor, and Abhishesh Silwal. Splatsim: Zero-shot sim2real transfer of rgb manipulation policies using gaussian splatting, 2024. URL https://arxiv.org/abs/2409.10161. 

- [22] Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman R¨adle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Doll´ar, and Christoph Feichtenhofer. Sam 2: Segment anything in images and videos. _arXiv preprint arXiv:2408.00714_ , 2024. URL https://arxiv.org/abs/2408.00714. 

- [23] St´ephane Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. In _Proceedings of the fourteenth international conference on artificial intelligence and statistics_ , pages 627–635. JMLR Workshop and Conference Proceedings, 2011. 

- [24] Sara Fridovich-Keil and Alex Yu, Matthew Tancik, Qinhong Chen, Benjamin Recht, and Angjoo Kanazawa. Plenoxels: Radiance fields without neural networks. In _CVPR_ , 2022. 

- [25] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _ArXiv_ , abs/1707.06347, 2017. URL https: //api.semanticscholar.org/CorpusID:28695052. 

- [26] Clemens Schwarke, Mayank Mittal, Nikita Rudin, David Hoeller, and Marco Hutter. Rsl-rl: A learning library for robotics research. _arXiv preprint arXiv:2509.10771_ , 2025. 

- [27] Ritvik Singh, Arthur Allshire, Ankur Handa, Nathan Ratliff, and Karl Van Wyk. Dextrah-rgb: Visuomotor policies to grasp anything with dexterous hands. _arXiv preprint arXiv:2412.01791_ , 2024. 

- [28] Ritvik Singh, Jason Jingzhou Liu, Karl Van Wyk, Yu-Wei Chao, Jean-Francois Lafleche, Florian Shkurti, Nathan Ratliff, and Ankur Handa. Synthetica: Large scale synthetic data generation for robot perception. In _2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 7810–7817. IEEE, 2025. 

- [29] Jos M. F. ten Berge. The rigid orthogonal procrustes rotation problem. _Psychometrika_ , 71(1):201–205, 2006. doi: 10.1007/s11336-004-1160-5. 

- [30] Jiaxu Wang, Qiang Zhang, Jingkai Sun, Jiahang Cao, Gang Han, Wen Zhao, Weining Zhang, Yecheng Shao, Yijie Guo, and Renjing Xu. Reinforcement learning with generalizable gaussian splatting. In _2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 435–441, 2024. doi: 10.1109/IROS58592. 2024.10801348. 

- [31] Bowen Wen, Wei Yang, Jan Kautz, and Stanley T. Birchfield. Foundationpose: Unified 6d pose estimation and tracking of novel objects. _2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 17868–17879, 2023. URL https://api.semanticscholar. org/CorpusID:266191252. 

- [32] Maximum Wilder-Smith, Vaishakh Patil, and Marco Hutter. Radiance fields for robotic teleoperation. In _2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 13861–13868, 2024. doi: 10.1109/IROS58592.2024.10801345. 

- [33] Yuxuan Wu, Lei Pan, Wenhua Wu, Guangming Wang, Yanzi Miao, Fan Xu, and Hesheng Wang. Rl-gsbridge: 3d gaussian splatting based real2sim2real method for robotic manipulation learning. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 192– 198, 2025. doi: 10.1109/ICRA55743.2025.11128103. 

- [34] Max Yang, chenghua lu, Alex Church, Yijiong Lin, Christopher J. Ford, Haoran Li, Efi Psomopoulou, David A.W. Barton, and Nathan F. Lepora. Anyrotate: Gravity-invariant in-hand object rotation with simto-real touch. In _8th Annual Conference on Robot Learning_ , 2024. URL https://openreview.net/forum?id= 8Yu0TNJNGK. 

- [35] Zhao-Heng Yin, Binghao Huang, Yuzhe Qin, Qifeng Chen, and Xiaolong Wang. Rotating without seeing: Towards in-hand dexterity through touch. _Robotics: Science and Systems_ , 2023. 

APPENDIX A ADDITIONAL RESULTS 

TABLE V: Simulation results on different objects. We evaluate the policy across 256 environments with randomized physical conditions (DR) and report the mean and standard deviation over five episodes. 

## _A. Simulation Results_ 

To quantify the distillation gap and robustness against observation noise, we evaluate the teacher and student policies across randomized simulation environments parameterized by the domain randomization ranges used during training. Results are summarized in Table V. 

As expected, the teacher policy, with access to groundtruth dynamics via privileged system information, consistently outperforms the student policy across all geometries, even when the student is provided with noiseless observations. This performance delta underscores the value of explicit physical state information (e.g., friction, mass) that cannot be perfectly inferred from proprioception and exteroceptive information alone. Crucially, however, the student policy exhibits minimal performance degradation when transitioning from noiseless to noisy exteroceptive observations. This stability indicates that the distillation process successfully imparts robustness against the noise model, enabling the student to filter observation noise effectively while retaining the behaviour of the teacher policy. 

When comparing simulation results to hardware deployments, we observe a quantitative performance gap, a phenomenon common in contact-rich manipulation tasks [2, 34]. We attribute this sim-to-real gap to inevitable physical disparities, including inaccurate contact models, actuator dynamics, and material properties. A notable instance of this is the _Tablet Bottle_ , where unmodeled low-surface friction significantly impacted real-world controllability despite high simulation success. Additionally, although our perception noise model significantly enhances robustness, it cannot perfectly replicate the full spectrum of stochastic sensor noise found in the realworld sensors, leading to a natural drop in performance on hardware. 

## _B. Belief State Analysis_ 

To evaluate the noise rejection capabilities of the belief decoder, we analyze the reconstructed exteroceptive state derived from the belief latent _zt_ . During real-world rollouts, we artificially corrupt the pose estimator’s output with synthetic noise at intermittent 1-second intervals. We then compare the error of the belief decoder’s reconstruction against the raw pose estimator input, utilizing FoundationPose [31] as the offline ground truth reference. The resulting position and rotation errors are visualized in Fig. 7, where red shaded regions indicate phases of noise injection. 

Under nominal conditions, the raw pose estimator yields lower error than the belief decoder, as indicated by the mean error lines. This is an expected artifact of the decoder’s training on high-variance noise, which induces a conservative smoothing bias in the predictions. However, during noise injection phases, the belief decoder demonstrates superior robustness, yielding significantly lower errors than the corrupted sensor input. It effectively filters high-amplitude noise, maintaining stable state estimates for multiple timesteps before drift accumulates. A critical instance of this robustness is 

||**C**|**onsecutive Success**|**es**|
|---|---|---|---|
|**Objects**|Teacher Policy<br>(w/o obs noise)|Student Policy<br>(w/o obs noise)|Student Policy<br>(with obs noise)|
|**Cube**|111_._4_±_24_._7|92_._1_±_5_._7|82_._3_±_8_._4|
|**3D Printed Toy**|106_._0_±_25_._0|74_._9_±_4_._7|74_._6_±_6_._2|
|**Rubber Duck**|97_._1_±_14_._1|46_._2_±_1_._8|41_._6_±_2_._3|
|**Tablet Bottle**|118_._4_±_2_._8|77_._0_±_4_._2|69_._4_±_2_._9|
|**Globe**|163_._6_±_3_._4|138_._1_±_2_._4|129_._5_±_5_._9|
|**Mean**|119_._3_±_17_._05|85_._7_±_4_._03|79_._5_±_5_._61|



highlighted in the region highlighted by the blue box. While the pose estimator suffers a catastrophic 180<sup>_◦_</sup> flip, the belief decoder successfully rejects this outlier. This confirms that the recurrent architecture effectively functions as a temporal filter, mitigating high-frequency perturbations and preventing tracking divergence during sensor failures. 

## _C. Pose Estimation Results for Rollouts_ 

TABLE VI: Pose estimation during real-world hardware deployment. We report the translation error (in mm) and the rotation error (in degrees). We also report Pearson correlation coefficient between the occlusion ratio and errors. 

|**Objects**|Trans Error|Rot Error|Trans Error<br>Correlation|Rot Error<br>Correlation|
|---|---|---|---|---|
|**Cube**|9_._05|14_._6|0_._4|0_._38|
|**3D Printed Toy**|11_._14|33_._59|0_._42|0_._12|
|**Rubber Duck**|8_._85|18_._84|0_._02|0_._17|
|**Tablet Bottle**|10_._9|38_._27|0_._14|0_._08|
|**Globe**|12_._01|32_._42|0_._04|0_._20|
|**Mean**|10_._39|27_._54|0_._20|0_._19|



We quantify the errors of our pose estimator during hardware deployment, with results detailed in Table VI. The system demonstrates strong overall performance, achieving a mean translation error of 10 _._ 39 mm and a mean rotation error of 27 _._ 54<sup>_◦_</sup> . Performance varies across geometries: the _Rubber Duck_ yields the lowest translation error (8 _._ 85 mm), while the _Cube_ exhibits the lowest rotational error (14 _._ 6<sup>_◦_</sup> ). Conversely, objects with complex or symmetric properties, such as the _Tablet Bottle_ and _Globe_ , show higher rotational variance (38 _._ 27<sup>_◦_</sup> and 32 _._ 42<sup>_◦_</sup> , respectively). 

To evaluate robustness against hand-object interference, we compute the Pearson correlation coefficient between the error metrics and the instantaneous occlusion ratio. The mean correlations are remarkably low (0 _._ 20 for translation and 0 _._ 19 for rotation), suggesting that pose accuracy is not strongly degraded by partial occlusions. While the _Cube_ shows moderate sensitivity (correlation _≈_ 0 _._ 4), performance on complex objects like the _Rubber Duck_ and _Globe_ is effectively decoupled from occlusion levels (translation correlations of 0 _._ 02 and 0 _._ 04, respectively), validating that the pose estimator successfully leverages local features when global geometry is occluded. 

## _D. Pose Estimation Errors_ 

We report explicit Translation Error (in mm) and Rotation Error (in degrees) for the pose estimator across two studies. In 



<!-- Start of picture text -->
Actual Pose Pose Estimator Output Belief Decoder Reconstruction<br><!-- End of picture text -->

Fig. 7: **Top:** Temporal evolution of translation and rotation errors during a real-world rollout. Red regions indicate intervals where artificial noise is injected into the pose estimator input. The belief decoder (orange) effectively filters these high-frequency perturbations, maintaining significantly lower error compared to the corrupted input (green). **Bottom:** Visualization of a specific failure case (corresponding to the blue box in the plot). The belief decoder successfully maintains a stable pose estimate close to the ground truth, effectively rejecting a catastrophic 180<sup>_◦_</sup> flip returned by the pose estimator. 

the baseline comparison, reported in Table VII, we compare our approach against Standard Tiled, Domain Randomized, and Naive GS rendering. While translation errors remain comparable across methods in nominal conditions, our method demonstrates significantly superior rotational stability. Under adversarial lighting, our pipeline achieves a mean rotation error of 14.6<sup>_◦_</sup> , outperforming other methods by a significant margin. In Table VIII, we quantify the contribution of each augmentation component. Similar to Section IV-A results identify Global Shift as the most critical factor; its removal causes a catastrophic degradation in adversarial rotation error (spiking to 38.9<sup>_◦_</sup> ). Structured perturbations (Spatial and Color Clustering) are shown to be essential for maintaining precision, whereas unstructured Random Noise has a comparatively minor impact on final pose errors. 

## APPENDIX B METHOD DETAILS 

_A. Teacher Training using Reinforcement Learning_ 

## _1) MDP Formulation:_ 

_a) Action Space:_ The action space _A ⊆_ R<sup>16</sup> consists of target joint positions for the 16 independently actuated joints of the Allegro Hand. The policy outputs actions _at_ , which are scaled to the robot’s joint limits and processed via an Exponential Moving Average (EMA) filter _a_ ¯ _t_ = (1 _− α_ )¯ _at−_ 1 + _αat_ to ensure smooth motion. The smoothing parameter _α_ of the EMA filter is randomized between (0.08, 0.2) during training to enhance robustness against unmodeled gaps in the robot’s actuator dynamics. 

_b) Reward Modeling:_ To guide the policy, we employ a dense reward function _rt_ = _r_ task + _r_ reg. The task term _r_ task incentivizes minimizing orientation error, augmented by a sparse success bonus. To encourage smooth and stable behavior, the regularization term _r_ reg penalizes aggressive control inputs, high joint velocities, energy consumption and object instability. The various reward terms used for training the teacher policy are listed in Table IX 

_c) Early Terminations:_ An episode terminates if the object falls from the hand, the agent fails to achieve a success within a 10-second window, or the policy successfully completes a sequence of 50 consecutive reorientations. 

_d) Observations:_ Table X lists out the observation terms in the different observation groups introduced in Section III-A2. 

_2) Domain Randomization:_ We employ domain randomization across multiple aspects of the simulation to improve robustness against varying physical conditions and facilitate sim-to-real transfer. Physical properties of both the robot and the object, including link and object mass, friction coefficients, and restitution, are randomized to account for inaccuracies in contact dynamics. Geometric properties of the object are varied to capture shape and size variations. We perform system identification for the Allegro hand using [4] to obtain simulation-accurate values for actuation-related parameters, such as joint stiffness and damping. At each episode, these values are randomized around the identified ranges to account for model mismatch between the simulated and actual robot dynamics. Finally, external disturbances are introduced by applying random forces and perturbing the gravity vector at fixed intervals, to add robustness against unmodeled interactions. Various randomizations and their ranges are listed in Table XI. 

_3) Policy Architecture and Optimization:_ We employ a modified asymmetric actor-critic framework to learn the teacher policy. Unlike standard implementations, where only the critic has access to privileged state information, we provide privileged observations _O_ priv to both the actor and the critic. The asymmetry is instead introduced in the actor’s proprioceptive input _O_ prop<sup>noisy,whichisaugmentedwithnoiseand</sup> latency during training, to induce robustness against sensor inaccuracies encountered in real-world observations. 

To effectively fuse heterogeneous modalities, we utilize a multi-encoder network architecture. Exteroceptive and priv- 

TABLE VII: Evaluation of learned pose estimator on real-world data under nominal and adversarial lighting. Our method is compared against three baselines: _Standard Tiled_ , _Randomized Tiled_ , and _Naive GS_ rendering. We report the translation error (in mm) and the rotation error (in degrees), averaged over 5 random seeds. 

|**Objects**|**Cu**|**be**|**3D Prin**|**ted Toy**|**Rubbe**|**r Duck**|**Tablet **|**Bottle**|**Glo**|**be**|**Me**|**an**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Method**|Trans Error|Rot Error|Trans Error|Rot Error|Trans Error<br>**NOMINA**|Rot Error<br>**L CONDITION**|Trans Error<br>**S**|Rot Error|Trans Error|Rot Error|Trans Error|Rot Error|
|Standard Tiled<br>Domain Randomized<br>Naive GS<br>Ours|10_._8_±_0_._78<br>10_._0_±_0_._80<br>8_._7_±_1_._25<br>**8**_._**2**_±_**0**_._**64**|5_._6_±_1_._57<br>**4**_._**0**_±_**0**_._**15**<br>6_._9_±_1_._22<br>4_._8_±_0_._18|11_._2_±_0_._32<br>15_._4_±_0_._74<br>15_._3_±_0_._96<br>**10**_._**2**_±_**1**_._**01**|19_._2_±_3_._79<br>**8**_._**8**_±_**0**_._**78**<br>23_._2_±_2_._04<br>**8**_._**8**_±_**0**_._**82**|8_._1_±_0_._22<br>8_._3_±_0_._26<br>10_._6_±_0_._32<br>**7**_._**5**_±_**0**_._**26**|7_._5_±_0_._75<br>5_._0_±_0_._20<br>6_._0_±_0_._27<br>**4**_._**2**_±_**0**_._**08**|8_._2_±_0_._39<br>7_._8_±_0_._13<br>8_._6_±_0_._54<br>**7**_._**5**_±_**0**_._**74**|13_._3_±_1_._41<br>**10**_._**2**_±_**1**_._**29**<br>16_._0_±_3_._54<br>10_._3_±_1_._93|13_._9_±_2_._51<br>14_._5_±_1_._29<br>18_._8_±_1_._50<br>**11**_._**7**_±_**0**_._**83**|8_._4_±_0_._59<br>14_._5_±_2_._31<br>11_._7_±_1_._38<br>**5**_._**3**_±_**0**_._**55**|10_._4_±_1_._20<br>11_._2_±_0_._77<br>12_._4_±_1_._01<br>**9**_._**0**_±_**0**_._**74**|10_._8_±_1_._99<br>8_._5_±_1_._24<br>12_._8_±_2_._01<br>**6**_._**7**_±_**0**_._**97**|
||||||**ADVERSAR**|**IAL CONDITI**|**ONS**||||||
|Standard Tiled<br>Domain Randomized<br>Naive GS<br>Ours|**9**_._**0**_±_**0**_._**95**<br>9_._1_±_0_._64<br>10_._9_±_0_._79<br>9_._1_±_0_._46|12_._0_±_1_._74<br>9_._2_±_1_._63<br>13_._5_±_1_._21<br>**6**_._**6**_±_**0**_._**78**|15_._9_±_1_._49<br>**12**_._**2**_±_**0**_._**58**<br>17_._4_±_0_._66<br>12_._7_±_0_._61|33_._4_±_5_._14<br>**13**_._**3**_±_**1**_._**79**<br>37_._6_±_2_._73<br>17_._2_±_1_._67|9_._1_±_0_._53<br>9_._1_±_0_._38<br>**8**_._**3**_±_**0**_._**43**<br>9_._5_±_0_._32|25_._1_±_1_._83<br>**10**_._**7**_±_**1**_._**31**<br>22_._3_±_4_._35<br>12_._0_±_2_._07|12_._4_±_1_._03<br>8_._7_±_0_._72<br>9_._5_±_0_._76<br>**7**_._**7**_±_**0**_._**35**|57_._2_±_4_._08<br>28_._8_±_4_._55<br>56_._3_±_4_._37<br>**26**_._**7**_±_**2**_._**66**|15_._3_±_2_._38<br>14_._4_±_1_._37<br>15_._9_±_1_._84<br>**12**_._**3**_±_**0**_._**71**|20_._7_±_1_._39<br>26_._5_±_2_._03<br>31_._1_±_1_._80<br>**10**_._**7**_±_**2**_._**20**|12_._3_±_1_._42<br>10_._7_±_0_._81<br>12_._4_±_1_._02<br>**10**_._**3**_±_**0**_._**51**|29_._7_±_3_._21<br>17_._7_±_2_._55<br>32_._2_±_3_._17<br>**14**_._**6**_±_**1**_._**98**|



TABLE VIII: Ablation study of pre-rasterization augmentations under nominal and adversarial conditions for pose estimation. We compare our method with models trained with specific augmentation groups removed. We report the translation error (in mm) and the rotation error (in degrees), averaged over 5 random seeds. 

|**Objects**|**Cu**|**be**|**3D Prin**|**ted Toy**|**Rubbe**|**r Duck**|**Tablet **|**Bottle**|**Gl**|**obe**|**Me**|**an**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Method**|Trans Error|Rot Error|Trans Error|Rot Error|Trans Error|Rot Error|Trans Error|Rot Error|Trans Error|Rot Error|Trans Error|Rot Error|
||||||**NOMINAL**|**CONDITIONS**|||||||
|w/o Random Noise<br>w/o Spatial Clustering<br>w/o Color Clustering<br>w/o Global Shift<br>Ours|10_._8_±_3_._05<br>**8**_._**1**_±_**1**_._**23**<br>**8**_._**1**_±_**0**_._**62**<br>8_._3_±_0_._60<br>8_._2_±_0_._64|6_._8_±_2_._27<br>5_._6_±_3_._46<br>5_._4_±_0_._54<br>11_._0_±_4_._64<br>**4**_._**8**_±_**0**_._**18**|12_._5_±_0_._91<br>11_._7_±_0_._93<br>12_._2_±_1_._78<br>**9**_._**9**_±_**1**_._**10**<br>10_._2_±_1_._01|10_._0_±_2_._63<br>10_._9_±_1_._48<br>11_._7_±_1_._61<br>9_._5_±_1_._69<br>**8**_._**8**_±_**0**_._**82**|7_._7_±_0_._44<br>**7**_._**2**_±_**0**_._**28**<br>7_._6_±_0_._65<br>8_._1_±_0_._34<br>7_._5_±_0_._26|4_._7_±_0_._29<br>5_._8_±_0_._24<br>4_._7_±_0_._16<br>6_._6_±_0_._53<br>**4**_._**2**_±_**0**_._**08**|8_._3_±_0_._62<br>10_._7_±_0_._71<br>14_._0_±_0_._71<br>29_._5_±_3_._50<br>**7**_._**5**_±_**0**_._**74**|12_._6_±_2_._20<br>26_._7_±_3_._23<br>33_._8_±_2_._11<br>67_._9_±_1_._83<br>**10**_._**3**_±_**1**_._**93**|14_._0_±_1_._16<br>13_._1_±_2_._36<br>13_._7_±_1_._81<br>11_._9_±_0_._43<br>**11**_._**7**_±_**0**_._**83**|5_._5_±_0_._59<br>6_._6_±_0_._86<br>6_._5_±_0_._98<br>12_._4_±_1_._10<br>**5**_._**3**_±_**0**_._**55**|10_._7_±_1_._55<br>10_._2_±_1_._31<br>11_._1_±_1_._25<br>13_._5_±_1_._68<br>**9**_._**0**_±_**0**_._**74**|7_._9_±_1_._86<br>11_._1_±_2_._25<br>12_._4_±_1_._29<br>21_._5_±_2_._42<br>**6**_._**7**_±_**0**_._**97**|
||||||**ADVERSARI**|**AL CONDITIO**|**NS**||||||
|w/o Random Noise<br>w/o Spatial Clustering<br>w/o Color Clustering<br>w/o Global Shift<br>Ours|11_._1_±_0_._73<br>11_._2_±_1_._34<br>10_._9_±_0_._84<br>16_._0_±_0_._93<br>**9**_._**1**_±_**0**_._**46**|9_._3_±_1_._68<br>9_._7_±_1_._11<br>13_._2_±_2_._58<br>35_._4_±_2_._40<br>**6**_._**6**_±_**0**_._**78**|14_._2_±_1_._24<br>13_._5_±_1_._39<br>14_._4_±_1_._45<br>16_._6_±_1_._14<br>**12**_._**7**_±_**0**_._**61**|**16**_._**8**_±_**1**_._**90**<br>23_._6_±_1_._15<br>22_._3_±_2_._46<br>41_._2_±_4_._81<br>17_._2_±_1_._67|10_._4_±_0_._45<br>10_._0_±_0_._30<br>10_._8_±_0_._44<br>14_._7_±_1_._71<br>**9**_._**5**_±_**0**_._**32**|12_._2_±_1_._18<br>17_._3_±_2_._21<br>17_._9_±_2_._85<br>25_._2_±_3_._11<br>**12**_._**0**_±_**2**_._**07**|8_._7_±_0_._60<br>8_._9_±_0_._72<br>11_._2_±_0_._71<br>10_._3_±_0_._60<br>**7**_._**7**_±_**0**_._**35**|**26**_._**1**_±_**1**_._**83**<br>39_._8_±_2_._90<br>41_._8_±_4_._49<br>71_._7_±_6_._55<br>26_._7_±_2_._66|15_._0_±_0_._85<br>13_._7_±_1_._85<br>14_._0_±_1_._85<br>13_._9_±_0_._54<br>**12**_._**3**_±_**0**_._**71**|11_._5_±_1_._15<br>17_._1_±_1_._51<br>13_._8_±_3_._40<br>21_._2_±_0_._66<br>**10**_._**7**_±_**2**_._**20**|11_._9_±_0_._82<br>11_._5_±_1_._25<br>12_._3_±_1_._18<br>14_._3_±_1_._07<br>**10**_._**3**_±_**0**_._**51**|15_._2_±_1_._58<br>21_._5_±_1_._90<br>21_._8_±_3_._24<br>38_._9_±_4_._05<br>**14**_._**6**_±_**1**_._**98**|



TABLE IX: Reward Terms 

|**Term**|**Weight**|**Equation**|**Description**|
|---|---|---|---|
|**TASK REWARDS**||||
|Orientation Tracking|1.0|(_d_(_θ_) +_ϵ_)<sup>_−_1</sup>|_d_(_θ_): orientation error, _ϵ_= 0_._1.|
|Success Bonus|250.0|I(_d_(_θ_)_≤ϵ_success)|Bonus when _d_(_θ_)_≤ϵ_success = 0_._1rad.|
|**TERMINATION PENA**|**LTIES**|||
|Object Dropped|_−_10_._0|I(drop)|Penalty when the object falls.|
|**CURRICULUM PENAL**|**TIES**|_(Wei_|_ghts are gradually increased during training)_|
|Object Distance|-20.0|_−∥p_robot_−p_obj_∥_2|Object-robot distance.|
|Object Velocity|-1e-3|_−∥v_obj_∥_2|_L_2 norm of object linear velocity.|
|Joint Velocity|-8e-2|_−∥_˙_q∥_2|_L_2 norm of joint velocities.|
|Action Magnitude|-0.80|_−∥at∥_2|_L_2 norm of the action vector.|
|Action Rate|-0.12|_−∥at −at−_1_∥_2|_L_2 norm of diff. b/w consecutive actions.|
|Joint Work|-0.12|_−_<sup>�</sup>_|τ ·_ ˙_q|_|Mechanical work.|
|Joint Torques|-50.0|_−∥τ∥_2|_L_2 norm of applied joint torques.|



ileged observation groups are processed by dedicated MultiLayer Perceptrons (MLPs) to extract latent embeddings _z_ exte _∈_ R<sup>24</sup> and _z_ priv _∈_ R<sup>128</sup> , with encoder hidden dimensions of [64 _,_ 64] and [256 _,_ 256], respectively. These embeddings are concatenated with normalized proprioceptive observations and passed to the primary backbone. We observed a strong correlation between network capacity and task performance; consequently, both the actor and critic are parameterized as deep MLPs with hidden units [1024 _,_ 1024 _,_ 1024 _,_ 512] and ELU activations. Policy optimization is performed using the Proximal Policy Optimization (PPO) algorithm [25], implemented within the RSL-RL library [26]. The policy architecture and training hyperparameters are listed in Table XII. 

TABLE X: Observation Space 

|**Term**|**Dim.**|**Description**|
|---|---|---|
|**PROPRIOCEPTIVE OBSER**<br>|**VATIONS** <br>|**_O_**prop<br>|
|Joint Positions|16|Measured robot joint angles.|
|Action History|64|Joint position commands from the last four time steps.|
|Goal Orientation|4|Target orientation (quaternion).|
|Palm Link Position|3|Position of the palm link (constant)|
|Remaining Time|1|Normalized time remaining in the episode.|
|_Group Total_|_88_||
|**EXTEROCEPTIVE OBSER**<br>|**VATIONS** <br>|**_O_**extero<br>|
|Object Pose|7|Ground-truth object position and orientation (quaternion).|
|Goal Quaternion Diff.|4|Quaternion representing rotation from object to goal.|
|_Group Total_|_11_||
|**PRIVILEGED OBSERVATI**<br>|**ONS** **_O_**priv<br>||
|Joint Velocities|16|Angular velocities of robot joints.|
|Joint Torques|16|Actuator-applied joint torques.|
|Fingertip Forces|12|Net contact forces at the four fingertips.|
|Object Velocities|6|Linear and angular velocities of the object.|
|Physical Properties|7|Randomized object/robot scale and object mass.|
|Scene Gravity|3|Gravity vector.|
|Actuator Gains|32|Randomized joint stiffness and damping.|
|Action Properties|2|Randomized EMA parameter _α_ and delay|
|Random Forces|6|External forces and torques applied to the object.|
|_Group Total_|_100_||
|**Total Observation Dim.**|**199**||



## _B. Student Training using Distillation_ 

_1) Student Policy:_ The parameters for the student policy architecture and training are listed in Table XIII. 

_2) Online DAgger:_ We employ an online variant of DAgger [23] to mitigate the covariate shift between states induced by the student’s and teacher’s actions. During data collection, we generate trajectories by stochastically mixing the teacher’s and student’s actions. At each timestep, the action 

TABLE XI: Domain Randomization Parameters 

|**Parameter**|**Type**|**Distribution**|**Range / Details**|
|---|---|---|---|
|**STARTUP RANDOMIZ**|**ATION**|||
|Robot Link Mass|Scaling|Log-Uniform|_×_[0_._75_,_1_._5]|
|Robot Link Friction|Absolute|Uniform|Static/Dynamic: [0_._0_,_0_._3]|
|Fingertip Friction|Absolute|Uniform|Static/Dynamic: [0_._3_,_0_._8]|
|Robot Restitution|Absolute|Uniform|[0_._0_,_0_._4]|
|Object Scale|Scaling|Uniform|_×_[0_._8_,_1_._2] (per axis)|
|Object Mass|Scaling|Uniform|_×_[0_._5_,_1_._5]|
|Object Friction|Absolute|Uniform|Static/Dynamic: [0_._3_,_0_._8]|
|Object Restitution|Absolute|Uniform|[0_._0_,_0_._4]|
|**RESET RANDOMIZATI**|**ON**|||
|Joint Stiffness|Scaling|Log-Uniform|_×_[0_._75_,_1_._5]|
|Joint Damping|Scaling|Log-Uniform|_×_[0_._75_,_1_._5]|
|Joint Friction|Scaling|Log-Uniform|_×_[0_._75_,_1_._5]|
|Joint Armature|Scaling|Log-Uniform|_×_[0_._75_,_1_._5]|
|Joint Limits|Scaling|Log-Uniform|Lower/Upper: _×_[0_._95_,_1_._05]|
|**INTERVAL RANDOMIZ**|**ATION**|||
|External Forces|Additive|Impulse|Magnitude: 2_._0_×_, Prob.: 0_._1<br>|
|Gravity Vector|Additive|Uniform|_±_0_._5m/s<sup>2 </sup>every 0–15s|



TABLE XII: Teacher Policy Architecture and PPO Training Configuration 

|**Parameter**|**Value**|
|---|---|
|**POLICY ARCHITECTURE**||
|Actor Hidden Layers<br>[1024_,_|1024_,_1024_,_512]|
|Critic Hidden Layers<br>[1024_,_|1024_,_1024_,_512]|
|Exte. Encoder Hidden Layers|<br>[64_,_64]|
|Exte. Encoder Latent Dimension|24|
|Priv. Encoder Hidden Layers|[256_,_256]|
|Priv. Encoder Latent Dimension|<br>128|
|Activation Function|ELU|
|**PPO TRAINING PARAMETERS**||
|Steps per Environment|24|
|Discount Factor _γ_|0_._998|
|GAE Parameter _λ_|0_._95|
|Learning Rate|1_×_10<sup>_−_3</sup>|
|Learning Rate Schedule|Adaptive|
|Clip Range|0_._2|
|Value Loss Coefficient|0_._5|
|i<br>Entropy Coefficient|0_._002|
|i<br>Learning Epochs per Iteration|5|
|Mini-batches|12|
|Target KL Divergence|0_._01|



applied to the robot is selected from the teacher’s policy with probability _β_ (mixing ratio), and from the student’s policy with probability 1 _−β_ . Regardless of which action is executed, the student is trained to predict the teacher’s optimal action for the visited state. To stabilize the early phases of training, we initialize _β_ to a high value (0 _._ 9) and exponentially decay it after each iteration, gradually transitioning full control to the student as its performance improves. 

_3) Perception Noise Generator:_ The various noise terms used in the perception noise model and their distribution parameters are listed in Table XIV. 

## _C. Visual Object Representation and Augmentations_ 

_1) Pre-Rasterization Augmentations:_ We outline the general algorithm for applying the pre-rasterization augmentations 

TABLE XIII: Student Policy and Distillation Hyperparameters 

|**Parameter**|**Value**|
|---|---|
|**STUDENT ARCHITECTURE**||
|Actor MLP|[1024_,_1024_,_512_,_512]<br>|
|Exteroceptive MLP|[256_,_256]|
|Exteroceptive Latent Dim|64|
|Privileged Latent Dim|256|
|Activation Function|ELU|
|Initial Action Noise Std.|0_._02|
|**BELIEF ENCODER AND DECODER**||
|RNN Hidden Dimension|256|
|Number of RNN Layers|2|
|Latent Hidden Dimensions|[256_,_256]|
|Attention Gate Dimensions|[128_,_128]|
|Exteroceptive Decoder MLP|[256_,_256]|
|Privileged Decoder MLP|[256_,_256]|
|**DISTILLATION ALGORITHM**||
|Optimizer|AdamW<br>|
|Learning Rate|3_._0_×_10<sup>_−_4</sup>|
|Number of Learning Epochs|32|
|Mini-batches|1|
|Backpropagation Length|45 steps|
|DAgger Mixing Ratio|0_._9|
|Mixing Ratio Decay|0_._95|
|Reconstruction Loss Coefficient|0_._2|
|Decoder L1 Loss Coefficient|0_._2|
|Decoder Exteroceptive Loss Coefficient|2_._0|



TABLE XIV: Perception Noise Generator Parameters 

|**Noise Component**|**Distribution / Type**|**Parameters / Range**|
|---|---|---|
|**OBJECT POSITION**|||
|Temporal Downsampling|Discrete Sampling (_k_)|Update period: 1–3 steps|
|Stochastic Jitter|Bernoulli Delay (_p_)|Delay probability: 0_._0–0_._1|
|Tracking Failure|Random Replacement|Failure probability: 0_._0–0_._3|
|Biased Noise|Additive Uniform|Noise: _U_[_−_12_,_12]mm<br>Bias: _U_[_−_12_,_12]mm|
|**OBJECT ORIENTATION**|||
|Temporal Downsampling|Discrete Sampling (_k_)|Update period: 1–3 steps|
|Stochastic Jitter|Bernoulli Delay (_p_)|Delay probability: 0_._0–0_._1|
|Tracking Failure|Random Replacement|Failure probability: 0_._0–0_._3|
|Biased Noise|Additive Uniform|Noise: _U_[_−_1_,_1]deg<br>Bias: _U_[_−_0_._1_,_0_._1]deg|



(Section III-C3) to the Gaussian scenes in Algorithm 1. The parameters used for different augmentation layers are provided in Table I. 

_2) Post-process Image Augmentations:_ Consistent with prior work [7, 27], our baselines utilize standard postprocess image augmentations for data randomization (see Section IV-A). A complete list of these augmentations and parameters is provided in Table XV. 

## _D. Visual Object Pose Estimator Training_ 

_1) Network Architecture and Training:_ The pose estimator employs a ResNet-34 [8] backbone, initialized with weights pre-trained on ImageNet. The network receives 120 _×_ 120 pixel RGB images, which are normalized and upsampled to 224 _×_ 224 pixels to align with the backbone’s input size. Feature maps extracted from the final convolutional layer are spatially compressed via adaptive average pooling. These 

**Algorithm 1** Pre-Rasterization Augmentation for Gaussians **Require:** Gaussian parameters **S** _∈_ R<sup>_N×D_</sup> Cluster assignments **C** _∈{_ 1 _, . . . , K}_<sup>_N_</sup> Augmentation probability _p_ aug Cluster activation fraction _p_ cluster Perturbation range [ _δ_ min _, δ_ max] Augmentation operator _⊕∈{_ + _, ×}_ **Ensure:** Augmented Gaussian parameters **S**<sup>_′_</sup> 1: **S**<sup>_′_</sup> _←_ **S** 2: Sample _p ∼U_ (0 _,_ 1) 3: **if** _p > p_ aug **then** 4: **return S**<sup>_′_</sup> 5: **end if** 6: **for** each cluster _k ∈{_ 1 _, . . . , K}_ **do** 7: Sample _pk ∼U_ (0 _,_ 1) 8: **if** _pk > p_ cluster **then** 9: **continue** 10: **end if** 11: Sample _δ ∼U_ ( _δ_ min _, δ_ max) 12: _Ik ←{i | Ci_ = _k}_ 13: **S**<sup>_′_</sup> [ _Ik_ ] _←_ **S**<sup>_′_</sup> [ _Ik_ ] _⊕ δ_ 14: **end for** 15: **return S**<sup>_′_</sup> 

TABLE XV: Image Augmentation Operators and Parameters 

|**Augmentation**|**Probability**|**Range**|
|---|---|---|
|**PHOTOMETRIC AUG**|**MENTATIONS**||
|Color Jitter|0_._2|[0_._8_,_1_._2]|
|Hue Shift|0_._2|[_−_0_._2_,_0_._2]|
|Brightness Scaling|0_._5|[0_._5_,_1_._5]|
|Contrast Scaling|0_._5|[0_._5_,_1_._5]|
|Gamma|0_._5|[0_._5_,_1_._5]|
|Saturation Scaling|0_._5|[0_._5_,_1_._5]|
|**SENSOR AND NOISE **|**AUGMENTATI**|**ONS**|
|ISO-like Noise|0_._25||
|Motion Blur|0_._5|Kernel size: 3–17|
|**BLUR AND FILTERIN**|**G**||
|Box Blur|0_._5|Kernel Size: 3–5|
|Binary Opening|1_._0|Kernel size: 3|



features are then processed by a projection head consisting of a Multi-Layer Perceptron (MLP) with two hidden layers of 512 and 256 units, and ReLU activations. We formulate the training as a supervised regression problem, minimizing the Huber loss ( _δ_ = 0 _._ 05) between the predicted and ground-truth keypoint coordinates. The network parameters are optimized using AdamW with a base learning rate of 1 _×_ 10<sup>_−_4</sup> , employing a schedule that combines linear warmup and cosine annealing. 

