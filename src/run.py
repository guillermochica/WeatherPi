#!/usr/bin/python
import sys
import lib.Temperature as Temperature
import lib.Humidity as Humidity
import lib.Clock as Clock

STATES={'T': 'Temperature',
		'H': 'Humidity',
		'C': 'Clock'}
if len(sys.argv) == 2 and sys.argv[1] in STATES:
	current_state = STATES[sys.argv[1]]
else:
	print 'To use it write: sudo ./run [T|H|C]'

try:
	if current_state == 'Temperature':
		Temperature.runTemperature()
	elif current_state == 'Humidity':
		Humidity.runHumidity()
	elif current_state == 'Clock':
		Clock.runClock()
except KeyboardInterrupt:
	print '\nGoodbye...'
	if current_state == 'Temperature':
		Temperature.segment.__init__()
	elif current_state == 'Humidity':
		Humidity.segment.__init__()
	elif current_state == 'Clock':
		Clock.segment.__init__()
