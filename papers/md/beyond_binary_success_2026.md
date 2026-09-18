# Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison 

David Snyder<sup>1</sup> , Apurva Badithela<sup>3</sup> , Nikolai Matni<sup>1</sup> , 

George Pappas<sup>1</sup> , Anirudha Majumdar<sup>3</sup> , Masha Itkina<sup>2</sup><sup>_‡_</sup> , and Haruki Nishimura<sup>2</sup><sup>_‡_</sup> 

> 1University of Pennsylvania, 2Toyota Research Institute (TRI), 3Princeton University. 

> _‡_ Equal Advising. Corresponding Author: dsnyder5@seas.upenn.edu 

**_Abstract_ —Generalist robot manipulation policies are becoming increasingly capable, but are limited in evaluation to a small number of hardware rollouts. This strong resource constraint in real-world testing necessitates both more informative performance measures and reliable and efficient evaluation procedures to properly assess model capabilities and benchmark progress in the field. This work presents a novel framework for robot policy comparison that is sample-efficient, statistically rigorous, and applicable to a broad set of evaluation metrics used in practice. Based on safe, anytime-valid inference (SAVI), our test procedure is** **_sequential_ , allowing the evaluator to** **_stop early_ when sufficient statistical evidence has accumulated to reach a decision at a pre-specified level of confidence. Unlike previous work developed for binary success, our unified approach addresses a wide range of informative metrics: from discrete partial credit task progress to continuous measures of episodic reward or trajectory smoothness, spanning both parametric and nonparametric comparison problems. Through extensive validation on simulated and real-world evaluation data, we demonstrate up to 70% reduction in evaluation burden compared to standard batch methods and up to 50% reduction compared to state-ofthe-art sequential procedures designed for binary outcomes, with no loss of statistical rigor. Notably, our empirical results show that competing policies can be separated more quickly when using fine-grained task progress than binary success metrics.** 

## I. INTRODUCTION 

Recent advances in robot policy synthesis incorporate increasing complexity throughout the design process, training on large-scale datasets, using sophisticated, stochastic architectures, and requiring commensurate increases in training resources. These advances have led to significant improvements in solving dexterous and long-horizon tasks [9], inferring semantic information from context [33], and safely interacting with numerous other autonomous agents [42]. However, this complexity makes design decisions like the choice of dataset, the training or fine-tuning procedure, and the network architecture analytically opaque. The value of a novel intervention cannot be determined from first principles but instead requires rigorous analysis [2, 41] of its effect on empirical performance. 

Unfortunately, rigorous analysis of empirical performance is a significant challenge in the robotics setting. Hardware evaluation is the gold-standard measure, but is expensive and slow to collect. Evaluations in simulation reduce the time burden, but continue to suffer from sim-to-real gaps, making them an imperfect proxy [3]. Further, evaluation metrics can be quite coarse. Binary measurement of task success or failure, the _de facto_ standard for measuring the performance of robot 

manipulation policies (particularly on hardware), can obscure valuable information about the robot behavior [11, 41]. For instance, a policy that completes 90% of the task is clearly better than a policy that is frozen the whole time, yet their success rates would be identically 0%. Finally, rigorous evaluation must account for inherent uncertainty, including in environment configuration and policy action selection (which is often stochastic [20]). This uncertainty means that observed empirical performance is a noisy estimate of, and _not equivalent to_ , the true expected performance of the policy. 

Since the value of design interventions is implicitly counterfactual (see Figure 1), policy comparison is a particularly important form of evaluation to reliably determine the effects of design changes. For example: ‘does a change in policy architecture [40, 59] or action tokenization [62] improve downstream performance?’ Or: ‘what set of expert data is the most valuable [84] to improve policy performance?’ Importantly, comparison must account for uncertainty in evaluating both the new design and the baseline. Making rigorous, statistically assured decisions for these problems is necessary to ensure reliable progress within the field. 

The costs of robot evaluation and the complexity of the robot policy design space motivate the development of a versatile framework for policy comparison. Ideally, such a framework would apply to very general performance measures, maintain statistical rigor, and ensure maximal sample efficiency via sequentialized evaluation. Current methods are deficient in at least one of these respects. Active learning [5] and asymptotic [16, 81] approaches are not statistically rigorous, particularly in small-data regimes. Batch and fully nonparametric methods [8, 26, 80, 81] are not maximally sample efficient: the former due to the batch evaluation, and the latter due to not tailoring to the comparison setting. Nearoptimal approaches [48, 68, 73] are constrained to narrow metrics (e.g., binary success rate), and do not readily generalize. 

This work presents **N** onparametric **S** equential **CO** mparison for **R** igorous **E** valuation (N-SCORE) to compare robot policy performance. N-SCORE is designed to address the shortcomings of prior approaches by explicitly accounting for all three of the preceding desiderata – rigor, sample efficiency, and generality – within the decision rule synthesis. We summarize our **contributions** as follows: 

- 1) We introduce N-SCORE, a novel method for sequential policy comparison with general progress metrics. 



<!-- Start of picture text -->
Which robot policy is better? Hardware Evaluation Policy Comparison<br>Trial 1<br>Design  vs. Beyond binary metrics<br>Choices  πA πB<br>Action  Simple  Learned Trial 1 : 1/3<br>tokenization binning Tokenizations Stage 1 Stage 2 Stage 3<br>• Partial credit<br>Sequential, any-time<br>• Continuous<br>Data mixture stopping procedure Trial n : 3/3<br>𝒟 A 𝒟 B Trial  n progress score<br>Policy  Single- Pre- Sample efficient<br>Architecture task trained ≈min 𝔼[ n ]<br>Vision  Stage 1 Stage 2 Stage 3 Statistically valid<br>Encoder ℙ[ π 0 >  π 1] ≤ α<br>…<br>…<br>ViT<br>ResNet<br><!-- End of picture text -->

Fig. 1: The evaluation context of the N-SCORE procedure. (Left) We consider the general problem of policy comparison, which arises out of counterfactual design decisions in the policy synthesis process. (Middle) Evaluation on hardware or in high-fidelity simulation is the gold standard to assess the effect of such changes, but is costly to collect. (Right) N-SCORE is a sequential evaluation procedure that is statistically rigorous, sample efficient, and generalizes to rich, diverse measures of robot performance. 

- 2) We prove that N-SCORE is statistically rigorous in the sense of controlling Type-1 Error, and empirically demonstrate its improved sample efficiency compared to state-of-the-art (SOTA) baselines. 

- 3) We comprehensively evaluate N-SCORE on large, highimpact evaluation datasets in robotics comprising over 4500 hardware evaluation rollouts and 2000 high-fidelity simulation rollouts [6, 9]. The results demonstrate significant savings in evaluation effort of up to 70% over batch methods and 50% over methods using binary success measures to rigorously certify policy improvements. 

## II. RELATED WORK 

Efficient evaluation is increasingly appreciated as a critical aspect of the robot policy design process. The fundamental concern of these approaches is the strict limit on available hardware data. A core focus lies in constructing proxy signals (e.g., using simulations or evaluator preferences) to circumvent this constraint. By contrast, statistical testing approaches seek to employ the available hardware data more efficiently. These approaches are complementary; improvements in one domain augment those in the other. 

## _A. Robot Policy Evaluation_ 

**Hardware and Simulation Evaluation.** In robot manipulation, evaluation constraints often limit evaluation to 10-60 trials; the statistical validity of such comparisons is often not reported [41, 68]. To address this constraint, recent works have introduced standardized benchmarks [23, 29, 38, 54, 83], cloud-based evaluation platforms [10, 53, 85, 86], and distributed evaluation infrastructure [6] to increase available data. Further, recent works have proposed active sampling of policy-task pairs to improve efficiency [5]. However, none 

of these approaches confer statistical rigor on downstream comparisons. Similarly, though policy evaluation via simulation [49, 52, 56, 63, 71] or via world models [28, 32, 50, 64, 69, 70, 72, 87] show promise, the sim-to-real gap [3] makes rigorous comparison difficult. Some recent works have proposed statistically rigorous methods to combine small-scale hardware testing with large-scale simulation evaluation [7, 55], but these do not address policy comparison. 

**Evaluation Metrics.** Recent studies emphasize the importance of detailed rubrics and task progress scores [6, 9, 41] over traditional binary success metrics. In parallel, finetuning procedures [33] and policy ranking problems [6, 21] have introduced indirect signals of policy performance, including reinforcement learning (RL) rewards and human preferences. However, none of the approaches give rigorous methods for decision-making. Whereas the state-of-the-art procedure for policy comparison under binary success metrics [68] is rigorous and sample-efficient, current methods for more informative signals are not. This paper introduces a novel test procedure that scales rigorous evaluation to general metrics. 

## _B. The Parametric Policy Comparison Problem_ 

The _parametric_ setting for policy comparison arises when the evaluator designs the performance measure to have definite distributional structure (e.g., binary success or discrete partial credit). This structure specifies a tradeoff between the generality, sample efficiency, and correctness of the comparison. 

Classic tests [8, 13, 26] were designed to optimize power for Bernoulli (binary) outcomes. Some subsequent results use tools from sequential analysis [67] to improve the sample efficiency [47, 77, 78]. In this regime, the STEP procedure [68] is state-of-the-art. Other developments extend the generality of these tests to broader classes of parametric 

distributions [48, 73]. However, simultaneously extending both parametric generality and sample efficiency is difficult, requiring an exact solution of the Wald-Bellman partial differential equation [14, 47, 74]. For more complex parametric families, finding this solution quickly becomes intractable [19, 25]. 

This motivates work that extends generality by making approximations in the large-data regime. A canonical example is Welch’s t-Test [81], which is often used for batch comparison [9, 24, 82]. Further _asymptotic_ results [12] can extend generality [16–18] _and_ improve sample efficiency [43–46], at the cost of losing rigorous statistical assurances. This cost is significantly more pronounced in the low-data regime common to robotic evaluation [41]. Thus, in our setting, conclusions derived from asymptotic approaches are difficult to assess, as their validity is not guaranteed in the low-data regime. 

## _C. Nonparametric Methods and Safe, Anytime-Valid Inference_ 

Nonparametric methods seek to exchange some exploitable structure for generality in application. Within the batch regime, these are often termed ‘distribution free,’ as in the case of conformal prediction and related techniques [4, 66, 76]. However, they have two downsides: limited capacity to represent the underlying data distribution, and limited generalization to sequential settings. Kernel density estimation (KDE) addresses the first constraint by directly constructing a representation of the data-generating process [61]; see [15] for an overview. Critically, KDE is more efficient in low-dimensional settings [35] because it can quickly adapt to structure in the data. However, alone, it is not generally valid in finite samples [79]. 

To address the second constraint, work in the line of safe, anytime-valid inference (SAVI) considers _sequentialization_ of estimation and decision problems, which act in an _online fashion_ [65]. A core benefit is safety in the face of p-hacking [36], or ‘data dredging’ [27, 65]. Additionally, though not parametric, the framework does allow for methodological finetuning to the particular problem setting (as in [22, 51, 73]). Of these approaches, the WSR method [80] is closest to our own, considering the problem of estimating the mean of a general class of random variables (see Definition 1). Importantly, N- SCORE utilizes ideas from KDE to tailor a SAVI framework _specifically to the comparison problem_ , achieving state-of-theart generality and sample-efficiency. 

## III. PRELIMINARIES 

We model a robot that must complete a task while subject to stochastic uncertainty in its environment as a Partially Observable Markov Decision Process (POMDP) [37]. The uncertainty might arise in the initial environment configuration or in the robot’s action selection. We assume the existence of a real-valued scalar performance measure _R_ encoding the degree of success the robot demonstrates in completing the task. Conditioned on an arbitrary robot policy _π_ mapping state observations to actions, the stochastic environment uncertainty is compressed to uncertainty over performance outcomes (i.e., 

by running the policy and measuring its level of success).<sup>1</sup> Thus, all the potential complexities of the task, real-world system dynamics, and policy class are compressed to a (possibly complicated) distribution over the performance measure _DR_ . Our goal is to make rigorous comparisons for as general a class of _DR_ as possible. With this in mind, we make a single restriction: that _R_ be a _progress metric_ , defined as a performance measure that is bounded w.p. 1. 

**Definition 1** (Generalized Progress Metric) **.** A real-valued random variable _M_ ( _ω_ ) is termed a ‘ _generalized progress metric_ ’ if it is bounded; that is, P[ _M ∈_ [0 _,_ 1]] = 1.<sup>2</sup> 

Unless stated otherwise, we assume _R_ is a progress metric as per Definition 1 but make no other structural assumptions. 

We conclude this section with a formalization of the comparison problem in the robotics context. In the most general form, we are tasked with quickly and accurately comparing the means of two distributions over a progress metric _R_ : 



This encompasses many practical problems, for example: comparing two policies with different architectures or trained on different data ( _π_ 0 and _π_ 1), comparing distribution shift in task realizations for a single policy, or comparing the effects of different hyperparameters in training. Importantly, because the true means are unknown and not directly observable, a testing decision must be made on the basis of empirical performance in evaluation. Due to stochastic uncertainty in gathering this data, any decisions are inherently _probabilistic_ over the collection of evaluation data. Thus, we seek statistical assurances that bound the probability of an incorrect inference: 



