"""Feature flag yaml interface"""
import logging
import os
from typing import Any, Dict

import yaml

from app.src.utils.helpers.dict_lookup import dict_lookup
from app.src.utils.feature_flag.feature_flag_abstract import FeatureFlagInterface

logging.basicConfig(level=logging.INFO)


class FeatureFlagYAMLInterface(FeatureFlagInterface):
    """
    YAMl interface for feature flags. This class give the ability to turn on and off features using a yaml file.
    """

    def get_config(self, environment: str, yaml_path: str) -> Dict[str, Any]:
        """Parse yaml config file into a dictionary

        Args:
            environment (str): This should be a valid environment name. example: local, latest, load, stage or prod
            yaml_path (str): key path to a feature in the form of a object path. Example: pattern_instances.resources.kinesis.kinesis_firehose.enabled

        Returns:
            Dict[str, Any]: dictionary of all key/value pairs in the yaml config path.
        """
        directory = os.path.dirname(os.path.realpath(__file__))
        internal_yaml_path = f"{directory}/configs/{environment}-infra-feature-flags.yaml"

        if yaml_path:
            internal_yaml_path = yaml_path
        with open(
            internal_yaml_path,
            "r",
            encoding="utf-8",
        ) as infra_feature_flags:
            infra_feature_flags_config = yaml.unsafe_load(infra_feature_flags)  # this is linked to unsafe load issue in the repo
            return infra_feature_flags_config

    def resolve_dependences(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Not implemented

        Args:
            config (Dict[str, Any]): ""

        Returns:
            Dict[str, Any]: ""
        """

        # TODO: implement dependence resolution to help track co dependant resources
        # - Need to make sure a object is not dependant on it self
        # - Check to see if turning off a feature will have a effect on another resource
        return {}

    def is_feature_enabled(self, environment: str, key_path: str, yaml_path: str) -> bool:
        """Validates if a feature is enabled

        Args:
            environment (str):This should be a valid environment name. example: local, latest, load, stage or prod
            feature_key_path (str): key path to a feature in the form of a object path. Example: pattern_instances.resources.kinesis.kinesis_firehose.enabled
            yaml_path (str): Path to the yaml file with the feature definitions.



        Returns:
            bool: Return true or false based on if a feature is enabled are not
        """
        config: Dict[str, Any] = self.get_config(environment, yaml_path)
        logging.debug("feature config: %s", config)
        key_path = f"{key_path}"
        is_feature_enable = dict_lookup(config, key_path)  # config[area][resource_type][name]
        logging.debug("Key used to lookup: %s", key_path)
        is_feature_enable_type = type(is_feature_enable)

        if is_feature_enable_type != bool:
            raise TypeError(f"The object provided is of type {is_feature_enable_type}. Please provide a boolean!")

        return bool(is_feature_enable)
