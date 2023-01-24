import RPi.GPIO as GPIO
import time
import math

buttonPin = 27
buzzerPin = 17

GPIO.setmode (GPIO.BCM)
GPIO.setup (buttonPin, GPIO.IN, pull_up_down=GPIO. PUD_UP)
GPIO.setup(buzzerPin, GPIO.OUT)
global p
P= GPIO.PWM (buzzerPin,1)
p.start(0)

while True:
	if GPIO.input(buttonPin) ==GPIO.LOW:
		p.start(50)
		for x in range(0,361):
			sinVal = math.sin(x* (math.pi/180))
			toneVal = 2000+ sinVal 500
			p.ChangeFrequency (toneVal)
			time.sleep(0.001)
			print('On')
	else:
		p.stop()
		print('Off')

