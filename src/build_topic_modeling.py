import os
import gensim.corpora as corpora
import gensim.models as models

from pipeline import clean_tweets
from pprint import pprint

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]


def convert_dict_to_list(data):
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
    # Create Dictionary
    id2word = corpora.Dictionary(word_list)
    print(id2word)

    # Create Corpus
    texts = word_list

    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    return corpus, id2word


def model_training(corpus, id2word):
    # number of topics
    num_topics = 10

    # Build LDA model
    lda_model = models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)

    pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]


if __name__ == '__main__':

    for trend in trends[25:26]:
        data = clean_tweets(trend)
        # print(convert_dict_to_list(data))
        list_data = convert_dict_to_list(data)
        corpus_data, id2word_data = preparing_data_for_LDA(list_data)
        model_training(corpus_data, id2word_data)

print("You are doing great! :)")
