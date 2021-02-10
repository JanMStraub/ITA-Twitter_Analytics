import matplotlib.pyplot as plt
import os
from vaderSentimentGER import SentimentIntensityAnalyzer as SentimentIntensityAnalyzer_GerVADER
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SentimentIntensityAnalyzer_VADER
from textblob import TextBlob

from pipeline import read_from_storage

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]

def sentiment_analysis_comparison(trend_from_storage):
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

    # analyze each individual tweet with TextBlob
    #analyzer = SentimentIntensityAnalyzer_GerVADER()
    analyzer = SentimentIntensityAnalyzer_VADER()
    for tweet in tweets_of_trend[:10]:
        print(tweet)
        score = analyzer.polarity_scores(tweet)
        neg, neu, pos = score["neg"], score["neu"], score["pos"]

        if neg > pos:
            negative_tweets += 1
        elif pos > neg:
            positive_tweets += 1
        elif pos == neg:
            neutral_tweets += 1
        
    # calculate the percentage of positive/ neutral/ negative tweets of the trend
    percentage_positive = positive_tweets / len(tweets_of_trend)
    percentage_neutral = neutral_tweets / len(tweets_of_trend)
    percentage_negative = negative_tweets / len(tweets_of_trend)        
    
    return percentage_positive, percentage_neutral, percentage_negative

if __name__ == '__main__':

    for trend in trends:
        percentage_positive, percentage_neutral, percentage_negative = sentiment_analysis_comparison(trend)

    print("You are doing great! :)")