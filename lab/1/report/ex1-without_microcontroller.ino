int LED = 13;

void setup()
{
  pinMode(LED, OUTPUT);
}

void loop()
{
  int reading = analogRead(A0);
  reading = map(reading, 0, 1023, 0, 255); // Mapping reading to get values between 0 and 255
  analogWrite(LED, reading);
}
