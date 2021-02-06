import React from 'react';
import './Navbar.css'
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <header>
      <div className="navigation">
        <nav>
          <ul> 
            <Link to="/"><li>Analytics</li></Link>
            <Link to="/aboutproject"><li>About The Project</li></Link>
            <Link to="/aboutus"><li>About US</li></Link>
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
            <Link to="/contact"><li>Contact</li></Link>
            <li><a href="https://github.com/JanMStraub/ITA-Twitter_Analytics/">Github</a></li>
          </ul>
        </nav>
      </div>
    </header>
  )
}

export default Navbar;