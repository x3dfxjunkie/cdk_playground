"""Processing Guest360 Construct
"""
import logging
import os
from pathlib import Path
import sys
from typing import Dict, cast

import aws_cdk.aws_dynamodb as dynamodb
import yaml
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.guest360_constructs.identity.identity_graph import IdentityGraph
from app.guest360_constructs.identity.keyring_table import KeyringTable
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from app.guest360_constructs.processing.analytics_datalake import AnalyticsDatalake
from app.guest360_constructs.processing.source_lightning_lane import SourceLightningLane
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from app.infrastructure.identity.identity import Identity
from app.infrastructure.ingestion.ingestion import Ingestion
from app.infrastructure.workstream_stack import WorkstreamStack
from aws_cdk import CfnElement, aws_kinesis, aws_s3_deployment, aws_iam, Stack, Fn
from cdk_nag import NagSuppressions
import zipfile

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Processing | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class Processing(WorkstreamStack):
    """Stack for managing the processing infrastructure"""

    @property
    def stack_export_streams(self):
        return []
        # return self._stack_export_streams

    def __init__(
        self,
        scope: Stack,
        construct_id: str,
        environment_config: dict,
        # identity_stack: Identity,
        # ingestion_stack: Ingestion,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)  # type: ignore
        return None

        stack = Stack.of(self)

        stack_path = str(Path(os.getcwd()).parents[0])

        identity_stack_name = identity_stack.stack_name

        keyring_table = KeyringTable.from_ssm(cast(Construct360, self), "keyring_table", identity_stack_name)

        keyring_table_stream = keyring_table.kinesis_stream

        analytics_datalake = AnalyticsDatalake(
            cast(Construct360, self),
            "analytics_datalake",
            {
                "targets": [
                    {
                        "stream": keyring_table_stream.stream,
                        "partitioning": "keyring/date=!{partitionKeyFromLambda:year}-!{partitionKeyFromLambda:month}-!{partitionKeyFromLambda:day}/",
                    }
                ]
            },
        )

        identity_graph = IdentityGraph.from_ssm(cast(Construct360, self), "identity_graph", identity_stack_name)

        identity_nodes_table = identity_graph.node_global_table

        identity_nodes_table_stream = identity_graph.node_table_stream.kinesis_stream

        identity_edges_table = identity_graph.edge_global_table

        identity_edge_table_stream = identity_graph.edge_table_stream.kinesis_stream

        analytics_datalake.add_target(
            {
                "stream": identity_nodes_table_stream,
                "partitioning": "nodes/date=!{partitionKeyFromLambda:year}-!{partitionKeyFromLambda:month}-!{partitionKeyFromLambda:day}/",
            }
        )

        analytics_datalake.add_target(
            {
                "stream": identity_edge_table_stream,
                "partitioning": "edges/date=!{partitionKeyFromLambda:year}-!{partitionKeyFromLambda:month}-!{partitionKeyFromLambda:day}/",
            }
        )

        environment = self.node.try_get_context("environment")

        self._stack_export_streams: Dict[str, aws_kinesis.IStream] = {}  # streams to export

        directory = os.path.dirname(os.path.realpath(__file__))
        try:
            with open(
                f"{directory}/configs/{environment}-processing.yaml",
                "r",
                encoding="utf-8",
            ) as processing_config_yaml:
                processing_config = yaml.unsafe_load(processing_config_yaml)
        except FileNotFoundError:
            with open(f"{directory}/configs/local-processing.yaml", "r", encoding="utf-8") as processing_config_yaml:
                processing_config = yaml.unsafe_load(processing_config_yaml)

        # Events dynamodb table to place curated events (output stream into services):
        profile_table_name = processing_config["profile_table_name"]

        # Events dynamodb table to place curated events (output stream into services):
        curated_experience_events_table_name = processing_config["curated_experience_events_table_name"]

        # Events stream where dynamodb change data capture flows into (output stream into services):
        curated_experience_events_stream_name: str = processing_config["curated_experience_events_stream_name"]

        # Define props from the parsed yaml {environment}-processing.yaml
        props = processing_config["kinesis"]

        # Create dynamodb table where events will be persisted for data services pipeline to pickup from:
        self.curated_experience_events_stream = Guest360KinesisDatastream(
            self, construct_id=curated_experience_events_stream_name, props=props  # type:ignore
        ).stream
        self._stack_export_streams[curated_experience_events_stream_name] = self.curated_experience_events_stream

        self.profile_table = Guest360DynamodbGlobaltable(
            self,  # type:ignore
            construct_id=profile_table_name,
            table_name=profile_table_name,
            partition_key=dynamodb.Attribute(name="atomic_id", type=dynamodb.AttributeType.STRING),
        )

        self.profile_table.export_ssm("profile_table")

        self.curated_experience_events_table = Guest360DynamodbGlobaltable(
            self,  # type:ignore
            construct_id=curated_experience_events_table_name,
            table_name=curated_experience_events_table_name,
            partition_key=dynamodb.Attribute(name="atomic_id#event_name", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="event_time", type=dynamodb.AttributeType.NUMBER),
            kinesis_stream=self.curated_experience_events_stream,
        )

        self.curated_experience_events_table.export_ssm("curated_experience_events_table")

        # Stack for pipeline which reads from source/raw LL data and writes it to processing
        #  dynamodb curated events table.
        # TODO - Instead of using "lightning-lane" in name match, leverage config file with experience types.
        #  This should probably be in the ingestion side when kinesis stream is instantiated.
        lightning_lane_source_streams = [
            source_stream
            for source_stream in ingestion_stack.streams
            if "lightning-lane" in source_stream["stream_name"]  # type:ignore
        ]
        for stream in lightning_lane_source_streams:
            SourceLightningLane(
                self,
                f'{stream["stream_name"]}-processor',  # type:ignore
                lightning_lane_source_stream=stream["stream"],  # type:ignore
                profile_table=self.profile_table,
                curated_events_table=self.curated_experience_events_table,
                identity_table=keyring_table.global_table,
                identity_nodes_table=identity_nodes_table,
                identity_edges_table=identity_edges_table,
                environment_config=environment_config,
            )

        if environment != "prod":
            keyring_table.global_table.table.grant_read_write_data(analytics_datalake.analysis_role.role)
            identity_graph.edge_global_table.table.grant_read_write_data(analytics_datalake.analysis_role.role)
            identity_graph.node_global_table.table.grant_read_write_data(analytics_datalake.analysis_role.role)
        else:
            # Only allow read permissions in prod
            keyring_table.global_table.table.grant_read_data(analytics_datalake.analysis_role.role)
            identity_graph.edge_global_table.table.grant_read_data(analytics_datalake.analysis_role.role)
            identity_graph.node_global_table.table.grant_read_data(analytics_datalake.analysis_role.role)

        dependency_bucket = Guest360S3Bucket(
            cast(Construct360, self),
            "dependency_bucket",
            stack.region,
            {
                "bucket_name": f"{stack.stack_name}-analytics-dependency-bucket",
            },
        )
        managed_policy_reason = "Managed Policies are okay"

        if False:  # pylint: disable=using-constant-test
            # TODO: figure this out - currently causing problems with our releases
            # Error: Cannot find asset at /codebuild/output/src2136504384/src/bazel-bin/app.zip
            app_code_asset = aws_s3_deployment.Source.asset(f"{stack_path}/bazel-bin/app.zip")

            app_code_s3_prefix = "app_code/"

            app_code_deployment = aws_s3_deployment.BucketDeployment(
                self,
                "app_code_deployment",
                sources=[app_code_asset],
                destination_bucket=dependency_bucket.bucket,
                destination_key_prefix=app_code_s3_prefix,
                extract=False,
            )

            requirements_zip_directory = f"{stack_path}/bazel-bin/requirements.zip"

            requirements_asset = aws_s3_deployment.Source.asset(requirements_zip_directory)

            requirements_asset_prefix = "requirements/"

            requirements_s3_deployment = aws_s3_deployment.BucketDeployment(
                self,
                "requirements_deployment",
                sources=[requirements_asset],
                destination_bucket=dependency_bucket.bucket,
                destination_key_prefix=requirements_asset_prefix,
            )

            app_code_uri = f"s3://{app_code_deployment.deployed_bucket.bucket_name}/{app_code_s3_prefix}{Fn.select(0, app_code_deployment.object_keys)}"

            with zipfile.ZipFile(requirements_zip_directory) as archived_file:
                requirements_file_name = archived_file.infolist()[0].filename

            requirements_uri = f"s3://{requirements_s3_deployment.deployed_bucket.bucket_name}/{requirements_asset_prefix}{requirements_file_name}"

            dependency_bucket.bucket.grant_read(analytics_datalake.analysis_role.role)

            dependency_bucket.kms_key.add_to_resource_policy(
                aws_iam.PolicyStatement(
                    actions=["kms:Decrypt", "kms:DescribeKey"],
                    principals=[aws_iam.ArnPrincipal(analytics_datalake.analysis_role.role.role_arn)],
                    effect=aws_iam.Effect.ALLOW,
                    resources=["*"],
                )
            )

            self.ssm_export("analysis_role", analytics_datalake.analysis_role.role.role_arn)
            self.ssm_export("app_code", app_code_uri)
            self.ssm_export("requirements_whl", requirements_uri)
            NagSuppressions.add_resource_suppressions(
                [
                    child
                    for child in self.node.children
                    if child.node.default_child
                    and "CDKBucketDeployment" in self.resolve(cast(CfnElement, child.node.default_child).logical_id)
                ][0],
                [
                    {"id": "AwsSolutions-IAM4", "reason": managed_policy_reason},
                    {"id": "AwsSolutions-IAM5", "reason": "Okay for Log Retention"},
                ],
                apply_to_children=True,
            )

        log_retention_node = next(
            iter(
                [
                    child
                    for child in self.node.children
                    if child.node.default_child
                    and "LogRetention" in self.resolve(cast(CfnElement, child.node.default_child).logical_id)
                ]
            ),
            None,
        )

        if log_retention_node is not None:
            NagSuppressions.add_resource_suppressions(
                log_retention_node,
                [
                    {"id": "AwsSolutions-IAM4", "reason": managed_policy_reason},
                    {"id": "AwsSolutions-IAM5", "reason": "Okay for Log Retention"},
                ],
                apply_to_children=True,
            )

        self.ssm_export(
            "curated-experiences-stream",
            self._stack_export_streams[curated_experience_events_stream_name].stream_arn,
        )

        for child in self.node.children:
            if child.node.default_child and "BucketNotificationsHandler" in self.resolve(
                cast(CfnElement, child.node.default_child).logical_id
            ):
                NagSuppressions.add_resource_suppressions(
                    child,
                    [
                        {"id": "AwsSolutions-IAM4", "reason": managed_policy_reason},
                        {"id": "AwsSolutions-IAM5", "reason": "Okay for bucket notification handler"},
                    ],
                    apply_to_children=True,
                )
