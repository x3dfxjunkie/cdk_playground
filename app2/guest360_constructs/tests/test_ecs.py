"""test for messaging instance construct
"""
# pylint: disable=redefined-outer-name
import builtins
import json
import logging
import os
import sys

import aws_cdk
import pytest
import yaml
from app.guest360_constructs import ecs, iam_role
from aws_cdk import assertions, aws_ecr, aws_ecs, aws_iam
from test_helpers.print_template import print_template_on_debug

# set log levels for noisy calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

construct_id = "test-construct-id"


@pytest.mark.timeout(30, method="signal")
def test_cluster_with_props(singlestack):
    ecs.Guest360ECSCluster(singlestack, construct_id, props={"vpc": "test123"})
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])

    template.has_resource_properties(
        "AWS::ECS::Cluster", props={"ClusterSettings": [{"Name": "containerInsights", "Value": "enabled"}]}
    )


@pytest.mark.timeout(30, method="signal")
def test_cluster_with_kwargs(singlestack):
    ecs.Guest360ECSCluster(singlestack, construct_id, vpc="test123")
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])
    template.has_resource_properties(
        "AWS::ECS::Cluster", props={"ClusterSettings": [{"Name": "containerInsights", "Value": "enabled"}]}
    )


@pytest.mark.timeout(30, method="signal")
def test_cluster_missing_vpc(singlestack):
    cluster_name = "test_cluster_name"
    with pytest.raises(builtins.AttributeError):
        ecs.Guest360ECSCluster(singlestack, construct_id, cluster_name=cluster_name)


@pytest.mark.timeout(30, method="signal")
def test_cluster_vpc_wrong_type(singlestack):
    cluster_name = "test_cluster_name"
    with pytest.raises(builtins.AttributeError):
        ecs.Guest360ECSCluster(singlestack, construct_id, cluster_name=cluster_name, vpc={"foo": "bar"})


@pytest.mark.timeout(30, method="signal")
def test_cluster_with_cluster_name(singlestack):
    cluster_name = "test_cluster_name"
    ecs.Guest360ECSCluster(singlestack, construct_id, vpc="test123", cluster_name=cluster_name)
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])

    template.has_resource_properties(
        "AWS::ECS::Cluster",
        props={"ClusterName": f'{singlestack.node.try_get_context("prefix")}-{construct_id}-{cluster_name}'},
    )


@pytest.mark.timeout(30, method="signal")
def test_fargateservice_construct_required_args(singlestack):
    # create resources necessary to instantiate FargateService
    cluster = ecs.Guest360ECSCluster(singlestack, f"{construct_id}-cl", props={"vpc": "test123"})
    task_definition = aws_cdk.aws_ecs.TaskDefinition(
        singlestack,
        f"{construct_id}-tskdef",
        cpu="512",
        memory_mib="512",
        compatibility=aws_cdk.aws_ecs.Compatibility.FARGATE,
    )
    task_definition.add_container(
        f"{construct_id}-container",
        image=aws_cdk.aws_ecs.ContainerImage.from_asset(os.path.dirname(__file__) + "/test_ecs/"),
        essential=True,
    )

    ecs.Guest360FargateService(
        singlestack,
        f"{construct_id}-fs",
        cluster=cluster,
        service_name="foobar",
        task_definition=task_definition,
        subnet_type="non-routable",
    )
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])

    template.has_resource_properties(
        "AWS::ECS::Service",
        props={
            "EnableECSManagedTags": True,
            "LaunchType": "FARGATE",
        },
    )


@pytest.mark.timeout(30, method="signal")
def test_fargateservice_construct_missing_required_prop_service_name(singlestack):
    # create resources necessary to instantiate FargateService
    cluster = ecs.Guest360ECSCluster(singlestack, f"{construct_id}-cl", props={"vpc": "test123"})
    task_definition = aws_cdk.aws_ecs.TaskDefinition(
        singlestack,
        f"{construct_id}-tskdef",
        cpu="512",
        memory_mib="512",
        compatibility=aws_cdk.aws_ecs.Compatibility.FARGATE,
    )
    task_definition.add_container(
        f"{construct_id}-container",
        image=aws_cdk.aws_ecs.ContainerImage.from_asset(os.path.dirname(__file__) + "/test_ecs/"),
        essential=True,
    )
    with pytest.raises(builtins.AttributeError):
        ecs.Guest360FargateService(
            singlestack,
            f"{construct_id}-fs",
            cluster=cluster,
            task_definition=task_definition,
            subnet_type="non-routable",
        )


@pytest.mark.timeout(30, method="signal")
def test_fargate_task_definition_minimum_required_props(singlestack, task_roles):
    task_def = ecs.Guest360FargateTaskDefinition(
        singlestack,
        "taskdef",
        execution_role=task_roles[0],
        task_role=task_roles[1],
        cpu="256",
        memory_mib="512",
        log_prefix="log_prefix",
    )
    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])


@pytest.mark.parametrize(
    "env_dict",
    [
        {"foo": "bar"},
        {"foo": 123},
    ],
)
def test_fargate_task_definition_convert_env_to_str_proper_dict(env_dict):
    env = ecs.Guest360FargateTaskDefinition.convert_env_to_str(env_dict)
    logger.debug(f"{env=}")
    for key, value in env.items():
        logger.debug(f"{key=}, {type(value)=}")
        assert isinstance(value, str)


