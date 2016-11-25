//Continously run the transmitters

int trans_1_push = 2;
int trans_1_pull = 3;

int trans_2_push = 4;
int trans_2_pull = 5;

int trans_3_push = 6;
int trans_3_pull = 7;

int trans_4_push = 8;
int trans_4_pull = 9;

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
    Serial.print('a');                                 //special char
    send_signal(trans_1_push,trans_1_pull);

    delay(time_diff);
    
    time = millis();
    Serial.print(time);
    Serial.print('a');                                 //special char
    send_signal(trans_2_push,trans_2_pull);

    delay(time_diff);
    
    time = millis();
    Serial.print(time);
    Serial.print('a');                                 //special char
    send_signal(trans_3_push,trans_3_pull);

    delay(time_diff);
    
    time = millis();
    Serial.print(time);
    Serial.print('a');                                 //special char
    send_signal(trans_4_push,trans_4_pull);

    delay(time_diff);
    
    

    
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
