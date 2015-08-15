import Adafruit_DHT
from time import sleep
from AdafruitLEDBackpackModules.Adafruit_LEDBackpack.Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)

sensor = Adafruit_DHT.DHT22
pin = 17

def getTemperature():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	#we keep only one decimal
	temperature = float('{0:.1f}'.format(temperature))
	return temperature
def displayTemperature():
	temperature = getTemperature()
	segment.writeDigit(0,int(temperature/10))
   	segment.writeDigit(1,int(temperature%10),True)
   	segment.writeDigit(3,int((temperature*10))%10)
   	segment.writeDigitRaw(4,0x63) #turn on ABFG
def runTemperature():
	while True:
		displayTemperature()
		sleep(60)
