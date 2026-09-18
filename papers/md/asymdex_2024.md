# **AsymDex: Asymmetry and Relative Coordinates for RL-based Bimanual Dexterity** 

**Zhaodong Yang**<sup>1</sup> **, Yunhai Han**<sup>1</sup> **, Ai-Ping Hu**<sup>1</sup> **, Harish Ravichandar**<sup>1</sup> 

1Georgia Institute of Technology 

_{_ `halyang, yhan389, ahu6, harish.ravichandar` _}_ `@gatech.edu` 

**Abstract:** We present _Asymmetric Dexterity (AsymDex)_ , a novel and simple reinforcement learning (RL) framework that can efficiently learn a large class of bimanual skills in multi-fingered hands without relying on demonstrations. Two crucial insights enable AsymDex to reduce the observation and action space dimensions and improve sample efficiency. First, true ambidexterity is rare in humans and most of us exhibit strong “handedness”. Inspired by this observation, we assign complementary roles to each hand: the _facilitating hand_ repositions and reorients one object, while the _dominant hand_ performs complex manipulations to achieve the desired result (e.g., opening a bottle cap, or pouring liquids). Second, controlling the _relative_ motion between the hands is crucial for coordination and synchronization of the two hands. As such, we design relative observation and action spaces and leverage a relative-pose tracking controller. Further, we propose a two-phase decomposition in which AsymDex can be readily integrated with recent advances in grasp learning to facilitate both the acquisition and manipulation of objects using two hands. Unlike existing RL-based methods for bimanual dexterity with multi-fingered hands, which are either sample inefficient or tailored to a specific task, AsymDex can efficiently learn a wide variety of bimanual skills that exhibit asymmetry. Detailed experiments on seven asymmetric bimanual dexterous manipulation tasks (four simulated and three real-world) reveal that AsymDex consistently outperforms strong baselines that challenge our design choices. The project website is at `https://sites.google.com/view/asymdex-2025/` . 

**Keywords:** Dexterous Bimanual Manipulation, Multi-Fingered Hands 

## **1 Introduction** 

Bimanual dexterity is crucial for robots operating in human environments as they allow for complex yet flexible manipulation compared to a single hand [1, 2, 3, 4, 5, 6]. We are interested in learning a wide range of bimanual dexterous skills on multi-fingered hands purely from reinforcement. 

While learning on a single multi-fingered hand is known to be challenging [7, 8, 9, 10, 11, 12, 13], learning bimanual dexterity is made more challenging due to the higher-dimensionality and the need for coordination and synchronization of two hands [1, 14]. These challenges are only exacerbated when these skills have to be learned from reinforcement, explaining why existing efforts often either resort to expert demonstrations [15, 16, 17, 18] or limit themselves to specific tasks [19, 20]. 

We rely on two insights to tackle the challenges of bimanual dexterity. First, we are inspired by how humans and other great apes approach these challenges: there is a natural _asymmetry_ in how we use each of our hands when we perform most bimanual tasks [21]. Specifically, we tend to use one hand to reposition and reorient an object so as to make it easier for the other hand to perform complex manipulation. While leveraging such asymmetry might appear to restrict the class of bimanual skills we can learn, rich bodies of work in human biomechanics and evolution reveal its prevalence and necessity [21, 22, 23, 24]. Evolutionary biologists posit handedness evolved to meet the escalating cognitive demands of tool use, language, and complex manipulation [25]. Indeed, a large number of real-world tasks admit such asymmetry (e.g., attachment, detachment, assembly, and pouring). 



<!-- Start of picture text -->
Learning Framework Real-world Evaluation<br>Simulation-based Evaluation<br>Time<br>Block-in-cup<br>Pouring<br>BiDexHands Twist-Lid<br><!-- End of picture text -->

Figure 1: Our approach (AsymDex) efficiently learns asymmetric bimanual dexterous manipulation skills based on reinforcement learning by effectively leveraging i) the natural asymmetry in the hands’ roles and ii) relative state and action spaces that prioritize synchronization. 

Looking closely at the asymmetry in bimanual dexterity reveals our second insight. Our nondominant hand tends to hold an object firmly as we reorient and reposition it _relative_ to the dominant hand or the object being held by the dominant hand (e.g., tilting a pen before uncapping). This suggests that there is often little to no in-hand movement of the object grasped by the non-dominant hand, and robust synchronization can be achieved by ensuring relative movement of the two hands. 

We contribute a novel RL-based learning framework for bimanual dexterity, dubbed _Asymmetric Dexterity (AsymDex)_ by operationalizing the above two insights (see Fig. 3). To incorporate asymmetry, we define a _dominant hand_ and a _facilitating hand_ . While the dominant hand learns complex skills across all its degrees of freedom, the facilitating hand learns to reposition and reorient the object by controlling the 6D pose of its base (i.e., no finger movement). This allows us to both reduce the dimensionality of the observation and action spaces and tightly integrate the roles of the two hands. To ensure coordination and synchronization, AsymDex operates over relative observation and action spaces that incentivize flexible coordination of the two hands without resorting to explicit time-dependence or task-specific coordinate frame designs. 

We also leverage the observation that bimanual manipulation in practice is composed of two distinct phases: i) the _acquisition phase_ in which objects are grasped, and ii) the _interaction phase_ in which the two hands coordinate to perform the bimanual task. Unlike many existing methods that entirely ignore the acquisition phase[2, 14, 19, 26], we show that this decomposition enables AysmDex to be seamlessly integrated with learned grasping policies to enable fluent execution. 

In summary, we contribute AsymDex – a novel Rl-based framework for learning a wide variety of bimanual dexterous skills by taking inspiration from two key aspects of human bimanual dexterity: i) asymmetric hand roles, and ii) relative hand movement. We conduct comprehensive experiments on seven complex tasks (four simulated and three real) and compare against strong baselines that challenge the need for AsymDex’s structural inductive biases. Our results show that AsymDex consistently outperforms these baselines in terms of both task performance and sample efficiency. 

## **2 Related Work** 

**Learning Bimanual Manipulation** : Several existing methods focus on learning bimanual skills, but are often limited to simple end-effectors. Imitation learning (IL) based approaches have been particularly successful in bimanual manipulation [3, 27, 28, 26], and have led to novel and low-cost infrastructure to collect bimanual manipulation data [4, 29]. These approaches rely on demonstrations to provide the necessary supervision to learn effective coordination strategies. Reinforcement learning (RL) has also been shown to be successful in learning bimanual manipulation skills [30, 31, 32, 33]. These methods implicitly incentivize coordination by learning to optimize reward functions that 

2 

favor task success and efficiency. In contrast to all of these works that only consider parallel jaw grippers, AsymDex learns bimanual dexterous manipulation skills involving multi-fingered hands. 

**Asymmetry in Bimanual Manipulation** : Motivated by the asymmetry in how humans use their two hands (referred to as _role-differentiated bimanual manipulation_ [22, 23, 24, 34]), recent works assign different roles to each robot hand in the bimanual system [2, 35, 36, 37, 38]. However, some of these approaches restrict the role of the facilitating hand to stabilizing the object while the dominant hand manipulates it [2, 35, 36]. In contrast, AsymDex allows the facilitating hand to reposition and reorient the object _simultaneously_ as the dominant hand executes its role. Importantly, unlike AsymDex, all these prior methods are limited to parallel jaw grippers. 

**Learning Dexterous Manipulation** : Learning dexterous manipulation skills involves addressing numerous challenges due to high dimensional state and action spaces and highly nonlinear dynamics. Recent works have tackled these challenges using imitation learning (IL) or reinforcement learning (RL) and demonstrate impressive performance [7, 8, 9, 10, 11, 13, 39, 40, 41, 42]. However, IL-based methods rely either on complex infrastructure and retargeting methods to collect demonstrations [7, 13, 40, 43, 44] or pre-trained expert policies [10, 11, 42]. On the other hand, RL-based methods do not share these constraints as they learn skills via reinforcement, but tend to require significant exploration even for dexterous manipulation with a single hand [8, 9, 39, 41]. As we show in our experiments, naive application of RL-based methods is not effective for bimanual dexterous manipulation due to the increased dimensionality and the need for coordination. 

**Learning Bimanual Dexterous Manipulation** : A few recent studies have focused on learning bimanual dexterity. Some of these methods require the collection of expert demonstrations [5] and suffer from the same limitations we discussed earlier for IL-based methods that use parallel jaw grippers. To circumvent the need for collecting demonstrations, recent efforts have led to methods that only leverage RL and yet are capable of learning impressive bimanual manipulation skills, such as playing the piano [6], twisting lids off containers [19], and dynamic handover [20]. While these methods are specifically designed to solve a particular task, AsymDex is capable of efficiently learning different bimanual dexterous manipulation tasks. Some recent studies investigate generalized learning method by utilizing expert demonstration for efficient RL training [15, 16, 17, 18], while AsymDex can efficiently learn bimanual manipulation skills without relying on demonstration. 

