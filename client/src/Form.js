import React from "react";
import axios from "axios";
import "./App.css";

export default class Form extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.state = {numChannels: ""};
  }

Change(e){
  this.setState({numChannels: e});
  console.log(this.state.numChannels);
}
  
handleChange = e => {
  this.setState({
    [e.target.name]: e.target.value
  });
  console.log(this.state.numChannels);
};

onSubmit = async(e) => {
  e.preventDefault();
  const { numChannels } = this.state;

  const result = await axios.post('/submitform', {numChannels});
  const response = result.data;
  console.log(response);
  //this.props.updateGrid(response)
  // this.setState({
  //     numChannels: "",
  //     });

};

render () {
  const numChannels = this.props.numChannels;

  return (
  <div className = "wrapper">
    <h1> CSCI 39596 Project: Iftikhar, Jasmine, Kenny, Sami, Sanjay, Xiangmin </h1>
    <h3> Please enter the following information: </h3>
  <form>
    <input
    name = "numChannels"
    placeholder="Number of channels"
    value={numChannels}
    onChange={this.handleChange}
    />
    <br />
    <button onClick={e => this.onSubmit(e)}>Submit</button>
  </form>
  </div>
  );
  }
}
