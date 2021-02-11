import React from 'react';
import { Helmet } from 'react-helmet'
import Navbar from './Navbar';
import Botbar from './Botbar';
import './Demo.css'

const TITLE = "Demo mode"

function Demo() {
    return (
        <div className="demo">
            <Helmet><title>{TITLE}</title></Helmet>
            <div className="hero_wrapper_demo">
                <Navbar />
                <div className="demo_text">
                    <p>This site is in demo mode only because...</p>
                </div>
            </div>
            <Botbar />
        </div>
    );
}

export default Demo;