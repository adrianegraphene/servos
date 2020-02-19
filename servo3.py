#https://www.electronicshub.org/raspberry-pi-servo-motor-interface-tutorial/

import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo1 = 22
servo2 = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)
# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

p=GPIO.PWM(servo1,50)# 50hz frequency
p2=GPIO.PWM(servo2,50)# 50hz frequency

p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )
p2.start(2.5)# starting duty cycle ( it set the servo to 0 degree )

try:
       while True:
           for x in range(100):
             p.ChangeDutyCycle(control[x])
             p2.ChangeDutyCycle(control[x])
             time.sleep(0.5) 
             print x

           for x in range(9,0,-1):
             p.ChangeDutyCycle(control[x])
             p2.ChangeDutyCycle(control[x])
             time.sleep(1)
             print x

except KeyboardInterrupt:
    GPIO.cleanup()
