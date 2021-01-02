import React from 'react';
import './navbar.css'
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <header>
      <div className="navigation">
        <nav>
          <ul> 
            <Link to="/ITA-Twitter_Analytics"><li>Analytics</li></Link>
            <Link to="/ITA-Twitter_Analytics/aboutproject"><li>About The Project</li></Link>
            <Link to="/ITA-Twitter_Analytics/aboutus"><li>About US</li></Link>
          </ul>
        </nav>
      </div>

      <div className="names">
        <ul>
          <li>Maximilian Schöneberger</li>
          <li>Jan Straub</li>
          <li>Paavo Streibich</li>
          <li>Robin Viellieber</li>
        </ul>
      </div>

      <div className="icons">
        <nav>
          <ul>
            <li><a href="mailto:viellieber@stud.uni-heidelberg.de">Contact</a></li>
            <li><a href="https://github.com/JanMStraub/ITA-Twitter_Analytics/">Github</a></li>
          </ul>
        </nav>
      </div>
    </header>
  )
}

export default Navbar;