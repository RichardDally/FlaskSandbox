from flask import current_app
from flask_sandbox import db
from flask_sandbox.models import Trading, User
from werkzeug.security import generate_password_hash


def create_new_user_in_db(
        username: str,
        email: str,
        clear_password: str,
        balance: float,
) -> None:
    current_app.logger.info(f"Creating new user={username}")
    user = User(
        name=username,
        password=generate_password_hash(password=clear_password),
        email=email,
    )
    trading = Trading(balance=balance, user=user)
    db.session.add(user)
    db.session.add(trading)
    db.session.commit()
