from flask_socketio import SocketIO, emit, send

class ServerSocket(object):
    DEFAULT_EVENT = 'event msg' 
    socketio = SocketIO()
    
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(ServerSocket,cls).__new__(cls)
        return cls.instance

    def initSocket(self,app,handler):
        self.socketio.init_app(app)
        self.handler = handler

    def emit(self,msg, channel, broadcast):
        if broadcast:
            self.socketio.emit( 'server response' , msg)
        else:
            self.socketio.emit( 'server response' , msg, room = channel )     

    def run(self,_app,_debug, _host, _port ):
        print "Socket starting program"
        self.socketio.run(_app,debug = _debug, host = _host, port= _port)

chatSocket = ServerSocket()
