import cv2 as cv
import pyautogui as py
import numpy as np
import time 
from PIL import Image


def screenshot():
    time.sleep(1)
    ss = py.screenshot()
    
    #converting screenshot into OpenCV format
    ss_cv = cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)
    #converting screenshot to grayscale
    ss_cv_grayscale = cv.cvtColor(ss_cv,cv.COLOR_RGB2GRAY)
    return ss_cv_grayscale