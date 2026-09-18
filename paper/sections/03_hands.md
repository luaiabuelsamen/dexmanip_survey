# 3. Hands and who makes them

## 3.1 The design axes

The degree-of-freedom count is the first number a vendor states and the least comparable one.
Shadow's specification of December 2024 reads "20 actuated DOF and a further 4 under-actuated
movements for a total of 24 joints" `shadow_dexterous_hand_2005`. LEAP Hand v2 Advanced claims
"21 DOF with 17 powered motors" on its page while its own README calls the hand "17-DOF"
`leap_hand_v2_adv_2025`. Unitree's Dex5-1 page reads "20 Degrees of freedom (16 active+4)"
`unitree_dex5_2025`. Table 2 therefore prints actuated DoF beside DoF, and the gap is the
informative number.

The actuation ratio is the real decision. The Pisa/IIT SoftHand drives 19 joints from one motor
through an adaptive-synergy differential and holds about 20 N with a 6 W Maxon RE-max21
`pisa_iit_softhand_2014`. Its authors state the cost plainly: "No in-hand dexterous manipulation
is required for this prototype." At the other end sit 1X's claimed 25 fully actuated degrees of
freedom `onex_neo_hand_2026` and Daxo's reported 120 actuators in 0.75 kg
`daxo_muscle_v0_2025`, neither of them measured by anyone outside the company.

Tendon drive moves the motors off the fingers and the mass follows them. Shadow's hand plus
forearm weighs 4.3 kg and holds 4 kg in a power grasp `shadow_dexterous_hand_2005`, while RUKA's
11 forearm Dynamixels give a 2.74 N pinch and a 6.0 kg payload `ruka_2025`. What tendons cost is
state estimation. The Faive Hand shipped without joint encoders and estimated angles from tendon
length through a Kalman filter, and its cube reorientation still failed on hardware, which its
authors blamed on "poor joint angle measurement from the EKFs, especially when there is contact"
`faive_hand_2023`. ORCA reports the same problem as maintenance: "Prolonged use requires manual
re-tensioning to maintain performance" `orca_hand_2025`. Ruka-v2 bolts AS5600 encoders onto the
joints instead, leaving an 8.26-degree average error under a linear joint-to-motor map
`ruka_v2_2026`.

Direct drive trades torque density for transparency. LEAP's Dynamixel joints give a 19.5 N
pull-out force against the Allegro Hand's 8.5 N at 595 g `leap_hand_2023`. Wuji states
"Direct-drive rotary, back-drivable" with 1000 Hz across 20 axes, and states no weight and no
fingertip force at all `wuji_hand_2025`. 1X makes the same argument by gear ratio, calling the
100:1 to 200:1 ratios of stiff hands "write-only" `onex_neo_hand_2026`.

Linkage drive is the argument against the forearm. ILDA puts 15 motors, drivers and ball screws
inside the palm and reports 34 N of fingertip force at 1.1 kg `ilda_hand_2021`, a quarter of
Shadow's mass for a larger force. Linkages also buy coupling for free, as in BiDexHand's
anti-parallelogram four-bar that drives each DIP off its PIP and saves an actuator per finger
`bidexhand_2025`, or the Ability Hand's five fingers on six motors `psyonic_ability_hand_2021`.
Hydraulics appear only in hands nobody outside the company has held. Sanctuary claims
miniaturised valves with "an order of magnitude higher power density than cable and
electromechanical-based systems" and puts no number behind it `sanctuary_phoenix_hand_2024`.
Clone's 27-DoF hand weighs under 2 pounds only because its 500 W pump sits outside it
`clone_robotics_hand_2024`.

Compliance and repairability are the same axis seen twice. The Pisa/IIT SoftHand's
rolling-contact joints are held by polyurethane ligaments and return to assembly after
over-extension `pisa_iit_softhand_2014`, and ORCA's "poppable" pin joints dislocate rather than
break `orca_hand_2025`. Both are mechanical fuses, and both are cheaper than the force
transparency 1X buys with low gear ratios `onex_neo_hand_2026`. RUKA states that "most repairs
take under 20 minutes" `ruka_2025` and ORCA that one person with no prior experience assembles
it "in less than eight hours" `orca_hand_2025`, while Shadow releases controller source and
schematics only under a non-disclosure agreement `shadow_dexterous_hand_2005`. What fails is
rarely the motors. ORCA's durability run found silicone skin degrading on two fingertips after
about 2,000 to 4,000 grasp cycles and sensor wires snapping on three after about 4,500 to 7,000
`orca_hand_2025`. The sensing wore out an order of magnitude sooner than the hand.

## 3.2 The hands the research literature actually runs on

