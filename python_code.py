import pygame
from pygame.locals import *
import sys,os
import serial
import common_region
import time

pygame.init()
window_width = 500
window_height = 500
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
circle_color=[(255,0,0),(0,0,255),(255,0,255),(128,180,200)]          # some random colors for four circles
global count1
global count2

count1=0
count2=0
display_surface = pygame.display.set_mode((window_width,window_height),0,32)
display_surface.fill(white)
pygame.display.set_caption("map_69")
myfont = pygame.font.SysFont("monospace", 20)
		
class Transmitter:
	def __init__(self, trans_id):
		self.trans_id = trans_id
		self.x_center=0
		self.y_center=0
		self.radius=0
	
	def draw(self):
		self.x = 450 - 450*int(bool(self.trans_id %2!=0))
		self.y = 450 - 450*int(bool (self.trans_id<3))
		pygame.draw.rect(display_surface,(0,255,0),(self.x ,self.y,50,50))
		
		a = int(bool(self.trans_id %2 != 0))
		b = int(bool(self.trans_id %2 == 0))
		c = int(bool(self.trans_id >= 3))
		d = int(bool(self.trans_id < 3))
		label = myfont.render(str(self.trans_id), 1, (0,0,0))
		display_surface.blit(label, (25*a + 475*b, 475*c + 25*d))
    	
	def send_serial(self):
			for i in range(0,5):
				self.serial.write(self.trans_id)
			
	def receive_and_draw(self,r_data):
		self.time = r_data[time]
		print(self.time)
		self.radius = (self.time/1000)*340

		exp_1 =  int(bool(self.trans_id%2 ==0)) 
		exp_2 = int(bool(self.trans_id>3))
		self.x_center=25+int(bool(self.trans_id%2 ==0))*450
		self.y_center=25+int(bool(self.trans_id > 3))*450
		pygame.draw.circle(display_surface, circle_color[self.trans_id],self.x_center,self.y_center,self.radius,1)
                                             
trans_1  = Transmitter(1)
trans_2  = Transmitter(2)
trans_3  = Transmitter(3)
trans_4  = Transmitter(4)

trans_1.draw()
trans_2.draw()
trans_3.draw()
trans_4.draw()

# configuring the serial receiver that recives from the target object
serialReceiver = serial.Serial(
    port='/dev/ttyACM1',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SIXBITS
)

trans_id=[trans_1,trans_2,trans_3,trans_4]

# main loop 
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	while serialReceiver.inWaiting() > 0:                 #and serialReceiver.isOpen():
		r_data=serialReceiver.read()
		r_data_string = str(r_data)
		if r_data_string == 'c':
			starting_time=time.time()
			serialReceiver.write('c')
		if r_data_string == '!':
			print(val)
			if count1%2==0:
				transmitted_time=time.time()-starting_time            # transmitted_time will be in seconds
			else:
				received_time=time.time()-starting_time               # received_time will be in milliseconds
				delta_t=(received_time*1000)-transmitted_time
				distance=(delta_t)*340
				print(str(distance))
			val = ''
			count1+=1

		else:
			val = val + r_data_string

		count2=((count2)%4)+1
		trans_id[count2].receive_serial(r_data)
   		pygame.display.update()
   		getCommonRegion(trans_id,display_surface)
   	pygame.display.update()
