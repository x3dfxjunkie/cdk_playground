import os
import sys

import aws_cdk
import yaml
from aws_cdk import Stack, aws_iam
from cdk_nag import NagSuppressions

import app.guest360_constructs.iam_role as iam_role
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.data_service.kinesis_consumer.kinesis_consumer.roles import KinesisConsumerRoles


class ConsumerRoles(Stack):
    def __init__(self, scope: Construct360, id: str, environment_config: dict, stream_name: str, role_configs: list, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        return None

        # ENVIRONMENT_NAME = self.node.try_get_context("environment")
        stack = Stack.of(self)
        stack_name = self.node.try_get_context("stack_name")
        environment = self.node.try_get_context("environment")
        prefix = self.node.try_get_context("prefix")
        prefix_global = self.node.try_get_context("prefix_global")

        experiences_roles = KinesisConsumerRoles(self, f"{stream_name.title()}ExperiencesRoles", stream_name=stream_name, role_configs=role_configs)
