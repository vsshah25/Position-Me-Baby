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

Signal processing, computation technology, and space science have advanced considerably over the past 50 years. GPS depends on the use of orbiting space-based atomic  A Phase Measurement Radio Positioning System for Indoor Use Reynolds 8 clocks, spread spectrum microwave radios, high speed digital signal processing (DSP), and sophisticated mathematics including algorithms that compensate for general relativity. The initial design and deployment of GPS for military use by the Department of
Defense in the 1980s has led to the availability of inexpensive commercial GPS receivers in the 1990s. In 1998, a consumer GPS receiver fits in the palm of a hand and costs its manufacturer less than fifty dollars to make. This receiver is capable of reporting the user’s position to within 50m RMS accuracy at any point on the Earth’s surface.  However, GPS suffers from a fundamental limitation: it cannot be used indoors. The microwave signal from the GPS satellites is extremely weak by the time it arrives at the Earth’s surface, and the presence of the leaves of a tree or the roof of a building in the GPS signal path reduce the signal strength to imperceptible levels. Even the use of sophisticated cryogenically cooled receiver electronics cannot recover GPS signals when deep inside a typical reinforced concrete building; the imperceptibly weak GPS signals are overwhelmed by interference from other electronic equipment or more fundamentally by the blackbody radiation of the building itself. The problem is roughly equivalent to trying to see and decode morse code sent by the beam of a flashlight on Earth-- from the surface of Mars. 

### 1st model 
Using ultrasonic sensors   


## Approach
The underlying technology we are using is analyzing wireless connection which follows IEEE 802.11 protocol also called WIFI. 
The fundamental principle is to estimate the distance between 2 nodes of the wifi network by analysing the signal characteristics of the wireless connection. There are many signal properties which can be analyzed to estimate the distance between two nodes but as now we are focussing on RSSI(received signal strength indicator) and path loss exponent. In telecommunications, *RSSI* (Received Signal Strength Indicator) is a measurement of the power present in a received radio signal. And *path loss* (or path attenuation) is the attenuation in power density of an electromagnetic wave as it propagates through space. These parameters will be explained in depth later.
Ideally, there should be an analytical formula relating distance with these signal parameters and yes such an analytical expression does exist. But the actual measured distance deviates from the value which we get from the above mentioned expression. And the credit goes to the constantly changing environmental characteristics which unfortunately can't be modeled in an analytical expression as an independent variable. In a situation where you can't have an explicit function but you know the variables (parameters) which should be in the function, machine learning comes to help. Now having established that we are going to use learning to model, the first thing we need to have is a database of the values of the parameters and the value of distance which is the target variable which we are intending to predict. 
We will detail the process of preparing a dataset later. After having the dataset ready, just put on your shoes and march out to train our learning algorithm. Having done the training, the model is ready to spit out values of distance given the required parameters. To get the position, we will be doing trilateration using 3 such systems. 
 

### WIFI  

Wi-Fi or Wireless Fidelity is a technology for wireless local area networking with devices based on the IEEE 802.11 standards. Wi-Fi most commonly uses the 2.4 gigahertz (12 cm) UHF and 5 gigahertz (6 cm) SHF ISM radio bands.
IEEE 802.11 is a set of media access control (MAC) and physical layer (PHY) specifications for implementing wireless local area network (WLAN) computer communication in the 900 MHz and 2.4, 3.6, 5, and 60 GHz frequency bands. They are created and maintained by the Institute of Electrical and Electronics Engineers (IEEE) LAN/MAN Standards Committee (IEEE 802). 
The router becomes an informal access point for the Internet, creating an invisible "cloud" of wireless connectivity all around it which is known as a hotspot. Any device under the scope of hotspot can connect to it and form a LAN. So basically, WIFI is wireless form of LAN. More technically, WIFI is known as IEEE 802.11.

The wifi receivers are just decoders and encoders which are capable of encoding and decoding data from electromagnetic( radio) to electrical signals(digital).
More on frequencies of WIFI: There are two types of Wi-Fi signal, based on the frequencies they use:
2.4GHz - A lower frequency, this is the more common Wi-Fi technology in use today. Many devices use it, so the signals can become more crowded and interfere with each other. It can pass through walls and windows fairly well.
5GHz - This higher frequency technology is used by fewer devices, and can sometimes achieve higher speeds because the frequencies are less crowded. It cannot pass through walls and windows as well as the 2.4GHz band signals, so the range of 5GHz technology is often shorter.


