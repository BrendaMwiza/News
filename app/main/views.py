from flask import render_tempate
from app import app

@app.route('/')
def index():
    '''
    function that returns the index page and it's data
    '''
    return render_template('index.html')