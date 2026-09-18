# dexvla_2025

source: https://github.com/juruobenruo/DexVLA


commit: fc21a822f4c774e242eb6f1ab4a235788de7aba9


## README

<h1 align="center">
DexVLA: Vision-Language Model with Plug-In Diffusion Expert for Visuomotor Policy Learning</h1>

![](./docs/dexvla_banner.gif)

* **DexVLA: Vision-Language Model with Plug-In Diffusion Expert for Visuomotor Policy Learning** <br>
  [![arXiv](https://img.shields.io/badge/Arxiv-2502.05855-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2502.05855)
  


## 📰 News
* **`Mar. 11th, 2025`**: Add a script for training DiVLA.
* **`Feb. 24th, 2025`**: We released our Stage 1 trained ScaleDP-H !!!
* **`Feb. 17th, 2025`**: **DexVLA** is out! **Paper** can be found [here](https://arxiv.org/abs/2502.05855). The **project web** can be found [here](https://dex-vla.github.io/).

## Contents
- [Install](#install)
- [Data Preparation](#data-preparation)
- [Download Pretrained VLM](#Download-Pretrained-VLM)
- [Train](#train)
- [Evaluation](#evaluation)
- [DiVLA](#diffusion-vla)
- [ScaleDP](#scaledp)

## Install

1. Clone this repository and navigate to diffusion-vla folder
```bash
git clone https://github.com/juruobenruo/dexvla.git
```
Install Packages
```Shell
conda create -n dexvla python=3.10 -y
conda activate dexvla
pip install --upgrade pip  # 
pip install -r requirements.txt
cd policy_heads
pip install -e .
```
For training acceleration, please install [flash_attention](https://github.com/Dao-AILab/flash-attention).
```shell
pip install flash-attn --no-build-isolation
```

## Data Preparation
We provide an example data [here](https://huggingface.co/datasets/lesjie/dexvla_example_data). You can download it and run the whole pipeline quickly.
1. Our data format is the same as [act](https://github.com/MarkFzp/act-plus-plus), so you need to transfer your data into h5py format. You can refer to function "generate_h5" in [data_preprocess_scripts/rlds_to_h5py.py](
https://github.com/juruobenruo/DexVLA/blob/main/data_preprocess_scripts/rlds_to_h5py.py) which is used to transfer the data from rlds format to h5py format.
```angular2html
# h5 data structure
root
  |-action (100,10)
  |-language_raw (1,)
  |-substep_reasonings (100,)
  |-observations
      |-images # multi-view
          |-left (100,480,640,3)
          |-right (100,480,640,3)
          |-wrist (100,480,640,3)
      |-joint_positions (100,7)
      |-qpos (100,7)
      |-qvel (100,7)
```
2. You have to add one entry in [constants.py](https://github.com/juruobenruo/DexVLA/blob/main/aloha_scripts/constants.py) to specify the path of your data as follows.
```python
    'example_task_name': { # for local debug
        'dataset_dir': [
            '/path/to/task1', # define the path of the dataset
        ],
        'episode_len': 1000,  
        'camera_names': ['left', 'right', 'wrist'] # keys corresponding to below h5 data structure
    }
```

## 🤗Download Pretrained Weights
### Download official Qwen2_VL weights
We construct the VLM backbone by integrating Qwen2-VL-2B, a powerful and efficient model, into our framework. 
The Qwen2-VL 2B serves as the core of our architecture, providing robust capabilities 
for vision-language tasks. We use off-the-shelf Qwen2-VL model proposed 
in [Qwen2-VL](https://arxiv.org/pdf/2409.12191) without any post training on VLM itself. You can download the official weights from this link:

| Model               | Link                                                           |
|---------------------|----------------------------------------------------------------|
| Qwen2-VL (~2B)      | [huggingface](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) |

**❗❗** After downloading the standard weights, you have to replace the official "config.json"
with our "docs/config.json" designed for VLA.
### Download our pretrained ScaleDP-H weights(Stage 1)
We released our pretrained weights of ScaleDP-H which is trained after Stage1. Now you can download the weights and directly finetuning your data on Stage 2.

| Model             | Link                                                           |
|-------------------|----------------------------------------------------------------|
| ScaleDP-H (~1B)   | [huggingface](https://huggingface.co/lesjie/scale_dp_h)  |
| ScaleDP-L (~400M) | [huggingface](https://huggingface.co/lesjie/scale_dp_l)  |

## 🦾Train
The training script are "scripts/stage2_train.sh" and "scripts/stage3_train.sh". And you need to change following parameters:
1. **OUTPUT** :refers to the save directory for training, which must include the keyword "qwen2"(and optionally "lora"). If LoRA training is used, the name must include "lora" (e.g., "qwen2_lora").
2. **task_name** :refers to the tasks used for training, which should be corresponded to "your_task_name" in aloha_scripts/constant.py
3. **model_name_or_path** :path to the pretrained VLM weights

Other hyperparameters like "batch_size", "save_steps" could be customized according to your computation resources.
Start training by following commands:

Train stage2. Training on large amount of tasks.
And following hyper-parameters must be set as:
1. **load_pretrain_dit** : True
2. **DIT_PRETRAIN** :Path to pretrained policy head(ScaleDP).
3. **MNOP** :Path to official Qwen2_vl weights(VLM backbone).

```shell
./scripts/train_dexvla_stage2.sh 
```
Train stage3. Post-training on target dexterous tasks. 
And following hyper-parameters must be set as:
1. **MNOP** :Path to trained DexVLA of Stage2.

```shell
./scripts/train_dexvla_stage3.sh 
```

## Evaluation
**❗❗** Make sure your trained checkpoint dir has two files: "preprocessor_config.json" and "chat_template.json".
If not, please copy them from downloaded Qwen2_vl weights or this [link](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct/tree/main).

You can refer to our evaluation script [smart_eval_agilex.py](https://github.com/juruobenruo/DexVLA/blob/main/evaluate/smart_eval_agilex.py) to evaluate your DexVLA.

## ⚠️ Trouble Shooting
### 1."TypeError: _batch_encode_plus() got an unexpected keyword argument 'images'". 
Copy "preprocessor_config.json" and "chat_template.json" into your own trained 
DexVLA dir. And must be put in target "checkpoint-XXXX" dir.
~~~
Traceback (most recent call last):
  File "/media/rl/HDD/projects/open_dexvla_preview/train_vla.py", line 320, in <module>
    main(all_config=config, model_config=model_config)
  File "/media/rl/HDD/projects/open_dexvla_preview/train_vla.py", line 282, in main
    train_dataset, val_dataset, stats, sampler_params = load_data(dataset_dir, name_filter, camera_names, all_config['training_args'].per_device_train_batch_size,
  File "/media/rl/HDD/projects/open_dexvla_preview/data_utils/utils.py", line 337, in load_data
    train_dataset = EpisodicDataset(dataset_path_list, camera_names, norm_stats, train_episode_ids, train_episode_len, chunk_size, policy_class, robot=robot, llava_pythia_process=llava_pythia_process, data_args=config['data_args'])
  File "/media/rl/HDD/projects/open_dexvla_preview/data_utils/utils.py", line 43, in __init__
    a=self.__getitem__(0) # initialize self.is_sim and self.transformations
  File "/media/rl/HDD/projects/open_dexvla_preview/data_utils/utils.py", line 191, in __getitem__
    return self.llava_pythia_process.forward_process(sample, use_reasoning=self.data_args.use_reasoning)
  File "/media/rl/HDD/projects/open_dexvla_preview/qwen2_vla/utils/robot_data_processor.py", line 87, in forward_process
    model_inputs = self.multimodal_processor(
  File "/home/rl/miniconda3/envs/opendexvla/lib/python3.8/site-packages/transformers/tokenization_utils_base.py", line 3016, in __call__
    encodings = self._call_one(text=text, text_pair=text_pair, **all_kwargs)
  File "/home/rl/miniconda3/envs/opendexvla/lib/python3.8/site-packages/transformers/tokenization_utils_base.py", line 3126, in _call_one
    return self.encode_plus(
  File "/home/rl/miniconda3/envs/opendexvla/lib/python3.8/site-packages/transformers/tokenization_utils_base.py", line 3202, in encode_plus
    return self._encode_plus(
  File "/home/rl/miniconda3/envs/opendexvla/lib/python3.8/site-packages/transformers/tokenization_utils_fast.py", line 603, in _encode_plus
    batched_output = self._batch_encode_plus(
TypeError: _batch_encode_plus() got an unexpected keyword argument 'images'
~~~
### 2. <font color=red>CUDA OOM</font>. 
For OOM problem, we provide three ways to save CUDA memory. You can use only one solution or all of them. And here we listed the training speed, GPU memory for all three solutions.
Notably, all results are evaluated on **single** A6000(46G) with batch_size 2. 

❗Notably, deepspeed may takes more GPU memory on single gpu with zero2 optimization.

| Script                   | DeepSpeed offload | LoRA VLM | Smaller ScaleDP | training speed | CUDA memory |
|--------------------------|-------------------|----------|-----------------|----------------|-------------|
| local_debug_deepspeed.sh | ✔️                | -        | -               | 6.56s/iter     | 20-29G      |
| local_debug_python.sh    | -                 | ✔️       | -               | 1.09s/iter     | 24G         |
| local_debug_python.sh    | -                 | -        | ✔️              | 1.01s/iter     | 33G         |
| local_debug_python.sh    | -                 | -        | -               | 1.1s/iter      | 38G         |
#### Deepspeed offload
Deepspeed allows to offload optimizer part to cpu which saves a lot of cuda memory. You can enbale the offload by adding following part in scripts/zero2.json. 
Please make sure your GCC version > 9.
~~~json
    "zero_optimization": {
        "stage": 2,
        "overlap_comm": true,
        "contiguous_gradients": true,
        "sub_group_size": 1e9,
        "reduce_bucket_size": "auto",
        //##Adding this part to zero2.json###
        "offload_optimizer": {
            "device": "cpu",
            "pin_memory": true
        }
        //###################################
    },
~~~
#### LoRA Finetune
Our scripts facilitate LoRA (Low-Rank Adaptation) fine-tuning of the Vision-Language Model (VLM) backbone. This approach is effective in reducing GPU memory usage. Meanwhile, the policy head continues to undergo full parameter training.

To enable LoRA, you can set the following hyperparameters within the training scripts:
~~~ shell
  ...
  --lora_enable True \
  ...
  --freeze_vision_tower True \
  --freeze_backbone True \
  ...
~~~
**Notice:** After LoRA finetune, you need to process the checkpoint files as follows:
~~~ shell
cd /path/to/finetuned/dir/checkpoint-xxxx
python ./zero_to_fp32.py ./ ./non_lora_trainables.bin
~~~
For evaluation, you have to specify following arguments in ``evaluate/smart_eval_agilex.py``:
~~~
"model_base": None, # path to base model
"enable_lora": True, 
~~~

#### Smaller ScaleDP
Our DexVLA consists of two parts: the VLM backbone and the ScaleDP policy head. In our paper, we utilize a 1B - sized ScaleDP. Additionally, we recommend that users employ a smaller one, such as a 410M - sized ScaleDP, to save memory.

By setting the following hyperparameters:
~~~ shell
  ...
  --policy_head_size "ScaleDP_L" \
  ...
~~~
### 3. Action value is <font color=red>Nan</font> during inference which happens at the last denoising in "policy_heads/models/transformer_diffusion/modeling_dit_diffusion.py". 
This is a precision overflow problem in "[DDIMScheduler](https://github.com/huggingface/diffusers/blob/v0.11.1/src/diffusers/schedulers/scheduling_ddim.py)" from diffusers.schedulers.scheduling_ddim. The easiest way is adding a line in "scheduling_ddim.py"
~~~python
        ###other code###
        else:
            raise NotImplementedError(f"{beta_schedule} does is not implemented for {self.__class__}")
        
        ### newly added ###############################
        self.betas = self.betas.to(dtype=torch.float32)
        ###############################################
        self.alphas = 1.0 - self.betas
        self.alphas_cumprod = torch.cumprod(self.alphas, dim=0)
        ###other code###
~~~

### 4. Robot performs <font color=red>random actions</font> when evaluation.
This is a bug in evaluation which not affect the training process. Sorry about that and we have fixed this in [23e29e1](https://github.com/juruobenruo/DexVLA/commit/23e29e16a65eac72d940d55f5475e20c996f1e42).

# Diffusion-VLA
Our DexVLA is built on Diffusion-VLA(DiVLA) which can be found [here](https://diffusion-vla.github.io/). Paper can be found in [Citation](#citation). You can train Diffusion-VLA with "./scripts/train_divla.sh".
The mainly differences are as follows:
1. DiVLA utilizes Unet-based diffusion policy as policy head of VLA.
2. DiVLA has no three-stage training recipe. 

# ScaleDP
DexVLA utilizes ScaleDP as diffusion policy head that the main structure of ScaleDP can be found [here](https://scaling-diffusion-policy.github.io/).  Paper can be found in [Citation](#citation). The code can be found in this [dir](https://github.com/juruobenruo/DexVLA/tree/main/policy_heads/models/transformer_diffusion). There are only two files, one for configuration and the other is model structure.

## Acknowledgement
We build our project based on:
- [LLaVA](https://github.com/haotian-liu/LLaVA): an amazing open-sourced project for vision language assistant
- [act-plus-plus](https://github.com/haotian-liu/LLaVA): an amazing open-sourced project for robotics visuomotor learning
- [Miphi](https://github.com/zhuyiche/llava-phi): an amazing open-sourced project for tiny vision language model

## Citation

```bibtex
# DexVLA
@article{wen2025dexvla,
  title={DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control},
  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Tang, Zhibin and Shen, Chaomin and Feng, Feifei},
  journal={arXiv preprint arXiv:2502.05855},
  year={2025}
}

# Diffusion-VLA
@article{wen2024diffusion,
  title={Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression},
  author={Wen, Junjie and Zhu, Minjie and Zhu, Yichen and Tang, Zhibin and Li, Jinming and Zhou, Zhongyi and Li, Chengmeng and Liu, Xiaoyu and Peng, Yaxin and Shen, Chaomin and others},
  journal={arXiv preprint arXiv:2412.03293},
  year={2024}
}

# ScaleDP
@article{zhu2024scaling,
  title={Scaling diffusion policy in transformer to 1 billion parameters for robotic manipulation},
  author={Zhu, Minjie and Zhu, Yichen and Li, Jinming and Wen, Junjie and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and others},
  journal={arXiv preprint arXiv:2409.14411},
  year={2024}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
aloha_scripts/
  __init__.py
  constants.py
  utils.py
data_preprocess_scripts/
  rlds_to_h5py.py
data_utils/
  __init__.py
  check_data_integrity.py
  data_collators.py
  truncate_data.py
  utils.py
evaluate/
  smart_eval_agilex.py
policy_heads/
  LICENSE
  README.md
  __init__.py
  main.py
  models/
    transformer_diffusion/
    unet_diffusion/
  setup.py
  util/
    __init__.py
    box_ops.py
    misc.py
    plot_utils.py
qwen2_vla/
  __init__.py
  model_load_utils.py
  models/
    __init__.py
    configuration_qwen2_vla.py
    modeling_qwen2_vla.py
  train/
    qwen2_vla_trainer.py
  utils/
    fusion_modules.py
    image_processing_qwen2_vla.py
    processing_qwen2_vla.py
    robot_data_processor.py
requirements.txt
scripts/
  for_debug/
    local_debug_deepspeed.sh
    local_debug_python.sh
  train_dexvla_stage2.sh
  train_dexvla_stage3.sh
  train_divla.sh
  zero2.json
  zero3.json
setup.py
torch_utils.py
train_vla.py
```

## Config files (0)


## Python signatures and reward/observation bodies (14 files)


### policy_heads/main.py

```
def get_args_parser()
def build_ACT_model_and_optimizer(args_override)
def build_CNNMLP_model_and_optimizer(args_override)
```

### policy_heads/models/transformer_diffusion/configuration_scaledp.py

```
class ScaleDPPolicyConfig(PretrainedConfig)
    """Configuration for ScaleDP policy head"""
    def __init__(self, eval, action_dim, cond_dim, state_dim, prediction_horizon, n_obs_steps, depth, n_emb, num_heads, mlp_ratio, time_as_cond, obs_as_cond, learn_sigma, model_size, num_inference_timesteps, noise_samples, num_train_timesteps, is_tinyvla)
    def from_pretrained(cls, pretrained_model_name_or_path)
```

### policy_heads/models/transformer_diffusion/modeling_scaledp.py

```
class Attention(Module)
    def __init__(self, dim, num_heads, qkv_bias, qk_norm, attn_drop, proj_drop, norm_layer)
    def forward(self, x, attn_mask)
def modulate(x, shift, scale)
class TimestepEmbedder(Module)
    """Embeds scalar timesteps into vector representations."""
    def __init__(self, hidden_size, frequency_embedding_size)
    def timestep_embedding(t, dim, max_period)
    def forward(self, t)
class ScaleDPBlock(Module)
    """A ScaleDP block with adaptive layer norm zero (adaLN-Zero) conScaleDPioning."""
    def __init__(self, hidden_size, num_heads, mlp_ratio)
    def forward(self, x, c, attn_mask)
class FinalLayer(Module)
    """The final layer of ScaleDP."""
    def __init__(self, hidden_size, output_dim)
    def forward(self, x, c)
class ScaleDP(PreTrainedModel)
    """Diffusion models with a Transformer backbone."""
    def __init__(self, config)
    def initialize_weights(self)
    def get_optim_groups(self, weight_decay)
    def configure_optimizers(self, learning_rate, weight_decay, betas)
    def forward(self, actions, hidden_states, states, is_pad)
    def model_forward(self, x, t, global_cond, states)
def get_2d_sincos_pos_embed(embed_dim, grid_size, cls_token, extra_tokens)
def get_2d_sincos_pos_embed_from_grid(embed_dim, grid)
def get_1d_sincos_pos_embed_from_grid(embed_dim, pos)
def ScaleDP_H()
def ScaleDP_L()
```

### policy_heads/models/unet_diffusion/configuration_unet_diffusion.py

```
class UnetDiffusionPolicyConfig(PretrainedConfig)
    """Configuration for dit diffusion policy head"""
    def __init__(self, action_dim, global_cond_dim, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, state_dim, prediction_horizon, noise_samples, num_inference_timesteps, num_train_timesteps)
    def from_pretrained(cls, pretrained_model_name_or_path)
```

### policy_heads/models/unet_diffusion/modeling_unet_diffusion.py

```
"""Implementation of Diffusion Policy https://diffusion-policy.cs.columbia.edu/ by Cheng Chi"""
class SinusoidalPosEmb(Module)
    def __init__(self, dim, dtype)
    def forward(self, x)
class Downsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Upsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Conv1dBlock(Module)
    """Conv1d --> GroupNorm --> Mish"""
    def __init__(self, inp_channels, out_channels, kernel_size, n_groups)
    def forward(self, x)
class ConditionalResidualBlock1D(Module)
    def __init__(self, in_channels, out_channels, cond_dim, kernel_size, n_groups)
    def forward(self, x, cond)
class ConditionalUnet1D(PreTrainedModel)
    def __init__(self, config)
    def forward(self, actions, hidden_states, states, is_pad)
    def model_forward(self, sample, timestep, global_cond, states)
```

### policy_heads/util/box_ops.py

```
"""Utilities for bounding box manipulation and GIoU."""
def box_cxcywh_to_xyxy(x)
def box_xyxy_to_cxcywh(x)
def box_iou(boxes1, boxes2)
def generalized_box_iou(boxes1, boxes2)
def masks_to_boxes(masks)
```

### policy_heads/util/misc.py

```
"""Misc functions, including distributed helpers.

Mostly copy-paste from torchvision references."""
class SmoothedValue(object)
    """Track a series of values and provide access to smoothed values over a
window or the global series average."""
    def __init__(self, window_size, fmt)
    def update(self, value, n)
    def synchronize_between_processes(self)
    def median(self)
    def avg(self)
    def global_avg(self)
    def max(self)
    def value(self)
    def __str__(self)
def all_gather(data)
def reduce_dict(input_dict, average)
class MetricLogger(object)
    def __init__(self, delimiter)
    def update(self)
    def __getattr__(self, attr)
    def __str__(self)
    def synchronize_between_processes(self)
    def add_meter(self, name, meter)
    def log_every(self, iterable, print_freq, header)
def get_sha()
def collate_fn(batch)
def _max_by_axis(the_list)
class NestedTensor(object)
    def __init__(self, tensors, mask)
    def to(self, device)
    def decompose(self)
    def __repr__(self)
def nested_tensor_from_tensor_list(tensor_list)
def _onnx_nested_tensor_from_tensor_list(tensor_list)
def setup_for_distributed(is_master)
def is_dist_avail_and_initialized()
def get_world_size()
def get_rank()
def is_main_process()
def save_on_master()
def init_distributed_mode(args)
def accuracy(output, target, topk)
def interpolate(input, size, scale_factor, mode, align_corners)
```

### policy_heads/util/plot_utils.py

```
"""Plotting utilities to visualize training logs."""
def plot_logs(logs, fields, ewm_col, log_name)
def plot_precision_recall(files, naming_scheme)
```

### qwen2_vla/models/configuration_qwen2_vla.py

```
"""Qwen2VL model configuration"""
class Qwen2VLAVisionConfig(PretrainedConfig)
    def __init__(self, depth, embed_dim, hidden_size, hidden_act, mlp_ratio, num_heads, in_channels, patch_size, spatial_merge_size, temporal_patch_size)
    def from_pretrained(cls, pretrained_model_name_or_path)
class Qwen2VLAConfig(PretrainedConfig)
    """This is the configuration class to store the configuration of a [`Qwen2VLModel`]. It is used to instantiate a
Qwen2-VL model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of
Qwen2-VL-7"""
    def __init__(self, vocab_size, hidden_size, intermediate_size, num_hidden_layers, num_attention_heads, num_key_value_heads, hidden_act, max_position_embeddings, initializer_range, rms_norm_eps, use_cache, tie_word_embeddings, rope_theta, use_sliding_window, sliding_window, max_window_layers, attention_dropout, vision_config, rope_scaling, policy_head_type)
```

### qwen2_vla/train/qwen2_vla_trainer.py

```
def maybe_zero_3(param, ignore_status, name)
def get_mm_adapter_state_maybe_zero_3(named_params, keys_to_match)
def split_to_even_chunks(indices, lengths, num_chunks)
def get_modality_length_grouped_indices(lengths, batch_size, world_size, generator)
def get_length_grouped_indices(lengths, batch_size, world_size, generator, merge)
class LengthGroupedSampler(Sampler)
    """Sampler that samples indices in a way that groups together features of the dataset of roughly the same length while
keeping a bit of randomness."""
    def __init__(self, batch_size, world_size, lengths, generator, group_by_modality)
    def __len__(self)
    def __iter__(self)
class CustomBatchSampler(Sampler)
    def __init__(self, batch_size, episode_len_l, sample_weights, replacement, eval, episode_first)
    def __iter__(self)
def _is_peft_model(model)
class QWen2VLATrainer(Trainer)
    def __init__(self, sampler_params, prefetch_factor)
    def get_train_dataloader(self)
    def get_eval_dataloader(self, eval_dataset)
    def _get_train_sampler(self)
    def create_optimizer(self)
    def training_step(self, model, inputs)
    def _inner_training_loop(self, batch_size, args, resume_from_checkpoint, trial, ignore_keys_for_eval)
    def _maybe_log_save_evaluate(self, tr_loss, model, trial, epoch, ignore_keys_for_eval, all_loss)
    def _load_from_checkpoint(self, resume_from_checkpoint, model)
    def _save_checkpoint(self, model, trial, metrics, using_ema)
    def _save(self, output_dir, state_dict)
```

### train_vla.py

```
class ActionHeadArguments()
class ModelArguments()
class DataArguments()
class TrainingArguments(TrainingArguments)
def rank0_print()
def parse_param()
def train_bc(train_dataset, val_dataset, model, config, sampler_params, tokenizer, processor)
def main(all_config, model_config)
```