import React, { Component } from 'react';
import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom';
import LandingPage from './Components/LandingPage';
import AboutProject from './Components/AboutProject';
import Mobile from './Components/mobile_notifiy';

class App extends Component {
  constructor() {
    super();
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Mobile />
          <Switch>
            <Route path="/" exact component={LandingPage} />
            <Route path="/aboutproject" component={AboutProject} />
            <Redirect to="/" />
          </Switch>
        </div>
      </Router>
    )
  }
}

export default App;