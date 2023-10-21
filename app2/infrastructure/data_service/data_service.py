""" data service aws stack based infrastructure resources"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
import importlib
import logging
import os
import sys
from pathlib import Path
from typing import cast

import yaml
from aws_cdk import Stack, aws_apigateway, aws_lambda
from cdk_nag import NagSuppressions

from app.guest360_constructs.api_gateway import Guest360APIGateway, Guest360APIGatewayProps
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.data_service.experience_api import ExperienceApiLambda, ExperienceRestAPILambdaEnvironment
from app.guest360_constructs.data_service.lambda_authorizer.lambda_authorizer import LambdaAuthorizer
from app.guest360_constructs.data_service.lambda_authorizer.scope_map_dynamodb import ScopeMapDynamoDB
from app.guest360_constructs.data_service.snowflake.cdk.static_resources.static_resources import StaticResources
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.guest360_constructs.identity.identity_graph import IdentityGraph
from app.guest360_constructs.identity.keyring_table import KeyringTable
from app.guest360_constructs.kinesis_firehose import Guest360KinesisFirehose
from app.infrastructure.data_service.kinesis_consumers import Consumer
from app.infrastructure.identity.identity import Identity
from app.infrastructure.ingestion.ingestion import Ingestion
from app.infrastructure.processing.processing import Processing
from app.infrastructure.reliability.enable_stack import DeployFlag
from app.infrastructure.workstream_stack import WorkstreamStack
from app.src.reliability.utils import StackName

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class DataService(WorkstreamStack):
    """Data Service cloudformation stack"""

    @property
    def kinesis_consumer_stacks(self):
        return []
        # return self._kinesis_consumer_stacks

    @property
    def s3_consumers(self):
        return []
        # return self._s3_consumers

    def __init__(
        self,
        scope: Stack,
        construct_id: str,
        environment_config: dict,
        # identity_stack: Identity,
        # ingestion_stack: Ingestion,
        # processing_stack: Processing,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        return None

        environment = self.node.try_get_context("environment")
        stack = Stack.of(self)
        processing_stack_name = processing_stack.stack_name
        project_path = self.project_dir
        prefix = self.node.try_get_context("prefix")

        # import here due to dynamic environment from context
        snowflake_static_resources_configs = importlib.import_module(
            f"app.infrastructure.data_service.configs.snowflake_static_resources.{environment}"
        )

        """
        Data Services
        """

        directory = os.path.dirname(os.path.realpath(__file__))

        #####
        # snowflake static resources
        #####
        for config in snowflake_static_resources_configs.get_configs():
            bucket_info = self.get_ingestion_bucket(
                ingestion_stack.s3_buckets, config["external_stage"]["s3_bucket_name"]
            )
            if bucket_info is None:
                raise ValueError("Failed to find required s3_bucket for snowpipe")
            config["external_stage"]["s3_bucket"] = bucket_info["bucket"]
            config["external_stage"]["s3_bucket_name"] = bucket_info["bucket_full_name"]
            StaticResources(self, config["static_resources_name"], props=config)

        #########################################
        # kinesis consumers (streaming events):
        #########################################
        with open(
            f"{directory}/configs/kinesis_consumers/{environment}.yaml",
            "r",
            encoding="UTF-8",
        ) as config_yaml:
            stream_types = yaml.unsafe_load(config_yaml)
        self._kinesis_consumer_stacks = {}
        for data_services_config in stream_types:
            stream_type = data_services_config["stream_props"]["stream_name"].title()
            stack_name = StackName(prefix, f"DS-{stream_type}").name()
            if DeployFlag.is_stack_enabled(self, "DataService/Consumer"):
                kinesis_consumer_stack = Consumer(
                    self,
                    stream_type,
                    stack_name=stack_name,
                    data_services_config=data_services_config,
                    environment_config=environment_config,
                    event_source_streams=processing_stack.stack_export_streams,  # Circular Dependency
                    # event_source_streams={
                    #     "curated-experiences-stream": aws_kinesis.Stream.from_stream_arn(
                    #         self,
                    #         "curated_experiences_stream",
                    #         self.ssm_import("curated-experiences-stream", processing_stack_name),
                    #     )
                    # },
                    tags=stack.tags.tag_values(),
                    termination_protection=environment == "prod",
                )
                # stack dependencies to not propagate down to lower stacks
                # Need to ensure dataservice stack is complete (and thereby processing so source streams are created)
                # kinesis_consumer_stack.add_dependency(self)
                self._kinesis_consumer_stacks[stack_name] = kinesis_consumer_stack

        #########################################
        # s3 consumers (snowflake):
        #########################################
        self._s3_consumers = {}
        with open(
            f"{directory}/configs/s3_consumers/{environment}.yaml",
            "r",
            encoding="UTF-8",
        ) as config_yaml:
            s3_types = yaml.unsafe_load(config_yaml)
        for s3_type in s3_types:
            logger.debug(f"{s3_type=}")
            bucket_name = s3_type["KinesisFirehoseProps"]["bucket_name"]
            stream_name = s3_type["kinesis_source"]["stream_name"]
            bucket_info = self.get_ingestion_bucket(ingestion_stack.s3_buckets, bucket_name)
            if bucket_info is None:
                raise ValueError(f"Failed to find required s3_bucket for firehose delivery {bucket_name}")
            source_stream = processing_stack.stack_export_streams.get(stream_name)
            if source_stream is None:
                raise ValueError(f"Failed to find required processing stack stream {stream_name}")

            props = s3_type["KinesisFirehoseProps"]
            props["bucket_name"] = bucket_info["bucket_full_name"]
            props["bucket"] = bucket_info["bucket"]
            props["kinesis_stream"] = source_stream
            props["data_transformation"]["lambda_properties"]["code"] = aws_lambda.Code.from_asset(
                f'{project_path}/{props["data_transformation"]["lambda_properties"]["code"]}'
            )
            props["data_transformation"]["lambda_properties"]["runtime"] = aws_lambda.Runtime(
                props["data_transformation"]["lambda_properties"]["runtime"]
            )
            logger.debug(f"{props=}")
            firehose = Guest360KinesisFirehose(self, s3_type["s3_consumer"]["name"], props)
            self._s3_consumers[firehose.firehose_name] = firehose.firehose_name

        #########################################
        # APIs:
        #########################################

        # Authorizer:
        config_root = f"{directory}/../../src/data_service/api_authorizers/configs"
        try:
            with open(f"{config_root}/{environment}-authorizer.yaml", "r", encoding="utf-8") as authorizer_config_yaml:
                authorizer_config = yaml.safe_load(authorizer_config_yaml)
        except FileNotFoundError:
            with open(f"{config_root}/default-authorizer.yaml", "r", encoding="utf-8") as authorizer_config_yaml:
                authorizer_config = yaml.safe_load(authorizer_config_yaml)

        directory = os.path.dirname(os.path.realpath(__file__))

        authz_validate_url = authorizer_config["authz_validate_url"]

        scope_map_table = ScopeMapDynamoDB(
            self,
            construct_id="scope-map-dynamodb-construct",
            stack_path=project_path,
            stack_prefix=prefix,
            lambda_environment={
                "AUTHZ_VALIDATE_URL": authz_validate_url,
            },
        ).scopes_map_dynamodb

        authorizer_lambda = LambdaAuthorizer(
            self,
            construct_id="authorizer-lambda-construct",
            stack_path=project_path,
            stack_prefix=prefix,
            lambda_environment={
                "AUTHZ_VALIDATE_URL": authz_validate_url,
                "SCOPE_MAP_TABLE_NAME": scope_map_table.table.table_name,
            },
        ).authorizer_lambda

        scope_map_table.table.grant_read_data(authorizer_lambda)
        identity_stack_name = identity_stack.stack_name

        keyring_table = KeyringTable.from_ssm(cast(Construct360, self), "keyring_table", identity_stack_name)

        identity_graph = IdentityGraph.from_ssm(cast(Construct360, self), "identity_graph", identity_stack_name)

        identity_notification_stream = keyring_table.kinesis_stream.stream

        curated_experience_events_table = Guest360DynamodbGlobaltable.from_ssm(
            self, "curated_experience_events_table", processing_stack_name, "curated_experience_events_table"
        )

        profile_table = Guest360DynamodbGlobaltable.from_ssm(
            self,
            "profile_table",
            processing_stack.stack_name,
            "profile_table",
        )

        # Experience API Lambda:
        experience_api_lambda_environment: ExperienceRestAPILambdaEnvironment = {
            "EXPERIENCE_EVENT_TABLE_NAME": curated_experience_events_table.table.table_name,
            "IDENTITY_TABLE_NAME": keyring_table.global_table.table.table_name,
            "IDENTITY_NODES_TABLE_NAME": identity_graph.node_global_table.table.table_name,
            "IDENTITY_EDGES_TABLE_NAME": identity_graph.edge_global_table.table.table_name,
            "PROFILE_TABLENAME": profile_table.table.table_name,
            "IDENTITY_NOTIFICATION_STREAM_NAME": identity_notification_stream.stream_name,
        }
        experiences_api = ExperienceApiLambda(
            self,
            construct_id="experience-api-construct",
            stack_prefix=prefix,
            lambda_environment=experience_api_lambda_environment,
        ).experiences_api_lambda

        # Experience API needs read access to each of the dynamodb tables:
        curated_experience_events_table.table.grant_read_data(experiences_api)
        keyring_table.global_table.table.grant_read_data(experiences_api)
        profile_table.table.grant_read_data(experiences_api)

        NagSuppressions.add_stack_suppressions(
            self,
            [
                {"id": "AwsSolutions-IAM5", "reason": "CDK lambda ScopeMapProvider"},
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok for ScopeMapProvider"},
                {"id": "AwsSolutions-L1", "reason": "Using a specific version of Runtime."},
            ],
        )

        api_lambda_arn = experiences_api.function_arn
        authorizer_lambda_arn = authorizer_lambda.function_arn

        props: Guest360APIGatewayProps = {
            "method_props": [
                {
                    "path": "/api/v1/experiences",
                    "method": "get",
                    "api_lambda": api_lambda_arn,
                    "credentials": {"enabled": True, "authorizer_lambda_arn": authorizer_lambda_arn},
                }
            ],
            "api_log_level": aws_apigateway.MethodLoggingLevel.INFO,
            "swagger_path": f"{project_path}/docs/workstreams/services/openapi.yaml",
        }

        NagSuppressions.add_resource_suppressions(
            experiences_api,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Grant Write creates wildcard policy to allow dynamodb index wildcards.",
                }
            ],
            True,
        )

        Guest360APIGateway(
            self,
            construct_id="api-gateway-guest360construct",
            environment_config=environment_config,
            props=props,
        )

    @staticmethod
    def get_ingestion_bucket(ingestion_s3_buckets: list, bucket_name: str) -> dict:
        """find the ingestion bucket exported objects that match the bucket name in the config"""
        bucket_info = next(
            (bucket_dict for bucket_dict in ingestion_s3_buckets if bucket_dict["bucket_name"] == bucket_name),
            None,
        )
        logger.debug(f"{bucket_info=}")
        return bucket_info
