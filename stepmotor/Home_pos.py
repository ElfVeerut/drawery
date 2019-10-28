import RPi.GPIO as GPIO
from time import sleep
import threading
GPIO.setmode(GPIO.BCM)
CW =1
CCW =0

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class HomePosition(threading.Thread):
    def __init__(self,dir_motor,step_motor,pos_home,CW_CCW):
        self.dir_motor = dir_motor
        self.step_motor = step_motor
        self.pos_home = pos_home
        self.value_switch = GPIO.input(self.pos_home)
        self.CW_CCW = CW_CCW
        self.home = False
        GPIO.setup(self.dir_motor, GPIO.OUT)
        GPIO.setup(self.step_motor, GPIO.OUT)
    def limit_switch(self):
        self.value_switch = GPIO.input(self.pos_home)
        return self.value_switch
    def run(self): 
        GPIO.output(self.dir_motor,self.CW_CCW)
        temp =  
        while not self.limit_switch():
            try:
                GPIO.output(self.step_motor,GPIO.HIGH)
                sleep(.001)
                GPIO.output(self.step_motor,GPIO.LOW)
                sleep(.001)
            except:
                if temp == 
x = HomePosition(19,26,4,CW)
y = HomePosition(20,21,17,CCW)
z = HomePosition(13,6,18,CCW)

x.start()
y.start()
z.start()

x_t.join()
y_t.join()
z_t.join()

GPIO.cleanup()
print("HOME")

