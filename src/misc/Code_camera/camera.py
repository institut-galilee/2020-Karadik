import picamera
import time
import classify_original

def captureImageAnalyse():
    camera = PiCamera()
    camera.start_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    classify_original.analyse("/home/pi/Desktop/image.jpg")