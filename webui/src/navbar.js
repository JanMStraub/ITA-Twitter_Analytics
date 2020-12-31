import React from 'react';
import './navbar.css'

function Navbar() {
  return (
    <header>
      <div className="navigation">
        <nav>
          <ul>
            <li><a href="index.html">Analytics</a></li>
            <li><a href="project.html">About The Project</a></li>
            <li><a href="about.html">About Us</a></li>
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