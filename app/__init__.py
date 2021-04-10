from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import config
from .admin import HomeAdminView, UserAdminView

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Admin

    from .models import User
    admin = Admin(app, 'FlaskyApp', url='/', index_view=HomeAdminView())
    admin.add_views(UserAdminView(User, db.session))

    # Blueprints

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_bluprint
    app.register_blueprint(auth_bluprint, url_prefix='/auth')

    return app
