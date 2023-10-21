""" Automated Data Contract """
import os
import traceback

from flask import Blueprint, render_template, request, current_app
from app.src.data_structures.utilities.ui.dataclass_generator.config import error
from app.src.data_structures.utilities.ui.dataclass_generator.ui_scripts.sample_load import (
    get_data_contract,
    get_synthetic_data,
)

sample_load_bp = (
    Blueprint(
        "sample_load_bp",
        __name__,
        # template_folder="/dataclass-app/templates/",
        # static_folder="/dataclass-app/static/",
        # for aws deployment
        template_folder="app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
    if os.environ.get("AWS_LAMBDA_FUNCTION_NAME")
    else Blueprint(
        "sample_load_bp",
        __name__,
        template_folder="/dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="/dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
    if os.environ.get("ENVIRONMENT") == "DOCKER"
    else Blueprint(
        "sample_load_bp",
        __name__,
        template_folder="/workspace/app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="/workspace/app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
)
sample_load_interface = "sample_load.html"
sample_load_bp.register_blueprint(error.error_bp)


@sample_load_bp.route("/sample-load", methods=["GET"])
# @oidc.require_login
def sample_load():
    """
    Index page for Auto-Mater App.
    If there are any files to be processed, function will generate the data contract and return it to the template.
    Returns:
        Template: Index HTML template.
    """
    return render_template(sample_load_interface, environment=os.environ.get("ENVIRONMENT"))


@sample_load_bp.route("/sample-load/contract", methods=["POST"])
# @oidc.require_login
def get_contract():
    """
    Index page for Auto-Mater App.
    If there are any files to be processed, function will generate the data contract and return it to the template.
    Returns:
        Template: Index HTML template.
    """
    requested_files = request.files.getlist("file")
    data_contract, model_name = get_data_contract(requested_files)
    number_of_samples = 5
    synthetic_data = get_synthetic_data(data_contract, model_name, number_of_samples)
    return render_template(
        sample_load_interface,
        environment=os.environ.get("ENVIRONMENT"),
        data_contract=data_contract,
        synthetic_data=synthetic_data,
        model_name=model_name,
        quantity=number_of_samples,
    )


@sample_load_bp.route("/sample-load/refresh-samples", methods=["POST"])
# @oidc.require_login
def refresh_samples():
    """
    Index page for Auto-Mater App.
    If there are any files to be processed, function will generate the data contract and return it to the template.
    Returns:
        Template: Index HTML template.
    """
    number_of_samples = int(request.form.get("number_of_samples"))
    data_contract = request.form.get("data-contract-output-box")  # Get the value of the textarea
    model_name = request.form.get("model_name")  # Get the value of the textarea
    synthetic_data = get_synthetic_data(data_contract, model_name, number_of_samples)
    return render_template(
        sample_load_interface,
        environment=os.environ.get("ENVIRONMENT"),
        data_contract=data_contract,
        synthetic_data=synthetic_data,
        model_name=model_name,
        quantity=number_of_samples,
    )
