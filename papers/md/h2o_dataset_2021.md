# **H2O: Two Hands Manipulating Objects for First Person Interaction Recognition** 

Taein Kwon<sup>1</sup> , Bugra Tekin<sup>2</sup> , Jan St¨uhmer<sup>3*</sup> , Federica Bogo<sup>1</sup> , and Marc Pollefeys<sup>1</sup><sup>_,_2</sup> 

1ETH Zurich, 2Microsoft, 3Samsung AI Center, Cambridge 

## **Abstract** 

_We present a comprehensive framework for egocentric interaction recognition using markerless 3D annotations of two hands manipulating objects. To this end, we propose a method to create a unified dataset for egocentric 3D interaction recognition. Our method produces annotations of the 3D pose of two hands and the 6D pose of the manipulated objects, along with their interaction labels for each frame. Our dataset, called H2O (2 Hands and Objects), provides synchronized multi-view RGB-D images, interaction labels, object classes, ground-truth 3D poses for left & right hands, 6D object poses, ground-truth camera poses, object meshes and scene point clouds. To the best of our knowledge, this is the first benchmark that enables the study of first-person actions with the use of the pose of both left and right hands manipulating objects and presents an unprecedented level of detail for egocentric 3D interaction recognition. We further propose the method to predict interaction classes by estimating the 3D pose of two hands and the 6D pose of the manipulated objects, jointly from RGB images. Our method models both inter- and intra-dependencies between both hands and objects by learning the topology of a graph convolutional network that predicts interactions. We show that our method facilitated by this dataset establishes a strong baseline for joint hand-object pose estimation and achieves state-of-the-art accuracy for first person interaction recognition._ 

## **1. Introduction** 

In recent years, there has been tremendous progress in video understanding and action recognition. Current algorithms can reliably recognize the action the subject is performing in many unconstrained settings from third person viewpoints [9, 22, 23, 24, 74, 92]. Although action recognition from first-person views has many applications in augmented reality, robotics and surveillance, it trails behind the progress in third person views, mostly due to the lack of large and diverse egocentric datasets. From an egocentric viewpoint, action recognition is mostly about understanding hand & object interactions. A unified understanding of 

> *Work performed while at Microsoft. Project Page: https://www.taeinkwon.com/projects/h2o 



Figure 1: **Two hands manipulating objects for first person interaction recognition.** We propose a dataset providing rich annotations for 3D poses of left & right hands, 6D object poses, camera poses, object meshes and scene point clouds, along with their associated interaction labels. We leverage our dataset to propose novel methods for 3D interaction recognition. 

the positions and movements of hands and the manipulated objects is crucial for recognizing egocentric interactions. However, existing first-person interaction datasets mostly provide only 2D features ( _e.g_ . bounding boxes, hand segmentation) without reasoning in 3D about the motions of hands and the manipulated objects. In this work, we propose, for the first time, a unified dataset for first person interaction recognition with markerless 3D annotations of two hands manipulating objects, as depicted in Fig. 1. We collect a richly annotated dataset including synchronized RGB-D images, camera poses, right & left hand poses, object poses, object meshes, scene point clouds and action labels, which provides an unprecedented level of detail for understanding 3D hand-object interactions. With the help of our dataset, we present the first method to estimate jointly the 3D pose of two hands and objects from a color image. We further propose to learn interdependencies within and across hand and object poses using an adaptive graph convolutional network for 3D interaction recognition. 

Jointly capturing hands in action and the manipulated objects in 3D is a challenging problem due to reciprocal occlusions. The problem is more challenging from first person viewpoints due to the unique challenges brought by egocentric vision such as fast camera motion, large occlusion, background clutter [50] and most importantly, lack of datasets. Recent works have proposed datasets that successfully addressed some of these challenges. Sridhar et al. [76] have presented one of the earliest datasets for hand-object interactions, in which a single hand manipulates a cuboid object. Pioneering works by [26, 32, 34] have further proposed datasets that include 3D annotations for object ma- 

nipulation scenarios of a single hand. 

Most of these works, however, are limited by different factors. They mainly focus on _single hand manipulation scenarios_ [26, 32, 34]. While single hand manipulation is relevant for some scenarios, most of the time, hand-object interaction involves two hands manipulating an object. Using _only 2D annotations_ , [82, 83] presented datasets for hand-hand and hand-object interactions. The intricate nature of hand-object interactions, however, requires 3D reasoning rather than 2D to better resolve mutual occlusions. In the context of hand-object interactions, early work mostly tackles the problem of joint estimation of 3D hand and object poses, _without reasoning about the actions_ . While precise 3D position data for hands and objects is crucial for many applications in robotics and graphics, the sole knowledge of the pose lacks semantic meaning about the actions of the subject. To that end, [26] released an egocentric action dataset including 3D annotations of hands and objects; however, the data is captured with an _intrusive motion capture system_ . Although motion capture datasets [26, 78] can provide large amounts of training samples with accurate 3D annotations, they can only be captured in controlled settings and have visible markers on the images that bias pose prediction in color images. _Synthetic datasets_ [34] could provide an alternative to them, however, the existing ones cannot yet reach the realism that is needed to generalize to real images and are only for single-image scenarios that lack temporal context crucial for recognizing interactions. 

Our method aims at tackling these limitations exhibited by prior work. To this end, we propose an approach for creating a unified dataset for egocentric 3D interaction recognition that includes markerless annotations of the 3D pose of two hands and the 6D pose of the manipulated objects, along with their associated action labels for each frame of a large number of recordings that include 571,645 synchronized RGB-D frames. In addition, we propose the first method to jointly predict the 3D pose of two hands and 6D pose of the manipulated objects using only RGB images and present a novel 3D interaction recognition approach that learns the interdependencies between hand and object poses by a topology-aware graph convolutional network. 

Our contributions can be listed as follows: 

- We present the first unified dataset for egocentric interaction recognition with markerless 3D annotations of two hands and the 6D pose of manipulated objects. Our dataset, which we call _H_ 2 _O_ , standing for _2 hands_ and _objects_ , provides rich ground-truth annotations for 3D hand-object poses & shapes, action labels, camera poses, scene point clouds and object meshes that enable us to produce comprehensive egocentric scene interpretations. 

- We propose a semi-automatic pipeline to curate a handobject interaction dataset with action labels and the poses of two interacting hands as well as the objects in contact, 

using a practical multi-camera system with diverse backgrounds. We demonstrate the fidelity and accuracy of our annotations by detailed verifications. 

- We introduce a unified approach to recognize handobject interactions from RGB images that simultaneously predicts, for the first time, the 3D pose of two interacting hands and the 6D pose of manipulated objects, along with action and object classes. 

- Leveraging our dataset, we propose a novel method for 3D interaction recognition that learns the interdependencies between two hands and objects with a topologyaware graph convolutional network. To this end, we parameterize both hand and object poses as individual graphs and combine them in a single multi-graph architecture. We then learn the interdependencies and connections between different graph entities with an adaptive architecture and compute the topology of the multi-graph structure for recognizing 3D hand-object interactions. We demonstrate that using the pose predictions facili- 

- tated by our dataset, we achieve better overall performance for recognizing interactions outperforming the state-of-theart [9, 17, 23]. We further provide baselines for hand & object pose estimation and interaction recognition to enable further benchmarking on this dataset. We will make our dataset and annotations publicly available upon acceptance. 

## **2. Related Work** 

**Datasets for egocentric action recognition and handobject pose estimation.** While many datasets for thirdperson action recognition have been proposed throughout the years [30, 40, 72, 99], recently there is a surge in interest for data targeting also egocentric scenarios [12, 13, 29, 48, 62, 71] that involve mostly 2D features. These datasets provide only limited multi-view data and do not provide hand and object poses, which have been shown to be useful cues for a comprehensive understanding of the scene [26, 80]. 

A few datasets collect hand pose ground truth, acquired in an automated or semi-automated way (Panoptic [37, 38], FreiHand [102], Interhand [57]). However, they do not consider interactions with objects. Recently, GRAB [78] uses a mocap system and objects from [6] to track body and hand pose while interacting with the scene without providing corresponding images. HOnnotate [32] relies on an optimization process to estimate accurate hand and object pose from 

|Dataset|Frames|Action|6D Obj|3D left|3D right|(**)Markerless|Real|Ego|Depth|Multiview|
|---|---|---|---|---|---|---|---|---|---|---|
|H2O|571k||||||||||
|FPHA [26]|100k||* (23k)|_·_||_·_||||_·_|
|HOnnotate [32]|78k|_·_||_·_||||_·_|||
|Obman [34]|150k|_·_||_·_|||_·_|_·_||_·_|
|Freihand [102]|37k|_·_|_·_|_·_||||_·_|_·_||
|Panoptic [38]|1.5M|_·_|_·_|||||_·_|||
|ContactPose[7]|2.9M|_·_|(***)|||_·_||_·_|||



Table 1: A comparison of the existing related _image-based datasets_ with 3D annotations for hand interactions. H2O provides a total of 571k frames captured from 5 different views. (*): Object pose provided only for a subset of frames. (**) Methods without markers on hands & objects. (***) Printed, textureless objects. 



(a) 

(b) 

(c) 

(d) (e) 

Figure 2: (a) We calibrate cameras using IR sphere markers and PnP [45], (b) create object meshes using BADSLAM [68] on RGB-D captures, and (c) estimate object poses using DenseFusion [86] on RGB-D images and mask images from Mask R-CNN [35]. We then select the pose with the highest confidence among five cameras. (d) Consequently, we detect hand joints with OpenPose [8] and optimize hand shape using Eq. 1. (e) We finally detect and smooth temporally inaccurate poses. 

