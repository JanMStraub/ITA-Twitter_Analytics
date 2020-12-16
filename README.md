# Consumer-Based Decision Aid Of The Top 50 German Twitter Trends
Maximilian Schöneberger,
maxschoeneberger@t-online.de

Jan Straub,
jan.straub@stud.uni-heidelberg.de

Paavo Streibich,
kf223@uni-heidelberg.de

Robin Viellieber,
viellieber@stud.uni-heidelberg.de


# Milestone one

## 2 Project State
Currently we implemented our scraper for the german twitter trends and our pipeline. 
We were not able to finish the machine learning part and the website where we will present our results.
In the second part of the project we want to finish the machine learning part and hope to get started with the website.

In our pipeline we firstly clean our data form all non alphabetical characters. Secondly we used the CountVectorizer from sklearn to remove the stop words and set all letters to their lower cased form. Thirdly we tokenize it all and add it to a dictionary. Then we lemmatize the words and count them again in a new dictionary for further use.
Furthermore we listened to the suggestions from our tutor and only used lemmatization. Also we followed his advise and focused on the text analytics part and reserved the sentiment analysis for later use if we got some time left on our hands.
We also tested the pipeline with our data, and the stemmedwordcounts seem as correct as the lemmatizer is good.

## 3 Data Analysis
First we planed on using getdaytrends.com to access the top 50 twitter trends, but after reading more into the twitter API, we realised that we can directly extract the trends from their API. Therefore we discarded our original plan to use getdaytrends.com. The twitter API provides with a specific number of german tweets for a given topic in a .json file. 
As a example:
[
    {
        "created_at": "2020-12-06T19:15:04.000Z",
        "id": "1335664071623004167",
        "lang": "de",
        "text": "Zwei Rennen in Bahrain, zweimal spektakul\u00e4r bis chaotisch. #F1 #Formel1 #Formula1 #SakhirGP  #BahrainGP"
    },
    ...
]

## Contributions
 * Maximilian wrote the scraper and got in contact with Twitter to get access to their API.
 * Maximilian, Paavo, Robin and Jan worked together to built the pipeline.
