from flask import Flask, redirect, url_for, request, render_template, jsonify, request
import ast, json, os, webbrowser,csv
from enrollm1 import enroll
from checkm1 import check
from weight_check import checkWeight

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/withdraw_or_deposit')
def WithdrawOrDeposit():
    return render_template('WithdrawOrDeposit.html')

@app.route('/unavailable')
def unavailable():
    return render_template ('NoAvailible.html')

@app.route('/deposit_available')
def available():
    return render_template('Deposit_Avaible.html')
    
@app.route('/deposit_public_available')
def public_available():
    return render_template('Deposit_Public_Available.html')
    
@app.route('/deposit_private_available')
def private_available():
    return render_template('Deposit_Private_Available.html')

@app.route('/withdrawal')
def withdrawal():
    return render_template('Withdraw_Available.html')

@app.route('/check_finger')
def checkFinger():
    return render_template('fingerprint.html')

@app.route('/no_finger_found')
def noFinger():
    return render_template('regis_adminpass.html')

@app.route('/public_or_private')
def PublicOrPrivate():
    box = [1,1,1,1]
    if box == [1,1,1,1]:
        return render_template('NoAvailableForEveryDrawer.html')
    else:
        return render_template('Private_public.html')
 
@app.route('/name_deposit', methods = ['GET','POST'])
def nameDeposit():
    res = ''
    nc=[0,0,1,1]
    if request.method == 'POST':
        name = request.form['FirstName']
        res += name       
        return render_template('Deposit_Avaible.html')
    if request.method == 'GET':
        return json.dumps(nc)
        
@app.route('/box_check_dp')
def check_dp():
    public_box = [0,1]
    if public_box == [1,1]:
        return render_template('NoAvailibleDrawer.html')
    else:
        return render_template('Deposit_Public_Available.html')
               
@app.route('/box_check_public_deposit', methods = ['GET','BOX'])
def public_deposit():
    public_box = [0,1]
    if request.method == 'GET':
        return json.dumps(public_box)
        
@app.route('/box_check_pp')
def check_pp():
    private_box = [1,0]
    if private_box == [1,1]:
        return render_template('NoAvailibleDrawer.html')
    else:
        return render_template('Deposit_Private_Available.html')
        
@app.route('/box_check_private_deposit', methods = ['GET','POST'])
def private_deposit():
    private_box = [1,0]
    if request.method == 'GET':        
        return json.dumps(private_box)
                
@app.route('/name_withdrawal', methods = ['GET'])
def nameWithdrawal():
    name_withdraw = [0,1,1,0]
    if request.method == 'GET':
        return json.dumps(name_withdraw)
        
@app.route('/register', methods = ['GET','POST'])
def enroll_():
    if request.method == 'POST':
        name_withdraw = [1,1,1,1]
        name2 = request.form['num2']
        print(name2)
        if name2 == '1':
            if enroll():
                return render_template('welcome.html')
            else:
                return render_template('welcome.html')
    return ('error')

@app.route('/check', methods = ['GET','POST'])
def check_():
    if request.method == 'POST':
        name = request.form['num']
        print(name)
        if name == '1':
            if check()!= (-1):
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
        else:
            return render_template('')
    
@app.route('/register_name', methods = ['POST'])
def getRegisterName():
    if request.method == 'POST':
        register_name = request.form['FirstName']
        print (register_name)
        return render_template('fingerprint_register.html')
    
@app.route('/weight_check', methods = ['POST'])
def check_weight():
    if request.method == 'POST':
        checkweight = request.form['weight']
        if checkweight == '1':
            checkWeight()
            return render_template('Place_item.html')
        
@app.route('/getData', methods = ['POST'])
def det_data():
    if request.method == 'POST':
        data = (request.json)
        print('fdsfsd')
        print(jsonify(data))
        return ('fdsfdsf')
    
#@app.route('/track', methods = ['POST'])
#def track_info():
#    if request.method == 'POST':
        
           
        
        
        
        
        


