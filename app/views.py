from flask import render_template,request,redirect,url_for
from . import main
from app import app
from .request import get_sources,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # heading = 'Home - Welcome to our News Highlight'
    # return render_template('index.html', heading = heading)

    # Getting current news
    current_sources = get_sources('everything')
    # print('current_newshl')

    heading = 'Home - Welcome to The best News Review Website Online'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
        return render_template('index.html', heading = heading, current = current_sources)

@app.route('/articles/<id>')
def articles(id):

    '''
    View some page source function that returns the news details page and its articles
    '''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('news.html',id = id, articles = articles)

@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',articles = searched_articles)

