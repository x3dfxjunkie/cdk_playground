import json
import logging
import sys

import aws_cdk
import pytest
from aws_cdk import aws_kinesis
from aws_cdk.assertions import Template
from app.guest360_constructs.construct_360 import Construct360

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class FooStack(aws_cdk.Stack):
    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        prefix: str,
        prefix_resource_name: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.node.set_context("prefix", prefix)
        bar_stack = BarStack(self, "BarStack", prefix_resource_name)


class BarStack(aws_cdk.Stack):
    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        prefix_resource_name: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        prefix = self.node.try_get_context("prefix")
        kinesis = aws_kinesis.Stream(self, "BarKinesis", stream_name=f"{prefix}-{prefix_resource_name}")


class TestGuest360App:
    prefix = "MyPrefix"
    prefix_resource_name = "FooBar"

    def test_contest_prefix_set_for_resource_name(self):
        app = aws_cdk.App()
        # create root stack
        foo_stack = FooStack(app, "FooStack", prefix=self.prefix, prefix_resource_name=self.prefix_resource_name)
        template = Template.from_stack(foo_stack.node.find_child("BarStack"))
        logger.info(json.dumps(template.to_json(), indent=2))
        template.has_resource_properties(
            "AWS::Kinesis::Stream",
            {
                "Name": f"{self.prefix}-{self.prefix_resource_name}",
            },
        )
