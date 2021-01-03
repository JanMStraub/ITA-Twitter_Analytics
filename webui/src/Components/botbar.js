import React from 'react';
import './botbar.css'
import { Link } from 'react-router-dom';

function Botbar() {
    return (
      <footer>
        <ul>
          <Link to="/imprint"><li>Imprint</li></Link>
          <Link to="/privacy"><li>Privacy Notice</li></Link>
          <Link to="/agb"><li>AGB'S</li></Link>
        </ul>
      </footer>
    )
}

export default Botbar