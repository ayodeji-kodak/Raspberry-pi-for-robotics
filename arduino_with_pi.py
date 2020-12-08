import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

def led_on_off():
    user_input = input ("\n Type on / off / blink / quit :")
    user_input = str (user_input)
    if user_input == "on":
       print ("LED is on.....")
       time.sleep(0.1)
       ser.write(b'H')
       led_on_off()
    elif user_input == "off":
       print ("LED is off.....")
       time.sleep(0.1)
       ser.write(b'L')
       led_on_off()
    elif user_input == "blink":
       print ("LED is blinking.....")
       time.sleep(0.1)
       ser.write(b'B')
       led_on_off()
    elif user_input == "quit" or user_input == "q":
       print ("Program Exiting")
       time.sleep(0.1)
       ser.write(b'L')
       ser.close()
    else:
       print ("Invalid input. Type on / off / quit. ")
       led_on_off()

time.sleep(2)  # wait for serial connection to intialize

led_on_off()
