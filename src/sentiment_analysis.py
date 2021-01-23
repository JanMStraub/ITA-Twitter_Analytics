# this is inspired from https://towardsdatascience.com/step-by-step-twitter-sentiment-analysis-in-python-d6f650ade58d
from textblob import TextBlob
import matplotlib.pyplot as plt
import os
import nltk
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from pipeline import read_from_storage

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]

def sentiment_analysis(trends):
    """
    IN:
    trends (list): list of trends in the form "<trend>.json"
    OUT:
    percentage_positive (list): list where the i-th element is the percentage of positive tweets for the i-th trend
    percentage_neutral (list): list where the i-th element is the percentage of neutral tweets for the i-th trend
    percentage_negative (list): list where the i-th element is the percentage of negative tweets for the i-th trend
    """

    percentage_positive = []
    percentage_neutral = []
    percentage_negative = []

    for trend in trends:
        positive_tweets = 0
        negative_tweets = 0
        neutral_tweets = 0

        tweets_of_trend = read_from_storage(trend)

        # analyze each individual tweet with TextBlob
        for tweet in tweets_of_trend:
            tweet_analysis = TextBlob(tweet)
            score = SentimentIntensityAnalyzer().polarity_scores(tweet)
            neg, neu, pos = score["neg"], score["neu"], score["pos"]

            if neg > pos:
                negative_tweets += 1
            elif pos > neg:
                positive_tweets += 1
            elif pos == neg:
                neutral_tweets += 1
        
        # calculate the percentage of positive/ neutral/ negative tweets per trend
        percentage_positive.append(positive_tweets/len(tweets_of_trend))
        percentage_neutral.append(neutral_tweets/len(tweets_of_trend))
        percentage_negative.append(negative_tweets/len(tweets_of_trend))        
    
    return percentage_positive, percentage_neutral, percentage_negative

def create_pie_chart(percentage_positive, percentage_neutral, percentage_negative):
    """
    IN:
    percentage_positive (list): list where the i-th element is the percentage of positive tweets for the i-th trend
    percentage_neutral (list): list where the i-th element is the percentage of neutral tweets for the i-th trend
    percentage_negative (list): list where the i-th element is the percentage of negative tweets for the i-th trend
    OUT:
    None (png's created in storage/results)
    """

    for index, trend in enumerate(trends):
        colors = ["limegreen", "orange", "firebrick"]
        labels = 'Positive', 'Neutral', 'Negative'
        sizes = [percentage_positive[index], percentage_neutral[index], percentage_negative[index]]

        fig, ax = plt.subplots()
        wedges, text, autotext =  ax.pie(sizes,
            colors=colors,
            autopct='%1.1f%%',
            textprops=dict(color='white'),
            wedgeprops = dict(width = 0.7,
            edgecolor = 'lightgray'),
            pctdistance = 0.8,
            startangle=120)

        plt.setp(wedges, width = 0.40)
        fig.set_facecolor('darkblue')
        ax.axis('equal')
        legend = ax.legend(wedges, labels,
            title=None,
            loc="upper left",
            bbox_to_anchor=(-0.1, 1.1),
            fontsize = 13,
            fancybox = True,
            facecolor = 'dimgray',
            edgecolor = 'darkgray',
            framealpha = 0.5)

        # change color of legend text      
        for text in legend.get_texts():
            text.set_color('gainsboro')

        # save figure in storage
        save_path = current_dir + '/../storage/results/' + 'sentiment_pie_chart_' + str(index) + '.png'
        fig.savefig(save_path, transparent = True)
        plt.close(fig)


if __name__ == '__main__':

    percentage_positive, percentage_neutral, percentage_negative = sentiment_analysis(trends)
    create_pie_chart(percentage_positive, percentage_neutral, percentage_negative)

    print("You are doing great! :)")