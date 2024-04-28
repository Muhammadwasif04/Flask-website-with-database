from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if len(first_name) < 2:
            flash("first name must be greater than 10 characters.", category='error')
        elif len(last_name) < 2:
            flash("last name must be greater than 10 characters.", category='error')
        elif len(username) < 2:
            flash("user name must not have spaces between them.", category='error')
        elif len(email) < 5:
            flash("Email must be greater than 10 characters.", category='error')
        elif password != confirm_password:
            flash("Password don\'t match.", category='error')
        elif len(password) < 7:
            flash('Password contain special characters')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name,
                            username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('register.html')