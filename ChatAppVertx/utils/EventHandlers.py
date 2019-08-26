from MessageWrapper import MessageWrapper
from UserSession import Session

class EventHandlers(object):

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super (EventHandlers,cls).__new__(cls)
        return cls.instance

    def sendEvent(self, eventName, jsonMessage, broadCast ):
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
        return self.sendEvent('REG_MSG_RESPONSE', jsonMessage, False)

    def handleEvent(self, json):
        
        if (json['event']=='EVENT_PRI_MSG'):
            return self.sendEvent('EVENT_PRI_MSG_RESPONSE', json['data'],False)
        elif(json['event']=='EVENT_PUB_MSG'):
            return self.sendEvent('EVENT_PUB_MSG_RESPONSE',json['data'], True)
        elif(json['event']=='REG_MSG'):
            return self.registerUser(json['data'])


EventHandler = EventHandlers()