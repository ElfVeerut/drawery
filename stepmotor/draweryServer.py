from flask import Flask
from time import sleep
from FULL_1 import go_home , prepare_pos, go_to_locker , returnpos_to_locker , go_home2
app = Flask(__name__)

@app.route('/')
def hello():
    n = int(input())
    go_to_locker(n)
    sleep(1) # code bam
    returnpos_to_locker(n)
    go_home()
    prepare_pos()
    return "DONE"