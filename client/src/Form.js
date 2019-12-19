import React from "react";
import axios from "axios";
import "./App.css";
import { Redirect } from 'react-router-dom';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import {withRouter} from 'react-router-dom';

export default class Form extends React.Component {
  state = {
    numChannels: "",
   };

   change = e => {
      this.setState({
          [e.target.name]: e.target.value
              });
                };

    onSubmit = async(e) => {
        e.preventDefault();
        const { numChannels } = this.state;

        const result = await axios.post('/submitform', {numChannels});
        const response = result.data;
        console.log(response);
        //this.props.updateGrid(response)

      };

render () {
  return (
  <div className = "wrapper">
    <h1> CSCI 39596 Project: Iftikhar, Jasmine, Kenny, Sami, Sanjay, Xiangmin </h1>
    <h3> Please enter the following information: </h3>
  <form>
    <input
    name = "numChannels"
    placeholder="Number of channels"
    value={this.state.numChannels}
    onChange={e => this.change(e)}
    />
    <br />
    <button onSubmit= {e => this.onSubmit} >Submit</button>
  </form>
</div>
    );
  }
}
