# **Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators** 

**Apurva Badithela**<sup>1</sup> , **David Snyder**<sup>1</sup><sup>_∗_</sup> , **Lihan Zha**<sup>1</sup><sup>_∗_</sup> , **Joseph Mikhail**<sup>2</sup> , **Matthew O’Kelly**<sup>3</sup><sup>_†_</sup> , **Anushri Dixit**<sup>4</sup><sup>_†_</sup> , **Anirudha Majumdar**<sup>1</sup> 

> 1Princeton University, 2University of Texas, Austin, 3Waymo, 4University of California, Los Angeles 

> _∗_ Equal contribution, _†_ Equal advising. 

Rapid progress in imitation learning, foundation models, and large-scale datasets has led to robot manipulation policies that generalize to a wide-range of tasks and environments. However, rigorous evaluation of these policies remains a challenge. Typically in practice, robot policies are often evaluated on a small number of hardware trials without any statistical assurances. We present SureSim, a framework to augment large-scale simulation with relatively small-scale real-world testing to provide reliable inferences on the real-world performance of a policy. Our key idea is to formalize the problem of combining real and simulation evaluations as a prediction-powered inference problem, in which a small number of paired real and simulation evaluations are used to rectify bias in large-scale simulation. We then leverage non-asymptotic mean estimation algorithms to provide confidence intervals on mean policy performance. Using physics-based simulation, we evaluate both diffusion policy and multi-task fine-tuned _π_ 0 on a joint distribution of objects and initial conditions, and find that our approach saves over 20 _−_ 25% of hardware evaluation effort to achieve similar bounds on policy performance. 

**Keywords:** Policy Evaluation, Finite-Sample Statistical Inferences, Real2Sim 

**Website: suresim-robot-eval.github.io** 





<!-- Start of picture text -->
Small-scale Real Evaluation Paired Simulation Evaluations Task and environment distribution<br>𝒟 env Initial Conditions<br>Real2Sim<br>Task<br>Large-scale Simulation Evaluation Correcting  bias  in<br>simulation ( rectifier )<br>Finite-sample valid<br>confidence interval ℙ( μ * ∈ CI ) ≥1 − α<br>Mean<br>performance in  CI  on real On  true, real-world  mean policy<br>simulation performance performance  μ * over 𝒟 env<br><!-- End of picture text -->

**Figure 1** Our goal is to evaluate a policy by computing bounds on its mean real-world performance on a diverse environment distribution _D_ env. We present a framework that augments real-world evaluations with simulation evaluations to provide stronger inferences on real-world policy performance that could otherwise only be obtained by scaling up real-world evaluations. 

## **1 Introduction** 

Advancing robot learning requires statistically rigorous policy evaluation for reliably assessing how policies generalize to new tasks and environments [1–3]. Rapid progress in deep learning was driven by standardized metrics and evaluation benchmarks such as ImageNet [4] and COCO [5] in computer vision, and SquaD [6] and GLUE/SuperGLUE [7, 8] in natural language. Unlike the static benchmarks in these domains, robot 

1 

policy evaluation in the real-world requires physical interaction of the robot and its environment which is resource intensive in time and human effort. For instance, consider the fundamental question of evaluating the success rate of a policy on a distribution of environments. Due to the expensive nature of real-world evaluation, most research studies report empirical success rates of policies evaluated on a small number (e.g., 20-40) of trials. At the same time, there is a growing consensus for rigorous statistical analysis and nuanced discussions of evaluation criteria and policy failure modes [1, 3, 9]. As a result, assessing whether a policy will perform reliably in a new environment distribution remains a core challenge [2]. 

In robotic manipulation, recent advances in physics-based simulators [10] and action-conditioned video prediction models [11, 12] provide scalable alternatives to real-world policy evaluation. While growing evidence suggests that simulation performance correlates well with real-world performance in aggregate across a diversity of tasks and environments [13, 14], the simulation-to-real gap precludes rigorous statistical inferences about real-world outcomes from simulation results alone. This paper presents a framework to augment a small number of real-world evaluations with large-scale simulations to achieve scalable policy evaluation with trustworthy statistical inferences about real-world performance. Crucially, our framework can achieve tighter statistical bounds on policy performance by scaling up the number of simulations in place of scaling the number of real-world evaluations. 

However, using large-scale simulations for policy evaluation with trustworthy statistical inferences on real performance faces significant challenges due to the simulation-to-real gap, stemming from mismatches in visual features (e.g., lighting conditions, object textures) and inaccurate modeling of contact physics and real physical parameters (e.g., friction coefficients) [15, 16]. Current robot policies, including foundation models and imitation learning-based policies, can be sensitive to such discrepancies. As a result, performance bounds solely relying on large-scale simulation predictions can be biased. 

We tackle the aforementioned challenges in order to provide confidence intervals on mean performance of robot manipulation policies. Our key idea is to connect the problem of combining simulated and real-world evaluations to that of prediction powered inference (PPI) [17, 18]. PPI is a paradigm for valid statistical inference that can leverage a large set of learned model predictions together with a comparatively small number of gold-standard data. In our setting, gold-standard labels are real-world evaluations of a policy, while the predictions are obtained from simulation evaluations. For a bounded performance metric, the resulting confidence intervals on mean policy performance are valid with the finite samples of real and simulated data. When simulation is sufficiently predictive, PPI yields tighter non-asymptotic confidence bounds than using real-world trials alone, allowing us to scale with simulation rather than costly hardware evaluations. Our experiments show that it is possible to save 20 _−_ 25% of hardware trials using state-of-the-art physics-based simulators [10]. 

**Statement of Contributions.** First, we present a rigorous policy evaluation framework for finite-sample valid inferences on real-world performance by combining large-scale simulation trials with a relatively small number of real trials. A key element is pairing each real trial with its corresponding simulation trial on the same task or environment instance to estimate and correct for simulation bias. To operationalize this, we introduce a real2sim pipeline to leverage prediction powered inference, and we identify best practices for integrating simulation with real-world evaluation to obtain tighter confidence intervals. Second, we demonstrate our evaluation paradigm on a single-task diffusion policy [19] trained from scratch as well as the robot foundation model _π_ 0 [20] finetuned on multiple tasks. Finally, we discuss the sensitivity of our method to different types of real-simulation gap, including an example of when the gap is too large for simulation to provide benefits over real-only trials. 

## **2 Related Work** 

**Real-world Policy Evaluation.** Real-world evaluation is expensive because it offers limited parallelism while often requiring manual logging of outcomes and careful resetting of environments. Yet, it remains the gold-standard for assessing policy performance, driving significant efforts to establish standardized robotic benchmarks with carefully defined tasks, environments, and robot setups for reproducible policy evaluation [21– 25]. A comprehensive list of best practices for rigorously evaluating robot policies is detailed in [1]. To address these challenges, the community is building cloud-based evaluation platforms [15, 26–29] and distributed 

2 

evaluator networks for unbiased, pairwise policy comparisons [30]. For example, AutoEval [15] autonomously classifies outcomes and resets environments using fine-tuned robot foundation models, while RoboArena [30] evaluates policies on the DROID platform [31]. However, rapidly evaluating policies by scaling hardware evaluations with sufficient coverage for statistical assurances remains challenging. 

**Policy Evaluation in Simulation.** Physics-based simulation benchmarks [10, 32–40] offer a reproducible and cheaper alternative to real-world robot policy evaluation. For example, SIMPLER [13] uses system identification and real2sim image editing methods to mitigate visual and dynamics discrepancies, showing that simulationbased performance rankings of vision-language-action models from match real-world rankings. However, setting up physics-based simulation can be time-consuming, especially when optimizing for visual fidelity and accurate matching of real-world dynamics. On the other hand, action-conditioned video world models [11, 41, 42] promise faster scene initialization via text, image, or video prompts [43]. While their use in policy evaluation is nascent, it is attracting growing interest due to advantages over physics-based simulation [12, 14]. These models, however, remain susceptible to hallucinations, and accurately capturing real-world dynamics is still a major challenge. Yet, simulation remains a valuable proxy. For example, simulation-based rankings—whether across different policies or for a given policy under diverse environmental factors—have been shown to correlate well with real-world performance [13, 14, 21, 38, 44]. Predictive red-teaming algorithms [45] offer an alternative to simulation by predicting whether a policy will succeed in a new environment without policy rollouts, showing strong correlation between real and predicted performance rankings across various environmental factors. In contrast to these methods, our approach leverages simulation, even when imperfect, to provide assurances on _real_ policy performance over a distribution of tasks and environments. 

**Statistically Confident Policy Evaluation.** In end-to-end self-driving applications, scalable simulation-based evaluation using importance sampling was used to provide statistical confidence on the safety of a selfdriving policy [46]. However, real-world evaluation remains gold-standard since it is difficult to model the real distribution of environments in simulation, which can lead to a bias in the resulting guarantees. In manipulation, limited by real-world evaluation costs and the large diversity of environments to evaluate in, researchers typically compare policy performance using only 20-30 real-world trials. However, such small sample sizes are insufficient to draw statistically significant conclusions in policy comparisons [9]. Recognizing this need for reliable policy evaluation, a recent study compares generalist large behavior models to single-task policy counterpart using rigorous statistical evaluation methods, incorporating A/B real-world testing, and comprehensive real-world and simulation trials with robust statistical analysis [3]. Sequential policy comparison frameworks further reduce real-world evaluation cost while maintaining statistical validity under anytime stopping [9]. Beyond comparing policies, it is also important to assess the individual policy performance. For binary success criteria, Vincent _et al._ [47] provide optimal confidence intervals from real evaluations. For non-binary metrics, confidence intervals may be obtained from real-world evaluation samples via concentration inequalities (e.g., Hoeffding [48]), though this would require a large real evaluation budget. Instead, we scale simulation while requiring a small number of real evaluations to ensure reliability. 

Finally, concurrent to our work are efforts that apply statistical inference techniques to off-policy evaluation [49], and the use of control variates to combine simulation evaluation with real-world logged data for evaluation in self-driving applications [50]. While conceptually related, our work differs in two key respects. First, we present finite-sample valid confidence bounds on real-world performance of manipulation policies that are tighter than existing baselines. Secondly, we demonstrate the idea of combining real-world and simulation evaluations on robotic manipulation, which faces a unique set of challenges — robot policies can be sensitive to small perturbations in the environment, and the robot and environment state are more tightly interdependent. 

