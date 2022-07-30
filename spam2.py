#install module pyautogui
#pip install <Module_Name>

import pyautogui as gui
import time

message=input("Open Whatsapp web and select person to spam\nI M P O R T A N T\nCopy the message to spam\n")
input("After copying press any key")
print("Select the contact and wait for 10 sec")

time.sleep(10)

for j in "Spammer Alert ":
    gui.press(j)
gui.press('enter')

while (True):
    gui.hotkey('ctrl', 'v')
    gui.press('enter')

