from flask import render_template
from app import app
from .request import get_newshl

# Views
@app.route('/news/<string:news_article>')
def news(news_article):

    '''
    View news page function that returns the news details page and its articles
    '''
    return render_template('news.html',title = news_article)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    heading = 'Home - Welcome to our News Highlight'
    return render_template('index.html', heading = heading)

    # Getting current news
    current_newshl = get_newshl('current')
    print(current_newshl)

    heading = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', heading = heading,current = current_newshl)