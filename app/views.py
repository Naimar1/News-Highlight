from flask import render_template
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
    return render_template('index.html', heading = heading, current = current_sources)

@app.route('/articles/<id>')
def articles(id):

    '''
    View some page source function that returns the news details page and its articles
    '''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('news.html',id = id, articles = articles)

