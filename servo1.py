#From https://bitbucket.org/MattHawkinsUK/rpispy-misc/src/master/python/servo1.pyrm
#Use CTRL-C to break out of While loopo
#https://www.raspberrypi-spy.co.uk/tag/servo/

from gpiozero import Servo
from time import sleep

myGPIO=18

myServo = Servo(myGPIO)

print("Using GPIO18")
print("Using Gpiozero defaults for the servo class")

while True:
    myServo.mid()
    print("Set to middle pos.")
    sleep(1)
    myServo.min()
    print("set to min pos.")
    sleep(1)
    myServo.mid()
    print("Set to mid. pos.")
    sleep(1)
    myServo.max()
    print("Set to max. pos.")
    sleep(1)
