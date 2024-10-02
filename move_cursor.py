from find_loc import match
import pyautogui as py
def move(img):
    reply, coordinates = match(img)
    if(reply =="found"):
        py.moveTo(coordinates[0],coordinates[1])  
        return "found"
    if(reply =="not_found"):
        return  "not_found"


