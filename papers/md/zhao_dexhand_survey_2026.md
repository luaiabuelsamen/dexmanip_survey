JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

1 

# Towards Robotic Dexterous Hand Intelligence: A Survey 

**Weiguang Zhao**<sup>1,2*</sup> , **Tian Liang**<sup>3*</sup> , **Xihao Guo**<sup>3*</sup> , **Rui Zhang**<sup>2</sup><sup>_†_</sup> , **Irwin King**<sup>4</sup> , **Kaizhu Huang**<sup>3</sup><sup>_†_</sup> 1University of Liverpool 2Xi’an Jiaotong-Liverpool University 

> 3Duke Kunshan University 4The Chinese University of Hong Kong 

**_Abstract_ —Robotic dexterous hands are central to contactrich manipulation, with rapid progress driven by advances in hardware, sensing, control, simulation, and data generation. However, existing studies are often developed under different assumptions regarding hand embodiments, sensory configurations, task settings, training data, and evaluation protocols, making systematic comparison difficult and obscuring the developmental trajectory of the field. This survey provides a holistic review of dexterous hand research from four complementary aspects. First, we present a hardware-level analysis covering actuation, transmission, perception, and representative hand designs, highlighting the key trade-offs in force capability, compliance, bandwidth, integration, and system complexity. Furthermore, we review control and learning methods for dexterous manipulation from a methodological perspective, grouping representative works by major paradigms and tracing their evolution in chronological order. In addition, we consolidate datasets, modality design, and evaluation practices, which enables methodological progress to be interpreted together with the ways in which it is trained, benchmarked, and assessed. Finally, we discuss the major limitations of current dexterous hand research and summarize the corresponding future directions. By connecting hardware analysis, methodological development, data resources, and evaluation, this survey aims to provide a structured understanding of dexterous hand research and to clarify the most important open challenges for future study.** 

**_Index Terms_ —Survey, Dexterous Hand, Diffusion Policy, VLA, Reinforcement learning, Imitation learning** 

## I. INTRODUCTION 

A dexterous hand refers to a mechanical hand capable of controllably manipulating an object within the hand by coordinating multi-finger motions and contact force control, without the aid of external supports [1]. Since the late 20th century, when prosthetic-hand designs began incorporating additional degrees of freedom more aligned with natural human hand motion, dexterous hands have entered a stage of rapid development. 

In recent years, learning-based control methods, scalable data generation pipelines, the widespread adoption of simulation platforms, and improvements in highly compliant hardware have been proposed to achieve stable performance, enabling high-degree-of-freedom in-hand manipulation for the first time. The rapid advancement of dexterous hands further stimulates the publication of comprehensive and insightful review studies. 

* Equal Contribution 

Existing reviews examine dexterous hands from several complementary perspectives. Hardware-oriented surveys analyze hand structures, actuation, transmission, and design tradeoffs, comparing rigid, tendon-driven, underactuated, and soft hands in terms of anthropomorphism, force capability, and system complexity [2], [3], [4]. Sensing-oriented surveys establish taxonomies of tactile and multimodal perception for inhand manipulation, emphasizing perception–action coupling and multifunctional tactile sensing [5], [6], [7], [8]. With the rapid growth of learning-based dexterous manipulation, many surveys further focus on reinforcement learning, imitation learning, and interactive learning paradigms, but they often abstract away the hardware and sensing assumptions under which these methods operate [9], [10], [11], [12]. More holistic surveys adopt broader views across hardware, sensing, and control, while scenario-driven reviews derive design requirements for specific applications such as industrial settings or fragile object handling [13], [14], [15], [16]. Nevertheless, most prior reviews still emphasize selected layers or subsystems, with limited effort to jointly connect hardware analysis, methodological evolution, datasets and evaluation, and a dedicated discussion of the field’s overarching limitations and future directions. 

To this end, this survey revisits dexterous hand research from a holistic perspective. Rather than centering the discussion on any single technical trend, we organize the field around four complementary aspects: a hardware-level analysis of dexterous hands, a methodological review of control and learning approaches, a consolidated discussion of datasets and evaluation practices, and a dedicated examination of major limitations together with future directions. This organization enables us to compare representative works under clearer assumptions and to position different research lines within a common analytical framework. To support this review, our literature collection was primarily conducted through the EI and Web of Science databases. We retrieved articles mentioning relevant concepts in fields such as title, abstract, and subject/topic, and then further screened and organized representative works from this large initial corpus for the subsequent survey and analysis. 

Specifically, we first provide a systematic hardware-level analysis of dexterous hands, covering actuation, transmission, perception, and representative hand designs, and highlighting the key trade-offs that shape their development in terms of force capability, compliance, bandwidth, integration, and overall system complexity. Furthermore, we review control 

_†_ Corresponding authors 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

2 

and learning methods for dexterous manipulation from a methodological perspective, grouping representative works by major paradigms and tracing the developmental trajectory of the field in chronological order, thereby clarifying how different research directions emerged and evolved over time. To complement this analysis, we further consolidate datasets, modality design, and evaluation practices, so that methodological progress can be interpreted together with the ways in which it is trained, benchmarked, and assessed. Finally, we devote a dedicated discussion to the major limitations of current dexterous hand research and summarize the corresponding future directions of the field, with the aim of clarifying the central open challenges and identifying promising avenues for future study. The contributions of this survey are as follows: 

- 1) We review dexterous hand research from a holistic perspective, organizing the field around the interplay among hardware, research methods, datasets, and evaluation. 

- 2) We provide a systematic hardware-level analysis of dexterous hands, covering actuation, transmission, perception, and representative hand designs, and summarize the key trade-offs in force capability, compliance, bandwidth, integration, and system complexity. 

- 3) We systematically review control and learning methods for dexterous manipulation from a methodological perspective, grouping representative works by major method paradigms and tracing the developmental trajectory of the field in chronological order. We further consolidate datasets, modality design, and evaluation practices to provide a more complete view of how dexterous manipulation research is developed and assessed. 

- 4) We provide a dedicated discussion of the major limitations of current dexterous hand research and summarize the corresponding future directions of the field. 

The remainder of this survey is organized as follows. Section II presents the anatomy, focusing on degrees of freedom, actuation, transmission, and sensing. Section III reviews control and learning frameworks for dexterous grasping and in-hand manipulation, together with training and transfer strategies. Section IV summarizes commonly used datasets and evaluation protocols, and discusses what robustness is measured under different settings. Finally, Section V highlights key bottlenecks and outlines future directions toward robust dexterous hands and robust real-world deployment. 

## II. ANATOMY OF THE DEXTEROUS HAND 

This section provides a system-level anatomy of dexterous hands, focusing on how actuation, transmission, perception, and representative hand designs are organized and coupled in practical systems. We first summarize representative actuation principles in Section II-A, then review common transmission architectures that map actuator outputs to multi-DoF finger motions in Section II-B, followed by perception systems for dexterous feedback in Section II-C, and finally provide a comparative summary of existing dexterous hands in Section II-D. 

## _A. Actuation System of Dexterous Hands_ 

An actuation system is the system that converts energy into mechanical motion [17]. Different actuation principles 

vary fundamentally in their energy sources, force generation mechanisms, achievable power density, dynamic response, and inherent compliance. Consequently, no single actuation solution is universally optimal for all dexterous manipulation tasks. From the perspectives of energy input and physical actuation mechanisms, the actuation systems of dexterous hands can be systematically categorized into four major classes: electromagnetic, fluidic, smart-material, and hybrid actuation. 

**Electromagnetic Actuation (EA).** In electromagnetic actuation for dexterous hands, miniature motors constitute the primary power sources. Coreless DC permanent-magnet motors are widely used due to their high power density, low rotational inertia, and fast dynamic response, enabling precise and rapid finger motion. Frameless torque motors, which eliminate shafts, housings, and bearings, allow direct structural integration into joints, reducing system volume and mass while improving torque transmission efficiency [18], [19]. Ultrasonic motors, operating based on the inverse piezoelectric effect, offer advantages such as compact structure, high positioning resolution, and immunity to electromagnetic interference, making them suitable for space-constrained dexterous hands [20], [21]. In addition, brushless direct current (BLDC) motors have been adopted in recent large-scale humanoid platforms, such as the Tesla Optimus hand, due to their high efficiency, reliability, and compatibility with high-precision transmission mechanisms. 

**Fluidic Actuation (FA).** Fluidic actuation converts pressurized fluids or gases into mechanical motion and mainly includes hydraulic and pneumatic actuation. Hydraulic actuation relies on pump-powered fluid supply and valve-based flow control to generate motion at the end effector, offering high power density and large output force [22]. To improve compliance, soft hydraulic actuation integrates soft structures with hydraulics, achieving a balance between high force output and flexibility [23]. 

Pneumatic actuation, typically realized as pneumatic artificial muscles (PAMs), produces contraction or bending by regulating internal air pressure. Positive-pressure designs include McKibben, fiber-reinforced, and PneuNet actuators [24], [25], [26], while negative-pressure vacuum PAMs (VPAMs) exploit buckling, jamming, or origami-like structures for actuation [27], [28], [29]. Valves and fluidic circuits serve as essential energy modulation components in fluidic actuation systems, enabling precise, compliant control. 

**Smart-Material Actuation (SMA).** Smart-material actuation exploits controllable material responses under external stimuli to directly generate mechanical output, enabling highly integrated and compact actuation solutions for dexterous hands. Representative examples include shape memory alloys (SMAs), which produce actuation through thermally or electrically induced phase transformations and offer lightweight, compliant, and structurally simple designs, albeit with limitations in response speed and fatigue life [30]. Electroactive polymers (EAPs) constitute another important class of smart actuators. Among them, dielectric elastomer actuators (DEAs) generate large deformations and high energy density via Maxwell stress, making them well suited for biomimetic muscle-like actuation [31], [32], while ionic polymer–metal 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

3 



<!-- Start of picture text -->
Fuses vision, touch, and proprioception across time 1. Tendon-<br>From single-modal sensing to tightly scales to achieve robust, context-aware manipulation. driven 2.Linkage-<br>integrated multimodal perception for based<br>robust manipulation in unstructured 3. Multimodal  1) Compact,<br>environments. Vision Perception lightweight, synergy-friendly 1) High stiffness and precision<br>1. Proprioception 2) Friction and  2) Low compliance<br>2. Tactile Sensing maintenance sensitive and adaptability<br>Enables contact-rich perception 4. Screw-<br>of force, texture, and interaction 3. Gear-based based<br>dynamics for stable and adaptive<br>grasping. 1) Precise, stiff, high-torque 1) High stiffness and precision<br>2) Low compliance,  2) Limited by friction<br>1. Electromagnetic  Offers high precision, fast response, poor scalability losses and axial<br>and mature control, but trades off compactness, length constraints<br>compliance, and power density in highly integrated<br>dexterous hands.<br>2. Fluidic Provides high force output and intrinsic compliance, 5. Belt &  6. Integrated<br>yet suffers from bulky peripheral hardware, slower dynamics, Pulley & Direct<br>and complex system integration.<br>3. Smart-Material  Enables lightweight, compact, and biomimetic 1) Simple and low-cost with  1) Highly compact and<br>flexible routing mechanically simple<br>actuation with high integration, but remains constrained by response<br>speed, durability, and controllability. 2) Limited stiffness  2) Limited in output<br>and accuracy  force, scalability<br>4. Hybrid Combines complementary actuation principles to balance force, precision,<br>compliance, and integration, representing a practical system-level optimization strategy.<br><!-- End of picture text -->

Fig. 1. System-Level Architecture of Dexterous Hands: Actuation, Transmission, and Multimodal Perception 

composites (IPMCs) rely on ion migration to achieve lowvoltage, highly compliant actuation. More recently, magnetoand photothermally tunable soft magnetic muscles, formed by combining shape memory polymers with magnetic particles, have enabled the integration of actuation and variable stiffness within a single structure [33]. In addition, piezoelectricceramic-based robotic hands employing direct joint actuation eliminate the need for complex transmission mechanisms and provide high resolution and fast response, offering a promising pathway for precision dexterous manipulation [34]. 

**Hybrid Actuation (HA).** Hybrid actuation refers to systems that intentionally combine multiple actuation principles, or integrate actuation with specific transmission mechanisms, in order to leverage complementary advantages that cannot be achieved by a single actuation modality alone. Typical examples include servo-motor direct actuation coupled with tendon transmission, which combines high control bandwidth with flexible force routing [35], and SMA-based actuation integrated with tendons, enabling lightweight and compliant designs while extending actuation range and force delivery [36]. Pneumatic–tendon hybrid architectures, such as pneumatic tendon-coupled actuators (PTCA) and discrete pneumatic tendon-coupled actuators (DPTCAs), merge the compliance and variable stiffness of pneumatic actuation with the precision of tendon transmission [37]. Large-scale humanoid platforms further demonstrate hybrid paradigms, exemplified by the “planetary gearbox + lead screw + tendon” architecture adopted in the Tesla Optimus hand, which balances high force output, precision, and structural compactness. Overall, hybrid actuation systems embody a pragmatic, task-oriented design philosophy that addresses the inherent trade-offs among force, speed, precision, compliance, and integration in dexterous robotic hands. 

_B. Transmission System of Dexterous Hands_ 

Transmission mechanisms define how actuator forces are distributed among joints and contact [38]. While it does not generate energy, the transmission system plays a critical role in determining force efficiency, motion accuracy, compliance, and overall manipulation performance. Transmission mechanisms in dexterous hands can be broadly categorized into tendon-driven, linkage-based, gear-based, screw-based, belt–pulley, and integrated transmission architectures, each offering distinct trade-offs between force capacity, precision, compliance, structural complexity, and suitability for underactuated designs [39]. 

**Tendon-Driven Transmission (TDT).** Tendon-driven transmission is a widely adopted approach in dexterous hands, in which flexible tendons are used to transmit force or displacement generated by actuation to the joints, mimicking the muscle–tendon architecture of the human hand [40]. Typical implementations combine tendons with pulleys, Bowden cable sheaths, and elastic elements such as springs or rubber components, enabling remote placement of actuators and facilitating underactuated designs. This transmission strategy offers high structural compactness, low mass, and strong suitability for high-degree-of-freedom finger layouts, while naturally supporting motion coupling and synergy. Consequently, tendondriven mechanisms have been extensively employed in representative systems such as the Shadow Dexterous Hand [41], the Robonaut hand [42], and the DLR David hand [43]. However, their performance is often limited by challenges in tendon tension regulation, friction-induced hysteresis, backlash, and wear, which can degrade control accuracy and response speed and constrain achievable grasping forces. Systematic analyses of tendon-driven and underactuated robotic hands can be found in [39], [38], while the relationship between the minimum number of tendons and the controllability of multi-DoF hands 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

4 

has been further investigated in [44]. 

**Linkage-Based Transmission (LBT).** Linkage-based transmission employs rigid links and revolute joints to directly map actuation outputs into joint motions, thereby establishing deterministic kinematic relationships. Typical implementations include four-bar mechanisms, serial–parallel multi-link configurations, and hybrid screw–linkage structures. Owing to their short force transmission paths and rigid mechanical connections, linkage-based mechanisms can deliver large output forces with high motion repeatability and positioning accuracy, making them well-suited for applications requiring high stiffness and high load capacity. Representative examples include the Schunk SVH five-finger hand [45], [46] and the ILDA hand, which achieves multi-DoF finger motion through a sophisticated combination of serial and parallel linkage chains [47]. However, the inherent rigidity of linkagebased transmission limits compliance and adaptability, while constrained workspaces and complex kinematic designs further limit scalability in high-DoF dexterous hands. Extensive studies have investigated the grasp stability and kinetostatic relationships of linkage-driven hands [48], [49], as well as underactuated linkage designs that enhance adaptability while reducing actuation complexity [50]. 

**Gear-Based Transmission (GT).** Gear-based transmission utilizes gear mechanisms to achieve torque amplification, motion direction change, and coordinated actuation across multiple degrees of freedom. Common implementations include harmonic drives, planetary gear trains, and bevel-gear differential structures. Owing to their high transmission ratios and mechanical rigidity, gear-based transmissions provide accurate positioning and stable torque output, making them suitable for precision manipulation and coordinated joint control. For example, bevel-gear differential mechanisms have been employed to realize multi-DoF metacarpophalangeal (MCP) joint control with enhanced robustness and flexibility [51]. Earlier dexterous hand designs also extensively adopted gear- and roller-based transmission architectures [52], [53]. However, gear transmissions typically introduce additional mass and volume, which can limit scalability in compact dexterous hands. Moreover, certain high-ratio reducers, such as harmonic drives, are sensitive to impact loads and may suffer from reduced durability under repetitive or high-force manipulation tasks. 

**Lead and Roller-Screw Transmission (LRST).** Leadscrew and roller-screw transmissions convert rotary motion into precise linear displacement and are commonly employed to drive joints or tension tendons in dexterous hands. Owing to their high stiffness and fine positional resolution, screwbased transmissions enable accurate force and motion control and are well suited for closed-loop actuation architectures. Planetary roller screws, in particular, offer improved load capacity and transmission efficiency compared with conventional lead screws, making them attractive for compact, highforce applications. A representative example is the Tesla Optimus hand, which integrates brushless DC motors, planetary roller screws, and tendon-driven mechanisms to achieve highprecision, high-stiffness joint actuation. Screw-based transmission is also adopted in the ILDA hand, where a motor–lead- 

screw–linkage architecture is used to realize coordinated multijoint finger motion [47]. Despite these advantages, screw transmissions suffer from friction-induced efficiency losses and impose constraints on structural length, which may limit their applicability in highly compact or anthropomorphic hand designs. 