## RSSI
In telecommunications, RSSI (received signal strength indicator) is a measurement of the power present in a received radio signal. RSSI is of no use for a user of hotspot created by the router. But because the signal strength can vary greatly and affect the functionality of networking, IEEE 802.11 devices often make the measurements available to all. 
The RSSI output is an analog value. It can be sampled by an ADC and the resulting codecs(data) can be used further. The RSSI in 802.11 is an indication of the power level being received.
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

- Another method is to directly update the environmental parameters using gradient descent technique. In this case, measurement of received power can be done in spread and random style as long as the exact locations in the area are known. This method is called online-update measurement as the environmental parameters such as path loss exponent can
be updated continuously regardless of the change of environment.

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

Among them, multipath fading effect is unwanted and can be mitigated by filters. Shadowing model explains the slow signal strength fluctuation versus distance. This effect is caused by multipath signal propagation encounters such as reflection(s) and diffraction. This effect can be emulated by ray tracing method. The last model, path loss model is an empirical model which describes the attenuation of signal strength versus distance. It is the only model contributing to RSSI radio ranging.
RSSI signal improvement mainly involves filtering noise and fast fading effect. This increases the stability of the RSSI signal. 

Let's study about multipath effect: 
In wireless telecommunication, multi-path is the propagation phenomena that results in radio signals
reaching the receiving antenna by two or more paths.

</br>
In a typical wireless communication environment, multiple propagation paths exist between transmitter
and receiver due to scattering by different objects. Thus, copies of the signal following different paths can undergo different attenuation, distortions, delays and phase shifts. Constructive and destructive interference can occur at the receiver. When destructive interference occurs, the signal power can be significantly diminished.
This phenomenon is called fading.

- **Frequency Selective fading**: The transmitted signal reaching the receiver through multiple propagation paths, having a different relative delay and amplitude. This is called multipath propagation and causes different parts of the transmitted signal spectrum to be attenuated differently, which is known as frequency-selective fading.

- **Frequency Non-Selective fading**: If all the frequency components of the signal would roughly undergo the same degree of fading, the channel is then classified as frequency non-selective (also called flat fading).

- **Slow fading**:
Slow fading is a long-term fading effect changing the mean value of the received signal. Slow fading is
usually associated with moving away from the transmitter and experiencing the expected reduction in signal strength. Slow fading can be caused by events such as shadowing, where a large obstruction such as a hill or large building obscures the main signal path between the transmitter and the receiver.

- **Fast fading**:
Fast fading is the short term component associated with multipath propagation. It is influenced by the
speed of the mobile terminal and the transmission bandwidth of the signal. In a fast fading channel, the rate of change of the channel is higher than the signal symbol period and hence the channel changes over one period

This section describe methods that can help reduce the problem of fading in wireless communication channels. 
They are:
- Diversity for fast and slow fading 
- Equalization for flat and frequency selective fading
- Rake receiver for multipath fading
- Channel Coding for deep fading.

For details on individual techniques [click here]("https://github.com/pranav1001/Position-Me-Baby/blob/master/references/reference_articles/fading_reduction_technique.pdf")

[Click here]("https://github.com/pranav1001/Position-Me-Baby/blob/master/references/reference_articles/reduce_ISI_effects.pdf") for an article on removal of fast fading effect using artificial neural networks. 


### DIVERSITY

Diversity is a method used to develop information from several signals transmitted over independent fading paths. It exploits the random nature of radio propagation by finding independent signal paths for communication. It is a very simple concept where if one path undergoes a deep fade, another independent path may have a strong signal. As there is more than one path to select from, both the instantaneous and average SNRs at the receiver may be improved. Receivers in diversity technique are used in such a way that the signal received by one is independent of the other. We take up the types one by one in the sequel. 