The challenges to obtaining a result in the form of Equation (1) are twofold. First, the decision must be statistically rigorous— it must safeguard against inadvertently reporting statistical noise as genuine improvement. This can require a substantial number of evaluations when the difference is small or the desired confidence 1 _− α_<sup>_∗_</sup> is very high. However, the result also must be obtained as quickly as possible, so that the evaluator can efficiently allocate hardware or computational resources to begin investigating other problems. Indeed, allocating limited evaluation resources is a major bottleneck in improving policy performance [68]. The sequential nature of N-SCORE balances statistical confidence and speed of decision-making, adaptively making decisions when precisely enough evidence has accumulated and minimizing unnecessary evaluation trials. 

> 1This can be thought of as a pushforward measure (subject to necessary regularity assumptions). 

> 2This immediately extends to real-valued performance measures that are bounded in an interval [ _A, B_ ] via normalization [34, 60, 80]. 

## IV. PROBLEM FORMULATION 

Section III introduced the policy comparison problem, which seeks guarantees as in Equation (1). The challenge in designing a test is the complexity of _DR_<sup>[</sup><sup>_i_],asourprocedure</sup> must be robust to _any such progress metrics arising in practice_ . 

## _A. The Formal Hypotheses_ 

We formulate the problem in the context of frequentist statistical testing [12]. To do so, we construct a general null (skeptical) hypothesis and an alternative (desired) hypothesis which reflect _all possible_ cases of Equation (1). 

In the general nonparametric case (see Section II-C), we consider the set _M_ [0 _,_ 1] of all Lebesgue-measurable distributions on the real interval [0 _,_ 1] (i.e., all progress metrics per Definition 1). We partition _M_ [0 _,_ 1] into two parts:<sup>3</sup> 



Comparing the means amounts to formulating null and alternative hypotheses as _H_ 0 : ( _DR_<sup>[0]</sup><sup>_, D_</sup> _R_<sup>[1])</sup><sup>_∈S−_and</sup><sup>_H_1:</sup> ( _DR_<sup>[0]</sup><sup>_, D_</sup> _R_<sup>[1])</sup><sup>_∈S_+,respectively.</sup> 

These can be intuitively understood as “all possible true states of the world in which the novel innovation is not better” ( _H_ 0, the ‘skeptic’), and “all possible true states of the world in which the novel innovation is better” ( _H_ 1, the ‘desired result’). Equation (1) amounts to being 1 _− α_<sup>_∗_</sup> confident that the true state is _not_ in _S_<sup>_−_</sup> . 

## _B. Measuring the Quality of an Evaluation Algorithm_ 

Having formulated the test hypotheses _H_ 0 and _H_ 1, we consider how to measure the quality of any potential evaluation scheme. These measures can be understood intuitively: the optimal evaluation protocol should _make correct decisions_ and _make the decisions as quickly as possible_ . 

There are precise mathematical analogues of these desiderata. In particular, there are two types of errors which can be made. First, in the case that _H_ 0 is true, the evaluation algorithm may incorrectly decide that _H_ 1 is true. This is termed a false positive, or a ‘Type-1 Error.’ The rate at which such errors occur (under a particular decision-making protocol) is denoted _α ∈_ (0 _,_ 1). Equation (1) precisely amounts to the statement “the Type-1 Error rate of our evaluation method must be less than _α_<sup>_∗_</sup> .” In the case that _H_ 1 is true, the protocol may incorrectly decide that _H_ 0 is true. This is a false negative, or a ‘Type-2 Error.’ The rate at which this occurs is denoted _β ∈_ (0 _,_ 1). Semantically, a Type-1 Error corresponds to reporting a false discovery — that the new policy is better _when it actually is not_ . A Type-2 Error corresponds to a missed discovery — failing to discern that the new policy is better _when it actually is_ . These two error types combine to give a complete accounting of the algorithm’s correctness. The last metric pertains to sample efficiency: how long the algorithm 

> 3For a parametric family Θ (e.g., Bernoulli distributions), the same formalism holds with a restriction to Θ<sup>2</sup> _⊆M_<sup>2</sup> [0 _,_ 1] 

takes to make a decision, denoted E[ _N_ ].<sup>4</sup> As presented, an optimal evaluation algorithm — one that is fast and correct — minimizes all three of the measures _{α, β,_ E[ _N_ ] _}_ . 

## _C. Efficient Tests as a Multi-Objective Optimization_ 

Unfortunately, there are fundamental tradeoffs which prevent simultaneous minimization of all of these metrics. Therefore, we adopt the Neyman-Pearson testing approach [58], which normatively chooses the Type-1 Error rate as the quantity to be rigorously controlled. This amounts to requiring that _α ≤ α_<sup>_∗_</sup> be treated as a hard constraint. Having made this selection, the problem of designing an evaluation procedure reduces to finding (near-)optimal solutions to the following multi-objective optimization problem: 



Here, Γ denotes a space of decision-making rules (evaluation procedures) and _λ ∈_ [0 _, ∞_ ) is a nonnegative parameter trading off the expected time to decision and false negative rate. 

Efficiently solving Equation (2) results in an evaluation procedure that is guaranteed to maintain statistical rigor and quickly and effectively detects changes in performance. This provides the roboticist with the capacity to quickly iterate on new innovations, while ensuring justified and well-calibrated confidence in reported performance improvements. 

## V. METHODOLOGY 

We motivate the N-SCORE procedure via the construction of a process to distinguish _S_<sup>_−_</sup> from _S_<sup>+</sup> . Intuitively, we will construct a scalar-valued dynamical system that behaves fundamentally differently when _H_ 0 is true than when _H_ 1 is true, based on the empirical evidence observed during evaluation. This difference is precisely in the sense of being stable in the former case and unstable in the latter. The testing problem then reduces to assessing the stability properties of the dynamical system; this assessment can be rigorously quantified within the SAVI framework described in Section II-C. 

## _A. Constructing an ‘Evidence Integrator’_ 

A natural correlate to _H_ 1 is the difference in the evaluation reward; if we are on the _n_<sup>_th_</sup> evaluation trial, we consider: 



where _ξ >_ 0 is a positive scaling factor and _r_ 0 _,n_ , _r_ 1 _,n_ are the observed progress values. Intuitively, the evidence for _H_ 1 is positive when _r_ 1 _,n > r_ 0 _,n_ and negative otherwise. Note that by assumed independence of the evaluation trials, this relationship does not depend on _n_ . What remains is to design the appropriate rate of integration of this evidence. Results in 

> 4For technical reasons, sample efficiency must be posed with respect to a measure over _S_<sup>+</sup> . This amounts in practice to prior beliefs over features like the size of the gap in performance; the reader may safely assume, e.g., an ‘uninformative’ uniform measure. 

|**Algorithm 1** N-SCORE Evaluation Protocol|
|---|
|**Input:**<br>|
|Type-1 error limit _α_<sup>_∗_</sup>_∈_(0_,_1), evaluation limit _N_max _>_0.|
|**Initialize:**<br><sup>¯</sup>|
|_X_0 = 1; _X_ = 1; _ξ_0 = 0; _F_0 =_{∅}_; _n_= 1.<br><sup>¯</sup>|
|**while** _X <_1_/α_<sup>_∗_</sup>**and** _n ≤Nmax_ **do**<br>|
|Observe evaluation progress scores: _r_0_,n_, _r_1_,n_<br>|
|Compute increment: _an−_1 = 1 +_ξn−_1(_r_1_,n −r_0_,n_)|
|Update martingale: _Xn ←an−_1_· Xn−_1<br><sup>¯¯</sup>|
|Update test statistic: _X ←_max_{_ _X, Xn}_|
|Update filtration: _Fn ←Fn−_1_∪_(_r_0_,n_, _r_1_,n_)<br>|
|Update _ξn ←_proj[0_,_1] _g_(_Fn_)<br>_n ←n_+ 1<br>**end while**<br><sup>¯</sup>|
|**if** _X <_1_/α_<sup>_∗_</sup>**then**<br>**return** Fail to Reject Null<br>**else**|
|**return** Reject Null<br>**end if**|



the SAVI literature and across a variety of statistical estimation contexts suggest that the optimal aggregation rate [65] is _multiplicative_ , resulting in a measure of aggregate evidence _Xn_ (setting _X_ 0 = 1 w.l.o.g.) that evolves according to: 



Therefore, when the evidence is positive for _H_ 1, the growth rate is greater than one, and the system is locally unstable. Conversely, when it is negative (i.e., in favor of _H_ 0), the growth rate is less than one and the system is stable. We can additionally optimize _ξn_ = _g_ ( _Fn−_ 1) online based on the evidence accumulated so far (the ‘natural filtration’ _Fn−_ 1), as long as the choice of _ξn_ is independent of ( _r_ 0 _,n, r_ 1 _,n_ ). 

The last step is designating an evidence threshold, amounting to the idea that “ _Xn_ has become sufficiently unstable as to provide sufficient evidence that the true state of the world is not in _H_ 0.” We designate the threshold to be 1 _/α_<sup>_∗_</sup> , for a desired Type-1 Error rate _α_<sup>_∗_</sup> of the test procedure. 



This procedure is operationalized in Algorithm 1. As shown in Section V-B, this evaluation protocol efficiently balances time-to-decision and correctness, while rigorously controlling the Type-1 Error rate at tunable, pre-specified level _α_<sup>_∗_</sup> . These properties enable rigorous confidence in comparison problems (yielding statements of the form of Equation (1)) while minimizing the evaluation burden necessary to reliably form them. 

## _B. Theoretical Properties of Algorithm 1_ 

We briefly present several key theoretical results of the evaluation protocol effectuated in Algorithm 1. The import of 

these results, along with proof sketches, are included _in situ_ . Detailed proofs are deferred to the Supplement. 

We begin with a critical lemma pertaining to a property of the evidence aggregation process in Equation (3). This property amounts to a statement that the stochastic process _Xn_ is stable in expectation _for all_ elements _h ∈H_ 0. 

**Lemma 1** (Null Stability (NSM) Property) **.** _Consider the stochastic process {Xn} defined in Equation_ (3) _, setting (w.l.o.g.) X_ 0 = 1 _. Then the expectation of {Xn} is contracting in time with respect to the current value, for all h ∈ S_<sup>_−_</sup> _for any ξn ∈_ [0 _,_ 1] _. That is:_ 



Lemma 1 is necessary for ensuring stability of the process in Equation (3) because it rules out (with high probability) that evidence increments generated by any element of _H_ 0 will cause the process to grow by very much. This is a necessary step to ensure Type-1 Error control and enforce the hard constraint in Equation (2), which is formalized in Theorem 1. 

**Theorem 1** (Type-1 Error Control of Algorithm 1) **.** _Consider the evaluation procedure in Algorithm 1, utilizing the process defined in Equation_ (3) _. Then_ 



_Proof:_ The proof uses Lemma 1 in concordance with Ville’s Inequality [75] to bound the probability of observing large values of _Xn_ . After verifying several ancillary conditions and matching constants, the bound can be computed directly. More detail can be found in the Supplement. 

Enforcing Type-1 Error control ensures high confidence (at level 1 _− α_<sup>_∗_</sup> ) that reported significant innovations and improvements to the state-of-the-art are strictly separated from the inherent noise in robotic evaluation. 

**Remark 1** (Efficient Optimization of _ξn_ ) **.** Consider the stochastic process family described in Equation (3), and let _Fn_ be the natural filtration _{_ ( _r_ 0 _,i, r_ 1 _,i_ ) _}_<sup>_n_</sup> _i_ =1<sup>_−_1at step</sup><sup>_n_. There exists</sup> an efficient algorithm to maximize (online) over _{ξn}_<sup>_N_</sup> _n_ =1<sup>the</sup> expected growth rate of _{Xn}_<sup>_N_</sup> _n_ =1<sup>.</sup> 

Intuitively, _ξn_ modulates the degree of confidence in marginal changes to _Xn_ . Large _ξn_ grow the process more quickly when data is favorable, but are penalized more harshly when it is not. Identifying an effective strategy to modulate _ξn_ online is central to improving sample efficiency across a broad array of evaluation problems. To do this, N-SCORE utilizes intuition from kernel density estimation and the structure of the discrete partial credit setting to optimize _ξn_ via constructing explicit nonparametric representations of _DR_<sup>[</sup><sup>_i_].This</sup> is represented as a family N-SCORE _k_ , where _k ∈_ N is a real-valued parameter akin to the kernel bandwidth. For brevity, details about this optimization are deferred to the Supplement. However, we emphasize that this optimization 

has strong practical benefits, yielding a state-of-the-art nearoptimal solution to Equation (2) for general progress metrics. 

## VI. EXPERIMENTAL RESULTS 

We evaluate N-SCORE across a broad suite of evaluation settings, including some of the largest available datasets for real-world robot comparison with task progress metrics, such as RoboArena [6] and the LBM 1.0 study [9]. To organize the results, we tie them to three core research questions (RQs): 

