import React from 'react';
import { Helmet } from 'react-helmet'
import Navbar from './navbar';
import Botbar from './botbar';
import Mobile from './mobile_notifiy'
import './AboutProject.css'

const TITLE = "About the Project"

function AboutProject() {
    return (
        <div className="aboutproject">
            <Helmet><title>{ TITLE }</title></Helmet>
            <div className="hero_wrapper_about">
                <Navbar />
                <h1>About the Project</h1>
            </div>
            <Botbar />
        </div>
    );
}

export default AboutProject;