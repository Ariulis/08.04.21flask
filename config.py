import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLASKY_ADMIN = 'stylev38@gmail.com'
    MAIL_SUBJECT_PREFIX = '[Flasky]'
    MAIL_SENDER = 'Flasky admin <stylev38@gmail.com>'

    POSTS_PER_PAGE = 5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL', 'postgresql://postgres:1@localhost/test')

    # Mail

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'data_test.sqlite3'))


config = {
    'default': DevelopmentConfig,
    'delopment': DevelopmentConfig,
    'testing': TestConfig
}
