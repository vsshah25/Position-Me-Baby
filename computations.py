from __future__ import division
import xbee
import serial
import numpy as np 
import math 
import socket
import pygame

s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.connect((host, port))


no_of_refs = 3
expoList = []

 
d =  0                   #distance between master 1 and master 2 
i =  0			 #x-coordinate of master3 	
j =  0			 #y-coordinate of master3 	


#======================================================================== 
#                              functions

def path_expo(inlist):
	device_tag = inlist[0]
	if device_tag == "ref":
	
		device_id = inlist[1]
		rssi_val = inlist[2]
		bit_rate = inlist[3]

	
	
	        Fm = -154 + 10*math.log10(bit_rate)
        	rssi = Pr
	        d = ref_dist[device_id]

        	val1 = p0 - Fm -Pr -32.44
        	val2 = math.log10(d) + 10*math.log10(freq) - 30
	        val = val1/val2
        	expolist.append([device_id,val])
	else:
		return	 

def get_dist():

        device_tag = inlist[0]
        if device_tag == "obj":

                device_id = inlist[1]
                rssi_val = inlist[2]
                bit_rate = inlist[3]

        		

		val1 = p0 - Fm - Pr -10*n*math.log10(freq) - 32.44
		val2 = 10*n
		val3 = val1/val2
		val = math.pow(10,val3)
		return val
	else:
		return 

def getposition(radList):
	r1 = radList[0]
	r2 = radList[0]
	r3 = radList[0]

	x = (r1*r1 - r2*r2 + 2*d*d)/(2*d)
	y = -(i*x)/j
	z = math.sqrt(r1*r1 - x*x - y*y)  

	return [x,y,z]

def avgexpo(elist):
	if len(elist) == 0:
		print "No readings :/ "	

	if len(elist) < 5:
		total = 0
		for elem in elist:
			total = total + elem[1]
		avg = total/len(elist)
		
	else: 
		total = 0
		for i in range(len(elist)-6,len(elist)-1):
			total = total + elist[1]
		avg = total/5				
	return avg	   

def nearest_ref(coordinates,inStep):
	x = coordinates[0]
	y = coordinates[1]
	z = coordinates[2]
	
	diff_ref1 = math.sqrt( (x -x1)*(x-x1) + (y-y1)*(y-y1) )
	diff_ref2 = math.sqrt( (x -x2)*(x-x2) + (y-y2)*(y-y2) )
	diff_ref3 = math.sqrt( (x -x3)*(x-x3) + (y-y3)*(y-y3) )
	diff_list = [diff_ref1, diff_ref2, diff_ref3]
	
	nnref = diff_list.index(min(diff_list))
	
	return nnref	
	


	
	
	
#========================================================================


while True:
	data_list = s.recv(1024)
	expo = avgexpo(path_expo(data_list))
	rssi = data_list[2]
	dist = get_dist(data_list)
		
	print dist	
		

	 
