import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:  
    while True:  
        #GPIO.output(4, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
	i = GPIO.input(4)
        print(i)                # wait half a second  
	sleep(1)	
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()     
