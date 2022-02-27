from users_io import read_users, remove_users, save_user, read_user

def get_users():
    return read_users()

def get_user(userName):
    user = read_user(userName);
    return user

def create_user(userData):
    return save_user(userData)

def clear_users():
    return remove_users()