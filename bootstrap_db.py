from flask_sandbox import db, create_app

# pass the create_app result so Flask-SQLAlchemy gets the configuration.
db.create_all(app=create_app())
