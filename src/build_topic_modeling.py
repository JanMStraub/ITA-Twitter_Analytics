import os
import gensim.corpora as corpora
import gensim.models as models

from pipeline import clean_tweets
from pprint import pprint

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

    # Create Dictionary
    id2word = corpora.Dictionary(word_list)

    # Create Corpus
    texts = word_list

    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    return corpus, id2word


def model_training(corpus, id2word):
    """
    IN:
    corpus (corpus): gensim corpus with the term document frequency
    id2word (dict): gensim corpora with the word_list
    OUT:
    lda_model (model): gensim lda_model
    """

    # number of topics
    num_topics = 1

    # Build LDA model
    lda_model = models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)

    pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]

    return lda_model

def model_analysis(corpus, id2word, lda_model):
    return 0



if __name__ == '__main__':

    for trend in trends[25:27]:
        data = clean_tweets(trend)
        # print(convert_dict_to_list(data))
        list_data = convert_dict_to_list(data)
        corpus_data, id2word_data = preparing_data_for_LDA(list_data)
        lda_model_data = model_training(corpus_data, id2word_data)
        model_analysis(corpus_data, id2word_data, lda_model_data)

    print("You are doing great! :)")
