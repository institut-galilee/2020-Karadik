const int ledPin = 3; // La LED est branchée sur le port 3

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT); // Assigne la LED en sortie
}

void loop() {
  if (Serial.available() > 1) { 
	// On a mis > 1 pour que la LED reste allumée à la même fréquence 
	// après chaque changement (sinon elle s'éteint)
    int frequency = Serial.parseInt();
    analogWrite(ledPin, frequency); // Change la fréquence de la LED avec celle entrée dans le Serial
    Serial.print("La fréquence de la LED a changé. Nouvelle valeur : ");
    Serial.println(frequency, DEC);
  }
}
