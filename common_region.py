import math
import pygame
from pygame.locals import *
import sys,os
import serial
from random import randint

pygame.init()
window_width = 500
window_height = 500
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
circle_color=[(255,0,0),(0,0,255),(255,0,255),(128,180,200)]          # some random colors for four circles
global count
count=0

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

	def assign(self):
		self.radius = 350
		self.x_center=25+int(bool(self.trans_id%2 == 0))*450
		self.y_center=25+int(bool(self.trans_id >= 3))*450
		pygame.draw.circle(display_surface, circle_color[self.trans_id-1],(self.x_center,self.y_center),self.radius,1)
		pygame.display.update()

def getCommonRegion(trans_id,display_surface):
	intersection_points=[]
	for i in range(0,4):
		if trans_id[i].x_center!=0 and trans_id[i].y_center!=0:
			j=i+1
			while j<4:
				if trans_id[j].x_center!=0 and trans_id[j].y_center!=0:
					x1=trans_id[i].x_center
					y1=trans_id[i].y_center
					x2=trans_id[j].x_center
					y2=trans_id[j].y_center
					r1=trans_id[i].radius
					r2=trans_id[j].radius

					center_d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
					if center_d<r1+r2:
						k=((r1**2-r2**2)-(y1**2-y2**2)-(x1**2-x2**2))/2.0
						if (x2-x1)!=0:
							a=(float(y2-y1)**2)/((x2-x1)**2)+1
							b=float(y1)+float(k*(y2-y1)/((x2-x1)**2))-float((y2-y1)/(x2-x1))*x1
							c=float(k/(x2-x1))**2 +x1**2+y1**2-r1**2-((2*x1*k)/(x2-x1))
							yr1=(b+math.sqrt(b*b-a*c))/a
							yr2=(b-math.sqrt(b*b-a*c))/a
							xr1=(k-yr1*(y2-y1))/(x2-x1)
							xr2=(k-yr2*(y2-y1))/(x2-x1)
						elif (x2-x1)==0:
							yr1=k/(y2-y1)
							yr2=k/(y2-y1)
							xr1=x1+math.sqrt(r1**2-(yr1-y1)**2)
							xr2=x1-math.sqrt(r1**2-(yr2-y2)**2)
						if xr1==xr2 and yr1==yr2:
							if xr1 in (0,500) and yr1 in (0,500):
								intersection_points.append((xr1,yr1))
						else:
							if xr1>=0 and xr1<=500 and yr1>=0 and yr1<=500:
								intersection_points.append((xr1,yr1))
							if xr2>=0 and xr2<=500 and yr2>=0 and yr2<=500:
								intersection_points.append((xr2,yr2))
				j+=1
	global avg_x,avg_y
	avg_x=0
	avg_y=0
	c=0
	if intersection_points!=[]:
		for point in intersection_points:
			avg_x+=point[0]
			avg_y+=point[1]
			c+=1
		avg_x/=c
		avg_y/=c
	pygame.draw.circle(display_surface,(0,0,0),(int(avg_x),int(avg_y)),4,4)
	pygame.display.update()

trans_1  = Transmitter(1)
trans_2  = Transmitter(2)
trans_3  = Transmitter(3)
trans_4  = Transmitter(4)

trans_1.draw()
trans_2.draw()
trans_3.draw()
trans_4.draw()
trans_id=[trans_1,trans_2,trans_3,trans_4]

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for i in trans_id:
		i.assign()
	getCommonRegion(trans_id,display_surface)
	pygame.display.update()



