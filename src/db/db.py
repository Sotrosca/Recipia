from bson.json_util import ObjectId
from flask import current_app
from pymongo import MongoClient
from werkzeug.local import LocalProxy


def get_db():
    client = MongoClient(current_app.config['DATABASE_URI'])
    db = client.Recipia
    return db

db = LocalProxy(get_db)

def get_recipes(**kwargs):
    recipes = db.recipes.find(kwargs)
    return recipes

def get_recipe(recipe_id):
    recipe = db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return recipe

def get_recipe_name(recipe_name):
    recipe = db.recipes.find_one({'name': recipe_name})
    return recipe

def get_user(id):
    user = db.users.find_one({'_id': ObjectId(id)})
    return user

def create_user(name, password):
    user = db.users.insert_one({'name': name, 'password': password})
    return user.inserted_id

def get_user_by_name(name):
    user = db.users.find_one({'name': name})
    return user
