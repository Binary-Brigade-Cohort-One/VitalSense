from flask import redirect, render_template, url_for, request, flash

from src import app
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from src.models import USER , DATA, Weekly
from src import db





@app.route('/')
def hello():
    return render_template('index.html')


@app.route("/createaccount/<int:a>", methods=["POST", "GET"])
def createaccount(a):
   if request.method == "POST":
        firstnamehtml = request.form['firstname']
        lastnamehtml = request.form['lastname']
        emailhtml = request.form['email']
        passwordhtml = request.form['password']

        if len(firstnamehtml) < 3:
            flash('frist name must be grater than 3 character', category="error")

        elif len(lastnamehtml) < 1:
            flash("lastname must be grater than 1 characters", category="error")
        elif len(emailhtml) < 6:
            flash("Email should be grater than 6 characters", category='error')
        elif len(passwordhtml) < 4:
            flash("Password should be grater than 4 characters", category="error")
        else:

            user = USER(firstname=firstnamehtml, lastname=lastnamehtml,
                        email=emailhtml, password=generate_password_hash(passwordhtml, method='scrypt'))
            alluser = USER.query.all()
            if len(alluser) != 0:
                b = True
                for us in alluser:
                    if (emailhtml != us.email):
                        b = True

                    else:
                        b = False
                        break

                if (b == True):
                    db.session.add(user)
                    db.session.commit()
                    alluser = USER.query.all()
                    return render_template('creataccount.html', alluser=alluser, a=2)
                else:
                    alluser = USER.query.all()
                    return render_template('creataccount.html', alluser=alluser, a=-1)

            else:
                db.session.add(user)
                db.session.commit()

   alluser = USER.query.all()
   return render_template('creataccount.html', alluser=alluser, a=a)


@app.route('/login/<int:a>', methods=["POST", "GET"])
def login(a):
   
    if request.method == "POST":
        emailhtml = request.form['email']
        passwordhtml = request.form['password']

        alluser = USER.query.all()
        if len(alluser) != 0:
            b = True
            for user in alluser:
                if (emailhtml == user.email and check_password_hash(user.password, passwordhtml)):
                    login_user(user, remember=True)
                    b = True
                    break
                else:
                    b = False

            if (b == True):
                alluser = USER.query.all()
                return redirect(url_for('user', a=1))
            else:
                alluser = USER.query.all()
                return  render_template('login.html', alluser=alluser, a=-1)

        else:
            alluser = USER.query.all()
            return render_template('login.html', alluser=alluser, a=-1)

    alluser = USER.query.all()
    return render_template('login.html', alluser=alluser, a=a)


@app.route('/show')
def show():
    alluser = USER.query.all()
    print(alluser)
    return "Hi this is me inside show "


@app.route('/user/<int:a>', methods=['POST', 'GET'])
@login_required
def user(a):
    if (request.method == 'POST'):
        Heighthtml = request.form['height']
        Weighthtml = request.form['weight']
        Calorie_burnedhtml= request.form['calorie_burned']
        sleep_qualityhtml = request.form['sleepquality']
        Heartratehtml = request.form['heartrate']
        Caloriintakehtml = request.form['caloriintake']
        Hydrationhtml = request.form['hydration']

        data = DATA(Height=Heighthtml, Weight=Weighthtml, Calorie_burned=Calorie_burnedhtml, sleep_quality=sleep_qualityhtml,
                    Heartrate=Heartratehtml, Caloriintake=Caloriintakehtml,  Hydration=Hydrationhtml, user_id=current_user.id)
        db.session.add(data)
        db.session.commit()
        countdata=len(current_user.datas)
        if ( countdata% 7==0 and countdata !=0):   
         return redirect(url_for('weekly', b=countdata))
         
        
    return render_template('user.html', user=current_user, a=a)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    print(id)
    if id %7 ==0:
     weeklytotal=Weekly.query.all() 
     weektotal=len(weeklytotal)
     week=Weekly.query.filter_by(id=weektotal).first()
     db.session.delete(week)
     db.session.commit()
         
    data = DATA.query.filter_by(id=id).one()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('user', a=1))


@app.route('/update/<int:id>', methods=['GET', "POST"])
@login_required
def update(id):
    if request.method == "POST":
        Heighthtml = request.form['height']
        Weighthtml = request.form['weight']
        Calorie_burnedhtml = request.form['Calorie_burned']
        sleep_qualityhtml = request.form['sleepquality']
        Heartratehtml = request.form['heartrate']
        Caloriintakehtml = request.form['caloriintake']
        Hydrationhtml = request.form['hydration']

        data = DATA.query.filter_by(id=id).one()

        data.Height = Heighthtml
        data.Weight = Weighthtml
        data.Calorie_burned = Calorie_burnedhtml
        data.sleep_quality = sleep_qualityhtml
        data.Heartrate = Heartratehtml
        data.Caloriintake = Caloriintakehtml
        data.Hydration = Hydrationhtml
        data.user_id = current_user.id

        db.session.add(data)
        db.session.commit()
        return redirect(url_for('user', a=1))

    data = DATA.query.filter_by(id=id).one()
    return render_template('Update.html', data=data, id=id)

@app.route('/weekly/<int:b>')
@login_required
def weekly(b):
 weekly_calories=0
 weekly_weight=0
 weekly_hydration=0
 i=b-6
 data=DATA.query.filter_by(id=i).one()
 averageidealWt=data.Weight*7
 for i in range(i, len(current_user.datas)+1):
        data=DATA.query.filter_by(id=i).one()
        weekly_calories += (data.Caloriintake)-(data.Calorie_burned)
        weekly_weight += (data.Weight)
        weekly_hydration += (data.Hydration)
        
 week= Weekly(weeklyCalorie= weekly_calories, weeklyWeight=weekly_weight, weeklyHydration=weekly_hydration)
 db.session.add(week)
 db.session.commit()
 return render_template('weekly.html', week=week, user=current_user, avgidealWt=averageidealWt)
