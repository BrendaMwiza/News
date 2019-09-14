from flask import render_template
from . import main
from ..models import Sources, Articles
from flask import request,redirect,url_for
from ..request import get_sources, get_article

@main.route('/')
def index():
    '''
    function that returns the index page and it's data
    '''
    news_source = get_sources()

    title = "Right at News Highlights"

    return render_template('index.html', title = title, sources = news_source)

@main.route('/article/<article_id>')
def article(article_id):
    '''
    function for returning artcicle details and its data
    '''
    article = get_article()

    return render_template('article.html',  article = article)