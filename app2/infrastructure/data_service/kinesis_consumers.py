import logging
import os
import sys

from aws_cdk import Stack, aws_iam
from cdk_nag import NagSuppressions
from pathlib import Path
import app.guest360_constructs.iam_role as iam_role
import aws_cdk
import yaml

from app.guest360_constructs.construct_360 import Construct360
from app.infrastructure.data_service.kinesis_consumers_roles import ConsumerRoles
from app.infrastructure.workstream_stack import WorkstreamStack
from app.src.reliability.utils import StackName
from app.guest360_constructs.data_service.kinesis_consumer.kinesis_consumer.consumer import (
    KinesisConsumerStream,
)

# logger = logging.getLogger(__name__)
# streamHandler = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# streamHandler.setFormatter(formatter)
# logger.addHandler(streamHandler)


class Consumer(WorkstreamStack):
    def __init__(
        self,
        scope: Construct360 | Stack,
        id: str,
        environment_config: dict,
        data_services_config: dict,
        event_source_streams: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # ENVIRONMENT_NAME = self.node.try_get_context("environment")
        stack = Stack.of(self)
        stack_name = self.node.try_get_context("stack_name")
        environment = self.node.try_get_context("environment")
        prefix = self.node.try_get_context("prefix")
        prefix_global = self.node.try_get_context("prefix_global")
        stack_path = str(Path(os.getcwd()).parents[0])

        # prepend stack_path to code_path
        # stack_path needs to be prepended here otherwise in construct it is duped
        data_services_config["lambda_producer_props"][
            "code_path"
        ] = f'{stack_path}/{data_services_config["lambda_producer_props"]["code_path"]}'

        stream_type = data_services_config["stream_props"]["stream_name"].title()
        if stack.region == "us-east-1":
            """
            With roles being global
            Only instantiate stack to create kinesis consumer roles if region is us-east-1
            """
            kinesis_consumer_roles = ConsumerRoles(
                self,
                f"{stream_type}Roles",
                stack_name=StackName(prefix, f"DS-{stream_type}Roles").name(),
                environment_config=environment_config,
                role_configs=data_services_config.get("role_configs", []),
                stream_name=data_services_config["stream_props"]["stream_name"],
                tags=stack.tags.tag_values(),
                termination_protection=environment == "prod",
            )

        data_services_config["event_source_props"]["stream"] = event_source_streams.get(
            data_services_config["event_source_props"]["stream_name"]
        )
        del data_services_config["event_source_props"]["stream_name"]

        self.kinesis_experiences_consumer = KinesisConsumerStream(
            self,
            f"{stream_type}Kinesis",
            stream_props=data_services_config["stream_props"],
            role_configs=data_services_config.get("role_configs", []),
            lambda_producer_props=data_services_config["lambda_producer_props"],
            event_source_props=data_services_config["event_source_props"],
        )

        if environment in ["local", "pra", "latest"] and stack.region == "us-east-1":
            self.kinesis_experiences_consumer.node.add_dependency(kinesis_consumer_roles)
