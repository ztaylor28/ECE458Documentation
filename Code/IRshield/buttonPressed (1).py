#create a variable(X) that can be toggled between a 0 and 1
#if button1 is pressed, changes variable(X) from a 0 to a 1, start to scan for commericals,default command is KEY_MUTE
#if button2 is pressed, changes variable(X) from a 1 to a 0, command is now KEY_VOLUMEDOWN

import os
import time
import RPi.GPIO as GPIO
buttonPin=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)
buttonPin1=22
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin1,GPIO.IN)
latestState = None
latestState1 = None
powerButton = 0
volumeDownTen = 0

while True:
    startAlgo = GPIO.input(buttonPin)
    if startAlgo != latestState:
        latestState = startAlgo
        if latestState:
            if powerButton == 1:
                # !ADD POINTER TO ALGORITHM STOP
                print("++Algorithm is OFF")
                powerButton = 0
            elif powerButton == 0:
                # !ADD POINTER TO ALGORITHM START
                print("++Algorithm is ON, Mute is selected")
                os.system('irsend SEND_ONCE ESTINGHOUSE KEY_MUTE')
                powerButton = 1
            else:
                print("?ERROR: Error in powerButton Loop (Line 23)")
            print("ButtonTop Pressed")
        else:
            print("ButtonTop Depressed")
        time.sleep(.15)

    volumeControl1 = GPIO.input(buttonPin1)
    if volumeControl1 != latestState1:
        latestState1 = volumeControl1
        if latestState1:
            if volumeDownTen == 1:
                # !ADD POINTER TO VOLUME ALGORITHM STOP
                print("++Reduced Volume OFF")
                volumeDownTen = 0
            elif volumeDownTen == 0:
                # !ADD POINTER TO VOLUME ALGORITHM START
                print("++Reduced Volume ON")
                os.system('irsend --count=8 SEND_ONCE ESTINGHOUSE KEY_VOLUMEDOWN')
                volumeDownTen = 1
            else:
                print("?ERROR: Error in volumeDownTen Loop (Line 43)")
            print("ButtonBottom Pressed")
        else:
            print("ButtonBottom Depressed")
        time.sleep(.15)

    # !Add to the algorithm
    #     #os.system('irsend SEND_ONCE ESTINGHOUSE KEY_MUTE')
    #     #os.system('irsend --count=8 SEND_ONCE ESTINGHOUSE KEY_VOLUMEDOWN')