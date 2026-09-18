# kress_gazit_policy_eval_2024 — Robot Learning as an Empirical Science: Best Practices for Policy Evaluation (Kress-Gazit, Hashimoto, Kuppuswamy, Shah, Horgan, Richardson, Feng, Burchfiel; Cornell / Toyota Research Institute, arXiv 2024)

sources: papers/md/kress_gazit_policy_eval_2024.md [48978e4b] ; no code

## One-line contribution
Position paper: success rate alone, reported without trial counts, initial conditions, success criteria, statistics or failure narrative, is insufficient; proposes best practices for experiment setup, complementary metrics (rubrics, STL robustness, smoothness), statistical analysis and reporting, illustrated on physical Franka BC policies (Abstract; Sec. 1 "Contribution").

## Setting
- hand(s): n/a: position paper. Illustrative data uses Franka Emika Panda arms with parallel gripper (single arm for Bowl; two arms for Pancake and Shirt; bimanual robot in the Appendix 6.4 energy-bar report) (Sec. 1 "Data used in this paper"; Sec. 6.4).
- simulator / physics: n/a: physical experiments only. "all the best practices discussed are applicable to evaluation in simulation. Some aspects of the evaluation become straight forward, for example ensuring identical initial condition and environmental state (lighting, friction, etc) and automating all the metrics, at the expense of needing to reason about the sim-to-real gap." (Sec. 5 "Simulation")
- observation: policies are treated as black boxes; they "differ in architecture, observation space, and hyper parameters" (Sec. 1).
- action space: not stated.
- objects / data: three tasks, all BC from the same human teleop demos per task: Push Bowl (6 policies), Flip and Serve Pancake (3 policies), Fold Shirt (2 policies) (Sec. 1, Fig. 1). Bowl had 154 demonstrations (Table 2).

## Method
- paradigm: evaluation methodology; the case-study policies are behavior cloning (Sec. 1). algorithm: not disclosed by design ("we treat their implementation details as black-boxes").
- reward or loss: n/a: position paper. The proposed computable metric is STL robustness; example spec for Bowl, verbatim: "□((contact > 100) → (z > 0.25))" — "at all times, whenever the robot is making contact, the value of z must be greater than 0.25" (Sec. 3.2.1, Example 4). Robustness computed with the RTAMT library (Sec. 3.2.1). Energy-bar report spec: "□((gripper_diff ∗ 1000 > 9) → (z < 0.25))" (Sec. 6.4.2).
- key trick(s): two metric families — "semantic information" (Yes/No: success, subgoal rubric, failure modes) and "performance metrics" (continuous: STL robustness, smoothness via SPARC and velocity-peak count) (Sec. 3). Bayesian estimation of the success probability with a uniform prior instead of a point estimate (Sec. 4.2).

## Evaluation
- metrics (exact definitions):
  - Success rate: "the percentage of autonomous runs that were successful" (Sec. 1); requires "a clear, detailed, and unambiguous definition of success" (Sec. 2.1).
  - Rubric: per-task list of Yes/No sub-goal questions "filled out by the evaluator during the evaluation"; some items task-agnostic, e.g. "did the robot exhibit unexpected collisions" (Sec. 3.1.1).
  - STL robustness: "A positive robustness indicates that the formula is True, negative that it is False"; quantifies "how close the formula is to satisfying or violating the formula" (Sec. 3.2.1).
  - SPARC (SPectral ARC length) over speed profiles: "the more negative the value, the less smooth the trajectory is" (Sec. 3.2.2); velocity-peak count: "more peaks correspond to longer and less smooth trajectories" (Sec. 6.4.2).
