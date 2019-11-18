from flask import Flask, redirect, url_for, request, render_template, jsonify, request
import ast, json, os, webbrowser,csv
#import flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required, \
    UserMixin
from flask_security.utils import hash_password
from time import sleep
from dear import *
from enrollm1 import enroll
from checkm1 import check
from weight_check import checkWeight
from startpy import *
import csv
#import panda as pd

#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'thisisasecret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.fingerprintLogin'
#app.config['SECURITY_PASSWORD_SALT'] = 'thisisasecretsalt'

#db = SQLAlachemy(app)

#roles_users = db.Table('roles_users',
#                       db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
#                       db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
#                       )

filename = "new_finger_track.csv"
header = ("ID","Name","Item","Public/Private","Availability","Process")
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
    
    return 

def rewrite_data(number):

    with open(filename,'r', newline= "") as file:

        readData = [row for row in csv.DictReader(file)]
        readData[number-1]['Availability'] = '0'

    readHeader = readData[0].keys()

    with open (filename, "w", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header)
        writer.writeheader()
        writer.writerows(readData)
#    file.close()
#    csvfile.close()
    return 
#rewrite_data(4)
#    readData = [row for row in csv.DictReader(file)]

go_home()
sleep(0.5)
prepare_pos()
recall_data()
data = '0'
withdrawdata = '0'
fingerAuth = 0
#check = (-1)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')
    
@app.route('/withdraw_or_deposit')
def WithdrawOrDeposit():
    if fingerAuth:
        return render_template('WithdrawOrDeposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/deposit_available')
def available():
    if fingerAuth == 1:
        return render_template('Deposit_Avaible.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/deposit_public_available')
def public_available():
    if fingerAuth == 1:
        return render_template('Deposit_Public_Available.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/deposit_private_available')
def private_available():
    if fingerAuth == 1:
        return render_template('Deposit_Private_Available.html')
    else:
        return redirect(url_for('home'))
    
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
    if fingerAuth == 1:
        return render_template('return_drawer_deposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/return_item_withdraw')
def ReturnItemWithdraw():
    if fingerAuth == 1:
        return render_template('return_drawer_withdraw.html')
    else:
        return redirect(url_for('home'))

@app.route('/return_item_private')
def ReturnItemPrivate():
    if fingerAuth == 1:
        return render_template('return_drawer_private.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_item_deposit')
def InterrupItemDeposit():
    if fingerAuth == 1:
        return render_template('interrupt_drawer_deposit.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/withdrawal')
def withdrawal():
    recall_data()
    if fingerAuth == 1:
        if box != [1,1,1,1]:
            return render_template('Withdraw_Available.html')
        else:
            return render_template('NoAvailableForEveryDrawer.html')
        return ('error')
    else:
        return redirect(url_for('home'))
    
@app.route('/public_or_private')
def PublicOrPrivate():
    recall_data()
    print(box)
    if fingerAuth == 1:
    #    box = [0,0,0,0]    
        if box == [1,1,1,1]:
            return render_template('NoAvailableForEveryDrawer.html')
        else:
            return render_template('Private_public.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/name_deposit', methods = ['GET','POST'])
def nameDeposit():
    res = ''
    recall_data()
    if fingerAuth == 1:
        if request.method == 'POST':
            name = request.form['FirstName']
            res += name       
            return render_template('Deposit_Avaible.html')
        if request.method == 'GET':
            return json.dumps(box)
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_dp')
def check_dp():
    recall_data()
#    public_box = [0,0]
#    x = HomePosition(19,26,4,CW)
#    y = HomePosition(20,21,17,CWW)
#    z = HomePosition(13,6,18,CW)
    if fingerAuth == 1:
        if public_box != [1,1]:
            return render_template('Deposit_Public_Available.html')  
        else:
            return render_template('NoAvailibleDrawer.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_public_deposit', methods = ['GET','POST'])
def public_deposit():
    recall_data()
#    public_box = [0,0]
    if fingerAuth == 1:
        if request.method == 'GET':
            return json.dumps(public_box)
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_pp')
def check_pp():
    recall_data()
#    private_box = [0,0]
#    x = HomePosition(19,26,4,CW)
#    y = HomePosition(20,21,17,CWW)
#    z = HomePosition(13,6,18,CW)
    if fingerAuth == 1:
        if private_box != [1,1]:
            return render_template('get_drawer_private.html')
        else:
            return render_template('NoAvailibleDrawer.html')
    else:
        return redirect(url_for('home'))

@app.route('/get_drawer_private', methods = ['POST'])
def getDrawerPrivate():
    recall_data()
