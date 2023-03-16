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
url = "https://tritium.work/"


def searchConfig():
    # 检测当前目录下有无指定文件
    if os.path.exists('launch.py'):
        if os.path.exists('boot.bat'):
            print("检测到配置文件，跳过生成步骤")
            return True
        else:
            print("检测到webui，但是没有配置文件，正在生成配置文件")
            return False
    else:
        print("没有检测到webui")
        exit(0)


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

    print(f"最终使用的启动参数: {args_ok}")
    final = bat_content.replace("<args>", args_ok)
    with open("boot.bat", "w", encoding="utf-8") as f:
        f.write(final)
    print("生成完成~ 请使用A启动脚本.bat启动")


def createConfig():
    args_ok = ""
    # 创建配置文件
    print('''
    ============================
    请先选择你的显存大小

    1) 4G 及以下
    2) 6G
    3) 8G 及以上
    4) 我没有Nvidia的独立显卡，使用CPU生成
    ============================
    ''')
    vram_choice = input("请输入上面的数字后按回车: ")
    if vram_choice == "1":
        args_ok += "--lowvram "
    elif vram_choice == "2":
        args_ok += "--medvram "
    elif vram_choice == "3":
        pass
    elif vram_choice == "4":
        args_ok += "--use-cpu all --precision full --no-half --skip-torch-cuda-test"
        end(args_ok)
        exit(0)
    else:
        print("选择的不对捏 重开吧!")
        exit(0)

    print('''
    =============================================
               请选择你需要的启动参数

    ===================常用参数===================
    1) deepdanbooru (识别tag用, 训练可能会用到)
    2) xformers (可能会让你生成图片变快)
    3) 16系显卡生成图片黑的选我 (单精度)

    ================一般不用的参数，没事别选================
    4) --no-half-vae (生成超大图防止黑图, 拖慢生成速度一般不要选这个)
    5) --listen 允许公网访问
    6) --api 启用api (如果你搭建bot, 需要选择这个)
    7) --disable-safe-unpickle (!!!! 不安全的加载模型方式，部分大模型必须开启这个选项才可以加载，后果自负 !!!!)
    提示: 如果你想同时选择1和2只需要输入12就可以了
    ''')

    args_choice = input("请输入上面的数字后按回车(1-6): ")

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
        else:
            print(f"无法识别这个参数: {c}")
    end(args_ok)


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
    response = requests.post(url=target, headers=headers, data=content)
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
    response = requests.get(url=target, headers=headers,data=content)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        return response['result']
    else:
        print('获取用户信息失败，原因：', response['msg'])
        exit(1)



# 认领任务
def claim_task(token,task_num):
    target = url + "claim_task"
    # 生成请求头
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 生成content
    content = {'token': token, 'task_num': task_num}
    # 发送请求
    js = json.dumps(content)
    response = requests.post(url=target, headers=headers, data=js)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        return True
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
    js = json.dumps(content)
    response = requests.post(url=target, headers=headers, json=js)
    # 获取响应
    response = response.json()
    # 判断响应
    if response['code'] == 200:
        return True
    else:
        print('提交任务失败，重试中')
        status = submit_task(token,task_name, task_num, pics_list)
        if status:
            return True
        return False
