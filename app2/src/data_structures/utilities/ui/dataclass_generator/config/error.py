""" Error page configuration and error handlers """
from flask import Blueprint, render_template, current_app

error_bp = Blueprint(
    "error_bp",
    __name__,
    template_folder="/dataclass-app/templates/",
    static_folder="/dataclass-app/static/",
)


@error_bp.app_errorhandler(400)
def bad_request(error):
    current_app.logger.error(error)
    return render_template("error.html", error=error), 400


@error_bp.app_errorhandler(403)
def forbidden(error):
    current_app.logger.error(error)
    return render_template("error.html", error=str(error).split(":")[1], message="Forbidden"), 403


@error_bp.app_errorhandler(404)
def not_found(error):
    current_app.logger.error(error)
    return render_template("error.html", error=error), 404


@error_bp.app_errorhandler(500)
def internal_server_error(error):
    current_app.logger.error(error)
    return render_template("error.html", error=error, message="Please, contact support."), 500
