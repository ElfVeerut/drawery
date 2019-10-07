'''Copyright (C) jumejume1
All rights reserved '''

from time import sleep
import RPi.GPIO as gpio

DIR = 20
STEP = 21
CW =1
CCW =0

gpio.setmode(gpio.BCM)
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)
gpio.output(DIR,CW)

def sleepMicro(sec):
    sleep(sec/10000000)
    
# Main body of code
try :
    while True:
            n = int(input())
            if n == 1:
                print('go to position1')
                sleep(1)
                gpio.output(DIR,CW)
                for x in range(3600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(65)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(65)
                
                sleep(1)
                gpio.output(DIR,CCW)
                for x in range(3600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(100)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(100)
            elif n == 2:
                print('go to position 2')
                sleep(1)
                gpio.output(DIR,CW)
                for x in range(3600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(650)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(655)
                
                sleep(1)
                gpio.output(DIR,CCW)
                for x in range(3600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(5555)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(5555)
            elif n == 3:
                print('go to position 3')
                sleep(1)
                gpio.output(DIR,CW)
                for x in range(3600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(400)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(400)
                
                sleep(1)
                gpio.output(DIR,CCW)
                for x in range(3600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(65)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(65)
            elif n == 4:
                print('go to position 4')
                sleep(1)
                gpio.output(DIR,CW)
                for x in range(9600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(65)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(65)
                
                sleep(1)
                gpio.output(DIR,CCW)
                for x in range(3600):
                    gpio.output(STEP,gpio.HIGH)
                    sleepMicro(465)
                    gpio.output(STEP,gpio.LOW)
                    sleepMicro(465)
            else :
                print('full')
except KeyboardInterrupt:
    print("cleaning up")
    gpio.cleanup()