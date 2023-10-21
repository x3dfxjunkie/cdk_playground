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
from app.guest360_constructs.load_testing.kinesis.load_testing_kinesis_ingest import LoadTestingKinesisIngest
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
        "guest360_execute_all_system_test": {
            "name": "execute_all_load_test",
            "description": "main orchestrator statemachine",
            "definition_file": "execute_all_system_test.yaml",
            "iam": {
                "role_name": "execute_all_load_test_scenarios_stepfunction_role",
                "description": "Statemachine guest360_execute_all_load_test_scenarios role",
            },
            "step_function_parameters": {
                "guest360_execution_status_table": "",
                "guest360_execute_load_test_scenario_arn": "",
            },
        },
        "guest360_system_test_kinesis_ingest": {
            "name": "execute_system_test",
            "description": "system test executor statemachine",
            "definition_file": "execute_system_test_kinesis_ingest.yaml",
            "iam": {
                "role_name": "execute_system_test_scenarios_stepfunction_role",
                "description": "Statemachine guest360_system_test_scenarios role",
            },
            "step_function_parameters": {"limit_records": "500", "bucket_scenarios_name": ""},
        },
        "glue_job": {
            "job_name": "glue-s3-evaluator",
            "script": {
                "bucket": "load-testing",
                "prefix": "glue-jobs/latest/",
                "artifact_name": "glue_s3_evaluator.py",
            },
            "resources": {
                "buckets": {"ingestion": ["ingestion-raw"]},
                "dynamodb": ["guest360-load-testing-sfn-exec-eval"],
                "log_group": "glue-s3-evaluator/logs/",
            },
        },
        "lambda_ecs_calculator": {
            "function_name": "ecs-calculator-lambda",
            "description": "Locust ECS Calculator Lambda",
            "code_path": "bazel-bin/app/src/load_testing/ecs_calculator.zip",
            "lambda_handler": "lambda_function.lambda_handler",
            "allow_public_subnet": False,
            "timeout": 60,
        },
        "lambda_list_files_s3": {
            "function_name": "list_files_s3_lambda_name",
            "description": "Locust ECS Calculator Lambda",
            "code_path": "bazel-bin/app/src/load_testing/list_files_s3.zip",
            "lambda_handler": "lambda_function.lambda_handler",
            "allow_public_subnet": False,
            "timeout": 60,
        },
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
def test_loadtest_stack_k2k_created(
    props: Dict[str, Any], environment_config, lambda_assets, test_stack, load_test_static
):
    LoadTestingKinesisIngest(test_stack, "test-loadtest-k2k", props, environment_config, load_test_static)
    template = assertions.Template.from_stack(test_stack)
    logger.debug(json.dumps(template.to_json(), indent=2))
    template.resource_count_is("AWS::Lambda::Function", 8)
    template.resource_count_is("AWS::IAM::Role", 6)
    template.resource_count_is("AWS::StepFunctions::StateMachine", 2)
    template.resource_count_is("AWS::DynamoDB::Table", 2)