#### Space Diversity 
A method of transmission or reception, or both, in which the effects of fading are minimized by the simultaneous use of two or more physically separated antennas, ideally separated by one half or more wavelengths. 
</br>
Space diversity reception methods can be classified into four categories:
#### Selection Diversity:
The basic principle of this type of diversity is selecting the signal which has the maximum SNR value among all the signals received from different branches at the receiving end. ‘M’ demodulators are used to provide M diversity branches whose gains are adjusted to provide the same average SNR for each branch. The receiver branches having the highest instantaneous SNR is connected to the demodulator. It is not an optimal diversity technique as it doesn’t use all the possible branches simultaneously.

#### Feedback or Scanning Diversity:
Scanning all the signals in a fixed sequence until the one with SNR more than a predetermined threshold is identified. Quite similar to Selection diversity. 

#### Maximal Ratio Combining:
Signals from all of the M branches are weighted according to their individual signal voltage to noise power ratios and then summed. Requires an individual receiver and phasing circuit for each antenna element. Produces an output SNR equal to the sum of all individual SNR. Advantage of producing an output with an acceptable SNR even when none of the individual signals are themselves acceptable.

#### Equal Gain Combining:
In some cases it is not convenient to provide for the variable weighting capability required for true maximal ratio combining. In such cases, the branch weights are all set unity, but the signals from each branch are co-phased to provide equal gain combining diversity. It allows the receiver to exploit signals that are simultaneously received on each branch.

#### Polarization Diversity
Polarization Diversity relies on the decorrelation of the two receive ports to achieve diversity gain. The two receiver ports must remain cross-polarized. Polarization Diversity at a base station does not require antenna spacing. Polarization diversity combines pairs of antennas with orthogonal polarizations. Reflected signals can undergo polarization changes depending on the channel. Pairing two complementary polarizations, this scheme can immunize a system from polarization mismatches that would otherwise cause signal fade. Polarization diversity has prove valuable at radio and mobile communication base stations since it is less susceptible to the near random orientations
of transmitting antennas.

#### Frequency Diversity
In Frequency Diversity, the same information signal is transmitted and received simultaneously on two or more independent fading carrier frequencies. Rationale behind this technique is that frequencies separated by more than the coherence bandwidth of the channel will be uncorrelated and will thus not experience the same fades.The probability of simultaneous fading will be the product of the individual
fading probabilities.
</br>
Main disadvantage is that it requires spare bandwidth also as many receivers as there are channels used
for the frequency diversity. 

#### Time Diversity
In time diversity, the signal representing the same information are sent over the same channel at different times. Time diversity repeatedly transmits information at time spacings that exceeds the coherence time of the channel. Multiple repetition of the signal will be received with independent fading conditions, thereby providing for diversity. A modern implementation of time diversity involves the use of RAKE receiver for spread spectrum CDMA, where the multipath channel provides 
redundancy in the transmitted message. Disadvantage is that it requires spare bandwidth also as many receivers as there are channels used for the frequency diversity.
</br>

Two important types of time diversity application is discussed below. 
#### RAKE Receiver
CDMA spread spectrum systems, CDMA spreading codes are designed to provide very low correlation between successive chips, propagation delay spread in the radio channel provides multiple version of the transmitted signal at the receiver. Delaying multipath components by more than a chip duration, will appear like uncorrelated noise at a CDMA receiver. CDMA receiver may combine the time delayed versions of the original signal to improve the signal to noise ratio at the receiver.
</br>
RAKE receiver collect the time shifted versions of the original signal by providing a separate correlation receiver for M strongest multipath components. Outputs of each correlator are weighted to provide a better estimate of the transmitted signal than provided by a single component. Demodulation and bit decisions are based on the weighted output of the correlators.

Schematic of a RAKE receiver is shown below : 

