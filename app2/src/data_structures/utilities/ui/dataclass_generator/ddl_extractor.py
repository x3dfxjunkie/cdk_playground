""" Automated Data Contract """
import os
import json
import pyairtable

from pyairtable.formulas import match
from flask import Blueprint, render_template, request, send_file
from config import error, oidc_client
from app.src.data_structures.utilities.ui.dataclass_generator.ui_scripts.ddl_extractor import DDLExtractor

ddl_extractor_bp = (
    Blueprint(
        "ddl_extractor_bp",
        __name__,
        # template_folder="/dataclass-app/templates/",
        # static_folder="/dataclass-app/static/",
        # for aws deployment
        template_folder="app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
    if os.environ.get("AWS_LAMBDA_FUNCTION_NAME")
    else Blueprint(
        "ddl_extractor_bp",
        __name__,
        template_folder="/dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="/dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
    if os.environ.get("ENVIRONMENT") == "DOCKER"
    else Blueprint(
        "ddl_extractor_bp",
        __name__,
        template_folder="/workspace/app/src/data_structures/utilities/ui/dataclass_generator/templates/",
        static_folder="/workspace/app/src/data_structures/utilities/ui/dataclass_generator/static/",
    )
)
ddl_extractor_bp.register_blueprint(oidc_client.oidc_client_bp)
ddl_extractor_bp.register_blueprint(error.error_bp)


@ddl_extractor_bp.route("/ddl-extractor")
# @oidc.require_login
def ddl_extractor():
    """
    Index page for Auto-Mater App.
    Returns:
        Template: Index HTML template.
    """
    ddl_ext = DDLExtractor(pyairtable_api=pyairtable)
    ddl_ext.init_airtable_api()
    conn_ids = sorted(ddl_ext.get_connection_ids())
    return render_template("ddl_extractor.html", conn_ids=conn_ids)


@ddl_extractor_bp.route("/ddl-extractor/all-contracts", methods=["POST"])
# @oidc.require_login
def all_contracts():
    """
    Generates data contracts from all tables in database and returns a Zip file with them.
    Returns:
        Zip file string.
    """
    ddl_ext = DDLExtractor(json.loads(request.get_data()), pyairtable)
    # send_file() flask function  needs to be ignored by Sonarqube.
    # There is an open jira ticket due outdated Flask version in Sonarqube.
    # https://sonarsource.atlassian.net/browse/SONARPY-1131
    return send_file(
        ddl_ext.get_all_contracts_zip(),
        as_attachment=True,
        mimetype="application/zip",
        download_name="data_contracts.zip",
    )  # NOSONAR


@ddl_extractor_bp.route("/ddl-extractor/database", methods=["POST"])
# @oidc.require_login
def database_auth():
    """
    Index page for Auto-Mater App.
    Returns:
        Template: Index HTML template.
    """
    try:
        ddl_ext = DDLExtractor(json.loads(request.get_data()), pyairtable)
        return ddl_ext.get_tables()
    except Exception as e:
        return {"message": str(e)}, 500
