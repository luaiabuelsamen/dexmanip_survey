# taxim_2021 — Taxim: An Example-based Simulation Model for GelSight Tactile Sensors (Si, Yuan; IEEE RA-L 2022, arXiv 2021)

sources: papers/md/taxim_2021.md [24feb040] ; code/md/taxim_2021.md [4936657a]

## One-line contribution
An example-based (calibrated-from-real-data, not physics-simulated) GelSight tactile simulator combining a polynomial photometric-stereo optical model, a shadow-mask compositing model, and a superposition-principle marker-motion field model, calibrated from under 100 real indentation datapoints, that beats TACTO/Phong/physics-based baselines on optical realism and is the fastest of the compared methods on CPU (Abstract).

## Setting
- hand(s): none — bench-mounted GelSight and DIGIT sensors on an XYR optical stage with a vertically-actuated indenter (Sec. IV-A, Fig. 4), not attached to a robot hand in this paper.
- simulator / physics: not a rigid-body/MPM physics simulator — Taxim is an example-based/data-driven optical+mechanical model. Optical response comes from an example-based photometric-stereo polynomial lookup table (Sec. III-B); elastic marker-motion comes from a linear-displacement/superposition model calibrated against a separate FEM (ANSYS) simulation (Sec. III-D).
- observation: what signal is simulated — (1) an **optical (RGB) image**, the GelSight/DIGIT-style camera imprint, via the polynomial-table photometric-stereo mapping from surface normal to pixel intensity plus a synthesized shadow mask; (2) a **marker-motion (flow) field**, i.e. per-marker 3D surface displacement under normal + shear loads, via the superposition of "unit" load responses. No raw normal-force array is output as a first-class signal (contact geometry/height map is the intermediate representation).
- objects / data: 3D-printed test objects (10×10 mm or 15×15 mm base) of varying shape/texture designed in Solidworks (Fig. 7); calibration uses 50 datapoints from a 4 mm spherical indenter (optical) and 10 datapoints from a 1 mm pin indenter (shadow), collectable "within 1 hour" (Sec. IV-B). Marker-motion evaluation load displacement ranges 0.3-0.8 mm (Sec. IV-C).

## Physics block
This is not a rigid-body contact-solver paper; "Physics block" here covers Taxim's mechanical/optical model in place of a contact solver:
- contact model: a collision is detected when an indenter/object contacts the gelpad; the local contact shape is represented as a height map built from the object's geometry in the contact region and the gelpad's geometry elsewhere, then smoothed at the contact/non-contact boundary with pyramid Gaussian kernels to approximate soft-body deformation ("an approximation of soft body simulation," Sec. III-B "Simulation"). This is a heightfield/geometric approximation, not a force-based contact solve.
- solver and iterations: none in the rigid-body-physics sense. The optical mapping is a single polynomial-table lookup (no iteration); the marker-motion model solves for "virtual displacements" of active (in-contact) mesh nodes via a linear system built from a pre-calibrated 3×3 influence tensor T (stacked equations, solved once per contact event, not iteratively refined) (Sec. III-D).
- differentiability: not discussed/not implemented.
- timestep: not applicable — Taxim operates on static/quasi-static indentation snapshots, not a time-stepped dynamical simulation. The authors state this explicitly as a limitation (see below): "currently we simulate the quasi-static contact" (Sec. V).
- friction model: not modeled as a force law; shear/tangential loading is handled only at the marker-motion level (loads on active nodes decomposed into z, x, y virtual displacements via the same superposition tensor T, Sec. III-D), not as a Coulomb-type friction force.
- how penetration is resolved / is depth exposed: penetration/indentation depth is the primary *input* to the model (not something resolved by a solver) — the real calibration rig measures indentation depth to 0.01 mm precision via a vertical linear stage (Sec. IV-A), and the optical/marker models are functions of that known depth and the resulting height map; there is no separate "interpenetration artifact" concept here since there is no rigid-body dynamics being integrated.
- GPU or CPU: CPU, in the reported speed test; the authors note their method "can be potentially optimized for GPU computation as well" (future work) but this is not implemented in the paper (Sec. IV-B "Speed test").
- throughput with the table and hardware: speed test on an "AMD Ryzen Threadripper 2950X 16-Core Processor CPU," input height maps 480×640, average running FPS (Table II): **Ours w/o shadows** 18.1 FPS; **Ours w/ shadows** 9.6 FPS; **Physics-based [12]** 0.1 FPS; **TACTO [14]** 1.9 FPS; **Phong's [13]** 3.8 FPS. The authors note TACTO and the physics-based model "can be largely accelerated on GPUs but not considered here for evaluation," so this is a CPU-only comparison (Sec. IV-B).

