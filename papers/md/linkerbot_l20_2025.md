# LinkerBot Linker Hand L20 (and O6)

source entry: linkerbot_l20_2025


## https://openelab.io/products/linker-hand-linkerbot-l20-21,

HTTP 404


## https://www.roboticscenter.ai/hardware/linker-bot-o6

[](/)

[Robots](/store)

[Data & Dev](/marketplace)

[Learn](/learn)

[About](/about)

Shop

[StoreBrowse the full hardware catalog](/store)[Shop by BrandExplore robotics manufacturers](/brands)[HardwareBrowse robots, parts & components](/hardware)

Explore

[ApplicationsRobots by task & industry](/applications)[Compare ProductsSide-by-side specs & pricing](/compare)[LeasingFlexible access to research hardware](/leasing)

Build & deploy

[Contract ManufacturingSourcing, assembly & QA from prototype to production](/contract-manufacturing)[Mobile ManipulatorThe RCSV M1 platform](/mobile-manipulator)

Data

[Data MarketplaceHardware-synced robot datasets](/marketplace)[DatasetsExplore robot-learning datasets](/datasets)[Data ServicesCollection, teleop & annotation](/data-services)[Dexterous Hand DataTeleop, egocentric & UMI collection](/data-services/dexterous-hand-data)[DatakitBuild and manage robot datasets](/datakit)

Develop & evaluate

[RL² EvalEvaluate policies on real robots](/eval)[VLA ModelsVision-language-action model guide](/vla-models)[BenchmarksRobot-learning benchmarks explained](/benchmarks)[ToolsSimulators, datasets & stacks](/tools)

Operate

[TeleoperationOperate robots and collect demonstrations](/teleop)[RL EnvironmentsTrain and evaluate policies in simulation](/rl-environments)

Partners

[Start SellingList products on the marketplace](/marketplace/sell)[Supplier PortalManage products, orders & fulfillment](/supplier)

Learn

[AcademyGuides to deploy faster](/learn)[GuidesHands-on hardware & data guides](/guides)[GlossaryRobotics terms, defined](/glossary)[Developer DocsQuickstarts & integration notes](/wiki)

Community

[ForumQ&A, build logs & deployments](/forum)[InstitutionsLabs & universities we work with](/institutions)[EventsWorkshops, demos & meetups](/events)

Insights

[BlogDeep dives on physical AI](/blog)[NewsCompany news & robotics digest](/news)[ResearchPaper explainers & write-ups](/research)

Research

[ReportsIndustry reports & analysis](/reports)[MarketsRobotics by market & region](/markets)[WhitepaperRL² technical whitepaper](/whitepaper)

Company

[AboutWho we are](/about)[PeopleResearchers shaping robotics](/people)[CareersJoin the team](/careers)

Connect

[LocationsGlobal service coverage](/locations)[ContactTalk to our sales engineers](/contact)[NewsletterSubscribe to the Robotics Center weekly brief](/list)

SearchSearch robots, parts, datasets`⌘K`

[](/contact)[Contact Sales](/contact)

## Sign in

Account & settings[Sign in](/login?redirect=%2Fhardware%2Flinker-bot-o6)

LanguageEN

EnglishEN中文ZHDeutschDE日本語JAFrançaisFR한국어KOالعربيةARहिन्दीHIעבריתHEPortuguêsPTРусскийRUEspañolES

[](/)

RobotsData & DevLearnAbout

[Sign in](/login?redirect=%2Fhardware%2Flinker-bot-o6)[Chat with us](/chat)

LanguageEN

EnglishEN中文ZHDeutschDE日本語JAFrançaisFR한국어KOالعربيةARहिन्दीHIעבריתHEPortuguêsPTРусскийRUEspañolES

[Shop now→](/store)[Contact](/contact)

Shop Hardware

[Humanoids](/store/category/humanoid-robot)[Robotic Arms](/store/category/robotic-arm)[Quadrupeds](/store/category/quadruped-robot)[Dexterous Hands](/store/category/robotic-hand)[Sensors](/store/category/sensor)[Teleoperation](/store/category/teleoperation-motion-capture)

Data & Dev

[Data Marketplace](/marketplace)[RL² Eval](/eval)[Academy](/learn)[Developer Docs](/wiki)

