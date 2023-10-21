""" OIDC configuration for MyID Authentication """
import os

from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import write_file
from flask import Blueprint, abort
from flask_oidc import OpenIDConnect, g
from functools import wraps

oidc_client_bp = Blueprint("oidc_client_bp", __name__)
oidc = OpenIDConnect()


def get_oidc_json() -> dict:
    """
    Create OIDC client URL's for OIDC authentication.
    Returns: OIDC client dictionary.

    """
    oidc_client = {
        "web": {
            "client_id": os.getenv("OIDC_CLIENT_ID"),
            "client_secret": os.getenv("OIDC_CLIENT_SECRET"),
            "auth_uri": f"{os.getenv('OIDC_AUTH_URI')}/as/authorization.oauth2",
            "token_uri": f"{os.getenv('OIDC_AUTH_URI')}/as/token.oauth2",
            "issuer": f"{os.getenv('OIDC_AUTH_URI')}",
            "userinfo_uri": f"{os.getenv('OIDC_AUTH_URI')}/idp/userinfo.openid",
            "token_introspection_uri": f"{os.getenv('OIDC_AUTH_URI')}/as/introspect.oauth2",
        }
    }
    return oidc_client


def get_oidc_config(secrets_path: str) -> dict:
    """
    Create OIDC configuration.
    Args:
        secrets_path: Path where the secrets are stored.

    Returns: OIDC configuration dictionary.

    """
    oidc_config = {
        "SECRET_KEY": os.getenv("OIDC_CRYPTO_PASSPHRASE"),
        "OIDC_SCOPES": ["openid", "profile"],
        "OIDC_CLIENT_SECRETS": secrets_path,
    }
    return oidc_config


def initialize_oidc_config() -> dict:
    """
    Initialize the OIDC client by writing the secrets file.
    Returns: OIDC configuration dictionary.

    """
    file = get_oidc_json()
    path = f"{os.getenv('OIDC_JSON_PATH')}/oidc_client.json"
    write_file(file, path)
    return get_oidc_config(path)


def require_keystone_role(required_roles: list):
    """
    Function to check for a KeyStone client role in JWT access token.
    This is intended to be replaced with a more generic 'require this value
    in token or claims' system, at which point backwards compatibility will
    be added.
    """

    def wrapper(view_func):
        @wraps(view_func)
        def decorated(*args, **kwargs):
            if "roles" in g.oidc_id_token and set(required_roles).intersection(set(g.oidc_id_token["roles"])):
                return view_func(*args, **kwargs)
            else:
                return abort(403)

        return decorated

    return wrapper


@oidc_client_bp.route("/oidc_callback")
@oidc.require_login
def oidc_callback():
    return {"message": "LOGGED IN"}


@oidc_client_bp.route("/logout")
@oidc.require_login
def logout():
    oidc.logout()
    return {"message": "LOGGED OUT"}


@oidc_client_bp.before_request
def refresh_token():
    oidc.authenticate_or_redirect()
