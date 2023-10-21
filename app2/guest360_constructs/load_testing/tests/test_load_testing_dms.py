"""test for kinesis2kinesis instance construct
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
from app.guest360_constructs.load_testing.load_testing_dms import LoadTestingDmsRdsIngest
from app.guest360_constructs.load_testing.static.load_testing_static import LoadTestingStatic
from aws_cdk import assertions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.fixture
def props() -> Dict[str, Any]:
    load_test_props = {
        "execute_system_test_rds_dms": {
            "name": "execute_system_test_rds_dms",
            "description": "system test rds statemachine",
            "definition_file": "execute_system_test_rds_dms.yaml",
            "iam": {
                "role_name": "execute_rds_dms_stepfunction_role",
                "description": "Statemachine dms_rds role",
            },
            "step_function_parameters": {"limit_records": "100"},
        }
    }
    return load_test_props


@pytest.fixture
def load_test_props() -> Dict[str, Any]:
    iam_role = {
        "assumed_by": aws_cdk.aws_iam.ServicePrincipal("ec2.amazonaws.com"),
        "role_name": "test_role",
        "description": "Test IAM Role",
    }

    networking = {
        "vpc_id": None,
        "is_default": True,
        "allowlist": {
            "ingress": {"cidrs": ["0.0.0.0/8"], "ports": [8080]},
            "egress": {"cidr": ["0.0.0.0/8"], "ports": [-1]},
        },
        "blocklist": {},
    }

    s3_props = {"bucket_name": "test-rabbit-mq-fail-bucket"}

    load_test_props = {
        "cluster_name": "load-testing",
        "dynamo_db": [
            {"table_name": "guest360-load-testing-static-sfn-exec-state", "partition_key": "execution_name"},
            {
                "table_name": "guest360-load-testing-static-sfn-exec-eval",
                "partition_key": "execution_name",
                "sort_key": "test_case_record_name",
            },
        ],
        "ecs": {
            "memory_mib": "30720",
            "cpu_limitmb": "4096",
            "networking": networking,  #'pragma: allowlist secret'
            "secret_name": "local-pytest",  #'pragma: allowlist secret'
            "ecr": {"repository_name": "lst-use1-repository"},
            "iam": iam_role,
            "s3": s3_props,
            "services": [
                {
                    "service_name": "queue_1",
                    "image_tag": "",
                    "environment": {"env_var_1": "value_1"},
                    "command": ["test"],
                    "desired_count": 1,
                    "cloudmap": True,
                }
            ],
        },
    }
    return load_test_props


@pytest.fixture
def load_test_static(
    load_test_props: Dict[str, Any], environment_config, lambda_assets, test_stack
) -> LoadTestingStatic:
    return LoadTestingStatic(test_stack, "test-loadtest-static", load_test_props, environment_config)


@pytest.mark.timeout(30, method="signal")
def test_loadtest_stack_dms_rds_created(
    props: Dict[str, Any], environment_config, lambda_assets, test_stack, load_test_static
):
    LoadTestingDmsRdsIngest(
        test_stack, "test-loadtest-dms", props, environment_config, load_test_static, dms_stack_extension=["test"]
    )
    template = assertions.Template.from_stack(test_stack)
    logger.debug(json.dumps(template.to_json(), indent=2))
    template.resource_count_is("AWS::IAM::Role", 6)
    template.resource_count_is("AWS::StepFunctions::StateMachine", 1)
