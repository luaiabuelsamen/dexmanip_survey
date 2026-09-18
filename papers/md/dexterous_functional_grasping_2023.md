# **Dexterous Functional Grasping** 

**Ananye Agarwal Shagun Uppal Kenneth Shaw Deepak Pathak** Carnegie Mellon University 



<!-- Start of picture text -->
Simulation<br><!-- End of picture text -->

Figure 1: We accomplish functional grasping in the wild using a dexterous hand using a single policy to pickup and functionally grasp objects like hammers, drills, saucepan, staplers and screwdriver in different positions and orientations. We combine the strengths of both internet data and large-scale simulation. An affordance model based on matching DINOv2 features is used to localize the object and move close to the functional region of the object. A blind reactive policy then picks up the object and moves it inside the palm to a firm grasp so that post-grasp motions like drilling, hammering, etc can be executed. Even though the policy only sees hammers at training time (bottom), it generalizes to a much wider set at deployment. Videos at `https://dexfunc.github.io/` . 

**Abstract:** While there have been significant strides in dexterous manipulation, most of it is limited to benchmark tasks like in-hand reorientation which are of limited utility in the real world. The main benefit of dexterous hands over two-fingered ones is their ability to pickup tools and other objects (including thin ones) and grasp them firmly in order to apply force. However, this task requires both a complex understanding of functional affordances as well as precise low-level control. While prior work obtains affordances from human data this approach doesn’t scale to lowlevel control. Similarly, simulation training cannot give the robot an understanding of real-world semantics. In this paper, we aim to combine the best of both worlds to accomplish functional grasping for in-the-wild objects. We use a modular approach. First, affordances are obtained by matching corresponding regions of different objects and then a low-level policy trained in sim is run to grasp it. We propose a novel application of eigengrasps to reduce the search space of RL using a small amount of human data and find that it leads to more stable and physically realistic motion. We find that eigengrasp action space beats baselines in simulation and outperforms hardcoded grasping in real and matches or outperforms a trained human teleoperator. Videos at `https://dexfunc.github.io/` . 

**Keywords:** Functional Grasping, Tool Manipulation, Sim2real 

7th Conference on Robot Learning (CoRL 2023), Atlanta, USA. 

## **1 Introduction** 

The human hand has played a pivotal role in the development of intelligence – dexterity enabled humans to develop and use tools which in turn necessitated the development of cognitive intelligence. [1, 2, 3, 4, 5] Dexterous manipulation is central to the day-to-day activities performed by humans ranging from tasks like writing, typing, lifting, eating, or tool use. In contrast, the majority of robot learning research still relies on using two-fingered grippers (usually parallel jaws) or suction cups which makes them restricted in terms of the kind of objects that can be grasped and how they can be grasped. For instance, grasping a hammer using a parallel jaw is not only challenging but also inherently unstable due to the center of mass of the hammer being close to the head, which makes it impossible to use it for its intended hammering function. Although there are lots of recent works in learning control of dexterous hands, they are either limited to simple grasping or the tasks of in-hand reorientation [6, 7, 8, 9, 10, 11] which ignore the functional aspect of picking the object for tool use. 

This paper investigates the problem of functional grasping of such complex daily life objects using the low-cost dexterous LEAP hand [12]. Consider the sequence of events that take place when one uses a hammer. First, the hammer must be detected and localized in the environment. Next, one must position their hand in a pose perpendicular to the handle such that a suitable grasp pose may be initiated. A hammer may be stably grasped from both the hammer or the head and choosing the correct pose (also known as _pre-grasp pose_ ) requires an understanding of how hammers work. Next, the actual grasping motion is executed which is a high-dimensional closed-loop operation involving first picking up the hammer from the table and then moving it with respect to the hand into a firm power grasp. Power grasp is essential to ensure the stability of the hammer during usage. Once this is done, the arm can then execute the hammering motion while the hand holds it stably ( _post-grasp trajectory_ ). Notably, the act of functional grasping, which is almost a muscle memory for humans, is not just a control problem but lies at the intersection of perception, reasoning, and control. How to do it seamlessly in a robot is the focus of our work. 

Inspired by the above example, we approach the problem of functional grasping in three stages: predicting pre-grasp, learning low-level control of grasping, post-grasp trajectory. Out of these stages, visual reasoning is the critical piece of the first and third stage, while the second stage can be performed blind using proprioception as long as the pre-grasp pose is reasonable. To obtain the pregrasp pose, we use a one-shot affordance model that gives pre-grasp keypoints for different objects in different orientations by finding correspondences across objects. To obtain these correspondences, we leverage a pretrained DinoV2 model [13] which is trained using self-supervised learning on internet images. This allows us to generalize across object instances. However, a more challenging problem is how to learn the low-level control for functional grasping the task itself. 

We take a sim2real approach for the grasping motion in our approach. Prior approaches to sim2real have shown remarkable success for in-hand reorientation [7, 6] and locomotion [14, 15, 16, 17]. However, we observe that directly applying prior sim2real methods that have shown success in locomotion or reorientation yields unrealistic finger-gaiting results in simulation that are not transferrable to the real world. This is because grasping tools typically involve continuous surface contacts and high forces while maintaining the grasping pose – challenges which pose a significant sim2real gap and are nontrivial to engineer reward for. We introduce an action compression scheme to leverage a small amount of human demo data to reduce the action space of the hand from 16 to 9 and constrain it to output physically realistic poses. We evaluate our approach across 7 complex tasks in both the real world and simulation and find that our approach is able to make significant progress towards this major challenge of dexterous functional grasping as illustrated in Figure 1. 

