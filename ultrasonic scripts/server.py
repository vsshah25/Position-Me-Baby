import serial
serialReceiver = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    stopbits=serial.STOPBITS_ONE,
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
	print r_data
	# print r_data
	# header = ""
	# if r_data == "$":
	# 	for i in range(5):		
	# 		header = header + serialReceiver.read()

	# 	print "header",header	

	# if 	

'''
	header = ""
	
	for i in range(5):
		header = header + serialReceiver.read()
		continue
'''
	


		


