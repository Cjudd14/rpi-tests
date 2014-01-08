#!/usr/bin/python

import RPi.GPIO as g
import time

g.setmode(g.BCM)
g.setup(4, g.OUT)

p = g.PWM(4, 500)
p.start(1)
while 1:
	for i in range(1,100):
		p.ChangeDutyCycle(i)
		time.sleep(0.01)
	for i in range(100,1,-1):
		p.ChangeDutyCycle(i)
		time.sleep(0.01)
