from flask_sandbox import create_app, db
from flask_sandbox.models import Trading, User


app = create_app()
with app.app_context():
    user = User(name="test", email="test@test.com", password="test")
    trading = Trading(balance=0.0, user=user)
    db.session.add(user)
    db.session.add(trading)

    user = User(name="richard", email="richard@test.com", password="test")
    trading = Trading(balance=1000.0, user=user)
    db.session.add(user)
    db.session.add(trading)
    db.session.commit()

    q = db.session.query(User, Trading).filter(User.email == "richard@test.com").filter(User.id == Trading.user_id).first()
    print(f"name={q[0].name} balance={q[1].balance}")
