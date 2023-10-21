""" Automated Data Contract """
import os

from flask import Blueprint, render_template, request, current_app
from app.src.data_structures.utilities.ui.dataclass_generator.config import error
from app.src.data_structures.utilities.ui.dataclass_generator.ui_scripts.sample_load import (
    handle_s3_request,
)

s3_extractor_bp = (
    Blueprint(
        "s3_extractor_bp",
        __name__,
        # template_folder="/dataclass-app/templates/",
        # static_folder="/dataclass-app/static/",
        # for aws deployment
        template_folder="app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
    if os.environ.get("AWS_LAMBDA_FUNCTION_NAME")
    else Blueprint(
        "s3_extractor_bp",
        __name__,
        template_folder="/dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="/dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
    if os.environ.get("ENVIRONMENT") == "DOCKER"
    else Blueprint(
        "s3_extractor_bp",
        __name__,
        template_folder="/workspace/app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="/workspace/app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
)

s3_extractor_bp.register_blueprint(error.error_bp)


@s3_extractor_bp.route("/s3-extractor", methods=["GET"])
# @oidc.require_login
def s3_extractor():
    """
    Index page for Auto-Mater App.
    If there are any files to be processed, function will generate the data contract and return it to the template.
    Returns:
        Template: Index HTML template.
    """
    if not (s3_path := request.args.get("S3Location")):
        return render_template("s3_extractor.html")

    data_contract = handle_s3_request(s3_path)
    return render_template("s3_extractor.html", data_contract=data_contract)
