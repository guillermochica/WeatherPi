#!/usr/bin/python
import sys
import lib.Temperature as Temperature
import lib.Humidity as Humidity
import lib.Clock as Clock
import RPi.GPIO as io

switch_pin = 22
io.setmode(io.BCM)
io.setup(switch_pin, io.IN, pull_up_down=io.PUD_UP)

STATES={'T': 1,
	'H': 2,
	'C': 3}
if len(sys.argv) == 2 and sys.argv[1] in STATES:
	current_state = STATES[sys.argv[1]]
else:
	print 'To use it write: sudo ./run [T|H|C]'

try:
	while True:
		key_pressed = not io.input(switch_pin)
		if key_pressed:
			current_state = current_state +1
			if current_state > STATES['C']:
				current_state = STATES['T']
		if current_state == STATES['T']:
			Temperature.displayTemperature()
		elif current_state == STATES['H']:
			Humidity.displayHumidity()
		elif current_state == STATES['C']:
			Clock.displayTime()
except KeyboardInterrupt:
	print '\nGoodbye...'
	if current_state == STATES['T']:
		Temperature.segment.__init__()
	elif current_state == STATES['H']:
		Humidity.segment.__init__()
	elif current_state == STATES['C']:
		Clock.segment.__init__()
