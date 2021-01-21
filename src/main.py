import os
import nltk
import json
import requests
from operator import itemgetter
from pipeline import clean_tweets
from pipeline import get_links_from_tweet
from get_tweets import save_trend_to_storage
from build_wordcloud import create_and_save_wordcloud_to_storage
from build_topic_modeling import perform_LDA

#Hyperparameter
TOTAL_AMOUNT = 200


def analyze_trend(trend):

    save_trend_to_storage(trend, TOTAL_AMOUNT)

    data = clean_tweets(trend + '.json')

    links = get_links_from_tweet(trend + '.json')
    top_links = dict(sorted(links.items(), key = itemgetter(1), reverse = True)[:5])
    unshort_top_links = {}
    for url in top_links.keys():
        r = requests.head(url, allow_redirects=True)
        unshort_top_links[r.url] = top_links[url]

    create_and_save_wordcloud_to_storage(trend, data)
    topic_words = perform_LDA(trend, data)
    topic_words.update((k, str(v)) for k, v in topic_words.items())

    with open(os.path.dirname(os.path.abspath(__file__)) + '/../storage/jsons/' + trend + ".json") as file:
        tweet_count = len(json.load(file))

    results_json = {"trend" : trend, "tweet_count" : tweet_count, "keywords": topic_words, "sentiment" : "TBI", "links" : unshort_top_links}

    return results_json



if __name__ == "__main__":

    print("You are doing great! :)")
