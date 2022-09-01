from flask import Flask
from flask_login import LoginManager

from config import DevelopmentConfig
from src.controller import recipe, user
from src.db import db
from src.entities.user import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(recipe.bp)
    app.register_blueprint(user.bp)
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    return app

app = create_app()

@app.login_manager.user_loader
def load_user(id):
    user = db.get_user(id)
    if not user:
        return None
    return User(user['_id'], user['name'], user['password'])
