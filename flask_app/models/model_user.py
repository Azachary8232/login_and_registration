# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app import app
import re
from flask_bcrypt import Bcrypt     
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #<--- Add to /model top




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
    def vaildate_user(user):
        is_valid = True 
        
        if len(user['first_name']) < 1: 
            flash("First name must be included.")
            is_valid = False 
        if len(user['last_name']) < 1: 
            flash("Last name must be included.")
            is_valid = False
        if len(user['email']) < 1: 
            flash("Email name must be included.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 1: 
            flash("Password must be included.")
            is_valid = False 
        if user['confirm_password'] != user['password']: 
            flash("Passwords do not match.")
            is_valid = False
        return is_valid


    # ***CREATE***






    # ***Retreive***






    # ***Update***







    # ***Delete***