- 1) ( **Sequential Evaluation** ) Are there sample efficiency benefits of sequential evaluation? 

- 2) ( **Informative Metrics** ) Are there sample efficiency benefits from using more informative evaluation metrics than coarse binary success? 

- 3) ( **Technical Novelty** ) What are the benefits of N- SCORE with respect to statistically valid sequential policy comparison approaches? 

## _A. Baseline Methods_ 

We introduce three relevant baselines, proceeding in order of increasing generality. The recently proposed STEP procedure [68] demonstrated SOTA performance in the setting of binary success metrics. However, STEP is tailored to this narrow, but important setting and does not generalize to more informative metrics. Another recent work proposed a safe, anytimevalid inference approach to parametric comparison problems, motivated by settings with discrete partial credit [73]. This method, termed _θ_ -SAVI to denote its parametric nature, is more general than STEP, as it retains validity for any parametric comparison setting (defined in Section II-B). As with STEP, _θ_ -SAVI cannot extend to nonparametric performance metrics such as continuous-valued progress scores. The most general evaluation procedure is the test dual to the WSR estimation method [80], which is also most similar among the baselines to our approach. Thus, the key comparison between WSR and N- SCORE will center on sample efficiency. 

## _B. RQ1 and RQ2: Sequential Evaluation with Informative Metrics_ 

Our experiments support the observations in Snyder et al. [68] that sequential test procedures save significant time and resources for robotics evaluations under binary success metrics. We further observe the benefit of sequential procedures to extend to more fine-grained evaluation metrics. 

_1) Results on Artificial Bernoulli Sequences:_ The left-hand side of Table I shows the average time-to-decision for each baseline and N-SCORE on artificially generated Bernoulli data comprising 35 different distributions, where each baseline is tested on each distribution 250 times. In each instance, the batch evaluation size was set to _N_ = 1000 samples per test. Further visualizations of these tests are deferred to the Supplement. The average time-to-decision is shown to be significantly less than 1000 samples, illustrating the practical benefit of early stopping when the evaluation problem is sufficiently easy as to not require the full batch allocation. 

||**Bernou**|**lli Data**|**Nonpara**|**metric Data**|
|---|---|---|---|---|
||TTD|Power|TTD|Power|
|STEP|95.1|0.953|–|–|
|SAVI|117.6|0.962|–|–|
|N-SCORE2|117.9|0.965|–|–|
|N-SCORE_∞_|122.3|0.958|206.8|0.889|
|WSR|224.8|0.592|247.3|0.840|



TABLE I: **Average time-to-decision (TTD) and empirical power for each method on simulated data.** For Bernoulli data (left), TTD is averaged over all 35 alternative hypotheses, while Power is averaged only the 9 hardest alternative hypotheses corresponding to a gap of 0 _._ 1 (all other 26 alternatives have empirical power 1). For each alternative, metrics are averaged over 250 independent redraws; each redraw has _N_ = 1000. We observe similar statistical power for all methods except WSR, which lags substantially due to high variance in the Bernoulli regime. For nonparametric data (right), TTD and power are averaged over 3000 independent redraws (there is only one alternative). Only N-SCORE _∞_ and WSR are valid in the nonparametric regime; the remaining methods cannot be adapted to this case. We observe that N-SCORE _∞_ outperforms WSR by approximately 15% on average in terms of time-to-decision, while improving the empirical power by approximately 5 percentage points. 



<!-- Start of picture text -->
395 Trials required 503 641 503 18 641 Trials required581 641 641 18<br>N-SCORE WSR<br>(Ours)<br>2<br><!-- End of picture text -->

Fig. 2: **Policy performance comparisons on crowd-sourced real-world evaluations on the DROID [39] setup from RoboArena [6]** . The violin plots represent empirical distributions of observed results. Policies with different letters are statistically distinguishable by the method. Policies are compared at a global error bound of _α_ = 0 _._ 05 with a Bonferroni correction. 

_2) Results on LBM 1.0 Binary Evaluation [9]:_ We now consider real-world binary evaluation data for robot policies from the LBM 1.0 study results [9]. The binary success metric results are on the right side of Table II. In this example, a pretrained and then finetuned policy is compared to a singletask policy trained from scratch to evaluate performance; it is desired to test whether the pretrained policy outperforms the single-task policy on challenging, long-horizon tasks. The tasks and rollout data come from the experimental setup of LBM 1.0 [9]. The top half considers robot performance comparison in high-fidelity simulator data. For each task and 

|Method _→_|**Progress Me**|**trics**|**Bin**|**ary Success/Fa**|**ilure Metr**|**ics**|
|---|---|---|---|---|---|---|
|Task _↓_|N-SCORE_∞_|WSR|STEP|N-SCORE2|_θ_-SAVI|WSR|
|DumpVegetables|38|36|154|–|–|–|
|PutContainer|33|36|169|–|–|–|
|PutFruit|10|10|40|46|45|52|
|SeparateFruit|18|20|77|98|98|103|
|TurnUpsideDown|–|–|–|–|–|–|
|Total (Simulation)|598|604|1280|1488|1486|1510|
|BikeRotor|–|–|–|–|–|–|
|CutApple|29|29|–|–|–|–|
|CleanLitter|36|23|–|–|–|–|
|ClearCounter|16|15|23|25|30|46|
|SetUpBreakfast|12|13|15|19|19|17|
|Total (Hardware)|286|260|376|388|398|426|



TABLE II: **Time-to-decision for all simulation (top) and hardware (bottom) policy comparisons for evaluation context in [9]** . If a decision is not reached, the entry is left blank; for the purpose of computing evaluation savings, any blank entry is counted at _N_ trials. All simulation tasks utilize _N_ = 200; all hardware tasks utilize _N_ = 50. The total number of trials is the column sum multiplied by two (because there are two policies being evaluated, and each must be run). Thus, a column in the top half could require up to 2000 simulated trajectories; one in the bottom half could require up to 500 hardware evaluations. Several important observations are: (1) sequential evaluation saves significant evaluation effort over batch methods (right); (2) more informative partial credit metrics can provide _even greater_ savings (left). In fact, for these evaluations, the savings are up to 50% on hardware and 70% in simulation. 

method, the time-to-decision (TTD) is recorded in terms of the number of evaluations per policy before a comparison outcome at level _α_ = 0 _._ 05 was reached. The total number of nominal batch evaluations is 2000. We observe savings of 25% _−_ 35% from the use of sequential evaluation procedures, resulting in an empirical reduction in the requisite number of simulations of approximately 500-700. In the bottom half, we consider the same comparison on hardware. In this setting, the nominal batch evaluation burden is 500. We again observe significant savings, on the order of 16% _−_ 25%, corresponding to a savings of up to 125 total evaluations on this task suite. 

RQ2 considers the efficiency of evaluation in settings which go beyond binary metrics. Following the structure of RQ1, we again consider significant evidence from both simulated and real-world evaluation data. Here, however, the core purpose is to illustrate the generality of nonparametric approaches, which open up opportunities for rigorous comparison of richer metrics, including RL rewards and continuous progress metrics. 

_3) Results on Simulated Nonparametric Data:_ We again start with results on simulated data, now generated from nonparametric densities. Random polynomials of order up to 10 are generated, and then rectified into an appropriate density (they are shifted and scaled to be everywhere nonnegative on [0 _,_ 1] and to integrate to 1). This process is analytically opaque, making it difficult to express the resulting family of distributions in any parametric form. Thus, only N-SCORE and WSR are applicable. We run 3000 comparison sequences of pairs of these distributions, limiting to cases where the gap 

in mean performance is at least 0 _._ 01. _N_ = 1000 for each sequence. The right-hand side of Table I shows summary statistics for N-SCORE and WSR, respectively. Again, the average time-to-decision is very low in comparison to the batch allocation, suggesting that distribution complexity does not impede efficient comparison, and does not attenuate the sample efficiency benefits of this evaluation paradigm. 

_4) Results on LBM 1.0 Partial Credit Evaluation [9]:_ We repeat the analysis of the task and rollout data obtained from Barreiros et al. [9], as described in the preceding section, but using the discrete partial credit rubric instead of binary success metrics. Before each task was evaluated, partial credit measures (e.g., completion rate of _K_ subtasks) were designed to provide fine-grained information on the policy performance. In every task, this varied between six and eight partial credit outcomes; each subtask was weighted equally in the scoring. As before, the top half corresponds to policy evaluation in high-fidelity simulation, with a total evaluation budget of 2000 rollouts. As shown in the left-hand side of Table II, partial credit metrics yield savings of approximately 70%, corresponding to a nearly 1400-sample reduction in the number of evaluations for each sequential procedure. Further, this corresponds to an equivalent improvement over sequential binary methods, such as STEP, of over 50%. On hardware trials, the results are similar in trend. We observe approximately 45% reduction in the number of required evaluations with respect to the batch procedure (which arbitrarily chooses 50 runs per task per policy). This corresponds to a 24% _−_ 30% reduction in evaluation burden with respect to SOTA binary procedures like STEP [68]. The preceding evaluation gives strong empirical evidence for answering RQ1 and RQ2 in the affirmative: sequentialized evaluation reliably improves sample efficiency on artificial and real-world data across a wide range of metrics and uncertainty distributions. 

## _C. RQ3: Improving Sample Complexity Over Baselines_ 

Finally, we discuss instances of performance differences between N-SCORE and related baselines. 

_1) Simulated Nonparametric Data:_ From the right-hand side of Table I, there is a moderate gap in average timeto-decision, corresponding to average savings of around 15% in evaluation burden. This can be understood as the aggregate effect of the efficient mechanism to optimize _ξn_ (see Algorithm 1), which does not have a clear analogue in the WSR approach. Furthermore, neither STEP nor the _θ_ -SAVI approaches can be applied in this setting. 

Due to the generality of the nonparametric testing paradigm, the times-to-decision can be statistically compared using the N-SCORE framework. To do this, the 3000 runs are randomly partitioned into two sets, each of size 1500, corresponding to the time-to-decision of one of the two methods (N-SCORE or WSR) on that data. These can be sequentially ttd _i,n_ compared using the metrics _ri,n_ = _N_<sup>.Notethattorun</sup> this evaluation in a parametric model would require dimension _N_ +1 = 1001. The N-SCORE procedure returns a decision at _α_ = 0 _._ 05 in approximately 525 evaluations, corresponding to 

the hypothesis: “the N-SCORE procedure has a lower timeto-decision than WSR on this class of nonparametric densities w.p. _≥_ 0 _._ 95.” 

_2) Simulated Bernoulli Data:_ We consider the left-hand side of Table I to specifically consider the differences between sequential evaluation methods. Here, all baselines are applicable. We observe that STEP is optimal, as expected in this setting. However, among the remaining methods, _θ_ -SAVI and N-SCORE perform nearly identically, suggesting that our approach is able to efficiently approximate the available parametric structure. WSR, conversely, suffers substantially in the time-to-decision as compared to these approaches. 

_3) LBM 1.0 Success and Partial Credit:_ Now, we revisit the results in Table II to consider the implications for each evaluation procedure. Here, we observe that STEP is again optimal for binary success measures, consistent with the previous section. For this data, _θ_ -SAVI, N-SCORE , and WSR are equally effective in both binary and discrete partial credit evaluation on this dataset. 

_4) Results on RoboArena:_ We continue the analysis of real-world evaluation data by illustrating the efficacy of N- SCORE , in addition to its applicability to multi-policy comparisons using continuous progress evaluation scores, in simultaneously comparing four policies from the open-source RoboArena [6] benchmark. Further details of the dataset are deferred to the Supplement. Because the rewards are continuous, only N-SCORE and WSR can be applied. Figure 2 illustrates the time-to-decision (TTD) in terms of the number of trials required for each policy by N-SCORE and WSR. N- SCORE is able to distinguish the performance of all policies. In contrast, while WSR is able to correctly distinguish the best policy as _π_ 0-FAST, it is unable to separate _π_ 0 and PGDiff even after exhausting all available 641 trials. Notably, N- SCORE requires over 200 fewer trials of _π_ 0, and results in a total savings of at least **450 trials** (1419 vs. 1881). The efficacy of our method can be attributed to efficient optimization of _ξn_ (see Remark 1) with the available data, and due to WSR not being optimized for policy comparison. 

_5) Real-valued Continuous Metrics:_ The final example we consider is determining the best reinforcement learning (RL) policy based on continuous-valued episodic rewards, whose underlying distribution is difficult to model. Table III lists the time-to-decision in distinguishing popular RL algorithms (PPO, TD3, DDPG, and SAC) on Mujoco [71] benchmarks. Due to the continuous nature of the reward metric, only N- SCORE and WSR are applicable. We observe significant improvement over the WSR baseline when policies perform similarly but have high variance such as in the case of InvertedPendulum-v4. In this instance, N-SCORE saves over 400 trials when comparing PPO with DDPG. For the same benchmark, SAC and TD3 are highly effective, returning the maximum possible reward in each rollout, thereby leading to no statistical separation by either method. We provide further experimental details including mean episodic return and violin plots in the Supplement. 

