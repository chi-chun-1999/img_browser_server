import mpld3
import socketio
import matplotlib.pyplot as plt

class ImgBrowser():
    def __init__(self,ip='127.0.0.1',port=8888):
        self.__connect_string = 'http://'+ip+':'+str(port)

    def show(self,fig):
        sio = socketio.Client()
        sio.connect(self.__connect_string)
        img_html = mpld3.fig_to_html(fig)
        sio.emit('img',img_html)
        sio.disconnect()
    def show_img(self,fig):
        sio = socketio.Client()
        sio.connect(self.__connect_string)
        sio.emit('img_',{'img_':fig})
        sio.disconnect()

    def clear(self):
        sio = socketio.Client()
        sio.connect(self.__connect_string)
        sio.emit('clear',0)
        sio.disconnect()




