#Path Loss estimation techniques

In most radio transceiver modules, the measurement ofreceived power is just an auxiliary function. The measured
value provided by the module may not be exactly received power in dBm. However, received signal strength indicator
(RSSI) is used to represent the condition of received power level. This can be easily converted to a received power by
applying offset to obtain the correct level :

** ![](https://lh6.googleusercontent.com/bDMhUrdkqVenVwa9qVZ4g_WDlEymHZflDIMV9Eyx6_dAcGkNcXSkxZAyg89u8fZviD5OrCqp6yCJVIXrh-wNqNOSPAS3XztQREBLXkIOHpXXyojWPDmqKOvimHBfErn_Z_1uAPy5)**

where,
- Pi = actual received power from transmitter node i.
- RSSIi = measured RSSI value for transmitter node i, (which is stored in the RSSI register of the radio transceiver) 
RSSI offset is the offset found empirically from the front end gain and it is approximately equal to −45 dBm. 

</br>
This is to make sure that the actual received power value has dynamic range from −100 to 0 dBm, where −100 dBm indicates the minimum power that can receive, and 0 dBm indicates the maximum received power. 

If RSSI ranging is used to measure the distances between transmitter and receiver, log-distance path loss model [18] is
used to express the relationship between received power and the corresponding distance as shown in the following
expression:

**![](https://lh3.googleusercontent.com/8s0yWhG1mmcUQPpFjhSlPm_GXcSVr0JR8WLUQEk0Pf0hg-JzV-My586lMHXi_3TAsmkUslM6dGS5HTbooqB20OR5pxnTSBsLCzE0Lf-BfeUsaF_URsLn8X4pUNSMlKt-JURYqOM8)**

where,
- Pr(d) = received power of the receiver measured at a distance d to the transmitter, which is expressed in dBm.
- n = path loss exponent 

**Note** : 
In path loss model, two important parameters are used to characterize environment: path loss exponent n and the
received power Pr(d0). Pr(d0) is the measured received power at distance d0 to the transmitter. To characterize the
environment for RSSI ranging, received power Pr(d0) is first measured by allocating a receiver d 0 apart from the transmitter. d0 is generally fixed at 1 meter. After Pr(d0) is obtained, the receiver is moved to other locations randomly to measure the received power with the corresponding distance.

There are two methods to estimate the path loss exponent: 

- One method is to calculate the path loss exponent using a number of received powers and the corresponding distances. This method is called one-line measurement as the collection of RSSI values was done by locating the transmitter and receiver along a straight line, and varying the distance between them.

- Another method is to directly update the environmental parameters using gradient decent technique. In this case, measurement of received power can be done in spread and random style as long as the exact locations in the area are known. This method is called online-update measurement as the environmental parameters such as path loss exponent can
be updated continuously regardless of the change of environment.

For further details [click here]("https://github.com/pranav1001/Position-Me-Baby/blob/master/references/reference_articles/path_loss_exponent_estimation.pdf")