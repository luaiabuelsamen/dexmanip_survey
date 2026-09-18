# **GigaHands: A Massive Annotated Dataset of Bimanual Hand Activities** 

Rao Fu<sup>1</sup><sup>_∗_</sup> Dingxi Zhang<sup>2</sup><sup>_∗_</sup> Alex Jiang<sup>1</sup> Wanjia Fu<sup>1</sup> Austin Funk<sup>1</sup> Daniel Ritchie<sup>1</sup> Srinath Sridhar<sup>1</sup><sup>_†_</sup> 

> _∗_ Equal contribution _†_ Corresponding author 1Brown University 2ETH Zurich 

https://ivl.cs.brown.edu/research/gigahands.html 



<!-- Start of picture text -->
Intersect your fingers<br>Give a thumbs-up  and pull gently to  Deliver the fry<br>gesture. stretch. to your mouth.<br>Strum the ukelele strings with your right hand<br>Figure 1. GigaHands is a massive dataset of human bimanual activities with paired text annotations. Each column above shows an<br>activity sequence from the dataset. The dataset covers diverse 3D hand activities, including hand-object interactions (blue) across objectblue) across object) across object<br>arXiv:2412.04244v3  [cs.CV]  9 Apr 2025<br><!-- End of picture text -->

Figure 1. **GigaHands** is a massive dataset of human bimanual activities with paired text annotations. Each column above shows an activity sequence from the dataset. The dataset covers diverse 3D hand activities, including hand-object interactions (blue) across objectblue) across object) across object scales, gestures (orange), and self-interactions (red). Each clip is paired with descriptive text and 51 camera views, enabling radiance field reconstruction. The bottom row show other annotations in the dataset including hand shape, object shape and pose (left half images). The right half images show novel views from dynamic radiance field fitting. 

## **Abstract** 

_Understanding bimanual human hand activities is a critical problem in AI and robotics. We cannot build large models of bimanual activities because existing datasets lack the scale, coverage of diverse hand activities, and detailed annotations. We introduce GigaHands, a massive annotated dataset capturing 34 hours of bimanual hand activities from 56 subjects and 417 objects, totaling 14k motion clips derived from 183 million frames paired with 84k text annota-_ 

_tions. Our markerless capture setup and data acquisition protocol enable fully automatic 3D hand and object estimation while minimizing the effort required for text annotation. The scale and diversity of GigaHands enable broad applications, including text-driven action synthesis, hand motion captioning, and dynamic radiance field reconstruction._ 

## **1. Introduction** 

_“The_ **_human hand_** _is a marvel of evolution, whose intricate structures and capabilities have allowed us to manipulate_ 

_the environment in ways no other species can.”_ 

#### – F.R. Wilson [108] 

From the skillful manipulation involved in cooking a meal, to the rapid movement of fingers to type this sentence, hands are always busy shaping our environments and communicating with others. Enabling machines to understand and replicate the remarkable capabilities of human hands is one of the grand challenges of AI and robotics. One approach to achieve this goal could be to train models on massive datasets, the strategy followed by recent large models that learn from trillions of text tokens [27], billions of text-image pairs [89], tens of millions of 3D shapes [25], or millions of robot trajectories [12, 13, 46, 73]. However, datasets of this scale are currently unavailable for natural hand activities. 

Sourcing large-scale 3D hand activities data is challenging. The two most common methods for data acquisition involve using cameras to capture hand manipulations in the wild or in controlled studio settings. In-the-wild data includes monocular internet videos [91], egocentric videos captured using wearable cameras [22, 23, 32, 52, 57, 79], or multi-view videos from third-person cameras [30, 62, 91]. However, this data is sparse, hard to calibrate, and noisy, resulting in limited 3D motion reconstruction accuracy, especially for objects. Alternatively, studio settings bring subjects into camera-rich environments and could employ markers for accurate reconstruction. However, the staged setup and lack of real-world context limits data diversity, and marker-based tracking [8, 28, 29, 55, 58, 59, 101, 111, 116] inhibits natural interactions. 

We address the data sourcing problem preventing the scaling up of hand datasets by introducing **GigaHands** , a diverse, massive, and fully-annotated 3D bimanual hand activities dataset (see Figure 1). To our knowledge, GigaHands is the largest bimanual hand activities dataset, with over **183 million** unique image frames with two hands each (0.37 _×_ 10<sup>9</sup> unique hand poses, hence GigaHands). We used a multi-camera markerless capture system to acquire accurate bimanual hand-object interaction activities, gestures, and self-contacts. We overcome the studio capturing limitation by designing procedural activity elicitation protocols to include as many actions as in the real-world in-the-wild setting. To ensure diversity that reflects the real world, we captured data from **56 subjects** interacting with **417 realworld objects** . All images in our dataset are fully annotated with: detailed activity text descriptions; 3D hand shape and pose; MANO [86] hand meshes; 3D object shape, pose and appearance; hand/object segmentation masks; 2D/3D hand keypoints; camera pose. We minimized manual annotation effort using a procedural _instruct-to-annotate_ strategy by guiding subjects with detailed instructions to reduce annotation effort post-capture. In total, we collected **34 hours** of text-annotated bimanual hand activities, **13k** 3D motion se- 

quences, and over **14k** post-processed 3D motion clips with **84k** detailed atomic-level text description annotations. Our 3D hand motion clips exceed the combined size of all existing 3D bimanual hand activities datasets [57, 58, 116], and the range of verbs in our text annotations is larger than any other hand dataset, even those captured in the wild [32, 33]. 

GigaHands can unlock new capabilities in applications including motion generation, robotics, and dynamic 3D reconstruction [81]. To demonstrate, we show improvements enabled by our dataset on text-driven action synthesis and hand motion captioning, along with examples dynamic radiance field reconstruction. To sum up our contributions: 

- We present **GigaHands** , a massive, diverse and annotated 3D bimanual activities dataset. It includes **34 hours** of activities, **14k** hand motions clips paired with **84k text annotation** , and over **183M** unique hand images. 

- A **procedural data acquisition** strategy that ensures activity diversity and detailed atomic-level text descriptions while minimizing manual effort. We also built an accurate and fully-automated pipeline for estimating 3D hand/object shape and pose, segmentation, and camera pose. 

- We show **applications** enabled by our dataset’s scale, including 3D hand motion generation, hand motion captioning, and dynamic semantic scene reconstruction. 

## **2. Related Work** 

### **2.1. Hand Motion Data Sourcing** 

Hand motion data has four primary sources, and each presents its own advantages and challenges concerning realism, diversity, accuracy, and practicality. 

**Static poses** involve motion planning [5, 7, 10, 93], policy learning [19, 60], or motion synthesis [20, 117, 118] from individual static positions. While these methods provide reliable 3D data, it lacks semantic richness, resulting in motions disconnected from real-world activities and not fully representing diverse human movement. 

**Synthetic data** from game engines [126], augmented reality [66], virtual reality [38], or simulations [39, 63, 105] allow for controlled and accurate 3D motion sequences. Despite their reliability, these synthetic motions often fail to capture the intricacies of genuine human movements, limiting their applicability in modeling natural hand behaviors. **Real-world in-the-wild settings** involves using wearable or portable sensors to capture hand interactions from egocentric [22, 23, 32, 52, 57, 79], third-person [30, 62, 91] or both types of views [33, 95], yielding realistic and natural motions. However, obtaining reliable 3D motion data for both hands and objects is challenging due to occlusions resulting from limited sensor deployment and accuracy. Additionally, annotating such data is labor-intensive, and certain self-contact motions are difficult to record accurately. **Studio environments** place participants in controlled set- 

tings equipped with extensive sensors, enabling reliable capture of detailed information such as 3D hand motions [45, 54, 55, 72, 120, 122], object movements [8, 18, 29, 36, 37, 48, 58, 59, 111, 116], contact regions [28, 80, 101], audio [44, 49, 71, 113], and tactile data [14, 31, 78, 100]. However, collecting data in studios is arduous and may not reflect the diversity of real-life scenarios. Participants might find it challenging to perform natural motions in an unfamiliar environment, especially when encumbered with wearable sensors. For example, motion capture (MoCap) systems [8, 28, 29, 55, 58, 59, 101, 111, 116] require markers attached to the body, reducing visual realism and inhibiting movements like self-contact between hands, necessitating additional post-processing to restore a realistic appearance. On the other hand, markerless motion capture systems [18, 36, 37, 45, 48, 54, 72, 80, 120, 122] offer more realistic visuals and encourage natural motions, but they may trade off capture accuracy. GigaHands balances accuracy, diversity, realism, and practicality by replicating in-the-wild settings during activity elicitation and estimating accurate 3D motion from marker-less motion capture. 

### **2.2. Hand Datasets and Annotations** 

Hand datasets vary in sources and scales, each constructed for specific purposes and enriched with various annotations. **Hand motion** is the most common type of annotation, represented as bounding boxes [30, 79, 91], segmentation masks [24, 52, 70], 2D keypoints [6, 43, 61, 90], 3D keypoints [82, 99, 102, 106], or parameters of parametric models [55, 77, 97]. Depending on the data source and desired detail, annotations are obtained through manual labeling [106], synthesis [66, 67, 92, 126], markers and sensors [29, 45, 54, 104, 115, 120, 122], cross-view bootstrapping [65, 96], iteratively trained keypoint extraction networks [72, 127], multi-view annotation [72], or audio refinement [44]. Semi-automatic and automatic labeling techniques significantly improve scalability. 

**Object annotations** are provided given the frequent interaction between hands and objects. These can be acquired from manual labeling [18, 57, 98], synthesis [21, 39], MoCap [8, 28, 58, 59, 111, 112, 116, 124], hand-object reconstruction or retrieval [15, 64, 109], or multi-view RGB-D data [36, 37, 48]. We demonstrate that multi-view RGB us sufficient for automatic annotation, enhancing scalability. **Text annotations.** To capture the rich semantic meanings in human hand actions, certain datasets provide text annotations. These annotations may include action types [26, 30, 32, 47, 79], atomic action descriptions [22, 23, 33, 52, 90], activity narration [22, 23, 33, 62], activity commentary [17, 32, 33, 116], object affordance [42, 58, 111, 116], or body dynamics [114, 122, 123]. Typically, annotations are manually provided, especially when data are collected in uncontrolled, unscripted environments [22, 23, 32, 33]. 

Table 1. Comparisons of 3D bimanual motion datasets. Dataset names are highlighted with different colors if it has no text annotations (gray), action type (green), sparse description (red), and dense description (blue). See the supp. document for the full table. 

|Name<br>w/o Object Annotatio|mins  <br>n|motions|poses|views|frames|sub.|obj.|
|---|---|---|---|---|---|---|---|
|AssemblyHands[72]|630|62|203k|12|3.03M|34|_/_|
|Ego-Exo4D[33]|_/_|_/_|**4.4M**|5-6|_/_|**740**|_/_|
|w/ Object Annotation||||||||
|HOI4D[57]|1,333|4k|1.2M|1|2.4M|4|**800**|
|ARCTIC[28]|121|339|218k|9|2.1M|10|11|
|TACO[58]|202|2.3k|363k|13|4.7M|14|196|
|OakInk2[116]|557|2.8k|993k|4|4.01M|9|75|
|HOT3D[8]|833|4.1k|1.7M|2-3|3.7M|19|33|
|GigaHands(Ours)|**2,034 **|**13.9k**|3.7M|**51**|**183M**|56|417|



Even in studio settings, post-processing is often required to extract meaningful action clips [52, 116]. We introduce a procedural instruct-and-annotate pipeline that maximizes semantic interpretability and minimizes the annotation effort. 

**Contact** are derived from manual annotation [91], video grounding [69], thermal sensors [9, 11] or geometry analysis [80, 101, 125] based on captured data. Our dataset enables us to derive contact regions using geometry analysis on both surface mesh and density fields. 

## **3. The GigaHands Dataset** 

**Dataset Characteristics.** GigaHands is a large and diverse dataset of bimanual hand activities with detailed annotations. It encompasses a wide range of scenarios, including hand-object interactions, gesturing, and self-contacts performed by 56 subjects who collectively used 417 objects (see Table 1). The dataset contains 2,034 minutes of bimanual hand activities, surpassing the length of any existing 3D hand motion dataset. Compared to other datasets that are unannotated [8, 28], contain motion type annotations [57, 58, 72], or provide sparse motion descriptions [33, 116], GigaHands offers detailed text annotations for all captured activities. With a total of 13k instructed motion sequences, 14k annotated motion clips, and 84k augmented text descriptions, it is larger than any other dataset. Furthermore, GigaHands includes 3.7 million bimanual 3D hand poses, represented by both 3D keypoints and MANO [86] hand meshes, comparable to the scale of Ego-Exo4D [33] – the current largest annotated 3D hand pose dataset. However, unlike Ego-Exo4D, which is annotated from selected, non-continuous frames, GigaHands provides continuous bimanual 3D hand poses and shapes. Each motion clip was captured using 51 camera views, resulting in 183M RGB frames (and 366M unique hand images). This multi-view setup enables new applications such as dynamic 3D radiance field reconstruction. Additionally, 







<!-- Start of picture text -->
dataset verb count<br><!-- End of picture text -->

Figure 2. **Dataset Diversity.** The left and middle figures illustrate the diversity of pose and motion variations in GigaHands, visualized using t-SNE embeddings. Some points along the convex hull are highlighted with their corresponding text instructions, showcasing unique motions captured in our dataset. The right figure compares the verb sets among different datasets using an UpSet visualization [50]. Each column represents the number of verbs exclusive to specific subsets of datasets, indicated by the connected dots below the columns. The rows indicate the total verb count in each dataset. GigaHands contains more verbs and more exclusive verbs compared to other datasets. 

the dataset contains annotations for hand/object segmentation masks, 3D object shape, pose and appearance, 2D/3D keypoints, and camera poses. 

**Diverse Hand Pose and Motion.** Figure 2 (left) compares hand pose diversity across datasets using t-SNE [107] clustering of 3D keypoints of both hands. Similarly, Figure 2 (middle) shows hand motion diversity through t-SNE clustering of the latent codes of a Variational Autoencoder trained for motion reconstruction. GigaHands exhibits significantly greater diversity than existing datasets in both bimanual hand pose and motion. Additionally, datapoints near the boundary of our dataset seem to correspond to text annotations that are unique in our datasets, demonstrating that diverse verbs contribute to diverse poses and motions. 

**Diverse Text Annotation.** GigaHands contains activities that are more diverse than existing datasets [32, 33, 116] as measured using verb counts in Figure 2 (right). Since each verb corresponds to an activity, a diverse set of verb indicates activity diversity. GigaHands contains the most verbs (1467) with 580 of them being unique to our dataset. The key to achieving this diversity is our _instruct-to-annotate_ strategy (see Section 4.3) for automated labeled activity sourcing. Please refer to the supp. document for the source of verbs and detailed verb comparison. 

**Diverse Objects.** Figure 3 shows some of the tabletop objects included in GigaHands. We provide 3D meshes [2] with associated textures for rigid objects and multiview segmentation masks for non-rigid objects. Different from most datasets, we also include small-scale objects ( _e.g_ . pens) that are difficult to capture. We employ single-view reconstruction [3] to obtain meshes for these small objects. In total, the dataset includes 417 objects, with 310 multiview scanned meshes and 31 single-view generated meshes. 



<!-- Start of picture text -->
rendered objects front/left front/right<br>max<br>0<br>back/left back/right<br><!-- End of picture text -->

Figure 3. **Diverse Objects and Frequent Hand Contact Regions.** GigaHands provide objects (left) spanning diverse scenarios, including cooking, office working, crafting, entertainment, and housework. The diverse activities result in contact regions (right) spanning both the front and back of both hands. 

**Diverse Contacts.** Since we have 3D meshes both hands and objects, we can use them to estimate **contact maps** on both hands, following the approach in [101]. Figure 3 shows the accumulated contact regions from randomly sampled frames across the dataset. The results reveal diverse contact areas, including regions between fingers and on the back of the hands (e.g. punching uses the backs of hands). The right hand interacts with objects more frequently than the left, since a majority of our subjects were right-handed. 

## **4. Dataset Acquisition** 

We present our data acquisition pipeline, which balances realism, diversity, and accuracy while reducing annotation effort. Our procedural pipeline, called _Instruct-to-Annotate_ (see Figure 4), consists of several key components: 

- **Procedural instruction elicitation** (Section 4.1) for generating instructions to guide participants during data capture. 

