import pymssql

class SQLConnection:

    """Connecto to Microsoft SQL DB """
    def __init__(self, userType=None):
        self.server = "autionDB"

        if userType == "admin":
            self.user = "admin"
            self.password = "Admin"
        elif userType == "agent":
            self.user = "App"
            self.password = "app"
        elif userType == "participant":
            self.user = "user"
            self.password = "123"
        else:
            self.user = "App"
            self.password = "app"

    def connect(self):
        return  pymssql.connect(self.server,
            self.user,self.password,'AuctionSystem')

    def close(self, con):
        con.close()
