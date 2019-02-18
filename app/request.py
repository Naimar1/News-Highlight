from app import app
import urllib.request,json
from .models import news-article


# Getting api key
api_key = app.config['NEWS_API_KEY']

News = news.News

# Getting the news base url
base_url = app.config["News_API_BASE_URL"]

def get_newshl(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newshl_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_newshl_url) as url:
        get_newshl_data = url.read()
        get_newshl_response = json.loads(get_newshl_data)

        news_results = None

        if get_newshl_response['results']:
            news_results_list = get_newshl_response['results']
            news_results = process_results(news_results_list)
            
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('original_title')
        urlToImage = news_item.get('url_To_Image')
        description = news_item.get('description')
        publishedAt = news_item.get('date')
        author = news_item.get('name_author')

        if poster:
            news_object = News(title,urlToImage,description,publishedAt,author)
            news_results.append(news_object)


    return news_results