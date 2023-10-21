"""test for rds instance load-testing construct
"""
# pylint: disable=redefined-outer-name
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict

import aws_cdk
import pytest
from app.guest360_constructs.load_testing.load_testing_rds import LoadTestingRDS
from aws_cdk import assertions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.fixture
def props() -> Dict[str, Any]:
    load_test_props = {
        "rds": {
            "engine": aws_cdk.aws_rds.DatabaseInstanceEngine.MARIADB,
            "database_name": "db_load_testing",
            "iam_authentication": True,
        },
        "network_config": {"allowlist": {"ingress": {"cidrs": ["127.0.0.0/8"]}}},
    }
    return load_test_props


# @pytest.mark.skip(reason="skip this test if featureflag for RDS turned off")
@pytest.mark.timeout(30, method="signal")
def test_loadtest_rds_created(props, environment_config, test_stack, lambda_assets, constants):
    LoadTestingRDS(test_stack, "test-loadtest-rds", props, environment_config)
    template = assertions.Template.from_stack(test_stack)
    logger.debug(json.dumps(template.to_json(), indent=2))
    template.resource_count_is(constants["AWSLAMBDAFUNCTION"], 3)
    template.resource_count_is(constants["AWSIAMROLE"], 2)
    template.resource_count_is(constants["AWSKMSKEY"], 1)
    template.resource_count_is(constants["AWSDBINSTANCE"], 1)
    template.resource_count_is(constants["AWSSECURITYGROUP"], 3)
    template.resource_count_is(constants["AWSDBSUBNETGROUP"], 1)
