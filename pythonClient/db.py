from sql import SQLConnection

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
