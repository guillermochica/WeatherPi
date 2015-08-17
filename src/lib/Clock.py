import time
from AdafruitLEDBackpackModules.Adafruit_LEDBackpack.Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)

def getTime():
	hour = time.localtime().tm_hour
	minute = time.localtime().tm_min
	return [hour,minute]
def displayTime():
	clock = getTime()
	hour = clock[0]
	minute = clock[1]
	segment.writeDigit(0,int(hour/10))
	segment.writeDigit(1,int(hour%10))
	segment.writeDigit(3,int(minute/10))
	segment.writeDigit(4,int(minute%10))
	segment.setColon(False)
	time.sleep(0.5)
	segment.setColon(True)
	time.sleep(0.5)
def runClock():
	while True:
		displayTime()
	
