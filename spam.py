#install module pyautogui, webbrowser
#pip install <Module_Name>

import pyautogui as gui
import webbrowser as wb
import time

message=input("Enter message to spam: ")

#wb.open("https://web.whatsapp.com/")

time.sleep(20)

for j in "Spammer Alert Somesh":
    gui.press(j)
gui.press("enter")


while (True):
    for j in message:
        gui.press(j)
    gui.press("enter")

  
    

    
