import os
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from pipeline import clean_tweets


# to color the plot
# function from https://towardsdatascience.com/create-word-cloud-into-any-shape-you-want-using-python-d0b88834bc32
def similar_color_func(word=None, font_size=None,
                       position=None, orientation=None,
                       font_path=None, random_state=None):

    h = 210  # 0 - 360 / 200
    s = 70  # 0 - 100  / 50 / 70
    random = random_state.randint(30, 70)  # 0 - 100
    return "hsl({}, {}%, {}%)".format(h, s, random)


# to color the plot
# function from https://towardsdatascience.com/create-word-cloud-into-any-shape-you-want-using-python-d0b88834bc32
def multi_color_func(word=None, font_size=None,
                     position=None, orientation=None,
                     font_path=None, random_state=None):

    colors = [[4, 77, 82],
              [25, 74, 85],
              [82, 43, 84],
              [158, 48, 79]]

    rand = random_state.randint(0, len(colors) - 1)
    return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])


def make_circle():
    """
    OUT:
    mask (mask): shaped mask
    """

    # code from https://codefires.com/how-create-word-cloud-python/
    # makes elliptic shape using numpy
    x, y = np.ogrid[:500, :700]
    mask = (x - 350) ** 2 + (y - 350) ** 2 > 350 ** 2
    mask = 255 * mask.astype(int)
    return mask


def create_and_save_wordcloud_to_storage(trend_name, data):
    """
    IN:
    trend_name (string): one trend in the form "<trend>"
    data (dict): preprocessed data dict for that trend, structure: {"word": <word count>, ...}
    OUT:
    None (png created in storage/wordclouds)
    """

    # get all trend filenames from storage
    current_dir = os.path.dirname(os.path.abspath(__file__))
    name = str(trend_name).removesuffix('.json')
    path = current_dir + '/../storage/results/' + name + '_wordcloud.png'

    if not os.path.exists(path):
        print("processing: " + name)

        # build wordcloud
        wordcloud = WordCloud(
            background_color=None, mode='RGBA', max_words=500, random_state=42, width=1000, height=1000,
            color_func=similar_color_func, mask=make_circle(), min_word_length=2).generate_from_frequencies(data)
        plt.imshow(wordcloud, interpolation="bilinear")
        wordcloud.to_file(path)

        print("Image successfully writen to storage/results/" + name)

    else:
        print("skipping " + name + " -> already in storage")


def create_and_save_wordcloud_to_storage_lda(trend_name, topic_words, current_dir):
    """
    IN:
    trend_name (string): one trend in the form "<trend>"
    topic_words (dict): dict with counted topic words
    current_dir (string): path to storage
    OUT:
    None (png created in storage/results)
    """

    name = str(trend_name).removesuffix('.json')
    path = current_dir + '/../storage/results/' + name + '_lda.png'

    if not os.path.exists(path):
        print("building wordcloud: " + name)

        # build wordcloud
        wordcloud = WordCloud(
            background_color=None, mode='RGBA', max_words=10, random_state=42, width=1000, height=1000,
            color_func=similar_color_func, scale=5).generate_from_frequencies(topic_words)
        plt.imshow(wordcloud, interpolation="bilinear")
        wordcloud.to_file(path)

        print("Image successfully writen to storage/results/" + name)

    else:
        print("skipping " + name + " -> already in storage")


if __name__ == "__main__":

    # get all trend filenames from storage
    current_dir = os.path.dirname(os.path.abspath(__file__))
    trends = [trend for trend in os.listdir(current_dir + '/../storage/jsons')]
    trends = ["#Lanz.json"]

    for trend in trends:
        print(trend)
        data = clean_tweets(trend)
        create_and_save_wordcloud_to_storage(trend, data)


    print("\nYou are doing great! :)")  # Motivational Message
