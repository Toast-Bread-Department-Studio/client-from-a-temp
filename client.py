import requests
from util import *
import eel

# 向本地api发送作画请求
def txt2img(params: dict):
    target = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    task = json.dumps(params)
    seed = int(params['seed'])
    enable_hr = bool(params['enable_hr'])
    denoising_strength = int(params['denoising_strength'])
    firstphase_width = int(params['firstphase_width'])
    firstphase_height = int(params['firstphase_height'])
    hr_scale = int(params['hr_scale'])
    hr_upscaler = str(params['hr_upscaler'])
    hr_second_pass_steps = int(params['hr_second_pass_steps'])
    hr_resize_x = int(params['hr_resize_x'])
    hr_resize_y = int(params['hr_resize_y'])
    prompt = str(params['prompt'])
    seed = int(params['seed'])
    subseed = int(params['subseed'])
    subseed_strength = int(params['subseed_strength'])
    seed_resize_from_h = int(params['seed_resize_from_h'])
    seed_resize_from_w = int(params['seed_resize_from_w'])
    sampler_name = str(params['sampler_name'])
    batch_size = int(params['batch_size'])
    n_iter = int(params['n_iter'])
    steps = int(params['steps'])
    cfg_scale = int(params['cfg_scale'])
    restore_faces = bool(params['restore_faces'])
    tiling = bool(params['tiling'])
    negative_prompt = str(params['negative_prompt'])

    payload = {
        "enable_hr": enable_hr,
        "denoising_strength": denoising_strength,
        "firstphase_width": firstphase_width,
        "firstphase_height": firstphase_height,
        "hr_scale": hr_scale,
        "hr_upscaler": hr_upscaler,
        "hr_second_pass_steps": hr_second_pass_steps,
        "hr_resize_x": hr_resize_x,
        "hr_resize_y": hr_resize_y,
        "prompt": prompt,
        "styles": [],
        "seed": seed,
        "subseed": subseed,
        "subseed_strength": subseed_strength,
        "seed_resize_from_h": seed_resize_from_h,
        "seed_resize_from_w": seed_resize_from_w,
        "sampler_name": sampler_name,
        "batch_size": batch_size,
        "n_iter": n_iter,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "width": 512,
        "height": 512,
        "restore_faces": restore_faces,
        "tiling": tiling,
        "negative_prompt": negative_prompt,
        "eta": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
        "override_settings": {},
        "override_settings_restore_afterwards": True,
        "script_args": [],
        "sampler_index": "Euler",
    }
    r = requests.post(target, json=payload).json()
    return r








def CNtxt2img(params: dict):
    target = "http://127.0.0.1:7860/controlnet/txt2img"
    task = json.dumps(params)
    seed = int(params['seed'])
    enable_hr = bool(params['enable_hr'])
    denoising_strength = int(params['denoising_strength'])
    firstphase_width = int(params['firstphase_width'])
    firstphase_height = int(params['firstphase_height'])
    hr_scale = int(params['hr_scale'])
    hr_upscaler = str(params['hr_upscaler'])
    hr_second_pass_steps = int(params['hr_second_pass_steps'])
    hr_resize_x = int(params['hr_resize_x'])
    hr_resize_y = int(params['hr_resize_y'])
    prompt = str(params['prompt'])
    seed = int(params['seed'])
    subseed = int(params['subseed'])
    subseed_strength = int(params['subseed_strength'])
    seed_resize_from_h = int(params['seed_resize_from_h'])
    seed_resize_from_w = int(params['seed_resize_from_w'])
    sampler_name = str(params['sampler_name'])
    batch_size = int(params['batch_size'])
    n_iter = int(params['n_iter'])
    steps = int(params['steps'])
    cfg_scale = int(params['cfg_scale'])
    restore_faces = bool(params['restore_faces'])
    tiling = bool(params['tiling'])
    negative_prompt = str(params['negative_prompt'])

    payload = {
        "enable_hr": enable_hr,
        "denoising_strength": denoising_strength,
        "firstphase_width": firstphase_width,
        "firstphase_height": firstphase_height,
        "hr_scale": hr_scale,
        "hr_upscaler": hr_upscaler,
        "hr_second_pass_steps": hr_second_pass_steps,
        "hr_resize_x": hr_resize_x,
        "hr_resize_y": hr_resize_y,
        "prompt": prompt,
        "styles": [],
        "seed": seed,
        "subseed": subseed,
        "subseed_strength": subseed_strength,
        "seed_resize_from_h": seed_resize_from_h,
        "seed_resize_from_w": seed_resize_from_w,
        "sampler_name": sampler_name,
        "batch_size": batch_size,
        "n_iter": n_iter,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "width": 512,
        "height": 512,
        "restore_faces": restore_faces,
        "tiling": tiling,
        "negative_prompt": negative_prompt,
        "eta": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
        "override_settings": {},
        "override_settings_restore_afterwards": True,
        "script_args": [],
        "sampler_index": "Euler",
        "controlnet_units": [
            {
                "input_image": "",
                "mask": "",
                "module": "none",
                "model": "None",
                "weight": 1,
                "resize_mode": "Scale to Fit (Inner Fit)",
                "lowvram": False,
                "processor_res": 64,
                "threshold_a": 64,
                "threshold_b": 64,
                "guidance": 1,
                "guidance_start": 0,
                "guidance_end": 1,
                "guessmode": True
            }
        ]
    }
    # 设置payload




if __name__ == '__main__':
    eel.init('web')
    eel.start('/Login/index.js', size=(800, 600))
