#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Michael Olson
# 27 Feb 2019

# This program turns on a yellow LED and a red LED,
# alternating one to the other in a time (timeframe)
# for (NumCycles) oscillations

import RPi.GPIO as GPIO
import time
import random

###  Set up variables  ###
timeframe = 0.2     # Time before switching to other color
#NumCycles = 30      # Number of oscillations
NumCycles = random.randint(1,30)      # Random Number of oscillations

YellowPin = 23      # GPIO pin with the Yellow LED
RedPin = 24         # GPIO pin with the Red LED

###  Set up GPIO pins on Raspberry Pi  ###
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

###  Start up GPIO pins  ###
GPIO.setup(YellowPin,GPIO.OUT)
GPIO.setup(RedPin,GPIO.OUT)

###  Oscillate between Yellow and Red LEDs  ###
for x in range(1, NumCycles):
    GPIO.output(YellowPin,GPIO.HIGH)
    GPIO.output(RedPin,GPIO.LOW)
    time.sleep(timeframe)
    GPIO.output(YellowPin,GPIO.LOW)
    GPIO.output(RedPin,GPIO.HIGH)
    time.sleep(timeframe)
    
###  Turn off both LEDs  ###
GPIO.output(YellowPin,GPIO.LOW)
GPIO.output(RedPin,GPIO.LOW)

