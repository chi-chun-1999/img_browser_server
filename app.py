from flask import Flask, render_template
from flask_socketio import SocketIO  # 加上這行
import json
import mpld3



app = Flask(__name__)


socketio = SocketIO(app,max_http_buffer_size = 50*1000*1000)  # 加上這行


g_data = None
g_img = None
g_img_ = None

@app.route('/')
@app.route('/home')
def index():
    return render_template("hello.html")
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

@socketio.on('img_')
def get_img_(data):
    #socketio.emit('get', data)
    #print(data)
    img = data['img_']
    
    global g_img
    #g_img = json.dumps(data)
    g_img = mpld3.fig_to_d3(img)
    return 'get data'

if __name__ == "__main__":
    socketio.run(app,port=8888,debug=True)
