class User:

    def __init__(self, userid):
        #set users basic values
        self.userid = userid
        #is it a valid user?
        if self.isValid() is False:
            return None
        #set type of user we are
        self.userType = self.setUserType()

    def setUserType(self):
        return "admin" #placeholder need return dynamic type

    #FLASK needs this for login management v
    def isValid(self):
        return True #this needs to validate with server

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userid
