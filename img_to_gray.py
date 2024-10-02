import cv2 as cv
import pyautogui as py
import numpy as np
import time 
from PIL import Image

def input2GRAYSCALE(image_path):
    cv_img = cv.imread(image_path) #home.png
    cv_img_grayscale = cv.cvtColor(cv_img, cv.COLOR_RGB2GRAY)
    return cv_img_grayscale