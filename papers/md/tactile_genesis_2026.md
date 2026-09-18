# **Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks** 

**Trinity Chung**<sup>_†,_1</sup> **Kashu Yamazaki**<sup>1</sup> **Dhruv Patel**<sup>1</sup> **Alexis Duburcq**<sup>2</sup> **Yiling Qiao**<sup>2</sup> **Katerina Fragkiadaki**<sup>1</sup> **Aran Nayebi**<sup>1</sup> 

1Carnegie Mellon University 2Genesis AI 

> _†_ Corresponding Author: `trinityc@cmu.edu` 

**Abstract:** Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. `https://neuroagents-lab.github.io/tactile-genesis/` 

**Keywords:** tactile simulation, dexterous manipulation 

## **1 Introduction** 

Dexterous manipulation is fundamentally contact-rich. Vision can localize objects before contact, and proprioception can track the robot’s own motion, but many manipulation failures happen through local phenomena that neither modality observes directly: slip, incipient loss of force closure, decoupled object-hand motion, small contact timing errors, and hidden contacts inside clutter. Biological manipulation makes the same point from the other direction: humans and animals can manipulate objects with little or no visual feedback once contact is established. The question for robot learning is therefore not whether touch can help, but what kind of tactile information a policy needs. 

Current tactile hardware spans capacitive arrays [1], magnetic skins [2], vision-based elastomer sensors [3], strain gauge [4], contact microphones [4, 5], multisensory fingertips [6, 7, 8]. These sensors differ in spatial resolution, bandwidth, cost, durability, wiring complexity, calibration burden, and suitability to cover the entire hand versus only the fingertip. A lab that buys or builds one sensorized hand usually cannot repeat the same dexterous learning experiment across all of these alternatives. 



<!-- Start of picture text -->
(a) Configurable Sensor Contact Physics (b) Sim vs Real Demonstration<br>Fingertips<br>only<br>Simulated XHand1 with KinematicTaxel sensors Real XHand1<br>(c) Mass Parallelizable (d) Supports Any Robot (e) Any Placement (f) Temperature & Audio<br>Allegro Inspire Franka<br>XHand1<br>Wuji SharpaWave<br>...and all<br>Shadow others!<br><!-- End of picture text -->

Figure 1: **Overview of Tactile Genesis features.** (a) The sensor physics can be configured to match their real sensor analogues, including 6-axis force/torque measurements, elastomer displacement, and proximity signal. (b) A visual comparison of the simulated tactile force reading per taxel on an XHand1 compared to the real XHand1’s sensor fidelity. (c) Our sensor implementations are highly parallelized and supports heterogeneous objects and randomization. (d) The simulated tactile sensors can be applied on any robot hardware surface and (e) the placement can be of arbitrary shape and resolution. (f) A temperature sensor which simulates contact heat transfer, heat diffusion, heat generation, and radiation, and a contact audio sensor which outputs high frequency signals based on material properties which the rigid body physics engine alone cannot capture. 

Simulation gives us the missing controlled comparison, but only if the simulated tactile sensing is realistic enough to transfer and fast enough for large-scale policy training. Previous work has already shown that carefully calibrated tactile simulators can support sim-to-real manipulation for visuotactile sensors [9, 10, 11]. **We ask a complementary design question:** if we can simulate many tactile abstractions at scale, which representation of touch is sufficient to learn general-purpose dexterous manipulation tasks? 

We present Tactile Genesis, a scalable and hardware-agnostic platform for tactile sensor simulation. Tactile Genesis covers a representative set of contact abstractions under a unified interface (Fig. 1): binary contact, raw contact depth, per-taxel kinematic force/torque, elastomer marker displacement, and geometry-aware proximity. Each sensor exposes configurable placement, resolution, and noise parameters (drift, hysteresis, dead taxels, crosstalk). The implementation is GPU-parallelized across thousands of environments and taxels, making it usable as the tactile front-end for dexterous reinforcement learning (Fig. 3). Using this platform, we train teacher-student policies on three dexterous tasks and ablate sensor type, placement, resolution, and noise. Our findings give concrete guidance for which tactile abstractions are worth the hardware cost on a given manipulation task. In summary, our contributions are: 

1. We introduce Tactile Genesis, a GPU-parallel tactile simulation platform that unifies diverse tactile sensing abstractions under a common configurable interface, scaling to over 20,000 parallel environments and 1,000+ taxels on a single GPU. 

2. We implement a temperature sensor, the first in any robot learning simulation, and use it to learn a policy that locates a hot object among geometrically identical distractors from proprioception and temperature alone. We ablate the thermal properties of the sensing surface and show that the low sensitivity of current real hardware is insufficient for learning this task. 

3. We perform a controlled study of tactile representations across dexterous tasks, robot hands, sensor placements, resolutions, and noise settings. 

2 

