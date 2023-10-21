"""kinesis_firehose construct tests
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument fixture
import builtins
import json
import logging
import os
import sys
import pytest
import yaml
from aws_cdk import App, Aspects, Environment, Stack, aws_kinesis, aws_lambda
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks, NagSuppressions

from app.guest360_constructs.kinesis_firehose import Guest360KinesisFirehose
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from app.guest360_constructs.s3_bucket import Guest360S3Bucket


# set log levels for nozy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

RESOURCE = "AWS::KinesisFirehose::DeliveryStream"
ALARM_RESOURCE = "AWS::CloudWatch::Alarm"

S3_NAG_SUPRESSION = [
    {
        "id": "AwsSolutions-S1",
        "reason": "testing does not need S1 for mocking",
    }
]

GENERIC_FIREHOSE_PROPS = {
    "enabled": True,
    "bucket_name": "Test",
    "buffering_hints": {"interval": 60, "unit_of_time": "SECONDS"},
}

DYNAMIC_CUSTOM_PARTITIONING_PROPS = {
    "partitioning": {
        "dynamic": {"enabled": True, "keys": {"test": ".test"}},
        "custom_keys": {"foo": "bar", "hello": "world"},
    },
}

DYNAMIC_PARTITIONING_PROPS = {
    "partitioning": {
        "dynamic": {"enabled": True, "keys": {"test": ".test"}},
        "custom_keys": None,
    },
}

DATA_TRANSFORMATION_ENABLED_PROPS = {
    "data_transformation": {
        "enabled": True,
        "lambda_properties": {
            "code": aws_lambda.Code.from_inline("""mytestcode"""),
            "handler": "index.handler",
            "runtime": aws_lambda.Runtime.PYTHON_3_9,
            "enable_otel_tracing": False,
        },
    },
}

DATA_TRANSFORMATION_DISABLED_PROPS = {
    "data_transformation": {
        "enabled": False,
        "lambda_properties": {
            "code": aws_lambda.Code.from_inline("""mytestcode"""),
            "handler": "index.handler",
            "runtime": aws_lambda.Runtime.PYTHON_3_9,
        },
    },
}

MONITORING_PROPS = {
    "delivery_freshness": {
        "period": 10,  # Minutes
        "evaluation_periods": 3,
        "datapoints_to_alarm": 2,
        "threshold": 600,  # unit Seconds (15') # Configurable
    }
}

DYNAMIC_PARTITIONING_MONITORING_PROPS = {
    "partition_count_exceeded": {
        "period": 5,  # Minutes
        "evaluation_periods": 3,
        "datapoints_to_alarm": 3,
        "threshold": 1,  # unit Boolean
    },
}

DYNAMIC_PARTITIONING_NONE_KEYS_PROPS = {
    "partitioning": {
        "dynamic": {"enabled": True, "keys": None},
        "custom_keys": {"foo": "bar", "hello": "world"},
    },
}

PARTITIONING_NONE_KEYS_PROPS = {
    "partitioning": {
        "dynamic": {"enabled": True, "keys": None},
        "custom_keys": None,
    },
}

JSONQUERY_PROCESSING_CONFIG_TEMPLATE = {
    "ProcessingConfiguration": {
        "Enabled": True,
        "Processors": [
            {
                "Parameters": [
                    {
                        "ParameterName": "MetadataExtractionQuery",
                        "ParameterValue": "{test: .test,}",
                    },
                    {"ParameterName": "JsonParsingEngine", "ParameterValue": "JQ-1.6"},
                ],
                "Type": "MetadataExtraction",
            },
            {
                "Parameters": [
                    {
                        "ParameterName": "SubRecordType",
                        "ParameterValue": "JSON",
                    }
                ],
                "Type": "RecordDeAggregation",
            },
            {
                "Parameters": [
                    {
                        "ParameterName": "Delimiter",
                        "ParameterValue": "\\n",
                    }
                ],
                "Type": "AppendDelimiterToRecord",
            },
        ],
    },
}

DEFAULT_JSONQUERY_PROCESSING_CONFIG_TEMPLATE = {
    "ProcessingConfiguration": {
        "Enabled": True,
        "Processors": [
            {
                "Parameters": [
                    {
                        "ParameterName": "MetadataExtractionQuery",
                        "ParameterValue": "{database: .router_database,schema: .router_schema,table: .router_table,stream: .stream,}",
                    },
                    {"ParameterName": "JsonParsingEngine", "ParameterValue": "JQ-1.6"},
                ],
                "Type": "MetadataExtraction",
            },
            {
                "Parameters": [
                    {
                        "ParameterName": "SubRecordType",
                        "ParameterValue": "JSON",
                    }
                ],
                "Type": "RecordDeAggregation",
            },
            {
                "Parameters": [
                    {
                        "ParameterName": "Delimiter",
                        "ParameterValue": "\\n",
                    }
                ],
                "Type": "AppendDelimiterToRecord",
            },
        ],
    },
}

KINESIS_FIREHOSE_TEMPLATE = {
    "DeliveryStreamType": "KinesisStreamAsSource",
    "ExtendedS3DestinationConfiguration": {
        "Prefix": "foo=bar/hello=world/test=!{partitionKeyFromQuery:test}/!{timestamp:yyyy/MM/dd/HH}/",
        "ErrorOutputPrefix": "foo=bar/hello=world/Errors/result=!{firehose:error-output-type}/!{timestamp:yyyy/MM/dd/HH}/",
        "DynamicPartitioningConfiguration": {
            "Enabled": True,
        },
        **JSONQUERY_PROCESSING_CONFIG_TEMPLATE,
    },
}

DEFAULT_MONITORING_TEMPLATE = {
    "MetricName": "DeliveryToS3.DataFreshness",
    "DatapointsToAlarm": 1,
    "EvaluationPeriods": 1,
    "Period": 300,
    "Statistic": "Average",
    "Threshold": 900,
}

DEFAULT_PARTITIONING_MONITORING_TEMPLATE = {
    "MetricName": "PartitionCountExceeded",
    "DatapointsToAlarm": 1,
    "EvaluationPeriods": 1,
    "Period": 300,
    "Statistic": "Average",
    "Threshold": 1,
}

CUSTOM_PARTITIONING_MONITORING_TEMPLATE = {
    "MetricName": "PartitionCountExceeded",
    "DatapointsToAlarm": 3,
    "EvaluationPeriods": 3,
    "Period": 300,
    "Statistic": "Average",
    "Threshold": 1,
}

CUSTOM_MONITORING_TEMPLATE = {
    "MetricName": "DeliveryToS3.DataFreshness",
    "DatapointsToAlarm": 2,
    "EvaluationPeriods": 3,
    "Period": 600,  # Seconds
    "Statistic": "Average",
    "Threshold": 600,
}


test_context = {
    "environment": "latest",
    "stack_name": "testStack",
    "prefix": "lst-TestStack-use1",
    "prefix_global": "lst-testStack",
    "account": "123456789",
    "region": "us-east-1",
}
stack_id = "TestStack"
kinesis_id = "TestKinesis"
firehose_id = "TestFirehose"
bucket_id = "TestBucket"
directory = os.path.dirname(os.path.realpath(__file__))


class TestKinesisFirehose:
    """Guest360 TestKinesisFirehose"""

    @pytest.fixture
    def stack_test(self):
        test_app = App(context=test_context)
        aspects = Aspects.of(test_app)
        aspects.add(AwsSolutionsChecks(verbose=True))
        stack_test = Stack(
            test_app, stack_id, env=Environment(account=test_context["account"], region=test_context["region"])
        )
        yield stack_test

    @pytest.mark.timeout(30, method="signal")
    def test_instantiate_construct_general_params(self, stack_test):
        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template.
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        self.assert_aws_solutions_check(stack_test)

        template.has_resource_properties(
            ALARM_RESOURCE,
            props=DEFAULT_MONITORING_TEMPLATE,
        )

        template.has_resource_properties(
            RESOURCE,
            {
                "DeliveryStreamType": "KinesisStreamAsSource",
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_instantiate_construct_general_params_and_monitoring(self, stack_test):
        # Emulating static guest360 environment
        stack_test.node.set_context("prefix", "test-guest360-use1")

        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]

        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "monitoring": MONITORING_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template.
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        self.assert_aws_solutions_check(stack_test)

        template.has_resource_properties(
            ALARM_RESOURCE,
            props=CUSTOM_MONITORING_TEMPLATE,
        )

    @pytest.mark.timeout(30, method="signal")
    def test_partitioning_custom_keys_and_dynamic_keys_enabled(self, stack_test):
        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
            **DYNAMIC_CUSTOM_PARTITIONING_PROPS,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            RESOURCE,
            {
                **KINESIS_FIREHOSE_TEMPLATE,
            },
        )

        template.has_resource_properties(
            ALARM_RESOURCE,
            props=DEFAULT_MONITORING_TEMPLATE,
        )

        template.has_resource_properties(
            ALARM_RESOURCE,
            props=DEFAULT_PARTITIONING_MONITORING_TEMPLATE,
        )

    @pytest.mark.timeout(30, method="signal")
    def test_partitioning_custom_keys_dynamic_keys_and_monitoring(self, stack_test):
        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]

        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
            **DYNAMIC_CUSTOM_PARTITIONING_PROPS,
            "monitoring": {
                **MONITORING_PROPS,
                **DYNAMIC_PARTITIONING_MONITORING_PROPS,
            },
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            RESOURCE,
            {
                **KINESIS_FIREHOSE_TEMPLATE,
            },
        )

        template.has_resource_properties(
            ALARM_RESOURCE,
            props=CUSTOM_MONITORING_TEMPLATE,
        )

        template.has_resource_properties(
            ALARM_RESOURCE,
            props=CUSTOM_PARTITIONING_MONITORING_TEMPLATE,
        )

    @pytest.mark.timeout(30, method="signal")
    def test_partitioning_custom_keys_with_none_and_dynamic_keys_enabled(self, stack_test):
        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
            **DYNAMIC_PARTITIONING_PROPS,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            RESOURCE,
            {
                "DeliveryStreamType": "KinesisStreamAsSource",
                "ExtendedS3DestinationConfiguration": {
                    "Prefix": "snowpipe/test=!{partitionKeyFromQuery:test}/!{timestamp:yyyy/MM/dd/HH}/",
                    "ErrorOutputPrefix": "snowpipe/Errors/result=!{firehose:error-output-type}/!{timestamp:yyyy/MM/dd/HH}/",
                    "DynamicPartitioningConfiguration": {
                        "Enabled": True,
                    },
                    **JSONQUERY_PROCESSING_CONFIG_TEMPLATE,
                },
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_partitioning_dynamic_enabled_with_none_keys_and_custom_keys_monitoring(self, stack_test):
        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
            **DYNAMIC_PARTITIONING_NONE_KEYS_PROPS,
            "monitoring": DYNAMIC_PARTITIONING_MONITORING_PROPS,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            RESOURCE,
            {
                "DeliveryStreamType": "KinesisStreamAsSource",
                "ExtendedS3DestinationConfiguration": {
                    "Prefix": "foo=bar/hello=world/database=!{partitionKeyFromQuery:database}/schema=!{partitionKeyFromQuery:schema}/table=!{partitionKeyFromQuery:table}/stream=!{partitionKeyFromQuery:stream}/!{timestamp:yyyy/MM/dd/HH}/",
                    "ErrorOutputPrefix": "foo=bar/hello=world/Errors/result=!{firehose:error-output-type}/!{timestamp:yyyy/MM/dd/HH}/",
                    "DynamicPartitioningConfiguration": {
                        "Enabled": True,
                    },
                    **DEFAULT_JSONQUERY_PROCESSING_CONFIG_TEMPLATE,
                },
            },
        )

        template.has_resource_properties(
            ALARM_RESOURCE,
            props=CUSTOM_PARTITIONING_MONITORING_TEMPLATE,
        )

    def test_partitioning_dynamic_enabled_and_none_keys(self, stack_test):
        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
            **PARTITIONING_NONE_KEYS_PROPS,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            RESOURCE,
            {
                "DeliveryStreamType": "KinesisStreamAsSource",
                "ExtendedS3DestinationConfiguration": {
                    "Prefix": "snowpipe/database=!{partitionKeyFromQuery:database}/schema=!{partitionKeyFromQuery:schema}/table=!{partitionKeyFromQuery:table}/stream=!{partitionKeyFromQuery:stream}/!{timestamp:yyyy/MM/dd/HH}/",
                    "ErrorOutputPrefix": "snowpipe/Errors/result=!{firehose:error-output-type}/!{timestamp:yyyy/MM/dd/HH}/",
                    "DynamicPartitioningConfiguration": {
                        "Enabled": True,
                    },
                    **DEFAULT_JSONQUERY_PROCESSING_CONFIG_TEMPLATE,
                },
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_data_transformation_enabled(self, stack_test):
        kinesis_instance = Guest360KinesisDatastream(
            stack_test,
            kinesis_id,
            props={
                "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            },
        ).kinesis_stream
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
            **DATA_TRANSFORMATION_ENABLED_PROPS,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(f"template={json.dumps(template.to_json(), indent=2)}")

        template.has_resource_properties(
            RESOURCE,
            {
                "DeliveryStreamType": "KinesisStreamAsSource",
                "ExtendedS3DestinationConfiguration": {
                    "ProcessingConfiguration": {
                        "Enabled": True,
                        "Processors": [
                            {
                                "Type": "Lambda",
                            },
                        ],
                    },
                },
            },
        )
        template.has_resource_properties(
            "AWS::Lambda::Function",
            {
                "Description": "Firehose Data Processing Lambda",
                "FunctionName": f'{test_context["prefix"].lower()}-{firehose_id.lower()}-fh-lambda',
            },
        )
        template.has_resource_properties(
            "AWS::IAM::Policy",
            {
                "PolicyDocument": {
                    "Statement": [
                        {
                            "Action": [
                                "lambda:InvokeFunction",
                                "lambda:GetFunction",
                                "lambda:GetFunctionConfiguration",
                            ],
                            "Effect": "Allow",
                            "Resource": [
                                f'arn:aws:lambda:{test_context["region"]}:{test_context["account"]}:function:{test_context["prefix"].lower()}-{firehose_id.lower()}-fh-lambda',
                                f'arn:aws:lambda:{test_context["region"]}:{test_context["account"]}:function:{test_context["prefix"].lower()}-{firehose_id.lower()}-fh-lambda:*',
                            ],
                        }
                    ]
                }
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_data_transformation_disabled(self, stack_test):
        kinesis_instance = aws_kinesis.Stream(stack_test, kinesis_id)
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
            **DATA_TRANSFORMATION_DISABLED_PROPS,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            RESOURCE,
            {
                "DeliveryStreamType": "KinesisStreamAsSource",
                "ExtendedS3DestinationConfiguration": {
                    "ProcessingConfiguration": {
                        "Enabled": False,
                    },
                },
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_data_transformation_none(self, stack_test):
        kinesis_instance = aws_kinesis.Stream(stack_test, kinesis_id)
        s3_instance = Guest360S3Bucket(
            stack_test, bucket_id, region="us-east-1", props={"bucket_name": bucket_id}
        ).bucket
        NagSuppressions.add_resource_suppressions(
            s3_instance,
            S3_NAG_SUPRESSION,
            True,
        )
        my_static_buckets = [{"bucket": s3_instance, "bucket_name": bucket_id}]
        # adding props
        firehose_props = {
            **GENERIC_FIREHOSE_PROPS,
            "kinesis_stream": kinesis_instance,
            "static_buckets": my_static_buckets,
        }

        Guest360KinesisFirehose(stack_test, construct_id=firehose_id, props=firehose_props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            RESOURCE,
            {
                "DeliveryStreamType": "KinesisStreamAsSource",
                "ExtendedS3DestinationConfiguration": {
                    "ProcessingConfiguration": {
                        "Enabled": False,
                    },
                },
            },
        )
        # ensure that the template does not contain a lambda function
        with pytest.raises(builtins.RuntimeError):
            template.has_resource_properties(
                "AWS::Lambda::Function",
                {
                    "Description": "Firehose Data Processing Lambda",
                    "FunctionName": f'{test_context["prefix"].lower()}-fh-lambda',
                },
            )

    def assert_aws_solutions_check(self, stack_test):
        # this should be 0 since the construct has nags for lambda role
        # validate that template does not contain any nag rules
        annotations = Annotations.from_stack(stack_test)
        errors = annotations.find_error(
            "Guest360*",
            Match.string_like_regexp(r"AwsSolutions-.*"),
        )
        assert len(errors) == 0
