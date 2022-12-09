import mpld3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import socketio


def test_hist():
    x = [1,2,3]
    y = [2,3,5]
    fig1 = plt.figure()
    plt.xlabel("xlabel 1")
    plt.ylabel("ylabel 1")
    plt.title("Plot 1")
    plt.legend()
    plt.bar(x,y, label = 'label for bar', color = 'y')
    html1 = mpld3.fig_to_html(fig1)
    return html1

def test_img():
    fig1,ax = plt.subplots()
    img = mpimg.imread('./slice.png')
    ax.imshow(img)
    html1 = mpld3.fig_to_html(fig1)
    return html1



sio = socketio.Client()

sio.connect('http://127.0.0.1:5000')
print(sio.sid)

img_html = test_img()
#print(img_html)
#sio.emit('img',{'foo':'2ar'})
sio.emit('img',img_html)
#sio.emit('clear',0)
sio.disconnect()


