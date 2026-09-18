# **PianoMime: Learning a Generalist, Dexterous Piano Player from Internet Demonstrations** 

**Cheng Qian Julen Urain Kevin Zakka Jan Peters** TU Munich TU Darmstadt UC Berkeley TU Darmstadt 

**Abstract:** In this work, we introduce PianoMime, a framework for training a piano-playing agent using internet demonstrations. The internet is a promising source of large-scale demonstrations for training our robot agents. In particular, for the case of piano-playing, Youtube is full of videos of professional pianists playing a wide myriad of songs. In our work, we leverage these demonstrations to learn a generalist piano-playing agent capable of playing any arbitrary song. Our framework is divided into three parts: a data preparation phase to extract the informative features from the Youtube videos, a policy learning phase to train songspecific expert policies from the demonstrations and a policy distillation phase to distil the policies into a single generalist agent. We explore different policy designs to represent the agent and evaluate the influence of the amount of training data on the generalization capability of the agent to novel songs not available in the dataset. We show that we are able to learn a policy with up to 56% F1 score on unseen songs. Project website: https://pianomime.github.io/ 

**Keywords:** Imitation Learning, Reinforcement Learning, Dexterous Manipulation, Learning from Observations 

## **1 Introduction** 

The Internet is a promising source of large-scale data for training generalist robot agents. If properly exploited, it is full of demonstrations (video, text, audio) of humans solving an infinite amount of tasks [1, 2, 3] that could inform our robot agents on how to behave. However, learning from these databases is challenging for several reasons. First, unlike teleoperation demonstrations, video data does not specify the actions applied by the robot, usually requiring the use of reinforcement learning to induce the robot actions [4, 2, 5]. Second, videos typically show a human performing the task, while the learned policy is deployed on a robot. This often requires to re-target the human motion to the robot body [5, 6, 7]. Finally, as pointed in [2], if we aim to learn a generalist agent, we must select a task for which large-scale databases are available and that allows an unlimited variety of open-ended goals. 

From opening doors [6] to rope manipulation [8] or pick and place tasks [9, 10], previous works have successfully taught robot manipulation skills through observations. However, these approaches have been limited to low dexterity in the robots or to a small variety of goals. 

In this work, we focus on the task of **learning a generalist piano player from Internet demonstrations** . Piano-playing is a highly dexterous open-ended task [11]. Given two multi-fingered robot hands and a desired song, the goal of a piano-playing agent is to press the correct keys and only the correct keys at the proper timing. Moreover, the task can be conditioned on arbitrary songs, allowing for a large, and high-dimensional goal conditioning. 

Additionally, the Internet is full of videos of professional piano players performing a wide myriad of songs. Interestingly, these piano players often record themselves from a top-view allowing an easy observation of the demonstrations. Additionally, they usually share the MIDI files of the song they play, facilitating the extraction of relevant information. 



Figure 1: The goal of this work is to train a generalist piano-playing agent (PianoMime) from Youtube videos. We collect a set of videos and accompanying MIDI files and train a single agent to play any song, combining reinforcement learning and behavioral cloning. 

To learn a generalist piano-playing agent from internet data, we introduce **PianoMime** , a framework to train a single policy capable of playing any song (See Figure 1). In its essence, the PianoMime agent is a goal-conditioned policy that generates configuration space actions given the desired song to be played. At each timestep, the agent receives as goal input a trajectory of the keys to be pressed. Then, the policy generates a trajectory of actions and executes them in chunk. 

**To learn the agent,** we combine both reinforcement learning with imitation learning. We train individual song-specific expert policies by using reinforcement learning in conjunction with Youtube demonstrations and we distill all the expert policies into a single generalist behavioral cloning policy. **To represent the agent,** we perform ablations of different architectural design strategies to model the behavioral cloning policy. We investigate the benefit of incorporating representation learning to enhance the geometric information of the goal input. Additionally, we explore the effectiveness of a hierarchical policy that combines a high-level policy generating fingertip trajectories with a learned _cross-domain inverse dynamics model_ generating joint-space actions. We show that the learned agent is able to play arbitrary songs not included in the training dataset with around 56% F1-score. 

In summary, **the main contribution** of this work is a framework for training a generalist pianoplaying agent using Internet demonstration data. To achieve this goal, we: 

- Introduce a method to learn policies from the internet demonstrations by decoupling the human motion information from the task-related information. 

- Present a reinforcement learning approach that combines residual policy learning strategies [12, 13] with style reward-based strategies [5]. 

- Explore different policy architecture designs, introducing novel strategies to learn geometrically consistent latent features and conducting ablations on different architectural designs. 

Finally, we are releasing the dataset and the trained models as a benchmark for testing internet-datadriven dexterous manipulation. 

## **2 Related Work** 

**Robotic Piano Playing** Several studies have investigated the development of robots capable of playing the piano. In [14], multiple-targets Inverse Kinematics (IK) and offline trajectory planning are utilized to position the fingers above the intended keys. In [15], a Reinforcement Learning (RL) agent is trained to control a single Allegro hand to play the piano using tactile sensor feedback. However, the piano pieces used in these studies are relatively simple. Subsequently, in [11], an RL agent is trained to control two Shadow Hands to play complex piano pieces by designing a reward function comprising a fingering reward, a task reward, and an energy reward. In contrast with previous approaches, our approach exploits Youtube piano-playing videos, enabling faster training and more accurate and human-like robot behavior. 

**Motion Retargeting and Reinforcement Learning** Our work shares similarities with motion retargeting [16], specifically with those works that combine motion retargeting with RL to learn control policies [17, 18, 5, 19, 6]. Given a mocap demonstration, it has been common to exploit the 

2 

demonstration rather as a reward function [5, 19] or as a nominal behavior for residual policy learning [18, 6]. In our work, we not only extract the mocap information, but also task-related information (piano states) allowing the agent to balance between mimicking the demonstrations and solving the task. 

## **3 Method** 

The PianoMime framework is composed of three phases: data preparation, policy learning, and policy distillation. 

In the **data preparation phase** , given the raw video demonstration, we extract the informative signals needed to train the policies. Specifically, we extract fingertip trajectories and a MIDI file that informs the piano state at every time instant. 

In the **policy learning phase** , we train song-specific policies via RL. This step is essential for generating the robot actions that are missing in the demonstrations. The policy is trained with two reward functions: a style reward and a task reward. The style reward aims to match the robot’s finger movements with those of the human in the demonstrations to preserve the human style, while the task reward encourages the robot to press the correct keys at the proper timing. 

In the **policy distillation phase** , we train a single behavioral cloning policy to mimic all the songspecific policies. The goal of this phase is to train a single generalist policy capable of playing any song. We explore different policy designs and the representation learning of goals to improve the generalization capability of the policy. 

