import pyautogui,time
pre=input("Enter the preffix: ")
start=int(input("Start from? "))
end=int(input("End point? "))
print()
print("Switch to page!!")
time.sleep(5)
for i in range(start,end+1):
    
    
    pyautogui.rightClick(751,339)
    pyautogui.click(794,385)
    # pyautogui.hotkey("ctrl","s")
    
    time.sleep(1)
    pyautogui.typewrite(pre+str(i))
    time.sleep(0.75)

    pyautogui.click(1287,53)
    # pyautogui.press("enter")

    time.sleep(0.75)
    
    pyautogui.click(1316,430)
    #pyautogui.press("right")

    time.sleep(1)

