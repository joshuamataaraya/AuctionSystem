#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, render_template, request,
                    flash, redirect, url_for)
from flask_login import (LoginManager, login_user,
                        logout_user, login_required, current_user)

from user import User
from sql import SQLConnection
from db import *

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3nan --~XHH!jmN]LWX/,?RT'

#login manager
loginManager = LoginManager()

@app.route("/", methods=['GET', 'POST'])
@login_required
def index():

    sqlCon = SQLConnection(current_user.userType)
    con = sqlCon.connect()

    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspViewCategories')

    cate1 = []
    cate2 = []

    for row in cursor:
        if (row['category']) not in cate1:
            cate1.append(row['category'])
        if (row['subCategory']) not in cate2:
            cate2.append(row['subCategory'])

    #close connection
    sqlCon.close(con)

    cate1.sort()
    cate2.sort()

    if request.method == 'POST':
        try: #if user selected newBid button
            item = request.values.get('idItem')
            #show them all past bids and let them bid
            return redirect(url_for('bids', itemId=item))
            
            
        except Exception:
            category1 = request.form['category1']
            category2 = request.form['category2']

            if category1 == "----":
                category1 = None
            if category2 == "----":
                category2 = None

            sqlCon = SQLConnection(current_user.userType)
            con = sqlCon.connect()
            cursor = con.cursor(as_dict=True)
            #get all listings
            cursor.callproc('uspViewAvailableAuctions', (current_user.userid,
                        category1, category2,))
            entries = []
            for row in cursor:
                entries.append(row)

            sqlCon.close(con)
            return render_template('index.html',
                entries=entries, cate1=cate1, cate2=cate2)


    return render_template('index.html', cate1 = cate1, cate2 = cate2)


@app.route("/login", methods=['GET', 'POST'])
def login():
    #if someone tried to login
    if request.method == 'POST':
        alias = request.form['alias'].encode("UTF-8")
        password = request.form['password'].encode("UTF-8")

        user = User(alias, getUserType(alias))

        if checkLogin(alias, password):    #if valid user
            login_user(user) #login the user
            #show login msg
            flash('You are now logged in!')
            return redirect(request.args.get('next') or url_for('index'))
        else:
            flash("Wrong Login!")

    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/userPage", methods=['GET', 'POST'])
@login_required
def userPage():
    users = dbGetParticipants(current_user.userType, 0)
    
    mySold = getListingsByUser(current_user.userid,
            current_user.userid, current_user.userType)
    myWon = getWinningListingsByUser(current_user.userid,
    current_user.userid, current_user.userType)

    if request.method == 'POST':
       
        auction = request.values.get('idItem')
        comment = request.values.get('textComment')
            
        if comment != None:
            #add the comment
            dbComment(current_user.userType, current_user.userid,
                comment, auction)
            flash("Your comment was added")
              
        else:
            user = request.form['user']
            winningBids = request.form['winningBids']
            
            listings = []
            winningListings = []

            if user != '----':
                listings= getListingsByUser(user,
            current_user.userid, current_user.userType)
            if winningBids != '----':
                winningListings= getWinningListingsByUser(winningBids,
            current_user.userid, current_user.userType)
           
           
            return render_template('userPage.html',
                user=users, listings=listings, myWon = myWon, mySold = mySold,
                    winningListings=winningListings)


    return render_template('userPage.html', user=users,
        myWon = myWon, mySold = mySold)


@app.route('/bid/item/<itemId>', methods=['GET', 'POST'])
@login_required
def bids(itemId):
  
    if request.method == 'POST':
        newBid = request.form['newBid']
        dbPlaceBid(current_user.userType,
                itemId, current_user.userid, newBid)

        flash("Your bid for " + newBid + " was successfull!")
    
    pastBids = dbBids(current_user.userType, current_user.userid,itemId)
    
    return render_template('bids.html', entries = pastBids)