## **3 Problem Statement** 

Let _D_ env denote a distribution over real-world environments _X_ in which we wish to evaluate a robot policy _π ∈_ Π. In robotic manipulation, this distribution could be defined by the diversity of objects and tasks, environmental factors (e.g., lighting, background, table texture), and spatial variations in object and robot poses, among others. We assume a bounded evaluation metric _M_ : _X ×_ Π _→_ [0 _,_ 1], such as a success/failure metric or a continuous metric for partial task completion. 

We consider the mean estimation problem in policy evaluation, where the goal is to estimate the policy’s 

3 

average performance according to metric _M_ over the environment distribution _D_ env. Formally, we define mean policy performance _µ_<sup>_∗_</sup> as: 



where _Y_ ( _X_ ) = _M_ ( _X, π_ ) is the outcome of evaluating policy _π_ in environment _X_ under metric _M_ . For sampled iid environments _X_ 1 _, . . . , Xn ∼D_ env, the outcomes of real-world policy evaluation according to metric _M_ are denoted as _Y_ 1 _, . . . , Yn_ , respectively. We define the empirical evaluation sample as _Sn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ . Using the empirical data _Sn_ we seek a confidence interval _CI_ = ( _l, u_ ) that contains _µ_<sup>_∗_</sup> with high probability. Confidence intervals provide bounds on the true performance of a policy with high probability, and can be useful for decision-making and policy comparison. Mathematically stated, for any significance level _α ∈_ (0 _,_ 1) and any finite number _n_ of real-world evaluations, we seek a confidence interval _CI_ such that: 



where the probability measure is defined over the draw of the empirical evaluation sample _Sn_ . Any method that satisfies Equation (1) is Type-I error controlling at significance level _α_ . While the interval [0 _,_ 1] trivially satisfies this guarantee, it provides little insight; therefore, we seek a tight confidence interval satisfying Equation (1). Importantly, we make no assumptions on the distribution of _Yi_ beyond measurability and the boundedness induced by the metric _M_ . We do not require _a priori_ knowledge of a distribution family, the existence of a density, or other structural assumptions. 

A nonasymptotic confidence interval for _µ_<sup>_∗_</sup> can be derived directly from the finite number of gold-standard evaluations _Y_ 1 _, . . . , Yn_ using standard non-asymptotic methods like Hoeffding [48] or Bernstein inequalities, or more recent state-of-the-art betting-based methods [51]. Ideally, we want a tight interval concentrated around _µ_<sup>_∗_</sup> , but collecting a large number of real-world evaluations is costly. In contrast, simulation evaluations are relatively cheap and scalable. This motivates the central question of our work: _Can we make valid inferences on the real performance of a policy by augmenting a small amount of real-world evaluations with a large number of simulation evaluations?_ 

## **4 Approach: Simulation to Augment Real Tests via Prediction Powered Inference** 

Suppose we have access to a simulator for policy evaluation. Let _X_ sim denote the set of simulation environments. We can define a real2sim function _g_ : _X →X_ sim that translates a real environment setup into simulation. For each real environment _X ∈X_ , the corresponding simulation environment is defined as _X_<sup>˜</sup> = _g_ ( _X_ ). For example, as shown in Figure 1, if _X_ is a robot manipulation environment—defined by the robot (type, dynamics, texture, and initial pose), the objects (3D models, textures, material properties, and initial pose), and background conditions (lighting and background textures) — then the corresponding simulation environment _X_ ˜ is constructed to closely match the real-world dynamics and visual features. Simulation evaluations are given by the function _f_ : _X_ sim _→_ [0 _,_ 1] defined as _f_ ( _X_<sup>˜</sup> ) = _M_ sim( _X, π_<sup>˜</sup> ), where _X_<sup>˜</sup> _∈X_ sim and _M_ sim simulation evaluation metric. 

Correcting for bias in large-scale simulation predictions and deriving valid confidence intervals for _µ_<sup>_∗_</sup> requires more than simply combining real and simulated evaluations through imputation. To tackle this challenge, we identify prediction powered inference (PPI) [17] as a suitable mathematical framework for our problem. Prediction powered inference enables valid statistical inference when experimental datasets are supplemented with machine-learning predictions. It has been applied to diverse problems such as protein structure analysis with AlphaFold, galaxy classification, and deforestation monitoring using computer vision [17]. For example, in galaxy classification, human annotators provide a limited set of ground-truth labels (“spiral” vs. “not spiral”) from galaxy images, while computer vision models provide cheaper predictions on the input images at a much larger-scale. 

**SureSim.** In our setting, each input corresponds to a robot manipulation environment _X_ , with the groundtruth label given by real outcome _Y_ ( _X_ ) of rolling out the policy. We choose simulation as a proxy for real-world evaluation but unlike the problems studied in [17], we cannot directly evaluate on _X_ in simulation. Composing the real2sim function with the simulator yields simulation predictions for real environments: _f_ ( _X_<sup>˜</sup> ) = _f_ ( _g_ ( _X_ )). 

4 

This formulation enables us to apply prediction-powered inference to rigorously combine real-world trials with large-scale simulation for reliable estimates of real performance. To apply PPI, we require a small number of iid paired evaluations in both real and simulation. For the set of _n_ + _N_ real environments _X_ 1 _, . . . Xn_ + _N ∼D_ env, we apply the real2sim function to get simulation environments _X_<sup>˜</sup> 1 _, . . . , X_<sup>˜</sup> _n_ + _N_ , where _X_<sup>˜</sup> _i_ = _g_ ( _Xi_ ). The corresponding outcomes of evaluating the policy in simulation are denoted as _f_ ( _X_<sup>˜</sup> 1) _, . . . , f_ ( _X_<sup>˜</sup> _n_ + _N_ ). Uniformly at random, we select _n_ of those environments in which to conduct real trials. Thus, the paired evaluation data comprises of the real-world outcomes and associated simulation predictions: _D_ paired = _{_ ( _Yi, f_ ( _X_<sup>˜</sup> _i_ )) _}i_<sup>_n_</sup> =1<sup>.</sup> The remaining number of additional simulation evaluations _N_ exceeds the number of real-world evaluations _n_ , and these are denoted as _D_ sim = _{f_ ( _X_<sup>˜</sup> _i_ ) _}_<sup>_n_</sup> _i_ =<sup>+</sup> _n_<sup>_N_</sup> +1<sup>.The</sup><sup>_ith_datasampleisdefinedas:</sup> 



where _ξi_ is an indicator of whether ( _Yi, f_ ( _X_<sup>˜</sup> _i_ )) _∈ D_ paired. The sample mean of Equation (2) yields the uniform PPI estimator for _µ_<sup>_∗_</sup> [52]: 



The first term is referred as the rectifier, since it adjusts the bias in simulation predictions. For some significance level _α_ , a confidence interval for _µ_<sup>_∗_</sup> is computed from the sample evaluation data (Equation (2)) using non-asymptotic methods for mean estimation via the Waudby-Smith and Ramdas (WSR) algorithm [51], which just requires the bounds of the random variable to be specified a priori. This method is denoted as **SureSim** ( **S** calable and **R** eliable Policy **E** valuation with **Sim** ulation), and the framework is summarized in Algorithm 1. We also present a hedged variant termed **SureSim** - **UB** which returns a confidence interval resulting from a union bound of **SureSim** (computed at budget<sup><u>3</u></sup> 4<sup>_<u>α</u>_)and</sup><sup>**Classical**(atbudget</sup><sup>_<u>α</u>_</sup> 4<sup>).</sup> 

**SureSim (2-Stage)** . Prediction-powered inference was originally introduced with a two-stage setup for data sampling [17]. This approach considers two sets of environments drawn i.i.d from _D_ env: the first set consists of a small number _n_ of environments for which we collect both real and paired simulation evaluations, and the second set consists of a large number _N_ of additional simulations. The PPI estimator for mean estimation is defined as: 



where _µ_ PPI is also an unbiased estimate of _µ_<sup>_∗_</sup> . If we assume real and simulation scores to lie in the range [0 _,_ 1], the rectifier is bounded between [ _−_ 1 _,_ 1]. For a significance level _α_ , a confidence interval on _µ_<sup>_∗_</sup> is computed by separately deriving confidence intervals for the rectifier at some significance level _δ < α_ and for the additional simulation data at significance _α − δ_ , and taking their Minkowski sum [17].<sup>1</sup> For mean estimation, it can be proven that the true mean _µ_<sup>_∗_</sup> lies in the resulting confidence interval with probability 1 _− α_ [17]. To obtain finite sample guarantees, the rectifier and prediction confidence intervals are computed using WSR [51]. In this two-stage approach, the bloating of the rectifier bounds coupled with the small number _n_ of rectifier samples introduces inefficiencies in the resulting confidence interval. Similar to **SureSim** - **UB** , we also introduce a hedged version of this method termed **SureSim** - **UB (2-Stage)** . 

**Theorem 1. SureSim** _and its variants return finite-sample valid confidence interval CI that satisfies Equation_ (1) _._ 

_Proof._ By construction of the real2sim function, the prediction rule is the functional composition _f ◦ g_ : _X →_ [0 _,_ 1]. Under the assumption that _{Xi}_<sup>_n_</sup> _i_ =1<sup>+</sup><sup>_N_</sup> are drawn i.i.d from the task and distribution _D_ env, the finite-sample validity of the resulting confidence interval follows directly from [17, 52]. 

> 1The allocation of risk to _δ_ and _α − δ_ can be approximately optimized. In practical settings, using _δ ≈_ 0 _._ 9 _α_ is a reliable heuristic. 

5 

#### **Algorithm 1: SureSim** 

**Data:** Real task and environment distribution _D_ env, Real-to-sim function _g_ , Policy _π_ , Real metric _M_ , Simulation metric _M_ sim, Significance levels 0 _< δ < α <_ 1 **Result:** Confidence interval _CI_ on true mean _µ_<sup>_∗_</sup> Sample environments _X_ 1 _. . . , Xn_ + _N ∼D_ env **for** _i ←_ 1 **to** _n_ + _N_ **do** 

