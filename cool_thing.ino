void setup(){
  Serial.begin(9600);
}
int i;
char a[100];
void loop(){
   if(Serial.available()){
    //a = Serial.read();
    i = Serial.parseInt();
    Serial.println(a);
  }
}
