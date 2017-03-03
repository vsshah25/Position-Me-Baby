import time
import serial

serialReceiver = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SIXBITS
)
'''
def receive_serial(self,r_data):
		self.time = r_data[time]
		print(self.time)
		print("hi")
		self.radius = (self.time/1000)*340
'''
serialReceiver.open()
while serialReceiver.isOpen():
	serialReceiver.write('0')
