# What are routers ? 
 
Before delving into details of routing mechanism and routers, let's have a look at some basic terminlogies/concepts/entities frequently used in computer networking. 

</br> 

## Basics: 

- #### IP Address
In order to communicate, the first and the most obvious thing is to know is the location of the PC with whom we intend to exchange data. And that's the reason, we define IP address for each communicating device. If there is another computer on the same network with the same IP there will be an IP address conflict and both computers will lose network capability until this is resolved.

</br>
The IP address itself is bifurcated into a network address and a host address. As an example, for an IP address of 192.168.0.45, the network id would be 192.168.0 and the host id would be 45. Computers can only communicate with other computers on the same network id.

- #### Subnet Mask
As a general rule wherever there is a 255 in the subnet mask then the corresponding number of the IP address is part of the network id; where there is 0 in the subnet mask the corresponding number in the IP address is part of the host id. 
As an example, let’s say you have an IP address of 192.168.0.1 with a subnet mask of 255.0.0.0. This tells the computer that the first number of the IP address is to be used as the network address and the last 3 are to be used as the host id.   
- Router (basics)
We saw above that computers on different network cannot communicate between each other. To make it possible we use routers. Networking will work across different network IDs as long as there is a router between them.

</br>  
A router in its basic form is simply a network device with 2 network interfaces (NICs), each being on separate network ids. So, you may have 2 networks; 192.168.1.x and 192.168.2.x. On one NIC  the router would have the IP address 192.168.1.1 and on the other it would have an IP address of 192.168.2.1. Computers on the 192.168.1.x network can now communicate with computers on the 192.168.2.x network by the virtue of the fact that they are connected via router.

- Default Gateway
The default gateway is where your computer sends traffic (packets) to if it doesn’t know where the destination IP address. The default gateway is always a router.
When a computer tries to send data on the same network, there are no issues whatsoever coz it knows about the network it is connected to. Problem arrives when it tries to send data to an altogether different network. Since it has no idea about the other network, it sends all the data through a fixed common _gateway_ . 

</br>
Since you want to send your data to different networks,obviously the "route" you take is connecting your network and the other networks. This common junction is essentially a router. So you will set the gateway as the default IP address of the router so that the router can provide a *route* for your data. 

</br>

##### A small note on how using routers you access a website halfway around the world. 
</br>
Routers also have default gateways so that if they don’t know where the destination is it also sends the data onto it’s own default gateway. This continues up the IP network hierarchy (tree) until it eventually finds a router that is part of the destination network. This last router knows where the destination is and sends it on it’s way. You have your own network in your house but the internet is a different network. When you want to access that website half way around the world your computer has no idea how to get there so it first of all sends it onto the default gateway. This process continues unless and until the packet reaches the destination.

</br>

- DHCP (Dynamic Host Configuration Protocol)
ALl these networking parameters discussed above need to be assigned by someone to our PC. But I don't think anyone of us has ever done that coz this is automatically configured when your PC boots up by a process known as DHCP.
But there might be situations when your computer's dhcp is disabled (might be done by you or by some system settings) and then u have to manually configure the IP address, subnet mask and other details related to the network which you want to connect to.

</br>
Basically all it does is to assign out all the corect IP information to computers automatically so everything is configured to work on that network without user input.


I think it's enough for the basics. Let's get our asses started on routers.

So let's come back to our question,** How do routers work ? **

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
  Note thatthis is the only row where the gateway is 192.168.0.1.  This line tells the computer that for ALL traffic no matter what the destination IP address is send it to 192.168.0.1. This is my default gateway. It is the last route it evaluates if it can’t find a more specific match in the routing table.	

- 192.168.0.0 – this is for your local network (LAN). 

The other lines will be explained further. If not explained then not relevant for us. As an article says thet are some default value. Anyways, ditch. We will focus on the relevant stuff. 

</br>
Now let's see how the routing table is processed. 

Before sending a packet your PC looks up the destination IP address in the routing table to determine the best route possible. 



