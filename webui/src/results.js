import React, { Component } from 'react';
import axios from "axios";
import './results.css'

class Results extends Component {
    constructor() {
        super()
        this.state = {
            title: "did not work :("
        };
        this.getTrends = this.getTrends.bind(this);
    }

    componentDidMount() {
        this.getTrends()
    }

    async getTrends() {
        axios.get("http://localhost:5000/")
        .then(response => {
            this.setState({ title : response.data });
        })
        .catch(function(error) {
            console.log(error);
        });
    }
    
    render() {
        return (
            <div className="results">
            <h2>Current Trends</h2>
        </div>
        )
    }
}

export default Results;