- **Filming** (Section 4.2) using a markerless multi-camera system to record high-quality hand activity sequences. 



<!-- Start of picture text -->
parsing grouping structuring script generation filming annotating<br>cook Make and drink tea Make and drink tea<br>Ego4D Verbs.  add,   Objects.   1. Preparing the teapot.: 2. Adding hot water:  pour.lift. [Lift]: [Pour]:  Lift the lid off the teapot.Pour hot water from the<br>Ego-Exo4D apply,  beat,  bind,  cap,  carry,  chop,  clean … apple, banana, baking sheet … 3. Steeping tea bag:  tear, hold, steep, release, place. 4. Pouring tea:  pour. open, select,  kettle into the teapot. [Open]: [Select]:  bag from the box.Open the tea bag box.Select and remove a tea<br>OakInk-2 … … … [Tear]:  Tear the tea bag wrapper.<br>… craft Make a bowl of salad. [Hold]:  string. [Steeping]:  Hold the tea bag by the Steep the tea bag in the  Pour hot water from the kettle into the teapot.<br>TACO hot water.<br>office Bake and frost a bread. … Put down the teapot.<br>action datasets verb pool scenarios scenes instruction scripts motion sequences motion clips<br><!-- End of picture text -->

Figure 4. **Instruct-to-Annotate Pipeline.** The instruction elicitation process (left yellow block) creates atomic action-level instruction scripts in a temporally smooth order, structured within scenes. This is achieved by parsing action datasets, grouping verbs into a pool, structuring scenarios, and generating scene scripts. During filming, subjects act according to these scripts, producing recorded motion sequences. Annotators then process these sequences (right blue block) by segmenting them into clips and annotating unscripted motions. 

- **Motion annotation and text augmentation** (Section 4.3) to refine sequences by breaking them into shorter clips with accurate annotations. 

- **Hand motion** (Section 4.4) and **object motion estimation** (Section 4.5) for detailed 3D hand and object motions from the captured multi-view RGB videos. 

### **4.1. Instruction Elicitation** 

To ensure diverse hand activities and reduce annotation effort, the _Instruct-to-Annotate_ pipeline starts with a procedural instruction elicitation protocol. We began by sourcing atomic actions from multiple datasets [32, 33, 58, 116], extracting a pool of verbs corresponding to those actions. To elicit subjects to perform these verbs (actions), we manually associated each verb with multiple objects and, with the assistance of an LLM [4], grouped the verbs and objects into different scenarios such as cooking and eating, office work, crafting, entertainment, and housework. We then structured these scenarios into scenes where the objects could co-occur. Using LLM, we organized the scenes into lists of activities that utilized the objects and verbs in a temporally smooth order and automatically generated detailed instruction scripts. These scripts comprise 5 scenarios, 25 scenes, 191 activities, and 1370 instructions containing a total of 533 verbs. Please see the supp. document for details. 

### **4.2. Filming** 

**Hardware.** To capture our dataset, we use a customdesigned multi-camera tabletop capture system that consists of 51 RGB cameras uniformly arranged within a cubic capture volume, with each face of the cube containing a 3 _×_ 3 grid of cameras evenly illuminated by LED lights. Inside the cube, a transparent glass surface serves as a supportive platform for objects. Each camera records at 30fps with a resolution of 1280 _×_ 720. Cameras are softwaresynchronized, with the temporal phase misalignment being less than 3 ms. Camera intrinsics and extrinsics are obtained using COLMAP [87, 88] aided by fiducial markers. 

**Filming Process.** During filming, subjects perform actions according to the provided instructions, keeping both hands within the filming area. Instructions are converted to audio and played sequentially to guide the participants, while an operator controls the capture by playing each audio instruction and recording each motion sequence. If the ending state of a performance does not align with the next instruction, a corrective instruction will be given and rerecorded to ensure smooth transitions and reduce annotation efforts. This approach ensures all recorded sequences correspond to a pre-scripted or recorded instruction. 

### **4.3. Action Annotation & Augmentation** 

Though each filmed motion sequence was paired with an instruction, manual annotation was still necessary for two reasons. First, the instructions generated by the LLM occasionally contained inconsistencies or hallucinations. Second, participants might misunderstand the instructions or add unintentional actions during filming. To encourage subjects to act freely and naturally, we intentionally retained these recordings. Annotators then split these sequences into individual clips and annotated any actions not included in the original instructions. This process resulted in a more accurate dataset with matched (description, clip) pairs. In total, we refined the 13k motion sequences into 14k motion clips. 

To further enhance the text descriptions, we used the LLM to rephrase each description 5 times, providing multiple textual variations for each motion clip. This expanded our 14k motion clips into 84k motion-text pairs containing 1,467 unique verbs. The augmentation prompts and examples are provided in the supp. document. 

### **4.4. Hand Motion Estimation** 

GigaHands provides detailed hand motion data, including 2D and 3D hand keypoints and MANO [86] meshes for both hands. Since existing hand shape and pose estimation did not work well enough, we built our own hybrid 

method. We begin by obtaining bounding boxes for the hands across videos using YOLOv8 [85]. Then, 2D keypoints are extracted from the MANO meshes estimated with HaMeR [77] and handedness (left or right) is determined with ViTPose [110]. HaMeR meshes cannot directly be used since they lacks accurate depth. With camera parameters, 2D keypoints are triangulated across views [97] to obtain accurate 3D positions. To ensure temporal smoothness in the sequences, the one-euro filter [16] is applied to the both 2D and 3D keypoints. With the bounding box and 2D & 3D keypoints, we fit the MANO parametric hand model [86] following the EasyMoCap pipeline [1]. This results in a fully automated pipeline for extracting coherent and accurate hand motions. Details and the evaluation of each step are provided in the supp. document. 

### **4.5. Object Motion Estimation** 

GigaHands also provides 3D object motions represented as 3D shape and 6D pose. Given target meshes obtained from pre-scanning or single-view reconstruction, we track these objects with multi-view constraints. First, we segment the target objects from the background in each view. We detect salient objects across the video using DINOv2 [74] on frames subsampled at 1 fps. Using both object text descriptions and rendered template meshes from multiple views, we select the top-k bounding boxes most aligned with the template mesh throughout the video with Grounding DINO [56]. To eliminate false positives, we use OpenCLIP [41] to filter out boxes aligned with negative prompts. With the positive bounding boxes as the prompt, we use SAM2 [84] to segment object masks throughout the video. 

Since no existing method for object pose estimation worked well [75], we decided to build our own robust method that exploits our dense multi-view setting. We use a differentiable rendering approach [83] supervised by the multi-view masks. To initialize the translation and rotation, we first build a radiance field using Instant-NGP [68]. We initialize the object’s translation using the center of the density field. To address potential object symmetries, we use object appearance to initialize the rotation. Following FoundPose [75], we render the template mesh with multiple initial rotations and use DINOv2 features to find the best match, aggregating cross-view information. This process yields precise object motion estimates even in complex, cluttered scenes. More details and the evaluation of each step are provided in the supp. document. 

## **5. Applications & Experiments** 

We demonstrate the utility of GigaHands in several applications that require large-scale data, including text-driven hand motion synthesis (Section 5.1), motion captioning for our dataset (Section 5.2) and for in-the-wild datasets (Section 5.2), and dynamic radiance field reconstruction (Sec- 

Table 2. Quantitative results for text-driven motion synthesis with models trained on different datasets. _upper bound_ indicates performance calculated with the ground truth. We report the mean of 20 evaluations, and _→_ means the closer to the upper bound the better. The model trained on GigaHands performs best on most metrics. 

|Dataset|R Pre|cision|(%)_↑_|MM Dist_↓_|FID_↓_|Div_→_|MM_↑_|
|---|---|---|---|---|---|---|---|
||@1|@2|@3|.||.|.|
|upper bound|64.4|86.2|89.4|2.86|0.045|14.2|-|
|TACO[58]|18.9|37.7|52.9|7.39|11.0|11.1|6.83|
|upper bound|50.4|71.2|81.1|3.67|0.022|9.30|-|
|OakInk2[116]|17.9|31.7|47.9|7.75|19.6|6.88|3.45|
|upper bound|77.4|88.8|91.3|2.96|0.002|11.9|-|
|GigaHands|**31.2 **|**44.7 **|**53.1**|**6.68**|**4.70**|**10.5**|**9.11**|



tion 5.3). More results can be found in the supp. document. 

### **5.1. Text-driven Hand Motion Synthesis** 

Generating diverse and complex motions is crucial for training virtual agents and robotic manipulation. We use GigaHands to train models for text-driven hand motion synthesis, overcoming the limitations of approaches that rely on strict conditions [116] or generate only simple skills [17] due to constrained data. We demonstrate that the scale of GigaHands leads to better performance compared to other datasets [58, 116] and smaller subsets of GigaHands. 

**Training and Evaluation Protocol.** We split GigaHands into train, test, and val sets with a ratio of 16:3:1. From among our annotations, we chose 42 3D keypoints for both hands as the representation for model training (see the supp. document for an analysis of alternative representations). To evaluate the naturalness, diversity, and alignment of generated motions with textual descriptions, we use metrics from [34], including R-Precision, Multimodal Distance (MM Dist), Fr´echet Inception Distance (FID), Diversity (Div.), and Multimodality (MM.). For computing FID and Div., we train a motion autoencoder to define a compressed motion space. For R-Precision, MM Dist, and MM., we employ contrastive learning to create a joint motion-text embedding space, following [34]. Feature extractors are trained independently for each dataset and subset. 

**Results.** We report text to hand motion synthesis performance using the T2M-GPT [119] backbone in Table 2 (see the supp. document for more results on GRU-based [35] and diffusion [103] architectures). Since the evaluation embedding spaces are trained on different test sets, we also evaluate the metrics on ground truth test data to indicate upperbound performance for each test set. Models trained on GigaHands outperform others on all metrics except MM Dist., with higher R-Precision due to better text-motion alignment. Compared to OakInk2 (which also includes textual descriptions for hand motions), GigaHands achieves significantly better FID, Diversity, and Multimodality scores, 



<!-- Start of picture text -->
Open the gate of the  (Dust, Brush, Plate) Make a heart gesture with  Open the book to  Grip the drumsticks  Hold the can of soda<br>Text microwave oven your hands page 200 with both hands<br>Result 1<br>Result 2<br><!-- End of picture text -->

Figure 5. Generated motions from models trained on different datasets. Texts highlighted in green, orange, and blue come from the OakInk2, TACO, and GigaHands datasets. In the bottom two rows, hand meshes highlighted in these colors are generated by models trained on the corresponding datasets. The model trained on GigaHands can generate diverse motions from a single text (right four columns) and accurate motion with text from other datasets (left two columns). Darker color indicates later frame in the sequence. 



Figure 6. Effect of dataset size on motion reconstruction and textto-motion generation performance. The x-axis shows the percentage of training data used (10%, 20%, 50%, 80%, and 100%), and the y-axis displays performance metrics: FID, MM Dist., Top-1, and Top-3 accuracy. Larger datasets consistently improve performance across all metrics, highlighting the benefits of increased data scale. 

likely due to its greater dataset diversity. Figure 5 shows hand motions generated by T2M-GPT trained with GigaHands using text inputs from the test sets of GigaHands, OakInk and TACO. Even without object geometry input, our model generates reasonable hand shapes and poses for object manipulation, benefiting from the diversity of objects in our dataset. Our model can also generate reasonable motion using text from other datsasets, showing the comprehensiveness of GigaHands. 

**Effect of Data Scale.** Figure 6 illustrates the impact of dataset size on motion reconstruction and text-to-motion generation. Based on the T2M-GPT architecture, we train a motion VQ-VAE for reconstruction and a generative pretrained transformer model for text-to-motion generation using 10%, 20%, 50%, 80%, and 100% of the training set, evaluating on the same test set. We evaluate FID, MM Dist., and Top 1 & Top 3 accuracies. Most metrics continually improve with larger datasets, demonstrating the value 

of larger-scale data. 

### **5.2. Hand Motion Captioning** 

Captioning human hand motion helps interpret action intent. We train a motion captioning model on GigaHands and generate captions for its test set motions; we also show examples of captioning in-the-wild datasets. 

**Training and Evaluation Protocol.** We adopt TM2T [35] as the model backbone. For text-motion alignment evaluation, we utilize R-Precision and MM Dist., employing the same embedding space described in Section 5.1. To evaluate alignment with the ground-truth text annotations, we use BLEU [76], ROUGE [53], and BERTScore [121]. Since our dataset has diverse verbs, we evaluate text diversity with distinct-n [51] and Pairwise BLEU [94]. Since TACO lacks text annotations, we use its triplet labels (<action, tool, object>) as scripts, transforming motion captioning in TACO into a classification task. 

Table 3. Quantitative evaluation for motion captioning with models trained on different datasets. GigaHands performs best on most metrics. 

|Datasets|RP@1(%)_↑_|RP@2(%)_↑_|RP@3(%)_↑_|MM Dist_↓_|
|---|---|---|---|---|
|upper bound|64.4|86.2|94.2|2.86|
|TACO[58]|43.5|59.6|68.5|5.84|
|upper bound|51.1|69.5|79.6|3.67|
|Oakink2[116]|40.4|58.8|68.2|**4.55**|
|upper bound|75.3|89.1|93.9|2.87|
|GigaHands|**57.0**|**66.1**|**69.8**|5.37|



|Table 4.<br>BERTScore <br>datasets. Gig|Pairewise<br>for motion<br>aHands perf|-BLEU, BL<br> captioning <br>orms best on|EU@4,<br>ROUGE, distin<br> with models trained o<br>most metrics.|ct-n,<br>and<br>n different|
|---|---|---|---|---|
|Datasets|P-B_↓_|B@4_↑_R_↑_|dist.-1(%)_↑_dist.-2_↑_(%|) BScore_↑_|
|TACO [58]|4.59|39.4 **61.2**|2.03<br>6.35|**57.1**|
|Oakink2 [1|16] 8.21|39.9 56.3|2.76<br>6.82|35.3|
|GigaHands|**0.916 **|**43.1** 57.7|**15.3**<br>**36.9**|55.4|





<!-- Start of picture text -->
Stir in the yellow mug with  (Cut, Knife, Plate) Pour hot water from the  Uncap the pen Grab the watering bottle<br>the spoon. kettle into the teapot<br>Stir in the blue cup with the  (Cut, Knife, Plate) Fill the teacup with tea  Twist off the pen Take hold of the watering<br>rod from the kettle bottle<br>Stir the tea and sugar  Chop the apple into smaller  Dispense the tea into the  Remove the cap from the  Pick up the watering bottle<br>together with the teaspoon  segments teacup from the kettle highlighter<br>until well mixed<br>motion<br>GT<br>#1<br>#2<br><!-- End of picture text -->

Figure 7. **Motion captioning results with different datasets.** Each column shows a motion sequence, its ground truth text description, and two generated texts. Hand motions highlighted in green, orange, and blue come from OakInk2, TACO, and GigaHands, respectively. Texts highlighted in these colors are generated by models trained on the corresponding datasets. The model trained on GigaHands generates diverse captions from a single motion (right three columns) and accurately captions motions from other datasets (left two columns). 



<!-- Start of picture text -->
view 1 view 2 view 1 view 2<br>timestep 1 timestep 2<br>GT<br>2DGS<br>zoom-in<br><!-- End of picture text -->

Figure 8. Synthesized test views using 2DGS for the motion ‘zip up the pants,’ displayed at two timesteps and from two viewpoints. The synthesized views faithfully reconstruct the scene by leveraging the ample camera views provided by GigaHands. 

building dynamic radiance fields. From the 51 views provided, we remove 12 camera views due to lighting issues and randomly select one view as the test view, resulting in 38 views used for training. We segment consistent object and hand masks throughout the video as described in Section 4.5. We then fit 2DGS [40] for frame-wise radiance field reconstruction, initializing each frame with the previous frame for temporal consistency. Figure 8 shows an example of synthesized test views for a motion clip. Notably, the pants are a non-rigid object that cannot be easily tracked, but GigaHands provides ample camera views for capturing non-rigid objects (more results in supp. document). 

**Hand Motion Captioning for GigaHands** Figure 7 shows examples of generated 3D motion captions. The model trained on GigaHands generates diverse and accurate captions. Though objects are not present in the input, the model still generates captions which include reasonable object descriptions. Table 3 and Table 4 report the quantitative performance of models trained on different datasets [58, 116]. The model trained on GigaHands achieves superior motion-text alignment, particularly in Pairwise BLEU and distinct-n, which reflect caption diversity. While our accuracy is marginally lower compared to the simple triplet captioning in TACO, our approach produces richer and more varied captions. 