As demonstrated by these extensive empirical validations, 

|Comparison _→_|**PPO**|**vs. DDPG**|**SAC **|**vs. TD3**|
|---|---|---|---|---|
|Task _↓_<br>Method _→_|WSR|N-SCORE_∞_|WSR|N-SCORE_∞_|
|Ant-v4|27|21|14|13|
|HalfCheetah-v4|8|8|18|15|
|Hopper-v4|13|12|30|20|
|InvertedPendulum-v4|677|**267**|–|–|
|Humanoid-v4|42|40|96|89|
|Walker2d-v4|23|22|24|22|
|Pusher-v4|89|77|249|220|
|Total (14000 nominal)|1758|**894**|2862|**2758**|



TABLE III: **Time-to-decision for selected reinforcement learning policy comparisons on Mujoco benchmarks.** If a decision is not reached, the entry is left blank; for the purpose of computing evaluation savings, any blank entry is counted at _N_ trials. All simulated tasks utilize _N_ = 1000. We observe similar behavior between N-SCORE and WSR on easier instances (with lower times-to-decision); however, in harder instances significant improvements can be observed. In aggregate, the hard instances dominate sample complexity, resulting in substantial savings in evaluation burden. 

the key impact of our novel approach lies in effectively matching the sample efficiency of _θ_ -SAVI in parametric contexts (e.g., Table I and Table II), while maintaining the generality of, and improving sample efficiency over, the WSR procedure in nonparametric contexts (e.g., Table III and Figure 2). 

## VII. LIMITATIONS AND FUTURE WORK 

There are several current limitations of N-SCORE, which suggest the possibility for valuable future investigation. First, unlike STEP, any procedure using tools from safe, anytimevalid inference (SAVI) tends to achieve tighter Type-1 error control than specified, leaving some ‘risk budget’ unused. This both explains the gap to STEP in the regime of binary evaluation metrics and the capacity for robust generalization to complex and nonparametric measures. Developing a finite- _N_ rectification to use the full available risk budget would be exceedingly valuable for a host of problems for which SAVI is currently applied. Similarly, the current method for optimizing _ξn_ has connections to ideas in kernel density estimation, but at present the full insight of developments in the latter have not been applied to our approach. Using these tools and domain knowledge promises more efficiency and potential generalization to unbounded performance measures. 

We note that, while SAVI methods naturally hinder some avenues towards inadvertent data dredging, they rely crucially on i.i.d. evaluation data. Moreover, rigorous guarantees are only meaningful if the evaluation paradigm is similarly rigorous and reproducible. As such, these methods are inherently dependent on careful and measured evaluation procedures. 

## VIII. CONCLUSION 

We have introduced and validated a novel procedure for statistically rigorous sequential evaluation of robot policies, generalized to metrics that go beyond binary success and failure rates. In so doing, we have highlighted the practical benefits of sequential methods and informative metrics to reduce evaluation burden, and situated our approach as a 

novel synthesis of two state-of-the-art sequential evaluation procedures. Each of these results is validated by substantial empirical evidence spanning simulated and real-world evaluation data. The promise of such results is to both codify _and accelerate_ progress within the field, by ensuring reliable performance improvements and minimizing the requisite evaluation burden necessary to confirm them. 

## ACKNOWLEDGMENTS 

D. Snyder acknowledges support from the Toyota Research Institute (TRI) and the Penn AI Fellowship. A. Badithela is supported by the Presidential Postdoctoral Fellowship. Additionally, the authors were partially supported by the NSF Career Award #2044149, the NSF SLES Award #2331880, and the Sloan Fellowship. TRI provided funds to assist the authors with their research; this article solely reflects the opinions and conclusions of its authors, and not TRI nor any other Toyota entity. 

## REFERENCES 

- [1] Joshua Achiam. Spinning Up in Deep Reinforcement Learning. 2018. 

- [2] Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron C Courville, and Marc Bellemare. Deep reinforcement learning at the edge of the statistical precipice. volume 34, pages 29304–29320, 2021. doi: 10.48550/arXiv.2108.13264. 

- [3] Elie Aljalbout, Jiaxu Xing, Angel Romero, Iretiayo Akinola, Caelan Reed Garrett, Eric Heiden, Abhishek Gupta, Tucker Hermans, Yashraj Narang, Dieter Fox, Davide Scaramuzza, and Fabio Ramos. The Reality Gap in Robotics: Challenges, Solutions, and Best Practices. December 2025. doi: 10.1146/annurev-control-031924-100130. URL https://www.annualreviews.org/content/journals/10. 1146/annurev-control-031924-100130. 

- [4] Anastasios N. Angelopoulos and Stephen Bates. A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification, December 2022. URL http://arxiv.org/abs/2107.07511. arXiv:2107.07511 [cs]. 

- [5] Abrar Anwar, Rohan Gupta, Zain Merchant, Sayan Ghosh, Willie Neiswanger, and Jesse Thomason. Efficient evaluation of multi-task robot policies with active experiment selection. _arXiv preprint arXiv:2502.09829_ , 2025. 

- [6] Pranav Atreya, Karl Pertsch, Tony Lee, Moo Jin Kim, Arhan Jain, Artur Kuramshin, Clemens Eppner, Cyrus Neary, Edward Hu, Fabio Ramos, et al. Roboarena: Distributed real-world evaluation of generalist robot policies. _arXiv preprint arXiv:2506.18123_ , 2025. 

- [7] Apurva Badithela, David Snyder, Lihan Zha, Joseph Mikhail, Matthew O’Kelly, Anushri Dixit, and Anirudha Majumdar. Reliable and scalable robot policy evaluation with imperfect simulators. _arXiv preprint arXiv:2510.04354_ , 2025. 

- [8] G. A. Barnard. Significance Tests for 2×2 Tables. _Biometrika_ , 34(1-2):123–138, January 1947. ISSN 00063444. doi: 10.1093/biomet/34.1-2.123. 

- [9] Jose Barreiros, Andrew Beaulieu, Aditya Bhat, Rick Cory, Eric Cousineau, Hongkai Dai, Ching-Hsin Fang, Kunimatsu Hashimoto, Muhammad Zubair Irshad, Masha Itkina, et al. A careful examination of large behavior models for multitask dexterous manipulation. _arXiv preprint arXiv:2507.05331_ , 2025. 

- [10] Stefan Bauer, Manuel W¨uthrich, Felix Widmaier, Annika Buchholz, Sebastian Stark, Anirudh Goyal, Thomas Steinbrenner, Joel Akpo, Shruti Joshi, Vincent Berenz, et al. Real robot challenge: A robotics competition in the cloud. In _NeurIPS 2021 Competitions and Demonstrations Track_ , pages 190–204. PMLR, 2022. 

- [11] Yoav Beck, Talia Herman, Marina Brozgol, Nir Giladi, Anat Mirelman, and Jeffrey M. Hausdorff. SPARC: a new approach to quantifying gait smoothness in patients with Parkinson’s disease. _Journal of NeuroEngineering and Rehabilitation_ , 15(1):49, June 2018. ISSN 17430003. doi: 10.1186/s12984-018-0398-3. URL https:// doi.org/10.1186/s12984-018-0398-3. 

- [12] Peter J. Bickel and Kjell A. Doksum. _Mathematical Statistics: Basic Ideas and Selected Topics, Volumes I- II Package_ . Chapman and Hall/CRC, New York, December 2015. ISBN 978-1-315-36926-6. doi: 10.1201/ 9781315369266. 

- [13] R. D. Boschloo. Raised conditional level of significance for the 2 × 2-table when testing the equality of two probabilities. _Statistica Neerlandica_ , 24(1):1–9, 1970. doi: 10.1111/j.1467-9574.1970.tb00104.x. 

- [14] Luis A. Caffarelli and S. Salsa. _A Geometric Approach to Free Boundary Problems_ . American Mathematical Soc., 2005. ISBN 978-0-8218-3784-9. Google-BooksID: YOzpBwAAQBAJ. 

- [15] Yen-Chi Chen. A Tutorial on Kernel Density Estimation and Recent Advances, September 2017. URL http://arxiv. org/abs/1704.03924. arXiv:1704.03924 [stat]. 

- [16] Herman Chernoff. Sequential Tests for the Mean of a Normal Distribution. In _Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Contributions to the Theory of Statistics_ , volume 4.1, pages 79–92. University of California Press, January 1961. 

- [17] Herman Chernoff. Sequential Test for the Mean of a Normal Distribution III (Small t). _The Annals of Mathematical Statistics_ , 36(1):28–54, 1965. ISSN 00034851. Publisher: Institute of Mathematical Statistics. 

- [18] Herman Chernoff. Sequential Tests for the Mean of a Normal Distribution IV (Discrete Case). _The Annals of Mathematical Statistics_ , 36(1):55–68, 1965. ISSN 00034851. Publisher: Institute of Mathematical Statistics. 

- [19] Herman Chernoff and A. John Petkau. Numerical Solutions for Bayes Sequential Decision Problems. _SIAM Journal on Scientific and Statistical Computing_ , 7(1):46– 59, 1986. doi: 10.1137/0907003. 

- [20] Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran Song. Diffusion policy: Visuomotor policy learning via action diffusion. _The International Journal of Robotics Research_ , 44(10-11):1684–1704, September 2025. ISSN 0278-3649. doi: 10.1177/02783649241273668. URL https://doi.org/10.1177/02783649241273668. 

- [21] Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li, Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E Gonzalez, et al. Chatbot arena: An open platform for evaluating llms by human preference. In _Forty-first International Conference on Machine Learning_ , 2024. 

- [22] Brian Cho, Kyra Gan, and Nathan Kallus. Peeking with PEAK: Sequential, Nonparametric Composite Hypothesis Tests for Means of Multiple Data Streams, June 2024. URL http://arxiv.org/abs/2402.06122. arXiv:2402.06122 [stat]. 

- [23] Jack Collins, Mark Robson, Jun Yamada, Mohan Sridharan, Karol Janik, and Ingmar Posner. Ramp: A benchmark for evaluating robotic assembly manipulation and planning. _IEEE Robotics and Automation Letters_ , 9(1): 9–16, 2023. 

- [24] Yan Duan, Xi Chen, Rein Houthooft, John Schulman, and Pieter Abbeel. Benchmarking Deep Reinforcement Learning for Continuous Control, May 2016. URL http: //arxiv.org/abs/1604.06778. arXiv:1604.06778 [cs]. 

- [25] Michael Fauss, Abdelhak M. Zoubir, and H. Vincent Poor. Minimax Optimal Sequential Hypothesis Tests for Markov Processes. _The Annals of Statistics_ , 48(5):2599– 2621, 2020. ISSN 0090-5364. Publisher: Institute of Mathematical Statistics. 

- [26] R. A. Fisher. On the interpretation of _χ_<sup>2</sup> from contingency tables, and the calculation of p. _Journal of the Royal Statistical Society_ , 85(1):87–94, 1922. ISSN 09528385. URL http://www.jstor.org/stable/2340521. 

- [27] Peter Gr¨unwald, Rianne de Heide, and Wouter Koolen. Safe testing. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 86(5):1091–1128, November 2024. ISSN 1369-7412. doi: 10.1093/jrsssb/ qkae011. URL https://doi.org/10.1093/jrsssb/qkae011. 

- [28] Yanjiang Guo, Lucy Xiaoyang Shi, Jianyu Chen, and Chelsea Finn. Ctrl-world: A controllable generative world model for robot manipulation. _arXiv preprint arXiv:2510.10125_ , 2025. 

- [29] Minho Heo, Youngwoon Lee, Doohyun Lee, and Joseph J. Lim. Furniturebench: Reproducible real-world benchmark for long-horizon complex manipulation. In _Robotics: Science and Systems_ , 2023. 

- [30] Wassily Hoeffding. Probability inequalities for sums of bounded random variables. _Journal of the American statistical association_ , 58(301):13–30, 1963. 

- [31] Shengyi Huang, Rousslan Fernand Julien Dossa, Chang Ye, Jeff Braga, Dipam Chakraborty, Kinal Mehta, and Jo˜ao G.M. Ara´ujo. Cleanrl: High-quality single-file implementations of deep reinforcement learning algorithms. 

_Journal of Machine Learning Research_ , 23(274):1–18, 2022. URL http://jmlr.org/papers/v23/21-1342.html. 

- [32] Siyuan Huang, Liliang Chen, Pengfei Zhou, Shengcong Chen, Zhengkai Jiang, Yue Hu, Yue Liao, Peng Gao, Hongsheng Li, Maoqing Yao, et al. Enerverse: Envisioning embodied future space for robotics manipulation. _arXiv preprint arXiv:2501.01895_ , 2025. 

- [33] Physical Intelligence, Ali Amin, Raichelle Aniceto, Ashwin Balakrishna, Kevin Black, Ken Conley, Grace Connors, James Darpinian, Karan Dhabalia, Jared DiCarlo, et al. _π{_ 0 _._ 6 _}_ : A vla that learns from experience. _arXiv preprint arXiv:2511.14759_ , 2025. 

