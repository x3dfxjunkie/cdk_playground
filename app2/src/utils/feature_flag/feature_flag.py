"""
Feature flag context decorator
https://github.com/aws/aws-cdk/issues/21250
"""
import logging
from contextlib import ContextDecorator

from app.src.utils.feature_flag.feature_flag_yaml_interface import FeatureFlagYAMLInterface

logging.basicConfig(level=logging.DEBUG)


class FeatureFlag(ContextDecorator):
    """This class gives users the ability to wrap a block of code into a Feature Flag context. Once the code is wrapped into the context, users can turn on and off the code block using a config value.
    Args:
        ContextDecorator (class): ContextDecorator base class
    """

    def __init__(self, environment: str, key_path: str, yaml_path: str = ""):
        """
        Args:
            environment (str): This should be a valid environment name. example: local, latest, load, stage or prod
            key_path (str): key path to a feature in the form of a object path. Example: pattern_instances.resources.kinesis.kinesis_firehose.enabled
            yaml_path (str): Path to the yaml file with the feature definitions
        """
        self.environment = environment
        self.key_path = key_path
        self.execute_feature = False
        self.yaml_path = yaml_path

    def __enter__(self):
        """This function is triggered when the feature flag context is called

        Returns:
            bool: return a true or false based on if a feature is enabled are not
        """
        feature_flag_interface = FeatureFlagYAMLInterface()
        self.execute_feature = feature_flag_interface.is_feature_enabled(
            self.environment, self.key_path, self.yaml_path
        )
        logging.debug("%s is enabled: %s", self.key_path, self.execute_feature)
        return self.execute_feature

    def __exit__(self, exc_type, exc, exc_tb):
        """This function is triggered up on the completion of the feature flag context

        Args:
            exc_type (_type_): Not used
            exc (_type_): Not used
            exc_tb (_type_): Not used
        """
        logging.debug("Exiting: %s", self.key_path)


def feature_flag(environment: str, feature_key_path: str, yaml_path: str = "") -> callable:
    """This function gives users the ability to wrap a function into a Feature Flag context. Once the function is wrapped into the context, users can turn on and off the code block using a config value.
    Args:
        environment (str):This should be a valid environment name. example: local, latest, load, stage or prod
        feature_key_path (str): key path to a feature in the form of a object path. Example: pattern_instances.resources.kinesis.kinesis_firehose.enabled
        yaml_path (str): Path to the yaml file with the feature definitions.

    Returns:
        callable: Callable object in the form of a function
    """
    with FeatureFlag(environment=environment, key_path=feature_key_path, yaml_path=yaml_path) as is_feature_flag:
        if is_feature_flag:

            def inner(func) -> callable:
                # need to have the ability to pass all params that are needed down to the wrapped function
                def wrapper(*args, **kwargs):
                    # calling wrapped function with params
                    func(*args, **kwargs)
                    logging.info("Running feature %s for %s", feature_key_path, func.__name__)

                return wrapper

            return inner
        else:

            def inner(func) -> callable:
                def wrapper(*args, **kwargs):
                    logging.info(
                        "skipping feature %s for %s with these params %s %s",
                        feature_key_path,
                        func.__name__,
                        args,
                        kwargs,
                    )

                return wrapper

            return inner
