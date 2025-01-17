import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import App from './App';
import Form from './Form';

class App extends Component {
  render () {
    return (
      <BrowserRouter>
      <div>
      <Switch>
      <Route path= "/" component = {Form} exact/>
      <Route path= "/data" component = {App}/>
      </Switch>
      </div>
      </BrowserRouter>
    );
  }
}

export default App;