Two hand designs, one from 2005 and one from 2016, carry 52 of the 103 method rows that name a
hand at all. Figure 2 counts, per hand, the method papers whose own experiments use it. Of 110
method rows, 103 name a hand. The Allegro accounts for 35, Shadow for 21, the Inspire RH56 family
for 19, a parallel-jaw gripper for 12 and LEAP for 11. Seventy-four of the 103 name an Allegro, a
Shadow or Adroit model, LEAP or an Inspire.

The Allegro's position is the uncomfortable part. It is a 16-joint hand with no tactile sensing,
and its product page at allegrohand.com/v4 returned HTTP 404 while the Wonik wiki timed out
`allegro_hand_v4_2016`. Everything Table 2 confirms about the most-used hand in the corpus comes
from its ROS driver: 16 joints, four fingers, a torque interface, a 333 Hz CAN clock, 12 V. Its
weight, joint torque, payload and price have no reachable source. The field's most common
platform cannot be specified from a page a reader can open.

Concentration would matter less if the hand did not move the result, and it does. On the same
simulated cube rotation, LEAP reaches 0.2288 rad/s against the Allegro's 0.0828 rad/s, which the
LEAP authors attribute to supporting the cube from the sides without releasing it
`leap_hand_2023`. RUKA reports a 2.74 N pinch against the Allegro's 1.60 N over three trials per
test `ruka_2025`. A method compared only on Allegro hardware is compared at one point in a space
where a single axis moves the headline number by two or three times. Two further patterns follow
in the figure: Inspire, XHand and Sharpa take 33 method rows between them and none predates 2023
here, while ORCA, RUKA, Ruka-v2, BiDexHand, DexHand, the Tesollo DG-5F and the Unitree Dex5 take
none at all.

## 3.3 Open hardware and the collapse in cost

The costs are quoted verbatim because they are quoted on inconsistent bases at the source. LEAP
Hand: "LEAP Hand is low-cost and can be assembled in 4 hours at a cost of 2000 USD from readily
available parts", alongside a separate "commodity 3D printer that costs around 200 USD" and a
two-day print `leap_hand_2023`. RUKA: "The total cost of the raw materials needed, excluding
tools (a 3D-printer and soldering iron), is under $1,300 USD. There is also a $500 and $900
version of RUKA with varying Dynamixel motors" `ruka_2025`. Ruka-v2: "The total material cost of
Ruka-v2 is under $1,500" `ruka_v2_2026`. LEAP Hand v2 Advanced: "a dexterous, $3000, simple
anthropomorphic hybrid rigid-soft hand" `leap_hand_v2_adv_2025`. DexHand: "The hand is made
entirely by 3dprinting with additional total cost of components required for the hand around
$300 USD" `dexhand_open_source_2023`. ORCA is "built for a material cost below 2,000 CHF"
`orca_hand_2025`, stated only in Swiss francs, which is why Table 2's price column is empty for
ORCA rather than silently converted.

Two of the six have no cost figure at all. The Faive Hand paper states no bill of materials for
itself and only names a comparison, "a steep price tag of 110k GBP as quoted from their website",
for the Shadow Hand `faive_hand_2023`. BiDexHand's README points at a `BOM.md` that the parsed
repository does not contain, and no figure appears in its paper either `bidexhand_2025`. Neither
hand should carry an inferred price.

For scale, RUKA's comparison table lists the Allegro at $15,000 and the Shadow Hand at $100,000
`ruka_2025`, and Ruka-v2's lists the Sharpa Wave at about $50K under a footnote saying it is
"reported by third-party sources only" `ruka_v2_2026`. Those are secondhand figures in a hardware
paper and belong to those tables, not to the vendors. The only vendor-adjacent price in Table 2
is the 14,000 USD a tracker lists for the XHAND1 `robotera_xhand1_2024`.

The collapse is real, from a six-figure hand to a $300 one inside a decade, and it has barely
moved the literature. Fourteen of the 103 hand-naming method rows use an open-hardware hand, and
11 of those are LEAP. What the cheap hands give up is sensing. LEAP has none and names touch
sensors as future work `leap_hand_2023`, RUKA states its design "lacks tactile sensing"
`ruka_2025`, Ruka-v2 offers e-flesh fingertips outside the base design `ruka_v2_2026`, and
BiDexHand's sources never mention touch `bidexhand_2025`. ORCA is the exception, with binary FSR
fingertips whose detection threshold was measured "as low as 0.05 N" `orca_hand_2025`.

## 3.4 Announced and unreleased hands

Behind Table 3's rows sit three kinds of evidence, and conflating them is how a DoF figure with
no source ends up in a survey.

