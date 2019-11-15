from flask import Flask
from time import sleep
from start import *
app = Flask(__name__)

return_home_inter()
#go_home()
sleep(1)
prepare_pos()

@app.route('/')
def Hello():
    public_box = [0,1]
    #x = HomePosition(19,26,4,CW)
    #y = HomePosition(20,21,17,CCW)
    #z = HomePosition(13,6,18,CW)
    if public_box[0] == 0:
        go_to_locker(1)
        sleep(1)
        returnpos_to_locker(1)
        sleep(1)
        go_home()
        prepare_pos()
        
        return ('sss')
    elif public_box[1] == 0:
        go_to_locker(2)
        sleep(1)
        returnpos_to_locker(2)
        return('ssss')
    else:
        return ('error')