multi-view RGB-D data. ObMan [34] collects purely synthetic images of hands holding objects. All these works, however, consider only single-hand scenarios and do not focus on action recognition. Similarly to us, FPHA [26] collects egocentric RGB-D frames with action, hand and object pose annotations. However, the dataset relies on mangnetic sensors, which pollute the RGB images, and does not include neither multi-view data nor two-hand poses. 

As shown in Table 1, our dataset is the first including real, multi-view RGB-D data and accurate annotations for the 3D pose of two hands, object pose, and action labels for egocentric 3D interaction recognition. 

**Hand & object pose estimation.** While a significant amount of research has focused on predicting the pose of hands [27, 56, 58, 60, 73, 96, 97, 101] or objects [5, 49, 61, 81, 86, 93] in isolation, joint understanding of hand-object interactions has received far less attention. Considering hands and objects together adds a number of challenges, which require to reason _e.g_ . about occlusions and inter-penetrations. Pioneer works in [1, 82, 83] investigate hand-hand and hand-object interactions relying on optimization frameworks which might be slow and difficult to tune. Tekin et al. [80] and Hasson et al. [33, 34] efficiently estimate hand & object poses directly from RGB images. However they consider only single-hand scenarios. 

**Recognizing interactions.** Action recognition has received a lot of attention in the computer vision community [4, 14, 36, 43, 59, 87, 91]. With the advent of deep learning and the availability of large datasets, significant progress has been made in third-person action recognition [9, 22, 23, 24, 52, 92, 88, 98]. Recently, there has also been an increase in interest for explicitly reasoning about human-object interactions [16, 18, 28, 31, 39, 51, 65, 84, 89, 94, 100] and skeletal action recognition [10, 46, 54, 69, 95], however mostly from third-person viewpoints. 

Recognizing interactions from first-person viewpoints, however, poses a number of specific challenges like large occlusions, fast camera motion and background clutter [50]. While initially the lack of large amounts of data somewhat hindered the development of effective DNN-based methods, 

over the recent years, there has been a renewed interest in the problem. Some approaches leverage multi-modal input like head motion [42, 47, 67, 75] and eye gaze [20, 47]. It is also common to extract features with CNNs and leverage additional 2D cues related to motion, hand location, object location or object class, in isolation [3, 47, 55] or jointly [19, 21, 25, 70, 77]. While all these methods focus on 2D features, recent work [26, 80] suggests that 3D cues (like hand and object pose) can be effective in the context of egocentric action recognition. However, existing methods have focused on single-hand tracking and no attention has been paid so far to estimating the pose of two hands interacting with objects – a scenario which is more representative of the interactions encountered in real-world scenarios. 

## **3. Annotation Method** 

Fig. 2 shows an overview of our annotation pipeline. We capture synchronized RGB-D frames from multiple views with five Azure Kinect cameras [79]. One of the cameras is mounted on a helmet worn by different subjects to capture egocentric frames. We acquire ground-truth hand and object poses in a semi-automated way. First, we scan each object with a Kinect to obtain a complete 3D model. This model is used to track object 6D pose in each frame via DenseFusion [86]. To track hands, we fit the MANO parametric hand model [64] to multi-view depth data in each frame. This automated tracking process may fail on some frames, due to challenges like (self-)occlusions, blur and cluttered background. We therefore manually detect failure cases and remove corresponding poses; such poses can be then replaced via temporal smoothing. Finally, we manually annotate action labels over the sequences. In the following sections, we describe each step of our pipeline in detail. 

### **3.1. Camera Calibration** 

Our setup consists of four static plus one head-mounted RGB-D cameras. We use the factory-calibrated intrinsic parameters accessible via Azure Kinect DK [79]. As for the extrinsic parameters, we obtain them with a calibration method relying on IR reflective spheres. We choose this method to make our setup portable and easy to deploy. 

We place nine IR reflective spheres at random locations in the scene, ensuring that each sphere is visible from all the cameras. In the IR images captured by our cameras to reconstruct depth, such spheres are shown as bright circles, which can be easily detected in an automated way. We compute the center of each sphere and then obtain its 3D location by considering the corresponding pixel in the depth image. Given the 3D location of the nine spheres in each frame, we solve for camera pose via PnP [44]. In order to consistently identify spheres across frames, we define an initial mapping in the first frame and then track it over time. 

Poses computed for the head-mounted camera can exhibit jitter. We smooth them via Kalman filtering [85], under the assumption that the head moves with uniform speed. The overall framework allows us to use multiple cameras during annotation, which eventually increases the fidelity and accuracy of our annotations. 

### **3.2. Object Pose Annotation** 

We obtain accurate per-frame object 6D poses using multi-view images together with camera pose information. We first reconstruct a 3D mesh model for each object. To this end, we scan the object by capturing RGB-D frames with a hand-held Kinect camera moving around it. We feed these frames into a state-of-the-art RGB-D SLAM method, BADSLAM [68], to reconstruct a 3D mesh. We obtain texture for each object in Blender [11]: we project the RGB images obtained at scanning time onto the mesh surface, using the camera pose returned by BADSLAM. 

We leverage these models to train an object pose tracker. First, we train an object mask predictor based on Mask R- CNN [35]. As training data, we use the masks obtained by projecting our 3D models onto the images used for their BADSLAM-based reconstruction. Then, we feed mask predictions together with the corresponding RGB-D images into DenseFusion [86] to estimate object pose. We obtain a pose prediction for each camera view, and select the one with the highest confidence. Finally, we refine this pose estimate via ICP [44]. Namely, we compute a point cloud from each of the five depth images and merge them into a single point cloud by using camera pose information; then, we fit our object model to this point cloud, taking the prediction from DenseFusion as initialization. 

### **3.3. Hand Pose Annotation** 

For hand pose estimation, we rely on the widely used MANO hand model [64]. MANO factorizes human hand shape into a set of identity parameters _β ∈_ R<sup>10</sup> and a set of pose parameters _θ ∈_ R<sup>51</sup> , storing angles for 15 skeleton joints plus global rotation and translation. Formally, we can define MANO as a function _HV_ ( _θ, β_ ) returning a triangulated mesh with _NV_ vertices. We also define the MANO skeleton as a function _HJ_ ( _θ, β_ ) which returns _NJ_ = 21 

joint locations (the 15 original ones plus 6 other for fingertips and wrist, to map to the OpenPose [8] skeleton – see Supp. Mat.). We take the object pose estimated as above, and we leverage it when tracking hand pose. 

We track hands by minimizing at each frame, _f_ , a loss function defined as: 



where _Nc_ is the number of cameras. Here, _Ls_ is a silhouette-based error term, _L_ 2 _D_ and _L_ 3 _D_ measure joint error in 2D and 3D, respectively, _Lp_ and _La_ are regularizers for pose, _Lphy_ penalizes physically implausible interpenetrations between hand and objects, and _Lm_ penalizes distance in 3D between the hand depth data and the MANO surface. Lambdas weight the contribution of each error term. Note that, in order to obtain subject-specific parameters, we minimize Eq. (1) with respect to **_β_** on one frame only. Then, we track hand pose over the sequence by keeping _β_ fixed and optimizing Eq. (1) with respect to _θ_ (for both left and right hands). We omit _β_ from the following equations for simplicity. 

**2D joint error.** We penalize distance in 2D between MANO joints and OpenPose estimates by defining: 



where _J_ 2 _D_ denotes the 2D joint positions pre-computed with OpenPose, and _HJ_ ( _θ_ )[ _i_ ] returns the _i_ th 3D joint location of the MANO skeleton. 

**3D joint error.** Similarly to the 2D joint error, we compute a penalty in 3D by triangulating OpenPose estimates. We found that using this error term helps achieve faster convergence and increase stability. 

**3D mesh surface error.** We obtain a point cloud for hand data by merging the point clouds obtained from each depth image across our different views, and segmenting out the points that do not project onto the hand mask computed as above. Our 3D surface error term penalizes the distance between this point cloud and the MANO surface: 



where _pj_ is the _j_ th point of the point cloud, and _HV_<sup>_⊥_(</sup><sup>_θ_)</sup> denotes the normal of the hand mesh vertex _i_ . 

As shown in Eq. 1, our optimization function further includes a silhouette error term and regularizers for joint angle limits and physical constraints. We refer the reader to the Supp. Mat. for more details on these terms and for an 



<!-- Start of picture text -->
(c)<br>(d)<br><!-- End of picture text -->











<!-- Start of picture text -->
Read Grab Squeeze Spray<br><!-- End of picture text -->

Figure 3: RGB and depth images with the corresponding annotations of hand & object pose, and action label. First row: Left hand keypoints, right hand keypoints, and 3D object bounding box are projected on the RGB image. Second row: Synchronous depth images. Third row: Ground-truth data for hand and object meshes. We provide further examples of ground-truth data in Supp. Mat. ablation study on the influence of different error terms in the annotation accuracy. 

Figure 4: (a) Number of instances per action in the H2O dataset. (b) Average number of frames per each action class. (c) Schematic camera capture setup. Four static cameras can capture parts that can not be observed by the egocentric view. (d) Scene point cloud computed from multi-view data. 