#    private_box = [0,0]
    if fingerAuth == 1:
        if request.method == 'POST':
            if private_box[0] == 0:
    #            go_to_locker(3)
                return render_template('place_item_private.html') #return page GUI
    #            
            elif private_box[1] == 0:
    #            go_to_locker(4)
                return render_template('place_item_private.html') #return page GUI
        return('error')
    else:
        return redirect(url_for('home'))
    
@app.route('/return_drawer_private', methods = ['POST'])
def returnDrawerPrivate():
    recall_data()
#    private_box = [0,0]
    if fingerAuth == 1:
        if request.method == 'POST':
            if private_box[0] == 0:
                returnpos_to_locker(3)
                sleep(1)
                go_home()
                prepare_pos()
                rewrite_data(3)
                return render_template('welcome.html')
                
            elif private_box[1] == 0:
                returnpos_to_locker(4)
                sleep(1)
                go_home()
                prepare_pos()
                rewrite_data(4)
                return render_template('welcome.html')
        return ('error')
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_private_deposit', methods = ['GET','POST'])
def private_deposit():
    recall_data()
#    private_box = [0,0]
    if fingerAuth == 1:
        if request.method == 'GET':        
            return json.dumps(private_box)
    else:
        return redirect(url_for('home'))
    
@app.route('/name_withdrawal', methods = ['GET'])
def nameWithdrawal():
    recall_data()
#    name_withdraw = [0,0,0,0]
    if fingerAuth == 1:
        if request.method == 'GET':
            return json.dumps(box)
    else:
        return redirect(url_for('home'))
    
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
    global fingerAuth
    if request.method == 'POST':
        name = request.form['num']
        print(name)
        if name == '1':
            check_tim = check()
            if check_tim != (-1):
                fingerAuth = 1
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
    if fingerAuth == 1:
        if request.method == 'POST':
            if checkWeight() == True:
    #            return 'True'
                return render_template('return_drawer_private.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/buttonpressed_private', methods = ['POST'])
def button_pressed():
    if fingerAuth == 1:
        if request.method == 'POST':
            if request.form['buttonPressed'] == 'True':
    #            return 'True'
                return render_template('return_drawer_private.html')
    else:
        return redirect(url_for('home'))
#@app.route('/weightcheck_or_buttonpressed_private')
#def weight_or_button():
#    if check_weight()=='True' or button_pressed()=='True':
#        return render_template('return_drawer_private.html')
        
@app.route('/getDataPublic', methods = ['POST'])
def get_data():
    if fingerAuth == 1:
        if request.method == 'POST':
            global data
            data = request.form['data']
            print(type(data))
            print(data)
            return render_template('get_drawer_deposit.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/get_drawer', methods=['POST'])
def get_drawers():
    global data
    print(data)
    print(type(data))
    if fingerAuth == 1:
        if request.method == 'POST':
            data = int(data)
    #        name = request.form['getdrawer']
    #        print(name)
            go_to_locker(data)
            return render_template('Place_item.html')  
        return(str(data))
    else:
        return redirect(url_for('home'))
    
@app.route('/return_drawer', methods=['POST'])
def return_drawers():
    global data
    global fingerAuth
    print(data)
    print(type(data))
    if fingerAuth == 1:
        if request.method == 'POST':
            data = int(data)
            print(data)
            returnpos_to_locker(data)
            sleep(1)
            go_home()
            prepare_pos()
            recall_data()
            fingerAuth = 0
            return redirect(url_for('home'))
#            return render_template('welcome.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_drawer', methods=['POST','GET'])
def interrupt_drawers():
    if fingerAuth == 1:
        if request.method == 'POST':
            print(inter())
            return ('interrupt')
        return('wow')
    else:
        return redirect(url_for('home'))
    
@app.route('/getWithdrawData', methods=['POST'])
def get_withdraw_data():
    if fingerAuth == 1:
        if request.method == 'POST':
            global withdrawdata
            withdrawdata=request.form['withdrawdata']
            print(withdrawdata)
            return render_template('get_drawer_withdraw.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/getWithdrawDrawer', methods=['POST'])
def get_withdraw_drawer():
    global withdrawdata
    print(withdrawdata)
    if fingerAuth == 1:
        if request.method == 'POST':
            withdrawdata = int(withdrawdata)
            go_to_locker(withdrawdata)
            return render_template('place_item_withdraw.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/return_drawer_withdraw', methods=['POST'])
def return_drawers_withdraw():
    global withdrawdata
    print(withdrawdata)
    print(type(withdrawdata))
    if fingerAuth == 1:
        if request.method == 'POST':
            withdrawdata = int(withdrawdata)
            print(withdrawdata)
            returnpos_to_locker(withdrawdata)
            sleep(1)
            go_home()
            prepare_pos()
            recall_data()
            fingerAuth = 0    
#            return render_template('welcome.html')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
    
#if __name__=="__main__":
#    app.run(ssl_context="adhoc")
        
        
        


