import Adafruit_DHT

class TemperatureService:
    def __init__(self, pin):
        self.pin = pin

    def read_temperatur(self):
        temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.pin)[1]

        return temperature