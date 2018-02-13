import sys
import config as cfg
import Adafruit_DHT

def getValues():

    sensor = cfg.hardwareVersion
    pin = cfg.gpioPort
      
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
	return ('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    else:
	print('Failed to get reading. Try again!')
	sys.exit(1)
