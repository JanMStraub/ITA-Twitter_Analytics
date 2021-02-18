import React, { Component } from 'react';
import './TrendList.css';
import axios from "axios";


class TrendList extends Component {
    constructor() {
        super()
        this.state = {
            trends: [],
            firstTrend: 0
        };
        this.getTrends = this.getTrends.bind(this);
        this.increaseTrend = this.increaseTrend.bind(this);
        this.decreaseTrend = this.decreaseTrend.bind(this);
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

    increaseTrend() {
        if (this.state.firstTrend < 45) {
            this.setState({firstTrend: this.state.firstTrend + 5})
        }
    }

    decreaseTrend() {
        if (this.state.firstTrend >= 5) {
            this.setState({firstTrend: this.state.firstTrend - 5})
        }
    }


    render() {

        const TrendsMenuBlock = (trends, firstTrend) => {

            const items = trends.map((trend, idx) => {
                return <div>
                    
                    <p className="trendNumber">{firstTrend + idx + 1}</p>
                    <li onClick={() => {
                    this.props.selectTrend(trend, firstTrend + idx + 1)
                    }} key={idx}>{trend}</li>
        
                </div>;
            });
        
            return (
                <div className="trendmenublock">
                    <ul>{items}</ul>
                </div>
            )
        }

        const trendsBlock = TrendsMenuBlock(this.state.trends.slice(this.state.firstTrend, this.state.firstTrend + 5), this.state.firstTrend)

        return (
            <div className="TrendList">
                <h2>Trends</h2>
                <h6>Quick Access</h6>
                <p className="tweet_count">Start here by Selecting a Trend</p>
                <div className="menu-bar">
                    <button className="left_button" onClick={this.decreaseTrend}> </button>
                    {trendsBlock}
                    <button className="right_button" onClick={this.increaseTrend}> </button>
                </div>
            </div>
        )
    }
}

export default TrendList;