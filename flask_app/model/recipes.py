from flask_app.config.MySqlConnection import connectToMySQL
from flask_app.model.cook import cook
 
class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under = data['under']
        self.cooked_at = data['cooked_at']
        self.updated_at = data['update_at']
        self.cook_id = data['cooks_id']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO cooks(name,description,instruction,under) VALUES(%(name)s,%(description)s,%(instruction)s,%(under)s);"
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
    