import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from img_browser import ImgBrowser
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    img_browser = ImgBrowser()
    fig,ax = plt.subplots()
    img = mpimg.imread('../../slice.png')
    print(np.shape(img))
    ax.imshow(img)
    img_browser.show(fig)
    



