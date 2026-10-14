# 3. Hands and who makes them

## 3.1 Design axes

A policy is only as dexterous as the hand it runs on, and the hands available divide sharply: a
few that a laboratory can buy, a few more it can build from published designs, and a growing
number that exist only in an announcement. What can be said about them is less than it looks.
No degree-of-freedom, force, weight or price figure in Table 2 or Table 3 was measured by
anyone outside the maker. Six entries are the exception, from peer-reviewed papers with stated
protocols: ILDA, Pisa/IIT, ORCA, RUKA, LEAP and BiDexHand. Table 2 dates every other claim.

The degree-of-freedom count is the first number a vendor states and the least comparable one,
because three different quantities get printed under that heading: joints, actuated joints and
actuators. Shadow's own specification separates them, reading "20 actuated DOF and a further 4
under-actuated movements for a total of 24 joints" `shadow_dexterous_hand_2005`; Inspire's page
gives a DoF figure and a joint count that differ by a factor of two `inspire_rh56dfx_2023`; a
tendon hand can list more actuators than it has kinematic degrees of freedom
`daxo_muscle_v0_2025`. Table 2 therefore prints joints and actuated DoF in separate columns, with
actuators in a third, and the gap between them is the informative number.

The actuation ratio is the real decision. The Pisa/IIT SoftHand drives nineteen joints from one
motor, and its authors state the cost plainly: "No in-hand dexterous manipulation is required for
this prototype". Tendon drive moves the motors off the fingers and the mass follows them, so a
hand with every motor in its palm can weigh a quarter of a tendon hand with a forearm; Table 2
gives both weights. What tendons cost is state estimation. The Faive Hand estimated joint angles from tendon length through
a Kalman filter and its cube reorientation failed on hardware, which its authors blamed on "poor
joint angle measurement from the EKFs, especially when there is contact" `faive_hand_2023`.
Ruka-v2 adds detachable AS5600 encoders to measure that problem rather than close the loop on it,
and those encoders put its open-loop linear joint-to-motor map at 8.26 degrees of error over seven
joints `ruka_v2_2026`.

Direct drive trades torque density for transparency: LEAP's Dynamixel joints resist 19.5 N in a
pull-out test against the Allegro's 8.5 N `leap_hand_2023`. Linkage drive is the argument against
the forearm, putting motors, drivers and ball screws inside the palm and still reaching tens of
newtons at the fingertip `ilda_hand_2021`. Linkages also buy joint coupling for free, as in
BiDexHand's four-bar that drives each distal joint off the one behind it, though that hand's paper
and its own README disagree about how many joints and servos it has `bidexhand_2025`.

Fingertip force is the number a hand buyer reads first, and across these hands it is six
different measurements wearing one name. Pull-out resistance, a pinch between two fingers,
fingertip normal force under a standard indenter, a calibrated multi-trial measurement, a peak
vendor claim and two unlabelled columns on a spec sheet all appear as "fingertip force". One
vendor's figure turns out to be the newton equivalent of a payload at a fixed motor current, which
is a different quantity again. Table 2 therefore prints the protocol beside every force it
reports, and leaves the cell empty where the protocol cannot be recovered. No two hands in it
report payload under the same test either.

Compliance is repairability seen twice over, and both are mechanical fuses: the Pisa/IIT
SoftHand's rolling-contact joints return to assembly after over-extension and ORCA's "poppable"
pin joints dislocate rather than break `pisa_iit_softhand_2014` `orca_hand_2025`. ORCA also
reports tendon drive as maintenance: "Prolonged use requires manual re-tensioning to maintain
performance". What fails is rarely the motors. Its durability run found silicone skin degrading on
two fingertips after about 2,000 to 4,000 grasp cycles and sensor wires snapping on three after
about 4,500 to 7,000. The sensing wore out an order of magnitude sooner than the hand.

Two columns matter before any of the above, and no vendor comparison carries them. The first is
the rate at which a control loop can actually be closed, which spans a factor of four across these
hands and is not stated at all by some; one hand's quoted rate turns out to be a serial query
ceiling while its own transferred policy runs at 20 Hz, which answer different questions. A reader
deploying torque control is bitten by that first. The second column says whether a URDF or MJCF
exists and who ships it, which is the bridge to section 4 and to this survey's recommendation:
prefer a hand a simulator already carries. LEAP is the warning there, because its paper says the
URDF is released and the released API repository contains none `leap_hand_2023`.

{{table:table2_hands_available}}

## 3.2 Hands in use, and what they cost

{{figure:fig2_hands}}

The two oldest designs in Table 2 carry 49 of the 104 papers that name a hand at all, and seven
papers use both. Figure 2 counts, per hand, the papers whose own experiments use it, and the shape
of that figure is the finding: four hands take three quarters of the corpus and everything else
shares the remainder.

