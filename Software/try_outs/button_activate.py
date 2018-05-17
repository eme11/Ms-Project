#will be used to activate the system
import RPi.GPIO as GPIO

global isActive = false;

button = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def btn_callback(pin):
    global isActive =  not isActive
	
	try:
		GPIO.add_event_detect(12,GPIO.RISING,callback=btn_callback,bouncetime=100)