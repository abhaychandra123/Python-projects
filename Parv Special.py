import pyautogui
import time

time.sleep(0.5)
pyautogui.click(1244, 17, duration=0.5)
pyautogui.alert(text="This is dedicated to my bro, PARV!!!", title="IMPORTANT MESSAGE", button="Click here to continue")
pyautogui.moveTo(921, 735, duration=2.5)
pyautogui.click()
pyautogui.moveTo(386, 180, duration=2.5)
pyautogui.click()
pyautogui.typewrite(
    "<html>\n<head>\n<title>King Khare</title>\n</head>\n<body bgcolor=red>\n<font color=yellow>\n<font color=white>\n<center><h1><b><u>Favorite dishes of Parv Khare(boss)</u></b</h1></center>\n",
    interval=0.009)
pyautogui.typewrite(
    "</font><br><br>\n<ol type=i>\n<li>NON-VEGETARIAN DISHES\n<ol type=1>\n<li>Chicken Leg piece\n<li>Butter chicken\n<li>Briyani\n</ol><br><br>\n<li>VEGETERIAN DISHES\n",
    interval=0.009)
pyautogui.typewrite(
    "<ol type=1>\n<li>Khadhai Panner\n<li>Dal Makhani\n<li>Cheese Corn Pizza\n</ol>\n</ol><br>\n<hr size=9 color=cyan>\n<marquee width=100%><font size=30>THANK YOU</font></marquee>\n",
    interval=0.009)
pyautogui.typewrite("<hr size=9 color=cyan>\n<marquee>Parv paagal hai</marquee>\n</font>\n</body>\n</html>",
                    interval=0.02)
pyautogui.hotkey("ctrl", "s")
pyautogui.typewrite("Parv.html", interval=0.5)
pyautogui.click(521, 442, duration=0.9)
pyautogui.click(385, 481, duration=0.9)
pyautogui.click(503, 486, duration=1)
pyautogui.click(1365, 766, duration=2.5)
pyautogui.doubleClick(336, 127, duration=2.5)
