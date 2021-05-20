"""Flask app configuration."""

from constants import BASE_DIR
from os import environ
from dotenv import load_dotenv
import redis

load_dotenv(BASE_DIR / ".env")


class FlaskConfig:
    """Set Flask configuration from environment variables."""

    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    # # Flask-Assets
    # LESS_BIN = environ.get('LESS_BIN')
    # ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    # LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    # COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Session
    SESSION_TYPE = environ.get('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))

    # Celery
    CELERY_BROKER_URL = environ.get('CELERY_BROKER_URL')
    
    # Flask-Mail
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    
