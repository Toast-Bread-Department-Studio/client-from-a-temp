# coding: utf-8
import subprocess
import threading
import wget

import eel
import sys
import os
import json
import time
import hmac
import hashlib
import base64
import urllib
import urllib.parse
import requests
from util import *

secret_key = 'Tritium0041'
aes_Key = 'ECWOhQRHulelarhrlLa+BfDQrTECNCr6'
url = "https://tritium.work:5000/"


@eel.expose
def hello():
    print('hello')


# 登录函数
@eel.expose
def signin(username, password):
    print("接收到登录请求")
    print(username, password)
    content = {'username': username, 'password': password}
    # 生成请求体
    content = json.dumps(content)
    # 生成请求头
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 发送请求
    target = url + "signin"
    response = requests.post(url=target, headers=headers, data=content, verify=False)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        print('登录成功')
        return response['token']
    else:
        return 403


@eel.expose
def get_user_info(token):
    content = {'token': token}
    # 生成请求头
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 发送请求
    target = url + "userinfo"
    content = json.dumps(content)
    response = requests.post(url=target, headers=headers, data=content, verify=False)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        return response['result'], response['username']
    else:
        return 403


@eel.expose
def check_config():
    isConfigExist = searchConfig()
    if isConfigExist == 2:
        return 2
    elif isConfigExist == 1:
        return 1
    else:
        return 0


@eel.expose
def createConfig(vram_choice):
    args_ok = ""
    # 创建配置文件
    vram_choice = str(vram_choice)
    if vram_choice == "1":
        args_ok += "--lowvram "
    elif vram_choice == "2":
        args_ok += "--medvram "
    elif vram_choice == "3":
        pass
    args_choice = "26"
    arg_dic = {
        "1": "--deepdanbooru ",
        "2": "--xformers ",
        "3": "--precision full --no-half ",
        "4": "--no-half-vae ",
        "5": "--listen ",
        "6": "--api ",
        "7": "--disable-safe-unpickle "
    }
    for c in args_choice:
        if c in arg_dic:
            args_ok += arg_dic[c]
    end(args_ok)

@eel.expose
def run_webui():
    subprocess.Popen("boot.bat")
    return 1

@eel.expose
def checkmodels():
    localmodels =requests.get("http://127.0.0.1:7860/sdapi/v1/sd-models").json()
    localmodelsHash = [i["hash"] for i in localmodels]
    print(localmodelsHash)
    remoteModels = requests.get("https://tritium.work:5000/checkList",verify=False).json()["models"]
    for i in localmodelsHash[::]:
        #检测是否存在于remoteModels的key中
        if i in remoteModels.keys():
            remoteModels.pop(i)
    print(remoteModels)
    for i in remoteModels:
        Downurl = remoteModels[i]
        r = requests.get(Downurl,verify=False,stream=True,allow_redirects=True)
        #从连接获取文件名
        with open("./models/Stable-diffusion/"+Downurl.split("/")[-1],"wb") as f:
            f.write(r.content)
            f.close()
    return 1



@eel.expose
def croissantNetwork(token):
    response = claim_task(token)
    task_num = response['task_num']
    task_detail = response['task_detail']
    task_name = response['task_name']







if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({"port": 3000}, host="localhost", port=8888, mode="chrome")
    else:
        eel.init('build')
        eel.start({"port": 8888},host="localhost", port=8888,mode="edge")