## **3 Problem Formulation** 

We first formulate the general problem of bimanual dexterous manipulation, and then introduce asymmetric bimanual dexterity. 

Consider the general problem of bimanual dexterous manipulation, in which two multi-fingered hands coordinate to manipulate up to two objects. Formally, this problem can be defined as a Partially-Observable Markov Decision Process (POMDP) _M_ = ( _S, Z, A, R, P_ ), where _S ∈_ R<sup>_n_</sup> is the state space, _Z ∈_ R<sup>_m_</sup> is the observation space, _A ∈_ R<sup>_u_</sup> is the action space, _R_ : R<sup>_m_</sup> _×_ R<sup>_u_</sup> _→_ R is the reward function, and _P_ : R<sup>_n_</sup> _×_ R<sup>_u_</sup> _→_ R<sup>_n_</sup> is the environment dynamics. Note that we do not assume access to any demonstrations. Instead, we tackle of challenge of learning purely based on reinforcement. Given this formulation, the problem boils down to learning a policy _π_ : _Z →A_ that maximizes the expected discounted cumulative reward _Eπ_ [Σ<sup>_T_</sup> _t_ =0<sup>_−_1</sup><sup>_γtR_(</sup><sup>_z_(</sup><sup>_t_)</sup><sup>_, a_(</sup><sup>_t_))].</sup> 

**Observation and Action Spaces** : The observation space _Z_ is composed of hand and object states. At time step _t_ , _z_ ( _t_ ) = [ _ξ_ 1( _t_ ) _, ξ_ 2( _t_ ) _, ξ_<sup>_obj_</sup> ( _t_ )], where _ξ_ 1( _t_ ) contains the first hand’s current full (fingers + wrist) configuration _ξ_ 1<sup>_h_(</sup><sup>_t_)</sup><sup>_∈_R</sup><sup>_n_1and the6 DOF poseof its base</sup><sup>_ξ_</sup> 1<sup>_b_(</sup><sup>_t_)</sup><sup>_∈_SE(3),</sup><sup>_ξ_2(</sup><sup>_t_)contains</sup> the corresponding elements for the second hand, and _ξ_<sup>_obj_</sup> ( _t_ ) contains the 6 DOF poses of either two objects (e.g., stacking two cups) or parts of one object (e.g., bottle and lid). The joint action at time step _t_ is given by _a_ ( _t_ ) = [ _ξ_<sup>ˆ</sup> 1( _t_ ) _, ξ_<sup>ˆ</sup> 2( _t_ )], where _ξ_<sup>ˆ</sup> 1( _t_ ) denotes the target joint configuration of the first hand _ξ_<sup>ˆ</sup> 1<sup>_h_(</sup><sup>_t_) and the target 6 DOF pose of its base</sup><sup>_ξ_ˆ</sup> 1<sup>_b_(</sup><sup>_t_), and</sup><sup>_ξ_ˆ2(</sup><sup>_t_) denotes the corresponding</sup> targets for the second hand. With the above definitions, we can now define the problem of learning bimanual dexterity as one of learning a monolithic symmetric policy: _π_ sym( _a_ ( _t_ ) _|z_ ( _t_ )). 

3 

**Asymmetric Dexterity Problem** : Asymmetric dexterity can be viewed as a broad subclass to the above general class of problems. Inspired by strategies employed by humans and other great apes, we are interested in tasks in which one multi-fingered hand performs complex and precise manipulations while the other plays a facilitating role by supporting and actively reorienting objects of interest (e.g., stacking, attachment, detachment, etc.). Note that our formulation does not restrict the movement of the second hand; it merely restricts the relative movement between the second hand and the object being held. As explained in Sec. 1, a large number of bimanual tasks exhibit asymmetry, hinting at handedness in most humans. We are thus interested in learning an asymmetric policy _π_ AsymDex( _·_ ) with carefully-defined observation _Z_ AsymDex and action _A_ AsymDex spaces in an effort to improve both effectiveness and sample efficiency. 

Note that our primary contributions and the asymmetric assumption pertain to the _interaction phase_ of bimanual dexterity, in which the two hands actively coordinate to complete the task after having grasped the necessary object(s). Most existing works focus solely on the interaction phase [19, 20, 45]. In Sec. 4.4, we discuss how our approach can be readily extended to also tackle the _acquisition phase_ (learning to grasp the necessary objects before coordinating). 

## **4 AsymDex: Learning Asymmetric Dexterity** 

While one could learn the symmetric policy _πsym_ ( _·_ ) as defined in Sec. 3, training such a policy can be inefficient or ineffective due to the high dimensionality of the observation and action spaces (see Sec. 5 for empirical evidence). Importantly, a symmetric approach ignores the natural asymmetry found in most bimanual tasks. Below, we explain how AsymDex overcomes these challenges. 

### **4.1 Incorporating Asymmetry** 

Motivated by the natural asymmetry in human bimanual manipulation [22, 23, 24], we assign different roles to each robot hand during their interaction: a _facilitating hand_ that is responsible for holding and repositioning and reorienting the object, and a _dominant hand_ which is responsible for fine-grained dexterous manipulation of the object(s). We note that there tends to be no relative motion between the facilitating hand and the grasped object in asymmetric dexterity since the facilitating hand need only hold, move, and reorient the object (i.e., no in-hand reorientation). In contrast, the dominant hand can interact freely with the object(s). This suggests that the asymmetric dexterity is neither dependent on nor influences the finger joints of the facilitating hand during the interaction phase. As such, we can considerably reduce the observation and action spaces by defining an asymmetry-only bimanual policy: _π_ asym( _a_ asym( _t_ ) _|z_ asym( _t_ )) with actions _a_ asym( _t_ ) = [ _ξ_<sup>ˆ</sup> _d_ ( _t_ ) _, ξ_<sup>ˆ</sup> _f_<sup>_b_(</sup><sup>_t_)]</sup> and observations _z_ asym( _t_ ) = [ _ξd_ ( _t_ ) _, ξf_<sup>_b_(</sup><sup>_t_)</sup><sup>_, ξobj_(</sup><sup>_t_)].Thischangebothreducesthedimensionality</sup> and ensures that the facilitating hand doesn’t learn unproductive or unnecessary behaviors. 

### **4.2 Incorporating Relative Observation and Action Spaces** 

In addition to asymmetry, a key characteristic of bimanual dexterity is the synchronized and responsive movement of the two hands. We can further reduce the size of the observation and action spaces and introduce tight coupling between the hands’ behaviors by defining _relative_ and _object-centric_ coordinates that capture the relationships between the movements of two hands and the object(s) being manipulated. Indeed, the use of relative state spaces has shown to considerably benefit bimanual manipulation with simple end effectors [26, 46, 47, 48]. While some of these prior works limit the relative space to a one-degree-offreedom (1-DoF) action space [26], AsymDex allows for complete 6-DoFs relative space. 



Figure 2: AsymDex’s observation and Action Spaces. 

4 



Figure 3: We decompose asymmetric bimanual dexterous manipulation into two phases: An _acquisition_ phase and an _interaction_ phase. We show that AsymDex can be readily integrated with learned grasping policies in order to seamlessly acquire and manipulate objects. 

Let _ξf_<sup>_obj_</sup> ( _t_ ) be the state of the object being held by the facilitating hand, and let _ξd_<sup>_obj_(</sup><sup>_t_) be the state</sup> of the object being manipulated by the dominant hand. We attach a coordinate frame to the object being held by the facilitating hand: _Pf_ . Now, we can transform the asymmetry-only observations _z_ asym( _t_ ) (originally defined in the absolute or world coordinate frame) into the new coordinate frame _Pf_ . Note that since there is no relative motion between the facilitating hand and the object that it is holding, neither _ξf_<sup>_obj_</sup> ( _t_ ) nor _ξf_<sup>_b_(</sup><sup>_t_) change in</sup><sup>_Pf_, and can thus be removed from our observation space</sup> without losing any information. Now, transforming the observations ( _ξd_<sup>_b_(</sup><sup>_t_)</sup><sup>_, ξ_</sup> _d_<sup>_obj_(</sup><sup>_t_)) onto</sup><sup>_Pf_yields</sup> _z_ AsymDex = [ _ξd_<sup>_h_(</sup><sup>_t_)</sup><sup>_, ξ_</sup> _r_<sup>_b_(</sup><sup>_t_)</sup><sup>_, ξ_</sup> _r_<sup>_obj_</sup> ( _t_ )], where _ξr_<sup>_b_(</sup><sup>_t_) and</sup><sup>_ξ_</sup> _r_<sup>_obj_</sup> ( _t_ ) respective denote the 6D relative poses of the dominant hand base and the object being manipulated by the dominant hand, both defined with respect to the object being held by the facilitating hand. Note that since _ξd_<sup>_h_(</sup><sup>_t_) denotes the dominant</sup> hands’ joint states, it is not impacted by the change of coordinates. Similarly, we apply the same modifications to the asymmetry-only action _aasym_ ( _t_ ), yielding _a_ AsymDex( _t_ ) = ( _ξ_<sup>ˆ</sup> _r_<sup>_b_(</sup><sup>_t_)</sup><sup>_,_ˆ</sup><sup>_ξ_</sup> _d_<sup>_h_(</sup><sup>_t_)), where</sup> _ξ_ ˆ _r_<sup>_b_(</sup><sup>_t_) is the target relative pose of the dominant hand now defined relative to the object being held</sup> by the facilitating hand. Incorporating the above change of coordinates in addition to leveraging asymmetry, allows us to define AsymDex’s policy as _π_ AsymDex( _a_ AsymDex( _t_ ) _|z_ AsymDex( _t_ )). Note that our formulation has significantly reduced the dimensions of both the state and action spaces, compared to the symmetric policy _π_ sym as defined in Section 3. 