- [34] Kyoungseok Jang, Kwang-Sung Jun, Ilja Kuzborskij, and Francesco Orabona. Tighter PAC-Bayes Bounds Through Coin-Betting. In _Proceedings of Thirty Sixth Conference on Learning Theory_ , pages 2240–2264. PMLR, July 2023. URL https://proceedings.mlr.press/v195/jang23a. html. 

- [35] Heinrich Jiang. Uniform Convergence Rates for Kernel Density Estimation. In _Proceedings of the 34th International Conference on Machine Learning_ , pages 1694– 1703. PMLR, July 2017. URL https://proceedings.mlr. press/v70/jiang17b.html. 

- [36] Leslie K John, George Loewenstein, and Drazen Prelec. Measuring the prevalence of questionable research practices with incentives for truth telling. _Psychological Science_ , 23(5):524–532, 2012. doi: 10.1177/ 0956797611430953. 

- [37] Leslie Pack Kaelbling, Michael L Littman, and Anthony R Cassandra. Planning and acting in partially observable stochastic domains. _Artificial intelligence_ , 101(1-2):99–134, 1998. doi: 10.1016/S0004-3702(98) 00023-X. 

- [38] Ninad Khargonkar, Sai Haneesh Allu, Yangxiao Lu, Balakrishnan Prabhakaran, Yu Xiang, et al. Scenereplica: Benchmarking real-world robot manipulation by creating replicable scenes. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 8258– 8264. IEEE, 2024. 

- [39] Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth Karamcheti, Soroush Nasiriany, Mohan Kumar Srirama, Lawrence Yunliang Chen, Kirsty Ellis, et al. Droid: A large-scale in-the-wild robot manipulation dataset. _arXiv preprint arXiv:2403.12945_ , 2024. 

- [40] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, et al. OpenVLA: An Open-Source Vision-Language-Action Model. _arXiv preprint arXiv:2406.09246_ , 2024. doi: 10.48550/ arXiv.2406.09246. 

- [41] Hadas Kress-Gazit, Kunimatsu Hashimoto, Naveen Kuppuswamy, Paarth Shah, Phoebe Horgan, Gordon Richardson, Siyuan Feng, and Benjamin Burchfiel. Robot learning as an empirical science: Best practices for policy evaluation. _arXiv preprint arXiv:2409.09491_ , 2024. 

- [42] Kristofer D. Kusano, John M. Scanlon, Yin-Hsiu Chen, Timothy L. McMurry, Tilia Gode, and Trent Victor. Comparison of Waymo Rider-Only crash rates by crash type to human benchmarks at 56.7 million miles. _Traffic Injury Prevention_ , 26(sup1):S8–S20, October 2025. ISSN 1538-9588. doi: 10.1080/15389588. 2025.2499887. URL https://www.tandfonline.com/doi/ full/10.1080/15389588.2025.2499887. 

- [43] Tze Leung Lai. Optimal Stopping and Sequential Tests which Minimize the Maximum Expected Sample Size. _The Annals of Statistics_ , 1(4):659–673, 1973. ISSN 0090-5364. URL https://www.jstor.org/stable/2958310. Publisher: Institute of Mathematical Statistics. 

- [44] Tze Leung Lai. Boundary Crossing Probabilities for Sample Sums and Confidence Sequences. _The Annals of Probability_ , 4(2):299–312, 1976. ISSN 0091-1798. URL https://www.jstor.org/stable/2959164. Publisher: Institute of Mathematical Statistics. 

- [45] Tze Leung Lai. First Exit Times from Moving Boundaries for Sums of Independent Random Variables. _The Annals of Probability_ , 5(2):210–221, 1977. ISSN 00911798. URL https://www.jstor.org/stable/2242894. Publisher: Institute of Mathematical Statistics. 

- [46] Tze Leung Lai. Boundary Crossing Problems for Sample Means. _The Annals of Probability_ , 16(1):375–396, 1988. ISSN 0091-1798. Publisher: Institute of Mathematical Statistics. 

- [47] Tze Leung Lai. Nearly Optimal Sequential Tests of Composite Hypotheses. _The Annals of Statistics_ , 16(2): 856–886, 1988. ISSN 0090-5364. Publisher: Institute of Mathematical Statistics. 

- [48] Tze Leung Lai and Li Min Zhang. Nearly Optimal Generalized Sequential Likelihood Ratio Tests in Multivariate Exponential Families. _Lecture Notes-Monograph Series_ , 24:331–346, 1994. ISSN 0749-2170. Publisher: Institute of Mathematical Statistics. 

- [49] Xuanlin Li, Kyle Hsu, Jiayuan Gu, Karl Pertsch, Oier Mees, Homer Rich Walke, Chuyuan Fu, Ishikaa Lunawat, Isabel Sieh, Sean Kirmani, et al. Evaluating real-world robot manipulation policies in simulation. _arXiv preprint arXiv:2405.05941_ , 2024. 

- [50] Yaxuan Li, Yichen Zhu, Junjie Wen, Chaomin Shen, and Yi Xu. Worldeval: World model as real-world robot policies evaluator. _arXiv preprint arXiv:2505.19017_ , 2025. 

- [51] Michael Lindon and Nathan Kallus. Anytime-Valid A/B Testing of Counting Processes. In _Proceedings of The 28th International Conference on Artificial Intelligence and Statistics_ , pages 3529–3537. PMLR, April 2025. URL https://proceedings.mlr.press/v258/lindon25a.html. 

- [52] Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, and Peter Stone. Libero: Benchmarking knowledge transfer for lifelong robot learning. _Advances in Neural Information Processing Systems_ , 36:44776– 44791, 2023. 

- [53] Ziyuan Liu, Wei Liu, Yuzhe Qin, Fanbo Xiang, Minghao 

Gou, Songyan Xin, Maximo A Roa, Berk Calli, Hao Su, Yu Sun, et al. Ocrtoc: A cloud-based competition and benchmark for robotic grasping and manipulation. _IEEE Robotics and Automation Letters_ , 7(1):486–493, 2021. 

- [54] Jianlan Luo, Charles Xu, Fangchen Liu, Liam Tan, Zipeng Lin, Jeffrey Wu, Pieter Abbeel, and Sergey Levine. Fmb: a functional manipulation benchmark for generalizable robotic learning. _The International Journal of Robotics Research_ , 44(4):592–606, 2025. 

- [55] Rachel Luo, Heng Yang, Michael Watson, Apoorva Sharma, Sushant Veer, Edward Schmerling, and Marco Pavone. Leveraging correlation across test platforms for variance-reduced metric estimation. _arXiv preprint arXiv:2506.20553_ , 2025. 

- [56] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

- [57] Andreas Maurer and Massimiliano Pontil. Empirical bernstein bounds and sample variance penalization. _arXiv preprint arXiv:0907.3740_ , 2009. 

- [58] Jerzy Neyman, Egon Sharpe Pearson, and Karl Pearson. IX. On the problem of the most efficient tests of statistical hypotheses. _Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character_ , 231(694-706): 289–337, January 1997. doi: 10.1098/rsta.1933.0009. Publisher: Royal Society. 

- [59] Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, Kevin Black, Oier Mees, Sudeep Dasari, Joey Hejna, Charles Xu, Jianlan Luo, Tobias Kreiman, You Liang Tan, Pannag Sanketi, Quan Vuong, Ted Xiao, Dorsa Sadigh, Chelsea Finn, and Sergey Levine. Octo: An Open-Source Generalist Robot Policy. 2024. doi: 10.48550/arXiv.2405.12213. 

- [60] Francesco Orabona and Kwang-Sung Jun. Tight Concentrations and Confidence Sequences From the Regret of Universal Portfolio. _IEEE Transactions on Information Theory_ , 70(1):436–455, January 2024. ISSN 00189448, 1557-9654. doi: 10.1109/TIT.2023.3330187. URL https://ieeexplore.ieee.org/document/10315047/. 

- [61] Emanuel Parzen. On Estimation of a Probability Density Function and Mode. _The Annals of Mathematical Statistics_ , 33(3):1065–1076, 1962. ISSN 0003-4851. URL https://www.jstor.org/stable/2237880. 

- [62] Karl Pertsch, Kyle Stachowicz, Brian Ichter, Danny Driess, Suraj Nair, Quan Vuong, Oier Mees, Chelsea Finn, and Sergey Levine. FAST: Efficient Action Tokenization for Vision-Language-Action Models, January 2025. URL http://arxiv.org/abs/2501.09747. arXiv:2501.09747 [cs]. 

- [63] Wilbert Pumacay, Ishika Singh, Jiafei Duan, Ranjay Krishna, Jesse Thomason, and Dieter Fox. The colosseum: A benchmark for evaluating generalization for robotic 

   - manipulation. _arXiv preprint arXiv:2402.08191_ , 2024. 

- [64] Julian Quevedo, Percy Liang, and Sherry Yang. Evaluating robot policies in a world model. _arXiv preprint arXiv:2506.00613_ , 2025. 

- [65] Aaditya Ramdas, Peter Gr¨unwald, Vladimir Vovk, and Glenn Shafer. Game-theoretic statistics and safe anytimevalid inference. _Statistical Science_ , 38(4):576–601, 2023. 

- [66] Glenn Shafer, Vladimir Vovk, and Cs Rhul Ac Uk. A Tutorial on Conformal Prediction. 

- [67] David Siegmund. _Sequential analysis: tests and confidence intervals_ . Springer-Verlag, 1985. doi: 10.1007/ 978-1-4757-1862-1. 

- [68] David Snyder, Asher James Hancock, Apurva Badithela, Emma Dixon, Patrick Miller, Rares Andrei Ambrus, Anirudha Majumdar, Masha Itkina, and Haruki Nishimura. Is your imitation learning policy better than mine? policy comparison with near-optimal stopping. _arXiv preprint arXiv:2503.10966_ , 2025. 

- [69] 1X World Model Team. 1x world model: Evaluating bits, not atoms. Technical report, 1X, 2025. 

- [70] Gemini Robotics Team, Coline Devin, Yilun Du, Debidatta Dwibedi, Ruiqi Gao, Abhishek Jindal, Thomas Kipf, Sean Kirmani, Fangchen Liu, Anirudha Majumdar, et al. Evaluating gemini robotics policies in a veo world simulator. _arXiv preprint arXiv:2512.10675_ , 2025. 

- [71] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ international conference on intelligent robots and systems_ , pages 5026–5033. IEEE, 2012. 

- [72] Wei-Cheng Tseng, Jinwei Gu, Qinsheng Zhang, Hanzi Mao, Ming-Yu Liu, Florian Shkurti, and Lin Yen-Chen. Scalable policy evaluation with video world models. _arXiv preprint arXiv:2511.11520_ , 2025. 

- [73] Rosanne J. Turner and Peter D. Gr¨unwald. Exact anytime-valid confidence intervals for contingency tables and beyond. _Statistics & Probability Letters_ , 198:109835, July 2023. ISSN 0167-7152. doi: 10.1016/j.spl.2023. 109835. URL https://www.sciencedirect.com/science/ article/pii/S0167715223000597. 

- [74] Pierre Van Moerbeke. Optimal Stopping and Free Boundary Problems. _The Rocky Mountain Journal of Mathematics_ , 4(3):539–578, 1974. ISSN 0035-7596. Publisher: Rocky Mountain Mathematics Consortium. 

- [75] Jean Ville. _Etude Critique de la Notion de Collectif_ . PhD thesis, Universite de Paris, 1939. Publisher:GauthierVillars, Paris. 

