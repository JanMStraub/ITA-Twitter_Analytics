(this.webpackJsonpwebui=this.webpackJsonpwebui||[]).push([[0],{45:function(e,t,s){},54:function(e,t,s){},57:function(e,t,s){},59:function(e,t,s){},78:function(e,t,s){},79:function(e,t,s){},80:function(e,t,s){},81:function(e,t,s){},82:function(e,t,s){},83:function(e,t,s){},84:function(e,t,s){},85:function(e,t,s){},86:function(e,t,s){"use strict";s.r(t);var i=s(0),c=s(1),n=s.n(c),r=s(23),a=s.n(r),o=(s(45),s(9)),d=s(3),l=s(12),j=s(13),h=s(5),b=s(15),u=s(14),p=s(11),O=s(38),m=s.n(O);s(54);var x=function(){return Object(i.jsxs)("header",{children:[Object(i.jsx)("div",{className:"navigation",children:Object(i.jsx)("nav",{children:Object(i.jsxs)("ul",{children:[Object(i.jsx)(o.b,{to:"/",children:Object(i.jsx)("li",{children:"Analytics"})}),Object(i.jsx)(o.b,{to:"/aboutproject",children:Object(i.jsx)("li",{children:"About The Project"})}),Object(i.jsx)(o.b,{to:"/aboutus",children:Object(i.jsx)("li",{children:"About US"})})]})})}),Object(i.jsx)("div",{className:"names",children:Object(i.jsxs)("ul",{children:[Object(i.jsx)("li",{children:"Maximilian Sch\xf6neberger"}),Object(i.jsx)("li",{children:"Jan Straub"}),Object(i.jsx)("li",{children:"Paavo Streibich"}),Object(i.jsx)("li",{children:"Robin Viellieber"})]})}),Object(i.jsx)("div",{className:"icons",children:Object(i.jsx)("nav",{children:Object(i.jsxs)("ul",{children:[Object(i.jsx)(o.b,{to:"/contact",children:Object(i.jsx)("li",{children:"Contact"})}),Object(i.jsx)("li",{children:Object(i.jsx)("a",{href:"https://github.com/JanMStraub/ITA-Twitter_Analytics/",children:"Github"})})]})})})]})};s(57);var f=function(){return Object(i.jsxs)("footer",{children:[Object(i.jsxs)("ul",{children:[Object(i.jsx)(o.b,{to:"/imprint",children:Object(i.jsx)("li",{children:"Imprint"})}),Object(i.jsx)(o.b,{to:"/privacy",children:Object(i.jsx)("li",{children:"Privacy Notice"})}),Object(i.jsx)(o.b,{to:"/agb",children:Object(i.jsx)("li",{children:"AGB'S"})})]}),Object(i.jsx)("ul",{className:"demo_mode_disclaimer",children:Object(i.jsxs)("li",{children:["This site is currently in demo mode. Click ",Object(i.jsx)(o.b,{to:"/demo",children:"here"})," to learn more."]})})]})},v=s(17),w=s.n(v),g=s(19),T=(s(59),s(20)),_=s.n(T),N=function(e){Object(b.a)(s,e);var t=Object(u.a)(s);function s(){var e;return Object(l.a)(this,s),(e=t.call(this)).state={trends:[],firstTrend:0},e.getTrends=e.getTrends.bind(Object(h.a)(e)),e.increaseTrend=e.increaseTrend.bind(Object(h.a)(e)),e.decreaseTrend=e.decreaseTrend.bind(Object(h.a)(e)),e}return Object(j.a)(s,[{key:"getTrends",value:function(){var e=Object(g.a)(w.a.mark((function e(){var t,s=this;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:t="http://localhost:5000/trend_list",this.props.demoMode&&(t+="?demo=True"),_.a.get(t).then((function(e){s.setState({trends:e.data}),s.props.selectTrend(s.state.trends[0],1)})).catch((function(e){console.log(e)}));case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"componentDidMount",value:function(){this.getTrends()}},{key:"increaseTrend",value:function(){this.state.firstTrend<45&&this.setState({firstTrend:this.state.firstTrend+5})}},{key:"decreaseTrend",value:function(){this.state.firstTrend>=5&&this.setState({firstTrend:this.state.firstTrend-5})}},{key:"render",value:function(){var e=this,t=function(t,s){var c=t.map((function(t,c){return Object(i.jsxs)("div",{children:[Object(i.jsx)("p",{className:"trendNumber",children:s+c+1}),Object(i.jsx)("li",{onClick:function(){e.props.selectTrend(t,s+c+1)},children:t},c)]})}));return Object(i.jsx)("div",{className:"trendmenublock",children:Object(i.jsx)("ul",{children:c})})}(this.state.trends.slice(this.state.firstTrend,this.state.firstTrend+5),this.state.firstTrend);return Object(i.jsxs)("div",{className:"TrendList",children:[Object(i.jsx)("h2",{children:"Trends"}),Object(i.jsx)("h6",{children:"Quick Access"}),Object(i.jsx)("p",{className:"tweet_count",children:"Start here by Selecting a Trend"}),Object(i.jsxs)("div",{className:"menu-bar",children:[Object(i.jsx)("button",{className:"left_button",onClick:this.decreaseTrend,children:" "}),t,Object(i.jsx)("button",{className:"right_button",onClick:this.increaseTrend,children:" "})]})]})}}]),s}(c.Component),y=(s(78),s.p+"static/media/loading.df1e3eaf.gif"),k=function(e){Object(b.a)(s,e);var t=Object(u.a)(s);function s(){var e;return Object(l.a)(this,s),(e=t.call(this)).state={wordcloudURL:"",sentimentURL:"",links:{},keywords:{},tweetCount:0,finishedLoading:!1,errorWhileLoading:!1},e.getStats=e.getStats.bind(Object(h.a)(e)),e.showLinks=e.showLinks.bind(Object(h.a)(e)),e.createTokenTable=e.createTokenTable.bind(Object(h.a)(e)),e}return Object(j.a)(s,[{key:"getStats",value:function(){var e=Object(g.a)(w.a.mark((function e(t){var s,i=this;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:s="http://localhost:5000/analyze_trend?trend="+encodeURIComponent(t),this.props.demoMode&&(s="http://localhost:5000/"+encodeURIComponent(t)+".json"),_.a.get(s).then((function(e){i.setState({links:e.data.links}),i.setState({keywords:e.data.keywords}),i.setState({wordcloudURL:"http://localhost:5000/"+encodeURIComponent(t)+"_wordcloud.png"}),i.setState({sentimentURL:"http://localhost:5000/"+encodeURIComponent(t)+"_sentiment_pie_chart_gervader.png"}),i.setState({tweetCount:e.data.tweet_count}),i.setState({finishedLoading:!0})})).catch((function(e){console.log(e),i.setState({errorWhileLoading:!0})}));case 3:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()},{key:"showLinks",value:function(){if(0===Object.keys(this.state.links).length)return"LINKS";var e=[];for(var t in this.state.links){var s=this.state.links[t],c=Object(i.jsxs)("tr",{children:[Object(i.jsx)("td",{children:s}),Object(i.jsx)("td",{children:Object(i.jsx)("a",{href:t,children:t})})]});e.push(c)}return e}},{key:"createTokenTable",value:function(){if(0===Object.keys(this.state.keywords).length)return"KEYWORDS";var e=[],t=1;for(var s in this.state.keywords){var c=this.state.keywords[s],n=Object(i.jsxs)("tr",{children:[Object(i.jsx)("td",{children:t}),Object(i.jsxs)("td",{children:[s," ",Object(i.jsxs)("p",{children:["(",c,")"]})]})]});t+=1,e.push(n)}return e}},{key:"componentDidMount",value:function(){this.props.trend&&this.getStats(this.props.trend)}},{key:"componentDidUpdate",value:function(e){this.props.trend&&this.props.trend!==e.trend&&(this.setState({errorWhileLoading:!1}),this.getStats(this.props.trend),this.setState({finishedLoading:!1}))}},{key:"render",value:function(){var e;return e=this.state.finishedLoading?Object(i.jsxs)("div",{children:[Object(i.jsxs)("h6",{children:[this.props.id,".  ",this.props.trend]}),Object(i.jsxs)("p",{className:"tweet_count",children:["based on ",this.state.tweetCount," tweets"]}),Object(i.jsxs)("div",{className:"first_row",children:[Object(i.jsxs)("div",{className:"topic_words_wrapper",children:[Object(i.jsx)("h3",{children:"Topic Words"}),Object(i.jsxs)("table",{children:[Object(i.jsxs)("tr",{children:[Object(i.jsx)("th",{children:"#"}),Object(i.jsxs)("th",{children:["Top Words ",Object(i.jsx)("p",{children:" (Score)"})]})]}),this.createTokenTable()]})]}),Object(i.jsxs)("div",{className:"wordcloud_wrapper",children:[Object(i.jsx)("h3",{children:"Wordcloud"}),Object(i.jsx)("img",{className:"wordcloud",src:this.state.wordcloudURL,alt:""})]})]}),Object(i.jsxs)("div",{className:"second_row",children:[Object(i.jsxs)("div",{className:"sentiment_wrapper",children:[Object(i.jsx)("h3",{children:"Trend Sentiment"}),Object(i.jsx)("img",{className:"sentiment",src:this.state.sentimentURL,alt:""})]}),Object(i.jsx)("div",{className:"categories_links_wrapper",children:Object(i.jsxs)("div",{className:"links_wrapper",children:[Object(i.jsx)("h3",{children:"Top Links"}),Object(i.jsxs)("table",{children:[Object(i.jsxs)("tr",{children:[Object(i.jsx)("th",{children:"#"}),Object(i.jsx)("th",{children:"Top Links"})]}),this.showLinks()]})]})})]})]}):Object(i.jsx)("div",{className:"loading",children:Object(i.jsx)("img",{src:y,alt:"",height:"40",width:"40"})}),this.state.errorWhileLoading&&(e=Object(i.jsx)("h3",{children:"Error while loading data from backend!"})),Object(i.jsx)("div",{className:"TrendStats",children:e})}}]),s}(c.Component),S=(s(79),function(e){Object(b.a)(s,e);var t=Object(u.a)(s);function s(){var e;return Object(l.a)(this,s),(e=t.call(this)).selectTrend=function(t,s){e.setState({activeTrend:t}),e.setState({showStats:!0}),e.setState({id:s})},e.state={activeTrend:"",showStats:!1,demoMode:!1,id:0},e.selectTrend=e.selectTrend.bind(Object(h.a)(e)),e}return Object(j.a)(s,[{key:"render",value:function(){return Object(i.jsxs)("div",{className:"results",children:[Object(i.jsx)(N,{selectTrend:this.selectTrend,demoMode:this.state.demoMode}),this.state.showStats&&Object(i.jsx)(k,{trend:this.state.activeTrend,id:this.state.id,demoMode:this.state.demoMode})]})}}]),s}(c.Component)),C=(s(80),function(e){Object(b.a)(s,e);var t=Object(u.a)(s);function s(){var e;return Object(l.a)(this,s),(e=t.call(this)).state={showResults:!1},e.showResults=e.showResults.bind(Object(h.a)(e)),e}return Object(j.a)(s,[{key:"showResults",value:function(){m()(this.results,{offset:0,align:"top",duration:1500})}},{key:"render",value:function(){var e=this;return Object(i.jsxs)("div",{className:"wrapper",children:[Object(i.jsx)(p.a,{children:Object(i.jsx)("title",{children:"Twitter Trend Analytics"})}),Object(i.jsxs)("div",{className:"hero_wrapper",children:[Object(i.jsx)(x,{}),Object(i.jsx)("h1",{children:"Consumer-Based Decision Aid Of The Top 50 German Twitter Trends"}),Object(i.jsx)("button",{onClick:this.showResults})]}),Object(i.jsx)("section",{ref:function(t){e.results=t},children:Object(i.jsx)(S,{})}),Object(i.jsx)(f,{})]})}}]),s}(c.Component)),A=(s(81),s.p+"static/media/headertext.df3e7990.png"),L=s.p+"static/media/pipeline.e26b223e.png";var I=function(){return Object(i.jsxs)("div",{className:"aboutproject",children:[Object(i.jsx)(p.a,{children:Object(i.jsx)("title",{children:"About the Project"})}),Object(i.jsxs)("div",{className:"hero_wrapper_about",children:[Object(i.jsx)(x,{}),Object(i.jsxs)("div",{className:"project",children:[Object(i.jsx)("img",{className:"heading",src:A,alt:"Our Project"}),Object(i.jsx)("p",{children:"Twitter trends are increasingly becoming people\u2019s first choice when they want to inform themselves about whats happening in the world. Millions of messages are appearing every day about people\u2019s lives, opinions on a variety of topics and latest discussions."})]}),Object(i.jsxs)("div",{className:"ap_motivation",children:[Object(i.jsx)("h4",{children:"Our Motivation"}),Object(i.jsx)("p",{children:"Even for twitter users that spend multiple hours per day on twitter, it can be hard to get a solid overview and background information about the latest twitter trends. This can be considered as a big data challenge, and it is difficult and time consuming for users to go through enough tweets for every trend to be able to make a good decision which trend is of relevance. In this research, we developed a model that provides decision guidance in terms of the relevance of the twitter top 50 trend using textual features. The results of this project can help twitter users to get faster to the trends they are appealed to most, and to get a first insight to all trends and their resonance in the community at a glance."})]}),Object(i.jsxs)("div",{className:"ap_topic_words",children:[Object(i.jsx)("h4",{children:"Feature: Topic Words"}),Object(i.jsx)("p",{children:"To get a quick overview about the different themes in a trend, the Topic Words feature uses topic extraction to show you what words are most commonly used in that specific tweet. This feature helps you to stay up to date with all the discussion happening around a topic."})]}),Object(i.jsxs)("div",{className:"ap_wordcloud",children:[Object(i.jsx)("h4",{children:"Feature: Wordcloud"}),Object(i.jsx)("p",{children:"In a world of colourful pictures a visualisation of the data is not allowed to be missing. This feature shows you the most used words by creating a word cloud out of them."})]}),Object(i.jsxs)("div",{className:"ap_sentiment",children:[Object(i.jsx)("h4",{children:"Feature: Trend Sentiment"}),Object(i.jsx)("p",{children:"Our Sentiment Analysis provides a quick overview of what emotions are subjectively perceived about a trend in percentages via a pie chart. It is based on a ruled-based system that operates on a predefined lexicon."})]}),Object(i.jsxs)("div",{className:"ap_top_links",children:[Object(i.jsx)("h4",{children:"Feature: Top Links"}),Object(i.jsx)("p",{children:"This feature extracts the most called links of a specific trend and lists them, providing a useful summary for further research."})]}),Object(i.jsxs)("div",{className:"pipeline",children:[Object(i.jsx)("h4",{children:"Feature: Pipeline"}),Object(i.jsxs)("div",{className:"pipeline_content",children:[Object(i.jsxs)("div",{className:"pipeline_content_top",children:[Object(i.jsx)("img",{className:"pipeline_graph",src:L,alt:"Visualization of Pipeline"}),Object(i.jsxs)("div",{children:[Object(i.jsx)("p",{children:"The pipeline processes the data in the following steps:"}),Object(i.jsx)("p",{children:"1. The get_links_from_tweet function searches for all links in a tweet and counts them in a dict."}),Object(i.jsx)("p",{children:"2. The remove_numbers_and_links function deletes all numbers, links and removes underscores, because we encountered a problem where they are present in the word cloud."})]})]}),Object(i.jsx)("p",{children:"3. In the function clean_tweets all non-alphabetic characters are removed and all is set in lower case."}),Object(i.jsx)("p",{children:"4. Here it removes all stop words. We added a additional stop words, because twitter users use specific twitter abbreviations that do not offer any value for us."}),Object(i.jsx)("p",{children:"5. After removing the stop words some tokens where left with one char or even empty, so it removes them in this step."}),Object(i.jsx)("p",{children:"6. In this step it removes the empty lists that remained after the removal of one char and empty tokens."}),Object(i.jsx)("p",{children:"7. Finally it adds all words in a dict and counts them."})]})]})]}),Object(i.jsx)(f,{})]})};s(82);var P=function(){return Object(i.jsx)("div",{className:"mobile",children:Object(i.jsx)("h3",{children:"Site is currently not available on mobile"})})},U=(s(83),s.p+"static/media/contact_headertext.0dc1546d.png");var R=function(){return Object(i.jsxs)("div",{className:"contact",children:[Object(i.jsx)(p.a,{children:Object(i.jsx)("title",{children:"Contact"})}),Object(i.jsxs)("div",{className:"hero_wrapper_contact",children:[Object(i.jsx)(x,{}),Object(i.jsx)("img",{className:"heading",src:U,alt:"Contact Us"}),Object(i.jsxs)("form",{children:[Object(i.jsxs)("div",{className:"input",children:[Object(i.jsx)("h5",{children:"Name"}),Object(i.jsx)("input",{type:"text",name:"",placeholder:"Your Name..."})]}),Object(i.jsxs)("div",{className:"input",children:[Object(i.jsx)("h5",{children:"email"}),Object(i.jsx)("input",{type:"text",name:"",placeholder:"Your Email..."})]}),Object(i.jsxs)("div",{className:"input",children:[Object(i.jsx)("h5",{children:"message"}),Object(i.jsx)("div",{className:"message_spacing",children:Object(i.jsx)("textarea",{className:"input_message",rows:"5",name:"",placeholder:"Your message..."})})]}),Object(i.jsx)("div",{className:"submit_placing",children:Object(i.jsx)("input",{className:"submit_contact",type:"submit",value:"Submit"})})]})]}),Object(i.jsx)(f,{})]})};s(84);var M=function(){return Object(i.jsxs)("div",{className:"demo",children:[Object(i.jsx)(p.a,{children:Object(i.jsx)("title",{children:"Demo mode"})}),Object(i.jsxs)("div",{className:"hero_wrapper_demo",children:[Object(i.jsx)(x,{}),Object(i.jsx)("div",{className:"demo_text",children:Object(i.jsx)("p",{children:"We run the site in demo mode, because our twitter API has a limit on how many tweets we can scrape. If our site would function normally every visit would trigger a new scrape of the most recent trends, which would download thousands of tweets per trend. That means that in a short amount of time we would reach out limit, set by Twitter. Therefore we decided, that we would scrape trends when something interesting is happening and use this data to feed our algorithm. "})})]}),Object(i.jsx)(f,{})]})},W=(s(85),s.p+"static/media/aboutus_headertext.0777aa43.png");var D=function(){return Object(i.jsxs)("div",{className:"about_us",children:[Object(i.jsx)(p.a,{children:Object(i.jsx)("title",{children:"About Us"})}),Object(i.jsxs)("div",{className:"hero_wrapper_about_us",children:[Object(i.jsx)(x,{}),Object(i.jsx)("img",{className:"heading_aboutus",src:W,alt:"About Us"}),Object(i.jsxs)("div",{className:"one_of_us",children:[Object(i.jsx)("h4",{children:"Maximilian Sch\xf6neberger"}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Course of Study:"}),Object(i.jsx)("p",{children:"Computer Science, B.Sc. 100%"})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Interests:"}),Object(i.jsx)("p",{children:"Medical Informatics, Algorithm & Datastructures, UI Implementation"})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Contributions:"}),Object(i.jsx)("p",{children:"Backend-Coordination, Twitter-Scraper, Pipeline assisted, Website UI & API coded"})]})]}),Object(i.jsxs)("div",{className:"one_of_us",children:[Object(i.jsx)("h4",{children:"Jan Straub"}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Course of Study:"}),Object(i.jsx)("p",{children:"Computer Science, B.Sc. 100%"})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Interests:"}),Object(i.jsx)("p",{children:"Computer Graphics"})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Contributions:"}),Object(i.jsx)("p",{children:"Wrote pipeline, word cloud, topic modeling, About the Project/About Us Page Content, Video Script"})]})]}),Object(i.jsxs)("div",{className:"one_of_us",children:[Object(i.jsx)("h4",{children:"Paavo Streibich"}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Course of Study:"}),Object(i.jsx)("p",{children:"Computer Science, B.Sc. 100%"})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Interests:"}),Object(i.jsx)("p",{children:"Algorithm & Datastructures"})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Contributions:"}),Object(i.jsx)("p",{children:"Pipeline assiested, Tests developed, About the Project/ About Us Page Content, Video Script"})]})]}),Object(i.jsxs)("div",{className:"one_of_us",children:[Object(i.jsx)("h4",{children:"Robin Viellieber"}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Course of Study:"}),Object(i.jsx)("p",{children:"Scientific Computing, M.Sc."})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Interests:"}),Object(i.jsx)("p",{children:"Computer Vision, Statistical Learning"})]}),Object(i.jsxs)("div",{className:"au_item",children:[Object(i.jsx)("p",{children:"Contributions:"}),Object(i.jsx)("p",{children:"Pipeline assisted, Sentiment Analysis, Website Design, About the Project/ About Us Page Content, Video Script, Video Edit"})]})]})]}),Object(i.jsx)(f,{})]})};var F=function(){return Object(i.jsx)(o.a,{children:Object(i.jsxs)("div",{className:"App",children:[Object(i.jsx)(P,{}),Object(i.jsxs)(d.d,{children:[Object(i.jsx)(d.b,{path:"/",exact:!0,component:C}),Object(i.jsx)(d.b,{path:"/aboutproject",component:I}),Object(i.jsx)(d.b,{path:"/aboutus",component:D}),Object(i.jsx)(d.b,{path:"/contact",component:R}),Object(i.jsx)(d.b,{path:"/demo",component:M}),Object(i.jsx)(d.a,{to:"/"})]})]})})},B=function(e){e&&e instanceof Function&&s.e(3).then(s.bind(null,87)).then((function(t){var s=t.getCLS,i=t.getFID,c=t.getFCP,n=t.getLCP,r=t.getTTFB;s(e),i(e),c(e),n(e),r(e)}))};a.a.render(Object(i.jsx)(n.a.StrictMode,{children:Object(i.jsx)(F,{})}),document.getElementById("root")),B()}},[[86,1,2]]]);
//# sourceMappingURL=main.a2bb9fb5.chunk.js.map