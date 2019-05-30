from flask import request
class UserSession :
    _userSessionInstance = None;
    users={}

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super (UserSession,cls).__new__(cls)
        return cls.instance

    def registerUser(self,userName):
        self.users[userName]= request.sid
        print("Registration Successfull for " + userName)
    
    def getSessionId(self,id):
        return self.users[id]

