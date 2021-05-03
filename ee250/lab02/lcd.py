from grove_rgb_lcd import *
import time

setRGB(0,255,0)
buf=list("Grove -Update without erase")
setText("".join(buf))
time.sleep(1)

for i in range(len(buf)):
	buf[i]="."
	setText_norefresh("".join(buf))
	time.sleep(.1)
