import RPi.GPIO as GPIO
import time

def compute_occupancy_rate(id, trashcan_height):
    if id == 1 : # Si papier/plastique/carton
        Trig = 20
        Echo = 21
    elif id == 2 : # Si verre
        Trig = 5
        Echo = 6
    elif id == 3 : # Si déchets
        Trig = 13
        Echo = 19
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Trig,GPIO.OUT)
    GPIO.setup(Echo,GPIO.IN)
    GPIO.output(Trig, False)
    
    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)
    
    while GPIO.input(Echo)==0:  ## Emission de l'ultrason
        debutImpulsion = time.time()

    while GPIO.input(Echo)==1:   ## Retour de l'Echo
        finImpulsion = time.time()

    distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
    
    GPIO.cleanup()
        
    return 100-(distance/trashcan_height*100)