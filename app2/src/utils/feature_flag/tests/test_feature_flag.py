"""feature flag test"""
import logging
import os

from app.src.utils.feature_flag.feature_flag import FeatureFlag

# import pytest


logging.basicConfig(level=logging.INFO)

environment = "local"
config_path = f"{os.path.dirname(os.path.realpath(__file__))}/configs/local-infra-feature-flags-test.yaml"


# Testing object with array
def test_freature_flag_yaml_with_array():
    with FeatureFlag(environment, "pattern_instances.0.resources.kinesis.kinesis_firehose.enabled", config_path) as kinesis_firehose_flag:
        assert kinesis_firehose_flag is False


def test_freature_flag_yaml_without_array():
    with FeatureFlag(environment, "feature_group.data_services_lambda_api_gateway_ll") as kinesis_firehose_flag:
        if kinesis_firehose_flag:
            assert kinesis_firehose_flag is True


test_freature_flag_yaml_without_array()
test_freature_flag_yaml_with_array()
