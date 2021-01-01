import os

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from pipeline import clean_tweets

# get all trend filenames from storage
current_dir = os.path.dirname(os.path.abspath(__file__))
trends = [trend for trend in os.listdir(current_dir + '/../storage')]


def save_wordcloud_to_storage(trend_name, wordcloud):
    name = str(trend_name).removesuffix('.json')
    path = current_dir + '/../storage/' + name + '.png'

    if not os.path.exists(path):
        print("processing: " + name)

        fig = plt.figure(1, figsize=(10, 10))  # set size of image
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.savefig(path)
        print("Image successfully writen to storage/" + name)

    else:
        print("skipping " + name + " -> already in storage")


def get_most_common():
    # run pipeline for all tweets from each trend to get preprocessed data
    preprocessed_data = []
    for trend in trends[:2]: # only for testing purposes set to 2
        preprocessed_data.append(clean_tweets(trend))
        most_common = []
        print(trend)


        for item in preprocessed_data:
            most_common = sorted(item, key=item.get, reverse=True)[:20] # change value as needed
            wordcloud = WordCloud().generate(str(most_common))

        save_wordcloud_to_storage(trend, wordcloud)

if __name__ == "__main__":

    get_most_common()
    print("\nYou are doing great! :)")  # Motivational Message