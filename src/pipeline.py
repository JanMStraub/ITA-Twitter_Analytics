import json
import os
import nltk
import re
import spacy

from nltk.corpus import stopwords
from gensim.models.phrases import Phrases, Phraser


def read_from_storage(filename):
    """
    IN:
    file_name (str): one trend in the form "<trend>.json"
    OUT:
    tweets (list): text of all tweets of the trend
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + '/../storage/jsons/' + filename
    tweets = []

    with open(path, 'r') as file:
        tweets_json = json.load(file)
        for tweet in tweets_json:
            tweets.append(tweet["text"])

    return tweets


def count_links(extracted_links):
    """
    IN:
    extracted_links (list): list containing all links in on trend
    OUT:
    counted_links_dict (dict): dict containing number of links and the links itself
    """

    counted_links_dict = {}

    for link in extracted_links:
        link_str = ' '.join(link)
        
        if counted_links_dict.get(link_str):
            counted_links_dict[link_str] += 1
        else:
            counted_links_dict[link_str] = 1
        
    return counted_links_dict


def get_links_from_tweet(trend_from_storage):
    """
    IN:
    trend_from_storage (string): one trend in the form "<trend>.json
    OUT:
    count_links(extracted_links) (dict): dict containing all links in on trend
    """

    tweets = read_from_storage(trend_from_storage)

    extracted_links = []
    
    link_string = r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"
    for tweet in tweets:
        if re.search(link_string, tweet):
            for link in re.findall(link_string, tweet):
                if len(link) == 23:
                    extracted_links.append(re.findall(link_string, link))
    
    return count_links(extracted_links)


def remove_numbers_and_links(tweets):
    """
    IN:
    tweets (list): text of all tweets of the trend
    OUT:
    tweets (list): text of all tweets of the trend
    """

    for index in range(len(tweets)):
        tweets[index] = re.sub(r'[\d]', '', tweets[index])
        tweets[index] = re.sub(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweets[index])
        tweets[index] = tweets[index].replace("_", "")

    return tweets


def clean_tweets(trend_from_storage):
    """
    IN:
    trend_from_storage (string): one trend in the form "<trend>.json"
    OUT:
    lemmatized_dict (dict): preprocessed data dict for that trend, structure: {"word": <word count>, ...}
    """

    # load nltk stopwords
    # TODO: move to main ?
    nltk.download('stopwords')
    # load NLP for tokenisation/lemmatization
    nlp = spacy.load('de_core_news_sm')
    nlp.disable_pipes('tagger', 'parser', 'ner')

    tweets = read_from_storage(trend_from_storage)

    # Remove all numbers, links and underscores
    tweets = remove_numbers_and_links(tweets)

    german_stop_words = stopwords.words('german')
    # Some Twitter abbreviations
    additional_stopwords = ["rt", "cn", "tw", "mt", "ht", "prt", "rthx", "tmb", "tl", "tt", "dm", "tldr", "em", 
                            "fwd", "hth", "irl", "jk", "til", "nsfw", "tmi", "fyi", "idk", "idc", "fb", "yt", "ff",
                            "de", "gg", "re", "gt", "sc", "str", "whs", "ne", "rbg", "kah", "gk", "ps", "bo", "jp",
                            "je", "en", "ft", "ik", "lol", "mh", "pe", "oh", "btw", "jpg", "png", "to", "nr"]
    german_stop_words.extend(additional_stopwords)

    lemmatized_dict = {}
    tweet_list = []

    for tweet in tweets:
        
        # lower case and remove non-alphabetic characters
        tweet = str(re.sub("[/']", '', re.sub(r"[^A-ZÄÖÜa-zäöüß\d']+", ' ', str(tweet))).lower())
        tweet = nlp.tokenizer(tweet)
        # removing the stopwords
        tweet = [str(word) for word in tweet if str(word) not in german_stop_words]
        # removing one char tokens
        tweet = [word for word in tweet if (len(word) > 1)]
        # removing empty tokens
        tweet = [word for word in tweet if (len(word) != 0)]
        # removing empty list
        if len(tweet) > 0:
            tweet_list.append(tweet)
            for word in tweet:
                if word not in lemmatized_dict:
                    lemmatized_dict[word] = 1
                else:
                    lemmatized_dict[word] += 1

    return lemmatized_dict


if __name__ == "__main__":

    # print(get_links_from_tweet("Kane.json"))
    print(clean_tweets("#Streeck.json"))
    # print(clean_tweets("#AdoreYouDay.json"))
    print("\nYou are doing great! :)")  # Motivational Message
