import os

from pipeline import clean_tweets
import gensim.corpora as corpora

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]

def preparing_data_for_LDA(data):
    text = data

    corpus = [data.doc2bow(text) for text in texts]



if __name__ == '__main__':

    for trend in trends[25:26]:
        data = clean_tweets(trend)
        preparing_data_for_LDA(data)

    print("You are doing great! :)")
