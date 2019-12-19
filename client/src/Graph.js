import axios from "axios";
import React, { Component } from "react";
import logo from './logo.svg';
import "./App.css";
import Form from "./Form";
import { XYPlot, CustomSVGSeries, LineSeries} from 'react-vis';
import { grid } from "./files/grid.json";
import { connections } from "./files/connections.json";
import lineSeries from "react-vis/dist/plot/series/line-series";

class App extends Component {
state = {
  gridData : [],
  fields: {},
  gridId: null,
  SourceNode: "",
  DestinationNode: "",
};

change = e => {
  this.setState({
    [e.target.name]: e.target.value
  });
};

onSubmit = async(e) => {
  e.preventDefault();
  const { SourceNode } = this.state;
  const { DestinationNode } = this.state;

  const result = await axios.post('/submitform', {SourceNode, DestinationNode});
  const response = result.data;
  console.log(response);
  //this.props.updateGrid(response)
  this.setState({
      SourceNode: "",
      DestinationNode: "",
      });

};


render () {
  return (
    <div className="App">
        <p>
        {JSON.stringify(this.state.fields, null, 2)}
        </p>
        <XYPlot width={300} height={300}>
          <CustomSVGSeries data = {grid}/>
          {Object.values(connections).map((index) => {
            return(
              <LineSeries data={index}/>
            )
          })}
        </XYPlot>

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
          <button onSubmit={e => this.onSubmit(e)}>Submit</button>
        </form>

    </div>


  );
  }
}

export default App;