Try: OpenArm, Wuji Hand, Unitree G1, quadruped, gripper

[ProductOpenArmOpen 7-DoF arm, bimanual-ready. Ships from San Francisco with pilot data-collection packages from $2,500.](/store/product/openarm)[ProductBrowse the Store90+ platforms — humanoids, arms, quadrupeds, dexterous hands, and teleoperation kits. In-stock hardware ships in 48 hours.](/store)[DatasetData MarketplaceHardware-synced demonstrations for VLA and imitation learning. Download in LeRobot, HDF5, or RLDS format.](/marketplace)[GuideGet Started with Physical AIFrom first arm on the bench to a policy that survives a real workcell — the Robotics Center pipeline in three steps.](/learn)[GuideWuji GloveSpecifications and integration guide for the tactile and pose-tracking data glove.](/hardware/wuji-glove)[GuideUnitree Go2 — Setup & SDKUnbox, calibrate, and run your first autonomous walk. Includes ROS 2 bringup and teleop quickstart.](/wiki)

`↵` to select

[Home](/) › [Hardware](/hardware) › LinkerBot O6 Dexterous Hand System

# LinkerBot O6

A 5-finger dexterous hand system with 12 DOF, glove-style teleoperation controller, 16-region tactile sensing, and USB serial integration. Three commands from unboxing to a live browser teleop session.

[Start Setup →](/hardware/linker-bot-o6/setup) [Wiki / SDK Docs →](/wiki/linker-bot-o6)

[Overview](/hardware/linker-bot-o6) [Quickstart](/hardware/linker-bot-o6/quickstart) [Setup](/hardware/linker-bot-o6/setup) [Software](/hardware/linker-bot-o6/software) [Specs](/hardware/linker-bot-o6/specs) [Data Collection](/hardware/linker-bot-o6/data-collection) [Safety](/hardware/linker-bot-o6/safety) [Community](/hardware/linker-bot-o6/community)

12

Degrees of Freedom

16

Tactile Regions

580 g

Hand Weight

15 min

Setup Time

Technical Specifications

## Full Hardware Specs

Vendor| LinkerBot / Linker / SVRC  
---|---  
Total DOF| 12 per hand (5 fingers, 2-3 DOF each)  
Fingers| 5 per hand, individual bend sensors  
Tactile Regions| 16 per hand (capacitive)  
Payload (per finger)| ~500 g tip pinch / ~2 kg power grasp  
Repeatability| ±0.5 mm fingertip position  
Max Finger Speed| ~300 deg/s  
Hand Weight| ~580 g (hand unit only)  
Power Supply| 12V DC, 3A peak  
Hand Support| Left and right, simultaneous  
Interface| USB Serial (/dev/ttyUSB0 Linux, COM* Windows)  
Baud Rate| 921600  
Protocol| SVRC framing (AA 55 03 99 header)  
Control Rate| 50 Hz command loop  
Operating Temp| 0 - 45 C  
SDK| pip install roboticscenter (Python 3.8+)  
ROS2 Package| linkerbot_o6_ros2 (Humble / Iron)  
  
[Full Specs →](/hardware/linker-bot-o6/specs)

Applications

## Use Cases

The LinkerBot O6 is designed for research labs, educational institutions, and data collection workflows that need reliable dexterous manipulation at an accessible price point.

### Imitation Learning Data Collection

Pair with the glove controller to record dexterous manipulation demonstrations at 50 Hz. Episodes export as JSONL, compatible with ACT, Diffusion Policy, and custom pipelines via the SVRC data platform.

### Manipulation Research

16 tactile regions give per-finger contact feedback for grasp stability analysis, slip detection, and in-hand regrasping experiments. Publish tactile data alongside joint state to ROS2 topics.

### Robotics Education

The 15-minute setup time and browser-based teleop panel make O6 ideal for university courses and workshops. Students go from unboxing to a working teleop demo in a single lab session.

### End-Effector Integration

Standard flange adapter mounts O6 on OpenArm 1, UR5e, Franka, or Kinova arms. The USB serial protocol means no CAN bus wiring -- just one cable to the host.

Why LinkerBot O6

## Why Choose the O6 Over Alternatives

### Fastest Setup in Class

