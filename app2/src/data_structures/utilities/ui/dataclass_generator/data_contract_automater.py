""" Automated Data Contract Landing Page"""
import os
import awsgi
import sample_load
import ddl_extractor
import s3_extractor
import secrets
from flask import Flask, render_template, url_for
from config import error, oidc_client
from utils.apigw_utils import add_prefix_to_path
from flask_wtf.csrf import CSRFProtect

app = Flask(
    __name__,
    template_folder="templates/",
    static_folder="static/",
)
# Generate a random 24-character secret key
secret_key = secrets.token_hex(24)
app.config["SECRET_KEY"] = secret_key
csrf = CSRFProtect()
csrf.init_app(app)

app.register_blueprint(error.error_bp)
app.register_blueprint(oidc_client.oidc_client_bp)
app.register_blueprint(sample_load.sample_load_bp)
app.register_blueprint(ddl_extractor.ddl_extractor_bp)
app.register_blueprint(s3_extractor.s3_extractor_bp)

stage: str | None = None


@app.context_processor
def utility_processor():
    def lambda_url_for(endpoint, **values):
        url = (
            add_prefix_to_path(url_for(endpoint, **values), stage) if stage is not None else url_for(endpoint, **values)
        )
        return url

    return {"lambda_url_for": lambda_url_for}


@app.route("/")
# @oidc.require_login
def index():
    """
    Home page for Auto-Mater App.
    """
    return render_template("home.html")


def lambda_handler(event, context):
    global stage
    if stage is None:
        stage = str(event["requestContext"]["stage"])
    return awsgi.response(app, event, context, base64_content_types={"*/*"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
