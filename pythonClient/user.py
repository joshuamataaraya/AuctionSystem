class User:

    def __init__(self, userid, userType):
        #set users basic values
        self.userType = userType
        self.userid = userid

    def is_authenticated(self):
        #this gets verified when object made so it's fine
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userid
