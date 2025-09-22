int buttonState1 = 0;
int buttonState2 = 0;
const int butt1 = 29;
const int butt2 = 28;
int count = 0;
const int led1 = 6;
const int led2 = 7;
const int led3 = 8;
const int led4 = 9;
const int led5 = 10;
const int led6 = 11;
const int led7 = 12;
const int led8 = 13;
int ledArray[] = {led1, led2, led3, led4, led5, led6, led7, led8};

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led1, OUTPUT);
pinMode(led2, OUTPUT);
pinMode(led3, OUTPUT);
pinMode(led4, OUTPUT);
pinMode(led5, OUTPUT);
pinMode(led6, OUTPUT);
pinMode(led7, OUTPUT);
pinMode(led8, OUTPUT);
pinMode(butt1,INPUT_PULLUP);
pinMode(butt2,INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
buttonState1 = digitalRead(butt1);
buttonState2 = digitalRead(butt2);
// Serial.print("Butt State: ");
// Serial.println(buttonState1);


if (buttonState1 == 0){
  delay(500);
//   while(buttonState1 == LOW) {
// }
  Serial.print("Count: ");
  Serial.println(count);        
  digitalWrite(ledArray[count], HIGH);
  count++;
}
  if (count > 8){
    for (int i=0; i<=7; i++) {
      digitalWrite(ledArray[i],LOW);
    }
    count = 0;
  }
    // } else {
    // // turn LED off:
    // digitalWrite(ledArray[count], LOW);
    // }
if (buttonState2 == 0){
    for (int i=0; i<=7; i++) {
      digitalWrite(ledArray[i],LOW);
    }
    count = 0;
}
}

