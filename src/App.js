import React, { Component } from "react";
import "./App.css";
import Login from "./pages/login/login.js";
import MainPage from "./pages/mainpage/mainpage.js";
import {Routes, Route, BrowserRouter} from "react-router-dom";

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
        page: "login"
    }
  }
  paras = new URLSearchParams(window.location.search);

  routepage = (paras) => {
    if(paras.get("page") === "mainpage") {
        return <MainPage />
    }
    else {
        return <Login />
    }
  }
  pageid = this.routepage(this.paras);


  render() {
      //通过解析get参数进行路由
    return (
        this.pageid
    );
  }
}

export default App;
