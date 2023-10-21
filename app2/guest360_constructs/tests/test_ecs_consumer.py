"""Modules required by the unit test of the ECS Constructor"""
import json
import logging
import sys

import aws_cdk
import pytest
from itertools import product
from aws_cdk import assertions, aws_iam

from app.guest360_constructs.ecs_consumer import Guest360ECS

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


IAM_ROLE = {
    "assumed_by": aws_iam.ServicePrincipal("ec2.amazonaws.com"),
    "role_name": "test_role",
    "description": "Test IAM Role",
}

NETWORKING = {
    "vpc_id": None,
    "is_default": True,
    "allowlist": {
        "ingress": {"cidrs": ["0.0.0.0/8"], "ports": [8080]},
        "egress": {"cidr": ["0.0.0.0/8"], "ports": [-1]},
    },
    "blocklist": {},
}

S3_PROPS = {"bucket_name": "test-rabbit-mq-fail-bucket"}


def construct_local_environment_template(stack: aws_cdk.Stack) -> assertions.Template:
    props = {
        "secret_name": "local-pytest",  # 'pragma: allowlist secret'
        "image_url": "",
        "memory_mib": "1024",
        "cpu_limitmb": "1024",
        "ecr": {"repository_name": "test_repository"},
        "iam": IAM_ROLE,
        "networking": NETWORKING,
        "s3": S3_PROPS,
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
    }
    cluster = Guest360ECS(stack, "test-ecs", props)

    monitoring_props = {
        "cpu_alarm": {
            "custom_sns_alarm_topic_name": "wdpr-guest360-dev-snow-pri4",  # Suscribed to SNOW and Chatbot
            "alarm_description": "WARNING CPU Utilization Threshold Reached in wdpr-guest360-ecs-test-prefix-use1-test-ecs-queue_1-fs",
            "evaluation_periods": 3,
            "datapoints_to_alarm": 3,
            "threshold": 1,  # 1 CPU Unit
        },
        "memory_alarm": {
            "custom_sns_alarm_topic_name": "wdpr-guest360-dev-snow-pri4",  # Suscribed to SNOW and Chatbot
            "alarm_description": "WARNING Memory Utilization Threshold Reached in wdpr-guest360-ecs-test-prefix-use1-test-ecs-queue_1-fs",
            "evaluation_periods": 3,
            "datapoints_to_alarm": 3,
            "threshold": 70,  # Percent Unit
        },
    }

    # coverage
    for service in cluster.fargate_services:
        cluster._set_monitoring(service.service_name, monitoring_props)  # pylint: disable=W0212

    template = assertions.Template.from_stack(stack)
    return template


def construct_static_environment_template(stack: aws_cdk.Stack) -> assertions.Template:
    props = {
        "secret_name": "local-pytest",  # 'pragma: allowlist secret'
        "image_url": "",
        "memory_mib": "1024",
        "cpu_limitmb": "1024",
        "ecr": {"repository_name": "test_repository"},
        "iam": IAM_ROLE,
        "networking": NETWORKING,
        "s3": S3_PROPS,
        "monitoring": {
            "cpu_alarm": {
                "custom_sns_alarm_topic_name": "wdpr-guest360-dev-snow-pri4",  # Suscribed to SNOW and Chatbot
                "alarm_description": "WARNING CPU Utilization Threshold Reached in wdpr-guest360-ecs-test-prefix-use1-test-ecs-queue_1-fs",
                "evaluation_periods": 3,
                "datapoints_to_alarm": 3,
                "threshold": 1,  # 1 CPU Unit
            },
            "memory_alarm": {
                "custom_sns_alarm_topic_name": "wdpr-guest360-dev-snow-pri4",  # Suscribed to SNOW and Chatbot
                "alarm_description": "WARNING Memory Utilization Threshold Reached in wdpr-guest360-ecs-test-prefix-use1-test-ecs-queue_1-fs",
                "evaluation_periods": 3,
                "datapoints_to_alarm": 3,
                "threshold": 70,  # Percent Unit
            },
            "metric_period": 5,  # Minutes
            "metric_statistic": "Average",
        },
        "services": [
            {
                "service_name": "queue_1",
                "image_tag": "",
                "environment": {"env_var_1": "value_1"},
                "command": ["test"],
                "desired_count": 1,
                "cloudmap": True,
                "sidecar": {
                    "registry_repository_name": "public.ecr.aws/cloudwatch-agent/cloudwatch-agent",
                    "tag": "tag_test",
                    "port_mappings": [25888, 25889],
                    "environment": {"env_var_2": "value_2"},
                },
            }
        ],
    }
    Guest360ECS(stack, "test-ecs", props)

    template = assertions.Template.from_stack(stack)

    return template


