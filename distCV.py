import argparse
import cv2
import imutils
import time
import numpy as np 
#-------------------------------------------------------------------------------------------------------
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=800, help="minimum area size")
args = vars(ap.parse_args())
#-------------------------------------------------------------------------------------------------------
flag = 0 
x = 0
y = 0
w = 0 
h = 0 
firstFrame = None
threshold = 100        #calibrate
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	#([86, 31, 4], [220, 88, 50]),
	#([25, 146, 190], [62, 174, 250]),
	#([103, 86, 65], [145, 133, 128])
]
# ([17, 15, 100], [50, 56, 200]) implies that R >= 100, B >= 15, and G >= 17 along with R <= 200, B <= 56, and G <= 50 will be considered red.

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
if args.get("video", None) is None:
    cap = cv2.VideoCapture(-1)
    time.sleep(0.25)
 
# otherwise, we are reading from a video file
else:
    cap = cv2.VideoCapture(args["video"])

if(cap.isOpened()==False):
        print 'error'
#--------------------------------------------------------------------------------------------------------

class ShapeDetector:
	def __init__(self):
		pass
 
	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		# if the shape is a triangle, it will have 3 vertices
		# if len(approx) == 3:
		# 	shape = "triangle"
 
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		if len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
 
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
 
		# # if the shape is a pentagon, it will have 5 vertices
		# elif len(approx) == 5:
		# 	shape = "pentagon"
 
		# # otherwise, we assume the shape is a circle
		# else:
		# 	shape = "circle"
 
		# return the name of the shape
		return shape		
#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------


if(cap.isOpened()==False):
        print 'error'

#----------------------------------------------------------------------------------------------------------

while (cap.isOpened()):

	(grabbed, frame) = cap.read()
	cv2.imshow("first_frame",frame)

	# # convert the resized image to grayscale, blur it slightly,
	# # and threshold it


	# loop over the boundaries
	# for (lower, upper) in boundaries:
	# 	# create NumPy arrays from the boundaries
	lower = np.array([0,0, 100], dtype = "uint8")
	upper = np.array([80, 80, 255], dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	frame_blur = cv2.GaussianBlur(frame, (21, 21), 0)

	mask = cv2.inRange(frame_blur, lower, upper)
	mod_mask = cv2.dilate(mask, None, iterations=5)

	# cv2.imshow("mod_mask",mod_mask)
	# cv2.imshow("mask",mask)

	(_,cnts, khai) = cv2.findContours(mod_mask, cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	print len(cnts)
	for c in cnts:

		if cv2.contourArea(c) < 800:                               #calibrate  
			continue
		print cv2.contourArea(c)
		(x, y, w, h) = cv2.boundingRect(c)        
		# rects.append((x, y, w, h))
		
		#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		#cv2.drawContours(frame, c, -1, (0,255,0), 3)		


	output = cv2.bitwise_and(frame, frame, mask = mod_mask)
		# show the images
	cv2.imshow("images", np.hstack([frame, output]))	
	print x,y,w,h
	if x > 0 and y > 0 and w > 0 and h  > 0 :  
		roi = frame[y-10:y+h+10, x-10:x+w+10]
		cv2.imshow("crop",roi )
		flag = 1 

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break	



#----------------------------------------------------------------------------------------------------------
									#Detect shapes 

	#resized = imutils.resize(frame, width=300)
	ratio = 1#frame.shape[0] / float(resized.shape[0])
	 
	# convert the resized image to grayscale, blur it slightly,
	# and threshold it
	gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 170, 255, cv2.THRESH_BINARY)[1]
	cv2.imshow("thresh", thresh) 


	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	sd = ShapeDetector()	

		# loop over the contours
	for c in cnts:
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		M = cv2.moments(c)
		if M["m00"] != 0 and cv2.contourArea(c) > 500  : 
			cX = int((M["m10"] / M["m00"]) * ratio)
			cY = int((M["m01"] / M["m00"]) * ratio)
			shape = sd.detect(c)
		 	
			# multiply the contour (x, y)-coordinates by the resize ratio,
			# then draw the contours and the name of the shape on the image
			c = c.astype("float")
			c *= ratio
			c = c.astype("int")
			if shape == "rectangle" or shape == "square" :
				print "rect detected"
			cv2.drawContours(roi, [c], -1, (0, 255, 0), 2)
			cv2.putText(roi, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (255, 255, 255), 2)
			cv2.imshow("Image", roi)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
	 	
		# show the output image
#----------------------------------------------------------------------------------------------------------
#						                Detect Movements
'''	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	if firstFrame is None:
		firstFrame = gray

	frameDelta = cv2.absdiff(gray,firstFrame )
	thresh = cv2.threshold(frameDelta,threshold, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=2)
	(_,cnts, khai) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	for c in cnts:
        
		if cv2.contourArea(c) < args["min_area"]:
			continue

		(x, y, w, h) = cv2.boundingRect(c)        
		# rects.append((x, y, w, h))

		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	#cv2.drawContours(img, cnts, -1, (0,255,0), 3)
	cv2.imshow("movements",img)	    
'''

#----------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------


cap.release()
cv2.destroyAllWindows()
