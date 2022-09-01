import json

from flask import Blueprint, jsonify, request
from src.service import recipe as recipe_service

bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@bp.route('/')
def recipes():
    recipes = recipe_service.get_recipes(**request.args)
    return jsonify(json.loads(recipes))

@bp.route('/<recipe_id>')
def recipe(recipe_id):
    return jsonify(json.loads(recipe_service.get_recipe(recipe_id)))


