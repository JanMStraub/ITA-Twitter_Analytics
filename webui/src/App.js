import React, { Component } from 'react';
import scrollToComponent from 'react-scroll-to-component';
import Navbar from './navbar';
import Botbar from './botbar';
import Results from './results';
import Mobile from './mobile_notifiy';

class App extends Component {
  constructor() {
    super();
    this.state = {
      showResults: false
    };

    this.showResults = this.showResults.bind(this);
  }

  showResults() {
    this.setState({
      showResults : true
    });
  }

  componentDidUpdate() {
    if (this.state.showResults) {
      scrollToComponent(this.results, {offset: 0, align: 'top', duration: 1500})
    }
  }

  //scrollToComponent(this.results, {offset: 0, align: 'top'})

  render() {
    return (
      <div className="wrapper">
        <Mobile />
        <div className="hero_wrapper">
          <Navbar />
            <h1>Consumer-Based Decision Aid Of The Top 50 German Twitter Trends</h1>
            <button onClick={this.showResults}>Run Analytics</button>
        </div>
        <section ref={(section) => {this.results = section;}}>
          {this.state.showResults && <Results />}
        </section>
        <Botbar />
      </div>
    )
  }
}

  export default App;