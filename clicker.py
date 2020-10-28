#These are all of the modules we will be using to clik the cookie
from PIL import ImageGrab, ImageOps
import pyautogui
import time

still_click = False

def clickcookie():
    #THis will be the line of code to click the cookie

    still_click = True
    while still_click == True:
        pyautogui.click(clicks=100000000000000, interval=0.01, x=800, y=500)



clickcookie()
