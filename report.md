# LOCAL POSITIONING SYSTEM


## Abstract 

We present here the detailed design for a WIFI based positioning system called the Local Positioning System (LPS). This system is designed to work indoors, where the microwave radio signals of the Global Positioning System (GPS) cannot be received.Potential applications for this system range from asset tracking, security, and human-computer interface, to robot navigation and the management of services as diverse as medical care and postal delivery. I first present the issues surrounding its conceptual design and then describe in detail the component level implementation of the prototype LPS system, which we have designed and built but not yet tested as a whole.

Our problem statement which precisely describes the problem which we are aiming to tackle goes as follows: 
**To design a system which is able to return the coordinates of an object in a given map (size ~100 m*100 m) with accuracy in cms. The solution must be inexpensive and easy to calibrate.**

## 1.Introduction 
</br>

### 1.1 Motivation
	
The location of people and objects relative to their environment is a crucial piece of information for asset tracking, security, and human-computer interface (HCI) applications. These applications may be as simple as tracking the location of a valuable shipping carton or detecting the theft of a laptop computer, or as complex as helping someone to find his or her way around an unfamiliar building. Other applications include the optimization of services such as medical care or postal delivery. Current technologies, such as GPS or differential GPS, can help to solve this problem as long as the people or objects to be tracked are outdoors, where the signals from the 24 orbiting GPS satellites may be received, but there is a latent demand for a similar system that works indoors, where the physics of radio propagation rules out the reception of GPS’s weak microwave signals.
We had once worked on a traffic management system for which the position of the vehicles was an important input for the system to make a decision. It was here where we found out lack of an efficient and an accurate indoor positioning system. 

### 1.2 GPS Technology 

GPS depends on the use of orbiting space-based atomic clocks, spread spectrum microwave radios, high speed digital signal processing (DSP), and sophisticated mathematics including algorithms that compensate for general relativity. GPS receiver is capable of reporting the user’s position to within 50m RMS accuracy at any point on the Earth’s surface.  However, GPS suffers from a fundamental limitation: it cannot be used indoors. The microwave signal from the GPS satellites is extremely weak by the time it arrives at the Earth’s surface, and the presence of the leaves of a tree or the roof of a building in the GPS signal path reduce the signal strength to imperceptible levels. Even the use of sophisticated cryogenically cooled receiver electronics cannot recover GPS signals when deep inside a typical reinforced concrete building; the imperceptibly weak GPS signals are overwhelmed by interference from other electronic equipment or more fundamentally by the blackbody radiation of the building itself. The problem is roughly equivalent to trying to see and decode morse code sent by the beam of a flashlight on Earth-- from the surface of Mars. 


## Approach
The underlying technology used is analyzing wireless connection which follows IEEE 802.11 protocol also called WIFI. 
The fundamental principle is to estimate the distance between 2 nodes of the wifi network by analysing the signal characteristics of the wireless connection. There are many signal properties which can be analyzed to estimate the distance between two nodes but as now we are focussing on RSSI(received signal strength indicator) and path loss exponent. In telecommunications, *RSSI* (Received Signal Strength Indicator) is a measurement of the power present in a received radio signal. And *path loss* (or path attenuation) is the attenuation in power density of an electromagnetic wave as it propagates through space.
There exists an analytical formula relating distance with these signal parameters. But the actual measured distance deviates from the calculated value due to the constantly changing environmental characteristics which unfortunately can't be modeled in an analytical expression as an independent variable. In a situation where an explicit function is not known but the variables (parameters) which should be in the function are known, machine learning comes to help. For the learning fo model a dataset of the values of the parameters and the value of distance(target variable) needs to be created. 
Having trained the model, distance from one fixed position is known. This is repeated for 3 different positions and finally the exact coordinates of the object are calculated using trilateration. 
 

### WIFI  

Wi-Fi or Wireless Fidelity is a technology for wireless local area networking with devices based on the IEEE 802.11 standards. Wi-Fi most commonly uses the 2.4 gigahertz (12 cm) UHF and 5 gigahertz (6 cm) SHF ISM radio bands.
IEEE 802.11 is a set of media access control (MAC) and physical layer (PHY) specifications for implementing wireless local area network (WLAN) computer communication in the 900 MHz and 2.4, 3.6, 5, and 60 GHz frequency bands. They are created and maintained by the Institute of Electrical and Electronics Engineers (IEEE) LAN/MAN Standards Committee (IEEE 802). 
The router becomes an informal access point for the Internet, creating an invisible "cloud" of wireless connectivity all around it which is known as a hotspot. Any device under the scope of hotspot can connect to it and form a LAN. So basically, WIFI is wireless form of LAN. More technically, WIFI is known as IEEE 802.11.

