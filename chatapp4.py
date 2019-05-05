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
    if(json['event']=='EVENT_PRI_MSG'):
        sendPrivateMessage(json['data'])
    elif(json['event']=='EVENT_PUB_MSG'):
        sendBroadCastMessage(json['data'])
    elif(json['event']=='REG_MSG'):
        registerUser(json['data'])

def sendPrivateMessage( json ):
    print( 'received something : ' + str( json ) )
    session_id = users[json['user']]
    msg =   msgAsEvent('EVENT_PRI_MSG_RESPONSE',json['msg']); 
    socketio.emit( 'private room' , msg, room= session_id )
    
def registerUser(user_name):
    print( 'received private msg :' + user_name)
    users[user_name]= request.sid
    print (users)

def msgAsEvent(event,jsonMessage):
    newMessage = {'event': event, 'msg': jsonMessage}
    print(newMessage)
    return jsonMessage

def sendBroadCastMessage( json ):
    print( 'received something : ' + str( json ) )
    msg =   msgAsEvent('EVENT_PUB_MSG_RESPONSE',json['msg']); 
    socketio.emit( 'private room' , msg)

if __name__ == '__main__':
    socketio.run(app,debug =True)

