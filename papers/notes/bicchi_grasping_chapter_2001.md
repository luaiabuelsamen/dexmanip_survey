# bicchi_grasping_chapter_2001 — Robotic Grasping and Manipulation (Bicchi, with V. Kumar; book chapter 1 of RAMSETE: Articulated and Mobile Robotics, Springer LNCIS, 2001)

sources: papers/md/bicchi_grasping_chapter_2001.md [58,674 bytes; fetched from
https://www.centropiaggio.unipi.it/sites/default/files/surveys-ramsete01.pdf ; manifest records no sha256] ; no code

Obtained open access and used in place of the paywalled `bicchi_hands_2000` (IEEE T-RO), which it
overlaps but is NOT identical to. The chapter's own acknowledgement says it "builds upon previous
works by the authors ([7],[8])", where [7] is Bicchi 2000, "Hands for dextrous manipulation and
robust grasping: a difficult road toward simplicity". Cite this key, never the T-RO key, for
anything quoted here.

## One-line contribution
A chapter-length survey of the analytic theory of grasping and dexterous manipulation as it stood
in 2001: contact kinematics as unilateral non-holonomic constraints, form closure, force closure,
constrained hand-object dynamics, stability, contact compliance, the kinematics of defective
hands, and grasp quality measures, written explicitly as theory rather than as a survey of hand
technology.

## Setting
- hand(s): none used. The model is generic: "an arbitrary number of fingers (i.e. simple chains of
  links -phalanges-, connected through rotoidal or prismatic joints), and of an object, which is in
  contact with some or all of the phalanges" (Sec. 1.2). Hands named in passing as history:
  Salisbury's three-fingered hand, the Utah-MIT hand, the University of Bologna dexterous hand
  (Fig. 1.1), the University of Pisa dexterous gripper (Fig. 1.2) (Sec. 1.1).
- single/bimanual: single hand. Multi-arm systems are named once as an analogous constrained
  system, alongside legged locomotion (Sec. 1.4). No two-hand analysis.
- simulator / physics: no simulator. Sec. 1.4 is about why simulating these systems is hard.
- observation / action / objects / data: not applicable; no experiments, no numbers, no figures of
  merit computed.

## Method (taxonomy = section structure)
- 1.1 Introduction. Splits hand design into "an anthropomorphic vs. a minimalistic approach", and
  splits the task into restraining objects ("grasping or fixturing") and "manipulating objects with
  fingers (in contrast to manipulation with the robot arm), sometimes called dexterous
  manipulation". Names enveloping grasps versus fingertip grasps as the two ways a hand holds.
- 1.2 Kinematics of manipulation. Configuration q for the fingers, u = (p_o, R_o) in SE(3) for the
  object; contact constraints written C(q, q̇, u, u̇) >= 0.
- 1.3 Grasp closure properties. 1.3.1 form closure, with the first-order test N^T G^T u̇ >= 0 over the
  grasp matrix G and stacked contact normals N, and its three cases. 1.3.2 force closure, with the
  wrench balance w = Gp and the hand Jacobian relation tau = J^T p.
- 1.4 Dynamics. Disjoint hand and object dynamics M_h(q)q̈ + Q_h(q,q̇) = tau and M_o(u)ü + Q_o(u,u̇) = w,
  "linked through the n rigid-body contact constraints".
- 1.5 Stability. Distinguishes the Lyapunov and the Lagrange senses and states that the Lagrange
  sense "is prevalent in studies on grasp stability".
- 1.6 Contact compliance. Point contacts classified as frictionless, frictional ("point contact with
  friction"), or soft, the last "also allows the finger to exert a pure torsional moment about the
  common normal".
- 1.7 Grasping and the kinematics of the hand. Defective grasps, where the hand Jacobian is rank
  deficient.
- 1.8 Measures of grasp performance. Grasp stiffness matrix, frame-invariant minimum stiffness,
  object-deflection measures.
- 1.9 Concluding remarks.
- reward or loss: none. This predates learned control entirely; the words "learning", "policy" and
  "reinforcement" do not appear as methods anywhere in the chapter.

## Evaluation
- metrics: quality measures are surveyed, not computed. Sec. 1.8 surveys measures derived from the
  conditioning of the grasp matrix, from the grasp stiffness matrix, and from scaled object
  deflection under disturbance.
- headline numbers: none. The only numbers in the chapter are the classical contact counts for
  form closure: "at least four frictionless contacts are necessary for grasping an object in the
  plane, and seven in the 3D case", and "four and seven contacts are necessary and sufficient for
  the form-closure grasp of any polyhedron in the 2D and 3D case" (Sec. 1.3.1).
- baselines / real robot: none.

## Limitations stated by the authors
- Sec. 1.9: "Because of the limitations on space, we have not given the algorithmic aspects, and the
  applications the attention that they deserve."
- Sec. 1.9: the review "mainly addressed research that has established the theoretical framework for
  grasp analysis, simulation and synthesis".
- Sec. 1.1: "the chapter does not attempt at providing a survey of the technology of robot hands".
- Sec. 1.7: much of the force-closure work that models the gripping mechanism "is based on
  instantaneous kinematics".
- Sec. 1.8: "most of these measures are based on the assumptions of small perturbations:
  displacements, forces and errors".

## Gaps / open problems named (verbatim)
- Sec. 1.8: "the nonsmooth nature of grasp dynamics (because of the unilateral constraints on
  displacements and forces) has made a thorough analysis very difficult."
