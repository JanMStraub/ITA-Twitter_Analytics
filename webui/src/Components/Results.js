import React, { Component } from 'react';
import TrendList from './TrendList';
import TrendStats from './TrendStats';
import './Results.css'

class Results extends Component {
    constructor() {
        super()
        this.state = {
            activeTrend: "",
            showStats: false,
            demoMode: false
        };

        this.selectTrend = this.selectTrend.bind(this);
    }

    selectTrend = (trend) => {
        this.setState({activeTrend : trend})
        this.setState({showStats : true})
    }

    render() {

        console.log(this.state.activeTrend)

        return (
            <div className="results">
                <TrendList selectTrend={this.selectTrend} demoMode={this.state.demoMode}/>
                {this.state.showStats && <TrendStats trend={this.state.activeTrend} demoMode={this.state.demoMode}/>}
            </div>
        )
    }
}

export default Results;