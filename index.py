# coding: utf-8
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
    response = requests.post(url=target, headers=headers,data=content,verify=False)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        return response['result'],response['username']
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


if __name__ == '__main__':
    if sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({"port": 3000}, host="localhost", port=8888)
    else:
        eel.init('build')
        eel.start('index.html')
