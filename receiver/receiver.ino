#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX

long int time = 0;
int readings[10];
int sum = 0;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  
  for(int i=0;i<10;i++)
  {
  readings[i] = digitalRead(2);
  //Serial.print(i);
  //Serial.print("  ");
  //Serial.println(readings[i]);
  }
  if(readings[0]==1 &&readings[1]==1 && readings[2]==1 &&readings[3]==1 &&readings[4]==1 &&readings[5]==1 &&readings[6]==1 &&readings[7]==1 &&readings[8]==1 &&readings[9]==1 )
  {
  time = millis();
  //Serial.print("time");

  Serial.print(time);
  Serial.print("@");
  
  }
 delay(10);
  
 
}
