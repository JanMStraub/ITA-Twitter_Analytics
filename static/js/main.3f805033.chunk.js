(this.webpackJsonpwebui=this.webpackJsonpwebui||[]).push([[0],{45:function(e,t,s){},54:function(e,t,s){},57:function(e,t,s){},59:function(e,t,s){},78:function(e,t,s){},79:function(e,t,s){},80:function(e,t,s){},81:function(e,t,s){},82:function(e,t,s){},83:function(e,t,s){},84:function(e,t,s){},85:function(e,t,s){"use strict";s.r(t);var i=s(0),n=s(1),c=s.n(n),a=s(23),r=s.n(a),l=(s(45),s(9)),o=s(3),d=s(11),u=s(12),j=s(5),h=s(15),m=s(14),b=s(13),p=s(38),O=s.n(p);s(54);var x=function(){return Object(i.jsxs)("header",{children:[Object(i.jsx)("div",{className:"navigation",children:Object(i.jsx)("nav",{children:Object(i.jsxs)("ul",{children:[Object(i.jsx)(l.b,{to:"/",children:Object(i.jsx)("li",{children:"Analytics"})}),Object(i.jsx)(l.b,{to:"/aboutproject",children:Object(i.jsx)("li",{children:"About The Project"})}),Object(i.jsx)(l.b,{to:"/aboutus",children:Object(i.jsx)("li",{children:"About US"})})]})})}),Object(i.jsx)("div",{className:"names",children:Object(i.jsxs)("ul",{children:[Object(i.jsx)("li",{children:"Maximilian Sch\xf6neberger"}),Object(i.jsx)("li",{children:"Jan Straub"}),Object(i.jsx)("li",{children:"Paavo Streibich"}),Object(i.jsx)("li",{children:"Robin Viellieber"})]})}),Object(i.jsx)("div",{className:"icons",children:Object(i.jsx)("nav",{children:Object(i.jsxs)("ul",{children:[Object(i.jsx)(l.b,{to:"/contact",children:Object(i.jsx)("li",{children:"Contact"})}),Object(i.jsx)("li",{children:Object(i.jsx)("a",{href:"https://github.com/JanMStraub/ITA-Twitter_Analytics/",children:"Github"})})]})})})]})};s(57);var v=function(){return Object(i.jsxs)("footer",{children:[Object(i.jsxs)("ul",{children:[Object(i.jsx)(l.b,{to:"/imprint",children:Object(i.jsx)("li",{children:"Imprint"})}),Object(i.jsx)(l.b,{to:"/privacy",children:Object(i.jsx)("li",{children:"Privacy Notice"})}),Object(i.jsx)(l.b,{to:"/agb",children:Object(i.jsx)("li",{children:"AGB'S"})})]}),Object(i.jsx)("ul",{className:"demo_mode_disclaimer",children:Object(i.jsxs)("li",{children:["This site is currently in demo mode. Click ",Object(i.jsx)(l.b,{to:"/demo",children:"here"})," to learn more."]})})]})},f=s(17),g=s.n(f),N=s(19),T=(s(59),s(20)),k=s.n(T),w=function(e){Object(h.a)(s,e);var t=Object(m.a)(s);function s(){var e;return Object(d.a)(this,s),(e=t.call(this)).state={trends:[],firstTrend:0},e.getTrends=e.getTrends.bind(Object(j.a)(e)),e.increaseTrend=e.increaseTrend.bind(Object(j.a)(e)),e.decreaseTrend=e.decreaseTrend.bind(Object(j.a)(e)),e}return Object(u.a)(s,[{key:"getTrends",value:function(){var e=Object(N.a)(g.a.mark((function e(){var t,s=this;return g.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:t="https://dry-sierra-67161.herokuapp.com",this.props.demoMode&&(t+="?demo=True"),k.a.get(t).then((function(e){s.setState({trends:e.data})})).catch((function(e){console.log(e)}));case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"componentDidMount",value:function(){this.getTrends()}},{key:"increaseTrend",value:function(){this.state.firstTrend<45&&this.setState({firstTrend:this.state.firstTrend+5})}},{key:"decreaseTrend",value:function(){this.state.firstTrend>=5&&this.setState({firstTrend:this.state.firstTrend-5})}},{key:"render",value:function(){var e=this,t=function(t,s){var n=t.map((function(t,n){return Object(i.jsxs)("div",{children:[Object(i.jsx)("p",{className:"trendNumber",children:s+n+1}),Object(i.jsx)("li",{onClick:function(){e.props.selectTrend(t,s+n+1)},children:t},n)]})}));return Object(i.jsx)("div",{className:"trendmenublock",children:Object(i.jsx)("ul",{children:n})})}(this.state.trends.slice(this.state.firstTrend,this.state.firstTrend+5),this.state.firstTrend);return Object(i.jsxs)("div",{className:"TrendList",children:[Object(i.jsx)("h2",{children:"Trends"}),Object(i.jsx)("h6",{children:"Quick Access"}),Object(i.jsx)("p",{className:"tweet_count",children:"Start here by Selecting a Trend"}),Object(i.jsxs)("div",{className:"menu-bar",children:[Object(i.jsx)("button",{className:"left_button",onClick:this.decreaseTrend,children:" "}),t,Object(i.jsx)("button",{className:"right_button",onClick:this.increaseTrend,children:" "})]})]})}}]),s}(n.Component),y=(s(78),s.p+"static/media/loading.df1e3eaf.gif"),S=function(e){Object(h.a)(s,e);var t=Object(m.a)(s);function s(){var e;return Object(d.a)(this,s),(e=t.call(this)).state={wordcloudURL:"",sentimentURL:"",links:{},keywords:{},tweetCount:0,finishedLoading:!1,errorWhileLoading:!1},e.getStats=e.getStats.bind(Object(j.a)(e)),e.showLinks=e.showLinks.bind(Object(j.a)(e)),e.createTokenTable=e.createTokenTable.bind(Object(j.a)(e)),e}return Object(u.a)(s,[{key:"getStats",value:function(){var e=Object(N.a)(g.a.mark((function e(t){var s,i=this;return g.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:s="https://dry-sierra-67161.herokuapp.com/analyze_trend?trend="+encodeURIComponent(t),this.props.demoMode&&(s="https://dry-sierra-67161.herokuapp.com/"+encodeURIComponent(t)+".json"),k.a.get(s).then((function(e){i.setState({links:e.data.links}),i.setState({keywords:e.data.keywords}),i.setState({wordcloudURL:"https://dry-sierra-67161.herokuapp.com/"+encodeURIComponent(t)+"_wordcloud.png"}),i.setState({sentimentURL:"https://dry-sierra-67161.herokuapp.com/"+encodeURIComponent(t)+"_sentiment_pie_chart_gervader.png"}),i.setState({tweetCount:e.data.tweet_count}),i.setState({finishedLoading:!0})})).catch((function(e){console.log(e),i.setState({errorWhileLoading:!0})}));case 3:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()},{key:"showLinks",value:function(){if(0===Object.keys(this.state.links).length)return"LINKS";var e=[];for(var t in this.state.links){var s=this.state.links[t],n=Object(i.jsxs)("tr",{children:[Object(i.jsx)("td",{children:s}),Object(i.jsx)("td",{children:Object(i.jsx)("a",{href:t,children:t})})]});e.push(n)}return e}},{key:"createTokenTable",value:function(){if(0===Object.keys(this.state.keywords).length)return"KEYWORDS";var e=[],t=1;for(var s in this.state.keywords){var n=this.state.keywords[s],c=Object(i.jsxs)("tr",{children:[Object(i.jsx)("td",{children:t}),Object(i.jsxs)("td",{children:[s," ",Object(i.jsxs)("p",{children:["(",n,")"]})]})]});t+=1,e.push(c)}return e}},{key:"componentDidMount",value:function(){this.props.trend&&this.getStats(this.props.trend)}},{key:"componentDidUpdate",value:function(e){this.props.trend&&this.props.trend!==e.trend&&(this.setState({errorWhileLoading:!1}),this.getStats(this.props.trend),this.setState({finishedLoading:!1}))}},{key:"render",value:function(){var e;return e=this.state.finishedLoading?Object(i.jsxs)("div",{children:[Object(i.jsxs)("h6",{children:[this.props.id,".  ",this.props.trend]}),Object(i.jsxs)("p",{className:"tweet_count",children:["(based on ",this.state.tweetCount," tweets)"]}),Object(i.jsxs)("div",{className:"first_row",children:[Object(i.jsxs)("div",{className:"topic_words_wrapper",children:[Object(i.jsx)("h3",{children:"Topic Words"}),Object(i.jsxs)("table",{children:[Object(i.jsxs)("tr",{children:[Object(i.jsx)("th",{children:"#"}),Object(i.jsx)("th",{children:"Top Words"})]}),this.createTokenTable()]})]}),Object(i.jsxs)("div",{className:"wordcloud_wrapper",children:[Object(i.jsx)("h3",{children:"Wordcloud"}),Object(i.jsx)("img",{className:"wordcloud",src:this.state.wordcloudURL,alt:""})]})]}),Object(i.jsxs)("div",{className:"second_row",children:[Object(i.jsxs)("div",{className:"sentiment_wrapper",children:[Object(i.jsx)("h3",{children:"Trend Sentiment"}),Object(i.jsx)("img",{className:"sentiment",src:this.state.sentimentURL,alt:""})]}),Object(i.jsx)("div",{className:"categories_links_wrapper",children:Object(i.jsxs)("div",{className:"links_wrapper",children:[Object(i.jsx)("h3",{children:"Top Links"}),Object(i.jsxs)("table",{children:[Object(i.jsxs)("tr",{children:[Object(i.jsx)("th",{children:"#"}),Object(i.jsx)("th",{children:"Top Links"})]}),this.showLinks()]})]})})]})]}):Object(i.jsx)("div",{className:"loading",children:Object(i.jsx)("img",{src:y,alt:"",height:"40",width:"40"})}),this.state.errorWhileLoading&&(e=Object(i.jsx)("h3",{children:"Error while loading data from backend!"})),Object(i.jsx)("div",{className:"TrendStats",children:e})}}]),s}(n.Component),_=(s(79),function(e){Object(h.a)(s,e);var t=Object(m.a)(s);function s(){var e;return Object(d.a)(this,s),(e=t.call(this)).selectTrend=function(t,s){e.setState({activeTrend:t}),e.setState({showStats:!0}),e.setState({id:s})},e.state={activeTrend:"",showStats:!1,demoMode:!0,id:0},e.selectTrend=e.selectTrend.bind(Object(j.a)(e)),e}return Object(u.a)(s,[{key:"render",value:function(){return console.log(this.state.activeTrend),Object(i.jsxs)("div",{className:"results",children:[Object(i.jsx)(w,{selectTrend:this.selectTrend,demoMode:this.state.demoMode}),this.state.showStats&&Object(i.jsx)(S,{trend:this.state.activeTrend,id:this.state.id,demoMode:this.state.demoMode})]})}}]),s}(n.Component)),q=(s(80),function(e){Object(h.a)(s,e);var t=Object(m.a)(s);function s(){var e;return Object(d.a)(this,s),(e=t.call(this)).state={showResults:!1},e.showResults=e.showResults.bind(Object(j.a)(e)),e}return Object(u.a)(s,[{key:"showResults",value:function(){O()(this.results,{offset:0,align:"top",duration:1500})}},{key:"render",value:function(){var e=this;return Object(i.jsxs)("div",{className:"wrapper",children:[Object(i.jsx)(b.a,{children:Object(i.jsx)("title",{children:"Twitter Trend Analytics"})}),Object(i.jsxs)("div",{className:"hero_wrapper",children:[Object(i.jsx)(x,{}),Object(i.jsx)("h1",{children:"Consumer-Based Decision Aid Of The Top 50 German Twitter Trends"}),Object(i.jsx)("button",{onClick:this.showResults})]}),Object(i.jsx)("section",{ref:function(t){e.results=t},children:Object(i.jsx)(_,{})}),Object(i.jsx)(v,{})]})}}]),s}(n.Component)),L=(s(81),s.p+"static/media/headertext.df3e7990.png"),C=s.p+"static/media/pipeline.49a091d9.png";var A=function(){return Object(i.jsxs)("div",{className:"aboutproject",children:[Object(i.jsx)(b.a,{children:Object(i.jsx)("title",{children:"About the Project"})}),Object(i.jsxs)("div",{className:"hero_wrapper_about",children:[Object(i.jsx)(x,{}),Object(i.jsxs)("div",{className:"project",children:[Object(i.jsx)("img",{className:"heading",src:L,alt:"Our Project"}),Object(i.jsx)("p",{children:"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam"})]}),Object(i.jsxs)("div",{className:"motivation",children:[Object(i.jsx)("h4",{children:"Our Motivation"}),Object(i.jsx)("p",{children:"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"})]}),Object(i.jsxs)("div",{className:"description",children:[Object(i.jsx)("h4",{children:"Project Description"}),Object(i.jsx)("p",{children:"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"})]}),Object(i.jsxs)("div",{className:"pipeline",children:[Object(i.jsxs)("div",{children:[Object(i.jsx)("h4",{children:"Beschreibung Pipeline"}),Object(i.jsx)("p",{children:"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."})]}),Object(i.jsx)("img",{className:"pipeline_graph",src:C,alt:"Visualization of Pipeline"})]})]}),Object(i.jsx)(v,{})]})};s(82);var D=function(){return Object(i.jsx)("div",{className:"mobile",children:Object(i.jsx)("h3",{children:"Site is currently not available on mobile"})})},M=(s(83),s.p+"static/media/contact_headertext.0dc1546d.png");var R=function(){return Object(i.jsxs)("div",{className:"contact",children:[Object(i.jsx)(b.a,{children:Object(i.jsx)("title",{children:"Contact"})}),Object(i.jsxs)("div",{className:"hero_wrapper_contact",children:[Object(i.jsx)(x,{}),Object(i.jsx)("img",{className:"heading",src:M,alt:"Contact Us"}),Object(i.jsxs)("form",{children:[Object(i.jsxs)("div",{className:"input",children:[Object(i.jsx)("h5",{children:"Name"}),Object(i.jsx)("input",{type:"text",name:"",placeholder:"Your Name..."})]}),Object(i.jsxs)("div",{className:"input",children:[Object(i.jsx)("h5",{children:"email"}),Object(i.jsx)("input",{type:"text",name:"",placeholder:"Your Email..."})]}),Object(i.jsxs)("div",{className:"input",children:[Object(i.jsx)("h5",{children:"message"}),Object(i.jsx)("div",{className:"message_spacing",children:Object(i.jsx)("textarea",{className:"input_message",rows:"5",name:"",placeholder:"Your message..."})})]}),Object(i.jsx)("div",{className:"submit_placing",children:Object(i.jsx)("input",{className:"submit_contact",type:"submit",value:"Submit"})})]})]}),Object(i.jsx)(v,{})]})};s(84);var I=function(){return Object(i.jsxs)("div",{className:"demo",children:[Object(i.jsx)(b.a,{children:Object(i.jsx)("title",{children:"Demo mode"})}),Object(i.jsxs)("div",{className:"hero_wrapper_demo",children:[Object(i.jsx)(x,{}),Object(i.jsx)("div",{className:"demo_text",children:Object(i.jsx)("p",{children:"This site is in demo mode only because..."})})]}),Object(i.jsx)(v,{})]})};var U=function(){return Object(i.jsx)(l.a,{children:Object(i.jsxs)("div",{className:"App",children:[Object(i.jsx)(D,{}),Object(i.jsxs)(o.d,{children:[Object(i.jsx)(o.b,{path:"/",exact:!0,component:q}),Object(i.jsx)(o.b,{path:"/aboutproject",component:A}),Object(i.jsx)(o.b,{path:"/contact",component:R}),Object(i.jsx)(o.b,{path:"/demo",component:I}),Object(i.jsx)(o.a,{to:"/"})]})]})})},P=function(e){e&&e instanceof Function&&s.e(3).then(s.bind(null,86)).then((function(t){var s=t.getCLS,i=t.getFID,n=t.getFCP,c=t.getLCP,a=t.getTTFB;s(e),i(e),n(e),c(e),a(e)}))};r.a.render(Object(i.jsx)(c.a.StrictMode,{children:Object(i.jsx)(U,{})}),document.getElementById("root")),P()}},[[85,1,2]]]);
//# sourceMappingURL=main.3f805033.chunk.js.map