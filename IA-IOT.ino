int ledIndicadorPin = 10;
int ledSextantePin = 9;
int motorPin = 8;

void setup() {
  pinMode(ledIndicadorPin, OUTPUT);
  pinMode(ledSextantePin, OUTPUT);
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    if (data == '1') {
      digitalWrite(ledIndicadorPin, HIGH);
      digitalWrite(ledSextantePin, LOW);
      digitalWrite(motorPin, LOW);
    } else if (data == '6') {
      digitalWrite(ledIndicadorPin, LOW);
      digitalWrite(ledSextantePin, HIGH);
      digitalWrite(motorPin, LOW);
    } else if (data == '0') {
      digitalWrite(ledIndicadorPin, LOW);
      digitalWrite(ledSextantePin, LOW);
      digitalWrite(motorPin, HIGH);
    } else {
      digitalWrite(ledIndicadorPin, LOW);
      digitalWrite(ledSextantePin, LOW);
      digitalWrite(motorPin, LOW);
    }
  }
}
