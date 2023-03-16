import React, { Component } from "react";
import "./App.css";
import { eel } from "./eel.js";
import Login from "./pages/login/login.js";
import MainPage from "./pages/mainpage/mainpage.js";
import { BrowserRouter, Routes, Route } from "react-router-dom";

class App extends Component {
  constructor(props){
    super(props);
    eel.set_host("ws://localhost:8888");
  }
  render() {
    return (
        <BrowserRouter>
        <div className="App">
          <Routes>
            <Route path='/' element={<Login />}/>
            <Route path='/mainpage' element={<MainPage />}/>
          </Routes>
        </div>
        </BrowserRouter>
    );
  }
}

export default App;
