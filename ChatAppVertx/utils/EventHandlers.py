from MessageWrapper import MessageWrapper
from UserSession import UserSession
from Socket import chatSocket 


class EventHandlers(object):
    Session = UserSession()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super (EventHandlers,cls).__new__(cls)
        return cls.instance


    def initSocket(self,app):
        chatSocket.initSocket(app,self)
    
    def runApp(self,app, debug, host, port):
        chatSocket.run(app,debug, host, port)

    def sendEvent(self,eventName, jsonMessage, broadcast):
        session_id = self.Session.getSessionId(jsonMessage['receiver'])
        msg =   MessageWrapper.wrap(eventName,jsonMessage['msg'],jsonMessage['sender']); 
        chatSocket.emit( msg, session_id , broadcast)
    
    def registerUser(self,data):
        self.Session.registerUser(data['userName'])
        jsonMessage = {
            'msg' : 'Successfully register',
            'sender' : 'Server',
            'receiver' : data['userName']
            };
        self.sendEvent('REG_MSG_RESPONSE', jsonMessage, False)

    def handleEvent(self,event):
        print event
        if (event['event']=='EVENT_PRI_MSG'):
            self.sendEvent('EVENT_PRI_MSG_RESPONSE', json['data'],False)
        elif(event['event']=='EVENT_PUB_MSG'):
            self.sendEvent('EVENT_PUB_MSG_RESPONSE',json['data'], True)
        elif(event['event']=='REG_MSG'):
            self.registerUser(event['data'])
    
    @chatSocket.socketio.on('event msg' )
    def incomingMessage(json):
        print "incoming Message From Socket :: " + json
        EventHandler.handleEvent(json)

EventHandler = EventHandlers()