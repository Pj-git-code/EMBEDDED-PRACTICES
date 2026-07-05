// Arduino sketch: sends an incrementing counter and analog reading every second
int counter = 0;

void setup() {
  Serial.begin(9600);   // must match baud rate in Python
}

void loop() {
  int sensorValue = analogRead(A0);  // read a potentiometer or any analog sensor

  // Send as: counter,sensorValue
  Serial.print(counter);
  Serial.print(",");
  Serial.println(sensorValue);

  counter++;
  delay(1000);  // send once per second
}