import RPi.GPIO as GPIO
import time
import threading


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
GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=motion_detected_callback,bouncetime=200)

def move_servo_smooth(angle):
    duty = angle / 18 + 2
    servo.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
def servo_control():
    global motion_detected
    last_angle = 0        # Store the last known angle of the servo
    while True:
        if motion_detected:
            print("Motion detected!")
            last_angle = servo_angle  # Store the current angle before stopping
            servo.stop()  # Stop the servo motor
            time.sleep(5)  # Wait for 5 seconds
            motion_detected = False  # Reset the flag
            move_servo_smooth(last_angle)  # Move servo to the last known angle
            servo.start(0)  # Start the servo motor        
            time.sleep(0.5)  # Wait for the servo to start
            #move_servo_smooth(last_angle)  # Move servo to the last known angle
        time.sleep(1)
        
# Create a new thread for servo control
servo_thread = threading.Thread(target=servo_control)
servo_thread.daemon = True
servo_thread.start()

try:
    servo_angle = 0  # Initialize servo angle
    while True:
        for angle in range(0, 181, 5):
            servo_angle = angle
            move_servo_smooth(angle)

        # Move servo back to 0 degrees
        for angle in range(180, -1, -5):
            servo_angle = angle
            move_servo_smooth(angle)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