We parameterize the AsymDex policy _π_ AsymDex( _·_ ) using an MLP and using Proximal Policy Optimization (PPO) [49] to train it. See Appendix. A for details of the algorithm and policy architecture. 

### **4.3 Relative Pose Tracking Controller** 

To control the hand bases based on the target relative pose _ξ_<sup>ˆ</sup> _r_<sup>_b_(</sup><sup>_t_) provided by</sup><sup>_π_AsymDex, we designed</sup> a bimanual controller that computes both the target dominant hand base pose _ξ_<sup>ˆ</sup> _d_<sup>_b_(</sup><sup>_t_)andthetarget</sup> facilitating hand base pose _ξ_<sup>ˆ</sup> _f_<sup>_b_(</sup><sup>_t_) as follows</sup> 



where _Rworld_<sup>_of_denotes the rotational transformation from Frame</sup><sup>_Pf_to the world frame</sup><sup>_PW_,</sup><sup>_dist_(</sup><sup>_·_)</sup> denotes the difference between two 6D poses, and _α_ is a hyperparameter that controls the relative involvement of each hand. The pseudo-code of the training process is included in Alg. 1. 

### **4.4 Acquisition Phase** 

While our approach as explained thus far deals with the challenge of coordinating two hands to accomplish asymmetric dexterous manipulation tasks, it assumes that the object(s) of interest have already been grasped at the beginning of the task. However, in practice, robots must be learn to grasp and pick up the necessary objects before the interaction between the two hands (and the objects) can begin. We refer to this initial phase as the _acquisition_ phase. Most recent works on bimanual dexterous manipulation often entirely ignore the acquisition phase and focus purely on the interaction 

5 

phase [6, 19, 20]. In contrast, we demonstrate that our approach can seamlessly accommodate the acquisition phase by i) leveraging the observation that the acquisition phase doesn’t require the coordination of two arms, and ii) employing recent advances in learning to grasp. Specifically, we demonstrate that we can seamlessly integrate AsymDex with PDGM [50], which can efficiently learn multi-fingered grasping policies by leveraging pre-grasp poses (see Fig. 3). Details about the grasping reward design are available in Appendix. B. We begin by executing the grasping policy in isolation and then ”turn on” the asymmetric policy learned by AsymDex after the object has been firmly grasped by the facilitating hand. If the task requires the dominant hand to also grasp a second object, we employ the same method to train a grasping policy for dominant hand to acquire the object, but switch the control of the dominant hand’s joints over the asymmetric policy after the object has been grasped. 

## **5 Experimental evaluation** 

We evaluated AsymDex on four simulated and three real-world bimanual dexterous tasks and compared its performance against strong baselines that challenge our key design choices. 

### **5.1 Simulation Experiments** 

Our experiments in simulation both systematically and rigorously evaluate AsymDex. 

**Tasks** : We evaluated AsymDex and the baselines on the following four bimanual manipulation tasks which contain both original ( _Block in cup_ , _Bottle cap_ ) and adapted tasks ( _Stack_ , _Switch_ ) from BiDexHand [14] (see Fig. 1). All these tasks use two Shadow Hands – each a 30-DoF simulated multi-finger hand system (24-DoF hand + 6-DoF floating wrist base) built with Isaac Gym [51]. 

- _Block in cup_ : The two hands must coordinate to ensure that one hand places a block inside a cup that is being held by the other without letting either the cup or the block fall to the ground. 

- _Stack_ : Two cups need to be stacked together. Each hand must hold a cup, and both must coordinate such that the two cups are aligned as one slides into the other. 

- _Bottle cap_ : One hand must hold and reorient a bottle such that the other hand can grasp and separate the bottle cap from the bottle. 

- _Switch_ : One hand holds and reorients a switch in a way that allows the other hand to turn it on. 

Note that our task designs are more challenging than their counterparts in BiDexHand [14]. We require that the two hands coordinate and synchronize to achieve success in each of the above four tasks, especially since (unlike the original designs) we do not provide a support surface (e.g., a table) that would significantly reduce the need for bimanual coordination. See Appendix. C for details on state space design, sampling procedure, success criteria, and reward design. 

**Metrics** : We quantify performance in terms of i) _success rate_ (see Appendix. C for criteria) and ii) _sample efficiency_ . We report both metrics across five random seeds in all experiments. 

### **5.1.1 Learning Bimanual Coordination** 

We first evaluated AsymDex’s effectiveness during the interaction phase. Following contemporary practice in methods that learn bimanual dexterous skills [19, 20], we initialized the environment such that the hands are at appropriate pre-grasp poses near the respective objects. This allows us to isolate and examine AsymDex’s ability to learn to coordinate two multi-fingered hands. See Section 5.1.2 for the second experiment in which we also consider the challenge of acquiring the objects from a tabletop surface before interaction begins. 

We compared AsymDex against the following baselines: 

- `Sym` : This policy assumes that both hands play an equal role in bimanual manipulation (see _πsym_ in Sec. 3). This baseline allows us to examine the necessity and effectiveness of leveraging the asymmetry in hand roles as well as the relative action and observation spaces. 

6 

|**Task**<br>**Method**|`Sym`|`Asym-w/o-rel`|`Rel-w/o-Asym`|`AsymDex`(ours)|
|---|---|---|---|---|
|_Block in cup_|0_._0429_±_0_._0266|0_._0164_±_0_._0190|0_._1086_±_0_._1378|**0.7701**_±_**0.0559**|
|_Stack_|0_._0771_±_0_._0611|0_._2185_±_0_._3232|0_._6560_±_0_._3213|**0.8392**_±_**0.0596**|
|_Bottle cap_|0_._3111_±_0_._1813|0_._4143_±_0_._1410|0_._4730_±_0_._2011|**0.6295**_±_**0.1422**|
|_Switch_|0_._0563_±_0_._0126|0_._1626_±_0_._0882|0_._1149_±_0_._0176|**0.6700**_±_**0.0359**|



Table 1: Success rates (mean _±_ std. dev.) for the interaction phase. 

- `Asym-w/o-rel` : This policy leverages asymmetry in hand roles, but learns over absolute observation and action places (see Sec. 4.1). As such, this baseline allows us to examine the necessity and effectiveness of relative action and observation spaces. 

- `Rel-w/o-asym` : This policy leverages the relative observation and action places, but ignores asymmetry. As such, it allows us to examine the necessity and effectiveness of asymmetry. 

**Both asymmetry and relative spaces are necessary for consistent performance** : We report the learning curves in Fig. 4 (a) and success rates in Table 1. Note that AsymDex consistently outperforms all the baselines across all four tasks in terms of success rate and sample efficiency, with significant margins in two tasks ( _Block in cup_ and _Switch_ ). `Rel-w/o-asym` performs better than the other two baselines across all tasks except _Switch_ , while `Asym-w/o-rel` performs better than `Monolithic` on all tasks except _Block in cup_ , on which both struggle. 

Taken together, the above observations reveal a few key insights. First, when used in isolation, neither asymmetry nor relative spaces are sufficient across all tasks. Second, the use of relative spaces offers a larger boost in performance compared to asymmetry, likely due to the fact that relative spaces avoid unnecessary exploration (e.g., when the two hands move in parallel) while allowing the facilitating hand to exhibit more complex behaviors. Third, ignoring both asymmetry and relative spaces ( `Sym` ) hardly leads to success. 

### **5.1.2 Learning to Grasp and Coordinate** 

We next evaluated AsymDex’s ability to incorporate the object acquisition phase before the interaction phase. Specifically, we initialize the environment for each task such that the objects of interest are placed on a tabletop surface. As such, each method needs to learn both to grasp the necessary objects and to coordinate the two hands to complete the tasks. 

