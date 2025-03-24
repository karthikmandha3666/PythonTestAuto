import subprocess

import time

import pyautogui

subprocess.Popen("notepad.exe")
time.sleep(3)

pyautogui.write("Start Selenium python")

for _ in range(9):
    pyautogui.press("enter")

pyautogui.write("hello Selenium")

subprocess.run("taskkill /IM notepad.exe")
pyautogui.hotkey("alt", "s")
pyautogui.write("test23ert.txt")
pyautogui.press("enter")



