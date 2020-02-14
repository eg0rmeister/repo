int a = 0;
void setup(){
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop(){
  if(Serial.available() > 0){
    digitalWrite(13, HIGH);
  }
  else{
   digitalWrite(13, LOW);
  } 
  a = a + 1;
  Serial.write(a);
  delay(1000);
}
