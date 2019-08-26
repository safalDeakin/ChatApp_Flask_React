from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)

app.config['SECRET_KEY'] = "asduicqdqweqweqwe9209"

socketio = SocketIO(app)

@app.route( '/' ) 
def index():
    return render_template( './ChatAppPage.html' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
    print( 'received something : ' + str( json ) )
    socketio.emit( 'my response' , json)
    
if __name__ == '__main__':
    socketio.run(app,debug =True)