## **2 Method: Dexterous Functional Grasping** 

In this paper, we aim to combine the best of both internet data and large scale simulation training to accomplish dexterous functional grasping in the real world. Given an object to grasp we use an affordance model to predict a plausible _functional_ grasp pose for the hand. Then, we train a blind 

2 



<!-- Start of picture text -->
Affordance from<br>internet data Robust grasping policy from large-scale RL in sim Post-grasp<br>Human-annotated  VR play data<br>exemplar  Teleop<br>DiNOv2<br>feature  Motion<br>matching Capture<br>Intersection   16-dim  PCA Passive<br>with mask hand poses data<br>9-dim action space Large-scale sim training<br><!-- End of picture text -->

Figure 2: We divide the problem into three phases - pre-grasp, grasping and post-grasp. This combines large-scale data from both internet and simulation. Internet data helps to generalize to a large set of visually diverse objects and tells the robot ‘where’ to grasp. Simulation data allows training adaptive policies that work with objects of different physical properties and are even robust to errors in the pre-grasp. (1) To get the pre-grasp pose we use a one-shot affordance model. After annotating one object we are able to get affordances for other objects in that category via feature matching. Given a new object, the arm is moved to that point and oriented perpendicular to the principal component of the object mask. (2) Next, a policy trained in simulation is executed. We use a novel eigengrasp action space reduction to make training feasible. A small dataset of hand poses is colleted and 9 eigengrasps are extracted from it. The policy is trained in the linear space of these grasps. 

pickup policy to pickup the object and then grasp it tightly so that the arm may execute the post-grasp trajectory. Our method is divided into three phases - the pre-grasp, grasp and post-grasp (see Fig. 2) 

In the pre-grasp phase, an affordance model outputs a region of interest of the object and we use the local object geometry around that region to compute a reasonable pre-grasp pose. We train a sim2real policy to execute robust grasps for pickup. However, in contrast to two fingered manipulation or locomotion where simple reward functions suffice, in the complex high-dimensional dexterous case it is easy to fall into local minima or execute poses in simulation that are not realizable in the real world. We therefore use human data to extract a lower-dimensional subspace of the full action space and run RL inside the restricted action space. Empirically, this leads to physically plausible poses that can transfer to real and stabler RL training. Overall, decomposing the pipeline in this way allows us to generalize to a wide range of objects. Because of the affordance model trained on internet data our blind policy generalizes to a wide range of objects even though it only sees hammers at training time. 

### **2.1 Pre-grasp pose from affordances** 

An affordance describes a region of interest on the object that is relevant for the purpose of using it. This usually cannot be inferred from object geometry alone and depends upon the intended proper use of the object. For instance, by just looking at the geometry or by computing grasp metrics we could conclude that grabbing a hammer from the head or handle are both equally valid ways of using it. However, because we have seen other people use it we know that the correct usage is to grab the handle. This problem has been studied in the literature and one approach is to use human data in the form of videos, demos to obtain annotations for affordances. However, these are either not scalable or too noisy to enable zero-shot dexterous grasping. 

Another approach is to use the fact that affordances across objects correspond. For all hammers, no matter the type the hammering, affordance will always be associated with the handle. This implies that feature correspondence can be used in a one-shot fashion to obtain affordances. In particular, we use Hadjivelichkov et al. [18], where for each object category we annotate one image from the internet with its affordance mask. To obtain the affordance mask for a new object instance we simply match DINO-ViT features to find the region which matches the specified mask. Since the mask may bleed across the object boundary we take its intersection with the segment obtained using 

3 



<!-- Start of picture text -->
Top View<br>Side View Front View<br><!-- End of picture text -->

Figure 3: Hardware setup with LEAP hand mounted on xarm6 with one D435 along each axis. 



Figure 4: Affordance prediction for an upright drill from multiple angles. The best angle of approach is from the side and that is also the angle with highest affordance score. Our system picks this angle and then grasps. 

DETIC [19]. Taking the center of the resulting mask gives us the keypoint ( _x_ img _, y_ img) in image space corresponding to the pre-grasp position. To get the _z_ img, we project to the points ( _x_ img _, y_ img) into the aligned depth image and then transform by camera intrinsics and extrinsics to get the corresponding point in the coordinate frame of the robot ( _x_ robot _, y_ robot _, z_ robot). To get the correct hand orientation **q** we use the object mask obtained from DETIC and take the angle perpendicular to its largest principal component. Since there are three cameras, one each along _x, y, z_ axes (Fig. 3) we repeat this process for each camera and pick the angle that has the highest affordance matching score (see Fig. 4, 9). This allows us to grasp objects in any direction, like upright drills and glasses. 

Given the pregrasp pose, we first move the hand to a point at fixed offset ( _x_ robot _, y_ robot _, z_ robot) + _δ_ **v** where _δ_ **v** is a fixed offset along the chosen grasp axis. We then move the finger joints to a pre-grasp pose with the joint positions midway between their joint limits. We found that same pre-grasp pose to work well across objects since our policy learns to adapt to the inaccuracies in the pre-grasp. 

### **2.2 Sim2real for dexterous grasping** 

Once the robot is in a plausible pre-grasp pose it must execute the grasp action which involves using the fingers to grip the object and then moving it into a stable grasp pose. This requires high frequency closed-loop control. Further, this is typically a locally reactive behavior which can be accomplished using proprioception alone. Indeed, once we move our hand close to the object we wish to grasp we can usually pick it up even if we close our eyes. However, the challenge is that learning high frequency closed loop behavior typically requires a lot of interaction data which is missing from human videos and infeasible to scale via demos. Sim2real has been effective in locomotion and in-hand dexterous manipulation for learning robust and reactive policies and we use this method. 

