#include <VarSpeedServo.h>

VarSpeedServo motorA;
VarSpeedServo motorB;
int boton2A = 8;
int boton2D = 9;
int boton2E = 10;
int boton2H = 11;
int botonI0 = 12;
int valor;
void setup () {
   motorA.attach(2);
   motorB.attach(3);
   pinMode(boton2A,INPUT);
   pinMode(boton2D,INPUT);
   pinMode(boton2H,INPUT);
   pinMode(boton2E,INPUT);
   pinMode(botonI0,INPUT);
   Serial.begin(9600);
}

void loop () {

   if (Serial.available()) {
      char c = Serial.read();
        if (c == 'i') {
         valor = digitalRead(botonI0);
         if(valor == 0){
            Serial.println(0);
         }else{
            Serial.println(1);
         }
      }
      if (c == 'a') {
         valor = digitalRead(boton2A);
         if(valor == 0){
            Serial.println(0);
         }else{
            Serial.println(1);
         }
      }
       if (c == 'd') {
         valor = digitalRead(boton2D);
         if(valor == 0){
            Serial.println(0);
         }else{
            Serial.println(1);
         }
      }
      if (c == 'h') {
         valor = digitalRead(boton2H);
         if(valor == 0){
            Serial.println(0);
         }else{
            Serial.println(1);
         }
      }
      if (c == 'e') {
         valor = digitalRead(boton2E);
         if(valor == 0){
            Serial.println(0);
         }else{
            Serial.println(1);
         }
      }
      if (c == 'w') {
         motorA.write(90);
         Serial.println(0);
         motorA.stop();
      }
      if(c == 'x'){
         motorB.write(90);
         Serial.println(0);
         motorB.stop();
      }
       if (c == 'y') {
         motorA.write(0);
         Serial.println(1);
          motorA.stop();
      }
      if(c == 'z'){
         motorB.write(180);
         Serial.println(1);
         motorB.stop();
      }
   }
}