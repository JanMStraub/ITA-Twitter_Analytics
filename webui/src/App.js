import React from 'react';
import Navbar from './navbar';
import Botbar from './botbar';
import Results from './results';
import Mobile from './mobile_notifiy';

function App() {

  return (
    <div className="wrapper">
    <Mobile />
      <div className="hero_wrapper">
        <Navbar />
        <h1>Consumer-Based Decision Aid Of The Top 50 German Twitter Trends</h1>
        <button>Run Analytics</button>
      </div>
      <Botbar />
    </div>
  )
}

export default App;