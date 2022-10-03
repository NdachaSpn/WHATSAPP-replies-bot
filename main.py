# -*- coding: utf-8 -*-

import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
position1=pt.locateOnScreen("pics/smiley.png",confidence=.6)

x=position1[0]
y=position1[1]

def get_message():
    global x,y
    
    position=pt.locateOnScreen("pics/smiley.png",confidence=.6)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y,duration=.05)
    pt.moveTo(x+50,y-50,duration=5)
get_message()