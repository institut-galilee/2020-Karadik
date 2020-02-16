const int ledPin = 22;
const int potPin = 36;

void setup()
{
  ledcAttachPin(ledPin, 0);
  ledcSetup(0, 5000, 8);
  Serial.begin(9600);
}

void loop()
{
  int PWM = analogRead(potPin);
  PWM = map(PWM, 0, 1023, 0, 255); // Mapping reading to get values between 0 and 255
  ledcWrite(0, PWM);
  Serial.println(PWM);
}
