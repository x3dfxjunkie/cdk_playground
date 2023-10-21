"""test for lambda shredder construct
"""
import logging
import json
import sys
import pytest
from unittest.mock import patch
from aws_cdk import App, Stack, assertions, aws_kinesis, aws_lambda, Environment, Duration
from app.guest360_constructs.ingestion.lambda_shredder_construct import BatchLambdaShredder


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_PROPS = {
    "stack_extension": "lambdashreddertest",
    "kinesis": {
        "stream_mode": aws_kinesis.StreamMode.PROVISIONED,
        "shard_count": 1,
        "retention_period": Duration.days(1),
    },
    "lambda_": {
        "name": "lambda-shredder-test",
        "directory": "PLACEHOLDER_PATH.zip",
        "timeout": 60,
        "environment": {"REGION": "us-east-1", "MAX_FILE_SIZE": "1000000"},
    },
    "s3": {"notifications": {"key_filters": {"suffixes": ["json", "csv"]}}},
}

TEST_CONTEXT = {
    "environment": "local",
    "stack_name": "testStack",
    "prefix": "test-prefix-use1",
    "region": "us-east-1",
}


@pytest.fixture
def app_stack():
    test_app = App(context=TEST_CONTEXT)
    test_stack = Stack(test_app, "TestStack", env=Environment(account="123456789", region="us-east-1"))
    yield test_stack


def test_lambda_shredder_created(app_stack):  # pylint: disable=redefined-outer-name
    """
    Patch the `aws_lambda.Code.from_asset` function since we can't create and access temporary zip files easily in bazel
    """
    with patch(
        "app.guest360_constructs.ingestion.lambda_shredder_construct.aws_lambda.Code.from_asset",
        lambda *args: aws_lambda.Code.from_inline("""mytestcode"""),
    ):
        BatchLambdaShredder(app_stack, "batch_shredder_test", TEST_PROPS)
    # render template
    template = assertions.Template.from_stack(app_stack)

    logger.debug("app_stack=%s", json.dumps(template.to_json(), indent=2))

    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "FunctionName": "test-prefix-use1-lambdashreddertest",
            "Environment": {"Variables": {"REGION": "us-east-1", "STACK_NAME": "teststack"}},
            "Handler": "main.handler",
            "Timeout": 60,
        },
    )

    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "BucketName": "test-prefix-use1-lambdashreddertest-bucket",
        },
    )

    template.has_resource_properties(
        "AWS::Kinesis::Stream",
        {
            "Name": "test-prefix-use1-lambdashreddertest-stream",
            "RetentionPeriodHours": 24,
            "ShardCount": 1,
            "StreamModeDetails": {"StreamMode": "PROVISIONED"},
        },
    )

    """
    The stack creates 2 lambdas:
    BatchLambdaShredder8a5a4testprefixuse1lambdashreddertestE47560C3 :: {
             "Properties": {
               "Code": {
                 "S3Bucket": "cdk-hnb659fds-assets-123456789-us-east-1",
                 "S3Key": "bf7cdd298713e4e0cf0e1037c6f49c2cc2d5d6923f153c2828dec0a9831f366b.zip"
               },
               "Environment": {
                 "Variables": {
                   "KINESIS_STREAM_NAME":
                "FunctionName": "test-prefix-use1-lambdashreddertest"

    BucketNotificationsHandler050a0587b7544547bf325f094a3db8347ECC3691 :: {
             "Properties": {
               "Code": { "ZipFile": "import boto3
               "Description": "AWS CloudFormation handler for \"Custom::S3BucketNotifications\" resources (@aws-cdk/aws-s3)",
           !!   Missing key 'Environment'
               "Environment": undefined,
           !!   Missing key 'FunctionName'
               "FunctionName": undefined,
               "Handler": "index.handler",

    Also for s3 in local env creates 2 buckets, the other is for logging:
    BatchLambdaShredder8a5a4Guest360S3Bucketec29ctestStackloggingbucketA99AB281 :: {
             "DeletionPolicy": "Retain",
             "Metadata": { "cdk_nag": { "rules_to_suppress": [ { ... } ] } },
             "Properties": {
               "AccessControl": "LogDeliveryWrite",
               "BucketEncryption": { "ServerSideEncryptionConfiguration": [ { "ServerSideEncryptionByDefault": { "SSEAlgorithm": "AES256" } } ] },
               "BucketName": "wdpr-guest360-local-us-east-1-logging",
    """
