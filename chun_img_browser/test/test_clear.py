import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from img_browser import ImgBrowser

if __name__ == '__main__':
    img_browser = ImgBrowser()
    img_browser.clear()
