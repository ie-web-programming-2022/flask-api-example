import json

users_path = './users.json'

def read_json_file(file_path):
    with open(file_path) as file:
        return json.load(file)

def write_json_file(file_path, data):
    with open(file_path, "w") as file:
        return json.dump(data, file)

def user_exists(userName):
    return read_user(userName) != None

def read_users():
    return read_json_file(users_path)

def read_user(userName):
    for user in read_users():
        if user.username == userName:
            return user

def save_user(user_data):
    if user_exists(user_data.userName):
        raise Exception()

    users = read_users()
    users.push(user_data)
    write_json_file(users_path, users)
    return user_data

def remove_users():
    write_json_file(users_path, [])
    return []