#include <SoftwareSerial.h>

long int time = 0;
int readings[10];
int sum = 0;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  while(1)
  {
    if(Serial.available()>0)
    {
    char c = Serial.read();
    if(c == 'c') 
    {
      in_time = millis()
      break;
    }
    }
    
  }
  
  
  for(int i=0;i<10;i++)
  {
  readings[i] = digitalRead(2);
  }
  if(readings[0]==1 &&readings[1]==1 && readings[2]==1 &&readings[3]==1 &&readings[4]==1 &&readings[5]==1 &&readings[6]==1 &&readings[7]==1 &&readings[8]==1 &&readings[9]==1 )
  {
  time = millis() - in_time;
  Serial.print(time);
  Serial.print("a");
  
  }
 delay(10);
  
 
}
