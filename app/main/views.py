from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Sources, Articles, User
from flask import request,redirect,url_for
from ..requests import get_sources, get_article
from flask_login import login_required, current_user
from .forms import ReviewForm,UpdateProfile
from .. import db,photos
import markdown2

@main.route('/')
def index():
    '''
    function that returns the index page and it's data
    '''
    new_source = get_sources()

    title = "Right at News Highlights"

    return render_template('index.html', title = title, new_source = new_source)

@main.route('/new_source/<id>')
def article(id):
    '''
    function for returning artcicle details and its data
    '''
    article = get_article(id)

    return render_template('article.html',  article = article)

@main.route('/article/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
   form = ReviewForm()
   article = get_article(id)
   if form.validate_on_submit():
       title = form.title.data
       review = form.review.data

       # Update review instance
       new_review = Review(article_id=article.id,article_title=title,image_path=article.poster,article_review=review,user=current_user)

       # save review method
       new_review.save_review()
       return redirect(url_for('article',id = article.id ))

   title = f'{article.title} review'
   return render_template('new_review.html',title = title, review_form=form, article=article)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/review/<int:id>')
def single_review(id):
    review=Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)