For AsymDex, we follow the same strategy introduced in Section 4.4, and comapare its performance against the following baselines: 

- `Monolithic` : This baseline uses a single policy to learn both the grasping and interaction phases for both hands, allowing us to investigate the benefits of two-phase decomposition. 

- `2-stage-sym` : This policy benefits from the two phase decomposition but leverages neither asymmetry nor relative spaces. As such, this baseline allows us to examine if merely employing two-phase decomposition is sufficient. 

To ensure a fair comparison, we provide pre-grasp pose annotations to both baselines. Further, we ensure that the total number of env. interactions (the number of one stage or the sum of two stages) is the same across AsymDex and the baselines. See Appendix. B for details of the grasping learning. 







<!-- Start of picture text -->
(a) BiDexHand task training curve (b) Real-world task training curve<br><!-- End of picture text -->

Figure 4: AsymDex consistently outperforms the baselines in terms of sample efficiency and success rate. Solid lines indicate mean trends and shaded areas show _±_ std. dev., over five random seeds. 

7 

**AsymDex can effectively combine the acquisition and interaction phases** : We report the overall roll-out success rate of all methods for two tasks across five random seeds in Table. 2. We find that AsymDex significantly outperforms the other two baselines in both tasks, suggesting that combining phase decomposition with AsymDex’s other two design choices (asymmetry and relative spaces) results in policies that can effectively handle both the acquisition and the interaction phases of bimanual dexterous manipulation. The fact that `2-stage-sym` baseline outperforms the `Monolithic` baseline points to the inherent benefits of phase decomposition. Our qualitative analysis of _Block in cup_ task revealed that `Monolithic` policy learns to tip the cup over and push the block towards the cup. In contrast, both the two-stage policies learn more intuitive behaviors, suggesting that the phase decomposition nudges the grasping and interaction policies to learn reasonable behaviors that complement each other. 

### **5.2 Real-world Experiments** 

We finally evaluated AsymDex and the same baselines on the following 3 real-world bimanual manipulation tasks inspired by recent bimanual manipulation works [5, 19, 26, 52, 53, 54, 55]. 

**Hardware setup** : We use one 16-dof Allegro hand from Wonik Robotics and one 6-DoF Ability Hand from Psyonic. They are mounted on two 7-DoF Kinova Gen3 robotic arms. We used the Ability Hand for one of the hands since we only had access to one physical Allegro hand. For object pose information, we either employ an Realsense camera with AprilTag-based object tracking method or estimate it directly from the end-effector’s pose, especially during occlusion. 

**Real-world Tasks** : i) _Block in Cup_ : Place a block with sides of 5 cm inside a cylindrical cup with an internal diameter of 10 cm, ii) _Pour_ : Pour dry beans from one cup into another, and iii) _Twist Lid_ : Twist the lid off a jar while holding the jar. Snapshots are shown in Fig. 5. 

**Simulation Evaluation** : For each task, we first construct a simulated counterpart of our hardware setup and then train all policies in simulation. We then compared their performance in terms of _success rate_ and _sample efficiency_ , as reported in Fig. 4 (b). As observed in previous experiments, AsymDex consistently and significantly outperformed all baselines in terms of both metrics. 

**Sim2Real Transfer** : We deployed only the AsymDex policies on hardware since the baseline policies tended to exhibit either negligible success rates or aggressive behaviors that could damage the hardware. To enable effective sim-to-real transfer, we apply domain randomization during reinforcement learning, and details of the randomization process are provided in Appendix. D. 

**AsymDex enables zero-shot Sim2Real Transfer** : As shown in Block in cup Pouring Twist Lid Table. 3, AsymDex achieves high success rates across all deploy16/20 17/20 18/20 ments. This once again highlights the effectiveness of AsymDex in learning robust and reliable real-world bimanual dexterous maTable 3: Real-world task sucnipulation skills. For the _block in cup_ and _pour_ task, AsymDex is cess rates for AsymDex. simply trained with observation noise component of common domain randomization technique to learn a policy that can be deployed in real world successfully. For the most challenging _twist lid_ task, we added observation noise and action noise, as well as other randomization components for sim2real transfer. Though we utilized similar reward design as previous work [19] for this task, we observed that AsymDex learns a more natural and human-like behavior compared to the previous work. Besides, unlike previous work which fixes the hand base motion [2, 19], AsymDex is able to reposition and reorient both hand bases while two hands interact, enabling more fluent bimanual coordination. See Appendix. D for the detailed reward design and simulation success criterion for each task. 

Table 2: Success rates (mean _±_ std. dev.) after combining acquisition and interaction phases 

|**Task**<br>**Method**|`Monolithic`|`2-stage-sym`|`AsymDex`|
|---|---|---|---|
|_Block in cup_|0_._0321_±_0_._0251|0_._1505_±_0_._1059|**0.7938**_±_**0.0897**|
|_Bottle cap_|0_._0_±_0_._0|0_._2552_±_0_._1573|**0.6116**_±_**0.1328**|



8 











<!-- Start of picture text -->
(a) Block in cup (b) Pour<br><!-- End of picture text -->







<!-- Start of picture text -->
(c) Twist lid<br><!-- End of picture text -->

Figure 5: We created simulation environments to match our hardware setup. 

## **6 Conclusion** 

Our framework (AsymDex) is capable of learning complex asymmetric bimanual dexterous manipulation tasks via reinforcement without relying on demonstrations. We introduced and validated the need for AsymDex’s two crucial ingredients: assigning asymmetric roles to the two hands, and using relative observation and action spaces. Our evaluation results reveal that the combination of these choices consistently leads to better sample efficiency and success rates across different tasks. 

## **7 Limitations and Future Work** 

Our work has revealed a number of limitations and avenues for future research. First, AsymDex in its current form cannot handle certain bimanual tasks that require complex multi-finger manipulation from both hands (e.g., reorienting a heavy object, dynamic handover). Second, AsymDex does not consider the kinodynamic constraints that might result from manipulator arms. Three, behaviors produced by AsymDex are not always natural or human-like due to lack of necessary incentives. 

9 

## **References** 

- [1] C. Smith, Y. Karayiannidis, L. Nalpantidis, X. Gratal, P. Qi, D. V. Dimarogonas, and D. Kragic. Dual arm manipulation—a survey. _Robotics and Autonomous systems_ , 60(10):1340–1353, 2012. 

- [2] J. Grannen, Y. Wu, B. Vu, and D. Sadigh. Stabilize to act: Learning to coordinate for bimanual manipulation. In _Conference on Robot Learning_ , pages 563–576. PMLR, 2023. 

- [3] Y. Avigal, L. Berscheid, T. Asfour, T. Kr¨oger, and K. Goldberg. Speedfolding: Learning efficient bimanual folding of garments. In _2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 1–8. IEEE, 2022. 

- [4] C. Chi, Z. Xu, C. Pan, E. Cousineau, B. Burchfiel, S. Feng, R. Tedrake, and S. Song. Universal manipulation interface: In-the-wild robot teaching without in-the-wild robots. _arXiv preprint arXiv:2402.10329_ , 2024. 

- [5] C. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and C. K. Liu. Dexcap: Scalable and portable mocap data collection system for dexterous manipulation. _arXiv preprint arXiv:2403.07788_ , 2024. 

- [6] K. Zakka, P. Wu, L. Smith, N. Gileadi, T. Howell, X. B. Peng, S. Singh, Y. Tassa, P. Florence, A. Zeng, et al. Robopianist: Dexterous piano playing with deep reinforcement learning. _arXiv preprint arXiv:2304.04150_ , 2023. 

- [7] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine. Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2018. 

- [8] OpenAI, M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, J. Schneider, S. Sidor, J. Tobin, P. Welinder, L. Weng, and W. Zaremba. Learning Dexterous In-Hand Manipulation. _International Journal of Robotics Research (IJRR)_ , 2020. 

- [9] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik. In-hand object rotation via rapid motor adaptation. _arXiv preprint arXiv:2210.04887_ , 2022. 

- [10] Y. Han, M. Xie, Y. Zhao, and H. Ravichandar. On the utility of koopman operator theory in learning dexterous manipulation skills. In _Conference on Robot Learning_ , pages 106–126. PMLR, 2023. 

- [11] Y. Han, Z. Chen, K. A. Williams, and H. Ravichandar. Learning prehensile dexterity by imitating and emulating state-only observations. _IEEE Robotics and Automation Letters_ , 9(10): 8266–8273, 2024. 

- [12] H. Chen, A. ABUDUWEILI, A. Agrawal, Y. Han, H. Ravichandar, C. Liu, and J. Ichnowski. Korol: Learning visualizable object feature with koopman operator rollout for manipulation. In _8th Annual Conference on Robot Learning_ . 

