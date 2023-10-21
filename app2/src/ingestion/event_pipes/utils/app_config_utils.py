"""Module for AWS AppConfig Logic"""
import requests
import json
from typing import Dict, Any


class AppConfigUrlErrorException(Exception):
    pass


def get_app_config_data(url_path: str, timeout: int) -> Dict[Any, Any]:
    """get AppConfig configuration data"""
    try:
        response = requests.get(url_path, timeout=timeout)  # type: ignore
        response.raise_for_status()
        return json.loads(response.content.decode("utf-8"))

    except Exception as err:
        raise AppConfigUrlErrorException(f"Error querying AWS AppConfig URL {url_path}") from err
