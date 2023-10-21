"""Utils for Lambda Function  data validation"""
import os
import hashlib
import importlib

from typing import Any, List, Dict
from pydantic import error_wrappers, parse_obj_as
import yaml

from aws_lambda_powertools import Logger

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
logger = Logger(service=__name__)


class DataContractNotFoundException(Exception):
    """Custom Exception for data not matching an existing data contract"""


class DataValidationError(Exception):
    """Custom exception for data not conforming to model"""

    def __str__(self) -> str:
        err = self.__cause__
        return type(err).__name__ + ":" + str(err)


def load_datacontract_mappings(file_name: str = "data_contract_mappings.yaml") -> List[Dict[str, Any]]:
    with open(
        f"{os.path.abspath(os.path.join(DIR_PATH, '../config'))}/{file_name}", "r", encoding="UTF-8"
    ) as datacontract:
        datacontract_mappings = yaml.safe_load(datacontract)
    return datacontract_mappings


def generate_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def validate_record_conforms_to_data_contract(config_object, data, logger):
    # Dynamically import the datacontract and parse it with the decoded data from the payload
    try:
        logger.info("config_object in pydantic_validation:%s", config_object)
        logger.debug("Data in pydantic_validation:%s", data)
        module = importlib.import_module(config_object["data_contract"])
        data_contract = getattr(module, config_object["class_name"])
        data_contract.update_forward_refs()
        parse_obj_as(data_contract, data)
        logger.info("Data was successfully parsed using pydantic.")
        return f"{config_object['data_contract']}.{config_object['class_name']}"
    except error_wrappers.ValidationError as err:
        raise DataValidationError from err
