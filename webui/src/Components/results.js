import React, { Component } from 'react';
import axios from "axios";
import './results.css'

class Results extends Component {
    constructor() {
        super()
        this.state = {
            trends: []
        };
        this.getTrends = this.getTrends.bind(this);
    }

    componentDidMount() {
        this.getTrends()
    }

    async getTrends() {
        axios.get("http://localhost:5000/init_analysis")
        .then(response => {
            this.setState({ trends : response.data });
        })
        .catch(function(error) {
            console.log(error);
        });
    }
    
    render() {
        return (
            <div className="results">
            <h2>Current Trends</h2>
            <p>{this.state.trends}</p>
        </div>
        )
    }
}

export default Results;