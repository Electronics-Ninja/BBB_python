from bbio import *
from time import sleep
from sys import exit

stp = 'GPIO2_2'
dir = 'GPIO2_3'  # Push LOW for forward movement, HIGH for reverse
MS1 = 'GPIO2_5'
MS2 = 'GPIO2_4'
EN =  'GPIO1_13'  # Push LOW to allow motor control

pinMode(stp, OUTPUT)
pinMode(dir, OUTPUT)
pinMode(MS1, OUTPUT)
pinMode(MS2, OUTPUT)
pinMode(EN,  OUTPUT)

def resetEDPins():
	digitalWrite(stp, LOW)
	digitalWrite(dir, LOW)
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
		digitalWrite(dir, LOW)	
		moveMotor(360/1.8)

	elif selection == 2:
		digitalWrite(dir, LOW)	
		degree = input("How many degrees? ")
		moveMotor(degree/1.8)

	elif selection == 3:
		digitalWrite(dir, HIGH)
		moveMotor(360/1.8)

	elif selection == 0:
		print
		print "Thank you for using this program."
		print
		exit()

	else:
		print "Invalid Selection, please try again..."


run(setup, loop)
