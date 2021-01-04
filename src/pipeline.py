import json
import os
import nltk
import re
import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


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

def remove_duplicate_links(extracted_links):
    """
    IN:
    extracted_links (list): list containing all links in on trend
    OUT:
    extracted_links_filterd (list): list containing all links in on trend but duplicates are removed
    """

    extracted_links_filterd = []

    [extracted_links_filterd.append(link) for link in extracted_links if link not in extracted_links_filterd]

    return extracted_links_filterd

def get_links_from_tweet(tweets):
    """
    IN:
    tweets (list): text of all tweets of the trend
    OUT:
    extracted_links (list): list containing all links in on trend
    """

    extracted_links = []
    
    link_string = "(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"
    for tweet in tweets:
        if re.search(link_string, tweet):
            extracted_links.append(re.findall(link_string, tweet))
    

    return remove_duplicate_links(extracted_links)

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
    
    return tweets

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

    # Get all links in tweets
    extracted_links = get_links_from_tweet(tweets)

    # Remove all numbers and links
    tweets = remove_numbers_and_links(tweets)

    german_stop_words = stopwords.words('german')
    vectorizer = CountVectorizer(analyzer="word", lowercase=True, stop_words=german_stop_words)
    X = vectorizer.fit_transform(tweets).toarray()

    lemmatized_dict = {}
    sorted_list = dict(vectorizer.vocabulary_.items())

    for string in list(sorted_list.keys()):
        index = sorted_list[string]
        for t in nlp.tokenizer(string):
            if t.lemma_ not in lemmatized_dict:
                lemmatized_dict[t.lemma_] = X[0:X.shape[0], index].sum()
            else:
                lemmatized_dict[t.lemma_] += X[0:X.shape[0], index].sum()

    return lemmatized_dict, extracted_links

# not quite finished yet
def clean_tweets_twopointo(trend_from_storage):
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
    # remove numbers
    for index in range(len(tweets)):
        tweets[index] = re.sub(r'[\d]', '', tweets[index])

    lemmatized_dict = {}
    sorted_list = []

    for line in tweets:
        doc = nlp(line)
        # token_list = [token for token in doc]
        filtered_tokens = [token for token in doc if not token.is_stop]
        lemmas = [token.lemma_ for token in filtered_tokens]
        # might change to a list comprehension
        while(" " in lemmas):
            lemmas.remove(" ")
        sorted_list.append(lemmas)
    
    for token_list in sorted_list:
        for token in token_list:          
            if not lemmatized_dict.get(token):
                lemmatized_dict[token] = 1
            else:
                lemmatized_dict[token] += 1

    return lemmatized_dict

if __name__ == "__main__":

    print(clean_tweets("Vettel.json"))
    print("\nYou are doing great! :)")  # Motivational Message
