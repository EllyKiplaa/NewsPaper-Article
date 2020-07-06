import unittest
from app.models import News, Articles

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("bbc-news",'BBC News','The news site that will provide you with realtime news and what is happenning around the globe','bbc.com',"all-news","London,UK","en")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()