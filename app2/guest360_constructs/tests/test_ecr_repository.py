"""
Tests for Guest360ECRRepository
"""
import yaml
import logging
import sys

import pytest
import aws_cdk
from app.guest360_constructs.ecr_repository import Guest360ECRRepository, RepoProps, ImageReplicationProps
from aws_cdk import assertions, aws_ecr

from app.guest360_constructs.tests.utils import print_template_on_debug

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

test_repo_name = "TEST_REPO"
stack_id = "TestStack"


def test_ecr_default_repo():
    """
    By default all repos will have 1) image scan on push 2) lifecycle to expire untagged >24hrs and 4th oldest
    image version.
    """
    test_context = {
        "environment": "local",
        "prefix": "test-prefix-use1",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, stack_id)
    # props: RepoProps = {"dummy_field": "dummy_field"}  # Empty for default props
    repo = Guest360ECRRepository(scope=stack, construct_id=test_repo_name)
    logger.debug(repo.repository_name)
    template = assertions.Template.from_stack(stack)
    logger.debug(yaml.dump(template.to_json()))
    template.resource_count_is("AWS::ECR::Repository", 1)
    template.has_resource("AWS::ECR::Repository", {"DeletionPolicy": "Delete", "UpdateReplacePolicy": "Delete"})
    template.has_resource_properties(
        "AWS::ECR::Repository",
        props={
            "ImageScanningConfiguration": {"ScanOnPush": True},
            "LifecyclePolicy": {
                "LifecyclePolicyText": (
                    """{"rules":["""
                    """{"rulePriority":1,"description":"Expire untagged images older than 24 hours","""
                    """"selection":{"tagStatus":"untagged","countType":"sinceImagePushed","countNumber":1,"""
                    """"countUnit":"days"},"action":{"type":"expire"}},"""
                    """{"rulePriority":2,"description":"Keep last 3 """
                    """images","selection":{"tagStatus":"tagged","tagPrefixList":["v"],"countType":"""
                    """"imageCountMoreThan","countNumber":3},"action":{"type":"expire"}}]}"""
                ),
            },
        },
    )


def test_ecr_prod_default_repo():
    """
    Prod repos will have removal and deletion policies set to Retain
    """
    test_context = {
        "environment": "prod",
        "prefix": "prd-use1-guest360",
        "region": "us-east-1",
        "is_static_env": True,
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, stack_id)
    Guest360ECRRepository(scope=stack, construct_id=test_repo_name)
    template = assertions.Template.from_stack(stack)
    logger.debug(yaml.dump(template.to_json()))
    template.resource_count_is("AWS::ECR::Repository", 1)
    template.has_resource("AWS::ECR::Repository", {"DeletionPolicy": "Retain", "UpdateReplacePolicy": "Retain"})
    template.has_resource_properties(
        "AWS::ECR::Repository",
        props={
            "ImageScanningConfiguration": {"ScanOnPush": True},
            "LifecyclePolicy": {
                "LifecyclePolicyText": (
                    """{"rules":["""
                    """{"rulePriority":1,"description":"Expire untagged images older than 24 hours","""
                    """"selection":{"tagStatus":"untagged","countType":"sinceImagePushed","countNumber":1,"""
                    """"countUnit":"days"},"action":{"type":"expire"}},"""
                    """{"rulePriority":2,"description":"Keep last 3 """
                    """images","selection":{"tagStatus":"tagged","tagPrefixList":["v"],"countType":"""
                    """"imageCountMoreThan","countNumber":3},"action":{"type":"expire"}}]}"""
                ),
            },
        },
    )


def test_ecr_static_environment_default_repo():
    """
    Static environment repos will have immutable tags.
    """
    test_context = {
        "environment": "stage",
        "prefix": "stg-use1-guest360",
        "region": "us-east-1",
        "is_static_env": True,
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, stack_id)
    # props: RepoProps = {"dummy_field": "dummy_field"}  # Empty for default props
    Guest360ECRRepository(scope=stack, construct_id=test_repo_name)
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger, print_type="yaml")
    template.resource_count_is("AWS::ECR::Repository", 1)
    template.has_resource_properties(
        "AWS::ECR::Repository",
        props={
            "ImageScanningConfiguration": {"ScanOnPush": True},
            "LifecyclePolicy": {
                "LifecyclePolicyText": (
                    """{"rules":["""
                    """{"rulePriority":1,"description":"Expire untagged images older than 24 hours","""
                    """"selection":{"tagStatus":"untagged","countType":"sinceImagePushed","countNumber":1,"""
                    """"countUnit":"days"},"action":{"type":"expire"}},"""
                    """{"rulePriority":2,"description":"Keep last 3 """
                    """images","selection":{"tagStatus":"tagged","tagPrefixList":["v"],"countType":"""
                    """"imageCountMoreThan","countNumber":3},"action":{"type":"expire"}}]}"""
                ),
            },
            "ImageTagMutability": "MUTABLE",
        },
    )


