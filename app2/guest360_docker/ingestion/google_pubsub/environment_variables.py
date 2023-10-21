"""
"""

import boto3
from base64 import b64decode
from json import dumps, loads
from logging import info
from os import environ


def load_env_vars(env_vars: list, gac_filename: str = "gac_file.json") -> dict:
    env_vars_dict = dict()
    for variable in env_vars:
        if variable == "GOOGLE_APPLICATION_CREDENTIALS":
            # Getting the Google Application Credentials (gac) from secret
            gac_secret = get_aws_secret(environ["GOOGLE_APPLICATION_CREDENTIALS"], environ["REGION"])

            # Transforming the secret result into a json file
            convert_dict_to_json_file(gac_secret, gac_filename)

            # Updating the GOOGLE_APPLICATION_CREDENTIALS global variable
            environ["GOOGLE_APPLICATION_CREDENTIALS"] = gac_filename
            info("The environment variable GOOGLE_APPLICATION_CREDENTIALS has been properly overwritten.\n")

        # does not need an else because all vars should be part of os env vars
        env_vars_dict[variable.lower()] = environ[variable]

    return env_vars_dict


@staticmethod
def get_aws_secret(secret_name, region):
    """Returns the decoded secret value of a given secret name."""

    secretsmanager_client = boto3.client(service_name="secretsmanager", region_name=region)

    try:
        get_secret_value_response = secretsmanager_client.get_secret_value(SecretId=secret_name)
    except secretsmanager_client.exceptions.ClientError as e:
        if e.response["Error"]["Code"] in (
            "DecryptionFailureException",
            "InternalServiceErrorException",
            "InvalidParameterException",
            "InvalidRequestException",
            "ResourceNotFoundException",
        ):
            raise e
    else:
        if "SecretString" in get_secret_value_response:
            return get_secret_value_response["SecretString"]
        else:
            return b64decode(get_secret_value_response["SecretBinary"])


@staticmethod
def convert_dict_to_json_file(dict_object, file_name):
    """Writes a dict data type object into a json file"""

    # Transforming the dict object into a json object
    json_object = dumps(loads(dict_object))

    # Writing the file
    with open(file_name, "w", encoding="utf-8") as outfile:
        outfile.write(json_object)