_X_ ˜ _i ← g_ ( _Xi_ ) _▷_ Apply real2sim function _f_ ( _X_<sup>˜</sup> _i_ ) _← M_ sim( _X_<sup>˜</sup> _i, π_ ) _▷_ Simulation evaluation **end for** _i ←_ 1 **to** _n_ **do** _Yi ← M_ ( _Xi, π_ ) _▷_ Real evaluation **end** _D_ paired = _{_ ( _Yi, f_ ( _X_<sup>˜</sup> _i_ )) _}i_<sup>_n_</sup> =1<sup>,</sup><sup>_D_sim=</sup><sup>_{f_( ˜</sup><sup>_Xi_)</sup><sup>_}n_</sup> _i_ =<sup>+</sup> _n_<sup>_N_</sup> +1 _CI ←_ PPI( _D_ paired _, D_ sim _, f, n, N, α, δ_ ) _▷_ UniformPPI or 2-StagePPI **<u>return</u>** _<u>CI</u>_ 

**Baseline.** Termed as **Classical** , our primary baseline computes finite-sample confidence intervals — without augmenting simulation — by applying the non-asymptotic WSR procedure [17, 51] directly on real evaluations. These intervals represent the standard procedure for obtaining confidence intervals on the mean, and serve as an ablation with respect to the incorporation of proxy data. 

**Related Methods.** While we primarily compare our methods to **Classical** since it provides a finite-sample guarantee, we also implement and discuss the control variates procedure (denoted **Control Variate** ) [50] in the sim2sim setting. We do not consider it a baseline for the hardware experiments because it is not provably Type-I error controlling in finite samples. Therefore, the practitioner cannot know for their problem that the resulting confidence interval from [50] contains the true mean at a specified level of confidence. In particular, this procedure utilizes the empirical correlation of the simulation evaluations to make optimization-based reductions to the mean estimation, at the expense of looser dependence on the confidence level _α_ . These paired samples yield a variance estimate for the control variate estimator, which is subsequently used in Chebyshev’s inequality to derive a confidence interval for the mean [50]. However, in finite-sample settings, the variance estimate may be biased for small _n_ , and even unbiased constructions (such as through data splitting) need not upper-bound the _true_ variance, a requirement for Chebyshev’s inequality. 

## **5 Robot Experiments** 

We illustrate our method on pick-and-place tasks and evaluate policy generalization across diverse pick object types and initial conditions. Specifically, we seek to address the following questions: 

1. How tight are our confidence intervals relative to the baselines? What benefit does this translate to in terms of real-world evaluation cost? 

2. How does the confidence interval width decrease as we scale the number of simulation evaluations? 

3. How well does our method perform under high and low real-simulation correlation? 

**Real2Sim Pipeline.** For evaluating object generalization, we gathered around 120 objects, most of which are toy kitchen items, shown in Figure 2. To carry out paired evaluations in simulations, 3D models for these objects were obtained from a single image of the object using an off-the-shelf tool Meshy. These 3D models were scaled to match real-world dimensions, and their pose was set according to real-world experiments. To construct the additional simulation dataset, we draw over 2100 objects from the RoboCASA repository [36], 



**Figure 2** Objects used for real-world evaluations. 

6 

which includes assets from Objaverse [53] and assets generated using a text-to-3D model Luma AI. We filter out assets that are not semantically or geometrically equivalent—objects whose category or shape lacks a counterpart in the real-world set (e.g., plates). 

In an ideal setting, we would have access to a large-scale repository of real-world objects paired with corresponding 3D models—akin to the YCB dataset [54], but expanded to include thousands of objects. This would allow us to uniformly sample a subset of objects for real-world and paired simulation evaluation, while using the remaining objects exclusively for additional simulation evaluations. However, these large datasets do not at present exist, and therefore, we take these 120 objects are taken to approximate the real-world distribution of objects that we wish to evaluate our policy on. 

**Experimental Setup.** We evaluate policies on a Franka Panda robot equipped with a wrist-mounted RealSense D405 and a Logitech C920 third-person camera. For simulation, we replicate the setup in ManiSkill3 [10] by constructing a customized Franka Panda robot in which the default gripper is replaced with the 3D model used in our real-world experiments. The robot base pose in simulation is aligned with the real robot through manual calibration. Similarly, we transfer the camera calibration parameters from the real setup—covering both the wrist-mounted camera and the third-person camera—to their counterparts in simulation. We use the same control frequency as the robot in the real world. The workspace table is constructed by scripting a table-like mesh and overlaying it with the texture of the real table. For the background, we import a real-world mesh obtained via 3D scanning. Finally, we use the default shader with shadows enabled to strike a balance between simulation speed and visual quality, and tune lighting parameters until policy performance in simulation on randomly selected initial conditions is as high as possible. 

**Policies.** We evaluate two policies: i) a single-task diffusion policy [19] trained from scratch and ii) a generalist policy _π_ 0 [20], fine-tuned on multiple objects. Our diffusion policy is trained on 200 demonstrations of a single task — to pick up a tomato and place it in a plate. The training distribution comprises of the tomato and the plate being placed randomly in a 30cm-by-40cm space. Though trained on a single object, we evaluate this diffusion policy on its generalization to multiple objects. We finetune _π_ 0 for 7 different objects according to the language instruction “put _<_ object _>_ into the box” with 40 demonstrations for each object. In the fine-tuning demonstrations, the _pick_ object is randomly placed in a 10cm-by-20cm grid, while the box is placed at roughly the same xy-position. After each inference step, the open-loop action horizon was set to full action chunk size of 30. 

**Evaluation Metrics.** For each real object, we rollout diffusion policy and _π_ 0 at five different initial conditions of the pick object as shown in Figures 3a and 3b, respectively. Each rollout is assigned a partial evaluation score: 0 for no grasp, 0.25 for a failed grasp (object slips), 0.5 for a successful grasp, 0.75 for successful grasp but unsuccessful release over the place object, and 1 for complete task success. In simulation, we record a partial success score as follows: 0 for no grasp, 0.5 for successful grasp, and 1 for complete task success. 

**Real-Simulation Evaluation Gap.** Additionally, we discuss the real-simulation evaluation gap for robot manipulation, and share a few insights to mitigate 



<!-- Start of picture text -->
2 1 3<br>4 5<br>(a) Diffusion Policy Setup (b) π 0 Setup<br><!-- End of picture text -->

**Figure 3** Initial conditions for evaluation experiments 

this. Crucially, for mean estimation, this gap manifests in the variance of the rectifier, which represents the difference in the real and simulation outcomes on the paired set _D_ paired. That is, a high rectifier variance corresponds to low correlation on _D_ paired and a high real-simulation gap, while a low variance corresponds to high correlation and a small gap. Depending on the evaluation criteria used for constructing _D_ paired, well-known sources of the real-simulation gap — such as visual and dynamics discrepancies — can reduce the reliability of simulation in predicting real outcomes and increase rectifier variance. For stochastic policies (e.g., diffusion policy which has randomness in the denoising process), this mismatch is further exacerbated by inconsistencies in policy seeding between real and simulated runs. For example, if we evaluate diffusion policy using a discrete evaluation metric over a set of initial conditions by pairing a single hardware trial 

7 

with a simulation evaluation at the same initial condition, we are unlikely to see a high correlation on the paired set of evaluations. For the same real-simulation experimental setup, the rectifier variance can vary with the task and evaluation criteria, the policy under evaluation, and the axis of generalization considered in the distribution _D_ env. Together, these factors can lead to low correlation in paired evaluations, thereby diminishing the predictive utility of simulation and undermining the advantage of large-scale simulation for trustworthy inference on real performance. To address this issue, we implement the following measures: (1) we ensure that both real-world and simulation evaluations use the same random seed, and (2) in simulation, we sample 20 initial conditions from a 2cm-by-2cm box of the the real ( _x, y_ ) initial condition, execute the policy for each, and average the results to obtain a more robust estimate of the simulation counterpart. These measures are designed to mitigate the real-simulation gap without requiring additional real evaluations. 

### **5.1 Real2Sim Robot Experiments** 

**Diffusion Policy.** First, we evaluate a single-task diffusion policy on a distribution of various types of pick objects. For each real object _Xi_ , we get the real label _Yi_ by taking the average of partial scores of trials conducted at 5 initial conditions shown in Figure 3a. The paired evaluation score _f_ ( _X_<sup>˜</sup> _i_ ) is the average of simulation partial scores averaged over 100 simulation initial conditions corresponding to the 5 real-world initial conditions. On average, the correlation on the paired dataset is 0.72. For the additional simulation objects, we choose the Objaverse split of RoboCASA ob- **Figure 4** Evaluating Diffusion Policy with _n_ = 60 paired trials and up jects. For the following results, we use to 700 additional simulations. 100 random samples<sup>2</sup> of _n_ = 60 paired evaluations and up to _N_ = 700 additional evaluations. For the **SureSim (2-Stage)** family, the rectifier significance level is set to _δ_ = 90% of the the total significance level. All methods are given a significance level of _α_ = 0 _._ 1. 

Figure 4 illustrates the size of confidence interval widths as we scale-up simulation. At just 100 additional simulations, **SureSim** tightens the confidence interval with respect to **Classical** as simulation is scaled up further. In cases where the confidence interval is not truncated at 0 or 1, the rectifier interval width corresponds to a lower bound on the confidence interval width as the number of additional simulations increase. Here, the rectifier interval width is computed from finite-sample confidence intervals for the rectifier at _δ_ = 0 _._ 09 level of significance, and is determined by the rectifier variance. **SureSim** and **SureSim** - **UB** in Figure 4 approach this lower bound 



<!-- Start of picture text -->
Diffusion Policy (N=700) π 0 : Moderate Correlation (N=2100)<br>SureSim   SureSim-UB<br>SureSim SureSim-UB<br>(2-Stage) (2-Stage)<br><!-- End of picture text -->

**Figure 5** Average number of hardware trials saved compared to **Classical** , computed over 100 random draws of data. Error bars indicate standard error of the mean savings. 

relatively quickly, indicating efficient usage in incorporating simulation data up to the limit imposed by the real-simulation gap. At _N_ = 700, the mean interval width of **SureSim** is 0 _._ 16 which is a decrease of 14 _._ 4% compared to the interval width of length 0 _._ 187 for the **Classical** method. The **SureSim (2-Stage)** 