**Belt Cable and Pulley Transmission (BCPT).** Belt-, cable, and pulley-based transmissions utilize flexible belts or ropes routed over pulleys to transmit motion and force from actuators to finger joints. Owing to their simple mechanical structure and low manufacturing cost, such transmission mechanisms were widely adopted in early multi-fingered robotic hands and in designs emphasizing structural simplicity [54], [55]. These systems enable flexible routing and decoupling between actuators and joints; however, their relatively low stiffness makes them susceptible to elastic deformation, slip, and backlash, which limits positioning accuracy and force transmission fidelity. As a result, belt- and pulley-based transmissions are less favored in modern dexterous hands that require high precision, high bandwidth, and stable force control, but they remain relevant in low-cost or lightweight implementations. 

**Direct or Integrated Transmission (DIT).** Direct or integrated transmission architectures eliminate or significantly reduce independent transmission mechanisms by tightly integrating transmission functions within the actuation structure itself. In such designs, the deformation of soft chambers or intelligent materials directly generates joint motion, effectively merging actuation and transmission into a single functional unit. Typical examples include soft pneumatic or hydraulic hands, in which the fluidic chambers simultaneously serve as both actuators and transmission pathways [23], as well as piezoelectric ceramic–driven robotic hands where joints are directly actuated without any intermediate transmission elements [34]. These integrated approaches enable compact structures, reduced mechanical complexity, and improved compliance, but often face limitations in output force, scalability, and precise motion control. 

## _C. Perception System_ 

The perception system of a dexterous hand is the system that collects data from onboard sensors. Related algorithms then process this information to perceive both the hand itself and its external environment. It determines the adaptability and intelligence of the dexterous hand in unstructured environments. The perception system has evolved from singlesensor to multiple-sensor use, and then to a “proprioception–tactile–vision” tri-cooperative fusion. It is now rapidly advancing toward multimodal fusion, with technological trends characterized by high precision, miniaturization, multimodality, anti-interference, and low cost. 

**Proprioception.** Proprioception in dexterous hands refers to the capability of sensing the internal state of the hand itself, including joint position, motion, force/torque, and tendon tension, thereby providing essential feedback for closedloop control, motion accuracy, and protective behaviors [56]. Compared with external proprioceptive approaches based on vision [57] or motion capture systems [58], embedded proprioceptive sensing offers higher precision, lower latency, 

5 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

TABLE I 

ANATOMY OF EXISTING DEXTEROUS HANDS 

|**Hand**|**Year **|**Actuation **|**Transmission **|**Tactile **|**Fingers**|**DoF **|**Voltage **|**Current **|**Capacity **|**Weight **|**Communication**|**Developer**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|SKKU Hand II|2006|EA|GT|✓|5|10|24V|1.5A|5kg|0.9kg|CAN|SKKU|
|DLR-HIT HAND II|2008|EA|BCPT|✓<br>|5<br>|15<br>|28V|3A<br>|7kg<br>|1.5kg<br>|PPSeCo, CAN|DLR & HIT|
|MPL|2010|EA|GT|✓|5|26|24V|6A|15.9kg|4.8kg|CAN|JHU|
|DEXHAND|2012|EA|LBT|✓|4|12|28V|3A|8kg|4.0kg|EtherCAT, CAN|DLR|
|Self-contained Soft Hand|2016|FA|DIT|✓|3|3|–|–|–|–|USB|Harvard|
|Agile Hand|2018|HA|GT|✗|5|16|24V|2A|5kg|1.5kg|Proprietary|Agile Robot|
|ShadowHand LITE|2018|EA|TDT|✓|4|13|24V|2.5A|4kg|2.4kg|EtherCAT|Shadow Robot|
|ShadowHand Ertra LITE|2018|EA|TDT|✓|3|10|24V|2.5A|4kg|2.1kg|EtherCAT|Shadow Robot|
|ShadowHand Super LITE|2018|EA|TDT|✓|2|7|24V|2.5A|4kg|1.8kg|EtherCAT, ROS|Shadow Robot|
|HRI Hand|2020|EA|TBT|✗|5|15|12V|–|–|0.6kg|Bluetooth|KHU|
|RH56DFX|2020|EA|TDT|✗|5|6|24V|3A|5kg|0.5kg|CAN|Inspire Robot|
|Frontiers SMA Hand|2020|SMA|DIT|✗|5|14|–|1.8A|4.5kg|0.3kg|Real-time FPGA|Saarland Univ.|
|ILDA Hand|2021|EA|LBT|✓|5|15|12V|0.1A|9.2kg|1.1kg|CAN|Ajou Univ.|
|Shadow Hand|2021|EA|LBT|✓|5|24|48V|2.5A|5kg|4.3kg|EtherCAT|Shadow Robot|
|UTD SMA Hand|2021|SMA|DIT|✓|5|15|6.6V|0.7A|0.1kg|0.2kg|PWM|UT Dallas|
|LEAP Hand II|2023|EA|TDT|✗|5|21|–|0.6A|2.2kg|1.0kg|ROS|CMU|
|ARTUS Lite|2023|EA|LBT|✗|5|20|24V|2.5A|20kg|1.4kg|CAN|Sarcomere Dynamics|
|DG-5F|2024|EA|DIT|✗|5|20|24V|10A|20kg|1.8kg|EtherNet, Modbus|Tesollo|
|Unitree Dex3-1|2024|HA|GT|✓|3|7|58V|10A|0.5kg|0.7kg|USB|Unitree|
|F-TAC Hand|2024|HA|BCPT|✓|5|15|–|–|2.2kg|–|CAN|BIGAI|
|GR-2|2024|EA|LRST|✓|5|12|–|–|3kg|–|EtherCAT|Fourier|
|Skilhand|2024|EA|BCPT|✗|5|19|24V|3.5A|3kg|0.5kg|EtherCAT|AgiBot|
|XHAND1|2024|EA|GT|✓|5|12|72V|2.5A|25kg|1.1kg|USB|Robot Era|
|DexCo Hand|2024|FA|DIT|✓|3|4|–|–|–|–|ROS|UCB|
|DG-4F|2025|EA|GT|✗|4|18|24V|10A|10kg|1.4kg|EtherNet, Modbus|Tesollo|
|DG-3F-M|2025|EA|GT|✗|3|12|24V|10A|5kg|1.1kg|EtherNet, Modbus|Tesollo|
|Unitree Dex5-1P|2025|EA|DIT|✗|5|20|60V|3A|4.5kg|1.0kg|USB|Unitree|
|Optimus Gen 3|2026|HA|LRST|✓|5|22|52V|–|8kg|–|EtherNet|Tesla|
|EFORT Dexterous I|2026|EA|GT|✗|5|15|24V|5A|10kg|–|EtherNet,ROS|EFORT|



and stronger robustness against occlusion and environmental disturbances [59], [60], and thus constitutes a fundamental component of dexterous hand perception systems. 

From a functional perspective, embedded proprioception in dexterous hands can be categorized into four types. Joint pose sensing, which measures joint angles and configurations to support accurate kinematic modeling and position control, is commonly implemented using rotary encoders, potentiometers, Hall-effect sensors, or optical encoders [61]. Furthermore, motion-state sensing focuses on capturing dynamic information such as velocity and acceleration. Inertial Measurement Units (IMUs) are widely used for this purpose, enabling realtime estimation of hand motion and dynamic states, often in combination with encoder-based velocity sensing [62]. 

In addition, joint force and torque sensing provides direct feedback on interaction forces and internal loads, which is critical for compliant manipulation and safety; such sensing is often realized using strain-gauge-based torque sensors or multi-axis force/torque sensors [63]. Moreover, tendon tension sensing, which is particularly important for tendon-driven and underactuated dexterous hands, enables indirect estimation of joint torques and contact forces by monitoring tendon forces in real time [64]. Fiber-optic sensing technologies, such as Fiber Bragg Grating (FBG) sensors, have been increasingly adopted due to their high precision and strong immunity to electromagnetic interference. 

Together, these proprioceptive sensing modalities provide complementary internal feedback that supports precise motion control, stable force regulation, and robust interaction with uncertain environments. By forming a reliable internal feedback loop, proprioception serves as the foundation for dexterous manipulation performance and plays a crucial role in enabling adaptive, safe, and intelligent hand behaviors. **Tactile Sensing.** Human skin contains approximately 

17,000 mechanoreceptors, enabling rich tactile perception of contact forces, texture, temperature, and spatial distribution. Inspired by this biological capability, the tactile perception system in dexterous hands provides detailed sensing of object–hand interactions, playing a critical role in stable grasping, manipulation, and fine force regulation [65], [66]. Modern robotic tactile sensing technologies can be broadly classified into resistive, capacitive, piezoelectric, triboelectric, optoelectronic, fluidic, and vision-based approaches, each exhibiting distinct trade-offs in sensitivity, bandwidth, spatial resolution, robustness, and integration complexity. As systematically reviewed in [67], no single tactile sensing modality can simultaneously optimize all performance metrics, motivating the continued development of multimodal tactile sensors and application-specific designs for dexterous manipulation tasks. 

**Multimodal Vision Perception.** Multimodal perception fusion is a fundamental enabler for dexterous hands to approach human-level manipulation intelligence, driving the evolution from single-modal sensing toward tightly integrated perception of proprioception, touch, and vision. By jointly exploiting complementary sensory modalities, multimodal perception provides more comprehensive and accurate awareness of both the hand’s internal state and external environment, thereby supporting precise, robust manipulation in unstructured scenarios. 

At the sensor level, multimodal sensors represent an important trend, offering higher integration density and faster response by simultaneously measuring multiple physical quantities. Recent advances in materials and fabrication have enabled sensors capable of jointly sensing strain, curvature, contact force, temperature, texture, or proximity, such as stretchable optical waveguide sensors [68], multifunctional flexible tactile sensors [69], textile-based soft sensors [70], and fabric-based multimodal capacitive sensors [71]. These designs reduce sensing redundancy while enhancing spatial 

6 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

and temporal coherence across modalities. 

At the algorithmic level, multimodal fusion can be performed at the data, feature, and decision levels, or through hybrid strategies combining all three. Representative systems integrate tactile and proprioceptive sensing to emulate human mechanoreceptors and enable fine texture recognition [72], or fuse vision, touch, and joint sensing to achieve reliable multimodal perception despite heterogeneous sensing latencies, as demonstrated by the RAPID Hand [51]. Hybrid fusion strategies further balance control performance and computational cost by hierarchically combining low-level motion–force features with higher-level visual object representations. 

Beyond perception alone, multimodal sensing is increasingly co-designed with actuation and control to form closedloop perception–decision–control architectures. Examples include indirect sensing of tendon length and tension via encoders or vision [73], [74], vision-centric multimodal hands that minimize onboard sensors while retaining rich perception [75], and monolithic soft electronic skins that integrate multimodal sensing with neuromorphic signal processing and closed-loop actuation [76]. Together, these developments highlight a clear trend toward tightly coupled, multimodal perception systems that enhance dexterity, adaptability, and systemlevel efficiency in next-generation robotic hands. 

## _D. Anatomy of Existing Dexterous Hands_ 

Table I summarizes representative dexterous hand platforms and provides a compact anatomy across key hardware and system attributes, including the release year, actuation and transmission choices, developer, communication interface, finger count, DoF, electrical envelope, and basic capability indicators such as fingertip force, payload capacity, and weight. In this table, the actuation abbreviations follow the taxonomy in Sec. IIA, where electromagnetic actuation is denoted as EA and is discussed as a mainstream solution due to its mature control and fast response. Similarly, the transmission abbreviations follow Sec. II-B, where tendon-driven, linkage-based, gearbased, and integrated transmission represent different tradeoffs among force efficiency, motion accuracy, compliance, and integration complexity. 

Moreover, Table I highlights that dexterous hands span a wide range of design envelopes rather than converging on a single best architecture. This variation directly shapes what is feasible in closed-loop manipulation, because actuation and transmission determine the achievable torque and bandwidth, while the communication interface and electrical constraints influence controller update rate, sensing integration, and system latency. In addition, the large spread in fingertip force, payload capacity, and weight provides an intuitive reference for discussing robustness-oriented design. 

## III. RESEARCH ON DEXTEROUS HAND 

Dexterous hand manipulation comprises heterogeneous tasks with diverse contact dynamics, force requirements, and perceptual demands, making universal training paradigms impractical. Consequently, task-oriented analysis is necessary to clarify how different training paradigms support dexterous 



<!-- Start of picture text -->
First stage: Task Planning<br>Long-horizon reasoning and symbolic planning<br>(Low frequency)<br>Planning<br>Input<br>Task & Scene<br>High Level Goals & Plans<br>Planning  Strategy Signal Data<br>Strategy<br>Second stage: Policy Training<br>Policy learning, adaptation, and sim-to-real transfer Real System<br>Domain Randomization<br>Learning<br>Simulation<br>Strategy Signal Data<br>Data<br>Third stage: Deployment<br>Fast feedback control and reflexive behaviors<br>(High frequency) Policy Learning Model<br>Vision<br>Execution<br>Tactile Control  Control<br>Proprioception Signal<br>Perception Actuation<br><!-- End of picture text -->

Fig. 2. Research Workflow on Dexterous Hand 

manipulation across varying task regimes. In this section, we first summarize a general open-ended workflow shared by dexterous-hand tasks in Section III-A, and then examine the current progress of dexterous-hand research from the perspective of specific task categories, as shown in Fig. 3, including In-Hand Manipulation (Section III-B), Grasping & Pick-andPlace (Section III-C), Human Interaction (Section III-E), Tool & Device Operation (Section III-D), and Bimanual Manipulation (Section III-F). 

## _A. Research Workflow_ 

Dexterous hand control aims to reproduce the fine manipulation skills of the human hand, enabling stable grasping, precise motion control, and safe interaction with objects. The central challenge is to translate the high degrees of freedom, compliant contacts, and rich multi-modal perception of the human hand into robotic control strategies that satisfy real-time constraints, stability, and safety requirements. With recent advances in bionics, material science, and artificial intelligence, dexterous hand systems have gradually evolved from monolithic controllers to hierarchical and learning-augmented frameworks. In this section, we summarize a three-stage closed-loop research workflow for dexterous hand control and introduce its key mechanisms and algorithmic components. 

Dexterous hand control systems are commonly formulated as closed-loop pipelines that integrate perception, planning, execution, and evaluation. To cope with the high dimensionality, hybrid contact dynamics, and task diversity of dexterous manipulation, hierarchical structures are widely adopted, as they improve data efficiency, modularity, and generalization across tasks [77]. Existing designs often decompose control according to abstraction level and temporal scale. At the 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

7 



<!-- Start of picture text -->
Research on Dexterous Hand<br>1) In-Hand Manipulation 2) Grasping & Pick-and-Place 3) Tool & Device Operation 4) Human Interaction 5) Bimanual Manipulation<br>Reinforcement Learning Reinforcement Learning Reinforcement Learning Reinforcement Learning Reinforcement Learning<br>Diffusion Policy Diffusion Policy Imitation Learning Diffusion Policy<br>Imitation Learning<br>Imitation Learning Imitation Learning VLA Imitation Learning<br>Model-Based Control Representation Learning Other Representation Learning<br>VLA VLA VLA<br>Other Other Other<br><!-- End of picture text -->

Fig. 3. Research on Dexterous Hand 

system level, high-level task planning is decoupled from low-level execution, so task generalization can be separated from policy realization [78]. In learning-augmented systems, high-level planners may further leverage large language models to decompose complex manipulation goals into ordered sub-goals, while low-level controllers map these sub-goals into executable motor commands under current states and constraints [79]. Representative hierarchical systems include the DLR-HIT Hand architecture, which integrates low-level control, distributed FPGA-based data processing, high-level control, and external command interfaces [80], and three-layer designs that separate task planning, event-level coordination, and low-level trajectory and force control [81]. 

As learning-based control and foundation-model-driven methods become increasingly prevalent, overall system performance depends not only on the control hierarchy itself but also on the research workflow that connects planning, training, and deployment. A widely adopted paradigm can be summarized as a three-stage closed loop, as illustrated in Fig. 2. In the first stage (task planning), problem discovery and task specification are conducted, including requirement definition, failure analysis, and the formulation of objectives, constraints, and evaluation criteria. In the second stage (policy training), manipulation policies are trained and validated using simulation and collected data, while transfer robustness is improved through domain randomization, calibration, and simto-real adaptation. In the third stage (deployment), the learned policy is executed on a real dexterous hand with real-time perception and safety monitoring, and execution logs and failure cases are collected as feedback to refine both the training data and planning, forming an iterative closed loop. 

## _B. In-Hand Manipulation_ 

In-hand manipulation constitutes the core capability of dexterous hands and serves as the fundamental building block for more complex manipulation tasks. Precise force–motion coupling, severe visual occlusion, and irreversible failure modes make explicit modeling and open-loop planning particularly challenging. Fig. 4 shows the research timeline for in-hand manipulation. 

**Reinforcement Learning.** In-hand manipulation involves persistent contact, frequent contact switching, and partial observability, where tightly coupled force–motion dynamics and visual occlusion render explicit modeling and trajectory optimization difficult. Reinforcement learning addresses these challenges by learning closed-loop manipulation strategies directly from interaction, enabling stable in-hand translation, rotation, and reorientation without accurate contact models. 

Existing work primarily focuses on improving training efficiency and robustness under high-dimensional contact dynamics. Data-efficient RL methods accelerate convergence [82], while improved sampling strategies address exploration bottlenecks in in-hand motion planning [83]. Reset-free learning further enables continuous in-hand manipulation training without manual intervention after failure [84]. Vision-based RL extends these approaches by decomposing manipulation into guided substeps learned directly from visual observations [85]. Point-cloud-based observations improve geometryaware generalization [86], while post-simulation fine-tuning enables targeted adaptation to real contact conditions [87]. 

