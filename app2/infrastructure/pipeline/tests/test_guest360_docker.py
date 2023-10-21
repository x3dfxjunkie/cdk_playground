"""
Tests for Guest360Alarm
"""
import logging
import yaml
import json
from pathlib import Path
import os

import pytest
import aws_cdk
from aws_cdk import assertions

from app.infrastructure.pipeline.guest360_docker import Docker
from app.guest360_constructs.tests.utils import print_template_on_debug

logger = logging.getLogger(__name__)

APP_FOLDER = Path(__file__).parents[3]
CDK_JSON = APP_FOLDER / "cdk.json"
DEFAULT_CONTEXT = json.load(CDK_JSON.open())["context"]
TEST_STACK_ID = "TestDockerStack"
CDK_ENV = aws_cdk.Environment(account="123456789", region="us-east-1")
AWS_ECR_REPOSITORY = "AWS::ECR::Repository"

DOCKER_REPO_COUNTS = {
    "analyticsengineering": 1,
    "infrastructure": 1,
    "ingestion": 3,
    "loadtesting": 1,
    "otel": 1,
}

DOCKER_GITHUB_LABELS = [
    "Docker",
    "Docker/AnalyticsEngineering",
    "Docker/Infrastructure",
    "Docker/Ingestion",
    "Docker/LoadTesting",
    "Docker/Otel",
]


@pytest.mark.parametrize("environment", ["local", "latest", "stage", "load", "prod"])
def test_docker_stack(environment):
    """
    Basic instantiation - no alarm action attached
    """
    test_context = {
        **DEFAULT_CONTEXT,
        "environment": environment,
        "region": "us-east-1",
        "is_static_env": True,
        "github_pr_labels": json.dumps(DOCKER_GITHUB_LABELS),
    }
    file_path = os.path.realpath(__file__)
    environment_config_dir = Path(file_path).parents[3] / "configs"
    with (environment_config_dir / f"{environment}-environment.yaml").open() as file:
        environment_config = yaml.safe_load(file)
    test_app = aws_cdk.App(context=test_context)
    docker_stack = Docker(
        test_app,
        f"{TEST_STACK_ID}",
        environment_config=environment_config,
        env=CDK_ENV,
    )
    expected_docker_build_stack_count = 5  # Total number of workstream docker stacks (folders) expected
    docker_build_stack_count = 0
    for child in docker_stack.node.children:
        if isinstance(child, aws_cdk.Stack) and "docker" in child.stack_name:
            docker_build_stack = child
            docker_stack_name = docker_build_stack.stack_name
            docker_build_stack_count += 1
            logger.debug(f"Testing Docker Stack...")
            logger.debug(f"Docker Stack {docker_build_stack_count} of {expected_docker_build_stack_count}")
            logger.debug(f"Docker Stack Name: {docker_stack_name}")
            template = assertions.Template.from_stack(docker_build_stack)
            for docker_repo_substring, docker_repo_count in DOCKER_REPO_COUNTS.items():
                if docker_repo_substring in docker_stack_name:
                    template.resource_count_is(AWS_ECR_REPOSITORY, docker_repo_count)

            print_template_on_debug(
                template,
                logger,
                print_type="yaml",
                include_resource_types=[AWS_ECR_REPOSITORY],
            )
        elif isinstance(child, aws_cdk.Stack) and environment == "prod":
            template = assertions.Template.from_stack(child)
            template.resource_count_is("AWS::ECR::RegistryPolicy", 1)
            print_template_on_debug(
                template,
                logger,
                print_type="yaml",
                include_resource_types=["*"],
            )
        else:
            logger.debug(f"Skipping child type {child}...")
    assert docker_build_stack_count == expected_docker_build_stack_count
