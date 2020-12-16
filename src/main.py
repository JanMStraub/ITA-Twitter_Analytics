import os
import nltk
from pipeline import clean_tweets
from get_tweets import save_tweets_to_storage


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
    trends = [trend for trend in os.listdir(current_dir + '/../storage')]

    # run pipeline for all tweets from each trend to get preprocessed data
    preprocessed_data = []
    for trend in trends:
        preprocessed_data.append(clean_tweets(trend))

    # TODO: work with data
    # TODO: parse results to frontend


if __name__ == "__main__":

    main()
    print("You are doing great! :)")
