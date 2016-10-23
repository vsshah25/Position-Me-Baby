import pygame
from pygame.locals import *
import sys,os
import serial

pygame.init()
window_width = 500
window_height = 500
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
circle_color=[(255,0,0),(0,0,255),(255,0,255),(128,180,200)]          # some random colors for four circles
count=0


display_surface = pygame.display.set_mode((window_width,window_height),0,32)
display_surface.fill(white)
pygame.display.set_caption("map_69")
myfont = pygame.font.SysFont("monospace", 20)
		
class Transmitter:
	def __init__(self, trans_id):
		self.trans_id = trans_id
	
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
			
	def receive_serial(self,r_data):
		self.time = r_data[time]
		print(self.time)
		self.radius = (self.time/1000)*340
		self.x_center=25+int(bool(trans_id%2 ==0))*450
        self.y_center=25+int(bool(trans_id>3))*450
		pygame.draw.circle(display_surface, circle_color[trans_id],(self.x_center, self.y_center), self.radius, 1)
                                             
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
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

trans_id=[trans_1,trans_2,trans_3,trans_4]

#main loop 
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	# An interrupt should be there which at a constant duration  checks whether 
	# it has received data from the receiver object
	while serialReceiver.inWaiting() > 0 and serialReceiver.isOpen():
		r_data=serialReceiver.read()                    # r_data will be an array containing time and trans_id
		global count
		count=(count)%4+1
		trans_id[count].receive_serial(r_data)
   		pygame.display.update()


	
   	pygame.display.update()