As in-hand manipulation increasingly involves multimodal feedback and coordination, RL frameworks integrate kinematic priors [88] and tactile sensing [89] to stabilize manipulation under partial observability. Extensions to bimanual in-hand manipulation [90] and human–robot handover scenarios [91] further demonstrate the scalability of RL in contact-rich, interactive manipulation. 

**Diffusion Policy.** In-hand manipulation demands coordinated multi-finger motion, smooth force–motion transitions, and robustness under contact uncertainty. Diffusion policies naturally fit this setting by generating continuous action trajectories, avoiding abrupt control signals, and enabling diverse, multimodal manipulation behaviors. Recent work explores different ways of integrating diffusion policies into dexterous manipulation. SteeringDP combines diffusion policies with reinforcement learning by optimizing a low-dimensional latent policy whose outputs are decoded into high-dimensional actions, preserving smooth multimodal behaviors while improving task performance [92]. Several methods adapt diffusion policies to contact and force-sensitive in-hand settings. TacDif- 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

8 



<!-- Start of picture text -->
Data-Efficient  Learning  Robotic<br>RL Synergies Telekinesis Sampling-Based Bi-DexHands MyoDex<br>(Popov et al) ( Deng et al ) ( Sivakumar et al ) ( Khandate et al ) ( Qin et al ) ( Caggiano et al )<br>Learning with  Deep Visuomotor  Solving<br>Tactile  Policies Challenge ILAD Tactile in Hand MimicTouch<br>( Hoof et al ) ( Jain et al ) ( Charlesworth et al ) ( Wu et al ) ( Andrychowicz et al ) ( Yin et al )<br>2015 2016 2017 2018 2019 2020 2021 2022 2023<br>Data- Learning In-Hand TrajectoTree Manipulation  KODex DeFT<br>Efficient RL ( Andrychowicz et al ) ( Chen et al ) from Image ( Yin et al ) ( Kannan et al )<br>(Popov et al) ( Xu et al )<br>Reset-Free DIME Rotating   DexPoint Estimator-<br>( Gupta et al ) ( Arunachalam et al ) ( Yin et al ) ( Qin et al ) Coupled<br>( Rostel et al )<br>Consistency  Contact<br>Octo Policy Implicit RxR DextrAH-G RoboDexVLM ViviDex DexVLA OmniVLA DyDexHandOver<br>( Octo team et al ) ( Prasad et al ) ( Jiang et al ) ( Khandate et al ) (Lum et al) ( Liu et al ) ( Chen et al ) ( Wen et al ) ( Cheng et al ) ( Wan et al )<br>Bridging RGMC<br>MyoDex 3D VLA Robust Gap DexForce Villa-X Champion DexHandDiff ManiDext<br>( Caggiano et al ) ( Zhen et al ) ( Luo et al ) ( Guzey et al ) ( Chen et al ) ( Chen et al ) ( Yu et al ) ( Liang et al ) ( Zhang et al )<br>2024 2025<br>OpenVLA 3D Diffuser  PAD Generative Time- Steering  MimicTouch FBI DexReMoE<br>( Kim et al ) Actor ( Guo et al ) Factor Optional DP (Yu et al) ( Chen et al ) ( Wan et al )<br>Smooth  ( Ke et al ) 3D Diffusion ( Mishra et al )Shape- ( Pitz et al ) ( Wagenmaker et al TacDiffusion) HUDOR   ReDMan Being-H0<br>Computation Policy Conditioned ( Wu et al ) ( Guzey et al ) ( Chen et al ) ( Zhang et al )<br>( Luo et al ) ( Ze et al ) (Pitz et al)<br>Reinforcement  Model-Based  Imitation<br>Learning VLA Control Diffusion Policy Learning Others<br><!-- End of picture text -->

Fig. 4. In-Hand Manipulation Timeline 

fusion generates actions directly in the 6D force–torque space, enabling precise tactile manipulation under geometric and frictional uncertainty [93]. DexHandDiff introduces interactionaware diffusion planning to mitigate ghost states and improve adaptability under changing targets [94]. ManiDext conditions diffusion policies on object 3D motion trajectories to synthesize high-quality in-hand manipulation sequences [95]. Diffusion policies are also extended to perceptually grounded manipulation. PAD unifies future visual prediction and action generation within a single diffusion process, supporting cross-modal learning from both videos and robot demonstrations [96]. 

**Imitation Learning.** Imitation learning is well-suited for in-hand manipulation, where high-dimensional finger coordination, persistent contact, and force–motion coupling make exploration and reward design difficult. By leveraging expert demonstrations, IL injects human manipulation priors and enables stable learning of contact-rich behaviors. Early studies focus on low-cost acquisition of in-hand demonstrations from human motion. Robotic Telekinesis retargets monocular human videos to robotic hands without specialized hardware [97], while ILAD synthesizes large-scale demonstrations from human grasp affordances to support cross-object generalization [98]. 

Subsequent work incorporates structural and dynamical constraints to improve learning efficiency and stability. DIME enables practical RGB-based demonstration collection [99], and KODex models coupled with hand–object dynamics using Koopman operators [100]. More recent approaches emphasize contact-aware imitation. DexForce integrates measured contact forces from kinesthetic demonstrations [101], while MimicTouch leverages multimodal tactile demonstrations for force-sensitive manipulation [102]. Vision-based imitation further evolves toward outcome-centric supervision, where HU- 

DOR extracts object-oriented imitation signals from human videos [103], and ViViDex distills video-derived demonstrations into physically plausible in-hand manipulation policies [104]. 

**Model-based Control.** Model-based control provides explicit physical reasoning, reliable multi-finger coordination, and strong generalization for contact-rich in-hand manipulation, making it safer, more stable, and less data-dependent than purely learning-based approaches. 

TrajectoTree[105] combines tree search with contactimplicit trajectory optimization in a hierarchical framework, decomposing and efficiently solving the complex contactswitching problems in multi-contact dexterous manipulation. This leads to faster, more stable, and more physically consistent manipulation planning. SmoothComp [106] proposes a model-based framework that leverages system dynamics for prediction, planning, and robust control, and addresses real-time and stability challenges through tube MPC and a piecewise-linearized optimization structure. LeTac-MPC [107] combines neural tactile encoding with a differentiable MPC layer, forming a learning-augmented model-based control framework that enables stable, interpretable, and real-time tactile-reactive grasping under dynamic disturbances and varying object physical properties. On the other hand, DextrAHG [108] combines a strongly model-driven geometric fabric controller with deep reinforcement learning and policy distillation, achieving safe, coordinated, real-time, and highly generalizable pixels-to-action dexterous grasping. 

**VLA.** VLA models introduce high-level semantic grounding and long-horizon task reasoning into dexterous in-hand manipulation. Rather than directly replacing low-level force and motion control, VLA primarily operates at the high and mid-level, providing task decomposition, semantic constraints, and goal-conditioned guidance that complement contact-rich 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

9 



<!-- Start of picture text -->
Precision  Grasping Neural<br>Assembly DexMV Dynamic Attention Push-Grasp SERL DextrAH-RGB ImMimic DexGraspVLA UniGraspTransformer<br>( Schoettler et al ) ( Qin et al ) ( Qin et al ) ( Wang et al ) ( Li et al ) ( Luo et al ) ( Wang et al ) ( Liu et al ) ( Zhong et al ) ( Wang et al )<br>Multimodal Learning Grain Manipulation Paper<br>D-Grasp Grasp Occluded CrossDex Grasp SpringGrasp via IL DiffusionRL Picking<br>( Christen et al ) ( Wu et al ) ( Zhou et al ) ( Yuan et al ) ( Zhao et al ) ( Chen et al ) ( An et al ) ( Makarova et al ) ( Lin et al )<br>2020 2021 2022 2023 2024 2025<br>Functional D(R,O) GenDP Pin-Pression SoftGrasp GraspVLA<br>Grasping ( Wei et al ) ( Wang et al ) ( Xiao et al ) ( Li et al ) ( Deng et al )<br>( Wei et al )<br>One-Shot UniDexGrasp UniDexGrasp++ DexDiffuser CyberDemo VLA Single-Demo D3Grasp<br>( Qin et al ) ( Xu et al ) ( Xu et al ) ( Weng et al ) ( Wang et al ) Grasping ( Li et al ) ( Wang et al )<br>( Pan et al )<br>Reinforcement  VLA Representation  Diffusion Policy Imitation  Others<br>Learning Learning Learning<br><!-- End of picture text -->

Fig. 5. Grasp & Pick-and-Place Timeline 

controllers. OpenVLA [109] establishes the open-source VLA paradigm by fine-tuning vision–language–action models for robotic manipulation, enabling dexterous hands to execute language-conditioned tasks. Octo [110] scales this paradigm to large trajectory datasets and demonstrates cross-embodiment generalization, while subsequent work further expands training data sources by incorporating Internet-scale human interaction data into the VLA framework [111]. 

Recent studies extend VLA toward stronger geometric grounding and hierarchical control, which are critical for in-hand manipulation. 3D-VLA [112] augments 2D visual inputs with 3D scene representations, enabling reasoning about hand–object geometry and contact. RoboDexVLM [113] and Villa-X [114] decompose long-horizon instructions into structured subgoals, marking a shift from end-to-end language policies toward hierarchical architectures that interface more naturally with low-level controllers. DexVLA [115] introduces plug-in diffusion experts to handle multimodal coordination during reorientation, while OmniVLA [116] unifies visual, linguistic, and haptic inputs within a single Transformer architecture, improving feedback stability during manipulation. 

**Other.** Several additional works, although not belonging to the categories discussed above, also introduce highly constructive approaches for in-hand manipulation and have significantly advanced the field. MyoDex [117] introduces a generalizable prior for high-DoF musculoskeletal hand models (MyoHand). By jointly training a multi-task policy across a wide range of manipulation behaviors, the method automatically discovers reusable muscle synergies within the complex muscle-driven dynamics. These synergies significantly improve generalization to unseen tasks and novel objects. When used as an initialization for downstream fine-tuning, the MyoDex prior accelerates convergence across 57 dexterous manipulation tasks and consistently achieves higher success rates than single-task training. Robot Synesthesia [89] presents a visuotactile fusion approach for in-hand manipulation, addressing the limitations of vision- or touch-only methods. Its key idea is the tactile point cloud, which maps tactile signals into 3D point clouds and fuses them with visual point clouds to form a unified touch–vision representation. 

## _C. Grasping and Pick-and-Place_ 

Grasping and pick-and-place constitute the foundational skills of dexterous manipulation, establishing stable 

hand–object coupling for downstream tasks [118], [119], [120]. Dexterous grasping is typically formulated as grasp generation followed by grasp execution, where feasible contact configurations are selected based on object geometry and task constraints, and then realized through motion planning and feedback control [121], [122], [123], [124]. Pick-and-place further introduces perceptual uncertainty and force regulation during transport and placement, requiring adaptive control based on tactile and contact feedback [125]. Fig. 5 shows the research timeline for grasping and pick-and-place. 

**Reinforcement Learning.** Reinforcement learning plays an important role in dexterous hand grasping and pick-and-place tasks, as it enables policies to learn contact-rich manipulation strategies directly through interaction. DRLKT [126] adopt task-related pretraining strategies to accelerate learning, while CrossDex [127] achieves cross-morphology data transfer between different dexterous hands, eliminating the need for retraining when the platform changes. In addition, Luo et al. focus on improving exploration strategies for realworld dexterous hands, significantly reducing interaction data requirements compared with standard RL [128]. 

Generalization across environments and embodiments is another central concern. To improve robustness under visual uncertainty, CrossDex [127] further extend point-cloud-based task representations to enable generalization across different dexterous hands, providing a promising solution to sim-to-real transfer failures. RL is also applied to increasingly complex grasping and pick-and-place scenarios that demand precise force regulation and rich contact reasoning. Schoettler et al. demonstrate submillimeter-precision industrial assembly using a vision-based RL policy [129], while Li et al. introduce coordinated push–grasp primitives to improve success rates in cluttered environments [130]. Hu et al. employ inverse reinforcement learning to infer manipulation strategies from human demonstrations, enabling robust interaction with dynamic targets [131]. 

**Diffusion Policy.** As shown in Fig. 6, diffusion policies generate smooth, multimodal, and robust action trajectories, significantly improving fine-grained control, generalization, and resilience to perceptual or physical disturbances in grasping and pick-and-place tasks. Wu et al. [132] introduced a diffusion policy for grasping tasks and modeled grasping generation as a denoising process, demonstrating that this strategy is more effective at capturing multimodal grasping distributions. It 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

10 



<!-- Start of picture text -->
PERCEPTION DIFFUSION POLICY PROCESS ACTUATION<br>RGB Camera Neural Network Convert a Signal Architecture Grasping<br>Noisy to Action  Diffusion Model<br>Process (Action Denoising)<br>Depth Sensors Manipulation<br>Noisy Action  Diffusion Policy  Iterative  Generated Action<br>Tactile Sensors State Neural Network Denoising Sequence Tool Using<br>t = T 4 steps t = 0<br>Pose & Force<br>Sensors Bimanual<br>Coordination<br><!-- End of picture text -->

Fig. 6. Overview of diffusion policies connecting multimodal perception to diverse dexterous manipulation tasks. The generative policy denoises action states into smooth control trajectories for varying task requirements. 

laid the foundation for the subsequent grasping and pick-andplace task operations. DexDiffuser[133] and GrainGrasp[134] considered the geometric and physical constraints of the object on this basis, enhancing the effect of contact operations. 

Additionally, GenDP[135] starts from the semantics of functional grasping, enabling operations to go beyond merely relying on large-scale shape learning and to better understand the functions of objects and achieve generalization. SpringGrasp[136] extends the grasping task of diffusion policy to flexible and variable objects, addressing the limitation that early operations were limited to rigid bodies. Pan et al.[137] combine VLA and diffusion policy to achieve advanced reasoning capabilities: VLA is responsible for identifying the grasping objects, and diffusion policy is responsible for handling the grasping strategies. Makarova et al.[138] combine diffusion policy and RL, improving the sample efficiency of using a single method. 

**Imitation Learning.** Imitation learning (IL) offers an effective alternative to reinforcement learning for grasping and pick-and-place tasks by directly leveraging expert demonstrations to learn fine-grained contact behaviors, while avoiding large-scale trial-and-error exploration [10]. Early visionbased approaches retarget human hand motions captured from videos to robotic hands [139], and are later extended with 3D hand–object reconstruction to extract grasping trajectories from daily-life videos [140]. To mitigate the morphological gap between human and robotic hands, adversarial domain adaptation further improves cross-instance generalization in video-based imitation learning [141]. 

Beyond vision-only supervision, multimodal imitation integrates visual, tactile, and proprioceptive signals to improve grasp robustness under varying object properties [142], and proves particularly effective for tactile-dominant pick-andplace tasks such as paper picking [143]. To address data efficiency, attention-based models enable one-shot or few-shot grasp learning [144], while reusable skill primitives support generalization to new objects and environments [145], [146]. In parallel, synthetic data pipelines such as CyberDemo scale supervision and demonstrate strong sim-to-real transfer [147]. 

**Representation Learning.** Representation learning provides stable, generalizable, and noise-robust visual features for grasping and pick-and-place, significantly improving policy 

learning efficiency, action planning, and cross-scene manipulation performance. D(R,O) [148] uses a distance matrix to encode the relationship between the hand’s geometry at a given grasp pose and the object’s shape. This representationlearning approach enables the model to learn a unified grasp representation across different hand embodiments, object categories, and configurations, allowing it to predict executable grasps directly from point clouds while remaining robust to partial or incomplete observations. UniDexGrasp [149] and UniDexGrasp++ [150] focus on learning universal dexterous grasping policies, with UniDexGrasp using object curriculum learning and DAgger distillation for category-level generalization, while UniDexGrasp++ incorporates geometry-aware representation learning for enhanced generalization across object shapes. Together, these models demonstrate that learning geometry-aware representations improves grasping generalization across hands, objects, and configurations. 

Furthermore, D3Grasp [151] constructs a multimodal representation that fuses visual, tactile, and hand-object interaction states into a unified semantic feature, which is used to guide reinforcement learning strategies. D-Grasp [152] formulates dynamic hand–object interaction as a representation-learning problem: instead of operating in the raw state space, it learns object-centric and grasp-conditioned representations that, combined with physics simulation and reinforcement learning, enable the synthesis of stable, physically plausible grasp-tomotion trajectories. UniGraspTransformer [153] uses a Transformer to learn a unified, generalizable grasp representation, improving cross-task and cross-object generalization. Offline distillation consolidates multiple expert policies into a single model, reducing data requirements while ensuring strong generalization and robustness. 



<!-- Start of picture text -->
MULTIMODAL<br>TRANSFORMER  ACTIONS<br>FOUNDATION MODEL<br>Camera RGB Image Data<br>Continuous Robotic<br>Attention Layers Control Dexterous Hand<br>Signal<br>Point Cloud 3D Geometric Data Token Processing a(t)<br>a(t+1)<br>A Text Prompt ：<br>文 a(t+n) Joint Angles,<br>Command / Goal “Pick up theblue cube.” Feature Extraction& Tokenization Cross-Modal Attention Velocity …Torques,<br>VISION  INPUT<br>…<br>LANGUAGE  INSTRUCTION<br><!-- End of picture text -->

Fig. 7. General architecture of a Vision-Language-Action (VLA) foundation model. Multimodal inputs (RGB/Depth and natural language instructions) are processed through a central Transformer model, which outputs low-level joint angle and torque commands for dexterous execution. 

