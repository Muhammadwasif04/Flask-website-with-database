from flask import Blueprint, render_template, request, flash

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
        first_name = request.form.get('Firstname')
        last_name = request.form.get('lastname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category='error')
        elif len(first_name) < 10:
            flash("first name must be greater than 10 characters.", category='error')
        elif len(last_name) < 10:
            flash("last name must be greater than 10 characters.", category='error')
        elif len(username) < 9:
            flash("user name must not have spaces between them.", category='error')
        elif password != confirm_password:
            flash("Password don\'t match.", category='error')
        elif password < 7:
            flash('Password contain special characters')
        else:
            flash('Account created!', category='success')
    return render_template('register.html')