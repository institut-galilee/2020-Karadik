import RPi.GPIO as GPIO
import time
import camera
#initialisation des ports
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN)

#Detection d'un bouton 
#Quand on appuit sur le bouton on prend une photo

while True :
    valeur = GPIO.input(19)
    if not valeur :
        #prendre une photo et l'analyser
        camera.captureImageAnalyse()
        while not valeur :
            valeur = GPIO.input(19)
            time.sleep(0.02)
    time.sleep(0.02)
