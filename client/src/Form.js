import React from "react";
import axios from "axios";

export default class Form extends React.Component {
  state = {
    SourceNode: "",
    DestinationNode: "",
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
  this.props.updateGrid(response)
  this.setState({
      SourceNode: "",
      DestinationNode: "",
      numChannels: "",
  });
};

render () {
  return (
  <div className = "wrapper">
    <h1> CSCI 39596 Project: Iftikhar, Jasmine, Kenny, Sami, Sanjay, Xiangmin </h1>
    <h3> Please enter the following information: </h3>
  <form>
    <input
    name="SourceNode"
    placeholder="Choose your source node"
    value={this.state.SourceNode}
    onChange={e => this.change(e)}
    />
    <br />
    <input
    name = "DestinationNode"
    placeholder="Choose your destination node"
    value={this.state.DestinationNode}
    onChange={e => this.change(e)}
    />
    <br />
    <input
    name = "numChannels"
    placeholder="Number of channels"
    value={this.state.numChannels}
    onChange={e => this.change(e)}
    />
    <br />
    <button onClick={e => this.onSubmit(e)}>Submit</button>
  </form>
</div>
    );
  }
}
