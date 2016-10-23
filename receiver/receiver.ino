#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX

time = 0;
const byte interrupt_pin = 2;

void setup()
{
  pinMode(receiver,INPUT);
  Serial.begin(9600);
  pinMode(interruptPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(interrupt_pin), send_data, HIGH);
}

void loop()
{
  time = millis();
}


void send_data()
{	
	Serial.write(time);
}