import cv2 as cv
import pyautogui as py
import numpy as np
import time 
from PIL import Image
from take_screenshot import screenshot
from img_to_gray import input2GRAYSCALE

#finds location of center of required image
def match(img2find):
    ss_gray = screenshot() #takes an ss and gives grayscale output
    gray_input = input2GRAYSCALE(img2find)  #converts input to grayscale
    match_result = cv.matchTemplate(ss_gray, gray_input, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(match_result)
    print(max_val)
    threshold = 0.6
    if(max_val>threshold):
      center_x = (min_loc[0] + max_loc[0]) // 2

      # Calculate the y-coordinate of the center
      center_y = (min_loc[1] + max_loc[1]) // 2
      image_width, image_height = gray_input.shape[::-1]
      top_left = max_loc
      center = (top_left[0] + image_width // 2, top_left[1] + image_height // 2)
      print(f"Center coordinates: {center}")
      return "found",center
    else:
       #print("not found")
       return "not_found",0
    




    