> 2In practice, this amounts to 100 random re-samplings of 60 objects (without replacement) from the bank of 120 real objects. 

8 

family has a slower decrease in interval width with scaling simulations as compared to **SureSim** family due to: i) the two-stage procedure introducing inefficiencies in separately computing confidence intervals for the rectifier and additional simulations, and ii) the significance level allocated to the simulation confidence interval ( _α − δ_ = 0 _._ 01), requiring further simulation trials. 

We study the advantage of our methods over hardware-only evaluations as follows. For each method, we compute a confidence interval at _n_ = 60 samples, and iteratively search over the number of samples _n_ given to **Classical** until the resulting confidence interval is tighter than the method’s interval. Figure 5 illustrates the resulting savings, where the **SureSim** method family yields over 25% savings with respect to real-only evaluation. 



**Figure 6 How does interval width decrease with scaling simulations under moderate correlation?** This figure reports results for _π_ 0 evaluated on initial conditions _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ for _n_ = 60 paired trials and over 2100 additional simulations. 

**Finetuned** _π_ 0 **.** We present two examples of evaluating _π_ 0, where we consider a joint distribution over objects and initial conditions. In the first case, an object is randomly selected and placed at an initial condition sampled from _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ , as shown in Figure 3b. In the second case, the initial condition is sampled from _{_ 1 _,_ 2 _,_ 3 _}_ . The former setting yields a moderate real-to-sim correlation, whereas the latter produces a low correlation. We present both cases to evaluate our methods under contrasting real-simulation correlation regimes. The real evaluation label for a specific object and initial condition is recorded according to the partial score metric, and the paired simulation records the average of simulation partial scores on the perturbed set of initial conditions corresponding to the real initial condition. 

_Moderate Correlation._ In Figure 6, we report average interval widths. Confidence intervals will vary in width and location for different draws of data from the same distribution; we illustrate one representative confidence interval in Figure 6. The real-simulation Pearson correlation _ρ_ is 0 _._ 59 on average on the paired evaluation set. The number of additional simulations is sufficient for the **SureSim** family to approach the rectifier lower bound and result in an advantage over **Classical** . Further scaling up simulation would address the two-stage inefficiency in the **SureSim (2-Stage)** family. However, the **SureSim** family converges by _N_ = 500 additional simulations, indicating efficiency with scaling simulations compared to the **SureSim** 



**Figure 7** Evaluating _π_ 0 at _n_ = 60 and scaling simulations up to _N_ = 50000. 

9 

**(2-Stage)** family. As seen in Figure 5, this leads to over a 20% decrease in real trials on average. In future work, we study further improvements to these finite-sample results by fine-tuning simulation. 

Although our object repository is limited to approximately 2100 objects, we conduct a sanity check in Figure 7 by sampling additional simulations with replacement, up to _N_ = 50 _,_ 000. While the rectifier interval width is limited by the difference in the real and simulation outcomes ( _Yi − f_ ( _X_<sup>˜</sup> _i_ )) on a small number of evaluations, additional simulation evaluations can be scaled up in the two-stage methods to reduce interval width. We observe that **SureSim (2-Stage)** progressively approaches the rectifier lower bound as the number of simulations increases. **SureSim** and **SureSim** - **UB** more efficiently converge to the rectifier lower bound within 5000 additional simulations, illustrating an upper bound on the benefit that additional simulation can provide given the real–simulation gap. 

_Low Correlation._ In Figure 8, we present results for a low correlation case, where initial conditions are sampled from _{_ 1 _,_ 2 _,_ 3 _}_ shown in Figure 3b. Empirically, the finetuned _π_ 0 demonstrates strong generalization to diverse object types despite being finetuned on only 7 objects. The initial conditions _{_ 1 _,_ 2 _,_ 3 _}_ achieve higher success rates across object types compared to initial condition 4. While these initial conditions are correspondingly easy and difficult in simulation, the predictive signal from simulation is insufficient to capture subtle variations in real-world performance, resulting in a low correlation of around _−_ 0 _._ 05. 

This results in qualitatively different behavior. As seen in Figure 8, none of our methods beat **Classical** . This is unsurprising because the there is nothing to infer about real policy performance from simulation. In particular, as listed in Table 1, the sample variance on real data is smaller than the sample rectifier variance. As a result, scaling up simulation does not help in reducing the variance in our estimates of the true mean (Equations (1) and (3)). 



**Figure 8 How does interval width decrease with scaling simulations under low correlation?** _π_ 0 evaluated on initial conditions _{_ 1 _,_ 2 _,_ 3 _}_ at _n_ = 60. _Left_ : There is no decrease in interval width with scaling simulations, which is expected given the low correlation between paired real and simulation trials. Due to truncation, the interval widths are smaller than the rectifier interval width (which do not truncate here). 

Across all Real2Sim experiments with moderate correlation, we observe that **SureSim** yields the greatest savings in terms of hardware trials saved and reduction in interval width. **SureSim** converges relatively quickly in the number of additional simulations in comparison to the two-stage methods. Furthermore, as we scale the number of simulations, the confidence intervals from our methods do not shrink to arbitrarily small widths. This controlled behavior is desirable, as it prevents overconfidence and ensures robust estimation of the mean. The gain from large-scale simulation depends on the correlation between paired real and simulated evaluations, which determines the rectifier variance. As shown in the asymptotic setting [17], combining real and simulated data is effective only when the rectifier variance is smaller than the variance of real evaluations—a condition that remains necessary in the non-asymptotic regime before committing substantial effort to large-scale simulation. Table 1 in Section A summarizes key experimental parameters as well as the sample correlation, means, and variances for each of the experiments. 

10 



**Figure 9** Prediction-powered inference for _n_ = 100 paired trials with up to 2000 additional simulations. Our methods always beat the classical baseline irrespective of increasing confidence levels. 

### **5.2 Sim2Sim Experiments** 

To illustrate coverage rate of confidence intervals, we run simulation-simulation experiments where we use a larger number of simulation evaluations as heldout samples to compute the “true” mean and validate coverage. As illustrated in Figure 10, we use one simulator setting as the “real” environment and the other as “simulation”. We evaluate finetuned _π_ 0 on 3D object models of real **(a)** [0 _,_ 6 _,_ 6] **(b)** [0 _,_ 3 _,_ 2] objects (Figure 2) as well RoboCASA. Once again, we consider a joint distribution over objects and initial con- **Figure 10** Sim2Sim setup with lighting parameters ditions _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ , and evaluate each trial according to for “real” (left) and “sim” (right) settings. the simulation partial score metric. The paired evaluation set has a very high correlation of around 0 _._ 97. We use 400 randomly drawn environments as heldout samples for validating coverage. 

For these experiments, we also report intervals for the **Control Variate** method, including the standard implementation presented in [50] as well as a data split version for an unbiased variance estimate. For data splitting, we use 20% of the paired data for variance estimation and the remaining for inference. As shown in Figure 9, at _α_ = 0 _._ 1, all methods beat **Classical** , with the **SureSim** family efficiently converging to the rectifier interval width. As the significance level decreases, **Control Variate** no longer beats **Classical** while **SureSim** always improves. 

Based on the prior discussion on the **Control Variate** method, we do not expect it to meet 



**Figure 11** Validating coverage using 400 heldout samples. 

the required coverage rate, and as seen in Figure 11, our experiments suggest that the empirical coverage rate can degrade with additional simulation samples. This degradation is cause for caution when interpreting the tightness of interval widths at _α_ = 0 _._ 1 in Figure 10, which highlights the importance of controlling for Type-1 

11 

error. Further rigorous validation of coverage on synthetic data is presented in Section D<sup>3</sup> . 

## **6 Conclusions** 

We introduce **SureSim** for augmenting large-scale simulation with a relatively smaller number of real-world evaluations to provide non-asymptotically valid inferences on real-world policy performance. With a real2sim formalism, we can characterize the problem of combining real and simulation evaluations as a predictionpowered inference problem, and leverage finite-sample valid mean estimation algorithms. This pipeline allows us to evaluate the generalization capabilities of robot foundation models such as diffusion policy and _π_ 0. Compared to hardware-only evaluation, our method saves over 20 _−_ 25% of hardware evaluations on average. 

## **7 Limitations and Future Work** 

While we introduce a non-asymptotically valid policy evaluation framework that allows us to rigorously combine real and simulation evaluations, the simulation-real gap poses a challenge to the effectiveness of large-scale simulation. We list a few exciting directions for future work. 

**Correlation between Simulation and Real.** Correcting for the bias in large-scale simulation with respect to the real-world in a statistically rigorous manner requires a paired dataset of simulation and real evaluations. The simulation–real gap also poses challenges for paired evaluations in the following ways. First, reliably predicting the real evaluation outcome for a specific initial condition is extremely challenging, as also elaborated in [16]. Secondly, real-world evaluations can be noisy — repeated trials from the same initial condition can produce different outcomes due to inherent stochasticity and policy sensitivity to hard-to-control perturbations (e.g., lighting or object placement). Reducing this simulation-reality gap for evaluation along various axes of generalization (e.g., spatial, environmental factors, task) remains an important direction of future work. Additionally, data efficient methods of fine-tuning simulation evaluations to improve real-simulation correlation can be valuable. 

**Action-conditioned video models.** Setting up physics-based simulations demands substantial effort and is difficult to scale or adapt to new environments and tasks. An appealing alternative is action-conditioned video world models, which can rapidly generate simulation scenes from text and image prompts [11]. As these models improve, it would be valuable to empirically assess the correlation in paired policy evaluations from world models. 

**Actively sampling real environments for evaluation.** Our current framework uses random batch sampling of real environments for mean estimation. A promising extension would be to develop active sampling schemes that prioritize real evaluations in regions with larger real–simulation gaps. 

Finally, just as large-scale datasets [55, 56] have been pivotal for training robot foundation models, scaling evaluation will similarly require further investment in repositories of diverse manipulation tasks and environments [36, 54], as well as scalable real2sim pipelines. 

## **8 Acknowledgments** 

The authors would like to thank Tijana Zrnic, Anastasios Angelopoulos, and Allen Z. Ren for insightful discussions. The authors were partially supported by the NSF CAREER Award #2044149, the Office of Naval Research (N00014-23-1-2148), and the Sloan Fellowship. A. Badithela is supported by the Presidential Postdoctoral Research Fellowship at Princeton University. 

