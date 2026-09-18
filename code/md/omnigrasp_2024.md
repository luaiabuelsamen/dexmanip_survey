# omnigrasp_2024

source: https://github.com/ZhengyiLuo/Omnigrasp


commit: f7740cdc31aa4a0e152533b96d10de7d4d7aaacd


## File tree (depth 3, assets pruned)

```
.gitignore
README.MD
download_data.sh
index.html
phc/
  __init__.py
  env/
    __init__.py
    tasks/
    util/
  learning/
    __init__.py
    amp_agent.py
    amp_datasets.py
    amp_models.py
    amp_network_builder.py
    amp_network_mcp_builder.py
    amp_network_omnigrasp_builder.py
    amp_network_pnn_builder.py
    amp_network_tcn_builder.py
    amp_network_z_builder.py
    amp_network_z_part_builder.py
    amp_players.py
    ar_prior.py
    common_agent.py
    common_player.py
    im_amp.py
    im_amp_players.py
    kin_tcn.py
    loss_functions.py
    network_builder.py
    network_loader.py
    pnn.py
    replay_buffer.py
    running_norm.py
    task_agent.py
    task_models.py
    tcn.py
    transformer.py
    transformer_layers.py
    vq_quantizer.py
  run_hydra.py
  utils/
    __init__.py
    benchmarking.py
    config.py
    data_tree.py
    draw_utils.py
    flags.py
    isaacgym_torch_utils.py
    logger.py
    motion_lib_base.py
    motion_lib_smpl.py
    motion_lib_smpl_obj.py
    o3d_utils.py
    parse_task.py
    plot_script.py
    point_utils.py
    pytorch3d_transforms.py
    running_mean_std.py
    torch_smpl_humanoid_sk_batch.py
    torch_utils.py
    traj_generator.py
    traj_generator_3d.py
    traj_generator_3d_orig.py
requirement.txt
scripts/
  data_process/
    compute_bps.py
    convert_amass_data.py
    convert_amass_isaac.py
    convert_amassx_data.py
    convert_data_mdm.py
    convert_data_smpl.py
    convert_data_smplx.py
    convert_dexterous_amass_data.py
    convert_grab_smplx.py
    grad_fit_interhands.py
    process_amass_db.py
    process_amass_raw.py
    process_grab_raw.py
    process_interhands.py
  demo/
    video_to_pose_server.py
  eval/
    eval_omnigrasp.py
    reload_obj_feast.py
  joint_monkey_smpl.py
  mdm_test.py
  mjcf_to_urdf.py
  pmcp/
    forward_pmcp.py
  quest_camera.py
  render_smpl_o3d.py
  train_model.py
  vis/
    test_sim.py
    vis_grab_motion_mj.py
    vis_mano_o3d.py
    vis_mesh.py
    vis_motion.py
    vis_motion_mano.py
    vis_motion_mj.py
    vis_obj_o3d.py
    vis_plt.py
    vis_render.py
    vis_smpl_o3d.py
    vis_smpl_o3d_ego.py
    vis_smpl_o3d_multi.py
    vis_smpl_o3d_single.py
    vis_smplx_grab_o3d.py
    vis_smplx_mano_o3d.py
    vis_smplx_o3d.py
    vis_turtle.py
    vis_world_model.py
  ws_client.py
```

## Config files (0)


## Python signatures and reward/observation bodies (31 files)


### phc/env/tasks/base_task.py

```
class BaseTask()
    def __init__(self, cfg, enable_camera_sensors)
    def create_viewer(self)
    def set_sim_params_up_axis(self, sim_params, axis)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def step(self, actions)
    def get_states(self)
    def _clear_recorded_states(self)
    def _record_states(self)
    def _write_states_to_file(self, file_name)
    def setup_video_client(self)
    def setup_talk_client(self)
    def talk(self)
    def video_stream(self)
    def render(self, sync_frame_time)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)
    def pre_physics_step(self, actions)
    def _physics_step(self)
    def post_physics_step(self)
def get_attr_val_from_sample(sample, offset, prop, attr)
```

### phc/env/tasks/humanoid.py

```
class Humanoid(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _load_proj_asset(self)
    def _build_proj(self, env_id, env_ptr)
    def _setup_tensors(self)
    def load_humanoid_configs(self, cfg)
    def load_common_humanoid_configs(self, cfg)
    def load_smpl_configs(self, cfg)
    def _clear_recorded_states(self)
    def _record_states(self)
    def _write_states_to_file(self, file_name)
    def get_obs_size(self)
    def get_running_mean_size(self)
    def get_self_obs_size(self)
    def get_action_size(self)
    def get_dof_action_size(self)
    def get_num_actors_per_env(self)
    def create_sim(self)
    def reset(self, env_ids)
    def change_char_color(self)
    def sample_char_color(self, cols, env_ids)
    def set_char_color(self, col, env_ids)
    def _reset_envs(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _create_ground_plane(self)
    def _setup_character_props(self, key_bodies)
    def _build_self_obs_part_index(self)
    def _build_termination_heights(self)
    def _create_smpl_humanoid_xml(self, num_humanoids, smpl_robot, queue, pid)
    def _load_amass_gender_betas(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def create_humanoid_force_sensors(self, humanoid_asset, sensor_joint_names)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _build_pd_action_offset_scale(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _refresh_sim_tensors(self)
    def _compute_observations(self, env_ids)
    def _compute_humanoid_obs(self, env_ids)
    def _reset_actors(self, env_ids)
    def pre_physics_step(self, actions)
    def _compute_torques(self, actions)
    def _physics_step(self)
    def _init_tensor_history(self, env_ids)
    def _update_tensor_history(self)
    def post_physics_step(self)
    def render(self, sync_frame_time)
    def _build_key_body_ids_tensor(self, key_body_names)
    def _build_key_body_ids_orig_tensor(self, key_body_names)
    def _build_contact_body_ids_tensor(self, contact_body_names)
    def _action_to_pd_targets(self, action)
    def _init_camera(self)
    def _update_camera(self)
    def _update_debug_viz(self)
def dof_to_obs_smpl(pose)
def dof_to_obs(pose, dof_obs_size, dof_offsets)
def compute_humanoid_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets)
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs)
def compute_humanoid_reward(obs_buf)
def compute_humanoid_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, max_episode_length, enable_early_termination, termination_heights)
def remove_base_rot(quat)
def compute_humanoid_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, dof_obs_size, dof_offsets, smpl_params, local_root_obs, root_height_obs, upright, has_smpl_params)
def compute_humanoid_observations_smpl_max(body_pos, body_rot, body_vel, body_ang_vel, smpl_params, limb_weight_params, local_root_obs, root_height_obs, upright, has_smpl_params, has_limb_weight_params)
def compute_humanoid_observations_smpl_max_v2(body_pos, body_rot, body_vel, body_ang_vel, smpl_params, limb_weight_params, local_root_obs, root_height_obs, upright, has_smpl_params, has_limb_weight_params, time_steps)
def compute_humanoid_observations_smpl_max_v3(body_pos, body_rot, body_vel, body_ang_vel, force_sensor_readings, smpl_params, limb_weight_params, local_root_obs, root_height_obs, upright, has_smpl_params, has_limb_weight_params)

```python
def compute_humanoid_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, int, List[int]) -> Tensor
    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    local_root_vel = torch_utils.my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_to_obs(dof_pos, dof_obs_size, dof_offsets)

    obs = torch.cat((root_h_obs, root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos), dim=-1)
    return obs
