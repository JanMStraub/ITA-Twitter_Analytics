import React, { Component } from 'react';
import TrendList from './TrendList';
import TrendStats from './TrendStats';
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
        axios.get("http://localhost:5000/trend_list")
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
            <TrendList trends={this.state.trends}/>
            <TrendStats trend={"%23DSDS"}/>
            
        </div>
        )
    }
}

export default Results;