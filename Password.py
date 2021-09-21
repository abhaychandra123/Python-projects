from itertools import chain, product
import pyautogui,time
import keyboard

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
ans=list(bruteforce('1234567890', 5))

for j in ans:
    pyautogui.typewrite(j)
    pyautogui.press("enter")
    if keyboard.is_pressed('z') == True:
        quit()
