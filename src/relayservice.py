import RPi.GPIO as GPIO

class RelayService:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)

    def switch(self, desired_state):       
        GPIO.output(self.pin, desired_state)