**VLA.** As depicted in Fig. 7, incorporating VLA models into grasping and pick-and-place enables semantic understanding, cross-object generalization, multi-task capability, and more natural human–robot interaction, thereby significantly improving the flexibility, robustness, and generality of manipulation policies. By integrating a VLA architecture with dexterous grasping, DexGraspVLA [154] achieves unprecedented generalization and robustness in grasping and pick-and-place tasks. The system reaches over 90% zero-shot grasp success across 1,287 unseen cluttered scenes, handles challenging objects such as transparent, reflective, and deformable items, 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

11 

and executes long-horizon language-conditioned tasks with an overall success rate of 89.6%. It also supports non-prehensile pre-grasp strategies and remains robust under physical disturbances, positioning it as one of the most versatile and reliable VLA-driven grasping systems to date. 

Moreover, GraspVLA [155] applies a unified VisionLanguage-Action model to grasping and pick-and-place, achieving strong cross-object and cross-scene generalization. With SynGrasp-1B and large-scale semantic pretraining, it supports open-vocabulary understanding and zero-shot sim-toreal grasping, reaching 91 _._ 2% success on unseen objects and showing robust performance under challenging real-world conditions. Pan et al. combine VLA-based semantic planning with diffusion policy–based fine manipulation, achieving the first language-conditioned, highly robust, and multimodal grasping system for dexterous multi-fingered pick-and-place[137]. 

**Other.** Beyond the methods discussed above, several additional works have also demonstrated strong performance on grasping and pick-and-place tasks. Xiao et al. [156] use a deformable pin-pression gripper, together with geometryaware representations and curriculum RL, to achieve robust dynamic grasping and online in-hand adjustment for complex objects, thereby improving adaptability and stability compared with traditional parallel-jaw grippers. DextrAH-RGB [157] combines geometric fabrics, an RL-based teacher policy, and an RGB-only distilled student to form an end-to-end visuomotor control framework, achieving the first reliable sim-to-real transfer for RGB-based dexterous grasping and demonstrating strong robustness and generalization across diverse objects and real-world settings. Zhou et al. [158] uses external environmental cues and goal-conditioned RL to address occluded grasping, showing that extrinsic dexterity allows a simple gripper to execute complex grasp behaviors. 

## _D. Tool & Device Operation_ 

Tool and device operation represent some of the most challenging forms of dexterous manipulation, as they require reasoning about functional affordances rather than mere object geometry. Robots must understand how tools are intended to be used, adapt to variations in shape and mechanics, and generate precise force interactions to achieve task goals. Recent research explores multiple learning paradigms for this problem—from imitation learning that transfers human tooluse demonstrations, to reinforcement learning for mastering complex contact dynamics, to VLA models that inject semantic understanding of tool functions. As depicted in Fig. 8, we review representative methods under each category. 

**Reinforcement Learning.** RL can learn complex contact dynamics, non-intuitive coordination strategies, and taskspecific force behaviors in tool use and device operation, while also providing strong generalization and long-horizon planning abilities, making it a key approach for solving these challenging manipulation tasks. PDDM [159] combines deep dynamics models with online MPC, enabling RL to learn complex contact dynamics, fine-grained pose control, and non-intuitive manipulation strategies for tool use and device operation. This approach achieves high-precision dexterous 



<!-- Start of picture text -->
Design<br>PDDM Few Demo and Use MimicFunc<br>( Nagabandi et al ) ( Wei et al ) ( Liu et al ) ( Tang et al )<br>Hand-Tool<br>( Atar et al )<br>2020 2021 2022 2023 2024 2025<br>π0 DexGeb<br>( Black et al ) ( Yin et al )<br>TOG-Net RT-2 Hierarchical RL<br>( Fang et al ) ( Zıțkovich et al ) ( Xu et al )<br>Reinforcement Learning VLA<br>Imitation Learning Others<br><!-- End of picture text -->

Fig. 8. Tool Use & Device Operation Timeline 

manipulation in the real world with minimal data. Xu et al. [160] use hierarchical RL to decouple tool-deformation control from task-level planning, enabling a multifingered hand to learn complex three-way dynamics and non-intuitive tool-use strategies, ultimately achieving robust indirect grasping with articulated tools. Atar et al. [161] employ sim-toreal reinforcement learning to master the joint dynamics of articulated tools, and use tactile-guided online adaptation to achieve stable operation and generalization to unseen tools. Liu et al. [162] use a two-stage reinforcement learning framework that enables a robot to automatically design and deploy task-specific tools, leading to more efficient tool-use policy learning and stronger cross-task generalization. 

**Imitation Learning.** A key challenge in tool-use tasks lies in the large intra-function variations of differences in shape, size, and category—which makes many approaches that rely on geometric or visual similarity struggle to achieve one-shot generalization. MimicFunc addresses the problem of enabling a robot to imitate tool manipulation from a single human video and generalize the skill to entirely novel tools. Its core IL mechanism lies in inferring functional correspondences from the single demonstration and using them to synthesize executable robot trajectories [163].Wei et al. propose a method that enables robots to learn functional grasping from only a few human demonstrations and generalize to completely novel tools with diverse shapes. From these minimal demonstrations, the system extracts functional keypoints of the tool, the key hand poses used by humans, and a distribution of grasping preferences. In doing so, the robot learns the functional structure of the tool rather than merely imitating its geometric appearance [146]. 

**VLA.** VLA integrates visual perception with functional language semantics, enabling robots to understand tool purposes, decompose long-horizon tasks, generalize to new tools, and produce safer, more stable, and more precise tool-use behaviors through semantic alignment. RT-2 [164] aligns visual inputs with large-scale language semantics, enabling robots to understand tool functions, select appropriate or alternative tools, and act correctly in unseen scenarios, thereby greatly improving generalization and decision-making in tooluse tasks. _π_ 0 [165] introduces a VLA flow-based policy that aligns vision with language and produces continuous, highfrequency actions for multi-embodiment, cross-task manipula- 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

12 

tion. With large-scale pre-training and targeted post-training, it outperforms existing VLA and diffusion models, showing strong generalization and high performance across complex tasks. 

**Other.** There are also several methods outside the categories above that achieve strong performance on this task. DexGen [166] combines large-scale RL pretraining with a diffusion-based controller to build the first general-purpose dexterous hand foundation policy, transforming coarse highlevel commands into safe, stable, and fine-grained motions, and enabling unprecedented real-world dexterity such as rotation, regrasping, and complex tool use. Fang et al. use TOG-Net [167] to jointly optimize task-oriented grasping and manipulation strategies, trained in a self-supervised learning framework, successfully achieving task-specific tool grasping and manipulation, providing stability and high generalization for complex tasks. 

cloud input. Imitation learning is used in both stages. Firstly, using planner-generated expert demonstrations for pre-training in imitation learning. Then, finetuning with reinforcement learning in dynamic human-robot motion via a self-supervised teacher-student framework [170]. VRB is a system that learns visual affordances from large-scale human interaction videos for deployment on real robots. It provides demonstration priors that are directly usable for imitation learning and VRB effectively addresses the common data scarcity problem in imitation learning by supplying large-scale, video guidance[171]. In addition, several datasets can be used for interaction tasks within imitation-learning frameworks. OpenEgo is a largescale egocentric human-interaction dataset whose core value lies in systematically capturing real human–object interaction processes, including 3D hand joints, fine-grained dexterous motions, bimanual coordination patterns, and intention-aligned action primitives. These signals provide the essential priors that enable robots to learn human interaction behaviors [172]. 

## _E. Human Interaction_ 

Human–robot interaction tasks involve continuous motion, uncertainty, and strict safety requirements, making policy learning more challenging than object-centric dexterity. Unlike purely mechanical manipulation, interaction requires understanding human intent, predicting changes in motion, and maintaining compliant contact. Recent research therefore focuses on learning interaction strategies from human behavior—either through imitation to inherit natural handover patterns, or through reinforcement learning to adapt safely in dynamic collaboration. Below, we summarize key developments in imitation learning and reinforcement learning for human interaction. 

**Reinforcement Learning.** Reinforcement learning can handle the unpredictability of human motion, learn safe and compliant interaction strategies, and adapt to real-time feedback, making it a key approach for managing dynamic collaboration and contact uncertainty in human–robot interaction. Human-in-the-Loop Reinforcement Learning (HIL-RL) [168] framework that enables RL to learn precise, stable interaction behaviors with human participation. Through preferencebased RL, the policy is optimized to match human-preferred interaction styles rather than merely achieving task completion. By iteratively exploring and incorporating human corrections, RL compensates for missing demonstrations and significantly improves the robot’s adaptability to real human partners. Lin [169] et al. enhance the reliability of RL in realworld interaction scenarios by combining structured rewards, interaction-aware visual representations, and robust sim-toreal transfer, enabling robots to adapt stably to external disturbances in dynamic, contact-rich bimanual tasks and significantly improving interaction capability. 

**Imitation Learning.** In human interaction tasks, human motions are continuous, unpredictable, and subject to strict safety requirement. Imitation learning provides a direct prior on how humans perform handovers. In that case, imitation learning is a crucial method for human interaction tasks involving dexterous hands. Christen et al. introduce a two-stage framework for learning human-to-robot handovers from point 

## _F. Bimanual Manipulation_ 

Bimanual manipulation requires synchronized control of two high-DoF hands under complex contact dynamics, making coordination, force allocation, and stability notably more challenging than single-hand tasks. To address this, recent studies have developed dedicated learning frameworks and datasets that enable effective collaboration between both hands, as shown in Fig. 9. 



<!-- Start of picture text -->
Unified<br>Bimanual SIMPLe TACO BiDexHD PAD HATO MANIPTRANS<br>( Chen et al ) ( Frazese et al ) ( Liu et al ) ( Zhou et al ) ( Guo et al ) ( Lin et al ) ( Li et al )<br>HDP Bi-VLA<br>( Ma et al ) ( Gbagbe et al )<br>2022 2023 2024 2025<br>ARCTIC UMI DexMimicGen Shake-VLA<br>( Fan et al ) ( Chi et al ) ( Jiang et al ) ( Khan et al )<br>Bi-DexHands RoboMIND RDT-1B 3D-ViTac<br>( Chen et al ) ( Wu et al ) ( Liu et al ) ( Huang et al )<br>Reinforcement Learning Representation Learning VLA<br>Imitation Learning Diffusion Policy Others<br><!-- End of picture text -->

Fig. 9. Bimanual Manipulation Timeline 

**Reinforcement Learning.** Reinforcement learning plays a crucial role in bimanual manipulation, enabling coordinated control in high-dimensional coupled systems, adapting to complex contact-rich dynamics, providing flexible online adjustment, and leveraging demonstrations to achieve strong generalization, thereby enhancing the robustness and intelligence of bimanual manipulation. Bi-DexHands[90] establishes the first systematic learning platform for bimanual dexterous manipulation, enabling RL to acquire multi-contact coordination and complex dynamic skills, and serving as a key benchmark for advancing human-level bimanual manipulation research. HATO [173] presents the first scalable visuotactile imitation learning system that enables robots to learn realworld bimanual dexterous skills from human demonstrations and achieve high performance across multiple complex tasks. Chen et al. [174] introduces a unified framework for bimanual dexterous manipulation that combines multimodal perception 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

13 

with IL–RL hybrid learning, enabling coordinated control, contact switching, and force allocation. 

**Diffusion Policy.** Diffusion Policy can model multi-modal coordination strategies, generate smooth and coherent dualarm trajectories, and remain robust with only a small number of demonstrations, making it an ideal approach for handling the high-dimensional coupling inherent in bimanual manipulation. In HDP [175], the diffusion policy generates semantically aligned, physically feasible, and kinematically safe low-level control trajectories, making it a key component for achieving long-horizon and multi-task manipulation. PAD [96] unifies future visual prediction and action generation within a single diffusion denoising process, enabling the diffusion policy to learn more physically consistent and semantically aligned behaviors, which significantly improves generalization and real-world manipulation performance. 

**Imitation Learning.** In bimanual manipulation tasks, which require tightly coordinated motions, human-like motion is difficult for reinforcement learning to discover. Imitation learning improves training efficiency, prevents unnatural behaviors, and enhances generalization. Franzese et al. present SIMPLe, an Interactive Imitation Learning framework designed specifically for bimanual manipulation. By modeling demonstrations with a Graph Gaussian Process and allowing users to iteratively adjust trajectories, the method reduces the burden of demonstrations and enables dual-arm coordination to be learned through IL [176]. Maniptrans [177] frames dexterous bimanual manipulation as an imitation learning problem. A large human motion dataset is used to learn a human-like hand prior, and a small residual policy then adapts these imitated trajectories to satisfy physical constraints. This two-stage design based on IL enables the efficient transfer of human demonstrations to dexterous hands without task-specific rewards [177]. BiDexHD uses a human motion dataset (e.g., TACO [178]) and automatically parses trajectories, finger poses, and object poses.It converts each demonstration into a trainable task in the simulation. This removes the need for manually defining tasks and ensures that task diversity and quantity are no longer constrained [179]. 

Furthermore, UMI is a pipeline that can transfer in-thewild human demonstrations into a deployable dexterous hand policy. The approach eliminates the need for a physical robot during demonstrations, relying solely on a hand-held instrumented gripper to gather effective in-the-wild demonstrations for imitation learning, enabling the learned policies to zeroshot generalize when deployed on dexterous hands. It can achieve bimanual demonstrations via dual grippers [180]. In addition, some models can generate bimanual manipulation data for imitation learning by expanding the training set through a real-to-sim pipeline. DexMimicGen introduces an automated data generation system for imitation learning in bimanual dexterous manipulation. It models three types of dualarm subtasks—parallel, coordination, and sequential—and incorporates per-arm segmentation, asynchronous execution, synchronization, and ordering constraints. These mechanisms modularize otherwise tightly coupled bimanual actions and enable their automatic transformation and reproduction in simulation [181]. 

**VLA.** VLA provides strong cross-object and cross-scene generalization in bimanual manipulation. It supports role allocation and coordination between the two hands, offers better task decomposition and error recovery for long-horizon operations, and unifies high-level semantic reasoning with low-level action generation, enabling interpretable high-level planning for complex bimanual tasks. Bi-VLA [182] builds a VLA system for bimanual dexterous manipulation, where visual perception interprets the scene, language models generate task plans, and action modules execute coordinated dualarm behaviors, enabling multi-step tasks such as grasping, cutting, and mixing. The system executes complex bimanual tasks directly from language instructions without additional training. In RDT-1B [183], VLA encodes language task objectives and visual scene semantics as conditioning inputs for the diffusion policy, enabling the model to generate coordinated and robust bimanual action sequences directly from natural language instructions. Shake-VLA [184] introduces a Vision–Language–Action system for bimanual dexterous manipulation, specifically designed for multi-step cocktailmixing tasks. The system integrates visual recognition, speech interaction, RAG-based recipe retrieval, anomaly detection, and action execution, enabling a complete closed-loop pipeline from natural language instructions to recipe lookup, ingredient verification, and coordinated dual-arm execution. 

**Representation Learning.** Representation learning provides structured, semantic, and generalizable state spaces for bimanual manipulation, enabling policies to more easily acquire coordinated, multi-stage, and contact-rich behaviors while maintaining strong robustness across objects and environments. 3D-ViTac’s [185] core contribution is the introduction of a unified 3D visuo-tactile representation that projects RGB-D point clouds and high-resolution tactile signals into a shared 3D coordinate space, producing a geometrically and semantically consistent multi-modal point-cloud embedding. This unified representation provides a structured, generalizable, and occlusion-robust state space, enabling diffusion policies to learn multi-contact, force-sensitive, and geometrically constrained bimanual manipulation more reliably. ARCTIC [186] provides a high-precision, temporally synchronized dataset of bimanual articulated hand–object interactions, enabling representation learning to be systematically trained for the first time in realistic, dynamic, multi-contact, and coordinated dual-hand manipulation scenarios. 

**Other.** There are also several approaches that do not fall neatly into the categories above but nevertheless demonstrate strong performance on bimanual manipulation tasks. RoboMIND [187] offers a unified cross-embodiment, crosstask, multi-modal data foundation that enables representation learning to capture coordination patterns, contact dynamics, and semantic task structures in bimanual manipulation. This dataset provides essential support for the generalization of VLA, imitation learning, and diffusion policies in complex dual-arm tasks. 

IV. DATASET OF DEXTEROUS HAND RESEARCH 

This section surveys representative datasets for dexteroushand research from three interconnected perspectives: data 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

14 

TABLE II 

SUMMARY OF MAJOR DEXTEROUS HAND DATASETS. 

|**Dataset**|**Year Scene**|**Modality**|**Embodiment**|**Collection**|**Scale**|
|---|---|---|---|---|---|
|DexGraspNet [181]|2022 Sim.|Pose, Object, Point cloud|Shadow Hand|Optimization-based|1.32M poses; 5355 objects|
|GenDexGrasp [182]|2022 Sim.|Pose, Contact, Object|Barrett; Robotiq; Allegro; Shado|w Hand Optimization-based|436K poses; 58 objects|
|DexMV [140]|2022 Real+Sim.|RGB, Pose, Point cloud|Adroit Hand|Human capture|700 demos;|
|DexArt [188]|2023 Sim.|Point cloud, Proprioception|Adroit; Allegro|learning-based|82 objects|
|UniDexGrasp++ [150]|2023 Sim.|Pose, Point cloud, Proprioception|Shadow Hand|learning-based|1.32M poses; 5355 objects|
|RealDex [122]|2024 Real|Pose, RGB-D, Point cloud|Shadow Hand|Human capture|59K poses; 52 objects; 2.6K seqs.|
|DexCap [189]|2024 Real|Pose, RGB-D, Point cloud|LEAP Hand|Human capture|3.5h demo|
|DexFuncGrasp [190]|2024 Real+Sim.|Pose, RGB-D, Contact|Shadow Hand|Human capture|14K+ Pose; 559 objects|
|RH20T [191]|2024 Real|RGB-D; Contact; Proprioception|Franka; Allegro;|Human capture|110K+ seqs.|
|DexGraspAnything [192]|2025 Sim.|Pose, RGB-D, Point cloud, Semantics|Shadow Hand|learning-based|3.4M grasps; 15.7K objects|
|BODex [193]|2025 Sim.|Pose, Contact, Object|Shadow Hand|Optimization-based|3.08M grasps; 2397 objects|
|CEDex [194]|2025 Sim.|Pose, Contact, Point cloud|Allegro; LEAP Hand|learning-based|20M grasps; 500K objects|
|Dex1B [195]|2025 Sim.|Pose, Contact, Object|Inspire; Ability Hand|learning-based|1B demos; 6K+ objects|
|DexTOG [196]|2025 Sim.|Pose, Point cloud, Semantics|Shadow Hand|learning-based|80K grasps; 80 objects|
|VTDexManip [197]|2025 Sim.|RGB, Contact|Shadow Hand|Human capture|182 objects; 2032 seqs.|



