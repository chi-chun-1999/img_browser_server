import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from img_browser import ImgBrowser
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if os.path.exists(sys.argv[1]):
        img_browser = ImgBrowser()
        fig,ax = plt.subplots()
        img = mpimg.imread(sys.argv[1])
        ax.imshow(img)
        img_browser.show(fig)
    else:
        print('File Not Found')
