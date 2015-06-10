from sql import SQLConnection

def getUserType(alias, password):
    sqlCon = SQLConnection()
    con = sqlCon.connect()

    cursor = con.cursor(as_dict=True)
    print(str(alias) + " " + str(password))

    cursor.callproc('upsGetKindOfUser', (alias, password,))

    for row in cursor:
        try:
            if row['Error'] != None:
                sqlCon.close(con)
                return False
        except KeyError:
            sqlCon.close(con)
            return True
