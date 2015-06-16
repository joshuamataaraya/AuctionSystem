import pymssql

from user import getPassword

class SQLConnection:

    """Connecto to Microsoft SQL DB """
    def __init__(self, userType=None, userName=None):
        self.server = "autionDB"

        if userType == "admin":
            self.user = userName
            self.password = getPassword(userName)
        elif userType == "agent":
            self.user = userName
            self.password = getPassword(userName)
        elif userType == "participant":
            self.user = "Participant"
            self.password = "AppParticipant"
        else:
            self.user = "App"
            self.password = "app"

    def connect(self):
        return  pymssql.connect(self.server,
            self.user,self.password,'AuctionSystem')

    def close(self, con):
        con.close()