and depth images. To ensure synchronization between multiple cameras, we use physical cables between them. This results in less than 100 microseconds of lag between cameras [79]. As instructed in [79], to avoid interference between multiple depth cameras, we further offset camera captures from one another by 160 microseconds, which results in a total maximum of only 0.74 ms of delay between cameras. We place four different static cameras at arbitrary locations that cover hand-object interactions. An egocentric camera is further mounted on the forehead of a helmet and adjusted by the participants to set egocentric views. We calibrate all of the five cameras with nine IR reflective balls as explained in Sec. 3.1. The data is acquired in three environments ( _e.g_ . hall, office and kitchen) using several different backgrounds. We record videos at a resolution of 1280x720 pixels for both RGB and depth images with a frame rate of 30 fps. Each video corresponds to a series of actions involving various hand-object interactions. 

After running our automated pipeline, we inspect all the frames to identify and remove inaccurate poses. As a final step, we smooth and interpolate poses via Kalman filtering. 

### **3.4. Temporal Action Annotation** 

We provide action labels as verb-noun pairs. We consider 11 verb classes: _grab_ , _place_ , _open_ , _close_ , _pour_ , _take out_ , _put in_ , _apply_ , _read_ , _spray_ and _squeeze_ . As for nouns, we consider 8 classes: _book_ , _espresso_ , _lotion_ , _spray_ , _milk_ , _cocoa_ , _chips_ , _cappuccino_ . By combining verbs and nouns, after excluding pairs which are not represented in our dataset, we obtain a total of 36 action classes. Note that we pick only one verb and one noun for every frame, so there are no overlapping action labels. We select action labels for the entire dataset manually, using the VIA annotation tool [15]. Fig. 3 shows some annotation examples. 

## **4. The H2O Dataset** 

We acquired the images of the H2O dataset in indoor settings in which the subjects interact with eight different objects using both of their hands. The dataset includes 571,645 RGBD frames, and features four participants performing 36 distinct action classes in three different environments. With the methodology described in Sec. 3, we annotate accurate ground-truth data for left and right hand pose, 6D object pose, camera pose and action labels. In our dataset we further provide MANO [64] hand fits for both left and right hand, and high-quality object meshes. In addition, we also compute scene point clouds using the camera poses and the synchronized RGBD data. Altogether, the curated dataset allows for a comprehensive understanding of the egocentric scene. 

### **4.2. Dataset Statistics** 

We divide the dataset into a training and test set. We split the training and test data with a subject-based split where we leave one subject out for testing and the rest for training. We further use a part of the training data of one subject as the validation dataset for model selection. The data from multiple views consists of 344,645 frames for training, 73,380 frames for validation and 153,620 frames for testing. 

We plot the number of instances per action and the average number of frames for each action class in Fig. 4. Action instances are well distributed across the dataset with the least frequent action appearing 21 times. In the dataset, both hands are used in 57.8%, only left hand in 12.4%, and only right hand in 29.8% of the dataset. The length of action clips spans a wide range demonstrating the diversity of the dataset that includes both slow and fast actions. 

### **4.1. Capture Setup** 

Fig. 4(c) demonstrates our data capture setup. We use five Azure Kinect cameras to acquire synchronized RGB 

## **5. Recognizing 3D Hand-Object Interactions** 

Given the rich annotations of H2O, our goal is to construct comprehensive interpretations of egocentric scenes from image sequences to understand human interactions. For this purpose, we propose a unified framework that jointly estimates the poses of two hands & the manipulated objects, and recognizes egocentric interactions. We use this framework to establish baselines on first person interaction recognition and hand & object pose estimation. 

**Pose Prediction.** We build upon the network architecture of [80] to estimate the poses of both left and right hand, and the pose of the manipulated object. While [80] addresses only single hand scenarios, in our case, we aim to predict the pose of both hands. To this end, each frame in a sequence is passed through a fully convolutional network with a backbone of YOLOv2 [63]. We produce a 3D grid as the output of our fully convolutional network, instead of producing a 2D grid as in [63]. To be able to predict the pose of both hands and objects at the same time, we associate each output grid cell with 3 vectors for left hand, right hand and the manipulated object. These vectors contain target values for left hand ( **y** _i_<sup>_h,l_), right hand (</sup><sup>**y**</sup> _i_<sup>_h,r_</sup> ) and object pose ( **y** _i_<sup>_o_),with overall confidence values (</sup><sup>_ch,l_,</sup><sup>_ch,r, co_) for</sup> individual pose predictions. The confidence values are defined on-the-fly during training as a function of the distance of the predicted poses to the ground-truth ones. The final layer of our single-shot network produces, for each cell _i_ , predictions for left hand ( **y** ˆ _i_<sup>_h,l_), right hand (</sup><sup>**y**ˆ</sup> _i_<sup>_h,r_</sup> ) and object ( **y** ˆ _i_<sup>_o_), along with their associated overall confidence values,</sup> _c_ ˆ<sup>_h,l_</sup> _i_<sup>,</sup><sup>_c_ˆ</sup><sup>_h,r_</sup> _i_ and _c_ ˆ<sup>_o_</sup> _i_<sup>.For each frame,the loss function to train</sup> our network is defined as follows: 



While the poses for the left and right hand are defined by 3D joint coordinates, object pose is parameterized by corner points of a 3D bounding box surrounding the object. Given the control point predictions of the network on the 3D bounding box, 6D object pose can be efficiently computed by aligning the predictions to the reference 3D bounding box with a rigid transformation. Predictions with low confidence values are pruned and the ones with high confidence values are selected as pose predictions. **Interaction Recognition.** RNNs have been successfully used before to recognize actions [2, 80]. However they do not fully leverage the special graph structure of the skeleton data for hand-object interactions. Therefore, we resort to parameterizing the left hand skeleton, right hand skeleton and object bounding box as individual graphs and combine them in a multi-graph structure. We then compute the topology of the multi-graph structure using a graph convolutional 













Figure 5: Qualitative results on the _H_ 2 _O_ dataset. We show estimated hand 3D pose, object 6D pose, and action labels. The proposed method can properly handle challenging occlusions. 

network (GCN) by learning the links across hand and object locations that are involved in interaction. While modeling intra-dependencies within a single graph, this framework also allows for learning interdependencies between left hand-right hand, left hand-object, and right hand-object. 

More particularly, we employ a spatiotemporal graph to encode both spatial and temporal information as in STGCN [95] and 2s-AGCN [69]. Standard ST-GCN [95] for human action recognition models structured information between body skeleton joints using 



where **fin** _∈_ R<sup>_Cin×T ×N_</sup> is an input feature map, **Aj** _∈_ R<sup>_N×N_</sup> is an adjacency matrix that represents skeletal connections, **Wj** _∈_ R<sup>_Cout×Cin×_1</sup><sup>_×_1</sup> is a weight vector of 1 _×_ 1 convolutions and **Mj** _∈_ R<sup>_N×N_</sup> is an attention map. Here _j_ denotes the vertex neighborhood defined by the convolutional kernel, _C_ is the number of channels, _T_ is the temporal length and _N_ is the number of vertices. ST-GCN works on a single graph entity, _e.g._ human skeleton, and models intra-skeleton connections with a fixed adjacency matrix. In our case, in addition to intra-graph dependencies, we aim to model also inter-graph dependencies between hands and objects. Since each time different hand and object parts are involved in interactions, a fixed adjacency matrix to model inter-dependencies would not yield optimal results. Therefore, individually for left hand, right hand and object, we employ the following to be able to model their dependencies: 



While **Aj** _,_ **intra** plays the same role as **Aj** in Eq. 6 for left hand, right hand and object, **Aj** _,_ **inter** models interrelated dependencies between hands and objects via static connections between symmetric hand parts and object center. Here, both of these matrices are fixed adjacency matrices as in ST-GCN (Eq. 6). In addition to them, we represent inter-connections between left hand and right hand, left hand and object, and right hand and object with an additional adjacency matrix, **Tj** _,_ **inter** . Differently from **Aj** _,_ **inter** , **Tj** _,_ **inter** is not fixed, but rather parameterized. Its values are unconstrained and jointly optimized with other 

network parameters, which means that the graph topology and edge weights are fully learned from the training data. In addition to **Tj** _,_ **inter** , we also use an additional parameterized adjacency matrix, **Tj** _,_ **intra** that adaptively learns intrarelated dependencies within single graph entities ( _e.g_ . left hand, right hand or object) during interaction. This datadriven model allows us to learn graphs that are fully targeting the hand-object interaction task. 

Note that in contrast to Eq. 6, we do not use an attention map as in [69], since our _parameterized_ adjacency matrices can play the same role of the attention mechanism performed by **Mj** in Eq. 6 to attribute more importance to edges between hands and objects that are involved in interaction. Besides in Eq. 6, if one of the elements of **Aj** is 0, the result will be 0 regardless of the value of **Mj** due to the dot multiplication. Therefore we use addition instead of dot multiplication in Eq. 7 to allow for forming new connections between our graphs. Similarly with [69], we use an additional data-dependent term, **Sj** in our formulation which learns a unique graph for each sample that use the dot product to measure the similarity of the two vertices in an embedding space. 



where **W** _θ_ and **W** _φ_ are the parameters of the embedding functions _θ_ and _φ_ , respectively. Here, embedding functions are chosen as 1 _×_ 1 convolutional layers. 

