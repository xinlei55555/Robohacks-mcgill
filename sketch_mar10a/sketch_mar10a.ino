#include <stdio.h>
int input;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Serial.print("hi");
  int n=5;
  int arr[n]; 
  for(int i=0;i<n;i++){
    if(Serial.available()){
      input = Serial.read();
      Serial.println(input);
    }
  }
}
