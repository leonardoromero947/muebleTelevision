int boton2A = 8;
int boton2D = 9;
int boton2E = 10;
int boton2H = 11;
int valor;
void setup () {
   pinMode(boton2A,INPUT);
   pinMode(boton2D,INPUT);
   pinMode(boton2H,INPUT);
   pinMode(boton2E,INPUT);
   Serial.begin(9600);
}

void loop () {
   if (Serial.available()) {
      char c = Serial.read();
      if (c == 'a') {
         valor = digitalRead(boton2A);
         if(valor == 0){
            Serial.println(1);
         }else{
            Serial.println(0);
         }
      }
       if (c == 'd') {
         valor = digitalRead(boton2D);
         if(valor == 0){
            Serial.println(1);
         }else{
            Serial.println(0);
         }
      }
      if (c == 'h') {
         valor = digitalRead(boton2H);
         if(valor == 0){
            Serial.println(1);
         }else{
            Serial.println(0);
         }
      }
      if (c == 'e') {
         valor = digitalRead(boton2E);
         if(valor == 0){
            Serial.println(1);
         }else{
            Serial.println(0);
         }
      }
   }
}