Dexterous manipulation however presents a unique challenge because of its high-dimensional nature. It is easy for the hand to enter physically inconsistent poses or experience self collisions. Further, RL in high dimensional action spaces is unstable or sample efficient. We propose to leverage a small amount of human data to restrict the action space to physically realistic poses. 

**Eigengrasp action space** A small number of human demos are often used to guide RL towards reasonable solutions like offline RL [20], DAPG [21]. However, the problem with these is that they fail to learn optimal behavior from highly suboptimal demos. The coverage of the demo data may be very poor which can artificially restrict the exploration space of the RL algorithm. We propose a simple alternative to these approaches which works from a few demos and can discover optimal behaviors even from suboptimal data. Our insight is that we desire a very weak constraint on the behavior of the policy. We care that the hand poses to are realistic and not so much about the exact sequence in which they occur. We can therefore restrict the action space to only realistic hand poses. 

In particular, suppose we are given a mocap dataset _D_ = _{τ_ 1 _, . . . , τn}_ where _τi_ = ( **x** 1 _, . . . ,_ **x** _k_ ) and **x** _i ∈_ R<sup>16</sup> is a set of joints angles of the 16 dof hand. We perform PCA on the set of all hand poses to get 9 eigenvectors **e** 1 _, . . . ,_ **e** _m_ where _m_ = 9. These vectors are called eigengrasps [22] and have been classically used in grasp synthesis approaches. Here, we instead use it as a compressed action space for RL. Our policy predicts _m_ -dimensional actions _π_ ( **o** _t_ ) = **a** _t ∈_ R<sup>_m_</sup> . The raw joint angles are then computed as a linear combination of eigenvectors ( **at** )1 **e** 1 + _. . ._ + ( **at** ) _k_ **e** _k_ . This transformation 

4 

reduces the action dimension of the RL problem and decreases sample complexity in addition to enforcing realism. It also exploits the property that the convex combination of any two realistic hand poses is also likely to be realistic. Thus, doing PCA (as opposed to training a generative model) allows the policy to output hand poses that were not seen in the dataset. Empirically, we find that this stabilizes training and minimizes variation between different random seeds. 

**Rewards** We train our policy to lift objects off the ground and them firmly grasp them in their hand. We find that a simple reward function that is a combination of two terms _r_ threshold and _r_ hand-obj is enough. The first, is a binary signal incentivizing the policy to pickup the object _r_ threshold( _t_ ) = I [( **r** obj( _t_ )) _z ≥_ 0 _._ 04cm] and the second is a sum of exponentials and an L2 distance to incentivize the object to be close to the palm of the hand 



where _d_ 1 = 10cm, _d_ 2 = 5cm and _d_ 3 = 1cm. The overall reward function is _r_ ( _t_ ) = _r_ hand-obj( _t_ ) + 0 _._ 1 _· r_ threshold( _t_ ) + 1. Due to the eigengrasp parameterization additional reward shaping is not needed. 

**Training environment** We want our policy to be robust to different surface properties and geometries and grasp them firmly. We therefore domain randomize the physical properties of the object, robot and simulation environment. We procedurally generate a set of hammers in simulation with randomized physical parameters. The hand is initialized in a rough pre-grasp pose with hand joint angles zeroed out. This corresponds to a neutral relaxed pose for the hand. The end-effector pose is initialized to be close to the real world pose obtained from the affordance model. The arm is kept close to the ground for 1s to allow the grasp to execute and then spun around in a circle. Episodes are terminated if the hand object distance exceeds 20cm. This spinning motion produces tight grasps and we see emergent behavior where the hand adjusts its grasp in response to changes in orientation (Sec. 4.3). We also randomize physical properties and add gaussian noise to observations and actions (Tab. 4). 

### **2.3 Post-grasp trajectory** 

Once the object or tool is firmly grasped, since it is mounted on a 6-dof arm it can be moved arbitrarily in space to accomplish tasks such as screwing, hammering, drilling, etc. During training and evaluation we use either mocap trajectories or define keypoints and interpolate between them, but these could be obtained from other sources such as internet video or third person imitation. 

## **3 Experimental Setup** 

We demonstrate the performance of our method on a variety of objects, like stapler, drill (light and heavy), saucepan, hammer (light and heavy). In our real world experiments, we aim to understand the reliability and efficiency of our method relative to an expert _teleop oracle_ (20 hours) and a _hardcoded_ grasping primitive. The former acts as an upper bound on the performance of the hardware while the latter is designed to show that large scale sim training yields a more robust policy than naive hardcoding. Note that our blind policy only sees hammers at training time so screwdrivers, staplers, drills and saucepan are out-of-distribution. 

In simulation, we test the effectiveness of our restricted action space and policy architecture. First, we compare against an _unconstrained_ baseline that operates in the full 16 dimensional action space. Second, we compare against a policy that operates in the latent space of a _VAE_ trained on the mocap dataset. Unlike our method, since a VAE is a generative model it can only output hand poses seen in the dataset and cannot extrapolate to new ones. Finally, we compare to a _feedforward_ version of our method where the RNN policy is replaced by a feedforward one. This is designed to test whether recurrence helps in adaptation to domain randomization. 

We experimentally validate the pre-grasp affordance matching [18] part of our pipeline separately. We compare against CLIPort [23] and CLIPSeg [24], two CLIP-based affordance prediction methods. 

5 

