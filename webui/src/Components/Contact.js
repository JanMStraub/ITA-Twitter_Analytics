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
                    <div>
                        <h5>Name</h5>
                        <input type="text" name="name" />
                    </div>
                    <div>
                        <h5>email</h5>
                        <input type="text" name="email" />
                    </div>
                    <div>
                        <h5>message</h5>
                        <input type="text" name="message" />
                    </div>
                    <input type="submit" value="Submit" />
                </form>

            </div>
            <Botbar />
        </div>
    );
}

export default Contact;