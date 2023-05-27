from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'



@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'<h1>Hello, {escape(username)}!</h1>' 

