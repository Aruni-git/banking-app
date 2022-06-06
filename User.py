from flask import jsonify
import DataHandler, uuid


def createUser(requestData):
    firstName = requestData['first_name']
    lastName = requestData['last_name']

    userId =  str(uuid.uuid4())
    data = {
                "user_id":userId,
                "first_name": firstName,
                "last_name": lastName 
            }
     
    DataHandler.jsonCreateNewUser(data)

    responseMsg = {
            'status': 'success',
            'user_id': userId
        }
    return jsonify(responseMsg)