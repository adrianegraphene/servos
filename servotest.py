#https://www.electronicshub.org/raspberry-pi-servo-motor-interface-tutorial/
#https://reefwingrobotics.blogspot.com/2017/02/raspberry-pi-and-towerpro-sg90-micro.html

import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo2 = 22
servo1 = 18

GPIO.setmode(GPIO.BOARD)

duty_cycle = 7.5

GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)

p=GPIO.PWM(servo1,50)# 50hz frequency
p2=GPIO.PWM(servo2,50)# 50hz frequency

# Duty Cycle ranges from 3 to 13 for SG90s. DO NOT GO  BEYOND 3 or 13.
p.start(duty_cycle)# starting duty cycle ( it set the servo to 0 degree )
p2.start(duty_cycle)# starting duty cycle ( it set the servo to 0 degree )

try:
    while True:
        duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Right = 10):"))
        p.ChangeDutyCycle(duty_cycle)
#        p2.ChangeDutyCycle(duty_cycle)

except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()

