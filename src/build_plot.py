import os
import numpy as np
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))

def create_plot(trend_name, topic_words):
    name = str(trend_name).removesuffix('.json')
    path = current_dir + '/../storage/results/' + name + '_plot.png'

    if not os.path.exists(path):
        print("processing: " + name)

        plt.bar(range(len(topic_words)), list(
            topic_words.values()), align='center')
        plt.xticks(range(len(topic_words)), list(topic_words.keys()))
        plt.savefig(path)

        print("Image successfully writen to storage/results/" + name)

    else:
        print("skipping " + name + " -> already in storage")
