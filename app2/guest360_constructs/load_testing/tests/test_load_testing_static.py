"""test for dms replication instance construct
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
from app.guest360_constructs.load_testing.static.load_testing_static import LoadTestingStatic
from aws_cdk import assertions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.fixture
def props() -> Dict[str, Any]:
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
                    "service_name": "rabbitmq",
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


@pytest.mark.timeout(30, method="signal")
def test_loadtest_static_stack_created(props: Dict[str, Any], environment_config, test_stack, lambda_assets):
    LoadTestingStatic(test_stack, "test-loadtest-static", props, environment_config)
    template = assertions.Template.from_stack(test_stack)
    template.resource_count_is("AWS::Lambda::Function", 9)
    template.resource_count_is("AWS::IAM::Role", 5)
    template.resource_count_is("AWS::DynamoDB::Table", 2)
    template.resource_count_is("AWS::KMS::Key", 3)
    template.has_resource_properties(
        "AWS::DynamoDB::Table", {"PointInTimeRecoverySpecification": {"PointInTimeRecoveryEnabled": True}}
    )
