class User:

    def __init__(self, userid, userType, password=None):
        #set users basic values
        self.userType = userType
        self.userid = userid
        self.password = password
        if password == None:
            self.password = getPassword(userid)
        else:
            setUserPassword(userid, password)

    def is_authenticated(self):
        #this gets verified when object made so it's fine
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userid

users = []
def setUserPassword(userid, password):
    user = [userid, password]
    if user not in users:
        users.append(user)

def getPassword(userid):
    for user in users:
        if user[0] == userid:
            return user[1]
    return None
