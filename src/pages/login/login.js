import React, { Component } from "react";
import "./login.css"
import Logo from '../../assets/Logo001.png'
import WallPaper from '../../assets/Wallpaper001.JPG'

import { eel } from "../../eel.js";
//从antd导入输入框、按钮、提示框
import { Input } from 'antd';
import { Button } from 'antd';
import { Form } from 'antd';
import { Checkbox } from 'antd';
import { Card } from 'antd';
import { message } from 'antd';
import cookie from "react-cookies";
import {Link} from "react-router-dom";


//登陆框组件
class Login extends Component {
    constructor(props) {
        super(props);
        eel.set_host("ws://localhost:8888");
    }
    onFinish = (values) => {
        let username = values.username;
        let password = values.password;
        let status = values.remember;
        if(status === false) {
            alert("请同意用户协议");
            location.reload();
        }
        eel.signin(username, password)(token => {
            if(token === 403) {
                alert("用户名或密码错误");
                location.reload();
            }
            else {
                cookie.save("token", token);
                message.success("登陆成功");
                //跳转
                window.location.href = "/mainpage";

            }
        })
    }
    onFinishFailed = (errorInfo) => {
        alert("填写信息不完整")
        location.reload();
    };
    render() {
        return (
            <div>
                <img src={WallPaper} className="backgroundImage">
                </img>
                <Card className="login-container">
                    <img className="login-Logo"
                         src={Logo} alt="logo"/>
                    <h1 className="login-title">用户登录</h1>
                    <Form
                        name="basic"
                        labelCol={{
                            span: 6,
                        }}
                        wrapperCol={{
                            span: 16,
                        }}
                        style={{
                            maxWidth: 800,
                        }}
                        initialValues={{
                            remember: true,
                        }}
                        onFinish={this.onFinish}
                        onFinishFailed={this.onFinishFailed}
                        autoComplete="off"
                    >
                        <Form.Item
                            label="用户名"
                            name="username"
                            rules={[
                                {
                                    required: true,
                                    message: 'Please input your username!',
                                },
                            ]}
                        >
                            <Input />
                        </Form.Item>

                        <Form.Item
                            label="密码"
                            name="password"
                            rules={[
                                {
                                    required: true,
                                    message: 'Please input your password!',
                                },
                            ]}
                        >
                            <Input.Password />
                        </Form.Item>

                        <Form.Item
                            name="remember"
                            valuePropName="checked"
                            rules={
                                [
                                    {
                                        required: true,
                                    }
                                ]
                            }
                            wrapperCol={{
                                offset: 5,
                                span: 16,
                            }}
                        >
                            <Checkbox>同意用户协议</Checkbox>
                        </Form.Item>
                        <Form.Item
                            wrapperCol={{
                                offset: 4,
                                span: 16,
                            }}
                        >
                            <Button type="primary" htmlType="submit">
                                Submit
                            </Button>
                        </Form.Item>
                    </Form>
                </Card>
            </div>

        );
    }
}


export default Login;