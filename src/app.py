
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'




@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    return render_template('user.html', name=username)
