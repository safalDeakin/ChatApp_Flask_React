from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET_KEY'] = "asduicqdqweqweqwe9209"

socketio = SocketIO(app)

@app.route( '/' ) 
def index():
    return render_template( './ChatAppPage2.html' )

@socketio.on( 'message' )
def handle_my_custom_event( msg ):
    print( 'received something : ' + msg )
    send(msg)
    

if __name__ == '__main__':
    socketio.run(app,debug =True)