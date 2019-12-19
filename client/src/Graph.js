import axios from "axios";
import React, { Component } from "react";
import logo from './logo.svg';
import "./App.css";
import Form from "./Form";
import { XYPlot, CustomSVGSeries, LineSeries} from 'react-vis';
import { grid } from "./files/grid.json";
import { connections } from "./files/connections.json";
import lineSeries from "react-vis/dist/plot/series/line-series";

class Graph extends Component {
  constructor(props) {
    super(props);
    this.handleGridState = this.handleGridChange.bind(this);
    this.state = {
      gridData : [],
      fields: {},
      gridId: this.props.gridId,
      SourceNode: "",
      DestinationNode: "",
      gridG: this.props.gridG,
    };
  }


  componentDidMount(){
    console.log(this.state.gridG);
  }
  handleGridChange(gridGM){
    this.setState({gridG: gridGM});
    console.log(this.state.gridG);
  }



getConnectionData(){
  
}


change = e => {
  this.setState({
    [e.target.name]: e.target.value
  });
};

getConnectionData() {
  console.log(Object.values(connections));
}

onSubmit = async(e) => {
  e.preventDefault();
  const { SourceNode } = this.state;
  const { DestinationNode } = this.state;
  console.log(SourceNode);
  console.log(DestinationNode);
  //this.getGridData();
  //this.getConnectionData();
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
  const gridG = this.state.gridG;
  return (
    <div className="App">
        <XYPlot width={300} height={300}>
          <CustomSVGSeries data = {gridG}/>
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
          <button onClick={e => this.onSubmit(e)}>Submit</button>
        </form>

    </div>


  );
  }
}

export default Graph;