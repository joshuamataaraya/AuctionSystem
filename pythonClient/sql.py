import pymssql

class SQLConnection:

    """Connecto to Microsoft SQL DB """
    def __init__(self, userType=None):
        self.server = "autionDB"

        if userType == "admin":
            self.user = "Admin"
            self.password = "Admin"
        elif userType == "agent":
            self.user = "Agent1"
            self.password = "FirstAgent"
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
