from flask import Flask
from time import sleep
from FULL_1 import *
app = Flask(__name__)

@app.route('/')
def Hello():
    public_box = [1,1]
    x = HomePosition(19,26,4,CW)
    y = HomePosition(20,21,17,CCW)
    z = HomePosition(13,6,18,CW)
    go_home()
    prepare_pos()
    if public_box[0] == 0:
        go_to_locker(3)
        sleep(1)
        returnpos_to_locker(3)
        return ('sss')
    elif public_box[1] == 0:
        go_to_locker(4)
        sleep(1)
        returnpos_to_locker(4)
        return('ssss')
    else:
        return ('error')