@pytest.mark.timeout(30, method="signal")
def test_fargate_task_definition_missing_required_props_roles(singlestack):
    with pytest.raises(builtins.AttributeError):
        task_def = ecs.Guest360FargateTaskDefinition(
            singlestack, "taskdef", cpu="256", memory_mib="512", log_prefix="log_prefix"
        )


@pytest.mark.timeout(30, method="signal")
def test_fargate_task_definition_missing_required_props_log_prefix(singlestack, task_roles):
    with pytest.raises(builtins.AttributeError):
        task_def = ecs.Guest360FargateTaskDefinition(
            singlestack,
            "taskdef",
            cpu="256",
            memory_mib="512",
            execution_role=task_roles[0],
            task_role=task_roles[1],
        )


@pytest.mark.timeout(30, method="signal")
def test_fargate_task_definition_ecr_image_privs(singlestack, task_roles):
    task_def = ecs.Guest360FargateTaskDefinition(
        singlestack,
        "taskdef",
        execution_role=task_roles[0],
        task_role=task_roles[1],
        cpu="256",
        memory_mib="512",
        log_prefix="log_prefix",
    )
    ecr_repo = aws_ecr.Repository.from_repository_name(singlestack, "repo", "foobar")
    container = aws_ecs.ContainerImage.from_ecr_repository(ecr_repo)
    task_def.add_container(
        "container1",
        image=container,
        essential=True,
    )

    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])
    template.has_resource_properties(
        "AWS::IAM::Policy",
        props={
            "PolicyDocument": {
                "Statement": [
                    {
                        "Action": [
                            "ecr:BatchCheckLayerAvailability",
                            "ecr:GetDownloadUrlForLayer",
                            "ecr:BatchGetImage",
                        ],
                        "Effect": "Allow",
                        "Resource": {
                            "Fn::Join": [
                                "",
                                ["arn:", {"Ref": "AWS::Partition"}, ":ecr:us-east-1:123456789:repository/foobar"],
                            ]
                        },
                    },
                    {"Action": "ecr:GetAuthorizationToken", "Effect": "Allow", "Resource": "*"},
                    {},
                ],
            }
        },
    )


@pytest.mark.timeout(30, method="signal")
def test_fargate_task_definition_add_container_force_logging(singlestack, task_roles):
    task_def = ecs.Guest360FargateTaskDefinition(
        singlestack,
        "taskdef",
        execution_role=task_roles[0],
        task_role=task_roles[1],
        cpu="256",
        memory_mib="512",
        log_prefix="log_prefix",
    )
    ecr_repo = aws_ecr.Repository.from_repository_name(singlestack, "repo", "foobar")
    container = aws_ecs.ContainerImage.from_ecr_repository(ecr_repo)
    task_def.add_container(
        "container1",
        image=container,
        essential=True,
    )

    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])

    template.has_resource_properties(
        "AWS::ECS::TaskDefinition",
        props={
            "ContainerDefinitions": [
                {"Essential": True, "LogConfiguration": {"Options": {"awslogs-stream-prefix": "log_prefix"}}}
            ]
        },
    )


@pytest.mark.timeout(30, method="signal")
def test_fargate_task_definition_otel_side_car_added(singlestack, task_roles):
    task_def = ecs.Guest360FargateTaskDefinitionOtel(
        singlestack,
        "taskdef",
        execution_role=task_roles[0],
        task_role=task_roles[1],
        cpu="256",
        memory_mib="512",
        log_prefix="log_prefix",
    )
    ecr_repo = aws_ecr.Repository.from_repository_name(singlestack, "repo", "foobar")
    container = aws_ecs.ContainerImage.from_ecr_repository(ecr_repo)
    task_def.add_container(
        "container1",
        image=container,
        essential=True,
    )

    template = assertions.Template.from_stack(singlestack)
    print_template_on_debug(template, logger, print_sections=["*"])

    template.has_resource_properties(
        "AWS::ECS::TaskDefinition",
        props={
            "ContainerDefinitions": [
                {
                    "Essential": True,
                    "LogConfiguration": {"Options": {"awslogs-stream-prefix": "log_prefix"}},
                    "Image": {
                        "Fn::Join": [
                            "",
                            [
                                "123456789.dkr.ecr.us-east-1.",
                                {"Ref": "AWS::URLSuffix"},
                                "/guest360/otel/otel_sidecar:v0.31.x",
                            ],
                        ]
                    },
                    "Name": "otel-adot-collector",
                },
                {},
            ]
        },
    )


@pytest.fixture
def task_roles(singlestack):
    execution_role = iam_role.Guest360IamRole(
        singlestack,
        "execution_role",
        props={
            "assumed_by": aws_iam.ServicePrincipal("ecs.amazonaws.com"),
            "description": "ecs execution role",
        },
    ).role
    task_role = iam_role.Guest360IamRole(
        singlestack,
        "task_role",
        props={
            "assumed_by": aws_iam.ServicePrincipal("ecs.amazonaws.com"),
            "description": "ecs task  role",
        },
    ).role
    return (execution_role, task_role)