> 3At 400 heldout samples used to characterize the “true” mean, we can still expect some variance in the computed mean. For a very rigorous validation of coverage, we would need to use synthetic data. 

12 

## **References** 

- [1] H. Kress-Gazit, K. Hashimoto, N. Kuppuswamy, P. Shah, P. Horgan, G. Richardson, S. Feng, and B. Burchfiel, “Robot learning as an empirical science: Best practices for policy evaluation,” _arXiv preprint arXiv:2409.09491_ , 2024. 

- [2] J. Gao, S. Belkhale, S. Dasari, A. Balakrishna, D. Shah, and D. Sadigh, “A taxonomy for evaluating generalist robot policies,” _arXiv preprint arXiv:2503.01238_ , 2025. 

- [3] J. Barreiros, A. Beaulieu, A. Bhat, R. Cory, E. Cousineau, H. Dai, C.-H. Fang, K. Hashimoto, M. Z. Irshad, M. Itkina, _et al._ , “A careful examination of large behavior models for multitask dexterous manipulation,” _arXiv preprint arXiv:2507.05331_ , 2025. 

- [4] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “Imagenet: A large-scale hierarchical image database,” in _2009 IEEE conference on computer vision and pattern recognition_ , pp. 248–255, Ieee, 2009. 

- [5] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Doll´ar, and C. L. Zitnick, “Microsoft coco: Common objects in context,” in _European conference on computer vision_ , pp. 740–755, Springer, 2014. 

- [6] P. Rajpurkar, J. Zhang, K. Lopyrev, and P. Liang, “Squad: 100,000+ questions for machine comprehension of text,” _arXiv preprint arXiv:1606.05250_ , 2016. 

- [7] A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman, “Glue: A multi-task benchmark and analysis platform for natural language understanding,” _arXiv preprint arXiv:1804.07461_ , 2018. 

- [8] A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill, O. Levy, and S. Bowman, “Superglue: A stickier benchmark for general-purpose language understanding systems,” _Advances in Neural Information Processing Systems_ , vol. 32, 2019. 

- [9] D. Snyder, A. J. Hancock, A. Badithela, E. Dixon, P. Miller, R. A. Ambrus, A. Majumdar, M. Itkina, and H. Nishimura, “Is your imitation learning policy better than mine? policy comparison with near-optimal stopping,” _arXiv preprint arXiv:2503.10966_ , 2025. 

- [10] S. Tao, F. Xiang, A. Shukla, Y. Qin, X. Hinrichsen, X. Yuan, C. Bao, X. Lin, Y. Liu, T. kai Chan, Y. Gao, X. Li, T. Mu, N. Xiao, A. Gurha, Z. Huang, R. Calandra, R. Chen, S. Luo, and H. Su, “Maniskill3: Gpu parallelized robotics simulation and rendering for generalizable embodied ai,” _arXiv preprint arXiv:2410.00425_ , 2024. 

- [11] J. Jang, S. Ye, Z. Lin, J. Xiang, J. Bjorck, Y. Fang, F. Hu, S. Huang, K. Kundalia, Y.-C. Lin, _et al._ , “Dreamgen: Unlocking generalization in robot learning through neural trajectories,” _arXiv e-prints_ , pp. arXiv–2505, 2025. 

- [12] J. Quevedo, P. Liang, and S. Yang, “Evaluating robot policies in a world model,” _arXiv preprint arXiv:2506.00613_ , 2025. 

- [13] X. Li, K. Hsu, J. Gu, K. Pertsch, O. Mees, H. R. Walke, C. Fu, I. Lunawat, I. Sieh, S. Kirmani, _et al._ , “Evaluating real-world robot manipulation policies in simulation,” _arXiv preprint arXiv:2405.05941_ , 2024. 

- [14] X. W. M. Team, “1x world model: Evaluating bits, not atoms,” tech. rep., 1X, 2025. 

- [15] Z. Zhou, P. Atreya, Y. L. Tan, K. Pertsch, and S. Levine, “Autoeval: Autonomous evaluation of generalist robot manipulation policies in the real world,” _arXiv preprint arXiv:2503.24278_ , 2025. 

- [16] N. Pfaff, E. Fu, J. Binagia, P. Isola, and R. Tedrake, “Scalable real2sim: Physics-aware asset generation via robotic pick-and-place setups,” _arXiv preprint arXiv:2503.00370_ , 2025. 

- [17] A. N. Angelopoulos, S. Bates, C. Fannjiang, M. I. Jordan, and T. Zrnic, “Prediction-powered inference,” _Science_ , vol. 382, no. 6671, pp. 669–674, 2023. 

- [18] A. N. Angelopoulos, J. C. Duchi, and T. Zrnic, “PPI++: Efficient prediction-powered inference,” _arXiv preprint arXiv:2311.01453_ , 2023. 

- [19] C. Chi, Z. Xu, S. Feng, E. Cousineau, Y. Du, B. Burchfiel, R. Tedrake, and S. Song, “Diffusion policy: Visuomotor policy learning via action diffusion,” _The International Journal of Robotics Research_ , p. 02783649241273668, 2023. 

- [20] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, _et al._ , “ _π_ 0: A vision-language-action flow model for general robot control,” in _Robotics: Science and Systems_ , 2025. 

- [21] M. Heo, Y. Lee, D. Lee, and J. J. Lim, “Furniturebench: Reproducible real-world benchmark for long-horizon complex manipulation,” in _Robotics: Science and Systems_ , 2023. 

13 

- [22] J. Luo, C. Xu, F. Liu, L. Tan, Z. Lin, J. Wu, P. Abbeel, and S. Levine, “Fmb: a functional manipulation benchmark for generalizable robotic learning,” _The International Journal of Robotics Research_ , vol. 44, no. 4, pp. 592–606, 2025. 

- [23] B. Yang, D. Jayaraman, J. Zhang, and S. Levine, “Replab: A reproducible low-cost arm benchmark for robotic learning,” in _2019 International Conference on Robotics and Automation (ICRA)_ , pp. 8691–8697, IEEE, 2019. 

- [24] N. Khargonkar, S. H. Allu, Y. Lu, B. Prabhakaran, Y. Xiang, _et al._ , “Scenereplica: Benchmarking real-world robot manipulation by creating replicable scenes,” in _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 8258–8264, IEEE, 2024. 

- [25] J. Collins, M. Robson, J. Yamada, M. Sridharan, K. Janik, and I. Posner, “Ramp: A benchmark for evaluating robotic assembly manipulation and planning,” _IEEE Robotics and Automation Letters_ , vol. 9, no. 1, pp. 9–16, 2023. 

- [26] D. Pickem, P. Glotfelter, L. Wang, M. Mote, A. Ames, E. Feron, and M. Egerstedt, “The robotarium: A remotely accessible swarm robotics research testbed,” in _2017 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 1699–1706, IEEE, 2017. 

- [27] G. Zhou, V. Dean, M. K. Srirama, A. Rajeswaran, J. Pari, K. Hatch, A. Jain, T. Yu, P. Abbeel, L. Pinto, _et al._ , “Train offline, test online: A real robot learning benchmark,” _arXiv preprint arXiv:2306.00942_ , 2023. 

- [28] Z. Liu, W. Liu, Y. Qin, F. Xiang, M. Gou, S. Xin, M. A. Roa, B. Calli, H. Su, Y. Sun, _et al._ , “Ocrtoc: A cloud-based competition and benchmark for robotic grasping and manipulation,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 1, pp. 486–493, 2021. 

- [29] S. Bauer, M. W¨uthrich, F. Widmaier, A. Buchholz, S. Stark, A. Goyal, T. Steinbrenner, J. Akpo, S. Joshi, V. Berenz, _et al._ , “Real robot challenge: A robotics competition in the cloud,” in _NeurIPS 2021 Competitions and Demonstrations Track_ , pp. 190–204, PMLR, 2022. 

- [30] P. Atreya, K. Pertsch, T. Lee, M. J. Kim, A. Jain, A. Kuramshin, C. Eppner, C. Neary, E. Hu, F. Ramos, _et al._ , “Roboarena: Distributed real-world evaluation of generalist robot policies,” _arXiv preprint arXiv:2506.18123_ , 2025. 

- [31] A. Khazatsky, K. Pertsch, S. Nair, A. Balakrishna, S. Dasari, S. Karamcheti, S. Nasiriany, M. K. Srirama, L. Y. Chen, K. Ellis, _et al._ , “Droid: A large-scale in-the-wild robot manipulation dataset,” _arXiv preprint arXiv:2403.12945_ , 2024. 

- [32] E. Todorov, T. Erez, and Y. Tassa, “Mujoco: A physics engine for model-based control,” in _2012 IEEE/RSJ international conference on intelligent robots and systems_ , pp. 5026–5033, IEEE, 2012. 

- [33] Y. Tassa, Y. Doron, A. Muldal, T. Erez, Y. Li, D. d. L. Casas, D. Budden, A. Abdolmaleki, J. Merel, A. Lefrancq, _et al._ , “Deepmind control suite,” _arXiv preprint arXiv:1801.00690_ , 2018. 

- [34] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, _et al._ , “Isaac gym: High performance gpu-based physics simulation for robot learning,” _arXiv preprint arXiv:2108.10470_ , 2021. 

- [35] Y. Zhu, J. Wong, A. Mandlekar, R. Mart´ın-Mart´ın, A. Joshi, S. Nasiriany, and Y. Zhu, “robosuite: A modular simulation framework and benchmark for robot learning,” _arXiv preprint arXiv:2009.12293_ , 2020. 

- [36] S. Nasiriany, A. Maddukuri, L. Zhang, A. Parikh, A. Lo, A. Joshi, A. Mandlekar, and Y. Zhu, “Robocasa: Large-scale simulation of everyday tasks for generalist robots,” _arXiv preprint arXiv:2406.02523_ , 2024. 

- [37] S. James, Z. Ma, D. R. Arrojo, and A. J. Davison, “Rlbench: The robot learning benchmark & learning environment,” _IEEE Robotics and Automation Letters_ , vol. 5, no. 2, pp. 3019–3026, 2020. 

- [38] W. Pumacay, I. Singh, J. Duan, R. Krishna, J. Thomason, and D. Fox, “The colosseum: A benchmark for evaluating generalization for robotic manipulation,” _arXiv preprint arXiv:2402.08191_ , 2024. 

