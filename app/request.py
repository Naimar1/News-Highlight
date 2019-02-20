import urllib.request,json
from app import app
from .models import newsAr

News = newsAr.News
Article = newsAr.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
source_base_url = app.config['NEWS_SOURCES_BASE_URL']
articles_base_url = app.config['NEWS_ARTICLES_API_BASE_URL']
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_base_url.format(api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        # print(get_sources_response)
        news_results = None

        if get_sources_response['sources']:
            news_results_list = get_sources_response['sources']
            news_results = process_results(news_results_list)
     
    return news_results
            
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
        id = news_item.get('id')
        name = news_item.get('name')

        news_object = News(id,name)
        news_results.append(news_object)


    return news_results

def get_articles(id):
    '''
    Function thet gets the json response to our url request
    '''
    get_articles_url = articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results   

def process_articles(article_list):
    '''
    Function that processes the article result and transforms them to a list of objects
    Args:
        article_list: a list of dictionaries that contain articles
    Returns:
        article_results: a list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        title = article_item.get('title')
        author= article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            article_object = Article(id,title,author,description,url,urlToImage,publishedAt)
            article_results.append(article_object)

    return article_results
