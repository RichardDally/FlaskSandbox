import os
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from .database import db
import secrets
from flask_sandbox.general.general import general_bp
from flask_sandbox.auth.auth import auth_bp
from flask_sandbox.user.user import user_bp
from flask_sandbox.files.files import files_bp


def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", secrets.token_urlsafe(16))
    # In-memory  : sqlite:///:memory:
    # Local file : sqlite:///flask_sandbox.db
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///flask_sandbox.db")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our videos table, use it in the query for the videos
        return User.query.get(int(user_id))

    # Registering blue prints
    app.register_blueprint(general_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(files_bp)

    return app
