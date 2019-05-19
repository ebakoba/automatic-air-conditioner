

# Setup

## Hardware
![Project sketch](images/sketch.png)

## Software

* Python 3

* Pyhton modules ```Adafruit_DHT``` and ```RPi.GPIO```


# How to run

* Create a config (i.e. with `cp ./config.example.json ./config.json`)

* `python3 main.py`

# Usage

The threshold temperature or the timeout period between the switches    can be changed in the ```config.json``` file.

Program will adapt settings in next 10 seconds and does not require a restart

