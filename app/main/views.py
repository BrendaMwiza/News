from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    function that returns the index page and it's data
    '''
    news_source = get_source()

    title = "Right at News Highlights"

    return render_template('index.html', title = title, sources = news_source)

@main.route('/article/<article_id>')
def article(article_id):
    '''
    function for returning artcicle details and its data
    '''
    article = get_article()

    return render_template('article.html',  article = article)