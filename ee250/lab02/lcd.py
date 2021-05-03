from grove_rgb_lcd import *
import time


distance = int(input("Enter a suitable distance: "))
threshold = 100

if distance < threshold:
    setText_norefresh(threshold + " " + "OBJ PRES\n" + "    "+ distance)
    setRGB(255,0,0)
else:
    setText_norefresh(threshold + "           \n " +  distance)
    setRGB(0,255,0)


