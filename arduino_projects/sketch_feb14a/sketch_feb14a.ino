

int a[100];
void setup(){
 Serial.begin(9600);
}

void loop(){
  if (Serial.available()){
    for(int i = 0, k = 0;1;){
      if(Serial.available()){
        k = Serial.parseInt();
        if(k == 1000){
          break;
        }
        a[i] = k;
        i++;
        
      }
    }
  }
  analogWrite(a[0], a[1]);
  Serial.write(digitalRead(3));
}
