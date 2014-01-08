]#!/usr/bin/python
import RPi.GPIO as g
import time


g.setmode(g.BCM)
g.setup(4, g.OUT)
while 1:
	g.output(4, 1)
	time.sleep (0.5)
	g.output(4, 0)
	time.sleep (0.5)