- [39] K. Zheng, X. Chen, O. C. Jenkins, and X. Wang, “Vlmbench: A compositional benchmark for vision-and-language manipulation,” _Advances in Neural Information Processing Systems_ , vol. 35, pp. 665–678, 2022. 

- [40] O. Mees, L. Hermann, E. Rosete-Beas, and W. Burgard, “Calvin: A benchmark for language-conditioned policy learning for long-horizon robot manipulation tasks,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 3, pp. 7327–7334, 2022. 

- [41] M. Yang, Y. Du, K. Ghasemipour, J. Tompson, D. Schuurmans, and P. Abbeel, “Learning interactive real-world simulators,” _arXiv preprint arXiv:2310.06114_ , vol. 1, no. 2, p. 6, 2023. 

14 

- [42] T. Brooks, B. Peebles, C. Holmes, W. DePue, Y. Guo, L. Jing, D. Schnurr, J. Taylor, T. Luhman, E. Luhman, _et al._ , “Video generation models as world simulators,” _OpenAI Blog_ , vol. 1, no. 8, p. 1, 2024. 

- [43] N. Agarwal, A. Ali, M. Bala, Y. Balaji, E. Barker, T. Cai, P. Chattopadhyay, Y. Chen, Y. Cui, Y. Ding, _et al._ , “Cosmos world foundation model platform for physical ai,” _arXiv preprint arXiv:2501.03575_ , 2025. 

- [44] A. Kadian, J. Truong, A. Gokaslan, A. Clegg, E. Wijmans, S. Lee, M. Savva, S. Chernova, and D. Batra, “Sim2real predictivity: Does evaluation in simulation predict real-world performance?,” _IEEE Robotics and Automation Letters_ , vol. 5, no. 4, pp. 6670–6677, 2020. 

- [45] A. Majumdar, M. Sharma, D. Kalashnikov, S. Singh, P. Sermanet, and V. Sindhwani, “Predictive red teaming: Breaking policies without breaking robots,” _arXiv preprint arXiv:2502.06575_ , 2025. 

- [46] M. O’Kelly, A. Sinha, H. Namkoong, R. Tedrake, and J. Duchi, “Scalable end-to-end autonomous vehicle testing via rare-event simulation,” _Advances in Neural Information Processing Systems_ , vol. 31, 2018. 

- [47] J. A. Vincent, H. Nishimura, M. Itkina, P. Shah, M. Schwager, and T. Kollar, “How generalizable is my behavior cloning policy? a statistical approach to trustworthy performance evaluation,” _IEEE Robotics and Automation Letters_ , 2024. 

- [48] W. Hoeffding, “Probability inequalities for sums of bounded random variables,” _Journal of the American statistical association_ , vol. 58, no. 301, pp. 13–30, 1963. 

- [49] A. Mandyam, J. Meng, G. Gao, J. Sun, M. Schwager, B. E. Engelhardt, and E. Brunskill, “Perry: Policy evaluation with confidence intervals using auxiliary data,” _arXiv preprint arXiv:2507.20068_ , 2025. 

- [50] R. Luo, H. Yang, M. Watson, A. Sharma, S. Veer, E. Schmerling, and M. Pavone, “Leveraging correlation across test platforms for variance-reduced metric estimation,” _arXiv preprint arXiv:2506.20553_ , 2025. 

- [51] I. Waudby-Smith and A. Ramdas, “Estimating means of bounded random variables by betting,” _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , vol. 86, no. 1, pp. 1–27, 2024. 

- [52] T. Zrnic and E. Candes, “Active statistical inference,” in _International Conference on Machine Learning_ , pp. 62993– 63010, PMLR, 2024. 

- [53] M. Deitke, D. Schwenk, J. Salvador, L. Weihs, O. Michel, E. VanderBilt, L. Schmidt, K. Ehsani, A. Kembhavi, and A. Farhadi, “Objaverse: A universe of annotated 3d objects,” in _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pp. 13142–13153, 2023. 

- [54] B. Calli, A. Singh, J. Bruce, A. Walsman, K. Konolige, S. Srinivasa, P. Abbeel, and A. M. Dollar, “Yale-cmuberkeley dataset for robotic manipulation research,” _The International Journal of Robotics Research_ , vol. 36, no. 3, pp. 261–268, 2017. 

- [55] H. R. Walke, K. Black, T. Z. Zhao, Q. Vuong, C. Zheng, P. Hansen-Estruch, A. W. He, V. Myers, M. J. Kim, M. Du, _et al._ , “Bridgedata v2: A dataset for robot learning at scale,” in _Conference on Robot Learning_ , pp. 1723–1736, PMLR, 2023. 

- [56] “Open X-Embodiment: Robotic learning datasets and RT-X models.” `https://arxiv.org/abs/2310.08864` , 2023. 

- [57] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” 2015. 

15 

# Appendix 

## **A Summary Statistics from Experiments** 

|Experiment|_n_|_N_|_ρ_|1<br>_n_<br>�_n_<br>_i_=1 <sup>_Yi_</sup>|1<br>_n_<br>�_n_<br>_i_=1 <sup>_f_( ˜</sup><br>_Xi_)|1<br>_N_<br>�_N_<br>_i_=1 <sup>_f_( ˜</sup><br>_Xi_)|ˆ_σ_<sup>2</sup><br>_Y_|ˆ_σ_<sup>2</sup><br>_Y −f_|
|---|---|---|---|---|---|---|---|---|
|Diffusion Policy (Real2Sim)|60|700|0.702|0.246|0.188|0.174|0.104|0.054|
|_π_0 (Real2Sim, moderate _ρ_)|60|2100|0.588|0.825|0.820|0.772|0.138|0.090|
|_π_0 (Real2Sim, low _ρ_)|60|2100|-0.051|0.983|0.932|0.928|0.014|0.029|
|_π_0 (Sim2Sim, high _ρ_)|100|2000|0.974|0.751|0.731|0.732|0.116|0.006|



**Table 1** Summary statistics indicating the number of paired trials _n_ , additional simulation evaluations _N_ , Pearson correlation coefficient _ρ_ , sample real mean _n_<sup><u>1</u></sup> � _ni_ =1<sup>_Yi_,samplepairedsimulationmean</sup> _n_<sup><u>1</u></sup> � _ni_ =1<sup>_f_(</sup> _X_<sup>˜</sup> _i_ ), sample additional simulation mean _N_ <u>1</u> � _Ni_ =1<sup>_f_(</sup> _X_<sup>˜</sup> _i_ ), the sample real variance _σ_ ˆ _Y_<sup>2,andthesamplerectifiervariance</sup><sup>_σ_ˆ</sup> _Y_<sup>2</sup> _−f_<sup>.Thereported</sup> statistics are averaged over 100 draws of data. 

## **B Algorithms** 

**Algorithm 2:** Uniform Prediction Powered Inference <u>(UniformPPI)</u> 

**Input:** Paired dataset _D_ paired, Simulation dataset _D_ sim, Sim outcomes _f_ , counts _n, N_ , significance level _α_ **Output:** Confidence interval _CI_ **for** _i ←_ 1 **to** _n_ + _N_ **do** _ξi_ = 1 if _Xi_ has a real evaluation, else _ξi_ = 0 ∆ _i_ = _f_ ( _X_<sup>˜</sup> _i_ ) +<sup>_<u>n</u>_</sup><sup><u>+</u></sup> _n_<sup>_<u>N</u>_(</sup><sup>_Yi −f_( ˜</sup><sup>_Xi_))</sup><sup>_· ξi_</sup> **end** _D_ unif = _{_ ∆ _i}_<sup>_n_</sup> _i_ =1<sup>+</sup><sup>_N_</sup> `// Problem Data` _CI ←_ WSR( _D_ unif _, α_ = _α, L_ = _−_<sup>_<u>n</u>_</sup><sup><u>+</u></sup> _n_<sup>_<u>N</u>, U_= 1 +</sup><sup>_<u>n</u>_</sup><sup><u>+</u></sup> _n_<sup>_<u>N</u>_)</sup> `// Single call to WSR` **<u>return</u>** _<u>CI</u>_ 

**Algorithm 3:** Two-Stage Prediction Powered Inference <u>(2-StagePPI)</u> 

**Input:** Paired dataset _D_ paired, Simulation dataset _D_ sim, levels _α, δ_ **Output:** Confidence interval _CI_ ( _fl, fu_ ) _←_ WSR( _D_ sim _, α_ = _δ, L_ = 0 _, U_ = 1) `// Additional Simulation Confidence Interval` **for** _i ←_ 1 **to** _n_ **do** ∆ _i_ = _Yi − f_ ( _X_<sup>˜</sup> _i_ ) **end** ( _Rl, Ru_ ) _←_ WSR( _{_ ∆ _i}_<sup>_n_</sup> _i_ =1<sup>_,α_=</sup><sup>_α −δ, L_=</sup><sup>_−_1</sup><sup>_, U_= 1)</sup> `// Rectifier Confidence Interval` _CI ←_ ( _fl − Ru, fu − Rl_ ) `// Union bound` **<u>return</u>** _<u>CI</u>_ 

16 

**Algorithm 4:** Non-asymptotic mean estimation via Waudby-Smith Ramdas <u>(WSR)</u> Procedure <u>[17,</u> 51] 

