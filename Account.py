import uuid, DataHandler
from flask import jsonify


def createAccount(requestData):
    userId = requestData['user_id']

    accountId = str(uuid.uuid4())
    data = {
        "account_id": accountId,
        "account_balance": 0
    }
    DataHandler.jsonCreateNewAccount(userId, data)

    responseMsg = {
        'status': 'success',
        'account_id': accountId
    }
    return jsonify(responseMsg)


def deposit(accountId, requestData):
    depositAmount = requestData['amount']
    newBalance = int(depositAmount) + int(DataHandler.jsonGetCurrentBalance(accountId))

    DataHandler.jsonUpdateAccountBalance(accountId, newBalance)

    responseMsg = {
        'status': 'success',
        'account_id': accountId,
        'account_balance': newBalance
    }
    return jsonify(responseMsg)


def withdraw(accountId, requestData):
    withdrawAmount = requestData['amount']
    newBalance = int(DataHandler.jsonGetCurrentBalance(accountId)) - int(withdrawAmount)

    DataHandler.jsonUpdateAccountBalance(accountId, newBalance)

    responseMsg = {
        'status': 'success',
        'account_id': accountId,
        'account_balance': newBalance
    }
    return jsonify(responseMsg)


def balance(accountId):
    balance = int(DataHandler.jsonGetCurrentBalance(accountId))

    responseMsg = {
        'status': 'success',
        'account_id': accountId,
        'account_balance': balance
    }
    return jsonify(responseMsg)


def send(srcAccountId, destAccountId, requestData):
    sendAmount = requestData['amount']

    srcNewBalance = int(DataHandler.jsonGetCurrentBalance(srcAccountId)) - int(sendAmount)
    destNewBalance = int(DataHandler.jsonGetCurrentBalance(destAccountId)) + int(sendAmount)

    DataHandler.jsonUpdateAccountBalance(srcAccountId, srcNewBalance)
    DataHandler.jsonUpdateAccountBalance(destAccountId, destNewBalance)

    responseMsg = {
        'status': 'success',
        'source_account_id': srcAccountId,
        'source_account_balance': srcNewBalance,
        'destination_account_id': destAccountId,
        'destination_account_balance': destNewBalance
    }
    return jsonify(responseMsg)