By stacking the layers defined by Eq. 7, with a total of 10 layers, we build our topology-aware graph convolutional network (TA-GCN) for 3D interaction recognition. It takes at each iteration the combination of **y** ˆ _i_<sup>_h,l_,</sup><sup>**y**ˆ</sup> _i_<sup>_h,r_</sup> and **y** ˆ _i_<sup>_o_as its</sup> initial feature map to model hand object-interactions. We demonstrate learned graph connections for a hand-object interaction scenario in Fig. 8 and analyze our design choices in Sec. 6. We provide further details for the architecture, hyperparameters and training of the pose prediction and interaction recognition models in the Supp. Mat.. 

## **6. Evaluation** 

In this section, we first verify the accuracy of our groundtruth annotations. We then present baseline results on hand & object pose estimation and egocentric action recognition on our dataset. For the latter, we also compare our baseline approach against the state-of-the-art in action recognition and demonstrate the clear benefits of our approach based on hand-object poses with respect to the existing methods. 

### **6.1. Dataset Analysis** 

**Verfication.** We verify the accuracy of our hand-object pose annotations on a random split of our dataset. To that end, we annotate 500 images on 5 different camera views with the fingertips of the hand and the predefined keypoints of the manipulated objects. We then triangulate these 2D 



Figure 6: Contact modelling on H2O. Our dataset facilitates modelling hand-object contact and 3D affordances. 

|Pose feature|Object|Left hand|Right hand|
|---|---|---|---|
|Mean(std)|1.10(_±_0.37)|0.82(_±_0.43)|0.93(_±_0.57)|



Table 2: Hand & object pose verification results (in cm) for evaluating the accuracy of the provided ground-truth data. 

points to get manual 3D annotations for hands and objects. We compute the distance of our annotations to those of the manually created ones to measure the accuracy of our poses. We demonstrate the results of our verification in Table 2. For both hands and the object, the error is approximately within a range of 1 cm, which demonstrates the high precision of our dataset. Our error margin is comparable with those of [32, 102] even though our dataset features more mutual occlusions due to two-hand manipulation. 

**Contact Modelling.** Having precise hand & object pose annotations and meshes, H2O further facilitates modelling hand-object contact [7, 78]. To this end, for each vertex in the hand mesh, we find the nearest vertices on the object within a certain a threshold ( _e.g_ . 2 cm). We then compute a histogram counting the number of neighbors for each vertex of the MANO mesh and normalize it to model contact hotspots on hand. We repeat the same procedure also for the object mesh to create a contact map on the object surface. We visualize example contact maps of our dataset in Fig. 6. 

### **6.2. Experimental Results** 

**Predicting jointly the 3D pose of two hands and the manipulated objects.** We train and evaluate our method using the training, validation and test splits described in Sec. 4.2 and report baseline pose estimation accuracies for hands and objects in Fig. 7. We use the percentage of correctly estimated poses to evaluate hand and object pose estimation accuracy. Specifically, we use the 3D PCK metric for hand pose estimation, and the 2D reprojection and ADD metrics for object pose estimation as in [80]. We demonstrate that our method can reliably predict the pose of two hands and the manipulated objects with a low error margin and constitutes a strong baseline for joint pose estimation of two hands interacting with objects. Note also that our approach constitutes the first method and baseline for estimating the pose of _two hands interacting with objects_ from a single RGB image. We still evaluate our approach against single 









<!-- Start of picture text -->
(a) (b) (c)<br><!-- End of picture text -->

Figure 7: Pose estimation results on the H2O dataset using different thresholds, for (a) hands with 3D PCK metric, and for objects with (b) 2D reprojection and (c) ADD metric. 



<!-- Start of picture text -->
Model Acc. (%)<br>ST-GCN 73.86<br>Model Acc. (%) TA-GCN wo  Sj 73.44<br>LEFT HAND 33.61 Model Acc. (%) TA-GCN wo  Tj , inter 75.52<br>OBJECT 48.55 NO INTERCONNECTION 75.52 TA-GCN wo  Tj , intra 76.76<br>RIGHT HAND 52.70 LEFT HAND-RIGHT HAND 76.76 TA-GCN wo  Aj , inter 76.35<br>BOTH HANDS 58.92 HANDS-OBJECT 78.84 TA-GCN wo  Aj , intra 77.59<br>ALL 79.25 ALL INTERCONNECTIONS 79.25 TA-GCN 79.25<br>(a) (b) (c)<br><!-- End of picture text -->

Table 3: Impact of different (a) input modalities, (b) interconnections and (c) graph terms on interaction recognition accuracy. 

hand-object pose estimation methods of [33, 80], for comparison purposes, in Table 4 and further provide qualitative examples of our pose predictions in Fig. 5. 

**Interaction recognition.** In Table 3(a), we show the influence of different input modalities on the accuracy of interaction recognition on the H2O dataset. To this end, we evaluate the impact of hand & object poses for interaction recognition. Hand pose and object keypoints are predicted through our single pass network described in Sec. 5. We show that the combination of right and left hand pose as well as the combination of hand and object poses significantly improve overall action recognition scores, which demonstrates the individual contributions and the complementary nature of each input modality. We further evaluate the importance of modelling inter-dependencies between both hands and objects in Table 3(b) and demonstrate that modelling interdependencies between left hand & right hand, and hands & objects, boosts the accuracy for recognizing interactions. In Table 3(c), we evaluate the influence of different terms of Eq. 7 and demonstrate that with all the graphs added together, the model obtains the best results compared to the baselines. We visualize the learned connections of our model in Fig. 8. 

We further compare our action recognition accuracy to the state-of-the-art image-based learning methods of C2D [90], I3D [9] and SlowFast [23] using the PySlowFast library [17] and pose-based learning methods of H+O [80] and ST-GCN [95] and show our results in Table 4. Following [17], we train image-based models using a batch size of 16 and a temporal window size of 64 frames with a sampling ratio of 2. We use a ResNet-50 backbone and train the network using SGD with a learning rate of 0 _._ 1. Pose-based methods are trained as in [80, 95], and evaluated with the estimated poses using our method from RGB images of our dataset. Our approach to interaction recognition achieves the highest validation and test accuracy on the H2O dataset, 



Figure 8: Learned graph connections for different layers. We demonstrate the top-20 learned intra-(top) and inter-(bottom) connections at layer 1, 5 and 9, respectively, in each column. The thickness of the connections corresponds to the weight of learned connection value. Hand-object connections are given more weight than hand-hand connections during interaction with an object. Our model attributes more importance to fingertips and DIP joints that are more commonly involved in manipulation. 

|**Method**|Left h.|Right h.|Object|Model<br>|Val acc. (%)<br>|Test acc. (%)<br>|
|---|---|---|---|---|---|---|
|Hasson[33]|**3956**|-|6747|C2D [90]|76.10|70.66|
|Hasson[33]|**.**<br>-|4187|.<br>6605|I3D [9]|85.15|75.21|
|H+O[80]|4142|.<br>-|.<br>4806|SlowFast[23]|86.00|77.69|
|H+O[80]|.<br>-|3886|.<br>5257|H+O [80]|80.49|68.88|
|Ours|4145|.<br>**3721**|.<br>**4790**|ST-GCN [95]|83.47|73.86|
||.|**.**|**.**|OURS(TA-GCN)|**86.78**|**79.25**|



Table 4: Pose errors (left, in mm) and action accuracies (right). Single hand methods of [33, 80] are separately trained for left & right hand. [80, 95] use pose predictions of our method. 

demonstrating the effectiveness of our method and the importance of the 3D pose predictions facilitated by H2O. 

## **7. Conclusion** 

In this paper, we propose a method to collect a dataset of two hands manipulating objects for first person interaction recognition. We provide a rich set of annotations including action labels, object classes, 3D left & right hand poses, 6D object poses, camera poses and scene point clouds. We further propose the first method to jointly recognize the 3D poses of two hands manipulating objects and a novel topology-aware graph convolutional network for recognizing hand-object interactions. Our framework models the interactions between hands and objects in 3D to recognize actions from first-person views and yields state-of-the-art accuracy. We believe that our dataset and experiments can be of interest to communities of 3D hand pose estimation, 6D object pose estimation, hand-object interaction, robotics and action recognition, and help bridge the gap between hand-object interaction and egocentric action recognition. **Acknowledgements.** Taein Kwon was supported by the Microsoft Mixed Reality & AI Z¨urich Lab PhD scholarship. The authors thank Silvano Galliani, Joshua Elsdon, Yana Hasson, Jeff Delmerico, Helen Oleynikova and Mihai Dusmanu for helpful discussions. 

## **References** 

- [1] Luca Ballan, Aparna Taneja, J¨urgen Gall, Luc Van Gool, and Marc Pollefeys. Motion capture of hands in action using discriminative salient points. In _ECCV_ , 2012. 3 

- [2] Fabien Baradel, Natalia Neverova, Christian Wolf, Julien Mille, and Greg Mori. Object level visual reasoning in videos. In _ECCV_ , 2018. 6 

- [3] Gedas Bertasius, Hyun Soo Park, Stella X Yu, and Jianbo Shi. First person action-object detection with egonet. _arXiv preprint arXiv:1603.04908_ , 2016. 3 

- [4] Aaron F. Bobick and James W. Davis. The recognition of human movement using temporal templates. _PAMI_ , 23(3):257–267, 2001. 3 

- [5] Eric Brachmann, Frank Michel, Alexander Krull, Michael Ying Yang, Stefan Gumhold, et al. Uncertainty-driven 6d pose estimation of objects and scenes from a single rgb image. In _CVPR_ , 2016. 3 

- [6] Samarth Brahmbhatt, Cusuh Ham, Charles C. Kemp, and James Hays. ContactDB: Analyzing and predicting grasp contact via thermal imaging. In _CVPR_ , 2019. 2 

