import os

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from pipeline import clean_tweets

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]

def save_wordcloud_to_storage(trend_name, wordcloud):
    name = str(trend_name).removesuffix('.json')
    path = current_dir + '/../storage/wordclouds/' + name + '.png'

    if not os.path.exists(path):
        print("processing: " + name)

        fig = plt.figure(1, figsize=(10, 10))  # set size of image
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.savefig(path)
        print("Image successfully writen to storage/wordclouds/" + name)

    else:
        print("skipping " + name + " -> already in storage")


def get_most_common(trend, data):
    # run pipeline for all tweets from each trend to get preprocessed data
    most_common = sorted(data, key=data.get, reverse=True)[:20] # change value as needed
    wordcloud = WordCloud().generate(str(most_common))

    save_wordcloud_to_storage(trend, wordcloud)

if __name__ == "__main__":

    for trend in trends:
        preprocessed_data = []
        data = clean_tweets(trend)
        preprocessed_data.append(data)
        get_most_common(trend, data)
    print("\nYou are doing great! :)")  # Motivational Message