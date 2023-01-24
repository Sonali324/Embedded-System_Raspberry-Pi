import RPi.GPIO as GPIO
import time
LedPin = 17
def setup():
   # Set the GPIO modes to BCM Numbering
   GPIO.setmode(GPIO.BCM)
   # Set LedPin's mode to output,and initial level to High(3.3v)
   GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)
# Define a main function for main process
   p = GPIO.PWM(ledpin, 100) 
   p.start(0)
def main():
   while True:
       for x in range (0, 100):
           p.ChangeDutyCycle(x)
           time.sleep(0.1)
           for x in range (100, -1):
               p.ChangeDutyCycle(x)
               time.sleep(0.1)
      
# Define a destroy function for clean up everything after the script finished
def destroy():
   # Turn off LED
   GPIO.output(LedPin, GPIO.HIGH)
   # Release resource
   GPIO.cleanup()
# If run this script directly, do:
if __name__ == '__main__':
   setup()
   try:
      main()
   # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
   except KeyboardInterrupt:
      destroy()

 