acquisition (Section IV-A), modality design (Section IV-B), and evaluation (Section IV-C). Furthermore, the overview of representative datasets is summarized in Table II. 

Broader robot-learning efforts also aggregate heterogeneous datasets for cross-embodiment training [203], and multimodal capture systems continue to blend sensing modalities to improve coverage. These trends complement the three collection families above. 

## _A. Data Acquisition_ 

From a collection-method perspective, recent dexteroushand datasets can be grouped into three families, summarized in the Collection column of Table II: optimizationbased acquisition in simulation, learning-based acquisition in simulation, and human capture. The distinction is whether labels come mainly from numerical optimization, from learned or generative models, or from human demonstrations and wearable sensing in the real world, optionally followed by simulation-based verification or scaling. 

**Optimization-based.** These pipelines synthesize grasps or interaction poses by minimizing analytic or differentiable objectives, such as force-closure energies, bilevel programs with QP subproblems, or SDF-based refinement, and they validate candidates in physics engines such as MuJoCo or Isaac Gym [198]. They offer high throughput and reproducible labels, but quality still depends on energy design and the simto-real gap. 

**Learning-based.** These [188], [150], [194], [195] data are produced or enlarged by learned components: reinforcement learning with curricula and distillation, diffusion or other generative models, retrieval-based and rule-guided data engines, or model-in-the-loop filtering and expansion. Such methods can reach very large scales and encode complex distributions, at the cost of training stability, compute, and careful alignment with physical plausibility. 

**Human Capture.** This family records humans or teleoperated robots directly, using multi-view RGB-D, wearable motion capture, electromagnetic or inertial gloves, tactile arrays, or similar modalities [199], [200], [201], [202]. It yields realistic contact and behavior priors but can be expensive to scale. Many systems combine human acquisition with downstream simulation; for example, retargeting human motions to dexterous hands and checking grasps in sim, or augmenting mocap with reinforcement learning rollouts. In those cases, the boundary to pure simulation is methodological rather than exclusive. 

## _B. Data Modality_ 

The Modalities column in Table II shows that curated dexterous manipulation datasets are increasingly organized around complementary observation channels rather than a single sensing stream. The most common foundation is geometric state, including hand and object poses, object meshes or point clouds, and robot proprioception. These signals provide the structural information required for grasp synthesis, state estimation, and object-centric control. In parallel, visual observations such as RGB or RGB-D are widely adopted [140], [122], [189], [190], [191], [192], [197], especially in real-world and hybrid pipelines, because they preserve scene appearance, occlusion, and cross-instance variation that geometry alone cannot capture. Geometry and visual appearance form the perceptual basis of most current dexterous learning pipelines. 

A second trend is the growing inclusion of contact-related modalities, reflecting the fundamentally contact-rich nature of dexterous manipulation. Beyond pose and vision, many recent datasets [204], [190], [191], [193], [194], [195], [197] explicitly record contact labels, tactile signals, force and torque measurements, or contact-aware visual observations. These modalities are particularly important for grasp stability, slip detection, force regulation, and fine manipulation under partial observability. Thus, curated datasets differ not only in scale, but also in how contact is represented: some remain geometrydominant and mainly support grasp generation, whereas others incorporate richer interaction signals and are better suited for closed-loop manipulation and tactile-reactive control. 

Another emerging direction is the integration of semantics and task-level conditioning. Several recent datasets [192], [196] augment geometric and contact-centric observations with semantic labels, task descriptors, or language-level annotations, enabling learning beyond isolated grasp generation toward task-aware and long-horizon manipulation. This shift matters because dexterous behavior is rarely defined only by contact feasibility; it also depends on what action 

15 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

should be performed, under which object function, and toward which downstream goal. Therefore, dataset modalities should be understood not merely as sensing choices, but also as assumptions about the level of manipulation intelligence a benchmark can support. In practice, modality composition largely determines whether a dataset is best suited for grasp prediction, contact-rich closed-loop control, or semantically conditioned manipulation. 

## _C. Evaluation_ 

**Evaluation Metric.** Evaluation in curated dexterous-hand datasets is highly heterogeneous and cannot be reduced to a single notion of success. In practice, existing works usually assess at least two layers of performance: the quality of grasps or poses prior to execution, and the performance of policies or generators during downstream execution. For grasp- and posecentric datasets, the most common criteria concern physical plausibility, including penetration, analytic or quasi-static stability, and diversity over generated grasp proposals or object geometries. Representative examples include DexGraspNet, GenDexGrasp, CeDex, BODex, and DexGrasp, which emphasize whether synthesized grasps are physically feasible and sufficiently diverse before policy deployment [205], [204], [194], [193], [192]. Related benchmarks such as DexTOG further connect grasp-level quality with downstream utility by jointly considering grasp validity and policy performance, explicitly distinguishing analytic grasp quality from executable manipulation value [196]. 

A second evaluation dimension concerns whether policies trained on a dataset can reliably execute manipulation tasks and generalize beyond the conditions seen during training. Here, task success rate remains the dominant endpoint, but its interpretation depends strongly on the evaluation protocol. Simulation-oriented benchmarks such as DexArt, UniDexGrasp++, and Dex1B evaluate not only nominal task completion, but also transfer across held-out object instances, unseen categories, or broader task settings [188], [150], [195]. Datasets with tactile sensing introduce an additional robustness axis. For example, VTDexManip emphasizes performance under contact uncertainty and evaluates manipulation under variations such as unseen objects, viewpoint changes, tactile thresholds, and tactile noise [197]. Taken together, these works show that the success rate is meaningful only when paired with a clear specification of whether it reflects nominal execution, cross-instance generalization, or robustness to sensing perturbations [188], [150], [197], [195]. 

For real-world or human-capture datasets, reporting often shifts from grasp validity alone toward motion fidelity, stage completion, and demonstration quality. RH20T, for instance, supports long-horizon human manipulation analysis and is commonly associated with stage-aware or temporally structured evaluation rather than only single-step task completion [191]. DexCap and related imitation-oriented settings place greater emphasis on repeated-trial task success, subtask completion, and data efficiency, making partial progress distinguishable from full execution success [189]. Other real or hybrid datasets, including RealDex, DexMV, and DexFuncGrasp, additionally emphasize real-robot success, trajectory 

consistency, contact realism, or motion reconstruction fidelity, reflecting that real-world dexterous manipulation is often evaluated not only by task completion, but also by how stably, naturally, and efficiently the behavior is executed [122], [140], [190]. These protocols indicate that current reporting practices combine multiple notions of quality, including grasp validity, execution success, generalization, robustness, motion realism, and demonstration efficiency [122], [189], [191], [140], [190]. 

**Reliability and Trustworthiness.** Beyond conventional performance metrics, reliability and trustworthiness are increasingly important for dexterous hand systems, especially when learning-based policies are deployed in open, contact-rich, and human-centered environments [206]. Real-world deployment requires not only high task success but also reliable perception, robust decision making, safe interaction, and predictable failure behavior. A system may perform well under nominal benchmark settings, yet still fail under occlusion, sensor noise, ambiguous object boundaries, unseen objects, changing contact conditions, or human intervention [207]. Therefore, evaluation protocols should move beyond benchmark-centered assessment and include reliability-oriented criteria. 

A key requirement is to evaluate whether the system can perceive, decide, and recover reliably under uncertainty and distribution shift. Dexterous hand systems depend on object detection, segmentation, pose estimation, affordance prediction, and contact-region understanding, where errors may propagate to grasp planning, force control, and policy execution. Future evaluation should therefore assess not only perception accuracy and task success, but also uncertainty calibration, robustness to occlusion and clutter, out-of-distribution detection, failure prediction, recovery rate, safety violation rate, and multimodal consistency across vision, tactile sensing, and proprioception. These criteria can better reveal whether a dexterous hand system is not only capable, but also reliable, interpretable, and safe in open environments [208], [209], [210]. 

## V. CURRENT LIMITATIONS AND FUTURE DIRECTIONS 

Although dexterous hand research has made remarkable progress in recent years, it still faces several fundamental challenges that limit the applicability of existing technologies and, at the same time, point to the most critical future directions. Rather than discussing limitations and future work separately, it is more coherent to connect each current bottleneck with its corresponding research avenue. 

**From the trade-off between bionic complexity and hardware feasibility to scalable dexterous hand design.** The design of dexterous hands faces a fundamental tradeoff between high degrees of freedom and system complexity. Achieving human-like manipulation requires tightly integrated actuation, perception, and control, which increases mechanical complexity, computational demand, and system cost. As a result, existing robotic hands either simplify structure at the expense of manipulation capability or suffer from limited reliability, scalability, and maintainability due to highly integrated mechatronic systems. A promising direction is to move from mechanical complexity toward functional intelligence. 

16 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

Rather than merely mimicking appearance or structure, future research should focus more on the biomechanical and neural control mechanisms of the human hand [211]. In this regard, motion synergies offer an effective means to reduce control dimensionality, allowing coordinated movements of multiple joints to be driven by a single control signal. 

**From the dilemma of multimodal perception fusion to robust and interpretable perception.** Despite increasing sensor integration, effective multimodal perception fusion in dexterous hands remains challenging. Differences in sensing modalities, update rates, noise characteristics, and spatial locality make real-time synchronization and interpretation difficult. As a result, achieving stable, low-latency perception– control loops under contact-rich conditions remains a major bottleneck for human-level dexterity. To address this, perception systems should move beyond simple multi-sensor integration toward cross-modal contextual understanding, with stronger emphasis on robustness, generalization, and trustworthiness under noisy or partially missing sensory inputs. 

**From limitations in learning, control, and data to robust and generalizable learning frameworks beyond benchmark-centric optimization.** Traditional model-based control relies on accurate dynamics models, yet the complex and discontinuous contact interactions in dexterous manipulation make precise modeling difficult, leading to performance degradation. Although data-driven methods have become dominant, learning-based approaches still suffer from distribution shift, limited generalization, safety concerns, and heavy computational demands, especially when combined with large models [212]. These challenges are further aggravated by data limitations. Existing datasets also lack sufficient diversity in long-horizon interactions, failure cases, and recovery behaviors, and tactile information is often underutilized. Looking forward, learning frameworks should move beyond benchmark-centric optimization toward robust, generalizable, and trustworthy policy learning [213], [214], so that commands can be interpreted and executed in physically plausible and semantically meaningful ways [215], [212]. 

**From system integration and industrialization barriers to deployable dexterous platforms.** Cost and reliability remain the primary barriers to the industrial deployment of dexterous hands. High-performance systems such as the Shadow Hand are expensive to manufacture and maintain, while lowcost or open-source alternatives often sacrifice sensing quality, material durability, or long-term reliability, limiting large-scale adoption [216]. These issues are further amplified by the high training and deployment cost of dexterous manipulation policies. High-dimensional state–action spaces impose substantial sample and computational demands, and the sim-to-real gap continues to degrade real-world performance despite domain randomization and adaptation efforts [164], [217], [218]. In addition, the absence of unified performance evaluation standards and benchmark protocols hampers objective comparison across systems, slowing standardization and industrialization. Establishing authoritative evaluation frameworks is therefore essential for the sustainable development of dexterous hand technologies [11]. A practical future direction is to move from laboratory prototypes toward deployable dexterous platforms 

through modular system design, standardized interfaces, and plug-and-play components such as fingers, joints, and sensors, thereby making manufacturing, maintenance, and upgrades more affordable and scalable. 

## VI. CONCLUSION 

This survey revisits dexterous hand research from a holistic perspective and organizes the field around hardware design, methodological development in control and learning, datasets and evaluation practices, and the field’s major limitations and future directions. At the hardware level, we summarize key developments in actuation, transmission, perception, and representative hand designs, showing that dexterous hand design is fundamentally shaped by trade-offs in force capability, compliance, bandwidth, integration, and system complexity. At the methodological level, we review the evolution of control and learning approaches, highlighting how different paradigms have emerged to address increasingly complex dexterous manipulation problems. We further consolidate datasets, modality design, and evaluation practices, emphasizing that methodological progress should be interpreted together with the ways in which dexterous manipulation is trained, benchmarked, and assessed. 

Despite substantial progress, dexterous hand research still faces several fundamental challenges. These include the tradeoff between dexterity and hardware complexity, the difficulty of integrating and synchronizing multimodal perception, the limited generalization of learning-based methods, the constraints imposed by data quality and scale, and the practical barriers of system integration and industrial deployment. In addition, the lack of unified evaluation standards continues to hinder fair comparison across different systems and methods. Looking forward, further progress will depend on more effective hardware design, better integration of sensing and control, more scalable and informative datasets, more transferable and data-efficient learning methods, and more standardized evaluation frameworks. We hope this survey provides a structured framework for understanding the development of dexterous hands and clarifies promising directions for future research. 

## REFERENCES 

- [1] A. Bicchi, “Hands for dexterous manipulation and robust grasping: a difficult road toward simplicity,” _IEEE Transactions on Robotics and Automation_ , vol. 16, no. 6, pp. 652–662, 2000. 

- [2] J. Vertongen, D. G. Kamper, G. Smit, and H. Vallery, “Mechanical aspects of robot hands, active hand orthoses, and prostheses: A comparative review,” _IEEE/ASME Transactions on Mechatronics (T-MECH)_ , vol. 26, no. 2, pp. 955–965, 2020. 

- [3] M. Pozzi, M. Malvezzi, D. Prattichizzo, and G. Salvietti, “Actuated palms for soft robotic hands: review and perspectives,” _IEEE/ASME Transactions on Mechatronics (T-MECH)_ , vol. 29, no. 2, pp. 902–912, 2023. 

- [4] G. Gu, N. Zhang, C. Chen, H. Xu, and X. Zhu, “Soft robotics enables neuroprosthetic hand design,” _ACS Nano_ , vol. 17, no. 11, pp. 9661– 9672, 2023. 

- [5] H. Yousef, M. Boukallel, and K. Althoefer, “Tactile sensing for dexterous in-hand manipulation in robotics—a review,” _Sensors and Actuators A: Physical_ , vol. 167, no. 2, pp. 171–187, 2011. 

- [6] Q. Li, O. Kroemer, Z. Su, F. F. Veiga, M. Kaboli, and H. J. Ritter, “A review of tactile information: Perception and action through touch,” _IEEE Transactions on Robotics (T-RO)_ , vol. 36, no. 6, pp. 1619–1634, 2020. 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

17 

- [7] T. Liang, Z. Liu, H. Zhang, X. Zhou, and Y. Liang, “The structure, material and performance of multi-functional tactile sensor and its application in robot field: A review,” _Materials Today_ , 2025. 

- [8] H. Zhou and G. Alici, “Non-invasive human-machine interface (hmi) systems with hybrid on-body sensors for controlling upper-limb prosthesis: A review,” _IEEE Sensors Journal_ , vol. 22, no. 11, pp. 10292– 10307, 2022. 

- [9] X. Song, Y. Li, Y. Zhang, _et al._ , “An overview of learning-based dexterous grasping: Recent advances and future directions,” _Artificial Intelligence Review_ , vol. 58, p. 300, 2025. 

- [10] S. An, Z. Meng, C. Tang, Y. Zhou, T. Liu, F. Ding, S. Zhang, Y. Mu, R. Song, W. Zhang, _et al._ , “Dexterous manipulation through imitation learning: A survey,” _arXiv preprint arXiv:2504.03515_ , 2025. 

- [11] Y. Huang, D. Fan, H. Duan, D. Yan, W. Qi, J. Sun, Q. Liu, and P. Wang, “Human-like dexterous manipulation for anthropomorphic five-fingered hands: A review,” _Biomimetic Intelligence and Robotics_ , p. 100212, 2025. 

- [12] E. Welte and R. Rayyes, “Interactive imitation learning for dexterous robotic manipulation: Challenges and perspectives – a survey,” 2025. 

- [13] C. Firth, K. Dunn, M. H. Haeusler, and Y. Sun, “Anthropomorphic soft robotic end-effector for use with collaborative robots in the construction industry,” _Automation in Construction_ , vol. 138, p. 104218, 2022. 

- [14] Q. Wang, Y. Tu, W. Xu, J. Zhang, A. Knoll, M. Zhou, and Y. Ying, “Towards damage-less robotic fragile fruit grasping: A systematic review on system design, end effector, and visual and tactile feedback,” _Journal of Field Robotics_ , 2025. 

- [15] B. Gao, J. Fan, and P. Zheng, “Empower dexterous robotic hand for human-centric smart manufacturing: A perception and skill learning perspective,” _Robotics and Computer-Integrated Manufacturing (RCIM)_ , vol. 93, p. 102909, 2025. 