- [13] K. Shaw, S. Bahl, A. Sivakumar, A. Kannan, and D. Pathak. Learning dexterity from human hand motion in internet videos. _The International Journal of Robotics Research_ , page 02783649241227559, 2024. 

- [14] Y. Chen, T. Wu, S. Wang, X. Feng, J. Jiang, Z. Lu, S. McAleer, H. Dong, S.-C. Zhu, and Y. Yang. Towards human-level bimanual dexterous manipulation with reinforcement learning. _Advances in Neural Information Processing Systems_ , 35:5150–5163, 2022. 

- [15] Y. Chen, C. Wang, Y. Yang, and C. K. Liu. Object-centric dexterous manipulation from human motion data. _arXiv preprint arXiv:2411.04005_ , 2024. 

10 

- [16] R.-Z. Qiu, S. Yang, X. Cheng, C. Chawla, J. Li, T. He, G. Yan, L. Paulsen, G. Yang, S. Yi, et al. Humanoid policy˜ human policy. _arXiv preprint arXiv:2503.13441_ , 2025. 

- [17] Z. Jiang, Y. Xie, K. Lin, Z. Xu, W. Wan, A. Mandlekar, L. Fan, and Y. Zhu. Dexmimicgen: Automated data generation for bimanual dexterous manipulation via imitation learning. _arXiv preprint arXiv:2410.24185_ , 2024. 

- [18] B. Zhou, H. Yuan, Y. Fu, and Z. Lu. Learning diverse bimanual dexterous manipulation skills from human demonstrations. _arXiv preprint arXiv:2410.02477_ , 2024. 

- [19] T. Lin, Z.-H. Yin, H. Qi, P. Abbeel, and J. Malik. Twisting lids off with two hands. _arXiv preprint arXiv:2403.02338_ , 2024. 

- [20] B. Huang, Y. Chen, T. Wang, Y. Qin, Y. Yang, N. Atanasov, and X. Wang. Dynamic handover: Throw and catch with bimanual hands. _arXiv preprint arXiv:2309.05655_ , 2023. 

- [21] Y. Guiard. Asymmetric division of labor in human skilled bimanual action: The kinematic chain as a model. _Journal of motor behavior_ , 19(4):486–517, 1987. 

- [22] M. Kimmerle, C. L. Ferre, K. A. Kotwica, and G. F. Michel. Development of role-differentiated bimanual manipulation during the infant’s first year. _Developmental Psychobiology: The Journal of the International Society for Developmental Psychobiology_ , 52(2):168–180, 2010. 

- [23] R. L. Sainburg. Evidence for a dynamic-dominance hypothesis of handedness. _Experimental brain research_ , 142:241–258, 2002. 

- [24] B. E. Studenka and H. N. Zelaznik. The influence of dominant versus non-dominant hand on event and emergent motor timing. _Human Movement Science_ , 27(1):29–52, 2008. 

- [25] L. Cashmore, N. Uomini, and A. Chapelain. The evolution of handedness in humans and great apes: a review and current issues. _Journal of anthropological sciences_ , 86(2008):7–35, 2008. 

- [26] A. Bahety, P. Mandikal, B. Abbatematteo, and R. Mart´ın-Mart´ın. Screwmimic: Bimanual imitation from human videos with screw space projection. _arXiv preprint arXiv:2405.03666_ , 2024. 

- [27] G. Franzese, L. de Souza Rosa, T. Verburg, L. Peternel, and J. Kober. Interactive imitation learning of bimanual movement primitives. _IEEE/ASME Transactions on Mechatronics_ , pages 1–13, 2023. 

- [28] M. Seo, S. Han, K. Sim, S. H. Bang, C. Gonzalez, L. Sentis, and Y. Zhu. Deep imitation learning for humanoid loco-manipulation through human teleoperation. In _2023 IEEE-RAS 22nd International Conference on Humanoid Robots (Humanoids)_ , pages 1–8. IEEE, 2023. 

- [29] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn. Learning fine-grained bimanual manipulation with low-cost hardware. _arXiv preprint arXiv:2304.13705_ , 2023. 

- [30] Y. Lin, A. Church, M. Yang, H. Li, J. Lloyd, D. Zhang, and N. F. Lepora. Bi-touch: Bimanual tactile manipulation with sim-to-real deep reinforcement learning. _IEEE Robotics and Automation Letters_ , 2023. 

- [31] S. Kataoka, S. K. S. Ghasemipour, D. Freeman, and I. Mordatch. Bi-manual manipulation and attachment via sim-to-real reinforcement learning. _arXiv preprint arXiv:2203.08277_ , 2022. 

- [32] R. Chitnis, S. Tulsiani, S. Gupta, and A. Gupta. Efficient bimanual manipulation using learned task schemas. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 1149–1155. IEEE, 2020. 

- [33] Y. Li, C. Pan, H. Xu, X. Wang, and Y. Wu. Efficient bimanual handover and rearrangement via symmetry-aware actor-critic learning. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 3867–3874. IEEE, 2023. 

11 

- [34] H. Jo, W. Choi, G. Lee, W. Park, and J. Kim. Analysis of visuo motor control between dominant hand and non-dominant hand for effective human-robot collaboration. _Sensors_ , 20(21):6368, 2020. 

- [35] R. Holladay, T. Lozano-P´erez, and A. Rodriguez. Robust planning for multi-stage forceful manipulation. _The International Journal of Robotics Research_ , 43(3):330–353, 2024. 

- [36] J. Grannen, Y. Wu, S. Belkhale, and D. Sadigh. Learning bimanual scooping policies for food acquisition. _arXiv preprint arXiv:2211.14652_ , 2022. 

- [37] J. Liu, Y. Chen, Z. Dong, S. Wang, S. Calinon, M. Li, and F. Chen. Robot cooking with stir-fry: Bimanual non-prehensile manipulation of semi-fluid objects. _IEEE Robotics and Automation Letters_ , 7(2):5159–5166, 2022. 

- [38] Y. Cui, Z. Xu, L. Zhong, P. Xu, Y. Shen, and Q. Tang. A task-adaptive deep reinforcement learning framework for dual-arm robot manipulation. _IEEE Transactions on Automation Science and Engineering_ , 2024. 

- [39] A. Nagabandi, K. Konolige, S. Levine, and V. Kumar. Deep dynamics models for learning dexterous manipulation. In _Conference on Robot Learning_ , pages 1101–1112. PMLR, 2020. 

- [40] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision_ , pages 570–587. Springer, 2022. 

- [41] G. Khandate, S. Shang, E. T. Chang, T. L. Saidi, J. Adams, and M. Ciocarlie. Samplingbased Exploration for Reinforcement Learning of Dexterous Manipulation. In _Proceedings of Robotics: Science and Systems_ , Daegu, Republic of Korea, July 2023. doi:10.15607/RSS. 2023.XIX.020. 

- [42] M. Xie, A. Handa, S. Tyree, D. Fox, H. Ravichandar, N. D. Ratliff, and K. Van Wyk. Neural geometric fabrics: Efficiently learning high-dimensional policies from demonstration. In _Conference on Robot Learning_ , pages 1355–1367. PMLR, 2023. 

- [43] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox. Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 9164–9170. IEEE, 2020. 

- [44] S. P. Arunachalam, I. G¨uzey, S. Chintala, and L. Pinto. Holo-dex: Teaching dexterity with immersive mixed reality. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 5962–5969. IEEE, 2023. 

- [45] T. Chen, E. Cousineau, N. Kuppuswamy, and P. Agrawal. Vegetable peeling: A case study in constrained dexterous manipulation. In _Towards Generalist Robots: Learning Paradigms for Scalable Skill Acquisition@ CoRL2023_ , 2023. 

- [46] R. Laha, J. Vorndamme, L. F. Figueredo, Z. Qu, A. Swikir, C. J¨ahne, and S. Haddadin. Coordinated motion generation and object placement: A reactive planning and landing approach. In _2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 9401–9407. IEEE, 2021. 

- [47] P. Chiacchio, S. Chiaverini, and B. Siciliano. Direct and inverse kinematics for coordinated motion tasks of a two-manipulator system. 1996. 

- [48] S. Tarbouriech, B. Navarro, P. Fraisse, A. Crosnier, A. Cherubini, and D. Sall´e. Dual-arm relative tasks performance using sparse kinematic control. In _2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 6003–6009. IEEE, 2018. 

12 

- [49] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov. Proximal policy optimization algorithms, 2017. 

- [50] S. Dasari, A. Gupta, and V. Kumar. Learning dexterous manipulation from exemplar object trajectories and pre-grasps. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 3889–3896. IEEE, 2023. 

- [51] J. Liang, V. Makoviychuk, A. Handa, N. Chentanez, M. Macklin, and D. Fox. Gpu-accelerated robotic simulation for distributed reinforcement learning, 2018. 

