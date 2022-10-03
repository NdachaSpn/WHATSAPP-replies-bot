# -*- coding: utf-8 -*-

import pyautogui as pt
from time import sleep

while True:
    posXY=pt.position
    print(posXY)
    sleep(1)
    
    if posXY==0:
        break
    