- [16] J. Zhang, H. Zhao, K. Chen, G. Fei, X. Li, Y. Wang, Z. Yang, S. Zheng, S. Liu, and H. Ding, “Dexterous hand towards intelligent manufacturing: A review of technologies, trends, and potential applications,” _Robotics and Computer-Integrated Manufacturing (RCIM)_ , vol. 95, p. 103021, 2025. 

- [17] S. B. Skaar, “Robot modeling and control-[book review; m. spong, s. hutchinson, and m. vidyasagar],” _IEEE Transactions on Automatic Control (T-ACON)_ , vol. 52, no. 2, pp. 378–379, 2007. 

- [18] W. Zhang, Z. Yu, X. Chen, and Q. Huang, “The magneto-thermal analysis of a high torque density joint motor for humanoid robots,” in _IEEE/RAS International Conference on Humanoid Robots (Humanoids)_ , pp. 112–117, 2018. 

- [19] K. Guo, Y. Guo, S. Fang, C. Li, and W. Xue, “Design and analysis of a permanent magnet frameless motor,” _IEEE Journal of Emerging and Selected Topics in Power Electronics_ , vol. 12, no. 3, pp. 3124–3134, 2024. 

- [20] K. Guo, J. Lu, and H. Yang, “Simulation analysis of a sandwich cantilever ultrasonic motor for a dexterous prosthetic hand,” _Micromachines_ , vol. 14, no. 12, p. 2150, 2023. 

- [21] S. Izuhara and T. Mashimo, “Miniature robot finger using a micro linear ultrasonic motor and a closed-loop linkage,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 1–9, 2018. 

- [22] A. Kargov, T. Werner, C. Pylatiuk, and S. Schulz, “Development of a miniaturised hydraulic actuation system for artificial hands,” _Sensors and Actuators A: Physical_ , vol. 141, no. 2, pp. 548–557, 2008. 

- [23] J. Zhou, J. Huang, Q. Dou, P. Abeel, and Y. Liu, “A dexterous and compliant hand based on soft hydraulic actuation for human inspired fine in-hand manipulation,” _IEEE Transactions on Robotics (T-RO)_ , 2024. 

- [24] C.-P. Chou and B. Hannaford, “Measurement and modeling of mckibben pneumatic artificial muscles,” _IEEE Transactions on Robotics and Automation_ , vol. 12, no. 1, pp. 90–102, 1996. 

- [25] J. Bishop-Moser, G. Krishnan, and S. Kota, “Force and moment generation of fiber-reinforced pneumatic soft actuators,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 4460–4465, 2013. 

- [26] Y. W. Hadi, B. A. Y. Sunarya, A. F. Alifdhyatra, E. Hidayat, J. Salomo, A. Purwidyantri, B. A. Prabowo, and I. Anshori, “Programmable soft robotics actuator with pneumatic networks (pneunets),” _IEEE Sensors Journal_ , vol. 23, no. 17, pp. 19382–19389, 2023. 

- [27] M. A. Robertson and J. Paik, “New soft robots really suck: Vacuumpowered systems empower diverse capabilities,” _Science Robotics_ , vol. 2, no. 9, p. eaan6357, 2017. 

- [28] J.-G. Lee and H. Rodrigue, “Design and analysis of reconfigurable origami-based vacuum pneumatic artificial muscles for versatile robotic system,” _Soft Robotics_ , vol. 11, no. 6, pp. 984–993, 2024. 

- [29] C. Tawk, G. M. Spinks, M. in het Panhuis, and G. Alici, “3d printable linear soft vacuum actuators: their modeling, performance quantification and application in soft robotic systems,” _IEEE/ASME Transactions on Mechatronics (T-MECH)_ , vol. 24, no. 5, pp. 2118– 2129, 2019. 

- [30] H. Baek, A. M. Khan, V. Bijalwan, S. Jeon, and Y. Kim, “Dexterous robotic hand based on rotational shape memory alloy actuator-joints,” _IEEE Transactions on Medical Robotics and Bionics (T-MRB)_ , vol. 5, no. 4, pp. 1082–1092, 2023. 

- [31] P. Brochu and Q. Pei, “Advances in dielectric elastomers for actuators and artificial muscles,” _Macromolecular Rapid Communications_ , vol. 31, no. 1, pp. 10–36, 2010. 

- [32] Q. Zhang, W. Yu, J. Zhao, C. Meng, and S. Guo, “A review of the applications and challenges of dielectric elastomer actuators in soft robotics,” _Machines_ , vol. 13, no. 2, p. 101, 2025. 

- [33] M. Seong, K. Sun, S. Kim, H. Kwon, S.-W. Lee, S. C. Veerla, D. K. Kang, J. Kim, S. Kondaveeti, S. M. Tawfik, _et al._ , “Multifunctional magnetic muscles for soft robotics,” _Nature Communications (NC)_ , vol. 15, no. 1, p. 7929, 2024. 

- [34] S. Zhang, Y. Liu, J. Deng, X. Gao, J. Li, W. Wang, M. Xun, X. Ma, Q. Chang, J. Liu, _et al._ , “Piezo robotic hand for motion manipulation from micro to macro,” _Nature Communications (NC)_ , vol. 14, no. 1, p. 500, 2023. 

- [35] N. Zhang, P. Zhou, X. Yang, F. Shen, J. Ren, T. Hou, L. Dong, R. Bian, D. Wang, G. Gu, _et al._ , “Biomimetic rigid-soft finger design for highly dexterous and adaptive robotic hands,” _Science Advances_ , vol. 11, no. 17, 2025. 

- [36] H. Yang, Z. Tao, J. Yang, W. Ma, H. Zhang, M. Xu, M. Wu, S. Sun, H. Jin, W. Li, _et al._ , “A lightweight prosthetic hand with 19-dof dexterity and human-level functions,” _Nature Communications (NC)_ , vol. 16, no. 1, p. 955, 2025. 

- [37] J. Xia, J. Huang, S. Fu, J. Qu, L. Mo, Y. Li, T. Ren, Y. Yang, Y. Li, and H. Liu, “Discrete pneumatic-tendon-coupled actuators with interconnected air circuit for untethered soft robots,” _Advanced Intelligent Systems_ , vol. 7, no. 4, 2025. 

- [38] L. Birglen, T. Lalibert´e, and C. Gosselin, _Underactuated Robotic Hands_ , vol. 40 of _Springer Tracts in Advanced Robotics_ . Berlin, Heidelberg: Springer, 2008. 

- [39] G. Palli, C. Melchiorri, G. Vassura, U. Scarcia, L. Moriello, G. Berselli, A. Cavallo, G. De Maria, C. Natale, S. Pirozzi, _et al._ , “The dexmart hand: Mechatronic design and experimental evaluation of synergybased control for human-like grasping,” _The International Journal of Robotics Research_ , vol. 33, no. 5, pp. 799–824, 2014. 

- [40] M. Yin, H. Wang, D. Shang, M. Li, T. Xu, and X. Wu, “Disturbance compensation control for humanoid robot hand driven by tendon-sheath based on disturbance observer,” _IEEE Transactions on Automation Science and Engineering (T-ASE)_ , 2025. 

- [41] S. R. Company, “Shadowrobot dexterous hand.” https://www. shadowrobot.com/dexterous-hand-series/, 2005. 

- [42] L. B. Bridgwater, C. Ihrke, M. A. Diftler, M. E. Abdallah, N. A. Radford, J. Rogers, S. Yayathi, R. S. Askew, and D. M. Linn, “The robonaut 2 hand-designed to do work with tools,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 3425–3430, 2012. 

- [43] M. Grebenstein, M. Chalon, W. Friedl, S. Haddadin, T. Wimb¨ock, G. Hirzinger, and R. Siegwart, “The hand of the dlr hand arm system: Designed for interaction,” _The International Journal of Robotics Research_ , vol. 31, no. 13, pp. 1531–1555, 2012. 

- [44] Y. Tu, J. Jiang, S. Li, N. Hendrich, M. Li, and J. Zhang, “Posefusion: Robust object-in-hand pose estimation with selectlstm,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 6839–6846, 2023. 

- [45] S. G. . C. KG, “Svh 5-finger gripping hand.” https://schunk.com/de en/gripping-systems/highlights/svh/, 2025. 

- [46] F. M. Ribeiro, T. Correia, J. Lima, G. Gonc¸alves, and V. H. Pinto, “Modeling and realistic simulation of a dexterous robotic hand: Svh hand use-case,” in _IEEE International Conference on Autonomous Robot Systems and Competitions (ICARSC)_ , pp. 132–138, 2023. 

- [47] U. Kim, D. Jung, H. Jeong, J. Park, H.-M. Jung, J. Cheong, H. R. Choi, H. Do, and C. Park, “Integrated linkage-driven dexterous anthropomorphic robotic hand,” _Nature Communications (NC)_ , vol. 12, no. 1, p. 7177, 2021. 

- [48] L. Birglen and C. M. Gosselin, “Kinetostatic analysis of underactuated fingers,” _IEEE Transactions on Robotics and Automation_ , vol. 20, no. 2, pp. 211–221, 2004. 

- [49] L. Birglen and C. M. Gosselin, “Grasp-state plane analysis of twophalanx underactuated fingers,” _Mechanism and Machine Theory_ , vol. 41, no. 7, pp. 807–822, 2006. 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

18 

- [50] D. Yoon and Y. Choi, “Underactuated finger mechanism using contractible slider-cranks and stackable four-bar linkages,” _IEEE/ASME Transactions on Mechatronics (T-MECH)_ , vol. 22, no. 5, pp. 2046– 2057, 2017. 

- [51] Z. Wan, Z. Bi, Z. Zhou, H. Ren, Y. Zeng, Y. Li, L. Qi, X. Yang, M.-H. Yang, and H. Cheng, “Rapid hand: A robust, affordable, perceptionintegrated, dexterous manipulation platform for generalist robot autonomy,” _arXiv preprint arXiv:2506.07490_ , 2025. 

- [52] M. Higashimori, H. Jeong, I. Ishii, M. Kaneko, A. Namiki, and M. Ishikawa, “A new four-fingered robot hand with dual turning mechanism,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 2679–2684, 2005. 

- [53] Q. Quan, Q. Wang, Z. Deng, S. Jiang, X. Hou, and D. Tang, “A planetary gear based underactuated self-adaptive robotic finger,” in _IEEE International Conference on Robotics and Biomimetics (ROBIO)_ , pp. 1586–1591, 2013. 

- [54] K. Tahara, K. Maruta, A. Kawamura, and M. Yamamoto, “Externally sensorless dynamic regrasping and manipulation by a triple-fingered robotic hand with torsional fingertip joints,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 3252–3257, 2012. 

- [55] S. Yuan, A. D. Epps, J. B. Nowak, and J. K. Salisbury, “Design of a roller-based dexterous hand for object grasping and within-hand manipulation,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 8870–8876, 2020. 

- [56] J. C. Tuthill and E. Azim, “Proprioception,” _Current Biology_ , vol. 28, no. 5, pp. R194–R203, 2018. 

- [57] A. S. Morgan, W. G. Bircher, and A. M. Dollar, “Towards generalized manipulation learning through grasp mechanics-based features and selfsupervision,” _IEEE Transactions on Robotics (T-RO)_ , vol. 37, no. 5, pp. 1553–1569, 2021. 

- [58] J. Shi, J. Z. Woodruff, P. B. Umbanhowar, and K. M. Lynch, “Dynamic in-hand sliding manipulation,” _IEEE Transactions on Robotics (T-RO)_ , vol. 33, no. 4, pp. 778–795, 2017. 

- [59] W. Zhao, Y. Yan, C. Yang, J. Ye, X. Yang, and K. Huang, “Divide and conquer: 3d point cloud instance segmentation with point-wise binarization,” in _IEEE/CVF International Conference on Computer Vision (ICCV)_ , pp. 562–571, 2023. 

- [60] W. Zhao, R. Zhang, Q. Wang, G. Cheng, and K. Huang, “Bfanet: Revisiting 3d semantic segmentation with boundary feature analysis,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 29395–29405, 2025. 

- [61] C. Li, A. Fahmy, and J. Sienz, “Development of a neural networkbased control system for the dlr-hit ii robot hand using leap motion,” _IEEE Access_ , vol. 7, pp. 136914–136923, 2019. 

- [62] R. Saegusa, G. Metta, and G. Sandini, “Self-body discovery based on visuomotor coherence,” in _International Conference on Human System Interaction_ , pp. 356–362, 2010. 

- [63] H. Liu, K. Wu, P. Meusel, N. Seitz, G. Hirzinger, M. Jin, Y. Liu, S. Fan, T. Lan, and Z. Chen, “Multisensory five-finger dexterous hand: The dlr/hit hand ii,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 3692–3697, 2008. 

- [64] W. Friedl, M. Chalon, J. Reinecke, M. Grebenstein, _et al._ , “Fas a flexible antagonistic spring element for a high performance over,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 1366–1372, 2011. 

- [65] S. Fang, Z. Yi, T. Mi, Z. Zhou, C. Ye, W. Shang, T. Xu, and X. Wu, “Tactonet: Tactile ordinal network based on unimodal probability for object hardness classification,” _IEEE Transactions on Automation Science and Engineering (T-ASE)_ , vol. 20, no. 4, pp. 2784–2794, 2022. 

- [66] Y. Liu, Z. Yi, S. Fang, Y. Zhang, F. Wan, Z.-X. Yang, X. Lu, and X. Wu, “Tactclnet: Tactile continual learning network based on generative replay for object hardness recognition,” _IEEE Transactions on Automation Science and Engineering (T-ASE)_ , 2024. 

- [67] Y. Wan, Y. Wang, and C. F. Guo, “Recent progresses on flexible tactile sensors,” _Materials Today Physics_ , vol. 1, pp. 61–73, 2017. 

- [68] H. Zhao, K. O’brien, S. Li, and R. F. Shepherd, “Optoelectronically innervated soft prosthetic hand via stretchable optical waveguides,” _Science Robotics_ , vol. 1, no. 1, 2016. 

- [69] Q. Mao, Z. Liao, J. Yuan, and R. Zhu, “Multimodal tactile sensing fused with vision for dexterous robotic housekeeping,” _Nature Communications (NC)_ , vol. 15, no. 1, p. 6871, 2024. 

- [70] J. Seong, J.-H. Lee, and M.-W. Han, “Soft sensors via conductive textile stitching: Enabling strain, tactile, and volumetric sensing,” _Advanced Materials Technologies_ , vol. 10, no. 6, p. 2401306, 2025. 

- [71] M. Song, Q. Liu, X. Xu, B. Wang, Y. Lu, L. Yang, X. Liu, Y. Wang, M. Li, and D. Wang, “A fabric-based multimodal flexible tactile 

sensor with precise sensing and discrimination capabilities for pressureproximity-magnetic field signals,” _Advanced Functional Materials_ , vol. 35, no. 19, p. 2420445, 2025. 

- [72] B. Rostamian, M. Koolani, P. Abdollahzade, M. Lankarany, E. Falotico, M. Amiri, and N. V. Thakor, “Texture recognition based on multisensory integration of proprioceptive and tactile signals,” _Scientific Reports_ , vol. 12, no. 1, p. 21690, 2022. 

- [73] Y. Ogahara, Y. Kawato, K. Takemura, and T. Maeno, “A wire-driven miniature five fingered robot hand using elastic elements as joints,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , vol. 3, pp. 2672–2677, 2003. 

- [74] K. Gilday, T. G. Thuruthel, and F. Iida, “A vision-based collocated actuation-sensing scheme for a compliant tendon-driven robotic hand.,” in _RoboSoft_ , pp. 760–765, 2020. 

- [75] S. Chen, J. Li, Z. Deng, P. Wang, C. Wei, and X. Cao, “An 18-dof hand integrating force–position multimodal perception using a monocular camera,” _Nature Communications (NC)_ , vol. 16, no. 1, p. 6801, 2025. 

- [76] W. Wang, Y. Jiang, D. Zhong, Z. Zhang, S. Choudhury, J.-C. Lai, H. Gong, S. Niu, X. Yan, Y. Zheng, _et al._ , “Neuromorphic sensorimotor loop embodied by monolithically integrated, low-voltage, soft e-skin,” _Science_ , vol. 380, no. 6646, pp. 735–742, 2023. 

- [77] D.-A. Huang, D. Xu, Y. Zhu, A. Garg, S. Savarese, L. Fei-Fei, and J. C. Niebles, “Continuous relaxation of symbolic planner for oneshot imitation learning,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 2635–2642, 2019. 

- [78] S. Bai, W. Song, J. Chen, Y. Ji, Z. Zhong, J. Yang, H. Zhao, W. Zhou, W. Zhao, Z. Li, _et al._ , “Towards a unified understanding of robot manipulation: A comprehensive survey,” _arXiv preprint arXiv:2510.10903_ , 2025. 

- [79] C. H. Song, J. Wu, C. Washington, B. M. Sadler, W.-L. Chao, and Y. Su, “Llm-planner: Few-shot grounded planning for embodied agents with large language models,” in _IEEE/CVF International Conference on Computer Vision (ICCV)_ , pp. 2998–3009, 2023. 

- [80] H. Liu, P. Meusel, G. Hirzinger, M. Jin, Y. Liu, and Z. Xie, “The modular multisensory dlr-hit-hand: hardware and software architecture,” _IEEE/ASME Transactions on Mechatronics (T-MECH)_ , vol. 13, no. 4, pp. 461–469, 2009. 

- [81] C. Yu and P. Wang, “Dexterous manipulation for multi-fingered robotic hands with reinforcement learning: A review,” _Frontiers in Neurorobotics_ , vol. 16, p. 861825, 2022. 

