import os
import json
import requests
from operator import itemgetter
from pipeline import clean_tweets
from pipeline import get_links_from_tweet
from get_tweets import save_trend_to_storage
from build_wordcloud import create_and_save_wordcloud_to_storage
from build_topic_modeling import perform_LDA
from sentiment_analysis import sentiment_analysis, create_pie_chart

# Hyperparameter
TOTAL_AMOUNT = 200


def analyze_trend(trend):
    """
    IN: trend(string)
    OUT: results_json(dict)
    """

    save_trend_to_storage(trend, TOTAL_AMOUNT)  # save tweets to storage

    data = clean_tweets(trend + '.json')  # perform cleaning

    # extract top 5 links and unshorten them
    links = get_links_from_tweet(trend + '.json')
    top_links = dict(sorted(links.items(), key=itemgetter(1), reverse=True)[:5])
    unshort_top_links = {}
    for url in top_links.keys():
        r = requests.head(url, allow_redirects=True)
        unshort_top_links[r.url] = top_links[url]

    # create worldcloud and perform LDA
    create_and_save_wordcloud_to_storage(trend, data)
    topic_words = perform_LDA(trend + '.json', data)
    topic_words.update((k, str(v)) for k, v in topic_words.items())

    # perform sentiment analysis
    percentage_positive, percentage_neutral, percentage_negative = sentiment_analysis(trend + '.json')
    create_pie_chart(trend + '.json', percentage_positive, percentage_neutral, percentage_negative)

    # get number of analysed tweets
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../storage/jsons/' + trend + ".json") as file:
        tweet_count = len(json.load(file))

    # create results dict(to be used as json)
    results_json = {"trend": trend,
                    "tweet_count": tweet_count,
                    "keywords": topic_words,
                    "sentiment": "TBI",
                    "links": unshort_top_links
                    }

    with open(os.path.dirname(os.path.abspath(__file__)) + '/../storage/results/' + trend + ".json", 'w') as outfile:
        json.dump(results_json, outfile, indent=4)

    return results_json


if __name__ == "__main__":

    analyze_trend("#sterntv")

    print("You are doing great! :)")
