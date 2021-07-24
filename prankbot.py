#spams same word multiple times

import pyautogui as pya
import time

times= 10;
while times>0:
    time.sleep(2)
    pya.typewrite("hola")
    time.sleep(1)
    pya.press("enter")
    times= times-1
