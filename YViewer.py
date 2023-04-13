import webbrowser
import time
import pyautogui

url = 'https://www.youtube.com/watch?v=RgKAFK5djSk'

for i in range(3):
	webbrowser.open_new(url)
	time.sleep(5)
	pyautogui.hotkey('ctrl','w')
