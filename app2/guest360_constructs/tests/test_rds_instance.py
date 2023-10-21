"""Class for test the RDS Instance constructor"""
import logging
import os
import sys

import aws_cdk
import pytest
import yaml
from aws_cdk import assertions

from app.guest360_constructs.rds_instance import Guest360RDSInstance

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class TestRDSInstance:
    """Class for test the RDS Instance constructor"""

    stack_id = "TestStack"

    @pytest.mark.timeout(30, method="signal")
    def test_rds_instance_creation(self):
        test_app = aws_cdk.App()
        stack = aws_cdk.Stack(test_app, self.stack_id, env=aws_cdk.Environment(account="123456789", region="us-east-1"))
        stack.node.set_context("environment", "local")
        stack.node.set_context("prefix", "test-prefix-use1")
        stack.node.set_context("prefix_global", "test-prefix")
        stack.node.set_context("region", "us-east-1")

        environment = stack.node.try_get_context("environment")
        rds_props = {
            "engine": aws_cdk.aws_rds.DatabaseInstanceEngine.MARIADB,
            "database_name": "dbloadtesting",
            "iam_authentication": True,
        }

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(
            f"{os.path.abspath(os.path.join(dir_path, '../../../app'))}/configs/{environment}-environment.yaml",
            "r",
            encoding="utf-8",
        ) as file:
            environment_config = yaml.safe_load(file)

        Guest360RDSInstance(stack, "test_rds_instance", environment_config=environment_config, props=rds_props)

        template = assertions.Template.from_stack(stack)
        template.resource_count_is("AWS::RDS::DBInstance", 1)
        template.has_resource_properties(
            "AWS::RDS::DBInstance",
            {
                "AllocatedStorage": "100",
                "CopyTagsToSnapshot": True,
                "DBInstanceClass": "db.m5.large",
                "DBName": "dbloadtesting",
            },
        )
