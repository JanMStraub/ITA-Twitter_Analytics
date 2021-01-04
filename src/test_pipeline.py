import pipeline
import unittest
import json
import os
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

class TestPipelineMethods(unittest.TestCase):


    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        #self.testdata = open(current_dir + '/../storage/jsons/TEST.json').read()
        self.testdata_read_from_storage = [
            "Dies ist ein Test! Halleluja",
            "Dies ist ein Test! Halleluja",
            "Dies ist ein Test! Tag",
            "Dies ist ein Test! Tag https://www.youtube.com/watch?v=ERGbgvvCJ8o",
            "Dies sind Tests! 9 Tage. https://www.youtube.com/watch?v=ERGbgvvCJ8o",
            "Dies ist ein Test! https://www.youtube.com/watch?v=rOaKyH858yY"
        ]
        self.testdata_count_links = {
            "https://www.youtube.com/watch?v=ERGbgvvCJ8o": 2,
            "https://www.youtube.com/watch?v=rOaKyH858yY": 1
        }

        self.testdata_get_links_from_tweets = [
            ["https://www.youtube.com/watch?v=ERGbgvvCJ8o"],
            ["https://www.youtube.com/watch?v=ERGbgvvCJ8o"],
            ["https://www.youtube.com/watch?v=rOaKyH858yY"]
        ]


    def test_read_from_storage(self):
        """
        test if list of only tweet texts is correct imported
        """
        self.assertEqual(self.testdata_read_from_storage, pipeline.read_from_storage("TEST.json"))


    def test_count_links(self):
        """
        test if links are counted correct
        """
        self.assertEqual(self.testdata_count_links, pipeline.count_links(self.testdata_get_links_from_tweets))


    def test_get_links_from_tweet(self):
        """

        """
        self.assertEqual(self.testdata_count_links, pipeline.get_links_from_tweet("TEST.json"))


if __name__ == "__main__":
    unittest.main()