**3D Hand Motion Captioning for Unlabeled Datasets** 

GigaHands’s large variety motions and associated annotations allows models trained on it to caption other 3D hand motion datasets. Fig. 7 shows some examples using the model trained on GigaHands to caption motions from TACO and OakInk2 datasets after aligning their motion range with GigaHands. This model trained with GigaHands generates finer-granularity captions for these other datasets. 

### **5.3. Dynamic Radiance Field Reconstruction** 

Unlike existing hand activity datasets, GigaHands provides dense camera views. This enables new applications, such as 

## **6. Conclusion** 

We present GigaHands, a massive annotated dataset of bimanual hand activities. The dataset contains 14k motion clips with 3D hand and object motions from 56 subjects interacting with 417 real-world objects, all captured from 51 camera views. It provides 183 million unique image frames and 84k textual descriptions, enabling a wide range of applications. We demonstrated how the scale and diversity of the dataset benefit text-driven motion synthesis and motion captioning, both within the dataset and on other data. Additionally, we have shown that GigaHands enables dynamic radiance field reconstruction, opening possibilities for downstream tasks. 

**Limitations and Future Directions.** Despite its scale and diversity, GigaHands has limitations. The studio setting confines data collection to a limited space, making it challenging to accurately capture motions that require larger environments. While we can track rigid objects and object parts, fully automatic tracking of articulated and non-rigid objects remains challenging. Moreover, although we have showcased applications in motion synthesis and captioning, further research could explore how the dataset’s scale and diversity can enhance robotic manipulation and humancomputer interaction tasks. 

## **Acknowledgement** 

This research was supported by AFOSR grant FA9550-211-0214, NSF CAREER grant #2143576, and ONR DURIP grant N00014-23-1-2804. We would like to thank the OpenAI Research Access Program for API support and extend our gratitude to Ellie Pavlick, Tianran Zhang, Carmen Yu, Angela Xing, Chandradeep Pokhariya, Sudarshan Harithas, Hongyu Li, Chaerin Min, Xindi Qu, Xiaoquan Liu, Hao Sun, Melvin He and Brandon Woodard. 

## **References** 

- [1] Easymocap - make human motion capture easier. Github, 2021. 6 

- [2] AR Code, Augmented Reality QR Codes — ar-code.com. https://ar-code.com/, 2024. [Accessed 05-112024]. 4 

- [3] Meshy Docs — docs.meshy.ai. https://docs. meshy.ai/image-to-3d, 2024. [Accessed 13-112024]. 4 

- [4] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. _arXiv preprint arXiv:2303.08774_ , 2023. 5 

- [5] Heni Ben Amor, Oliver Kroemer, Ulrich Hillenbrand, Gerhard Neumann, and Jan Peters. Generalization of human grasping for multi-fingered robot hands. In _2012 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 2043–2050. IEEE, 2012. 2 

- [6] Mykhaylo Andriluka, Leonid Pishchulin, Peter Gehler, and Bernt Schiele. 2d human pose estimation: New benchmark and state of the art analysis. In _Proceedings of the IEEE Conference on computer Vision and Pattern Recognition_ , pages 3686–3693, 2014. 3 

- [7] Yunfei Bai and C Karen Liu. Dexterous manipulation using both palm and fingers. In _2014 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 1560– 1565. IEEE, 2014. 2 

- [8] Prithviraj Banerjee, Sindi Shkodrani, Pierre Moulon, Shreyas Hampali, Fan Zhang, Jade Fountain, Edward Miller, Selen Basol, Richard Newcombe, Robert Wang, et al. Introducing hot3d: An egocentric dataset for 3d hand and object tracking. _arXiv preprint arXiv:2406.09598_ , 2024. 2, 3 

- [9] Samarth Brahmbhatt, Cusuh Ham, Charles C Kemp, and James Hays. Contactdb: Analyzing and predicting grasp contact via thermal imaging. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 8709–8719, 2019. 3 

- [10] Samarth Brahmbhatt, Ankur Handa, James Hays, and Dieter Fox. Contactgrasp: Functional multi-finger grasp synthesis from contact. In _2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 2386–2393. IEEE, 2019. 2 

- [11] Samarth Brahmbhatt, Chengcheng Tang, Christopher D Twigg, Charles C Kemp, and James Hays. Contactpose: 

A dataset of grasps with object contact and hand pose. In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XIII 16_ , pages 361–378. Springer, 2020. 3 

- [12] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea Finn, Keerthana Gopalakrishnan, Karol Hausman, Alex Herzog, Jasmine Hsu, et al. Rt-1: Robotics transformer for real-world control at scale. _arXiv preprint arXiv:2212.06817_ , 2022. 2 

- [13] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, et al. Rt-2: Vision-language-action models transfer web knowledge to robotic control. _arXiv preprint arXiv:2307.15818_ , 2023. 2 

- [14] Gereon H B¨uscher, Risto K˜oiva, Carsten Sch¨urmann, Robert Haschke, and Helge J Ritter. Flexible and stretchable fabric-based tactile sensor. _Robotics and Autonomous Systems_ , 63:244–252, 2015. 3 

- [15] Zhe Cao, Ilija Radosavovic, Angjoo Kanazawa, and Jitendra Malik. Reconstructing hand-object interactions in the wild. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 12417–12426, 2021. 3 

- [16] G´ery Casiez, Nicolas Roussel, and Daniel Vogel. 1 ~~C~~ filter: a simple speed-based low-pass filter for noisy input in interactive systems. In _Proceedings of the SIGCHI Conference on Human Factors in Computing Systems_ , pages 2527–2530, 2012. 6 

- [17] Junuk Cha, Jihyeon Kim, Jae Shin Yoon, and Seungryul Baek. Text2hoi: Text-guided 3d motion generation for hand-object interaction. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 1577–1585, 2024. 3, 6 

- [18] Yu-Wei Chao, Wei Yang, Yu Xiang, Pavlo Molchanov, Ankur Handa, Jonathan Tremblay, Yashraj S Narang, Karl Van Wyk, Umar Iqbal, Stan Birchfield, et al. Dexycb: A benchmark for capturing hand grasping of objects. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 9044–9053, 2021. 3 

- [19] Sammy Christen, Muhammed Kocabas, Emre Aksan, Jemin Hwangbo, Jie Song, and Otmar Hilliges. D-grasp: Physically plausible dynamic grasp synthesis for handobject interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 20577–20586, 2022. 2 

- [20] Sammy Christen, Shreyas Hampali, Fadime Sener, Edoardo Remelli, Tomas Hodan, Eric Sauser, Shugao Ma, and Bugra Tekin. Diffh2o: Diffusion-based synthesis of handobject interactions from textual descriptions. _arXiv preprint arXiv:2403.17827_ , 2024. 2 

- [21] Enric Corona, Albert Pumarola, Guillem Alenya, Francesc Moreno-Noguer, and Gr´egory Rogez. Ganhand: Predicting human grasp affordances in multi-object scenes. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 5031–5041, 2020. 3 

- [22] Dima Damen, Hazel Doughty, Giovanni Maria Farinella, Sanja Fidler, Antonino Furnari, Evangelos Kazakos, Davide Moltisanti, Jonathan Munro, Toby Perrett, Will Price, 

et al. Scaling egocentric vision: The epic-kitchens dataset. In _Proceedings of the European conference on computer vision (ECCV)_ , pages 720–736, 2018. 2, 3 

- [23] Dima Damen, Hazel Doughty, Giovanni Maria Farinella, Antonino Furnari, Evangelos Kazakos, Jian Ma, Davide Moltisanti, Jonathan Munro, Toby Perrett, Will Price, et al. Rescaling egocentric vision: Collection, pipeline and challenges for epic-kitchens-100. _International Journal of Computer Vision_ , pages 1–23, 2022. 2, 3 

- [24] Ahmad Darkhalil, Dandan Shan, Bin Zhu, Jian Ma, Amlan Kar, Richard Higgins, Sanja Fidler, David Fouhey, and Dima Damen. Epic-kitchens visor benchmark: Video segmentations and object relations. _Advances in Neural Information Processing Systems_ , 35:13745–13758, 2022. 3 

- [25] Matt Deitke, Ruoshi Liu, Matthew Wallingford, Huong Ngo, Oscar Michel, Aditya Kusupati, Alan Fan, Christian Laforte, Vikram Voleti, Samir Yitzhak Gadre, et al. Objaverse-xl: A universe of 10m+ 3d objects. _Advances in Neural Information Processing Systems_ , 36, 2024. 2 

- [26] Christian RG Dreher, Mirko W¨achter, and Tamim Asfour. Learning object-action relations from bimanual human demonstration using graph networks. _IEEE Robotics and Automation Letters_ , 5(1):187–194, 2019. 3 

- [27] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. _arXiv preprint arXiv:2407.21783_ , 2024. 2 

- [28] Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed Kocabas, Manuel Kaufmann, Michael J Black, and Otmar Hilliges. Arctic: A dataset for dexterous bimanual handobject manipulation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 12943–12954, 2023. 2, 3 

- [29] Guillermo Garcia-Hernando, Shanxin Yuan, Seungryul Baek, and Tae-Kyun Kim. First-person hand action benchmark with rgb-d videos and 3d hand pose annotations. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 409–419, 2018. 2, 3 

- [30] Raghav Goyal, Samira Ebrahimi Kahou, Vincent Michalski, Joanna Materzynska, Susanne Westphal, Heuna Kim, Valentin Haenel, Ingo Fruend, Peter Yianilos, Moritz Mueller-Freitag, et al. The” something something” video database for learning and evaluating visual common sense. In _Proceedings of the IEEE international conference on computer vision_ , pages 5842–5850, 2017. 2, 3 

- [31] Patrick Grady, Chengcheng Tang, Samarth Brahmbhatt, Christopher D Twigg, Chengde Wan, James Hays, and Charles C Kemp. Pressurevision: estimating hand pressure from a single rgb image. In _European Conference on Computer Vision_ , pages 328–345. Springer, 2022. 3 

- [32] Kristen Grauman, Andrew Westbury, Eugene Byrne, Zachary Chavis, Antonino Furnari, Rohit Girdhar, Jackson Hamburger, Hao Jiang, Miao Liu, Xingyu Liu, et al. Ego4d: Around the world in 3,000 hours of egocentric video. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 18995–19012, 2022. 2, 3, 4, 5 

- [33] Kristen Grauman, Andrew Westbury, Lorenzo Torresani, Kris Kitani, Jitendra Malik, Triantafyllos Afouras, Kumar Ashutosh, Vijay Baiyya, Siddhant Bansal, Bikram Boote, et al. Ego-exo4d: Understanding skilled human activity from first-and third-person perspectives. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 19383–19400, 2024. 2, 3, 4, 5 

- [34] Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li, and Li Cheng. Generating diverse and natural 3d human motions from text. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 5152–5161, 2022. 6 

- [35] Chuan Guo, Xinxin Zuo, Sen Wang, and Li Cheng. Tm2t: Stochastic and tokenized modeling for the reciprocal generation of 3d human motions and texts. In _ECCV_ , 2022. 6, 7 

- [36] Shreyas Hampali, Mahdi Rad, Markus Oberweger, and Vincent Lepetit. Honnotate: A method for 3d annotation of hand and object poses. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 3196–3206, 2020. 3 

- [37] Shreyas Hampali, Sayan Deb Sarkar, Mahdi Rad, and Vincent Lepetit. Keypoint transformer: Solving joint identification in challenging hands and object interactions for accurate 3d pose estimation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 11090–11100, 2022. 3 

- [38] Shangchen Han, Po-chen Wu, Yubo Zhang, Beibei Liu, Linguang Zhang, Zheng Wang, Weiguang Si, Peizhao Zhang, Yujun Cai, Tomas Hodan, et al. Umetrack: Unified multi-view end-to-end hand tracking for vr. In _SIGGRAPH Asia 2022 conference papers_ , pages 1–9, 2022. 2 

- [39] Yana Hasson, Gul Varol, Dimitrios Tzionas, Igor Kalevatykh, Michael J Black, Ivan Laptev, and Cordelia Schmid. Learning joint reconstruction of hands and manipulated objects. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 11807– 11816, 2019. 2, 3 

- [40] Binbin Huang, Zehao Yu, Anpei Chen, Andreas Geiger, and Shenghua Gao. 2d gaussian splatting for geometrically accurate radiance fields. In _ACM SIGGRAPH 2024 Conference Papers_ , pages 1–11, 2024. 8 

- [41] Gabriel Ilharco, Mitchell Wortsman, Ross Wightman, Cade Gordon, Nicholas Carlini, Rohan Taori, Achal Dave, Vaishaal Shankar, Hongseok Namkoong, John Miller, Hannaneh Hajishirzi, Ali Farhadi, and Ludwig Schmidt. Openclip, 2021. If you use this software, please cite it as below. 6 

- [42] Juntao Jian, Xiuping Liu, Manyi Li, Ruizhen Hu, and Jian Liu. Affordpose: A large-scale dataset of hand-object interactions with affordance-driven hand pose. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 14713–14724, 2023. 3 

- [43] Sheng Jin, Lumin Xu, Jin Xu, Can Wang, Wentao Liu, Chen Qian, Wanli Ouyang, and Ping Luo. Whole-body human pose estimation in the wild. In _Computer Vision– ECCV 2020: 16th European Conference, Glasgow, UK, Au-_ 

_gust 23–28, 2020, Proceedings, Part IX 16_ , pages 196–214. Springer, 2020. 3 

- [44] Yitong Jin, Zhiping Qiu, Yi Shi, Shuangpeng Sun, Chongwu Wang, Donghao Pan, Jiachen Zhao, Zhenghao Liang, Yuan Wang, Xiaobing Li, et al. Audio matters too! enhancing markerless motion capture with audio signals for string performance capture. _ACM Transactions on Graphics (TOG)_ , 43(4):1–10, 2024. 3 

- [45] Hanbyul Joo, Tomas Simon, and Yaser Sheikh. Total capture: A 3d deformation model for tracking faces, hands, and bodies. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 8320–8329, 2018. 3 

- [46] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, et al. Openvla: An open-source vision-language-action model. _arXiv preprint arXiv:2406.09246_ , 2024. 2 

- [47] Franziska Krebs, Andre Meixner, Isabel Patzer, and Tamim Asfour. The kit bimanual manipulation dataset. In _2020 IEEE-RAS 20th International Conference on Humanoid Robots (Humanoids)_ , pages 499–506. IEEE, 2021. 3 

- [48] Taein Kwon, Bugra Tekin, Jan St¨uhmer, Federica Bogo, and Marc Pollefeys. H2o: Two hands manipulating objects for first person interaction recognition. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 10138–10148, 2021. 3 

- [49] Gilwoo Lee, Zhiwei Deng, Shugao Ma, Takaaki Shiratori, Siddhartha S Srinivasa, and Yaser Sheikh. Talking with hands 16.2 m: A large-scale dataset of synchronized bodyfinger motion and audio for conversational motion analysis and synthesis. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 763–772, 2019. 3 

- [50] Alexander Lex, Nils Gehlenborg, Hendrik Strobelt, Romain Vuillemot, and Hanspeter Pfister. Upset: visualization of intersecting sets. _IEEE transactions on visualization and computer graphics_ , 20(12):1983–1992, 2014. 4 

- [51] Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, and Bill Dolan. A diversity-promoting objective function for neural conversation models. _arXiv preprint arXiv:1510.03055_ , 2015. 7 

- [52] Yin Li, Miao Liu, and James M Rehg. In the eye of the beholder: Gaze and actions in first person video. _IEEE transactions on pattern analysis and machine intelligence_ , 45 (6):6731–6747, 2021. 2, 3 

- [53] Chin-Yew Lin. Rouge: A package for automatic evaluation of summaries. In _Text summarization branches out_ , pages 74–81, 2004. 7 

- [54] Jing Lin, Ailing Zeng, Shunlin Lu, Yuanhao Cai, Ruimao Zhang, Haoqian Wang, and Lei Zhang. Motion-x: A largescale 3d expressive whole-body human motion dataset. _Advances in Neural Information Processing Systems_ , 36, 2024. 3 

