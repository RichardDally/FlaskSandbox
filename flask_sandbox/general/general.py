from flask import Blueprint, render_template


general_bp = Blueprint(
    name="general",
    import_name=__name__,
    template_folder="templates",
)


@general_bp.route('/')
def index():
    return render_template("general/index.html")
