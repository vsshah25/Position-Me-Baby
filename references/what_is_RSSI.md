In telecomminications, RSSI (received signal strength indicator) is a measurement of the power present in a received radio signal.

RSSI is of no use for a user of hotspot created by the router. But coz the signal strength can vary greatly and affect the functionality of networking, IEEE 802.11 devices often make the measurements available to all .

About IEEE 802.11: 
IEEE 802.11 is set of specifications of media access control (sublayer of second layer of the OSI model) and physical layer (the 1st layer of the OSI model). 

RSSI output is ADC analog value. It can be sampled by an ADC and the resulting codecs(data) can be used further. The RSSI in 802.11 is an indication of power level being received.
But 802.11 standard does not define any equations of power (in watts) and the DC analog value we get. But you can say for sure that if the RSSI value increases, the power increases.
In order to calculate probably calibration based on experimental data will help.

RSSI has been replaced in most of the scenarios with RCPI(received channel power indication)         

</br>
</br>
</br>

# RSSI to distance

This is the relation between distance and the received power signal. 

**![rssi_distance.png](https://lh4.googleusercontent.com/qhHNGTuqD84Z4YnDmLChOZTzBp3x9I9ZrbIAy0Cwad6ViMW32A-oqfUpJvkIj0KLwOzwNSySv0-YI086DLNDe2-8C0flKtmrgkC13yzs_fF4sS7gVuNLMhF8iJq-O_ZD1Hq9CqHn)**

- Fm = Fade Margin
- N = Path-Loss Exponent, ranges from 2.7 to 4.3
- Po = Signal power (dBm) at zero distance
- Pr = Signal power (dBm) at distance
- F = signal frequency in MHz

# Fade Margin : 
Fade margin is the difference in power levels between the actual signal hitting the receiver and the bottom-line minimum signal needed by the receiver to work. It gives an indication of likely bit error rates for instance.
There is a standard formula for calculating minimum theoretical signal level needed by a receiver for a given data rate. This is -154dBm + 10log10(bit rate).

**To get the power received we need to lookup the programming of the wifi receiver devices **

</br>
</br>
</br>


**Note** : 
RSSI (signal strength) readings can be affected by reflections, position of objects in the target space, object motion, line of site or not between nodes, number of nodes, presence of other unrelated signals on the allocated frequency band (or stronger ones out of band), directionality (or not) of antennas, front end overload and intermodulation performance, system signal to noise ratio. Calibration infi hai :sweat:
RSSI distance measurements almost certainly need to be based on multiple signal attempts processed in some way. Having reference nodes of known distance can help. We can have fixed "beacons" with moving targets, or moving beacons with fixed targets, or some mix.



To get the final position, here are some of the things we can do: 
- get angle of the approach, for that matter, get angle w.r.t any fixed reference. 
- Apply triangulation to get position. For this we need more than  router. (3 to be exact)