Three commands from unboxing to live browser teleop. No firmware flashing, no CAN bus wiring, no ROS dependency. Plug USB, install SDK, launch session. Most competing hands require 2-4 hours of setup including driver installation and bus configuration.

### Integrated Glove Teleoperation

Ships with a matched glove controller for intuitive data collection. Calibrate open/closed fist, then record demonstrations immediately. Competing hands (Orca, Allegro) require separate teleoperation hardware purchased and integrated separately.

### Built-In Tactile Sensing

16 capacitive tactile regions per hand included out of the box. No aftermarket sensor integration needed. The Allegro Hand has zero tactile sensing stock; the Orca Hand requires Paxini sensors added separately.

### Cost-Effective for Labs

Priced well below the Shadow Hand ($100K+) and Allegro Hand ($15K+), the O6 provides 12 DOF and tactile sensing at a fraction of the cost. Leasing starts at a monthly rate that makes dexterous manipulation accessible to teaching labs and startups.

Head-to-Head

## Dexterous Hand Comparison

Feature | LinkerBot O6 | Orca Hand | Allegro Hand | Leap Hand  
---|---|---|---|---  
DOF| 12| 17| 16| 16  
Fingers| 5| 5| 4| 4  
Tactile Sensing| 16 regions (included)| Add-on (Paxini)| None stock| None stock  
Glove Teleop| Included| Separate purchase| Separate purchase| Separate purchase  
Setup Time| ~15 min| ~3-4 hrs| ~2 hrs| ~1 hr  
Interface| USB Serial| USB Serial| CAN / EtherCAT| USB Serial  
Open Source| SDK only| Full (MIT)| No| Full (MIT)  
Approx. Price| Contact for quote| ~$2K BOM (DIY)| ~$15K+| ~$2K BOM (DIY)  
Best For| Fast data collection| Research customization| High-torque research| Low-cost research  
  
[Compare All Hardware →](/compare)

Software Integration

## Python SDK & ROS2 Package

Control the O6 from Python in under 10 lines. The SDK handles serial framing, tactile decoding, and glove calibration automatically.

### Python SDK -- Joint Position Control

# pip install roboticscenter from roboticscenter import LinkerBotO6 # Auto-detect USB port and connect hand = LinkerBotO6.connect() # Read current joint positions (12 floats, normalized 0-1) joints = hand.get_joint_positions() print(f"Current positions: {joints}") # Command a pinch grasp (thumb + index close) hand.set_finger("thumb", position=0.8) hand.set_finger("index", position=0.8) # Read 16-region tactile data tactile = hand.get_tactile() print(f"Tactile: {tactile}") # Start recording to JSONL hand.start_recording("episode_001.jsonl") 

### ROS2 Integration

# Install ROS2 package (Humble / Iron) cd ~/ros2_ws/src git clone https://github.com/svrc/linkerbot_o6_ros2.git cd ~/ros2_ws && colcon build # Launch driver node -- publishes: # /linkerbot/joint_states (sensor_msgs/JointState) # /linkerbot/tactile (std_msgs/Float32MultiArray) ros2 launch linkerbot_o6_ros2 driver.launch.py port:=/dev/ttyUSB0 

After Unboxing

## Your Setup Journey

From unboxing to live browser teleop in under 15 minutes. Three commands is all it takes.

**Difficulty:** Beginner-friendly. No soldering, no firmware flashing, no CAN bus.

