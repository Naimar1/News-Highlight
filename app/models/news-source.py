import unittest
from models import news-article
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("Bitmain Announces Energy-Efficient ASIC Chip for Mining Bitcoin and Bitcoin Cash","https://images.cointelegraph.com/images",
        "Chinese mining giant Bitmain has announced its new 7nm ASIC chip, which reportedly enables faster and cheaper mining of BTC and BCH","2019-02-18T14:40:00Z","Cointelegraph By Ana Berman")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()