'''
This is a whatsapp and Google drive img downloader, with which you can download enormous num of images along with naming them.
INSTRUCTIONS:
1. Count the num of images
2.Goto start image and download to the desired folder.
3. Go back to the img
4. Now run this code, Enter the name preffix, start point(here 1) and end point( here num of images-1)
5.Quickly switch back to the image and enjoy!
'''
import pyautogui, time
pyautogui.FAILSAFE= True
pre = input("Enter the preffix: ")
start = int(input("Start from? "))
end = int(input("End point? "))
mode = input("Enter the mode(wp or dr): ")
delay= float(input("Delay? "))


print()
print("Switch to page!!")
time.sleep(5)
for i in range(start, end + 1):

    if mode=="wp":
        pyautogui.rightClick(751,339)
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("enter")
    elif mode=="dr":
        pyautogui.hotkey('ctrl','s')
    time.sleep(delay)
    pyautogui.typewrite(pre + str(i))
    time.sleep(0.75)

    # pyautogui.click(1287, 53)
    pyautogui.press("enter")

    time.sleep(1)

    # pyautogui.click(1316, 430)
    pyautogui.press("right")

    time.sleep(1)