[ 1 Unboxing & USB Connect Plug in O6 via USB, confirm port appears on Linux or Windows ~5 min ](/hardware/linker-bot-o6/setup#step-1) [ 2 SDK Install & Connect pip install roboticscenter, then rc connect -- auto-detects the O6 ~5 min ](/hardware/linker-bot-o6/setup#step-2) [ 3 Browser Teleop Panel Open session URL -- finger positions, gesture presets, tactile heatmap ~2 min ](/hardware/linker-bot-o6/setup#step-3) [ 4 Glove Calibration Calibrate glove to operator hand size -- open and closed fist positions ~5 min ](/hardware/linker-bot-o6/setup#step-4) [ 5 Data Collection Start/stop episode recording from the browser panel -- JSONL format, platform-ready Ongoing ](/hardware/linker-bot-o6/setup#step-5)

[Open Full Setup Guide →](/hardware/linker-bot-o6/setup)

Documentation

## Guides & SDK Docs

Everything from protocol internals to platform integration and data collection.

[ Setup Guide → ](/hardware/linker-bot-o6/setup) [ Full Specifications → ](/hardware/linker-bot-o6/specs) [ Wiki: Full SDK & Protocol Docs → ](/wiki/linker-bot-o6) [ SDK Quickstart → ](/wiki/sdk-quickstart) [ SDK API Reference → ](/wiki/sdk-api-reference) [ Community & FAQ → ](/hardware/linker-bot-o6/community)

SVRC Services

## Services for LinkerBot O6

### [Data Collection Service Our team collects dexterous manipulation demonstrations using O6 + glove at our San Francisco or Allston labs. You receive cleaned JSONL episodes ready for training. ](/contact) ### [Hardware Leasing Lease the O6 (hand + glove bundle) on a monthly basis. Includes SDK access, firmware updates, and priority support. No long-term commitment. ](/leasing) ### [Repair & Calibration Send your O6 to our service center for recalibration, tendon replacement, or tactile sensor maintenance. Typical turnaround: 5 business days. ](/contact)

Related Hardware

## Also Consider

[ Orca Hand -- Open-source 17-DOF hand for deep customization → ](/hardware/orca-hand) [ Wuji Hand -- High-DOF teleop hand with 768-point tactile map → ](/hardware/wuji-hand) [ BrainCo Revo II -- Bionic hand with BLE + USB dual interface → ](/hardware/brainco-revo) [ OpenArm 1 -- 6-DOF arm to mount the O6 on → ](/hardware/openarm) [ Paxini GEN3 -- Add 6-axis tactile sensing to any gripper → ](/hardware/paxini-gen3)

Get Help & Share

## Community

Have a question or want to share your setup?

[SVRC Forum →](/forum) [FAQ →](/hardware/linker-bot-o6/community)

## Pricing & Availability

Purchase

Custom Quote

[Request Quote](/contact)

Monthly Lease

Available

[Lease Options](/leasing)

Pricing depends on hand configuration (left/right/pair), glove bundle, and quantity. Ships worldwide from San Francisco, CA. [Contact Us](/contact) for volume pricing or demo units.

Learn More

## Related Guides

[ Dexterous Hands Buying Guide → ](/guides/dexterous-hands) [ Teleoperation Setup Guide → ](/guides/teleoperation) [ Data Collection Best Practices → ](/guides/robot-data) [ LinkerBot O6 Learning Path → ](/learn/paths/linker-bot-o6)

## Ready to Start?

Three commands from unboxing to a live browser teleop session.

[Start Setup Guide](/hardware/linker-bot-o6/setup) [SDK Docs](/wiki/linker-bot-o6) [Contact Us](/contact)

Robotics Center of Silicon Valley. A global hub for showcasing, testing, and advancing robotics.

[](https://www.linkedin.com/company/roboticscenter/)[](https://www.youtube.com/@roboticscentersv)[](https://www.tiktok.com/@roboticscentersv)[](https://www.facebook.com/roboticscenterai)[](https://www.instagram.com/roboticscentersv/)

## Shop

[Store](/store)[Unitree](https://unitree.roboticscenter.ai)[Compare Products](/compare)[Leasing](/leasing)[Mobile Manipulator](/mobile-manipulator)

## Explore

[VLA Models](/vla-models)[Benchmarks](/benchmarks)[Tools](/tools)[Applications](/applications)[Locations](/locations)

## Learn & Data

[Academy](/learn)[Guides](/guides)[Blog](/blog)[Research](/research)[Glossary](/glossary)[Data Marketplace](/marketplace)

## Company

[About](/about)[People](/people)[Careers](/careers)[Events](/events)[Contact](/contact)

[Privacy](/privacy-policy)[Terms](/terms)[Refunds](/refund-policy)[Returns](/return-policy)

West Coast: 90 Welsh St, San Francisco, CA 94107 · East Coast: 125 Western Ave, Allston, MA 02134 · contact@roboticscenter.ai

## Your cart

[View cart](/cart)

Your cart is empty.

[Browse the Store →](/store)