||Hammer|Average Reward<br>Drill|Screwdriver|Hammer|Success Rate<br>Drill|Screwdriver|
|---|---|---|---|---|---|---|
|Unconstrained|213_._40_±_169_._37|102_._12_±_36_._12|121_._28_±_96_._05|0_._60_±_0_._55|0_._09_±_0_._11|0_._46_±_0_._45|
|VAE|140_._60_±_109_._24|83_._34_±_43_._32|117_._25_±_76_._26|0_._30_±_0_._44|0_._08_±_0_._18|0_._25_±_0_._41|
|Feed-forward|232_._80_±_175_._59|104_._61_±_44_._84|153_._19_±_105_._83|0_._60_±_0_._54|0_._21_±_0_._19|0_._56_±_0_._52|
|**Ours**|**327**_._**40**_±_**11**_._**61 **|**129**_._**03**_±_**22**_._**58 **|**211**_._**13**_±_**11**_._**14**|**1**_._**00**_±_**0**_._**00 **|**0**_._**23**_±_**0**_._**16 **|**0**_._**95**_±_**0**_._**10**|



Table 1: We measure the average reward and success rate of the trained policy in simulation. For each method we train a policy to hold the object close to the palm while arm spins. A success is counted when the arm does not drop the object at anytime. We see that our method outperforms the baselines and has significantly less variation between the runs. This is likely because the restricted action space makes the exploration problem easier and the physically plausible poses help keep the motion smooth. Each policy was trained randomized hammer but still generalizes to other different objects. 

CLIPort uses demonstration data to learn the correct affordances in a supervised fashion. CLIPSeg uses CLIP text and image features to zero-shot segment an object given a text prompt. 

## **4 Results and Analysis** 

### **4.1 Simulation Results** 

We train each baseline and our method for 400 epochs over 5 seeds. We find that ours beats all other methods primarily because it is stable with respect to the seed whereas the other baselines fluctuate widely in performance across seeds resulting in a high standard deviation and lower average overall performance. Note that our method also perfectly solves the training task for all seeds. This is likely due to a combination of two factors (a) the restricted action space nearly halves the action dimension (from 16 to 9), since the search space scales exponentially with action dimension this cuts down the space significantly and it is more likely that the algorithm discovers optimal behavior regardless of seed, and (b) since each hand pose is realistic and doesn’t have self-collisions it leads to smoother and more predictable dynamics in simulation allowing the policy to learn better. 

The RNN policy is also better and more stable than the feedforward variant as reported in Table 1. This is because (a) an RNN can use the hidden state to adapt to domain randomization (b) since the hand hardware does not output joint velocities, the feedforward policy has no idea of how fast the fingers are moving which can hinder performance. The RNN on the other hand is able to implicitly capture velocity of joints in the hidden state and this helps it to learn better. 

### **4.2 Real World Results** 

We choose a variety of objects to compare Success Rate _↑_ against – hammer and drill (light and heavy), Teleop Oracle Hardcoded Ours saucepan, stapler and screwdriver. Of these, Hammer (heavy) 0.5 0.0 0.8 hammer and saucepan are quite similar to the Hammer (light) 0.6 0.3 0.9 training distribution because of the handle geSauce pan 0.9 0.3 0.9 Drill (heavy) 0.9 0.2 0.5 ometry while the drill, stapler and screwdriver Drill (light) 0.9 0.3 0.8 have substantially different geometry. The heavy Stapler 0.9 0.3 1.0 drill is especially challenging because of its narScrewdriver 0.5 0.0 0.7 row grip and unbalanced weight distribution. We run 10 trials per object per baseline in the Table 2: We compare to a hardcoded pinch grasp and a trained teleoperator with a VR glove. The hardcoded real world (see Table 2). For all objects except baseline fails since the fingers push the object behind. the saucepan, we execute a post-grasp trajecOur method is able to beat the teleop oracle on challengtory where the object is picked up and waved ing objects such as screwdriver, stapler and hammer. around to test the strength of the grasp. For the saucepan, we simply pick it up since waving it around is a safety hazard. During each trial, the orientation is randomized in the range [ _−π, π_ ] and position is randomized in 1m _×_ 0 _._ 5m, the affordance model is run and the hand is moved to the pre-grasp pose. Videos at `https://dexfunc.github.io/` . 

6 

||Hammer (un|seen)|Spatula (seen)|Frying Pan|(seen)|
|---|---|---|---|---|---|
||Pick success|IoU|Pick success<br>IoU|Pick success|IoU|
|CLIPort|2/10|0.034|6/10<br>0.15|7/10|0.15|
|ClipSeg|1/10|0.05|2/10<br>0.06|1/10|0.014|
|Ours|**9/10**|**0.33**|**8/10**<br>**0.23**|**7/10**|**0.17**|



Table 3: We compare our affordance matching against CLIPort and CLIPSeg in terms of pick success rate and IoU between the predicted and ground truth affordance (human-annotated). We use the simulated CLIPort dataset for both unseen and seen objects. Our method outperforms CLIPort on both seen and unseen categories. CLIPSeg fails because it does not capture object parts such as the handle of the hammer. 

We obtain the hardcoded baseline by interpolating between the fully open and fully closed eigengrasp over 1s. This leads to the hand quickly snapping shut before the arm rises up. This performs poorly and gets zero success on many objects, especially thin ones. This is because to successfully grasp the object the thumb must retract closer to the palm. However, the timing of this is crucial, if the thumb retracts too early then the object flies back away from the hand. This is the most common failure case of this method. The hardcoded grasp succeeds for tall objects like an upright stapler or if the object happens to be in a favorable pose at the time of grasping. 

