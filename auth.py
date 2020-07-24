from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()
    
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    name = request.form.get('name')
    password = request.form.get('password')
    phone = request.form.get('phone')


    user = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Username already in use, choose a different one or')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(username=username, name=name, password=generate_password_hash(password, method='sha256'), phone=phone,w1="0",w2="0",w3="0",w4="0",w5="0",w6="0",w7="0",w8="0",w9="0",w10="0",w11="0",w12="0",w13="0",w14="0",w15="0",w16="0",w17="0",w18="0",w19="0",w20="0",w21="0",w22="0",w23="0",w24="0")

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
