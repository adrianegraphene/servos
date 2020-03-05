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
        print("Starting from the top")
    
        #This for loop should create a granular movement effect that reflects a human movement on drop.
        for x in range(0, 170, 20):
            y = float(x) / 100
            p.ChangeDutyCycle(duty_cycle-y)
            print("current duty cycle is :")
            print(duty_cycle-y)
            time.sleep(0.1)

        #This for loop should create a granular movement effect that reflects a human movement on swipe.
        for x in range(0, 450, 25):
            y = float(x) / 100
            p2.ChangeDutyCycle(duty_cycle+y)
            print("current duty cycle is :")
            print(duty_cycle-y)
            time.sleep(0.10)

        time.sleep(1.00)
        #"Pick up" p2 using p as an arm (giving p2 clearance to hang up)
        p.ChangeDutyCycle(duty_cycle+0.5)
        time.sleep(0.5)
        
        #Position p2 over the hang up button
        p2.ChangeDutyCycle(duty_cycle-3)
        time.sleep(0.75)
        
        #here is when p ought to "lower" p2 onto the hangup button
        print("Dropping")
        p.ChangeDutyCycle(duty_cycle-3)
        time.sleep(0.25)
        
        #immediately raise p2 using p as an arm. This should complete the hangup motion
        print("picking up")
        p.ChangeDutyCycle(duty_cycle+1.5)
        time.sleep(0.1)
        p2.ChangeDutyCycle(duty_cycle)
        time.sleep(5)


except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()

