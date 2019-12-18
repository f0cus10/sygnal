import React, { Component } from "react";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Form from "./Form";
import Graph from "./Graph";
import "./App.css";

class App extends Component {

render () {
  return (
    <BrowserRouter>
    <Switch>
      <Route path="/" component={Form} exact />
      <Route path="/data" component={Graph} exact />
      <Route component={Error} />
    </Switch>
    </BrowserRouter>
    );
  }
}

export default App;