**![image](https://lh3.googleusercontent.com/Q98G6LYKqbLVS9_5j9_bSePIjpCoflJ7M1TnyyfJ6sOTuu4OqVnWG2Lyf7ODnilbK1L38BUrLmZh4sIIBX1-4FZT5-cl943DucvfZqEZsP8WYMBMUOxMoDP9q1WaPo-9tGj2Eyd_)**




** Now let’s shift our gears and have a look at hardware we are using. We will come back to signal processing later.**

## Routers  : 

### What are routers ? 
 
Before delving into details of routing mechanism and routers, let's have a look at some basic terminologies/concepts/entities frequently used in computer networking. 

</br> 

## Basics: 

- **IP Address**
In order to communicate, the first and the most obvious thing is to know is the location of the PC with whom we intend to exchange data. And that's the reason, we define IP address for each communicating device. If there is another computer on the same network with the same IP there will be an IP address conflict and both computers will lose network capability until this is resolved.

</br>
The IP address itself is bifurcated into a network address and a host address. As an example, for an IP address of 192.168.0.45, the network id would be 192.168.0 and the host id would be 45. Computers can only communicate with other computers on the same network id.

- **Subnet Mask**
As a general rule wherever there is a 255 in the subnet mask then the corresponding number of the IP address is part of the network id; where there is 0 in the subnet mask the corresponding number in the IP address is part of the host id. 
As an example, let’s say you have an IP address of 192.168.0.1 with a subnet mask of 255.0.0.0. This tells the computer that the first number of the IP address is to be used as the network address and the last 3 are to be used as the host id.   
- Router (basics)
We saw above that computers on different network cannot communicate between each other. To make it possible we use routers. Networking will work across different network IDs as long as there is a router between them.
	
</br>  
A router in its basic form is simply a network device with 2 network interfaces (NICs), each being on separate network ids. So, you may have 2 networks; 192.168.1.x and 192.168.2.x. On one NIC  the router would have the IP address 192.168.1.1 and on the other it would have an IP address of 192.168.2.1. Computers on the 192.168.1.x network can now communicate with computers on the 192.168.2.x network by the virtue of the fact that they are connected via router.

- **Default Gateway**
The default gateway is where your computer sends traffic (packets) to if it doesn’t know where the destination IP address. The default gateway is always a router.
When a computer tries to send data on the same network, there are no issues whatsoever coz it knows about the network it is connected to. Problem arrives when it tries to send data to an altogether different network. Since it has no idea about the other network, it sends all the data through a fixed common _gateway_ . 

</br>
Since you want to send your data to different networks,obviously the "route" you take is connecting your network and the other networks. This common junction is essentially a router. So you will set the gateway as the default IP address of the router so that the router can provide a *route* for your data. 

</br>

##### A small note on how using routers you access a website halfway around the world. 
Routers also have default gateways so that if they don’t know where the destination is it also sends the data onto it’s own default gateway. This continues up the IP network hierarchy (tree) until it eventually finds a router that is part of the destination network. This last router knows where the destination is and sends it on it’s way. You have your own network in your house but the internet is a different network. When you want to access that website halfway around the world your computer has no idea how to get there so it first of all sends it onto the default gateway. This process continues unless and until the packet reaches the destination.

</br>

- **DHCP** (Dynamic Host Configuration Protocol)
ALl these networking parameters discussed above need to be assigned by someone to our PC. But I don't think anyone of us has ever done that coz this is automatically configured when your PC boots up by a process known as DHCP.  

</br>
Basically all it does is to assign out all the correct IP information to computers automatically so everything is configured to work on that network without user input.


I think it's enough for the basics. Let's get our asses started on routers.

So let's come back to our question,**How do routers work ?**

Routing is the process of forwarding IP packets from one network to another. And no need to state the that router is a device that joins networks together and routes traffic between them. . A router will have at least two network cards (NICs), one physically connected to one network and the other physically connected to another network. A router can connect any number of networks together providing it has a dedicated NIC for each network. 

If you don't what a NIC is: 
It is a computer hardware component that connects computers to a network.
The network controller implements the electronic circuitry required to communicate using a specific physical layer and data link layer standard like ethernet ,etc. This provides the base for full network protocol stack.
</br>
The NIC is both a physical layer and data link layer device, as it provides physical access to a networking medium and, for IEEE 802 (which we are gonna use) and similar networks, provides a low-level addressing system through the use of MAC addresses that are uniquely assigned to network interfaces.

Coming back to routers, 
Routers don’t just route traffic to other networks, they learn which are the fastest routes and use them first. It assigns a metric value to each route. A metric value is basically a preference number. If there are two routes leading  to the same destination then the one with the lowest metric is assumed to be the most efficient.

##Routing Table

All network devices that use the TCP/IP protocol have a routing table. ALL devices use their routing table to determine where to send packets. To see routing table on your PC, enter following command in terminal "sudo route -n". No idea about windows, sorry rahega. 

Here is a screenshot of my terminal:

**![table.png](https://lh6.googleusercontent.com/5QlPtPya2enpymwUy66SHiZDo89Lzt3Zl_IGxuu1pWo5eXAYP4R7c-2MG4ldl83rkitK-wyn8Ze1U9kk4Y1H3ScCd5ferFRJFbO26c2fZBRjW3GEfyaWJlnkEPiQRVbYrXnPoriE)** 

Here are the TCP/IP settings of my PC:
IP Address: 192.168.0.0  
Subnet mask: 255.255.255.0
Default gateway: 192.168.0.1

In the table, each row is a route to a specific network or device.

Let's understand the routing table line by line :

- 0.0.0.0 – The 0.0.0.0 network combined with the netmask (subnet mask) of 0.0.0.0 means ALL IP addresses.
  Note that this is the only row where the gateway is 192.168.0.1.  This line tells the computer that for ALL traffic no matter what the destination IP address is send it to 192.168.0.1. This is my default gateway. It is the last route it evaluates if it can’t find a more specific match in the routing table.	

- 192.168.0.0 – this is for your local network (LAN). 

The other lines will be explained further. If not explained then not relevant for us. As an article says that are some default value. Anyways, ditch. We will focus on the relevant stuff. 

</br>
Now let's see how the routing table is processed. 

Before sending a packet your PC looks up the destination IP address in the routing table to determine the best route possible. A more specific match will take priority over others. Once it finds a match it then checks the gateway column of the corresponding match. If it finds the “on-link” status in the gateway column, it means that this network is directly attached so it sends the packets directly to using the NIC(with the interface of my IP address). 

You may wonder what the Iface interface is for. We know that a router has NIC's. We need to specify the NIC we intend to use. 

Let's see an example for step by step understanding of routing. 
The router I am connected to is 192.168.0.1. This router will have its own routing table.  We will join the router to another subnet with it’s second NIC. We assign it an IP address of 192.168.1.254 with a subnet mask of 255.255.255.0
Now our router is aware of two subnets and it knows that it is directly attached to both of them via it’s respective interfaces.

Say I want to communicate to 192.168.1.9. 
- The PC looks at the destination IP address of 192.168.1.9 and looks at it’s routing table to find a match
- As the PC is totally unaware of the other subnet(192.168.1.9) the match is 0.0.0.0 (that means anywhere).
-  In this entry it finds the gateway of 192.168.0.1. The PC now knows that to get to the 192.168.1.x network it must forward the packets onto 192.168.0.1 (the gateway) and does so. 
- The router receives these packets on interface 192.168.0.1 and examines it’s own routing table.
-  It finds a match for this network which states it is directly attached to (on-link) through the interface assigned with IP 192.168.0.1.
- Then the router sends the packet to the other subnet via the NIC. Job done :smiley:

**Summary** : 
All devices have a routing table, without it they wouldn’t know where to send packets to. When a PC sends packets to another PC it looks at it’s routing table to determine the best route possible. If it finds the destination address is “on-link” it knows it is part of the same subnet as the destination and sends the packets directly to the PC. If not it forwards the packet onto whatever is in the gateway field of the matching route entry. This same process is repeated at every router/hop along the way until it eventually arrives at a router that is part of the destination network. The router then sends the packets directly to the destination PC.

**Important Note**: When packets take a certain route to their destination they DO NOT have to take the same route back coz packets DO NOT record the route they take.  



###NodeMCU's 





###Database 

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

###Database

To model the constantly changing environmental characteristics we need to implement machine learning algorithms which need a dataset of various measurable properties of the system. 
The parameters of dataset are actual distance of object and reference points for each of the three routers

To create the dataset the actual distance between router and reference points, and between router and object is measured using image processing. The object is moved across the room in discrete steps and at every position its distance and RSSI values are logged.

 
