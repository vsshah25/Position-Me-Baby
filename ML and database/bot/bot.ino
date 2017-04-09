int motor1_f = 3;
int motor1_b = 5;
int motor2_f = 9;
int motor2_b = 10;

int iterations = 100;

void setup()
{
	pinMode(motor1_f,OUTPUT);
	pinMode(motor1_b,OUTPUT);
	pinMode(motor2_f,OUTPUT);
	pinMode(motor2_b,OUTPUT);			
}

void loop()
{
	for(int i=0;i<iterations;i++){
		int PWM = 50;
		int Time = 200;
		move_forward(PWM,Time);
		delay(1000);
	}
	
 	int PWM = 50;
	int Time = 200;
	int rotation_time = 100;

	rotate_90(rotation_time);
	move_forward(PWM,Time);
	rotate_90(rotation_time);	

}


void move_forward(int PWM, int Time){

	analogWrite(motor1_f,PWM);
	analogWrite(motor2_f,PWM);
	digitalWrite(motor1_b,0);
	digitalWrite(motor2_b,0);
	delay(Time);
	digitalWrite(motor1_f,0);
	digitalWrite(motor1_b,0);
	digitalWrite(motor2_f,0);
	digitalWrite(motor2_b,0);

}

void rotate_90(int Time){

	digitalWrite(motor1_f,1);
	digitalWrite(motor1_b,0);
	digitalWrite(motor2_f,0);
	digitalWrite(motor2_b,1);	
	delay(Time);
	digitalWrite(motor1_f,0);
	digitalWrite(motor1_b,0);
	digitalWrite(motor2_f,0);
	digitalWrite(motor2_b,0);

}

