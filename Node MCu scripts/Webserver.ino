#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

WiFiUDP UDP;


const char *ssid = "TP LINK Wifi";
const char *password = "devsak49";

const uint16_t UDP_LOCAL_PORT =  8051;
char TRIGGER_STRING[] = "node_";

char rssi[4][10];   // decide the postion of this rssi matrix declaration
                                                   
WiFiServer server(80);


void setup() {
  // put your setup code here, to run once:

  pinMode(2, OUTPUT);
  Serial.begin(115200);
  delay(10);

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected"); 
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  // Start the server
  server.begin();
  Serial.println("Server started");


  Serial.println("PROGRAM: starting UDP");
  if (UDP.begin(UDP_LOCAL_PORT) == 1)
  {
    Serial.println("PROGRAM: UDP started");
  }
  else
  {
    Serial.println("PROGRAM: UDP not started");
  }
}


void loop() {
//------------------------------------------
  char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; // buffer(array) to hold incoming packet,
  int packetSize = UDP.parsePacket();

  // the server checks whether there is any packet in its buffer
  if (packetSize > 0)
  {
    Serial.print("PROGRAM: received UDP packet of size ");
    Serial.println(packetSize);
    Serial.print("PROGRAM: from ");
    IPAddress remote = UDP.remoteIP();        // extracts the remote IP of the client
    for (int i = 0; i < 4; i++)
    {
      Serial.print(remote[i], DEC);
      if (i < 3)
      {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(UDP.remotePort());
    UDP.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);    // extract the data from the packet
    packetBuffer[packetSize] = '\0';
    Serial.print("PROGRAM: contents: ");
    Serial.println(packetBuffer);

    int char_to_cmp = 6;                 // chars comparing = node_
    if (strncmp(packetBuffer, TRIGGER_STRING, char_to_cmp) == 0)
    {
      Serial.println("PROGRAM: trigger received");
      // DO YOUR STUFF HERE
      int node_id;
      Serial.print("PROGRAM: Data received from node-");
      // identify the node
      switch(packetBuffer[5]){
        
        case 1:
          // node 1
          node_id = 0;
          break;
        case 2:
          // node 2
          node_id = 1;
          break;
        case 3:
          // node 3
          node_id = 2;
          break;
        case 4:
          // node 4
          node_id = 3;
          break;
        default:
          node_id = 5;
          break;
      }
      Serial.println(node_id);

      // Extract the rssi value from the packetBuffer only
      for (int j = 6, int k = 0; packetBuffer[j]!='\0'; j++, k++){
        rssi[node_id][k] = packetBuffer[j];
      }
      delay(200);
    }
    delay(10);
    // Add an extra delay for the other node mcu's to transmit to maintain a periodic 
    // cycle among the four node mcu's
  }
}