## Tactile-specific fields
- signal simulated: optical RGB image (photometric-stereo intensity model + shadow compositing) and marker-motion displacement field (X/Y/Z per marker/mesh node). No raw force field is output; force enters only as the load boundary condition on active nodes for the marker-motion model.
- real sensor calibrated against: GelSight (dome-shaped gelpad, four different physical GelSight units used across figures/experiments, Sec. IV-B "Simulation on various sensors and objects") and, separately, a DIGIT sensor (Fig. 10) — demonstrating the calibration procedure transfers across GelSight-family hardware with per-sensor recalibration.
- reported sim-to-real error, with its table:
  - **Optical simulation vs. real** (Table I, image-similarity on cropped 400×400 contact regions, GIMP-aligned): Taxim L1=**5.565**, MSE=**58.358**, SSIM=**0.882**, PSNR=**30.974** — best on all four metrics vs. TACTO (L1=10.861, MSE=215.861, SSIM=0.808, PSNR=25.495), Phong's model (L1=8.163, MSE=123.249, SSIM=0.832, PSNR=27.763), and a cited physics-based model (L1=7.409, MSE=90.623, SSIM=0.759, PSNR=28.687).
  - **Marker-motion vs. FEM** (dense-mesh comparison, Sec. IV-C): mean interpolated pixel-wise L1 error over the gelpad surface = 3.58×10⁻³ mm (X), 3.32×10⁻³ mm (Y), 5.43×10⁻³ mm (Z), 5.40×10⁻³ mm (XY/gelpad-surface).
  - **Marker-motion vs. real + FEM jointly** (Sec. IV-C): mean marker-motion-magnitude L1 error = 1.00×10⁻² mm (real vs. FEM), 1.02×10⁻² mm (real vs. Taxim), 3.96×10⁻³ mm (FEM vs. Taxim) — i.e. Taxim tracks the FEM reference (3.96×10⁻³ mm) about as tightly as FEM tracks real data (1.00×10⁻² mm), and Taxim-vs-real (1.02×10⁻² mm) is essentially the same magnitude as FEM-vs-real.

## Evaluation
- metrics (exact definitions): L1 (mean absolute pixel error), MSE, SSIM, PSNR for optical images (Table I); FPS for the speed test (Table II); mean interpolated pixel-wise L1 displacement error (mm) for marker motion vs. FEM and vs. real (Sec. IV-C).
- headline numbers: see the sim-to-real table above (Table I, Table II, and the two marker-motion error sets).
- baselines beaten: TACTO, Phong's reflection model, and a cited physics-based optical model — beaten on all four optical-similarity metrics (Table I) and on CPU speed except for the "with shadows" variant which trades some speed for the shadow feature (Table II).
- real robot? none — bench-top indenter rig only (Sec. IV-A); no robot arm/hand manipulation trial in this paper.

## Limitations stated by the authors
- "currently we simulate the quasi-static contact, and we plan to investigate the dynamic contact process and simulate the dynamic phenomena such as slip" (Sec. V).
- "The simulation pipeline can be computationally improved by applying GPU acceleration" (Sec. V) — i.e. the reported 9.6-18.1 FPS is a CPU-only number and is explicitly flagged as improvable.
- Calibration is per-sensor: "these parameters vary for different sensors, this process has to be done per sensor" (Sec. III-B "Calibration"), though it needs "less than 100 data points" and "can be accomplished within 1 hour" and reused "till any components of the sensor are replaced or the sensor is broken."
- Most artifacts in results on Google-Scan-dataset objects "come from the coarse mesh files of the objects" rather than the simulation model itself (Fig. 11 caption).

## Quotable claims (verbatim, with section)
- "Our method is computationally lightweight, easy to set up and use, and simple to apply to different sensors." (Sec. V)
- "Our method outperforms all the other methods." (Sec. IV-B, re: Table I)
- "This is the first integrated work considering both the optical and marker motion simulation." (Sec. V)
- "It also incorporates the sensor's illumination features and system noise through calibration with examples from real sensors." (Sec. V)

## Notes for the survey
- Taxim's Table I is the paper's own head-to-head against TACTO, giving the survey a direct, single-source optical-fidelity ranking (Taxim > Phong > physics-based-model > TACTO on 3 of 4 metrics, TACTO worst on all 4) — cite this table rather than re-deriving a ranking across the `tacto_2020` and `taxim_2021` notes separately.
- Taxim is explicitly example-based/calibration-driven, not a first-principles soft-body physics simulator; its marker-motion model is itself calibrated against a separate FEM (ANSYS) ground truth (Sec. III-D "Calibration"), so its ~1×10⁻² mm real-vs-Taxim marker error is bounded below by the ~1×10⁻² mm real-vs-FEM error of the calibration reference itself — the two are not fully independent measurements.
- Cross-reference: `tactile_genesis_2026`'s `ElastomerTaxel` sensor explicitly builds on HydroShear rather than Taxim's method, but cites Taxim as the standard way to turn its own `ContactDepthProbe` output into a renderable RGB tactile image — Taxim remains the reference optical-rendering step even in more recent GPU-parallel tactile platforms.
- Code md provenance: `code/md/taxim_2021.md` (6,492 chars) is README + minimal file tree; no polynomial-table or marker-motion source code was captured, so all numeric detail above is from the paper text.
