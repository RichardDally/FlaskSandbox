from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
from flask_sandbox import db
from flask_sandbox.models import Trading, User

trading_bp = Blueprint(
    name="trading",
    import_name=__name__,
    template_folder="templates",
)


@trading_bp.route('/balance')
@login_required
def balance():
    with current_app.app_context():
        q = db.session.query(User, Trading).filter(User.email == current_user.email).filter(User.id == Trading.user_id).first()
        if q:
            balance = q[1].balance
            current_app.logger.info(f"current_user={User.name} balance={balance}")
            return render_template('trading/stock.html', balance=balance)

        current_app.logger.critical(q)
        return render_template('trading/stock.html', balance="N/A")
