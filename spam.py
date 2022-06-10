#install module pyautogui, webbrowser
#pip install <Module_Name>

import pyautogui as gui
import webbrowser as wb
import time

message=input("Open Whatsapp web and select person to spam\nEnter message to spam: ")
print("Select the contact and wait for 20 sec")
#wb.open("https://web.whatsapp.com/")

time.sleep(20)

for j in "Spammer Alert ":
    gui.press(j)
gui.press("enter")


while (True):
    for j in message:
        gui.press(j)
    gui.press("enter")

  
    

    