- [82] I. Popov, N. Heess, T. Lillicrap, R. Hafner, G. Barth-Maron, M. Vecerik, T. Lampe, Y. Tassa, T. Erez, and M. Riedmiller, “Dataefficient deep reinforcement learning for dexterous manipulation,” _arXiv preprint arXiv:1704.03073_ , 2017. 

- [83] G. Khandate, S. Shang, E. T. Chang, T. L. Saidi, Y. Liu, S. M. Dennis, J. Adams, and M. Ciocarlie, “Sampling-based exploration for reinforcement learning of dexterous manipulation,” _arXiv preprint arXiv:2303.03486_ , 2023. 

- [84] A. Gupta, J. Yu, T. Z. Zhao, V. Kumar, A. Rovinsky, K. Xu, T. Devlin, and S. Levine, “Reset-free reinforcement learning via multi-task learning: Learning dexterous manipulation behaviors without human intervention,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 6664–6671, 2021. 

- [85] K. Xu, Z. Hu, R. Doshi, A. Rovinsky, V. Kumar, A. Gupta, and S. Levine, “Dexterous manipulation from images: Autonomous realworld rl via substep guidance,” _arXiv preprint arXiv:2212.09902_ , 2022. 

- [86] Y. Qin, B. Huang, Z.-H. Yin, H. Su, and X. Wang, “Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation,” in _Conference on Robot Learning (CoRL)_ , pp. 594–605, 2023. 

- [87] A. Kannan, K. Shaw, S. Bahl, P. Mannam, and D. Pathak, “Deft: Dexterous fine-tuning for real-world hand policies,” _arXiv preprint arXiv:2310.19797_ , 2023. 

- [88] Y. Ze, Y. Liu, R. Shi, J. Qin, Z. Yuan, J. Wang, and H. Xu, “H-index: Visual reinforcement learning with hand-informed representations for dexterous manipulation,” _Advances in Neural Information Processing Systems (NeurIPS)_ , vol. 36, pp. 74394–74409, 2023. 

- [89] Y. Yuan, H. Che, Y. Qin, B. Huang, Z.-H. Yin, K.-W. Lee, Y. Wu, S.C. Lim, and X. Wang, “Robot synesthesia: In-hand manipulation with visuotactile sensing,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 6558–6565, 2024. 

- [90] Y. Chen, Y. Geng, F. Zhong, J. Ji, J. Jiang, Z. Lu, H. Dong, and Y. Yang, “Bi-dexhands: Towards human-level bimanual dexterous manipulation,” _IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)_ , vol. 46, no. 5, pp. 2804–2818, 2023. 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

19 

- [91] H. Zhou, Y. You, and S. Wang, “Dydexhandover: Human-like bimanual dynamic dexterous handover using rgb-only perception,” _arXiv preprint arXiv:2509.17350_ , 2025. 

- [92] A. Wagenmaker, M. Nakamoto, Y. Zhang, S. Park, W. Yagoub, A. Nagabandi, A. Gupta, and S. Levine, “Steering your diffusion policy with latent space reinforcement learning,” _arXiv preprint arXiv:2506.15799_ , 2025. 

- [93] Y. Wu, Z. Chen, F. Wu, L. Chen, L. Zhang, Z. Bing, A. Swikir, S. Haddadin, and A. Knoll, “Tacdiffusion: Force-domain diffusion policy for precise tactile manipulation,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 11831–11837, 2025. 

- [94] Z. Liang, Y. Mu, Y. Wang, T. Chen, W. Shao, W. Zhan, M. Tomizuka, P. Luo, and M. Ding, “Dexhanddiff: Interaction-aware diffusion planning for adaptive dexterous manipulation,” in _Proceedings of the Computer Vision and Pattern Recognition Conference_ , pp. 1745–1755, 2025. 

- [95] J. Zhang, Y. Zhang, L. An, M. Li, H. Zhang, Z. Hu, and Y. Liu, “Manidext: Hand-object manipulation synthesis via continuous correspondence embeddings and residual-guided diffusion,” _IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)_ , 2025. 

- [96] Y. Guo, Y. Hu, J. Zhang, Y.-J. Wang, X. Chen, C. Lu, and J. Chen, “Prediction with action: Visual policy learning via joint denoising process,” _Advances in Neural Information Processing Systems (NeurIPS)_ , vol. 37, pp. 112386–112410, 2024. 

- [97] A. Sivakumar, K. Shaw, and D. Pathak, “Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube,” _arXiv preprint arXiv:2202.10448_ , 2022. 

- [98] Y.-H. Wu, J. Wang, and X. Wang, “Learning generalizable dexterous manipulation from human grasp affordance,” 2022. 

- [99] S. P. Arunachalam, S. Silwal, B. Evans, and L. Pinto, “Dexterous imitation made easy: A learning-based framework for efficient dexterous manipulation,” _arXiv preprint arXiv:2203.13251_ , 2022. 

- [100] Y. Han, M. Xie, Y. Zhao, and H. Ravichandar, “On the utility of koopman operator theory in learning dexterous manipulation skills,” in _Conference on Robot Learning (CoRL)_ , pp. 106–126, 2023. 

- [101] C. Chen, Z. Yu, H. Choi, M. Cutkosky, and J. Bohg, “Dexforce: Extracting force-informed actions from kinesthetic demonstrations for dexterous manipulation,” _IEEE Robotics and Automation Letters (RAL)_ , vol. 10, no. 6, pp. 6416–6423, 2025. 

- [102] M. Yu, Y. Jiang, C. Chen, Y. Jia, and X. Li, “Robotic in-hand manipulation for large-range precise object movement: The rgmc champion solution,” _IEEE Robotics and Automation Letters (RA-L)_ , 2025. 

- [103] I. Guzey, Y. Dai, G. Savva, R. Bhirangi, and L. Pinto, “Bridging the human to robot dexterity gap through object-oriented rewards,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 3344–3351, 2025. 

- [104] Z. Chen, S. Chen, E. Arlaud, I. Laptev, and C. Schmid, “Vividex: Learning vision-based dexterous manipulation from human videos,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 3336–3343, 2025. 

- [105] C. Chen, P. Culbertson, M. Lepert, M. Schwager, and J. Bohg, “Trajectotree: Trajectory optimization meets tree search for planning multicontact dexterous manipulation,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 8262–8268, 2021. 

- [106] Y. Luo, T. Ji, F. Sun, Q. Sima, H. Liu, M. Jing, and J. Zhang, “Robust tube-based mpc with smooth computation for dexterous robot manipulation,” _Science China Information Sciences_ , vol. 67, no. 11, p. 212207, 2024. 

- [107] Z. Xu and Y. She, “Letac-mpc: Learning model predictive control for tactile-reactive grasping,” _IEEE Transactions on Robotics (T-RO)_ , 2024. 

- [108] T. G. W. Lum, M. Matak, V. Makoviychuk, A. Handa, A. Allshire, T. Hermans, N. D. Ratliff, and K. Van Wyk, “Dextrah-g: Pixels-toaction dexterous arm-hand grasping with geometric fabrics,” _arXiv preprint arXiv:2407.02274_ , 2024. 

- [109] M. J. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair, R. Rafailov, E. Foster, G. Lam, P. Sanketi, _et al._ , “Openvla: An open-source vision-language-action model,” _arXiv preprint arXiv:2406.09246_ , 2024. 

- [110] O. M. Team, D. Ghosh, H. Walke, K. Pertsch, K. Black, O. Mees, S. Dasari, J. Hejna, T. Kreiman, C. Xu, _et al._ , “Octo: An open-source generalist robot policy,” _arXiv preprint arXiv:2405.12213_ , 2024. 

- [111] H. Luo, Y. Feng, W. Zhang, S. Zheng, Y. Wang, H. Yuan, J. Liu, C. Xu, Q. Jin, and Z. Lu, “Being-h0: vision-language-action pretraining from large-scale human videos,” _arXiv preprint arXiv:2507.15597_ , 2025. 

- [112] H. Zhen, X. Qiu, P. Chen, J. Yang, X. Yan, Y. Du, Y. Hong, and C. Gan, “3d-vla: A 3d vision-language-action generative world model,” _arXiv preprint arXiv:2403.09631_ , 2024. 

- [113] H. Liu, S. Guo, P. Mai, J. Cao, H. Li, and J. Ma, “Robodexvlm: Visual language model-enabled task planning and motion control for dexterous robot manipulation,” _arXiv preprint arXiv:2503.01616_ , 2025. 

- [114] X. Chen, H. Wei, P. Zhang, C. Zhang, K. Wang, Y. Guo, R. Yang, Y. Wang, X. Xiao, L. Zhao, _et al._ , “Villa-x: enhancing latent action modeling in vision-language-action models,” _arXiv preprint arXiv:2507.23682_ , 2025. 

- [115] J. Wen, Y. Zhu, J. Li, Z. Tang, C. Shen, and F. Feng, “Dexvla: Visionlanguage model with plug-in diffusion expert for general robot control,” _arXiv preprint arXiv:2502.05855_ , 2025. 

- [116] Z. Cheng, Y. Zhang, W. Zhang, H. Li, K. Wang, L. Song, and H. Zhang, “Omnivtla: Vision-tactile-language-action model with semantic-aligned tactile sensing,” _arXiv preprint arXiv:2508.08706_ , 2025. 

- [117] V. Caggiano, S. Dasari, and V. Kumar, “Myodex: a generalizable prior for dexterous manipulation,” in _International Conference on Machine Learning (ICML)_ , pp. 3327–3346, 2023. 

- [118] A. Bicchi and V. Kumar, “Robotic grasping and contact: A review,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , vol. 1, pp. 348–353, 2000. 

- [119] W. Zhao, J. Dong, R. Zhang, K. Li, Q. Zhao, and K. Huang, “Telecatch: Adaptive teleoperation for dexterous dynamic 3d object catching,” _arXiv preprint arXiv:2603.28427_ , 2026. 

- [120] Z. Li, J. Liu, Z. Li, Z. Dong, T. Teng, Y. Ou, D. Caldwell, and F. Chen, “Language-guided dexterous functional grasping by llm generated grasp functionality and synergy for humanoid manipulation,” _IEEE Transactions on Automation Science and Engineering (T-ASE)_ , vol. 22, pp. 10506–10519, 2025. 

- [121] J. Huber, F. H´el´enon, H. Watrelot, F. B. Amar, and S. Doncieux, “Domain randomization for sim2real transfer of automatically generated grasping datasets,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 4112–4118, 2024. 

- [122] Y. Liu, Y. Yang, Y. Wang, X. Wu, J. Wang, Y. Yao, S. Schwertfeger, S. Yang, W. Wang, J. Yu, _et al._ , “Realdex: Towards human-like grasping for robotic dexterous hand,” _arXiv preprint arXiv:2402.13853_ , 2024. 

- [123] X. Song, Y. Li, Y. Zhang, Y. Liu, and L. Jiang, “An overview of learning-based dexterous grasping: recent advances and future directions,” _Artificial Intelligence Review_ , vol. 58, no. 10, pp. 1–44, 2025. 

- [124] T. Li, Y. Yan, C. Yu, J. An, Y. Wang, and G. Chen, “A comprehensive review of robot intelligent grasping based on tactile perception,” _Robotics and Computer-Integrated Manufacturing (RCIM)_ , vol. 90, p. 102792, 2024. 

- [125] A. Billard and D. Kragic, “Trends and challenges in robot manipulation,” _Science_ , vol. 364, no. 6446, p. eaat8414, 2019. 

- [126] Q. Wang, F. R. Sanchez, R. McCarthy, D. C. Bulens, K. McGuinness, N. O’Connor, M. W¨uthrich, F. Widmaier, S. Bauer, and S. J. Redmond, “Dexterous robotic manipulation using deep reinforcement learning and knowledge transfer for complex sparse reward-based tasks,” _Expert Systems_ , vol. 40, no. 6, p. e13205, 2023. 

- [127] H. Yuan, B. Zhou, Y. Fu, and Z. Lu, “Cross-embodiment dexterous grasping with reinforcement learning,” _arXiv preprint arXiv:2410.02479_ , 2024. 

- [128] J. Luo, Z. Hu, C. Xu, Y. L. Tan, J. Berg, A. Sharma, S. Schaal, C. Finn, A. Gupta, and S. Levine, “Serl: A software suite for sample-efficient robotic reinforcement learning,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 16961–16969, 2024. 

- [129] G. Schoettler, A. Nair, J. Luo, S. Bahl, J. A. Ojea, E. Solowjow, and S. Levine, “Deep reinforcement learning for industrial insertion tasks with visual inputs and natural rewards,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 5548–5555, 2020. 

- [130] B. Li, S. Qiu, J. Bai, H. Wang, B. Wang, Z. Zhang, L. Li, and X. Wang, “Grasp with push policy for multi-finger dexterity hand based on deep reinforcement learning,” _Applied Soft Computing_ , vol. 167, p. 112365, 2024. 

- [131] Z. Hu, Y. Zheng, and J. Pan, “Grasping living objects with adversarial behaviors using inverse reinforcement learning,” _IEEE Transactions on Robotics (T-RO)_ , vol. 39, no. 2, pp. 1151–1163, 2023. 

- [132] Y.-H. Wu, J. Wang, and X. Wang, “Learning generalizable dexterous manipulation from human grasp affordance,” in _Conference on Robot Learning (CoRL)_ , pp. 618–629, 2023. 

- [133] Z. Weng, H. Lu, D. Kragic, and J. Lundell, “Dexdiffuser: Generating dexterous grasps with diffusion models,” _IEEE Robotics and Automation Letters (RA-L)_ , 2024. 

- [134] F. Zhao, D. Tsetserukou, and Q. Liu, “Graingrasp: Dexterous grasp generation with fine-grained contact guidance,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 6470–6476, 2024. 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

20 

- [135] Y. Wang, G. Yin, B. Huang, T. Kelestemur, J. Wang, and Y. Li, “Gendp: 3d semantic fields for category-level generalizable diffusion policy,” in _Conference on Robot Learning (CoRL)_ , vol. 2, 2024. 

- [136] S. Chen, J. Bohg, and C. K. Liu, “Springgrasp: Synthesizing compliant, dexterous grasps under shape uncertainty,” _arXiv preprint arXiv:2404.13532_ , 2024. 

- [137] C. Pan, K. Junge, and J. Hughes, “Vision-language-action model and diffusion policy switching enables dexterous control of an anthropomorphic hand,” _arXiv preprint arXiv:2410.14022_ , 2024. 

- [138] M. Makarova, Q. Liu, and D. Tsetserukou, “Diffusionrl: Efficient training of diffusion policies for robotic grasping using rl-adapted largescale datasets,” _arXiv preprint arXiv:2505.18876_ , 2025. 

- [139] Y. Qin, H. Su, and X. Wang, “From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation,” _IEEE Robotics and Automation Letters (RA-L)_ , vol. 7, no. 4, pp. 10873–10881, 2022. 

- [140] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang, “Dexmv: Imitation learning for dexterous manipulation from human videos,” in _European Conference on Computer Vision (ECCV)_ , pp. 570–587, 2022. 

- [141] Y. Liu, W. C. Shin, Y. Han, Z. Chen, H. Ravichandar, and D. Xu, “Immimic: Cross-domain imitation from human videos via mapping and interpolation,” _arXiv preprint arXiv:2509.10952_ , 2025. 

- [142] Y. Li, C. Guo, J. Ren, B. Chen, C. Cheng, H. Zhang, and H. Lu, “Softgrasp: Adaptive grasping for dexterous hand based on multimodal imitation learning,” _Biomimetic Intelligence and Robotics_ , vol. 5, no. 2, p. 100217, 2025. 

- [143] P. Lin, Y. Huang, W. Li, J. Ma, C. Xiao, and Z. Jiao, “Pp-tac: Paper picking using tactile feedback in dexterous robotic hands,” _arXiv preprint arXiv:2504.16649_ , 2025. 

- [144] Q. Wang, C. Deng, T. G. W. Lum, Y. Chen, Y. Yang, J. Bohg, Y. Zhu, and L. Guibas, “Neural attention field: Emerging point relevance in 3d scenes for one-shot dexterous grasping,” _arXiv preprint arXiv:2410.23039_ , 2024. 

- [145] J. Li, Y. Lv, X. Lin, J. Hang, X. Li, and Y. Sun, “A single-demonstration guided manipulation learning with dexterous hand,” _Engineering Applications of Artificial Intelligence (EAAI)_ , vol. 159, p. 111606, 2025. 

- [146] W. Wei, P. Wang, and S. Wang, “Generalized anthropomorphic functional grasping with minimal demonstrations,” _arXiv preprint arXiv:2303.17808_ , 2023. 

- [147] J. Wang, Y. Qin, K. Kuang, Y. Korkmaz, A. Gurumoorthy, H. Su, and X. Wang, “Cyberdemo: Augmenting simulated human demonstration for real-world dexterous manipulation,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 17952–17963, 2024. 

- [148] Z. Wei, Z. Xu, J. Guo, Y. Hou, C. Gao, Z. Cai, J. Luo, and L. Shao, “D (r, o) grasp: A unified representation of robot and object interaction for cross-embodiment dexterous grasping,” _arXiv preprint arXiv:2410.01702_ , 2024. 

- [149] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, _et al._ , “Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 4737–4746, 2023. 

- [150] W. Wan, H. Geng, Y. Liu, Z. Shan, Y. Yang, L. Yi, and H. Wang, “Unidexgrasp++: Improving dexterous grasping policy learning via geometry-aware curriculum and iterative generalist-specialist learning,” in _IEEE/CVF International Conference on Computer Vision (ICCV)_ , pp. 3891–3902, 2023. 

- [151] K. Wang, B. Lu, Z. Cheng, H. Zhang, and L. Song, “D3grasp: Diverse and deformable dexterous grasping for general objects,” _arXiv preprint arXiv:2509.19892_ , 2025. 