- headline numbers (with the table/figure they come from):
  - Table 1 (Pancake rubric, Y/N): overall success A 15/3, B 11/6, C 4/19; both spatula pick-ups and pancake flip 18/0, 17/0 (flip 16/1), 23/0; "picked up pancake" 15/3, 12/5, 5/18. Caption: Policy C's overall rate is 17% yet it completes spatula grasp and flip "100% of the time".
  - Example 1 (Fig. 2, Shirt): overall success A 72% vs B 80% over 5 ICs x 5 runs each; "for ICs 0,1,2 both policies always succeed, while for IC 3 they mostly fail".
  - Example 2: after a lab reorganisation, policy A on the same ICs went from 13/20 (65%) to 0/8 (0%) (8 runs, 2 each on ICs 0,1,3,4).
  - Example 6 (Fig. 6): Pancake A 83.3% (15/18) vs B 64.7% (11/17); Bayesian posterior with uniform prior gives "a .11 probability that B actually performs better than A". Fig. 7: same rates at 5/1 vs 6/3 (weaker) and 150/30 vs 110/60 (a difference of 0 "no longer in the support of the histogram").
  - Example 5 (Fig. 4): SPARC for policy 2 on Bowl ranged −2.72 to −11.13; both extremes were successes, taking 4 s vs 15 s.
  - Example 7: Bowl miss-the-bowl failure — policy 5 had 9 such failures; policies 1,2,3 had none.
  - Table 2 (Bowl, 154 demos): A 18/10, B 12/6, C 13/6 successes/failures.
  - Appendix 6.4 report: A 13/20 (0.65) vs B 14/20 (0.7); "we cannot state that one policy outperforms the other" (Fig. 11). Failures: A 6/7 grasp failures; B picked up the bar 20/20 but 6/6 failures were misplacement.
- baselines beaten: n/a; the paper explicitly makes no claim about which policy is better.
- real robot? Yes, all data is physical Franka Panda; trial counts per policy range from 8 to 28 (Tables 1, 2; Examples 1, 2; Sec. 6.4.1). No dexterous hand.

## Concrete recommendations (verbatim, for the survey's evaluation section)
- Success criteria (Sec. 2.1): "there must be a clear, detailed, and unambiguous definition of success."
- Experimental process (Sec. 2.3), four bullets:
  1. "Defining detailed success criteria ahead of time for overall success and semantic metrics ... We advocate for the behavior designer to be the person writing the criteria, but not the person evaluating - that way it is easier to detect ambiguous or incomplete descriptions."
  2. "Reducing, as much as possible, the unintended variability in environmental conditions between different policy rollouts, especially in the initial conditions. This can be done by matching initial conditions using image overlays or markings in the scene, and ensuring policies are evaluated in the same session so lighting and other environmental conditions are more likely to be the same."
  3. "A/B testing, i.e., interleaving policy rollouts when comparing different policies in a way that is blind to the evaluator. This means evaluating all of the policies within one session, as opposed to different policies in different sessions; this will mitigate unintended bias from the evaluator since they will not know which policy is running."
  4. "Ensuring consistency across evaluators and separating the role of demonstrator and evaluator. ... separating the roles and ensuring the same person (or group of people) performs all the evaluations will create a more consistent assessment of the policies."
- Initial-condition axes named (Sec. 2.2): "object types and locations in the environment, lighting conditions and camera locations"; drift sources "object placements, environmental shifts such as sunlight, background changes".
- Reporting checklist (Sec. 4.1): "every experimental evaluation provide the following information: 1) a clear description of the semantic metrics, i.e. an explicit description of what is considered a success overall and in subgoals, 2) the number of evaluations performed across each condition and not just percentages (see Section 4.2), 3) the timing of the evaluations, i.e. were all the policies evaluated in an A/B fashion, were they evaluated in one session, were evaluations performed across different days/weeks, and 4) information regarding the initial conditions; visually as in Examples 1 and 8 or as in [44] (Fig.8), or in a narrative form." Plus: "provide information regarding the relationship of the evaluation initial condition to the training initial conditions; were the evaluation ICs chosen as to try to capture in-distribution evaluation or were they chosen explicitly to evaluate out of distribution behavior?"
- Statistics (Sec. 4.2): "Providing a point estimate for success and performance metrics can be misleading [10]. ... The statistical analysis can follow the frequentist approach, by providing interval estimates [10] or bounds [45], or the Bayesian approach [46] of estimating parameters of distributions". Their worked approach: "we treat task success as a Bernoulli distribution with (unknown) parameter p ... Given a prior on p, here a uniform distribution between 0 and 1, and the data, we can estimate the distribution of p; the more the distributions of the policies overlap, the less confidence we have that one policy is better than the other." (Example 6, computed with the Lyst Bayesian A/B calculator [48]). "Reducing the number of evaluations makes any conclusions weaker, adding more evaluations makes them stronger." Reporting guidelines deferred to Kruschke [47]. [10] is Agarwal et al. "statistical precipice"; [45] Vincent et al. BC generalisation bounds; [46] Kruschke "Bayesian estimation supersedes the t test" (References).
- Trial count: the paper gives NO prescribed minimum number of trials. It only demonstrates that 15/3 vs 11/6 (n=18,17) does not separate two policies (P(B>A)=.11) while 150/30 vs 110/60 does (Fig. 7). Its own report uses "10 different initial conditions ... each policy twice on each IC (for a total of 20 evaluations per policy)" (Sec. 6.4.1). No frequentist confidence-interval widths are given anywhere in the paper.
- Failure modes (Sec. 4.3): "We recommend providing a detailed description of common and surprising failure modes encountered during the evaluation. This includes information regarding failure categories, narrative descriptions, frequency, and visual descriptions through images and videos".
- Data release (Sec. 5): "we also strongly advocate for open release of evaluation rollout data to enable additional nuanced posthoc analysis by the community."
- Example report structure (Sec. 6.4): A/B blind, two days (12 + 8 runs per policy, second day 4 days later), evaluator "not involved in the data collection or policy training", ICs matched "using an image overlay tool", success criterion stated verbatim ("Energy bar is on the wooden tray and the tray in on the table"; collisions not counted as failures), performance metrics on successful runs only, per-IC failure listing.

