import time
import threading
import pyautogui as py
from move_cursor import move

stop_event = threading.Event()

def defogging():
  while not stop_event.is_set():  
    def check_stop():
        if stop_event.is_set():
            print("Stopping bot...")
            return True
        return False

    count = 0
    time.sleep(1)
    while not check_stop():
        count += 1  #1 find scout hangar
        reply = move("explore_imgs/scout_hangar.png")
        if reply == "not_found":
            reply = move("explore_imgs/scout_hangar1.png") 
        print(reply)
        if reply == "found":
            break
        if reply == "not_found":
            go_back()
            move_in_city()
            defogging()
            if check_stop():
                return
        time.sleep(2)

    if check_stop():
        return

    time.sleep(1)
    py.click()


    while not check_stop():
          #2 finding scout icon
        reply = move("explore_imgs/scout_icon.png")
        if reply == "found":
            break
        if reply == "not_found":
            go_back()
            move_in_city()
            defogging()
            if check_stop():
                return
        time.sleep(2)

    if check_stop():
        return

    time.sleep(1)
    py.click() #clicking on scout icon
    time.sleep(0.6)

    reply = move("explore_imgs/explore_icon.png")  #3 find explore icon
    if reply == "not_found":
        go_back()
        move_in_city()
        defogging()
        if check_stop():
            return
        time.sleep(2)

    if check_stop():
        return

    if reply == "found":
        time.sleep(1)
        py.click()  #click on explore icon

    count = 0
    while not check_stop():
        count += 1
        reply = move("explore_imgs/explore_icon1.png") #4 find next explore icon
        if reply == "found":
            break
        if reply == "not_found":
            go_back()
            move_in_city()
            defogging()
            if check_stop():
                return

    if check_stop():
        return

    time.sleep(0.5)
    py.click() #click on it 
    time.sleep(0.5)

    count = 0
    while not check_stop():
        count += 1
        reply = move("explore_imgs/dispatch_icon.png") # 5 find dispatch icon
        if reply == "found":
            break
        i=0
        while(i<4):
         if reply == "not_found":
            time.sleep(1)
            if move("explore_imgs\dispatch_glitch.png")== "found":  
             time.sleep(0.5)
             py.click()
             defogging()
            i=i+1
            if check_stop():
                return
           
            

    if check_stop():
        return

    time.sleep(1)
    py.click() #click on it 
    #move_in_city()

def move_in_city():
    reply = move("explore_imgs/city_icon.png")
    if reply == "found":
        time.sleep(0.5)
        py.click()

def go_back():
    if move("explore_imgs/go_back.png") == "found":
        time.sleep(0.5)
        py.click()
