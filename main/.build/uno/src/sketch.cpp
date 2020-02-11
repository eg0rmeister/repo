#include <Arduino.h>

void setup();
void loop();
#line 1 "src/sketch.ino"
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
char s[200];
int k = 0;
int v;
bool b;
char vrem;

void loop() {
  int fin[100];
  // put your main code here, to run repeatedly:
  for(int i = 0; i < 200; ++i){
    s[i] = '0';
  }
  b = 0;
  vrem = NULL;
  k = 0;
  for(int i = 0; Serial.available() > 0; ++i){
    if (Serial.available()){
      vrem = Serial.read();
    }
    //Serial.print(vrem);
    if (vrem != ';'){
      s[i] = vrem;
      k = i + 1;
      //Serial.write(vrem);
      b = 1;
    }
    else{
      //Serial.println();
      //Serial.println(k);
      k = i;
      break;
    }
    delay(1);
  }
  
  //k = 200;
  v = 0;


  
  if (b){
    //Serial.print(0);
    //Serial.println(5);
    for(int i = 0; i < 100; ++i){
      fin[i] = 0;
    }

    
    for(int i = 0; i < k; ++i){
      //Serial.println(s[i]);
      if ((int)s[i] == 46){
        ++v;
        //Serial.println(8);
        //Serial.println(fin[v-1]);
        continue;
      }
      else{
        fin[v] = fin[v] * 10 + s[i] - '0';
        //Serial.println(fin[v]);
      }
    }
    analogWrite(fin[0], fin[1]);
    b = 0;
  }
  Serial.write(':');
  Serial.write(analogRead(0)/4);
  Serial.write('.');
  Serial.write(analogRead(1)/4);
  Serial.write(';');
}
