from pathlib import Path
from flask import Blueprint, render_template, request, flash, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


files_bp = Blueprint(
    name="files",
    import_name=__name__,
    template_folder="templates",
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@files_bp.route('/upload', methods=["GET", "POST"])
@login_required
def upload():
    if request.method == 'POST':

        if 'file' not in request.files:
            error: str = "There is no uploaded file"
            current_app.logger.debug(error)
            flash(error)
            return render_template('files/upload.html', error=error)
        file = request.files['file']

        if file.filename == '':
            error: str = "No file has been selected"
            current_app.logger.info(error)
            flash(error)
            return render_template('files/upload.html', error=error)

        if file and allowed_file(file.filename):
            upload_folder: str = current_app.config['UPLOAD_FOLDER']
            current_app.logger.info(f"Uploading filename={file.filename} to upload_folder={upload_folder}")
            filename: str = secure_filename(file.filename)
            file.save(str(Path(upload_folder, filename)))
            return render_template(
                'files/upload.html',
                info=f"{filename} has been successfully uploaded !"
            )
    return render_template('files/upload.html')
