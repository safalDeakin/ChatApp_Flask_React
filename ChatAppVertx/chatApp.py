from flask import Flask, render_template
from utils.EventHandlers import EventHandler

app = Flask(__name__)

app.config['SECRET_KEY'] = "asduicqdqweqweqwe9209"

DEFAULT_TEMPLATE = './chatPage.html' 

EventHandler.initSocket(app)

@app.route( '/' ) 
def index():
    return render_template(DEFAULT_TEMPLATE )

if __name__ == '__main__':
    EventHandler.runApp(app,True, '127.0.0.1', 9999)


    


