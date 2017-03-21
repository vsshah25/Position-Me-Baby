#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

WiFiUDP UDP;

const char *ssid = "Tinkerers' Lab";
//const char ldap_id = "150070031";
const char *password = "tinker@tl";

const uint16_t UDP_LOCAL_PORT =  8050;
const uint16_t UDP_REMOTE_PORT = 8051;        // Must match UDP_REMOTE_PORT on receiver

const char UDP_REMOTE_HOST[] = "192.168.0.128";  // ip address of the server(receiver)
                                                // has to be put here
char TRIGGER_STRING[] = "2_";           // Must match TRIGGER_STRING on receiver

void setup() {
  // put your setup code here, to run once:

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

// Suppose this is for node_i

void loop() {
  // put your main code here, to run repeatedly:

  char packet_to_send[15] = "2_";
  long rssi = WiFi.RSSI();

  String rssi_string = String(rssi);
  int i;
  for(i = 2; i<2+rssi_string.length();i++){
    packet_to_send[i] = rssi_string[i-2];
  }
  packet_to_send[i] = '\0';     // put the last character of the packet as null character

  pinMode(2, LOW);
  delay(1000);
  Serial.println("PROGRAM: sending rssi data");
  
  UDP.beginPacket(UDP_REMOTE_HOST, UDP_REMOTE_PORT);
  UDP.write(packet_to_send);
  UDP.endPacket();

  pinMode(2, HIGH);   // when the data is completely sent light on an led(2) for 1 sec
  delay(50);    // wait after sending, for all the four nodes to send data(cyclic order)
}