- [55] Haiyang Liu, Zihao Zhu, Naoya Iwamoto, Yichen Peng, Zhengqing Li, You Zhou, Elif Bozkurt, and Bo Zheng. Beat: A large-scale semantic and emotional multi-modal dataset for conversational gestures synthesis. In _European_ 

_conference on computer vision_ , pages 612–630. Springer, 2022. 2, 3 

- [56] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Chunyuan Li, Jianwei Yang, Hang Su, Jun Zhu, et al. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. _arXiv preprint arXiv:2303.05499_ , 2023. 6 

- [57] Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, and Li Yi. Hoi4d: A 4d egocentric dataset for category-level human-object interaction. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21013–21022, 2022. 2, 3 

- [58] Yun Liu, Haolin Yang, Xu Si, Ling Liu, Zipeng Li, Yuxiang Zhang, Yebin Liu, and Li Yi. Taco: Benchmarking generalizable bimanual tool-action-object understanding. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21740–21751, 2024. 2, 3, 5, 6, 7, 8 

- [59] Xintao Lv, Liang Xu, Yichao Yan, Xin Jin, Congsheng Xu, Shuwen Wu, Yifan Liu, Lincheng Li, Mengxiao Bi, Wenjun Zeng, et al. Himo: A new benchmark for full-body human interacting with multiple objects. In _European Conference on Computer Vision_ , pages 300–318. Springer, 2025. 2, 3 

- [60] Priyanka Mandikal and Kristen Grauman. Learning dexterous grasping with object-centric visual affordances. In _2021 IEEE international conference on robotics and automation (ICRA)_ , pages 6169–6176. IEEE, 2021. 2 

- [61] R McKee, D McKee, D Alexander, and E Paillat. Nz sign language exercises. deaf studies department of victoria university of wellington, 2024. 3 

- [62] Antoine Miech, Dimitri Zhukov, Jean-Baptiste Alayrac, Makarand Tapaswi, Ivan Laptev, and Josef Sivic. Howto100m: Learning a text-video embedding by watching hundred million narrated video clips. In _Proceedings of the IEEE/CVF international conference on computer vision_ , pages 2630–2640, 2019. 2, 3 

- [63] Andrew T Miller and Peter K Allen. Graspit! a versatile simulator for robotic grasping. _IEEE Robotics & Automation Magazine_ , 11(4):110–122, 2004. 2 

- [64] Chaerin Min and Srinath Sridhar. Genheld: Generating and editing handheld objects. _arXiv preprint arXiv:2406.05059_ , 2024. 3 

- [65] Gyeongsik Moon, Shoou-I Yu, He Wen, Takaaki Shiratori, and Kyoung Mu Lee. Interhand2. 6m: A dataset and baseline for 3d interacting hand pose estimation from a single rgb image. In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XX 16_ , pages 548–564. Springer, 2020. 3 

- [66] Franziska Mueller, Dushyant Mehta, Oleksandr Sotnychenko, Srinath Sridhar, Dan Casas, and Christian Theobalt. Real-time hand tracking under occlusion from an egocentric rgb-d sensor. In _Proceedings of the IEEE international conference on computer vision_ , pages 1154–1163, 2017. 2, 3 

- [67] Franziska Mueller, Florian Bernard, Oleksandr Sotnychenko, Dushyant Mehta, Srinath Sridhar, Dan Casas, and 

Christian Theobalt. Ganerated hands for real-time 3d hand tracking from monocular rgb. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 49–59, 2018. 3 

- [68] Thomas M¨uller, Alex Evans, Christoph Schied, and Alexander Keller. Instant neural graphics primitives with a multiresolution hash encoding. _ACM transactions on graphics (TOG)_ , 41(4):1–15, 2022. 6 

- [69] Tushar Nagarajan, Christoph Feichtenhofer, and Kristen Grauman. Grounded human-object interaction hotspots from video. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 8688–8697, 2019. 3 

- [70] Supreeth Narasimhaswamy, Zhengwei Wei, Yang Wang, Justin Zhang, and Minh Hoai. Contextual attention for hand detection in the wild. In _Proceedings of the IEEE/CVF international conference on computer vision_ , pages 9567– 9576, 2019. 3 

- [71] Evonne Ng, Javier Romero, Timur Bagautdinov, Shaojie Bai, Trevor Darrell, Angjoo Kanazawa, and Alexander Richard. From audio to photoreal embodiment: Synthesizing humans in conversations. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 1001–1010, 2024. 3 

- [72] Takehiko Ohkawa, Kun He, Fadime Sener, Tomas Hodan, Luan Tran, and Cem Keskin. Assemblyhands: Towards egocentric activity understanding via 3d hand pose estimation. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 12999–13008, 2023. 3 

- [73] Abby O’Neill, Abdul Rehman, Abhinav Gupta, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, et al. Open x-embodiment: Robotic learning datasets and rt-x models. _arXiv preprint arXiv:2310.08864_ , 2023. 2 

- [74] Maxime Oquab, Timoth´ee Darcet, Th´eo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, et al. Dinov2: Learning robust visual features without supervision. _arXiv preprint arXiv:2304.07193_ , 2023. 6 

- [75] Evin Pınar Ornek,<sup>¨</sup> Yann Labb´e, Bugra Tekin, Lingni Ma, Cem Keskin, Christian Forster, and Tomas Hodan. Foundpose: Unseen object pose estimation with foundation features. _arXiv preprint arXiv:2311.18809_ , 2023. 6 

- [76] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine translation. In _Proceedings of the 40th annual meeting of the Association for Computational Linguistics_ , pages 311– 318, 2002. 7 

- [77] Georgios Pavlakos, Dandan Shan, Ilija Radosavovic, Angjoo Kanazawa, David Fouhey, and Jitendra Malik. Reconstructing hands in 3d with transformers. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 9826–9836, 2024. 3, 6 

- [78] Tu-Hoa Pham, Nikolaos Kyriazis, Antonis A Argyros, and Abderrahmane Kheddar. Hand-object contact force estimation from markerless visual tracking. _IEEE transactions_ 

_on pattern analysis and machine intelligence_ , 40(12):2883– 2896, 2017. 3 

- [79] Hamed Pirsiavash and Deva Ramanan. Detecting activities of daily living in first-person camera views. In _2012 IEEE conference on computer vision and pattern recognition_ , pages 2847–2854. IEEE, 2012. 2, 3 

- [80] Chandradeep Pokhariya, Ishaan Nikhil Shah, Angela Xing, Zekun Li, Kefan Chen, Avinash Sharma, and Srinath Sridhar. Manus: Markerless grasp capture using articulated 3d gaussians. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 2197– 2208, 2024. 3 

- [81] Albert Pumarola, Enric Corona, Gerard Pons-Moll, and Francesc Moreno-Noguer. D-nerf: Neural radiance fields for dynamic scenes. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 10318–10327, 2021. 2 

- [82] Chen Qian, Xiao Sun, Yichen Wei, Xiaoou Tang, and Jian Sun. Realtime and robust hand tracking from depth. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 1106–1113, 2014. 3 

- [83] Nikhila Ravi, Jeremy Reizenstein, David Novotny, Taylor Gordon, Wan-Yen Lo, Justin Johnson, and Georgia Gkioxari. Accelerating 3d deep learning with pytorch3d. _arXiv:2007.08501_ , 2020. 6 

- [84] Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman R¨adle, Chloe Rolland, Laura Gustafson, et al. Sam 2: Segment anything in images and videos. _arXiv preprint arXiv:2408.00714_ , 2024. 6 

- [85] Dillon Reis, Jordan Kupec, Jacqueline Hong, and Ahmad Daoudi. Real-time flying object detection with yolov8. _arXiv preprint arXiv:2305.09972_ , 2023. 6 

- [86] Javier Romero, Dimitrios Tzionas, and Michael J Black. Embodied hands: Modeling and capturing hands and bodies together. _arXiv preprint arXiv:2201.02610_ , 2022. 2, 3, 5, 6 

- [87] Johannes Lutz Sch¨onberger and Jan-Michael Frahm. Structure-from-motion revisited. In _Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2016. 5 

- [88] Johannes Lutz Sch¨onberger, Enliang Zheng, Marc Pollefeys, and Jan-Michael Frahm. Pixelwise view selection for unstructured multi-view stereo. In _European Conference on Computer Vision (ECCV)_ , 2016. 5 

- [89] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. Laion-5b: An open large-scale dataset for training next generation image-text models. _Advances in Neural Information Processing Systems_ , 35:25278–25294, 2022. 2 

- [90] Fadime Sener, Dibyadip Chatterjee, Daniel Shelepov, Kun He, Dipika Singhania, Robert Wang, and Angela Yao. Assembly101: A large-scale multi-view video dataset for understanding procedural activities. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21096–21106, 2022. 3 

- [91] Dandan Shan, Jiaqi Geng, Michelle Shu, and David F Fouhey. Understanding human hands in contact at internet scale. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 9869–9878, 2020. 2, 3 

- [92] Toby Sharp, Cem Keskin, Duncan Robertson, Jonathan Taylor, Jamie Shotton, David Kim, Christoph Rhemann, Ido Leichter, Alon Vinnikov, Yichen Wei, et al. Accurate, robust, and flexible real-time hand tracking. In _Proceedings of the 33rd annual ACM conference on human factors in computing systems_ , pages 3633–3642, 2015. 3 

- [93] Qijin She, Ruizhen Hu, Juzhan Xu, Min Liu, Kai Xu, and Hui Huang. Learning high-dof reaching-and-grasping via dynamic representation of gripper-object interaction. _arXiv preprint arXiv:2204.13998_ , 2022. 2 

- [94] Tianxiao Shen, Myle Ott, Michael Auli, and Marc’Aurelio Ranzato. Mixture models for diverse machine translation: Tricks of the trade. In _International conference on machine learning_ , pages 5719–5728. PMLR, 2019. 7 

- [95] Gunnar A Sigurdsson, Abhinav Gupta, Cordelia Schmid, Ali Farhadi, and Karteek Alahari. Charades-ego: A largescale dataset of paired third and first person videos. _arXiv preprint arXiv:1804.09626_ , 2018. 2 

- [96] Tomas Simon, Hanbyul Joo, Iain Matthews, and Yaser Sheikh. Hand keypoint detection in single images using multiview bootstrapping. In _Proceedings of the IEEE conference on Computer Vision and Pattern Recognition_ , pages 1145–1153, 2017. 3 

- [97] Srinath Sridhar, Antti Oulasvirta, and Christian Theobalt. Interactive markerless articulated hand motion tracking using rgb and depth data. In _Proceedings of the IEEE international conference on computer vision_ , pages 2456–2463, 2013. 3, 6 

- [98] Srinath Sridhar, Franziska Mueller, Michael Zollh¨ofer, Dan Casas, Antti Oulasvirta, and Christian Theobalt. Real-time joint tracking of a hand manipulating an object from rgbd input. In _Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part II 14_ , pages 294–310. Springer, 2016. 3 

- [99] Xiao Sun, Yichen Wei, Shuang Liang, Xiaoou Tang, and Jian Sun. Cascaded hand pose regression. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 824–832, 2015. 3 

- [100] Subramanian Sundaram, Petr Kellnhofer, Yunzhu Li, JunYan Zhu, Antonio Torralba, and Wojciech Matusik. Learning the signatures of the human grasp using a scalable tactile glove. _Nature_ , 569(7758):698–702, 2019. 3 

- [101] Omid Taheri, Nima Ghorbani, Michael J Black, and Dimitrios Tzionas. Grab: A dataset of whole-body human grasping of objects. In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IV 16_ , pages 581–600. Springer, 2020. 2, 3, 4 

- [102] Danhang Tang, Hyung Jin Chang, Alykhan Tejani, and TaeKyun Kim. Latent regression forest: Structured estimation of 3d articulated hand posture. In _Proceedings of the_ 

   - _IEEE conference on computer vision and pattern recognition_ , pages 3786–3793, 2014. 3 

- [103] Guy Tevet, Sigal Raab, Brian Gordon, Yoni Shafir, Daniel Cohen-or, and Amit Haim Bermano. Human motion diffusion model. In _The Eleventh International Conference on Learning Representations_ , 2023. 6 

- [104] Jonathan Tompson, Murphy Stein, Yann Lecun, and Ken Perlin. Real-time continuous pose recovery of human hands using convolutional networks. _ACM Transactions on Graphics (ToG)_ , 33(5):1–10, 2014. 3 

- [105] Dylan Turpin, Liquan Wang, Eric Heiden, Yun-Chun Chen, Miles Macklin, Stavros Tsogkas, Sven Dickinson, and Animesh Garg. Grasp’d: Differentiable contact-rich grasp synthesis for multi-fingered hands. In _European Conference on Computer Vision_ , pages 201–221. Springer, 2022. 2 

- [106] Dimitrios Tzionas, Luca Ballan, Abhilash Srikantha, Pablo Aponte, Marc Pollefeys, and Juergen Gall. Capturing hands in action using discriminative salient points and physics simulation. _International Journal of Computer Vision_ , 118: 172–193, 2016. 3 

- [107] Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. _Journal of machine learning research_ , 9 (11), 2008. 4 

- [108] Frank R Wilson. _The hand: How its use shapes the brain, language, and human culture_ . Vintage, 1999. 2 

- [109] Wei Xie, Zhipeng Yu, Zimeng Zhao, Binghui Zuo, and Yangang Wang. Hmdo: Markerless multi-view hand manipulation capture with deformable objects. _Graphical Models_ , 127:101178, 2023. 3 

- [110] Yufei Xu, Jing Zhang, Qiming Zhang, and Dacheng Tao. Vitpose: Simple vision transformer baselines for human pose estimation. _Advances in Neural Information Processing Systems_ , 35:38571–38584, 2022. 6 

- [111] Lixin Yang, Kailin Li, Xinyu Zhan, Fei Wu, Anran Xu, Liu Liu, and Cewu Lu. Oakink: A large-scale knowledge repository for understanding hand-object interaction. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 20953–20962, 2022. 2, 3 

- [112] Ruolin Ye, Wenqiang Xu, Zhendong Xue, Tutian Tang, Yanfeng Wang, and Cewu Lu. H2o: A benchmark for visual human-human object handover analysis. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 15762–15771, 2021. 3 

- [113] Youngwoo Yoon, Pieter Wolfert, Taras Kucherenko, Carla Viegas, Teodor Nikolov, Mihail Tsakov, and Gustav Eje Henter. The genea challenge 2022: A large evaluation of data-driven co-speech gesture generation. In _Proceedings of the 2022 International Conference on Multimodal Interaction_ , pages 736–747, 2022. 3 

- [114] Zhengdi Yu, Shaoli Huang, Yongkang Cheng, and Tolga Birdal. Signavatars: A large-scale 3d sign language holistic motion dataset and benchmark, 2024. 3 

- [115] Shanxin Yuan, Qi Ye, Bjorn Stenger, Siddhant Jain, and Tae-Kyun Kim. Bighand2. 2m benchmark: Hand pose dataset and state of the art analysis. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 4866–4874, 2017. 3 

- [116] Xinyu Zhan, Lixin Yang, Yifei Zhao, Kangrui Mao, Hanlin Xu, Zenan Lin, Kailin Li, and Cewu Lu. Oakink2: A dataset of bimanual hands-object manipulation in complex task completion. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 445–456, 2024. 2, 3, 4, 5, 6, 7, 8 

for markerless capture of hand pose and shape from single rgb images. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 813–822, 2019. 3 

- [117] Hui Zhang, Sammy Christen, Zicong Fan, Otmar Hilliges, and Jie Song. Graspxl: Generating grasping motions for diverse objects at scale. _arXiv preprint arXiv:2403.19649_ , 2024. 2 

- [118] Hui Zhang, Sammy Christen, Zicong Fan, Luocheng Zheng, Jemin Hwangbo, Jie Song, and Otmar Hilliges. Artigrasp: Physically plausible synthesis of bi-manual dexterous grasping and articulation. In _2024 International Conference on 3D Vision (3DV)_ , pages 235–246. IEEE, 2024. 2 

- [119] Jianrong Zhang, Yangsong Zhang, Xiaodong Cun, Yong Zhang, Hongwei Zhao, Hongtao Lu, Xi Shen, and Ying Shan. Generating human motion from textual descriptions with discrete representations. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 14730–14740, 2023. 6 

- [120] Siwei Zhang, Qianli Ma, Yan Zhang, Zhiyin Qian, Taein Kwon, Marc Pollefeys, Federica Bogo, and Siyu Tang. Egobody: Human body shape and motion of interacting people from head-mounted devices. In _European conference on computer vision_ , pages 180–200. Springer, 2022. 3 

