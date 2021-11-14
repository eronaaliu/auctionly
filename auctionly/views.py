from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
import flask_login
from werkzeug.utils import redirect

views = Blueprint('views', __name__)

from .art.art import Art
from . import db



@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/rank_info')
@login_required
def rank_info():
    return render_template("rank_info.html")

@views.route('/profile')
@login_required
def profile():
    user = flask_login.current_user
    user_art = user.get_user_art()

    return render_template("profile.html", user=user, user_art=user_art)

@views.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_art():
    if request.method == 'POST':
        image = request.form.get('email') 
        name = request.form.get('name')
        description = request.form.get('description')
        art_category = request.form.get('artCategory')
        owner_id = flask_login.current_user.id
        
        print(owner_id)
            

        new_art = Art(name, owner_id, image, description, art_category)

        db.session.add(new_art)
        db.session.commit()
        db.session.flush()
        new_art.set_art_id(new_art.id)

        return redirect(url_for('views.profile'))


    return render_template("upload.html")

@views.route('/auction-art', methods=['GET', 'POST'])
@login_required
def auction_art():
    if request.method == 'POST':
        pass

    user = flask_login.current_user
    user_art = user.get_user_art()
    for art in user_art:
        print(art.get_description())

    return render_template("auction-art.html", user=user,)
