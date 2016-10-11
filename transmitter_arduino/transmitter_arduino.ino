

//Continously run the transmitters

int trans_1_1 = 2;
int trans_1_2 = 3;

int trans_2_1 = 4;
int trans_2_2 = 5;

int trans_3_1 = 6;
int trans_3_2 = 7;

int trans_4_1 = 8;
int trans_4_2 = 9;

time = 0;
freq = 0;
pulse_width = 0;
time_diff = 0;
void setup()
{
   pinMode(2,OUTPUT);
   pinMode(3,OUTPUT);
   pinMode(4,OUTPUT);
   pinMode(5,OUTPUT);
   Serial.begin(9600);
}

void loop()
{
    time = millis();
    //use interrupt o continuously check the value of time;
    send_signal(trans_1_1,trans_1_2);
    delay(time_diff);
    
    send_signal(trans_1_1,trans_1_2);
    delay(time_diff);
    
    send_signal(trans_1_1,trans_1_2);
    delay(time_diff);
    
    send_signal(trans_1_1,trans_1_2);
    delay(time_diff);
    
    
  
}


void send_signal(pin1, pin2 )
{  
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,LOW);
  delay(freq);
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,HIGH);
  delay(freq);
}
