int LED = 3;

void setup()
{
  pinMode(LED, OUTPUT);
}

void loop()
{
  int PWM = analogRead(A0);
  PWM = map(PWM, 0, 1023, 0, 255); // Mapping reading to get values between 0 and 255
  analogWrite(LED, PWM);
}
