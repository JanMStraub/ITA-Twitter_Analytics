import os
import gensim.corpora as corpora
import gensim.models as models

from pipeline import clean_tweets
from build_wordcloud import create_and_save_wordcloud_to_storage_lda


def convert_dict_to_list(data):
    """
    IN:
    data (dict): preprocessed data dict for that trend, structure: {"word": <word count>, ...}
    OUT:
    word_list (list): list of list containing all words of one tweet
    """

    word_list = []
    for key in data:
        i = data.get(key)
        tweet_list = []
        while i > 0:
            tweet_list.append(key)
            i -= 1
        word_list.append(tweet_list)

    return word_list


def preparing_data_for_LDA(word_list):
    """
    IN:
    word_list (list): list of list containing all words of one tweet
    OUT:
    corpus (corpus): gensim corpus with the term document frequency
    id2word (dict): gensim corpora with the word_list
    """

    id2word = corpora.Dictionary(word_list)  # Create Dictionary
    texts = word_list  # Create Corpus
    corpus = [id2word.doc2bow(text) for text in texts]  # Term Document Frequency

    return corpus, id2word


def model_training(corpus, id2word):
    """
    IN:
    corpus (corpus): gensim corpus with the term document frequency
    id2word (dict): gensim corpora with the word_list
    OUT:
    lda_model (model): gensim lda_model
    """

    # Build LDA model
    lda_model = models.LdaMulticore(corpus=corpus, id2word=id2word, num_topics=1)

    return lda_model


def model_visualization(trend, lda_model, current_dir):
    """
    IN:
    trend (string): one trend in the form "<trend>.json"
    lda_model (model): gensim lda_model
    current_dir (string): path to storage
    OUT:
    topic_words (dict): dict with counted topic words
    """

    # to get the topic words for the plot
    topics = lda_model.show_topics(formatted=False)
    topic_words = dict(topics[0][1])

    create_and_save_wordcloud_to_storage_lda(trend, topic_words, current_dir)

    return topic_words


def perform_LDA(trend, data):
    """
    IN:
    trend (string): one trend in the form "<trend>.json"
    data (dict): preprocessed data dict for that trend, structure: {"word": <word count>, ...}
    OUT:
    topic_words (dict): dict with counted topic words
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # lda needs list and not dict
    list_data = convert_dict_to_list(data)
    # generate data for lda model training
    corpus_data, id2word_data = preparing_data_for_LDA(list_data)
    # lda model data for visualization
    lda_model_data = model_training(corpus_data, id2word_data)
    topic_words = model_visualization(trend, lda_model_data, current_dir)

    return topic_words


if __name__ == '__main__':

    # get all trend filenames from storage
    current_dir = os.path.dirname(os.path.abspath(__file__))
    trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]
    trends = ["#Lanz.json"]

    for trend in trends:
        data = clean_tweets(trend)
        list_data = convert_dict_to_list(data)
        corpus_data, id2word_data = preparing_data_for_LDA(list_data)
        lda_model_data = model_training(corpus_data, id2word_data)
        model_visualization(trend, lda_model_data, current_dir)

    print("You are doing great! :)")
