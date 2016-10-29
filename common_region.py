import math
def getCommonRegion(trans_id):
	for i in range(1,4) and trans_id[i].x_center!=0 and trans_id[i].y_center!=0:
		j=i+1
		while j<=4 and trans_id[j].x_center!=0 and trans_id[j].y_center!=0:
			x1=trans_id[i].x_center
			y1=trans_id[i].y_center
			x2=trans_id[i].x_center
			y2=trans_id[i].y_center
			r1=trans_id[i].radius
			r2=trans_id[i].radius

			center_d=sqrt((x2-x1)**2 + (y2-y1)**2)
			if center_d<r1+r2:
				k=((r1**2-r2**2)-(y1**2-y2**2)-(x1**2-x2**2))/2

				a=((y2-y1)**2)/((x2-x1)**2)+1
				b=y1+(k*(y2-y1)/((x2-x1)**2))-((y2-y1)/(x2-x1))*x1
				c=(k/(x2-x1))**2 +x1**2+y1**2-r1**2

				yr1=(b+sqrt(b*b-a*c))/a
				yr2=(b-sqrt(b*b-a*c))/a

				xr1=(k-yr1*(y2-y1))/(x2-x1)
				xr2=(k-yr2*(y2-y1))/(x2-x1)

			elif center_d==r1+r2:
				pygame.draw.line(display_surf,(0,0,0),(x1+x2)/2,(y1+y2)/2)

			else:
				print 'Yp'
				# No common Region
				pass