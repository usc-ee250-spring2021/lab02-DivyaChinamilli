from grove_rgb_lcd import *
import time


distance = int(input("Enter a suitable distance: "))
threshold = 100

if distance < threshold:
    setText_norefresh(str(threshold) + " " + "OBJ PRES\n" + "    "+ str(distance))
    setRGB(255,0,0)
else:
    setText_norefresh(str(threshold) + "           \n " + str(distance))
    setRGB(0,255,0)


