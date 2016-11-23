//Continously run the transmitters

int trans_1_t = 2;
int trans_1_r = 3;

int trans_2_t = 4;
int trans_2_r = 5;

int trans_3_t = 6;
int trans_3_r = 7;

int trans_4_t = 8;
int trans_4_r = 9;

float time = 0;
float freq = 40000;      //in Hz
float pulse_width = 0;
float time_diff = 20;

void setup()
{
   pinMode(2,OUTPUT);
   pinMode(3,OUTPUT);
   pinMode(4,OUTPUT);
   pinMode(5,OUTPUT);
   Serial.begin(9600);
   Serial.write("c");
 }

void loop()
{
    
    time = millis();
    Serial.print(time);
    Serial.print('a');
    send_signal(trans_1_t,trans_1_r);
    //time_1 =  millis();
    delay(time_diff);
    
    
     
    /*
    send_signal(trans_1_t,trans_1_r);
    delay(time_diff);
    
    send_signal(trans_1_t,trans_1_r);
    delay(time_diff);
    
    send_signal(trans_1_t,trans_1_r);
    delay(time_diff);  
    */
    
}

void send_signal(int pin1, int pin2)
{  
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,LOW);
  delay(1000/freq);
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,HIGH);
  delay(1000/freq);
}
