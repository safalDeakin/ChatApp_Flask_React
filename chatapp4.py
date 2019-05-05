from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)

app.config['SECRET_KEY'] = "asduicqdqweqweqwe9209"

socketio = SocketIO(app)
users={}

@app.route( '/' ) 
def index():
    return render_template( './ChatAppPage4.html' )

@socketio.on( 'event msg' )
def incomingMessage(json):
    print json
    if(json['event']=='EVENT_PRI_MSG'):
        sendPrivateMessage(json['data'])
    elif(json['event']=='EVENT_PUB_MSG'):
        sendBroadCastMessage(json['data'])
    elif(json['event']=='REG_MSG'):
        registerUser(json['data'])

def sendPrivateMessage( jsonMessage ):
    print( 'received private message : ' + str( jsonMessage ) )
    session_id = users[jsonMessage['receiver']]
    print(session_id)
    msg =   msgAsEvent('EVENT_PRI_MSG_RESPONSE',jsonMessage['msg'],jsonMessage['sender']); 
    socketio.emit( 'server response' , msg, room= session_id )
    
def registerUser(data):
    print( 'received register msg :' + str(data))
    users[data['userName']]= request.sid
    print (users)

def msgAsEvent(event,jsonMessage,sender):
    newMessage = {'event': event, 'data':{ 'msg': jsonMessage,'sender':sender}}
    print(newMessage)
    return newMessage

def sendBroadCastMessage( json ):
    print( 'received something : ' + str( json ) )
    msg =   msgAsEvent('EVENT_PUB_MSG_RESPONSE',json['msg']); 
    socketio.emit( 'server response' , msg)

if __name__ == '__main__':
    socketio.run(app,debug =True)

