from bson.json_util import dumps
from src.db import db
from src.entities.recipe import Recipe


def get_recipes(**kwargs):
    return dumps(db.get_recipes(**kwargs))

def get_recipe(recipe_id):
    return dumps(db.get_recipe(recipe_id))

def add_recipe(body):
    recipe = Recipe(body.get('name'), body.get('description'), body.get('ingredients'), body.get('steps'), body.get('tags'))
    return dumps(db.add_recipe(recipe.__dict__()))
