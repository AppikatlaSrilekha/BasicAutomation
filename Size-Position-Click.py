import pyautogui
# returns a size object with
# width and height of the screen
print(pyautogui.size())
# returns a point  object with
# x and y values
print(pyautogui.position())
# moves to (519,1060) in 1 sec
pyautogui.moveTo(1206, 407, duration=1)
# simulates a click at the present

# mouse position
pyautogui.click()
pyautogui.click(button="right")
pyautogui.moveTo(1209, 449, duration=1)
pyautogui.click()