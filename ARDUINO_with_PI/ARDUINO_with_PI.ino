
int LED_pin = 12;

void setup() {

  Serial.begin(9600);

  pinMode(LED_pin, OUTPUT);

}



void loop() {

  if(Serial.available() > 0){

    char data = Serial.read();

    if (data == 'H'){

      digitalWrite(LED_pin, HIGH);

    }

    else if (data == 'L') {

      digitalWrite(LED_pin , LOW);


    }
    
    else if (data == 'B') {
       for(int i =0; i < 20; i++){
       digitalWrite(LED_pin, HIGH);
       delay (1000);
       digitalWrite(LED_pin, LOW);
       delay (1000);
       }
    }
    
    else {
    }



  }



}


