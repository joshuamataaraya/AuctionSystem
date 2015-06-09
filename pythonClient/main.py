from flask import Flask, render_template, request, flash
from flask_login import LoginManager, login_user
from sql import SQLConnection
from user import User

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3nan --~XHH!jmN]LWX/,?RT'

#login manager
loginManager = LoginManager()

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    #if someone tried to login
    if request.method == 'POST':
        alias = request.form['alias'].encode("UTF-8")
        #password = request.form['password'].encode("UTF-8")

        user = User(alias)
        if user is not None:    #if valid user
            login_user(user)
            #show login msg
            flash('You are now logged in!')



    cursor.callproc('uspAllowAgent', ('zeth',))

    for row in cursor:
        print("return = %r" % (row,))

    return render_template('login.html')

@app.route("/newListing")
def newListing():
    return render_template('newListing.html')

#Agent stuff
@app.route("/newAgent")
def newAgent():
    return render_template('newAgent.html')

@app.route("/modifyAgent")
def modifyAgent():
    return render_template('modifyAgent.html')

@app.route("/reactivateAgent")
def reactivateAgent():
    return render_template('reactivateAgent.html')

@app.route("/suspendAgent")
def suspendAgent():
    return render_template('suspendAgent.html')

#Listing stuff
@app.route("/showListings")
def showListings():
    return render_template('showListings.html')


#get user's id
@loginManager.user_loader
def load_user(userid):
    return User.get(userid)


if __name__ == "__main__":
    sqlCon = SQLConnection("autionDB", 'user', "123")
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    loginManager.init_app(app)

    app.debug = True    #auto refresh
    app.run()
