import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 100) #11 is pin number and 100 is max range of PWM.
p.start(0) #//Starting point of PWM signal you can select any value between 0 to 100.
while True:
    for x in range (0, 101, 2): #//Increasing brightness of LED from 0 to 100
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    for x in range (100, -1, -2): #//fading brightness of LED from 100 to 0
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
p.stop()
GPIO.cleanup()