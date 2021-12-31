import pyautogui
import pyperclip
import time
# pos = pyautogui.locateOnScreen("Debg_extnsn.png")
# x, y = pos[:2]
# x = x+300
# # pyautogui.moveTo(x, y)

# pyautogui.click(x, y)
time.sleep(5)
pyautogui.hotkey("ctrlleft", "a")

pyautogui.hotkey("ctrlleft", "c")
data = pyperclip.paste()

pyautogui.press("right")

data = [x for x in data if x == '\n']
for x in range(len(data)+1):
    pyautogui.hotkey("ctrlleft", "c")
    Single_line_data = pyperclip.paste()

    for y in range(len(Single_line_data)-1):
        pyautogui.hotkey("ctrlleft", "c")
        if len(pyperclip.paste()) == 2:
            pyautogui.press("backspace")
            pyautogui.scroll(50)
            # pyautogui.typewrite("#nextline")
            break
        pyautogui.press("backspace")
