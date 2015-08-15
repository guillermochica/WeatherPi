#!/usr/bin/python
###Simple test for the temperature functionality
from time import sleep
import sys
import Adafruit_DHT
from . lib.Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)
 
#command line arguments
arguments = {'11': Adafruit_DHT.DHT11,
			'22' : Adafruit_DHT.DHT22,
			'2302' : Adafruit_DHT.AM2302}

if len(sys.argv) == 3 and sys.argv[1] in arguments:
	sensor = arguments[sys.argv[1]]
	pin = sys.argv[2]
else:
	print 'To use it write: sudo python temperature.py [11|22|2301] #GPIOpin'
try:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		#print humidity
		print temperature
		humidity = float('{0:.2f}'.format(humidity))
		temperature = float('{0:.1f}'.format(temperature))
		print humidity
		print 'Temperatura: ', temperature
	
		segment.writeDigit(0,int(temperature/10))
		segment.writeDigit(1,int(temperature%10),True)
		segment.writeDigit(3,int((temperature*10))%10)
		segment.writeDigitRaw(4,0x63) #turn on ABFG
		sleep(60) #We measure each minute
except KeyboardInterrupt:
	print '\nGoodbye..'
finally:
	segment.__init__()