### **3.1 Data preparation: From raw data to human and piano state trajectories** 

We generate the training dataset by web scraping. We download YouTube videos of professional piano artists playing various songs. We particularly choose YouTube channels that also upload MIDI files of the played songs. The MIDI files represent trajectories of the piano state (pressed/unpressed keys) throughout the song. We use the video to extract the motion of human pianists and the MIDI file to inform about the goal state of piano during the execution of the song. 

We select the fingertip position as the essential signal to mimic with the robot hand. While several dexterous tasks might require the use of the palm (e.g. grasping a bottle), we consider mimicking the fingertip motion to be sufficient for the task of piano playing. This will also reduce the constraints applied to the robot, allowing it to adapt its embodiment more freely. 

To extract the fingertip motion from videos, we use MediaPipe [20], an open-source framework for perception. Given a frame from the demonstration videos, MediaPipe outputs the skeleton of the hand. We find that the classical top-view recording in piano-playing YouTube videos is highly beneficial for obtaining an accurate estimate of the fingertip positions. Notice that given the videos are RGB, we lack depth signal. Therefore, we predict the 3D fingertip positions based on the piano state. The detailed procedure is explained in Appendix A. 

### **3.2 Policy learning: generating robot actions from observations** 

Through the data preparation phase, we extract two trajectories: a human fingertip trajectory **_τ_** _x_ and a piano state trajectory **_τ_** ˇ “( . The human fingertip trajectory **_τx_** : p **_x_** 1 _, . . . ,_ **_x_** _T_ q is a _T_ -step trajectory of two hands’ 3D fingertip positions **_x_** P R<sup>3ˆ10</sup> (10 fingers). The piano state trajectory **_τ_** ˇ “( : p<sup>ˇ “</sup> ( 1 _, . . . ,_<sup>ˇ “</sup> ( _T_ q is a _T_ -step trajectory of piano states<sup>ˇ “</sup> ( P B<sup>88</sup> , represented with an 88-dimensional binary variable representing which keys should be pressed. 

Given the ROBOPIANIST [11] environment, **our goal** is to learn a goal-conditioned policy _π_ **_θ_** that plays the song defined by **_τ_** ˇ “( while matching the fingertip motion given by **_τx_** . Notice that satisfying both objectives jointly might be impossible. Tracking perfectly the fingertip trajectory **_τx_** might not necessarily lead to playing the song correctly. Although both trajectories are collected from the same source, errors in hand tracking and embodiment mismatches might lead to deviations, resulting in poor song performance. Thus, we propose using **_τx_** as a style guiding behavior. 

3 



<!-- Start of picture text -->
Observation Fingertip Inverse<br>Encoder  Policy Model<br>FK<br><!-- End of picture text -->

Figure 2: Proposed distillation policy architecture. Given a L steps window of a target song _τ_<sup>_t_</sup> ˇ<sup>“</sup> (<sup>:</sup> p<sup>ˇ “</sup> ( _t_ : _t_ ` _L_ q at time _t_ , a latent representation _τ_ **_z_**<sup>_t_iscomputedgivenapre-trainedobservationencoder.</sup> Then, the policy is decoupled between a high-level fingertip predictor that generates a trajectory of fingertip positions _τ_ **_x_**<sup>_t_andalow-levelinversedynamicsmodelthatgeneratesatrajectoryoftarget</sup> joint position _τ_ **_q_**<sup>_t_.</sup> 

Similarly to [11], we formulate the piano playing as an **Markov Decision Process (MDP)** with the horizon of the episode _H_ , being the duration of the song to be played. The state observation is defined by the robot’s proprioception **_s_** and the goal state **_g_** _t_ . The goal state **_g_** _t_ at time _t_ informs the desired piano key configurations<sup>ˇ “</sup> ( in the future **_g_** _t_ “ p<sup>ˇ “</sup> ( _t_ `1 _, . . . ,_<sup>ˇ “</sup> ( _t_ ` _L_ q, with _L_ being the lookahead horizon. As claimed in [11], to successfully learn how to play, the agent needs to be aware of several steps into the future to plan its actions. The action **_a_** is defined as the desired configuration for both hands **_q_** P R<sup>23ˆ2`1</sup> , each with 23 joint angles and one dimension for the sustain pedal. 

We propose solving the reinforcement learning problem by combining residual policy learning [12, 13, 6] and style mimicking rewards [5, 19]. 

**Residual policy architecture.** Given the fingertip trajectory **_τx_** , we solve an IK [21] problem to obtain a trajectory of desired joint angles **_τq_**<sup>ik: p</sup><sup>**_q_**</sup> 0<sup>ik</sup><sup>_, . . . ,_</sup><sup>**_q_**</sup> _T_<sup>ikq for the robot hands.Then, we represent</sup> the policy _π_ **_θ_** p **_a_** | **_s_** _,_ **_g_** _t_ q “ _π_ **_θ_**<sup>_r_p</sup><sup>**_a_**|</sup><sup>**_s_**</sup><sup>_,_</sup><sup>**_g_**</sup><sup>_t_q`</sup><sup>**_q_**</sup> _t_<sup>ik</sup> `1<sup>as a combination of a nominal behavior (given by the IK</sup> solution) and a residual policy _π_ **_θ_**<sup>_r_.Given the goal state at time</sup><sup>_t_, the nominal behavior is defined as</sup> the next desired joint angle **_q_** _t_<sup>ik</sup> `1<sup>.We then only learn the residual term around the nominal behavior.</sup> In practice, we initialize the robot at **_q_** 0<sup>ikand roll both the goal state and the nominal behavior with a</sup> sliding window along **_τ_** ˇ “( and **_τq_**<sup>ikrespectively.</sup> 

**Style-mimicking reward.** We also integrate a style-mimicking reward to preserve the human style in the trained robot actions. The reward function _r_ “ _r_ ˇ “( ` _r_ **_x_** is composed of a task reward _r_ ˇ “( and a style-mimicking reward _r_ **_x_** . While the task reward _r_ ˇ “( encourages the agent to press the correct keys, the style reward _r_ **_x_** encourages the agent to move its fingertips similar to the demonstration **_τx_** . We provide further details in Appendix C. 

### **3.3 Policy distillation: learning a generalist piano-playing agent** 

Through the policy learning phase, we train song-specific expert policies from which we roll out state and action trajectories _τ_ **_s_** : p **_s_** 0 _, . . . ,_ **_s_** _T_ q and _τ_ **_q_** : p **_q_** 0 _, . . . ,_ **_q_** _T_ q. Then, we generate a dataset _D_ : p _τ_ **_s_**<sup>_i, τ_</sup> **_q_**<sup>_i, τ_</sup> **_x_**<sup>_i, τ i_</sup> ˇ<sup>“</sup> (<sup>q</sup> _i_<sup>_N_</sup> “1<sup>with</sup><sup>_N_being the number of learned songs.Given the dataset</sup><sup>_D_,we apply Be-</sup> havioral Cloning (BC) to learn a single generalist piano-playing agent _π_ **_θ_** p **_q_** _t_ : _t_ ` _L,_ **_x_** _t_ : _t_ ` _L_ | **_s_** _t,_<sup>ˇ “</sup> ( _t_ : _t_ ` _L_ q that outputs configuration-space actions **_q_** _t_ : _t_ ` _L_ and fingertip motion **_x_** _t_ : _t_ ` _L_ conditioned on the current state **_s_** _t_ and the future desired piano state<sup>ˇ “</sup> ( _t_ : _t_ ` _L_ . 

We explore different strategies to represent and learn the behavioral cloning policy and improve its generalization capabilities. In particular, we explore ( **1** ) representation learning approaches to induce spatially informative features, ( **2** ) a hierarchical policy structure for sample-efficient training, and ( **3** ) expressive generative models [22, 23, 24] to capture the multimodality of the data. Also, inspired by current behavioral cloning approaches [22, 25], we train policies that output sequences of actions rather than single-step actions and execute them in chunks. 

**Representation Learning.** We pre-train an observation encoder over the piano state<sup>ˇ “</sup> ( to learn spatially consistent latent features. We hypothesize that two piano states that are spatially close 

4 

should lead to latent features that are close. Using these latent features as goal should induce better generalization. To obtain the observation encoder, we train an autoencoder with a reconstruction loss over a Signed Distance Field (SDF) defined on the piano state. Specifically, the encoder compresses the binary vector of the goal into a latent space, while the decoder predicts the SDF function value of a randomly sampled query point (the distance between the query point and the closest ”on” piano key). We provide further details in Appendix E. 

**Hierarchical Policy.** We represent the piano-playing agent with a hierarchical policy. The highlevel policy receives a sequence of desired future piano states<sup>ˇ “</sup> ( and outputs a trajectory of human fingertip positions **_x_** . Then, a low-level policy takes the fingertip and piano state trajectories as input and outputs a trajectory of desired joint angles **_q_** . On one hand, while fingertip trajectory data is easily available from the Internet, obtaining low-level joint trajectories requires solving a computationally expensive RL problem. On the other hand, while the high-level mapping (<sup>ˇ “</sup> ( ÞÑ **_x_** ) is complex, which involves fingerings, the low-level mapping ( **_x_** ÞÑ **_q_** ) is relatively simpler, which addresses a cross-embodiment inverse dynamics problem. This decoupling allows us to train the more complex high-level mapping on large cheap datasets and the simpler low-level mapping on smaller expensive ones. We visualize the policy in Figure 2. 

**Expressive Generative Models.** Considering that the human demonstration data of piano playing is highly multi-modal, we explore using expressive generative models to better represent this multimodality. We compare the performance of different deep generative models based policies, e.g., Diffusion Policies [22] and Behavioral Transformer [23], as well as a deterministic policy. 

## **4 Experimental Results** 

We split the experimental evaluation into three parts. In the first part, we explore the performance of our proposed framework in learning song-specific policies via RL. In the second part, we perform ablation studies on policy designs for learning a generalist piano-playing agent by distilling the previously learned policies via BC. Finally, in the third part, we explore the influence of the amount of training data on the performance of the test environments. 

**Dataset and Evaluation Metrics** All experiments are conducted on our collected dataset, which contains the notes and the corresponding demonstration videos and fingertip trajectories of 60 piano songs from a Youtube channel **PianoX**<sup>1</sup> . To standardize the length of each task, each song is divided into several clips, each with a duration of 30 seconds (The dataset contains totally 431 clips, 258K state-action pairs). Furthermore, we choose 12 unseen clips to investigate the generalization capability of the generalist policy. We use the same evaluation metrics from RoboPianist [11], i.e., precision, recall, and F1 score. 

**Simulation Environment** Our experiment setup utilizes ROBOPIANIST simulation environment [11], conducted in Mujoco physics simulator [26]. The agent predicts target joint angles at 20Hz and the targets are converted to torques using PD controllers running at 500Hz. We use the same physical setting as [11] with two modifications: 1) The z-axis sliding joints fixed on both forearms are enabled to allow more versatile hand movement. Therefore, the action space of our agent is 47 dimensional (45 dimensional in [11]). 2) We increase the proportional gain of the PD controller for the x-axis sliding joints to enable faster horizontal movement, which we find essential for some fast-paced piano songs. 

### **4.1 Evaluation on learning song-specific policies from demonstrations** 

In this section, we evaluate the song-specific policy learning and aim to answer the following questions: ( **1** ) Does integrating human demonstrations with RL help in achieving better performance? ( **2** ) What elements of the learning algorithm are the most influential in achieving good performance? 

We use Proximal Point Optimization (PPO) [27], because we find that it performs the best compared to other RL algorithms. We compare our model against two baselines: **Robopianist [11]** We use the RL method introduced in [11]. We maintain the same reward functions 

> 1https://www.youtube.com/channel/UCsR6ZEA0AbBhrF-NCeET6vQ 

5 



<!-- Start of picture text -->
Method Without Both Without Residual<br>Baseline Baseline IK Ours Without Mimic With Both<br>1.0<br>0.8<br>0.6<br>Ours 0.4<br>0.2<br>F1 Score<br><!-- End of picture text -->

Figure 3: Left: Qualitative comparison of hand postures. Middle: The F1 score achieved by three methods for 10 chosen clips; Right: The F1 score achieved by excluding different elements in RL. as the original work and manually label the fingering from the demonstrations videos to provide the fingering reward. 

**Inverse Kinematics (IK) [21]** Given a demonstration fingertip trajectory _τ_ **_x_** , a Quadratic Programming-based IK solver [21] is used to compute a target joint position trajectory and execute it open-loop. 

We select 10 clips with diverse levels of difficulty from the collected dataset. We individually train specialized policies for each of the 10 clips using both the baseline and our methods. Subsequently, we assess and compare their performance based on the achieved F1 Score. **Performance.** As shown in Figure 3, our method consistently outperforms the Robopianist baseline for all 10 clips, achieving an average F1 score of 0.94 compared to the baseline’s 0.75. We attribute this improvement to the incorporation of human priors, which narrows the RL search space to a favorable subspace, thereby encouraging the algorithm to converge towards more optimal policies. Additionally, the IK method achieves an average F1 score of 



Figure 4: Qualitative comparison of hand poses. Top: Youtube video, Middle: IK solution given the video. Bottom: After residual RL. 

0.72, only slightly lower than the baseline. This demonstrates the effectiveness of incorporating human priors, providing a strong starting point for RL. 

**Impact of Elements.** Our RL method incorporates two main elements: Style-mimicking reward and Residual learning. We individually exclude each element to investigate their respective influences on policy performance (See Figure 3). We clearly observe the critical role of residual learning implying the benefit of exploiting human demonstrations as nominal behavior. We observe a marginal performance increase of 0.03 when excluding the style-mimicking reward; however, this also results in a larger discrepancy between the fingertip trajectory of the robot and the human. Thus, the weight of the style-mimicking reward can be viewed as a parameter that controls the human likeness of the learned robot actions. 

**Qualitative comparison.** We present a qualitative comparison of the human likeness of the robot motion in Figure 4 and the attached videos. We inspect the hand poses for certain frames and observe that the IK nominal behavior leads the robot to place the fingers in positions similar to those in Youtube videos. The RL policy then slightly adapts the fingertip positions to press the keys correctly. 

### **4.2 Evaluation of model design strategies for policy distillation** 

This section focuses on the evaluation of policy distillation for playing different songs. We evaluate the influence of different policy design strategies on the agent’s performance. We aim to assess ( **1** ) the impact of integrating a pre-trained observation encoder to induce spatially consistent features, ( **2** ) the impact of a hierarchical design of the policy, and ( **3** ) the performance of different generative models on piano-playing data. 

6 

|||Multi-RL|BC-MSE|**Two-Stage Diff**|**-res**|w/o SDF|One-Stage|BeT|
|---|---|---|---|---|---|---|---|---|
|**n**|P|0.85|0.56|0.87|**0.89**|0.86|0.53|0.63|
|**Trai**|R|0.20|0.29|0.78|**0.80**|0.76|0.34|0.42|
||F1|0.12|0.30|0.81|**0.82**|0.78|0.35|0.49|
||P|**0.95**|0.54|0.69|0.71|0.66|0.58|0.53|
|**Test**|R|0.18|0.22|0.54|**0.55**|0.49|0.27|0.30|
||F1|0.13|0.21|0.56|**0.57**|0.51|0.26|0.31|



Table 1: Quantitative results evaluated on Training and Test Datasets. Test datasets consist of 12 clips unseen in the training dataset. We report Precision (P), Recall (R) and F1-score (F1). 

We propose two base policies, **Two-stage Diff** and **Two-stage Diff-res** policy. Both of them utilize hierarchical policies and goal representation learning, as described in Section 3.3. The only difference between them is: the low-level policy of **Two-stage Diff** directly predicts the target joints, while **Two-stage Diff-res** predicts the residual term of an IK solver. Both high- and low-level policies are trained with Denoising Diffusion Probabilistic Models (DDPM) [28]. The high-level policy is trained to predict the fingertip trajectory for 4 timesteps given the SDF embedding (See Appendix E) of goals over 10 timesteps, while the low-level policy predicts the robot actions or residuals for 4 timesteps given the fingertip trajectory. Note that the entire dataset is used for training the high-level policy, while only around 40 % of the collected clips (110K state-action pairs) are trained with RL and further used for training the low-level policy. The detailed network implementation is described in Appendix F. 

Then, to analyze the impact of each variable, we design four variants of the Two-stage Diffusion policy. To evaluate ( **1** ) the impact of integrating a pre-trained observation encoder, we train a model without the SDF embedding representation for the goal ( **w/o SDF** ). To evaluate ( **2** ) the impact of the hierarchical architecture, we train a **One-stage** Diffusion policy that directly predict the joint space actions given the goal. Finally, to evaluate ( **3** ) the influence of using different generative models, we train a Two-stage **BeT** , that replaces Diffusion models with Behavior-Transformers [23]. We also consider as baselines a **Multi-task RL** policy and a **BC** policy with **MSE** Loss. We provide further details of the models in Appendix G. 

**Results** As shown in Table 1, despite that Multi-task RL has the highest precision on the test dataset (this is because it barely presses any keys), our methods (Two-stage Diff and Two-stage Diff-res) outperform the others in all metrics on both training and test datasets. We also observe that the incorporation of SDF embedding for goal representation leads to better performance, especially on the test dataset, which demonstrates the impact of goal representation on policy generalization. Furthermore, we observe a slight performance enhancement when the model predicts the residual term of IK (Two-stage Diff-res). We speculate that this improvement stems from our training data being generated through residual RL, which leverages the output of the IK solver as a prior. This approach likely causes the learned actions to correlate with the outputs of the IK solver. 

### **4.3 Evaluations on the impact of the data in the generalization** 

In this section, we investigate the impact of scaling training data on the generalization capabilities of the agent. We evaluate three policy designs ( **One-stage Diff** , **Two-stage Diff** , and **Two-stage Diff-res** ). We train them using various proportions of the dataset, and evaluate their performance on the test dataset (see Figure 5 Top). Note that One-stage Diff uses the same dataset as the low-level policy of Two-stage Diff. 

**Results.** We observe that both Two-stage Diff and Two-stage Diff-res show consistent performance improvement with increasing used data. This trend implies that the two-stage policies have not yet reached their performance saturation with the given data and could potentially continue to benefit from additional training data in future works. 

7 



Figure 5: Precision and Recall for three different policy architectures trained with varying amount of data volumes evaluated on the test dataset. **Top** : Models are trained with the same proportion of high-level and low-level datasets. **Bottom** : Models are trained with different proportions of highlevel and low-level datasets. The x-axis represents the percentage of the low-level dataset utilized, while HL % indicates the percentage of the high-level dataset used. 

**Evaluation on imbalance training datasets.** We further employ different combinations of the highlevel and low-level policies of Two-stage Diff trained with different proportions of the dataset and assess their performance. In addition, we introduce an oracle high-level policy, which outputs the ground-truth fingertip position from human demonstration videos. The results (see Figure 5 Bottom) demonstrate that the overall performance of policy is significantly influenced by the quality of the high-level policy. Low-level policies paired with Oracle high-level policies consistently outperform the ones paired with other high-level policies. Besides, we observe early performance convergence with increasing training data when paired with a low-quality high-level policy. Specifically, with the HL 1% policy and HL 50%, performance almost converged with around 10% and 50% low-level data, respectively. 

### **4.4 Limitations** 

**Inference Speed** One of the limitations is the inference speed. The models operate with an inference frequency of approximately 15Hz on an RTX 4090 machine, which is lower than the standard real-time demand on hardware. Future works can employ faster diffusion models, e.g., DDIM [29], to speed up the inference. 

**Out-of-distribution Data** Most of the songs in our collected dataset are of modern style. When evaluating the model on the dataset from [11], which mainly contains classical songs, the performance degrades. This discrepancy implies the model’s limited generalization across songs of different styles. Future work can collect more diverse training data to improve this aspect. 

**Acoustic Experience** Although the policy achieves up to 56% F1-score on unseen songs, we found that higher accuracy is still necessary to make the song acoustically appealing and recognizable. Future work should focus on improving this accuracy to enhance the overall acoustic experience. 

## **5 Conclusion** 

In this work, we present PianoMime, a framework for training a generalist robotic pianist using internet video sources. We start by training song-specific policies with residual RL, enabling the robot to master individual songs by mimicking human pianists. Subsequently, we train a single behavioral cloning policy that mimics these song-specific policies to play unseen songs. The policy leverages three key techniques: goal representation learning, policy hierarchy, and expressive generative models. The resulting policy demonstrates an impressive generalization capability, achieving an average F1-score of 70% on unseen songs. This also highlights that leveraging internet data can be highly useful for training generalist robotic agents. 

8 

### **Acknowledgments** 

If a paper is accepted, the final camera-ready version will (and probably should) include acknowledgments. All acknowledgments go at the end of the paper, including thanks to reviewers who gave useful comments, to colleagues who contributed to the ideas, and to funding agencies and corporate sponsors that provided financial support. 

## **References** 

- [1] M. V¨olske, M. Potthast, S. Syed, and B. Stein. Tl; dr: Mining reddit to learn automatic summarization. In _Proceedings of the Workshop on New Frontiers in Summarization_ , pages 59–63, 2017. 

- [2] L. Fan, G. Wang, Y. Jiang, A. Mandlekar, Y. Yang, H. Zhu, A. Tang, D.-A. Huang, Y. Zhu, and A. Anandkumar. Minedojo: Building open-ended embodied agents with internet-scale knowledge. _Advances in Neural Information Processing Systems_ , 35:18343–18362, 2022. 

- [3] K. Grauman, A. Westbury, E. Byrne, Z. Chavis, A. Furnari, R. Girdhar, J. Hamburger, H. Jiang, M. Liu, X. Liu, et al. Ego4d: Around the world in 3,000 hours of egocentric video. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 18995–19012, 2022. 

- [4] F. Torabi, G. Warnell, and P. Stone. Recent advances in imitation learning from observation. _arXiv preprint arXiv:1905.13566_ , 2019. 

- [5] X. B. Peng, P. Abbeel, S. Levine, and M. Van de Panne. Deepmimic: Example-guided deep reinforcement learning of physics-based character skills. _ACM Transactions On Graphics (TOG)_ , 37(4):1–14, 2018. 

- [6] G. Garcia-Hernando, E. Johns, and T.-K. Kim. Physics-based dexterous manipulations with estimated hand poses and residual reinforcement learning. In _2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 9561–9568. IEEE, 2020. 

- [7] X. B. Peng, E. Coumans, T. Zhang, T.-W. Lee, J. Tan, and S. Levine. Learning agile robotic locomotion skills by imitating animals. _Robotics: Science and Systems (RSS)_ , 2020. 

- [8] A. Nair, D. Chen, P. Agrawal, P. Isola, P. Abbeel, J. Malik, and S. Levine. Combining selfsupervised learning and imitation for vision-based rope manipulation. In _2017 IEEE international conference on robotics and automation (ICRA)_ , pages 2146–2153. IEEE, 2017. 

- [9] L. Shao, T. Migimatsu, Q. Zhang, K. Yang, and J. Bohg. Concept2robot: Learning manipulation concepts from instructions and human demonstrations. _The International Journal of Robotics Research_ , 40(12-14):1419–1434, 2021. 

- [10] Y. J. Ma, S. Sodhani, D. Jayaraman, O. Bastani, V. Kumar, and A. Zhang. Vip: Towards universal visual reward and representation via value-implicit pre-training. _arXiv preprint arXiv:2210.00030_ , 2022. 

- [11] K. Zakka, P. Wu, L. Smith, N. Gileadi, T. Howell, X. B. Peng, S. Singh, Y. Tassa, P. Florence, A. Zeng, et al. Robopianist: Dexterous piano playing with deep reinforcement learning. In _Conference on Robot Learning_ , pages 2975–2994. PMLR, 2023. 

- [12] T. Silver, K. Allen, J. Tenenbaum, and L. Kaelbling. Residual policy learning. _arXiv preprint arXiv:1812.06298_ , 2018. 

- [13] T. Johannink, S. Bahl, A. Nair, J. Luo, A. Kumar, M. Loskyll, J. A. Ojea, E. Solowjow, and S. Levine. Residual reinforcement learning for robot control. In _2019 international conference on robotics and automation (ICRA)_ , pages 6023–6029. IEEE, 2019. 

9 

- [14] B. Scholz. Playing piano with a shadow dexterous hand. _PhD thesis, Universitat Hamburg_ , 2019. 

- [15] H. Xu, Y. Luo, S. Wang, T. Darrell, and R. Calandra. Towards learning to play piano with dexterous hands and touch. In _2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 10410–10416. IEEE, 2022. 

- [16] T. Geijtenbeek, M. Van De Panne, and A. F. Van Der Stappen. Flexible muscle-based locomotion for bipedal creatures. _ACM Transactions on Graphics (TOG)_ , 32(6):1–11, 2013. 

- [17] N. Chentanez, M. M¨uller, M. Macklin, V. Makoviychuk, and S. Jeschke. Physics-based motion capture imitation with deep reinforcement learning. In _Proceedings of the 11th ACM SIGGRAPH Conference on Motion, Interaction and Games_ , pages 1–10, 2018. 

- [18] L. Liu and J. Hodgins. Learning basketball dribbling skills using trajectory optimization and deep reinforcement learning. _ACM Transactions on Graphics (TOG)_ , 37(4):1–14, 2018. 

- [19] X. B. Peng, Z. Ma, P. Abbeel, S. Levine, and A. Kanazawa. Amp: Adversarial motion priors for stylized physics-based character control. _ACM Transactions on Graphics (ToG)_ , 40(4): 1–20, 2021. 

- [20] C. Lugaresi, J. Tang, H. Nash, C. McClanahan, E. Uboweja, M. Hays, F. Zhang, C.-L. Chang, M. G. Yong, J. Lee, et al. Mediapipe: A framework for building perception pipelines. _arXiv preprint arXiv:1906.08172_ , 2019. 

- [21] S. Caron, Y. De Mont-Marin, R. Budhiraja, and S. H. Bang. Pink: Python inverse kinematics based on Pinocchio, 2024. URL `https://github.com/stephane-caron/pink` . 

- [22] C. Chi, S. Feng, Y. Du, Z. Xu, E. Cousineau, B. Burchfiel, and S. Song. Diffusion policy: Visuomotor policy learning via action diffusion. _arXiv preprint arXiv:2303.04137_ , 2023. 

- [23] N. M. Shafiullah, Z. Cui, A. A. Altanzaya, and L. Pinto. Behavior transformers: Cloning _k_ modes with one stone. _Advances in neural information processing systems_ , 35:22955–22968, 2022. 

- [24] P. Florence, C. Lynch, A. Zeng, O. A. Ramirez, A. Wahid, L. Downs, A. Wong, J. Lee, I. Mordatch, and J. Tompson. Implicit behavioral cloning. In _Conference on Robot Learning_ , pages 158–168. PMLR, 2022. 

- [25] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn. Learning fine-grained bimanual manipulation with low-cost hardware. _arXiv preprint arXiv:2304.13705_ , 2023. 

- [26] E. Todorov, T. Erez, and Y. Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , pages 5026– 5033, 2012. doi:10.1109/IROS.2012.6386109. 

- [27] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 

- [28] J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic models. _Advances in neural information processing systems_ , 33:6840–6851, 2020. 

- [29] J. Song, C. Meng, and S. Ermon. Denoising diffusion implicit models. _arXiv preprint arXiv:2010.02502_ , 2020. 

- [30] A. Raffin, A. Hill, A. Gleave, A. Kanervisto, M. Ernestus, and N. Dormann. Stable-baselines3: Reliable reinforcement learning implementations. _Journal of Machine Learning Research_ , 22 (268):1–8, 2021. URL `http://jmlr.org/papers/v22/20-1364.html` . 

10 

- [31] D. Hendrycks and K. Gimpel. Gaussian error linear units (gelus). _arXiv preprint arXiv:1606.08415_ , 2016. 

- [32] E. Perez, F. Strub, H. De Vries, V. Dumoulin, and A. Courville. Film: Visual reasoning with a general conditioning layer. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 32, 2018. 

- [33] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In _International conference on machine learning_ , pages 1861–1870. PMLR, 2018. 

11 



<!-- Start of picture text -->
Youtube 𝐻3×3 Mujoco<br><!-- End of picture text -->

Figure 6: Compute homography matrix given 8 correspondence feature points. 

## **A Retargeting: From human hand to robot hand** 

To retarget from the human hand to robot hand, we follow a structured process. **Step 1: Homography Matrix Computation** Given a top-view piano demonstration video, we firstly choose _n_ different feature points on the piano. These points could be center points of specific keys, edges, or other identifiable parts of the keys that are easily recognizable (See Figure 6). Due to the uniform design of pianos, these points represent the same physical positions in both the video and Mujoco. Given the chosen points, we follow the Eight-point Algorithm to compute the Homography Matrix _H_ that transforms the pixel coordinate in videos to the x-y coordinate in Mujoco (z-axis is the vertical axis). 

**Step 2: Transformation of Fingertip Trajectory** We then obtain the human fingertip trajectory with MediaPipe [20]. We collect the fingertips positions every 0.05 seconds. Then we transform the human fingertip trajectory within pixel coordinate into the Mujoco x-y 2D coordinate using the computed homography matrix _H_ . 

**Step 3: Heuristic Adjustment for Physical Alignment** We found that the transformed fingertip trajectory might not physically align with the notes, which means there might be no detected fingertip that physically locates at the keys to be pressed or the detected fingertip might locate at the border of the key (normally human presses the middle point of the horizontal axis of the key). This misalignment could be due to the inaccuracy of the hand-tracking algorithm and the homography matrix. Therefore, we perform a simple heuristic adjustment on the trajectory to improve the physical alignment. Specifically, at each timestep of the video, we check whether there is any fingertip that physically locates at the key to be pressed. If there is, we adjust its y-axis value to the middle point of the corresponding key. Otherwise, we search within a small range, specifically the neighboring two keys, to find the nearest fingertip. If no fingertip is found in the range or the found fingertip has been assigned to another key to be pressed, we then leave it. Otherwise, we adjust its y-axis value to the center of the corresponding key to ensure proper physical alignment. 

**Step 4: Z-axis Value Assignment** Lastly, we assign the z-axis value for the fingertips. For the fingertips that press keys, we set their z-axis values to 0. For other fingertips, we set their z-axis value to 2 ¨ _hkey_ , where _hkey_ is the height of the keys in Mujoco. 

## **B Implementation of Inverse Kinematics Solver** 

The implementation of the IK solver is based on the approach of [21]. The solver addresses multiple tasks simultaneously by formulating an optimization problem and find the optimal joint velocities that minimize the objective function. The optimization problem is given by: 



12 

where _wi_ is the weight of each task, _Ki_ is the proportional gain and _vi_ is the velocity residual. We define a set of 10 tasks, each specifying the desired position of one of the robot fingertips. We do not specify the desired quaternions. All the weights _wi_ are set to be equal. We use quadprog<sup>2</sup> to solve the optimization problem with quadratic programming. The other parameters are listed in Table 2. 

Table 2: The parameters of IK solver 

|**Parameter**|**Value**|
|---|---|
|Gain|1.0|
|Limit Gain|0.05|
|Damping|1e-6|
|Levenberg-Marquardt Damping|1e-6|



## **C Detailed MDP Formulation of Song-specific Policy** 

Table 3: The detailed reward function to train the song-specific policy. The Key Press reward is the same as in [11], where _ks_ and _kg_ represent the current and the goal states of the key respectively, and g is a function that transforms the distances to rewards in the [0, 1] range. _pdf_ and _prf_ represent the fingertip positions of human demonstrator and robot respectively. 

|**Reward**|**Formula**|**Weight**|**Explanation**|
|---|---|---|---|
|Key Press|0_._5¨_g_p}_ks_´_kg_}2q `0_._5¨ p1´**1**false positiveq|2/3|Press the right keys and<br>only the right keys|
|Mimic|_g_p}_pdf_ ´_prf_}2q|1/3|Mimic the demonstrator’s<br>fingertip trajectory|



Table 4: The observation space of song-specific agent. 

|**Observation**|**Unit**|**Size**|
|---|---|---|
|Hand and Forearm Joint Positions|Rad|52|
|Hand and forearm Joint Velocities|Rad/s|52|
|Piano Key Joint Positions|Rad|88|
|Piano key Goal State|Discrete|88|
|Demonstrator Forearm and Fingertips Cartesian Positions|m|36|
|Prior control input ˜_u_(solved by IK)|Rad|52|
|Sustain Pedal state|Discrete|1|



## **D Training Details of Song-specific Policy** 

We use PPO [27] (implemented by StableBaseline 3 [30]) to train the song-specific policy with residual RL(See Algorithm 1). All of the experiments are conducted using the same network architecture and tested using 3 different seeds. Both actor and critic networks are of the same architecture, containing 2 MLP hidden layers with 1024 and 256 nodes, respectively, and GELU [31] as activation functions. The detailed hyperparameters of the networks are listed in Table 7. 

> 2https://github.com/quadprog/quadprog 

13 

Table 5: The action space of song-specific agent. 

|**Action**|**Unit**|**Size**|
|---|---|---|
|Target Joint Positions|Rad|46|
|Sustain Pedal|Discrete|1|



Table 6: The Hyperparameters of PPO 

|**Hyperparameter**|**Value**|
|---|---|
|Initial Learning Rate|3e-4|
|Learning Rate Scheduler|Exponential Decay|
|Decay Rate|0.999|
|Actor Hidden Units|1024, 256|
|Actor Activation|GELU|
|Critic Hidden Units|1024, 256|
|Critic Activation|GELU|
|Discount Factor|0.99|
|Steps per Update|8192|
|GAE Lambda|0.95|
|Entropy Coefficient|0.0|
|Maximum Gradient Norm|0.5|
|Batch Size|1024|
|Number of Epochs per Iteration|10|
|Clip Range|0.2|
|Number of Iterations|2000|
|Optimizer|Adam|



## **E Representation Learning of Goal** 

We train an autoencoder to learn a geometrically continuous representation of the goal (See Figure 7 and Algorithm 2). During the training phase, the encoder _E_ , encodes the original 88-dimensional binary representation of a goal piano state<sup>ˇ “</sup> ( _t_ into a 16-dimensional latent code _z_ . The positional encoding of a randomly sampled 3D query coordinate _x_ is then concatenated with the latent code _z_ and passed through the decoder _D_ . We use positional encoding here to represent the query coordinate more expressively. The decoder is trained to predict the SDF _f_ p _x,_<sup>ˇ “</sup> ( _t_ q. We define the SDF value of _x_ with respect to<sup>ˇ “</sup> ( _t_ as the Euclidean distance between the _x_ and the nearest key that is supposed to be pressed in<sup>ˇ “</sup> ( _t_ , mathematically expressed as: 



where _pi_ represents the position of the _i_ -th key on the piano. The encoder and decoder are jointly optimized to minimize the reconstruction loss: 



We pre-train the autoencoder using the **GiantMIDI** dataset<sup>3</sup> , which contains 10K piano MIDI files of 2,786 composers. The pre-trained encoder maps the<sup>ˇ “</sup> ( _t_ into the 16-dimensional latent code, which serves as the latent goal for behavioral cloning. The encoder network is composed of four 

> 3https://github.com/bytedance/GiantMIDI-Piano 

14 

**Algorithm 1:** Training of the song-specific policy with residual RL 

- 1: Initialize actor network _πθ_ 2: Initialize critic network _vϕ_ 3: **for** _i_ “ 1 : _Niteration_ **do** 4: # Collect trajectories 5: **for** _t_ “ 1 : _T_ **do** 6: Get human demonstrator fingertip position _xt_ and observation _ot_ 7: Compute the prior control signal that tracks _xt_ with the IK controller _u_ ˜ _t_ “ _ik_ p _xt, ot_ q 8: Run policy to get the residual term _rt_ “ _πθ_ p _ot_ q 9: Compute the adapted control signal _ut_ “ _u_ ˜ _t_ ` _rt_ 

- 10: Execute _ut_ in environment and collect _st, ut, rt, st_ `1 11: **end for** 12: # Update networks 13: **for** _n_ “ 1 : _N_ **do** 14: Sample a batch of transitions tp _sj, uj, rj, sj_ `1qu from the collected trajectories 15: Update the actor and critic network with PPO 16: **end for** 17: **end for** 



<!-- Start of picture text -->
Query<br>Coordinate<br>88-dimensional<br>binary vector Positional<br>Embedding<br>1<br>+<br>0<br>Encoder SDF<br>0<br>1<br>Latent<br>1<br>Code<br>...<br><!-- End of picture text -->

Figure 7: 1) Encoding: The encoder compresses the binary representation of the goal into latent code. 2) Decoding: A 3D query coordinate _x_ is randomly sampled. A neural network predicts the SDF value given the positional encoding of _x_ and the latent code. 

1D-convolutional layers, followed by a linear layer. Each successive 1D-convolutional layer has an increasing number of filters, specifically 2, 4, 8, and 16 filters, respectively. All convolutional layers utilize a kernel size of 3. The linear layer transforms the flattened output from the convolutional layers into a 16-dimensional latent code. The decoder network is a MLP with 2 hidden layers, each with 16 neurons. We train the autoencoder for 100 epochs with a learning rate of 1 _e_ ´ 3. 

## **F Training Details of Diffusion Model** 

All the diffusion models utilized in this work, including One-stage Diff, the high-level and low-level policies of Two-stage Diff, Two-stage Diff-res and Two-stage Diff w/o SDF, share 

15 

**Algorithm 2:** Training of the goal autoencoder 



<!-- Start of picture text -->
1: Initialize encoder  Eϕ<br>2: Initialize decoder  Dψ<br>3: for  i  “ 1 :  Nepoch  do<br>4: for  j “ 1 :  Nbatch  do<br>5: for  each goal  v  in batch  do<br>6: Compute the latent code  z  “  Eψ p ˇ “ ( t q<br>7: Sample a 3D coordinate as query  x  “ Sample3DCoordinate()<br>8: Compute the positional encoding of query  pe  “ PositionalEncoding( x q<br>9: Compute the output of the decoder conditioned by the query  Dϕ p z, pe q<br>10: Compute the SDF value of query SDFp x, ˇ “ ( t q<br>11: Compute the reconstruction loss  L<br>12: end for<br>13: Compute the sum of the loss<br>14: Compute the gradient<br>15: Update network parameter  ϕ, ψ<br>16: end for<br>17: end for<br><!-- End of picture text -->

the same network architecture. The network architecture are the same as the U-net diffusion policy in [22] and optimized with DDPM [28], except that we use temporal convolutional networks (TCNs) as the observation encoder, taking the concatenated goals (high-level policy) or fingertip positions (low-level policy) of several timesteps as input to extract the features on temporal dimension. Each level of U-net is then conditioned by the outputs of TCNs through FiLM [32]. 

High-level policies take the goals over 10 timesteps and the current fingertip position as input and predict the human fingertip positions. In addition, we add a standard gaussian noise on the current fingertip position during training to facilitate generalization. We further adjust the y-axis value of the fingertips pressing the keys in the predicted high-level trajectories to the midpoint of the keys. This adjustment ensures closer alignment with the data distribution of the training dataset. Low-level policies take the predicted fingertip positions and the goals over 4 timesteps, the proprioception state as input predict the robot actions. The proprioception state includes the robot joint positions and velocities, as well as the piano joint positions. We use 100 diffusion steps during training. To achieve high-quality results during inference, we find that at least 80 diffusion steps are required for high-level policies and 50 steps for low-level policies. 

Table 7: The Hyperparameters of DDPM 

|**Hyperparameter**|**Value**|
|---|---|
|Initial Learning Rate|1e-4|
|Learning Rate Scheduler|Cosine|
|U-Net Filters Number|256, 512, 1024|
|U-Net Kernel Size|5|
|TCN Filters Number|32, 64|
|TCN Kernel Size|3|
|Diffusion Steps Number|100|
|Batch Size|256|
|Number of Iterations|800|
|Optimizer|AdamW|
|EMA Exponential Factor|0.75|
|EMA Inverse Multiplicative Factor|1|



16 

## **G Policy Distillation Experiment** 

**Two-stage Diff w/o SDF** We directly use the binary representation of goal instead of the SDF embedding representation to condition the high-level and low-level policies. 

**Two-stage Diff-res** We employ an IK solver to compute the target joints given the fingertip positions predicted by the high-level policy. The low-level policy predicts the residual terms of IK solver instead of the robot actions. 

**Two-stage BeT** We train both high-level and low-level policies with Behavior Transformer [23] instead of DDPM. The hyperparameter of Bet is listed in Table 8. 

**One-stage Diff** We train a single diffusion model to predict the robot actions given the SDF embedding representation of goals and the proprioception state. 

**Multi-task RL** We create a multi-task environment where for each episode a random song is sampled from the dataset. Consequently, we use Soft-Actor-Critic (SAC) [33] to train a single agent within the environment. Both the actor and critic networks are MLPs, each with 3 hidden layers, and each hidden layer contains 256 neurons. The reward function is the same as that in [11]. 

**BC-MSE** We train a feedforward network to predict the robot action of next timestep conditioned on the binary representation of goal and proprioception state with MSE loss. The feedforward network is a MLP with 3 hidden layers, each with 1024 neurons. 

Table 8: The Hyperparameters of Behavior Transformer 

|**Hyperparameter**|**Value**|
|---|---|
|Initial Learning Rate|3e-4|
|Learning Rate Scheduler|Cosine|
|Number of Discretization Bins|64|
|Number of Transformer Heads|8|
|Number of Transformer Layers|8|
|Embedding Dimension|120|
|Batch Size|256|
|Number of Iterations|1200|
|Optimizer|AdamW|
|EMA Exponential Factor|0.75|
|EMA Inverse Multiplicative Factor|1|



## **H F1 Score of All Trained Song-Specific Policies** 

Figure 8 shows the F1 score of all song-specific policies we trained. 

## **I Detailed Results on Test Dataset** 

In Table 9 and Table 10, we show the Precision, Recall and F1 score of each song in our collected test dataset and the Etude-12 dataset from [11], achieved by Two-stage Diff and Two-stage Diff-res, respectively. We observe an obvious performance degradation when testing on Etude-12 dataset. We suspect that the reason is due to out-of-distribution data, as the songs in the Etude-12 dataset are all classical, whereas our training and test dataset primarily consists of modern songs. 

17 

Table 9: Quantitative results of each song in the our collected test dataset 

|**Song Name**|**Two-**|**stage Dif**|**f**|**Two-st**|**age Diff-**|**res**|
|---|---|---|---|---|---|---|
||Precision|Recall|F1|Precision|Recall|F1|
|Forester|0.81|0.70|0.68|0.79|0.71|0.67|
|Wednesday|0.66|0.57|0.58|0.67|0.54|0.55|
|Alone|0.80|0.62|0.66|0.83|0.65|0.67|
|Somewhere Only We Know|0.63|0.53|0.58|0.67|0.57|0.59|
|Eyes Closed|0.60|0.52|0.53|0.61|0.45|0.50|
|Pedro|0.70|0.58|0.60|0.67|0.56|0.47|
|Ohne Dich|0.73|0.55|0.58|0.75|0.56|0.62|
|Paradise|0.66|0.42|0.43|0.68|0.45|0.47|
|Hope|0.74|0.55|0.57|0.76|0.58|0.62|
|No Time To Die|0.77|0.53|0.55|0.79|0.57|0.60|
|The Spectre|0.64|0.52|0.54|0.67|0.50|0.52|
|Numb|0.55|0.44|0.45|0.57|0.47|0.48|
|**Mean**|**0.69**|**0.54**|**0.56**|**0.71**|**0.55**|**0.57**|



Table 10: Quantitative results of each song in the Etude-12 dataset 

|**S N**|**Two-**|**stage Dif**|**f**|**Two-st**|**age Diff-**|**res**|
|---|---|---|---|---|---|---|
|**ong ame**|Precision|Recall|F1|Precision|Recall|F1|
|FrenchSuiteNo1Allemande|0.45|0.31|0.34|0.39|0.27|0.30|
|FrenchSuiteNo5Sarabande|0.29|0.23|0.24|0.24|0.18|0.19|
|PianoSonataD8451StMov|0.58|0.52|0.52|0.60|0.50|0.51|
|PartitaNo26|0.35|0.22|0.24|0.40|0.24|0.26|
|WaltzOp64No1|0.44|0.31|0.33|0.43|0.28|0.31|
|BagatelleOp3No4|0.45|0.30|0.33|0.45|0.28|0.32|
|KreislerianaOp16No8|0.43|0.34|0.36|0.49|0.34|0.36|
|FrenchSuiteNo5Gavotte|0.34|0.29|0.33|0.41|0.31|0.33|
|PianoSonataNo232NdMov|0.35|0.24|0.25|0.29|0.19|0.21|
|GolliwoggsCakewalk|0.60|0.43|0.45|0.57|0.40|0.42|
|PianoSonataNo21StMov|0.32|0.22|0.25|0.36|0.23|0.25|
|PianoSonataK279InCMajor1StMov|0.43|0.35|0.35|0.53|0.38|0.39|
|**Mean**|**0.42**|**0.31**|**0.33**|**0.43**|**0.30**|**0.32**|



18 

Figure 8: F1 score of all 184 trained song-specific policies (descending order) 

19 

