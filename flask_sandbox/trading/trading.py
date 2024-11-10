from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
from flask_sandbox import db
from flask_sandbox.models import Trading


trading_bp = Blueprint(
    name="trading",
    import_name=__name__,
    template_folder="templates",
)


@trading_bp.route('/balance')
@login_required
def balance():
    with current_app.app_context():
        trading = db.session.execute(db.session.execute(db.select(Trading)))
    return render_template('trading/balance.html')
