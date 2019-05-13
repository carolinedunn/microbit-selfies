# Write your code here :-)
from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll("3 2 1")
        sleep(500)
        pin1.write_digital(1)
    	sleep(3000)
    	pin1.write_digital(0)
    if button_b.is_pressed():
        display.scroll('exit')
        sleep(500)
        pin2.write_digital(1)
    	sleep(5000)
    	pin2.write_digital(0)