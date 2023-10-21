"""Tests for Guest360S3Bucket"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
import json
import logging
import sys

import pytest
from app.guest360_constructs.kms_key import Guest360KMSKey
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from aws_cdk import App, Stack, assertions

# set log levels for nozy calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"


@pytest.mark.timeout(30, method="signal")
def test_s3_bucket_created():
    test_context = {
        "environment": "latest",
        "stack_name": "testStack",
        "prefix": "lst-testStack-use1",
    }
    app = App(context=test_context)
    stack = Stack(app)

    Guest360S3Bucket(stack, "TestBucket", region="us-east-1", props={"bucket_name": "lst-testStack-use1-test-bucket"})
    template = assertions.Template.from_stack(stack)
    logger.debug(json.dumps(template.to_json(), indent=2))

    template.resource_count_is("AWS::S3::Bucket", 1)
    template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 1)
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 2,
            "DatapointsToAlarm": 2,
            "MetricName": "5xxErrors",
            "Namespace": "AWS/S3",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 5,
            "Unit": "Count",
        },
    )


@pytest.mark.timeout(30, method="signal")
def test_s3_bucket_created_local_logging():
    test_context = {
        "environment": "local",
        "stack_name": "testStack",
        "prefix": "lst-testStack-use1",
    }
    app = App(context=test_context)
    stack = Stack(app)

    prefix = stack.node.try_get_context("prefix")

    bucket = Guest360S3Bucket(stack, "TestBucket", region="us-east-1", props={"bucket_name": "test-bucket"})
    template = assertions.Template.from_stack(stack)
    logger.debug(json.dumps(template.to_json(), indent=2))

    template.resource_count_is("AWS::S3::Bucket", 2)
    # Validate logging bucket properties for "local" environment
    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "BucketName": bucket.logging_bucket_map["local"],
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [{"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]
            },
            "PublicAccessBlockConfiguration": {
                "BlockPublicAcls": True,
                "BlockPublicPolicy": True,
                "IgnorePublicAcls": True,
                "RestrictPublicBuckets": True,
            },
        },
    )
    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "BucketName": f"{prefix.lower()}-test-bucket",
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [{"ServerSideEncryptionByDefault": {"KMSMasterKeyID": {}}}]
            },
            "PublicAccessBlockConfiguration": {
                "BlockPublicAcls": True,
                "BlockPublicPolicy": True,
                "IgnorePublicAcls": True,
                "RestrictPublicBuckets": True,
            },
            "VersioningConfiguration": {"Status": "Enabled"},
            "LoggingConfiguration": {"DestinationBucketName": {}},
        },
    )


@pytest.mark.timeout(30, method="signal")
def test_s3_bucket_created_provide_key():
    test_context = {
        "environment": "local",
        "stack_name": "testStack",
        "prefix": "lst-testStack-use1",
    }
    app = App(context=test_context)
    stack = Stack(app)

    kms_key = Guest360KMSKey(
        stack,
        "KinesisEncryptionKey",
        {"alias": "test_key", "description": "test_key"},
    ).key
    Guest360S3Bucket(
        stack, "TestBucket", region="us-east-1", props={"bucket_name": "test-bucket", "encryption_key": kms_key}
    )

    template = assertions.Template.from_stack(stack)
    logger.debug(json.dumps(template.to_json(), indent=2))


@pytest.mark.timeout(30, method="signal")
def test_s3_import_export_ssm():
    export_test_context = {
        "environment": "latest",
        "stack_name": "testStack",
        "prefix": "lst-testStack-use1",
    }
    export_app = App(context=export_test_context)
    export_stack = Stack(export_app)

    export_s3_bucket = Guest360S3Bucket(
        export_stack, "TestBucket", region="us-east-1", props={"bucket_name": "lst-testStack-use1-test-bucket"}
    )
    export_s3_bucket.export_ssm("s3_bucket")
    export_template = assertions.Template.from_stack(export_stack)
    export_template.resource_count_is("AWS::SSM::Parameter", 2)

    import_test_context = {
        "environment": "latest",
        "stack_name": "importTestStack",
        "prefix": "lst-testStack-use1",
    }
    import_app = App(context=import_test_context)
    import_stack = Stack(import_app)

    Guest360S3Bucket.from_ssm(import_stack, "bucket", export_stack.stack_name, "s3_bucket")
    template = assertions.Template.from_stack(import_stack)

    template_json = template.to_json()

    bucket_arn = [item for item in template_json["Parameters"].values() if item["Default"].endswith("bucket_arn")]
    kms_arn = [item for item in template_json["Parameters"].values() if item["Default"].endswith("kms_arn")]

    assert len(bucket_arn) == 1
    assert len(kms_arn) == 1
