#include <SoftwareSerial.h>
#include <String>
#define RX 10
#define TX 11

SoftwareSerial XBee(RX,TX);
string data_array[4];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  XBee.begin(9600);
}

void loop() {

  if(XBee.available() > 0){
    string str = "";
    int count=0;
    while(XBee.available() > 0){
        readData = (char)XBee.read();
        str += readData;
    }
    str += '\0';
    for(int i = 0;str[i]!='\0';i++){
      if(str[i]=='@'){    //special symbol to segregate
        //data_array[count++]=str[]
        // will add the four individual data to data_array in future commits.
        //Don't play around with it.
      }
    }
    Serial.write(data_array);
  }
}