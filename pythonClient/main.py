from flask import (Flask, render_template, request,
                    flash, redirect, url_for)
from flask_login import (LoginManager, login_user,
                        logout_user, login_required )
from sql import SQLConnection
from user import User

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3nan --~XHH!jmN]LWX/,?RT'

#login manager
loginManager = LoginManager()

@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        category1 = "hola"
        category2 = "hola"

        cursor.callproc('uspViewAvailableAuctions', (category1, category2,))

        return render_template('index.html', entries=cursor)


    return render_template('index.html')


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

            return redirect(request.args.get('next') or url_for('index'))


    #cursor.callproc('uspAllowAgent', ('zeth',))

    #for row in cursor:
    #    print("return = %r" % (row,))

    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/userPage")
@login_required
def userPage():
    return render_template('userPage.html')

@app.route("/newListing")
@login_required
def newListing():
    return render_template('newListing.html')

#Admin stuff
@app.route("/newAgent")
@login_required
def newAgent():
    return render_template('newAgent.html')

@app.route("/modifyAgent")
@login_required
def modifyAgent():
    return render_template('modifyAgent.html')

@app.route("/reactivateAgent")
@login_required
def reactivateAgent():
    return render_template('reactivateAgent.html')

@app.route("/suspendAgent")
@login_required
def suspendAgent():
    return render_template('suspendAgent.html')

#Agent stuff

#Listing stuff
@app.route("/showListings")
@login_required
def showListings():
    return render_template('showListings.html')


#get user's id
@loginManager.user_loader
def load_user(userid):
    return User(userid)

@loginManager.unauthorized_handler
def unauthorized():
    flash("You are not logged in!")
    # do stuff
    return redirect(url_for('login'))

if __name__ == "__main__":
    sqlCon = SQLConnection("autionDB", 'user', "123")
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    loginManager.init_app(app)

    app.debug = True    #auto refresh
    app.run()
