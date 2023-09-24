from flask_app.config.MySqlConnection import connectToMySQL
from flask import flash
from datetime import date
import re

class Cook:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.dob = data['dob']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.recipe = []
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO cooks(first_name,last_name,email,password,dob) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(dob)s);"
        result = connectToMySQL('friends').query_db(query,data)
        return result
    
    @classmethod
    def show_all(cls):
        query = "SELECT * from cooks;"
        result = connectToMySQL('friends').query_db(query)
        return result 
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * from cooks WHERE id = %(id)s;"
        results = connectToMySQL('friends').query_db(query,data)
        return cls(results[0])
    
    @classmethod 
    def login(cls,data):
        query = "SELECT * from cooks WHERE email = %(email)s;"
        results = connectToMySQL('friends').query_db(query,data)
        if len(results) < 1:
            False
        return cls(results[0])
    
    @staticmethod
    def validation(user):
        
        is_valid = True
        # regular expressions ----------------==######
        
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


        # date algorithm-----------##########
        
        
        if not email_regex.match(user['email']):
            flash('Invalid email address!','register')
            False
        
        if len(user['first_name']) < 2 :
            flash("First name must be atleast 3 characters long " , 'register')
            False
        
        if len(user['last_name']) < 2 :
            flash(" Last name must be atleast 3 characters long " , 'register')
            False
        
        if user['password2'] != user['password'] :
            flash(" Password doesn't match ", 'register')
            False
        return is_valid