# ma_dollar_dexterity_2011 — On Dexterity and Dexterous Manipulation (Ma & Dollar, ICAR 2011)

sources: papers/md/ma_dollar_dexterity_2011.md [sha256 949ad934] ; no code

## One-line contribution
A conceptual/opinion paper (no experiments, no hardware, no simulation): it surveys prior
definitions of dexterity, argues out the trade-off between a dexterous arm with a simple
gripper versus a dexterous hand, taxonomizes the classes of within-hand manipulation, and
reviews a set of previously-built dexterous hands.

## Setting / Method
Not an experimental paper: no hand, simulator, observation, action space, objects/data,
paradigm, reward, or trick of the authors' own. Section IV.B reviews hands built by others
(below); the paper's only "figures" are schematic illustrations of manipulation classes and
arm/hand trade-offs (Figs. 1-9).

## Definitions of dexterity (verbatim, Sec. II.A "Definitions of Dexterity")
The paper does not propose its own formal definition; it collects and contrasts five from
prior literature, quoted exactly as given:
- "(The) capability of changing the position and orientation of the manipulated object from a
  given reference configuration to a different one, arbitrarily chosen within the hand
  workspace" — Bicchi 2000, [6].
- "(The) process of manipulating an object from one grasp configuration to another" — Li 1989,
  [9].
- "(When) multiple manipulators, or fingers, cooperate to grasp and manipulate objects" —
  Okamura 2000 [8].
- "(The) kinematic extent over which a manipulator can reach all orientations" — Klein/Blaho
  1987 [10].
- "Skill in use of hands" — Sturges 1990 [11].

The paper's own scoping choice (not a definition, a stated focus, Sec. II.A): "For this
discussion, we will focus on more generalized task and object-centric definitions of
dexterity, focusing on the systems' kinematic and dynamic capabilities as opposed to the
similarity of their mechanical design to the human hand."

Its closing characterization of dexterity (Sec. V, Conclusions, verbatim): "Dexterity in
general refers to the variety of tasks that the system can complete, and also how well it can
perform those tasks, though the means by which that can be quantified is still open to
interpretation."

No definition of "dexterous manipulation" as a separate term from "dexterity" is given; the
paper uses the two interchangeably throughout and defines within-hand manipulation instead via
its taxonomy (below).

## Taxonomy of manipulation types (verbatim, Sec. IV, "Within Hand Manipulation")
Whole-arm vs. within-hand split (Sec. IV intro, verbatim): "the contribution of each can be
decoupled into the arm manipulation (which is typically large-scale positioning of the hand in
space combined with application of large forces) and the within-hand manipulation component
(if any)."

Classes of within-hand manipulation (Sec. IV.A, verbatim definitions):
- **Regrasping**: "this type of manipulation may be the simplest form of dexterous
  manipulation, where the object is released and re-grasped in order to change its position
  and orientation within the grasp." Can occur "between multiple hand workspaces or entirely
  within the hand workspace."
- **In-Grasp Manipulation**: "utilizes the kinematic redundancy of fingers to make small
  changes to the object's orientation and position while maintaining fingertip contact with
  the object... it is assumed that no sliding or slippage occurs at the fingertips" (though
  local rolling may occur).
- **Finger Gaiting**: "extends the kinematic limits of in-grasp manipulation in the absence of
  rolling and sliding by replacing grasping fingers with free fingers"; subdivided into
  "finger substitution, where a free finger replaces a grasping finger at the edge of its
  configuration space, and finger rewind, where a free finger is used to maintain stability of
  the object while a grasping finger is freed to move to another position."
- **Finger Pivoting/Tracking**: "establishes an axis of object rotation through two point
  contacts while utilizing the remaining free fingers to guide the object's rotation about
  this axis."
- **Rolling**: "only realizable for objects/fingers of certain geometries but can also be
  performed by non-fingered end effectors. This is generally regarded as a form of
  non-prehensile manipulation requiring non-holonomic control in task planning."
- **Sliding**: "Whereas the other forms of within-hand manipulation assume no slippage,
  sliding manipulates objects through controlled slip."

