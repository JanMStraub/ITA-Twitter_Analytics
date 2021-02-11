import React from 'react';
import './Botbar.css'
import { Link } from 'react-router-dom';

function Botbar() {
    return (
      <footer>
        <ul>
          <Link to="/imprint"><li>Imprint</li></Link>
          <Link to="/privacy"><li>Privacy Notice</li></Link>
          <Link to="/agb"><li>AGB'S</li></Link>
        </ul>
        <ul className="demo_mode_disclaimer">
          <li>This site is currently in demo mode. Click <Link to="/demo">here</Link> to learn more.</li>
        </ul>
      </footer>
    )
}

export default Botbar