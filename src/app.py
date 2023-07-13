from flask import Flask, render_template


app = Flask(__name__,template_folder='./templates',static_folder='./asset')

@app.route('/')
def hello():
    notLoggedin = True
    return render_template('index.html', notLoggedin=notLoggedin)

@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    notLoggedin = False
    return render_template('user.html', name=username, notLoggedin=notLoggedin)
