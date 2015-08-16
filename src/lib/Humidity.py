### Module for collecting and displaying humidity values
import Adafruit_DHT
from time import sleep
from AdafruitLEDBackpackModules.Adafruit_LEDBackpack.Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)

sensor = Adafruit_DHT.DHT22
pin = 17

def getHumidity():
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	humidity = float('{0:.1f}'.format(humidity))
	return humidity
def displayHumidity():
	humidity = getHumidity()
	segment.writeDigitRaw(0,0x76) # 'H' letter
	segment.writeDigit(1,int(humidity/10))
	segment.writeDigit(3,int(humidity%10),True)
	segment.writeDigit(4,int((humidity*10))%10)
def runHumidity():
	while True:
		displayHumidity()
		sleep(60)
