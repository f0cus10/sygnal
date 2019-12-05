import React, { Component } from "react";
import logo from './logo.svg';
import "./App.css";
import Form from "./Form";
import { Graph } from "react-d3-graph";

class App extends Component {
state = {
  fields: {},
  gridData : [],
  gridId: null,
  data: {
    nodes: [ 
    { id: "BS1", symbolType: "triangle"}, { id: "BS2", symbolType: "triangle"}, 
    { id: "Node1"}, { id: "Node2"}, { id: "Node3"}, { id: "Node4"}],
    links: [
    { source: "BS1", target: "Node1" }, { source: "BS1", target: "Node3" },
    { source: "BS2", target: "Node2" }, { source: "BS2", target: "Node4" }]
  }

};

  formSubmit = (serverData) => {
    const {gridID, grid} = serverData;
    this.setState({
      gridId: gridID,
      gridData: grid 
    })
  }

render () {
  return (
    <div className="App">
      <Form updateGrid={this.formSubmit} />
        <p>
        {JSON.stringify(this.state.fields, null, 2)}
        </p>
        {/* <Graph
          id="graph-id"
          data={this.state.data}
        /> */}
    </div>
  );
  }
}

export default App;
