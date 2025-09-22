import RPi.GPIO as GPIO
import time

# Set the GPIO pin number (BCM numbering)
led_pin = 17  # Change this to the pin you are using

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # LED ON
        time.sleep(1)                    # Wait 1 second
        GPIO.output(led_pin, GPIO.LOW)   # LED OFF
        time.sleep(1)                    # Wait 1 second
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