## Limitations stated by the authors
- Physical replication is impossible: "with a physical system it is impossible to replicate the exact same experimental conditions between evaluation runs" (Sec. 2).
- Automated semantic/failure detection via learned or VLM models "is not yet a reliable way to automate the assessment of semantic information for policy rollouts on physical systems" (Sec. 3.1.1).
- STL needs state: "The challenge is providing the state information; for physical robots we can use proprioceptive information and classifiers" (Sec. 3.1.2). The two-mode robustness signal in Example 4 arises "because the signals themselves have a different range of values. This might not be the case in all situations" (Sec. 3.2.1).
- SPARC "is well suited for reaching tasks" (Sec. 3.2.2).
- Metric choice is task-dependent; "We are advocating for researchers to choose the set of metrics that is best suited for their approach, task, and domain" (Sec. 5). "While not panacea" (Sec. 5 "Closing thoughts").

## Quotable claims (verbatim, with section)
- "it is common for papers to report this number with little to no information regarding the number of runs, the initial conditions, and the success criteria, little to no narrative description of the behaviors and failures observed, and little to no statistical analysis of the findings." (Abstract)
- "It is well known among robot learning practitioners that today's learning-based robots are highly sensitive to their deployment environment." (Sec. 2.2)
- "Looking only at overall success would deem Policy C to be an unsuccessful policy; however, that is not the full picture, as it is able to accomplish more than half the task consistantly." (Table 1 caption)
- "For simulation evaluation, the world state is known, therefore STL metrics can shine." (Sec. 3.1.2)
- "Evaluating physical systems is difficult. It requires controlling numerous potentially confounding variables, balancing sample-size with diversity of conditions and comparisons given a fixed resource budget, contending with equipment malfunction, and managing human subjectivity and bias." (Sec. 5)

## Notes for the survey (which sections this feeds; contradictions with other notes)
- Evaluation section: the four-item reporting checklist (Sec. 4.1), the four process bullets (Sec. 2.3), and the Bayesian-posterior argument that n=18 vs 17 cannot separate 83% from 65% (Example 6, Fig. 7) are the citable core. Cite it for "report counts not percentages" and "blind A/B interleaving", not for a specific trial number: the paper prescribes none.
- Dexterous relevance: no hand modelled; the in-hand metrics it cites from others (time to fall, angle of rotation, torque applied [21]) are examples of task-specific performance metrics (Sec. 1.1). The rubric/sub-goal idea maps directly onto grasp-then-carry-then-place decompositions.
- STL over simulator state (Sec. 3.1.2, Sec. 5) is the paper's argument that simulation makes the whole protocol automatable — pairs with simpler_2024 / autoeval_2025 notes on automated evaluation; contrast with roboarena_2025's pairwise human preference, which sidesteps absolute success criteria altogether.
- Example 2 (65% -> 0% after a lab reorganisation on identical ICs) is the cleanest published instance of silent distribution shift and supports colosseum_2024-style perturbation axes (lighting, camera, background).
