import json


def jsonCreateNewUser(new_data, filename='json_example.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["users"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def jsonCreateNewAccount(user_id, new_data, filename='json_example.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        for dict in file_data["users"]:
            if dict['user_id'] == user_id:
                if "account" in dict:
                    dict["account"].update(new_data)
                else:
                    dict["account"] = new_data
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def jsonUpdateAccountBalance(accountId, newBalance, filename='json_example.json'):
    with open('json_example.json','r+') as file:
        file_data = json.load(file)         
        for dict in file_data["users"]:
            if "account" in dict and dict['account']['account_id'] == accountId:
                    dict['account']['account_balance'] = newBalance

        file.seek(0)
        json.dump(file_data, file, indent = 4)

def jsonGetCurrentBalance(accountId, filename='json_example.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)         
        for dict in file_data["users"]:
            if "account" in dict and dict['account']['account_id'] == accountId:
                return dict['account']['account_balance']
    
    return "0"