One row rests on vendor prose carrying numbers. 1X's page dated 9 July 2026 claims 25 degrees of
freedom, 22 in the fingers and palm plus three at the wrist, quasi-direct-drive tendons at
roughly 5:1 to 15:1, peak torques of 3.5 Nm at the thumb CMC and 2.6 Nm at the finger MCP,
distal flexion forces to 45 N, IP68, and capacity "to produce 10,000 hands this year"
`onex_neo_hand_2026`. No datasheet sits behind that prose, and every capability the page names is
a video with no success rate, trial count or task definition.

Video is the second kind of evidence, and it carries no numbers. Tesla's Optimus Gen 2 was shown
on 13 December 2023 with a feature list reading "Faster, 11-DoF brand-new hands" and "Tactile
sensing on all fingers", over an egg pick-up with a fingertip force overlay
`tesla_optimus_hand_2025`. Sanctuary's release links an in-hand manipulation video with no task
list and no trial counts `sanctuary_phoenix_hand_2024`. Clone Robotics' whole evidence is a
teleoperated desk video of 15 November 2025, and the press item notes Clone "hasn't released a
full demo of the robot with the hand" `clone_robotics_hand_2024`.

Everything else is press or bibliography assertion. Tesla's V3 hand is known here only through a
Teslarati paraphrase of three patents filed in October 2024, because the USPTO PDF parsed empty
and the Wikipedia page returned HTTP 404 `tesla_optimus_hand_2025`. The repeated 22-DoF figure is
that article's arithmetic of four DoF on each of five fingers plus two at the wrist, and the
50-actuator figure is a bibliography claim. As manufacturer statements, both have no reachable
source.

Figure 03 is the clearest case of a number outrunning its source. The launch page
figure.ai/news/introducing-figure-03 returned HTTP 404, leaving a third-party tracker as the only
stored source `figure_03_hand_2025`. The repeated 16 DoF per hand and roughly 3 g of fingertip
sensitivity have no reachable source. Where the tracker does speak it contradicts them, listing
"Degrees of freedom, hands | 20" and "Number of fingers | 10" without saying whether either is
per hand or for the pair. The one fact both sources share is palm cameras, which are vision, not
tactile.

Boston Dynamics is the counterexample to five fingers, and its own CES blog of 5 January 2026
contains no hand content at all. The description comes from trade press: "a four-digit
gripper—three fingers and an opposable thumb—equipped with tactile sensing in the fingers and
palms" `boston_dynamics_atlas_hand_2026`. No DoF figure is stated, and the 7-DoF, 7-actuator
figure circulating for the 2025 three-finger hand has no reachable source.

Xiaomi shows a vendor-relayed number contradicting the circulating one. The 36kr page fetched
empty, leaving an Interesting Engineering article of 30 March 2026 relaying a WeChat post
`xiaomi_cyberone_hand_2026`. It says the redesign "increases active degrees of freedom by 83
percent" without giving an absolute count, and reports a 90.2 percent nut-fastening success rate
in a 76-second factory cycle. The figures in circulation are 64 percent and 98 percent, and both
contradict the only readable source. The hand's own DoF count has no reachable source.

Proception's ProHand belongs in Table 2, since a Y Combinator post and a TechCrunch article of
29 June 2026 state 22 degrees of freedom, tendon actuation and "integrated skin-like sensors",
with the first batch shipping that week `proception_prohand_2026`. Beyond the 22, nothing is
specified. Daxo's Muscle V0 is known only through the catalogue post, since
daxo-robotics.com returned HTTP 404, and the circulating "108 artificial muscles" and roughly
$1,200 prototype cost have no reachable source against that post's 120 actuators
`daxo_muscle_v0_2025`. AgiBot's OmniHand is worse: both store.agibot.com URLs returned HTTP 404
and the stored page holds no product text, so the circulating 16 DoF, 500 g, "400+ touch points"
and RMB 9,800 price all have no reachable source `agibot_omnihand_2025`. One method paper
nonetheless runs on an "AgiBot dexterous hand" `clutterdexgrasp_2025`, so the hand exists, is
used, and cannot be specified.

ByteDance's ByteDexter breaks the pattern. It has no vendor page here and no Table 3 row, because
its evidence is a technical report: 21 DoF per hand, linkage-driven, with piezoresistive tactile
fingertips, 16 of them present in the policy's action vector `gr_dexter_2025`. The Sharpa Wave is
the best-specified vendor page in the corpus and still ambiguous, because its spec table has two
unlabelled columns, so fingertip force reads "20 N | 12 N" and the fingertip array reads 240x240
at 180 fps or 60x60 at 30 fps `sharpa_wave_2026`.

The same divergence reaches the hands that are sold. Tesollo's page gives 1,763 g, Modbus and
Ethernet, while two published survey tables round the weight to 1.7 and 1.8 kg and one names
EtherCAT, which the page does not `tesollo_dg5f_2024`. The XHAND1 tracker page states no
fingertip force, a survey table gives 15 N and the bibliography gives an 80 N grip
`robotera_xhand1_2024`.

