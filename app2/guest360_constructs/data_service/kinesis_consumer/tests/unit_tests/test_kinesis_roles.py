"""
kinesis_consumer roles construct test
"""
import copy
import json
import logging
import os
import sys
from pathlib import Path

import aws_cdk
import pytest
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks

from app.guest360_constructs.data_service.kinesis_consumer.kinesis_consumer.roles import KinesisConsumerRoles
from app.src.reliability.utils import RoleName

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

directory = os.path.dirname(os.path.realpath(__file__))
stack_path = str(Path(os.getcwd()).parents[0])


class StackTest(aws_cdk.Stack):
    """
    create test stack in order to instantiate the aws construct
    """

    def __init__(self, scope, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, env=kwargs.get("env"))
        del kwargs["env"]
        self.node.set_context("prefix", "prefix")
        self.node.set_context("prefix_global", "prefix_global")
        kc_roles = KinesisConsumerRoles(
            self,
            construct_id,
            **kwargs,
        )
        assert kc_roles.roles is not None and len(kc_roles.roles) > 0


class TestKinesisConsumerRoles:
    """Test Class for Kinesis Consumer Roles"""

    config = {
        "stream_name": "consumer_test_stream",
        "role_configs": [
            {
                "id": "XAccountRoleTest1",
                "role_arns": [
                    "arn:aws:iam::111111111111:role/event-forwarder-data-role",
                    "arn:aws:iam::000000000000:role/event-forwarder-data-role",
                ],
            },
            {
                "id": "XAccountRoleTest2",
                "role_arns": [
                    "arn:aws:iam::111111111111:role/event-forwarder-data-role",
                    "arn:aws:iam::000000000000:role/event-forwarder-data-role",
                ],
            },
        ],
    }
    stack_name = "TestStack"
    region = "us-east-1"

    @pytest.fixture
    def stack_test(self):
        cdk_app = aws_cdk.App()
        aspects = aws_cdk.Aspects.of(cdk_app)
        aspects.add(AwsSolutionsChecks(verbose=True))
        # use cop.deepcopy create new object so original is kept intact
        stack_test = StackTest(
            cdk_app,
            self.stack_name,
            **copy.deepcopy(self.config),
            env=aws_cdk.Environment(account="0" * 12, region=self.region),
        )
        yield stack_test

    def test_instantiate_construct(self, stack_test):
        """
        create dummy aws_cdk app and instantiate the StackTest with construct
        """
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(json.dumps(template.to_json(), indent=2))

        template.find_resources("AWS::IAM::Policy").keys()
        # ensure all role policy id's are created with proper policies
        # test for expected policy without dynamic resource cloudformation lookups
        # read for stream.grant_read should produce first 2 statements
        # manually add actions using stream.grant() for kcl should generate the rest
        template.has_resource_properties(
            "AWS::IAM::Role",
            {
                "RoleName": RoleName(
                    "prefix_global", f'{self.config["stream_name"]}_{self.config["role_configs"][0]["id"]}'
                ).name()
            },
        )
        template.has_resource_properties(
            "AWS::IAM::Role",
            {
                "RoleName": RoleName(
                    "prefix_global", f'{self.config["stream_name"]}_{self.config["role_configs"][1]["id"]}'
                ).name()
            },
        )

        # validate that template does not contain any nag rules
        annotations = Annotations.from_stack(stack_test)
        errors = annotations.find_error(
            "*",
            Match.string_like_regexp(r"AwsSolutions-.*"),
        )
        assert len(errors) == 0
