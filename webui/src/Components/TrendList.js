import React from 'react';
import './TrendList.css'

function TrendList(props) {

    const items = props.trends.map((trend, idx) => {
        return <li key={idx}>{trend}</li>;
    });

    return (
        <div className="TrendList">
            <ul>{items.slice(0, 10)}</ul>
            <ul>{items.slice(10, 20)}</ul>
            <ul>{items.slice(20, 30)}</ul>
            <ul>{items.slice(30, 40)}</ul>
            <ul>{items.slice(40, 50)}</ul>
        </div>
  )
}

export default TrendList;