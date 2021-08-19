import pyautogui,time,keyboard
while True:
    try:
        if keyboard.is_pressed('*'):
            pyautogui.click(1326,650)

    except:
        break