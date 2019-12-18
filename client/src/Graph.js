import React, { Component } from "react";
import logo from './logo.svg';
import "./App.css";
import Form from "./Form";
import { XYPlot, CustomSVGSeries, LineSeries} from 'react-vis';
import { grid } from "./files/grid.json";
import { connections } from "./files/connections.json";
import lineSeries from "react-vis/dist/plot/series/line-series";

render () {
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
}
