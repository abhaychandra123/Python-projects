'''
This is a whatsapp img downloader, with which you can download enormous num of images along with naming them.
REQUIREMENT:
1. Have an ide for python
2. Intall the pyautogui library through terminal.Type pip install pyautogui
Check https://pyautogui.readthedocs.io/en/latest/install.html if not working


INSTRUCTIONS:
1. Count the num of images
2.Goto start image and download to the desired folder.
3. Go back to the img
4. Now run this code, Enter the name preffix, start point(here 1) and end point( here num of images-1)
5.Quickly switch back to the image and enjoy!
PS Make sure there isn't any other type of media in the images
'''
import pyautogui, time
pyautogui.FAILSAFE= True
pre = input("Enter the preffix: ")
start = int(input("Start from? "))
end = int(input("End point? "))
print()
print("Switch to page!!")
time.sleep(5)
for i in range(start, end + 1):
    # pyautogui.rightClick(751, 339)
    # pyautogui.click(794, 385)
    pyautogui.rightClick(751,339)
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("enter")

    time.sleep(1)
    pyautogui.typewrite(pre + str(i))
    time.sleep(0.75)

    # pyautogui.click(1287, 53)
    pyautogui.press("enter")

    time.sleep(0.75)

    # pyautogui.click(1316, 430)
    pyautogui.press("right")

    time.sleep(1)
