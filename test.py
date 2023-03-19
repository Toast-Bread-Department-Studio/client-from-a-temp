import requests
from util import *

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJUcml0aXVtIiwiZXhwIjoxNjc5Mjg2MjEyLCJpYXQiOjE2NzkxOTk4MTIsImRhdGEiOnsidXNlcm5hbWUiOiJ0ZXN0MSJ9fQ.9N9MiMpJRqfX2yYrEOxdmX-7iMF8pQ-dQ5e8QjCfitM"


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


res = claim_task(token)
task_detail = res['task_detail']
task_num = res['task_num']
task_name = res['task_name']
# model = task_detail['model']
param = {
    "prompt": task_detail['Prompts'],
    "negative_prompt": task_detail['NPrompts'],
    "num": task_num
}

payload = {
    "enable_hr": False,
    "prompt": param['prompt'],
    "styles": [],
    "seed": -1,
    "subseed": -1,
    "subseed_strength": 0,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "sampler_name": "Euler a",
    "batch_size": param['num'],
    "n_iter": 1,
    "steps": 30,
    "cfg_scale": 7,
    "width": 512,
    "height": 512,
    "restore_faces": False,
    "tiling": False,
    "negative_prompt": param['negative_prompt'],
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

res = requests.post("http://127.0.0.1:7860/sdapi/v1/txt2img", json=payload).json()

submit = submit_task(token, task_name, task_num, res['images'])
print(submit)
