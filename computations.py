from __future__ import division
import xbee
import serial
import numpy as np 
import math 
import socket



d =  0            #distance between master 1 and master 2 
i =  0			 #x-coordinate of master3 	
j =  0			 #y-coordinate of master3 	


def get_dist():

	val1 = p0 - Fm - Pr -10*n*math.log10(freq) - 32.44
	val2 = 10*n
	val3 = val1/val2
	val = math.pow(10,val3)
	return val

def trilateration(radList):
	r1 = radList[0]
	r2 = radList[0]
	r3 = radList[0]

	x = (r1*r1 - r2*r2 + 2*d*d)/(2*d)
	y = -(i*x)/j
	z = math.sqrt(r1*r1 - x*x - y*y)  

	return [x,y,z]