- [52] A. . Team, J. Aldaco, T. Armstrong, R. Baruch, J. Bingham, S. Chan, K. Draper, D. Dwibedi, C. Finn, P. Florence, S. Goodrich, W. Gramlich, T. Hage, A. Herzog, J. Hoech, T. Nguyen, I. Storz, B. Tabanpour, L. Takayama, J. Tompson, A. Wahid, T. Wahrburg, S. Xu, S. Yaroshenko, K. Zakka, and T. Z. Zhao. Aloha 2: An enhanced low-cost hardware for bimanual teleoperation, 2024. URL `https://arxiv.org/abs/2405.02292` . 

- [53] X. Cheng, J. Li, S. Yang, G. Yang, and X. Wang. Open-television: Teleoperation with immersive active visual feedback. In _8th Annual Conference on Robot Learning_ , 2024. URL `https://openreview.net/forum?id=Yce2jeILGt` . 

- [54] R. Ding, Y. Qin, J. Zhu, C. Jia, S. Yang, R. Yang, X. Qi, and X. Wang. Bunny-visionpro: Realtime bimanual dexterous teleoperation for imitation learning, 2024. URL `https://arxiv. org/abs/2407.03162` . 

- [55] K. Shaw, Y. Li, J. Yang, M. K. Srirama, R. Liu, H. Xiong, R. Mendonca, and D. Pathak. Bimanual dexterity for complex tasks. In _8th Annual Conference on Robot Learning_ , 2024. URL `https://openreview.net/forum?id=55tYfHvanf` . 

13 

# Appendices 

## **A Training Details** 

We use Proximal Policy Optimization (PPO) [49] algorithm to train all policies _π_ naive _, π_ asym _,_ and _π_ AsymDex with their corresponding value functions. Both policies and value functions are parameterized via a three-layer MLP network. The size of hidden layers for each is i) policy: (256, 256, 128), ii) value function: (512, 512, 512). The activation functions are all set as Exponential Linear Unit (ELU). We use the same PPO hyperparameters for all the baselines and AsymDex ( _γ_ : 0 _._ 98 _, λ_ : 0 _._ 95, clip range: 0.2, minibatch size: 8092). We use an adaptive learning rate with KL threshold of 0.016. We train the polices on a computer with a single Nividia RTX 4090 GPU. 

**Algorithm 1:** AsymDex: Interaction Phase 

**1** Randomly initialize the two hand bases’ poses _ξf_<sup>_b_(0) and</sup><sup>_ξ_</sup> _d_<sup>_b_(0), and initialize object poses</sup> _of_ (0) and _od_ (0) based on _ξf_<sup>_b_(0) and</sup><sup>_ξ_</sup> _d_<sup>_b_(0).Initialize policy</sup><sup>_πθ_.</sup> **2 for** _iter ∈{_ 1 _, ...,_ max _}_ **do 3** Initialize replay buffer _B_ = ∅ ; **4 for** _t ∈{_ 1 _, ..., M }_ **do 5 Simulate: 6** Collect hand and object states _ξf_<sup>_b_(</sup><sup>_t_),</sup><sup>_ξ_</sup> _d_<sup>_b_(</sup><sup>_t_),</sup><sup>_ξ_</sup> _d_<sup>_h_(</sup><sup>_t_),</sup><sup>_of_(</sup><sup>_t_),</sup><sup>_od_(</sup><sup>_t_);</sup> **7** Compute relative states _ξr_<sup>_b_(</sup><sup>_t_) =</sup><sup>_ξ_</sup> _a_<sup>_b_(</sup><sup>_t_)⊖</sup><sup>_Pf_,</sup><sup>_or_(</sup><sup>_t_) =</sup><sup>_od_(</sup><sup>_t_)⊖</sup><sup>_Pf_;</sup> **8** Policy _π_ AsymDex( _ξ_<sup>ˆ</sup> _r_<sup>_b_(</sup><sup>_t_)</sup><sup>_,_ˆ</sup><sup>_ξ_</sup> _d_<sup>_h_(</sup><sup>_t_)</sup><sup>_|ξ_</sup> _r_<sup>_b_(</sup><sup>_t_)</sup><sup>_, ξ_</sup> _d_<sup>_h_(</sup><sup>_t_)</sup><sup>_, or_(</sup><sup>_t_)) outputs relative actions;</sup> **9** Bimanual controller (Eqn. 1) computes _ξ_<sup>ˆ</sup> _f_<sup>_b_(</sup><sup>_t_) and</sup><sup>_ξ_ˆ</sup> _d_<sup>_b_(</sup><sup>_t_) based on</sup><sup>_ξ_ˆ</sup> _r_<sup>_b_(</sup><sup>_t_);</sup> **10 if** _Meet reset condition_ **then 11** Reset environment; **12 end 13** Environment physics steps with _ξ_<sup>ˆ</sup> _f_<sup>_b_(</sup><sup>_t_)</sup><sup>_,_ˆ</sup><sup>_ξ_</sup> _d_<sup>_b_(</sup><sup>_t_)</sup><sup>_,_ˆ</sup><sup>_ξ_</sup> _d_<sup>_h_(</sup><sup>_t_);</sup> **14 Evaluate: 15** Compute reward _r_ ( _t_ ) **16** Collect observations ( _ξr_<sup>_b_(</sup><sup>_t_)</sup><sup>_, ξ_</sup> _r_<sup>_h_(</sup><sup>_t_)</sup><sup>_, or_(</sup><sup>_t_)), actions (ˆ</sup><sup>_ξ_</sup> _r_<sup>_b_(</sup><sup>_t_)</sup><sup>_,_ˆ</sup><sup>_ξ_</sup> _r_<sup>_h_(</sup><sup>_t_)), and reward</sup><sup>_r_(</sup><sup>_t_)</sup> into buffer _B_ ; **17 end 18** Update the Policy _π_ AsymDex based on _B_ ; **19 end 20 Return:** Trained policy _π_ AsymDex 

## **B Grasping Learning** 

**Two-stage policy** Both AsymDex (our approach) and `2-stage-sym` policy (one of the baselines in Sec. 5.1.2) are two-stage policies. Therefore, they can first learn a grasping policy for the facilitating hand (or two grasping policies for facilitating hand and dominant hand respectively). Such policy _π_ grasp( _ξ_<sup>ˆ</sup> _f_<sup>_h_(</sup><sup>_t_)</sup><sup>_|ξ_</sup> _f_<sup>_h_(</sup><sup>_t_)</sup><sup>_, ξ_</sup> _f_<sup>_b_(</sup><sup>_t_) ⊖</sup><sup>_Pf_)takesin thehand jointstates andtherelative posebetween</sup> hand and the object, and outputs the target hand joint positions to grasp the object firmly. We first provide pre-grasp annotations [50], which allows the hands to initialize at the position close to the objects with proper joint positions. Then we script the 6 _D_ lifting hand base motions and design the the following rewards, which is the same across all objects. 

_Reward_ = _Rrel pos_ + _Rrel rot_ 

The relative position reward _Rrel pos_ = ( _α−||xobj −xinitial||_ ) _∗β_ , where _xobj_ is the current relative position between the object and the hand, and _xinitial_ is the initial relative position between the object and the hand. The _α, β ∈R_ + are hyper-parameters. The relative rotation reward _Rrel pos_ = _<_ 

14 

_uobj, uhand >_ , where _uobj_ is the object direction vector, _uhand_ is the hand direction vector, and _< ·, · >_ denotes the inner product of two vectors. We define the object direction vector and hand direction vector to be the same at the beginning of the grasping phase. Both rewards encourage the hand to keep a constant relative pose, i.e., grasping the object, during the script motion. 

**One-stage policy** Another baseline in Sec. 5.1.2, i.e., the `monolithic` policy, does not incorporate the task decomposition. Therefore, it only uses the task-specific interaction rewards (see Appendix. C) to learn how to complete the entire bimanual task. For a fair comparison, both hands also start at the pre-grasp poses. 

## **C BiDexHands Task Design** 

In this section, we show the details for each BiDexHands simulation task. 

**State Space Design** For each task, the hand joint states _ξf_<sup>_h_(</sup><sup>_t_),</sup><sup>_ξ_</sup> _d_<sup>_h_(</sup><sup>_t_)includethe24-DoFhand</sup> joint positions and the 24-DoF hand joint velocities. We use quaternions to represent rotation part of object and hand base poses. And for all policies, we also include the previous actions in the policy input. For the _block in cup_ task, _ξf_<sup>_obj_</sup> ( _t_ ) and _ξd_<sup>_obj_(</sup><sup>_t_)representtheposesofthecupandthe</sup> block respectively. For the _stack_ task, _ξf_<sup>_obj_</sup> ( _t_ ) and _ξd_<sup>_obj_(</sup><sup>_t_) represent the poses of two cups.For the</sup> _Bottle cap_ task, _ξf_<sup>_obj_</sup> ( _t_ ) and _ξd_<sup>_obj_(</sup><sup>_t_) represent the poses of the bottle and the cap respectively.For the</sup> _Switch_ task, _ξf_<sup>_obj_</sup> ( _t_ ) and _ξd_<sup>_obj_(</sup><sup>_t_) represent the poses of the switch body and the button respectively.</sup> The dimensions of the observation and action spaces of each policy are shown in Table. 4. It is obvious that AsymDex policy significantly reduces the state dimensions. 