@app.route("/newListing", methods=['GET', 'POST'])
@login_required
def newListing():
    sqlCon = SQLConnection(current_user.userType)
    con = sqlCon.connect()

    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspViewCategories')

    cate1 = []
    cate2 = []

    for row in cursor:
        if (row['category']) not in cate1:
            cate1.append(row['category'])
        if (row['subCategory']) not in cate2:
            cate2.append(row['subCategory'])

    #close connection
    sqlCon.close(con)

    cate1.sort()
    cate2.sort()

    if request.method == 'POST':
        category1 = request.form['category1']
        category2 = request.form['category2']
        description = request.form['description']
        listingEndDate = request.form['listingEndDate']
        listingEndTime = request.form['listingEndTime']
        startingPrice = request.form['startingPrice']

        listingEndDate += "T"+ listingEndTime
        for char in listingEndDate:
            if char == '/':
                char = '-'

        dbNewListing(current_user.userType, current_user.userid,
            description, category1, category2, listingEndDate,
                startingPrice)
        flash("Listing had been added!")

    return render_template('newListing.html', cate1=cate1, cate2=cate2)



#Admin stuff    ***
@app.route("/newAdmin", methods=['GET', 'POST'])
@login_required
def newAdmin():
    if request.method == 'POST':
        name = request.form['adminFirstName']
        lastName = request.form['adminLastName']
        alias = request.form['adminAlias']
        password = request.form['adminPassword']
        personalId=request.form['adminId']
        address=request.form['adminAddress']
        telCel=request.form['telCel']
        telWork=request.form['telWork']
        telHome=request.form['telHome']
        telOther=request.form['telOther']
        phones=[telCel,telWork,telHome,telOther]
        #add new Agent
        dbNewAdmin(current_user.userType,
            name, lastName, alias, password,
            address,personalId)
        dbAddPhones(current_user.userType,alias,phones)
        flash("Agent Successfully added to DB!")

    return render_template('newAdministrator.html')
@app.route("/newAgent", methods=['GET', 'POST'])
@login_required
def newAgent():
    if request.method == 'POST':
        name = request.form['agentFirstName']
        lastName = request.form['agentLastName']
        alias = request.form['agentAlias']
        password = request.form['agentPassword']
        personalId=request.form['agentId']
        address=request.form['agentAddress']
        telCel=request.form['telCel']
        telWork=request.form['telWork']
        telHome=request.form['telHome']
        telOther=request.form['telOther']
        phones=[telCel,telWork,telHome,telOther]
        #add new Agent
        dbNewAgent(current_user.userType,
            name, lastName, alias, password,
            address,personalId)
        dbAddPhones(current_user.userType,alias,phones)
        flash("Agent Successfully added to DB!")

    return render_template('newAgent.html')

@app.route("/modifyAgent", methods=['GET', 'POST'])
@login_required
def modifyAgent():

    agents = dbGetAgents(current_user.userType,2)

    if request.method == 'POST':
        alias = request.form['agentSelect']
        name = request.form['agentFirstName']
        lastName = request.form['agentLastName']
        agentAddress=request.form['agentAddress']

        dbModifyAgent(current_user.userType, alias, name, lastName,address)
        flash("Agent Modified Successfully!")

    return render_template('modifyAgent.html', agents=agents)

@app.route("/reactivateAgent", methods=['GET', 'POST'])
@login_required
def reactivateAgent():
    agents = dbGetAgents(current_user.userType,1)

    if request.method == 'POST':
        alias = request.form['agentSelect']
        dbActivateAgent(current_user.userType, alias)
        flash("Agent Activated!")
    if len(agents)==0:
            flash("we dont have Suspended Agents")

    return render_template('reactivateAgent.html', agents=agents)

@app.route("/suspendAgent", methods=['GET', 'POST'])
@login_required
def suspendAgent():
    agents = dbGetAgents(current_user.userType,0)
    if request.method == 'POST':
        alias = request.form['agentSelect']

        dbSuspendAgent(current_user.userType, alias)

        flash("Agent Suspended!")
    if len(agents)==0:
        flash("We dont have Activated Agents")
    return render_template('suspendAgent.html', agents=agents)
