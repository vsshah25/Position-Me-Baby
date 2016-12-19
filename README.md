Hello :smiley:

We are aiming to localise an object in a closed room of given dimensions. Technically speaking, we are trying to get the co-ordinates of an object w.r.t the room. 


Our setup :

**![setup.jpg](https://lh3.googleusercontent.com/f_es4LcptbaIX3OgNvNJrrwy0wemO15gNM1_mpcWDHfqBRMe8X1n5wB3tXBpI_SCFGwwfc0TrP613-uP6S8be2wJoR_-1IUJVu-cndkXkfck9tyG5CjXmT0I6IicszM1rhb6G6JM)**



Working : 

**![model.jpg](https://lh5.googleusercontent.com/r76gHACgSBFo-jQUVcIS1vHyGGp7yDBUdSsMMtg2TIF63tDcKmuDxQx3Rf0dKmqJnqykBKPznAMxb-JufeljTV7NnfnPTXtsScM0xzUV8nsJgZNuqTpNqMDd_UG5EUzKfNHS-wbb)**

</br>

The transmitters send a signal which is catched by the receiver. The transmitters send signals in specific intervaks if time and one after other (to ensure no mixing up of 2 signals). 
Based on the time at which the signal is recieved, the distance from the corresponding transmitter is calculated. 
Thus for the transmitter, the reciever must be on one of the point of the circle with the transmitter at the center and radius equal to the distance calculated. 

</br>

The intersection of circles localises the object. The accuracy getting better with increasing the number of transmitters. 

</br>

using laser sensors and odometry to get the distance. 



