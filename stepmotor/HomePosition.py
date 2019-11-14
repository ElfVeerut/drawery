import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
CW =1
CCW =0

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class HomePosition():
    def __init__(self,dir_motor,step_motor,pos_home,CW_CCW,num_sleep=.001):
        self.dir_motor = dir_motor
        self.step_motor = step_motor
        self.pos_home = pos_home
        self.value_switch = GPIO.input(self.pos_home)
        self.CW_CCW = CW_CCW
        self.num_sleep = num_sleep
        GPIO.setup(self.dir_motor, GPIO.OUT)
        GPIO.setup(self.step_motor, GPIO.OUT)
        self.interupt = False
        self.lift = False
        self.status = False
    def limit_switch(self):
        self.value_switch = GPIO.input(self.pos_home)
        return self.value_switch
    def return_home(self): 
        try:
            GPIO.output(self.dir_motor,self.CW_CCW)
            while True:
                GPIO.output(self.step_motor,GPIO.HIGH)
                sleep(self.num_sleep)
                GPIO.output(self.step_motor,GPIO.LOW)
                sleep(self.num_sleep)
                if self.limit_switch():
                    sleep(0.01)
                    if self.limit_switch():
                        break
            return True
        except:
            print(self.limit_switch())
    def move(self,duration,direction,num2=0.001):
        GPIO.output(self.dir_motor,direction)
        self.status = True
        # global stop_running
        for _ in range(duration):
            if self.interupt and not self.lift :
                self.status = False
                return "Interupt"
            GPIO.output(self.step_motor,GPIO.HIGH)
            sleep(num2)
            GPIO.output(self.step_motor,GPIO.LOW)
            sleep(num2)
        self.status = False
        return "DONE"
