from sql import SQLConnection
import pymssql
from flask import flash

def fixDate(date, time):
    date += "T"+ time
    charCount = 0
    for char in date:
        if char == '/':
            char = '-'
        charCount += 1
    if charCount <  18:
        date += ":00"
    return date

def dbPlaceBid(userType, itemId, alias, newBid):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspNewBid', (itemId, alias,newBid,))
    checkError(cursor,"Your bid for " + newBid + " was successfull!")
    con.commit()
    sqlCon.close(con)

def checkLogin(alias, password):
    result = False

    sqlCon = SQLConnection()
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspCheckLogin', (alias,password,))
    for row in cursor:
        if row['EXITO'] == 1:
            result = True

    sqlCon.close(con)
    return result

def dbBids(userType, alias, itemId):
    sqlCon = SQLConnection(userType, alias)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspViewBidsForAnAuction', (itemId,alias,))

    pastBids = []
    for row in cursor:
        pastBids.append(row)
    checkError(cursor,"")
    sqlCon.close(con)
    return pastBids

def dbComment(userType, alias, comment, auctionId):
    sqlCon = SQLConnection(userType, alias)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspNewComment', (alias,comment,
            auctionId,))
    checkError(cursor,"Your comment was added")
    sqlCon.close(con)

def dbNewListing(userType, alias,
    description, category, subCategory, listingEndDate, startingPrice, image):
    sqlCon = SQLConnection(userType, alias)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspNewAuction', (alias, description, category,
        subCategory, listingEndDate,startingPrice,image,))
    checkError(cursor,"Listing had been added!")
    con.commit()
    sqlCon.close(con)

def dbRePublishListing(userType, alias, auctionId,
    description, listingEndDate, startingPrice):
    sqlCon = SQLConnection(userType, alias)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspRestartAuction', (alias,auctionId, description,     listingEndDate,startingPrice,))
    checkError(cursor,"Listing had been added!")
    con.commit()
    sqlCon.close(con)



def getUserType(alias):
    sqlCon = SQLConnection()
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('upsGetKindOfUser', (alias,))

    for row in cursor:
        if row['Exito'] == 0:
            sqlCon.close(con)
            return None
        elif row['Administrator'] == 1:
            sqlCon.close(con)
            return 'admin'
        elif row['Agent'] == 1:
            sqlCon.close(con)
            return 'agent'
        elif row['Participant'] == 1:
            sqlCon.close(con)
            return 'participant'


def getFailedAuctionsByUser(userType, userId):
    listings = []

    if userType == 'participant':
        sqlCon = SQLConnection(userType, userId)
        con = sqlCon.connect()
        cursor = con.cursor(as_dict=True)
        #get all listings
        cursor.callproc('uspViewFailedAuctions', (userId,))

        for row in cursor:
            listings.append(row)
        checkError(cursor,"")
        sqlCon.close(con)
    return listings

def getListingsByUser(user, userId, userType):
    if user == "----":
        user = None

    listings = []

    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    #get all listings
    cursor.callproc('uspViewSellerHistory', (user, userId,))

    for row in cursor:
        listings.append(row)
    checkError(cursor,"")
    sqlCon.close(con)
    return listings

def getWinningListingsByUser(user, userId, userType):
    if user == "----":
        user = None

    listings = []

    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    #get all listings
    cursor.callproc('uspViewWonAuctionHistory', (user,userId,))
    for row in cursor:
        listings.append(row)
    checkError(cursor,"")
    sqlCon.close(con)
    return listings

def dbNewAdmin(userType,userId,name, lastName, alias,
    password,address,personalId):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspAddNewAdmin', (alias,password, name, lastName,address,personalId,))
    checkError(cursor,"Admin Successfully added to DB!")
    con.commit()
    sqlCon.close(con)

def dbNewAgent(userType, userId,name, lastName, alias,
    password,address,personalId):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspAddNewAgent', (alias,password,
        name, lastName,address,personalId,))
    checkError(cursor,"Agent Successfully added to DB!")
    con.commit()
    sqlCon.close(con)

