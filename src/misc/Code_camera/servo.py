#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent
    
def activate_servo (pwm_gpio) :
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(False) #Disable warnings

    frequence = 50
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    
    #Init at 0°
    pwm.start(angle_to_percent(0))
    time.sleep(1)

    #Go at 90°
    pwm.ChangeDutyCycle(angle_to_percent(90))
    time.sleep(5)

    #Finish at 0°
    pwm.ChangeDutyCycle(angle_to_percent(0))
    time.sleep(1)

    #Close GPIO & cleanup
    pwm.stop()
    GPIO.cleanup()

def open_can (id) :
    if id == 1 : #Si papier/plastique/carton
        pwm_gpio = 16
        activate_servo(pwm_gpio)
    elif id == 2 : #Si verre
        pwm_gpio = 12
        activate_servo(pwm_gpio)
    elif id == 3 : #Si déchets ménagers
        pwm_gpio = 22
        activate_servo(pwm_gpio)
    #Sinon trop volumineux ou bac plein
        # Renvoyer un msg à l'utilisateur
