import RPi.GPIO as GPIO
import time

# Set GPIO pins for servo motor and PIR sensor
servo_pin = 40
pir_pin = 12

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(pir_pin, GPIO.IN)

# Initialize servo motor
servo = GPIO.PWM(servo_pin, 50)  # PWM frequency of 50 Hz
servo.start(0)  # Initial position of the servo

# Flag to control servo behavior
motion_detected = False
    
# Interrupt function
def motion_detected_callback(channel):
    global motion_detected
    motion_detected = True

# Set up interrupt for PIR sensor
GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=motion_detected_callback, )

try:
    while True:
        if motion_detected:
            print("Motion detected!")
            servo.stop()  # Stop the servo motor
            motion_detected = False  # Reset the flag

        else:
            for angle in range(0, 181, 5):
                duty = angle / 18 + 2
                servo.ChangeDutyCycle(duty)
                time.sleep(0.05)

            # Move servo back to 0 degrees
            for angle in range(180, -1, -5):
                duty = angle / 18 + 2
                servo.ChangeDutyCycle(duty)
                time.sleep(0.05)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
