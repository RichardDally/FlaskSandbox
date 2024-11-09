from flask import Blueprint, render_template
from flask_login import login_required, current_user


files_bp = Blueprint(
    name="files",
    import_name=__name__,
    template_folder="templates",
)


@files_bp.route('/upload')
@login_required
def upload():
    return render_template('files/upload.html', name=current_user.name)
