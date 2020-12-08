int echo = 10;
int trig = 9;
int distance;
long duration;
int LED = 12;
int IN3 = 7;
int IN4 = 6;

void setup(){

  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  pinMode(LED, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  
}

void loop(){

  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distance = duration * 0.034 / 2;
  //Serial.print("distance: ");
  Serial.println(distance);

  if (Serial.available() > 0 ){
    char data = Serial.read();
    if (data == 'H'){
    
      digitalWrite(LED, HIGH);
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
      
    }
    else if (data == 'L'){
    
      digitalWrite(LED, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
    
    }
  }
  
  else{
  }
  
  


}
void halt(){
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  
 
}