Table 4: Dimension of Observation and action spaces. For all tasks, the dimensions are identical. 

||`Sym`|`Asym-w/o-rel`|`Rel-w/o-Asym`|`AsymDex` (ours)|
|---|---|---|---|---|
|_Observation_|176|108|163|88|
|_Action_|52|32|46|26|



### **Sampling Procedure** 

- _Block in cup_ : The initial position of dominant hand base is randomized: _xd ∈X ∼ U_ (0 _._ 3 _,_ 0 _._ 7), _yd ∈Y ∼U_ ( _−_ 0 _._ 2 _,_ 0 _._ 0), _zd ∈Z ∼U_ (0 _._ 7 _,_ 1 _._ 1). For the rotation of the dominant hand, we randomly rotate it around the axis along the arm at a random angle, _α ∈A ∼U_ ( _−_ 1 _._ 57 _,_ 1 _._ 57), in radians. The block is initialized in the dominant hand. Thus its position and rotation is calculated based on the initial position and rotation of dominant hand base. The initial position of the facilitating hand base is at [0 _._ 55 _,_ 0 _._ 6 _,_ 0 _._ 8]. 

- _Stack_ : The initial position of dominant hand base is randomized: _xd ∈X ∼U_ (0 _._ 3 _,_ 0 _._ 7), _yd ∈Y ∼U_ ( _−_ 0 _._ 2 _,_ 0 _._ 0), _zd ∈Z ∼U_ (0 _._ 7 _,_ 1 _._ 1). For the rotation of the dominant hand, we randomly rotate it around the axis along the arm at a random angle, _α ∈A ∼U_ ( _−_ 1 _._ 57 _,_ 1 _._ 57), in radians. The cup is initialized in the dominant hand. Thus its position and rotation is calculated based on the initial position and rotation of dominant hand. The initial position of the facilitating hand base is at [0 _._ 55 _,_ 0 _._ 6 _,_ 0 _._ 8]. 

- _∼_ 

- • _Bottle cap_ : The initial position of dominant hand base is randomized: _xd ∈X U_ (0 _._ 58 _,_ 0 _._ 62), _yd ∈Y ∼U_ ( _−_ 0 _._ 21 _, −_ 0 _._ 19), _zd ∈Z ∼U_ (0 _._ 58 _,_ 0 _._ 62). For the rotation of the dominant hand, we randomly rotate it around the axis along the arm at a random angle, _α ∈A ∼U_ ( _−_ 1 _._ 0 _,_ 1 _._ 0), in radians. The initial position of the facilitating hand base is randomized: _xf ∈X ∼U_ (0 _._ 53 _,_ 0 _._ 57), _yf ∈Y ∼U_ (0 _._ 59 _,_ 0 _._ 61), _zf ∈Z ∼U_ (0 _._ 43 _,_ 0 _._ 45). For the rotation of the facilitating hand, we randomly rotate it around the axis along the arm at a random angle, _β ∈B ∼U_ ( _−_ 0 _._ 5 _,_ 0 _._ 5), in radians. The bottle is initialized in the facilitating hand. Thus its position and rotation is calculated based on the initial position and rotation of facilitating hand base. 

15 

- _Switch_ : The initial position of dominant hand base is randomized: _xd ∈X ∼U_ (0 _._ 2 _,_ 0 _._ 6), _yd ∈Y ∼U_ ( _−_ 0 _._ 25 _, −_ 0 _._ 05), _zd ∈Z ∼U_ (0 _._ 5 _,_ 0 _._ 9). For the rotation of the dominant hand, we randomly rotate it around the axis along the arm at a random angle, _α ∈A ∼U_ ( _−_ 1 _._ 0 _,_ 1 _._ 0), in radians. The initial position of the facilitating hand base is randomized: _xf ∈X ∼U_ (0 _._ 2 _,_ 0 _._ 6), _yf ∈Y ∼U_ (0 _._ 05 _,_ 0 _._ 25), _zf ∈Z ∼U_ (0 _._ 41 _,_ 0 _._ 81). For the rotation of the facilitating hand, we randomly rotate it around the axis along the arm at a random angle, _β ∈B ∼U_ ( _−_ 1 _._ 0 _,_ 1 _._ 0), in radians. The switch is initialized in the facilitating hand. Thus its position and rotation is calculated based on the initial position and rotation of facilitating hand base. 

### **Success Criteria** 

- _Block in cup_ The task is considered successful if the distance of the block center and the cup center is smaller than 0.035 meters. This distance makes sure the task is only considered successful when the block is inside the cup. If the block falls on the ground or has not entered the cup within a certain time step, the task is considered failed. 

- _Stack_ The task is considered successful if the distance between the cup centers is smaller than 0.02 meters. If either cup falls on the ground or has not been stacked within a certain time step, the task is considered failed. 

- _Bottle cap_ The task is considered successful if the cap is taken off from its original position 0.05 meters away within a time duration, and is considered failed otherwise. 

- _Switch_ The button and the switch body are connected by a revolute joint ranging from 0 to 0.5585 rads. The task is considered successful if the button is pressed and rotated 0.3585 rads within a time duration, and is considered failed otherwise. 

**Reward Design** The reward design is similar across all tasks: 

_Reward_ = _α_ 1 _Rhand distance_ + _α_ 2 _Rprogress_ + _α_ 3 _Raction penalty_ + _α_ 4 _Rsuccess bonus_ 

For each task, _Raction penalty_ = _−||a_ ( _t_ ) _||_<sup>2</sup> , and the _Rsuccess bonus_ is the task success reward. _Rhand distance_ and _Rprogress_ are slightly different for each tasks. 

- _Block in cup_ : _Rhand distance_ = _e_<sup>_−||xpalm−xcupmouth||_</sup> , where _xpalm_ is the dominant hand palm position, and _xcup mouth_ is the position of the cup mouth. _Rprogress_ = _−||xcup − xblock||_ , where _xcup_ is the position of the cup, and _xblock_ is the position of the block. 

- _Stack_ : _Rhand distance_ = _e_<sup>_−||xpalm−xcupmouth||_</sup> , where _xpalm_ is the dominant hand palm position, and _xcup mouth_ is the position of the cup mouth, which is grasped by the facilitating hand. _Rprogress_ = _−||xcupd − xcupf ||_ , where _xcupf_ is the position of the cup grasped by the facilitating hand, and _xcupd_ is the position of the cup grasped by the dominant hand. 

- _Bottle cap_ : _Rhand distance_ = (1 _−_ ( _||xindex − xcap||_ + _||xthumb − xcap||_ ))<sup>3</sup> , where _xindex_ and _xthumb_ are the tip position of index finger and thumb respectively, and _xcap_ is the position of the bottle cap. _Rprogress_ = _||xcap − xbottle top||_ , where _xcap_ is the position of the cap, and _xbottle top_ is the position of the top of the bottle. 

- _Switch_ : _Rhand distance_ = (1 _−_ ( _||xindex −xbutton||_ + _||xthumb −xbutton||_ ))<sup>3</sup> , where _xindex_ and _xthumb_ are the tip position of index finger and thumb respectively, and _xbutton_ is the position of the button. _Rprogress_ = 2 _∗ θbutton_ , where _θbutton_ is the rotated angle of the joint that connects the button and the switch body. 

## **D Real-world Task Design** 

In this section, we present the details for each real-world task. 

16 

**State Space Design** For each task, the hand joint states _ξf_<sup>_h_(</sup><sup>_t_),</sup><sup>_ξ_</sup> _d_<sup>_h_(</sup><sup>_t_) include the 16-DoF hand joint</sup> positions. We use quaternions to represent rotation part of object and hand base poses. For the _block in cup_ task, _ξf_<sup>_obj_</sup> ( _t_ ) and _ξd_<sup>_obj_(</sup><sup>_t_)representtheposesofthecupandtheblockrespectively.Forthe</sup> _pour_ task, _ξf_<sup>_obj_</sup> ( _t_ ) and _ξd_<sup>_obj_(</sup><sup>_t_)representtheposesoftwocups.Forthe</sup><sup>_twistlid_task,</sup><sup>_ξ_</sup> _f_<sup>_obj_</sup> ( _t_ ) and _ξd_<sup>_obj_(</sup><sup>_t_) represent the poses of the jar and the lid respectively.The dimensions of the observation and</sup> action spaces of each policy are shown in Table. 5. AsymDex policy significantly reduces the state dimensions in real-world tasks consistently. 

