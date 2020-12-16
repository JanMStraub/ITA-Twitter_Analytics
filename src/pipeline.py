import json
import os
import nltk
import re
import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


# returns list with strings containing the text of a tweet
# filename must be like : "#Formel1.json"
def read_from_storage(filename):
    """
    IN:
    filename (string): one filename of a json in storage in the form: "<trend>.json"
    OUT:
    data (List): a list of string, each containing the raw text data from one tweet
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + '/../storage/' + filename
    data = []

    with open(path, 'r') as file:
        tweets_json = json.load(file)
        for tweet in tweets_json:
            data.append(tweet["text"])

    return data


def clean_tweets(trend_from_storage):
    """
    IN:
    trend_from_storage (string): one trend in the form "<trend>.json"
    OUT:
    lemmatized_dict (dict): preprocessed data dict for that trend, structure: {"word": <word count>, ...}
    """

    # load nltk stopwords
    nltk.download('stopwords')
    # load NLP for tokenisation/lemmatization
    nlp = spacy.load('de_core_news_sm')
    nlp.disable_pipes('tagger', 'parser', 'ner')

    tweets = read_from_storage(trend_from_storage)
    for index in range(len(tweets)):
        tweets[index] = re.sub(r'[\d]', '', tweets[index])

    german_stop_words = stopwords.words('german')
    vectorizer = CountVectorizer(analyzer="word", lowercase=True, stop_words=german_stop_words)
    vectorizer.fit_transform(tweets)

    lemmatized_dict = {}
    sorted_list = dict(vectorizer.vocabulary_.items())

    for string in list(sorted_list.keys()):
        for t in nlp.tokenizer(string):
            if t.lemma_ not in lemmatized_dict:
                lemmatized_dict[t.lemma_] = sorted_list[string]
            else:
                lemmatized_dict[t.lemma_] += sorted_list[string]

    return lemmatized_dict


if __name__ == "__main__":

    clean_tweets("#Formel1.json")
    print("\nYou are doing great! :)")  # Motivational Message