- [76] Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic Learning in a Random World_ . Springer International Publishing, Cham, 2022. ISBN 978-3-031-06648-1 978-3-031-06649-8. doi: 10.1007/ 978-3-031-06649-8. URL https://link.springer.com/10. 1007/978-3-031-06649-8. 

   - [78] A. Wald and J. Wolfowitz. Optimum Character of the Sequential Probability Ratio Test. _The Annals of Mathematical Statistics_ , 19(3):326–339, 1948. ISSN 00034851. Publisher: Institute of Mathematical Statistics. 

   - [79] Larry Wasserman. _All of Nonparametric Statistics_ . Springer Texts in Statistics. Springer, New York, NY, 2006. ISBN 978-0-387-25145-5. doi: 10.1007/ 0-387-30623-4. URL http://link.springer.com/10.1007/ 0-387-30623-4. 

   - [80] Ian Waudby-Smith and Aaditya Ramdas. Estimating means of bounded random variables by betting. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 86(1):1–27, 2024. 

   - [81] B. L. WELCH. The Generalization of ‘Student’s’ Problem When Several Different Population Variances are Involved. _Biometrika_ , 34(1-2):28–35, January 1947. ISSN 0006-3444. doi: 10.1093/biomet/34.1-2.28. URL https://doi.org/10.1093/biomet/34.1-2.28. 

   - [82] Robert M West. Best practice in statistics: Use the Welch t-test when testing the difference between two groups. _Annals of Clinical Biochemistry_ , 58(4): 267–269, July 2021. ISSN 0004-5632. doi: 10. 1177/0004563221992088. URL https://doi.org/10.1177/ 0004563221992088. 

   - [83] Brian Yang, Dinesh Jayaraman, Jesse Zhang, and Sergey Levine. Replab: A reproducible low-cost arm benchmark for robotic learning. In _2019 International Conference on Robotics and Automation (ICRA)_ , pages 8691–8697. IEEE, 2019. 

   - [84] Lihan Zha, Apurva Badithela, Michael Zhang, Justin Lidard, Jeremy Bao, Emily Zhou, David Snyder, Allen Z. Ren, Dhruv Shah, and Anirudha Majumdar. Guiding Data Collection via Factored Scaling Curves, May 2025. URL http://arxiv.org/abs/2505.07728. arXiv:2505.07728 [cs]. 

   - [85] Gaoyue Zhou, Victoria Dean, Mohan Kumar Srirama, Aravind Rajeswaran, Jyothish Pari, Kyle Hatch, Aryan Jain, Tianhe Yu, Pieter Abbeel, Lerrel Pinto, et al. Train offline, test online: A real robot learning benchmark. _arXiv preprint arXiv:2306.00942_ , 2023. 

   - [86] Zhiyuan Zhou, Pranav Atreya, You Liang Tan, Karl Pertsch, and Sergey Levine. Autoeval: Autonomous evaluation of generalist robot manipulation policies in the real world. _arXiv preprint arXiv:2503.24278_ , 2025. 

   - [87] Fangqi Zhu, Hongtao Wu, Song Guo, Yuxiao Liu, Chilam Cheang, and Tao Kong. Irasim: Learning interactive real-robot action simulators. _arXiv preprint arXiv:2406.14540_ , 2024. 

- [77] A. Wald. Sequential Tests of Statistical Hypotheses. _The Annals of Mathematical Statistics_ , 16(2):117–186, 1945. ISSN 0003-4851. Publisher: Institute of Mathematical Statistics. 

## APPENDIX A 

## ANALYTICAL RESULTS 

In this section, we present the proofs for key theoretical results in the main paper, in the order that they are introduced in Section V. 

## _A. Proof of Lemma 1_ 

Consider the stochastic process increment in Equation (5), interpreted as the ‘approximate marginal evidence increment’ represented in Equation (3). We need to show that: 



The property arises directly out of the boundedness assumption of general progress metrics and the linear separability of _r_ 0 and _r_ 1 in the increment computation. From boundedness on _r_ 0 and _r_ 1, we know that the increment is bounded w.p. 1 in [1 _−ξ,_ 1+ _ξ_ ] _⊆_ [0 _,_ 2]. Therefore, the increment has well-defined moments. 

The exact value can be computed as: 



The last term is precisely the definition of _S_<sup>_−_</sup> ; therefore, we have shown the nonnegative (super)martingale property holds precisely for any instance in which the null hypothesis is true.<sup>5</sup> This argument directly extends to any parametric progress metric setting, due to the nature of the increment construction. Thus, it holds for binary, discrete, and continuous valued bounded metrics. 

## _B. Proof of Theorem 1_ 

We now utilize the results of Section A-A, which demonstrated the equivalent of the nonnegative supermartingale (NSM) property of the evidence aggregation _when the true state of the world lies within the set S_<sup>_−_</sup> , to prove Theorem 1. _1) Verifying Ancillary Conditions:_ Note that by construction, _ξn ∈_ [0 _,_ 1] and ( _r_ 1 _,n − r_ 0 _,n_ ) _∈_ [ _−_ 1 _,_ 1] implies that 



Therefore, 

This verifies nonnegativity. 

> 5If we restrict _ξ ∈_ (0 _,_ 1), then the relation holds bidirectionally, i.e., with _⇐⇒_ . 

_2) Ville’s Inequality:_ Ville’s Inequality is the critical mechanism whereby the expectation of a nonnegative supermartingale process (see Definition 2) can be linked to right-tailed quantiles of its realized behavior. 

**Definition 2** (Nonnegative Supermartingale (NSM)) **.** 

Consider a discrete-time stochastic process _{Xn}n≥_ 0 equipped with the natural filtration _Fs_ = _{Xi}_<sup>_s_</sup> _i_ =0<sup>_−_1,6and</sup> w.l.o.g. let _X_ 0 = 1. The process _{Xn}n≥_ 0 is a **nonnegative supermartingale (NSM)** if it is everywhere nonnegative and contracting in expectation with respect to the filtration: 



Intuitively, an NSM is a ‘stable process’ in that it is lower bounded by 0 and contracting in expectation. This stability is the intuitive mechanism from which Ville’s Inequality arises. 

**Ville’s Inequality [75].** _Let {Xn}n≥_ 0 _be a nonnegative supermartingale. Then for any α ∈_ (0 _,_ 1) _,_ 



The critical interpretation of this result is that, for all _n ≥_ 0, the 1 _− α_ quantile of _Xn_ is upper bounded by E[ _X_ 0] _/α_ for any _α ∈_ (0 _,_ 1). Importantly, this means that the result holds even for optional (i.e., selective) determination of a time of decision.<sup>7</sup> 

_3) Time-Varying ξn:_ We now confirm that the use of timevarying _ξn_ = _g_ ( _Fn−_ 1), measurable with respect to the filtration, do not violate the Type-1 Error bounds in Section A-A. This follows from the definition of the natural filtration and the independence of marginal evaluation outcomes. Specifically, we must modify the proof in Section A-A to account for the conditional dependencies of _ξn_ = _g_ ( _Fn−_ 1) on the previous data. However, the change is minimal due to the independence of _ξn_ with the _new data_ ( _r_ 0 _,n, r_ 1 _,n_ ). We include the modification for completeness: 



The third line follows from the independence of _ξn_ and ( _r_ 0 _,n, r_ 1 _,n_ ), and the maximum in the penultimate line arises from taking the extremal values (0 and 1) of E[ _ξn_ ]. We again observe that membership in the the null hypothesis is precisely sufficient to ensure the NSM property. 

> 6The natural filtration in this context is simply the available information on which a causal algorithm may act. Consistent with this semantic meaning, we note for completeness that _F_ 0 = _{∅}_ . 

> 7In the language of stochastic processes and sequential analysis, the time of decision is often referred to as the “stopping time” of the process. Adaptively selecting to stop and decide or to continue collecting data is then referred to as “optional stopping.” 

_4) Completing the Proof:_ We consider the stochastic process defined in Equation (8) taking _X_ 0 = 1. From Lemma 1 and the ancillary verification, we have that _{Xn}_ is a nonnegative supermartingale on _S_<sup>_−_</sup> . Using Ville’s Inequality, we conclude that, for any possible true state of the world represented by some _h ∈ S_<sup>_−_</sup> , the probability that max _n{Xn}_ exceeds 1 _/α_<sup>_∗_</sup> is less than or equal to _α_<sup>_∗_</sup> . Therefore, using the stopping rule defined in Equation (4), the probability of falsely rejecting any true null _h ∈ S_<sup>_−_</sup> is uniformly bounded by _α_<sup>_∗_</sup> . This is equivalent to the claim of Equation (6). 

## _C. Proof of Remark 1_ 

We describe in more detail the explicit nonparametric representation of the optimization problem for selecting _ξn_ = _g_ ( _Fn−_ 1). As described in Section V, we draw inspiration from kernel density estimation to explicitly model the distribution of outcomes of new evaluation draws. We use a simple version KDE with a preset, uniform binning scheme. That is, we represent the distribution of evaluation scores for each policy _πi_ with _k_ bins partitioning the interval [0 _,_ 1]. For the case of exact partial credit evaluation with _K_ outcomes, these bins can be chosen to precisely model the true underlying distribution when _k_ = _K_ . For nonparametric instances or cases with continuous densities, the choice of _k_ trades off greater accuracy in the representation ( _k ↑_ ) against computational burden (which decreases as _k ↓_ ). 

Importantly: when constructing the martingale increments in Equation (3) the exact (possibly continuously-valued) evaluation scores must be used to certify Type-1 Error control. However, no restriction is made with regard to how said data is used to sequentially construct _ξn_ . Very informally, the algorithm to select the multiplier may ‘deceive itself’ however it likes without violating rigorous validity – it will simply risk being less efficient. This is precisely the key insight – N- SCORE will ‘pretend’ that the data is parametric partial credit (via discretization of the observed performance scores) when choosing _ξn_ , allowing for efficient optimization. Nonetheless, this discretization of the observed data for selecting _ξn_ does not invalidate Lemma 1; it can only affect the efficiency of the process as measured by time-to-decision. This is in _stark contrast with θ_ -SAVI, which requires that the _true underlying distribution_ be of a parametric (i.e., partial credit) form. 

As a concrete example of the binning procedure, utilizing eleven bins, we may sort the data by its first two significant digits. This is equivalent to 



This can then be seen as a lossy compression of the observed data, where we only represent its approximate value: 



The importance of this compression lies in reducing all (highly complex) distributions over general progress metrics to the (parametric) family of categorical distributions over _k_ outcomes, where _k_ is precisely the number of bins. Now, we 

fix the binning procedure to be shared for both policies, and denote the vector of _k_ compressed outcomes to be **c** _∈_ R<sup>_k_</sup> +<sup>.</sup> We will w.l.o.g. assume henceforth that **c** is ordered from least to greatest, and that the elements **c** _i_ are distinct.<sup>8</sup> The true underlying distributions over outcome scores are compressed to vectors on the _k_ -simplex: 



There are various useful quantities which arise from this representation. The probability of each possible joint evaluation outcome (i.e., of _π_ 0 and _π_ 1) can be simultaneously represented as a _k × k_ square matrix _P_ : 



where _Pij_ is understood to be ‘the probability that, for a new evaluation draw, _π_ 0 gets a (compressed) score ˜ _r_ 0 _,n_ = **c** _i_ and _π_ 1 gets a (compressed) score _r_ ˜1 _,n_ = **c** _j_ .’ Furthermore, the set of approximate evidence integrator outcomes can be represented by a _k × k_ square matrix _A_ , where: 



To link this to Lemma 1: in the special case of discrete partial credit structure, Lemma 1 amounts to demonstrating that the following statement is true _under the null_ : 



Conversely, Lemma 1 is sufficient to demonstrate that the above statement must be true, as the latter follows from the generality of the former.<sup>9</sup> The key point here is that this is precisely a stability condition on the expectation of the evidence aggregator _when the true state of the world is an element of the null set S_<sup>_−_</sup> _._ The optimization of _ξn_ , by contrast, relates to optimally _de-stabilizing_ the evidence aggregator when the the true state of the world is an element of the alternative set, _S_<sup>+</sup> . In that setting, we very much wish for the expectation to be _greater than one_ , in contrast with Equation (16). 

_1) Intuition for Optimizing ξ:_ With the preceding development, our KDE-inspired approach attempts to optimize _ξ_ over the lossy representation induced by the discretization (i.e., the nonparametric distribution representation as, approximately, a discrete partial credit random variable).<sup>10</sup> Unlike in verifying 

> 8Distinctness is not restrictive; if any set of (semantic) outcomes has the same evaluation score, then they can be ‘lumped together’ into a single composite outcome. The binning procedure itself is assumed to be a deterministic function of the evaluation outcome; therefore, it will always ensure distinction between outcomes it observes. The particular semantic meaning of a score, however, may not be directly observable. 

> 9This can be shown independently using properties of the matrix _A_ and some linear algebraic identities, but is outside the scope of the core intuition. 

> 10Doing this ever-more efficiently is precisely a subject of future work, as much of the specific domain knowledge of KDE is not present in our simplified implementation. 

the NSM property (Lemma 1), the linear algebraic representation of the partial credit problem provides insight into choosing _ξn_ . Recall that the choice of _ξn_ does not affect Type-1 Error, and therefore does not affect any state of the world in which the null is true. Therefore, it will only be used to accelerate detection when the state of the world is such that the alternative is true. The core idea is to observe two phenomena arising out of realizations of _Aij_ : the ‘signal effect’ and the ‘hysteresis effect.’ 

_2) Signal Effect:_ The ‘signal effect’ amounts to direct evidence for the alternative. This arises when _r_ 1 _,n > r_ 0 _,n_ ; when this is the case, the multiplier ∆ _n_ grows with _ξn_ . Thus, greater likelihood of seeing positive differences in the metrics (‘positive signals’) promotes _increasing_ the value of _ξ_ . This is linear in the _asymmetric component_ of _P_ , in the following sense. Define 



and 0 otherwise. By definition, ∆ _P_ is an upper triangular matrix. In general, if the matrix has more _positive_ elements, this is evidence that the alternative is more likely to be true. That is, ∆ _Pij >_ 0 for some _i < j_ means that the probability of observing _r_ 1 _,n − r_ 0 _,n_ = **c** _j −_ **c** _i >_ 0 is _larger than_ the converse of _r_ 1 _,n − r_ 0 _,n_ = **c** _i −_ **c** _j <_ 0. Considering all pairs ( _i, j_ ), we observe that ∆ _P_ precisely encodes _asymmetry_ in _P_ and its contribution to differences in the mean performance of _π_ 0 vs _π_ 1. Considering the expected martingale growth rate, we can observe now that this contributes to the growth linearly in _ξ_ : 



