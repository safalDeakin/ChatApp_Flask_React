from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)

app.config['SECRET_KEY'] = "asduicqdqweqweqwe9209"

socketio = SocketIO(app)

@app.route( '/' ) 
def index():
    return render_template( './ChatAppPage3.html' )

# only has one event "message"
@socketio.on( 'message' )
def handle_my_custom_event( json ):
    print( 'received something : ' +  str(json)  )
    send(json)

# in emit we can use custom events
@socketio.on( 'client event' )
def handle_my_custom_event( json ):
    print( 'received something : ' +  str(json)  )
    socketio.emit('server response', json)
    

if __name__ == '__main__':
    socketio.run(app,debug =True)