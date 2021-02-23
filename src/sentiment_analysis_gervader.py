import matplotlib.pyplot as plt
import os
from GerVADER.vaderSentimentGER import SentimentIntensityAnalyzer

from pipeline import read_from_storage

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))


def sentiment_analysis(trend_from_storage):
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

    # analyze each individual tweet with GerVader
    analyzer = SentimentIntensityAnalyzer()
    for tweet in tweets_of_trend:
        score = analyzer.polarity_scores(tweet)
        neg, neu, pos = score["neg"], score["neu"], score["pos"]

        # increment the positive/ neutral/ negative counter depending on which score is the highest
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


def create_pie_chart(trend_from_storage, percentage_positive, percentage_neutral, percentage_negative):
    """
    IN:
    trend_from_storage (string): one trend in the form "<trend>.json"
    percentage_positive (float): the percentage of positive tweets of this trend
    percentage_neutral (float): the percentage of neutral tweets of this trend
    percentage_negative (float): the percentage of negative tweets of this trend
    OUT:
    None (png's created in storage/results)
    """

    colors = ["lightskyblue", "steelblue", "midnightblue"]
    labels = 'Positive', 'Neutral', 'Negative'
    sizes = [percentage_positive, percentage_neutral, percentage_negative]

    # create pie chart plot and wedges
    fig, ax = plt.subplots()
    wedges, text, autotext = ax.pie(sizes,
        colors=colors,
        autopct='%1.1f%%',
        textprops=dict(color='white'),
        wedgeprops=dict(width=0.7,
        edgecolor='lightgray'),
        pctdistance=0.8,
        startangle=120)

    # various parameters to change the visual of the pie chart
    plt.setp(wedges, width=0.40)
    fig.set_facecolor('darkblue')
    ax.axis('equal')
    legend = ax.legend(wedges, labels,
        title=None,
        loc="upper left",
        bbox_to_anchor=(-0.1, 1.1),
        fontsize=13,
        fancybox=True,
        facecolor='dimgray',
        edgecolor='darkgray',
        framealpha=0.5)

    # change color of legend text
    for text in legend.get_texts():
        text.set_color('gainsboro')

    # save figure in storage
    trend_name = str(trend_from_storage).removesuffix('.json')
    save_path = current_dir + '/../storage/results/' + trend_name + '_sentiment_pie_chart_gervader.png'
    fig.savefig(save_path, transparent=True)
    plt.close(fig)