Prehensile vs. non-prehensile: the paper does not define these terms formally. It applies
"non-prehensile" explicitly in two places — to Rolling (quoted above), and, earlier (Sec.
III.A), to armless cooperating manipulators: "Independently, each would only be capable of
non-prehensile manipulation, but their cooperative behavior together falls under a typical
definition of dexterity." By implication, regrasping, in-grasp manipulation, finger gaiting
and finger pivoting are treated as prehensile (grasp is held or re-formed, never lost), while
rolling is the taxonomy's one class explicitly named non-prehensile; sliding is not labeled
either way.

## Hand complexity vs. system dexterity (Sec. III, Fig. 1, Table I)
Fig. 1 caption (verbatim): "Increasing system dexterity can be accomplished by adding arm
kinematic redundancy or hand complexity" — i.e., the two are posed as substitutable routes to
the same end (system-level dexterity), not as independent contributions.

The paper lays out three arguments (Sec. III.B, its own subheadings, verbatim) for how hand
complexity trades off against arm redundancy:
1. "A Dexterous Arm with a Simple Gripper is Sufficient" — a highly redundant arm plus a
   simple stable gripper (with regrasping as needed) covers most object-centric,
   six-DoF-placement tasks.
2. "A Dexterous End-Effector can make up for Limitations in Arm Functionality" — at arm joint
   limits, singularities, or near obstacles, hand dexterity restores workspace the arm alone
   cannot reach (Figs. 3–4); but "in scenarios where a power grasp is required... the dexterity
   of the hand is greatly reduced, and even a dexterous hand's function becomes comparable to
   that of a parallel-jaw gripper," so added arm dexterity is then more valuable than added
   hand dexterity.
3. "Manipulation with a Dexterous End-Effector is Sometimes More Appropriate for a Given Task"
   — for small-scale, precision motions, actuating the hand rather than the whole arm lowers
   inertial load, lowers required feedback gains, and lets an object be reoriented (e.g.
   fingertip grasp to power grasp) without releasing it (Fig. 5).

Table I ("Considerations for/against in-hand dexterity"), verbatim:
- Advantages: Greater precision; Increased efficiency; Increased generality, kinematic
  redundancy; Specialized for tasks of a certain scale.
- Disadvantages: Increased mechanical complexity; Decreased strength/power; Increased control
  complexity; Restricted to tasks of that certain scale.

Conclusion on the split (Sec. V, verbatim): "It is perhaps appropriate to classify the hand and
arm as subsystems responsible for tasks of different scales, where the hand performs fixturing
and fine manipulation while the arm handles gross positioning motions."

## Hands reviewed (Sec. IV.B, "Review of Dexterous Within Hand Manipulators")
- **Utah/MIT Dextrous Hand** [22]: "one of the early attempts at reproducing the dexterity of
  the human hand through a tendon-based, fingered design." Four anthropomorphic fingers, 4 DoF
  each, 32 total actuators. Each joint driven by an antagonist tendon pair to mimic human joint
  compliance, but this "also decreased the systems' overall reliability and consistency in
  positioning."
- **UB Hand** [23] and its current iteration **UBH3** [24]: uses "compliant, elastic hinges in
  place of tendons to better emulate the coupled behavior of the human hand," which "resulted
  in improvements for both adaptability in grasps and ease of fabrication."
- **Gifu hand** [25], **DLR hand** [26], **Robonaut hand** [27], **Karlsruhe humanoid hand**
  [28]: listed as other anthropomorphic hands; no individual assessment given beyond the
  citation.
- **Stanford-JPL hand** (Salisbury) [29]: three-fingered, 9 DoF, explicitly non-anthropomorphic
  ("was not meant to be anthropomorphic in design"); "grasp research with this device focused
  on fingertip prehension in grasp formulation."
- **Karlsruhe dexterous hand** [14] (Osswald): non-anthropomorphic, four fingers; "used to
  demonstrate in-hand regrasping motions and localized rolling at the fingertip."
