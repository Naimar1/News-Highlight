import unittest
from newsAr_test import News,Article

# test for News class

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('crypto-coins-news','Crypto Coins News')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

# test for Article class

class ArticleTest(unittest.TestCase):
        '''
        Test class to test the beahviour of the Article class
        '''

    def setUp(self):
        '''
        Set up method that will run before each test case
        '''
        self.new_article = Article()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))



if __name__ == '__main__':
    unittest.main()