- [121] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Weinberger, and Yoav Artzi. Bertscore: Evaluating text generation with bert. _arXiv preprint arXiv:1904.09675_ , 2019. 7 

- [122] Wenqian Zhang, Molin Huang, Yuxuan Zhou, Juze Zhang, Jingyi Yu, Jingya Wang, and Lan Xu. Both2hands: Inferring 3d hands from both text prompts and body dynamics. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 2393–2404, 2024. 3 

- [123] Zhongqun Zhang, Hengfei Wang, Ziwei Yu, Yihua Cheng, Angela Yao, and Hyung Jin Chang. Nl2contact: Natural language guided 3d hand-object contact modeling with diffusion model. _arXiv preprint arXiv:2407.12727_ , 2024. 3 

- [124] Chengfeng Zhao, Juze Zhang, Jiashen Du, Ziwei Shan, Junye Wang, Jingyi Yu, Jingya Wang, and Lan Xu. I’m hoi: Inertia-aware monocular capture of 3d human-object interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 729– 741, 2024. 3 

- [125] Zehao Zhu, Jiashun Wang, Yuzhe Qin, Deqing Sun, Varun Jampani, and Xiaolong Wang. Contactart: Learning 3d interaction priors for category-level articulated object and hand poses estimation. In _2024 International Conference on 3D Vision (3DV)_ , pages 201–212. IEEE, 2024. 3 

- [126] Christian Zimmermann and Thomas Brox. Learning to estimate 3d hand pose from single rgb images. In _Proceedings of the IEEE international conference on computer vision_ , pages 4903–4911, 2017. 2, 3 

- [127] Christian Zimmermann, Duygu Ceylan, Jimei Yang, Bryan Russell, Max Argus, and Thomas Brox. Freihand: A dataset 

**Supplementary Material for GigaHands: A Massive Annotated Dataset of Bimanual Hand Activities** 

The supplementary material for GigaHands provides additional details and results to support the main paper. It includes supplementary videos, examples of data and annotations, comprehensive comparisons of dataset statistics, detailed explanations of our hand and object motion tracking methods, elaborations on text instructions and annotations (including prompts and examples), further experiments on text-driven motion synthesis, motion captioning, and dynamic reconstruction. We also provide additional applications on hand-object motion tasks, as well as detailed inspections of the dataset, such as object visualizations, the verb pool, and lists of scenarios and scenes. 

## **Contents** 

|**1. Data and Annotation Example**|**2**|
|---|---|
|**2. Comparison of Dataset Statistics**|**3**|
|**3. Experiments on Text-driven Motion Synthesis**|**3**|
|**4. Experiments on Motion Captioning**|**6**|
|**5. Experiments on Dynamic Reconstruction**|**8**|
|**6. Experiments on Hand-Object Interaction**|**9**|
|**7. Hand Motion Tracking**|**10**|
|**8. Object Motion Tracking**|**11**|
|**9. Text Instructions and Annotations**|**13**|
|9.1. Prompts and Examples for scenario grouping . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>13|
|9.2. Prompts and Examples for Scene structuring<br>. . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>13|
|9.3. Prompts and Examples for instruction scripting . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>15|
|9.4. Annotation Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>15|
|9.5. Prompts and Examples for text augmentation . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>15|
|**10. Dataset Inspection**|**16**|
|10.1. Object Visualization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>16|
|10.2. Verb Pool.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>17|
|10.3. List of Scenarios and Scenes.<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .<br>18|



1 

## **1. Data and Annotation Example** 

Table 1 illustrates the types of annotations we provided for a single motion clip. These include the text instruction, text annotation, augmented annotations, original multi-view RGB videos, 2D and 3D keypoints, 3D hand meshes, hand motions, object masks, textured object meshes, and object motions. 

|type<br>view #1<br>view #2<br>view #3<br>i|
|---|
|instruction<br>Placeyour left-hand fingers on the fretboard of the ukelele to form chords.|
|annotation<br>Placeyour left-hand fingers on the fretboard of the ukelele to form chords.<br>i|
|augmented annotation<br>Position your left-hand fingers on the fretboard to shape chords.<br>Rest your left-hand fingers on the fretboard to create chords.<br>Set your left-hand fingers on the fretboard to assemble chords.<br>Arrange your left-hand fingers on the fretboard to build chords.<br>Useyour left-hand fingers on the fretboard to construct chords.|
|video<br>object masks|
|2D hand keypoints<br>3D hand keypoints<br>3D hand mesh/motion<br>3D object mesh/motion|



Table 1. Annotations for a single motion clip. 

## **2. Comparison of Dataset Statistics** 

Table 2. Comparisons of 3D bimanual motion datasets. Dataset names are highlighted with different colors if it has no text annotations (gray), action type (green), sparse description (red), and dense description (blue). 

|Name|setting<br>|markerles|s hand track. o|bject track|. #mins #|motions|#poses|#views|#frames #|subjects|#object|s #verbs|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|AssemblyHands[22]|studio|✓|semi-auto.|_/_|630|62|203k|12|3.03M|34|_/_|24|
|Ego4D[13]|in-the-wild|✓|_/_|_/_|_/_|_/_|_/_|1|_/_|931|_/_|1452|
|Ego-Exo4D[7]|in-the-wild|✓|manual|_/_|_/_|_/_|**4.4M**|5-6|_/_|**740**|_/_|402|
|HOI4D[17]|in-the-wild|✓|manual|manual|1,333|4k|1.2M|1|2.4M|4|**800**|25|
|ARCTIC[5]|studio|✗|mocap|mocap|121|339|218k|9|2.1M|10|11|✗|
|TACO[18]|studio|✗|mocap|mocap|202|2.3k|363k|13|4.7M|14|196|13|
|OakInk2[39]|studio|✗|mocap|mocap|557|2.8k|993k|4|4.01M|9|75|55|
|HOT3D[3]|studio|✗|mocap|mocap|833|4.1k|1.7M|2-3|3.7M|19|33|✗|
|GigaHands(Ours)|studio|✓|auto|auto|**2,034**|**13.9k**|3.7M|**51**|**183M**|56|417|**1467**|



Table 2 provides a comprehensive comparison of 3D bimanual motion datasets, including their capturing sources, annotation methods, and statistics across various features. The table applies the same method as Figure 2 in the main paper for verb counting. To compile the verb counts, we extracted verbs from several sources: fine-granularity labels from AssemblyHands [22], atomic descriptions from Ego-Exo4D [7], redacted narrations from Ego4D [6], category labels and task definitions from HOI4D [17], action types from TACO [18], task descriptions and affordance annotations from OakInk2, and our own augmented text descriptions from GigaHands. For verb extraction, we parsed sentences using spaCy [11] and collected the verb stems. Verb stems that were misspelled or not recognized as verbs in either WordNet [20] or spaCy’s ‘en ~~c~~ ore ~~w~~ eb ~~s~~ m’ model were removed. Clearly, GigaHands surpasses all other datasets in filming length, number of motion sequences, number of camera views, frame count, and verb count. 

## **3. Experiments on Text-driven Motion Synthesis** 

**Implementation Details** Our framework builds upon the T2M-GPT architecture proposed by [40] and utilizes their publicly available PyTorch codebase<sup>1</sup> . The network comprises a motion VQ-VAE that learns a mapping between motion data and discrete code sequences and a T2M-GPT which generates code indices conditioned on the text description. For the Motion VQ-VAE, the codebook size is set to 512 _×_ 512, with a downsampling rate _l_ = 4. The encoder and decoder is a simple convolutional architecture consisting of 1D convolutions, residual blocks [10], and ReLU activations. Temporal downsampling and upsampling are performed using strided convolutions (stride = 2) and nearest-neighbor interpolation, respectively. We use the AdamW optimizer [19] with [ _β_ 1 _, β_ 2] = [0 _._ 9 _,_ 0 _._ 99], a batch size of 256, and an exponential moving constant _λ_ = 0 _._ 99. The model is trained for the first 200K iterations with a learning rate of 2 _×_ 10<sup>_−_4</sup> , followed by 100K iterations with a reduced learning rate of 1 _×_ 10<sup>_−_5</sup> . Based on our text annotations, we construct a custom word vectorizer utilizing pre-trained 300-dimensional word embedding vectors from GloVe [28]. 

For the T2M-GPT, we employ adopts a transformer architecture [36] consisting of 18 layers with a model dimensionality of 1,024 and 16 attention heads. The maximum length of the code index sequence is capped at 50, with an additional end token incorporated to indicate sequence termination. The optimization of the transformer is performed using the AdamW algorithm [19], configured with hyperparameters [ _β_ 1 _, β_ 2] = [0 _._ 5 _,_ 0 _._ 99] and a batch size of 128. The training process spans 150K iterations with an initial learning rate of 1 _×_ 10<sup>_−_4</sup> , followed by a decay to 5 _×_ 10<sup>_−_6</sup> over an additional 150K iterations. 

To ensure consistency across three datasets—TACO [18], OakInk2 [39], and GigaHands—we standardize the hand representations and motion ranges. First, we extract 3D hand keypoints from the MANO [31] parameters using the MANO Layer<sup>2</sup> . Subsequently, we align the hand orientations such that the fingertips point in the positive z-axis direction. Additionally, we recenter each motion sequence by adjusting the hand positions so that the motion center of both hands is aligned to the origin. 

**Evaluation Metrics** Given the lack of a standard hand motion feature extractor, we train a simple framework consisting of a motion extractor and a text extractor trained under a contrastive learning paradigm, following [8]. The Motion and Text Feature Extractors are designed to learn geometrically close feature vectors for matched text-motion pairs while ensuring separation for mismatched pairs. Specifically, the input text and motion are encoded into semantic vectors _Ft_ and _Fm_ , 

> 1https://github.com/Mael-zys/T2M-GPT 

> 2https://github.com/hassony2/manopth 

respectively, using two distinct bi-directional GRUs. To achieve this, we minimize a contrastive loss that enforces proximity for matched pairs and imposes a margin of separation _m_ for mismatched pairs: 



where _y ∈_ 0 _,_ 1, with _y_ = 1 indicating matched text-motion pairs and _y_ = 0 otherwise. The margin _m_ is set to 10 across all datasets. These feature extractors are independently trained for each dataset to establish an upper bound respectively. 

The trained text and motion feature extractors are utilized to evaluate text-to-motion generation using the metrics proposed in [8]. We denote the ground-truth motion features, generated motion features, and text features derived from the aforementioned feature extractors as _Fgt_ , _Fgen_ , and _Ft_ , respectively. 

**R Precision.** For each generated motion, a text pool is formed with its ground truth text and 31 randomly selected mismatched texts. Euclidean distances between the description feature and motion features are computed and ranked. If the ground truth text ranks in the top-k positions (k=1, 2, 3), it counts as a successful retrieval. The average accuracy over all samples defines the top-k R-precision. 

**Multimodal Distance (MM Dist.)** MM Dist. evaluates the alignment between text embeddings and generated motion features. Given _N_ randomly generated samples, it calculates the average Euclidean distance between each text feature and the corresponding generated motion feature: 



where _Fgen_<sup>_i_and</sup><sup>_F i_</sup> _t_<sup>are the features of the i-th text-motion pair.</sup> 

**Frechet Inception Distance (FID).** FID measures the distributional similarity between real and generated motion features. Features are extracted from ground-truth motions in the test set and generated motions from the corresponding descriptions. FID is computed as: 



where _µgt_ and _µpred_ are mean of _Fgt_ and _Fgen_ . _σ_ is the covariance matrix and Tr denotes the trace of a matrix. **Diversity.** Diversity quantifies the variance across all generated motion sequences in the dataset. From the generated motions, _Sdis_ pairs of motion features are randomly sampled, denoted as _Fgen_<sup>_i_and</sup><sup>_F i_</sup> _gen_<sup>_′_.The diversity is then calculated as:</sup> 



In our experiments, we set _Sdis_ = 300, as suggested in [8]. 

**MultiModality.** MultiModality assesses the diversity of hand motions generated from the same text description. For the _i_ -th text description, 20 motions are generated, and two subsets, each containing 10 motions, are sampled. Denoting the features of the _j_ -th pair for the _i_ -th text description as ( _Fgen_<sup>_i,j, F_</sup> _gen_<sup>_i,j′_), MultiModality is computed as:</sup> 



**Comparison of Different Backbones.** We evaluate the text-to-hand motion synthesis performance on our dataset using three different backbone models: TM2T [9], MDM [35], and T2M-GPT [40], as summarized in Table 3. TM2T comprises a motion VQ-VAE module for motion quantization and an attentive GRU-based model for text-to-motion generation. MDM employs a classifier-free diffusion generative approach. While these models were originally developed for human motion synthesis, we adapted them to generate hand motions on our dataset. 

From Table 3, it is evident that our dataset supports all three backbones effectively. Notably, the state-of-the-art T2MGPT architecture for human motion generation also achieves the best performance on our dataset, demonstrating its superior capability for motion synthesis. 

Table 3. Quantitative results for text-driven motion synthesis with different backbones trained on our dataset. _upper bound_ indicates performance calculated with the ground truth. We repeat the evaluation 20 times and report the averge with 95% confidence interval. 

|Dataset|R<br>@1|Precision(%)<br>@2|_↑_<br>@3|MM Dist._↓_|FID_↓_|Diversity_→_|MultiModality_↑_|
|---|---|---|---|---|---|---|---|
|upper bound|77_._4<sup>_±._002</sup>|88_._8<sup>_±._002</sup>|91_._3<sup>_±._001</sup>|2_._96<sup>_±._005</sup>|0_._002<sup>_±._000</sup>|11_._9<sup>_±._097</sup>|-|
|MDM [35]|22_._5<sup>_±._004</sup>|42_._7<sup>_±._005</sup>|50_._2<sup>_±._005</sup>|7_._81<sup>_±._082</sup>|5_._60<sup>_±._126</sup>|9_._8<sup>_±._088</sup>|8_._52<sup>_±._103</sup>|
|TM2T [9]|24_._1<sup>_±._002</sup>|38_._4<sup>_±._003</sup>|47_._1<sup>_±._004</sup>|9_._28<sup>_±._017</sup>|8_._60<sup>_±._161</sup>|9_._7<sup>_±._065</sup>|6_._29<sup>_±._085</sup>|
|T2M-GPT [40]|**31.2**<sup>_±._003</sup>|**44.7**<sup>_±._004</sup>|**53.1**<sup>_±._004</sup>|**6.68**<sup>_±._023</sup>|**4.70**<sup>_±._078</sup>|**10.5**<sup>_±._090</sup>|**9.11**<sup>_±._255</sup>|



Table 4. Ablation study on different hand motion representations and text annotations for text-driven motion synthesis. _KP_ refers to the 3D hand keypoints representation, while _6D_ denotes the MANO pose parameters encoded in the 6D representation. Numbers in parentheses indicate the quantity of text scripts. _upper bound_ indicates performance calculated with the ground truth. We repeat the evaluation 20 times and report the averge with 95% confidence interval. 

|Dataset|R<br>@1|Precision(%<br>@2|)_↑_<br>@3|MM Dist._↓_|FID_↓_|Diversity_→_|MultiModality_↑_|
|---|---|---|---|---|---|---|---|
|upper bound|73_._3<sup>_±._003</sup>|87_._0<sup>_±._002</sup>|92_._1<sup>_±._001</sup>|3_._29<sup>_±._006</sup>|0_._002<sup>_±._000</sup>|12_._8<sup>_±._067</sup>|-|
|6D (14k)|26_._5<sup>_±._003</sup>|43_._3<sup>_±._004</sup>|52_._3<sup>_±._003</sup>|7_._56<sup>_±._051</sup>|5_._11<sup>_±._183</sup>|9_._7<sup>_±._078</sup>|7_._28<sup>_±._059</sup>|
|6D(84k)|29_._5<sup>_±._003</sup>|**46.9**<sup>_±._004</sup>|**57.3**<sup>_±._004</sup>|7_._04<sup>_±._041</sup>|**4.34**<sup>_±._221</sup>|**11.7**<sup>_±._068</sup>|9_._08<sup>_±._060</sup>|
|upper bound|77_._4<sup>_±._002</sup>|88_._8<sup>_±._002</sup>|91_._3<sup>_±._001</sup>|2_._96<sup>_±._005</sup>|0_._002<sup>_±._000</sup>|11_._9<sup>_±._097</sup>|-|
|KP (14k)|27_._2<sup>_±._003</sup>|40_._1<sup>_±._002</sup>|49_._7<sup>_±._004</sup>|7_._13<sup>_±._020</sup>|5_._20<sup>_±._169</sup>|8_._7<sup>_±._067</sup>|7_._29<sup>_±._085</sup>|
|KP (84k)|**31.2**<sup>_±._003</sup>|44_._7<sup>_±._004</sup>|53_._1<sup>_±._004</sup>|**6.68**<sup>_±._023</sup>|4_._70<sup>_±._078</sup>|10_._5<sup>_±._090</sup>|**9.11**<sup>_±._255</sup>|