- [152] S. Christen, M. Kocabas, E. Aksan, J. Hwangbo, J. Song, and O. Hilliges, “D-grasp: Physically plausible dynamic grasp synthesis for hand-object interactions,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 20577–20586, 2022. 

- [153] W. Wang, F. Wei, L. Zhou, X. Chen, L. Luo, X. Yi, Y. Zhang, Y. Liang, C. Xu, Y. Lu, _et al._ , “Unigrasptransformer: Simplified policy distillation for scalable dexterous robotic grasping,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 12199–12208, 2025. 

- [154] Y. Zhong, X. Huang, R. Li, C. Zhang, Z. Chen, T. Guan, F. Zeng, K. N. Lui, Y. Ye, Y. Liang, _et al._ , “Dexgraspvla: A vision-languageaction framework towards general dexterous grasping,” _arXiv preprint arXiv:2502.20900_ , 2025. 

- [155] S. Deng, M. Yan, S. Wei, H. Ma, Y. Yang, J. Chen, Z. Zhang, T. Yang, X. Zhang, W. Zhang, _et al._ , “Graspvla: a grasping foundation 

model pre-trained on billion-scale synthetic action data,” _arXiv preprint arXiv:2505.03233_ , 2025. 

- [156] H. Xiao, X. Liu, H. Zhao, J. Liu, and K. Xu, “Designing pinpression gripper and learning its dexterous grasping with online in-hand adjustment,” _ACM Transactions on Graphics (TOG)_ , vol. 44, no. 4, pp. 1–17, 2025. 

- [157] R. Singh, A. Allshire, A. Handa, N. Ratliff, and K. Van Wyk, “Dextrahrgb: Visuomotor policies to grasp anything with dexterous hands,” _arXiv preprint arXiv:2412.01791_ , 2024. 

- [158] W. Zhou and D. Held, “Learning to grasp the ungraspable with emergent extrinsic dexterity,” in _Conference on Robot Learning (CoRL)_ , pp. 150–160, PMLR, 2023. 

- [159] A. Nagabandi, K. Konolige, S. Levine, and V. Kumar, “Deep dynamics models for learning dexterous manipulation,” in _Conference on Robot Learning (CoRL)_ , pp. 1101–1112, PMLR, 2020. 

- [160] W. Xu, Y. Zhao, W. Guo, and X. Sheng, “Hierarchical reinforcement learning for articulated tool manipulation with multifingered hand,” _arXiv preprint arXiv:2507.06822_ , 2025. 

- [161] S. Atar, D. Huang, F. Richter, and M. Yip, “In-hand manipulation of articulated tools with dexterous robot hands with sim-to-real transfer,” _arXiv preprint arXiv:2509.23075_ , 2025. 

- [162] Z. Liu, S. Tian, M. Guo, C. K. Liu, and J. Wu, “Learning to design and use tools for robotic manipulation,” _arXiv preprint arXiv:2311.00754_ , 2023. 

- [163] C. Tang, A. Xiao, Y. Deng, T. Hu, W. Dong, H. Zhang, D. Hsu, and H. Zhang, “Mimicfunc: Imitating tool manipulation from a single human video via functional correspondence,” _arXiv preprint arXiv:2508.13534_ , 2025. 

- [164] B. Zitkovich, T. Yu, S. Xu, P. Xu, T. Xiao, F. Xia, J. Wu, P. Wohlhart, S. Welker, A. Wahid, _et al._ , “Rt-2: Vision-language-action models transfer web knowledge to robotic control,” in _Conference on Robot Learning (CoRL)_ , pp. 2165–2183, 2023. 

- [165] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, L. Ke, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, L. X. Shi, J. Tanner, Q. Vuong, A. Walling, H. Wang, and U. Zhilinsky, “ _π_ 0: A vision-language-action flow model for general robot control,” _arXiv preprint arXiv:2410.24164_ , 2023. 

- [166] Z.-H. Yin, C. Wang, L. Pineda, F. Hogan, K. Bodduluri, A. Sharma, P. Lancaster, I. Prasad, M. Kalakrishnan, J. Malik, _et al._ , “Dexteritygen: Foundation controller for unprecedented dexterity,” _Robotics: Science and Systems (RSS)_ , 2025. 

- [167] K. Fang, Y. Zhu, A. Garg, A. Kurenkov, V. Mehta, L. Fei-Fei, and S. Savarese, “Learning task-oriented grasping for tool manipulation from simulated self-supervision,” _The International Journal of Robotics Research_ , vol. 39, no. 2-3, pp. 202–216, 2020. 

- [168] J. Luo, C. Xu, J. Wu, and S. Levine, “Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning,” _Science Robotics_ , vol. 10, no. 105, 2025. 

- [169] T. Lin, K. Sachdev, L. Fan, J. Malik, and Y. Zhu, “Sim-to-real reinforcement learning for vision-based dexterous manipulation on humanoids,” _arXiv preprint arXiv:2502.20396_ , 2025. 

- [170] S. Christen, W. Yang, C. P´erez-D’Arpino, O. Hilliges, D. Fox, and Y.-W. Chao, “Learning human-to-robot handovers from point clouds,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 9654–9664, 2023. 

- [171] S. Bahl, R. Mendonca, L. Chen, U. Jain, and D. Pathak, “Affordances from human videos as a versatile representation for robotics,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 13778–13790, 2023. 

- [172] A. Jawaid and Y. Xiang, “Openego: A large-scale multimodal egocentric dataset for dexterous manipulation,” _arXiv preprint arXiv:2509.05513_ , 2025. 

- [173] T. Lin, Y. Zhang, Q. Li, H. Qi, B. Yi, S. Levine, and J. Malik, “Learning visuotactile skills with two multifingered hands,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 5637–5643, 2025. 

- [174] Y. Chen, T. Wu, S. Wang, X. Feng, J. Jiang, Z. Lu, S. McAleer, H. Dong, S.-C. Zhu, and Y. Yang, “Towards human-level bimanual dexterous manipulation with reinforcement learning,” _Advances in Neural Information Processing Systems (NeurIPS)_ , vol. 35, pp. 5150– 5163, 2022. 

- [175] X. Ma, S. Patidar, I. Haughton, and S. James, “Hierarchical diffusion policy for kinematics-aware multi-task robotic manipulation,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 18081–18090, 2024. 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

21 

- [176] G. Franzese, L. de Souza Rosa, T. Verburg, L. Peternel, and J. Kober, “Interactive imitation learning of bimanual movement primitives,” _IEEE/ASME Transactions on Mechatronics (T-MECH)_ , 2023. 

- [177] K. Li, P. Li, T. Liu, Y. Li, and S. Huang, “Maniptrans: Efficient dexterous bimanual manipulation transfer via residual learning,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 6991–7003, 2025. 

- [178] Y. Liu, H. Yang, X. Si, L. Liu, Z. Li, Y. Zhang, Y. Liu, and L. Yi, “Taco: Benchmarking generalizable bimanual tool-action-object understanding,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 21740–21751, 2024. 

- [179] B. Zhou, H. Yuan, Y. Fu, and Z. Lu, “Learning diverse bimanual dexterous manipulation skills from human demonstrations,” _arXiv preprint arXiv:2410.02477_ , 2024. 

- [180] C. Chi, Z. Xu, C. Pan, E. Cousineau, B. Burchfiel, S. Feng, R. Tedrake, and S. Song, “Universal manipulation interface: In-the-wild robot teaching without in-the-wild robots,” _arXiv preprint arXiv:2402.10329_ , 2024. 

- [181] Z. Jiang, Y. Xie, K. Lin, Z. Xu, W. Wan, A. Mandlekar, L. J. Fan, and Y. Zhu, “Dexmimicgen: Automated data generation for bimanual dexterous manipulation via imitation learning,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 16923–16930, 2025. 

- [182] K. F. Gbagbe, M. A. Cabrera, A. Alabbas, O. Alyunes, A. Lykov, and D. Tsetserukou, “Bi-vla: Vision-language-action model-based system for bimanual robotic dexterous manipulations,” in _IEEE International Conference on Systems, Man, and Cybernetics (SMC)_ , pp. 2864–2869, 2024. 

- [183] S. Liu, L. Wu, B. Li, H. Tan, H. Chen, Z. Wang, K. Xu, H. Su, and J. Zhu, “Rdt-1b: a diffusion foundation model for bimanual manipulation,” _arXiv preprint arXiv:2410.07864_ , 2024. 

- [184] M. H. Khan, S. Asfaw, D. Iarchuk, M. A. Cabrera, L. Moreno, I. Tokmurziyev, and D. Tsetserukou, “Shake-vla: Vision-languageaction model-based system for bimanual robotic manipulations and liquid mixing,” in _ACM/IEEE International Conference on HumanRobot Interaction (HRI)_ , pp. 1393–1397, 2025. 

- [185] B. Huang, Y. Wang, X. Yang, Y. Luo, and Y. Li, “3d-vitac: Learning fine-grained manipulation with visuo-tactile sensing,” _arXiv preprint arXiv:2410.24091_ , 2024. 

- [186] Z. Fan, O. Taheri, D. Tzionas, M. Kocabas, M. Kaufmann, M. J. Black, and O. Hilliges, “Arctic: A dataset for dexterous bimanual handobject manipulation,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 12943–12954, 2023. 

- [187] K. Wu, C. Hou, J. Liu, Z. Che, X. Ju, Z. Yang, M. Li, Y. Zhao, Z. Xu, G. Yang, _et al._ , “Robomind: Benchmark on multi-embodiment intelligence normative data for robot manipulation,” _arXiv preprint arXiv:2412.13877_ , 2024. 

- [188] C. Bao, H. Xu, Y. Qin, and X. Wang, “Dexart: Benchmarking generalizable dexterous manipulation with articulated objects,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 21190–21200, 2023. 

- [189] C. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and C. K. Liu, “Dexcap: Scalable and portable mocap data collection system for dexterous manipulation,” _arXiv preprint arXiv:2403.07788_ , 2024. 

- [190] J. Hang, X. Lin, T. Zhu, X. Li, R. Wu, X. Ma, and Y. Sun, “Dexfuncgrasp: A robotic dexterous functional grasp dataset constructed from a cost-effective real-simulation annotation system.,” in _AAAI Conference on Artificial Intelligence (AAAI)_ , pp. 10306–10313, 2024. 

- [191] H.-S. Fang, H. Fang, Z. Tang, J. Liu, C. Wang, J. Wang, H. Zhu, and C. Lu, “Rh20t: A comprehensive robotic dataset for learning diverse skills in one-shot,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 653–660, 2024. 

- [192] Y. Zhong, Q. Jiang, J. Yu, and Y. Ma, “Dexgrasp anything: Towards universal robotic dexterous grasping with physics awareness,” _arXiv preprint arXiv:2503.08257_ , 2025. 

- [193] J. Chen, Y. Ke, and H. Wang, “Bodex: Scalable and efficient robotic dexterous grasp synthesis using bilevel optimization,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 01–08, 2025. 

- [194] Z. Wu, R. A. Potamias, X. Zhang, Z. Zhang, J. Deng, and S. Luo, “Cedex: Cross-embodiment dexterous grasp generation at scale from human-like contact representations,” _arXiv preprint arXiv:2509.24661_ , 2025. 

- [195] J. Ye, K. Wang, C. Yuan, R. Yang, Y. Li, J. Zhu, Y. Qin, X. Zou, and X. Wang, “Dex1b: Learning with 1b demonstrations for dexterous manipulation,” in _Robotics: Science and Systems (RSS)_ , 2025. 

- [196] J. Zhang, W. Xu, Z. Yu, P. Xie, T. Tang, and C. Lu, “Dextog: Learning task-oriented dexterous grasp with language condition,” _IEEE Robotics and Automation Letters (RA-L)_ , vol. 10, no. 2, 2025. 

- [197] Q. Liu, Y. Cui, Z. Sun, G. Li, J. Chen, and Q. Ye, “Vtdexmanip: A dataset and benchmark for visual-tactile pretraining and dexterous manipulation with reinforcement learning,” in _International Conference on Learning Representations (ICLR)_ , 2025. 

- [198] E. Todorov, T. Erez, and Y. Tassa, “Mujoco: A physics engine for model-based control,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 5026–5033, 2012. 

- [199] G. Garcia-Hernando, S. Yuan, S. Baek, and T.-K. Kim, “First-person hand action benchmark with rgb-d videos and 3d hand pose annotations,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 409–419, 2018. 

- [200] S. Brahmbhatt, C. Tang, C. D. Twigg, C. C. Kemp, and J. Hays, “Contactpose: A dataset of grasps with object contact and hand pose,” in _European Conference on Computer Vision (ECCV)_ , pp. 361–378, 2020. 

- [201] Y.-W. Chao, W. Yang, Y. Xiang, P. Molchanov, A. Handa, J. Tremblay, Y. S. Narang, K. Van Wyk, U. Iqbal, S. Birchfield, _et al._ , “Dexycb: A benchmark for capturing hand grasping of objects,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 9044–9053, 2021. 

- [202] L. Yang, K. Li, X. Zhan, F. Wu, A. Xu, L. Liu, and C. Lu, “Oakink: A large-scale knowledge repository for understanding hand-object interaction,” in _IEEE/CVF conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 20953–20962, 2022. 

- [203] A. O’Neill, A. Rehman, A. Maddukuri, A. Gupta, A. Padalkar, A. Lee, A. Pooley, A. Gupta, A. Mandlekar, A. Jain, _et al._ , “Open x-embodiment: Robotic learning datasets and rt-x models: Open x- embodiment collaboration 0,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 6892–6903, 2024. 

- [204] P. Li, T. Liu, Y. Li, Y. Zhu, Y. Yang, and S. Huang, “Gendexgrasp: Generalizable dexterous grasping.” urlhttps://arxiv.org/abs/2210.00722, 2022. 

- [205] R. Wang, J. Zhang, J. Chen, Y. Xu, P. Li, T. Liu, and H. Wang, “Dexgraspnet: A large-scale robotic dexterous grasp dataset for general objects based on simulation,” _arXiv preprint arXiv:2210.02697_ , 2022. 

- [206] P. Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, M. Y. Galliker, D. Ghosh, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, L. Ke, D. LeBlanc, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, A. Z. Ren, L. X. Shi, L. Smith, J. T. Springenberg, K. Stachowicz, J. Tanner, Q. Vuong, H. R. Walke, A. Walling, H. Wang, L. Yu, and U. Zhilinsky, “ _pi_ 0 _._ 5: a vision-language-action model with open-world generalization,” _Conference on Robot Learning (CoRL)_ , 2025. 

- [207] F. Bai, Y. Li, J. Chu, T. Chou, R. Zhu, Y. Wen, Y. Yang, and Y. Chen, “Retrieval dexterity: Efficient object retrieval in clutters with dexterous hand,” in _arXiv preprint arXiv:2502.18423_ , 2025. 

- [208] K. Fang, F. Liu, P. Abbeel, and S. Levine, “Moka: Open-world robotic manipulation through mark-based visual prompting,” _Robotics: Science and Systems (RSS)_ , 2024. 

- [209] W. Zhao, C. Jiang, C. Zhang, J. Sun, Y. Yan, R. Zhang, and K. Huang, “3d-cdrgp: Towards cross-device robotic grasping policy in 3d open world,” _arXiv preprint arXiv:2411.18133_ , 2024. 

- [210] Y. Li, Y. Deng, J. Zhang, J. Jang, M. Memmel, C. R. Garrett, F. Ramos, D. Fox, AnqiLi, AbhishekGupta, A. Goyal, and Nvidia, “Hamster: Hierarchical action models for open-world robot manipulation,” _International Conference on Learning Representations (ICLR)_ , 2025. 

- [211] P. Rothemund, N. Kellaris, S. K. Mitchell, E. Acome, and C. Keplinger, “Hasel artificial muscles for a new generation of lifelike robots—recent progress and future opportunities,” _Advanced Materials_ , vol. 33, no. 19, p. 2003375, 2021. 

- [212] S. H. Vemprala, R. Bonatti, A. Bucker, and A. Kapoor, “Chatgpt for robotics: Design principles and model abilities,” _IEEE Access_ , vol. 12, pp. 55682–55696, 2024. 

- [213] Y. Zhang, D. Zeng, J. Luo, Z. Xu, and I. King, “A survey of trustworthy federated learning with perspectives on security, robustness and privacy,” in _ACM web conference (WWW)_ , pp. 1167–1176, 2023. 

- [214] Y. Zhang, D. Zeng, J. Luo, X. Fu, G. Chen, Z. Xu, and I. King, “A survey of trustworthy federated learning: Issues, solutions, and challenges,” _ACM Transactions on Intelligent Systems and Technology (TIST)_ , vol. 15, no. 6, pp. 1–47, 2024. 

- [215] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, _et al._ , “Rt-1: 

JOURNAL OF L<sup>A</sup> TEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 

22 

Robotics transformer for real-world control at scale,” _arXiv preprint arXiv:2212.06817_ , 2022. 

- [216] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, _et al._ , “Learning dexterous in-hand manipulation,” _The International Journal of Robotics Research_ , vol. 39, no. 1, pp. 3–20, 2020. 

- [217] Q. Zhao, R. Roy, C. Spurlock, K. Lister, and L. Wang, “A high-fidelity simulation framework for grasping stability analysis in human casualty manipulation,” _IEEE Transactions on Medical Robotics and Bionics (TMRB)_ , 2025. 

- [218] P. Hao, S. Cui, J. Wei, T. Lu, Y. Cai, and S. Wang, “Learn-gen-plan: Bridging the gap between vision language models and real-world longhorizon dexterous manipulations,” _IEEE Transactions on Automation Science and Engineering (T-ASE)_ , 2025. 