```

```python
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs):
    # type: (Tensor, Tensor, Tensor, Tensor, bool, bool) -> Tensor
    root_pos = body_pos[:, 0, :]
    root_rot = body_rot[:, 0, :]

    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, body_pos.shape[1], 1))
    flat_heading_rot = heading_rot_expand.reshape(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])

    root_pos_expand = root_pos.unsqueeze(-2)
    local_body_pos = body_pos - root_pos_expand
    flat_local_body_pos = local_body_pos.reshape(local_body_pos.shape[0] * local_body_pos.shape[1], local_body_pos.shape[2])
    flat_local_body_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_local_body_pos)
    local_body_pos = flat_local_body_pos.reshape(local_body_pos.shape[0], local_body_pos.shape[1] * local_body_pos.shape[2])
    local_body_pos = local_body_pos[..., 3:]  # remove root pos

    flat_body_rot = body_rot.reshape(body_rot.shape[0] * body_rot.shape[1], body_rot.shape[2])  # global body rotation
    flat_local_body_rot = quat_mul(flat_heading_rot, flat_body_rot)
    flat_local_body_rot_obs = torch_utils.quat_to_tan_norm(flat_local_body_rot)
    local_body_rot_obs = flat_local_body_rot_obs.reshape(body_rot.shape[0], body_rot.shape[1] * flat_local_body_rot_obs.shape[1])

    if (local_root_obs):
        root_rot_obs = torch_utils.quat_to_tan_norm(root_rot)
        local_body_rot_obs[..., 0:6] = root_rot_obs

    flat_body_vel = body_vel.reshape(body_vel.shape[0] * body_vel.shape[1], body_vel.shape[2])
    flat_local_body_vel = torch_utils.my_quat_rotate(flat_heading_rot, flat_body_vel)
    local_body_vel = flat_local_body_vel.reshape(body_vel.shape[0], body_vel.shape[1] * body_vel.shape[2])

    flat_body_ang_vel = body_ang_vel.reshape(body_ang_vel.shape[0] * body_ang_vel.shape[1], body_ang_vel.shape[2])
    flat_local_body_ang_vel = torch_utils.my_quat_rotate(flat_heading_rot, flat_body_ang_vel)
    local_body_ang_vel = flat_local_body_ang_vel.reshape(body_ang_vel.shape[0], body_ang_vel.shape[1] * body_ang_vel.shape[2])

    obs = torch.cat((root_h_obs, local_body_pos, local_body_rot_obs, local_body_vel, local_body_ang_vel), dim=-1)
    return obs
```

```python
def compute_humanoid_reward(obs_buf):
    # type: (Tensor) -> Tensor
    reward = torch.ones_like(obs_buf[:, 0])
    return reward
```

```python
def compute_humanoid_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, dof_obs_size, dof_offsets, smpl_params, local_root_obs, root_height_obs, upright, has_smpl_params):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, int, List[int], Tensor, bool, bool,bool, bool) -> Tensor
    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    local_root_vel = torch_utils.my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_to_obs(dof_pos, dof_obs_size, dof_offsets)

    obs_list = []
    if root_height_obs:
        obs_list.append(root_h_obs)
    obs_list += [
        root_rot_obs,
        local_root_vel,
        local_root_ang_vel,
        dof_obs,
        dof_vel,
        flat_local_key_pos,
    ]
    if has_smpl_params:
        obs_list.append(smpl_params)
    obs = torch.cat(obs_list, dim=-1)

    return obs
```

```python
def compute_humanoid_observations_smpl_max(body_pos, body_rot, body_vel, body_ang_vel, smpl_params, limb_weight_params, local_root_obs, root_height_obs, upright, has_smpl_params, has_limb_weight_params):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, bool, bool, bool) -> Tensor
    root_pos = body_pos[:, 0, :]
    root_rot = body_rot[:, 0, :]

    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot_inv = torch_utils.calc_heading_quat_inv(root_rot)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    heading_rot_inv_expand = heading_rot_inv.unsqueeze(-2)
    heading_rot_inv_expand = heading_rot_inv_expand.repeat((1, body_pos.shape[1], 1))
    flat_heading_rot_inv = heading_rot_inv_expand.reshape(heading_rot_inv_expand.shape[0] * heading_rot_inv_expand.shape[1], heading_rot_inv_expand.shape[2])

    root_pos_expand = root_pos.unsqueeze(-2)
    local_body_pos = body_pos - root_pos_expand
    flat_local_body_pos = local_body_pos.reshape(local_body_pos.shape[0] * local_body_pos.shape[1], local_body_pos.shape[2])
    flat_local_body_pos = torch_utils.my_quat_rotate(flat_heading_rot_inv, flat_local_body_pos)
    local_body_pos = flat_local_body_pos.reshape(local_body_pos.shape[0], local_body_pos.shape[1] * local_body_pos.shape[2])
    local_body_pos = local_body_pos[..., 3:]  # remove root pos

    flat_body_rot = body_rot.reshape(body_rot.shape[0] * body_rot.shape[1], body_rot.shape[2])  # This is global rotation of the body
    flat_local_body_rot = quat_mul(flat_heading_rot_inv, flat_body_rot)
    flat_local_body_rot_obs = torch_utils.quat_to_tan_norm(flat_local_body_rot)
    local_body_r
```

### phc/env/tasks/humanoid_amp.py

```
class HumanoidAMP(HumanoidZ)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _compute_observations(self, env_ids)
    def resample_motions(self)
    def pre_physics_step(self, actions)
    def get_task_obs_size_detail(self)
    def post_physics_step(self)
    def get_num_amp_obs(self)
    def fetch_amp_obs_demo(self, num_samples)
    def build_amp_obs_demo_steps(self, motion_ids, motion_times0, num_steps)
    def build_amp_obs_demo(self, motion_ids, motion_times0)
    def _build_amp_obs_demo_buf(self, num_samples)
    def _setup_character_props(self, key_bodies)
    def _load_motion(self, motion_file)
    def _reset_envs(self, env_ids)
    def _reset_actors(self, env_ids)
    def _reset_default(self, env_ids)
    def _sample_time(self, motion_ids)
    def _get_fixed_smpl_state_from_motionlib(self, motion_ids, motion_times, curr_gender_betas)
    def _get_state_from_motionlib_cache(self, motion_ids, motion_times, offset)
    def begin_seq_motion_samples(self)
    def _sample_ref_state(self, env_ids)
    def _reset_ref_state_init(self, env_ids)
    def _reset_hybrid_state_init(self, env_ids)
    def _compute_humanoid_obs(self, env_ids)
    def _init_amp_obs(self, env_ids)
    def _init_amp_obs_default(self, env_ids)
    def _init_amp_obs_ref(self, env_ids, motion_ids, motion_times)
    def _set_env_state(self, env_ids, root_pos, root_rot, dof_pos, root_vel, root_ang_vel, dof_vel, rigid_body_pos, rigid_body_rot, rigid_body_vel, rigid_body_ang_vel)
    def _refresh_sim_tensors(self)
    def _update_hist_amp_obs(self, env_ids)
    def _compute_amp_observations(self, env_ids)
    def _compute_amp_observations_from_state(self, root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, key_body_vels, smpl_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright)
    def _hack_motion_sync(self)
    def _update_camera(self)
    def _hack_consistency_test(self)
    def _hack_output_motion(self)
    def get_num_enc_amp_obs(self)
    def fetch_amp_obs_demo_enc_pair(self, num_samples)
    def fetch_amp_obs_demo_pair(self, num_samples)
def build_amp_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets)
def build_amp_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright)
def build_amp_observations_smpl_v2(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, key_body_vel, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright)

```python
def build_amp_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, int, List[int]) -> Tensor
    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    local_root_vel = torch_utils.my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_to_obs(dof_pos, dof_obs_size, dof_offsets)
    obs = torch.cat((root_h_obs, root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos), dim=-1)
    return obs
```

```python
def build_amp_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, bool, bool, bool, bool) -> Tensor
    B, N = root_pos.shape
    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot_inv = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot_inv, root_rot)
    else:
        root_rot_obs = root_rot

    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    local_root_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot_inv.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    if has_dof_subset:
        dof_vel = dof_vel[:, dof_subset]
        dof_pos = dof_pos[:, dof_subset]

    dof_obs = dof_to_obs_smpl(dof_pos)
    obs_list = []
    if root_height_obs:
        obs_list.append(root_h)
    obs_list += [root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos]
    # 1? + 6 + 3 + 3 + 114 + 57 + 12
    if has_shape_obs_disc:
        obs_list.append(shape_params)
    if has_limb_weight_obs:
        obs_list.append(limb_weight_params)
    obs = torch.cat(obs_list, dim=-1)
    
    return obs
```

