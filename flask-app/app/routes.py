from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

# --- Vulnerable login route ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Vulnerable: credentials checked in an unsafe way
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == request.args.get('pw'):
            return "Logged in as admin!"
        else:
            return "Invalid credentials", 401
    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit">
        </form>
    '''