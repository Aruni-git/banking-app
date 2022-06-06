import User, Account
from flask import Flask, redirect, request
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/user/create_user', methods=['POST'] )
def createUser():
    return User.createUser(request.get_json())

@app.route('/account/create_account', methods=['POST'] )
def createAccount():
    return Account.createAccount(request.get_json())

@app.route('/account/<accountId>/deposit', methods=['PUT'] )
def deposit(accountId):   
    return Account.deposit(accountId, request.get_json())

@app.route('/account/<accountId>/withdraw', methods=['PUT'] )
def withdraw(accountId):
    return Account.withdraw(accountId, request.get_json())
    
@app.route('/account/<accountId>/balance', methods=['GET'] )
def balance(accountId):
    return Account.balance(accountId)

@app.route('/account/<srcAccountId>/send/<destAccountId>', methods=['PUT'] )
def send(srcAccountId, destAccountId):
    return Account.send(srcAccountId, destAccountId, request.get_json())
  
app.run()


