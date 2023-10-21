"""external_stage tests
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures
# pylint: disable=protected-access testing purposes
# pylint: disable=unused-import

import copy
import logging
import os
import sys
from pathlib import Path

import pytest
import yaml
from aws_cdk import App, Aspects, Environment, Stack, aws_iam, aws_sqs
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks

from app.guest360_constructs.data_service.snowflake.cdk.external_stage.tests.unit_tests.external_stage_fixtures import (
    stack_test,
    stack_west_test,
    bucket_test,
    user_test,
    sqs_test,
)

from app.guest360_constructs.data_service.snowflake.cdk.external_stage.external_stage import ExternalStage
from app.guest360_constructs.s3_bucket import Guest360S3Bucket

# set log levels for noisy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

directory = os.path.dirname(os.path.realpath(__file__))
stack_path = str(Path(os.getcwd()).parents[0])
stack_name = "StackTest"
test_context = {
    "account_id": "0" * 12,
    "environment": "latest",
    "stack_name": "testapp",
    "prefix": "lst-testapp-use1",
    "prefix_global": "lst-testapp",
    "region": "us-east-1",
    "is_static_env": True,
}
test_props = {
    "external_stage_name": "test_pipe-name",
    "s3_bucket_name": "test-bucket",
    "s3_bucket_prefix": "/foo",
}
user_name_test = "DisneySnowFlakeUser"


class TestExternalStageConstruct:
    """Guest360 Test ExternalStage"""

    def test_normalize_s3_prefix(self):
        assert ExternalStage.normalize_s3_prefix("") == ""
        assert ExternalStage.normalize_s3_prefix("/foo") == "foo/*"
        assert ExternalStage.normalize_s3_prefix("/foo/") == "foo/*"
        assert ExternalStage.normalize_s3_prefix("foo") == "foo/*"
        assert ExternalStage.normalize_s3_prefix("foo/") == "foo/*"

    def test_normalize_s3_prefix_test_props(self):
        props = copy.deepcopy(test_props)
        assert ExternalStage.normalize_s3_prefix(props["s3_bucket_prefix"]) == "foo/*"

    def test_instantiate_construct(self, stack_test, bucket_test, user_test, sqs_test):
        """
        create dummy aws_cdk app and instantiate the StackTest with construct
        """
        logger.info(f'{stack_test.node.try_get_context("prefix_global")=}')
        logger.info(f"{type(stack_test)=}")
        props = {
            **copy.deepcopy(test_props),
            **{
                "s3_bucket": bucket_test.bucket,
                "iam_principal": user_name_test,
                "snowflake_sqs_arn": sqs_test.queue_arn,
            },
        }
        external_stage = ExternalStage(stack_test, "test_external_stage", props=props)

        # ensure user found
        assert external_stage._iam_principal is not None

        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        logger.debug(f"{external_stage._external_stage_name=}")
        template.has_resource_properties(
            "AWS::S3::BucketPolicy",
            {
                "PolicyDocument": {
                    "Statement": [
                        {},
                        {},
                        {
                            "Action": [
                                "s3:GetObject",
                                "s3:GetObjectVersion",
                            ],
                            "Effect": "Allow",
                            "Sid": f"{external_stage._external_stage_name}ExternalStageS3RO",
                        },
                        {
                            "Action": [
                                "s3:DeleteObject",
                                "s3:DeleteObjectVersion",
                                "s3:PutObject",
                            ],
                            "Effect": "Allow",
                            "Sid": f"{external_stage._external_stage_name}ExternalStageS3RW",
                        },
                        {
                            "Action": [
                                "s3:ListBucket",
                                "s3:GetBucketLocation",
                            ],
                            "Effect": "Allow",
                            "Sid": f"{external_stage._external_stage_name}ExternalStageS3BucketInfo",
                        },
                    ]
                }
            },
        )

        template.has_resource_properties(
            "Custom::S3BucketNotifications",
            {
                "Managed": True,
                "NotificationConfiguration": {
                    "QueueConfigurations": [
                        {
                            "Events": ["s3:ObjectCreated:*"],
                        },
                    ],
                },
            },
        )

        template.has_output(
            "*",
            {
                "Description": "ExternalStage S3 Bucket Name",
            },
        )
        template.has_output(
            "*",
            {
                "Description": "ExternalStage S3 Bucket Prefix",
            },
        )
        template.has_output(
            "*",
            {
                "Description": "ExternalStage S3 Bucket KMS Key",
            },
        )

        # validate that template does not contain any nag rules
        annotations = Annotations.from_stack(stack_test)
        errors = annotations.find_error(
            "Guest360*",
            Match.string_like_regexp(r"AwsSolutions-.*"),
        )
        assert len(errors) == 0

    def test_instantiate_construct_no_user(self, stack_test, bucket_test):
        """
        create dummy aws_cdk app and instantiate the StackTest with construct
        """
        logger.info(f'{stack_test.node.try_get_context("prefix_global")=}')
        logger.info(f"{type(stack_test)=}")
        props = {
            **copy.deepcopy(test_props),
            **{
                "s3_bucket": bucket_test.bucket,
            },
        }
        external_stage = ExternalStage(stack_test, "test_external_stage", props=props)

        # ensure iam principal is none
        assert external_stage._iam_principal is None

        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        # validate that template does not contain any nag rules
        annotations = Annotations.from_stack(stack_test)
        errors = annotations.find_error(
            "Guest360*",
            Match.string_like_regexp(r"AwsSolutions-.*"),
        )
        assert len(errors) == 0

    def test_instantiate_construct_no_sqs(self, stack_test, bucket_test):
        """
        create dummy aws_cdk app and instantiate the StackTest with construct
        """
        logger.info(f'{stack_test.node.try_get_context("prefix_global")=}')
        logger.info(f"{type(stack_test)=}")
        props = {
            **copy.deepcopy(test_props),
            **{
                "s3_bucket": bucket_test.bucket,
                "iam_principal": user_name_test,
            },
        }
        ExternalStage(stack_test, "test_external_stage", props=props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        # validate that template does not contain any nag rules
        annotations = Annotations.from_stack(stack_test)
        errors = annotations.find_error(
            "Guest360*",
            Match.string_like_regexp(r"AwsSolutions-.*"),
        )
        assert len(errors) == 0
