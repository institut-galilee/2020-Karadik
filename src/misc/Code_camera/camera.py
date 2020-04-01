import picamera
import time
import classify_original

camera = PiCamera()
camera.start_preview()
sleep(1)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
classify_original.analyse("/home/pi/Desktop/image.jpg")