import RPi.GPIO as GPIO
import os
import time
import datetime
import emai_attach

#we import one of the functions from email_send.py
from emai_send import send_mail_simple

#setting up the GPIO
#from pin 12 we read the data from the sensor
#on pin 14 it is the ground and on pin 2 is the voltage
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)       


def getMessage():
    body ="Alert, motion detected in your home.\nYou can see the live stream at:\n http://www.youtube.com/live_dashboard \n"
    return body

#analyze the data from the sensor
pirState = 0
while True:
    global pirState
    input=GPIO.input(12)
    if input==1 and pirState == 0:
                pirState = 1
                body = getMessage()
                send_mail_simple("raspberrypi.camera.project@gmail.com", "PassWord12",
                      "emese.mathe.07@gmail.com",
                      "Motion detected",body)
    pirState=input
