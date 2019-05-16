import RPi.GPIO as GPIO

class RelayService:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)

    def get_state(self):
        return GPIO.input(self.pin)

    def switch(self):       
        GPIO.output(self.pin, self.get_state() == False)
