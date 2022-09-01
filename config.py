from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DATABASE_URI')
