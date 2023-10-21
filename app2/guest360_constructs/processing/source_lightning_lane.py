"""
Logic for Guest360's lighting pipeline processing
"""
import re
import os
from pathlib import Path

import aws_cdk
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.guest360_constructs.kinesis_datastream_processor import Guest360KinesisDatastreamProcessor
from app.guest360_constructs.lambda_function import LambdaFunctionProps, Guest360LambdaFunction
from app.guest360_constructs.sqs_queue import Guest360SQSQueue
from aws_cdk import Stack, aws_kinesis, aws_lambda, aws_logs
from cdk_nag import NagSuppressions


class SourceLightningLane(Construct360):
    """
    Construct for processing pipeline which reads from raw lightning lane sourcing kinesis data stream and writes into processing dynamodb table via lambda consumer.
    """

    def __init__(
        self,
        scope: aws_cdk.Stack,
        construct_id: str,
        lightning_lane_source_stream: aws_kinesis.IStream,
        profile_table: Guest360DynamodbGlobaltable,
        curated_events_table: Guest360DynamodbGlobaltable,
        identity_table: Guest360DynamodbGlobaltable,
        identity_nodes_table: Guest360DynamodbGlobaltable,
        identity_edges_table: Guest360DynamodbGlobaltable,
        environment_config: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stack_path = str(Path(os.getcwd()).parents[0])
        stack = Stack.of(self)

        environment = self.node.try_get_context("environment")
        is_static_env = self.node.try_get_context("is_static_env")
        prefix = self.node.try_get_context("prefix")

        stack = Stack.of(self)

        self.error_queue = Guest360SQSQueue(
            self,
            construct_id="deadletter-queue",
            props={
                "queue_name": f"{construct_id}-dlq",
                "encryption_key": None,
            },
        ).queue

        source_otel_lambda_layer = aws_lambda.LayerVersion.from_layer_version_arn(
            self, "lambda-layer", f"arn:aws:lambda:{stack.region}:901920570463:layer:aws-otel-python-amd64-ver-1-16-0:2"
        )

        source_lightning_lane_consumer_layers = [source_otel_lambda_layer] if environment not in ("local",) else []

        processing_lambda_environment = {
            "RAW_LL_STREAM_NAME": lightning_lane_source_stream.stream_name,
            "EXPERIENCE_EVENT_TABLE_NAME": curated_events_table.table.table_name,
            "IDENTITY_TABLE_NAME": identity_table.table.table_name,
            "PROFILE_TABLENAME": profile_table.table.table_name,
            "IDENTITY_NODES_TABLE_NAME": identity_nodes_table.table.table_name,
            "IDENTITY_EDGES_TABLE_NAME": identity_edges_table.table.table_name,
            "OPENTELEMETRY_COLLECTOR_CONFIG_FILE": "/var/task/otel-config.yaml",
            "AWS_LAMBDA_EXEC_WRAPPER": "/opt/otel-instrument",
        }

        function_name = str(re.sub(r"[^a-zA-Z0-9_-]", "", f"{lightning_lane_source_stream.stream_name}_consumer"))

        self.source_lightning_lane_consumer = Guest360LambdaFunction(
            self,
            "source_lightning_lane_consumer",
            LambdaFunctionProps(
                function_name=function_name,
                description="Reads from raw lightning lane sourcing kinesis data stream and writes into processing dynamodb table.",
                runtime=aws_lambda.Runtime.PYTHON_3_9,
                code=aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/processing/realtime/processing_realtime_lambda.zip"
                ),
                handler="processing_lambda.handler",
                allow_public_subnet=False,
                timeout=aws_cdk.Duration.seconds(60),
                environment=processing_lambda_environment,
                dead_letter_queue=self.error_queue,
                dead_letter_queue_enabled=True,
                profiling=environment != "local" and is_static_env,
                tracing=aws_lambda.Tracing.ACTIVE,
                log_retention=aws_logs.RetentionDays.ONE_DAY,
                layers=source_lightning_lane_consumer_layers,
                on_failure=aws_cdk.aws_lambda_destinations.SqsDestination(self.error_queue),
            ),
        ).function

        profile_table.table.grant_read_write_data(self.source_lightning_lane_consumer)
        curated_events_table.table.grant_read_write_data(self.source_lightning_lane_consumer)
        identity_table.table.grant_read_write_data(self.source_lightning_lane_consumer)
        identity_nodes_table.table.grant_read_write_data(self.source_lightning_lane_consumer)
        identity_edges_table.table.grant_read_write_data(self.source_lightning_lane_consumer)

        self.error_queue.grant_send_messages(self.source_lightning_lane_consumer)

        Guest360KinesisDatastreamProcessor(
            self,
            construct_id="ll-source-consumer-pipeline",
            source_stream=lightning_lane_source_stream,
            source_stream_consumer_lambda=self.source_lightning_lane_consumer,
            grant_read_write_tables=[
                curated_events_table,
                identity_table,
                profile_table,
                identity_nodes_table,
                identity_edges_table,
            ],
            environment_config=environment_config,
        )

        NagSuppressions.add_resource_suppressions(
            self.source_lightning_lane_consumer.role,
            [{"id": "AwsSolutions-IAM4", "reason": "Managed execution policy is ok."}],
        )

        NagSuppressions.add_resource_suppressions(
            self.source_lightning_lane_consumer.role.node.try_find_child("DefaultPolicy"),
            [{"id": "AwsSolutions-IAM5", "reason": "kms:GenerateDataKey* and kms:ReEncrypt* are ok"}],
        )

        NagSuppressions.add_resource_suppressions(
            self.error_queue,
            [
                {
                    "id": "AwsSolutions-SQS3",
                    "reason": "SQS Queue is actually a DLQ itself (for Kinesis stream).",
                }
            ],
        )
