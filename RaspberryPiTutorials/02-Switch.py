#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Michael Olson
# 28 Feb 2019

# This program is a test for using a switch. It's goal
# is to switch from a red LED to a yellow and back again
# whenever the switch is pressed.

import RPi.GPIO as GPIO
import time

###  Set up variables  ###
YellowPin = 23      # GPIO pin with the Yellow LED
RedPin = 24         # GPIO pin with the Red LED
SwitchPin = 12      # GPIO pin connected to the switch

###  Set up GPIO pins on Raspberry Pi  ###
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(SwitchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(YellowPin,GPIO.OUT)
GPIO.setup(RedPin,GPIO.OUT)

###  Turn on Yellow LED and wait for Switch  ###
GPIO.output(YellowPin,GPIO.HIGH)
input_state = 1
color = "yellow"

while True:
    previous_state = input_state
    input_state = GPIO.input(SwitchPin)
    if (previous_state == True and input_state == False):
        print(previous_state," ",color," ",input_state)
        current_color = color
        if current_color == "yellow":
            GPIO.output(YellowPin,GPIO.LOW)
            GPIO.output(RedPin,GPIO.HIGH)
            color = "red"
            print("Color is now Red")
            time.sleep(0.2)
        if current_color == "red":
            GPIO.output(YellowPin,GPIO.HIGH)
            GPIO.output(RedPin,GPIO.LOW)
            color = "yellow"
            print("Color is now Yellow")
            time.sleep(0.2)

###  Push button to turn Red; Release button to turn Yellow  ###
#while True:
#    input_state = GPIO.input(SwitchPin)
#    if input_state == False:
#        GPIO.output(YellowPin,GPIO.LOW)
#        GPIO.output(RedPin,GPIO.HIGH)
#    if input_state == True:
#        GPIO.output(YellowPin,GPIO.HIGH)
#        GPIO.output(RedPin,GPIO.LOW)

