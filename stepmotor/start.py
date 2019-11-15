from time import sleep
import threading
from HomePosition import HomePosition
CW =1
CCW =0
""" test """
state = "Start"
box = False
num_box = 0
x = HomePosition(19,26,4,CW,.0003)
y = HomePosition(1,12,17,CCW,.0003)
z = HomePosition(13,6,18,CCW,.00035)
def prepare_pos():
    motor_threading1 = threading.Thread(target=x.move,args=(1000,CCW,.0003)) #1000
    motor_threading2 = threading.Thread(target=y.move,args=(1600,CW,.0003)) #1675
    motor_threading3 = threading.Thread(target=z.move,args=(150,CW,.0003))
    motor_threading1.start()
    motor_threading2.start()
    motor_threading3.start()
    motor_threading1.join()
    motor_threading2.join()
    motor_threading3.join()
    state = "Prepare_pos"
    return "Prepare positon"
def prepare_pos2():
    motor_threading2 = threading.Thread(target=y.move,args=(1600,CW,.0003)) #167
    motor_threading2.start()
    motor_threading2.join()
    state = "Prepare_pos"
    return "Prepare positon"    
def out():
    state = "move to locker"
    z.move(700,CW,.00035)
    sleep(0.05)
    x.move(3000,CW,.0003)
    sleep(0.05)
    return "OUT"
def lift():
    state = "lifting"
    x.lift = True
    z.lift = True
    x.move(2300,CCW,.0003)
    sleep(0.05)
    z.move(500,CW,.00035)
    sleep(0.05)
    x.move(3000,CW,.0003)

    x.lift = False
    z.lift = False
    box = True

    return "LIFT"
def place():
    state = "place the box"
    x.move(3000,CCW,.0003)
    sleep(0.05)
    z.move(600,CCW,.0003)
    sleep(0.05)
    x.move(3000,CW,.0003)
    return
def go_home():
    motor_threading1 = threading.Thread(target=x.return_home,args=()) #1000
    motor_threading2 = threading.Thread(target=y.return_home,args=()) #1675
    motor_threading3 = threading.Thread(target=z.return_home,args=())
    motor_threading1.start()
    motor_threading2.start()
    motor_threading3.start()
    motor_threading1.join()
    motor_threading2.join()
    motor_threading3.join()
    state = "Home"
    return "HOME"
#GPIO.cleanup()

def go_to_locker(n):
    num_box = n
    if n == 3 :
        y.move(1400,CW,.0003)
        state = "locker"
        print("reach locker bot_left")
        lift()
        box = True
        state = "locker with box"
        motor_threading1 = threading.Thread(target=y.move,args=(2600,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(4400,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        sleep(0.05)
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(460,CCW,.0003)

    elif n == 4:
        y.move(1350,CCW,.0003)
        print("reach locker bot_right")
        box = True
        state = "locker"
        lift()
        state = "locker with box"
        z.move(4400,CW,.0003)
        sleep(0.05)
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(460,CCW,.0003)

    elif n == 2 :
        motor_threading1 = threading.Thread(target=y.move,args=(1400,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2000,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        print("reach locker top_left")
        state = "locker"
        lift()
        box = True
        state = "locker with box"
        motor_threading1 = threading.Thread(target=y.move,args=(2700,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2300,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(400,CCW,.0003)

    elif n == 1 :
        motor_threading1 = threading.Thread(target=y.move,args=(1350,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2000,CW,.00032)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        state = "locker"
        print("reach locker top_right")
        lift()
        box = True
        state = "locker with box"
        z.move(2600,CW,.00032)
        sleep(0.05)
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(700,CCW,.00032)

    state = "return pos"
    return

def returnpos_to_locker(n):
    num_box = n
    if n == 1:
        out()
        state = "return_to_locker"
        z.move(2600,CCW,.0003)
        sleep(0.05)
        place()
    elif n == 2:
        out()
        state = "return_to_locker"
        sleep(0.05)
        motor_threading1 = threading.Thread(target=y.move,args=(2725,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2650,CCW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        sleep(0.05)
        place()
    elif n == 4 :
        out()
        state = "return_to_locker"
        z.move(4600,CCW,.0003)
        sleep(0.05)
        place()
    elif n == 3:
        out()
        state = "return_to_locker"
        sleep(0.05)
        motor_threading1 = threading.Thread(target=y.move,args=(2600,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(4600,CCW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        place()
    box = False
    num_box = 0
    state = "locker"
    return
def return_home_inter():
    x.return_home()
    t1 = threading.Thread(target=y.return_home,args=())
    t2 = threading.Thread(target=z.return_home,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    z.return_home()
    
    print("HOME")
    return
def return_home_inter2():
    z.return_home()
    sleep(0.05)
    if not z.value_switch:
        z.return_home()
    sleep(0.05)
    x.return_home()
    y.return_home()
    print("HOME")
    return

def return_box_inter(n):
    if n == 3 :
        motor_threading1 = threading.Thread(target=y.move,args=(1400,CW,.0003))
        motor_threading2 = threading.Thread(target=z.move,args=(700,CW,.0003))
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(300,CCW,.0003)
    elif n == 4:
        motor_threading1 = threading.Thread(target=y.move,args=(1400,CCW,.0003))
        motor_threading2 = threading.Thread(target=z.move,args=(700,CW,.0003))
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(300,CCW,.0003)
    elif n == 2 :
        motor_threading1 = threading.Thread(target=y.move,args=(1450,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2700,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(300,CCW,.0003)
        
    elif n == 1 :
        motor_threading1 = threading.Thread(target=y.move,args=(1400,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2700,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(300,CCW,.0003)
    place()

def inter(a):
    x.interupt = True
    y.interupt = True
    z.interupt = True
    while  x.status or y.status or z.status:
        sleep(0.005)
    x.interupt = False
    y.interupt = False
    z.interupt = False
    if a == "Prepare_pos":
        pass
    elif a == "locker with box":
        return_home_inter2()
        sleep(0.05)
        prepare_pos2()
        return_box_inter(num_box)
        
    elif a  == "return_to_locker" :
        return_home_inter()
        t1 = threading.Thread(target=z.move,args=(5000,CW,.0003)) 
        t2 = threading.Thread(target=y.move,args=(300,CW,.0003)) 
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        x.move(3000,CCW,.0003)
        z.move(500,CCW,.0003)
        #distance from home to return pos
        return
    return_home_inter()
    prepare_pos()
    return
#inter("Prepare_pos")
#inter("locker with box")
  
#inter("return_to_locker")
#returnpos_to_locker(4)
