import pyautogui
w, h =pyautogui.size()
print(w  +h)
print(pyautogui.position())
x,y = pyautogui.position()
pyautogui.click(x,y)
pyautogui.doubleClick(41,345)

pyautogui.moveTo(10,10)
pyautogui.moveTo(500,1000, duration=1.5)
pyautogui.moveTo(20,20, duration=5.0)
pyautogui.moveRel((200,0), duration=2.0)