- [7] Samarth Brahmbhatt, Chengcheng Tang, Christopher D. Twigg, Charles C. Kemp, and James Hays. ContactPose: A dataset of grasps with object contact and hand pose. In _ECCV_ , 2020. 2, 7 

- [8] Zhe Cao, Gines Hidalgo, Tomas Simon, Shih-En Wei, and Yaser Sheikh. Openpose: realtime multi-person 2d pose estimation using part affinity fields. _PAMI_ , 43(1):172–186, 2019. 3, 4, 13, 14 

- [9] Joao Carreira and Andrew Zisserman. Quo vadis, action recognition? a new model and the kinetics dataset. In _CVPR_ , 2017. 1, 2, 3, 8 

- [10] Ke Cheng, Yifan Zhang, Xiangyu He, Weihan Chen, Jian Cheng, and Hanqing Lu. Skeleton-based action recognition with shift graph convolutional network. In _CVPR_ , 2020. 3 

- [11] Blender Online Community. _Blender - a 3D modelling and rendering package_ . Blender Foundation, Stichting Blender Foundation, Amsterdam, 2018. 4 

- [12] Dima Damen, Hazel Doughty, Giovanni Farinella, Sanja Fidler, Antonino Furnari, Evangelos Kazakos, Davide Moltisanti, Jonathan Munro, Toby Perrett, Will Price, et al. The epic-kitchens dataset: Collection, challenges and baselines. _IEEE Computer Architecture Letters_ , (01):1–1, 2020. 2 

- [13] Dima Damen, Hazel Doughty, Giovanni Maria Farinella, Sanja Fidler, Antonino Furnari, Evangelos Kazakos, Davide Moltisanti, Jonathan Munro, Toby Perrett, Will Price, and Michael Wray. Scaling egocentric vision: The epickitchens dataset. In _ECCV_ , 2018. 2 

- [14] Piotr Doll´ar, Vincent Rabaud, Garrison Cottrell, and Serge Belongie. Behavior recognition via sparse spatio-temporal features. In _International Workshop on Visual Surveillance and Performance Evaluation of Tracking and Surveillance_ , 2005. 3 

- [15] Abhishek Dutta and Andrew Zisserman. The VIA annotation software for images, audio and video. In _Proceedings of the 27th ACM International Conference on Multimedia_ , 2019. 5 

- [16] Victor Escorcia and Juan Niebles. Spatio-temporal humanobject interactions for action recognition in videos. In _ICCV Workshops_ , 2013. 3 

- [17] Haoqi Fan, Yanghao Li, Bo Xiong, Wan-Yen Lo, and Christoph Feichtenhofer. Pyslowfast. https://github.com/ facebookresearch/slowfast, 2020. 2, 8 

- [18] Hao-Shu Fang, Jinkun Cao, Yu-Wing Tai, and Cewu Lu. Pairwise body-part attention for recognizing human-object interactions. In _ECCV_ , 2018. 3 

- [19] Alireza Fathi, Ali Farhadi, and James M Rehg. Understanding egocentric activities. In _ICCV_ , 2011. 3 

- [20] Alireza Fathi, Yin Li, and James M Rehg. Learning to recognize daily actions using gaze. In _ECCV_ , 2012. 3 

- [21] Alireza Fathi, Xiaofeng Ren, and James M Rehg. Learning to recognize objects in egocentric activities. In _CVPR_ , 2011. 3 

- [22] Christoph Feichtenhofer. X3d: Expanding architectures for efficient video recognition. In _CVPR_ , 2020. 1, 3 

- [23] Christoph Feichtenhofer, Haoqi Fan, Jitendra Malik, and Kaiming He. Slowfast networks for video recognition. In _ICCV_ , 2019. 1, 2, 3, 8 

- [24] Christoph Feichtenhofer, Axel Pinz, and Andrew Zisserman. Convolutional two-stream network fusion for video action recognition. In _CVPR_ , 2016. 1, 3 

- [25] David F Fouhey, Wei-cheng Kuo, Alexei A Efros, and Jitendra Malik. From lifestyle vlogs to everyday interactions. In _CVPR_ , 2018. 3 

- [26] Guillermo Garcia-Hernando, Shanxin Yuan, Seungryul Baek, and Tae-Kyun Kim. First-person hand action benchmark with rgb-d videos and 3d hand pose annotations. In _CVPR_ , 2018. 1, 2, 3, 16 

- [27] Liuhao Ge, Yujun Cai, Junwu Weng, and Junsong Yuan. Hand pointnet: 3d hand pose estimation using point sets. In _CVPR_ , 2018. 3 

- [28] Georgia Gkioxari, Ross Girshick, Piotr Doll´ar, and Kaiming He. Detecting and recognizing human-object interactions. In _CVPR_ , 2018. 3 

- [29] Raghav Goyal, Samira Ebrahimi Kahou, Vincent Michalski, Joanna Materzynska, Susanne Westphal, Heuna Kim, Valentin Haenel, Ingo Fruend, Peter Yianilos, Moritz Mueller-Freitag, et al. The” something something” video database for learning and evaluating visual common sense. In _ICCV_ , 2017. 2 

- [30] Chunhui Gu, Chen Sun, David A Ross, Carl Vondrick, Caroline Pantofaru, Yeqing Li, Sudheendra Vijayanarasimhan, George Toderici, Susanna Ricco, Rahul Sukthankar, et al. Ava: A video dataset of spatio-temporally localized atomic visual actions. In _CVPR_ , 2018. 2 

- [31] Tanmay Gupta, Alexander Schwing, and Derek Hoiem. No-frills human-object interaction detection: Factorization, layout encodings, and training techniques. In _ICCV_ , 2019. 3 

- [32] Shreyas Hampali, Mahdi Rad, Markus Oberweger, and Vincent Lepetit. Honnotate: A method for 3d annotation of hand and object poses. In _CVPR_ , 2020. 1, 2, 7, 13 

- [33] Yana Hasson, Bugra Tekin, Federica Bogo, Ivan Laptev, Marc Pollefeys, and Cordelia Schmid. Leveraging photo- 

metric consistency over time for sparsely supervised handobject reconstruction. In _CVPR_ , pages 571–580, 2020. 3, 

8 

- [34] Yana Hasson, Gul Varol, Dimitrios Tzionas, Igor Kalevatykh, Michael J Black, Ivan Laptev, and Cordelia Schmid. Learning joint reconstruction of hands and manipulated objects. In _CVPR_ , 2019. 1, 2, 3, 13 

- [35] Kaiming He, Georgia Gkioxari, Piotr Doll´ar, and Ross Girshick. Mask r-cnn. In _ICCV_ , 2017. 3, 4, 13, 14 

- [36] Hueihan Jhuang, Thomas Serre, Lior Wolf, and Tomaso Poggio. A biologically inspired system for action recognition. In _ICCV_ , 2007. 3 

- [37] Hanbyul Joo, Hao Liu, Lei Tan, Lin Gui, Bart Nabbe, Iain Matthews, Takeo Kanade, Shohei Nobuhara, and Yaser Sheikh. Panoptic studio: A massively multiview system for social motion capture. In _ICCV_ , 2015. 2 

- [38] Hanbyul Joo, Tomas Simon, Xulong Li, Hao Liu, Lei Tan, Lin Gui, Sean Banerjee, Timothy Scott Godisart, Bart Nabbe, Iain Matthews, Takeo Kanade, Shohei Nobuhara, and Yaser Sheikh. Panoptic studio: A massively multiview system for social interaction capture. _PAMI_ , 41(1):190– 204, 2017. 2 

- [39] Keizo Kato, Yin Li, and Abhinav Gupta. Compositional learning for human object interaction. In _ECCV_ , 2018. 3 

- [40] Will Kay, Joao Carreira, Karen Simonyan, Brian Zhang, Chloe Hillier, Sudheendra Vijayanarasimhan, Fabio Viola, Tim Green, Trevor Back, Paul Natsev, et al. The kinetics human action video dataset. _arXiv preprint arXiv:1705.06950_ , 2017. 2 

- [41] Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In _ICLR_ , 2015. 14, 15 

- [42] Kris M Kitani, Takahiro Okabe, Yoichi Sato, and Akihiro Sugimoto. Fast unsupervised ego-action learning for firstperson sports videos. In _CVPR_ , 2011. 3 

- [43] Ivan Laptev. On space-time interest points. _IJCV_ , 64(23):107–123, 2005. 3 

- [44] Vincent Lepetit, Francesc Moreno-Noguer, and Pascal Fua. Epnp: An accurate o (n) solution to the pnp problem. _IJCV_ , 81(2):155, 2009. 4 

- [45] V. Lepetit, F. Moreno-Noguer, and P. Fua. EPnP: An Accurate O(n) Solution to the PnP Problem. _IJCV_ , 81(2):155– 166, 2009. 3 

- [46] Maosen Li, Siheng Chen, Xu Chen, Ya Zhang, Yanfeng Wang, and Qi Tian. Actional-structural graph convolutional networks for skeleton-based action recognition. In _CVPR_ , 2019. 3 

- [47] Yin Li, Alireza Fathi, and James M Rehg. Learning to predict gaze in egocentric video. In _ICCV_ , 2013. 3 

- [48] Yin Li, Miao Liu, and James M Rehg. In the eye of beholder: Joint learning of gaze and actions in first person video. In _ECCV_ , 2018. 2 

