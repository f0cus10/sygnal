import React, { Component } from "react";
import logo from './logo.svg';
import "./App.css";
import Form from "./Form";
import { XYPlot, CustomSVGSeries, LineSeries} from 'react-vis';
import { grid } from "./files/grid.json";
import { connections } from "./files/connections.json";
import lineSeries from "react-vis/dist/plot/series/line-series";

/*** what i need to do:
-axios for GET request of nodes and BS
-axios for GET request for connections
-need an API call to post to a JSON file for source & destination links
-figure out how to use the SVG component
-need to parse through the data from GET request to produce the JSON
 ***/

class App extends Component {
state = {
  gridData : [],
  fields: {},
  gridId: null,
};


render () {
  return (
    <div className="App">
      <Form updateGrid={this.formSubmit} />
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
    </div>
  );
  }
}

export default App;
