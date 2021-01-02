import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom';
import LandingPage from './LandingPage';
import AboutProject from './AboutProject';
import Mobile from './mobile_notifiy';
import Navbar from './navbar';
import Botbar from './botbar';

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
            <Route path="/ITA-Twitter_Analytics" exact component={LandingPage} />
            <Route path="/ITA-Twitter_Analytics/aboutproject" component={AboutProject} />
            <Redirect to="/ITA-Twitter_Analytics" />
          </Switch>
        </div>
      </Router>
    )
  }
}

export default App;