## 3.5 Tactile sensing as part of the hand

DIGIT set the cost floor. It is 20 by 27 by 18 mm, weighs about 20 g, streams 640x480 at 60 fps,
and its paper states a "total estimated manufacturing cost is approximately 15 USD per sensor ...
when manufactured in a batch of 1000" `digit_2020`. Durability was as much the contribution as
price: its gel degraded 0.3 percent over 15 abrasion passes, against 805 and 918 percent for the
two gels compared with it.

Digit 360 is the same lineage at a different operating point, claiming about 8.3 million taxels,
spatial features to 7 um, normal and shear force resolution of 1.01 mN and 1.27 mN, and
on-device processing that cuts event-to-action latency from 6 ms to 1.2 ms `digit360_2024`. It is
also not for sale. Units go at no charge to selected researchers, and no corpus paper's parsed
text names the sensor.

XELA's uSkin is the non-camera alternative and the one that bolts onto hands the field already
uses. Its curved fingertip kit for the Allegro V4 and LEAP carries 30 three-axis sensing points,
a full Allegro integration reaches 368, resolution is 0.1 gram-force, and the fingertip kit runs
at 275 Hz `xela_uskin_2020`. The 500 Hz figure often quoted belongs to the product family, not
the curved fingertip. One corpus paper names it, `sparsh_2024`.

Sparsh is the layer above. Its self-supervised encoders are pre-trained on 462.7k tactile images
spanning DIGIT, GelSight 2017 and GelSight Mini, and frozen Sparsh features beat matched
end-to-end models by 95.1 percent on average when both see 33 to 50 percent of the labels
`sparsh_2024`. Its own bead-maze policies never complete the maze on the real robot. It also
reports DIGIT at 320x240 where DIGIT's table says 640x480, which neither source resolves.

The usage number is the one to keep. Eight of 110 method rows feed a physical tactile signal into
a policy: `anyrotate_2024`, `articulated_tools_inhand_2025`, `dexteleop0_2026`, `dexumi_2025`,
`hato_visuotactile_2024`, `penspin_2024`, `robot_synesthesia_2023` and `rotateit_2023`.
Thirty-five of the 110 mention tactile somewhere. Almost none of the eight uses a
high-resolution sensor. PenSpin uses 20 binary contacts, five per fingertip `penspin_2024`, and
Robot Synesthesia uses 16 force-sensing resistors read as binary `robot_synesthesia_2023`. Two
papers exclude touch deliberately, HORA reporting rotation "even without the usage of vision and
tactile sensing" `hora_2022`, and ORCA's authors dropped it from their reinforcement learning
"due to the additional complexity involved in accurately modeling them" `orca_hand_2025`. Taxel
counts have risen by three orders of magnitude while the policies consuming them have stayed at
binary contact.

## 3.6 What is sold against what is published on

The bottom rows of Figure 2 carry the finding. None of the nine company-announced hands in
Table 3 appears in a single method row. Tesla, Figure, 1X, Sanctuary, Boston Dynamics, Xiaomi,
Clone, Daxo and PaXini together account for zero of the 110 method papers' experiments. The four
research prototypes in Table 3 are not in that position, since the Faive Hand and LEAP Hand v2
Advanced account for three method rows between them `graspxl_2024`, `bidex_teleop_2024`,
`dexwild_2025`. The clean claim is about company hands, not about Table 3 as a whole.

Table 3's emptiness is measurable and part of the same finding. Twenty-eight percent of its cells
are values no source stated, against 21 percent for the hands that can be bought. The hands with
the highest advertised DoF counts have the least specification behind them.

The one hand that crosses the gap crosses it because its maker published rather than announced.
ByteDexter reaches a method row through a ByteDance technical report with real-robot success
rates `gr_dexter_2025`, not through a product page. That mechanism is available to every vendor
in Table 3 and none of them has used it.

The gap runs the other way too, and the last column of Table 2 shows it. Hands that are sold,
documented and cheap go unused: the Unitree Dex5 with 94 pressure sensors on its P variant
`unitree_dex5_2025`, the fully actuated Tesollo DG-5F `tesollo_dg5f_2024`, ORCA `orca_hand_2025`,
RUKA `ruka_2025`, Ruka-v2 `ruka_v2_2026`, BiDexHand `bidexhand_2025` and DexHand
`dexhand_open_source_2023` take zero method rows each. A reader choosing a hand on this corpus's
evidence has two well-precedented options, an Allegro or an Inspire, and a third in LEAP if
eleven papers is enough. Everything else is a press release or a hand nobody has published a
result on.