```python
def build_amp_observations_smpl_v2(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, key_body_vel,  shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, bool, bool, bool, bool) -> Tensor
    B, N = root_pos.shape
    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot_inv = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot_inv, root_rot)
    else:
        root_rot_obs = root_rot

    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    local_root_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot_inv.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, local_key_body_pos.view(-1, 3)).view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])
    
    local_vel = torch_utils.my_quat_rotate(flat_heading_rot, key_body_vel.view(-1, 3)).view(key_body_vel.shape[0], key_body_vel.shape[1] * key_body_vel.shape[2])

    if has_dof_subset:
        dof_vel = dof_vel[:, dof_subset]
        dof_pos = dof_pos[:, dof_subset]

    dof_obs = dof_to_obs_smpl(dof_pos)
    obs_list = []
    if root_height_obs:
        obs_list.append(root_h)
    obs_list += [root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, local_end_pos, local_vel]
    # 1 + 6 + 3 + 3 + 114 + 57 + 12
    if has_shape_obs_disc:
        obs_list.append(shape_params)
    if has_limb_weight_obs:
        obs_list.append(limb_weight_params)
    obs = torch.cat(obs_list, dim=-1)
    
    return obs
```

```python
def _compute_observations(self, env_ids=None):
        if env_ids is None:
            env_ids = self.all_env_ids
        obs = self._compute_humanoid_obs(env_ids)

        self.obs_buf[env_ids] = obs

        return
```

```python
def _compute_amp_observations(self, env_ids=None):
        key_body_pos = self._rigid_body_pos[:, self._key_body_ids, :]
        key_body_vel = self._rigid_body_vel[:, self._key_body_ids, :]

        if self.humanoid_type in ["smpl", "smplh", "smplx"] and self.dof_subset is None:
            # ZL hack
            self._dof_pos[:, 9:12], self._dof_pos[:, 21:24], self._dof_pos[:, 51:54], self._dof_pos[:, 66:69] = 0, 0, 0, 0
            self._dof_vel[:, 9:12], self._dof_vel[:, 21:24], self._dof_vel[:, 51:54], self._dof_vel[:, 66:69] = 0, 0, 0, 0

        # if (key_body_pos[..., 2].mean(dim = -1) > 2).sum():
        #     self.humanoid_shapes[torch.where((key_body_pos[..
        # ., 2].mean(dim = -1) > 2))].cpu().numpy()
        #     import ipdb; ipdb.set_trace()
        #     print('bugg')
        # if flags.debug:
        # print(torch.topk(self._dof_pos.abs().sum(dim=-1), 5))

        if (env_ids is None):
            if self.humanoid_type in ["smpl", "smplh", "smplx"] :
                self._curr_amp_obs_buf[:] = self._compute_amp_observations_from_state(self._rigid_body_pos[:, 0, :], self._rigid_body_rot[:, 0, :], self._rigid_body_vel[:, 0, :], self._rigid_body_ang_vel[:, 0, :], self._dof_pos, self._dof_vel, key_body_pos, key_body_vel, self.humanoid_shapes, self.humanoid_limb_and_weights,
                                                                            self.dof_subset, self._local_root_obs, self._amp_root_height_obs, self._has_dof_subset, self._has_shape_obs_disc, self._has_limb_weight_obs_disc, self._has_upright_start)

            else:
                self._curr_amp_obs_buf[:] = build_amp_observations(self._rigid_body_pos[:, 0, :], self._rigid_body_rot[:, 0, :], self._rigid_body_vel[:, 0, :], self._rigid_body_ang_vel[:, 0, :], self._dof_pos, self._dof_vel, key_body_pos, self._local_root_obs, self._amp_root_height_obs,
                                                                   self._dof_obs_size, self._dof_offsets)
        else:
            if len(env_ids) == 0:
                return
            if self.humanoid_type in ["smpl", "smplh", "smplx"] :
                self._curr_amp_obs_buf[env_ids] = self._compute_amp_observations_from_state(self._rigid_body_pos[env_ids][:, 0, :], self._rigid_body_rot[env_ids][:, 0, :], self._rigid_body_vel[env_ids][:, 0, :], self._rigid_body_ang_vel[env_ids][:, 0, :], self._dof_pos[env_ids], self._dof_vel[env_ids],
                                                                                  key_body_pos[env_ids], key_body_vel[env_ids], self.humanoid_shapes[env_ids], self.humanoid_limb_and_weights[env_ids], sel
```

### phc/env/tasks/humanoid_amp_getup.py

```
class HumanoidAMPGetup(HumanoidAMP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def pre_physics_step(self, actions)
    def _generate_fall_states(self)
    def _reset_actors(self, env_ids)
    def _reset_recovery_episode(self, env_ids)
    def _reset_fall_episode(self, env_ids)
    def _reset_envs(self, env_ids)
    def _init_amp_obs(self, env_ids)
    def _update_recovery_count(self)
    def _compute_reset(self)
```

### phc/env/tasks/humanoid_amp_task.py

```
class HumanoidAMPTask(HumanoidAMP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def get_obs_size(self)
    def get_task_obs_size(self)
    def pre_physics_step(self, actions)
    def render(self, sync_frame_time)
    def _update_task(self)
    def _reset_envs(self, env_ids)
    def _reset_task(self, env_ids)
    def _compute_observations(self, env_ids)
    def _compute_task_obs(self, env_ids)
    def _compute_reward(self, actions)
    def _draw_task(self)

```python
def _compute_observations(self, env_ids=None):
        # env_ids is used for resetting
        if env_ids is None:
            env_ids = self.all_env_ids
        humanoid_obs = self._compute_humanoid_obs(env_ids)

        if (self._enable_task_obs):
            task_obs = self._compute_task_obs(env_ids)
            obs = torch.cat([humanoid_obs, task_obs], dim=-1)
        else:
            obs = humanoid_obs
        
            
        if self.cfg.env.get("add_noise", False):
            noise_scale = self.cfg.env.get("noise_scale", 0.01)
            obs += (2 * torch.rand_like(obs) - 1) * noise_scale
       
        self.obs_buf[env_ids] = obs

        return
```

```python
def _compute_reward(self, actions):
        return NotImplemented
```
```

### phc/env/tasks/humanoid_amp_z.py

```
class HumanoidAMPZ(HumanoidAMP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def step(self, actions)
    def _setup_character_props(self, key_bodies)
```

### phc/env/tasks/humanoid_grab.py

```
class HumanoidGrab(HumanoidAMPTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _create_smpl_humanoid_xml(self, num_humanoids, smpl_robot, queue, pid)
    def _load_motion(self, motion_train_file, motion_test_file)
    def get_task_obs_size(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _load_target_asset(self)
    def _build_target(self, env_id, env_ptr)
    def _build_target_tensors(self)
    def _reset_actors(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _reset_target(self, env_ids)
    def _sample_time(self, motion_ids)
    def _sample_ref_state(self, env_ids)
    def _compute_task_obs(self, env_ids)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _reset_ref_state_init(self, env_ids)
    def _update_cycle_count(self)
    def pre_physics_step(self, actions)
    def _build_termination_heights(self)
    def _draw_task(self)
    def _hack_output_motion_target(self)
class HumanoidGrabZ(HumanoidGrab)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def step(self, actions)
    def _setup_character_props(self, key_bodies)
def compute_grab_observations(root_pos, root_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright)
def compute_contact_force_obs(root_pos, root_rot, contact_forces_subset, upright)
def compute_grab_reward(root_pos, root_rot, obj_pos, obj_rot, obj_vel, obj_ang_vel, hand_contact_force, obj_contact_forces, ref_obj_pos, ref_obj_rot, ref_body_vel, ref_body_ang_vel, hand_pos, ref_hand_pos, rwd_specs)
def compute_humanoid_grab_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, obj_pos, obj_rot, ref_obj_pos, ref_obj_rot, hand_pos, pass_time, enable_early_termination, termination_distance, disableCollision, use_mean)

```python
def compute_grab_observations(root_pos, root_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding pose information at the back
    # Future tracks in this obs will not contain future diffs.
    obs = []
    B, J, _ = o_pos.shape
    if not upright:
        root_rot = remove_base_rot(root_rot)
    
    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    

    ##### Body position and rotation differences
    diff_global_body_pos = ref_o_pos.view(B, time_steps, J, 3) - o_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    diff_global_body_rot = torch_utils.quat_mul(ref_o_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(o_rot[:, None].repeat_interleave(time_steps, 1)))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### linear and angular  Velocity differences
    diff_global_vel = ref_o_vel.view(B, time_steps, J, 3) - o_lin_vel.view(B, 1, J, 3)
    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))


    diff_global_ang_vel = ref_o_ang_vel.view(B, time_steps, J, 3) - o_ang_vel.view(B, 1, J, 3)
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    

    ##### body pos + Dof_pos This part will have proper futuers.
    local_o_body_pos = o_pos.view(B, 1, J, 3) - root_pos.view(B, 1, 1, 3)  # preserves the body position
    local_o_body_pos = torch_utils.my_quat_rotate(heading_inv_rot.view(-1, 4), local_o_body_pos.view(-1, 3))

    local_o_body_rot = torch_utils.quat_mul(heading_inv_rot.view(-1, 4), o_rot.view(-1, 4))
    local_o_body_rot = torch_utils.quat_to_tan_norm(local_o_body_rot)

    # make some changes to how futures are appended.
    
    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * timestep * 24 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * timestep * 24 * 6
    obs.append(diff_local_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_pos.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_rot.view(B, -1))  # timestep  * 24 * 6
    
    obs = torch.cat(obs, dim=-1).view(B, -1)
    return obs
