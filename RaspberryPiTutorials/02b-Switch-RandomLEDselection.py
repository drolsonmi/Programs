#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Michael Olson
# 1 Mar 2019

# This program will have an array of LED lights. When the
# switch is pressed, it will create a random number, then
# turn on sequential lights until the random number is
# reached and stop on that random number.

import RPi.GPIO as GPIO
import time
import random

### Set up variables ###
Pins = [21,20,16,12,25,24,23,18]
SwitchPin = 4

###  Set up GPIO pins on Raspberry Pi  ###
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(SwitchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for x in range (0,len(Pins)):
    GPIO.setup(Pins[x],GPIO.OUT)
    print(Pins[x]," set up.")

GPIO.setup(21,GPIO.OUT)
input_state = 1
current_pin = 0
GPIO.output(Pins[current_pin],GPIO.HIGH)

while True:
    previous_state = input_state
    input_state = GPIO.input(SwitchPin)
    if (previous_state == True and input_state == False):
        NumOfLoops = random.randint(5,45)
        for x in range (1,NumOfLoops):
            GPIO.output(Pins[current_pin],GPIO.LOW)
            if current_pin == len(Pins)-1:
                print("Resetting counter")
                current_pin = 0
            else:
                current_pin = current_pin + 1
            print(current_pin," of ",len(Pins)-1)
            GPIO.output(Pins[current_pin],GPIO.HIGH)
            time.sleep(0.15)
