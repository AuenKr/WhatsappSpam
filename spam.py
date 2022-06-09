#install module pyautogui, webbrowser
#pip install <Module_Name>

import pyautogui as gui
import webbrowser as wb
import time

message=input("Enter message to spam: ")

wb.open("https://web.whatsapp.com/")

time.sleep(30)

while (1):
    for j in message:
        gui.press(j)
    gui.press("enter")

    

    