- Sec. 1.8: "in stability analysis, a figure relating to the size of the basin of attraction of the
  equilibrium, indicating how large a perturbation can be without causing instability would be
  desirable."
- Sec. 1.6: "One of the very hard problems is getting an accurate and tractable model of contact
  compliance, particularly in the tangential direction ... In addition to this, a tractable and
  accurate model of friction, one that accurately predicts slip and one that lends itself to
  stability analysis, is currently not available."
- Sec. 1.7: "Many open problems remain to be solved in order to be able to design robot hands to
  effectively exploit defectivity to increase grasp robustness and reduce hardware complexity."
- Sec. 1.4: "it is very difficult to write accurate simulators for dexterous and fine manipulation
  where the contact forces may be finite and the results may be sensitive to the parameters in the
  contact model."

## What it does NOT cover
- Learning of any kind: no RL, no imitation, no data. The chapter is analytic throughout.
- Hand technology, actuation, sensing, cost: excluded by its own statement (Sec. 1.1).
- Bimanual and two hands on one object: absent. Multi-arm systems are named once (Sec. 1.4).
- Perception: absent. Object geometry and pose are assumed given.
- Evaluation of controllers: no trials, no success rate, no benchmark.
- Simulation as a tool: treated only as a problem to be solved (Sec. 1.4), never used.

## Quotable claims (verbatim, with section)
- Sec. 1.2: "Contacts represent a particular kind of kinematic constraint on the allowable
  configurations of the system, and cause most of the differences in the analysis of dextrous
  manipulation from other robotic systems. Contact constraints are typically unilateral,
  non-holonomic constraints".
- Sec. 1.2: "The inequality relationship reflects the fact that contact can be lost if the
  contacting bodies are brought away from each other. This involves an abrupt change of the
  structure of the model under consideration."
- Sec. 1.3.1: "Form-closure is the ability of a hand to prevent motions of the object, relying only
  on unilateral contact constraints."
- Sec. 1.3.2: "the concept of force-closure is somewhat less clearcut and universally accepted."
- Sec. 1.5: "It is important to note that force closure does not guarantee stability."
- Sec. 1.4: "if we consider the simulation of a rod sliding along a rough ground in a plane with a
  single contact, there are configurations in which no solutions (that are consistent with the
  constraints) exist, and others in which the solution is not unique."
- Sec. 1.4: "The inconsistencies and ambiguities in the dynamic analysis of frictional contacts have
  been attributed to the approximate nature of Coulomb's model and to the incorrect assumption of
  rigidity."
- Sec. 1.4: "One of the main difficulties that is present in multifingered grasps, and a feature
  that is particularly true of such grasps as power grasps and enveloping grasps, is that the
  number of independent contact forces is much larger than the number of actuators. Thus, from a
  controllability standpoint, not all the contact forces are controllable".
- Sec. 1.4: "The analysis of statically indeterminate grasps or grasps in which there is no unique
  solution to the inital value problem is simply not possible unless one explicitly models the
  compliance at the contacts" [sic, "inital"].
- Sec. 1.7: "It is interesting that much of the literature in grasping actually ignores the
  kinematics of the fingers or the articulations that are involved in contacting the object."
- Sec. 1.7: "Intuitively, the more a grasp is defective, the more robust it is in restraining an
  object with respect to external disturbances and the lower is sensitivity to positioning errors,
  but also the lower is manipulability."
- Sec. 1.1: "there are two prevailing philosophies, which can be identified with an anthropomorphic
  vs. a minimalistic approach to design."

## Notes for the survey
- This is the only one of the survey's classical analytic sources that was actually obtained.
  `okamura_overview_2000`, `bicchi_hands_2000`, `ma_dollar_dexterity_2011`, `piazza_century_2019`,
  `ferrari_canny_1992` and `roa_suarez_grasp_quality_2015` are all SOURCE THIN. Any statement about
  what analytic grasp planning assumed, and what it could not deliver, should be sourced here or
  left unmade.
- Feeds Sec. 1 (why the field moved from analytic planning to learned control: the chapter itself
  names the blockers, namely no tractable friction model, no tangential compliance model, quality
  measures valid only for small perturbations, and non-smooth dynamics that resists analysis).
- Feeds Sec. 2.2 (contact non-smoothness: Sec. 1.2 on unilateral constraints and the "abrupt change
  of the structure of the model"; Sec. 1.4 on non-existence and non-uniqueness of solutions) and
  the underactuation argument (Sec. 1.4: independent contact forces outnumber actuators).
- Feeds Sec. 2.3 (bimanual): the chapter's hand-object system is already a constrained system whose
  hand and object dynamics are coupled only through the contact constraints, which is the frame in
  which a second hand on the same object is a second constraint set on the same object, not a
  second independent problem. The chapter itself does not make that extension.
- Caution on provenance: the manifest records no sha256 for this file and no page count. The PDF was
  fetched from Centro Piaggio. Quoted text carries the OCR's typography artefacts (ligature loss,
  "dextrous", "ojects", "inital"); quotes above are transcribed as printed, with [sic] where the
  source itself is misspelled.
