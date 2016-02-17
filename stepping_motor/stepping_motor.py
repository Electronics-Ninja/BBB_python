###########################################################
# Parts required:
#  1. Sparkfun 200 steps/rev motor (ROB-10847)
#  2. Beaglebone Black
#  3. Sparkfun Easy Driver (ROB-12779)
#
# This uses the PyBBIO library and *not* the Adafruit_BBIO
###########################################################
__author__   = 'Paul Kincaid'
__test__     = 'blah'
__email__    = 'paul@electronics-ninja.io'
__github__   = 'https://github.com/Electronics-Ninja/BBB_python.git'
__version __ = 1.0
__date__     = 'October 21, 2015'

from bbio import *
from time import sleep
from sys import exit

stp    = 'GPIO2_2'   # BBB Pin P8_7
direct = 'GPIO2_3'   # Push LOW for forward movement, HIGH for reverse - BBB Pin P8_8
MS1    = 'GPIO2_5'   # BBB Pin P8_9
MS2    = 'GPIO2_4'   # BBB Pin P8_10
EN     = 'GPIO1_13'  # Push LOW to allow motor control - BBB Pin P8_11

pinMode(stp, OUTPUT)
pinMode(direct, OUTPUT)
pinMode(MS1, OUTPUT)
pinMode(MS2, OUTPUT)
pinMode(EN,  OUTPUT)

def resetEDPins():
	digitalWrite(stp, LOW)
	digitalWrite(direct, LOW)
	digitalWrite(MS1, LOW)
	digitalWrite(MS2, LOW)
	digitalWrite(EN, HIGH)

def moveMotor(steps):
	x = 0
	while (x <= steps):
		digitalWrite(stp, HIGH)
		sleep(0.001)
		digitalWrite(stp, LOW)
		sleep(0.001)
		x += 1

def setup():
	print
	print "[*] BBB Stepping Motor Control"
	resetEDPins()

def loop():
	print
	print "[+++] Menu [+++]"
	print "  [1] Move forward 1 full revolution"
	print "  [2] Move forward and specify degrees"
	print "  [3] Move in reverse 1 full revolution"
	print "  [0] Exit"
	print
	selection = input("Please make a selection: ")
	digitalWrite(EN, LOW)
	if selection == 1:
		digitalWrite(direct, LOW)
		moveMotor(360/1.8)

	elif selection == 2:
		digitalWrite(direct, LOW)
		degree = input("How many degrees? ")
		moveMotor(degree/1.8)

	elif selection == 3:
		digitalWrite(direct, HIGH)
		moveMotor(360/1.8)

	elif selection == 0:
		print
		print "Thank you for using this program."
		print
		exit()

	else:
		print "Invalid Selection, please try again..."


run(setup, loop)
