import React, { Component } from 'react';
import './TrendList.css';
import axios from "axios";

class TrendList extends Component {
    constructor() {
        super()
        this.state = {
            trends: []
        };
        this.getTrends = this.getTrends.bind(this);
    }


    async getTrends() {

        var url = "http://localhost:5000/trend_list"
        if (this.props.demoMode) {
            url += "?demo=True"
        }

        axios.get(url)
            .then(response => {
                this.setState({ trends: response.data })
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    componentDidMount() {

        this.getTrends()
    }


    render() {

        const items = this.state.trends.map((trend, idx) => {
            return <li onClick={() => {
                this.props.selectTrend(trend)
            }} key={idx}>{trend}</li>;
        });

        return (
            <div className="TrendList">
                <h2>Current Trends</h2>
                <h6>Quick Access</h6>
                <div className="list_div">
                    <ul>{items.slice(0, 10)}</ul>
                    <ul>{items.slice(10, 20)}</ul>
                    <ul>{items.slice(20, 30)}</ul>
                    <ul>{items.slice(30, 40)}</ul>
                    <ul>{items.slice(40, 50)}</ul>
                </div>
            </div>
        )
    }
}

export default TrendList;