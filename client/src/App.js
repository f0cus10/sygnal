import React, { Component } from "react";
import logo from './logo.svg';
import "./App.css";
import Form from "./Form";
import { XYPlot, CustomSVGSeries, LineSeries} from 'react-vis';

class App extends Component {
state = {
  fields: {},
  gridData : [],
  gridId: null,
  data: [
  {x: 10, y: 20, customComponent: 'circle', size: 20, style: {fill:'orange'}},
  {x: 40, y: 20 , customComponent: 'circle', size: 20, style: {fill:'orange'}},
  {x: 70, y: 50, customComponent: 'square', size: 20},
  {x: 55, y: 15, customComponent: 'square', size: 20}
  ],
  connectionData: [
    {x: 70, y: 50},
    {x: 55, y: 15}
  ]

};

  // formSubmit = (serverData) => {
  //   const {gridID, grid} = serverData;
  //   this.setState({
  //     gridId: gridID,
  //     gridData: grid 
  //   })
  // }

render () {
  return (
    <div className="App">
      <Form updateGrid={this.formSubmit} />
        <p>
        {JSON.stringify(this.state.fields, null, 2)}
        </p>
        <XYPlot width={300} height={300}>
          <CustomSVGSeries data = {this.state.data}/>
          <LineSeries data = {this.state.connectionData}/>
        </XYPlot>
    </div>
  );
  }
}

export default App;