**Ablations of Different Motion Representations and Text Annotations.** We further explore the performance of text-tomotion generation using different hand motion representations in Table 4. One approach leverages the 3D hand keypoints derived from MANO parameters, represented as _X ∈_ R<sup>42</sup><sup>_×_3</sup> . The other employs the MANO hand pose parameters _θ ∈_ R<sup>16</sup><sup>_×_6</sup> , encoded in a 6D representation [42]. We also conduct an ablation study to evaluate the impact of the number of text descriptions on text-to-motion generation. In GigaHands, each motion clip is paired with six distinct text descriptions, resulting in a total of 84k annotations. We compare the generation results using 14k annotations versus the full set of 84k annotations, as presented in Table 4. 

The results demonstrate that both the 6D representation and the 3D keypoint representation achieve comparable performance in text-driven hand motion synthesis. This finding suggests that both representations are equally capable of capturing the essential hand motion features required for this task. Nevertheless, incorporating additional text annotations significantly boosts performance across all evaluation metrics. This improvement underscores the importance of enriched textual descriptions in enhancing the semantic alignment between textual inputs and generated hand motions, irrespective of the chosen motion representation. 

**More Qualitative Results.** We present additional qualitative results from our testing sets to demonstrate the effectiveness of text-driven hand motion synthesis in Figure 1. These examples further highlight the ability of our approach to generate semantically aligned hand motions from diverse textual inputs. 

|test_\_train|(F|ID / Diversity|)|
|---|---|---|---|
||GigaHands|Oakink2|TACO|
|GigaHands|6.61 / 10.5|44.8 / 4.01|52.1 / 7.11|
|Oakink2|19.1 / 6.45|19.6 / 6.88|58.1 / 5.04|
|TACO|22.5 / 11.5|33.6 / 9.31|11.0 / 11.1|



Table 5. Cross-dataset evaluation of text-to-motion models trained on different datasets. Each column represents the training dataset, while each row shows the evaluation results on a different dataset. Metrics include FID and Diversity, computed on the test set feature extractor. The ground truth Diversity metrics for GigaHands, Oakink, and TACO are 11.9, 9.30, and 14.2, respectively. 



<!-- Start of picture text -->
off the bread with Saw a small piece  Take out an egg from the carton length of adhesive tapeTear off a suitable  Distribute one of each dollar type to yourself Loosen the selfie stick to prepare for  Dispense a few drops of serum onto your<br>the sawing knife shortening it fingertips<br>Lift the soup to  Scrape the squashed  Hold the box or bottle of  Dab ear cleaning  Snap once with your  Unscrew the cap of<br>the spoon and sipyour mouth using  board into the salad bowlapple from the chopping  cream securely solution onto a rag left hand the cream container<br>Text<br>GT<br>Generated<br>Text<br>GT<br>Generated<br><!-- End of picture text -->

Figure 1. More qualitative results for text-driven motion synthesis on GigaHands. Darker color indicates later frame in the sequence. 

**Cross Validation on different datasets.** To validate the capacity of text-to-To evaluate the generalization ability of textto-motion generation models trained on GigaHands, we conduct cross-dataset validation. Specifically, we train T2M-GPT models on one dataset and evaluate their performance on others. Table 5 presents the quantitative results, where each column indicates the dataset used for training, and each row corresponds to the dataset on which the model is tested. We report the FID and Diversity metrics, computed on the corresponding test dataset’s feature extractor. Since the triplet-based textual annotations in the TACO dataset are coarse, with each triplet corresponding to multiple motion sequences, we employ ChatGPT-4o [2] to refine the captions during testing and select the best-performing generation for each triplet. The results in Table 5 demonstrate that our models achieve competitive performance on unseen datasets, despite being trained on a single dataset. However, due to the simplistic nature of TACO’s annotations, models trained on other datasets struggle to perform well when tested on TACO. 

For OakInk2, object descriptions rely on material and texture distinctions rather than explicit shape descriptions. For example, ”yellow striped bottle” refers to a large plastic jar, whereas ”white bottle” describes a small bottle. This captioning style differs from the textual descriptions in our dataset, leading to a slight performance drop when models trained on our dataset are tested on OakInk2. 

## **4. Experiments on Motion Captioning** 

**Implementation Details.** Our motion captioning framework is also built upon the TM2T [9] architecture, leveraging the same VQ-VAE for motion quantization as used in the text-driven motion synthesis task. For tokenized motion representation, we employ a transformer model to efficiently map hand motions to textual descriptions. The transformers have 4 attention layers, both with 8 attention heads with 512 hidden size. 

When evaluate captioning performance across datasets, we train the VQ-VAE and motion-to-text models separately on TACO [18], OakInk2 [39], and GigaHands. For testing the model’s ability in in-the-wild motion captioning, we first train a VQ-VAE using all datasets combined, followed by training the motion-to-text model exclusively on GigaHands. When generating captions for other datasets, tokenized motion sequences from the combined VQ-VAE are processed by our motionto-text model, enabling consistent inference across diverse motion data. 

**Evaluation Metrics.** We use **R Precision** and **Multimodal Distance (MM Dist.)** to quantitatively measure the performance of our motion-to-text mapping. Unlike in text-to-motion tasks, where motion features are used to retrieve text, we reverse the process by using text features to retrieve the corresponding motion. This adaptation ensures the metrics effectively measure the alignment in motion-to-text tasks. For linguistic evaluation, we use the NLPEval codebase<sup>3</sup> to compute 

3https://github.com/Maluuba/nlg-eval 



Figure 2. Effect of dataset size on motion reconstruction and motion-to-text generation performance. The x-axis shows the percentage of training data used (10%, 20%, 50%, 80%, and 100%), and the y-axis displays performance metrics: Pairwise BLEU, MM Dist., Top-1, and Top-3 accuracy. Larger datasets consistently improve performance across all metrics, highlighting the benefits of increased data scale. 

BLEU [26] and ROUGE [15]. To assess text diversity, we compute Distinct-n[14], which evaluates diversity by counting the number of distinct unigrams and bigrams in the generated texts. Additionally, we measure Pairwise BLEU[34] using the SacreBLEU<sup>4</sup> . 

**Impact of Dataset Size.** We show the influence of dataset size on both motion reconstruction and text-to-motion tasks in the paper. Figure 2 further illustrates the impact of dataset size on motion reconstruction and motion-to-text generation. Based on the TM2T architecture, we train a motion VQ-VAE for reconstruction and a transformer-based motion-to-text model for captioning with varying proportions of the training set (10%, 20%, 50%, 80%, and 100%), while evaluating performance on the same test set. We report Pairwise BLEU, MM Dist., and Top-1/Top-3 accuracies. 

The results show consistent improvements across all tasks as the dataset size increases. Larger datasets lead to better motion-text alignment (lower MM Dist.), more diverse text generation, and improved retrieval accuracies. These findings emphasize the importance of large-scale data for enhancing performance in motion reconstruction, text-to-motion, and motion-to-text generation. 

Table 6. Ablation study on different hand motion representations and text annotations for motion captioning task. _KP_ refers to the 3D hand keypoints representation, while _6D_ denotes the MANO pose parameters encoded in the 6D representation. Numbers in parentheses indicate the quantity of text scripts. Upper bound indicates the metric performance calculated with the ground truth. 

|Datasets|R Pr<br>@1|ecision(<br>@2|%)_↑_<br>@3|MM Dist_↓_|Pairwise<br>BLEU _↓_|B@4_↑_|ROUGE_↑_|distinct-1(%)_↑_|distinct-2_↑_(%)|BScore_↑_|
|---|---|---|---|---|---|---|---|---|---|---|
|upper bound|75.7|87.2|92.1|3.28|-|-|-|-|-|-|
|6D (14k)|49.8|62.8|70.2|5.66|1.30|33.7|51.2|4.03|16.4|47.1|
|6D(84k)|50.2|61.3|66.7|6.31|**0.804**|36.0|53.7|7.27|24.5|50.3|
|upper bound|75.3|89.1|93.9|2.87|-|-|-|-|-|-|
|KP (14k)|**57.2**|**68.9**|**74.4**|**4.69**|1.21|41.3|56.8|6.28|21.4|52.4|
|KP (84k)|57.0|66.1|69.8|5.37|0.916|**43.1**|**57.7**|**15.3**|**36.9**|**55.4**|



**Ablations of Different Motion Representations and Text Annotations.** We also conduct ablation study on different motion representation and number of text annotations for motion captioning task in Table 6 

The results indicate that the 6D representation slightly underperforms compared to the keypoint representation in the motion captioning task. However, the addition of extra text annotations significantly improves performance on linguistic metrics, boosting the diversity of generated motions. Also as the number of text annotations per motion clip increases, the retrieval accuracy for matching motions to corresponding text slightly decreases. This could be due to the fact that with more annotations, the matching process becomes more challenging, as the model may have to distinguish between a larger variety of possible descriptions for the same motion, leading to more potential mismatches in retrieval. 

4https://github.com/mjpost/sacrebleu 



<!-- Start of picture text -->
Raise the brightness control  Grip the color pen to  Cross your index and middle  Insert the Type-C power  Open the lid of the hand<br>bar to lighten the screen prepare for write fingers on both hands supply into the laptop sanitizer bottle<br>Move the brightness control  Clutch the pen to begin  Intertwine your index and  Plug the audio cable of the  Uncap the moisturizer<br>bar up to make the screen  writing middle finger on each hand headphones into the laptop container<br>brighter<br>Swipe up to show the  Seize one earring with  Place your index and middle  Connect the Type-C power  Twist off the cap of the hand<br>password screen your finger fingers in a crisscross  supply to the laptop sanitizer bottle<br>position on both hands<br>Unscrew the cap of the large  Rearrange the alcohol  (empty, cup, bowl) Open, laptop Grasp, notebook<br>black and yellow striped bottle burner from one position<br>to another position<br>black and white striped bottleUnscrew the cap of the large  Rearrange the beaker from one position to another  (empty, cup, bowl) Lift open the laptop Grip the notebook<br>position<br>Take off the lid of the water bottle Pick up the salt container Pour the cream into the teacup containing the  Open the lid of the laptop Clutch the notebook<br>steeped tea<br>motion<br>GT<br>#1<br>#2<br>motion<br>GT<br>#1<br>#2<br><!-- End of picture text -->

Figure 3. More qualitative results for motion caption. Each column shows a motion sequence, its ground truth text description, and two generated texts. Hand motions highlighted in green, orange, pink and blue come from OakInk2, TACO, Arctic and GigaHands, respectively. Texts highlighted in these colors are generated by models trained on the corresponding datasets. The model trained on GigaHands generates diverse captions from a single motion (first row) and accurately captions motions from other datasets (second row). Darker color indicates later frame in the sequence. 

**More Qualitative Results.** We present additional qualitative results for motion captioning on our dataset and in-the-wild scenarios (Figure 3). Captions in matching colors are generated by models trained on these datasets. Notably, the model on GigaHands generates diverse descriptions from a single motion and accurately captions motions from other datasets, demonstrating its robustness and generalization ability. For the ARCTIC dataset [5], we apply a similar processing procedure to align orientation and motion range, ensuring consistent 3D hand keypoints. Additionally, we leverage verb annotations from [4] to obtain semantically meaningful motion clips for training the combined VQ-VAE model. 

## **5. Experiments on Dynamic Reconstruction** 

**More Qualitative Results.** Figure 4 presents additional qualitative results on novel view synthesis using GigaHands data with 2D Gaussian Splatting [12]. Each example shows two test views at three different time steps. By utilizing 38 training views from GigaHands, we are able to faithfully synthesize the test views, demonstrating the effectiveness of our method in capturing complex hand motions and interactions. 

|PSNR|SSIM|LPIPS|
|---|---|---|
|29.50|0.963|0.063|



Table 7. Quantitative Evaluation of Image Quality on Synthesized Views. 

**Quantitative Evaluations.** Table 7 provides quantitative evaluations of the synthesized test views. We measure the rendering quality for 15 randomly selected motion sequences from GigaHands using Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM)[33], and Learned Perceptual Image Patch Similarity (LPIPS)[41]. These metrics confirm the high fidelity and perceptual quality of our synthesized views, highlighting the effectiveness of our dataset in novel view synthesis. 



<!-- Start of picture text -->
view 1 view 2 view 1 view 2 view 1 view 2<br>timestep 1 timestep 2 timestep 3<br>view 1 view 2 view 1 view 2 view 1 view 2<br>timestep 1 timestep 2 timestep 3<br>view 1 view 2 view 1 view 2 view 1 view 2<br>timestep 1 timestep 2 timestep 3<br>GT<br>2DGS<br>zoom-in<br>GT<br>2DGS<br>zoom-in<br>GT<br>2DGS<br>zoom-in<br><!-- End of picture text -->

Figure 4. **Qualitative Results on Novel View Synthesis.** 

## **6. Experiments on Hand-Object Interaction** 

To assess the effectiveness of our dataset in modeling hand-object interactions, we evaluate its applicability across two objectrelated tasks inspired by prior benchmarks in Oakink and TACO. GigaHands provides rich and diverse annotations of objects and their interactions with human hands, making it a valuable resource for learning and predicting hand-object dynamics. The selected tasks aim to demonstrate the advantages of GigaHands in capturing fine-grained motion patterns and enhancing downstream applications. 

**Task-aware Motion Fulfillment.** The Task-aware Motion Fulfillment task aims to generate realistic hand motion sequences that align with predefined object trajectories while adhering to a given textual task description. To achieve this, we adapt the 

Table 8. Quantitative results for text-driven motion synthesis with models trained on different datasets. _upper bound_ indicates performance calculated with the ground truth. We report the mean of 20 evaluations, and _→_ means the closer to the upper bound the better. The model trained on GigaHands performs best on most metrics. 

|Dataset|R Pr<br>@1|ecision(<br>@2|%)_↑_<br>@3|MM Dist._↓_|FID_↓_|Div._→_|MM._↑_|
|---|---|---|---|---|---|---|---|
|upper bound|50.4|71.2|81.1|3.67|0.022|9.30|-|
|OakInk2[39]|23.4|35.7|49.8|7.41|13.1|6.24|3.71|
|upper bound|77.4|88.8|91.3|2.96|0.002|11.9|-|
|GigaHands|**27.2**|**46.2**|**54.6**|**6.12**|**5.91**|**10.2**|**9.73**|



MDM baseline model [35] by incorporating dual-conditioning on both textual instructions and object trajectories. Given a task description and a sequence of object movements, the model predicts a corresponding sequence of hand motions that naturally interact with the object. For evaluation, we employ feature extractors and metrics used in text-to-motion tasks above. Table 8 provides a quantitative comparison between our approach and Oakink2. Our method outperforms Oakink2 across all evaluated metrics, highlighting its effectiveness in generating task-aware hand-object interactions. 

|Method|_Je_(_mm, ↓_)|_Te_(_mm, ↓_)|_Re_(<sup>_◦_</sup>_, ↓_)|
|---|---|---|---|
|TACO|71.7 / 58.4|52.8|73.2|
|GigaHands|69.3 / 62.3|47.6|67.5|



Table 9. Quantitative comparison of hand-object motion forecasting across different datasets. The evaluation metrics include Mean Per Joint Position Error ( _Je_ ) for right / left hand pose prediction, translation error ( _Te_ ) and rotation error ( _Re_ ) for object motion. Lower values indicate better performance. 

