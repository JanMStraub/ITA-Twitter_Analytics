import React from 'react';
import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom';
import LandingPage from './Components/LandingPage';
import AboutProject from './Components/AboutProject';
import Mobile from './Components/MobileNotifiy';
import Contact from './Components/Contact';
import Demo from './Components/Demo';

function App() {
  return (
    <Router>
      <div className="App">
        <Mobile />
        <Switch>
          <Route path="/" exact component={LandingPage} />
          <Route path="/aboutproject" component={AboutProject} />
          <Route path="/contact" component={Contact} />
          <Route path="/demo" component={Demo} />
          <Redirect to="/" />
        </Switch>
      </div>
    </Router>
  )
}

export default App;