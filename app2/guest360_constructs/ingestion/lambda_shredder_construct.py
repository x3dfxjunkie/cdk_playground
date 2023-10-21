#!/usr/bin/env python3
"""BatchLambdaShredder Guest360 Construct
"""
import logging
import os
from copy import deepcopy
from pathlib import Path
from typing import Dict, TypedDict

from aws_cdk import aws_s3, aws_s3_notifications, Duration, Stack, aws_lambda
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream, KinesisProps
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from app.src.reliability.utils import LambdaFunctionName

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class EnvironmentProps(TypedDict):
    REGION: str
    MAX_FILE_SIZE: str


class LambdaProps(TypedDict):
    name: str
    directory: str
    timeout: int
    environment: EnvironmentProps


@match_class_typing
class StackConfigProps(TypedDict):
    stack_extension: str
    kinesis: Dict  # this should be KinesisProps, just FYI.
    lambda_: LambdaProps  # previous name lambda generates a bug - Python reserved word


class BatchLambdaShredder(Construct360):
    """Custom CDK construct class for a AWS s3 --> lambda --> kinesis file pattern
    Additional resources may be created such as IAM roles.

    Args:
    Construct (Construct360): Defined as a re-usable Construct object

    """

    def __init__(self, scope: Construct360, construct_id: str, props: StackConfigProps) -> None:
        """
        Class for creating Lambda to push data from s3 to kinesis
        Creates Lambda, s3 bucket to land data and kinesis stream.

        Args:
        Construct (Construct360): Defined as a re-usable Contruct object
        props (dictionary):
        "stack_extension": "<string value>",
        "kinesis": {"retention_period": <int>,
                    "stream_mode": "PROVISIONED" or "ONDEMAND",
                    "shard_count": <int>,
        "lambda": {"name":'<string>',
                    "directory": "<string path to lambda package>",
                    "timeout": <int>,
                    "environment": {"REGION": "<string",
                                    "MAX_FILE_SIZE": '<string>'}
                    },
        "s3": {"notifications": {"key_filters": {"suffixes": <list of file extensions>}}
            }
        """
        super().__init__(scope, construct_id)

        # Check that props matches proper input structure
        # Imported props need to be checked apart
        KinesisProps(props["kinesis"])
        StackConfigProps(props)

        stack_name = self.node.try_get_context("stack_name").lower()
        stack_path = self.node.try_get_context("stack_path")
        logger.info("stack_path:%s", stack_path)
        region = Stack.of(self).region.lower()
        prefix = self.node.try_get_context("prefix").lower()
        stack_config = deepcopy(props)
        temp_prefix = stack_config["stack_extension"]

        ##############################
        # s3 Bucket
        ##############################
        s3_props = stack_config["s3"]  # S3 construct is doing nothing with notifications config
        var_bucket_name = f"{temp_prefix}-bucket"
        s3_props["bucket_name"] = var_bucket_name

        s3_bucket_landing = Guest360S3Bucket(self, var_bucket_name, region=region, props=s3_props)

        self.bucket = s3_bucket_landing.bucket
        stack_config["lambda_"]["environment"]["S3_BUCKET_NAME_LANDING"] = self.bucket.bucket_name

        ##############################
        # Kinesis Data Stream
        ##############################
        var_kinesis_stream_name = f"{temp_prefix}-stream"
        props = stack_config["kinesis"]
        props["stream_name"] = var_kinesis_stream_name

        # create kinesis datastream specific props
        datastream_props = deepcopy(props)

        g_kinesis_stream = Guest360KinesisDatastream(self, construct_id=var_kinesis_stream_name, props=datastream_props)

        self.stream = g_kinesis_stream.stream

        # Adding stream name explicitly since reference will return a Token to CDK, so downstream
        # stacks cannot leverage "self.kinesis_target_stream_name.stream_name" directly:
        self.kinesis_target_stream_name = self.stream.stream_name

        logger.debug("var_kinesis_stream_name: %s", self.stream.stream_name)

        #######################################################################################################
        # Lambda - IAM Role & Function
        #######################################################################################################

        var_lambda_function_name = LambdaFunctionName(prefix, temp_prefix).name()

        lambda_props = stack_config["lambda_"]

        lambda_props["environment"]["KINESIS_STREAM_NAME"] = self.stream.stream_name
        lambda_props["environment"]["STACK_NAME"] = stack_name

        lambda_props["code"] = aws_lambda.Code.from_asset(f"{stack_path}/{lambda_props['directory']}")

        self._invoker_lambda_function = aws_lambda.Function(
            self,
            var_lambda_function_name,
            function_name=var_lambda_function_name,
            code=lambda_props["code"],
            handler="main.handler",
            memory_size=5038,
            timeout=Duration.seconds(lambda_props["timeout"]),
            environment=lambda_props["environment"],
            runtime=aws_lambda.Runtime.PYTHON_3_9,
        )

        # grant bucket read access to lambda function
        self.bucket.grant_read(self._invoker_lambda_function)

        self.stream.grant_write(self._invoker_lambda_function)

        # Create trigger for Lambda function using suffix
        s3_notification = aws_s3_notifications.LambdaDestination(self._invoker_lambda_function)

        s3_notification.bind(self, self.bucket)

        suffixes = s3_props["notifications"]["key_filters"]["suffixes"]
        for suffix in suffixes:
            self.bucket.add_object_created_notification(
                s3_notification, aws_s3.NotificationKeyFilter(suffix=f".{suffix}")
            )

        ####################
        # NagSuppressions
        ###################
        NagSuppressions.add_resource_suppressions(
            self._invoker_lambda_function.role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                },
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok."},
            ],
            True,
        )
