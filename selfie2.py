from picamera import PiCamera
from gpiozero import Button
from time import sleep
import os

button0 = Button(4, pull_up = False)
button1 = Button(5, pull_up = False)
i = 0

while button1.is_pressed == False:
    with PiCamera() as camera:
        camera.start_preview()
        sleep(5)
        if button0.is_pressed:
            while os.path.exists("/home/pi/selfie/selfie%s.jpg" % i):
                i += 1
            camera.capture('/home/pi/selfie/selfie%s.jpg' % i)
        if button1.is_pressed:
            camera.stop_preview()
   
