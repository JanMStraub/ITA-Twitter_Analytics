import json
import os


# returns list with strings containing the text of a tweet
# filename must be like : #Formel1.json
def read_from_storage(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + '/../storage/' + filename
    data = []

    with open(path, 'r') as file:
        tweets_json = json.load(file)
        for tweet in tweets_json:
            data.append(tweet["text"])

    return data


def clean_tweets():
    data = read_from_storage("#Formel1.json")




if __name__ == "__main__":

    clean_tweets()
    print("\nYou are doing great! :)")  # Motivational Message
