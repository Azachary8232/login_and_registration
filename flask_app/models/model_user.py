# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app import app
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #<--- Add to /model top

model_db = 'login_and_registration'


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def vaildate_info(user):
        is_valid = True 
        
        if len(user['first_name']) < 1: 
            flash("First name must be included.", category= "user_first_name")
            is_valid = False 
        if len(user['last_name']) < 1: 
            flash("Last name must be included.", category= "user_last_name")
            is_valid = False
        if len(user['email']) < 1: 
            flash("Email name must be included.", category= "user_email")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", category= "user_invalid_email")
            is_valid = False
        if len(user['password']) < 1: 
            flash("Password must be included.", category= "user_password")
            is_valid = False 
        if user['confirm_password'] != user['password']: 
            flash("Passwords do not match.", category= "user_confirm_password")
            is_valid = False
        return is_valid

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = connectToMySQL(model_db).query_db(query,data)
        return user_id


    # ***CREATE***






    # ***Retreive***






    # ***Update***







    # ***Delete***