@app.route("/SetUp", methods=['GET', 'POST'])
@login_required
def SetUp():
    if request.method == 'POST':
        commission = request.form['commission']
        minimumIncrease = request.form['minimumIncrease']
        #add new Agent
        dbSetUpSystem(current_user.userType,
            commission,minimumIncrease)
        flash("Values Successfully updated to DB!")

    return render_template('setUp.html')


#Agent stuff ***
@app.route("/addCard", methods=['GET', 'POST'])
@login_required
def addCard():
    participants = dbGetParticipants(current_user.userType,2)
    if request.method == 'POST':
        participant = request.form['participantSelect']
        cardNumber = request.form['cardNumber']
        securityCode = request.form['securityCode']
        cardName = request.form['cardName']
        expirationDate = request.form['expirationDate']
         #add new Agent
        for char in expirationDate :
            if char == '/':
                char = '-'
        dbAddCard(current_user.userType,
            participant, cardNumber, securityCode, cardName, expirationDate)

        # dbAddPhones(current_user.userType,alias,phones)

        flash("Participant Successfully added to DB!")

    return render_template('addCard.html',participants=participants)
@app.route("/newParticipant", methods=['GET', 'POST'])
@login_required
def newParticipant():
    if request.method == 'POST':
        name = request.form['participantFirstName']
        lastName = request.form['participantLastName']
        alias = request.form['participantAlias']
        password = request.form['participantPassword']
        personalId=request.form['participantId']
        address=request.form['participantAddress']
        email=request.form['participantEmail']
        telCel=request.form['telCel']
        telWork=request.form['telWork']
        telHome=request.form['telHome']
        telOther=request.form['telOther']
        phones=[telCel,telWork,telHome,telOther]

        #add new Agent
        dbNewParticipant(current_user.userType,
            name, lastName, alias, password,address,personalId,email)

        dbAddPhones(current_user.userType,alias,phones)

        flash("Participant Successfully added to DB!")

    return render_template('newParticipant.html')

@app.route("/modifyParticipant", methods=['GET', 'POST'])
@login_required
def modifyParticipant():

    agents = dbGetParticipants(current_user.userType,2)

    if request.method == 'POST':
        alias = request.form['participantSelect']
        name = request.form['FirstName']
        lastName = request.form['participantLastName']
        email=request.form['participantEmail']
        address=request.form['participantAddress']

        dbModifyParticipant(current_user.userType, alias, name, lastName,email,address)
        flash("Participant Modified Successfully!")

    return render_template('modifyParticipant.html', agents=agents)

@app.route("/reactivateParticipant", methods=['GET', 'POST'])
@login_required
def reactivateParticipant():
    agents = dbGetParticipants(current_user.userType,1)

    if request.method == 'POST':
        alias = request.form['participantSelect']
        dbActivateParticipant(current_user.userType, alias)
        flash("Participant Activated!")
    if len(agents)==0:
        flash("We dont have Suspended Participants")
    return render_template('reactivateParticipant.html', agents=agents)

@app.route("/suspendParticipant", methods=['GET', 'POST'])
@login_required
def suspendParticipant():
    agents = dbGetParticipants(current_user.userType,0)

    if request.method == 'POST':
        alias = request.form['participantSelect']
        dbSuspendParticipant(current_user.userType, alias)
        flash("Participant Suspended!")

    if len(agents)==0:
        flash("We dont have Suspended Participants")

    return render_template('suspendParticipant.html', agents=agents)


#Listing stuff
@app.route("/showListings")
@login_required
def showListings():
    return render_template('showListings.html')

#get user's id
@loginManager.user_loader
def load_user(userid):
    return User(userid, getUserType(userid))

@loginManager.unauthorized_handler
def unauthorized():
    flash("You are not logged in!")
    # do stuff
    return redirect(url_for('login'))

if __name__ == "__main__":
    loginManager.init_app(app)

    app.debug = True    #auto refresh
    app.run()
