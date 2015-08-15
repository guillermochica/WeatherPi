#!/usr/bin/python
## A simple script to test all 7 segments
from lib.Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)
segment.writeDigit(0,8,True)
segment.writeDigit(1,8,True)
segment.writeDigit(3,8,True)
segment.writeDigit(4,8,True)
segment.setColon(True)
