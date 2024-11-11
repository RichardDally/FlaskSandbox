from flask import current_app
from werkzeug.security import generate_password_hash
from flask_sandbox import db
from flask_sandbox.models import User, Trading


def create_dummy_user():
    current_app.logger.info("Creating user=dummy")
    name = "dummy"
    email = "dummy@test.com"
    password = "test"
    user = User(
        name=name,
        password=generate_password_hash(password=password),
        email=email,
    )
    trading = Trading(balance=1000.0, user=user)
    db.session.add(user)
    db.session.add(trading)
    db.session.commit()
