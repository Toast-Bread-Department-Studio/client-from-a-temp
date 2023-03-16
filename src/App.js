import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";

import { eel } from "./eel.js";
//从antd导入输入框、按钮、提示框
import { UserOutlined } from '@ant-design/icons';
import { Input } from 'antd';
import { Button } from 'antd';



//登陆框组件
class Login extends Component {
    constructor(props) {
        super(props);
        eel.set_host("ws://localhost:8888");
    }
    render() {
        return (
            <div className="login" style={
                {
                    position: "absolute",
                    top: "60%",
                    left: "50%",
                    transform: "translate(-50%,-50%)",
                }
            }>
                <Input size="large" placeholder="用户名" prefix={<UserOutlined />} />
                <br />
                <br />
                <Input.Password size="large" placeholder="密码" prefix={<UserOutlined />} />
                <br />
                <Button>qwe</Button>
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
        <div className="App" style={
            {
                backgroundImage: `url("https://i.328888.xyz/2023/03/16/JYivc.png")`
            }
        }>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
<br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
<br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
<br/>
            <br/>
            <br/>


            <h1>123qwe</h1>

            <Login />
        </div>
    );
  }
}

export default App;