|Elastomer Marker|Motion Comparison|||
|---|---|---|---|
|Real GelSight<br>FOTS|HydroShear|Our ElastomerTaxel||
|dilate|||)|
|shear|||indentation depth (mm|
|igure 2: **Elastomer marker motion comparison.** <br>ent fields on a real GelSight under dilation (norm<br>hear (tangential drag), compared with FOTS [9],|Marker displace-<br>al indentation) and<br> HydroShear [11],|Relative RMSE (_↓_)||
|nd our `ElastomerTaxel`. The table on the right <br>arker-displacement error for each simulator after o|reports the relative<br>ptimizing parame-|FOTS HydroShea|r<br>Ours|
|ers to match the real image. The real GelSight image|was obtained from|dilate 0.514<br>0.403|**0.329**|
|heFOTSpapercodebaseandwereplicatethesetu|insimusingour|shear<br>0.210<br>0.217|**0.174**|



Figure 2: **Elastomer marker motion comparison.** Marker displacement fields on a real GelSight under dilation (normal indentation) and shear (tangential drag), compared with FOTS [9], HydroShear [11], and our `ElastomerTaxel` . The table on the right reports the relative marker-displacement error for each simulator after optimizing parameters to match the real image. The real GelSight image was obtained from the FOTS paper codebase, and we replicate the setup in sim, using our `ContactDepthProbe` sensor to measure depth. 

4. We show that tactile placement matters more than sensor type, with whole-hand coverage substantially outperforming fingertip-only sensing, and that per-taxel force/torque is a strong default representation. 

## **2 Related Work** 

**Tactile hardware.** Tactile hardware for robot hands spans a diverse set of transduction principles, each with its own resolution, bandwidth, footprint, and cost. Capacitive arrays [1] and strain-gauge fingertips [4] provide direct force readings but are typically restricted to the fingertip. Magnetic skins such as ReSkin [2] estimate deformation indirectly from magnetometer displacements and can cover larger areas at lower spatial resolution. Vision-based elastomer sensors such as GelSight [3] resolve fine surface deformation but are bulky and again confined to flat pads. Multimodal fingertips [8, 6, 7] combine several of these channels at the cost of substantial wiring and calibration. As a result, comparing sensors apples-to-apples on the same robot hand and task is rarely feasible in hardware: each sensor effectively defines a different hand. 

**Tactile simulation.** Tactile simulators broadly fall into two families: full deformable physics, typically using the Finite Element Method (FEM), and rigid-body simulation with soft-contact postprocessing. FEM has historically been considered too slow for robot learning, but Taccel [12] narrows this gap by combining Incremental Point Contact (IPC), deformable only on the sensor surface, with GPU parallelization, scaling to 4096 environments. The rigid-body family extracts tactile signal from existing contact queries. Tacmap [10] casts rays from the sensor surface to produce per-pixel contact depth, which is a good match for rigid-pad fingertips such as SharpaWave and XHand1. We support the same query via either raycasting or a Signed Distance Function (SDF), and benchmark against Tacmap in Fig. 4. FOTS [9] simulates the visual output of GelSight-style sensors directly, bypassing the deformation physics by modeling how the elastomer indentation maps to the camera image. HydroShear [11] extends this idea to GPU-parallel marker displacement, combining SDF-based depth with anchored point-cloud tracking to capture shear and twist. Our analogous Elastomer sensor builds on HydroShear with substantially better throughput and memory usage (Fig. 4). TacSL [13] is likewise GPU-parallel, integrated into Isaac Lab, and renders a tactile depth image, RGB image, and a penalty-based tactile force field; we benchmark our throughput 

3 

against it in Fig. 4. We do not render a tactile RGB image directly, since its appearance is specific to the sensor vendor (e.g. GelSight), but it can be derived from our `ContactDepthProbe` depth with an example-based renderer such as Taxim [14]. Yin et al. [15] uses sampled point-cloud tracking, not for deformation but to estimate ReSkin [2] magnetometer readings; we include a corresponding Proximity sensor variant as well. To our knowledge, no prior simulator offers all five of these abstractions (binary contact, depth, kinematic force/torque, elastomer displacement, proximity) under a common interface, nor does it have temperature sensors, which is what makes the representation ablation in this paper possible. 

**Tactile representations.** What tactile information a policy actually needs is still an open empirical question. Miller et al. [16] report that sparse binary contacts are sufficient for several in-hand manipulation skills. Sparsh-X [8] goes the other direction and fuses tactile images, audio, motion, and pressure to encode object-level physical properties. ManiWAV [17] shows that a contact audio sensor embedded in the gripper lets the robot learn contact modes and surface materials. In between sit force/torque arrays and elastomer displacement fields, which expose richer local mechanics than binary contact without the bandwidth and calibration cost of full multimodal fingertips. Prior work typically commits to a single point in this design space because the underlying hardware does. We instead hold the policy architecture, task, and hand fixed and vary the tactile abstraction directly in simulation, asking which abstraction is sufficient on which task. 

|Sensor Type|Data Description|Shape|
|---|---|---|
|Surface Distance Probe|Shortest distance to the surface of tracked object.|(_N_)|
|Contact Depth Probe|Raw contact depth scalar from simulated physics, either from SDF<br>or raycasting and sphere-triangle intersection.|(_N_)|
|Contact Probe|Binarized contact with depth threshold and hysteresis|(_N_)|
|Kinematic Taxel|Per-taxel force/torque estimate from SDF depth, contact normal,<br>and linear/angular velocity of object in contact.|(_N,_6)|
|Proximity Taxel|Measures object surface mass within sensing distance using point<br>cloud sampled on tracked objects for signal strength. Computes<br>force/torque using object velocities.|(_N,_6)|
|Elastomer Taxel|Marker displacement modeling the sensing surface as an elastomer.|(_N,_3)|
|Temperature Grid|Temperature in <sup>_◦_</sup>_C_ over voxelized link.|(_N_)|
|Contact Audio|Block of_K_ synthesized vibration samples per step.|(_N, K_)|



Table 1: **Tactile Genesis sensor implementations.** _N_ represents the number of probes/taxels. The full implementation details and configurable parameters per sensor are available in the Appendix. 

## **3 Method** 

### **3.1 Tactile Sensor Simulation** 

We integrate our tactile sensors into the open-source Genesis World physics simulator [19], exposing 7 sensor abstractions summarized in Table 1, which together span the design space of current tactile hardware. All sensors share a common pose-and-radius geometry, can be attached to arbitrary surfaces of any robot, and expose both a clean and a noisy readout under a configurable noise model (Appendix A.8). Our Elastomer sensor approach is based on HydroShear [11] and the Proximity sensor extends Yin et al. [15]; full equations are in Appendix A. In these prior works, these sensor simulation approaches have been validated to transfer to a real GelSight Mini on a robot gripper and ReSkin on the Allegro hand. Our `ElastomerTaxel` extends HydroShear with an elastomer compressibility term and a clamped boundary condition, which lowers the marker-displacement error against real GelSight under both dilation and shear motion (Fig. 2). 

Compared to our predecessors, Tactile Genesis improves throughput by up to 20 _×_ at matched sensor configurations and reduces GPU memory per environment by roughly 5 _×_ (Fig. 4), with the gap widening as the number of parallel environments grows. Three implementation choices drive this. 

4 



<!-- Start of picture text -->
Tactile Sensors Performance<br>Sensor Type<br><!-- End of picture text -->

Figure 3: **Performance benchmark per each simulated sensor type.** We demonstrate that our sensors are able to be parallelized on a single NVIDIA RTX A6000 beyond 16,384 environments, with a total throughput of 150,000 environment steps per second (FPS). To isolate the effect of the sensors, we perform the benchmark in a simple scene of a pyramid of 10 cubes. We compare the performance of different sensor types, fixing the sensor resolution at 10 _×_ 10 (100 taxels) and 500 tracked point cloud samples (applicable to Elastomer and Proximity sensors). Adding more sensors or noise parameters adds small overhead (-10% FPS) for most sensors. The Elastomer sensor slows as more sensors are added (-22% FPS) since local displacement effects must be computed per sensor. 

First, the per-probe contact, depth, and force kernels are vectorized over probes _and_ environments, so a single launch covers the entire batch rather than iterating per sensor. Second, mesh and point-cloud queries (SDF lookups, sphere–triangle intersection, proximity neighbor search) are accelerated by Bounding Volume Hierarchies (BVHs) over the tracked geometry, which keeps cost sublinear in the number of points. Third, for the elastomer sensor’s dilation kernel and the spatial crosstalk model, we exploit the regular planar taxel grid to replace the dense convolution by a 2D Fast Fourier Transform with separable kernels. Together these allow us to scale Tactile Genesis past 16 _,_ 384 parallel environments (Fig. 3) and beyond 10,000 taxels per hand (Fig. 4c) on a single GPU, which is the regime needed for student-policy training. 

### **3.2 Dexterous Task Training** 

Our goal is to compare _tactile observation types_ , not specific hardware, on a fixed set of dexterous tasks. We pair each simulator-level sensor class with a downstream postprocessing step to produce eight tactile observation types plus a proprioception-only baseline ( `none` ), listed in Table 2. The `agg` ~~`*`~~ variants aggregate per-taxel signals to a single per-link value, matching the convention used by real fingertip force sensors in XHand1. The per-taxel variants instead expose the full tactile field to the policy. Holding placement, resolution, and policy architecture fixed across these types lets us isolate the effect of the abstraction itself. 

For each task–hand tuple, we first train a privileged teacher with PPO using full object state, then distill a tactile student that replaces the privileged state group with one of the tactile observation types from Table 2 (Fig. 5). The student is trained with behavioral cloning against the teacher’s actions, plus auxiliary heads that decode privileged object state from the policy’s hidden representation. The decoders are not used at deployment; they act as a regularizer that pushes the tactile encoder to recover task-relevant object state from touch. Each tactile observation group is processed by its own small MLP encoder before being concatenated with the proprioception features and fed to the policy head. Full training hyperparameters and the per-task reward terms are listed in the Appendix. 

5 



<!-- Start of picture text -->
Tactile Sensors Performance (continued) Comparison with Previous Work<br>(a) by Point Cloud Size (b) by Tactile Resolution (c) Temperature Sensor (d) Tactile Policy Rollout (e) 5 Sensors with 1000+ taxels<br>Number of environments<br>(e) Tactile Forces<br>TacSL Force Field Our KinematicTaxel<br>Number of environments<br>Number of environments<br>Env steps per second Env steps per second<br>GPU Memory (GB)<br>Environment steps per second<br>Env steps per second (log scale)<br>GPU Memory (GB)<br>GPU Memory (GB)<br><!-- End of picture text -->

Figure 4: **Performance benchmark (continued).** (a, b) With the number of environments fixed at 1024 and varying point-cloud size and taxel count, our sensors retain low GPU memory and high throughput up to over 10,000 taxels per hand. The elastomer sensor has to track the motion of each object point in contact and therefore scales less well with point-cloud size, but point clouds larger than _∼_ 6000 are not typically needed for dexterous tasks. (c) Our temperature sensor also scales well with number of environments, achieving 80% of the no sensor baseline throughput FPS with 5 active sensors with 8 voxels each. **Comparison with previous work.** Comparison to performance numbers reported by Tacmap [10] and HydroShear [11]; neither paper reports the GPU used or metrics beyond 1024 environments. All Tactile Genesis benchmarks were run on one NVIDIA RTX A6000. (d) Tacmap is based on SharpaWave, which has _>_ 1 _,_ 000 tactile pixels per fingertip [18]; our FPS for 10,000 taxels across 5 ContactDepthProbe sensors is 20 _×_ Tacmap’s and uses 7 _×_ less GPU memory per environment. (e) HydroShear reports per-step time for a single 7 _×_ 9 (35 taxels) elastomer sensor on a robot arm; we rollout a trained robot-hand policy with five 5 _×_ 4 (100 taxels) elastomer sensors and achieve higher FPS as the number of parallel environments grows ( 1 _._ 6 _×_ HydroShear’s at 1024 envs). (f) Comparison against TacSL [13] reported FPS for their penalty-based force field vs. our KinematicTaxel sensor FPS and GPU memory usage for 10x10 and 100x100 taxels. We consistently achieve around 3x higher throughput (note the log scale on FPS) and can run at 16k envs without running out of memory. 



<!-- Start of picture text -->
Privileged Teacher Policy Tactile Student Policy<br>Goal<br>π MLP T aT Goa l MLP<br>Object StateProprioception CriticMLP V ( s ) Tactile Signals RNN π MLP S aS<br>Proprioception RNN<br>LPPO  +  LRND LBC  +  Laux<br>concatenate<br><!-- End of picture text -->

Figure 5: **Teacher-student training setup.** A privileged teacher is trained with PPO and an MLP actorcritic. We additionally incorporate a Random Network Distillation (RND) [20, 21] loss to explore states more quickly. Tactile student policies encode each observation group before passing to the MLP head. In addition to the DAgger [22] behavioral cloning (BC) loss, we incorporate auxillary losses to decode object state. See Appendix B for the full training parameters. 

We evaluate 3 tasks spanning complementary contact regimes: `in` ~~`p`~~ `alm rotate` requires reorienting an object on the palm with the thumb sweeping in to capture it, so locating the object before contact is informative. `in` ~~`h`~~ `and` ~~`r`~~ `epose` requires reposing an object to a target pose while it is in near-continuous contact with multiple fingers, so slip and grip-strength signals dominate. `screwdriver` requires a fast finger gait that keeps a screwdriver spinning, so contacts are brief and rapidly changing. We sweep three tactile placements ( `tips` , `fingers` , `hand` ) at three resolution levels, with both clean and noisy sensor settings; the full matrix is in Appendix Tables 10–12. 

6 

|Type|Sensor Type|Output (after optional postprocessing)|
|---|---|---|
|`none`|–|Proprioception-only baseline with tactile group removed.|
|`bool`|ContactProbe|Binarized contact_per taxel_.|
|`agg`<br>`bool`|ContactProbe|Binary contact _per link_ after thresholding by the number of taxels in<br>contact.|
|`depth`|ContactDepthProbe|Contact depth_per taxel_|
|`agg`<br>`force`|ContactDepthProbe|Estimated force_per link_based on summing contact depth along probe<br>normals.|
|`force`|KinematicTaxel|Force_per taxel_.|
|`force`<br>~~`t`~~`orque`|KinematicTaxel|Force and torque_per taxel_.|
|`elastomer`<br>`proximity`|ElastomerTaxel<br>ProximityTaxel|XYZ marker displacement_per taxel_(marker) on an elastomer surface.<br>Force and torque signals _per taxel_ based on object surface proximity<br>for signal strength.|



Table 2: **Tactile observation types used by student policies.** We compare 8 different tactile representations, using the tactile signals from the simulated sensors and optionally postprocessing before passing into the observations. Tactile data _per link_ means we aggregate the data and output one tactile signal per every sensing area (e.g. 5 fingertips). 

### **3.3 Temperature Sensing for Learning Object Discrimination** 

Temperature can be a useful cue for telling objects apart, but temperature sensors on current robots are mostly used for hardware health monitoring rather than sensing, since the actuators heat up under sustained use. Using our simulated tactile sensors, we explore what temperature sensitivity is needed to distinguish an object only by temperature. We train a policy with proprioception and tactile sensors to find the hot ball out of 8 balls in a bin. Our results in Fig. 6 show that high sensitivity is indeed critical, and we fail to succeed on the task with material properties matching real temperature sensors on current robot hands. 



||emissivity 0.5 (steel)|emissivity 0.85 (rubber)|
|---|---|---|
|conductivity|heat gener|ation (W/m<sup>2</sup>)|
|(W/m_·_K)|500<br>5000|500<br>5000|
|1 (glass)|–<br>–|–<br>–|
|10 (steel)|–<br>–|–<br>–|
|100 (aluminum alloy)|–<br>–|–<br>–|
|150 (aluminum)|✓<br>✓|–<br>–|



Figure 6: **Temperature properties ablation for finding a target hot object.** Checkmark indicates that the hand successfully maintains touch with the hot ball. Emissivity values approximate stainless steel (0 _._ 5) and rubber (0 _._ 85); conductivities approximate glass (1), stainless steel (10), and aluminum (100). For scale, human skin dissipates on the order of 60 W/m<sup>2</sup> at rest and 100 to 600 W/m<sup>2</sup> during exercise, while small actuators under heavy load can reach 1 _,_ 000–5 _,_ 000 W/m<sup>2</sup> . The temperature sensor implementation, task, and success metric are detailed in Appendix D. 

## **4 Results** 

### **4.1 Tactile Student Ablations** 

**Proprioception is not enough.** In Fig 7, we can see that the `none` baseline trails every tactile student on all three tasks, including the cheapest binary contact variant. The auxiliary state decoders alone are not enough to recover task-relevant object state from proprioception; any meaningful student performance requires the tactile group. 

**Placement dominates sensor type.** Restricting sensing to fingertips, the placement that most current commercial hardware supports, trails whole-hand coverage by a large margin on `in palm rotate` . Adding the palm and mid-finger surfaces closes most of the remaining gap to 

7 



<!-- Start of picture text -->
Tactile  Task: in_palm_rotate in_hand_repose screwdriver<br>Student  Sensor Area: Fingertips only Hand Hand Fingers<br>Ablations Goal<br>Training Steps<br>by Sensor Type<br>Consecutive Successes<br>by Resolution and Noise<br><!-- End of picture text -->

Figure 7: **Tactile student ablations.** For 3 tasks `in palm` ~~`r`~~ `otate` , `in hand` ~~`r`~~ `epose` , and `screwdriver` using the XHand1, we compare tactile data types against the privileged teacher and distilled tactile student. For `in palm` ~~`r`~~ `otate` we try having fingertips only (the real XHand1 only has fingertips) vs including sensors on the whole hand. We also vary the tactile resolution and add noise parameters (white noise, random walk drift, hysteresis, sensing radius noise) and compare. A complete table of parameters is available in the Appendix. 

the privileged teacher, even for sensor types that individually carry less information. Adding taxels on the palm and proximal phalanges of the fingers is, at the margin, more useful than upgrading the fingertip sensor. 

**The best sensor type is task-dependent, with force/torque as a robust default.** On `in hand repose` , where the object is in near-continuous contact and the dominant failure mode is incipient slip, the `force torque` student is best and clearly separates from the binary and depth variants. On `in palm` ~~`r`~~ `otate` , `proximity` edges out the contact-only types, since its sensing radius registers the approaching object before direct contact and lets the thumb pre-shape rather than search. On `screwdriver` , where contacts are brief and the fingers gait quickly, all tactile signals perform similarly and none saturates the teacher; we conjecture that integration over time, or visual feedback, is the missing channel here rather than a different contact abstraction. Aggregated across tasks, per-taxel `force torque` matches or outperforms every other type and is our recommended default when hardware allows. 

**Elastomer displacement underperforms when per-taxel locality matters.** The `elastomer` student trails `force` ~~`t`~~ `orque` on both `in` ~~`p`~~ `alm` ~~`r`~~ `otate` and `in` ~~`h`~~ `and` ~~`r`~~ `epose` . This is consistent with how the substrate model behaves: marker displacement at one taxel is a function of indentation _and_ shear at neighboring taxels, so a displacement in _x_ can be caused by adjacent dilation as easily as by local shear. The resulting signal is well suited for inferring object shape patches, the use case GelSight-like sensors were originally designed for, but less suited for reading off the local force vector that the in-hand tasks actually need. 

**Sim-to-real validation.** We validate transfer by deploying the `in` ~~`p`~~ `alm` ~~`r`~~ `otate` policy on the real XHand1, whose only tactile sensing is fingertip aggregate force. The deployed policy achieves one to two successes, which matches the success rate of the fingertip `agg` ~~`b`~~ `ool` student in simulation, the observation type that most closely mirrors the real fingertip readout. This confirms that policies 

8 

trained in Tactile Genesis transfer to hardware, and that the simulated fingertip abstraction is a faithful enough proxy for the real sensor to predict its performance. 

## **5 Discussion and Limitations** 

Across all tasks, sensor types, and placements, the takeaways for practitioners outfitting a dexterous hand are threefold. First, cover the palm and proximal phalanges before paying for higher-end fingertip sensors. Second, prefer per-taxel force/torque as a default abstraction. Third, consider a proximity channel when the task involves capturing an object that approaches the hand rather than one already grasped. The first two findings are at odds with the de facto convention in current commercial tactile fingertips, which concentrate spatial resolution on the distal pad and stop there. From a simulation-design perspective, our experiments also suggest that the dominant source of useful tactile information for these tasks is the coarse spatial distribution of contact rather than the fine-grained mechanics of the substrate. This is encouraging for rigid-body tactile simulation, since substrate physics is exactly what is most expensive to model faithfully. 

We deliberately scope this paper to sensor implementation and observation-type comparison. Because our students distill from a privileged teacher, they inherit its strategy and are therefore bounded by it. An important direction for future work would be a larger sweep over hands and tasks, with continued (curiosity-driven) RL [20] using either tactile observations as the only sensory channel or paired with vision, would help separate “what the teacher can be matched on” from “what touch is actually capable of.” 

## **Acknowledgements** 

This material is based upon work supported by the National Science Foundation Graduate Research Fellowship Program under Grant No(s) DGE2140739. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation. This work is also partially funded by DARPA SAFRON award HR0011-25-3-0203 and an Amazon robotics award. A.N. thanks the Burroughs Wellcome Fund (CASI award) and Google Robotics Award for funding. 

9 

## **References** 

- [1] Y. Song, J. Wang, Z. Li, W. Hu, Y. Qiu, Y. Tian, P. Zhao, A. Liu, and H. Wu. Fingertipscale six-axis tactile interface with high-precision force sensing and position localization for dexterous human–machine interactions. _Microsystems & Nanoengineering_ , 12(1):193, 2026. 

- [2] R. Bhirangi, T. Hellebrekers, C. Majidi, and A. Gupta. ReSkin: Versatile, replaceable, lasting tactile skins. In _Proceedings of the Conference on Robot Learning_ , November 2021. URL `https://arxiv.org/abs/2111.00071` . 

- [3] W. Yuan, S. Dong, and E. H. Adelson. GelSight: High-resolution robot tactile sensors for estimating geometry and force. _Sensors_ , 17(12):2762, 2017. doi:10.3390/s17122762. 

- [4] Z. Xu, Z. Si, K. Zhang, O. Kroemer, and Z. Temel. A multi-modal tactile fingertip design for robotic hands to enhance dexterous manipulation, 2025. URL `https://arxiv.org/abs/ 2510.05382` . 

- [5] J. Mejia, V. Dean, T. Hellebrekers, and A. Gupta. Hearing touch: Audio-visual pretraining for contact-rich manipulation. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 6912–6919. IEEE, 2024. 

- [6] E. Chelly, A. Cherubini, P. Fraisse, F. B. Amar, and M. Khoramshahi. Tactile-based force estimation for interaction control with robot fingers, 2025. URL `http://arxiv.org/abs/ 2411.13335` . 

- [7] D. Kitouni, E. Chelly, M. Khoramshahi, and V. Perdereau. Fingertip contact force direction control using tactile feedback, 2024. URL `http://arxiv.org/abs/2406.11545` . 

- [8] C. Higuera, A. Sharma, T. Fan, C. K. Bodduluri, B. Boots, M. Kaess, M. Lambeta, T. Wu, Z. Liu, F. R. Hogan, and M. Mukadam. Tactile beyond pixels: Multisensory touch representations for robot manipulation, 2025. URL `http://arxiv.org/abs/2506.14754` . 

- [9] Y. Zhao, K. Qian, B. Duan, and S. Luo. FOTS: A fast optical tactile simulator for sim2real learning of tactile-motor robot manipulation skills, 2024. URL `http://arxiv.org/abs/ 2404.19217` . 

- [10] L. Su, Z. Peng, R. Ren, S. Mao, J. Du, K. Zhang, and X. Zhu. Tacmap: Bridging the tactile sim-to-real gap via geometry-consistent penetration depth map, 2026. URL `http://arxiv. org/abs/2602.21625` . 

- [11] A. Dang, J. Lee, M. Mukadam, X. A. Wu, B. Bucher, M. Nambi, and N. Fazeli. HydroShear: Hydroelastic shear simulation for tactile sim-to-real reinforcement learning, 2026. URL `https://arxiv.org/abs/2603.00446` . 

- [12] Y. Li, W. Du, C. Yu, P. Li, Z. Zhao, T. Liu, C. Jiang, Y. Zhu, and S. Huang. Taccel: Scaling up vision-based tactile robotics via high-performance gpu simulation, 2025. URL `http:// arxiv.org/abs/2504.12908` . 

- [13] I. Akinola, J. Xu, J. Carius, D. Fox, and Y. Narang. Tacsl: A library for visuotactile sensor simulation and learning. _IEEE Transactions on Robotics_ , 2025. 

- [14] Z. Si and W. Yuan. Taxim: An example-based simulation model for gelsight tactile sensors. _IEEE Robotics and Automation Letters_ , 7(2):2361–2368, 2022. 

- [15] J. Yin, H. Qi, J. Malik, J. Pikul, M. Yim, and T. Hellebrekers. Learning in-hand translation using tactile skin with shear and normal force sensing. In _2025 IEEE International Conference on Robotics and Automation_ , pages 5850–5856, 2025. doi:10.1109/ICRA55743.2025.11127974. 

- [16] E. Miller, T. McInroe, D. Abel, O. Mac Aodha, and S. Vijayakumar. Enhancing tactilebased reinforcement learning for robotic control. In _OpenReview_ , 2025. URL `https: //openreview.net/forum?id=Toy96yYopR` . 

10 

- [17] Z. Liu, C. Chi, E. Cousineau, N. Kuppuswamy, B. Burchfiel, and S. Song. Maniwav: Learning robot manipulation from in-the-wild audio-visual data. In _Conference on Robot Learning_ , pages 947–962. PMLR, 2025. 

- [18] Jan 2026. URL `https://www.sharpa.com/blogs/news/ sharpa-unveils-its-first-autonomous-full-body-robot-with-human-dexterity-at-ces-2026` . 

- [19] G. A. Team. The role of simulation in scalable robotics, genesis world 1.0, and the path forward. _Genesis AI Blog_ , May 2026. URL `https://www.genesis.ai/blog/ the-role-of-simulation-in-scalable-robotics-genesis-world-10-and-the-path-forward` . 

- [20] Y. Burda, H. Edwards, A. Storkey, and O. Klimov. Exploration by random network distillation, 2018. URL `https://arxiv.org/abs/1810.12894` . 

- [21] C. Schwarke, V. Klemm, M. v. d. Boon, M. van der Bjelonic, and M. Hutter. Curiosity-driven learning of joint locomotion and manipulation tasks. In _Proceedings of the 7th Conference on Robot Learning_ , pages 2594–2610, 2023. URL `https://proceedings.mlr.press/v229/ schwarke23a.html` . 

- [22] S. Ross, G. Gordon, and D. Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. In G. Gordon, D. Dunson, and M. Dud´ık, editors, _Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics_ , volume 15 of _Proceedings of Machine Learning Research_ , pages 627–635, Fort Lauderdale, FL, USA, 11–13 Apr 2011. PMLR. URL `https://proceedings.mlr.press/v15/ross11a.html` . 

11 

## **A Tactile Sensor Implementation** 

This section gives the mathematical definitions of our tactile sensor implementations, which have been incrementally integrated into Genesis World open-source physics simulation platform. All code used for this work will be made available on GitHub. Note that there may be some differences in the latest version of Genesis compared to the version used in this paper; please refer to the code for the most accurate source of truth. 

### **A.1 Probe geometry and contact-depth query** 

Each probe is rigidly attached to a sensor link and described by a link-frame position, unit normal, and radius. Let sensor link _L_ have pose ( _pL, RL_ ) and let probe _j_ have link-frame position _xj_ , unit normal _nj_ , and radius _Rj_ . Its world-frame position and normal are 



Depth and force probes only consider collision geometries that are currently in a rigid-body contact pair with the sensor link. A probe with _Rj_ = 0 is treated as an inactive filler and returns zero, which keeps batched tensors regular over heterogeneous link layouts. 

**Two contact-depth backends.** The penetration depth at probe _j_ can be queried in two ways, selected by the `contact` ~~`d`~~ `epth query` option. The `sdf` backend queries the per-geometry analytic signed-distance field maintained by the rigid solver. For an opposing collision geometry _g_ with SDF _ϕg_ , the penetration depth is 



and the contact normal is the SDF gradient _mj_ = _∇ϕg⋆_ ( _qj_ ) at the winning geometry _g_<sup>_⋆_</sup> when _d_<sup>sdf</sup> _j >_ 0. This is fast and exact on primitives, but requires SDF activation on the collider. The `raycast` backend instead walks a per-frame Bounding Volume Hierarchy over the rigid-body collision meshes, shared with Genesis’s raycaster sensor. At each candidate BVH leaf, the probe runs a sphere–triangle closest-point test (penetration = _Rj −_ dist) and a ray–triangle test along _−aj_ (penetration = _Rj −_ hit ~~d~~ istance); the deepest of the two wins, and the contact normal is the face normal of the deepest-penetrating triangle. The two backends produce equivalent depths to leading order for smooth meshes and differ at sharp features. `sdf` is the default; `raycast` handles arbitrary triangle meshes uniformly and is preferable when the scene mixes many small or thin objects. 

### **A.2** `SurfaceDistanceProbe` 

The `SurfaceDistanceProbe` reports, per probe, the shortest distance from the probe center to the surface of each tracked object. Unlike the contact sensors below, it does not require a rigid-body contact pair and is defined before contact, which makes it a pre-contact proximity cue. 

### **A.3** `ContactProbe` 

The `ContactProbe` binarizes the measured penetration depth _d_<sup>m</sup> _bj_<sup>at probe</sup><sup>_j_into a contact bit, with</sup> optional Schmitt hysteresis to suppress chatter near the contact boundary: 



Here _η_ on is the contact threshold and _η_ off _≤ η_ on the release threshold; setting _η_ off = _η_ on disables the hysteresis. We use _η_ on = 5 _×_ 10<sup>_−_4</sup> m, adding a release threshold _η_ off = 2 _×_ 10<sup>_−_4</sup> m and dead-taxel noise in the noisy condition (Table 12). 

### **A.4** `ContactDepthProbe` 

The `ContactDepthProbe` reports the raw measured penetration depth _d_<sup>m</sup> _bj_<sup>at each probe, taken from</sup> the `sdf` or `raycast` backend of the previous section. 

12 

### **A.5** `KinematicTaxel` 

The `KinematicTaxel` converts depth, contact normal, and relative velocity into a per-taxel sixchannel force/torque estimate without modeling a deformable substrate. Let _m_ ¯ _j_ = _RL_<sup>_⊤mj_bethe</sup> SDF normal in the sensor-link frame. For a contact with opposing link _C_ , the point velocities are 





where _rC, rL_ are the corresponding centers of mass. The relative velocity in the sensor-link frame is 



With _sj_ = ( _dj_ )<sup>_α_</sup> , the normal and tangential components are 



The local force and torque are 





If no opposing contact link is available we drop the velocity terms, returning only the spring force and _τj_ = _xj × fj_ . The sensor reports the six channels ( _fj, τj_ ) per taxel. The parameters used in our experiments are 



For regular planar taxel grids, we apply spatial crosstalk to the noisy channel. Let _zc_ be one force or torque channel on the grid, _χ_ the crosstalk strength, and _Gσ_ an L1-normalized Gaussian kernel of standard deviation _σ_ . The channel update is 



applied independently to all six channels. 

### **A.6** `ProximityTaxel` 

The `ProximityTaxel` models a geometry-aware taxel that responds to nearby tracked mass, mirroring how capacitive and magnetic skins behave. Tracked links are sampled into a surface point cloud at scene reset and organized in a static BVH for fast neighbor queries. For taxel _j_ , let _Pj_ = _{i_ : _∥pi − qj∥ < Rj}_ be the set of tracked points inside the taxel sensing sphere. Each point contributes 



Let 



and remove the taxel-normal component of relative velocity: 



The density scale is 



The world-frame force and torque are 





The reported channels are _RL_<sup>_⊤f_</sup> _bj_<sup>_w_and</sup><sup>_R_</sup> _L_<sup>_⊤τ w_</sup> _bj_<sup>.Ourexperimentsuse</sup><sup>_Rj_=0</sup><sup>_._01m,</sup><sup>_N_pc=5000,</sup> _k_ = 300, _ks_ = 10, and a density scalar of 100. Radius noise enters by perturbing _Rj_ before the BVH query; per-probe gain scales the accumulated penetration, slip, and torque terms before the force/torque conversion. 

13 

### **A.7** `ElastomerTaxel` 

The `ElastomerTaxel` models marker displacements on a deformable substrate by combining SDFdriven dilation with anchored shear history [11]. Let 



be projection onto the tangent plane. For source probe _i_ , the per-probe penetration into the elastomer is 



For target marker _j_ , write _rij_ = Π _nj_ ( _xj − xi_ ) for the tangential offset to source _i_ . The in-plane marker spreading interpolates between a local Gaussian falloff and an incompressible global stretch through a compressibility parameter _c ∈_ [0 _,_ 1]: 



where _g_ ( _r_ ) = exp( _−λd∥r∥_<sup>2</sup> ) is the Gaussian kernel, _ρ_ ( _r_ ) = ( _∥r∥_<sup>2</sup> + _ε_<sup>2</sup> )<sup>_−_1</sup> is a regularized inversedistance kernel, and _g_ ¯ = _e_<sup>_−_1</sup><sup>_/_2</sup> _/_<sup>_√_</sup> 2 _λd_ and _ρ_ ¯ = 1 _/_ (2 _ε_ ) peak-normalize the two so that _c_ blends them on a common scale. Setting _c_ = 1 recovers the local Gaussian response, while _c_ = 0 recovers an incompressible response whose in-plane displacement decays as 1 _/∥r∥_ . The out-of-plane bulge keeps the Gaussian falloff with the depth power law, and the dilation contribution is 



The regularization length _ε_ is set to the elastomer thickness when it is modeled, otherwise to the taxel spacing. Tracked links are also sampled into surface points to capture shear history. A sampled point _p_ initializes an anchor _ep_ when its elastomer SDF drops below _−η_ enter and clears the anchor when the SDF rises above + _η_ exit. Let _zp_ be the current sensor-frame point position and _hp_ the elastomer penetration depth. The shear contribution to target marker _j_ is 



The displacement output is 



**Clamped boundary condition.** When the elastomer is bonded to a rigid housing, markers cannot move at the pad edge. We optionally enforce this as a Dirichlet condition on the in-plane dilation field. Writing the field above as _u_<sup>free</sup> , the corrected field is _u_ = _u_<sup>free</sup> + _u_<sup>corr</sup> , where the correction solves the homogeneous depth-averaged bonded-layer equations 



on the pad interior with _u_<sup>corr</sup> = _−u_<sup>free</sup> on the boundary loop, so that the total displacement vanishes at the wall over a boundary layer of width _t/_<sup>_√_</sup> _β_ . Here _t_ is the elastomer thickness, _β_ = 3 sets the drag, and _K_ penalizes in-plane compression. On the regular grid we precompute this discrete solution operator once at build time and apply it as a low-rank correction to the FFT field at each step. 

Our experiments use _N_ pc = 1000, _sd_ = 100, _ss_ = 100, _λd_ = 8000, _λs_ = 2000, _α_ = 1 _._ 2, compressibility _c_ = 1 (the local-Gaussian limit), and shear enter/exit thresholds _η_ enter = 10<sup>_−_5</sup> m and _η_ exit = 10<sup>_−_4</sup> m, with no clamped boundary. The compressibility and boundary condition are calibrated against real GelSight marker motion in Fig. 2. For regular planar grids we accelerate the dilation term with FFT: tangent channels convolve _hi_ and the normal channel convolves _h_<sup>_α_</sup> _i_<sup>;shear</sup> is accumulated directly. 

14 

### **A.8 Sensor Noise Model** 

Every sensor in Genesis exposes both a clean ground-truth readout and a noisy readout. Table 3 lists which imperfection knobs each sensor type supports; the numerical values we use in the experiments are in Section B (Table 12). 

**Base noise (every sensor).** At the simulator level, every sensor honors a read delay ∆read (with optional uniform jitter), additive Gaussian white noise _σ_ , constant bias _b_ , random-walk drift _σ_ rw, and uniform quantization with step _q_ : 



**Probe-level imperfections (probe-based sensors).** Probe sensors additionally perturb the perprobe sensing radius and apply a per-probe multiplicative gain: 





where the gain _γbj_ models persistent per-unit calibration error. 

**Taxel-level imperfections (tactile probe sensors).** Tactile probe sensors further sample dead taxels at episode reset: 



and when _Mbj_ = 1 the measured value at taxel _j_ is overwritten by the stuck readout _zbj_ for the entire episode. 

**Viscoelastic hysteresis (contact, depth, kinematic, elastomer, proximity).** Substrate-like sensors model a single-Maxwell viscoelastic loop on the noisy readout: 



with strength _β_ and time constant _τ_ . After a rising step the noisy signal overshoots and decays back to equilibrium; after a falling step it undershoots analogously. 

**Spatial crosstalk.** On regular planar grids, the sensor mixes neighboring channels to model spatial crosstalk between adjacent sensing sites. Let _zc_ be one force or torque channel on the grid, _χ_ the crosstalk strength, and _Gσ_ an L1-normalized Gaussian kernel of standard deviation _σ_ : 



applied independently to each of the six channels. 

|Noise knob|SurfaceDist.|ContactProbe|ContactDepth|Kinematic|Elastomer|Proximity|
|---|---|---|---|---|---|---|
|Read delay / jitter|✓|✓|✓|✓|✓|✓|
|White noise_σ_|✓|✓|✓|✓|✓|✓|
|Constant bias|✓|✓|✓|✓|✓|✓|
|Random-walk drift|✓|✓|✓|✓|✓|✓|
|Quantization|✓|✓|✓|✓|✓|✓|
|Probe-radius noise|✓|✓|✓|✓|✓|✓|
|Per-probe gain|–|✓|✓|✓|✓|✓|
|Dead taxels|–|✓|✓|✓|✓|✓|
|Viscoelastic hysteresis|–|✓|✓|✓|✓|✓|
|Spatial crosstalk|–|–|–|✓|–|✓|



Table 3: Imperfection knobs available per sensor type. 

15 

## **B Training Setup** 

The training pipeline, task definitions, and tactile sensor wiring used in this paper live in the companion `dexterous` ~~`h`~~ `ands` repository. This section documents the optimization and network hyperparameters, the observation–type mapping, the dexterous tasks, the sweep matrix, the per-resolution probe counts, and the noise values used in the noisy condition. 

### **B.1 Optimization and Network Hyperparameters** 

Table 4 lists the teacher PPO, RND exploration, and student DAgger optimization settings; values that differ across tasks are shown per task. Teacher and student share the same actor–critic backbone: a three-layer MLP head with hidden sizes [512 _,_ 256 _,_ 128] and ELU activations, with input normalization and an initial policy standard deviation of 1 _._ 0. Each non-tactile observation group is embedded by a per-group encoder (an MLP [512 _,_ 256 _,_ 128] _→_ 64, or an LSTM with hidden size 128 _→_ 64) before concatenation. Each tactile group is embedded by its own encoder projecting to a 32-dimensional embedding: gridless types use an MLP ([64 _,_ 64]) or an LSTM (hidden 64), while grid-structured types use a convolutional encoder ( `tactile` ~~`c`~~ `nn` , channels [16 _,_ 32], kernel 3) or a convolutional–recurrent encoder ( `tactile` ~~`c`~~ `onvrnn` , 16 channels, kernel 3, layer norm). The RND predictor uses learning rate 10<sup>_−_3</sup> , an 8-dimensional output, and normalized state and reward. The student additionally trains auxiliary heads that decode privileged object state from its latent (Table 5); these decoders are used only during training and discarded at deployment. The simulation steps at 200 Hz with a control decimation of 5 (40 Hz control). 

||`in`<br>~~`p`~~`alm`<br>`rotate`|`in`<br>`hand`<br>~~`r`~~`epose`|`screwdriver`|
|---|---|---|---|
|_Teacher (PPO)_||||
|parallel environments|8192|8192|8192|
|steps per env|24|24|12|
|teacher iterations|6000|20000|5000|
|learning rate (adaptive)|10<sup>_−_3</sup>|10<sup>_−_3</sup>|10<sup>_−_3</sup>|
|learning epochs / minibatches|5 / 4|5 / 4|5 / 4|
|discount_γ_|0.998|0.998|0.99|
|GAE_λ_|0.95|0.95|0.95|
|clip param / desired KL|0.2 / 0.01|0.2 / 0.01|0.2 / 0.01|
|entropy coef.|2_×_10<sup>_−_3</sup>|2_×_10<sup>_−_3</sup>|0|
|value loss coef. / max grad norm|1.0 / 1.0|1.0 / 1.0|1.0 / 1.0|
|episode length (s)|10|20|20|
|_Student (DAgger)_||||
|student iterations|6000|6000|2000|
|learning rate|10<sup>_−_4</sup>|10<sup>_−_4</sup>|10<sup>_−_5</sup>|
|learning epochs|5|5|5|
|<br>gradient length|2|2|4|
|clip param|–|–|0.1|
|max grad norm|2.0|–|0.5|
|BC loss|MSE|MSE|inv-var MSE|



Table 4: Teacher PPO and student DAgger optimization hyperparameters. 

### **B.2 Tactile Observation Types** 

Table 6 shows how each downstream observation type maps to an underlying Genesis sensor abstraction together with the postprocessing applied to the raw read. 

Each observation type derives from one native sensor (Appendix A) followed by light postprocessing. Writing _d_<sup>m</sup> _bj_<sup>forthemeasured</sup><sup>`ContactDepthProbe`depthand</sup><sup>_nj_forthelink-frameprobe</sup> normal: 

16 

|Task|Decoded target|Weight|Target scale|Head hidden dims|
|---|---|---|---|---|
|`in`<br>~~`p`~~`alm`<br>`rotate`|object size|1.0|20.0|[128_,_64]|
|`in`<br>~~`p`~~`alm`<br>`rotate`|goal distance|1.0|1.0|[128_,_64]|
|`screwdriver`|object tilt|0.5|1.0|<br>[512_,_128]|
|`screwdriver`|rotation progress|0.5|1.0|[512_,_128]|
|`in`<br>~~`h`~~`and`<br>`repose`|none||||



Table 5: Auxiliary decoder losses used during student distillation. Each head predicts a privileged scalar from the student latent under an MSE loss (target scaled by the listed factor); the total loss adds the weighted auxiliary terms to the DAgger behavioral-cloning loss. The decoders regularize the tactile encoder toward task-relevant object state and are discarded at deployment. 

|Type|Sensor abstraction|Key parameters|Policy observation|
|---|---|---|---|
|`bool`|`ContactProbe`|_η_on = 5_×_10<sup>_−_4 </sup>m<br>|thresholded contact bits|
|`agg`<br>`bool`|`ContactProbe`|_η_on = 5_×_10<sup>_−_4 </sup>m; count thresh-<br>old_>_2|per-link aggregate con-<br>tact bit|
|`depth`|`ContactDepthProbe`|`contact`<br>~~`d`~~`epth`<br>~~`q`~~`uery`=`sdf`|flattened contact depths|
|`agg`<br>`force`|`ContactDepthProbe`|`sdf` query; 10<sup>4 </sup>scale, ZYX axis<br>order|per-link patch force|
|`force`|`KinematicTaxel`|_kn_ = 500, _cn_ = 1, _α_ = 1_._2,<br>_kt_ = 2,_kω_ = 2|force channels only|
|`force`<br>~~`t`~~`orque`|`KinematicTaxel`|same as`force`|force and torque chan-<br>nels|
|`elastomer`|`ElastomerTaxel`|_N_pc = 1000,_λd_ = 8000,_λs_ =<br>2000,_sd_ = 100,_ss_ = 100,_α_ =<br>1_._2|marker displacements|
|`proximity`|`ProximityTaxel`|_R_ = 0_._01m,_N_pc = 5000,_k_ =<br>300,_ks_ = 10|force and torque chan-<br>nels|



Table 6: Mapping from downstream observation type to underlying Genesis sensor abstraction and key parameters. 

**Contact observations.** `depth` flattens the per-taxel `ContactDepthProbe` depths. `bool` is the pertaxel `ContactProbe` bit, and `agg` ~~`b`~~ `ool` sums those bits over a link and reports a single bit when more than two taxels are in contact. `agg` ~~`f`~~ `orce` aggregates the contact-depth probes into one patch force per link, 



permuting axes and applying an empirical scale to match the per-fingertip force that the XHand1 `calc` ~~`p`~~ `ressure` channel returns on the real robot. 

**Force, displacement, and proximity observations.** `force` and `force` ~~`t`~~ `orque` read the `KinematicTaxel` : `force` ~~`t`~~ `orque` keeps all six channels ( _fj, τj_ ), while `force` drops the torque, _h_ force( _F, T_ ) = vec( _F_ ). `proximity` flattens the `ProximityTaxel` force and torque channels, and `elastomer` flattens the `ElastomerTaxel` marker displacements. 

Except for `agg` ~~`b`~~ `ool` , `agg force` , and `force` , the policy input flattens each raw sensor tensor and concatenates the results: 



Only the per-link aggregate types `agg` ~~`b`~~ `ool` and `agg` ~~`f`~~ `orce` have a counterpart on the real XHand1; their deployment is described in Appendix C. 

### **B.3 Tasks and Hands** 

`in palm rotate` **.** A partial-hand task in which the policy controls only the thumb and middle finger (index, ring, and pinky fingers are frozen) to rotate the object around the commanded axis. the object 

17 

is reset to a sampled bottom-aligned pose at the center of the palm. We train with 16 objects: 14 different cubes and 2 cylinders around 4cm in length. 

`in hand repose` **.** A whole-hand reposing task in which the policy must drive the object pose to a target orientation while keeping it in continuous contact with multiple fingers. The reward combines orientation tracking with grip-strength and slip penalties. We train with the same 16 objects as in the previous task. 

`screwdriver` **.** A finger-gaiting task in which the hand spins a screwdriver about its long axis while keeping the tip engaged. We train with 4 different screwdriver handles. 

**Observations.** All three tasks share the same observation grouping (Table 7). The student (deployable) policy sees only proprioception (joint positions and velocities and the last action), the tactile group (one observation type from Table 2), and, for the reorientation tasks, the goal. The privileged groups available to the teacher and critic add per-link contact forces, full object state, and object properties. `screwdriver` has no goal group and folds the surface-distance probes into its object-state group. 

|Group|Contents|Available to|
|---|---|---|
|`proprio`|joint positions, joint velocities, last action|student + teacher|
|`tactile`<br>~~`s`~~`ensors`|one tactile observation type (Table2)|student|
|`goal`|goal orientation and angular error to target|student <sup>_‡_</sup>|
|`priv`<br>~~`p`~~`roprio`|proprioception plus per-link contact forces|teacher, critic|
|`priv`<br>~~`o`~~`bj`<br>~~`s`~~`tate`<br>`priv`<br>~~`o`~~`bj`<br>~~`p`~~`rops`|object position, 6D orientation, linear and angular velocity<br>object friction, mass, and surface-distance probes|teacher, critic<br>critic|



Table 7: Observation groups. The student policy is restricted to `proprio` , `tactile` ~~`s`~~ `ensors` , and (where present) `goal` ; the privileged groups are used only to train the teacher and critic. _‡_ `in palm` ~~`r`~~ `otate` and `in` ~~`h`~~ `and` ~~`r`~~ `epose` only; `screwdriver` has no goal group and places the surface-distance probes in `priv` ~~`o`~~ `bj state` . 

**Reward terms.** Table 8 lists the reward-term weights for each task; blank entries mark terms not used by that task. 

|Reward term|`in`<br>~~`p`~~`alm`<br>~~`r`~~`otate`|`in`<br>~~`h`~~`and`<br>`repose`|`screwdriver`|
|---|---|---|---|
|success bonus|150|500|–|
|orientation tracking (Gaussian)|–|2_._0|–|
|orientation tracking (inverse-_L_2)|–|2_._0|–|
|rotation progress / spin rate|2_._0|0_._2|10_._0|
|surface-distance reward|0_._1|0_._5|1_._0|
|off-axis orientation penalty|_−_1_._0|–|–|
|vertical-alignment penalty|–|–|_−_400|
|object-distance penalty|_−_100|–|_−_300|
|hand pose-deviation penalty|–|–|_−_1_._0|
|contact-force penalty|_−_5_._0|_−_5_._0|–|
|drop / termination penalty|_−_100|_−_100|_−_100|
|goal-timeout penalty|–|_−_200|–|
|action-rate penalty|_−_5_×_10<sup>_−_4</sup>|_−_1_×_10<sup>_−_5</sup>|_−_1_×_10<sup>_−_2</sup>|
|joint-limit penalty|_−_40|_−_20|_−_40|
|work penalty|_−_5_×_10<sup>_−_3</sup>|_−_1_×_10<sup>_−_3</sup>|_−_1_×_10<sup>_−_3</sup>|



Table 8: Reward-term weights per task. Positive weights are shaping rewards; negative weights are penalties. A dash means the term is not used by that task. 

**Domain randomization.** Every task applies the same actuator randomization, resampled per reset: proportional and derivative gains and motor strength each scaled by _U_ [0 _._ 95 _,_ 1 _._ 05], a position bias in _±_ 0 _._ 01 m, a deadband in [0 _,_ 0 _._ 005], gear backlash in [0 _,_ 0 _._ 01] rad, a torque-kick ratio in [0 _._ 9 _,_ 1 _._ 1], 

18 

and per-step torque noise at RFI scale 0 _._ 1. The task-specific object and disturbance randomization is listed in Table 9. 

|Quantity|`in`<br>~~`p`~~`alm`<br>`rotate`|`in`<br>`hand`<br>~~`r`~~`epose`|`screwdriver`|
|---|---|---|---|
|object friction (_×_)|[0_._5_,_1_._5]|[0_._3_,_2_._0]|[0_._2_,_1_._2]|
|object mass offset (kg)|[0_,_0_._1]|[0_,_0_._1]|[0_,_0_._2]|
|initial placement_xy_(m)|_±_0_._02|_±_0_._02|sampled grasp|
|<br>initial yaw (rad)|_±π/_12|_±π_|<br>sampled grasp|
|external force_x, y_(N)|_±_1|_±_1|_±_5|
|<br>external force_z_(N)|_±_1|_±_1|[_−_5_,_0]|
|force interval (s)|2–4|2–4|<br>2–4|



Table 9: Task-specific domain randomization, on top of the shared actuator randomization described in the text. External forces are reapplied at random intervals within the listed range. `screwdriver` initializes from a set of pre-sampled grasps rather than a randomized free placement. 

### **B.4 Distillation Sweep** 

Each task–hand entry in Table 10 is expanded into the proprioception-only baseline ( `none` ) plus the cross product of taxel resolutions ( `low` , `med` , `high` ), the available placement subsets for that hand, the seven tactile observation types, and both clean and noisy sensor settings. Type-ablation runs pin resolution to `med` and use the clean setting; resolution and noise sweeps vary one axis at a time. 

|Task|Robot|Placement subsets swept|Max student iters|
|---|---|---|---|
|`in`<br>~~`p`~~`alm`<br>`rotate`|`xhand1`|`tips`,`hand`|6000|
|`screwdriver`|`xhand1`|`fingers`|2000|
|`in`<br>~~`h`~~`and`<br>`repose`|`xhand1`|`hand`|6000|
|`in`<br>~~`h`~~`and`<br>`repose`|`sharpa`|`hand`|6000|



Table 10: Task–hand entries in the distillation sweep. 

### **B.5 Tactile Placement and Probe Counts** 

Sensor placement is encoded as a probe asset per (robot, resolution) pair; placement subsets such as `tips` , `fingers` , and `palm` are link filters applied at runtime to the full `hand` probe set. Table 11 shows the resulting probe counts. 

|Robot|Resolution|Hand|Tips|Fingers|Palm|
|---|---|---|---|---|---|
|`xhand1`|`low`|90|45|78|12|
|`xhand1`|`med`|199|100|164|35|
|`xhand1`|`high`|667|224|448|219|
|`sharpa`|`low`|98|45|89|9|
|`sharpa`|`med`|206|70|190|16|
|`sharpa`|`high`|781|245|660|121|



Table 11: Number of active probes per (robot, resolution) and placement subset used in our experiments. `tips` , `fingers` , and `palm` are link-filtered subsets of the full `hand` probe set; `fingers` includes the fingertips. 

### **B.6 Sensor Imperfection Parameters in the “Noisy” Condition** 

Table 12 lists the numerical values used in the noisy condition for each observation type, layered on top of the clean parameters from Table 6. The available knobs and their semantics are defined in Section A.8 (Table 3); knobs not listed here are zero or disabled. 

19 

|Type|_σ_|`rw`|`quant`|_ρ_(m)|rel. thr. (m)|_p_dead|_γ_|(_β, τ_)|
|---|---|---|---|---|---|---|---|---|
|`bool`,`agg`<br>~~`b`~~`ool`|–|–|–|–|2_×_10<sup>_−_4</sup>|0_._05|–|–|
|<br>`depth`,`agg`<br>`force`|2_×_10<sup>_−_4 </sup>m|–|10<sup>_−_4 </sup>m|3_×_10<sup>_−_4</sup>|–|0_._05|[0_._85_,_1_._15]|(0_._5_,_ 0_._05)|
|<br>`force`,`force`<br>`torque`|5_×_10<sup>_−_3 </sup>N|10<sup>_−_4 </sup>N|10<sup>_−_2</sup>|3_×_10<sup>_−_4</sup>|–|0_._05|[0_._85_,_1_._15]|(0_._5_,_ 0_._05)|
|`proximity`|10<sup>_−_2</sup>|10<sup>_−_3</sup>|10<sup>_−_2</sup>|6_×_10<sup>_−_4</sup>|–|0_._05|[0_._85_,_1_._15]|(0_._5_,_ 0_._05)|
|`elastomer`|10<sup>_−_4 </sup>m|10<sup>_−_5 </sup>m|10<sup>_−_4 </sup>m|3_×_10<sup>_−_4</sup>|–|0_._05|[0_._85_,_1_._15]|(0_._5_,_ 0_._05)|



Table 12: Sensor imperfection parameters layered on the clean configuration (Table 6) in the noisy condition. _σ_ is additive white noise, `rw` random-walk drift, `quant` the quantization step, _ρ_ probe-radius noise, “rel. thr.” the Schmitt release threshold, _p_ dead the dead-taxel probability, _γ_ the per-reset gain range, and ( _β, τ_ ) the viscoelastic hysteresis strength and time constant (in seconds). Dashes mark knobs that are disabled for that sensor type. 

## **C Sim-to-Real Deployment** 

The real XHand1 SDK reports both a per-taxel raw pressure field and an aggregate contact pressure _f_ calc ~~p~~ ressure<sup>=(</sup><sup>_f_</sup> _x_<sup>_, f_</sup> _y_<sup>_, f_</sup> _z_<sup>)perfingertip.Thehanddoesthereforeexposeindividualtaxelvalues,</sup> but the exact position and response characteristics of each taxel are not documented, so we cannot register the raw field to our simulated probe layout; the most faithful usable signal is the SDK’s aggregate contact pressure. We simulate this as `agg` ~~`f`~~ `orce` , defined by the contact depths along the normal of the surface and scaled by a constant to match XHand1’s _f_ calc ~~p~~ ressure<sup>inaxisorderand</sup> scale. For `agg` ~~`b`~~ `ool` we threshold the contact-pressure magnitude per finger, 



We deploy the `in` ~~`p`~~ `alm rotate` policy on the real XHand1 and observe 1-2 consecutive rotations before dropping the object. Note that our teacher policy was deliberately not extensively tuned for robustness and that about 2 consecutive successes is precisely what is observed for fingertips-only `agg` ~~`b`~~ `ool` . 

20 

## **D Temperature Object-Discrimination Experiment** 

This section details the `TemperatureGrid` sensor model together with the task and success metric for the temperature experiment of Section 3.3 (Fig. 6). 

### **D.1** `TemperatureGrid` **Sensor Model** 

The `TemperatureGrid` models heat transfer over a voxelized sensor link rather than contact mechanics, returning a temperature field in<sup>_◦_</sup> _C_ . Each sensor link is voxelized into a grid of _nx ×ny ×nz_ cells from its axis-aligned bounding box, with per-axis voxel size ∆= extent _/_ ( _nx, ny, nz_ ). The cell temperatures _T_ are advanced each step by diffusion and an internal source, contact conduction, then radiation and convection, with material properties (conductivity _k_ , density _ρ_ , specific heat _cp_ , emissivity _ε_ , base temperature) assigned per link. We write _ρcp_ for the volumetric heat capacity and _α_ = _k/_ ( _ρcp_ ) for the thermal diffusivity. 

**Diffusion within the grid.** We solve the heat equation _∂T/∂t_ = _α∇_<sup>2</sup> _T_ with a semi-implicit spectral method. To impose Neumann (zero-flux) boundaries, the grid is mirror-padded to twice its size along each axis before a real-input FFT, so the discrete spectrum carries the even extension consistent with _∂T/∂n_ = 0 on the walls. With wavenumber vector **k** and _k_<sup>2</sup> = _∥_ **k** _∥_<sup>2</sup> , each Fourier mode is updated implicitly, 



followed by an inverse FFT and a crop back to the original grid; the zero mode is regularized as _k_<sup>2</sup> _←_ max( _k_<sup>2</sup> _, ϵ_ ). The update is unconditionally stable, so it does not constrain ∆ _t_ as an explicit diffusion stencil would. 

**Internal heat source.** An optional volumetric source field _q_ (in W/m<sup>2</sup> ) is integrated with explicit Euler on the same heat equation, 



where dividing by the cell thickness ∆ _z_ converts the surface flux to a volumetric rate before applying the capacity. 

**Radiation and convection.** Surface voxels, those on any face of the grid, additionally lose heat to the environment at ambient temperature _T_ amb. Radiation follows the Stefan–Boltzmann law for a grey body and convection follows Newton’s law of cooling, 



where _σ_ = 5 _._ 670 _×_ 10<sup>_−_8</sup> W/(m<sup>2</sup> K<sup>4</sup> ), _h_ is the convection coefficient, and _TK_ = _T_ +273 _._ 15 converts to Kelvin for the radiative term. The combined loss is applied as ∆ _T_ = _−_ ∆ _t_ ( _q_ rad + _q_ conv) _/_ ( _ρcp_ ). 

**Contact conduction.** Heat crosses a contact interface by Fourier’s law _q_ = _−k∇T_ . With the sensor and the contacting body acting as two thermal resistances in series, the interface uses the harmonic-mean conductivity 



The conduction length scale is taken as _L_ = _V/A_ , one cell’s volume over the contact area, which is a heuristic stand-in for the unresolved temperature gradient through the interface. For a contacting voxel at temperature _T_ cell opposite a body at _T_ other, the flux, volumetric rate, and temperature change are 



21 

**Contact area estimation.** The contact area _A_ is estimated from the contact-manifold points shared by the two links. We project the points onto their mean contact plane, order them by polar angle about the centroid, and take the polygon area by the shoelace formula. When fewer than three manifold points are available, each contact falls back to a disk of area _π δ_ , where _δ_ is the penetration depth. In the conduction update the area is additionally floored at _π dw δ_ , where _dw_ is a depth-weight scalar (default 1 _._ 0), so that deep point contacts still carry a plausible area. 

**Sensor element lag.** The instantaneous cell field _T_ is the physical temperature; the reported measurement _T_ meas trails it through a first-order RC low-pass filter integrated with forward Euler, 



with sensor time constant _τ_ ; _τ ≤_ 0 disables the lag and reports _T_ directly. This filter is applied only on the measured readout, modeling the finite thermal response of a physical sensing element, while the ground-truth field is left unfiltered. 

### **D.2 Task and Success Metric** 

**Task setup.** The hand rummages a tilted bin (side 0 _._ 5 m) holding 8 geometrically identical balls (diameter 8 cm), one of which is the hot target. The bin, the hand, and the seven distractor balls start at ambient _T_ amb = 22<sup>_◦_</sup> _C_ , while the target ball starts at _T_ tgt = 45<sup>_◦_</sup> _C_ . The policy observes proprioception and one `TemperatureGrid` sensor per finger link; it has no other cue to which ball is hot, so the task is only solvable if temperature differences are resolvable through contact. The hand is reset above the bin and acts at 40 Hz (a control decimation of 5 over the 200 Hz simulation) for episodes of up to 20 s. 

**Temperature progress and heat latch.** For finger sensor _i_ we map its reading to a normalized progress 



where _Ti_ is the maximum cell temperature over that sensor’s voxels. A single sticky _heat latch_ fires the first time the selected-finger progress reaches 1 _− m_ with margin _m_ = 0 _._ 12 (equivalently _Ti ≥_ 42 _._ 2<sup>_◦_</sup> _C_ ), and remains on for the rest of the episode. The latch marks the moment the hand has thermally identified the hot ball. 

**Success metric.** We score a run by the latched hot-ball contact time: the cumulative seconds for which the heat latch is on _and_ at least one fingertip is in contact with the hot ball, 



A configuration counts as a success (a checkmark in Fig. 6) when the trained policy sustains this latched contact, _S >_ 0 across evaluation episodes. A material configuration whose temperature signal is too weak for the latch to fire, or for which the hand cannot stay in contact once it fires, scores _S ≈_ 0 and is marked as a failure. 

22 

## **E Contact and Actuation Audio** 

Beyond the tactile and thermal sensors above, we develop a proof-of-concept audio pipeline in Genesis that synthesizes both the structure-borne sound of contacts and the airborne noise of joint actuation. Procedurally generating sound from simulated physics is well established for interactive games and film, where the goal is perceptual plausibility rather than measurement. We instead propose it as a training signal: a policy that hears its own contacts can infer object properties that the rigid-body solver never resolves. Audio has already been shown to help contact-rich manipulation [5], and this pipeline makes such a signal available directly inside the simulator. 

The motivating observation is one of timescale. The acoustic signature of a material lives in its vibration modes, which for stiff objects sit in the kilohertz range, whereas the rigid-body solver integrates at a few hundred hertz. Resolving those vibrations directly would require shrinking the simulation timestep by orders of magnitude, which is infeasible for RL rollouts. Rather than simulate the vibration, we faithfully approximate it: each physics step emits a short block of audio samples synthesized from the contact state the solver already computes, so the audio carrier sits well above the physics Nyquist frequency while the dynamics step stays cheap. A physics step of duration ∆ _t_ produces _K_ samples at the sub-step rate ∆ _t_ sub = ∆ _t/K_ , for an audio sample rate _fs_ = 1 _/_ ∆ _t_ sub. 

**Contact audio.** We use source–filter modal synthesis: the material is a bank of damped resonators, and the contact is the source that excites it. Each material is a set of modes _{_ ( _fi, di, gi_ ) _}_ of center frequency, amplitude decay rate, and output gain. Mode _i_ is a two-pole resonator advanced over the block _k_ = 1 _, . . . , K_ , 



and the emitted sample is the gain-weighted sum _s_ [ _k_ ] =<sup>�</sup> _i_<sup>_gi yi_[</sup><sup>_k_].The excitation</sup><sup>_ui_is read from</sup> the solver contacts on the sensor link: a sharp rise in the normal contact force injects an impulse that pings the modes into an impact ring-down, while sliding injects a velocity- and force-scaled noise source so a scrape colors the same resonances. 

**Material modes from modal analysis.** The per-material modes are what make different objects sound different, and they follow from the object’s geometry and its isotropic elastic material. We assemble the linear-elasticity stiffness _K_ and a lumped mass _M_ over a tetrahedral mesh and solve the generalized eigenproblem 



keeping the non-rigid modes and reading their frequencies _fi_ = _ωi/_ 2 _π_ . Rayleigh damping _C_ = _αM_ + _βK_ sets each decay rate _di_ = ( _α_ + _β ωi_<sup>2)</sup><sup>_/_2,andthegains</sup><sup>_gi_arethesurfacenor-</sup> mal component of each mode shape _ϕi_ . Because _K_ scales with Young’s modulus and _M_ with density, the modal spectrum is a fingerprint of the material: this is the cue a policy could use to tell a steel box from a wooden one through contact alone, even when the two are dynamically identical to the rigid solver. The eigensolve is a one-time precompute per object, and hand-tuned material presets are also supported. 

**Actuation audio.** The actuation source models motor and joint noise with one emitter per actuated DOF, driven by the controller effort _τ_ and joint speed _ω_ the solver already exposes. Its loudness tracks the mechanical load and power, 



and a velocity-pitched partial bank at fundamental _f_ 0 = _κ |ω|_ gives the characteristic whine, layered with velocity-scaled friction noise and an idle hum, synthesized with the same two-pole primitives. A microphone sensor renders what a listener point hears by summing every source over the scene, each attenuated by distance as 1 _/r_<sup>_p_</sup> and delayed by _r/c_ for propagation, so contact and actuation sound mix into a single airborne signal. 

23 



<!-- Start of picture text -->
Contact Audio by Material<br>Time (s)<br>Frequency (Hz)<br><!-- End of picture text -->

Figure 8: **Example contact audio by materials.** A ball bounces and rolls across a wooden, metallic, and glass box. Although physically identical to the rigid-body solver, the three boxes can be distinguished by their modal spectra. 

**Toward greater realism.** This pipeline is a simplified, real-time model, and several improvements can be made to achieve acoustic realism. Modal synthesis captures the dominant resonances of a struck body, but it omits the frequency- and geometry-dependent radiation efficiency that turns surface vibration into pressure, the room acoustics a real microphone records, and the fine transients of stick–slip friction that our single noise source only coarsely approximates. The actuation source is likewise a parametric approximation of gear-mesh, bearing, and winding noise rather than a measured motor signature. Several extensions could narrow this gap. The dry synthesized signal could be convolved with measured impulse responses of the object and its environment, so it inherits real radiation and reverberation instead of being heard in free field. Per-material and per-motor recordings could replace or augment the procedural banks, either as sample libraries indexed by contact state and joint speed, or as data to fit the modal frequencies, decays, and gains against rather than tuning them by hand. A model trained on paired physics-state and audio recordings could learn this mapping directly. We leave a study of which level of audio fidelity actually benefits policy learning to future work. 

24 

