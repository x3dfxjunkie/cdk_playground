"""test for dms replication instance construct
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
import json
import logging
import sys

import aws_cdk
import pytest
from aws_cdk import assertions

from app.guest360_constructs.ingestion.dms.dms_replication_instance import Guest360DMSReplication

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class TestReplicationInstance:
    """Test class for DMS Replication Instance Construct"""

    stack_id = "TestStack"

    @pytest.mark.timeout(30, method="signal")
    def test_replication_instance_created(self):
        test_app = aws_cdk.App()
        stack = aws_cdk.Stack(test_app, self.stack_id, env=aws_cdk.Environment(account="123456789", region="us-east-1"))
        stack.node.set_context("environment", "local")
        stack.node.set_context("prefix", "lst-use1-guest360")
        stack.node.set_context("prefix_global", "test-prefix")
        stack.node.set_context("region", "us-east-1")

        subnet_props = {
            "group_name": "my_test_group",
            "description": "subnet group for dms test",
            "subnet_list": ["subnet-abc123456789efghi", "subnet-123456789abcefghi"],
            "subnet_identifer": "my_subnet_identifier",
        }

        props = {
            "name": "dms_test",
            "instance_class": "dms.t2.micro",
            "storage": 10,
            "engine_version": "3.4.6",
            "auto_minor_version_upgrade": False,
            "allow_major_version_upgrade": True,
            "multi_az": True,
            "maint_window": "Mon:00:00-Mon:01:00",
            "instance_identifier": "mytestinstance",
            "security_group_ids": ["sg-abc123456789efghi", "sg-123456789abcefghi"],
            "subnet_props": subnet_props,
        }

        instance = Guest360DMSReplication(stack, "test-replication-instance", props)
        logger.debug(f"{instance.dms_replication_instance_name=}")
        assert instance.dms_replication_instance_name == "lst-use1-g360-dms_test"

        template = assertions.Template.from_stack(stack)

        logger.debug(json.dumps(template.to_json(), indent=2))

        template.resource_count_is("AWS::DMS::ReplicationInstance", 1)