The Allegro's position is the uncomfortable part. Its product page at allegrohand.com/v4 returned
HTTP 404 while the Wonik wiki timed out `allegro_hand_v4_2016`. Everything Table 2 confirms about
the most-used hand in the corpus comes from its ROS driver: 16 joints, four fingers, a torque
interface, a 333 Hz CAN clock, 12 V, no tactile sensing. Its weight, joint torque, payload and
price have no reachable source. The field's most common platform cannot be specified from a page a
reader can open.

Concentration would matter less if the hand did not move the result, and it does. On the same
simulated cube rotation LEAP turns the cube nearly three times faster than the Allegro
`leap_hand_2023`, and on the same three-trial pinch test RUKA reports almost twice the Allegro's
force `ruka_2025`. A method compared only on Allegro hardware is compared at one point in a space
where a single axis moves the headline number two or three times over. The three newest Chinese
hands have arrived quickly and take a growing share, none of them before 2024, and eight hands
that can be bought or built take no papers at all.

The cost of entry has collapsed at the open-hardware end. Seven hands in Tables 2 and 3 publish
their designs, and the five that also publish a price run from a few hundred dollars to a few
thousand, against six figures for the hands this literature actually runs on. Table 2 carries each
price with what it includes, because the bases differ: the cheapest figure excludes printing and
wrist servos `dexhand_open_source_2023`, and one vendor's own number sits against a third party's
estimate several times higher `orca_hand_2025` `ruka_v2_2026`.

The expensive end of that comparison is secondhand throughout: the six-figure prices for a
Shadow Hand come from other people's comparison tables, because the vendor's own page asks buyers
to discuss pricing. So the collapse is real at the cheap end and inferred at the expensive one,
and it has barely moved the literature. Twelve of the 104 hand-naming papers use an open-hardware
hand, and all twelve of those are LEAP.

What the cheap hands give up is sensing. LEAP has none and names touch sensors as future work
`leap_hand_2023`, RUKA states its design "lacks tactile sensing" `ruka_2025`, and BiDexHand's
sources never mention touch `bidexhand_2025`. ORCA is the exception, with binary FSR fingertips
whose threshold was measured as low as 0.05 N on a fresh fingertip, against the sensor's rated
0.29 N, and 6.38 N on a degraded one `orca_hand_2025`.

## 3.3 Tactile sensing

DIGIT set the cost floor, stating a manufacturing cost of about 15 USD per sensor in batches of
a thousand `digit_2020`, which is where the price of touch sensing stopped being the obstacle.
Durability was as much of the contribution: its gel barely degraded over an abrasion test that
destroyed the two gels compared against it.

Digit 360 is the same lineage at a different operating point: millions of taxels, force
resolution around a millinewton, and on-device processing that cuts event-to-action latency by
most of an order of magnitude `digit360_2024`. It is also not for sale, and no paper in this
corpus names it.

XELA's uSkin is the non-camera alternative, and the one that bolts onto hands the field already
uses: a curved fingertip kit for the Allegro and LEAP, with three-axis sensing points at
gram-force resolution running at a few hundred hertz `xela_uskin_2020`. Table 3 gives the
specification, including which figures belong to the product family rather than to the fingertip
kit. One paper in this corpus uses it, and its self-supervised encoders beat matched end-to-end
models when both see a fraction of the labels, though its own bead-maze policies never complete
the maze on the real robot `sparsh_2024`.

The usage number is the one to keep, and it needs its inclusion rule stated: a sensor
physically on the hand, read by the deployed policy. Eight papers meet it:
`anyrotate_2024`, `articulated_tools_inhand_2025`, `dexteleop0_2026`, `dexumi_2025`,
`hato_visuotactile_2024`, `robot_synesthesia_2023`, `rotateit_2023` and
`rotating_without_seeing_2023`. The rule excludes `penspin_2024`, whose 20 binary contacts are
simulated on an Allegro that has no tactile hardware and whose released config sets
`enable_tactile: False`, and it excludes `dexndm_2025` and `dexplore_2025` for the same reason.
Sixty-three of the 113 method papers use the word tactile somewhere in their parsed text and 35
carry it in their structured note. Against the eight that meet the rule above, either number is
the gap worth quoting.

Almost none of the eight uses a high-resolution sensor. `rotating_without_seeing_2023` removes
vision entirely and rotates objects from 16 binary touch sensors over the palm, links and
fingertips, deployed zero-shot to a real Allegro, and Robot Synesthesia uses 16 force-sensing
resistors read as binary `robot_synesthesia_2023`. Two papers exclude touch deliberately, HORA
reporting rotation "even without the usage of vision and tactile sensing" `hora_2022`, and ORCA's
authors dropping it from their reinforcement learning "due to the additional complexity involved
in accurately modeling them" `orca_hand_2025`. Taxel counts have risen by three orders of
magnitude while the policies consuming them have stayed at binary contact.

