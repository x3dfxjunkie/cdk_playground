"""kinesis_datastream construct tests
"""
import logging
import sys

import pytest
from aws_cdk import App, Duration, Environment, Stack, aws_kinesis
from aws_cdk.assertions import Template

from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from app.guest360_constructs.tests.utils import print_template_on_debug

# from app.src.reliability.utils import KinesisStreamName

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {
    "environment": "prod",
    "stack_name": "testStack",
    "prefix": "lst-TestStack-use1",
}

SHORT_ENV = {
    "ephemeral": "lst",
    "latest": "lst",
    "stage": "stg",
    "load": "lod",
    "prod": "prd",
}
SNOW_TOPIC_SHORT_ENV = {
    "ephemeral": "dev",
    "latest": "dev",
    "load": "tst",
    "stage": "tst",
    "prod": "prd",
}


class TestKinesis:
    """Guest360 TestKinesis"""

    stack_id = "TestStack"
    kinesis_id = "TestKinesis"

    @pytest.mark.timeout(30, method="signal")
    @pytest.mark.parametrize(
        "environment,snow_p_level", [("ephemeral", "pri4"), ("latest", "pri4"), ("load", "pri4"), ("prod", "pri4")]
    )
    def test_instantiate_construct_default_params(self, environment: str, snow_p_level: str):
        short_env = SHORT_ENV[environment]
        snow_env = SNOW_TOPIC_SHORT_ENV[environment]
        if environment == "ephemeral":
            prefix = "lst-use1-pr-0000"
            environment = "latest"  # ephemeral stacks will be in the latest environment with different prefix
        else:
            prefix = f"{short_env}-use1-guest360"
        test_context = {**TEST_CONTEXT, "environment": environment, "prefix": prefix}
        test_app = App(context=test_context)
        test_stack = Stack(test_app, self.stack_id, env=Environment(account="123456789", region="us-east-1"))

        # adding props
        props = {"retention_period": Duration.hours(24), "stream_mode": aws_kinesis.StreamMode("ON_DEMAND")}

        Guest360KinesisDatastream(test_stack, construct_id=self.kinesis_id, props=props)
        # render template
        template = Template.from_stack(test_stack)
        print_template_on_debug(template, logger)

        # ensure kinesis stream created with kms encryption and on_demand
        template.has_resource_properties(
            "AWS::Kinesis::Stream",
            {
                "StreamEncryption": {"EncryptionType": "KMS"},
                "StreamModeDetails": {"StreamMode": "ON_DEMAND"},
            },
        )
        # ensure kms cdk auto creates kms key
        template.has_resource_properties(
            "AWS::KMS::Key",
            {
                "Description": f"{prefix}-{self.kinesis_id}-KinesisEncryptionKey",
                "EnableKeyRotation": True,
            },
        )
        template.resource_count_is("AWS::CloudWatch::Alarm", 1)
        template.has_resource_properties(
            "AWS::CloudWatch::Alarm",
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "ActionsEnabled": "guest360" in prefix,
                "AlarmActions": [f"arn:aws:sns:us-east-1:123456789:{prefix}-alarm-notifications"],
                "DatapointsToAlarm": 3,
                "MetricName": "GetRecords.IteratorAgeMilliseconds",
                "Namespace": "AWS/Kinesis",
                "Period": 300,
                "Statistic": "Maximum",
                "Threshold": 60000,
            },
        )

    @pytest.mark.parametrize("environment", ["latest", "stage"])
    def test_instantiate_construct_env(self, environment):
        TEST_CONTEXT["environment"] = environment
        test_app = App(context=TEST_CONTEXT)
        test_stack = Stack(test_app, "testStack", env=Environment(account="123456789", region="us-east-1"))

        # adding props
        props = {
            "retention_period": Duration.days(5),
            "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            "shard_count": 5,
            "stream_name": "testStack",
        }

        mykinesis = Guest360KinesisDatastream(test_stack, construct_id="TestKinesis", props=props)
        # render template
        template = Template.from_stack(test_stack)
        print_template_on_debug(template, logger)

        # ensure kinesis stream created with kms encryption and latest env values
        template.has_resource_properties(
            "AWS::Kinesis::Stream",
            {
                "StreamEncryption": {"EncryptionType": "KMS"},
                "StreamModeDetails": {"StreamMode": "ON_DEMAND"},
                "RetentionPeriodHours": 120,
                "Name": "lst-teststack-use1-teststack",
            },
        )

        assert isinstance(mykinesis, Guest360KinesisDatastream)
        assert isinstance(mykinesis.kinesis_stream, aws_kinesis.Stream)
        assert isinstance(mykinesis.kinesis_stream_name, str)
        assert mykinesis.kinesis_stream_name == "lst-teststack-use1-teststack"

    @pytest.mark.timeout(30, method="signal")
    def test_kinesis_stream_name(self):
        self.kinesis_id = "TestKinesis"
        test_app = App(context=TEST_CONTEXT)
        test_stack = Stack(test_app, "testStack", env=Environment(account="123456789", region="us-east-1"))
        # adding props
        props = {
            "retention_period": Duration.days(5),
            "stream_mode": aws_kinesis.StreamMode("PROVISIONED"),
            "stream_name": self.kinesis_id,
            "shard_count": 5,
        }

        mykinesis = Guest360KinesisDatastream(test_stack, self.kinesis_id, props=props)

        template = Template.from_stack(test_stack)
        print_template_on_debug(template, logger)

        # ensure kinesis stream created with kms encryption and provisioned
        template.has_resource_properties(
            "AWS::Kinesis::Stream",
            {
                "StreamEncryption": {"EncryptionType": "KMS"},
                "StreamModeDetails": {"StreamMode": "PROVISIONED"},
                "ShardCount": 5,
                "RetentionPeriodHours": 120,
                "Name": "lst-teststack-use1-testkinesis",
            },
        )

        # render template
        assert isinstance(mykinesis, Guest360KinesisDatastream)
        assert isinstance(mykinesis.kinesis_stream, aws_kinesis.Stream)
        assert isinstance(mykinesis.kinesis_stream_name, str)