```

```python
def compute_grab_reward(root_pos, root_rot, obj_pos, obj_rot, obj_vel, obj_ang_vel, hand_contact_force, obj_contact_forces, ref_obj_pos, ref_obj_rot, ref_body_vel, ref_body_ang_vel, hand_pos, ref_hand_pos, rwd_specs):
     # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Dict[str, float]) -> Tuple[Tensor, Tensor]
    k_pos, k_rot, k_vel, k_ang_vel = rwd_specs["k_pos"], rwd_specs["k_rot"], rwd_specs["k_vel"], rwd_specs["k_ang_vel"]
    w_pos, w_rot, w_vel, w_ang_vel = rwd_specs["w_pos"], rwd_specs["w_rot"], rwd_specs["w_vel"], rwd_specs["w_ang_vel"]

    k_pos, k_rot, k_vel, k_ang_vel = 100, 10, 0.1, 0.1
    # w_pos, w_rot, w_vel, w_ang_vel = 0.4, 0.3, 0.05, 0.05
    w_pos, w_rot, w_vel, w_ang_vel = 0.25, 0.25, 0.05, 0.05
    # w_cos,  w_dist= 0.1, 0.1
    k_cos, k_dist = 50, 50
    # w_conctact, w_close = 0.2, 0
    w_conctact, w_close = 0.1, 0
    
    # object position tracking reward
    diff_global_body_pos = ref_obj_pos - obj_pos
    diff_body_pos_dist = (diff_global_body_pos**2).mean(dim=-1).mean(dim=-1)
    r_obj_pos = torch.exp(-k_pos * diff_body_pos_dist)

    # object rotation tracking reward
    diff_global_body_rot = torch_utils.quat_mul(ref_obj_rot, torch_utils.quat_conjugate(obj_rot))
    diff_global_body_angle = torch_utils.quat_to_angle_axis(diff_global_body_rot)[0]
    diff_global_body_angle_dist = (diff_global_body_angle**2).mean(dim=-1)
    r_obj_rot = torch.exp(-k_rot * diff_global_body_angle_dist)

    # object linear velocity tracking reward
    diff_global_vel = ref_body_vel - obj_vel
    diff_global_vel_dist = (diff_global_vel**2).mean(dim=-1).mean(dim=-1)
    r_lin_vel = torch.exp(-k_vel * diff_global_vel_dist)

    # object angular velocity tracking reward
    diff_global_ang_vel = ref_body_ang_vel - obj_ang_vel
    diff_global_ang_vel_dist = (diff_global_ang_vel**2).mean(dim=-1).mean(dim=-1)
    r_ang_vel = torch.exp(-k_ang_vel * diff_global_ang_vel_dist)

    obj_contact_force_sum = obj_contact_forces.sum(dim = -2).abs().sum(dim = -1) > 0
    hand_pos_diff = (hand_pos - obj_pos).norm(dim=-1, p = 2)
    
    table_no_contact = obj_contact_forces[:, -1].abs().sum(dim = -1) == 0 
    obj_has_contact = obj_contact_forces[:, 0].abs().sum(dim = -1) > 0 
    object_lifted = torch.logical_and(obj_has_contact, table_no_contact)
    
    pos_filter = (hand_pos_diff < 0.1).sum(dim = -1) > 0
    vel_filter = (torch.norm(obj_vel, dim= -1, p = 2) > 0.01)[:, 0]
    
    vel_filter = torch.logical_or(vel_filter, object_lifted) # velocity means the object is moved. The object lifted is for when the object is mid-air and stationary. 
    
    contact_filter = torch.logical_and(obj_contact_force_sum, torch.logical_and(pos_filter, vel_filter)) # 
    r_contact_lifted = contact_filter.float() 
    
    
    # print(vel_filter, contact_filter)
    
    # if contact_filter.sum() > 0:
        # import ipdb; ipdb.set_trace()

    # # r_close = torch.exp(-k_pos * (hand_pos_diff.min(dim = -1).values **2))

    # ##### pos_filter makes sure that no reward is given if the hand is too far from the object.
    # # reward = (w_pos * r_obj_pos + w_rot * r_obj_rot + w_vel * r_lin_vel + w_ang_vel * r_ang_vel) * contact_filter + r_contact_lifted * w_conctact  + r_close * w_close
    # reward = (w_pos * r_obj_pos + w_rot * r_obj_rot + w_vel * r_lin_vel + w_ang_vel * r_ang_vel) * contact_filter + r_contact_lifted * w_conctact  
    # # reward_raw = torch.stack([r_obj_pos, r_obj_rot, r_lin_vel, r_ang_vel, r_close], dim=-1)
    # reward_raw = torch.stack([r_obj_pos, r_obj_rot, r_lin_vel, r_ang_vel], dim=-1)

    w_cos,  w_dist= 0.15, 0.15
    k_cos, k_dist = 50, 50
    B, H, C = hand_pos.shape

    ref_hand_pos_diff = (ref_hand_pos - ref_obj_pos)
    hand_pos_diff = (hand_pos - obj_pos)
    ref_diff_norm = ref_hand_pos_diff.norm(dim = -1, keepdim = True, p = 2)
    hand_diff_norm = hand_pos_diff.norm(dim = -1, keepdim = True, p = 2)
    # pos_filter = (ref_hand_pos_dif
```

```python
def _compute_reward(self, actions):
        obj_pos = self._obj_states[..., 0:3]
        obj_rot = self._obj_states[..., 3:7]
        root_pos = self._humanoid_root_states[..., 0:3]
        root_rot = self._humanoid_root_states[..., 3:7]
        
        obj_pos = self._obj_states[..., None,   0:3]
        obj_rot = self._obj_states[...,  None,  3:7]
        obj_lin_vel = self._obj_states[..., None,  7:10]
        obj_ang_vel = self._obj_states[..., None,  10:13]
        obj_contact_forces = self._obj_contact_forces
        
        hand_pos = self._rigid_body_pos[:, self._grab_body_ids, :]
        
        motion_times = self.progress_buf * self.dt + self._motion_start_times 
        motion_res = self._get_state_from_motionlib_cache(self._sampled_motion_ids, motion_times, None) 
        
        ref_o_ang_vel, ref_o_lin_vel, ref_o_rb_rot, ref_o_rb_pos = motion_res['o_ang_vel'][:, :1], motion_res['o_lin_vel'][:, :1], motion_res['o_rb_rot'][:, :1], motion_res['o_rb_pos'][:, :1]
        

        body_pos = self._rigid_body_pos
        body_rot = self._rigid_body_rot
        body_vel = self._rigid_body_vel
        body_ang_vel = self._rigid_body_ang_vel
        ref_root_pos, ref_root_rot, ref_dof_pos, ref_root_vel, ref_root_ang_vel, ref_dof_vel, ref_smpl_params, ref_limb_weights, ref_pose_aa, ref_rb_pos, ref_rb_rot, ref_body_vel, ref_body_ang_vel = \
                motion_res["root_pos"], motion_res["root_rot"], motion_res["dof_pos"], motion_res["root_vel"], motion_res["root_ang_vel"], motion_res["dof_vel"], \
                motion_res["motion_bodies"], motion_res["motion_limb_weights"], motion_res["motion_aa"], motion_res["rg_pos"], motion_res["rb_rot"], motion_res["body_vel"], motion_res["body_ang_vel"]
        ref_hand_pos = ref_rb_pos[:, self._grab_body_ids, :]
        hand_contact_force = self._contact_forces[:, self._grab_body_ids, :]
        
        
        grab_reward, grab_reward_raw  = compute_grab_reward(root_pos, root_rot, obj_pos, obj_rot, obj_lin_vel, obj_ang_vel, hand_contact_force, obj_contact_forces, ref_o_rb_pos, ref_o_rb_rot, ref_o_lin_vel, ref_o_ang_vel, hand_pos, ref_hand_pos, self.reward_specs)
        if self.cfg.env.get("im_reward", False):
            im_reward, im_rewad_raw = humanoid_im.compute_imitation_reward(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_rb_pos, ref_rb_rot, ref_body_vel, ref_body_ang_vel, self.reward_specs_im)
            self.rew_buf[:], self.reward_raw = im_reward * 0.3 + grab_reward * 0.7, torch.cat([grab_reward_raw, im_rewad_raw], dim=-1)
        else:
            self.rew_buf[:], self.reward_raw =  grab_reward * 1, torch.cat([grab_reward_raw], dim=-1)
        return
