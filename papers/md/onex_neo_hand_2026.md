# NEO's Hands: An API to the Physical World (1X tendon-driven hand)

source entry: onex_neo_hand_2026


## https://www.1x.tech/discover/neos-hands

[](/)

[Neo](/neo)[AI](/ai)[Factory](/manufacturing)[Stories](/discover)[Careers](/careers)[About](/about)

[Order](/order)

[Watch](https://youtu.be/QRyXV3csReA)

# NEO’s Hands | An API to the Physical World

JUL 09 '261X

We’re excited to announce our breakthrough 25 Degree of Freedom (DOF), tendon-driven hands for the NEO humanoid platform– achieving near human-level dexterity, strength, safety, and reliability.

These hands are designed to do something fundamental: remove the hardware ceiling on what humanoid robots can actually do, and make data the only barrier to capabilities. By matching or surpassing human hands across the dimensions that matter, they ensure our AI models are no longer limited by dexterity. NEO can now perform virtually any task a human can do with their hands– with the precision, adaptability, and gentleness required for real-world environments.

This is what we’re shipping: not an end effector, but a true instrument. A hand is how a robot acts on the world, and our new NEO hands are the most capable ever built across nearly every metric.

## A humanoid is a computer whose API is its hands

Everything else: the model, the perception stack, the legs– determines how well the machine reaches the world. The hands determine what it can do there, what it can know about what it’s doing, and therefore what anyone building on it can do there. A humanoid with a two-finger gripper exposes three verbs to developers: pick, place, push. Every application anyone writes on that platform is a composition of those three verbs, forever– executed blind. The ceiling isn’t in the software. It’s at the end of the arm.These are the hands that will ship on every NEO. With them, we believe the hardware ceiling on what humanoid robots– and the developers building for them– can do is finally gone. What follows is the full engineering story behind them– the interface spec for acting on the world, the hardware that backs it, and why we believe this is the foundation our customers have been waiting for.

## You experience the world through your fingers

Watch a person meet an unfamiliar object and notice how little they look at it. They press it to find hardness. They slide a fingertip to read texture. They heft it for weight, trace the contour for shape, squeeze and release to feel it give. Touch is not a passive channel the way a camera is– it’s an experiment. The hand asks a question with force and reads the answer back through the same joints that asked it. That is how humans come to understand objects, and it is how we learned manipulation in the first place: by probing, millions of times, from the crib onward.

Which means a hand is not an actuator bolted to the end of a perception stack. It is a perception stack. An instrument. And its quality as an instrument is set by the whole machine at once. Writing the question takes precise force control. Reading the answer takes backdrivability and force transparency, so the world’s reaction flows back through the transmission instead of dying in a gearbox. Posing the question takes degrees of freedom and precision. Feeling the fine print takes skin. Catching a fast answer takes bandwidth. And asking millions of times takes robustness, because probing is contact and contact is wear.

## World-picture · assembled one subsystem at a time

RIGID GRIPPER\+ FORCE TRANSPARENCY\+ FINE MOTION\+ TACTILE SKIN\+ REFLEX & ROBUSTNESS

**Rigid gripper.** Position-controlled, numb through its own joints. It can act — barely, blindly — and perceive almost nothing. The world is a dark patch.

**\+ Force transparency.** Backdrivable tendons make every joint a sensor: press on the world and the answer comes back through the motor. The picture gains dynamic range — from a feather touch to a firm grip.

**\+ Fine motion.** Now the hand can pose, trace, and probe: turn things over, follow an edge, pinch a thread. Fine structure appears — resolution.

**\+ Tactile & shear skin.** Pressure, pressure change, slip — across the whole finger, not just a pad at the tip. The picture gains channels: now it’s cold milk, and shear says it’s starting to slide.

**\+ Reflex & robustness.** Reflex, built to probe. Fast enough to re-grip a slip before it finishes; durable enough to touch everything, all day. Full coverage: it knows the glass is at the edge, **and it won’t spill the milk.**

##   
The joints are sensors

Most robot hands are write-only devices. You command a position; the hand goes there; nothing meaningful comes back. The transmission is the reason: at the 100:1 and 200:1 gear ratios common in the field, friction swallows the contact forces before they ever reach the motor. The hand is numb through its own joints, so builders wrap it in external sensors and infer what’s happening at the fingertips — a camera pointed at a hand that can’t feel.

Our NEO hand is read-write. Developed from the ground up by our world-class engineering team, it runs quasi-direct-drive tendons via the 1X Tendon Drive at low gear ratios of approximately 5:1 to 15:1. All 25 degrees of freedom (22 fully actuated DoF in the fingers and palm, plus 3 at the wrist) are natively force-controlled and fully backdrivable. Push on a finger and it yields — and reports exactly how hard you pushed. Force flows out and information flows back through the same physical path. We call this force transparency, and it’s what turns a push into a measurement.

  
There’s a quieter read running alongside it: proprioception. Because every joint is closed-loop, the hand always knows its own configuration without looking, in the same way you can touch your fingertips together with your eyes shut. Pose plus effort, through the same 25 joints, all the time.

## Twenty-five ways to ask a question

  
What do 25 force-transparent degrees of freedom actually buy? Not joints for their own sake– a repertoire of grasps and of questions. The allocation matters more than the count: our DoF are distributed the way anatomy distributes them, biased toward a thumb that genuinely opposes. This architecture was chosen as the optimal balance between human-like manipulation capability and practical manufacturing, control, and serviceability.

The result speaks for itself. These new hands match or exceed human performance in fine manipulation. NEO can assemble LEGO structures, pick up individual screws and coins from a wallet, spin and install light bulbs, use a screwdriver, rotate objects in-hand, zip a jacket, sort grapes by color, pour tea from a kettle, catch a squishy ball, plug in a USB-C charger, grab a wine glass, wipe surfaces with a paper towel and spray, and communicate via sign language, and infinitely more.

Fruit Picking

These 25-DoF hands are IP68 waterproof and food-safe, allowing NEO to wash its own hands like a human. Far from fragile, they deliver powerful, useful strength: Peak torques reach 3.5 Nm at the thumb CMC and 2.6 Nm at the finger MCP joints, with distal flexion forces up to 45N. The wrist delivers 17.75 Nm of torque. This enables strong whole-hand grasps, tool use, lifting and carrying, opening doors, pushing loaded carts, and precision pinch under load, all while retaining full dexterity. With ±0.2 mm positioning accuracy, they work (and perceive) in the small-object regime where most human labor actually happens. Those aren’t demo modes. They’re the natural output of enough independent, force-controlled DoF at human scale.

Lift

## The last half-millimeter

The skin adds the channels. Tactile data is an image– it has dynamic range, resolution, channels, and field of view. Our hands feature rich, high-resolution tactile sensing across the fingertips and surfaces, measuring normal force, contact location, and shear. This enables NEO to detect when objects begin to slip and respond in real time. Visualizations show contact normals, pressure heatmaps during handshakes, and delicate grasping of fragile origami without damage.

Force Sensing

  
The skin is co-designed with the sensors inside it and the tendons behind it. It is a functional material, not a cosmetic one. Because vision alone is insufficient for many tasks (especially with small, transparent, deformable, or occluded objects), this contact feedback is critical for adaptive, intelligent manipulation.

## Fast enough to catch it. Tough enough to keep asking

Perception through action has a clock speed. Feel the slip begin through the shear channel; re-grip through the transparent joints before it finishes.

And a hand that learns by touching everything must survive touching everything. These hands are built for continuous operation and maintain performance after millions of interaction cycles. Reliability was designed into every subsystem and component: tendon routing, bearings, finger structures, electrical cable routing, tactile integration, electronics, and assembly procedures. Components and full finger assemblies have undergone millions of test cycles, drive units have been tested at extreme temperatures, and wrist joints have been proven reliable well beyond 2 million cycles under high loads.

  
The whole hand is sealed to IP68 with food-safe materials, so it works at the sink and washes itself when dirty. Compliance closes the loop on safety: extremely low gear ratios, combined with the tendon drive and low distal inertia, allow external impacts to safely backdrive the fingers. Slow-motion footage shows the hands yielding when slapped, hit with a hammer, pinched in a closing drawer, or slammed into Styrofoam. A machine that perceives by touching had better be gentle by construction, because the world it needs to touch has people in it.

## The hardware behind the instrument

An API is only as good as its physical layer. The motors live in the forearm, where most of your own grip strength lives– pulling proprietary tendons through the wrist. This is how a lightweight hand produces such high forces while running cool enough for continuous operation.

  
  
Our hands are designed as an integral part of the full NEO stack– tightly integrating in-house motors, custom electronics, embedded sensing, proprietary tendon systems, compact transmissions, and hand-specific firmware. This deep vertical integration enables rapid iteration and compounding improvements that modular approaches simply cannot match. Every grasp is an experiment.

Now put the halves together. A hand that perceives by acting turns every task into an experiment: every joint reports force, every fingertip reports contact and shear, every pose is known. Every grasp your policy takes arrives pre-labeled, and every probe returns a measurement. This is the substrate learning-based manipulation has been waiting on, and it’s the same loop children run: act, feel, update, act again.

One more number, and it’s the strategic one: hundreds of these hands have already come off a scalable production line. We manufacture NEO’s 25 DoF hands on our dedicated line using high-yield processes with full end-of-line testing. Every unit is built end-to-end in-house — from tendon materials and 1X Motors to the final soft polymers, skin, and tactile sensing stack. This gives us the capacity to produce 10,000 hands this year.That’s not a manufacturing footnote, it’s the whole strategy. A hand that can’t be built at scale can’t run experiments at scale, and without data at scale there is no embodied AGI.For seventy years, robotics worked around the hand problem. The humanoid bet is the reverse. And it lives or dies at the fingertips. We built the hand for this world. One that’s strong enough to act in it, transparent enough to see it, and durable enough to keep learning from it. Soon it will be your instrument.

“Our goal was never a hand that just looks impressive on paper. These hands are the culmination of intensive engineering focused on making humanoids truly useful. We built them to match or surpass human capability across every dimension that matters. With these hands, NEO crosses a critical threshold. The robot can now do the things humans do with their hands, every day. This is what the industry has been waiting for.”

Bernt Børnich, CEO and Founder of 1X  
  


## Discover

#### [Welcoming Bill Nash as CFOBill brings extensive financial leadership experience from some of the most technically ambitious and fast-moving companies in autonomy, aerospace, and life sciences.JUL 02 '261X](/discover/bill-nash-cfo)

#### [Welcoming Tom Sanocki as VP of EngineeringTom joins the 1X team with a remarkable track record of building and scaling software organizations that have reached millions of people.JUN 25 '261X](/discover/tom-sanocki-vp-engineering)

#### [The 1X World Model Lab | Est. 20261X Launches World Model Lab to Scale Humanoid Intelligence, Appoints Sam Sinha as Head of World Models and Founding ResearcherJUN 04 '261X](/discover/1x-world-model-lab)

## ExperienceNEO

Join waitlist

Opt in to receive updates. Unsubscribe anytime.

[](/)1X © 2026

[NEO](/neo)[Careers](/careers)[AI](/ai)[Factory](/manufacturing)[About](/about)[Stories](/discover)[Robot Fleet](/robot-fleet)[Logs](/logs)

[LinkedIn](https://www.linkedin.com/company/1x-technologies)[YouTube](https://www.youtube.com/@1X-tech)[Instagram](https://www.instagram.com/1x.technologies/)[TikTok](https://www.tiktok.com/@1x.tech)[X](https://x.com/1x_tech)

[Terms of Use](/terms-and-conditions)[Privacy & Cookies](/privacy-policy)[Press](/press)[Support](/support)

[Get Updates](/get-updates)[Investor Relations](/investor-relations)
