# groot_n1_2025

source: https://github.com/NVIDIA/Isaac-GR00T


commit: 51d4c89f72fda44cbf77285c6a8114b52676b8a1


## README

<div align="center">

  <img src="media/header_compress.png" width="800" alt="NVIDIA Isaac GR00T N1.7 Header">

  <!-- --- -->

  <p style="font-size: 1.2em;">
    <a href="https://developer.nvidia.com/isaac/gr00t"><strong>Website</strong></a> |
    <a href="https://huggingface.co/collections/nvidia/gr00t-n17"><strong>Model</strong></a> |
    <a href="https://huggingface.co/collections/nvidia/physical-ai"><strong>Datasets (Physical AI)</strong></a> |
    <a href="https://arxiv.org/abs/2503.14734"><strong>Paper</strong></a> |
    <a href="https://developer.nvidia.com/isaac"><strong>NVIDIA Isaac</strong></a> |
    <a href="FAQ.md"><strong>FAQ</strong></a>
  </p>
</div>

## Table of Contents

- [NVIDIA Isaac GR00T](#nvidia-isaac-gr00t)
- [What's New in GR00T N1.7](#whats-new-in-gr00t-n17)
- [Installation](#installation)
- [LeRobot Integration](#lerobot-integration)
- [Model Checkpoints & Embodiment Tags](#model-checkpoints--embodiment-tags)
- [Data Format](#data-format)
- [Inference](#inference)
- [Fine-tuning](#fine-tuning)
- [Evaluation](#evaluation)
- [Contributions](#contributions)
- [License](#license)
- [Citation](#citation)

---

## NVIDIA Isaac GR00T

<table style="width:100%; table-layout:fixed;">
  <tr>
    <td style="width:33.33%; text-align:center;">
      <img src="media/unitree_g1.gif" style="max-width:100%; height:auto;">
    </td>
    <td style="width:33.33%; text-align:center;">
      <img src="media/agibot_g1.gif" style="max-width:100%; height:auto;">
    </td>
    <td style="width:33.33%; text-align:center;">
      <img src="media/yam.gif" style="max-width:100%; height:auto;">
    </td>
  </tr>
</table>

> We just released GR00T N1.7 General Availability, the latest version of GR00T N1 with a new VLM backbone (Cosmos-Reason2-2B / Qwen3-VL) and improved performance.

> **This is a General Availability (GA) release.** You are welcome to download the model, explore the codebase, and build on the stack, with full support and stability guarantees.
>
> **What's available:**
> - Pre-trained GR00T N1.7 model weights and reference code
> - Fine-tuning and inference with custom robot data or demonstrations
> - Experimentation, prototyping, and research use cases
> - Production deployment with commercial support
> - Complete benchmarks and a fully validated, stable feature set
> - Pull request contributions
>
> We welcome feedback - please feel free to raise issues and pull requests in this repository.

> Previous releases: [N1.6](https://github.com/NVIDIA/Isaac-GR00T/tree/n1d6) | [N1.5](https://github.com/NVIDIA/Isaac-GR00T/tree/n1d5)

NVIDIA Isaac GR00T N1.7 is an open vision-language-action (VLA) model for generalized humanoid robot skills. This cross-embodiment model takes multimodal input, including language and images, to perform manipulation tasks in diverse environments.

GR00T N1.7 is trained on a diverse mixture of robot data including bimanual, semi-humanoid and an expansive humanoid dataset. It is adaptable through post-training for specific embodiments, tasks and environments.

GR00T N1.7 is fully commercially licensable under Apache 2.0. It delivers comparable performance to N1.6, with improved generalization and language-following capabilities driven by the inclusion of 20K hours of EgoScale human video data in pretraining.

The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model and diffusion transformer head that denoises continuous actions. Here is a schematic diagram of the architecture:

<div align="center">
<img src="media/model-architecture.png" width="800" alt="model-architecture">
</div>

### Workflow Overview

1. **Prepare data** — Collect robot demonstrations (video, state, action) and convert them to the [GR00T LeRobot format](#data-format). Demo datasets are included for quick testing.
2. **Run inference** — Try zero-shot inference with the base model on [pretrain embodiments](#embodiment-tags), or use a [finetuned checkpoint](#checkpoints) for benchmark tasks.
3. **Fine-tune** — Adapt the model to your robot using [`launch_finetune.py`](#fine-tuning) with your own data and modality config.
4. **Evaluate** — Validate with [open-loop evaluation](#open-loop-evaluation), then test in [simulation benchmarks](#benchmark-examples) or on real hardware via the [Policy API](getting_started/policy.md).
5. **Deploy** — Connect `Gr00tPolicy` to your robot controller, optionally accelerated with [TensorRT](scripts/deployment/README.md).

## What's New in GR00T N1.7

GR00T N1.7 builds on N1.6 with a new VLM backbone and code-level improvements.

1. **Relative EEF Action Space** — N1.7 adopts a relative end-effector action space shared across robot and human embodiments. Representing actions as deltas from the current pose (rather than absolute targets) improves generalization and is a key factor in the model's cross-embodiment performance. See [`getting_started/finetune_new_embodiment.md`](getting_started/finetune_new_embodiment.md) for guidance on configuring relative EEF for your own robot.

2. **Human Video Pretraining** — N1.7 is pretrained on 20K hours of EgoScale human video data alongside diverse robot demonstrations. Because the relative EEF action representation is consistent across both human and robot data, the model can transfer manipulation priors learned from human video directly to robot control.

### Key Changes from N1.6

Compared with N1.6, N1.7 updates the model stack, training data interface,
evaluation coverage, deployment flow, fine-tuning workflow, and runtime behavior.

- **New VLM backbone:** Cosmos-Reason2-2B (Qwen3-VL architecture), replacing the Eagle backbone used in N1.6. Supports flexible resolution and encodes images in their native aspect ratio without padding.
- **Updated model interface:** N1.7 moves to the `gr00t_n1d7` model package, expands the state/action dimensions, and increases the model action horizon.
- **More flexible dataset handling:** Fine-tuning can use multiple dataset paths with mixture weighting, making multi-dataset training easier to configure.
- **Broader benchmark coverage:** N1.7 refreshes and expands documented results across RoboCasa, RoboCasa GR1 tabletop tasks, SimplerEnv, and real G1 evaluation.
- **More complete deployment path:** N1.7 adds full-pipeline ONNX and TensorRT export support and improves deployment consistency across desktop GPUs and edge platforms.
- **More predictable runtime behavior:** Policy serving, rollout recording, evaluation, and configuration validation have been hardened so errors are easier to diagnose.

<details>
<summary>Detailed changes from N1.6</summary>

These are the main code, model, training, evaluation, and deployment changes
that distinguish the current N1.7 main branch from the N1.6 / 1D6 code path.
Use the [`n1d6` branch](https://github.com/NVIDIA/Isaac-GR00T/tree/n1d6) when you need
the N1.6 model package and runtime behavior.

- Model package changed from `gr00t_n1d6` to `gr00t_n1d7`, so codepaths and processor metadata move to the N1.7 namespace.
- VLM backbone changed from vendored Eagle, `nvidia/Eagle-Block2A-2B-v2`, to `nvidia/Cosmos-Reason2-2B` via Qwen3-VL.
- Transformers changed from `4.51.3` to `4.57.3` to support the newer Qwen3-VL stack.
- Model defaults changed: `select_layer` `16` to `12`, `tune_top_llm_layers` `4` to `0`, and `load_bf16` `true` to `false`.
- State and action dimensions expanded from `29` to `132`, and `action_horizon` expanded from `16` to `40`.
- Action head remains flow-matching DiT, but changes from `32` to `16` diffusion layers and adds newer N1.7 behavior options.
- Dataset input handling now supports multiple dataset paths and `ds_weights_alpha` for dataset mixtures.
- The rollout CLI flag was renamed from `--action-horizon` to `--execution-horizon` to clarify how many predicted actions are executed per policy call.
- Server/client transport has stronger object-dtype ndarray serialization and cleaner socket timeout behavior.

</details>

---

## Installation

### Hardware Requirements

**Inference:** 1 GPU with 16 GB+ VRAM (e.g., RTX 4090, L40, H100, Jetson AGX Thor/Orin, DGX Spark).

**Fine-tuning:** 1 or more GPUs with 40 GB+ VRAM recommended. We recommend H100 or L40 nodes for optimal performance. Other hardware (e.g., A6000) works but may require longer training time. See the [Hardware Recommendation Guide](getting_started/hardware_recommendation.md) for detailed specs.

**CUDA / Python per platform:** dGPU on CUDA 12.8 with Python 3.12; Jetson Thor and Orin on JetPack 7.2 / CUDA 13.2 with Python 3.12; DGX Spark on CUDA 13.0 with Python 3.12. The per-platform install scripts and Dockerfiles live under `scripts/deployment/`; see the [Deployment & Inference Guide](scripts/deployment/README.md) for the full matrix.

### Clone the Repository

GR00T relies on submodules for certain dependencies. Include them when cloning:

**Note:** `git-lfs` is **required** to download parquet data files in `demo_data/`. Install it before cloning: `sudo apt install git-lfs && git lfs install`.
```sh
git clone --recurse-submodules https://github.com/NVIDIA/Isaac-GR00T
cd Isaac-GR00T
```

If you've already cloned without submodules, initialize them separately:

```sh
git submodule update --init --recursive
```

### Set Up the Environment

GR00T uses [uv](https://github.com/astral-sh/uv) for fast, reproducible dependency management. Install uv first:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### dGPU (x86_64) — Default

Install FFmpeg (required by `torchcodec`, the only supported video backend):
```sh
sudo apt-get update && sudo apt-get install -y ffmpeg
```
> **FFmpeg version:** `torchcodec==0.8.0` supports **FFmpeg 4-7 only**. On Ubuntu 25.10+/26.04 the `ffmpeg` package is version 8, which `torchcodec` cannot load (`RuntimeError: Could not load libtorchcodec ... We support versions 4, 5, 6 and 7`). On those distros install an FFmpeg&lt;8 runtime instead, e.g. `conda install -c conda-forge 'ffmpeg<8'`, and make sure its libraries are on `LD_LIBRARY_PATH`.

Create the environment and install GR00T:
```sh
uv sync --python 3.12
```
GPU dependencies (flash-attn, TensorRT, etc.) are included in the default install.

Verify the installation:
```sh
uv run python -c "import gr00t; print('GR00T installed successfully')"
```

> **Hugging Face access (required):** GR00T's VLM backbone is [`nvidia/Cosmos-Reason2-2B`](https://huggingface.co/nvidia/Cosmos-Reason2-2B), a **gated** model that every GR00T checkpoint (including the base `nvidia/GR00T-N1.7-3B`) loads on first use. Before running inference or finetuning, request access on the model page and authenticate:
> ```sh
> uv run huggingface-cli login   # or: export HF_TOKEN=<your_token>
> ```
> Without access, model loading fails with a `GatedRepoError` / `401 Client Error`.

> **`flash-attn` message on every `uv run`:** You may see `Installing flash-attn...` each time you run `uv run`. This is a known `uv` behavior with URL-pinned wheel sources — `uv` re-validates the cached wheel against the source URL on each invocation. It is **not** rebuilding from source; the wheel is already cached locally and the operation takes 2-3 seconds. This affects platforms that use URL-pinned flash-attn wheels (x86_64 and aarch64). 
> To suppress it, remove the `flash-attn` entries under `[tool.uv.sources]` in your local `pyproject.toml` after the initial install. But that will break `uv lock` and cause flash-attn to build from source on next lock regeneration.

<details>
<summary><strong>Alternative: pip install (without uv)</strong></summary>

If you prefer pip/conda over uv, create a Python 3.12 virtualenv and install:
```sh
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e .
```
Note: GPU dependencies (flash-attn, TensorRT) may require manual installation with pip. The `uv` workflow handles these automatically.
</details>

> **If fine-tuning fails with `CUDA_HOME is unset`:** Run `bash scripts/deployment/dgpu/install_deps.sh` once to configure CUDA paths, or manually `export CUDA_HOME=/usr/local/cuda`.

> **CUDA 13.x Users (Thor, Spark, and other CUDA 13+ platforms):** PyTorch 2.7 pins Triton to 3.3.1, which does not recognize CUDA major version 13+. This causes a `RuntimeError` in Triton's `ptx_get_version()`. Run `scripts/patch_triton_cuda13.sh` to fix:
> ```sh
> uv run bash scripts/patch_triton_cuda13.sh
> ```

> **GB300 (sm_103) Users:** Triton 3.3.1 (pinned by PyTorch 2.7) does not support the GB300 GPU architecture (sm_103). `torch.compile` will fail on GB300. Use PyTorch eager mode or TensorRT inference instead. Triton 3.5.1+ adds sm_103 support but is not yet compatible with the pinned PyTorch version.

> **Video Backend:** GR00T uses [`torchcodec`](https://github.com/pytorch/torchcodec) as its sole video decoding backend. Backends such as `decord` and `pyav` are no longer supported. The default dGPU install pins `torchcodec` 0.8.0, which requires **FFmpeg 4-7** (FFmpeg 8 is not supported — see the FFmpeg version note above) and supports H.264 on all platforms; AV1 decoding is not guaranteed (convert AV1 datasets to H.264 with `examples/SimplerEnv/convert_av1_to_h264.py`). JetPack 7.2 Thor and Orin use the PyTorch cu132 `torchcodec` 0.15.0 wheel; Spark may build `torchcodec` from source during `install_deps.sh` when a platform wheel is not available.

<details>
<summary><strong>DGX Spark</strong> (tested with DGX Spark GB10)</summary>

```bash
bash scripts/deployment/spark/install_deps.sh
source .venv/bin/activate
source scripts/activate_spark.sh
```

See the [Spark setup guide](scripts/deployment/README.md#dgx-spark-setup) for Docker and bare metal details.
</details>

<details>
<summary><strong>Jetson AGX Thor</strong> (tested with JetPack 7.2)</summary>

```bash
bash scripts/deployment/thor/install_deps.sh
source .venv/bin/activate
source scripts/activate_thor.sh
```

See the [Thor setup guide](scripts/deployment/README.md#jetson-thor-setup) for Docker and bare metal details.
</details>

<details>
<summary><strong>Jetson Orin</strong> (tested with JetPack 7.2)</summary>

```bash
bash scripts/deployment/orin/install_deps.sh
source .venv/bin/activate
source scripts/activate_orin.sh
```

See the [Orin setup guide](scripts/deployment/README.md#jetson-orin-setup) for Docker and bare metal details.
</details>

> ⚠️ **aarch64 users (Spark / Thor / Orin):** After running `install_deps.sh`, always
> activate the venv with `source .venv/bin/activate && source scripts/activate_<platform>.sh`
> (`activate_spark.sh`, `activate_thor.sh`, or `activate_orin.sh`) and run the example
> commands in this guide with **plain `python`** / `torchrun`, not `uv run python` /
> `uv run torchrun`. The latter will re-sync against the root `pyproject.toml` (which targets
> x86_64 Python 3.12) and destroy the platform-specific environment. See the
> [Deployment & Inference Guide](scripts/deployment/README.md#platform-specific-setup) for
> per-platform Docker and bare-metal setup.


For a containerized setup that avoids system-level dependency conflicts, see our [Docker Setup Guide](docker/README.md). The recommended container workflow is to start the image first, then clone or pull the repo inside the running container so your checkout uses the image's prebuilt dependency environment.

---

## LeRobot Integration

GR00T N1.7 is also available through Hugging Face LeRobot via the `groot` policy type. Use the [LeRobot GR00T documentation](https://github.com/huggingface/lerobot/blob/main/docs/source/groot.mdx) for LeRobot-native training, evaluation, and rollout workflows. Use this repository for the reference GR00T implementation, model internals, deployment tooling, and benchmark-specific examples.

---

## Model Checkpoints & Embodiment Tags

### Checkpoints

| Checkpoint | Type | Embodiment Tag | Description |
|------------|------|---------------|-------------|
| [`nvidia/GR00T-N1.7-3B`](https://huggingface.co/nvidia/GR00T-N1.7-3B) | Base | See [pretrain tags](getting_started/policy.md#--embodiment-tag) | Base model (3B params) — zero-shot inference on pretrain embodiments, or finetune for new tasks |
| [`nvidia/GR00T-N1.7-LIBERO`](https://huggingface.co/nvidia/GR00T-N1.7-LIBERO) | Finetuned | `LIBERO_PANDA` | Finetuned on [LIBERO](https://libero-project.github.io/) benchmark (Franka Panda) |
| [`nvidia/GR00T-N1.7-DROID`](https://huggingface.co/nvidia/GR00T-N1.7-DROID) | Finetuned | `OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT` | Finetuned on [DROID](https://droid-dataset.github.io/) dataset |
| [`nvidia/GR00T-N1.7-SimplerEnv-Bridge`](https://huggingface.co/nvidia/GR00T-N1.7-SimplerEnv-Bridge) | Finetuned | `SIMPLER_ENV_WIDOWX` | Finetuned on SimplerEnv Bridge (WidowX) |
| [`nvidia/GR00T-N1.7-SimplerEnv-Fractal`](https://huggingface.co/nvidia/GR00T-N1.7-SimplerEnv-Fractal) | Finetuned | `SIMPLER_ENV_GOOGLE` | Finetuned on SimplerEnv Fractal (Google Robot) |

### Embodiment Tags

Every inference or finetuning command requires an `--embodiment-tag`. The tag determines which modality config (state/action keys, normalization) the model uses. Tags are **case-insensitive**.

For the full list of pretrain and posttrain tags, see the [Policy API Guide — Embodiment Tags](getting_started/policy.md#--embodiment-tag).

---

## Data Format

GR00T uses a flavor of the [LeRobot v2 dataset format](https://github.com/huggingface/lerobot) with an additional `meta/modality.json` file that describes state/action/video structure. A dataset looks like:

```
my_dataset/
  meta/
    info.json            # dataset metadata
    episodes.jsonl       # episode index and lengths
    tasks.jsonl          # language task descriptions
    modality.json        # state/action/video key mapping (GR00T-specific)
  data/chunk-000/        # parquet files (state, action per timestep)
  videos/chunk-000/      # mp4 video files per episode
```

The `modality.json` maps how the concatenated state/action arrays split into named fields (e.g., `x`, `y`, `z`, `gripper`) and which video keys are available. This is what the embodiment tag uses to interpret the data.

**Included demo datasets** (ready to use, no download needed):

| Dataset | Robot | Embodiment Tag | Use Case |
|---------|-------|---------------|----------|
| `demo_data/droid_sample` | DROID (3 episodes) | `OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT` | Zero-shot or finetuned inference (DROID) |
| `demo_data/libero_demo` | LIBERO Panda (5 episodes) | `LIBERO_PANDA` | Inference with finetuned checkpoint |
| `demo_data/simplerenv_bridge_sample` | WidowX (SimplerEnv Bridge) | `SIMPLER_ENV_WIDOWX` | Inference with finetuned SimplerEnv Bridge checkpoint |
| `demo_data/simplerenv_fractal_sample` | Google Robot (SimplerEnv Fractal) | `SIMPLER_ENV_GOOGLE` | Inference with finetuned SimplerEnv Fractal checkpoint |
| `demo_data/cube_to_bowl_5` | SO100 arm (5 episodes) | `NEW_EMBODIMENT` | Fine-tuning custom embodiment example |
| `demo_data/cube_to_bowl_5_with_mask` | SO100 arm + per-frame masks | `NEW_EMBODIMENT` | [Mask-guided background suppression](examples/mask-guided-background-suppression/README.md) example |

> To generate more DROID episodes: `python scripts/download_droid_sample.py --num-episodes 10`

**Using your own data:** Convert your demonstrations to the format above. If coming from LeRobot v3, use the conversion helper in its own environment:
```bash
cd scripts/lerobot_conversion
uv venv
source .venv/bin/activate
uv pip install -e . --verbose
python convert_v3_to_v2.py --repo-id <DATASET_REPO_ID>
```
See the full [Data Preparation Guide](getting_started/data_preparation.md) for schema details and examples.

---

## Inference

> **Prefer an interactive walkthrough?** The [`getting_started/GR00T_inference.ipynb`](getting_started/GR00T_inference.ipynb) notebook steps through loading the model and predicting actions from observations on a sample dataset.

### Zero-Shot Inference (Base Model)

The included `demo_data/droid_sample` dataset works with the base model out of the box — no finetuning or checkpoint download needed:

```bash
uv run python scripts/deployment/standalone_inference_script.py \
    --model-path nvidia/GR00T-N1.7-3B \
    --dataset-path demo_data/droid_sample \
    --embodiment-tag OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT \
    --traj-ids 1 2 \
    --inference-mode pytorch \
    --execution-horizon 8
```

This runs open-loop inference on 2 DROID episodes, comparing predicted actions against ground truth. The base model downloads automatically from HuggingFace on first run (~6 GB).

> **Note:** The base model loads the gated `nvidia/Cosmos-Reason2-2B` backbone, so this command requires Hugging Face access (see [Set Up the Environment](#set-up-the-environment)). Without it the run fails with a `GatedRepoError`.

### Finetuned Inference

For posttrain embodiments, use a finetuned checkpoint. Most finetuned checkpoints (e.g., DROID, SimplerEnv) have a flat file structure and can be passed directly as a HuggingFace model ID — no manual download needed:

```bash
uv run python scripts/deployment/standalone_inference_script.py \
    --model-path nvidia/GR00T-N1.7-DROID \
    --dataset-path demo_data/droid_sample \
    --embodiment-tag OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT \
    --traj-ids 1 2 \
    --inference-mode pytorch \
    --execution-horizon 8
```

Some checkpoints (e.g., LIBERO) use a nested folder structure with model files under a subfolder. HuggingFace does not support nested repo paths in `--model-path`, so you must download first:

```bash
uv run hf download nvidia/GR00T-N1.7-LIBERO \
    --include "libero_10/config.json" "libero_10/embodiment_id.json" \
    "libero_10/model-*.safetensors" "libero_10/model.safetensors.index.json" \
    "libero_10/processor_config.json" "libero_10/statistics.json" \
    --local-dir checkpoints/GR00T-N1.7-LIBERO
```

```bash
uv run python scripts/deployment/standalone_inference_script.py \
    --model-path checkpoints/GR00T-N1.7-LIBERO/libero_10 \
    --dataset-path demo_data/libero_demo \
    --embodiment-tag LIBERO_PANDA \
    --traj-ids 0 1 2 \
    --inference-mode pytorch \
    --execution-horizon 8
```

### Server-Client Inference (for Deployment)

For real-world deployment or simulation evaluation, use the server-client architecture. The policy runs on a GPU server; a lightweight client sends observations and receives actions over ZMQ.

**Terminal 1 — Start the policy server:**
```bash
uv run python gr00t/eval/run_gr00t_server.py \
    --model-path nvidia/GR00T-N1.7-3B \
    --embodiment-tag OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT \
    --device cuda:0
```

**Terminal 2 — Run open-loop evaluation as a client:**
```bash
uv run python gr00t/eval/open_loop_eval.py \
    --dataset-path demo_data/droid_sample \
    --embodiment-tag OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT \
    --host 127.0.0.1 \
    --port 5555 \
    --traj-ids 1 2 \
    --execution-horizon 8
```

> **Tip:** If you get `ZMQError: Address already in use`, the default port 5555 is occupied. Use `--port <other_port>`.

For connecting to a real robot (e.g., DROID hardware), see [examples/DROID/README.md](examples/DROID/README.md). For faster inference with TensorRT, see the [Deployment & Inference Guide](scripts/deployment/README.md).

See the complete [Policy API Guide](getting_started/policy.md) for documentation on observation/action formats, batched inference, and troubleshooting.

---

## Fine-tuning

### Reproducing Benchmark Results

Each benchmark has a self-contained README with dataset download, finetune, and evaluation commands:

| Benchmark | Embodiment | Guide |
|-----------|-----------|-------|
| LIBERO | `LIBERO_PANDA` | [examples/LIBERO/README.md](examples/LIBERO/README.md) |
| SimplerEnv (Fractal) | `SIMPLER_ENV_GOOGLE` | [examples/SimplerEnv/README.md](examples/SimplerEnv/README.md) |
| SimplerEnv (Bridge) | `SIMPLER_ENV_WIDOWX` | [examples/SimplerEnv/README.md](examples/SimplerEnv/README.md) |
| SO100 | `NEW_EMBODIMENT` | [examples/SO100/README.md](examples/SO100/README.md) |

### Humanoid Whole-Body Control (SONIC)

GR00T N1.7 supports whole-body humanoid control via the `UNITREE_G1_SONIC` embodiment tag and the [GEAR-SONIC](https://github.com/NVlabs/GR00T-WholeBodyControl) controller. In this workflow, the VLA predicts compact latent action tokens that a learned whole-body controller decodes into full-body joint commands — including legs, arms, and hands. A single policy produces language-conditioned, coordinated manipulation and locomotion end-to-end. SONIC supports whole-body coordination with precise hand and foot placements.

The complete collect → finetune → deploy workflow is documented in the [GR00T-WholeBodyControl repository](https://github.com/NVlabs/GR00T-WholeBodyControl):

- [Data collection](https://nvlabs.github.io/GR00T-WholeBodyControl/tutorials/data_collection.html) — VR teleoperation with SONIC for demonstration recording
- [VLA Workflow](https://nvlabs.github.io/GR00T-WholeBodyControl/tutorials/vla_workflow.html) — finetuning Isaac-GR00T N1.7 on collected data and deploying the policy
- [VLA Inference](https://nvlabs.github.io/GR00T-WholeBodyControl/tutorials/vla_inference.html) — running the PolicyServer + SONIC decoder for real-time control

> **Note:** The `UNITREE_G1` embodiment tag is compatible with the [decoupled WBC](https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/decoupled_wbc) controller, but the end-to-end collect-finetune-deploy workflow is only supported for GEAR-SONIC (`UNITREE_G1_SONIC`).

### Fine-tune on Your Own Robot ("NEW_EMBODIMENT")

To finetune GR00T on your own robot data and configuration, follow the detailed tutorial at [`getting_started/finetune_new_embodiment.md`](getting_started/finetune_new_embodiment.md).

Ensure your input data follows the [GR00T LeRobot format](#data-format), and specify your modality configuration via `--modality-config-path`.

**Single GPU:**
```bash
CUDA_VISIBLE_DEVICES=0 uv run python \
    gr00t/experiment/launch_finetune.py \
    --base-model-path nvidia/GR00T-N1.7-3B \
    --dataset-path demo_data/cube_to_bowl_5 \
    --embodiment-tag NEW_EMBODIMENT \
    --modality-config-path examples/SO100/so100_config.py \
    --num-gpus 1 \
    --output-dir /tmp/test_finetune \
    --max-steps 2000 \
    --global-batch-size 32 \
    --dataloader-num-workers 4
```

**Multi-GPU (e.g., 8xH100):**
```bash
uv run torchrun --nproc_per_node=8 --master_port=29500 \
    gr00t/experiment/launch_finetune.py \
    --base-model-path nvidia/GR00T-N1.7-3B \
    --dataset-path demo_data/cube_to_bowl_5 \
    --embodiment-tag NEW_EMBODIMENT \
    --modality-config-path examples/SO100/so100_config.py \
    --num-gpus 8 \
    --output-dir /tmp/test_finetune_8gpu \
    --max-steps 2000 \
    --global-batch-size 32 \
    --dataloader-num-workers 4
```

Replace `demo_data/cube_to_bowl_5` and `examples/SO100/so100_config.py` with your own dataset and modality config. See [`examples/SO100`](examples/SO100/README.md) for a complete walkthrough.

> **Note:** Use `uv run torchrun` (not bare `torchrun`) to ensure the correct virtual environment is used. Add `--use-wandb` to enable Weights & Biases logging. For more extensive configuration, use `gr00t/experiment/launch_train.py`.

### Training Tips

- Maximize batch size for your hardware and train for a few thousand steps.
- Users may observe 5-6% variance between runs due to non-deterministic image augmentations. Keep this in mind when comparing to reported benchmarks.
- **`--state_dropout_prob`** (model config default: 0.8; finetune CLI default: 0.2; see `gr00t/configs/finetune_config.py`): Randomly drops state inputs during training to improve generalization and reduce state-dependency. The shipped benchmark scripts override the CLI default per suite: LIBERO 10-Long uses 0.2 (the CLI default), SimplerEnv Bridge uses 0.8, SimplerEnv Fractal uses 0.5. If your task relies heavily on proprioceptive state, lower this value.

---

## Evaluation

### Open-Loop Evaluation

Compare predicted actions against ground truth from your dataset:

```bash
uv run python gr00t/eval/open_loop_eval.py \
    --dataset-path <DATASET_PATH> \
    --embodiment-tag NEW_EMBODIMENT \
    --model-path <CHECKPOINT_PATH> \
    --traj-ids 0 \
    --execution-horizon 16
```

This generates a visualization at `/tmp/open_loop_eval/traj_{traj_id}.jpeg` with ground truth vs. predicted actions and MSE metrics. Use `--save-plot-path <dir>` to save plots to a custom location.

### Closed-Loop Evaluation

Test your model in simulation or on real hardware using the server-client architecture:

```bash
# Start the policy server
uv run python gr00t/eval/run_gr00t_server.py \
    --embodiment-tag NEW_EMBODIMENT \
    --model-path <CHECKPOINT_PATH> \
    --device cuda:0 \
    --host 0.0.0.0 --port 5555
```

```python
from gr00t.policy.server_client import PolicyClient

policy = PolicyClient(host="localhost", port=5555)
env = YourEnvironment()
obs, info = env.reset()
action, info = policy.get_action(obs)
obs, reward, done, truncated, info = env.step(action)
```

**Debugging with ReplayPolicy:** To verify your environment setup without a trained model, start the server with `--dataset-path <DATASET_PATH>` (omit `--model-path`) to replay recorded actions from the dataset.

See the complete [Policy API Guide](getting_started/policy.md) for observation/action formats, batched inference, and troubleshooting.

### Benchmark Examples

We support evaluation on public benchmarks using a server-client architecture. The policy server reuses the project root's uv environment; simulation clients have individual setup scripts.

You can use [the verification script](scripts/eval/check_sim_eval_ready.py) to verify that all dependencies are properly configured.

#### One-Time Simulation Environment Setup

Each simulation benchmark needs a one-time environment setup before its first run. First install the shared system libraries:

```bash
sudo apt update
sudo apt install libegl1-mesa-dev libglu1-mesa
```

Then run the

## File tree (depth 3, assets pruned)

```
.coveragerc
.dockerignore
.gitattributes
.github/
  ISSUE_TEMPLATE/
    bug_report.yml
    documentation.yml
    feature_request.yml
  actions/
    setup-venv/
  pull_request_template.md
  workflows/
    main.yml
.gitignore
.gitmodules
.pre-commit-config.yaml
AGENTS.md
ATTRIBUTIONS.md
CLAUDE.md
CONTRIBUTING.md
FAQ.md
LICENSE
README.md
demo_data/
  .gitignore
  cube_to_bowl_5/
    meta/
    videos/
  cube_to_bowl_5_with_mask/
    masks/
    meta/
    videos/
  droid_sample/
    meta/
    videos/
  libero_demo/
    meta/
    videos/
  simplerenv_bridge_sample/
    meta/
    videos/
  simplerenv_fractal_sample/
    meta/
    videos/
docker/
  .dockerignore
  Dockerfile
  README.md
  build.sh
examples/
  DROID/
    README.md
    main_gr00t.py
    server_client.py
    utils.py
  GR00TWholeBodyControl/
    README.md
  LIBERO/
    README.md
    modality.json
    patches/
  RoboLab/
    README.md
  SO100/
    README.md
    modality.json
    so100_config.py
  SimplerEnv/
    README.md
    bridge_modality.json
    convert_av1_to_h264.py
    fractal_modality.json
  finetune.sh
  mask-guided-background-suppression/
    README.md
    so101_config.py
    test_extra_augmentation.py
  rebot-arm-dm/
    README.md
    eval_rebot_arm_dm.py
    modality.json
    pyproject.toml
    rebot_config.py
  robocasa/
    README.md
  robocasa-gr1-tabletop-tasks/
    README.md
external_dependencies/
  LIBERO/
  SimplerEnv/
  robocasa/
  robocasa-gr1-tabletop-tasks/
getting_started/
  GR00T_inference.ipynb
  data_config.md
  data_preparation.md
  finetune_new_embodiment.md
  hardware_recommendation.md
  policy.md
  real_world_deployment.md
gr00t/
  __init__.py
  configs/
    __init__.py
    base_config.py
    deepspeed/
    finetune_config.py
    model/
    training/
  deployment/
    __init__.py
    modes.py
  eval/
    _horizon_contract.py
    open_loop_eval.py
    real_robot/
    rollout_policy.py
    run_gr00t_server.py
    sim/
  experiment/
    __init__.py
    experiment.py
    launch_finetune.py
    launch_train.py
    trainer.py
    utils.py
  model/
    __init__.py
    base/
    gr00t_n1d7/
    modules/
    registry.py
  policy/
    __init__.py
    gr00t_policy.py
    policy.py
    replay_policy.py
    server_client.py
  utils/
    determinism.py
    dist_utils.py
    initial_actions.py
    video_utils.py
pyproject.toml
scripts/
  activate_jetpack72.sh
  activate_orin.sh
  activate_spark.sh
  activate_thor.sh
  deployment/
    GR00T_inference_timing.ipynb
    README.md
    __init__.py
    _trt_contract.py
    benchmark_inference.py
    build_flash_attn.sh
    build_tensorrt_engine.py
    build_trt_pipeline.py
    dgpu/
    export_onnx_n1d7.py
    jetson/
    orin/
    spark/
    standalone_inference_script.py
    thor/
    trt_model_forward.py
    trt_torch.py
    verify_n1d7_trt.py
  download_droid_sample.py
  download_simplerenv_sample.py
  eval/
    check_sim_eval_ready.py
  lerobot_conversion/
    README.md
    convert_v3_to_v2.py
    pyproject.toml
  patch_triton_cuda13.sh
  repair_lerobot_metadata.py
  validate_hf_config_alignment.py
  verify_droid_rotation_correction.py
tests/
  __init__.py
  conftest.py
  examples/
    __init__.py
    test_droid.py
    test_libero.py
    test_robocasa.py
    test_robocasa_gr1_tabletop.py
    test_simplerenv.py
    test_so100.py
  fixtures/
    README.md
    processor_config/
  getting_started/
    test_data_config_md.py
    test_finetune_new_embodiment_md.py
    test_policy_md.py
    test_real_world_deployment_md.py
  gr00t/
    configs/
    eval/
    experiment/
    model/
    policy/
    test_hf_local_first.py
    test_no_weight_load.py
    utils/
  scripts/
    deployment/
    test_repair_lerobot_metadata.py
  test_support/
    __init__.py
    compass.py
    readme.py
    runtime.py
    sync.py
    test_fast_copy_tree.py
  tools/
    test_manifest_alignment.py
tools/
  check_manifest_alignment.py
  manifest_alignment.toml
uv.lock
```

## Config files (2)


### .github/actions/setup-venv/action.yml

```yaml
name: Python virtualenv
description: Set up a Python virtual environment with caching
inputs:
  python-version:
    description: The Python version to use
    required: true
  cache-prefix:
    description: Update this to invalidate the cache
    required: true
    default: v4
runs:
  using: composite
  steps:
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ inputs.python-version }}

    - shell: bash
      run: |
        # Install prerequisites.
        pip install --upgrade pip setuptools wheel virtualenv

    - shell: bash
      run: |
        # Get the exact Python version to use in the cache key.
        echo "PYTHON_VERSION=$(python --version)" >> $GITHUB_ENV

    - uses: actions/cache@v4
      id: virtualenv-cache
      with:
        path: .venv
        key: ${{ inputs.cache-prefix }}-${{ runner.os }}-${{ env.PYTHON_VERSION }}-${{ hashFiles('pyproject.toml') }}

    - if: steps.virtualenv-cache.outputs.cache-hit != 'true'
      shell: bash
      run: |
        # Set up virtual environment without cache hit.
        test -d .venv || virtualenv -p $(which python) --copies --reset-app-data .venv
        . .venv/bin/activate
        pip install ruff

    - if: steps.virtualenv-cache.outputs.cache-hit == 'true'
      shell: bash
      run: |
        # Set up virtual environment from cache hit.
        . .venv/bin/activate

    - shell: bash
      run: |
        # Show environment info.
        . .venv/bin/activate
        echo "✓ Installed $(python --version) virtual environment to $(which python)"
        echo "Packages:"
        pip freeze

```

### .pre-commit-config.yaml

```yaml
exclude: ^(external_dependencies/)
repos:
  # Ruff: lint + autofix
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.7
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  # Catch cross-platform pyproject pin drift (dGPU/Orin/Spark/Thor) at commit
  # time; a missed mirror otherwise only surfaces at install on the unsynced
  # platform. tomli is the 3.10 backport of stdlib tomllib (3.11+).
  - repo: local
    hooks:
      - id: check-manifest-alignment
        name: cross-platform pyproject manifest alignment
        entry: python tools/check_manifest_alignment.py
        language: python
        additional_dependencies: ["tomli; python_version < '3.11'"]
        # Mirrors MANIFESTS in tools/check_manifest_alignment.py; keep in sync when
        # adding a platform. A miss only drops the local trigger — the unit-test
        # live gate reads MANIFESTS directly and still fails CI on drift.
        files: ^(pyproject\.toml|scripts/deployment/(orin|spark|thor)/pyproject\.toml|tools/(check_manifest_alignment\.py|manifest_alignment\.toml))$
        pass_filenames: false

```

## Python signatures and reward/observation bodies (53 files)


### examples/SimplerEnv/convert_av1_to_h264.py

```
def run(cmd)
def is_av1(path)
def convert_file(path)
def find_videos(root)
def main()
```

### gr00t/configs/base_config.py

```
def _build_safe_tree(obj)
def _load_safe_yaml(path)
class Config()
    """Complete configuration."""
    def save(self, path)
    def load(self, path)
    def load_dict(self, data)
    def from_pretrained(cls, path)
    def get_deepspeed_config(self)
    def validate(self)
def get_default_config()
```

### gr00t/configs/finetune_config.py

```
class FinetuneConfig()
    """Configuration for fine-tuning a Vision-Language-Action (VLA) model.

This dataclass defines all parameters needed to launch a fine-tuning job
on a pretrained base model using a custom dataset and embodiment-specific
modality configuration. It controls model tuning options, data augmentation,
and tra"""
    def __post_init__(self)
```

### gr00t/configs/model/__init__.py

```
def register_model_config(shortname, configtype)
def create_model_union_type()
```

### gr00t/configs/model/gr00t_n1d7.py

```
class Gr00tN1d7Config(PretrainedConfig)
    """Unified configuration for Gr00tN1d7 model with backbone and action head.

Gr00tN1d7 uses the Cosmos-Reason2-2B (Qwen3-VL architecture) VLM backbone,
replacing the Eagle backbone used in Gr00tN1d6."""
    def __init__(self)
    def to_filtered_dict(self, exclude_augment)
    def to_filtered_json(self, exclude_augment)
```

### gr00t/configs/training/training_config.py

```
class TrainingConfig()
    """Training configuration."""
    def accumulated_batch_size(self)
    def __post_init__(self)
def check_resume_compatibility(training)
```

### gr00t/eval/rollout_policy.py

```
class VideoConfig()
    """Configuration for video recording settings.

Attributes:
    video_dir: Directory to save videos (if None, no videos are saved)
    steps_per_render: Number of steps between each call to env.render() while recording
        during rollout
    fps: Frames per second for the output video
    codec: Vi"""
class MultiStepConfig()
    """Configuration for multi-step environment settings.

Attributes:
    contract: policy-resolved :class:`PolicyHorizonSpec` carrying
        ``n_action_steps`` and the video / state delta-indices.
    max_episode_steps: Maximum number of steps per episode.
    terminate_on_success: End the episode once"""
class WrapperConfigs()
    """Container for various environment wrapper configurations.

Attributes:
    multistep: Configuration for multi-step processing (required; carries
        the policy-resolved horizon contract).
    video: Configuration for video recording."""
def get_simpler_env_fn(env_name)
def get_libero_env_fn(env_name)
def get_robocasa_env_fn(env_name, robocasa_split)
def get_gym_env(env_name, env_idx, total_n_envs, robocasa_split)
def create_eval_env(env_name, env_idx, total_n_envs, wrapper_configs, robocasa_split)
class _RobustAsyncVectorEnv(AsyncVectorEnv)
    """AsyncVectorEnv that tolerates variable-shaped info arrays across envs.

Gymnasium's default _add_info pre-allocates a numpy array based on the
first env's value shape and then assigns subsequent envs into it.  When
envs return differently-shaped values (e.g. variable-length contact arrays)
the assig"""
    def _add_info(self, infos, info, env_num)
def _macro_step_env_steps(env_infos, env_idx)
def _collect_rollout_episodes(env, policy, n_episodes, n_envs, seed)
def run_rollout_gymnasium_policy(env_name, policy, wrapper_configs, n_episodes, n_envs, seed, robocasa_split)
def create_gr00t_sim_policy(model_path, embodiment_tag, policy_client_host, policy_client_port, trt_engine_path, trt_mode)
def run_gr00t_sim_policy(env_name, n_episodes, max_episode_steps, model_path, policy_client_host, policy_client_port, n_envs, n_action_steps, video_dir, trt_engine_path, trt_mode, seed, robocasa_split)
class RolloutConfig()
    """Configuration for rollout policy evaluation."""
```

### gr00t/eval/sim/LIBERO/libero_env.py

```
"""LIBERO environment

This file wraps the original LIBERO as a Gymnasium environment,
and registers it so that it can be instantiated via gym.make(...) and work
using our distributed evaluation."""
def quat2axisangle(quat)
def normalize_gripper_action(action, binarize)
def invert_gripper_action(action)
class LiberoEnv(Env)
    """LanguageTable env."""
    def __init__(self, task_bddl_file, task_description)
    def close(self)
    def _process_observation(self, obs)
    def reset(self, seed, options)
    def step(self, action)
def register_libero_envs()

```python
def _process_observation(self, obs):
        xyz = obs["robot0_eef_pos"]
        rpy = quat2axisangle(obs["robot0_eef_quat"])
        gripper = obs["robot0_gripper_qpos"]
        new_obs = {
            "video.image": obs["agentview_image"][::-1, ::-1],
            "video.wrist_image": obs["robot0_eye_in_hand_image"][::-1, ::-1],
            "state.x": [xyz[0]],
            "state.y": [xyz[1]],
            "state.z": [xyz[2]],
            "state.roll": [rpy[0]],
            "state.pitch": [rpy[1]],
            "state.yaw": [rpy[2]],
            "state.gripper": gripper,
            "annotation.human.action.task_description": self._task_description,
        }
        return new_obs
```
```

### gr00t/eval/sim/SimplerEnv/simpler_env.py

```
class GoogleFractalEnv(Env)
    def __init__(self, env_name, image_size)
    def reset(self, seed, options)
    def step(self, action)
    def _process_observation(self, obs)
    def _postprocess_gripper(self, current_gripper_action)
class WidowXBridgeEnv(Env)
    def __init__(self, env_name, image_size)
    def reset(self, seed, options)
    def step(self, action)
    def _process_observation(self, obs)
    def _postprocess_gripper(self, action)
def register_simpler_envs()

```python
def _process_observation(self, obs):
        img = get_image_from_maniskill2_obs_dict(self.env, obs)
        proprio = obs["agent"]["eef_pos"]
        qunat_xyzw = np.roll(proprio[3:7], -1)
        gripper_closedness = 1 - proprio[7]
        return {
            "video.image": cv2.resize(img, (self.image_size[1], self.image_size[0])),
            "state.x": [proprio[0]],
            "state.y": [proprio[1]],
            "state.z": [proprio[2]],
            "state.rx": [qunat_xyzw[0]],
            "state.ry": [qunat_xyzw[1]],
            "state.rz": [qunat_xyzw[2]],
            "state.rw": [qunat_xyzw[3]],
            "state.gripper": [gripper_closedness],
            "annotation.human.action.task_description": self.env.unwrapped.get_language_instruction(),
        }
```

```python
def _process_observation(self, obs):
        img = get_image_from_maniskill2_obs_dict(self.env, obs)
        proprio = obs["agent"]["eef_pos"]
        rm_bridge = tq.quat2mat(proprio[3:7])
        rpy_bridge_converted = te.mat2euler(rm_bridge @ self.default_rot.T)
        return {
            "video.image_0": cv2.resize(img, (self.image_size[1], self.image_size[0])),
            "state.x": [proprio[0]],
            "state.y": [proprio[1]],
            "state.z": [proprio[2]],
            "state.roll": [rpy_bridge_converted[0]],
            "state.pitch": [rpy_bridge_converted[1]],
            "state.yaw": [rpy_bridge_converted[2]],
            "state.pad": [0],
            "state.gripper": [proprio[7]],
            "annotation.human.action.task_description": self.env.unwrapped.get_language_instruction(),
        }
```
```

### gr00t/eval/sim/env_utils.py

```
def get_embodiment_tag_from_env_name(env_name)
```

### gr00t/eval/sim/robocasa365/__init__.py

```
"""RoboCasa365 simulation helpers for GR00T evaluation."""
```

### gr00t/eval/sim/robocasa365/gymnasium_groot.py

```
"""GR00T-compatible Gymnasium wrapper for upstream RoboCasa365.

The existing RoboCasa benchmark uses a fork that registers
``robocasa_panda_omron/<Task>_PandaOmron_Env`` and emits the Panda Omron
observation/action keys used by the ROBOCASA_PANDA_OMRON checkpoint. Upstream
RoboCasa365 has a newer task registry and different wrapper keys, so this
module registers a separate namespace while preserving the checkpoint schema."""
def _gather_robot_observations(env)
def _map_obs(input_obs)
def _unmap_action(input_action)
class GrootRoboCasa365Env(Env)
    def __init__(self, env_name, enable_render, split, obj_registries)
    def _process_img(img)
    def _create_spaces(self)
    def _get_basic_observation(self, raw_obs)
    def _get_groot_observation(self, raw_obs)
    def reset(self, seed, options)
    def step(self, action)
    def render(self)
    def close(self)
    def __getattr__(self, name)
def _create_groot_robocasa365_env_class(env_name)

```python
def _gather_robot_observations(env) -> dict[str, np.ndarray]:
    observations = {}

    for robot_id, robot in enumerate(env.robots):
        sim = robot.sim
        gripper_names = {robot.get_gripper_name(arm): robot.gripper[arm] for arm in robot.arms}
        for part_name, indexes in robot._ref_joints_indexes_dict.items():
            qpos_values = []
            for joint_id in indexes:
                qpos_addr = sim.model.jnt_qposadr[joint_id]
                joint_type = sim.model.jnt_type[joint_id]
                if joint_type == mujoco.mjtJoint.mjJNT_FREE:
                    qpos_size = 7
                elif joint_type == mujoco.mjtJoint.mjJNT_BALL:
                    qpos_size = 4
                else:
                    qpos_size = 1
                qpos_values = np.append(
                    qpos_values, sim.data.qpos[qpos_addr : qpos_addr + qpos_size]
                )

            if part_name in gripper_names:
                qpos_values = np.asarray(qpos_values)[::-1]
            if len(qpos_values) > 0:
                observations[f"robot{robot_id}_{part_name}"] = qpos_values

    return observations
```

```python
def _get_basic_observation(self, raw_obs: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
        raw_obs.update(_gather_robot_observations(self.env))
        for obs_name, obs_value in list(raw_obs.items()):
            if obs_name.endswith("_image"):
                raw_obs[obs_name] = np.copy(obs_value[::-1, :, :])
            elif obs_name.endswith("_depth"):
                raw_obs[obs_name] = np.copy(obs_value[::-1, :, :]).astype(np.float32)
            elif isinstance(obs_value, np.ndarray):
                raw_obs[obs_name] = obs_value.astype(np.float32)

        if not self.enable_render:
            for name in self.camera_names:
                raw_obs[f"{name}_image"] = np.zeros(
                    (CAMERA_RESOLUTION, CAMERA_RESOLUTION, 3), dtype=np.uint8
                )

        self.render_cache = raw_obs[self.render_obs_key]
        raw_obs["language"] = self.env.get_ep_meta().get("lang", "")
        return raw_obs
```

```python
def _get_groot_observation(self, raw_obs: dict[str, np.ndarray]) -> dict[str, Any]:
        basic_obs = self._get_basic_observation(raw_obs)
        obs: dict[str, Any] = _map_obs(basic_obs)
        for mapped_name, camera_name in zip(MAPPED_CAMERA_NAMES, CAMERA_NAMES):
            image = self._process_img(basic_obs[f"{camera_name}_image"])
            obs[f"video.{camera_name}"] = image
            obs[mapped_name] = image
            obs[mapped_name.replace("256", "512")] = np.copy(basic_obs[f"{camera_name}_image"])
        obs[LANGUAGE_OBSERVATION_KEY] = basic_obs["language"]
        obs[ROBOCASA_PANDA_LANGUAGE_OBSERVATION_KEY] = basic_obs["language"]
        return obs
```
```

### gr00t/eval/sim/wrapper/multistep_wrapper.py

```
class AggregateMethod(str, Enum)
    """Supported strategies for reducing a sequence of per-step values.

Subclassing ``str`` keeps the members interchangeable with their
string values, so existing callers (and configs) that pass e.g.
``"max"`` keep working while the code itself references the typed
members instead of magic strings."""
def stack_repeated(x, n, loc)
def repeated_box(box_space, n, loc)
def repeated_space(space, n, loc)
def take_last_n(x, n)
def dict_take_last_n(x, n)
def compress_dict_list(ds, recursive)
def aggregate(data, method)
class MultiStepWrapper(Wrapper)
    def __init__(self, env, contract, max_episode_steps, reward_agg_method, terminate_on_success)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def get_max_steps_needed(self)
    def assert_delta_indices(self, delta_indices, horizon)
    def reset(self, seed, options)
    def step(self, action)
    def _get_obs(self, video_delta_indices, state_delta_indices)
    def _add_info(self, info)
    def get_rewards(self)
    def get_attr(self, name)
    def get_infos(self)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        """
        For video, the observation space will be (video_horizon,) + original shape
        For state (if not None), the observation space will be (state_horizon,) + original shape
        """
        new_observation_space = {}
        for k in observation_space.keys():
            if k.startswith("video"):
                box = observation_space[k]
                horizon = video_horizon
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("state"):
                box = observation_space[k]
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("annotation"):
                text = observation_space[k]
                new_observation_space[k] = text
            else:
                warnings.warn(f"Key without a prefix: {k}")
                box = observation_space[k]
                horizon = state_horizon
                new_observation_space[k] = repeated_space(box, horizon)

        return spaces.Dict(new_observation_space)
```

```python
def _get_obs(self, video_delta_indices, state_delta_indices):
        """
        Output:
        For video: (video_horizon,) + obs_shape
        For state (if not None): (state_horizon,) + obs_shape
        """
        assert len(self.obs) > 0
        if isinstance(self.observation_space, spaces.Dict):
            result = dict()
            for key in self.observation_space.keys():
                if key.startswith("video"):
                    """
                    NOTE:
                      We need to subtract 1 because video_delta_indices is 0-indexed.
                      E.g., video_delta_indices = np.array([-4, -3, -2, -1, 0])
                      Then when we select the observation,
                        it should be [obs[-5], obs[-4], obs[-3], obs[-2], obs[-1]]
                      (i.e., the latest observation is at the last index)
                    """
                    delta_indices = video_delta_indices - 1
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("state"):
                    if state_delta_indices is not None:
                        delta_indices = state_delta_indices - 1
                    else:
                        raise ValueError(
                            f"state_delta_indices is None but `state` is still in the {self.observation_space=}"
                        )
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("annotation"):
                    result[key] = self.obs[-1][key]
                else:
                    if state_delta_indices is not None:
                        delta_indices = state_delta_indices - 1
                    else:
                        raise ValueError(
                            f"state_delta_indices is None but `state` is still in the {self.observation_space=}"
                        )
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
            return result
        else:
            raise RuntimeError(f"Unsupported space type: {type(self.observation_space)=}")
```

```python
def get_rewards(self):
        return self.reward
```
```

### gr00t/eval/sim/wrapper/video_recording_wrapper.py

```
class VideoRecordingWrapper(Wrapper)
    def __init__(self, env, mode, video_dir, steps_per_render, max_episode_steps, fps, codec, overlay_text, record_video_keys)
    def close(self)
    def __del__(self)
    def _open_video_writer(self)
    def _write_video_frame(self, frame)
    def _close_video_writer(self)
    def _get_video_frames(self, obs)
    def _resize_frames_to_common_height(self, frames)
    def reset(self)
    def step(self, action)
    def render(self, mode)
```

### gr00t/experiment/trainer.py

```
"""Custom Trainer with simple profiling utilities.

This subclass of HuggingFace's ``Trainer`` measures:
1. Data loading latency (time between the end of the previous ``training_step`` and
   the start of the current ``training_step``).
2. Forward-pass latency (time spent inside the base ``training_step`` implementation,
   which essentially wraps the model's forward / loss computation).

The statistics are logged via ``self.log`` every ``profile_log_interval`` steps and
also sent to the standard ``logging`` logger.  This is *not* meant to be a fully
fledged profiler – it is a quick, lightweight """
class ProfCallback(TrainerCallback)
    def __init__(self, prof)
    def on_step_end(self, args, state, control)
class _BatchIterator()
    """Lightweight iterator that yields pre-collated batches."""
    def __init__(self, buffer, bs, collator, total_steps)
    def __iter__(self)
    def __len__(self)
    def __next__(self)
class _PrefetchIterator()
    def __init__(self, buffer, bs, collate_fn, total_steps)
    def _fill(self)
    def __iter__(self)
    def __len__(self)
    def __next__(self)
def _batch_accuracy(preds, labels, action_offset)
class Gr00tTrainer(Trainer)
    """Trainer that bypasses torch dataloader and makes data collator async."""
    def __init__(self)
    def log(self, logs, start_time)
    def get_train_dataloader(self)
    def train(self, resume_from_checkpoint)
    def compute_loss(self, model, inputs, return_outputs, num_items_in_batch)
```

### gr00t/policy/gr00t_policy.py

```
"""Gr00t Policy implementation for inference.

This module provides the core policy classes for running Gr00t models:
- Gr00tPolicy: Base policy class for model inference
- Gr00tSimPolicyWrapper: Wrapper for compatibility with existing Gr00t simulation environments"""
def _rec_to_dtype(x, dtype)
def _sim_language_batch_to_sequence(value)
class Gr00tPolicy(BasePolicy)
    """Core policy class for Gr00t model inference.

This policy handles the end-to-end inference pipeline:
1. Validates input observations
2. Processes observations with pretrained VLA processor
3. Runs model inference
4. Decodes and returns actions

The policy expects observations with specific modalitie"""
    def __init__(self, embodiment_tag, model_path)
    def _unbatch_observation(self, value)
    def _to_vla_step_data(self, observation)
    def check_observation(self, observation)
    def _get_action(self, observation, options)
    def check_action(self, action)
    def get_modality_config(self)
    def reset(self, options)
class Gr00tSimPolicyWrapper(PolicyWrapper)
    """Wrapper for Gr00tPolicy to enable compatibility with existing Gr00t simulation environments.

This wrapper is specifically designed for retro-fitting the Gr00t policy with the current
Gr00t simulation environment interface. It handles the transformation between the flat
observation format used by Gr"""
    def __init__(self, policy)
    def check_observation(self, observation)
    def _get_action(self, observation, options)
    def check_action(self, action)
    def get_modality_config(self)

```python
def _unbatch_observation(self, value: dict[str, Any]) -> list[dict[str, Any]]:
        """Unbatch a batched observation into a list of single observations.

        Args:
            value: Batched observation with shape (B, ...) for each modality

        Returns:
            List of B observations, each with the batch dimension removed
        """
        unbatched_obs = []
        # Infer batch size from the first video key
        batch_size = value["video"][list(value["video"].keys())[0]].shape[0]

        # Split each modality along the batch dimension
        for i in range(batch_size):
            unbatched_value = {
                "video": {k: v[i] for k, v in value["video"].items()},
                "state": {k: v[i] for k, v in value["state"].items()},
                "language": {k: v[i] for k, v in value["language"].items()},
            }
            unbatched_obs.append(unbatched_value)
        return unbatched_obs
```

```python
def check_observation(self, observation: dict[str, Any]) -> None:
        """Validate that the observation has the correct structure and types.

        This method ensures that all required modalities are present and that their
        data types, shapes, and dimensions match the model's expectations.

        Expected observation structure:
            - video: dict[str, np.ndarray[np.uint8, (B, T, H, W, C)]]
                - B: batch size
                - T: temporal horizon (number of frames)
                - H, W: image height and width
                - C: number of channels (must be 3 for RGB)
            - state: dict[str, np.ndarray[np.float32, (B, T, D)]]
                - B: batch size
                - T: temporal horizon (number of state observations)
                - D: state dimension
            - language: dict[str, list[list[str]]]
                - Shape: (B, T) where each element is a string
                - T: temporal horizon (typically 1 for language)

        Args:
            observation: Dictionary containing video, state, and language modalities

        Raises:
            AssertionError: If any validation check fails
        """
        # Check that observation contains all required top-level modality keys
        for modality in ["video", "state", "language"]:
            assert modality in observation, f"Observation must contain a '{modality}' key"
            assert isinstance(observation[modality], dict), (
                f"Observation '{modality}' must be a dictionary. Got {type(observation[modality])}: {observation[modality]}"
            )

        # Track batch size across modalities to ensure consistency
        bs = -1

        # ===== VIDEO VALIDATION =====
        # Validate each video stream defined in the modality config
        for video_key in self.modality_configs["video"].modality_keys:
            assert video_key in observation["video"], (
                f"Video key '{video_key}' must be in observation"
            )

            # Set or verify batch size consistency across all video keys
            if bs == -1:
                bs = len(observation["video"][video_key])
            else:
                assert len(observation["video"][video_key]) == bs, (
                    f"Video key '{video_key}' must have batch size {bs}. Got {len(observation['video'][video_key])}"
                )

            batched_video = observation["video"][video_key]

            # Verify data type is numpy array
            assert isinstance(batched_video, np.ndarray), (
                f"Video key '{video_key}' must be a numpy array. Got {type(batched_video)}"
            )

            # Verify dtype is uint8 (standard for image data, range 0-255)
            assert batched_video.dtype == np.uint8, (
                f"Video key '{video_key}' must be a numpy array of type np.uint8. Got {batched_video.dtype}"
            )

            # Verify shape has 5 dimensions: (B, T, H, W, C)
            assert batched_video.ndim == 5, (
                f"Video key '{video_key}' must be a numpy array of shape (B, T, H, W, C), got {batched_video.shape}"
            )

            # Verify temporal dimension matches the expected horizon from config
            assert batched_video.shape[1] == len(self.modality_configs["video"].delta_indices), (
                f"Video key '{video_key}'s horizon must be {len(self.modality_configs['video'].delta_indices)}. Got {batched_video.shape[1]}"
            )

            # Verify channel dimension is 3 (RGB images)
            assert batched_video.shape[-1] == 3, (
                f"Video key '{video_key}'s channel 'C' must be 3. Got {batched_video.shape[-1]}"
            )

        # ===== STATE VALIDATION =====
        # Validate each state stream defined in the modality config
        for state_key in self.modality_configs["state"].modality_keys:
            # Check that the expected state key exists in the observation
            # (must happen before index
```

```python
def check_observation(self, observation: dict[str, Any]) -> None:
        """Validate observation from Gr00t sim environment format.

        This validation is specific to the flat observation format used by Gr00t sim environments.
        Unlike Gr00tPolicy.check_observation which expects nested dicts, this expects flat keys.

        Expected observation structure (Gr00t sim format):
            - Flat keys like 'video.camera_name': np.ndarray[np.uint8, (B, T, H, W, C)]
            - Flat keys like 'state.state_name': np.ndarray[np.float32, (B, T, D)]
            - Language keys: tuple[str] or list[str] with shape (B,)
                - Key can be 'task' or 'annotation.human.coarse_action' (for DC envs)

        Args:
            observation: Flat observation dictionary from Gr00t sim environment

        Raises:
            AssertionError: If any validation check fails
        """
        modality_configs = self.get_modality_config()

        # ===== VIDEO VALIDATION =====
        # Check video modalities with flat key format: 'video.camera_name'
        for video_key in modality_configs["video"].modality_keys:
            # Construct flat key expected in Gr00t sim environment
            parsed_key = f"video.{video_key}"
            assert parsed_key in observation, f"Video key '{parsed_key}' must be in observation"

            batched_video = observation[parsed_key]

            # Verify data type is numpy array
            assert isinstance(batched_video, np.ndarray), (
                f"Video key '{video_key}' must be a numpy array. Got {type(batched_video)}"
            )

            # Verify dtype is uint8 (standard for image data, range 0-255)
            assert batched_video.dtype == np.uint8, (
                f"Video key '{video_key}' must be a numpy array of type np.uint8. Got {batched_video.dtype}"
            )

            # Verify shape has 5 dimensions: (B, T, H, W, C)
            assert batched_video.ndim == 5, (
                f"Video key '{video_key}' must be a numpy array of shape (B, T, H, W, C), got {batched_video.shape}"
            )

            # Verify temporal dimension matches the expected horizon from config
            assert batched_video.shape[1] == len(modality_configs["video"].delta_indices), (
                f"Video key '{video_key}'s horizon must be {len(modality_configs['video'].delta_indices)}. Got {batched_video.shape[1]}"
            )

            # Verify channel dimension is 3 (RGB images)
            assert batched_video.shape[-1] == 3, (
                f"Video key '{video_key}'s channel 'C' must be 3. Got {batched_video.shape[-1]}"
            )

        # ===== STATE VALIDATION =====
        # Check state modalities with flat key format: 'state.state_name'
        for state_key in modality_configs["state"].modality_keys:
            # Construct flat key expected in Gr00t sim environment
            parsed_key = f"state.{state_key}"
            assert parsed_key in observation, f"State key '{parsed_key}' must be in observation"

            batched_state = observation[parsed_key]

            # Verify data type is numpy array
            assert isinstance(batched_state, np.ndarray), (
                f"State key '{state_key}' must be a numpy array. Got {type(batched_state)}"
            )

            # Verify dtype is float32 (standard for continuous state values)
            assert batched_state.dtype == np.float32, (
                f"State key '{state_key}' must be a numpy array of type np.float32. Got {batched_state.dtype}"
            )

            # Verify shape has 3 dimensions: (B, T, D)
            assert batched_state.ndim == 3, (
                f"State key '{state_key}' must be a numpy array of shape (B, T, D), got {batched_state.shape}"
            )

            # Verify temporal dimension matches the expected horizon from config
            assert batched_state.shape[1] == len(modality_configs["state"].delta_indices), (
                f"State key '{state_
```
```

### gr00t/policy/policy.py

```
class BasePolicy(ABC)
    """Abstract base class for robotic control policies.

This class defines the interface that all policies must implement, including
methods for action computation, input/output validation, and state management.

Subclasses must implement:
    - check_observation(): Validate observation format
    - chec"""
    def __init__(self)
    def check_observation(self, observation)
    def check_action(self, action)
    def _get_action(self, observation, options)
    def get_action(self, observation, options)
    def reset(self, options)
class PolicyWrapper(BasePolicy)
    """Base wrapper class for composing policy behaviors.

Note: This base implementation only forwards reset(). Subclasses should
implement validation logic and additional functionality as needed."""
    def __init__(self, policy)
    def reset(self, options)

```python
def check_observation(self, observation: dict[str, Any]) -> None:
        """Check if the observation is valid.

        Args:
            observation: Dictionary containing the current state/observation of the environment

        Raises:
            AssertionError: If the observation is invalid.
        """
        pass
```
```

### gr00t/policy/replay_policy.py

```
"""Replay Policy implementation for replaying actions from a dataset.

This module provides a policy that replays recorded actions from a LeRobot-style dataset,
with observation validation matching the Gr00tPolicy interface."""
class ReplayPolicy(BasePolicy)
    """Policy that replays recorded actions from a LeRobot-style dataset.

This policy loads actions from a dataset and replays them in sequence. It validates
that incoming observations match the expected format (compatible with Gr00tPolicy).

The policy expects observations with specific modalities (video"""
    def __init__(self, dataset_path, modality_configs, execution_horizon)
    def _preload_actions(self)
    def check_observation(self, observation)
    def check_action(self, action)
    def _get_action(self, observation, options)
    def reset(self, options)
    def get_modality_config(self)
    def num_episodes(self)

```python
def check_observation(self, observation: dict[str, Any]) -> None:
        """Validate that the observation has the correct structure and types.

        This method ensures that all required modalities are present and that their
        data types, shapes, and dimensions match the expected format (same as Gr00tPolicy).

        Expected observation structure:
            - video: dict[str, np.ndarray[np.uint8, (B, T, H, W, C)]]
                - B: batch size
                - T: temporal horizon (number of frames)
                - H, W: image height and width
                - C: number of channels (must be 3 for RGB)
            - state: dict[str, np.ndarray[np.float32, (B, T, D)]]
                - B: batch size
                - T: temporal horizon (number of state observations)
                - D: state dimension
            - language: dict[str, list[list[str]]]
                - Shape: (B, T) where each element is a string
                - T: temporal horizon (typically 1 for language)

        Args:
            observation: Dictionary containing video, state, and language modalities

        Raises:
            AssertionError: If any validation check fails
        """
        # Check that observation contains all required top-level modality keys
        for modality in ["video", "state", "language"]:
            assert modality in observation, f"Observation must contain a '{modality}' key"
            assert isinstance(observation[modality], dict), (
                f"Observation '{modality}' must be a dictionary. Got {type(observation[modality])}"
            )

        # Track batch size across modalities to ensure consistency
        bs = -1

        # ===== VIDEO VALIDATION =====
        for video_key in self.modality_configs["video"].modality_keys:
            assert video_key in observation["video"], (
                f"Video key '{video_key}' must be in observation"
            )

            if bs == -1:
                bs = len(observation["video"][video_key])
            else:
                assert len(observation["video"][video_key]) == bs, (
                    f"Video key '{video_key}' must have batch size {bs}. Got {len(observation['video'][video_key])}"
                )

            batched_video = observation["video"][video_key]

            assert isinstance(batched_video, np.ndarray), (
                f"Video key '{video_key}' must be a numpy array. Got {type(batched_video)}"
            )

            assert batched_video.dtype == np.uint8, (
                f"Video key '{video_key}' must be a numpy array of type np.uint8. Got {batched_video.dtype}"
            )

            assert batched_video.ndim == 5, (
                f"Video key '{video_key}' must be a numpy array of shape (B, T, H, W, C), got {batched_video.shape}"
            )

            assert batched_video.shape[1] == len(self.modality_configs["video"].delta_indices), (
                f"Video key '{video_key}'s horizon must be {len(self.modality_configs['video'].delta_indices)}. Got {batched_video.shape[1]}"
            )

            assert batched_video.shape[-1] == 3, (
                f"Video key '{video_key}'s channel 'C' must be 3. Got {batched_video.shape[-1]}"
            )

        # ===== STATE VALIDATION =====
        for state_key in self.modality_configs["state"].modality_keys:
            # Existence check must precede indexing — see video validation above.
            assert state_key in observation["state"], (
                f"State key '{state_key}' must be in observation"
            )

            if bs == -1:
                bs = len(observation["state"][state_key])
            else:
                assert len(observation["state"][state_key]) == bs, (
                    f"State key '{state_key}' must have batch size {bs}. Got {len(observation['state'][state_key])}"
                )

            batched_state = observation["state"][state_key]

            assert isinstance(batched_state, np.ndarray), (
    
```
```

### gr00t/policy/server_client.py

```
class MsgSerializer()
    """msgpack_numpy serializer with a hard ``allow_pickle=False`` boundary.

Implementation note: msgpack_numpy's ``Packer``/``Unpacker`` wire any
user-provided ``default``/``object_hook`` *behind* their own
``mnp.encode``/``mnp.decode`` (``functools.partial(encode, chain=user_fn)``).
That means an object"""
    def to_bytes(data)
    def from_bytes(data)
    def _safe_encode(obj, chain)
    def _safe_decode(obj, chain)
    def _encode_custom(obj)
    def _decode_custom(obj)
class EndpointHandler()
class PolicyServer()
    """An inference server that spin up a ZeroMQ socket and listen for incoming requests.
Can add custom endpoints by calling `register_endpoint`."""
    def __init__(self, policy, host, port, api_token)
    def _kill_server(self)
    def close(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc, tb)
    def _handle_ping(self)
    def register_endpoint(self, name, handler, requires_input)
    def _validate_token(self, request)
    def run(self)
    def start_server(policy, port, host, api_token)
class PolicyClient(BasePolicy)
    def __init__(self, host, port, timeout_ms, api_token, strict)
    def _init_socket(self)
    def ping(self)
    def kill_server(self)
    def call_endpoint(self, endpoint, data, requires_input)
    def close(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc, tb)
    def __del__(self)
    def _get_action(self, observation, options)
    def reset(self, options)
    def get_modality_config(self)
    def check_observation(self, observation)
    def check_action(self, action)

```python
def check_observation(self, observation: dict[str, Any]) -> None:
        raise NotImplementedError(
            "check_observation is not implemented. Please use `strict=False` to disable strict mode or implement this method in the subclass."
        )
```
```

### gr00t/utils/initial_actions.py

```
"""Safe (pickle-free) save/load for the per-dataset initial-actions cache.

Why this isn't just ``np.savez(path, the_nested_list)``:
    The cache is a nested ``list[dict[trajectory, dict[action_key, ndarray]]]``.
    numpy can only store plain arrays, so handing it the nested object forces
    it to *pickle* the whole structure — and reading a pickle runs whatever
    code the file tells it to. An ``initial_actions.npz`` can come from an
    untrusted place (a HuggingFace dataset bundle, shared NFS), so that load
    would be an arbitrary-code-execution hole.

How we avoid pickle:
    We flatten"""
def _encode_key(dataset_idx, trajectory, action_key)
def _decode_key(key)
def save_initial_actions(initial_actions, initial_actions_path)
def load_initial_actions(initial_actions_path)
```

### scripts/download_simplerenv_sample.py

```
"""Download small SimplerEnv sample datasets from HuggingFace for inference testing.

Creates two demo datasets under demo_data/:
  - simplerenv_fractal_sample  (3 episodes from IPEC-COMMUNITY/fractal20220817_data_lerobot)
  - simplerenv_bridge_sample   (3 episodes from IPEC-COMMUNITY/bridge_orig_lerobot)

Both source datasets are already in LeRobot v2 format (per-episode parquet + per-episode mp4),
so this script simply downloads the first few episodes and rewrites the meta files.

Prerequisites:
    pip install huggingface_hub jsonlines pyarrow

Usage:
    python scripts/download_simplerenv_sam"""
def download_sample(dataset_key, num_episodes, repo_root)
def _assemble_sample(cache_dir, output_dir, num_episodes, cfg, repo_root)
def main()
```

### scripts/eval/check_sim_eval_ready.py

```
def check_uv_installation()
def _test_nvidia_driver_installation()
def _test_egl()
def check_vulkan_installation()
def check_egl_installation()
def check_simpler_env_environments()
def check_libero_environments()
```

### scripts/validate_hf_config_alignment.py

```
"""Validate HuggingFace config alignment against source-of-truth definitions.

Usage:
    # Internal consistency checks only (no HF download required):
    uv run python scripts/validate_hf_config_alignment.py

    # Full check with HF configs (requires auth + local dirs):
    uv run python scripts/validate_hf_config_alignment.py --hf-config-dir /tmp/hf_configs"""
def check(condition, msg)
def info(msg)
def load_modality_configs()
def load_model_config_defaults()
def load_embodiment_tags()
def load_projector_index()
def load_processor_default_max_action_horizon()
def check_dim_f_internal_consistency()
def check_dim_e_documentation()
def check_dim_f2_modality_json()
def check_dim_j_enum_serialization()
def load_hf_json(base_dir, model_name, filename, subdir)
def check_dim_a_processor_config(hf_dir, model_name, model_def)
def check_dim_b_config_json(hf_dir, model_name, model_def)
def check_dim_c_embodiment_id(hf_dir, model_name, model_def)
def check_dim_d_statistics(hf_dir, model_name, model_def)
def check_dim_f1_cross_file(hf_dir, model_name, model_def)
def check_test_fixture()
def main()
```

### tests/examples/test_simplerenv.py

```
def _run_simplerenv_eval(env, blocks, server_model_key, client_env_name_old, client_env_name_new, server_startup_env_var)
def test_simplerenv_fractal_readme_eval_flow()
def test_simplerenv_bridge_readme_eval_flow()
```

### tests/getting_started/test_data_config_md.py

```
def test_complete_so100_config()
```

### tests/getting_started/test_policy_md.py

```
class TinyGr00tConfig(PretrainedConfig)
    def __init__(self, action_horizon, max_action_dim)
class TinyGr00tModel(PreTrainedModel)
    """Minimal stand-in for Gr00tN1d6: accepts any kwargs, returns zero action_pred."""
    def __init__(self, config)
    def get_action(self)
def tiny_checkpoint(tmp_path_factory)
def _make_policy_md_modality_configs()
class MockProcessor()
    def eval(self)
    def get_modality_configs(self)
    def __call__(self, messages)
    def collator(self)
    def decode_action(self, action_array, embodiment_tag, batched_states)
def mock_processor()
def test_automodel_loads_tiny_checkpoint(tiny_checkpoint)
def test_get_action_returns_correct_shape(tiny_checkpoint)
def test_get_action_respects_batch_size(tiny_checkpoint)
def test_policy_md_steps(monkeypatch, tiny_checkpoint, mock_processor)
```

### tests/gr00t/configs/test_base_config_safe_yaml.py

```
"""CPU-only regression tests for the safe-YAML contract on
:class:`gr00t.configs.base_config.Config`: the save side must emit
plain-dict YAML (no ``!!python/`` tags) and the load sides
(``Config.load`` / ``Config.from_pretrained``) must refuse to
instantiate any Python object from a maliciously crafted config."""
def _import_config()
def test_save_does_not_emit_python_object_tags(tmp_path)
def test_load_rejects_malicious_python_object_tag(tmp_path, monkeypatch)
def test_from_pretrained_rejects_malicious_python_object_tag(tmp_path)
def test_load_rejects_non_mapping_top_level(tmp_path)
def test_safe_dump_yaml_can_be_loaded_back(tmp_path)
def test_save_serialises_enum_action_configs(tmp_path)
def test_save_creates_parent_directory(tmp_path)
def _no_stray_canary(tmp_path)
```

### tests/gr00t/configs/test_batch_size_invariant.py

```
"""``accumulated_batch_size`` must equal what HuggingFace ``Trainer`` consumes
per optimizer step (``per_device × num_gpus × gradient_accumulation_steps``)."""
def test_training_config_accumulated_mirrors_hf(kwargs, per_device, num_gpus, grad_accum)
```

### tests/gr00t/eval/sim/test_env_utils.py

```
"""Regression tests for env_name → EmbodimentTag mapping.

Covers all 10 supported sim benchmarks, including fixes for:
- GitHub Issue #479: LIBERO, SimplerEnv Google, SimplerEnv WidowX"""
class TestEnvPrefixMapping()
    """Verify ENV_PREFIX_TO_EMBODIMENT_TAG covers all known benchmarks."""
    def test_all_known_prefixes_present(self)
    def test_related_prefixes_map_to_same_tag(self)
class TestGetEmbodimentTagFromEnvName()
    """Test get_embodiment_tag_from_env_name() for all supported benchmarks."""
    def test_locomanip_g1(self, env_name)
    def test_simpler_env_google(self)
    def test_simpler_env_widowx(self)
    def test_libero_panda(self)
    def test_gr1_unified_maps_to_robocasa_gr1_tabletop(self)
    def test_robocasa_panda_omron_maps_to_dedicated_tag(self)
    def test_robocasa365_panda_omron_maps_to_dedicated_tag(self)
    def test_unknown_env_raises_value_error(self)
    def test_empty_string_raises_value_error(self)
    def test_multi_slash_uses_first_segment(self)
class TestRegisteredPrefixClosure()
    """Author-vs-truth closure check for the env-prefix -> EmbodimentTag mapping.

Binds the mapping to the *real* gym registration sites (the ground truth)
instead of a hand-written prefix list: it scans ``gr00t/eval/sim/**/*.py``
for ``register(id="<prefix>/...")`` call sites and asserts that every
stati"""
    def _prefix_from_node(cls, node)
    def _registered_prefixes(self)
    def test_every_registered_prefix_resolves(self)
```

### tests/gr00t/eval/sim/test_robocasa365_gymnasium_groot.py

```
def _install_robocasa365_import_stubs(monkeypatch)
def test_robocasa365_observation_keys_match_embodiment_config(monkeypatch)

```python
def test_robocasa365_observation_keys_match_embodiment_config(monkeypatch):
    _install_robocasa365_import_stubs(monkeypatch)
    module = importlib.import_module("gr00t.eval.sim.robocasa365.gymnasium_groot")

    env = module.GrootRoboCasa365Env.__new__(module.GrootRoboCasa365Env)
    env.env = types.SimpleNamespace(robots=[], get_ep_meta=lambda: {"lang": "open the fridge"})
    env.enable_render = True
    env.camera_names = module.CAMERA_NAMES
    env.render_obs_key = "robot0_agentview_left_image"
    env.render_cache = None

    raw_obs = {
        "robot0_gripper_qpos": np.zeros(1, dtype=np.float32),
        "robot0_base_pos": np.zeros(3, dtype=np.float32),
        "robot0_base_quat": np.zeros(4, dtype=np.float32),
        "robot0_base_to_eef_pos": np.zeros(3, dtype=np.float32),
        "robot0_base_to_eef_quat": np.zeros(4, dtype=np.float32),
        "robot0_gripper_qvel": np.zeros(1, dtype=np.float32),
        "robot0_eef_pos": np.zeros(3, dtype=np.float32),
        "robot0_eef_quat": np.zeros(4, dtype=np.float32),
        "robot0_joint_pos": np.zeros(7, dtype=np.float32),
        "robot0_joint_pos_cos": np.zeros(7, dtype=np.float32),
        "robot0_joint_pos_sin": np.zeros(7, dtype=np.float32),
        "robot0_joint_vel": np.zeros(7, dtype=np.float32),
        "robot0_agentview_left_image": np.zeros((256, 256, 3), dtype=np.uint8),
        "robot0_agentview_right_image": np.zeros((256, 256, 3), dtype=np.uint8),
        "robot0_eye_in_hand_image": np.zeros((256, 256, 3), dtype=np.uint8),
    }

    obs = env._get_groot_observation(raw_obs)

    assert set(module.VIDEO_OBSERVATION_KEYS).issubset(obs)
    assert set(module.ROBOCASA_PANDA_VIDEO_OBSERVATION_KEYS).issubset(obs)
    assert obs["video.robot0_agentview_left"].shape == (256, 256, 3)
    assert obs["video.res256_image_side_0"].shape == (256, 256, 3)
    assert obs["annotation.human.task_description"] == "open the fridge"
    assert obs["annotation.human.action.task_description"] == "open the fridge"
```
```

### tests/gr00t/eval/sim/test_simpler_env_success.py

```
"""SimplerEnv success signal must come from the task predicate, not termination.

The step wrappers previously set ``info["success"] = done``. Under
``terminate_on_success`` the multistep wrapper both terminates on and counts
``info["success"]``, so conflating it with the raw termination flag miscounts
episodes (a timeout/other termination reads as a success, and a success that has
not yet terminated reads as a failure). These CPU-only tests drive ``step`` with a
fake inner env and assert the two signals are decoupled. Heavy sim deps are stubbed
so the test runs without cv2 / simpler_env / transf"""
def _install_simpler_env_import_stubs(monkeypatch)
class _FakeInner()
    """Minimal inner env returning a controlled (done, info["success"]) pair."""
    def __init__(self, done, success)
    def step(self, action_vector)
def _make_env(cls, inner)
def _action()
def test_step_success_from_predicate_not_termination(monkeypatch, env_cls_name, done, success)
def test_step_success_defaults_false_when_predicate_absent(monkeypatch, env_cls_name)
```

### tests/gr00t/eval/sim/test_video_recording_wrapper.py

```
def _frame(value)
class DummyEnv(Env)
    def reset(self)
    def step(self, action)
def _make_wrapper(record_video_keys)
def test_video_recording_wrapper_uses_explicit_video_keys_in_order()
def test_video_recording_wrapper_falls_back_to_all_video_keys()
def test_video_recording_wrapper_reports_missing_explicit_video_keys()
def test_video_recording_wrapper_configures_ffmpeg_h264_quality_options(monkeypatch, tmp_path)
def test_video_recording_wrapper_writes_mp4_with_ffmpeg(tmp_path)
```

### tests/gr00t/eval/sim/wrapper/test_multistep_aggregate.py

```
"""Pin :class:`AggregateMethod` and the
``MultiStepWrapper(reward_agg_method=...)`` constructor's fail-fast
validation: every allowed method round-trips, and any unknown method
raises ``ValueError`` at the constructor boundary (not deep inside the
first ``step()``) with both the bad input and the allowed set named."""
def _import_module()
def test_aggregate_method_enum_members_match_supported_values()
def test_aggregate_returns_expected_value_for_each_allowed_method(method, data, expected)
def test_aggregate_raises_value_error_with_helpful_message_on_unknown_method()
def _build_dummy_env_kwargs(mod)
def test_multistep_wrapper_init_rejects_unknown_reward_agg_method()
def test_multistep_wrapper_init_accepts_each_allowed_method(method)
def test_step_reports_inner_env_step_count(done_after, expected)

```python
def test_multistep_wrapper_init_rejects_unknown_reward_agg_method():
    """Bad ``reward_agg_method`` raises at construction time, not on
    the first ``step()``, and the error names the allowed set."""
    mod = _import_module()
    try:
        kwargs = _build_dummy_env_kwargs(mod)
    except (ImportError, OSError) as e:
        pytest.skip(f"gymnasium not importable: {e}")

    with pytest.raises(ValueError) as excinfo:
        mod.MultiStepWrapper(reward_agg_method="median", **kwargs)
    msg = str(excinfo.value)
    assert "median" in msg
    assert "max" in msg, "error message must enumerate the allowed set"
```
```

### tests/gr00t/eval/sim/wrapper/test_video_recorder_cleanup.py

```
"""Pin the ffmpeg recorder lifecycle: ``close()`` reaps the encoder child
and the inner env, a wedged encoder is killed within the grace window
(never blocks the caller forever), and a non-zero exit still surfaces.

These tests drive a *real* child ``subprocess`` (a tiny ``python -c`` stand-in
for ffmpeg) rather than a stub, so they exercise the actual
``Popen.communicate()`` semantics — in particular that the cleanup path must
not close stdin before ``communicate()`` flushes it (a stub that never touches
stdin would hide that bug)."""
def _import_module()
def _make_wrapper(mod, cmd)
def test_close_reaps_recorder_and_inner_env()
def test_close_surfaces_nonzero_ffmpeg_exit()
def test_close_kills_wedged_recorder_within_grace(monkeypatch)
```

### tests/gr00t/eval/test_robocasa365_rollout_policy.py

```
def test_robocasa365_env_fn_passes_split_to_gym_make(monkeypatch)
def test_robocasa365_record_video_keys_match_observation_keys()

```python
def test_robocasa365_record_video_keys_match_observation_keys():
    assert rollout_policy.ROBOCASA365_PANDA_RECORD_VIDEO_KEYS == (
        "video.robot0_agentview_left",
        "video.robot0_agentview_right",
        "video.robot0_eye_in_hand",
    )
```
```

### tests/gr00t/eval/test_so100_action_steps.py

```
"""SO100 real-robot eval must not silently execute fewer action steps than the
configured ``action_horizon``. ``_select_action_steps`` returns the requested
window when the policy supplies enough steps and raises otherwise."""
def _chunk(n)
def test_returns_requested_window_when_chunk_is_long_enough()
def test_returns_full_chunk_when_horizon_equals_length()
def test_raises_when_horizon_exceeds_chunk()
```

### tests/gr00t/experiment/test_trainer_resume_strictness.py

```
"""CPU regression test pinning ``Gr00tTrainer.train()`` resume-error semantics.

Before this MR, ``Gr00tTrainer.train()`` swallowed HF's ``ValueError("No valid
checkpoint found ...")`` and downgraded it to a single ``logging.warning``,
silently falling back to fresh training. That silencer is what hid the
``resume_from_checkpoint=True`` hardcoding (see the silent-corruption fix in
this same MR) for ~6 months: fresh runs printed one easy-to-miss WARNING and
otherwise looked normal.

This test ensures the strict-raise behavior never regresses: an explicit
``resume_from_checkpoint=True`` against a d"""
class _TinyModel(Module)
    def __init__(self)
    def forward(self, x, labels)
class _TinyDataset(Dataset)
    def __init__(self, n)
    def __len__(self)
    def __getitem__(self, i)
def _collate(batch)
def _make_trainer(output_dir)
def test_raises_when_resume_true_but_no_checkpoint(tmp_path)
def test_raises_when_resume_true_and_only_non_checkpoint_subdirs(tmp_path)
```

### tests/gr00t/experiment/test_warn_configs.py

```
"""CPU-only guards for the training-config invariants in ``experiment``:

* ``num_gpus`` must equal the launcher ``WORLD_SIZE`` (otherwise per-device
  batch math and the real data-parallel size disagree).
* ``warmup_steps`` is actually forwarded to HF ``TrainingArguments`` so its
  documented "overrides warmup_ratio" contract holds."""
def test_num_gpus_must_match_world_size(monkeypatch, world_size_env, num_gpus, expect_error)
def _training_arguments_keywords()
def test_warmup_steps_is_forwarded_to_training_arguments()
```

### tests/gr00t/model/test_action_head.py

```
"""Test Gr00tN1d7ActionHead: flow matching forward, get_action, feature encoding.

These tests instantiate the action head directly (no backbone required)
and feed it synthetic backbone output tensors."""
def _small_config()
def action_head()
def _make_backbone_output(config, batch_size, seq_len)
def _make_action_input(config, batch_size)
class TestActionHeadForward()
    """Test training forward pass."""
    def test_forward_returns_loss(self, action_head)
    def test_forward_loss_shape(self, action_head)
    def test_forward_with_state_dropout(self)
class TestActionHeadGetAction()
    """Test inference (denoising loop)."""
    def test_get_action_output_shape(self, action_head)
    def test_get_action_no_grad(self, action_head)
    def test_get_action_single_sample(self, action_head)
class TestActionHeadEncodeFeatures()
    """Test feature encoding helper."""
    def test_encode_features_shapes(self, action_head)
def _beta_time_moments(alpha, beta, noise_s)
class TestActionHeadTimeSamplingMetaSafe()
    """Oracle tests for sample_time under meta / no_init_weights construction.

Regression guard: when the action head is built while the default device is
meta (as happens inside a nested from_pretrained), sample_time must still
produce a valid, correctly-distributed noise schedule on the requested
device"""
    def test_sample_time_under_meta_construction(self, alpha, beta, noise_s)
    def test_sample_time_construction_device_invariant(self)
class TestActionHeadTrainableParams()
    """Test parameter freezing."""
    def test_all_trainable_by_default(self, action_head)
    def test_freeze_projector(self)
    def test_freeze_diffusion(self)
```

### tests/gr00t/model/test_action_horizon_validation.py

```
"""``validate_action_horizons`` must reject an embodiment whose action horizon
exceeds the model's ``max_action_horizon`` at processor construction, rather than
letting it surface deep in the first forward."""
def _action(horizon)
def test_passes_when_all_horizons_fit()
def test_raises_when_horizon_exceeds_max()
def test_reports_the_largest_required_horizon()
def test_ignores_embodiments_without_an_action_config()
```

### tests/gr00t/policy/conftest.py

```
"""Local pytest hooks for GPU policy tests."""
def pytest_collection_modifyitems(config, items)
```

### tests/gr00t/policy/test_gr00t_policy.py

```
"""Test Gr00tPolicy: observation validation and inference pipeline.

Uses mocked model and processor to avoid downloading checkpoints."""
def _build_modality_configs()
def policy()
def _make_observation(batch_size)
class TestGr00tPolicyInit()
    def test_policy_has_model_and_processor(self, policy)
    def test_policy_embodiment_tag(self, policy)
class TestGr00tPolicyCheckObservation()
    def test_valid_observation_passes(self, policy)
    def test_missing_video_key_raises(self, policy)
    def test_wrong_video_dtype_raises(self, policy)
class TestGr00tPolicyGetAction()
    def test_get_action_returns_tuple(self, policy)
    def test_get_action_returns_dict(self, policy)
class _NumpyLanguageSimPolicy()
    def __init__(self)
    def get_modality_config(self)
    def get_action(self, observation, options)
    def reset(self, options)
def test_sim_policy_wrapper_accepts_numpy_language_batches()

```python
def _make_observation(batch_size=1):
    return {
        "video": {
            k: np.random.randint(0, 255, (batch_size, 1, 256, 256, 3), dtype=np.uint8)
            for k in VIDEO_KEYS
        },
        "state": {
            k: np.random.randn(batch_size, 1, 1).astype(np.float32)
            for k in STATE_KEYS[:-1]  # all except gripper
        }
        | {"gripper": np.random.randn(batch_size, 1, 2).astype(np.float32)},
        "language": {
            LANGUAGE_KEY: [["pick up the apple"]] * batch_size,
        },
    }
```

```python
def fake_process_observation(observation, embodiment_tag):
        return BatchFeature(
            data={
                "state": torch.randn(1, 1, 128),
                "action_mask": torch.ones(1, 16, 128),
                "embodiment_id": torch.zeros(1, dtype=torch.long),
                "input_ids": torch.ones(1, 10, dtype=torch.long),
                "attention_mask": torch.ones(1, 10, dtype=torch.long),
                "pixel_values": torch.randn(1, 3, 256, 256),
                "image_grid_thw": torch.tensor([[1, 16, 16]]),
            }
        )
```

```python
def test_valid_observation_passes(self, policy):
        obs = _make_observation()
        policy.check_observation(obs)
```
```

### tests/gr00t/policy/test_gr00t_policy_gpu.py

```
"""GPU integration test for Gr00tPolicy._get_action() with the real model architecture.

This top-down test exercises the full inference pipeline:
  Gr00tPolicy._get_action()
    → processor.__call__() (VLM tokenization + state/action normalization)
    → model.get_action() (backbone forward + DiT diffusion denoising)
    → processor.decode_action() (denormalization + action decoding)

Covers modules with 0% or low coverage that cannot be tested on CPU:
  - gr00t_n1d7.py (model forward)
  - qwen3_backbone.py (VLM backbone)
  - dit.py / alternate_vl_dit.py (transformer)
  - embodiment_conditioned_"""
def _build_observation(policy, batch_size, seed)
def policy(request)
def test_warmup_model_load(policy)
class TestGr00tPolicyGPU()
    """End-to-end GPU inference through Gr00tPolicy."""
    def test_get_action_keys_match_config(self, policy)
    def test_get_action_shapes(self, policy)
    def test_get_action_values_finite_and_bounded(self, policy)
    def test_get_action_batch(self, policy)
    def test_get_action_deterministic(self, policy)
    def test_get_action_accepts_different_inputs(self, policy)

```python
def _build_observation(policy, batch_size=1, seed=42):
    """Build a synthetic observation that matches the policy's modality config.

    Uses a fixed seed so that failures are reproducible.
    """
    rng = np.random.RandomState(seed)
    mc = policy.modality_configs

    video_horizon = len(mc["video"].delta_indices)
    state_horizon = len(mc["state"].delta_indices)

    obs = {"video": {}, "state": {}, "language": {}}

    for k in mc["video"].modality_keys:
        obs["video"][k] = rng.randint(
            0, 255, (batch_size, video_horizon, 256, 256, 3), dtype=np.uint8
        )

    embodiment_val = policy.embodiment_tag.value
    norm_params = policy.processor.state_action_processor.norm_params[embodiment_val]["state"]
    for k in mc["state"].modality_keys:
        dim = int(norm_params[k]["dim"])
        obs["state"][k] = rng.randn(batch_size, state_horizon, dim).astype(np.float32)

    language_key = mc["language"].modality_keys[0]
    obs["language"][language_key] = [["pick up the red cube"]] * batch_size

    return obs
```
```

### tests/gr00t/policy/test_policy_service.py

```
"""Test PolicyServer and PolicyClient ZMQ communication.

Uses a mock policy to avoid loading real model weights. The server is
started in a background thread and the client connects on localhost."""
class MockPolicy()
    """Minimal mock that satisfies BasePolicy interface without ABC enforcement."""
    def __init__(self)
    def get_action(self, observation, options)
    def reset(self, options)
    def get_modality_config(self)
    def check_observation(self, observation)
    def check_action(self, action)
def _find_free_port()
def server_client()
class TestPolicyServerClient()
    """Test ZMQ roundtrip communication."""
    def test_ping(self, server_client)
    def test_get_action_roundtrip(self, server_client)
    def test_reset(self, server_client)
    def test_get_modality_config(self, server_client)
    def test_kill_server(self)
    def test_unknown_endpoint_returns_error(self, server_client)
class TestPolicyServerAuth()
    """Test API token authentication."""
    def test_valid_token(self)
    def test_invalid_token(self)
class TestMsgSerializer()
    """Test msgpack serialization helpers."""
    def test_roundtrip_dict(self)
    def test_roundtrip_numpy(self)
    def test_encode_numpy_payload_is_legacy_msgpack_numpy_compatible(self)
    def test_decode_npy_numpy_payload(self)
    def test_roundtrip_modality_config(self)
    def test_encode_modality_config_uses_legacy_marker(self)
    def test_decode_modality_config_class_marker(self)
    def test_encode_rejects_object_dtype_ndarray(self)
    def test_decode_rejects_object_dtype_ndarray_bin_keys(self)
    def test_decode_rejects_object_dtype_ndarray_str_keys(self)
    def test_decode_rejects_object_dtype_ndarray_int_nd(self)
    def test_decode_raises_on_marker_without_payload(self)
def _can_bind(host, port)
class TestPolicyServerLifecycle()
    """Pin that ``PolicyServer.close()`` / ``__exit__`` actually release the OS port."""
    def test_close_releases_bound_port(self)
    def test_close_is_idempotent(self)
    def test_context_manager_releases_port_on_exit(self)
    def test_context_manager_releases_port_when_body_raises(self)
    def test_start_server_releases_port_after_run_returns(self)
class TestPolicyClientLifecycle()
    """Pin that ``PolicyClient.__del__`` survives interpreter-shutdown attribute teardown."""
    def test_close_is_idempotent(self)
    def test_context_manager_closes_client(self)
    def test_del_does_not_raise_when_socket_attribute_missing(self)
    def test_del_does_not_raise_when_context_attribute_missing(self)
    def test_del_does_not_raise_on_partially_initialized_client(self)

```python
def check_observation(self, observation):
        pass
```
```

### tests/gr00t/utils/test_initial_actions_safety.py

```
"""CPU-only regression tests for the pickle-free
:func:`gr00t.utils.initial_actions.save_initial_actions` /
:func:`gr00t.utils.initial_actions.load_initial_actions` round-trip:
structured nested dicts must go through the flat keyed-npz layout
(``allow_pickle=False``-compatible), and any file written by the
legacy pickle-based path must be rejected with a migration error."""
def _sample_payload()
def test_roundtrip_preserves_structure_and_values(tmp_path)
def test_roundtrip_handles_empty_dataset_list(tmp_path)
def test_roundtrip_handles_dataset_with_no_trajectories(tmp_path)
def test_save_rejects_separator_in_trajectory_name(tmp_path)
def test_save_rejects_separator_in_action_key(tmp_path)
def test_load_rejects_legacy_pickle_format(tmp_path)
def test_load_rejects_npz_missing_schema_marker(tmp_path)
def test_load_rejects_unrecognised_format_marker(tmp_path)
```