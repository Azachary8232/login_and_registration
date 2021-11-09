# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User   
from flask_bcrypt import Bcrypt  
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login_registration.html')

@app.route('/create', methods=['POST'])
def create():
        if not User.vaildate_info(request.form):
            return redirect('/')

        password_hash = bcrypt.generate_password_hash(request.form['password'])

        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "password" : password_hash
        }
        id = User.create(data)
        session['user_id'] = id
        return redirect('/dashboard/')

@app.route('/login', methods = ['POST'])
def login():
    data = { 
        "email" : request.form["email"]
        }
    user_in_db = User.get_one_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", category= "login_email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", category= "login_password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")


@app.route('/dashboard/')
def dashboard():
    if  session:
        return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
