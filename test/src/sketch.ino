
void setup()
{
	pinMode(4, OUTPUT);
	pinMode(5, OUTPUT);
	pinMode(6, OUTPUT);
	pinMode(6, OUTPUT);
	pinMode(0, INPUT);
	pinMode(1, INPUT);
}
int i;
void loop()
{
	if(Serial.available()){
		i = Serial.parseInt();
		Serial.println(i);
	}
}
