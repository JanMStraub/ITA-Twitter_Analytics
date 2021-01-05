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

        self.testdata_remove_numbers_and_links = [
            "Dies ist ein Test! Halleluja",
            "Dies ist ein Test! Halleluja",
            "Dies ist ein Test! Tag",
            "Dies ist ein Test! Tag ",
            "Dies sind Tests!  Tage. ",
            "Dies ist ein Test! "
        ]

        self.testdata_clean_tweets = {
            "test": 5,
            "halleluja": 2,
            "tag": 2,
            "tests": 1,
            "tage": 1
        }


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
        test if links are filtered correctly
        """
        self.assertEqual(self.testdata_count_links, pipeline.get_links_from_tweet("TEST.json"))


    def test_remove_numbers_and_links(self):
        """

        """
        self.assertEqual(self.testdata_remove_numbers_and_links, pipeline.remove_numbers_and_links(self.testdata_read_from_storage))


    def test_clean_tweets(self):
        self.assertEqual(self.testdata_clean_tweets, pipeline.clean_tweets("TEST.json"))


if __name__ == "__main__":
    unittest.main()
