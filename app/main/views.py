from flask import render_tempate
from . import main

@main.route('/')
def index():
    '''
    function that returns the index page and it's data
    '''
    news_source = get_source()

    title = "Right at News Highlights"

    return render_template('index.html', title = title, sources = news_source)
    