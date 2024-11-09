import os
import secrets
from logging.config import dictConfig
from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from .database import db
from flask_sandbox.general.general import general_bp
from flask_sandbox.auth.auth import auth_bp
from flask_sandbox.user.user import user_bp
from flask_sandbox.files.files import files_bp


def create_app():
    dictConfig(
        {
            # Specify the logging configuration version
            "version": 1,
            "formatters": {
                # Define a formatter named 'default'
                "default": {
                    # Specify log message format
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                # Define a console handler configuration
                "console": {
                    # Use StreamHandler to log to stdout
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    # Use 'default' formatter for this handler
                    "formatter": "default",
                }
            },
            # Configure the root logger
            "root": {
                # Set root logger level to DEBUG
                "level": "DEBUG",
                # Attach 'console' handler to the root logger
                "handlers": ["console"]},
        }
    )
    app = Flask(__name__)

    load_dotenv()
    flask_secret_key: str = os.getenv("FLASK_SECRET_KEY", secrets.token_urlsafe(16))
    # In-memory  : sqlite:///:memory:
    # Local file : sqlite:///flask_sandbox.db
    sqlalchemy_database_uri: str = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///flask_sandbox.db")
    upload_folder: str = os.getenv("UPLOAD_FOLDER", "uploads")

    app.logger.info(f"Creating upload_folder={upload_folder}")
    Path(upload_folder).mkdir(parents=True, exist_ok=True)

    # Setting Flask configuration
    app.config['SECRET_KEY'] = flask_secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
    app.config['UPLOAD_FOLDER'] = upload_folder

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
