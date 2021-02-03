import os
import matplotlib.pyplot as plt


def create_plot(trend_name, topic_words, current_dir):
    """
    IN:
    trend_name (string): one trend in the form "<trend>"
    topic_words (dict): dict with counted topic words
    current_dir (string): path to storage
    OUT:
    None (png created in storage/results)
    """

    name = str(trend_name).removesuffix('.json')
    path = current_dir + '/../storage/results/' + name + '_plot.png'

    if not os.path.exists(path):
        print("building plot: " + name)

        plt.figure()
        fig, ax = plt.subplots()
        ax.bar(range(len(topic_words)), list(topic_words.values()), align="center")
        ax.xaxis.label.set_color('white')
        ax.tick_params(colors='white')
        plt.xticks(range(len(topic_words)), list(topic_words.keys()))
        plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
        fig.subplots_adjust(bottom=0.2)
        plt.savefig(path, transparent=True)
        plt.clf()

        print("Image successfully writen to storage/results/" + name)

    else:
        print("skipping " + name + " -> already in storage")
