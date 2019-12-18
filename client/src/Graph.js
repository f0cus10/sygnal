import React, { Component } from "react";
import "./App.css";
import { XYPlot, CustomSVGSeries, LineSeries} from 'react-vis';
import { grid } from "./files/grid.json";
import { connections } from "./files/connections.json";

class Graph extends Component {
  state = {
    fields: {}
  }
  render(){
    return(
      <div>
        <p>
          {JSON.stringify(this.state.fields, null, 2)}
        </p>
        <XYPlot width={300} height={300}>
          <CustomSVGSeries data={grid} />
          {
            Object.values(connections).map((i) => {
              return(
                <LineSeries data={i} />
              );
            })
          }
        </XYPlot>
      </div>
    )
  }
}

export default Graph;