from flask import Flask, redirect, url_for, request, render_template, jsonify, request
import ast, json, os, webbrowser, csv
#import flask_sqlalchemy import SQLAlchemy
#from flask_security import Security, SQLAlchemyUserDatastore, login_required, \
#   UserMixin
#from flask_security.utils import hash_password
from time import sleep
from enrollm1 import enroll
from checkm1 import check
from weight_check import checkWeight
from start_2 import *
from Drawer_Data import *


#go_home()
return_home_inter()
sleep(0.5)
prepare_pos()
recall_data()
box = []
public_box = []
private_box = []
data = '0'
withdrawdata = '0'
fingerAuth = 0
returnBoxState = 0
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
    if fingerAuth:
        return render_template('return_drawer_withdraw.html')
    else:
        return redirect(url_for('home'))

@app.route('/return_item_private')
def ReturnItemPrivate():
    if fingerAuth:
        return render_template('return_drawer_private.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_item_deposit')
def InterrupItemDeposit():
    if fingerAuth:
        return render_template('interrupt_drawer_deposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_withdraw')
def InterrupItemWithdraw():
    if fingerAuth:
        return render_template('interrupt_drawer_withdraw.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_private')
def InterrupItemPrivate():
    if fingerAuth:
        return render_template('interrupt_drawer_private.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_item_return_deposit')
def InterrupItemReturnDeposit():
    if fingerAuth:
        return render_template('interrupt_drawer_return_deposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_return_withdraw')
def InterrupItemReturnWithdraw():
    if fingerAuth:
        return render_template('interrupt_drawer_return_withdraw.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_return_private')
def InterrupItemReturnPrivate():
    if fingerAuth:
        return render_template('interrupt_drawer_return_private.html')
    else:
        return redirect(url_for('home'))

@app.route('/withdrawal')
def withdrawal():
    recall_data()
    if fingerAuth:
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
    if fingerAuth:    
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
    if fingerAuth:
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
    if fingerAuth:
        if public_box != [1,1]:
            return render_template('Deposit_Public_Available.html')  
        else:
            return render_template('NoAvailibleDrawer.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_public_deposit', methods = ['GET','POST'])
def public_deposit():
    recall_data()
    if fingerAuth:
        if request.method == 'GET':
            return json.dumps(public_box)
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_pp')
def check_pp():
    recall_data()
    if fingerAuth:
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
                go_to_locker(3)
                return render_template('place_item_private.html') #return page GUI
    #            
            elif private_box[1] == 0:
                go_to_locker(4)
                return render_template('place_item_private.html') #return page GUI
        return('error')
    else:
        return redirect(url_for('home'))
    
@app.route('/return_drawer_private', methods = ['POST'])
def returnDrawerPrivate():
    global fingerAuth
    recall_data()
#    private_box = [0,0]
    if fingerAuth == 1:
        if request.method == 'POST':
            if private_box[0] == 0:
                returnpos_to_locker(3)
                sleep(1)
                go_home()
                prepare_pos()
                rewrite_data(3,'1')
                recall_data()
                returnBoxState = 0
                fingerAuth = 0
                return render_template('welcome.html')
                
            elif private_box[1] == 0:
                returnpos_to_locker(4)
                sleep(1)
                go_home()
                prepare_pos()
                rewrite_data(4,'1')
                recall_data()
                returnBoxState = 0
                fingerAuth = 0
                return render_template('welcome.html')
        return ('error')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_private', methods=['POST','GET'])
def interrupt_drawers_private():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            return redirect(url_for('WithdrawOrDeposit'))
        return('wow')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_return_private', methods=['POST'])
def interrupt_drawers_return_private():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            return render_template('place_item_private.html')
    else:
        return redirect(url_for('home'))


@app.route('/box_check_private_deposit', methods = ['GET','POST'])
def private_deposit():
    recall_data()
    if fingerAuth:
        if request.method == 'GET':        
            return json.dumps(private_box)
    else:
        return redirect(url_for('home'))
    
@app.route('/name_withdrawal', methods = ['GET'])
def nameWithdrawal():
    recall_data()
    if fingerAuth:
        if request.method == 'GET':
            return json.dumps(box)
    else:
        return redirect(url_for('home'))
    
@app.route('/register', methods = ['POST'])
def enroll_():
    global fingerData
    if request.method == 'POST':
#        name2 = request.form['num2']
#        print(name2)
#        if name2 == '1':
        fingerData = enroll()
        if fingerData != False:
            return redirect(url_for('home'))
        else:
                return render_template('regest_fail.html')
    return ('error')

@app.route('/check', methods = ['GET','POST'])
def check_():
    global check_tim
    global fingerAuth
    if request.method == 'POST':
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
        else:
            return redirect(url_for('noFinger'))
    
@app.route('/register_name', methods = ['POST'])
def getRegisterName():
    if request.method == 'POST':
        register_name = request.form['FirstName']
        print (register_name)
        return render_template('fingerprint_register.html')
    
@app.route('/weight_check_private', methods = ['POST'])
def check_weight():
    if fingerAuth:
        if request.method == 'POST':
            if checkWeight():
                if not returnBoxState:
                    returnBoxState = 1
                    return render_template('return_drawer_private.html')
                else:return
    else:
        return redirect(url_for('home'))
    
@app.route('/buttonpressed_private', methods = ['POST'])
def button_pressed():
    if fingerAuth == 1:
        if request.method == 'POST':
            if not returnBoxState:
                returnBoxState = 1
                return render_template('return_drawer_private.html')
    else:
        return redirect(url_for('home'))
        
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
            rewrite_data(data,'1')
            recall_data()
            fingerAuth = 0
            returnBoxState = 0
            return redirect(url_for('home'))
#            return render_template('welcome.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_drawer', methods=['POST','GET'])
def interrupt_drawers():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            return redirect(url_for('WithdrawOrDeposit'))
        return('wow')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_return', methods=['POST'])
def interrupt_drawers_return():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            return render_template('Place_item.html')
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
    global fingerAuth
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
            rewrite_data(withdrawdata,'0')
            recall_data()
            fingerAuth = 0
            returnBoxState = 0
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_withdraw', methods=['POST','GET'])
def interrupt_drawers_withdraw():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            return redirect(url_for('WithdrawOrDeposit'))
        return('wow')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_return_withdraw', methods=['POST'])
def interrupt_drawers_return_withdraw():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            return render_template('place_item_withdraw.html')
    else:
        return redirect(url_for('home'))

#if __name__=="__main__":
#    app.run(ssl_context="adhoc")
        
        
        


