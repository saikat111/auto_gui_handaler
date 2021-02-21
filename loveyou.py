import pyautogui
import time
count = 0
while True:
    time.sleep(1)
    pyautogui.typewrite("I love you 💕❤❤❤❤💕❤❤❤❤💕")
    pyautogui.press("enter")
    count = count + 1
    print("I love you")
    print("❤❤❤❤💕❤❤❤❤💕 ")
    print(count)
    time.sleep(1)

