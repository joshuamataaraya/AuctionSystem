import pymssql

class SQLConnection:

    """Connecto to Microsoft SQL DB """
    def __init__(self, ip, user, password):
        self.server = ip
        self.user = user
        self.password = password

    def connect(self):
        conn = pymssql.connect(self.server,
        self.user,self.password,
        'AuctionSystem')
        return conn
