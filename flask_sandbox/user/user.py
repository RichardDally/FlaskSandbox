from flask import Blueprint, render_template
from flask_login import login_required, current_user

user_bp = Blueprint(
    name="user",
    import_name=__name__,
    template_folder="templates",
)


@user_bp.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html', name=current_user.name)
