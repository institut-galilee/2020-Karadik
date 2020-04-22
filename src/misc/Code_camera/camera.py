import picamera
import classify_original

def captureImageAnalyse():
    camera = picamera.PiCamera()
    camera.start_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    value = classify_original.analyse("/home/pi/Desktop/image.jpg")
    return value
    #for cle, valeur  in value.items():
     #   print('%s (valeur = %.5f)' % (cle, valeur))
        