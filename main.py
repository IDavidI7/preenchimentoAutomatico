import pyautogui
import time

time.sleep(7)

for i in range(5):
    if i + 1 == 1:
        x, y = 85, 293
    elif i + 1 == 2:
        x, y = 189, 361
    elif i + 1 == 3:
        x, y = 474, 441
    elif i + 1 == 4:
        x, y = 207, 501
    elif i + 1 == 5:
        x, y = 623, 484
    for c in range(93):
        pyautogui.click(x, y, clicks=3, interval=0.0, button='left')
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'c', interval=0.1)
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'tab', interval=0.1)
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v', interval=0.1)
        time.sleep(0.2)
        pyautogui.hotkey('enter')
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'tab', interval=0.1)
        time.sleep(0.2)
        pyautogui.press('right')
        time.sleep(0.2)

    pyautogui.click(x=424, y=126, clicks=2, interval=0.0, button='left')
    time.sleep(0.2)
    pyautogui.press('1')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.hotkey('alt', 'tab', interval=0.1)
    time.sleep(0.2)
    if i + 1 == 2:
        pyautogui.press('right')
        time.sleep(0.2)
    pyautogui.press('right')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'up', interval=0.1)
    time.sleep(0.2)
    pyautogui.hotkey('alt', 'tab', interval=0.1)
    time.sleep(0.2)


pyautogui.hotkey('alt', 'tab', interval=0.1)
pyautogui.press('left')
time.sleep(0.1)
pyautogui.press('left')
time.sleep(0.1)
pyautogui.press('left')
time.sleep(0.1)
pyautogui.press('left')
time.sleep(0.1)
pyautogui.typewrite('=ARREDONDAR.PARA.BAIXO((HOJE()-B1)/365;0)')
time.sleep(0.1)
pyautogui.press('enter')
time.sleep(0.1)
pyautogui.press('up')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'c', interval=0.1)
time.sleep(0.1)
pyautogui.press('enter')
for cont in range(92):
    pyautogui.hotkey('ctrl', 'v', interval=0.1)
    time.sleep(0.1)
    pyautogui.press('enter')