```
```

### phc/env/tasks/humanoid_im.py

```
class HumanoidIm(HumanoidAMPTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def setup_kin_info(self)
    def pause_func(self, action)
    def next_func(self, action)
    def reset_func(self, action)
    def record_func(self, action)
    def hide_ref(self, action)
    def create_o3d_viewer(self)
    def render(self, sync_frame_time)
    def _load_motion(self, motion_train_file, motion_test_file)
    def resample_motions(self)
    def get_motion_lengths(self)
    def _record_states(self)
    def _write_states_to_file(self, file_name)
    def forward_motion_samples(self)
    def get_task_obs_size(self)
    def get_task_obs_size_detail(self)
    def _build_termination_heights(self)
    def init_root_points(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _load_marker_asset(self)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _update_marker(self)
    def _build_marker(self, env_id, env_ptr)
    def _build_marker_state_tensors(self)
    def _sample_time(self, motion_ids)
    def _reset_task(self, env_ids)
    def post_physics_step(self)
    def _compute_observations(self, env_ids)
    def _compute_task_obs(self, env_ids, save_buffer)
    def save_kin_buffer(self, env_ids, motion_res)
    def _compute_reward(self, actions)
    def _reset_ref_state_init(self, env_ids)
    def _get_state_from_motionlib_cache(self, motion_ids, motion_times, offset)
    def _sample_ref_state(self, env_ids)
    def _hack_motion_sync(self)
    def _update_cycle_count(self)
    def _update_occl_training(self)
    def _action_to_pd_targets(self, action)
    def step(self, actions)
    def update_kin_info(self)
    def pre_physics_step(self, actions)
    def _compute_reset(self)
    def _draw_task(self)
    def _build_im_obs_part_idex(self)
class HumanoidImZ(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def step(self, actions)
    def _setup_character_props(self, key_bodies)
def compute_imitation_observations(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v2(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, dof_pos, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, ref_dof_pos, time_steps, upright)
def compute_imitation_observations_v3(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v6(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v7(root_pos, root_rot, body_pos, body_vel, ref_body_pos, ref_body_vel, time_steps, upright)
def compute_imitation_observations_v8(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v9(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_root_vel, ref_body_root_ang_vel, time_steps, upright)
def compute_imitation_observations_v10(root_pos, root_rot, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_reward(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, rwd_specs)
def compute_point_goal_reward(prev_dist, curr_dist)
def compute_location_reward(root_pos, tar_pos)
def compute_humanoid_im_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, ref_body_pos, pass_time, enable_early_termination, termination_distance, disableCollision, use_mean)
def compute_location_observations(root_pos, root_rot, target_pos, upright)
def compute_humanoid_traj_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, pass_time, enable_early_termination, termination_heights, disableCollision)

```python
def compute_imitation_observations(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, int, bool) -> Tensor
    # We do not use any dof in observation.
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)

    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot).repeat_interleave(time_steps, 0).view(B, time_steps, J, 4))

    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis

    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * 10 * 3 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * 10 * 3 * 6

    ##### Velocities
    diff_global_vel = ref_body_vel.view(B, time_steps, J, 3) - body_vel.view(B, 1, J, 3)
    diff_global_ang_vel = ref_body_ang_vel.view(B, time_steps, J, 3) - body_ang_vel.view(B, 1, J, 3)

    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    obs.append(diff_local_vel.view(B, -1))  # 3 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # 3 * 3

    obs = torch.cat(obs, dim=-1)
    return obs
```

```python
def compute_imitation_observations_v2(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, dof_pos, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, ref_dof_pos, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding dof
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)

    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot).repeat_interleave(time_steps, 0).view(B, time_steps, J, 4))

    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis

    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * 10 * 3 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * 10 * 3 * 6

    ##### Velocities
    diff_global_vel = ref_body_vel.view(B, time_steps, J, 3) - body_vel.view(B, 1, J, 3)
    diff_global_ang_vel = ref_body_ang_vel.view(B, time_steps, J, 3) - body_ang_vel.view(B, 1, J, 3)

    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    obs.append(diff_local_vel.view(B, -1))  # 3 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # 3 * 3

    ##### Dof_pos diff
    diff_dof_pos = ref_dof_pos.view(B, time_steps, -1) - dof_pos.view(B, time_steps, -1)
    obs.append(diff_dof_pos.view(B, -1))  # 23 * 3

    obs = torch.cat(obs, dim=-1)
    return obs
```

```python
def compute_imitation_observations_v3(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, int, bool) -> Tensor
    # No velocities
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)

    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))
    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * 10 * 3 * 3

    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot).repeat_interleave(time_steps, 0).view(B, time_steps, J, 4))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * 10 * 3 * 6

    obs = torch.cat(obs, dim=-1)

    return obs
```

```python
def compute_imitation_observations_v6(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding pose information at the back
    # Future tracks in this obs will not contain future diffs.
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    

    ##### Body position and rotation differences
    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    body_rot[:, None].repeat_interleave(time_steps, 1)
    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot[:, None].repeat_interleave(time_steps, 1)))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### linear and angular  Velocity differences
    diff_global_vel = ref_body_vel.view(B, time_steps, J, 3) - body_