The teleop oracle baseline was carried out with a Manus VR glove with the joints mapped one-toone to the robot hand (ignoring the pinky). This was teleoperated by a trained user ( 20 hours of experience). This was intended to serve as an upper bound of hardware capability. We find our method matches or slightly lags behind the oracle for drill (light) and saucepan. Surprisingly, for stapler, screwdriver and both hammers it even exceeds the oracle baseline. This is because these objects are heavy and sit close to the ground and require very swift and forceful motion which is also very precise in order to be successfully picked out. This is hard to execute reliably for a human being, whereas our policy is able to do it well. Our method completes the task faster for the same reason. 

### **4.3 Emergent Behavior** 

Even though our reward function is extremely simple, because of large-scale training in simulation, our policy exhibits complex emergent behavior. It learns to be robust to failures of the affordance model. For instance, in Fig. 5, the initial graps causes the thumb to be stuck between the object and the palm. However, the policy detects this from proprioception and moves the thumb around the object. 

While manipulating heavy objects the grasp needs to be adjusted based on the pose of the object. Since our policy is aware of the endeffector pose, it learns this behavior. In Fig. 6 when the heavy drill is moved upright, the thumb changes position for better stability. 



Figure 5: The initial pre-grasp is wrong and the thumb gets stuck between palm and bottle, but the policy recovers and moves the thumb around to the correct grasp. 



Figure 6: As the hand changes the orientation of the heavy drill, the thumb moves position to stabilize it better. 

### **4.4 Affordance Analysis** 

We experimentally validate the pre-grasp affordance matching part of our pipeline separately. We compare against CLIPort [23] and CLIPSeg [24] in terms of both pick success rate and IoU between the predicted and ground truth affordance (human-annotated). We run evaluation on the simulated CLIPort dataset for both unseen and seen objects (Table. 3). 

For our method, we annotate one exemplar per category. To get affordance from CLIPSeg we prompt with the relevant part such as “hammer handle”. Spatula and Frying Pan are present in the CLIPort trainset while hammer is not. 

7 



<!-- Start of picture text -->
Ground Truth CLIP-Seg CLIPort Ours<br>Hammer<br>Saucepan<br>Spatula<br><!-- End of picture text -->

Our method outperforms CLIPort on both seen and unseen categories. CLIPSeg fails to localize objects or is not able to capture the functional part of the object and only has understanding of the entire object as a whole (Fig. 7). CLIPort localizes objects better but often predicts functionally incorrect regions (such as the pan of the saucepan instead of the handle in Fig. 7). 

Figure 7: Qualitative comparisons of the affordance **5 Related Work** prediction from our method and CLIP-Seg, CLIPort. Overall, our method produces predictions that are more **In-hand dexterous manipulation:** Dexterity functionally aligned. 

**In-hand dexterous manipulation:** Dexterity in humans is the ability to manipulate objects 

within their hand’s workspace [25, 26, 27]. Accordingly, in-hand reorientation has remained a standard, yet challenging task in robotics to imitate a human’s dexterity. In recent years, there has been a surge of interest in this field and sim2real approaches have shown some success at reorienting objects [7, 28, 9, 29, 8] and also manipulating them [6, 30]. Other works bypass sim and directly learn in-hand manipulation through trial and error in the real world [11, 10]. Some other works use human demos to guide RL [21] and others directly use demos to learn policies [31]. 

**Dexterous grasping:** While in-hand reorientation is an important task most of the uses of a dexterous hand involve grasping objects in different poses. Because of the large degrees of freedom, grasp synthesis is significantly more challenging. The classical approach is to use optimization [22, 32, 33]. This approach is still used today with the form or force closure objective [34, 35, 36]. Some methods use the contact between the object and the hand as a way to learn proper grasping [37, 38, 39, 40]. A VAE can be trained on these generated poses to learn a function that maps from object to grasp pose [35, 41]. Recent works leverage differentiable simulation to synthesize stable grasp poses [42]. Other works don’t decouple this problem into a grasp synthesis phase and learn it end-to-end in simulation [43], from demonstrations [44, 45, 31] or teleoperation [46, 47]. 

**Functional Grasping:** While simulation can be a powerful tool to optimize grasp metrics, functional affordances are usually human data since there may be more than one physically valid grasp pose but only one functionally valid one that allows one to use the object properly. Some approaches rely on clean annotations or motion capture datasets [48, 49, 50, 51] for hand object contact [52, 53, 54, 55, 56]. Some papers learn affordances from human images or video [57, 58] directly or through retargeting. These can however be noisy since they rely on hand pose detectors such as [59, 60] which are often noisy and difficult to learn from directly [44]. Some recent work in this area has begun to target functional grasping using large-scale datasets as a prior [61, 62, 63]. 

## **6 Limitations and Conclusion** 

We show that combining semantic information from models trained on internet data with the robustness of low-level control trained in simulation can yield functional grasps for a large range of objects. We show that using eigengrasps to restrict the action space of RL leads to policies that transfer better and are physically realistic. This leads to policies that are better to deploy in the real hardware. 

While our method is robust to slight errors in pre-grasp pose if errors are large a blind grasping policy cannot recover. One way to address this limitation is to equip the robot with a local field of view around the wrist such that it can finetune its grasp even if the affordance model is incorrect. 

Our method currently does not leverage joint pose information from the affordance model. While we found this to not be necessary in the set of objects we have, it might be useful in the case of more fine-grained manipulation such as picking up very thin objects like coins or credit cards. 

8 

## **7 Acknowledgements** 

