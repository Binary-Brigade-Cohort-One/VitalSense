from datetime import datetime
from flask_login import UserMixin
from src import db, app
from flask_login import LoginManager



class USER(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    image_file= db.Column(db.String(20), nullable=False, default='default.jpg')
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    datas = db.relationship('DATA')
    weekli = db.relationship('Weekly')



class DATA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Height = db.Column(db.Float, nullable=False)
    Weight = db.Column(db.Float, nullable=False)
    Calorie_burned = db.Column(db.Float, nullable=False)
    sleep_quality = db.Column(db.String(200), nullable=False)
    Heartrate = db.Column(db.String(200), nullable=False)
    Caloriintake = db.Column(db.Float, nullable=False)
    Hydration = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Weekly(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    weeklyCalorie= db.Column(db.Float, nullable=False)
    weeklyHydration= db.Column(db.Float, nullable=False)
    weeklyWeight=db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


with app.app_context():  # we have to include this to make a table
 db.create_all()
 
login_manager = LoginManager()
login_manager.login_view = '/'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return USER.query.get(id)
        
