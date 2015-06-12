from sql import SQLConnection
import pymssql

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

def dbNewListing(userType, alias,
    description, category, subCategory, listingEndDate, startingPrice):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspNewAuction', (alias, description, category,
        subCategory, listingEndDate,startingPrice,))

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


def getListingsByUser(user, userId, userType):
    if user == "----":
        user = None

    listings = []

    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    #get all listings
    cursor.callproc('uspViewSellerHistory', (user, userId,))

    for row in cursor:
        listings.append(row['Alias'])
    sqlCon.close(con)
    return listings

def getWinningListingsByUser(user, userId, userType):
    if user == "----":
        user = None

    listings = []

    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    #get all listings
    cursor.callproc('uspViewWonAuctionHistory', (user,userId,))
    for row in cursor:
        listings.append(row['Alias'])
    sqlCon.close(con)
    return listings

def dbNewAgent(userType,name, lastName, alias,
    password,address,personalId):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)

    cursor.callproc('uspAddNewAgent', (alias,password, 
        name, lastName,address,personalId,))

    con.commit()
    sqlCon.close(con)

def dbAddPhones(userType,alias,phones):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    for phone in phones:
        if phone!="":
            cursor.callproc('uspAddPhoneNumber', (alias,phone,))
    con.commit()
    sqlCon.close(con)

def dbModifyAgent(userType, alias, name, lastName,address):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspModifyAgentData', (alias, name, lastName,address,))
    con.commit()
    sqlCon.close(con)

def dbSuspendAgent(userType, alias):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspSuspendAgent', (alias,))
    con.commit()
    sqlCon.close(con)

def dbActivateAgent(userType, alias):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspAllowAgent', (alias,))
    con.commit()
    sqlCon.close(con)


def dbActivateParticipant(userType, alias):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspAllowParticipant', (alias,))
    con.commit()
    sqlCon.close(con)

def dbSuspendParticipant(userType, alias):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspSuspendParticipant', (alias,))
    con.commit()
    sqlCon.close(con)


def dbGetAgents(userType,JustSuspended):
    sqlCon = SQLConnection(userType)
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
    #close connection
    sqlCon.close(con)
    return agents

def dbGetParticipants(userType,JustSuspended):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()

    cursor = con.cursor(as_dict=True)
    if JustSuspended==0:
        cursor.callproc('uspGetParticipants',(0,))
    elif JustSuspended==1:
        cursor.callproc('uspGetParticipants',(1,))
    else:
        cursor.callproc('uspGetParticipants',(2,))

    participants = []
    for row in cursor:
        participants.append(row['Alias'])
    #close connection
    sqlCon.close(con)
    return participants

def dbNewParticipant(userType,name, lastName, alias,
    password,address,personalId,email):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspNewParticipant', (alias,password, name, lastName,address,personalId,email,))
    con.commit()
    sqlCon.close(con)

def dbModifyParticipant(userType, alias, name, lastName,email,address):
    sqlCon = SQLConnection(userType)
    con = sqlCon.connect()
    cursor = con.cursor(as_dict=True)
    cursor.callproc('uspModifyParticipantData', (alias, name, lastName,address,email,))
    con.commit()
    sqlCon.close(con)