- [49] Yi Li, Gu Wang, Xiangyang Ji, Yu Xiang, and Dieter Fox. Deepim: Deep iterative matching for 6d pose estimation. In _ECCV_ , 2018. 3 

- [50] Yin Li, Zhefan Ye, and James M Rehg. Delving into egocentric actions. In _CVPR_ , 2015. 1, 3 

- [51] Yong-Lu Li, Siyuan Zhou, Xijie Huang, Liang Xu, Ze Ma, Hao-Shu Fang, Yanfeng Wang, and Cewu Lu. Transferable interactiveness knowledge for human-object interaction detection. In _CVPR_ , 2019. 3 

- [52] Ji Lin, Chuang Gan, and Song Han. Tsm: Temporal shift module for efficient video understanding. In _ICCV_ , 2019. 3 

- [53] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Doll´ar, and C Lawrence Zitnick. Microsoft coco: Common objects in context. In _ECCV_ , 2014. 14 

- [54] Ziyu Liu, Hongwen Zhang, Zhenghao Chen, Zhiyong Wang, and Wanli Ouyang. Disentangling and unifying graph convolutions for skeleton-based action recognition. In _CVPR_ , 2020. 3 

- [55] Minghuang Ma, Haoqi Fan, and Kris M Kitani. Going deeper into first-person activity recognition. In _CVPR_ , 2016. 3 

- [56] Gyeongsik Moon, Ju Yong Chang, and Kyoung Mu Lee. V2v-posenet: Voxel-to-voxel prediction network for accurate 3d hand and human pose estimation from a single depth map. In _CVPR_ , 2018. 3 

- [57] Gyeongsik Moon, Shoou-I Yu, He Wen, Takaaki Shiratori, and Kyoung Mu Lee. Interhand2. 6m: A dataset and baseline for 3d interacting hand pose estimation from a single rgb image. _arXiv preprint arXiv:2008.09309_ , 2020. 2 

- [58] Franziska Mueller, Dushyant Mehta, Oleksandr Sotnychenko, Srinath Sridhar, Dan Casas, and Christian Theobalt. Real-time hand tracking under occlusion from an egocentric rgb-d sensor. In _ICCVW_ , 2017. 3 

- [59] Juan Carlos Niebles, Hongcheng Wang, and Li Fei-Fei. Unsupervised learning of human action categories using spatial-temporal words. _IJCV_ , 79(3):299–318, 2008. 3 

- [60] Markus Oberweger and Vincent Lepetit. Deepprior++: Improving fast and accurate 3d hand pose estimation. In _ICCVW_ , 2017. 3 

- [61] Sida Peng, Yuan Liu, Qixing Huang, Xiaowei Zhou, and Hujun Bao. Pvnet: Pixel-wise voting network for 6dof pose estimation. In _CVPR_ , 2019. 3 

- [62] Francesco Ragusa, Antonino Furnari, Salvatore Livatino, and Giovanni Maria Farinella. The meccano dataset: Understanding human-object interactions from egocentric videos in an industrial-like domain. _arXiv preprint arXiv:2010.05654_ , 2020. 2 

- [63] J. Redmon and A. Farhadi. YOLO9000: Better, Faster, Stronger. In _CVPR_ , 2017. 6, 15 

- [64] Javier Romero, Dimitrios Tzionas, and Michael J Black. Embodied hands: Modeling and capturing hands and bodies together. _ACM Transactions on Graphics (ToG)_ , 36(6):245, 2017. 3, 4, 5, 14 

- [65] Amir Rosenfeld and Shimon Ullman. Hand-object interaction and precise localization in transitive action recognition. In _2016 13th Conference on Computer and Robot Vision (CRV)_ , pages 148–155. IEEE, 2016. 3 

- [66] Carsten Rother, Vladimir Kolmogorov, and Andrew Blake. ” grabcut” interactive foreground extraction using iterated graph cuts. _ACM transactions on graphics (TOG)_ , 23(3):309–314, 2004. 13, 14 

- [67] Michael S Ryoo and Larry Matthies. First-person activity recognition: What are they doing to me? In _CVPR_ , 2013. 3 

- [68] Thomas Schops, Torsten Sattler, and Marc Pollefeys. Bad slam: Bundle adjusted direct rgb-d slam. In _CVPR_ , pages 134–144, 2019. 3, 4, 14 

- [69] Lei Shi, Yifan Zhang, Jian Cheng, and Hanqing Lu. Twostream adaptive graph convolutional networks for skeletonbased action recognition. In _CVPR_ , 2019. 3, 6, 7, 15 

- [70] Gunnar A Sigurdsson, Abhinav Gupta, Cordelia Schmid, Ali Farhadi, and Karteek Alahari. Actor and observer: Joint modeling of first and third-person videos. In _CVPR_ , 2018. 3 

- [71] Gunnar A Sigurdsson, Abhinav Gupta, Cordelia Schmid, Ali Farhadi, and Karteek Alahari. Charades-ego: A largescale dataset of paired third and first person videos. _arXiv preprint arXiv:1804.09626_ , 2018. 2 

- [72] Gunnar A Sigurdsson, G¨ul Varol, Xiaolong Wang, Ali Farhadi, Ivan Laptev, and Abhinav Gupta. Hollywood in homes: Crowdsourcing data collection for activity understanding. In _ECCV_ . Springer, 2016. 2 

- [73] Tomas Simon, Hanbyul Joo, Iain Matthews, and Yaser Sheikh. Hand keypoint detection in single images using multiview bootstrapping. In _CVPR_ , 2017. 3 

- [74] Karen Simonyan and Andrew Zisserman. Two-stream convolutional networks for action recognition in videos. In _NeurIPS_ , 2014. 1 

- [75] Suriya Singh, Chetan Arora, and CV Jawahar. First person action recognition using deep learned descriptors. In _CVPR_ , 2016. 3 

- [76] Srinath Sridhar, Franziska Mueller, Michael Zollhoefer, Dan Casas, Antti Oulasvirta, and Christian Theobalt. Realtime joint tracking of a hand manipulating an object from rgb-d input. In _ECCV_ , 2016. 1 

- [77] Sudeep Sundaram and Walterio W Mayol Cuevas. High level activity recognition using low resolution wearable vision. In _CVPRW_ , 2009. 3 

- [78] Omid Taheri, Nima Ghorbani, Michael J. Black, and Dimitrios Tzionas. GRAB: A dataset of whole-body human grasping of objects. In _ECCV_ , 2020. 2, 7 

- [79] Azure SDK Team. _Azure Kinect SDK_ . Microsoft, 2020. 3, 5 

- [80] Bugra Tekin, Federica Bogo, and Marc Pollefeys. H+ o: Unified egocentric recognition of 3d hand-object poses and interactions. In _CVPR_ , 2019. 2, 3, 6, 7, 8, 15 

- [81] Bugra Tekin, Sudipta N Sinha, and Pascal Fua. Real-time seamless single shot 6d object pose prediction. In _CVPR_ , 2018. 3 

- [82] Dimitrios Tzionas, Luca Ballan, Abhilash Srikantha, Pablo Aponte, Marc Pollefeys, and Juergen Gall. Capturing hands in action using discriminative salient pointsand physics simulation. _IJCV_ , 2016. 2, 3 

- [83] Dimitrios Tzionas, Abhilash Srikantha, Pablo Aponte, and Juergen Gall. Capturing hand motion with an rgb-d sensor, fusing a generative model with salient points. In _GCPR_ , 2014. 2, 3 

- [84] Bo Wan, Desen Zhou, Yongfei Liu, Rongjie Li, and Xuming He. Pose-aware multi-level feature network for human object interaction detection. In _ICCV_ , 2019. 3 

- [85] Eric A Wan and Rudolph Van Der Merwe. The unscented kalman filter for nonlinear estimation. In _Adaptive Systems for Signal Processing, Communications, and Control Symposium_ , pages 153–158, 2000. 4 

- [86] Chen Wang, Danfei Xu, Yuke Zhu, Roberto Mart´ın-Mart´ın, Cewu Lu, Li Fei-Fei, and Silvio Savarese. Densefusion: 6d object pose estimation by iterative dense fusion. In _CVPR_ , 2019. 3, 4, 14 

- [87] Heng Wang, Alexander Kl¨aser, Cordelia Schmid, and Cheng-Lin Liu. Action recognition by dense trajectories. In _CVPR_ , 2011. 3 

- [88] Limin Wang, Yuanjun Xiong, Zhe Wang, Yu Qiao, Dahua Lin, Xiaoou Tang, and Luc Van Gool. Temporal segment networks: Towards good practices for deep action recognition. In _ECCV_ , 2016. 3 

- [89] Tiancai Wang, Rao Muhammad Anwer, Muhammad Haris Khan, Fahad Shahbaz Khan, Yanwei Pang, Ling Shao, and Jorma Laaksonen. Deep contextual attention for humanobject interaction detection. In _ICCV_ , 2019. 3 

- [90] Xiaolong Wang, Ross Girshick, Abhinav Gupta, and Kaiming He. Non-local neural networks. In _CVPR_ , 2018. 8 

- [91] Shu-Fai Wong, Tae-Kyun Kim, and Roberto Cipolla. Learning motion categories using both semantic and structural information. In _CVPR_ , 2007. 3 

- [92] Chao-Yuan Wu, Christoph Feichtenhofer, Haoqi Fan, Kaiming He, Philipp Krahenbuhl, and Ross Girshick. Long-term feature banks for detailed video understanding. In _CVPR_ , 2019. 1, 3 

