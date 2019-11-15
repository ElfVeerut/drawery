from flask import Flask, redirect, url_for, request, render_template, jsonify, request
import ast, json, os, webbrowser,csv
from time import sleep
from dear import *
from enrollm1 import enroll
from checkm1 import check
from weight_check import checkWeight
import csv
#import panda as pd

filename = "new_finger_track.csv"
header = ("ID","Name","Item","Public/Private","Availability","Time")
def recall_data():
    global box
    global public_box
    global private_box
    box = []
    public_box = []
    private_box = []
    with open(filename,'r', newline= "") as file:
        reader = csv.reader(file, delimiter=',')
        i=0
        for line in reader:
            if i == 0: i+=1; continue
            box.append(int(line[4]))
        print(box)
        public_box = [box[0],box[1]]
        private_box = [box[2],box[3]]
    
    return ('done')

def rewrite_data(number):

    with open(filename,'r', newline= "") as file:

        readData = [row for row in csv.DictReader(file)]
        readData[number-1]['Availability'] = '1'

    readHeader = readData[0].keys()

    with open (filename, "w", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header)
        writer.writeheader()
        writer.writerows(readData)
#    file.close()
#    csvfile.close()
    return ("Done")

#    readData = [row for row in csv.DictReader(file)]

#go_home()
#sleep(0.5)
#prepare_pos()
recall_data()
data = '0'
withdrawdata = '0'
#check = (-1)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/withdraw_or_deposit')
def WithdrawOrDeposit():
    return render_template('WithdrawOrDeposit.html')

@app.route('/deposit_available')
def available():
    return render_template('Deposit_Avaible.html')
    
@app.route('/deposit_public_available')
def public_available():
    return render_template('Deposit_Public_Available.html')
    
@app.route('/deposit_private_available')
def private_available():
    return render_template('Deposit_Private_Available.html')

@app.route('/check_finger')
def checkFinger():
    return render_template('fingerprint.html')

@app.route('/enroll_finger')
def enroll_finger_():
    return render_template('fingerprint_register.html')

@app.route('/no_finger_found')
def noFinger():
    return render_template('regis_adminpass.html')

@app.route('/return_item_deposit')
def ReturnItem():
    return render_template('return_drawer_deposit.html')

@app.route('/return_item_withdraw')
def ReturnItemWithdraw():
    return render_template('return_drawer_withdraw.html')

@app.route('/return_item_private')
def ReturnItemPrivate():
    return render_template('return_drawer_private.html')

@app.route('/withdrawal')
def withdrawal():
    recall_data()
    if box != [1,1,1,1]:
        return render_template('Withdraw_Available.html')
    else:
        return render_template('NoAvailableForEveryDrawer.html')
    return ('error')

@app.route('/public_or_private')
def PublicOrPrivate():
    recall_data()
    print(box)
#    box = [0,0,0,0]    
    if box == [1,1,1,1]:
        return render_template('NoAvailableForEveryDrawer.html')
    else:
        return render_template('Private_public.html')
 
@app.route('/name_deposit', methods = ['GET','POST'])
def nameDeposit():
    res = ''
    recall_data()
    if request.method == 'POST':
        name = request.form['FirstName']
        res += name       
        return render_template('Deposit_Avaible.html')
    if request.method == 'GET':
        return json.dumps(box)
        
@app.route('/box_check_dp')
def check_dp():
    recall_data()
#    public_box = [0,0]
#    x = HomePosition(19,26,4,CW)
#    y = HomePosition(20,21,17,CWW)
#    z = HomePosition(13,6,18,CW)
    if public_box != [1,1]:
        return render_template('Deposit_Public_Available.html')
#    if public_box[0] == 0:
#        go_to_locker(3)
#        sleep(1)
#        returnpos_to_locker(3)
#        go_home()
#        prepare_pos()
#        return('returning box1') #return page GUI
        
#    elif public_box[1] == 0:
#        go_to_locker(4)
#        sleep(1)
#        returnpos_to_locker(4)
#        go_home()
#        prepare_pos()
#        return ('returning box2') #return page GUI
    
    else:
        return render_template('NoAvailibleDrawer.html')
               
@app.route('/box_check_public_deposit', methods = ['GET','POST'])
def public_deposit():
    recall_data()
#    public_box = [0,0]
    if request.method == 'GET':
        return json.dumps(public_box)
        
@app.route('/box_check_pp')
def check_pp():
    recall_data()
#    private_box = [0,0]
#    x = HomePosition(19,26,4,CW)
#    y = HomePosition(20,21,17,CWW)
#    z = HomePosition(13,6,18,CW)
    if private_box != [1,1]:
        return render_template('get_drawer_private.html')
#    if private_box[0] == 0:
#        go_to_locker(2)
#        sleep(1)
#        returnpos_to_locker(2)
#        go_home()
#        prepare_pos()
#        return('returning box3') #return page GUI
        
#    elif private_box[1] == 0:
#        go_to_locker(1)
#        sleep(1)
#        returnpos_to_locker(1)
#        go_home()
#        prepare_pos()
#        return ('returning box4') #return page GUI
    
    else:
        return render_template('NoAvailibleDrawer.html')

