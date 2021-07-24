#spams with custom message

import pyautogui as pya
import time

f= open("message",'r') #reads from message file
for text in f:
    time.sleep(2)
    pya.typewrite(text)
    time.sleep(1)
    pya.press("enter")

