void setup() {
 // put your setup code here, to run once:
 pinMode(4, OUTPUT);
 pinMode(5, OUTPUT);
 pinMode(6, OUTPUT);
 pinMode(7, OUTPUT);
 pinMode(1, INPUT);
 pinMode(0, INPUT);
 Serial.begin(9600);
}
int inp[2];
char c[10];
void loop() {
 if (Serial.available())
 {	
  inp[0] = Serial.parseInt();
  inp[1] = Serial.parseInt();
  analogWrite(inp[0], inp[1]);
 }
 itoa(analogRead(2), c, 10);
 Serial.write("2 ");
 Serial.write(c);
 Serial.write("\n");
 itoa(analogRead(3), c, 10);
 Serial.write("3 ");
 Serial.write(c);
 Serial.write("\n");
}
