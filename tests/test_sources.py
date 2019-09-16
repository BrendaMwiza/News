import unittest
from app.models import Sources

class SourcesTEst(unittest.TestCase):

    def setUp(self):
        '''
        Methode that runs before every test.
        '''
        self.source = Sources ( "cnn", "cnn", "View the latest news and breaking news today for U.S., world, weather and politics", "http:url//us.cnn.com", "general", "en", "us")

    def test_it(self):
        self.assertTrue(isinstance(self.source,Sources))