def assert_all_expected_resources_in_static_environments(template: assertions.Template, constants):
    logger.debug(json.dumps(template.to_json(), indent=2))

    template.resource_count_is("AWS::IAM::Role", 4)
    template.resource_count_is("AWS::S3::Bucket", 1)
    template.resource_count_is("AWS::ECS::Cluster", 1)
    template.resource_count_is("AWS::ECS::TaskDefinition", 1)
    template.has_resource_properties(
        constants["AWSCWALARM"],
        {
            "ComparisonOperator": "LessThanThreshold",
            "EvaluationPeriods": 1,
            "DatapointsToAlarm": 1,
            "MetricName": "RunningTaskCount",
            "Namespace": "ECS/ContainerInsights",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 1,
            "Unit": "Count",
        },
    )
    template.has_resource_properties(
        constants["AWSCWALARM"],
        props={
            "ActionsEnabled": True,  # FYI Actions are not supported by ephemeral environments. For more info see Guest360Alarm construct
            "AlarmActions": ["arn:aws:sns:us-east-1:123456789:test-guest360-use1-alarm-notifications"],
            "AlarmDescription": "[SNOWAG:app-global-Guest360][SNOWCI:WDPR Guest360 - AWS Latest][SNOWDESC:Guest360ECSdf61e failed on CPUUtilization ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1]WARNING CPU Utilization Threshold Reached in wdpr-guest360-ecs-test-prefix-use1-test-ecs-queue_1-fs",
            "Dimensions": [
                {
                    "Name": "ClusterName",
                    "Value": {"Ref": "Guest360ECSdf61etestguest360use1testecsfargatecluster7FEC14EB"},
                },
                {
                    "Name": "ServiceName",
                    "Value": "test-guest360-use1-test-ecs-queue_1-fs",
                },
            ],
            "MetricName": "CPUUtilization",
        },
    )
    template.has_resource_properties(
        constants["AWSCWALARM"],
        props={
            "ActionsEnabled": True,  # FYI Actions are not supported by ephemeral environments. For more info see Guest360Alarm construct
            "AlarmActions": ["arn:aws:sns:us-east-1:123456789:test-guest360-use1-alarm-notifications"],
            "AlarmDescription": "[SNOWAG:app-global-Guest360][SNOWCI:WDPR Guest360 - AWS Latest][SNOWDESC:Guest360ECSdf61e failed on MemoryUtilization ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 70]WARNING Memory Utilization Threshold Reached in wdpr-guest360-ecs-test-prefix-use1-test-ecs-queue_1-fs",
            "Dimensions": [
                {
                    "Name": "ClusterName",
                    "Value": {"Ref": "Guest360ECSdf61etestguest360use1testecsfargatecluster7FEC14EB"},
                },
                {
                    "Name": "ServiceName",
                    "Value": "test-guest360-use1-test-ecs-queue_1-fs",
                },
            ],
            "MetricName": "MemoryUtilization",
        },
    )
    template.has_resource_properties(
        "AWS::ECS::TaskDefinition",
        props={
            "ContainerDefinitions": [
                {
                    "Command": ["test"],
                    "Environment": [
                        {"Name": "env_var_1", "Value": "value_1"},
                        {
                            "Name": "FAILED_MSG_BUCKET_NAME",
                        },
                    ],
                    "LogConfiguration": {
                        "Options": {
                            "awslogs-stream-prefix": "queue_1-log",
                            "awslogs-region": "us-east-1",
                        }
                    },
                    "Name": "test-guest360-use1-test-ecs-queue_1-consumer",
                    "PortMappings": [{"ContainerPort": 8080, "Protocol": "tcp"}],
                },
                {
                    "Environment": [{"Name": "env_var_2", "Value": "value_2"}],
                    "Image": "public.ecr.aws/cloudwatch-agent/cloudwatch-agent",
                    "LogConfiguration": {
                        "LogDriver": "awslogs",
                        "Options": {
                            "awslogs-stream-prefix": "queue_1-sidecar-log",
                            "awslogs-region": "us-east-1",
                        },
                    },
                    "Name": "test-guest360-use1-test-ecs-queue_1-sidecar",
                    "PortMappings": [
                        {"ContainerPort": 25888, "Protocol": "tcp"},
                        {"ContainerPort": 25889, "Protocol": "tcp"},
                    ],
                },
                {
                    "Environment": [{"Name": "AWS_REGION", "Value": "us-east-1"}],
                    "LogConfiguration": {
                        "LogDriver": "awslogs",
                        "Options": {
                            "awslogs-stream-prefix": "otel-sidecar-log",
                            "awslogs-region": "us-east-1",
                        },
                    },
                    "Name": "test-guest360-use1-test-ecs-queue_1-otel-sidecar",
                    "PortMappings": [
                        {"ContainerPort": 55679, "Protocol": "tcp"},
                        {"ContainerPort": 4317, "Protocol": "tcp"},
                        {"ContainerPort": 13133, "Protocol": "tcp"},
                    ],
                },
            ],
        },
    )


