import json
import pytest
import os
from pathlib import Path
import aws_cdk

STACK_PATH = str(Path(os.getcwd()))
ENVIRONMENTS = ["latest"]
ENV_SHORT = {"latest": "lst", "stage": "stg", "prod": "prd", "load": "lod"}


def delete_files(file_list):
    for file in file_list:
        os.remove(file)


@pytest.fixture(params=ENVIRONMENTS)
def test_stack(request):
    environment = request.param
    test_app = aws_cdk.App()
    stack = aws_cdk.Stack(test_app, "TestStack", env=aws_cdk.Environment(account="123456789", region="us-east-1"))
    stack.node.set_context("region", "us-east-1")
    stack.node.set_context("stack_name", "test")
    stack.node.set_context("is_static_env", True)
    stack.node.set_context("is_local_test", True)
    stack.node.set_context("stack_path", STACK_PATH)
    stack.node.set_context("environment", environment)
    stack.node.set_context("prefix", f"{ENV_SHORT[environment]}-use1-guest360")
    stack.node.set_context("prefix_global", f"{ENV_SHORT[environment]}-guest360")
    stack.is_primary_region = lambda: True
    yield stack


@pytest.fixture
def lambda_assets(request):
    zip_files = []
    lambda_names = [
        "ecs_calculator",
        "list_files_s3",
        "evaluator",
        "sqs_validator",
        "init_rds_lambda",
        "send_s3_results",
        "evaluator_system_test",
        "consolidate_results",
        "sfn_executor",
        "eval_conditions_system_test",
        "get_app_config",
        "get_list_app_config",
        "rabbitmq_test",
        "rds_manager_lambda",
    ]
    permission_config = {
        "policies": [
            {
                "actions": ["kinesis:List*", "kinesis:PutRecord*", "kinesis:Get*", "kinesis:Describe*"],
                "resources": ["arn:aws:kinesis:us-*:000000000000:stream/*"],
            }
        ]
    }
    permissions_files = ["latest_ecs_role", "latest_lambda_role"]

    scheduled_config = {
        "environment": "local",
        "resources": {
            "rules": {
                "load_testing_rule": {
                    "description": "Rule",
                    "hour": "9",
                    "minute": "0",
                    "day": "*",
                    "week_day": "*",
                    "month": "*",
                    "year": "*",
                }
            }
        },
    }

    stack_path = STACK_PATH
    base_dir = Path(f"{stack_path}/bazel-bin/app/src/load_testing/")

    if not stack_path.startswith("/workspace/"):
        scheduled_path = Path(f"{stack_path}/scheduling/")
        os.makedirs(scheduled_path, exist_ok=True)

        with open(f"{scheduled_path}/latest-scheduling.yaml", "w") as file:
            json.dump(scheduled_config, file, indent=2)

        permission_path = Path(f"{stack_path}/permissions/")
        os.makedirs(permission_path, exist_ok=True)

        for i in permissions_files:
            permissions_file = f"{permission_path}/{i}.yaml"
            with open(permissions_file, "w") as json_file:
                json.dump(permission_config, json_file, indent=4)

    if not os.path.exists(base_dir):
        base_dir.mkdir(parents=True, exist_ok=True)

    empty_zip_data = b"PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    for i in lambda_names:
        lambda_file = f"{base_dir}/{i}.zip"
        with open(lambda_file, "wb") as zip_file:
            zip_file.write(empty_zip_data)
            zip_files.append(zip_file)

    def cleanup():
        delete_files([f"{base_dir}/{i}.zip" for i in lambda_names])
        os.rmdir(base_dir)

    request.addfinalizer(cleanup)

    yield zip_files


@pytest.fixture
def environment_config():
    environment_props = {
        "account": "000000000000",
        "networking": {
            "us-east-1": {
                "short_region": "use1",
                "vpc": {"id": "vpc-771156a5", "cidr": "0.0.0.0/8"},
                "subnets": {
                    "private": [
                        {"id": "subnet-e0e7bc90", "cidr": "0.0.0.0/8"},
                    ],
                    "non-routable": [
                        {"id": "subnet-e0e7bc90", "cidr": "0.0.0.0/16"},
                    ],
                },
                "endpoints": [{"id": "vpce-08900cd41ebaa4322", "service_name": "events", "type": "Interface"}],
            }
        },
        "short_env": "lcl",
    }

    return environment_props
