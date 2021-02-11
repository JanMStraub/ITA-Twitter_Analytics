import React, { Component } from 'react';
import './TrendStats.css'
import axios from "axios";
import loading from '../images/loading.gif'


class TrendStats extends Component {
    constructor() {
        super()
        this.state = {
            wordcloudURL: "",
            sentimentURL: "",
            links: {},
            keywords: {},
            tweetCount: 0,
            finishedLoading: false,
            errorWhileLoading: false,
        };
        this.getStats = this.getStats.bind(this);
        this.showLinks = this.showLinks.bind(this);
        this.createTokenTable = this.createTokenTable.bind(this);
    }


    async getStats(trend) {

        var backendURL = "http://localhost:5000/analyze_trend?trend=" + encodeURIComponent(trend)
        if (this.props.demoMode) {
            backendURL = "http://localhost:5000/" + encodeURIComponent(trend) + ".json"
        }

        axios.get(backendURL)
            .then(response => {
                this.setState({ links: response.data.links });
                this.setState({ keywords: response.data.keywords });
                this.setState({ wordcloudURL: "http://localhost:5000/" + encodeURIComponent(trend) + "_wordcloud.png" });
                this.setState({ sentimentURL: "http://localhost:5000/" + encodeURIComponent(trend) + "_sentiment_pie_chart_gervader.png" });
                this.setState({ tweetCount: response.data.tweet_count });
                this.setState({ finishedLoading: true })
            })
            .catch(error => {
                console.log(error);
                this.setState({ errorWhileLoading: true });
            });
    }

    showLinks() {
        if (Object.keys(this.state.links).length === 0) {
            return "LINKS"
        } else {
            var links_tr = []
            for (var key in this.state.links) {
                var value = this.state.links[key]
                var tr = <tr><td>{value}</td><td><a href={key}>{key}</a></td></tr>;
                links_tr.push(tr)
            }
            return links_tr
        }
    }


    createTokenTable() {
        if (Object.keys(this.state.keywords).length === 0) {
            return "KEYWORDS"
        } else {
            var keywords_tr = []
            var counter = 1
            for (var key in this.state.keywords) {
                var value = this.state.keywords[key];
                var tr = <tr><td>{counter}</td><td>{key} <p>({value})</p></td></tr>;
                counter += 1;
                keywords_tr.push(tr)
            }
            return keywords_tr
        }

    }

    componentDidMount() {
        if (this.props.trend) {
            this.getStats(this.props.trend)
        }
    }

    componentDidUpdate(prevProps) {
        if (this.props.trend) {
            if (this.props.trend !== prevProps.trend) {
                this.setState({errorWhileLoading : false})
                this.getStats(this.props.trend)
                this.setState({finishedLoading : false})
            }
        }
    }

    render() {

        var content;
        if (this.state.finishedLoading) {
            content =
                <div>
                    <h6>1.  {this.props.trend}</h6>
                    <p className="tweet_count">(based on {this.state.tweetCount} tweets)</p>
                    <div className="first_row">
                        <div className="topic_words_wrapper">
                            <h3>Topic Words</h3>
                            <table>
                                <tr>
                                    <th>#</th>
                                    <th>Top Words</th>
                                </tr>
                                {this.createTokenTable()}
                            </table>
                        </div>
                        <div className="wordcloud_wrapper">
                            <h3>Wordcloud</h3>
                            <img className="wordcloud" src={this.state.wordcloudURL} alt="" />
                        </div>
                    </div>
                    <div className="second_row">
                        <div className="sentiment_wrapper">
                            <h3>Trend Sentiment</h3>
                            <img className="sentiment" src={this.state.sentimentURL} alt="" />
                        </div>
                        <div className="categories_links_wrapper">
                            <div className="categories_wrapper">
                                <h3>Categories</h3>
                                <p className="WIP">Work in Progress</p>
                            </div>
                            <div className="links_wrapper">
                                <h3>Top Links</h3>
                                <table>
                                    <tr>
                                        <th>#</th>
                                        <th>Top Links</th>
                                    </tr>
                                    {this.showLinks()}
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
        } else {
            content = <div className="loading"><img src={loading} alt="" height="40" width="40" /></div>
        }

        if (this.state.errorWhileLoading) {
            content = <h3>Error while loading data from backend!</h3>
        }

        return (
            <div className="TrendStats">
                {content}
            </div>
        )
    }
}

export default TrendStats;