#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX

long int time = 0;
int interrupt_pin = 2;

void setup()
{
  Serial.begin(9600);
  pinMode(interrupt_pin, INPUT);
  //attachInterrupt(interrupt_pin, send_data, HIGH);
}

void loop()
{
  time = millis();
  //Serial.println(digitalRead(2));
  if(digitalRead(2) == 1) 
  {
    mySerial.write(time);
    Serial.println(time);
  }
}


