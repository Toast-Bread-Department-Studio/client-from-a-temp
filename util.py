import os
import json
import time
import hmac
import hashlib
import base64
import urllib
import urllib.parse

import requests

secret_key = 'Tritium0041'
aes_Key = 'ECWOhQRHulelarhrlLa+BfDQrTECNCr6'
url = "https://tritium.work:5000/"

def get_model_list():
    target = url + "checkList"
    res = requests.get(url=target).json
    return res




def searchConfig():
    # 检测当前目录下有无指定文件
    if os.path.exists('launch.py'):
        if os.path.exists('boot.bat'):
            return 0
        else:
            return 1
    else:
        return 2


def end(args_ok):
    bat_content = '''@echo off
    set TRANSFORMERS_CACHE=.cache\\huggingface\\transformers
    set XDG_CACHE_HOME=.cache
    set MATPLOTLIBRC=.cache

    set GIT=git\\bin\\git.exe
    set GIT_PYTHON_GIT_EXECUTABLE=git\\bin\\git.exe
    set PYTHON=py310\\python.exe
    set COMMANDLINE_ARGS=<args>

    %PYTHON% launch.py
    pause
    exit /b'''

    final = bat_content.replace("<args>", args_ok)
    with open("boot.bat", "w", encoding="utf-8") as f:
        f.write(final)



# 登录函数
def signin():
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
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
    response = requests.post(url=target, headers=headers, data=content,verify=False)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        print('登录成功')
        return response['token']
    else:
        print('登录失败，原因：', response['msg'])
        exit(0)


# 获取用户信息
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
    response = requests.get(url=target, headers=headers,data=content,verify=False)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        return response['result']
    else:
        print('获取用户信息失败，原因：', response['msg'])
        exit(1)



# 认领任务
def claim_task(token):
    target = url + "claim_task"
    # 生成请求头
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 生成content
    content = {"token": token}
    # 发送请求
    response = requests.post(target, headers=headers, json=content,verify=False).json()
    # 获取响应
    if response['code'] == 200:
        return response
    else:
        print('认领任务失败，原因：', response['msg'])
        return False


# 提交任务
def submit_task(token,task_name, task_num, pics_list):
    target = url + "submit_task"
    # 生成请求头
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 生成content
    content = {'token': token, 'task_name': task_name, 'task_num': task_num, 'pics_list': pics_list}
    # 发送请求
    response = requests.post(url=target, headers=headers, json=content,verify=False).json()
    # 获取响应
    # 判断响应
    if response['code'] == 200:
        return True
    else:
        print('提交任务失败，重试中')
        status = submit_task(token,task_name, task_num, pics_list)
        if status:
            return True
        return False
