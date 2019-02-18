from flask import render_template
from app import app

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

    heading = 'Home - Welcome tto our News Highlight'
    return render_template('index.html', heading = heading)