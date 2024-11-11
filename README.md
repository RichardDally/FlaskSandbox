# Flask Sandbox

Experiment `Flask` with various features (e.g. authentication)

## Start web server

Create `.env` to use in-memory database for local testing
````ini
SQLALCHEMY_DATABASE_URI=sqlite:///:memory:
````

Bootstrap virtual environment with `uv`
````commandline
uv venv
venv\Scripts\activate
uv pip install -r requirements.txt
flask --app flask_sandbox run
````

## Bulma template gallery

https://bulmatemplates.github.io/bulma-templates/
