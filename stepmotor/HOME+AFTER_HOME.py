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
        threading.Thread.__init__(self)
        self.dir_motor = dir_motor
        self.step_motor = step_motor
        self.pos_home = pos_home
        self.value_switch = GPIO.input(self.pos_home)
        self.CW_CCW = CW_CCW
        GPIO.setup(self.dir_motor, GPIO.OUT)
        GPIO.setup(self.step_motor, GPIO.OUT)
    def limit_switch(self):
        self.value_switch = GPIO.input(self.pos_home)
        return self.value_switch
    def run(self): 
        try:
            GPIO.output(self.dir_motor,self.CW_CCW)
            while True:
                GPIO.output(self.step_motor,GPIO.HIGH)
                sleep(.001)
                GPIO.output(self.step_motor,GPIO.LOW)
                sleep(.001)
                if self.limit_switch():
                    sleep(0.01)
                    if self.limit_switch():
                        break
            return True
        except:
            print(self.limit_switch())
    def move(self,duration,direction):
        GPIO.output(self.dir_motor,direction)
        global stop_running
        for _ in range(duration):
            GPIO.output(self.step_motor,GPIO.HIGH)
            sleep(0.001)
            GPIO.output(self.step_motor,GPIO.LOW)
            sleep(0.001)
        print("DONE")
        
x = HomePosition(19,26,4,CW)
y = HomePosition(20,21,17,CCW)
z = HomePosition(13,6,18,CCW)

x.start()
y.start()
z.start()

x.join()
y.join()
z.join()

#GPIO.cleanup()

print("HOME")

while True:
    n = int(input())
    if n == 1 :
        print('prepare position')
        #move('X',3600)
        motor_threading1 = threading.Thread(target=x.move,args=(1000,CCW)) #1000
        motor_threading2 = threading.Thread(target=y.move,args=(1600,CW)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
    elif n == 2 :
        motor_threading1 = threading.Thread(target=move,args=(1450,CW)) #1000
        #motor_threading2 = threading.Thread(target=move,args=('z',1675,CW)) #1675
        motor_threading1.start()
        #motor_threading2.start()
        motor_threading1.join()
        print("reach locker bot_left")
    elif n == 3:
        motor_threading1 = threading.Thread(target=move,args=(1400,CCW)) #1000
        #motor_threading2 = threading.Thread(target=move,args=('z',1675,CW)) #1675
        motor_threading1.start()
        #motor_threading2.start()
        motor_threading1.join()
        print("reach locker bot_right")
    elif n == 4 :
        motor_threading1 = threading.Thread(target=move,args=(1450,CW)) #1000
        motor_threading2 = threading.Thread(target=move,args=(2050,CW)) #1675
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
        print("reach locker top_right")
