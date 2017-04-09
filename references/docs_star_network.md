The technology which we are using for getting the distance is the wifi RSSI(Received Signal Strength Indicator) value. Basically it is a measure in the loss of power when a signal reaches a receiver from a transmitter. For getting the RSSI values, Node MCU(a wifi transceivers) are one of the best options.For the later part I have referred the Node MCU's as simply nodes.

In our project we are using 4 nodes as reference points at the four corners of a rectangular room(suppose for now). These nodes are sending RSSI values to a central co-ordinator which is also a similar node(this central node can be replaced by the laptop). Now the four nodes at the corners are sending the rssi value and the central one is receiving those values. Coming to the arduino code part, below is the explanation of certain parts of the code.
One important thing is that these nodes use UDP protocol for communication.For those who don't know what UDP protocol is they can go through [this](http://www.erg.abdn.ac.uk/users/gorry/course/inet-pages/udp.html).

# **Sender Code**
The first two lines includes the esp8266 library and the wifi udp library.Then we define an object of the WiFiUDP class which has functions for sending the packet as we shall see later...
```C++
 #include <ESP8266WiFi.h>
 #include <WiFiUdp.h>

 WiFiUDP UDP;
```
For connecting to any router(secured router),it requires a password.So first the node looks for the router with the given ssid and then matches the password to set up a wifi connection.

```C++
const char *ssid = "Tinkerers' Lab";
const char *password = "tinker@tl";
```
The sender needs to know the address(IP addr) of the node to which it is sending.This part is manual and the user has to manually set the ip addr assigned to the receiver node end.
```C++
const char UDP_REMOTE_HOST[] = "192.168.0.128";    // IP address assigned to the receiver.
```
The payload(data) that is being sent contains a string whose format is :: **nodeid_rssivalue**
where node_id belongs to {0,1,2,3}

In the setup function, the main task that is performed is to begin the connection with the router and wait until the connection is set up.
```C++
WiFi.begin(ssid, password);
 
while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
} 
Serial.println(WiFi.localIP());     // prints on the serial the IP address assigned to that specific node.
```

Now comes the everlasting loop function.Everytime it creates a packet with the format specified above. The main Hero in this code is the built-in function provided by the arduino library **WiFi.RSSI()** which returns the rssi value of a particular connection.
```C++
char packet_to_send[15] = "0_";
long rssi = WiFi.RSSI();
```
The for loop specifically appends the rssi value at the end of the packet created above.
```C++
for(i = 2; i<2+rssi_string.length();i++){
    packet_to_send[i] = rssi_string[i-2];
}
```

So what to do after setting up the connection and creating the packet. Yes, you guess it right.Finally,time to send the packet using the UDP object created in the beginning of the program.
```C++
UDP.beginPacket(UDP_REMOTE_HOST, UDP_REMOTE_PORT);
UDP.write(packet_to_send);
UDP.endPacket();
```

# **Receiver Code**
This part is very much similar to the sender code hence things which are in repititions are not covered in this section.
The receiver has to receive the rssi values from all the nodes.For this the receiver stores the rssi values(along with id) in a buffer and prints it on the serial.
In the beginning of the code the maximum size of the packet which is going to be received is defined so that it ensures that everytime only that amount of memory is allocated to store the packet received.
```C++
#define UDP_TX_PACKET_MAX_SIZE 5
```
Then the node ids of the sending nodes are defined for identification.
```C++
char TRIGGER_STRING1[] = "0_";
char TRIGGER_STRING2[] = "1_";
char TRIGGER_STRING3[] = "2_";
char TRIGGER_STRING4[] = "3_";
```
In the loop function, with every loop it parses(reads) the data stored in UDP buffer(and if some data is available) it stores it in the packetBuffer. 
```C++
int packetSize = UDP.parsePacket();
if (packetSize > 0){
	IPAddress remote = UDP.remoteIP(); 
	UDP.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE); 
}
```

In this way the star network of nodes communicates.
