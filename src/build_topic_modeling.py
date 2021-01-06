import os
import gensim.corpora as corpora

from pipeline import clean_tweets

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

    print(corpus)

if __name__ == '__main__':

    for trend in trends[25:26]:
        data = clean_tweets(trend)
        # print(convert_dict_to_list(data))
        preparing_data_for_LDA(convert_dict_to_list(data))

print("You are doing great! :)")