**Data:** Data points _{Z_ 1 _, . . . , Zn}_ , error level _α ∈_ (0 _,_ 1), range [ _L, U_ ] such that _Zi ∈_ [ _L, U_ ]. **Result:** Confidence interval _CI_ for the mean **for** _i ←_ 1 **to** _n_ **do** _Zi ←_ ( _Zi − L_ ) _/_ ( _U − L_ ) `// Normalize to` [0 _,_ 1] **end** Construct fine grid _M_ grid over [0 _,_ 1] Initialize set of candidate means _A ← M_ grid **for** _t ←_ 1 **to** _n_ **do** 0 _._ 5 +<sup><u>�</u></sup><sup>_t_</sup> _<u>j</u>_ =1<sup>_Zj_</sup> _µ_ ˆ _t ← t_ + 1 0 _._ 25 +<sup><u>�</u></sup><sup>_t_</sup> _<u>j</u>_ =1<sup>(</sup><sup>_Zj−µ_ˆ</sup><sup>_t_)2</sup> _σ_ ˆ _t_<sup>2</sup><sup>_←_</sup> _<u>t</u>_ <u>+ 1</u> 2 log(2 _<u>/α</u>_ <u>)</u> _λt ←_ � _nσ_ ˆ _t_<sup>2</sup> _−_ 1 **for** _m ∈ M_ grid **do** _▷_ In computing the martingales, we choose the hyperparameter _c_ = 0 _._ 99 due to its empirical performance _Mt_<sup>+(</sup><sup>_m_)</sup><sup>_←_</sup> �1 + min� _λt, m_<sup>_<u>c</u>_</sup> �( _Zt − m_ )� _Mt_<sup>+</sup> _−_ 1<sup>(</sup><sup>_m_)</sup> _Mt_<sup>_−_(</sup><sup>_m_)</sup><sup>_←_</sup> <u>�1</u> _−_ min� _λt,_ 1 _−cm_ �( _Zt − m_ )� _Mt_<sup>_−_</sup> _−_ 1<sup>(</sup><sup>_m_)</sup> _Mt_ ( _m_ ) _←_ 2<sup><u>1</u>max</sup><sup>_{M_+</sup> _t_<sup>(</sup><sup>_m_)</sup><sup>_, M_</sup> _t_<sup>_−_(</sup><sup>_m_)</sup><sup>_}_</sup> `// Martingale` **if** _Mt_ ( _m_ ) _≥_ 1 _/α_ **then** _A ←A \ {m}_ `// Remove` _m_ `from set of candidate means` **end end** 

**end** 

_Cα_ = _{m_ ( _U − L_ ) + _L_ : _m ∈A}_ `// True mean lies in this set with high probability` _CI_ = [max _{_ 0 _,_ min _Cα},_ min _{_ 1 _,_ max _Cα}_ ] **<u>return</u>** _<u>CI</u>_ 

## **C Choosing the Confidence For Each Interval** 

The allocation of risk between the rectifier and simulator intervals can be approximately optimized in an efficient manner. The sub-Gaussian nature of the respective means ensures that the interval growth rate with respect to increasing confidence is monotonic and increasing. Thus, there is an approximate equilibrium that can be found via binary search, in which the rate of width increase in the rectifier (resp., simulator) is precisely offset by the rate of interval shrinkage in the simulator (resp., rectifier). On either “side” of this equilibrium, the rate of growth of one of the intervals outpaces the rate of shrinkage of the other, making the landscape approximately convex. Generally speaking, the optimal allocation in practical situations has _δ ≈_ 0 _._ 9 _α_ . 

## **D Evaluation on Artificial Data** 

In order to investigate counterfactual properties of the evaluation methods, we test all method using artificial (simulated) data with known statistical properties. This is **not** data generated by a physics-based _robot simulator_ , but is rather simulated i.i.d. draws of _scalar random variables_ with known statistical properties. We term this data “artificial” in order to avoid any confusion with the the simulator predictions in Section 5. 

17 

### **D.1 Value of Artificial Data and Research Questions** 

Practical estimation problems arise precisely because the investigator does not have access to the true statistical parameter in question (in this case, the mean performance). Thus, when evaluating on real data as in Section 5, we cannot verify whether the confidence intervals we generate – or those generated by any baseline procedure – actually contain the true mean. As such, using artificial data allows for the important step of verifying the theoretical claims of each method in practice, so that they may profitably be used on such problems as may be encountered in, for example, the sciences and engineering. Furthermore, access to the “true parameter labels” for artificial data allow us to efficiently pose hundreds or even thousands of estimation problems reflective of varying contexts, which inform the reader as to the best method for their particular application. 

The core additional technical objection this must raise is the degree to which the simulated data fails to represent some data that may be observed by the practitioner; necessarily, it is impossible to sample from, and validate against, _all distributions_ – certainly in finite time. Addressing this problem will be crucial to effective characterization and evaluation. 

To the aforementioned ends, we provide the following core analyses via the evaluations on artificial data: 

- A justification of the generality of our data generation process with respect to key parameters; 

- A discussion of the most informative metrics in evaluating estimation procedures; 

- An investigation of the effectiveness of all methods subject to variation in the key parameters; 

- A brief discussion and usage guide for the strengths of each method, and interpretable scenarios in which one should likely be preferred to the others. 

### **D.2 The Key Parameters and Data Generation** 

As introduced in Section 3, the robot evaluation problem tackled here is a special case of a more general mean estimation problem in statistics. The canonical Neyman-Pearson framework for understanding these estimation problems relies on several key parameters: the batch size ( _n_ ) and the significance level ( _α_ ). As introduced in Section 4, we are interested in using the information contained in proxy signals (e.g., simulators) to effectively increase the sample size of real evaluations. Thus, this procedure _also depends_ on the amount of proxy data ( _N_ ) and the degree to which the simulator is “useful” – informally, the amount of additional information contained in the proxy variables. 

This last piece of information is of course key to the investigation. We argue that, consistent with the analysis of control variates methods, the critical measure by which the proxy variable improves nonasymptotic (finite-sample) confidence interval generation is in the variance reduction of the (unbiased) mean estimator. Intuitively, such a reduction tightens the confidence intervals while ensuring Type-1 error control at all data scales. With this in mind, we use as the core “effectiveness measure” the Pearson correlation coefficient, _ρ_ , which is a direct ratio of the real-to-proxy covariance to their geometric mean variance. This intuition is reflected directly in the control variates analysis of [50], particularly with respect to their Theorem 1. 

Given the preceding discussion, we intend to investigate the relative advantages of each estimation procedure as a function of the four stated parameters: _α_ , _n_ , _N_ , and _ρ_ . To generate artificial data, we construct artificial real data of size _k_ ( _n_ + _N_ ) drawn uniformly in the interval [max _{_ 0 _,_ 2 _µ −_ 1 _},_ min _{_ 2 _µ,_ 1 _}_ ]. This enforces a tunable true population mean _µ_ while ensuring that the data is always bounded in [0 _,_ 1].<sup>4</sup> The proxy data requires a desired value _ρ_<sup>_∗_</sup> . To generate the artificial proxy data, the real data is copied, shifted to mean _µsim_ , and then iteratively perturbed by small amounts of random noise or small perfect-signal gradients in order to push the empirical correlation to _ρ_ . Matched and unmatched datasets of respective size _n_ and _N_ are drawn from partitions of the large dataset; for the unmatched data, the real labels are discarded for the purposes of running the algorithms. To save time, this single large dataset can be sampled from repeatedly (i.e., bootstrapped), or new datasets can be generated for each experiment. We opt for the latter, though it is more time-consuming in practice for empirically negligible effects. 

> 4To avoid unnecessary subtleties around the effects of interval truncation at 0 and 1 on the aggregate interval width metrics, we will in general set the means to be equal to 0 _._ 5. 

18 

**A Brief Discussion of Estimation Metrics** The “proper” metrics to report for the problem of mean estimation admits a wide array of context-relevant options. We argue for the metrics herein, and attempt to briefly justify the preference. 

**The Natural Option: Interval Widths** The ultimate purpose of estimation in our context is to minimize the region of uncertainty in which the true parameter lies (subject to a tunable risk of error); this is a dual result to many “operationalizable” uses, including tests of maximal efficiency and power, certification in the least number of trials, etc. As such, it is unsurprising that reporting interval width directly is the most natural metric, and is our primary metric of choice in this work. 

**A Caution About Variance Minimization** Another natural metric, albeit one slightly upstream of the intended methodological usage, is estimator variance. This analysis is interchangeable with the interval width (i.e., equivalent under monotonic transformations), but _only when the space of estimators is constrained to be unbiased_ . Unbiased estimators overwhelmingly dominate among methods used in practice, but analysis can be misleading when the constraint is not satisfied. A minimum-variance estimator is _essentially meaningless_ (for example, the estimator ‘5’ has no variance over the draw of the data); a minimum-variance _unbiased_ estimator, on the other hand, can be exceedingly novel and useful. 

**Dependence on Significance Level** Bounded random variables are a special case of random variables with bounded moments. These random variables are sub-Gaussian, and therefore any optimal interval widths (across data scales) should be able to attain poly-logarithmic dependence on the significance level. 

### **D.3 Results on Artificial Data** 

We illustrate the three aforementioned themes in evaluation over artificial data. All results will report interval widths as the primary metric (Theme 1), and will discuss the downside of additional metrics via the example cases. Second, the limitations of variance minimization will be illustrated (Theme 2), which will also inform our investigation of each method’s coverage (i.e., enforcing the Type-I error control constraint in Equation (1)). Finally, we will sketch the gap in efficiency with respect to confidence or significance level, which has implications for different types of validation settings encountered in practice. To be specific, we will discuss in particular the implications of statistical guarantees in safety-critical certification and evaluation paradigms. 

In order to avoid certain distracting or confounding phenomena, we present intervals for data with characteristics designed to highlight the fundamental behavior of the algorithms. Specifically: the real data and simulator data means are set arbitrarily to 0.5 each, in order to minimize instances of truncation of the intervals at 0 or 1. Truncation does not in general benefit any particular method, but it does increase variation in interval widths that can make the results noisier. As these results are purely designed to validate existential and not universal quantifications of algorithm behavior, this choice does not bias the result and discussion. 

**Interval Width as Simulator Data or Correlation Grows** We begin by validating the behavior of each algorithm seen in Section 5. The artificial data is iteratively redrawn for _n_ = 100 and varying levels of _N_ up to 10k additional simulation runs. We first consider a case of relative strength for **Control Variate** , taking a large correlation _ρ_ = 0 _._ 97 and varying _α_ across approximately two orders of magnitude. As shown in Figure 12, every method has near-monotonic improvement (in expectation) as the amount of additional sim data grows, reflecting the intuition that there must be more ‘information’ being given to the evaluator. However, the intervals do not asymptote to zero, indicating that, even so, there remains fundamental uncertainty in linking the sim data to the real data (the rectifier uncertainty) that is _irreduceable_ given a fixed amount of real data. In other words, we cannot trust the sim data to an arbitrary degree, but can still use the data productively to tighten the intervals. As shown in Figures 12 and 13, the **SureSim** family of methods recover the real-simulation gap determined by the number of paired trials _n_ . In contrast, the two-stage methods, **SureSim (2-Stage)** and **SureSim** - **UB (2-Stage)** , remain inefficient even at _N_ = 10000, requiring an even higher number of simulation evaluations to converge. 

