import os
import numpy as np
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))

def create_and_save_plot(trend, topic_words):
    name = str(trend_name).removesuffix('.json')
    path = current_dir + '/../storage/results/' + name + '_lda.png'

    if not os.path.exists(path):
        print("processing: " + name)

        wordcloud = WordCloud(
            background_color=None, mode='RGBA', max_words=10, random_state=42, width=1000, height=1000,
            color_func=similar_color_func).generate_from_frequencies(lda_model)
        plt.imshow(wordcloud, interpolation="bilinear")
        wordcloud.to_file(path)

        print("Image successfully writen to storage/wordclouds/" + name)

    else:
        print("skipping " + name + " -> already in storage")
