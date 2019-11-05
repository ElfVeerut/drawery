from flask import Flask
from time import sleep
from FULL_1 import go_home , prepare_pos, go_to_locker , returnpos_to_locker
app = Flask(__name__)

@app.route('/')
def hello():
    go_home()
    print("HOME")
    #sleep(0.5)
    prepare_pos()
    n = int(input())
    if n==1:
        go_to_locker(1)
        sleep(1)
        returnpos_to_locker(1)
        return
    elif n==2:
        go_to_locker(2)
        sleep(1)
        returnpos_to_locker(2)
        return
    elif n==3:
        go_to_locker(3)
        sleep(1)
        returnpos_to_locker(3)
        return
    elif n==4:
        go_to_locker(4)
        sleep(1)
        returnpos_to_locker(4)
        return 'Hello World'
