import React, { Component } from "react";
import "./App.css";
import "./login.css"
import Logo from './assets/Logo001.png'
import WallPaper from './assets/Wallpaper001.JPG'

import { eel } from "./eel.js";
//从antd导入输入框、按钮、提示框
import { UserOutlined, KeyOutlined } from '@ant-design/icons';
import { Input } from 'antd';
import { Button } from 'antd';
import { Form } from 'antd';
import { Checkbox } from 'antd';
import { Card } from 'antd';
import { message } from 'antd';
import { Modal } from 'antd';
import { notification } from 'antd';
import {values} from "mobx";
import cookie from "react-cookies";


//登陆框组件
class Login extends Component {
    constructor(props) {
        super(props);
        eel.set_host("ws://localhost:8888");
    }
    onFinish = (values) => {
        let username = values.username;
        let password = values.password;
        eel.signin(username, password)(token => {
            if(token === 403) {
                alert("用户名或密码错误");
                location.reload();
            }
            else {
                cookie.save("token", token);
                message.success("登陆成功");
            }
        })
    }
    onFinishFailed = (errorInfo) => {
    };
    render() {
        return (
            <div>
                <img src={WallPaper} className="backgroundImage">
                </img>
                <Card className="login-container">
                    <img className="login-Logo"
                        src={Logo} alt="logo"/>
                    <Form
                        name="basic"
                        labelCol={{
                            span: 8,
                        }}
                        wrapperCol={{
                            span: 16,
                        }}
                        style={{
                            maxWidth: 600,
                        }}
                        initialValues={{
                            remember: true,
                        }}
                        onFinish={this.onFinish}
                        autoComplete="off"
                    >
                        <Form.Item
                            label="Username"
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
                            label="Password"
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
                            wrapperCol={{
                                offset: 8,
                                span: 16,
                            }}
                        >
                            <Checkbox>Remember me</Checkbox>
                        </Form.Item>
                        <Form.Item
                            wrapperCol={{
                                offset: 8,
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

class App extends Component {
  constructor(props){
    super(props);
    eel.set_host("ws://localhost:8888");
    eel.hello();
  }
  render() {
    return (
        <div>
            <Login />
        </div>
    );
  }
}

export default App;
