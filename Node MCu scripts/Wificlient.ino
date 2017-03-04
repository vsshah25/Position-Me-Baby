#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

WiFiUDP UDP;

const char *ssid = "TP LINK Wifi";
const char *password = "devsak49";

const uint16_t UDP_LOCAL_PORT =  8050;
const uint16_t UDP_REMOTE_PORT = 8051;        // Must match UDP_REMOTE_PORT on receiver
const char UDP_REMOTE_HOST[] =   "192.168.0.124";

char TRIGGER_STRING[] = "node_1";           // Must match TRIGGER_STRING on receiver

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
  String rssi = String(WiFi.RSSI());
  //int rssi = WiFi.RSSI();
  char TRIGGER_STRING[3];
  for(int i = 0; i!=3; i++){
    TRIGGER_STRING[i] = rssi[i];
  }
  //Serial.println(String(TRIGGER_STRING));
  // put your main code here, to run repeatedly:
  //char rssi[] = "Saqib";

  pinMode(2, LOW);
  delay(1000);
  Serial.println("PROGRAM: sending rssi data");
  UDP.beginPacket(UDP_REMOTE_HOST, UDP_REMOTE_PORT);
  UDP.write(TRIGGER_STRING);

  UDP.endPacket();

  pinMode(2, HIGH);
  delay(1000);

}
