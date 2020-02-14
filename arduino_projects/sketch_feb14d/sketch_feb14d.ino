unsigned long timing;
int a[100];
void setup(){
 Serial.begin(9600);
}

void loop(){
  if (Serial.available()){
      for(int i = 0; i < 2; ++i){
      a[i] = Serial.parseInt();
      }
  }
  analogWrite(a[0], a[1]);
  //if (millis() - timing > 1){ 
  //  timing = millis(); 
    Serial.write(digitalRead(3));
  //}0
}

