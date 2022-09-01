import json

from bson.json_util import dumps
from flask import Blueprint, jsonify, make_response, request
from flask_login import current_user, login_required
from src.service import user as user_service

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/logged', methods=['GET'])
@login_required
def users():
    id = current_user.get_id()
    user = user_service.get_user(id)
    return jsonify(json.loads(user))

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    id = user_service.create_user(data['name'], data['password'])
    return make_response(jsonify({'id': str(id)}), 201)

@bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    logged = user_service.login(data.get('name'), data.get('password'))
    if logged:
        return make_response(dumps(logged), 200)
    return make_response('Unauthorized', 401)
