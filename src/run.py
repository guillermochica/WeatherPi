#!/usr/bin/python
import lib.Temperature as Temperature
#import Humidity
#import Clock

STATES={'T': 'Temperature',
		'H': 'Humidity',
		'C': 'Clock'}
current_state = STATES['T']

try:
	Temperature.runTemperature()
except KeyboardInterrupt:
	print '\nGoodbye...'
	Temperature.segment.__init__()
#except ButtonPushed:
#	if current_state=='Temperature':
#		Humidity.runHumidity()
#		current_state = STATES['H']
#	elif current_state == 'Humidity':
#		Clock.runClock()
#		current_state = 'Clock'
#	elif current_state == 'Clock':
#		Temperature.runTemperature()
#		current_state = 'Temperature'
