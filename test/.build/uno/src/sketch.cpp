#include <Arduino.h>

void setup();
void loop();
#line 1 "src/sketch.ino"

void setup()
{
	pinMode(6, OUTPUT);
}

void loop()
{
	digitalWrite(6, 1);
}