We would like to thank Russell Mendonca, Shikhar Bahl, and Murtaza Dalal for fruitful discussions. KS is supported by the NSF Graduate Research Fellowship under Grant No. DGE2140739. This work is supported in part by ONR N00014-22-1-2096, ONR DURIP, and Air Force Office of Scientific Research (AFOSR) FA9550-23-1-0747. 

## **References** 

- [1] K. Libertus, A. S. Joh, and A. W. Needham. Motor training at 3 months affects object exploration 12 months later. _Developmental Science_ , 19(6):1058–1066, 2016. 

- [2] E. J. Gibson. Exploratory behavior in the development of perceiving, acting, and the acquiring of knowledge. _Annual review of psychology_ , 39(1):1–42, 1988. 

- [3] K. E. Adolph and S. E. Berger. _Motor Development_ , chapter 4. John Wiley & Sons, Ltd, 2007. ISBN 9780470147658. doi:https://doi.org/10.1002/9780470147658.chpsy0204. URL `https://onlinelibrary.wiley.com/doi/abs/10.1002/9780470147658.chpsy0204` . 

- [4] T. Bruce. _Learning through play, for babies, toddlers and young children_ . Hachette UK, 2012. 

- [5] R. A. Cortes, A. E. Green, R. F. Barr, and R. M. Ryan. Fine motor skills during early childhood predict visuospatial deductive reasoning in adolescence. _Developmental Psychology_ , 2022. 

- [6] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 39(1):3–20, 2020. 

- [7] T. Chen, M. Tippur, S. Wu, V. Kumar, E. Adelson, and P. Agrawal. Visual dexterity: In-hand dexterous manipulation from depth. _arXiv preprint arXiv:2211.11744_ , 2022. 

- [8] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko, R. Singh, J. Liu, D. Makoviichuk, K. Van Wyk, A. Zhurkevich, B. Sundaralingam, et al. Dextreme: Transfer of agile in-hand manipulation from simulation to reality. _arXiv preprint arXiv:2210.13702_ , 2022. 

- [9] Z.-H. Yin, B. Huang, Y. Qin, Q. Chen, and X. Wang. Rotating without seeing: Towards in-hand dexterity through touch. _Robotics: Science and Systems_ , 2023. 

- [10] A. Nair, A. Gupta, M. Dalal, and S. Levine. Awac: Accelerating online reinforcement learning with offline datasets. _arXiv preprint arXiv:2006.09359_ , 2020. 

- [11] A. Nagabandi, K. Konolige, S. Levine, and V. Kumar. Deep dynamics models for learning dexterous manipulation. In _Conference on Robot Learning_ , pages 1101–1112. PMLR, 2020. 

- [12] K. Shaw, A. Agarwal, and D. Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. In _RSS: Robotics Science and Systems_ , 2023. 

- [13] M. Oquab, T. Darcet, T. Moutakanni, H. V. Vo, M. Szafraniec, V. Khalidov, P. Fernandez, D. Haziza, F. Massa, A. El-Nouby, R. Howes, P.-Y. Huang, H. Xu, V. Sharma, S.-W. Li, W. Galuba, M. Rabbat, M. Assran, N. Ballas, G. Synnaeve, I. Misra, H. Jegou, J. Mairal, P. Labatut, A. Joulin, and P. Bojanowski. Dinov2: Learning robust visual features without supervision, 2023. 

- [14] A. Agarwal, A. Kumar, J. Malik, and D. Pathak. Legged locomotion in challenging terrains using egocentric vision. _CoRL_ , 2022. 

- [15] T. Miki, J. Lee, J. Hwangbo, L. Wellhausen, V. Koltun, and M. Hutter. Learning robust perceptive locomotion for quadrupedal robots in the wild. _Science Robotics_ , 7(62):eabk2822, 2022. 

9 

- [16] G. B. Margolis and P. Agrawal. Walk these ways: Tuning robot control for generalization with multiplicity of behavior. In K. Liu, D. Kulic, and J. Ichnowski, editors, _Proceedings of The 6th Conference on Robot Learning_ , volume 205 of _Proceedings of Machine Learning Research_ , pages 22–31. PMLR, 14–18 Dec 2023. URL `https://proceedings.mlr.press/v205/ margolis23a.html` . 

- [17] A. Kumar, Z. Fu, D. Pathak, and J. Malik. Rma: Rapid motor adaptation for legged robots. _RSS_ , 2021. 

- [18] D. Hadjivelichkov, S. Zwane, M. P. Deisenroth, L. de Agapito, and D. Kanoulas. One-shot transfer of affordance regions? affcorrs! In _Conference on Robot Learning_ , 2022. 

- [19] X. Zhou, R. Girdhar, A. Joulin, P. Krahenb¨ uhl, and I. Misra.¨ Detecting twenty-thousand classes using image-level supervision. In _ECCV_ , 2022. 

- [20] A. Kumar, A. Zhou, G. Tucker, and S. Levine. Conservative q-learning for offline reinforcement learning, 2020. 

- [21] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 

- [22] M. Ciocarlie, C. Goldfeder, and P. Allen. Dexterous grasping via eigengrasps: A lowdimensional approach to a high-complexity problem. In _Robotics: Science and systems manipulation workshop-sensing and adapting to the real world_ , 2007. 

- [23] M. Shridhar, L. Manuelli, and D. Fox. Cliport: What and where pathways for robotic manipulation. In _Conference on Robot Learning_ , pages 894–906. PMLR, 2022. 

- [24] T. Luddecke and A. Ecker.¨ Image segmentation using text and image prompts. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 7086–7096, 2022. 

