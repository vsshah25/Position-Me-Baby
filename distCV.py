import argparse
import cv2
import imutils
import time
import numpy as np 

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=800, help="minimum area size")
args = vars(ap.parse_args())


firstFrame = None
threshold = 100        #calibrate

if args.get("video", None) is None:
    cap = cv2.VideoCapture(-1)
    time.sleep(0.25)
 
# otherwise, we are reading from a video file
else:
    cap = cv2.VideoCapture(args["video"])

if(cap.isOpened()==False):
        print 'error'


boundaries = [
	([17, 15, 100], [50, 56, 200]),
	#([86, 31, 4], [220, 88, 50]),
	#([25, 146, 190], [62, 174, 250]),
	#([103, 86, 65], [145, 133, 128])
]
# ([17, 15, 100], [50, 56, 200]) implies that R >= 100, B >= 15, and G >= 17 along with R <= 200, B <= 56, and G <= 50 will be considered red.

def detect_color(img):
	# loop over the boundaries
	# for (lower, upper) in boundaries:
	# 	# create NumPy arrays from the boundaries
	lower = np.array([17, 15, 100], dtype = "uint8")
	upper = np.array([50, 56, 200], dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(img, lower, upper)
	output = cv2.bitwise_and(img, img, mask = mask)
	
    return output
		# show the images
	#cv2.imshow("images", np.hstack([img, output]))	




if(cap.isOpened()==False):
        print 'error'

while (cap.isOpened()):

	(grabbed, frame) = cap.read()

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




	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break



# cleanup the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
