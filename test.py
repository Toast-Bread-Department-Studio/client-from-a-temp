import requests
from util import *
import json

token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJUcml0aXVtIiwiZXhwIjoxNjc5ODQzNTQyLCJpYXQiOjE2Nzk3NTcxNDIsImRhdGEiOnsidXNlcm5hbWUiOiJ0ZXN0MSJ9fQ.dU2R9Q7GC4_x8O7gfHU40iEpimeOA02QpMd3zieckQA"


res = claim_task(token)
param = res["task_detail"]
task_name = res['task_name']
task_num = res['task_num']
param["batch_size"] = task_num

res = requests.post("http://127.0.0.1:7860/sdapi/v1/txt2img", json=param).json()

submit = submit_task(token, task_name, task_num, res['images'])
print(submit)
