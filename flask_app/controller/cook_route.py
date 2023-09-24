from flask_app import app
from flask import render_template,redirect,session,flash,request
from flask_bcrypt import Bcrypt
from flask_app.model.cook import Cook 
from flask_app.model import cook       

bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument



# render templates
@app.route('/')
def register_login_page():
    return render_template('index.html')

@app.route('/account')
def account_page():
    data = {
        'id': session['cook_id']
    }
    
    return render_template('recipes.html', cooks = Cook.get_one(data))

@app.route ('/account/create_recipe')
def create_recipe():
    return render_template('create_recipe.html')

@app.route ('/account/edit')
def edit_page():
    return render_template('edit.html')

@app.route ('/description')
def description():
    
    return render_template('description.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')

# Post routes
# Register =======================

@app.route('/create', methods=['POST'])
def create_cook():
    
    if not Cook.validation(request.form):
        return redirect('/')
        
    pw_hashed = bcrypt.generate_password_hash(request.form['password'])
    
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'password': pw_hashed,
        'dob': request.form['dob'],
        'email': request.form['email']
    }
    
    cooks_id = Cook.save(data)
    print()
    print(cooks_id)
    session['cook_id'] = cooks_id
    return redirect('/')


#  login ========================>

@app.route('/login', methods=['post'])
def login():
    
    # session.pop['cook_id', None]
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    
    cook_in_db = Cook.login(data)
    
    if not cook_in_db :
        flash('Invalid Email/Password','login')
        return redirect('/')
    if not bcrypt.check_password_hash(cook_in_db.password,request.form['password']):
        flash('Invalid Email/Password','login')
        return redirect('/')
        
    session['cook_id'] = cook_in_db.id
    return redirect('/account')