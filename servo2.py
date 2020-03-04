#https://www.electronicshub.org/raspberry-pi-servo-motor-interface-tutorial/
#https://reefwingrobotics.blogspot.com/2017/02/raspberry-pi-and-towerpro-sg90-micro.html

import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo1 = 22
servo2 = 18

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
        #duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Right = 10):"))
        p.ChangeDutyCycle(duty_cycle)
        p2.ChangeDutyCycle(duty_cycle)
        p.ChangeDutyCycle(duty_cycle-3.5)
        time.sleep(0.5)
    
        #This for loop should create a granular movement effect that reflects a human movement.
        for x in range(0,2.5,0.25):
            p2.ChangeDutyCycle(duty_cycle-x)
            time.sleep(0.1)
        time.sleep(0.75)
        #"Pick up" p2 using p as an arm (giving p2 clearance to hang up)
        p.ChangeDutyCycle(duty_cycle-2.5)
        time.sleep(0.25)
        #Position p2 over the hang up button
        p2.ChangeDutyCycle(duty_cycle-2)
        time.sleep(0.3)
        #here is when p ought to "lower" p2 onto the hangup button
        #Note. using 3.5 as a template here. Need to get actual nubmers down later.
        #"Lower" ps using p as an arm
        p.ChangeDutyCycle(duty_cycle-3.5)
        #immediately raise p2 using p as an arm. This should complete the hangup motion
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.25)
        #bring P2 back to start.
        p2.ChangeDutyCycle(duty_cycle)


# try:
#        while True:
#            for x in range(11):
#              p.ChangeDutyCycle(control[x])
#              p2.ChangeDutyCycle(control[x])
#              time.sleep(0.2) 
#              print x

#            for x in range(9,0,-1):
#              p.ChangeDutyCycle(control[x])
#              p2.ChangeDutyCycle(control[x])
#              time.sleep(0.1)
#              print x

except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