- [25] R. R. Ma and A. M. Dollar. On dexterity and dexterous manipulation. In _2011 15th International Conference on Advanced Robotics (ICAR)_ , pages 1–7. IEEE, 2011. 

- [26] N. Kamakura, M. Matsuo, H. Ishii, F. Mitsuboshi, and Y. Miura. Patterns of static prehension in normal hands. _The American journal of occupational therapy_ , 34(7):437–445, 1980. 

- [27] C. L. MacKenzie and T. Iberall. _The grasping hand_ . Elsevier, 1994. 

- [28] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik. In-Hand Object Rotation via Rapid Motor Adaptation. In _Conference on Robot Learning (CoRL)_ , 2022. 

- [29] I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 

- [30] Y. Qin, B. Huang, Z.-H. Yin, H. Su, and X. Wang. Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. In _Conference on Robot Learning_ , 2022. 

- [31] S. P. Arunachalam, S. Silwal, B. Evans, and L. Pinto. Dexterous imitation made easy: A learningbased framework for efficient dexterous manipulation. _arXiv preprint arXiv:2203.13251_ , 2022. 

- [32] A. Miller and P. Allen. Graspit! a versatile simulator for robotic grasping. _IEEE Robotics & Automation Magazine_ , 11(4):110–122, 2004. doi:10.1109/MRA.2004.1371616. 

- [33] D. Berenson and S. S. Srinivasa. Grasp synthesis in cluttered environments for dexterous hands. In _Humanoids 2008-8th IEEE-RAS International Conference on Humanoid Robots_ , pages 189–196. IEEE, 2008. 

10 

- [34] R. Wang, J. Zhang, J. Chen, Y. Xu, P. Li, T. Liu, and H. Wang. Dexgraspnet: A largescale robotic dexterous grasp dataset for general objects based on simulation. _arXiv preprint arXiv:2210.02697_ , 2022. 

- [35] P. Li, T. Liu, Y. Li, Y. Geng, Y. Zhu, Y. Yang, and S. Huang. Gendexgrasp: Generalizable dexterous grasping. _arXiv preprint arXiv:2210.00722_ , 2022. 

- [36] K. M. Lynch and F. C. Park. _Modern robotics_ . Cambridge University Press, 2017. 

- [37] P. Grady, C. Tang, C. D. Twigg, M. Vo, S. Brahmbhatt, and C. C. Kemp. ContactOpt: Optimizing contact to improve grasps. In _Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2021. 

- [38] P. Mandikal and K. Grauman. Learning dexterous grasping with object-centric visual affordances. In _2021 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 6169–6176, 2021. doi:10.1109/ICRA48506.2021.9561802. 

- [39] S. Brahmbhatt, C. Ham, C. C. Kemp, and J. Hays. Contactdb: Analyzing and predicting grasp contact via thermal imaging. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , June 2019. 

- [40] S. Brahmbhatt, A. Handa, J. Hays, and D. Fox. Contactgrasp: Functional multi-finger grasp synthesis from contact. In _2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 2386–2393, 2019. doi:10.1109/IROS40897.2019.8967960. 

- [41] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, T. Liu, L. Yi, and H. Wang. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 4737–4746, June 2023. 

- [42] D. Turpin, L. Wang, E. Heiden, Y.-C. Chen, M. Macklin, S. Tsogkas, S. Dickinson, and A. Garg. Grasp’d: Differentiable contact-rich grasp synthesis for multi-fingered hands. In _Computer Vision–ECCV 2022: 17th European Conference, Tel Aviv, Israel, October 23–27, 2022, Proceedings, Part VI_ , pages 201–221. Springer, 2022. 

- [43] Y. Qin, B. Huang, Z.-H. Yin, H. Su, and X. Wang. Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. In _Deep Reinforcement Learning Workshop NeurIPS 2022_ , 2022. 

- [44] K. Shaw, S. Bahl, and D. Pathak. VideoDex: Learning Dexterity from Internet Videos. In _Conference on Robot Learning (CoRL)_ , 2022. 

- [45] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _Computer Vision–ECCV 2022: 17th European Conference, Tel Aviv, Israel, October 23–27, 2022, Proceedings, Part XXXIX_ , pages 570–587. Springer, 2022. 

- [46] A. Sivakumar, K. Shaw, and D. Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube, 2022. 

- [47] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox. Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 9164–9170. IEEE, 2020. 

- [48] Z. Fan, O. Taheri, D. Tzionas, M. Kocabas, M. Kaufmann, M. J. Black, and O. Hilliges. ARCTIC: A dataset for dexterous bimanual hand-object manipulation. In _Proceedings IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2023. 

11 

- [49] R. Goyal, S. Ebrahimi Kahou, V. Michalski, J. Materzynska, S. Westphal, H. Kim, V. Haenel, I. Fruend, P. Yianilos, M. Mueller-Freitag, et al. The” something something” video database for learning and evaluating visual common sense. In _Proceedings of the IEEE international conference on computer vision_ , pages 5842–5850, 2017. 

- [50] C. Zimmermann, D. Ceylan, J. Yang, B. Russell, M. Argus, and T. Brox. Freihand: A dataset for markerless capture of hand pose and shape from single rgb images. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 813–822, 2019. 

- [51] O. Taheri, N. Ghorbani, M. J. Black, and D. Tzionas. GRAB: A dataset of whole-body human grasping of objects. In _European Conference on Computer Vision (ECCV)_ , 2020. URL `https://grab.is.tue.mpg.de` . 

- [52] S. Brahmbhatt, C. Ham, C. C. Kemp, and J. Hays. Contactdb: Analyzing and predicting grasp contact via thermal imaging. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 8709–8719, 2019. 

