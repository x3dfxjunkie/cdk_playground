"""
    Class Virtual User Utils
"""

import boto3
import json
import yaml
from typing import Dict, Union, Optional


class VirtualUserUtils:
    """
    A utility class providing methods for Virtual Users Class
    """

    sec_manager_template = {
        "dms": {
            "password": str,
            "dbname": str,
            "engine": str,
            "port": int,
            "dbInstanceIdentifier": str,
            "host": str,
            "username": str,
        }
        # add here future templates e.g. messaging
    }

    @staticmethod
    def validate_secret(secret_data: Dict[str, Union[str, int]], pattern_type: str) -> bool:
        """
        Validates the provided secret data against the specified pattern type.

        Args:
        - secret_data (Dict[str, Union[str, int]]): The secret data to validate.
        - pattern_type (str): The type of the pattern template to validate against.

        Returns:
        - bool: True if the secret data matches the pattern type template, otherwise False.

        Raises:
        - ValueError: If the pattern type is not defined.
        """
        if pattern_type not in VirtualUserUtils.sec_manager_template:
            raise ValueError(f"Pattern type {pattern_type} is not defined.")

        template = VirtualUserUtils.sec_manager_template[pattern_type]

        for key, val_type in template.items():
            if key not in secret_data or not isinstance(secret_data[key], val_type):
                return False

        if set(secret_data.keys()) - set(template.keys()):
            return False

        return True

    @staticmethod
    def get_secret(secret_identifier: Union[str], pattern_type: Optional[str] = None) -> Dict[str, Union[str, int]]:
        """
        Fetches and returns the secret value from AWS Secrets Manager given a secret identifier.
        Optionally, validates the fetched secret against a pattern type in case don't use a template

        Args:
        - secret_identifier (Union[str]): The unique identifier of the secret in AWS Secrets Manager.
        - pattern_type (Optional[str]): Optional pattern type to validate the fetched secret against.

        Returns:
        - Dict[str, Union[str, int]]: The parsed secret data.

        Raises:
        - ValueError: If the fetched secret does not have a "SecretString" field or does not match the expected template.
        """
        client = boto3.client("secretsmanager")
        response = None

        try:
            response = client.get_secret_value(SecretId=secret_identifier)
        except Exception as e:
            print(f"Error retrieving secret: {e}")
            return {}

        if "SecretString" in response:
            secret_data = json.loads(response["SecretString"])

            if pattern_type and not VirtualUserUtils.validate_secret(secret_data, pattern_type):
                raise ValueError(
                    f"The fetched secret does not match the expected template for pattern type {pattern_type}."
                )

            return secret_data
        else:
            raise ValueError("The secret does not have a SecretString field.")

    @staticmethod
    def get_config(
        pattern_type: str,
        key_config_name: str,
        path="app/src/load_testing/app/virtual_users/system_tests/system_test_config.yaml",
    ) -> dict:
        """
        Load the YAML file and retrieve configurations based on the given pattern_type and key_config_name.

        Args:
        path (str): Path to the YAML configuration file. Default path is set to the location specified.
        pattern_type (str): Section in the YAML to navigate based on.
        key_config_name (str): Key in the section to retrieve configurations from.

        Returns:
        dict: Dictionary containing the configurations from the specified section in the YAML.

        Raises:
        KeyError: If the specified pattern_type or key_config_name is not found in the YAML configuration.

        """
        with open(path, "r") as file:
            config = yaml.safe_load(file)

        try:
            return config["pattern"][pattern_type][key_config_name]
        except KeyError as exc:
            raise KeyError(
                f"No configuration found for pattern type: {pattern_type} and key config name: {key_config_name}"
            ) from exc

    @staticmethod
    def get_parameter(parameter_name: Union[str]) -> Union[str, None]:
        """Returns a parameter store string giving the parameter name
        Args:
        - parameter_name (Union[str]): The unique identifier of the parameter in AWS paramter store.
        Returns:
        - Union[str, None]: the value of the parameter store as string."""

        client = boto3.client("ssm")
        response = None

        try:
            response = client.get_parameter(Name=parameter_name)
            return response["Parameter"]["Value"]

        except Exception as e:
            print(f"Error retrieving parameter: {e}")
            return None
