import os
import gensim.corpora as corpora
import gensim.models as models

from pprint import pprint

from pipeline import clean_tweets
from build_wordcloud import create_and_save_wordcloud_to_storage_lda
from build_plot import create_plot


# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]


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


def model_visualization(trend, corpus, lda_model):
    # pprint(lda_model.print_topics())

    topics = lda_model.show_topics(formatted=False)
    topic_words = dict(topics[0][1])

    create_and_save_wordcloud_to_storage_lda(trend, topic_words)
    create_plot(trend, topic_words)

    return topic_words
    

def perform_LDA(trend, data):
    list_data = convert_dict_to_list(data)
    corpus_data, id2word_data = preparing_data_for_LDA(list_data)
    lda_model_data = model_training(corpus_data, id2word_data)
    topic_words = model_visualization(trend, corpus_data, lda_model_data)
    return topic_words

if __name__ == '__main__':

    for trend in trends[25:28]: # select TEST.json for testing
        data = clean_tweets(trend)
        list_data = convert_dict_to_list(data)
        corpus_data, id2word_data = preparing_data_for_LDA(list_data)
        lda_model_data = model_training(corpus_data, id2word_data)
        model_visualization(trend, corpus_data, lda_model_data)

    print("You are doing great! :)")
