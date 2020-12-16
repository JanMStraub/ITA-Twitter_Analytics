## Requirements
Make sure to download all required packages first, i.e. run:
```
pip install -r requirements.txt
```
and please also run:

```
python -m spacy download de
```

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

## Project State
We implemented our pipeline and scraper for the german twitter trends.
For the next milestone we are going to write the machine learning part and the website where we will present our results.

First, we created a scraper that scrapes for each of the top 50 german Twitter trends n tweets, where n is a hyperparameter.
Our pipeline then takes the scraped tweets and first cleanes the data from all non-alphabetical characters. Secondly, we used the CountVectorizer from sklearn to remove the stop words and set all letters to their lower-cased form. Thirdly we tokenize the data and add it to a dictionary. Then we lemmatize the words and count them again in a new dictionary, and achieve the final preprocessed form of our data.
Furthermore, we followed the advice from our tutor and only used lemmatization and skipped stemming. We found out that german lemmatization is possible via a package from the spacey module. Also, we pursued his guidance and focused on the text analytics part, and reserved the sentiment analysis for later in case we choose we want to invest more in that direction.
We also tested the pipeline with our data and everything seems to work as intended. In addition, the lemmatizer also seems to work properly, since most morphological variations were correctly lemmatized to an identical basic word.


## Data Analysis
At first, we planed on using getdaytrends.com to access the top 50 Twitter trends, but after we did more research about the Twitter API, we realized that we can directly extract the trends from their API. Therefore we discarded our original plan to use getdaytrends.com and instead directly use the Twitter API, which provides a specific number of german tweets for a given topic in a .json file.
In this file we get the creation timestamp, the twitter id, the language abbreviation, and the tweet itself.
As an example:
```
[
  {
    "created_at": "2020-12-06T19:15:04.000Z",
    "id": "1335664071623004167",
    "lang": "de",
    "text": "Zwei Rennen in Bahrain, zweimal spektakul\u00e4r bis chaotisch. #F1 #Formel1"
  },
  ...
]
```

## relationship model
![relationship model](https://github.com/JanMStraub/ITA-Twitter_Analytics/blob/main/relationship_model.png)


## Contributions
 * Maximilian wrote the scraper and got in contact with Twitter to get access to their API.
 * Maximilian, Robin, Paavo, and Jan worked together to build the pipeline.
 * Robin and Paavo worked on the relationship model.