Table 5: Dimension of Observation and action spaces. For all tasks, the dimensions are identical. 

||`Sym`|`Asym-w/o-rel`|`Rel-w/o-Asym`|`AsymDex` (ours)|
|---|---|---|---|---|
|_Observation_|60|44|53|30|
|_Action_|44|28|38|22|



**Sampling Procedure** The corresponding simulation environments of real-world tasks include two arms and two hands attached to them. Hence, we randomize the initial position of objects and hand poses by randomizing the initial joint angles of two Kinova arms. Then we initialize the poses of objects according to the initial hand poses. 

- _Block in cup_ : The default initial joint angles of the 7-DoF Kinova arms attached to the dominant hand are [0 _._ 0 _,_ 0 _._ 8 _,_ 0 _, π/_ 2+0 _._ 5 _,_ 0 _, −_ 1 _._ 3 _, −π/_ 2]. We randomized each angle by adding a _δθi_ : _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 1 _,_ 0 _._ 1) _, ∀i ∈{_ 1 _, . . . ,_ 4 _}_ ; _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 2 _,_ 0 _._ 2) _, ∀i ∈ {_ 5 _,_ 6 _}_ ; _δθ_ 7 _∈_ Θ7 _∼U_ ( _−_ 0 _._ 3 _,_ 0 _._ 3). The default initial joint angles of the 7-DoF Kinova arms attached to the facilitating hand are [ _−_ 0 _._ 0 _,_ 0 _._ 8 _,_ 0 _, π/_ 2 + 0 _._ 5 _,_ 0 _, −_ 1 _._ 3 _,_ 0]. We randomized each angle by adding a _δθi_ : _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 0 _,_ 0 _._ 0) _, ∀i ∈{_ 1 _, . . . ,_ 3 _}_ ; _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 1 _,_ 0 _._ 1) _, ∀i ∈{_ 4 _,_ 7 _}_ . 

- _Pour_ : The default initial joint angles of the 7-DoF Kinova arms attached to the dominant hand are [0 _._ 2 _,_ 0 _._ 8 _,_ 0 _, π/_ 2+0 _._ 5 _,_ 0 _, −_ 1 _._ 3 _, −π/_ 2]. We randomized each angle by adding a _δθi_ : _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 1 _,_ 0 _._ 1) _, ∀i ∈{_ 1 _, . . . ,_ 4 _}_ ; _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 2 _,_ 0 _._ 2) _, ∀i ∈{_ 5 _,_ 6 _}_ ; _δθ_ 7 _∈_ Θ7 _∼U_ ( _−_ 1 _._ 1 _,_ 0 _._ 6). The default initial joint angles of the 7-DoF Kinova arms attached to the facilitating hand are [ _−_ 0 _._ 2 _,_ 0 _._ 8 _,_ 0 _, π/_ 2 + 0 _._ 5 _,_ 0 _, −_ 1 _._ 3 _,_ 0]. We randomized each angle by adding a _δθi_ : _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 0 _,_ 0 _._ 0) _, ∀i ∈{_ 1 _, . . . ,_ 3 _}_ ; _δθi ∈_ Θ _i ∼ U_ ( _−_ 0 _._ 1 _,_ 0 _._ 1) _, ∀i ∈{_ 4 _,_ 7 _}_ . 

- _Twist lid_ : The default initial joint angles of the 7-DoF Kinova arms attached to the dominant hand are [0 _._ 1 _,_ 0 _._ 5 _,_ 0 _, π/_ 2 + 0 _._ 55 _,_ 0 _._ 75 _, −_ 1 _._ 5 _, −π/_ 2 _−_ 0 _._ 2]. We randomized each angle by adding a _δθi_ : _δθi ∈_ Θ _i ∼U_ ( _−_ 0 _._ 0 _,_ 0 _._ 0) _, ∀i ∈{_ 1 _, . . . ,_ 4 _}_ ; _δθ_ 5 _∈_ Θ5 _∼ U_ ( _−_ 0 _._ 05 _,_ 0 _._ 05); _δθ_ 6 _∈_ Θ6 _∼U_ ( _−_ 0 _._ 2 _,_ 0 _._ 0); _δθ_ 7 _∈_ Θ7 _∼U_ ( _−_ 0 _._ 1 _,_ 0 _._ 1). The default initial joint angles of the 7-DoF Kinova arms attached to the facilitating hand are [ _−_ 0 _._ 1 _,_ 0 _._ 8 _,_ 0 _, π/_ 2 + 0 _._ 5 _, −_ 0 _._ 7 _, −_ 1 _._ 35 _, −_ 0 _._ 1]. 

### **Success Criteria** 

- _Block in cup_ The task is considered successful if the distance of the block center and the cup center is smaller than 0.035 meters. This distance makes sure the task is only considered successful when the block is inside the cup. If the block falls on the ground or has not entered the cup within a certain time step, the task is considered failed. 

- _Pour_ The task is considered successful if the distance between the rims of the two cups is less than 0.035 meters and the cup grasped by the facilitating hand is up-right. If either cup falls on the ground or the task is not success within a certain time step, the task is considered failed. 

- _Twist lid_ We utilize the articulated bottle simulation of the previous work [19]. The lid and bottle are connected by a single revolute joint. The task is considered successful if the lid is rotated over 3 _× π_ rad within a time duration, and is considered failed otherwise. 

17 

**Reward Design** The reward function structure is similar across all tasks: 

_Reward_ = _Rtask_ + _α_ 2 _Raction penalty_ + _α_ 3 _Rsuccess bonus_ 

- For each task, _Raction penalty_ = _−||a_ ( _t_ ) _||_<sup>2</sup> , and the _Rsuccess bonus_ is the task success bonus. 

   - _Block in cup_ : _Rtask_ = _β_ 1 _Rhand dist_ + _β_ 2 _Rprogress_ . _Rhand dist_ = _e_<sup>_−||xpalm−xcuprim||_</sup> , where _xpalm_ is the dominant hand palm position, and _xcup rim_ is the position of the cup rim. _Rprogress_ = _−||xcup − xblock||_ , where _xcup_ is the position of the cup, and _xblock_ is the position of the block. 

   - _Pour_ : _Rtask_ = _β_ 1 _Rhand dist_ + _β_ 2 _Rprogress_ + _β_ 3 _Rcup orient_ . _Rhand dist_ = _e_<sup>_−||xpalm−xcuprim||_</sup> , where _xpalm_ is the dominant hand palm position, and _xcup rim_ is the position of the cup rim, which is grasped by the facilitating hand. _Rprogress_ = _−||xcupd − xcupf ||_ , where _xcupf_ is the position of the cup rim grasped by the facilitating hand, and _xcupd_ is the position of the cup rim grasped by the dominant hand. _Rcup orient_ = **z** _cupf ·_ **z** _world_ , where **z** _cupf_ is the z-axis unit vector of the cup grasped by the facilitating hand, and **z** _world_ is the z-axis unit vector of the world frame. 

   - • _Twist lid_ : _Rtask_ = _β_ 1 _Rorient_ + _β_ 2 _Rtwist_ + _β_ 3 _Rfinger dist_ + _β_ 4 _Rhand dist penalty_ . _Rorient_ = **z** _bottle ·_ **z** _world_ , where **z** _bottle_ is the z-axis unit vector of the bottle grasped by the facilitating hand, and **z** _world_ is the z-axis unit vector of the world frame. _Rtwist_ = _θlid_<sup>_t−_</sup> _θlid_<sup>_t−_1, where</sup><sup>_θ_</sup> _lid_<sup>_t_is the current bottle-lid revolute joint angle, and</sup><sup>_θ_</sup> _lid_<sup>_t−_1is the previous bottle-</sup> lid revolute joint angle. And _Rfinger dist_ is the _finger contact reward_ we adopted from a previous lid twisting work [19]. _Rhand dist penalty_ = _−min_ (( _||xf − xd|| −_ 0 _._ 1) _,_ 0 _._ 0), where _xf_ and _xd_ are the position of the facilitating hand palm and the dominant hand palm. 

**Domain Randomization** The domain randomization details are shown in Table. 6 

Table 6: Domain Randomization Setup. 

|**Object: Friction (only for****_twist lid_ task)**|[0.5, 1.5]|
|---|---|
|**Hand: Friction (only for****_twist lid_ task)**|[0.5, 1.5]|
|**Object Pos Observation Noise**|+_N_(0_,_0_._02)<br>|
|**Hand Joint Observation Noise**|+_N_(0_,_0_._2)|
|**Hand Pos Observation Noise**|+_N_(0_,_0_._02)|
|**Hand Orientation Observation Noise**|+_N_(0_,_0_._05)|
|**Action Noise (only for****_twist lid_ task)**|+_N_(0_,_0_._1)|



18 

