# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User

@app.route('/')
def index():
    return render_template('login_registration.html')

@app.route('/create', methods=['POST'])
def create():
        if not User.vaildate_info(request.form):
            return redirect('/')
        data = {
            # 'id' : id
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "password" : request.form['password']

        }
        User.create(data)
        return redirect('/dashboard')