- [93] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and Dieter Fox. Posecnn: A convolutional neural network for 6d object pose estimation in cluttered scenes. _arXiv preprint arXiv:1711.00199_ , 2017. 3 

- [94] Tete Xiao, Quanfu Fan, Dan Gutfreund, Mathew Monfort, Aude Oliva, and Bolei Zhou. Reasoning about humanobject interactions through dual attention networks. In _ICCV_ , 2019. 3 

- [95] Sijie Yan, Yuanjun Xiong, and Dahua Lin. Spatial temporal graph convolutional networks for skeleton-based action recognition. In _AAAI_ , volume 32, 2018. 3, 6, 8, 15 

- [96] Qi Ye, Shanxin Yuan, and Tae-Kyun Kim. Spatial attention deep net with partial pso for hierarchical hybrid hand pose estimation. In _ECCV_ , 2016. 3 

- [97] Shanxin Yuan, Guillermo Garcia-Hernando, Bj¨orn Stenger, Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee, Pavlo Molchanov, Jan Kautz, Sina Honari, Liuhao Ge, et al. Depth-based 3d hand pose estimation: From current achievements to future goals. In _CVPR_ , 2018. 3 

- [98] Bolei Zhou, Alex Andonian, Aude Oliva, and Antonio Torralba. Temporal relational reasoning in videos. In _ECCV_ , 2018. 3 

- [99] Luowei Zhou, Chenliang Xu, and Jason J Corso. Towards automatic learning of procedures from web instructional videos. In _AAAI_ , 2018. 2 

- [100] Penghao Zhou and Mingmin Chi. Relation parsing neural network for human-object interaction detection. In _ICCV_ , 2019. 3 

- [101] Christian Zimmermann and Thomas Brox. Learning to estimate 3d hand pose from single rgb images. In _ICCV_ , 2017. 3 

- [102] Christian Zimmermann, Duygu Ceylan, Jimei Yang, Bryan Russell, Max Argus, and Thomas Brox. Freihand: A dataset for markerless capture of hand pose and shape from single rgb images. In _ICCV_ , 2019. 2, 7 

# **Supplementary Material: H2O: Two Hands Manipulating Objects for First Person Interaction Recognition** 

Taein Kwon<sup>1</sup> , Bugra Tekin<sup>2</sup> , Jan St¨uhmer<sup>3</sup><sup>_∗_</sup> , Federica Bogo<sup>1</sup> , and Marc Pollefeys<sup>1</sup><sup>_,_2</sup> 

1ETH Zurich, 2Microsoft, 3Samsung AI Center, Cambridge 

In the supplemental material, we provide further analysis of our annotation method and evaluate different error and regularization terms. Next, we explain how the training images were prepared for object pose estimation. We then provide the implementation details, evaluation metrics and further analysis of our method for joint pose estimation and interaction recognition. We finally present further qualitative results of our method. 

### **S.1. Analysis of the Annotation Method** 

**Influence of different error terms.** In Table S1, we analyze the influence of different error terms in our joint loss function for annotating hand & object poses. To validate the accuracy of our pose estimates, we annotate the fingertips of the hands on 500 images from 5 different views. We start with the silhouette error term, _Ls_ , since it optimizes the shape of the hands. We then progressively add to our loss function, the 2D joint error term ( _L_ 2 _D_ ), the 3D joint error term ( _L_ 3 _D_ ), the physical constraint error term ( _Lphy_ ), and the 3D mesh surface error term ( _Lm_ ). We observe that _L_ 2 _D_ and _L_ 3 _D_ significantly increase joint estimation accuracy. While _Lm_ improves the estimates for subtle hand mesh shape and location, the improvement in joint accuracy is less pronounced. _Lphy_ improves both the physical plausibility and the accuracy of pose annotations. Further smoothing and pose corrections give an additional boost in accuracy. Overall, all the terms of our optimization function in Eq. 9 increase the quality of our pose estimates. 



We provide below additional details for the terms of our loss function. 

**Silhouette error term.** We use object masks obtained using a self-trained Mask RCNN [35]. For hands, we estimate 

*Work performed while at Microsoft. 

hand joint 2D locations in RGB using OpenPose [8], and use them to initialize the GrabCut algorithm [66]. For each camera _c_ , we merge the hand mask obtained via GrabCut with the object mask into a single mask, _Mc,h,o_ , and define our silhouette error term as: 



where _|| · ||_ denotes the 2-norm, Π _c_ ( _·_ ) gives the 2D projection of a 3D point onto the image plane, _Mc,h,o_ [ _j_ ] returns the _j_ th coordinate in the mask of the _c_ th camera, and _HV_ ( _θ_ )[ _i_ ] returns the _i_ th vertex of the hand mesh. We compute Eq. 10 for each camera. 

**Physical constraint regularization.** To avoid physically invalid poses (e.g. a finger inside an object), we regularize our loss function with an additional term as in [34]: 



where _θh_ are hand pose, _θo_ are object pose parameters, _La_ is attraction loss and, _Lr_ is repulsion loss. While repulsion loss penalizes interpenetration of hand and objects, attraction loss penalizes the cases in which hand vertices are in the vicinity of the objects but the surfaces are not in contact. In our experiments, we set _λr_ to 0 _._ 8. 

**Hand joint angle limit regularization.** In our loss function, we further penalize unrealistic joint angles as in [32]: 



where _θa_ [ _k_ ] is the _kth_ joint angle, _θa_ is the lower limit of the angle, and _θa_ is the upper limit of the angle. There exist in total 45 joint angles. As also observed in [32], the PCA space of the MANO hand model does not provide sufficient 

|Terms|_Ls_|_Ls_+_L_2_D_|_Ls_+_L_2_D_+_L_3_D_|_Ls_+_L_2_D_+<br>_L_3_D_ +_Lm_|_Ls_+_L_2_D_+<br>_L_3_D_ +_Lphy_|_Ls_+_L_2_D_+_L_3_D_+<br>_Lphy_ +_Lm_|_Ls_+_L_2_D_+_L_3_D_+<br>_Lphy_ +_Lm_ +_Smoothing_|
|---|---|---|---|---|---|---|---|
|Left Mean (std)|2.87 (_±_1.48)|1.25 (_±_1.12)|1.09 (_±_1.03)|1.08 (_±_1.02)|0.95 (_±_0.79)|0.95 (_±_0.77)|0.82 (_±_0.43)|
|Right Mean(std)|3.02(_±_1.65)|1.31(_±_1.03)|1.11(_±_0.98)|1.11(_±_1.00)|1.05(_±_0.98)|1.04(_±_0.94)|0.93(_±_0.57)|



Table S1: Impact of different error terms in our joint loss function. Errors are given in millimeters (mm). Note that all the experiments include regularization terms, _La_ and _Lp_ , to avoid unrealistic hand poses. 





(a) (b) 





(c) (d) 

Figure S1: We show some examples of (a) our object images and their corresponding masks obtained by projecting the object models, (b) egocentric images and Mask R-CNN results, (c) synthetic images and the corresponding depth images for training DenseFusion, (d) hand masks obtained by GrabCut [66]. 

|Joint|Ind|ex|Mo|ddle|Pin|ky|Ri|ng|Thu|mb|
|---|---|---|---|---|---|---|---|---|---|---|
||Min|Max|Min|Max|Min|Max|Min|Max|Min|Max|
||-0.45|0|0|0|-1.5|0.5|-0.5|0.5|0|2|
|MPC(CMC)|-0.2|0.2|-0.2|0.2|-0.6|0.6|-0.4|0.4|-0.66|0.83|
||-0|2|0|2|0|2|0|2|0|0.5|
||-0.3|0.3|-0.3|0.3|-0.3|0.3|-0.3|0.3|-0.3|0.3|
|PIP(MCP)|0|0|0|0|0|0|0|0|-1|1|
||0|2|0|2|0|2|0|2|0|1|
||0|0|0|0|0|0|0|0|0|0|
|DIP(IP)|0|0|0|0|0|0|0|0|0|0|
||0|1.25|0|1.25|0|1.25|0|1.25|0|1|



Table S2: Hand joint limits we use in computing _La_ . 

details to represent all possible hand poses. Therefore instead we use joint angle space which is more descriptive for hand poses. We calculate the limits of joint angles heuristically and give them in Table S2. 

**Pose prior.** In order to regularize hand pose, we model the distribution of hand poses provided in the MANO dataset [64] as a multivariate Gaussian. Based on this, we define a pose prior, _Lp_ , which penalizes the Mahalanobis distance between both left and right hand pose _θ_ and the learned Gaussian distributions as in [64]. 



where S is the covariance of the hand pose distribution. 

**Pose correction.** To provide an even higher quality for our pose annotations, we inspected our dataset after optimization and selected keyframes on our videos to generate smooth trajectories for hand & object poses. The number of keyframes we choose is reported in Table S3. We fix small errors of hand and object poses via interpolation based on these keyframes. 

**Implementation details of the annotation method.** We further provide implementation details for our annotation method below. 

_Hand joint definition._ The MANO [64] model provides hand joints for 15 locations as shown in Table S2. In order to map hand joints from the MANO skeleton to OpenPose [8] skeleton, we reorganize the order of joints and add wrist & fingertip locations by selecting corresponding points on the MANO mesh as shown in Fig. S2(b). 







<!-- Start of picture text -->
(a)<br><!-- End of picture text -->

(b) 

Figure S2: (a) Object 3D models obtained with our method. We reconstruct textured 3D meshes for 8 different objects. (b) The map of the OpenPose [8] hand skeleton. 

