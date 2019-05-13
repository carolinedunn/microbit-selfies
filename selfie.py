from picamera import PiCamera
from gpiozero import Button
from time import sleep
import os

button = Button(4, pull_up = False)
button1 = Button(5, pull_up = False)
i = 0

#new_index = len(os.listdir('/home/pi/selfie'))
#new_file = open('/home/pi/selfie/selfie%s.jpg' % new_index, 'w')


with PiCamera() as camera:
    camera.start_preview()
    sleep(5)
    button.wait_for_press()   
    while os.path.exists("selfie%s.jpg" % i):
        i += 1
    camera.capture('/home/pi/selfie%s.jpg' % i)
    i += 1
    
    button1.wait_for_press()
    camera.stop_preview()