**Generalizable Hand-object Motion Forecasting.** Hand-object motion forecasting aims to predict future hand and object motions based on a short observed sequence. Given the poses of both hands and objects over _N_ consecutive frames, the objective is to forecast their poses over the subsequent _M_ frames. In our experiments, we set _N_ = 10 and _M_ = 10 We adapt the MDM model by conditioning it on the past N frames of hand and object poses to predict their future states over the next M frames. Following human-object forecasting evaluations [18, 38], we access hand pose estimation using Mean Per Joint Position Error _Je_ , while object motion is evaluated with translation error _Te_ and rotation error _Re_ . For TACO’s triplet representation, we condition only on tool poses and compute the corresponding metrics. Table 9 presents a comparative analysis of models trained on different datasets. While both models achieve comparable performance in hand pose prediction, our approach outperforms TACO in object motion forecasting. However, hand-object motion forecasting still remains a challenging task. The inherent complexity and rapid variations in generative motion patterns make modeling motion distributions difficult. Future work could explore more effective strategies to address this challenge. 

## **7. Hand Motion Tracking** 

|box detection|2D keypoints detection|time(150frames)|valid rate|
|---|---|---|---|
|detectron2|VITPose|6.5min|91.7%|
|yolov9c/track|VITPose|3.3min|89.6%|
|yolov9c/detect batch|VITPose|1.1min|85.4%|
|yolov9c/detect batch|HaMeR|3.0min|97.9%|



Table 10. Comparison of different bounding box detection and 2D keypoint estimation methods. 

Figure 5 illustrates the complete pipeline for hand motion tracking. The process begins with view-wise hand detection, tracking, handedness classification, and 2D keypoint extraction. Using multi-view 2D keypoints for both hands, we then triangulate each hand separately to obtain 3D hand keypoints. Finally, with the 2D keypoints and triangulated 3D keypoints, 



<!-- Start of picture text -->
box detection handness  merge multi-view 2D keypoints<br>classification w/ handness<br>constraint<br>handness<br>triangulation<br>2d keypoint  constraint<br>extraction merge<br>hand bounding  2D keypoints  2D keypoints<br>filmed video boxes w/o handness w/ handness 3D keypoints w/ handness 3D hand meshes<br><!-- End of picture text -->

Figure 5. **Hand Motion Tracking Pipeline.** 

we fit the MANO [32] parameters under these constraints. To validate our choices for hand detection, handedness classification, and 2D keypoint estimation, we calculate the number of valid 3D triangulated frames. We consider a 3D frame valid if, for both hands: (1) there are no missing keypoints; (2) the hand kinematics are normal, with bone length variations across frames within a certain threshold; and (3) the root of the hand moves temporally consistently. Frames that do not meet these criteria are considered invalid 3D triangulated keypoints.Table 10 compares the valid frame rate among 60 motion clips and the inference time for processing 150 frames (5 seconds). 

**Hand Detection and Tracking.** For hand detection, we choose YOLO-v9 [30] as the backbone because it provides reliable detection results, runs efficiently compared to other backbones such as Detectron2[37], and yields consistent temporal results. Instead of using box tracking, we batch frames across multiple time steps (up to 256 images) and apply the detection function simultaneously, which accelerates inference time without significantly reducing the valid rate. During the filming process, we instructed subjects to keep both of their hands within the scene. Therefore, by default, we extract the two most confident bounding boxes labeled as ’hand’ from the detection results. 

**Handness (left or right).** To determine the handedness (left or right) of each detected hand, we follow the method adopted in HaMeR [27]. We use a side-aware checkpoint of ViTPose to detect keypoints within each bounding box. We classify a hand as ’right’ if more than 60% of the detected keypoints correspond to the right hand, and ’left’ if they correspond to the left hand. 

**2D Keypoint Extraction.** We use HaMeR[27] for 2D keypoint extraction for two main reasons. First, it estimates a parametric representation of the hand from a cropped image, ensuring that all keypoints can be extracted from the output. Second, it provides more reliable results that ensure the hand kinematics are reasonable. We believe this is the primary reason that keypoints extracted from HaMeR lead to the most valid triangulated 3D keypoints. Although using HaMeR decreases inference speed, it significantly improves the valid rate. 

**3D Keypoint Triangulation.** With the camera parameters and 2D keypoints extracted from multiple views, we triangulate the 3D keypoints for each hand. We remove outliers using RANSAC to improve accuracy. 

**Parameter Fitting.** For MANO parameter fitting, we follow the EasyMoCap [1] pipeline, using both 2D and 3D keypoints as supervision. To capture fine-grained finger motions, we disable the PCA components and use a flat mean shape during the fitting process. This approach allows for more detailed and accurate hand mesh reconstruction. 

## **8. Object Motion Tracking** 

The tracking process aims to estimate the 6DoF (six degrees of freedom) pose of the pre-scanned or generated mesh over time using multi-view RGB videos as constraints. Since our capturing system only contains RGB information without depth, pose estimation poses significant challenges. Figure 6 illustrates the complete object tracking pipeline. However, this can be mitigated by utilizing 51 camera views that provide 360-degree coverage of the scene. The tracking process generally consists of three stages: (1) extracting object masks across views as constraints; (2) providing a coarse pose estimation for 



<!-- Start of picture text -->
detect *most confident<br>retrieval<br>filmed video<br>filter filter *best match<br>match …<br>random initialization<br>initial candidates  positive candidates true positive candidates<br>across time across time across time<br>init R<br>multi-view renders match constraint<br>match<br>rendered mesh<br>“keyboard.”<br>“drum face.”<br>“ukelele. guitar.” “embedded cameras.”… init T tracking<br>object scan positive prompts negative prompts density field differentiable rendering<br><!-- End of picture text -->

Figure 6. **Hand Motion Tracking Pipeline.** 

|stage|mask coverage|
|---|---|
|coarse estimation|45.2%|
|pose refinement (first frame)|91.1%|
|i i<br>pose refinement(sequence)|78.5%|



Table 11. Evaluation of Mask Coverage Rates Across Different Stages of Object Motion Tracking. 

the mesh as an initialization for the following refinement process; (3) refining the object pose using multi-view pixel-level constraints to achieve accurate pose estimation. We use the mask coverage rate as an evaluation metric for tracking quality. The mask coverage rate is defined as the percentage of true positive segmented masks across frames that overlap with the rendered object’s silhouette during differentiable rendering. Table 11 provides this evaluation across different stages. 

**Object Segmentation.** To use the multi-view RGB videos as constraints, accurate object masks are necessary. During the mask extraction process, we aim for three objectives: (1) obtaining masks from as many views as possible to guarantee more accurate results; (2) avoiding false positives in the segmentation masks, as they can be very distracting; (3) ensuring the masks are consistent across views to provide stable supervision. To achieve the first goal, for each view, we use DINOv2 [24] to detect as many object candidates as possible across time steps. We detect objects across time steps because an object might only appear during certain time period throughout the video. With multiple candidates that cover all objects across time steps, we address the second goal by using both image and text prompts to identify true positive candidates through feature matching methods using CLIP [23] and Grounding DINO [16]. Image prompts are generated by rendering object scans from random views on a sphere, while text positive prompts are manually designed. To remove false positives, we design negative prompts and compare them with the positive candidates. If an object candidate is more similar to the negative prompt than to the positive prompt, we regard it as a false positive. From all the true positive candidates, we select the most confident one using text-image similarity evaluated by CLIP [23]. With the most confident candidate, we can track the object across the video using SAM2 [29]. 

**Coarse Pose Estimation** Given the segmented object masks across views, we can initialize the coarse pose of the object. We first find the time step with the largest summed mask area of views. We use the multi-view masks at this time step to reconstruct the density field using Instant-NGP [21]. We threshold the reconstructed density field and find the largest cluster inside the field, shown as the yellow points in Figure 6. We then use the center of this density field as the coarse translation of the object. If the density field reconstruction fails, we use the center of the capture system with five random offsets as the coarse translations. Since the reconstructed density field is noisy, we cannot reliably use ICP (Iterative Closest Point) to 

obtain the coarse rotation. Additionally, the geometric symmetry of the meshes requires us to use appearance information to initialize the rotation. We follow FoundPose [25] by randomly rotating the template mesh and retrieving the top five matched rotations using DINOv2 features. We use these as the initialization for rotation. Table 11 row 1 reports the mask coverage of the coarse estimation at this stage. 

**Pose Refinement.** Given the coarse estimation of translation and rotation, we refine the pose estimation using differentiable rendering supervised with multi-view silhouette loss. The refinement consists of three stages. In the first stage, we select the best coarse initialization. In the previous step, we might have multiple translation and rotation candidates due to density field reconstruction failure and ambiguity in object symmetry. Therefore, we first optimize the pose starting from multiple coarse pose candidates for 200 steps. In the second stage, we select the coarse pose candidate with the minimal silhouette loss and further optimize the pose for 500 steps. Table 11 row 2 reports the mask coverage of the pose refinement for this frame after these two stages. In the third stage, we optimize the whole sequence, using the frame from the previous stage as initialization. Note that this time step is selected based on the maximal mask area, so it could be in the middle of a sequence. If this is the case, we need to optimize the loss temporally in both directions. For each next time step to optimize, we use its nearest optimized time step as initialization. We optimize 500 steps for each frame. Table 11 row 3 reports the final mask coverage across the sequence. Note that the mask coverage drops compared to the first frame; this is because for sequences with fast motion or where the object is severely occluded due to manipulation, the pose might lose track and accumulate errors. 

## **9. Text Instructions and Annotations** 

In this section, we provide the prompts and examples used to create the instruction scripts and for annotation augmentation, along with details about the annotation interface. 

### **9.1. Prompts and Examples for scenario grouping** 

In the scenario grouping phase, we start with verb pools extracted from multiple hand datasets. Our goal is to find objects corresponding to these verbs within various scenarios, enabling us to act out the associated actions. We prompt the LLM with specific instructions to generate verb-object pairs. From the LLM’s outputs, we select reasonable verb-object pairs that can be filmed on a tabletop setting. Here is an example to find objects associate with the verb ‘beat’. 

Task: Using the verb "beat," generate a list of objects that can be acted upon with this verb in various scenarios. Ensure the objects are relevant and specific to the given context. 

Scenarios 

1. Cooking: Identify objects or ingredients commonly associated with "beat" in culinary activities. 

2. Entertainment: List objects or tools that can be "beat" in entertainment or recreational contexts. 

3. Housework: Suggest items or surfaces that are "beat" during cleaning or household chores. 

4. Crafting: Find materials or tools that involve "beat" as part of a creative or crafting process. 

5. Office Work: Consider any metaphorical or literal uses of "beat" with objects in an office or work environment. 

Requirements: 

1. Ensure that each object aligns with the context of the scenario. 

2. Provide a diverse and creative range of examples for each scenario. 

3. Be specific about the relationship between "beat" and the object. 

### **9.2. Prompts and Examples for Scene structuring** 

In the scene structuring phase, we have already associated each scene with verbs and objects, organizing them through activities. However, in the manually designed raw activity scripts, some verbs related to the activities might be missing. To address this, we provide the LLM with a prompt to add the missing verbs to the scenes. For example below, we augmented 

the ”playing cards” part within the ”Playing Monopoly, Cards, Coins, and Knucklebones” scene. After obtaining the output from the LLM, we perform a sanity check to ensure accuracy and coherence. 

- **<sup>RefinedPromptforPlayingCardsScript</sup> ** 

- You are tasked with refining a script for playing cards. The script must follow the format: **[verb-ing]: detailed description**. Several actions are missing, and you need to incorporate them into the sequence of actions in the correct position while ensuring the script is clear, organized, and detailed enough for a hand actor to act out. 

#### Instructions: 

1. Follow the format: Each action is described with a verb ending in "-ing" and its detailed description. 

2. Include the following missing actions: scatter, slide, split, swap, wave. 

3. Ensure the scenario is consecutive: The sequence of actions should flow logically without gaps. 

4. Provide detailed hand action descriptions: Describe how the hands move, grip, and interact with the cards for clarity and precision. 

5. This script is for a hand actor to act out. The quality of your addition and organization will determine the final output. 

6. Ensure the sequence of actions forms a coherent and consecutive scenario. 

If you revise the script well, I will reward you $20. 

#### Original Script: 

#### Play Cards 

- [Bridge Shuffling]: Hold the deck with your right hand. Use your thumb and middle finger to grip the deck on the short sides, with your index finger resting along the long edge of the deck. Do the bridge shuffle. 

- [Regular Shuffling]: Shuffle the deck of cards by interweaving them with your hands, mixing them thoroughly. 

- [Cutting + Dealing]: Cut the deck of cards in half using a quick motion, separating it into two smaller decks. Deal the cards to the players one by one, distributing them evenly. 

- [Flipping]: Flip the top card of the deck face-up, revealing its value or suit. 

- [Fanning + Checking + Sorting]: Fan out the cards in your hand, creating a spread of cards that can be easily viewed. Check the value of your cards by looking at them without revealing them to others. Sort the cards in your hand according to their suits or numerical order. 

- [Drawing + Discarding]: Draw a card from the deck and add it to your hand, increasing the number of cards you hold. Discard a card from your hand by placing it face-down on a designated discard pile. 

- [Collecting + Stacking]: Collect the cards from all players after a round of the game has ended. Stack the cards on top of each other, forming a neat pile. 

### **9.3. Prompts and Examples for instruction scripting** 

In the instruction scripting phase, we already have an activity script for each scene, where each activity is associated with a list of verbs that occur sequentially. Our goal here is to expand each verb into a complete instruction that helps fulfill the activity. We provide the LLM with a prompt to achieve this expansion. For instance below, we applied this process to an activity in the ”Making and Drinking Tea” scene. After receiving the output from the LLM, we conducted three rounds of sanity checks to ensure the instructions were accurate and coherent. 

- You are tasked with refining and structurizing the given hand action script. The final script must follow these guidelines: 

1. Format: Each action must follow the format ‘[verb-ing]: detailed description of the action.‘ 

2. Retain All Verbs: Do not delete or remove any verbs provided in the brackets. 3. Separate Multiple Verbs: If a bracket contains multiple verbs, split them into individual actions, each with its own description. 

4. Expand Missing Verbs: If a verb is implied but not explicitly described in the action, add it with an accurate and detailed description. 

5. Verb Format: Change all verbs into the present participle format (‘-ing‘ form). 

6. Clarity and Detail: Ensure the descriptions are clear, precise, and detailed enough for a hand actor to perform the actions. 

Example: 

Original Action: 

- ‘[grip, set, lift]: Grip the teapot lid with the right hand, lift it, and set it aside.‘ 

Refined Actions: 

- [Gripping]: Grip the teapot lid firmly with the right hand. 

- [Lifting]: Lift the teapot lid straight up, keeping it steady. 

- [Setting]: Set the teapot lid down gently on a flat surface. 

### **9.4. Annotation Interface** 

For the annotation phase, we already have the instruction scripts and the motion sequences filmed accordingly. Our task is to annotate any actions that were not mentioned in the original instruction scripts. Figure 7 illustrates the annotation interface we used. This interface loads the filmed multi-view videos with the hand mesh rendered on top for visual clarity. The original instruction is displayed below the video. Features such as a progress bar and controls like “Play,” “+1 Frame,” and “-1 Frame” buttons are provided to accurately segment the motion sequence. Additionally, buttons like “Match Annotation,” “Add Annotation,” “Remove Annotation,” “Split Video,” and “Remove Split” are available to correct or refine the original instructions. 

### **9.5. Prompts and Examples for text augmentation** 

In the text augmentation phase, we have the motion clips along with their text annotations. To enhance the diversity of descriptions, we aim to augment these annotations since one action can be described in multiple ways. We feed the LLM with a specific prompt for text augmentation. Outputs such as system errors or phrases like “I’m sorry” are removed to maintain data quality and consistency. 

You are a sentence rewriter. Your task is to rewrite the provided input sentence into five different variations. You can vary the verbs and descriptions but 

**<sup>donotaddanynewactionsorchangetheoriginalmeaning</sup> **<sup>.</sup> 



Figure 7. **Annotation Interface.** 

Instructions: 

- Begin the output with: "Rewritten Sentences:" 

- Each sentence should be separated by the symbol "$" 

- Use different verbs or phrasing to achieve natural, varied expressions 

   - without changing the action or intent of the original sentence. 

#### Example: 

Input: "Take out an egg from the carton.\n" 

Output: Rewritten Sentences: Remove an egg from the carton. $ Pick out an egg from the carton. $ Pull an egg from the carton. $ Grab an egg from the carton. $ Lift an egg from the carton. 

## **10. Dataset Inspection** 

### **10.1. Object Visualization.** 

Figure 8 shows 96 of the objects in GigaHands by randomly select a few objects each scene. The objects spans diverse scenarios and functionalities. 



