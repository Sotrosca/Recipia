from bson.json_util import dumps
from flask_login import login_user, logout_user
from src.db import db
from src.entities.user import User
from werkzeug.security import check_password_hash, generate_password_hash


def get_user(id):
    return dumps(db.get_user(id))

def get_user_by_name(name):
    user = db.get_user_by_name(name)
    if not user is None:
        return User(user['_id'], user['name'], user['password'])
    return None

def create_user(name, password):
    return db.create_user(name, generate_password_hash(password))

def login(username, password):
    user = get_user_by_name(username)
    if user and check_password_hash(user.password, password):
        login_user(user)
        return True
    return False

def logout():
    return logout_user()


