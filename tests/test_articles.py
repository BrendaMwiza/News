import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):

    def setUp(self):
        '''
        Method that runs before every test
        '''
        self.article = Articles("id", "name", "author", "title", "description", "url", "urlToImage", "publishedAt")

    def test_it(self):
        self.assertTrue(isinstance(self.article,Articles))