```

### phc/env/tasks/humanoid_im_demo.py

```
class HumanoidImDemo(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def talk(self)
    def _update_marker(self)
    def _reset_ref_state_init(self, env_ids)
    def _compute_observations(self, env_ids)
    def _compute_task_obs_demo(self, env_ids)

```python
def _compute_observations(self, env_ids=None):
        # env_ids is used for resetting
        if env_ids is None:
            env_ids = self.all_env_ids

        self_obs = self._compute_humanoid_obs(env_ids)
        self.self_obs_buf[env_ids] = self_obs

        if (self._enable_task_obs):
            task_obs = self._compute_task_obs_demo(env_ids)
            obs = torch.cat([self_obs, task_obs], dim=-1)
        else:
            obs = self_obs

        if self.obs_v == 4:
            # Double sub will return a copy.
            B, N = obs.shape
            sums = self.obs_buf[env_ids, 0:10].abs().sum(dim=1)
            zeros = sums == 0
            nonzero = ~zeros
            obs_slice = self.obs_buf[env_ids]
            obs_slice[zeros] = torch.tile(obs[zeros], (1, 5))
            obs_slice[nonzero] = torch.cat([obs_slice[nonzero, N:], obs[nonzero]], dim=-1)
            self.obs_buf[env_ids] = obs_slice
        else:
            self.obs_buf[env_ids] = obs
        return obs
```
```

### phc/env/tasks/humanoid_im_distill.py

```
class HumanoidImDistill(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def setup_kin_info(self)
    def load_pnn(self, pnn_ck)
    def load_moe_actor(self, checkpoint)
    def load_moe_composer(self, checkpoint)
    def step(self, actions)
```

### phc/env/tasks/humanoid_im_distill_getup.py

```
class HumanoidImDistillGetup(HumanoidImGetup, HumanoidImDistill)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
```

### phc/env/tasks/humanoid_im_getup.py

```
class HumanoidImGetup(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def update_getup_schedule(self, epoch_num, getup_udpate_epoch)
    def pre_physics_step(self, actions)
    def _generate_fall_states(self)
    def resample_motions(self)
    def _reset_actors(self, env_ids)
    def _reset_recovery_episode(self, env_ids)
    def _reset_fall_episode(self, env_ids)
    def _reset_envs(self, env_ids)
    def _init_amp_obs(self, env_ids)
    def _update_recovery_count(self)
    def _compute_reset(self)
```

### phc/env/tasks/humanoid_im_mcp.py

```
class HumanoidImMCP(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _setup_character_props(self, key_bodies)
    def get_task_obs_size_detail(self)
    def step(self, weights)
```

### phc/env/tasks/humanoid_im_mcp_demo.py

```
class HumanoidImMCPDemo(HumanoidImMCP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def talk(self)
    def _update_marker(self)
    def _compute_observations(self, env_ids)
    def _compute_task_obs_demo(self, env_ids)
    def _compute_reset(self)

```python
def _compute_observations(self, env_ids=None):
        # env_ids is used for resetting
        if env_ids is None:
            env_ids = self.all_env_ids

        self_obs = self._compute_humanoid_obs(env_ids)
        self.self_obs_buf[env_ids] = self_obs

        if (self._enable_task_obs):
            task_obs = self._compute_task_obs_demo(env_ids)
            obs = torch.cat([self_obs, task_obs], dim=-1)
        else:
            obs = self_obs

        if self.obs_v == 4:
            # Double sub will return a copy.
            B, N = obs.shape
            sums = self.obs_buf[env_ids, 0:10].abs().sum(dim=1)
            zeros = sums == 0
            nonzero = ~zeros
            obs_slice = self.obs_buf[env_ids]
            obs_slice[zeros] = torch.tile(obs[zeros], (1, 5))
            obs_slice[nonzero] = torch.cat([obs_slice[nonzero, N:], obs[nonzero]], dim=-1)
            self.obs_buf[env_ids] = obs_slice
        else:
            self.obs_buf[env_ids] = obs
        return obs
```
```

### phc/env/tasks/humanoid_im_mcp_getup.py

```
class HumanoidImMCPGetup(HumanoidImGetup, HumanoidImMCP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
```

### phc/env/tasks/humanoid_omnigrab.py

```
class HumanoidOmniGrab(HumanoidAMPTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _setup_tensors(self)
    def _create_smpl_humanoid_xml(self, num_humanoids, smpl_robot, queue, pid)
    def forward_motion_samples(self)
    def recreate_sim(self, failed_keys, epoch)
    def resample_motions(self)
    def _load_motion(self, motion_train_file, motion_test_file)
    def get_task_obs_size(self)
    def get_task_obs_size_detail(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _load_target_asset(self)
    def _build_target(self, env_id, env_ptr)
    def _build_target_tensors(self)
    def _reset_actors(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _reset_target(self, env_ids)
    def _sample_time(self, motion_ids)
    def _sample_ref_state(self, env_ids)
    def _compute_task_obs(self, env_ids)
    def get_running_mean_size(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _reset_ref_state_init(self, env_ids)
    def _update_cycle_count(self)
    def pre_physics_step(self, actions)
    def remove_table(self, env_ids)
    def post_physics_step(self)
    def _build_termination_heights(self)
    def _draw_task(self)
    def _hack_output_motion_target(self)
    def _penality_slippage(self)
class HumanoidOmniGrabZ(HumanoidOmniGrab)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def step(self, actions)
    def step_z(self, action_z)
    def _setup_character_props(self, key_bodies)
def compute_grab_observations(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright)
def compute_grab_observations_v1_4(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright)
def compute_grab_observations_v1_5(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright)
def compute_grab_observations_v2(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright)
def compute_grab_observations_v3(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright)
def compute_pregrasp_reward(root_pos, root_rot, hand_pos, hand_rot, hand_vel, hand_ang_vel, ref_hand_pos, ref_hand_rot, ref_hand_vel, ref_hand_ang_vel, ref_obj_pos, hand_pos_prev, close_distance, rwd_specs)
def compute_grab_reward(root_pos, root_rot, obj_pos, obj_rot, obj_vel, obj_ang_vel, hand_contact_force, obj_contact_forces, ref_obj_pos, ref_obj_rot, ref_body_vel, ref_body_ang_vel, hand_pos, ref_hand_pos, rwd_specs)
def compute_humanoid_grab_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, obj_pos, obj_rot, ref_obj_pos, ref_obj_rot, hand_pos, pass_time, enable_early_termination, termination_distance, disableCollision, check_rot_reset)
def compute_contact_force_obs(root_pos, root_rot, contact_forces_subset, upright)

```python
def compute_grab_observations(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding pose information at the back
    # Future tracks in this obs will not contain future diffs.
    obs = []
    B, J, _ = o_pos.shape
    if not upright:
        root_rot = remove_base_rot(root_rot)
    
    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    

    ##### Body position and rotation differences
    diff_global_body_pos = ref_o_pos.view(B, time_steps, J, 3) - o_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    diff_global_body_rot = torch_utils.quat_mul(ref_o_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(o_rot[:, None]).repeat_interleave(time_steps, 1))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### linear and angular  Velocity differences
    diff_global_vel = ref_o_vel.view(B, time_steps, J, 3) - o_lin_vel.view(B, 1, J, 3)
    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))


    diff_global_ang_vel = ref_o_ang_vel.view(B, time_steps, J, 3) - o_ang_vel.view(B, 1, J, 3)
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    
    ##### Object position and rotation in body frame
    local_o_body_pos = o_pos.view(B, 1, J, 3) - root_pos.view(B, 1, 1, 3)  # preserves the body position
    local_o_body_pos = torch_utils.my_quat_rotate(heading_inv_rot.view(-1, 4), local_o_body_pos.view(-1, 3))

    local_o_body_rot = torch_utils.quat_mul(heading_inv_rot.view(-1, 4), o_rot.view(-1, 4))
    local_o_body_rot = torch_utils.quat_to_tan_norm(local_o_body_rot)


    B, J_f, _ = fingertip_pos.shape
    diff_global_finger_to_obj_pos = fingertip_pos - o_pos
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J_f, 1))
    local_finger_to_obj_pos = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_finger_to_obj_pos.view(-1, 3))

    
    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * timestep * 24 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * timestep * 24 * 6
    obs.append(diff_local_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_pos.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_rot.view(B, -1))  # timestep  * 24 * 6
    obs.append(local_finger_to_obj_pos.view(B, -1))  # 10 * 3
    
    obs = torch.cat(obs, dim=-1).view(B, -1)
    return obs
```

```python
def compute_grab_observations_v1_4(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # No hand object relative position information. 
    obs = []
    B, J, _ = o_pos.shape
    if not upright:
        root_rot = remove_base_rot(root_rot)
    
    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    

    ##### Body position and rotation differences
    diff_global_body_pos = ref_o_pos.view(B, time_steps, J, 3) - o_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    diff_global_body_rot = torch_utils.quat_mul(ref_o_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(o_rot[:, None]).repeat_interleave(time_steps, 1))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### linear and angular  Velocity differences
    diff_global_vel = ref_o_vel.view(B, time_steps, J, 3) - o_lin_vel.view(B, 1, J, 3)
    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))


    diff_global_ang_vel = ref_o_ang_vel.view(B, time_steps, J, 3) - o_ang_vel.view(B, 1, J, 3)
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    
    ##### Object position and rotation in body frame
    local_o_body_pos = o_pos.view(B, 1, J, 3) - root_pos.view(B, 1, 1, 3)  # preserves the body position
    local_o_body_pos = torch_utils.my_quat_rotate(heading_inv_rot.view(-1, 4), local_o_body_pos.view(-1, 3))

    local_o_body_rot = torch_utils.quat_mul(heading_inv_rot.view(-1, 4), o_rot.view(-1, 4))
    local_o_body_rot = torch_utils.quat_to_tan_norm(local_o_body_rot)
    
    
    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * timestep * 24 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * timestep * 24 * 6
    obs.append(diff_local_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_pos.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_rot.view(B, -1))  # timestep  * 24 * 6
    
    obs = torch.cat(obs, dim=-1).view(B, -1)
    return obs
```

```python
def compute_grab_observations_v1_5(root_pos, root_rot, fingertip_pos, fingertip_rot, o_pos, o_rot, o_lin_vel, o_ang_vel, ref_o_pos, ref_o_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding pose information at the back
    # Future tracks in this obs will not contain future diffs.
    obs = []
    B, J, _ = o_pos.shape
    if not upright:
        root_rot = remove_base_rot(root_rot)
    
    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    
    ##### Body position and rotation differences
    diff_global_body_pos = ref_o_pos.view(B, time_steps, J, 3) - root_pos.view(B, 1, J, 3) # Object future trajectory, in the body frame. 
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    diff_global_body_rot = torch_utils.quat_mul(ref_o_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(root_rot[:, None, None]).repeat_interleave(time_steps, 1))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### reference linear and angular Velocity 
    local_obj_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), ref_o_vel.view(-1, 3))

    local_obj_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), ref_o_ang_vel.view(-1, 3))
    
    ##### Object position and rotation in body frame
    local_o_body_pos = o_pos.view(B, 1, J, 3) - root_pos.view(B, 1, 1, 3)  # preserves the body position
    local_o_body_pos = torch_utils.my_quat_rotate(heading_inv_rot.view(-1, 4), local_o_body_pos.view(-1, 3))

    local_o_body_rot = torch_utils.quat_mul(heading_inv_rot.view(-1, 4), o_rot.view(-1, 4))
    local_o_body_rot = torch_utils.quat_to_tan_norm(local_o_body_rot)


    B, J_f, _ = fingertip_pos.shape
    diff_global_finger_to_obj_pos = fingertip_pos - o_pos
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J_f
```

### phc/env/tasks/humanoid_omnigrasp.py

```
class HumanoidOmniGrasp(HumanoidAMPTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _setup_tensors(self)
    def _build_traj_generator(self)
    def _create_smpl_humanoid_xml(self, num_humanoids, smpl_robot, queue, pid)
    def forward_motion_samples(self)
    def recreate_sim(self, failed_keys, epoch)
    def resample_motions(self)
    def _load_motion(self, motion_train_file, motion_test_file)
    def get_task_obs_size(self)
    def get_task_obs_size_detail(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _load_target_asset(self)
    def _build_target(self, env_id, env_ptr)
    def _build_target_tensors(self)
    def _reset_actors(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _reset_target(self, env_ids)
    def _sample_time(self, motion_ids)
    def _sample_ref_state(self, env_ids)
    def _compute_task_obs(self, env_ids)
    def get_running_mean_size(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _reset_ref_state_init(self, env_ids)
    def _update_cycle_count(self)
    def remove_table(self, env_ids)
    def debug_obj_pose(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _build_termination_heights(self)
    def _draw_task(self)
    def _hack_output_motion_target(self)
    def _penality_slippage(self)
    def _penality_stumble(self)
    def _reward_feet_air_time(self)
    def render(self, sync_frame_time)
class HumanoidOmniGraspZ(HumanoidOmniGrasp)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def step(self, actions)
    def step_z(self, action_z)
    def _setup_character_props(self, key_bodies)
    def _compute_reward(self, actions)
def compute_grab_observations(root_pos, root_rot, fingertip_pos, fingertip_rot, obj_pos, obj_rot, o_lin_vel, o_ang_vel, ref_obj_pos, ref_obj_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright)
def compute_pregrasp_reward_time(root_pos, root_rot, hand_pos, hand_rot, hand_vel, hand_ang_vel, ref_hand_pos, ref_hand_rot, ref_hand_vel, ref_hand_ang_vel, ref_obj_pos, hand_pos_prev, close_distance, rwd_specs)
def check_contact(hand_contact_force, obj_contact_forces, hand_pos, obj_pos, obj_vel, table_removed, close_distance_contact)
def compute_grab_reward(root_pos, root_rot, obj_pos, obj_rot, obj_vel, obj_ang_vel, ref_obj_pos, ref_obj_rot, ref_body_vel, ref_body_ang_vel, contact_filter, rwd_specs)
def compute_humanoid_grab_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, obj_pos, obj_rot, ref_obj_pos, ref_obj_rot, hand_pos, pass_time, enable_early_termination, termination_distance, disableCollision, check_rot_reset)
def compute_contact_force_obs(root_pos, root_rot, contact_forces_subset, upright)

```python
def compute_grab_observations(root_pos, root_rot, fingertip_pos, fingertip_rot, obj_pos, obj_rot, o_lin_vel, o_ang_vel, ref_obj_pos, ref_obj_rot, ref_o_vel, ref_o_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding pose information at the back
    # Future tracks in this obs will not contain future diffs.
    obs = []
    B, J, _ = obj_pos.shape
    if not upright:
        root_rot = remove_base_rot(root_rot)
    
    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, J, 1)).repeat_interleave(time_steps, 0)
    

    ##### Body position and rotation differences
    diff_global_body_pos = ref_obj_pos.view(B, time_steps, J, 3) - obj_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    diff_global_body_rot = torch_utils.quat_mul(ref_obj_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(obj_rot[:, None]).repeat_interleave(time_steps, 1))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### linear and angular  Velocity differences
    diff_global_vel = ref_o_vel.view(B, time_steps, J, 3) - o_lin_vel.view(B, 1, J, 3)
    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))


    diff_global_ang_vel = ref_o_ang_vel.view(B, time_steps, J, 3) - o_ang_vel.view(B, 1, J, 3)
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    
    ##### Object position and rotation in body frame
    local_o_body_pos = obj_pos.view(B, 1, J, 3) - root_pos.view(B, 1, 1, 3)  # preserves the body position
    local_o_body_pos = torch_utils.my_quat_rotate(heading_inv_rot.view(-1, 4), local_o_body_pos.view(-1, 3))

    local_o_body_rot = torch_utils.quat_mul(heading_inv_rot.view(-1, 4), obj_rot.view(-1, 4))
    local_o_body_rot = torch_utils.quat_to_tan_norm(local_o_body_rot)


    B, J_f, _ = fingertip_pos.shape
    diff_global_finger_to_obj_pos = fingertip_pos - obj_pos
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, J_f, 1))
    local_finger_to_obj_pos = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_finger_to_obj_pos.view(-1, 3))

    
    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * timestep * 24 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * timestep * 24 * 6
    obs.append(diff_local_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_pos.view(B, -1))  # timestep  * 24 * 3
    obs.append(local_o_body_rot.view(B, -1))  # timestep  * 24 * 6
    obs.append(local_finger_to_obj_pos.view(B, -1))  # 10 * 3
    
    obs = torch.cat(obs, dim=-1).view(B, -1)
    return obs
```

```python
def compute_pregrasp_reward_time(root_pos, root_rot, hand_pos, hand_rot, hand_vel, hand_ang_vel, ref_hand_pos, ref_hand_rot, ref_hand_vel, ref_hand_ang_vel, ref_obj_pos, hand_pos_prev, close_distance, rwd_specs):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, Tensor, Tensor, float, Dict[str, float]) -> Tuple[Tensor, Tensor]
    k_pos, k_rot, k_vel, k_ang_vel = rwd_specs["k_pos"], rwd_specs["k_rot"], rwd_specs["k_vel"], rwd_specs["k_ang_vel"]
    w_pos, w_rot, w_vel, w_ang_vel = rwd_specs["w_pos"], rwd_specs["w_rot"], rwd_specs["w_vel"], rwd_specs["w_ang_vel"]
    w_pos, w_rot = 0.9, 0.1
    
    # body position reward
    diff_hand_to_object = torch.norm(ref_hand_pos - ref_obj_pos, dim = -1, p = 2)
    close_hand_flag = diff_hand_to_object < close_distance # This flag decides whether the reference hand should be used in computing the pregrasp reward; is it close? 

    prev_dist = torch.norm(hand_pos_prev - ref_hand_pos, dim=-1, p = 2)
    curr_dist = torch.norm(hand_pos - ref_hand_pos, dim=-1, p = 2)
    prev_dist[~close_hand_flag] = 0
    curr_dist[~close_hand_flag] = 0
    distance_filter = curr_dist.sum(dim = -1)/close_hand_flag.sum(dim=-1) > close_distance # distance filter computes whether the hand is close to reference hand pose. If not close enough, it will be replaced with the "getting closer" reward. 
    
    closer_to_hand_r = torch.clamp(prev_dist - curr_dist, min=0, max=1/10).sum(dim=-1)/close_hand_flag.sum(dim=-1)   # cap max at 1/10, encourage the hand that is close enough in referect to get closer to the reference
    
    # Hand position reward
    diff_global_body_pos = ref_hand_pos - hand_pos
    distance = (diff_global_body_pos**2).mean(dim=-1)
    distance[~close_hand_flag] = 0
    diff_body_pos_dist = distance.sum(dim=-1)/close_hand_flag.sum(dim=-1)
    r_body_pos = torch.exp(-k_pos * diff_body_pos_dist)

    # hand rotation reward
    diff_global_body_rot = torch_utils.quat_mul(ref_hand_rot, torch_utils.quat_conjugate(hand_rot))
    diff_global_body_angle = torch_utils.quat_to_angle_axis(diff_global_body_rot)[0]
    diff_global_body_angle[~close_hand_flag] = 0
    diff_global_body_angle_dist = (diff_global_body_angle**2).sum(dim=-1)/close_hand_flag.sum(dim=-1)
    r_body_rot = torch.exp(-k_rot * diff_global_body_angle_dist)

    r_body_pos[distance_filter] = closer_to_hand_r[distance_filter]
    r_body_rot[distance_filter] = closer_to_hand_r[distance_filter]
    
    reward = w_pos * r_body_pos + w_rot * r_body_rot 
    reward_raw = torch.stack([r_body_pos, r_body_rot], dim=-1)
    
    return reward, reward_raw
```

```python
def compute_grab_reward(root_pos, root_rot, obj_pos, obj_rot, obj_vel, obj_ang_vel,  ref_obj_pos, ref_obj_rot, ref_body_vel, ref_body_ang_vel, contact_filter, rwd_specs):
     # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor,Tensor, Tensor, Tensor, Tensor, Dict[str, float]) -> Tuple[Tensor, Tensor]
    k_pos, k_rot, k_vel, k_ang_vel = rwd_specs["k_pos"], rwd_specs["k_rot"], rwd_specs["k_vel"], rwd_specs["k_ang_vel"]
    w_pos, w_rot, w_vel, w_ang_vel, w_conctact = rwd_specs["w_pos"], rwd_specs["w_rot"], rwd_specs["w_vel"], rwd_specs["w_ang_vel"], rwd_specs["w_conctact"]

    # object position tracking reward
    diff_global_body_pos = ref_obj_pos - obj_pos
    diff_body_pos_dist = (diff_global_body_pos**2).mean(dim=-1).mean(dim=-1)
    r_obj_pos = torch.exp(-k_pos * diff_body_pos_dist)

    # object rotation tracking reward
    diff_global_body_rot = torch_utils.quat_mul(ref_obj_rot, torch_utils.quat_conjugate(obj_rot))
    diff_global_body_angle = torch_utils.quat_to_angle_axis(diff_global_body_rot)[0]
    diff_global_body_angle_dist = (diff_global_body_angle**2).mean(dim=-1)
    r_obj_rot = torch.exp(-k_rot * diff_global_body_angle_dist)

    # object linear velocity tracking reward
    diff_global_vel = ref_body_vel - obj_vel
    diff_global_vel_dist = (diff_global_vel**2).mean(dim=-1).mean(dim=-1)
    r_lin_vel = torch.exp(-k_vel * diff_global_vel_dist)

    # object angular velocity tracking reward
    diff_global_ang_vel = ref_body_ang_vel - obj_ang_vel
    diff_global_ang_vel_dist = (diff_global_ang_vel**2).mean(dim=-1).mean(dim=-1)
    r_ang_vel = torch.exp(-k_ang_vel * diff_global_ang_vel_dist)

    r_contact_lifted = contact_filter.float() 

    # # r_close = torch.exp(-k_pos * (hand_pos_diff.min(dim = -1).values **2))

    # ##### pos_filter makes sure that no reward is given if the hand is too far from the object.
    # # reward = (w_pos * r_obj_pos + w_rot * r_obj_rot + w_vel * r_lin_vel + w_ang_vel * r_ang_vel) * contact_filter + r_contact_lifted * w_conctact  + r_close * w_close
    reward = (w_pos * r_obj_pos + w_rot * r_obj_rot + w_vel * r_lin_vel + w_ang_vel * r_ang_vel) * contact_filter + r_contact_lifted * w_conctact  
    # # reward_raw = torch.stack([r_obj_pos, r_obj_rot, r_lin_vel, r_ang_vel, r_close], dim=-1)
    reward_raw = torch.stack([r_obj_pos, r_obj_rot, r_lin_vel, r_ang_vel], dim=-1)
    
    # np.set_printoptions(precision=4, suppress=1)
    # print(reward_raw.detach().numpy())
    
    return reward, reward_raw
```

```python
def _compute_reward(self, actions):
        obj_pos = self._obj_states[..., 0:3]
        obj_rot = self._obj_states[..., 3:7]
        root_pos = self._humanoid_root_states[..., 0:3]
        root_rot = self._humanoid_root_states[..., 3:7]
        
        obj_pos = self._obj_states[..., None,   0:3]
        obj_rot = self._obj_states[...,  None,  3:7]
        obj_lin_vel = self._obj_states[..., None,  7:10]
        obj_ang_vel = self._obj_states[..., None,  10:13]
        obj_contact_forces = self._obj_contact_forces
        
        hand_pos = self._rigid_body_pos[:, self._hand_body_ids, :]
        hand_rot 
```

### phc/env/tasks/humanoid_z.py

```
class HumanoidZ(Humanoid)
    def initialize_z_models(self)
    def _setup_character_props_z(self)
    def get_task_obs_size_detail_z(self)
    def compute_z_actions(self, action_z)
    def step_z(self, action_z)
```

### phc/env/tasks/vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class VecTaskCPU(VecTask)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations)
    def step(self, actions)
    def reset(self)
class VecTaskGPU(VecTask)
    def __init__(self, task, rl_device, clip_observations)
    def step(self, actions)
    def reset(self)
class VecTaskPython(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### phc/env/tasks/vec_task_wrappers.py

```
class VecTaskCPUWrapper(VecTaskCPU)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations)
class VecTaskGPUWrapper(VecTaskGPU)
    def __init__(self, task, rl_device, clip_observations)
class VecTaskPythonWrapper(VecTaskPython)
    def __init__(self, task, rl_device, clip_observations)
    def reset(self, env_ids)
    def amp_observation_space(self)
    def enc_amp_observation_space(self)
    def fetch_amp_obs_demo(self, num_samples)
    def enc_amp_observation_space(self)
    def fetch_amp_obs_demo_pair(self, num_samples)
    def fetch_amp_obs_demo_enc_pair(self, num_samples)
    def fetch_amp_obs_demo_per_id(self, num_samples, motion_ids)

```python
def amp_observation_space(self):
        return self._amp_obs_space
```

```python
def enc_amp_observation_space(self):
        return self._enc_amp_obs_space
```

```python
def enc_amp_observation_space(self):
        return self._enc_amp_obs_space
```
```

### phc/env/util/gym_util.py

```
def setup_gym_viewer(config)
def initialize_gym(config)
def configure_gym(gym, config)
def parse_states_from_reference_states(reference_states, progress)
def parse_states_from_reference_states_with_motion_id(precomputed_state, progress, motion_id)
def parse_dof_state_with_motion_id(precomputed_state, dof_state, progress, motion_id)
def get_flatten_ids(precomputed_state)
def parse_states_from_reference_states_with_global_id(precomputed_state, global_id)
def get_robot_states_from_torch_tensor(config, ts, global_quats, vels, avels, init_rot, progress, motion_length, actions, relative_rot, motion_id, num_motion, motion_onehot_matrix)
def get_xyzoffset(start_ts, end_ts, root_yaw_inv)
```

### phc/learning/task_agent.py

```
def load_my_state_dict(target, saved_dict)
class TaskAgent(CommonAgent)
    def __init__(self, base_name, config)
```

### phc/learning/task_models.py

```
class ModelTaskContinuous(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### phc/utils/config.py

```
def set_np_formatting()
def warn_task_name()
def set_seed(seed, torch_deterministic)
def load_cfg(args)
def parse_sim_params(args, cfg, cfg_train)
def get_args(benchmark)
```

### phc/utils/parse_task.py

```
def warn_task_name()
def parse_task(args, cfg, cfg_train, sim_params)
```

### scripts/vis/test_sim.py

```
"""Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.

NVIDIA CORPORATION and its licensors retain all intellectual property
and proprietary rights in and to this software, related documentation
and any modifications thereto. Any use, reproduction, disclosure or
distribution of this software and related documentation without an express
license agreement from NVIDIA CORPORATION is strictly prohibited.

Visualize motion library"""
def clamp(x, min_value, max_value)
class AssetDesc()
    def __init__(self, file_name, flip_visual_attachments)
```