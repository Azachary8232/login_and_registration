# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app import app
import re
from flask_bcrypt import Bcrypt      
bcrypt = Bcrypt(app) 





class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ***CREATE***






    # ***Retreive***






    # ***Update***







    # ***Delete***