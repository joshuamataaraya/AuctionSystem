from flask import Flask
from flask import render_template
from sql import SQLConnection

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
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


if __name__ == "__main__":
    sqlCon = SQLConnection("autionDB", 'user', "123")
    #con = sqlCon.connect()
    app.debug = True    #auto refresh
    app.run()
