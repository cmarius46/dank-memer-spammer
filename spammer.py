import pyautogui
import time

lastTime = time.time() - 45

time.sleep(5)

while(True) :
    
    currentTime = time.time()
    if currentTime >= lastTime + 45:
        lastTime = currentTime
	
        pyautogui.moveTo(470, 990)
        pyautogui.click()
        pyautogui.write('pls beg', 0.05)
        pyautogui.press('enter')

        time.sleep(1)

        pyautogui.click()
        pyautogui.write('pls dig', 0.05)
        pyautogui.press('enter')

        time.sleep(1)

        pyautogui.click()
        pyautogui.write('pls hunt', 0.05)
        pyautogui.press('enter')

        time.sleep(1)

        pyautogui.click()
        pyautogui.write('pls fish', 0.05)
        pyautogui.press('enter')

        time.sleep(1)

        pyautogui.click()
        pyautogui.write('pls deposit max', 0.05)
        pyautogui.press('enter')







