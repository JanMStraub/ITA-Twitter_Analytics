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
    extracted_links (list): list containing all links in on trend
    """

    tweets = read_from_storage(trend_from_storage)

    extracted_links = []
    
    link_string = "(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"
    for tweet in tweets:
        if re.search(link_string, tweet):
            for link in re.findall(link_string, tweet):
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
    additional_stopwords = ["rt", "lt"]
    german_stop_words.extend(additional_stopwords)

    """
    for tweet in tweets:
        re.sub  # lower case and remove non-alphabetic characters
        nlp
        stopwords remove
        one char tokens
        empty tokens...
        cleaned_tweets.append()
        bigrams

        -> lemmatized dict
    """

    lemmatized_dict = {}

    for tweet in tweets:
        # lower case and remove non-alphabetic characters
        tweet = re.sub("[/']", '', re.sub("[^A-Za-z\d']+", ' ', str(tweet))).lower()
        tweet = nlp.tokenizer(tweet)
        # removing the stopwords
        tweet = [str(word) for word in tweet if str(word) not in german_stop_words]
        # removing one char tokens
        tweet = [word for word in tweet if (len(word) > 1)]
        # removing empty tokens
        tweet = [word for word in tweet if (len(word) != 0)]
        # removing empty list
        if len(tweet) > 0:
            
            tweet_stream = [tweet]
            print(tweet)
            # define the phraser for bi-gram creation#
            phrases = Phrases(tweet_stream, threshold=2)
            bigram = Phraser(phrases)
            new_lines = bigram[tweet]
            print(new_lines)


    """

    sent = [] # list of all words
    sent = quotes

    # for quote in quotes:
    #     for word in quote:
    #         sent.append(word)


    phrases = Phrases(sent, min_count=10, threshold=2) #define the phraser for bi-gram creation#
    bigram = Phraser(phrases)

    new_lines = bigram[sent] # transformed the lines

    vectorizer = CountVectorizer(analyzer="word", lowercase=True, ngram_range=(1, 2), stop_words=german_stop_words)
    X = vectorizer.fit_transform(tweets).toarray()

    
    sorted_list = dict(vectorizer.vocabulary_.items())

    for string in list(sorted_list.keys()):
        index = sorted_list[string]
        token = []
        token.append(nlp.tokenizer(string))
        print(token)

    
    for string in list(sorted_list.keys()):
        index = sorted_list[string]
        for t in nlp.tokenizer(string):
            if t.lemma_ not in lemmatized_dict:
                lemmatized_dict[t.lemma_] = X[0:X.shape[0], index].sum()
            else:
                lemmatized_dict[t.lemma_] += X[0:X.shape[0], index].sum()
    """

    return lemmatized_dict


if __name__ == "__main__":

    # print(get_links_from_tweet("TEST.json"))
    print(clean_tweets("TEST.json"))
    # print(clean_tweets("#AdoreYouDay.json"))
    print("\nYou are doing great! :)")  # Motivational Message
