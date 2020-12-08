
import  RPi.GPIO as GPIO
import time

motor_a = 2
motor_b = 3
motor_c = 17
motor_d = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_a, GPIO.OUT)
GPIO.setup(motor_b, GPIO.OUT)
GPIO.setup(motor_c, GPIO.OUT)
GPIO.setup(motor_d, GPIO.OUT)


while True:
    user_control = input("enter 1 to start and 0 to stop" + "\n"+": ")
    if user_control == 1:
	GPIO.output(motor_a, True)
        GPIO.output(motor_b, False)
        GPIO.output(motor_c, True)
        GPIO.output(motor_d, False)


    elif user_control == 0: 
        GPIO.output(motor_a, False)
        GPIO.output(motor_b, False)
        GPIO.output(motor_c, False)
        GPIO.output(motor_d, False)



