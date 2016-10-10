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

display_surface = pygame.display.set_mode((window_width,window_height),0,32)
display_surface.fill(white)
pygame.display.set_caption("map_69")


class transmitter:
	def __init__(self, trans_id):
		self.trans_id = trans_id
	
	def draw(self):
		self.x = 450 - 450*int(bool(self.trans_id <3))
		self.y = (450 - 450*int(bool(self.trans_id%2 !=0)))
		pygame.draw.rect(display_surface,(0,255,0),(self.x ,self.y,50,50))
		'''
		self.a = int(475*(int(bool(self.trans_id%2 !=0))))
		self.b = int(25*(int(bool(self.trans_id%2 =0))))
		self.c = int(475*(int(bool(self.trans_id >=3))))
		self.d = int(25*(int(bool(self.trans_id <3))))
		label = myfont.render(str(self.trans_id), 1, (0,0,0))
		display_surface.blit(label, (a+b, c+d, 25))
		'''

	self.serial = serial.Serial('/dev/ttyACM0')
    

	
	def send_serial(self):
		while(1):
			c = self.serial.write(self.trans_id)
			if self.serial.read() == 0 
				break

def recieve_serial(self):
	r_data  = self.serial.read()
	self.time = r_data                                            #will be calculted by the arduino                                                
				




myfont = pygame.font.SysFont("monospace", 20)

trans_1  = transmitter(1)
trans_2  = transmitter(2)
trans_3  = transmitter(3)
trans_4  = transmitter(4)

trans_1.draw()
trans_2.draw()
trans_3.draw()
trans_4.draw()





while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
