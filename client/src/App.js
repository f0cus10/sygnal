import React, { Component } from "react";
import logo from './logo.svg';
import "./App.css";
import Form from "./Form";
import { BrowserRouter as Router } from "react-router-dom";

class App extends Component {
state = {
  fields: {}
};

  onSubmit = updatedValue => {
    this.setState({
      fields: {
      ...this.state.fields,
      ...updatedValue
      }
    });
  };

render () {
  return (
    <div className="App">
      <Form onChange={fields => this.onSubmit(fields)}/>
        <p>
        {JSON.stringify(this.state.fields, null, 2)}
        </p>
    </div>
  );
  }
}

export default App;
