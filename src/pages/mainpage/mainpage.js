import React, {Component} from "react";
import {eel} from "./eel.js";
import './mainpage.css'
import WallPaper from '../../assets/Wallpaper004.png'
import {Card, Form, message, Modal} from 'antd';
import {Button} from 'antd';
import cookie from "react-cookies";
import {Radio} from "antd";
import {Space} from "antd";
import {wait} from "@testing-library/user-event/dist/utils";

class MainPage extends Component {
    handleOk = e => {
        console.log(e);
        this.setState({
            visible: false,
        });
    };
    handleCancel = e => {
        console.log(e);
        this.setState({
            visible: false,
        });
    };

    constructor(props) {
        super(props);
        this.state = {
            balance: 0,
            username: "",
            vramvisible: false,
            openingvisible: false,
            configChecked: false,
            webuiRunning: false,
            webuiloading: false,
        }
        eel.set_host("ws://localhost:8888");
        let token = cookie.load("token");
        eel.get_user_info(token)((values) => {
            this.setState({
                balance: values[0],
                username: values[1]
            })
        });
    }

    setVisiable = () => {
        this.setState({
            vramvisible: true,
        });
    }
    setInVisiable = () => {
        this.setState({
            vramvisible: false,
        });

    }

    check_config = () => {
        eel.check_config()((status) => {
            if (status === 2) {
                alert("未检测到webui!请下载webui后将该程序放入webui根文件夹内");
            } else if (status === 1) {
                message.error("未检测到config，即将开始生成");
                this.setVisiable();
            }else {
                message.success("已检测到config");
                this.setState({
                    configChecked: true,
                })
            }
        })
    }
    onFinish = (values) => {
        let vram = values.vram;
        eel.createConfig(vram);
        this.setInVisiable();
    }
    onFinishFailed = (errorInfo) => {
        console.log(errorInfo);
    }
    runUI = () => {
        eel.run_webui()(async (status) => {
            if (status === 1) {
                message.success("运行成功 webui启动中");
                this.setState({
                    webuiloading: true,
                })
                await wait(20000);
                this.setState({
                    webuiloading: false,
                    webuiRunning: true,

                })

            } else {
                message.error("运行失败");
            }
        })
    }

    checkModels = () => {
        message.info("正在检查模型");
        eel.checkmodels()(() => {
                message.success("模型下载完成");

        })

    }
    croissant = () => {
        eel.croissantNetwork()(() => {
            message.success("成功");
        })
    }

    render() {
        let balance;
        balance = this.state.balance;
        return (
            <div className="Mainpage">
                <img src={WallPaper} className="backgroundImage">
                </img>
                <Modal title="选择显存大小" open={this.state.vramvisible} footer={null}>
                    <Form
                        onFinish={this.onFinish}
                        onFinishFailed={this.onFinishFailed}>
                        <Form.Item
                            label="显存大小"
                            name='vram'
                            rules={[{
                                        required: true,
                                        message: '请输入显存大小',
                                    }]}>
                            <Radio.Group>
                                <Space direction="vertical">
                                    <Radio value={1}>2-4G</Radio>
                                    <Radio value={2}>4-8G</Radio>
                                    <Radio value={3}>8G以上</Radio>
                                </Space>
                            </Radio.Group>
                        </Form.Item>
                        <Form.Item
                            name="submit">
                            <Button type="primary" htmlType="submit">确认</Button>
                        </Form.Item>
                    </Form>
                </Modal>


                <Card className="container">
                    <p>balance:{balance} username:{this.state.username}</p>
                    <h1 className="title">控制面板</h1>
                    <h2 className="subtitle">第一步:检测文件完整性</h2>
                    <Button className='Buttons' type="primary" size='Large' onClick={this.check_config}>
                        执行</Button>
                    <h2 className="subtitle">第二步:开启webui</h2>
                    <Button className='Buttons' type="primary" size='Large' disabled={!this.state.configChecked} onClick={this.runUI} loading={this.state.webuiloading}>
                        执行</Button>
                    <h2 className="subtitle">第三步:检测模型及插件</h2>
                    <Button className='Buttons' type="primary" size='Large' disabled={!this.state.webuiRunning} onClick={this.checkModels}>
                        执行</Button>
                    <h2 className="subtitle">第四步:🥐可颂网络🥐</h2>
                    <Button className='croissantButtons' type="primary" size='Large' disabled={this.state.webuiRunning} onClick={this.croissant}>
                        🥐🥐</Button>
                </Card>
            </div>
        );

    }
}


export default MainPage;