||Object|Left hand|Right hand|
|---|---|---|---|
|# keyframes|107,300|88,342|88,264|
|# interpolated frames|7,029|25,987|26,065|



Table S3: The number of keyframes and interpolated frames for the annotations of hands and objects in our dataset. 

_Object pose estimation network._ We use DenseFusion [86] on multi-view RGBD images to bootstrap our object pose annotations. To this end, we train on the RGB and depth images as well as the corresponding segmentation masks, given in Fig. S1(a). We train the network using ADAM [41] with a learning rate of 0.0001. We generate synthetic training images by superimposing object meshes (Fig. S2(a)) with known 6D poses on random backgrounds and cover a large variety of object poses as shown in Fig. S1(c). We create the object meshes using BADSLAM [68]. 

_Segmentation masks._ To minimize silhouette error term and train DenseFusion, we require segmentation mask for objects. To generate segmentation masks, we train Mask R- CNN [35] with a ResNet-101 backbone. We optimize the network using SGD with a learning rate of 0.001. We obtain training data for masks by projecting our 3D models onto the images as shown in Fig. S1 (a). An example result of Mask R-CNN is shown in Fig. S1 (b). We use randomly selected COCO [53] images for background augmentation (Fig. S1 (c)). As discussed in the main paper, we use GrabCut to generate segmentation masks for hands. We provide an example segmentation mask for hands in Fig. S1 (d). 

|Layer|Type|Filters|Size/Stride|Input|Output|
|---|---|---|---|---|---|
|0|conv|32|3_×_3 / 1|416_×_416_×_3|416_×_416_×_32|
|1|max||2_×_2 / 2|416_×_416_×_32|208_×_208_×_32|
|2|conv|64|3_×_3 / 1|208_×_208_×_32|208_×_208_×_64|
|3|max||2_×_2 / 2|208_×_208_×_64|104_×_104_×_64|
|4|conv|128|3_×_3 / 1|104_×_104_×_64|104_×_104_×_128|
|5|conv|64|1_×_1 / 1|104_×_104_×_128|104_×_104_×_64|
|6|conv|128|3_×_3 / 1|104_×_104_×_64|104_×_104_×_128|
|7|max||2_×_2 / 2|104_×_104_×_128|52_×_52_×_128|
|8|conv|256|3_×_3 / 1|52_×_52_×_128|52_×_52_×_256|
|9|conv|128|1_×_1 / 1|52_×_52_×_256|52_×_52_×_128|
|10|conv|256|3_×_3 / 1|52_×_52_×_128|52_×_52_×_256|
|11|max||2_×_2 / 2|52_×_52_×_256|26_×_26_×_256|
|12|conv|512|3_×_3 / 1|26_×_26_×_256|26_×_26_×_512|
|13|conv|256|1_×_1 / 1|26_×_26_×_512|26_×_26_×_256|
|14|conv|512|3_×_3 / 1|26_×_26_×_256|26_×_26_×_512|
|15|conv|256|1_×_1 / 1|26_×_26_×_512|26_×_26_×_256|
|16|conv|512|3_×_3 / 1|26_×_26_×_256|26_×_26_×_512|
|17|max||2_×_2 / 2|26_×_26_×_512|13_×_13_×_512|
|18|conv|1024|3_×_3 / 1|13_×_13_×_512|13_×_13_×_1024|
|19|conv|512|1_×_1 / 1|13_×_13_×_1024|13_×_13_×_512|
|20|conv|1024|3_×_3 / 1|13_×_13_×_512|13_×_13_×_1024|
|21|conv|512|1_×_1 / 1|13_×_13_×_1024|13_×_13_×_512|
|22|conv|1024|3_×_3 / 1|13_×_13_×_512|13_×_13_×_1024|
|23|conv|1024|3_×_3 / 1|13_×_13_×_1024|13_×_13_×_1024|
|24|conv|1024|3_×_3 / 1|13_×_13_×_1024|13_×_13_×_1024|
|25|route|16||||
|26|conv|64|1_×_1 / 1|26_×_26_×_512|26_×_26_×_64|
|27|reorg||/ 2|26_×_26_×_64|13_×_13_×_256|
|28|route|27 24||||
|29|conv|1024|3_×_3 / 1|13_×_13_×_1280|13_×_13_×_1024|
|30|conv|720|1_×_1 / 1|13_×_13_×_1024|13_×_13_×_10_·_(3_× Nc_+1+_Na_+_No_)|
|31|prediction||||13_×_13_×_5_×_2_×_ (3_×Nc_+1+_Na_+_No_)|



Table S4: Network architecture 

**Example data.** We provide in Fig. S6 and Fig. S7 additional qualitative examples for our ground-truth data, which demonstrate the high fidelity and accuracy of our dataset. 

### **S.2. Analysis of Pose and Interaction Recognition** 

**Implementation details for pose prediction.** We provide in Table S4 the full details of our network architecture. We use YOLOv2 [63] as the backbone of our network. The input to our network model is a 416 _×_ 416 image. At the output layer, we produce a 3D grid instead of a 2D grid with a dimension of 13 _×_ 13 _×_ 5, in width, height and depth axes, respectively. We set the grid cell size in image dimensions to 32 _×_ 32 pixels and in depth dimension to 15cm. We define the confidence of a prediction with a function that is inversely proportional to the distance of the prediction to the ground truth as in [80] with its default parameters. We use ADAM [41] for optimization with a learning rate of 0 _._ 0001. We randomly change the hue, saturation and exposure of our images to augment our training data. 

**Implementation details for interaction recognition.** As shown by Eq. 9 in the main paper, the outputs from two 1 _×_ 1 convolutional layers, **W** _θ_ and **W** _φ_ , are multiplied to form a data dependent adjacency matrix, **Sj** . This is followed by a softmax layer to normalize the elements in the matrix. 

The dimensionality of the input to our overall TA-GCN network is 3 _×_ 200 _×_ 51 (for _C × T × N_ ). We use 21 keypoints from left & right hand as shown in Fig. S2(b) and 9 keypoints from objects (8 corners and 1 center point of a 3D bounding box). This, in total, results in 51 keypoints fed as input to the network. For inputs larger than 200 frames, we randomly sample 200 frames. For inputs smaller than 200 frames, we pad the data by looping the clip. 



Figure S3: Some failure cases of our pose prediction method, due to motion blur, reflection and occlusion. 

||Avg. val error(mm)|Avg. test error(mm)|
|---|---|---|
|Left hand joints|22.05|41.45|
|Right hand joints|30.12|37.21|
|Object vertices|36.20|47.90|



Table S5: Average errors (in mm) for hand & object estimates using our pose prediction approach. 

Each TA-GCN block takes a _C × T × N_ input which is fed into 2D convolutional layer following batch normalization and a ReLu layer. Another batch normalization layer and a dropout layer are placed after the 2D convolutional layer. A skip connection is added to each TA-GCN block to learn more stable features, similarly with 2s-AGCN [69]. We set the size of the vertex neighborhood defined by the convolutional kernel as 2. The convolution for the temporal dimension is the same as ST-GCN [95]. 

To build our TA-GCN, we stack 10 TA-GCN blocks. The consecutive numbers of output channels for TA-GCN blocks are 64, 64, 64, 64, 128, 128, 128, 256, 256, and 256. A fully connected layer following average pooling is used as the last layer to predict the class of action labels. We train the network using SGD with a momentum of 0.9. We set the dropout rate as 0.5 and the batch size as 16. The learning rate starts from 0.005 and is divided by 10 at the 150<sup>th</sup> , 200<sup>th</sup> and 250<sup>th</sup> epoch. 

**Evaluation metrics.** In our paper, we use the percentage of correctly estimated poses to assess the accuracy of pose estimation. Specifically, for hand pose estimation, we use the 3D PCK metric as in [80] and consider a pose estimate to be correct when the mean distance between the predicted and ground-truth joint positions is less than a certain threshold without a rigid alignment. When using the percentage of correct poses to evaluate 6D object pose estimation ac- 



Figure S4: Confusion matrix for interaction recognition . 



Figure S5: Inter-dataset examples when we train both hand poses on our dataset with our method and validate on FPHA [26]. Note that the offsets are observed due to different camera parameters across datasets. Polluted images by the magnetic sensors on the FPHA dataset detriment generalization for right hand poses. 

curacy, we take a pose estimate to be correct if the 2D projection error or the average 3D distance of model vertices is less than a certain threshold (the latter being also referred to as the ADD metric). 

**Confusion matrix for interaction recognition.** We show in Fig. S4 the confusion matrix for interaction recognition. As shown by the strong diagonal of the confusion matrix, our model is able to distinguish between different classes achieving a high accuracy. **Mean errors for hand & object keypoint prediction.** We further provide average keypoint prediction errors for hands and objects in Euclidean distance in Table S5. Keypoints are selected as 21 joint locations for hands and 21 points on the bounding box (1 center point, 8 corner points, 12 midpoints of the edges) for the object. We demonstrate that, with a low error margin, our method constitutes a strong baseline for joint pose estimation of two hands interacting with objects. We provide further qualitative pose estimation results in Fig. S8. 







Figure S6: Some examples of ground-truth data of our dataset for hand & object poses on five different camera views. 







Figure S7: Some examples of ground-truth data of our dataset for hand & object poses on five different camera views. 



Figure S8: Qualitative results of our method that jointly estimates the poses for two hands & objects, along with action and object classes. 

