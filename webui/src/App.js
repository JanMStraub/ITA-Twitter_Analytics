import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom';
import LandingPage from './LandingPage';
import AboutProject from './AboutProject';
import Mobile from './mobile_notifiy';
import Navbar from './navbar';
import Botbar from './botbar'

class App extends Component {
  constructor() {
    super();
  }

//TODO: Change default url to janmstraub.github.io/TwitterAnalytics

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