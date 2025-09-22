import RPi.GPIO as GPIO
import time

# Suggested GPIO pins for LEDs and buttons
led_pins = [2, 3, 4, 17, 27, 22, 10, 9]  # 8 LEDs
button1_pin = 20  # Button 1
button2_pin = 21  # Button 2

GPIO.setmode(GPIO.BCM)

# Set up LED pins as outputs
for pin in led_pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

# Set up button pins as inputs with pull-up resistors
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0

try:
	while True:
		button1_state = GPIO.input(button1_pin)
		button2_state = GPIO.input(button2_pin)

		if button1_state == GPIO.LOW:
			time.sleep(0.5)  # Debounce delay
			print(f"Count: {count}")
			if count < len(led_pins):
				GPIO.output(led_pins[count], GPIO.HIGH)
				count += 1

		if count >= len(led_pins):
			for pin in led_pins:
				GPIO.output(pin, GPIO.LOW)
			count = 0

		if button2_state == GPIO.LOW:
			for pin in led_pins:
				GPIO.output(pin, GPIO.LOW)
			count = 0

		time.sleep(0.05)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
