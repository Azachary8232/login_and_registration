# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/create', methods=['POST'])
def create():
    data = {
        # 'id' : id
        "(something/no())" : request.form['(somethong/no())'],
        "(something/no())" : request.form['(somethong/no())'],
    }
    Sample.create(data)
    return redirect('/sample')