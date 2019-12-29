from .MessageWrapper import MessageWrapper
from .UserSession  import Session

class EventHandlers(object):

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super (EventHandlers,cls).__new__(cls)
        return cls.instance

    def getResponse(self, eventName, jsonMessage, broadCast ):
        if broadCast :
            session_id = None
        else :
            session_id = Session.getSessionId(jsonMessage['receiver'])
            
        msg =   MessageWrapper.wrap(eventName,jsonMessage['msg'],jsonMessage['sender']);        
        return msg, session_id , broadCast
    
    def registerUser(self, data):
        Session.registerUser(data['userName'])
        jsonMessage = {
            'msg' : 'Successfully register',
            'sender' : 'Server',
            'receiver' : data['userName']
            };
        return self.getResponse('REG_MSG_RESPONSE', jsonMessage, False)

    def sendUsers(self,data):
        jsonMessage = {};
        if(data['userName'] !=None):
            jsonMessage = {
                'msg' :  {
                        'users' : Session.getUsers()},
                'sender' : 'Server',
                'receiver' : data['userName'] 
            } ;    

        return self.getResponse('EVENT_REQUEST_USERS_RESPONSE', jsonMessage, False)

    def handleEvent(self, json):
        
        if (json['event']=='EVENT_PRI_MSG'):
            return self.getResponse('EVENT_PRI_MSG_RESPONSE', json['data'],False)
        elif(json['event']=='EVENT_PUB_MSG'):
            return self.getResponse('EVENT_PUB_MSG_RESPONSE',json['data'], True)
        elif(json['event']=='REG_MSG'):
            return self.registerUser(json['data'])
        elif(json['event']=='EVENT_REQUEST_USERS'):
            return self.sendUsers( json['data'])
        else:
            return self.getResponse('EVENT_EROOR',"invalid cmd" ,False)


EventHandler = EventHandlers()