In Figure 13, we generalize these results to variations across the true correlation between real data and simulation. Naturally, higher correlation implies greater signal in the proxy (simulation) data, and therefore more achievable tightening. This also validates the analysis of monotonic and quadratic **Control Variate** 

19 





<!-- Start of picture text -->
(a) Interval width vs ( N ): α  = 0 . 1, ρ  = 0 . 97<br>(c) Interval width vs ( N ): α  = 0 . 01, ρ  = 0 . 97<br><!-- End of picture text -->





<!-- Start of picture text -->
(b) Interval width vs ( N ): α  = 0 . 03, ρ  = 0 . 97<br><!-- End of picture text -->





<!-- Start of picture text -->
(d) Interval width vs ( N ): α  = 0 . 005, ρ  = 0 . 97<br><!-- End of picture text -->

**Figure 12** Interval widths on all methods for artificial data. Each plot shows the width against varying _N_ ( _n_ = 100). Results averaged over 100 independent redraws of data. The desired confidence level increases ( _α_ decreases) left-to-right, top-to-bottom. Note that **Control Variate** constructs tighter intervals at large _α_ , but that the interval widths are much more sensitive as _α_ changes. As will be shown in Figure 14, the biased nature of the CV estimator leads to miscoverage in regimes for which its intervals appear to be narrower. 

20 

interval width scaling given in [50]. Note that the numbers in Figure 12 correspond to nearly the right-most points of the curves in Figure 13.<sup>5</sup> Additionally, even if the 





<!-- Start of picture text -->
(a) Interval width vs ( ρ ); n  = 100, N = 5000, α  = 0 . 1<br><!-- End of picture text -->



**(c)** Interval width vs ( _ρ_ ); _n_ = 100, _N_ = 5000, _α_ = 0 _._ 01 





<!-- Start of picture text -->
(b) Interval width vs ( ρ ); n  = 100, N = 5000, α  = 0 . 05<br><!-- End of picture text -->



**(d)** Interval width vs ( _ρ_ ); _n_ = 100, _N_ = 5000, _α_ = 0 _._ 005 

**Figure 13** Interval widths versus true data correlation between real and paired data. As correlation increases, intervals narrow due to the greater amount of signal present. Results averaged over 100 independent redraws of data. As can be seen, **Control Variate** has greater sensitivity to the true correlation because of the direct correspondence of _ρ_ to the attainable rectifier variance. However, the construction comes at a significant cost in lower-correlation regimes, and again illustrates strong sensitivity to _α_ . Furthermore, as noted in Figure 14, cases of very high correlation often result in miscoverage using the standard control variates implementation with Chebyshev’s Inequality [50]. 

**Coverage as Simulator Data Grows** We now investigate the second thematic point, on the limitations of variance minimization as a certification for estimation efficiency. The first key comment pertains to the resulting interval coverage, to which we have access by virtue of constructing the artificial data and knowing its key features (including the mean). 

Variance minimization is generally synonymous with improving the estimator efficiency – i.e., shrinking the interval width – _but only so long as the intervals enforce validity_ . As shown in Figure 14, this is a challenge for **Control Variate** , because the technique is _not unbiased_ . Thus, it is susceptible to excessive optimism (“trusting the simulator too much”), which leads to miscoverage when the amount of simulator data grows. As shown, this effect is most pronounced precisely when **Control Variate** is relatively strongest (at larger _α_ ). Importantly, for practical problems, the evaluator cannot know whether they are in an excessively optimistic regime; this is precisely the reason for enforcing Equation (1) as a property of the evaluation procedure. As shown, such methods cover uniformly, while being generally efficient (recovering the rectifier variance) across different levels of _α_ and _ρ_ . **Interval Width versus Significance Level** Finally, we evaluate the effect of changes in significance level on the interval scaling. As the **SureSim** and **SureSim (2-Stage)** family of procedures apply WSR[51], which admits bounded (and therefore, sub-Gaussian) random variables, these methods can recover _O_ (log _α_<sup><u>1</u>)scalingas</sup><sup>_α →_0+.ThisisbroadlyindicativeofHoeffding-orBernstein-typeconcentration</sup> bounds. By contrast, **Control Variate** is slightly more general (not requiring boundedness), but loses this 

> 5This statement is modulo the small differences in _α_ for two of the plots, which differed in order to allow us to illustrate qualitatively different coverage behavior for **Control Variate** in Figure 14. 

21 







<!-- Start of picture text -->
(a) Coverage Rate vs ( N ): α  = 0 . 1, ρ  = 0 . 97 (b) Coverage Rate vs ( N ): α  = 0 . 03, ρ  = 0 . 97<br>(c) Coverage Rate vs ( N ): α  = 0 . 01, ρ  = 0 . 97 (d) Coverage Rate vs ( N ): α  = 0 . 005, ρ  = 0 . 97<br><!-- End of picture text -->

**Figure 14** Interval coverage rate on all methods for artificial data. Each plot shows the coverage rate against varying _N_ ( _n_ = 100). Results averaged over 100 independent redraws of data. The desired confidence level increases ( _α_ decreases) left-to-right, top-to-bottom. First, every provably nonasymptotically valid method covers in every regime, as expected. By contrast, note that **Control Variate** fails to cover in the top row as the amount of simulation data grows; this is a result of bias in the estimator causing inconsistency. Importantly: it is _precisely when_ **Control Variate** _intervals become narrower than our methods that they lose validity_ . Thus, the only valid instance of empirical improvement of **Control Variate** over our procedure on this data is in the case _α_ = 0 _._ 01; crucially, however, the practitioner cannot know for their problem whether they are in this regime (as for different problem instances, the critical value of _α_ will differ in general from 0 _._ 01). Thus, the practitioner may be in the (narrow) valid and efficient regime, or may be in the invalid (too-optimistic) regime, or in the inefficient regime – and will not be able to distinguish which one. 

scaling rate as a consequence. This explains the significantly increased sensitivity to _α_ (specifically, _O_ ( _~~√~~_<sup><u>1</u></sup> _<u>α</u>_<sup>)</sup> scaling) obtained via Chebyshev’s inequality. 

The tradeoffs of this design choice can be seen in several intuitive ways. First, naturally-unbounded metrics (e.g., log likelihoods) are more suited to **Control Variate** . However, from a practical standpoint, guarantees requiring very high confidence (often the best that statistical assurances can achieve for safety-critical applications) will scale much more efficiently with our methods; that is, **Control Variate** will very often yield vacuous intervals for, e.g., _α <_ 0 _._ 0001, especially when _n_ is constrained. The method can tighten this by instead using a Hoeffding-type bound, but then loses the generality that sets it apart from WSR-based procedures, as it must also enforce a boundedness constraint. 

### **D.4 Key Takeaways** 

A recurring theme of the methodological comparison given in the preceding sections is the relative strength of **Control Variate** procedures for (a) less stringent significance requirements (higher _α_ ), and (b) higher correlation _ρ_ . Intuitively, it is better able to exploit ‘easier’ settings to tighten intervals more aggressively, at the cost of underperforming (in terms of downstream interval width) in ‘harder’ ones, where greater confidence is required and the amount of signal in the proxy data is limited. However, in small _n_ settings, the optimistic 

22 

choice of the control variate coefficient can lead to miscoverage. 

## **E Implementation Details** 

**Hardware Setup** We use a Franka Panda robot for our real robot experiment. For all experiments, we use joint space control at 15Hz. We use Logitech C920 webcam as our third person camera, and RealSense D405 for the wrist camera. Both cameras use resolution 192 _×_ 192. We use a Meta Quest 2 VR headset for teleoperation to perform data collection. 

### **E.1 Policy Implementation Details** 

We implement Diffusion Policy [19] and _π_ 0 [20] for our two experiments respectively. Below we detail their implementations. 

**Diffusion Policy.** We follow the original implementations from **(author?)** [19], and use ResNet-18 [57] as our vision encoder. The policy takes in two images from the wrist camera and the third person camera, as well as the robot state. The robot state is an 8-dimensional vector comprising the seven joint positions and a single gripper binary state. Action output is specified as 8-dimensional target absolute joint-position and a target gripper state. We train the policy with 50000 gradient updates with a fixed batch size of 64. The training can be finished in approximately one wall-clock hour on a Nvidia L40 GPU. We augment the input images with standard color-jitter and random rotation during training. A complete list of hyper-parameters is provided in Table 2. 

**Table 2** Hyper-parameters of simulation diffusion policy. 

|Model Dimension|Dim Mults|Time Embedding Dimension|History Steps|Horizon|Action Steps|
|---|---|---|---|---|---|
|128|[1,2,4]|128|1|16|8|



**Multi-task** _π_ 0 **.** We fine-tune from _π_ 0-base model. Similar to Diffusion Policy, _π_ 0 takes in two images from the wrist camera and the third person camera, proprioception states, and additionally a task language instruction. The instruction is formatted as “Put _<_ object _>_ into the box”. We freeze the VLM and only train the action expert. We train all policies for 15,000 gradient steps with batch size 64. The training can be finished in 8 wall-clock hours, parallelized on 4 Nvidia L40 GPUs. For other hyper-parameters, we follow the default setting from [20]. Initially, we had trained diffusion policy for putting tomato on the plate. While fine-tuning _π_ 0, we chose to replace the plate with a box to make the task semantically more meaningful with a variety of objects. 

### **E.2 Paired and Additional Simulation Data** 

**Figure 15** Objects used to train multi-object policy. 

A key assumption in our work is that the environments for the paired evaluation and the additional simulation evaluations are drawn i.i.d from the same distribution. We assume that the objects used for real evaluation are representative of and randomly sampled from some universal distribution of kitchen objects. As discussed in the limitations section, operationalizing this pipeline would require a community-wide investment in building large datasets for evaluation. Despite this limitation, the following histograms in Figure 16 illustrate qualitative similarity in the paired and additional simulation evaluations. 

23 







<!-- Start of picture text -->
(a) (b) π 0<br><!-- End of picture text -->

**Figure 16** Simulation success scores of policies on 3D object models used for paired and additional simulations 

24 

