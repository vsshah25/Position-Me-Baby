#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

WiFiUDP UDP;

#define UDP_TX_PACKET_MAX_SIZE 6

const char *ssid = "lps";

const char *password = "positionme";

const uint16_t UDP_LOCAL_PORT =  8051;

char TRIGGER_STRING1[] = "0_";      // replace 1 with the node_id of client node
char TRIGGER_STRING2[] = "1_";
char TRIGGER_STRING3[] = "2_";
char TRIGGER_STRING4[] = "3_";
char rssi[5][10];   // decide the postion of this rssi matrix declaration
                                                   
//WiFiServer server(80);


void setup() {
  // put your setup code here, to run once:

  pinMode(2, OUTPUT);
  Serial.begin(115200);
  delay(10);

  //Serial.println();
  //Serial.println();
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

  // Start the server. Right now I don't think we will need a server.
  //server.begin();
  //Serial.println("Server started");


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
  label:
  char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; // buffer(array) to hold incoming packet,
  int packetSize = UDP.parsePacket();
  int node_id;

  // the server checks whether there is any packet in its buffer
  if (packetSize > 0)
  {
    //Serial.print("PROGRAM: received UDP packet of size ");
    //Serial.println(packetSize);
    //Serial.print("PROGRAM: from ");
    IPAddress remote = UDP.remoteIP();        // extracts the remote IP of the client
    /*
    for (int i = 0; i < 4; i++)
    {
      //Serial.print(remote[i], DEC);
      if (i < 3)
      {
        Serial.print(".");
      }
    }*/
    //Serial.print(", port ");
    //Serial.println(UDP.remotePort());
    UDP.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);   // extract the data from the packet
    packetBuffer[packetSize] = '\0';
    //Serial.print("PROGRAM: contents: ");
    //Serial.println(packetBuffer);
    Serial.print('(');
      Serial.print(packetBuffer[0]);
      Serial.print(',');
      int count = 0;
      for(int i=2;packetBuffer[i]!='\0';i++){
        count++;
      }
      Serial.print(packetBuffer[2]);   // print -ve symbol
      if(count == 3){
        Serial.print('0');
      }
      for(int i=3; packetBuffer[i]!='\0';i++){
        Serial.print(packetBuffer[i]);
      }
      
      Serial.println(')');

    // code for synthesizing packet to send

    int char_to_cmp = 2;
    // compares the first two elements of packet to be i_
    if (strncmp(packetBuffer, TRIGGER_STRING1, char_to_cmp) == 0 || 
        strncmp(packetBuffer, TRIGGER_STRING2, char_to_cmp) == 0 ||
        strncmp(packetBuffer, TRIGGER_STRING3, char_to_cmp) == 0 ||
        strncmp(packetBuffer, TRIGGER_STRING4, char_to_cmp) == 0)
    {
      // Serial.println("PROGRAM: trigger received"); 
      //Serial.print("PROGRAM: Data received from node-");
      
      // identify the node
      switch(packetBuffer[0]){
        case 0:
          // node 1
          node_id = 0;
          break;
        case 1:
          // node 2
          node_id = 1;
          break;
        case 2:
          // node 3
          node_id = 2;
          break;
        case 3:
          // node 4
          node_id = 3;
          break;
        default:     // for random data
          node_id = 4;
          break;
      }
      if (node_id == 4){
        goto label;
      }
      Serial.print('(');
      Serial.print(node_id);
      Serial.print(',');
      Serial.print(packetBuffer[3]);
      Serial.print(packetBuffer[4]);
      Serial.println(')');
      int k;
      // Extract the rssi value from the packetBuffer
      for (int j = 6, k = 0; packetBuffer[j]!='\0'; j++, k++){
        rssi[node_id][k] = packetBuffer[j];
      }
      //Serial.println(rssi);
      delay(20);   // Add an extra delay for the other node mcu's to transmit to
                    // maintain a periodic cycle among the four node mcu's
    }
    delay(10);
  }
}
