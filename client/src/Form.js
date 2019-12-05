import React from "react";

export default class Form extends React.Component {
  state = {
    SourceNode: "",
    DestinationNode: "",
    Channels: "",
  };

change = e => {
  this.props.onChange({ [e.target.name]: e.target.value });
  this.setState({
    [e.target.name]: e.target.value
  });
};

onSubmit = e => {
  e.preventDefault();
  // this.props.onSubmit(this.state);
  this.setState({
      SourceNode: "",
      DestinationNode: "",
      Channels: "",
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
    name = "Channels"
    placeholder="Number of channels"
    value={this.state.Channels}
    onChange={e => this.change(e)}
    />
    <br />
    <button onClick={e => this.onSubmit(e)}>Submit</button>
  </form>
</div>
    );
  }
}