- **Turntable-based manipulator** (Bicchi [18], Nagata [30]): the paper's example of the "few
  non-fingered manipulators that do more than just affix the object to the arm" — turntables
  mounted on a parallel-jaw gripper that "can manipulate spherical objects through rolling."

No quantitative comparison (grip force, cycle time, task success) is given for any hand; the
review is qualitative — design approach and demonstrated manipulation class only.

## Evaluation
- metrics (exact definitions): none — no experiments are run or reported.
- headline numbers: none.
- baselines beaten: none.
- real robot? no.

## Open problems named (Sec. IV.C, "Research Issues in Dexterity", verbatim)
- Design trade-off: "researchers must make the key decision between pursuing a more
  complicated hand design and attempting to do more with a simpler hand mechanism." Citing
  Mason [33]: "generality and mechanism complexity are directly correlated, such that the
  benefits of a truly general hand capable of all examples of in-hand manipulation from
  Section IV.A will not necessarily justify the required level of complexity in both
  mechanical design and control."
- Sensing: "Precise sensory feedback, a prerequisite of many approaches to dexterous control
  in multi-fingered manipulators, continues to be a major challenge in the implementation of
  dexterity." Tactile approaches named — "layers of piezoresistive films, optical arrays, and
  fluid-filled sacs" — but "high cost generally limits these sensors to the manipulator
  fingertips, and these sensitive manipulation systems still must deal with issues of sensor
  noise in unstructured environments."
- Grasp acquisition under uncertainty: "the use of compliant and adaptive fingers and
  appropriate control strategies such as push-grasping can circumvent strict sensor
  requirements by adapting to uncertainty rather than trying to eliminate it. Designing
  adaptive manipulators with flexible material creates 'mechanically intelligent' mechanisms
  inherently suited for particular tasks."

## Limitations stated by the authors
None stated as a dedicated limitations section; the paper frames itself as a discussion piece
("We believe this work will help to revitalize the dialogue on dexterity... and lead to
further formalization of the concepts discussed here," Abstract) rather than a study with
methodological limits to disclose.

## What this paper does not cover
- No quantitative dexterity metric of its own (no manipulability ellipsoid, isotropy index, or
  workspace-volume formula is derived or evaluated) — it only catalogs five prior *verbal*
  definitions (above). This matters for how this survey cites it: the bib entry's `why` field
  ("reviews definitions and measures of hand dexterity (workspace, isotropy, manipulability)")
  overstates the source — no such measures are worked out here.
- No simulation, no RL/IL, no learned policy of any kind.
- No tactile-sensing algorithm or perception pipeline — sensor technologies are named, not
  evaluated.
- No bimanual or multi-arm manipulation content beyond the passing "handless" thought
  experiment of cooperating armless manipulators (Sec. III.A).
- No object dataset, no grasp dataset, no real-robot trial of any kind, no code.
- Hand review (Sec. IV.B) is 2011-era and pre-underactuated/soft-hand-dominant designs; it
  predates tendon-driven high-DoF hands common in the current survey's corpus (e.g. Allegro,
  Shadow, LEAP) and does not mention them.

## Notes for the survey
- Use for the survey's background/taxonomy section only as: (a) a historical snapshot of how
  "dexterity" was defined circa 1982–2000 (five verbatim definitions above, all secondary —
  attributed to Hollerbach, Wright, Bicchi, Li, Okamura, Klein/Blaho, Sturges), and (b) the
  within-hand manipulation taxonomy (regrasping / in-grasp / finger gaiting / finger
  pivoting-tracking / rolling / sliding), which is still the taxonomy most later dexterous-hand
  papers implicitly cite.
- Do not cite this note for any quantitative dexterity metric — none is here (see "What this
  paper does not cover").
- Sits with okamura_overview_2000, bicchi_hands_2000 and piazza_century_2019 as the four
  classic overviews the survey wanted for its taxonomy/background section. As of this note,
  those three remain SOURCE THIN (checked 2026-09-18); if their papers/md/ files are ever
  filled in, they should be re-parsed the same way this one was.
