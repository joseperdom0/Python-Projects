import random
import time
import pyautogui
import datetime

counter = 0
print(datetime.datetime.now())
now = datetime.datetime.now()

while now.hour < 12:
    print("testing",counter)
    print(now.hour,':',now.minute)
    counter += 1
    time.sleep(random.randint(30,120))
    #pyautogui.move(5)
    pyautogui.press('f13')
    now = datetime.datetime.now()

print("Time is ",now)