- [53] Y. Liu, Y. Liu, C. Jiang, K. Lyu, W. Wan, H. Shen, B. Liang, Z. Fu, H. Wang, and L. Yi. Hoi4d: A 4d egocentric dataset for category-level human-object interaction, 2022. 

- [54] O. Taheri, N. Ghorbani, M. J. Black, and D. Tzionas. Grab: A dataset of whole-body human grasping of objects. In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IV 16_ , pages 581–600. Springer, 2020. 

- [55] S. Dasari, A. Gupta, and V. Kumar. Learning dexterous manipulation from exemplar object trajectories and pre-grasps. In _IEEE International Conference on Robotics and Automation 2023_ , 2023. 

- [56] A. Patel, A. Wang, I. Radosavovic, and J. Malik. Learning to imitate object interactions from internet videos, 2022. 

- [57] S. Bahl, R. Mendonca, L. Chen, U. Jain, and D. Pathak. Affordances from human videos as a versatile representation for robotics. In _CVPR_ , 2023. 

- [58] Y. Ye, X. Li, A. Gupta, S. D. Mello, S. Birchfield, J. Song, S. Tulsiani, and S. Liu. Affordance diffusion: Synthesizing hand-object interactions. In _CVPR_ , 2023. 

- [59] Y. Rong, T. Shiratori, and H. Joo. Frankmocap: A monocular 3d whole-body pose estimation system via regression and integration. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 1749–1759, 2021. 

- [60] A. Mittal, A. Zisserman, and P. H. Torr. Hand detection using multiple proposals. In _Bmvc_ , volume 2, page 5, 2011. 

- [61] Z. Q. Chen, K. Van Wyk, Y.-W. Chao, W. Yang, A. Mousavian, A. Gupta, and D. Fox. Learning robust real-world dexterous grasping policies via implicit shape augmentation. _arXiv preprint arXiv:2210.13638_ , 2022. 

- [62] J. Ye, J. Wang, B. Huang, Y. Qin, and X. Wang. Learning continuous grasping function with a dexterous hand from human demonstrations. _IEEE Robotics and Automation Letters_ , 8(5): 2882–2889, 2023. 

- [63] S. Brahmbhatt, A. Handa, J. Hays, and D. Fox. Contactgrasp: Functional multi-finger grasp synthesis from contact. In _2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 2386–2393. IEEE, 2019. 

- [64] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

12 

## **A Grasping along multiple axes** 

In some cases, an object may be kept upright and a top-down angle of approach does not work. To deal with these cases, we setup three cameras along each axis (Fig. 3) and run affordance matching for each one. We finally pick the axis that has the highest score and move the hand along that axis to the pre-grasp pose. See Fig. 8, 9 for a vizualization. Empirically, we find that the confidence score is indeed always highest for the correct direction of approach. 



Figure 8: Affordance prediction for an upright drill from multiple angles. The best angle of approach is from the side and that is also the angle with highest affordance score. Our system picks this angle and executes a grasp. 



Figure 9: Affordance prediction for an upright mug from multiple angles. Our system picks the side angle with highest affordance score and executes a grasp. 

13 

## **B Training curves in simulation** 



Figure 10: Training curves for baselines in simulation. Each baseline is run over 5 seeds. We see that ours outperforms the other baselines and also is more stable with respect to the seed. This is because of the lower dimensional action space. 

## **C Hardware Setup** 

We use the xArm6 with LEAP hand [12] pictured in Fig. 3. The arm has 6 actuated joints, while the hand has 16 joints, four on each digit (three fingers and one thumb). Three calibrated D435 cameras facing along each axis are used to obtain masks and affordance regions. Both the arm and the hand run at 30Hz. To teleoperate the hand and collect human demos for eigengrasps we use a Manus VR glove with SteamVR lighthouses which gives fingertip and hand positions which are then retargeted to our hand as in Figure 12. 



<!-- Start of picture text -->
Top View<br>Side View<br>Front View<br><!-- End of picture text -->

Figure 11: Hardware setup with LEAP hand mounted on xarm6 with one D435 along each axis. 

14 



Figure 12: (left) the Manus VR glove we use to teleoperate our hand (right) the hand in the retargeted pose. 

## **D Implementation Details** 

We use a recurrent policy as that maps observations **o** _t ∈_ R<sup>16</sup> to actions **a** _t ∈_ R<sup>9</sup> . A stateful policy is able to adapt to changes in environment dynamics better than a feedforward one. This allows our robot to adapt to slight errors in the pre-grasp pose from the affordance model. The policy observes the 7 dimensional target pose (position, quaternion) of the end-effector and the 16 joint angle positions of the hand. 

We use IsaacGym [64] as a simulator with IsaacGymEnvs for the environments and rl ~~g~~ ames as the reinforcement learning library. The policy contains a layer-normed GRU with 256 as the hidden state followed by an MLP with hidden states 512, 256, 128. The policy is trained using PPO with backpropagation through time truncated at 32 timesteps. We run 8192 environments in parallel and train for 400 epochs. 

## **E Domain Randomization** 

For robustness, we domain randomize physics parameters as shown in Tab. 4. 

|Name|Range|
|---|---|
|object scale|[0_._8_,_1_._2]|
|object mass scaling|[0_._5_,_1_._5]<br>|
|Friction coefficient|[0_._7_,_1_._3]|
|stiffness scaling|[0_._75_,_1_._5]|
|damping scaling|[0_._3_,_3_._0]|



Table 4: domain randomization in simulation 

15 

