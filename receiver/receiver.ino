#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX

int receiver = 13;
time = 0;

void setup()
{
  pinMode(receiver,INPUT);
  Serial.begin();
}

void loop()
{
  if( digitalRead(receiver) == 0 )
  {
     time = millis();
     mySerial.println(time);
  }
  
}