## 3.4 The catalog against the literature

Behind Table 3's entries sit three kinds of evidence, and
conflating them is how a DoF figure with no source ends up in a survey. Vendor prose carrying
numbers is the strongest, as on 1X's page of 9 July 2026 `onex_neo_hand_2026`. Video is second
and carries none. Press or bibliography assertion is third, as with Tesla's V3 hand, known here
only through a paraphrase of patents because the USPTO PDF parsed empty
`tesla_optimus_hand_2025`. Table 3 blanks the cells resting on the third class and footnotes
who did the arithmetic.

A survey can go one step past recording that a claim is unverified, which is to say which claims
are implausible on their face. One vendor's actuator count and mass work out to about six grams
per actuator including structure, tendons, routing and skin `daxo_muscle_v0_2025`. Another's mass
figure appears to exclude a half-kilowatt pump `clone_robotics_hand_2024`. A third's
degree-of-freedom figure sits on the same page as a finger count that is exactly half of it, so it
is almost certainly the pair of hands `figure_03_hand_2025`. A fourth number, widely repeated for
the Optimus hand, is one article's arithmetic rather than a vendor statement, and the previous
generation's own figure was half of it `tesla_optimus_hand_2025`.

Skepticism belongs to the evidence class, not to which table an entry lands in. The
fully-actuated claims from the newest vendors are claims about unmeasured hardware, and they sit
in Table 2 beside the footnotes their own pages carry: "Specifications may vary between products"
on one, a spec that "will continue to iterate" on a beta product on another `sharpa_wave_2026`
`wuji_hand_2025`. Even the best-specified vendor page in the corpus leaves its fingertip-force
columns unlabelled.

{{table:table3_hands_announced}}

The bottom of Figure 2 carry the finding.
None of the nine company-announced hands in Table 3 appears in a single paper whose own
experiments use it. Tesla, Figure, 1X, Sanctuary, Boston Dynamics, Xiaomi, Clone, Daxo and
PaXini account for zero of the 113 method papers' experiments. The nearest thing to a
counterexample is `helix_2025`, a Figure blog post claiming a 35-DoF whole-upper-body action
space at 200 Hz that includes individual finger control. It never names the hand, gives no
per-hand DoF count, and reports no success rate or trial count for any task. It is the maker
describing its own unreleased hand, which is the evidence class the finding is about. The four
research prototypes in Table 3 are in a different position, since the Faive Hand and LEAP Hand
v2 Advanced account for three papers between them `graspxl_2024` `bidex_teleop_2024`.

Table 3's emptiness is measurable and part of the same finding. Over the twelve specification
columns, 61 percent of its cells are values no source stated, against 39 percent for the hands
that can be bought. The hands with the highest advertised DoF counts have the least specification
behind them.

The one hand that crosses the gap crosses it because its maker published rather than announced.
ByteDexter reaches a paper through a ByteDance technical report stating 21 DoF per hand, 16
piezoresistive fingertip channels in the action vector and real-robot success rates
`gr_dexter_2025`, not through a product page. That mechanism is available to every vendor in Table
3 and none has used it.

The gap runs the other way too, and the last column of Table 2 shows it. Eight hands that can be
bought today or built from published designs take no papers at all: the Unitree Dex5
`unitree_dex5_2025`, the Tesollo DG-5F `tesollo_dg5f_2024`, the Proception ProHand
`proception_prohand_2026`, ORCA, RUKA, Ruka-v2, BiDexHand and DexHand. Cheapness is
established for only three of those eight, because the price cell is empty for the rest. A reader
choosing a hand on this corpus's evidence has four options with published precedent behind them,
and only one of the four, LEAP, has both a published design and a stated price. Below those four
the record thins fast, and 19 of the hands in Tables 2 and 3 sit there on their specifications
alone, with no paper in this corpus running on any of them.

What would close the gap is tooling rather than manufacturing. Nineteen of the 33 hands in
Tables 2 and 3 appear in no paper here, and most of those are neither sold nor open, so the eight
obtainable ones named above are the real measure of the lag. The lag runs through the simulators
too: fewer than half of them ship a first-party hand model at all, and every model they do ship is
an Allegro or a Shadow. Two recent benchmarks compare a dozen hands between them without stating a
degree-of-freedom count for any. What would close it is a conformance suite for hand models: one
URDF or MJCF per hand, fixed joint-limit, mass and collision checks, and a published pass or fail
per engine.