Figure 8. **Randomly Sampled Objects.** 

### **10.2. Verb Pool.** 

GigaHands contains a total of 1467 verbs. Table 12 and Tab. 13 shows the most frequent and least frequent verbs in the text annotation. 

|place<br>|take|use<br>|put<br>|press<br>|set<br>|open<br>|remove<br>|
|---|---|---|---|---|---|---|---|
|position|move|hold|pull|seize|apply|pick|lift|
|secure|slide|grab|lay|turn|grasp|tap|push|
|extract|clutch|insert|shift|detach|fasten|adjust|grip|
|rest|twist|rotate|arrange|snatch|hit|spread|return|
|close|retrieve|employ|release|loosen|squeeze|drop|flip|
|glide|rub|make|click|fold|attach|touch|clean|
|cut|get|leave|raise|sweep|wipe|switch|collect|
|shut|seal|transfer|cover|snap|draw|withdraw|keep|
|spin|swipe|select|separate|strike|perform|shake|toss|
|bring|utilize|pour|extend|activate|compress|stretch|smooth|
|pinch|ease|execute|unseal|pluck|tighten|lock|dab|
|gather|uncap|throw|scoop|roll|break|create|hoist|
|give|brush|flick|change|reduce|wrap|elevate|fill|
|trim|clasp|work|engage|distribute|swivel|slice|increase<br>l|
|drag|deposit|slip<br>i|fetch|unfold|split|let|flatten|
|pat|pass|fit|add|divide|bend|peel|dispense|
|decrease|mix|i<br>deliver|connect|agitate|trace|organize|choose|
|undo|stick|form|guide|gesture|clip|continue|swing|
|play|blend|disconnect<br>i|tear|stir|wiggle|carry|tilt|
|alter|direct|affix|coat|run|modify|unzip|uncover|
|clench|dry|shape|present|mark|maintain|depress|sketch|
|slow|massage|speed|lessen|replace|rip|wind|join|
|reach|submerge|unplug|wave|capture<br>i|immerse|bind|reveal|
|point|crush|accelerate|diminish|fix|swirl|straighten|navigate|
|snip|carve|ensure|restore|free|strip|combine|unroll|
|obtain|handle|store|tie|wash|sway|repeat|strum|
|intensify|lower|disengage|aim|plug|chop|quicken|unwind|
|catch|jiggle|reverse|go|thread|revolve|stroke|identify|
|display|pound|jostle|render|highlight|coil|knock|pretend|
|stack|relocate|scroll|untangle|rinse|show|amplify|clap|
|beat|start|enhance|wrench|spoon|tidy|align|pop|
|zip|acquire|unravel|shave|punch|widen|indicate|enter|
|write|dump|assemble|remover|launch|loop|knot|crack|
|curl|encircle|weave|plunge|do|opt|soak|suspend|
|enclose|lengthen|examine|drizzle|dispose|fle|sprinkle|pump|
|expand|unhook|grind|send|build|clamp|nudge|smack|
|relax|operate|stow|pack|hasten|tickle|shear|buckle<br>l|
|interlock|whisk|act|dunk|lean|stop|hurl|shuffle|
|hand|caress|flex|envelop|slot|drive|shoot|l<br>introduce|



Table 12. Most Frequent 320 Verbs. 

### **10.3. List of Scenarios and Scenes.** 

Table 14 presents all of the scenarios and scenes in GigaHands. 

## **References** 

- [1] Easymocap - make human motion capture easier. Github, 2021. 11 

> [2] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. _arXiv preprint arXiv:2303.08774_ , 2023. 6 

> [3] Prithviraj Banerjee, Sindi Shkodrani, Pierre Moulon, Shreyas Hampali, Fan Zhang, Jade Fountain, Edward Miller, Selen Basol, 

|hydrate<br>|nourish<br>|gain|closed<br>|travel|document<br>|interchange<br>|submit<br>|
|---|---|---|---|---|---|---|---|
|disorganize|investigate|convert|decorate|opener|imperfect|realign|be|
|disarrange|toggle|tab|purify|enfold|seek|tension|container|
|crisscross|come|systematize|chuck|tangle|slurp|bunch|relay|
|stem|filter|wield|impact|protect|achieve|slam|narrow|
|remain|dish|null|trickle|segregate|distinguish|rely|assist|
|disjoin|fuse|fish|disintegrate|heave|patch|file|waver|
|buff|stab|excise<br>i|shoelace|swell|practice|uncrease|notch|
|avoid|estimate|confirm|probe|unlink|disassemble|underline|unbend|
|orient|crash|i<br>haul|redo|enact<br>i|tense|discharge|disburse|
|amass|annotate|state|incorporate|fire|rid|reproduce|modulate|
|diffuse|collide|assort|invite|i<br>bash|beetle|blower|wound|
|lash|mount|swish|actuate|doodle|help|suck<br>l|absorb|
|center|revert|need|ascertain|demonstrate|lodge|deflate|shove|
|delve|repack|stuff|wriggle|cascade|stri|imbibe|encapsulate|
|freshen|back|scrap|sieve|screen|ignite|ajar|cool|
|swinge|defend|exhale|trill|uptick|augment|cuddle|inspire|
|exame|belt|srew|sit|quench|nil<br>l|isolate|copy|
|overcross|authenticate|reaccess|register|poke|flood|calm|remit|
|burrow|bottle|engrave|glaze|speckle|jitter|strain|stash|
|encompass|commence|erase|structure|delineate|envelope|pamper|neaten|
|mention<br>l|designate|jump|muster|signify|aid|distill|swarm|
|overflow|infest|glitch|unblock|rise|weigh|hover|amp|
|categorize|establish|hinge|emphasize|specify<br>i|assert|rebuild|seem|
|fragment|saw|retie|conclude|finalize<br>i|scribe<br>l|acknowledge|portray|
|tumble|perfect|reinforce|temper|define|flaunt|amalgamate|tend|
|recompose|customize|water|irrigate|coax|uplift|magnify|grap|
|sud|prompt|jingle|aside|leftover|peal|infuse|nest|
|bury|quarter|mop|cap|heft|nearer|expel|dress<br>l|
|interleave|cooperate|crawl|intermingle|rummage|briskly|hurry|float|
|reform|nab|bake|amend|shade|unsecure|harvest|discard|
|sample|recite|advise|grace|drum|repress|reapply|rectify|
|hop|leverage|ring|substitute|issue|believe|channel|object|
|tease|crease<br>i|snuff|draft|survey|bounce|test|hack<br>l|
|pipe|refit|prefer|style|duplicate|echo|shorn|fluctuate|
|twitch|i<br>pressurize|toast|melt|latticework|twiddle|impress|l<br>disturb|
|tremble|recreate|snug|envision|think|interweave|redirect<br>i|paste|
|scald|permit|tip|interconnect|improve|experience|refill|stock|
|resort|impart|involve|claw|pry|drap|chip|hone|
|allot|deck|trap|juggle|clarify|retreat|unfurl|disband|



Table 13. Least Frequent 320 Verbs. 

Richard Newcombe, Robert Wang, et al. Introducing hot3d: An egocentric dataset for 3d hand and object tracking. _arXiv preprint arXiv:2406.09598_ , 2024. 3 

- [4] Junuk Cha, Jihyeon Kim, Jae Shin Yoon, and Seungryul Baek. Text2hoi: Text-guided 3d motion generation for hand-object interaction. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 1577–1585, 2024. 8 

- [5] Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed Kocabas, Manuel Kaufmann, Michael J Black, and Otmar Hilliges. Arctic: A dataset for dexterous bimanual hand-object manipulation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 12943–12954, 2023. 3, 8 

- [6] Kristen Grauman, Andrew Westbury, Eugene Byrne, Zachary Chavis, Antonino Furnari, Rohit Girdhar, Jackson Hamburger, Hao Jiang, Miao Liu, Xingyu Liu, et al. Ego4d: Around the world in 3,000 hours of egocentric video. In _Proceedings of the IEEE/CVF_ 

|scenarios|scenes|
|---|---|
|Cooking, Cleaning, Eating.|Making and Drinking Tea<br>Making, Eating and Cleaning Instant Noodle<br>Eating and Packing Delivered Food<br>Making an open egg and spam sandwich<br>Making a Bowl of Salad<br>Bakingand Frostinga Bread|
|Office Working|Drawing Mind Map<br>Receiving and Sending a File<br>Testing the laptop<br>Testing Tablet DigitalPen Phone SmartWatch on Charging Station<br>Filming gestures with GoPro<br>Unwrappingand Wrappingapresent|
||Seal Carving and Smoothing|
|Crafting|Assemble and Disassemble Kids Tool Bench<br>Cultivating and uproot a Plant<br>Sewingkit,Crocheting,Knittingand Finger Knitting|
||Playing monopoly, cards, coins and knucklebones|
|Entertaining|Playing mini instruments<br>Desktop Boxing|
||Payingwith a PuppyDog|
||Applying Makeups<br>Packing a gym bag|
|Houseworks|Massaging Your Own Hands<br>First Aid<br>CleaningGlass Tabletop|



##### Table 14. All 5 Scenarios and 25 Scenes. 

_Conference on Computer Vision and Pattern Recognition_ , pages 18995–19012, 2022. 3 

- [7] Kristen Grauman, Andrew Westbury, Lorenzo Torresani, Kris Kitani, Jitendra Malik, Triantafyllos Afouras, Kumar Ashutosh, Vijay Baiyya, Siddhant Bansal, Bikram Boote, et al. Ego-exo4d: Understanding skilled human activity from first-and third-person perspectives. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 19383–19400, 2024. 3 

- [8] Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li, and Li Cheng. Generating diverse and natural 3d human motions from text. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 5152–5161, 2022. 3, 4 

- [9] Chuan Guo, Xinxin Zuo, Sen Wang, and Li Cheng. Tm2t: Stochastic and tokenized modeling for the reciprocal generation of 3d human motions and texts. In _ECCV_ , 2022. 4, 5, 6 

- [10] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 770–778, 2016. 3 

- [11] Matthew Honnibal and Ines Montani. spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing. To appear, 2017. 3 

- [12] Binbin Huang, Zehao Yu, Anpei Chen, Andreas Geiger, and Shenghua Gao. 2d gaussian splatting for geometrically accurate radiance fields. In _ACM SIGGRAPH 2024 Conference Papers_ , pages 1–11, 2024. 8 

- [13] Juntao Jian, Xiuping Liu, Manyi Li, Ruizhen Hu, and Jian Liu. Affordpose: A large-scale dataset of hand-object interactions with affordance-driven hand pose. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 14713–14724, 2023. 3 

- [14] Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, and Bill Dolan. A diversity-promoting objective function for neural conversation models. _arXiv preprint arXiv:1510.03055_ , 2015. 7 

- [15] Chin-Yew Lin. Rouge: A package for automatic evaluation of summaries. In _Text summarization branches out_ , pages 74–81, 2004. 7 

- [16] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Chunyuan Li, Jianwei Yang, Hang Su, Jun Zhu, et al. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. _arXiv preprint arXiv:2303.05499_ , 2023. 12 

- [17] Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, and Li Yi. Hoi4d: A 4d egocentric dataset for category-level human-object interaction. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21013–21022, 2022. 3 

- [18] Yun Liu, Haolin Yang, Xu Si, Ling Liu, Zipeng Li, Yuxiang Zhang, Yebin Liu, and Li Yi. Taco: Benchmarking generalizable bimanual tool-action-object understanding. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21740–21751, 2024. 3, 6, 10 

- [19] I Loshchilov. Decoupled weight decay regularization. _arXiv preprint arXiv:1711.05101_ , 2017. 3 

- [20] George A Miller. Wordnet: a lexical database for english. _Communications of the ACM_ , 38(11):39–41, 1995. 3 

- [21] Thomas M¨uller, Alex Evans, Christoph Schied, and Alexander Keller. Instant neural graphics primitives with a multiresolution hash encoding. _ACM transactions on graphics (TOG)_ , 41(4):1–15, 2022. 12 

- [22] Takehiko Ohkawa, Kun He, Fadime Sener, Tomas Hodan, Luan Tran, and Cem Keskin. Assemblyhands: Towards egocentric activity understanding via 3d hand pose estimation. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 12999–13008, 2023. 3 

- [23] Abby O’Neill, Abdul Rehman, Abhinav Gupta, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, et al. Open x-embodiment: Robotic learning datasets and rt-x models. _arXiv preprint arXiv:2310.08864_ , 2023. 12 

- [24] Maxime Oquab, Timoth´ee Darcet, Th´eo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, et al. Dinov2: Learning robust visual features without supervision. _arXiv preprint arXiv:2304.07193_ , 2023. 12 

- [25] Evin Pınar Ornek,<sup>¨</sup> Yann Labb´e, Bugra Tekin, Lingni Ma, Cem Keskin, Christian Forster, and Tomas Hodan. Foundpose: Unseen object pose estimation with foundation features. _arXiv preprint arXiv:2311.18809_ , 2023. 13 

- [26] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine translation. In _Proceedings of the 40th annual meeting of the Association for Computational Linguistics_ , pages 311–318, 2002. 7 

- [27] Georgios Pavlakos, Dandan Shan, Ilija Radosavovic, Angjoo Kanazawa, David Fouhey, and Jitendra Malik. Reconstructing hands in 3d with transformers. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 9826–9836, 2024. 11 

- [28] Jeffrey Pennington, Richard Socher, and Christopher D Manning. Glove: Global vectors for word representation. In _Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP)_ , pages 1532–1543, 2014. 3 

- [29] Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman R¨adle, Chloe Rolland, Laura Gustafson, et al. Sam 2: Segment anything in images and videos. _arXiv preprint arXiv:2408.00714_ , 2024. 12 

- [30] Dillon Reis, Jordan Kupec, Jacqueline Hong, and Ahmad Daoudi. Real-time flying object detection with yolov8. _arXiv preprint arXiv:2305.09972_ , 2023. 11 

- [31] Javier Romero, Dimitrios Tzionas, and Michael J. Black. Embodied hands: Modeling and capturing hands and bodies together. _ACM Transactions on Graphics, (Proc. SIGGRAPH Asia)_ , 2017. 3 

- [32] Javier Romero, Dimitrios Tzionas, and Michael J Black. Embodied hands: Modeling and capturing hands and bodies together. _arXiv preprint arXiv:2201.02610_ , 2022. 11 

- [33] Umme Sara, Morium Akter, and Mohammad Shorif Uddin. Image quality assessment through fsim, ssim, mse and psnr—a comparative study. _Journal of Computer and Communications_ , 7(3):8–18, 2019. 8 

- [34] Tianxiao Shen, Myle Ott, Michael Auli, and Marc’Aurelio Ranzato. Mixture models for diverse machine translation: Tricks of the trade. In _International conference on machine learning_ , pages 5719–5728. PMLR, 2019. 7 

- [35] Guy Tevet, Sigal Raab, Brian Gordon, Yoni Shafir, Daniel Cohen-or, and Amit Haim Bermano. Human motion diffusion model. In _The Eleventh International Conference on Learning Representations_ , 2023. 4, 5, 10 

- [36] A Vaswani. Attention is all you need. _Advances in Neural Information Processing Systems_ , 2017. 3 

- [37] Yuxin Wu, Alexander Kirillov, Francisco Massa, Wan-Yen Lo, and Ross Girshick. Detectron2. https://github.com/ facebookresearch/detectron2, 2019. 11 

- [38] Sirui Xu, Zhengyuan Li, Yu-Xiong Wang, and Liang-Yan Gui. InterDiff: Generating 3d human-object interactions with physicsinformed diffusion. In _ICCV_ , 2023. 10 

- [39] Xinyu Zhan, Lixin Yang, Yifei Zhao, Kangrui Mao, Hanlin Xu, Zenan Lin, Kailin Li, and Cewu Lu. Oakink2: A dataset of bimanual hands-object manipulation in complex task completion. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 445–456, 2024. 3, 6, 10 

- [40] Jianrong Zhang, Yangsong Zhang, Xiaodong Cun, Yong Zhang, Hongwei Zhao, Hongtao Lu, Xi Shen, and Ying Shan. Generating human motion from textual descriptions with discrete representations. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 14730–14740, 2023. 3, 4, 5 

- [41] Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 586–595, 2018. 8 

- [42] Yi Zhou, Connelly Barnes, Jingwan Lu, Jimei Yang, and Hao Li. On the continuity of rotation representations in neural networks. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 5745–5753, 2019. 5 