Therefore, the aggregate positive evidence that _π_ 1 is better than _π_ 0 is the sum of these pairwise effects: 



As noted previously, the key idea of N-SCORE is to estimate the quantity ∆ _P_ from the data currently observed (i.e., the filtration _Fn_ ) to choose an effective _ξn_ . 

_3) Hysteresis Effect:_ The signal effect generally pushes _ξn_ to be larger; by contrast, there is an opposing mechanism which induces it to shrink. This relates to the _symmetric_ component of the _P_ matrix, and is termed the ‘hysteresis effect.’ This effect is so named because of how it manifests: symmetric aspects of _P_ correspond to ‘self-negating’ outcomes (e.g., in which _r_ ˜1 _,n − r_ ˜0 _,n_ = _−_ (˜ _r_ 1 _,n−_ 1 _− r_ ˜0 _,n−_ 1). Direct inspection should convince the reader that difference in empirical performance between the policies has not changed from step _n −_ 2 to step _n_ (each has observed the same total return since step _n −_ 2). However, in the course of cycling through zero net change in mean performance difference, the 

value of _Xn_ has _decreased_ from _Xn−_ 2. Achieving both of the converse outcomes (i.e., ( _i, j_ ) and ( _j, i_ )) is reflected in the _symmetric component_ of _P_ : the fraction of realizations of _Aij_ which will be ‘counteracted’ by realizations of _Aji_ . As just stated, these pairs of outcomes do not change the empirical gap between the policies, but they _negatively impact_ the _Xn_ . The idea of losing value (in _Xn_ ) via a closed loop in net performance difference motivates the term ‘hysteresis.’ Mathematically, we first define 



This symmetric matrix quantifies the degree to which hysteresis plays a part. The effect on the stochastic process value can be observed via approximate Taylor Expansion (assuming for now that _ξn_ is slowly varying): 



This term acts to regularize the choice of _ξn_ , because it suggests that, even with no net gain of information, the stochastic process will tend to decay, and that this decay is larger when _ξn_ is larger. Thus, hysteresis motivates a smaller _ξn_ , opposing the signal effect. However, importantly, unlike the signal effect, the hysteresis effect is quadratic in _ξ_ . At an informal level, this is suggestive of maximizing a concave quadratic function over a convex domain, which is a convex optimization problem. Continuing the informal discussion, this suggests that the signal effect (which is linear) will always locally dominate and _ξn_ will never be forced to zero when the means differ favorably. 

**Remark 2** (Linearity of _<u>P</u>_ _~~i~~ j_<sup>)</sup><sup>**.**Theoptimizationof</sup><sup>_ξn_isim-</sup> plicitly single-step, which should not be suboptimal given the temporal independence of evaluation outcomes. The weighting of the hysteresis terms arises from understanding each component in the single-step context. That is, evaluation outcomes are partitioned as “an observation ( _i, j_ ) which will be balanced out by an associated ( _j, i_ )” (hysteresis) versus “an observation ( _i, j_ ) which will _not_ be balanced out by an associated ( _j, i_ )” (signal). Of course, the outcomes which will cancel in the future are twice _<u>P</u>_ _~~i~~ j_<sup>(because one can get either the contribut-</sup> ing ( _i, j_ ) outcome _or_ the ( _j, i_ ) outcome), but the fact that _both_ outcomes are required to achieve hysteresis means that each individual observation (that is, ( _i, j_ ) xor ( _j, i_ )) should be weighted _by one half_ . Thus, the appropriate weighting in the right-hand term in Equation (20) is precisely _<u>P</u>_ _~~i~~ j_<sup>,asopposed</sup> to either _<u>P</u>_ 2 _~~i~~ j_<sup>(whichisnotsingle-step)or2</sup><sup>_<u>P</u>_</sup> _~~i~~ j_<sup>,whichdoes</sup> not take into account the fact that _both outcomes_ are needed for hysteresis to occur. 

_4) The Optimization Problem:_ With the preceding development, we attempt to maximize the log-value of the stochastic 

process via single-step optimization, given the currently available information. 

Breaking this down: the log-value of _Xn_ is precisely the sum of the log ∆ _i_ , per the definition of the evidence integrator in Section V. The available information manifests as 



which represents the empirical distribution of the observed results. Each **p** ˆ _i_ can be computed by simply calculating the empirical frequency of occurrence of each bin. Thus, the approximate expected multiplier value (given the current available information) is _⟨A, P_<sup>ˆ</sup> _⟩_ . Lemma 1 guarantees that this expectation is bounded by 1 when the null is true; we are interested, however, precisely in the case where the alternative is true. In that setting, the bound does not apply. 

Due to the linearity of the inner product, the optimization essentially acts elementwise on _P_<sup>ˆ</sup> -weighted elements of log _Aij_ : 



Applying first-order optimality conditions, we obtain an efficient representation for which a root-finding procedure on [0 _,_ 1] quickly converges: 



This can be understood as choosing the optimal _ξn_ to maximize the expected growth rate of _Xn_ under the currently available estimate of the distributions **ˆp** _i_ . This choice explicitly balances the signal and hysteresis effects in order to achieve this maximization. Further, though it is beyond the scope of the present work, it is believed that the nominal objective is in fact concave (via analysis of the second-order shape of the objective). Thus, the current approach is likely sufficient despite only the first-order verification; additionally, faster approaches are likely feasible. Regardless, this proves the necessary result, and describes the practical optimization scheme used for N- SCORE in all experiments. 





## _A. Waudby-Smith Ramdas Confidence Sequences_ 

The Waudby-Smith-Ramdas (WSR) procedure [80] provides time-uniform, non-parametric, and non-asymptotic confidence sequences for mean estimation. Suppose we wish to estimate the mean _µ_<sup>_∗_</sup> of a bounded random variable _Z_ using a sequential stream of observations _Z_ 1 _, Z_ 2 _, . . ._ . A confidence sequence is a sequence of confidence intervals _{CIt}_<sup>_∞_</sup> _t_ =1<sup>such</sup> that 

where _α_ is a pre-specified error budget and _CIt_ = [ _lt, ut_ ] _⊆_ R are intervals. Algorithm 2 gives an overview of confidence sequence estimation. The WSR procedure typically provides tighter bounds in the same number of samples than other nonparametric concentration methods such as Hoeffding [30] and empirical Bernstein bounds [57]. We apply WSR to sequential policy comparison by constructing confidence sequences on the difference in evaluation scores of the two policies. That is, we estimate the mean of the sequence _Zn_ = ( _r_ 1 _,n − r_ 0 _,n_ ), which denotes the difference in evaluation scores. If the time-uniform sequence ever excludes 0, then there is strong evidence that the policies are significantly different from each other. Specifically, if the interval is entirely negative, it is evidence for the null; if positive, evidence for the alternative. The test is thus formed by constructing the confidence sequence and stopping precisely at arg min _t∈_ N _{t_ : 0 _∈/ CIt}_ . 

**Algorithm 2** Waudby-Smith–Ramdas (WSR) procedure for Confidence Sequences [80] 

**Require:** Data _{Z_ 1 _, . . . , Zn}_ , error level _α ∈_ (0 _,_ 1), range [ _L, U_ ] such that _Zi ∈_ [ _L, U_ ] 

**Ensure:** Confidence sequence _CS_ for the mean 

1: Confidence Sequence _CS ←{}_ 

- 2: **for** _i ←_ 1 **to** _n_ **do** 

3: _Zi ←_ ( _Zi − L_ ) _/_ ( _U − L_ ) // Normalize to [0 _,_ 1] 

- 4: **end for** 

- 5: _c_ = 0 _._ 95 // Hyperparameter for computing martingales 

- 6: Construct fine grid _M_ grid over [0 _,_ 1] 

7: Initialize set of candidate means _A ← M_ grid 

- 8: **for** _t ←_ 1 **to** _n_ **do** 



- 21: _CIt_ = �max _{_ 0 _,_ min _Cα},_ min _{_ 1 _,_ max _Cα}_ � 22: Append _CIt_ to _CS_ 23: **end for** 

- 24: **return** _CS_ 



|Comparison _→_<br>Task _↓_<br>Method _→_|**PPO**<br>WSR|**vs. TD3**<br>N-SCORE|**PPO **<br>WSR|**vs. DDPG**<br>N-SCORE|**PPO **<br>WSR|**vs. SAC**<br>N-SCORE|**SAC **<br>WSR|**vs. DDPG**<br>N-SCORE|**TD3 **<br>WSR|**vs. DDPG**<br>N-SCORE|**SAC**<br>WSR|**vs. TD3**<br>N-SCORE|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Ant-v4|69|60|27|21|13|12|10|9|21|19|14|13|
|HalfCheetah-v4|10|9|8|8|8|7|40|38|26|23|18|15|
|Hopper-v4|142|79|13|12|46|41|17|14|11|10|30|20|
|InvertedPendulum-v4|39|39|677|267|39|39|46|46|46|46|–|–|
|Humanoid-v4|8|7|42|40|8|7|8|8|8|8|96|89|
|Walker2d-v4|25|25|23|22|12|11|8|7|11|10|24|22|
|Pusher-v4|70|61|89|77|56|47|133|109|294|237|249|220|
|Total (14000 nominal)|726|**560**|1758|**894**|364|**328**|524|**462**|834|**706**|2862|**2758**|



TABLE A.I: **Empirical time-to-decision for all** **_reinforcement learning_ pairwise policy comparisons on Mujoco benchmark tasks using WSR and N-SCORE.** If a decision is not reached, the entry is left blank; for the purpose of computing evaluation savings, any blank entry is counted at _N_ trials. All simulated tasks utilize _N_ = 1000. Thus, as there are two algorithms being compared pairwise, the total number of batch trials for each column is 14k. Due to not being optimized for policy comparison, WSR requires more trials to reach a decision, uniformly across tasks and learning algorithms. Though performance is similar in the low-variance regime (small TTD, or ‘easy problems’), there are multiple instances where significant variation in timeto-decision arises due to this suboptimal multiplier selection, most notably with _PPO vs DDPG_ on InvertedPendulum-v4. 



Fig. A.1: **Number of trials required to separate RL policies on InvertedPendulum-v4.** This is one of the most stark instances of disparity between N-SCORE and WSR, the latter of which requires significantly more evaluation effort (by nearly a factor of three) to reach a decision. 

## APPENDIX C ADDITIONAL EXPERIMENTAL RESULTS 

## _A. Real Valued Continuous Metrics (RL Baselines)_ 

The following experiments demonstrate that we can apply N-SCORE to compare rich behavioral properties of robot policies quantified by continuous metrics such as jitter, smoothness, and stability, that are not easily represented in discrete, partial scoring rubrics. We use N-SCORE to differentiate between RL policies trained via different canonical algorithms on Mujoco benchmark tasks. Variation in reward structure and order of magnitude is significant across tasks, and the rewards themselves are complex, often continuous, and span multiple orders of magnitude at convergence to benchmark performance (see Table A.II).<sup>11</sup> Due to this complexity, the WSR procedure is the only applicable baseline, as the distribution over evaluation rewards is nonparametric. We train RL policies on Mujoco benchmarks using the CleanRL library [31]. Policies 

are trained for 10<sup>6</sup> global steps. Mean policy rewards are averaged over 1000 independent episodes using a frozen policy post-training. Table A.II lists the average episodic return of the various policies, which are comparable to SOTA training curves listed in Spinning Up RL baselines [1]. Figure A.2 shows the the trials required for each benchmark to separate all RL policies in a multi-policy comparison setting where the global error tolerance _α_ = 0 _._ 05 is split between six pairwise comparisons. Figure A.1 illustrates the time to separation for InvertedPendulum-v4. In this case, both N-SCORE and WSR cannot distinguish between SAC and TD3, which have an average empirical performance of 1000 and 998, respectively. Both policies attain the maximum possible reward for this benchmark, making it statistically impossible to distinguish in a 1000 trials. Table A.I lists the time-to-decision on pairwise comparison of policies, showing significant savings of N- SCORE over WSR in the number of trials required, most notably saving over 800 trials in the comparison of DDPG and PPO. In total, from a nominal simulation burden of 28k batch evaluation rollouts, N-SCORE requires approximately 5600 evaluations to make all necessary comparisons (savings of over 80%), while WSR requires approximately 7100 evaluations. These each reflect strong savings over batch methods, while N- SCORE displays an additional 20% improvement in total sample complexity over the entire RL evaluation process. 

## _B. Binary vs. Continuous Valued Metrics_ 

We add further validation to the empirical observation of Section VI – that partial credit evaluation tends to improve average time-to-decision on practical evaluation problems – by comparing the times-to-decision of STEP [68] on binary success data from [6] with times-to-decision of N-SCORE on equivalent partial credit data taken from the same evaluations. We emphasize that the evaluation burden of using partial credit measures is essentially identical to success measures, so the added informativity (and reduction in necessary evaluation trials), can be realized for free. 

