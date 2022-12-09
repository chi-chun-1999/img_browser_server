from flask import Flask, render_template
from flask_socketio import SocketIO  # 加上這行
import json



app = Flask(__name__)

socketio = SocketIO(app)  # 加上這行
g_data = None
g_img = None

@app.route('/')
def index():
    global g_data
    print(g_data)
    if g_data != None:
        show = g_data['foo']
        return show
    else:
        return 'hello socketio'
        
@app.route('/img')
def img():
    
    global g_img
    if g_img != None:
        return g_img
    else:
        return 'Without Image'

@socketio.on('send')
def chat(data):
    #socketio.emit('get', data)
    global g_data
    g_data = data
    print(data)
    return 'get data'

@socketio.on('img')
def get_img(data):
    #socketio.emit('get', data)
    #print(data)
    global g_img
    #g_img = json.dumps(data)
    g_img = data
    return 'get data'

@socketio.on('clear')
def clear_img(data):
    #socketio.emit('get', data)
    #print(data)
    global g_img
    #g_img = json.dumps(data)
    g_img = None
    return 'clear img'


@socketio.on('test')
def test():
    socketio.send("test")


if __name__ == "__main__":
    socketio.run(app,debug=True)
