from __future__ import division
import xbee
import serial
import numpy as np 
import math 
import socket 

#==================================================================================
#need to check the port used by the zigbee explorer. 
serial_address = '/dev/ttyUSB0'
baudRate = 9600 
serial_port = serial.Serial(serial_address, baudRate)
xbee = XBee(serial_port)

#==================================================================================
#                         Global Varialbles
no_of_refs = 3 

d =  0            #distance between master 1 and master 2 
i =  0			 #x-coordinate of master3 	
j =  0			 #y-coordinate of master3 	

#================================================================================== 
#                              functions

def path_expo(bit_rate,rssi,device_id):

	Fm = -154 + 10*math.log10(bit_rate)
	rssi = Pr 
	d = ref_dist[device_id]

	val1 = p0 - Fm -Pr -32.44
	val2 = math.log10(d) + 10*math.log10(freq) - 30
	val = val1/val2  
	return device_id, val 

def send_data():
	
#====================================================================================


while True:
	try:
		in_list = xbee.wait_read_frame()

		device_tag = 		#can be a ref or an object which we want to recognise. 
		device_id = 		#for refs, the device id will be the circle number. for the object to be localised. 
		rssi_val = 				
		bit_rate = 		#to calculate the Fade margin. 

	    

		# path_expo = np.zeros((10,4))

		if device_tag == 'ref':
			var = path_expo(bit_rate,rssi_val,device_id)
			send_data(var)

		if device_tag == "obj":
			send_data([device_tag,device_id,rssi_val,bit_rate])



	except KeyboardInterrupt:
		break

serial_port.close()


