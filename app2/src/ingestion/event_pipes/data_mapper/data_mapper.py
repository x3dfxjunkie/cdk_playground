from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

import base64
import binascii
import json
import xmltodict
import xml

from aws_lambda_powertools import Logger

from app.src.utils.helpers.dict_lookup import dict_lookup
from app.src.ingestion.event_pipes.utils.data_contract_utils import DataContractNotFoundException


class PayloadParsingError(Exception):
    """Custom exception for when a payload can't be properly parsed"""


class IngestionDataMapper(ABC):
    _type: str = "default"

    def __init__(self, data_contract_mappings: Dict[str, Any]):
        self.data_contract_mappings = data_contract_mappings

    @classmethod
    def _get_all_subclasses(cls):
        subclasses = set(cls.__subclasses__())
        for subclass in list(subclasses):
            subclasses |= set(subclass._get_all_subclasses())
        return subclasses

    @classmethod
    def get_data_mapper(cls, _type: str) -> "IngestionDataMapper":
        return next(sub for sub in cls._get_all_subclasses() if sub._type == _type)

    @abstractmethod
    def parse_payload(self, payload: str, logger: Logger) -> Dict[str, Any]:
        pass

    @abstractmethod
    def _match_data_to_contract(self, obj: dict) -> Optional[Dict[str, Any]]:
        pass

    def match_data_to_contract(self, obj: dict) -> Dict[str, Any]:
        if not (matched_contract := self._match_data_to_contract(obj)):
            raise DataContractNotFoundException(
                "The data in the payload does not match with any existing data contract."
            )
        return matched_contract


class ParserMixin(ABC):
    def parse_payload(self, payload: str, logger: Logger) -> Dict[str, Any]:
        """
        All data coming from kinesis streams will be b64 encoded, so we have a method for decoding it,
        then passing it to another method which does the real parsing
        """
        b64_decoded_payload = base64.b64decode(payload).decode("utf-8")
        return self._parse_payload(b64_decoded_payload, logger)

    @abstractmethod
    def _parse_payload(self, payload: str, logger: Logger) -> Dict[str, Any]:
        pass


class JSONParserMixin(ParserMixin):
    def _parse_payload(self, payload: str, logger: Logger) -> Dict[str, Any]:
        try:
            data = json.loads(payload)
            return data
        except (binascii.Error, json.decoder.JSONDecodeError) as exception_info:
            logger.exception("Failed to decode payload")
            raise PayloadParsingError("Failed to decode data") from exception_info


class XMLParserMixin(ParserMixin):
    def _parse_payload(self, payload: str, logger: Logger) -> Dict[str, Any]:
        try:
            return xmltodict.parse(payload)
        except xml.parsers.expat.ExpatError as exception_info:
            logger.exception("Failed to decode payload")
            raise PayloadParsingError("Failed to decode data") from exception_info


class NestedDataMapper(JSONParserMixin, IngestionDataMapper):
    """
    Nested - the expectation is we have a key path defined in the configuration which tells us how to identify the matching contract
    """

    _type: str = "nested"

    def _match_data_to_contract(self, obj: dict) -> Optional[Dict[str, Any]]:
        configs = self.data_contract_mappings.get("data_contracts", [])
        for config in configs:
            for i in range(len(config["key_path"])):
                key_name_value = dict_lookup(obj, config["key_path"][i]["name"])
                key_value = dict_lookup(config, f"key_path.{i}.value")
                if key_name_value == key_value:
                    return config


class SingletonDataMapper(JSONParserMixin, IngestionDataMapper):
    """
    Simple - there's only one contract to match all payloads, so just return that
    """

    _type: str = "singleton"

    def _match_data_to_contract(self, obj: dict) -> Optional[Dict[str, Any]]:
        configs = self.data_contract_mappings.get("data_contracts", [])
        return next(iter(configs), None)


class WrappedDataMapper(NestedDataMapper):
    """
    A more complex data mapper which performs nested matching, but additionally has to load a stringified json field
    """

    _type: str = "wrapped"

    def _parse_payload(self, payload: str, logger: Logger) -> Dict[str, Any]:
        parsed_payload = super()._parse_payload(payload, logger)
        key_to_load = self.data_contract_mappings.get("key_to_load")
        try:
            parsed_payload[key_to_load] = json.loads(parsed_payload[key_to_load])
            return parsed_payload
        except (KeyError, TypeError) as e:
            # dude, where's my parse (key)
            raise PayloadParsingError(f"Error when loading key_to_load {key_to_load}") from e


class NestedXMLDataMapper(XMLParserMixin, NestedDataMapper):
    _type: str = "nested-xml"
