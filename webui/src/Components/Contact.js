import React from 'react';
import { Helmet } from 'react-helmet'
import Navbar from './navbar';
import Botbar from './botbar';
import './Contact.css'
import headertext from '../images/contact_headertext.png';

const TITLE = "Contact"

function Contact() {
    return (
        <div className="contact">
            <Helmet><title>{TITLE}</title></Helmet>
            <div className="hero_wrapper_contact">
                <Navbar />
                <img className="heading" src={headertext} alt="Contact Us" />
                <form>
                    <div className="input">
                        <h5>Name</h5>
                        <input type="text" name="" placeholder="Your Name..." />
                    </div>
                    <div className="input">
                        <h5>email</h5>
                        <input type="text" name="" placeholder="Your Email..." />
                    </div>
                    <div className="input">
                        <h5>message</h5>
                        <div className="message_spacing">
                            <textarea className="input_message" rows="5" name="" placeholder="Your message..." />
                        </div>
                    </div>
                    <div className="submit_placing">
                        <input className="submit_contact" type="submit" value="Submit" />
                    </div>
                </form>

            </div>
            <Botbar />
        </div>
    );
}

export default Contact;