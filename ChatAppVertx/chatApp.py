from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from utils.EventHandlers import EventHandler


DEFAULT_EVENT = 'event msg' 
DEFAULT_TEMPLATE = './chatPage.html' 
app = Flask(__name__)

app.config['SECRET_KEY'] = "asduicqdqweqweqwe9209"

socketIO = SocketIO(app)

@app.route( '/' ) 
def index():
    return render_template(DEFAULT_TEMPLATE )

def emit(msg, channel, broadCast):
    if broadCast:
        socketIO.emit( 'server response' , msg)
    else:
        socketIO.emit( 'server response' , msg, room = channel ) 
        
@socketIO.on('event msg' )
def incomingMessage(json):
    print "incoming Message From Socket :: "
    print json
    handleMessage(json)  

def handleMessage(json):
    responseMsg , channel, broadCast = EventHandler.handleEvent(json)  
    emit(responseMsg,channel,broadCast) 
    
if __name__ == '__main__':
    print "Socket is starting program"
    socketIO.run(app, debug = True, host = '127.0.0.1', port = 9999)


    


