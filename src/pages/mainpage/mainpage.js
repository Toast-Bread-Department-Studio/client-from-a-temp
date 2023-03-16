import React, { Component } from "react";
import { eel } from "../../eel.js";
import './mainpage.css'
import WallPaper from '../../assets/Wallpaper004.png'
import { Card } from 'antd';
import {Button} from 'antd';
import cookie from "react-cookies";

class MainPage extends Component {
    balance = 0;
    username = "";
    constructor(props) {
        super(props);
        eel.set_host("ws://localhost:8888");
        let token = cookie.load("token");
        eel.get_user_info(token)((balance, username) => {
            this.balance = balance;
            this.username = username;
        })
    }

    render() {
        return (
            <div className="Mainpage">
                <img src={WallPaper} className="backgroundImage">
                </img>
                <Card className="container">
                    <p>balance:{this.balance}</p>
                    <h1 className="title">控制面板</h1>
                    <h2 className="subtitle">第一步:检测文件完整性</h2>
                    <Button type="primary" size='Large'>
                        执行</Button>


                </Card>
            </div>
        );

    }
}


export default MainPage;