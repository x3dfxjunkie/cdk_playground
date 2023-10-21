"""kinesis_consumer consumer construct tests
"""
import copy
import yaml
import logging
import os
import re
import sys
from pathlib import Path

import pytest
from app.guest360_constructs.data_service.kinesis_consumer.kinesis_consumer.consumer import KinesisConsumerStream
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from aws_cdk import App, Aspects, Duration, Environment, Stack, aws_kinesis
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

directory = os.path.dirname(os.path.realpath(__file__))
stack_path = str(Path(os.getcwd()).parents[0])


class StackTest(Stack):
    """
    create test stack in order to instantiate the aws construct
    """

    def __init__(self, scope, construct_id: str, configs: list, **kwargs) -> None:
        super().__init__(scope, construct_id, env=kwargs.get("env"))
        self.node.set_context("prefix", "prefix_test")
        self.node.set_context("prefix_global", "prefix_global_test")
        self.node.set_context("environment", "prod")

        self.props = {
            "retention_period": Duration.hours(24),
            "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
        }

        for config in configs:
            config["lambda_producer_props"]["code_path"] = f'{directory}/{config["lambda_producer_props"]["code_path"]}'

            stream = Guest360KinesisDatastream(
                self,
                construct_id=f'SourceStream-{config["stream_props"]["stream_name"]}',
                props=self.props,
            ).stream

            config["event_source_props"]["stream"] = stream
            KinesisConsumerStream(
                self,
                f'{config["stream_props"]["stream_name"]}',
                **config,
            )


class TestKinesisConsumer:
    """Guest360 Test Kinesis Consumer"""

    region = "us-east-1"
    configs = [
        {
            "stream_props": {
                "stream_name": "consumer_test_stream",
                "retention_period": Duration.days(7),
                "stream_mode": aws_kinesis.StreamMode("PROVISIONED"),
                "shard_count": 1,
            },
            "lambda_producer_props": {
                "runtime": "PYTHON_3_9",
                "code_path": "../../kinesis_consumer/",
                "timeout": Duration.seconds(180),
                "handler": "producer.lambda_handler",
                "environment": {},
            },
            "event_source_props": {
                "starting_position": "LATEST",
                "max_batching_window": 300,
            },
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
        },
        {
            "stream_props": {
                "stream_name": "consumer_test_stream_2",
                "retention_period": Duration.days(7),
                "stream_mode": aws_kinesis.StreamMode("PROVISIONED"),
                "shard_count": 1,
            },
            "lambda_producer_props": {
                "runtime": "PYTHON_3_9",
                "code_path": "../../kinesis_consumer/",
                "timeout": Duration.seconds(180),
                "handler": "producer.lambda_handler",
                "environment": {},
            },
            "event_source_props": {
                "max_batching_window": 300,
            },
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
        },
    ]
    stack_name = "mystackprefix-TestStack"

    @pytest.fixture
    def stack_test(self):
        cdk_app = App()
        aspects = Aspects.of(cdk_app)
        aspects.add(AwsSolutionsChecks(verbose=True))
        # use cop.deepcopy create new object so original is kept intact
        stack_test = StackTest(
            cdk_app,
            self.stack_name,
            configs=copy.deepcopy(self.configs),
            env=Environment(account="0" * 12, region=self.region),
        )
        yield stack_test

    def test_instantiate_construct(self, stack_test):
        """
        create dummy aws_cdk app and instantiate the StackTest with construct
        """
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        iam_policy_ids = template.find_resources("AWS::IAM::Policy").keys()
        for config in self.configs:
            # ensure all role policy id's are created with proper policies
            for _ in config["role_configs"]:
                # consumerteststreamprefixglobaltestuseast1XAccountRoleTest1rolePolicyF9277039
                # validate policyid is formed correctly <stackname><region><roleid>Policy.replace('_', '')
                regexstr = "KinesisConsumerStream.*Role.*Policy.*"
                regexstr = regexstr.replace("_", "").replace("-", "")
                # logger.debug(f'{regexstr=}')
                assert any((match := re.match(regexstr, iam_policy)) for iam_policy in iam_policy_ids)

                # test for expected policy without dynamic resource cloudformation lookups
                # read for stream.grant_read should produce first 2 statements
                # manually add actions using stream.grant() for kcl should generate the rest
                logger.info("{match.group(0)= %s}", match.group(0))
                template.has_resource_properties(
                    "AWS::IAM::Policy",
                    {
                        "PolicyName": match.group(0),
                    },
                )

        # validate that template does not contain any nag rules
        annotations = Annotations.from_stack(stack_test)
        errors = annotations.find_error(
            "*",
            Match.string_like_regexp(r"AwsSolutions-.*"),
        )
        assert len(errors) == 0
