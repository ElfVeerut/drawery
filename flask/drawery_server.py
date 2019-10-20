from flask import Flask, redirect, url_for, request, render_template, jsonify
import ast, json, os, webbrowser
from enrollm1 import enroll
from checkm1 import check
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Deposit_Avaible.html')

@app.route('/unavailable')
def unavailable():
    return render_template ('NoAvailible.html')

# @app.route('/deposit')
#def deposit():
    #return render_template ('register.html')

# @app.route('/')

    
@app.route('/name', methods = ['GET','POST'])
def name():
    firstname = 'FirstName'
    res = ''
    nc=[1,0,0,1]
    # print("helo")
    if request.method == 'POST':
        name = request.form[firstname]
        res += name
        print (res)
    # return render_template('Deposit_Avaible.html')
        return res
    if request.method == 'GET':
        print(json.dumps(nc))
        return json.dumps(nc)
    
    # if request.method = 'POST'
@app.route('/enroll', methods = ['GET','POST'])
def enroll():
    res=0
    print('fdsfsd')
    if request.method == 'POST':
        name = request.form['num']
        print(123)
        res = name
        print (type(res))
        
        if res == '1':
            print('fsdfsdf')
            
            if check():
                return render_template('WithdrawOrDeposit.html')
            else:
                return render_template('register.html')
    return ('fsdfsd')           
    #$value = 'num'
    #check()
    #return render_template('fingerprint.html')
    


