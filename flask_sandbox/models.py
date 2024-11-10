from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from flask_sandbox import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    trading = db.relationship("Trading", backref="user", lazy=True, uselist=False)


class Trading(db.Model):
    __tablename__ = "trading_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    balance: Mapped[float] = mapped_column()