def dbAddCard(userType,userId,alias, cardNumber, securityCode,
    cardName, expirationDate):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspAddCard', (alias,securityCode,
        cardNumber, cardName,expirationDate,))
    checkError(cursor,"Card added Successfully!")
    con.commit()
    sqlCon.close(con)

def dbAddPhones(userType,userId,alias,phones):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    for phone in phones:
        if phone!="":
            cursor.callproc('uspAddPhoneNumber', (alias,phone,))
    if len(phones)!=0:
        checkError(cursor,"Phones were added to the DB!")
    else:
        checkError(cursor,"")
    con.commit()
    sqlCon.close(con)

def dbModifyAgent(userType, userId, alias, name, lastName,address):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspModifyAgentData', (alias, name, lastName,address,))
    checkError(cursor,"Agent Modified Successfully!")
    con.commit()
    sqlCon.close(con)

def dbSetUpSystem(userType,userId,commission,minimumIncrease):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspSetSystemParameters', (commission,minimumIncrease,))
    checkError(cursor,"Values Successfully updated to DB!")
    con.commit()
    sqlCon.close(con)

def dbSuspendAgent(userType,userId,  alias):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspSuspendAgent', (alias,))
    checkError(cursor,"Agent Suspended!")
    con.commit()
    sqlCon.close(con)

def dbActivateAgent(userType, userId, alias):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspAllowAgent', (alias,))
    checkError(cursor,"Agent Activated!")
    con.commit()
    sqlCon.close(con)


def dbActivateParticipant(userType, userId, alias):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspAllowParticipant', (alias,))
    checkError(cursor,"Participant Activated!")
    con.commit()
    sqlCon.close(con)

def dbSuspendParticipant(userType, userId, alias):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspSuspendParticipant', (alias,))
    checkError(cursor,"Participant Suspended!")
    con.commit()
    sqlCon.close(con)


def dbGetAgents(userType,userId, JustSuspended):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()

    cursor = con.cursor(as_dict=True)
    if JustSuspended==0:
        cursor.callproc('uspGetAgents',(0,))
    elif JustSuspended==1:
        cursor.callproc('uspGetAgents',(1,))
    else:
        cursor.callproc('uspGetAgents',(2,))
    agents = []
    for row in cursor:
        agents.append(row['Alias'])

    checkError(cursor,"")
    #close connection
    sqlCon.close(con)
    return agents

def dbGetParticipants(userType, userid,JustSuspended):
    print 'user is type =' + userType
    print 'Hola = '+ userid
    sqlCon = SQLConnection(userType, userid)
    con = sqlCon.connect()

    cursor = con.cursor(as_dict=True)
    if JustSuspended==0:
        cursor.callproc('uspGetParticipants',(0,))
    elif JustSuspended==1:
        cursor.callproc('uspGetParticipants',(1,))
    else:
        cursor.callproc('uspGetParticipants',(2,))

    participants = []
    error=False;
    for row in cursor:
        participants.append(row['Alias'])

    checkError(cursor,"")
    #close connection
    sqlCon.close(con)
    return participants

def dbNewParticipant(userType,userId,name, lastName, alias,
    password,address,personalId,email):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspNewParticipant', (alias,password, name, lastName,address,personalId,email,))
    checkError(cursor,"Participant Successfully added to DB!")
    con.commit()
    sqlCon.close(con)

def dbModifyParticipant(userType, userId,alias, name, lastName,email,address):
    sqlCon = SQLConnection(userType, userId)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspModifyParticipantData', (alias, name, lastName,address,email,))
    checkError(cursor,"Participant Modified Successfully!")
    con.commit()
    sqlCon.close(con)

def checkError(cursor,MSJ):
    for row in cursor:
        if row['SUCCESS']==0:
            flash(row['ERROR'])
        elif MSJ!="":
            flash(MSJ)
