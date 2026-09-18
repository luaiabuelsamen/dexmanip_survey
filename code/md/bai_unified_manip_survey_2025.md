# bai_unified_manip_survey_2025

source: https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation


commit: b208a6634908074a5e17f883024385889df836e0


## README

# Awesome-Robotics-Manipulation

## ✨ About

This repository curates research papers on robot manipulation, featuring a smaller collection of non-learning control methods and a larger body of learning-based approaches.

This repository will be continuously updated, and we warmly welcome contributions from the community. If you have papers, projects, or resources that are not yet included, please feel free to submit them via a pull request, open an issue for discussion or [email](baishuanghao@stu.xjtu.edu.cn) us to add papers!


## 📚 Related Surveys

- **Comprehensive Survey:**  
  [Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey](https://arxiv.org/abs/2510.10903)

- **IEEE Transactions on Robotics (T-RO) Version:**  
  Main paper: [Embodied Robot Manipulation in the Era of Foundation Models: Planning and Learning Perspectives](https://arxiv.org/abs/2512.22983)  
  Supplementary material: [Appendix](documents/T-RO/appendix.pdf)


## 📢 News

- **[2026/08]** 🎉 Our paper [Embodied Robot Manipulation in the Era of Foundation Models: Planning and Learning Perspectives](https://arxiv.org/abs/2512.22983) has been accepted by IEEE Transactions on Robotics (T-RO)!
- **[2026/08]** Released Version 2 of [Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey](https://arxiv.org/abs/2510.10903). The detailed revision log is available in [arxiv_update_log_v2.md](documents/arxiv_update_log_v2.md).
- **[2026/04]** Updated venue information for most papers and removed a few references without publicly available code. Refined the taxonomy under *High-Level Planning*, separated *Video-Based Planners* into an independent subsection, and are revising the *Motion Planning* section. Added coverage of *Aerial Manipulation* and *Underwater Manipulation*, and improved categories such as *Human Teleoperation* under *Data Collection*.
- **[2025/10]** Our paper [Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey](https://arxiv.org/abs/2510.10903) is now available!

<details>
<summary><i>Earlier Updates</i></summary>

- **[2025/08]** Major revision of the classification system with a more refined taxonomy; substantial improvements across all sections.
- **[2025/07]** Expanded coverage of **Dexterous**, **Soft Robotic**, **Mobile**, **Quadrupedal**, and **Humanoid Manipulation**; refined the categorization and content for **Awesome Simulators, Benchmarks, and Datasets**; added non-learning-based control methods.
- **[2025/06]** Introduced new sections on **Grasp in Cluttered Scenes**, **Quadrupedal and Humanoid Manipulation**, and **Learning from Human Demonstrations**. Also improved the classification of the **Applications** section and added a subsection on **Embodied QA Datasets**.
- **[2025/02]** Added a new section on **Bimanual Grasp**.
- **[2024/12]** Introduced coverage of **Dexterous Grasp**.
- **[2024/10]** Repository is now public!

</details>



## 📝 Summary of Survey
<details>

<summary>Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey</summary>

<div style="height:5px;"></div>

This survey presents a unified perspective on robot manipulation by organizing existing methods according to the relationship between **high-level planning** and **low-level action modeling**. We provide a systematic taxonomy that connects different forms of task-level reasoning, structured representations, and executable action generation.

<div align="center">
  <img src="imgs/summary.png" alt="summary" 
       style="image-rendering: auto; max-width: 100%; height: auto;">
</div>

<b>Summary.</b> The survey first reviews robot manipulation from multiple aspects, including task types, robot embodiments, simulators and benchmarks, high-level planning, learning-based action modeling, applications, and key challenges. This overview provides a comprehensive map of recent advances and highlights the connections among different research directions.

<div align="center">
  <img src="imgs/basic.png" alt="basic" width="50%"
       style="image-rendering: auto; max-width: 65%; height: auto;">
</div>

At the algorithmic level, we formulate robot manipulation as a two-stage process consisting of **high-level planning** and **low-level action modeling**. High-level planning focuses on generating structured intermediate representations, such as task plans, geometric constraints, affordances, code, video predictions, and 3D representations. These structured outputs can be instantiated as constraints or inputs for low-level action models, which generate executable robot actions.

For learning-based action modeling, we further organize existing methods into three fundamental components:
**input modeling**, which studies what sensory modalities are used and how they are represented; **latent learning**, which explores how intermediate representations or latent actions are learned; and **policy learning**, which investigates how actions are generated from learned representations.

<div align="center">
  <img src="imgs/venue_distribution.png" alt="venue distribution"
       style="image-rendering: auto; max-width: 95%; height: auto;">
</div>

<b>Literature Distribution.</b> The survey covers a broad range of literature from major robotics, machine learning, and computer vision venues. The collected papers are mainly published in leading conferences and journals, including CoRL, ICRA, RSS, IROS, NeurIPS, ICLR, CVPR, ICML, IEEE RA-L, IEEE T-RO, IJRR, and other representative venues.

<div align="center">
  <img src="imgs/keyword_wordcloud.png" alt="keyword cloud"
       style="image-rendering: auto; max-width: 100%; height: auto;">
</div>

<b>Word Cloud.</b> The keyword analysis summarizes major research trends in robot manipulation, highlighting emerging topics such as imitation learning, reinforcement learning, vision-language-action models, diffusion policies, dexterous manipulation, grasping, world models, and generalization.

</details>



<!-- ------- 0 - Content Table ------- -->
<h2 id="table-of-contents">🏠 Table of Contents</h2>

- [📝 Awesome Papers](#-awesome-papers)
  - [📄 Survey](#-survey)
  - [Manipulation Tasks](contents/manipulation_tasks.md)
    - [Grasp](contents/manipulation_tasks.md#grasp)
    - [Basic Manipulation](contents/manipulation_tasks.md#basic-manipulation)
    - [Dexterous Manipulation](contents/manipulation_tasks.md#dexterous-manipulation)
    - [Soft Robotic Manipulation](contents/manipulation_tasks.md#soft-robotic-manipulation)
    - [Deformable Object Manipulation](contents/manipulation_tasks.md#deformable-object-manipulation)
    - [Mobile Manipulation](contents/manipulation_tasks.md#mobile-manipulation)
    - [Quadrupedal Manipulation](contents/manipulation_tasks.md#quadrupedal-manipulation)
    - [Humanoid Manipulation](contents/manipulation_tasks.md#humanoid-manipulation)
    - [Aerial Manipulation](contents/manipulation_tasks.md#aerial-manipulation)
    - [Underwater Manipulation](contents/manipulation_tasks.md#underwater-manipulation)
  - [High-level Structured Planning](contents/high-level_structured_planning.md)
    - [Task Planning](contents/high-level_structured_planning.md#task-planning)
    - [Programmatic Planning](contents/high-level_structured_planning.md#programmatic-planning)
    - [Multimodal Reasoning](contents/high-level_structured_planning.md#multimodal-reasoning)
    - [Geometric Constraint-based Planning](contents/high-level_structured_planning.md#geometric-constraint-based-planning)
    - [3D Representation-based Planning](contents/high-level_structured_planning.md#3d-representation-based-planning)
    - [Video-based Planning](contents/high-level_structured_planning.md#video-based-planning)
  - [Low-level Learning-based Action Modeling](contents/low-level_learning-based_action_modeling.md)
    - [Learning Strategy](contents/low-level_learning-based_action_modeling.md#learning-strategy)
      - [Imitation Learning (IL)](contents/low-level_learning-based_action_modeling.md#imitation-learning-il)
      - [Reinforcement Learning (RL)](contents/low-level_learning-based_action_modeling.md#reinforcement-learning-rl)
      - [RL and IL](contents/low-level_learning-based_action_modeling.md#rl-and-il)
      - [Learning with Auxiliary Tasks](contents/low-level_learning-based_action_modeling.md#learning-with-auxiliary-tasks)
    - [Input Modeling](contents/low-level_learning-based_action_modeling.md#input-modeling)
      - [Vision Action Models](contents/low-level_learning-based_action_modeling.md#vision-action-models)
      - [Vision Language Action Models](contents/low-level_learning-based_action_modeling.md#vision-language-action-models)
      - [Tactile-based Action Models](contents/low-level_learning-based_action_modeling.md#tactile-based-action-models)
      - [Other Modalities](contents/low-level_learning-based_action_modeling.md#other-modalities)
    - [Latent Learning](contents/low-level_learning-based_action_modeling.md#latent-learning)
      - [Pretrained Latent Learning](contents/low-level_learning-based_action_modeling.md#pretrained-latent-learning)
      - [Latent Action Learning](contents/low-level_learning-based_action_modeling.md#latent-action-learning)
    - [Policy Learning](contents/low-level_learning-based_action_modeling.md#policy-learning)
      - [Diffusion Policy](contents/low-level_learning-based_action_modeling.md#diffusion-policy)
      - [Flow Matching Policy](contents/low-level_learning-based_action_modeling.md#flow-matching-policy)
      - [Other Policies](contents/low-level_learning-based_action_modeling.md#other-policies)
  - [Bottlenecks](contents/bottlenecks.md)
    - [Data Collection and Utilization](contents/bottlenecks.md#data-collection-and-utilization)
        - [Data Collection](contents/bottlenecks.md#data-collection)
        - [Data Utilization](contents/bottlenecks.md#data-utilization)
    - [Generalization](contents/bottlenecks.md#generalization)
      - [Task Generalization](contents/bottlenecks.md#task-generalization)
      - [Environment Generalization](contents/bottlenecks.md#environment-generalization)
      - [Cross-Embodiment Generalization](contents/bottlenecks.md#cross-embodiment-generalization)
  - [Applications](contents/applications.md)
- [📊 Awesome Simulators, Benchmarks and Datasets](#-awesome-simulators-benchmarks-and-datasets)
  - [Grasp Datasets](#grasp-datasets)
  - [Single-Embodiment Manipulation Simulators and Benchmarks](#single-embodiment-manipulation-simulators-and-benchmarks)
  - [Cross-Embodiment Simulators and Benchmarks](#cross-embodiment-simulators-and-benchmarks)
  - [Other Simulators and Benchmarks](#other-simulators-and-benchmarks)
  - [Trajectory Datasets](#trajectory-datasets)
  - [Embodied QA and Affordance Datasets](#embodied-qa-and-affordance-datasets)
  - [Human and Robotic Video Benchmarks and Datasets](#human-and-robotic-video-benchmarks-and-datasets)
- [🛠️ Awesome Techniques](#-awesome-techniques)
  - [Tutorial](#tutorial)
  - [GitHub Repo](#github-repo)



<!-- ------- 1 - Papers ------- -->
## 📑 Awesome Papers

<!-- ------- 1.1 - Survey ------- -->
### 📄 Survey
|  Title  |   Venue  |   Date   |   Code   |   Notes  |
|:--------|:--------:|:--------:|:--------:|:--------:|
| _VLA Models_ |
| [**Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms**](https://arxiv.org/abs/2604.23775) | arXiv | 2026-04-26 | ![Star](https://img.shields.io/github/stars/LiQiiiii/Awesome-VLA-Safety?style=social&label=Star) [GitHub](https://github.com/LiQiiiii/Awesome-VLA-Safety) | VLA + Robustness |
| [**Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines**](https://arxiv.org/abs/2604.23001) | TMLR 2026 | 2026-04-24 | ![Star](https://img.shields.io/github/stars/ziyaow1010/vla-datasets-benchmarks?style=social&label=Star) [GitHub](https://github.com/ziyaow1010/vla-datasets-benchmarks) | VLA + Data |
| [**An Anatomy of Vision-Language-Action Models: From Modules to Milestones and Challenges**](https://arxiv.org/abs/2512.11362) | arXiv | 2025-12-12 | ![Star](https://img.shields.io/github/stars/SuyuZ1/VLA-Survey-Anatomy?style=social&label=Star) [GitHub](https://github.com/SuyuZ1/VLA-Survey-Anatomy) | VLA |
| [**A Survey on Efficient Vision-Language-Action Models**](https://arxiv.org/abs/2510.24795) | arXiv | 2025-10-27 | ![Star](https://img.shields.io/github/stars/YuZhaoshu/Efficient-VLAs-Survey?style=social&label=Star) [GitHub](https://github.com/YuZhaoshu/Efficient-VLAs-Survey) | VLA Models + Efficiency |
| [**Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey**](https://arxiv.org/abs/2510.17111) | arXiv | 2025-10-20 | - | VLA + Efficiency |
| [**Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications**](https://arxiv.org/abs/2510.07077) | IEEE Access 2025 | 2025-10-08 | [Project](https://vla-survey.github.io/) | VLA |
| [**Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey**](https://arxiv.org/abs/2508.13073) | arXiv | 2025-08-23 | ![Star](https://img.shields.io/github/stars/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation?style=social&label=Star) [GitHub](https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation) | VLA |
| [**Survey of Vision-Language-Action Models for Embodied Manipulation**](https://arxiv.org/abs/2508.15201) | arXiv | 2025-08-21 | - | VLA |
| [**Vision Language Action Models in Robotic Manipulation: A Systematic Review**](https://arxiv.org/abs/2507.10672) | arXiv | 2025-07-14 | - | VLA |
| [**A Survey on Vision-Language-Action Models: An Action Tokenization Perspective**](https://arxiv.org/abs/2507.01925) | arXiv | 2025-07-02 | - | VLA |
| [**Parallels Between VLA Model Post-Training and Human Motor Learning: Progress, Challenges, and Trends**](https://arxiv.org/abs/2506.20966) | arXiv | 2025-05-26 | ![Star](https://img.shields.io/github/stars/AoqunJin/Awesome-VLA-Post-Training?style=social&label=Star) [GitHub](https://github.com/AoqunJin/Awesome-VLA-Post-Training) | VLA |
| [**Vision-Language-Action Models: Concepts, Progress, Applications and Challenges**](https://arxiv.org/abs/2505.04769) | arXiv | 2025-05-07 | - | VLA |
| [**A Survey on Vision-Language-Action Models for Embodied AI**](https://arxiv.org/abs/2405.14093) | TNNLS 2026 | 2024-05-23 | - | VLA |
| _World Model_|
| [**Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models**](https://arxiv.org/abs/2609.03927) | arXiv | 2026-09-03 | - | World Model |
| [**From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence**](https://arxiv.org/abs/2607.11689) | arXiv | 2026-07-13 | - | World Model |
| [**A Definition and Roadmap for World Models**](https://arxiv.org/abs/2607.06401) | arXiv | 2026-07-07 | - | World Model |
| [**World Models for Robotic Manipulation: A Survey**](https://arxiv.org/abs/2606.00113) | arXiv | 2026-05-27 | - | World Model |
| [**World Action Models: The Next Frontier in Embodied AI**](https://arxiv.org/abs/2605.12090) | arXiv | 2026-05-12 | ![Star](https://img.shields.io/github/stars/OpenMOSS/Awesome-WAM?style=social&label=Star) [GitHub](https://github.com/OpenMOSS/Awesome-WAM) | World Model |
| [**World Model for Robot Learning: A Comprehensive Survey**](https://arxiv.org/abs/2605.00080) | IJRR 2026 | 2026-04-30 | ![Star](https://img.shields.io/github/stars/NTUMARS/Awesome-World-Model-for-Robotics-Policy?style=social&label=Star) [GitHub](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy) | World Model |
| [**A Step Toward World Models: A Survey on Robotic Manipulation**](https://arxiv.org/abs/2511.02097) | arXiv | 2025-10-31 | - | World Model |
| _Manipulation_ |
| [**Data Pyramid for Embodied Manipulation**](https://arxiv.org/abs/2607.24744) | arXiv | 2026-07-27 | ![Star](https://img.shields.io/github/stars/worldbench/awesome-embodied-data-pyramid?style=social&label=Star) [GitHub](https://github.com/worldbench/awesome-embodied-data-pyramid) | Data |
| [**3D Generation for Embodied AI and Robotic Simulation: A Survey**](https://arxiv.org/abs/2604.26509) | arXiv | 2026-04-29 | - | 3D |
| [**Embodied Robot Manipulation in the Era of Foundation Models: Planning and Learning Perspectives**](https://arxiv.org/abs/2512.22983) | T-RO 2026 | 2025-12-28 | ![Star](https://img.shields.io/github/stars/BaiShuanghao/Awesome-Robotics-Manipulation?style=social&label=Star) [GitHub](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) | Manipulation |
| [**Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey**](https://arxiv.org/abs/2510.10903) | arXiv | 2025-10-13 | ![Star](https://img.shields.io/github/stars/BaiShuanghao/Awesome-Robotics-Manipulation?style=social&label=Star) [GitHub](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) | Manipulation |
| [**A Survey of Robotic Navigation and Manipulation with Physics Simulators in the Era of Embodied AI**](https://arxiv.org/abs/2505.01458) | arXiv | 2025-05-01 | - | Navigation and Manipulation |
| [**Diffusion Models for Robotic Manipulation: A Survey**](https://arxiv.org/abs/2504.08438) | arXiv | 2025-04-11 | - | Manipulation + DP |
| [**Generative Artificial Intelligence in Robotic Manipulation: A Survey**](https://arxiv.org/abs/2503.03464) | arXiv | 2025-03-05 | ![Star](https://img.shields.io/github/stars/GAI4Manipulation/AwesomeGAIManipulation?style=social&label=Star) [GitHub](https://github.com/GAI4Manipulation/AwesomeGAIManipulation) | Manipulation + Generative Models |
| [**A Survey of Embodied Learning for Object-Centric Robotic Manipulation**](https://arxiv.org/abs/2408.11537) | MIR 2025 | 2024-08-21 | ![Star](https://img.shields.io/github/stars/RayYoh/OCRM_survey?style=social&label=Star) [GitHub](https://github.com/RayYoh/OCRM_survey) | Manipulation + Object-Centric |
| [**Language-conditioned Learning for Robotic Manipulation: A Survey**](https://arxiv.org/abs/2312.10807) | arXiv | 2023-12-17 | ![Star](https://img.shields.io/github/stars/hk-zh/language-conditioned-robot-manipulation-models?style=social&label=Star) [GitHub](https://github.com/hk-zh/language-conditioned-robot-manipulation-models) | Manipulation |
| _Dexterous Manipulation_ |
| [**The Developments and Challenges towards Dexterous and Embodied Robotic Manipulation: A Survey**](https://arxiv.org/abs/2507.11840) | RAM 2025 | 2025-07-16 | - | Dexterous Manipulation |
| [**Interactive Imitation Learning for Dexterous Robotic Manipulation: Challenges and Perspectives -- A Survey**](https://arxiv.org/abs/2506.00098) | arXiv | 2025-06-30 | - | Dexterous Manipulation |
| [**Dexterous Manipulation through Imitation Learning: A Survey**](https://arxiv.org/abs/2504.03515) | arXiv | 2025-04-04 | - | Dexterous Manipulation |
| _Deformable Object Manipulation (DOM)_ |
| [**T-DOM: A Taxonomy for Robotic Manipulation of Deformable Objects**](https://arxiv.org/abs/2412.20998) | arXiv | 2024-12-30 | [Project](https://sites.google.com/view/t-dom) | DOM |
| [**A Survey on Robotic Manipulation of Deformable Objects: Recent Advances, Open Challenges and New Frontiers**](https://arxiv.org/abs/2312.10419) | arXiv | 2023-12-16 | - | DOM |
| [**Robotic manipulation and sensing of deformable objects in domestic and industrial applications: a survey**](https://uca.hal.science/hal-01816189/document) | IJRR 2018 | 2018-06-13 | - | DOM |
| _Humanoid Manipulation_ |
| [**Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning**](https://arxiv.org/abs/2501.02116) | TMECH 2025 | 2025-01-03 | - | Humanoid Manipulation |
| [**Teleoperation of Humanoid Robots: A Survey**](https://arxiv.org/abs/2301.04317) | T-RO 2024 | 2023-01-11 | [Project](https://humanoid-teleoperation.github.io/) | Humanoid |
| _Others_ |
| [**No Free Checker: A Survey of Verifiers for Robot Policies**](https://arxiv.org/abs/2609.09250) | arXiv | 2026-09-08 | ![Star](https://img.shields.io/github/stars/ZJUSCL/Awesome-Robot-Verifier?style=social&label=Star) [GitHub](https://github.com/ZJUSCL/Awesome-Robot-Verifier) | Robustness |
| [**Progress Reward Modeling for Robotic Learning: A Comprehensive Survey**](https://arxiv.org/abs/2607.21655) | arXiv | 2026-07-22 | ![Star](https://img.shields.io/github/stars/sterzhang/Awesome-Progress-Models?style=social&label=Star) [GitHub](https://github.com/sterzhang/Awesome-Progress-Models) | Data |
| [**Robot Learning from Human Videos: A Survey**](https://arxiv.org/abs/2604.27621) | arXiv | 2026-04-30 | ![Star](https://img.shields.io/github/stars/IRMVLab/awesome-robot-learning-from-human-videos?style=social&label=Star) [GitHub](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) | Video |
| [**Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions**](https://arxiv.org/abs/2604.15395) | arXiv | 2026-04-16 | - | Robotics |
| [**From Video to Control: A Survey of Learning Manipulation Interfaces from Temporal Visual Data**](https://arxiv.org/abs/2604.04974) | arXiv | 2026-04-04 | - | Video |
| [**Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses**](https://arxiv.org/abs/2605.02900) | arXiv | 2026-03-28 | ![Star](https://img.shields.io/github/stars/x-zheng16/Awesome-Embodied-AI-Safety?style=social&label=Star) [GitHub](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety) | Embodied + Safety |
| [**Toward Generalist Neural Motion Planners for Robotic Manipulators: Challenges and Opportunities**](https://arxiv.org/abs/2603.24318) | TASE 2026 | 2026-03-25 | ![Star](https://img.shields.io/github/stars/DavoodSZ/DeepLearning-MotionPlanning-Manipulators?style=social&label=Star) [GitHub](https://github.com/DavoodSZ/DeepLearning-MotionPlanning-Manipulators) | Motion Planning |
| [**Video Generation Models in Robotics -- Applications, Research Challenges, Future Directions**](https://arxiv.org/abs/2601.07823) | arXiv | 2026-01-12 | - | Video Generation |
| [**Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models**](https://arxiv.org/abs/2512.11908) | arXiv | 2025-12-10 | - | Contact-Rich Manipulation |
| [**Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision**](https://arxiv.org/abs/2504.02477) | arXiv | 2025-04-03 | ![Star](https://img.shields.io/github/stars/Xiaofeng-Han-Res/MF-RV?style=social&label=Star) [GitHub](https://github.com/Xiaofeng-Han-Res/MF-RV) | Robot Vision |
| [**Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI**](https://arxiv.org/abs/2407.06886) | arXiv | 2024-07-09 | ![Star](https://img.shields.io/github/stars/HCPLab-SYSU/Embodied_AI_Paper_List?style=social&label=Star) [GitHub](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) | Embodied Agent |
| [**Survey of Learning-based Approaches for Robotic In-Hand Manipulation**](https://arxiv.org/abs/2401.07915) | arXiv | 2024-01-15 | - | In-hand Manipulation |
| [**Deep Learning Approaches to Grasp Synthesis: A Review**](https://arxiv.org/abs/2207.02556) | T-RO 2023 | 2023-07-06 | [Project](https://rhys-newbury.github.io/projects/6dof/) | Grasp |
| [**A Survey of Wheeled Mobile Manipulation: A Decision Making Perspective**](https://par.nsf.gov/servlets/purl/10393722) | J. Mech. Robot. 2023 | 2023-04 | - | Mobile Manipulation |
| [**A Review of Soft Manipulator Research, Applications, and Opportunities**](https://onlinelibrary.wiley.com/doi/abs/10.1002/rob.22051) | J Field Robot. 2023 | 2023-04 | - | Soft Manipulator |

<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

<!-- ------- 1.2 - Future Direction ------- -->
<!-- ### Future Direction
<!-- |  Title  |   Venue  |   Date   |   Code   | 
|:--------|:--------:|:--------:|:--------:|
| [**Federated Learning for Large-Scale Cloud Robotic Manipulation: Opportunities and Challenges**](https://www.arxiv.org/abs/2507.17903) | ICMLC 2025 | 2025-07-23 | - | | --> 

> **Note:** Other papers are **summarized** in the [**Contents**](contents/).



<!-- ------- 2 - Benchmarks ------- -->
## 📊 Awesome Simulators, Benchmarks and Datasets

<!-- ------- 2.1 - Grasp Datasets ------- -->
### Grasp Datasets
<!-- |  Title  |   Venue  |   Date   |   Code   |   Notes  |
|:--------|:--------:|:--------:|:--------:|:--------:| -->
|  Title  |   Venue  |   Date   |   Code   | 
|:--------|:--------:|:--------:|:--------:|
| _Rectangle-based Grasp_ |
| [**Beyond Visual Grasping: Benchmarking Complex Grasping from Detection to Execution**](https://arxiv.org/abs/2607.14341) | IROS 2026 | 2026-07-15 | [Project](https://airvlab.github.io/GCA-Bench/) |  |
| [**RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation**](https://arxiv.org/abs/2603.14880) | CVPR 2026 | 2026-03-16 | ![Star](https://img.shields.io/github/stars/lif314/RealVLG-R1?style=social&label=Star) [GitHub](https://github.com/lif314/RealVLG-R1) |  |
| [Grasp-Anything-6D: **Language-Driven 6-DoF Grasp Detection Using Negative Prompt Guidance**](https://arxiv.org/abs/2407.13842) | ECCV 2024 | 2024-07-18 | ![Star](https://img.shields.io/github/stars/Fsoft-AIC/Language-Driven-6-DoF-Grasp-Detection-Using-Negative-Prompt-Guidance?style=social&label=Star) [GitHub](https://github.com/Fsoft-AIC/Language-Driven-6-DoF-Grasp-Detection-Using-Negative-Prompt-Guidance) |  |
| [Grasp-Anything++: **Language-driven Grasp Detection**](https://arxiv.org/abs/2406.09489) | CVPR 2024 | 2024-06-13 | ![Star](https://img.shields.io/github/stars/Fsoft-AIC/LGD?style=social&label=Star) [GitHub](https://github.com/Fsoft-AIC/LGD) |  |
| [**Grasp-Anything: Large-scale Grasp Dataset from Foundation Models**](https://arxiv.org/abs/2309.09818) | ICRA 2024 | 2023-09-18 | ![Star](https://img.shields.io/github/stars/Fsoft-AIC/Grasp-Anything?style=social&label=Star) [GitHub](https://github.com/Fsoft-AIC/Grasp-Anything) | |
| [**REGRAD: A Large-Scale Relational Grasp Dataset for Safe and Object-Specific Robotic Grasping in Clutter**](https://arxiv.org/abs/2104.14118) | ICRA 2021 | 2021-04-29 | ![Star](https://img.shields.io/github/stars/poisonwine/REGRAD?style=social&label=Star) [GitHub](https://github.com/poisonwine/REGRAD) | |
| [**Jacquard: A Large Scale Dataset for Robotic Grasp Detection**](https://arxiv.org/abs/1803.11469) | IROS 2018 | 2018-03-30 | [Project](https://jacquard.liris.cnrs.fr/) | |
| [Cornell: **Efficient Grasping from RGBD Images: Learning Using a New Rectangle Representation**](https://ieeexplore.ieee.org/document/5980145) | ICRA 2011 | 2011-08 | - | |
| _6-DoF Grasp_ |
| [**GraspFactory: A Large Object-Centric Grasping Dataset**](https://arxiv.org/abs/2509.20550) | CoRLW 2025 | 2025-09-24 | ![Star](https://img.shields.io/github/stars/AutodeskRoboticsLab/graspfactory?style=social&label=Star) [GitHub](https://github.com/AutodeskRoboticsLab/graspfactory) | |
| [**MapleGrasp: Mask-guided Feature Pooling for Language-driven Efficient Robotic Grasping**](https://arxiv.org/abs/2506.06535) | WACV 2026 | 2025-06-06 | - | |
| [**GraspClutter6D: A Large-scale Real-world Dataset for Robust Perception and Grasping in Cluttered Scenes**](https://arxiv.org/abs/2504.06866) | RA-L 2025 | 2025-04-09 | [Project](https://sites.google.com/view/graspclutter6d) | |
| [**QDGset: A Large Scale Grasping Dataset Generated with Quality-Diversity**](https://arxiv.org/abs/2410.02319) | ICRA 2025 | 2024-10-03 | [Project](https://github.com/qdgrasp/qdgrasp.github.io/blob/main/qdg_set.md) | |
| [**Real-to-Sim Grasp: Rethinking the Gap between Simulation and Real World in Grasp Detection**](https://arxiv.org/abs/2410.06521) | CoRL 2024 | 2024-10-09 | [Project](https://isee-laboratory.github.io/R2SGrasp/) | |
| [**MetaGraspNetV2: All-in-One Dataset Enabling Fast and Reliable Robotic Bin Picking via Object Relationship Reasoning and Dexterous Grasping**](https://ieeexplore.ieee.org/document/10309974) | TASE 2023 | 2023-11-06 | ![Star](https://img.shields.io/github/stars/maximiliangilles/MetaGraspNet?style=social&label=Star) [GitHub](https://github.com/maximiliangilles/MetaGraspNet) | |
| [**MetaGraspNet: A Large-Scale Benchmark Dataset for Scene-Aware Ambidextrous Bin Picking via Physics-based Metaverse Synthesis**](https://arxiv.org/abs/2208.03963) | CASE 2022 | 2022-08-08 | ![Star](https://img.shields.io/github/stars/maximiliangilles/MetaGraspNet?style=social&label=Star) [GitHub](https://github.com/maximiliangilles/MetaGraspNet) | |
| [**ACRONYM: A Large-Scale Grasp Dataset Based on Simulation**](https://arxiv.org/abs/2011.09584) | ICRA 2021 | 2020-11-18 | ![Star](https://img.shields.io/github/stars/NVlabs/acronym?style=social&label=Star) [GitHub](https://github.com/NVlabs/acronym) | |
| [**GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping**](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf) | CVPR 2020 | 2020-08-05 | ![Star](https://img.shields.io/github/stars/graspnet/graspnet-baseline?style=social&label=Star) [GitHub](https://github.com/graspnet/graspnet-baseline) | |
| _Dexterous Grasp_ |
| [**HRDexDB: A Large-Scale Dataset of Dexterous Human and Robotic Hand Grasps**](https://arxiv.org/abs/2604.14944) | arXiv | 2026-04-16 | [Project](https://snuvclab.github.io/HRDexDB/) | |
| [**Dex1B: Learning with 1B Demonstrations for Dexterous Manipulation**](https://arxiv.org/abs/2506.17198) | RSS 2025 | 2025-06-20 | [Project](https://jianglongye.com/dex1b/) | |
| [**DexGraspNet 2.0: Learning Generative Dexterous Grasping in Large-scale Synthetic Cluttered Scenes**](https://openreview.net/attachment?id=5W0iZR9J7h&name=pdf) | CoRL 2024 | 2024 | ![Star](https://img.shields.io/github/stars/PKU-EPIC/DexGraspNet2?style=social&label=Star) [GitHub](https://github.com/PKU-EPIC/DexGraspNet2)  |
| [**UniFucGrasp: Human-Hand-Inspired Unified Functional Gras

## File tree (depth 3, assets pruned)

```
LICENSE
README.md
contents/
  applications.md
  bottlenecks.md
  high-level_structured_planning.md
  low-level_learning-based_action_modeling.md
  manipulation_tasks.md
documents/
  T-RO/
    appendix.pdf
  arxiv_update_log_v2.md
imgs/
  basic.png
  keyword_wordcloud.png
  summary.png
  venue_distribution.png
```

## Config files (0)


## Python signatures and reward/observation bodies (0 files)