The wifi receivers are just decoders and encoders which are capable of encoding and decoding data from electromagnetic( radio) to electrical signals(digital).
The frequency used for LPS is 2.4gHz.


## RSSI
RSSI (received signal strength indicator) is a measurement of the power of a received radio signal. RSSI is of no use for a user of hotspot created by the router. But because the signal strength can vary greatly and affect the functionality of networking, IEEE 802.11 devices often make the measurements available to all. 
The RSSI output is an analog value which can be sampled by an ADC. The RSSI in 802.11 is an indication of the power level being received.
But 802.11 standard does not define any equations of power (in watts) and the DC analog value we get. But you can say for sure that if the RSSI value increases, the power increases.In order to calculate probably calibration based on experimental data will help.
RSSI (signal strength) readings can be affected by reflections, position of objects in the target space, object motion, line of site or not between nodes, number of nodes, presence of other unrelated signals on the allocated frequency band (or stronger ones out of band), directionality (or not) of antennas, front end overload and intermodulation performance, system signal to noise ratio. RSSI distance measurements almost certainly need to be based on multiple signal attempts processed in some way. 

### RSSI to distance

This is the relation between distance and the received power signal. 

**![rssi_distance.png](https://lh4.googleusercontent.com/qhHNGTuqD84Z4YnDmLChOZTzBp3x9I9ZrbIAy0Cwad6ViMW32A-oqfUpJvkIj0KLwOzwNSySv0-YI086DLNDe2-8C0flKtmrgkC13yzs_fF4sS7gVuNLMhF8iJq-O_ZD1Hq9CqHn)**

- Fm = Fade Margin
- N = Path-Loss Exponent, ranges from 2.7 to 4.3
- Po = Signal power (dBm) at zero distance
- Pr = Signal power (dBm) at distance
- F = signal frequency in MHz

#### Path Loss estimation techniques

In most radio transceiver modules, the measurement of received power is just an auxiliary function. The measured value provided by the module may not be exactly received power in dBm. However, received signal strength indicator (RSSI) is used to represent the condition of received power level. This can be easily converted to a received power by applying offset to obtain the correct level:

**![](https://lh6.googleusercontent.com/bDMhUrdkqVenVwa9qVZ4g_WDlEymHZflDIMV9Eyx6_dAcGkNcXSkxZAyg89u8fZviD5OrCqp6yCJVIXrh-wNqNOSPAS3XztQREBLXkIOHpXXyojWPDmqKOvimHBfErn_Z_1uAPy5)**

where,
- Pi = actual received power from transmitter node i.
- RSSIi = measured RSSI value for transmitter node i, (which is stored in the RSSI register of the radio transceiver) 
RSSI offset is the offset found empirically from the front end gain and it is approximately equal to −45 dBm. 

</br>
This is to make sure that the actual received power value has dynamic range from −100 to 0 dBm, where −100 dBm indicates the minimum power that can be received, and 0 dBm indicates the maximum power received. 

If RSSI ranging is used to measure the distances between transmitter and receiver, log-distance path loss model [18] is used to express the relationship between received power and the corresponding distance as shown in the following expression:

**![](https://lh3.googleusercontent.com/8s0yWhG1mmcUQPpFjhSlPm_GXcSVr0JR8WLUQEk0Pf0hg-JzV-My586lMHXi_3TAsmkUslM6dGS5HTbooqB20OR5pxnTSBsLCzE0Lf-BfeUsaF_URsLn8X4pUNSMlKt-JURYqOM8)**

where,
- Pr(d) = received power of the receiver measured at a distance d to the transmitter, which is expressed in dBm.
- n = path loss exponent 

**Note** : 
In path loss model, two important parameters are used to characterize environment: path loss exponent n and the received power Pr(d0). Pr(d0) is the measured received power at distance d0 to the transmitter. To characterize the environment for RSSI ranging, received power Pr(d0) is first measured by allocating a receiver d0 apart from the transmitter. d0 is generally fixed at 1m. After Pr(d0) is obtained, the receiver is moved to other locations randomly to measure the received power with the corresponding distance.

There are two methods to estimate the path loss exponent: 

- One method is to calculate the path loss exponent using a number of received powers and the corresponding distances. This method is called one-line measurement as the collection of RSSI values was done by locating the transmitter and receiver along a straight line, and varying the distance between them.

- Another method is to directly update the environmental parameters using gradient descent technique. In this case, measurement of received power can be done in spread and random style as long as the exact locations in the area are known. This method is called online-update measurement as the environmental parameters such as path loss exponent can be updated continuously regardless of the change of environment.

For further details [click here]("https://github.com/pranav1001/Position-Me-Baby/blob/master/references/reference_articles/path_loss_exponent_estimation.pdf")

</br>
</br>
</br>

### Fade Margin : 
Fade margin is the difference in power levels between the actual signal hitting the receiver and the minimum signal needed by the receiver to work. It gives an indication if there are any errors in bit rates.
The standard formula for calculating minimum theoretical signal level needed by a receiver for a given data rate is -154dBm + 10log10(bit rate).

### RSSI Signal Improvement

Radio ranging using RSSI generally considers three models: 
- small scale (spatial and temporal) multipath fading model,
- medium scale (spatial) shadowing model
- large scale (spatial) path loss (PL) model 

**![rssi_model.png](https://lh4.googleusercontent.com/1Zi3tO954zQ9XgQgTstx4kLGqBytEpBECsWWXrWjt59MzvVDaFfdHVtbkQkNYz_Jg4Yx9bgUX2ydtPfu9K6_jLSUmFn6XMAU0kanSPuOlrviqHQ2rl1ueV8As1NS-mmi9-9_I8PB)**



### NodeMCU's 
<<<<<<< HEAD




=======
The technology which we are using for getting the distance is the wifi RSSI(Received Signal Strength Indicator) value. Basically it is a measure in the loss of power when a signal reaches a receiver from a transmitter. For getting the RSSI values, Node MCU(a wifi transceivers) are one of the best options for getting the RSSI value.For the later part I have referred the Node MCU's as simply nodes.
In our project we are using 4 nodes as reference points at the four corners of a rectangular room(suppose for now). These nodes are sending RSSI values to a central co-ordinator which is also a similar node(this central node can be replaced by the laptop). Now the four nodes at the corners are sending the rssi value and the central one is receiving those values.
One important thing is that these nodes use UDP protocol for communication.For those who don't know what UDP protocol is they can go through [this](http://www.erg.abdn.ac.uk/users/gorry/course/inet-pages/udp.html).
**![node_mcu.jpeg](https://github.com/sabSAThai/Position-Me-Baby/blob/master/images/node_mcu.jpeg)**

>>>>>>> 575ee9f0ce77f2eb379816434395ece8143060ba
### Dataset

To model the constantly changing environmental characteristics we need to implement machine learning algorithms which need a dataset of various measurable properties of the system. 
The parameters of dataset are actual distance of object and reference points from the router and RSSI value of the connection between object and reference points from the router.

To create the dataset the actual distance between router and reference points, and between router and object is measured using image processing. The object is moved across the room in discrete steps and at every position its distance and RSSI values are logged.

<<<<<<< HEAD
The values of RSSI

### Machine learning algorithm  

The ML algorithm we are using is Multilayer Perceptron layer Neural Network.

**![ML model](https://github.com/sabSAThai/Position-Me-Baby/blob/master/images/Ml_model.jpg)**

We measure the RSSI values of all the signal connections. What we get is RSSI values of 4 reference points and RSSI of object which we want to localize. 
To add the information of the analytical expression, using the distance between router and the reference point and its RSSI value, we obtain the value of eta which represents a quadrant of the room.

The model is trained on dataset and saved. After the model has been trained, the model is ready to spit out the value of distance given the inputs. 

As of now, we have been successful in achieving accuracy of 4cm. With some further modifications in the model we are expecting to obtain more accuracy. 

The modifications are as follows: 
- Apply Principal Component analysis on the dataset to remove redundancy. 
- Add a feature in the learning algorithm which accounts for the room modeling 
- Optimize the hardware used in the model 
- Improve the signal received using hardware and some specific filtering algorithms.
