'''Copyright (C) jumejume1
All rights reserved
https://github.com/jumejume1/raspberry-tb6560'''

from time import sleep
import RPi.GPIO as gpio
import threading
from time import sleep
motor_setup = {'X': [19,26],'Y':[20,21],'Z':[13,6]} # [DIR,STEP]
CW = 1
CCW = 0
stop_running = False

gpio.setmode(gpio.BCM)
for i in motor_setup:
    gpio.setup(motor_setup[i][0], gpio.OUT)
    gpio.setup(motor_setup[i][1], gpio.OUT)
    gpio.output(motor_setup[i][0],CW)
def Hello(motor_axis,duration):
    global stop_running
    print(f"motor {motor_axis} is running")
    for i in range(duration):
        if stop_running:
            break
    if not stop_running:
        print(f"{duration} DONEEEE")
    
def move(motor_axis,duration,direction):
    gpio.output(motor_setup[motor_axis][0],direction)
    global stop_running
    for x in range(duration):
        if stop_running:
            break
        gpio.output(motor_setup[motor_axis][1],gpio.HIGH)
        sleep(0.001)
        gpio.output(motor_setup[motor_axis][1],gpio.LOW)
        sleep(0.001)
    print("DONE")

# Main body of code
def go_to_locker(n):
    global stop_running
    try :
        if n == 1 :
            print('prepare position')
            #move('X',3600)
            motor_threading1 = threading.Thread(target=move,args=('X',1000,CCW)) #1000
            motor_threading2 = threading.Thread(target=move,args=('Y',1675,CW)) #1675
            motor_threading1.start()
            motor_threading2.start()
            motor_threading1.join()
            motor_threading2.join()
        elif n == 2 :
            motor_threading1 = threading.Thread(target=move,args=('Y',1450,CW)) #1000
            #motor_threading2 = threading.Thread(target=move,args=('z',1675,CW)) #1675
            motor_threading1.start()
            #motor_threading2.start()
            motor_threading1.join()
            print("reach locker bot_left")
        elif n == 3:
            motor_threading1 = threading.Thread(target=move,args=('Y',1400,CCW)) #1000
            #motor_threading2 = threading.Thread(target=move,args=('z',1675,CW)) #1675
            motor_threading1.start()
            #motor_threading2.start()
            motor_threading1.join()
            print("reach locker bot_right")
        elif n == 4 :
            motor_threading1 = threading.Thread(target=move,args=('Y',1450,CW)) #1000
            motor_threading2 = threading.Thread(target=move,args=('Z',2050,CW)) #1675
            motor_threading1.start()
            motor_threading2.start()
            motor_threading1.join()
            motor_threading2.join()
            print("reach locker top_left")
        elif n == 5 :
            motor_threading1 = threading.Thread(target=move,args=('Y',1450,CCW)) #1000
            motor_threading2 = threading.Thread(target=move,args=('Z',2050,CW)) #1675
            motor_threading1.start()
            motor_threading2.start()
            motor_threading1.join()
            motor_threading2.join()
            print("reach locker top_left")
        else :
            print('motor is running or unavalable')
    except KeyboardInterrupt:
        stop_running = True
        print("going back to withdraw/deposit position")
        
        gpio.cleanup()

if __name__ == "__main__":
    try :
        while True:
            print("Starting")
            n = int(input())
            go_to_locker(n)
    except KeyboardInterrupt:
        print("Ending")
