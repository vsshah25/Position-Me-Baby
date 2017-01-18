import time

val = ''
count=0
serialReceiver = serial.Serial(
    port='/dev/ttyACM1',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SIXBITS
)
'''
def receive_serial(self,r_data):
		self.time = r_data[time]
		print(self.time)
		print("hi")
		self.radius = (self.time/1000)*340
'''
while serialReceiver.isOpen():
	r_data=serialReceiver.read()
	r_data_string = str(r_data)
	if r_data_string == 'c':
		starting_time=time.time()
		serialReceiver.write('c')
	if r_data_string == '!':
		print(val)
		if count%2==0:
			transmitted_time=time.time()-starting_time            # transmitted_time will be in seconds
		else:
			received_time=time.time()-starting_time               # received_time will be in milliseconds
			delta_t=(received_time*1000)-transmitted_time
			distance=(delta_t)*340
			print(str(distance))
		val = ''
		count+=1

	else:
		val = val + r_data_string