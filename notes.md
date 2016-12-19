Our get started plan was to use ultrasonic sensors and the implement triangularization to get distance. 
Pains are : Ultrasonic suck in accuracy.
	    Light of sight. (peizo based ultrasonic transducers have a cone of 30 degrees but still at the corners the system will fail.)

New strategy : Use wifi RSSI 
There would be a routers/router to send data and wifi receivers to recei
ve the same. 
For wifi reciever/receivers wer have 2 options :
					- cell phones
					- zigbee modules 
For cell phones we need to develop an android app to get compute the RSSI Computations. If android app doesn't work well we can create a serve where we can upload the data and the computatio will be done at the server level. Handling servers and its communication with clients can be done on python. 

If we use zigbees, first point is we need to invest a litte bit or we can ask the prof to get it done. Secondly, we would need a microcontroller to handle all the computations.

Another issue: If there are random obstacles in the enviroment which would be pretty much the case, we need to check upto what extent it is affecting the calculations. If they are substantial effects then we need to figure out a way to quantify them. One way to do it is to experiment and calibrate. 
this can be postponed for a while and focus on the no obsatcle free localization.

RSSI value varies over factors like humidity, etc. So instead of implementing RSSI, we can try relative RSSI. By relative RSSI I mean, RSSI- ambient_RSSI 

  
	    			    	 