@app.route('/get_drawer_private', methods = ['POST'])
def getDrawerPrivate():
    recall_data()
#    private_box = [0,0]
    if request.method == 'POST':
        if private_box[0] == 0:
#            go_to_locker(3)
            return render_template('place_item_private.html') #return page GUI
#            
        elif private_box[1] == 0:
#            go_to_locker(4)
            return render_template('place_item_private.html') #return page GUI
    return('error')

@app.route('/return_drawer_private', methods = ['POST'])
def returnDrawerPrivate():
    recall_data()
#    private_box = [0,0]
    if request.method == 'POST':
        if private_box[0] == 0:
#            returnpos_to_locker(3)
#            sleep(1)
#            go_home()
#            prepare_pos()
#            rewrite_data(3)
            return render_template('welcome.html')
            
        elif private_box[1] == 0:
#            returnpos_to_locker(4)
#            sleep(1)
#            go_home()
#            prepare_pos()
#            rewrite_data(4)
            return render_template('welcome.html')
    return ('error')

@app.route('/box_check_private_deposit', methods = ['GET','POST'])
def private_deposit():
    recall_data()
#    private_box = [0,0]
    if request.method == 'GET':        
        return json.dumps(private_box)
                
@app.route('/name_withdrawal', methods = ['GET'])
def nameWithdrawal():
    recall_data()
#    name_withdraw = [0,0,0,0]
    if request.method == 'GET':
        return json.dumps(box)
        
@app.route('/register', methods = ['POST'])
def enroll_():
    global fingerData
    if request.method == 'POST':
        name2 = request.form['num2']
        print(name2)
        if name2 == '1':
            fingerData = enroll()
            if fingerData != False:
                return render_template('welcome.html')
            else:
                return render_template('regest_fail.html')
    return ('error')

@app.route('/check', methods = ['GET','POST'])
def check_():
    global check_tim
    if request.method == 'POST':
        name = request.form['num']
        print(name)
        if name == '1':
            check_tim = check()
            if check_tim != (-1):
                return render_template('WithdrawOrDeposit.html')
            else:
                return render_template('regis_adminpass.html')
    return ('error')

@app.route('/admin_password', methods = ['POST'])
def adminPassword():
    SetPassword = '12345'
    if request.method == 'POST':
        GetPassword = request.form['Password']
        print (GetPassword)
        if GetPassword == SetPassword:
            return render_template('register.html')
#        else:
#            return render_template('')
    
@app.route('/register_name', methods = ['POST'])
def getRegisterName():
    if request.method == 'POST':
        register_name = request.form['FirstName']
        print (register_name)
        return render_template('fingerprint_register.html')
    
@app.route('/weight_check_private', methods = ['POST'])
def check_weight():
    if request.method == 'POST':
        if checkWeight() == True:
#            return 'True'
            return render_template('return_drawer_private.html')
@app.route('/buttonpressed_private', methods = ['POST'])
def button_pressed():
    if request.method == 'POST':
        if request.form['buttonPressed'] == 'True':
#            return 'True'
            return render_template('return_drawer_private.html')
#@app.route('/weightcheck_or_buttonpressed_private')
#def weight_or_button():
#    if check_weight()=='True' or button_pressed()=='True':
#        return render_template('return_drawer_private.html')
        
@app.route('/getDataPublic', methods = ['POST'])
def get_data():
    if request.method == 'POST':
        global data
        data = request.form['data']
        print(type(data))
        print(data)
        return render_template('get_drawer_deposit.html')

@app.route('/get_drawer', methods=['POST'])
def get_drawers():
    global data
    print(data)
    print(type(data))
    if request.method == 'POST':
        data = int(data)
#        name = request.form['getdrawer']
#        print(name)
        go_to_locker(data)
        return render_template('Place_item.html')  
    return(str(data))

@app.route('/return_drawer', methods=['POST'])
def return_drawers():
    global data
    print(data)
    print(type(data))
    if request.method == 'POST':
        data = int(data)
        print(data)
        returnpos_to_locker(data)
        sleep(1)
        go_home()
        prepare_pos()
        recall_data()        
        return render_template('welcome.html')

        
@app.route('/getWithdrawData', methods=['POST'])
def get_withdraw_data():
    if request.method == 'POST':
        global withdrawdata
        withdrawdata=request.form['withdrawdata']
        print(withdrawdata)
        return render_template('get_drawer_withdraw.html')
    
@app.route('/getWithdrawDrawer', methods=['POST'])
def get_withdraw_drawer():
    global withdrawdata
    print(withdrawdata)
    if request.method == 'POST':
        withdrawdata = int(withdrawdata)
        go_to_locker(withdrawdata)
        return render_template('place_item_withdraw.html')

@app.route('/return_drawer_withdraw', methods=['POST'])
def return_drawers_withdraw():
    global withdrawdata
    print(withdrawdata)
    print(type(withdrawdata))
    if request.method == 'POST':
        withdrawdata = int(withdrawdata)
        print(withdrawdata)
        returnpos_to_locker(withdrawdata)
        sleep(1)
        go_home()
        prepare_pos()
        recall_data()
            
        return render_template('welcome.html')
        
#if __name__=="__main__":
#    app.run(ssl_context="adhoc")
        
        
        