def test_repo_props():
    """
    Ensure props and related logic working as expected
    """
    test_context = {
        "environment": "stage",
        "prefix": "stg-use1-guest360",
        "region": "us-east-1",
        "is_static_env": True,
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, stack_id)
    test_props = RepoProps(
        image_scan_on_push=False,  # Should be overridden to true
        removal_policy=aws_cdk.RemovalPolicy.RETAIN,  # Should be overriddent to DESTROY
        image_tag_mutability=aws_ecr.TagMutability.IMMUTABLE,  # This should be overridden to MUTABLE since static
        lifecycle_rules=[
            aws_ecr.LifecycleRule(
                description="Keep last 4 images",
                tag_status=aws_ecr.TagStatus.TAGGED,
                tag_prefix_list=["v"],
                max_image_count=4,
            ),
        ],
    )
    Guest360ECRRepository(scope=stack, construct_id=test_repo_name, props=test_props)
    template = assertions.Template.from_stack(stack)
    logger.debug(yaml.dump(template.to_json()))
    template.resource_count_is("AWS::ECR::Repository", 1)
    template.has_resource_properties(
        "AWS::ECR::Repository",
        props={
            "ImageScanningConfiguration": {"ScanOnPush": True},
            "LifecyclePolicy": {
                "LifecyclePolicyText": (
                    """{"rules":["""
                    """{"rulePriority":1,"description":"Expire untagged images older than 24 hours","""
                    """"selection":{"tagStatus":"untagged","countType":"sinceImagePushed","countNumber":1,"""
                    """"countUnit":"days"},"action":{"type":"expire"}},"""
                    """{"rulePriority":2,"description":"Keep last 3 images","""
                    """"selection":{"tagStatus":"tagged","tagPrefixList":["v"],"countType":"imageCountMoreThan","""
                    """"countNumber":3},"action":{"type":"expire"}},"""
                    """{"rulePriority":3,"description":"Keep last 4 images","""
                    """"selection":{"tagStatus":"tagged","tagPrefixList":["v"],"countType":"imageCountMoreThan","""
                    """"countNumber":4},"action":{"type":"expire"}}"""
                    """]}"""
                ),
            },
            "ImageTagMutability": "MUTABLE",
        },
    )


def test_replicate_image_to_custom_ecr():
    """
    If called, images under ECR repo should be copied from the default
    ECR repo to a custom one
    """
    test_context = {
        "environment": "latest",
        "prefix": "guest360-test-prefix-use1",
        "region": "us-east-1",
        "is_static_env": True,
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, stack_id)

    test_props = RepoProps(
        repository_name="guest360/spec/analytics_engineering/dbt_helix_mono",
        image_replication_props=[
            ImageReplicationProps(
                destination_account_id="795965727170",
                destination_region="us-east-1",
                source_environments=["latest"],
            ),
            ImageReplicationProps(
                destination_account_id="54323456435",
                destination_region="us-west-1",
                source_environments=["latest", "stage"],
            ),
        ],
    )
    Guest360ECRRepository(scope=stack, construct_id=test_repo_name, props=test_props)

    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger, print_type="yaml")

    template.resource_count_is("AWS::ECR::ReplicationConfiguration", 0)
    # TODO: move this testing for pipeline docker stack
    # template.has_resource_properties(
    #     "AWS::ECR::ReplicationConfiguration",
    #     props={
    #         "ReplicationConfiguration": {
    #             "Rules": [
    #                 {
    #                     "Destinations": [
    #                         {"Region": "us-east-1", "RegistryId": "795965727170"},
    #                         {"Region": "us-west-1", "RegistryId": "54323456435"},
    #                     ],
    #                     "RepositoryFilters": [
    #                         {"Filter": "guest360/spec/analytics_engineering/", "FilterType": "PREFIX_MATCH"},
    #                         {"Filter": "guest360/spec/analytics_engineering/", "FilterType": "PREFIX_MATCH"},
    #                     ],
    #                 }
    #             ]
    #         },
    #     },
    # )


def test_special_replication_only_from_source_environment():
    test_context = {
        "environment": "stage",
        "prefix": "stg-use1-guest360",
        "region": "us-east-1",
        "is_static_env": True,
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, stack_id)
    replication_filter = "guest360/spec/analytics_engineering/"
    repository_name = f"{replication_filter}dbt_helix_mono"
    test_props = RepoProps(
        repository_name=repository_name,
        image_replication_props=[
            ImageReplicationProps(
                destination_account_id="795965727170",
                destination_region="us-east-1",
                source_environments=["latest"],
            ),
        ],
    )
    Guest360ECRRepository(scope=stack, construct_id=test_repo_name, props=test_props)
    template = assertions.Template.from_stack(stack)
    # TODO: move this testing for pipeline docker stack
    template.resource_count_is("AWS::ECR::ReplicationConfiguration", 0)


if __name__ == "__main__":  # pragma: no cover
    test_repo_props()
