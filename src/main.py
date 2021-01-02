import os
import nltk
from pipeline import clean_tweets
from get_tweets import save_tweets_to_storage
from build_wordcloud import get_most_common 


def setup():
    """
    OUT:
    None (setup completed)
    """
    nltk.download('stopwords')


def main():
    """
    OUT:
    None
    """

    # Hyperparameters
    trend_amount = 5
    tweet_amount = 10

    # perform initial setup
    setup()

    # request tweets from API and saves them
    save_tweets_to_storage(trend_amount, tweet_amount)

    # get all trend filenames from storage
    current_dir = os.path.dirname(os.path.abspath(__file__))
    trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]

    # run pipeline for all tweets from each trend to get preprocessed data
    preprocessed_data = []
    for trend in trends:
        data = clean_tweets(trend)
        preprocessed_data.append(data)
        get_most_common(trend, data)

    # TODO: work with data
    # TODO: parse results to frontend
    # TODO: update Pipeline to filter '`´" 
    # TODO: update Pipeline to filter _
    # TODO: update Pipeline to filter links


if __name__ == "__main__":

    main()
    print("You are doing great! :)")
