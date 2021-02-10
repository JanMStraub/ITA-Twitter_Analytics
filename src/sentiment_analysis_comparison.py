import matplotlib.pyplot as plt
import os
import pandas as pd
from GerVADER.vaderSentimentGER import SentimentIntensityAnalyzer as SentimentIntensityAnalyzer_GerVADER
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SentimentIntensityAnalyzer_VADER
from textblob import TextBlob

from pipeline import read_from_storage

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]

def sentiment_analysis_Vader(trend_from_storage):
    """
    IN:
    trend_from_storage (string): one trend in the form "<trend>.json"
    OUT:
    percentage_positive (float): the percentage of positive tweets of this trend
    percentage_neutral (float): the percentage of neutral tweets of this trend
    percentage_negative (float): the percentage of negative tweets of this trend
    """

    positive_tweets = 0
    negative_tweets = 0
    neutral_tweets = 0

    tweets_of_trend = read_from_storage(trend_from_storage)

    # analyze each individual tweet with Vader
    analyzer = SentimentIntensityAnalyzer_VADER()

    sentiment_per_tweet = []

    for tweet in tweets_of_trend[10:20]:
        score = analyzer.polarity_scores(tweet)
        neg, neu, pos = score["neg"], score["neu"], score["pos"]

        if neg > pos:
            negative_tweets += 1
            sentiment_per_tweet.append('negative')
        elif pos > neg:
            positive_tweets += 1
            sentiment_per_tweet.append('positive')
        elif pos == neg:
            neutral_tweets += 1
            sentiment_per_tweet.append('neutral')    
    
    return sentiment_per_tweet

def sentiment_analysis_GerVADER(trend_from_storage):
    """
    IN:
    trend_from_storage (string): one trend in the form "<trend>.json"
    OUT:
    percentage_positive (float): the percentage of positive tweets of this trend
    percentage_neutral (float): the percentage of neutral tweets of this trend
    percentage_negative (float): the percentage of negative tweets of this trend
    """

    positive_tweets = 0
    negative_tweets = 0
    neutral_tweets = 0

    tweets_of_trend = read_from_storage(trend_from_storage)

    # analyze each individual tweet with GerVADER
    analyzer = SentimentIntensityAnalyzer_GerVADER()

    sentiment_per_tweet = []

    for tweet in tweets_of_trend[10:20]:
        score = analyzer.polarity_scores(tweet)
        neg, neu, pos = score["neg"], score["neu"], score["pos"]

        if neg > pos:
            negative_tweets += 1
            sentiment_per_tweet.append('negative')
        elif pos > neg:
            positive_tweets += 1
            sentiment_per_tweet.append('positive')
        elif pos == neg:
            neutral_tweets += 1
            sentiment_per_tweet.append('neutral')     
    
    return sentiment_per_tweet

def sentiment_analysis_TextBlob(trend_from_storage):
    """
    IN:
    trend_from_storage (string): one trend in the form "<trend>.json"
    OUT:
    percentage_positive (float): the percentage of positive tweets of this trend
    percentage_neutral (float): the percentage of neutral tweets of this trend
    percentage_negative (float): the percentage of negative tweets of this trend
    percentage_no_sentiment (float): the percentage of tweets with zero sentiment according to textblob of this trend 
    """

    positive_tweets = 0
    negative_tweets = 0
    neutral_tweets = 0
    no_sentiment_tweets = 0

    tweets_of_trend = read_from_storage(trend_from_storage)

    # analyze each individual tweet with TextBlob

    sentiment_per_tweet = []

    for tweet in tweets_of_trend[10:20]:
        analysis = TextBlob(tweet)
        score = analysis.sentiment.polarity
        if score > 0.1:
            sentiment_per_tweet.append('positive')
            positive_tweets += 1
        elif score > -0.1 and score < 0.0:
            neutral_tweets += 1
            sentiment_per_tweet.append('neutral')
        elif score == 0.0:
            no_sentiment_tweets += 1
            sentiment_per_tweet.append('no sentiment')
        else:            
            negative_tweets += 1
            sentiment_per_tweet.append('negative')
    
    return sentiment_per_tweet

if __name__ == '__main__':

    for trend in trends:
        sentiment_vader = sentiment_analysis_Vader(trend)
        sentiment_gervader = sentiment_analysis_GerVADER(trend)
        sentiment_textblob = sentiment_analysis_TextBlob(trend)

        tweets_of_trend = read_from_storage(trend)

        our_labels = ['negative', 'neutral', 'negative', 'neutral', 'negative', 'negative', 'neutral', 'negative', 'negative', 'negative']

        comparison_dict = {
            "tweet": tweets_of_trend[10:20],
            "vader": sentiment_vader,
            "gervader": sentiment_gervader,
            "textblob": sentiment_textblob,
            "ourlabels": our_labels
        }

        comparison_df = pd.DataFrame(comparison_dict)
        pd.options.display.max_colwidth = 100
        print(comparison_df)

    print("You are doing great! :)")