environment_deployment_controller_combos = product(["local", "latest", "stage", "load", "prod"], [True, False])


@pytest.mark.timeout(30, method="signal")
@pytest.mark.parametrize("environment,deployment_controller_disabled", environment_deployment_controller_combos)
def test_ecs_consumer_created(environment, deployment_controller_disabled, constants):
    test_app = aws_cdk.App()
    stack = aws_cdk.Stack(test_app, "TestStack", env=aws_cdk.Environment(account="123456789", region="us-east-1"))
    stack.node.set_context("environment", environment)
    stack.node.set_context("prefix", "test-guest360-use1")
    stack.node.set_context("prefix_global", "guest360-prefix")  # Emulating static guest360 environment.
    stack.node.set_context("region", "us-east-1")
    stack.node.set_context("stack_name", "test")

    # https://github.com/aws/aws-cdk/pull/22467
    stack.node.set_context(
        "@aws-cdk/aws-ecs:disableExplicitDeploymentControllerForCircuitBreaker", deployment_controller_disabled
    )

    match environment:
        case "local":
            template = construct_local_environment_template(stack)
            logger.debug(json.dumps(template.to_json(), indent=2))
            template.resource_count_is("AWS::IAM::Role", 3)
            template.resource_count_is("AWS::S3::Bucket", 2)
            template.resource_count_is("AWS::ECS::Cluster", 1)

        case ["latest", "stage", "load", "prod"]:
            template = construct_static_environment_template(stack)
            assert_all_expected_resources_in_static_environments(template, constants)
            if environment == "prod":
                template.has_resource_properties(
                    constants["AWSCWALARM"],
                    {
                        "ComparisonOperator": "LessThanThreshold",
                        "EvaluationPeriods": 1,
                        "DatapointsToAlarm": 1,
                        "MetricName": "IncomingLogEvents",
                        "Namespace": "AWS/Logs",
                        "Period": 300,
                        "Statistic": "Sum",
                        "Threshold": 1,
                    },
                )
