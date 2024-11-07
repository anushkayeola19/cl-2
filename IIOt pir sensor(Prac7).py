int pirPin = 2;      // PIR sensor output pin
int ledPin = 13;     // LED pin (optional)

void setup() {
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int motionState = digitalRead(pirPin);
 
  if (motionState == HIGH) {
    Serial.println("Motion detected!");
    digitalWrite(ledPin, HIGH);  // Turn on LED
  } else {
        Serial.println("No Motion detected!");

    digitalWrite(ledPin, LOW);   // Turn off LED
  }
 
  delay(100); // Small delay to avoid flooding serial output
}