To illustrate this, we rerun multi-policy comparisons in the setting of [6], but using instead the associated binary eval- 

> 11For additional details on the structure, see, e.g., the implementation of [31]. 







<!-- Start of picture text -->
(a) Ant (b) Half Cheetah<br>(c) Hopper (d) Humanoid<br>(e) Pusher (f) Walker2D<br><!-- End of picture text -->

Fig. A.2: **Violin plots and the number of samples required for N-SCORE and WSR on multi-policy comparison of RL policies on Mujoco benchmarks.** Policies with different letters are statistically distinguishable by the method. Policies are compared at a global error bound of _α_ = 0 _._ 05 with a Bonferroni correction. In all cases, N-SCORE results in the same comparison conclusions as WSR with fewer samples, demonstrating its broadly improved efficiency. These results also serve as an alternate visualization of the time-to-decision results in Table A.I. 

uation metrics. The resulting times-to-decision are shown in Figure A.3. STEP is maximally sample efficient on Bernoulli scores at 1979 total evaluation trials, but fails to separate two of the policies. In contrast, the total sample complexity for N- SCORE on continuous progress scores is 1419, a savings of 560 evaluation trials. Furthermore, N-SCORE achieves these savings with higher empirical power, correctly separating every policy (i.e., giving a statistically significant _complete ordering_ of the performance of the policies). 

we present the anytime-valid p-values against the number of trials, in both continuous and binary metrics. While both WSR and N-SCORE are sequential procedures that carry a notion of an anytime-valid p-value, the STEP procedure does not; when STEP rejects the null hypothesis, it is due to the p-value dropping below the error threshold for the comparison. Figures A.4 and A.5 plot the anytime-valid p-value against the number of trials in the pairwise policy comparisons from RoboArena data under both continuous progress and binary task success 

To further illustrate the time-to-decision of a test procedure, 



Fig. A.3: **Continuous task progress scores enable faster policy comparison on RoboArena policy evaluation data** . Violin plots and time-to-decision for multi-policy comparison from RoboArena evaluations. _Left:_ Policy comparison under continuous scores with N-SCORE. _Right:_ policy comparison under Bernoulli scores with N-SCORE, WSR, and STEP. In the Bernoulli comparison setting, none of the methods are able to distinguish all the policies. Even though STEP is maximally efficient on Bernoulli comparisons, N-SCORE on continuous progress requires fewer total trials to distinguish policies. We emphasize that the partial credit and binary metrics arise _from the same rollouts_ of each policy; the partial credit thus reflects precisely a more informative ‘representation’ of the rollout for evaluation purposes. The reduced time-to-decision and increased power (separating all of the policies successfully) highlights the fundamental advantage of fine-grained task progress scores over sparse binary success rates for efficient policy comparison. As can be observed in Figure 2 in the main text, N-SCORE also significantly reduces the time-to-decision with respect to WSR. The former requires approximately 1420 trials, while the latter needs an additional 450, while failing to distinguish _π_ 0 from _PG-Diff_ . 

|Task|DDPG|TD3|PPO|SAC|
|---|---|---|---|---|
|Ant-v4|418.8|2477.5|1849.0|4901.8|
|HalfCheetah-v4|9932.2|7782.5|1332.2|11759.0|
|Hopper-v4|1106.4|3234.6|2797.4|2488.7|
|InvertedPendulum-v4|927.2|998.6|848.2|1000.0|
|Pusher-v4|-38.5|-35.7|-47.6|-32.4|
|Walker2d-v4|1732.5|3513.4|1679.8|4544.1|
|Humanoid-v4|1386.0|5288.2|748.4|5042.7|



TABLE A.II: **Empirical mean episodic return on evaluation instances for Mujoco benchmark tasks.** Note, in tandem with Figure A.2, that the distributions over rewards near optimality vary significantly in shape and scale. This emphasizes the generality of nonparametric procedures and their broad applicability to creative or nonstandard metrics of robot performance or behavior. 

score setting, the empirical performance gap shrinks (as shown in Figure A.3), making it harder to distinguish and requiring more trials than the continuous progress setting. Furthermore, even when the Bernoulli performance gap is substantial, such as in the case of _π_ 0-FAST-DROID vs. PG-Bin-DROID which differ by around 20% points, the p-values of the tests require around 80 trials to gather sufficient statistical evidence of distinction (see Figure A.4c). Intuitively, for the same performance gap, the signal-to-noise ratio is relatively higher in continuous progress settings because the empirical variance of continuous scores is no greater than the empirical variance of the corresponding Bernoulli scores. These results illustrate that N-SCORE and WSR are able to leverage the rich information captured in continuous evaluation scores to distinguish policies faster than Bernoulli scores. 

settings. Due to multi-test correction, the total error budget of _α_ = 0 _._ 05 is split between the six pairwise comparisons, resulting in an allocation of _α_ = 0 _._ 0083 each. A test procedure terminates when the p-value is at or below the error threshold. In Figure A.4, we illustrate time-to-decision under large gaps in the empirical performance of policies. Here, we compare policies to PG-Binning-DROID policy which has the lowest empirical performance in RoboArena, up to 30% points lower than other policies on continuous task progress. For both NSM and N-SCORE, the p-value quickly approaches the error threshold in 18 trials, consistent with the reported time-todecision illustrated in Figure 2. However, in the Bernoulli 

In Figure A.5, we plot the progression of p-values for comparisons where the performance gaps between policies are small (around 10% or lower). N-SCORE in the continuous task progress setting is the fastest in distinguishing the policies and WSR in the binary metric setting is the slowest. In the comparison shown in Figure A.5b, N-SCORE even in the binary metric setting requires fewer trials to distinguish than WSR with continuous scores. In the comparisons shown in Figures A.5a and A.5c, while both N-SCORE and WSR with binary metrics fail to distinguish policies within 641 trials, the p-value of N-SCORE is much closer to the _α_ - threshold than WSR. For a valid multi-policy comparison, we split the error budget and apply a Bonferroni correction to control for type-I error across all pairwise comparisons at the 

cost of reduced statistical power. In future work, we plan to investigate efficient multi-test correction methods to proportionally allocate the risk budget. This would be complement our current work, enabling further efficiency gains. 

Finally, we make an additional observation on the trends of anytime-valid p-values of WSR and N-SCORE. As seen in Figures A.4 and A.5, WSR p-values under either metric can show a steeper decrease initially, but p-values of N- SCORE ultimately approaches the risk threshold first. We attribute this efficiency to our optimization of the betting coefficient _ξn_ for policy comparison. In contrast, the betting coefficients for WSR (line 11 of Algorithm 2) are not optimized for policy comparison. 

## _C. Data Independence in Robot Policy Evaluation_ 

Robot policy evaluations can be conducted in several ways, differing in how evaluation environments are sampled due to logistical feasibility. We clarify these distinctions for a better understanding of statistical assumptions and interpretation of evaluation results. In all of the following evaluation settings, we wish to estimate policy performance over some environment distribution _D_ env. 

In the first setting, suppose the evaluator wishes to compare policies on a specific environment (i.e., a single initial condition), which is useful in discerning whether one policy succeeds while the other one fails more consistently in that particular setting. This corresponds to a degenerate environment distribution, in which we evaluate both policies on the same environment all the time. Despite the deterministic environment selection in this context (arising from the distribution degeneracy), our method remains valid because identical environments amount to i.i.d. samples in this special case. 

In the second setting, the evaluator samples an environment i.i.d., and runs a single trial of every policy on that same environment before moving on to sample a new initial condition. This is useful in collecting pairwise preferences and is logistically easier for the evaluator to reset to the same environment for all policies<sup>12</sup> . This is the evaluation scheme adopted in RoboArena [6]. 

In the third setting, the evaluator samples an environment i.i.d. with replacement for each trial and for each policy. For rich environment distributions, it is important to gather independent data from each trial for statistical inference. Specifically, this implies that the environment at trial _n_ for policy A might be different from that of trial _n_ of policy B. While this ensures i.i.d. sampling, the frequencies of various initial conditions might not be equal across policies. 

A separate but important scheme is one that is exchangeable but not i.i.d. Often, this arises from stratification over an auxiliary variable – for example, forcing the _N_ evaluations to be split equally so as to have exactly _N/L_ evaluations in each of _L_ task contexts. Stratification often induces implicit 

> 12This is of course only theoretical: resets are inherently imprecise due to small errors in resetting the environment, small perturbations in camera poses, etc. This is discussed in more detail in, for example, [41]. 

sampling without replacement to ensure that all policies see all _L_ ‘types’ of initial conditions at exactly the same frequency, rather than the softer i.i.d. constraint of them having the same _expected_ frequency, but allowing the frequency to vary in finite samples.<sup>13</sup> Very concretely: if 100 evaluations are to consider a distribution that perturbs a target object or the background lighting color, stratification forces 50 evaluations _exactly_ for changes in target object and 50 evaluations _exactly_ for changes in background lighting. For truly i.i.d. data, this context itself is random, and we might observe, say, 55 of one and 45 of the other in a given evaluation sample. This exchangeable-but-noti.i.d. scheme is adopted in Barreiros et al. [9]. While slightly weaker than i.i.d., any potential effects due to the deviation from the i.i.d. assumption are practically negligible as long as all the policies are evaluated on each ‘type’ of environment a sufficient number of times (i.e., when _L_ is small relative to _N_ ). 

The importance of independence, and the challenge of _L ≈ N_ with respect to the second setting, is clarified as follows. If there are latent or hidden correlations between different policies’ performance levels with respect to the draw of the particular environment, then the variance of the difference in observed performance will be inflated<sup>14</sup> . Without accounting for this inflation, collecting results in the second setting could result in test procedures being overly optimistic, violating Type-1 Error control. When _L_ is smaller, it implies more independence in the _N/L_ evaluations per _L_ ‘types’ or ‘contexts,’ reducing the non-i.i.d. bias in practice. For small stratification in particular these effects are often small – especially when the space of environments is very highdimensional (i.e., covariances tend to diffuse in those spaces in practice). Therefore, for the purposes of running our evaluation algorithms, we do not attempt to correct for this phenomenon in the data, but we do note its presence. We hope that greater uptake of statistical uncertainty-aware evaluation procedures will also promote evaluation protocols that optimize for these considerations. 

To partially address the preceding point, we note a simple post-hoc correction to obtain truly i.i.d data from existing evaluations collected under the second setting. Recall that in this case, we have an ordered list of initial conditions (possibly with randomization and duplicates), and all the policies have been evaluated in this same order. For each initial condition in this list, we sample a policy at random and record its score, and ignore the evaluation outcomes of all other policies in the same round. Thus, if we have _N_ trials (and corresponding environments) and _K_ policies, we will have an effective sample size of _N/K_ , on average, for each policy. One can then apply test procedures such as N-SCORE and WSR on the reduced sample size of _N/K_ evaluations. In essence, to 

> 13RoboArena is again a special case, taking _L_ = _N_ . 

14This can be intuitively seen if we imagine that the policies are negatively correlated, using the simple identity Var( _R_ 1 _− R_ 0) = Var( _R_ 1) + Var( _R_ 0) _−_ 2Cov( _R_ 1 _, R_ 0). If the covariance is negative, the variance is amplified. If environments are chosen instead to be i.i.d. per trial _and per policy_ , then this covariance is precisely fixed to be 0. 









<!-- Start of picture text -->
(b) π 0-DROID vs. PG-Bin-DROID (c) π 0-FAST-DROID vs. PG-Bin-DROID<br><!-- End of picture text -->

(a) PG-Diff-DROID vs. PG-Bin-DROID 

Fig. A.4: **Anytime-valid p-values vs. number of trials on multi-policy comparisons on RoboArena. A test procedure terminates when its p-value is at or below the error threshold** _α_ **. As can be seen, it is faster to distinguish policies under task progress metrics as opposed to binary metrics when the policy performance gap is large.** PG-Binning-DROID has an empirical mean that is more than 30% points lower than _π_ 0-DROID, _π_ 0-FAST-DROID, and PG-Diff-DROID. 









<!-- Start of picture text -->
(a) π 0-DROID vs. PG-Diff-DROID (b) π 0-DROID vs. π 0-FAST-DROID (c) π 0-FAST-DROID vs. PG-Diff-DROID<br><!-- End of picture text -->

Fig. A.5: **Anytime p-values of test procedures on multi-policy comparisons on RoboArena data with small gaps in empirical performance of the policies.** A test procedure terminates when its p-value is at or below the error threshold _α_ . In this regime, binary metrics often fail to obtain a significant result at all, whereas methods that exploit more informative measures can stop significantly more quickly. 

robustly account for potential (worst-case) correlations in the realized environments, we must deflate the sample size by a factor of _K_ , where _K_ is the number of policies being evaluated. However, this is generally inefficient as compared to simply resampling an environment configuration for each policy in turn, and should therefore only be undertaken _posthoc_ (i.e., given that the data has already been collected in the aforementioned manner). 

