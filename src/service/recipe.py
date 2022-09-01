from bson.json_util import dumps
from src.db import db


def get_recipes(**kwargs):
    return dumps(db.get_recipes(**kwargs))

def get_recipe(recipe_id):
    return dumps(db.get_recipe(recipe_id))
