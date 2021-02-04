import React, { Component } from 'react';
import TrendList from './TrendList';
import TrendStats from './TrendStats';
import './results.css'

class Results extends Component {
    constructor() {
        super()
        this.state = {
            activeTrend: "",
            showStats: false
        };

        this.selectTrend = this.selectTrend.bind(this);
    }

    selectTrend = (trend) => {
        this.setState({activeTrend : trend})
        this.setState({showStats : true})
    }


    //TODO: convert trend to %-notiation for https://de.wikipedia.org/wiki/URL-Encoding
    //convert direct in axios call 

    render() {

        console.log(this.state.activeTrend)

        return (
            <div className="results">
                <TrendList selectTrend={this.selectTrend}/>
                {this.state.showStats && <TrendStats trend={this.state.activeTrend}/>}
            </div>
        )
    }
}

export default Results;