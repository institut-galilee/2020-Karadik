import picamera
import classify_original as co
import servo

def captureImageAnalyse():
    camera = picamera.PiCamera()
    camera.start_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    camera.close()
    dict = co.analyse("/home/pi/Desktop/image.jpg")
    max_key = co.getMaxKey(dict)
    max_val = dict[max_key]*100
        
    if max_key in ['paper','cardboard','plastic']:
        servo.open_can(1)
    elif max_key == 'glass':
        servo.open_can(2)
    elif max_key == 'trash':
        servo.open_can(3)
    else:
        return 'Dechet trop volumineux ou poubelle pleine'

    return "Le dechet jete est detecte comme etant de categorie " + str(max_key) + " a une probabilite de " + "{:.2f}".format(max_val) + "%."