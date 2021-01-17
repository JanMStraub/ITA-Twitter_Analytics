import React from 'react';
import './TrendStats.css'
import axios from "axios";
import { useState, useEffect } from 'react';


function TrendStats(props) {

    const [ldaURL, setLdaURL] = useState("");
    const [wordcloudURL, setWordcloudURL] = useState("");
    const [plotURL, setPlotURL] = useState("");


    async function getStats(trend) {
        axios.get("http://localhost:5000/analyze_trend?trend=" + trend)
        .then(
            setLdaURL("http://localhost:5000/" + trend + "_lda.png")
            // set WordcloudURL
            // set PlotURL
            )
        .catch(function(error) {
            console.log(error);
        });
    }

    useEffect(() => {
        // Update the document title using the browser API
        getStats(props.trend)
      });

    // load and display result.json

    return (
        <div className="TrendStats">
            <img src={ldaURL} alt="" height="200" width="200"/>
            <img src={wordcloudURL} alt="" height="200" width="200"/>
            <img src={plotURL} alt="" height="200" width="200"/>
            

        </div>
  )
}

export default TrendStats;